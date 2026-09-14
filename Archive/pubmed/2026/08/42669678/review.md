## Review setup
- **Input scope** Full manuscript text (Abstract, Introduction, Results, Discussion, Methods) without supplementary figures, tables, or data files
- **Assessment boundary** Scientific validity, technical soundness, and significance of the claims as presented in the main text; experimental validation quality as described; methodological transparency
- **Shared manuscript claim summary** The authors present LLPSense, a machine learning framework that integrates ProtT5 protein language model embeddings with 13 environmental condition variables (concentration, temperature, pH, crowding agents, salts, glycerol) to predict condition-dependent protein phase separation. They report: (1) superior predictive performance over Droppler; (2) identification of SGTA as a novel phase-separating protein with reentrant temperature-dependent behavior, validated experimentally; (3) accurate prediction of α-synuclein mutations that enhance or suppress phase separation, validated experimentally; (4) successful reprogramming of UBQLN4 from LCST to UCST behavior via iterative mutation; (5) proteome-wide analysis revealing physicochemical trends consistent with established principles.
- **Visible evidence base** Main text figures (Figs. 1–6) and their legends; Methods section; Supplementary figure and table references (without actual content)
- **Missing materials affecting confidence** Supplementary figures, tables, and data files; Source Data; detailed Methods for supplementary analyses; exact dataset statistics for LLPSDB v2 curation; hyperparameter configurations; code availability statement

## Reviewer

- **Overall assessment** This manuscript addresses a genuine and important limitation in the field of protein phase separation prediction: the static, sequence-only nature of existing predictors. The authors propose a conceptually sound framework that integrates environmental conditions, which is a meaningful advance. The experimental validations, particularly the SGTA discovery and the UBQLN4 reprogramming, are compelling and demonstrate practical utility. However, the manuscript as presented has several technical concerns that need to be addressed. The most significant issues are: (1) the lack of a clear description of the training data construction from LLPSDB v2, particularly how positive and negative instances are defined and how the interval-partitioning strategy affects label integrity; (2) the absence of a rigorous comparison with Droppler under identical evaluation protocols, as the reported comparison appears to rely on previously published performance metrics; (3) the RAD23A high-salt discrepancy, while acknowledged, raises questions about the model's reliability in extrapolation; (4) the UBQLN4 reprogramming, while impressive, is based on a single protein and the mechanism of the 30 accumulated mutations is not analyzed. The writing is generally clear and accessible, though some methodological details are deferred to supplementary materials. Overall, the core idea is strong and the validations are promising, but the technical rigor of the evaluation and the transparency of the data curation need to be strengthened to fully establish the case.

- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, and intrinsically disordered proteins would be the primary audience. The framework's ability to predict condition-dependent behavior and guide mutagenesis would be of interest to those studying disease-associated mutations in proteins like α-synuclein and to synthetic biologists aiming to design programmable condensates. The methodological approach of integrating language model embeddings with environmental parameters may also appeal to the broader computational biology and machine learning community.

