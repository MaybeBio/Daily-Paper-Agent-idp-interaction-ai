## Review setup
- **Input scope** Full manuscript text including abstract, main text, methods, results, discussion, conclusions, and references to supporting material.
- **Assessment boundary** Scientific content, methodological soundness, validity of claims relative to presented evidence, and alignment with Nature-style criteria. Editorial quality and formatting are considered only insofar as they affect scientific clarity.
- **Shared manuscript claim summary** The authors present a multiscale simulation framework (AA-CG-AA) integrating all-atom structure modeling, coarse-grained Martini 3 simulations, and backmapping to atomistic resolution. They apply this framework to two disease-associated proteins, TDP-43 CTD (274–414) and white-tailed deer prion protein (24–233), and report condition-dependent differences in condensate morphology, chain mobility, and ion-mediated interactions. They propose that solvent-mediated interactions involving Na+ and Cl− ions are primary drivers of early-stage condensation, with direct chain-chain contacts playing a secondary role.
- **Visible evidence base** Full manuscript text including methods, results, discussion, conclusions, figure captions (Figures 1–11), tables (Tables 1–2), and references to supporting figures (S1–S7), tables (S1–S2), and videos (S1–S2). No actual figure images, supporting documents, or video files were provided for direct inspection.
- **Missing materials affecting confidence** Figure images and supporting information (Figures S1–S7, Tables S1–S2, Videos S1–S2) were not available for direct examination. Simulation parameter files, force field modification details, and raw trajectory data were not provided. The GitHub repository link is given but its contents were not assessed.

## Reviewer

- **Overall assessment** This manuscript describes a technically ambitious multiscale simulation workflow and applies it to two biologically relevant proteins. The central methodological contribution, the AA-CG-AA pipeline, is potentially useful to the simulation community. However, the scientific claims regarding condensation mechanisms, particularly the proposed role of ion-mediated interactions, are not fully supported by the evidence presented. The study is largely descriptive, and the absence of quantitative validation against experimental data or established theoretical models weakens the conclusions. The manuscript would benefit from a more rigorous analysis of statistical significance, a clearer articulation of what is novel relative to existing multiscale approaches, and a more direct connection to experimentally testable predictions.
- **Who would be interested in the results, and why** Computational biophysicists and molecular simulators working on protein aggregation, phase separation, and intrinsically disordered proteins would find the multiscale framework of interest. Researchers studying TDP-43 and prion protein biology, particularly those focused on the early stages of misfolding and condensation, may also find the qualitative observations relevant. The work could serve as a methodological reference for those seeking to combine Martini 3 coarse-grained simulations with atomistic backmapping for large multi-chain systems.
- **Major strengths**
  1. The AA-CG-AA framework is a coherent and practical integration of established tools, addressing a real need for simulating large multi-chain protein systems with atomistic resolution.
  2. The choice of two structurally distinct proteins (mostly disordered TDP-43 CTD vs. mixed folded/disordered PrP) provides a useful comparative test case.
  3. The analysis of ion-chain versus chain-chain contacts as distinct contributors to mobility reduction is an interesting angle that goes beyond simple structural characterization.
  4. The authors are transparent about limitations, including force field sensitivity and the challenge of preserving secondary structure in coarse-grained simulations.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Validity of central claim
