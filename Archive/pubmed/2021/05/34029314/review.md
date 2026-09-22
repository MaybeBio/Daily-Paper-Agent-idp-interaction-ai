## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion) without figures, tables, or supplementary materials
- **Assessment boundary** Evaluation of the manuscript's claims, methodology, and conclusions based solely on the provided text
- **Shared manuscript claim summary** The authors evaluate 18 residue-residue contact prediction methods across three datasets (610 proteins, 215 proteins, 32 CASP13 targets) from multiple perspectives, including contact density, model probability, physicochemical interactions, secondary structure, multi-domain proteins, runtime, and application to 3D structure reconstruction. They report that multi-input deep learning methods perform best overall, particularly for low-contact-density proteins, while ECA methods excel at detecting salt bridges and disulfide bonds. They also identify limitations including sensitivity to shallow MSAs, inter-domain prediction challenges, and runtime inefficiencies.
- **Visible evidence base** Text descriptions of results referencing Figures 1-12, Tables 1-2, and Supplementary Figures/Tables S1-S12; no actual data values, figures, or tables are visible
- **Missing materials affecting confidence** All figures, tables, and supplementary materials are referenced but not provided; detailed numerical results, statistical analyses, and methodological parameters are absent; the exact composition of the test sets and the implementation details of the 18 methods are not fully described

