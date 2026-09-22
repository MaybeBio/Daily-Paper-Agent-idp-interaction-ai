## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, data analysis, and conclusions as presented in the manuscript
- **Shared manuscript claim summary** The authors analyze compositional biases of amino acids across four classes of intrinsically disordered proteins and regions (fully disordered proteins, short IDRs, long IDRs, binding IDRs) using CAID benchmark data. They identify three distinct bias types, show that compositional bias of predictions from top predictors correlates with predictive accuracy, and demonstrate that no single predictor is universally best across disorder classes. A meta-predictor combining class-specific best predictors yields significantly improved performance.
- **Visible evidence base** Abstract, Introduction, Materials and Methods, Results and Discussion, Conclusions, Tables 1-3, Figures 1-3 (referenced but not shown)
- **Missing materials affecting confidence** Figures 1-3 are referenced but not provided in the supplied text. Table contents are described but not fully shown. Statistical details of the bootstrap procedure and normality tests are partially described. The Composition Profiler tool's specific parameters and output format are not detailed.

## Reviewer
- **Overall assessment** The manuscript addresses an important and timely question in the field of intrinsic disorder prediction: whether compositional biases of predicted disordered regions align with native biases and how this affects predictive performance. The analysis is well-structured and the findings are potentially valuable for guiding future predictor development. However, several methodological details and statistical considerations need clarification to fully establish the claims. The correlation between compositional bias accuracy and predictive performance is intriguing but the causal interpretation requires more careful treatment. The meta-predictor demonstration is compelling but its practical limitations are acknowledged appropriately.
- **Who would be interested in the results, and why** Researchers developing and benchmarking disorder prediction tools will find the compositional bias analysis and the meta-predictor results directly relevant. Computational biologists studying sequence determinants of disorder will benefit from the refined categorization of compositional biases across disorder classes. The findings may also interest experimentalists who use disorder predictions to prioritize candidate regions for functional studies, as the results highlight which disorder classes are more reliably predicted.
- **Major strengths** The use of a well-annotated, large benchmark dataset (CAID) with clear exclusion of organizers' methods strengthens the reliability of the analysis. The categorization of disorder into four biologically meaningful classes is a thoughtful approach that goes beyond simple short/long dichotomies. The systematic comparison of compositional biases across native and predicted disorder using a consistent background is methodologically sound. The demonstration that compositional bias accuracy correlates with predictive performance provides a novel diagnostic insight. The meta-predictor concept, while acknowledged as impractical, offers a clear direction for future architecture development.
- **Major Concerns** The causal interpretation of the correlation between compositional bias accuracy and predictive performance is not fully justified. The categorization criteria for disorder classes, while reasonable, may introduce biases that are not fully explored. The statistical significance testing for the meta-predictor improvements relies on bootstrap resampling but the details of how class assignments are handled in resampling are unclear. The practical implications of the findings for predictor development are discussed but not fully developed into concrete recommendations.
- **Minor Comments** The manuscript would benefit from a more explicit discussion of why certain amino acids show class-specific biases. The choice of Kendall rank correlation over other measures could be justified more thoroughly. The authors could clarify whether the compositional bias analysis accounts for amino acid background frequencies in a way that is comparable across classes of different sizes. The statement about "generic" disorder bias could be more precisely defined.
- **Technical failings that need to be addressed before the case is established** The causal claim linking compositional bias accuracy to predictive performance requires either experimental manipulation or a more nuanced discussion of confounding factors. The bootstrap procedure for statistical testing needs clearer specification regarding how protein-level dependencies are handled. The authors should demonstrate that the three identified bias types are robust to alternative categorization thresholds.
- **Assessment against Nature-style criteria** Originality: The work provides a novel integration of compositional bias analysis with predictive performance assessment, extending prior observations about short vs. long IDR differences. Scientific importance: The findings have direct implications for understanding the limitations of current predictors and guiding future development, which is significant for the field. Interdisciplinary readership: The work is primarily of interest to computational biologists and bioinformaticians; the connection to experimental biology is indirect. Technical soundness: The methodology is generally sound but requires additional statistical rigor and sensitivity analyses to fully support the conclusions. Readability for nonspecialists: The manuscript is clearly written and accessible to readers with basic knowledge of protein sequence analysis, though some statistical details may be challenging for non-experts.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the causal interpretation of the correlation and the robustness of the classification scheme.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor and causal inference
- **Claim pointer** "The accuracy of disorder predictions across different methods is correlated with the correctness of the compositional bias of their predictions highlighting the importance of the compositional bias."
- **Evidence pointer** Section 3.3, Figure 3 (not shown)
- **Concern** The manuscript reports a Pearson correlation coefficient of 0.703 between predictive performance (AUC) and compositional bias accuracy (KCC with native bias) across ten predictors. However, the causal direction is not established. It is plausible that predictors with higher overall accuracy naturally produce predictions with more accurate compositional biases as a byproduct, rather than compositional bias accuracy being a driver of performance. The authors do not control for potential confounding variables such as predictor architecture, training data size, or feature types.
- **Why it matters** The claim that compositional bias accuracy "highlights the importance" of compositional bias implies a mechanistic relationship. If the correlation is merely a consequence of overall accuracy, the finding is less novel and the recommendation to focus on compositional bias in predictor development would be less justified.
- **Resolution test** The authors should either (a) perform a partial correlation analysis controlling for overall accuracy or other relevant variables, (b) demonstrate that predictors with similar overall accuracy but different compositional bias accuracy show corresponding performance differences, or (c) rephrase the claim to be explicitly correlational without causal language.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency and robustness
- **Claim pointer** "We identify three distinct biases: for the fully disordered proteins, the short IDRs and the long and binding IDRs combined."
- **Evidence pointer** Section 3.2, Figures 1 and 2 (not shown)
- **Concern** The categorization of IDRs into four classes uses specific thresholds (disorder content ≥ 0.8 for fully disordered, 10-15 residues for short, >70 residues for long, and binding annotation). The authors state that these thresholds are not rigorously defined but do not provide a sensitivity analysis. It is unclear whether the identification of three distinct bias types is robust to reasonable variations in these thresholds. Additionally, the binding IDR class overlaps with the other three classes, and the authors do not clarify how this overlap is handled in the analysis.
- **Why it matters** The central finding of three distinct bias types depends on the classification scheme. If the result is sensitive to threshold choices, the conclusion would be weakened. The overlap between binding and other classes could confound the interpretation of the binding-specific bias.
- **Resolution test** The authors should perform a sensitivity analysis varying the thresholds (e.g., disorder content 0.7-0.9, short IDR length 8-20, long IDR length 50-100) and demonstrate that the three-bias structure is stable. They should also clarify whether binding IDRs are analyzed as a separate class or as a subset of the other classes.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Statistical testing methodology
- **Claim pointer** "We also assessed the statistical significance of differences in the predictive performance between the meta-method and each of the top ten disorder predictors using the procedure described in Section 2.3."
- **Evidence pointer** Section 2.3, Section 3.5, Table 3 (not fully shown)
- **Concern** The bootstrap procedure resamples 50% of proteins 100 times and uses t-tests or Wilcoxon tests depending on normality. However, the manuscript does not specify how the class assignments are handled during resampling. If a protein is resampled, its class assignment should be preserved, but it is unclear whether the class proportions are maintained in each bootstrap sample. Additionally, 100 bootstrap iterations may be insufficient for stable p-value estimates, particularly for small classes.
- **Why it matters** The statistical significance of the meta-predictor improvements is a key claim. If the resampling procedure does not properly account for the class structure or has insufficient iterations, the reported p-values may be unreliable.
- **Resolution test** The authors should describe the resampling procedure in more detail, including how class assignments are preserved, and consider increasing the number of bootstrap iterations to at least 1000. They should also report confidence intervals for the performance differences.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability and external validity
- **Claim pointer** "The predictive quality is relatively low for the disorder classes with compositional bias that is the most different from the 'generic' disorder bias, while being much higher for the classes with the most similar bias."
- **Evidence pointer** Section 3.4, Table 2 (not fully shown)
- **Concern** The analysis is based solely on the CAID dataset, which is derived from DisProt annotations. The authors do not discuss whether these findings would generalize to other disorder annotation sources (e.g., IDEAL, PED) or to predictions on novel proteins not represented in the training data of the predictors. The CAID dataset may have inherent biases in terms of protein types and disorder functions represented.
- **Why it matters** The claim that compositional bias influences predictive performance across disorder classes is presented as a general finding. If it is specific to the CAID dataset, the implications for predictor development would be more limited.
- **Resolution test** The authors should either (a) validate the key findings on an independent dataset, or (b) explicitly discuss the limitations of generalizing from the CAID dataset and temper the claims accordingly.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of definitions
- **Affected element** Section 2.2, categorization of IDRs
- **Evidence pointer** Section 2.2
- **Issue** The term "generic disorder bias" is used in the abstract and results but is not precisely defined. It appears to refer to the bias computed across all disordered residues in the CAID dataset, but this should be stated explicitly.
- **Required correction** Define "generic disorder bias" as the compositional bias computed over all disordered residues in the CAID dataset, and use this term consistently throughout.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Interpretation of amino acid biases
- **Affected element** Section 3.2, discussion of proline
- **Evidence pointer** Section 3.2
- **Issue** The discussion of proline enrichment in long and binding IDRs is interesting but could be expanded. The authors mention proline as a modulator of secondary structures but do not discuss other amino acids that show class-specific biases.
- **Required correction** Provide a brief discussion of at least two or three other amino acids that show notable class-specific biases and their potential functional implications.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section 2.3, Composition Profiler
- **Evidence pointer** Section 2.3
- **Issue** The manuscript states that Composition Profiler was used but does not specify the version, parameters, or whether the output was normalized in any way. This limits reproducibility.
- **Required correction** Provide the specific version of Composition Profiler used, the parameters selected, and any post-processing steps applied to the output.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation of results
- **Affected element** Section 3.4, Table 2
- **Evidence pointer** Section 3.4, Table 2
- **Issue** The manuscript reports average AUC values across predictors for each class but does not report the variability (e.g., standard deviation or range) across predictors. This makes it difficult to assess the consistency of the pattern.
- **Required correction** Report the standard deviation or range of AUC values across the ten predictors for each class in Table 2.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Section 4, Conclusions
- **Evidence pointer** Section 4
- **Issue** The conclusions do not explicitly acknowledge the limitation that the meta-predictor is impractical without prior knowledge of the disorder class. While this is mentioned in Section 3.5, it should be reiterated in the conclusions to avoid overstatement.
- **Required correction** Add a sentence in the conclusions acknowledging the practical limitation of the meta-predictor approach and clarifying that the finding is motivational rather than directly applicable.

## Risk / unsupported claims
- The causal claim that compositional bias accuracy "highlights the importance" of compositional bias in determining predictive performance is not fully supported by the correlational evidence presented.
- The claim of "three distinct biases" is not demonstrated to be robust to variations in the categorization thresholds.
- The generalizability of the findings beyond the CAID dataset is not established.
- The statistical significance of the meta-predictor improvements may be unreliable given the limited bootstrap iterations and unclear handling of class structure.
- The statement that "no single predictor is universally best" is supported by the data but is presented as a general conclusion without discussing potential exceptions or context-dependence.