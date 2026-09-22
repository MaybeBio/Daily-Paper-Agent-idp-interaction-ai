## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and conclusions. Figures and tables are referenced but not provided in full detail.
- **Assessment boundary** The scientific claims, methodology, and interpretation presented in the manuscript. No assessment of editorial fit or journal policy.
- **Shared manuscript claim summary** The authors claim that the intrinsically disordered C-terminal domain (CTD) of p53 allosterically regulates the DNA-binding domain (DBD) by promoting DNA binding through a two-step mechanism: DNA binding first induces conformational changes in the DBD, and subsequent CTD-DNA interactions amplify and stabilize the allosteric network, enhancing overall binding affinity.
- **Visible evidence base** Molecular dynamics simulation data (8 μs total), free energy landscapes, dynamic cross-correlation analyses, binding free energy calculations (MM-GBSA), residue contact maps, RMSD/RMSF analyses, and in silico mutagenesis simulations.
- **Missing materials affecting confidence** Figures S1–S11 and Tables S1–S4 are referenced but not provided. Structural coordinates and simulation input files are not available. No experimental validation data are presented.

## Reviewer
- **Overall assessment** The manuscript presents a plausible computational model for CTD-mediated allosteric regulation of p53 DBD DNA binding. The two-step mechanism is clearly articulated and supported by multiple complementary analyses. However, the evidence is entirely computational, and several key claims regarding the allosteric network and its functional consequences require stronger validation. The study is technically sound in its execution but limited in its ability to establish causality without experimental corroboration.
- **Who would be interested in the results, and why** Researchers studying p53 biology, intrinsically disordered proteins, allosteric regulation, and protein-DNA interactions. The findings may also interest computational biophysicists developing methods for studying IDR-mediated regulation and drug discovery efforts targeting p53.
- **Major strengths** 1) The study addresses a significant gap in understanding how IDRs regulate structured domains, using p53 as a relevant model system. 2) The integration of multiple computational approaches (MD, FEL, DCC, MM-GBSA) provides a comprehensive view of the proposed mechanism. 3) The two-step allosteric model is clearly articulated and testable. 4) The inclusion of in silico mutagenesis strengthens the causal claims. 5) The authors acknowledge limitations of MM-GBSA and interpret results cautiously.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** The lack of experimental validation for the proposed mechanism, the absence of convergence analysis for the MD simulations, and the insufficient justification for the choice of collective variables in the FEL analysis.
- **Assessment against Nature-style criteria** **Originality**: Moderate. The concept of IDR-mediated allosteric regulation is not new, but the specific application to p53 CTD-DBD communication and the two-step mechanism offer some novelty. **Scientific importance**: High for the p53 field and IDR biology, but the purely computational nature limits immediate impact. **Interdisciplinary readership**: Moderate. The work bridges structural biology, biophysics, and computational chemistry, but may not attract broad readership beyond these fields. **Technical soundness**: Generally sound, but several methodological details require clarification and additional validation. **Readability for nonspecialists**: The manuscript is well-structured and clearly written, though some technical sections may be challenging for non-computational readers.
- **Recommendation posture** Supportive if technical concerns are resolved and additional validation is provided.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that the CTD "enhances the allosteric regulatory mechanisms" and that the identified allosteric network "promotes the binding of DBD to DNA."
- **Evidence pointer** Figures 4, 5, 6; Tables S1–S4
- **Concern** The central claim of CTD-mediated allosteric regulation relies entirely on computational predictions without any experimental validation. While the simulations are internally consistent, the absence of experimental corroboration (e.g., mutagenesis studies, binding assays, or NMR/SAXS experiments) leaves the proposed mechanism as a hypothesis rather than an established finding. The in silico mutagenesis is a step in the right direction, but it does not substitute for wet-lab validation.
- **Why it matters** The manuscript's primary contribution is a mechanistic model with potential implications for drug design. Without experimental support, the model's predictive power and biological relevance remain uncertain. The p53 field has a history of conflicting computational predictions that were not borne out experimentally.
- **Resolution test** Provide experimental validation of the proposed mechanism, such as site-directed mutagenesis of key residues (e.g., R379, F212, R280) followed by DNA binding assays, or biophysical characterization of the CTD-DBD interaction. Alternatively, clearly frame the work as a predictive model requiring experimental testing.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the RMSD values for all four systems fluctuated within a certain range, suggesting that the system had generally reached a stable state."
- **Evidence pointer** Figure 2A; Section 2
- **Concern** The manuscript does not provide convergence analysis for the MD simulations. Merely observing RMSD plateau is insufficient to establish equilibration, especially for IDR-containing systems that may sample multiple metastable states. No block averaging, autocorrelation analysis, or replica comparisons are presented. The 1 μs simulation time per system may also be insufficient for full conformational sampling of the disordered CTD.
- **Why it matters** Without demonstrated convergence, the FELs and DCC analyses may reflect incomplete sampling rather than equilibrium properties. This undermines the reliability of the proposed allosteric mechanism.
- **Resolution test** Provide convergence metrics (e.g., RMSD block averaging, time-dependent FEL evolution, or comparison of independent trajectories). Justify the simulation length based on the timescales of CTD conformational dynamics.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Methodological justification
- **Claim pointer** The authors use two sets of collective variables for FEL construction, including distances between CA atoms of specific residue pairs (R158-F212, R156-D208, K120-R280).
- **Evidence pointer** Section 4.2.1; Figures 7, S4, S5
- **Concern** The choice of collective variables is not justified. It is unclear why these specific residue pairs were selected and whether they adequately capture the relevant conformational changes. The manuscript does not discuss alternative CVs or validate that the chosen CVs distinguish functionally distinct states.
- **Why it matters** The FEL interpretation depends critically on the quality of the CVs. Poorly chosen CVs can lead to misleading conclusions about conformational states and transitions.
- **Resolution test** Justify the CV selection based on prior structural knowledge, PCA analysis, or other systematic approaches. Show that the CVs capture known functional states of p53 DBD.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of results
- **Claim pointer** The authors state that "the CTD directly interacts with DNA through electrostatic interactions, expanding the interface of p53 binding with DNA."
- **Evidence pointer** Figure 5; Section 2.2
- **Concern** The claim that the CTD "expands the interface" is not directly supported by the data presented. The contact probability maps and binding free energy decomposition show increased interactions, but the spatial extent of the binding interface is not quantified. The term "expanding" implies a geometric change that is not demonstrated.
- **Why it matters** The proposed mechanism of interface expansion is a key component of the two-step model. If the CTD merely adds additional contacts without altering the DBD-DNA interface geometry, the mechanistic interpretation would differ.
- **Resolution test** Quantify the binding interface size (e.g., number of contacting residues, buried surface area) in both systems and show a statistically significant increase in the presence of CTD.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, Conclusions
- **Issue** The abstract states "the conformation of DBD changes on the S6-S7 loop and L1 upon DNA binding" but does not specify the nature of the change (e.g., open vs. closed state, increased flexibility).
- **Required correction** Briefly describe the conformational change (e.g., "the S6-S7 loop transitions to a closed state") in the abstract for clarity.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Section 4.1
- **Issue** The manuscript states that "two independent, unbiased molecular dynamics (MD) simulations" were performed for each system, but the initial velocities or starting configurations for the replicas are not described.
- **Required correction** Specify how the independent simulations were initiated (e.g., different random seeds, different initial velocities) to ensure reproducibility.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results
- **Evidence pointer** Figure 5; Section 2.2
- **Issue** The binding free energy values are reported as single numbers without error estimates or statistical significance testing.
- **Required correction** Provide standard errors or confidence intervals for the binding free energy calculations, and state whether differences between systems are statistically significant.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction
- **Evidence pointer** Section 1
- **Issue** The introduction cites several studies on p53 IDRs but does not discuss recent experimental work on CTD-DNA interactions that may be relevant to the proposed mechanism.
- **Required correction** Add a brief discussion of experimental studies on CTD-DNA binding and how the current computational findings relate to or extend those observations.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 2
- **Evidence pointer** Figure 2
- **Issue** The RMSD and Rg plots are described but not shown in the provided text. The figure legends are not available for assessment.
- **Required correction** Ensure all figures are clearly labeled with axes, units, and legends, and that the main text refers to specific panels.

## Risk / unsupported claims
- The claim that the CTD "enhances the allosteric regulatory mechanisms" is not directly supported by quantitative comparison of allosteric network properties between systems with and without CTD.
- The statement that the identified allosteric network "promotes the binding of DBD to DNA" implies causality that is not established by correlational analyses (DCC, contact maps).
- The claim that the CTD "expands the interface" of p53-DNA binding is not quantified.
- The assertion that the proposed mechanism "will provide new insights into the functional mechanisms of the p53 CTD and inform the rational design of p53-targeted drugs" is speculative and not supported by the data presented.
- The statement that "the CTD regulates the global allosteric network of the DBD" is based on computational predictions without experimental validation.
- The claim that DNA binding "promotes population shifts in the conformation (S6-S7 loop)" is based on FEL analysis but the statistical significance of the population differences is not reported.