## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as stated in the abstract
- **Shared manuscript claim summary** The authors propose design principles for intrinsically disordered regions (IDRs) in transcription factors (TFs), arguing that IDRs enhance both binding affinity and search time, with model predictions consistent with experimental results.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or experimental data provided
- **Missing materials affecting confidence** Full manuscript, methods, model equations, parameter values, experimental datasets, and validation details

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting theoretical contribution to understanding IDR function in TF DNA search. However, the current evidence base is insufficient to evaluate the validity of the claims. The central assertions regarding enhancement of binding affinity and search time lack quantitative support, and the claimed agreement with experiments cannot be assessed without access to the underlying data and model details.
- **Who would be interested in the results, and why** Researchers in gene regulation, biophysics of protein-DNA interactions, and computational biology would find these results relevant. The work addresses a fundamental question about how IDRs contribute to TF function, which has implications for understanding transcriptional control mechanisms and potentially for engineering synthetic TFs.
- **Major strengths** The question addressed is timely and important, given recent experimental findings on IDR roles in TF search. The abstract clearly identifies a gap in understanding and proposes a framework to address it. The stated intention to connect theory with experiments is commendable.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** 
  - Originality: The question of IDR design principles is timely, but the abstract does not clearly distinguish the proposed framework from existing models of facilitated diffusion or IDR-mediated interactions. Originality cannot be fully assessed without the full manuscript.
  - Scientific importance: If substantiated, the findings could have broad relevance for understanding TF regulation across eukaryotes. However, the abstract does not provide sufficient evidence to establish the significance of the claimed effects.
  - Interdisciplinary readership: The topic bridges biophysics, molecular biology, and computational modeling, which could appeal to a broad audience. The abstract is written in accessible language.
  - Technical soundness: Cannot be evaluated from the abstract alone. No model details, parameter choices, or statistical analyses are provided.
  - Readability for nonspecialists: The abstract is clearly written and avoids excessive jargon, making it accessible to a general scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a plausible hypothesis but lacks the quantitative and methodological detail required to assess the validity of the claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "the IDR significantly enhances both of these aspects" referring to binding affinity and search time.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract states that IDRs enhance binding affinity and search time but provides no quantitative results, no model description, and no comparison to baseline conditions without IDRs. The magnitude of the claimed enhancement is not specified, and it is unclear whether the effect is universal across different TF types or specific to certain conditions.
- **Why it matters** Without quantitative details, the central claim cannot be evaluated. The term "significantly" implies statistical or functional significance, but no metrics are provided. This is the core assertion of the paper, and its validity is essential for the manuscript's contribution.
- **Resolution test** Provide quantitative results in the full manuscript, including effect sizes, confidence intervals, or statistical tests comparing models with and without IDRs. Specify the conditions under which enhancement occurs and any limitations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors claim that "our model shows good agreement with experimental results."
- **Evidence pointer** Abstract, location not provided
- **Concern** No experimental datasets are referenced or described. The abstract does not specify which experiments were used for comparison, what metrics were compared, or how agreement was quantified. Without this information, the claim of agreement is unverifiable.
- **Why it matters** Agreement with experiments is a key pillar of the paper's credibility. If the comparison is not rigorous or the datasets are not appropriate, the conclusion may be overstated. The lack of detail prevents any assessment of whether the model captures biologically relevant behavior.
- **Resolution test** In the full manuscript, clearly identify the experimental datasets used, describe the comparison methodology, and provide quantitative measures of agreement such as correlation coefficients, error metrics, or statistical tests.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The authors propose "design principles of the IDR related to TF binding affinity and search time."
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract does not describe the model framework, the parameters used, or the assumptions underlying the design principles. It is impossible to determine whether the principles are generalizable or specific to the model's construction. No information is given about the model type, such as stochastic simulations, mean-field theory, or molecular dynamics.
- **Why it matters** Reproducibility is a fundamental requirement for scientific claims. Without model details, other researchers cannot test or build upon the proposed principles. The lack of methodological transparency undermines the paper's utility to the community.
- **Resolution test** Provide a complete model description in the full manuscript, including equations, parameter values, simulation protocols, and sensitivity analyses. Make code or model implementations available where appropriate.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract wording
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "search time" is used without defining whether it refers to the mean first-passage time to the target, the association rate, or another kinetic measure. This ambiguity could confuse readers.
- **Required correction** Define "search time" explicitly in the abstract or full manuscript, specifying the kinetic quantity being measured.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Scope
- **Affected element** Generalizability claim
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract states that "most TFs contain an IDR" and implies the design principles are general, but it does not address potential variations in IDR length, composition, or function across different TF families.
- **Required correction** Acknowledge potential limitations in generalizability or provide evidence that the principles hold across diverse TF families.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Proposed experiments
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract mentions "we propose further experiments to validate the model's predictions" but does not indicate what these experiments would measure or how they would distinguish the model from alternatives.
- **Required correction** Briefly describe the nature of the proposed experiments in the abstract or full manuscript, including what specific predictions they would test.

## Risk / unsupported claims
- The claim that IDRs "significantly enhance" binding affinity and search time is unsupported without quantitative data.
- The claim of "good agreement with experimental results" is unverifiable without specifying the experiments and comparison metrics.
- The proposed "design principles" cannot be evaluated without model details and assumptions.
- The generalizability of the findings to all TFs with IDRs is asserted but not supported by evidence in the abstract.