## Review setup
- **Input scope** Full manuscript text (abstract, introduction, theory, methods, results, discussion, conclusions) as provided
- **Assessment boundary** Scientific content, methodological soundness, validity of claims relative to presented evidence; not language editing or formatting
- **Shared manuscript claim summary** The authors present a new algorithm, reweighted hierarchical chain growth (RHCG), to build atomically resolved structural ensembles of the intrinsically disordered protein tau K18. They claim that integrating local NMR chemical shift data during fragment assembly, followed by a formal Bayesian reweighting step, yields ensembles that reproduce global experimental observables (RDCs, SAXS, FRET) without further fitting. They further claim that pathogenic P301 mutations shift the conformational population from microtubule-binding turn-like structures toward aggregation-prone extended structures.
- **Visible evidence base** Main text figures referenced (Figures 1–5), supplementary figures and text referenced (Figures S1–S11), experimental methods described in main text and SI
- **Missing materials affecting confidence** Full supplementary information not provided; specific numerical values for key comparisons (e.g., χ² values, correlation coefficients beyond those stated) not fully detailed; details of the fragment library construction and REMD simulation parameters only partially described; SI Text referenced but not available for full assessment

## Reviewer
- **Overall assessment** This manuscript addresses a significant challenge in the structural biology of intrinsically disordered proteins: building ensembles that are simultaneously consistent with local and global experimental observables. The RHCG approach is a conceptually important advance, as it formalizes the incorporation of experimental data during chain growth within a Bayesian framework, thereby addressing the exponential weighting problem that plagues reweighting of long polymer chains. The validation against multiple independent experimental measurements (RDCs, SAXS, FRET) is commendable. The biological finding regarding P301 mutations shifting conformational equilibria is potentially important. However, several technical aspects require clarification and additional analysis before the central claims can be considered fully established. In particular, the sensitivity of the results to the choice of fragment library, the robustness of the importance sampling assessment, and the quantitative rigor of the mutation comparisons need further scrutiny.
- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, integrative structural biology, computational biophysics, and neurodegeneration. The methodological advance (RHCG) will be of interest to those developing ensemble methods for IDPs and flexible polymers. The biological findings on tau conformational ensembles and the effects of pathogenic mutations will interest the tau and neurodegeneration communities, particularly those studying the structural basis of tau aggregation and microtubule binding.
- **Major strengths** The manuscript presents a formally rigorous framework for integrating experimental data into ensemble generation, addressing a known limitation of post-hoc reweighting. The validation strategy is strong, testing predictions against multiple independent experimental observables not used in the fitting. The comparison of wild-type and mutant ensembles provides a biologically relevant application. The authors are transparent about the limitations of their approach and the need for large ensembles.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that RHCG produces ensembles that "capture the average local structure of tau as reported by NMR" and that the improvement over HCG is meaningful.
- **Evidence pointer** Results section "RHCG Models of tau K18 Capture the Average Local Structure of tau as Reported by NMR"; Figures S4A,B
- **Concern** The reported improvement in Cα chemical shift agreement from HCG to RHCG is modest (Pearson's r from 0.28 to 0.41; average residual from 0.35 to 0.27 ppm). Given that the stated uncertainty in the forward calculation is approximately 1 ppm, the residual values are well within this error for both methods. The authors state that a lower θ was "not justified" due to the small amplitude of the secondary shifts, but this raises the question of whether the chemical shift data provide sufficient information content to meaningfully bias the ensemble. The improvement, while in the right direction, may not be statistically distinguishable from noise given the forward model uncertainty. The authors should provide a statistical analysis (e.g., error bars on the correlation coefficients, or a null-hypothesis test comparing RHCG to HCG with the same number of effective parameters) to demonstrate that the improvement is significant.
- **Why it matters** The central methodological claim is that incorporating local data during chain growth improves ensemble quality. If the improvement is within noise, the advantage of RHCG over HCG for this system is not established, weakening the case for the method's general utility.
- **Resolution test** Provide a statistical comparison of the chemical shift agreement between HCG and RHCG ensembles, including confidence intervals on the correlation coefficients or a permutation test. Alternatively, demonstrate that the RHCG ensemble improves prediction of a local observable not used in the fitting (e.g., 3J coupling) with statistical significance.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that the RHCG ensemble reproduces RDC data "without further fitting" and that this validates the ensemble.
- **Evidence pointer** Results section "The RHCG ensemble of tau K18 Reproduces the Experimental NMR Residual Dipolar Couplings"; Figures 1A,B, 2B,C
- **Concern** The RDC calculation uses the steric alignment mode of PALES, which is a forward model with its own parameters and assumptions. The authors report Pearson r values of 0.73 (RHCG) and 0.70 (HCG). While the agreement is described as "remarkable," the difference between RHCG and HCG is small. More critically, the authors note that RDC values are widely distributed for individual residues (±25 Hz range) and that large ensembles (≥10,000) are needed for convergence. This raises concerns about whether the ensemble average is stable and whether the agreement is sensitive to the specific ensemble composition. The authors should report the uncertainty in the calculated RDC values (e.g., from bootstrapping the ensemble) and demonstrate that the agreement is robust to ensemble size and composition.
- **Why it matters** The RDC validation is a key piece of evidence that the ensemble captures global structural properties. If the agreement is not robust or is sensitive to details of the calculation, the claim that the ensemble is validated by RDCs is weakened.
- **Resolution test** Provide bootstrap or jackknife estimates of the RDC correlation coefficients to demonstrate stability. Show that the agreement does not depend critically on a small subset of high-weight chains. Report the distribution of per-residue RDC predictions and compare to experimental uncertainties.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The claim that "pathogenic single-point P301 mutations shift the population from the turn-like conformations of the functional microtubule-bound state to the extended conformations of disease-associated tau fibrils."
- **Evidence pointer** Results section "Aggregation-Prone Extended Structures Feature Prominently in the Solution Ensemble of tau K18" and "RHCG Captures the Effect of Mutations Towards Aggregation-Prone Structures"; Figures 4, 5
- **Concern** The comparison between wild-type and mutant ensembles is based on the fraction of structures within a 1 Å Cα RMSD cutoff of specific fibril structures. The choice of this cutoff is arbitrary, and the authors do not report how sensitive their conclusions are to this threshold. Furthermore, the fraction of wild-type structures matching fibril conformations (9% for VQIINK, 8% for VQIVYK) is described as "small but significant," but the statistical significance of the difference between wild-type and mutants is not quantified. The authors state a "more than twofold reduction" in turn-like structures for mutants, but no confidence intervals or statistical tests are provided. Given that the ensembles are generated from the same fragment library with only local sequence changes, the differences could be within the noise of the method.
- **Why it matters** The biological conclusion regarding mutation effects is a major selling point of the paper. If the differences between wild-type and mutant ensembles are not statistically robust, the biological interpretation is not supported.
- **Resolution test** Provide statistical analysis of the differences in conformational populations between wild-type and mutants, including confidence intervals or bootstrap estimates. Show that the conclusions are robust to the choice of RMSD cutoff and to the specific fibril reference structures used.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The claim that the importance sampling assessment, quantified by the KL divergence from ideal importance sampling, demonstrates the effectiveness of the bias.
- **Evidence pointer** Theory section "Assessment of Importance Sampling"; Results section "RHCG Produces a Diverse Ensemble of tau K18 Chains"; Figure S1B
- **Concern** The authors report that the global reweighting step results in near-uniform weights with S_KL ≈ 0.2 for the FRET reweighting. However, the assessment of the importance sampling quality is only briefly described. The authors state that the KL divergence from ideal importance sampling is used to assess effectiveness, but the actual values for the RHCG versus HCG ensembles are not systematically reported. A more thorough analysis of the effective sample size or the distribution of weights would strengthen the claim that RHCG produces well-defined ensembles.
- **Why it matters** The methodological contribution of RHCG depends on demonstrating that the bias introduced during chain growth is properly corrected and that the final ensemble is not dominated by a few chains. Without a clear demonstration of this, the advantage of RHCG over simpler approaches is not fully established.
- **Resolution test** Report the effective sample size or the distribution of weights for the RHCG and HCG ensembles before and after reweighting. Show that the RHCG ensemble has a more uniform weight distribution than HCG after reweighting.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The claim that the RHCG ensemble is consistent with single-molecule FRET data and that the small correction needed to match FRET distances indicates the ensemble is nearly correct.
- **Evidence pointer** Results section "The RHCG Ensemble Captures the Extension of tau K18 in Solution" and "Structure of tau K18 as Assessed by Single-Molecule FRET"; Figure 1E, S2
- **Concern** The comparison to FRET data involves a reweighting step (S_KL ≈ 0.2) to match the mean distance. The authors interpret the small S_KL as indicating that the ensemble is close to the true distribution. However, the FRET data provide only a single mean distance, which is a very low-dimensional constraint. The fact that a small reweighting is sufficient to match this single observable does not strongly validate the ensemble's global properties. The authors should acknowledge this limitation more explicitly and discuss what additional experimental data would be needed to more rigorously validate the ensemble.
- **Why it matters** The claim that the ensemble captures global structure is based on agreement with a limited set of observables. Overinterpreting agreement with a single mean distance could mislead readers about the level of validation achieved.
- **Resolution test** Discuss the limitations of validation against a single mean distance. If possible, compare the full distance distributions (not just means) from the ensemble to the FRET data, or identify additional experimental observables that could provide stronger constraints.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Theory section
- **Evidence pointer** Theory section "Bayesian Ensemble Refinement of Polymeric Molecules"
- **Issue** The derivation of the Bayesian framework is presented compactly, and the connection between the KL divergence and the effective sample size could be explained more clearly for readers not deeply familiar with importance sampling.
- **Required correction** Add a brief intuitive explanation of why the KL divergence from ideal importance sampling measures the quality of the ensemble, and how the effective sample size relates to the weight distribution.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods section
- **Evidence pointer** Methods section "Hierarchical and Reweighted Hierarchical Chain Growth"
- **Issue** The description of the fragment library construction is brief. The number of fragments per position, the criteria for selecting fragments from the REMD trajectories, and the convergence of the fragment simulations are not fully described.
- **Required correction** Provide additional details on the fragment library construction, including the number of fragments per position, the selection criteria, and the convergence assessment of the REMD simulations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion of mutation effects
- **Evidence pointer** Results section "RHCG Captures the Effect of Mutations Towards Aggregation-Prone Structures"
- **Issue** The authors compare P301L, P301S, and P301T mutations but do not discuss potential differences in the severity of their effects. The clinical phenotypes of these mutations differ, and the authors could comment on whether their modeling captures any differential effects.
- **Required correction** Add a brief discussion of whether the three mutations show quantitatively different effects in the ensembles and how this might relate to their distinct clinical presentations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Figure 1
- **Evidence pointer** Figure 1
- **Issue** The figure is information-dense, and the caption does not fully explain all panels. In particular, the relationship between panels C, D, and E could be clarified.
- **Required correction** Expand the figure caption to clearly describe each panel and the relationship between the structural ensembles, RDC predictions, and FRET comparisons.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** SAXS analysis
- **Evidence pointer** Results section "The RHCG Ensemble Captures the Extension of tau K18 in Solution"
- **Issue** The authors mention accounting for possible aggregation in the low-q regime of the SAXS data. The details of this correction are not fully described in the main text.
- **Required correction** Provide a brief description of the aggregation correction in the main text or refer more explicitly to the SI for details.

- **Technical failings that need to be addressed before the case is established** The statistical significance of the improvement of RHCG over HCG for chemical shifts and RDCs needs to be established. The robustness of the mutation effect conclusions to analysis choices (e.g., RMSD cutoffs) needs to be demonstrated. The validation against FRET data should be presented with appropriate caveats about the low-dimensional nature of the constraint.
- **Assessment against Nature-style criteria** Originality: High. The RHCG approach is a novel methodological contribution that addresses a recognized problem in IDP ensemble modeling. Scientific importance: High. The work has implications for understanding tau structure and function, and the method could be broadly applicable to other IDPs. Interdisciplinary readership: Moderate to high. The work bridges computational biophysics, NMR spectroscopy, and neurodegeneration research. Technical soundness: Moderate. The framework is formally rigorous, but the statistical validation of key claims is incomplete. Readability for nonspecialists: Moderate. The manuscript is clearly written but assumes familiarity with ensemble refinement and IDP biophysics.
- **Recommendation posture** Supportive if technical concerns are resolved. The methodological framework is promising and the biological application is significant, but the current evidence does not fully establish the superiority of RHCG over existing approaches or the robustness of the mutation effect conclusions.