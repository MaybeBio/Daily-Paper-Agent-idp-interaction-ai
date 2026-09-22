## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, and supplementary declarations
- **Assessment boundary** Scientific validity, methodological soundness, interpretational accuracy, and alignment with stated claims; limited to content provided in the manuscript
- **Shared manuscript claim summary** The authors present a generalized Rouse model using graph Laplacians derived from lattice-based Metropolis Monte Carlo simulations to compute viscoelastic moduli of biomolecular condensates. They demonstrate that a collective graph incorporating inter-chain contacts reproduces measured moduli better than a single-chain graph, and that a mixture of both graphs captures the full frequency-dependent behavior. They further argue that condensates are best described as generalized Maxwell fluids with a continuous distribution of relaxation times, contrary to recent claims of a single relaxation time.
- **Visible evidence base** Full text including equations, figure descriptions, simulation parameters, and comparison to experimental data from prior work (Alshareedah et al., 2024)
- **Missing materials affecting confidence** Actual figures and numerical data tables are not provided; only figure captions and in-text descriptions are available. Experimental datasets used for comparison are referenced but not included. Code availability is stated but not reviewed.

## Reviewer
- **Overall assessment** This manuscript presents a conceptually interesting and potentially valuable methodological advance for computing viscoelastic properties of biomolecular condensates from equilibrium simulations. The generalization of the Rouse model via graph Laplacians is mathematically sound and the distinction between single-chain and collective graphs is physically motivated. However, the manuscript has several significant limitations that prevent full acceptance in its current form. The validation against experimental data relies on a rescaling procedure that may mask systematic errors, the treatment of the mixture model is somewhat ad hoc, and the claim regarding the continuous distribution of relaxation times, while plausible, is not rigorously established from the provided evidence. The work is likely to be of interest to the condensate biophysics community, but the technical concerns outlined below need to be addressed.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, particularly those interested in material properties and rheology; computational biophysicists developing coarse-grained models for phase-separating systems; experimentalists using microrheology to characterize condensate mechanics. The methodological framework could also be relevant to polymer physics more broadly.
- **Major strengths** The conceptual framing of condensates as generalized Maxwell fluids with continuous relaxation spectra is a useful corrective to oversimplified single-relaxation-time interpretations. The use of graph Laplacians to bridge equilibrium structure and dynamical response is elegant and computationally efficient. The comparison between single-chain and collective graphs provides clear physical insight into the relative contributions of intra- and inter-chain interactions. The authors are appropriately cautious about the limitations of lattice simulations and the need for experimental input for absolute calibration.
- **Major Concerns** 
  - R1-M1: The rescaling procedure used to compare computed and measured moduli may obscure systematic discrepancies. The authors rescale both frequency and modulus values based on a single crossover point, which guarantees agreement at that point but does not validate the overall frequency dependence. A more rigorous approach would involve fitting the friction coefficient and other parameters to minimize global discrepancies, or presenting unscaled comparisons to assess the quality of the model independently.
  - R1-M2: The mixture model in Eq. (17) is introduced somewhat arbitrarily. While the physical rationale (combination of network compliance and chain rigidity) is reasonable, the linear combination form is not derived from any underlying theory. The authors should justify why a linear combination is appropriate, and whether other functional forms (e.g., weighted geometric mean, or a more complex coupling) would give different results. The optimization procedure for determining coefficients a and b is described but the sensitivity of the results to the choice of learning rate, initialization, and convergence criteria is not discussed.
  - R1-M3: The claim that a continuous distribution of relaxation times exists in condensates is presented as a key finding, but the evidence is indirect. The authors infer this from the shape of the computed moduli and the mixture model, but they do not directly demonstrate that the relaxation spectrum h(τ) is continuous rather than discrete. The inversion procedure in Eq. (23) could potentially produce a continuous spectrum even for a system with discrete relaxation times, depending on the regularization. The authors should address this potential artifact.
  - R1-M4: The manuscript does not adequately address the timescale problem in lattice Monte Carlo simulations. The authors acknowledge that lattice simulations lack physical timescales, but the implications for the computed moduli are not fully explored. The rescaling procedure implicitly assumes that the ratio of timescales between different modes is preserved, which may not hold for lattice models with simplified dynamics.
