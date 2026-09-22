## Review setup

- **Input scope** Full manuscript text (Introduction, Model, Results, Conclusion, Methods, Analytical model) without figures or supplementary materials
- **Assessment boundary** Scientific content, methodological soundness, claims versus evidence, and clarity of the reported simulation study
- **Shared manuscript claim summary** The authors use Brownian dynamics simulations of Lennard-Jones particles interacting with fixed chromatin-like fiber substrates to show that local fiber geometry and global network organization control condensate size, multiplicity, wetting behavior, and spatial localization, providing an equilibrium physical mechanism for chromatin-guided biomolecular condensate organization.
- **Visible evidence base** Text descriptions of simulation results, qualitative references to Figures 1–9, and an analytical model in Appendix B. No actual figure data, numerical values, or simulation trajectories are available in the provided material.
- **Missing materials affecting confidence** All figures and their underlying numerical data, simulation parameter tables (Table 1 referenced but not shown), error bars or statistical analyses, convergence tests, and details of the LAMMPS implementation are absent. This severely limits quantitative verification of the claims.

## Reviewer

- **Overall assessment** The manuscript addresses a timely and biologically relevant question: how the multiscale architecture of chromatin influences the formation and positioning of biomolecular condensates. The authors employ a minimal coarse-grained model that isolates geometric effects from chromatin dynamics, which is a sensible and potentially powerful approach. The qualitative findings, such as wetting transitions, preferential nucleation at loops and intersections, and localization driven by network asymmetry, are plausible and consistent with existing experimental observations. However, the current manuscript, as presented without figures and quantitative data, cannot be fully evaluated. The claims are largely qualitative, and the connection between the simulation observables and the proposed biological implications requires more rigorous quantitative support. The analytical model in Appendix B is a useful addition but its validation against simulation data is only described qualitatively. The writing is generally clear, but some sections, particularly the results, rely heavily on figure descriptions that are not available for inspection.

- **Who would be interested in the results, and why** Researchers in the fields of biophysics, soft matter physics, and chromatin biology would find this work relevant. Specifically, those studying liquid-liquid phase separation, biomolecular condensates, chromatin organization, and the physical mechanisms underlying nuclear compartmentalization would benefit from the systematic exploration of how fiber geometry and network topology influence condensate behavior. The work also speaks to the broader community interested in wetting phenomena on structured substrates and the role of geometric confinement in phase separation.

