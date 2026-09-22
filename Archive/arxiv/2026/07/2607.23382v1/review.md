## Review setup

- **Input scope** Full manuscript text, including main text, methods, and supplementary information.
- **Assessment boundary** The scientific claims, methodology, and conclusions as presented in the provided manuscript. The review is based solely on the content of the provided text.
- **Shared manuscript claim summary** The manuscript argues that the ability of biomolecular condensates to buffer concentration noise depends on whether they undergo binary or ternary liquid-liquid phase separation (LLPS). Using random phase approximation (RPA) theory and coarse-grained molecular dynamics (MD) simulations of model intrinsically disordered proteins (IDPs), the authors show that ternary LLPS, in principle, offers superior noise buffering in the infinite-volume limit. However, they demonstrate that finite-size effects, including interfacial tension and thermal fluctuations, significantly alter this picture for small condensates, such as those simulated by MD, and can diminish or even reverse the advantage of ternary over binary LLPS. They propose a phase-field model augmented with interfacial terms to bridge the gap between small-scale simulations and larger, more realistic condensates.
- **Visible evidence base** The manuscript provides RPA-derived phase diagrams, MD simulation density profiles, phase-field model calculations, and MC simulation results. The evidence is presented in Figures 1-8 and Supplementary Figures S1-S14.
- **Missing materials affecting confidence** The manuscript is a preprint and does not include experimental validation. The phase-field model parameters are fitted to MD data, and the extrapolation to larger systems is based on this model. The specific simulation parameters for the MD runs (e.g., exact system composition, equilibration times) are not fully detailed in the main text and are only partially described in the SI. The link between the model IDP sequences and real biological sequences is not established.

## Reviewer

- **Overall assessment** This manuscript addresses a timely and important question in the field of biomolecular condensates: how does the size of a condensate and the multiplicity of coexisting phases affect its ability to buffer concentration fluctuations? The authors combine analytical theory (RPA) with coarse-grained simulations (MD) and a phenomenological phase-field model to provide a compelling and nuanced picture. The central finding, that finite-size effects can significantly alter the noise-buffering capacity of ternary versus binary LLPS, is novel and has important implications for interpreting both simulations and biological experiments. The work is technically sound, and the conclusions are generally well-supported by the evidence presented. The main weaknesses are the lack of experimental validation and the reliance on a fitted model for extrapolation to larger scales. Overall, this is a strong contribution that will be of interest to a broad audience in biophysics and cell biology.
- **Who would be interested in the results, and why** Researchers studying the physical chemistry of biomolecular condensates, particularly those using computational methods (MD, field-theoretic simulations). Cell biologists interested in the functional roles of condensates in cellular organization and noise regulation. The work provides a theoretical framework for understanding how the size and multiphase architecture of condensates, such as the nucleolus, might influence their biochemical function.
- **Major strengths**
    1.  The study addresses a significant and under-explored problem: the interplay between phase multiplicity and finite-size effects in condensate function.
    2.  The combination of RPA theory, MD simulations, and a phase-field model is powerful and provides a multi-scale perspective.
    3.  The finding that finite-size effects can reverse the expected superiority of ternary over binary LLPS for noise buffering is a novel and important insight.
    4.  The manuscript is generally clearly written and the figures are informative.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical Soundness
    - **Claim pointer** The claim that the phase-field model with fitted interfacial coefficients can be used to extrapolate from small MD systems to larger, more realistic condensates.
    - **Evidence pointer** Figures 3, 5, 6, and the "Phenomenlogical phase-field treatment" section in the SI.
    - **Concern** The phase-field model's interfacial coefficients are fitted to reproduce the behavior of the specific, small MD systems. The manuscript then uses this model to predict behavior at larger length scales (e.g., L > 200b). This extrapolation is a central part of the paper's conclusions, but its validity is not rigorously tested. The model's predictions for larger systems are not compared to any independent data (e.g., from larger-scale simulations or experiments). The sensitivity of the predicted threshold size (~80 nm) to the fitted parameters is not explored.
    - **Why it matters** The main biological conclusion, that ternary LLPS is a superior noise buffer only for condensates above a certain size, hinges on the accuracy of this extrapolation. If the model is not predictive outside the fitted regime, the conclusion is not established.
    - **Resolution test** The authors should perform a sensitivity analysis of the phase-field model's predictions to the fitted parameters. They could also test the model's predictions against a limited number of larger-scale MD simulations (e.g., 2000 or 4000 chains) to see if the predicted trend of reduced concentration dispersion with increasing size is observed. If such simulations are not feasible, the authors should more explicitly caveat the speculative nature of the extrapolation.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific Importance
    - **Claim pointer** The claim that the findings have direct implications for understanding noise buffering in natural biomolecular condensates, which are often much larger than the simulated systems.
    - **Evidence pointer** Discussion section, Figure 6.
    - **Concern** The model systems are simple, fully charged, 50-bead polyampholytes. Real IDPs are much more complex, with specific sequence features, varied charge patterning, and interactions with other molecules (e.g., RNA). The manuscript does not adequately discuss how these complexities might alter the predicted size-dependent noise buffering. The extrapolation from a generic model system to specific biological condensates like the nucleolus is a significant leap.
    - **Why it matters** The paper's significance for a biology audience depends on the relevance of the model systems to real biological situations. Without a discussion of the limitations of the model in capturing biological complexity, the claims of biological relevance are overstated.
    - **Resolution test** The authors should add a more detailed discussion of the potential limitations of their model systems. They could also discuss how their findings might be tested experimentally, for example, by using in vitro reconstituted systems with designed IDPs of varying lengths and charge patterns to measure noise buffering as a function of droplet size.
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability for Nonspecialists
    - **Affected element** Introduction and Significance Statement
    - **Evidence pointer** Main text, first two sections.
    - **Issue** The concept of "noise buffering" and its biological importance could be introduced more explicitly for a general reader. The distinction between "binary" and "ternary" LLPS and why the latter might be better at buffering is stated but could be explained more intuitively.
    - **Required correction** Consider adding a sentence or two in the introduction explaining what is meant by "noise" in a cellular context and why a condensate with three phases might be more robust to changes in input concentration than one with two phases.
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Results section, Figure 4.
    - **Evidence pointer** Figure 4 and the corresponding text.
    - **Issue** The statement that the MD distributions are "almost indistinguishable" from the binary LLPS case for the ternary systems is a strong qualitative claim. A quantitative measure of similarity (e.g., a distance metric between the distributions) would strengthen this point.
    - **Required correction** Provide a quantitative comparison of the MD-generated 2D density distributions, perhaps by calculating the overlap or a Kullback-Leibler divergence between the distributions for different systems and sizes.
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Materials and Methods, MC model.
    - **Evidence pointer** "MC moves" section in the SI.
    - **Issue** The description of the MC moves for the two-component system is clear, but the equilibration criterion is not stated. It is mentioned that equilibration is monitored, but the specific criterion used is not defined.
    - **Required correction** State the specific equilibration criterion used for the two-component MC simulations.
    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Readability for Nonspecialists
    - **Affected element** Results section, Figure 6.
    - **Evidence pointer** Figure 6 and the corresponding text.
    - **Issue** The definition of the two measures of noise buffering (S and sigma_phi) is clear, but the biological interpretation of the "threshold size" L ≈ 200b could be made more explicit.
    - **Required correction** In the discussion of Figure 6, explicitly state the biological implication of the threshold size: "This suggests that only condensates larger than approximately 80 nm can fully leverage the noise-buffering advantage of a three-phase architecture."
