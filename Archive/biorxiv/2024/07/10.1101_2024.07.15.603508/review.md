## Review setup
- **Input scope** Full manuscript text, abstract, methods, and supporting information descriptions
- **Assessment boundary** Scientific content, methodological rigor, claims versus evidence, and presentation quality
- **Shared manuscript claim summary** The authors use atomistic MD simulations of FUS-LCD in condensate and dilute phases to show that protein dynamics are heterogeneously slowed in the condensate: large-scale translational and orientational motions are retarded by up to two orders of magnitude, while small-scale local motions (Cα distance fluctuations, side-chain rotamer jumps) are only modestly affected (about twofold). Water dynamics in the protein hydration layer are slowed approximately twofold for single-molecule rotations and more strongly for collective relaxation.
- **Visible evidence base** Main text figures (Figures 1-4), supplementary figure descriptions (Figures S1-S9), methods section, and simulation details
- **Missing materials affecting confidence** Actual figure data files, numerical values for correlation times and ratios, error bar definitions, convergence analysis, force field validation details, and the full supporting information document

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question in the biophysics of biomolecular condensates: how does the dense condensate environment differentially affect various modes of protein dynamics? The authors use state-of-the-art atomistic MD simulations of a biologically relevant system (FUS-LCD) and provide a mode-resolved analysis of dynamical retardation. The central finding, that dynamical slowdown is heterogeneous and length-scale dependent, is physically plausible and consistent with some prior experimental observations. However, the manuscript has several technical and presentational issues that need to be addressed before the conclusions can be fully accepted. The distinction between translational, orientational, and internal distance dynamics is conceptually useful, but the interpretation of some correlation functions and the connection to experimental observables could be strengthened. The water dynamics analysis, while interesting, is somewhat disconnected from the main narrative and would benefit from clearer motivation and interpretation.

- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, intrinsically disordered proteins, and computational biophysics would find these results of direct interest. The work provides molecular-level insights into how condensate environments modulate protein dynamics, which is relevant for understanding the physical basis of condensate function and material properties. The mode-resolved analysis approach could also be of methodological interest to the MD simulation community studying crowded and confined environments. Experimental groups using NMR, fluorescence, or vibrational spectroscopy to probe dynamics in condensates would find the predictions testable and useful for interpreting their data.

