## Review setup
- **Input scope** Full manuscript text (Abstract, Introduction, Results, Discussion, Methods) as provided
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the supplied text; no external data or supplementary figures were available for verification
- **Shared manuscript claim summary** The authors propose that the bulk viscosity of biomolecular condensates formed by complex coacervation of highly charged disordered proteins is quantitatively linked to nanoscale chain dynamics (reconfiguration times) and microscale translational diffusion via the Rouse model with entanglement corrections. They support this with single-molecule FRET, fluorescence correlation spectroscopy, microrheology, and atomistic molecular dynamics simulations, and suggest the framework generalizes to other condensates and synthetic polyelectrolytes.
- **Visible evidence base** Main text figures referenced (Figures 1–4), supplementary figures referenced (Figures S1–S7), methods summary, and prior validation cited (reference 41)
- **Missing materials affecting confidence** Supplementary figures and detailed methods not provided; raw data, error bars, statistical analyses, and simulation convergence metrics not accessible; details of fitting procedures and parameter estimation for Eqs. 1–5 not fully specified

## Reviewer
- **Overall assessment** This manuscript addresses a fundamental question in the biophysics of biomolecular condensates: how nanoscale molecular dynamics give rise to mesoscale material properties. The authors present a compelling correlation between experimentally measured chain reconfiguration times, translational diffusion, and bulk viscosity across a series of model coacervates, and they propose a quantitative framework based on the Rouse model with entanglement corrections. The inclusion of atomistic simulations to provide mechanistic insight is a strength. However, the manuscript's central claim of a universal predictive link rests on a limited number of systems, and the quantitative agreement between theory and experiment is stated to be within an order of magnitude, which warrants careful scrutiny. The generalizability to other condensate types is asserted rather than demonstrated. The work is potentially significant but requires additional validation and clarification before the case is fully established.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, polymer physics, and cellular biophysics would be interested. The work provides a potential framework for predicting material properties from molecular-level measurements, which is relevant for understanding condensate function in health and disease. The methodological combination of single-molecule FRET, FCS, microrheology, and MD simulations is of broad interest to the biophysical community.
- **Major strengths** 1. The study addresses a key open question in the field with a multi-scale experimental and computational approach. 2. The use of a well-defined model system (ProTα with different polycations) allows systematic variation of interaction strength. 3. The proposed Rouse-based framework is conceptually simple and potentially powerful. 4. The inclusion of atomistic simulations provides mechanistic depth. 5. The comparison with literature data on other condensates and synthetic polyelectrolytes suggests broader applicability.
- **Major Concerns** 
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The authors claim that "analytical relations from polymer physics can predict condensate viscosity from diffusivity and chain dynamics, and vice versa" and that this provides a "universal link" across systems.
  - **Evidence pointer** Figure 4D, Eqs. 1–5, Discussion
  - **Concern** The quantitative agreement between the Rouse model predictions and experimental viscosities is stated to be "within an order of magnitude" (Results, "Universal link" section). This is a wide margin that may not convincingly establish the predictive power claimed. The fit for the tube diameter a yields 4 ± 2 nm, which overlaps with the independent estimate of 3 ± 1 nm, but the uncertainty is large. The manuscript does not provide a statistical measure of the goodness of fit or a quantitative comparison of predicted versus measured values across all systems.
  - **Why it matters** The central claim of the paper is that viscosity can be predicted from molecular dynamics. If the agreement is only within an order of magnitude, the predictive utility is limited, and alternative explanations for the observed correlations (e.g., both quantities scaling with interaction strength) cannot be excluded. The claim of universality requires a more rigorous quantitative test.
  - **Resolution test** Provide a quantitative comparison of predicted and measured viscosities for all systems, including error bars and a statistical measure (e.g., R², chi-squared). Show that the model outperforms simpler scaling relationships. If possible, test the prediction on an independent system not used to calibrate the model.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Generalizability
  - **Claim pointer** The authors state that the Rouse framework "may provide a simple universal link" and that existing data on other condensates (LAF-1, A1-LCD, FUS-LCD) and synthetic polyelectrolytes are "in line with" the behavior of the studied coacervates.
  - **Evidence pointer** Figure 4D, Discussion
  - **Concern** The comparison with literature data is presented qualitatively ("in line with") without a detailed analysis. The systems cited (LAF-1, A1-LCD, FUS-LCD) are driven by different interactions (e.g., hydrophobic, pi-pi) than the electrostatic coacervates studied here. The synthetic polyelectrolyte system has viscosities six orders of magnitude higher, and it is unclear whether the same Rouse framework with the same parameters applies. The claim of universality is therefore not adequately supported by the evidence presented.
  - **Why it matters** The generalizability of the proposed framework is a key selling point of the paper. If the framework only applies to a narrow class of electrostatically driven coacervates, its significance is reduced. The authors need to demonstrate, not just assert, that the framework holds across different interaction types and timescales.
  - **Resolution test** Provide a quantitative re-analysis of the literature data using Eqs. 1–5, with clear assumptions and parameter choices. Show that the model captures the viscosity-diffusion relationship for these systems within a defined error margin. Discuss any deviations and their implications.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Methodological transparency
  - **Claim pointer** The authors use single-molecule FRET to measure reconfiguration times and FCS to measure translational diffusion, and microrheology to measure viscosity. They state that "the details of single-molecule experiments, concentration, viscosity, diffusion coefficient measurements, and the experimental setup have been described before" (Methods).
  - **Evidence pointer** Methods, Figure 2
  - **Concern** The manuscript relies heavily on previously published methods (reference 41) for key experimental procedures. While this is acceptable practice, the current manuscript does not provide sufficient detail on how the measurements were adapted to the new systems (e.g., protamine, K50, R50). For instance, the labeling positions for ProTα are given, but the labeling positions for the polycations (if any) are not specified. The concentration of labeled vs. unlabeled protein in the droplets is mentioned, but the potential effects of labeling on phase separation or dynamics are not discussed. The analysis of FCS data to extract diffusion times in a dense, viscous environment is not described.
  - **Why it matters** The validity of the experimental measurements is foundational to the paper's conclusions. Without sufficient methodological detail, the reader cannot assess the reliability of the reported reconfiguration times, diffusion coefficients, and viscosities. This is particularly important given the wide range of timescales reported (hundreds of ns to tens of μs).
  - **Resolution test** Provide a more detailed description of the experimental methods in the main text or supplementary information, including sample preparation, data acquisition parameters, and analysis procedures. Address potential artifacts such as dye photophysics, triplet states, and concentration effects.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Simulation validation
  - **Claim pointer** The authors use atomistic MD simulations to show that "the observed differences in friction reflect differences in inter-residue contact lifetimes as a function of arginine content and salt concentration."
  - **Evidence pointer** Figure 3, Methods
  - **Concern** The simulation systems are described as "recently validated" (reference 41), but the current manuscript does not provide details on the simulation length, equilibration, or convergence. The authors acknowledge that "complete equilibration of the protamine-ProTα simulations is challenging," which raises concerns about the reliability of the contact lifetime estimates for this system. The relationship between contact lifetimes and friction is inferred, not directly measured.
  - **Why it matters** The simulations are used to provide a mechanistic explanation for the experimental observations. If the simulations are not well-equilibrated or converged, the derived contact lifetimes and their correlation with reconfiguration times may be unreliable, undermining the proposed mechanism.
  - **Resolution test** Provide details on simulation length, equilibration criteria, and convergence checks. Show that the contact lifetimes are stable over the simulation time. If possible, validate the contact lifetime estimates against experimental measurements or more rigorous sampling methods.
