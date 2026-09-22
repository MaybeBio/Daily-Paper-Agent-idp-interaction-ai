## Review setup
- **Input scope** Full manuscript text (abstract, introduction, model development, linear stability analysis, results for local and non-local elasticity, conclusions, data availability statement)
- **Assessment boundary** Scientific and technical evaluation of the modelling framework, analysis methods, results, and claims as presented in the provided manuscript text. Figures referenced but not provided in full detail.
- **Shared manuscript claim summary** The authors develop a 1D poromechanical phase-field model coupling phase separation to non-local elasticity via large-deformation poroelasticity. They claim that non-local elasticity arrests coarsening and produces patterned domains with a well-defined length scale that decreases with increasing stiffness, whereas local elasticity only inhibits phase separation and affects domain count without suppressing coarsening.
- **Visible evidence base** Linear stability analysis (dispersion relation, eqn 16), numerical simulations (described in Sections 4 and 5), phase diagrams (Fig. 3, Fig. 5), simulation snapshots (Fig. 6, Fig. 7), quantitative analysis of domain size (Fig. 8), energy analysis (Appendix C, referenced)
- **Missing materials affecting confidence** Figures are referenced but not fully visible in the provided text. Appendix A (derivation of non-local stress equations) and Appendix C (energy analysis) are referenced but not provided. Details of numerical discretisation, convergence testing, and parameter values used in simulations are not fully specified.

## Reviewer
- **Overall assessment** This manuscript presents a timely and relevant extension of equilibrium theories of phase separation in elastic networks to a dynamic, large-deformation poroelastic framework. The central claim that non-local elasticity arrests coarsening and produces patterned states is physically plausible and supported by the presented linear stability analysis and simulation results. However, the manuscript has several technical gaps that need to be addressed before the case is fully established, particularly regarding the derivation of the non-local stress law, the numerical methods, and the quantitative comparison to previous equilibrium predictions. The work is likely to be of interest to the soft matter and biophysics communities, but the current evidence base is incomplete in several respects.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates and their interaction with the cytoskeleton, experimentalists working on phase separation in polymer gels, and theorists developing models of mechanochemical pattern formation. The framework could also be relevant to those studying gas bubble formation in soft geological materials and structural colouration in biological tissues.

