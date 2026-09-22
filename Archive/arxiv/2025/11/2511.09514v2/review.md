## Review setup
- **Input scope** Full manuscript text, including main text, supplementary information, and references.
- **Assessment boundary** Scientific soundness, methodological rigor, validity of claims, and clarity of presentation. This review does not assess the novelty of the work relative to the existing literature beyond what is presented in the manuscript.
- **Shared manuscript claim summary** The authors use coarse-grained molecular dynamics simulations and a generalized random-phase approximation (GRPA) theory to study the force-extension behavior of polyampholyte (PA) chains with different charge sequences. They report a continuous coil-to-stretch transition at weak electrostatic coupling, which becomes a sharp globule-coil-like transition at stronger coupling. They observe hysteresis in force-extension-relaxation cycles and identify four distinct regimes in the elastic modulus, including a novel exponential stress-softening regime. They extend their findings to intrinsically disordered proteins (IDPs) LAF1 and DDX4, suggesting universality of the mechanisms.
- **Visible evidence base** Main text (Sections I-IV), including Figures 2, 3, 4, 5, 6, 8, 14, and 16; Supplementary Information (Sections SI-A to SI-E), including Figures 11, 12, 13, 14, and 15.
- **Missing materials affecting confidence** The manuscript does not provide a detailed description of the simulation protocol for the IDP systems (LAF1 and DDX4), including the specific force field parameters, temperature, and salt concentration. The derivation of the GRPA free energy is referenced to a previous publication, and the key equations are presented without a step-by-step derivation. The exact definition of the "block length" for the PA chains and the method for generating sequences with varying block lengths are not fully specified. The method for calculating the elastic modulus from simulation data is not described in detail.

