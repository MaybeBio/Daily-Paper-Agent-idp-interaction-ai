## Review setup
- **Input scope** Full manuscript text (abstract and main body sections)
- **Assessment boundary** Scientific content, technical soundness, and clarity of the presented perspective; no assessment of formatting or journal fit beyond Nature-style criteria
- **Shared manuscript claim summary** The authors argue that while AI, particularly deep learning and large protein language models, has revolutionized computational protein studies, current methods are limited by their focus on single static structures. They advocate for a shift toward predicting conformational ensembles, dynamics, and multi-state behaviors, and propose integrating AI with physics-based coarse-grained simulations to overcome these limitations.
- **Visible evidence base** Abstract, sections on alternative conformations (Arf6 example), training data quality and water molecules, ligand-binding and protein-protein interaction prediction, integration with experimental data, LPLM embeddings, homolog discovery, disordered proteins, ensemble modeling, transition pathways, DL-CG integration, and RNA structure prediction. Figures referenced but not provided.
- **Missing materials affecting confidence** Figures 1–5, references list, and any supplementary data are not provided. This limits verification of specific claims about structural comparisons, prediction accuracies, and illustrative examples.

## Reviewer
- **Overall assessment** This perspective presents a timely and relevant argument that the next frontier in computational protein studies lies in moving beyond single static structures toward conformational ensembles and dynamics. The authors draw on a broad range of recent literature and provide a compelling case for integrating AI with physics-based methods. However, the manuscript suffers from uneven depth, with some sections being overly brief or lacking critical analysis. The central thesis is well-supported by examples, but several claims require more rigorous evidence or clearer articulation. The writing is generally accessible but occasionally imprecise, and the lack of figures in the provided material limits full evaluation.
- **Who would be interested in the results, and why** Computational biologists, structural biologists, and researchers in AI-driven drug discovery would find this perspective valuable. It synthesizes current challenges and opportunities in applying AI to protein dynamics and ensembles, which is directly relevant to those developing or using such methods. The call for integrating AI with coarse-grained simulations may also interest method developers in molecular simulation.
- **Major strengths** The manuscript addresses a critical and timely gap in the field: the over-reliance on static structures. The Arf6 example is illustrative and effectively demonstrates the potential of AI to generate alternative conformations. The discussion of training data quality and water molecules raises important, often overlooked issues. The proposal to integrate DL with CG simulations is a constructive and forward-looking suggestion. The section on LPLM embeddings provides practical advice on validation, which is valuable for practitioners.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** "ESM-IF1/ESMFold successfully predicted the other conformation of 1E0S, which is 2J5X."
  - **Evidence pointer** Section "Example of Generating Alternative Conformations", Figure 1 (not provided)
  - **Concern** The claim that ESMFold successfully predicted the alternative conformation is central to the manuscript's thesis, but the provided text does not describe the methodology, the quantitative comparison, or the criteria for "success." Without Figure 1 or a detailed description of the prediction protocol and comparison metrics, this claim cannot be evaluated.
  - **Why it matters** This example is the primary evidence that AI can generate biologically relevant alternative conformations. If this claim is not rigorously supported, the manuscript's central argument is weakened.
  - **Resolution test** Provide a detailed description of the prediction method, the structural comparison (e.g., RMSD, TM-score), and a statistical or qualitative assessment of the similarity between the predicted and experimental structures. Include Figure 1 with clear annotations.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** "SuperWater32 has recently been developed to integrate a score-based diffusion model with equivariant Graph Neural Networks (GNNs) and was found to predict water molecule placements around proteins with an accuracy of 0.3 ± 0.06 Å relative to experimentally validated positions."
  - **Evidence pointer** Section "Inaccuracies in the training data and the problem of water in proteins", location not provided
  - **Concern** The reported accuracy of 0.3 ± 0.06 Å is exceptionally high and would be a significant advance. However, the text does not specify the benchmark dataset, the number of water molecules tested, the comparison method, or whether this accuracy is for all predicted waters or only high-confidence ones. This level of precision is unusual and requires careful scrutiny.
  - **Why it matters** If this claim is inaccurate or taken out of context, it could mislead readers about the current state of water prediction methods. The manuscript should provide sufficient context for readers to assess the significance of this result.
  - **Resolution test** Provide details on the benchmark dataset, evaluation protocol, and statistical significance. Clarify whether this accuracy is typical or represents a best-case scenario.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** "In CASP16, the AlphaFold3 server's predictions of 3D RNA structures were outperformed by physics-based models."
  - **Evidence pointer** Section "Predicted RNA Structures", location not provided
  - **Concern** This is a strong claim that contradicts the general narrative of AI superiority. The text does not provide details on the specific metrics, the margin of outperformance, or which physics-based models were used. This claim is presented without sufficient context or citation details.
  - **Why it matters** This statement is important for the manuscript's argument that AI has limitations. However, without specifics, it is difficult to assess its validity and generalizability.
  - **Resolution test** Provide specific CASP16 results, including the metrics used (e.g., TM-score, INF), the ranking of AlphaFold3 relative to physics-based methods, and a discussion of the implications.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** "AlphaFold3 is still unable to predict functional structures (see Figure 5), even for oligomeric proteins that are part of the same clade as proteins whose structures were determined experimentally, e.g., by cryo-EM."
  - **Evidence pointer** Section "Modeling transition pathways and conformational changes", Figure 5 (not provided)
  - **Concern** The claim that AlphaFold3 is "unable to predict functional structures" is broad and potentially misleading. The example of katanin is described, but the text does not provide quantitative details on the prediction failure, such as the confidence scores, the structural deviation from experimental structures, or whether the failure is due to ligand handling or other factors.
  - **Why it matters** This claim is used to support the argument that AI methods are insufficient for capturing functional states. Without clear evidence, the claim may be overstated.
  - **Resolution test** Provide a detailed analysis of the katanin prediction, including metrics comparing the predicted and experimental structures, and a discussion of why the prediction fails.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Section "How to Use LPLM Embeddings"
  - **Evidence pointer** Location not provided
  - **Issue** The section is brief and lacks a concrete example or a step-by-step guide. The statement "The differences between embedding values can be used to identify the best homologs" is vague.
  - **Required correction** Provide a more detailed explanation of the method, possibly with a small illustrative example or a reference to a specific protocol.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Readability
  - **Affected element** Section "Inaccuracies in the training data and the problem of water in proteins"
  - **Evidence pointer** Location not provided
  - **Issue** The sentence "This problem will be solved with more high resolution crystal structures solved with the higher energy beam lines coming online now" is speculative and not directly supported by evidence.
  - **Required correction** Rephrase to be more cautious, e.g., "This problem may be alleviated as more high-resolution crystal structures become available from new high-energy beamlines."
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Section "Modeling transition pathways and conformational changes"
  - **Evidence pointer** Location not provided
  - **Issue** The text states "MinActionPath292 and eBDIMS2,78" but the reference numbering appears inconsistent (78 is used for both eBDIMS2 and a later reference to Scaramozzino et al.).
  - **Required correction** Check and correct all reference numbers for consistency.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Section "Predicted RNA Structures"
  - **Evidence pointer** Location not provided
  - **Issue** The section introduces "gML" (genomic language model) but does not clearly define its relationship to LPLMs or how it differs from other models.
  - **Required correction** Provide a clear definition and context for gML, and explain its relevance to the manuscript's main argument.

