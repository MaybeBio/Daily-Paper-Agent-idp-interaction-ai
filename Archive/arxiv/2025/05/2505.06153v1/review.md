## Review setup
- **Input scope** Full manuscript text (main text, methods appendices, figure captions not fully provided)
- **Assessment boundary** Scientific content, methodology, claims, and internal consistency of the provided manuscript. No external literature verification performed.
- **Shared manuscript claim summary** The authors develop a microscopic stochastic model of chemically active droplets, combining Brownian dynamics simulations with a mean-field compartment model, to show that active chemical reactions can control encounter kinetics between biomolecules. They find that condensates can either accelerate or decelerate molecular encounters depending on the match between residence time and encounter time within droplets.
- **Visible evidence base** Main text sections I-VII, methods appendices (BD simulations, stochastic reactions, system sizes, cluster analysis, encounter time computation, diffusion coefficients, residence times). Figures referenced but not fully visible in provided material.
- **Missing materials affecting confidence** Figure panels (Figs. 1-4) not fully visible; supplementary material referenced but not provided; exact parameter values for some simulations not stated in main text; numerical values for key results (e.g., encounter time ratios) not explicitly given.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question in the field of biomolecular condensates: whether phase separation accelerates or decelerates biochemical reactions. The authors combine a mean-field compartment model with Brownian dynamics simulations of a Lennard-Jones fluid with active interconversion reactions. The central finding, that encounter kinetics can be optimized when residence time matches encounter time within droplets, is conceptually interesting and potentially impactful. However, the manuscript has several technical weaknesses that need to be addressed before the case is fully established. The mean-field model's assumptions require more careful justification, the comparison between model and simulation needs more quantitative rigor, and the connection to real biological systems remains speculative without more concrete parameter estimates.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, and intracellular organization would be the primary audience. The work is also relevant to the broader community interested in reaction kinetics in compartmentalized or confined media, including soft matter physicists, physical chemists, and systems biologists. The conceptual framework of matching residence and encounter times could inform experimental design in synthetic biology and drug delivery.

- **Major strengths** 
  1. The question addressed is important and timely, with direct relevance to understanding the functional role of biomolecular condensates.
  2. The combination of a tractable mean-field model with explicit Brownian dynamics simulations provides complementary perspectives.
  3. The identification of three distinct kinetic regimes based on the ratio of residence to encounter time is a clear and useful conceptual framework.
  4. The authors are careful to note limitations of equilibrium results and extend to active systems.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The mean-field model is claimed to "reproduce qualitatively well the long-time encounter dynamics predicted by the BD simulations" (Section III) and "a good qualitative agreement of simulation data with the prediction from the mean field model, with no fitting parameter" (Section VI).
