## Review setup
- **Input scope** Full manuscript text (main text, methods summary, significance statement; supplementary material referenced but not provided)
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by presented evidence; limited to material provided in the manuscript text
- **Shared manuscript claim summary** The authors propose that the nanoscale dynamics of disordered proteins within biomolecular condensates, specifically chain reconfiguration times and contact lifetimes, quantitatively determine mesoscale material properties such as viscosity and translational diffusion. They present experimental measurements (single-molecule FRET, nsFCS, microliter rheology) and atomistic MD simulations across four coacervate systems with varying lysine/arginine content and salt concentration, and demonstrate that a Rouse model with entanglement corrections quantitatively links these observables without adjustable parameters.
- **Visible evidence base** Main text figures referenced (Figs. 1–4), methods summary, significance statement; supplementary figures and tables referenced but not provided
- **Missing materials affecting confidence** Supplementary Information (SI Appendix) including Figs. S1–S8, detailed methods, simulation protocols, and analysis procedures; full experimental protocols; simulation trajectory data; force field parameters; fitting procedures and error analysis details

## Reviewer
- **Overall assessment** This manuscript presents a compelling and potentially significant advance in connecting nanoscale molecular dynamics to mesoscale material properties of biomolecular condensates. The combination of single-molecule FRET, nsFCS, microrheology, and atomistic MD simulations across multiple coacervate systems is methodologically ambitious and the observed correlations across scales are striking. The Rouse model with entanglement corrections provides a quantitative framework that appears to unify the experimental observations. However, the manuscript as presented has several critical gaps: the supplementary material containing essential methodological details and supporting data is not available for assessment, the statistical treatment of the data is not described, and some claims regarding universality and predictive power extend beyond what the presented evidence can support. The work is potentially suitable for a high-impact journal, but the current evidence base is insufficient to fully evaluate the robustness of the central claims.

- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, intrinsically disordered proteins, polymer physics, and cellular organization would find this work of significant interest. The proposed quantitative link between nanoscale dynamics and mesoscale viscosity could provide a framework for understanding and predicting condensate material properties from molecular-level information, which has implications for understanding cellular processes, disease mechanisms involving aberrant phase separation, and the design of synthetic biomimetic materials. The methodological approach combining single-molecule FRET with atomistic simulations may also interest biophysicists developing multiscale approaches to biological systems.

- **Major strengths**
  1. The study addresses a fundamental and timely question in the condensate field: how molecular-level interactions determine macroscopic material properties.
  2. The combination of multiple experimental techniques (single-molecule FRET, nsFCS, microrheology) with atomistic MD simulations provides a rare and powerful multiscale approach.
  3. The systematic variation of lysine vs. arginine content and salt concentration allows for mechanistic insight into sequence-specific effects.
  4. The Rouse model with entanglement corrections provides a quantitative, parameter-free framework that appears to capture the observed relationships across scales.
  5. The inclusion of literature data from other condensate systems (LAF-1, A1-LCD, FUS-LCD, synthetic coacervates) suggests broader applicability.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims quantitative agreement between the Rouse model predictions and experimental measurements of viscosity, diffusion, and reconfiguration times across all coacervate systems studied.
