## Review setup
- **Input scope** Full manuscript text including abstract, introduction, simulation model, results, discussion, conclusions, and data availability statement.
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by presented evidence. No assessment of formatting, grammar, or journal fit beyond Nature-style criteria.
- **Shared manuscript claim summary** The authors use coarse-grained bead-spring polymer simulations of the budding yeast genome to show that transient chromatin cross-links within the nucleolus regulate its viscoelastic properties. They report that cross-link density and lifetime tune nucleolar condensation, stress relaxation, and Rouse-mode dynamics, with an optimal intermediate cross-link density producing the strongest mechanical response.
- **Visible evidence base** Simulation model description (LAMMPS, Langevin dynamics, FENE and LJ potentials), Tables I–IV (chain assignments, tethering positions, kinetic parameters), Figures 2–7 (conformations, stress relaxation moduli, radial distribution functions, Rouse-mode analyses), and references to prior experimental work.
- **Missing materials affecting confidence** Figure files are not provided, so quantitative values plotted in Figs. 2–7 cannot be independently verified. Supplemental Material (Ref. [57]) is not available. No experimental validation data are included. Simulation parameter values for τB, PB, τU, PU are only summarized in Table III, but the table content is not visible in the provided text.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question in nuclear mechanics, namely how transient protein-DNA cross-links modulate nucleolar rheology. The computational framework is clearly described and builds on prior work by the same group. The central finding of a nonmonotonic relationship between cross-link density and viscoelastic response is interesting and potentially significant. However, the evidence as presented is insufficient to fully establish this claim. Key quantitative results are only shown in figures that are not available for inspection, and the manuscript lacks a systematic error analysis or comparison with alternative models. The selective assignment of cross-links to nucleolar beads is acknowledged as a working hypothesis, but its consequences are not critically examined. The connection to experimental observables is plausible but not quantitatively grounded. Overall, the work is promising but requires additional evidence and analysis before the case is fully established.
- **Who would be interested in the results, and why** Researchers in biophysics, soft matter physics, and chromatin biology would be interested. The work connects polymer physics concepts (transient cross-linking, Rouse dynamics, viscoelasticity) to a specific biological organelle, offering a mechanistic framework that could inform experimental studies of nucleolar mechanics and phase separation. The findings may also interest those studying nuclear organization in disease contexts, as the authors suggest links to cancer and neurodegeneration.
- **Major strengths** The manuscript addresses a well-defined gap in understanding nucleolar rheology. The computational model is described in sufficient detail to be reproducible. The systematic exploration of nine kinetic scenarios is a reasonable approach. The distinction between nucleolar and nonnucleolar behavior provides a clear comparative framework. The authors appropriately acknowledge limitations, such as the lack of direct evidence for preferential SMC binding to the nucleolus.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (missing quantitative evidence), R1-M2 (lack of error analysis), R1-M3 (unexamined model assumption), R1-M4 (insufficient connection to experiments).
- **Assessment against Nature-style criteria** Originality: The work is original in applying transient cross-linking kinetics to nucleolar rheology, though it builds on established polymer physics frameworks. Scientific importance: Potentially high, as it offers a mechanistic explanation for nucleolar mechanical behavior, but the significance is not fully demonstrated without quantitative validation. Interdisciplinary readership: The topic bridges physics and biology, but the presentation is heavily simulation-focused and may not be accessible to a broad biological audience. Technical soundness: The simulation methodology is standard and appropriate, but the lack of error analysis and sensitivity studies weakens the technical case. Readability for nonspecialists: The introduction and conclusions are accessible, but the results section assumes familiarity with polymer rheology and Rouse models, which may limit broader readership.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is sound and the preliminary results are suggestive, but the manuscript as provided does not contain enough quantitative evidence to fully establish the claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "modulations in protein-DNA interactions critically dictate the phase behavior, relaxation dynamics, and viscoelastic properties of the nucleolus" and that "protein-mediated bridging emerges as a critical factor enhancing nucleolar condensation and modulating stress relaxation."
- **Evidence pointer** Figures 2–7, Tables III–IV; figure files not provided
- **Concern** The central quantitative results are presented only in figures that are not available for inspection. The manuscript text describes trends (e.g., nonmonotonic stress relaxation, changes in radial distribution functions, Rouse-mode deviations) but does not provide numerical values, error bars, or statistical measures. Without access to the actual data, it is impossible to assess the magnitude of the reported effects, the significance of differences between kinetic scenarios, or the robustness of the nonmonotonic relationship.
- **Why it matters** The core claim of a nonmonotonic relationship between cross-link density and viscoelastic response is the main contribution of the work. If the effect sizes are small or the differences between scenarios are within noise, the conclusion would not be supported. The manuscript cannot be evaluated on its merits without the underlying quantitative data.
- **Resolution test** Provide the figure data in a form that allows quantitative assessment, such as tabulated values, error bars, or statistical comparisons. Alternatively, include the figures in the manuscript submission so that the trends can be visually verified.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors report stress relaxation moduli and Rouse-mode parameters for different cross-link densities and lifetimes, implying that differences between scenarios are meaningful.
- **Evidence pointer** Section "RESULTS AND DISCUSSION", Figures 3, 6, 7; location not provided for error analysis
- **Concern** No error analysis or uncertainty quantification is presented. The manuscript does not report standard deviations, confidence intervals, or the number of independent simulation runs. It is unclear whether the observed differences between kinetic scenarios are statistically significant or could arise from stochastic fluctuations in a single trajectory.
- **Why it matters** Without error estimates, the reader cannot distinguish genuine physical effects from simulation noise. This is particularly important for the claimed nonmonotonic behavior, which requires comparing multiple scenarios with potentially similar magnitudes.
- **Resolution test** Perform multiple independent simulation runs for each kinetic scenario and report mean values with standard deviations or standard errors. Provide statistical tests (e.g., t-tests or ANOVA) for key comparisons.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Model validity
- **Claim pointer** The authors state that "nucleolar beads are selectively assigned dynamic, transient cross-linking interactions, reflecting a modeling assumption motivated by prior studies suggesting SMC protein enrichment at the rDNA locus."
- **Evidence pointer** Section "SIMULATION MODEL AND COMPUTATIONAL DETAILS", paragraph on transient bond formation
- **Concern** The selective assignment of cross-links to nucleolar beads is a strong assumption that is acknowledged but not critically examined. The authors do not test whether this selectivity is necessary for the observed effects, nor do they compare with a model where cross-links are distributed uniformly across all chromatin. The choice of which proteins mediate the cross-links (SMC complexes, Hmo1) is also not varied.
- **Why it matters** If the observed rheological effects arise from any transient cross-linking, regardless of location, then the biological interpretation in terms of nucleolar-specific regulation would be weakened. The manuscript would be strengthened by a control simulation with uniform cross-linking or with cross-links on a different chromosome region.
- **Resolution test** Add a control simulation where cross-links are applied to nonnucleolar chromatin or uniformly across all chromosomes, and show that the nucleolar-specific effects are not reproduced.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Experimental relevance
- **Claim pointer** The authors state that "these insights not only deepen our understanding of nucleolar function but also open avenues for interventions in genetic engineering and disease therapeutics."
- **Evidence pointer** Abstract, Conclusions; no experimental data in manuscript
- **Concern** The manuscript does not provide any quantitative comparison with experimental measurements of nucleolar mechanics. While the authors cite experimental studies (e.g., Feric et al., Brangwynne et al.) as supporting plausibility, they do not attempt to map their simulation parameters to experimental conditions or predict specific measurable quantities that could be tested. The claim of relevance to disease therapeutics is speculative and not supported by the presented evidence.
- **Why it matters** For a computational study to have broad impact, it should either make testable predictions or provide quantitative agreement with existing experiments. Without such a connection, the biological significance remains suggestive rather than demonstrated.
- **Resolution test** Identify specific experimental observables (e.g., viscosity, elastic modulus, relaxation timescales) that could be measured in yeast or other systems, and provide quantitative predictions from the model. Alternatively, compare simulation results with existing experimental data on nucleolar mechanics.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section "SIMULATION MODEL AND COMPUTATIONAL DETAILS", paragraph on transient bond formation
- **Evidence pointer** Text describing τB, PB, τU, PU
- **Issue** The relationship between the kinetic parameters (τB, PB, τU, PU) and the resulting cross-link density cXlink and lifetime τlife is described qualitatively but not derived or shown explicitly. The manuscript states that cXlink is "jointly determined by both the binding and unbinding kinetics" but does not provide a formula or a plot showing this relationship.
- **Required correction** Provide a clear definition of how cXlink and τlife are computed from the input parameters, and consider showing a table or figure that maps the nine kinetic scenarios to the resulting cXlink and τlife values.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section "SIMULATION MODEL AND COMPUTATIONAL DETAILS", paragraph on simulation setup
- **Evidence pointer** Text describing initial conditions and equilibration
- **Issue** The manuscript states that initial configurations are based on pre-equilibrated structures from Refs. [3,4], but does not describe how these structures were obtained or whether they are publicly available. The equilibration time (1.5×10^6 τ0) and production time (2.1×10^6 τ0) are stated, but it is unclear whether these are sufficient for the system to reach steady state.
- **Required correction** Provide more detail on the initial configuration generation and justify the equilibration time. Consider showing that key observables (e.g., radius of gyration, cross-link density) have converged over the production run.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Section "RESULTS AND DISCUSSION", paragraph on stress relaxation
- **Evidence pointer** Text describing Fig. 3(a)
- **Issue** The authors attribute the lack of stress relaxation in nonnucleolar chromatin to tethering and chain tangles. This interpretation is plausible but not directly tested. For example, a simulation without tethering could confirm that tethering is the cause.
- **Required correction** Consider adding a control simulation without tethering to support the interpretation, or soften the claim by presenting it as a hypothesis.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Section "RESULTS AND DISCUSSION", paragraph on Rouse-mode analysis
- **Evidence pointer** Text describing Fig. 7
- **Issue** The description of the Rouse-mode results is somewhat terse. The manuscript states that "higher cross-link densities cause βp to deviate further from the reference values" and that "in some cases, the correlation appears to be reversed," but does not explain why this reversal occurs or what it implies physically.
- **Required correction** Expand the discussion of the Rouse-mode results, providing a physical interpretation of the observed trends and the reversal.

## Risk / unsupported claims
- The claim that "modulations in protein-DNA interactions critically dictate the phase behavior, relaxation dynamics, and viscoelastic properties of the nucleolus" is not fully supported because the quantitative data are not available for inspection.
- The claim that "protein-mediated bridging emerges as a critical factor enhancing nucleolar condensation and modulating stress relaxation" is suggestive but not quantitatively verified.
- The claim that the findings "open avenues for interventions in genetic engineering and disease therapeutics" is speculative and not supported by the presented evidence.
- The statement that "the nucleolus, located in the middle of the 24th arm, has relatively free ends, allowing its conformation to relax completely" is an interpretation that is not directly tested.
- The relevance of the simulation parameters to experimental conditions is not established, so any claims about experimental correspondence are unverifiable from the provided material.