## Reviewer
- **Overall assessment** This manuscript presents a systematic computational and theoretical study of the mechanical response of polyampholyte chains, a topic of significant relevance to the physics of intrinsically disordered proteins and the design of soft materials. The combination of coarse-grained simulations with a GRPA-based analytical theory is a strength, and the identification of a universal exponential softening regime is an interesting finding. However, the manuscript has several weaknesses that need to be addressed. The presentation of the theoretical model is incomplete, and the connection between the theory and the observed exponential softening is not rigorously established. The analysis of the simulation data, particularly the identification of the four elastic regimes, relies on qualitative visual inspection of the figures. The extension to IDPs is presented as a brief add-on without sufficient detail or analysis. The manuscript would be strengthened by a more detailed and quantitative analysis of the simulation results, a clearer exposition of the theoretical framework, and a more thorough discussion of the limitations of the model.
- **Who would be interested in the results, and why** Researchers in the fields of polymer physics, biophysics, and soft matter. Specifically, those studying the mechanical properties of intrinsically disordered proteins, the physics of polyelectrolytes and polyamphpholytes, and the design of stimuli-responsive or tough hydrogels. The findings on sequence-dependent elasticity and the universal softening behavior could inform the design of biomimetic materials.
- **Major strengths**
    1.  The study addresses a relevant and timely problem: the role of charge sequence in determining the mechanical response of polyamphpholytes and IDPs.
    2.  The combination of coarse-grained simulations and an analytical theory (GRPA) is a powerful approach that can provide both detailed insights and generalizable predictions.
    3.  The identification of a universal exponential softening regime, supported by both simulation and a theoretical argument, is a potentially significant finding.
    4.  The study connects single-molecule mechanics to macroscopic material properties (e.g., energy dissipation, viscoelasticity), which is an important conceptual step.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The manuscript claims that the GRPA theory "quantitatively captures these behaviors, including the sharp conformational transition and its dependence on electrostatic strength" and that the elastic modulus in the softening regime decreases exponentially, E ∼ exp(−α₀f/Γe), "which aligns with the simulation results."
    - **Evidence pointer** Section III.2, Figure 14 (main text), Figure 14 (SI)
    - **Concern** The theoretical derivation is presented in a highly condensed form. The key equations for the free energy (Eqs. 15-19) are stated without a clear derivation, and the connection between the GRPA free energy and the predicted force-extension behavior is not shown. The claim of "quantitative" agreement is not supported by a direct comparison between the theoretical and simulation force-extension curves or the elastic modulus. The theoretical prediction for the elastic modulus (Figure 14, SI) shows a "pronounced drop" and recovery, but it is not demonstrated that this drop follows the exponential form E ∼ exp(−α₀f/Γe) claimed in the abstract and conclusions. The theoretical curve does not appear to show the subsequent stiffening at high forces that is observed in the simulations. The manuscript needs to provide a more complete derivation of the theory, a direct and quantitative comparison between theory and simulation, and a clear demonstration of the exponential form of the softening.
    - **Why it matters** The central claim of the paper is that the GRPA theory provides a quantitative understanding of the simulation results. Without a clear and direct comparison, this claim is not substantiated. The exponential softening is a key finding, and its theoretical basis must be rigorously established.
    - **Resolution test** The authors should provide a figure directly comparing the theoretical and simulation force-extension curves and elastic modulus for at least one strong-coupling case. They should also explicitly fit the theoretical and simulation data in the softening regime to the exponential form and report the extracted parameters (α₀). A step-by-step derivation of the GRPA free energy, or a more detailed reference to the original derivation, is required.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The manuscript claims the existence of four distinct elastic regimes: "an initial plateau, stress stiffening, an exponential stress-softening behavior, and a stress stiffening regime."
    - **Evidence pointer** Section III.1, Figure 3
    - **Concern** The identification of the four regimes is based on a qualitative description of the force-extension curve and the elastic modulus plot. The boundaries of these regimes are not defined quantitatively. The scaling exponents for the stiffening regimes (α ≈ 1.2 and α ≈ 1.5) are stated, but it is not clear how these exponents were extracted from the data. The "plateau" regime is not clearly identified in the figures. A more rigorous analysis, such as a log-log plot of the elastic modulus vs. force with clear linear fits for each regime, is needed to support the claim of distinct scaling laws.
    - **Why it matters** The identification of distinct mechanical regimes is a central result of the paper. If the regime boundaries and scaling exponents are not robustly determined, the conclusions drawn from them are weakened.
    - **Resolution test** The authors should provide a log-log plot of the elastic modulus vs. force, with the proposed scaling regimes clearly marked and the corresponding power-law fits shown. The method for determining the regime boundaries should be described.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific importance
    - **Claim pointer** The manuscript claims that the findings on PA chains can be extended to IDPs, stating that "coarse-grained models of IDPs such as LAF-1 and DDX4 exhibit similar nonlinear elasticity, highlighting the universality of these mechanisms."
    - **Evidence pointer** Section III.4, Figure 16
    - **Concern** The analysis of the IDP systems is very brief. The manuscript only shows the elastic modulus for a few variants of LAF1 and DDX4. It is not clear how the "nSCD" parameter was varied for these proteins, or whether the observed behavior is truly analogous to the block-length dependence seen in the synthetic PA chains. The claim of "universality" is a strong statement that is not fully supported by the limited data presented. A more detailed analysis of the IDP systems, including a comparison of their force-extension curves and structural transitions with the PA chains, is needed.
    - **Why it matters** The extension to IDPs is a key part of the paper's significance, as it suggests that the findings are relevant to biological systems. If this connection is not made convincingly, the broader impact of the work is diminished.
    - **Resolution test** The authors should provide a more detailed analysis of the IDP simulations, including force-extension curves, structural characterization (e.g., radius of gyration, shape), and a direct comparison with the behavior of the synthetic PA chains with equivalent block lengths.

    - **Concern ID** R1-M4
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical soundness
    - **Claim pointer** The manuscript claims that the "elastic softening" is due to the "dissociation of oppositely charged monomer pairs within the folded hairpin-like conformations" and that the structure in this regime is a "double hairpin loop."
    - **Evidence pointer** Section III.1, Figure 4, Figure 5
    - **Concern** The structural characterization of the "double hairpin" conformation is not quantitative. The manuscript refers to Figure 4, but the snapshots are likely not sufficient to demonstrate a well-defined double-hairpin structure. The claim that the softening is due to the dissociation of "electrostatic bonds" is a hypothesis that is not directly tested. The manuscript should provide a quantitative measure of the structure, such as the number of intra-chain contacts, the distribution of the angle between the two arms, or a contact map, to support the claim of a double-hairpin conformation.
    - **Why it matters** The proposed mechanism for the softening is a key part of the paper's narrative. Without direct structural evidence, the mechanism remains speculative.
    - **Resolution test** The authors should provide a quantitative structural analysis of the chain in the softening regime, such as a plot of the number of native contacts or the radius of gyration as a function of force, and a representative contact map or density plot showing the double-hairpin structure.

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability for nonspecialists
    - **Affected element** Introduction
    - **Evidence pointer** Section I
    - **Issue** The introduction is dense and assumes a high level of familiarity with polymer physics. The motivation for studying PA chains could be stated more clearly for a broader audience.
    - **Required correction** Briefly explain why the force-extension behavior of PA chains is important for understanding IDP function and for materials design, perhaps with a concrete example.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Simulation Model
    - **Evidence pointer** Section II
    - **Issue** The manuscript states that "counterion effects on the PA conformations are negligible at dilute concentrations; hence, explicit counterions are omitted." This is a significant approximation that should be justified more carefully, as counterion condensation can be important for polyelectrolytes.
    - **Required correction** Provide a more detailed justification for neglecting counterions, perhaps by citing relevant literature or showing that the qualitative results are unchanged in a system with explicit counterions.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Results, Section III.1
    - **Evidence pointer** Figure 2
    - **Issue** The manuscript states that the transition is "continuous" for Γe ≤ 1 and "sharp" for Γe > 1. The definition of "sharp" is not quantitative. It would be helpful to provide a measure of the sharpness of the transition, such as the width of the transition region.
    - **Required correction** Define a quantitative measure for the sharpness of the transition (e.g., the derivative of Re with respect to f at the inflection point) and report its value for different Γe.

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Results, Section III.1
    - **Evidence pointer** Figure 6
    - **Issue** The definition of the "number of dipoles" (Nd) is somewhat arbitrary, as it depends on the cutoff distance and the rule that each monomer can participate in only one dipole. The sensitivity of the results to these choices is not discussed.
    - **Required correction** Briefly discuss the sensitivity of the Nd results to the chosen cutoff and the single-pair rule.

    - **Concern ID** R1-m5
    - **Severity** Minor
    - **Axis** Readability for nonspecialists
    - **Affected element** Results, Section III.2
    - **Evidence pointer** Section III.2
    - **Issue** The theoretical section is very technical and will be difficult for non-experts to follow. The physical meaning of the different terms in the free energy expression is not explained.
    - **Required correction** Add a brief physical interpretation of the key terms in the free energy (e.g., the confinement term, the electrostatic correlation term) to make the theory more accessible.

    - **Concern ID** R1-m6
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Results, Section III.4
    - **Evidence pointer** Figure 16
    - **Issue** The manuscript does not specify the simulation temperature or the dielectric constant used for the IDP simulations. These parameters are crucial for the strength of electrostatic interactions.
    - **Required correction** State the simulation temperature and dielectric constant for the IDP simulations.

