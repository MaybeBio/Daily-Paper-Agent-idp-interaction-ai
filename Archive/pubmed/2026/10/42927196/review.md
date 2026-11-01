## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and supplemental figure/table legends
- **Assessment boundary** Scientific content, methodological soundness, claims-to-evidence alignment, and clarity of the presented work. No assessment of editorial fit or journal-specific scope beyond general Nature-style criteria.
- **Shared manuscript claim summary** The authors introduce flux-driven molecular dynamics (FD-MD), a coarse-grained nonequilibrium simulation framework, to study how rigid β-prone motifs, hydrophobic sequence patterning, and molecular deposition rate control fibril growth at biomolecular condensate interfaces. They report that rigid motifs sustain orientational order that converts interfacial adsorption into directional fibrillar growth, while flexible chains form spreading surface aggregates. They further report that deposition rate and initial drift velocity redirect assembly between lateral spreading, outward fibrillar growth, and bridging between opposing interfaces, with stronger initial drift accelerating surface coverage but slowing axial elongation.
- **Visible evidence base** Main text figures 1–5, supplemental figures S1–S6, supplemental tables S1–S3, methods section describing model construction, simulation protocols, and analysis procedures
- **Missing materials affecting confidence** No simulation trajectory files, no parameter files beyond those summarized in tables, no convergence checks, no reproducibility statistics beyond three trajectories for the filament analysis, no code execution logs, no raw data files. The provenance of two figure panels is acknowledged by the authors as not fully recoverable.

## Reviewer

- **Overall assessment** This manuscript presents a conceptually interesting minimal model for how molecular flux and chain rigidity might jointly control fibril growth at condensate interfaces. The central idea, that interfacial orientational order combined with deposition kinetics selects between spreading and protrusive growth, is plausible and potentially useful. However, the evidence base is thin in several critical places. The morphology map in Figure 3 is based on single trajectories per condition, the filament growth analysis in Figure 5 uses only three trajectories per condition with acknowledged overlap between conditions, and two figure panels are explicitly acknowledged as having unrecoverable provenance. The authors are appropriately cautious in several places, but the core claims about flux-controlled morphological selection rest on a small number of simulations without error bars, convergence checks, or finite-size analysis. The manuscript would be strengthened substantially by additional trajectories, quantitative order parameters for morphology classification, and a clearer demonstration that the reported effects are robust to simulation length and system size.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensate aging, amyloid formation at interfaces, and nonequilibrium self-assembly would find this work relevant. The distinction between spreading and protrusive growth controlled by deposition kinetics is a useful conceptual framing that could inform experimental design in condensate systems where fibril formation is observed at interfaces. The coarse-grained model is simple enough to be adapted by other simulation groups, and the emphasis on molecular flux as a control parameter connects to experimental work on protein concentration and delivery rates in cellular contexts.

