## Review setup

- **Input scope** Full manuscript text including main text, references, and supplementary information
- **Assessment boundary** Scientific content, methodological soundness, logical coherence, and support of claims by presented evidence
- **Shared manuscript claim summary** The authors propose that co-condensation of BRD4 with chromatin below bulk saturation concentration, combined with multivalent binding to acetylated histone tails, enables condensate assembly that is both sensitive to acetylation density and robust to BRD4 concentration fluctuations. They support this with an ultra-coarse-grained molecular dynamics model.
- **Visible evidence base** Main text Sections I–III, Figures 1–7 (referenced), Supplementary Information Sections S1–S5, Supplementary Figures S1–S11 (referenced)
- **Missing materials affecting confidence** Actual figure images and numerical data values are not provided in the text; only figure captions and in-text descriptions are available. Simulation parameter tables (Table S1) are referenced but not fully reproduced. Specific quantitative results (e.g., exact threshold values, rate measurements) are described qualitatively in the text.

## Reviewer

- **Overall assessment** The manuscript presents a conceptually interesting and potentially important mechanism for how chromatin-associated condensates achieve spatial selectivity and concentration robustness. The combination of co-condensation below saturation with multivalency-driven sharpening of acetylation response is a plausible and novel physical picture. However, the evidence as presented is entirely from a coarse-grained simulation model, and the text does not provide sufficient quantitative detail to fully evaluate the robustness of the conclusions. The connection to experimental observables is discussed but not demonstrated. The manuscript would benefit from clearer presentation of quantitative results and a more explicit discussion of model limitations.

- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, chromatin biology, and transcriptional regulation would be interested. The work addresses a fundamental question about how condensates achieve specificity in a complex cellular environment, which is of broad relevance. The proposed mechanism could inform experimental design for studying BRD4 and similar chromatin-associated proteins.

- **Major strengths**
  1. The manuscript addresses a significant and timely question about the physical principles governing condensate localization and specificity.
  2. The proposed mechanism (co-condensation below saturation + multivalency) is conceptually novel and provides a coherent framework that reconciles sensitivity and robustness.
  3. The model includes relevant biological features (multivalency, chromatin deformability, acetylation density) and is calibrated to experimental data where possible.
  4. The distinction between classical nucleation and co-condensation regimes is clearly articulated and systematically explored.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that co-condensation enables "rapid assembly below the bulk coexistence concentration" and that this mechanism "suppresses off-chromatin condensation and enhances spatial selectivity."