- **Technical failings that need to be addressed before the case is established**
    - R1-M1: The quantitative agreement between theory and simulation is not demonstrated.
    - R1-M2: The identification of the four elastic regimes is not based on a rigorous quantitative analysis.
    - R1-M3: The extension to IDPs is not sufficiently detailed to support the claim of universality.
    - R1-M4: The structural basis for the "double hairpin" conformation and the proposed softening mechanism is not quantitatively established.

- **Assessment against Nature-style criteria**
    - **Originality** The work is original in its specific focus on the sequence-dependent elastic softening of polyamphpholytes and its connection to IDPs. The use of GRPA to model the force-extension behavior is a novel application. However, the general phenomenon of force-induced conformational transitions in polymers is well-established.
    - **Scientific importance** The findings have the potential to be important for understanding the mechanical properties of IDPs and for designing soft materials with tunable elasticity. The link between charge sequence and macroscopic elasticity is a valuable contribution. The importance is somewhat diminished by the lack of a robust quantitative analysis and the limited treatment of the IDP systems.
    - **Interdisciplinary readership** The topic is of interest to polymer physicists, biophysicists, and soft matter scientists. The manuscript is written in a way that is accessible to these groups, but the technical density of the theory section may limit its appeal to a broader audience.
    - **Technical soundness** The simulation methodology appears sound, but the analysis of the results is not sufficiently rigorous. The theoretical framework is not presented in enough detail to be fully evaluated, and the claimed quantitative agreement is not demonstrated. The structural interpretation of the softening mechanism is not supported by quantitative evidence.
    - **Readability for nonspecialists** The abstract and introduction are clear, but the results and theory sections are dense and will be challenging for non-specialists. The manuscript would benefit from a more accessible explanation of the key concepts and findings.

- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is interesting and the combination of simulation and theory is promising. However, the manuscript in its current form does not fully substantiate its central claims. The authors need to provide a more rigorous and quantitative analysis of their data, a more complete presentation of the theory, and a more detailed treatment of the IDP systems to make the case for universality.