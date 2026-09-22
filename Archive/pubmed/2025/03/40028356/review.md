## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, conclusions, methods) without supplementary figures, tables, or supporting information
- **Assessment boundary** Scientific claims, methodological soundness, and evidence consistency as presented in the main text; supplementary materials referenced but not independently verifiable
- **Shared manuscript claim summary** The authors present Mpipi-Recharged, a residue-resolution coarse-grained model that introduces a pair-specific asymmetric Yukawa potential for electrostatic interactions, parameterized from atomistic umbrella sampling simulations. The model is claimed to improve predictions of phase behavior for charge-rich biomolecular condensates, including complex coacervates and RNA–protein systems, relative to symmetric Debye–Hückel treatments.
- **Visible evidence base** Main text figures (Figures 1–5), equations (eqs 1–10), and methods descriptions; supplementary tables and figures referenced but not provided
- **Missing materials affecting confidence** Supplementary figures (S1–S18), tables (S1–S5), amino acid sequences of 46 IDPs, force field parameter details, and simulation convergence data; these are essential for full verification of parameterization and validation claims

## Reviewer
- **Overall assessment** The manuscript addresses a significant and timely problem in the coarse-grained modeling of biomolecular condensates: the inadequate representation of electrostatic interactions in implicit-solvent models. The central idea, that electrostatic attraction and repulsion should be treated asymmetrically and in a pair-specific manner, is physically motivated and supported by the presented atomistic PMF data. The validation against experimental phase behavior for multiple systems is impressive and suggests genuine predictive improvement. However, the manuscript as presented has several technical gaps that prevent full confidence in the claims. The parameterization procedure is described at a level that makes reproduction difficult, the sensitivity of results to the introduced asymmetry is not systematically explored, and the comparison to alternative models is limited to a single variant (HPS-cation-π) for select systems. The limitations section is candid but also reveals that the model's applicability boundaries are not fully mapped. Overall, the work is potentially important and suitable for a high-impact venue, but the current evidence base is insufficient to fully establish the case.

- **Who would be interested in the results, and why** Computational biophysicists and physical chemists working on coarse-grained simulations of biomolecular phase separation, particularly those studying charge-rich systems such as chromatin, RNA–protein granules, and protamine–DNA complexes. The work is also relevant to experimentalists studying condensate stoichiometry and salt sensitivity, as the model offers testable predictions. The methodological advance, asymmetric pair-specific electrostatics, could influence the design of future coarse-grained force fields beyond condensate applications.

- **Major strengths**
  1. The physical insight that electrostatic attraction and repulsion should be parameterized asymmetrically is well-motivated by atomistic simulations and addresses a known limitation of Debye–Hückel-type treatments.
  2. The validation is broad and demanding, covering single-molecule dimensions, homopolymer phase diagrams, charge blockiness effects, complex coacervates, and RNA–protein reentrant behavior.
  3. The model retains the computational efficiency of the original Mpipi framework, making it practical for large-scale simulations.
  4. The candid discussion of limitations, including the mean-field treatment of ions and the simplified RNA representation, is scientifically honest and helps define the model's scope.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "To parameterize the pair-dependent Yukawa function, we use our atomistic PMF results shown in Figure 1" and the associated claim that the model "improves the description of charge effects in biomolecular condensates"
