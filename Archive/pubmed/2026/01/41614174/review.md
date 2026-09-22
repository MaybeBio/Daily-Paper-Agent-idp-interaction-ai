## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, methods, results, discussion, and supplementary figure references
- **Assessment boundary** Scientific validity, technical soundness, and support of claims based solely on the provided manuscript text
- **Shared manuscript claim summary** The authors report that phosphorylation of α-synuclein fibrils at S129 reduces the dynamics of the intrinsically disordered C-terminus and increases binding of the cochaperone DNAJB1, as probed by solid-state NMR, binding assays, electron microscopy, and molecular dynamics simulations
- **Visible evidence base** Methods sections for protein expression, fibril formation, phosphorylation, MALDI-TOF, LC-MS, sedimentation assays, EM, NMR spectroscopy, and HyRes coarse-grained simulations; Results sections describing binding affinity, fibril width, NMR spectra, and simulation outcomes; Discussion section interpreting findings
- **Missing materials affecting confidence** Supplementary figures (S1-S15) and tables (S1) referenced but not provided; raw NMR spectra not shown; full LC-MS data not shown; simulation trajectories and analysis scripts referenced via GitHub but not independently verified; statistical details for K D fitting not fully described

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question regarding how the most prevalent post-translational modification of α-synuclein, phosphorylation at S129, modulates chaperone recognition. The combination of solid-state NMR, binding assays, and coarse-grained simulations is appropriate and potentially powerful. However, several technical concerns regarding the interpretation of NMR intensity changes, the quantitation of binding affinities, and the consistency between experimental and simulation results need to be resolved before the central claims are fully established. The work is of interest to the neurodegeneration and protein chaperone communities, and the methodological approach is sound in principle.
- **Who would be interested in the results, and why** Researchers studying α-synuclein aggregation and synucleinopathies, molecular chaperone biology, protein post-translational modifications, and amyloid fibril structure and dynamics. The findings have implications for understanding how phosphorylation modulates chaperone-mediated disaggregation, which is relevant to therapeutic strategies targeting protein clearance in Parkinson's disease and related disorders.
- **Major strengths** The study addresses a clinically relevant question with a clear hypothesis. The use of solid-state NMR to probe dynamics in fibrils is technically sophisticated. The combination of experimental binding assays with MD simulations provides complementary perspectives. The authors carefully controlled for fibril batch variability by splitting samples. The observation that phosphorylation reduces C-terminal dynamics and increases DNAJB1 binding is potentially significant.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (K D quantitation), R1-M2 (NMR intensity interpretation), R1-M3 (simulation-experiment consistency), R1-M4 (phosphorylation site specificity)
- **Assessment against Nature-style criteria** Originality: The question of how S129 phosphorylation affects chaperone binding to α-synuclein fibrils is novel and timely. Scientific importance: The findings could have implications for understanding how a prevalent PTM modulates chaperone-mediated disaggregation, which is relevant to disease mechanisms. Interdisciplinary readership: The work bridges structural biology, biophysics, and neurodegeneration, and would appeal to a broad audience. Technical soundness: The methods are generally appropriate, but several concerns about quantitation and interpretation need resolution. Readability for nonspecialists: The manuscript is generally well-written and accessible, though some NMR details may be challenging for non-experts.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding K D quantitation, NMR intensity interpretation, and simulation-experiment consistency

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative binding analysis
- **Claim pointer** The authors report a K D of 58.1 μM for WT fibrils and 1.9 μM for pS129 fibrils, indicating a ~30-fold higher affinity of DNAJB1 for phosphorylated fibrils
- **Evidence pointer** Results section, Figure C, Figure S2
- **Concern** The K D values are derived from sedimentation assays analyzed by SDS-PAGE densitometry. The manuscript does not provide details on the fitting procedure, the number of replicates, the error estimates for the K D values, or whether the binding model accounts for the multivalent nature of fibril-DNAJB1 interactions. The K D values differ by ~30-fold, which is a large effect, but the statistical robustness of this difference is not demonstrated. Additionally, the assay measures depletion of free DNAJB1 from the supernatant, which may not directly reflect equilibrium binding if fibril pelleting is incomplete or if DNAJB1 binds nonspecifically to the tube or to monomeric α-synuclein present in the supernatant.
- **Why it matters** The claim of enhanced binding to pS129 fibrils is central to the paper. If the K D values are not reliably determined, the quantitative conclusion of a 30-fold affinity difference is not supported. This would weaken the primary functional claim of the study.
- **Resolution test** Provide full binding curves with replicates, error bars, and statistical analysis. Describe the fitting model in detail, including whether it accounts for multivalent binding. Demonstrate that the assay specifically reports fibril-bound DNAJB1 and not monomer-bound or nonspecifically adsorbed protein. If possible, validate K D values with an orthogonal method such as isothermal titration calorimetry or fluorescence anisotropy.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** NMR intensity interpretation
- **Claim pointer** The authors state that phosphorylation at S129 reduces the dynamics of the intrinsically disordered C-terminus, based on reduced INEPT/CP intensity ratios and loss of cross-peaks in 2D HSQC spectra
- **Evidence pointer** Results section, Figures C, S3, S4
- **Concern** The interpretation of reduced INEPT/CP ratios and HSQC cross-peak intensities as reduced dynamics is plausible but not unambiguous. INEPT intensity depends on transverse relaxation rates, which are influenced by both dynamics and chemical exchange. The loss of specific cross-peaks in pS129 fibrils could also result from chemical shift changes due to the phosphate group, leading to peak overlap or broadening from conformational heterogeneity, rather than a genuine reduction in mobility. The authors do not provide relaxation dispersion measurements or other dynamic probes to distinguish these possibilities. Additionally, the normalization procedure for INEPT/CP ratios is not fully described, and it is unclear whether the observed differences are statistically significant.
- **Why it matters** The claim that phosphorylation reduces C-terminal dynamics is a key mechanistic finding that links the PTM to altered chaperone binding. If the NMR data are misinterpreted, the proposed mechanism is weakened.
- **Resolution test** Provide quantitative analysis of INEPT/CP ratios with error estimates and statistical tests. Consider additional experiments such as 15N relaxation dispersion or 13C R1ρ measurements to directly assess dynamics. Discuss whether chemical shift changes from phosphorylation could account for the observed spectral differences. Show full HSQC spectra with assignments to demonstrate which peaks are lost or shifted.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Simulation-experiment consistency
- **Claim pointer** The authors state that MD simulations suggest reduced dynamics of pS129 is due to increased interaction of the phosphorylated C-terminus with the fibril core, and that simulations confirm enhanced DNAJB1 binding to pS129 fibrils
- **Evidence pointer** Results section, Figures D-G, S5, S14, S15
- **Concern** The coarse-grained HyRes simulations are used to provide a structural rationale for the experimental observations. However, the manuscript does not provide sufficient detail on the simulation setup, including the initial placement of DNAJB1 dimers, the force field parameters for the phosphorylated serine, the convergence criteria, or the statistical analysis of the contact probabilities. The simulations show increased contact of pS129 with the fibril core, but it is unclear whether this is due to specific electrostatic interactions or to non-specific effects of the added negative charge. The contact frequency analysis in Figure C shows the phosphorylation site as the most contacted residue, but the manuscript does not discuss whether this is statistically significant compared to other residues. The claim that simulations "confirm" the experimental findings is overstated given the approximate nature of coarse-grained models.
- **Why it matters** The simulations are used to propose a mechanistic explanation for the experimental observations. If the simulation results are not robust or are overinterpreted, the proposed mechanism is not well supported.
- **Resolution test** Provide detailed simulation parameters, convergence analysis, and statistical error estimates for contact probabilities. Discuss the limitations of the coarse-grained model for capturing phosphorylation effects. Consider additional simulations with different initial conditions or force field parameters to test the robustness of the findings. Clarify whether the simulations are hypothesis-generating or confirmatory.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Phosphorylation site specificity
- **Claim pointer** The authors conclude that phosphorylation at S129 specifically changes DNAJB1 binding to the C-terminus of α-synuclein fibrils
- **Evidence pointer** Results section, Figures A-C, S1
- **Concern** The manuscript reports that approximately 63% of S129 is phosphorylated after 24 hours, and that phosphorylation at other serine and threonine residues is below 1%. However, the binding assays and NMR experiments were performed on fibrils with partial phosphorylation. It is unclear whether the observed effects are due to the fraction of phosphorylated S129 or to other changes induced by the phosphorylation reaction conditions. The authors do not compare the binding of DNAJB1 to fully phosphorylated versus partially phosphorylated fibrils, nor do they test whether phosphorylation at other sites (e.g., S87) could contribute to the observed effects. The specificity of the phosphorylation for S129 is claimed but not rigorously demonstrated in the context of the fibril.
- **Why it matters** The central claim is that S129 phosphorylation specifically modulates DNAJB1 binding. If the effects are not specific to S129 or are influenced by the degree of phosphorylation, the conclusions are not well supported.
- **Resolution test** Provide data on the binding of DNAJB1 to fibrils with varying degrees of S129 phosphorylation. Consider using a phosphomimetic mutant (e.g., S129E) or a phosphorylation-deficient mutant (e.g., S129A) to test specificity. Discuss whether the 63% phosphorylation level is sufficient to explain the observed effects and whether the remaining unphosphorylated S129 could dilute the signal.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Fibril width measurements
- **Evidence pointer** Results section, Figure B
- **Issue** The manuscript reports a reduction in fibril width from 11.21 ± 2.04 nm to 9.15 ± 1.94 nm with a p value of 3.7193 × 10⁻¹⁴. The number of fibrils measured and the number of independent experiments are not stated.
- **Required correction** Provide the number of fibrils measured, the number of independent experiments, and the statistical test used. Consider reporting the effect size and confidence intervals.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Phosphorylation reaction
- **Evidence pointer** Methods section, Phosphorylation of aSyn Fibrils
- **Issue** The phosphorylation reaction conditions are described, but the efficiency of phosphorylation is only reported as 63% by LC-MS. It is unclear whether this is the maximum achievable or whether longer incubation or higher enzyme concentrations could increase the yield.
- **Required correction** Discuss whether 63% phosphorylation is saturating and whether higher levels could be achieved. Consider reporting the range of phosphorylation levels across replicates.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Figure accessibility
- **Affected element** NMR spectra
- **Evidence pointer** Results section, Figures C, S3, S4
- **Issue** The HSQC spectra are described as showing reduced intensity in pS129 fibrils, but the figures are not provided in the manuscript text. It is difficult to assess the quality of the spectra and the extent of the intensity changes.
- **Required correction** Ensure that representative spectra are shown with clear annotations of assigned peaks and that intensity differences are quantified and displayed in a way that is accessible to readers.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Simulation reproducibility
- **Affected element** MD simulations
- **Evidence pointer** Methods section, Coarse-Grained Simulations of the Long Fibril
- **Issue** The simulation scripts are available on GitHub, but the manuscript does not provide a version number or a DOI for the code. This limits reproducibility.
- **Required correction** Provide a persistent identifier (e.g., Zenodo DOI) for the simulation scripts and input files.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The discussion mentions a recent study by Han and co-workers on C-terminus-core interactions in α-synuclein fibril polymorphs, but does not provide a full citation.
- **Required correction** Add the full citation for the Han and co-workers study and any other references mentioned in the discussion.

## Risk / unsupported claims
- The claim of a ~30-fold difference in K D between WT and pS129 fibrils is not fully supported due to insufficient detail on the binding assay fitting and statistical analysis
- The interpretation of reduced INEPT/CP ratios and HSQC cross-peak intensities as reduced C-terminal dynamics is plausible but not unambiguously established without additional dynamic measurements
- The simulation results are presented as confirmatory, but the coarse-grained model limitations and lack of detailed convergence analysis make this claim overstated
- The specificity of the observed effects for S129 phosphorylation is not rigorously demonstrated given the partial phosphorylation level and lack of mutant controls
- The claim that DNAJB1 binding "pulls" the C-terminus away from the fibril surface is speculative and not directly supported by the presented data