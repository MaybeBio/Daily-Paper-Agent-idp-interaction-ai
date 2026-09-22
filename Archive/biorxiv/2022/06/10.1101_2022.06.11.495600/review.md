## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, experimental section) as provided
- **Assessment boundary** Scientific validity, technical soundness, and support of claims based solely on the supplied text; no external data or supplementary materials were available for verification
- **Shared manuscript claim summary** The authors introduce biofunctional nanodot arrays (bNDAs) fabricated by capillary nanostamping to spatially control receptor clustering in the plasma membrane of live cells. Using Wnt signaling as a model, they report that nanoscale clustering of Lrp6 recruits Frizzled-8, Axin-1, and Dishevelled-2 in a ligand-independent, density-dependent manner, and propose that liquid-liquid phase separation drives cooperative assembly of "Wnt signalodroplets" that activate downstream β-catenin signaling.
- **Visible evidence base** Abstract; Introduction; Results sections (four subsections); Discussion; Experimental Section (materials, protein expression, surface modification, detection methods, microscopy, FRAP, dSTORM, single-molecule tracking, image evaluation, statistics); figure legends referenced but figures not visible; supplementary figure/video/table titles listed but content not provided
- **Missing materials affecting confidence** All figures and supplementary figures, videos, tables, and raw data; detailed protocols for capillary nanostamping parameters; validation data for the GFP-clamp construct; control experiments (e.g., negative controls for clustering specificity); statistical details for key comparisons; information on replicate numbers for most experiments

## Reviewer
- **Overall assessment** This manuscript presents a technically ambitious approach to interrogate nanoscale receptor clustering and its role in Wnt signaling. The bNDA platform is potentially valuable, and the observation of ligand-independent, density-dependent recruitment of Wnt pathway components is intriguing. However, the evidence as presented is incomplete: key quantitative data, control experiments, and mechanistic validations are referenced but not visible in the supplied material. The claim of LLPS-driven assembly is plausible but not fully established from the provided text alone. The manuscript would benefit from clearer presentation of quantitative analyses and additional controls to rule out alternative explanations.
- **Who would be interested in the results, and why** Researchers in cell signaling, membrane biophysics, and nanobiotechnology would find this work relevant. Those studying Wnt signaling specifically would be interested in the proposed co-condensation mechanism. Developers of nanopatterning and surface functionalization methods would value the technical advance. The work bridges biophysical approaches with cell biology, appealing to interdisciplinary groups interested in phase separation in living cells.
- **Major strengths** 1. The bNDA technology is a creative and potentially powerful tool for controlling receptor organization at the nanoscale, addressing a genuine experimental gap. 2. The combination of super-resolution imaging, FRAP, and single-molecule tracking provides a multi-pronged approach to study dynamics. 3. The use of knockout cell lines and domain-deletion constructs (Lrp6ΔICD) strengthens the mechanistic argument. 4. The observation of biphasic density-dependent recruitment is a notable finding that could have broad implications.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative evidence for LLPS not fully visible), R1-M2 (specificity of GFP-clamp capture not fully validated), R1-M3 (control for artificial membrane tethering not fully described), R1-M4 (statistical rigor and replicate reporting incomplete)
- **Assessment against Nature-style criteria**  
  *Originality*: The bNDA approach is novel and distinct from existing micropatterning and nanopatterning methods. The application to Wnt signalosome assembly is a fresh angle. However, the concept of receptor clustering-induced signaling is not entirely new, and the LLPS hypothesis for Wnt signaling has been proposed elsewhere. The originality lies mainly in the technical platform.  
  *Scientific importance*: If fully validated, the findings could reshape understanding of Wnt signal initiation and more broadly, how membrane receptor clustering drives signaling. The potential to control signaling platforms with nanoscale precision has wide applicability. However, the current evidence does not yet fully establish the mechanistic claims.  
  *Interdisciplinary readership*: The work spans surface chemistry, biophysics, and cell signaling, making it potentially attractive to a broad audience. The technical detail may be dense for non-specialists, but the conceptual framing around phase separation is accessible.  
  *Technical soundness*: The methods are sophisticated and generally well-described, but key validations and controls are not visible in the supplied material. The reliance on overexpression systems and the lack of quantitative rigor in some analyses weaken the technical case.  
  *Readability for nonspecialists*: The abstract and introduction are clear, but the results section assumes significant background knowledge. The manuscript would benefit from more explicit explanations of the significance of each finding for a general audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea and platform are promising, but the current evidence base is insufficient to fully establish the claims of LLPS-driven cooperative assembly and functional signaling. The authors should provide complete quantitative data, additional controls, and clearer statistical reporting.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency for LLPS claim
