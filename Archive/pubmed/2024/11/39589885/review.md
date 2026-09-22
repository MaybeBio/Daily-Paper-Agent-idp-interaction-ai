## Review setup
- **Input scope** Full manuscript text (main text, methods summary, data availability statement) as provided by the user
- **Assessment boundary** Scientific content, technical soundness, and clarity of the reported findings based solely on the supplied material
- **Shared manuscript claim summary** The authors present SERF, a small disordered protein from S. cerevisiae, as a model system to study interactions between intrinsically disordered proteins (IDPs) and structured RNA. They characterize the conformational ensemble of free SERF using NMR, SAXS, and all-atom simulations; show that SERF binds the HIV-1 TAR RNA with micromolar affinity in a 1:1 complex; identify the N-terminal region of SERF as the primary RNA-binding interface; and demonstrate that SERF and TAR undergo associative phase separation at high concentrations, consistent with complex coacervation.
- **Visible evidence base** Main text figures referenced (Figs. 1–5), supplementary figure and table references (SI Appendix Figs. S1–S8, Tables S1–S5), methods summaries for NMR, SAXS, simulations, and condensate assays
- **Missing materials affecting confidence** Full Materials and Methods details, all supplementary figures and tables, raw data files, simulation parameters and analysis scripts, NMR assignment tables, and the complete source data file were not provided. These are essential for independent verification of several key claims.

## Reviewer
- **Overall assessment** This manuscript presents a well-structured and technically ambitious study of a disordered protein–RNA interaction system. The combination of solution NMR, SAXS, all-atom and coarse-grained simulations, and phase-separation assays is appropriate and complementary. The central claims, namely that SERF binds TAR primarily through its N-terminal region and that the complex is dynamic and electrostatically driven, are plausible and supported by the evidence summarized. However, several technical details and quantitative validations are not fully visible from the provided material, and the significance of the findings relative to existing literature on IDP–RNA interactions could be more sharply articulated. The work is of interest to the biophysics and phase-separation communities, but the case for broad conceptual advance is not fully established from the supplied text alone.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, RNA-binding proteins, biomolecular condensates, and phase separation will find this work relevant. The study provides a tractable minimal system for dissecting IDP–RNA interactions, which is valuable given the prevalence of disordered regions in RNA-binding proteins. The methodological integration of NMR, SAXS, and simulations will also appeal to biophysicists interested in conformational ensembles of IDPs.
- **Major strengths**
  1. The study uses a complementary suite of biophysical methods (NMR, SAXS, IM-MS, simulations) to characterize both the free protein and the complex, which strengthens the conclusions.
  2. The identification of the N-terminal region of SERF as the primary RNA-binding interface, supported by both experimental CSP data and coarse-grained simulations, is a clear and testable finding.
  3. The demonstration that SERF and TAR undergo complex coacervation with salt sensitivity provides a direct link between the molecular interaction and phase behavior.
  4. The authors are appropriately cautious in interpreting crosslinking data and in distinguishing apparent from true binding stoichiometry.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the 1:1 binding model is the most appropriate fit to the fluorescence anisotropy data, yielding a KD,app of 0.67 ± 0.04 µM for SERF–TAR.
