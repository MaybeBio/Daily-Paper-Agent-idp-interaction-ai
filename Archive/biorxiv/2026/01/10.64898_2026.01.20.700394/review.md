## Review setup
- **Input scope** Full manuscript text (abstract, background, methods, results, discussion, conclusion, declarations)
- **Assessment boundary** Scientific soundness, methodological rigor, validity of claims relative to presented evidence, and suitability for a general biomedical audience
- **Shared manuscript claim summary** The authors systematically evaluate nine LLPS prediction tools across multiple curated datasets (standard, disordered/folded, mutation, viral) and report that predictor performance is strongly context-dependent, with DeePhase and MolPhase best for overall assessment, PSPHunter best for mutation effects, and structure-informed tools (PSPire, PICNIC) providing value for mutation analysis.
- **Visible evidence base** Abstract, Background, Methods (narrative), Results and Discussion (narrative), Conclusion, Figure legends referenced (Figs 1-7), Table 1 referenced, Additional File 1 referenced
- **Missing materials affecting confidence** Figures 1-7 (actual data plots), Table 1 (predictor details), Additional File 1 (sequence-level scores), exact dataset sizes, statistical test details, predictor version/parameter details, code availability statement

## Reviewer

- **Overall assessment** This manuscript addresses a timely and practically important question: how do currently available LLPS predictors perform across diverse protein contexts? The study design is thoughtful, with multiple curated datasets targeting specific biological scenarios (folded vs disordered, mutation effects, viral proteins). The narrative is clear and the conclusions are appropriately nuanced. However, the manuscript as presented cannot be fully evaluated because all quantitative results are contained in figures and supplementary files that were not provided. The claims of "substantial variability," "reduced accuracy," and "context dependence" rest entirely on data the reviewer cannot see. The methodological descriptions are also insufficiently detailed to assess reproducibility (e.g., exact dataset construction steps, predictor parameter settings, statistical treatment). The work is potentially valuable and publishable if the data support the claims, but the current submission does not allow verification.

- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation, particularly those needing to select computational tools for screening candidate proteins; developers of LLPS prediction algorithms who need benchmarks and identified weaknesses; virologists studying viral replication factories; computational biologists working on protein function prediction. The practical guidance on which tool to use for which question is directly actionable.

