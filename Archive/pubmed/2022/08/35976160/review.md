## Review setup
- **Input scope** Full manuscript text (abstract, introduction, main sections, conclusions, acknowledgments)
- **Assessment boundary** Scientific content, logical coherence, support for claims, and alignment with stated scope; no assessment of formatting or journal fit beyond Nature-style criteria
- **Shared manuscript claim summary** The manuscript argues that AlphaFold, despite its transformative impact on protein structure prediction, does not resolve the protein folding problem, does not capture conformational ensembles, and cannot directly address allostery or related dynamic phenomena. It further claims that AI and machine learning, including integration with molecular dynamics simulations, can indirectly assist in generating ensembles and predicting protein–protein interactions, with implications for drug discovery and precision medicine.
- **Visible evidence base** Full text including abstract, introduction, sections on protein folding, structure prediction, structure–function paradigm, AI in simulations, AI in pathogen–host PPIs, and conclusions. No figures, tables, or supplementary materials were provided.
- **Missing materials affecting confidence** Figures (referenced as Figures 1, 2, 3) are not available; no experimental data, benchmarks, or quantitative comparisons are provided; no code or algorithmic details are given; no citations are verifiable from the text alone.

## Reviewer
- **Overall assessment** This is a perspective or review-style manuscript that surveys the capabilities and limitations of AlphaFold and AI in structural biology, with a particular focus on allostery and conformational ensembles. The writing is clear and accessible, and the authors demonstrate broad knowledge of the field. However, the manuscript is largely descriptive and lacks original data or novel synthesis. The central claims about AlphaFold's limitations are well known and not substantiated with new evidence or analysis. The discussion of AI applications, while relevant, is superficial in places and does not provide sufficient depth or critical evaluation. The manuscript would benefit from a more focused argument and concrete examples or case studies to support its assertions.
- **Who would be interested in the results, and why** Computational biologists, structural biologists, and biophysicists interested in the capabilities and limitations of AlphaFold and AI-based methods. Researchers working on allostery, conformational dynamics, and protein–protein interactions may find the perspective useful as a summary of current challenges. Drug discovery scientists may also be interested in the discussion of AI applications, though the treatment is not sufficiently detailed to guide practical use.
- **Major strengths** The manuscript is well written and accessible to a broad audience. It correctly identifies key limitations of AlphaFold, particularly its inability to capture conformational ensembles and dynamic allostery. The discussion of AI in molecular dynamics and protein–protein interaction prediction is timely and relevant. The authors appropriately emphasize the importance of ensembles and populations for understanding function, which is a valuable conceptual point.
- **Major Concerns** The manuscript lacks original data or novel insights; it reads as a summary of known issues without offering new perspectives or solutions. The claims about AlphaFold's limitations are not supported by quantitative analysis or case studies. The discussion of AI applications is uneven, with some topics treated superficially. The manuscript does not clearly define its target audience or the specific contribution it makes beyond existing reviews. The absence of figures and detailed examples weakens the argumentation.
- **Minor Comments** Some terminology is used loosely, such as "machine language" instead of "machine learning" in section headings. The manuscript would benefit from a more structured comparison of AlphaFold's capabilities versus other methods. The references are not verifiable from the text, and the authors do not provide a critical assessment of the limitations of the AI methods they discuss.
- **Technical failings that need to be addressed before the case is established** The manuscript does not provide any quantitative evidence or benchmarks to support its claims about AlphaFold's limitations. The discussion of allostery and ensembles is conceptual but lacks concrete examples or simulations. The claim that MD simulations can generate ensembles from AlphaFold structures is plausible but not demonstrated. The manuscript does not address potential counterarguments or alternative views.
- **Assessment against Nature-style criteria** Originality: Low. The manuscript summarizes known limitations of AlphaFold and does not offer new concepts or methods. Scientific importance: Moderate. The topic is important, but the treatment is not sufficiently deep or novel to advance the field. Interdisciplinary readership: Moderate. The manuscript may appeal to structural biologists and computational scientists, but the lack of technical detail limits its reach. Technical soundness: Weak. The claims are not supported by data or rigorous analysis. Readability for nonspecialists: Good. The writing is clear, but the lack of concrete examples reduces accessibility.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript is a reasonable perspective but does not meet the standards for a Nature-style publication due to lack of originality, depth, and technical support.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The manuscript claims that AlphaFold "does not resolve the decades-long protein folding challenge, nor does it identify the folding pathways" and that it "cannot elucidate the mechanisms of allosteric activating driver hotspot mutations nor of allosteric drug resistance."
- **Evidence pointer** Abstract and Introduction, location not provided
- **Concern** These claims are presented as definitive statements without supporting evidence or analysis. While they are likely true, the manuscript does not provide any data, simulations, or case studies to demonstrate these limitations. The authors do not engage with potential counterexamples or discuss the conditions under which AlphaFold might partially capture dynamic features.
- **Why it matters** The central thesis of the manuscript rests on these claims. Without evidence, the argument is assertion rather than demonstration, which weakens the scientific contribution.
- **Resolution test** Provide concrete examples or case studies where AlphaFold predictions fail to capture allosteric mechanisms or conformational ensembles, ideally with quantitative comparisons to experimental data or MD simulations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Originality
- **Claim pointer** The manuscript claims to "briefly overview AI in structural biology, including in molecular dynamics simulations and prediction of microbiota–human protein–protein interactions" and to highlight "advancements accomplished by the deep-learning-powered AlphaFold."
- **Evidence pointer** Abstract and Introduction, location not provided
- **Concern** The manuscript reads as a summary of existing knowledge without offering a novel perspective, framework, or synthesis. The discussion of AI in MD and PPI prediction is superficial and does not critically evaluate the methods or their limitations. The authors do not propose new research directions or hypotheses.
- **Why it matters** For a Nature-style publication, a perspective must offer new insights or a unifying framework. This manuscript does not advance beyond what is already known in the field.
- **Resolution test** Clearly articulate a novel argument or framework that distinguishes this manuscript from existing reviews, and support it with specific examples or analysis.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that "by capturing key features, deep learning techniques can use the single predicted conformation as the basis for generating a diverse ensemble" and that "AI strategies can but will need to go beyond prediction of stabilizing interactions."
- **Evidence pointer** Abstract and Introduction, location not provided
- **Concern** These claims are speculative and not supported by any demonstration or reference to specific methods. The manuscript does not explain how deep learning would generate ensembles from a single structure, nor does it discuss the challenges or limitations of such approaches.
- **Why it matters** The manuscript's proposed path forward is central to its argument, but it is not substantiated. Without technical details or examples, the claims are not credible.
- **Resolution test** Provide a concrete example or reference to a method that generates ensembles from AlphaFold structures, and discuss its validation and limitations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scope coherence
- **Claim pointer** The manuscript discusses "AI and Machine Language in Prediction of Pathogen–Human Host PPIs" as a separate section, but this topic is not clearly connected to the central theme of allostery.
- **Evidence pointer** Section "AI and Machine Language in Prediction of Pathogen–Human Host PPIs", location not provided
- **Concern** The section on PPI prediction feels tangential to the main argument about AlphaFold and allostery. The connection is not explicitly made, and the discussion is brief and lacks depth.
- **Why it matters** The manuscript's focus is diluted, and the reader is left uncertain about the intended scope and message.
- **Resolution test** Either integrate the PPI discussion more tightly with the allostery theme or remove it to sharpen the manuscript's focus.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section headings
- **Evidence pointer** Section "Appications of Artificial Intelligence and Machine Language", location not provided
- **Issue** The heading contains a typo ("Appications" instead of "Applications") and uses "Machine Language" instead of "Machine Learning," which is imprecise.
- **Required correction** Correct the typo and use "Machine Learning" consistently throughout.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Readability
- **Affected element** Introduction
- **Evidence pointer** Introduction, location not provided
- **Issue** The introduction is dense and covers many topics without a clear roadmap for the reader. The transition from AlphaFold's achievements to its limitations is abrupt.
- **Required correction** Provide a brief outline of the manuscript's structure at the end of the introduction to guide the reader.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion of allostery
- **Evidence pointer** Section "The Structure–Function Paradigm Overlooked Ensembles and Dynamic Energy Landscapes", location not provided
- **Issue** The discussion of allostery is conceptual but does not reference specific examples or experimental evidence to illustrate the points.
- **Required correction** Add a concrete example of an allosteric system where AlphaFold predictions are insufficient, to make the argument more tangible.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Terminology
- **Evidence pointer** Throughout, location not provided
- **Issue** The terms "AI," "machine learning," and "deep learning" are used interchangeably in places, which may confuse readers.
- **Required correction** Define these terms early and use them consistently.

## Risk / unsupported claims
- The claim that AlphaFold "cannot elucidate the mechanisms of allosteric activating driver hotspot mutations nor of allosteric drug resistance" is stated without supporting evidence or examples.
- The claim that "deep learning techniques can use the single predicted conformation as the basis for generating a diverse ensemble" is speculative and not substantiated.
- The claim that "AI strategies can but will need to go beyond prediction of stabilizing interactions" is vague and not supported by specific methods or results.
- The assertion that "the cost is prohibitive" for MD simulations at the required scales is not quantified or referenced.
- The statement that "AI-powered algorithms... are already at hand" for the requisite computing power is not supported by specific evidence or references.