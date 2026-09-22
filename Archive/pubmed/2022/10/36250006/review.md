## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, technical soundness, and completeness of the review article as provided
- **Shared manuscript claim summary** The manuscript presents a review of 30 computational predictors for protein-protein interaction sites in intrinsically disordered proteins (IDP-PPIS), categorizing them into scoring functions, machine learning-based methods, and consensus approaches, and summarizing databases, features, and algorithms used in their construction.
- **Visible evidence base** Full text including abstract, introduction, sections on databases, features, algorithms, discussion, and conclusion. Tables 1 and 2 are referenced but not provided in the submitted material.
- **Missing materials affecting confidence** Tables 1 and 2 (referenced as summarizing features and predictors) are not included. Performance metrics for individual predictors are described in text but not systematically tabulated. No supplementary data or benchmark comparisons are provided.

## Reviewer
- **Overall assessment** This manuscript provides a structured narrative review of computational methods for predicting protein-protein interaction sites in intrinsically disordered proteins. The authors cover a reasonable selection of 30 predictors and organize them into three methodological categories. The text is generally readable and the discussion identifies several plausible future directions. However, the review lacks critical depth in several areas: the selection criteria for the 30 predictors are not stated, performance comparisons are reported inconsistently without standardized benchmarks, and the discussion of methodological limitations is largely qualitative. The absence of the referenced tables substantially weakens the utility of the review as a reference document. The scientific contribution is incremental relative to existing reviews in this area, and the manuscript would benefit from a more systematic and critical treatment of the field.

- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein disorder prediction, functional annotation of IDPs, and development of machine learning methods for biological sequence analysis would find this review useful as a starting point for selecting or comparing available tools. Researchers entering the field of IDP binding site prediction may benefit from the organized summary of databases, features, and algorithmic families. However, specialists in the field are unlikely to encounter substantially new information beyond what is available in the primary literature and prior reviews.

- **Major strengths** The manuscript provides a broad and organized overview of 30 predictors, which is useful for readers seeking a landscape summary. The categorization into scoring functions, machine learning, and consensus approaches is clear and intuitive. The description of feature types (amino acid composition, predicted structural features, disorder scores, physicochemical properties, evolutionary information) is reasonably comprehensive. The discussion of future directions, particularly the potential use of AlphaFold2 structures and salt bridge features, is forward-looking and relevant.

- **Major Concerns** The following concerns are detailed below.

- **Minor Comments** The following comments are detailed below.

- **Technical failings that need to be addressed before the case is established** R1-M1 (selection criteria), R1-M2 (missing tables), R1-M3 (performance comparison), R1-M4 (critical evaluation depth).

- **Assessment against Nature-style criteria**  
  *Originality*: The manuscript is a review and does not present new experimental or computational results. Its originality lies in the synthesis of existing methods, but the organizational framework is not novel and overlaps with prior reviews in the IDP prediction field.  
  *Scientific importance*: The topic is of moderate importance to the computational biology community. IDP binding site prediction is an active area, but the review does not resolve open questions or provide new insights that would substantially advance the field.  
  *Interdisciplinary readership*: The manuscript is primarily relevant to computational biologists and bioinformaticians. It is unlikely to attract broad interdisciplinary readership beyond these communities.  
  *Technical soundness*: The technical descriptions of algorithms and features are generally accurate, but the lack of systematic performance comparison and the absence of the referenced tables reduce the technical completeness. The selection of predictors is not justified, which weakens the reproducibility of the review methodology.  
  *Readability for nonspecialists*: The text is accessible to readers with a basic background in bioinformatics, but the density of method names and acronyms without a glossary may challenge nonspecialists. The abstract and introduction are clear, but the body assumes familiarity with machine learning terminology.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript has merit as a descriptive review, but the missing tables, lack of selection criteria, and inconsistent performance reporting prevent a full assessment of its contribution. Revisions addressing these issues are necessary before the case for publication is established.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodology transparency
