## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods description, results, conclusions) without figures, tables, or supplementary material
- **Assessment boundary** Technical soundness and scientific claims as presented in the text; code functionality and benchmark completeness cannot be independently verified
- **Shared manuscript claim summary** The authors present CondenSimAdapter, a Python package that integrates SE(3)-transformer-based backmapping with a staged optimization protocol to convert coarse-grained condensate configurations into relaxed, explicitly solvated all-atom systems, compatible with multiple force fields and simulation engines, and validated across diverse protein systems including a 2 μs FUS LC simulation
- **Visible evidence base** Text descriptions of workflow stages, validation metrics (clash rates, ring penetration, chirality, Fmax), and comparison to literature values for FUS LC properties; references to figures and tables not visible in the supplied material
- **Missing materials affecting confidence** All figures, tables, and supplementary sections referenced throughout the text; code repository contents; detailed simulation parameters; benchmark system compositions

## Reviewer
- **Overall assessment** The manuscript addresses a genuine and practically important bottleneck in multiscale simulation of biomolecular condensates. The proposed workflow is sensible and the validation strategy is appropriately multifaceted. However, the provided text alone does not permit verification of the central claims, and several methodological details and benchmark results are only accessible through unreviewed supplementary material. The FUS LC validation is promising but rests on comparisons to a single prior simulation study, and the reported agreement may not be sufficiently discriminating. The manuscript is potentially suitable for publication after the missing evidence is examined and several technical points are clarified.

- **Who would be interested in the results, and why** Researchers in computational biophysics and molecular simulation, particularly those studying phase-separating proteins and biomolecular condensates. The tool lowers the barrier for constructing multiscale simulation pipelines and may be of interest to developers of simulation workflows and force-field parametrization efforts. The broad force-field compatibility and engine support could also attract users in the broader molecular dynamics community.

