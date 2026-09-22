## Review setup
- **Input scope** Full manuscript text (main text, Materials and Methods, figure legends referenced but not provided in full)
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors propose that arginine-rich dipeptide repeats (R-DPRs) poly-PR and poly-GR, linked to C9orf72 ALS/FTD, bind to the negatively charged IDR1 of G3BP1 and switch it from a closed, inactive state to an open, activated state, driving liquid-liquid phase separation (LLPS) more potently than RNA. They further propose that this interaction represents a general pathological mechanism targeting switch-like proteins in stress granules and nucleoli, with implications for therapeutic intervention.
- **Visible evidence base** Turbidity assays, fluorescence microscopy, dynamic light scattering, FRAP, biolayer interferometry, Thioflavin S assays, coarse-grained Monte Carlo simulations, bioinformatic interactome analyses, Western blot-based recruitment assays
- **Missing materials affecting confidence** Full figures and supplementary figures (Fig. 1A, 1B, 1C inset, 2A, 2B, 3A-G, 4A-F, S1-S16), supplementary tables (S1-S7), Dataset S1, detailed experimental protocols for several assays, statistical analysis details, and raw data

## Reviewer

- **Overall assessment** This manuscript addresses an important and timely question in the ALS/FTD field: the molecular mechanism by which arginine-rich dipeptide repeats exert toxicity through dysregulation of stress granule dynamics. The authors present a compelling hypothesis centered on G3BP1 as a primary cytoplasmic target, supported by a multi-pronged experimental approach combining biochemistry, biophysics, cell biology, and computational modeling. The claim that R-DPRs bind G3BP1's IDR1 with sub-nanomolar affinity and drive LLPS more potently than RNA is striking and, if fully substantiated, would represent a significant advance. However, several technical concerns and missing experimental details limit the current assessment. The quantitative claims regarding binding affinities, the mechanistic distinction between RNA- and R-DPR-driven LLPS, and the generalizability of the proposed "switch-like" mechanism require additional scrutiny and experimental support.

- **Who would be interested in the results, and why** Researchers in the fields of neurodegeneration (specifically ALS/FTD), RNA biology, phase separation and biomolecular condensates, and intrinsically disordered proteins would find this work of high interest. The study directly addresses a key open question in C9orf72 ALS/FTD pathogenesis and proposes a unifying mechanism for R-DPR toxicity. The broader implications for other repeat expansion disorders and the potential therapeutic angle would also attract interest from translational researchers and drug discovery groups.

