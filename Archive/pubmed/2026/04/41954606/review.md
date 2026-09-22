## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, conclusions, and materials and methods
- **Assessment boundary** Scientific content, methodological soundness, interpretation of results, and support of claims by presented evidence
- **Shared manuscript claim summary** The authors propose that the intrinsically disordered C-terminal tail of Hsp90 is not a passive tether but an active structural element that modulates the conformational ensemble of the folded CTD, with distinct behavior in isolated CTD versus full-length protein, and that cochaperone binding or cellular environments shift these conformations toward a compact state
- **Visible evidence base** DEER distance measurements, CW-EPR spectra, NMR HSQC chemical shift perturbations, SPR binding data, MST measurements, nanoDSF thermal stability data, AlphaFold predictions, pull-down mass spectrometry
- **Missing materials affecting confidence** Supplementary figures and tables referenced but not provided (Figures S1-S18, Tables S1-S8), raw DEER time traces, full NMR assignment details, AlphaFold confidence metrics beyond pLDDT, pull-down mass spectrometry raw data and statistical analysis details

## Reviewer
- **Overall assessment** This manuscript addresses a genuinely under-explored question in the Hsp90 field, namely whether the disordered C-terminal tail has structural and regulatory functions beyond serving as a passive docking site for TPR cochaperones. The combination of site-directed spin labeling with DEER, CW-EPR, NMR, and biophysical binding assays is methodologically ambitious and appropriate for the question posed. The central observation, that the tail adopts different conformational ensembles in isolated CTD versus full-length Hsp90 and that Cpr6 binding or cellular environments collapse these differences, is potentially interesting. However, several concerns limit the strength of the conclusions as currently presented. The interpretation of DEER data relies heavily on distance distributions that are not shown in the main text, the quantitative link between the observed conformational changes and functional relevance remains speculative, and the pull-down experiments, which are used to support claims about endogenous TPR partner engagement, are presented with insufficient statistical detail. The manuscript would benefit from clearer presentation of the raw data and a more cautious framing of the functional implications.

- **Who would be interested in the results, and why** Researchers studying Hsp90 structure and function, particularly those interested in chaperone cochaperone interactions and the role of intrinsically disordered regions in protein function. The work may also appeal to the EPR/DEER spectroscopy community as an example of applying these techniques to disordered protein regions in complex environments. The findings could be relevant to those studying TPR domain-containing proteins and their recognition of disordered C-terminal motifs more broadly.

