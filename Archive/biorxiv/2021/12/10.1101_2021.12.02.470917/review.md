## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors present PEPPI, a pipeline combining structural similarity, sequence similarity, functional association data, and a naïve Bayesian classifier to predict proteome-wide protein-protein interactions. They report a 4.5% higher AUROC than state-of-the-art methods on a benchmark of 798 ground truth interactions and 798 noninteractions, and a SARS-CoV-2 human interactome application yielding 403 high-confidence interactions covering 73% of a gold standard dataset from PSICQUIC.
- **Visible evidence base** Abstract text only; no quantitative details beyond AUROC improvement, benchmark size, interaction count, and coverage percentage
- **Missing materials affecting confidence** Full methods, benchmark construction details, definition of ground truth and noninteractions, feature engineering, classifier training and validation procedures, statistical significance tests, comparison method configurations, SARS-CoV-2 dataset details, gold standard composition, and software implementation specifics

## Reviewer
- **Overall assessment** The abstract presents a potentially useful integrative approach for proteome-wide protein-protein interaction prediction, with a plausible combination of diverse data types. However, the evidence provided is insufficient to evaluate the technical soundness of the method, the validity of the benchmark, or the robustness of the reported performance gains. The SARS-CoV-2 application is interesting but lacks critical context for assessing its significance. The claims are not currently established from the supplied material.
- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein-protein interaction prediction, systems biology researchers studying interactome networks, and virologists interested in host-pathogen interactions, particularly SARS-CoV-2. The tool's availability as a webserver and standalone version may appeal to experimentalists seeking computational screening support.
- **Major strengths** The proposed integration of structural, sequence, and functional data is conceptually reasonable and addresses a recognized gap in the field. The reported benchmark includes a balanced set of interactions and noninteractions, which is a positive design choice. The application to SARS-CoV-2 human interactions demonstrates a practical use case with potential biological relevance.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria**  
  - Originality: The combination of data types is not entirely novel, as similar integrative approaches exist, but the specific pipeline configuration may offer incremental novelty. This cannot be fully assessed without methods.  
  - Scientific importance: Proteome-wide interaction prediction is a significant problem, and improved accuracy would be valuable. However, the claimed improvement is modest and not statistically contextualized.  
  - Interdisciplinary readership: The topic bridges computational biology and virology, which could attract a broad audience, but the abstract does not provide enough biological insight to engage nonspecialists.  
  - Technical soundness: Not assessable from the abstract alone. The benchmark design, classifier implementation, and evaluation methodology are critical and unverified.  
  - Readability for nonspecialists: The abstract is generally clear but uses technical terms without sufficient explanation, and the significance of the results is not framed for a general scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. Supportive if technical concerns are resolved through full manuscript review.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** "PEPPI attains 4.5% higher AUROC than the best of other state-of-the-art methods"  
- **Evidence pointer** Abstract, benchmark description; location not provided  
- **Concern** The abstract reports a single AUROC improvement of 4.5% over the best comparator, but no details are given on which methods were compared, how they were configured, whether the difference is statistically significant, or what variance exists across benchmark splits.  
- **Why it matters** A single metric without statistical context cannot establish superiority. The choice of comparators and their tuning heavily influences such comparisons, and the claim may not generalize.  
- **Resolution test** Provide full benchmark details, including comparator versions, hyperparameters, cross-validation strategy, and statistical tests (e.g., confidence intervals or p-values) for the AUROC difference.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** "benchmarking against a set of 798 ground truth interactions and an equal number of noninteractions"  
- **Evidence pointer** Abstract, benchmark description; location not provided  
- **Concern** The construction of the ground truth and noninteraction sets is not described. It is unclear how interactions were curated, whether they are experimentally verified, how noninteractions were defined, and whether the sets are independent of the training data.  
- **Why it matters** Benchmark quality directly determines the validity of all performance claims. Biased or circular benchmarks can inflate accuracy and mislead users.  
- **Resolution test** Describe the source and curation of the interaction and noninteraction sets, including any filtering criteria, and confirm no overlap with training data.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** "PEPPI integrates structural similarity, sequence similarity, functional association data, and machine learning-based classification through a naïve Bayesian classifier model"  
- **Evidence pointer** Abstract, method description; location not provided  
- **Concern** The abstract does not specify how each data type is represented, how features are computed, how missing data are handled, or how the naïve Bayesian model combines these heterogeneous inputs.  
- **Why it matters** Without this information, the method cannot be reproduced or evaluated for methodological soundness. The integration strategy is central to the claimed performance.  
- **Resolution test** Provide a detailed methods section covering feature extraction, normalization, missing data handling, and the classifier formulation.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Scientific importance  
- **Claim pointer** "predictions covering 73% of a gold standard dataset from PSICQUIC and demonstrating significant complementarity with the most recent high-throughput experiments"  
- **Evidence pointer** Abstract, SARS-CoV-2 application; location not provided  
- **Concern** The abstract does not define the gold standard dataset, the criteria for high-confidence predictions, or the basis for claiming complementarity. The biological significance of the 403 predicted interactions is not discussed.  
- **Why it matters** The SARS-CoV-2 application is a key demonstration of utility, but without context, the coverage and complementarity claims are uninterpretable and may not reflect biological relevance.  
- **Resolution test** Specify the gold standard source, prediction confidence threshold, and provide a comparison with experimental datasets, including any functional enrichment or validation analyses.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Readability  
- **Affected element** Abstract, first sentence  
- **Evidence pointer** Abstract, opening statement; location not provided  
- **Issue** The phrase "formidable task" is vague and does not quantify the scale of the problem or the limitations of existing methods.  
- **Required correction** Replace with a specific statement about the number of potential interactions or the coverage gap in current experimental methods.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Software availability statement  
- **Evidence pointer** Abstract, final sentence; location not provided  
- **Issue** The abstract states that PEPPI is available as a webserver and standalone version, but no URL, license, or system requirements are provided.  
- **Required correction** Include a link to the software repository and specify the license and supported platforms.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Scientific importance  
- **Affected element** SARS-CoV-2 application  
- **Evidence pointer** Abstract, application description; location not provided  
- **Issue** The abstract does not state how many of the 403 predicted interactions are novel or previously known, which limits the assessment of added value.  
- **Required correction** Provide a breakdown of known versus novel interactions and discuss the potential biological implications of the novel predictions.

## Risk / unsupported claims
- The 4.5% AUROC improvement over state-of-the-art methods is unsupported without statistical significance testing and comparator details.
- The benchmark of 798 interactions and 798 noninteractions is unverifiable without curation and independence details.
- The SARS-CoV-2 coverage claim of 73% of a gold standard dataset is uninterpretable without dataset definition and prediction threshold.
- The claim of "significant complementarity" with high-throughput experiments is unsupported without comparative analysis.
- The general applicability of PEPPI as a "powerful" tool is an assertion not backed by evidence in the abstract.