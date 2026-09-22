## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no evaluation of methodology details, simulation parameters, or quantitative results beyond what is stated
- **Shared manuscript claim summary** The authors use Martini 3 coarse-grained simulations to study phase transitions of G4C2 RNA repeats across salt concentrations. They report salt-dependent transitions from dispersed to condensed states, shifts in dominant interaction patterns (Watson-Crick-like and G-G contacts) with ionic strength, and length-dependent stability of phase-separated states. They conclude the model reproduces key biophysical features of RNA LLPS and provides molecular-level insight into sequence composition and ionic strength effects.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary materials provided
- **Missing materials affecting confidence** Full manuscript, simulation protocols, force field parameters, system sizes, salt concentration ranges, quantitative phase diagram data, comparison details with experiments, and all figures/tables

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting application of Martini 3 coarse-grained simulations to RNA repeat phase separation, a topic of relevance to neurodegeneration research. The claims are plausible but the evidence base is entirely inaccessible from the abstract alone. The central conclusions regarding salt-dependent and length-dependent condensation rest on simulation results that cannot be evaluated without methodological detail and quantitative data. The work may be of interest to the computational biophysics and RNA biology communities, but the current abstract does not provide sufficient information to assess technical soundness or the strength of the claims.
- **Who would be interested in the results, and why** Computational biophysicists studying biomolecular condensates and LLPS would be interested in the demonstration of Martini 3 applicability to RNA systems. Researchers working on ALS and FTD, particularly those studying G4C2 repeat expansions, would be interested in the molecular-level insights into repeat RNA phase behavior. The broader RNA biology community interested in sequence- and salt-dependent phase separation would also find relevance.
- **Major strengths** The topic is timely and of high interest given the growing focus on RNA-driven condensates in neurodegeneration. The use of Martini 3, a widely used coarse-grained model, suggests potential broad applicability. The explicit focus on salt dependence and sequence length effects addresses key biophysical variables. The claim that the model reproduces experimental observations of length-dependent stability adds translational relevance.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1 (simulation validation), R1-M2 (quantitative evidence), R1-M3 (interaction pattern analysis)
- **Assessment against Nature-style criteria** Originality: the application of Martini 3 to G4C2 repeat RNA phase separation appears novel, though the abstract does not clarify how this extends beyond prior coarse-grained RNA LLPS studies. Scientific importance: potentially high given the disease relevance, but the abstract does not establish the magnitude of the advance. Interdisciplinary readership: the topic bridges computational biophysics, RNA biology, and neurodegeneration, which could attract broad interest. Technical soundness: cannot be assessed from the abstract; no methodological details, validation, or error analysis are provided. Readability for nonspecialists: the abstract is generally clear and accessible, though terms such as "Watson-Crick-like contacts" and "condensed-like states" could benefit from brief clarification for a general audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents interesting claims, but the absence of methodological detail and quantitative results prevents assessment of whether the conclusions are supported. A supportive posture would require access to the full manuscript.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The model captures salt-dependent transitions from dispersed to condensed-like states and reproduces key biophysical features of RNA LLPS.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract claims the Martini 3 model captures salt-dependent phase transitions, but no information is provided on how the simulations were validated against experimental data, what salt concentration ranges were tested, how many independent simulations were performed, or how finite-size effects and equilibration were addressed. Coarse-grained models are known to be sensitive to parameter choices, and Martini 3 has not been extensively benchmarked for RNA LLPS. Without this information, the reliability of the reported phase behavior cannot be evaluated.
- **Why it matters** The central claim of the paper rests on the ability of the simulation model to faithfully reproduce RNA phase behavior. If the model has not been validated or if the simulation protocol is inadequate, the conclusions about salt- and length-dependent condensation would be unsupported. This is the foundation of the entire study.
- **Resolution test** Provide simulation details including system composition, box sizes, salt concentrations, simulation lengths, number of replicas, and equilibration criteria. Include validation against experimental phase diagrams or known RNA structural data. Demonstrate convergence of phase behavior across independent simulations and system sizes.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** Longer RNA sequences maintain phase-separated states at salt concentrations that dissolve shorter ones, in line with experimental observations.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract states that longer sequences maintain phase-separated states at salt concentrations that dissolve shorter ones, but no quantitative data are presented. No phase boundaries, critical salt concentrations, or free energy estimates are given. The comparison to experimental observations is mentioned but not specified, making it impossible to assess the degree of agreement or the significance of the finding.
- **Why it matters** The length-dependent behavior is a key claim that connects the simulations to experimental relevance. Without quantitative phase diagrams or at least numerical values for transition points, the claim cannot be verified. The comparison to experiments is essential for establishing the predictive value of the model.
- **Resolution test** Provide quantitative phase diagrams showing dispersed versus condensed states as a function of salt concentration for at least two RNA lengths. Include numerical values for transition salt concentrations and, where possible, direct comparison to experimental data with quantitative agreement metrics.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation
- **Claim pointer** Dominant interaction patterns, including Watson-Crick-like and G-G contacts, shift with ionic strength.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract claims that interaction patterns shift with ionic strength, but the nature of this shift is not described. It is unclear whether the shift is gradual or abrupt, which specific contacts become more or less dominant, and how these changes relate mechanistically to the observed phase behavior. The term "Watson-Crick-like" is ambiguous in the context of G4C2 repeats, which are known to form G-quadruplex structures, and the abstract does not clarify whether such structures are observed.
- **Why it matters** The interaction analysis is presented as providing molecular-level insight into the phase separation mechanism. If the interpretation of interaction patterns is ambiguous or incomplete, the mechanistic conclusions are weakened. The relationship between specific contact types and phase stability is central to the claimed insight.
- **Resolution test** Provide detailed contact analysis with clear definitions of interaction types, including whether G-quadruplex or other non-canonical structures are considered. Show how contact populations change quantitatively with salt concentration and relate these changes to phase behavior. Clarify the structural interpretation of "Watson-Crick-like" contacts in the context of G4C2 repeats.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract terminology
- **Evidence pointer** Abstract text
- **Issue** The term "condensed-like states" is vague and could refer to a range of phenomena from transient clustering to true phase-separated droplets. The abstract does not clarify the criteria used to define these states.
- **Required correction** Define the operational criteria for "condensed-like states" in the abstract, such as cluster size thresholds, density criteria, or coexistence analysis.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Experimental comparison
- **Evidence pointer** Abstract text
- **Issue** The abstract states the results are "in line with experimental observations" but does not specify which experiments or how the comparison was made.
- **Required correction** Cite the specific experimental studies and briefly describe the nature of the comparison, including any quantitative metrics used.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scope
- **Affected element** Generalizability claim
- **Evidence pointer** Abstract text
- **Issue** The abstract claims the work provides insight into "sequence composition and ionic strength" effects, but only G4C2 repeats are studied. The generalizability to other RNA sequences is not demonstrated.
- **Required correction** Either temper the claim to be specific to G4C2 repeats or provide preliminary evidence that the findings extend to other repeat sequences.

## Risk / unsupported claims
- The claim that the Martini 3 model "reproduces key biophysical features of RNA LLPS" is unsupported from the abstract alone, as no validation data are presented.
- The claim of "molecular-level insight into RNA-driven phase separation" is not substantiated without detailed interaction analysis and structural interpretation.
- The quantitative agreement with experimental observations is not assessable, as no specific experimental comparisons or numerical values are provided.
- The generalizability of findings to RNA phase separation beyond G4C2 repeats is not established from the presented material.