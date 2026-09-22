## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the supplied abstract
- **Shared manuscript claim summary** The authors introduce SeqDance and ESMDance, two protein language models trained on dynamic biophysical properties derived from molecular dynamics simulations and normal mode analyses of over 64,000 proteins. They claim that SeqDance captures dynamic interactions between residues, that its embeddings support transfer learning for conformational property prediction, that predicted dynamic property changes reflect mutation effects on folding stability, and that ESMDance outperforms ESM2 in zero-shot prediction of mutation effects for designed and viral proteins lacking evolutionary information.
- **Visible evidence base** Abstract text only. No figures, tables, methods, or quantitative results are provided.
- **Missing materials affecting confidence** Full manuscript, methods description, training data details, benchmark definitions, quantitative performance metrics, comparison protocols, and statistical analyses are not available. The abstract contains no numerical results.

## Reviewer
- **Overall assessment** The abstract presents a conceptually appealing approach to integrating protein dynamics into language model training. The motivation is clear and the potential applications are broad. However, the abstract provides no quantitative evidence to support the central claims. The performance advantage of ESMDance over ESM2 is stated without any numbers, and the claim that SeqDance predictions reflect mutation effects is not substantiated. The scientific premise is interesting, but the case is not established from the supplied material.
- **Who would be interested in the results, and why** Researchers in protein engineering, computational biology, and machine learning applied to biology would be interested. Those working on mutation effect prediction, protein design, and understanding conformational ensembles would find the approach relevant. The potential to capture dynamics that static structure models miss addresses a recognized limitation in the field.
- **Major strengths** The motivation is well articulated and addresses a genuine gap in current protein language models. The use of biophysical simulation data as training signal is a sensible and potentially impactful idea. The distinction between the two models, one trained from scratch and one built on ESM2, provides a useful comparison framework. The claim that attention captures co-movement between residues is mechanistically plausible and interesting.
- **Major Concerns** The abstract contains no quantitative results. Every performance claim is qualitative. The claim that SeqDance predicted dynamic property changes reflect mutation effects is vague and lacks any metric. The comparison with ESM2 is stated as "substantially outperforms" without effect sizes, datasets, or statistical significance. The scope of the evaluation, including how many benchmarks and what types of proteins were tested, is not described.
- **Minor Comments** The abstract would benefit from stating the number of benchmarks used. The phrase "designed and viral proteins which lack evolutionary information" could be clarified regarding how this was determined. The relationship between the two models and when one should be preferred over the other is not explained.
- **Technical failings that need to be addressed before the case is established** No quantitative evidence is provided for any of the central claims. The abstract does not report any performance metrics, benchmark results, or statistical analyses. Without these, the claims of improved prediction and generalizability cannot be evaluated.
- **Assessment against Nature-style criteria** Originality is high, as the integration of dynamics-derived features into protein language model training is a novel direction. Scientific importance is potentially high, given the centrality of dynamics to protein function. Interdisciplinary readership is plausible, as the work bridges biophysics and machine learning. Technical soundness cannot be assessed from the abstract alone, as no methods or results are presented. Readability for nonspecialists is adequate, though some terms such as "normal mode analyses" and "co-movement" may require definition for a general audience.
- **Recommendation posture** Currently not established from the provided evidence. The conceptual contribution is promising, but the absence of any quantitative support means the claims cannot be evaluated. A revised abstract with concrete results would be needed to assess the case.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "ESMDance substantially outperforms ESM2 in zero-shot prediction of mutation effects for designed and viral proteins which lack evolutionary information."
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract states that ESMDance outperforms ESM2 but provides no performance metrics, benchmark names, effect sizes, or statistical significance. The term "substantially" is undefined.
- **Why it matters** This is the central comparative claim of the work. Without quantitative support, the reader cannot judge whether the improvement is meaningful or whether it generalizes beyond the specific test sets.
- **Resolution test** Provide specific benchmark datasets, performance metrics (for example correlation coefficients or AUC values), and confidence intervals or significance tests for the comparison with ESM2.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "SeqDance predicted dynamic property changes reflect mutation effect on protein folding stability."
- **Evidence pointer** Abstract, location not provided
- **Concern** This claim is stated without any supporting data. It is unclear what metric was used, how many mutations were tested, what the correlation was, or how this was validated.
- **Why it matters** This claim links the model output to a biophysical observable of broad interest. Without evidence, it is not possible to assess whether the relationship is robust or coincidental.
- **Resolution test** Report the dataset of mutations used, the correlation or classification metric between predicted dynamic changes and experimentally measured stability changes, and the statistical significance of the result.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "SeqDance, trained from scratch, has attentions that capture dynamic interaction and co-movement between residues, and its embeddings encode rich representations of protein dynamics that can be further utilized to predict conformational properties beyond the training tasks via transfer learning."
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract claims that attention captures dynamic interactions and that embeddings support transfer learning, but no evidence is provided. No examples of captured interactions, no downstream task results, and no comparison to alternative representations are given.
- **Why it matters** These claims are central to the novelty of the approach. Without demonstration, it is unclear whether the model actually learns dynamics or simply memorizes simulation outputs.
- **Resolution test** Provide qualitative or quantitative evidence that attention patterns correspond to known dynamic couplings, and report transfer learning results on at least one conformational property prediction task with comparison to baseline methods.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract text
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "designed and viral proteins which lack evolutionary information" is ambiguous. It is unclear how "lack of evolutionary information" was determined and whether this applies to all designed proteins or only some.
- **Required correction** Clarify the criterion used to define proteins lacking evolutionary information and specify the number of proteins in this category.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Scope description
- **Affected element** Abstract text
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract does not state how many benchmarks or datasets were used for evaluation, nor the diversity of protein types tested.
- **Required correction** Include the number and type of evaluation benchmarks in the abstract.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract text
- **Evidence pointer** Abstract, location not provided
- **Issue** The term "co-movement" is used without definition. It may be unclear to readers outside the biophysics community.
- **Required correction** Define the term or replace it with a more standard phrase such as "correlated motion" with a brief explanation.

## Risk / unsupported claims
- The claim that ESMDance substantially outperforms ESM2 is unsupported by any quantitative data.
- The claim that SeqDance predicted dynamic changes reflect mutation effects on stability is unsupported.
- The claim that attention captures dynamic interactions and co-movement is unsupported.
- The claim that embeddings enable transfer learning for conformational property prediction is unsupported.
- The general claim of "more generalizable predictions" is not supported by any comparative evidence.
- The claim that current models "failed to directly capture protein dynamics" is presented as fact but is a framing statement that may require nuance, though it is not a central scientific claim.