- **Major strengths** The study addresses a significant and timely question with a well-chosen model system. The mode-resolved analysis of dynamics (translational, orientational, distance fluctuations, side-chain rotamers, water) provides a comprehensive picture that goes beyond simple diffusion measurements. The use of atomistic MD simulations with a force field previously validated for FUS is appropriate. The comparison between dilute and condensate conditions is clean and well-controlled. The finding that different dynamical modes respond differently to the condensate environment is an important contribution that helps reconcile seemingly conflicting experimental observations.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that translational diffusion in the condensate is slowed by up to two orders of magnitude based on MSD analysis of Cα atoms.
- **Evidence pointer** Figure 1A, Figure S2, "location not provided" for specific values
- **Concern** The MSD analysis for translational diffusion in a condensate system of only 8.9 nm box size (containing 8 protein chains) may be severely affected by finite-size effects and periodic boundary conditions. The mean squared displacement of Cα atoms at long lag times will be limited by the box size, and the apparent "up to two orders of magnitude" slowdown could be an artifact of the confined simulation box rather than a genuine physical effect. The authors should estimate the maximum accessible mean-square displacement before finite-size effects become dominant and verify that the linear regime of the MSD is properly identified. Additionally, the diffusion coefficient of 0.26 x 10^-3 nm^2/ns is derived from a linear fit, but the fitting range and its statistical uncertainty are not reported.
- **Why it matters** The central quantitative claim of the paper, that translational dynamics are slowed by up to two orders of magnitude, depends critically on the reliability of the MSD analysis. If finite-size effects are significant, the magnitude of the reported slowdown could be substantially overestimated, undermining the main conclusion.
- **Resolution test** Provide a systematic analysis of finite-size effects, including MSD plots with clear indication of the diffusive regime, block averaging or multiple independent simulations to estimate statistical errors, and a discussion of how the box size compares to the relevant length scales of the system. If possible, repeat the analysis with a larger box or use alternative methods to extract diffusion coefficients that are less sensitive to finite-size effects.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that orientational dynamics of Cα-Cα vectors are slowed by approximately 5-15 fold in the condensate, while distance fluctuations show no noticeable slowdown.
- **Evidence pointer** Figure 2, "location not provided" for specific values
- **Concern** The interpretation of the orientational correlation functions and distance fluctuation correlation functions is not fully clear. For orientational dynamics, the correlation function of Cα-Cα vectors at different sequence separations mixes internal chain dynamics with overall tumbling of the chain. In a condensate, the effective "tumbling" of the entire chain is expected to be much slower than in dilute solution, which could dominate the observed slowdown for large separations. The authors should separate overall rotational diffusion from internal chain dynamics, for example by analyzing the correlation functions in the molecular frame or by removing the overall rotation of each chain. Similarly, for distance fluctuations, the correlation function measures the relaxation of the distance magnitude, but the interpretation in terms of "local motions around average positions" needs more careful justification.
- **Why it matters** The distinction between large-scale and small-scale dynamical slowdown is a key conclusion of the paper. If the observed slowdown in orientational dynamics is dominated by overall chain tumbling rather than internal modes, the interpretation of length-scale-dependent heterogeneity would need to be revised.
- **Resolution test** Perform a mode decomposition of the chain dynamics (e.g., using principal component analysis or normal mode analysis) to separate overall rotation from internal dynamics. Alternatively, analyze the correlation functions after removing the center-of-mass and overall rotation of each chain. Provide a clear physical interpretation of what each correlation function measures and how the reported time scales relate to specific dynamical modes.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that the heterogeneous retardation of dynamics supports the notion of liquid-like character of condensates and that the findings might be transferable to other biocondensates.
- **Evidence pointer** Abstract, Conclusion, "location not provided"
- **Concern** The connection between the observed dynamical heterogeneity and the liquid-like character of condensates is not well developed. The authors show that different modes are slowed to different extents, but do not provide a mechanistic framework for why this should be the case or how it relates to the material properties of the condensate (e.g., viscosity, elasticity, mesh size). The claim of transferability to other biocondensates is speculative without a broader comparative analysis or a theoretical model that would allow prediction of dynamical behavior in other systems.
- **Why it matters** The broader significance of the work, beyond the specific FUS-LCD system, depends on whether the findings can be generalized. Without a mechanistic framework or comparative analysis, the generalizability of the conclusions remains uncertain.
- **Resolution test** Provide a more quantitative connection between the observed dynamical slowdown and the physical properties of the condensate (e.g., using the Stokes-Einstein relation or mode-coupling theory). Discuss how the results might apply to other IDP condensates with different sequence compositions or interaction strengths. If possible, compare with experimental measurements of dynamics in condensates to validate the predictions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that water dynamics in the protein hydration layer are slowed by a factor of two for single-molecule rotations and more strongly for collective relaxation.
- **Evidence pointer** Figure 4, "location not provided" for specific values
- **Concern** The water dynamics analysis has several potential issues. First, the definition of the protein hydration layer (within 0.5 nm of the protein surface) is reasonable but the sensitivity of the results to this cutoff should be tested. Second, tracking only water molecules that remain within the hydration layer for the duration of the analysis introduces a selection bias, as these are likely the most strongly bound waters. Third, the collective dipole correlation function C_M(t) includes contributions from both water rotation and water exchange between the hydration layer and the bulk, which complicates the interpretation. The triexponential fit for C_M(t) is mentioned but the physical meaning of the three components is not discussed.
- **Why it matters** The water dynamics results are presented as an additional finding, but if the analysis is biased or the interpretation is unclear, it could detract from the main conclusions rather than strengthen them.
- **Resolution test** Test the sensitivity of the results to the hydration layer definition (e.g., 0.4 nm, 0.6 nm). Provide a more detailed analysis of the water dynamics, including residence times and exchange rates. Discuss the physical meaning of the different exponential components in the collective correlation function.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Introduction
- **Evidence pointer** "location not provided"
- **Issue** The introduction is somewhat lengthy and covers a broad range of topics. The transition from general condensate biology to the specific question of dynamical heterogeneity could be streamlined.
- **Required correction** Consider condensing the introduction to focus more directly on the question of dynamics in condensates and the specific gap this work addresses.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods
- **Evidence pointer** "location not provided"
- **Issue** The methods section mentions that the initial condensate system was obtained from coarse-grained simulations with scaled protein-protein interactions, but the scaling factor is not specified. This is important for reproducibility.
- **Required correction** Provide the specific scaling factor used for the protein-protein Lennard-Jones interactions in the coarse-grained simulations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure 2
- **Evidence pointer** "location not provided"
- **Issue** The authors mention that error bars have been added to Figure 2 and Figure 3, but the definition of the error bars (standard deviation, standard error, confidence interval) and the number of independent samples used are not stated.
- **Required correction** Clearly state the definition of error bars and the statistical methodology used to compute them.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Results
- **Evidence pointer** "location not provided"
- **Issue** The manuscript contains some typographical errors and awkward phrasing (e.g., "ins FUS condensates" in the results section).
- **Required correction** Careful proofreading is needed to correct typographical errors and improve sentence flow.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods
- **Evidence pointer** "location not provided"
- **Issue** The simulation protocol uses a 2 fs time step with constraints on protein bonds and water internal degrees of freedom. This is standard, but the choice of the velocity rescaling thermostat with a stochastic term and the Berendsen barostat should be justified, as the Berendsen barostat is known to not produce the correct ensemble.
- **Required correction** Justify the choice of the Berendsen barostat or consider using a more accurate barostat (e.g., Parrinello-Rahman) for the production runs.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Abstract
- **Evidence pointer** "location not provided"
- **Issue** The abstract states that large-amplitude motions are "strongly slowed by up to two orders of magnitude" but does not specify which motions exactly. This could be clarified.
- **Required correction** Specify in the abstract which dynamical modes show the largest slowdown (e.g., translational diffusion of the protein chains).