- **Evidence pointer** Methods section, "Mpipi-Recharged Model for Disordered, Globular, and Multidomain Proteins"; Figure 1; Table S3 (referenced)
- **Concern** The parameterization procedure is described only qualitatively. The text states that PMF integrals are used to set Yukawa prefactors, but the exact mapping from PMF curves to Aij values is not specified. Specifically, it is unclear how the "integrals of the attractive part of the corresponding PMF curve" are converted into the prefactor Aij, how the multiplicative factor mentioned in the Methods is determined, and whether this factor is universal or system-dependent. The claim that the model "improves" predictions depends critically on this mapping, and without a reproducible protocol, the scientific case is incomplete.
- **Why it matters** The central methodological advance is the asymmetric parameterization. If the mapping from atomistic PMFs to coarse-grained parameters is not fully specified, other researchers cannot reproduce or build upon the work, and the robustness of the improvement cannot be assessed.
- **Resolution test** Provide a step-by-step parameterization protocol, including the exact functional form of the mapping from PMF integrals to Aij, the value of the multiplicative factor, and a demonstration that the resulting parameters are insensitive to reasonable variations in the fitting procedure. Ideally, include a supplementary table with all Aij values and the corresponding PMF integrals.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Mpipi-Recharged provides excellent agreement with experiments in predicting the phase behavior of highly charged condensates" and the specific validation claims for DDX4, R12, H1–ProTα, and RNA–protein systems
- **Evidence pointer** Figures 2–5; Methods section, "Calculation of Temperature vs Density Phase Diagrams via Direct Coexistence Simulations" and "Estimation of the Critical Temperature via NpT Simulations"
- **Concern** The validation relies on comparisons between simulated critical temperatures (Tc) and experimental saturation concentrations (Csat) or critical salt concentrations. The text states that Tc and Csat are "both good proxies of condensate thermodynamic stability," but the relationship between these quantities is not quantitatively established. For the H1–ProTα system, the comparison is between a simulated salt-concentration-vs-density phase diagram and an experimental phase diagram, but the experimental curve is described only as "red curve" without specifying the experimental method, error bars, or the exact conditions. For the RNA–protein systems, the comparison is between simulated Tc and experimental fluorescence intensities, which are indirect measures of condensate stability. The manuscript does not provide a statistical framework for assessing agreement (e.g., correlation coefficients, confidence intervals, or a defined tolerance for "excellent agreement").
- **Why it matters** The claim of quantitative or near-quantitative agreement is central to the paper's impact. Without a clear definition of what constitutes agreement and a statistical assessment, the strength of the validation is unclear. This is particularly important given that the original Mpipi model already showed qualitative agreement for some systems, and the improvement claim needs to be quantified.
- **Resolution test** Provide a quantitative comparison metric (e.g., correlation coefficient, mean absolute error, or a defined threshold for agreement) for each validation case. For the H1–ProTα phase diagram, specify the experimental method and error bars. For the RNA–protein systems, clarify how fluorescence intensity relates to Tc and whether the comparison is on a linear or logarithmic scale.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** "We show that this asymmetric coarse-graining of electrostatic forces captures intricate effects, such as charge blockiness, stoichiometry variations in complex coacervates, and modulation of salt concentration"
- **Evidence pointer** Figure 3 (DDX4 and R12), Figure 4 (H1–ProTα), Figure 5 (RNA–protein systems)
- **Concern** The manuscript demonstrates that Mpipi-Recharged improves upon the original Mpipi model for the tested systems, but the scope of the improvement is not systematically characterized. For example, the text states that the original Mpipi model "struggles to differentiate" between DDX4 WT and CS variants, but the quantitative difference in Tc between the two models is not given. Similarly, for the RNA–protein systems, the improvement of Mpipi-Recharged over Mpipi is shown for Tc values, but the magnitude of the improvement and its dependence on system properties (e.g., charge density, sequence composition) are not analyzed. The claim that the model captures "charge blockiness" is supported by the DDX4 and R12 results, but the mechanism by which the asymmetric potential achieves this is not explained.
- **Why it matters** The scientific importance of the work depends on the generality of the improvement. If the asymmetric potential only helps for a narrow range of systems, the impact is limited. A systematic analysis of when and why the asymmetry matters would strengthen the case and guide future applications.
- **Resolution test** Provide a systematic comparison of Mpipi-Recharged vs. Mpipi across a broader range of systems or a theoretical analysis of how the asymmetric potential affects phase behavior. At minimum, quantify the improvement for the presented systems and discuss the conditions under which the asymmetry is expected to be most important.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "Mpipi-Recharged provides excellent agreement with experiments in predicting the phase behavior of highly charged condensates" and the specific claim regarding the H1–ProTα system
- **Evidence pointer** Figure 4d; Methods section, "Calculation of Temperature vs Density Phase Diagrams via Direct Coexistence Simulations"
- **Concern** The H1–ProTα system is modeled with a 1:1.2 stoichiometry, described as "nearly electroneutral." However, the sensitivity of the phase diagram to the exact stoichiometry is not explored. Given that the model is designed to capture electrostatic effects, small deviations from electroneutrality could have significant effects on the predicted phase behavior. Additionally, the treatment of the globular domain of H1 as a rigid body is a significant approximation, and the text does not discuss how this approximation might affect the results.
- **Why it matters** The H1–ProTα system is a key validation case, and the model's predictive success depends on the appropriateness of the modeling choices. If the results are highly sensitive to the stoichiometry or the rigid-body approximation, the generality of the approach is questionable.
- **Resolution test** Perform a sensitivity analysis of the H1–ProTα phase diagram to the stoichiometry ratio and to the rigid-body treatment of the globular domain. Discuss the expected impact of these approximations on the results.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "The model ignores ion-specific effects, such as the Hofmeister series or ion-bridging, and the role of multivalent ions, which are likely critical in biomolecular condensates in cells"
- **Evidence pointer** Limitations section
- **Concern** The limitations section correctly identifies the neglect of ion-specific effects as a limitation, but the practical impact of this neglect is not quantified. For the systems studied, the salt concentrations range from approximately 30 mM to 300 mM, and the model's performance is claimed to be good across this range. However, the text does not discuss whether the model's accuracy degrades at higher salt concentrations or in the presence of divalent ions, which are common in cellular environments.
- **Why it matters** The model's applicability to cellular conditions depends on its behavior across a range of ionic conditions. If the model's accuracy is limited to monovalent salts at moderate concentrations, this should be stated explicitly to guide users.
- **Resolution test** Discuss the expected range of validity of the model with respect to salt concentration and ion type, based on the parameterization data and any available test cases.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Introduction, paragraph 3
- **Evidence pointer** "location not provided"
- **Issue** The introduction transitions abruptly from a general discussion of coarse-grained models to the specific limitations of Debye–Hückel treatments. A brief explanation of why the asymmetry in electrostatic interactions arises (e.g., due to ion correlation effects or the discrete nature of charges) would help nonspecialist readers understand the motivation.
- **Required correction** Add one or two sentences explaining the physical origin of the asymmetry between attraction and repulsion in charged systems.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, "Atomistic Umbrella Sampling Molecular Dynamics Simulations"
- **Evidence pointer** "location not provided"
- **Issue** The text states that "three independent runs for each system" were performed, but it is not clear whether these runs were used to estimate statistical errors in the PMF curves or whether the PMF curves were averaged. The error bars in Figure 1d are mentioned, but the propagation of these errors to the model parameters is not discussed.
- **Required correction** Clarify how the three independent runs were used and how statistical uncertainties in the PMF curves were propagated to the Yukawa parameters.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability
- **Affected element** Results, "Mpipi-Recharged Captures the Regulation of the Stability of Complex Coacervates with Salt"
- **Evidence pointer** "location not provided"
- **Issue** The term "critical salt concentration" is used without a formal definition. For readers unfamiliar with coacervate phase behavior, it would be helpful to define this term and explain how it is extracted from the simulations.
- **Required correction** Define "critical salt concentration" and briefly describe how it is determined from the phase diagram.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, "Model for Disordered Single-Stranded RNA Chains"
- **Evidence pointer** "location not provided"
- **Issue** The RNA model uses one bead per nucleotide centered on the phosphorus atom, but the text does not specify how the RNA backbone flexibility is treated beyond the harmonic bond potential. Given the acknowledged limitation regarding RNA backbone flexibility, a brief description of the current treatment would be helpful.
- **Required correction** Add a sentence describing the treatment of RNA backbone angles and dihedrals, or explicitly state that these are not included.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability
- **Affected element** Conclusions, paragraph 1
- **Evidence pointer** "location not provided"
- **Issue** The conclusions section repeats the main findings but does not clearly distinguish between what is new in this work (the asymmetric potential) and what is inherited from the original Mpipi model. A clearer separation would help readers understand the specific contribution.
- **Required correction** Restructure the first paragraph of the conclusions to explicitly state which features are new and which are retained from the predecessor model.

## Risk / unsupported claims
- The claim of "near-quantitative agreement" with experimental phase diagrams for DDX4, R12, H1–ProTα, and RNA–protein systems is not supported by a quantitative statistical comparison; the text relies on visual inspection of figures.
- The claim that the asymmetric potential "captures" charge blockiness effects is supported by the DDX4 and R12 results, but the mechanism is not explained, and the generality of this finding is not established.
- The statement that the original Mpipi model "struggles to differentiate" between DDX4 WT and CS variants is not quantified; the difference in Tc between the two models is not reported.
- The parameterization protocol for the Yukawa potential is not fully specified, making the central methodological claim not reproducible from the main text alone.
- The relationship between simulated critical temperature (Tc) and experimental saturation concentration (Csat) is asserted but not quantitatively justified; the text states they are "both good proxies" without providing a theoretical or empirical basis.
- The treatment of the H1 globular domain as a rigid body is not validated, and the sensitivity of the results to this approximation is not discussed.
- The RNA model's treatment of backbone flexibility is not described, and the impact of this simplification on the reported results is not assessed.