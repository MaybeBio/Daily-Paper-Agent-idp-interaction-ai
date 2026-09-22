## Review setup
- **Input scope** Full manuscript text (Abstract, Introduction, Methods, Results, Conclusion, Acknowledgments)
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by presented evidence
- **Shared manuscript claim summary** The authors propose a unified theoretical and computational framework to compare shape recovery and fusion dynamics of Newtonian and viscoelastic droplets, arguing that these processes are fundamentally distinct, with fusion being multistage and viscoelasticity introducing additional timescales that modify dynamics.
- **Visible evidence base** Analytical theory (Jeffreys model), axisymmetric finite-element simulations (Oldroyd-B, COMSOL), mesh convergence and validation studies, comparisons of deformation histories, velocity fields, and empirical fits
- **Missing materials affecting confidence** Figures referenced (Figs. 1–10) are not provided; simulation parameter values (e.g., surface tension, droplet radius, solvent viscosity) are not fully specified; no quantitative error metrics for fits; no experimental data for direct comparison

## Reviewer
- **Overall assessment** The manuscript presents a systematic computational and theoretical study of droplet shape recovery and fusion in viscoelastic fluids, with potential relevance to biomolecular condensates. The distinction between global relaxation (shape recovery) and multistage, localized dynamics (fusion) is physically reasonable and supported by the described simulations. However, the absence of figures and key parameter values limits the ability to fully assess the strength of the evidence. The empirical stretched-exponential fit is presented without rigorous statistical evaluation, and the claim of enhanced intermediate-stage fusion dynamics in viscoelastic droplets requires clearer quantitative support. The work is technically sound in its approach but would benefit from additional detail and validation before the conclusions are fully established.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, soft matter physics, and microfluidics would find this work relevant. The comparison between shape recovery and fusion dynamics, and the role of viscoelasticity, addresses a gap between purely viscous models and observed condensate behavior. The computational framework could be useful for interpreting experimental measurements of condensate material properties.

