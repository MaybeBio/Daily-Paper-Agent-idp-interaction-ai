## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors introduce H-CNN, a physically motivated machine learning approach that models amino acid preferences in protein structures, predicts mutation effects on stability and binding, and offers an interpretable structure-function map for protein design
- **Visible evidence base** Abstract text only; no quantitative results, benchmarks, datasets, or comparisons are described
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, dataset descriptions, benchmark definitions, baseline comparisons, and code availability

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting idea, namely a holographic convolutional architecture for protein micro-environments, with a claim of interpretability and accurate mutation effect prediction. However, the abstract provides no quantitative evidence, no benchmark details, no comparison to existing methods, and no description of the training or evaluation protocol. As such, the core claims are currently unverifiable from the supplied material. The idea may have merit, but the case is not established at this stage.
- **Who would be interested in the results, and why** Computational biologists, protein engineers, and machine learning researchers working on structure-function relationships would be interested if the claims hold. The promise of an interpretable model that predicts stability and binding effects from structure could be useful for protein design and variant effect prediction. However, interest will depend on demonstrated performance relative to established tools such as Rosetta, DeepDDG, or EVE.
- **Major strengths** The proposed architecture is physically motivated, which is a reasonable design principle. The emphasis on interpretability is valuable and often lacking in deep learning models for proteins. The application domain, namely predicting mutation effects from structure, is of high practical relevance.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality is plausible given the holographic convolution concept, but novelty cannot be fully assessed without comparison to prior work. Scientific importance is potentially high if the method generalizes, but this is not demonstrated. Interdisciplinary readership could be broad, but the abstract lacks sufficient detail for nonspecialists to evaluate the method. Technical soundness is not assessable from the abstract alone. Readability for nonspecialists is acceptable in tone but lacks concrete context and quantitative framing.
- **Recommendation posture** Currently not established from the provided evidence. The idea is promising, but the abstract alone does not support the claims made. A full manuscript with benchmarks, baselines, and validation is required before a supportive posture can be considered.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The abstract claims that H-CNN "accurately predicts the impact of mutations on protein function, including stability and binding of protein complexes."
- **Evidence pointer** Abstract only; location not provided
- **Concern** No quantitative results are presented. There is no mention of correlation coefficients, AUC values, or any performance metric that would substantiate the word "accurately." No benchmark datasets are named, and no comparison to existing methods is described.
- **Why it matters** The central claim of the paper is predictive accuracy. Without any numerical evidence or defined evaluation protocol, the claim is unfalsifiable from the supplied material. Readers cannot judge whether the method is competitive or even functional.
- **Resolution test** Provide performance metrics on established benchmarks such as stability prediction datasets (e.g., S2648, ProTherm) and binding affinity datasets, with comparisons to at least one or two baseline methods. Report confidence intervals and statistical significance.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical reproducibility
- **Claim pointer** The abstract describes a "physically motivated machine learning approach" and an "interpretable computational model."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract does not describe the architecture, the nature of the holographic convolution, the input features, the training data, or the interpretability mechanism. A reader cannot reproduce or even understand the method from this description.
- **Why it matters** Reproducibility is a core requirement for any computational method. Without a description of the model and data, the work cannot be evaluated technically, and the claim of interpretability is unverifiable.
- **Resolution test** Include a methods section that specifies the network architecture, the physical priors encoded, the training data and preprocessing, and a concrete explanation of how interpretability is achieved and validated.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability and scope
- **Claim pointer** The abstract claims the model "recapitulates the functional information stored in evolutionary data" and "could guide design of novel proteins with desired function."
- **Evidence pointer** Abstract only; location not provided
- **Concern** No evidence is provided that the model captures evolutionary information beyond what sequence-based methods already achieve. The claim about guiding protein design is speculative and not supported by any design experiment or prospective validation.
- **Why it matters** The broader significance of the work depends on whether it offers something beyond existing sequence-based or structure-based predictors. Without evidence of generalizability across protein families or of design utility, the claims remain aspirational.
- **Resolution test** Show that the model outperforms or complements sequence-only baselines on held-out families. Include a prospective or retrospective design experiment, such as improved variant ranking or successful in silico design candidates.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "holographic" is used without definition or context. It is unclear whether this refers to a specific mathematical transform, a memory-based architecture, or a conceptual analogy.
- **Required correction** Define the term in the abstract or methods, and clarify the specific technical meaning in the context of convolutional networks.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Readability
- **Affected element** Context for nonspecialists
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract does not explain why modeling amino acid preferences in protein structures is a meaningful task, nor does it give examples of what "stability" and "binding" mean in practical terms.
- **Required correction** Add one or two sentences that frame the problem for a broad audience, such as the relevance of mutation effects in disease or engineering.

## Risk / unsupported claims
- The claim of accurate prediction of mutation effects is unsupported due to absence of quantitative results.
- The claim that the model recapitulates functional information from evolutionary data is unsupported without comparative analysis.
- The claim that the model could guide protein design is speculative and not backed by any design experiment.
- The interpretability of the model is asserted but not demonstrated or defined.
- The physical motivation of the architecture is stated but not explained in sufficient detail to be evaluated.