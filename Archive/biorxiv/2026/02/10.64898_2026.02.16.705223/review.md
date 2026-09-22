## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv, 2026-02-17)
- **Assessment boundary** Scientific content, methodology, and claims as presented in the provided text; no external data or supplementary figures were available for independent verification
- **Shared manuscript claim summary** The authors propose that aging-associated reduction in total cellular RNA increases the RBP-to-RNA ratio within stress granules, producing viscous, persistent condensates ("alt-SGs") that protect senescent cells under fluctuating stress; restoring RNA levels via nucleoside supplementation reverses these phenotypes and alleviates senescence markers.
- **Visible evidence base** Results sections describing live-cell imaging, fixed-cell immunofluorescence, FISH, NHS ester labeling, EU metabolic labeling, in vitro reconstitution, and nucleoside supplementation experiments; figures referenced but not provided
- **Missing materials affecting confidence** All figures and supplementary figures; statistical details (exact p-values, n numbers, replicates); raw imaging data; antibody validation data; details of the custom MATLAB analysis pipeline; full methods for in vitro reconstitution and FRAP fitting

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question: how aging alters the material properties of RNA-protein condensates. The central hypothesis, that age-related decline in total RNA shifts condensate stoichiometry toward RBP-enriched, viscous states, is conceptually appealing and potentially unifying. However, the evidence presented in the text is insufficient to fully establish the causal chain from reduced RNA metabolism to altered condensate dynamics to senescence protection. Several key claims rest on correlative observations or on experiments whose quantitative details are not fully described. The manuscript would benefit from additional mechanistic dissection and from clearer presentation of the quantitative data underlying the main conclusions.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, RNA biology, and cellular aging. The work bridges biophysics and cell biology and could inform understanding of age-related neurodegeneration, where persistent RNA-protein aggregates are a hallmark. The proposed role of RNA abundance as a "rheostat" for condensate state is likely to be of broad interest.
- **Major strengths** The study addresses a fundamental question with potential translational relevance. The use of multiple model systems (human cells, mouse fibroblasts, Drosophila tissues) strengthens the generality of the observations. The combination of live-cell imaging, in vitro reconstitution, and metabolic labeling provides complementary approaches. The finding that nucleoside supplementation can reverse condensate phenotypes is potentially actionable and clinically relevant.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5, R1-M6
- **Assessment against Nature-style criteria** Originality: High. The concept that absolute RNA concentration, rather than specific RNA sequences, governs condensate material state in aging is novel and potentially paradigm-shifting. Scientific importance: High. If substantiated, the findings would link metabolic decline to phase behavior and could explain age-related aggregation. Interdisciplinary readership: Broad. The work speaks to biophysicists, cell biologists, and aging researchers. Technical soundness: Currently insufficient. Several key experiments lack quantitative detail, and the causal link between RNA loss and condensate viscosity is not fully established. Readability for nonspecialists: The main text is generally clear, but the Results section is dense and would benefit from more explicit framing of the key questions and conclusions at each step.
- **Recommendation posture** Supportive if technical concerns are resolved. The central hypothesis is compelling and the preliminary data are suggestive, but the current evidence does not fully establish the causal chain proposed.

## Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal inference
- **Claim pointer** "Aging cells display diminished absolute RNA concentrations due to reduced RNA metabolic activity. Reactivation of RNA metabolism restores RNA/RBP ratios within SGs and alleviates aging-associated phenotypes."
- **Evidence pointer** Results sections "Cellular RNA concentration decreases in aging" and "Restored RNA metabolism rejuvenates senescent phenotypes"; Figures 4, 6, 7
- **Concern** The manuscript claims that reduced RNA is causal for the alt-SG phenotype, but the evidence presented is largely correlative. The nucleoside supplementation experiment is the key intervention, but the text does not specify whether the effect is specific to RNA synthesis or could be due to off-target effects of nucleosides on other metabolic pathways. Furthermore, the text does not demonstrate that the increase in RNA after supplementation occurs specifically within SGs, nor that the rescued condensate dynamics are due to the restored RNA/RBP ratio rather than to other downstream effects of improved cellular metabolism.
- **Why it matters** The central claim of the manuscript is that RNA abundance is a "rheostat" for condensate state. Without a clean causal demonstration, the conclusion is not established.
- **Resolution test** Provide a more detailed analysis of the nucleoside supplementation experiment, including measurements of total RNA and SG RNA content before and after treatment. Ideally, use an orthogonal approach to increase RNA levels (e.g., overexpression of a catalytically inactive RNA polymerase or inhibition of RNA degradation) and show that this also rescues the alt-SG phenotype. Alternatively, deplete RNA in young cells and show that this phenocopies the aging phenotype.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative rigor
- **Claim pointer** "Alt-SGs exhibit elevated RNA-binding protein (RBP)-to-RNA ratios" and "increased condensate viscosity and persistence"
- **Evidence pointer** Results sections "Senescent cells are prone to form persistent and viscous SGs" and "Alt-SGs have more RBP and less RNA"; Figures 1, 3
- **Concern** The text describes qualitative differences in RBP-to-RNA ratios and viscosity but does not provide quantitative details. For example, the FRAP analysis is described as showing "increased contribution of the slow fraction" and "higher viscosity," but the actual fitted parameters (A1, A2, b, c) and their statistical comparison between young and aged cells are not reported. Similarly, the claim of "elevated RBP-to-RNA ratio" is based on enrichment measurements, but the text does not specify how these were calculated or whether they were normalized for SG size or cellular background.
- **Why it matters** The central biophysical claim of the manuscript rests on quantitative measurements. Without reporting the actual numbers and statistical tests, the reader cannot assess the robustness of the findings.
- **Resolution test** Report the fitted FRAP parameters (with confidence intervals) for all conditions, along with the number of cells/condensates analyzed and the statistical test used. Provide a clear description of how RBP-to-RNA ratios were calculated, including normalization steps and controls.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Model system relevance
- **Claim pointer** "Aged cells across different model organisms have enriched SGs" and "alt-SGs confer protection to senescent cells under fluctuating stress conditions"
- **Evidence pointer** Results section "Aged cells across different model organisms have enriched SGs"; Figures 2, 7
- **Concern** The manuscript uses multiple model systems (HeLa senescence, primary human and mouse fibroblasts, Drosophila tissues), but the text does not clearly explain how the different models relate to each other. For example, the protective role of alt-SGs is demonstrated in senescent HeLa cells, but it is unclear whether the same protective effect operates in primary cells or in vivo. Additionally, the physiological relevance of the stress conditions used (sodium arsenite) to natural aging is not discussed.
- **Why it matters** The claim that alt-SGs are protective is important and potentially counterintuitive. If this is only shown in one cell line under one stress condition, the generality of the claim is limited.
- **Resolution test** Clarify the relationship between the different models and explicitly state which claims are supported by which model. If possible, test the protective role of alt-SGs in a more physiologically relevant stress model (e.g., heat shock or ER stress) or in primary cells.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic depth
- **Claim pointer** "RNA concentration is a key determinant of condensate material properties, molecular composition, and dissolution capacity"
- **Evidence pointer** Results section "RNA drives the liquid-like properties of RNA-RBP condensates"; Figure 5
- **Concern** The in vitro reconstitution experiments are described as showing that RNA addition "fluidizes" condensates, but the text does not provide a mechanistic explanation for this effect. Is the effect due to changes in RNA length, secondary structure, or sequence composition? Does RNA act by competing with protein-protein interactions or by altering the network connectivity? The manuscript would be strengthened by a more detailed biophysical characterization of the condensates (e.g., measurements of surface tension, viscosity, or diffusion coefficients).
- **Why it matters** The claim that RNA is a "rheostat" implies a general mechanism. Without understanding the molecular basis of the RNA effect, it is difficult to predict how this would apply to other condensate systems or to design interventions.
- **Resolution test** Provide additional biophysical characterization of the in vitro condensates, such as microrheology measurements or FRAP with varying RNA concentrations. Test whether the effect is specific to RNA or can be recapitulated by other polyanions.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Data availability
- **Claim pointer** "We demonstrate that restoring RNA levels reverses aberrant SG dynamics and alleviates cellular aging phenotypes"
- **Evidence pointer** Results section "Restored RNA metabolism rejuvenates senescent phenotypes"; Figures 6, 7
- **Concern** The text states that nucleoside supplementation "alleviates aging-associated phenotypes" and "reduces senescence markers," but the specific markers and the magnitude of the effect are not described. The text also mentions that "NS treatment reduced the proportion of dying senescent cells from 37% to 20%," but it is unclear whether this is a statistically significant difference and how many cells were analyzed.
- **Why it matters** The therapeutic potential of nucleoside supplementation is a key selling point of the manuscript. Without quantitative details, the reader cannot assess the strength of this claim.
- **Resolution test** Provide a detailed description of the senescence markers measured, the statistical analysis, and the effect sizes. Include the number of biological replicates and cells analyzed.

