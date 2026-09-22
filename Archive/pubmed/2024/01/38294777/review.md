## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, conclusions) without supplementary material
- **Assessment boundary** Scientific validity, methodological soundness, and internal consistency of the presented computational procedure and its validation against experimental data
- **Shared manuscript claim summary** The authors propose a computationally efficient multiscale method combining atomistic MD simulations, binding polynomial theory, and Wertheim's thermodynamic perturbation theory to predict the rank-ordering of excipient effects on protein–protein interaction affinities and solution viscosity for a monoclonal antibody (MEDI-4212)
- **Visible evidence base** Main text figures (Figures 1–6), Tables (Table 1), equations (Eqs 1–13), and references to Supporting Information sections (S1–S6, Figures S1–S10, Tables S1–S4)
- **Missing materials affecting confidence** Full Supporting Information content (detailed simulation parameters, fitting procedures, additional figures and tables), experimental viscosity datasets referenced but not reproduced, and specific numerical values for all fitted parameters

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting and potentially useful computational framework for predicting excipient effects on protein–protein interactions. The combination of binding polynomial theory with MD-derived parameters is a reasonable and novel approach. However, the validation is limited to a single antibody system with four excipients, and several methodological details and assumptions require clarification. The claim of "semiquantitative agreement" is only partially supported by the evidence presented, and the sensitivity of the results to key modeling choices (e.g., interface definition, Cookie model selection) is not fully explored. The work is likely of interest to the computational biophysics and biologics formulation communities, but the current evidence base is insufficient to fully establish the general utility of the method.

- **Who would be interested in the results, and why** Researchers in computational biophysics, protein engineering, and biologics formulation development would be interested. The method offers a potentially faster route to screen excipients for reducing antibody viscosity, which is a practical industrial problem. The binding polynomial framework could also be adapted to other protein–protein interaction contexts, making it relevant to a broader biophysical audience.

- **Major strengths**  
  1. The conceptual framework is elegant, combining established theories (binding polynomials, Wertheim TPT) with MD simulations in a computationally tractable manner.  
  2. The explicit treatment of multiple Cookie models (empty, traditional, double-stuffed) provides a systematic way to test assumptions about excipient accommodation at interfaces.  
  3. The use of a proxy parameter (a = NKe) to overcome identifiability issues in fitting is a practical and sensible solution.  
  4. The method successfully rank-orders the four tested excipients in agreement with experimental observations, providing a proof-of-principle demonstration.

