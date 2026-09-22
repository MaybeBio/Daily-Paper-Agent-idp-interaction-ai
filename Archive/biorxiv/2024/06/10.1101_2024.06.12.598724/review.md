## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, data availability, acknowledgments)
- **Assessment boundary** Scientific content, methodology, claims, and evidence as presented in the provided text. No external data or supplementary materials were accessed.
- **Shared manuscript claim summary** The authors evaluate 35 variant effect predictors (VEPs) across 963 human protein-coding genes using ClinVar pathogenic and gnomAD putatively benign missense variants. They report considerable gene-level heterogeneity in VEP performance as measured by AUROC, train random forest models to predict gene-level AUROC from 99 gene and protein features, identify intrinsic disorder as a key factor that inflates apparent VEP performance, and discuss implications for interpreting and using VEPs in clinical and research settings.
- **Visible evidence base** Abstract, Introduction, Results (four subsections), Discussion, Methods (three subsections), Data availability statement. Figures are referenced but not visible. Supplementary tables are referenced but not provided.
- **Missing materials affecting confidence** Figures 1-6, Tables S1-S2, the supplementary dataset with predictions, and the full feature list are not available. The Methods section is abbreviated and lacks computational details. No statistical code or model parameters are provided.

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question: why do variant effect predictors perform so differently across genes, and can this heterogeneity be predicted? The authors present a large-scale analysis with a clear conceptual framework and identify intrinsic disorder as a factor that inflates AUROC in a way that may not reflect true clinical utility. The work is relevant to a broad audience in human genetics, clinical genomics, and computational biology. However, the manuscript as provided has several significant limitations. The most critical issue is that the central claim regarding disorder-driven inflation of AUROC is presented with insufficient quantitative detail and without visible figures. The random forest models are described at a high level, and the feature set includes gnomAD-derived variables that may introduce circularity, which the authors acknowledge but do not fully address. The discussion of AUROC limitations is thoughtful but the proposed alternatives are not explored. Overall, the study is promising and likely of interest to the community, but the current evidence base is insufficient to fully establish the claims.
- **Who would be interested in the results, and why** Clinical geneticists and molecular diagnosticians who use VEPs for variant interpretation would be interested in understanding when these tools are more or less reliable. Computational biologists developing or benchmarking VEPs would benefit from the gene-level feature analysis and the identification of disorder as a confounder. Researchers studying intrinsically disordered proteins and their role in disease would find the connection between disorder and VEP performance relevant. The work also speaks to the broader community interested in the evaluation of machine learning models in genomics.
- **Major strengths** The study addresses a practical and underappreciated problem: gene-level heterogeneity in VEP performance. The scale of the analysis, covering 35 VEPs and 963 genes, is substantial. The use of random forest models with SHAP explanations is appropriate for identifying predictive features. The authors are transparent about the limitations of AUROC and the potential circularity of including gnomAD-derived features. The Pax6 example is a clear and illustrative case study. The writing is generally clear and accessible.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (circularity of gnomAD-derived features), R1-M2 (insufficient quantitative evidence for disorder claim), R1-M3 (incomplete methodological detail for reproducibility), R1-M4 (unvalidated predictive utility).
- **Assessment against Nature-style criteria** Originality: The question of gene-level heterogeneity in VEP performance is not entirely new, but the systematic analysis across 35 predictors and the identification of intrinsic disorder as a specific inflating factor is a novel contribution. Scientific importance: The findings have direct implications for the use of VEPs in clinical variant interpretation, which is a high-stakes application. The work could influence how VEP performance is reported and interpreted. Interdisciplinary readership: The topic bridges clinical genetics, protein biophysics, and machine learning, and the writing is largely accessible to nonspecialists. Technical soundness: The core methodology is reasonable, but the lack of visible figures and detailed methods limits the ability to fully assess technical rigor. The circularity concern is a substantive issue. Readability for nonspecialists: The manuscript is well written and the concepts are explained clearly, though some sections assume familiarity with VEPs and AUROC.
- **Recommendation posture** Supportive if technical concerns are resolved. The study addresses an important problem and the core idea is compelling, but the current evidence base is insufficient to fully establish the claims. The authors should provide the missing figures, address the circularity issue, and strengthen the quantitative analysis.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Circularity / validity of performance prediction
- **Claim pointer** The authors state that gnomAD-derived features, including ddG_fold, gnomAD_distance, and vep_gnomad_mean, are among the most important predictors of AUROC. They acknowledge potential circularity but argue for inclusion from a practical perspective.
- **Evidence pointer** Results section "Multiple features contribute to the predictability of AUROC"; Methods section "Gene features dataset"
- **Concern** The inclusion of features derived from the same gnomAD variants used to calculate the AUROC being predicted introduces a direct circularity. The AUROC for a gene is computed using the putatively benign gnomAD variants, and the model then uses properties of those same variants (e.g., mean predicted stability, clustering) to predict that AUROC. This is not merely a practical concern; it means the predictive models may be learning to identify genes with certain gnomAD variant properties rather than genes where VEPs are genuinely more discriminative. The authors acknowledge this but do not provide a quantitative assessment of how much of the predictive power is driven by these circular features versus independent biological features. Without such an analysis, the claim that gene-level features can predict VEP performance is not established.
- **Why it matters** If the predictive power of the models is largely due to circular features, then the models cannot be used to predict performance for genes with few or no gnomAD variants, which is precisely the scenario where such predictions would be most valuable. The central practical implication of the study is undermined.
- **Resolution test** The authors should retrain the random forest models excluding all gnomAD-derived features and report the change in predictive performance. They should also report the feature importance rankings for models trained without these features. If the models retain reasonable predictive power, the claim is strengthened. If not, the authors should temper their conclusions and discuss the implications of circularity more thoroughly.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative support for central claim
- **Claim pointer** The authors claim that intrinsic disorder inflates apparent VEP performance, leading to higher AUROC values, and that this is due to enrichment of putatively benign variants in disordered regions.
- **Evidence pointer** Results section "Intrinsically disordered regions inflate the apparent performance of VEPs"; Figures 5 and 6
- **Concern** The central claim of the paper is presented with reference to Figures 5 and 6, but these figures are not visible in the provided text. The quantitative basis for the claim is therefore not assessable. The text states a mean difference of 0.015 in AUROC between high- and low-disorder groups, but it is unclear if this is statistically significant, what the variance is, and whether this effect is consistent across VEPs. The Pax6 example is illustrative but is a single gene and does not establish a general phenomenon. The mechanism proposed, that disordered regions are enriched in weakly conserved putatively benign variants, is plausible but is not directly tested.
- **Why it matters** This is the most novel and potentially impactful finding of the study. If the effect is small or inconsistent, the practical implications are limited. If the effect is large, it has implications for how VEP performance should be evaluated. The current evidence is insufficient to judge.
- **Resolution test** The authors should provide the actual data behind Figures 5 and 6, including effect sizes, confidence intervals, and statistical tests. They should also perform a direct test of the proposed mechanism, for example by comparing AUROC for variants in disordered vs ordered regions within the same genes, or by controlling for conservation levels. The Pax6 example should be supplemented with a systematic analysis across all genes.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The Methods section describes the training of random forest models with Bayesian hyperparameter optimization and 100 repeated hold-out cross-validations.
- **Evidence pointer** Methods section "Model training and evaluation"
- **Concern** The Methods section is too brief to allow reproduction of the analysis. Key details are missing, including the exact feature list (referenced to Table S1, not provided), the handling of missing values, the correlation structure among features, the specific hyperparameter search space, and the criteria for selecting the final models. The use of 100 repeated hold-out cross-validations is mentioned but the rationale and the variance of the performance estimates are not reported. The split into training and evaluation sets is described, but it is unclear whether the same split was used across all VEPs and whether any nested validation was performed.
- **Why it matters** Reproducibility is a core requirement for computational studies. Without sufficient methodological detail, other researchers cannot verify or build upon the findings. The lack of a detailed feature list is particularly problematic given the circularity concern.
- **Resolution test** The authors should provide a complete description of the methods, including the full feature list, data preprocessing steps, hyperparameter ranges, and model selection criteria. They should also make the code and data publicly available, or at least provide a detailed pseudocode. The supplementary materials should be referenced more precisely.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Practical utility of predictions
- **Claim pointer** The authors suggest that their models could be used to identify genes where VEPs are likely to be more or less reliable, and they provide predictions for the majority of human protein-coding genes in a supplementary dataset.
- **Evidence pointer** Results section "VEP performance on different genes as measured by AUROC is predictable"; Data availability statement
- **Concern** The practical utility of the predictions is not demonstrated. The authors do not show how the predicted AUROC values could be used in a real clinical or research setting. For example, they do not compare their model predictions to any external benchmark or show that genes predicted to have high AUROC actually have better VEP performance in an independent dataset. The supplementary dataset is mentioned but not described in detail, and its format and content are unclear.
- **Why it matters** The stated motivation for the study is to improve the interpretation and trust of VEP predictions. If the models cannot be shown to have practical utility, the impact of the work is limited.
- **Resolution test** The authors should provide a concrete example of how their predictions could be used, such as a decision rule for when to trust VEP predictions for a given gene. They should also validate the predictions on an independent set of genes or variants, for example using recent ClinVar submissions or a held-out set of genes.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** Use of "putatively benign"
- **Evidence pointer** Methods section "Missense variants dataset"
- **Issue** The term "putatively benign" is used throughout, but the definition is not precise. The authors state that gnomAD variants were used with no allele frequency filter, which means the set includes variants at all frequencies, including potentially deleterious variants in recessive genes or with incomplete penetrance. The authors acknowledge this in the Discussion but the implications for the AUROC calculations are not fully explored.
- **Required correction** The authors should clarify the composition of the putatively benign set, including the allele frequency distribution, and discuss how the inclusion of potentially pathogenic variants might affect the AUROC estimates.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Cross-validation results
- **Evidence pointer** Results section "VEP performance on different genes as measured by AUROC is predictable"; Figure 3
- **Issue** The results of the random forest models are presented as Spearman correlations and R-squared values, but the variability of these estimates across the 100 cross-validation runs is not reported. It is unclear how stable the predictions are.
- **Required correction** The authors should report the mean and standard deviation (or confidence intervals) of the performance metrics across the 100 runs.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of feature importance
- **Affected element** SHAP analysis
- **Evidence pointer** Results section "Multiple features contribute to the predictability of AUROC"; Figure 4
- **Issue** The SHAP analysis identifies the most important features, but the direction of the effects is not described in the text. For example, it is stated that genes with higher disorder tend to have higher AUROC, but it is not stated whether the GO terms "Multicellular Organismal Process" and "Developmental Process" are associated with higher or lower AUROC.
- **Required correction** The authors should describe the direction of the effects for the top features, either in the text or in the figure legend.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of alternatives
- **Affected element** AUROC limitations
- **Evidence pointer** Discussion section
- **Issue** The authors correctly identify limitations of AUROC, particularly the inflation due to disorder, but they do not discuss alternative metrics in any detail. The recently introduced AUBPRC is mentioned but not evaluated.
- **Required correction** The authors should briefly discuss whether alternative metrics, such as AUBPRC or precision-recall curves, would be less susceptible to the disorder effect, and whether their conclusions would change if such metrics were used.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation of supplementary data
- **Affected element** Data availability
- **Evidence pointer** Data availability statement
- **Issue** The supplementary dataset is described as providing predictions for the majority of human protein-coding genes, but the format, column names, and how to interpret the predictions are not described.
- **Required correction** The authors should provide a brief description of the supplementary dataset, including the columns and the meaning of the prediction values.

## Risk / unsupported claims
- The claim that intrinsic disorder inflates AUROC is not quantitatively supported in the provided text, as the relevant figures are not visible and the statistical details are incomplete.
- The claim that gene-level features can predict VEP performance is weakened by the circularity of including gnomAD-derived features in the models.
- The practical utility of the predictions for clinical or research applications is not demonstrated.
- The generalizability of the findings beyond the specific set of 963 genes and 35 VEPs is not established.
- The claim that the putatively benign set is "more reflective of the actual clinical utilisation of VEPs" is an assertion that is not directly tested.