- **Major strengths** The study addresses a question of genuine importance that has been largely overlooked, namely whether the disordered CTD tail of Hsp90 has structural roles beyond cochaperone recruitment. The methodological approach is sophisticated, combining multiple complementary biophysical techniques. The comparison between isolated CTD and full-length protein is well conceived and provides insight into context-dependent behavior of the tail. The inclusion of cellular and cell extract conditions is a valuable step toward physiological relevance. The observation that Cpr6 binding and cellular environments converge on a similar compact conformational state is intriguing and potentially significant.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The authors claim that the CTD tail in IsoC stabilizes an additional CTD conformation near the dimer interface that is absent in FL and lost upon tail truncation, and that this population is reduced upon Cpr6 binding
  - **Evidence pointer** Results section, DEER distance measurements; Figures 1-3 (main text); Figures S4, S6, S9, S10 (supplementary, not provided)
  - **Concern** The central structural claims rest on DEER distance distributions that are not shown in the main text. The authors state that IsoC637-Gd exhibits two distance populations (3.4 nm and 4.9 nm) while FL637-Gd shows a single peak at 3.6 nm, but the actual distance distributions are not presented in any main-text figure. The reader cannot evaluate the quality of the DEER data, the reliability of the Tikhonov regularization, or the separation of the two populations. Furthermore, the claim that Cpr6 binding selectively reduces the longer-distance component is based on global fitting with fixed parameters, but the quality of these fits is not demonstrated.
  - **Why it matters** The entire thesis of the paper, that the tail actively modulates CTD conformation, depends on the identification and quantification of these distinct conformational populations. Without direct visualization of the distance distributions and the fitting quality, the central claim cannot be adequately assessed. The distinction between a genuine two-population system versus a broadened single distribution is critical and requires careful examination of the raw data.
  - **Resolution test** Show the raw DEER time traces and the resulting distance distributions for all key constructs (IsoC637, FL637, IsoCΔ, FLΔ) in the main text or a clearly referenced supplementary figure. Provide quantitative measures of fit quality, such as RMSD values between experimental and fitted traces, and demonstrate that the two-population model is statistically justified over a one-population model for IsoC637. Show the evolution of the distance distributions with increasing Cpr6 concentration.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Interpretation and functional relevance
  - **Claim pointer** The authors conclude that the CTD tail is an active structural element that modulates CTD architecture and highlight its potential functional relevance in the Hsp90 chaperone cycle
  - **Evidence pointer** Conclusions section; Results sections on DEER, CW-EPR, and cellular experiments
  - **Concern** The leap from in vitro conformational observations to claims about functional relevance in the chaperone cycle is not adequately supported. The authors show that Cpr6 binding and cellular environments shift IsoC toward a compact conformation similar to FL, but no functional readout is provided. The relevance of the tail-mediated conformational heterogeneity to Hsp90 function, such as client activation, ATPase activity, or cochaperone exchange, is not demonstrated. The title and abstract imply a functional significance that the data do not directly establish.
  - **Why it matters** The broader significance of the work, and its appeal to a wide readership, depends on the functional implications. Without a functional link, the observations remain structural characterizations of a purified system. The authors themselves acknowledge that the functional relevance is speculative, but the framing of the abstract and conclusions overstates the case.
  - **Resolution test** Either temper the functional claims to match the structural evidence, or provide a direct functional readout, such as ATPase activity measurements, client binding assays, or chaperone activity assays comparing full-length, tail-truncated, and Cpr6-bound forms. Alternatively, provide a more explicit and testable model for how the observed conformational modulation could influence the chaperone cycle, with clear predictions that could be tested in future work.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Quantitative rigor of binding analysis
  - **Claim pointer** The authors use DEER-derived population shifts to estimate binding affinities of Cpr6 for two CTD conformations, yielding Kd,a = 158 ± 32 μM and Kd,b = 528 ± 105 μM, and derive thermodynamic parameters from the temperature dependence of these values
  - **Evidence pointer** Results section, DEER distance measurements; Figure 3D; Figure S15 (supplementary, not provided)
  - **Concern** The extraction of binding constants from DEER population shifts at a single freezing temperature, followed by extrapolation to room temperature using a van't Hoff analysis, involves substantial assumptions that are not fully justified. The authors acknowledge the discrepancy with SPR-derived Kd values but attribute it to temperature differences. However, the uncertainty in the freezing temperature, the assumption of a linear van't Hoff regime over a wide temperature range, and the propagation of errors through this multi-step analysis are not addressed. The derived thermodynamic parameters should be presented with appropriate caveats or omitted.
  - **Why it matters** The thermodynamic analysis adds a layer of quantitative interpretation that goes beyond the primary structural findings. If these values are not robust, they could mislead readers and detract from the more solid conformational observations. The discrepancy with SPR values, while explained, raises questions about the validity of the DEER-derived approach.
  - **Resolution test** Either remove the thermodynamic analysis and the DEER-derived Kd values, or provide a more rigorous treatment that includes a systematic analysis of uncertainties, validation of the van't Hoff assumption, and a clearer discussion of the limitations. If the values are retained, they should be clearly labeled as rough estimates with substantial uncertainty.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Evidence for endogenous partner engagement
  - **Claim pointer** The authors claim that pull-down experiments followed by mass spectrometry demonstrate that IsoC687-Gd retains the ability to engage TPR-domain proteins in HeLa cell extracts, and that this engagement provides a molecular basis for the conformational compaction observed in cells
  - **Evidence pointer** Results section, cellular experiments; Tables S5-S8 (supplementary, not provided); Figure S18 (supplementary, not provided)
  - **Concern** The pull-down experiments are described with insufficient detail to evaluate their validity. The authors state that enrichment levels were generally modest and that a class-level analysis was performed, but the criteria for defining specific interactors, the statistical thresholds, and the reproducibility between the two experiments are not clearly presented. The claim that five TPR cochaperones were reproducibly recovered above background is not supported by the data shown in the main text. The connection between the pull-down results and the DEOR observations in cells is correlative rather than causal.
  - **Why it matters** The cellular experiments are important for establishing physiological relevance. If the pull-down evidence is weak, the claim that endogenous TPR partners reproduce the effects of Cpr6 binding is not well supported. The modest enrichment levels could reflect non-specific binding or background contamination.
  - **Resolution test** Provide the full results of the pull-down experiments, including the list of identified proteins, their enrichment values, statistical significance, and the criteria for defining specific interactors. Show the class-level analysis with appropriate statistical tests. If the evidence is not robust, temper the claims about endogenous partner engagement and present the cellular DEER results as consistent with, but not proof of, TPR-mediated effects.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of presentation
  - **Affected element** Figure 1 and associated text
  - **Evidence pointer** Results section, first paragraph
  - **Issue** The description of the spin labeling positions and the schematic in Figure 1 is difficult to follow without seeing the figure. The relationship between the labeling positions (D560C, K627C, K637C, A687C, A701C) and the domain structure of Hsp90 is not clearly described in the text.
  - **Required correction** Provide a clearer verbal description of where each labeling position is located relative to domain boundaries and secondary structure elements. Ensure the figure legend is self-contained and explains the domain organization.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Methodological detail
  - **Affected element** CW-EPR analysis
  - **Evidence pointer** Materials and Methods, EPR Measurements and Data Analysis
  - **Issue** The CW-EPR spectra are described as being simulated with SimLabel, but the parameters used for the simulations, the criteria for good fits, and the quantitative measures of the mobile versus restricted components are not provided.
  - **Required correction** Provide the simulation parameters, the fitting criteria, and the quantitative fractions of mobile and restricted components for each condition. This would strengthen the claims about Cpr6-induced restriction of tail mobility.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** SPR and MST measurements
  - **Evidence pointer** Materials and Methods, SPR and MST sections
  - **Issue** The number of replicates, the error bars, and the statistical treatment of the SPR and MST data are not described. The Kd values are presented without confidence intervals.
  - **Required correction** Report the number of independent measurements, the standard errors or confidence intervals for all Kd values, and the statistical tests used to compare conditions.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Interpretation of AlphaFold predictions
  - **Affected element** Results section, DEER distance measurements
  - **Evidence pointer** Figure S6 (supplementary, not provided)
  - **Issue** The AlphaFold predictions are used to support the experimental DEER data, but the limitations of AlphaFold for disordered regions are only briefly acknowledged. The authors state that AlphaFold does not explicitly model conformational ensembles, yet they use the predictions to interpret their distance distributions.
  - **Required correction** Provide a more nuanced discussion of what AlphaFold predictions can and cannot tell us about disordered regions, and clarify how the predictions are used in the interpretation. If the predictions are used primarily as a qualitative check, state this explicitly.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Completeness of methods
  - **Affected element** NMR measurements
  - **Evidence pointer** Materials and Methods, NMR Measurements
  - **Issue** The NMR experiments are described briefly, and the chemical shift perturbation analysis is mentioned in the results but the specific residues affected and the magnitude of the perturbations are not shown in the main text.
  - **Required correction** Provide a figure showing the chemical shift perturbations mapped onto the CTD structure or sequence, with the affected residues clearly identified. This would strengthen the claim of tail-CTD interactions.

