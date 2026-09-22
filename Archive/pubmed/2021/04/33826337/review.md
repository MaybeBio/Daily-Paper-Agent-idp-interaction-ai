## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, claims, and evidence presented in the manuscript
- **Shared manuscript claim summary** The authors present a new coarse-grained force field (MOFF) derived from a combination of maximum entropy optimization and energy landscape theory principles. They claim MOFF consistently models both ordered and disordered proteins, accurately predicts radii of gyration, differentiates protein types via theta temperature, resolves structural differences between HP1 homologs, and captures phase separation behavior consistent with experiments.
- **Visible evidence base** Methods section, Results and Discussion section, Figures 1–7 (referenced), Tables 1 and S1–S5 (referenced), Equations 1–6
- **Missing materials affecting confidence** Supplementary Information (SI) sections referenced but not provided, including simulation details, mathematical expressions of the energy function, and additional figures (S1–S16). Experimental data for HP1γ validation not available. Atomistic simulation data for bias strength calibration not shown.

## Reviewer
- **Overall assessment** The manuscript presents a methodologically interesting approach to unify coarse-grained force field parameterization for ordered and disordered proteins. The combination of maximum entropy optimization with energy gap constraints is a reasonable strategy, and the application to HP1 phase separation is timely. However, the evidence provided in the main text is insufficient to fully evaluate the robustness of the method, particularly regarding the transferability claims, the sensitivity of results to training set composition, and the quantitative accuracy of phase behavior predictions. Several key technical details are relegated to the SI, which was not available for review. The claims regarding homolog-resolved phase separation are supported by simulation but lack direct experimental validation for two of the three homologs.
- **Who would be interested in the results, and why** Researchers in computational biophysics, specifically those developing or using coarse-grained models for intrinsically disordered proteins and phase-separating systems. The force field development community would be interested in the methodological combination of maximum entropy and energy landscape approaches. Experimental groups studying HP1 and heterochromatin organization may also find the predictions useful for generating hypotheses, though they would likely require more direct experimental validation.
- **Major strengths** 1) The methodological combination of maximum entropy optimization with energy landscape constraints is novel and addresses a real gap in the field. 2) The application to a biologically relevant system (HP1) with clear experimental context strengthens the motivation. 3) The computational efficiency enabling large-scale phase separation simulations is a practical advantage. 4) The identification of specific amino acid clusters and their correlation with protein type provides a potentially useful predictive framework.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** **Originality**: The methodological combination is novel, though individual components are established. The application to HP1 homologs is new. **Scientific importance**: The work addresses a significant challenge in the field, but the impact depends on the robustness and generalizability of the method, which is not fully demonstrated. **Interdisciplinary readership**: The topic bridges biophysics, computational chemistry, and cell biology, but the presentation is heavily method-focused and may not be accessible to a broad readership. **Technical soundness**: The approach is reasonable, but key validation steps and sensitivity analyses are missing from the main text. The reliance on SI for critical details limits assessment. **Readability for nonspecialists**: The manuscript is clearly written for a computational biophysics audience. The biological motivation is clear, but the methodological sections require significant expertise to follow.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding validation, sensitivity analysis, and clarification of key methodological details.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that MOFF "can model both ordered and disordered proteins with consistent accuracy" and that it "outperforms" existing force fields.
- **Evidence pointer** Figures 2A–B, Tables S2–S3
- **Concern** The validation of MOFF's accuracy is based on a training set of only 23 proteins (7 ordered, 16 disordered) and a validation set of 8 proteins. This is a small sample size, and the selection criteria for these proteins are not described in the main text. The claim of "consistent accuracy" is based on percent error in Rg, but the distribution of errors across different protein types, sizes, and sequence compositions is not shown. The improvement over MJ and MOFF-IDP is presented as aggregate percent error, but the statistical significance of these differences is not assessed. Furthermore, the validation set results (17.9% error) are substantially worse than the training set results (9.6% error), suggesting possible overfitting, which is not discussed.
- **Why it matters** The central claim of the paper is that MOFF provides a unified and accurate description of both ordered and disordered proteins. If the validation is not robust, the method's generalizability is questionable, and the conclusions drawn from its application to HP1 may not be reliable.
- **Resolution test** Provide a more detailed breakdown of errors per protein, including individual Rg values for all training and validation proteins. Perform a leave-one-out cross-validation analysis. Discuss the potential for overfitting and how the method's parameters were regularized. If possible, test on a larger, independent set of proteins with diverse sequence properties.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the theta temperature determined from MOFF separates ordered and disordered proteins at 300 K and exhibits a strikingly linear relationship with amino acid sequence composition."
- **Evidence pointer** Figures 5A–D, Equation 5
- **Concern** The theta temperature is a thermodynamic quantity that depends on the balance of interactions. The claim that Tθ separates ordered and disordered proteins at exactly 300 K is striking, but the uncertainty in Tθ values is not reported. The linear relationship in Equation 5 is based on a LASSO regression, but the number of data points (23 proteins) is small relative to the number of potential predictors (20 amino acids, or 6 clusters). The model's predictive power is assessed via correlation with simulated Tθ values, but this is circular since the same simulations were used to derive the model. The generalizability of Equation 5 to proteins outside the training set is not demonstrated.
- **Why it matters** The theta temperature and its sequence dependence are presented as key insights from the force field. If these relationships are not robust, the biological conclusions drawn from them (e.g., about HP1 phase behavior) are weakened.
- **Resolution test** Report uncertainties in Tθ estimates. Validate Equation 5 on a held-out set of proteins not used in the regression. Discuss the physical interpretation of the fitted coefficients and whether they are consistent with known interaction propensities. Provide a more thorough cross-validation of the LASSO model.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The authors claim that "the force field successfully resolved the structural difference of two HP1 homologs, despite their high sequence similarity" and that the predicted critical temperatures "agree with qualitative experimental observations that only HP1α can phase separate in vitro at room temperature."
- **Evidence pointer** Figures 6B–D, 7C, S10, S13, Table S4
- **Concern** The comparison between simulated and experimental Rg values for HP1α and HP1β is presented as favorable, but the experimental values are from different studies and conditions, and the uncertainty in these values is not discussed. The claim that only HP1α can phase separate in vitro is based on specific experimental conditions (Refs 14, 25); the authors do not discuss whether the simulated conditions (e.g., concentration, salt, temperature range) match these experiments. The critical temperatures for HP1β and HP1γ are predicted to be below 300 K, but the authors do not provide a quantitative comparison to any experimental measurement of phase behavior for these homologs. The statement that "only HP1α can phase separate" is a qualitative conclusion drawn from TC values, but the relationship between TC and the experimentally observed phase separation at a specific temperature and concentration is not rigorously established.
- **Why it matters** The biological relevance of the work hinges on the accuracy of the HP1 predictions. If the comparison to experiment is not rigorous, the claim that MOFF captures homolog-resolved phase separation is not established.
- **Resolution test** Provide a more detailed comparison to experimental conditions, including salt concentration, protein concentration, and temperature. Discuss the sensitivity of the predicted TC values to these conditions. If possible, perform simulations under conditions that more closely match the cited experiments. Acknowledge the limitations of comparing coarse-grained simulation results to experimental measurements.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "we augmented MOFF with additional biases derived from the initial structures" to stabilize HP1 tertiary structure, and that these biases "do not impact our prediction of the radius of gyration and inter-dimer interactions."
- **Evidence pointer** Methods section, SI Section: Folding potential for HP1 tertiary structure stabilization
- **Concern** The nature and strength of these additional biases are not described in the main text. The claim that they do not impact Rg and inter-dimer interactions is not supported by any data shown in the main text. If these biases are strong enough to hold the ordered domains in their folded state, they could artificially constrain the conformational ensemble and affect the predicted interactions between domains and between dimers. The calibration of the bias strength using "short atomistic simulations" is mentioned but not shown.
- **Why it matters** The use of structure-based biases could introduce a bias toward the experimentally known folded state, potentially masking inaccuracies in the force field. If the biases affect inter-domain or inter-dimer interactions, the conclusions about multivalent interactions driving phase separation could be compromised.
- **Resolution test** Provide a detailed description of the bias potential, its functional form, and its strength. Show data demonstrating that the biases do not affect Rg or inter-dimer interactions, e.g., by comparing simulations with and without the biases. Describe the atomistic simulations used for calibration and show the resulting bias parameters.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section, "Details on Molecular Dynamics Simulations"
- **Evidence pointer** Location not provided
- **Issue** The description of the replica exchange simulation parameters (e.g., number of replicas, exchange acceptance rate, total simulation time per replica) is not provided in the main text.
- **Required correction** Provide these details in the main text or refer more explicitly to the SI section where they are described.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section, "Coarse-grained Protein Force Field"
- **Evidence pointer** Equation 1
- **Issue** The functional form of UMOFF is given, but the specific parameters for the bond, angle, dihedral, and electrostatic terms are not described in the main text.
- **Required correction** Provide a summary of these parameters or a clear reference to the SI where they are fully defined.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results, "MOFF Identifies Sequence Features to Differentiate Ordered and Disordered Proteins"
- **Evidence pointer** Figure 4
- **Issue** The clustering analysis is based on the contact energy matrix, but the choice of Euclidean distance and hierarchical clustering is not justified. The robustness of the clusters to the choice of clustering algorithm is not assessed.
- **Required correction** Briefly justify the clustering approach or note that the results are robust to alternative methods.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, "Homolog Specific HP1 Phase Separation"
- **Evidence pointer** Figure 7
- **Issue** The slab simulation method is mentioned, but the details of how the phase boundary is determined and how the critical temperature is extracted from the simulations are not described in the main text.
- **Required correction** Provide a brief description of the analysis method or refer to the SI for details.

## Risk / unsupported claims
- The claim that MOFF "can model both ordered and disordered proteins with consistent accuracy" is not fully supported due to the small validation set and lack of cross-validation.
- The claim that Tθ "separates ordered and disordered proteins at 300 K" is presented without uncertainty estimates and may be sensitive to the training set composition.
- The claim that the linear relationship in Equation 5 is "general and transferable" is not supported by validation on an independent set of proteins.
- The claim that the additional biases used to stabilize HP1 tertiary structure "do not impact" Rg and inter-dimer interactions is not supported by data in the main text.
- The comparison of simulated critical temperatures to experimental phase separation behavior is qualitative and does not account for differences in conditions.
- The prediction for HP1γ phase behavior is not validated by any experimental data.