- **Minor Comments**
  - R1-m1: The abstract states that the collective graph reproduces measured moduli "with greater fidelity" than the single-chain graph, but the quantitative degree of improvement is not stated. A numerical measure of agreement (e.g., RMS error) would strengthen this claim.
  - R1-m2: The discussion of the crossover frequency and its relationship to the relaxation spectrum could be clearer. The authors state that the peak in h(τ) corresponds to the crossover time, but the exact relationship is not derived or explained.
  - R1-m3: The manuscript would benefit from a more explicit statement of the limitations of the lattice model, particularly regarding the neglect of hydrodynamic interactions and the simplified treatment of solvent. The authors mention this in the discussion but do not quantify the potential impact on the computed moduli.
  - R1-m4: The reference to "recent assertions" of a single relaxation time (in the abstract and discussion) is vague. The authors should cite the specific work they are responding to and briefly summarize the claim to provide context.
  - R1-m5: The description of the Metropolis Monte Carlo simulation parameters is incomplete. The number of independent runs, the length of equilibration, and the criteria for determining convergence of the phase-separated state are not specified.
- **Technical failings that need to be addressed before the case is established** The rescaling procedure (R1-M1) and the potential artifact in the relaxation spectrum inversion (R1-M3) are the most critical technical issues. Without addressing these, the central claims of the manuscript are not fully supported.
- **Assessment against Nature-style criteria** 
  - Originality: The work is original in its specific application of graph Laplacians to compute viscoelastic moduli of condensates, though the underlying Rouse formalism is well-established. The conceptual framing of generalized Maxwell fluids is not entirely new but is applied here in a novel context.
  - Scientific importance: The work addresses an important gap in the field, namely the connection between equilibrium structure and dynamical material properties of condensates. The potential to extract relaxation spectra from measured moduli has practical implications for interpreting microrheology data.
  - Interdisciplinary readership: The work is primarily of interest to the condensate biophysics community and computational polymer physicists. The level of technical detail may limit broader appeal, though the conceptual messages about viscoelasticity are accessible.
  - Technical soundness: The mathematical framework is sound, but the validation approach and the interpretation of the relaxation spectrum have weaknesses as detailed above.
  - Readability for nonspecialists: The manuscript is generally well-written and the key concepts are explained clearly. However, the technical details of the graph Laplacian construction and the inversion procedure may be challenging for readers without a background in polymer physics or spectral graph theory.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the manuscript addresses an important problem, but the validation methodology and the interpretation of the relaxation spectrum need to be strengthened before the claims can be fully accepted.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation methodology
