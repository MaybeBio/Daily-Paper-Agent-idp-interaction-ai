## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, experiments, discussion) without figures, tables, or supplementary materials
- **Assessment boundary** Scientific claims, methodological soundness, and evidence quality as presented in the provided text
- **Shared manuscript claim summary** The authors propose GeoGAT-site, a face-centered geometric graph attention network for protein-protein interface prediction, claiming a 3.64-fold acceleration in patch generation over vertex-centered methods, a ROC AUC of 0.89 on an independent test set of 167 complexes, and superiority over MaSIF-site, SPPIDER, and PSIVER
- **Visible evidence base** Textual descriptions of methods, experimental design, and reported numerical results; no actual figures, tables, or code were provided
- **Missing materials affecting confidence** All figures (Figures 1-7), Table 1, supplementary materials, code repository, and dataset access details are absent from the provided material

## Reviewer
- **Overall assessment** The manuscript addresses a relevant problem in structural biology with a plausible methodological innovation, namely the use of face-centered rather than vertex-centered surface fingerprints for PPI interface prediction. The reported performance metrics are competitive with existing methods. However, the provided text contains several inconsistencies, incomplete methodological details, and unsupported claims that prevent a full evaluation of the work. The absence of figures, tables, and supplementary materials substantially limits the ability to verify the reported results. The manuscript has potential but requires substantial revision and additional evidence before its claims can be considered established.
- **Who would be interested in the results, and why** Computational structural biologists, researchers in protein-protein interaction prediction, and developers of geometric deep learning methods for molecular surfaces would find this work relevant. The claimed computational efficiency gain and the geometric attention mechanism could be of interest to those working on high-throughput PPI screening and docking applications. The work may also appeal to researchers in drug design and protein engineering who rely on interface prediction tools.
- **Major strengths** The face-centered approach is a conceptually interesting alternative to the dominant vertex-centered paradigm, with a plausible efficiency argument. The integration of geometric edge attributes (distance and angle) into the attention mechanism is a sensible design choice. The authors report a large-scale training dataset and provide a clear statement of public code and data availability. The ablation study design, with multiple variants, is thorough in principle.
- **Major Concerns** 
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The manuscript claims a 72.51% speedup in patch generation and a 3.64-fold acceleration compared to vertex-centered methods, with the efficiency attributed to face-centered representation and implementation optimizations
  - **Evidence pointer** Section "Computational Efficiency of the Face-Centered Approach"; Section "Data Preprocessing and Face Fingerprint Generation"
  - **Concern** The efficiency claim is internally inconsistent. The text states a 72.51% speedup, which corresponds to a factor of approximately 3.64 (1 / (1 - 0.7251) = 3.64), yet the abstract and introduction describe a "3.64-fold acceleration." These are equivalent statements, but the text also claims that face-centered patches number 150 million versus 402 million for vertex-centered, which is a reduction by a factor of 2.68, not 3.64. The text further states that feature aggregation contributes "roughly 62.7% to the observed speedup under linear scaling assumptions," but no derivation or empirical decomposition is provided. The relationship between patch count reduction, per-patch cost, and total speedup is not rigorously established. The claim that Euler's formula (F ≈ 2V - 4) is relevant to patch count reduction is confusing, since the number of faces is larger than vertices, not smaller, and the reduction from 402M to 150M patches is not explained by this formula.
  - **Why it matters** The computational efficiency advantage is a central selling point of the method and is highlighted in the abstract, introduction, and contributions list. If the efficiency claim is not rigorously supported, the novelty and practical value of the approach are substantially weakened.
  - **Resolution test** Provide a clear derivation of the speedup with a breakdown of contributions from patch count reduction, per-patch computation, and implementation factors. Report actual wall-clock timings for both face-centered and vertex-centered pipelines on the same hardware and dataset. Clarify the relationship between the 72.51% figure and the 3.64-fold claim, and reconcile the patch count numbers with the Euler formula discussion.
  
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The manuscript claims that GeoGAT-site achieves a ROC AUC of 0.89 on an independent test set of 167 complexes, outperforming MaSIF-site (0.845), SPPIDER (0.65), and PSIVER (0.63)
  - **Evidence pointer** Section "Experiments"; Figure 4 (not provided)
  - **Concern** The comparison with MaSIF-site is problematic. The text states that MaSIF-site achieves a ROC AUC of 0.845 on the independent test set, but it is unclear whether MaSIF-site was retrained on the authors' training data or evaluated using its original pretrained model. The test set is described as having "no sequence or structural overlap with the training set (sequence identity < 30%, TM score < 0.5)," but the criteria for ensuring this non-overlap are not described in detail. Furthermore, the comparison with SPPIDER and PSIVER is performed on a subset of 50 complexes, while the headline ROC AUC of 0.89 is reported on the full 167-complex set. The relationship between these two evaluations is unclear. The text also reports a ROC AUC of 0.9145 for GeoGAT-site on the single complex 1A0G versus 0.8546 for MaSIF-site, but it is not stated whether this is a per-patch or per-protein metric, or how many patches were evaluated.
  - **Why it matters** The performance comparison is the primary evidence for the method's utility. If the baselines were not evaluated under comparable conditions, the reported superiority may be an artifact of experimental setup rather than a genuine improvement.
  - **Resolution test** Clearly describe the evaluation protocol for each baseline method, including whether they were retrained, which hyperparameters were used, and how the test subsets were selected. Report confidence intervals or statistical significance tests for the ROC AUC differences. Provide per-complex performance distributions rather than only aggregate metrics.
  
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The manuscript claims that the geometric attention mechanism, which integrates distance and angle edge attributes, improves performance over variants without these attributes
  - **Evidence pointer** Section "Experiments"; Table 1 (not provided); Figures 6 and 7 (not provided)
  - **Concern** The ablation study is described in the text but the actual results are not visible. The text reports that the full model achieved a ROC AUC of 0.9041 (internal) and 0.8956 (independent), but these numbers differ from the headline ROC AUC of 0.89 reported elsewhere. The relationship between the internal test set (30 million patches from 4,000 structures) and the independent test set (1 million patches from 167 complexes) is not clearly defined. The text mentions a "distance-only variant" and an "angle-only variant" but the angle-only result is only mentioned in passing. The statistical significance testing is described as using Wilcoxon signed-rank tests with p-values < 0.01, but the number of paired observations and the exact comparison groups are not specified. The claim that "heads = 4 and hidden channels = 128" are optimal is stated without showing the full hyperparameter sweep results.
  - **Why it matters** The ablation study is the key evidence for the contribution of the geometric attention mechanism. Without visible results, the claim that the mechanism is beneficial cannot be evaluated.
  - **Resolution test** Provide Table 1 and Figures 6 and 7 in the manuscript. Clearly define the internal and independent test sets and their relationship. Report all ablation variant results with error bars or confidence intervals. Specify the exact statistical test procedure, including the number of paired samples and the correction for multiple comparisons.
  
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Reproducibility
  - **Claim pointer** The manuscript claims that the code and dataset are publicly available
  - **Evidence pointer** Section "Introduction"; no repository link or accession number provided
  - **Concern** The text states "We make our code and dataset publicly available" but no URL, DOI, or repository identifier is provided. The dataset of 150 million fingerprints from over 20,000 proteins is described but its exact composition, source PDB IDs, and processing scripts are not detailed. The preprocessing pipeline references multiple tools (PDB2PQR, APBS, HBMLUS, FreeSASA, MSMS, meshio) but the specific parameters and versions are not given.
  - **Why it matters** Reproducibility is a core requirement for computational biology research. Without access to the code, data, and detailed processing parameters, other researchers cannot verify or build upon the results.
  - **Resolution test** Provide a working repository link or DOI in the manuscript. Include a detailed data card describing the dataset composition, source structures, and processing parameters. Specify software versions and configuration files for the full pipeline.
  
  - **Concern ID** R1-M5
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The manuscript claims that GeoGAT-site "augments downstream structural modeling paradigms through targeted constraints" and has "profound implications for therapeutic discovery, protein redesign, and molecular epistemology"
  - **Evidence pointer** Section "Abstract"; Section "Discussion"
  - **Concern** The claimed downstream applications are not demonstrated anywhere in the text. No experiments show integration with docking tools, therapeutic target identification, or protein design workflows. The statement about "molecular epistemology" is vague and not substantiated. The claim that GeoGAT-site "can guide tools like Rosetta or Osprey" is speculative and not supported by any experimental evidence.
  - **Why it matters** Overstated claims about downstream utility without demonstration can mislead readers about the maturity of the method. The core contribution is interface prediction, and the broader implications should be framed as future directions rather than established capabilities.
  - **Resolution test** Either remove or substantially soften the claims about downstream applications, or provide concrete demonstrations of integration with docking or design tools. Frame the broader implications as speculative future work in the Discussion section.
  
  - **Concern ID** R1-M6
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** The manuscript claims that the face-centered approach "preserves granular surface descriptors" and maintains "robust generalization across heterogeneous interaction motifs"
  - **Evidence pointer** Section "Abstract"; Section "Data Preprocessing and Face Fingerprint Generation"
  - **Concern** The text does not provide a quantitative comparison of the information content or fidelity of face-centered versus vertex-centered fingerprints. The claim of "robust generalization" is supported only by the aggregate ROC AUC on the independent test set, without analysis of performance across different interaction types, protein sizes, or structural classes. The text mentions category-specific results (enzyme-substrate 0.90, receptor-ligand 0.88, antibody-antigen 0.87) but does not report the number of complexes in each category or the variance within categories.
  - **Why it matters** The claim of preserved fidelity and robust generalization is central to the argument that face-centered representations are not merely faster but also equally informative. Without comparative analysis, the reader cannot assess whether the efficiency gain comes at a cost in predictive quality for certain protein classes.
  - **Resolution test** Provide a systematic comparison of face-centered versus vertex-centered fingerprint information content, such as reconstruction error or downstream task performance on identical data. Report per-category performance with confidence intervals and sample sizes. Analyze failure cases to identify any systematic biases in the face-centered approach.
