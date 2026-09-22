## Review setup
- **Input scope** Full manuscript text including main text, methods, and supplemental figure descriptions
- **Assessment boundary** Scientific validity, methodological soundness, claims versus evidence, and suitability for the stated journal context
- **Shared manuscript claim summary** The authors propose the Bethe-Peierls (cavity) approximation as a superior mean-field approach for modeling biomolecular condensate phase separation, demonstrating quantitative agreement with lattice simulations in binary and ternary systems, and showing that the regular solution model fails qualitatively in ternary cases with mixed interactions. They further apply the approach to infer interaction parameters from experimental coacervation data of poly-lysine and ADP, including a successful prediction of re-entrant phase behavior.
- **Visible evidence base** Main text equations (1-12), Figures 1-6, STAR Methods derivations, experimental phase diagram data, Monte Carlo simulation descriptions, and code availability statement
- **Missing materials affecting confidence** Full experimental dataset (raw microscopy images, replicate counts), complete parameter ranges explored in inference, uncertainty quantification on inferred parameters, and detailed comparison statistics beyond the stated accuracy percentages

## Reviewer

### Overall assessment
This manuscript presents a potentially valuable application of cavity methods to biomolecular condensate phase separation, addressing a genuine need for approaches that go beyond simple mean-field models. The binary system validation is convincing, and the demonstration that the regular solution model fails in ternary systems with mixed interactions is an important contribution. However, the manuscript has several significant weaknesses that must be addressed before the central claims can be considered fully established. The experimental comparison relies on a single system with limited parameter exploration, the inference procedure lacks rigorous uncertainty quantification, and the claimed "prediction" of re-entrance requires clearer articulation of what was known versus predicted at the time of inference. The computational efficiency claims, while plausible, are not systematically documented. The work is interesting and likely publishable after substantial revision, but the current evidence base does not fully support all stated conclusions.

### Who would be interested in the results, and why
Researchers in biophysics and soft matter physics studying phase separation, particularly those working on biomolecular condensates and membraneless organelles, would find this work relevant. The methodological comparison between cavity methods and regular solution models addresses a known limitation in the field. Researchers in the origins-of-life community studying coacervation as a prebiotic compartmentalization mechanism would also be interested in the experimental system and the inference approach. Additionally, the statistical physics community working on disordered systems and mean-field approximations may find the application of Bethe-Peierls methods to this new domain of interest.

