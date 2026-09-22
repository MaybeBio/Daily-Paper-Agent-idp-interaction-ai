## Review setup
- **Input scope** Full manuscript text, including main text, appendices, and figure captions (figures themselves not provided).
- **Assessment boundary** Scientific validity, methodological soundness, clarity of claims, and alignment with stated conclusions. No assessment of formatting or journal fit beyond general scope.
- **Shared manuscript claim summary** The authors propose that a low-concentration "programmable surfactant" protein species, which interacts with components of two immiscible biomolecular condensates, can act as a tunable switch to control the morphology of multiphase condensates. They support this claim using lattice-model Monte Carlo simulations, classical density functional theory (CDFT), and a simplified analytical adsorption model, and they derive design rules for triggering wetting transitions between dispersed and docked morphologies.
- **Visible evidence base** Main text Sections I–VI; Appendices A–F; Figures 1–6 (captions only); Figure A1–A2 (captions only); Equations 1–33.
- **Missing materials affecting confidence** Actual figure images and numerical data underlying the plots are not provided. Simulation code and parameter values are not fully specified in the text. Experimental validation is absent, which the authors acknowledge.

## Reviewer
- **Overall assessment** This manuscript presents a theoretically and computationally rigorous study of a plausible mechanism for controlling multiphase condensate morphology via low-abundance "surfactant" proteins. The combination of lattice simulations, CDFT, and an analytical adsorption model is commendable and provides a coherent, multi-level picture. The central claim—that weak, low-concentration bridging species can trigger wetting transitions—is well supported by the model evidence presented. However, the direct biological relevance is inferred rather than demonstrated, and the quantitative accuracy of the CDFT approach is limited. The work is likely to be of interest to the biomolecular condensate and soft matter communities, and it offers testable predictions. The main weaknesses are the lack of experimental validation and the reliance on a highly coarse-grained model. Overall, this is a solid contribution that would benefit from clearer articulation of its limitations and a more direct connection to experimental systems.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, particularly those interested in multiphase architectures, phase separation regulation, and the role of scaffold/client proteins. Also relevant to the soft matter physics community working on wetting, surface tension, and multicomponent mixtures. The design rules and computational methods could inform experimental design in synthetic biology and cell biology.
- **Major strengths**
    1.  The study addresses a timely and important question: how multiphase condensate morphology is regulated at the molecular level.
    2.  The multi-method approach (simulation, CDFT, analytical model) provides a robust and cross-validated theoretical framework.
    3.  The identification of a "programmable surfactant" mechanism is novel and provides a concrete, testable hypothesis for biological regulation.
    4.  The derivation of design rules (e.g., minimum binding strength, low concentration requirement) is practically useful.
    5.  The manuscript is generally well-written and logically structured, with technical details appropriately relegated to appendices.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** No
    - **Axis** Biological relevance and model generalizability
    - **Claim pointer** The authors state in the Discussion that their insights "can be applied directly to protein/RNA interaction networks that underlie the phase behavior of multiphase biomolecular condensates" and specifically propose DDX6 as a candidate surfactant in the SG/PB system.
    - **Evidence pointer** Section VI (Discussion); Figure 1A
    - **Concern** The leap from a highly coarse-grained lattice model to a specific biological prediction (DDX6 in SG/PB) is significant. The model uses only three species with simplified interactions and does not account for the complexity of real protein/RNA networks, including post-translational modifications, RNA sequence specificity, or the viscoelastic properties of condensates. The claim of direct applicability is therefore overstated.
    - **Why it matters** The central motivation for the study is biological relevance. If the model's predictions do not translate to real systems, the impact of the work is substantially diminished. Overstating the connection could mislead experimentalists.
    - **Resolution test** The authors should either (a) temper the language to "may be applicable" and explicitly list the assumptions that would need to hold for the model to apply, or (b) provide a more detailed mapping of model parameters to known biophysical properties of DDX6 and its interaction partners, even if approximate.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Quantitative accuracy of CDFT predictions
    - **Claim pointer** The authors state that CDFT "reproduces our simulation results semi-quantitatively" (Section V.1) and use CDFT to predict the location of the wetting transition.
    - **Evidence pointer** Section V.2; Figures 4 and 5
    - **Concern** The CDFT approach requires a regularization of the square-gradient coefficient matrix, which is a significant approximation. The authors note that CDFT underestimates the interaction strength required for wetting compared to simulations. The magnitude of this discrepancy is not quantified, and it is unclear whether the CDFT predictions are accurate enough to be used for quantitative design.
    - **Why it matters** The CDFT method is presented as a complementary, faster alternative to simulation. If its quantitative predictions are unreliable, its utility for screening parameter space is limited.
    - **Resolution test** The authors should provide a quantitative measure of the discrepancy between CDFT and simulation predictions (e.g., percentage difference in critical interaction strength) across the parameter range studied. They should also discuss the conditions under which the regularization is expected to be valid.
    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Robustness of the adsorption model
    - **Claim pointer** The authors claim that the analytical adsorption model "explains all the essential features of our wetting phase diagrams" (Section V.5).
    - **Evidence pointer** Section V.5; Figure 6
    - **Concern** The adsorption model relies on several assumptions, including a Langmuir isotherm and specific forms for the entropic and enthalpic contributions. The derivation of the key result, Eq. (13), is not shown in detail, and the model's parameters are not directly linked to the underlying lattice model parameters. It is unclear how predictive this model is beyond the specific cases tested.
    - **Why it matters** The adsorption model is intended to provide intuitive design rules. If its assumptions are too restrictive, the rules may not generalize.
    - **Resolution test** The authors should provide a more complete derivation of the adsorption model, including the assumptions and approximations made. They should also test the model's predictions against a wider range of simulation data, including cases with non-zero homotypic B–B interactions.
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity of model motivation
    - **Affected element** Section II (Minimal model)
    - **Evidence pointer** Figure 1
    - **Issue** The choice of the specific lattice model parameters (e.g., interaction strengths, volume fractions) is not fully justified. Why these particular values?
    - **Required correction** Provide a brief justification for the parameter choices, perhaps referencing typical values for protein-protein interactions or stating that the results are robust to parameter variations.
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Presentation of simulation details
    - **Affected element** Appendix A
    - **Evidence pointer** Appendix A
    - **Issue** The equilibration time is stated as 5000 MC sweeps, but it is not clear how this was determined to be sufficient.
    - **Required correction** Briefly describe the equilibration criterion (e.g., monitoring the stability of the order parameter or energy).
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Definition of wetting transition
    - **Affected element** Section III.2
    - **Evidence pointer** Figure 2B
    - **Issue** The criterion for identifying the wetting transition from the PMF is stated as the point where the minimum becomes "statistically indistinguishable from zero." The statistical test used is not specified.
    - **Required correction** Specify the statistical test and significance threshold used to determine when the PMF minimum is zero.
    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Generalizability of design rules
    - **Affected element** Section V.3
    - **Evidence pointer** Figure 5
    - **Issue** The design rules are derived for a specific set of model parameters. It is not clear how they would change if, for example, the homotypic interaction strengths of N1 and N2 were different.
    - **Required correction** Add a sentence discussing the expected dependence of the design rules on the bulk phase properties.
    - **Concern ID** R1-m5
    - **Severity** Minor
    - **Axis** Comparison with previous work
    - **Affected element** Section I (Introduction)
    - **Evidence pointer** References [Mao et al., Sanders et al.]
    - **Issue** The distinction between the authors' CDFT approach and the "linear path approximation" used in previous work is clear, but the practical implications of this difference could be emphasized more.
    - **Required correction** Briefly state that the linear path approximation would incorrectly predict non-wetting behavior for the conditions studied here, highlighting the importance of the full CDFT approach.