- **Claim pointer** The manuscript claims that Wnt signalosome assembly is driven by "highly cooperative liquid-liquid phase separation (LLPS)-driven assembly" and that "co-condensation of Axin and Dvl" is the underlying mechanism.
- **Evidence pointer** Results section "Effector protein dynamics supports LLPS-driven signalodot assembly"; Figures 5 and S4; Videos S1-S6
- **Concern** The claim of LLPS-driven assembly rests primarily on FRAP recovery dynamics and single-molecule tracking, but the quantitative data are not fully presented in the supplied text. The FRAP recovery of 34% for Axin1 within 200 s is mentioned, but no comparison to controls (e.g., membrane-bound proteins not expected to phase separate) or to theoretical expectations for LLPS is provided. The single-molecule tracking analysis is described as showing "heterogeneous diffusion," but the interpretation of this heterogeneity as evidence for LLPS is not rigorously justified. Additionally, the observation that artificial Axin1/Dvl2 co-condensates show different FRAP behavior than Lrp6-based signalodots is noted but not quantitatively compared or mechanistically explained. Without these quantitative details and appropriate controls, the LLPS claim is not fully supported.
- **Why it matters** LLPS is a specific biophysical mechanism with distinct predictions (e.g., concentration dependence, reversibility, exchange dynamics). If the evidence does not distinguish LLPS from other forms of clustering (e.g., stable protein-protein interactions or membrane-mediated aggregation), the central mechanistic claim of the paper is weakened.
- **Resolution test** Provide full FRAP recovery curves with fits, comparison to appropriate controls (e.g., non-phase-separating membrane proteins), quantitative analysis of single-molecule diffusion coefficients and their distribution, and demonstration of concentration-dependent behavior consistent with LLPS. Show that the observed dynamics are distinct from simple binding or aggregation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Specificity and efficiency of GFP-clamp capture
- **Claim pointer** The manuscript states that "efficient, high-density capturing of GFP-tagged proteins was achieved" using the tandem anti-GFP clamp, and that this enables "highly efficient and selective immobilization of transmembrane receptor."
- **Evidence pointer** Results section "Efficient reorganization of Lrp6 in the plasma membrane induces active Wnt signalosomes"; Figures 2 and S2; Experimental Section "Protein expression, purification and labeling"
- **Concern** The efficiency and specificity of the GFP-clamp-mediated capture are central to the validity of all subsequent experiments. However, the supplied text does not provide quantitative data on capture efficiency (e.g., fraction of Lrp6 molecules immobilized), specificity (e.g., lack of capture of non-GFP-tagged proteins), or the stability of the interaction over the experimental time course. The claim of "high contrast" is mentioned, but the actual contrast values and their variability are not reported. Additionally, the potential for the GFP-clamp to induce dimerization of Lrp6 independent of the bNDA pattern is not addressed, which could confound the interpretation of density-dependent effects.
- **Why it matters** If the capture is inefficient or non-specific, the observed recruitment of Fzd8, Axin1, and Dvl2 could be an artifact of overexpression or non-physiological clustering. The quantitative interpretation of density-dependent effects relies on precise control of Lrp6 density, which requires validated capture efficiency.
- **Resolution test** Provide quantitative binding assays (e.g., surface plasmon resonance or fluorescence-based measurements) showing capture efficiency and specificity. Include control experiments with non-GFP-tagged receptors or with a non-functional GFP-clamp mutant. Demonstrate that the bNDA pattern is faithfully reproduced in the receptor distribution using super-resolution imaging.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Control for artificial membrane tethering
- **Claim pointer** The manuscript describes experiments where Axin1 is directly recruited to the plasma membrane via an artificial transmembrane linker (ALFAnb-TMD-GFPnb) and claims that this "does not trigger signalosome assembly" based on the absence of Fzd8 recruitment.
- **Evidence pointer** Results section "Axin1/Dvl2 nanodroplets at the membrane do not trigger signalosome assembly"; Figure 6; Figures S5 and S6
- **Concern** The conclusion that artificial Axin1 recruitment does not trigger signalosome assembly is critical for the model that Lrp6 clustering is the initiating event. However, the supplied text does not provide quantitative data on the density of Axin1 achieved by this artificial tethering, nor does it compare this density to that achieved in the Lrp6 bNDA experiments. If the artificial tethering results in much lower Axin1 density, the negative result could be due to insufficient concentration rather than a fundamental difference in mechanism. Additionally, the observation that Lrp6 is recruited to Axin1 bNDAs is mentioned but not quantified, and the functional consequences (β-catenin activation) are stated to be "impeded" without providing the data.
- **Why it matters** The distinction between Lrp6-initiated and Axin1-initiated assembly is central to the proposed mechanism. If the artificial tethering experiment is not properly controlled, the conclusion that Lrp6 clustering is uniquely capable of initiating signalosome assembly is not established.
- **Resolution test** Quantify the density of artificially tethered Axin1 and compare it to the density of Lrp6 in the bNDA experiments. Provide dose-response experiments where Axin1 density is varied to show that even high densities do not recruit Fzd8. Include quantitative β-catenin data for these experiments.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor and replicate reporting
- **Claim pointer** The manuscript reports various quantitative measurements (e.g., β-catenin levels, FRAP recovery, contrast values) and states statistical significance in some cases, but the statistical methods and replicate numbers are not consistently reported.
- **Evidence pointer** Experimental Section "Statistical Analysis"; various results subsections
- **Concern** The statistical analysis section states that Student's t-test was used and significance was defined, but the number of independent experiments, the number of cells analyzed, and the variability (e.g., standard deviation or confidence intervals) are not consistently reported for each measurement. For example, the β-catenin quantification mentions n > 15 cells, but it is unclear if these are from a single experiment or multiple independent replicates. The FRAP analysis mentions n ≥ 25, but the number of independent experiments is not stated. This lack of detail makes it difficult to assess the robustness of the findings.
- **Why it matters** Reproducibility and statistical rigor are essential for establishing the validity of the claims, especially for quantitative comparisons (e.g., β-catenin levels between conditions, FRAP recovery differences).
- **Resolution test** Provide a detailed statistical analysis plan, including the number of independent experiments, the number of cells or regions analyzed per experiment, and the appropriate statistical tests for each comparison. Report effect sizes and confidence intervals where relevant.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** "Wnt signalodroplets" and "Wnt signalodots"
- **Evidence pointer** Abstract; Results; Discussion
- **Issue** The manuscript introduces two terms, "signalodroplets" and "signalodots," which appear to be used interchangeably. This could confuse readers.
- **Required correction** Define both terms clearly at first use and use them consistently, or consolidate to a single term.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of figure legends
- **Affected element** All figures
- **Evidence pointer** Figure legends referenced in text but not visible
- **Issue** The figure legends are not provided in the supplied material, making it impossible to assess the data presentation and statistical annotations.
- **Required correction** Ensure that all figure legends are complete, including descriptions of all panels, statistical annotations, and definitions of error bars.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Discussion of alternative mechanisms
- **Affected element** Discussion section
- **Evidence pointer** Discussion
- **Issue** The discussion focuses heavily on the LLPS interpretation but does not thoroughly consider alternative explanations for the observed cooperative recruitment, such as receptor oligomerization driven by specific protein-protein interactions or membrane-mediated effects.
- **Required correction** Add a paragraph discussing alternative models and how the data distinguish between them.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical detail on capillary nanostamping
- **Affected element** Experimental Section "Capillary nanostamping"
- **Evidence pointer** Experimental Section
- **Issue** The description of the capillary nanostamping procedure is brief, and key parameters (e.g., stamp porosity, contact time, pressure) are not specified, which may hinder reproducibility.
- **Required correction** Provide more detailed parameters or reference a prior publication with full details.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarification of "co-condensation" terminology
- **Affected element** Abstract; Results; Discussion
- **Evidence pointer** Abstract; Results; Discussion
- **Issue** The term "co-condensation" is used to describe the recruitment of Fzd8, Axin1, and Dvl2 to Lrp6 clusters. It is unclear whether this implies a specific phase separation process or simply co-localization.
- **Required correction** Clarify the operational definition of "co-condensation" and specify what evidence supports this interpretation versus simple co-clustering.

## Risk / unsupported claims
- The claim that bNDA-mediated Lrp6 clustering "induces active Wnt signalosomes" is not fully supported without visible β-catenin quantification data and appropriate controls (e.g., cells without Fzd8 co-expression).
- The claim that "highly cooperative" assembly occurs is based on the biphasic density dependence, but the cooperativity is not quantified (e.g., Hill coefficient) and the underlying mechanism is not established.
- The statement that "two types of LLPS for Axin1 and Dvl2 co-exist within the co-condensates" is speculative and not directly supported by the data presented.
- The claim that capillary nanostamping is "very suitable for cell biological applications" is an assertion without comparative data against other nanopatterning methods.
- The physiological relevance of the findings is unclear, as all experiments appear to rely on overexpression of tagged proteins; no evidence is provided that endogenous proteins behave similarly.