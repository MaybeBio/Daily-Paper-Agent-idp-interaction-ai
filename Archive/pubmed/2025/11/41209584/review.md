## Review setup
- **Input scope** Full manuscript text (review article)
- **Assessment boundary** Scientific content, structure, and claims as presented in the provided manuscript text. Figures and tables referenced but not provided are assessed only through textual description.
- **Shared manuscript claim summary** The manuscript is a narrative review summarizing recent advances in cryo-EM and AI-based protein structure prediction, emphasizing their complementary roles, applications in drug discovery and disease understanding, and future directions including integrative and in situ methods.
- **Visible evidence base** The manuscript text includes descriptions of methods, cited examples, and references to figures and tables. No figures, tables, or reference list were provided for direct inspection.
- **Missing materials affecting confidence** Figures 1–5, Tables 1–4, Box 1, and the full reference list were not provided. This limits verification of figure accuracy, table completeness, and citation appropriateness.

## Reviewer
- **Overall assessment** This is a broad, readable review covering the intersection of cryo-EM and AI in protein structure determination. The topic is timely and of interest to a wide structural biology audience. However, the manuscript has several weaknesses: some claims are overstated or imprecise, several examples are misattributed or lack sufficient context, and the depth of analysis varies considerably across sections. The review would benefit from a clearer conceptual framework, more critical evaluation of the cited literature, and careful fact-checking of specific claims.
- **Who would be interested in the results, and why** Structural biologists, computational biologists, and researchers in drug discovery would find this review useful as an entry point to the current state of cryo-EM and AI integration. It may also serve as educational material for students and scientists entering the field.
- **Major strengths** The manuscript covers a timely and important topic. The structure is logical, moving from foundational methods to recent advances and future directions. The inclusion of standards and reproducibility is a valuable addition. The text is generally accessible to nonspecialists.
- **Major Concerns** Several specific claims are inaccurate or poorly supported. The review lacks critical depth in places, sometimes reading as a list of examples rather than a synthesis. The treatment of AI limitations is uneven, and some examples cited do not clearly support the stated conclusions.
- **Minor Comments** The manuscript contains some awkward phrasing and grammatical errors. Some sections are repetitive. The generative AI statement is transparent but the extent of AI use beyond grammar checking is unclear.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5
- **Assessment against Nature-style criteria**  
  *Originality*: The review covers well-trodden ground. While the combination of topics is sensible, the manuscript does not offer a novel perspective or framework that would distinguish it from existing reviews.  
  *Scientific importance*: The topic is important, but the manuscript does not provide a sufficiently critical or comprehensive synthesis to serve as a definitive reference.  
  *Interdisciplinary readership*: The review is accessible to a broad audience, but the lack of depth in some technical areas may limit its value for specialists.  
  *Technical soundness*: Several factual claims are questionable or incorrect, which undermines confidence in the overall accuracy.  
  *Readability for nonspecialists*: The text is generally clear and well-organized, though some sections assume prior knowledge.
