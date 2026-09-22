## Review setup
- **Input scope** Full manuscript text (main text, methods, figure legends not provided separately)
- **Assessment boundary** Scientific content, methodological soundness, claims versus evidence, and presentation quality based solely on the supplied text
- **Shared manuscript claim summary** The authors use mean-field modeling and Brownian dynamics simulations to show that chemically active droplets can control encounter kinetics between molecules, with residence time matching encounter time within droplets leading to optimal reaction rates, challenging the simple view of condensates as uniformly beneficial nanoreactors.
- **Visible evidence base** Main text equations (Eqs. 1-11), Figures 1-4 (referenced but not shown), SI references (Figs. S2-S8), simulation methods, parameter choices, and comparison between mean-field predictions and BD simulation results.
- **Missing materials affecting confidence** Figure panels themselves, SI figures and derivations, exact parameter values for all simulations, statistical error bars, convergence criteria, and details of the mean-field model derivation are not fully visible in the provided text.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question in the field of biomolecular condensates: whether and how chemically active droplets can control encounter kinetics. The authors combine a mean-field kinetic model with Brownian dynamics simulations of active emulsions, identifying a design principle where matching residence time to intra-droplet encounter time optimizes reaction rates. The work is conceptually interesting and the combination of theory and simulation is appropriate. However, several technical aspects require clarification and strengthening before the conclusions can be fully accepted, particularly regarding the generality of the mean-field model, the parameter ranges explored, and the quantitative robustness of the claimed optimality condition.

- **Who would be interested in the results, and why** Researchers in biophysics, soft matter physics, and cell biology studying biomolecular condensates, phase separation, and intracellular organization. The work is also relevant to the synthetic biology community interested in designing artificial compartments for biochemical reactions, and to theoretical chemists working on diffusion-limited reactions in heterogeneous media.

- **Major strengths**
  1. The manuscript addresses a fundamental and debated question about whether condensates accelerate or slow down biochemical reactions, providing a nuanced answer that depends on kinetic parameters.
  2. The combination of a tractable mean-field model with explicit Brownian dynamics simulations is a powerful approach, and the qualitative agreement between the two lends credibility to the main conclusions.
  3. The identification of a time-scale matching condition (τres ≈ τS,d) for optimal encounter kinetics is a clear, testable prediction that could guide future experimental work.
  4. The authors carefully distinguish between equilibrium and active systems, showing that activity can decouple structure from kinetics, which is a non-trivial and important insight.
  5. The manuscript is generally well-written and accessible, with a clear logical flow from model to simulations to biological implications.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The mean-field model is claimed to "reproduce qualitatively well the long-time encounter dynamics predicted by the BD simulations" for equilibrium systems, and later to show "good qualitative agreement" for active systems with no fitting parameters.