### Major Strengths
1. The manuscript addresses a real and recognized limitation of standard mean-field approaches (regular solution model) in capturing phase behavior of heterogeneous multicomponent systems.
2. The binary system validation provides a clear, quantitative demonstration of the improvement offered by the cavity method over the regular solution model.
3. The ternary system analysis correctly identifies a case where the regular solution model fails qualitatively, not just quantitatively.
4. The application to experimental data, including the inference of interaction parameters and the subsequent prediction of re-entrant behavior, represents a meaningful step toward inverse modeling in this field.
5. The computational efficiency of the approach (solving algebraic equations versus full simulations) is a practical advantage worth highlighting.
6. The manuscript is generally well-organized and the mathematical derivations in the methods are presented with sufficient detail for reproduction.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency for experimental validation
- **Claim pointer** The manuscript claims that the inferred model reproduces the experimental phase diagram with 97% accuracy and that this validates the cavity method approach for experimental systems.
- **Evidence pointer** Figure 4, "Modeling experiments" section
- **Concern** The experimental validation rests on a single system (poly-lysine and ADP at pH 9.0) with a single set of inferred parameters. The 97% accuracy figure is presented without clear definition of what constitutes "accuracy" in this context (pixel-level agreement? phase boundary location? classification rate?). No error bars or confidence intervals are provided for the inferred parameters J++, J--, and J-+. The inference procedure's sensitivity to initial conditions, optimization algorithm settings, and the choice of which experimental points to include are not discussed. Furthermore, the mapping between the lattice model volume fractions and experimental concentrations is not rigorously justified.
- **Why it matters** Without uncertainty quantification and a clear definition of the accuracy metric, the claim that the model "reproduces" the experimental phase diagram cannot be properly evaluated. The inference of three interaction parameters from a single phase diagram may be underdetermined, and the reported accuracy could reflect overfitting rather than genuine predictive power.
- **Resolution test** Provide: (1) a precise definition of the accuracy metric used; (2) confidence intervals or posterior distributions for the inferred parameters; (3) a sensitivity analysis showing how the inferred parameters and resulting phase diagram change with different optimization runs or initial conditions; (4) validation of the concentration-to-volume-fraction mapping; and (5) ideally, application to at least one additional experimental system or condition to demonstrate generalizability.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim substantiation for the "prediction" of re-entrance
- **Claim pointer** The manuscript states that the inferred model predicted re-entrant phase behavior at high concentrations, which was subsequently confirmed experimentally, and presents this as a successful non-trivial prediction.
- **Evidence pointer** Figure 5, "Predicted re-entrance in the experimental phase diagram" section
- **Concern** The timeline and logic of the "prediction" are not clearly established. Was the re-entrance predicted before the experiments at those concentrations were performed, or was the model fitted to data that already included some indication of re-entrance? The manuscript states that the binding energies were "inferred in the first part of the phase diagram, apparently showing no sign of re-entrance," but this is not demonstrated. The experimental data shown in Figure 5 covers a wide concentration range; if any of these points were used in the inference, the claim of prediction is weakened. Additionally, the physical mechanism for the predicted re-entrance is not explained.
- **Why it matters** The re-entrance prediction is presented as a key success of the approach. If the prediction claim is not rigorously established, this weakens the case for the method's predictive power. The distinction between interpolation and extrapolation is critical here.
- **Resolution test** Clearly state: (1) which experimental data points were used for inference versus which were reserved for validation; (2) the exact timeline of prediction versus experimental confirmation; (3) the model's predicted phase diagram before the confirmation experiments were conducted; and (4) a physical explanation for why re-entrance occurs in this system according to the model.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness of the ternary phase diagram classification
- **Claim pointer** The manuscript claims that the cavity method classifies simulation results with 88% accuracy in the ternary system and that this demonstrates the method's ability to capture the three modes of phase separation (associative, segregative, counter-ionic).
- **Evidence pointer** Figure 3, "Ternary system" section, "Further details on the comparison between the cavity method results and numerical simulations" section
- **Concern** The 88% accuracy figure is presented without details on how this was computed. What is the confusion matrix? Are all three phase separation modes equally well classified, or is the accuracy dominated by one mode? The phase diagrams in Figure 3 show qualitative agreement, but the quantitative claim of 88% accuracy requires a clear methodology. Additionally, the choice of interaction parameters for the three cases (associative, segregative, counter-ionic) is not systematically varied or justified.
- **Why it matters** The quantitative accuracy claim is a central part of the paper's contribution. Without a clear methodology for computing this figure, it cannot be independently verified or compared with other approaches.
- **Resolution test** Provide: (1) the exact procedure for computing classification accuracy (including how phase-separated vs. well-mixed states were determined from simulation snapshots); (2) a confusion matrix or per-mode accuracy breakdown; (3) sensitivity of the accuracy to the choice of interaction parameters; and (4) a description of how the threshold for the phase separation measure was calibrated.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the approach
- **Claim pointer** The manuscript suggests that the cavity method is a general tool for modeling biomolecular condensates, with the ternary case serving as a demonstration of its broader applicability.
- **Evidence pointer** Discussion section, "Ternary system" section
- **Concern** The manuscript only demonstrates the method on binary and ternary systems with specific interaction symmetries. Real biomolecular condensates involve many components with heterogeneous interactions, sequence-specific effects, and non-equilibrium processes. The claim that this approach "paves the way" for such systems is not supported by any demonstration or even a detailed discussion of how the method would scale to larger numbers of components or more complex interaction structures. The computational complexity of the cavity equations for general interaction matrices is not analyzed.
- **Why it matters** The broader significance of the work depends on its applicability to realistic biological systems. If the method cannot scale or handle realistic complexity, its impact is limited to simple model systems.
- **Resolution test** Provide a discussion of: (1) computational scaling with number of components; (2) how the method would handle asymmetric interaction matrices or multi-body interactions; (3) potential limitations for systems with long-range interactions or spatial heterogeneity; and (4) a concrete roadmap for applying the method to a more realistic biological system.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** "Cavity methods" versus "Bethe-Peierls approximation"
- **Evidence pointer** Throughout
- **Issue** The terms "cavity methods," "Bethe-Peierls approximation," and "belief propagation" are used somewhat interchangeably. While related, these are distinct concepts in statistical physics, and the relationship should be clarified for readers who may not be specialists.
- **Required correction** Add a brief paragraph in the introduction or methods clarifying the relationship between these concepts and specifying which variant is being used in this work.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility of experimental methods
- **Affected element** Experimental section
- **Evidence pointer** "Experimental methods" section
- **Issue** The experimental description lacks several details needed for reproduction: the concentration ranges tested, the number of replicate wells per condition, the criteria for visual classification of phase separation, and the temperature control during imaging.
- **Required correction** Add these details to the methods section or supplementary information.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Figure quality and information content
- **Affected element** Figure 3
- **Evidence pointer** Figure 3
- **Issue** The phase diagrams in Figure 3 are difficult to compare across methods because the color scales and contour levels are not consistent. The reader cannot easily assess where the cavity method and simulations agree or disagree.
- **Required correction** Use consistent color scales and contour levels across panels, and consider overlaying the simulation results on the cavity method predictions for direct comparison.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Statistical rigor in simulation analysis
- **Affected element** Simulation results
- **Evidence pointer** "Further details on numerical simulations" section
- **Issue** The manuscript does not report the number of independent simulation runs or the statistical uncertainty in the measured phase boundaries. Given the stochastic nature of Monte Carlo simulations, this is important for assessing the significance of the agreement with the cavity method.
- **Required correction** Report the number of independent runs and provide error bars or confidence intervals on the simulation results.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Accessibility of the inference procedure
- **Affected element** Parameter inference section
- **Evidence pointer** "Modeling experiments" section
- **Issue** The differential evolution optimization procedure is mentioned but not described in sufficient detail. The objective function, constraints, and convergence criteria are not specified.
- **Required correction** Provide a more detailed description of the inference procedure, including the objective function and any constraints on the parameter space.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Evidence pointer** "Discussion" section
- **Issue** The discussion of the mean-field nature of the cavity method and its known limitations (e.g., inaccuracies near critical points, neglect of long-range correlations) is brief. A more thorough discussion would help readers understand the regime of validity of the approach.
- **Required correction** Expand the discussion of limitations, particularly regarding the accuracy of the method near critical points and for systems with strong correlations.

