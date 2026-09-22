## Review setup
- **Input scope** Full manuscript text (review article, published in Frontiers in Molecular Biosciences, 2021)
- **Assessment boundary** Scientific content, technical soundness, clarity, and alignment with stated aims; assessment is based solely on the provided manuscript text
- **Shared manuscript claim summary** The manuscript argues that combining single-molecule fluorescence microscopy and molecular dynamics simulations provides a powerful and complementary approach to characterize the molecular actions of DNA-binding proteins on DNA and within liquid-liquid phase-separated condensates, using p53 as a model system
- **Visible evidence base** Abstract, Introduction, sections on sliding, hopping/jumping, intersegmental transfer, liquid-liquid phase separation, summary, and author/funding statements. No figures, tables, or supplementary materials were provided
- **Missing materials affecting confidence** Figures (including Figure 1 and Figure 2 referenced in text), figure legends, any supplementary data, and full methodological details for cited experimental and simulation studies. Without these, quantitative claims and visual representations cannot be independently verified

## Reviewer
- **Overall assessment** This is a well-structured and readable review that synthesizes recent work on p53 target search mechanisms and liquid-liquid phase separation, highlighting the complementary roles of single-molecule microscopy and molecular dynamics simulations. The manuscript is informative for a broad biophysics audience and provides a useful conceptual framework. However, the review is largely descriptive and relies heavily on the author's own prior publications, with limited critical evaluation of conflicting results or methodological limitations. The absence of figures in the provided material limits full assessment of the presented data. The manuscript would benefit from a more balanced discussion of alternative interpretations and unresolved questions in the field.
- **Who would be interested in the results, and why** Researchers in biophysics, molecular biology, and computational biology studying protein-DNA interactions, facilitated diffusion, and biomolecular condensates. The review is also relevant to those interested in methodological integration of experimental and computational approaches. The focus on p53 may attract cancer biology researchers, though the content is primarily mechanistic rather than disease-oriented.
- **Major strengths** The manuscript provides a clear and concise overview of the four target search mechanisms and how single-molecule and simulation approaches have contributed to their characterization. The use of p53 as a unifying model system is effective. The discussion of liquid-liquid phase separation is timely and connects two research areas that are often treated separately. The writing is accessible and logically organized.
- **Major Concerns** The review is heavily centered on the author's own work, which may introduce bias in the selection and interpretation of studies. Several claims are presented without sufficient critical discussion of contradictory evidence or methodological caveats. The section on hopping and jumping acknowledges a technical limitation (time resolution) but does not fully explore how this affects the interpretation of the cited results. The liquid-liquid phase separation section introduces a specific study (Kamagata et al., 2021c) with detailed findings, but the generalizability of these results to other systems is not critically examined. The manuscript lacks a clear statement of the criteria used to select the studies discussed, which limits its value as an unbiased review.
- **Minor Comments** The manuscript contains a few typographical errors (e.g., "categolized" and "drived" in the Summary of the Molecular Activity section). The phrase "hopping and jumping are not well-distinguished because the criterion is not clear" could be clarified with a more precise definition. The reference list is not provided in the submitted material, making it impossible to verify citations. The "Publisher's Note" and "Conflict of Interest" sections are standard but add little to the scientific content.
- **Technical failings that need to be addressed before the case is established** The manuscript does not provide quantitative comparisons of the cited experimental and simulation results, nor does it discuss the accuracy or limitations of the coarse-grained models used. The claim that "all guest proteins exhibited normal diffusion in p53 droplets in the sub-second time range" is presented without error bars or statistical analysis. The statement that "molecular uptake did not significantly depend on the structural properties of the guest proteins" is made without showing the underlying data or statistical tests. These issues prevent a full evaluation of the robustness of the presented conclusions.
- **Assessment against Nature-style criteria** Originality: Moderate. The review synthesizes existing work but does not present new concepts or a novel framework. Scientific importance: Moderate. The topic is relevant, but the review does not identify major unresolved questions or propose new directions beyond general statements. Interdisciplinary readership: Good. The manuscript bridges experimental and computational approaches and is accessible to both communities. Technical soundness: Adequate for a review, but the lack of critical methodological discussion and quantitative detail weakens the technical rigor. Readability for nonspecialists: Good. The writing is clear, and concepts are introduced with sufficient context for a general scientific audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript is a competent review, but it would be strengthened by a more balanced and critical treatment of the literature, explicit discussion of methodological limitations, and inclusion of quantitative details where claims are made. The absence of figures in the provided material is a practical limitation for this assessment, but the text alone is sufficient to support publication in a specialized journal after minor revisions.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** No
- **Axis** Balance and bias in literature selection
- **Claim pointer** The manuscript states that "this review discusses the molecular action of DNA-binding proteins on DNA and in liquid condensate based on the latest studies that mainly focused on the model protein p53."
- **Evidence pointer** Abstract and Introduction; location not provided
- **Concern** The review is heavily weighted toward the author's own publications (e.g., Kamagata et al., 2017, 2019, 2020a, 2020b, 2020c, 2021a, 2021b, 2021c; Itoh et al., 2016, 2018; Murata et al., 2015, 2017; Subekti et al., 2017, 2020). While this is not inherently problematic, the selection of studies is not justified, and alternative or conflicting findings from other groups are not discussed. This creates a risk of presenting a one-sided view of the field.
- **Why it matters** A review should provide a balanced and comprehensive overview of the field. Over-reliance on the author's own work may lead to confirmation bias and reduce the credibility of the conclusions for readers unfamiliar with the broader literature.
- **Resolution test** The author should either broaden the scope to include a more diverse set of studies or explicitly state the rationale for focusing on their own work. A brief discussion of any contradictory results or alternative interpretations would strengthen the review.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Critical evaluation of methodological limitations
- **Claim pointer** The manuscript states that "single-molecule fluorescence microscopy can track molecules on DNA, which distinguishes between the four mechanisms and characterizes their details" and that "molecular dynamics simulations can reproduce the behavior of proteins on DNA in a computer, providing theoretical insight into the molecular actions that happen."
- **Evidence pointer** Introduction; location not provided
- **Concern** The manuscript does not critically discuss the limitations of either technique. For example, the time resolution limitation of single-molecule microscopy is mentioned in the context of hopping and jumping, but its broader implications for interpreting the other mechanisms are not explored. Similarly, the accuracy of coarse-grained models is not discussed, despite their widespread use in the cited studies.
- **Why it matters** A review that aims to characterize molecular actions should acknowledge the uncertainties and approximations inherent in both experimental and computational approaches. Without this, readers may overestimate the certainty of the presented conclusions.
- **Resolution test** The author should add a paragraph or section discussing the limitations of single-molecule microscopy and molecular dynamics simulations, including temporal and spatial resolution limits, model simplifications, and potential artifacts.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative support for claims
- **Claim pointer** The manuscript states that "all guest proteins exhibited normal diffusion in p53 droplets in the sub-second time range" and that "molecular uptake did not significantly depend on the structural properties of the guest proteins."
- **Evidence pointer** Section "Liquid-Liquid Phase Separation"; location not provided
- **Concern** These claims are presented as definitive findings, but no quantitative data (e.g., diffusion coefficients, p-values, confidence intervals) are provided in the text. The reader cannot assess the robustness of these conclusions without access to the original figures or supplementary materials.
- **Why it matters** Quantitative claims require quantitative support. Without error bars or statistical analysis, the reader cannot determine whether the observed effects are significant or within experimental noise.
- **Resolution test** The author should either include the relevant quantitative data in the text or refer the reader to specific figures or tables that contain this information. If the data are not available, the claims should be softened to reflect the preliminary nature of the findings.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Language and typographical errors
- **Affected element** Summary of the Molecular Activity of DNA-Binding Proteins
- **Evidence pointer** Section "Summary of the Molecular Activity of DNA-Binding Proteins"; location not provided
- **Issue** The words "categolized" and "drived" are misspelled. They should be "categorized" and "driven," respectively.
- **Required correction** Correct the spelling errors.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity of definitions
- **Affected element** Introduction
- **Evidence pointer** Section "Introduction"; location not provided
- **Issue** The statement "hopping and jumping are not well-distinguished because the criterion is not clear" is vague. The reader is left uncertain about the operational distinction between these two mechanisms.
- **Required correction** Provide a clearer definition or explanation of the difference between hopping and jumping, or state that the distinction is not critical for the purposes of this review.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Referencing
- **Affected element** Entire manuscript
- **Evidence pointer** Location not provided
- **Issue** The reference list is not included in the submitted material, making it impossible to verify the accuracy and completeness of the citations.
- **Required correction** Ensure that the full reference list is provided in the final submission and that all citations are correctly formatted.

## Risk / unsupported claims
- The claim that "the combination of single-molecule microscopy and molecular dynamics simulations has provided a molecular understanding of DNA-protein interactions and LLPS" is a general statement that is supported by the cited studies but is not critically evaluated in terms of the strength of the evidence.
- The claim that "molecular uptake did not significantly depend on the structural properties of the guest proteins" is presented without quantitative data or statistical analysis, making it unsupported from the provided text.
- The claim that "all guest proteins exhibited normal diffusion in p53 droplets in the sub-second time range" is presented without quantitative data, making it unsupported from the provided text.
- The claim that "the preceding simulations perfectly predicted the presence of intersegmental transfer and the involvement of the disordered CT domains" uses the word "perfectly," which is an overstatement that is not justified by the data presented.
- The claim that "these theoretical studies, therefore, highlight the validity of molecular dynamics simulations for characterizing LLPS" is an overgeneralization, as the validity of simulations depends on the specific models and parameters used, which are not discussed in detail.