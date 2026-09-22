## Review setup

- **Input scope** Abstract and metadata only. The provided material is the arXiv landing page for the manuscript, containing the title, author list, submission date, DOI, and abstract. No full text, figures, tables, or supplementary materials were provided.
- **Assessment boundary** This review is limited to the claims and evidence visible in the abstract and the bibliographic record. Any assessment of methodology, results, or validation is constrained by the absence of the full manuscript.
- **Shared manuscript claim summary** The manuscript presents Seq2Bind, a webserver that uses fine-tuned protein language models to decode binding hotspots directly from protein sequences. The abstract implies that the tool can predict binding sites without structural input, and that it is available as a web-based platform.
- **Visible evidence base** The abstract text as provided. No figures, tables, methods sections, or validation data are accessible from the supplied material.
- **Missing materials affecting confidence** Full manuscript text, all figures and tables, methods description, validation datasets, webserver URL and interface details, and any benchmark results. The absence of these materials severely limits the ability to assess the technical soundness and validity of the claims.

## Reviewer

- **Overall assessment** The abstract presents a potentially useful tool for the structural biology and bioinformatics communities. The concept of using protein language models to predict binding hotspots from sequence alone is timely and aligns with current trends in the field. However, the abstract provides insufficient detail to evaluate the method's novelty, performance, or practical utility. The claims are broad and lack quantitative support. The manuscript cannot be assessed for technical soundness from the supplied material alone.
- **Who would be interested in the results, and why** Researchers in computational biology, structural bioinformatics, and drug discovery would be interested. The tool could be valuable for those studying protein-protein interactions, identifying functional residues, or prioritizing mutations in the absence of experimental structures. The webserver format also makes it accessible to experimental biologists seeking quick predictions.
- **Major strengths** The concept of sequence-only prediction is practically appealing, as it removes the dependency on experimentally determined structures. The use of fine-tuned protein language models is a modern and relevant approach. The webserver format suggests an intent to provide a user-friendly resource for the broader community.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3
- **Minor Comments**  
  - R1-m1  
  - R1-m2
- **Technical failings that need to be addressed before the case is established** The abstract does not provide any quantitative performance metrics, benchmark comparisons, or validation details. Without these, the predictive accuracy and reliability of the tool cannot be established. The novelty relative to existing sequence-based binding site predictors is not articulated.
- **Assessment against Nature-style criteria**  
  - Originality: The abstract suggests a novel application of protein language models, but without details on the fine-tuning approach or comparison to existing methods, the degree of originality cannot be assessed.  
  - Scientific importance: The problem of predicting binding hotspots from sequence is important, but the abstract does not demonstrate how the tool advances the field beyond current capabilities.  
  - Interdisciplinary readership: The topic is relevant to computational and experimental biologists, but the abstract is too brief to convey the significance to a broad audience.  
  - Technical soundness: Not assessable from the abstract. No methodological details or validation results are provided.  
  - Readability for nonspecialists: The abstract is concise and accessible, but lacks context on the significance and limitations of the approach.
- **Recommendation posture** Currently not established from the provided evidence. The abstract alone does not provide sufficient information to support the claims. A full review of the manuscript is required to determine whether the technical concerns can be resolved.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The abstract claims that Seq2Bind can decode binding hotspots directly from sequences using fine-tuned protein language models.  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The abstract provides no quantitative evidence of predictive performance. There are no accuracy metrics, no comparison to existing tools, and no description of the validation datasets used.  
- **Why it matters** Without performance benchmarks, the scientific community cannot judge whether the tool is reliable or an improvement over existing methods. A claim of predictive capability requires empirical support.  
- **Resolution test** Provide benchmark results on standard datasets, including metrics such as precision, recall, and area under the ROC curve, and compare against at least one established sequence-based binding site predictor.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Originality  
- **Claim pointer** The abstract implies that the fine-tuned protein language model approach is a novel contribution.  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The abstract does not describe how the fine-tuning approach differs from existing protein language model applications for binding site prediction. Several such methods have been published in recent years.  
- **Why it matters** The field is rapidly advancing, and novelty must be clearly articulated to justify publication. Without a clear distinction from prior work, the contribution may be incremental.  
- **Resolution test** Include a clear statement of novelty in the abstract or introduction, and provide a comparison to at least two existing sequence-based binding site prediction methods.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Reproducibility  
- **Claim pointer** The abstract presents Seq2Bind as a webserver, implying that it is accessible and usable by others.  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The abstract does not provide the webserver URL, details on the input and output formats, or any information on the underlying code availability.  
- **Why it matters** A webserver is only useful if it is accessible and documented. Without this information, the reproducibility and practical utility of the tool cannot be evaluated.  
- **Resolution test** Provide the webserver URL, a description of the user interface, and a statement on code and data availability in the manuscript.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Readability for nonspecialists  
- **Affected element** Abstract  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The term "binding hotspots" is not defined in the abstract. Nonspecialist readers may not understand what is being predicted.  
- **Required correction** Add a brief definition or example of binding hotspots in the abstract.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Abstract  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The abstract does not mention the scope of the tool, such as whether it applies to protein-protein, protein-ligand, or protein-nucleic acid interactions.  
- **Required correction** Specify the types of binding interactions that the tool is designed to predict.

## Risk / unsupported claims

- The claim that Seq2Bind can decode binding hotspots directly from sequences is unsupported by any quantitative evidence in the abstract.
- The implied novelty of the fine-tuned protein language model approach is not substantiated by comparison to existing methods.
- The availability and functionality of the webserver cannot be verified from the abstract alone.