## Risk / unsupported claims
- The claim that ESMFold successfully predicted the alternative conformation of Arf6 (R1-M1) is not verifiable without Figure 1 and methodological details.
- The reported accuracy of SuperWater (0.3 ± 0.06 Å) is presented without sufficient context to assess its validity.
- The claim that AlphaFold3 was outperformed by physics-based models in CASP16 for RNA is stated without specific data.
- The assertion that AlphaFold3 is "unable to predict functional structures" is overly broad and not fully supported by the provided example.
- The statement about "higher energy beam lines" solving the water placement problem is speculative.
- The section on LPLM embeddings claims success in finding new homologs with as low as 10% sequence identity, but no details on the method or validation are provided.

## Assessment against Nature-style criteria
- **Originality** The perspective is original in its synthesis of current challenges and its specific proposal to integrate AI with coarse-grained simulations. However, the individual topics (ensembles, dynamics, water, etc.) are not new, and the manuscript does not present a fundamentally novel framework.
- **Scientific importance** The topic is of high importance to the field, as the limitations of static structure prediction are widely recognized. The manuscript highlights key challenges and potential directions, which is valuable for guiding future research.
- **Interdisciplinary readership** The manuscript is relevant to computational biologists, structural biologists, and AI researchers. However, some sections may be too specialized for a general audience, and the lack of figures in the provided material limits accessibility.
- **Technical soundness** The manuscript is generally sound in its descriptions of existing methods, but several key claims lack sufficient evidence or detail, as noted in the major concerns. The technical arguments would benefit from more rigorous support.
- **Readability for nonspecialists** The writing is mostly clear, but some sections assume prior knowledge of specific methods (e.g., diffusion models, equivariant GNNs). The abstract is accessible, but the main text could be improved with more context and clearer explanations of technical terms.

## Recommendation posture
Supportive if technical concerns are resolved. The manuscript addresses an important and timely topic, and the central argument is compelling. However, the major concerns regarding the verification of key claims must be addressed before the case is fully established. Specifically, the authors should provide more detailed evidence for the Arf6 example, the SuperWater accuracy, and the CASP16 RNA results. With these revisions, the manuscript would be a valuable contribution to the field.