- **Major strengths** (1) The conceptual advance of incorporating environmental conditions into phase separation prediction is significant and addresses a clear gap in the field. (2) The experimental validation of SGTA as a novel phase-separating protein with complex reentrant behavior is a strong demonstration of the model's discovery power. (3) The bidirectional prediction of α-synuclein mutations and the experimental confirmation provide a rigorous test of the model's granularity. (4) The successful reprogramming of UBQLN4's phase behavior from LCST to UCST is a compelling proof-of-concept for the model's utility in protein design. (5) The proteome-wide analysis provides useful insights into the physicochemical determinants of phase separation.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data and label construction
- **Claim pointer** The authors claim that LLPSense is trained on a "rigorously curated, ML-ready dataset" derived from LLPSDB v2, filtered for single-protein entries, with 13 condition variables extracted and standardized.
- **Evidence pointer** Methods, "Sampling of experimental condition data"; Results, "LLPSense accurately predicts condition-dependent protein phase behavior"
- **Concern** The description of how the training dataset was constructed from LLPSDB v2 is insufficient. Specifically, it is unclear how positive and negative instances are defined. Does a "positive" instance mean a condition under which phase separation was observed, and a "negative" instance a condition under which it was not? How are entries with ranges handled in terms of label assignment? The interval-partitioning strategy is mentioned, but the details of how this affects the label (e.g., if a range is partitioned, does each sub-interval inherit the same label?) are not provided. This is a critical methodological detail that directly impacts the validity of the training data and the interpretation of the model's output.
- **Why it matters** If the labels are not clearly defined, the model's predictions are difficult to interpret. For example, a probability of 0.5 is used as a threshold for "phase separation" in screening, but it is unclear what this probability represents in terms of experimental observation. The lack of clarity on label construction undermines the reproducibility and the scientific validity of the model's outputs.
- **Resolution test** The authors should provide a detailed description of the data curation process, including a clear definition of positive and negative instances, the exact procedure for handling ranges and the interval-partitioning strategy, and the distribution of labels in the final dataset. Ideally, a data availability statement with a link to the curated dataset should be provided.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Comparative evaluation
- **Claim pointer** The authors claim that LLPSense "significantly surpasses the AUROC value reported for Droppler (0.64)" and that it outperforms Droppler retrained on their dataset.
- **Evidence pointer** Results, "LLPSense accurately predicts condition-dependent protein phase behavior"; Fig. 1f
- **Concern** The comparison with Droppler is not described with sufficient rigor. The AUROC of 0.64 for Droppler is cited from the original publication, but it is unclear if this was computed on the same evaluation protocol (e.g., same cross-validation scheme, same test set). The retrained Droppler (Droppler+ProtT5) is mentioned, but the details of its training (e.g., hyperparameters, data split) are not provided. A fair comparison requires that both models are evaluated on the same held-out test set using the same metrics and the same cross-validation procedure.
- **Why it matters** The claim of superior performance is a central pillar of the manuscript. Without a rigorous, apples-to-apples comparison, the reader cannot assess whether the improvement is due to the model architecture, the input features, or the training data. This weakens the case for LLPSense's advantage.
- **Resolution test** The authors should provide a detailed description of the evaluation protocol, including the exact data split, the cross-validation scheme, and the hyperparameters for all models compared. Ideally, they should report performance metrics (AUROC, AUPRC) for all models on the same test set, with confidence intervals.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Experimental validation scope
- **Claim pointer** The authors claim that "Multiple experimental validations confirm LLPSense's predictive power and utility," citing SGTA, α-synuclein, and UBQLN4 experiments.
- **Evidence pointer** Results, "Identification of potential phase-separating proteins...", "In silico mapping of the α-synuclein mutational landscape...", "LLPSense-guided mutations reprogram UBQLN4..."
- **Concern** While the experimental validations are a strength, the scope is limited. The SGTA validation is based on turbidity and microscopy, but the reentrant behavior is only shown for a limited set of conditions. The α-synuclein validation is based on turbidity, but the relationship between turbidity and actual phase separation (e.g., droplet formation) is not fully established for all variants. The UBQLN4 reprogramming is based on a single protein with 30 accumulated mutations, and the mechanism by which these mutations collectively invert the temperature dependence is not investigated. The authors acknowledge the RAD83A discrepancy, but this highlights the model's limitations in extrapolation.
- **Why it matters** The claims of "predictive power and utility" are strong, and the experimental evidence, while supportive, is not exhaustive. A more thorough validation, including a broader range of conditions and a mechanistic analysis of the mutations, would strengthen the case. The RAD23A discrepancy, while acknowledged, should be discussed more thoroughly in terms of its implications for the model's applicability.
- **Resolution test** The authors should provide additional experimental data, such as microscopy images for the α-synuclein variants, a more detailed analysis of the SGTA phase diagram, and a discussion of the potential mechanisms underlying the UBQLN4 reprogramming. They should also discuss the RAD23A discrepancy in the context of the model's limitations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Model interpretability and feature analysis
- **Claim pointer** The authors claim that LLPSense "reveals complex, temperature-dependent reentrant behavior" and that it can "guide sequence modifications for tuning condition-specific phase behavior."
- **Evidence pointer** Results, "Identification of potential phase-separating proteins...", "LLPSense-guided mutations reprogram UBQLN4..."
- **Concern** The manuscript does not provide any analysis of which features (sequence or environmental) are most important for the model's predictions. The authors mention SHAP analysis in the supplementary materials, but it is not described in the main text. Understanding which environmental parameters and which sequence regions drive the predictions would provide valuable biological insight and help build trust in the model's mechanisms.
- **Why it matters** A "black box" model, even with good predictive performance, is less useful for generating hypotheses about the underlying biophysics. An interpretability analysis would help the reader understand why the model makes certain predictions, such as the reentrant behavior of SGTA or the effect of specific mutations in α-synuclein.
- **Resolution test** The authors should include a section in the main text or a more detailed supplementary analysis that uses SHAP or a similar method to identify the most influential features for key predictions. This would enhance the biological interpretability of the model.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** Introduction, "Droppler represents a pioneering effort..."
- **Evidence pointer** Introduction, paragraph 3
- **Issue** The term "condition-dependent LLPS" is used throughout, but the distinction between "condition-dependent" and "sequence-dependent" is not always clear. The authors should explicitly define what they mean by "condition" (e.g., temperature, pH, concentration) and how this differs from the sequence-based features.
- **Required correction** Add a brief definition of "condition" in the Introduction and clarify how the model integrates these conditions with sequence information.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Experimental reproducibility
- **Affected element** Methods, "Turbidity assays"
- **Evidence pointer** Methods, "Turbidity assays"
- **Issue** The turbidity assay description states that "Each reported turbidity value represents the average of ten consecutive measurements taken from a single sample." This is a single technical replicate, not a biological replicate. The manuscript does not state how many independent protein preparations or experiments were performed.
- **Required correction** Clarify the number of independent biological replicates for each turbidity experiment and report the variability (e.g., standard deviation) across these replicates.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data Availability statement
- **Evidence pointer** Not explicitly stated in the main text
- **Issue** The manuscript mentions that "All curated datasets and preprocessing scripts used in this study are publicly available," but the specific repository or accession number is not provided in the main text.
- **Required correction** Provide the specific repository name and accession number or DOI for the curated dataset and code in the Data Availability statement.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Figure clarity
- **Affected element** Fig. 2c
- **Evidence pointer** Fig. 2c
- **Issue** The predicted temperature profile for SGTA is described as exhibiting "reentrant phase behavior," but the figure legend does not clearly indicate the regions corresponding to UCST and LCST behavior. The smoothed curve may obscure the underlying data points.
- **Required correction** Add annotations to Fig. 2c to clearly indicate the UCST and LCST regions, and consider overlaying the raw data points on the smoothed curve.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion
- **Evidence pointer** Discussion, paragraph 2
- **Issue** The Discussion mentions "inaccuracies under high salt concentrations in the case of RAD23A" but does not provide a detailed analysis of why this might occur or what it implies for the model's applicability to other proteins or conditions.
- **Required correction** Expand the discussion of the RAD23A discrepancy, including potential reasons (e.g., data scarcity, feature limitations) and the implications for the model's use in extrapolative predictions.

