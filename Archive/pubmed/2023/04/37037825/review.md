## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and figure legends
- **Assessment boundary** Scientific content, technical soundness, logical coherence, and support of claims by presented evidence; not editorial or formatting issues
- **Shared manuscript claim summary** The intrinsically disordered carboxyl terminus (CT) of the β2 adrenergic receptor (β2AR) acts as an autoinhibitory domain, suppressing basal and agonist-stimulated Gs signaling through dynamic electrostatic interactions with positively charged residues on the cytoplasmic surface (primarily ICL2 and ICL3). Agonists and positive allosteric modulators weaken these interactions via distinct mechanisms, facilitating G protein access.
- **Visible evidence base** Cell-based cAMP assays (GloSensor), NanoBiT G protein dissociation assays, flow cytometry, single-molecule FRET (smFRET) on TIRF and confocal microscopes, solution NMR spectroscopy with segmental isotope labeling, paramagnetic relaxation enhancement (PRE), molecular dynamics simulations with adaptive sampling, and site-directed mutagenesis
- **Missing materials affecting confidence** Supplementary figures and tables referenced throughout (Supplementary Figs. 1–9, Supplementary Tables 1–4) were not provided; raw smFRET traces and statistical analysis details for FRET fitting are not fully described; MD simulation convergence and force field validation details are limited; NMR assignment completeness and quality metrics not shown

## Reviewer

- **Overall assessment** This manuscript presents a compelling and multi-faceted investigation into the autoinhibitory role of the intrinsically disordered CT of β2AR. The combination of cellular assays, single-molecule biophysics, NMR, and MD simulations provides a strong, convergent case for the proposed mechanism. The work addresses a significant gap in GPCR biology, as disordered regions have been largely overlooked in structural and functional studies. The evidence is generally well-aligned with the claims, though several technical details and control experiments require clarification to fully establish the mechanistic model.

- **Who would be interested in the results, and why** Researchers in GPCR biology, signal transduction, and membrane protein biophysics will find this work directly relevant. The demonstration that a disordered region can act as an autoinhibitory module with allosteric regulation expands the conceptual framework for GPCR signaling. The methodological integration of smFRET, NMR, and MD provides a template for studying disordered regions in other membrane proteins. Additionally, those interested in intrinsically disordered proteins and their functional roles in signaling complexes will find the findings of broad interest.

- **Major strengths**
  1. The study addresses a previously underappreciated aspect of GPCR biology: the functional role of intrinsically disordered regions, specifically the CT, in receptor regulation.
  2. The multi-technique approach (cellular assays, smFRET, NMR, PRE, MD) provides convergent evidence for the autoinhibitory mechanism, strengthening the overall conclusions.
  3. The identification of specific negatively charged residues in the CT and positively charged residues in ICL2/ICL3 as key interaction partners is well-supported by mutagenesis and MD data.
  4. The demonstration that different ligands (agonists, allosteric modulators) affect CT dynamics through distinct mechanisms adds mechanistic depth.
  5. The use of β-arrestin knockout cells and purified protein systems helps isolate the direct effects of the CT on Gs coupling.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency for mechanistic model
