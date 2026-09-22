## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors introduce Martini3-NMR, an integrative framework that incorporates NMR observables (chemical shifts modeled by artificial neural networks at the CG level, and NOE restraints) into coarse-grained protein force fields, aiming to enhance structural accuracy of CG simulations while preserving sampling efficiency. They report improved conformational ensembles and demonstrate applicability to protein folding from misfolded states, oligomer disassembly in lipid bilayers, and disordered fuzzy regions at amyloid fibril surfaces, which they describe as displaying condensate-like properties.
- **Visible evidence base** Abstract text only; no quantitative results, methodological details, validation metrics, or system-specific outcomes are provided
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, simulation protocols, neural network architecture and training details, validation datasets, error analysis, and comparisons to experimental or alternative computational benchmarks

## Reviewer
- **Overall assessment** The abstract presents a potentially valuable integrative approach that addresses a recognized limitation in coarse-grained simulations, namely the trade-off between sampling efficiency and structural accuracy. The concept of embedding NMR-derived restraints into CG force fields via neural network chemical shift prediction is timely and could appeal to a broad computational and experimental biophysics audience. However, the abstract provides no quantitative evidence, no validation metrics, and no methodological specifics. The central claims of enhanced accuracy and broad applicability are therefore not assessable from the supplied material. The mention of "condensate-like structural and dynamical properties" for amyloid fuzzy coats is intriguing but unsupported by any data in the abstract. The work may be of interest if the full manuscript substantiates the claims, but the current evidence base is insufficient to evaluate technical soundness or scientific impact.
- **Who would be interested in the results, and why** Computational biophysicists and method developers working on coarse-grained simulations, integrative modeling, and force field refinement would be primary readers. Experimental NMR spectroscopists interested in linking observables to conformational ensembles may also find the framework relevant. Researchers studying intrinsically disordered proteins, membrane-associated assemblies, and amyloid systems could benefit if the method proves broadly applicable, as these systems are notoriously difficult to characterize by both experiment and simulation.
- **Major strengths** The proposed approach addresses a well-recognized limitation in CG simulations, namely reduced structural accuracy due to simplified interaction potentials. The integration of NMR chemical shifts and NOE restraints into CG force fields is conceptually novel and could provide a general strategy for experimentally driven refinement. The claimed applicability to diverse and challenging systems, including disordered proteins and membrane processes, suggests potential broad utility if substantiated.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality is potentially high, as the combination of neural network chemical shift prediction with CG simulations and NMR restraints appears novel. Scientific importance could be significant if the method demonstrably improves CG ensemble accuracy without compromising efficiency, but this is not established from the abstract. Interdisciplinary readership is plausible given the intersection of computational methods, NMR spectroscopy, and biophysics. Technical soundness cannot be evaluated without methodological details and validation data. Readability for nonspecialists is adequate in the abstract, though terms such as "fuzzy coats" and "condensate-like" may require clearer definition in the full text.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a promising concept, but the absence of quantitative results and methodological transparency precludes a supportive recommendation. A revised assessment would require access to the full manuscript.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that Martini3-NMR "significantly enhance[s] the accuracy of CG simulations while maintaining their elevated sampling efficiency."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract provides no quantitative metrics, such as root-mean-square deviations from experimental ensembles, free energy comparisons, or convergence assessments, to support the claim of enhanced accuracy. No baseline comparison to standard Martini3 simulations is described, and no statistical measures of improvement are given.
- **Why it matters** The central premise of the work is that accuracy is improved without sacrificing efficiency. Without quantitative validation, the claim is unsubstantiated, and the reader cannot judge whether the method offers a genuine advance over existing CG approaches or whether any accuracy gains come at an unacceptable computational cost.
- **Resolution test** The full manuscript must provide quantitative comparisons between Martini3-NMR and standard CG simulations for at least one test system, including error metrics relative to experimental data (e.g., chemical shift deviations, NOE violations, or ensemble similarity measures) and computational cost benchmarks.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The authors state that "artificial neural networks to model NMR chemical shifts at the CG level" are used, and that NOE restraints are integrated.
- **Evidence pointer** Abstract only; location not provided
- **Concern** No details are provided on the neural network architecture, training data, feature representation, or how chemical shifts are mapped to CG beads. The integration protocol for NOE restraints into the CG force field is also unspecified, including how restraint strengths, averaging, or violations are handled.
- **Why it matters** Reproducibility is a core requirement for method papers. Without these details, other researchers cannot implement or test the approach, and the scientific community cannot assess the robustness or generalizability of the framework.
- **Resolution test** The full manuscript must include a complete description of the neural network model, training and validation datasets, the mapping from atomistic to CG chemical shifts, and the exact protocol for applying NOE restraints in CG simulations, including any parameters or software used.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim "broad applicability" demonstrated by generating CG ensembles for protein folding from misfolded states, oligomer disassembly within lipid bilayers, and disordered fuzzy regions at amyloid fibril surfaces, which "were found to display condensate-like structural and dynamical properties."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract lists three application areas but provides no results, no system details, no comparison to experimental data, and no analysis supporting the "condensate-like" characterization. The term "condensate-like" is not defined, and no metrics (e.g., density fluctuations, cluster sizes, or dynamic properties) are mentioned.
- **Why it matters** The claim of broad applicability is a key selling point of the method. Without evidence, the reader cannot determine whether the approach works reliably across different system types or whether the "condensate-like" observation is robust or an artifact of the method.
- **Resolution test** The full manuscript must present results for each claimed application, including validation against experimental data where available, and provide a clear operational definition of "condensate-like" with supporting quantitative analyses.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract wording
- **Evidence pointer** Abstract, first paragraph
- **Issue** The phrase "have enabled accessing to extended timescales" is grammatically awkward and should be revised for clarity.
- **Required correction** Change to "have enabled access to extended timescales" or "have enabled the exploration of extended timescales."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract, last sentence
- **Evidence pointer** Abstract, final sentence
- **Issue** The phrase "opens to significant new opportunities" is nonstandard English; "opens up" or "offers" would be more appropriate.
- **Required correction** Revise to "opens up significant new opportunities" or "offers significant new opportunities."

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Precision
- **Affected element** Abstract, application examples
- **Evidence pointer** Abstract, third paragraph
- **Issue** The term "condensate-like" is introduced without definition or context, which may confuse readers unfamiliar with phase separation concepts.
- **Required correction** Provide a brief definition or contextual explanation in the abstract, or defer this characterization to the full text with supporting data.

## Risk / unsupported claims
- The claim of "significantly enhance[d] accuracy" is unsupported by any quantitative data in the abstract.
- The claim of "broad applicability" across three distinct systems is unsupported by results or system-specific details.
- The characterization of amyloid fuzzy regions as displaying "condensate-like structural and dynamical properties" is unsupported and undefined.
- The general statement that Martini3-NMR "provides a novel general framework" is an assertion without comparative or benchmark evidence.
- All methodological claims regarding neural network performance and restraint integration are unverifiable from the abstract alone.