- **Major strengths** The combination of analytical theory and finite-element simulations provides a robust methodological approach. The systematic comparison of two fundamental processes under comparable conditions is a clear strength. The discussion of the Deborah number as a controlling parameter is physically insightful. The acknowledgment of limitations in purely viscous descriptions is timely and relevant.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that viscoelasticity leads to "enhanced intermediate-stage fusion dynamics" compared to Newtonian droplets.
- **Evidence pointer** Results section, Figures 6 and 8 (figures not provided)
- **Concern** The claim of enhanced intermediate-stage fusion dynamics is stated qualitatively, but no quantitative metrics (e.g., bridge radius growth rate, velocity magnitudes, time to full coalescence) are provided in the text. Without numerical values or comparative plots, this claim cannot be evaluated.
- **Why it matters** This is a central conclusion of the work, distinguishing viscoelastic from Newtonian behavior. If unsupported, the core message is weakened.
- **Resolution test** Provide quantitative comparisons (e.g., bridge radius vs. time, velocity at neck) for Newtonian and viscoelastic cases across the range of Deborah numbers studied, with error bars or confidence intervals.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The manuscript describes finite-element simulations using the Oldroyd-B model but does not specify all material and numerical parameters.
- **Evidence pointer** Methods section, Computational Modeling (location not provided)
- **Concern** Key parameters such as surface tension γ, droplet radius R, solvent viscosity ηs, polymeric viscosity ηp, and relaxation time tc are mentioned but not all values are given. The Deborah number range is stated (0.1–1 s for tc), but the corresponding viscocapillary timescale is not explicitly defined for the simulations. This prevents reproduction of the results.
- **Why it matters** Reproducibility is a fundamental requirement for computational studies. Without full parameter specification, the work cannot be independently verified.
- **Resolution test** Provide a table listing all simulation parameters, including geometry, material properties, and numerical settings (mesh size, time stepping, convergence criteria).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Validation completeness
- **Claim pointer** The manuscript states that the computational framework is validated by comparing shape recovery simulations against analytical theory, covering small- and large-deformation regimes.
- **Evidence pointer** Results section, Figure 7 (figure not provided)
- **Concern** The validation is described qualitatively. No quantitative agreement metrics (e.g., relative error, correlation coefficient) are reported. For the large-deformation case (aspect ratio 1:8), deviations are acknowledged but not quantified.
- **Why it matters** Validation is critical to establish confidence in the simulation results, especially for the fusion cases where no analytical solution exists.
- **Resolution test** Report quantitative error measures for the comparisons in Fig. 7, and discuss the magnitude and source of deviations in the large-deformation case.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Empirical model assessment
- **Claim pointer** The stretched-exponential form (Eq. 17) is claimed to match numerical results well for Newtonian droplets, with deviations increasing with tc.
- **Evidence pointer** Results section, Figure 10 (figure not provided)
- **Concern** The fit quality is not quantified. No values for β or τf are given for the different cases, and no statistical measures (e.g., R², chi-square) are reported. The claim of "excellent fit" is subjective without such data.
- **Why it matters** The empirical model is proposed as a practical tool for interpreting experiments. Its reliability depends on demonstrated fit quality.
- **Resolution test** Provide fitted values of β and τf for each case, along with goodness-of-fit statistics and residuals.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract (location not provided)
- **Issue** The abstract states that shape recovery "follows single- or multi-exponential decay depending on the relative magnitude of the viscocapillary timescale and the stress relaxation time," but the criterion for this transition is not stated.
- **Required correction** Briefly specify the condition (e.g., De ≪ 1 vs. De ≳ 1) in the abstract.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph 2 (location not provided)
- **Issue** The term "aging" is introduced with quotes but not defined. It is used to describe progressive solidification of condensates, but the mechanism is not explained.
- **Required correction** Provide a brief definition or reference for "aging" in the context of biomolecular condensates.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Methods, Analytical model
- **Evidence pointer** Methods section, Eq. 4 (location not provided)
- **Issue** The notation Gˆ(s) is used for the Laplace-transformed modulus, but the relationship between Gˆ(s) and the time-domain modulus G(t) is not explicitly stated.
- **Required correction** Define the Laplace transform convention used.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, Exterior domain effects
- **Evidence pointer** Results section, Figure 9 (figure not provided)
- **Concern** The effect of exterior viscosity is described qualitatively, but no quantitative comparison (e.g., percent change in fusion time) is given.
- **Required correction** Provide numerical values for the reduction in fusion rate for the cases studied.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Referencing
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph 3 (location not provided)
- **Issue** The statement that "no analytical solution currently exists for droplet fusion" is made without citing recent literature that may have addressed this problem.
- **Required correction** Add a brief literature survey to support this claim.

- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative support for enhanced fusion dynamics), R1-M2 (parameter specification for reproducibility), R1-M3 (quantitative validation metrics)

- **Assessment against Nature-style criteria**  
  **Originality** The work offers a novel comparison of two fundamental processes within a unified framework, which is a fresh angle. However, the individual components (shape recovery theory, fusion simulations) are not entirely new.  
  **Scientific importance** The relevance to biomolecular condensates and the limitations of purely viscous models are important, but the impact would be higher with experimental validation or direct application to specific systems.  
  **Interdisciplinary readership** The topic bridges soft matter physics, biophysics, and materials science, which could attract a broad audience.  
  **Technical soundness** The methodological approach is sound, but the lack of quantitative details and validation metrics weakens the current presentation.  
  **Readability for nonspecialists** The manuscript is generally clear, but the Methods section assumes familiarity with viscoelastic models and COMSOL. A brief introduction to key concepts would improve accessibility.

- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the framework is appropriate, but the current evidence base is insufficient to fully support the central claims. Quantitative data, parameter transparency, and validation metrics are required before the conclusions can be considered established.

## Risk / unsupported claims
- The claim of "enhanced intermediate-stage fusion dynamics" in viscoelastic droplets is not quantitatively supported.
- The assertion that the stretched-exponential form provides an "excellent fit" is not backed by statistical measures.
- The statement that viscoelasticity "can extend the regime of validity of linearized theoretical descriptions" is speculative and not directly tested.
- The relevance of the findings to biomolecular condensates is asserted but not demonstrated with experimental data or specific parameter ranges typical of such systems.