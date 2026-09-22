## Review setup

- **Input scope** Abstract and short description only
- **Assessment boundary** Claims presented in the abstract and short description; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors propose a workflow combining AlphaFold2 via ColabFold with a MiniPAE scoring metric to identify SLiM-mediated protein-protein interactions, benchmark this approach against AlphaFold3, and introduce a proximity labeling-based validation assay. The workflow is applied to predict SLiMs binding to RSK2.
- **Visible evidence base** Abstract text, short description, short abstract, author affiliations, and a GitHub URL for MiniPAE
- **Missing materials affecting confidence** Full manuscript text, all figures and tables, benchmark datasets, statistical analyses, code implementation details, validation assay protocols, and experimental results

## Reviewer

- **Overall assessment** The abstract presents a potentially useful methodological contribution to the SLiM prediction field, but the evidence base available for review is limited to the abstract and short description. The core claims regarding benchmark performance, workflow utility, and validation sensitivity cannot be independently assessed without access to the full manuscript, figures, and underlying data. The concept of using AlphaFold with a novel scoring metric for SLiM discovery is timely and of interest to the structural biology and molecular interaction communities, but the current submission does not provide sufficient detail to evaluate technical soundness or reproducibility.
- **Who would be interested in the results, and why** Researchers studying protein-protein interactions, particularly those focused on intrinsically disordered regions and SLiM-mediated signaling. Computational biologists developing or applying structure prediction tools for interaction discovery. Virologists and cell biologists interested in host-pathogen interactions, given the authors' stated context. The workflow's accessibility via Colab notebooks may appeal to experimental laboratories without dedicated bioinformatics infrastructure.
- **Major strengths** The proposed approach addresses a recognized gap in SLiM detection, which is challenging due to the small size, degeneracy, and transient nature of these motifs. The emphasis on evaluating AlphaFold's capacity independent of model quality is a thoughtful distinction from prior work. The provision of a no-installation, cost-effective workflow via Colab enhances accessibility. The introduction of a proximity labeling-based validation method addresses a practical bottleneck in SLiM confirmation.
- **Major Concerns** The abstract claims superior performance of AlphaFold2 with MiniPAE over AlphaFold3, but no benchmark details, statistical significance measures, or comparison criteria are provided. The workflow's predictive utility is demonstrated on RSK2, yet no specific predictions, validation results, or false positive rates are described. The sensitivity of the proposed validation assay is stated as "highly sensitive" without quantitative evidence. The relationship between the in-silico predictions and the experimental validation is not explained.
- **Minor Comments** The short description contains typographical errors ("unfergradiate", "form September to November") that should be corrected. The author contribution timeline for Victor J is unclear and should be clarified. The GitHub link for MiniPAE is provided but no version, license, or usage details are given in the abstract.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: The concept of using AlphaFold with a purpose-built scoring metric for SLiM discovery is novel, though the abstract does not clearly differentiate from prior AlphaFold-based interaction prediction studies. Scientific importance: SLiM-mediated interactions are biologically significant, and improved detection methods would be valuable, but the importance of this specific contribution cannot be fully assessed without performance data. Interdisciplinary readership: The work bridges structural biology, bioinformatics, and cell biology, which could attract broad interest, but the abstract is too brief to convey the interdisciplinary implications effectively. Technical soundness: Not assessable from the abstract alone; benchmark methodology, statistical treatment, and validation rigor are not described. Readability for nonspecialists: The abstract is generally clear but uses field-specific terms (SLiM, MiniPAE, proximity labeling) without sufficient context for a general scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract describes a potentially valuable workflow, but the absence of full text, figures, and data prevents assessment of the core claims. A revised submission with complete methodological detail and results would be required for a supportive recommendation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "we benchmarked several scoring metrics and showed that AlphaFold2 combined with MiniPAE yields the best performance, outperforming AlphaFold3 in this context"
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract claims that AlphaFold2 with MiniPAE outperforms AlphaFold3 for SLiM detection, but no benchmark details are provided. The evaluation criteria, dataset composition, number of test cases, statistical significance, and comparison methodology are entirely absent.
- **Why it matters** This is the central technical claim of the manuscript. Without transparent benchmark design and quantitative results, the superiority of the proposed approach cannot be verified, and readers cannot assess whether the conclusion is robust or an artifact of specific test conditions.
- **Resolution test** Provide a detailed benchmark section in the full manuscript including dataset description, evaluation metrics, baseline comparisons, statistical tests, and effect sizes. The claim should be supported by reproducible results with confidence intervals or equivalent measures.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "This workflow was used to predict the occurrence of SLiMs that mediate binding to ribosomal protein S6 kinase A3 (RPS6KA3 or RSK2)"
- **Evidence pointer** Abstract, location not provided
- **Concern** The application of the workflow to RSK2 is mentioned, but no predicted SLiM sequences, binding sites, or experimental confirmation are described. The abstract does not indicate how many predictions were made, whether any were validated, or what the success rate was.
- **Why it matters** A demonstration on a specific protein is only meaningful if the predictions are shown to be biologically relevant. Without evidence of validation or at least detailed predictions, the utility of the workflow for real-world applications remains unsubstantiated.
- **Resolution test** Include a case study section with predicted SLiM sequences, their locations in RSK2, and experimental validation results using the proposed proximity labeling assay or other orthogonal methods.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "we also introduce a highly sensitive detection method based on proximity labeling in living cells"
- **Evidence pointer** Abstract, location not provided
- **Concern** The proximity labeling-based validation method is described as "highly sensitive," but no sensitivity data, detection limits, comparison to existing methods, or protocol details are provided.
- **Why it matters** The validation assay is a key component of the proposed integrated pipeline. Without quantitative sensitivity metrics and methodological detail, the claim of high sensitivity is unsupported, and the assay's practical utility cannot be evaluated.
- **Resolution test** Provide a methods section describing the proximity labeling protocol, including controls, and present sensitivity data such as detection thresholds, signal-to-noise ratios, and comparisons with established SLiM validation approaches.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Short description
- **Evidence pointer** Short description, location not provided
- **Issue** Typographical errors are present: "unfergradiate" should be "undergraduate," and "form September to November" should be "from September to November."
- **Required correction** Correct the typographical errors in the author description.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** MiniPAE availability
- **Evidence pointer** Abstract, GitHub URL
- **Issue** The GitHub link for MiniPAE is provided, but no version number, software license, or usage instructions are mentioned in the abstract.
- **Required correction** Specify the software version, license, and provide a brief usage example or link to documentation in the full manuscript.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Author contribution timeline
- **Evidence pointer** Short description, location not provided
- **Issue** The contribution period for Victor J is stated as "form September to November 2023," which is ambiguous regarding the year and the nature of the contribution.
- **Required correction** Clarify the exact dates and describe the specific contribution made during that period.

## Risk / unsupported claims

- The claim that AlphaFold2 with MiniPAE outperforms AlphaFold3 for SLiM detection is unsupported without benchmark data.
- The claim that the workflow successfully predicts SLiMs mediating RSK2 binding is unsupported without specific predictions and validation.
- The claim that the proximity labeling method is "highly sensitive" is unsupported without quantitative sensitivity data.
- The claim that the workflow is "scalable and widely accessible" is plausible but not fully assessable without details on computational requirements and user experience.
- The overall utility of the integrated pipeline for SLiM discovery and validation cannot be evaluated from the abstract alone.