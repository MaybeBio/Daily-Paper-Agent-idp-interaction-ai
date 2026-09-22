## Review setup

- **Input scope** Full manuscript text (review article)
- **Assessment boundary** Scientific content, structure, and claims as presented in the provided text; no external literature verification
- **Shared manuscript claim summary** The manuscript argues that protein self-interaction (homodimerization and higher-order homo-oligomerization) is a ubiquitous, evolutionarily conserved phenomenon that shapes PPI network topology, provides functional advantages including allosteric regulation and liquid-liquid phase separation, and that dysregulated self-interactions drive human disease. It further claims that recent AI-driven structural prediction methods have transformed our ability to study these systems, and that homotypic interfaces represent promising therapeutic targets.
- **Visible evidence base** Abstract, Introduction, Sections 2-6, Figures 1-4 (referenced but not provided), reference list (cited but not provided)
- **Missing materials affecting confidence** Figures 1-4 (referenced but not viewable), full reference list, any supplementary materials, author contributions, funding statements

## Reviewer

- **Overall assessment** This is a broad, well-structured review covering protein self-interaction from molecular mechanisms to network evolution and therapeutic applications. The manuscript is ambitious in scope and touches on timely topics including AI-driven structural prediction and liquid-liquid phase separation. However, the review suffers from several significant weaknesses: it lacks critical depth in key areas, makes strong claims without adequate supporting evidence, and contains some internal inconsistencies. The treatment of computational methods is uneven, and the therapeutic section, while interesting, is largely speculative without concrete examples. The manuscript would benefit from substantial revision to sharpen its focus, strengthen its evidence base, and improve its critical engagement with the literature.

- **Who would be interested in the results, and why** Structural biologists studying protein oligomerization and macromolecular assemblies; computational biologists working on protein-protein interaction prediction and AI-driven structure determination; evolutionary biologists interested in network evolution and gene duplication; researchers in neurodegeneration and protein misfolding diseases; drug discovery scientists exploring protein-protein interaction interfaces as therapeutic targets. The review provides a useful entry point for researchers new to the field and a broad overview for those seeking to understand the interdisciplinary connections between structural biology, network science, and medicine.

