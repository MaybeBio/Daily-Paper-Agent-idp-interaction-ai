## Review setup

- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors propose PredLLPS_PSSM, a predictor for liquid-liquid phase separation (LLPS) protein identification based solely on sequence evolutionary information (PSSM) combined with two deep learning frameworks. They report new data collection from three databases, performance superiority over state-of-the-art methods on three existing and two newly constructed independent test datasets, validation on nine experimentally identified LLPS proteins from three insects, and interpretability analysis using SHAP and heatmaps.
- **Visible evidence base** Abstract text only; no quantitative performance metrics, dataset descriptions, model architecture details, or figures are available
- **Missing materials affecting confidence** Full manuscript, all figures and tables, dataset construction details, model hyperparameters, baseline method descriptions, statistical significance tests, and code or data availability statements

## Reviewer

- **Overall assessment** The abstract presents a potentially useful contribution to the field of LLPS protein prediction, addressing a biologically relevant problem with a sequence-based approach. However, the evidence provided in the abstract is insufficient to evaluate the technical soundness, reproducibility, or claimed superiority of the method. Key quantitative results, dataset details, and methodological specifics are absent, preventing a rigorous assessment of whether the claims are supported.
- **Who would be interested in the results, and why** Researchers in computational biology, bioinformatics, and biophysics studying biomolecular condensates and phase separation, particularly those developing or applying machine learning predictors for protein function annotation. The interpretability component may also interest biologists seeking to identify key amino acid determinants of LLPS.
- **Major strengths** The problem is biologically important and timely. The use of evolutionary information (PSSM) is well motivated for protein function prediction. The inclusion of newly collected data and validation on experimentally identified proteins from non-model organisms (insects) suggests attention to generalization. The interpretability analysis is a positive addition.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** "Independent tests using three existing independent test datasets and two newly constructed independent test datasets demonstrated the superiority of PredLLPS_PSSM compared with state-of-the-art methods."
  - **Evidence pointer** Abstract; location not provided
  - **Concern** No quantitative performance metrics (e.g., accuracy, sensitivity, specificity, Matthews correlation coefficient, area under the ROC curve) are reported. The claim of superiority is made without any numerical comparison to state-of-the-art methods.
  - **Why it matters** Without quantitative results, the reader cannot assess the magnitude of improvement, statistical significance, or whether the difference is practically meaningful. This is the central claim of the paper and is currently unsupported.
  - **Resolution test** Provide performance metrics for PredLLPS_PSSM and all compared methods on each independent test dataset, including confidence intervals or statistical tests (e.g., DeLong test for AUC differences).
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Reproducibility
  - **Claim pointer** "we collected anew and collated the LLPS proteins from the latest versions of three databases"
  - **Evidence pointer** Abstract; location not provided
  - **Concern** The abstract does not specify which three databases were used, the version numbers, the number of proteins collected, or the criteria for inclusion and exclusion. The phrase "collected anew and collated" is ambiguous regarding whether new experimental data were generated or existing database entries were reorganized.
  - **Why it matters** Dataset construction is foundational for training and evaluation. Without clear description, the results cannot be reproduced or compared with other studies, and potential biases (e.g., redundancy, homology, annotation errors) cannot be assessed.
  - **Resolution test** Describe the databases, versions, retrieval dates, filtering criteria, redundancy removal, and final dataset sizes in the full manuscript. Provide accession numbers or a data availability statement.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** "PredLLPS_PSSM combined PSSM-based information and two deep learning frameworks"
  - **Evidence pointer** Abstract; location not provided
  - **Concern** The abstract does not describe the two deep learning frameworks, how they are combined (e.g., ensemble, concatenation, attention), or the model architecture. The comparison with word embedding is mentioned but not detailed.
  - **Why it matters** The methodological novelty and technical contribution cannot be evaluated without architectural details. The choice of deep learning frameworks and their combination strategy directly affect performance and generalizability.
  - **Resolution test** Provide a full description of the model architecture, training procedure, hyperparameters, and the rationale for combining the two frameworks. Include a diagram or pseudocode.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Validation rigor
  - **Claim pointer** "we tested PredLLPS_PSSM on nine experimentally identified LLPS proteins from three insects that were not included in any of the databases"
  - **Evidence pointer** Abstract; location not provided
  - **Concern** Nine proteins is a very small sample size for external validation. The abstract does not report the prediction results for these nine proteins (e.g., how many were correctly identified) or the criteria for "experimentally identified."
  - **Why it matters** A small external test set can provide anecdotal evidence but is insufficient to establish generalizability, especially across species. The lack of reported results makes the outcome of this test unclear.
  - **Resolution test** Report the prediction outcomes for each of the nine proteins, including confidence scores, and discuss limitations of the small sample size. If possible, include additional external validation on larger independent datasets.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Title and terminology
  - **Evidence pointer** Abstract title
  - **Issue** The phrase "liquid-liquid protein separation" is imprecise. The standard term is "liquid-liquid phase separation" (LLPS). The title may confuse readers.
  - **Required correction** Revise the title to "PredLLPS_PSSM: a novel predictor for liquid-liquid phase separation protein identification based on evolutionary information and a deep neural network."
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Interpretability
  - **Affected element** SHAP analysis description
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The abstract states that SHAP and heatmaps were applied to find critical amino acids, but does not specify whether the analysis was performed on the model's predictions globally or on specific proteins, nor how the results were validated.
  - **Required correction** Clarify the scope of the interpretability analysis (e.g., global feature importance vs. per-protein explanations) and describe any validation of the identified amino acids against known LLPS-relevant motifs or experimental data.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Comparison with word embedding
  - **Evidence pointer** Abstract; location not provided
  - **Concern** The abstract mentions comparing PSSM and word embedding but does not report the outcome of this comparison. It is unclear whether PSSM was chosen because it performed better or for other reasons.
  - **Required correction** Report the comparative performance of PSSM-based and word embedding-based models, or state explicitly why PSSM was selected.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Accessibility
  - **Affected element** Data and code availability
  - **Evidence pointer** Abstract; location not provided
  - **Concern** No statement is provided regarding availability of the predictor, code, or datasets, which is important for reproducibility and community use.
  - **Required correction** Include a data and code availability statement in the full manuscript, with a link to a public repository if applicable.

