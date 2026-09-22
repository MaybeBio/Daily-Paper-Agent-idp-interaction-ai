## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors present an automated protocol (QEBSS) that integrates molecular dynamics simulations with NMR spin relaxation data to select experimentally validated conformational ensembles of intrinsically disordered proteins (IDPs). They claim that spin relaxation provides more stringent discrimination between IDP ensembles than chemical shifts or SAXS, and they apply the protocol to four IDPs, revealing a spectrum of conformational behaviors from random coil to compact states.
- **Visible evidence base** Abstract text only; no quantitative results, methodological details, or validation metrics are visible
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, simulation parameters, NMR experimental details, validation statistics, and comparison data for chemical shift and SAXS benchmarks

## Reviewer
- **Overall assessment** The abstract presents a potentially valuable methodological contribution to the IDP ensemble determination field. The central claim that NMR spin relaxation offers superior discrimination power over chemical shifts and SAXS is scientifically plausible and, if rigorously demonstrated, would be of considerable interest. However, the abstract alone provides no quantitative evidence to support this claim, and the absence of methodological detail prevents any assessment of technical soundness. The application to four diverse IDPs suggests breadth, but the functional interpretations offered are speculative without supporting data.
- **Who would be interested in the results, and why** Researchers in the IDP structural biology community, computational biophysicists developing ensemble determination methods, NMR spectroscopists studying protein dynamics, and developers of force fields and machine learning models for IDP prediction. The benchmark datasets proposed would be of direct utility to these groups.
- **Major strengths** The methodological concept is timely and addresses a recognized bottleneck in IDP ensemble determination. The comparative claim regarding spin relaxation versus chemical shifts and SAXS is a testable hypothesis that, if confirmed, would advance the field. The selection of four biologically diverse IDPs with distinct conformational characteristics provides a useful test bed. The stated goal of establishing benchmark datasets for force field and machine learning development is valuable.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
  - R1-m4
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: the concept of using spin relaxation for ensemble selection is not entirely new, but the systematic automated protocol and the comparative benchmarking claim may offer a novel contribution. Scientific importance: potentially high if the discrimination claim holds, as it would provide a more rigorous selection criterion for IDP ensembles. Interdisciplinary readership: the work bridges NMR spectroscopy, molecular dynamics simulation, and IDP biology, which could attract a broad readership. Technical soundness: cannot be assessed from the abstract alone; the absence of any quantitative validation is a critical gap. Readability for nonspecialists: the abstract is generally clear, though terms such as QEBSS and specific protein identifiers are introduced without context.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a promising framework, but the core claims require full manuscript evaluation. Supportive if technical concerns are resolved upon review of the complete work.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that spin relaxation measurements provide more stringent discrimination between distinct IDP ensembles than chemical shift or SAXS data.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The central comparative claim is stated without any quantitative support. No discrimination metrics, statistical comparisons, or error analyses are presented. It is unclear how the stringency of spin relaxation was quantified relative to chemical shifts and SAXS, whether the comparison was performed under matched conditions, and whether the conclusion holds across all four IDPs or only a subset.
- **Why it matters** This claim is the primary methodological contribution of the work. If the comparison is not rigorously controlled or the metrics are not well defined, the conclusion may be overstated or condition-dependent. The utility of the QEBSS protocol hinges on this claim being robust.
- **Resolution test** Provide quantitative discrimination metrics (for example, ensemble separation in reduced chi-square space, Bayesian evidence ratios, or cross-validation scores) for spin relaxation, chemical shifts, and SAXS across all four IDPs, with appropriate uncertainty estimates and statistical testing.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The QEBSS protocol is described as automated and integrates molecular dynamics simulations with NMR spin relaxation data to determine experimentally validated conformational ensembles.
- **Evidence pointer** Abstract only; location not provided
- **Concern** No methodological details are provided regarding the QEBSS protocol. Key questions include how the simulation ensembles were generated, how many independent simulations were performed, how convergence was assessed, how the spin relaxation data were processed and back-calculated, what model-free or spectral density approach was used, and how the selection threshold was defined. Without this information, the reproducibility and robustness of the protocol cannot be evaluated.
- **Why it matters** The protocol is the core deliverable of the work. If the automation pipeline has arbitrary thresholds, insufficient sampling, or inadequate treatment of experimental uncertainty, the selected ensembles may not be reliable. The claim of experimental validation depends entirely on the rigor of the integration method.
- **Resolution test** Provide a complete description of the QEBSS workflow, including simulation parameters, convergence criteria, spin relaxation back-calculation methodology, selection thresholds, and a validation strategy such as cross-validation against held-out experimental data.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The authors state that the four IDPs reveal a spectrum of conformational behaviors ranging from near-random coil structures to compact, transiently ordered states, with specific descriptions for each protein.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The conformational descriptions for each protein are presented as definitive findings, but no quantitative measures are provided. Terms such as minimal backbone correlations, charge-driven transient looping, moderate backbone ordering, and extensive intrachain contacts are not defined with numerical thresholds or statistical confidence. It is unclear whether these distinctions are statistically significant and whether they emerge from the spin relaxation selection or are influenced by the simulation force field.
- **Why it matters** These per-protein characterizations are the biological findings of the study. If the distinctions are not quantitatively supported, the functional interpretations drawn from them are speculative. The claim of a spectrum of behaviors is only meaningful if the differences between proteins exceed the uncertainty of the method.
- **Resolution test** Provide quantitative ensemble descriptors for each protein, such as radius of gyration distributions, contact probabilities, secondary structure propensities, and order parameter profiles, with statistical uncertainties and significance testing for inter-protein comparisons.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract; location not provided
- **Issue** The acronym QEBSS is introduced without expansion or contextual explanation of what quality evaluation entails.
- **Required correction** Expand the acronym at first use and briefly describe the evaluation criteria used in the selection process.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Protein selection rationale
- **Evidence pointer** Abstract; location not provided
- **Issue** The four IDPs are described as biologically diverse, but the rationale for selecting these specific proteins is not stated.
- **Required correction** Briefly justify the choice of these four proteins, for example in terms of sequence length, charge distribution, biological function, or availability of experimental data.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Functional implications
- **Evidence pointer** Abstract; location not provided
- **Issue** The statement that the ensembles provide insights into how conformational properties relate to biological function is not supported by any specific functional correlation in the abstract.
- **Required correction** Either provide a concrete example of a structure-function relationship observed, or temper the claim to indicate that the ensembles provide a foundation for future functional studies.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Context
- **Affected element** Benchmark claim
- **Evidence pointer** Abstract; location not provided
- **Issue** The claim of establishing high-resolution benchmark datasets is not accompanied by any description of what constitutes high resolution in this context or how the datasets will be made accessible.
- **Required correction** Specify the resolution criteria for the benchmark datasets and state the intended data deposition or availability plan.

## Risk / unsupported claims
- The comparative superiority of spin relaxation over chemical shifts and SAXS is unsupported by any quantitative evidence in the abstract.
- The specific conformational characterizations of the four IDPs are asserted without numerical descriptors or statistical confidence.
- The claim of experimental validation of the ensembles is unverifiable without details on the validation methodology.
- The functional insights claim is speculative and not tied to any specific observation.
- The benchmark dataset claim is not assessable without information on data format, resolution criteria, or accessibility.
- The automated nature of the QEBSS protocol cannot be evaluated without workflow details.