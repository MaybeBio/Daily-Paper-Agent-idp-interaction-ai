## Review setup
- **Input scope** Full manuscript text including abstract, introduction, materials and methods, results, discussion, conclusion, and supplementary figure references
- **Assessment boundary** Scientific content, experimental design, data interpretation, and conclusions as presented in the manuscript
- **Shared manuscript claim summary** The authors investigate the effects of two macromolecular crowding agents, Ficoll-70 and Dextran-40, on the structure and dynamics of the intrinsically disordered protein NUPR1 using a multi-spectroscopic approach including SDSL-EPR, NMR, CD, SAXS, and DLS. They report that NUPR1 remains largely disordered in crowded environments, with local conformational changes at the N- and C-termini attributed to weak protein-crowder interactions rather than viscosity effects.
- **Visible evidence base** Full text with figures referenced (Figures 1-5), tables (Tables 1-2), and supplementary figures (S1-S10) described but not directly viewable
- **Missing materials affecting confidence** Actual figure data, supplementary figures, raw spectral data, and experimental replicates are not directly accessible; only descriptions are provided

## Reviewer
- **Overall assessment** The manuscript addresses a relevant question in the field of intrinsically disordered proteins, namely how macromolecular crowding affects their conformational ensemble and dynamics. The multi-technique approach is commendable, and the conclusion that NUPR1 remains disordered while showing local terminal effects is plausible. However, several technical concerns regarding data interpretation, control experiments, and the quantitative rigor of the EPR analysis need to be addressed before the conclusions can be fully supported.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, macromolecular crowding, and the biophysical characterization of IDPs in cellular-like environments. The work may also interest those investigating NUPR1 specifically, given its role in stress response and chromatin remodeling.
- **Major strengths** The use of multiple complementary biophysical techniques to characterize both global and local conformational properties is a strength. The inclusion of viscosity control experiments with sucrose is thoughtful. The study addresses a biologically relevant question about IDP behavior under crowded conditions.
- **Major Concerns** Several concerns are detailed below, primarily related to the interpretation of EPR data, the lack of quantitative analysis in some techniques, and the generalizability of the conclusions given the limited conditions tested.
- **Minor Comments** Several minor issues regarding presentation, methodological details, and interpretation are listed below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** 
  - Originality: Moderate. The question of crowding effects on IDPs is not new, but the specific application to NUPR1 and the multi-technique approach provide some novelty.
  - Scientific importance: Moderate. The findings are incremental, confirming that NUPR1 remains disordered under crowding, which is consistent with many other IDP studies.
  - Interdisciplinary readership: Limited. The work is primarily of interest to biophysicists and biochemists specializing in IDPs.
  - Technical soundness: The multi-technique approach is sound in principle, but several technical concerns (detailed below) weaken the current evidence.
  - Readability for nonspecialists: The manuscript is generally well-written and accessible, though some sections assume familiarity with EPR spectroscopy.
