## Review setup
- **Input scope** Full manuscript text, including main text, Materials and Methods, and references to SI Appendix and figures.
- **Assessment boundary** Scientific content, technical soundness, internal consistency, and support of claims by the provided evidence. No external literature verification or reproduction of simulations was performed.
- **Shared manuscript claim summary** The authors propose that nonequilibrium phase behaviors in chemically driven fluids, including altered phase diagrams and steady-state diffusive fluxes, originate from interfacial effects. They support this with kinetic Monte Carlo simulations of a minimal lattice model and introduce a microscopic-mesoscopic theory (FLEX) that predicts phase coexistence and interfacial fluctuations without equilibrium assumptions.
- **Visible evidence base** Main text figures (Figs. 1-5), equations (Eqs. 1-13), Materials and Methods, and references to SI Appendix figures (Figs. S1-S10). SI Appendix content itself was not provided.
- **Missing materials affecting confidence** SI Appendix (detailed derivations, alternative reaction schemes, additional data), simulation code (referenced but not inspected), and full figure data. These omissions limit verification of several quantitative claims and the generality statement.

## Reviewer
- **Overall assessment** This manuscript presents a conceptually important and technically solid contribution to the nonequilibrium phase separation field. The central claim, that interfacial effects govern mesoscopic nonequilibrium behaviors, is well supported by the simulation evidence shown. The proposed theory is a significant step beyond equilibrium-based approaches and is validated across multiple observables. However, the manuscript's reliance on the SI Appendix for key derivations and alternative scheme tests, combined with some unquantified claims, leaves certain aspects not fully assessable from the provided material. The work is likely to be of high interest to the condensate and active matter communities.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, particularly those interested in nonequilibrium or ATP-driven behaviors. Also, the broader soft matter and active matter communities, as the work provides a tractable theoretical framework for nonequilibrium phase coexistence. The connection between microscopic interfacial statistics and mesoscopic fluxes is a general result that could inform future experimental and theoretical studies.
- **Major strengths**
  1. The central insight, that interfacial effects rather than bulk properties determine nonequilibrium phase behavior, is clearly articulated and convincingly demonstrated by the simulation data.
  2. The theoretical framework (FLEX) is a novel and practical approach that avoids effective equilibrium assumptions, and its predictions match simulations across multiple observables (coexistence curves, fluxes, fluctuations).
  3. The study systematically connects microscopic quantities (non-Boltzmann statistics, entropy production) to mesoscopic observables (fluxes, interfacial tension), providing a mechanistic understanding.
  4. The manuscript is well-written and logically structured, with a clear narrative from observation to theory to validation.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness / Evidence sufficiency
  - **Claim pointer** The authors claim the theory "predicts accurate phase diagrams for both macroscopic and finite-size droplets" and provides "quantitative agreement" with simulations.
  - **Evidence pointer** Figure 4A-C, Figure 5A-B, and associated text. SI Appendix Figs. S6-S7 referenced but not provided.
  - **Concern** The quantitative agreement between theory and simulation is asserted, but the provided figures are not accompanied by quantitative error metrics or statistical measures. The text states "good agreement" and "quantitative agreement" without specifying the magnitude of deviations. Furthermore, the theory's predictive accuracy for finite-size droplets relies on fitting the interfacial tension (σ) as a single free parameter (Figure 5C), which weakens the claim of being "first-principles" and predictive. The validation of this fitting procedure and its uniqueness is not fully discussed.
  - **Why it matters** The central contribution is a predictive theory. Without clear quantitative validation metrics, the reader cannot assess the theory's accuracy or limitations. The fitting of σ, while reasonable, needs justification that it is not merely absorbing model error.
  - **Resolution test** Provide quantitative error bars or deviation measures for the theory-simulation comparisons in Figures 4 and 5. Discuss the sensitivity of the theory to the fitted σ value and demonstrate that the fit is well-constrained. If possible, show a prediction for σ from the theory without fitting.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Generalizability / Claim scope
  - **Claim pointer** The authors state that "these central conclusions can be straightforwardly extended to alternative concentration-dependent reaction schemes with one or more driven pathways."
  - **Evidence pointer** SI Appendix, Fig. S7 (referenced but not provided).
  - **Concern** The generality of the results is a key selling point, but the evidence for it is entirely delegated to the SI Appendix, which was not provided for review. The main text only demonstrates one specific reaction scheme (Eq. 1). The claim of "straightforward extension" is plausible but not verifiable from the provided material.
  - **Why it matters** The significance of the work is substantially increased if the conclusions are general. Without seeing the alternative scheme results, the reader cannot judge whether the observed phenomena are specific to the chosen model or robust features of chemically driven fluids.
  - **Resolution test** Include a summary of the alternative scheme results in the main text, or provide the SI Appendix for review. At minimum, explicitly state the range of schemes tested and any qualitative differences observed.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness / Interpretation
  - **Claim pointer** The authors interpret the inferred interfacial tension (σ) as a nonequilibrium property and correlate it with capillary fluctuations (Figure 5C).
  - **Evidence pointer** Figure 5C, and the discussion of capillary fluctuations in Figure 3A and the text.
  - **Concern** The relationship between the fitted σ and the measured capillary fluctuations is presented as a correlation, but the causal or theoretical link is not fully established. The text states the slope of the linear trend in Figure 5C is "not unity" and attributes this to breakdown of equilibrium scaling, but does not provide a theoretical model for this relationship. The interpretation of σ as a genuine interfacial tension, distinct from an equilibrium one, needs more theoretical support.
  - **Why it matters** The concept of a nonequilibrium interfacial tension is central to the paper's implications. If the fitted parameter is not rigorously connected to a physical interfacial tension, the interpretation of the results could be questioned.
  - **Resolution test** Provide a theoretical derivation or a more detailed discussion of how the nonequilibrium σ relates to the capillary fluctuation spectrum. Address why the slope in Figure 5C is not unity and what determines its value.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity / Reproducibility
  - **Affected element** Simulation parameters and initialization
  - **Evidence pointer** Materials and Methods, Simulation Model.
  - **Issue** The description of the simulation initialization states that the system is "relaxed to steady state over 5×10^5 sweeps" and measurements are "accumulated over another 10^6 sweeps." It is unclear how the steady state is verified and whether the equilibration time is sufficient for all parameter sets, particularly for large droplets or slow diffusion.
  - **Required correction** Specify the criteria used to determine that the steady state has been reached. Provide evidence (e.g., convergence of measured quantities over time) or cite prior work for the chosen equilibration times.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Clarity / Technical soundness
  - **Affected element** Definition of interfacial tension
  - **Evidence pointer** Materials and Methods, and Figure 5C.
  - **Issue** The method for extracting the interfacial tension σ from finite-size droplet simulations is described briefly. It is stated that σ is the "sole fitting parameter," but the exact fitting procedure (e.g., least-squares fit to what function?) is not detailed.
  - **Required correction** Provide the explicit fitting function and procedure used to extract σ from the data in Figure 5A-B.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Readability / Interpretation
  - **Affected element** Figure 2 decomposition
  - **Evidence pointer** Figure 2B-C and associated text.
  - **Issue** The decomposition of fluxes into "bulk dilute phase" and "interfacial" contributions is clear, but the text states the condensed phase contribution is "less than 0.1% of the total and is thus not plotted." It would be helpful to state whether this is a general result or specific to the conditions shown.
  - **Required correction** Clarify whether the negligible condensed-phase contribution is expected for all conditions studied or is a specific observation.
- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Lack of quantitative error metrics for theory-simulation comparisons.
  - R1-M2: Generality claim not verifiable without SI Appendix.
  - R1-M3: Theoretical basis for the nonequilibrium interfacial tension and its relation to fluctuations is underdeveloped.
- **Assessment against Nature-style criteria**
  - **Originality** High. The work presents a new theoretical framework (FLEX) for nonequilibrium phase coexistence and identifies interfacial effects as the primary origin of nonequilibrium behavior, which is a novel perspective.
  - **Scientific importance** High. The results have direct implications for understanding biomolecular condensates and other chemically driven fluids, providing a quantitative framework that goes beyond equilibrium assumptions.
  - **Interdisciplinary readership** Broad. The work bridges statistical physics, soft matter, and cell biology, and is likely to attract readers from all these fields.
  - **Technical soundness** Generally strong, but with the caveats noted in R1-M1 and R1-M3. The simulation methodology is appropriate, and the theory is well-motivated. The lack of quantitative validation metrics and the fitting of σ are the main weaknesses.
  - **Readability for nonspecialists** Good. The manuscript is clearly written, with a logical flow and helpful figures. The significance and main results are accessible, although the theory section is necessarily technical.
- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are novel and important, and the evidence presented is largely convincing. However, the lack of quantitative validation metrics (R1-M1), the unverifiable generality claim (R1-M2), and the underdeveloped theoretical basis for the nonequilibrium interfacial tension (R1-M3) need to be addressed before the case is fully established.

## Risk / unsupported claims
- The claim that the theory provides "quantitative agreement" with simulations is not supported by quantitative metrics in the provided material.
- The claim that conclusions extend "straightforwardly" to alternative reaction schemes is not assessable without the SI Appendix.
- The interpretation of the fitted parameter σ as a physical nonequilibrium interfacial tension is plausible but not rigorously established.
- The statement that the theory "predicts accurate phase diagrams" is supported for the shown conditions, but the range of validity (e.g., proximity to critical points) is not fully explored in the main text.