- **Evidence pointer** Section "Equilibrium Brownian Dynamics of Phase-Separated Systems", Fig. 2B; Section "Encounters in Active Systems Are Not Fully Controlled by the Structure of the System", Fig. 4B
- **Concern** The agreement between the mean-field model and BD simulations is stated as "qualitative" but the text does not provide quantitative measures of this agreement. How is "qualitative" defined? Is it visual inspection of curves? Are there error bars on the BD data? What is the typical discrepancy between model and simulation across the parameter range? Without quantitative metrics (e.g., relative errors, chi-squared values, or confidence intervals), it is difficult to assess whether the agreement is genuinely good or merely suggestive. This is particularly important because the mean-field model is used to make predictions about optimal conditions, and the reliability of those predictions depends on the model's accuracy.
- **Why it matters** The central claim of the paper rests on the validity of the mean-field model as a descriptor of the simulated systems. If the agreement is only loose, the quantitative predictions (e.g., the location of the optimum in Fig. 4C) may not be reliable, and the design principles derived from the model could be misleading.
- **Resolution test** Provide quantitative measures of agreement between model and simulation for all compared quantities (e.g., Te values, survival probabilities). Include error bars or confidence intervals on simulation results. State explicitly the maximum and typical relative deviations between model and simulation across the parameter space. If possible, show a parity plot of model-predicted versus simulated Te values.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "there is an optimal mean encounter time for particles in active emulsions when the time to encounter in a droplet τS,d and the time to exit the droplet τres are similar" and that this is a general design principle.
- **Evidence pointer** Section "Time Scale Matching Leads to Encounter Optimization", Fig. 3G, Fig. 4C
- **Concern** The optimality condition is demonstrated for a specific set of parameters and a specific model system. The authors state that "we checked that these results hold for different volumes of the droplets," but no data are shown in the main text. How robust is this optimality across other parameter variations, such as different diffusion coefficient ratios (Dc/Dd), different droplet volume fractions, different interaction strengths, or different numbers of droplets? The mean-field model predicts a non-monotonic dependence of Te on τres, but the depth and width of the minimum may vary. Without a systematic exploration of the parameter space, the claim of a general "time scale matching" principle is not fully established.
- **Why it matters** The paper's main conceptual contribution is the identification of this optimality condition as a design principle for active condensates. If the condition only holds in a narrow parameter regime, its biological relevance and practical utility are diminished.
- **Resolution test** Perform a systematic parameter sweep in the mean-field model (and ideally in BD simulations for a few representative points) varying τres/τS,d, Dc/Dd, droplet volume fraction, and N. Show that the optimality condition (minimum in Te) persists across a wide range of parameters, and quantify how the location and depth of the minimum shift. Present these results in a figure or table.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors state that "our results challenge the simple view of condensates as uniformly beneficial for reactions" and that condensates can act as "agents of repression or activation of specific network elements."
- **Evidence pointer** Section "Discussion"
- **Concern** While the results do show that active droplets can either speed up or slow down encounters depending on parameters, the biological relevance of the specific parameter regimes explored is not thoroughly discussed. For example, the authors mention that in real biocondensates, diffusion can be reduced by up to a factor of 500, and they use this to argue that condensates can slow down encounters. However, they do not systematically map their model predictions onto realistic biological parameter ranges. Which regime (acceleration or repression) is more likely for typical cellular condensates? How sensitive is the conclusion to uncertainties in biological parameters (e.g., droplet size, volume fraction, diffusion coefficients)? A more explicit connection to experimental measurements would strengthen the biological significance of the work.
- **Why it matters** The paper aims to provide insights into the function of biomolecular condensates in cells. If the parameter regimes that lead to repression or activation are not clearly linked to known biological systems, the impact of the work on the broader cell biology community will be limited.
- **Resolution test** Add a section or figure that maps the model predictions onto a realistic range of biological parameters (e.g., using published values for condensate size, protein diffusion coefficients, and volume fractions). Discuss which regime (acceleration, repression, or optimal) is most likely for specific types of condensates and whether the predictions are robust to parameter uncertainty.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "the residence time τres strongly decreases with Δμ" and that this is due to active fluxes across the interface.
- **Evidence pointer** Section "Encounters in Active Systems Are Not Fully Controlled by the Structure of the System", Fig. 3E
- **Concern** The mechanism by which the chemical drive Δμ controls the residence time is not fully explained. The authors state that "a mass flow arises from the conversion of chemical energy into mechanical energy" and that this flow is related to the reaction flux, but the microscopic origin of this effect is not clear. Is it due to a change in the effective interaction potential? A change in the local density? A phoretic effect? The authors reference their previous work (ref 47) for details, but the current manuscript should provide enough information for the reader to understand the physical mechanism without consulting the prior paper.
- **Why it matters** The dependence of residence time on Δμ is a key ingredient in the model and in the interpretation of the simulation results. If the mechanism is not clearly explained, the reader cannot assess whether the effect is robust or an artifact of the specific simulation setup.
- **Resolution test** Provide a more detailed explanation of the physical mechanism by which Δμ controls the residence time. This could include a simple analytical argument, a schematic figure, or additional simulation data (e.g., density profiles, velocity fields) that illustrate the effect.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction and model description
- **Evidence pointer** Section "Mean Field Model for Encounter Kinetics in Mesostructured Media"
- **Issue** The mean-field model is introduced rather abruptly. The states (1)-(5) are described, but the physical meaning of each state and the rationale for choosing these particular states could be explained more clearly for readers not familiar with encounter kinetics in compartmentalized systems.
- **Required correction** Add a brief introductory paragraph explaining the physical picture behind the five states and why this level of coarse-graining is appropriate. A schematic figure showing the states and the transitions between them would be very helpful.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Simulation methods
- **Evidence pointer** Section "Brownian Model of Active Emulsions"
- **Issue** The choice of simulation parameters (e.g., the values of Δw, Δμ, the interaction strengths, the system size) is not justified in the main text. It is unclear whether the chosen parameters are representative of typical biological systems or are chosen for computational convenience.
- **Required correction** Provide a table of all simulation parameters and a brief justification for the chosen values. If the parameters are varied, state the range explored and the rationale for that range.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Discussion
- **Evidence pointer** Section "Discussion"
- **Issue** The discussion of biological implications is somewhat brief and general. The authors mention "post-translational modifications" and "control of encounter kinetics" but do not provide specific examples of biological processes where this mechanism could be important.
- **Required correction** Add a few concrete examples of biological processes where the proposed mechanism could be relevant (e.g., RNA processing, stress granule formation, DNA repair), and discuss how the model predictions could be tested experimentally in these systems.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, encounter time calculation
- **Evidence pointer** Section "Mean Encounter Time Between Brownian Particles"
- **Issue** The definition of the encounter time from the survival probability is clear, but the statistical quality of the estimate is not discussed. How many independent pairs are averaged over? What is the statistical uncertainty in the estimated Te?
- **Required correction** Provide information on the number of pairs used in the averaging and the statistical error on the estimated Te values. If the error is small, state this explicitly.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Figure captions
- **Evidence pointer** Figures 1-4 (captions not provided in the text)
- **Issue** The figure captions are not included in the provided text, making it difficult to fully assess the figures. Based on the text references, the figures appear to be information-dense and may benefit from clearer labeling and annotations.
- **Required correction** Ensure that all figure captions are self-contained and clearly explain the key features of each panel. Consider adding annotations to highlight the main conclusions drawn from each figure.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Model parameters
- **Evidence pointer** Section "Mean Field Model for Encounter Kinetics in Mesostructured Media"
- **Issue** The parameters τS,d, τS,c, τres, and τent are introduced, but it is not clear how they are computed from the BD simulations. Are they measured directly from the trajectories, or are they derived from other quantities?
- **Required correction** Clarify in the Methods section how each of these times is computed from the simulation data. This is important for reproducibility.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion
- **Evidence pointer** Section "Discussion"
- **Issue** The authors do not discuss the limitations of their model. For example, the mean-field model assumes well-mixed compartments and does not account for spatial heterogeneity within droplets or for the effects of droplet coalescence and fission.
- **Required correction** Add a paragraph discussing the limitations of the model and the potential impact of these limitations on the conclusions.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Lack of quantitative agreement metrics between mean-field model and BD simulations.
  - R1-M2: Insufficient exploration of parameter space to establish the generality of the optimality condition.
  - R1-M4: Incomplete explanation of the mechanism by which Δμ controls residence time.

