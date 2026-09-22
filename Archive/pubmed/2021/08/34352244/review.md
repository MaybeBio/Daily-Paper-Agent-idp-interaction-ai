## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no figures, methods, or supplementary material provided
- **Shared manuscript claim summary** The authors present a polymer-based coarse-grained model coupled to a hybrid simulation algorithm to study DNA-mediated phase separation of cGAS. They report a multi-step kinetic aggregation process, a requirement for both cGAS dimerization and protein-DNA interactions for phase separation, kinetic trapping under strong binding affinities, and a facilitative role of multivalency and intrinsic disordered regions. They claim this is the first computational model for cGAS-DNA condensate formation and that the method bridges timescales beyond atomistic MD while retaining spatial information absent in mean-field theory.
- **Visible evidence base** Abstract text only; no simulation details, parameter values, validation data, or comparison to experimental results are provided
- **Missing materials affecting confidence** Full manuscript, methods section, simulation parameters, validation against experimental data, quantitative results, and any figures or tables

## Reviewer
- **Overall assessment** The abstract describes a potentially useful computational approach to a biologically timely problem, namely cGAS-DNA phase separation. The conceptual framing is clear and the stated conclusions align with general expectations in the field. However, the abstract alone provides no quantitative evidence, no methodological detail, and no validation against experimental data. The central claims, including the multi-step kinetics and the specific molecular requirements, cannot be assessed from the supplied material. The claim of being the first computational model is plausible but unverifiable without a literature survey. The work may be of interest to the biophysics and innate immunity communities, but the case is not established from the abstract alone.
- **Who would be interested in the results, and why** Researchers studying phase separation in biological systems, particularly those focused on nucleic acid-protein condensates, will find the coarse-grained approach relevant. The innate immunity community, especially those investigating cGAS-STING signaling and cytosolic DNA sensing, may be interested in the mechanistic implications for cGAS clustering and activation. Computational biophysicists developing multiscale models for biomolecular condensation may also find the method useful as a complement to atomistic simulations and mean-field theories.
- **Major strengths** The abstract addresses a timely and important biological question with a computational approach that is positioned to fill a gap between atomistic simulations and mean-field theories. The stated inclusion of spatial arrangement of functional modules is a sensible design choice. The conclusions, if supported by the full manuscript, would be mechanistically informative and consistent with prior experimental observations.
- **Major Concerns** The abstract provides no quantitative results, no methodological specifics, and no validation. The central claims are therefore unverifiable from the supplied material. The claim of being the first computational model is not substantiated. The relationship between simulation parameters and biological reality is not addressed.
- **Minor Comments** The abstract would benefit from a clearer statement of the model's resolution and limitations. The phrase "multi-step kinetic process" is vague and could be specified. The connection to experimental evidence is mentioned but not detailed.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: The approach is positioned as novel, but this cannot be confirmed from the abstract alone. Scientific importance: The topic is significant, and the potential to bridge simulation scales is valuable, but the importance is not demonstrated with evidence. Interdisciplinary readership: The work could appeal to biophysicists, immunologists, and computational biologists, but the abstract does not make the case accessible to nonspecialists. Technical soundness: Not assessable from the abstract; no methodological detail or validation is provided. Readability for nonspecialists: The abstract is generally clear but uses jargon such as "multivalency" and "intrinsic disordered regions" without explanation.
- **Recommendation posture** Currently not established from the provided evidence. The abstract suggests a potentially interesting study, but the absence of quantitative results and methodological detail prevents any assessment of validity. A full manuscript with data and validation would be required to evaluate the claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that their coarse-grained model and hybrid simulation algorithm reveal a multi-step kinetic process of aggregation between cGAS and DNA.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract states that a multi-step kinetic process was observed, but no data, timescales, or intermediate states are described. There is no indication of how the kinetic steps were identified or distinguished from artifacts of the simulation protocol.
- **Why it matters** The central scientific claim of the work rests on this kinetic observation. Without quantitative evidence, the claim cannot be evaluated, and the reader cannot determine whether the observed process is biologically meaningful or a consequence of model assumptions.
- **Resolution test** The full manuscript must provide representative time series, identification of intermediate states, and a comparison of timescales with experimental observations or known biophysical rates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that phase separation requires both cGAS dimerization and protein-DNA interactions, and that strong binding affinities lead to kinetic trapping in small aggregates.
- **Evidence pointer** Abstract only; location not provided
- **Concern** These are strong mechanistic claims, but the abstract provides no parameter values, no phase diagrams, and no systematic variation of binding affinities or concentrations. The reader cannot assess whether the conclusions are robust to parameter choices or model details.
- **Why it matters** The claims are central to the biological interpretation. If the model is sensitive to arbitrary parameter choices, the conclusions may not be generalizable. Without evidence, the claims are unsupported.
- **Resolution test** The full manuscript must show phase diagrams or equivalent quantitative results across a range of concentrations and binding parameters, with clear definitions of phase separation and kinetic trapping criteria.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation and comparison to experiment
- **Claim pointer** The authors state that their findings are consistent with previous experimental evidence and that the model adds a useful dimension to existing techniques.
- **Evidence pointer** Abstract only; location not provided
- **Concern** No specific experimental data are cited or compared. The claim of consistency is vague and cannot be verified. The assertion that the method bridges timescales beyond atomistic MD while retaining spatial information is plausible but unquantified.
- **Why it matters** For a computational model to be credible, it must be validated against experimental observations or at least clearly benchmarked against known results. Without such validation, the biological relevance of the findings is uncertain.
- **Resolution test** The full manuscript must include direct comparisons to experimental data on cGAS-DNA condensates, such as droplet size, dynamics, or concentration thresholds, and a quantitative discussion of the model's timescale and resolution relative to atomistic simulations and mean-field theories.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and accessibility
- **Affected element** Abstract text
- **Evidence pointer** Abstract only; location not provided
- **Issue** The terms "multivalency" and "intrinsic disordered regions" are used without definition or context, which may limit accessibility for readers outside the biophysics community.
- **Required correction** Provide brief definitions or contextual explanations in the abstract, or rephrase to make the concepts accessible to a broader audience.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Specificity of claims
- **Affected element** Abstract text
- **Evidence pointer** Abstract only; location not provided
- **Issue** The phrase "multi-step kinetic process" is vague and does not convey the nature or number of steps observed.
- **Required correction** Specify the number and nature of the kinetic steps, or provide a representative example in the abstract.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Claim of being the first computational model
- **Evidence pointer** Abstract only; location not provided
- **Issue** The claim of being the first computational model for cGAS-DNA condensation is not substantiated with any literature comparison.
- **Required correction** Add a brief statement in the abstract or introduction that situates the work relative to prior computational studies, or soften the claim if a comprehensive survey is not provided.

## Risk / unsupported claims
- The claim of a multi-step kinetic process is unsupported without quantitative data.
- The claim that phase separation requires both cGAS dimerization and protein-DNA interactions is unsupported without parameter studies.
- The claim of kinetic trapping under strong binding affinities is unsupported without evidence.
- The claim that multivalency and intrinsic disordered regions facilitate assembly is unsupported without specific results.
- The claim of consistency with previous experimental evidence is unverifiable without citations or comparisons.
- The claim of being the first computational model for cGAS-DNA condensation is unverifiable from the abstract alone.
- The assertion that the method bridges timescales beyond atomistic MD while retaining spatial information is unquantified and not assessable.