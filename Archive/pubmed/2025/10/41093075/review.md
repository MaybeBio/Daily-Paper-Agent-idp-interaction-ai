## Review setup
- **Input scope** Full manuscript text, including abstract, results, experimental procedures, and data availability statements. Figures and supplementary materials referenced but not fully provided.
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and technical soundness based solely on the provided text. No assessment of formatting, grammar, or journal policy compliance.
- **Shared manuscript claim summary** The authors report that Sp100A, one of four main Sp100 isoforms, is required for IFN-induced localization of the HIRA histone chaperone complex to PML nuclear bodies in NIKS keratinocytes. They generated Sp100 knockout cell lines, demonstrated normal differentiation and PML-NB formation, and used isoform-specific rescue and mutagenesis to identify the SUMO-interacting motif (SIM) as important for HIRA recruitment. Structural predictions and molecular dynamics simulations were used to support mechanistic interpretations.
- **Visible evidence base** Results sections describing CRISPR KO generation, genotyping, immunofluorescence, Western blot, RNA-seq, and structural modeling. Figures 1–8 and Supplementary Figures S1–S9 are referenced but not fully visible. Experimental procedures are described in detail.
- **Missing materials affecting confidence** Full figures and figure legends, supplementary tables (including Table S1 genotyping details), complete RNA-seq analysis (differential expression lists, statistical thresholds), and the structural model files deposited in ModelArchive. The manuscript text alone does not allow independent verification of image quantitation, statistical methods, or the quality of structural predictions.

## Reviewer
- **Overall assessment** This manuscript addresses a focused question in nuclear body biology: which Sp100 isoform recruits HIRA to PML-NBs, and what molecular features are required. The generation of clean Sp100 KO keratinocyte lines is a valuable resource, and the isoform-specific rescue experiments are well conceived. The finding that Sp100A uniquely promotes HIRA localization, despite all isoforms sharing the N-terminal region, is interesting and potentially important. However, the mechanistic depth is limited. The SIM mutagenesis data are suggestive but incomplete, and the structural modeling, while thorough, is largely speculative and not directly tested. The RNA-seq data are used only to exclude major transcriptional changes, which is appropriate but not a central strength. The manuscript is technically sound in its core cell biology, but the conclusions about molecular mechanism would be strengthened by direct interaction or biochemical data. The work is likely of interest to specialists in PML-NB biology, chromatin regulation, and innate immunity, but its broader impact is moderate.
- **Who would be interested in the results, and why** Researchers studying PML nuclear bodies, histone chaperones, chromatin dynamics at interferon-stimulated genes, and the functional diversification of Sp100 isoforms. The KO cell lines will be useful to the HPV and keratinocyte biology communities. The structural predictions may interest computational biologists working on intrinsically disordered regions in nuclear body proteins.
- **Major strengths**
  1. Generation and validation of multiple Sp100 KO NIKS clones, with confirmation of normal differentiation and PML-NB formation.
  2. Systematic comparison of all four Sp100 isoforms in a clean genetic background, avoiding confounding effects of endogenous Sp100.
  3. Rigorous mutagenesis approach targeting seven distinct functions, with careful quantitation of localization phenotypes.
  4. Integration of multiple AI-based structural prediction methods with molecular dynamics, providing a framework for interpreting isoform-specific behavior.
  5. Clear demonstration that HIRA recruitment to PML-NBs is not required for immediate IFN signaling, reinforcing prior work.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic evidence
