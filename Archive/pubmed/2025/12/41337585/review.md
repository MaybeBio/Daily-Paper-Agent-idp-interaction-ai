## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods) without figures, tables, or supplementary materials
- **Assessment boundary** Scientific claims, methodological soundness, and interpretational validity based solely on the provided text
- **Shared manuscript claim summary** The authors develop a machine learning model (IDR-Puncta) trained on experimentally characterized intrinsically disordered regions (IDRs) from fusion oncoproteins to predict cellular condensate formation. They apply this model to the human proteome, predicting that ~12% of human IDRs form condensates, and report that proteins containing condensate-forming IDRs are enriched in RNA processing and splicing functions and localize to membraneless organelles.
- **Visible evidence base** Text descriptions of experimental procedures, model performance metrics (AUC, AUCPR, accuracy, balanced accuracy), enrichment analyses, and comparisons with existing predictors
- **Missing materials affecting confidence** All figures, tables, supplementary materials, model code, and raw data; specific numerical results for GO enrichment analyses; details of the 25 selected features; full performance comparison with existing tools

## Reviewer
- **Overall assessment** This manuscript presents a valuable dataset of experimentally characterized IDR condensation behavior and a predictive model with strong reported performance. The central claims regarding proteome-wide prediction and functional enrichment are plausible but cannot be fully evaluated without access to figures, tables, and supplementary data. The work addresses an important gap in the field by providing standardized cellular assays for IDR condensate formation. However, several methodological details and potential biases require clarification before the broader conclusions can be accepted.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, and intrinsically disordered proteins would find the experimentally validated dataset and predictive model useful. The proteome-wide predictions and functional enrichment analysis will interest cell biologists studying RNA processing and nuclear organization. Computational biologists developing predictors for protein phase behavior would benefit from the standardized experimental dataset and feature analysis.
- **Major strengths** The use of standardized experimental conditions and rigorous image analysis to generate training data addresses a known limitation in the field. The model's reported performance metrics (AUC 0.98 in cross-validation, 0.95 on held-out verification set) are strong. The analysis of feature importance and the comparison with existing predictors provide useful context. The application to the human proteome and functional enrichment analysis generates testable hypotheses.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Data representativeness and generalizability
  - **Claim pointer** The authors claim that "the physicochemical features of the FO-derived Training IDRs and Verification IDRs selected from the human IDRome spanned the feature landscape of the human IDRome, including the high-density regions"
  - **Evidence pointer** Results section "Predicting IDR cellular condensation using physicochemical features and ML"; Figure S7B-C (not visible)
  - **Concern** The training data are derived exclusively from fusion oncoproteins, which may have sequence features that differ systematically from the broader human proteome. While the authors argue that the feature space is well-covered, the UMAP analysis is performed on the same 25 features used for model training, which could mask relevant differences. The claim that the model applies to the human IDRome depends critically on this representativeness argument, but the evidence is not visible in the provided text.
  - **Why it matters** If the training distribution is not representative, the proteome-wide predictions (12% of human IDRs) could be systematically biased, undermining the central claim of the paper.
  - **Resolution test** Provide the UMAP visualization with clear labeling of training, verification, and human IDRome points. Additionally, perform a quantitative assessment of feature distribution overlap (e.g., Kolmogorov-Smirnov tests per feature) between the training set and the human IDRome.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Model validation and performance reporting
  - **Claim pointer** The authors report cross-validated performance (AUC 0.98, AUCPR 0.93, accuracy 0.95, balanced accuracy 0.92) and verification performance (AUC 0.95, AUCPR 0.88, accuracy 0.90, balanced accuracy 0.92)
  - **Evidence pointer** Results section "Predicting IDR cellular condensation using physicochemical features and ML"; Figure 3B, 3D (not visible)
  - **Concern** The verification set of 30 IDRs is small, and the selection procedure for the 13 additional verification IDRs was based on model predictions (predicted probability range 0.39-1.0), which could introduce selection bias. The exclusion of 3 verification IDRs classified as "nucleolar" or "other" from performance evaluation is not fully justified. Additionally, the class imbalance in the training set (41 positive vs 137 negative) and its handling in the model are not described.
  - **Why it matters** Biased verification set construction or inadequate handling of class imbalance could inflate reported performance metrics and lead to overoptimistic claims about model accuracy.
  - **Resolution test** Report performance metrics on the full 33 verification IDRs including those classified as "nucleolar" or "other" (potentially as a three-class problem). Describe the class imbalance handling strategy. Provide confidence intervals for all performance metrics.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Functional enrichment analysis interpretation
  - **Claim pointer** The authors claim that "proteins with condensate-forming IDRs are significantly enriched in RNA processing and splicing functions and are predominantly localized to membraneless organelles"
  - **Evidence pointer** Results section "Human proteins with puncta(+) IDRs are enriched for RNA processing–related functions"; Figure 4A-B (not visible)
  - **Concern** The GO enrichment analysis compares proteins with puncta(+) IDRs against all human proteins, but the appropriate background should be proteins containing IDRs (since the model only applies to IDR-containing proteins). The comparison against all human proteins could inflate enrichment for functions common to IDR-containing proteins generally. The authors do note that some functions are shared with puncta(−) IDR proteins, but the magnitude of the difference is not quantified in the text.
  - **Why it matters** The claim of specific functional enrichment for condensate-forming IDRs is central to the biological conclusions. If the enrichment is not specific to puncta(+) IDRs but rather general to IDR-containing proteins, the interpretation would need substantial revision.
  - **Resolution test** Re-run the GO enrichment analysis using proteins with only puncta(−) IDRs as the background. Report the enrichment statistics for both comparisons and demonstrate that the RNA processing enrichment is specific to puncta(+) IDR proteins.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Comparison with existing predictors
  - **Claim pointer** The authors state that existing predictors "rely on literature-mined data, which were often obtained using nonstandard experimental conditions, leading to variability and noise" and imply their model addresses these limitations
  - **Evidence pointer** Introduction; Discussion
  - **Concern** The manuscript does not provide a systematic quantitative comparison between the IDR-Puncta model and existing predictors (e.g., catGranule, ParSe v2, FuzDrop) on the same verification set. The authors mention applying the von Bülow et al. predictor to their data but do not report comparative performance metrics.
  - **Why it matters** Without direct comparison, it is unclear whether the IDR-Puncta model provides meaningful improvement over existing tools or merely represents an alternative approach with similar performance.
  - **Resolution test** Apply existing predictors to the verification set and report comparative performance metrics (AUC, accuracy, etc.). Discuss cases where predictions differ and what features drive those differences.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Methodological clarity
  - **Affected element** IDR length threshold
  - **Evidence pointer** Materials and Methods "IDR selection for in-cell expression"
  - **Issue** The threshold of ≥60 amino acids is justified by reference to existing databases, but the rationale for this specific cutoff is not explained. The authors note that no sequences shorter than 60 residues exist in PhaSePro or LLPSDB, but this does not establish that shorter IDRs cannot form condensates.
  - **Required correction** Provide additional justification for the length threshold or acknowledge that shorter IDRs may also form condensates and are excluded from the current analysis.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical detail
  - **Affected element** Puncta threshold
  - **Evidence pointer** Materials and Methods "Quantitative image analysis"
  - **Issue** The threshold of ≥24% of cells with puncta for classification as puncta(+) is described as chosen "for agreement with manual assessment," but the process for determining this threshold is not described in detail.
  - **Required correction** Describe how the 24% threshold was determined, including any sensitivity analysis around this value.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interpretational caution
  - **Affected element** Model interpretation
  - **Evidence pointer** Discussion
  - **Issue** The authors state the model "will be a powerful tool for uncovering the biological roles of proteins with puncta(+) and puncta(−) IDRs in organisms beyond humans" but do not discuss potential limitations of cross-species transfer, given that the model was trained on human fusion oncoprotein-derived IDRs.
  - **Required correction** Add a brief discussion of potential limitations when applying the model to non-human proteomes.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Data availability
  - **Affected element** Code and data availability
  - **Evidence pointer** Acknowledgments
  - **Issue** The authors state that "all original codes have been deposited on Zenodo" and provide a DOI, but the specific version and any dependencies are not described.
  - **Required correction** Provide a brief description of the code structure, dependencies, and usage instructions in the supplementary materials.

