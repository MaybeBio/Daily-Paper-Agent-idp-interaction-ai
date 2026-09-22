## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv, 2024)
- **Assessment boundary** Scientific content, methodology, claims, and evidence as presented in the provided text; no external data or code were accessed
- **Shared manuscript claim summary** The authors present CSP_Rank, an integrative modeling approach that combines AlphaFold2 (AF2) enhanced sampling methods with Bayesian model selection based on NMR chemical shift perturbation (CSP) data to determine structures of protein-polypeptide complexes. They report that baseline AF2 models of 108 complexes generally agree well with deposited PDB structures, that CSP-based ranking improves agreement with experimental NMR data, and that for two test cases the resulting ensembles fit NOESY data comparably to experimentally derived structures.
- **Visible evidence base** Abstract, Introduction, Methods, Results, Discussion, figure legends (Figures 1–5), Table 1 and Table 2 references, Supplementary Figure and Table references
- **Missing materials affecting confidence** Full figures and supplementary materials (including Supplementary Figures 1–10 and Tables 1–14) were not provided; raw data, code repository contents, and detailed statistical outputs were not accessible; the manuscript is a preprint and has not undergone peer review

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important problem: the integration of machine learning-based structure prediction with sparse experimental NMR data for modeling protein-polypeptide complexes. The proposed CSP_Rank protocol is conceptually sound and the Bayesian framework for model selection is a reasonable extension of existing approaches. The authors have assembled a substantial dataset of 108 complexes, which is a valuable resource. However, the manuscript as presented has several significant limitations. The validation of the method is largely based on comparison to CSP data that were used for selection, and the independent cross-validation is limited to two systems. The description of the clustering and model selection pipeline is incomplete, and the statistical significance of the reported improvements is not established. The claim that AF2 models often outperform PDB models in CSP fit is interesting but requires more careful analysis given the potential for bias in CSP prediction methods. Overall, the work has potential but the evidence presented does not fully establish the superiority or general utility of the CSP_Rank approach over existing methods.

- **Who would be interested in the results, and why** Structural biologists, computational biologists, and NMR spectroscopists interested in integrative modeling of protein complexes, particularly those involving intrinsically disordered peptides. The work is also relevant to developers of machine learning-based structure prediction methods who seek to incorporate experimental data for model validation and refinement. The dataset of 108 complexes with associated CSP data could be a useful benchmark for the community.

- **Major strengths**  
  1. The manuscript addresses a significant gap: the need for experimental validation and refinement of AF2 models, particularly for protein-peptide complexes involving disorder-to-order transitions.  
  2. The compilation of a dataset of 108 protein-peptide complexes with CSP data is a substantial contribution.  
  3. The Bayesian framework for combining CSP data with AF2 confidence metrics is a principled approach.  
  4. The use of multiple ES methods (AFSample, AFSample2, AFAlt) is comprehensive.  
  5. The cross-validation with NOESY data for two systems, while limited, is a valuable demonstration.

- **Major Concerns**

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Validation and overfitting  
- **Claim pointer** The authors claim that "applying enhanced sampling followed by data-guided conformational selection routinely results in ensembles of structures with improved agreement with NMR observables" and that CSP_Rank models "usually fit experimental CSP data better than the corresponding structures available in the PDB or the baseline AF2-multimer models."  
- **Evidence pointer** Results section, Figures 2 and 3, Supplementary Figure 10  
- **Concern** The primary metric used for model selection and evaluation is the CSP_Rank_Score, which is computed from the same CSP data used for selection. This creates a circularity problem: the selected models are chosen to fit the CSP data, so it is not surprising that they fit the CSP data well. The claim of "improved agreement" is therefore not a meaningful validation of model accuracy. The independent cross-validation is limited to only two systems (7JQ8 and 7JYN) using NOESY data, which is insufficient to establish the general utility of the method.  
- **Why it matters** Without independent validation on a larger set of systems, the reported improvements in CSP fit could simply reflect overfitting to the selection data. The method's ability to identify more accurate structures, as opposed to structures that better fit the selection data, is not established.  
- **Resolution test** The authors should provide independent validation on a larger set of systems, for example by using NOESY or RDC data for a substantial subset of the 17 complexes tested. Alternatively, they could use a cross-validation scheme where a subset of CSP data is held out from selection and used only for evaluation. The manuscript should also report the correlation between CSP_Rank_Score and structural accuracy (e.g., RMSD to the PDB structure) for the ES-generated models.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Methodological clarity and reproducibility  
- **Claim pointer** The authors describe a pipeline involving ES methods, clustering, and Bayesian model selection, and state that "the resulting ensembles of protein-peptide complexes usually fit experimental CSP data better than the corresponding structures available in the PDB or the baseline AF2-multimer models."  
- **Evidence pointer** Methods section, "Bayesian model selection score and model selection"; Results section, "Enhanced sampling with AF2"  
- **Concern** The description of the clustering and model selection pipeline is insufficiently detailed. Specifically, the manuscript does not specify: (1) the number of clusters used, (2) the clustering algorithm and its parameters, (3) how the number of models per cluster was determined, (4) the exact formula for the Bayesian score and how the prior and likelihood are normalized, and (5) how the final ensemble size was chosen. The statement that "the most egregious of these physically unreasonable models were identified and removed, as described elsewhere" refers to a manuscript in preparation, which is not acceptable for reproducibility.  
- **Why it matters** The method cannot be reproduced or evaluated by others without these details. The lack of specificity in the model selection procedure undermines confidence in the reported results and prevents the community from applying or benchmarking the method.  
- **Resolution test** The authors should provide a complete, step-by-step description of the pipeline, including all parameters and thresholds. The filtering of physically unreasonable models should be described in sufficient detail or the relevant manuscript should be made available. The code and data should be publicly accessible and documented.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** No  
- **Axis** Statistical analysis and significance  
- **Claim pointer** The authors report that "for ~90% of the protein-peptide complexes in our data set, the CSP_Rank_Scores for AF2 models... are similar or better than the CSP_Rank_Scores of the PDB models."  
- **Evidence pointer** Results section, "Performance of AF2 on protein-peptide complexes"; Figure 1C  
- **Concern** The manuscript does not provide any statistical analysis of the differences in CSP_Rank_Score between AF2, PDB, and CSP_Rank models. No confidence intervals, p-values, or effect sizes are reported. The claim that 90% of AF2 models are "similar or better" is vague, as "similar" is not defined. Furthermore, the distribution of differences is not shown, and it is unclear whether the improvements are consistent across different types of complexes or driven by a few outliers.  
- **Why it matters** Without statistical analysis, the reader cannot assess the reliability or generalizability of the reported improvements. The claim of broad applicability is not supported by the evidence presented.  
- **Resolution test** The authors should provide a statistical comparison of CSP_Rank_Score distributions (e.g., paired tests, effect sizes) between model types. They should also report the distribution of differences and identify any systematic patterns (e.g., by complex type, peptide length, or disorder propensity).

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Comparison to existing methods  
- **Claim pointer** The authors state that "CSP_Rank is a novel method for integrative modeling of protein-peptide complexes" and that it addresses "a significant need in the field for validating computational predictions with realistic experimental data."  
- **Evidence pointer** Abstract, Discussion  
- **Concern** The manuscript does not compare CSP_Rank to existing CSP-guided docking or integrative modeling approaches, such as HADDOCK with CSP restraints, or other methods that combine AF2 with experimental data. The novelty of the approach is therefore not clearly established. The authors mention ColabDock in the Introduction but do not compare their method to it.  
- **Why it matters** To establish the value of the method, it must be compared to existing approaches on the same benchmark datasets. Without such comparisons, the claim of novelty and improved performance is not substantiated.  
- **Resolution test** The authors should benchmark CSP_Rank against at least one or two existing methods (e.g., HADDOCK with CSP restraints, ColabDock) on a subset of their dataset, reporting structural accuracy (e.g., RMSD to PDB) and CSP fit.

