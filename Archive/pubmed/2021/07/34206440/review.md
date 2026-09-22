## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) as provided.
- **Assessment boundary** Scientific content, modeling approach, computational methodology, interpretation of results, and alignment with stated claims. No assessment of editorial fit or publication decision.
- **Shared manuscript claim summary** The authors extend the Cahn–Hilliard model for phase separation by coupling it to experimentally derived macromolecular crowding dynamics and state-dependent reaction kinetics. Through simulations, they claim that macromolecular crowding leads to late-stage coarsening and stabilization of smaller condensates, and that at high crowder concentrations, reactions arrest coarsening, producing labyrinthine morphologies akin to gelation.
- **Visible evidence base** Methods section (Sections 2.1–2.3), computational results (Section 3.1–3.2), figures referenced (Figures 2–9), and supplementary video references.
- **Missing materials affecting confidence** Figures themselves are not provided; only figure captions and in-text descriptions. Supplementary videos are referenced but not accessible. No code, parameter tables, or raw simulation data are included. No convergence or resolution studies are reported.

## Reviewer
- **Overall assessment** The manuscript presents a plausible and potentially useful extension of the Cahn–Hilliard framework to include crowding-dependent mobility and state-dependent kinetics. The conceptual motivation is sound and the qualitative predictions are consistent with some experimental observations. However, the evidence provided is insufficient to fully establish the claims. Key parameters are not systematically reported, the numerical methods lack validation details, and the connection between the model outputs and experimental observables is asserted rather than demonstrated. The work is of interest to the LLPS and biophysics community, but the current presentation does not yet make the case convincingly.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation in crowded cellular environments, and theoretical biophysics. The model offers a framework for interpreting how crowding and chemical reactions jointly shape condensate morphology, which is relevant to experimentalists probing LLPS in cells and in vitro.
- **Major strengths** The coupling of experimentally derived crowding-dependent diffusion to a phase-field model is a meaningful step beyond prior work. The inclusion of state-dependent kinetics addresses a recognized limitation of constant-rate models. The qualitative prediction of crowding-induced arrest and labyrinthine morphologies provides a testable link to experimental gelation phenomena.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (parameter reporting), R1-M2 (numerical validation), R1-M3 (quantitative link to experiments), R1-M4 (model derivation clarity).
- **Assessment against Nature-style criteria**  
  - Originality: Moderate. The extension of Cahn–Hilliard with crowding-dependent mobility and state-dependent kinetics is incremental but not entirely novel; similar ideas exist in polymer physics and electrochemistry.  
  - Scientific importance: Moderate. The topic is timely and relevant, but the claims are largely qualitative and not yet quantitatively validated against experiments.  
  - Interdisciplinary readership: Moderate. The work bridges biophysics, soft matter, and cell biology, but the presentation is heavily model-focused and may not be accessible to experimentalists without additional context.  
  - Technical soundness: Weak. The numerical methods are described at a high level, but key details (parameter values, grid resolution, time stepping, convergence) are missing, preventing reproducibility.  
  - Readability for nonspecialists: Weak. The manuscript assumes familiarity with Cahn–Hilliard theory and Flory–Huggins free energy; the connection to biological relevance is stated but not developed for a broad audience.
