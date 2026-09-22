## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors propose IDP-ELM, a method that uses representations from multiple protein language models and ensemble learning with bidirectional recurrent neural networks to predict intrinsically disordered regions and their functional subtypes (flexible linkers, protein binding). They report improved performance over existing methods on CAID and CAID2 test sets, with inputs limited to protein sequences, avoiding time-consuming profile generation, and provide code and weights.
- **Visible evidence base** Abstract text only; no quantitative results, dataset descriptions, baseline comparisons, or implementation details are visible
- **Missing materials affecting confidence** Full manuscript, all figures and tables, detailed methodology, exact performance numbers, baseline method definitions, statistical significance tests, and dataset composition

## Reviewer
- **Overall assessment** The abstract presents a plausible and potentially useful contribution to the field of intrinsically disordered protein prediction. The use of protein language models and ensemble learning is timely, and the claim of sequence-only input with fast prediction is attractive for proteome-scale applications. However, the abstract provides no quantitative evidence, no comparison details, and no methodological specifics that would allow an independent assessment of the stated improvements. The core claims are therefore not verifiable from the supplied material.
- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein function annotation, particularly those focused on disordered regions and their roles in signaling and protein-protein interactions. Researchers developing or applying deep learning methods for protein sequence analysis would also be interested, given the use of protein language models and ensemble strategies. The promise of fast, sequence-only prediction could appeal to those performing large-scale proteome analyses.
- **Major strengths** The problem is well motivated and of broad biological relevance. The approach is contemporary, leveraging protein language models that are currently of high interest. The stated goal of avoiding profile generation is a practical advantage over many existing tools. The provision of source code and model weights is commendable for reproducibility.
- **Major Concerns** The abstract lacks any quantitative results, making the claimed improvements unverifiable. No baseline methods are named, so the comparison context is unclear. The evaluation on CAID and CAID2 is mentioned, but the specific metrics, dataset sizes, and whether the same sequences were used across methods are not stated. The methodological description is too brief to assess novelty or technical soundness.
- **Minor Comments** The abstract would benefit from stating the number of PLMs used and their identities. The phrase "notable improvements" is vague and should be replaced with specific values. The relationship between the two test sets (CAID and CAID2) and whether they are truly independent is not clarified.
- **Technical failings that need to be addressed before the case is established** R1-M1 (no quantitative evidence), R1-M2 (unclear baseline comparison), R1-M3 (insufficient methodological detail)
- **Assessment against Nature-style criteria** Originality: The combination of multiple PLMs with ensemble learning for IDP prediction is a reasonable incremental advance, but the abstract does not demonstrate a novel conceptual contribution beyond existing PLM-based methods. Scientific importance: The topic is important, but the abstract does not show a significant advance over the state of the art. Interdisciplinary readership: The work is primarily of interest to computational biologists; the abstract does not frame the findings for a broader audience. Technical soundness: Cannot be assessed from the abstract alone; the lack of methodological detail and results is a major limitation. Readability for nonspecialists: The abstract is generally clear, but terms like "bidirectional recurrent neural networks" and "protein language models" are used without brief explanation, which may hinder nonspecialist comprehension.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim "notable improvements in terms of AUC, MCC, and F1 score" on CAID and CAID2 test sets.
- **Evidence pointer** Abstract, location not provided
- **Concern** No numerical values, confidence intervals, or statistical tests are provided for any of the stated metrics. The claim of improvement is entirely qualitative.
- **Why it matters** Without quantitative results, the reader cannot judge the magnitude or significance of the reported improvements, nor compare them to existing methods in a meaningful way.
- **Resolution test** Provide specific AUC, MCC, and F1 values for IDP-ELM and all compared baselines on both test sets, along with error bars or significance tests.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Comparison validity
- **Claim pointer** The abstract states the method was evaluated on CAID and CAID2, implying a comparison with other methods.
- **Evidence pointer** Abstract, location not provided
- **Concern** No baseline methods are named, and the evaluation protocol is not described. It is unclear whether the same training and test splits were used, whether the baselines were retrained or used as pre-trained models, and whether the comparison is fair.
- **Why it matters** A fair and transparent comparison is essential to establish that the proposed method is genuinely superior to existing approaches.
- **Resolution test** List all baseline methods, describe the evaluation protocol in detail, and confirm that identical test sets and evaluation criteria were used.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical reproducibility
- **Claim pointer** The method uses "high-dimensional representations extracted from several state-of-the-art PLMs" and "ensemble learning based on bidirectional recurrent neural networks."
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract does not specify which PLMs were used, how many, how their representations were combined, the architecture of the recurrent networks, the ensemble strategy, or the training procedure. This level of detail is insufficient for replication or for assessing technical soundness.
- **Why it matters** Reproducibility is a core requirement for computational methods. Without these details, the method cannot be independently implemented or validated.
- **Resolution test** Provide a full methodology section with model architectures, hyperparameters, training details, and a clear description of the ensemble approach.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract text
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "notable improvements" is subjective and does not convey the magnitude of the reported gains.
- **Required correction** Replace with specific numerical values for each metric.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract text
- **Evidence pointer** Abstract, location not provided
- **Issue** Terms such as "protein language models" and "bidirectional recurrent neural networks" are used without brief definitions, which may reduce accessibility for nonspecialist readers.
- **Required correction** Add a short parenthetical explanation for these terms on first use.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Abstract text
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract does not state how many PLMs were used or their identities, which is relevant for understanding the method's complexity and potential generalizability.
- **Required correction** List the specific PLMs used in the abstract or refer to a table in the full text.

## Risk / unsupported claims
- The claim of "notable improvements" in AUC, MCC, and F1 is unsupported due to the absence of any quantitative data.
- The claim that IDP-ELM is "accurate, fast, and convenient" is only partially supported; accuracy is not demonstrated, and speed is asserted without runtime comparisons.
- The claim that the method "does not entail a time-consuming process of protein profile generation" is plausible but not verified with timing data.
- The generalizability of the method to proteome-level analysis is asserted without any large-scale application or scalability evidence.