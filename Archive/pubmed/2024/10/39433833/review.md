## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion) as provided
- **Assessment boundary** Scientific validity, methodological rigor, reproducibility, and clarity of claims based solely on the provided material
- **Shared manuscript claim summary** The authors propose iDLB-Pred, a CNN-based predictor for disordered lipid-binding residues (DLBRs) in protein sequences, using feature extraction methods (PRIM, RPRIM, FV, AAPIV, RAAPIV) and statistical moments, reporting 86% accuracy in 10-fold cross-validation and 81% on an independent dataset
- **Visible evidence base** Abstract, methods sections (dataset, feature extraction, neural network descriptions), results tables (Tables 1-3), figures (Figs. 1-13), conclusion
- **Missing materials affecting confidence** Dataset composition details, feature vector dimensions, hyperparameter settings, training/validation split specifics, independent dataset source and construction, comparison with existing predictors, statistical significance tests, code or web server availability

## Reviewer
- **Overall assessment** The manuscript addresses a relevant gap in bioinformatics, namely the prediction of disordered lipid-binding residues, for which no dedicated predictor currently exists. The methodological approach is reasonable in principle, but the presentation suffers from substantial ambiguities, potential errors in the results reporting, and a lack of critical validation details. The core claims of high predictive performance cannot be fully assessed from the provided material due to missing information on dataset construction, feature engineering, and model configuration. The manuscript would require major revisions to establish the reliability and utility of the proposed method.

- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, protein-lipid interactions, and computational biology would be the primary audience. The availability of a dedicated DLBR predictor could be useful for functional annotation of disordered regions and for studying disease-associated proteins such as alpha-synuclein and tau. Additionally, developers of bioinformatics tools for protein function prediction may find the feature engineering approach of interest.

- **Major strengths**
  1. The manuscript addresses a genuine gap in the field, as no dedicated predictor for disordered lipid-binding residues currently exists.
  2. The use of multiple feature extraction techniques (compositional and positional) is a reasonable strategy to capture diverse sequence properties.
  3. The authors compare several deep learning architectures, which provides some context for the choice of CNN.
  4. The topic has potential biological and clinical relevance, particularly for neurodegenerative diseases.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Dataset construction and class definition
