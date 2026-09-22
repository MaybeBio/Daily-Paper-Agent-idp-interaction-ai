## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusions, methods) without supplementary materials
- **Assessment boundary** Scientific validity of the computational approach, consistency between claims and evidence presented, methodological soundness, and interpretation of results
- **Shared manuscript claim summary** The authors use umbrella sampling molecular dynamics simulations with the average backbone psi angle as a reaction coordinate, complemented by PM7 semi-empirical and M06-2X/6-31+G* density functional theory calculations, to estimate free energy profiles for helix-to-beta-sheet interconversion in amyloid-forming peptide sequences from amyloid-beta (KLVFFA) and tau (QVEVKSEKLD, VQIVYKPVD) proteins, with penta-alanine as a control
- **Visible evidence base** Main text figures (Figures 1-8), tables referenced in supplementary (Tables S1-S4), equations (1) and (2), and methodological descriptions in Section 4
- **Missing materials affecting confidence** Supplementary figures and tables (Figures S1-S8, Tables S1-S4) are referenced but not provided; convergence criteria for umbrella sampling simulations are not reported; force field parameters and validation details are incomplete; no error analysis for QM calculations is provided

## Reviewer

- **Overall assessment** The manuscript addresses a relevant question in the field of amyloid aggregation, namely the molecular determinants of amyloid-forming propensity in peptide sequences from disease-relevant proteins. The methodological combination of enhanced sampling simulations with QM-based validation is conceptually sound and potentially useful. However, the study suffers from several significant limitations that undermine the strength of the conclusions. The use of a single reaction coordinate (average psi angle) to describe a complex conformational transition is a simplification that requires more careful justification. The comparison between force-field-based free energies and QM single-point energies is not straightforward, as these quantities are not directly comparable. The reported energy differences, particularly the approximately 100 kcal/mol difference between alpha-helix and beta-sheet forms in DFT calculations, are physically unreasonable and attributed to neglect of solvation, which raises questions about the validity of the QM approach for this purpose. The control system (penta-alanine) is used appropriately, but the interpretation of its behavior is limited. The force-field comparison study is a positive addition but is only performed for one peptide system. Overall, the manuscript presents interesting preliminary data but does not fully establish the claimed general principles about amyloid-forming tendency.

- **Who would be interested in the results, and why** Computational biophysicists and molecular modelers studying protein aggregation and conformational transitions would find the methodological approach of interest. Researchers working on Alzheimer's disease mechanisms, particularly those focused on the molecular basis of amyloid formation by Abeta and tau peptides, may find the comparative analysis of different peptide sequences useful. The study could also be relevant to groups developing computational screening approaches for amyloidogenic sequences or testing force field performance for disordered and aggregating peptides.