- **Major strengths**
  1. The manuscript addresses a significant open problem: the dynamic mechanism underlying pattern formation in phase-separating systems coupled to elastic networks.
  2. The use of a large-deformation poroelastic framework is a methodological advance over previous linearised or equilibrium approaches.
  3. The combination of linear stability analysis and numerical simulation provides complementary evidence for the central claims.
  4. The identification of distinct instability regimes (classical vs. patterned spinodal) is a useful conceptual contribution.
  5. The authors are transparent about limitations (1D model, unclear microscopic interpretation of non-locality length).

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The non-local stress law (eqn 11-13) is derived from the non-local energy functional (eqn 4), and the manuscript claims this captures non-local elastic effects arising from network heterogeneities.
- **Evidence pointer** Section 2.4, eqn 11-13, Appendix A (referenced but not provided)
- **Concern** The derivation of the non-local stress law is not fully presented in the main text. The manuscript states that "a detailed derivation of these equations is provided in Appendix A," but this appendix is not included in the provided material. The physical interpretation of the non-local stress terms σ′ and σ* is unclear, and it is not obvious that the chosen convolution kernel (exponential) is justified beyond mathematical convenience. The relationship between the non-locality length ξ and the "characteristic pore size" mentioned in the abstract is not established.
- **Why it matters** The non-local stress law is the central novel ingredient of the model. If the derivation is flawed or the physical basis is not adequately justified, the main conclusions about arrested coarsening would be undermined. Readers need to be able to assess the validity of this constitutive choice.
- **Resolution test** Provide the full derivation in the main text or a supplementary appendix that is accessible. Justify the choice of kernel and discuss its physical interpretation. Show that the non-local stress law reduces to the local limit correctly and satisfies relevant thermodynamic consistency conditions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that "non-local elasticity arrests coarsening to form patterned domains with a well-defined length scale that decreases with increasing stiffness" (abstract and Section 5.2).
- **Evidence pointer** Section 5.2, Fig. 6, Fig. 7, Fig. 8
- **Concern** The evidence for arrested coarsening is based on simulations run to a fixed end time t_end. The manuscript states that "coarsening is exponentially slow in 1D" for the local case, and that for non-local cases "a regular periodic, or patterned, state at t = t_end, which does not evolve further with time." However, it is not demonstrated that the patterned state is a true steady state rather than a transient state that would coarsen on much longer timescales. The energy analysis in Appendix C (referenced but not provided) is said to show that energy reaches a constant value, but this is not visible. The distinction between "arrested coarsening" and "exponentially slow coarsening" is critical and needs stronger evidence.
- **Why it matters** The central claim of the paper is that non-local elasticity arrests coarsening. If the observed pattern is merely a very slow transient, the conclusion would be qualitatively different. The timescale of the simulations relative to the characteristic coarsening timescale needs to be established.
- **Resolution test** Show that the patterned state persists for simulation times significantly longer than the characteristic coarsening timescale of the local system. Provide convergence tests with respect to t_end. Present the energy as a function of time showing a clear plateau. If possible, demonstrate that the patterned state is a local minimum of the free energy landscape.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that the model "paves the way for quantitative comparisons between simulations and experiments" (abstract and Section 6).
- **Evidence pointer** Abstract, Section 6
- **Concern** The manuscript does not provide a clear pathway for quantitative comparison with experiments. The model is 1D, which limits direct comparison to 2D/3D experimental systems. The parameters (G, K, χ, ξ, κ) are not mapped to experimentally measurable quantities. The strain-stiffening rheology mentioned in the abstract is not actually implemented in the model (the model uses Neo-Hookean elasticity). The claim about quantitative comparison appears overstated given the current state of the model.
- **Why it matters** The stated significance of the work depends partly on its potential for experimental comparison. If this pathway is not credible, the impact of the work is reduced.
- **Resolution test** Provide a more concrete discussion of how model parameters could be estimated from experiments, or acknowledge more explicitly the gap between the 1D model and experimental systems. If strain-stiffening is mentioned as a future direction, clarify that it is not part of the current model.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The manuscript states that "in the limit of zero non-locality length ξ = 0, we recover the local Neo-Hookean stress σ = G(J − 1/J) + K(J − 1)" (Section 2.4).
- **Evidence pointer** Section 2.4, eqn 11-13
- **Concern** The recovery of the local limit is stated but not demonstrated. It is not clear from the presented equations how the non-local terms σ′ and σ* reduce to the local expression when ξ → 0. The convolution kernel gξ = exp(−|X|/ξ)/2ξ becomes a delta function in this limit, but the differential equations (eqn 12-13) may have a singular limit that requires careful treatment.
- **Why it matters** The local limit is used as a benchmark for comparison (Section 4). If the limit is not correctly recovered, the comparison between local and non-local cases would be invalid.
- **Resolution test** Show explicitly how eqn 11 reduces to the local Neo-Hookean stress when ξ → 0. Discuss any subtleties in taking this limit.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section 2.5 (Model summary and non-dimensionalisation)
- **Evidence pointer** Section 2.5
- **Issue** The non-dimensionalisation is presented briefly, and the definitions of the dimensionless variables are not fully explicit. The text states "Non-dimensionalising our model by length scale , time scale κν/ΛkBT, and stress scale kBT/ν motivates introducing the dimensionless variables , , and ℓ2 = ξ2/κ" but the actual definitions of the dimensionless variables are not clearly written out (likely due to formatting issues in the provided text).
- **Required correction** Clearly define all dimensionless variables and state the resulting non-dimensionalised equations.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section 3 (Linear stability analysis)
- **Evidence pointer** Section 3, eqn 14-16
- **Issue** The linear stability analysis is presented for a 1D system, but the boundary conditions are not specified. The manuscript mentions periodic boundary conditions in Section 2.3, but it is not clear if these are used throughout the analysis and simulations.
- **Required correction** State the boundary conditions explicitly for both the linear stability analysis and the numerical simulations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section 5.2 (Non-local elasticity leads to arrested coarsening)
- **Evidence pointer** Section 5.2, Fig. 8
- **Issue** The definition of the pattern length scale L_patt is given, but the method for extracting it from simulations is described only briefly ("identifying droplet interfaces via a threshold value ϕn = 0.5, and then measuring the mean distance between consecutive interfaces of the same type"). The robustness of this method to the choice of threshold is not discussed.
- **Required correction** Provide more detail on the pattern length scale extraction method and discuss sensitivity to the threshold choice.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Section 6 (Conclusions)
- **Evidence pointer** Section 6
- **Issue** The discussion of connections to other studies is brief. The manuscript mentions the work of Oudich et al. and Qiang et al., but does not discuss how the present results compare quantitatively or qualitatively to these works in detail.
- **Required correction** Expand the discussion to include a more detailed comparison with previous theoretical and experimental results.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section 2.2 (Free energy)
- **Evidence pointer** Section 2.2, eqn 1-2
- **Issue** The free energy functional is presented, but the derivation of the chemical potential (eqn 9) is not shown. The relationship between the chemical potential and the stress tensor is not fully explained.
- **Required correction** Provide the derivation of the chemical potential and clarify the relationship between chemical and mechanical driving forces in the flux expression (eqn 8).

## Risk / unsupported claims
- The claim that "non-local elasticity arrests coarsening" is not fully established from the provided evidence, as the distinction between true arrest and exponentially slow coarsening is not demonstrated with sufficient rigour.
- The claim that the model "paves the way for quantitative comparisons between simulations and experiments" is not supported by the current manuscript, as no concrete pathway for such comparison is provided.
- The physical interpretation of the non-locality length ξ and its relationship to pore size is stated but not justified.
- The claim that the model "extends the equilibrium theory of Qiang et al." is plausible but the specific novel contributions beyond the equilibrium theory are not clearly delineated.
- The behaviour of the model for very large or very small values of the non-locality length ℓ is not systematically explored, limiting the generality of the conclusions.
- The numerical methods are not described in sufficient detail to assess convergence, accuracy, or reproducibility (beyond the data availability statement).