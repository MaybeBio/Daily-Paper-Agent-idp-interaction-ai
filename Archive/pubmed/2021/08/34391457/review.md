## Review setup
- **Input scope** Full manuscript text, including abstract, background, results, discussion, conclusions, methods, and figure/table captions.
- **Assessment boundary** Scientific validity, methodological soundness, reproducibility, and clarity of claims based solely on the provided material.
- **Shared manuscript claim summary** The authors propose MoRFCNN, a convolutional neural network-based method for predicting molecular recognition features (MoRFs) in intrinsically disordered proteins, using only sequence-derived structural and physicochemical properties without evolutionary information. They report superior performance over existing methods on benchmark datasets.
- **Visible evidence base** Dataset descriptions (Table 1), performance comparisons (Tables 2 and 3), ROC curve analyses (Figures 1-4), model architecture description (Figures 5 and 6), and methodological details in the Methods section.
- **Missing materials affecting confidence** No code, hyperparameter details, training/validation split specifics, statistical significance tests, or raw prediction scores are provided. Figure images are not viewable, limiting visual verification of ROC curves.

## Reviewer
- **Overall assessment** The manuscript presents a reasonable application of CNNs to MoRF prediction, with a clear methodological pipeline and competitive results on standard benchmarks. However, several technical aspects require clarification and additional validation to fully establish the claimed advantages. The work is incremental, building on prior methods (MoRFMPM, MoRFCHiBi) with modest improvements, and lacks rigorous statistical analysis to support performance claims.
- **Who would be interested in the results, and why** Researchers in computational biology, specifically those working on intrinsically disordered proteins, protein-protein interactions, and machine learning applications in bioinformatics. The method could be useful for functional annotation of disordered regions and for developing more accurate prediction tools.
- **Major strengths** 1) Use of multiple feature sets capturing complementary sequence properties. 2) Systematic evaluation of window sizes and activation functions. 3) Comparison with several established methods on widely used benchmarks. 4) Clear description of the CNN architecture and preprocessing steps.
- **Major Concerns** 
  - R1-M1: Lack of statistical significance testing for performance differences.
  - R1-M2: Insufficient detail on hyperparameter selection and model training.
  - R1-M3: Limited analysis of failure cases and generalizability.
  - R1-M4: Potential overfitting risk not adequately addressed.
- **Minor Comments** 
  - R1-m1: Typographical errors and inconsistent notation.
  - R1-m2: Figure quality and readability concerns.
  - R1-m3: Missing discussion of computational cost and scalability.
  - R1-m4: Incomplete description of feature preprocessing for the second and third feature sets.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4.
- **Assessment against Nature-style criteria** 
  - Originality: Moderate. The approach combines existing features with CNNs, which is not entirely novel but offers a new combination.
  - Scientific importance: Moderate. MoRF prediction is a relevant problem, but the incremental improvement over existing methods limits broad impact.
  - Interdisciplinary readership: Limited. Primarily relevant to bioinformatics and structural biology communities.
  - Technical soundness: Adequate but with gaps in statistical rigor and training details.
  - Readability for nonspecialists: Acceptable, though some technical jargon may hinder accessibility.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding statistical validation and training transparency.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** "MoRFCNN obtains better performance" and "MoRFCNN gets higher AUC than MoRFpred, MoRFCHiBi, MoRFCHiBi_Light and MoRFMPM on both TEST464 and TEST_EXP53 sets."
