## Review setup

- **Input scope** Full manuscript text, including main text, appendices, and references (as provided).
- **Assessment boundary** The scientific claims, theoretical derivations, and internal consistency of the presented framework, based solely on the provided manuscript material.
- **Shared manuscript claim summary** The manuscript presents a theoretical framework for the dynamics of biomolecular condensates in viscoelastic media. It claims that (i) externally driven motion of condensates induces dipole force fields ("translation-induced polarization"), leading to directed coalescence; (ii) active stress fluctuations in viscoelastic media can either enhance or suppress condensate diffusion, depending on the ratio of correlation times; and (iii) these effects can lead to anomalous diffusion and altered coalescence kinetics.
- **Visible evidence base** Analytical derivations in the main text and Appendices A-G, and numerical solutions of the derived differential equation for mean squared displacement, as described in Appendix H and referenced in Figures 2-5.
- **Missing materials affecting confidence** Figures 1-5 are referenced but not provided. Derivations are presented in a condensed form, with several steps stated rather than fully shown. The manuscript does not include a comparison with experimental data or simulations of a specific physical system.

## Reviewer

- **Overall assessment** This manuscript presents a formal theoretical framework with potentially significant implications for the physics of biomolecular condensates. The central concept of translation-induced polarization, leading to dipole-dipole interactions between moving condensates, is an elegant and novel idea. The subsequent analysis of condensate diffusion in a viscoelastic medium with active fluctuations is a substantial piece of work, yielding non-trivial predictions such as the suppression or enhancement of size-dependent diffusion. However, the presentation is highly abstract, and the connection to concrete, testable experimental scenarios is not fully developed. The derivations, while plausible, are not presented with sufficient detail for a reader to easily verify all steps. The lack of figures and a direct application to a specific experimental system limits the current impact. The work is likely of high interest to theorists in soft matter and biological physics, but its broader significance will depend on the clarity of its predictions and their experimental accessibility.
- **Who would be interested in the results, and why** Researchers in theoretical soft matter physics, biological physics, and physical chemistry. Specifically, those studying phase separation, condensate dynamics, active matter, and non-equilibrium statistical mechanics. The work provides a new mechanism for condensate interactions and a framework for understanding their motion in complex, active environments like the cell cytoplasm. The predictions regarding diffusion scaling could be directly relevant to experimentalists tracking condensate motion in cells.
- **Major strengths**
    1.  The concept of translation-induced polarization is novel and provides a general, model-independent mechanism for long-range interactions between moving domains in conserved systems.
    2.  The theoretical framework is ambitious and aims to be general, covering potential and non-potential forces, and various fluid models.
    3.  The analysis of the interplay between condensate motion and fluid memory, leading to anomalous diffusion, is sophisticated and yields non-trivial predictions.
    4.  The work connects to a broad range of phenomena, from classical phase separation to active matter and intracellular organization.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical Soundness
    - **Claim pointer** The manuscript claims that the derived differential equation for the mean squared displacement (Eq. 9) and its solutions, as shown in Figures 2-5, are correct and lead to the stated predictions of enhanced or suppressed diffusion.
    - **Evidence pointer** Main text Section IV.3, Eq. (9), Appendix E, Appendix H, Figures 2-5.
    - **Concern** The derivation of the central differential equation for the mean squared displacement (Eq. 9) is not presented in sufficient detail to be verified. The transition from the velocity autocorrelation function (Eq. 7) and the series expansion (Eq. 8) to the second-order differential equation (Eq. 9) is a critical step, but the intermediate algebra is largely omitted. The "preaveraging approximation" in Appendix D is a strong assumption that is not fully justified. Furthermore, the numerical solutions presented in Figures 2-5 are not available for inspection, making it impossible to assess the validity of the claimed behaviors (e.g., the plateau in diffusion coefficient, the crossover regimes).
    - **Why it matters** The core quantitative predictions of the manuscript, such as the conditions for enhanced vs. suppressed diffusion and the scaling exponents for coalescence, rest entirely on the correctness of this equation and its solutions. Without a verifiable derivation and visible results, the central claims of the paper cannot be established.
    - **Resolution test** The authors should provide a complete, step-by-step derivation of Eq. (9) in the main text or an appendix. The numerical methods should be described in full detail, and the figures should be provided so that the predicted behaviors can be directly examined. Ideally, the analytical predictions for D0 and D∞ should be compared against direct numerical simulations of the underlying stochastic equations for a simple model system.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific Importance
    - **Claim pointer** The manuscript claims that translation-induced polarization "universally predicts" directed coalescence and that this phenomenon "has not been considered in prior work."
    - **Evidence pointer** Main text Section I, Eq. (2), Section III, Eq. (5).
    - **Concern** While the idea is interesting, the claim of universality and novelty is not fully supported by the presented analysis. The derivation of the dipole-dipole interaction (Eq. 5) relies on a specific form of the Green's function and a far-field approximation. The manuscript does not discuss the limitations of this approximation or the potential for higher-order multipole interactions to alter the predicted behavior at shorter distances. The claim that this has not been considered in prior work is a strong statement that would require a more thorough discussion of the existing literature on interacting domains in phase-separating systems.
    - **Why it matters** The significance of the work hinges on the generality and novelty of the proposed mechanism. If the effect is only present under very specific conditions, or if similar mechanisms have been previously described, the impact of the work is substantially reduced.
    - **Resolution test** The authors should clarify the range of validity of the dipole approximation and discuss potential corrections. They should also provide a more comprehensive review of related work on interactions between moving domains or particles in conserved systems to substantiate the claim of novelty.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Readability for Nonspecialists
    - **Claim pointer** The manuscript aims to provide a framework for understanding condensate dynamics in viscoelastic media, which is relevant to a broad audience in biology and physics.
    - **Evidence pointer** Entire manuscript.
    - **Concern** The manuscript is written in a highly abstract and formal style, with a heavy reliance on mathematical notation and a rapid succession of results. The physical intuition behind the key steps is often not explained. For example, the physical meaning of the "preaveraging approximation" or the origin of the different terms in the final differential equation for the MSD is not made clear. A reader who is not an expert in this specific area of theory would struggle to understand the main contributions and predictions.
    - **Why it matters** For a journal with a broad readership, it is essential that the key concepts and predictions are accessible to a wider audience. The current presentation limits the potential impact of the work.
    - **Resolution test** The authors should add a more extensive physical discussion of the main results, perhaps with a schematic figure illustrating the proposed mechanisms (e.g., translation-induced polarization, surfing vs. trapping). The main predictions should be summarized in a clear, non-technical way.

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Eq. (17) and Appendix G
    - **Evidence pointer** Main text Section IV.5, Eq. (17), Appendix G.
    - **Issue** The estimate for the threshold radius (R < 35 nm) is presented as a concrete number, but the calculation relies on several assumptions (e.g., specific values for mobility, volume fraction difference) that are not clearly stated or justified.
    - **Required correction** The authors should clearly state all parameters used in the estimate and discuss the sensitivity of the threshold radius to these assumptions.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Readability for Nonspecialists
    - **Affected element** Section V (Discussion)
    - **Evidence pointer** Main text Section V.
    - **Issue** The discussion of potential applications (e.g., chemical reactors) is very brief and speculative. The connection to the specific results of the paper is not made clear.
    - **Required correction** The authors should either expand on these ideas with more concrete examples or remove them to keep the discussion focused.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Appendix C
    - **Evidence pointer** Appendix C.
    - **Issue** The discussion of the effect of condensate motion on the fluid flow is presented as a brief comment, but it is a potentially important effect. The claim that it is of order O(Δc²) and decays as 1/M is stated without a full derivation.
    - **Required correction** The authors should provide a more detailed derivation of this result or clearly state it as a conjecture for future work.

## Risk / unsupported claims
- The claim that translation-induced polarization "universally" leads to directed coalescence is not fully supported, as the analysis is based on a specific far-field approximation.
- The quantitative predictions for diffusion coefficients (D0, D∞) and their dependence on parameters (τ_α, τ_f, R) are not verifiable without the figures and a more detailed derivation.
- The claim that the framework is "an ideal starting point" for studying condensate dynamics is an opinion, not a result.
- The estimate of the threshold radius (35 nm) is presented without sufficient justification of the underlying parameters.
- The statement that active stirring can "enable greater control over condensate dynamics" is a speculative interpretation of the theoretical results.