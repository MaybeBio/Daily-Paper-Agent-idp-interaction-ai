## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods) as provided
- **Assessment boundary** Technical and methodological soundness of imaging analyses; internal consistency of reported results; validity of conclusions drawn from the presented data
- **Shared manuscript claim summary** The authors compare different microscopy-based analytical approaches (single focal plane, Z-projection, volumetric analysis) and labeling strategies (fluorescent protein tags vs. antibodies) for quantifying thermodynamic properties of influenza A virus-induced biomolecular condensates, concluding that simpler 2D approaches suffice for detecting large changes but 3D analyses are needed for subtle differences
- **Visible evidence base** Results sections 2.1–2.4, Figures 2–5 (referenced), Supplementary Tables S1–S3, Supplementary Figures S1–S3, Videos S1–S4 (referenced)
- **Missing materials affecting confidence** Figures and supplementary materials not provided; statistical details in figure legends not visible; raw data not available; previous study [8] not accessible for verification of methodological continuity

## Reviewer
- **Overall assessment** The manuscript addresses a relevant methodological gap in the study of biomolecular condensates, specifically for viral inclusions formed during influenza A virus infection. The authors systematically compare imaging acquisition and analysis strategies, which is useful for the community. However, the manuscript has significant limitations in its presentation of quantitative results, statistical rigor, and clarity of methodological details. The central claim that "methods can be used interchangeably" for large changes but not for small ones is only partially supported by the data as presented, and the lack of visible figures and detailed statistical outputs prevents full evaluation. The manuscript would benefit from substantial revision to clarify the quantitative basis of its conclusions.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, liquid-liquid phase separation, viral replication compartments, and those developing imaging-based screening pipelines for condensate-modulating compounds. The practical guidance on when 2D vs. 3D imaging suffices is directly relevant to laboratories performing medium-to-high-throughput condensate screens.

