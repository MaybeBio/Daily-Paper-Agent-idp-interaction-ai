## Review setup
- **Input scope** Full manuscript text, including main text, appendices, and references.
- **Assessment boundary** Scientific validity, technical soundness, and clarity of the presented model, analyses, and conclusions. No assessment of editorial fit or publication venue.
- **Shared manuscript claim summary** The authors develop a one-dimensional poroelastic phase-field model coupling phase separation of a binary mixture to a non-local elastic network response. They report that non-local elasticity arrests coarsening and produces patterned steady states with a well-defined length scale, whereas local elasticity only inhibits phase separation and slows coarsening. The model is analyzed via linear stability analysis and numerical simulation.
- **Visible evidence base** Main text sections 1–6, Appendix A, Figures 1–8 (referenced but not provided), and a data availability statement with a Zenodo link.
- **Missing materials affecting confidence** Figures 1–8 are not included in the provided material. Numerical parameters, initial conditions, and simulation details (e.g., domain size, grid resolution, time stepping tolerances) are not fully specified. The derivation of the linearized equations (15)–(16) is not shown in full. The relationship between the non-local kernel and physical network heterogeneity is not quantitatively justified.

## Reviewer
- **Overall assessment** This manuscript presents a timely and potentially significant extension of equilibrium theories of non-local elastic phase separation to a dynamical, large-deformation poroelastic framework. The model is clearly formulated and the distinction between local and non-local elastic effects on coarsening is conceptually important. However, the absence of figures and incomplete simulation details prevent full verification of the central claims. The linear stability analysis is presented in a condensed form, and the numerical evidence for arrested coarsening, while plausible, cannot be fully assessed without the visual data and quantitative convergence checks. The work is likely to interest researchers in soft matter physics, biomechanics, and materials science, but the current evidence base is insufficient to fully establish the case.
- **Who would be interested in the results, and why** Researchers studying phase separation in soft materials, particularly those interested in biomolecular condensates interacting with cytoskeletal networks, structural coloration in biological tissues, and the mechanics of gels and elastomers. The dynamical framework and the prediction of non-local elasticity as a coarsening arrest mechanism are directly relevant to experimental efforts in these areas. The methodological approach may also appeal to theorists working on poroelasticity and phase-field models.
- **Major strengths** The manuscript addresses a clear gap in the literature by extending equilibrium non-local elastic theories to dynamics. The use of a large-deformation poroelastic framework is physically appropriate and represents a methodological advance over partially linearized approaches. The linear stability analysis provides a systematic classification of instability types, and the numerical simulations appear to probe the relevant parameter regimes. The writing is generally clear and the model derivation is logically structured.
- **Major Concerns** The central claims regarding arrested coarsening and the length scale dependence on stiffness cannot be verified without the figures. The linear stability analysis is presented without a full derivation, and the conditions under which the patterned instability occurs are not fully explored. The numerical method is described only briefly, and no convergence or robustness checks are reported. The relationship between the non-local kernel and physical network heterogeneity is asserted but not derived or justified from a microstructural model.
- **Minor Comments** The introduction is comprehensive but could be streamlined. The non-dimensionalization is stated but the resulting dimensionless equations are not written out explicitly. The choice of the exponential kernel is not discussed in terms of alternative forms. The discussion of the discrepancy with the square-root scaling predicted by equilibrium theories is speculative and would benefit from a more quantitative analysis.
- **Assessment against Nature-style criteria**  
  *Originality*: The dynamical non-local poroelastic framework is a novel contribution, extending prior equilibrium work. The identification of a patterned instability and arrested coarsening is conceptually new.  
  *Scientific importance*: The results are relevant to several active experimental areas and could inform the design of materials with controlled microstructure. The framework is general and likely to be adopted by other groups.  
  *Interdisciplinary readership*: The topic bridges soft matter physics, mechanics, and materials science, and the writing is accessible to nonspecialists in these fields. However, the mathematical formalism may be challenging for a broader audience.  
  *Technical soundness*: The model derivation is plausible, but the lack of full derivations and simulation details limits confidence. The linear stability analysis is standard but not fully verified.  
  *Readability for nonspecialists*: The structure is logical and the key concepts are explained, but the condensed presentation of the analysis sections may hinder comprehension for readers without a background in poroelasticity.
- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual advance is significant, but the current evidence base is insufficient to fully establish the claims. The authors should provide the missing figures, full derivations, and detailed numerical methods to allow verification.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence completeness  
- **Claim pointer** The manuscript claims that non-local elasticity arrests coarsening and produces patterned steady states with a well-defined length scale (Sections 5.2, 6).  
- **Evidence pointer** Figures 6–8, Section 5.2, location not provided  
- **Concern** The central claim of arrested coarsening is supported only by reference to figures that are not included in the provided material. Without the actual simulation data, it is impossible to verify that the observed patterns are true steady states, that coarsening is completely arrested rather than merely slowed, or that the length scale is independent of simulation time and domain size.  
- **Why it matters** The claim of arrested coarsening is the primary novel result of the manuscript. If the evidence is not robust, the main conclusion is not established.  
- **Resolution test** Provide the figures and quantitative measures of coarsening (e.g., domain size vs. time) for multiple simulation times, domain sizes, and initial conditions. Demonstrate that the pattern length scale converges and does not change over extended time horizons.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The linear stability analysis identifies a patterned instability (case 2) and a stable region (cases 3 and 4) with distinct boundaries (Section 3, Figure 2).  
- **Evidence pointer** Section 3, Equations (15)–(16), Figure 2, location not provided  
- **Concern** The derivation of the linearized equations (15)–(16) is not shown, and the conditions for the patterned instability are not fully characterized. The dispersion relation is stated but not derived, and the role of the non-local parameter α in shifting the instability boundaries is not analyzed in detail.  
- **Why it matters** The phase diagram and the identification of the patterned instability are foundational to the numerical results. If the linear analysis is incorrect or incomplete, the interpretation of the simulations is compromised.  
- **Resolution test** Provide a full derivation of the linearized equations, including all steps from the nonlinear model. Show the dispersion relation for representative parameters and verify the instability boundaries against numerical solutions of the linearized system.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Reproducibility  
- **Claim pointer** The numerical simulations are used to support claims about phase separation dynamics and pattern formation (Sections 4.2, 5.2).  
- **Evidence pointer** Section 2.5, Section 4.2, Section 5.2, location not provided  
- **Concern** The numerical method is described only as a central finite difference scheme with MATLAB’s ode15s solver. No details are given on grid resolution, domain size, time stepping tolerances, or convergence checks. The initial conditions are described as "small random perturbations" but the amplitude and distribution are not specified.  
- **Why it matters** Without these details, the numerical results cannot be reproduced or assessed for numerical artifacts. The claim that patterns are robust to domain size and initial conditions is not verifiable.  
- **Resolution test** Provide a complete description of the numerical setup, including grid spacing, domain size, time integration tolerances, and initial condition generation. Report convergence tests (e.g., grid refinement, time step reduction) and demonstrate that the results are independent of these choices.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Physical justification  
- **Claim pointer** The non-local elastic kernel gξ is introduced as a phenomenological representation of network heterogeneity, and the exponential form is chosen for analytical convenience (Section 2.2, Appendix A).  
- **Evidence pointer** Section 2.2, Appendix A, location not provided  
- **Concern** The physical origin of the non-local kernel is not justified. The manuscript does not explain how the kernel relates to specific microstructural features of the network (e.g., crosslink density variations, fiber length scales). The choice of the exponential kernel is not compared to other possible forms, and the range of ξ values used in simulations is not tied to experimental measurements.  
- **Why it matters** The non-local term is the key new physics in the model. If its physical basis is unclear, the predictive power of the model for real systems is limited.  
- **Resolution test** Provide a microstructural derivation or at least a heuristic argument for the non-local kernel. Discuss how ξ could be measured or estimated from experiments, and show how the results depend on the kernel shape.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Section 2.2, Equations (1)–(4)  
- **Evidence pointer** Section 2.2, location not provided  
- **Issue** The free energy functional is written in a mixed form with the local part in the lab frame and the non-local part in the reference frame. This is potentially confusing and the transformation between frames is not explicitly stated.  
- **Required correction** Clarify the frame of reference for each term and explicitly state the Jacobian transformation used to convert between lab and reference frames.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Section 3, Equation (16)  
- **Evidence pointer** Section 3, location not provided  
- **Issue** The dispersion relation is given but the definitions of all symbols (e.g., β, α) are not repeated in the equation caption or nearby text.  
- **Required correction** Define all symbols in the text immediately following the equation, or refer clearly to their definitions in Section 2.5.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Section 2.5, numerical method  
- **Evidence pointer** Section 2.5, location not provided  
- **Issue** The boundary conditions are stated as periodic, but the domain size and the number of grid points are not given.  
- **Required correction** Specify the domain length and grid resolution used in all simulations.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Interpretation  
- **Affected element** Section 5.2, Figure 8  
- **Evidence pointer** Section 5.2, location not provided  
- **Issue** The claim that the pattern length scale decreases with stiffness is presented without a quantitative scaling law or comparison to theoretical predictions.  
- **Required correction** Provide a quantitative fit of L_patt vs. stiffness and compare to the predicted scaling from the linear stability analysis.

## Risk / unsupported claims
- The claim that non-local elasticity completely arrests coarsening is not verifiable without the figures and quantitative time-evolution data.
- The claim that the pattern length scale is energetically selected and independent of domain size is not supported by the provided evidence.
- The relationship between the non-local kernel and physical network heterogeneity is asserted but not derived or justified.
- The discrepancy between the observed scaling of L_patt and the square-root prediction of equilibrium theories is speculative and not quantitatively analyzed.
- The numerical results are not reproducible without full details of the discretization, domain size, and initial conditions.