- **Major strengths** 1) The study addresses a significant and unresolved question in the field with clear clinical relevance. 2) The multi-technique approach (biophysical, biochemical, computational, and bioinformatic) provides complementary lines of evidence. 3) The comparative analysis between R-DPRs and RNA, and between poly-PR and poly-GR, adds mechanistic depth. 4) The bioinformatic interactome analysis extends the findings beyond a single protein pair and suggests broader relevance. 5) The writing is generally clear and the logical flow from hypothesis to evidence is well-structured.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative binding claims
- **Claim pointer** "The binding of both GR30 and PR30 is about three orders of magnitude stronger than that of polyU" and "sub-nanomolar binding strength of IDR1"
- **Evidence pointer** Figure 2C, Supplementary Figure S6, Supplementary Table S3
- **Concern** The authors report Kd values in the sub-nanomolar range for R-DPR binding to G3BP1 IDR1, which is approximately 1000-fold stronger than RNA binding. This is an extraordinary claim that requires rigorous validation. The BLI method, while appropriate for measuring binding affinities, can be prone to artifacts from non-specific binding, avidity effects (especially with multivalent interactions between R-DPRs and IDR1), and mass transport limitations. The manuscript text does not provide sufficient detail on the BLI experimental design, including the concentration ranges tested, the fitting model used, and whether the reported Kd values are from equilibrium or kinetic analysis. Furthermore, the claim that polyU Kd is "absolute" despite the undefined molecular weight of polyU is questionable, as the polyU preparation is polydisperse and the molar concentration cannot be accurately determined.
- **Why it matters** The quantitative difference in binding affinity between R-DPRs and RNA is central to the authors' argument that R-DPRs are more potent drivers of G3BP1 LLPS. If the Kd values are inaccurate due to technical artifacts, the mechanistic conclusion would be weakened. Sub-nanomolar affinities for a disordered protein-peptide interaction, while possible, are unusual and require independent validation.
- **Resolution test** Provide full BLI sensorgrams, detailed experimental protocols (including concentration ranges, regeneration conditions, and fitting procedures), and independent validation of binding affinities using an orthogonal method such as isothermal titration calorimetry (ITC) or fluorescence anisotropy. Address the polyU molecular weight issue explicitly and provide a rigorous error analysis.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic distinction between RNA- and R-DPR-driven LLPS
- **Claim pointer** "R-DPRs switch the closed inactive state of G3BP1 to an open activated state, driving its condensation more effectively than its cellular partner RNA" and "the IDR1–R-DPR interaction is sufficient for driving LLPS"
- **Evidence pointer** Figures 1C-H, 2A-B, 3A-G, Supplementary Figures S1-S4, S7, S9
- **Concern** The authors propose that R-DPRs and RNA activate G3BP1 through a similar switch-like mechanism, but with R-DPRs being more potent. However, the data presented suggest potentially different mechanisms. The finding that ΔIDR3 (lacking the positively charged IDR3) undergoes more intense phase separation with R-DPRs than full-length G3BP1 is counterintuitive if the mechanism is simply competition between IDR1-IDR3 intramolecular interactions and IDR1-R-DPR intermolecular interactions. If IDR3 is inhibitory, its removal should enhance LLPS, but the authors interpret this as evidence for the same mechanism. The simulations suggest different contact patterns for RNA vs. R-DPR, and the much higher protein concentration in R-DPR condensates (Fig. 3G) suggests a fundamentally different condensate architecture. The claim that both operate by the "same mechanism" appears oversimplified and not fully supported by the data.
- **Why it matters** The mechanistic distinction is crucial for understanding why R-DPR-driven condensates are pathological (less dynamic, more prone to aggregation) while RNA-driven condensates are physiological. If the mechanisms are fundamentally different, the therapeutic implications would differ.
- **Resolution test** Provide a more nuanced mechanistic model that accounts for the observed differences in condensate properties, protein concentration, and domain requirements. Directly test the proposed "switch" mechanism using single-molecule FRET or other conformational sensors. Compare the kinetics of LLPS and the internal dynamics of condensates formed by RNA vs. R-DPRs more systematically.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the proposed mechanism
- **Claim pointer** "The R-DPR–G3BP1 interaction represents a general pathological mechanism" and "Not only G3BP1 and NPM1 share similar switch-like features making them vulnerable to R-DPR misregulation, but these features are also shared by several other proteins"
- **Evidence pointer** Figure 4E, Supplementary Tables S5-S7, Dataset S1
- **Concern** The bioinformatic analysis identifies 23 R-DPR interactors and 7 toxicity effectors with the combined features of negative patch, positive patch, and RNA-binding domain. However, this is a purely computational prediction. No experimental validation is provided for any of these predicted targets. The claim of a "general pathological mechanism" is therefore speculative at this stage. Additionally, the analysis relies on interactome datasets from different sources with potentially different quality and coverage, and the criteria for defining "patches" and "RBDs" are not fully described.
- **Why it matters** The generalizability claim significantly extends the scope and impact of the work. Without experimental validation, this remains a hypothesis-generating observation rather than a demonstrated mechanism.
- **Resolution test** Experimentally validate at least 2-3 of the predicted switch-like targets by testing whether they (a) bind R-DPRs, (b) undergo R-DPR-induced LLPS, and (c) show R-DPR-dependent functional changes in cells. Provide a more detailed description of the bioinformatic criteria and include appropriate controls.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Pathological relevance and cellular context
- **Claim pointer** "R-DPRs cause a fast transition to a ThS positive state" and "these findings... appear to draw strong mechanistic parallels with the profound differences in SG formation under pathological and physiological conditions"
- **Evidence pointer** Figure 4A-B, Supplementary Figure S9
- **Concern** The Thioflavin S assay is performed in vitro with purified components. While this demonstrates that R-DPR-G3BP1 condensates can transition to amyloid-like states, the relevance to cellular pathology is inferred rather than demonstrated. The authors do not provide direct evidence that R-DPR-induced G3BP1 condensates in cells are less dynamic or more prone to aggregation. The connection to the well-established cellular phenotypes of R-DPR toxicity (e.g., impaired SG dynamics, nucleolar stress) is correlative.
- **Why it matters** The pathological relevance is a key part of the significance claim. Without cellular validation, the in vitro observations may not translate to the disease context.
- **Resolution test** Perform cellular experiments showing that R-DPR expression leads to G3BP1 condensates with altered dynamics (e.g., FRAP in cells), reduced reversibility, and recruitment of pathological proteins. Ideally, use patient-derived cells or animal models to strengthen the disease relevance.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Experimental detail
- **Affected element** Materials and Methods
- **Evidence pointer** "Materials and Methods" section
- **Issue** The Materials and Methods section is incomplete in the provided text. Several assays (BLI, FRAP, DLS, ThS, microfluidics) reference supplementary information for details, but the essential parameters (buffer conditions, protein concentrations, time courses, replicates, statistical tests) are not fully described in the main text.
- **Required correction** Provide complete experimental details in the main text or ensure the supplementary information contains all necessary information for reproducibility.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** All quantitative data
- **Evidence pointer** Figures 1C-H, 2A-B, 3A-G, 4A-F
- **Issue** The manuscript text does not describe the statistical methods used, the number of replicates, or the error bars shown in the figures. It is unclear whether the reported differences are statistically significant.
- **Required correction** Add a statistical analysis section describing the tests used, the number of independent replicates, and the criteria for significance. Ensure all figure legends include appropriate statistical annotations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data and Materials Availability
- **Evidence pointer** "Data, Materials, and Software Availability" section
- **Issue** The statement "All study data are included in the article and/or supporting information" is vague. Raw data for binding assays, turbidity measurements, and simulations are not explicitly deposited in a public repository.
- **Required correction** Deposit raw data in a public repository (e.g., Zenodo, Figshare) and provide accession numbers. Include source data files for all main and supplementary figures.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figures 1-4
- **Evidence pointer** Figure legends referenced in text
- **Issue** The manuscript text references multiple figures and supplementary figures, but the actual figures are not provided in the submitted text. It is impossible to assess the quality of the data presentation, the clarity of the images, or the appropriateness of the quantification.
- **Required correction** Ensure all figures are included in the submission with high-resolution images, clear labels, and comprehensive legends.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** "R-DPRs" and "poly-PR/poly-GR"
- **Issue** The authors use "R-DPRs" to refer collectively to poly-PR and poly-GR, but also use "arginine-rich dipeptide repeats" which could be confused with other arginine-containing DPRs (e.g., poly-GR is arginine-glycine, poly-PR is arginine-proline). The terminology is mostly clear but could be defined more explicitly at first use.
- **Required correction** Define all abbreviations clearly at first use and consider using "Arg-rich DPRs" for clarity.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion of previous work on G3BP1 and R-DPR interactions is somewhat brief. The authors mention that "it was recently suggested that a similar mechanism can be initiated by R-DPRs binding to IDR1 (38)" but do not critically compare their findings with this prior work or discuss any discrepancies.
- **Required correction** Expand the discussion to more thoroughly contextualize the findings within the existing literature, including any conflicting results or alternative interpretations.

