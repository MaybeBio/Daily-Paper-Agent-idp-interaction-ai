## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, and supplementary figure references
- **Assessment boundary** Scientific validity, methodological rigor, interpretation of results, and alignment with claims made in the abstract and discussion
- **Shared manuscript claim summary** The authors use molecular dynamics simulations of full-length p53 (including intrinsically disordered N- and C-terminal regions) to show that the Y220C mutation disrupts DNA-binding through long-range allosteric effects, and that PK11000 partially restores wild-type-like behavior primarily through electrostatic and hydrogen-bonding networks rather than large-scale structural changes. They also compare full-length versus DBD-only simulations to argue that the disordered termini are essential for capturing true p53 dynamics.
- **Visible evidence base** Results sections on global structural measures (Euclidean RMSD, dihedral RMSD, RMSF, secondary structure), cluster analysis, hydrogen bonding analysis, electrostatic network analysis, and FL|DBD versus DBD comparisons. Figures referenced include Figures 1–5 and supplementary Figures S1–S10, Tables T1–T3.
- **Missing materials affecting confidence** Actual figure images and numerical values in tables are not provided in the manuscript text; only figure captions and in-text descriptions are available. Simulation input files and parameter details are referenced but not included. The specific statistical tests used for significance are not described.

## Reviewer
- **Overall assessment** This manuscript presents a computationally intensive study of full-length p53 dynamics, addressing an important gap in the field where most simulations have focused on the DBD in isolation. The methodological choices are thoughtful, particularly the use of dihedral RMSD for disordered proteins and the comparison between FL and DBD systems. However, the central claims of "allosteric restoration" by PK11000 are supported by relatively subtle differences in the presented metrics, and the manuscript lacks clear statistical frameworks to distinguish genuine effects from simulation noise. The work is potentially valuable as a methodological contribution and hypothesis-generating study, but the current evidence does not fully establish the mechanistic conclusions drawn.
- **Who would be interested in the results, and why** Researchers studying p53 structure and dynamics, computational biophysicists interested in intrinsically disordered proteins, and medicinal chemists working on p53 reactivation strategies. The methodological pipeline for analyzing full-length disordered proteins with small-molecule binding could be of broader interest to the molecular simulation community.
- **Major strengths** 1) Addresses a significant gap by simulating full-length p53 including disordered termini, which most prior studies neglect. 2) Thoughtful adaptation of analysis metrics (dihedral RMSD) for intrinsically disordered systems. 3) Direct comparison between FL and DBD simulations provides insight into the limitations of truncated constructs. 4) The proposed "partial restoration" concept for drug efficacy is biologically plausible and clinically relevant.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (statistical rigor), R1-M2 (force field validation for IDPs), R1-M3 (covalent bond parameterization), R1-M4 (convergence assessment)
- **Assessment against Nature-style criteria** **Originality**: Moderate. The application of full-length p53 simulations is novel, but the overall approach follows established methods. **Scientific importance**: Moderate. The findings could inform drug design, but the mechanistic claims are not fully supported. **Interdisciplinary readership**: Limited. The manuscript is highly technical and would primarily appeal to computational biophysicists and p53 specialists. **Technical soundness**: Questionable in several areas as detailed in the concerns. **Readability for nonspecialists**: The manuscript is dense and assumes significant background knowledge; the abstract is accessible but the body requires expertise in MD simulations.
- **Recommendation posture** Supportive if technical concerns are resolved. The study addresses an important question and the methodological framework is promising, but the current evidence does not fully establish the allosteric restoration mechanism claimed.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The manuscript claims that PK11000 "restores wild-type-like behavior" in the Y220C mutant based on differences in hydrogen bonding and electrostatic metrics.
- **Evidence pointer** Results sections on Hydrogen Bond Analysis and Electrostatic Network Analysis; Figures 4 and 5
- **Concern** The manuscript reports differences in hydrogen bonding metrics (TRT, EHBS) and electrostatic network properties between constructs, but no statistical analysis is presented. With only four replicates per construct, it is unclear whether the observed differences (e.g., TRT of 13.9 for Y220C vs. 15.3 for Y220C_PK11000) are statistically significant or within the range of natural variation between independent simulations. The authors do not report standard deviations, confidence intervals, or any significance testing.
- **Why it matters** The central claim of the paper is that PK11000 restores wild-type-like behavior. Without statistical validation, the observed differences could be attributed to sampling noise, particularly given the high conformational variability of intrinsically disordered proteins. This undermines the primary conclusion.
- **Resolution test** Provide per-replicate values with means and standard deviations for all key metrics. Apply appropriate statistical tests (e.g., t-tests, Mann-Whitney U tests, or permutation tests) to compare constructs. Report effect sizes and confidence intervals. If differences are not statistically significant, temper the claims accordingly.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Force field validation
- **Claim pointer** The authors state that the ff14SB force field was selected "owing to its robust performance and reliable agreement with p53 DBD simulations" and that it was chosen over ff19SB due to "limited experimental validation."
- **Evidence pointer** Methods section, Force Field and Parameter Selection
- **Concern** The manuscript does not provide evidence for the claim that ff14SB is appropriate for simulating intrinsically disordered proteins. Standard fixed-charge force fields like ff14SB are known to produce overly compact conformations for IDPs and may not accurately sample the conformational ensemble. The authors acknowledge that ff19SB was considered but do not provide comparative data showing that ff14SB performs adequately for the disordered regions of p53. The statement that ff19SB has "limited experimental validation" is not substantiated with references.
- **Why it matters** The disordered N- and C-terminal regions are central to the study's claims about allosteric regulation. If the force field does not accurately model these regions, the conclusions about their role in mediating the effects of the Y220C mutation and PK11000 binding could be artifacts of the force field rather than genuine biological properties.
- **Resolution test** Provide validation data comparing simulated ensembles of the disordered regions against experimental data (e.g., SAXS, NMR chemical shifts, or FRET measurements). Alternatively, run test simulations with multiple force fields (e.g., ff19SB, CHARMM36m, or a99SB-disp) and show that the key conclusions are robust across force field choices. If such validation is not feasible, acknowledge this limitation explicitly and temper claims about the disordered regions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Ligand parameterization
- **Claim pointer** The manuscript states that PK11000 was "covalently bonded to Cys182, as described by Han et al." and that parameters were derived using GAFF2.
- **Evidence pointer** Methods section, Force Field and Parameter Selection
- **Concern** The manuscript does not describe how the covalent bond between PK11000 and Cys182 was modeled. Details such as the atom types, bond parameters, partial charges, and any constraints or restraints applied are not provided. The authors also do not specify whether the covalent bond was formed spontaneously during the simulation or was pre-formed in the initial structure. The reference to Han et al. is insufficient without specific parameter details.
- **Why it matters** The interaction between PK11000 and the protein is central to the study. If the covalent bond is not modeled correctly, the observed effects of PK11000 on the protein's dynamics and electrostatic network could be incorrect. Reproducibility is also compromised without these details.
- **Resolution test** Provide complete parameter files for PK11000, including the covalent linkage to Cys182, in the supplementary materials. Describe the charge derivation method (e.g., RESP fitting) and any validation of the ligand parameters (e.g., comparison to experimental data or QM calculations). If the covalent bond was pre-formed, justify this choice and discuss potential limitations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Convergence and sampling
- **Claim pointer** The authors claim that their simulations provide "a first-order exploration into the behavior of full-length p53" and draw conclusions about the effects of the Y220C mutation and PK11000.
- **Evidence pointer** Methods section, Molecular Dynamics Simulations; Results sections throughout
- **Concern** The manuscript does not provide sufficient evidence that the simulations have converged. For a protein with large disordered regions, microsecond timescales may not be sufficient to sample the conformational ensemble adequately. The authors do not report block averaging, autocorrelation times, or other convergence metrics. The use of only four replicates per construct, while reasonable for a starting point, may not capture the full conformational diversity of the system.
- **Why it matters** If the simulations have not converged, the observed differences between constructs could reflect incomplete sampling rather than genuine biophysical differences. This is particularly concerning for the disordered regions, which may require much longer timescales or enhanced sampling methods to equilibrate.
- **Resolution test** Provide convergence metrics such as RMSD vs. time plots for all replicates, block-averaged property estimates, and autocorrelation times for key observables. Consider running additional replicates or longer simulations to confirm that the reported differences are stable. If convergence is not achieved, acknowledge this limitation and frame the results as preliminary.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of electrostatic network analysis
- **Claim pointer** The authors claim that the electrostatic network analysis reveals "a large restorative effect by PK11000" in the Y220C mutant, particularly in the N-terminal domain and residues 50–85.
- **Evidence pointer** Results section, Electrostatic Network Analysis; Figure 5
- **Concern** The electrostatic network analysis methodology is described only briefly, and the interpretation of "embedding error" as a measure of similarity to the wild-type network is not fully justified. The authors do not explain how the thresholding (0.003) was chosen or how sensitive the results are to this parameter. The claim that specific residues (E68, A84, P85, S166, K305, K382) show "significant rescue" is not supported by any statistical measure of significance.
- **Why it matters** The electrostatic network analysis is a key piece of evidence for the proposed mechanism of PK11000 action. If the methodology is not robust or the interpretation is not well-justified, the conclusions drawn from this analysis are weakened.
- **Resolution test** Provide a more detailed description of the network analysis methodology, including how the threshold was determined and how sensitive the results are to this choice. Include error bars or confidence intervals for the embedding error values. Justify the interpretation of embedding error as a measure of "rescue" and discuss potential alternative interpretations.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the study "advances understanding of its regulatory mechanisms and sets the stage for developing targeted therapies," which overstates the direct therapeutic implications of a computational study.
- **Required correction** Soften the language to reflect that this is a computational study that provides hypotheses to be tested experimentally, rather than a direct step toward therapy development.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Methods section, Molecular Dynamics Simulations
- **Issue** The manuscript states that "simulations were set up and carried out on Wesleyan University's High Performance Computing Cluster" but does not provide specific software versions, hardware details, or the exact commands used for simulation setup and analysis.
- **Required correction** Provide the AMBER version, GPU/CPU specifications, and key input file examples in the supplementary materials to ensure reproducibility.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figures 1–5
- **Evidence pointer** Results sections referencing Figures 1–5
- **Issue** The manuscript text references figures but the actual figure images are not available for review. Based on the descriptions, some figures appear to be complex and may be difficult to interpret without clear labeling and annotations.
- **Required correction** Ensure all figures are clearly labeled with appropriate axis titles, legends, and annotations. Consider simplifying complex figures or providing additional explanatory text in the captions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction, Recent Insights from MD Simulations of p53
- **Issue** The manuscript cites several relevant studies but does not provide a comprehensive comparison of how the current findings differ from or extend prior computational work on p53, particularly regarding the role of disordered regions.
- **Required correction** Add a more detailed comparison with prior simulation studies of p53, explicitly stating what new information the full-length simulations provide beyond DBD-only studies.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** Abstract, Discussion
- **Issue** The term "allosteric restoration" is used to describe the effects of PK11000, but the mechanism is not fully established. The term implies a specific mechanistic interpretation that may not be warranted by the data.
- **Required correction** Use more neutral language such as "PK11000 binding is associated with changes in the electrostatic network that partially resemble the wild-type pattern" rather than "restoration."

## Risk / unsupported claims
- The claim that PK11000 "restores wild-type-like behavior" in the Y220C mutant is not statistically supported by the presented data.
- The claim that the N- and C-terminal regions "mediate additional allosteric regulation" is based on simulations with a force field that may not accurately model IDPs, and no experimental validation is provided.
- The statement that the ff19SB force field has "limited experimental validation" is not substantiated with references.
- The claim that the observed hydrogen bonding differences indicate "increased DNA binding specificity" is speculative and not directly tested.
- The assertion that the "pipeline developed can be applied to variants of p53" and other protein systems is an extrapolation that is not demonstrated in this study.
- The discussion of why "no successor to PK11000 has been discovered" is speculative and not directly supported by the data presented.