- **Major strengths** The study addresses a significant gap in the field by systematically varying fiber geometry from simple linear fibers to complex networks, allowing the authors to disentangle local and global geometric effects. The use of a minimal model is appropriate for isolating the physical mechanisms at play. The identification of distinct regimes (single-droplet, multi-droplet, coating) and the analogy to wetting transitions provides a useful conceptual framework. The inclusion of an analytical model to complement simulations is a strength, as it offers a potential route to predictive understanding. The authors also appropriately acknowledge the limitations of their model, such as neglecting chromatin dynamics.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The manuscript claims that "protein–chromatin interactions induce wetting transitions that modify droplet morphology and shift the effective phase behavior" and that "local fiber geometry and global network organization markedly affect droplet size, morphology, and multiplicity."
- **Evidence pointer** Figures 2, 3, 4, 5, 7, 8; location not provided
- **Concern** The central claims of the paper are presented without any quantitative data in the provided text. The descriptions of figures are qualitative ("marked change," "sharp increase," "significantly more likely"), but no numerical values, error bars, or statistical tests are reported. For example, the transition in Figure 3(b) is described as "sharp," but the actual values of the contact number and the precise location of the transition are not given. Similarly, the claim that droplets are "significantly more likely" to be near loops is not supported by any statistical measure.
- **Why it matters** Without quantitative data, the reader cannot assess the magnitude of the effects, the robustness of the observed transitions, or the significance of the differences between geometries. The claims, as presented, are not verifiable and the scientific case is not established.
- **Resolution test** The authors must provide the actual data from Figures 2–9, including numerical values, error bars, and statistical analyses (e.g., standard deviations, confidence intervals, or p-values where appropriate). The transition points in Figures 3 and 8 should be clearly identified with numerical values. The claim of preferential localization should be supported by a quantitative comparison of g_DN(r) and g_DI(r) or g_DS(r) with appropriate statistical significance.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript states that "the time to reach steady state increases significantly" for network systems and that "some droplet may be locally trapped in some metastable positions on the network," yet the analysis proceeds without a clear demonstration that the systems have reached equilibrium.
- **Evidence pointer** Section IV.2; location not provided
- **Concern** The authors acknowledge the presence of metastable states in the network simulations but do not provide a rigorous method for determining whether the systems have reached steady state. The statement "in any case the simulation time is much larger than that of all previous systems, which are clearly at steady-state" is not a sufficient justification. Without a convergence criterion (e.g., time-independence of order parameters, autocorrelation analysis, or multiple independent runs), the results, particularly the droplet size distributions and localization measures, may be influenced by non-equilibrium effects.
- **Why it matters** If the systems are not at steady state, the reported droplet configurations and statistics may not represent equilibrium behavior, undermining the conclusions about the role of geometry in controlling condensate organization.
- **Resolution test** The authors should provide a clear definition of steady state and demonstrate that it has been achieved for each system, for example by showing that key observables (droplet number, size, position) are time-independent over a significant fraction of the simulation, or by running multiple independent simulations and showing convergence.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The manuscript describes a "minimal analytical model" in Appendix B that predicts transition points, but the model's parameters and validation are not fully described.
- **Evidence pointer** Appendix B; location not provided
- **Concern** The analytical model is presented with equations, but the fitting procedure for the relationship between droplet radius and particle number is only mentioned ("inferred from the simulations data, by fitting"). The values of the fitted parameters, the quality of the fit, and the range of validity of the model are not reported. Furthermore, the comparison between the analytical predictions and the simulation results is only qualitative ("leads to a sharp transition similar to the one shown in Figure 3(b)").
- **Why it matters** For the analytical model to be a useful contribution, it must be fully specified and its predictive power must be quantitatively demonstrated. Without this, the model remains an illustrative sketch rather than a validated tool.
- **Resolution test** The authors should provide the full details of the fitting procedure, including the functional form, the fitted parameter values, and a measure of the fit quality. They should also provide a quantitative comparison between the analytical predictions and the simulation data, for example by overlaying the predicted transition lines on the simulation results in Figure 3(c).

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that "large-scale asymmetries in fiber organization can induce robust spatial localization of the dense phase," and that this is "consistent with recent experimental observations of DNA repair condensates."
- **Evidence pointer** Section IV.2, Figure 9; location not provided
- **Concern** The biological relevance of the findings is asserted but not deeply explored. The connection to DNA repair condensates is mentioned, but the specific geometric or energetic conditions that would correspond to the experimental systems are not discussed. The claim of "robust" localization is not quantified, and the parameter range over which this robustness holds is not mapped.
- **Why it matters** For the work to have impact beyond the specific model system, the authors need to articulate more clearly how their findings translate to biological contexts. The current discussion is too brief to establish the significance of the results for understanding nuclear organization.
- **Resolution test** The authors should expand the discussion to include a more detailed comparison with experimental systems, identifying the relevant parameter regimes and making testable predictions. They should also quantify the robustness of localization, for example by showing how the degree of localization varies with the strength of the density contrast or the interaction parameters.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section II.1, model description
- **Evidence pointer** Section II.1; location not provided
- **Issue** The evolution equation for the Brownian dynamics is mentioned but not explicitly written out in the provided text. The description of the integration scheme via LAMMPS is brief.
- **Required correction** The authors should include the explicit Langevin equation used, including the form of the noise and any thermostat parameters, to ensure the model is fully specified.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section IV.2, network simulations
- **Evidence pointer** Section IV.2; location not provided
- **Issue** The description of the network simulations is dense and would benefit from a clearer explanation of how the networks are constructed and how the "density contrast" is defined and varied.
- **Required correction** The authors should provide a more detailed description of the network generation procedure, including the number of fibers, their lengths, and the method for creating the density contrast, to aid reproducibility.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section II.3, coarse-grained chromatin
- **Evidence pointer** Section II.3; location not provided
- **Issue** The choice of the Lennard-Jones parameters (ε_PP, ε_PC, σ_PC) is not justified in the text. The mapping to physical units is only partially described.
- **Required correction** The authors should provide a table of all interaction parameters and a brief justification for their choices, including how they relate to known biophysical values if applicable.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section VI, data availability
- **Evidence pointer** Section VI; location not provided
- **Issue** The data availability statement is vague, stating that data will be made available "on reasonable request" without specifying what data will be shared.
- **Required correction** The authors should specify the exact data that will be shared (e.g., simulation input files, trajectories, analysis scripts) and consider depositing them in a public repository to enhance reproducibility.

- **Technical failings that need to be addressed before the case is established** The absence of quantitative data from all figures is the primary technical failing. The manuscript cannot be evaluated for the validity of its claims without the actual simulation results. Additionally, the lack of a clear steady-state criterion for the network simulations and the incomplete specification of the analytical model are significant issues that must be resolved.

- **Assessment against Nature-style criteria** 
  - **Originality:** The work is original in its systematic exploration of how fiber geometry and network topology affect condensate behavior in a minimal model. The analogy to wetting transitions is not entirely new but is applied here in a novel context.
  - **Scientific importance:** The question of how chromatin architecture influences condensate formation is of high importance in cell biology and biophysics. However, the current manuscript does not yet demonstrate sufficient quantitative insight to establish its importance beyond a proof-of-principle.
  - **Interdisciplinary readership:** The topic is inherently interdisciplinary, spanning physics, biology, and soft matter. The writing is accessible to a broad audience, but the lack of quantitative results limits its appeal to specialists who would want to see concrete numbers.
  - **Technical soundness:** The simulation approach is appropriate, but the lack of quantitative data and the incomplete description of the analytical model and steady-state determination prevent a full assessment of technical soundness.
  - **Readability for nonspecialists:** The manuscript is generally well-written and the concepts are explained clearly. However, the heavy reliance on figure descriptions without the figures themselves makes it difficult for any reader to follow the results.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript addresses a relevant and interesting question with a sensible approach, but the absence of quantitative data and the incomplete methodological details prevent a full evaluation. The authors should be encouraged to resubmit a revised version that includes all figures with numerical data, statistical analyses, a clear steady-state criterion, and a fully specified analytical model. If these issues are addressed, the work could become a valuable contribution to the field.