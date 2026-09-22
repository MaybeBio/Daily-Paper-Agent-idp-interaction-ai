## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the supplied abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors introduce RIBEX, a multimodal framework combining protein language model embeddings with protein–protein interaction network topology via Personalized PageRank positional encodings, FiLM conditioning, and LoRA fine-tuning, to improve RNA-binding protein prediction and interpretability across structured and IDR-rich proteins.
- **Visible evidence base** Abstract text only; no quantitative results, benchmark details, dataset descriptions, or methodological specifications beyond those named in the abstract
- **Missing materials affecting confidence** Full manuscript, all figures and tables, benchmark definitions, dataset preprocessing details, hyperparameter settings, baseline implementation details, statistical significance tests, and interpretability validation protocols

## Reviewer
- **Overall assessment** The abstract presents a plausible and potentially valuable multimodal approach to RBP prediction, with a sensible motivation grounded in the limitations of sequence-only methods. The integration of interactome topology with pLM embeddings is conceptually appealing, and the claimed improvements on challenging subsets are of interest. However, the abstract provides insufficient quantitative detail to assess the magnitude, robustness, or statistical validity of the reported gains. The interpretability claims, while ambitious, lack the methodological specificity needed to evaluate their reliability. The work is potentially significant, but the current evidence base is too thin to establish the core claims.
- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein function prediction, RNA biology researchers seeking novel RBP discovery tools, and method developers interested in multimodal integration of sequence and network features. The interpretability component may also appeal to researchers studying IDR function and RNA-binding mechanisms.
- **Major strengths** The motivation is clear and addresses a genuine gap in the field, namely the underprediction of RBPs lacking canonical domains. The multimodal design is principled, combining complementary information sources. The use of LoRA for parameter-efficient adaptation is a practical and timely choice. The focus on interpretability through multiple complementary approaches is commendable and distinguishes this work from purely predictive efforts.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
  - R1-M4
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
  - R1-m4
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: the combination of pLM embeddings with PPI topology for RBP prediction appears novel, though the abstract does not fully distinguish it from prior multimodal efforts. Scientific importance: the problem is important, and the potential to improve prediction on IDR-rich and RBD-lacking proteins addresses a real need. Interdisciplinary readership: the work bridges machine learning, network biology, and RNA biology, which could attract a broad audience if the methods are clearly presented. Technical soundness: cannot be adequately assessed from the abstract alone; the lack of quantitative results and methodological detail prevents verification. Readability for nonspecialists: the abstract is dense with technical jargon and would benefit from clearer framing of the core innovation and its biological relevance.
- **Recommendation posture** Currently not established from the provided evidence. The conceptual framework is promising, but the abstract lacks the quantitative and methodological detail required to support the performance and interpretability claims. A revised submission with full results, statistical validation, and clearer methodological exposition could change this assessment.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "PE consistently improves predictive performance" and "RIBEX outperforms state-of-the-art methods such as RBP-TSTL and HydRA"
- **Evidence pointer** Abstract, Results section; location not provided
- **Concern** The abstract reports qualitative performance improvements without any quantitative metrics, effect sizes, or statistical significance values. No AUC, precision-recall, F1, or other standard classification metrics are provided. The claim of outperforming baselines is unsupported by numerical evidence.
- **Why it matters** Without quantitative results, readers cannot evaluate whether the reported improvements are meaningful, reproducible, or statistically robust. The central claim of the paper, namely that RIBEX improves RBP prediction, cannot be verified.
- **Resolution test** Provide performance metrics (e.g., AUROC, AUPRC) with confidence intervals and statistical tests comparing RIBEX against all baselines on both benchmarks, including per-subset breakdowns for RBD-lacking and IDR-rich proteins.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological clarity
- **Claim pointer** "PE are computed using Personalized PageRank, reduced with principal component analysis, and fused with pooled sequence embeddings through FiLM conditioning"
- **Evidence pointer** Abstract, Results section; location not provided
- **Concern** The methodological description is too brief to assess the validity of the approach. Key details are missing, including the dimensionality of the PE, the number of PCA components retained, the architecture of the FiLM conditioning layers, the pooling strategy for sequence embeddings, and the specific configuration of the LoRA adaptation.
- **Why it matters** The novelty of the work rests on the specific integration strategy. Without sufficient detail, the approach cannot be reproduced, and the claimed benefits of the multimodal fusion cannot be attributed to specific design choices.
- **Resolution test** Provide a complete methods section with architectural diagrams, hyperparameter values, and ablation studies that isolate the contribution of each component (PE, FiLM, LoRA).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretability validation
- **Claim pointer** "recovering known RNA-binding domains, IDR-associated contributions, and functional interactome communities linked to RBP predictions"
- **Evidence pointer** Abstract, Results section; location not provided
- **Concern** The interpretability claims are presented without any validation metrics or comparison to ground truth. It is unclear how "recovery" was measured, whether it was quantitative or qualitative, and how the authors distinguished genuine biological signal from artifacts of the interpretability methods.
- **Why it matters** Interpretability is a major selling point of the work, but unvalidated interpretability claims can be misleading. Without rigorous evaluation, readers cannot trust that the identified domains and communities are biologically meaningful.
- **Resolution test** Provide quantitative evaluation of interpretability, such as overlap statistics between predicted and known RNA-binding domains, enrichment analyses for identified communities, and comparison against appropriate null models or alternative interpretability methods.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Benchmark validity
- **Claim pointer** "Across both an annotation-based benchmark and experimental RNA Interactome Capture (RIC) dataset"
- **Evidence pointer** Abstract, Results section; location not provided
- **Concern** The abstract does not describe the benchmarks, their sizes, class distributions, or how they were constructed. The RIC dataset is mentioned but its characteristics, preprocessing, and potential biases are not discussed.
- **Why it matters** Benchmark quality directly affects the validity of performance claims. If the benchmarks are small, imbalanced, or contain leakage between training and test sets, the reported improvements may not generalize.
- **Resolution test** Describe both datasets in detail, including construction protocols, train-test splits, and any filtering steps. Report dataset statistics and discuss potential limitations or biases.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract, Motivation section
- **Evidence pointer** Abstract, Motivation section; location not provided
- **Issue** The statement "no framework rigorously integrates both sequence information and protein interaction context for RBP prediction" is a strong claim that may be difficult to support, as prior multimodal approaches may exist in related domains.
- **Required correction** Soften the claim or provide a brief literature survey in the full text that demonstrates the absence of such frameworks.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Abstract, Results section
- **Evidence pointer** Abstract, Results section; location not provided
- **Issue** The abstract does not mention whether the code, models, or trained weights will be made publicly available.
- **Required correction** State data and code availability in the abstract or full text to support reproducibility.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scope
- **Affected element** Abstract, Results section
- **Evidence pointer** Abstract, Results section; location not provided
- **Issue** The abstract focuses on human proteins via the STRING network, but the title suggests broader applicability. It is unclear whether the method generalizes to other organisms.
- **Required correction** Clarify the scope of the method and discuss potential generalization to non-human species in the full text.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Abstract, Results section
- **Evidence pointer** Abstract, Results section; location not provided
- **Issue** The abstract uses several acronyms (PE, PCA, FiLM, LoRA, ESM2, RIC) without defining them, which may hinder readability for nonspecialist readers.
- **Required correction** Define all acronyms at first use in the abstract or provide a glossary in the full text.

## Risk / unsupported claims
- The claim that RIBEX "outperforms state-of-the-art methods" is unsupported by any quantitative data in the abstract.
- The claim that PE "consistently improves predictive performance" is unsupported without effect sizes or statistical tests.
- The interpretability claim of "recovering known RNA-binding domains, IDR-associated contributions, and functional interactome communities" is unvalidated and lacks methodological detail.
- The assertion that "no framework rigorously integrates both sequence information and protein interaction context for RBP prediction" is a strong negative claim that cannot be verified from the abstract alone.
- The generalizability of the method beyond human proteins is not addressed and cannot be assessed from the supplied material.