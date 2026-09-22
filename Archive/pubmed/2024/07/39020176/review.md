## Review setup
- **Input scope** Full manuscript text (main text, methods, figure legends not provided in full)
- **Assessment boundary** Scientific content, methodology, claims, and evidence as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors present a genome-wide experimental screen (PADI) in yeast to identify transcriptional activation domains (ADs) in Arabidopsis thaliana transcription factors, identifying 1,553 ADs in over 1,000 TFs. They develop a neural network (TADA) to predict ADs, identify six AD subtypes based on sequence features, validate ADs in the AUXIN RESPONSE FACTOR (ARF) family, and demonstrate evolutionary conservation of AD position across angiosperms.
- **Visible evidence base** Main text figures referenced (Fig. 1a-k, 2a-f, 3a-h, 4a-e, 5a-d), Extended Data Figures 1-10, Supplementary Tables 1-3, Supplementary Dataset 1, Methods section
- **Missing materials affecting confidence** Figure panels and legends not provided in full; exact statistical values, error bars, and sample sizes for many experiments not visible; full details of neural network hyperparameters and training curves not shown; raw sequencing data not accessible for independent verification

## Reviewer
- **Overall assessment** This manuscript presents a substantial and valuable resource for the plant transcription factor community. The experimental approach is systematic and the scale of data generation is impressive. The integration of experimental screening with neural network prediction and evolutionary analysis represents a strong methodological combination. However, several technical concerns need to be addressed, particularly regarding the interpretation of yeast-based results as representative of plant biology, the handling of false positives from folded domains, and the robustness of the neural network evaluation.
- **Who would be interested in the results, and why** Plant molecular biologists studying transcriptional regulation, particularly those working on transcription factor function, auxin signaling, and intrinsically disordered regions. The dataset and predictive tool will be of broad utility to the Arabidopsis community and potentially to researchers studying transcriptional regulation in other plants. The methodological framework for linking sequence features to function in IDRs will interest biochemists and computational biologists working on transcriptional activation mechanisms across eukaryotes.
- **Major strengths** 1) The scale of the experimental screen is unprecedented for plants, providing a genome-wide resource. 2) The combination of experimental data with neural network prediction and interpretability analysis (SHAP) is methodologically sophisticated. 3) The evolutionary analysis across 12 plant species adds a valuable dimension. 4) The identification of six AD subtypes moves beyond the classical acidic-aromatic paradigm. 5) The validation in Arabidopsis protoplasts and the ARF7 deletion analysis provide important biological confirmation.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (yeast-to-plant extrapolation), R1-M2 (folded domain false positives), R1-M3 (neural network evaluation robustness)
- **Assessment against Nature-style criteria** 
  - **Originality** High. This is the first proteome-wide experimental identification of ADs in plants, and the integration with neural network prediction and evolutionary analysis is novel.
  - **Scientific importance** High. The dataset and predictive tool will be widely used by the plant transcription factor community and will enable many follow-up studies.
  - **Interdisciplinary readership** Moderate. The work will primarily interest plant molecular biologists and computational biologists. The broader transcriptional regulation community may find the methodological framework of interest, but the plant-specific focus may limit broader appeal.
  - **Technical soundness** Generally strong, but with concerns about the interpretation of yeast-based results, the handling of false positives from folded domains, and the robustness of neural network evaluation metrics.
  - **Readability for nonspecialists** The main text is generally well-written and accessible, though some sections (particularly the neural network description) assume familiarity with computational methods.
