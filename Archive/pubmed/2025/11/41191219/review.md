## Review setup
- **Input scope** Full manuscript text including methods, figures, and supplementary information description
- **Assessment boundary** Resonance assignment quality, biological context justification, secondary structure analysis, and binding affinity measurement
- **Shared manuscript claim summary** The authors report the complete backbone and side-chain resonance assignment of the C-terminal 43 residues (Ct43) of the rat postsynaptic scaffold protein GKAP, demonstrate that this region is intrinsically disordered with a helical propensity between residues 950–970, and measure a binding affinity of 3.1 ± 0.7 µM for the Ct43 construct to the PDZ domain of Shank1.
- **Visible evidence base** Full text with methods, Figures 1 and 2, one supplementary figure described, BMRB deposition number 53245
- **Missing materials affecting confidence** The actual NMR spectra beyond the single HSQC shown, the supplementary interferogram, the complete chemical shift tables, and the raw BLI data are not available in the provided material

## Reviewer
- **Overall assessment** This manuscript presents a straightforward and technically sound resonance assignment of a 43-residue intrinsically disordered region of GKAP. The work is competently executed and the data support the conclusion that the construct is disordered with a modest helical propensity in the N-terminal portion. The biological context is well argued and the assignment will be useful for future studies of GKAP interactions. However, the manuscript contains some overinterpretation of the secondary structure predictions, and the binding affinity measurement, while interesting, is presented with insufficient methodological detail to fully assess its reliability. The work is appropriate for a specialized assignment journal but does not rise to the level of broad interdisciplinary significance.

- **Who would be interested in the results, and why** Researchers studying the postsynaptic density, scaffold protein organization, intrinsically disordered proteins, and PDZ domain-mediated interactions. The assignment provides a foundation for NMR-based studies of GKAP interactions with Shank and other PSD partners. The helical propensity data may also be of interest to those studying the role of transient secondary structure in disordered protein function.

- **Major strengths** The manuscript is clearly written and the biological context is well developed. The assignment appears complete and the use of multiple complementary analyses (POTENCI, CheSPI) strengthens the secondary structure conclusions. The comparison with AlphaFold2 predictions and the existing GH1 domain structure adds value. The inclusion of a binding affinity measurement, while preliminary, extends the utility of the assignment beyond a purely descriptive report.

- **Major Concerns**  
  - **Concern ID** R1-M1  
  - **Severity** Major  
  - **Blocking** No  
  - **Axis** Technical soundness of binding affinity measurement  
  - **Claim pointer** The manuscript states "We confirmed that the binding affinity to Shank1-PDZ of the GKAP-Ct43 protein is 3.1 ± 0.7 µM"  
  - **Evidence pointer** Methods section "Biolayer interferometry", Supplementary Fig. 1  
  - **Concern** The BLI measurement is presented as a single Kd value with standard deviation from three independent measurements, but the methods description lacks critical details. The authors do not specify the number of Shank1-PDZ concentrations used, whether the data were fit globally or locally, the quality of the fits, or whether the 6xHis tag on the bait could interfere with binding. The temperature variation of 0–3 °C between measurements is acknowledged but not discussed in terms of its potential effect on the Kd. The control measurements are described but the results of these controls are not shown or discussed.  
  - **Why it matters** The Kd value is presented as a "confirmed" result, but the methodological detail is insufficient for a reader to assess the reliability of this measurement. If this value is to be used as a reference for future studies, it needs to be more rigorously documented.  
  - **Resolution test** Provide the full BLI data including all concentrations tested, the sensorgrams, the fitting results, and the control experiments. Specify the exact number of replicates and the statistical analysis used. Discuss the potential effect of the 6xHis tag on the measured affinity.

  - **Concern ID** R1-M2  
  - **Severity** Major  
  - **Blocking** No  
  - **Axis** Interpretation of secondary structure predictions  
  - **Claim pointer** The manuscript states "The analysis of chemical shifts indicates that the construct is intrinsically disordered along its full length" and "definitive helical propensity in the extended flanking region, between residues 950–970"  
  - **Evidence pointer** Figure 1b–e, Results section "Extent of assignments and data deposition"  
  - **Concern** The authors describe the helical propensity between residues 950–970 as "definitive" based on CheSPI analysis and secondary chemical shifts, yet the Cα-Cβ secondary chemical shifts are only between −1.12 and +2 ppm, and the Hα shifts are between −0.12 and +0.08 ppm. These values are relatively modest for a "definitive" helical assignment. The comparison with the Drebrin SAH region, where Hα shifts are "almost twice as large in absolute value," suggests that the helical propensity in Ct43 is weak. The authors also note that the observed helix is shorter than the AlphaFold2 prediction, which raises questions about the reliability of the prediction.  
  - **Why it matters** The characterization of the helical propensity is a central finding of the paper. Overstating the confidence in this assignment could mislead future studies that rely on this result.  
  - **Resolution test** Provide a more quantitative comparison of the secondary chemical shifts with known helical systems, and discuss the limitations of CheSPI predictions for weakly populated helical states. Consider whether the term "definitive" is appropriate given the modest shift values.