## Technical failings that need to be addressed before the case is established

- R1-M1: Absence of quantitative performance metrics for the central claim of superiority
- R1-M2: Insufficient description of dataset construction and sources
- R1-M3: Lack of model architecture and combination details

## Assessment against Nature-style criteria

- **Originality** The combination of PSSM-based features with two deep learning frameworks for LLPS prediction appears potentially novel, but the abstract does not provide enough detail to distinguish it from existing methods. The interpretability component is a positive addition but not unprecedented.
- **Scientific importance** The problem of LLPS protein identification is biologically significant, particularly given the role of biomolecular condensates in cancer and cellular regulation. A reliable sequence-based predictor would be valuable. However, the importance of the specific contribution cannot be fully assessed without performance data.
- **Interdisciplinary readership** The topic bridges computational biology, biophysics, and cell biology. The abstract is written in a way that is broadly accessible, but the lack of quantitative results limits its appeal to a wide audience.
- **Technical soundness** Not assessable from the abstract. The absence of model details, dataset descriptions, and performance metrics precludes evaluation of the methodology's validity.
- **Readability for nonspecialists** The abstract is generally clear and avoids excessive jargon, though the term "liquid-liquid protein separation" in the title is imprecise. The description of methods is too vague for a specialist to evaluate and too sparse for a nonspecialist to understand the technical contribution.

## Recommendation posture

Currently not established from the provided evidence. The abstract presents a plausible and potentially useful approach, but the central claims of superiority and methodological novelty are unsupported by quantitative data or technical details. A full manuscript with performance metrics, dataset descriptions, and model architecture would be required to assess whether the case can be made. Supportive if technical concerns are resolved.

## Risk / unsupported claims

- The claim of superiority over state-of-the-art methods is unsupported without quantitative comparisons.
- The claim of successful validation on nine insect proteins is unsupported without reporting prediction outcomes.
- The claim that PSSM-based information was superior to word embedding is unsupported without comparative results.
- The generalizability of the predictor across species and protein types is not assessable from the abstract.
- The biological relevance of the identified critical amino acids is not assessable without details of the SHAP analysis and any experimental validation.