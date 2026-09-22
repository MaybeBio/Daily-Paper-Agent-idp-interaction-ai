## Review setup
- **Input scope** Full manuscript text, including abstract, main text, methods, figure legends, and supplementary information descriptions.
- **Assessment boundary** Scientific content, technical soundness, and clarity of claims as presented in the provided text. No assessment of formatting, grammar, or editorial style beyond what affects scientific comprehension.
- **Shared manuscript claim summary** The authors use single-fluorogen imaging (blinking-based super-resolution and single-molecule tracking) with solvatochromic dyes (NR, NB, MC540) to probe the internal and interfacial environments of biomolecular condensates formed by intrinsically disordered proteins (A1-LCD variants and DDX4). They report that condensates are spatially inhomogeneous, containing nanoscale "hubs" that are more hydrophobic, more crosslinked, and slower-moving than surrounding regions, and that interfaces have distinct orientational properties. These findings are interpreted as experimental support for simulation predictions of network-like, inhomogeneous condensate structure.
- **Visible evidence base** Main text figures 1–6 (described in text), Extended Data Figures 1–10 (referenced), Supplementary Figures 1–7, Supplementary Tables 1–5, Supplementary Videos 1–5, Methods section.
- **Missing materials affecting confidence** Actual figure images, numerical data values, statistical test outputs, and source data are not provided. The full Methods section is present but some details (e.g., exact dye concentrations in single-molecule experiments, photophysical characterization of dyes in condensates) are only partially described. Supplementary information content is listed but not fully visible.

## Reviewer
- **Overall assessment** This manuscript presents a technically sophisticated application of single-molecule fluorescence imaging to a question of significant current interest in the condensate field. The use of solvatochromic fluorogens as environmentally sensitive probes is creative and the combination of super-resolution localization, single-molecule tracking, and orientation measurements is powerful. The central claim that condensates are spatially inhomogeneous at the nanoscale, with distinct hydrophobic hubs, is plausible and consistent with some prior simulation work. However, the manuscript as presented has several important gaps. The quantitative rigor of the analysis is not fully demonstrated from the provided text, particularly regarding the interpretation of dye blinking as a proxy for protein organization, the calibration of dye response to hydrophobicity, and the statistical robustness of the clustering and orientation measurements. The connection between dye behavior and specific molecular features (e.g., aromatic residue content) is suggestive but correlative. The generalizability of the findings beyond A1-LCD is only briefly addressed. The manuscript would be strengthened by more explicit controls, clearer quantitative comparisons, and a more cautious framing of the inferences drawn from dye behavior.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, and intrinsically disordered proteins would be the primary audience. The work is also relevant to those developing and applying single-molecule imaging techniques, super-resolution microscopy, and solvatochromic probes. The findings on nanoscale inhomogeneity and hydrophobicity could inform biophysical models of condensate structure and function, and the methodological approach could be adopted by others studying similar systems.
- **Major strengths**
  1. The experimental approach is innovative, combining multiple single-molecule modalities (localization, tracking, orientation) with environmentally sensitive dyes to probe condensate properties at the nanoscale.
  2. The study directly tests computational predictions about inhomogeneous condensate structure, providing a valuable experimental counterpart to existing theory.
  3. The use of multiple dye types (NR, NB, MC540) with different properties and localizations (interior vs. interface) is a thoughtful design that allows cross-validation of some findings.
  4. The inclusion of simulation data (LaSSI) to support the interpretation of dye behavior in terms of crosslinking is a useful complement.
  5. The work addresses a fundamental question about the internal organization of condensates that has been difficult to access experimentally.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / Interpretation
