## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, figure legends, and supplementary information descriptions.
- **Assessment boundary** Scientific content, technical soundness, logical coherence, and alignment with the stated claims. Editorial and formatting issues are noted only where they affect comprehension.
- **Shared manuscript claim summary** The authors propose that phosphorylation tunes strain-specific protein condensation during rotavirus replication organelle assembly. Using machine learning (DeePhase), they identify rotavirus NSP5 variants with low liquid-liquid phase separation (LLPS) propensity, engineer a low-LLPS variant (SCLow), and demonstrate that phosphorylation is required for this variant to undergo phase separation and support viroplasm formation. They further propose a phosphorylation-driven allosteric switch that alters NSP2-NSP5 interactions in a strain-specific manner.
- **Visible evidence base** Abstract, full results section with figure legends (Figs 1-10, EV1-EV5), discussion, methods, and supplementary information descriptions. No raw data, source data files, or supplementary tables were provided for independent verification.
- **Missing materials affecting confidence** Source data files, Appendix Table S1 (DeePhase scores), Appendix Fig S1 (sequencing stability), raw HDX-MS data, mass spectrometry phosphorylation data, and detailed statistical outputs. The absence of these materials limits independent verification of quantitative claims.

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question in virology: whether the mechanism of rotavirus replication organelle assembly via LLPS is conserved across diverse strains, and how phosphorylation modulates this process. The combination of computational prediction, protein engineering, in vitro biochemistry, and virology is ambitious and largely well-executed. The central finding that a low-LLPS NSP5 variant requires phosphorylation to nucleate phase separation is novel and mechanistically interesting. However, several technical concerns, particularly around the interpretation of HDX-MS data, the specificity of the phosphomimetic approach, and the quantitative rigor of the phase separation assays, need to be addressed before the case is fully established. The manuscript is well-written and will be of interest to the virology and phase separation communities.
- **Who would be interested in the results, and why** Virologists studying rotavirus replication and other RNA viruses that form replication organelles via phase separation; cell biologists interested in the regulation of biomolecular condensates by post-translational modifications; and computational biologists developing and applying LLPS prediction tools. The finding that phosphorylation can compensate for low intrinsic LLPS propensity has broad implications for understanding how condensate formation is regulated in diverse biological contexts.
- **Major strengths**
  1. The study addresses a significant gap in the field by systematically examining strain-specific differences in NSP5 LLPS propensity, moving beyond the well-characterized SA11 strain.
  2. The combination of DeePhase predictions with experimental validation (in vitro phase separation, cell-based viroplasm formation) provides a strong framework for testing computational predictions.
  3. The engineering of SCLow, a low-LLPS variant that retains function, is a clever approach that allows the authors to dissect the role of phosphorylation in a physiologically relevant context.
  4. The HDX-MS data, while requiring further validation, offer a promising avenue for understanding the molecular basis of phosphorylation-dependent interaction changes.
  5. The manuscript is clearly written and the figures are generally well-organized and informative.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "phosphorylation restores phase separation and viroplasm formation by a low-LLPS NSP5 variant" based on experiments using phosphomimetic S-to-D mutations.
