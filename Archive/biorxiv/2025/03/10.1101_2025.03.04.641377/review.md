## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, supplementary notes) as provided
- **Assessment boundary** Scientific validity, technical soundness, clarity of claims, and adequacy of evidence based solely on the supplied material
- **Shared manuscript claim summary** The authors propose DynamicGT, a geometric transformer model that integrates conformational dynamics (from MD simulations and AlphaFlow-generated ensembles) into a cooperative graph neural network to predict protein binding interfaces, with claimed improvements in flexible and disordered regions and comparable or superior performance on static benchmarks
- **Visible evidence base** Abstract, introduction, results sections (architecture description, IDR benchmark results, transient/static benchmark results), discussion, methods (MD setup, training data, feature definitions, architecture details), supplementary note on equivariance
- **Missing materials affecting confidence** Full quantitative results tables (e.g., exact MCC, ROC-AUC, PR-AUC values for all benchmarks and baselines), figure panels referenced but not shown, detailed hyperparameter settings, baseline model descriptions, statistical significance tests, ablation results for all components, and complete benchmark dataset descriptions

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting approach to integrating conformational dynamics into binding site prediction, which addresses a genuine gap in the field. The architectural design, particularly the cooperative message-passing between core and surface residues and the use of dynamic features, is thoughtful and well-motivated. However, the current manuscript does not provide sufficient quantitative evidence to substantiate the central claims. Key performance metrics are reported only as medians or qualitative statements, baseline comparisons are incomplete, and the absence of full result tables and figures prevents rigorous evaluation. The equivariance proof in the supplementary note appears to have gaps. The work has potential, but the evidence as presented is insufficient to establish the claimed advantages.
- **Who would be interested in the results, and why** Computational structural biologists and bioinformaticians working on protein-protein interaction prediction, particularly those focused on intrinsically disordered proteins and conformational ensembles. Researchers developing deep learning methods for structural biology would be interested in the architectural innovations, especially the cooperative message-passing mechanism and dynamic feature encoding. The potential integration with AlphaFold and other structure prediction tools would also interest a broader structural biology audience.
- **Major strengths**
  1. The problem addressed is timely and important: most existing binding site predictors ignore conformational dynamics, which limits performance on disordered and flexible regions
  2. The architectural design is novel, particularly the cooperative message-passing between core and surface residues and the dynamic feature encoding at both node and edge levels
  3. The training data strategy, combining MD simulations with AlphaFlow-generated conformations, is creative and addresses the data scarcity issue for dynamic information
  4. The GeoLoss function, which accounts for distance to the interface in penalizing false positives, is a thoughtful contribution that could benefit the field
  5. The evaluation across diverse benchmarks (IDR-specific and general) is comprehensive in scope
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "Comprehensive evaluation on diverse independent datasets containing disordered, transient, and unbound structures showed that incorporating dynamic features in cooperative architecture significantly boosts prediction accuracy when flexibility matters, and requires substantially less amount of data than leading static models"
- **Evidence pointer** Results sections "Predicting binding regions with disordered binders" and "From Highly Flexible to Transient and Static Interactions", Figure 3c, Figure 5a
- **Concern** The central claim of significant performance improvement is not supported by the quantitative data presented. The manuscript reports only median ROC-AUC values (e.g., 0.88 for MFIB, 0.84 for Test42, 0.77 for FuzDB, 0.79 for IDRBind) without providing distributions, confidence intervals, or statistical significance tests. For the "Testing Transient" benchmark, the text states "marginal improvements over leading static models" (ROC-AUC 0.868), which contradicts the abstract's claim of "significantly boosts prediction accuracy." The comparison to baselines is incomplete: no baseline performance values are provided in the text, and the reader cannot assess whether the improvements are meaningful. The claim about requiring "substantially less amount of data" is not quantified or compared against any specific baseline.
- **Why it matters** The primary contribution of the manuscript is the claimed performance advantage of incorporating dynamics. Without complete quantitative results, including variance measures, statistical tests, and full baseline comparisons, the scientific case is not established. The internal inconsistency between "significant boosts" (abstract) and "marginal improvements" (results) further undermines confidence.
- **Resolution test** Provide full result tables with all metrics (MCC, ROC-AUC, PR-AUC) for all benchmarks and all baseline methods, including standard deviations or confidence intervals. Perform and report statistical significance tests (e.g., paired tests across benchmark entries). Quantify the data efficiency claim by training baselines on varying dataset sizes and showing learning curves.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "We proposed a novel time-free feature extraction pipeline using vectors as features in a rotationally equivariant manner (Supplementary Note S1)"
- **Evidence pointer** Supplementary Note 1, Methods section "Feature extraction strategy and labeling"
- **Concern** The equivariance proof in Supplementary Note 1 appears incomplete. The note demonstrates that the motion vector transforms correctly under rotation, but does not explicitly prove equivariance for the full architecture, including the attention mechanism, the cooperative message-passing constraints, and the pooling operation. The proof for the attention mechanism states "M p = softmax( QK p ) is invariant" but does not show how the spatial features (V * motionV) transform through the attention-weighted sum. The projection step is asserted to be equivariant but the derivation is not fully shown. Additionally, the note does not address translation invariance, which is claimed in the main text.
- **Why it matters** Equivariance is a fundamental design property claimed for the model. If the proof is incomplete or incorrect, the theoretical foundation of the architecture is compromised. This is particularly important because the model is applied to structures in different conformations, and the features must be consistent under rigid transformations.
- **Resolution test** Provide a complete, step-by-step proof of rotation equivariance and translation invariance for the entire architecture, including the attention mechanism, cooperative message-passing, and pooling. Alternatively, provide empirical verification by applying the model to rotated and translated versions of the same structures and showing identical outputs.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodology clarity
- **Claim pointer** "we provided an extensive set of MD simulations and collected NMR complexes from PDB... we curated a set of 1,115 protein chains in their bound forms... Performing three replicates of 500 microseconds for each entry, we obtained an overall 1-ms MD simulation data"
- **Evidence pointer** Methods section "Setup of MD simulations" and "Training data generation"
- **Concern** There is a critical inconsistency in the reported simulation time. The abstract states "overall 1-ms molecular dynamics simulations dataset," but the methods state "three replicates of 500 microseconds for each entry" (which would be 1.5 ms per entry, not 1 ms total). The text also mentions "500 ns" in the methods ("three replicates of 500 ns MD simulations"), which is inconsistent with the 500 microseconds claim. This discrepancy is substantial (a factor of 1000) and must be resolved. Additionally, the total simulation time across all 1,115 systems is not calculated, and the contribution from ATLAS and MDDB is not quantified.
- **Why it matters** The scale of the training data is a key claimed advantage. If the simulation time is misreported, the actual computational investment and the quality of the dynamic sampling are unclear. This affects the reproducibility and the assessment of whether the training data is indeed "extensive."
- **Resolution test** Correct the simulation time units consistently throughout the manuscript. Provide a clear breakdown of the total simulation time from each source (own MD, ATLAS, MDDB, AlphaFlow, NMR) and the number of conformations used per system.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Evaluation rigor
- **Claim pointer** "DynamicGT was run in inference mode on conformational ensembles generated by AlphaFlow using single-chain inputs (sequences without structural templates)"
- **Evidence pointer** Results section "Predicting binding regions with disordered binders", Figure 3b
- **Concern** The evaluation protocol for IDR benchmarks is not fully described. It is unclear how the AlphaFlow-generated ensembles are used: are predictions averaged across conformations, or is the maximum score taken? How many conformations are generated per protein? The manuscript does not specify whether the same AlphaFlow ensembles are used for all benchmark entries and whether the baseline methods are given the same conformational information. This is critical because the claimed advantage may partly stem from the use of AlphaFlow ensembles rather than the model architecture itself.
- **Why it matters** Fair comparison with baselines requires that all methods receive the same input information. If baselines are given only static structures while DynamicGT receives conformational ensembles, the comparison is not apples-to-apples. The manuscript does not clarify this.
- **Resolution test** Describe the exact inference protocol, including how AlphaFlow ensembles are generated and aggregated. Specify whether baseline methods are also provided with multiple conformations or only static structures. If baselines are disadvantaged, provide additional comparisons where all methods use the same input.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** "DynamicGT maintains robust performance across both bound and unbound structures, as evidenced by its performance on the ZDock benchmark"
- **Evidence pointer** Results section "From Highly Flexible to Transient and Static Interactions", Figure 5e
- **Concern** The ZDock benchmark results are presented only as a figure with no quantitative values in the text. The categorization of complexes (GPCR, antigen-epitope, enzyme-related, receptor-containing, miscellaneous) is described, but the actual performance numbers are not provided. The claim of "robust performance" cannot be assessed without these values. Additionally, the manuscript does not specify how the ZDock benchmark entries were filtered (e.g., removal of antibodies) and whether this filtering was applied consistently to all methods.
- **Why it matters** The generalizability claim across different complex types is important for the practical utility of the method. Without quantitative results, the reader cannot determine whether the model performs well in specific categories or only on average.
- **Resolution test** Provide the full ZDock results table with all metrics for each complex category and for all baseline methods. Describe the filtering criteria and ensure they are applied consistently.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states "requires substantially less amount of data than leading static models" but this claim is not quantified or supported by any specific comparison in the results.
- **Required correction** Either provide a quantitative comparison of data requirements (e.g., training set sizes needed to reach a given performance threshold) or remove this claim from the abstract.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, hyperparameters
- **Evidence pointer** Methods section "Architecture"
- **Issue** The architecture description mentions 35 layers and expanding receptive fields (12 to 48 neighbors), but does not specify other critical hyperparameters such as learning rate, batch size, optimizer, dropout, or the number of attention heads.
- **Required correction** Provide a complete list of hyperparameters in the methods or a supplementary table.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data description
- **Affected element** Training data
- **Evidence pointer** Methods section "Training data generation"
- **Issue** The manuscript mentions "around 3000 protein chains" from combined sources but does not specify the exact number of chains from each source (own MD, ATLAS, MDDB, NMR) or the number of conformations per chain.
- **Required correction** Provide a detailed breakdown of the training data composition, including the number of chains and conformations from each source.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Comparison fairness
- **Affected element** Baseline methods
- **Evidence pointer** Results sections, Figure 5a
- **Issue** The baseline methods (EquiPPIS, GraphPPIS, MaSIF-site, SPIDER) are mentioned but not described. It is unclear whether these are used with their default settings or retrained on the same data.
- **Required correction** Describe the baseline methods and their training/evaluation protocols. State whether they were retrained or used as pre-trained models.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figures 3, 4, 5
- **Evidence pointer** Results sections
- **Issue** The figures are referenced but not shown in the provided text. The descriptions suggest complex multi-panel figures, but the reader cannot assess the visual quality or the clarity of the presented data.
- **Required correction** Ensure all figures are included in the final submission with clear labels, legends, and sufficient resolution.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Dynamic-aware" vs "heterogeneity-aware"
- **Evidence pointer** Results sections
- **Issue** The manuscript uses both "dynamic-aware" and "heterogeneity-aware" to describe the model, which may cause confusion. The distinction between the two is not clearly defined.
- **Required correction** Use consistent terminology throughout the manuscript and define the terms clearly.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Related work
- **Affected element** Introduction
- **Evidence pointer** Introduction
- **Issue** The introduction mentions recent advances in GNNs and binding site prediction but does not provide a comprehensive comparison with the most recent state-of-the-art methods, particularly those published in the last 1-2 years.
- **Required correction** Update the related work section to include the most recent methods and clearly state the novelty of DynamicGT relative to them.

## Risk / unsupported claims
- The claim of "significant boosts in prediction accuracy" is not supported by the quantitative data presented, which shows only "marginal improvements" on one benchmark
- The claim of "requires substantially less amount of data" is not quantified or compared against any baseline
- The claim of "robust performance" on ZDock is not supported by quantitative values in the text
- The claim that the model "outperformed existing IDR site predictors" is not supported by specific comparison results
- The equivariance proof in Supplementary Note 1 is incomplete and does not cover the full architecture
- The reported simulation time is inconsistent (500 microseconds vs 500 ns vs 1 ms total), making the training data description unreliable
- The evaluation protocol for IDR benchmarks (how AlphaFlow ensembles are used) is not described, making the comparison potentially unfair
- The manuscript does not provide statistical significance tests for any performance comparisons