- **Major Concerns**

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Validation sufficiency  
- **Claim pointer** "This approach appears useful for predicting the effects of excipients on protein association and phase separation, as well as the effects of buffers on protein solutions" (Abstract) and "we found semiquantitative agreement with experimental results" (Conclusions)  
- **Evidence pointer** Results section "Evaluating the Cookie Models", Figure 6, Table 1  
- **Concern** The validation is based on a single antibody (MEDI-4212) and four excipients, all of which are amino acids. The claim of general utility for predicting excipient effects on protein association and phase separation extends well beyond this narrow test case. The "semiquantitative agreement" is based on rank-ordering rather than quantitative prediction of viscosity values or binding affinities. No error bars or uncertainty quantification are provided for the MD-derived parameters or the fitted aavg values. The sensitivity of the conclusions to the choice of interface definition (buried residue criterion) and the specific bound conformations from ClusPro is not systematically assessed.  
- **Why it matters** Without broader validation or uncertainty quantification, the generalizability of the method remains unestablished. The rank-ordering success could be coincidental or specific to this system. The claim of utility for phase separation and buffer effects is speculative given the limited evidence.  
- **Resolution test** Provide validation on at least one additional antibody or protein system with different excipient chemistries. Include uncertainty estimates for all fitted parameters and demonstrate that the rank-ordering is robust to reasonable variations in interface definition and bound conformation selection. Alternatively, temper the claims to match the evidence presented.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Methodological transparency  
- **Claim pointer** "We calculate the average number of excipient molecules bound to the protein surface at the PPI interface for both Fab and Fc and with each excipient molecule type" (Results, "Obtaining the Microscopic Parameters")  
- **Evidence pointer** Methods section "Simulation Protocol", Results section "Obtaining the Microscopic Parameters", Table 1, Figure 3  
- **Concern** The definition of "bound" excipient molecules is not clearly specified. What distance cutoff or interaction criterion is used to determine whether an excipient is bound to a surface residue? How is the PPI interface defined precisely (buried residue criterion, solvent accessibility threshold)? The manuscript states that the definition depends on the conformation and the definition of "buried," but the actual criteria are only in the Supporting Information, which was not provided. The fitting procedure for the binomial distributions (Figure 3) is described only qualitatively; the fitting method, initial guesses, and goodness-of-fit metrics are not reported.  
- **Why it matters** Reproducibility is a core requirement for computational studies. Without precise definitions of binding criteria and fitting procedures, other researchers cannot apply or verify the method. The parameters N and Ke are central to the model, and their derivation must be transparent.  
- **Resolution test** Provide explicit definitions of binding criteria (e.g., distance cutoffs, contact definitions) and interface residues in the main text or a clearly referenced supplement. Report the fitting algorithm, initial conditions, and goodness-of-fit statistics for the binomial fits. Include a step-by-step protocol that would allow independent implementation.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** No  
- **Axis** Model assumption validity  
- **Claim pointer** "we assume that all N excipient binding sites at the protein–protein interface are equivalent" (Results, "Protein-Excipient Binding Polynomial")  
- **Evidence pointer** Results section "Protein-Excipient Binding Polynomial", Eq 1–5, Figure 1  
- **Concern** The assumption of equivalent, independent binding sites is a strong simplification. Protein surfaces are heterogeneous, and excipient binding affinities likely vary across sites. The manuscript acknowledges this in the Supporting Information (Section S4) but does not test whether the equivalent-site assumption materially affects the conclusions. The authors also assume that excipient binding to the interface is competitive with protein–protein binding, but do not consider potential allosteric effects or changes in protein conformation upon excipient binding.  
- **Why it matters** If the equivalent-site assumption is violated, the derived parameters (N, Ke) may not accurately represent the physical system, and the predictive power of the model could be compromised. The method's utility depends on the robustness of this assumption.  
- **Resolution test** Perform a sensitivity analysis by comparing the equivalent-site model to a model with distributed affinities (e.g., using a site-specific binding model) for at least one excipient. If the results are insensitive, state this explicitly. If sensitive, discuss the implications and potential corrections.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Connection between microscopic and macroscopic scales  
- **Claim pointer** "The simulations above provide us with two parameters that we need for computing the protein dimerization equilibrium coefficient Kp(c) as a function of the excipient concentration" (Results, "From the Microscopic to Macroscopic Predictions")  
- **Evidence pointer** Results section "From the Microscopic to Macroscopic Predictions", Eqs 10–13, Figure 5  
- **Concern** The connection between the MD-derived parameters (N, Ke) and the macroscopic viscosity predictions relies on several intermediate steps: (1) converting MD binding parameters to Kp(c) via the Cookie model, (2) using Wertheim TPT to relate Kp to viscosity, and (3) fitting the Wertheim model to experimental viscosity data. The uncertainty in each step is not propagated. The manuscript states that the Wertheim model "fits the viscosity data well" (Figure 5A), but the quality of the fit is not quantified. The conversion from ϵ to Kp (Eq 11) uses a constant C = 18.2 kJ/mol, but the origin and uncertainty of this value are not discussed.  
- **Why it matters** The predictive power of the method depends on the reliability of each step in the chain. If uncertainties are large or unquantified, the final predictions may be misleading. The use of a single constant C for all conditions is a potential source of systematic error.  
- **Resolution test** Provide quantitative fit statistics for the Wertheim model (e.g., R², RMSD). Discuss the derivation and uncertainty of C. Perform a sensitivity analysis by varying C within a reasonable range and assessing the impact on the predicted rank-ordering. If possible, propagate uncertainties from the MD-derived parameters through to the final predictions.

