## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract, without access to full text, figures, tables, or supplemental information
- **Shared manuscript claim summary** The authors report construction of shallow, biophysically informed neural networks to predict transcriptional activation domain function from protein sequence. They claim these networks are interpretable and reveal two sequence grammar rules: (1) C-terminal hydrophobic residues increase coactivator binding and decrease protein abundance, and (2) N-terminal acidic residues promote coactivator binding while C-terminal acidic residues promote TF abundance. They further claim that combining biophysical and deep neural networks maximizes both prediction accuracy and interpretability.
- **Visible evidence base** Abstract text only. No figures, tables, methods, or supplemental materials were provided.
- **Missing materials affecting confidence** Full manuscript, all figures and tables, methods description, dataset details, model architecture specifications, quantitative performance metrics, statistical analyses, and supplemental information including the transparent peer review record.

## Reviewer
- **Overall assessment** The abstract presents a potentially valuable approach to interpretable neural network modeling of transcriptional activation domains. The central idea of embedding biophysical constraints into shallow networks to recover interpretable parameters is conceptually appealing and could address a genuine gap in the field. However, the abstract alone provides insufficient evidence to evaluate the technical soundness of the models, the robustness of the claimed sequence grammar rules, or the validity of the claim that the hybrid approach outperforms alternatives. The two mechanistic claims are stated with confidence but without quantitative support or clear indication of effect sizes, statistical significance, or validation across independent datasets. The work may be of interest to researchers studying transcriptional regulation and those developing interpretable machine learning methods for biology, but the case is not established from the supplied material.
- **Who would be interested in the results, and why** Researchers studying transcriptional regulation, particularly those focused on activation domain function and sequence grammar, would be interested in the mechanistic claims. Computational biologists developing interpretable machine learning approaches for biological sequence data would be interested in the methodological contribution. The work could also appeal to those studying intrinsically disordered regions and coactivator interactions.
- **Major strengths** The conceptual framing of combining biophysical models with neural networks to achieve both accuracy and interpretability is timely and addresses a recognized limitation of deep learning approaches. The focus on activation domains is well chosen given their biological importance and the existing deep learning predictors that lack interpretability. The explicit separation of protein abundance and coactivator binding as distinct functional axes is a useful conceptual distinction.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: The approach of embedding biophysical models into shallow neural networks for activation domain prediction appears conceptually novel, though the abstract does not fully distinguish it from prior interpretable machine learning efforts. Scientific importance: The mechanistic claims about sequence grammar are potentially important for understanding transcriptional regulation, but their significance cannot be assessed without quantitative evidence. Interdisciplinary readership: The work bridges computational biology and molecular biology, which could attract broad interest, but the abstract assumes familiarity with both domains. Technical soundness: Cannot be evaluated from the abstract alone. The absence of any quantitative performance metrics, validation details, or statistical analyses prevents assessment of whether the models perform as claimed. Readability for nonspecialists: The abstract is reasonably accessible but uses field-specific terminology without sufficient context for a general scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The conceptual approach is promising and the claims are potentially significant, but the abstract provides insufficient quantitative and methodological detail to support the conclusions. A full manuscript with detailed methods, validation, and statistical analyses would be required to assess whether the claims are supported.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that their shallow biophysical neural networks accurately predict activation domains and that combining biophysical and deep neural networks maximizes prediction accuracy and interpretability.
- **Evidence pointer** Abstract only, location not provided
- **Concern** The abstract provides no quantitative performance metrics, no comparison against existing deep learning predictors, no description of the datasets used for training and validation, and no details on how the biophysical constraints were implemented. Without these elements, the claim that the hybrid approach maximizes accuracy cannot be evaluated.
- **Why it matters** The central value proposition of the work is that the biophysical approach achieves competitive accuracy while adding interpretability. If the accuracy is substantially lower than existing deep learning methods, the trade-off may not be justified. The claim of maximizing both accuracy and interpretability requires direct quantitative comparison.
- **Resolution test** Provide performance metrics (e.g., AUC, accuracy, correlation) for the biophysical network, the deep network, and the combined approach on the same benchmark datasets, with appropriate statistical comparisons and confidence intervals.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors claim two sequence grammar rules: (1) C-terminal hydrophobic residues increase coactivator binding and decrease protein abundance, and (2) N-terminal acidic residues promote coactivator binding while C-terminal acidic residues promote TF abundance.
- **Evidence pointer** Abstract only, location not provided
- **Concern** The mechanistic claims are stated as established findings, but the abstract provides no indication of effect sizes, statistical significance, validation across independent datasets, or experimental confirmation. It is unclear whether these rules were derived from model parameters alone or validated experimentally.
- **Why it matters** These claims are the primary biological findings of the work. If they are based solely on model interpretation without experimental validation or independent dataset confirmation, they remain computational predictions rather than established mechanisms. The distinction is critical for the claims to be properly interpreted by the community.
- **Resolution test** Provide statistical measures of confidence for each claimed rule, demonstrate reproducibility across independent datasets, and indicate whether any experimental validation was performed. If experimental validation is absent, state this explicitly and frame the findings as predictions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The authors claim to have built biophysical neural networks and visualized parameters directly to reveal mechanisms.
- **Evidence pointer** Abstract only, location not provided
- **Concern** The abstract does not describe the model architecture, the biophysical model incorporated, the training procedure, or the parameter visualization approach. Without these details, the work cannot be reproduced or independently evaluated.
- **Why it matters** Reproducibility is a fundamental requirement for computational work. The specific design choices for the biophysical constraints and the network architecture are likely to substantially affect the results and the interpretability of the parameters.
- **Resolution test** Provide complete model specifications, code availability, and detailed methods in the full manuscript. Describe how the biophysical model was integrated into the network and how parameters were visualized and interpreted.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract, location not provided
- **Issue** The term "biophysical neural networks" is used without definition. It is unclear whether this refers to networks with physics-based constraints, networks whose architecture mirrors biophysical processes, or something else.
- **Required correction** Define the term explicitly in the abstract or introduction, and clarify the relationship between the biophysical model and the neural network architecture.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Scope
- **Affected element** Generalizability claim
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract states that the approach reveals mechanisms "across datasets" but does not specify which datasets or how many were used. The scope of the generalizability claim is unclear.
- **Required correction** Specify the number and nature of datasets used, and clarify whether the mechanisms were consistent across all datasets or only in a subset.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Context
- **Affected element** Related work
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract does not situate the work relative to prior interpretable machine learning approaches for biological sequences, making it difficult to assess the novelty of the contribution.
- **Required correction** Briefly describe prior interpretability approaches and explicitly state what is novel about the biophysical neural network approach relative to these prior methods.

## Risk / unsupported claims
- The claim that combining biophysical and deep neural networks maximizes prediction accuracy and interpretability is unsupported without quantitative comparisons.
- The two sequence grammar rules are stated as established findings but are unsupported without statistical measures, effect sizes, or experimental validation.
- The claim that the approach reveals mechanisms across datasets is unsupported without specification of datasets and consistency of findings.
- The general claim that the networks are interpretable is not evaluable without description of the visualization and interpretation methods.
- Any implied superiority of the approach over existing deep learning predictors is unsupported from the abstract alone.