- **Major strengths** The manuscript addresses a question of genuine biological and medical relevance, namely why certain peptide sequences from amyloidogenic proteins preferentially form beta-sheet-rich aggregates. The combination of multiple computational methods (umbrella sampling, semi-empirical QM, DFT) to cross-validate results is a commendable approach. The inclusion of a control system (penta-alanine) is methodologically appropriate. The investigation of force field effects on the results is a valuable contribution, as it highlights the sensitivity of such calculations to the choice of simulation parameters. The use of a reaction coordinate that has been previously validated in the literature provides some foundation for the methodological choices.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Validity of approach
- **Claim pointer** The manuscript claims that the calculated free energy profiles predict the relative stability of alpha-helix versus beta-sheet conformations for the studied peptide sequences, and that these predictions are validated by QM calculations.
- **Evidence pointer** Figures 2, 3, 5, 6; Section 2, Section 4.2, Section 4.3
- **Concern** The use of the average backbone psi angle as a single reaction coordinate to drive helix-to-sheet interconversion is problematic. The average psi angle is a collective variable that may not adequately distinguish between different conformational states, particularly for longer peptides where individual residues can adopt different secondary structures simultaneously. The authors do not demonstrate that this reaction coordinate provides a proper description of the conformational landscape, nor do they validate that the sampled conformations at each psi value are representative of the true ensemble. Furthermore, the free energy profiles obtained from umbrella sampling are compared directly with QM single-point energies calculated on a limited number of extracted configurations (10-20 per psi value). These are fundamentally different quantities: the former represents a potential of mean force including entropic contributions, while the latter are enthalpic estimates for specific configurations without thermal averaging. The comparison is therefore not quantitatively meaningful.
- **Why it matters** The central conclusions of the manuscript rest on the validity of the free energy profiles and their interpretation. If the reaction coordinate does not properly capture the conformational transition, or if the QM calculations are not comparable to the force-field results, then the claimed findings about the relative stability of different secondary structures are not established. This affects the core message of the manuscript.
- **Resolution test** The authors should validate the reaction coordinate by comparing with alternative collective variables or by demonstrating that the sampled ensembles at each psi value are converged and representative. They should also clarify the relationship between the QM single-point energies and the force-field free energies, possibly by computing QM energies on a larger set of configurations and comparing trends rather than absolute values. Alternatively, they could perform QM calculations on optimized structures representing each conformational state.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of results
- **Claim pointer** The manuscript claims that the DFT calculations show the beta-sheet form is preferred for the QVEVKSEKLD dimer, with an energy difference of approximately 100 kcal/mol, and attributes this to neglect of solvation effects.
- **Evidence pointer** Section 2, Figure 4
- **Concern** An energy difference of approximately 100 kcal/mol between two conformational states of a small peptide dimer is physically implausible, even in the gas phase. Such a large difference suggests either that the conformations being compared are not properly equilibrated or representative, that the QM method is being applied outside its valid domain, or that the comparison is between non-equivalent states. The attribution of this large difference to neglect of solvation is not convincing, as solvation effects for a decapeptide dimer would typically be on the order of tens of kcal/mol at most. This result undermines confidence in the QM calculations as a validation method.
- **Why it matters** The QM calculations are presented as validation of the force-field results. If the QM results are not physically reasonable, they cannot serve this purpose. The large energy difference also raises questions about whether the conformations sampled at different psi values are structurally meaningful and whether the QM calculations are being performed on appropriate geometries.
- **Resolution test** The authors should investigate the structural differences between the conformations at the two minima and identify the specific interactions responsible for the large energy difference. They should also test the effect of implicit solvation models on the QM energies. If the large energy difference persists, they should provide a detailed physical explanation or reconsider whether the QM approach is appropriate for this system.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Completeness of evidence
- **Claim pointer** The manuscript claims that the free energy profiles for the tau peptide sequences show a shallow second minimum for beta-sheet conformations, in contrast to the deeper minimum observed for KLVFFA, and interprets this as indicating a lower propensity for beta-sheet formation in the tau sequences.
- **Evidence pointer** Figure 3, Tables S2 and S3
- **Concern** The interpretation of the free energy profiles for the tau peptide sequences is based on visual inspection of the profiles and qualitative comparison with the KLVFFA results. The authors do not provide quantitative measures of the depth of the minima, the barrier heights, or the relative populations of the different conformational states. The claim that the second minimum is "not very deep" is subjective and not supported by numerical analysis. Additionally, the free energy profiles for the tau sequences are only shown for the parallel dimer configuration, not for the antiparallel configuration, which limits the generality of the conclusions.
- **Why it matters** The manuscript aims to compare the amyloid-forming tendencies of different peptide sequences. Without quantitative analysis of the free energy profiles, the comparison remains qualitative and the conclusions are not robust. The lack of data for the antiparallel configuration of the tau dimers means that the conclusions may not be general.
- **Resolution test** The authors should provide quantitative analysis of the free energy profiles, including the depths of the minima, barrier heights, and estimated relative populations of the conformational states. They should also perform and present results for the antiparallel configuration of the tau dimers to enable a complete comparison.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Methodological rigor
- **Claim pointer** The manuscript claims that the umbrella sampling simulations were performed with sufficient sampling to obtain reliable free energy profiles, citing a maximum standard error of less than 0.05 kcal/mol.
- **Evidence pointer** Section 2, Section 4.2
- **Concern** The reported standard error of less than 0.05 kcal/mol is surprisingly low for umbrella sampling simulations of peptide conformational transitions. The authors do not report the number of independent simulations, the total simulation time per window, or the convergence criteria used. The statement that "the input configuration for each simulation was taken from the previous simulation" suggests a sequential sampling approach that may not provide independent samples and could lead to hysteresis or inadequate sampling of orthogonal degrees of freedom. The lack of convergence analysis (e.g., block averaging, multiple independent runs) makes it difficult to assess the reliability of the reported free energy profiles.
- **Why it matters** The reliability of the free energy profiles is central to the conclusions of the manuscript. If the sampling is inadequate or the error estimates are not meaningful, the reported profiles may not be accurate, and the conclusions drawn from them may be incorrect.
- **Resolution test** The authors should provide detailed information about the simulation setup, including the number of windows, simulation time per window, and convergence analysis. They should also perform multiple independent umbrella sampling runs to assess the reproducibility of the free energy profiles.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2, Figure 2
- **Evidence pointer** Figure 2
- **Issue** The description of the free energy profiles in Figure 2 is somewhat unclear. The authors state that the monomer has a "flat minimum" between -30 and 30 degrees, but the figure is not available for inspection. The text also mentions that the coil-like structure corresponds to a minimum, which is surprising, but the explanation provided is brief.
- **Required correction** The authors should provide a more detailed description of the free energy profiles, including the numerical values of the minima and barriers, and clarify the structural features of the conformations at each minimum.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 4.3
- **Evidence pointer** Section 4.3
- **Issue** The description of the QM calculations is incomplete. The authors state that PM7 and M06-2X calculations were performed but do not provide details about the basis set superposition error correction, the treatment of solvation, or the convergence criteria for the SCF calculations.
- **Required correction** The authors should provide complete details of the QM calculations, including any corrections applied and the software settings used.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Section 2.2
- **Evidence pointer** Figure S8, Table S4
- **Issue** The comparison between the FF03 and ff99SB*-ILDN force fields is presented as showing that the force field affects the relative populations of secondary structures. However, the authors do not discuss the implications of this finding for the general conclusions of the manuscript. If the results are force-field dependent, this raises questions about the robustness of the conclusions.
- **Required correction** The authors should discuss the implications of the force-field dependence for the interpretation of their results and for the general applicability of their findings.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Section 1, Equations (1) and (2)
- **Evidence pointer** Equations (1) and (2)
- **Issue** The equations are presented without proper context or derivation. Equation (1) appears to be the standard WHAM equation but is not labeled as such. Equation (2) defines the total energy as a sum of van der Waals and electrostatic contributions but does not clarify whether this is the force field energy or a QM energy.
- **Required correction** The authors should provide proper context for the equations and clarify their meaning and origin.

