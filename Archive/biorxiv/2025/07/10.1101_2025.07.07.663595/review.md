## Review setup
- **Input scope** Full manuscript text (Abstract, Introduction, Results, Discussion, Methods, Data/Code availability, Author contributions, Acknowledgements, Footnotes)
- **Assessment boundary** Scientific claims, methodological soundness, and evidence quality as presented in the provided text. No supplementary figures, tables, or data files were available for inspection.
- **Shared manuscript claim summary** The authors introduce PPLM, a protein–protein language model pretrained on paired sequences with a hybrid intra-/inter-protein attention mechanism. They report state-of-the-art performance across three downstream tasks: binary PPI prediction (PPLM-PPI), binding affinity prediction (PPLM-Affinity), and inter-protein contact prediction (PPLM-Contact and PPLM-Contact2), with the latter also outperforming structure-based methods including AlphaFold2.3, AlphaFold3, and DMFold.
- **Visible evidence base** Main-text figures referenced (Figures 1–6), supplementary tables and figures referenced but not provided, and methodological descriptions in the Methods section.
- **Missing materials affecting confidence** All supplementary materials (Tables S1–S22, Figures S1–S16, Texts S1–S8, Data S1–S7), benchmark datasets, training details, and hyperparameter settings. The absence of these materials prevents independent verification of the reported results and statistical analyses.

## Reviewer

- **Overall assessment** The manuscript presents a timely and potentially impactful contribution to computational PPI modeling. The core idea of pretraining a language model on paired sequences with a dedicated inter-protein attention mechanism is conceptually sound and addresses a genuine limitation of single-sequence protein language models. The reported performance gains across three distinct tasks are impressive, particularly the claim that PPLM-Contact2 outperforms AlphaFold2.3, AlphaFold3, and DMFold on inter-protein contact prediction. However, the manuscript as provided has several critical gaps that prevent full assessment. The most significant concerns are the lack of accessible supplementary data, the absence of key methodological details (e.g., exact training data composition, hyperparameters, and the nature of the "custom clustering procedure"), and the need for clearer descriptions of the evaluation protocols, especially for the affinity and contact prediction tasks. The claim of outperforming AlphaFold3, a state-of-the-art structure prediction model, is extraordinary and requires particularly rigorous scrutiny. The manuscript would be substantially strengthened by making the supplementary materials available and by providing more detailed descriptions of the experimental setups.

- **Who would be interested in the results, and why** Computational biologists, bioinformaticians, and researchers in protein engineering and structural biology would be the primary audience. The work is directly relevant to those developing or using machine learning methods for PPI prediction, drug discovery, and antibody/TCR engineering. The potential for a sequence-only method to compete with structure-based approaches in contact prediction would be of broad interest to the protein modeling community.

- **Major strengths**
  1. The conceptual novelty of a paired-sequence language model with a hybrid attention mechanism is a clear strength, directly addressing a known limitation of single-chain PLMs.
  2. The scope of the work is broad, covering three major PPI-related tasks, which demonstrates the versatility of the proposed approach.
  3. The reported performance improvements are substantial and consistent across tasks, and the inclusion of challenging subsets (antibody–antigen, TCR–pMHC) adds practical relevance.
  4. The authors have made efforts to address data leakage concerns (e.g., structure-level clustering for affinity, similarity-stratified PPI evaluation), which is commendable.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality and reproducibility