- **Technical failings that need to be addressed before the case is established**
    - R1-M2: The quantitative accuracy of the CDFT method needs to be established more rigorously.
    - R1-M3: The adsorption model's derivation and range of validity need to be clarified.
- **Assessment against Nature-style criteria**
    - **Originality** High. The concept of a low-concentration "programmable surfactant" as a morphological switch for multiphase condensates is novel and not present in the existing literature.
    - **Scientific importance** High. The question of how multiphase condensate morphology is regulated is of significant current interest in cell biology and biophysics. The proposed mechanism offers a new paradigm that could explain how cells control the assembly of complex structures without major changes to bulk composition.
    - **Interdisciplinary readership** Moderate to High. The topic is relevant to biophysics, cell biology, and soft matter physics. The methods (lattice simulations, CDFT) are standard in physics and chemistry, but the biological framing will attract a broader audience. The paper is likely to be accessible to researchers in adjacent fields.
    - **Technical soundness** Good. The simulation methodology is appropriate, and the CDFT approach is a reasonable approximation, though its limitations are acknowledged. The analytical model provides a useful conceptual framework. The main technical weakness is the lack of quantitative error analysis for the CDFT method.
    - **Readability for nonspecialists** Good. The introduction and discussion are clearly written and accessible. The main text avoids excessive technical detail, with the appendices providing the necessary depth. The figures, based on captions, appear to be well-designed to convey the key results.
- **Recommendation posture** Supportive if technical concerns are resolved. The core claim is plausible and well-supported by the model evidence. The main issues are the need for a more rigorous quantitative assessment of the CDFT method's accuracy and a clearer articulation of the model's limitations and its connection to real biological systems. If these are addressed, the paper would be a valuable contribution.

## Risk / unsupported claims
- The claim that the model can be "applied directly" to real protein/RNA interaction networks (e.g., SG/PB) is not supported by the evidence presented, as no experimental data or detailed mapping to a real system is provided.
- The quantitative accuracy of the CDFT method for predicting the location of the wetting transition is not fully established, given the need for regularization and the noted discrepancy with simulations.
- The generality of the design rules beyond the specific parameter ranges tested is not demonstrated.