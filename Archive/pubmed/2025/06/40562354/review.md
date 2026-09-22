## Review setup
- **Input scope** Full manuscript text (review article, no experimental data)
- **Assessment boundary** Scientific content, logical coherence, completeness of coverage, and alignment with stated aims; no assessment of experimental reproducibility as no primary data are presented
- **Shared manuscript claim summary** The authors argue that NMR spectroscopy remains an indispensable and versatile tool in modern biomedical research and drug discovery, extending well beyond traditional structural biology. They emphasize its unique capabilities for studying dynamic and intrinsically disordered systems, its utility in cellular and metabolic contexts, its complementary role to X-ray crystallography and cryo-EM, and its potential to be enhanced by and to validate artificial intelligence-based structure prediction. They also highlight ongoing challenges and opportunities, including sample preparation, sensitivity, and attracting new practitioners.
- **Visible evidence base** The manuscript is a narrative review. Evidence is presented in the form of cited literature (references 1-205), a table of software packages (Table 1), and three figures (Figure 1: LEGO NMR labeling of HIV-1 Vif-CBFβ; Figure 2: NMR structures of dynamic proteasome regions and hRpn13 complexes; Figure 3: NMR-based metabolomics workflow and D-2HG detection). No primary experimental data are included.
- **Missing materials affecting confidence** The figures and Table 1 were not provided in the submitted material. Reference list was not provided. This limits verification of specific claims tied to figures and the completeness of the software list. The manuscript's conclusions are largely qualitative and depend on the cited literature, which could not be independently assessed.