- **Claim pointer** The authors claim that the collective graph reproduces measured moduli "with greater fidelity" than the single-chain graph, and that the mixture model captures the totality of the measured frequency dependence.
- **Evidence pointer** Section "The collective graph for computing graph Laplacians", Figure 5
- **Concern** The rescaling procedure used to compare computed and measured moduli is based on matching the crossover frequency and the modulus value at that frequency. This guarantees agreement at the crossover point but does not validate the overall frequency dependence. The authors do not provide any quantitative measure of agreement (e.g., RMS error, chi-squared statistic) across the full frequency range. Moreover, the rescaling implicitly assumes that the lattice model correctly captures the relative timescales of different modes, which is not established.
- **Why it matters** The central claim of the manuscript is that the collective graph and the mixture model can reproduce experimental measurements. If the rescaling procedure masks systematic discrepancies in the frequency dependence, the validation is not meaningful. The reader cannot assess whether the model is genuinely predictive or merely fitted to a single point.
- **Resolution test** The authors should present unscaled comparisons of computed and measured moduli, or use a more rigorous fitting procedure that minimizes the global discrepancy across the entire frequency range. They should also report quantitative measures of agreement (e.g., RMS error, coefficient of determination) for both the single-chain and collective graphs, and for the mixture model.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Model formulation
- **Claim pointer** The authors propose a mixture model where the measured storage modulus is a linear combination of the storage moduli from the collective and single-chain models, with coefficients a and b satisfying a + b = 1.
- **Evidence pointer** Section "Mixture of graphs", Equation (17)
- **Concern** The linear combination form of the mixture model is introduced without derivation or justification from underlying physics. While the physical rationale (combination of network compliance and chain rigidity) is plausible, it is not clear why a linear combination is the appropriate functional form. Other possibilities, such as a weighted geometric mean or a more complex coupling between modes, could give different results. The optimization procedure for determining a and b is described, but the sensitivity of the results to the choice of learning rate, initialization, and convergence criteria is not discussed.
- **Why it matters** The mixture model is used to explain the discrepancy between the collective graph and the experimental data at low frequencies. If the model form is arbitrary, the physical interpretation (that both inter-chain and intra-chain contributions matter) is not strongly supported. The reader cannot assess whether the mixture model is a genuine physical description or a phenomenological fit.
- **Resolution test** The authors should provide a derivation or physical justification for the linear combination form, or test alternative functional forms and show that the results are robust. They should also report the sensitivity of the fitted coefficients to the optimization parameters.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of relaxation spectrum
- **Claim pointer** The authors state that "a continuous distribution of relaxation times exists in condensates" and that this is in line with the theory of Rouse and contrary to recent assertions of a single relaxation time.
- **Evidence pointer** Section "Spectrum of relaxation times", Figure 6
- **Concern** The claim of a continuous distribution of relaxation times is inferred from the shape of the computed moduli and the mixture model, but the evidence is indirect. The inversion procedure in Eq. (23) uses Tikhonov regularization, which can produce a continuous spectrum even for a system with discrete relaxation times, depending on the regularization parameter. The authors do not demonstrate that the inferred spectrum is truly continuous rather than a smoothed representation of a discrete set of modes. Moreover, the relationship between the peak in h(τ) and the crossover frequency is stated but not derived.
- **Why it matters** The claim about the continuous distribution of relaxation times is a key conceptual point of the manuscript, as it directly contradicts prior work. If this claim is not rigorously established, the manuscript's contribution is weakened.
- **Resolution test** The authors should test the inversion procedure on synthetic data with known discrete relaxation times and show that the method can distinguish between discrete and continuous spectra. They should also provide a more rigorous analysis of the relationship between the relaxation spectrum and the crossover frequency.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Timescale mapping
- **Claim pointer** The authors state that the rescaling procedure based on the crossover frequency is "more than sufficient to put the computed moduli on realistic time and energy scales."
- **Evidence pointer** Section "Discussion"
- **Concern** The lattice Monte Carlo simulations do not have a direct mapping to physical timescales. The rescaling procedure assumes that the ratio of timescales between different modes is preserved between the lattice model and the real system, but this is not justified. The dynamics of lattice models can differ significantly from continuum models, particularly for collective motions involving many monomers.
- **Why it matters** The quantitative values of the computed moduli depend on the timescale mapping. If the mapping is not reliable, the comparison with experimental data is not meaningful, even after rescaling.
- **Resolution test** The authors should discuss the limitations of the timescale mapping more explicitly and, if possible, validate the mapping against a system where both lattice and continuum dynamics are known.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Quantitative reporting
- **Affected element** Abstract and Section "The collective graph for computing graph Laplacians"
- **Evidence pointer** Abstract, Figure 5
- **Issue** The claim that the collective graph reproduces measured moduli "with greater fidelity" is not quantified. The reader cannot assess the degree of improvement.
- **Required correction** Provide a quantitative measure of agreement (e.g., RMS error, chi-squared statistic) for both the single-chain and collective graphs.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Section "Spectrum of relaxation times"
- **Evidence pointer** Figure 6
- **Issue** The relationship between the peak in the relaxation spectrum h(τ) and the crossover frequency is stated but not explained. The reader is left to infer the connection.
- **Required correction** Provide a brief derivation or explanation of why the peak in h(τ) corresponds to the crossover time.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Section "MMC simulations"
- **Evidence pointer** Section "MMC simulations"
- **Issue** The simulation parameters are not fully specified. The number of independent runs, the length of equilibration, and the criteria for determining convergence of the phase-separated state are not given.
- **Required correction** Provide complete simulation parameters, including the number of independent runs, equilibration time, and convergence criteria.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Contextualization
- **Affected element** Abstract and Discussion
- **Evidence pointer** Abstract, Discussion
- **Issue** The reference to "recent assertions" of a single relaxation time is vague. The reader is not told which work is being referred to or what the specific claim was.
- **Required correction** Cite the specific work and briefly summarize the claim to provide context for the reader.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Data Availability section
- **Evidence pointer** Data Availability section
- **Issue** The data availability statement says that data are available from the corresponding author upon reasonable request, but the code is available on GitHub. It is not clear whether the simulation trajectories and analysis scripts are also available.
- **Required correction** Clarify what data and code are available and under what conditions.

## Risk / unsupported claims
- The claim that a continuous distribution of relaxation times exists in condensates is not rigorously established from the provided evidence, as the inversion procedure may produce a continuous spectrum even for discrete relaxation times.
- The claim that the mixture model captures the "totality" of the measured frequency dependence is not quantitatively supported, as no measure of agreement is provided.
- The statement that the rescaling procedure is "more than sufficient" to put computed moduli on realistic scales is not justified, as the timescale mapping from lattice simulations to physical systems is not validated.
- The assertion that the collective graph reproduces measured moduli "with greater fidelity" is not quantified and cannot be assessed from the provided information.