- **Evidence pointer** Section III, Fig. 2b; Section VI, Fig. 4b
- **Concern** The manuscript claims qualitative agreement between the mean-field model and BD simulations, but the evidence presented is not sufficient to assess this claim. The figures are not fully visible in the provided material, and no quantitative measures of agreement (e.g., error bars, statistical tests, or quantitative comparison metrics) are provided. The statement "qualitative agreement" is vague and could mask significant discrepancies. Furthermore, the claim that "none of the model parameters is adjusted" is difficult to verify without a complete list of all parameters used in both the mean-field model and the simulations.
- **Why it matters** The central thesis of the paper rests on the validity of the mean-field model as a predictive tool. If the agreement is only qualitative and not rigorously established, the quantitative predictions (e.g., the scaling law in Fig. 2c) may not be reliable. The reader cannot evaluate the strength of the evidence without seeing the actual data and a quantitative comparison.
- **Resolution test** Provide the actual data points for both the mean-field model and BD simulations in the figures, with error bars. Include a quantitative measure of agreement (e.g., relative error, chi-squared statistic) for the key comparisons. Provide a complete table of all parameters used in both approaches, with their sources (simulation measurements, theoretical estimates, or fitted values).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript states that "all the data collapse on the same line of equation 𝒯e/𝒯0 = 1.14 Dc v/(Dd V)" (Section III, Fig. 2c).
- **Evidence pointer** Section III, Fig. 2c
- **Concern** The data collapse presented in Fig. 2c is a strong claim that suggests a universal scaling relationship. However, the derivation of this scaling law is not provided. The factor 1.14 appears to be an empirical fit, but its origin is unclear. Moreover, the range of parameters over which this collapse holds is not specified. The manuscript also notes that "the curve collapse for 𝒩 > 1 is not as good as with single droplet systems," which raises questions about the universality of the scaling. The scaling factor α for the multi-droplet case is stated to be "of the order of 5 to 10," which is a very wide range and suggests the collapse is not tight.
- **Why it matters** The scaling law is used to make predictions for biological systems (e.g., the estimate that phase separation becomes unfavorable for Dd < 0.05 Dc). If the scaling is not robust or its range of validity is limited, these predictions may be misleading. The wide range of α for the multi-droplet case undermines confidence in the predictive power of the model.
- **Resolution test** Provide a derivation or at least a heuristic argument for the scaling law. Specify the exact range of parameters (v, Dd, 𝒩) over which the collapse holds. Provide error bars on the data points in Fig. 2c and quantify the scatter around the collapse line. For the multi-droplet case, provide a more precise estimate of α and its dependence on system parameters.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that "condensates can either accelerate or decelerate molecular encounters" and that "matching the residence time to the encounter time in droplets leads to a maximum of the kinetic rate of encounter in the active phase separated system."
- **Evidence pointer** Sections V-VI, Figs. 3-4
- **Concern** While the finding of an optimal residence time is interesting, the biological relevance is not fully established. The model uses a generic Lennard-Jones potential and a simplified two-state (A/B) description of proteins. Real biomolecular condensates involve complex multicomponent interactions, post-translational modifications, and active processes that may not be captured by this minimal model. The connection to specific biological systems (e.g., RNA granules in C. elegans) is made through rough estimates, but the authors do not discuss whether the predicted effects are experimentally testable or whether they have been observed.
- **Why it matters** The broader impact of this work depends on its relevance to real biological systems. If the model is too idealized, the predictions may not be applicable to actual condensates. The authors should more carefully discuss the limitations of their model and propose concrete experimental tests of their predictions.
- **Resolution test** Discuss the limitations of the minimal model in more detail. Propose specific experimental systems where the predicted optimal residence time could be tested (e.g., by varying the strength of active reactions or the viscosity of the condensate). If possible, compare the model predictions with existing experimental data on reaction kinetics in condensates.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The manuscript states that "the residence time τres strongly decreases with Δμ" (Section V, Fig. 3e) and that this controls encounter kinetics.
- **Evidence pointer** Section V, Fig. 3e
- **Concern** The relationship between the chemical drive Δμ and the residence time is a key mechanistic link in the paper, but the physical mechanism is not fully explained. The authors state that active reactions break detailed balance and generate fluxes, but the connection between these fluxes and the residence time is not made explicit. Is the decrease in residence time due to increased conversion of B to A (which then leaves the droplet)? Or is it due to changes in the droplet interface or size? The manuscript would benefit from a more mechanistic explanation of this relationship.
- **Why it matters** Understanding the mechanism by which active reactions control residence time is crucial for predicting how the system behaves under different conditions. Without this understanding, it is difficult to extrapolate the results to other parameter regimes or to design experiments.
- **Resolution test** Provide a more detailed mechanistic explanation of how Δμ affects residence time. This could include a theoretical analysis of the reaction-diffusion equations or additional simulation results that isolate the contributions of different processes (e.g., reaction rate vs. diffusion).

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section II, mean-field model description
- **Evidence pointer** Section II
- **Issue** The description of the mean-field model is brief and the master equations are not explicitly written out in the main text. The reader is referred to the methods, but the connection between the model states (1)-(5) and the rates is not fully transparent.
- **Required correction** Write out the master equations explicitly in the main text or in a clearly labeled box. Define all rates and parameters in one place.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section III, equilibrium simulations
- **Evidence pointer** Section III, Fig. 2
- **Issue** The manuscript states that the diffusion coefficient in the droplet is "roughly 16 times smaller" than in the continuous phase, but the method for measuring this is only described in the appendix. It would be helpful to state this in the main text and to specify whether this value is the same for all droplet sizes.
- **Required correction** State the measured diffusion coefficient ratio in the main text and specify whether it varies with droplet size.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section VI, client-scaffold model
- **Evidence pointer** Section VI, Fig. 4
- **Issue** The introduction of client proteins (A', B') in Section VI is somewhat abrupt. The motivation for this extension and its relationship to the scaffold-only model should be clarified.
- **Required correction** Add a brief paragraph explaining why the client-scaffold distinction is introduced and how it relates to the biological question.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section III, parameter estimates
- **Evidence pointer** Section III
- **Issue** The estimates for biological parameters (e.g., 20% of biomolecules in droplets, 30% volume fraction) are presented without citations. While these are likely reasonable, the lack of references makes it difficult to assess their accuracy.
- **Required correction** Add citations for the biological parameter estimates or state that they are illustrative.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section VII, Discussion
- **Evidence pointer** Section VII
- **Issue** The discussion of "three distinct kinetic regimes" is clear, but the connection to the earlier figures (Fig. 3d-g) could be made more explicit. A summary figure or table showing the regimes and their characteristics would be helpful.
- **Required correction** Consider adding a schematic figure or table summarizing the three regimes and their key features.

