## Review setup
- **Input scope** Full manuscript text including main text, appendices, and figure captions (as provided).
- **Assessment boundary** Scientific content, theoretical consistency, methodological validity, and clarity of presentation. Not assessed: editorial formatting, grammar, or style beyond scientific readability.
- **Shared manuscript claim summary** The authors develop a self-consistent sharp interface theory for active condensates, where enzyme-enriched droplets catalyze reactions between substrates and products, and the resulting concentration gradients drive droplet motion via reciprocal interactions. The theory inverts the usual explicit modeling approach by treating the enzyme concentration profile as a given sharp interface and inferring the chemical potential and currents required to maintain a steady state with a given velocity. A thermodynamic consistency condition (vanishing chemical potential imbalance) determines the droplet speed. The theory is tested against full diffuse-interface simulations and used to analyze how reciprocal interactions affect the onset of self-propulsion, including the identification of subcritical versus supercritical bifurcations.
- **Visible evidence base** Main text Sections I–V, Appendices A–H, Figures 1–12 (as referenced), and descriptions of Supplemental Videos 1–7. No actual figure images or simulation data files were provided.
- **Missing materials affecting confidence** Actual figure images, simulation parameter tables, and the referenced Mathematica notebooks (Goychuk et al. 2023) were not provided. The full derivation details in Appendices D and F are summarized but not fully reproduced. The exact numerical methods and convergence criteria for the FEM simulations are not fully specified.

## Reviewer
- **Overall assessment** This manuscript presents a conceptually novel and potentially impactful theoretical framework for studying active condensate dynamics. The key idea of inverting the modeling logic, treating the concentration profile as given and inferring the chemical potential, is elegant and could have broad applicability beyond the specific system studied. The thermodynamic consistency criterion provides a clear and physically motivated selection principle for the droplet velocity. The comparison with full simulations, while not fully visible, appears to support the theory's validity. However, several technical aspects require clarification and strengthening before the case is fully established. The treatment of reciprocal interactions, particularly the derivation of concentration jumps and the bifurcation analysis, needs more rigorous justification. The manuscript is generally well-written and accessible, though some sections are dense.
- **Who would be interested in the results, and why** Researchers in biological physics, soft matter physics, and non-equilibrium thermodynamics would be interested. Specifically, those studying biomolecular condensates, active matter, phase separation, and self-propelled droplets. The theoretical framework could also appeal to mathematicians and physicists working on sharp interface methods and moving boundary problems. The connection to Fisher waves and potential applications to cell migration broaden the potential audience.
- **Major strengths**
    1.  The central conceptual innovation, the implicit adiabatic elimination scheme, is a significant and elegant departure from standard approaches. It offers a computationally efficient and physically insightful way to analyze moving phase boundaries.
    2.  The thermodynamic consistency criterion provides a first-principles-based selection mechanism for the droplet velocity, grounding the theory in energy conservation.
    3.  The theory is general and not tied to the specific model details, suggesting broad applicability to other mass-conserved active systems.
    4.  The analysis of reciprocal interactions, including the identification of subcritical versus supercritical bifurcations, provides concrete, testable predictions about the nature of the self-propulsion transition.
    5.  The comparison with full FEM simulations, as described, demonstrates the quantitative accuracy of the theory across a range of parameters.
- **Major Concerns**

    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The claim that the sharp interface theory is "self-consistent" and that the thermodynamic consistency condition (Eq. 17) uniquely determines the droplet velocity relies on the assumption that the chemical potential profile is a well-defined, single-valued function of the droplet velocity and the concentration profiles.
    - **Evidence pointer** Section II.1, Eq. (13)-(17), Figure 3(b).
    - **Concern** The manuscript does not rigorously demonstrate the existence and uniqueness of the solution to the weak form (Eq. 15) for a given velocity. The chemical potential is introduced as a Lagrange multiplier, but the functional space in which it is sought is not specified. More critically, the claim that the thermodynamic consistency condition (Eq. 17) has a unique root for the velocity is not proven. The non-monotonic behavior of Δμ₀(v) shown in Figure 3(b) suggests multiple roots are possible, and the manuscript does not discuss how the "correct" physical root is selected, especially in the bistable regime. The stability analysis based on the slope of Δμ₀(v) is heuristic and not derived from a dynamical analysis of the full system.
    - **Why it matters** Without a rigorous proof of existence and uniqueness, the "self-consistent" nature of the theory is not fully established. The selection of the physical root for the velocity is crucial for the predictive power of the theory, especially in the bistable regime where multiple stable states may coexist. The heuristic stability argument needs a more solid foundation to be fully convincing.
    - **Resolution test** The authors should provide a mathematical proof or a more detailed numerical investigation of the solution space of Eq. (15) and the roots of Eq. (17). They should also derive the stability criterion from a linear stability analysis of the full dynamical equations in the sharp interface limit, rather than relying on a heuristic argument.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The claim that reciprocal interactions induce concentration jumps at the droplet interface, as described by Eq. (58), and that these jumps are essential for the subcritical bifurcation.
    - **Evidence pointer** Section III, Appendix D, Eq. (30), (58), Figure 6.
    - **Concern** The derivation of the concentration jumps in Appendix D is not fully detailed. The manuscript states that these arise from integrating the singular terms in Eq. (8) across the interface, but the precise mathematical steps and the physical assumptions (e.g., the nature of the interface, the behavior of the mobility functions) are not clearly presented. The claim that these jumps are the cause of the subcritical bifurcation is plausible but not rigorously demonstrated. The analysis appears to be limited to 1D, and the extension to higher dimensions is not discussed.
    - **Why it matters** The concentration jumps are a key new physical effect introduced by the reciprocal interactions. If their derivation is not rigorous, the subsequent analysis of the bifurcation structure is built on shaky ground. The restriction to 1D limits the generality of the conclusions, especially since the paper claims to develop a theory for arbitrary dimensions.
    - **Resolution test** The authors should provide a complete and rigorous derivation of the jump conditions, including all mathematical steps and a clear statement of the assumptions. They should also discuss how these conditions generalize to higher dimensions and whether the qualitative conclusions about the bifurcation structure hold in 2D and 3D.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific importance
    - **Claim pointer** The claim that the theory is "self-consistent" and provides a "thermodynamically consistent" description, implying it captures the essential physics of the system.
    - **Evidence pointer** Section II.2, Eq. (24), Figure 12(c).
    - **Concern** The thermodynamic consistency argument equates the vanishing of the chemical potential imbalance with the minimization of free energy dissipation. However, the manuscript does not discuss the relationship between this criterion and the second law of thermodynamics in the context of the active, non-equilibrium system. The "power dissipation" calculated in Eq. (20) is associated with the chemical potential of the enzyme-enzyme interactions, but the total entropy production rate of the system, which would include contributions from the active reactions, is not calculated. The claim that the system minimizes free energy dissipation is a strong statement that requires a more careful thermodynamic treatment.
    - **Why it matters** The thermodynamic interpretation is a central pillar of the paper's conceptual framework. If the connection to the second law is not made clear, the "thermodynamic consistency" criterion could be seen as an ad hoc selection rule rather than a fundamental principle. This weakens the claim of the theory's generality and physical grounding.
    - **Resolution test** The authors should provide a more complete thermodynamic analysis, calculating the total entropy production rate of the system and showing explicitly how the vanishing of the chemical potential imbalance relates to the second law. They should also discuss the conditions under which the system can be described by an effective free energy.