### Technical failings that need to be addressed before the case is established
1. The experimental validation lacks uncertainty quantification and clear accuracy metrics (R1-M1).
2. The "prediction" of re-entrance is not clearly established as a genuine prediction versus post-hoc fitting (R1-M2).
3. The 88% classification accuracy claim lacks methodological detail (R1-M3).
4. The generalizability claims are not supported by demonstrations or analysis (R1-M4).

### Assessment against Nature-style criteria
- **Originality**: The application of cavity methods to biomolecular condensates is a novel contribution. While the underlying statistical physics is well-established, the domain of application and the systematic comparison with the regular solution model in ternary systems provides a new perspective. The work does not introduce fundamentally new physics but offers a methodological advance.
- **Scientific importance**: The work addresses a genuine need in the condensate field for approaches that go beyond simple mean-field models. The demonstration that the regular solution model fails qualitatively in certain ternary systems is important and should influence future modeling choices. However, the impact is somewhat limited by the simplicity of the model systems considered.
- **Interdisciplinary readership**: The work bridges statistical physics, biophysics, and origins-of-life research. The experimental component with poly-lysine and nucleotides makes it accessible to a broader biological audience. However, the mathematical derivations may be challenging for non-specialists, and the biological implications could be more clearly articulated.
- **Technical soundness**: The mathematical derivations appear correct, and the binary system validation is convincing. However, the experimental validation and the quantitative accuracy claims require more rigorous treatment. The lack of uncertainty quantification is a significant weakness.
- **Readability for nonspecialists**: The manuscript is generally well-written, but the methods section is dense and assumes familiarity with statistical physics. The biological motivation and implications could be strengthened. The figures are informative but could be improved for cross-method comparison.

### Recommendation posture
Supportive if technical concerns are resolved. The core methodological contribution is sound and the binary system validation is convincing. However, the experimental validation, the prediction claim, and the quantitative accuracy assessments require substantial strengthening before the central claims can be considered fully established. The work has the potential to be a useful contribution to the field, but the current evidence base does not fully support all stated conclusions.