## Reviewer
- **Overall assessment** This is a well-written and comprehensive review that effectively argues for the continued relevance of NMR in biomedical research. The authors successfully position NMR as a complementary, not competing, technology to cryo-EM and X-ray crystallography, and they make a strong case for its unique value in studying dynamics, disorder, and metabolic processes. The discussion of AI integration is timely and balanced, acknowledging both the power of prediction and the need for experimental validation. The manuscript is accessible and logically structured. However, the review is largely descriptive and could be strengthened by a more critical and forward-looking analysis of the field's key bottlenecks and potential breakthroughs. The absence of the figures and table in the review package limits a full assessment of the illustrative material.
- **Who would be interested in the results, and why** This review will be of interest to a broad audience within the biomedical research community. This includes: (1) structural biologists using or considering NMR, cryo-EM, or X-ray crystallography, who will find the discussion of complementarity useful; (2) researchers studying intrinsically disordered proteins and dynamic systems, who will appreciate the focused discussion of NMR's unique capabilities; (3) drug discovery scientists, particularly those involved in fragment-based screening and PROTAC development; (4) metabolomics researchers and clinicians interested in biomarker discovery and treatment monitoring; and (5) computational biologists and AI developers seeking to understand how experimental data can be integrated with or validate prediction tools. The review is timely given the ongoing debate about the role of experimental structural biology in the age of AI.
- **Major strengths**
  1. The review provides a clear and compelling argument for the unique and ongoing value of NMR, effectively countering the narrative that AI and other structural methods have diminished its importance.
  2. The scope is broad yet well-organized, covering sample preparation, structural biology, dynamics, cellular applications, metabolomics, and AI integration, which provides a holistic view of the field.
  3. The use of specific, illustrative examples (e.g., HIV-1 Vif-CBFβ, proteasome subunits, D-2HG in gliomas) grounds the discussion in concrete applications and enhances readability.
  4. The discussion of the synergy between NMR and other techniques (cryo-EM, X-ray crystallography, AI) is balanced and constructive, highlighting a path forward for the field.
  5. The manuscript is well-written and accessible to a non-specialist, avoiding excessive technical jargon while still conveying the core concepts.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific Depth and Critical Analysis
  - **Claim pointer** The review summarizes the strengths and limitations of NMR but does not deeply analyze the fundamental challenges that limit its broader application, such as sensitivity and spectral complexity, nor does it critically evaluate the potential of emerging solutions (e.g., hyperpolarization, faster MAS, novel pulse sequences) to overcome them.
  - **Evidence pointer** Sections "Perspective" and throughout the manuscript.
  - **Concern** The review is largely descriptive, presenting a catalog of applications and challenges without a critical, in-depth analysis of the field's trajectory. For instance, the "Perspective" section mentions key challenges (size limitations, spectral complexity, low sensitivity) but does not discuss in any detail the specific research fronts aimed at solving these problems. A more critical discussion of the potential impact of emerging technologies (e.g., dissolution DNP, 1H-detected MAS at fast spinning speeds, or advances in quantum sensing) would significantly strengthen the review's value for experts and provide a clearer vision for the future.
  - **Why it matters** A review in a high-impact journal should not only summarize the state of the art but also provide a critical analysis of the field's key problems and potential solutions. Without this, the review risks being a summary of known facts rather than a thought-provoking piece that guides future research.
  - **Resolution test** The authors should add a section or expand the "Perspective" to critically evaluate 2-3 specific technological or methodological breakthroughs that could address the major limitations they identify. This should include a discussion of the feasibility, potential impact, and remaining hurdles for these approaches.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Completeness of Coverage
  - **Claim pointer** The review focuses heavily on solution-state NMR for proteins and metabolomics, but its claim to cover "modern biomedical research and drug discovery" is broad. The coverage of solid-state NMR (MAS) is limited to a single example (TET2), and its growing importance for studying amyloid fibrils, membrane proteins, and intact cells is not adequately discussed.
  - **Evidence pointer** Sections "NMR of systems in motion" and "Synergy of NMR with x-ray crystallography and cryo-EM".
  - **Concern** The review's scope is ambitious, but the coverage is uneven. While solution-state NMR is covered extensively, solid-state NMR (ssNMR) is only briefly mentioned. Given the significant recent advances in ssNMR for studying challenging biological systems like amyloids (e.g., α-synuclein fibrils), membrane proteins, and native cellular environments, a more substantial discussion of this technique is warranted to fully support the claim of comprehensive coverage.
  - **Why it matters** The stated aim is to cover NMR in "modern biomedical research." Omitting a major branch of the technique, which is uniquely suited for systems that are inaccessible to solution-state NMR, weakens the review's authority and comprehensiveness.
  - **Resolution test** The authors should add a dedicated section or expand existing sections to discuss the unique contributions and recent advances of solid-state NMR in biomedical research, with specific examples of its application to amyloids, membrane proteins, or in-cell settings.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Balance and Objectivity
  - **Claim pointer** The review presents a strongly positive view of NMR's capabilities. While it mentions limitations, it does not critically evaluate the practical advantages of alternative techniques (e.g., cryo-EM for large complexes, AlphaFold for static structures) in a way that gives the reader a clear framework for choosing the right tool for a given biological question.
  - **Evidence pointer** Sections "NMR and the Protein Data Bank" and "Synergy of NMR with x-ray crystallography and cryo-EM".
  - **Concern** The review is written from a clear pro-NMR perspective. While this is understandable, a more balanced analysis of when NMR is the method of choice versus when cryo-EM or X-ray crystallography (or AI prediction) is more appropriate would be more useful for the reader. For example, the discussion of the PDB statistics dismisses the low percentage of NMR structures without a thorough discussion of the reasons (e.g., size limits, cost, expertise) and the contexts where this is a genuine limitation.
  - **Why it matters** For a review aimed at a broad audience, including non-NMR specialists, an objective comparison of techniques is crucial for informed decision-making. A one-sided perspective may mislead readers about the relative utility of different methods.
  - **Resolution test** The authors should add a more explicit comparative discussion, perhaps a table or a dedicated section, that outlines the strengths and weaknesses of NMR, cryo-EM, and X-ray crystallography for different types of biological questions (e.g., size, dynamics, disorder, membrane proteins, high-throughput screening).
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity and Presentation
  - **Affected element** Section "NMR and advances in artificial intelligence"
  - **Evidence pointer** Section "NMR and advances in artificial intelligence"
  - **Issue** The section on AI, while interesting, reads as a list of applications (assignment, reconstruction, structure prediction) without a clear narrative thread. The connection between the challenges of NMR (complexity, labor-intensive analysis) and how specific AI tools address them could be made more explicit.
  - **Required correction** Consider restructuring this section to first clearly state the key bottlenecks in NMR data analysis and interpretation, and then discuss how AI-based tools are being developed to address each specific bottleneck. This will create a more logical and compelling argument for the synergy between the two fields.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness of Coverage
  - **Affected element** Section "Use of NMR for molecular targeting"
  - **Evidence pointer** Section "Use of NMR for molecular targeting"
  - **Issue** The section on drug discovery focuses on fragment-based screening and PROTACs. The discussion of other important NMR-based techniques in drug discovery, such as STD-NMR and WaterLOGSY, is present but brief. The section could be strengthened by a more detailed discussion of the information content provided by these techniques (e.g., epitope mapping, binding kinetics) and their role in the drug discovery pipeline.
  - **Required correction** Expand the discussion of ligand-based screening methods to more clearly explain what unique information they provide (e.g., binding affinity, binding site, kinetics) and how this information is used in the drug discovery process.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Readability for Nonspecialists
  - **Affected element** Section "Select 13C-labeling of methyl groups and the TROSY effect"
  - **Evidence pointer** Section "Select 13C-labeling of methyl groups and the TROSY effect"
  - **Issue** The explanation of the TROSY effect, while accurate, is dense and may be difficult for a nonspecialist to follow. The physical basis of the effect (cancellation of DD and CSA relaxation mechanisms) is stated, but the practical significance (e.g., "this allows us to see bigger proteins") could be emphasized more clearly.
  - **Required correction** Add a sentence or two at the beginning or end of the TROSY discussion that explicitly states the practical benefit in simple terms (e.g., "This effect allows NMR to be applied to much larger protein complexes than was previously possible, such as the 670 kDa proteasome.").
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Technical Soundness
  - **Affected element** Section "NMR and the Protein Data Bank"
  - **Evidence pointer** Section "NMR and the Protein Data Bank"
  - **Issue** The statement "NMR is frequently judged harshly for contributing <10 % of the structures in the Protein Data Bank (PDB)" is presented without a citation. While this is a commonly known statistic, providing a reference or a more precise figure would strengthen the claim.
  - **Required correction** Add a citation for the PDB statistics or rephrase to "as of 2024, NMR structures represent approximately X% of the PDB" with a reference.
