## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Technical soundness, scientific utility, and service completeness of the described web server, based solely on the provided manuscript
- **Shared manuscript claim summary** The authors present the CAID Prediction Portal, a web server that executes all methods from the CAID benchmark on user-provided protein sequences, standardizes outputs, provides consensus predictions, and offers benchmarking documentation. The server is claimed to be a valuable resource for researchers studying intrinsic disorder and binding regions.
- **Visible evidence base** Abstract, Introduction, Implementation (including subsections on Standardization, Benchmarking, Website), Conclusions, Data Availability, Funding, Acknowledgements. No figures, tables, or supplementary materials were provided.
- **Missing materials affecting confidence** Figure 1 (system overview), Table 1 (method list), website documentation, benchmark result details, performance statistics, and any user-facing interface screenshots. These are referenced but not included, limiting verification of several claims.

## Reviewer
- **Overall assessment** The manuscript describes a practically useful web service that addresses a real need in the intrinsically disordered protein research community. The implementation approach is reasonable, and the integration with CAID benchmarking is a notable strength. However, the manuscript lacks quantitative evidence of service performance, scalability, and usability. Several claims about the service's value and functionality are plausible but not verifiable from the provided material. The writing is clear and accessible, but the absence of key figures and tables weakens the case.
- **Who would be interested in the results, and why** Researchers in structural biology, bioinformatics, and computational biology who study intrinsically disordered proteins and regions. This includes those who need to compare multiple prediction tools, those who want standardized outputs for downstream analysis, and those who require a single interface for diverse prediction methods. The service is also relevant to developers of prediction methods who want to benchmark their tools against established ones.
- **Major strengths** The service addresses a clear community need by unifying heterogeneous prediction tools under a single interface. The use of containerization for reproducibility is a sound technical choice. The integration with CAID benchmarking provides a credible quality reference. The optional user authentication and session recovery are thoughtful features. The modular design for adding or removing methods is forward-looking.
- **Major Concerns** The manuscript does not provide any quantitative evaluation of the service, such as response times, throughput, or success rates. The claim that the service is "comprehensive" is not fully supported, as the method list is not shown. The consensus prediction method is described but not validated against any ground truth. The AlphaFold-disorder integration depends on external database availability, which is a potential point of failure not discussed. The manuscript does not address potential limitations, such as sequence length restrictions or resource constraints for large inputs.
- **Minor Comments** The term "flavors" is used without a formal definition. The description of the OAuth 2.0 implementation is brief and lacks security details. The manuscript does not specify the maximum input sequence length or the number of concurrent jobs supported. The Data Availability section only provides a URL, which is insufficient for reproducibility. The funding section is detailed but the acknowledgements repeat some funding information.
- **Technical failings that need to be addressed before the case is established** The absence of Figure 1 and Table 1 prevents verification of the system architecture and the claimed method coverage. No performance metrics are provided to support the claim of a "comprehensive service." The consensus method is described but not evaluated for accuracy or utility.
- **Assessment against Nature-style criteria** Originality: The service is not conceptually novel, as similar portals exist for other prediction categories, but the specific focus on CAID methods and the integration with benchmarking is a useful contribution. Scientific importance: The service has clear practical value for a specialized community, but the manuscript does not demonstrate a broad scientific impact. Interdisciplinary readership: The topic is relevant to structural biology and bioinformatics, but the manuscript is unlikely to attract readers outside these fields. Technical soundness: The implementation approach is sound, but the lack of evaluation data prevents a full assessment. Readability for nonspecialists: The manuscript is well-written and accessible, with clear explanations of the service's purpose and features.

## Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The manuscript claims the portal is a "comprehensive service" that executes "all CAID methods."
- **Evidence pointer** Table 1, referenced but not provided
- **Concern** The claim of comprehensiveness cannot be verified without Table 1, which is supposed to list all available methods. The manuscript states that the methods are "a subset of those evaluated in the second round of the CAID challenge," which contradicts the term "all." The scope of the service is therefore unclear.
- **Why it matters** The central value proposition of the service is its coverage of prediction methods. Without a verifiable method list, the reader cannot assess whether the service meets its stated purpose.
- **Resolution test** Provide Table 1 with the full list of methods, their types, and their corresponding publications. Clarify the relationship between the portal's method set and the full CAID benchmark set.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical validation
- **Claim pointer** The manuscript claims the service is "fast" and "efficient" and that the consensus prediction "highlights high-confidence ID regions."
- **Evidence pointer** Implementation section, Website subsection; location not provided
- **Concern** No performance data are provided to support the claims of speed and efficiency. The consensus method is described as a majority vote, but there is no evaluation of its accuracy or comparison to individual predictors. The claim that the consensus highlights "high-confidence" regions is not substantiated.
- **Why it matters** Users need to know whether the service can handle realistic inputs in a reasonable time and whether the consensus output is trustworthy. Without this information, the practical utility of the service is unproven.
- **Resolution test** Provide benchmark results showing response times for typical sequence lengths, and evaluate the consensus against a reference dataset or against the CAID benchmark results.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Robustness and failure handling
- **Claim pointer** The manuscript states that the AlphaFold-disorder method "takes as input the protein structure predicted by AlphaFold" and that "if the protein sequence is not present in the UniprotKB, no structure can be downloaded and the predictor will fail to execute."
- **Evidence pointer** Benchmarking subsection; location not provided
- **Concern** The failure mode for the AlphaFold-disorder method is described but not discussed in terms of user experience. It is unclear whether the user is notified of the failure, whether other predictors continue to run, or whether the failure is handled gracefully. This is a significant usability issue for a service that aims to be comprehensive.
- **Why it matters** A service that silently fails for a subset of inputs undermines user trust and the claim of comprehensiveness. The manuscript should address how failures are communicated and whether partial results are still useful.
- **Resolution test** Describe the error handling mechanism for failed predictors, including user notification and the ability to retrieve results from successfully completed predictors.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility and maintenance
- **Claim pointer** The manuscript claims the portal's "modular and extensible design makes it easy to add or remove prediction methods at any time."
- **Evidence pointer** Conclusions section; location not provided
- **Concern** The claim of extensibility is plausible but not demonstrated. No details are provided on how new methods are integrated, how versioning is handled, or how the containerized environments are updated when underlying dependencies change. The long-term maintainability of the service is unclear.
- **Why it matters** A web service that cannot be easily updated will quickly become obsolete, especially in a field where prediction methods evolve rapidly. The manuscript should provide evidence of the extensibility mechanism.
- **Resolution test** Provide a description of the integration process for a new method, including the steps required and the expected effort, or reference documentation that details this process.

## Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Implementation section, Standardization subsection; location not provided
- **Issue** The term "flavors" is used to describe different outputs of the same predictor, but it is not formally defined. This could be confusing to readers unfamiliar with the CAID terminology.
- **Required correction** Define "flavors" at first use, or replace with a more descriptive term such as "variants" or "output modes."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Data availability
- **Evidence pointer** Data Availability section
- **Issue** The Data Availability section only provides the server URL. No information is given about the underlying code, container definitions, or configuration files, which limits reproducibility of the service itself.
- **Required correction** Provide a link to a code repository or container registry where the service implementation can be inspected or redeployed.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** User guidance
- **Evidence pointer** Website subsection; location not provided
- **Issue** The manuscript describes the ability to change thresholds and sort methods, but does not explain how users should interpret the different threshold options or which threshold is recommended for a given use case.
- **Required correction** Add a brief explanation of the threshold options and their implications, or reference the documentation where this is described.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Funding and acknowledgements
- **Evidence pointer** Funding and Acknowledgements sections
- **Issue** The funding information is repeated in both sections, which is redundant.
- **Required correction** Consolidate the funding information into a single section and keep the acknowledgements for non-financial contributions.

## Risk / unsupported claims
- The claim that the portal is "comprehensive" is not supported without Table 1.
- The claim that the consensus prediction "highlights high-confidence ID regions" is not validated.
- The claim of "fast" and "efficient" execution is not supported by any performance data.
- The claim of "extensible design" is not demonstrated with concrete evidence.
- The claim that the service is "valuable" for researchers is plausible but not quantitatively supported.
- The failure handling for the AlphaFold-disorder method is described but not evaluated for user impact.
- The integration with OpenEBench is mentioned but not described in sufficient detail to assess its significance.