## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and data availability statements.
- **Assessment boundary** Scientific content, methodological soundness, validity of claims relative to presented evidence, and alignment with Nature-style criteria. Editorial and formatting issues are noted only where they affect scientific comprehension.
- **Shared manuscript claim summary** The authors develop a desolvation-aware implicit-solvent coarse-grained (CG) model for biomolecular liquid-liquid phase separation (LLPS) by incorporating residue-level desolvation barriers and solvent-separated minima into pairwise interaction potentials. They report that these terms reshape phase diagrams, reduce dense-phase overcompaction, alter conformational distributions, slow early density-fluctuation growth, shorten transient kinetic arrest, and modulate chain mobility within condensates. They further propose a linear correlation between the temperature gap from the critical point and conformational expansion upon phase separation, supported by theoretical analysis. A parameterization strategy combining all-atom simulations and experimental Rg data is presented.
- **Visible evidence base** Main text figures 1-5 (described but not directly viewable), figure supplements referenced, methods section with simulation protocols, and data availability links. No raw data, trajectories, or code were directly inspected.
- **Missing materials affecting confidence** Actual figure images and figure supplements were not provided. Simulation parameter tables (Tables 1-3) referenced but not shown. No supplementary information files. The theoretical derivation supporting the linear correlation is only summarized, not fully presented. No direct comparison to experimental phase diagrams beyond Rg calibration.

## Reviewer

### Overall assessment
This manuscript addresses a timely and important problem in the field of biomolecular phase separation: the role of desolvation in CG modeling. The authors propose a physically motivated extension to the widely used HPS framework and demonstrate nontrivial consequences for phase behavior, condensate structure, and dynamics. The work is potentially valuable, but the current presentation has several gaps that prevent full evaluation. The central claims about the linear correlation between temperature gap and conformational change, and the mechanistic separation of density versus energy-landscape effects on dynamics, require stronger evidence and clearer theoretical grounding. The parameterization strategy is pragmatic but the transferability claims need more rigorous testing. Overall, the manuscript shows promise but is not yet established from the provided evidence.

### Who would be interested in the results, and why
Computational biophysicists and physical chemists working on biomolecular condensates and intrinsically disordered proteins would be the primary audience. Researchers developing CG models for LLPS would find the desolvation-aware potential a useful extension. The work also speaks to experimentalists interested in the molecular determinants of condensate properties, particularly those studying pressure effects or cosolute modulation of phase behavior. The theoretical link between conformational change and distance from criticality could interest polymer physicists working on phase transitions in macromolecular systems.

