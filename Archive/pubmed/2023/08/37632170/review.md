## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods) for the article "Computational analysis of regulatory regions in human protein kinases" by Pei and Cong.
- **Assessment boundary** The review assesses the scientific claims, methodology, and evidence presented in the manuscript. It does not assess the editorial fit for a specific journal, but evaluates the work against general Nature-style criteria for originality, significance, technical soundness, and readability.
- **Shared manuscript claim summary** The authors use AlphaFold structural models of 496 human protein kinases to systematically identify intramolecular contacts between kinase domains (KDs) and other regions, including globular domains, N- and C-terminal tails, long insertions, and distal nonglobular regions. They identify 35 types of KD-interacting globular domains, prevalent KD-flanking region interactions, and specific long-range interactions that may have regulatory roles, including autoinhibition.
- **Visible evidence base** The manuscript text includes descriptions of results, figures (Figure 1a-d, 2a-d, 3, 4a-f, 5a-f, 6a-e, 7a-d, 8a-d, 9a-f), and supplementary materials (Table S1, Figures S1-S2). The methods section describes the criteria for defining contacts (distance and PAE) and the tools used (AlphaFold, DPAM, STRIDE, IUPred2A, AL2CO).
- **Missing materials affecting confidence** The figures and supplementary tables/figures themselves were not provided for review. This limits the ability to fully verify the quantitative results and the visual evidence for the described interactions. Specific numerical data (e.g., counts of contacts per category, statistical significance of enrichment/depletion) are not fully detailed in the text.

## Reviewer
- **Overall assessment** This manuscript presents a systematic and potentially valuable computational analysis of intramolecular interactions in human protein kinases using AlphaFold models. The authors identify a wide range of interactions between kinase domains and other regions, and they provide specific examples of interactions that may be involved in autoinhibition. The work is a useful resource for the kinase community. However, the manuscript is largely descriptive, and the functional significance of the identified interactions is mostly inferred. The main claims are supported by the described methodology, but the lack of detailed quantitative data and the absence of the figures themselves in the provided material prevent a full assessment of the strength of the evidence. The study's novelty is moderate, as it applies existing tools (AlphaFold) to a well-studied protein family.
- **Who would be interested in the results, and why** Researchers in the fields of protein kinase biology, signal transduction, structural biology, and computational biology would be interested. The catalog of potential regulatory interactions provides a resource for generating hypotheses about kinase regulation, autoinhibition, and allostery. It could also be of interest to those studying the evolution of domain architectures in signaling proteins.
- **Major strengths**
    1.  The study addresses a significant and challenging problem: understanding the regulatory roles of nonglobular regions and interdomain interactions in a large and important protein family.
    2.  The use of AlphaFold models to systematically survey intramolecular interactions across the entire human kinome is a timely and powerful approach.
    3.  The analysis identifies a broad range of interaction types (globular domains, tails, insertions, distal regions) and provides specific, structurally detailed examples (e.g., HASPIN, MAPK7, MAPK15, SIK1B) that offer new insights into potential regulatory mechanisms.
    4.  The methodology is clearly described, and the criteria for defining contacts are explicit.