- **Minor Comments** 
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Abstract
  - **Evidence pointer** Section "Abstract"
  - **Issue** The abstract states "3.64-fold acceleration" while the introduction and methods state "72.51% speedup." These are mathematically equivalent but presented inconsistently, which may confuse readers.
  - **Required correction** Use a single consistent expression throughout the manuscript, preferably with both forms stated once and then a consistent choice thereafter.
  
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Methods
  - **Evidence pointer** Section "Data Preprocessing and Face Fingerprint Generation"
  - **Issue** The equations for electrostatic potential, hydrogen bond strength, and hydrophobicity are referenced but not shown in the provided text. The text states "interpolated to vertices via: where φ is the potential grid" and "normalized to [−1, 1] as: where d_H−A is the hydrogen-acceptor distance" but the actual formulas are missing.
  - **Required correction** Ensure all equations are included in the manuscript with proper notation and variable definitions.
  
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Experiments
  - **Evidence pointer** Section "Experiments"
  - **Issue** The text states "a subset of 50 single-chain protein-protein complexes" for comparison with SPPIDER and PSIVER, but the criteria for selecting this subset are not described. It is unclear whether this subset is a random sample or selected for specific properties.
  - **Required correction** Describe the subset selection criteria and justify why this subset is representative of the full test set.
  
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Experiments
  - **Evidence pointer** Section "Experiments"
  - **Issue** The text mentions "transient (50 samples) and stable (60 samples) PPI subsets" but does not define what constitutes transient versus stable interactions or how these subsets were derived.
  - **Required correction** Provide clear definitions of transient and stable PPIs and describe how these subsets were constructed.
  
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Discussion
  - **Evidence pointer** Section "Discussion"
  - **Issue** The Discussion states "Training on holo-state structures may limit applicability to unbound (apo) structures" but does not provide any analysis of how the method performs on apo structures or what the expected degradation might be.
  - **Required correction** Either provide apo-structure evaluation results or clearly frame this as a hypothesis requiring future testing.
  
  - **Concern ID** R1-m6
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Introduction
  - **Evidence pointer** Section "Introduction"
  - **Issue** The introduction cites "MaSIF (Marchand, Buckley, and Schneuing 2025)" but the original MaSIF paper was published earlier. The citation year appears incorrect.
  - **Required correction** Verify all citations for accuracy, particularly the MaSIF reference.
  
  - **Concern ID** R1-m7
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Methods
  - **Evidence pointer** Section "GeoGAT-site Model"
  - **Issue** The text states "input channels in = 6" but the node features are described as "normal vectors [n_x, n_y, n_z] and chemical attributes [c_v, h_v, p_v]" which totals 6 features. However, the edge features include distance and angle, and it is unclear how these are incorporated into the attention mechanism beyond the described equations.
  - **Required correction** Provide a clearer description of how edge features are integrated into the attention computation, including the exact functional form of the attention coefficient.
  
  - **Concern ID** R1-m8
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Experiments
  - **Evidence pointer** Section "Experiments"
  - **Issue** The text mentions "Wilcoxon signed-rank tests, with p-values < 0.01" but does not specify which comparisons were tested or how many tests were performed. Multiple testing corrections are not mentioned.
  - **Required correction** Specify the exact comparisons tested, the number of tests, and whether any multiple testing correction was applied.