- **Technical failings that need to be addressed before the case is established**
    - The extrapolation of the phase-field model to larger sizes (R1-M1) is the most significant technical issue. The case for the main biological conclusion is not fully established without a more robust validation of this extrapolation.
- **Assessment against Nature-style criteria**
    - **Originality:** High. The focus on the interplay between phase multiplicity and finite-size effects for noise buffering is a novel angle that goes beyond previous work on binary systems.
    - **Scientific importance:** High. The findings have direct implications for understanding the function of multiphasic condensates like the nucleolus and for interpreting the results of MD simulations, which are a cornerstone of the field.
    - **Interdisciplinary readership:** High. The topic is relevant to biophysics, physical chemistry, cell biology, and synthetic biology.
    - **Technical soundness:** Good. The combination of RPA, MD, and phase-field modeling is appropriate and well-executed. The main weakness is the unvalidated extrapolation of the phase-field model.
    - **Readability for nonspecialists:** Good. The paper is well-structured, but the introduction could be slightly more accessible. The figures are clear and informative.
- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are novel and interesting, but the main biological conclusion relies on an extrapolation that needs to be more rigorously justified or at least more clearly caveated. I would be supportive of publication in a high-impact journal after the authors address the major concern regarding the predictive power of the phase-field model.

## Risk / unsupported claims
- The claim that the phase-field model can be used to predict the noise-buffering behavior of condensates much larger than the MD systems it was fitted to is not fully supported by the evidence presented.
- The claim that the findings are directly applicable to natural biomolecular condensates, given the simplicity of the model IDPs, is an extrapolation that is not fully supported.
- The statement that the MD distributions for ternary systems are "almost indistinguishable" from binary systems is a qualitative claim that is not quantitatively supported.