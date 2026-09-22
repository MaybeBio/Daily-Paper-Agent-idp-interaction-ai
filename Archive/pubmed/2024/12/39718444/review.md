## Review setup
- **Input scope** Full manuscript text including abstract, introduction, protocol descriptions, commentary, and supplementary sections
- **Assessment boundary** Evaluation of the protocol's clarity, reproducibility, technical accuracy, and utility for the target audience; assessment of whether the described MobiDB version 6 features are adequately documented and demonstrated
- **Shared manuscript claim summary** The manuscript presents a set of protocols for using MobiDB version 6, a database resource for intrinsically disordered proteins and regions. The authors claim that the updated resource includes significant improvements such as AlphaFoldDB prediction integration, a new homology transfer pipeline, expanded annotation coverage, and an updated user interface, and that the provided protocols enable users to effectively search, retrieve, visualize, and interpret disorder-related data through both web and programmatic interfaces.
- **Visible evidence base** Full protocol text with step-by-step instructions, figure references (Figs. 1, 4, 5, 8), table references (Tables 1, 3), and a case study using human growth hormone receptor (UniProt P10912)
- **Missing materials affecting confidence** Figures and tables referenced in the text were not provided; actual screenshots or visual demonstrations of the interface are absent; the REST API code examples are not shown in full; no supplementary materials or video tutorials were included