- **Recommendation posture** Supportive if technical concerns are resolved. The core dataset and resource are valuable, but the interpretation of yeast-based results as representative of plant biology, the handling of false positives from folded domains, and the robustness of the neural network evaluation need to be addressed.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validity / Interpretation
- **Claim pointer** The authors state that "over half of the Arabidopsis TFs carry an AD" and that the PADI screen "accurately identifies Arabidopsis ADs" based on validation in protoplasts.
- **Evidence pointer** Summary section; Fig. 1; Fig. 3h; Fig. 4e; Methods "PADI Assay"
- **Concern** The PADI screen is conducted in yeast, and the authors acknowledge that "Arabidopsis TF fragments that activate transcription in yeast may not activate transcription in Arabidopsis." However, the manuscript does not provide a systematic assessment of the false positive rate in planta. The validation in protoplasts is limited to a small number of representative fragments (24 additional hits, as stated in the text), and the ARF7 validation is limited to a single TF. The claim that "over half of the Arabidopsis TFs carry an AD" is based on yeast activity, and the extrapolation to Arabidopsis biology is not fully justified. The authors should provide a more comprehensive validation strategy, such as testing a larger, randomly selected set of PADI hits in planta, or at minimum, clearly state the limitations of the yeast-based approach in the main text.
- **Why it matters** The central claim of the manuscript is that the PADI screen identifies Arabidopsis ADs. If a substantial fraction of yeast-positive fragments are not active in plants, the resource would be significantly less useful, and the downstream analyses (TADA training, subtype identification, evolutionary analysis) would be built on a partially incorrect foundation.
- **Resolution test** Provide additional in planta validation data for a larger, randomly selected set of PADI hits (e.g., 50-100 fragments) using a plant-based transcriptional assay. Alternatively, provide a clear statistical framework for estimating the false positive rate in planta and discuss how this affects the interpretation of the dataset.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Data interpretation / False positive control
- **Claim pointer** The authors state that "43% of high scoring fragments are from globular domains, which have sequence features consistent with ADs, but may lack AD activity in their folded context and thus we urge caution for researchers following up on specific activation domains from these regions."
- **Evidence pointer** Main text, paragraph 2; Fig. 1e-f; Methods "Data Analysis"
- **Concern** The authors identify that 43% of high-scoring fragments come from globular domains and caution against interpreting these as functional ADs. However, the manuscript does not provide a clear strategy for how users of the dataset should distinguish between high-confidence ADs (from IDRs) and potentially false positives (from folded domains). The PADI score alone does not appear to discriminate between these two classes. The authors should provide a clear annotation or filtering strategy in the dataset, such as a confidence score that incorporates IDR prediction, to guide users.
- **Why it matters** The utility of the resource depends on users being able to identify reliable ADs. If 43% of hits are potentially false positives, the dataset requires clear guidance on how to interpret and use the data. Without this, the resource may be misused, and downstream analyses (e.g., TADA training) may be affected by the inclusion of false positives.
- **Resolution test** Provide a clear annotation in the dataset (e.g., in Supplementary Table 1) that flags each hit as "high confidence" (from IDR) or "low confidence" (from globular domain), and demonstrate that the TADA network performs well when trained on high-confidence hits only.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Computational validation / Model evaluation
- **Claim pointer** The authors state that TADA "outperformed existing predictors, including PADDLE, ADpred, and a composite model" on a human dataset and achieved "96.14% AUPR" on the plant evolutionary dataset.
- **Evidence pointer** Main text, paragraphs 3-4; Extended Data Fig. 3a, 4c, 9c-d; Methods "Training dataset and encoding", "Neural network architecture", "Experimental settings and evaluation"
- **Concern** The evaluation of TADA appears to be conducted on the same type of data used for training (yeast-based PADI hits). The claim that TADA "outperforms" existing predictors on human data is made, but the details of this comparison are not fully provided. Specifically, it is unclear whether the human dataset used for evaluation is independent of the training data, whether the same threshold criteria were applied, and whether the comparison was fair (e.g., same training data, same hyperparameter tuning). Additionally, the AUPR of 96.14% on the plant evolutionary dataset seems very high, and it is unclear whether this reflects true generalization or potential data leakage (e.g., if the evolutionary dataset includes Arabidopsis sequences that were used in training).
- **Why it matters** The TADA network is a key deliverable of the manuscript. If the evaluation is not rigorous, the claims of superior performance may not be reliable, and users may not be able to trust the predictions.
- **Resolution test** Provide a detailed description of the evaluation protocol, including how the human dataset was obtained, whether it was independent of training data, and how thresholds were set. Provide a clear statement on whether the plant evolutionary dataset overlaps with the training data and how this was handled. Consider providing an independent experimental validation of TADA predictions on a set of previously uncharacterized TFs.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor / Data presentation
- **Claim pointer** The authors state that "6,205 displayed strong activation" out of 68,441 fragments tested, and that "53% of the 1,918 tested Arabidopsis TFs contained at least one AD."
- **Evidence pointer** Main text, paragraph 2; Fig. 1d, 1h-k; Methods "Data Analysis"
- **Concern** The manuscript does not provide a clear description of the statistical significance of the PADI scores. The threshold of PADI score ≥ 1 (one standard deviation from the mean) is arbitrary, and it is unclear how this threshold was chosen and whether it is statistically meaningful. Additionally, the manuscript does not report confidence intervals or measures of variability for the key proportions (e.g., 53% of TFs with ADs). The authors should provide a more rigorous statistical framework for defining ADs and reporting the associated uncertainties.
- **Why it matters** The threshold for defining an AD is central to all downstream analyses. If the threshold is not well-justified, the conclusions about the prevalence of ADs, the subtype analysis, and the evolutionary analysis may be affected.
- **Resolution test** Provide a justification for the PADI score threshold, such as a comparison with known ADs or a statistical model that accounts for the distribution of scores. Report confidence intervals for the key proportions and discuss how the results change with different thresholds.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity / Data presentation
- **Affected element** Fig. 1e-f
- **Evidence pointer** Fig. 1e-f; Main text, paragraph 2
- **Issue** The description of the NLP7 validation is somewhat confusing. The text states that "we often observed extraneous hits in regions of the protein not previously associated with the transcriptional activity" and that these hits are from folded regions. However, the figure legend is not provided, and it is unclear how the "extraneous hits" are distinguished from the "true" AD in the figure.
- **Required correction** Clarify the figure legend to clearly indicate which hits are from IDRs and which are from folded domains, and how the NLP7 validation supports the interpretation.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodology / Reproducibility
- **Affected element** Methods "Training dataset and encoding"
- **Evidence pointer** Methods "Training dataset and encoding"
- **Issue** The description of the 42 features is incomplete. The text mentions "11 side-chain properties (Table 1), 9 properties used to describe disordered regions (Table 2), and the count of each of the 20 amino acids" but Tables 1 and 2 are not provided in the manuscript text.
- **Required correction** Provide the full list of 42 features, either in the main text or in a supplementary table, to ensure reproducibility.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity / Interpretation
- **Affected element** Fig. 3a-b
- **Evidence pointer** Fig. 3a-b; Main text, paragraph 4
- **Issue** The description of the six AD subtypes is brief. The text states that "we observed distinct clusters, ultimately identifying a total of six AD subtypes" but does not provide a clear description of the distinguishing features of each subtype beyond the general enrichment patterns shown in Fig. 3b.
- **Required correction** Provide a more detailed description of the six subtypes, including their defining sequence features and any functional implications, either in the main text or in a supplementary table.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data presentation / Reproducibility
- **Affected element** Methods "Auxin-responsive reporter activation assays in yeast"
- **Evidence pointer** Methods "Auxin-responsive reporter activation assays in yeast"
- **Issue** The description of the yeast auxin signaling assay is brief. It is unclear how the ARF7 deletion constructs were expressed and how the reporter activity was quantified. The text mentions "three separate measurements were drawn at approximately one hour apart" but does not specify the number of biological replicates or the statistical analysis used.
- **Required correction** Provide more detail on the experimental design, including the number of biological replicates, the statistical tests used, and how the reporter activity was normalized.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity / Data presentation
- **Affected element** Fig. 4e
- **Evidence pointer** Fig. 4e; Main text, paragraph 5
- **Issue** The description of the FrAR7 experiment is brief. The text states that "wild-type FrARF7 displayed strong transcriptional activation whereas FrARF7ΔAD1 ΔAD2 failed to activate transcription" but does not provide quantitative data or statistical analysis.
- **Required correction** Provide quantitative data for the FrARF7 experiments, including the mean and standard deviation of the reporter activity for each construct, and the results of the statistical tests.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Data presentation / Reproducibility
- **Affected element** Methods "Determining ARF Evolution Dataset Subtypes"
- **Evidence pointer** Methods "Determining ARF Evolution Dataset Subtypes"
- **Issue** The method for assigning subtypes to the ARF evolution dataset is described briefly. The text mentions "we utilized a method described in Kobak et al. 51" but does not provide sufficient detail for reproducibility.
- **Required correction** Provide a more detailed description of the subtype assignment method, including the parameters used and how the nearest neighbors were determined.

## Risk / unsupported claims
- The claim that "over half of the Arabidopsis TFs carry an AD" is based on yeast-based activity and may not fully represent Arabidopsis biology. The manuscript acknowledges this limitation but does not provide a systematic assessment of the false positive rate in planta.
- The claim that TADA "outperforms" existing predictors on human data is not fully supported by the evidence provided, as the evaluation protocol is not described in sufficient detail.
- The claim that "43% of high scoring fragments are from globular domains" and that these "may lack AD activity in their folded context" is presented as a caution, but the manuscript does not provide a clear strategy for users to distinguish between high-confidence and low-confidence hits.
- The evolutionary analysis of AD position conservation in the ARF family is based on a limited number of species (12) and may not fully capture the diversity of angiosperm evolution.
- The manuscript does not provide a clear description of the statistical significance of the PADI scores or the confidence intervals for the key proportions, making it difficult to assess the robustness of the findings.