### Major strengths
1. The manuscript identifies a genuine and underappreciated limitation of implicit-solvent CG models: the neglect of desolvation barriers and solvent-separated minima.
2. The proposed modification is physically motivated and grounded in all-atom PMF calculations.
3. The systematic exploration of desolvation parameters on phase diagrams, conformations, and dynamics is thorough.
4. The observation that desolvation can decouple phase-separation propensity from dense-phase packing is an important conceptual advance.
5. The parameterization strategy against experimental Rg data is pragmatic and addresses a real need in the field.
6. The dynamic analysis, including the identification of kinetic arrest and its modulation by desolvation, adds a valuable dimension beyond equilibrium thermodynamics.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims a strong linear correlation between the temperature gap (Tc* - Tsim*) and the extent of conformational expansion (ΔRg) accompanying the dilute-to-dense phase transition, with R² = 0.942.
- **Evidence pointer** Figure 3D and inset; theoretical derivation summarized in Results section "Conformational modulation by desolvation in dense and dilute phases"
- **Concern** The linear correlation is presented as a central finding, but the theoretical derivation is only sketched. The relationship between ΔRg and (Tc - Tsim) is derived through a chain of assumptions (Flory-Huggins theory, linear response of Rg to interaction strength) that are not fully justified. The R² value is reported for a single figure, but it is unclear how many data points, which parameter ranges, and whether this correlation holds across different sequences or only for the homopolymer model. The claim that this is a "fundamental coupling" requires more rigorous testing.
- **Why it matters** This correlation is presented as a general principle linking microscopic conformational changes to macroscopic phase behavior. If it is only an artifact of the specific model or parameter range, the claim is overstated. The theoretical framework needs to be explicit enough for others to test and extend.
- **Resolution test** Provide the full derivation of the linear relationship, including all assumptions. Show the correlation for multiple sequences and parameter sets. Test whether the correlation holds when desolvation parameters are varied independently. Report the number of data points and the statistical significance of the fit.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological validation
- **Claim pointer** The manuscript claims that the desolvation-aware model "enables an efficient representation of desolvation in CG simulations" and that the parameterization strategy is "transferable."
- **Evidence pointer** Results section "Parameterization of desolvation model for IDPs"; Figure 5; Table 1 (not shown)
- **Concern** The parameterization uses averaged values of αb and αss across a limited set of amino acid analogue pairs. The manuscript acknowledges this limitation but then applies these averaged parameters to all residue pairs in the IDP test set. The transferability claim is not adequately tested. The improvement in χ²Rg from 1082.27 to 85.88 for HPS-desolvation is impressive, but the comparison to CALVADOS2 (which achieves much lower χ²Rg values) is not fully contextualized. The manuscript does not show whether the desolvation parameters are sequence-dependent or whether the averaged values are appropriate for diverse IDP sequences.
- **Why it matters** The utility of the model depends on its transferability to arbitrary IDP sequences. If the averaged parameters are not representative, the model may not perform well outside the calibration set. The comparison to CALVADOS2 needs to be framed more carefully to show what the desolvation terms add beyond existing parameter optimization.
- **Resolution test** Test the model on a held-out set of IDPs not used in calibration. Compare the performance of the desolvation-aware model to CALVADOS2 with and without desolvation terms on the same test set. Show the distribution of fitted αb and αss values across residue pairs and justify the use of averaged values.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretational clarity
- **Claim pointer** The manuscript claims that "desolvation barriers slow early density-fluctuation growth and shorten transient kinetic arrest, whereas solvent-separated contact interactions exert the opposite effects."
- **Evidence pointer** Results section "Desolvation-modulated kinetic arrest of coarsening dynamics"; Figure 4F and G
- **Concern** The mechanistic interpretation of the kinetic data is not fully supported. The manuscript attributes the kinetic effects to "viscoelastic resistance" and "energy landscape roughness," but these concepts are invoked rather than demonstrated. The separation of density effects from energy-landscape effects in the reduced diffusion coefficient K̃ relies on assumptions (constant packing fraction at matched quench depth) that are stated but not verified. The claim that the standard HPS model exhibits "much faster" mobility is qualitative and needs quantitative support.
- **Why it matters** The dynamic analysis is a key contribution of the paper, but the interpretation needs to be rigorous. If the kinetic effects can be explained by simpler mechanisms (e.g., changes in effective temperature or density alone), the claim that desolvation specifically modulates dynamics is weakened.
- **Resolution test** Provide direct evidence for the viscoelastic interpretation, such as stress autocorrelation functions or relaxation time spectra. Verify the assumption of comparable packing fractions at matched quench depth. Quantify the difference in mobility between models and show that it is statistically significant.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scope of validation
- **Claim pointer** The manuscript claims that the desolvation-aware model "reshapes the phase diagram, alleviating dense-phase overcompaction" and that this is a general improvement over standard implicit-solvent CG models.
- **Evidence pointer** Results section "Thermodynamic impact of desolvation on the phase diagram"; Figure 2D-G
- **Concern** The validation is limited to a homopolymer model and two specific IDPs (FUS LC and LAF-1 RGG). The claim that desolvation alleviates overcompaction is demonstrated for these cases, but the generality is not established. The manuscript does not compare the dense-phase densities to experimental measurements or to predictions from explicit-solvent models. The reduction of approximately 5% in packing density is modest and may not be significant given the uncertainties in CG models.
- **Why it matters** The central motivation for the desolvation-aware model is to improve the physical realism of CG simulations. If the improvement is marginal or sequence-dependent, the practical impact is limited.
- **Resolution test** Apply the model to a broader set of IDPs with known experimental phase behavior. Compare predicted dense-phase densities to experimental measurements (e.g., from FRAP or sedimentation assays). Quantify the improvement relative to the original models across the full test set.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Equation 1 and parameter definitions
- **Evidence pointer** Results section "Effective representation of desolvation effects in coarse-grained models"
- **Issue** The notation for the desolvation parameters is introduced but the physical interpretation of αb and αss is not fully explained. The relationship between these parameters and the underlying PMF features is not made explicit.
- **Required correction** Provide a clear physical interpretation of αb and αss, and explain how they relate to the barrier height and solvent-separated minimum depth in the PMF. Consider adding a schematic figure showing the modified potential.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Simulation protocols
- **Evidence pointer** Methods section "Coarse-grained simulations"
- **Issue** The methods section describes the simulation setup but does not provide sufficient detail on the equilibration protocol, the number of independent replicas for the phase diagram calculations, or the criteria for determining phase coexistence.
- **Required correction** Provide more detailed simulation protocols, including the number of replicas, the length of equilibration and production runs, and the criteria for identifying coexisting phases. Consider adding a table summarizing all simulation conditions.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Figure 3D correlation
- **Evidence pointer** Results section "Conformational modulation by desolvation in dense and dilute phases"
- **Issue** The R² value of 0.942 is reported, but no confidence intervals or p-values are given. The number of data points is not stated.
- **Required correction** Report the number of data points, the p-value, and confidence intervals for the correlation. Consider showing the data points on the figure rather than only the fitted line.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion of desolvation in LLPS
- **Evidence pointer** Introduction and Discussion
- **Issue** The manuscript cites several relevant studies but does not fully engage with the recent literature on hydration and water dynamics in condensates, particularly experimental work on water mobility in dense phases.
- **Required correction** Add a brief discussion of experimental evidence for altered water dynamics in condensates and how the desolvation-aware model relates to these observations.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Theoretical derivation
- **Evidence pointer** Results section "Conformational modulation by desolvation in dense and dilute phases"
- **Issue** The theoretical derivation connecting ΔRg to (Tc - Tsim) is compressed and difficult to follow. The assumptions are not clearly stated.
- **Required correction** Expand the derivation in the main text or provide a supplementary derivation with all steps and assumptions explicitly stated.

