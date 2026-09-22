## Review setup
- **Input scope** Full manuscript text including abstract, introduction, materials and methods, results, discussion, and supplementary figure/table references
- **Assessment boundary** Scientific content, technical soundness, and claims as presented in the provided manuscript text. No external data or unpublished materials were consulted.
- **Shared manuscript claim summary** The authors report high-resolution crystal structures of three llama-derived single-domain antibodies (sdAbs) bound to the SARS-CoV-2 nucleocapsid (N) protein. Two sdAbs (B6 and C2) bind the N-terminal RNA-binding domain (RBD), and one (E2) binds the C-terminal dimerization domain (CTD). The authors map epitopes, assess sequence conservation across SARS-CoV-2 variants, and demonstrate that RBD-binding sdAbs compromise RNA binding and liquid-liquid phase separation (LLPS) of N protein.
- **Visible evidence base** Crystal structures (three complexes), nickel pulldown assays, electrophoretic mobility shift assays (EMSAs), in vitro phase separation assays, sequence variability analysis using publicly available datasets
- **Missing materials affecting confidence** Supplementary figures and tables (referenced but not provided), raw diffraction data statistics, full refinement statistics, EMSA gel images, phase separation quantification details, negative control data for pulldown assays

## Reviewer
- **Overall assessment** This manuscript presents structurally and biochemically informative data on sdAb recognition of the SARS-CoV-2 N protein. The crystal structures are likely of high quality given the reported resolutions, and the epitope mapping is clear. The functional experiments linking sdAb binding to impaired RNA binding and LLPS are interesting but raise questions about mechanism and physiological relevance. The conservation analysis is straightforward and supports the potential utility of these sdAbs for diagnostic applications. However, several technical details and interpretive claims require clarification or additional support before the conclusions are fully established.
- **Who would be interested in the results, and why** Structural biologists studying antibody-antigen recognition, virologists interested in SARS-CoV-2 N protein function, and developers of diagnostic reagents for COVID-19. The structures provide templates for engineering sdAbs with diagnostic or therapeutic applications, and the functional data on LLPS modulation may interest researchers studying viral RNP assembly.
- **Major strengths** 1) High-resolution crystal structures of three sdAb-N complexes provide detailed molecular insights into epitope recognition. 2) The combination of structural, biochemical, and bioinformatic approaches strengthens the conclusions. 3) The conservation analysis across nearly 500,000 SARS-CoV-2 genomes is comprehensive and directly relevant to diagnostic utility. 4) The demonstration that RBD-binding sdAbs affect RNA binding and LLPS adds functional depth beyond static structures.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** 
- **Recommendation posture** Supportive if technical concerns are resolved

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that sdAb-B6 and sdAb-C2 "significantly reduced the progressive band-shift observed with wild-type N protein" in EMSAs, and that this suggests these sdAbs compromise large-scale self-assembly of N rather than directly interfering with RNA binding.
- **Evidence pointer** Results section, RNA Binding Assays; Figure 4A, 4B; Supplementary Figure 3
- **Concern** The EMSA data are described qualitatively, and the claim that sdAbs affect "large-scale self-assembly" is inferred from band-shift patterns without direct quantification or controls. The authors report binding affinities (Kd values) but do not provide statistical comparisons between conditions. The Hill coefficient of 5 is fixed rather than fitted, which may mask differences in cooperativity between conditions. Additionally, the gels show "progressive shift toward the well" which is interpreted as higher-order assembly, but this could also reflect non-specific aggregation or gel artifacts. The distinction between effects on RNA binding per se versus effects on oligomerization is not rigorously established.
- **Why it matters** The functional conclusion that sdAbs compromise N protein self-assembly is a key finding of the manuscript. If this claim is not robustly supported, the physiological relevance of the structural data is diminished. The distinction between direct RNA-binding inhibition and effects on oligomerization has implications for how these sdAbs might be used diagnostically or therapeutically.
- **Resolution test** Provide quantified EMSA data with replicates and statistical analysis. Include native gel electrophoresis or size-exclusion chromatography to directly assess N oligomerization in the presence and absence of sdAbs. Fit the Hill coefficient rather than fixing it, or justify the fixed value with appropriate controls. Show that the band-shift phenotype is specific to sdAb binding and not due to non-specific protein effects.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "all three sdAbs recognize highly conserved surfaces on the N protein, suggesting that they could be used to develop affordable diagnostic tests to detect all circulating SARS-CoV-2 variants."
- **Evidence pointer** Results section, Variability of sdAb-Recognition Surfaces; Supplementary Figure 2; Supplementary Table 3
- **Concern** The conservation analysis relies on a dataset of 489,605 sequences from February 2021. The manuscript was published in August 2021, and the authors do not discuss whether more recent variants (e.g., Delta, which emerged in early 2021, or Omicron, which emerged later) were included. The analysis of "variants of concern" is mentioned but not detailed. The authors state that mutations in the epitopes are rare, but the threshold for "highly conserved" is not defined. The claim that sdAbs will recognize "all circulating SARS-CoV-2 variants" is a strong statement that requires more rigorous support, particularly given the rapid evolution of the virus.
- **Why it matters** The diagnostic utility of these sdAbs depends on their ability to recognize emerging variants. Overstating the breadth of recognition could mislead developers and public health officials. The analysis is time-limited and may not reflect the current variant landscape.
- **Resolution test** Update the analysis with more recent sequence data, including variants that emerged after February 2021. Define the criteria for "highly conserved" and provide a quantitative threshold. Discuss the limitations of the analysis with respect to future viral evolution. Consider testing sdAb binding to N proteins from specific variants of concern experimentally.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors report that sdAb-E2 binds the CTD and that "addition of sdAb-E2... did not strongly affect formation of N+RNA condensates."
- **Evidence pointer** Results section, sdAb Binding Compromises RNA Binding and Phase Separation; Figure 4C, 4D
- **Concern** The phase separation assay uses a 1:1 ratio of sdAb to N protein, but the stoichiometry of the N-CTD dimer to sdAb-E2 in the crystal structure is 2:1 (one sdAb per dimer). The authors do not discuss whether the 1:1 ratio used in the assay is appropriate or whether higher concentrations of sdAb-E2 might have an effect. Additionally, the quantification of LLPS is described as "total fluorescence inside condensates" but the details of image analysis, thresholds, and statistical comparisons are not provided. The conclusion that sdAb-E2 does not affect LLPS is based on a single condition and may not be generalizable.
- **Why it matters** The functional significance of sdAb-E2 binding to the CTD is unclear. If the authors claim that this sdAb does not affect LLPS, they should demonstrate this across a range of conditions. The stoichiometry issue could affect the interpretation of both the structural and functional data.
- **Resolution test** Test a range of sdAb-E2 concentrations, including saturating conditions. Provide detailed quantification methods and statistical analysis for LLPS experiments. Discuss the stoichiometry of the complex and its implications for the functional assays.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The authors state that "the structure was determined by molecular replacement using PHASER" and provide refinement details in Supplementary Table 2.
- **Evidence pointer** Materials and Methods, Crystallography; Supplementary Table 2
- **Concern** The manuscript does not provide key crystallographic statistics in the main text, and the supplementary table is not available for review. Critical information such as R-free, Ramachandran statistics, and coordinate errors is missing. The authors also do not report how the quality of the electron density was assessed, particularly for the sdAb-E2 complex where "some protomers of N269-364 showed poor electron density in regions distant from the sdAb-E2 interface." This raises concerns about the reliability of the models, particularly for the E2 complex.
- **Why it matters** The structural claims are central to the manuscript. Without full crystallographic statistics, the quality of the models cannot be assessed. The poor electron density in parts of the E2 complex could affect the interpretation of the interface and the conclusions drawn from it.
- **Resolution test** Provide complete crystallographic data in the main text or a fully accessible supplementary table, including R-work, R-free, Ramachandran statistics, and B-factor analysis. Discuss the quality of the electron density for all regions of the models, particularly for the E2 complex. Consider depositing structure factors along with coordinates.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the sdAbs "recognize highly conserved surfaces on the Nucleocapsid protein, suggesting that they could be used to develop affordable diagnostic tests to detect all circulating SARS-CoV-2 variants." The phrase "all circulating" is overly broad and not supported by the data, which only analyzed sequences up to February 2021.
- **Required correction** Revise to "currently circulating variants" or "variants analyzed in this study."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph 2
- **Issue** The introduction states that "two recent studies reported the isolation of a total of four single-domain antibodies (sdAbs) that target SARS-CoV-2 N with high affinity." However, the authors do not clearly distinguish which sdAbs came from which study until the Results section. This creates confusion for the reader.
- **Required correction** Briefly describe the origin of each sdAb in the Introduction or reorganize the text to avoid ambiguity.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Materials and Methods, RNA Binding Assays
- **Evidence pointer** Materials and Methods, RNA Binding Assays
- **Issue** The RNA binding assay uses a 7mer RNA, but the authors do not justify this choice or discuss whether longer RNAs might yield different results. The physiological relevance of such a short RNA is unclear.
- **Required correction** Provide a rationale for the RNA length used, or discuss the limitations of this choice.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, Variability of sdAb-Recognition Surfaces
- **Evidence pointer** Results, Variability of sdAb-Recognition Surfaces
- **Issue** The authors state that "the proteins' three intrinsically disordered regions are mutated more than 20-fold more often than the ordered NRBD or NCTD domains." This is an interesting observation, but the authors do not discuss the potential implications for N protein function or for the use of sdAbs targeting these regions.
- **Required correction** Add a brief discussion of why IDRs are more variable and what this means for diagnostic target selection.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Materials and Methods, Phase Separation Assays
- **Evidence pointer** Materials and Methods, Phase Separation Assays
- **Issue** The phase separation assay uses Cy5-labeled N protein, but the labeling efficiency and its effect on N protein behavior are not discussed. Labeling could potentially alter LLPS properties.
- **Required correction** Provide details on labeling efficiency and include a control showing that labeled and unlabeled N protein behave similarly.

## Risk / unsupported claims
- The claim that sdAbs "could be used to develop affordable diagnostic tests to detect all circulating SARS-CoV-2 variants" is not fully supported by the data, as the analysis is limited to sequences from February 2021 and does not include experimental validation against variant N proteins.
- The claim that sdAb binding "compromises large-scale self-assembly of N" is inferred from EMSA band-shift patterns without direct evidence of oligomeric state changes.
- The statement that sdAb-E2 "did not strongly affect formation of N+RNA condensates" is based on a single condition and lacks statistical rigor.
- The crystallographic quality of the E2 complex is uncertain given the reported poor electron density in some regions, and the impact on the structural conclusions cannot be fully assessed without complete statistics.