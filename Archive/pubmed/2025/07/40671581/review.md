## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, and supporting statements)
- **Assessment boundary** Scientific content, methodological soundness, claim support, and presentation quality as presented in the provided text
- **Shared manuscript claim summary** The authors develop a residue-based coarse-grained model for polyethylene glycol (PEG) compatible with the CALVADOS protein model, parameterize it against experimental data on PEG chain dimensions and PEG-induced compaction of disordered proteins, and demonstrate its utility in quantifying weak phase separation propensities via crowder titration simulations for hnRNPA1 LCD variants, Ddx4n1, and alpha-synuclein variants.
- **Visible evidence base** Main text figures (Figures 1-4), supplementary figures and tables referenced (Figures S1-S8, Tables S1-S8), simulation methods descriptions, and data availability statement
- **Missing materials affecting confidence** Full figure panels and captions, supplementary information contents, exact simulation parameters for all systems, convergence criteria for phase separation simulations, and detailed statistical analysis of fits

## Reviewer
- **Overall assessment** The manuscript presents a timely and useful contribution to the field of disordered protein biophysics by introducing a coarse-grained PEG model compatible with the widely used CALVADOS framework. The parameterization strategy is sensible, combining single-chain PEG properties with protein-PEG compaction data. The application to phase separation titrations is conceptually appealing and addresses a real need for characterizing weakly phase-separating proteins. However, several technical aspects require clarification and additional validation before the model's broader utility can be fully assessed. The claim that the model can reliably extrapolate intrinsic phase separation propensities from crowder titrations is supported by the A1-LCD data but needs stronger statistical backing and more careful treatment of potential systematic errors.

- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, biomolecular condensates, and phase separation, particularly those using coarse-grained simulations. The work will also interest experimentalists who use PEG crowding assays to probe protein phase behavior and who seek a computational framework for interpreting such experiments. The model's compatibility with CALVADOS makes it immediately usable by a substantial user community.

- **Major strengths**
  1. The model addresses a clear gap: a computationally efficient, physically reasonable PEG representation compatible with an established protein model.
  2. The parameterization strategy is pragmatic and data-driven, using both PEG-only and protein-PEG experimental data.
  3. The demonstration that PEG titrations can be used to extrapolate intrinsic phase separation propensities for weakly separating proteins is conceptually valuable and practically relevant.
  4. The observation that PEG response slopes can differ between sequence variants (alpha-synuclein charge patterning) is an important cautionary finding.
  5. The work is well contextualized within existing literature and the code/data are openly available.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the PEG model captures the balance between PEG-PEG and protein-PEG interactions, and that lambda_PEG = 0.2 gives the best overall agreement with experiments for both ACTR and IN.