- **Claim pointer** The manuscript claims that "solvent-mediated interactions involving Na+ and Cl− ions are important drivers of early-stage confinement" and that ion-chain contacts show a "clear inverse relationship with average chain diffusivity."
- **Evidence pointer** Results section, Figure 12, Table 3
- **Concern** The central mechanistic claim rests on a correlation between ion-chain contact counts and diffusivity. However, the analysis is purely correlative. No causal evidence is provided, such as control simulations without ions, systematic variation of ion concentration, or perturbation of specific ion-binding sites. The observed correlation could be a consequence of other factors, such as overall chain compaction or differences in protein-protein interactions, rather than a direct effect of ion binding. Furthermore, the statistical treatment is limited to standard deviations across replicas; no formal significance testing or error propagation is reported.
- **Why it matters** The claim that ions are "important drivers" of condensation is a strong mechanistic statement. If the evidence is only correlative, the conclusion overreaches. This is the central scientific message of the paper, and it must be supported by more direct evidence or substantially softened.
- **Resolution test** The authors should either (a) provide direct evidence of causality, for example by showing that removal of ions or alteration of ion-protein interaction parameters abolishes the mobility reduction and network formation, or (b) reframe the claim as a correlation requiring further investigation. Additionally, a statistical test (e.g., t-test or ANOVA across conditions and replicas) should be applied to the diffusivity and contact count comparisons.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of force field modifications
- **Claim pointer** The authors state that they "adjusted the Martini 3.0.b.3.2 nonbonded Lennard-Jones FF parameters following recent best practices" and describe two modified force fields, FF1 and FF2, with specific scaling factors.
- **Evidence pointer** Materials and methods, "Coarse-grained simulations in solution"
- **Concern** The description of the force field modifications is insufficient for reproduction. The authors mention scaling factors (e.g., protein-water interactions scaled by 1.03, protein-protein by 0.92, ion interactions by 1.029) but do not specify which interaction types were scaled, how the scaling was applied (e.g., global vs. bead-type specific), or whether the scaling was validated against experimental data. The choice of these specific values appears arbitrary without a systematic calibration or sensitivity analysis. Furthermore, the use of a beta version (Martini 3.0.b.3.2) rather than a stable release raises questions about reproducibility.
- **Why it matters** The entire study depends on the behavior of these modified force fields. If the modifications are not fully described and justified, the results cannot be reproduced or properly evaluated by the community. This is a fundamental requirement for a methods-focused paper.
- **Resolution test** The authors should provide a complete description of the force field modifications, including a table of all changed parameters, the rationale for each change, and a validation against experimental observables (e.g., radius of gyration, diffusion coefficients) for at least one test system. A sensitivity analysis showing how results vary with the scaling factors would also strengthen the case.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Adequacy of sampling and system size
- **Claim pointer** The authors claim to capture "key mesoscale features of early supramolecular condensation" and identify "condensate-like subpopulations" and "percolation-like networks."
- **Evidence pointer** Results and discussion, Figures 5–10, Table 2
- **Concern** The simulations are limited to 50 chains per system, with simulation times of 1000 ns (extended to 10,000 ns for one condition). For phase separation and condensation phenomena, these system sizes and timescales are likely insufficient to reach equilibrium or to draw robust conclusions about mesoscale behavior. The identification of "condensate-like subpopulations" based on low MSD is subjective; no order parameter, cluster analysis, or comparison to a homogeneous control is provided. The finite-size effects on the observed network formation are not discussed.
- **Why it matters** The conclusions about condensation behavior and network formation are central to the paper's significance. If the sampling is inadequate, the observed structures may be kinetic artifacts rather than equilibrium or near-equilibrium features. The claim of capturing "mesoscale" features is particularly problematic given the small system size.
- **Resolution test** The authors should either (a) provide evidence that the observed features are converged with respect to system size and simulation time, for example by showing similar behavior in systems of different sizes or by demonstrating that the MSD plateaus are stable over extended simulations, or (b) temper the claims to reflect the preliminary and system-size-dependent nature of the observations. A quantitative cluster analysis or a comparison to a non-interacting control system would also help.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Validation of backmapping and secondary structure analysis
- **Claim pointer** The authors report significant secondary structure changes after coarse-grained simulation and backmapping, including loss of β-sheet in PrP, and state that "improving β-structure stability without compromising condensation dynamics remains an important challenge."
- **Evidence pointer** Results and discussion, "Structural features of multiunit TDP-43 and PrP systems"; Table S2
- **Concern** The backmapping procedure is described as using the backward-v5 script, but the fidelity of the backmapping is not assessed. The authors do not compare the backmapped structures to the original atomistic structures or to experimentally determined structures. The loss of β-sheet content is attributed to the coarse-grained simulation, but it is unclear whether this is a genuine physical result or an artifact of the backmapping procedure or the elastic network parameters. The authors acknowledge this as a limitation but do not provide a quantitative assessment of the uncertainty this introduces into their subsequent analyses.
- **Why it matters** The secondary structure analysis is used to interpret the physical state of the proteins in the condensates. If the backmapping introduces artifacts, the conclusions about structural changes during condensation may be unreliable. This is particularly important for PrP, where the loss of β-sheet is highlighted as a significant finding.
- **Resolution test** The authors should validate the backmapping procedure by comparing backmapped structures to the original atomistic structures (e.g., RMSD, secondary structure assignment) and, if possible, to experimental structures or NMR-derived ensembles. A discussion of the sensitivity of the secondary structure results to the elastic network parameters would also be valuable.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability and biological relevance
- **Claim pointer** The authors suggest the framework is "broadly applicable to diverse systems" and that the findings offer "insight into early confinement mechanisms during protein assembly."
- **Evidence pointer** Conclusions section
- **Concern** The study uses only two proteins, both of which are disease-related and chosen for their distinct structural features. The authors do not discuss how the observed behavior might generalize to other proteins with different sequences, lengths, or degrees of disorder. The biological relevance of the findings is asserted but not developed; no connection is made to specific experimental observations of TDP-43 or PrP condensation, nor are testable predictions offered.
- **Why it matters** The significance of the work depends on its generalizability and biological utility. Without a broader context or specific predictions, the study remains a methodological demonstration with limited immediate impact.
- **Resolution test** The authors should either (a) apply the framework to at least one additional protein system to demonstrate generalizability, or (b) provide a more detailed discussion of how the observed mechanisms might operate in vivo, with specific, testable predictions that could be addressed experimentally.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 1 and Table 1
- **Evidence pointer** Introduction, Figure 1, Table 1
- **Issue** Figure 1 is described as showing "computational capability versus molecular resolution and interaction complexity" but the axes and data points are not clearly defined in the caption. Table 1 lists several force fields but the comparison criteria are not systematic, and the "Advantages" column is subjective.
- **Required correction** Clarify the axes and content of Figure 1. For Table 1, consider using a more structured comparison with defined criteria (e.g., resolution, speed, accuracy, availability) rather than subjective descriptions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Table 2 and Figure 12
- **Evidence pointer** Results and discussion, Table 2, Figure 12
- **Issue** Diffusivity values are reported with standard errors, but no statistical comparison between conditions is provided. The text describes differences as "clear" or "pronounced" without formal testing.
- **Required correction** Add statistical tests (e.g., t-tests or ANOVA) for the diffusivity comparisons and report effect sizes or confidence intervals.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility of methods
- **Affected element** Simulation protocols
- **Evidence pointer** Materials and methods, "Coarse-grained simulations in solution"
- **Issue** The description of the simulation protocol lacks some details, such as the specific Martini 3 version used (beyond "3.0.b.3.2"), the equilibration scheme, and the criteria for determining when simulations reached a stable regime.
- **Required correction** Provide a more complete description of the simulation protocol, including all relevant parameters, or reference a previously published protocol that was followed.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation of contact analysis
- **Affected element** Table 3 and Figure 12
- **Evidence pointer** Results and discussion, "Ion-chain and chain-chain contact numbers"
- **Issue** The contact analysis uses a single distance threshold (3.6 Å) and VDW overlap criterion. The sensitivity of the results to these thresholds is not discussed.
- **Required correction** Briefly discuss the choice of contact criteria and, if feasible, show that the qualitative conclusions are robust to reasonable variations in the thresholds.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Connection to experimental literature
- **Affected element** Discussion and conclusions
- **Evidence pointer** Conclusions section
- **Issue** The manuscript does not compare its findings to experimental studies of TDP-43 or PrP phase separation or condensation. This limits the reader's ability to assess the biological plausibility of the simulation results.
- **Required correction** Add a brief discussion of relevant experimental observations and how the simulation results align or conflict with them.

## Risk / unsupported claims
- The claim that "solvent-mediated interactions involving Na+ and Cl− ions are important drivers of early-stage confinement" is unsupported as a causal statement; the evidence is correlative only.
- The claim that the framework "captured key mesoscale features of early supramolecular condensation" is not fully supported given the limited system size (50 chains) and simulation timescales (1000 ns, with one 10,000 ns extension).
- The identification of "condensate-like subpopulations" and "percolation-like networks" is based on qualitative visual inspection and MSD analysis without quantitative cluster analysis or order parameters.
- The biological relevance of the findings is asserted but not substantiated by comparison to experimental data or by offering specific testable predictions.
- The generalizability of the framework to other protein systems is claimed but not demonstrated beyond the two test cases.
- The secondary structure changes observed after backmapping, particularly the loss of β-sheet in PrP, are presented as findings but the uncertainty introduced by the backmapping procedure is not quantified.