- **Evidence pointer** Figure 3A, SI Appendix Table S3, Materials and Methods (Fluorescence Anisotropy)
- **Concern** The manuscript states that a 2:1 model was considered and rejected, but the criteria for model selection are not described. The charge stoichiometry (+12 protein, −29 RNA) makes a 1:1 complex electrostatically imbalanced, and the authors acknowledge "fuzzy" stoichiometry. Without details on the fitting procedure, error analysis, and model comparison (e.g., AIC or F-test), the reported KD,app cannot be independently evaluated. Additionally, the anisotropy data are presented only as a single representative curve, with no replicates or error bars shown.
- **Why it matters** The binding affinity is a central quantitative claim that underpins the interpretation of the complex as weak and dynamic. If the 1:1 model is not robustly justified, the subsequent structural and mechanistic interpretations are weakened.
- **Resolution test** Provide the full fitting details, including the mathematical model, the alternative models tested, the selection criteria, and replicate data with error estimates. Show residuals for each model fit.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the N-terminal region of SERF (residues ~9–18) is the primary RNA-binding interface, based on large CSPs in this region and the absence of CSPs in the C-terminal region.
- **Evidence pointer** Figure 4C, SI Appendix Figures S5–S7
- **Concern** The CSP analysis is presented as a bar chart, but the threshold for significance is not defined. The authors note that CSPs in the NTR are "up to 10 times larger" than surrounding residues, but it is unclear whether this is statistically significant given the line broadening observed in the bound state. The manuscript also states that line broadening in the 13C,15N-CON spectrum posed a barrier to assignments, which raises the question of whether the CSP analysis is based on a complete set of assignments in the bound state. Furthermore, the claim that the CTR does not interact with RNA is based on the absence of CSPs, which is a negative result that requires careful validation (e.g., relaxation measurements or saturation transfer experiments).
- **Why it matters** The identification of the binding interface is a key finding of the paper. If the CSP analysis is incomplete or biased by line broadening, the conclusion that the NTR is the sole binding site may be premature.
- **Resolution test** Provide the CSP values with uncertainties, define the significance threshold, and show that the bound-state assignments are complete for the residues used in the analysis. Consider complementary experiments (e.g., paramagnetic relaxation enhancement on the RNA or cross-saturation) to confirm the interface.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors state that the SERF–TAR system serves as a "tractable model system" for studying IDP–RNA interactions and that the findings may inform understanding of condensate assembly.
- **Evidence pointer** Discussion section
- **Concern** The manuscript does not clearly articulate what general principle is established that was not already known from prior studies of IDP–RNA interactions or complex coacervation. The finding that a positively charged IDP binds RNA electrostatically and undergoes coacervation is consistent with a large body of literature. The specific claim that the N-terminal region of SERF is the binding site is interesting but may be system-specific. The broader significance for understanding how IDPs recognize folded RNAs, or how fuzzy complexes contribute to phase separation, is not developed with sufficient depth.
- **Why it matters** For a Nature-style journal, the work must demonstrate conceptual advance beyond a well-characterized example. If the findings are largely confirmatory, the impact is limited.
- **Resolution test** Revise the discussion to explicitly state what is generalizable and what is novel. Compare the SERF–TAR system to other IDP–RNA pairs and articulate what new mechanistic insight is provided.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that coarse-grained simulations using the Mpiri force field reproduce the relative binding affinity of SERF for TAR versus (rU)29, with a ~3.5-fold higher affinity for TAR.
- **Evidence pointer** SI Appendix Figure S4, Materials and Methods (CG Simulations)
- **Concern** The simulation methodology is only briefly described. The Mpiri force field is relatively new, and its accuracy for protein–RNA interactions is not well established. The calculation of relative dissociation constants from simulations is not described in sufficient detail to assess reliability. The agreement with the experimental ~2.8-fold difference is presented as validation, but the uncertainty in the simulated value is not reported.
- **Why it matters** The simulations are used to support the experimental findings and to provide mechanistic insight. If the simulation methodology is not robust, the conclusions drawn from it are weakened.
- **Resolution test** Provide full simulation parameters, convergence criteria, and error estimates for the calculated relative affinities. Validate the force field against experimental data for a test system.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1B
- **Evidence pointer** Figure 1B
- **Issue** The disorder prediction profile is mentioned but not shown in the provided text. The figure is referenced but not described in sufficient detail.
- **Required correction** Ensure the figure is described in the text with a clear explanation of the prediction method and the significance of the profile.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** SAXS analysis
- **Evidence pointer** Figure 2E, SI Appendix Figure S2
- **Issue** The SAXS data are described as showing agreement with simulations, but the specific metrics used for comparison (e.g., χ², Rg) are not reported in the main text.
- **Required correction** Report the quantitative agreement metrics and the uncertainty in the Rg values.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Phase-separation assays
- **Evidence pointer** Figure 5
- **Issue** The turbidity measurements are described as "saturable," but the saturation point and the relationship to the binding affinity are not discussed.
- **Required correction** Clarify the relationship between the turbidity saturation and the KD,app, and discuss whether the phase-separation threshold is consistent with the binding affinity.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion is somewhat repetitive and could be more focused on the key findings and their implications.
- **Required correction** Streamline the discussion to emphasize the novel contributions and the broader relevance.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Crosslinking experiments
- **Evidence pointer** Figure 5F
- **Issue** The crosslinking experiments are described as showing "evidence for a SERF trimer," but the band is described as "faint." The quantification and reproducibility of this result are not reported.
- **Required correction** Provide quantification of the gel bands and report the number of replicates.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Materials and Methods
- **Evidence pointer** Materials and Methods (NMR Spectroscopy)
- **Issue** The NMR methods are described in a condensed form, and the reader is referred to the SI for details. This makes it difficult to assess the quality of the data.
- **Required correction** Provide more detail on the NMR experiments in the main text or ensure the SI is accessible and complete.

## Risk / unsupported claims
- The claim that the 1:1 binding model is the most appropriate fit is not fully supported by the provided evidence, as the model selection criteria are not described.
- The claim that the N-terminal region of SERF is the primary RNA-binding interface is based on CSP data that may be incomplete due to line broadening.
- The claim that the CTR of SERF does not interact with RNA is based on a negative result and requires additional validation.
- The claim that the simulations reproduce the relative binding affinity is not fully supported, as the simulation methodology and uncertainty are not described in sufficient detail.
- The claim that the SERF–TAR system is a "tractable model system" for IDP–RNA interactions is not fully justified, as the broader significance is not clearly articulated.
- The phase-separation data are described qualitatively, and the relationship between the turbidity measurements and the molecular interaction is not quantified.