## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and figure references.
- **Assessment boundary** Scientific content, methodological soundness, logical consistency, and alignment with claims. Not assessed: language editing, formatting, or journal fit.
- **Shared manuscript claim summary** The authors propose that biomolecular condensates can reshape cellular membranes into tubes, sheets, and cups via capillary forces, governed by interfacial tension and volume-to-area ratio, with shape transitions exhibiting hysteresis and energy barriers. They support this with in planta imaging, in vitro reconstitution, and Monte Carlo simulations.
- **Visible evidence base** In planta confocal and electron microscopy of Arabidopsis vacuoles; in vitro GUV experiments with tunable interfacial tension; Monte Carlo simulations of elastic vesicles; theoretical free-energy calculations.
- **Missing materials affecting confidence** Figure panels referenced but not fully described (e.g., Fig. 1D, Fig. 2D-F, Fig. S4); no raw data or statistical details for frequency measurements; no explicit error analysis for free-energy differences; no details on the analytical model's derivation in the main text.

## Reviewer
- **Overall assessment** This manuscript presents a compelling and timely investigation into condensate-mediated membrane remodeling, combining experimental and computational approaches. The central hypothesis, that capillary forces from condensates drive shape transformations with hysteresis, is well-motivated and supported by qualitative agreement across systems. However, several technical gaps, particularly in the quantitative comparison between in vitro and in silico free energies and the treatment of contact angle effects, weaken the current evidence. The work is of broad interest to biophysics and cell biology, but the case would be strengthened by addressing these concerns.
- **Who would be interested in the results, and why** Biophysicists studying membrane mechanics and phase separation; cell biologists investigating organelle dynamics, particularly vacuole and autophagosome formation; and researchers in soft matter physics interested in capillary interactions. The findings offer a general physical mechanism that could apply to diverse intracellular contexts.
- **Major strengths** 1. Integration of three complementary approaches (in vivo, in vitro, in silico) provides a robust framework. 2. Identification of hysteresis in shape transitions is novel and mechanistically insightful. 3. The morphological diagram offers a predictive tool for understanding condensate-membrane interactions. 4. The work addresses a significant gap in understanding non-equilibrium effects in condensate-mediated remodeling.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative discrepancy in free energies), R1-M2 (contact angle assumption), R1-M3 (statistical rigor in frequency measurements).
- **Assessment against Nature-style criteria** Originality: High. The concept of capillary-driven membrane reshaping with hysteresis is novel and extends prior work on condensate wetting. Scientific importance: High. Provides a general mechanism for organelle morphogenesis, with implications for plant biology and beyond. Interdisciplinary readership: Strong. Bridges cell biology, biophysics, and soft matter physics, making it accessible to a broad audience. Technical soundness: Moderate. The computational and experimental methods are appropriate, but quantitative inconsistencies and missing statistical details reduce confidence. Readability for nonspecialists: Good. The narrative is clear, though some technical sections (e.g., free-energy derivations) may require effort from non-experts.
- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are promising and likely correct, but the quantitative discrepancies and methodological gaps must be addressed to fully establish the case.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative consistency
- **Claim pointer** The authors claim that in vitro and in silico free-energy differences show qualitative agreement, with cups favored at low interfacial tension and sheets at high tension.
- **Evidence pointer** Results section "Membrane shape remodeling and symmetry breaking", Fig. 4B-C
- **Concern** The in vitro and in silico free-energy differences for tubes are contradictory: tubes have the lowest free energy in vitro but the highest in silico. The authors attribute this to model limitations, but the discrepancy is substantial and undermines the quantitative validity of the comparison. Without a more rigorous reconciliation, the claim of qualitative agreement is weakened.
- **Why it matters** The free-energy landscape is central to the paper's mechanistic argument. If the model cannot reproduce experimental energetics for one morphology, the predictive power of the morphological diagram is questionable.
- **Resolution test** Provide a quantitative analysis of the discrepancy, such as sensitivity tests for model parameters (e.g., bending rigidity, interfacial tension range) or inclusion of additional terms (e.g., spontaneous curvature, inter-membrane interactions) to see if the tube free energy can be brought into closer agreement.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Assumption validity
- **Claim pointer** The model assumes a neutral wetting angle of θ = 90° and neglects contact angle variations, stating these are negligible.
- **Evidence pointer** Methods section "Theoretical vesicle model and the role of the contact angle", Fig. S11B
- **Concern** The authors test the neutral wetting assumption but only for a limited range of θ (60°–120°) and conclude robustness. However, the experimental contact angle is not directly measured, and the analytical model's derivation is not fully presented. The claim that contact angle effects are negligible may be premature, especially given the observed discrepancy in tube free energies.
- **Why it matters** If contact angle variations are significant, the model's predictions for shape stability and transitions could be inaccurate, affecting the generalizability of the conclusions.
- **Resolution test** Measure or estimate the contact angle in the in vitro system (e.g., via imaging) and incorporate this into the model. Alternatively, extend the analytical model to a wider θ range and show that conclusions remain unchanged.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor
- **Claim pointer** The authors quantify shape frequencies in vitro across different interfacial tensions and use them to derive free-energy differences.
- **Evidence pointer** Methods section "Equilibrium shape frequencies and shape transitions", Fig. 4A
- **Concern** The frequency measurements are based on 40-70 GUVs per condition, but no error bars, confidence intervals, or statistical tests are reported. The reproducibility across repeats is mentioned but not quantified. This limits the reliability of the derived free-energy differences.
- **Why it matters** The free-energy differences are key quantitative outputs. Without statistical rigor, it is unclear if the observed trends are significant or within experimental noise.
- **Resolution test** Report standard deviations or confidence intervals for frequency measurements and perform statistical tests (e.g., chi-square or bootstrap) to confirm that differences between conditions are significant.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1D
- **Evidence pointer** Results section "In planta observation of interfacial vacuole membranes"
- **Issue** The fluorescence intensity of sheets and cups is stated to be approximately twice that of the surrounding tonoplast, but the quantification method is not described.
- **Required correction** Provide details on how intensity was measured and normalized, or cite a method.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Analytical model derivation
- **Evidence pointer** Methods section "Theoretical vesicle model and the role of the contact angle"
- **Issue** The derivation of free energies for cylindrical tubes, toroidal sheets, and double-spherical cups is referenced to the SI but not summarized in the main text.
- **Required correction** Include a brief outline of the key steps or assumptions in the main text to aid reader comprehension.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Hysteresis discussion
- **Evidence pointer** Results section "Membrane shape remodeling and symmetry breaking"
- **Issue** The claim that hysteresis implies history-dependent behavior is clear, but the biological relevance is not fully discussed. How might this manifest in vivo?
- **Required correction** Add a sentence or two speculating on the physiological implications of hysteresis, e.g., during seed development or stress responses.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Simulation parameters
- **Evidence pointer** Methods section "Computational model"
- **Issue** The simulation temperature and equilibration time are given, but the number of independent runs for the transition simulations is not stated.
- **Required correction** Specify the number of replicates for the MC simulations to assess variability.

## Risk / unsupported claims
- The claim that "shape transformations depend on the history of the elastocapillary force" is supported by simulations but not directly by in vitro experiments, where history is not controlled. This is a gap in experimental validation.
- The statement that "variations in θ are unlikely to fully account for the observed discrepancy" is based on a limited parameter sweep and may be overstated.
- The generalization to other organelles (e.g., Golgi) is speculative and not directly tested, though it is framed as a hypothesis.
- The in planta observation of sheets and cups is qualitative; no quantitative morphometric analysis is provided to support the classification.