- **Technical failings that need to be addressed before the case is established** No technical failings were identified in the manuscript's logic or claims. The review is a synthesis of existing literature, and the arguments presented are consistent with the current understanding of the field. The main limitations are the lack of critical depth and uneven coverage, as detailed in Major Concerns R1-M1 and R1-M2.
- **Assessment against Nature-style criteria**
  - **Originality:** The review does not present novel experimental data or a fundamentally new conceptual framework. Its originality lies in the specific synthesis of topics, particularly the integration of NMR with AI and the focus on dynamics and disorder. However, the overall message of NMR's complementarity is not new.
  - **Scientific importance:** The topic is of high importance. The review addresses a timely and relevant debate about the role of experimental structural biology in the era of AI. It successfully articulates the unique and ongoing contributions of NMR, which is important for the field's visibility and funding.
  - **Interdisciplinary readership:** The review has the potential to appeal to a broad readership, including structural biologists, chemists, biochemists, cell biologists, and drug discovery researchers. The clear writing and use of illustrative examples help make it accessible.
  - **Technical soundness:** The technical content is sound and accurately represents the current state of NMR methodology. The claims are appropriately supported by citations to the primary literature.
  - **Readability for nonspecialists:** The manuscript is generally well-written and accessible. However, some sections, such as the TROSY explanation, are dense and could be improved for a broader audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript is a well-written and timely review that makes a valid and important argument. The major concerns are not about the accuracy of the content but about the depth of critical analysis and the completeness of coverage. Addressing these concerns would elevate the review from a good summary to a more insightful and influential piece. The minor comments are mostly editorial and would improve clarity and accessibility.

## Risk / unsupported claims
- The claim that NMR is "uniquely suited" for studies of intrinsically disordered and dynamic systems is well-supported by the cited literature and is a widely accepted view.
- The claim that AI-based methods like AlphaFold have "struggled to predict structures of intrinsically disordered sequences" is supported by a citation and is generally accurate, though the field is rapidly evolving.
- The claim that NMR can "reliably report false positives" for AI-predicted protein-protein interactions is presented as a potential application. While plausible, this is more of a forward-looking suggestion than an established fact, and the manuscript does not provide specific examples of this being done on a large scale.
- The statement regarding the percentage of NMR structures in the PDB is presented without a specific citation, making it difficult to verify the exact figure.
- The overall claim that NMR is "aptly suited to bench-to-bedside efforts" is supported by examples in metabolomics, but the review does not deeply discuss the practical challenges of implementing NMR in clinical settings, which are significant. This claim is somewhat overstated relative to the evidence presented.