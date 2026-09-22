## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, technical soundness, and clarity of the review article as provided
- **Shared manuscript claim summary** The authors argue that protein-protein interface dynamics are essential for understanding interaction stability, specificity, and function, and that current modeling approaches (docking, deep learning) rely on static reference structures, necessitating dynamic modeling strategies. They review computational tools (enhanced sampling, coarse-graining, experimental data integration) and discuss how interface dynamics relate to function in globular complexes, fuzzy complexes with intrinsically disordered proteins, and active complexes.
- **Visible evidence base** Full text including abstract, introduction, sections 2.1-2.5, 3.1-3.3, conclusions, and references cited within the text
- **Missing materials affecting confidence** Figures and tables referenced (Figure 1, Figure 2, Figure 3, Table 1, Table 2) are not provided; specific quantitative data from cited studies are not available for verification

## Reviewer
- **Overall assessment** This is a well-structured and timely review that addresses an important gap in the protein-protein interaction modeling field, namely the underappreciation of interface dynamics. The authors provide a broad survey of computational methods and functional contexts, with a clear narrative arc from tools to biological implications. However, the review's impact is limited by a lack of critical evaluation of the methods discussed, an absence of quantitative comparisons or benchmarks, and a somewhat superficial treatment of some topics (e.g., deep learning methods are mentioned but not integrated into the dynamic framework). The manuscript is readable and logically organized, but would benefit from a more rigorous synthesis and clearer articulation of open challenges.
- **Who would be interested in the results, and why** Computational structural biologists, biophysicists, and researchers in protein engineering and drug discovery would find this review useful as an entry point to dynamic interface modeling. The discussion of fuzzy complexes and active interfaces may also appeal to biochemists studying intrinsically disordered proteins and molecular machines. The review's emphasis on the need for dynamic benchmarks could inform method developers in the docking and AI/ML communities.
- **Major strengths** The review fills a niche by focusing specifically on interface dynamics rather than static structures, which is a timely perspective given recent advances in deep learning-based structure prediction. The organization is clear, moving from computational tools to functional implications, and the inclusion of diverse examples (e.g., RecA, microtubules, Rho, HSP70/HSP40) illustrates the breadth of the topic. The discussion of experimental data integration (NMR, cross-linking, SAXS) is valuable and highlights practical strategies for dynamic modeling.
- **Major Concerns** The review lacks critical assessment of the methods it surveys; for example, no comparison of the accuracy, computational cost, or limitations of enhanced sampling versus coarse-grained approaches is provided. The treatment of deep learning methods is cursory, despite their prominence in the field, and the authors do not address how these methods might incorporate dynamics. The functional sections (3.1-3.3) are descriptive rather than analytical, with limited mechanistic insight into how dynamics encode function. The conclusions are somewhat generic and do not propose concrete next steps or testable hypotheses.
- **Minor Comments** The manuscript would benefit from a summary table comparing the strengths and weaknesses of the discussed methods. Some statements are overly broad (e.g., "more and more data point to the fact that the interaction stability and specificity is encoded in the dynamics") and would benefit from specific citations or examples. The use of "E Pur Si Muove!" as a section title is engaging but may be obscure for some readers; a brief explanation would improve accessibility.
- **Technical failings that need to be addressed before the case is established** The core argument that dynamics must be incorporated into interface modeling is plausible but not rigorously supported with quantitative evidence. The authors do not provide a systematic analysis of how dynamic criteria improve model ranking or prediction accuracy compared to static approaches, beyond citing individual studies. Without such evidence, the case for a paradigm shift is not fully established.
- **Assessment against Nature-style criteria** Originality: Moderate. The focus on interface dynamics is not entirely novel, but the synthesis of tools and functional contexts is a useful contribution. Scientific importance: High. The topic is relevant to a broad community, and the call for dynamic benchmarks is timely. Interdisciplinary readership: Moderate. The review is accessible to computational biologists but may be less engaging for experimentalists due to the heavy focus on simulation methods. Technical soundness: Adequate. The methods described are accurately represented, but the lack of critical evaluation weakens the technical depth. Readability for nonspecialists: Good. The prose is clear, and the examples are illustrative, though some jargon (e.g., "dynasome") is introduced without sufficient explanation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors claim that "interaction stability and specificity is encoded in the dynamics of these interfaces" and that dynamic information "must be taken into account when modeling and assessing protein interactions."
- **Evidence pointer** Abstract; Section 1 (Introduction); Section 3 (general discussion)
- **Concern** The central thesis of the review is stated as a fact, but the supporting evidence is largely anecdotal, drawing on selected examples without a systematic or quantitative demonstration. The authors do not provide a comparative analysis showing that dynamics-based approaches outperform static methods in predicting interface stability or specificity, nor do they address potential counterexamples where static structures suffice.
- **Why it matters** If the claim is not rigorously supported, the review's rationale for advocating dynamic modeling is weakened, and readers may question the practical value of the proposed approaches.
- **Resolution test** The authors should either (a) provide a meta-analysis or summary of studies that quantitatively compare dynamic versus static modeling outcomes, or (b) explicitly frame the claim as a hypothesis with supporting evidence and acknowledge limitations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Scope and depth
- **Claim pointer** The review claims to cover "recent computational strategies aiming at investigating protein-protein interfaces in a dynamic fashion using enhanced sampling, multi-scale modeling, and experimental data integration."
- **Evidence pointer** Section 2 (Tools for Calculating PPI Dynamics)
- **Concern** The treatment of methods is uneven. Enhanced sampling and coarse-graining are described with some detail, but the discussion of experimental data integration is brief and lacks concrete examples of how data (e.g., NMR restraints, cross-linking) are converted into dynamic models. Deep learning methods, which are mentioned in the introduction, are not integrated into the dynamic framework, leaving a significant gap given their current prominence.
- **Why it matters** A review should provide a balanced and comprehensive overview. The omission of deep learning in the context of dynamics, and the superficial treatment of experimental integration, limits the review's utility as a reference for researchers seeking to adopt these methods.
- **Resolution test** The authors should expand the section on experimental data integration with specific case studies, and add a subsection or discussion on how deep learning approaches (e.g., AlphaFold, protein language models) could be extended to incorporate dynamics or be used in conjunction with simulation methods.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Analytical depth
- **Claim pointer** The authors state that "interface dynamics report on the function of protein assemblies" and discuss examples in globular complexes, fuzzy complexes, and active complexes.
- **Evidence pointer** Section 3 (E Pur Si Muove! How Can We Relate Protein Function to Interfaces Dynamics?)
- **Concern** The functional sections are largely descriptive, summarizing individual studies without synthesizing common principles or mechanisms. For example, the discussion of microtubules and RecA describes dynamic behaviors but does not extract generalizable insights about how interface dynamics control function (e.g., allostery, mechanotransduction). The section on fuzzy complexes is particularly thin, given the growing literature on this topic.
- **Why it matters** The review's value lies in its ability to provide conceptual frameworks that guide future research. Without analytical synthesis, the sections read as a catalog of examples rather than a coherent argument.
- **Resolution test** The authors should add a comparative discussion that identifies recurring themes (e.g., the role of conformational entropy, the balance between stability and plasticity) and propose hypotheses about how dynamics encode function across different complex types.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 3 title
- **Evidence pointer** Section 3 heading
- **Issue** The title "E Pur Si Muove!" is a literary reference that may not be universally recognized, and its relevance to the section content is not immediately clear.
- **Required correction** Add a brief parenthetical explanation or rephrase the title to be more descriptive, e.g., "Relating Interface Dynamics to Protein Function."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2.5
- **Evidence pointer** Table 1 (referenced but not provided)
- **Issue** The text lists several analysis tools but does not provide a critical comparison of their features, usability, or applicability to different systems. The referenced table is not available for review.
- **Required correction** In the text, add a sentence summarizing the key differences between the tools (e.g., input formats, supported analyses, scalability) to aid readers in tool selection.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Precision
- **Affected element** Section 3.3
- **Evidence pointer** Section 3.3, paragraph on RecA
- **Issue** The statement that "the totality of interface residue-residue contacts between rigid regions are lost when ATP is hydrolyzed" is strong and may depend on the specific system and analysis method. The authors do not provide the quantitative details (e.g., percentage of contacts lost, time scale) to support this claim.
- **Required correction** Qualify the statement with the specific conditions (e.g., "in the RecA filament studied by [reference], nearly all contacts were lost") and provide the relevant data or citation.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section 4 (Conclusions and Perspectives)
- **Evidence pointer** Section 4
- **Issue** The term "dynasome" is introduced without a clear definition, and the connection to the MoDel database is not fully explained.
- **Required correction** Define "dynasome" explicitly (e.g., "the ensemble of conformational states accessible to a protein") and clarify how MoDel relates to this concept.

## Risk / unsupported claims
- The claim that "interaction stability and specificity is encoded in the dynamics" is presented as established but is not quantitatively supported in the text.
- The statement that "more and more data point to the fact" (Introduction) is vague and lacks specific citations to substantiate the trend.
- The assertion that "none of these aspects provide enough sampling to report on the stability and specificity of the complexes" (Introduction) is made without a benchmark or comparative evidence.
- The claim regarding RecA that "the totality of interface residue-residue contacts between rigid regions are lost" is not accompanied by quantitative data or a specific citation.
- The review's implicit suggestion that dynamic modeling is necessary for all protein-protein interfaces is not qualified by cases where static models may be sufficient.