- **Minor Comments**

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity of presentation  
- **Affected element** Figure 1  
- **Evidence pointer** Results section "Protein-Excipient Binding Polynomial", Figure 1  
- **Issue** The schematic in Figure 1C is described as a "cartoon schematic of a binding polynomial with N = 3," but the figure itself is not available in the provided text. The relationship between the schematic and the equations (Eqs 1–5) is not explicitly described.  
- **Required correction** Provide a clear figure caption and in-text description that explains how the schematic relates to the mathematical formalism. If possible, include a step-by-step walkthrough of the states for N = 3.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness of reporting  
- **Affected element** Table 1  
- **Evidence pointer** Results section "Obtaining the Microscopic Parameters", Table 1  
- **Issue** Table 1 is referenced but not reproduced in the provided text. The values of N, Ke, and a for each excipient are central to the results, but their numerical values and uncertainties are not visible.  
- **Required correction** Ensure Table 1 is included with all values, units, and uncertainties. If space is limited, provide a summary in the main text and full details in the Supporting Information.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Terminology consistency  
- **Affected element** "Cookie model" terminology  
- **Evidence pointer** Results section "Cookie Model of Binding Interfaces", Figure 2  
- **Issue** The term "Cookie model" is introduced without a formal definition. The analogy to cookies (Oreo, etc.) is helpful but should be clearly defined in terms of the physical model. The distinction between "empty," "traditional," and "double-stuffed" is described, but the naming convention could be confusing to readers unfamiliar with the analogy.  
- **Required correction** Provide a formal definition of the Cookie model in the main text, including a clear statement of the physical assumptions and the meaning of the parameter mi. Consider using more descriptive terms (e.g., "zero-excipient interface," "single-excipient interface," "double-excipient interface") alongside the cookie analogy.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Literature context  
- **Affected element** Introduction and Discussion  
- **Evidence pointer** Introduction, Conclusions  
- **Issue** The manuscript cites prior work on excipient effects and computational modeling but does not clearly position the current method relative to existing approaches. For example, how does this method compare to coarse-grained simulations or machine-learning-based predictions of excipient effects?  
- **Required correction** Add a brief paragraph in the Introduction or Discussion that explicitly compares the current method to existing computational approaches for predicting excipient effects, highlighting the novelty and potential advantages.

- **Concern ID** R1-m5  
- **Severity** Minor  
- **Axis** Reproducibility of simulations  
- **Affected element** Methods section "Simulation Protocol"  
- **Evidence pointer** Methods section "Simulation Protocol", Table S1  
- **Issue** The simulation protocol is described, but key details such as the number of independent simulations, the equilibration criteria, and the statistical analysis of the binding probabilities are not fully specified. The manuscript states that "additional details" are in the Supporting Information, but this was not provided.  
- **Required correction** Provide a summary of the key simulation parameters in the main text (e.g., number of replicates, simulation length, temperature, pressure, and analysis methods). Ensure that the Supporting Information contains sufficient detail for independent reproduction.

- **Concern ID** R1-m6  
- **Severity** Minor  
- **Axis** Interpretation of results  
- **Affected element** Figure 6  
- **Evidence pointer** Results section "Evaluating the Cookie Models", Figure 6  
- **Issue** The manuscript states that "the Traditional Cookie model has the best quantitative agreement with the aavg parameters obtained from simulations," but the criteria for "best" are not explicitly defined. Is this based on visual inspection, a statistical metric, or a comparison of numerical values?  
- **Required correction** Provide a quantitative comparison metric (e.g., root-mean-square deviation, chi-squared) and report the values for each Cookie model. This will strengthen the claim of best agreement.

## Risk / unsupported claims
- The claim that the method "appears useful for predicting the effects of excipients on protein association and phase separation, as well as the effects of buffers on protein solutions" (Abstract) is not supported by the evidence, which only demonstrates rank-ordering of four amino acid excipients for viscosity reduction in one antibody.
- The statement "we found semiquantitative agreement with experimental results" (Conclusions) is only weakly supported, as the agreement is based on rank-ordering rather than quantitative prediction, and no uncertainty quantification is provided.
- The assumption that all excipient binding sites are equivalent (Eq 1–5) is stated but not validated against alternative models.
- The claim that AlphaFold Multimer "did not identify bound configurations that agree with the experimental data" is presented without quantitative comparison or details on the AlphaFold predictions.
- The constant C = 18.2 kJ/mol in Eq 11 is used without derivation or justification, and its uncertainty is not assessed.
- The generalizability of the method to other proteins, excipients, and solution conditions is asserted but not demonstrated.