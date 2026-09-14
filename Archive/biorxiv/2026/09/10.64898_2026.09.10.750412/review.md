## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors propose ICARus, a positive-unlabelled read-out refinement framework that integrates protein-protein interaction information derived from a protein language model, to improve the discovery of vaccinia virus-host interactions from a genome-wide RNA interference screen. They report enhanced identification of human genes with potential antiviral function and provide raw and refined screen read-outs as an agentic-AI-enabled community resource. They claim the strategy is generalisable for robust hit prioritisation in functional screens.
- **Visible evidence base** Abstract text only; no quantitative results, validation data, or methodological details are available
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, supplementary data, code availability, and any statistical or benchmarking analyses

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting idea, namely the use of protein language model-derived interaction information to refine functional screen read-outs. However, the current submission, as represented by the abstract alone, does not provide sufficient evidence to evaluate the validity, robustness, or generalisability of the proposed approach. Key claims regarding performance improvement, biological relevance, and the utility of the resource are stated without supporting quantitative or methodological detail. The manuscript may have merit, but the case is not established from the provided material.
- **Who would be interested in the results, and why** Researchers in virology, particularly those studying poxvirus-host interactions and antiviral host factors, would be the primary audience. Additionally, method developers in functional genomics and computational biology, especially those working on hit prioritisation in RNA interference or CRISPR screens, and those interested in applying protein language models to biological discovery, would find the approach relevant. The community resource aspect may also appeal to bioinformaticians and data scientists developing agentic AI tools for biological data.
- **Major strengths** The problem addressed is timely and important, given recent mpox outbreaks and the need for systematic identification of host factors involved in poxvirus infection. The proposed integration of protein language model-derived information with positive-unlabelled learning is a novel and potentially powerful conceptual direction. The intention to release raw and refined data as a community resource is commendable and aligns with open science principles.
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
  Originality: The concept of using protein language model embeddings to refine functional screen read-outs appears novel, but the abstract does not provide enough context to assess how distinct this is from existing computational refinement methods.  
  Scientific importance: The topic is of high importance given the public health relevance of poxviruses, but the abstract does not demonstrate the magnitude or significance of the reported improvement.  
  Interdisciplinary readership: The work bridges virology, functional genomics, and machine learning, which could appeal to a broad audience, but the abstract lacks the clarity and quantitative hooks needed to engage nonspecialists.  
  Technical soundness: Cannot be assessed from the abstract alone. No methodological details, validation metrics, or statistical analyses are provided.  
  Readability for nonspecialists: The abstract is reasonably clear in its narrative, but terms such as "positive-unlabelled read-out refinement" and "agentic-AI-enabled" are introduced without sufficient explanation for a general scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The idea is promising, but the abstract alone does not provide the necessary evidence to support the core claims. A full manuscript with detailed methods, validation, and benchmarking would be required to assess whether the approach is sound and the claims are justified.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The claim that ICARus "boosts the discovery of vaccinia virus-host interactions" and "enhances the identification of human genes with potential antiviral function" is central to the paper.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** No quantitative results are presented. There is no indication of the effect size, the number of genes identified, the false discovery rate, or any comparison against baseline methods. The abstract states that the approach "boosts" discovery, but no data are shown to support this assertion.  
- **Why it matters** Without quantitative evidence, the reader cannot evaluate whether the improvement is meaningful, statistically significant, or practically useful. The core claim of the paper rests on this improvement, and its absence makes the claim unsupported.  
- **Resolution test** Provide a comparison of ICARus against standard read-out analysis methods, including metrics such as precision, recall, enrichment of known host factors, and reproducibility across replicates. Include confidence intervals and statistical tests.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Methodological transparency  
- **Claim pointer** The abstract describes ICARus as a "positive-unlabelled read-out refinement framework" that integrates "protein-protein interaction information derived from a protein language model."  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The methodological details are entirely absent. It is unclear how the protein language model is applied, how the positive-unlabelled learning is implemented, how the interaction information is integrated with the screen read-outs, and how the framework handles off-target effects and assay noise, which are mentioned as motivating problems.  
- **Why it matters** Reproducibility is a fundamental requirement in computational biology. Without a clear description of the method, other researchers cannot apply or validate the approach. The lack of detail also prevents assessment of whether the method is sound or whether it introduces biases.  
- **Resolution test** Provide a full methods section that describes the model architecture, training data, feature representation, integration strategy, and the positive-unlabelled learning procedure. Include code and a reproducible pipeline.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Validation and benchmarking  
- **Claim pointer** The claim that the approach is "generalisable for robust hit prioritisation in functional screens" implies broad applicability beyond poxvirus screens.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** No validation is shown for the generalisability claim. The abstract only describes application to a vaccinia virus screen. There is no evidence that the method works on other viruses, other cell types, or other types of functional screens, such as CRISPR or chemical screens.  
- **Why it matters** The generalisability claim is a key part of the paper's significance. Without demonstration on independent datasets, the claim is speculative and not supported by the evidence.  
- **Resolution test** Apply ICARus to at least one or two independent functional screen datasets, preferably from different viruses or different screening modalities, and show that the refinement improves hit prioritisation in those contexts as well.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Resource utility and accessibility  
- **Claim pointer** The abstract states that the authors provide "raw and refined read-outs of a genome-wide screen for vaccinia virus host factors as an agentic-AI-enabled community resource."  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The nature of the "agentic-AI-enabled" resource is not described. It is unclear what form this resource takes, how it can be accessed, whether it includes interactive tools, and what the licensing and data standards are. The term "agentic-AI-enabled" is not defined.  
- **Why it matters** The community resource is presented as a major deliverable. If the resource is not accessible, well-documented, or interoperable, its value to the community is diminished. The lack of detail prevents assessment of its utility.  
- **Resolution test** Describe the resource in detail, including data format, access mechanism, documentation, and any associated tools. Provide a link or a clear plan for data deposition in a recognised repository.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity of terminology  
- **Affected element** Abstract text  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The term "agentic-AI-enabled" is used without definition. It is not clear what this means in the context of a data resource.  
- **Required correction** Define the term or replace it with a more standard description of the resource, such as "machine-readable" or "interactive," and explain what the resource offers.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Contextual framing  
- **Affected element** Abstract text  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The abstract mentions "off-target effects and assay noise" as motivating problems, but it is not stated how ICARus specifically addresses these issues.  
- **Required correction** Briefly state how the integration of protein language model information mitigates off-target effects or noise, or clarify that the method does not directly address these but rather improves signal detection.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Readability  
- **Affected element** Abstract text  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The phrase "positive-unlabelled read-out refinement framework" is dense and may be difficult for nonspecialists to parse.  
- **Required correction** Consider rephrasing to something like "a computational framework that uses positive-unlabelled learning to refine screen read-outs," which is more accessible.

## Risk / unsupported claims
- The claim that ICARus "boosts the discovery of vaccinia virus-host interactions" is unsupported by any quantitative data in the abstract.
- The claim that the approach "enhances the identification of human genes with potential antiviral function" is unsupported without validation data.
- The claim that the strategy is "generalisable for robust hit prioritisation in functional screens" is speculative and not supported by evidence from other screens.
- The claim that the resource is "agentic-AI-enabled" is not defined and cannot be evaluated.
- The overall significance of the work, in terms of effect size and biological relevance, cannot be assessed from the abstract alone.