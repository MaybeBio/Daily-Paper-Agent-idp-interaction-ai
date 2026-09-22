## Review setup
- **Input scope** Full manuscript text (Introduction, Model, Scaling Arguments, Linear Stability Analysis, 3D Simulations, Anisotropic Transport, Biological Implications, Conclusion, Appendix A) with figure captions referenced but figures not provided.
- **Assessment boundary** Scientific validity, technical soundness, and clarity of the proposed transport-driven microphase separation mechanism; consistency between analytical predictions, simulation results, and biological claims.
- **Shared manuscript claim summary** The authors propose that stochastic binding of phase-separating proteins to motor proteins, followed by active transport along cytoskeletal filaments, generates an effective long-range repulsion that arrests coarsening and selects finite condensate sizes. They derive scaling laws, confirm predictions via 3D simulations, and extend the mechanism to anisotropic transport, predicting morphological transitions.
- **Visible evidence base** Analytical derivations (scaling arguments, linear stability analysis), 3D simulation results (Figures 3 and 4 referenced), and parameter estimates for biological relevance (Figure 5 referenced). Figures themselves not provided.
- **Missing materials affecting confidence** Figures 1–5, SI Appendix (including derivations, simulation details, and supplementary figures), and Table 1 are referenced but not included. This limits verification of quantitative claims and simulation quality.

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting and potentially significant mechanism for condensate size control via motor-mediated active transport. The analytical framework is elegant, and the scaling predictions are clearly stated. However, the absence of figures and SI material prevents full verification of the simulation results and the quantitative accuracy of the predictions. The biological relevance claims, while plausible, require more careful consideration of parameter regimes and alternative interpretations.
- **Who would be interested in the results, and why** Researchers in phase separation, biophysics of intracellular organization, active matter physics, and synthetic biology. The mechanism offers a new, thermodynamically independent route to control condensate size and shape, which is relevant for understanding cellular organization and for designing synthetic emulsions.
- **Major strengths** 1) The mechanism is conceptually novel and distinct from chemical reaction-diffusion or mechanical confinement approaches. 2) The analytical framework provides clear, testable scaling predictions. 3) The extension to anisotropic transport and morphological transitions adds depth. 4) The robustness to noise is explicitly addressed.
- **Major Concerns** 1) The mapping of the nonequilibrium model to an effective equilibrium free energy (Ohta-Kawasaki type) requires careful justification, especially regarding the validity of the fluctuation-dissipation violation. 2) The discrepancy between the predicted and simulated transition point (e_c) is noted but not fully explained. 3) The biological parameter estimates (e.g., motor binding rates, transport velocities) are not rigorously justified. 4) The claim that the mechanism operates "independently of thermodynamic parameters" is overstated, as the phase diagram still depends on τ and the quench depth.
- **Minor Comments** 1) The notation for the effective free energy and the rescaled parameters could be clarified for nonspecialist readers. 2) The discussion of the Lifshitz point and its connection to the Ohta-Kawasaki functional is brief and could be expanded. 3) The biological implications section would benefit from more concrete experimental predictions or falsifiable tests.
- **Technical failings that need to be addressed before the case is established** 1) The validity of the effective equilibrium mapping in the presence of noise (fluctuation-dissipation violation) needs rigorous justification. 2) The quantitative agreement between the linear stability prediction and simulation results for the transition point needs to be demonstrated with figures. 3) The parameter regime for biological relevance (e.g., e_c values, transport velocities) needs to be grounded in experimental measurements or realistic estimates.
- **Assessment against Nature-style criteria**  
  *Originality*: High. The mechanism is a novel addition to the toolkit of condensate size control.  
  *Scientific importance*: Potentially high, as it addresses a fundamental question in cellular organization and offers a new design principle for synthetic systems.  
  *Interdisciplinary readership*: The topic bridges biophysics, cell biology, and soft matter physics, appealing to a broad audience.  
  *Technical soundness*: The analytical framework is sound, but the simulation and parameter-estimation aspects require verification with the missing figures and SI.  
  *Readability for nonspecialists*: The main text is generally clear, but the mathematical sections (Scaling, Linear Stability) may be challenging for readers without a physics background. A more intuitive explanation of the effective long-range repulsion would help.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising, but the manuscript currently lacks the necessary figures and SI to fully establish the quantitative claims. The authors should address the validity of the effective equilibrium mapping and provide a more rigorous grounding of the biological parameter estimates.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the nonequilibrium model can be mapped onto an equilibrium model with an effective free energy (Eq. 7), enabling the use of equilibrium concepts like the Ohta-Kawasaki functional.
