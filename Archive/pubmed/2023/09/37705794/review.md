## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion) as provided by the user.
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and alignment with stated claims. No assessment of formatting, grammar, or journal fit beyond Nature-style criteria.
- **Shared manuscript claim summary** The authors propose that a minimal coarse-grained model focusing solely on electrostatic interactions can reproduce DNA-protamine condensation phase behavior under low salt conditions, and that protamine length modulates aggregation and redissolution thresholds via entropic and fluctuation effects.
- **Visible evidence base** Abstract, full introduction, full methods (model description, simulation parameters), full results and discussion (including figures referenced but not shown), conclusion, conflicts of interest, acknowledgements. Supplementary material is referenced but not provided.
- **Missing materials affecting confidence** All figures (Fig. 1-4), all supplementary sections (S1-S5), and any associated data files are not provided. This limits verification of quantitative claims, simulation convergence, and statistical analysis.

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting and computationally efficient approach to studying DNA-protamine condensation, with a clear hypothesis that electrostatic interactions dominate under low salt conditions. The authors demonstrate internal consistency between their simple model and a previously published more refined model, and they identify a plausible mechanism (charge disproportionation) for bundle formation. However, the absence of figures and supplementary data prevents full evaluation of the quantitative results, simulation quality, and statistical robustness. The claims regarding protamine-length effects are qualitatively supported by the text but require the missing data to be fully assessed. The work is likely of interest to computational biophysicists and experimentalists studying polyelectrolyte condensation, but the current evidence base is insufficient to establish all conclusions with confidence.
- **Who would be interested in the results, and why** Computational biophysicists and soft matter physicists studying polyelectrolyte condensation, coarse-grained simulation method development, and phase behavior of charged polymers. Experimentalists working on DNA packaging, gene therapy nanoparticle formulation, and biomolecular condensates (e.g., RNA-protein coacervates) may also find the mechanistic insights useful, particularly the role of condensing agent length in controlling aggregation thresholds.
- **Major strengths** 1) The hypothesis-driven approach is clear and well-motivated, with a logical progression from prior work to a simplified model. 2) The model is computationally efficient, enabling longer timescales and larger systems than more detailed models, which is a practical advantage. 3) The identification of charge disproportionation as a key mechanism is consistent with prior theoretical predictions and provides a molecular-level explanation. 4) The comparison between short and long protamine models directly addresses a biologically and technologically relevant parameter (protamine length variation across species). 5) The authors acknowledge limitations (e.g., binding distances shorter than refined models) and provide a rationale for why these do not affect qualitative conclusions.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (missing figures/data), R1-M2 (statistical robustness), R1-M3 (model validation against experiments), R1-M4 (convergence and equilibration).
- **Assessment against Nature-style criteria** Originality: Moderate. The approach of simplifying a coarse-grained model to focus on electrostatics is not entirely new, but the systematic exploration of protamine length effects and the connection to charge disproportionation provide some novelty. Scientific importance: Moderate. The findings are relevant to understanding DNA condensation mechanisms and have potential implications for gene therapy and condensate biology, but the impact is incremental rather than transformative. Interdisciplinary readership: Moderate. The topic bridges biophysics, soft matter, and molecular biology, but the technical nature of the simulation methods may limit broader appeal. Technical soundness: Not fully assessable due to missing figures and supplementary data. The methodological description is plausible, but verification of simulation quality and statistical analysis is impossible without the data. Readability for nonspecialists: Good. The introduction and discussion are accessible, with clear explanations of key concepts (e.g., charge ratio, overcharging), though some simulation details may be dense for non-experts.
- **Recommendation posture** Supportive if technical concerns are resolved. The core hypothesis and qualitative findings are promising, but the manuscript cannot be fully endorsed without access to the figures and supplementary data, and without additional evidence of statistical robustness and convergence.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The manuscript claims to reproduce DNA-protamine phase behavior across a wide range of R+/− and to identify aggregation and redissolution thresholds (e.g., RCA between 0.5 and 0.8, RCR between 8 and 12 for short protamine).
- **Evidence pointer** Figures 2-4 and Supplementary Sections S1-S5, none of which are provided.
- **Concern** The central quantitative claims, including the phase behavior, bundle size distributions, charge ratios, and threshold values, are presented in figures and supplementary material that are not available for review. Without these data, it is impossible to verify the accuracy of the reported results, the statistical significance of differences between conditions, or the convergence of the simulations.
- **Why it matters** The conclusions rest entirely on the simulation results shown in the missing figures. The reader cannot assess whether the observed behaviors are robust, reproducible, or artifacts of the model or simulation setup.
- **Resolution test** Provide all figures and supplementary sections, including error bars or standard deviations for key quantities, and ensure that the data are clearly labeled and interpretable.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical robustness
- **Claim pointer** The manuscript states that at R+/− = 0.5, "short-lived pairs" appear, and at R+/− = 2.4, "20 independent simulations" are performed to ensure sufficient sampling. However, for other R+/− values, only single simulations are mentioned.
- **Evidence pointer** Section 2.4 (Unbiased MD simulation from a homogeneous mixture) and Section 3.1 (Stage 2. DNA assembly).
- **Concern** The use of single simulations for most R+/− values raises concerns about the statistical reliability of the reported phase behavior. The text acknowledges that at R+/− = 0.5, the number of bundles varies between 16 and 20 across independent runs, indicating significant variability. It is unclear whether the qualitative differences between R+/− values are statistically meaningful or within the noise of the simulations.
- **Why it matters** The phase diagram and threshold values (RCA, RCR) are key outputs of the study. If these are based on single trajectories, they may not be representative, and the conclusions about protamine-length effects could be unreliable.
- **Resolution test** Perform multiple independent simulations (e.g., at least 5-10) for each R+/− value and report mean values with standard deviations or confidence intervals. Show that the observed trends are consistent across replicates.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Model validation
- **Claim pointer** The manuscript claims that the simple model reproduces "the phase behaviour of DNA in a wide range of protamine concentrations under low salt conditions" and that it agrees "qualitatively very well" with a previous more refined model.
- **Evidence pointer** Section 3.1 (Discrepancy from previous more-refined simulation) and Section 3.2 (Protamine-length-dependent DNA assembly).
- **Concern** While the comparison to the previous refined model is useful, the manuscript does not provide a direct quantitative comparison to experimental data under low salt conditions. The authors note that experiments at low salt were limited to a narrow R+/− range, but it is unclear whether the model predictions (e.g., threshold values, bundle sizes) match any experimental observations. The claim of reproducing "phase behaviour" is therefore only validated against another simulation, not against experiments.
- **Why it matters** The hypothesis that electrostatics dominate under low salt conditions is central to the paper. Without experimental validation, it remains uncertain whether the model captures the essential physics or misses important non-electrostatic effects.
- **Resolution test** Include a quantitative comparison to available experimental data (e.g., from references 48-51) for the R+/− range where data exist, or clearly state the limitations of such a comparison. Alternatively, provide predictions that could be tested experimentally.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Simulation convergence
- **Claim pointer** The manuscript states that simulations are run for 120 ns (or 100 ns for long protamine) and that "reducing the DNA length is an unavoidable choice for staying close to experimentally-investigated dilute-DNA regimes."
- **Evidence pointer** Section 2.2 (MD simulation with scaled-down CG models) and Section 2.4 (Unbiased MD simulation from a homogeneous mixture).
- **Concern** The manuscript does not provide evidence that the simulations have reached equilibrium or steady state within the 120 ns timescale. The text mentions that "the dynamics slowed down upon coarsening" and that the nature of small bundles is "tricky to precisely assess," suggesting that the system may not be fully equilibrated. Additionally, the use of scaled-down models (17 nm DNA vs. 50 nm experimental) may affect the kinetics and the final states observed.
- **Why it matters** If the simulations are not converged, the reported phase behavior and threshold values may be time-dependent and not representative of the true equilibrium or steady-state behavior.
- **Resolution test** Provide convergence checks, such as time evolution of key observables (e.g., number of bundles, bundle size, charge ratio) showing that they plateau before the end of the simulation. Discuss the potential impact of the reduced DNA length on the results.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Model parameterization
- **Evidence pointer** Section 2.1 (Electrostatic-oriented simple CG models)
- **Issue** The manuscript states that the bond stretching constant Kstretch and bending constant Kbend are "simply set to a standard value of 700 kcal mol−1 Å−2" and "700 kcal mol−1 rad−2," respectively, but does not justify these choices or discuss their sensitivity. The choice of Kbend is noted to affect persistence length, but the impact on the results is not explored.
- **Required correction** Provide a brief justification for the chosen values, or include a sensitivity analysis showing that the results are robust to reasonable variations in these parameters.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Interpretation of results
- **Affected element** Charge disproportionation mechanism
- **Evidence pointer** Section 3.1 (Stage 2. DNA assembly)
- **Issue** The manuscript attributes bundle formation to a "charge disproportionation mechanism" but does not provide a clear definition or quantitative measure of charge disproportionation in the simulations. The term is used descriptively, but it is unclear how it is identified or quantified.
- **Required correction** Define charge disproportionation in the context of the simulations and provide a metric (e.g., variance in charge ratio across bundles) to support the claim.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Biological relevance
- **Affected element** Discussion of spermatogenesis
- **Evidence pointer** Abstract and Conclusion
- **Issue** The manuscript connects the findings to spermatogenesis and biomolecular condensates, but this connection is speculative and not developed in the discussion. The relevance to chromatin-nucleoplasm patterning is mentioned but not elaborated.
- **Required correction** Either expand the discussion of biological implications with specific hypotheses or temper the claims to avoid overreach.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Simulation setup
- **Evidence pointer** Section 2.2 (MD simulation with scaled-down CG models)
- **Issue** The manuscript does not specify the initial configuration of the simulations (e.g., random distribution vs. pre-arranged) or the equilibration protocol beyond the first 5 ns. This makes it difficult to reproduce the simulations.
- **Required correction** Provide details on the initial setup and equilibration procedure, or reference a previous publication where these are described.

## Risk / unsupported claims
- The claim that the simple model "reproduces the phase behaviour of DNA in a wide range of protamine concentrations under low salt conditions" is not fully supported without the missing figures and quantitative comparison to experiments.
- The claim that protamine length alters RCR from 8-12 to ~2.4 is based on data not shown and requires verification.
- The statement that "the influence of the protamine length on the DNA aggregation onset RCA would be minor" is supported only by qualitative observations and lacks statistical backing.
- The connection to spermatogenesis and biomolecular condensates is speculative and not substantiated by the simulation results.
- The assertion that the model captures "the crucial role of electrostatic interaction" is plausible but not definitively proven, as non-electrostatic effects are not systematically excluded.