- **Minor Comments**  
  - **Concern ID** R1-m1  
  - **Severity** Minor  
  - **Axis** Clarity of figure presentation  
  - **Affected element** Figure 1  
  - **Evidence pointer** Figure 1a–e  
  - **Issue** The figure is information-dense and the color coding for AlphaFold2 predictions versus experimentally confirmed helices may be difficult to distinguish, particularly for color-blind readers. The panel labels are small and the figure legend does not fully explain all elements.  
  - **Required correction** Increase the font size of panel labels, use more distinct colors or patterns for the two types of helical regions, and expand the figure legend to describe all elements clearly.

  - **Concern ID** R1-m2  
  - **Severity** Minor  
  - **Axis** Completeness of methods  
  - **Affected element** NMR spectroscopy section  
  - **Evidence pointer** Methods section "NMR spectroscopy and chemical shift assignment"  
  - **Issue** The authors list the experiments used but do not provide acquisition parameters such as the number of scans, spectral widths, or acquisition times. They also do not state the temperature calibration method or the referencing protocol beyond the use of DSS.  
  - **Required correction** Add a table or paragraph with the key acquisition parameters and referencing details, as is standard for assignment papers.

  - **Concern ID** R1-m3  
  - **Severity** Minor  
  - **Axis** Interpretation of the Ile985-Pro986 anomaly  
  - **Affected element** Results section "Extent of assignments and data deposition"  
  - **Evidence pointer** Figure 1b, c  
  - **Issue** The authors note the unusual secondary chemical shifts for the Ile985-Pro986 pair and speculate about steric constraints but do not provide any supporting analysis or comparison with similar motifs in other proteins.  
  - **Required correction** Either provide additional analysis to support the steric hypothesis or present the observation as an unexplained anomaly without speculation.

  - **Concern ID** R1-m4  
  - **Severity** Minor  
  - **Axis** Consistency of terminology  
  - **Affected element** Throughout the manuscript  
  - **Evidence pointer** Biological context section, Results section  
  - **Issue** The manuscript uses "GKAP" and "rGKAP" interchangeably, and the construct is referred to as both "Ct43" and "GKAP-Ct43". This is potentially confusing.  
  - **Required correction** Standardize the terminology, using "rGKAP" for the rat protein and "Ct43" for the construct throughout.

  - **Concern ID** R1-m5  
  - **Severity** Minor  
  - **Axis** Completeness of supplementary material description  
  - **Affected element** Supplementary Information section  
  - **Evidence pointer** Supplementary Fig. 1  
  - **Issue** The supplementary figure is described only as "one representative interferogram" but the figure itself is not available for review. The authors should ensure that the figure includes all necessary labels and annotations.  
  - **Required correction** Verify that the supplementary figure is complete and self-explanatory, including axis labels, concentration information, and fit results.

- **Technical failings that need to be addressed before the case is established**  
  R1-M1 (BLI methodological detail) is the most significant technical concern. The binding affinity measurement is presented as a key result but the methodology is insufficiently documented. This needs to be addressed before the affinity value can be considered reliable. R1-M2 (secondary structure interpretation) is also important, as the term "definitive" overstates the confidence in the helical assignment.

- **Assessment against Nature-style criteria**  
  - **Originality** The work is not original in concept, as resonance assignments of disordered proteins are routine. The specific target, the C-terminal region of GKAP, has not been previously assigned, which provides some novelty.  
  - **Scientific importance** The assignment is a useful resource for the PSD community but does not address a fundamental question. The biological context is well argued, but the findings are incremental.  
  - **Interdisciplinary readership** The manuscript will primarily appeal to NMR spectroscopists and researchers studying PSD scaffolding. The broader neuroscience community may find the binding affinity result of interest, but the scope is limited.  
  - **Technical soundness** The NMR assignment methodology is sound and the use of multiple analysis tools is appropriate. The BLI measurement is technically weaker and needs additional documentation.  
  - **Readability for nonspecialists** The manuscript is generally well written and the biological context is accessible. The methods section assumes familiarity with NMR techniques, which is appropriate for the target journal.

- **Recommendation posture** Supportive if technical concerns are resolved. The assignment itself appears complete and reliable, and the biological context is well argued. The BLI measurement needs additional methodological detail, and the secondary structure interpretation should be tempered. Once these issues are addressed, the manuscript would be suitable for publication in a specialized assignment journal.

## Risk / unsupported claims
- The claim that the helical propensity between residues 950–970 is "definitive" is not fully supported by the modest secondary chemical shift values presented.
- The binding affinity of 3.1 ± 0.7 µM is presented without sufficient methodological detail to assess its reliability, including the number of concentrations tested, fit quality, and control results.
- The statement that "we have not observed any signs of heterogeneity that might arise from isomerization" regarding Pro986 is not supported by any shown data.
- The comparison with the Drebrin SAH region is qualitative and not quantified, making it difficult to assess the significance of the difference.
- The claim that the construct "is deemed sufficiently long to be suitable for the investigation of potential interactions outside the primary binding site" is speculative and not supported by any data in this manuscript.