- **Recommendation posture** Supportive if technical concerns are resolved

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data interpretation
- **Claim pointer** The authors claim that the broadening of EPR spectra in the presence of crowders indicates weak, non-specific binding interactions between NUPR1 and the crowders, and that this is not due to viscosity effects.
- **Evidence pointer** Results section, EPR subsection; Tables 1 and 2; Supplementary Figures S7 and S8
- **Concern** The authors attribute the observed EPR spectral changes to weak protein-crowder interactions, but the evidence for this is indirect. The sucrose control experiments show that viscosity alone does not explain the changes, but this does not rule out other non-specific effects such as excluded volume or changes in solvent properties. The claim of "binding" is not directly supported by any binding assay or quantitative analysis.
- **Why it matters** The central conclusion of the paper rests on the interpretation that the observed local conformational changes are due to specific interactions with the crowders. Without direct evidence for binding, alternative explanations remain plausible.
- **Resolution test** Provide direct evidence for binding, such as isothermal titration calorimetry, surface plasmon resonance, or a concentration-dependent binding analysis. Alternatively, temper the claim to "interactions" rather than "binding" and discuss alternative mechanisms.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative analysis
- **Claim pointer** The authors report that the EPR spectra are composed of two components (sharp and broad) with specific correlation times and populations, but the quantitative analysis is not described in sufficient detail.
- **Evidence pointer** Results section, EPR subsection; Tables 1 and 2; Supplementary Figures S7 and S8
- **Concern** The manuscript states that spectra were simulated to obtain correlation times and component populations, but the fitting procedure, error analysis, and criteria for determining the number of components are not described. It is unclear how the populations were calculated and whether the two-component model is uniquely justified.
- **Why it matters** The quantitative parameters (τc values and populations) are central to the interpretation of local dynamics changes. Without a clear description of the fitting methodology and its validation, the reliability of these numbers cannot be assessed.
- **Resolution test** Provide a detailed description of the spectral simulation procedure, including the fitting model, error estimates, and justification for the number of components. Show residuals or goodness-of-fit statistics.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental design
- **Claim pointer** The authors conclude that NUPR1 remains disordered in the presence of crowders based on CD and NMR data, but the NMR data are limited to a small subset of observable residues.
- **Evidence pointer** Results section, NMR subsection; Supplementary Figures S4 and S6
- **Concern** The 2D 15N,1H-TROSY-HSQC spectrum of NUPR1 in isolation shows only a small subset of signals due to line broadening. In the presence of crowders, even fewer signals are observed. The conclusion that the protein remains disordered is based on a limited set of residues, which may not be representative of the entire protein.
- **Why it matters** The conclusion about the overall disordered nature of NUPR1 under crowding conditions relies heavily on NMR data that only sample a fraction of the residues. This limits the strength of the conclusion.
- **Resolution test** Provide additional evidence for the overall disordered state, such as CD spectra at multiple wavelengths with quantitative secondary structure analysis, or SAXS data with Kratky plot analysis at multiple concentrations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Data interpretation
- **Claim pointer** The authors state that the DLS data for the NUPR1-Ficoll mixture could not be fitted with a simple sum of two exponentials and required a stretched exponential, which they interpret as evidence of binding.
- **Evidence pointer** Results section, DLS subsection; Figure 5
- **Concern** The use of a stretched exponential to fit the slow relaxation mode is presented without adequate justification. The interpretation that this indicates binding is speculative. The DLS data are also complicated by the presence of large aggregates, which the authors acknowledge. The conclusion that DLS "was blind to the presence of the polypeptide chain" undermines the utility of this technique for supporting the binding claim.
- **Why it matters** The DLS data are used to support the binding interpretation, but the analysis is not rigorous and the conclusions are speculative. This weakens the overall case for protein-crowder interactions.
- **Resolution test** Provide a more detailed analysis of the DLS data, including justification for the stretched exponential model, and discuss alternative explanations for the observed relaxation behavior.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract states that "SDSL-EPR spectra of two spin-labelled mutants indicate that there was binding with the crowders," but the term "binding" is used without qualification. Given the indirect nature of the evidence, this overstates the findings.
- **Required correction** Rephrase to "indicate interactions with the crowders" or "suggest weak, non-specific interactions."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodology
- **Affected element** Materials and Methods, MTSL Labelling
- **Evidence pointer** Materials and Methods section, location not provided
- **Issue** The efficiency of MTSL labelling is not reported. It is important to know the labelling efficiency to interpret the EPR data correctly.
- **Required correction** Report the labelling efficiency for each mutant, e.g., by mass spectrometry or EPR quantification.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Results, Far-UV CD
- **Evidence pointer** Figure 1, location not provided
- **Issue** The CD spectra are described as showing "no major changes," but no quantitative analysis (e.g., secondary structure estimation) is provided. This makes the conclusion somewhat subjective.
- **Required correction** Provide a quantitative analysis of the CD data, such as deconvolution into secondary structure components, to support the claim of no significant change.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion section, location not provided
- **Issue** The authors speculate about the biological relevance of their findings, but the connection between the in vitro crowding conditions and the actual nuclear environment is not well developed.
- **Required correction** Expand the discussion to more carefully consider the limitations of using synthetic crowders as models for the nuclear environment.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, EPR
- **Evidence pointer** Results section, EPR subsection, location not provided
- **Issue** The description of the EPR spectra in the presence of crowders is somewhat vague. It is not clear whether the spectral changes are uniform across the entire spectrum or localized to specific regions.
- **Required correction** Provide a more detailed description of the spectral changes, possibly with overlaid spectra or difference spectra.

## Risk / unsupported claims
- The claim of "binding" between NUPR1 and the crowders is not directly supported by the data presented; the evidence is indirect and alternative explanations are not fully excluded.
- The conclusion that NUPR1 remains disordered in crowded environments is based on limited NMR data (only a subset of residues observable) and qualitative CD analysis.
- The interpretation of the DLS data, particularly the use of a stretched exponential and the conclusion that DLS was "blind" to NUPR1, is not rigorously justified.
- The speculation about the biological relevance of the findings, including the formation of "fuzzy complexes" and the role of terminal regions, goes beyond the direct evidence presented.