## Review setup
- **Input scope** Full manuscript text (Summary, Introduction, Results, Discussion, Limitations, STAR Methods) for the article by Cooper et al., submitted to iScience.
- **Assessment boundary** Scientific soundness, methodological rigor, validity of conclusions relative to the presented evidence, and clarity of presentation. Assessment is based solely on the provided manuscript text; no external data, figures, or supplementary materials were available for direct inspection.
- **Shared manuscript claim summary** The authors propose a hierarchy of grammar rules governing the sequence-function relationship of transcriptional activation domains (ADs). Using a rationally designed library of ~7,300 sequences tested in a high-throughput in vivo yeast assay, they identify redundant aromatic residues and net negative charge as dominant requirements, with balance, C-terminal positioning, and cluster avoidance as minor modulatory rules. They further propose that ADs function as acidic-hydrophobic surfactants.
- **Visible evidence base** Description of a high-throughput yeast-based growth assay with continuous readout; analysis of 32 rule-combination sets (n=3,200) plus additional derivative sets; regression coefficients for rule importance; AUC values for predictive models; multicollinearity (VIF) and interaction analyses; comparisons to external datasets (random sequences, natural sequences).
- **Missing materials affecting confidence** All figures (including Figure 1, 2, 3, 4, 5, 6, 7), supplementary figures (Figure S1), and supplementary tables (Tables S1–S3) are referenced but not provided. Raw sequencing data, detailed strain validation, and the full composition of the designed library are not described in sufficient detail to independently verify the analysis. The exact definitions of "functional" thresholds and the statistical distribution of the data are only partially described.

## Reviewer

- **Overall assessment** This manuscript addresses a long-standing and important problem in eukaryotic gene regulation: the sequence grammar of transcriptional activation domains. The experimental design is thoughtful, leveraging a continuous in vivo readout to move beyond binary classifications. The central finding, that redundant aromatic residues and net negative charge are the dominant determinants, is plausible and consistent with prior literature. However, the strength of the conclusions is limited by the narrow sequence space explored (primarily W, D, R, G) and the lack of visible data to assess the robustness of the statistical models. The claim of a "surfactant" mechanism is intriguing but remains speculative given the in vivo-only data. The manuscript is well-written and the logical flow is clear, but the evidence as presented does not fully establish the proposed hierarchy as a generalizable grammar for natural ADs.
- **Who would be interested in the results, and why** Researchers studying transcriptional regulation, intrinsically disordered proteins, and sequence-function relationships. The work provides a quantitative framework for understanding AD activity that could inform predictive models of activator function and synthetic biology efforts to design custom transcription factors. The proposed surfactant model may also interest biophysicists studying protein-membrane or protein-surface interactions.
- **Major strengths**
    1.  The use of a continuous, quantitative in vivo readout (growth slope) is a significant improvement over binary screens, allowing for nuanced analysis of rule strength.
    2.  The systematic decomposition of sequence space into defined rule combinations (the 32 sets) is a rigorous approach to disentangle overlapping features.
    3.  The refinement of binary rules into continuous metrics and the subsequent validation on external datasets (random and natural sequences) strengthens the generalizability of the findings.
    4.  The study directly addresses the "acidic exposure" model and provides a clear, testable alternative hypothesis (surfactant model).
