## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, methods, results, discussion, limitations, and conclusions. Figures are referenced but not provided in full detail; figure legends are partially available within the text.
- **Assessment boundary** This review evaluates the scientific content, methodological rigor, validity of claims, and presentation quality of the manuscript as submitted. It does not assess editorial fit or journal-specific policy compliance beyond general Nature-style criteria.
- **Shared manuscript claim summary** The authors claim to have developed a 21-gene phase separation-related prognostic signature for gastric cancer that predicts survival, characterizes the immune microenvironment, evaluates immunotherapy response, and identifies natural compounds targeting signature genes, with experimental validation of gene expression in cell lines.
- **Visible evidence base** Transcriptomic data from TCGA-STAD (n=407, 375 tumor/32 normal) and GSE62254 (n=300); four phase separation databases; LASSO regression for model construction; KM survival analysis; ROC analysis; univariate/multivariate Cox regression; nomogram; calibration curves; time-dependent ROC; DCA; GSVA; ssGSEA; TMB analysis; CMap and HERB database screening; molecular docking; qRT-PCR validation in cell lines.
- **Missing materials affecting confidence** Full figures and supplementary files (Additional Files 1-5) were not provided. Detailed results of molecular docking, complete immune infiltration data, and the full list of 78 candidate genes and their selection criteria are not fully described. The specific statistical outputs for many analyses are referenced but not shown.

## Reviewer
- **Overall assessment** The manuscript presents a comprehensive bioinformatics-driven study with a clear workflow, from data integration to model construction, validation, and therapeutic compound identification. The topic is timely and relevant, given the growing interest in phase separation in cancer biology. However, several methodological and conceptual concerns limit the current strength of the claims. The study is largely computational, with only minimal experimental validation (qRT-PCR), and the clinical utility of the signature remains speculative without prospective validation. The connection between the identified genes and phase separation biology is not deeply explored, and the functional relevance of the signature is not experimentally demonstrated. The drug discovery component, while interesting, relies on in silico predictions and docking without functional assays. Overall, the work is a solid hypothesis-generating study but does not yet establish a robust, clinically actionable framework as claimed.

- **Who would be interested in the results, and why** Researchers in gastric cancer genomics and biomarker discovery would find the prognostic model of interest. Investigators studying phase separation in cancer biology may appreciate the attempt to link this biophysical process to clinical outcomes. The immunotherapy response prediction component could attract translational researchers and clinicians interested in precision oncology. The natural compound screening may interest pharmacologists and those exploring repurposing or natural product-based therapies. The study is likely to be of moderate interest to a specialized audience rather than a broad interdisciplinary readership.

- **Major strengths**
  1. The study addresses a relatively unexplored area, phase separation in gastric cancer, which adds novelty to the field.
  2. The methodological workflow is systematic and integrates multiple public datasets and databases, enhancing the robustness of the model development.
  3. The model is validated in an independent cohort, which strengthens the generalizability of the findings.
  4. The inclusion of immune microenvironment characterization and immunotherapy response prediction adds translational relevance.
  5. The drug discovery component, including molecular docking, provides a potential therapeutic angle.