## Risk / unsupported claims
- The claim that R-DPRs bind G3BP1 with sub-nanomolar affinity (Kd ~0.01-6 nM) is not fully supported by the provided evidence; the BLI methodology and data analysis are not described in sufficient detail.
- The claim that R-DPRs are "three orders of magnitude" stronger than RNA in binding G3BP1 is problematic given the undefined molecular weight of polyU, which affects the accuracy of the reported Kd for RNA.
- The claim that the R-DPR-G3BP1 interaction represents a "general pathological mechanism" is speculative, as only two proteins (G3BP1 and NPM1) are experimentally characterized, and the bioinformatic predictions for additional targets are not validated.
- The claim that R-DPR-driven condensates are "pathological" based on ThS positivity in vitro is not directly supported by cellular or in vivo evidence.
- The statement that "the IDR1–R-DPR interaction is sufficient for driving LLPS" is based on experiments with isolated IDR1 and may not fully recapitulate the behavior of the full-length protein in a cellular context.
- The cooperativity between R-DPR and RNA binding is inferred from a single experiment (Kd of GR30 in the presence of RNA) and is not systematically explored.
- The differences between poly-GR and poly-PR in terms of binding, LLPS, and interactome preferences are presented as significant, but the mechanistic basis for these differences is not fully explained.