## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors propose a minimal capillary theory linking HIV capsid geometry to nuclear pore complex translocation, predicting geometry-dependent penetration, asymmetric capillary forces, metastable tilted stalled states, topological classification of energetic barriers, and spontaneous symmetry breaking of FG-Nup displacement, with consistency to published cryoelectron tomography orientations and a capillary advantage for the capsid's broken-symmetry geometry
- **Visible evidence base** Abstract text only; no methodological details, equations, numerical results, or experimental comparisons are visible
- **Missing materials affecting confidence** Full manuscript, all figures and tables, supplementary information, derivation details, numerical methods, parameter values, and the specific cryo-ET data used for contact angle estimation

## Reviewer
- **Overall assessment** The abstract presents an intriguing and potentially significant theoretical framework that connects mesoscale capillary physics to a long-standing puzzle in HIV biology. The conceptual leap from wetting phenomena to capsid translocation is compelling and could offer a unifying explanation for observed capsid orientations and the functional advantage of its conical geometry. However, the abstract alone provides insufficient detail to evaluate the rigor of the theory, the validity of the numerical methods, or the strength of the experimental consistency claim. The central assertion of a "capillary advantage" for broken-symmetry geometry is stated but not substantiated with quantitative comparisons. The work is likely to interest both soft matter physicists and virologists, but the current evidence base is too thin to establish the case.
- **Who would be interested in the results, and why** Biophysicists and soft matter theorists studying wetting and capillarity at the mesoscale; virologists investigating HIV nuclear entry and capsid uncoating; cell biologists working on nuclear pore complex transport mechanisms; and researchers in the broader field of virus-host interfacial interactions. The framework could also appeal to theorists developing minimal models for transport through disordered protein barriers.
- **Major strengths** The conceptual framing is original and timely, bridging two previously disconnected fields. The predicted phenomena, particularly metastable tilted stalled states and spontaneous symmetry breaking, are experimentally testable and could guide new imaging or functional studies. The explicit link to published cryo-ET orientations provides a concrete, if preliminary, point of contact with experimental data. The identification of a capillary advantage for the capsid's broken symmetry offers a potential evolutionary or functional rationale that is both elegant and falsifiable.
- **Major Concerns** The abstract does not provide any quantitative results, parameter values, or comparison metrics, making it impossible to assess the predictive power of the theory. The claim of consistency with cryo-ET orientations is vague, as no specific data, error bars, or statistical measures are given. The topological classification of energetic barriers is mentioned but not explained, leaving its physical meaning and utility unclear. The relationship between the model's predictions and the molecular composition of FG-Nups on each side of the pore is asserted but not elaborated. The "capillary advantage" claim requires a quantitative demonstration that the broken-symmetry geometry outperforms symmetric alternatives under realistic conditions.
- **Minor Comments** The abstract would benefit from a clearer statement of the model's assumptions and limitations. The term "minimal theory" is used without specifying what is minimized or what simplifications are made. The phrase "initial estimate of the cytoplasmic contact angle" suggests uncertainty, but the source and magnitude of this uncertainty are not described. The abstract could more explicitly state which predictions are unique to this model versus those that would arise from any capillary treatment.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** Originality is high, as the application of capillary physics to HIV capsid translocation appears novel and conceptually fresh. Scientific importance is potentially substantial, given the central role of nuclear entry in HIV infection and the lack of a mechanistic understanding of capsid geometry. Interdisciplinary readership is plausible, as the work bridges soft matter physics, virology, and cell biology. Technical soundness cannot be assessed from the abstract alone, as no derivations, numerical methods, or validation procedures are visible. Readability for nonspecialists is moderate, with the abstract using field-specific terms (FG-Nups, cryo-ET) without full explanation, though the core ideas are conveyed accessibly. Overall, the work has strong potential but is not yet established from the provided evidence.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The theory makes several predictions including a geometry-dependent trade-off between penetration depth and the wetting transition, asymmetric capillary forces, metastable stalled states, topological classification of barriers, and spontaneous symmetry breaking
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract states that analytical calculations and sharp- and diffuse-interface numerics were used, but provides no equations, boundary conditions, parameter ranges, or convergence criteria. Without these, the physical validity of the model and the robustness of its predictions cannot be evaluated.
- **Why it matters** The core contribution is a theoretical framework, and its credibility rests entirely on the correctness and appropriateness of the mathematical formulation and numerical implementation. Unverifiable numerics render all downstream predictions unsupported.
- **Resolution test** Provide the full derivation, the governing equations, the numerical methods with validation against known limits or benchmarks, and a sensitivity analysis of key parameters.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The results are consistent with published cryoelectron tomography orientations, which provide an initial estimate of the cytoplasmic contact angle
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract does not specify which cryo-ET data were used, how the contact angle was extracted, what the uncertainty is, or how many capsids were analyzed. The word "consistent" is used without any statistical or quantitative backing.
- **Why it matters** This is the only direct experimental anchor in the abstract. If the comparison is weak or selective, the claim of experimental consistency is not meaningful and could mislead readers about the model's validity.
- **Resolution test** Present the specific cryo-ET dataset, the method for angle measurement, the distribution of observed orientations, and a quantitative comparison (e.g., predicted vs. observed angle distributions with confidence intervals).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The results identify a capillary advantage for the HIV capsid's characteristic broken-symmetry geometry
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract asserts a capillary advantage but does not define the comparison baseline. Is the advantage relative to a symmetric cone, a sphere, a cylinder, or some other geometry? What metric defines "advantage" (e.g., lower free energy barrier, faster translocation, higher probability of successful entry)?
- **Why it matters** This is the central biological conclusion of the work. Without a clear definition of the comparator and the performance metric, the claim is unfalsifiable and cannot be assessed for significance.
- **Resolution test** Define the alternative geometries tested, the metric used to quantify advantage, and show quantitative results (e.g., free energy profiles or translocation probabilities) demonstrating the superiority of the broken-symmetry shape.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The model reduces to an interplay between capsid geometry, effective cytoplasmic and nucleoplasmic contact angles, and a ratio of interfacial tensions
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract does not state how the contact angles and interfacial tension ratio are determined. Are they free parameters, derived from molecular properties, or fitted to data? Without this information, the model's predictive power and its connection to molecular reality are unclear.
- **Why it matters** If the parameters are freely adjustable, the model may fit any observation without providing mechanistic insight. The claim of linking capillary physics to capsid geometry requires that the parameters have physical meaning and are constrained by independent evidence.
- **Resolution test** Specify the source of each parameter, whether they are measured, computed from molecular simulations, or fitted, and provide a table of values with uncertainties.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "minimal theory" is used without specifying what is minimized or what simplifications are made relative to more complex models.
- **Required correction** Clarify the scope of the model, listing the key assumptions and simplifications, and state what is deliberately omitted.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract text
- **Evidence pointer** Abstract; location not provided
- **Issue** The phrase "topological classification of the possible mechanisms underlying the largest energetic barrier" is dense and unexplained, making it difficult for nonspecialist readers to grasp its meaning.
- **Required correction** Provide a brief explanation of what the topological classification entails and why it matters for the biological question.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Precision
- **Affected element** Experimental comparison
- **Evidence pointer** Abstract; location not provided
- **Issue** The phrase "initial estimate" for the cytoplasmic contact angle suggests preliminary status, but the abstract does not indicate the level of uncertainty or whether this estimate is robust.
- **Required correction** State the estimated value with its uncertainty and note whether the conclusion is sensitive to this parameter.

## Risk / unsupported claims
- The claim of a "capillary advantage" for the broken-symmetry geometry is unsupported without a defined comparator and quantitative metric
- The claim of consistency with cryo-ET orientations is unsupported without specific data and statistical measures
- All four predicted phenomena (penetration-wetting trade-off, asymmetric forces, stalled states, symmetry breaking) are unverifiable from the abstract alone
- The relationship between model parameters and molecular composition of FG-Nups is asserted but not demonstrated
- The topological classification of energetic barriers is mentioned but not defined or substantiated