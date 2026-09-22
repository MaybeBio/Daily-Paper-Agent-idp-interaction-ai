## Review setup
- **Input scope** Full manuscript text (including abstract, introduction, methods, results, discussion, and conclusions)
- **Assessment boundary** Scientific content, methodology, statistical analysis, and interpretation as presented in the provided text
- **Shared manuscript claim summary** The authors assess how AlphaFold2 (AF2) predicts structures of conditionally folding regions (Protean Segments, ProSs) annotated in the IDEAL database, classifying ProSs into three groups based on RMSD between AF2 models and experimental structures, and identifying features that characterize ProSs that agree well with AF2 predictions.
- **Visible evidence base** Main text, figures referenced (Figures 1, 2, 3), tables referenced (Tables 1, S1, S2), supplementary figures referenced (Figures S1–S4), and appendices referenced (Appendices A, B)
- **Missing materials affecting confidence** Supplementary tables (S1, S2), supplementary figures (S1–S4), appendices (A, B), and the full statistical output were not provided. Figure content could not be directly inspected.

## Reviewer
- **Overall assessment** This manuscript addresses a relevant and timely question: whether AF2, trained primarily on folded protein structures, can accurately predict the structures of conditionally folding regions in intrinsically disordered proteins. The authors use the IDEAL database to construct a non-redundant dataset of 207 ProSs and compare AF2 monomeric predictions against experimentally determined complex structures. The finding that approximately one-third of ProSs are well predicted by AF2, and that these can be further subdivided into two groups based on pLDDT and nRG, is potentially useful for the community. However, several methodological aspects require clarification, and the statistical approach has limitations that need to be addressed before the conclusions can be fully supported. The manuscript is generally well-written and accessible, but the analysis would benefit from additional validation and more rigorous treatment of potential confounders.

- **Who would be interested in the results, and why** Researchers working on intrinsically disordered proteins, conditionally folding regions, and protein structure prediction would find this study relevant. The results may also interest developers and users of AF2 who seek to understand its limitations and strengths for disordered proteins. The identification of features that distinguish well-predicted from poorly-predicted ProSs could inform future tool development and guide experimental design for studying IDPs.

