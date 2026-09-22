## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, figure legends not provided)
- **Assessment boundary** Scientific claims, methodological soundness, evidence quality, and alignment with Nature-style criteria based solely on the supplied text
- **Shared manuscript claim summary** The authors claim that conformational fluctuations of three intrinsically disordered proteins (FUS-C, LAF-N, TAF-C) exhibit scale-free spatio-temporal correlations, evidenced by 1/f noise in power spectra of end-to-end distance fluctuations, power-law size distributions of dynamic residue domains, and scale-free behavioral correlations between residue motions. These features are interpreted as signatures of criticality, which the authors argue enables IDPs to respond sensitively to sequence composition and generate structural heterogeneity beneficial for phase separation.
- **Visible evidence base** Simulation data (10 independent 1-µs all-atom MD runs per protein), smFRET experiments (FUS-C and LAF-N), coarse-grained HP polymer model simulations, power spectrum analysis, residue domain size distribution analysis, correlation function analysis, sequence composition analysis, high-salt condition simulations
- **Missing materials affecting confidence** Figure contents and numerical values (Figures 1-5, S1-S10), table contents (Table S1), exact fitting parameters and error estimates, statistical significance tests, simulation convergence criteria, force field validation details, FRET dye labeling efficiency values, raw data traces

## Reviewer

- **Overall assessment** The manuscript presents an interesting and potentially significant observation that IDP conformational dynamics exhibit scale-free spatio-temporal correlations reminiscent of critical phenomena. The combination of µs-scale atomistic simulations with smFRET experiments is commendable and provides complementary evidence. However, the central claim of criticality rests on interpretive analogies that require stronger quantitative support and more rigorous statistical validation. Several methodological details and control analyses are missing that would be needed to firmly establish the case. The work is likely to interest the biophysics and soft matter communities, but the current evidence base is insufficient to fully support the strong conclusions drawn.

- **Who would be interested in the results, and why** Biophysicists studying IDP conformational dynamics and phase separation; soft matter physicists interested in critical phenomena in biological systems; researchers working on biomolecular condensates and membraneless organelles; computational biologists using MD simulations; single-molecule spectroscopists. The connection between IDP dynamics and criticality could provide a new conceptual framework for understanding how IDPs achieve functional versatility.

- **Major strengths**
  1. The study addresses an important and timely question about the physical principles underlying IDP collective behavior and phase separation.
  2. The combination of atomistic MD simulations with smFRET experiments provides complementary evidence across timescales.
  3. The observation of 1/f noise in IDP conformational fluctuations is a novel and potentially impactful finding.
  4. The power-law size distribution of residue domains and the collapse of scaled distributions across three different IDPs suggest a universal feature.
  5. The comparison with a coarse-grained polymer model provides a useful control to distinguish IDP-specific behavior from generic polymer physics.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality and statistical rigor
