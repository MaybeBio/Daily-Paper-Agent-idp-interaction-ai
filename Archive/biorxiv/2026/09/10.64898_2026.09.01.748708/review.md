## Review setup
- **Input scope** Full manuscript (abstract, introduction, methods, results, discussion, conclusions, supplementary materials referenced)
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the manuscript
- **Shared manuscript claim summary** The authors test whether a residue-level coarse-grained (CG) model that reproduces equilibrium phase behavior of complex coacervates also preserves a transferable timescale for conformational dynamics. They find that time rescaling is not transferable between dense and dilute phases, across condensate compositions, or between different dynamical observables, and that the required rescaling correlates with the total non-bonded interaction energy of the protein chains.
- **Visible evidence base** Abstract, Introduction, Models and Methods, Results and Discussion (Sections III.A–III.D), Conclusions, Supplementary Materials (Table S1, Figs. S1–S2)
- **Missing materials affecting confidence** Supplementary figures S1 and S2 are referenced but not provided in the submitted material. The raw simulation trajectories, force field parameter files, and analysis scripts are not provided. Experimental data used for comparison are cited but not included.

## Reviewer
- **Overall assessment** This manuscript presents a systematic and well-motivated investigation of the limitations of time rescaling in residue-level coarse-grained simulations of biomolecular condensates. The authors demonstrate that while the HPS CG model reproduces equilibrium properties (dense-phase concentrations, chain dimensions, FRET efficiencies) across four complex coacervate systems, the dynamical time rescaling required to match experimental reconfiguration times is system-dependent, environment-dependent, and potentially observable-dependent. The correlation between the time-rescaling factor and the total non-bonded interaction energy provides a physically plausible explanation. The work is timely and addresses an important gap in the field, as most CG condensate studies focus on equilibrium validation without critically examining dynamical fidelity. However, several technical aspects require clarification or additional analysis before the central claims can be fully established.
- **Who would be interested in the results, and why** Researchers in computational biophysics, particularly those developing or using coarse-grained models for intrinsically disordered proteins and biomolecular condensates. The findings are also relevant to experimentalists using single-molecule FRET and fluorescence correlation spectroscopy to study condensate dynamics, as the work provides a framework for interpreting CG simulation timescales. The conceptual connection to polymer physics and generalized Langevin dynamics will interest theorists working on coarse-graining methodologies.
- **Major strengths** 1. The study addresses a critical and underappreciated issue: whether equilibrium validation of CG models implies dynamical accuracy. 2. The experimental comparison is comprehensive, covering four condensate systems with distinct cationic partners, multiple ionic strengths, and two dynamical observables (reconfiguration time and diffusion coefficient). 3. The systematic variation of the Langevin friction coefficient over five orders of magnitude is a rigorous test of whether a single friction parameter can resolve the non-transferability. 4. The correlation between time-rescaling factors and interaction energies provides a physically interpretable, potentially predictive relationship.
- **Major Concerns** R1-M1, R1-M2, R1-M3, R1-M4
- **Minor Comments** R1-m1, R1-m2, R1-m3, R1-m4
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: High. While the general idea that CG models require time rescaling is known, the systematic demonstration across multiple condensate systems and the correlation with interaction energy are novel. Scientific importance: High. The work directly challenges the common practice of applying a single global time-rescaling factor in CG condensate simulations and provides a framework for more rigorous dynamical interpretation. Interdisciplinary readership: Moderate. The manuscript is written for a specialized biophysics audience; the conceptual framework connecting to polymer physics and generalized Langevin dynamics broadens its appeal. Technical soundness: Moderate. The simulation methodology is appropriate, but several technical concerns (friction coefficient choice, diffusion analysis, dilute-phase statistics) require clarification. Readability for nonspecialists: Moderate. The introduction and conclusions are accessible, but the methods and results sections assume familiarity with CG simulation techniques and Langevin dynamics.
- **Recommendation posture** Supportive if technical concerns are resolved

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodology / Data analysis
- **Claim pointer** The authors claim that the time-rescaling factor for chain reconfiguration is not transferable between dense and dilute phases, across condensate compositions, and may be observable-dependent.
- **Evidence pointer** Section III.D, Figures 4 and 5
- **Concern** The time-rescaling factors are calculated using a single Langevin friction coefficient of γ = 0.2 ps⁻¹, which the authors acknowledge is far from the physically motivated Stokes estimate of ~30 ps⁻¹. While the authors test the dependence on γ (Figure 5), the production simulations use γ = 0.2 ps⁻¹. The choice of this specific value is justified only by common usage in the field ("to accelerate sampling and improve sampling efficiency"). The authors show that varying γ does not eliminate system-dependent differences in time rescaling, but the absolute values of the rescaling factors and their ratios depend on γ. The claim of non-transferability is robust, but the quantitative rescaling factors reported (30, 170, 300 for monomer, dimer, dense phase) are specific to this friction coefficient and may not be directly comparable to other CG studies using different γ values.
- **Why it matters** The quantitative rescaling factors are the primary output of the dynamical analysis. If these values are artifacts of the chosen friction coefficient, their physical interpretation (e.g., the correlation with interaction energy in Figure 5f) may be compromised. The field needs guidance on whether rescaling factors from different CG studies are comparable.
- **Resolution test** The authors should provide a clear statement that the rescaling factors are conditional on γ = 0.2 ps⁻¹. They should also show, perhaps in a supplementary figure, how the rescaling factors for all four condensates and the dilute-phase systems vary with γ, not just the H1–ProTα system shown in Figure 5d–e. This would demonstrate whether the relative ordering of rescaling factors (e.g., protamine > H1) is robust across friction coefficients.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Data analysis / Statistical rigor
- **Claim pointer** The authors claim that the time-rescaling factors inferred from diffusion coefficients are approximately 1.5- to 5-fold smaller than those from reconfiguration times, suggesting possible observable dependence.
- **Evidence pointer** Section III.D, Figure S2 (not provided)
- **Concern** The diffusion coefficient analysis is described only briefly, and the key evidence (Figure S2) is not provided in the submitted material. The authors acknowledge substantial statistical and systematic uncertainties in the diffusion estimates, including chain-to-chain variation, finite-size effects, and slab geometry artifacts. Without seeing the actual data, it is impossible to assess whether the observed discrepancy between rescaling factors from reconfiguration and diffusion is statistically significant or within the noise. The authors themselves state that "the present data do not allow us to unequivocally attribute the discrepancy to the intrinsic observable dependence." This claim is therefore currently unsupported.
- **Why it matters** The claim of observable-dependent time rescaling is a significant finding with implications for how CG simulations should be calibrated. If this claim is not robust, the paper's conclusions should be tempered accordingly.
- **Resolution test** Provide Figure S2 and a more detailed analysis of the diffusion coefficient uncertainties. The authors should perform a statistical test (e.g., a bootstrap or jackknife analysis across chains) to determine whether the rescaling factors from reconfiguration and diffusion are significantly different for each condensate. If the uncertainties are too large to draw conclusions, this should be stated explicitly and the claim of observable dependence should be downgraded to a speculation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodology / Validation
- **Claim pointer** The authors claim that the CG simulations reproduce experimentally measured FRET efficiencies for ProTα in the dense phase.
- **Evidence pointer** Section III.C, Figure 3c–f
- **Concern** The dense-phase FRET efficiencies are calculated using an implicit-dye approximation (scaling the Cα distance by a factor based on sequence separation). The authors validate this approximation with a single explicit-dye simulation for the H1–ProTα condensate at one ionic strength (Figure 3c). However, the implicit-dye approximation is used for all other dense-phase systems and ionic strengths. The validation is insufficient: (1) only one condensate composition is tested; (2) only one ionic strength is tested; (3) the agreement between implicit and explicit methods is shown as a single data point, not a statistical comparison. The implicit-dye approximation may introduce systematic errors that vary with condensate composition or ionic strength, potentially affecting the comparison with experimental FRET data.
- **Why it matters** The FRET efficiency comparison is a key validation of the CG model's equilibrium conformational ensembles. If the implicit-dye approximation introduces systematic errors, the conclusion that the CG model reproduces experimental chain dimensions in the dense phase may be weakened.
- **Resolution test** Perform explicit-dye simulations for at least one additional condensate (e.g., protamine–ProTα) at one ionic strength to demonstrate that the implicit approximation holds across compositions. Alternatively, provide a more rigorous justification for the scaling factor used in the implicit approximation, including error estimates from the explicit-dye simulation.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation / Generalizability
- **Claim pointer** The authors claim that the correlation between the time-rescaling factor and the total non-bonded interaction energy (Figure 5f) suggests that missing frictional effects arise from protein-protein interactions rather than solely from protein-solvent interactions.
- **Evidence pointer** Section III.D, Figure 5f
- **Concern** The correlation in Figure 5f is based on only six data points (monomer, dimer, and four condensates). The approximately linear relationship on a log-linear scale is suggestive but not statistically robust. The authors interpret this correlation within a Kramers-like barrier-crossing picture, but they acknowledge that ⟨E_int⟩ is an equilibrium interaction energy, not an activation free energy. The mechanistic link between the total interaction energy and the effective friction from missing degrees of freedom is not established. The correlation could be coincidental or driven by a third variable (e.g., chain density, which correlates with both interaction energy and dynamics).
- **Why it matters** The correlation is presented as a key finding that provides a physical explanation for the system-dependent time rescaling. If the correlation is weak or confounded, the mechanistic interpretation is speculative.
- **Resolution test** The authors should (1) report the correlation coefficient and p-value for the relationship in Figure 5f; (2) test whether the correlation persists when controlling for dense-phase concentration or chain density; (3) discuss alternative interpretations, such as the possibility that the correlation reflects the density-dependence of friction rather than a direct energetic effect.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity / Presentation
- **Affected element** Section III.D, Figure 4a
- **Evidence pointer** Location not provided
- **Issue** The time-rescaling factors for monomeric ProTα (30), H1–ProTα dimer (170), and dense phase (300) are reported in the text but are not labeled directly on Figure 4a. The figure shows the reconfiguration times, not the rescaling factors.
- **Required correction** Add the rescaling factor values to the figure or figure legend, or provide a separate panel showing the rescaling factors explicitly.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodology / Reporting
- **Affected element** Section II (Models and Methods)
- **Evidence pointer** Location not provided
- **Issue** The method for calculating the chain reconfiguration time (τ_r) from the distance correlation function is described only by reference to equations 7-9, but these equations are not explicitly shown in the manuscript. The reader must infer the exact definition from the text.
- **Required correction** Include the explicit equations for the distance correlation function and the fitting procedure used to extract τ_r, either in the main text or in a supplementary methods section.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Section III.B, Figure 2
- **Evidence pointer** Location not provided
- **Issue** The dilute-phase concentrations are reported with large uncertainties, and the authors state that the uncertainty ranges "generally encompassed the corresponding experimental dilute-phase concentrations." However, the figure does not show the experimental dilute-phase concentrations for comparison, only the simulated values.
- **Required correction** Add the experimental dilute-phase concentration data to Figure 2c–f, or provide a supplementary table comparing simulated and experimental values.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity / Terminology
- **Affected element** Section IV (Conclusions)
- **Evidence pointer** Location not provided
- **Issue** The phrase "analssogous coarse-graining" appears to be a typographical error.
- **Required correction** Correct to "analogous coarse-graining."

## Risk / unsupported claims
- The claim of observable-dependent time rescaling (reconfiguration vs. diffusion) is unsupported because the key evidence (Figure S2) is not provided and the authors acknowledge large uncertainties.
- The claim that the correlation between time-rescaling factor and interaction energy (Figure 5f) implies that missing frictional effects arise from protein-protein interactions is plausible but not rigorously established; alternative interpretations (e.g., density-dependent friction) are not ruled out.
- The claim that the CG simulations reproduce dilute-phase concentrations is weakly supported due to large statistical uncertainties; the statement that uncertainty ranges "generally encompassed" experimental values is qualitative.