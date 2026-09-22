## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) as provided
- **Assessment boundary** Technical and scientific evaluation of the described hybrid resolution molecular dynamics method and its application to α-synuclein–membrane interactions, based solely on the supplied material
- **Shared manuscript claim summary** The authors present a hybrid resolution molecular dynamics approach combining the PACE protein force field with the MARTINI coarse-grained solvent and lipid force fields, and demonstrate its application to study the interaction of α-synuclein monomer with a mixed POPC:POPS lipid bilayer over microsecond timescales. They report rapid N-terminal insertion into the interfacial region, subsequent NAC region insertion, conformational changes from stretched to S-shaped states, and secondary structure alterations including helix disruption and reformation.
- **Visible evidence base** Abstract, introduction, methods description (system preparation, energy minimization, equilibration, production), results narrative for α-synuclein–bilayer simulations, conclusions, references cited within text, figure references (Fig. 1, Fig. 3, Fig. 4, Supplementary Figs. S1–S3)
- **Missing materials affecting confidence** Actual figures and supplementary data (Fig. 1, Fig. 3, Fig. 4, Supplementary Figs. S1–S3, Supplementary run parameters) are referenced but not provided. No simulation parameter files, force field parameter details, convergence data, or quantitative error analysis are included. No comparison with experimental data or alternative simulation methods is presented in the supplied text.

