## Review setup
- **Input scope** Full manuscript text including abstract, main text, methods, and figure legends
- **Assessment boundary** Scientific content, methodological rigor, statistical validity, and clarity of claims as presented in the provided material
- **Shared manuscript claim summary** The authors report the first edition of the CAID experiment, a community-based blind test evaluating 43 methods for predicting protein intrinsic disorder and disordered binding regions on a dataset of 646 proteins from DisProt. They claim that deep learning methods outperform physicochemical approaches, that disordered binding region prediction remains challenging, and that computational costs vary widely among methods.
- **Visible evidence base** Abstract, main text sections (Results, Discussion), Methods, Figures 1-4, Table 1, and references to supplementary materials
- **Missing materials affecting confidence** Supplementary figures and tables referenced throughout (e.g., Supplementary Figs. 3, 4, 6, 7, 10-14, 17-28, 30-35, 38-49, 50, 52, 61, 63-72; Supplementary Tables 4, 6-8) are not provided. Full methodological details for participant methods are not available. Statistical analysis details beyond brief descriptions are not fully specified.

## Reviewer

### Overall assessment
This manuscript describes a valuable community effort to benchmark intrinsic disorder predictors, addressing a significant gap in the field. The experimental design is thoughtful, particularly the use of two reference sets (DisProt and DisProt-PDB) to handle the challenge of defining negative labels. The results are presented clearly, and the identification of top-performing methods provides useful guidance for the community. However, several methodological aspects require clarification, particularly regarding statistical comparisons between methods, the handling of the imbalanced binding dataset, and the interpretation of baseline performance. The claims about deep learning superiority are supported but would benefit from more rigorous statistical testing. The practical recommendations regarding computational efficiency are useful but could be more systematically presented.

### Who would be interested in the results, and why
Computational biologists developing or using disorder prediction tools will find this benchmark essential for method selection and development. Experimental structural biologists studying intrinsically disordered proteins will benefit from guidance on which predictors to use for hypothesis generation. Researchers in protein-protein interaction fields will find the binding site prediction assessment relevant. The community-wide nature of the benchmark and its biennial structure will interest those involved in similar critical assessment efforts in bioinformatics.