- **Technical failings that need to be addressed before the case is established** The comparison between force-field free energies and QM single-point energies is not methodologically justified and needs to be reconsidered. The lack of convergence analysis for the umbrella sampling simulations needs to be addressed. The physical reasonableness of the QM energy differences needs to be investigated and explained. The quantitative analysis of the free energy profiles needs to be provided.

- **Assessment against Nature-style criteria** 
  - **Originality** The combination of umbrella sampling with QM validation for studying amyloid-forming peptides is not entirely novel, as similar approaches have been reported in the literature. The specific application to the chosen peptide sequences is new, but the methodological approach does not represent a significant advance over existing work.
  - **Scientific importance** The question of why certain peptide sequences form amyloid aggregates is of considerable importance for understanding neurodegenerative diseases. However, the study does not provide definitive answers to this question, and the limitations of the approach prevent strong conclusions from being drawn.
  - **Interdisciplinary readership** The manuscript is likely to be of interest primarily to computational biophysicists and molecular modelers. The connection to Alzheimer's disease may attract readers from the broader neuroscience community, but the highly technical nature of the content may limit accessibility.
  - **Technical soundness** The technical execution of the simulations appears to be standard, but several methodological issues need to be addressed, including the choice of reaction coordinate, the comparison between force-field and QM results, and the lack of convergence analysis.
  - **Readability for nonspecialists** The manuscript is written in a technical style that assumes familiarity with molecular dynamics simulations and QM calculations. The abstract provides a reasonable summary, but the main text would be challenging for nonspecialists to follow.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript addresses a relevant question and employs a reasonable methodological framework, but the major concerns identified above prevent the conclusions from being considered robust. The comparison between force-field and QM results needs to be reconsidered, the convergence of the simulations needs to be demonstrated, and the quantitative analysis of the free energy profiles needs to be provided. If these issues can be addressed, the manuscript could potentially be suitable for publication in a specialized computational biology journal, but in its current form, the case is not established.