- **Claim pointer** The authors claim to have collected "all of the experimentally confirmed protein sequences from the Disprot database" and divided them into "ordered" and "disordered" classes for identifying DLBRs.
- **Evidence pointer** Section "Benchmark dataset", location not provided
- **Concern** The description of dataset construction is critically underspecified. The authors state that 1446 protein samples were used (723 ordered, 723 disordered), but it is unclear how these samples were selected, how the positive class (DLBRs) was defined at the residue level, and how negative residues were chosen. The statement about "eliminating positive samples from the consideration" when extracting disordered sequences is confusing and appears contradictory. Furthermore, the relationship between the 1446 protein-level samples and residue-level predictions is not explained. The mention of "telomeres" in the feature extraction section is also inconsistent with the stated focus on lipid-binding residues.
- **Why it matters** Without a clear definition of positive and negative classes at the residue level, the reported performance metrics cannot be interpreted. If the class imbalance is not addressed or if the negative set is not representative, the accuracy figures may be misleading. The ambiguity in dataset construction prevents reproducibility and undermines confidence in the reported results.
- **Resolution test** The authors must provide a detailed description of how DLBRs were annotated, how negative residues were selected, the number of positive and negative residues, and how the 1446 protein sequences relate to the residue-level dataset. A clear flowchart or data processing pipeline would be essential.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Feature extraction and model input specification
- **Claim pointer** The authors state that features are extracted using PRIM, RPRIM, FV, AAPIV, and RAAPIV, and that statistical moments reduce the PRIM matrix from 400 coefficients to 30 features.
- **Evidence pointer** Sections "Position relative incidence matrix", "Reverse position relative incidence matrix", "Frequency vector", "Accumulative absoute position incidence vector", "Reverse accumulative absolute position incidence vector - RAAPIV", location not provided
- **Concern** The feature extraction methods are described in a fragmented and inconsistent manner. The PRIM and RPRIM matrices are said to produce 400 coefficients each, reduced to 30 features via statistical moments. However, the FV produces 20 coefficients, and the AAPIV/RAAPIV descriptions are unclear, with equations that appear incomplete or mislabeled. The total feature vector dimension is never stated. The text also refers to "telomeres" and "nucleotides" in places, which is inconsistent with protein sequence analysis. The relationship between the 2D matrices and the 1D input expected by a CNN is not explained.
- **Why it matters** The feature representation is the foundation of the predictive model. If the feature vector composition is not clearly defined, the method cannot be reproduced or compared with other approaches. The apparent confusion between nucleotide and amino acid terminology raises concerns about the rigor of the methodology.
- **Resolution test** The authors must provide a clear, step-by-step description of the feature extraction pipeline, including the final feature vector dimension, how each method contributes to the vector, and how the 2D matrices are converted for CNN input. All terminology should be corrected to be consistent with protein sequence analysis.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Model architecture and training details
- **Claim pointer** The authors claim that a CNN model achieves superior performance compared to DNN, GRU, LSTM, MLP, and RNN, with 86% accuracy in cross-validation and 81% on an independent test.
- **Evidence pointer** Sections "Convolutional neural network", "Deep neural network (DNN)", "Multilayer perceptron (MLP)", "Recurrent neural network (RNN)", "Long short-term memory (LSTM)", "Gated recurrent unit (GRU)", "The proposed approach", Tables 1-3, location not provided
- **Concern** The manuscript provides only generic descriptions of each neural network architecture without any specific details about the CNN configuration used in the final model. The number of layers, kernel sizes, activation functions, pooling strategies, dropout rates, optimization algorithm, learning rate, batch size, and number of epochs are all absent. The training procedure is described only as a "constant ratio of nine to one between the training set and the validation set" during cross-validation, which is insufficient. The independent test set is mentioned but its construction is not described.
- **Why it matters** Without architectural and training details, the reported performance cannot be reproduced or independently verified. The claim that CNN is superior to other architectures cannot be properly evaluated without knowing whether all models were optimized to a comparable degree. The lack of detail also prevents assessment of whether the model is prone to overfitting.
- **Resolution test** The authors must provide a complete specification of the CNN architecture and training protocol, including all hyperparameters. The independent test set must be described in terms of its source, size, and relationship to the training data. Consideration should be given to reporting performance with confidence intervals or statistical significance tests.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Performance metric consistency and interpretation
- **Claim pointer** The abstract reports 81% accuracy on an independent dataset and 86% in 10-fold cross-validation, while the results section reports different values for the same models.
- **Evidence pointer** Abstract, Section "Comparison of different deep learning models via 10-fold CV", Tables 1-3, location not provided
- **Concern** There are inconsistencies in the reported performance values. The abstract states 86% accuracy in cross-validation, but Table 1 reports CNN accuracy as 0.866, which is consistent. However, the text in the results section states "achieved ACC of 0.866, 0.808, 0.787, 0.707, 0.814 and 0.793" for six models, but only five models are listed (CNN, DNN, GRU, LSTM, MLP, RNN would be six, but the text lists CNN, DNN, GRU, LSTM, and RNN as five, with MLP appearing in the table). The sensitivity formula in Eq. 14 appears incorrect (TP/(TP+FP) is precision, not sensitivity). The specificity formula in Eq. 15 also appears incorrect (TP/(FP+TN) is not specificity). These errors in the metric definitions undermine confidence in the reported values.
- **Why it matters** Accurate reporting of performance metrics is essential for evaluating the method. Inconsistent values and incorrect formulas suggest a lack of careful review and may indicate deeper issues with the evaluation methodology. The sensitivity and specificity values reported in Tables 1-3 cannot be interpreted correctly if the formulas are wrong.
- **Resolution test** The authors must correct the metric formulas, ensure consistency between the abstract, results text, and tables, and provide a clear explanation of how each metric was computed. All reported values should be cross-checked for consistency.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Comparison with existing methods and practical utility
- **Claim pointer** The authors state that "there are no methods that consider for the linkage with lipids" and imply that iDLB-Pred fills this gap.
- **Evidence pointer** Introduction, Section "Comparison of different deep learning models via 10-fold CV", location not provided
- **Concern** While the authors correctly note the lack of dedicated DLBR predictors, they do not compare iDLB-Pred with general disordered region predictors or with predictors for other types of binding residues (e.g., DNA-binding, RNA-binding, protein-binding). Such comparisons would help contextualize the performance of the proposed method. Additionally, the practical utility of the predictor is not demonstrated through case studies or biological validation. The conclusion mentions alpha-synuclein and tau but does not show whether iDLB-Pred correctly identifies known lipid-binding regions in these proteins.
- **Why it matters** For a new predictor to be useful, it must demonstrate added value over existing tools. Without comparative analysis or biological validation, the practical significance of iDLB-Pred remains unclear. The claim of novelty is weakened by the lack of benchmarking against related methods.
- **Resolution test** The authors should include comparisons with existing predictors for disordered binding residues and provide case studies on well-characterized proteins with known lipid-binding regions. This would strengthen the case for the method's utility.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figures
- **Affected element** Figures 1-13
- **Evidence pointer** Figures 1-13, location not provided
- **Issue** The figures are referenced but not described in sufficient detail in the text. Figure 1 (architecture) and Figures 2-7 (network structures) are not explained in the text, and Figures 8-13 (performance comparisons) are only briefly mentioned.
- **Required correction** The authors should provide clear descriptions of each figure in the text, explaining what is shown and how it supports the results.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Abstract, Introduction, Methods
- **Evidence pointer** Throughout the manuscript, location not provided
- **Issue** The manuscript uses inconsistent terminology, including "telomeres" in the feature extraction section, "nucleotides" in the statistical moments section, and "disordered lipid-binding residues" versus "disordered proteins" in the conclusion. These inconsistencies suggest a lack of careful editing.
- **Required correction** The authors should carefully revise the manuscript to ensure consistent and accurate terminology throughout, particularly distinguishing between nucleotide and amino acid sequences.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Availability of resources
- **Affected element** Methods, Conclusion
- **Evidence pointer** Section "The proposed approach", location not provided
- **Issue** No information is provided about the availability of the model, code, or a web server for the predictor. This limits the practical utility of the method for the research community.
- **Required correction** The authors should provide information about code availability, a web server, or at least a detailed description of the model that would allow others to implement it.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reference quality
- **Affected element** Introduction, Methods
- **Evidence pointer** Throughout the manuscript, location not provided
- **Issue** Several references are cited in a generic manner (e.g., "Akmal et al. 27") without clear context. The reference list is not provided in the submitted material, making it impossible to verify the appropriateness of citations.
- **Required correction** The authors should ensure that all references are appropriately cited and that the reference list is complete and accurate.

## Risk / unsupported claims
1. The claim that iDLB-Pred achieves 86% accuracy in cross-validation and 81% on an independent dataset cannot be fully assessed due to missing details on dataset construction, class balance, and evaluation methodology.
2. The claim that the proposed feature extraction methods capture "both compositional and positional information" is not supported by a clear description of the feature vector composition or its dimensionality.
3. The statement that "there are no methods that consider for the linkage with lipids" is presented as fact but is not supported by a comprehensive literature review.
4. The conclusion that the method "represents a novel application of bioinformatics to IDPs" is overstated given the lack of comparison with existing methods.
5. The biological relevance of the predictions is not demonstrated through case studies or experimental validation, making claims about utility for biologists unsupported.
6. The performance comparison across different deep learning models is presented without statistical significance testing, making it unclear whether observed differences are meaningful.