### Major strengths
1. The establishment of a community-based blind test fills a critical gap, as no systematic assessment of disorder predictors has been conducted since CASP discontinued its disorder prediction category.
2. The careful construction of reference datasets, particularly the DisProt-PDB set that filters uncertain residues, demonstrates methodological rigor.
3. The inclusion of multiple baselines (PDB Observed, Gene3D, Conservation, Random, Shuffled) provides important context for interpreting predictor performance.
4. The evaluation of both prediction accuracy and computational efficiency addresses practical concerns for large-scale applications.
5. The analysis of fully disordered proteins as a separate category recognizes the unique challenges of this prediction task.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors state that "the best methods use deep learning techniques and notably outperform physicochemical methods" and that top methods are "consistently found among the top five" across different measures.
- **Evidence pointer** Figures 2 and 3, Supplementary Figs. 17, 18, 23, 28, 38, 39, 44, 49
- **Concern** The manuscript reports that differences among top methods are "not statistically significant" (Supplementary Figs. 17, 18, etc.), yet the abstract and main text emphasize the superiority of deep learning methods. The statistical testing methodology is not described in sufficient detail. It is unclear whether the comparisons account for multiple testing, how the bootstrap resampling at the residue level relates to method-level comparisons, and whether the lack of significance among top methods undermines the claim of deep learning superiority.
- **Why it matters** The primary claim of the paper is that deep learning methods outperform others. If the differences are not statistically significant, this claim is weakened. Readers need to understand the statistical framework to properly interpret the rankings and make informed method choices.
- **Resolution test** Provide a clear description of the statistical tests used, including how multiple comparisons are handled. Report effect sizes and confidence intervals for pairwise comparisons between top methods and baselines. If differences among top methods are not significant, temper the language in the abstract and conclusions accordingly.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Dataset representativeness and generalizability
- **Claim pointer** The authors claim the CAID dataset of 646 proteins from DisProt represents a community-based benchmark for disorder prediction.
- **Evidence pointer** Methods section "Reference sets", Figure 1d-f
- **Concern** The dataset is derived solely from DisProt, which may have inherent biases in the types of proteins annotated as disordered. The authors note the strong bias toward model organisms (Figure 1f, Supplementary Fig. 6) but do not discuss how this affects the generalizability of the benchmark results. Additionally, the exclusion of proteins with conflicting annotations or the handling of proteins with partial disorder annotations is not fully described.
- **Why it matters** If the benchmark dataset is not representative of the diversity of disordered proteins across the tree of life or across functional categories, the rankings may not generalize to other application contexts. Users need to understand the dataset composition to assess whether results apply to their specific proteins of interest.
- **Resolution test** Provide a more detailed analysis of dataset composition, including functional annotation enrichment, sequence length distribution, and comparison to the broader DisProt database. Discuss potential biases and their implications for result interpretation. Consider stratifying results by taxonomic or functional groups to assess consistency.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Baseline interpretation
- **Claim pointer** The authors state that "naive baselines are outperformed by predictors since they predict all uncertain residues as disordered, which are all counted as false positives" and that on the DisProt-PDB dataset, "PDB Observed is notably superior to all methods."
- **Evidence pointer** Figures 2 and 3, Discussion section
- **Concern** The interpretation of baseline performance is confusing. On the DisProt dataset, predictors outperform baselines because baselines predict uncertain residues as disordered. On the DisProt-PDB dataset, the PDB Observed baseline outperforms all predictors. This suggests that the choice of reference set dramatically changes conclusions. The authors acknowledge this but do not provide clear guidance on which reference set is more appropriate for different use cases. The statement that "predictors have reached a state of maturity and can be trusted with relative confidence when no experimental evidence is available" seems to contradict the poor performance relative to PDB Observed on the DisProt-PDB set.
- **Why it matters** The choice of reference set fundamentally affects the evaluation outcome. Readers need clear guidance on how to interpret results from each set and which is more relevant for their applications. The apparent contradiction between the two evaluations needs resolution.
- **Resolution test** Provide a more nuanced discussion of when each reference set is appropriate. Clarify whether the PDB Observed baseline performance on DisProt-PDB indicates that simple homology-based approaches are sufficient for identifying structured regions, and what this means for the value of disorder predictors. Consider presenting results stratified by protein type or disorder context.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility and practical guidance
- **Claim pointer** The authors evaluate software implementation aspects including speed and usability, noting that "computing times among methods can vary by up to four orders of magnitude."
- **Evidence pointer** Figure 2c,f, Software Implementation section
- **Concern** While the authors note variability in computational efficiency, they do not provide a systematic framework for users to select methods based on their specific needs (e.g., accuracy vs. speed trade-offs). The description of software issues (hardcoded paths, dependency problems, memory crashes) is anecdotal rather than systematic. No information is provided about the hardware configuration used for timing measurements beyond a general description.
- **Why it matters** For practical applications, users need clear guidance on method selection that balances accuracy and computational cost. The current presentation does not allow readers to make informed trade-offs. Reproducibility of the timing measurements is unclear.
- **Resolution test** Provide a more systematic evaluation of software quality, including a table summarizing key features (e.g., programming language, dependencies, input/output formats, parallelization support). Report timing measurements with clear specifications of hardware and software environment. Consider providing a decision tree or recommendations for different use cases.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** Abstract and Results section
- **Evidence pointer** Abstract, Figures 2 and 3
- **Issue** The term "Fmax" is used without a clear definition in the main text. While it is described as "maximum F1-score across all thresholds," the relationship between Fmax and the precision-recall curve could be explained more explicitly for readers unfamiliar with this metric.
- **Required correction** Add a brief definition of Fmax in the Results section or figure legends, explaining that it represents the maximum harmonic mean of precision and recall achievable across all possible classification thresholds.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Figure readability
- **Affected element** Figures 2 and 3
- **Evidence pointer** Figures 2b-g and 3b-g
- **Issue** The figures contain a large amount of information in small panels, making it difficult to distinguish between methods, especially in the precision-recall and ROC curves. The use of color and line styles may not be accessible to all readers.
- **Required correction** Consider enlarging the panels or splitting into multiple figures. Use distinct line styles in addition to color to differentiate methods. Provide a clear legend that is easy to reference.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Methods section
- **Evidence pointer** Methods section "Statistics"
- **Issue** The description of the bootstrap procedure is brief. It is unclear how the 1,000 resamples are used to calculate confidence intervals and whether these are at the residue level, protein level, or method level.
- **Required correction** Provide a more detailed description of the bootstrap procedure, including what is resampled, how confidence intervals are calculated, and how these relate to the statistical comparisons between methods.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data and code availability statement
- **Evidence pointer** Online content section
- **Issue** The manuscript does not include a clear data and code availability statement. Given the community-oriented nature of this work, it is important to specify where the evaluation data, predictions, and analysis scripts can be accessed.
- **Required correction** Add a data and code availability statement specifying where the CAID dataset, all predictions, and analysis code are deposited and how they can be accessed.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The discussion of limitations focuses primarily on the challenges of defining negative labels and the imbalance in the binding dataset. However, other potential limitations are not addressed, such as the temporal gap between method development and evaluation, potential overfitting of methods to training data that may overlap with the test set, and the limited taxonomic diversity of the dataset.
- **Required correction** Expand the limitations section to address these additional concerns and their potential impact on result interpretation.

### Technical failings that need to be addressed before the case is established
1. Statistical comparison methodology is insufficiently described, and the claim of deep learning superiority is not fully supported by the reported statistical tests (R1-M1).
2. The relationship between the two reference sets (DisProt and DisProt-PDB) and their implications for result interpretation needs clarification (R1-M3).
3. The evaluation of software implementation is anecdotal rather than systematic, limiting its practical utility (R1-M4).

### Assessment against Nature-style criteria
- **Originality** The work is original in establishing a community-based blind test for disorder prediction, filling a gap left by CASP. The biennial structure and community involvement are novel contributions to the field.
- **Scientific importance** The benchmark addresses a critical need in the field, as disorder prediction is widely used but has not been systematically evaluated. The results will influence method development and user choices.
- **Interdisciplinary readership** The topic is relevant to computational biology, structural biology, and molecular biology. The writing is accessible to these audiences, though some statistical details may be challenging for non-specialists.
- **Technical soundness** The experimental design is generally sound, but the statistical analysis requires more rigor and transparency. The handling of the imbalanced binding dataset and the interpretation of baseline performance need clarification.
- **Readability for nonspecialists** The manuscript is generally well-written and accessible. The figures are informative but could be improved for clarity. The abstract effectively summarizes the key findings.

### Recommendation posture
Supportive if technical concerns are resolved. The manuscript presents a valuable community resource and addresses an important gap in the field. However, the statistical framework needs to be more rigorously described and the claims appropriately tempered. The relationship between the two reference sets and the interpretation of baseline performance need clarification. Once these issues are addressed, the manuscript would be suitable for publication.