- **Minor Comments**

    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability for nonspecialists
    - **Affected element** Section II.1, Eq. (13)-(15)
    - **Evidence pointer** Section II.1
    - **Issue** The transition from the diffuse-interface model to the sharp-interface limit is described somewhat abruptly. The physical meaning of the Lagrange multiplier field μ₀ as a chemical potential is stated, but the connection to the original free energy functional is not fully elaborated for a reader unfamiliar with this type of asymptotic analysis.
    - **Required correction** Add a brief introductory paragraph in Section II.1 that explains the physical intuition behind the sharp interface limit and the role of the chemical potential as a Lagrange multiplier, perhaps with a simple analogy.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Section III.2, Figure 8
    - **Evidence pointer** Section III.2
    - **Issue** The description of the numerical methods for the full FEM simulations is very brief. The manuscript mentions "full FEM simulations" but does not specify the numerical scheme, time-stepping, or convergence criteria. This makes it difficult to assess the accuracy and reliability of the simulation results used for comparison.
    - **Required correction** Provide a more detailed description of the numerical methods used for the full simulations, including the discretization scheme, solver, and error tolerances. This could be in a separate appendix or in the main text.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Readability for nonspecialists
    - **Affected element** Section III.3, Eq. (44)
    - **Evidence pointer** Section III.3
    - **Issue** The analysis of the strong interaction limit (Λε₀/D → ∞) is mathematically dense and the physical interpretation of the resulting criteria is not immediately clear. The connection between the mathematical conditions and the physical picture of droplet motion is not fully articulated.
    - **Required correction** Add a short paragraph after Eq. (44) that summarizes the physical meaning of the derived criteria in plain language, explaining what conditions on the system parameters favor or disfavor self-propulsion.

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Originality
    - **Affected element** Section IV, Discussion
    - **Evidence pointer** Section IV
    - **Issue** The discussion of the analogy to fluid mechanics is interesting but brief. The comparison to Euler's equations is made, but the implications of this analogy for future work are not fully explored.
    - **Required correction** Expand the discussion of the fluid mechanics analogy, perhaps by discussing how the "chemical potential" could be interpreted as a pressure field and what new physical insights this analogy might provide.

- **Technical failings that need to be addressed before the case is established**
    - R1-M1: Lack of rigorous proof of existence and uniqueness of the solution to the sharp-interface equations and the root of the thermodynamic consistency condition.
    - R1-M2: Incomplete derivation of the concentration jump conditions at the interface for reciprocal interactions.
    - R1-M3: The thermodynamic interpretation of the consistency criterion is not fully grounded in a complete non-equilibrium thermodynamic analysis.

## Risk / unsupported claims
- The claim that the theory is "self-consistent" is not fully supported by a rigorous mathematical proof of existence and uniqueness.
- The claim that the thermodynamic consistency criterion is a consequence of energy conservation is not fully substantiated by a complete entropy production analysis.
- The claim that the theory applies to "arbitrary dimensions" is not fully supported, as the detailed analysis of reciprocal interactions is limited to 1D.
- The quantitative accuracy of the theory is claimed based on comparisons with simulations, but the simulation details are not fully provided, making it difficult to assess the strength of this evidence.
- The specific claim that the onset of self-propulsion is subcritical for Λ > 0 is based on the analysis of a specific parameter regime and may not be universally true.