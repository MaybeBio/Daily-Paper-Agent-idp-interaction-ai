## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, figure legends not fully provided)
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text
- **Shared manuscript claim summary** The authors identify molecular determinants of PKA RIα phase separation, showing that two dimerization interfaces (D/D domain and N3A motif) and the disordered linker region drive condensate formation, that cAMP-induced release of PKA-C from the pseudosubstrate inhibitory sequence promotes LLPS, and that a non-canonical R:C complex within condensates sequesters active PKA-C to modulate cytosolic PKA activity
- **Visible evidence base** Results sections describing cell-based imaging assays (puncta formation), BRET-based dimerization and dissociation assays, in vitro droplet assays, FRAP, FLIM-FRET, and FRET-based PKA activity biosensor experiments; supplementary figure references cited but not provided
- **Missing materials affecting confidence** Supplementary figures (S1-S6) and tables (S1-S2) not provided; figure panels referenced but not viewable; detailed statistical outputs and raw data not available; methods for some assays abbreviated

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question regarding the molecular mechanisms of PKA RIα phase separation and its functional consequences for cAMP signaling. The authors build on their prior work and provide a systematic dissection of the determinants of RIα LLPS, with several notable findings including the role of the N3A motif as a secondary dimerization interface and the identification of a non-canonical R:C complex within condensates. The work is technically ambitious, combining multiple live-cell imaging modalities with in vitro reconstitution. However, several claims, particularly regarding the non-canonical R:C complex and its functional significance, require stronger direct evidence. The manuscript would benefit from clearer presentation of quantitative data and additional controls to distinguish between competing models of R:C interaction within condensates.

- **Who would be interested in the results, and why** Researchers studying cAMP/PKA signaling, phase separation and biomolecular condensates, protein kinase regulation, and cell signaling compartmentation would find this work of interest. The findings have potential implications for understanding diseases associated with RIα mutations and for therapeutic targeting of PKA signaling.

