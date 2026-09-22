## Review setup
- **Input scope** Full manuscript text (Introduction, Materials and methods, Results, Discussion, Conclusions) without supplementary files
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and internal consistency based solely on the provided text
- **Shared manuscript claim summary** The authors report identification of a 9aaTAD activation domain in c-Myc and N-Myc, demonstrate its transcriptional activation function in yeast hybrid assays, and measure binding affinity to the KIX domain of CBP using bio-layer interferometry, reporting micromolar to sub-micromolar Kd values. They also propose a new "acetyl-TAD" region (69–103) with co-activation function.
- **Visible evidence base** Results sections describing conservation analysis, transactivation assays, BLI binding measurements, and western blot data; Methods sections for construct generation, peptide synthesis, protein expression, BLI, and β-galactosidase assays
- **Missing materials affecting confidence** Supplementary figures (S1), Additional files 1 and 2, raw BLI sensorgrams, full western blot images, statistical analysis details, peptide sequences for all constructs, and the prediction algorithm output details

## Reviewer
- **Overall assessment** The manuscript addresses a relevant question in Myc biology, namely the interaction between the Myc activation domain and the KIX domain of CBP. The topic is of interest to the transcription and cancer biology communities. However, the manuscript has substantial issues with internal consistency, data presentation, and interpretation. The title claims "superior high affinity" but the reported Kd values are in the micromolar range, which is not typically considered high affinity. The text contains contradictory statements about the scale of the interaction (nano-molar in the Introduction and Conclusions versus micromolar in the Results). The transactivation data are presented with insufficient statistical detail, and the proposed "acetyl-TAD" concept is speculative without direct experimental evidence. The negative control experiment with Sp1 is a good addition but does not fully address the specificity of the Myc-KIX interaction. Overall, the case for a functionally significant, high-affinity interaction is not established from the provided evidence.

- **Who would be interested in the results, and why** Researchers studying Myc oncoprotein function, transcriptional activation mechanisms, and the role of CBP/p300 coactivators in gene regulation. The potential druggability of the Myc-KIX interface could interest drug discovery groups focused on Myc-driven cancers. The 9aaTAD prediction methodology may interest bioinformaticians working on activation domain prediction.