- **Claim pointer** The manuscript claims that the CT "directly inhibits basal and agonist-stimulated signaling" and that this occurs "via interacting with the positively charged cytoplasmic surface of the receptor."
- **Evidence point** Results sections "Autoinhibitory role of the C-terminus in Gs-coupled GPCRs" and "Using single molecule FRET to probe the dynamics of the β2AR C-terminus"; Figures 1 and 2
- **Concern** While the cellular assays show increased signaling upon CT truncation, the direct causal link between CT-cytoplasmic surface interactions and signaling inhibition is inferred rather than directly demonstrated. The smFRET experiments show conformational changes, but the assignment of the high-FRET state to a "CT engaged" conformation that blocks Gs access is not rigorously validated. Specifically, the authors do not show that disrupting the CT-core interaction (e.g., via charge-neutralizing mutations in the core) phenocopies the effects of CT truncation on Gs coupling in the same experimental system. The mutagenesis data (ED1, ED2, ED3) are presented in supplementary figures that were not available for review, limiting the ability to assess this key link.
- **Why it matters** The central claim of the paper is that CT-core interactions are mechanistically responsible for autoinhibition. Without direct evidence that disrupting these specific interactions (beyond truncation) enhances Gs coupling, the model remains correlative. The distinction between the CT simply being "in the way" versus actively engaging in regulatory interactions is important for the proposed allosteric mechanism.
- **Resolution test** Provide data showing that mutations in the cytoplasmic surface (e.g., neutralizing positive charges in ICL2/ICL3) that disrupt CT binding also enhance basal and agonist-stimulated Gs activity, phenocopying CT truncation. Alternatively, show that a peptide corresponding to the CT can inhibit Gs coupling in trans when added to CT-truncated receptors.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative rigor of smFRET analysis
- **Claim pointer** The manuscript claims that smFRET experiments reveal "transitions between low-FRET and high-FRET states" and that dwell times in these states are modulated by ligands and Gs.
- **Evidence point** Results section "Using single molecule FRET to probe the dynamics of the β2AR C-terminus"; Figure 2
- **Concern** The smFRET analysis relies on fitting FRET histograms with double Gaussian models and dwell time analysis with Hidden Markov Modeling. However, the manuscript does not provide sufficient detail on the number of molecules analyzed, the criteria for selecting traces, the statistical significance of differences in dwell times, or the reproducibility across independent protein preparations. The claim that the high-FRET state dwell time "plateaus at about 2 s" at high Gs concentrations is presented without confidence intervals or statistical comparison to other conditions. Additionally, the relationship between the FRET states and specific conformational ensembles is not quantitatively validated against the MD simulations.
- **Why it matters** The kinetic parameters derived from smFRET are central to the proposed model of CT dynamics and Gs competition. Without rigorous statistical treatment and clear reporting of the analysis pipeline, the quantitative claims are difficult to evaluate or reproduce.
- **Resolution test** Provide a detailed description of the smFRET data analysis, including the number of traces/molecules per condition, the criteria for trace selection, the method for determining FRET state populations and dwell times, and statistical tests comparing conditions. Ideally, include representative raw traces and show that the results are reproducible across at least three independent experiments.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** MD simulation validation and interpretation
- **Claim pointer** The manuscript claims that MD simulations reveal "the ensemble of CT conformations" and that "the CT tends to adopt non-extended conformations and stay near the receptor."
- **Evidence point** Results section "Localizing interactions between the CT and β2AR core domain"; Figures 6 and 7
- **Concern** The MD simulations are used to support the structural interpretation of the smFRET data, but the validation of the simulation protocol is limited. The adaptive sampling scheme is described, but there is no assessment of convergence, no comparison to experimental observables (e.g., predicted FRET efficiencies from simulations vs. measured values), and no discussion of force field limitations for disordered proteins. The claim that the simulations are representative of the "high-FRET state" is based on a single distance criterion (Cys148-Cys378), which may not capture the full conformational ensemble relevant to the FRET measurement.
- **Why it matters** The integration of MD with smFRET is a key strength of the paper, but only if the simulations are demonstrably reliable. If the simulations are not validated against the experimental data, the structural interpretation of the FRET states remains speculative.
- **Resolution test** Show that the MD simulations reproduce the experimentally measured FRET efficiency distributions (e.g., by computing predicted FRET from the simulations and comparing to the smFRET histograms). Provide convergence metrics for the adaptive sampling and discuss the sensitivity of the results to force field choices.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the autoinhibitory mechanism
- **Claim pointer** The manuscript claims that "the CT of several Gs-coupled GPCRs plays an autoinhibitory function in constitutive receptor activation" and that this is a general phenomenon.
- **Evidence point** Results section "Autoinhibitory role of the C-terminus in Gs-coupled GPCRs"; Supplementary Figure 1
- **Concern** The claim of generalizability is based on data from five receptors (β2AR, A2AR, D1R, D5R, 5-HT6R) presented in supplementary figures that were not available for review. The manuscript does not discuss the sequence diversity of these CTs or whether the proposed electrostatic mechanism (negatively charged CT interacting with positively charged core) is conserved across these receptors. Without this analysis, it is unclear whether the autoinhibitory function is a general property of Gs-coupled GPCR CTs or specific to certain receptors.
- **Why it matters** The title and abstract emphasize the β2AR, but the introduction and discussion suggest broader implications. If the mechanism is not general, the significance of the work is reduced; if it is general, the manuscript should provide supporting evidence.
- **Resolution test** Provide the supplementary data for all five receptors and include a sequence alignment or conservation analysis of the CT regions, highlighting the presence of negatively charged residues and their positional conservation. Discuss whether the proposed mechanism is likely to apply to other GPCR families.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure presentation
- **Affected element** Figure 1
- **Evidence point** Figure 1b–e
- **Issue** The concentration-response curves in Figure 1b and 1d appear to show very small error bars, and the text notes that "in many data points error bars are smaller than the size of symbols." This makes it difficult to visually assess the variability and the statistical separation between conditions.
- **Required correction** Consider using a different visualization (e.g., shaded confidence bands or larger symbols) or providing the data in a more readable format. Additionally, ensure that the statistical comparisons are clearly indicated on the figure.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Methods section, smFRET analysis
- **Evidence point** Methods section "Single-molecule FRET experiments on a total internal reflection fluorescence (TIRF) microscope"
- **Issue** The methods describe the data collection but do not provide sufficient detail on the data analysis pipeline, including the specific algorithms used for trace selection, background subtraction, and FRET efficiency calculation. The reference to "custom-made software" is vague.
- **Required correction** Provide a more detailed description of the analysis pipeline, including the specific steps for identifying single molecules, correcting for crosstalk and direct excitation, and generating FRET histograms. If the software is described elsewhere, provide a clear citation.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of NMR data
- **Affected element** Results section "Localizing interactions between the CT and β2AR core domain"; Figure 4
- **Issue** The NMR chemical shift perturbations are interpreted as evidence for CT-core interactions, but the manuscript does not discuss whether the observed changes are consistent with a specific binding interface or could arise from more global conformational changes. The intensity ratio analysis is also not fully explained.
- **Required correction** Clarify the interpretation of the chemical shift perturbations and intensity ratios. Discuss whether the observed changes are localized to specific residues or distributed across the CT, and what this implies for the interaction interface.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Issue** The discussion does not address potential limitations of the study, such as the use of detergents for purified protein experiments, the potential effects of the mutations introduced for labeling, or the timescale limitations of the MD simulations.
- **Required correction** Add a brief paragraph acknowledging these limitations and discussing how they might affect the interpretation of the results.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure legends and results text
- **Evidence point** Figures 1–3 and associated text
- **Issue** The manuscript reports statistical significance in several places but does not consistently provide the statistical test used, the number of replicates, or the exact p-values. For example, in Figure 1c and 1e, the text mentions "one-way ANOVA with the Tukey multiple comparison test" but does not report the F-statistic or degrees of freedom.
- **Required correction** Ensure that all statistical analyses are fully described, including the test used, the number of replicates, and the exact p-values or confidence intervals.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Direct evidence linking CT-core interactions to functional inhibition is incomplete; mutagenesis data in supplementary figures are essential and must be provided.
  - R1-M2: Quantitative rigor of smFRET analysis is insufficiently documented; full details of trace selection, fitting, and statistical comparison are required.
  - R1-M3: MD simulations lack validation against experimental observables and convergence assessment.