- **Major strengths** The study fills a clear gap: no recent unbiased comparison of second- and third-generation LLPS predictors exists. The dataset design is thoughtful, addressing specific known biases (disorder over-reliance, training set composition, underrepresented taxa). The inclusion of mutation-level analysis and viral proteins is novel and practically relevant. The conclusion that predictor choice should depend on the biological question is sensible and well-argued. The authors also highlight the need for better benchmark datasets, which is an important community message.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence availability
- **Claim pointer** The manuscript reports quantitative performance metrics (AUROC, AUPRC) for nine predictors across five datasets and draws comparative conclusions (e.g., "DeePhase and MolPhase provided the most consistently accurate predictions," "PSPHunter reliably predicts mutation impacts").
- **Evidence pointer** Figures 2-6, Table 1, Additional File 1 (none provided in submission)
- **Concern** All quantitative results are contained in figures and a supplementary file that were not included in the submitted material. Without these, the core comparative claims cannot be verified. The narrative describes trends (e.g., "six of the nine predictors showed a decrease in overall AUROC and AUPRC scores") but the actual values, confidence intervals, and statistical significance are absent. The ranking of predictors and the specific claims about which tools are best for which scenario are unsupported in the provided text.
- **Why it matters** The central contribution of this manuscript is the comparative performance data. Without access to the figures and supplementary data, the claims are unverifiable. The reader cannot assess whether the observed differences are meaningful, whether the rankings are robust, or whether the conclusions follow from the data.
- **Resolution test** Provide all figures (2-6) with full axis labels, legend details, and any statistical annotations. Provide Table 1 with predictor details. Provide Additional File 1 or a representative sample. The claims should be re-evaluated with the actual data visible.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological reproducibility
- **Claim pointer** The Methods section describes dataset construction and predictor selection but lacks critical operational details.
- **Evidence pointer** Methods section, "Dataset Construction" and "Selecting Phase Separation Predictors for Evaluation"
- **Concern** The dataset construction description is insufficiently detailed. Specific issues: (1) The "standard dataset" collection from MLOsMetaDB is described but the exact query, date of access, and inclusion/exclusion criteria are not stated. (2) The PISCES-based negative set selection criteria (e.g., resolution cutoff, sequence identity threshold, date) are not given. (3) The disordered negative set from DisProt is mentioned but the selection process is not described. (4) For the mutation dataset, the criteria for selecting the 12 WT proteins and 24 mutations from LLPSDB v2.0 are not stated. (5) For the viral dataset, the selection of 30 LLPS+ sequences from BAV-LLPS-DB and 30 LLPS- sequences from PDB is described only as "filtered as with previous datasets" without specifying the filters. (6) The CD-HIT sequence identity threshold of 40% is stated, but it is unclear whether this was applied within datasets, against training sets, or both. (7) The use of AlphaFold structures for PSPire and PICNIC is mentioned, but the version, confidence filtering, and any quality control are not described.
- **Why it matters** Reproducibility is a core requirement for a methods-focused manuscript. Without precise dataset construction details, other researchers cannot replicate the benchmarks or apply the same protocols to new datasets. The validity of the comparison depends on the datasets being constructed consistently and appropriately.
- **Resolution test** Expand the Methods section to include: exact database versions and access dates, all filtering criteria with numerical thresholds, the number of sequences at each step of the pipeline, and details of AlphaFold structure acquisition and any quality filtering.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor
- **Claim pointer** The manuscript reports AUROC and AUPRC values and makes comparative claims about predictor performance, but no statistical analysis is described.
- **Evidence pointer** Methods section, "Data Analysis and Evaluation Parameters"; Results sections referencing Figures 2-6
- **Concern** The manuscript does not describe any statistical treatment of the performance metrics. It is unclear whether the AUROC/AUPRC values are point estimates from a single dataset split, whether confidence intervals were computed, whether any significance testing was performed (e.g., DeLong test for ROC curves, bootstrap for AUPRC), or whether any multiple-comparison correction was applied. The small size of the mutation dataset (12 WT proteins) and viral dataset (30+30) makes variability a particular concern. The claim that "DeePhase and MolPhase provided the most consistently accurate predictions" implies a consistency analysis that is not described.
- **Why it matters** Without uncertainty quantification, the reader cannot distinguish robust performance differences from noise. The practical recommendation to choose one tool over another should be based on statistically defensible evidence, especially given the small dataset sizes.
- **Resolution test** Add a statistical methods subsection describing how AUROC/AUPRC variability was assessed (e.g., bootstrap resampling, cross-validation), whether significance testing was performed, and how the "consistency" of top performers was determined. Report confidence intervals or variance measures alongside point estimates.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Claim-data alignment
- **Claim pointer** "For overall protein assessment, DeePhase and Molphase provided the most consistently accurate predictions, being the least impacted by structural bias."
- **Evidence pointer** Results sections for Figures 2, 3, and 4
- **Concern** The claim that DeePhase and MolPhase are "least impacted by structural bias" is stated in the abstract and conclusion, but the supporting evidence is not visible. The disordered vs folded analysis (Figure 3) apparently shows performance decreases for most predictors, but the specific comparison between DeePhase/MolPhase and other tools is not described in the text. The claim of "consistently accurate" across datasets is also not substantiated in the narrative; the text notes DeePhase and MolPhase are top performers on the standard dataset, but their relative performance on the benchmark and viral datasets is only partially described.
- **Why it matters** The abstract and conclusion make specific comparative claims that constitute the main practical takeaway of the manuscript. These claims must be directly and visibly supported by the data.
- **Resolution test** In the Results section, explicitly state the AUROC/AUPRC values for DeePhase and MolPhase across all datasets and compare them to the other predictors. Clarify what "least impacted" means quantitatively (e.g., smallest decrease in AUROC from standard to disordered/folded datasets).

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scope justification
- **Claim pointer** The manuscript evaluates nine predictors but excludes two identified tools (PSPredictor and Seq2Phase) for accessibility reasons.
- **Evidence pointer** Methods section, "Selecting Phase Separation Predictors for Evaluation"
- **Concern** The exclusion of PSPredictor and Seq2Phase is justified by accessibility (web interface unavailable; local training requires substantial compute). This is a pragmatic decision, but it means the comparison is not comprehensive. The manuscript should acknowledge this limitation more explicitly in the Discussion, particularly since Seq2Phase is a recent deep learning tool that may be of interest to the community. Additionally, the authors should clarify whether the "nine predictors" claim in the title and abstract is intended to signal comprehensiveness or a representative sample.
- **Why it matters** Readers may assume the nine tools represent the current state of the art. If two known tools are excluded, the scope should be clearly stated to avoid misinterpretation.
- **Resolution test** Add a sentence in the Discussion acknowledging the excluded tools and the potential impact on generalizability. Consider rephrasing the title or abstract to indicate the evaluation covers "nine accessible predictors" rather than implying full coverage.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract, Background
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "LLPS has also being increasingly implicated" contains a grammatical error ("being" should be "been").
- **Required correction** Correct to "LLPS has also been increasingly implicated."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Background, paragraph 1
- **Evidence pointer** Background, first paragraph
- **Issue** The term "biomolecular condensates (BMCs)" is introduced but the abbreviation is not used consistently throughout the text. The manuscript alternates between "BMCs," "condensates," and "membraneless organelles."
- **Required correction** Define the abbreviation at first use and use it consistently, or use "condensates" throughout for readability.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods, "Data Analysis and Evaluation Parameters"
- **Evidence pointer** Methods section, equations
- **Issue** The equations for fold change and the evaluation metrics are referenced but not shown in the text provided. The sentence "In the above equations: TP is true positive..." implies equations were present but they are not visible in the submitted text.
- **Required correction** Ensure all equations are included in the final manuscript and properly numbered.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, "Mutation-level analysis"
- **Evidence pointer** Results section, paragraph on mutation analysis
- **Issue** The sentence "For this study, the protein-level prediction module was used to enable calculation of analysis metrics and direct comparison to other algorithms, rather than the other purpose built-modules" is slightly awkward and could be clearer.
- **Required correction** Rephrase to: "For this study, we used the protein-level prediction module of PSPHunter to enable direct comparison with other predictors, rather than its residue- or region-level modules."

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Declarations, "Availability of data and materials"
- **Evidence pointer** Declarations section
- **Issue** The data availability statement says all data are included in the article and supplementary files, but no statement about code availability is provided. Given the computational nature of the analysis, code availability would be valuable.
- **Required correction** Add a code availability statement, or explicitly state that analysis code is available upon request.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Referencing
- **Affected element** Results, "Reduced Accuracy on Viral Proteins"
- **Evidence pointer** Results section, viral proteins paragraph
- **Issue** The statement "many viruses form replication centres in the cell by large-scale remodelling of cellular membranous organelles such as the Golgi apparatus (67), endoplasmic reticulum (68-71), and lysosomes (72,73)" cites references but the relevance of these references to the specific claim is not clear without seeing the reference list.
- **Required correction** Verify that all cited references are appropriate and relevant to the specific claims made.