- **Evidence pointer** Section II.5, Figures 5 and 6
- **Concern** The kinetic results are described qualitatively in the text, but no quantitative rate values, error bars, or statistical measures are provided. The claim that assembly is "diffusion-limited" and "approximately constant" when normalized relies on visual inspection of figures that are not shown in the text. Without access to the actual data, it is impossible to assess the strength of the evidence for this central claim.
- **Why it matters** The kinetic argument is central to the paper's thesis that co-condensation provides both sensitivity and robustness. If the rate plateau is not clearly demonstrated with quantitative data, the claim that assembly is robust to concentration fluctuations is not established.
- **Resolution test** Provide quantitative rate measurements (e.g., mean and standard error) for at least three saturation values in the co-condensation regime, and demonstrate statistically that the normalized rates are not significantly different across these conditions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Model validation
- **Claim pointer** The authors state that the model is calibrated using "corelet phase-separation experiments" and that binding strengths are "derived from experimental dissociation constants."
- **Evidence pointer** Section S1.2, Section S1.3, Figure S1
- **Concern** The calibration procedure is described, but the sensitivity of the results to the calibration choices is not systematically explored. Specifically, the multiplicative factor of 2.15 for binding strength and the choice of interaction range R_bind are critical parameters. It is unclear whether the qualitative conclusions (co-condensation regime, threshold behavior) are robust to reasonable variations in these parameters.
- **Why it matters** If the predicted behavior is highly sensitive to parameter choices, the biological relevance of the findings is questionable. The authors should demonstrate that the mechanism is not an artifact of specific parameter values.
- **Resolution test** Perform and report a sensitivity analysis varying the binding strength scaling factor (e.g., 1.5–3.0) and interaction range (e.g., ±20%) and show that the qualitative phase behavior and threshold characteristics are preserved.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Biological relevance
- **Claim pointer** The authors conclude that "co-condensation and multivalency jointly enable sensitive yet robust spatiotemporal targeting by chromatin-associated condensates" and suggest this mechanism is relevant to BRD4 function.
- **Evidence pointer** Section III, Section II.6
- **Concern** The model uses a single chromatin fiber with a defined acetylated segment. Real chromatin is organized into complex 3D structures with multiple acetylated regions, variable nucleosome density, and dynamic modifications. The authors do not discuss how their conclusions might be affected by these complexities, nor do they provide testable experimental predictions that could distinguish their mechanism from alternative explanations.
- **Why it matters** For the work to have impact beyond the simulation community, it should provide clear, experimentally testable predictions and discuss the limitations of the simplified model in relating to biological reality.
- **Resolution test** Add a section discussing model limitations and provide at least two specific, quantitative experimental predictions (e.g., expected dependence of condensate size or formation rate on acetylation density or BRD4 concentration) that could be tested in vitro or in cells.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section II.2, Figure 2
- **Evidence pointer** Figure 2 description
- **Issue** The description of chromatin partitioning in the bulk coexistence regime is somewhat confusing. The text states that at intermediate acetylation, chromatin localizes near the interface, but the physical reasoning for this is not fully explained.
- **Required correction** Clarify the physical mechanism for interfacial localization, perhaps with a brief explanation of the competing energetic contributions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section S1.3, binding strength derivation
- **Evidence pointer** Section S1.3
- **Issue** The grouping of the four experimental dissociation constants into two effective interaction strengths is described, but the specific values used and the rationale for the grouping are not fully detailed.
- **Required correction** Provide the specific numerical values for the two effective binding strengths and a brief justification for the grouping.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Section II.6, Equation 1
- **Evidence pointer** Section II.6
- **Issue** The key inequality for preferential targeting is presented as an equation, but the terms are not fully defined in the main text.
- **Required correction** Define all terms in the equation explicitly in the main text, even if they are defined in the SI.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section S4.2, rate measurements
- **Evidence pointer** Section S4.2
- **Issue** The text mentions that "in regimes where assembly formation is not observed within the simulation time window, we report upper bounds," but it is unclear how many data points are upper bounds versus actual measurements.
- **Required correction** Clearly indicate in the main text or figure captions which data points are upper bounds and how many independent simulations were performed for each condition.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Section II.2, "co-condensation"
- **Evidence pointer** Section II.2
- **Issue** The term "co-condensation" is used to describe a specific regime, but it is not clearly distinguished from other related phenomena such as "heterogeneous nucleation" or "surface adsorption" in the context of this model.
- **Required correction** Provide a clear operational definition of co-condensation as used in this work, distinguishing it from related concepts.

## Risk / unsupported claims

1. The claim that co-condensation enables "rapid assembly" below saturation is not quantitatively supported in the text; no rate values are provided.
2. The claim that the mechanism is "robust to BRD4 concentration fluctuations" is based on qualitative descriptions of rate plateaus; statistical evidence is not presented.
3. The statement that the model is "calibrated" to experimental data is only partially supported; the sensitivity of conclusions to calibration choices is not assessed.
4. The biological relevance of the findings to BRD4 function in cells is asserted but not demonstrated; no experimental validation or specific testable predictions are provided.
5. The claim that multivalency "sharpens" acetylation dependence is supported by comparison between WT and mBD2, but the quantitative degree of sharpening is not reported.
6. The hysteresis region described in Section S2.4 is mentioned but its extent and implications for the biological regime are not quantified in the main text.