- **Claim pointer** The claim that PPLM-Contact2 outperforms AlphaFold2.3, AlphaFold3, and DMFold on inter-protein contact prediction across 434 homodimers and 119 heterodimers.
- **Evidence pointer** Figure 5C–D, Supplementary Tables S14–S15, Supplementary Data 3–4 (not provided)
- **Concern** The manuscript reports that PPLM-Contact2, which integrates inter-protein distance maps from AlphaFold2.3-predicted complex structures, achieves top L precision of 85.1% on homodimers and 88.0% on heterodimers, surpassing AlphaFold2.3, AlphaFold3, and DMFold. This is a strong claim that challenges the capabilities of dedicated structure prediction models. However, the evaluation protocol is not described in sufficient detail. Specifically, it is unclear how the "top L" contacts are defined for the structure-based methods (e.g., are they derived from the predicted structure's distance matrix?), how the comparison is made fair given that PPLM-Contact2 uses AlphaFold2.3 predictions as input, and whether the same train/test split is used for all methods. The lack of access to the supplementary tables and data prevents verification of the statistical significance and the per-target breakdown.
- **Why it matters** The claim of outperforming AlphaFold3 is extraordinary and, if true, would be a significant finding. However, without a clear and fair evaluation protocol, the claim cannot be assessed. The potential for circularity (using AlphaFold2.3 predictions to train or inform a model that is then compared against AlphaFold2.3) is a serious concern that must be addressed.
- **Resolution test** Provide a detailed description of the evaluation protocol, including how contacts are defined for each method, how the comparison is made fair, and the exact train/test splits. Make the per-target results in Supplementary Data 3–4 available for inspection. Clarify whether any of the methods being compared were used to generate features for PPLM-Contact2 and how this potential circularity is avoided.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological clarity and reproducibility
- **Claim pointer** The description of the PPLM training dataset, which is claimed to comprise over 3.3 million high-quality protein pairs from PDB and STRING.
- **Evidence pointer** Methods, Datasets section
- **Concern** The dataset construction is described as integrating PDB complexes and STRING interactions, followed by "filtering for physical interfaces and removing redundancy through pair-level clustering using MMseqs2 together with a custom clustering procedure." The details of this "custom clustering procedure" are not provided. Furthermore, the criteria for "high-quality" pairs are not defined. The ratio of PDB to STRING pairs in the final training set is not stated, nor is the number of clusters from each source. The validation set selection is described, but the exact procedure for "removing validation pairs that were redundant to any pairs in the training clusters" is not specified.
- **Why it matters** The quality and composition of the training data are fundamental to the performance of any machine learning model. Without a clear description of the filtering and clustering procedures, the reproducibility of the work is compromised, and it is impossible to assess potential biases in the training data that could affect the reported results.
- **Resolution test** Provide a detailed description of the "custom clustering procedure," including any parameters and thresholds. Define the criteria for "high-quality" pairs. Report the number of clusters and pairs from each source (PDB, STRING) and the final training set composition. Specify the exact redundancy removal procedure for the validation set.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Evidence quality and statistical rigor
- **Claim pointer** The claim that PPLM-Affinity outperforms ESM2-Affinity and the structure-based PPB-Affinity model on binding affinity prediction, with particularly large gains on antibody–antigen and TCR–pMHC subsets.
- **Evidence pointer** Figure 3D–F, Supplementary Tables S7–S9 (not provided)
- **Concern** The reported improvements on the antibody–antigen and TCR–pMHC subsets are very large (e.g., 117.1% and 144.0% improvements in PCC over ESM2-Affinity). While this is promising, the manuscript does not report the number of samples in these subsets, nor does it provide confidence intervals or error bars for the PCC/SRCC values. The statistical comparison in Supplementary Tables S7–S9 is not visible. The choice of PCC and SRCC as the primary metrics is reasonable, but the lack of uncertainty quantification is a concern, especially for small subsets.
- **Why it matters** The strong performance on immunologically relevant complexes is a key selling point of the paper. However, without measures of uncertainty or sample sizes, it is difficult to judge the reliability of these estimates. The gains could be driven by a few outliers or by a small number of samples.
- **Resolution test** Report the number of samples in each subset and provide confidence intervals or bootstrap estimates for the PCC and SRCC values. Make the per-sample predictions and the statistical comparison tables available.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness and comparison fairness
- **Claim pointer** The claim that PPLM-Contact surpasses existing contact predictors, including those "deduced from cutting-edge complex structure predictions."
- **Evidence pointer** Figure 4A–B, Supplementary Tables S10–S13 (not provided)
- **Concern** The comparison of PPLM-Contact against structure-based methods like AlphaFold2.3, AlphaFold3, and DMFold is a central part of the paper's impact. However, the manuscript does not describe how these structure-based methods are used to generate contact predictions. For example, are contacts defined as residues within a certain distance in the predicted structure? What is the threshold? Are the same thresholds used for all methods? The manuscript also does not clarify whether the structure-based methods are given the same input information (e.g., sequences only) or if they are allowed to use their full pipeline (e.g., MSA search, template identification). This lack of detail makes it difficult to assess the fairness of the comparison.
- **Why it matters** The claim of outperforming AlphaFold3 is a major one. If the comparison is not fair or the protocol is not clearly defined, the claim is weakened. The reader needs to understand exactly what is being compared to evaluate the significance of the results.
- **Resolution test** Provide a detailed description of how contact predictions are derived from each method, including any distance thresholds. Clarify the input information available to each method. Describe the evaluation metrics and the statistical tests used.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and presentation
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, Introduction
- **Issue** The abstract states that PPLM-PPI achieves "state-of-the-art performance across different species," but the specific species and the magnitude of improvement are not mentioned. The Introduction could also benefit from a more explicit statement of the limitations of existing methods in the context of the three tasks.
- **Required correction** Briefly mention the number of species and the range of improvement in the abstract. In the Introduction, explicitly state the performance gap of existing methods for each of the three tasks to better motivate the work.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological clarity
- **Affected element** Methods, Protein–protein language model
- **Evidence pointer** Methods section
- **Issue** The description of the hybrid attention mechanism is somewhat brief. The equations for the attention mechanism are mentioned but not fully defined in the provided text. The role of the learnable weights (W_lh) and the binary mask (M_ij) is described, but the exact formulation of the final attention matrix is not fully clear.
- **Required correction** Provide the full equations for the attention mechanism, including the definitions of all variables and the exact way the intra- and inter-protein attention matrices are combined.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of reporting
- **Affected element** Results, PPLM improves language modeling of protein pairs
- **Evidence pointer** Figure 2A–C
- **Concern** The perplexity analysis is a key validation of the pretraining approach. However, the manuscript does not report the perplexity of ESM2 on the same masked positions when it is given the concatenated sequence as input. This would be a more direct comparison of the paired vs. single-sequence modeling capability.
- **Required correction** Add a comparison where ESM2 is evaluated on the same masked positions in the concatenated sequence, to isolate the effect of the paired training and attention mechanism.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results, PPLM-PPI outperforms existing methods
- **Evidence pointer** Figure 3A–C, Supplementary Tables S1–S3
- **Concern** The manuscript reports mean ± standard deviation for the overall performance, but the variability across the five species is not discussed. The large standard deviation for some species (e.g., 0.5745 for C. elegans) suggests that performance is not uniform.
- **Required correction** Discuss the variability in performance across species and provide a breakdown of the results for each species in the main text or a supplementary table.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity of claims
- **Affected element** Results, PPLM-Contact enhances interface residue recognition
- **Evidence pointer** Figure 6A–B
- **Issue** The definition of "interface residues" is provided, but the metric used for evaluation (precision at top N) is not clearly defined in the main text. It is stated that N equals the number of ground-truth interface residues, but it is not clear if this is the same for all methods and how ties are handled.
- **Required correction** Provide a clear definition of the evaluation metric and the protocol for selecting the top N residues.

- **Technical failings that need to be addressed before the case is established**
  1. The evaluation protocol for comparing PPLM-Contact2 against AlphaFold2.3, AlphaFold3, and DMFold is not described in sufficient detail, raising concerns about fairness and potential circularity (R1-M1).
  2. The training dataset construction is not fully specified, particularly the "custom clustering procedure" and the criteria for "high-quality" pairs, which compromises reproducibility (R1-M2).
  3. The statistical rigor of the affinity prediction results, especially for the small antibody–antigen and TCR–pMHC subsets, is insufficient without confidence intervals or sample sizes (R1-M3).
  4. The comparison of PPLM-Contact against structure-based methods lacks a clear description of how contacts are derived from each method, making it difficult to assess the validity of the claims (R1-M4).

- **Assessment against Nature-style criteria**
  - **Originality**: High. The concept of a paired-sequence language model with a hybrid attention mechanism is a novel contribution that goes beyond simple concatenation of single-sequence embeddings.
  - **Scientific importance**: High, if the claims are substantiated. The potential for a sequence-based method to outperform structure-based approaches in contact prediction would be a significant advance. The broad applicability across three tasks increases the potential impact.
  - **Interdisciplinary readership**: Moderate to high. The work is relevant to machine learning, computational biology, and structural biology. The clear writing and framing around three fundamental questions make it accessible to a broader audience.
  - **Technical soundness**: Currently not fully assessable. The core ideas are sound, but the lack of detail in the evaluation protocols and the unavailability of supplementary data prevent a full assessment of the technical rigor.
  - **Readability for nonspecialists**: Good. The manuscript is well-structured and the abstract and introduction are clear. The results sections are generally understandable, though some methodological details are dense.

- **Recommendation posture** Supportive if technical concerns are resolved. The core concept is promising and the reported results are potentially impactful. However, the manuscript in its current form does not provide sufficient evidence to fully substantiate the claims, particularly regarding the comparison with AlphaFold3. The authors must provide the supplementary materials, clarify the evaluation protocols, and address the concerns about statistical rigor and potential circularity before the case is established.