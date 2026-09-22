## Review setup

- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors present PenLight, a deep learning framework that integrates 3D protein structures via graph neural networks with protein language model representations, and applies contrastive learning to capture functional and structural similarities beyond sequence identity. The framework is claimed to outperform state-of-the-art methods on structural classification and functional annotation tasks.
- **Visible evidence base** Abstract text only; no quantitative results, benchmark details, or methodological specifics are provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, benchmark datasets, implementation details, hyperparameters, and statistical analyses

## Reviewer

- **Overall assessment** The abstract describes a conceptually appealing approach that combines several recent advances in protein representation learning, namely graph neural networks on 3D structures, protein language models, and contrastive learning. The motivation is clear and timely given the rapid growth of predicted structures. However, the abstract provides no quantitative evidence, no benchmark specifications, and no methodological detail sufficient to evaluate the validity of the performance claims. The core assertion of superior accuracy and coverage is currently unsupported by the supplied material.
- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein function prediction, structural bioinformatics, and representation learning would be the primary audience. Researchers developing deep learning methods for protein annotations and those applying such tools to large-scale unannotated protein datasets would find the approach relevant. The integration of predicted structures with sequence-based representations addresses a practical need in the field.
- **Major strengths** The conceptual framing is strong. The authors correctly identify a gap in existing tools that predominantly rely on sequence data despite the increasing availability of high-quality predicted structures. The proposed combination of GNNs on 3D structures with protein language model embeddings is a sensible and potentially powerful design. The use of contrastive learning to capture semantic similarities beyond sequence identity is a well-motivated innovation that could improve generalization to distantly related proteins.
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
  Originality: The combination of GNNs, protein language models, and contrastive learning for protein annotations is not entirely novel in concept, as each component has been explored separately, but the specific integration may offer a new contribution. The abstract does not provide enough detail to assess the degree of novelty relative to existing methods.  
  Scientific importance: The problem of improving functional and structural annotation coverage is of high importance, and the approach addresses a timely opportunity created by AlphaFold. However, the abstract does not demonstrate the magnitude of improvement or the breadth of impact.  
  Interdisciplinary readership: The work would appeal to computational biologists, structural biologists, and machine learning researchers. The abstract is written in accessible language for these audiences, though the lack of quantitative results limits its broader appeal.  
  Technical soundness: Cannot be assessed from the abstract alone. No methodological details, evaluation protocols, or statistical analyses are provided.  
  Readability for nonspecialists: The abstract is clearly written and the motivation is understandable. Technical terms such as graph neural networks and contrastive learning are used appropriately without excessive jargon.
- **Recommendation posture** Currently not established from the provided evidence. The conceptual approach is promising, but the abstract lacks the quantitative and methodological substance required to evaluate the central performance claims. A full manuscript with detailed benchmarks and analyses would be necessary to assess whether the claims hold.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** "PenLight achieved higher prediction accuracy and coverage than state-of-the-art methods"  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The abstract states that PenLight outperforms state-of-the-art methods on a structural classification task and a functional annotation task, but provides no numerical results, no specification of which methods were compared, no dataset descriptions, and no evaluation metrics.  
- **Why it matters** The central claim of the paper is the performance advantage of PenLight. Without quantitative evidence, the claim is unverifiable and the scientific contribution cannot be assessed. The choice of baselines and benchmarks substantially affects the interpretation of any reported improvement.  
- **Resolution test** Provide in the full manuscript the specific accuracy and coverage values for PenLight and all compared methods on each task, including confidence intervals or statistical significance tests, and describe the datasets and evaluation protocols in sufficient detail for replication.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Methodological clarity  
- **Claim pointer** "PenLight uses a graph neural network (GNN) to integrate 3D protein structure data and protein language model representations" and "applies a contrastive learning strategy to train the GNN"  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The abstract does not describe how the GNN integrates structure and sequence representations, what specific protein language model is used, how the contrastive learning objective is defined, what positive and negative pairs are constructed, or how the learned representations are used for the downstream classification and annotation tasks.  
- **Why it matters** The methodological design is the core of the proposed framework. Without these details, the approach cannot be evaluated for soundness, novelty, or reproducibility. The contrastive learning strategy in particular requires careful specification to understand what similarities are being captured.  
- **Resolution test** In the full manuscript, provide a detailed description of the model architecture, the integration mechanism, the contrastive loss function, the sampling strategy for positive and negative pairs, and the downstream prediction heads. Include a diagram or pseudocode if helpful.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Generalizability and scope  
- **Claim pointer** "a general deep learning framework for protein structural and functional annotations"  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The abstract claims that PenLight is a general framework, but only two tasks are mentioned, namely structural classification and functional annotation. It is unclear whether these tasks are representative of the broader annotation space, how the framework would generalize to other annotation types, and whether the two benchmarked tasks are sufficiently diverse to support the generality claim.  
- **Why it matters** The term "general" implies broad applicability. If the framework is only demonstrated on two related tasks, the claim of generality may be overstated. The scope of the evaluation directly affects the strength of the conclusions that can be drawn.  
- **Resolution test** In the full manuscript, either demonstrate the framework on a wider range of annotation tasks or temper the generality claim to match the actual scope of the evaluation. Clearly state the range of tasks for which the framework is designed and tested.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity of motivation  
- **Affected element** Background statement  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The abstract states that "many existing computational tools still only rely on sequence data," but does not specify which tools or how recent they are. Some modern methods already incorporate structure information.  
- **Required correction** Clarify which specific existing methods are being referred to and provide a brief comparison of their approaches to position PenLight more precisely in the context of current state-of-the-art.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Terminology precision  
- **Affected element** "semantic similarities"  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The phrase "semantic similarities in the function or structure space" is vague and could be interpreted in multiple ways. It is unclear what metric or definition of semantic similarity is intended.  
- **Required correction** Define what is meant by semantic similarity in this context, for example by specifying the functional or structural annotation terms used and how similarity is measured.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Completeness of reporting  
- **Affected element** Benchmark description  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The abstract mentions "a structural classification task and a functional annotation task" but does not name the datasets, the number of proteins, the annotation ontologies, or the evaluation splits.  
- **Required correction** In the full manuscript, provide complete descriptions of the benchmark datasets, including sources, sizes, and any preprocessing steps, to enable proper evaluation of the results.

## Risk / unsupported claims

- The claim that PenLight achieves "higher prediction accuracy and coverage than state-of-the-art methods" is unsupported by any quantitative data in the supplied material.
- The claim that PenLight is a "general deep learning framework" is not substantiated by the limited task scope described in the abstract.
- The methodological description of how GNN, protein language models, and contrastive learning are combined is insufficient to assess technical soundness or reproducibility.
- The relevance and timeliness of the motivation are supported, but the specific performance advantages over existing methods cannot be evaluated from the abstract alone.