- **Technical failings that need to be addressed before the case is established** R1-M1 (data and label construction) and R1-M2 (comparative evaluation) are the most critical. Without a clear description of the training data and a rigorous comparison with existing methods, the core claims of the manuscript cannot be fully evaluated. The other concerns, while important, are less fundamental.

- **Assessment against Nature-style criteria** 
  - **Originality**: The concept of integrating environmental conditions with sequence-based language model embeddings is a novel and valuable contribution. While Droppler attempted condition-dependent prediction, LLPSense's use of ProtT5 embeddings and its demonstrated experimental validation represent a significant step forward.
  - **Scientific importance**: The ability to predict and modulate condition-dependent phase separation has broad implications for understanding disease mechanisms and for synthetic biology. The framework's potential for proteome-wide analysis is particularly valuable.
  - **Interdisciplinary readership**: The work bridges computational biology, biophysics, and cell biology. The findings would be of interest to a broad readership, but the technical details of the machine learning approach may be challenging for non-specialists.
  - **Technical soundness**: The core methodology is sound, but the lack of detail on data construction and the comparative evaluation protocol are significant gaps. The experimental validations are well-executed but limited in scope.
  - **Readability for nonspecialists**: The manuscript is generally well-written and accessible. The abstract and introduction clearly frame the problem and the approach. However, the Methods section is dense and relies heavily on supplementary materials for key details.

- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is strong and the experimental validations are promising. However, the manuscript cannot be accepted in its current form due to the lack of clarity on the training data construction and the comparative evaluation. These issues are addressable and, if resolved, would significantly strengthen the case for LLPSense's utility and validity.

## Risk / unsupported claims
- The claim that LLPSense "significantly surpasses" Droppler is not fully supported without a rigorous, same-protocol comparison.
- The claim that the model can "reliably pinpoint sequence alterations that shift α-synuclein toward LLPS-prone states" is supported by the experimental data for the selected variants, but the generalizability to all possible mutations is not established.
- The claim that LLPSense can "guide sequence modifications for tuning condition-specific phase behavior" is supported by the UBQLN4 example, but this is a single case and the mechanism is not understood.
- The proteome-wide analysis claims (e.g., trends with salt concentration) are based on model predictions, not experimental validation, and should be presented as such.
- The statement that "LLPSense accurately predicts the LCST behavior of both UBQLN1 and UBQLN4" is based on a single experimental validation for UBQLN4; the prediction for UBQLN1 is not experimentally confirmed.