## Risk / unsupported claims
- The claim of "3.64-fold acceleration" and "72.51% speedup" in patch generation is not supported by any empirical timing data in the provided text
- The claim that GeoGAT-site "outperforms" MaSIF-site, SPPIDER, and PSIVER is based on reported ROC AUC values, but the evaluation protocol for baselines is not fully described
- The claim that the geometric attention mechanism improves performance is based on ablation results that are not visible in the provided material
- The claim of "robust generalization across heterogeneous interaction motifs" is not supported by per-category performance analysis with confidence intervals
- The claim that GeoGAT-site can "guide downstream structural modeling paradigms" and has "profound implications for therapeutic discovery, protein redesign, and molecular epistemology" is speculative and not demonstrated
- The claim that the dataset of 150 million fingerprints from over 20,000 proteins ensures "robust learning and broad interaction pattern coverage" is not supported by diversity analysis or comparison with existing datasets
- The claim of compatibility with docking tools is mentioned but no integration experiments are described
- The statement that the model "preserves granular surface descriptors" is not quantitatively compared with vertex-centered approaches
- The claim that "heads = 4 and hidden channels = 128" are optimal is not supported by visible hyperparameter sweep results
- The claim of statistical significance via Wilcoxon signed-rank tests is not fully specified in terms of sample sizes and comparison groups