- **Major strengths** The study addresses a clinically relevant target (Myc) and explores a specific protein-protein interaction that could have therapeutic implications. The use of multiple approaches (transactivation assays, BLI, conservation analysis) is commendable. The inclusion of a negative control (Sp1) strengthens the binding specificity argument. The evolutionary analysis of 9aaTAD conservation across Myc family members provides useful context.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data interpretation and internal consistency
- **Claim pointer** The manuscript claims "a strong interaction at nano-molar scale" (Introduction and Conclusions) but the Results section reports "equilibrium dissociation constant (Kd) values in the micromolar to sub-micromolar range" with c-Myc Kd(apparent) = 2.16 ± 1.17 μM and N-Myc Kd(apparent) = 0.88 ± 0.11 μM.
- **Evidence pointer** Introduction, Results section "The KIX domain interactions with c-Myc and N-Myc", Conclusions
- **Concern** The manuscript contains a direct contradiction regarding the affinity scale. The Introduction and Conclusions state "nano-molar scale" while the Results report micromolar values. A Kd of 2.16 μM is not nanomolar. This discrepancy is fundamental to the central claim of the paper and the title's assertion of "superior high affinity." The title itself is misleading given the reported values.
- **Why it matters** The central claim of the paper is the affinity of the Myc-KIX interaction. If the authors cannot consistently report the magnitude of this interaction, the reader cannot assess the significance of the finding. The title's claim of "superior high affinity" is not supported by micromolar Kd values, which are typically considered moderate affinity in protein-protein interactions.
- **Resolution test** The authors must correct the inconsistency and either revise the title and claims to match the micromolar values or provide additional data demonstrating nanomolar affinity. The title should accurately reflect the reported data.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental design and data interpretation
- **Claim pointer** The manuscript proposes a new "acetyl-TAD" region (69–103) with co-activation function based on transactivation assays comparing constructs with and without the 9aaTAD.
- **Evidence pointer** Results section "Activation of c-Myc transcription is linked with the 9aaTAD", Discussion
- **Concern** The transactivation data are presented as a single figure panel (Fig. 1b) with minimal statistical detail. The text states "we observed significant activation function independent of 9aaTAD in constructs with the region 69–103, although 3- and fivefold less, respectively" but no statistical analysis is described. The claim of a new "acetyl-TAD" domain is based on indirect evidence from deletion constructs and is not supported by direct experiments testing acetylation. The name "acetyl-TAD" implies a functional role for acetylation that is not experimentally addressed.
- **Why it matters** The proposal of a new functional domain requires robust experimental evidence. The current data do not distinguish between a specific co-activation function of region 69–103 and non-specific effects of protein truncation or stability. The acetylation implication in the name is not tested.
- **Resolution test** Provide statistical analysis of transactivation data, include protein expression controls for all constructs, and either provide direct evidence for acetylation-dependent function or rename the region without the acetylation implication.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of binding assay
- **Claim pointer** The BLI experiments report Kd(apparent) values for Myc peptides binding to KIX, with the claim that "both Myc peptides displayed strong binding to the KIX comparable to MLL peptide."
- **Evidence pointer** Results section "The KIX domain interactions with c-Myc and N-Myc", Methods section "Bio-layer interferometry"
- **Concern** The BLI methodology has several issues. First, the peptides are immobilized on streptavidin biosensors via biotin, which may affect the accessibility of the binding interface. Second, the Kd(apparent) values have large errors (c-Myc: 2.16 ± 1.17 μM, nearly 54% error), raising questions about the reliability of the measurements. Third, the assay was performed at pH 6.0, which may not reflect physiological conditions. Fourth, the manuscript does not report whether the binding is specific to the KIX domain or could be due to non-specific interactions with the biosensor surface. The negative control (Sp1) is helpful but only tested in the 3–16 μM range, and the Kd for Sp1-Ac (9.77 ± 1.57 μM) is only about 4-5 fold weaker than c-Myc, which may not be a convincing separation.
- **Why it matters** The binding affinity is the central quantitative claim of the paper. If the assay methodology has artifacts or the errors are too large, the reported Kd values cannot be considered reliable. The modest difference between the positive (Myc) and negative (Sp1-Ac) controls weakens the specificity argument.
- **Resolution test** Provide detailed BLI methodology including immobilization levels, regeneration validation, and demonstrate specificity through competition experiments or mutagenesis. Report confidence intervals and assess whether the assay can reliably distinguish between the reported Kd values.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Missing data and reproducibility
- **Claim pointer** The manuscript references Supplementary Figure S1 for western blot data showing protein expression levels of the constructs, and states that longer constructs (1–103 and 1–108) were "below our immuno-detection threshold."
- **Evidence pointer** Results section "Activation of c-Myc transcription is linked with the 9aaTAD", Methods section "Western blot analysis"
- **Concern** The western blot data are critical for interpreting the transactivation results. If the longer constructs are not detectable by western blot, it is unclear whether the reduced transactivation activity of these constructs is due to the absence of the 9aaTAD or due to lower protein expression. The manuscript mentions this observation but does not adequately address its implications for the interpretation of the transactivation data. The supplementary figure is not available for review.
- **Why it matters** Without proper expression controls, the transactivation data cannot be interpreted. If the constructs without 9aaTAD are expressed at lower levels, the reduced activity may be an artifact of protein abundance rather than a functional effect of the 9aaTAD.
- **Resolution test** Provide the supplementary figure and a clear discussion of how the differential expression affects the interpretation. Ideally, normalize transactivation activity to protein expression levels or use a different assay system where expression can be controlled.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Evolutionary analysis interpretation
- **Claim pointer** The manuscript claims that the absence of 9aaTAD in L-Myc paralogs in higher metazoans "suggests that the loss of 9aaTAD in L-Myc paralogs has occurred already in early tetrapod evolution and furthermore underpins the 9aaTAD activation function."
- **Evidence pointer** Results section "The 9aaTAD is well conserved in evolution of the MYC family", Figures 1 and 2
- **Concern** The evolutionary argument is presented as supporting evidence for the functional importance of 9aaTAD, but the logic is not fully developed. The loss of a domain in one paralog does not necessarily underpin its activation function in other paralogs. The manuscript does not discuss whether L-Myc has alternative activation mechanisms that compensate for the loss of 9aaTAD. The alignment figures are not available for detailed review.
- **Why it matters** The evolutionary analysis is used to support the functional significance of 9aaTAD. If the argument is not rigorous, it weakens the overall case for the domain's importance.
- **Resolution test** Provide a more detailed evolutionary analysis, including discussion of compensatory mechanisms in L-Myc and statistical support for the conservation pattern.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and terminology
- **Affected element** Title and abstract claims
- **Evidence pointer** Title, Abstract (not provided), Conclusions
- **Issue** The term "superior high affinity" in the title is not defined or justified. The reported Kd values (micromolar range) are not typically described as "high affinity" in the protein-protein interaction literature.
- **Required correction** Revise the title to accurately reflect the reported affinity range, or provide a clear definition of what constitutes "superior high affinity" in this context.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Transactivation assay data
- **Evidence pointer** Results section "Activation of c-Myc transcription is linked with the 9aaTAD", Figure 1b
- **Issue** The transactivation data are presented as means with standard deviation from two independent transformants (n = 2), which is a very small sample size. No statistical tests are described.
- **Required correction** Increase the number of independent experiments, report individual data points, and perform appropriate statistical analyses.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** BLI assay conditions
- **Evidence pointer** Methods section "Bio-layer interferometry"
- **Issue** The manuscript does not specify the temperature at which BLI experiments were performed, the regeneration buffer composition, or the number of independent experiments for each Kd determination.
- **Required correction** Provide complete methodological details to enable reproducibility.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Protein names
- **Evidence pointer** Throughout the manuscript
- **Issue** The manuscript uses "CPB" in the Introduction and Discussion but "CBP" in the Methods and Results sections. This inconsistency could confuse readers.
- **Required correction** Use a single consistent abbreviation throughout the manuscript.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reference accuracy
- **Affected element** Citation of prior work
- **Evidence pointer** Discussion section
- **Issue** The manuscript references "our prior reference's measurement using isothermal titration calorimetry" for MLL-KIX binding but does not provide the specific citation in the text.
- **Required correction** Add the appropriate citation for the prior ITC measurement.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Figure presentation
- **Affected element** Figure 3
- **Evidence pointer** Results section "The KIX domain interactions with c-Myc and N-Myc", Figure 3
- **Issue** The figure legend states that "A single experiment of pentaplicate is shown for each of the tested peptides" but the figure panels show data from multiple concentrations. It is unclear whether the shown curves are representative or averaged.
- **Required correction** Clarify in the figure legend whether the displayed data are representative traces or averaged data, and show error bars or confidence intervals where appropriate.

## Risk / unsupported claims
- The claim of "nano-molar scale" interaction in the Introduction and Conclusions is unsupported by the data presented in the Results (micromolar Kd values).
- The title's claim of "superior high affinity" is not supported by the reported micromolar Kd values.
- The proposal of a new "acetyl-TAD" domain (region 69–103) is speculative without direct evidence for acetylation-dependent function.
- The claim that the loss of 9aaTAD in L-Myc "underpins the 9aaTAD activation function" is an overinterpretation of the evolutionary data.
- The functional significance of the Myc-KIX interaction for Myc-driven tumorigenesis is stated in the Conclusions but not experimentally addressed in this study.
- The statement that the "acetyl-TAD is clearly independent but synergizes with the 9aaTAD domain" is not supported by statistical analysis or mechanistic experiments.
- The claim that "both Myc peptides displayed strong binding to the KIX comparable to MLL peptide" is weakened by the large errors in the Kd determinations and the modest difference from the negative control (Sp1-Ac).