## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as stated in the abstract, without access to full methods, derivations, or simulation details
- **Shared manuscript claim summary** The authors propose a minimal discrete-state stochastic model of transcription that incorporates reversible mRNA condensation. They claim that this condensation maintains constant free mRNA levels in the nucleoplasm, reduces stochastic noise, and increases robustness against external perturbations, supported by analytical calculations and computer simulations.
- **Visible evidence base** Abstract text only; no figures, equations, simulation parameters, or derivations provided
- **Missing materials affecting confidence** Full manuscript, model equations, parameter values, simulation protocols, validation against experimental data, and any comparison with prior models

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting theoretical contribution to understanding transcriptional noise regulation via mRNA condensates. The core idea, that reversible condensation buffers free mRNA levels and reduces noise, is plausible and could be of value to the biophysics and gene expression communities. However, the abstract provides insufficient detail to assess the technical soundness of the model, the validity of the analytical results, or the robustness of the conclusions. The claim of "maintaining a constant level of free mRNA" is strong and requires careful scrutiny, as it may depend critically on model assumptions not stated here. The work appears to be at an early stage of validation, with no reference to experimental data or quantitative predictions that could be tested. Overall, the concept is interesting, but the evidence base is too thin to establish the case.
- **Who would be interested in the results, and why** Researchers in biophysics, stochastic gene expression, and transcriptional regulation would be interested. The model offers a theoretical framework for understanding how biomolecular condensates, a topic of intense current interest, might modulate transcriptional noise. This could appeal to both theorists seeking new modeling approaches and experimentalists studying condensate function in the nucleus.
- **Major strengths** The topic is timely and relevant, given the growing interest in biomolecular condensates. The use of a minimal discrete-state stochastic model is appropriate for capturing noise dynamics. The abstract clearly states the main findings and provides a physicochemical rationale, which helps frame the work for a broad audience.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide any quantitative details, such as model equations, parameter ranges, or simulation outcomes. Without these, the analytical claims cannot be verified. The claim of constant free mRNA level is particularly strong and may be an artifact of model assumptions, such as infinite reservoir or specific rate balances, which are not described. No comparison with existing models of transcriptional noise or experimental data is mentioned, so the novelty and relevance are not fully established.
- **Assessment against Nature-style criteria** 
  - Originality: The idea of linking mRNA condensation to noise regulation appears novel, but the abstract does not clarify how it differs from prior models of transcriptional bursting or noise buffering. 
  - Scientific importance: If validated, the work could have broad implications for understanding condensate function, but the current abstract does not demonstrate this. 
  - Interdisciplinary readership: The topic bridges biophysics and molecular biology, which is attractive, but the abstract is too technical for nonspecialists without context. 
  - Technical soundness: Not assessable from the abstract; no equations or simulation details are provided. 
  - Readability for nonspecialists: The abstract is clear in its language but assumes familiarity with stochastic modeling and condensate biology, which may limit accessibility.
- **Recommendation posture** Currently not established from the provided evidence. The idea is promising, but the abstract alone does not provide sufficient technical detail to support the claims. I would be supportive if the full manuscript provides rigorous derivations, parameter sensitivity analysis, and testable predictions.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Analytical calculations supported by computer simulations suggest that reversible mRNA condensation influences the transcription processes by maintaining a constant level of free mRNA in the nucleoplasm"
- **Evidence pointer** Abstract, location not provided
- **Concern** The claim of maintaining a constant level of free mRNA is a strong, quantitative assertion. The abstract does not specify the conditions under which this constancy holds, such as the range of transcription rates, condensate sizes, or mRNA degradation rates. It is unclear whether this is a general property of the model or a special case arising from specific parameter choices or simplifying assumptions, such as rapid equilibration or infinite condensate capacity.
- **Why it matters** If the constancy is not robust across biologically relevant parameter regimes, the central conclusion of the paper would be misleading. A model that only works under narrow conditions would have limited applicability to real cellular systems, where transcription rates and condensate properties vary widely.
- **Resolution test** The full manuscript should provide a phase diagram or parameter sensitivity analysis showing the range of conditions under which free mRNA levels remain constant. Additionally, the authors should state the explicit model assumptions that lead to this behavior and discuss whether these assumptions are biologically justified.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "reversible mRNA condensation influences the transcription processes by maintaining a constant level of free mRNA in the nucleoplasm while lowering the degree of stochastic noise and increasing the robustness against external perturbations"
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract claims that condensation reduces stochastic noise and increases robustness, but no quantitative measures are provided. For example, what is the magnitude of noise reduction, and how is robustness defined and quantified? Without specific metrics, such as the Fano factor or coefficient of variation, and without comparison to a control model without condensation, the claim is not testable.
- **Why it matters** The scientific value of the work depends on demonstrating a significant and meaningful effect. Vague qualitative statements are insufficient for a quantitative modeling paper. Readers need to know the effect size to judge whether condensation is a biologically relevant regulatory mechanism.
- **Resolution test** The authors should report specific noise metrics, such as the Fano factor or coefficient of variation, for models with and without condensation, and show that the differences are statistically or practically significant. Robustness should be defined operationally, for example, as the variance in mRNA levels in response to parameter perturbations, and quantified.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** "Analytical calculations supported by computer simulations"
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract mentions analytical calculations and computer simulations but provides no details on the model formulation, simulation algorithm, or parameter values. This makes it impossible to reproduce the results or assess their validity. For a theoretical paper, reproducibility is essential, and the abstract should at least hint at the model structure, such as the number of states, the rates involved, and the simulation approach.
- **Why it matters** Without reproducibility, the claims cannot be independently verified, which undermines the credibility of the work. Reviewers and readers need to understand the model to evaluate its assumptions and limitations.
- **Resolution test** The full manuscript should include a complete model description, including master equations or reaction schemes, parameter values, and simulation details. The abstract should be revised to include a brief summary of the model structure, such as "a three-state model with rates for transcription, condensation, and degradation."

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract wording
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "maintaining a constant level of free mRNA" is ambiguous. It could mean a steady-state level that is constant over time, or it could mean a level that is insensitive to changes in transcription rates. These are different concepts.
- **Required correction** Clarify whether "constant" refers to temporal stability or parameter insensitivity, and use more precise language, such as "homeostatic regulation" or "buffering against parameter fluctuations."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Contextualization
- **Affected element** Abstract background
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract does not mention any prior models of transcriptional noise or condensate function, so it is unclear what is new about this work.
- **Required correction** Add a sentence in the abstract or introduction that explicitly states how this model differs from existing approaches, such as "unlike previous models that treat condensates as passive sinks, our model incorporates reversible exchange dynamics."

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract conclusion
- **Evidence pointer** Abstract, location not provided
- **Issue** The final sentence, "providing a convenient quantitative tool for investigating complex biological phenomena," is vague and does not specify what new insights the tool enables.
- **Required correction** Replace with a more specific statement, such as "this framework enables predictions of how condensate properties, such as size or binding affinity, affect transcriptional noise, which can be tested experimentally."

## Risk / unsupported claims
- The claim that mRNA condensation maintains constant free mRNA levels is unsupported without model details and parameter analysis.
- The claim that condensation lowers stochastic noise and increases robustness is unsupported without quantitative metrics and comparison to a control model.
- The claim that the model is a "convenient quantitative tool" is not substantiated, as no examples of its application or predictive power are provided.
- The overall relevance to experimental systems is not established, as no connection to empirical data or testable predictions is made in the abstract.