- **Major Concerns**
    - **R1-M1**
        - **Severity** Major
        - **Blocking** No
        - **Axis** Evidence strength and validation
        - **Claim pointer** The authors claim that the identified intramolecular interactions "could contribute to orthosteric or allosteric regulation of kinase activity" and that specific distal segments "could provide autoinhibition by blocking ATP binding."
        - **Evidence pointer** Results sections "Characterization of globular domains interacting with KDs", "KD interactions from long insertions inside the KDs", "Potential regulatory regions distal to KDs"; Figures 4-9.
        - **Concern** The functional significance of the identified interactions is largely inferred from the static AlphaFold models. While the authors note that some interactions are consistent with experimental data, the manuscript does not provide experimental validation for the novel predictions, nor does it systematically compare the predicted regulatory interactions with known regulatory mechanisms or mutations. The claim that these interactions "could" have regulatory roles is appropriately cautious, but the evidence for their functional importance is weak.
        - **Why it matters** The primary value of this study is in generating hypotheses. Without experimental validation or a stronger link to known functional data, the significance of the specific predictions remains uncertain. The manuscript would be strengthened by a more thorough discussion of how the predicted interactions relate to existing experimental evidence for autoinhibition or allostery in the specific kinases highlighted.
        - **Resolution test** The authors should either (1) provide experimental evidence for at least one or two of the novel predicted regulatory interactions, or (2) significantly expand the discussion to systematically compare their predictions with the existing experimental literature on kinase regulation, highlighting where their models provide new mechanistic insights and where they conflict with or are not supported by current data.
    - **R1-M2**
        - **Severity** Major
        - **Blocking** No
        - **Axis** Quantitative rigor and clarity
        - **Claim pointer** The authors state that "N-tail and C-tail (within 80 residues of KDs) nonglobular regions contribute the most numbers of contacts" and that "Globular domains and long insertions inside KDs each contribute to about 2000 contacts, about one-fifth of those from N-tail or C-tail."
        - **Evidence pointer** Results section "Identification of globular domains and nonglobular regions interacting with KDs"; Figure 1c.
        - **Concern** The quantitative analysis is presented at a high level. The manuscript lacks a detailed breakdown of the number of contacts per category, the number of kinases involved in each type of interaction, and any statistical analysis of the enrichment or depletion of interactions with specific KD structural elements. The text mentions "about 26,000 such residue-residue contacts" and "about 2000 contacts" for globular domains, but the basis for these numbers and their significance is not fully explored.
        - **Why it matters** A more detailed quantitative analysis would strengthen the descriptive findings and allow readers to better assess the prevalence and potential importance of different interaction types. For example, are certain KD structural elements (e.g., the activation loop) preferentially targeted by regulatory domains? Is there a correlation between interaction strength (e.g., PAE) and functional significance?
        - **Resolution test** The authors should provide a more detailed quantitative breakdown of the contacts, including the number of kinases with each interaction type, the distribution of contacts across KD structural elements, and statistical tests for enrichment or depletion. This could be presented in a supplementary table or a more detailed figure.
    - **R1-M3**
        - **Severity** Major
        - **Blocking** No
        - **Axis** Technical validation of AlphaFold predictions
        - **Claim pointer** The authors use AlphaFold models to identify intramolecular contacts, relying on both distance and PAE criteria.
        - **Evidence pointer** Materials and Methods section "Identification of globular domains and nonglobular regions interacting with KDs"; Figure S1.
        - **Concern** The manuscript does not include a systematic validation of the AlphaFold-predicted interactions against known experimental structures. While the authors mention that some interactions are consistent with experimental structures (e.g., CSK), a broader comparison would increase confidence in the predictions. The choice of the PAE cutoff (12 Å) and the distance cutoff (5 Å) is described, but the sensitivity and specificity of these cutoffs are not evaluated.
        - **Why it matters** AlphaFold models are predictions, and their accuracy can vary, especially for interdomain arrangements and disordered regions. A systematic comparison with experimentally determined structures of multi-domain kinases would help validate the approach and identify potential limitations.
        - **Resolution test** The authors should compare their predicted interdomain contacts with a set of experimentally determined structures of human protein kinases (e.g., from the PDB) to assess the accuracy of their method. This could be presented as a validation set, showing the fraction of predicted contacts that are observed in the experimental structures.

- **Minor Comments**
    - **R1-m1**
        - **Severity** Minor
        - **Axis** Clarity and presentation
        - **Affected element** Abstract and Introduction
        - **Evidence pointer** Abstract, Introduction
        - **Issue** The abstract and introduction are dense and could be more accessible to a broader audience. The significance of the "regulatory regions" concept and the specific advantages of using AlphaFold for this purpose could be stated more clearly.
        - **Required correction** Consider revising the abstract and introduction to more explicitly state the gap in knowledge (e.g., the difficulty in studying flexible regions) and how the systematic AlphaFold-based approach addresses this gap.
    - **R1-m2**
        - **Severity** Minor
        - **Axis** Data availability
        - **Affected element** Results and Methods
        - **Evidence pointer** Results sections, Materials and Methods
        - **Issue** The manuscript would benefit from a clear statement on data availability, including the list of all human protein kinases analyzed, their UniProt IDs, and the specific AlphaFold model versions used. The coordinates of the predicted interactions for the highlighted examples (e.g., HASPIN, MAPK7) should be made available.
        - **Required correction** Add a "Data Availability" section that specifies where the list of kinases, the AlphaFold models, and any analysis scripts can be accessed.
    - **R1-m3**
        - **Severity** Minor
        - **Axis** Figure quality
        - **Affected element** Figures 1-9
        - **Evidence pointer** Figures 1-9
        - **Issue** The figures were not provided for review. Based on the text, it is unclear if the figures clearly show the interactions described. For example, in Figure 4, it is not clear if the different interaction modes of SH2/SH3 domains are easily comparable across the different kinases.
        - **Required correction** Ensure that figures are high-resolution and clearly labeled, with consistent coloring and orientation for comparative purposes. Consider using surface representations or schematic diagrams to better illustrate the interaction interfaces.

## Risk / unsupported claims
- The claim that the identified interactions "could contribute to orthosteric or allosteric regulation" is a hypothesis, not a demonstrated fact, and is appropriately framed as such. However, the manuscript does not provide a clear path to test these hypotheses.
- The specific functional roles of the distal segments in MAPK7, MAPK15, and SIK1B are inferred from their location in the ATP-binding cleft. While this is a reasonable hypothesis, it is not directly supported by experimental evidence presented in this manuscript.
- The statement that "regulatory regions in disordered parts of the protein may not have strong signals from multiple sequence alignments" is a plausible explanation for the low number of long-range interactions, but it is not directly tested.
- The claim that the interaction between the PH domain and the pseudokinase domain in JAK family kinases "could be important to regulate the activity" is speculative and not supported by functional data in this study.
- The overall prevalence and significance of the identified interactions are not quantified in a way that allows for a robust assessment of their biological importance.