- **Claim pointer** The authors claim that power spectra of end-to-end distance fluctuations exhibit 1/f noise (β ≈ 1) for all three IDPs, and that this indicates scale-free temporal correlations.
- **Evidence pointer** Figure 2a, Section "The Power Spectrum of the Global Conformational Fluctuations Exhibits 1/f Noise"
- **Concern** The manuscript does not report the uncertainty in the fitted exponents β, the frequency range over which the power law holds, or the statistical significance of the deviation from white noise (β = 0) or Brownian noise (β = 2). With only 10 independent 1-µs trajectories per protein, the statistical power to distinguish β ≈ 1 from β ≈ 0.8 or β ≈ 1.2 may be limited. Additionally, the finite simulation length imposes a lower frequency cutoff that could affect the low-frequency behavior. The authors should provide confidence intervals for β, show the power spectra with fits and residuals, and demonstrate that the 1/f behavior is robust across individual trajectories rather than only in the ensemble average.
- **Why it matters** The central claim of scale-free temporal correlations and criticality hinges on the reliability of the measured exponent β. Without uncertainty quantification and demonstration of robustness, the claim that these systems exhibit 1/f noise rather than other colored noise processes is not firmly established.
- **Resolution test** Provide bootstrapped or trajectory-by-trajectory estimates of β with confidence intervals. Show that the power law holds over at least two decades of frequency with acceptable fit quality. Demonstrate that the result is insensitive to the choice of frequency range and analysis parameters.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Conceptual interpretation and alternative explanations
- **Claim pointer** The authors interpret the observed 1/f noise, power-law domain size distributions, and scale-free correlation functions as evidence that IDPs are poised at a critical state.
- **Evidence pointer** Sections "Power-Law Size Distribution of Residue Domains and Finite-Size Scaling" and "Scale-Free Behavioral Correlation Between Relative Motions of Residues"
- **Concern** The interpretation of these observations as signatures of criticality requires ruling out alternative explanations. For example, 1/f noise can arise from non-critical mechanisms such as hierarchical relaxation processes, random walks in rugged energy landscapes, or superposition of multiple relaxation timescales. Similarly, power-law distributions can emerge from multiplicative processes or other non-critical mechanisms. The authors do not provide a quantitative test of criticality, such as extracting a correlation length exponent, checking finite-size scaling in a systematic way, or demonstrating divergence of a susceptibility. The comparison with the HP polymer model is useful but the model itself may not be an appropriate control for criticality. The authors should either provide more direct evidence for criticality or temper their claims to state that the observations are "consistent with" rather than "demonstrative of" critical behavior.
- **Why it matters** The claim that IDPs are at a critical state is the central conceptual contribution of the paper. If this interpretation is not uniquely supported by the data, the significance of the work is substantially diminished.
- **Resolution test** Provide additional analyses that distinguish criticality from alternative explanations, such as measuring the correlation length as a function of system size, testing for scaling collapse with different exponents, or comparing against a broader set of non-critical null models. Alternatively, revise the language to acknowledge that criticality is one possible interpretation among several.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation and consistency
- **Claim pointer** The authors claim that smFRET experiments confirm the 1/f noise behavior observed in simulations, with an exponent β = 0.95 for FUS-C.
- **Evidence pointer** Section "Single-Molecule FRET Experiments on Conformational Fluctuations of IDPs", Figure 5
- **Concern** The experimental power spectrum is derived from FRET efficiency trajectories converted to distances. The manuscript does not report the number of photons per time bin, the time resolution of the measurements, the length of the trajectories, or the uncertainty in the fitted exponent. The conversion from FRET efficiency to distance assumes a specific relationship that may introduce artifacts. Additionally, only FUS-C and LAF-N were measured experimentally, not TAF-C, yet the conclusions are drawn for all three IDPs. The authors should report the experimental uncertainties, the number of molecules analyzed, and the trajectory lengths. They should also clarify whether the experimental timescales overlap with the simulation timescales or bridge a gap.
- **Why it matters** The experimental confirmation is a key strength of the paper, but if the experimental analysis has unquantified uncertainties or systematic biases, the claim of experimental validation is weakened.
- **Resolution test** Provide detailed experimental parameters, uncertainty estimates for β, and a demonstration that the power-law behavior is consistent across individual molecules. If possible, measure TAF-C as well to support the generality of the claim.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Methodological transparency and reproducibility
- **Claim pointer** The authors define residue domains using a k-core decomposition of contact maps, with contacts defined at a distance threshold of 0.35 nm.
- **Evidence pointer** Section "The Definition of Residue Domain"
- **Concern** The choice of the distance threshold (0.35 nm) and the k-core level (k = 2) are not justified. The results may be sensitive to these parameters. The manuscript does not report how the domain size distribution changes with different thresholds or k values. Additionally, the exclusion of contacts between neighboring residues (i and i±1) is reasonable but the rationale is not explained. The authors should perform a sensitivity analysis and show that the power-law behavior is robust to reasonable variations in these parameters.
- **Why it matters** The power-law size distribution of residue domains is a central piece of evidence for spatial scale-free correlations. If this result is an artifact of specific analysis parameters, the claim is undermined.
- **Resolution test** Perform a systematic variation of the contact distance threshold and k-core level, and show that the power-law exponent and scaling collapse are stable across a reasonable parameter range.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability and scope of claims
- **Claim pointer** The authors state that "IDPs are poised at a critical state" and that this is beneficial for IDP interactions and phase formation, implying a general property of IDPs.
- **Evidence pointer** Abstract, Conclusion
- **Concern** The study examines only three IDPs, all of which are RGG-rich and involved in phase separation. The claim of criticality as a general property of IDPs is not supported by this limited sample. Additionally, the connection between criticality and functional benefits (e.g., phase separation) is speculative and not directly tested. The authors should either restrict their claims to the specific IDPs studied or provide a broader survey of IDP sequences to support generality.
- **Why it matters** The significance of the work depends on whether the findings apply broadly to IDPs or are specific to the three proteins studied. Overgeneralization could mislead the field.
- **Resolution test** Either revise the language to limit claims to the studied systems, or include additional IDPs with diverse sequence compositions to test the generality of the observed phenomena.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 1 description
- **Evidence pointer** Section "The Power Spectrum of the Global Conformational Fluctuations Exhibits 1/f Noise"
- **Issue** The description of Figure 1 is brief and does not explain what is shown in each panel. The reader cannot assess the conformational fluctuations visually.
- **Required correction** Provide a more detailed figure legend describing each panel, the time range shown, and the color scheme used.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Mean and standard deviation values for Ree
- **Evidence pointer** Section "The Power Spectrum of the Global Conformational Fluctuations Exhibits 1/f Noise"
- **Issue** The mean values of Ree are reported as mean ± SD, but it is unclear whether the SD represents the spread across time within a single trajectory or across the 10 independent trajectories.
- **Required correction** Clarify the source of the reported standard deviation and report the number of independent samples used.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Force field validation
- **Evidence pointer** Section "Computational Details"
- **Issue** The a99SB-disp force field is used, but no validation is provided that this force field reproduces known IDP properties for the specific proteins studied.
- **Required correction** Cite prior validation studies or provide a brief comparison with experimental data (e.g., radius of gyration from SAXS) to justify the force field choice.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation of polymer model comparison
- **Evidence pointer** Section "Power-Law Size Distribution of Residue Domains and Finite-Size Scaling"
- **Issue** The HP polymer model is used as a comparison, but the model parameters (e.g., interaction strengths, chain length) are not described in the main text. The reader cannot assess whether the comparison is appropriate.
- **Required correction** Provide the model parameters in the main text or refer to the Supporting Information with a clear description.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Experimental reproducibility
- **Affected element** smFRET data analysis
- **Evidence pointer** Section "Single-Molecule Förster Resonance Energy Transfer (sm-FRET) Experiments"
- **Issue** The manuscript does not describe how FRET efficiency histograms were constructed, how the mean efficiency was determined, or how the distance trajectories were filtered for quality.
- **Required correction** Add a description of the data analysis pipeline, including any selection criteria applied to the trajectories.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction, Conclusion
- **Issue** The manuscript does not discuss prior work on criticality in biological systems in sufficient depth, nor does it compare the present findings with previous studies on IDP dynamics that may have observed similar phenomena.
- **Required correction** Expand the discussion to place the findings in the context of existing literature on criticality in biology and IDP dynamics.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Terminology precision
- **Affected element** Use of the term "critical state"
- **Evidence pointer** Throughout
- **Issue** The term "critical state" is used repeatedly, but the authors do not define what constitutes a critical state in this context or what specific observable would definitively indicate criticality.
- **Required correction** Provide a clear operational definition of criticality as used in this work, and state what evidence would be required to confirm or refute it.

## Risk / unsupported claims
- The claim that IDPs are "poised at a critical state" is an interpretation that is not uniquely supported by the presented evidence. Alternative explanations for 1/f noise and power-law distributions are not ruled out.
- The claim that criticality "allows IDPs to effectively respond to finite differences in residue compositions" is speculative and not directly tested in this work.
- The claim that the observed scale-free correlations are "beneficial for IDP interactions and phase formation" is not experimentally or computationally demonstrated.
- The generalizability of the findings to all IDPs is not supported, as only three RGG-rich IDPs were studied.
- The statement that "the consistency of our simulation and experimental results suggests that the self-similarity of IDP conformational dynamics is valid across extensive timescales, spanning from nanoseconds to seconds" is not fully supported because the experimental and simulation timescales may not overlap, and the comparison is indirect.
- The claim that the polymer model "shares similar large conformational fluctuations and Flory exponent with IDP" is stated but the quantitative comparison is not shown in the provided text.