- **Major Concerns**

  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Biological plausibility and mechanistic link
  - **Claim pointer** The manuscript claims that the 21-gene signature is "phase separation-related" and that these genes are functionally connected to phase separation biology in gastric cancer.
  - **Evidence pointer** Methods section "Candidate gene screening and PS-related dataset construction"; Results section "Identification and construction of PS-associated gene signatures in GC"; Figure 1B
  - **Concern** The identification of the 78 candidate genes relies on an intersection of PS-related genes, DEGs, and prognosis-related genes. However, the manuscript does not provide a clear biological rationale for how these specific genes contribute to phase separation processes in gastric cancer. The mere presence in a phase separation database does not establish functional relevance. No experimental evidence is provided to demonstrate that these genes undergo phase separation, that their phase separation behavior is altered in gastric cancer, or that the signature reflects phase separation activity in tumors.
  - **Why it matters** The central premise of the manuscript is that phase separation is a key biological process driving gastric cancer progression. Without functional validation or at least a strong mechanistic link, the signature could simply be a prognostic gene list with no specific connection to phase separation. This weakens the conceptual novelty and the biological interpretation of the model.
  - **Resolution test** The authors should provide experimental evidence, such as immunofluorescence or live-cell imaging, demonstrating phase separation behavior for at least a subset of the signature genes in gastric cancer cell lines. Alternatively, they could perform a functional assay, such as knockdown or overexpression of key signature genes, to show that altering their expression affects phase separation-dependent processes and tumor phenotypes. If experimental validation is not feasible, the authors should temper their claims and explicitly state that the phase separation association is inferred from database annotation only.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Statistical rigor and model validation
  - **Claim pointer** The manuscript claims that the 21-gene risk model "effectively stratifies" patients and demonstrates "consistent performance" in the validation cohort.
  - **Evidence pointer** Results section "Prognostic performance of the PS-related risk model in GC"; Figures 2A, 2B, 3A, 3B
  - **Concern** The AUC values in the validation cohort (GSE62254) are notably lower (0.63 for 3- and 5-year) compared to the training cohort (0.75-0.78). While the authors acknowledge this reduction, they still claim "consistent performance." The drop in AUC suggests potential overfitting in the training cohort. Additionally, the manuscript does not report confidence intervals for the AUC values in the validation cohort, nor does it provide a formal statistical comparison between the training and validation performance. The KM survival analysis in the validation cohort shows a significant p-value, but the HR is lower (1.84 vs 2.96), which may indicate a weaker effect.
  - **Why it matters** A prognostic model that performs substantially worse in an independent cohort has limited clinical utility. The claim of "consistent performance" is not fully supported by the data presented. Overfitting is a common issue in high-dimensional genomic models, and the authors need to demonstrate that their model is not overfitted and that its performance is robust.
  - **Resolution test** The authors should report the 95% confidence intervals for all AUC values in both cohorts. They should also perform a formal test for overfitting, such as a bootstrap-based optimism correction or cross-validation within the training cohort. If the model is overfitted, they should consider simplifying the model or using a more regularized approach. Additionally, they should discuss the clinical implications of the reduced performance in the validation cohort and avoid overstating the model's consistency.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Clinical and translational relevance
  - **Claim pointer** The manuscript claims that the model can "evaluate immunotherapy response" and that the identified natural compounds "provide promising therapeutic options."
  - **Evidence pointer** Results section "Immune landscape and ICI therapy response by PS-related risk stratification in GC"; Results section "Drug repurposing and identification of small-molecule compounds"; Figures 5H, 5I, 7, 8
  - **Concern** The immunotherapy response prediction is based solely on the TIDE algorithm, which is an in silico prediction tool. No actual immunotherapy-treated patient cohort is used to validate the model's ability to predict response. The TIDE score is a surrogate, and its correlation with real clinical response is not established in this study. Similarly, the drug discovery component is entirely computational. The molecular docking results are presented as "high-affinity binding," but no functional assays, such as cell viability or proliferation assays, are performed to demonstrate that these compounds actually inhibit gastric cancer cell growth or modulate the signature genes. The qRT-PCR validation only confirms gene expression differences, not the therapeutic efficacy of the compounds.
  - **Why it matters** The clinical claims are central to the manuscript's translational significance. Without validation in immunotherapy-treated cohorts or functional drug testing, these claims are speculative and could mislead readers into overestimating the clinical readiness of these findings. The gap between in silico prediction and clinical application is substantial.
  - **Resolution test** The authors should either validate the immunotherapy response prediction in an independent cohort of gastric cancer patients treated with immune checkpoint inhibitors, or clearly state that the TIDE-based prediction is hypothesis-generating and requires clinical validation. For the drug discovery component, they should perform at least basic in vitro experiments, such as cell viability assays or apoptosis assays, on gastric cancer cell lines treated with the identified compounds to demonstrate functional activity. If such experiments are not feasible, the claims should be substantially toned down.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Reproducibility and transparency
  - **Claim pointer** The manuscript describes a complex bioinformatics pipeline involving multiple databases, algorithms, and platforms, and claims that the model is "robust."
  - **Evidence pointer** Methods section "Data preparation", "Candidate gene screening and PS-related dataset construction", "PS-related risk model construction and validation"
  - **Concern** The methods section lacks sufficient detail for full reproducibility. For example, the specific parameters for LASSO regression beyond the L1 penalty and cross-validation are not fully described. The criteria for selecting the optimal lambda value are mentioned but not detailed. The "Wu Kong" platform is referenced but its specific role and parameters are unclear. The exact version and parameters for the TIDE algorithm are not specified. The molecular docking protocol, while described, lacks details on the preparation of protein structures, such as protonation states or energy minimization steps.
  - **Why it matters** Reproducibility is a cornerstone of scientific research. Without complete methodological details, other researchers cannot independently replicate the findings, which limits the study's impact and credibility. This is particularly important for bioinformatics studies where small variations in parameters can lead to different results.
  - **Resolution test** The authors should provide a detailed step-by-step description of all computational analyses, including specific R package versions, parameter settings, and any custom code. They should also consider depositing the code and processed data in a public repository to facilitate transparency and reproducibility.