- **Technical failings that need to be addressed before the case is established** The primary technical failing is the absence of the DEER distance distributions in the main text, which are essential for evaluating the central claims. The pull-down experiments lack sufficient statistical detail. The thermodynamic analysis from DEOR-derived populations requires more rigorous treatment or removal. The CW-EPR simulation parameters and fitting criteria are not provided.

- **Assessment against Nature-style criteria** 
  - Originality: The question of whether the disordered CTD tail of Hsp90 has structural functions beyond cochaperone recruitment is genuinely original and addresses a gap in the field. The application of DEER to this specific question in the context of full-length versus isolated domains is a novel approach.
  - Scientific importance: The findings have potential importance for understanding Hsp90 regulation and the general role of disordered regions in chaperone function. However, the functional significance is not directly demonstrated, which limits the current importance.
  - Interdisciplinary readership: The work bridges structural biology, biophysics, and chaperone biology. The methodological approach using multiple spectroscopic techniques could appeal to a broad readership, but the presentation is currently too specialized for non-experts in EPR spectroscopy.
  - Technical soundness: The combination of techniques is appropriate, but the presentation of key data is insufficient for full evaluation. The DEER analysis, in particular, requires more transparency.
  - Readability for nonspecialists: The manuscript is written in a style accessible to structural biologists and biochemists, but the heavy reliance on EPR methodology without adequate explanation of the approach may limit accessibility. The abstract is clear and appropriately framed.

- **Recommendation posture** Supportive if technical concerns are resolved. The core question is important and the methodological approach is sound, but the presentation of key data, particularly the DEER distance distributions, must be improved to establish the central claims. The functional implications should be either tempered or supported with additional data. The pull-down experiments require more rigorous statistical treatment. If these concerns are addressed, the manuscript could make a valuable contribution to the Hsp90 field.

## Risk / unsupported claims
- The claim that the CTD tail is an active structural element with functional relevance in the Hsp90 chaperone cycle is not directly supported by functional data and should be framed as a hypothesis
- The claim that endogenous TPR-domain proteins in cell extracts reproduce the effects of Cpr6 binding is correlative and not causally demonstrated
- The thermodynamic parameters derived from DEER population shifts at a single freezing temperature are based on assumptions that are not fully validated
- The claim that the proximal portion of the tail adopts a partially ordered conformation based on DEER peak width is suggestive but requires additional validation
- The statement that AlphaFold predictions reproduce the experimentally observed longer distance for IsoC versus FL is based on supplementary data not provided for evaluation