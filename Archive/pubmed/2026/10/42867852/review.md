## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no figures, methods, or supplementary material were provided
- **Shared manuscript claim summary** The authors use coarse-grained simulations with morphing particles to show that purely repulsive modulators do not alter alpha-synuclein fibrillization mechanisms, while attractive modulators toward disordered protein slow fibrillization dose-dependently via stabilization of intermediate heteroclusters, and modulators with specific attraction to the beta-rich state shorten fibrils via surface capping that inhibits elongation.
- **Visible evidence base** Abstract text only; no quantitative results, simulation parameters, or validation data are visible
- **Missing materials affecting confidence** Full manuscript, methods section, simulation details, all figures and tables, quantitative metrics, and any comparison with experimental data

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting coarse-grained simulation study that aims to link modulator properties to alpha-synuclein phase transition outcomes. The morphing particle approach is a creative simplification, and the distinction between repulsive and attractive modulator effects is a potentially useful framework. However, the abstract alone provides insufficient detail to evaluate the technical soundness of the simulations, the robustness of the conclusions, or the generalizability of the findings. The claims are plausible but not verifiable from the supplied material.
- **Who would be interested in the results, and why** Researchers in computational biophysics and protein aggregation, particularly those studying phase transitions in neurodegeneration. The work may also interest experimentalists seeking mechanistic hypotheses for how small molecules or peptides modulate fibrillization, as the predicted capping and heterocluster stabilization mechanisms could guide intervention design.
- **Major strengths** The conceptual framework is clear and potentially impactful, distinguishing modulator effects based on interaction specificity. The morphing particle representation is a novel simplification that could enable efficient exploration of parameter space. The predicted mechanisms, including dose-dependent slowing and surface capping, are testable and could inform experimental design.
- **Major Concerns** The abstract lacks quantitative detail on simulation methodology, including force field parameters, system sizes, timescales, and sampling approaches. The claim that repulsive modulators do not alter the final outcome is stated without supporting evidence or caveats. The link between simulation results and real biological conditions is asserted but not demonstrated. The abstract does not address potential limitations of the coarse-grained model, such as the neglect of sequence-specific effects or solvent details.
- **Minor Comments** The abstract would benefit from specifying the range of modulator concentrations tested and the timescales probed. The term "morphing particle" is introduced without explanation of how the transformation is implemented dynamically. The phrase "quantitative roadmap" overstates what appears to be a qualitative mechanistic insight from the abstract.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality is moderate to high, as the morphing particle approach and the focus on modulator-specific effects are not standard in the field. Scientific importance is potentially significant for understanding and designing modulators of protein phase transitions, but the abstract does not establish biological relevance. Interdisciplinary readership is plausible, spanning biophysics, chemistry, and neuroscience, though the abstract is written for a specialized audience. Technical soundness cannot be assessed from the abstract alone, as no methodological details or validation are provided. Readability for nonspecialists is limited by undefined terms and lack of context for the simulation approach.
- **Recommendation posture** Supportive if technical concerns are resolved, but currently not established from the provided evidence

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that "purely repulsive modulators do not alter the final outcome; that is, fibrils form following the same mechanisms independently of the modulator concentration"
- **Evidence pointer** Abstract text; location not provided
- **Concern** The abstract states that repulsive modulators have no effect on fibrillization mechanisms, but no quantitative data, such as fibril yield, kinetics, or structural metrics, are presented to support this claim. The absence of an effect is a strong negative claim that requires careful statistical analysis and demonstration of adequate sampling.
- **Why it matters** If the claim is based on insufficient simulation time or limited concentration ranges, the conclusion could be an artifact. This claim is central to the paper's message that only attractive interactions matter, and an unsupported negative result weakens the entire framework.
- **Resolution test** Provide quantitative comparison of fibril formation rates, final fibril lengths, and nucleation times across a range of repulsive modulator concentrations, with error bars and statistical tests demonstrating no significant differences.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that "attractive interactions toward the disordered protein dose-dependently slow down fibrillization by stabilizing intermediate species, including persistent disordered heteroclusters"
- **Evidence pointer** Abstract text; location not provided
- **Concern** The abstract does not specify how the dose dependence was quantified, what range of interaction strengths was tested, or how "persistent" heteroclusters were defined and measured. The mechanism of stabilization is asserted without showing free energy profiles, cluster size distributions, or kinetic traces.
- **Why it matters** Dose-dependent effects are a key predictive claim that could guide experimental design. Without quantitative details on the simulation parameters and analysis, the claim cannot be evaluated or reproduced.
- **Resolution test** Present dose-response curves for fibrillization half-times or lag times as a function of modulator concentration, along with cluster size distributions and residence times for heteroclusters, demonstrating a monotonic relationship.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that "specific attraction to the beta-rich state shortens fibrils through direct modulator surface capping that introduces kinetic barriers to monomer templating at the fibril ends and inhibits fibril elongation"
- **Evidence pointer** Abstract text; location not provided
- **Concern** The capping mechanism is described qualitatively, but no evidence is provided for the kinetic barrier, such as free energy profiles for monomer addition at capped versus uncapped fibril ends, or direct observation of modulator binding at fibril ends in the simulations.
- **Why it matters** The capping mechanism is a novel and potentially important prediction, but it requires direct simulation evidence to distinguish it from alternative explanations, such as altered bulk solution properties or nonspecific binding.
- **Resolution test** Show representative simulation snapshots or density maps of modulator localization at fibril ends, and compute free energy barriers for monomer addition with and without capping modulators, demonstrating a significant increase in barrier height.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract text; location not provided
- **Issue** The term "morphing particle" is used without explanation of how the transformation from soft sphere to hard spherocylinder is implemented, which may confuse readers unfamiliar with the method.
- **Required correction** Define the morphing particle concept in the abstract or provide a brief description of the transformation dynamics.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Parameter range
- **Evidence pointer** Abstract text; location not provided
- **Issue** The abstract does not state the range of modulator concentrations or interaction strengths tested, making it difficult to assess the generality of the conclusions.
- **Required correction** Include the parameter ranges in the abstract or refer to a figure that summarizes the phase diagram.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Overstatement
- **Affected element** Conclusion
- **Evidence pointer** Abstract text; location not provided
- **Issue** The phrase "providing a quantitative roadmap for designing interventions" implies a level of predictive power that is not demonstrated in the abstract, which presents qualitative mechanisms.
- **Required correction** Soften the claim to indicate that the results provide a mechanistic framework that could inform future design efforts.

## Risk / unsupported claims
- The claim that repulsive modulators have no effect on fibrillization outcomes is unsupported by quantitative evidence in the abstract.
- The dose-dependent slowing of fibrillization by attractive modulators is asserted without showing dose-response data.
- The capping mechanism for fibril shortening is proposed without direct simulation evidence of modulator binding at fibril ends.
- The generalizability of the results to real alpha-synuclein systems, including sequence-specific effects and solvent conditions, is not established.
- The "quantitative roadmap" claim overstates the current evidence, which appears qualitative in nature.