- **Assessment against Nature-style criteria**
  - **Originality** High. The concept of an intrinsically disordered CT acting as an autoinhibitory domain in a GPCR is novel and challenges the traditional view of GPCR regulation being mediated primarily by ordered cytoplasmic loops and helix 8.
  - **Scientific importance** High. If the proposed mechanism is generalizable, it has implications for understanding GPCR signaling, biased agonism, and the design of allosteric modulators targeting disordered regions.
  - **Interdisciplinary readership** Moderate to high. The work bridges GPCR biology, biophysics, and computational chemistry, and should appeal to researchers in these fields. The broader cell signaling community may also find the autoinhibitory concept of interest.
  - **Technical soundness** Generally strong, but with gaps in the quantitative analysis of smFRET data and validation of MD simulations. The cellular assays and NMR experiments appear well-executed, but the key mechanistic claims require additional supporting data.
  - **Readability for nonspecialists** Good. The manuscript is clearly written and the figures are well-designed. The abstract and introduction effectively convey the significance of the work. Some of the methods sections are dense but appropriate for a specialist audience.

- **Recommendation posture** Supportive if technical concerns are resolved. The core finding is novel and potentially significant, but the manuscript requires additional data and analysis to fully establish the mechanistic model. Specifically, the authors must provide the supplementary data on mutagenesis, strengthen the quantitative analysis of smFRET, and validate the MD simulations against experimental observables.

## Risk / unsupported claims
- The claim that the CT of "several Gs-coupled GPCRs" plays an autoinhibitory role is not fully supported by the available evidence, as the data for receptors other than β2AR are only in supplementary figures not provided for review.
- The claim that the CT "directly inhibits" Gs signaling implies a direct physical competition, but the data are also consistent with an allosteric mechanism where CT binding stabilizes an inactive conformation without directly blocking the Gs binding site.
- The statement that "the CT exists primarily in one major conformation or two or more conformations that exchange on a much faster time scale than we can measure" is speculative and not directly tested.
- The physiological relevance of the autoinhibitory mechanism is discussed only speculatively; no experiments are presented to test the role of the CT in a cellular or organismal context beyond the overexpression systems used.