- **Major strengths** The problem addressed is well-defined and practically relevant. The workflow design is modular and configurable, which is appropriate for a community tool. The validation spans multiple dimensions (conflict resolution, domain integrity, ensemble fidelity) and multiple force-field combinations. The FUS LC 2 μs simulation is a substantial computational effort and provides a meaningful test of the generated ensembles.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "CondenSimAdapter unifies four CG and nine AA force fields under a single interface" and "integrating SE(3)-transformer–based cg2all backmapping with a physics-inspired optimization protocol"
- **Evidence pointer** Table 1 (not visible), Figure 1 (not visible), SI Sections S2–S6
- **Concern** The central technical claims regarding force-field coverage and the integration of the cg2all model cannot be assessed from the provided text. The manuscript states that cg2all is embedded but does not describe how the model is invoked, whether it is retrained or used as-is, how its output is standardized, or how the SE(3)-transformer architecture is adapted for the dense multichain condensate context. Similarly, the claim of unifying four CG and nine AA force fields requires a detailed table of supported combinations, parameter sources, and any modifications made to original force-field implementations. Without this information, the core functionality of the tool is not verifiable.
- **Why it matters** The primary contribution of the manuscript is the tool itself. If the force-field coverage or the backmapping integration is incomplete or incorrect, the entire workflow is compromised. The reader must be able to understand exactly what is implemented and how.
- **Resolution test** Provide a complete table of all supported CG and AA force-field combinations with parameter sources and any modifications. Describe the cg2all integration in detail, including model version, input/output formats, and any preprocessing or postprocessing steps. If possible, include a minimal working example in the main text or clearly reference a documented tutorial in the repository.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "we validated the workflow by (1) demonstrating the robust elimination of major structure conflicts across diverse CG–AA combinations"
- **Evidence pointer** Figure 2 (not visible), Table S3, Figure S4, Figure S6
- **Concern** The validation of conflict resolution is described only through aggregate metrics (clash rates, ring penetration rates, chirality errors). The text states that "all clash rates... and nearly all ring-penetration rates... were reduced to zero" but does not report the distribution of these metrics across the five replicates, the system-to-system variability, or the criteria used to define a "major" conflict. The single exception (TDP43 with 0.01% residual ring penetration) is mentioned but not discussed. Furthermore, the comparison to "direct standard minimization" is mentioned but no quantitative data are provided in the text. The reader cannot judge whether the improvement is consistent and meaningful.
- **Why it matters** The central claim of the manuscript is that the staged optimization protocol succeeds where standard minimization fails. This claim requires a quantitative, system-by-system comparison showing the failure of standard minimization and the success of the proposed protocol, including variability across replicates.
- **Resolution test** Provide a table or figure showing, for each system and each replicate, the initial and final values of all three conflict metrics, and the corresponding values after standard minimization alone. Include the Fmax values for both protocols. Discuss the TDP43 residual explicitly.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** "confirming ensemble fidelity via a 2 μs atomistic simulation of a FUS LC condensate that accurately reproduced established macroscopic and microscopic properties"
- **Evidence pointer** Figure 3 (not visible), SI Section S10
- **Concern** The FUS LC validation is the strongest evidence for the physical relevance of the generated ensembles, but the text provides only a list of properties (density, Rg, relaxation time, diffusion coefficient, secondary structure, contact enrichment) with a statement of agreement with "previously reported atomistic simulations." The specific values are given for density and Rg, but the comparison is made to a single prior simulation study. It is unclear whether these properties are sufficiently sensitive to distinguish a correctly equilibrated condensate from one that is merely stable. The contact enrichment analysis is described qualitatively ("enriched in Tyr- and Gln-mediated interactions") without quantitative comparison to reference data.
- **Why it matters** The claim of ensemble fidelity is the scientific justification for the entire workflow. If the generated ensembles are not demonstrably equivalent to those obtained by direct atomistic simulation, the tool's value is substantially reduced. The comparison must be quantitative and should include multiple independent reference datasets if available.
- **Resolution test** Provide a quantitative comparison of all reported properties to reference values, including uncertainties. For contact enrichment, report the enrichment factors for key residue pairs and compare to reference simulations. Discuss whether the chosen properties are sufficient to establish ensemble equivalence, and if not, what additional validation would be needed.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "CondenSimAdapter also generates native-contact Q restraints to protect folded domains during early equilibration, implemented through PLUMED"
- **Evidence pointer** SI Sections S6 and S8, Figure 2 (not visible)
- **Concern** The use of Q restraints to protect folded domains is a reasonable approach, but the text does not specify how the native contacts are defined, how the restraint strength is chosen, or how the restraints are removed during production. The validation for the H1-ProTalpha system shows low RMSD across nine force fields, but the control experiment (without restraints) is only described qualitatively. The choice of H1-ProTalpha as the sole multidomain test system is also limited, as it contains only one folded domain.
- **Why it matters** The Q-restraint protocol is a key innovation of the tool, and its parameters will significantly affect the quality of the generated ensembles. The reader needs to understand the protocol in sufficient detail to reproduce it and to assess its generalizability to other multidomain systems.
- **Resolution test** Provide a detailed description of the Q-restraint protocol, including contact definition, restraint functional form, force constant selection, and the schedule for turning off restraints. Report the control experiment quantitatively. Consider testing on at least one additional multidomain system with different domain architecture.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph 1
- **Issue** The introduction uses the phrase "−" as a placeholder or formatting artifact in several places, which disrupts the flow of the text.
- **Required correction** Remove the placeholder characters and ensure the text reads smoothly.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Workflow description
- **Evidence pointer** Section "CondenSimAdapter Workflow and Tested Systems"
- **Issue** The text states that the workflow is "configuration-driven" and executed via a CLI, but no example configuration file or command is shown in the main text. The reader is referred to Figure S1, which is not visible.
- **Required correction** Include a minimal example of the YAML configuration and the corresponding command in the main text or as a clearly referenced code listing.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Entanglement detection
- **Evidence pointer** Conclusions and Outlook, Figure S7
- **Issue** The entanglement detection step is mentioned as a feature, and a comparison to Z1+ is referenced, but no details are given about the detection algorithm or its performance.
- **Required correction** Provide a brief description of the entanglement detection method and report the comparison to Z1+ quantitatively in the main text or supplementary material.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Software availability
- **Evidence pointer** Abstract
- **Issue** The software is stated to be freely available at a GitHub URL, but no version number, license, or dependency list is provided.
- **Required correction** Specify the software version, license, and key dependencies in the main text or in a clearly referenced section of the repository.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability
- **Affected element** Results section
- **Evidence pointer** Section "CondenSimAdapter-Generated Coordinates Allow for Reproduction of Physical Observables of Condensates"
- **Issue** The text states that the simulation "maintained a stable condensed-phase protein density of 528 mg/mL and a water density of 615 mg/mL" but does not report the uncertainty or the time evolution of these quantities.
- **Required correction** Report the mean and standard deviation of these properties over the simulation trajectory, and show the time series if possible.

## Risk / unsupported claims
- The claim that CondenSimAdapter "succeeds where standard energy minimization fails" is not quantitatively supported in the provided text, as no comparative data are shown.
- The claim of "robust elimination of major structural conflicts across diverse CG–AA combinations" is based on aggregate metrics without system-by-system reporting.
- The claim of "ensemble fidelity" for the FUS LC simulation rests on comparison to a single prior simulation study, and the sensitivity of the chosen properties to distinguish correct from incorrect ensembles is not established.
- The claim of "broad force-field compatibility" (four CG and nine AA force fields) is not verifiable without the detailed table of supported combinations.
- The performance of the entanglement detection step relative to Z1+ is referenced but not reported.
- The generalizability of the Q-restraint protocol beyond the single tested multidomain system is not established.