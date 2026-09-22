## Review setup
- **Input scope** Full preprint text (abstract and main text as provided)
- **Assessment boundary** Scientific claims, methodology, and evidence as presented in the supplied material
- **Shared manuscript claim summary** The authors propose that biomolecular condensates formed by prion-like low complexity domains exhibit internal network microstructures, characterized by small-world topology with hubs and cliques, and that this microstructure couples molecular-level features to mesoscale material properties such as surface tension and single-molecule dynamics
- **Visible evidence base** Abstract and main text narrative; no figures, tables, methods details, or supplementary materials were provided
- **Missing materials affecting confidence** Figures, simulation parameters, force field details, sequence definitions, statistical analyses, and any quantitative results

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question in the field of biomolecular condensates, namely how molecular-level interactions translate into mesoscale material properties. The conceptual framework linking network topology to condensate properties is intellectually appealing and potentially impactful. However, the provided material is insufficient to evaluate the technical validity of the claims. Key quantitative results, methodological details, and visual evidence are absent, making it impossible to assess whether the conclusions are supported by the data. The narrative is coherent and well written, but the scientific case is not established from the supplied material alone.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, soft matter physics, and computational biophysics would be interested. The work offers a potential bridge between molecular simulation and macroscopic material behavior, which is relevant for understanding condensate function in health and disease, and for designing synthetic condensates with tailored properties.
- **Major strengths** The conceptual framing is novel and timely, connecting graph-theoretic descriptions of molecular networks to experimentally relevant material properties. The use of both natural LCD sequences and designed binary sequences provides a systematic approach to generalize findings. The proposed link between network small-worldness and surface tension is a testable and potentially powerful predictive relationship.
- **Major Concerns** The absence of quantitative data, figures, and methodological details prevents verification of the central claims. The relationship between network topology and surface tension is stated but not demonstrated with numbers or statistical support. The claim that cliques localize near interfaces without a secondary phase transition is intriguing but unsupported by visible evidence. The generalization from specific sequences to general principles is asserted without sufficient parametric exploration being shown.
- **Minor Comments** The abstract is well structured but contains several terms (hubs, cliques, small-worldness) that are not defined for a general readership. The phrase "systematically encoded by network topology" is vague without specific quantitative metrics. The manuscript would benefit from a brief explanation of the coarse-grained model used, even in the abstract.
- **Technical failings that need to be addressed before the case is established** No quantitative results are visible; no figures or tables are provided; simulation methodology is not described; statistical significance of the claimed relationships is not reported; the definition and calculation of network metrics are not specified.
- **Assessment against Nature-style criteria** Originality is high, as the network-based multiscale framework appears novel. Scientific importance is potentially high, given the broad relevance of condensate material properties. Interdisciplinary readership is plausible, spanning biophysics, soft matter, and cell biology. Technical soundness cannot be assessed from the provided material. Readability for nonspecialists is moderate, but the abstract assumes familiarity with network terminology and condensate physics.
- **Recommendation posture** Currently not established from the provided evidence. The conceptual framework is promising, but the manuscript requires full presentation of methods, results, and figures before a supportive assessment can be made.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that network small-worldness predicts droplet surface tension.
- **Evidence pointer** Location not provided
- **Concern** The claim that small-worldness predicts surface tension is central to the manuscript, but no quantitative data, correlation coefficients, or statistical tests are presented in the supplied material. The relationship is stated qualitatively without any visible support.
- **Why it matters** This is a core predictive claim that would be of high interest to the field. Without quantitative evidence, the claim cannot be evaluated or reproduced, undermining the manuscript's central contribution.
- **Resolution test** Provide a figure showing the relationship between small-worldness and surface tension across multiple sequences, with correlation statistics and error estimates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that cliques localize near interfaces without a secondary phase transition.
- **Evidence pointer** Location not provided
- **Concern** The localization of cliques near interfaces is a specific and unusual claim, but no spatial data, density profiles, or interface definitions are provided. The absence of a secondary phase transition is asserted without supporting thermodynamic or structural evidence.
- **Why it matters** This claim has implications for understanding interfacial properties and condensate aging. If unsupported, it could mislead subsequent interpretations of condensate behavior.
- **Resolution test** Provide spatial density maps or radial distribution functions showing clique localization relative to the interface, along with evidence ruling out a phase transition, such as order parameter profiles or free energy calculations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The authors use a residue-resolution coarse-grained model to probe condensates comprising natural LCD sequences and binary sequences.
- **Evidence pointer** Location not provided
- **Concern** No details of the coarse-grained model, force field parameters, simulation protocols, or sequence definitions are given. Without this information, the simulations cannot be reproduced or assessed for accuracy.
- **Why it matters** Reproducibility is a fundamental requirement for computational studies. The lack of methodological detail prevents independent verification and limits the utility of the findings.
- **Resolution test** Include a full methods section describing the model, parameters, simulation length, equilibration criteria, and system sizes, plus a table of sequences used.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that internal heterogeneity at the single-molecule level is systematically encoded by network topology.
- **Evidence pointer** Location not provided
- **Concern** The relationship between single-molecule structure and dynamics and network topology is stated but not demonstrated with any quantitative metrics, such as correlation coefficients or comparative analyses across different network types.
- **Why it matters** This claim links molecular behavior to network properties, which is a key part of the multiscale framework. Without evidence, the claim remains speculative.
- **Resolution test** Provide quantitative comparisons of single-molecule conformational metrics and diffusion coefficients against network centrality or clustering measures, with statistical support.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract
- **Evidence pointer** Location not provided
- **Issue** Terms such as hubs, cliques, and small-worldness are used without definition, which may confuse nonspecialist readers.
- **Required correction** Add brief parenthetical definitions or a sentence explaining these network concepts in the context of condensates.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Location not provided
- **Issue** The phrase "systematically encoded by network topology" is vague and does not specify which metrics or relationships are meant.
- **Required correction** Specify the particular network metrics and single-molecule properties that are correlated, even at a qualitative level.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Abstract
- **Evidence pointer** Location not provided
- **Issue** The abstract does not mention the range of sequences studied or the number of simulations performed, which would help gauge the generality of the findings.
- **Required correction** Include a brief statement on the number and diversity of sequences and simulation replicates.

## Risk / unsupported claims
- The predictive relationship between network small-worldness and surface tension is unsupported by visible quantitative evidence.
- The localization of cliques near interfaces without a secondary phase transition is unsupported by visible spatial or thermodynamic data.
- The claim that single-molecule heterogeneity is systematically encoded by network topology is unsupported by visible comparative analyses.
- The generalization from specific sequences to general design principles is not assessable without details on the parametric variation performed.
- The overall multiscale structure-property relationships are asserted but cannot be evaluated without figures and quantitative results.