- **Major strengths** The study addresses a novel and important question about AF2's applicability to conditionally folding regions. The use of a curated database (IDEAL) with experimentally verified annotations provides a solid foundation. The classification of ProSs into three groups based on RMSD is straightforward and interpretable. The identification of two distinct groups within the well-predicted ProSs, characterized by pLDDT and nRG, is an interesting finding that may have practical implications. The manuscript is clearly written and the figures are well-referenced.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical methodology
- **Claim pointer** The authors claim that 11 features were selected as efficient discriminators between excellent and poor classes based on Mann–Whitney U-test p-values, and that multiple regression analysis identified pLDDT and nRG as the most contributing features.
- **Evidence pointer** Section 2.3, Section 2.4, Section 3.1.1, Section 3.1.2, Table 1, Table S2
- **Concern** The feature selection procedure is not adequately described. The authors state that features with p-values less than 0.01 between excellent and poor classes were selected, but it is unclear whether multiple testing correction was applied. With 38 features tested, the expected number of false positives at alpha = 0.01 is approximately 0.38, which is not negligible. Additionally, the multiple regression analysis appears to have been performed on the full dataset without cross-validation or train/test splitting. The reported R-squared values (0.31 and 0.52 after outlier removal) are modest, and the outlier removal criterion is not clearly defined. The authors should provide more details on the regression diagnostics, including checks for multicollinearity among the 11 features, which is particularly important given the cluster analysis showing correlated features.
- **Why it matters** The statistical validity of the feature selection and regression analysis underpins the central claim that two distinct groups of well-predicted ProSs exist. Without proper multiple testing correction and validation, the identified features may not generalize to new data, and the proposed grouping may be an artifact of overfitting.
- **Resolution test** The authors should apply multiple testing correction (e.g., Benjamini–Hochberg) to the feature selection step, perform cross-validated regression or at least a train/test split, report variance inflation factors for the regression model, and clearly define the outlier removal criterion. If the two-group structure persists under these conditions, the claim would be substantially strengthened.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Dataset and bias
- **Claim pointer** The authors claim that the dataset of 207 ProSs from 164 proteins is non-redundant and representative, and that the classification into excellent, average, and poor classes is meaningful.
- **Evidence pointer** Section 2.1, Section 3.1.1
- **Concern** The dataset construction involves several filtering steps that may introduce bias. ProSs shorter than 10 residues were discarded, and only eukaryotic proteins with AF2 models in AlphaFold DB were included. The redundancy reduction used BlastClust with 30% sequence identity and 90% overlap, but the rationale for these thresholds is not provided. More critically, the classification boundaries for excellent (RMSD ≤ 1.76 Å) and poor (RMSD ≥ 4.13 Å) classes were determined "so that the structural and sequential features of each class were most distinctive using the p-value of the Mann–Whitney U-test." This circular approach, where class boundaries are optimized to maximize feature differences and then the same features are used to characterize the classes, risks overfitting and may inflate the apparent discriminative power of the features. The authors should clarify whether the class boundaries were predetermined or optimized, and if optimized, how this affects the validity of subsequent analyses.
- **Why it matters** If the class boundaries are optimized to maximize feature differences, the subsequent finding that features discriminate between classes is tautological. This would undermine the central conclusion that specific features characterize well-predicted ProSs.
- **Resolution test** The authors should either use predetermined RMSD thresholds (e.g., based on structural biology conventions) or clearly acknowledge the optimization and validate the findings on an independent dataset. Sensitivity analysis with different thresholds would also help establish robustness.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Comparison with experimental structures
- **Claim pointer** The authors compare AF2 monomeric predictions with experimental structures of ProSs bound to their interaction partners, and interpret the RMSD as a measure of prediction accuracy.
- **Evidence pointer** Section 2.2, Section 3.1.4, Section 3.1.5
- **Concern** The comparison between AF2 monomeric predictions and experimental complex structures is conceptually problematic. ProSs undergo disorder-to-order transitions upon binding, meaning their bound conformations may differ substantially from their unbound states. A high RMSD between the AF2 monomeric prediction and the bound experimental structure could reflect either a poor AF2 prediction or the inherent conformational change upon binding. The authors acknowledge this in the Introduction but do not adequately address it in the interpretation. For example, the poor agreement for p21 (RMSD 5.19 Å) may be because the ProS adopts an extended conformation that only becomes structured upon binding, which AF2 cannot predict in the monomeric form. The authors should discuss this limitation more explicitly and consider whether the classification into excellent and poor classes partly reflects the degree of conformational change upon binding rather than AF2's predictive ability.
- **Why it matters** The interpretation of RMSD as a measure of AF2's predictive accuracy for ProSs is confounded by the conformational plasticity inherent to these regions. Without addressing this, the conclusions about AF2's strengths and limitations for ProSs may be misleading.
- **Resolution test** The authors should compare AF2 predictions against unbound experimental structures where available, or at least discuss how the binding-induced conformational change affects the interpretation. They could also analyze whether the degree of conformational change correlates with the classification into excellent and poor classes.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability and external validation
- **Claim pointer** The authors claim that this is the first systematic assessment of AF2 models using experimentally verified conditionally folding IDRs, and that the results provide a new aspect of AF2 models.
- **Evidence pointer** Section 3.2, Section 5
- **Concern** The study is based on a single database (IDEAL) with a relatively small number of ProSs (207). The authors compare their findings with two other studies (Alderson et al., Akdel et al.) but do not perform any external validation of their classification scheme or features on independent datasets. The claim of being "the first systematic assessment" is strong and may be difficult to verify. The authors should consider whether their findings generalize to other databases of conditionally folding regions (e.g., MFIB, DIBS) and whether the identified features are robust across different datasets.
- **Why it matters** The generalizability of the findings is important for the study's impact. If the classification and features are specific to the IDEAL dataset, the conclusions would have limited applicability.
- **Resolution test** The authors should validate their classification and features on an independent dataset of conditionally folding regions, or at least discuss the potential limitations of generalizing from IDEAL alone.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Section 2.2
- **Evidence pointer** Section 2.2
- **Issue** The description of how RMSD thresholds for classification were determined is vague. The authors state that boundaries were decided "so that the structural and sequential features of each class were most distinctive," but the specific procedure is not described.
- **Required correction** Provide a detailed description of the threshold selection procedure, including whether it was an optimization process and what criteria were used to determine "most distinctive."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Section 3.1.2, Table 1
- **Evidence pointer** Section 3.1.2, Table 1
- **Issue** The regression model is described with R-squared and correlation coefficients, but no confidence intervals, p-values for individual coefficients, or measures of model fit (e.g., adjusted R-squared, AIC) are reported.
- **Required correction** Report confidence intervals and p-values for regression coefficients, and include adjusted R-squared or other model fit statistics.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figures 1, 2, 3
- **Evidence pointer** Figures 1, 2, 3
- **Issue** The figures are referenced but could not be inspected. The authors should ensure that all figures are clearly labeled, include appropriate axis labels, and are legible.
- **Required correction** Verify that all figures are self-contained and clearly present the data described in the text.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Section 3.1.4
- **Evidence pointer** Section 3.1.4
- **Issue** The term "group1_HL" is used in the text but the definition is not explicitly stated. It appears to refer to "group1_LH" (long helix) based on context.
- **Required correction** Correct the typo and ensure consistent terminology throughout the manuscript.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Section 5
- **Evidence pointer** Section 5
- **Issue** The conclusions section is brief and does not discuss the limitations of the study, such as the potential bias in dataset construction, the circularity in class boundary selection, or the confounding effect of binding-induced conformational changes.
- **Required correction** Add a limitations paragraph to the conclusions or discussion section.

## Risk / unsupported claims
- The claim that "one-third of AF2 models agreed well with ProS structures" is supported by the data presented, but the generalizability of this proportion to other datasets is not established.
- The claim that the identified 11 features "possibly contribute toward the prediction of ProS structures" is not fully supported, as the regression model explains only 31-52% of variance and no external validation is provided.
- The claim that "this is the first report to systematically assess AF2 models by employing a considerable number of experimentally verified conditionally folding IDRs" cannot be verified from the provided text alone and may be difficult to substantiate.
- The interpretation that group 2 ProSs with relatively low pLDDT but good agreement with AF2 models suggests AF2 can provide good models "regardless of relatively low pLDDT" is interesting but requires further investigation, as the sample size for this subgroup is not reported.
- The comparison with Alderson et al. and Akdel et al. is brief and does not provide sufficient detail to assess the concordance or discordance with these previous studies.