## Risk / unsupported claims
- The claim that ~12% of human IDRs form condensates cannot be independently verified without access to the full prediction results and the definition of the human IDRome used
- The claim that proteins with puncta(+) IDRs are "predominantly localized to membraneless organelles" is based on GO cellular component analysis, but the statistical significance and effect sizes are not reported in the text
- The statement that the model "will be a powerful tool for uncovering the biological roles of proteins with puncta(+) and puncta(−) IDRs in organisms beyond humans" is speculative and not supported by cross-species validation data
- The comparison with the von Bülow et al. predictor is mentioned but not quantified in the text, making the claimed complementarity difficult to assess
- The claim that the training data "spanned the feature landscape of the human IDRome" relies on UMAP visualization that is not visible in the provided text

## Assessment against Nature-style criteria
- **Originality** The work provides a new experimentally validated dataset of IDR condensation behavior and a predictive model trained on standardized cellular assays. While individual components (IDR prediction, fusion oncoprotein condensates) have been explored, the combination of standardized experimental data with ML prediction for proteome-wide analysis represents a useful contribution. However, the conceptual advance over existing predictors is incremental rather than transformative.
- **Scientific importance** The question of which IDRs form condensates and their functional implications is of broad interest. The predicted enrichment of RNA processing functions among condensate-forming IDR proteins, if robust, would support emerging views of RNA-related processes occurring in condensate environments. The resource value of the dataset and model is significant for the phase separation community.
- **Interdisciplinary readership** The work bridges computational biology, biophysics, and cell biology. The findings on RNA processing enrichment would interest RNA biologists and cell biologists studying nuclear organization. The methodological approach would interest computational biologists developing predictive tools. The writing is generally accessible, though some sections assume familiarity with phase separation concepts.
- **Technical soundness** The experimental procedures appear carefully designed with standardized conditions and rigorous image analysis. The ML methodology is appropriate, though the small verification set and potential selection bias are concerns. The feature analysis is thorough. The GO enrichment analysis has a potential background selection issue that needs addressing.
- **Readability for nonspecialists** The abstract and introduction are clear and accessible. The results section is dense but understandable. The discussion effectively contextualizes the findings. Some methodological details in the materials and methods section would benefit from additional explanation for non-specialist readers.

## Recommendation posture
**Supportive if technical concerns are resolved.** The manuscript presents a valuable dataset and model with strong reported performance. The central claims are plausible but require verification of the representativeness argument, clarification of the verification set construction, and re-analysis of the GO enrichment with appropriate background. If these concerns are adequately addressed, the work would make a solid contribution to the field. However, the incremental nature of the advance over existing predictors and the need for more rigorous validation suggest this is not a transformative contribution.