- **Minor Comments**

  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Presentation and clarity
  - **Affected element** Abstract and Introduction
  - **Evidence pointer** Abstract, Background section
  - **Issue** The abstract states that the study "identified 78 candidate genes" and "developed a robust 21-gene risk prediction model," but the transition from 78 to 21 genes is not explained in the abstract. The abstract also uses the term "robust" without providing any performance metrics.
  - **Required correction** Briefly mention the LASSO-based feature selection step in the abstract and include key performance metrics (e.g., AUC values) to support the claim of robustness.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Language and grammar
  - **Affected element** Throughout the manuscript
  - **Evidence pointer** Multiple sections, e.g., Introduction, Discussion
  - **Issue** There are several grammatical errors and awkward phrasings. For example, "benifits" should be "benefits" in the Introduction. The sentence "the establishment of PS-related risk model contribute to earlier mechanistic insights" has subject-verb agreement issues.
  - **Required correction** The manuscript should undergo thorough language editing by a native English speaker or professional editing service.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Figure quality and completeness
  - **Affected element** Figures 1-8
  - **Evidence pointer** Figure legends and references in the text
  - **Issue** The figures are not provided in the manuscript text, and the legends are not fully detailed. For example, Figure 1B is described as a Venn diagram, but the specific numbers in each section are not given in the legend. Figure 8B shows qRT-PCR data, but the statistical test used and the number of biological replicates are not stated in the legend.
  - **Required correction** Provide complete figure legends with all necessary statistical details, sample sizes, and descriptions of all panels. Ensure that all figures are of high resolution and clearly readable.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** References and citations
  - **Affected element** Introduction and Discussion
  - **Evidence pointer** Reference list
  - **Issue** Some statements in the Introduction and Discussion lack specific citations. For example, the claim that "pharmacological disruption of PS has demonstrated promise in suppressing tumor metastasis" is not directly cited. The reference list format should be checked for consistency.
  - **Required correction** Ensure all factual claims are supported by appropriate citations. Verify that the reference list follows the journal's required format.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Data availability
  - **Affected element** Methods section "Data preparation"
  - **Evidence pointer** Data availability statement
  - **Issue** The manuscript does not include a clear data availability statement. While the data are from public databases, the specific accession numbers and processing steps should be clearly stated to allow others to access the same data.
  - **Required correction** Add a data availability statement listing the specific datasets used (e.g., TCGA-STAD, GSE62254) with accession numbers and URLs.

- **Technical failings that need to be addressed before the case is established**
  1. Lack of experimental validation for the phase separation functionality of the signature genes (R1-M1).
  2. Insufficient statistical rigor in model validation, particularly the drop in AUC in the external cohort without formal overfitting assessment (R1-M2).
  3. Overstated clinical claims regarding immunotherapy response prediction and drug efficacy without appropriate validation (R1-M3).
  4. Incomplete methodological details that hinder reproducibility (R1-M4).

## Risk / unsupported claims
- The claim that the 21-gene signature is "phase separation-related" is unsupported by functional evidence; the association is only based on database annotation.
- The claim that the model can "evaluate immunotherapy response" is unsupported by clinical data; TIDE is an in silico prediction tool.
- The claim that the identified natural compounds "provide promising therapeutic options" is unsupported by any in vitro or in vivo functional data.
- The claim of "consistent performance" between training and validation cohorts is weakened by the substantial drop in AUC in the validation cohort.
- The statement that "high-risk patients exhibited significantly greater immune cell infiltration" is presented without clear statistical support or effect sizes in the text.
- The claim that the model "provides a framework for personalized therapy" is speculative without prospective clinical validation.