## Reviewer
- **Overall assessment** The manuscript describes a practical protocol for hybrid resolution MD simulations of amyloid protein–membrane systems, with a specific application to α-synuclein interacting with a mixed lipid bilayer. The methodological description is detailed and potentially useful for practitioners. However, the scientific claims regarding the interaction dynamics and structural transitions are presented without quantitative evidence, statistical validation, or comparison to experimental benchmarks. The manuscript reads more as a methods protocol than a research article establishing new biophysical insights. The core claims about the method's accuracy and the biological relevance of the observed behaviors are not substantiated from the provided material.
- **Who would be interested in the results, and why** Computational biophysicists and molecular modelers studying protein–membrane interactions, particularly those working on amyloid proteins and intrinsically disordered proteins. Researchers developing or applying multiscale simulation approaches would find the protocol description useful. The broader community studying neurodegenerative disease mechanisms may be interested in the potential applications, though the current evidence does not yet provide new biological insights.
- **Major strengths** The manuscript addresses a technically challenging problem, namely simulating large protein–membrane systems over microsecond timescales with reasonable accuracy. The step-by-step protocol, including system preparation via CHARMM-GUI and specific GROMACS commands, is practical and reproducible. The choice of α-synuclein as a test case is relevant given its established membrane interactions. The discussion of limitations and future challenges in the conclusions is thoughtful.
- **Major Concerns** The central scientific claims about α-synuclein–membrane interaction dynamics are not supported by quantitative data in the provided text. The manuscript lacks validation of the hybrid method against experimental results or all-atom simulations. The description of structural transitions relies on qualitative narrative without statistical measures or error estimates. The claim that the method enables "routine and accurate" simulation is not demonstrated. The relevance of the observed behaviors to disease mechanisms is speculative.
- **Minor Comments** The manuscript would benefit from clearer definitions of the hybrid resolution scheme's parameters. The choice of specific lipid composition and its physiological relevance could be better justified. The discussion of pH effects and protonation states is brief and could be expanded. The conclusions section raises interesting questions but does not connect them to the presented results.
- **Technical failings that need to be addressed before the case is established** Lack of quantitative results (e.g., contact maps, distance time series, secondary structure fractions with error bars). No validation against experimental data or all-atom simulations. No demonstration of convergence or reproducibility across multiple independent simulations. No analysis of force field limitations or artifacts specific to the hybrid approach.
- **Assessment against Nature-style criteria** Originality: The hybrid PACE-MARTINI approach is not new, and the specific application to α-synuclein–membrane systems, while relevant, does not present a novel methodological advance. Scientific importance: The potential to study amyloid–membrane interactions at scale is important, but the current evidence does not establish new biological or methodological insights. Interdisciplinary readership: The topic bridges biophysics, computational chemistry, and neurobiology, but the presentation is too specialized for a broad audience. Technical soundness: The protocol is plausible, but the lack of validation and quantitative analysis undermines confidence. Readability for nonspecialists: The manuscript assumes significant familiarity with MD simulations and force fields, limiting accessibility.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript has potential as a methods protocol, but the scientific claims require substantial additional evidence, including quantitative results, validation, and statistical analysis.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that the hybrid resolution method enables "routine and accurate simulation" of multi-protein and complex membrane systems on microsecond timescales, and that the application to α-synuclein reveals specific interaction dynamics including N-terminal insertion, NAC region insertion, and conformational changes.
- **Evidence pointer** Results section "Interaction of α-synuclein monomer with lipid bilayer", Figures 3 and 4 (not provided)
- **Concern** The central results are described qualitatively without any quantitative data. No numerical values for contact frequencies, insertion depths, secondary structure fractions, or time constants are provided. The figures are referenced but not included in the supplied material, making it impossible to assess the validity of the claims. The absence of error bars, standard deviations, or replicate analyses means the robustness of the observations cannot be evaluated.
- **Why it matters** The scientific value of the manuscript rests on the demonstrated behavior of α-synuclein at the membrane. Without quantitative evidence, the claims are unverifiable and the method's utility is not established. Readers cannot assess whether the observed dynamics are reproducible or statistically significant.
- **Resolution test** Provide quantitative analysis of simulation trajectories, including time-resolved contact maps, residue-specific insertion profiles, secondary structure evolution with confidence intervals, and comparisons across multiple independent simulations. Include the actual figures with clear legends and statistical annotations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation
- **Claim pointer** The manuscript implies that the hybrid PACE-MARTINI approach provides accurate results for protein–membrane interactions, suitable for studying amyloid aggregation processes.
- **Evidence pointer** Methods section "Computational method to study the dynamics of complex amyloid systems", no validation data provided
- **Concern** No validation of the hybrid method is presented. There is no comparison with experimental data on α-synuclein–membrane interactions, no benchmarking against all-atom simulations, and no assessment of known limitations of the PACE or MARTINI force fields in this context. The claim of accuracy is therefore unsupported.
- **Why it matters** Hybrid resolution methods involve approximations that can introduce artifacts, particularly in protein–membrane interactions where electrostatic and hydrophobic balance is critical. Without validation, the biological relevance of the results is uncertain, and the method's reliability for other systems cannot be inferred.
- **Resolution test** Include a validation section comparing hybrid simulation results with experimental data (e.g., NMR or fluorescence measurements of α-synuclein membrane binding) or with all-atom simulations for a benchmark system. Discuss known limitations and potential artifacts of the hybrid approach.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The manuscript provides a step-by-step protocol for setting up and running hybrid resolution simulations, implying that the described procedure is sufficient for others to reproduce the results.
- **Evidence pointer** Methods section "System preparation" and "Hybrid resolution simulations", Supplementary run parameters (not provided)
- **Concern** The protocol description lacks critical details necessary for reproduction. The specific modifications to GROMACS for PACE compatibility are referenced but not described. The force field parameter files and scripts are only available via external links, which may not be stable. The equilibration and production parameters are only partially specified, and the supplementary run parameter files are not included in the supplied material.
- **Why it matters** Reproducibility is a core requirement for scientific methods. Without complete parameter specifications and access to necessary files, other researchers cannot implement the method, limiting its utility and the verifiability of the results.
- **Resolution test** Provide complete simulation parameter files, force field parameters, and scripts either in the supplementary material or via a stable repository. Describe all necessary modifications to GROMACS in detail. Include system-specific details such as box size, number of water molecules, and ion concentration.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Biological relevance
- **Claim pointer** The manuscript suggests that the observed α-synuclein–membrane interactions are relevant to understanding amyloid aggregation and disease progression, citing lipid-dependent aggregation propensity and the role of membrane surfaces in oligomer assembly.
- **Evidence pointer** Results section "Interaction of α-synuclein monomer with lipid bilayer", Conclusions section
- **Concern** The connection between the simulation results and disease mechanisms is speculative. The manuscript does not demonstrate that the observed conformational changes or insertion behaviors are linked to aggregation propensity or toxicity. No experimental correlation is provided, and the discussion of disease relevance is general.
- **Why it matters** The broader significance of the work depends on its relevance to amyloid pathology. Without a clear link between the simulated behaviors and aggregation outcomes, the impact on the disease-focused community is limited.
- **Resolution test** Discuss how the observed dynamics might influence aggregation, ideally with supporting simulations of oligomer formation or comparisons with experimental aggregation studies under similar membrane conditions. Alternatively, clearly frame the manuscript as a methods paper without overstating biological implications.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section "Preparation of initial parameters"
- **Evidence pointer** Location not provided
- **Issue** The description of the CHARMM-GUI procedure is somewhat terse, and the rationale for specific choices (e.g., rotation angles, water thickness) is not explained.
- **Required correction** Provide brief justifications for the chosen parameters and clarify how they affect the simulation outcomes.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section "Interaction of α-synuclein monomer with lipid bilayer"
- **Evidence pointer** Figure 4 (not provided)
- **Issue** The description of secondary structure changes is qualitative, and the specific residues involved in helix disruption or formation are not clearly identified.
- **Required correction** Specify the residue ranges for each secondary structure element and describe the time course of changes more precisely.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Referencing
- **Affected element** Introduction and Conclusions
- **Evidence pointer** References 25, 48–54, 55–59
- **Issue** Several references are cited to support claims about experimental observations and disease relevance, but the specific findings from these references are not summarized.
- **Required correction** Briefly describe the relevant findings from key references to strengthen the context and support the claims.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract and Introduction
- **Evidence pointer** Location not provided
- **Issue** The term "hybrid resolution" is used but not explicitly defined in contrast to other multiscale approaches.
- **Required correction** Define the term and clarify how it differs from other hybrid or multiscale methods.

## Risk / unsupported claims
- The claim that the method enables "routine and accurate simulation" is unsupported due to lack of validation and quantitative results.
- The specific interaction dynamics of α-synuclein (N-terminal insertion, S-shaped conformation, secondary structure changes) are unverifiable without the actual figures and quantitative data.
- The relevance of the observed behaviors to amyloid aggregation and disease progression is speculative and not supported by direct evidence.
- The statement that the hybrid method "can be employed to investigate the interaction of amyloid proteins with lipid membranes" is plausible but not demonstrated beyond the single α-synuclein case.
- The assertion that the method "enables routine and accurate simulation of multi-protein and complex membrane systems" is not substantiated, as no multi-protein systems or complex membrane compositions are simulated in the provided material.