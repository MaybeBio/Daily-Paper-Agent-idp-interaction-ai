## Review setup
- **Input scope** Full manuscript text including abstract, main text, methods, and figure legends
- **Assessment boundary** Scientific content, technical soundness, and claims as presented in the provided manuscript material
- **Shared manuscript claim summary** The authors propose that oligomerization state and sequence patterning jointly and asymmetrically tune the miscibility of multiphase biomolecular condensates, using coarse-grained simulations and in vivo reconstitution in mammalian and yeast cells
- **Visible evidence base** Main text Figures 1-6, Extended Data Figures 1-5, Extended Data Tables 1-3, Methods section
- **Missing materials affecting confidence** Supplementary Tables 1 and 2, uncropped source images, full statistical source data, and details of data availability are referenced but not provided

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question in the field of biomolecular condensates: how multiphase organization is encoded by molecular features. The combination of coarse-grained simulations with in vivo reconstitution is well conceived, and the central claim of asymmetric oligomerization effects is potentially significant. However, the evidence as presented has several gaps that prevent full confidence in the conclusions. The simulation results are described qualitatively in places, and the experimental quantification of valence and its relationship to the observed phenotypes requires more rigorous treatment. The claim of asymmetry, while supported by the data shown, would benefit from a more systematic exploration of parameter space and a clearer connection between the simulation observable (interfacial tension) and the experimental observable (CTC distance). The manuscript is well written and likely to interest a broad readership, but the technical concerns outlined below should be addressed before the case is fully established.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, intracellular organization, and biophysics. The work is also relevant to those studying the role of oligomerization in protein function and to synthetic biologists interested in designing multiphase compartments. The combination of in vivo and in silico approaches broadens the appeal.
- **Major strengths** The study addresses a fundamental question about the molecular determinants of multiphase condensate organization. The use of orthogonal, engineered core systems in yeast is a powerful approach to isolate specific variables. The combination of simulations and experiments is complementary and mutually reinforcing. The finding of asymmetry is conceptually novel and has implications for how cells might regulate condensate organization.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** 
  - **Originality** High. The concept of asymmetric oligomerization as a tunable mechanism for condensate miscibility is novel and extends beyond prior work on sequence patterning alone.
  - **Scientific importance** High. Understanding how multiphase condensates are organized is crucial for understanding their biological function. This work provides a new mechanistic principle that could be broadly applicable.
  - **Interdisciplinary readership** High. The work bridges biophysics, cell biology, and synthetic biology, and the findings are conceptually accessible to a broad scientific audience.
  - **Technical soundness** Moderate. The overall approach is sound, but several technical aspects require clarification and additional analysis to fully support the claims (see Major Concerns).
  - **Readability for nonspecialists** Good. The manuscript is clearly written, with helpful schematics. The concepts are introduced in an accessible manner, although some simulation details may be challenging for non-experts.