- **Evidence pointer** Figure 2, Figure S2, Methods section "Parameterization of the PEG model"
- **Concern** The parameterization for protein-PEG interactions relies on comparing simulated R_ee values (converted from R_g using Ree = 5Rg) with experimental smFRET data. This conversion factor is a rough approximation and may introduce systematic errors, particularly for compact or collapsed states at high crowder concentrations. The manuscript does not discuss the validity of this relationship for the specific proteins and conditions studied. Additionally, the chi-squared statistic used for model selection aggregates data across multiple crowder concentrations and molecular weights, but the sensitivity of the optimal lambda_PEG to the choice of experimental datasets or the weighting scheme is not explored.
- **Why it matters** The central parameter of the model (lambda_PEG = 0.2) is determined by this procedure. If the R_g to R_ee conversion is inaccurate or if the optimization is sensitive to dataset choices, the model's predictive power for other proteins or conditions could be compromised.
- **Resolution test** Provide a sensitivity analysis showing how the optimal lambda_PEG changes when (a) using a different R_g-R_ee relationship, (b) excluding individual datasets, or (c) using alternative weighting schemes. Alternatively, validate the model against an independent experimental dataset not used in parameterization.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that linear extrapolation of PEG titration curves can be used to quantify intrinsic phase separation propensities, and that this approach correctly captures differences between A1-LCD aromatic variants.
- **Evidence pointer** Figure 3, Figure S3, Figure S4
- **Concern** The linear fits used for extrapolation are performed over a limited range of PEG concentrations (approximately 2-10% w/v), and the manuscript notes convergence difficulties at the highest concentrations. The statistical quality of these fits is not reported (e.g., R-squared values, confidence intervals on slopes and intercepts). For the alpha-synuclein data, the extrapolated values are compared across variants with different slopes, but the uncertainty in these extrapolations is not propagated into the reported Delta-Delta-G values. The claim that the extrapolated value for A1-LCD WT matches direct simulation without PEG is based on a single comparison and lacks error analysis.
- **Why it matters** The central methodological contribution is the use of crowder titrations with linear extrapolation. If the fits are poorly constrained or the extrapolation is sensitive to the fitting range, the quantitative conclusions about intrinsic phase separation propensities could be unreliable.
- **Resolution test** Report full statistical details of all linear fits (including confidence intervals on all parameters), perform a jackknife or bootstrap analysis to assess the stability of extrapolated values, and test the sensitivity of the extrapolated Delta-G values to the choice of fitting range.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that the model can be used to quantify phase separation propensities of proteins that are not prone to phase separate strongly, and that this enables exploration of "weaker" phase separation.
- **Evidence pointer** Figure 4, Discussion
- **Concern** The demonstration of this capability is limited to a small number of systems (A1-LCD variants, Ddx4n1, alpha-synuclein and one variant). The alpha-synuclein results are only qualitatively compared to experimental trends, and the Ddx4n1 comparison shows quantitative disagreement in the PEG response slope. The manuscript does not provide a clear benchmark for what level of accuracy is required for the method to be practically useful for predicting relative phase separation propensities across a broader range of proteins.
- **Why it matters** The broader utility of the approach depends on its ability to reliably rank proteins or variants by their intrinsic phase separation propensity. Without a more extensive validation set or clear performance metrics, the practical impact of the method remains uncertain.
- **Resolution test** Apply the titration-extrapolation approach to a larger set of proteins or variants with known experimental phase separation behavior, and report the correlation between predicted and measured propensities. Alternatively, provide a clear discussion of the expected accuracy limits based on the current validation.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that the PEG model produces an apparent linear response in Delta-G-transfer with increasing PEG concentration, and that this enables distinguishing between effects of crowders of different sizes.
- **Evidence pointer** Figure 3, Discussion
- **Concern** The manuscript does not provide a mechanistic explanation for why the Delta-G-transfer response is linear in PEG concentration, nor does it discuss the theoretical basis for this relationship beyond citing prior work. The observation that PEG8000 has a substantially larger effect than PEG400 is reported but not analyzed in terms of the underlying physics (e.g., excluded volume vs. enthalpic contributions). The relationship between the slope of the titration curve and molecular properties of the protein remains largely empirical.
- **Why it matters** Understanding the physical basis of the linear response and the slope's dependence on protein sequence and crowder properties is important for interpreting what the slope means biologically and for predicting when the linear approximation might break down.
- **Resolution test** Provide a theoretical analysis or additional simulations that dissect the contributions to the PEG response (e.g., varying PEG-protein interaction strength independently of PEG size, or analyzing the radial distribution functions of PEG around the protein in the dense and dilute phases).

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction, Discussion
- **Issue** The manuscript assumes familiarity with coarse-grained simulation terminology and phase separation concepts. Some terms (e.g., "slab geometry," "direct-coexistence simulations," "transfer free energy") are introduced without brief definitions for readers who may be experimentalists.
- **Required correction** Add brief explanations of these terms at first use, or include a short "Computational methods primer" subsection for non-specialist readers.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, "Parameterization of the PEG model"
- **Evidence pointer** Methods section
- **Issue** The choice of the range for lambda_PEG (0.0 to 0.4) and sigma_PEG (0.35 to 0.46 nm) is not justified. The manuscript states that values close to or below the glycine bead size were chosen for sigma, but the rationale for the lambda range is unclear.
- **Required correction** Provide a brief justification for the parameter ranges explored, citing relevant physical considerations or prior simulation studies.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, "Phase separation of alpha-synuclein and a charge-segregated swap variant"
- **Evidence pointer** Figure 4, Figure S6
- **Concern** The comparison between simulated and experimental phase separation behavior for alpha-synuclein is described as "qualitative agreement," but the specific experimental data used for comparison are not clearly identified in the text. It is unclear whether the comparison is to the same experimental conditions (pH, salt, temperature) as the simulations.
- **Required correction** Clearly specify the experimental datasets used for comparison and state whether simulation conditions match those of the experiments.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The discussion of potential applications (e.g., integration with CALVADOS 3, expanding training sets for PS predictors) is brief and somewhat speculative. The authors do not provide concrete examples of what new biological insights the model could enable.
- **Required correction** Expand the discussion with one or two specific, concrete examples of questions that this model could address that were previously inaccessible.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, "Simulations"
- **Evidence pointer** Methods section
- **Issue** The manuscript states that simulations were performed with OpenMM v7.5 but does not specify the version of the CALVADOS model used (CALVADOS 2 is mentioned, but the specific parameter set or release version is not given). This could affect reproducibility.
- **Required correction** Specify the exact version or commit of the CALVADOS model used, and provide the specific parameter files or a link to them.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Results, "Phase separation of hnRNPA1 LCD is linearly dependent on PEG concentrations"
- **Evidence pointer** Figure 3
- **Issue** The term "Delta-G-transfer" is used throughout, but its physical meaning (the free energy difference between the dense and dilute phases) is only implicitly defined. For readers unfamiliar with phase separation thermodynamics, this could be confusing.
- **Required correction** Provide a brief definition of Delta-G-transfer and its relationship to the saturation concentration at first use.

## Risk / unsupported claims
- The claim that the model "will be useful for the interpretation of crowding experiments" is reasonable but not yet fully demonstrated; the validation is limited to a few systems and the quantitative accuracy for phase separation predictions is not established.
- The statement that the linear extrapolation approach "correctly extrapolates the intrinsic phase propensity" of A1-LCD is supported by the data but relies on a single comparison point and lacks rigorous error analysis.
- The claim that the model captures "the balance between PEG-PEG and protein-PEG interactions" is supported by the parameterization procedure, but the manuscript does not demonstrate that this balance is correct for systems beyond those used in parameterization.
- The observation that "the PEG crowding response changes between charge patterning variants of alpha-synuclein" is based on simulation data only and has not been experimentally validated; the manuscript appropriately notes this as a prediction.
- The statement that "shorter PEG chains are less excluded at high PEG concentrations" is presented as a finding but the supporting data are not shown in the main text (only referenced in supplementary figures).
- The claim that the model can be used to explore "weaker" phase separation is plausible but the manuscript does not provide a clear definition of what constitutes "weak" or a benchmark for the method's sensitivity limits.