- **Minor Comments**

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity of writing  
- **Affected element** Abstract, Introduction  
- **Evidence pointer** Abstract, first paragraph; Introduction, first paragraph  
- **Issue** The abstract and introduction contain some awkward phrasing and grammatical errors (e.g., "determining" instead of "determination" in the Discussion; "protein - peptide" with inconsistent spacing). The writing could be more concise and precise.  
- **Required correction** The manuscript should be carefully edited for grammar and style. For example, "determining 3D structures" should be "determination of 3D structures" or "determining 3D structures" in a grammatically correct context.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Figure quality and accessibility  
- **Affected element** Figures 1–5  
- **Evidence pointer** Figure legends  
- **Issue** The figure legends are referenced but the figures themselves were not provided in the manuscript text. It is unclear whether the figures are of sufficient quality and resolution to support the claims.  
- **Required correction** Ensure that all figures are of publication quality, with clear labels, legends, and appropriate resolution. Consider providing a summary of key results in the text for readers who cannot access the figures.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Data availability  
- **Affected element** Data and code availability  
- **Evidence pointer** Results section, "Dataset of protein-peptide complexes with NMR data"  
- **Issue** The authors state that data and code are available in a GitHub repository, but the URL is not accessible in the provided text (it is a private RPI GitHub instance). The repository contents are not described.  
- **Required correction** Provide a publicly accessible repository URL and a clear description of the contents, including data files, code, and instructions for use.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Terminology  
- **Affected element** Methods, "CSP_Rank_Score"  
- **Evidence pointer** Equation 6  
- **Issue** The CSP_Rank_Score is defined as a weighted average of F1 and MCC, but the weighting scheme is not explained. The formula appears to be an ad hoc combination rather than a statistically motivated score.  
- **Required correction** Clarify the rationale for the weighting scheme and discuss the properties of the score (e.g., its range, sensitivity to class imbalance).

- **Concern ID** R1-m5  
- **Severity** Minor  
- **Axis** References  
- **Affected element** Introduction, Discussion  
- **Evidence pointer** Throughout  
- **Issue** The manuscript cites several recent works on ES methods and AF2 variants, but some key references may be missing (e.g., recent benchmarks of AF2 for protein-peptide complexes, other integrative modeling approaches).  
- **Required correction** Ensure that all relevant literature is cited, particularly recent work on AF2-based complex prediction and CSP-guided docking.

## Risk / unsupported claims
- The claim that CSP_Rank models "usually fit experimental CSP data better than the corresponding structures available in the PDB" is not independently validated and may reflect selection bias.
- The claim that the method has "broad implications for studies of protein-peptide interactions" is speculative and not supported by the limited validation presented.
- The statement that "for ~90% of the protein-peptide complexes in our data set, the CSP_Rank_Scores for AF2 models... are similar or better than the CSP_Rank_Scores of the PDB models" is not statistically substantiated.
- The assertion that the ES methods generate "biophysically plausible" models is not quantitatively supported; the filtering of "physically unreasonable" models is described as being detailed elsewhere, which is not acceptable.
- The generalizability of the method to complexes where CSP data are only available for one partner, or where significant allosteric changes occur, is claimed but not systematically demonstrated.