- **Recommendation posture** Currently not established from the provided evidence. The conceptual framework is promising, but the manuscript requires substantial revision to provide reproducible parameters, numerical validation, and a clearer quantitative link to experimental data before the claims can be supported.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Reproducibility  
- **Claim pointer** The authors claim that their model, through simulations, shows crowding-dependent coarsening and arrest, but the parameter values used are not systematically reported.  
- **Evidence pointer** Section 2.1–2.3, Figures 2–9; location not provided  
- **Concern** The manuscript does not provide a table or explicit listing of the numerical values for key parameters: the interaction parameter χ, the surface tension coefficient κ, the mobility scaling M0, the reaction rate constant k0, the activation barrier μex, the degree of polymerization N, and the crowding parameters α and ζ. Without these, the simulations cannot be reproduced or compared across conditions.  
- **Why it matters** Reproducibility is a core requirement for computational studies. The absence of parameter values undermines the ability of other researchers to verify or build upon the results, and it also prevents assessment of whether the chosen parameters are biologically plausible.  
- **Resolution test** Provide a table of all parameter values used, with ranges explored and justification for each choice. If parameters are varied, show how results depend on them.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Numerical rigor  
- **Claim pointer** The authors state that simulations were performed on a 128×128 grid with finite difference schemes, but no validation of numerical accuracy is provided.  
- **Evidence pointer** Section 3, first paragraph; location not provided  
- **Concern** No convergence tests, grid-resolution studies, or time-step sensitivity analyses are reported. The choice of 128×128 is not justified, and it is unclear whether the observed morphologies are physical or numerical artifacts.  
- **Why it matters** Phase-field models are sensitive to grid resolution and time stepping, especially in the late-stage coarsening regime. Without validation, the reported morphologies and scaling exponents cannot be trusted.  
- **Resolution test** Include convergence tests showing that results are stable with respect to grid size and time step. Report the time-stepping scheme and error tolerances.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Quantitative link to experiments  
- **Claim pointer** The authors claim their results "elucidate crowder effects observed in experiments" and produce morphologies "akin to gel-like protein aggregates observed in experiments," but no quantitative comparison to experimental data is provided.  
- **Evidence pointer** Sections 3.1–3.2, Figures 5–9; location not provided  
- **Concern** The manuscript asserts qualitative agreement with experiments but does not present any quantitative comparison, such as measured length scales, growth exponents, or morphology statistics from experimental systems. The claim of "elucidation" is therefore not supported.  
- **Why it matters** Without quantitative benchmarking, the model remains a theoretical exercise. The stated relevance to experimental observations is central to the manuscript's significance, and this link must be demonstrated.  
- **Resolution test** Identify specific experimental datasets (e.g., condensate size distributions or growth kinetics under crowding) and compare model predictions quantitatively, or clearly state the limitations of the model in making such predictions.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Model derivation clarity  
- **Claim pointer** The derivation of the mobility function M(ϕ) in Equation (7) is unclear, particularly the step where ϕ is set to ϕ_rib0 = 0.  
- **Evidence pointer** Section 2.2, Equations (4)–(7); location not provided  
- **Concern** The connection between the tracer diffusion coefficient D_tr(ϕ_rib) and the mobility M(ϕ) is not fully explained. The substitution ϕ = ϕ_rib0 = 0 in the final line of Equation (7) is confusing, as it appears to set the protein volume fraction to zero, which would make the mobility expression trivial or undefined.  
- **Why it matters** The mobility function is central to the model dynamics. If the derivation is not transparent, the model's foundation is questionable and other researchers cannot properly assess or extend it.  
- **Resolution test** Provide a step-by-step derivation of Equation (7), clarify the relationship between ϕ and ϕ_rib, and justify the substitution. If the substitution is an approximation, state its validity range.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Section 2.1, Equation (1)  
- **Evidence pointer** Section 2.1; location not provided  
- **Issue** The sign convention in Equation (1) is not explicitly discussed. The term "∓R(μ,ϕ)" is unusual; it is unclear whether the reaction term is meant to be a source or sink, and how it couples to the conserved dynamics.  
- **Required correction** Clarify the sign convention and the physical meaning of the reaction term, and specify whether the dynamics conserve total mass.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Presentation  
- **Affected element** Section 3.1, Figure 5–6 descriptions  
- **Evidence pointer** Section 3.1; location not provided  
- **Issue** The text describes morphologies as "droplet-like" and "labyrinthine" but does not provide quantitative metrics (e.g., domain size, aspect ratio, or connectivity) to distinguish these regimes.  
- **Required correction** Define quantitative morphological descriptors or provide representative images with scale bars to support the qualitative descriptions.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Section 3.2, Figure 9  
- **Evidence pointer** Section 3.2; location not provided  
- **Issue** The dispersion relation analysis is presented briefly, and the connection between the unstable wavevector range and the observed morphologies is not fully developed.  
- **Required correction** Expand the discussion to explain how the dispersion relation predicts the transition from droplets to labyrinthine patterns, and relate the wavevector range to physical length scales.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Accessibility  
- **Affected element** Abstract and Introduction  
- **Evidence pointer** Abstract, Section 1; location not provided  
- **Issue** The abstract and introduction use technical terms (e.g., "Cahn–Hilliard model," "Flory–Huggins free energy") without defining them for a broader readership.  
- **Required correction** Add brief explanations or intuitive descriptions of these concepts to improve accessibility for experimental biologists.

## Risk / unsupported claims
- The claim that the model "elucidates crowder effects observed in experiments" is unsupported because no quantitative comparison to experimental data is provided.
- The claim that labyrinthine morphologies are "akin to gel-like protein aggregates observed in experiments" is asserted without direct evidence or quantitative similarity metrics.
- The statement that "the inclusion of macromolecular crowding results in late-stage coarsening and stabilization of relatively smaller condensates" is only qualitatively supported by the figures, which are not provided in the manuscript text.
- The model's predictive power for biological systems is not established, as the parameter values are not reported and their biological plausibility is not discussed.