## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors propose that protein aggregation within liquid-liquid phase separated condensates (the "condensation pathway") is governed by three sequence features: droplet-promoting propensity, aggregation-promoting propensity, and multimodal interactions quantified by binding mode entropy. They claim this framework enables prediction of aggregation-promoting mutations in droplet-forming proteins associated with amyotrophic lateral sclerosis (ALS), and provides insights into the amino acid code for liquid-to-solid conversion of condensates.
- **Visible evidence base** Abstract text only; no methodological details, datasets, validation statistics, or case study results are visible
- **Missing materials affecting confidence** Full manuscript, methods section, figures, tables, supplementary data, and any quantitative validation of the predictive approach

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting framework for understanding sequence determinants of protein aggregation within condensates, a topic of growing importance in the context of neurodegenerative diseases. However, the evidence base available for review is limited to the abstract, which precludes assessment of methodological rigor, validation, and the strength of the predictive claims. The central assertion that three features can predict aggregation-promoting mutations is plausible but not verifiable from the supplied material.
- **Who would be interested in the results, and why** Researchers in the fields of protein phase separation, amyloid aggregation, neurodegeneration (particularly ALS), and computational biology would find these results relevant. The work addresses a gap between deposition-based aggregation prediction and condensation-based aggregation, which is of interest to those studying the molecular mechanisms of liquid-to-solid transitions in biomolecular condensates.
- **Major strengths** The abstract identifies a clear gap in current computational approaches, namely the lack of sequence-based predictors for aggregation within condensates. The proposal of three distinct features provides a structured framework that could be operationally useful. The connection to ALS-associated proteins gives the work translational relevance.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
- **Technical failings that need to be addressed before the case is established** The abstract does not provide any quantitative evidence, such as prediction accuracy, sensitivity, specificity, or comparison to existing methods. Without these, the claim that the approach "makes it possible to predict" mutations is not established. The definition and computation of "binding mode entropy" are not described, and its role as a predictive feature is not justified.
- **Assessment against Nature-style criteria** 
  - Originality: The framework appears novel in combining droplet-promoting and aggregation-promoting propensities with binding mode entropy, but the abstract does not demonstrate how this differs from existing methods beyond the stated gap.
  - Scientific importance: The topic is important, given the increasing recognition of condensate-mediated aggregation in disease. However, the abstract does not provide evidence of broad mechanistic insight beyond a descriptive framework.
  - Interdisciplinary readership: The work bridges biophysics, computational biology, and neurobiology, which could appeal to a broad audience, but the abstract is too brief to convey the depth required for such reach.
  - Technical soundness: Not assessable from the abstract. No methodological details, validation, or statistical measures are provided.
  - Readability for nonspecialists: The abstract is concise and uses accessible terminology, though terms like "binding mode entropy" and "multimodal interactions" are introduced without definition, which may hinder nonspecialist comprehension.
- **Recommendation posture** Currently not established from the provided evidence. The conceptual framework is promising, but the abstract alone does not provide sufficient evidence to support the predictive claims. A full manuscript with detailed methods and validation would be required to assess whether the case is made.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "it is possible to predict aggregation-promoting mutations in droplet-forming proteins associated with ALS" using the three identified features.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract states that the approach enables prediction of aggregation-promoting mutations, but no quantitative results, validation metrics, or comparison to experimental data are presented. It is unclear how many proteins were tested, what the prediction accuracy was, or whether any predictions were experimentally confirmed.
- **Why it matters** A predictive claim requires demonstration of predictive performance. Without validation data, the claim is unsupported and cannot be evaluated for reliability or generalizability.
- **Resolution test** Provide in the full manuscript a clear description of the dataset, the prediction methodology, and quantitative performance metrics (e.g., area under the curve, sensitivity, specificity) with appropriate benchmarks and, ideally, experimental validation of at least a subset of predictions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological clarity
- **Claim pointer** The authors identify "multimodal interactions quantified by the binding mode entropy" as one of three relevant sequence features.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The concept of "binding mode entropy" is introduced without definition or explanation of how it is computed. The relationship between this feature and the other two features is not described, nor is it clear how it contributes uniquely to aggregation propensity within condensates.
- **Why it matters** Without a clear definition and computational protocol, the feature cannot be reproduced or independently assessed. The scientific contribution depends on the transparency and validity of the proposed metric.
- **Resolution test** In the full manuscript, provide a formal definition of binding mode entropy, the algorithm used to compute it, and a demonstration of its independence from and complementarity to the other two features, including sensitivity analyses.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scope of evidence
- **Claim pointer** The authors state that "much less is known about the physico-chemical principles that underlie aggregation within condensates" and imply that their framework addresses this gap.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract does not provide any comparative analysis with existing methods or a systematic exploration of the physico-chemical principles. It is unclear whether the three features are derived from first principles, empirical observations, or a combination, and whether they are sufficient to capture the complexity of condensate-mediated aggregation.
- **Why it matters** The claim of addressing a knowledge gap requires demonstration that the proposed framework provides new and non-redundant insight beyond existing approaches. Without comparative or mechanistic evidence, the contribution is not established.
- **Resolution test** Provide in the full manuscript a systematic analysis showing how the three features relate to known physico-chemical properties of phase-separating proteins, and a benchmark against existing aggregation prediction tools to demonstrate added value.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Terminology clarity
- **Affected element** "droplet-promoting propensity" and "aggregation-promoting propensity"
- **Evidence pointer** Abstract only; location not provided
- **Issue** These terms are used without operational definitions. It is unclear whether they refer to specific computational scores, experimental measurements, or qualitative classifications.
- **Required correction** Define each term explicitly in the full manuscript, including how they are quantified and what biophysical properties they represent.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Readability
- **Affected element** "liquid-like and solid-like condensates"
- **Evidence pointer** Abstract only; location not provided
- **Issue** The distinction between liquid-like and solid-like condensates is mentioned but not elaborated. For nonspecialist readers, the relevance of this distinction to the proposed framework is not immediately clear.
- **Required correction** Briefly explain in the introduction or discussion how the liquid-to-solid transition relates to the three features and why this transition is biologically significant.

## Risk / unsupported claims
- The claim that the three features enable prediction of aggregation-promoting mutations in ALS-associated proteins is unsupported by any quantitative or experimental evidence in the abstract.
- The assertion that the analysis "provides insights into the amino acid code" for liquid-to-solid conversion is not substantiated with specific sequence patterns or examples.
- The existence and utility of "binding mode entropy" as a predictive feature is not assessable from the abstract.
- The general statement that "much less is known" about condensation pathway aggregation is plausible but not supported by a literature comparison in the abstract.