- **Major strengths** The study addresses a significant gap in understanding the molecular determinants of RIα phase separation. The combination of structure-guided mutagenesis with multiple orthogonal assays (BRET, imaging, in vitro reconstitution) provides a comprehensive approach. The identification of the N3A motif as a second dimerization interface required for LLPS is a novel contribution. The finding that PKA-C can be retained within condensates via a non-canonical interaction has conceptual implications for how condensates may buffer or compartmentalize kinase activity.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency for non-canonical R:C complex
- **Claim pointer** The authors claim that "a non-canonical R:C complex which recruits active PKA-C to RIα condensates" exists and that this complex "minimizes the mutual inhibition between PKA-C and RIα so that PKA-C is active and RIα is able to form condensates"
- **Evidence point** Results section "Non-canonical PKA Cα recruitment to RIα condensates"; Figures 6A-E, S6A-G
- **Concern** The evidence for a non-canonical R:C complex relies primarily on colocalization (Pearson's correlation), FRAP recovery differences, and FLIM-FRET measurements. However, the authors do not provide direct biochemical evidence for a stable R:C interaction under cAMP-saturating conditions. The FLIM-FRET data show a modest difference in fluorescence lifetime (2.4 vs 2.59 ns) that could be influenced by local environmental factors within condensates rather than specific molecular interactions. The in vitro droplet experiments with purified proteins are described but the actual data are only in supplementary figures. The claim that PKA-C is "active" within condensates is inferred from the FluoSTEP-AKAR biosensor, but this measures local PKA activity and does not directly demonstrate that the R:C complex itself is catalytically active. The authors should provide more direct evidence, such as co-immunoprecipitation of RIα and PKA-C under cAMP conditions, or in vitro binding assays with purified components, to support the existence of a stable non-canonical complex.
- **Why it matters** The existence of a non-canonical, catalytically active R:C complex is a central claim of the paper and revises the classical model of PKA activation. If this claim is not rigorously supported, the functional significance of the findings is substantially weakened.
- **Resolution test** Provide biochemical evidence (e.g., co-IP, pull-down, or analytical ultracentrifugation) demonstrating stable RIα:PKA-C interaction in the presence of saturating cAMP. Alternatively, show that purified RIα and PKA-C form a complex in vitro with measurable binding affinity under conditions where PKA-C is catalytically active.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal link between dimerization interfaces and LLPS
- **Claim pointer** The authors claim that "two distinct interfaces within the RIα dimer are required for LLPS" and that the N3A motif "forms a unique, secondary dimer interface" that contributes to condensate formation
- **Evidence point** Results sections "Dimerization promotes and AKAP anchoring disrupts RIα condensate formation in cytosol" and "RIα LLPS involves a secondary dimer interface"; Figures 1, 3
- **Concern** The authors show that the L50R mutation disrupts both dimerization and LLPS, and that Y122A reduces dimerization and abolishes cAMP-stimulated puncta formation. However, the causal relationship between dimerization and LLPS is not fully established. The L50R mutation could disrupt LLPS through mechanisms other than loss of dimerization, such as altered protein folding or stability. Similarly, Y122A is in the N3A motif, which is also involved in cAMP-induced conformational changes; the effect on LLPS could be due to impaired cAMP signaling rather than loss of the secondary dimer interface. The authors should perform experiments that specifically disrupt the N3A dimer interface without affecting cAMP binding or use dimerization-deficient mutants that retain normal folding to strengthen the causal claim.
- **Why it matters** The identification of specific molecular determinants of LLPS is a key contribution. If the causal link between dimerization interfaces and LLPS is not clearly established, the mechanistic model proposed is on weaker footing.
- **Resolution test** Use structure-guided mutations that specifically disrupt the N3A dimer interface while preserving cAMP binding and PKA-C interaction. Alternatively, demonstrate that dimerization-deficient RIα mutants can be rescued by engineered dimerization domains to restore LLPS.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Functional significance of PKA-C sequestration
- **Claim pointer** The authors claim that "RIα LLPS not only facilitates cAMP compartmentation but also spatially restrains active PKA-C" and that disruption of the non-canonical R:C complex "leads to elevated cytosolic PKA activity"
- **Evidence point** Results section "Non-canonical PKA Cα recruitment to RIα condensates"; Figures 6F-G, S6H-K
- **Concern** The functional significance of PKA-C sequestration within condensates is inferred from comparing cytosolic PKA activity in cells expressing RIαWT versus RIαA99S. However, the A99S mutation has multiple effects: it weakens the R:C interaction, enhances LLPS, and promotes PKA-C release. The observed increase in cytosolic PKA activity could be due to any of these effects, not specifically to loss of PKA-C sequestration within condensates. The authors should use more specific perturbations that separate the effects on LLPS from effects on PKA-C binding. Additionally, the physiological relevance of the observed differences in basal PKA activity is unclear, as the magnitude of the effect and its downstream consequences are not fully explored.
- **Why it matters** The claim that condensates function to spatially restrain active PKA-C is a novel and important finding. If the causal link is not clearly established, the functional model proposed is weakened.
- **Resolution test** Use mutants that specifically disrupt PKA-C binding to condensates without affecting LLPS itself, or use optogenetic or chemically inducible systems to acutely disrupt the non-canonical R:C interaction and measure effects on PKA activity.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative rigor and statistical reporting
- **Claim pointer** Multiple quantitative claims throughout the results, including puncta counts, FRAP recovery rates, FLIM lifetimes, and BRET ratios
- **Evidence point** Results sections throughout; Figures 1, 3, 5, 6
- **Concern** The manuscript reports numerous quantitative measurements but the statistical reporting is inconsistent. Some comparisons report P values and confidence intervals, while others do not. The number of biological replicates and independent experiments is not consistently stated for each figure. The methods section describes statistical tests but does not specify which test was used for each comparison. Given the variability inherent in imaging-based assays, more rigorous and transparent statistical reporting is needed.
- **Why it matters** The conclusions depend on quantitative comparisons between conditions. Without clear statistical reporting, the reliability of the conclusions cannot be fully assessed.
- **Resolution test** Provide complete statistical details for each figure, including sample sizes, number of independent experiments, statistical tests used, and effect sizes. Consider including data points in all bar graphs and providing confidence intervals for key comparisons.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of model presentation
- **Affected element** Discussion section, model figure (not provided)
- **Evidence point** Discussion section
- **Issue** The proposed model of non-canonical R:C complex formation and its relationship to canonical holoenzyme dissociation is described in text but a clear schematic model figure is not described in the provided text. A visual model would help readers understand the proposed mechanism.
- **Required correction** Include a model figure that schematically depicts the canonical and non-canonical R:C complexes, the role of cAMP, and how LLPS relates to PKA-C sequestration.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Throughout the manuscript
- **Evidence point** Results and Discussion sections
- **Issue** The terms "condensate," "droplet," "puncta," and "phase separation" are used somewhat interchangeably. While these terms are related, they have distinct meanings in the field. The manuscript would benefit from consistent terminology.
- **Required correction** Define terms early in the manuscript and use them consistently. For example, "puncta" for cellular imaging observations and "droplets" for in vitro assays.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Control experiments
- **Affected element** Results sections
- **Evidence point** Figures 1, 3, 5
- **Issue** The manuscript does not clearly describe control experiments for the specificity of the observed puncta formation. For example, it is unclear whether the puncta represent liquid-like condensates with dynamic properties or more solid aggregates. FRAP experiments are described but the mobile fraction values are not reported.
- **Required correction** Report mobile fractions from FRAP experiments and include controls such as treatment with 1,6-hexanediol to demonstrate liquid-like properties.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Supplementary data accessibility
- **Affected element** Supplementary figures and tables
- **Evidence point** Throughout
- **Issue** The manuscript relies heavily on supplementary figures and tables, but these are not provided in the submitted text. Key data, including in vitro droplet assays, additional controls, and sequence analysis, are only in supplementary materials.
- **Required correction** Ensure all supplementary materials are complete and accessible. Consider moving key data from supplementary to main figures if they are essential for the main conclusions.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** In vitro droplet assay
- **Evidence point** Methods section "In vitro liquid droplet assay"
- **Issue** The description of the in vitro droplet assay is brief. Details on protein concentrations, buffer conditions, imaging parameters, and quantification methods are not fully described.
- **Required correction** Provide complete methodological details for the in vitro droplet assay, including protein concentration ranges, salt conditions, and how droplet formation was quantified.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Discussion of alternative models
- **Affected element** Discussion section
- **Evidence point** Discussion section
- **Issue** The discussion does not adequately address alternative interpretations of the data. For example, the possibility that PKA-C localization to condensates is due to passive diffusion and trapping rather than specific R:C interactions is not discussed.
- **Required correction** Add a paragraph discussing alternative models and how the data distinguish between them.

## Risk / unsupported claims
- The existence of a stable, non-canonical R:C complex within condensates under cAMP-saturating conditions is not directly supported by biochemical evidence; current evidence is indirect (colocalization, FRAP, FLIM-FRET)
- The claim that PKA-C is catalytically active within the non-canonical R:C complex is inferred from biosensor measurements and not directly demonstrated
- The causal link between the N3A dimer interface and LLPS is not fully established, as the Y122A mutation may affect cAMP-induced conformational changes independently of dimerization
- The functional significance of PKA-C sequestration in regulating cytosolic PKA activity is based on comparisons using the A99S mutation, which has pleiotropic effects
- The claim that AKAP docking inhibits LLPS is based on overexpression experiments and may not reflect endogenous stoichiometries
- Quantitative claims regarding puncta numbers, FRAP recovery, and FLIM lifetimes cannot be fully assessed without access to supplementary figures and raw data
- The physiological relevance of the findings in disease contexts is speculative and not directly tested