## Risk / unsupported claims
- The claim that the results "might be transferable to other biocondensates" is speculative and not supported by comparative data or a generalizable theoretical framework.
- The claim that the findings "support the notion of a liquid-like character of the condensates" is not directly tested; the authors do not measure or estimate material properties such as viscosity or elasticity.
- The quantitative magnitude of the translational slowdown (up to two orders of magnitude) may be affected by finite-size effects and should be treated with caution until the analysis is verified.
- The interpretation of the orientational correlation functions as reflecting internal chain dynamics versus overall tumbling is not fully resolved.
- The water dynamics analysis relies on a specific definition of the hydration layer and a selection criterion for water molecules that may bias the results.

## Assessment against Nature-style criteria
- **Originality** The work is original in its mode-resolved analysis of dynamical heterogeneity in condensates. While previous studies have examined diffusion in crowded environments, the systematic separation of translational, orientational, and internal distance dynamics in a condensate system is a novel contribution.
- **Scientific importance** The question of how condensate environments modulate protein dynamics is of significant importance for understanding condensate function, material properties, and the physical chemistry of phase-separated systems. The findings have implications for interpreting experimental measurements of dynamics in condensates.
- **Interdisciplinary readership** The topic bridges biophysics, physical chemistry, and cell biology. The results would be of interest to researchers in these fields, though the technical nature of the analysis may limit accessibility to a broader biological audience.
- **Technical soundness** The simulation methodology is generally appropriate, but several technical concerns (finite-size effects, interpretation of correlation functions, water dynamics analysis) need to be addressed to fully establish the conclusions.
- **Readability for nonspecialists** The manuscript is reasonably well-written but assumes familiarity with MD simulation techniques and correlation function analysis. The abstract is accessible, but the results section would benefit from clearer explanations of the methods and their physical meaning.

## Recommendation posture
Supportive if technical concerns are resolved. The central finding of heterogeneous dynamical slowdown in condensates is interesting and potentially important, but the quantitative claims need to be verified against finite-size effects, and the interpretation of the correlation functions needs to be clarified. If these issues are addressed, the work would be a valuable contribution to the field.