- **Evidence pointer** Figure 5, Figure 6, Figure EV3
- **Concern** The use of phosphomimetic S-to-D mutations as a proxy for actual phosphorylation is a significant limitation. While the authors show that SCLow treated with CKII and ATP forms condensates (Fig 5B), the phosphomimetic approach does not fully recapitulate the dynamic and site-specific nature of phosphorylation. The authors do not demonstrate that the S-to-D mutations accurately mimic the structural and electrostatic effects of phosphorylation at each site. Furthermore, the authors state that a single S67D substitution was insufficient to restore phase separation, but they do not systematically investigate which combinations of phosphorylation sites are necessary and sufficient. The claim that "multi-site phosphorylation across the IDR is required" is based on the observation that eight S-to-D mutations are needed, but this does not rule out the possibility that a smaller subset of specific sites is critical.
- **Why it matters** The central mechanistic claim of the paper rests on the interpretation that phosphorylation, and not merely the introduction of negative charge, is the key driver of phase separation in low-LLPS variants. Without a more rigorous validation of the phosphomimetic approach, the physiological relevance of these findings remains uncertain. The authors should either (a) validate the phosphomimetic mutations by comparing their effects to those of bona fide phosphorylation (e.g., by in vitro kinase assays with mass spectrometry confirmation of phosphorylation site occupancy), or (b) temper their claims and explicitly discuss the limitations of the phosphomimetic approach.
- **Resolution test** The authors should provide additional data demonstrating that the S-to-D mutations phenocopy the effects of actual phosphorylation. This could include: (1) mass spectrometry analysis of CKII-phosphorylated SCLow to confirm which sites are phosphorylated; (2) comparison of the phase separation behavior of CKII-phosphorylated SCLow with that of the SCLow HP variant; (3) site-directed mutagenesis to identify the minimal set of phosphorylation sites required for phase separation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that HDX-MS reveals "a phosphorylation-driven allosteric switch that alters NSP2 interactions depending on the NSP5 variant."
- **Evidence pointer** Figure 10
- **Concern** The HDX-MS data are presented as the key evidence for the proposed allosteric mechanism, but the interpretation is not fully supported by the data shown. The Woods plots in Figure 10 compare deuterium uptake between conditions, but the authors do not provide sufficient detail on the statistical significance of the observed differences, the reproducibility of the experiments, or the peptide-level resolution of the data. The claim of an "allosteric switch" implies a specific conformational change, but HDX-MS alone cannot distinguish between local conformational changes, changes in protein dynamics, or changes in binding interfaces. The authors also do not provide a clear structural model or a quantitative framework for how the observed protection/deprotection patterns translate into altered interaction affinities or specificities.
- **Why it matters** The proposed allosteric mechanism is a major conceptual advance of the paper. If the HDX-MS data are not robustly analyzed and interpreted, the mechanistic model is not well-supported. The authors need to provide a more detailed and rigorous analysis of their HDX-MS data, including: (a) the number of biological and technical replicates; (b) the statistical criteria used to identify significant differences; (c) the peptide-level coverage map; (d) a discussion of the limitations of HDX-MS for inferring allosteric mechanisms.
- **Resolution test** The authors should provide a more comprehensive HDX-MS analysis, including a full peptide coverage map, a volcano plot or similar statistical representation of significant differences, and a clear description of how the observed protection/deprotection patterns support the proposed allosteric model. Ideally, they would also validate the model using an orthogonal approach, such as cross-linking mass spectrometry or NMR.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that "phosphorylation plays a context-dependent role in condensate formation, tuning NSP5-NSP2 interactions in a strain-specific manner."
- **Evidence pointer** Figures 5, 6, 10
- **Concern** While the data support a role for phosphorylation in enabling phase separation of the low-LLPS SCLow variant, the broader claim of "strain-specific" tuning is not fully substantiated. The authors compare only a limited number of NSP5 variants (SA11, RF, SCLow, S4Low) and do not systematically explore the diversity of NSP5 sequences across a wider panel of rotavirus strains. The DeePhase analysis of 451 sequences is computational and not experimentally validated for most of these variants. The claim that this represents a "strain-specific" mechanism would be strengthened by demonstrating that the phosphorylation-dependent regulation varies predictably with sequence features across a larger panel of strains.
- **Why it matters** The title and abstract emphasize strain-specificity, which is a key aspect of the paper's significance. If the experimental evidence only covers a few strains, the claim may be overstated. The authors should either expand their experimental analysis to include more strains with varying LLPS propensities, or moderate their claims to reflect the limited number of strains tested.
- **Resolution test** The authors should either (a) experimentally test the phosphorylation dependence of phase separation for a larger panel of NSP5 variants with a range of DeePhase scores, or (b) revise the title and abstract to more accurately reflect the scope of the experimental evidence.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "DeePhase accurately predicted LLPS potential: all four tested variants SA11, RF and SCLow and S4Low behaved as expected in vitro."
- **Evidence pointer** Figure 5, Figure 6
- **Concern** The validation of DeePhase predictions is based on a small number of variants (n=4). While the correlation between predicted and observed behavior is encouraging, the sample size is too small to draw robust conclusions about the predictive accuracy of the model. Furthermore, the authors do not provide a quantitative comparison between predicted scores and experimentally measured phase separation thresholds (e.g., Csat values). A more rigorous validation would involve testing a larger panel of variants and correlating predicted scores with experimentally determined Csat values.
- **Why it matters** The use of DeePhase as a predictive tool is a key methodological contribution. If the validation is weak, the utility of the approach for future studies is uncertain. The authors should provide a more robust validation, either by testing more variants or by providing a quantitative correlation between predicted and measured values.
- **Resolution test** The authors should either (a) experimentally test a larger panel of NSP5 variants (e.g., 10-20) and provide a quantitative correlation between DeePhase scores and experimentally determined Csat values, or (b) clearly state the limitations of the validation and avoid overstating the predictive power of the model.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and reproducibility
- **Affected element** Methods, "Phosphorylation analysis by liquid chromatography-mass spectrometry"
- **Evidence pointer** Methods section
- **Issue** The description of the LC-MS method for phosphorylation analysis is brief and lacks critical details, such as the type of mass spectrometer used for the phosphorylation site mapping, the data analysis software parameters, and the criteria for confident phosphorylation site localization.
- **Required correction** The authors should expand the LC-MS methods to include details on the mass spectrometry data acquisition (e.g., DDA or DIA), the search engine and database used, the false discovery rate thresholds, and the criteria for phosphorylation site localization (e.g., Ascore or phosphoRS).

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity and reproducibility
- **Affected element** Figure 6
- **Evidence pointer** Figure 6 legend
- **Issue** The figure legend for Figure 6 does not clearly describe how the phase boundaries were inferred from the PhaseScan data. The black dotted lines are described as "inferred phase boundaries," but the statistical or computational method used to infer these boundaries is not described.
- **Required correction** The authors should describe the method used to infer phase boundaries from the PhaseScan data, including any fitting procedures or statistical criteria.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity and reproducibility
- **Affected element** Results, "SCLow-RV displays delayed viroplasm maturation and reduced NSP5 hyperphosphorylation"
- **Evidence pointer** Figure 4
- **Concern** The quantification of viroplasm number and area in Figure 4B,C is described as being from "three independent experiments (N > 200 cells per condition)," but the statistical analysis is not fully described. The authors state that a two-way ANOVA was used, but do not specify the factors or the post-hoc test used.
- **Required correction** The authors should provide a more detailed description of the statistical analysis, including the factors in the ANOVA, the post-hoc test used, and the exact p-values for all comparisons.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity and reproducibility
- **Affected element** Methods, "Western blotting"
- **Evidence pointer** Methods section
- **Issue** The western blotting method describes the use of an anti-actin antibody for normalization, but the quantification method is not described. It is unclear whether the band intensities were normalized to total protein or to a specific loading control.
- **Required correction** The authors should describe the quantification method used for western blots, including the software used and the normalization strategy.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity and reproducibility
- **Affected element** Results, "Engineering an NSP5 variant with diminished LLPS potential"
- **Evidence pointer** Figure 2
- **Concern** The description of the DeePhase analysis is clear, but the authors do not provide a measure of uncertainty for the DeePhase scores. It would be helpful to know the confidence intervals or standard deviations for the scores, particularly for the SCLow variant.
- **Required correction** The authors should provide a measure of uncertainty for the DeePhase scores, or at least discuss the potential variability in the predictions.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Validation of phosphomimetic approach against bona fide phosphorylation.
  - R1-M2: Rigorous analysis and interpretation of HDX-MS data.
  - R1-M4: More robust validation of DeePhase predictions.