- **Recommendation posture** Supportive if technical concerns are resolved. The central hypothesis is interesting and the preliminary evidence is promising, but the current manuscript does not fully establish the case due to the concerns detailed below.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that "increasing the oligomerization state of an intrinsically disordered protein results in enhanced immiscibility and multiphase formation" is central to the paper.
- **Evidence pointer** Figure 1c, 1d; Figure 4; Figure 6
- **Concern** The quantitative relationship between the oligomerization state (valence, f) and the degree of immiscibility is not rigorously established. In the simulations, the partitioning Kp is reported for different f values, but the statistical significance of the differences is not fully addressed. In the experiments, the "valence" is modulated by co-expressing free core subunits, but the actual effective valence at the condensate level is not measured or calculated. The relationship between the nominal valence (based on expression levels) and the effective valence (number of IDPs per condensate) is unclear.
- **Why it matters** The central claim of the paper is that oligomerization state is a key variable. Without a clear and quantitative link between the manipulated variable (valence) and the observed outcome (miscibility), the strength of this claim is weakened. The paper would be significantly strengthened by a more direct measurement or calculation of the effective valence in the experimental system.
- **Resolution test** Provide a quantitative analysis of the simulation data, including error bars and statistical tests, to demonstrate that the changes in Kp with f are significant. In the experimental system, either measure the effective valence directly (e.g., via single-molecule counting or fluorescence correlation spectroscopy) or provide a more detailed model that relates the expression levels of free cores to the effective valence of the condensates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that the effect of oligomerization is "asymmetric," with a greater effect when the IDR with stronger homotypic interactions is oligomerized.
- **Evidence pointer** Figure 5, Figure 6
- **Concern** The experimental evidence for asymmetry (Figure 5) is based on a limited number of IDR pairs and core combinations. The simulation evidence (Figure 6) uses interfacial tension as a proxy for immiscibility, but the connection between this observable and the experimental CTC distance is not explicitly demonstrated. The authors state that the effect is "more pronounced" for the stronger homotypic IDR, but the data in Figure 5 appear to show a more complex pattern, with some combinations showing little difference. A more systematic exploration of the parameter space (e.g., varying the strength of homotypic interactions more continuously) would strengthen the claim of asymmetry.
- **Why it matters** The asymmetry is a key conceptual finding of the paper. If it is not robustly demonstrated, the broader implications for how cells might use oligomerization to tune organization are less compelling.
- **Resolution test** Provide a more comprehensive dataset, either experimental or computational, that systematically varies the homotypic interaction strength and the oligomerization state of each component. This would allow a more definitive test of the asymmetry hypothesis. In the simulations, explicitly show how the interfacial tension correlates with the CTC distance measured in experiments.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that the simulation model captures the essential physics of the experimental system.
- **Evidence pointer** Methods section, Figure 1, Figure 6
- **Concern** The simulation model uses a coarse-grained "hydrophobicity scale-implicit solvent model" with "sticker" and "spacer" representations. The mapping between this model and the specific IDRs used in experiments (FUSN, hnRNPA1C, DDX4N) is not described in detail. The parameters used (e.g., interaction strengths, chain lengths) are not justified in the context of the experimental systems. The temperature of 250 K is used, which is below the critical temperature of the lowest-Tc sequence, but the relationship between this simulation temperature and the physiological temperature of the experiments is not discussed.
- **Why it matters** For the simulations to be a valid test of the hypothesis, the model must be a reasonable representation of the experimental systems. Without a clear mapping and parameter justification, it is difficult to assess whether the simulation results are directly relevant to the experimental observations.
- **Resolution test** Provide a more detailed description of the model parameters and how they relate to the specific IDRs used. Include a discussion of the sensitivity of the results to the choice of parameters. If possible, perform simulations with parameters that more closely mimic the specific sequences used in the experiments.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that the orthogonal core systems are truly orthogonal and that the observed behavior is due to the IDRs, not the cores.
- **Evidence pointer** Figure 3, Extended Data Figure 2
- **Concern** The orthogonality of the cores is tested by showing that free cores are not recruited to condensates formed by a different core. However, this test is performed with free cores, not with cores fused to IDRs. It is possible that the IDR fusion could alter the core's surface properties and lead to non-specific interactions. Additionally, the potential for the cores themselves to contribute to the phase behavior (beyond just providing oligomerization) is not fully addressed.
- **Why it matters** The experimental system is designed to isolate the effect of the IDRs. If the cores are not truly orthogonal or contribute directly to the phase behavior, the interpretation of the results in terms of IDR sequence and oligomerization is compromised.
- **Resolution test** Perform additional control experiments, such as testing the orthogonality of cores fused to IDRs, or using cores with mutations that disrupt their self-assembly. Also, include a control where the core is fused to a non-phase-separating protein to assess the core's contribution.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1b
- **Evidence pointer** Figure 1b
- **Issue** The density profiles in Figure 1b are described as showing "two compositionally distinct phases" for some pairs, but the visual difference between the profiles for different pairs is not always clear.
- **Required correction** Consider using a more quantitative metric to display the density profiles, such as the difference in density between the two phases, or provide a more detailed description of the profiles in the figure legend.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 3f
- **Evidence pointer** Figure 3f
- **Issue** The normalized CTC distance is described as a measure of miscibility, but the relationship between this metric and the physical state of the condensates (e.g., fully mixed, partially mixed, phase-separated) is not explicitly defined.
- **Required correction** Provide a clear definition of what different values of the normalized CTC distance mean in terms of the physical state of the condensates.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section
- **Evidence pointer** Methods section
- **Issue** The methods for image analysis and quantification of the CTC distance are described, but some details are missing, such as the number of cells analyzed per condition and the criteria for selecting cells for analysis.
- **Required correction** Provide more details on the image analysis, including the number of biological replicates and cells analyzed, and the criteria for including/excluding cells.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion of the potential biological implications of the asymmetric oligomerization effect is somewhat speculative and could be more focused.
- **Required correction** Consider tightening the discussion to focus on the most direct implications of the findings and how they might be tested in future work.

## Risk / unsupported claims
- The claim that the effective valence in the experimental system is directly related to the expression levels of free core subunits is not supported by direct measurement.
- The claim that the simulation model is a quantitatively accurate representation of the specific IDRs used in the experiments is not fully supported, as the parameter mapping is not detailed.
- The claim that the observed asymmetry is a general principle, rather than a specific feature of the tested IDR pairs, is not fully supported by the limited number of pairs tested.
- The claim that oligomerization could be a mechanism for regulating condensate organization in cells is plausible but speculative and not directly tested here.