- **Technical failings that need to be addressed before the case is established** R1-M1 (evidence availability) and R1-M2 (methodological reproducibility) are blocking. The manuscript cannot be evaluated for scientific soundness without the figures and supplementary data. The methods must be expanded to allow replication. R1-M3 (statistical rigor) is also critical; the comparative claims require uncertainty quantification.

- **Assessment against Nature-style criteria** 
  - Originality: Moderate. The question is important but not entirely new; the novelty lies in the inclusion of third-generation structure-informed predictors and the specific focus on mutation and viral datasets. The field needs such benchmarks, but the approach is not conceptually novel.
  - Scientific importance: High. Practical guidance for tool selection in a rapidly growing field is valuable. The identified limitations (disorder bias, viral underrepresentation) are important for the community.
  - Interdisciplinary readership: Moderate. The topic is of interest to cell biologists, virologists, and computational biologists, but the manuscript is written primarily for a specialist audience familiar with LLPS prediction tools.
  - Technical soundness: Cannot be assessed from the provided material. The study design is reasonable, but the absence of data and statistical detail prevents evaluation.
  - Readability for nonspecialists: The narrative is generally clear and well-structured, but assumes familiarity with LLPS concepts and prediction tool terminology. A brief explanation of what each predictor does (beyond the name) would improve accessibility.

- **Recommendation posture** Supportive if technical concerns are resolved. The study addresses a real need and the design is thoughtful, but the current submission does not provide sufficient evidence to verify the claims. The authors must provide the figures, supplementary data, expanded methods, and statistical analysis before the manuscript can be considered scientifically sound.