- **Major Concerns**

    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical Soundness
    - **Claim pointer** The manuscript claims that the refined rules "better reflect the AD functionality in vivo" based on increased prediction accuracy across three datasets (Figure 7B).
    - **Evidence pointer** Figure 7B, "Lasso regression AUC" section.
    - **Concern** The claim of improved prediction accuracy is central to the paper's conclusion, but the AUC values and the methodology for calculating them on the external datasets are not described in the text. It is unclear if the model was trained on the designed library and tested on the others, or if separate models were trained per dataset. The text mentions modifications "to account for the greater variety of residues and for a different sequence length" for external datasets, but the specifics are absent. Without seeing the actual AUC values, the confidence intervals, and the precise training/testing protocol, the improvement in prediction accuracy cannot be evaluated.
    - **Why it matters** The entire premise of a "refined" grammar rests on this quantitative demonstration. If the improvement is marginal or the methodology is flawed (e.g., data leakage), the central conclusion is undermined.
    - **Resolution test** Provide the AUC values (with confidence intervals) for all three datasets for both old and new rule formulations. Clearly describe the training/testing protocol, including whether features were standardized across datasets and how sequence length differences were handled.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical Soundness
    - **Claim pointer** The manuscript states that "the two dominant rules are the redundant representation of aromatic and acidic residues and the absence of positively charged residues, with coefficients of 3.51 and 2.85, respectively" (Figure 1A).
    - **Evidence pointer** Figure 1A, "Relative importance of grammar rules" section.
    - **Concern** The regression coefficients are presented as the primary evidence for the rule hierarchy. However, the text does not report the standard errors, confidence intervals, or p-values for these coefficients beyond a general significance star. More critically, the model used to generate these coefficients is not fully specified. Was it a single multiple linear regression with all five binary rule indicators? Or a univariate analysis? The interaction analysis is mentioned later, but the main model's structure is unclear. The potential for multicollinearity between the binary rules (e.g., a sequence with high redundancy might also have high balance) is acknowledged for the "new" rules but not for the "old" ones.
    - **Why it matters** The hierarchy is the core finding. If the coefficients are not robust or the model is misspecified, the ranking of rules could be an artifact. The reader cannot assess the statistical validity of the hierarchy without this information.
    - **Resolution test** Provide the full model specification, including the type of regression, the predictors included, and the standard errors or confidence intervals for all coefficients. Show that the assumptions of the regression model are met.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Reproducibility & Data Availability
    - **Claim pointer** The study analyzes 7,327 sequences and uses a high-throughput growth assay to generate a continuous "growth slope" as a measure of AD function.
    - **Evidence pointer** "Estimation of sequence growth rates" section in STAR Methods.
    - **Concern** The description of the growth slope calculation is incomplete. The text states that "Robust linear regression... was used to estimate the growth slope of each sequence over time" using "all BioReps at the initial timepoint and first growth timepoint." This implies only two time points are used, which is a very limited basis for a "slope." Furthermore, the text mentions that sequences where counts dropped to 0 at the first growth timepoint were excluded, which could introduce a significant bias by removing the most strongly non-functional sequences. The criteria for excluding sequences and the number of time points used are critical for understanding the data quality.
    - **Why it matters** The entire quantitative analysis depends on the reliability of the growth slope as a proxy for AD function. A slope calculated from two points, with a potentially biased exclusion step, may not be a robust or accurate measure.
    - **Resolution test** Clarify the exact number of time points used for slope calculation. Provide a detailed description of the exclusion criteria and the number of sequences excluded at each step. Show a validation that the two-point slope correlates well with slopes calculated from more time points, if available.

    - **Concern ID** R1-M4
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific Importance / Generalizability
    - **Claim pointer** The manuscript concludes that the findings support a "surfactant" model of AD function and that the rules are generalizable to natural ADs.
    - **Evidence pointer** Discussion section, "Refined grammar rules for ADs" section.
    - **Concern** The designed library is heavily biased towards W, D, R, and G residues. While the authors test substitutions with other amino acids (Figure 6), the foundational rules are derived from this narrow sequence space. The claim of generalizability to natural ADs, which contain a much wider variety of amino acids and are often longer, is a significant leap. The prediction accuracy on the natural sequences dataset is mentioned, but the dataset is small and the result is not shown. The surfactant model is an interesting hypothesis, but the in vivo data cannot directly test the biophysical claims of surfactant behavior (e.g., interfacial activity, micelle formation).
    - **Why it matters** The broader significance of the work depends on whether the rules apply beyond the specific library tested. If the rules are only relevant for W/D-rich sequences, their impact is limited.
    - **Resolution test** Discuss the limitations of the sequence space more explicitly. Provide the prediction results on the natural sequences dataset to support the generalizability claim. Frame the surfactant model as a hypothesis that requires direct biophysical testing, rather than a conclusion of this study.

- **Minor Comments**

    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity & Presentation
    - **Affected element** Figure 1B description
    - **Evidence pointer** Figure 1B, "Effect of not following each rule" section.
    - **Issue** The description of Figure 1B is confusing. It mentions "Non-functional outliers in sets #4 through #8 have sequence features that greatly deviate from the corresponding rules." It is unclear what "greatly deviate" means in a binary rule system. The inset and Figure S1 are referenced, but not visible.
    - **Required correction** Clarify the criteria for identifying "outliers" and describe the specific features that distinguish them from the rest of the set. Ensure the text is understandable without relying on the invisible figure.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Multicollinearity analysis
    - **Evidence pointer** "Feature collinearity and interaction analysis" section in STAR Methods.
    - **Issue** The text states that VIFs were calculated for the "Old" and "New" rule features. It is stated that the "New" rules show "slight multicollinearity" with a VIF of 2.17 for rule 2. However, the VIFs for the "Old" rules are not mentioned. If the "Old" rules had high multicollinearity, this would affect the interpretation of the initial regression coefficients in Figure 1A.
    - **Required correction** Report the VIF values for both the "Old" and "New" rule sets to allow for a direct comparison of model stability.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Reproducibility & Data Availability
    - **Affected element** Data and code availability
    - **Evidence pointer** "Data and code availability" section.
    - **Issue** The data and code are deposited in external repositories (GEO, Zenodo). While this is good practice, the manuscript does not state whether the code is open-source and what license it uses. It also does not specify the version of the code used for the analysis.
    - **Required correction** Specify the software license and the version of the code used to generate the results.

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Clarity & Presentation
    - **Affected element** Introduction
    - **Evidence pointer** Introduction, first paragraph.
    - **Issue** The introduction states that the "coactivator recruitment model" is "incomplete" and that the data "demands flexibility of thinking and potentially a new mechanistic model." This is a strong claim that is not fully supported by the data presented, which is primarily descriptive of sequence rules.
    - **Required correction** Soften the language in the introduction to avoid overstating the implications of the study before the results are presented.

## Risk / unsupported claims
- The claim that the refined rules "better reflect the AD functionality in vivo" is unsupported without the actual AUC values and a detailed description of the validation methodology (R1-M1).
- The claim that the findings support a "surfactant" model of AD function is unsupported by the in vivo data, which cannot directly assess biophysical properties.
- The claim that the rules are generalizable to natural ADs is weakly supported, given the narrow sequence space of the designed library and the lack of visible results on the natural sequences dataset.
- The statement that the "acidic exposure" model is "incomplete" is a reasonable interpretation, but the evidence presented (Figure 4) only shows that proline cannot substitute for acidic residues, which does not fully address the model's core premise.
- The specific numerical values of the regression coefficients (3.51 and 2.85) are presented without measures of uncertainty, making it impossible to assess the statistical significance of the hierarchy.