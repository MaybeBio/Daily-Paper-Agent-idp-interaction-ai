## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Database utility, prediction methodology, validation approaches, biological claims, and overall contribution as presented in the provided text
- **Shared manuscript claim summary** The authors present ricePSP, a database of rice phase separation-associated proteins (PSPs), built by applying PSPredictor and MolPhase to 66,338 annotated rice proteins, identifying 10,654 PSPs and 1,394 prion-like domain-containing proteins. Validation is claimed through AlphaFold structure predictions (negative correlation between PS scores and pLDDT) and in vivo condensate imaging in rice protoplasts for selected flowering-related candidates. A case study on flowering regulation is presented as proof of concept.
- **Visible evidence base** Main text, Figure legends (Figs. 1–4), Table 1, Supplementary figure/table legends
- **Missing materials affecting confidence** Actual database interface and functionality (not assessable from text), full supplementary tables (S1–S4), supplementary figures (S1–S4), detailed methods for PSPredictor and MolPhase parameter settings, raw imaging data, statistical details for enrichment analyses, code repository contents

## Reviewer
- **Overall assessment** The manuscript describes a potentially useful community resource for rice phase separation research. The computational pipeline is straightforward and the integration of multiple prediction tools is sensible. However, the validation strategy is limited in scope and depth, and several claims regarding biological significance and database utility are not fully supported by the evidence presented. The flowering case study is suggestive but preliminary. The manuscript would benefit from clearer benchmarking against existing resources, more rigorous statistical treatment, and additional experimental validation.
- **Who would be interested in the results, and why** Plant molecular biologists studying phase separation, rice functional genomics researchers, and crop scientists interested in stress responses and flowering regulation. The database could serve as a hypothesis-generating tool for identifying candidate PSPs in rice and related crops.
- **Major strengths** 1) Addresses an under-explored area (phase separation in crops) with potential agricultural relevance. 2) Integrates multiple prediction tools and provides a user-friendly web interface with searchable modules. 3) The combination of computational prediction with AlphaFold structural validation and in vivo imaging for selected candidates is a reasonable multi-pronged approach. 4) The flowering case study connects predictions to a biologically important process.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (validation scope), R1-M2 (benchmarking), R1-M3 (statistical rigor), R1-M4 (database accessibility)
- **Assessment against Nature-style criteria** **Originality:** Moderate. The application of existing prediction tools to rice is novel, but the methodological approach is not conceptually new. **Scientific importance:** Moderate. A rice PSP database could be valuable, but the biological insights presented are preliminary. **Interdisciplinary readership:** Limited. Primarily of interest to plant biologists and phase separation researchers; the broader cell biology community may find the crop focus narrow. **Technical soundness:** Partially adequate. The prediction pipeline is reasonable, but validation depth and statistical rigor are insufficient. **Readability for nonspecialists:** Acceptable. The manuscript is generally clear, though some sections assume familiarity with phase separation concepts.
- **Recommendation posture** Supportive if technical concerns are resolved. The resource has potential value, but the current evidence does not fully establish the database's reliability or the biological claims made.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation adequacy
- **Claim pointer** "The predicted PSPs could be invariably validated by protein structure data and in vivo condensate imaging assays."
- **Evidence pointer** Figure 3, Figure 4C, Supplementary Figure S4
- **Concern** The claim of "invariably validated" is not supported by the evidence presented. Only a small number of candidates (six flowering-related proteins) were tested by in vivo imaging, and the structural validation relies on a correlation analysis (R2 = 0.4224) that explains less than half of the variance. No negative controls are described for the imaging experiments, and no quantification of condensate frequency, size, or dynamics is provided. The generalizability of the validation to the full set of 10,654 predicted PSPs is unclear.
- **Why it matters** The central value of the database depends on the reliability of its predictions. Without systematic validation across diverse protein families and functional categories, users cannot assess the false positive rate or the confidence they should place in individual predictions.
- **Resolution test** Provide a more extensive validation set, including proteins with a range of PS scores (including low-scoring controls), quantitative imaging data (e.g., condensate number, size, fluorescence recovery after photobleaching), and a clear statement of how many predicted PSPs were experimentally tested versus how many were confirmed. Alternatively, benchmark against experimentally validated PSP datasets from other species.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Benchmarking and comparison
- **Claim pointer** "To evaluate the performance of ricePSP predictions, we compared the PSPredictor results with two other prediction tools, PLAAC and MolPhase."
- **Evidence pointer** Figure 2A and 2B
- **Concern** The comparison with PLAAC and MolPhase is descriptive (Venn diagrams) rather than evaluative. No metrics of agreement (e.g., correlation coefficients, Matthews correlation coefficient) or benchmarks against known experimentally validated PSPs are provided. The statement that "not all PrDPs necessarily exhibit PS potential" is presented as a finding, but without a gold standard, the relative performance of the tools cannot be assessed.
- **Why it matters** A database's utility depends on the accuracy of its predictions. Without benchmarking against known positives and negatives, users cannot determine whether the PSPredictor threshold (0.7) is appropriate or whether the database offers advantages over simply running the tools independently.
- **Resolution test** Include a benchmarking analysis against experimentally validated PSPs from Arabidopsis or other organisms, report sensitivity and specificity at different score thresholds, and provide a rationale for the chosen cutoff. Consider comparing against additional prediction tools (e.g., catGRANULE, PScore, IUPred) to position ricePSP within the existing landscape.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim** "LPSPs had significantly higher pLDDT values (median = 82.42) than HPSPs (median = 62.36) (p < 2.22 × 10−16)"
- **Evidence pointer** Figure 3D
- **Concern** The statistical test used to obtain the reported p-value is not described. Given the large sample size (66,338 proteins), even trivial differences would reach statistical significance. The effect size and biological relevance of the difference are not discussed. Additionally, the classification into HPSP and LPSP is not clearly defined (what score threshold separates the two groups?).
- **Why it matters** The correlation between PS scores and pLDDT is a key validation pillar. Without proper statistical reporting, the strength of this relationship cannot be evaluated, and the claim of structural validation is weakened.
- **Resolution test** Specify the statistical test used, report effect sizes (e.g., Cohen's d), and provide the classification criteria for HPSP and LPSP. Consider stratifying the analysis by protein family or functional category to assess whether the correlation holds across diverse protein types.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Database accessibility and functionality
- **Claim** "ricePSP database may serve as a valuable resource for protein function research"
- **Evidence pointer** Figure 1B, "Construction and content" section
- **Concern** The manuscript describes the database structure and modules, but the actual URL is not provided in the text (only the GitHub repository for the prediction pipeline is mentioned). The functionality of the search, filtering, and download features cannot be assessed from the manuscript. The claim that the database is "user-friendly" is not verifiable.
- **Why it matters** A database paper's primary contribution is the resource itself. If the database is not accessible or its functionality is not demonstrated, the manuscript's core value proposition is undermined.
- **Resolution test** Provide the database URL in the manuscript, include screenshots or a detailed walkthrough of the user interface, and demonstrate the search and download features with concrete examples. Consider including a "quick start" guide or tutorial video.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract and Introduction
- **Evidence pointer** "Background" section
- **Issue** The term "PS" is used interchangeably for "phase separation" and "PS score" without consistent definition. The abbreviation "PSP" is introduced but the distinction between "PSPs" (proteins) and "PS scores" (numerical values) could be clearer.
- **Required correction** Define all abbreviations at first use and maintain consistent terminology throughout. Consider using "phase separation propensity score" instead of "PS score" at first mention.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods
- **Evidence pointer** "Phase separation and prion-like domain prediction" section
- **Issue** The specific parameters and versions of PSPredictor, MolPhase, and PLAAC are not provided. The manuscript states the pipeline is on GitHub, but the exact commands and settings are not described.
- **Required correction** Include a detailed methods subsection or supplementary methods file describing software versions, parameters, and any custom modifications. This is essential for reproducibility.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Table 1
- **Evidence pointer** Table 1
- **Issue** The table lists Arabidopsis PSPs and their rice homologs with scores, but the criteria for selecting these particular Arabidopsis proteins are not stated. The table appears to be a curated list, but the selection process is unclear.
- **Required correction** State the criteria for inclusion in Table 1 (e.g., experimentally validated in Arabidopsis, involvement in stress responses). Consider adding a column indicating the evidence type for each Arabidopsis PSP.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** "PS-associated regulatory module in rice flowering" section
- **Evidence pointer** Figure 4B
- **Issue** The network analysis is described as revealing a "densely connected regulatory module," but no network statistics (e.g., number of edges, clustering coefficient, enrichment p-values) are provided. The network appears to be based on known protein-protein interactions, but the source of these interactions is not specified.
- **Required correction** Provide network construction details, including the interaction data source, and report basic network statistics. Clarify whether the network is based on experimental data or predicted interactions.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Language
- **Affected element** Throughout
- **Evidence pointer** "Construction and content" section
- **Issue** Some sentences are overly long and contain redundant phrasing. For example, "This static site generation approach allows ricePSP to be hosted efficiently on the GitHub Pages without requiring a backend server" could be simplified.
- **Required correction** Revise for conciseness and clarity. Consider having a native English speaker review the manuscript.

## Risk / unsupported claims
- The claim that predicted PSPs are "invariably validated" is not supported by the limited experimental and structural evidence presented.
- The statement that "LLPS could act as a central organizing principle for photoperiodic flowering regulation in rice" is speculative and goes beyond the data presented, which only shows that some flowering proteins have high PS scores and can form condensates.
- The claim that the database "may serve as a valuable resource" is reasonable but unproven without demonstrated usage or benchmarking against existing resources.
- The assertion that "most" rice homologs of stress-related Arabidopsis PSPs exhibit high PS scores is not quantified; the table shows scores but no summary statistics are provided.
- The functional significance of the observed condensates (e.g., whether they are involved in flowering regulation) is not experimentally tested, so the biological relevance of the case study remains correlative.