- **Major strengths** 
  1. Comprehensive scope covering experimental, computational, evolutionary, and clinical aspects of protein self-interaction
  2. Timely inclusion of recent AI-driven methods (AlphaFold2/3, protein language models) and their application to homo-oligomer prediction
  3. Good integration of evolutionary perspectives (gene duplication, dosage balance) with structural and functional considerations
  4. Clear articulation of the therapeutic potential of targeting homotypic interfaces, including emerging modalities like molecular glues and PROTACs
  5. Well-organized structure with logical progression from detection/prediction to evolution to function to disease

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The manuscript claims that "SIPs constitute a substantial proportion of proteomes, with estimates ranging from 30 to 50% of all proteins capable of homotypic assembly in broad structural surveys [4] to more domain-specific predictions of ~45% for prokaryotic and ~20% for eukaryotic proteomes [5]."
- **Evidence pointer** Section 1, Introduction; references [4] and [5]
- **Concern** The manuscript presents widely varying estimates of SIP prevalence (30-50% vs 20-45%) without critically evaluating why these estimates differ so substantially. The authors do not discuss the methodological basis for these different estimates, the confidence intervals, or the potential biases in each approach. This is particularly problematic because the prevalence claim is foundational to the entire review's argument that self-interaction is "ubiquitous" and "dominant."
- **Why it matters** If the true prevalence of SIPs is at the lower end of these estimates, the central thesis that self-interaction is a "dominant and biophysically robust evolutionary strategy" would be weakened. Readers need to understand the reliability and limitations of these estimates to properly interpret the review's core claims.
- **Resolution test** The authors should provide a critical comparison of the methodologies used to generate these estimates, discuss potential sources of bias (e.g., detection methods, organism sampling, definition of self-interaction), and offer a more nuanced synthesis of what can be confidently concluded about SIP prevalence.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript states that "AlphaFold3 can generate multiple structural predictions that may reflect different conformational states within homo-oligomeric assemblies" and that "by leveraging its diffusion-based generative framework, AlphaFold3 can sample multiple distinct assembly configurations during inference, providing a principled avenue for probing alternative oligomeric topologies without the need for explicit multi-copy template construction."
- **Evidence pointer** Section 2.2, Computational Approaches
- **Concern** These claims about AlphaFold3's capabilities are presented as established facts, but the manuscript does not provide specific evidence or examples demonstrating that AlphaFold3 can indeed sample distinct conformational states or alternative oligomeric topologies in this manner. The authors also do not acknowledge the significant limitations and controversies surrounding AlphaFold3's accuracy for protein-protein interactions, particularly for homo-oligomers. The claim that diffusion-based sampling provides a "principled avenue" for probing alternative topologies is an interpretation that requires substantiation.
- **Why it matters** The review's discussion of AI-driven methods is a key differentiator and selling point. If the capabilities of AlphaFold3 are overstated or misrepresented, this undermines the credibility of the computational sections and could mislead readers about the current state of the art.
- **Resolution test** The authors should either provide specific published examples demonstrating these AlphaFold3 capabilities, or temper the claims to accurately reflect what has been demonstrated in the literature. They should also discuss known limitations of AlphaFold3 for homo-oligomer prediction, including benchmark results and failure modes.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that "the most compelling translational impact of SIP research resides in the realm of precision therapeutics" and discusses "interfacial allosteric modulators, domain-disrupting stapled peptides, and homotypic molecular glues" as emerging strategies.
- **Evidence pointer** Section 6, Conclusions and Future Perspectives
- **Concern** The therapeutic section is almost entirely speculative. While the authors mention "emerging pharmacological strategies," they provide no specific examples of drugs in development, no clinical trial data, no proof-of-concept studies, and no discussion of the substantial challenges in targeting protein-protein interaction interfaces (e.g., large flat surfaces, lack of small-molecule binding pockets, poor drug-like properties of interface binders). The claim that homotypic interfaces offer "uniquely specific, historically untargeted molecular vulnerabilities" is an assertion without supporting evidence.
- **Why it matters** The therapeutic potential is presented as a major motivation for the review, but without concrete examples or critical assessment of the challenges, this section reads as promotional rather than scholarly. This weakens the overall impact of the review and its usefulness to researchers considering this therapeutic direction.
- **Resolution test** The authors should either provide specific examples of therapeutic candidates targeting homotypic interfaces (with references), discuss the challenges and limitations of this approach in a balanced manner, or substantially temper the claims about therapeutic potential.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Originality
- **Claim pointer** The manuscript claims to provide "a comprehensive overview of the state-of-the-art experimental methodologies" and "advanced computational frameworks" for studying protein self-interactions.
- **Evidence pointer** Section 2, Experimental Detection and Computational Prediction
- **Concern** The review's treatment of experimental methods is surprisingly brief and superficial given the claim of comprehensiveness. The discussion of proximity labeling, AP-MS, and Y2H variants is cursory, with no critical comparison of their relative strengths, limitations, and appropriate applications for studying self-interactions specifically. The computational section, while more detailed, focuses heavily on AlphaFold-related methods and does not adequately cover other important approaches such as co-evolution analysis, docking, or molecular dynamics simulations of oligomeric interfaces.
- **Why it matters** For a review claiming to provide a comprehensive methodological overview, the uneven and shallow treatment of experimental techniques limits its value as a reference. Readers seeking guidance on method selection will not find sufficient critical information.
- **Resolution test** The authors should either expand the experimental methods section to provide more depth and critical comparison, or revise the claim of comprehensiveness to more accurately reflect the scope of the review.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Readability for nonspecialists
- **Claim pointer** The manuscript discusses "liquid-liquid phase separation" and its role in disease, claiming that "aberrant liquid-liquid phase separation transitions linked to neurodegenerative and systemic diseases."
- **Evidence pointer** Abstract, Section 4.3, Section 5
- **Concern** The concept of LLPS is introduced and used extensively, but the physical basis of phase separation (e.g., multivalency, weak multivalent interactions, critical concentration) is not adequately explained for nonspecialist readers. The connection between self-interaction and phase separation is asserted but not mechanistically elaborated. Similarly, the distinction between functional and pathological phase transitions is mentioned but not clearly defined.
- **Why it matters** The review aims to reach a broad interdisciplinary audience, but the treatment of LLPS assumes significant prior knowledge. Nonspecialist readers will struggle to understand the mechanistic arguments and the significance of phase separation in disease.
- **Resolution test** The authors should provide a brief but clear introduction to the physical principles of LLPS, explain how self-interaction drives phase separation, and clarify the differences between functional and pathological phase transitions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 3.1, evolutionary mechanisms list
- **Evidence pointer** Section 3.1
- **Issue** The list of evolutionary mechanisms (exon shuffling, leucine zippers, surface substitutions, indels) is presented without sufficient explanation of how each mechanism specifically contributes to the emergence of self-interaction. The formatting is also inconsistent with the rest of the text.
- **Required correction** Expand each mechanism with a brief explanation of its role in generating homotypic interfaces, and format the list consistently with the rest of the manuscript.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 4.2, enzyme regulation
- **Evidence pointer** Section 4.2
- **Issue** The discussion of enzyme self-interaction mentions hemoglobin and caspase-9 as examples but does not explain the functional significance of their oligomeric states in sufficient detail. The transition from classical examples to recent cryo-EM work is abrupt.
- **Required correction** Provide brief mechanistic explanations of how oligomerization regulates hemoglobin and caspase-9 function, and smooth the transition to the discussion of recent structural work.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Precision
- **Affected element** Section 5, disease discussion
- **Evidence pointer** Section 5
- **Issue** The disease section mentions Alzheimer's disease, Pelizaeus-Merzbacher disease, Parkinson's disease, fragile X syndrome, and sickle cell anemia, but the depth of discussion varies considerably. The connection between self-interaction and each disease is not always clearly articulated.
- **Required correction** Ensure each disease example clearly explains the specific role of self-interaction in pathogenesis, and consider whether all examples are necessary or if some could be consolidated.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** Throughout
- **Issue** The term "self-interacting proteins" (SIPs) is used throughout, but the abbreviation is not defined at first use in the abstract. Some terms such as "structuromic" are used without definition.
- **Required correction** Define SIP at first use in the abstract and define or explain less common terms.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Balance
- **Affected element** Section 2.2, computational methods
- **Evidence pointer** Section 2.2
- **Issue** The discussion of computational methods is heavily weighted toward deep learning approaches, with relatively little attention to classical bioinformatics methods for self-interaction prediction. The SLIPPER and SPAR methods are described, but other important approaches are not mentioned.
- **Required correction** Provide a more balanced overview of computational methods, including classical sequence-based and structure-based approaches, and explain the relative advantages and limitations of different method classes.