- **Evidence pointer** Fig. 4D; Methods section; location not provided for statistical details
- **Concern** The manuscript presents correlations between experimental observables (Fig. 2J) and agreement with Rouse model predictions (Fig. 4D), but no statistical analysis is provided. There are no error bars shown in the figures, no confidence intervals for the fitted parameters, no goodness-of-fit metrics, and no description of how measurement uncertainties propagate through the model predictions. The claim of "remarkable agreement" and "no adjustable parameters" requires quantitative assessment of the uncertainties in all measured quantities (τr, D, η, cp, R²) and how these propagate to the model predictions.
- **Why it matters** Without statistical treatment, the reader cannot assess whether the observed correlations and model agreement are meaningful or could arise from systematic biases, large measurement uncertainties, or fortuitous cancellation of errors. The central claim of a quantitative, predictive relationship depends critically on the precision and accuracy of the measurements and the model comparison.
- **Resolution test** Provide error bars or confidence intervals for all reported measurements; perform and report statistical tests for the correlations in Fig. 2J; quantify the uncertainty in the Rouse model predictions based on propagated measurement errors; report goodness-of-fit metrics for the model comparisons in Fig. 4D.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that atomistic MD simulations validate the experimental findings and provide mechanistic insight into the observed dynamics.
- **Evidence pointer** Fig. 3; SI Appendix Figs. S4–S6; location not provided for simulation details
- **Concern** The simulation methodology is described only in the most general terms. Critical details are missing: force field parameters and their validation, simulation box construction and equilibration protocols, the number of independent simulations and their lengths, convergence criteria, how contact lifetimes were defined and calculated, how reconfiguration times were extracted from simulations, and how finite-size effects were assessed. The statement that "complete equilibration of the protamine-ProTα simulations is challenging" raises concerns about whether the simulations are sufficiently converged to support the quantitative claims made. The validation of the force field for these specific systems is referenced to previous work but not described.
- **Why it matters** The simulation results are used to support the mechanistic interpretation of the experimental observations and to establish the separation of timescales that justifies the Rouse model approach. If the simulations are not converged or the force field is not appropriate for these highly charged systems, the mechanistic conclusions could be incorrect. The claim that simulations "validate" the experimental findings requires that the simulation methodology be sufficiently robust and well-documented for the reader to assess.
- **Resolution test** Provide complete simulation details including force field parameters, system construction, equilibration and production protocols, simulation lengths, convergence metrics, and analysis procedures. Demonstrate convergence of the reported quantities. Provide validation of the force field for these specific systems, possibly through comparison with experimental data not used in the fitting.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the Rouse model with entanglement corrections provides a universal framework linking nanoscale, microscale, and mesoscale dynamics, applicable across different condensate systems including those from the literature.
- **Evidence pointer** Fig. 4D; Discussion; location not provided for literature data details
- **Concern** The comparison with literature data (LAF-1, A1-LCD, FUS-LCD, PMAPTAC/PAMPS) is presented as supporting the universality of the framework, but the details of this comparison are not provided. How were the literature values of D, τr, η, cp, and R² obtained? Were the same measurement techniques used? What are the uncertainties in these literature values? The claim that "all of these data are in line with the behavior of the coacervates studied here" requires a quantitative comparison that accounts for the different experimental conditions and measurement methods. Additionally, the estimated reconfiguration times for A1-LCD, FUS-LCD, and LAF-1 (0.5–5 µs, 3–30 µs, 10–100 µs) are presented without explanation of how these were derived.
- **Why it matters** The claim of universality is a key aspect of the paper's significance. If the literature comparison is not rigorous, the generality of the framework is not established. The predictive estimates for other systems are a strong claim that requires transparent derivation.
- **Resolution test** Provide a detailed description of how literature data were extracted and analyzed, including uncertainties. Show the quantitative comparison with the model predictions, including error bars. Explain how the reconfiguration time estimates for other systems were derived from the available data.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that the findings "open up possibilities for understanding and quantitatively influencing the properties of these essential cellular structures based on their molecular interactions."
- **Evidence pointer** Discussion; location not provided
- **Concern** While the Rouse model framework is elegant and appears to capture the observed relationships, the manuscript does not demonstrate how this framework can be used to predictively influence or engineer condensate properties. The discussion of implications is largely qualitative. The authors note that the framework does not enable inference of properties from sequence composition alone, which limits its predictive power for biological applications. The path from the current correlative framework to actual prediction and control of condensate properties is not articulated.
- **Why it matters** The significance statement promises quantitative prediction and influence over condensate properties. If the framework cannot yet predict properties from sequence or composition, the practical implications are more limited than claimed. The gap between the current framework and the stated implications should be acknowledged and the pathway to predictive applications should be clarified.
- **Resolution test** Clarify what the framework currently enables and what it does not. Provide a realistic assessment of the steps needed to achieve predictive power from sequence or composition. Alternatively, temper the claims in the significance statement to match what is actually demonstrated.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the microrheology measurements provide bulk viscosity values that correlate with nanoscale dynamics.
- **Evidence pointer** Fig. 2I; SI Appendix Fig. S3; location not provided for bead tracking details
- **Concern** The microrheology measurements are described only briefly. Details about bead size, surface chemistry, potential interactions with the condensate matrix, the number of measurements, the analysis method for mean squared displacement, and the validation of the Stokes-Einstein relation in these heterogeneous materials are not provided. The manuscript notes that viscosity is length-scale dependent in condensates, but the choice of bead sizes and how this affects the reported "bulk" viscosity values is not discussed. The statement that measurements are "well described in terms of normal Brownian diffusion" requires supporting data.
- **Why it matters** The viscosity values are a key experimental observable in the model comparison. If the microrheology measurements are not robust or the interpretation of the Stokes-Einstein relation is not valid for these materials, the comparison with the Rouse model predictions could be compromised.
- **Resolution test** Provide detailed microrheology methodology including bead size and surface chemistry, validation of the Stokes-Einstein relation for these systems, the number of independent measurements, and the analysis procedure. Show representative mean squared displacement curves and the fitting procedure.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Significance statement
- **Evidence pointer** Significance section
- **Issue** The significance statement is written at a level that assumes familiarity with polymer physics concepts (e.g., "Rouse model," "reconfiguration time") without defining them. Nonspecialist readers may struggle to understand the nature of the advance being claimed.
- **Required correction** Briefly define or explain key concepts in accessible language, or provide a more general framing of the significance that does not require specialized knowledge.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Fig. 2J correlations
- **Evidence pointer** Fig. 2J
- **Issue** The correlations shown in Fig. 2J are described as "remarkably high" but no correlation coefficients or significance values are reported. The number of data points is small (four coacervate systems), which limits the statistical power of any correlation analysis.
- **Required correction** Report correlation coefficients, p-values, and the number of data points. Acknowledge the limited sample size and discuss the implications for the strength of the conclusions drawn from these correlations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Contact lifetime analysis
- **Evidence pointer** Fig. 3F; location not provided
- **Issue** The definition of "contact lifetime" is not provided in the main text. It is unclear what constitutes a contact (distance cutoff? specific atom pairs?), how lifetimes were averaged, and whether the reported values are sensitive to the definition used.
- **Required correction** Provide a clear definition of contact lifetime as used in this study, including the specific criteria for defining a contact and the averaging procedure.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interdisciplinary readership
- **Affected element** Discussion of limitations
- **Evidence pointer** Discussion section
- **Issue** The discussion of limitations is brief and focuses primarily on the systems studied. The authors do not discuss potential limitations of the Rouse model itself for describing condensate dynamics, such as the assumptions of ideal chains, the neglect of hydrodynamic interactions, or the applicability to systems with more complex sequence patterning.
- **Required correction** Add a more thorough discussion of the assumptions and limitations of the Rouse model framework and the conditions under which it might break down.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Fluorescence labeling
- **Evidence pointer** Fig. 2; Methods; location not provided
- **Issue** The manuscript states that ProTα was labeled with Cy3B and CF660R at positions 56 and 110, but does not discuss whether the labeling positions could affect the conformational properties or dynamics of the protein, or whether the labels could interact with the condensate environment.
- **Required correction** Briefly address the potential effects of fluorescent labeling on the measured properties and any controls performed to assess this.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Fig. 4D
- **Evidence pointer** Fig. 4D
- **Issue** The presentation of the model comparison in Fig. 4D is not described in sufficient detail in the main text. The reader cannot determine what exactly is plotted, what the dashed lines represent, and how the literature data were incorporated.
- **Required correction** Provide a more complete description of Fig. 4D in the main text or figure legend, including the axes, the meaning of the dashed lines, and the sources of the literature data.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Concentration measurements
- **Evidence pointer** Fig. 1E; Methods; location not provided
- **Issue** The protein concentrations in the dense phase are reported to be above 100 mg/mL, but the method for determining these concentrations is not described in the main text. The accuracy of these concentration values is important for the model comparison.
- **Required correction** Briefly describe the method used to determine protein concentrations in the dense phase and the associated uncertainties.

## Risk / unsupported claims
- The claim of "universal" applicability of the Rouse framework across different condensate types is not fully supported by the presented evidence, as the literature comparison lacks quantitative detail and the number of systems studied is limited.
- The estimated reconfiguration times for LAF-1, A1-LCD, and FUS-LCD (0.5–5 µs, 3–30 µs, 10–100 µs) are presented without derivation or uncertainty estimates.
- The claim that the framework enables "quantitatively influencing" condensate properties is not demonstrated; the paper shows correlation and model agreement but not predictive control.
- The statement that "the analysis is robust with respect to the quantities we report" for the protamine-ProTα simulations is not verifiable without convergence data.
- The claim that the MD simulations "validate" the experimental findings requires the simulation details to be fully documented and the simulations to be demonstrably converged.
- The assertion that the observed correlations in Fig. 2J suggest "an underlying causal link across scales" is an interpretation that goes beyond what correlational data can establish.