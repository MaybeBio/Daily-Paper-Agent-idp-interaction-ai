## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and figure legends
- **Assessment boundary** Scientific validity, methodological soundness, claims versus evidence, and alignment with Nature-style criteria
- **Shared manuscript claim summary** The authors develop a machine learning approach to predict protein localisation into heteromolecular condensates, identify biophysical drivers distinct from homotypic phase separation, and construct a Protein Condensate Atlas by integrating predicted condensation propensity with interaction networks, validated against known condensate compositions.
- **Visible evidence base** Main text figures 1-6, supplementary datasets referenced (1-11), methods section, and supplementary figures S1-S5
- **Missing materials affecting confidence** Supplementary datasets 1-11 not provided; supplementary figures S1-S5 not provided; source data files not provided; code availability not stated; detailed hyperparameter tuning results not shown

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting approach to predicting condensate composition, with a potentially useful resource in the Protein Condensate Atlas. The finding that heteromolecular condensate localisation is driven by different biophysical features than homotypic phase separation is noteworthy. However, several methodological details and validation steps require clarification and strengthening before the claims are fully supported. The reliance on a single experimental dataset for training, the indirect validation approach, and the lack of quantitative benchmarking against existing methods limit the current impact.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, and cellular organisation would be the primary audience. Computational biologists developing predictive models for protein localisation would also find the methodology relevant. The Atlas itself could serve as a resource for experimental biologists seeking candidate condensate components. The work may also interest those studying nucleolar biology and RNA-binding protein function.
- **Major strengths** The study addresses an important gap by moving beyond single-protein phase separation prediction to composition prediction. The analysis of biophysical drivers is systematic and includes appropriate controls. The validation using independent immunohistochemical data provides some orthogonal support. The Atlas construction is a novel contribution that could generate testable hypotheses.
- **Major Concerns** 
  - R1-M1: Training data derived from a single condensate system (NPM1) reconstituted in vitro, raising questions about generalisability to native cellular condensates.
  - R1-M2: The validation of top-ranked predictions relies on visual inspection of immunohistochemistry images, which is subjective and lacks quantitative criteria.
  - R1-M3: The Atlas construction uses interaction data from STRING, which is not condensate-specific and may introduce bias toward well-studied proteins.
  - R1-M4: The claim that the model extends beyond NPM1-condensates is supported by enrichment analysis, but the statistical framework for determining significance is not fully described.
  - R1-M5: The comparison between COND+ and COND- datasets may be confounded by expression level filtering and the arbitrary threshold of 3.5 log10 units.
- **Minor Comments** 
  - R1-m1: Figure 2a presents expression level differences but the text does not fully address whether this reflects biological partitioning or detection bias.
  - R1-m2: The choice of 0.75 for DeePhase and 0.25 for partitioning score thresholds requires justification beyond the Youden J-statistic.
  - R1-m3: The manuscript would benefit from a clearer statement of limitations regarding the use of STRING interaction data.
  - R1-m4: The term "heteromolecular condensate" is used throughout but not explicitly defined in the introduction.
  - R1-m5: The methods section on clustering states n=50 cluster centres but the rationale for this number is not provided.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** 
  - Originality: The approach of predicting condensate composition rather than individual propensity is a novel angle, though it builds on existing machine learning methods for phase separation prediction.
  - Scientific importance: The potential to predict condensate composition genome-wide is significant, but the current evidence does not fully establish the reliability of these predictions.
  - Interdisciplinary readership: The work bridges computational biology, biophysics, and cell biology, which could attract broad interest if the methodology is made accessible.
  - Technical soundness: The machine learning pipeline is reasonable, but the training data limitations and validation approach weaken the technical case.
  - Readability for nonspecialists: The manuscript is generally well-written, but some methodological details in the results section assume familiarity with machine learning and biophysical concepts.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding training data generalisability, quantitative validation, and statistical rigour of the enrichment analysis.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data representativeness and generalisability
