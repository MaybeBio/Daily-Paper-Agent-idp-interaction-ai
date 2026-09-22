## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors use computational tools and molecular dynamics simulations to propose that human HOX transcription factors have a strong propensity for liquid-liquid phase separation, driven by large disordered regions via a fly-casting mechanism, with transient secondary structures matching short linear motifs that may recruit partner molecules such as TALE proteins into biomolecular cocondensates. They report mapping 352 SliMs in droplet-promoting disordered regions and provide an interactive webpage for motif maps.
- **Visible evidence base** Abstract text only; no methodological details, simulation parameters, validation metrics, or quantitative results are provided
- **Missing materials affecting confidence** Full manuscript, methods section, simulation details, validation of computational predictions, experimental corroboration, figure and table data, and details of the webpage content

## Reviewer
- **Overall assessment** The abstract presents an interesting and potentially significant hypothesis regarding phase separation of HOX transcription factors, with a plausible mechanistic model involving disordered regions and short linear motifs. However, the evidence base is entirely computational and descriptive, with no quantitative metrics, controls, or experimental validation. The claims of "strong propensity" and the proposed mechanism are not established from the supplied material. The work may be of interest to the phase separation and transcription factor communities, but the current abstract does not provide sufficient evidence to support the central conclusions.
- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation, transcription factor biology, developmental biology, and gene regulation would be interested. The potential link between HOX factors and phase separation could inform understanding of developmental processes and cancer biology. Computational biologists working on disordered protein prediction and molecular dynamics may also find the approach relevant.
- **Major strengths** The hypothesis is timely and addresses a gap in understanding HOX factor function. The proposed fly-casting mechanism is mechanistically plausible and testable. The integration of SliM mapping with disordered regions provides a concrete framework for partner recruitment. The provision of an interactive webpage is a useful resource for the community.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality is moderate; the application of phase separation concepts to HOX factors is novel but builds on established frameworks. Scientific importance is potentially high given the developmental and disease relevance of HOX factors, but the current evidence is insufficient to establish significance. Interdisciplinary readership is plausible, spanning biophysics, molecular biology, and computational biology. Technical soundness cannot be assessed from the abstract alone, as no methodological details or validation are provided. Readability for nonspecialists is adequate, though some terms such as "fly-casting" and "SliMs" are introduced without definition in the abstract.
- **Recommendation posture** Currently not established from the provided evidence. The hypothesis is interesting, but the abstract lacks the quantitative and methodological detail required to support the claims. A revised manuscript with full methods, validation, and ideally experimental corroboration would be needed to make the case.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "we found that the human HOX transcription factors have a strong propensity to undergo phase separation"
- **Evidence pointer** Abstract text; location not provided
- **Concern** The claim of a "strong propensity" for phase separation is made without any quantitative metric, such as scores from prediction algorithms, free energy estimates, or simulation-based measures. No thresholds, controls, or comparisons to known phase-separating proteins are provided.
- **Why it matters** Without quantitative evidence, the claim is subjective and cannot be evaluated or reproduced. The strength of the propensity is central to the paper's thesis, and the abstract does not provide a basis for this assertion.
- **Resolution test** Provide specific prediction scores, simulation observables (e.g., density profiles, cluster sizes, contact maps), and statistical comparisons to negative controls or known phase-separating systems. State thresholds used to define "strong" propensity.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic support
- **Claim pointer** "The large disordered regions of the HOX factors drive phase separation via a fly-casting like mechanism, where the terminal segments of the disordered regions extend out to interact with and draw in neighboring molecules."
- **Evidence pointer** Abstract text; location not provided
- **Concern** The fly-casting mechanism is proposed based on MD simulations, but no simulation details are given, including force field, simulation length, system composition, or analysis methods. No evidence is shown that terminal segments specifically extend and interact with neighboring molecules, as opposed to other regions of the disordered segments.
- **Why it matters** The mechanism is a central novel contribution. Without supporting simulation data and analysis, the claim is speculative and cannot be distinguished from alternative mechanisms such as multivalent interactions along the entire disordered region.
- **Resolution test** Present simulation snapshots, distance or contact time series for terminal segments, and comparative analyses of different regions of the disordered segments. Provide simulation parameters and demonstrate that the observed behavior is robust across replicates and conditions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Functional inference
- **Claim pointer** "the HOX transcription factors may act as scaffold proteins and recruit partner molecules, such as TALE proteins, in the biomolecular cocondensates, via interaction with these preformed structural elements."
- **Evidence pointer** Abstract text; location not provided
- **Concern** The inference that transient secondary structures matching SliMs enable partner recruitment is speculative. No experimental or computational evidence is provided that these structures are populated under physiological conditions, that they are accessible for binding, or that they actually interact with TALE proteins or other partners.
- **Why it matters** The scaffold function and partner recruitment are key functional implications of the work. Without evidence of binding or cocondensation, this claim is unsupported and may overstate the biological relevance of the findings.
- **Resolution test** Provide binding assays, cocondensation experiments, or enhanced sampling simulations showing that the identified SliMs interact with partner proteins. Alternatively, present evidence that the transient structures are stable enough and exposed for interaction.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract text; location not provided
- **Issue** The term "fly-casting" is used without definition or citation, which may confuse nonspecialist readers.
- **Required correction** Define the term briefly or provide a citation to the original concept.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Resource description
- **Affected element** Webpage
- **Evidence pointer** Abstract text; location not provided
- **Issue** The interactive webpage is mentioned, but its content, usability, and validation are not described. It is unclear what data are displayed and how they were generated.
- **Required correction** Describe the webpage features, data sources, and any validation or user testing in the main text or supplementary materials.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scope
- **Affected element** Context-dependent claim
- **Evidence pointer** Abstract text; location not provided
- **Issue** The abstract title and final sentence emphasize "context-dependent" interactions, but the abstract does not explain what context means here or how it was investigated.
- **Required correction** Clarify the concept of context dependence and describe how it was addressed in the study.

## Risk / unsupported claims
- The claim of "strong propensity" for phase separation is unsupported without quantitative metrics.
- The fly-casting mechanism is unsupported without simulation details and direct evidence.
- The scaffold function and partner recruitment via SliMs are unsupported without binding or cocondensation evidence.
- The number 352 SliMs is stated without context, such as how it compares to expected frequencies or what fraction of the disordered regions they cover.
- The biological relevance to HOX-related processes is asserted but not demonstrated.
- The webpage content and its utility are not assessable from the abstract.