### Technical failings that need to be addressed before the case is established
1. The theoretical derivation of the linear correlation between ΔRg and (Tc - Tsim) is incomplete and needs to be fully presented (R1-M1).
2. The transferability of the averaged desolvation parameters is not adequately tested (R1-M2).
3. The mechanistic interpretation of kinetic effects requires direct evidence for viscoelastic behavior (R1-M3).
4. The validation set is too limited to support general claims about improving CG models (R1-M4).

### Assessment against Nature-style criteria
- **Originality** The work is original in its specific focus on desolvation in CG models for LLPS. While desolvation has been studied in protein folding, its systematic incorporation into LLPS CG models is novel. The observation that desolvation can decouple phase-separation propensity from packing density is a new conceptual contribution.
- **Scientific importance** The problem addressed is important: implicit-solvent CG models are widely used, and their limitations are not fully understood. The work has the potential to improve the predictive power of such models. However, the importance is somewhat limited by the focus on generic desolvation features rather than sequence-specific effects.
- **Interdisciplinary readership** The work is primarily of interest to computational biophysicists and physical chemists. The relevance to experimental biologists is indirect, though the implications for understanding condensate properties could be of broader interest. The manuscript does not currently make a strong case for why experimentalists should care.
- **Technical soundness** The simulation methodology is generally sound, but the theoretical analysis is underdeveloped and the validation is limited. The statistical treatment of the key correlation is insufficient. The parameterization strategy is reasonable but not rigorously tested.
- **Readability for nonspecialists** The manuscript is written in a technical style that assumes familiarity with CG models and phase separation theory. The abstract is accessible, but the results section would be challenging for nonspecialists. The key conceptual points could be better highlighted.

### Recommendation posture
Supportive if technical concerns are resolved. The core idea is valuable and the preliminary results are promising, but the current evidence does not fully establish the central claims. The manuscript would benefit from a more rigorous theoretical treatment, broader validation, and clearer presentation of the key findings. If the authors can address the major concerns, particularly the theoretical derivation and the transferability testing, the work could make a significant contribution to the field.