- **Claim pointer** The authors claim that the SIM motif in Sp100A "plays an important role in HIRA localization to PML-NBs" and that IFN treatment can rescue HIRA recruitment in the mSIM mutant.
- **Evidence pointer** Figure 7C, Results section "Sp100A SUMO interacting motif is important for HIRA localization at PML"
- **Concern** The SIM mutagenesis data are interpreted as evidence for a direct SUMO-SIM interaction mediating HIRA recruitment. However, no biochemical evidence is provided to show that the SIM mutation disrupts a specific protein-protein interaction, nor is it shown that HIRA itself is SUMOylated or binds SUMO. The IFN-dependent rescue of HIRA localization in the mSIM mutant is unexplained and could reflect indirect effects, such as increased SUMOylation of other PML-NB components. The authors speculate about this but do not test it. Without direct interaction data, the mechanistic claim is not established.
- **Why it matters** The central mechanistic conclusion of the paper rests on the interpretation of the SIM mutant phenotype. If the SIM is not directly engaging HIRA or a SUMO-modified HIRA complex, the model proposed is unsupported. The field would benefit from knowing whether Sp100A and HIRA physically interact, and whether this requires SUMO.
- **Resolution test** Provide co-immunoprecipitation or proximity ligation assays showing Sp100A-HIRA interaction, and test whether the SIM mutation disrupts this interaction. Alternatively, show that HIRA is SUMOylated and that this is required for its PML-NB localization. If the IFN rescue is to be explained, identify the IFN-induced modification that compensates for the SIM mutation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative rigor
- **Claim pointer** The authors state that HIRA localization to PML-NBs is "greatly increased" after IFN treatment and that Sp100A is "primarily responsible" for this effect.
- **Evidence pointer** Figures 3B, 5C, 7C; Results sections "Sp100 is required for localization of HIRA to PML-NBs" and "Sp100A SUMO interacting motif is important for HIRA localization at PML"
- **Concern** Quantitation is based on manual scoring of 30 nuclei per condition, with categories (0, 1–3, 4–9, 10+ foci) rather than continuous measurements. The authors acknowledge lack of blinding. This approach is prone to observer bias and lacks the precision needed to support claims of "primary" responsibility or to distinguish subtle differences between isoforms and mutants. Statistical tests are not described for these comparisons.
- **Why it matters** The conclusions about isoform specificity and mutant phenotypes depend on reliable quantitation. Manual categorical scoring with small sample sizes may not detect meaningful differences or may overstate them. The field increasingly expects automated, unbiased image analysis.
- **Resolution test** Provide automated image analysis with defined thresholds, report continuous distributions of foci counts, and include appropriate statistical tests (e.g., mixed-effects models) with effect sizes. Increase sample size and include blinded scoring.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Structural interpretation
- **Claim pointer** The authors state that structural predictions and molecular dynamics simulations "highlight how interspersed structural domains and intrinsically disordered regions (IDRs) could influence this localization" and suggest that C-terminal domains in longer isoforms could sterically hinder interactions.
- **Evidence pointer** Results section "Structural prediction of the Sp100 isoforms and location of Sp100A mutations"; Figures 7D, S7–S9
- **Concern** The structural models have low global confidence (pLDDT < 50), and the authors acknowledge that only well-defined domains are reliable. The claim that IDRs and domain flexibility explain isoform-specific HIRA recruitment is speculative. The molecular dynamics simulation was performed on Sp100B, not Sp100A, and the relevance to HIRA recruitment is not directly tested. The "semi-stable region between residues 380 and 480" is not functionally validated.
- **Why it matters** The structural analysis is presented as supporting the mechanistic model, but it does not provide testable predictions that are experimentally verified. Overinterpretation of low-confidence models could mislead the field.
- **Resolution test** Test the functional relevance of the predicted semi-stable region or IDRs by targeted deletion or mutation experiments. If steric hindrance by C-terminal domains is proposed, construct chimeric isoforms or deletion mutants that test this directly. Consider cross-linking mass spectrometry or hydrogen-deuterium exchange to validate the predicted domain arrangements.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Completeness of evidence
- **Claim pointer** The authors conclude that "HIRA recruitment to PML-NBs absolutely requires the Sp100A protein" based on KO and rescue experiments.
- **Evidence pointer** Figures 3, 5; Results sections "Sp100 is required for localization of HIRA to PML-NBs" and "The Sp100A isoform promotes HIRA localization to PML-NBs in NIKS Sp100 KO cells"
- **Concern** The rescue experiments rely on transient transfection of YFP-tagged isoforms. The authors note that Sp100A is expressed at higher levels than other isoforms, and they argue this does not explain the specificity. However, the data supporting this argument are not fully shown. It is unclear whether the longer isoforms were expressed at comparable levels to Sp100A in the same cells, and whether the YFP tag affects function. The possibility that overexpression of Sp100A creates an artifact is not fully addressed.
- **Why it matters** The claim of absolute requirement and isoform specificity is strong. If the longer isoforms are simply expressed at lower levels or mislocalized due to the tag, the conclusion would be weakened. The field needs to know that the comparison is fair.
- **Resolution test** Provide quantitative analysis of YFP-Sp100 isoform expression levels in the same cells used for scoring, ideally with a titration experiment. Use an untagged or differently tagged Sp100A to confirm the phenotype. Consider generating stable cell lines with inducible expression to control for expression levels.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, last sentence
- **Issue** The statement that HIRA recruitment is "potentially required for maintaining epigenetic memory by delayed H3.3 incorporation" is presented as a conclusion but is not directly tested in this study.
- **Required correction** Rephrase to clearly indicate this is a hypothesis or speculation, not a finding of this work.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 7B
- **Evidence pointer** Results section "Sp100A SUMO interacting motif is important for HIRA localization at PML"
- **Issue** The immunoblot quantitation is described as normalized to Tubulin, but the authors note that IFN treatment reduced Tubulin levels. This could confound the normalization.
- **Required correction** Provide normalization to a loading control that is not affected by IFN treatment, or justify the use of Tubulin with appropriate controls.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** RNA-seq analysis
- **Evidence pointer** Figure 8, Results section "RNA-seq analysis shows no significant changes in basal or interferon-stimulated gene expression in the Sp100 KO cells"
- **Issue** The authors state there were "no major differences" but do not report the statistical thresholds, number of differentially expressed genes, or power analysis. The PCA is descriptive.
- **Required correction** Report the differential expression analysis criteria (e.g., adjusted p-value, fold-change cutoff), the number of genes passing thresholds, and consider a power analysis to justify the negative result.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** CRISPR KO generation
- **Evidence pointer** Results section "Generation of Sp100-deficient NIKS cell lines"
- **Issue** The authors describe using five gRNAs targeting exons 3, 6, and 8, but the genotyping results in Table S1 show mutations only in exons 3 and 8. The reason for the lack of mutations in exon 6 is not discussed.
- **Required correction** Clarify whether exon 6 mutations were not recovered, or whether they were not required for KO. Discuss potential off-target effects of the gRNAs.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion of IFN rescue
- **Evidence pointer** Results section "Sp100A SUMO interacting motif is important for HIRA localization at PML"
- **Issue** The IFN-dependent rescue of HIRA localization in the mSIM mutant is a key observation, but the authors do not discuss alternative explanations, such as IFN-induced changes in PML-NB composition or HIRA modification.
- **Required correction** Expand the discussion to consider these alternatives and propose experiments to distinguish them.

## Risk / unsupported claims
- The claim that Sp100A is "primarily responsible" for HIRA localization is not fully supported without quantitative comparison of isoform expression levels and unbiased image analysis.
- The mechanistic role of the SIM motif is inferred from mutagenesis alone; no direct interaction data are provided.
- The structural models and molecular dynamics simulations are presented as supportive but are not experimentally validated; the claim that C-terminal domains sterically hinder HIRA recruitment is speculative.
- The conclusion that HIRA recruitment is not required for immediate IFN signaling is supported, but the extension to "epigenetic memory" is not tested in this study.
- The RNA-seq negative result is reported without sufficient statistical detail to assess its robustness.
- The statement that Sp100 KO cells show "normal" differentiation is based on morphology alone (Fig. S2); no molecular markers are shown.