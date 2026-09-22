## Review setup
- **Input scope** Full manuscript text (abstract, biological context, methods, results, and data availability sections)
- **Assessment boundary** Scientific content, technical soundness, completeness of reporting, and alignment with the stated scope of Biomolecular NMR Assignments
- **Shared manuscript claim summary** The authors report the production, purification, and backbone resonance assignments (1H, 15N, 13C) of the C-terminal domain (residues 189–400) of human SERBP1, an intrinsically disordered RNA-binding protein. They further report secondary structure predictions indicating a stable α-helix in the 289–299 region, and deposit the assignments in the BMRB.
- **Visible evidence base** Text descriptions of protein expression, purification, NMR experiments, assignment statistics, and secondary structure calculations. No figures, spectra, or supplementary data were provided in the submitted material.
- **Missing materials affecting confidence** Figures 1 and 2 (HSQC spectrum and secondary structure plots), raw NMR data, assignment tables, mass spectrometry data, and SDS-PAGE results are referenced but not included. This limits independent verification of assignment completeness and spectral quality.

## Reviewer
- **Overall assessment** This manuscript reports a straightforward and technically sound NMR resonance assignment of a biologically relevant, intrinsically disordered protein domain. The work is within the scope of the journal and provides a useful resource for future structural and functional studies of SERBP1. However, the absence of figures and supporting data in the provided material prevents full verification of the claims. The manuscript is likely acceptable after minor revisions, provided the figures and data availability statements are complete and consistent.
- **Who would be interested in the results, and why** Researchers studying SERBP1 function in cancer biology, mRNA regulation, and ribosome-associated processes. Also, structural biologists and NMR spectroscopists interested in intrinsically disordered proteins and their RNA-binding mechanisms. The assignments will enable future studies of SERBP1 interactions with RNA and other partners.
- **Major strengths** The biological context is well described and justifies the study. The experimental methods are detailed and reproducible. The assignment statistics are clearly reported, including the percentage of assigned residues and the handling of ambiguous or missing resonances. The secondary structure analysis uses two complementary methods and is consistent with the expected disordered nature of the protein with a localized helical region.
- **Major Concerns** None identified from the supplied material, as the core claims appear technically sound. However, the lack of figures and raw data in the provided material limits full assessment.
- **Minor Comments** See items below.
- **Technical failings that need to be addressed before the case is established** None identified from the supplied material, provided the figures and data are consistent with the text.
- **Assessment against Nature-style criteria** Originality: Moderate. The assignment of a new protein domain is incremental but useful. Scientific importance: Moderate. SERBP1 is biologically relevant, but the assignment alone does not provide functional insight. Interdisciplinary readership: Limited. Primarily of interest to NMR spectroscopists and SERBP1 researchers. Technical soundness: Appears sound based on the text, but verification requires the figures. Readability for nonspecialists: The manuscript is clearly written and accessible, with adequate context for readers unfamiliar with SERBP1.
- **Recommendation posture** Supportive if the figures and supporting data are consistent with the text and the minor comments are addressed.

### Major Concerns
None identified from the supplied material.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Completeness of reporting
- **Affected element** Figure 1 (HSQC spectrum)
- **Evidence pointer** Section "Assignment and data deposition", Figure 1
- **Issue** The text states that 188 of 203 expected peaks were assigned, and that 15 peaks could not be unambiguously assigned. However, the description of the unassigned peaks is somewhat complex and could be clarified. Specifically, the text mentions 13 arginine/glycine residues in the RGG repeat, four glycines tentatively assigned to a single peak, two unassigned glycine peaks, seven overlapped peaks, and four low-intensity peaks. The arithmetic is not immediately transparent.
- **Required correction** Provide a clear breakdown of the 15 unassigned peaks, perhaps in a table or a more structured list, to allow readers to follow the accounting. Ensure the numbers in the text match the annotations in Figure 1.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** NMR experimental details
- **Evidence pointer** Section "NMR experiments"
- **Issue** The text states that the HNHA experiment was recorded on a 100 μM 15N-labelled sample, while the triple resonance experiments were recorded on an 80 μM 13C, 15N-labelled sample. The reason for the different sample concentrations is not explained.
- **Required correction** Briefly state why a different sample concentration was used for the HNHA experiment, or note that the concentration difference is not expected to affect the results.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Secondary structure analysis
- **Evidence pointer** Section "Assignment and data deposition", Figure 2
- **Issue** The text reports secondary structure predictions from two methods (secondary chemical shifts and SSP). The results are described qualitatively, but no numerical values or error estimates are provided.
- **Required correction** Consider reporting the SSP scores for the helical region (e.g., the range of scores for residues 289–298) to allow quantitative comparison with future studies.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness of reporting
- **Affected element** Data availability
- **Evidence pointer** Section "Data availability"
- **Issue** The data availability statement mentions that NMRPipe processing scripts are available upon reasonable request, but does not specify a contact or repository for the raw NMR data.
- **Required correction** Clarify whether raw NMR data will be deposited in a public repository (e.g., BMRB or a general repository) or provide a contact for data requests.

## Risk / unsupported claims
- The claim that the α-helix in the 289–299 region is "stable under the experimental conditions" is supported by the secondary structure analysis, but the text does not provide direct evidence of stability (e.g., temperature or concentration dependence). This claim is partially supported but could be strengthened.
- The statement that the last 8 residues of the 189–408 construct were "systematically degraded" is based on mass spectrometry and initial NMR spectra, but the data are not shown. This claim is not independently verifiable from the provided material.
- The assignment completeness (93% of expected backbone resonances) is stated, but the quality of the assignments (e.g., peak widths, overlap) is not discussed in detail. This is a minor limitation but does not undermine the core claims.