- **Recommendation posture** Currently not established from the provided evidence. Major revisions and careful fact-checking are required before the manuscript can be considered for publication.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Accuracy of claims
- **Claim pointer** The manuscript states that "RoseTTAFold predicted the structures of neurodegenerative disease-related proteins such as tau and α-synuclein" in 2022.
- **Evidence pointer** Section "Artificial intelligence (AI) in structure prediction", location not provided
- **Concern** This claim is not supported by the literature. RoseTTAFold is a general protein structure prediction tool, not specifically designed for or demonstrated on tau and α-synuclein in the manner implied. The statement appears to conflate RoseTTAFold with other methods or misattribute specific studies. The authors should provide a specific citation or correct the claim.
- **Why it matters** Inaccurate attribution of specific scientific achievements undermines the credibility of the review and could mislead readers.
- **Resolution test** The authors should verify the claim against the primary literature and either provide a specific, accurate citation or remove the statement.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Accuracy of claims
- **Claim pointer** The manuscript states that "AlphaFold 3 (AF3) represents a major step forward, capable of predicting not just protein structures but also protein–protein, protein–nucleic acid, and protein–ligand interactions using a unified framework."
- **Evidence pointer** Section "Artificial intelligence (AI) in structure prediction", location not provided
- **Concern** While AlphaFold 3 does have expanded capabilities, the claim as stated is overly broad. The manuscript does not discuss the limitations of AF3, such as its performance on ligand interactions being qualitative, as acknowledged later in the same paragraph. The statement should be more nuanced and clearly distinguish between demonstrated capabilities and prospective ones.
- **Why it matters** Overstating the capabilities of a method can mislead readers about its readiness for specific applications, particularly in drug discovery.
- **Resolution test** The authors should revise the claim to accurately reflect the current evidence, including known limitations, and ensure consistency with the later discussion in the same section.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Support for claims
- **Claim pointer** The manuscript states that "integrative modeling has been used to reconstruct the structure of the nuclear pore complex" and later that "AlphaFold2-derived models filled unresolved regions in cryo-EM maps to achieve near-complete reconstruction of this ∼120 MDa."
- **Evidence pointer** Sections "Introduction" and "Applications of high-resolution structural characterization", location not provided
- **Concern** The nuclear pore complex example is mentioned in two places, but the description is inconsistent. In the Introduction, it is cited as an example of integrative modeling, while in the Applications section, it is used as an example of AlphaFold2 filling unresolved regions. The manuscript does not clearly explain how these two statements relate, and the specific studies are not cited. The claim of "near-complete reconstruction" is also vague and should be qualified.
- **Why it matters** Inconsistent and unsupported claims about landmark structures confuse the reader and weaken the review's authority.
- **Resolution test** The authors should provide specific citations for the nuclear pore complex work and clarify the role of integrative modeling versus AlphaFold2 in the described achievements.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Accuracy of claims
- **Claim pointer** The manuscript states that "cryo-EM was used to determine the capsid structure of the monkeypox virus" in 2023.
- **Evidence pointer** Section "Cryo-electron microscopy (Cryo-EM)", location not provided
- **Concern** The manuscript does not provide a citation for this claim. While it is plausible that such a study exists, the lack of a reference makes it impossible to verify. Additionally, the sentence structure is awkward and the claim is presented without context.
- **Why it matters** Uncited specific claims are a serious issue in a review article, as readers cannot trace the original work.
- **Resolution test** The authors should add a proper citation for this claim and provide more context about the significance of the study.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Support for claims
- **Claim pointer** The manuscript states that "recent work using a PDMS-based microfluidic chip achieved tens of milliseconds mixing and freezing, enabling capture of early reaction intermediates" in time-resolved cryo-EM.
- **Evidence pointer** Section "Time-resolved structural biology", location not provided
- **Concern** This claim is presented without a citation. Given the technical specificity of the statement, a reference is essential. Furthermore, the manuscript does not discuss the limitations of this approach, such as the lower resolution mentioned later in the same sentence.
- **Why it matters** Uncited technical claims are not verifiable and reduce the scientific rigor of the review.
- **Resolution test** The authors should provide a citation for this work and discuss its limitations more thoroughly.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract states that cryo-EM and AI have "transformed protein structural biology from a predominantly structure-solving endeavour to a discovery-driven science." This is a strong claim that is not fully developed in the manuscript.
- **Required correction** Consider softening the claim or providing a brief explanation of what "discovery-driven" means in this context.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Accuracy
- **Affected element** Section "Cryo-electron microscopy (Cryo-EM)"
- **Evidence pointer** Section "Cryo-electron microscopy (Cryo-EM)", location not provided
- **Issue** The manuscript states that "cryo-EM was used to determine the capsid structure of the monkeypox virus" but the sentence is grammatically awkward and the claim is presented without context.
- **Required correction** Rewrite the sentence for clarity and add a citation.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Section "Artificial intelligence (AI) in structure prediction"
- **Evidence pointer** Section "Artificial intelligence (AI) in structure prediction", location not provided
- **Issue** The manuscript discusses AlphaFold 2 and AlphaFold 3 but does not clearly explain the relationship between them or the specific improvements in AF3.
- **Required correction** Add a brief comparison of AF2 and AF3 capabilities to help the reader understand the evolution.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "Standards and reproducibility"
- **Evidence pointer** Section "Standards and reproducibility", location not provided
- **Issue** The section on AI-based model standards mentions the need for sharing MSAs and random seeds but does not discuss the practical challenges of doing so.
- **Required correction** Add a brief discussion of the practical barriers to full reproducibility in AI-based modeling.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section "Emerging techniques"
- **Evidence pointer** Section "Emerging techniques", location not provided
- **Issue** The section on emerging techniques is somewhat disjointed, moving from single-molecule microscopy to mass photometry to CLEM without a clear connecting thread.
- **Required correction** Consider adding a brief introductory sentence to frame these techniques as complementary approaches for studying dynamics and native environments.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Accuracy
- **Affected element** Section "Applications of high-resolution structural characterization"
- **Evidence pointer** Section "Applications of high-resolution structural characterization", location not provided
- **Issue** The manuscript states that "cryo-EM was used to resolve the structure of HER2 kinase in complex with a novel inhibitor" but does not provide a citation.
- **Required correction** Add a citation for this claim.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "Challenges and future directions"
- **Evidence pointer** Section "Challenges and future directions", location not provided
- **Issue** The section on challenges and future directions is relatively brief and does not delve deeply into specific technical hurdles or potential solutions.
- **Required correction** Consider expanding this section with more specific examples of ongoing challenges and proposed approaches.

## Risk / unsupported claims
- The claim that RoseTTAFold predicted structures of tau and α-synuclein in 2022 is unsupported and likely inaccurate (R1-M1).
- The claim about AlphaFold 3's capabilities is overstated without discussion of limitations (R1-M2).
- The nuclear pore complex example is described inconsistently and without citations (R1-M3).
- The claim about monkeypox virus capsid structure determination by cryo-EM in 2023 lacks a citation (R1-M4).
- The claim about PDMS-based microfluidic chip achieving tens of milliseconds mixing and freezing in time-resolved cryo-EM lacks a citation (R1-M5).
- The claim about HER2 kinase structure determination by cryo-EM lacks a citation (R1-m6).
- Several other specific examples throughout the manuscript are presented without citations, making them unverifiable.
- The manuscript's overall narrative that cryo-EM and AI have made structural biology "discovery-driven" is asserted but not critically examined.