- **Evidence pointer** Section IV, Eq. 7, and the surrounding text.
- **Concern** The mapping to an effective equilibrium free energy is a central step in the analytical framework. However, the manuscript acknowledges that the stochastic term violates the fluctuation-dissipation relation, meaning the effective free energy is not a true thermodynamic potential. The conditions under which this mapping is valid (e.g., small noise, specific parameter regimes) are not clearly stated. Without a rigorous justification, the predictive power of the linear stability analysis based on this mapping is questionable.
- **Why it matters** If the effective equilibrium mapping is not valid, the predicted phase diagram and scaling laws may not hold in the actual nonequilibrium steady state. This would undermine the core quantitative claims of the manuscript.
- **Resolution test** The authors should provide a detailed derivation or argument showing under what conditions the effective free energy approach is valid, possibly by comparing the linear stability predictions with full simulations of the original nonequilibrium model across a range of parameters. Alternatively, they could derive the linear stability criterion directly from the original equations without the equilibrium mapping.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The manuscript claims that 3D simulations confirm the analytical predictions for the onset of microphase separation and the scaling of domain size with binding rate (L ∼ b^{-1/4}).
- **Evidence pointer** Section V, Figure 3, and the associated text.
- **Concern** The figures are not provided, so the quantitative agreement between the linear stability prediction and the simulation results cannot be assessed. The text notes a discrepancy: the transition from microphase to macrophase separation occurs at a higher value of e than theoretically predicted. This discrepancy is not explained. It is crucial to know whether this is a quantitative shift (e.g., due to noise or finite-size effects) or a qualitative failure of the theory.
- **Why it matters** The central claim of the manuscript is that the theory quantitatively predicts the simulation outcomes. If the agreement is only qualitative, the predictive power of the scaling laws is weakened. The unexplained discrepancy raises concerns about the completeness of the theoretical framework.
- **Resolution test** The authors should provide the figures and a detailed discussion of the discrepancy, including possible sources (e.g., finite-size effects, noise, the approximation of replacing F[ρ] by F[ρ1]). They should also show the scaling law L ∼ b^{-1/4} is robustly reproduced in simulations across a range of parameters.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Biological relevance
- **Claim pointer** The manuscript claims that the mechanism operates at "minute motor-bound protein fractions" and that tuning binding rates can adjust condensate sizes from nanometers to micrometers, with implications for cellular regulation.
- **Evidence pointer** Section VII, Figure 5, and the associated text.
- **Concern** The biological parameter estimates (e.g., s = 0.1 s^{-1}, e_c values) are not rigorously justified. The manuscript states that e_c scales as 1/λ^2, but the actual values of λ for intracellular transport are not discussed. The claim that the mechanism is "independent of thermodynamic parameters" is misleading, as the phase diagram still depends on τ and the quench depth. The biological relevance would be strengthened by a more careful discussion of realistic parameter ranges and a comparison with other known mechanisms.
- **Why it matters** The manuscript aims to provide a mechanism relevant to cellular biology. If the parameter regime for microphase separation is not biologically accessible, the significance of the work is diminished. Overstated claims about independence from thermodynamics could mislead readers.
- **Resolution test** The authors should provide a table or figure showing realistic ranges of motor binding rates, transport velocities, and diffusion constants in cells, and demonstrate that the predicted microphase separation regime falls within these ranges. They should also clarify the role of thermodynamic parameters in setting the overall phase behavior.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Introduction of the effective free energy and rescaled parameters
- **Evidence pointer** Section IV, Eq. 7, and the surrounding text.
- **Issue** The notation for the effective free energy and the rescaled parameters (e.g., λ̂, ŝ, τ) is introduced quickly and may be confusing for readers not familiar with the Foret model or similar approaches.
- **Required correction** Provide a brief intuitive explanation of the effective free energy and the physical meaning of each rescaled parameter, perhaps in a table or a dedicated paragraph.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion of the Lifshitz point
- **Evidence pointer** Section IV, last paragraph.
- **Issue** The connection to the Ohta-Kawasaki functional and the Lifshitz point is mentioned but not elaborated. This is a key conceptual link that could help readers understand the phase behavior.
- **Required correction** Expand the discussion of the Lifshitz point and its implications for the phase diagram, possibly with a schematic figure.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Biological implications section
- **Evidence pointer** Section VII.
- **Issue** The section is somewhat speculative and lacks concrete, falsifiable predictions. The statement that "approaches offer a direct experimental knob" is vague.
- **Required correction** Provide specific experimental predictions, such as the expected dependence of condensate size on motor concentration or the conditions under which elongated morphologies should appear.

## Risk / unsupported claims
- The claim that the mechanism operates "independently of thermodynamic parameters" is not fully supported, as the phase behavior still depends on τ and the quench depth.
- The quantitative agreement between the linear stability prediction and simulation results for the transition point is not verifiable without the figures.
- The biological relevance of the predicted parameter regime (e.g., e_c values, transport velocities) is not rigorously established.
- The validity of the effective equilibrium mapping in the presence of noise is not rigorously justified.