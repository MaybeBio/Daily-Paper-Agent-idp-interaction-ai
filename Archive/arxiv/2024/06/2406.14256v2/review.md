## Review setup
- **Input scope** Full manuscript text (arXiv preprint 2406.14256v2), including main text, figure captions, and references. Supplementary Material referenced but not provided.
- **Assessment boundary** Scientific content, methodological soundness, claims versus evidence, and presentation quality of the main text. No assessment of code availability, reproducibility scripts, or supplementary figures/data.
- **Shared manuscript claim summary** The authors present a particle-based (Brownian dynamics) model of chemically active droplets, where particles switch between droplet-forming (B) and non-forming (A) states via rates that depend on local density and a chemical drive Δμ. They claim this is the first microscopic stochastic simulation of active droplets, and that it captures size selection, polydispersity, shape anisotropy, and droplet lifetimes in the nonequilibrium steady state.
- **Visible evidence base** Main text with 5 figures (referenced), equations for dynamics and rates, and qualitative descriptions of simulation results. No numerical data tables, no error bars, no convergence tests, no parameter sweeps beyond Δμ variation.
- **Missing materials affecting confidence** Supplementary Material (SM) is referenced extensively for numerical methods, cluster analysis, tracking algorithm, parameter choices, and additional results. Without SM, several key methodological details and robustness checks cannot be evaluated. Also missing: simulation movie files, exact parameter values (system size, particle number, time steps, statistics), and quantitative error analysis.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important problem: bridging microscopic particle-based simulations with continuum theories of chemically active droplets. The model is conceptually appealing and the qualitative results (size selection, polydispersity, shape anisotropy, lifetime distributions) are plausible and potentially significant. However, the main text as provided lacks sufficient quantitative detail to fully assess the robustness and generality of the claims. The heavy reliance on SM for essential methodological information is a concern. The claim of "unprecedented" and "first" particle-based simulations needs careful contextualization against existing active-switching particle models. The physical interpretation of the size-selection mechanism, while qualitatively consistent with continuum theories, is not rigorously established from the presented data. Overall, the work is promising and likely of interest to the soft matter and biophysics communities, but the current evidence base is insufficient to fully support all claims made.

- **Who would be interested in the results, and why** Researchers in soft matter physics, biophysics, and physical chemistry studying phase separation, biomolecular condensates, and active matter. Specifically, those interested in nonequilibrium self-assembly, droplet dynamics, and the role of chemical reactions in controlling condensate properties. The methodological advance (particle-based simulations with controlled nonequilibrium drive) would also appeal to computational scientists developing simulation tools for active systems.

- **Major strengths**
  1. The model is conceptually clear and directly addresses a gap in the literature: most existing theories of active droplets are continuum and deterministic, while this work provides a microscopic stochastic framework.
  2. The design of the chemical drive (local-density-dependent rates) is physically motivated and allows controlled deviation from equilibrium, with a clear connection to ATP-driven processes.
  3. The analysis goes beyond static structure, providing dynamical quantities (droplet tracking, lifetimes, phase portraits) that are genuinely new in this context.
  4. The qualitative findings (size selection, polydispersity, shape anisotropy, death mechanisms) are consistent with and extend continuum predictions, suggesting the model captures essential physics.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / Reproducibility
