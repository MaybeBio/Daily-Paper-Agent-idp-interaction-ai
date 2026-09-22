## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, methods, results, discussion, conclusions, and supplementary material description.
- **Assessment boundary** Scientific content, methodological rigor, validity of claims, and alignment with stated scope. Editorial quality and formatting are considered only insofar as they affect scientific clarity.
- **Shared manuscript claim summary** The authors use residue-level coarse-grained simulations with the HPS model to study complex coacervates formed by prothymosin α with four cationic partners. They report that equilibrium properties (dense-phase concentrations, ionic-strength-dependent phase behavior, chain dimensions) are reproduced accurately, but that dynamical timescales require system-specific, environment-specific, and potentially observable-specific time rescaling factors. They further report a correlation between the required time rescaling and the mean non-bonded interaction energy per chain, interpreted as evidence for missing frictional effects arising from protein-protein interactions.
- **Visible evidence base** Main text figures (Figs. 1-5), supplementary figures (Figs. S1, S2), supplementary table (Table S1), and methods descriptions. No raw simulation trajectories, force field parameter files, or analysis scripts were provided.
- **Missing materials affecting confidence** Simulation input files, force field parameters, full analysis code, convergence diagnostics beyond those described, and the complete set of numerical values underlying the figures. The supplementary material is referenced but not fully provided in the submitted text.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question in the field of biomolecular condensate simulation: whether coarse-grained models that reproduce equilibrium properties can also be trusted for dynamical properties. The authors present a systematic study across four related coacervate systems, with careful attention to equilibrium validation before addressing dynamics. The central finding, that time rescaling is not transferable across environments or compositions, is well supported by the data presented. The correlation with interaction energy is intriguing and provides a plausible mechanistic hypothesis. However, several technical aspects require clarification, particularly regarding the treatment of the friction coefficient, the interpretation of the diffusion measurements, and the statistical robustness of the key comparisons. The manuscript is clearly written and will be of interest to a broad audience in computational biophysics and biomolecular condensate research.

- **Who would be interested in the results, and why** Researchers using coarse-grained simulations to study biomolecular condensates, intrinsically disordered proteins, and phase separation. The results are also relevant to the broader community developing and applying implicit-solvent coarse-grained models, as they highlight limitations in the transferability of dynamical timescales. Experimentalists using FRET and fluorescence correlation spectroscopy to measure chain dynamics in condensates will find the comparison between simulation and experiment valuable. The work may also interest theorists working on coarse-graining formalisms and generalized Langevin descriptions.

- **Major strengths** The study addresses a question of central importance to the field, namely the validity of dynamical predictions from coarse-grained models that are validated only against equilibrium data. The choice of four related but distinct coacervate systems allows for systematic comparison of composition effects. The authors validate equilibrium properties carefully before addressing dynamics, which strengthens the interpretation of the dynamical findings. The correlation between time rescaling and interaction energy provides a physically plausible and potentially predictive framework. The manuscript is well written and accessible to nonspecialists.

- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
  - R1-M4
  - R1-M5

- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
  - R1-m4
  - R1-m5
  - R1-m6

- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5

- **Assessment against Nature-style criteria** 
  - Originality: The question of time rescaling transferability in coarse-grained condensate simulations has not been systematically addressed before. The correlation with interaction energy is a novel contribution.
  - Scientific importance: The findings have direct implications for the interpretation of a large body of coarse-grained simulation studies of condensates. The demonstration that equilibrium validation is insufficient for dynamical predictions is an important cautionary result.
  - Interdisciplinary readership: The work bridges computational biophysics, physical chemistry of phase separation, and experimental single-molecule biophysics. The conceptual framework connecting coarse-graining to friction and memory effects will be accessible to a broad readership.
  - Technical soundness: The equilibrium validation is thorough. The dynamical analysis is mostly sound, but several technical concerns (detailed above) need to be addressed to fully establish the central claims.
  - Readability for nonspecialists: The manuscript is clearly written, with appropriate context provided for the methods and concepts. The figures are informative and well labeled.

- **Recommendation posture** Supportive if technical concerns are resolved. The central claims are plausible and important, but the current evidence base has gaps that need to be addressed before the case is fully established.

## Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of dynamical measurements
- **Claim pointer** The authors claim that the time rescaling factor required to reproduce experimental reconfiguration times differs by approximately an order of magnitude between isolated ProTα and the dense phase, and that this difference persists across a wide range of friction coefficients.
- **Evidence pointer** Section III.D, Fig. 4(a), Fig. 5(d)-5(e)
- **Concern** The reconfiguration time is calculated from the distance correlation function between labeled residues. The authors state that the dye-dye distance in dense-phase simulations is calculated using an implicit treatment with a scaling exponent of 0.6, and they validate this with one representative explicit-dye simulation. However, the accuracy of this approximation for the dynamics, as opposed to the equilibrium average, is not established. The distance correlation function is sensitive to the local dynamics of the dye attachment points, and an implicit treatment that reproduces the mean distance may not reproduce the correlation function. The single explicit-dye simulation is described as yielding a consistent mean FRET efficiency, but no comparison of the correlation function or reconfiguration time is provided. This is a critical validation step, as the central claim of the paper rests on the accuracy of the reconfiguration time measurements.
- **Why it matters** If the implicit dye treatment systematically biases the reconfiguration time in the dense phase, the reported time rescaling factors for the dense phase could be incorrect, potentially affecting the conclusion that time rescaling is not transferable between dilute and dense phases.
- **Resolution test** Provide a direct comparison of the distance correlation function and the resulting reconfiguration time between the implicit and explicit dye treatments in the dense phase, over a range of ionic strengths. If the implicit treatment is shown to be accurate for the dynamics, this concern is resolved. Alternatively, use the explicit dye treatment for all dense-phase reconfiguration time calculations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical robustness of key comparisons
- **Claim pointer** The authors claim that the time rescaling factors differ between lysine-rich and arginine-rich coacervates, with arginine-rich systems requiring factors at least threefold greater.
- **Evidence pointer** Section III.D, Fig. 4(d)-4(f)
- **Concern** The comparison between lysine-rich and arginine-rich systems is based on the time rescaling factors required to match experimental reconfiguration times. The uncertainty in these factors is not fully characterized. The reconfiguration time is calculated from a correlation function, and the statistical uncertainty in this quantity depends on the number of independent reconfiguration events sampled. The authors report standard deviations across chains, but this does not capture the statistical uncertainty in the correlation function itself. Additionally, the experimental reconfiguration times have their own uncertainties, which are not propagated into the rescaling factor comparison. Without a proper error analysis, it is unclear whether the reported threefold difference between lysine-rich and arginine-rich systems is statistically significant.
- **Why it matters** The claim that time rescaling depends on residue chemistry is a key finding of the paper. If the difference is not statistically robust, the conclusion would be weakened.
- **Resolution test** Provide a bootstrap or block-averaging analysis of the reconfiguration time for each system, and propagate the experimental uncertainties into the rescaling factor comparison. Report confidence intervals for the rescaling factors and demonstrate that the lysine-arginine difference is significant.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of the friction coefficient dependence
- **Claim pointer** The authors claim that varying the Langevin friction coefficient does not improve the transferability of the time mapping across systems, and that the system-dependent differences persist over the whole range of friction.
- **Evidence pointer** Section III.D, Fig. 5(d)-5(e)
- **Concern** The authors vary the friction coefficient over a wide range and show that the time rescaling factors remain system-dependent. However, the interpretation of this result is not fully developed. The friction coefficient in Langevin dynamics serves both as a thermostat coupling and as a proxy for solvent viscosity. At very low friction, the dynamics approach the inertial limit, where the system may not be in the overdamped regime relevant to solution conditions. At very high friction, the dynamics become increasingly slow, and the simulation time required to sample reconfiguration events becomes prohibitive. The authors show that the rescaling factors follow an empirical shifted inverse function, but the physical meaning of the parameters in this function is not discussed. More importantly, the claim that "adjusting a single uniform Langevin friction coefficient cannot improve transferability" is only demonstrated for the specific range of friction coefficients tested. It is possible that an intermediate value, not tested, could reduce the differences.
- **Why it matters** The conclusion that time rescaling is fundamentally system-dependent, rather than an artifact of the chosen friction coefficient, is central to the paper. If the range of friction coefficients tested is insufficient to support this claim, the conclusion would be weakened.
- **Resolution test** Provide a more systematic exploration of the friction coefficient, including values closer to the overdamped limit, and demonstrate that the rescaling factors do not converge to a common value. Additionally, discuss the physical interpretation of the empirical fit parameters and how they relate to the underlying dynamics.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability of the correlation between time rescaling and interaction energy
- **Claim pointer** The authors claim that the time rescaling factor correlates with the mean non-bonded interaction energy per chain, suggesting that missing frictional effects arise from protein-protein interactions.
- **Evidence pointer** Section III.D, Fig. 5(f)
- **Concern** The correlation in Fig. 5(f) is based on four data points, one for each coacervate system. With only four points, the correlation is not statistically robust, and the apparent linear relationship on a log scale could be coincidental. Furthermore, the interaction energy is a mean quantity that does not capture the distribution of interaction strengths or the dynamics of contact formation and breaking. The authors acknowledge that the correlation is phenomenological, but the claim that it suggests a mechanistic link between interaction energy and friction is speculative. A more direct test would be to vary the interaction strength systematically within a single system, for example by mutating specific residues, and show that the time rescaling factor changes accordingly.
- **Why it matters** The correlation with interaction energy is presented as a potential predictive framework for estimating time rescaling factors. If the correlation is not robust, this framework would be unreliable.
- **Resolution test** Provide additional data points, either by simulating additional coacervate systems or by varying interaction parameters within a single system, to strengthen the correlation. Alternatively, present the correlation as a hypothesis requiring further testing, rather than a finding.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Completeness of the comparison with all-atom simulations
- **Claim pointer** The authors compare their coarse-grained results with all-atom simulations for the protamine-ProTα condensate, noting that the dense-phase concentration is higher than experimentally observed but comparable to all-atom results.
- **Evidence pointer** Section III.A, Fig. 1(d)
- **Concern** The comparison with all-atom simulations is mentioned only briefly and for a single system. The authors do not discuss whether the all-atom simulations also reproduce the experimental reconfiguration times, or whether the time rescaling factors for the coarse-grained model are consistent with the all-atom dynamics. A more detailed comparison would help establish whether the observed time rescaling is a general feature of coarse-grained models or specific to the HPS model used here.
- **Why it matters** The paper aims to draw general conclusions about coarse-grained simulations of condensates. A more thorough comparison with all-atom simulations would strengthen the generalizability of the findings.
- **Resolution test** Provide a more detailed comparison with all-atom simulations, including reconfiguration times and diffusion coefficients, if available. If such data are not available, explicitly state this limitation and discuss its implications for the generalizability of the conclusions.

## Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Methods section, friction coefficient
- **Evidence pointer** Section II, Models and Methods
- **Issue** The choice of the production friction coefficient of 0.2 ps⁻¹ is justified only by reference to previous work. The authors do not discuss whether this value is appropriate for the systems studied, or whether the results depend on this choice beyond the explicit test shown in Fig. 5.
- **Required correction** Add a brief discussion of the rationale for the production friction coefficient and its relationship to the physical solvent viscosity.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Fig. 4 and Fig. 5
- **Evidence pointer** Section III.D
- **Issue** The error bars in Figs. 4 and 5 are described as standard deviations across chains, but the number of chains and the number of independent samples per chain are not reported.
- **Required correction** Report the number of chains and the effective number of independent samples used for each reported quantity.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of the Kramers-like model
- **Affected element** Section III.D, Fig. 5(f)
- **Evidence pointer** Section III.D
- **Issue** The Kramers-like interpretation is introduced briefly and the connection between the interaction energy and the barrier height is not developed. The authors state that the correlation should not be interpreted as implying that the total interaction energy constitutes the barrier, but the alternative interpretation is not discussed in detail.
- **Required correction** Expand the discussion of the Kramers-like model, including the assumptions and limitations of this interpretation.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness of the supplementary material
- **Affected element** Supplementary material
- **Evidence pointer** Supplementary Material section
- **Issue** The supplementary material is described as containing Table S1 and Figs. S1 and S2, but the full content is not provided in the submitted text. The authors reference additional analyses that are not described in the main text.
- **Required correction** Ensure that the supplementary material is complete and that all referenced analyses are described in sufficient detail.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity of the observable dependence claim
- **Affected element** Section III.D
- **Evidence pointer** Section III.D, Fig. 4
- **Issue** The claim that time rescaling may be observable-dependent is based on the comparison between reconfiguration times and diffusion coefficients. However, the diffusion coefficients are described as having large uncertainties, and the comparison is not quantified.
- **Required correction** Provide a more quantitative comparison between the time rescaling factors inferred from reconfiguration times and those inferred from diffusion coefficients, including the uncertainties.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Typos and minor errors
- **Affected element** Section IV, Conclusions
- **Evidence pointer** Section IV
- **Issue** The text contains a typo: "analssogous" should be "analogous".
- **Required correction** Correct the typo.

## Risk / unsupported claims
- The claim that time rescaling is not transferable between dense and dilute phases is supported by the data, but the statistical robustness of the comparison is not fully established (R1-M2).
- The claim that the time rescaling factor correlates with the mean non-bonded interaction energy is based on only four data points and should be treated as a hypothesis rather than a robust finding (R1-M4).
- The claim that the implicit dye treatment is accurate for dynamics in the dense phase is not fully validated (R1-M1).
- The claim that varying the Langevin friction coefficient cannot improve transferability is only demonstrated for the specific range tested (R1-M3).
- The generalizability of the findings to other coarse-grained models is not established, as only the HPS model is tested (R1-M5).