- **Assessment against Nature-style criteria**
  - **Originality**: The work is original in its specific focus on how active chemical processes within droplets control encounter kinetics, and in identifying a time-scale matching condition. The combination of mean-field theory with active emulsion simulations is not entirely new (the authors reference prior work), but the application to encounter kinetics and the identification of the optimality condition is a novel contribution.
  - **Scientific importance**: The question of whether condensates accelerate or repress biochemical reactions is of high importance in cell biology and biophysics. The paper provides a framework that could help resolve conflicting observations. However, the direct biological relevance is not fully established, as the parameter mapping to real systems is incomplete.
  - **Interdisciplinary readership**: The topic is inherently interdisciplinary, spanning soft matter physics, physical chemistry, and cell biology. The manuscript is written in a way that should be accessible to researchers in all these fields, though some parts (e.g., the mean-field model) may be challenging for cell biologists without a physics background.
  - **Technical soundness**: The simulation methodology appears sound, and the mean-field model is a reasonable coarse-grained description. However, the lack of quantitative validation and the incomplete parameter exploration are significant technical weaknesses that need to be addressed.
  - **Readability for nonspecialists**: The manuscript is generally well-written and the main ideas are clearly conveyed. The abstract and introduction are accessible. However, the model description and some of the results sections could be made more accessible with additional explanation and schematics.

- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is interesting and potentially important, and the combination of theory and simulation is appropriate. However, the manuscript in its current form does not fully establish the generality of the main claims due to the lack of quantitative validation and parameter exploration. Addressing these concerns would significantly strengthen the paper.

## Risk / unsupported claims
- The claim that the mean-field model "reproduces qualitatively well" the BD results is unsupported without quantitative metrics.
- The claim of a general "time-scale matching" optimality condition is not fully supported by the limited parameter exploration shown.
- The statement that "there is an optimal mean encounter time... when τS,d and τres are similar" is presented as a general principle but is only demonstrated for a specific set of conditions.
- The biological relevance of the findings is asserted but not quantitatively mapped to realistic cellular parameters.
- The claim that "active chemical processes can drive surface movements that either speed up or slow down molecular encounters" is supported by the simulations, but the mechanism is not fully explained.
- The statement that "the residence time τres strongly decreases with Δμ" is presented without a mechanistic explanation in the main text.