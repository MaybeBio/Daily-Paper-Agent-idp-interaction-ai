## Review setup
- **Input scope** Full manuscript text (abstract, introduction, main sections, summary, and back matter) as provided by the authors.
- **Assessment boundary** Scientific content, internal logic, coverage of the stated topic, and alignment with the journal's stated scope. No assessment of formatting, figures (not provided), or supplementary materials (not provided).
- **Shared manuscript claim summary** The manuscript is a review arguing that multiscale computational modeling, combining physics-based and data-driven approaches, is essential for understanding how phase separation contributes to genome folding across scales, from nucleosomes to nuclear compartments, and that integrating these models with experiments provides mechanistic insight into gene regulation and disease.
- **Visible evidence base** The manuscript text includes descriptions of specific models, simulations, and computational tools, with citations to the primary literature. No figures, tables, or boxes were provided in the submitted material.
- **Missing materials affecting confidence** Figures 1-17, Boxes 1-3, and the full reference list were not provided. This limits the ability to assess the accuracy of figure descriptions, the completeness of the conceptual frameworks, and the appropriateness of specific citations.

## Reviewer
- **Overall assessment** This is a well-structured and comprehensive review that covers a broad and rapidly evolving field. The authors successfully organize a large body of literature into two complementary modeling paradigms and provide a useful synthesis of how these approaches are applied across different genomic scales. The manuscript is clearly written and will be of interest to researchers in computational biology, biophysics, and chromatin biology. However, the review is largely descriptive and would be strengthened by a more critical and comparative analysis of the models discussed. The absence of figures and boxes in the provided material makes it difficult to fully evaluate the pedagogical value of the manuscript. The core claims are generally well-supported by the cited literature, but the review's overall impact would be enhanced by a more explicit discussion of the limitations and unresolved challenges in the field.

- **Who would be interested in the results, and why** Researchers in computational biology, biophysics, and chromatin biology will find this review valuable. It provides a useful entry point for those new to the field and a broad overview for established researchers. The discussion of model validation and identifiability is particularly relevant for practitioners. The review could also serve as a teaching resource for graduate courses in genome biology or computational biophysics.

- **Major strengths**
    1.  The organization of the field into physics-based and data-driven paradigms is clear and effective.
    2.  The review covers a wide range of scales, from nucleosomes to whole nuclear compartments, providing a coherent multiscale perspective.
    3.  The discussion of model validation, identifiability, and uncertainty is a valuable and often-overlooked addition to a review of this type.
    4.  The forward-looking perspective on non-equilibrium and active matter models is timely and thought-provoking.

- **Major Concerns**

    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** No
    - **Axis** Critical analysis and synthesis
    - **Claim pointer** The manuscript claims to "synthesize" and "organize" the field, but the presentation is largely a sequential summary of individual studies.
    - **Evidence pointer** Sections "Phase Separation in Mesoscale Chromatin", "Phase Separation in Chromatin Domains", "Phase Separation in Transcriptional Condensates", "Phase Separation in Nucleosomes, Nucleosome Arrays, and Associated Proteins"
    - **Concern** The review is predominantly descriptive, summarizing the findings of various models without a sufficiently critical comparison of their relative strengths, weaknesses, and domains of applicability. For example, the SBS and MiChroM models are both described, but the reader is not given a clear sense of when one might be more appropriate than the other, or what their key conceptual and practical differences are. The review would be significantly strengthened by a more direct, head-to-head comparison of major models, including their assumptions, limitations, and the specific questions they are best suited to answer.
    - **Why it matters** A review's primary value lies in its synthesis. Without a critical comparison, the manuscript risks being a catalog of models rather than a guide to the field. It does not fully deliver on its promise to help readers "navigate this complexity" as stated in the Introduction.
    - **Resolution test** The authors should add a dedicated section or table that directly compares the major models discussed (e.g., SBS, MiChroM, PAC, etc.) across key axes such as resolution, input data, physical mechanisms included, computational cost, and the types of experimental data they can predict or explain.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Depth of discussion on data-driven methods
    - **Claim pointer** The manuscript claims to cover "data-driven approaches, including machine learning" as a complementary paradigm.
    - **Evidence pointer** Sections "Introduction" and "Phase Separation in Nucleosomes, Nucleosome Arrays, and Associated Proteins"
    - **Concern** The discussion of data-driven and machine learning approaches is significantly less developed than the discussion of physics-based models. While tools like CHROMATIX and predictors like ESPredictor are mentioned, the section lacks the depth and mechanistic insight provided for physics-based models. The review does not adequately discuss the challenges of training these models, the types of data they require, their interpretability, or how they are being integrated with physics-based approaches beyond simple parameterization.
    - **Why it matters** The stated goal is to cover both paradigms. An imbalanced treatment undermines this goal and does not provide a complete picture of the current state of the field, which is increasingly moving towards hybrid approaches.
    - **Resolution test** The authors should expand the discussion of data-driven methods, including a more detailed description of the different types of machine learning models used (e.g., neural networks, random forests), their input features, their predictive targets, and a critical assessment of their current capabilities and limitations.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Validation of claims without figures
    - **Claim pointer** The manuscript frequently refers to figures (e.g., "Figure 1", "Figure 8") to illustrate key concepts and results.
    - **Evidence pointer** Figures 1-17 (not provided)
    - **Concern** The manuscript's arguments are heavily dependent on the figures, which were not provided for review. It is impossible to assess whether the figures accurately represent the described models, data, or concepts. For example, the claim that a "golden mean" principle governs enhancer-promoter communication (Figure 8) cannot be evaluated without seeing the supporting data or schematic.
    - **Why it matters** Figures are a critical component of a review's ability to communicate complex ideas. Without them, the scientific claims cannot be fully assessed, and the manuscript's pedagogical value is diminished.
    - **Resolution test** The authors must provide the figures and their legends for review. The figures should be of high quality, clearly labeled, and directly support the claims made in the text.