## Risk / unsupported claims

1. The claim that AlphaFold3 can "sample multiple distinct assembly configurations during inference" and provide a "principled avenue for probing alternative oligomeric topologies" is not supported by specific evidence or examples in the text.
2. The therapeutic potential claims in Section 6, including the discussion of "interfacial allosteric modulators, domain-disrupting stapled peptides, and homotypic molecular glues," are presented without specific examples, proof-of-concept studies, or discussion of challenges.
3. The statement that "SIPs are found to have greater protein complexity than other protein counterparts, indicated by a larger number of functional protein domains" is presented without supporting data or statistical analysis.
4. The claim that "SIPs are also revealed to be topologically more central in the protein interaction network and consequently tend to be more likely to be functionally essential" implies a causal relationship that may not be supported by the cited correlational evidence.
5. The assertion that "disease-associated mutations are significantly enriched at self-interacting interfaces" (attributed to Schweke et al.) is presented without discussion of the effect size, statistical significance, or potential confounding factors.
6. The manuscript's statement that "no current deep learning architecture autonomously infers the correct oligomeric number from sequence information alone" is a strong negative claim that would require comprehensive literature review to support.
7. The prevalence estimates for SIPs (30-50% vs 20-45%) are presented without critical evaluation of the methodological differences that might explain the discrepancy.