- **Evidence pointer** Tables 2 and 3, Figures 1-4
- **Concern** The performance differences are reported as point estimates without any statistical significance testing (e.g., confidence intervals, p-values, or cross-validation variance). The observed AUC improvements, particularly the small margins over MoRFCHiBi_Light and MoRFMPM, could be due to random variation.
- **Why it matters** Without statistical validation, the claimed superiority of MoRFCNN cannot be reliably established, undermining the core conclusion of the manuscript.
- **Resolution test** Provide confidence intervals or perform statistical tests (e.g., DeLong test for AUC comparison) across multiple runs or cross-validation folds to demonstrate that performance differences are significant.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** "We train three CNNs based on three feature sets respectively" and "The parameters of conv1 and conv2 are set to 2×2×1×16 and 2×2×16×8 respectively."
- **Evidence pointer** Methods section, "Prediction model" subsection
- **Concern** The manuscript lacks critical training details: learning rate, batch size, number of epochs, early stopping criteria, weight initialization, regularization techniques (e.g., dropout, L2), and the exact train/validation split within the TRAINING set. These parameters significantly affect model performance and reproducibility.
- **Why it matters** Without these details, other researchers cannot replicate the method or assess its robustness, which is essential for scientific validity.
- **Resolution test** Provide a complete description of all hyperparameters, training procedures, and the data split strategy, or make the code publicly available.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** "MoRFCNN is effective and competitive" and "MoRFCNN obtains higher AUC than ... on both TEST464 and TEST_EXP53 sets."
- **Evidence pointer** Tables 2 and 3, Discussion section
- **Concern** The evaluation is limited to two test sets derived from the same source (Disfani et al.). No analysis is provided on how the method performs on diverse protein families, different disorder-to-order transition types, or proteins with varying sequence lengths. The manuscript also does not discuss failure cases or limitations of the approach.
- **Why it matters** Without broader validation, the generalizability of MoRFCNN to real-world applications remains uncertain, and potential biases in the benchmark datasets could inflate performance estimates.
- **Resolution test** Evaluate MoRFCNN on additional independent datasets or perform subgroup analyses (e.g., by MoRF subtype, sequence length, or protein function) to demonstrate consistent performance.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Overfitting
- **Claim pointer** "The simulation results show that MoRFCNN is effective and competitive."
- **Evidence pointer** Methods section, "Prediction model" subsection, Figures 1-4
- **Concern** The manuscript does not address potential overfitting, despite the model having multiple trainable layers and the training set being relatively small (421 sequences). The use of three separate CNNs increases model complexity, and no regularization or dropout is mentioned.
- **Why it matters** Overfitting could lead to inflated performance on the test sets and poor generalization to new data, which is a common pitfall in deep learning applications with limited data.
- **Resolution test** Report training and validation loss curves, apply regularization techniques, or use cross-validation to demonstrate that the model does not overfit.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract and Background sections
- **Evidence pointer** Abstract, Background section
- **Issue** The abstract and background contain redundant statements about the importance of IDPs and MoRFs, which could be condensed. Additionally, the term "flexible 3-D structures" is imprecise; "lack of stable 3-D structures" is more accurate.
- **Required correction** Revise the abstract and background to be more concise and use precise terminology.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figures 1-4
- **Evidence pointer** Figure captions
- **Issue** The figures are described as showing ROC curves, but the captions do not specify the exact datasets or conditions for each panel. The right panels are described as "ROC curves at low FPR region," but the FPR range is not defined.
- **Required correction** Add clear axis labels, legends, and specify the FPR range for the low-FPR panels in the figure captions.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods section, "Feature selection" subsection
- **Evidence pointer** Methods section
- **Issue** The preprocessing for the second and third feature sets is not described in detail. The manuscript states they are "derived from MoRFCHiBi" but does not specify the exact features or how they are computed.
- **Required correction** Provide a detailed description of the features in the second and third sets, including their sources and preprocessing steps.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Practicality
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The manuscript does not discuss the computational cost of the method, including training time and inference speed, which is relevant for practical applications.
- **Required correction** Add a brief discussion of computational efficiency and scalability.

## Risk / unsupported claims
- The claim that "MoRFCNN obtains better performance" is not statistically substantiated due to lack of significance testing.
- The claim that "the preprocessing process enhances the performance" is not directly tested; no ablation study is provided.
- The claim that "the constructed CNN prediction model can reflect the relationship between each feature and its neighboring features" is speculative and not empirically demonstrated.
- The generalizability of the method beyond the tested datasets is unsubstantiated.
- The reproducibility of the method is limited by missing training details and code availability.