## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors propose a machine learning approach using unsupervised contrastive learning with self-attention neural networks to identify functionally important residues in intrinsically disordered regions (IDRs) of proteins. The model is trained on human IDR orthologs and reportedly identifies previously reported critical residues from experimental studies, particularly those with overall patterns such as multiple aromatic residues or charged blocks, rather than short motifs.
- **Visible evidence base** Abstract text only; no quantitative results, performance metrics, validation details, or dataset descriptions are available
- **Missing materials affecting confidence** Full manuscript, all figures and tables, training and validation dataset details, model architecture specifications, hyperparameters, baseline comparisons, statistical analyses, and any supplementary information

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting application of contrastive learning to a challenging problem in IDR biology. The core idea, that physicochemical features in IDRs may be conserved despite sequence divergence and can be captured by self-supervised methods, is conceptually appealing. However, the abstract provides insufficient technical detail and quantitative evidence to evaluate the validity, robustness, or generalizability of the claimed results. The central claim that the model "successfully identifies previously reported critical residues" is not supported by any metrics, comparisons, or statistical measures in the provided material.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins and regions, particularly those interested in functional annotation of IDRs, would find this work relevant. Computational biologists developing machine learning methods for protein sequence analysis, and experimentalists seeking to prioritize residues for mutagenesis studies in IDRs, could also benefit. The potential to identify functionally important residues without requiring structural information addresses a genuine need in the field.
- **Major strengths** The conceptual framing is sound, recognizing that sequence alignment fails for IDRs and proposing an alternative based on physicochemical feature conservation. The use of unsupervised contrastive learning is appropriate for the problem, as it leverages orthologous relationships without requiring labeled data. The stated availability of training scripts, datasets, and a runnable model via Binder is commendable for reproducibility.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
  - R1-m4
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: The application of contrastive learning to IDR residue importance prediction is novel, though the underlying concept of physicochemical conservation in IDRs has precedent. Scientific importance: The problem is significant, but the abstract does not demonstrate that the method advances the field beyond existing tools. Interdisciplinary readership: The work bridges machine learning and structural biology, but the abstract lacks sufficient detail for either community to assess its value. Technical soundness: Cannot be evaluated from the abstract alone; no metrics, baselines, or validation strategies are presented. Readability for nonspecialists: The abstract is generally clear but uses terms such as "unsupervised contrastive learning" and "self-attention neuronal networks" without explanation, which may limit accessibility.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a plausible approach but lacks the quantitative and technical detail necessary to assess whether the claims are supported. A full manuscript with rigorous validation would be required to evaluate the method's utility.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The model "successfully identifies previously reported critical residues from experimental studies"
- **Evidence pointer** Abstract text; location not provided
- **Concern** The abstract provides no quantitative performance metrics, such as precision, recall, F1 score, or area under the ROC curve, to support the claim of successful identification. No comparison to existing methods or baselines is presented. The phrase "successfully identifies" is vague and could encompass a wide range of performance levels.
- **Why it matters** Without quantitative evidence, the reader cannot assess whether the model performs adequately for practical use. A method that identifies only a small fraction of known critical residues or that has a high false positive rate would not be useful. The claim as stated is unfalsifiable from the provided material.
- **Resolution test** Provide performance metrics on held-out test sets, including comparisons to appropriate baselines and existing IDR residue prediction tools. Report confidence intervals or statistical significance tests. Specify the number of experimentally validated residues used for evaluation and the criteria for defining a "successful" identification.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The model was trained using "un-supervised contrastive learning" with "self-attention neuronal networks" on "human IDR orthologs"
- **Evidence pointer** Abstract text; location not provided
- **Concern** The abstract does not describe the model architecture, training procedure, hyperparameters, or the nature of the training data. Key details such as how ortholog pairs were defined, how IDRs were identified, how negative samples were selected, and how the contrastive loss was formulated are absent. The term "un-supervised contrastive learning" is unusual, as contrastive learning typically uses some form of supervision signal, even if derived from data structure.
- **Why it matters** Reproducibility is a core requirement for computational methods. Without architectural and training details, other researchers cannot implement or evaluate the method. Moreover, the lack of clarity on the training data and loss function raises questions about what the model actually learns and whether the results are robust to different data splits or parameter choices.
- **Resolution test** Provide a complete description of the model architecture, training data construction, loss function, and hyperparameters in the full manuscript. Include ablation studies to show the contribution of each component. Make code and data available for independent verification.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability
- **Claim pointer** "This predictive model can therefore be used to identify potentially important residues in other proteins"
- **Evidence pointer** Abstract text; location not provided
- **Concern** The model is trained exclusively on human IDR orthologs. The abstract provides no evidence that the model generalizes to proteins from other species, to IDRs with different sequence properties, or to proteins with different functions. The claim of applicability to "other proteins" is therefore unsupported.
- **Why it matters** A method that only works on human proteins or on a narrow subset of IDRs would have limited utility. The abstract's broad claim of general applicability requires demonstration on diverse datasets, including cross-species validation and testing on IDRs with varying amino acid compositions and lengths.
- **Resolution test** Validate the model on IDR datasets from multiple species and on proteins with diverse functions. Report performance stratified by sequence properties such as length, composition, and predicted disorder. If cross-species performance is lower, discuss the limitations and potential domain adaptation strategies.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract text; location not provided
- **Issue** The term "un-supervised contrastive learning" is nonstandard. Contrastive learning typically uses positive and negative pairs derived from data structure, which is a form of self-supervision. The phrasing may confuse readers familiar with the machine learning literature.
- **Required correction** Use the standard term "self-supervised contrastive learning" or clarify the specific training objective in the full manuscript.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Evaluation scope
- **Evidence pointer** Abstract text; location not provided
- **Issue** The abstract states that the model identifies residues with "overall pattern" features better than "short motifs," but no examples or definitions of these categories are provided.
- **Required correction** Define what constitutes an "overall pattern" versus a "short motif" and provide specific examples of experimentally validated residues in each category, along with the model's performance for each.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Data availability
- **Evidence pointer** Abstract text; location not provided
- **Issue** The abstract states that training datasets are deposited in an OSF repository, but the specific contents, format, and any preprocessing steps are not described.
- **Required correction** Provide a detailed description of the dataset contents, including sequence identifiers, ortholog pair definitions, IDR boundaries, and any filtering criteria, in the full manuscript or repository documentation.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Biological significance
- **Evidence pointer** Abstract text; location not provided
- **Issue** The abstract does not discuss the biological interpretation of the identified residues beyond stating they are "important." It is unclear whether the model identifies residues critical for function, stability, or interactions, and how this relates to known IDR biology.
- **Required correction** Discuss the biological relevance of the identified residues in the context of known IDR functions, such as post-translational modification sites, protein-protein interaction interfaces, or phase separation behavior.

## Risk / unsupported claims
- The claim that the model "successfully identifies previously reported critical residues" is unsupported by any quantitative evidence in the abstract.
- The claim that the model "can be used to identify potentially important residues in other proteins" is unsupported by cross-species or diverse dataset validation.
- The assertion that the model captures "common IDR features" that are "preserved in maintaining function" is presented as a premise but not directly tested or demonstrated.
- The distinction between "overall pattern" and "short motif" recognition is mentioned but not defined or quantified.
- The performance of the model relative to existing methods is not assessed, so the claimed utility cannot be contextualized.