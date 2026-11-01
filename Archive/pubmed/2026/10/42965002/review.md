## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, or supplementary material provided
- **Shared manuscript claim summary** The authors introduce REACT-RNA, a chemically specific coarse-grained molecular dynamics framework coupling RNA polymerization, degradation, and nucleotide fluxes to sequence-dependent protein-RNA phase behavior. They apply it to FUS and MED1 condensates and report that RNA polymerization occurs preferentially at condensate interfaces, generating spatially organized RNA populations that alter condensate properties. They further claim that sustained polymerization drives re-entrant dissolution, while degradation stabilizes long-lived nonequilibrium condensates, and propose a feedback loop between RNA metabolism and condensate organization.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary data
- **Missing materials affecting confidence** Full manuscript, methods description, simulation parameters, force field validation, experimental validation (if any), figures, and supplementary information

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting and potentially impactful framework for studying nonequilibrium RNA-protein condensates. The central claims are plausible and align with emerging themes in the field, but the abstract alone provides insufficient evidence to evaluate technical soundness, model fidelity, or robustness of the reported phenomena. The work would benefit from clearer articulation of validation strategies and quantitative outcomes.
- **Who would be interested in the results, and why** Researchers in biomolecular condensates, phase separation, RNA biology, and nonequilibrium soft matter. The framework could interest computational biophysicists developing chemically specific models for transcription-associated processes, and experimentalists studying transcriptional condensates who seek mechanistic predictions.
- **Major strengths** The abstract addresses a timely and important question, namely how nonequilibrium RNA fluxes shape condensate behavior. The proposed mechanism of interfacial polymerization is novel and mechanistically appealing. The framework appears to integrate sequence specificity with chemical reactions, which is a valuable direction. The prediction of re-entrant dissolution and RNA-mediated stabilization offers testable hypotheses.
- **Major Concerns** The abstract lacks quantitative evidence, validation details, and comparison with experimental data. The claims are stated with high confidence but the supporting evidence is not visible. The relationship between simulation timescales and biological timescales is unclear. The generality of the findings beyond FUS and MED1 is not addressed.
- **Minor Comments** The abstract could clarify what "submolecular resolution" means in the context of coarse-grained modeling. The term "reactive microenvironment" is used without operational definition. The phrase "aged gel-like condensates" would benefit from a precise definition of aging in the model.
- **Technical failings that need to be addressed before the case is established** None can be identified from the abstract alone, but the absence of methods and validation data prevents assessment of technical soundness.
- **Assessment against Nature-style criteria** Originality is high, as the coupling of RNA synthesis and degradation to phase behavior in a chemically specific model appears novel. Scientific importance is potentially high given the relevance to transcriptional condensates and RNA biology. Interdisciplinary readership is plausible, spanning biophysics, cell biology, and RNA biology. Technical soundness cannot be evaluated from the abstract. Readability for nonspecialists is adequate, though some terms require definition.
- **Recommendation posture** Supportive if technical concerns are resolved, but currently not established from the provided evidence.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that REACT-RNA explicitly couples RNA polymerization, degradation, and nucleotide fluxes to sequence-dependent protein-RNA phase behavior at submolecular resolution.
- **Evidence pointer** Abstract only; methods and validation not provided
- **Concern** The abstract provides no details on the coarse-grained model construction, parameterization, or validation. It is unclear how the model achieves "submolecular resolution" while being coarse-grained, and how the chemical reactions are implemented and calibrated.
- **Why it matters** Without evidence of model fidelity and parameterization against known experimental or atomistic data, the quantitative predictions cannot be trusted. The framework's utility depends on its ability to reproduce known phase behavior and reaction kinetics.
- **Resolution test** Provide methods section with model parameters, validation against experimental phase diagrams or atomistic simulations, and sensitivity analysis for key parameters.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The claim that RNA polymerization occurs preferentially at condensate interfaces because interfaces promote a reactive microenvironment combining nucleotide influx, enrichment of reactive RNA chain ends, and enhanced molecular dynamics.
- **Evidence pointer** Abstract only; no figures or quantitative data
- **Concern** The abstract states this as a finding, but no quantitative data are shown to support the preferential localization of polymerization at interfaces, nor the proposed mechanistic drivers.
- **Why it matters** This is a central mechanistic claim that underpins the spatial organization of RNA and the feedback loop. Without quantitative evidence, the claim is unsupported.
- **Resolution test** Provide figures showing spatial distributions of polymerization events, nucleotide concentrations, chain end enrichment, and molecular dynamics metrics at interfaces versus bulk.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The claim that sustained RNA polymerization drives re-entrant condensate dissolution, even of aged gel-like condensates, whereas RNA degradation stabilizes long-lived nonequilibrium condensates.
- **Evidence pointer** Abstract only; no time-resolved data or phase diagrams
- **Concern** The abstract reports these dynamic behaviors without presenting time evolution data, phase diagrams, or stability metrics. The distinction between "aged gel-like" and other condensate states is not defined.
- **Why it matters** These are the key dynamical predictions of the model. Without quantitative evidence, the claims cannot be evaluated, and the biological relevance remains speculative.
- **Resolution test** Provide time-resolved condensate size, density, and composition data under different synthesis and degradation rates, with clear definitions of condensate states.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The claim that the findings apply to FUS and MED1 condensates and suggest a general feedback mechanism for transcriptional condensates.
- **Evidence pointer** Abstract only; no comparison across systems
- **Concern** The abstract does not discuss whether the observed behaviors are specific to FUS and MED1 or generalizable to other transcriptional condensates with different RNA-binding domains or sequence compositions.
- **Why it matters** The broader significance of the work depends on the generality of the proposed mechanism. Without comparative analysis, the scope of the claims is unclear.
- **Resolution test** Include simulations or discussion of additional protein-RNA systems, or clearly state the limitations of the current model.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Definition of "submolecular resolution"
- **Evidence pointer** Abstract
- **Issue** The term is ambiguous in the context of coarse-grained modeling.
- **Required correction** Clarify what resolution level is achieved and how it relates to chemical specificity.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Definition of "reactive microenvironment"
- **Evidence pointer** Abstract
- **Issue** The term is used without operational definition.
- **Required correction** Define the criteria used to identify a reactive microenvironment in the simulations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Definition of "aged gel-like condensates"
- **Evidence pointer** Abstract
- **Issue** The term is not defined in the abstract.
- **Required correction** Provide a definition based on simulation observables, such as dynamics or connectivity.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract structure
- **Evidence pointer** Abstract
- **Issue** The abstract is dense and mixes mechanistic detail with high-level claims.
- **Required correction** Consider restructuring to separate model description, key findings, and implications.

## Risk / unsupported claims
- The claim of preferential interfacial polymerization is unsupported without quantitative spatial data.
- The claim of re-entrant dissolution and degradation-mediated stabilization is unsupported without time-resolved data.
- The claim of a feedback loop between RNA metabolism and condensate organization is speculative without direct evidence of causality.
- The generalizability of findings beyond FUS and MED1 is not assessable from the abstract.
- The biological relevance of the simulation timescales and conditions is not assessable without methods.