## Reviewer
- **Overall assessment** This manuscript presents a comprehensive and timely evaluation of residue-residue contact prediction methods, spanning traditional machine learning, evolutionary coupling analysis, and deep learning approaches. The scope is ambitious and the multi-perspective analysis is commendable. However, the absence of visible data, figures, and tables severely limits the ability to verify the claims made. The methodological descriptions are incomplete in several critical areas, particularly regarding dataset construction, statistical testing, and the specific implementations of the evaluated methods. The conclusions are plausible and align with the broader literature, but the evidence base as presented is insufficient to fully establish the case.
- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein structure prediction would find this assessment valuable for method selection and benchmarking. Developers of contact prediction methods would benefit from the comparative analysis and identified limitations. Researchers studying protein evolution and co-evolutionary signals would be interested in the physicochemical interaction analysis. The practical guidance on method selection based on MSA depth and protein type would be useful for structural biologists applying these tools.
- **Major strengths** The manuscript addresses a significant gap in the literature by providing a large-scale, multi-perspective comparison of contact prediction methods. The inclusion of diverse protein types, including intrinsically disordered and multi-domain proteins, is a notable strength. The analysis of physicochemical interactions and secondary structure preferences adds depth beyond simple accuracy metrics. The application to 3D structure reconstruction provides practical relevance. The discussion of runtime and scalability considerations is valuable for real-world applications.
- **Major Concerns** The most significant concern is the complete absence of visible data, figures, and tables, making it impossible to verify any of the reported results. The methodological descriptions lack critical details, including the exact criteria for dataset selection, the parameters used for each method, and the statistical significance of observed differences. The claim that "no single tool is dominant" is not supported by any quantitative comparison. The analysis of model probability reliability is described qualitatively without supporting data. The runtime comparison is limited to only 5 deep learning methods, which is a narrow subset. The CASP13 evaluation uses only 32 domains, which may not be statistically robust.
- **Technical failings that need to be addressed before the case is established** The manuscript lacks visible numerical results, statistical analyses, and methodological details necessary to evaluate the claims. The dataset construction process is not fully described, and the criteria for selecting the 610 proteins and 32 CASP13 targets are unclear. The implementation details of the 18 methods, including version numbers and parameter settings, are not provided. The statistical significance of performance differences between methods is not reported. The correlation analysis between contact prediction precision and structure quality is described but not quantified.
- **Assessment against Nature-style criteria** Originality: The manuscript offers a comprehensive multi-perspective evaluation that extends beyond previous assessments, but the individual perspectives are not entirely novel. Scientific importance: The topic is highly relevant to the protein structure prediction community, and the practical guidance is valuable. Interdisciplinary readership: The manuscript would appeal to computational biologists, structural biologists, and bioinformaticians, but the technical depth may limit broader appeal. Technical soundness: The methodology appears reasonable in design, but the lack of visible data and statistical rigor prevents full assessment. Readability for nonspecialists: The manuscript is generally well-written and accessible, though some sections assume familiarity with the field.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important topic with a comprehensive approach, but the current evidence base is insufficient to fully establish the claims. The authors must provide the actual data, figures, and tables, along with detailed methodological descriptions and statistical analyses, before the case can be considered established.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence availability
- **Claim pointer** The manuscript reports comprehensive evaluation results across multiple perspectives, including prediction precision, model probability reliability, physicochemical interaction coverage, and structure reconstruction quality.
- **Evidence pointer** Figures 1-12, Tables 1-2, Supplementary Figures S1-S12, location not provided
- **Concern** All figures, tables, and supplementary materials are referenced but not visible in the provided manuscript. The results section consists entirely of textual descriptions without any numerical data, statistical analyses, or visual representations. This makes it impossible to verify any of the reported findings or assess the magnitude of observed effects.
- **Why it matters** The core claims of the manuscript, including the superiority of multi-input DL methods and the differential performance of ECA methods for salt bridges, cannot be evaluated without the actual data. The absence of visible evidence prevents any meaningful assessment of the manuscript's validity.
- **Resolution test** The authors must provide all figures, tables, and supplementary materials with complete numerical data, including precision values, confidence intervals, and statistical significance tests.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological completeness
- **Claim pointer** The manuscript claims to evaluate 18 contact prediction methods on three datasets with consistent inputs and fair comparison conditions.
- **Evidence pointer** Materials and methods, Section "Benchmark data set", location not provided
- **Concern** The dataset construction process is not fully described. The criteria for selecting the 610 proteins from the initial 3136 PDB chains are unclear beyond sequence identity and resolution thresholds. The process for identifying and excluding proteins similar to CASP13 training sets is not described. The selection of the 32 CASP13 domains and the exclusion of multi-domain targets are not justified. The exact composition of TestSet2 (215 proteins) and its relationship to TestSet1 are not fully explained.
- **Why it matters** The validity of the comparative evaluation depends critically on the quality and representativeness of the benchmark datasets. Without clear selection criteria, the results may be biased or non-generalizable.
- **Resolution test** The authors must provide a detailed description of the dataset construction process, including the exact filtering criteria, the number of proteins excluded at each step, and the rationale for these decisions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The manuscript reports performance differences between method categories, such as DL methods outperforming ECA methods for low-contact-density proteins and ECA methods detecting more salt bridges.
- **Evidence pointer** Results, Sections 3.1-3.8, location not provided
- **Concern** No statistical tests are described or reported to support the claimed performance differences. The manuscript does not report confidence intervals, p-values, or effect sizes for any comparison. The variability across proteins within each category is not quantified beyond occasional mentions of standard deviations. The claim that "no single tool is dominant" requires a formal statistical demonstration of performance equivalence or trade-offs.
- **Why it matters** Without statistical rigor, the observed differences could be due to random variation, particularly given the limited number of proteins in some categories (e.g., only 6 IDR proteins and 9 TM proteins). The conclusions may not be robust.
- **Resolution test** The authors must perform and report appropriate statistical tests (e.g., paired tests across proteins, multiple comparison corrections) for all key comparisons, and provide effect sizes and confidence intervals.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Method implementation details
- **Claim pointer** The manuscript evaluates 18 methods, including traditional ML, ECA, consensus ML, and DL approaches, with specific version and parameter settings.
- **Evidence pointer** Supplementary Table S1, location not provided
- **Concern** The implementation details of the 18 methods are not described in the visible text. It is unclear whether the authors used the original implementations, re-implemented the methods, or used third-party packages. The specific versions, training datasets, and parameter settings for each method are not provided. The criteria for selecting these particular 18 methods as "representatives" are not justified.
- **Why it matters** The reproducibility of the evaluation depends on precise implementation details. Different versions or parameter settings can significantly affect performance, and the choice of methods may bias the conclusions.
- **Resolution test** The authors must provide complete implementation details for all 18 methods, including software versions, training data, and all relevant parameters, either in the main text or supplementary materials.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of conclusions
- **Claim pointer** The manuscript concludes that multi-input DL methods are the best choices for low-contact-density proteins and that methods relying only on MSA as input can achieve comparable performance to multi-input methods when Neff > 5L-8L.
- **Evidence pointer** Results, Sections 3.4-3.5, Discussion, location not provided
- **Concern** The conclusions are based on a specific set of 18 methods and three datasets. The generalizability of these findings to other methods, newer architectures, or different protein families is unclear. The CASP13 evaluation uses only 32 domains, which may not be representative of the diversity of protein structures. The analysis of intrinsically disordered proteins is based on only 6 proteins.
- **Why it matters** The manuscript aims to provide guidance for method selection, but the limited scope of the evaluation may not support broad conclusions. Users may make inappropriate method choices based on findings that do not generalize.
- **Resolution test** The authors should acknowledge the limitations of their dataset and method selection more explicitly, and temper their conclusions accordingly. Additional validation on independent datasets or newer methods would strengthen the claims.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of definitions
- **Affected element** Contact density definition
- **Evidence pointer** Materials and methods, Section "Definition of contact and contact density", location not provided
- **Issue** The definition of contact density is given as the total number of non-local contacts divided by protein length, but the rationale for this normalization is not explained. Different normalizations (e.g., by number of residue pairs) could yield different results.
- **Required correction** Provide a brief justification for the chosen normalization and discuss its potential impact on the results.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of runtime analysis
- **Affected element** Runtime comparison
- **Evidence pointer** Results, Section 3.10, location not provided
- **Issue** The runtime comparison is limited to 5 DL methods and does not include ML or ECA methods for context. The hardware configuration is described, but the software environment (e.g., operating system, library versions) is not specified.
- **Required correction** Include runtime data for representative ML and ECA methods for comparison, and specify the complete software environment.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of structure reconstruction results
- **Affected element** Section 3.11
- **Evidence pointer** Results, Section 3.11, location not provided
- **Issue** The manuscript reports that higher contact prediction precision does not always lead to better structure reconstruction, but the explanation is speculative. The relationship between contact precision and TM-score is not quantified.
- **Required correction** Provide a quantitative analysis of the correlation between contact precision and TM-score, and discuss potential confounding factors.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Evidence pointer** Discussion, location not provided
- **Issue** The manuscript does not discuss the potential impact of using a single MSA generation method (JackHMMER against nr) on the results. Different MSA generation strategies could affect method performance.
- **Required correction** Add a discussion of the sensitivity of the results to MSA generation parameters and the potential for different conclusions with alternative MSA strategies.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility of the analysis
- **Affected element** Data and code availability
- **Evidence pointer** Supporting information, location not provided
- **Issue** The manuscript states that prediction results are available at a URL, but does not mention the availability of analysis scripts or code for reproducing the figures and tables.
- **Required correction** Provide a statement on code availability and consider depositing analysis scripts in a public repository.

## Risk / unsupported claims
- The claim that "multi-input DL methods are the best choices for low-contact-density proteins" is not supported by visible data, as no numerical results are provided.
- The claim that "methods that rely only on MSA as input can reach comparable achievements as methods that adopt multi-input sources" when Neff > 5L-8L is not verifiable without the underlying data.
- The claim that "ECA methods can detect more secondary structure interactions" is not supported by quantitative evidence in the visible text.
- The claim that "DL methods can predict more hydrophobic interactions while ECA methods predict more salt bridges and disulfide bonds" is presented without supporting data.
- The claim that "strong prediction similarities between DL methods" is based on Jaccard indices that are not visible.
- The claim that "top L predicted contacts are most correlated with the quality of final protein models" is not supported by the correlation coefficients or statistical tests, which are not provided.
- The runtime comparison conclusions are not fully supported as only 5 DL methods are compared without context from other method categories.
- The generalizability of the findings to other methods or newer architectures is not established and should be treated as speculative.