- **Technical failings that need to be addressed before the case is established** 
  R1-M1 (quantitative agreement between model and simulation not established), R1-M2 (scaling law not derived and its range of validity not specified)

- **Assessment against Nature-style criteria** 
  - **Originality**: The work is original in its combination of a mean-field compartment model with explicit simulations of active droplets. The concept of matching residence and encounter times as a design principle is novel.
  - **Scientific importance**: The question of whether condensates accelerate or decelerate reactions is of high importance to the condensate field. The finding that active reactions can control encounter kinetics in a non-monotonic way is significant.
  - **Interdisciplinary readership**: The work should appeal to physicists, chemists, and biologists interested in phase separation and cellular organization. The writing is accessible, though some parts (e.g., the mean-field model) could be clearer for non-specialists.
  - **Technical soundness**: The simulation methodology appears sound, but the quantitative comparison between model and simulation is not rigorous enough. The scaling law is not derived, and its range of validity is unclear.
  - **Readability for nonspecialists**: The manuscript is generally well-written and the main ideas are clearly conveyed. However, the mean-field model section could benefit from more explanation for readers not familiar with such models.

- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual framework is interesting and potentially impactful, but the quantitative basis for the claims needs to be strengthened. Specifically, the authors should provide a more rigorous comparison between the mean-field model and simulations, derive or better justify the scaling law, and clarify the range of parameters over which their conclusions hold.

## Risk / unsupported claims
- The claim of "good qualitative agreement" between mean-field model and BD simulations is not quantitatively supported by the visible evidence.
- The scaling law 𝒯e/𝒯0 = 1.14 Dc v/(Dd V) is presented without derivation or error analysis.
- The estimate that phase separation becomes unfavorable for Dd < 0.05 Dc relies on the unvalidated scaling law and specific biological parameter choices.
- The claim that "matching the residence time to the encounter time in droplets leads to a maximum of the kinetic rate" is supported by the model, but the biological relevance is not experimentally validated.
- The relationship between Δμ and residence time is stated but not mechanistically explained.
- The biological parameter estimates (20% of biomolecules in droplets, 30% volume fraction) are presented without citations.