- **Concern ID** R1-M6
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** "We used a custom-written MATLAB (R2023a) script" for image analysis
- **Evidence pointer** Methods sections "Analysis of live cell images for SG nucleation" and "Fixed cell SG analysis"
- **Concern** The image analysis pipeline is described only briefly, and the custom MATLAB scripts are not provided or described in sufficient detail to be reproduced. Key parameters such as segmentation thresholds, background subtraction methods, and the criteria for identifying SGs are not specified.
- **Why it matters** Reproducibility is a core requirement for a study of this type. Without a detailed description of the analysis pipeline, other groups cannot replicate the findings or apply the methods to their own data.
- **Resolution test** Provide the custom scripts as supplementary material, along with a detailed description of the analysis steps and parameter choices. Alternatively, use publicly available image analysis software and describe the settings in detail.

## Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Results section "Senescent cells are prone to form persistent and viscous SGs"
- **Issue** The term "alt-SGs" is introduced without a clear definition of what "alt" stands for. The authors state "we will hereafter refer to them as alt-SGs," but the rationale for the name is not explained.
- **Required correction** Define the term explicitly (e.g., "altered stress granules") and explain why this name was chosen.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure legends
- **Evidence pointer** All figures
- **Issue** The text frequently states that differences are "significant" or "higher" without reporting p-values or confidence intervals.
- **Required correction** Add statistical details to figure legends or in the text, including the test used, the number of replicates, and the exact p-values.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Experimental design
- **Affected element** Senescence induction
- **Evidence pointer** Methods section "Cell culture"
- **Issue** The method for inducing senescence in HeLa cells (BrdU treatment) is described, but the duration of treatment and the validation of senescence (beyond SA-beta-gal) are not specified.
- **Required correction** Provide details on the BrdU treatment protocol and include additional senescence markers (e.g., p16, p21 expression, cell cycle arrest) to confirm the senescent state.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Protective role of alt-SGs
- **Evidence pointer** Results section "Restored RNA metabolism rejuvenates senescent phenotypes"
- **Issue** The claim that alt-SGs are "protective" is based on the observation that cells with persistent SGs survive better under stress. However, the text does not discuss alternative interpretations, such as the possibility that the persistent SGs are a marker of cellular distress rather than a protective mechanism.
- **Required correction** Discuss alternative interpretations and, if possible, provide additional evidence that the SGs themselves are protective (e.g., by disrupting SG formation and showing loss of protection).

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion cites several relevant papers but does not fully contextualize the findings within the broader literature on condensate aging and RNA metabolism. For example, the relationship between the proposed mechanism and known age-related changes in RNA polymerase activity or RNA degradation pathways is not discussed.
- **Required correction** Expand the discussion to more thoroughly address how the findings relate to existing models of condensate aging and to identify open questions.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figures 1 and 3
- **Evidence pointer** Figures 1 and 3
- **Issue** The text refers to "pre-formed SGs" in senescent cells, but the figures are not provided. It is unclear how these were distinguished from SGs formed during the stress period.
- **Required correction** Clarify the criteria for identifying pre-formed SGs and provide representative images with clear labeling.

## Risk / unsupported claims
- The claim that "alt-SGs confer protection to senescent cells" is not fully supported by the evidence presented, as the protective effect is only shown in one cell line and the mechanism is not established.
- The claim that "RNA concentration is a key determinant of condensate material properties" is supported by in vitro data, but the quantitative relationship between RNA concentration and viscosity is not reported.
- The claim that "reactivation of RNA metabolism restores RNA/RBP ratios within SGs" is based on a single intervention (nucleoside supplementation) and lacks mechanistic detail.
- The claim that "aging is associated with reduced total cellular RNA" is supported by multiple assays, but the text does not report the magnitude of the reduction or the variability across models.
- The claim that "alt-SGs are more viscous" is based on FRAP analysis, but the fitted parameters are not reported, making the claim difficult to evaluate.
- The claim that "restored RNA metabolism alleviates aging-associated phenotypes" is based on a reduction in senescence markers, but the specific markers and effect sizes are not described.