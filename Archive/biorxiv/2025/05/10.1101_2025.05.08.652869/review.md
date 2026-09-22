## Review setup
- **Input scope** Full manuscript text (Summary, Introduction, Results, Discussion, Limitations, Materials and Methods) as provided
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text; no external data or figures were available for direct inspection
- **Shared manuscript claim summary** The authors propose that tensin 1 (TNS1) forms biomolecular condensates in cells via phase separation, that these condensates act as selective reservoirs for inactive adhesion proteins, that the TNS1 intrinsically disordered region (IDR) drives condensation, and that stress-induced phosphorylation negatively regulates condensation to control adhesion dynamics and cell migration
- **Visible evidence base** Text descriptions of results referencing Figures 1–7, Supplementary Figures S1–S7, Movies S1–S8, and Tables S1–S3; no actual data, images, or numerical values were provided
- **Missing materials affecting confidence** All primary data (figures, quantitative measurements, statistical outputs, proteomics tables, microscopy images, FRAP curves, and molecular dynamics simulation details) were not available for direct evaluation; the manuscript appears to be a preprint without full figure content in the provided text

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question in cell adhesion biology: how the availability of adhesion components is regulated to support dynamic remodeling of integrin adhesion complexes. The central hypothesis, that TNS1 forms phase-separated condensates acting as reservoirs for inactive adhesion proteins, is conceptually novel and mechanistically plausible. The authors combine cell biology, proteomics, phosphoproteomics, and molecular dynamics approaches to build a multi-layered case. However, the provided text lacks the actual data needed to verify the strength of the evidence. Several claims, particularly regarding the selectivity of condensate composition, the functional consequences of IDR deletion, and the phosphorylation-dependent regulation, require careful quantitative scrutiny. The study is potentially significant for the adhesion and phase separation communities, but the current evidence base, as described, does not fully establish the model. The manuscript would benefit from clearer presentation of quantitative data, additional controls, and a more cautious interpretation of correlative observations.
- **Who would be interested in the results, and why** Cell biologists studying focal adhesion dynamics, integrin signaling, and cell migration would find this work directly relevant. The phase separation community, particularly those interested in cytoplasmic condensates beyond nuclear bodies, would also be engaged. Researchers working on tensin family proteins and their roles in adhesion maturation would find the IDR-mediated condensation mechanism of high interest. The potential link to stress signaling and EMT could attract cancer biology audiences. The study bridges biophysical concepts (phase separation) with cell biological function (adhesion dynamics), which broadens its appeal.
- **Major strengths** The study addresses a fundamental gap in understanding how adhesion component availability is regulated. The use of endogenous tagging (mGreenLantern) strengthens the physiological relevance of the observations. The combination of 2D and 3D contexts, the inhibitor screen, and the phosphoproteomic analysis provide a multi-pronged approach. The identification of the IDR as the driver of condensation, with specific sub-regions contributing differentially, adds mechanistic depth. The phosphomimetic and phosphodead mutant strategy is a logical approach to test the functional role of phosphorylation. The acknowledgment of limitations, particularly the inability to perform in vitro reconstitution, is transparent.
- **Major Concerns** The major concerns are detailed below. In summary, the evidence for phase separation as the underlying mechanism is incomplete, the selectivity of condensate composition requires more rigorous demonstration, the functional significance of condensation is not fully separated from other TNS1 functions, and the phosphorylation data, while suggestive, lack direct causal evidence.
- **Minor Comments** Several minor issues are listed below, including clarity of figure descriptions, statistical reporting, and interpretation of correlative data.
- **Technical failings that need to be addressed before the case is established** The lack of in vitro reconstitution data, the absence of a direct demonstration that condensation is required for the observed functional effects, and the incomplete quantitative analysis of condensate properties and composition are the main technical gaps.
- **Assessment against Nature-style criteria**  
  *Originality*: The concept of adhesion-derived condensates as reservoirs for inactive proteins is novel and extends the phase separation paradigm to adhesion biology. This is a fresh perspective.  
  *Scientific importance*: The work addresses a fundamental question in cell adhesion and migration, with potential implications for understanding how cells rapidly remodel adhesions. The link to stress signaling adds broader relevance.  
  *Interdisciplinary readership*: The study bridges biophysics, cell biology, and proteomics, which could attract a broad audience. However, the specialized nature of adhesion biology may limit appeal to a general readership.  
  *Technical soundness*: The experimental design is generally sound, but the lack of in vitro data and the reliance on overexpression for some experiments weaken the technical foundation. The proteomics and phosphoproteomics approaches are appropriate but require full data transparency.  
  *Readability for nonspecialists*: The text is well-written and logically structured, but the heavy reliance on domain-specific terminology (e.g., IDR, condensate, FA) may pose challenges for nonspecialists. A clearer explanation of phase separation concepts would improve accessibility.
- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual framework is promising and the experimental approach is largely appropriate, but the current evidence, as described, does not fully establish the central claims. The authors should address the major concerns with additional data and analyses before the manuscript is considered for publication in a high-impact journal.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency for phase separation mechanism  
- **Claim pointer** The authors claim that TNS1 undergoes phase separation in cells, supported by concentration-dependent condensate formation, fusion, fission, and FRAP recovery.  
- **Evidence pointer** Figures 1A–1F, S1A–S1D, Movies S1–S5; location not provided for specific data points  
- **Concern** The evidence for phase separation is largely phenomenological. Concentration-dependent condensate formation, fusion, and FRAP recovery are consistent with phase separation but are not definitive. The authors do not provide evidence for key phase separation criteria, such as a saturation concentration, sensitivity to 1,6-hexanediol, or disruption by mutations in predicted interaction motifs. The FRAP recovery of ~49% with a half-life of ~27 s is reported, but it is unclear how this compares to other condensate systems or whether it reflects liquid-like behavior. The lack of in vitro reconstitution, acknowledged in the Limitations, is a significant gap. Without purified protein or a minimal system, the claim that TNS1 intrinsically undergoes phase separation is not fully supported.  
- **Why it matters** Phase separation is a specific biophysical mechanism with distinct criteria. If the observed condensates are aggregates or result from other processes (e.g., oligomerization), the conclusions about reservoir function and regulation would be weakened. The manuscript's central thesis depends on the phase separation mechanism being correct.  
- **Resolution test** Provide in vitro phase separation assays with purified TNS1 or its IDR, demonstrate saturation concentration, test sensitivity to known phase separation disruptors, and show that condensate formation is reversible and concentration-dependent in a quantitative manner.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Selectivity of condensate composition  
- **Claim pointer** The authors claim that TNS1 condensates act as selective reservoirs for inactive adhesion proteins, recruiting a subset of FA components (TNS3, ZYX, PXN, CAS) while excluding others (FAK, TLN1, TLN2, VCL, KANK2).  
- **Evidence pointer** Figures 3C–3D, S3F; location not provided for specific images  
- **Concern** The selectivity claim is based on immunofluorescence colocalization, which is limited by resolution and antibody specificity. The authors do not provide quantitative colocalization analyses or demonstrate that the absence of signal for excluded proteins is not due to epitope masking or antibody accessibility issues. The BioID proximity labeling data (Figure 3B, S3C) are mentioned but not presented in detail, so it is unclear whether the selectivity is supported by proteomics. The functional significance of selective recruitment is also not directly tested; the authors show that TNS1 overexpression stabilizes ZYX and PXN levels, but this could be an indirect effect.  
- **Why it matters** The reservoir model depends on the selective recruitment of specific proteins. If the selectivity is not robust, the model loses its explanatory power. The distinction between active and inactive protein states is also inferred from phosphorylation status, but this is not directly demonstrated for the recruited proteins.  
- **Resolution test** Provide quantitative colocalization analyses (e.g., Pearson's coefficient) for recruited and excluded proteins, validate with super-resolution imaging, and confirm selectivity using the BioID data with appropriate statistical thresholds. Test the functional requirement for selective recruitment by disrupting condensate formation and measuring protein stability or availability.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Causal link between IDR, condensation, and function  
- **Claim pointer** The authors claim that the TNS1 IDR drives condensation and that IDR deletion (ΔIDR) leads to increased FA dynamics, migration, and invasion, implying that condensation negatively regulates these processes.  
- **Evidence pointer** Figures 4B–4F, 5A–5L, S4B, S5A–S5L; location not provided for specific data  
- **Concern** The ΔIDR mutant abolishes condensation, but the IDR is a large region likely involved in multiple protein-protein interactions beyond phase separation. The observed phenotypes (increased FA dynamics, migration, invasion) could be due to loss of specific binding partners rather than loss of condensation per se. The authors do not perform rescue experiments with condensation-competent but interaction-deficient mutants, or vice versa. The phosphomimetic (SD) and phosphodead (SG) mutants are used to link phosphorylation to condensation, but the specificity of these mutations is not fully validated. The correlation between condensate formation and functional outcomes is suggestive but not causal.  
- **Why it matters** The manuscript claims that condensation is a regulatory mechanism controlling adhesion dynamics. If the effects are due to other IDR functions, the central thesis is weakened. The distinction between condensation-dependent and condensation-independent functions is critical for the paper's impact.  
- **Resolution test** Perform structure-function analyses with IDR sub-deletions or point mutations that disrupt condensation without affecting known binding interactions. Rescue experiments with condensation-competent constructs in TNS1 KO cells should be performed. Validate the phosphomutants by confirming that they specifically affect phosphorylation at the targeted sites and that the effects on condensation are direct.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Quantitative rigor of functional assays  
- **Claim pointer** The authors claim that TNS1 ΔIDR and SD mutants increase FA dynamics, migration, and invasion compared to WT and SG.  
- **Evidence pointer** Figures 5A–5L, S5A–S5L; location not provided for specific data  
- **Concern** The functional assays are described qualitatively. For example, FA assembly and disassembly rates are mentioned, but the methodology for calculating these rates is not detailed. The migration and invasion assays are described, but the magnitude of effects and statistical significance are not reported in the text. The traction force measurements are mentioned, but the number of cells analyzed and the variability are not provided. Without quantitative details, it is difficult to assess the robustness of the phenotypes.  
- **Why it matters** The functional claims are central to the paper's significance. If the effects are small or variable, the conclusions may be overstated. Quantitative rigor is essential for reproducibility and for convincing readers of the biological relevance.  
- **Resolution test** Provide detailed methodology for all functional assays, including sample sizes, statistical tests, and effect sizes. Include representative data with appropriate error bars and significance levels in the figures.

- **Concern ID** R1-M5  
- **Severity** Major  
- **Blocking** No  
- **Axis** Phosphorylation mechanism and kinase specificity  
- **Claim pointer** The authors claim that stress-induced phosphorylation by p38, ERK, and AKT negatively regulates TNS1 condensation.  
- **Evidence pointer** Figures 6A–6L, S6A–S6L; location not provided for specific data  
- **Concern** The phosphoproteomic analysis identified 26 significantly enriched phosphorylation sites, but the specific sites responsible for regulating condensation are not identified. The kinase inhibitor experiments show that inhibiting p38, MEK, and AKT impairs arsenite-induced TNS1 translocation, but this is a pharmacological approach with potential off-target effects. The authors do not demonstrate direct phosphorylation of TNS1 by these kinases in vitro or in cells. The phosphomimetic and phosphodead mutants target 36 sites, but the rationale for selecting these specific sites is not clearly explained.  
- **Why it matters** The claim that phosphorylation regulates condensation is a key mechanistic insight. Without identifying the specific phosphorylation sites and validating the kinase-substrate relationship, the mechanism remains correlative. This weakens the paper's contribution to understanding how stress signals regulate adhesion dynamics.  
- **Resolution test** Identify the specific phosphorylation sites that affect condensation using mass spectrometry and site-directed mutagenesis. Validate kinase-substrate relationships using in vitro kinase assays and phospho-specific antibodies. Use genetic approaches (e.g., kinase knockouts or dominant-negative mutants) to confirm the pharmacological data.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity of figure descriptions  
- **Affected element** Figures 1A–1F, 2A–2H, 3A–3K, 4A–4F, 5A–5L, 6A–6L, 7A–7H  
- **Evidence pointer** Figure legends not provided in the text  
- **Issue** The text references specific panels (e.g., "Figures 1A and 1B") but does not describe what is shown in each panel. This makes it difficult to follow the logic of the results.  
- **Required correction** Provide detailed figure legends that describe the experimental setup, the specific data shown in each panel, and the statistical analyses performed.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Statistical reporting  
- **Affected element** All quantitative results  
- **Evidence pointer** Figures 1–7; location not provided  
- **Issue** The text mentions statistical significance (e.g., "significant reduction") but does not report the statistical tests used, the number of independent experiments, or the p-values.  
- **Required correction** Include statistical details in the figure legends or methods, including the test used, sample size, and exact p-values or confidence intervals.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Interpretation of correlative data  
- **Affected element** P-body association (Figure 3J–3K, S3D)  
- **Evidence pointer** Figures 3J–3K, S3D; location not provided  
- **Issue** The close association of P-bodies with TNS1 condensates is noted, but the functional significance is not explored. The authors state this is "beyond the scope of this study," which is acceptable, but the observation raises questions about whether TNS1 condensates have RNA-related functions.  
- **Required correction** Briefly discuss the potential implications of P-body association in the Discussion, even if functional studies are not performed.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Terminology consistency  
- **Affected element** "Condensates" vs. "aggregates"  
- **Evidence pointer** Throughout the text  
- **Issue** The authors use "condensates" throughout, but the distinction between phase-separated condensates and other types of aggregates is not always clear.  
- **Required correction** Define the criteria used to classify TNS1 structures as condensates and discuss any alternative interpretations.

- **Concern ID** R1-m5  
- **Severity** Minor  
- **Axis** Missing controls  
- **Affected element** Inhibitor experiments (Figures 2G–2H, 6E–6F)  
- **Evidence pointer** Figures 2G–2H, 6E–6F; location not provided  
- **Issue** The inhibitor experiments would benefit from controls showing that the inhibitors do not affect TNS1 expression levels or cell viability.  
- **Required correction** Include appropriate controls for inhibitor treatments, such as Western blots for TNS1 levels and cell viability assays.

## Risk / unsupported claims
- The claim that TNS1 undergoes phase separation is not fully supported without in vitro reconstitution data or evidence for key phase separation criteria (e.g., saturation concentration, reversibility).
- The claim that TNS1 condensates act as selective reservoirs for inactive adhesion proteins is based on colocalization and BioID data that are not fully presented; the selectivity and functional significance require stronger evidence.
- The claim that IDR deletion increases FA dynamics, migration, and invasion is correlative; the causal link to loss of condensation is not established.
- The claim that phosphorylation by p38, ERK, and AKT regulates condensation is based on pharmacological inhibition and phosphoproteomics, but direct kinase-substrate relationships are not demonstrated.
- The functional significance of P-body association with TNS1 condensates is noted but not explored; any implied function is unsupported.