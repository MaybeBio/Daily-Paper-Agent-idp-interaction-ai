## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion) without supplementary material or figures.
- **Assessment boundary** Scientific claims, methodological soundness, feature design rationale, model evaluation, and generalizability as presented in the provided text. No assessment of supplementary figures or data beyond what is described.
- **Shared manuscript claim summary** The authors propose a new fixed-dimensionality feature ("bag of amino acid interactions", BAAI) for predicting radius of gyration and scaling exponent of intrinsically disordered proteins from sequence, and demonstrate its performance against categorical and physically-motivated baselines on a coarse-grained simulation dataset (IDP-10260), including extrapolation and temperature-dependence tests.
- **Visible evidence base** Text descriptions of methods, results, and comparisons; references to figures (Fig. 2, 3a-c, 4, 5a-b) and supplementary sections (S5, S7, S8, S15, S18, S19) whose actual content is not provided.
- **Missing materials affecting confidence** All figures, tables, supplementary information, exact numerical results (R², MSE, RMSE values are mentioned but not given), dataset details beyond description, and code or model hyperparameters. These are essential for verifying the quantitative claims.

## Reviewer
- **Overall assessment** The manuscript presents a useful and physically-motivated feature representation for IDP property prediction, with a clear rationale and reasonable experimental design. However, the evidence as presented is insufficient to fully establish the claimed advantages, particularly regarding the marginal outperformance of BAAI over count encoding, the robustness of extrapolation claims, and the interpretability of the temperature-dependent results. The work is of interest to the IDP and machine learning communities, but several technical and evidential gaps must be addressed.
- **Who would be interested in the results, and why** Researchers in intrinsically disordered protein biophysics, computational polymer physics, and machine learning applied to biomolecular sequence-property prediction. The BAAI feature could be useful for high-throughput screening or design tasks where sequence-length-independent representations are desirable. The temperature integration also appeals to those studying temperature-dependent IDP behavior.
- **Major strengths** (1) The BAAI feature is novel, physically motivated, and fixed-dimensionality, addressing a real limitation of sequence-length-dependent encodings. (2) The comparison across multiple feature types and models is systematic. (3) The inclusion of extrapolation and temperature-dependence tests is forward-looking and relevant for practical deployment. (4) The writing is clear and accessible for a broad readership.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative evidence missing), R1-M2 (baseline comparison incomplete), R1-M3 (extrapolation claims under-supported), R1-M4 (temperature integration rationale unclear).
- **Assessment against Nature-style criteria**  
  - *Originality*: The BAAI feature is a novel contribution, though it builds on existing "bag of bonds" concepts from chemistry. The application to IDPs is new.  
  - *Scientific importance*: Moderate to high for the IDP community, as accurate and scalable sequence-based predictors are valuable. However, the demonstrated improvement over simpler baselines is marginal, limiting immediate impact.  
  - *Interdisciplinary readership*: The work bridges polymer physics, protein science, and machine learning, which could attract a broad audience if the claims are substantiated.  
  - *Technical soundness*: The methodology is generally sound, but the lack of quantitative results and incomplete baselines prevent full assessment.  
  - *Readability for nonspecialists*: The manuscript is well-written and explains concepts clearly, though some machine learning details are assumed.  