- **Claim pointer** The authors claim that nanoscale "hubs" revealed by dye blinking correspond to clusters of crosslinked protein molecules, and that differences in dye behavior (e.g., burst duration, speed) directly reflect differences in local protein density and crosslinking.
- **Evidence pointer** Figures 2, 3, 4; Extended Data Figures 4, 5, 6; Methods sections on single-molecule detection and tracking.
- **Concern** The interpretation of dye blinking dynamics as a direct readout of protein organization requires that the dye's photophysical behavior (blinking rate, burst duration, brightness) is primarily determined by the local protein environment in a predictable and calibrated manner. The manuscript does not provide sufficient evidence for this calibration. For example, how does the dye's blinking behavior in a homogeneous solution of known hydrophobicity compare to that in condensates? How do dye-dye interactions, dye concentration, or local viscosity affect the measurements? The correlation between dye burst duration and protein crosslinking is inferred from simulations, but the direct experimental link is not established. The authors should provide control experiments showing that dye behavior is specifically responsive to the features they claim to measure (e.g., hydrophobicity, crosslink density) and not to other factors.
- **Why it matters** If the dye behavior is not a faithful reporter of the claimed molecular features, the central conclusions about nanoscale inhomogeneity and its structural basis are not supported. The entire interpretive framework rests on this assumption.
- **Resolution test** Provide calibration experiments showing dye blinking parameters (burst duration, on/off rates) as a function of controlled solvent hydrophobicity, viscosity, and protein concentration. Show that the observed differences between hubs and non-hub regions are consistent with these calibrations and cannot be explained by other factors (e.g., dye aggregation, local pH, oxygen concentration). Ideally, correlate dye-based measurements with an independent structural readout (e.g., FRET, cryo-EM, or super-resolution imaging of labeled protein).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / Statistical rigor
- **Claim pointer** The authors report quantitative differences in burst durations, speeds, clustering coefficients, and orientation angles between different condensate types (Aro−, WT, Aro+) and between hubs and non-hub regions, with associated p-values.
- **Evidence pointer** Figures 2d, 2f, 3h, 3i, 4b, 4d, 4e, 5e; Methods section on statistics.
- **Concern** The statistical analysis is not described in sufficient detail to assess its validity. For example, how many condensates, how many localizations per condensate, and how many independent biological replicates were used for each comparison? The p-values are reported, but the specific test used, whether corrections for multiple comparisons were applied, and whether the data meet the assumptions of the test (e.g., normality) are not stated. The use of "mean ± s.d." for burst durations and speeds, which are likely highly skewed distributions, may be inappropriate. The authors should provide more detailed statistical reporting, including effect sizes, confidence intervals, and information about data distribution.
- **Why it matters** Without rigorous statistical validation, the reported differences between conditions (e.g., Aro+ vs. Aro−) may not be robust, and the conclusions drawn from them are weakened.
- **Resolution test** Provide a detailed description of the statistical methods, including the specific tests used, the number of replicates, and how the data were determined to meet test assumptions. Show the full distributions of the measured parameters, not just means and s.d. Consider using non-parametric tests or data transformations if the data are not normally distributed. Report effect sizes and confidence intervals for all key comparisons.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability / Scope of claims
- **Claim pointer** The authors state that their findings "provide a structural and dynamical basis for the viscoelasticity of condensates" and imply that the observed inhomogeneous organization is a general feature of condensates formed by IDPs.
- **Evidence pointer** Abstract; Figures 2–5; Extended Data Figure 10.
- **Concern** The primary data are from A1-LCD and its variants, with a brief mention of DDX4. The claim of generalizability to "biomolecular condensates" broadly is not supported by the data presented. The behavior of dyes in condensates formed by different proteins with different sequence features, and in more complex multi-component condensates, is not explored. The connection between the observed nanoscale structure and macroscopic viscoelasticity is made qualitatively, but no direct rheological measurements are presented to support this link.
- **Why it matters** The title and abstract make broad claims that go beyond the specific experimental system. Overstating the generalizability of the findings could mislead readers and overstate the significance of the work.
- **Resolution test** Either temper the claims to be specific to the systems studied, or provide additional data on other IDP systems and, ideally, direct measurements of viscoelasticity (e.g., microrheology) on the same samples to establish the proposed link.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness / Control experiments
- **Claim pointer** The authors state that the fluorogenic probes are "non-perturbative" and have "negligible effects" on condensate properties, based on measurements of csat.
- **Evidence pointer** Extended Data Figure 2; Methods section on csat measurements.
- **Concern** The csat measurements are a useful control, but they may not be sensitive to all potential perturbations. For example, the dyes could affect the internal dynamics, viscosity, or nanoscale organization of the condensate without significantly changing the saturation concentration. The manuscript does not report other controls, such as testing whether dye binding alters protein diffusion or the size distribution of hubs. The claim of "non-perturbative" is too strong based on the evidence provided.
- **Why it matters** If the dyes perturb the system in ways not captured by csat measurements, the measured properties (e.g., hub size, dynamics) may be artifacts of dye binding rather than intrinsic features of the condensate.
- **Resolution test** Perform additional control experiments to assess the impact of dye binding on condensate properties. For example, compare the diffusion of labeled protein (e.g., via HaloTag or SNAP-tag) in the presence and absence of dyes. Measure the size and dynamics of hubs as a function of dye concentration to check for concentration-dependent effects. Use dyes with different structures to see if the observed features are dye-specific or general.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness / Methodological details
- **Claim pointer** The authors use single-molecule orientation-localization microscopy (SMOLM) to measure the orientation of MC540 at condensate interfaces and infer that the dye has a preferred orientation parallel to the interface.
- **Evidence pointer** Figure 5; Extended Data Figure 8; Methods section on SMOLM.
- **Concern** The interpretation of MC540 orientation as reporting on the local protein organization at the interface is complex. The dye's orientation could be influenced by the local electrostatic environment, the curvature of the interface, or the specific binding mode to the protein. The manuscript does not provide sufficient detail on how the orientation measurements were calibrated and validated, or how potential artifacts (e.g., dipole defocusing, molecule wobble) were accounted for. The comparison with simulations (Figure 5f) is useful but the simulation model may not capture all relevant features of the interface.
- **Why it matters** The interfacial orientation measurements are a novel and potentially important contribution, but if the methodology is not rigorously validated, the conclusions about interfacial structure are uncertain.
- **Resolution test** Provide more detailed validation of the SMOLM measurements, including simulations of expected PSF shapes for known orientations, control experiments with dyes in isotropic environments, and a discussion of potential artifacts. Show that the measured orientation distributions are stable across different imaging conditions and are not affected by dye concentration or photobleaching.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity / Presentation
- **Affected element** Figure 1c
- **Evidence pointer** Figure 1c and associated text.
- **Issue** The partition coefficients are reported as medians with shaded probability densities, but the number of measurements and the variability between individual condensates are not clearly shown. The text mentions "~50 distinct measurements" but it is unclear if this is for each dye or combined.
- **Required correction** Clarify the number of measurements for each dye and show the full distribution of partition coefficients, perhaps as a scatter plot overlaid on the density plot. Report the interquartile range or other measures of variability.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity / Terminology
- **Affected element** Figure 2e, Methods section on clustering
- **Evidence pointer** Figure 2e; Methods section on clustering coefficient.
- **Issue** The term "clustering coefficient" is used, but the specific definition and threshold (value of 20) are not clearly explained in the main text. The relationship between the clustering coefficient and the physical concept of a "hub" could be clarified.
- **Required correction** Provide a brief explanation of the clustering coefficient in the main text or figure legend, and justify the choice of threshold. Consider showing how the results depend on the threshold choice.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity / Presentation
- **Affected element** Figure 3e
- **Evidence pointer** Figure 3e and associated text.
- **Issue** The speed distribution is shown, but the criteria for classifying emitters as "high," "medium," or "low" speed are not clearly defined. The cutoffs appear arbitrary.
- **Required correction** Define the speed categories explicitly and justify the cutoffs. Consider showing the results as a continuous function of speed rather than discrete categories.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness / References
- **Affected element** Discussion of dye photophysics
- **Evidence pointer** Extended Data Figure 1; Methods section.
- **Issue** The photophysical mechanisms underlying the fluorogenic behavior of NR, NB, and MC540 in different environments are not discussed in detail. A brief explanation of why these dyes become fluorescent in hydrophobic environments would help readers understand the basis of the measurements.
- **Required correction** Add a brief discussion of the photophysics of the dyes, possibly in the Methods or Extended Data, explaining the relationship between environment and fluorescence.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity / Interpretation
- **Affected element** Figure 6 and associated text
- **Evidence pointer** Figure 6; Discussion section.
- **Issue** The schematic in Figure 6 is helpful, but the distinction between "hubs" and the "background" of the condensate could be more clearly defined. The text mentions "sponge-like appearance" but does not fully explain what this means structurally.
- **Required correction** Expand the discussion of the proposed structural model, clarifying the relationship between hubs, the surrounding network, and the overall condensate architecture.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness / Data availability
- **Affected element** Methods section on statistics
- **Evidence pointer** Methods section.
- **Issue** The statement "No statistical method was used to predetermine sample size" is standard but the lack of a power analysis is a limitation. The number of condensates and localizations used for each analysis should be explicitly stated in the figure legends.
- **Required correction** Add the number of condensates and localizations to each figure legend, and consider adding a supplementary table summarizing all sample sizes.

## Risk / unsupported claims
- The claim that the observed nanoscale inhomogeneities "provide a structural and dynamical basis for the viscoelasticity of condensates" is not directly supported by the data, as no rheological measurements are presented.
- The claim that the findings apply broadly to "biomolecular condensates" is not supported, as only A1-LCD variants and DDX4 were studied.
- The assertion that the dyes are "non-perturbative" is only supported by csat measurements, which may not capture all potential perturbations.
- The interpretation of dye blinking dynamics as a direct readout of protein crosslinking density is not fully calibrated or validated.
- The claim that MC540 orientation reports on protein orientation at the interface is plausible but not rigorously validated.
- The generalizability of the findings to condensates with different sequence compositions, sizes, or in cellular contexts is not addressed.