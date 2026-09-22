## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the supplied abstract
- **Shared manuscript claim summary** The authors propose StructFuncNet, a hierarchical deep learning framework integrating structural interaction potentials, evolutionary information, and graph neural networks for protein-protein interaction affinity prediction. They claim state-of-the-art performance across diverse benchmarks, robustness on predicted structures, and synergistic contributions of multi-modal features via ablation studies.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or numerical results provided
- **Missing materials affecting confidence** Full manuscript, all quantitative results, benchmark descriptions, ablation details, model architecture specifications, and comparison baselines

## Reviewer
- **Overall assessment** The abstract presents a plausible and potentially valuable approach to protein-protein interaction affinity prediction, combining physical interaction potentials with deep learning. However, the claims of state-of-the-art performance and robustness cannot be evaluated from the abstract alone. The absence of any quantitative results, benchmark specifics, or methodological details prevents assessment of technical soundness and scientific contribution. The work may be of interest to the computational biology community, but the current evidence base is insufficient to establish the case.
- **Who would be interested in the results, and why** Computational biologists, bioinformaticians, and researchers in drug discovery would be interested in improved protein-protein interaction affinity prediction methods. Those working on interpretable deep learning for biological problems and on integrating physical constraints into neural networks would also find the approach relevant.
- **Major strengths** The proposed integration of structural interaction potentials with evolutionary information and graph neural networks is conceptually appealing and addresses a recognized limitation of black-box models. The stated focus on interpretability and physical realism is timely. The claimed evaluation across diverse benchmarks, including mutation affinity and intrinsically disordered proteins, suggests broad applicability if substantiated.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality cannot be fully assessed without comparison to existing methods and details of the novel components. Scientific importance is potentially high given the relevance of PPIA prediction to drug discovery, but this depends on demonstrated performance gains. Interdisciplinary readership is plausible given the intersection of machine learning and structural biology. Technical soundness is not assessable from the abstract alone. Readability for nonspecialists is adequate, though some terms such as "Structural Interaction Potentials" and "Transformer-like components" would benefit from brief clarification.
- **Recommendation posture** Currently not established from the provided evidence. The abstract describes a promising framework, but the absence of quantitative results and methodological detail precludes a supportive recommendation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim "consistently achieves state-of-the-art performance, demonstrating high correlations across all tested scenarios."
- **Evidence pointer** Abstract only; location not provided
- **Concern** No quantitative results are provided. There are no correlation coefficients, error metrics, or comparisons to existing methods. The claim of state-of-the-art performance is unsupported.
- **Why it matters** The central claim of the work is superior predictive performance. Without numerical evidence, the reader cannot verify this claim or compare it to existing benchmarks.
- **Resolution test** Provide specific performance metrics (e.g., Pearson correlation, RMSE) on each benchmark, with comparisons to at least two existing state-of-the-art methods.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological detail
- **Claim pointer** The authors claim a "novel hierarchical deep learning framework" integrating "multi-level Structural Interaction Potentials (SIP)" with "graph neural networks (GNNs)" and "Transformer-like components."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The architecture is described only at a high level. The nature of the hierarchy, the specific SIP formulations, the GNN architecture, and the Transformer-like components are not specified. The novelty cannot be assessed.
- **Why it matters** Reproducibility and assessment of technical contribution require sufficient methodological detail. The abstract does not allow the reader to understand what is genuinely new.
- **Resolution test** Provide a detailed architecture description, including equations for SIP terms, layer configurations, and a clear explanation of the hierarchical structure.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Benchmark validity
- **Claim pointer** The authors claim evaluation on "diverse and challenging benchmarks, including those for mutation affinity, multi-domain complexes, and intrinsically disordered proteins, as well as complexes derived from predicted structures."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The benchmarks are named but not described. No dataset sizes, train-test splits, or evaluation protocols are given. The claim of robustness on predicted structures is not substantiated.
- **Why it matters** Benchmark selection and protocol strongly influence reported performance. Without details, the reader cannot judge whether the evaluation is fair or comprehensive.
- **Resolution test** Describe each benchmark dataset, including source, size, and evaluation protocol. Provide results for each benchmark separately.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "Structural Interaction Potentials" is not defined. It is unclear whether this refers to physics-based energy terms, statistical potentials, or something else.
- **Required correction** Define the term explicitly in the abstract or provide a brief explanation of the types of potentials used.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Ablation studies
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states that "ablation studies confirm the synergistic contributions" but provides no details on which components were ablated or the magnitude of the effects.
- **Required correction** Summarize the key ablation results, including which components were removed and the resulting performance changes.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Data and code availability
- **Evidence pointer** Abstract; location not provided
- **Issue** No mention is made of data availability, code release, or model weights. This limits the practical utility of the work.
- **Required correction** State whether code and data will be made publicly available, and if so, where.

## Risk / unsupported claims
- The claim of "state-of-the-art performance" is unsupported by any quantitative data in the abstract.
- The claim of "robust on complexes derived from predicted structures" is unsupported without specific results.
- The claim of "synergistic contributions" from ablation studies is unverifiable without ablation details.
- The novelty of the framework cannot be assessed without comparison to existing methods and architectural specifics.
- The generalizability claim across "all tested scenarios" is not evaluable without benchmark descriptions and results.