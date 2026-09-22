## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, appendices, and footnotes
- **Assessment boundary** Scientific content, methodological rigor, data interpretation, and claims as presented in the provided manuscript
- **Shared manuscript claim summary** The authors determine the thermodynamic contributions of bivalent binding in the Notch transcriptional activation complex, showing that an intrinsically disordered linker between RAM and ANK domains of NICD enhances assembly by increasing effective concentration, and that bivalency improves occupancy at CSL binding sites by approximately three orders of magnitude
- **Visible evidence base** ITC experiments, analytical and numerical fitting models, binding polynomial calculations, and comparisons with previously published structural and biochemical data
- **Missing materials affecting confidence** Figures and tables referenced but not provided in the submitted text, including Figures 1-9, Tables S1-S2, and Figure S1-S3; raw ITC data; experimental replicates beyond those described; details on protein concentration determination and sample preparation

## Reviewer
- **Overall assessment** This manuscript presents a rigorous thermodynamic analysis of the Notch transcriptional activation complex assembly, addressing a long-standing question about the energetic role of bivalent interactions mediated by an intrinsically disordered linker. The authors develop a novel analytical framework for analyzing obligate heterotrimer formation by ITC and apply it to quantify the effective concentration enhancement provided by the disordered linker. The work is technically sound in its core approach, but several concerns about model assumptions, data interpretation, and the physiological relevance of the conclusions need to be addressed. The finding that bivalency enhances occupancy by three orders of magnitude is significant and will be of interest to the signaling and biophysics communities, though the broader implications for Notch regulation in vivo require more careful discussion.
- **Who would be interested in the results, and why** Researchers studying Notch signaling, transcriptional regulation, and signal transduction will find the quantitative framework valuable for understanding complex assembly. The biophysics community, particularly those interested in intrinsically disordered proteins and multivalent interactions, will appreciate the methodological advances in analyzing higher-order complexes by ITC. Additionally, those studying protein-protein interaction thermodynamics and the role of linkers in modulating binding affinity will find the effective concentration analysis instructive.
- **Major strengths** The development of an analytical model for obligate heterotrimer formation by ITC is a significant methodological contribution. The systematic comparison of binding reactions in trans and cis provides a clean experimental design to isolate the energetic contribution of bivalency. The authors appropriately address the standard state issue and provide a clear framework for interpreting the positive coupling free energy. The use of binding polynomials to calculate species populations and demonstrate the functional consequences of bivalency is elegant and compelling.
- **Major Concerns** The concerns below identify issues with model assumptions, data interpretation, and the strength of certain conclusions relative to the evidence provided.
- **Minor Comments** Several smaller issues regarding presentation, clarity, and completeness of the methods are noted.
- **Technical failings that need to be addressed before the case is established** The assumption of no binary complex formation under ITC conditions needs more rigorous validation. The potential for tetramer formation in the cis binding experiments and its impact on the extracted coupling parameters requires more thorough analysis. The physiological relevance of the conclusions depends on concentration estimates that are not fully justified.
- **Assessment against Nature-style criteria** Originality: The work provides a new quantitative framework for analyzing bivalent interactions in a biologically important complex, which is original and valuable. Scientific importance: The findings address a fundamental question about how disordered linkers contribute to complex assembly, with implications for understanding Notch signaling regulation. Interdisciplinary readership: The work bridges biophysics and cell signaling, making it relevant to multiple communities, though the technical nature may limit accessibility. Technical soundness: The core thermodynamic analysis appears sound, but several assumptions require further validation. Readability for nonspecialists: The manuscript is clearly written but assumes familiarity with ITC and binding thermodynamics, which may limit accessibility to a broad Nature readership.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding model validation and the physiological relevance of the conclusions.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that CSL, ANK, and MAML form an obligate heterotrimer with no appreciable binary complex formation under the ITC conditions used.
- **Evidence pointer** Results section, Figure 3, Figure S1
- **Concern** The conclusion that none of the pairwise binary complexes are populated to appreciable levels is based on the absence of detectable heat in pairwise titrations. However, the limit of detection is estimated using a c-value analysis that assumes a particular binding model. The authors state that the dissociation constant for each binary interaction must be greater than 20 µM based on a c-value of 0.1, but this threshold is somewhat arbitrary and depends on the sensitivity of the calorimeter and the enthalpy of binding. If the binary interactions have very small enthalpies, they could be present at significant levels without producing detectable heat. The authors should provide a more rigorous justification for the obligate heterotrimer assumption, perhaps by using a global analysis that includes binary species and demonstrating that the data cannot be fit with such species present.
- **Why it matters** The obligate heterotrimer model is central to the analysis. If binary complexes are populated, the extracted thermodynamic parameters for the ternary complex and the subsequent coupling analysis would be incorrect. The entire quantitative framework depends on this assumption.
- **Resolution test** The authors should perform a global fit of the ITC data that includes binary complex formation and demonstrate that the obligate heterotrimer model is statistically preferred. Alternatively, they could use an independent method such as analytical ultracentrifugation or mass spectrometry to directly assess the species present under the ITC conditions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that the bivalent interaction enhances occupancy of RAM and ANK at their binding sites on CSL by about three orders of magnitude.
- **Evidence pointer** Discussion section, Figures 8 and 9
- **Concern** The three orders of magnitude enhancement is derived from comparing the midpoint of the cis binding transition (74 pM) with the trans binding midpoints (20 and 65 nM). However, this comparison assumes that the concentrations of free RAM and ANK in the trans experiment are directly comparable to the concentration of the RAMANK polypeptide in the cis experiment. The effective concentration interpretation depends on the assumption that the disordered linker does not impose any conformational strain or entropic penalty beyond what is captured by the effective concentration. The authors should discuss whether the linker length and flexibility could introduce additional effects that are not accounted for in this simple model. Additionally, the calculation of the cis binding midpoint at 74 pM relies on the extracted coupling free energy, which itself depends on the obligate heterotrimer assumption. If that assumption is incorrect, the enhancement factor would change.
- **Why it matters** The three orders of magnitude enhancement is a headline result of the paper. If this number is not robust to model assumptions, the central conclusion about the importance of the disordered linker would be weakened.
- **Resolution test** The authors should perform a sensitivity analysis to show how the enhancement factor changes with reasonable variations in the model assumptions. They should also discuss whether the effective concentration of 17 µM is consistent with theoretical predictions for a disordered linker of this length, and whether the entropic cost of loop closure is reasonable.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The claim that the bivalent interaction through the disordered linker is important for assembly of the Notch transcriptional activation complex in a cellular context.
- **Evidence pointer** Discussion section
- **Concern** The authors show that at the ITC concentrations used, the ternary complex is formed with high affinity, and that bivalency enhances occupancy. However, the physiological relevance of these findings depends on the actual concentrations of NICD, CSL, and MAML in the nucleus. The authors cite a recent study suggesting nuclear concentrations of Notch2 of 2 nM, and they argue that the ternary complex would not assemble to high levels without bivalency. However, this argument assumes that the relevant concentrations are the total nuclear concentrations, which may not reflect the local concentrations at gene regulatory elements where these proteins are recruited. The authors should discuss whether the effective concentration enhancement they measure is sufficient to overcome the low nuclear concentrations, and whether other factors such as DNA binding or post-translational modifications could contribute to complex assembly.
- **Why it matters** The broader significance of the work for understanding Notch signaling in vivo depends on whether the thermodynamic effects measured in vitro are relevant at physiological concentrations. If the complex can assemble through other mechanisms, the importance of the disordered linker would be diminished.
- **Resolution test** The authors should provide a more nuanced discussion of the concentration regimes in which bivalency matters, and ideally estimate the local concentrations of these proteins at Notch target gene promoters. They could also discuss whether the effective concentration they measure is consistent with the known biology of Notch signaling.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The claim that the tetrameric complex R(A)CM(R)A forms at high RAMANK concentrations and that its inclusion in the fitting model is necessary.
- **Evidence pointer** Results section, Figure 6, Appendix 3
- **Concern** The authors state that the fitted value of ΔG° for bivalent coupling changes significantly when the tetrameric species is included in the model, from +6.4 to +6.5 kcal/mol for ΔG and from +3.0 to +9.5 kcal/mol for ΔH. The large change in ΔH with a small change in ΔG suggests that the model is not well constrained by the data. The authors should demonstrate that the data are sufficient to distinguish between the model with and without the tetrameric species, perhaps by showing that the fits are significantly worse when the tetramer is excluded. Additionally, the authors should discuss whether the tetrameric species is expected to form based on the structural biology of the system, and whether there is any independent evidence for its existence.
- **Why it matters** The inclusion of the tetrameric species affects the extracted thermodynamic parameters for bivalency. If the model is not well constrained, the reported values of ΔG and ΔH for bivalent coupling may not be reliable.
- **Resolution test** The authors should perform a model comparison using an information criterion such as AIC or BIC to demonstrate that the model with the tetramer is statistically preferred. They should also provide a figure showing the fits with and without the tetrameric species to allow readers to assess the quality of the fits.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Figure 1
- **Evidence pointer** Figure 1
- **Issue** The figure is not provided in the manuscript text, making it difficult to follow the domain architecture and the shorthand notation used throughout the paper.
- **Required correction** Ensure that Figure 1 clearly labels all domains and regions, and consider adding a schematic of the binding reactions described in Table 1.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods section
- **Evidence pointer** Methods section, ITC subsection
- **Issue** The methods state that protein concentrations were determined from UV absorbance and calculated extinction coefficients, but the specific extinction coefficients used are not provided. This makes it difficult to assess the accuracy of the concentration measurements.
- **Required correction** Provide the extinction coefficients used for each protein or a reference to where they were calculated.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion section
- **Evidence pointer** Discussion section, paragraph on standard state
- **Issue** The discussion of the standard state issue is somewhat dense and may be difficult for non-specialists to follow. The authors should consider adding a brief explanation of why the standard state matters for interpreting the coupling free energy.
- **Required correction** Add a sentence or two explaining the standard state concept in the context of binding thermodynamics.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Appendix 1
- **Evidence pointer** Appendix 1
- **Issue** The appendix provides a detailed derivation of the cubic equation solution, but the code for implementing the fitting is only mentioned as being available on GitHub. The authors should provide the code as supplementary material to ensure reproducibility.
- **Required correction** Include the Jupyter notebook or a link to a stable repository as supplementary material.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Footnote 3
- **Evidence pointer** Footnote 3
- **Issue** The footnote refers to a calculation of the relative amounts of bivalent ternary and tetrameric complexes at specific concentrations, but the calculation is not shown. This makes it difficult to verify the claim.
- **Required correction** Show the calculation or provide a reference to where it is described.

## Risk / unsupported claims
- The claim that the ternary complex would not assemble to high levels in a cellular context without bivalency is based on a single concentration estimate and is not directly supported by the experimental data.
- The claim that the disordered linker does not impose conformational strain beyond the effective concentration effect is an assumption that is not tested experimentally.
- The claim that the tetrameric complex forms at high RAMANK concentrations is inferred from the fitting model but is not directly validated by independent experiments.
- The claim that the bivalent interaction enhances occupancy by three orders of magnitude is dependent on the obligate heterotrimer assumption and the specific model used for analysis.