- **Recommendation posture** Supportive if technical concerns are resolved, particularly the provision of quantitative evidence and stronger baseline comparisons. Currently not fully established from the provided evidence.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The manuscript claims that BAAI "marginally outperforms" other features, and reports R² values (e.g., 0.77 for chain-length baseline, 0.95 and 0.98 for temperature-integrated model) without providing the actual numerical results for the main comparisons.  
- **Evidence pointer** Results and discussion, Section 3.1-3.4; figures referenced but not provided.  
- **Concern** The central quantitative claims are not verifiable from the text alone. No R², MSE, or RMSE values are given for the BAAI versus count encoding comparisons, nor for the extrapolation tests. The reader cannot assess whether the claimed "marginal outperformance" is statistically significant or practically meaningful.  
- **Why it matters** The core contribution of the paper is the performance of the BAAI feature. Without quantitative evidence, the case for its adoption is not established.  
- **Resolution test** Provide a table with all model-feature combinations, their R², MSE, RMSE (and confidence intervals if possible) for the 300 K test set, the extrapolation tests, and the temperature-integrated model. Include statistical significance tests where appropriate.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Baseline adequacy  
- **Claim pointer** The manuscript states that BAAI outperforms "purely categorical and other physically-motivated features," but the comparison set is incomplete. The augmented fingerprint (Webb et al.) is only mentioned in the extrapolation section, not in the main performance comparison.  
- **Evidence pointer** Results and discussion, Sections 3.1-3.4.  
- **Concern** The main comparison (Fig. 3c) appears to pit BAAI only against count encoding, ordinal encoding, and one-hot encoding. The augmented fingerprint, which is a strong physically-motivated baseline, is only used in the extrapolation tests. This is an unfair or incomplete comparison for establishing BAAI's relative merit.  
- **Why it matters** If the augmented fingerprint performs comparably or better on the main task, the claimed advantage of BAAI is weakened. The reader needs a direct comparison on the same test set.  
- **Resolution test** Include the augmented fingerprint in the main performance comparison (Fig. 3 or a new table) and report its R², MSE, RMSE alongside BAAI and other features.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Generalizability evidence  
- **Claim pointer** The manuscript claims "solid extrapolation capabilities" for BAAI based on tests with longer/shorter sequences and reverse sequences, but the results are only described qualitatively.  
- **Evidence pointer** Results and discussion, Section 3.4; Figure 5a.  
- **Concern** The extrapolation tests are a key selling point, but no quantitative results are provided. It is unclear how much performance degrades, whether the degradation is acceptable, and how it compares to other features (e.g., augmented fingerprint) on the same tasks. The reverse-sequence test is mentioned but not described in terms of results.  
- **Why it matters** Extrapolation is critical for real-world use in design or screening. Without numbers, the claim of "solid" performance is unsubstantiated.  
- **Resolution test** Provide quantitative results (R², MSE, RMSE) for all extrapolation tests, including the reverse-sequence test, and compare BAAI against at least one baseline (e.g., augmented fingerprint) on the same splits.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Conceptual clarity  
- **Claim pointer** The temperature integration section states that the model predicts Rg and scaling exponent at seven temperatures, but the rationale for adding temperature as a single scalar feature is not fully justified. The authors note that only chain expansion with temperature is considered, but the physical basis for this simplification is not discussed.  
- **Evidence pointer** Results and discussion, Section 3.5; Figure 5b.  
- **Concern** The temperature-dependent model is presented as a promising extension, but the limitations of the coarse-grained model (no cold denaturation) are acknowledged only briefly. The choice to use a single temperature feature, rather than temperature-dependent interaction parameters, is not compared to alternatives.  
- **Why it matters** The claim of "promising" temperature integration needs a clearer physical and methodological justification, especially if the model is to be used for predictive purposes.  
- **Resolution test** Discuss alternative ways to encode temperature (e.g., temperature-scaled interaction strengths) and justify the chosen approach. Provide a comparison, even if qualitative, of the model's performance across temperatures.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Methods, Training Process  
- **Evidence pointer** Section 2.4  
- **Issue** The manuscript does not specify the exact hyperparameters for the neural networks (e.g., number of layers, hidden units, activation functions, learning rate, regularization) or the classical models (e.g., kernel parameters for SVR, GPR).  
- **Required correction** Provide a table or supplementary section listing all hyperparameters and any tuning procedures.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Statistical rigor  
- **Affected element** Results, Section 3.1  
- **Evidence pointer** Figure 2  
- **Issue** The manuscript reports R², MSE, and RMSE but does not mention whether these are averaged over multiple train/test splits or if confidence intervals are provided.  
- **Required correction** State whether results are from a single split or cross-validation, and report standard deviations or confidence intervals.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Introduction, last paragraph  
- **Evidence pointer** Section 1  
- **Issue** The phrase "bag of amino acid interactions" is introduced but the abbreviation "BAAI" is used later without being defined at first use.  
- **Required correction** Define the abbreviation at first mention.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Results, Section 3.4  
- **Evidence pointer** Figure 5a  
- **Issue** The reverse-sequence test is mentioned but no results are shown or described.  
- **Required correction** Either provide results for the reverse-sequence test or remove the mention if it is not part of the main analysis.

- **Concern ID** R1-m5  
- **Severity** Minor  
- **Axis** Language  
- **Affected element** Abstract, last sentence  
- **Evidence pointer** Abstract  
- **Issue** The phrase "for future use, this feature can potentially provide physical insights into amino acid interactions, including their temperature dependence" is vague and could be more specific.  
- **Required correction** Clarify what kind of physical insights are expected and how the feature would enable them.

## Risk / unsupported claims
- The claim that BAAI "marginally outperforms" other features is unsupported without quantitative results.
- The claim of "solid extrapolation capabilities" is unsupported without numerical evidence.
- The claim that the temperature-integrated model is "promising" is weakly supported, as only one model architecture is tested and the physical rationale is incomplete.
- The statement that BAAI "can differentiate between sequences of the same amino acid composition, but with different sequencing of residues" is plausible but not demonstrated with specific examples or quantitative comparisons.
- The claim that the BAAI feature "does not have an explicit specification of the length in its features" is true by design, but the implication that this is advantageous is not tested against length-dependent features beyond the limited comparisons shown.