- **Claim pointer** "we propose a microscopic and stochastic model for chemically active droplets" and "we fully characterize the nonequilibrium steady state"
- **Evidence pointer** Model section, Figures 2–5; SM referenced but not provided
- **Concern** The main text lacks essential quantitative details about the simulation setup: system size (number of particles, box dimensions), integration time step, total simulation time, number of independent runs, and statistical averaging procedures. The cluster analysis and droplet tracking algorithms are described only by reference to SM. Without these details, the results cannot be reproduced or independently verified, and the statistical significance of the reported quantities (e.g., ⟨v⟩, distributions, phase portraits) cannot be assessed.
- **Why it matters** Reproducibility is a core requirement for computational studies. The absence of these details in the main text, combined with the inaccessibility of SM in this review, prevents verification of the central claims. Moreover, finite-size effects are acknowledged as a limitation for Δμ < 4, but the system size is not stated, making it impossible to judge whether the reported results for Δμ = 4 and 4.5 are free from such effects.
- **Resolution test** Provide full simulation parameters in the main text or ensure SM is available and contains: system size, particle number, time step, total time, number of runs, and convergence tests. Show that results are robust to system size and simulation time.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Originality / Contextualization
- **Claim pointer** "To our knowledge, the present work constitutes the first particle-based simulations of active droplets that form through the interplay between phase separation and chemical reactions which are driven away from equilibrium in a controlled way."
- **Evidence pointer** Introduction, Conclusion
- **Concern** The claim of being "first" is strong and requires careful contextualization. The authors cite previous work on "active switching" particles (Refs. Decayeux et al., Alston et al., Bley et al., Moncho-Jordá and Dzubiella, Longo et al.) but dismiss these as having rates "independent of their local environment." However, it is not clear from the main text whether any of these prior models included density-dependent switching or achieved similar size-selection behavior. A more thorough comparison with existing particle-based models of active or driven phase separation is needed to substantiate the novelty claim.
- **Why it matters** The novelty claim is central to the paper's significance. If similar models exist with comparable physics, the contribution is incremental rather than groundbreaking. The current treatment is too brief to establish priority or distinguish the present approach from prior work.
- **Resolution test** Expand the comparison with prior particle-based models, explicitly stating differences in model construction (e.g., density-dependent rates, detailed balance breaking) and in observed phenomena (e.g., size selection, polydispersity). If prior models exist, explain what new physics the present work adds.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Evidence strength / Quantitative support
- **Claim pointer** "we reveal how driving the system away from equilibrium in a controlled way determines the fluctuations and dynamics of active emulsions" and "the active pathway controls not only the size and shape of the droplets, but also the time during which they persist"
- **Evidence pointer** Figures 2–5
- **Concern** The qualitative trends are clear from the figures, but quantitative support is weak. For example, the phase portrait in Figure 4 shows ⟨v̇⟩ as a function of v, but no error bars or confidence intervals are provided. The claim that the stable fixed point v* corresponds to the maximum of P(v) is stated but not quantitatively demonstrated (e.g., no comparison of v* with the peak position). The lifetime distributions in Figure 5 are described qualitatively, but no statistical measures (mean, median, variance) are given. The dependence of polydispersity and shape anisotropy on Δμ is shown but not quantified.
- **Why it matters** The paper's central message is that the nonequilibrium drive controls droplet properties in a predictable way. Without quantitative measures and error analysis, it is unclear whether the observed trends are statistically significant or robust across realizations. This weakens the case for the model's predictive power.
- **Resolution test** Add quantitative analysis: report mean and standard deviation of droplet volumes, polydispersity indices, and shape anisotropy for each Δμ. Provide statistical tests (e.g., bootstrap or multiple independent runs) to support claims of trend significance. Quantitatively compare v* from the phase portrait with the peak of P(v).

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Physical interpretation / Theoretical connection
- **Claim pointer** "This mechanism for droplet size selection is therefore a microscopic and stochastic counterpart to the predictions from continuous and deterministic models"
- **Evidence pointer** Figure 4, Discussion
- **Concern** The connection to continuum theories is asserted but not rigorously established. The authors state that the size-selection mechanism is a "compromise between a growth (resp. loss) term," but they do not derive or measure these terms from their simulations. The phase portrait shows a stable fixed point, but the physical origin of the v̇(v) shape (e.g., why growth dominates at small v and shrinkage at large v) is not explained from microscopic principles. The authors also acknowledge that "we cannot identify these terms unambiguously given the limited statistics at small volumes," which weakens the mechanistic claim.
- **Why it matters** The paper's significance partly rests on connecting microscopic simulations to established continuum theories. If this connection is only qualitative and not quantitatively validated, the advance over existing theory is less clear. A more rigorous comparison (e.g., extracting effective growth/loss rates from simulations and comparing with theory) would strengthen the paper.
- **Resolution test** Provide a more detailed analysis of the growth and shrinkage mechanisms, possibly by measuring fluxes of B particles into and out of droplets as a function of droplet size. Compare the resulting v̇(v) with predictions from continuum theories (e.g., Zwicker et al.) and discuss discrepancies.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity / Presentation
- **Affected element** Model section, equation for dynamics
- **Evidence pointer** Model section, "The evolution equations of the particles positions read:" followed by an empty equation
- **Issue** The equation for the particle dynamics is missing from the main text. The sentence "The evolution equations of the particles positions read:" is followed by nothing, likely a formatting error.
- **Required correction** Insert the correct equation for the overdamped Langevin dynamics, including the force terms from interparticle potentials and the noise term.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity / Terminology
- **Affected element** Introduction, Model section
- **Evidence pointer** "active droplets" used throughout; "chemically active droplets" in title
- **Issue** The terminology is inconsistent. The title uses "chemically active droplets," while the introduction and conclusion use "active droplets" and "active emulsions." Clarify whether these terms are interchangeable or refer to distinct concepts.
- **Required correction** Define terms at first use and use consistently throughout.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness / Parameter justification
- **Affected element** Model section, parameter choices
- **Evidence pointer** "We fix k0 = 10−2 in all the simulations" and "ε = 2kBT"
- **Issue** The choice of k0 and ε is stated but not justified. Why these values? How sensitive are the results to these parameters? The authors note that "the choice of parameters is discussed in details in SM," but this is not accessible in the current review.
- **Required correction** Provide a brief justification in the main text or ensure SM contains a sensitivity analysis showing that results are robust to parameter variations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness / Statistical reporting
- **Affected element** Figures 2–5
- **Evidence pointer** All figures
- **Issue** No information is given on the number of independent simulations, the length of each simulation, or how statistical averages are computed. Error bars are absent from all figures.
- **Required correction** Add error bars or confidence intervals to all quantitative plots, and state the number of independent runs and averaging procedure in the main text or figure captions.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Physical interpretation / Crowding
- **Affected element** Model section, crowders
- **Evidence pointer** "C particles are crowders that do not undergo any reaction. Their density is chosen in such a way that the total volume fraction is 0.1."
- **Issue** The role of crowders is not discussed in the results. Do they affect droplet formation, size selection, or dynamics? Is the crowder density varied? The conclusion mentions "macromolecular crowding" as a perspective, but the current simulations do not seem to explore this.
- **Required correction** Either discuss the role of crowders in the results or remove them from the model if they do not play a significant role. If crowding effects are a future direction, state this explicitly.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness / Comparison with experiments
- **Affected element** Conclusion
- **Evidence pointer** "This property may play a key role in some biological processes"
- **Issue** The biological relevance is mentioned but not developed. No comparison with experimental observations of condensate lifetimes or polydispersity is provided. A brief discussion of how the model predictions could be tested experimentally would strengthen the paper.
- **Required correction** Add a short paragraph in the conclusion discussing potential experimental tests or comparisons with existing experimental data.

## Risk / unsupported claims
- The claim of being "the first particle-based simulations of active droplets" is not fully substantiated without a more thorough comparison with prior particle-based models of active switching or driven phase separation.
- The assertion that the size-selection mechanism is a "microscopic and stochastic counterpart" to continuum theories is only qualitative; no quantitative comparison with theory is provided.
- The claim that "the active pathway controls... the time during which they persist" is based on lifetime distributions that are not statistically characterized.
- The role of crowders (C particles) in the results is not discussed, making their inclusion in the model appear decorative rather than functional.
- The statement that "large, aspherical droplets... are quite rare" is not quantified, and the connection between shape anisotropy and coalescence events is not rigorously established.
- The generalizability of the model to "a wide range of systems" (conclusion) is asserted without demonstration.