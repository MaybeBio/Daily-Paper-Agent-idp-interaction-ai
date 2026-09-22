## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full text, figures, or supplementary materials
- **Shared manuscript claim summary** The authors propose a minimal model of biomolecular condensate self-assembly with programmable pairwise interactions among hundreds of species. They claim that the number of distinct condensates that can be reliably assembled grows superlinearly with the number of species when condensates share components, and that the maximum number of distinct condensates can be predicted without detailed knowledge of pairwise interactions. Simulations of condensate growth are stated to confirm these predictions.
- **Visible evidence base** Abstract text only; no figures, tables, equations, or simulation details provided
- **Missing materials affecting confidence** Full manuscript, simulation methodology, model equations, parameter choices, quantitative results, and any comparison with experimental data are not available. The abstract provides no numerical values, error estimates, or statistical analyses.

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting theoretical framework for understanding the combinatorial complexity of biomolecular condensate assembly. The central claim of superlinear scaling of condensate number with species number, under the condition of shared components, is potentially significant for the field of intracellular organization. However, the abstract alone provides insufficient detail to evaluate the rigor of the model, the validity of the scaling argument, or the robustness of the simulation results. The claim that the maximum number of condensates can be predicted without interaction details is intriguing but not substantiated in the provided material. The work appears to target a physics-oriented readership familiar with statistical mechanics and phase separation, and the abstract is written in a style consistent with Physical Review Letters. The scientific importance is plausible but not fully established from the abstract alone.
- **Who would be interested in the results, and why** Researchers in biophysics, soft matter physics, and cell biology studying phase separation and membraneless organelles would be interested. The theoretical framework could inform experimental design for synthetic condensate systems and provide a predictive basis for understanding cellular organization. The scaling result may also appeal to those interested in the physical limits of biological complexity.
- **Major strengths** The abstract identifies a clear and potentially generalizable principle, namely that shared components enable superlinear growth in the number of distinct condensates. The claim of predictability without detailed interaction knowledge is bold and, if correct, would be a valuable simplification. The use of a minimal programmable model is appropriate for isolating fundamental physical mechanisms.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide any quantitative evidence, such as scaling exponents, simulation parameters, or error bars. The model definition is not described, and the conditions under which the superlinear scaling holds are not specified. The claim of predictability without interaction details requires a clear statement of what information is assumed and what is predicted. Without these, the core claims cannot be assessed.
- **Assessment against Nature-style criteria** Originality: The idea of shared components enabling superlinear condensate diversity appears novel, though prior work on multicomponent phase separation exists. Scientific importance: Potentially high for understanding cellular organization, but the abstract does not demonstrate biological relevance beyond a generic statement. Interdisciplinary readership: The abstract is accessible to physicists but may be less so to biologists without additional context. Technical soundness: Cannot be evaluated from the abstract alone. Readability for nonspecialists: The abstract is concise but uses jargon such as "program the pairwise interactions" and "superlinearly" that may require background knowledge.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a promising idea, but the lack of quantitative detail and model specification prevents a supportive recommendation. A full manuscript with simulation details and robustness checks would be required to assess the claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "the number of distinct condensates that can be reliably assembled grows superlinearly with the number of species in the mixture when the condensates share components."
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract provides no definition of the model, the nature of the pairwise interactions, or the criterion for "reliably assembled." The superlinear scaling is stated without any supporting quantitative data, such as the scaling exponent, the range of species numbers tested, or the dependence on interaction strength or noise.
- **Why it matters** Without a clear model definition and quantitative results, the claim of superlinear scaling cannot be verified or reproduced. The term "reliably" is ambiguous and could refer to thermodynamic stability, kinetic accessibility, or something else, which fundamentally changes the interpretation.
- **Resolution test** The full manuscript must provide a precise model description, including the interaction matrix structure, the assembly criterion, and simulation results showing the scaling relationship with error bars or confidence intervals. The scaling should be demonstrated across a range of system sizes and parameter values.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The authors claim that "we can predict the maximum number of distinct condensates in a mixture without knowing the details of the pairwise interactions."
- **Evidence pointer** Abstract, location not provided
- **Concern** This is a strong claim of universality, but the abstract does not specify what information is required for the prediction, what the prediction is based on, or how accurate it is. The phrase "without knowing the details" could mean that only coarse-grained properties matter, but no such properties are identified.
- **Why it matters** If true, this would be a powerful result with broad applicability. However, the abstract does not provide any indication of the predictive error or the conditions under which the prediction holds. Overclaiming without evidence could mislead experimentalists who might rely on this prediction.
- **Resolution test** The manuscript must state the input information required for the prediction, provide a formula or algorithm, and demonstrate its accuracy against simulation results across diverse interaction matrices. The limits of the prediction, such as when it fails, should be explicitly discussed.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "Simulations of condensate growth confirm these predictions."
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract does not describe the simulation method, the growth dynamics, or the comparison metric between simulations and predictions. Without this information, the confirmation is unverifiable. It is also unclear whether the simulations are equilibrium or non-equilibrium, which is relevant given the abstract's mention of systems "which may not be at thermodynamic equilibrium."
- **Why it matters** The confirmation of predictions by simulations is central to the paper's credibility. If the simulation methodology is flawed or the comparison is qualitative, the claims may not be robust. The non-equilibrium aspect is mentioned but not addressed in the claims, creating a potential inconsistency.
- **Resolution test** The manuscript must describe the simulation algorithm, the initial conditions, the time scales, and the criteria for condensate identification. The comparison between predicted and simulated condensate numbers should be quantitative, with statistical measures of agreement.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Abstract wording
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "program the pairwise interactions" is informal and may be unclear to readers outside the immediate field. The term "superlinearly" is used without a brief explanation of its significance.
- **Required correction** Consider rephrasing to "specify the pairwise interaction strengths" and adding a parenthetical note such as "growing faster than linearly" for clarity.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Biological relevance
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract claims the rules are "broadly applicable to biomolecular mixtures" but provides no connection to specific biological systems or experimental observations. The relevance to living cells is asserted but not demonstrated.
- **Required correction** Add a sentence in the abstract or introduction that links the model predictions to a concrete biological example or experimental observation, even if qualitative.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Model assumptions
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract mentions that the system "may not be at thermodynamic equilibrium" but does not explain how the model accounts for non-equilibrium effects. This creates ambiguity about the validity of the predictions.
- **Required correction** Clarify in the abstract or main text whether the model is equilibrium or non-equilibrium, and if non-equilibrium, specify the driving forces or kinetic constraints.

## Risk / unsupported claims
- The claim of superlinear scaling of condensate number with species number is unsupported in the abstract due to lack of quantitative data.
- The claim of predicting the maximum number of condensates without interaction details is unsupported without specification of the prediction method and its accuracy.
- The statement that simulations confirm predictions is unverifiable without simulation details.
- The assertion that the rules are "broadly applicable to biomolecular mixtures" is unsupported without experimental or comparative evidence.