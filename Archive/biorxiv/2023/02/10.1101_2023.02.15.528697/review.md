## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, tables, or supplementary material were provided
- **Shared manuscript claim summary** The authors propose a PROMISE SCORE derived from the self-attention map of a deep Transformer protein language model to rank protein sequences by predicted interaction with a binding partner, and demonstrate its utility in nanobody discovery and protein optimization, alongside fine-tuning strategies for property prediction
- **Visible evidence base** Abstract text only; no quantitative results, experimental protocols, or validation data
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, supplementary data, benchmark definitions, and any statistical analyses

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting approach to leveraging self-attention in protein language models for sequence prioritization in protein engineering. However, the current submission provides no quantitative evidence, no methodological detail, and no validation of the claimed outcomes. The core claims regarding the effectiveness of the PROMISE SCORE in nanobody discovery and protein optimization are entirely unsupported in the provided material. The work may have merit, but the case is not established from the abstract alone.
- **Who would be interested in the results, and why** Protein engineers, computational biologists, and researchers in machine learning applied to biology would be interested if the method is validated. The potential to reduce experimental screening burden in antibody and enzyme engineering is broadly appealing. However, interest is conditional on demonstrated performance against existing methods.
- **Major strengths** The idea of using self-attention maps as a proxy for intermolecular interaction relevance is novel and potentially interpretable. The proposed dual application to both discovery and optimization is ambitious and could be impactful if supported. The discussion of fine-tuning with and without knowledge transfer suggests awareness of practical limitations.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The PROMISE SCORE provides an effective way to select lead sequences from Nb repertoires and to select site-specific mutagenesis experiments that identify a high percentage of improved sequences
  - **Evidence pointer** Abstract; location not provided
  - **Concern** No quantitative results are presented. There are no metrics such as enrichment factors, hit rates, or comparison to baseline methods. The terms "effective" and "high percentage" are undefined.
  - **Why it matters** Without quantitative validation, the central utility claim is unsubstantiated. The reader cannot assess whether the method outperforms random selection or existing scoring functions.
  - **Resolution test** Provide benchmark results with clear metrics, including comparison to established baselines, on defined datasets for both nanobody discovery and protein optimization.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Methodological clarity
  - **Claim pointer** The PROMISE SCORE weights the relative importance of a given sequence according to predicted interactions with a specified binding partner
  - **Evidence pointer** Abstract; location not provided
  - **Concern** The exact computation of the PROMISE SCORE from the self-attention map is not described. It is unclear how attention weights are aggregated, normalized, or converted into a per-sequence score.
  - **Why it matters** Reproducibility is impossible without a precise definition. The scientific contribution depends on the method being clearly specified and implementable by others.
  - **Resolution test** Provide a step-by-step mathematical definition of the PROMISE SCORE, including all equations and any hyperparameters.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Validation rigor
  - **Claim pointer** The self-attention map can indicate which regions of a protein are involved in intermolecular interactions that drive the targeted property
  - **Evidence pointer** Abstract; location not provided
  - **Concern** No evidence is shown that attention-derived regions correspond to actual binding interfaces or functional residues. Correlation with known structural or mutational data is absent.
  - **Why it matters** The interpretability claim is a key differentiator of the approach. Without validation against experimental or structural ground truth, the claim is speculative.
  - **Resolution test** Compare attention-highlighted regions to known binding interfaces in crystal structures or to alanine-scanning mutagenesis data, with quantitative overlap metrics.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Comparative assessment
  - **Claim pointer** The PROMISE SCORE provides an effective way to select lead sequences
  - **Evidence pointer** Abstract; location not provided
  - **Concern** No comparison to existing computational or experimental screening methods is mentioned. It is unclear whether the method adds value over simpler sequence-based or structure-based approaches.
  - **Why it matters** For adoption, the method must demonstrate advantage over the state of the art. Without comparison, the practical contribution is unclear.
  - **Resolution test** Include head-to-head comparisons with at least one established scoring method on the same datasets.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Terminology precision
  - **Affected element** "PROMISE SCORE"
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The term "PROMISE" is used as an acronym but its expansion is not provided.
  - **Required correction** Define the acronym at first use.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Scope clarity
  - **Affected element** "protein optimization"
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The scope of "protein optimization" is broad and could include stability, activity, or specificity. The abstract does not specify which property is optimized.
  - **Required correction** Specify the target property and the mutagenesis strategy in the abstract.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Fine-tuning discussion
  - **Affected element** "fine-tune the Transformer Protein Language Model"
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The abstract mentions fine-tuning but does not state whether the PROMISE SCORE is used before or after fine-tuning, or whether they are combined.
  - **Required correction** Clarify the relationship between the PROMISE SCORE and the fine-tuned model.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3. The absence of quantitative results, a precise method definition, and validation of interpretability claims are the primary technical failings.
- **Assessment against Nature-style criteria**  
  Originality: The concept of using self-attention for interaction-weighted scoring is novel and potentially original.  
  Scientific importance: If validated, the method could reduce experimental costs in protein engineering, which is of high importance.  
  Interdisciplinary readership: The work bridges machine learning and protein engineering, appealing to both communities.  
  Technical soundness: Not assessable from the abstract; no methodological or statistical detail is provided.  
  Readability for nonspecialists: The abstract is generally clear, though the PROMISE SCORE computation is opaque.
- **Recommendation posture** Currently not established from the provided evidence. The abstract describes a promising idea, but the claims require substantial additional evidence and methodological detail before the work can be considered for publication in a high-impact venue.

## Risk / unsupported claims
- The claim that the PROMISE SCORE is "effective" for nanobody discovery is unsupported by any data.
- The claim that the PROMISE SCORE identifies a "high percentage" of improved sequences is unsupported and undefined.
- The claim that self-attention regions indicate interaction-driving protein regions is unvalidated.
- The generalizability of the method beyond the two described contexts is not established.
- The performance of fine-tuning with and without knowledge transfer is described but not evaluated in the abstract.