## Reviewer
- **Overall assessment** This manuscript provides a practical and timely protocol for navigating the updated MobiDB resource, which is a valuable community resource for the intrinsically disordered protein field. The step-by-step structure is appropriate for the Current Protocols format, and the inclusion of both web-based and programmatic access methods addresses the needs of diverse users. However, the manuscript has several weaknesses that limit its current utility. The protocol descriptions are often high-level and lack the specificity required for true reproducibility, particularly in the REST API section where concrete code examples are missing. The case study using GHR is a good pedagogical choice, but the description of how to interpret the visualizations is superficial. The manuscript would benefit from more detailed explanations of the underlying data types, clearer differentiation between evidence categories, and explicit guidance on troubleshooting common user errors. The scientific claims about MobiDB's improvements are consistent with the broader literature, but the protocol itself does not provide sufficient depth to fully establish its utility as a standalone guide.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins and regions, including structural biologists, computational biologists, and bioinformaticians who need to access and interpret disorder predictions and annotations. The protocol would also be useful for researchers working on protein function, phase separation, and disease-related aggregation, as well as for educators teaching bioinformatics approaches to protein disorder analysis. The REST API section may appeal to developers and bioinformaticians seeking to integrate MobiDB data into custom pipelines.
- **Major strengths** The manuscript addresses a clear need for updated documentation of a widely used community resource. The protocol structure is logical, progressing from basic searches to advanced features and programmatic access. The use of a single case study protein throughout provides continuity and helps users understand the practical application of the resource. The inclusion of both "Selected datasets" and "Selected proteomes" sections demonstrates the breadth of the resource. The authors have clearly identified the key new features of version 6, particularly the AlphaFoldDB integration and homology transfer pipeline, which are significant updates.
- **Major Concerns** The protocol lacks the level of detail necessary for true reproducibility. The REST API section is particularly underdeveloped, with no concrete code examples or output demonstrations. The interpretation guidance for the visualization tools is insufficient for users unfamiliar with disorder prediction concepts. The manuscript does not adequately explain the differences between evidence types (curated, derived, homology, predicted) and how users should weight these in their analyses. The troubleshooting section is referenced but not described in sufficient detail. The figures, which are critical for a protocol paper, were not available for review, making it impossible to assess whether the visual guidance is adequate.
- **Minor Comments** The manuscript contains some typographical errors and awkward phrasing. The "Guidelines for Understanding Results" section is somewhat repetitive of earlier content. The relationship between MobiDB and other resources such as ELIXIR and IDP Central could be clarified. The authors should consider adding a section on common use cases or example research questions that the resource can address. The reference to "disorder-to-disorder (DD) and disorder-to-order (DO) binding modes" in the Guidelines section is not explained elsewhere in the text.
- **Technical failings that need to be addressed before the case is established** The REST API protocol is incomplete as presented. The manuscript claims that the homology transfer pipeline "substantially increased the number of entries with high-quality annotations" but does not provide quantitative evidence or a clear explanation of the methodology. The description of how AlphaFoldDB predictions are integrated and visualized is insufficient for users to understand the relationship between predicted structures and disorder annotations. The protocol does not explain how users should interpret conflicting annotations from different sources.
- **Assessment against Nature-style criteria** Originality: The manuscript is not original research but rather a protocol for an existing resource. Its novelty lies in documenting the updated features of MobiDB version 6. Scientific importance: The resource itself is important to the IDP community, and updated protocols are needed. However, the protocol as written does not fully deliver on its promise to guide users through the new features. Interdisciplinary readership: The protocol is primarily targeted at bioinformaticians and structural biologists, with limited appeal to a broader interdisciplinary audience. Technical soundness: The described features are consistent with the published literature on MobiDB, but the protocol's technical execution is incomplete, particularly regarding the API section. Readability for nonspecialists: The manuscript is generally readable but assumes familiarity with disorder prediction concepts and bioinformatics terminology. Some sections, particularly the API description, would be challenging for nonspecialists.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses a genuine need and the authors are clearly knowledgeable about the resource. However, the protocol requires substantial revision to achieve the level of detail and clarity expected for a methods paper. The API section needs concrete examples, the visualization interpretation needs more depth, and the evidence type explanations need expansion.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The Support Protocol claims to describe "Programmatic access with MobiDB REST API" and states that "Detailed descriptions of the endpoints, including their parameters, input, and output specifications, are provided below."
- **Evidence pointer** Section "PROGRAMMATIC ACCESS WITH MobiDB REST API", location not provided
- **Concern** The REST API section does not contain any actual code examples, request/response formats, or concrete demonstrations of how to use the described endpoints. The text mentions the download_page, count, and statistics endpoints but does not show how to construct queries, what parameters are required, or what the output looks like. For a protocol paper, this is a critical omission. Users cannot follow the protocol without this information.
- **Why it matters** The stated purpose of the protocol is to guide users through programmatic access. Without concrete examples, the protocol fails its primary objective for this section. Users would need to visit the external API documentation, which defeats the purpose of having a protocol paper.
- **Resolution test** Provide at least one complete worked example for each endpoint, including the full URL or code snippet, required and optional parameters, and a sample of the output. Include error handling guidance and common pitfalls.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical accuracy
- **Claim pointer** The Introduction states that "A notable enhancement in MobiDB... is the integration of AlphaFoldDB predictions... which have shown high correlation with experimental disorder data and state-of-the-art disorder predictors according to the Critical Assessment of Intrinsic protein Disorder (CAID) assessment."
- **Evidence pointer** Introduction, location not provided
- **Concern** The claim about AlphaFoldDB predictions showing "high correlation" with experimental disorder data is presented without specific correlation values, the CAID assessment reference is cited but not explained, and the manuscript does not clarify how AlphaFoldDB predictions are converted into disorder annotations. The relationship between AlphaFold's pLDDT scores and disorder is not explained, which is essential for users to interpret the data correctly.
- **Why it matters** Users need to understand the basis of the predictions they are viewing. Without this context, they may over-interpret or misinterpret the AlphaFold-derived disorder annotations. The claim as stated is too vague to be evaluated.
- **Resolution test** Provide specific correlation statistics from the CAID assessment, explain how AlphaFold predictions are processed to generate disorder annotations, and clarify the relationship between pLDDT scores and disorder classification.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Completeness
- **Claim pointer** The manuscript states that "The 'Selected datasets' are organized and displayed based on different confidence annotation levels (Gold and Silver stars) characterized by the type of 'Evidence,' which indicates the quality of the annotation (Table 1)."
- **Evidence pointer** Section "SEARCHING MobiDB SELECTED DATASETS AND SELECTED PROTEOMES", Table 1, location not provided
- **Concern** Table 1 is referenced as providing information about evidence types and confidence levels, but the table content is not included in the provided material. The text mentions Gold and Silver datasets but does not explain the criteria for these classifications in sufficient detail. The distinction between "curated (C), derived (D), homology (D), and predicted (P)" evidence types is mentioned in the Guidelines section but not explained in the context of the datasets. Note that "homology" and "derived" both use the letter D, which is confusing.
- **Why it matters** Understanding the confidence levels and evidence types is fundamental to interpreting the data in MobiDB. Users need to know what Gold versus Silver means and how to weigh different evidence types when drawing conclusions.
- **Resolution test** Include the full content of Table 1 in the manuscript, explain the criteria for Gold and Silver classifications, and clarify the evidence type abbreviations, potentially using distinct letters for each category.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Usability
- **Claim pointer** The manuscript states that "The entry page has also undergone substantial improvements. It has been redesigned to provide a more intuitive and informative user experience."
- **Evidence pointer** Section "VISUALIZING AND INTERPRETING A MobiDB ENTRY: THE GHR USE CASE", location not provided
- **Concern** The description of the entry page visualization is high-level and does not provide sufficient guidance for users to interpret the various components. The text mentions "Features Content, Feature viewer, and AlphaFold structure visualization" and tabs for "Overview," "Disorder," "Binding," "Interactions," and "Functions," but does not explain what each of these displays shows, how to read the visualizations, or how to extract meaningful biological insights from them.
- **Why it matters** The case study is meant to demonstrate how to interpret MobiDB data. Without detailed explanation of the visualization components, users will not be able to fully leverage the resource or understand the biological significance of what they are viewing.
- **Resolution test** Provide a detailed walkthrough of the entry page, explaining each visualization component, what the colors and symbols mean, and how to interpret the data in a biological context. Include specific examples of insights that can be derived from the GHR case study.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The manuscript states that "For a list of potential problems, their causes, and their solutions, please refer to Table 3."
- **Evidence pointer** Section "Troubleshooting", Table 3, location not provided
- **Concern** Table 3 is referenced as containing troubleshooting information, but the table content is not provided. The manuscript does not describe any of the common problems users might encounter, their causes, or solutions. This is a significant gap for a protocol paper, as troubleshooting guidance is often critical for successful execution.
- **Why it matters** Users will inevitably encounter issues when using the resource. Without the troubleshooting information, they may become frustrated and abandon the protocol. The absence of this content makes the protocol incomplete.
- **Resolution test** Include the full content of Table 3 in the manuscript, covering common issues such as failed searches, slow response times, API errors, and visualization problems, along with clear solutions.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract states that IDPs "make up around 30% of eukaryotic proteomes" but does not specify whether this refers to fully disordered proteins or includes proteins with disordered regions. The Introduction clarifies this later, but the abstract could be more precise.
- **Required correction** Clarify in the abstract whether the 30% figure refers to proteins that are fully disordered or proteins containing disordered regions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Guidelines for Understanding Results
- **Evidence pointer** Section "Guidelines for Understanding Results", location not provided
- **Issue** The text states that "Selected datasets comprise four types of evidence—curated (C), derived (D), homology (D), and predicted (P)" but uses the letter D for both "derived" and "homology." This is confusing and could lead to misinterpretation.
- **Required correction** Use distinct abbreviations for each evidence type, such as C, D, H, and P, and ensure these are used consistently throughout the manuscript.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Necessary Resources sections
- **Evidence pointer** All "Necessary Resources" sections, location not provided
- **Issue** The hardware and software requirements are identical across all protocols and are quite minimal. The "Input data" section consistently states "None required," which is accurate for web-based searches but may not be accurate for the API protocol, where users may need to prepare input files or scripts.
- **Required correction** Consider whether the API protocol requires any input data preparation and, if so, describe it in the corresponding "Necessary Resources" section.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Introduction
- **Evidence pointer** Introduction, location not provided
- **Issue** The sentence "The latest update of MobiDB (version 6, released in July 2024; Piovesan et al., 2024)) represents a substantial enhancement" contains a double closing parenthesis.
- **Required correction** Fix the typographical error by removing the extra closing parenthesis.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Background Information
- **Evidence pointer** Section "Background Information", location not provided
- **Issue** The text mentions that "functional annotations (GO and IDPO) from databases like DisProt are propagated using sequence similarity and protein embeddings" but does not explain what "protein embeddings" are or how they are used. This may be unfamiliar to some readers.
- **Required correction** Provide a brief explanation of protein embeddings or rephrase the sentence to be more accessible to a broader audience.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Data Availability Statement
- **Evidence pointer** Data Availability Statement, location not provided
- **Issue** The data availability statement is minimal and only states that data are openly available in MobiDB. It does not mention the version of the database or provide a specific access date, which would be helpful for reproducibility.
- **Required correction** Consider adding the database version and access date to the data availability statement.

## Risk / unsupported claims
- The claim that AlphaFoldDB predictions "have shown high correlation with experimental disorder data" is not supported with specific quantitative evidence in the provided text.
- The claim that the homology transfer pipeline "substantially increased the number of entries with high-quality annotations" is not supported with specific numbers or a comparison to previous versions.
- The claim that the updated user interface "provides an immediate overview of disorder, binding, and disorder functions information" cannot be fully evaluated without the referenced figures.
- The claim that MobiDB "remains a critical resource for researchers" is an assertion without supporting evidence in the provided text.
- The statement that "MobiDB now integrates AlphaFoldDB predictions, filling disorder-annotation gaps for those sequences for which experimental coordinates are lacking" is plausible but not demonstrated with examples in the provided text.
- The overall utility and usability of the protocols cannot be fully assessed without the referenced figures and tables, which are essential for a protocol paper.