- **Major strengths**
  1. Addresses a practical and underappreciated problem: how imaging acquisition and processing choices affect quantitative biophysical measurements of condensates
  2. Uses a relevant biological model (IAV inclusions) with clear relevance to viral replication and potential antiviral strategies
  3. Systematic comparison of multiple analytical approaches (single plane, Z-projection, volumetric) and labeling strategies
  4. Includes machine learning-based segmentation as a modern analytical tool
  5. Provides practical recommendations for when simpler approaches are sufficient

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "We found that when observing significant phase transitions, the methods can be used interchangeably, while small changes considerably vary based on the methodology employed"
- **Evidence pointer** Sections 2.1–2.3, Figures 3–4, Supplementary Tables S1–S3
- **Concern** The central conclusion that methods are interchangeable for large changes but not small ones is not quantitatively demonstrated in the text. The authors report mean values and standard deviations for some parameters (e.g., Cdense, ΔG) but do not provide effect sizes, confidence intervals, or formal statistical comparisons across methods. The claim of "interchangeability" requires demonstration of equivalence, not merely absence of significant difference, which is not provided.
- **Why it matters** The manuscript's primary practical recommendation depends on this claim. Without formal equivalence testing or at least clear quantitative comparisons, readers cannot assess whether the conclusion is justified.
- **Resolution test** Provide formal statistical comparisons (e.g., equivalence tests, Bland-Altman analysis, or at minimum effect sizes with confidence intervals) for key parameters across methods. Specify criteria for "interchangeable" a priori.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility and methodological transparency
- **Claim pointer** The manuscript describes comparisons of single focal plane, Z-projection, and volumetric analyses, and of antibody versus fluorescent protein labeling
- **Evidence pointer** Sections 2.1–2.4, Materials and Methods 4.4–4.6
- **Concern** Critical methodological details are missing or ambiguous. The number of cells, images, and biological replicates per condition is not clearly stated for each experiment. The criteria for selecting focal planes (bottom, middle, top) are not defined (e.g., how were these positions determined relative to cell morphology?). The Z-projection method is stated as "sum of slices" but the number of slices, step size, and total Z-depth are not provided. For volumetric analysis, the segmentation parameters in Imaris are not described. The statistical tests used are mentioned generically but specific tests per figure are not visible.
- **Why it matters** Reproducibility is a core requirement for methodological papers. Without these details, other laboratories cannot implement the described approaches or verify the conclusions.
- **Resolution test** Provide complete methodological details including sample sizes, Z-stack parameters, segmentation settings, and per-experiment statistical tests. Consider adding a detailed supplementary methods section.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Internal consistency
- **Claim pointer** "The PA-mNG virus is attenuated, which results in a roughly 2log difference in viral production when compared to the wild-type counterpart" and "10 h of infection with PA-mNG PR8 approximately corresponds to 8 h of infection with the wildtype PR8 virus"
- **Evidence pointer** Section 2, Figure 2B–D
- **Concern** The manuscript uses the attenuated PA-mNG virus for most analyses but compares results to previously published data from wild-type PR8 virus [8]. The authors acknowledge attenuation but do not systematically address how this affects the generalizability of their methodological conclusions. The claim of correspondence between 10 h PA-mNG and 8 h WT infection is presented without supporting data in this manuscript.
- **Why it matters** If the attenuation alters condensate properties (size, number, dynamics), the methodological conclusions may not transfer to wild-type infections or to other condensate systems.
- **Resolution test** Provide data supporting the temporal correspondence claim, or explicitly discuss how attenuation might affect the imaging analysis recommendations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative rigor
- **Claim pointer** "The concentration of vRNPs in the inclusions was significantly different, with the top inclusions containing a lower concentration of vRNPs, as measured by Cdense (20.75 ± 7; 22.07 ± 8 and 11.49 ± 8 AU, mean ± SD for bottom, middle or top., respectively)"
- **Evidence pointer** Section 2.1, Figure 3D, Supplementary Table S1
- **Concern** The reported Cdense values for single focal planes (11–22 AU) are dramatically lower than those reported for Z-projections (e.g., 446 AU in section 2.2, and 603–3650 AU in section 2.3). The authors do not explain this order-of-magnitude discrepancy. If Cdense is a ratio or normalized intensity, the units and calculation method must be clarified. This inconsistency undermines confidence in the quantitative comparisons.
- **Why it matters** Cdense is a key thermodynamic parameter. If values are not comparable across methods, the conclusion that methods are interchangeable for detecting large changes is questionable.
- **Resolution test** Clarify the calculation of Cdense for each method and explain the large numerical differences. Provide normalized values or a clear rationale for why absolute values differ across methods.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Completeness of evidence
- **Claim pointer** "Our previous work showcased the possibility of hardening these liquid inclusions, potentially leading to novel antiviral strategies"
- **Evidence pointer** Section 1, reference [8]
- **Concern** The manuscript relies heavily on the previous study [8] for methodological context and for the nucleozin-induced hardening phenotype. However, the current manuscript does not provide sufficient replication data for the key nucleozin effects. The time course of nucleozin treatment (5 min to 2 h) is mentioned but the data are not fully presented in the text.
- **Why it matters** The nucleozin treatment serves as the "large change" condition against which method interchangeability is tested. If this condition is not fully characterized, the comparison is weakened.
- **Resolution test** Present complete time-course data for nucleozin effects in the current manuscript, or clearly indicate which data are from the previous study.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.1, Figure 3E
- **Evidence pointer** "despite not showing differences in Cdilute (Figure E)"
- **Issue** The figure reference is incomplete. It should read "Figure 3E" not "Figure E".
- **Required correction** Correct the figure reference.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Section 2.2, "ΔΔG"
- **Evidence pointer** "ΔΔG (−2326.4 ± 0.04 J·mol−1, mean ± SD)"
- **Issue** The use of "ΔΔG" is confusing. In section 2.1, the authors use "ΔG" for free energy. The double delta notation typically implies a change in ΔG between conditions, but this is not explained. Also, the value reported as "−2326.4 ± 0.04" has an implausibly small standard deviation.
- **Required correction** Clarify the definition of ΔΔG and verify the reported value and standard deviation.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Section 2.1, nucleation density
- **Evidence pointer** "ρ = numberofinclusionCytoplasmArea, µm−2"
- **Issue** The formula is written without proper spacing or formatting. Also, the statistical comparison for nucleation density across focal planes is not reported.
- **Required correction** Format the formula properly and report statistical results for nucleation density.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Section 2.3, Figure 4U–V
- **Evidence pointer** "Cdense increased dramatically (from 2125.8 ± 0.09 AU, mean ± SD, without nucleozin to 3650.0 ± 0.03 AU, mean ± SD, with 2 h nucleozin)"
- **Issue** The standard deviations reported (0.09 and 0.03 AU) are implausibly small for intensity measurements and inconsistent with the variability reported elsewhere in the manuscript.
- **Required correction** Verify the reported values and standard deviations.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 4.5, Image Analysis
- **Evidence pointer** "Images were processed using either custom ImageJ... or custom Imaris... machine learning toolkits"
- **Issue** The machine learning segmentation approach is mentioned but not described in sufficient detail. The training set size, validation approach, and accuracy metrics are not provided.
- **Required correction** Provide details on the machine learning segmentation training and validation.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Language
- **Affected element** Section 1, Introduction
- **Evidence pointer** "structurers"
- **Issue** Typographical error. Should be "structures".
- **Required correction** Correct the typo.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.3, Figure 4M
- **Evidence pointer** "from 0.172 ± 0.04 to 0.289 ± 0.06 µm2, mean ± SD"
- **Issue** The units for area are reported as µm2, which is correct, but the values seem small for condensates described as 100 nm to 1 µm in diameter. A 1 µm diameter sphere would have a cross-sectional area of approximately 0.785 µm2. The reported values may be for a different metric.
- **Required correction** Clarify what area measurement is being reported (e.g., cross-sectional area, projected area) and ensure consistency with the stated size range.

## Risk / unsupported claims
- The claim that "methods can be used interchangeably" for detecting large changes is not formally supported by equivalence testing or effect size analysis
- The temporal correspondence between 10 h PA-mNG and 8 h wild-type PR8 infection is stated without supporting data
- The hypothesis that concentration influences the temporal response to nucleozin is speculative and explicitly acknowledged as not experimentally validated
- The reported Cdense values differ by orders of magnitude between single focal plane and Z-projection analyses without explanation
- Several reported values have implausibly small standard deviations (e.g., ΔΔG = −2326.4 ± 0.04 J·mol−1; Cdense = 2125.8 ± 0.09 AU), suggesting possible reporting errors
- The generalizability of conclusions to other condensate systems beyond IAV inclusions is not established