- **Claim pointer** The manuscript states that "we collected 30 representative predictors published recently" and "we select 30 predictors of IDP-PPIS published up to January 2022."
- **Evidence pointer** Section 2, Section 2.3, Section 4
- **Concern** The criteria for selecting the 30 predictors are not stated. The authors do not specify the literature search strategy, inclusion or exclusion criteria, or how "representative" was defined. Without this information, the selection is not reproducible and the claim of representativeness is unsupported.
- **Why it matters** A review article's value depends on the comprehensiveness and transparency of its literature coverage. If the selection is arbitrary or biased, the conclusions about the state of the field may be misleading. Readers cannot assess whether important predictors were omitted or whether the sample is skewed toward certain methods.
- **Resolution test** The authors should add a subsection describing the search strategy (databases, keywords, time range), inclusion and exclusion criteria, and a flow diagram or list of initially identified versus selected predictors. The claim of representativeness should be justified with reference to the broader literature.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Completeness of evidence
- **Claim pointer** The text repeatedly refers to "Table 1" and "Table 2" as summarizing features and predictors, respectively.
- **Evidence pointer** Section 2.2, Section 2.3, Table 1, Table 2
- **Concern** Tables 1 and 2 are referenced throughout the manuscript but are not included in the provided material. These tables are central to the review's utility, as they presumably list the 30 predictors, their features, algorithms, and performance metrics. Without them, the manuscript cannot be fully evaluated.
- **Why it matters** The tables are the primary data product of this review. Their absence prevents verification of the claims made in the text, such as which predictors use which features or how performance compares. The review is incomplete as submitted.
- **Resolution test** The authors must provide the full tables with all columns described in the text. The tables should include predictor names, publication years, input features, algorithms, training/test datasets, and reported performance metrics.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Comparative rigor
- **Claim pointer** The manuscript states that certain predictors "perform better than other predictors" with specific AUC or MCC values, e.g., "MFSPSSMpred outperforms other predictors in their paper with the highest AUC of 0.758" and "OPAL + performed better than other predictors with AUC of 0.820–0.876."
- **Evidence pointer** Section 2.3.2.1, Section 2.3.2.5, Section 2.3.3
- **Concern** Performance comparisons are reported inconsistently. Metrics are cited from individual papers without standardization across datasets, evaluation protocols, or benchmark versions. The authors do not discuss whether the reported AUC or MCC values are directly comparable, and no unified benchmark is used. Statements like "performs better" are therefore not substantiated.
- **Why it matters** Readers may use these comparisons to choose among predictors. If the comparisons are not based on consistent evaluation conditions, the conclusions may be misleading. A review should either provide a standardized comparison or clearly state that cross-paper comparisons are not directly valid.
- **Resolution test** The authors should either (a) conduct a unified benchmark evaluation on a common dataset, or (b) clearly state that performance values are taken from original publications and are not directly comparable, and avoid comparative language such as "performs better" unless the original studies used identical benchmarks.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Critical depth
- **Claim pointer** The discussion states that "there might be still some limitations for current methods which can be improved from several directions" and lists data bias, feature expansion, and structure-based prediction as future directions.
- **Evidence pointer** Section 3
- **Concern** The discussion of limitations is largely qualitative and does not critically evaluate the methodological weaknesses of the reviewed predictors. For example, the issue of dataset bias is mentioned but not analyzed in terms of which predictors are affected, how bias was assessed, or what the consequences are. The discussion of AlphaFold2 is speculative and does not address potential limitations of structure-based approaches for IDPs.
- **Why it matters** A review should provide critical analysis, not just description. The current discussion reads as a list of suggestions without evidence or depth. This limits the manuscript's value as a scholarly contribution.
- **Resolution test** The authors should expand the discussion to include specific examples of methodological weaknesses, such as overfitting, limited generalizability, or evaluation flaws, and support claims about future directions with references or preliminary evidence.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.1, paragraph on DisProt
- **Evidence pointer** Section 2.1
- **Issue** The sentence "DisProt is one of the common databases for IDP-PPIS predictors, and the latest version is DisProt 9, covering more than 2000 proteins and nearly 5,000 functional annotations" is vague. It is unclear whether "common" refers to frequency of use or general availability.
- **Required correction** Rephrase to specify the role of DisProt in predictor development, e.g., "DisProt is frequently used as a source of experimentally validated IDP annotations in predictor training and evaluation."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Accuracy
- **Affected element** Section 2.3.2.5, description of SPOT-Disorder
- **Evidence pointer** Section 2.3.2.5
- **Issue** The text states "LSTM networks are a modified recurrent neural network (CNN)" which is incorrect. LSTM is a type of recurrent neural network, not a modified CNN.
- **Required correction** Correct the sentence to "LSTM networks are a type of recurrent neural network (RNN) capable of solving long time series problems."

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Section 2.3.2.1, description of MFSPSSMpred
- **Evidence pointer** Section 2.3.2.1
- **Issue** The text states "MFSPSSMpred outperforms other predictors in their paper with the highest AUC of 0.758." Later, the same AUC value of 0.758 is attributed to PSSMpred in the same section. It is unclear whether these are the same method or different methods with identical performance.
- **Required correction** Clarify the relationship between MFSPSSMpred and PSSMpred, and verify the reported AUC values.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section 2.3.2.5, equations
- **Evidence pointer** Section 2.3.2.5
- **Issue** The equations for the BRNN architecture and the SPINE-D hidden layer are presented without sufficient context or definition of all variables. For example, the notation for the activation function and the meaning of the indices are not fully explained.
- **Required correction** Add a brief explanation of the notation and the role of each equation in the prediction pipeline.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2.3.2.4, description of flDPnn
- **Evidence pointer** Section 2.3.2.4
- **Issue** The description of flDPnn is brief and does not explain how the random forest model combines features from the deep neural network. The relationship between the deep feedforward network and the random forest is unclear.
- **Required correction** Provide a more detailed description of the flDPnn architecture, including how the deep network outputs are used as inputs to the random forest.

## Risk / unsupported claims
- The claim that the 30 predictors are "representative" is unsupported without stated selection criteria.
- Performance comparisons using phrases like "performs better" or "outperforms" are not substantiated without standardized benchmarks.
- The statement that "there has been a sharp increase in protein-binding IDR predictors, with 6–10 new predictors published every 3 years" is not supported by a systematic literature count or reference.
- The claim that "salt bridges contribute to the generation of local rigid structure of IDP" is presented as a general finding but is supported only by two references without critical evaluation.
- The suggestion that AlphaFold2-based predictors "may further enhance the protein binding site prediction performance" is speculative and not supported by direct evidence in the manuscript.
- The statement that "the flanking region includes more Ala, Gly, Glu, Ser and Thr which turns to promote disorder" is presented without a reference or quantitative support.