- **Minor Comments** 
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Figure 1E
  - **Evidence pointer** Figure 1E
  - **Issue** The phase diagrams in Figure 1E are mentioned but not described in detail. It is unclear what the axes represent and how the phase boundaries were determined.
  - **Required correction** Provide a clear description of the phase diagram axes and the method used to determine phase boundaries in the figure legend or main text.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** Abstract, Introduction
  - **Evidence pointer** Abstract, Introduction
  - **Issue** The term "complex coacervation" is used without a definition. While likely familiar to specialists, a brief definition would improve accessibility for a broader readership.
  - **Required correction** Add a brief definition of complex coacervation when first used.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Data presentation
  - **Affected element** Figure 2J
  - **Evidence pointer** Figure 2J
  - **Issue** The correlations shown in Figure 2J are described as "remarkably high," but no correlation coefficients or statistical significance values are provided in the text.
  - **Required correction** Report the correlation coefficients (e.g., Pearson's r) and p-values for the correlations shown in Figure 2J.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Discussion
  - **Evidence pointer** Discussion
  - **Issue** The discussion of condensates not expected to follow the Rouse model (e.g., those with structured molecules or persistent crosslinks) is brief and lacks specific examples or references.
  - **Required correction** Expand this section with specific examples and relevant citations to strengthen the discussion of the framework's limitations.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Notation
  - **Affected element** Eq. 1
  - **Evidence pointer** Eq. 1
  - **Issue** The notation in Eq. 1 uses R² for mean squared end-to-end distance, which could be confused with the coefficient of determination. The text uses 〈R²〉, but the equation does not.
  - **Required correction** Use consistent notation, e.g., 〈R²〉, in the equation and text.
  - **Concern ID** R1-m6
  - **Severity** Minor
  - **Axis** Units
  - **Affected element** Methods, Results
  - **Evidence pointer** Methods, Results
  - **Issue** The units for viscosity (Pa·s or cP) and diffusion coefficients (m²/s or μm²/s) are not consistently specified.
  - **Required correction** Ensure all physical quantities are reported with appropriate units throughout the text and figures.

## Risk / unsupported claims
- The claim of a "universal link" between nanoscale, microscale, and mesoscale dynamics is not fully supported by the data presented, as the quantitative agreement is within an order of magnitude and the generalizability to other systems is asserted rather than demonstrated.
- The statement that "the Rouse framework is more generally applicable" to other condensates and synthetic polyelectrolytes is based on a qualitative comparison with literature data and lacks a rigorous quantitative analysis.
- The mechanistic interpretation that contact lifetimes determine friction is inferred from simulations that are acknowledged to be challenging to equilibrate; this inference is plausible but not definitively established.
- The prediction of reconfiguration times for other IDPs (LAF-1, A1-LCD, FUS-LCD) is based on extrapolation and is not validated against experimental measurements.
- The claim that "the viscous component of the shear relaxation modulus is dominant" for the studied coacervates is based on limited microrheological measurements and may not hold at all timescales.

## Assessment against Nature-style criteria
- **Originality** The work is original in its attempt to provide a quantitative, predictive framework linking molecular dynamics to material properties in condensates. While the Rouse model is well-established in polymer physics, its application to biomolecular condensates with experimental validation is novel.
- **Scientific importance** The question of how molecular interactions determine condensate material properties is of central importance to the field. A validated predictive framework would be highly impactful. However, the current evidence does not fully establish the framework's predictive power, limiting its immediate importance.
- **Interdisciplinary readership** The topic is of interest to biophysicists, cell biologists, and polymer physicists. The writing is generally accessible, but the heavy reliance on specialized terminology (e.g., Rouse model, tube diameter) may limit accessibility to a broader biological audience.
- **Technical soundness** The experimental and computational methods are state-of-the-art and appropriate for the questions asked. However, the lack of detailed methodological descriptions and the acknowledged challenges with simulation equilibration raise concerns about the robustness of some conclusions.
- **Readability for nonspecialists** The abstract and introduction are clear, but the results and discussion sections assume significant background knowledge. The manuscript would benefit from a more explicit explanation of the Rouse model and its relevance for a general readership.

## Risk / unsupported claims
- The claim of a "universal link" between nanoscale, microscale, and mesoscale dynamics is not fully supported by the data presented, as the quantitative agreement is within an order of magnitude and the generalizability to other systems is asserted rather than demonstrated.
- The statement that "the Rouse framework is more generally applicable" to other condensates and synthetic polyelectrolytes is based on a qualitative comparison with literature data and lacks a rigorous quantitative analysis.
- The mechanistic interpretation that contact lifetimes determine friction is inferred from simulations that are acknowledged to be challenging to equilibrate; this inference is plausible but not definitively established.
- The prediction of reconfiguration times for other IDPs (LAF-1, A1-LCD, FUS-LCD) is based on extrapolation and is not validated against experimental measurements.
- The claim that "the viscous component of the shear relaxation modulus is dominant" for the studied coacervates is based on limited microrheological measurements and may not hold at all timescales.

## Recommendation posture
Supportive if technical concerns are resolved. The manuscript addresses an important question with a sophisticated multi-scale approach, and the proposed framework is conceptually appealing. However, the central claims of predictive power and universality are not fully established from the provided evidence. The authors should strengthen the quantitative analysis, provide more detailed methodological information, and demonstrate the framework's applicability to a wider range of systems before the case is fully made.