- **Claim pointer** The authors claim the model predicts protein localisation into heteromolecular condensates broadly, and that the predictive capability extends beyond NPM1-condensates.
- **Evidence pointer** Results section "NPM1-condensate composition is determined by both protein-RNA and protein-protein interactions"; Figure 2; Methods "Preparation of datasets"
- **Concern** The model is trained exclusively on data from reconstituted NPM1-condensates in lysate. This is a single, in vitro system that may not represent the diversity of cellular condensates. The authors attempt to address generalisability by testing on G3BP1 condensates and other systems, but the training data remains narrow. The claim of generalisability requires demonstration that the learned features are not specific to NPM1-condensate biology.
- **Why it matters** If the model is overfit to NPM1-condensate characteristics, the Atlas predictions for other condensate types could be systematically biased, undermining the central resource claim.
- **Resolution test** The authors should either train on multiple condensate datasets from different systems, or provide a more rigorous cross-system validation showing that model performance is consistent across diverse condensate types with different protein compositions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation rigour
- **Claim pointer** The authors claim that top-ranked predictions were confirmed to localise into condensates by orthogonal immunohistochemical staining imaging.
- **Evidence pointer** Results section "Machine learning models can predict protein partitioning and identify additional components of condensates"; Figure 4d; Supplementary Dataset 7
- **Concern** The validation relies on visual inspection of immunohistochemistry images, with the authors noting that four out of ten top targets showed clear condensates and a few additional showed less well-defined condensates. This is a subjective assessment without quantitative criteria, blinding, or statistical comparison to a control set of low-scoring proteins. The lack of a formal scoring rubric or inter-rater reliability assessment weakens the strength of this validation.
- **Why it matters** The claim that the model identifies true positives beyond training data is central to demonstrating utility. Subjective visual assessment is insufficient to establish this, particularly given the potential for confirmation bias.
- **Resolution test** Provide a quantitative validation framework, such as blinded scoring by multiple independent assessors, comparison of high-scoring versus low-scoring proteins with defined statistical thresholds, or use of automated image analysis to quantify condensate formation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Atlas construction methodology
- **Claim pointer** The authors claim the Atlas predicts the composition of heteromolecular condensates by combining condensation propensity with interaction profiles.
- **Evidence pointer** Results section "Predictive capability extends beyond NPM1-condensates and permits the construction of Protein Condensate Atlas"; Figure 5; Methods "Construction of the Protein Condensate Atlas"
- **Concern** The Atlas is built using STRING interaction data, which aggregates information from multiple sources including co-expression, experimental, and text-mining evidence. This data is not condensate-specific and may be biased toward well-studied proteins. The clustering approach uses k-means with n=50 centres, but the stability and biological meaning of these clusters are not thoroughly assessed. The manuscript does not report how many proteins were included in the clustering, the cluster size distribution, or whether the clusters are robust to parameter choices.
- **Why it matters** The Atlas is a key deliverable of the paper. If the underlying interaction data introduces systematic biases, the Atlas composition predictions could be misleading for less-studied proteins or condensate types.
- **Resolution test** Provide sensitivity analyses showing cluster stability across different parameter choices, assess whether results are robust to using alternative interaction databases, and report the coverage and potential biases of the STRING data for the proteins analysed.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigour of enrichment analysis
- **Claim pointer** The authors claim that the Atlas clusters show significant enrichment for known condensate components, validating the approach.
- **Evidence pointer** Results section "Evaluating the predictions of the Protein Condensate Atlas"; Figure 6; Methods "Evaluation of the predictions of the Protein Condensate Atlas"
- **Concern** The enrichment analysis compares observed overlap between predicted clusters and known condensate components to expected overlap under random allocation. However, the manuscript does not describe how statistical significance is determined, whether multiple testing corrections are applied across the many cluster-condensate pairs, or how the null distribution is generated. The enrichment values shown in Figure 6b appear to lack confidence intervals or significance thresholds.
- **Why it matters** Without a clear statistical framework, the enrichment values cannot be interpreted as evidence of predictive validity. High enrichment values could arise by chance given the number of comparisons made.
- **Resolution test** Describe the statistical test used, report p-values or confidence intervals for enrichment values, apply appropriate multiple testing corrections, and show that the observed enrichment is unlikely under a well-defined null model.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Interpretation of expression level differences
- **Affected element** Figure 2a-c
- **Evidence pointer** Results section "High homotypic phase separation propensity is not a prerequisite for protein localisation into NPM1-condensates"; Figure 2a-c
- **Issue** The authors note that proteins in condensates had tenfold higher expression levels, but the interpretation of this finding is ambiguous. It could reflect biological partitioning (concentration-dependent) or detection bias in mass spectrometry.
- **Required correction** Clarify whether the expression level difference is considered a biological finding or a technical artifact, and discuss the implications for the COND+ and COND- dataset construction.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Threshold justification
- **Affected element** Atlas construction thresholds
- **Evidence pointer** Results section "Predictive capability extends beyond NPM1-condensates and permits the construction of Protein Condensate Atlas"; Methods "Construction of the Protein Condensate Atlas"
- **Issue** The thresholds for defining the condensate-localising proteome (DeePhase score above 0.75 or partitioning score above 0.25) are stated but not justified beyond the Youden J-statistic. The sensitivity of the Atlas to these thresholds is not explored.
- **Required correction** Provide a brief justification for the chosen thresholds and ideally show that the main conclusions are robust to reasonable variations in these values.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Limitations of interaction data
- **Affected element** Atlas construction
- **Evidence pointer** Methods "Construction of the Protein Condensate Atlas"
- **Issue** The manuscript does not explicitly discuss the limitations of using STRING interaction data, which includes text-mining and predicted interactions that may not reflect physical interactions in condensates.
- **Required correction** Add a sentence in the discussion acknowledging this limitation and its potential impact on Atlas predictions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Definition of key term
- **Affected element** Introduction
- **Evidence pointer** Introduction, first paragraph
- **Issue** The term "heteromolecular condensate" is used throughout but not explicitly defined. It is implied to mean condensates with diverse protein and RNA composition, but a formal definition would help readers.
- **Required correction** Provide a brief definition of "heteromolecular condensate" in the introduction to clarify the scope of the study.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Clustering procedure
- **Evidence pointer** Methods "Construction of the Protein Condensate Atlas"
- **Issue** The clustering procedure is described briefly. The choice of n=50 clusters is not justified, and the stability of the clustering across runs is only addressed by running twice with different seeds.
- **Required correction** Provide additional detail on how the number of clusters was selected and assess cluster stability more thoroughly, such as using consensus clustering or bootstrap approaches.

## Risk / unsupported claims
- The claim that the model "can predict protein partitioning" across the proteome is not fully supported given the training data limitation to a single condensate system.
- The claim that the Atlas "can be valuable for discovering previously uncharacterised condensates" is speculative, as the validation only demonstrates enrichment for known condensate components.
- The statement that "the predictive capability extended beyond the NPM1-condensate system" is based on enrichment analysis that lacks a clear statistical framework.
- The claim that "charge mediated protein-RNA and hydrophobicity mediated protein-protein interactions play a key role" is supported by the data, but the relative importance of these factors is not quantified.
- The assertion that the model identifies "additional components of condensates" is based on visual inspection of a small number of examples and requires more rigorous validation.