- **Major strengths** The manuscript addresses a genuinely under-explored question, namely how nonequilibrium delivery of material to a condensate interface selects between different aging morphologies. The model design cleanly separates rigidity, sequence patterning, and deposition rate as independent variables. The authors are appropriately careful in several places, explicitly distinguishing interfacial fibril initiation from nucleation, acknowledging the limitations of single trajectories, and noting where their model does not resolve molecular-level details. The kinematic identity for the surface-loading proxy is a useful analytical contribution. The writing is generally clear and the figures are well organized.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that four distinct growth regimes exist in the Kθ–m˙ phase space, including regular surface growth, irregular surface deposition, fibrillar interfacial growth, and bridging networks, and that these regimes are organized by chain stiffness and deposition rate.
- **Evidence pointer** Figure 3, Tables S1 and S2, "location not provided" for trajectory counts beyond the statement of one trajectory per point
- **Concern** The morphology map in Figure 3 is constructed from one trajectory per condition. The authors state this explicitly, but the claim of four distinct regimes requires demonstrating that the classification is reproducible. Without multiple independent trajectories per condition, it is impossible to know whether the apparent regime boundaries reflect genuine dynamical regimes or stochastic variation in individual runs. The shaded regions interpolating between classified points imply structure that single trajectories cannot support.
- **Why it matters** The central claim of the paper, that flux and rigidity select between distinct morphological outcomes, depends entirely on this phase space being meaningful. If the classification is not reproducible, the entire conceptual framework is undermined.
- **Resolution test** Provide at minimum 5–10 independent trajectories per condition across the phase space, report the fraction of trajectories falling into each morphological class, and show representative snapshots from multiple trajectories per regime. If computational cost is prohibitive, reduce the parameter grid and increase replication.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that stronger initial drift velocity slows axial fibril elongation while accelerating surface coverage, and that this reflects competition between interfacial accumulation, orientational ordering, and outward growth.
- **Evidence pointer** Figure 5, Table S3, "location not provided" for individual trajectory data
- **Concern** The filament growth analysis in Figure 5 uses three trajectories per condition, and the authors acknowledge that individual trajectories overlap between conditions and that the scatter at the lowest drift velocity is comparable to the difference between conditions. The claim of a systematic slowdown with increasing drift velocity is therefore not established by the presented data. The mean slopes decrease monotonically, but with only three trajectories and acknowledged overlap, this could easily be sampling noise.
- **Why it matters** This is the most mechanistically interesting claim in the paper, that faster arrival paradoxically slows elongation. If this is not robustly demonstrated, the paper loses its most distinctive finding.
- **Resolution test** Increase the number of trajectories per condition to at least 10, report confidence intervals or standard errors on the mean slopes, and perform a statistical test for the trend across drift velocities. If the effect is real, it should survive this additional sampling.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Data provenance
- **Claim pointer** The manuscript states that the configuration sequence in Figures 5C–5G is taken from an archived composite whose provenance is not fully recoverable, and that the morphology map in Figure 3 classifies each end state visually.
- **Evidence pointer** "Provenance of the archived figure panels" section, Figures 3 and 5C–5G
- **Concern** Two figure panels in the main text are acknowledged to have unrecoverable provenance. The configuration sequence in Figures 5C–5G is described as illustrative only, but it is presented in the main text as visual evidence for the growth process. The morphology map in Figure 3 relies on visual classification without a quantitative order parameter. For a simulation paper, where full reproducibility is expected, this is a significant gap.
- **Why it matters** Readers cannot verify the visual claims in these figures, and the morphology classification cannot be independently checked. This weakens the evidentiary basis for the central claims.
- **Resolution test** Regenerate the configuration sequence from the identified trajectories used for the quantitative analysis, and provide a quantitative morphology classifier, such as a shape anisotropy parameter or orientational order metric, to replace or supplement visual classification.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Model validation
- **Claim pointer** The manuscript claims that the FD-MD model captures generic physical principles of interfacial fibril growth, and that the results connect to experimental observations of condensate aging.
- **Evidence pointer** Discussion section, "location not provided" for any direct comparison to experimental data
- **Concern** The model is intentionally minimal, and the authors acknowledge this, but the connection to experimental systems is asserted rather than demonstrated. No attempt is made to map model parameters to specific proteins or experimental conditions, and no experimental observables are predicted that could be tested. The claim that the model provides a minimal physical framework for distinct condensate-aging pathways is plausible but currently unsupported by any quantitative link to experiment.
- **Why it matters** Without a connection to experimental observables, the model remains an abstract exercise. The paper would be more compelling if it identified specific predictions, such as how fibril orientation or growth rate should scale with protein concentration or delivery rate in a particular experimental system.
- **Resolution test** Add a section discussing how model parameters could be mapped to experimental systems, or identify at least one quantitative prediction that could be tested with existing experimental techniques.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical completeness
- **Claim pointer** The manuscript claims that the initial drift velocity controls the timescale on which the system crosses from initial spreading to sustained three-dimensional growth, and that the deposition rate and drift velocity act together to select the growth trajectory.
- **Evidence pointer** Figure 4, Figure S2, "location not provided" for the full parameter grid
- **Concern** The joint deposition-drift grid in Figure S2 is described but the full grid is not shown in the main text, and the number of conditions and trajectories per condition is not stated. The claim that the two parameters act together to select the growth trajectory requires a systematic exploration of the joint parameter space, which is not presented in sufficient detail.
- **Why it matters** The interaction between deposition rate and drift velocity is a central claim, but the evidence for it is presented in a supplementary figure without clear statistical support.
- **Resolution test** Present the full joint grid in the main text or a clearly labeled supplementary figure, state the number of trajectories per condition, and provide a quantitative summary of the resulting morphologies.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Summary section, "location not provided"
- **Issue** The abstract contains the phrase "Counterinutively" which appears to be a typo for "Counterintuitively". Additionally, the phrase "pathwasy" in the final sentence of the Summary appears to be a typo for "pathways".
- **Required correction** Correct the typos in the abstract.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Introduction and Results
- **Evidence pointer** Introduction, Results, "location not provided"
- **Issue** The term "interfacial fibril initiation" is introduced to distinguish the simulation observations from experimentally defined nucleation. This is a reasonable distinction, but the term is not used consistently throughout the manuscript. In some places the text refers to "nucleation" without qualification, which could confuse readers.
- **Required correction** Use the term "interfacial fibril initiation" consistently when referring to the simulation observations, and reserve "nucleation" for experimental contexts or clearly define when the term is used loosely.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** "Simulation protocol" section, "location not provided"
- **Issue** The methods state that the initial drift velocity is assigned to newly inserted chains, but the exact procedure for assigning this velocity is not fully specified. It is stated that the normal component is drawn from an interval directed toward the nearer surface face, but the distribution within that interval is not described.
- **Required correction** Specify the exact distribution used for the initial velocity components, including whether they are drawn uniformly or from another distribution.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 5, Table S3
- **Evidence pointer** Figure 5, Table S3, "location not provided"
- **Issue** The filament growth analysis reports mean slopes from three trajectories per condition, but no measure of variability is provided in the main text. The authors acknowledge scatter in the text, but the figure does not show individual trajectory data or error bars.
- **Required correction** Add error bars or individual trajectory data to Figure 5, or state in the figure legend that individual trajectories are shown in Table S3.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion
- **Evidence pointer** Discussion, "location not provided"
- **Issue** The discussion mentions that the model connects to interface-associated fibrillation in hnRNPA1 condensates, suppression in multicomponent condensates, and Tau systems, but these connections are stated without specific mechanistic comparisons. It would strengthen the discussion to identify which specific model predictions align with or differ from each experimental system.
- **Required correction** Expand the discussion to include specific comparisons between model predictions and experimental observations for at least one of the cited systems.

- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, and R1-M3 are blocking. The single-trajectory morphology map, the underpowered filament growth analysis, and the unrecoverable provenance of two figure panels collectively prevent the core claims from being established. R1-M4 and R1-M5 are non-blocking but should be addressed to strengthen the manuscript.

- **Assessment against Nature-style criteria** Originality: The conceptual framing of flux as a control parameter for interfacial fibril growth is original and potentially valuable. Scientific importance: The question of how condensate aging pathways are selected is important, but the current evidence does not yet establish the claimed effects. Interdisciplinary readership: The work bridges soft matter physics, biophysics, and cell biology, and the writing is accessible to nonspecialists. Technical soundness: The model is simple and the methods are mostly clear, but the statistical and reproducibility issues described above are significant. Readability for nonspecialists: The manuscript is generally well written, with clear figures and a logical structure, though the methods section assumes familiarity with coarse-grained simulation conventions.

- **Recommendation posture** Currently not established from the provided evidence. The conceptual framework is interesting and the model is well designed, but the central claims about flux-controlled morphological selection and the slowdown of elongation with faster drift are not supported by sufficient replication or provenance. The authors should be encouraged to resubmit after addressing the blocking concerns, particularly by providing multiple trajectories per condition, quantitative morphology classification, and regenerated figure panels with full provenance.

## Risk / unsupported claims
- The claim of four distinct growth regimes in the Kθ–m˙ phase space is unsupported because each condition is represented by a single trajectory.
- The claim that stronger initial drift velocity slows axial fibril elongation is unsupported because the three-trajectory analysis shows overlap between conditions and scatter comparable to the effect size.
- The visual classification of morphologies in Figure 3 is not independently verifiable without a quantitative classifier.
- The configuration sequence in Figures 5C–5G is acknowledged to have unrecoverable provenance and is therefore not verifiable evidence.
- The connection between model predictions and experimental systems is asserted but not demonstrated with specific quantitative comparisons.
- The claim that the model captures generic physical principles is plausible but not established without a broader exploration of parameter space or comparison to experimental data.