- **Assessment against Nature-style criteria**
  - **Originality** The work is original in its systematic approach to comparing LLPS propensity across rotavirus strains and in its identification of phosphorylation as a compensatory mechanism for low intrinsic LLPS propensity. The concept of a phosphorylation-driven allosteric switch in a viral IDP is novel.
  - **Scientific importance** The findings have significant implications for understanding the diversity of mechanisms underlying viral replication organelle formation. The work also contributes to the broader understanding of how post-translational modifications regulate biomolecular condensates. The potential for targeting this regulatory mechanism for antiviral intervention is an important translational aspect.
  - **Interdisciplinary readership** The work bridges virology, biophysics, and computational biology. The use of machine learning and biophysical assays will appeal to a broad readership. The clear writing and well-organized figures make the work accessible to nonspecialists.
  - **Technical soundness** The experimental approaches are generally sound, but the concerns raised above (phosphomimetic validation, HDX-MS interpretation, DeePhase validation) need to be addressed to fully establish the case. The statistical analyses are mostly appropriate, but some details are missing.
  - **Readability for nonspecialists** The manuscript is well-written and the concepts are explained clearly. The use of figures to illustrate the proposed model is helpful. The abstract is concise and accessible.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important question and presents a novel and interesting model. However, the key mechanistic claims, particularly regarding the phosphorylation-driven allosteric switch, require stronger experimental support. The authors should address the concerns raised above, particularly the validation of the phosphomimetic approach and the rigor of the HDX-MS analysis, before the case is fully established.

## Risk / unsupported claims
- The claim that "phosphorylation plays a context-dependent role in condensate formation, tuning NSP5-NSP2 interactions in a strain-specific manner" is partially supported but overstated given the limited number of strains experimentally tested.
- The claim of a "phosphorylation-driven allosteric switch" is not fully supported by the HDX-MS data as presented.
- The claim that "DeePhase accurately predicted LLPS potential" is based on a small validation set and should be tempered.
- The statement that "multi-site phosphorylation across the IDR is required to reach the threshold necessary for phase separation" is inferred from the phosphomimetic data but not directly tested with actual phosphorylation.
- The functional significance of the delayed viroplasm maturation in SCLow-RV-infected cells is not fully explored; the authors state that "viral replication proceeds efficiently" but do not provide a detailed comparison of viral growth kinetics or yield.