- **Minor Comments**

    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity of terminology
    - **Affected element** Introduction, Section "Phase Separation in Mesoscale Chromatin"
    - **Evidence pointer** "location not provided"
    - **Issue** The terms "phase separation," "LLPS," and "condensation" are used throughout, sometimes seemingly interchangeably. While the authors introduce a distinction between LLPS and polymer-polymer phase separation (PPPS), the usage in later sections is not always consistent with this distinction.
    - **Required correction** The authors should ensure consistent use of terminology throughout the manuscript, explicitly referring back to the definitions provided in the Introduction and Box 1.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Readability and structure
    - **Affected element** Section "Model Validation, Identifiability, and Uncertainty"
    - **Evidence pointer** "location not provided"
    - **Issue** This section is a valuable addition, but it feels somewhat disconnected from the main body of the review. The "validation checklist" in Box 2 is a good idea, but the section could be better integrated with the preceding discussions of specific models.
    - **Required correction** The authors could add a brief paragraph at the end of each major section (e.g., on TADs, transcriptional condensates) that explicitly discusses the validation and identifiability challenges specific to the models described in that section.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Completeness of discussion
    - **Affected element** Section "Phase Separation in Transcriptional Condensates"
    - **Evidence pointer** "location not provided"
    - **Issue** The discussion of transcriptional condensates focuses heavily on their role in enhancer-promoter communication. The role of RNA, which is a key component of many transcriptional condensates and can modulate their properties, is mentioned but could be discussed in more depth.
    - **Required correction** The authors should consider adding a more detailed discussion of the role of RNA in the formation, dynamics, and function of transcriptional condensates, and how computational models are beginning to address this.

- **Technical failings that need to be addressed before the case is established**
    - The most significant technical failing is the lack of access to the figures and boxes. The manuscript's claims are often tied to these visual elements, and their absence prevents a full assessment of the review's accuracy and completeness. This must be resolved before a final decision can be made.

## Risk / unsupported claims
- The specific claims about the results of individual models (e.g., the "golden mean" principle, the "elastic ripening" phenomenon) are not directly verifiable from the text alone, as they are presented as summaries of cited work. Their accuracy is dependent on the fidelity of the authors' representation of the primary literature.
- The claim that the field can be "neatly divided" into two paradigms is a simplification, as the authors themselves acknowledge the existence of hybrid approaches. This is a reasonable organizational framework, but it is not a strict dichotomy.
- The claim that computational models are "indispensable" for unraveling the molecular grammar of chromatin is a strong statement. While the evidence presented supports the importance of modeling, the word "indispensable" may be an overstatement, as many key insights have also come from purely experimental approaches.