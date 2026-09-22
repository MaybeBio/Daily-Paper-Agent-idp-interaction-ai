## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and supplementary figure references.
- **Assessment boundary** Scientific content, methodological rigor, internal consistency, and support of claims by presented evidence. No assessment of formatting, grammar, or editorial fit.
- **Shared manuscript claim summary** The authors use coarse-grained molecular dynamics simulations of charge-neutral E-K polyampholytes with systematically varied chain length and charge patterning to show that (i) dense-phase chains adopt ideal conformations independent of charge patterning, (ii) chain relaxation times governed by transient interchain electrostatic contacts quantitatively predict condensate viscosity and diffusivity, and (iii) the sticky Rouse model, using sequence-informed contact lifetimes, provides a predictive framework linking sequence to macroscopic material properties.
- **Visible evidence base** Main text Figures 1-6, Supplementary Figures S1-S25, Supplementary Table S1, Methods section with simulation and analysis details.
- **Missing materials affecting confidence** Supplementary figures and table are referenced but not provided in the submitted material. This limits verification of several quantitative claims, particularly those relying on Supplementary Figures S3-S5, S7-S9, S12-S17, and S23-S25.

## Reviewer

### Overall assessment
The manuscript presents a systematic computational study addressing a timely question in the biomolecular condensate field: how sequence features control material properties. The authors combine extensive coarse-grained simulations with polymer theory to propose a predictive framework based on the sticky Rouse model. The central idea, that contact lifetimes rather than monomeric friction govern sequence-dependent dynamics, is conceptually appealing and potentially impactful. However, the manuscript as presented has several issues that need to be addressed before the case is fully established. The claim that the sticky Rouse model "accurately predicts" macroscopic properties rests on comparisons that are not fully shown in the main text, and the phenomenological model for contact lifetimes appears to have limited predictive power beyond the fitted data. The treatment of entanglement effects is somewhat cursory, and the dismissal of reptation-like contributions may be premature given the observed scaling exponents. The work is likely to be of interest to the condensate and polymer physics communities, but the current evidence base is insufficient to fully support the strong claims made.

### Who would be interested in the results, and why
Researchers studying biomolecular condensates, particularly those interested in sequence-encoded material properties, will find this work relevant. The demonstration that a modified Rouse framework can connect molecular interactions to macroscopic rheology addresses a central question in the field. The polymer physics community, especially those working on charged polymers and transient network theories, may also find the sticky Rouse application of interest. Additionally, experimentalists using FRET or rheology to probe condensate dynamics could benefit from the quantitative relationships proposed here, particularly the distinction between vector and distance relaxation times noted in the discussion.

### Major strengths
- Systematic variation of both chain length and charge patterning across a wide parameter range
- Clear conceptual framework connecting microscopic contact lifetimes to macroscopic properties
- Direct test of polymer theory predictions against simulation data
- Use of multiple complementary analyses (conformations, MSD, normal modes, contact lifetimes, viscosity)
- Explicit consideration of solvent effects via Martini simulations
- Practical insight regarding vector versus distance relaxation times for experimental interpretation

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that the sticky Rouse model "accurately predicts chain relaxation times and, consequently, macroscopic material properties" across all sequences.
- **Evidence pointer** Figure 6c, 6d, Supplementary Figures S16-S17
- **Concern** The central quantitative claim of the paper rests on the agreement between sticky Rouse predictions and simulation results shown in Figure 6c-d. However, the main text does not provide quantitative measures of agreement (e.g., correlation coefficients, mean absolute errors, or confidence intervals). The claim of "accurate prediction" requires statistical assessment. Furthermore, the phenomenological model for τEK (Equation 27) is fitted to the simulation data, so the subsequent prediction of τRe and material properties is not fully independent. The predictive power of the framework for sequences outside the fitted range is not demonstrated.
- **Why it matters** The paper's central contribution is a predictive framework. If the model is only descriptive of the simulated data, the claim of prediction is overstated. The field needs quantitative benchmarks to assess whether such frameworks can be used for rational design.
- **Resolution test** Provide quantitative error metrics for the agreement between predicted and simulated τRe, D, and η. Demonstrate predictive capability by training the phenomenological model on a subset of sequences and testing on held-out sequences. Report confidence intervals for fitted parameters.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of scaling exponents
- **Claim pointer** The authors state that scaling exponents for D versus N (ranging from -1.70 to -2.24) and for η versus N (1.91 to 2.14) place the system in a "crossover regime between Rouse and reptation behavior."
- **Evidence pointer** Figure 3a-b, Results section "Chain Length and Charge Patterning Modulate the Dynamics and Rheology of IDP Condensates"
- **Concern** The interpretation of the scaling exponents is ambiguous. The observed exponents for D are close to the reptation prediction of -2, and for η they are intermediate between Rouse (1) and reptation (3.4). However, the authors do not provide a rigorous statistical comparison of the fitted exponents to the theoretical predictions. The claim of a "crossover regime" is qualitative. Moreover, the authors later state that entanglement corrections do not improve predictions (Supplementary Figure S13), which seems to contradict the suggestion that reptation-like physics is relevant. The relationship between the scaling analysis and the sticky Rouse framework is not fully clarified.
- **Why it matters** The physical interpretation of the dynamics determines which theoretical framework is appropriate. If the system is truly in a crossover regime, the applicability of the sticky Rouse model (which does not include entanglements) needs justification. The apparent contradiction between the scaling analysis and the model selection undermines the conceptual coherence of the paper.
- **Resolution test** Perform statistical tests comparing fitted exponents to theoretical predictions. Clarify whether the sticky Rouse model is expected to hold in the crossover regime and why entanglement corrections are not needed despite scaling exponents suggesting otherwise. Provide a phase diagram or regime map showing where each model applies.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Model validation
- **Claim pointer** The authors claim that the sticky Rouse model with sequence-informed contact lifetimes provides a "robust and quantitative connection" from sequence to material properties.
- **Evidence pointer** Figure 6, Methods section "Phenomenological model for sequence-dependent contact lifetimes"
- **Concern** The phenomenological model for τEK (Equation 27) is empirical, with parameters fitted to the simulation data. The model assumes a specific functional form (power law in N, exponential in nSCD^0.24) without clear physical justification. The authors do not test alternative functional forms or assess the uniqueness of the fitted parameters. The model's ability to generalize to other sequence families (e.g., those with hydrophobic residues) is unclear.
- **Why it matters** For the framework to be useful for design, the model must be transferable. An empirical fit to one sequence family does not establish generalizability. The physical basis of the model needs to be articulated more clearly.
- **Resolution test** Test the model on additional sequence families (e.g., sequences with hydrophobic residues or different charge patterns). Provide a physical derivation or justification for the functional form of Equation 27. Assess parameter identifiability and model selection criteria.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Completeness of evidence
- **Claim pointer** The authors state that "the Rouse model with idealized friction fails to capture sequence effects" and that the sticky Rouse model resolves this failure.
- **Evidence pointer** Figure 5c-d, Supplementary Figures S11, S14-S15
- **Concern** The comparison between the standard Rouse model and the sticky Rouse model is not shown directly in the main text. The reader is referred to supplementary figures for the failure of the standard Rouse model, but the quantitative extent of the failure is not described. Additionally, the improvement offered by the sticky Rouse model is not quantified relative to the standard Rouse model. Without a direct comparison, it is difficult to assess whether the added complexity of the sticky model is justified.
- **Why it matters** The paper argues for a specific theoretical framework. The evidence for this framework must include a clear demonstration that simpler models fail and that the proposed model succeeds. The current presentation does not allow the reader to evaluate this claim.
- **Resolution test** Include a direct comparison of standard Rouse, sticky Rouse, and simulation data in the main text, with quantitative error metrics for each model. Show the improvement in prediction accuracy for τRe, D, and η.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 2 inset
- **Evidence pointer** Figure 2
- **Issue** The inset showing Rg = Re/√6 is mentioned but the quality of the collapse is not described. It would be helpful to state the coefficient of determination or mean relative error for this relationship.
- **Required correction** Add a quantitative measure of agreement for the Rg-Re relationship in the text or figure legend.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "Simulation Details"
- **Evidence pointer** Methods section
- **Issue** The number of independent simulations used for averaging viscosity is stated for some cases but not systematically reported for all sequences. The statistical uncertainty in η values is mentioned but not quantified.
- **Required correction** Provide a table or supplementary figure reporting the number of replicates and standard errors for all viscosity measurements.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion of entanglement corrections
- **Evidence pointer** Supplementary Figures S13, S15, S17
- **Issue** The authors state that entanglement corrections do not improve predictions but do not discuss why this is the case given the scaling exponents. A brief explanation of why the sticky Rouse model suffices despite apparent reptation-like scaling would strengthen the discussion.
- **Required correction** Add a paragraph in the Discussion addressing the relationship between the observed scaling exponents and the choice of theoretical framework.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Generalizability
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The authors note that their findings are relevant to natural IDPs but do not discuss potential limitations of the E-K model system, such as the absence of hydrophobic or aromatic interactions that are common in natural IDPs.
- **Required correction** Add a sentence acknowledging the limitations of the model system and how the framework might be extended to more complex sequences.

### Technical failings that need to be addressed before the case is established
- R1-M1: Quantitative validation of the sticky Rouse model predictions is insufficient. The model is fitted to the data it is claimed to predict.
- R1-M2: The interpretation of scaling exponents as indicating a crossover regime is not statistically rigorous and appears to conflict with the dismissal of entanglement corrections.
- R1-M3: The phenomenological model for contact lifetimes lacks physical justification and demonstrated transferability.

### Assessment against Nature-style criteria
- **Originality** The application of the sticky Rouse model to condensate dynamics, with contact lifetimes as the key sequence-dependent parameter, is a novel contribution. The distinction between vector and distance relaxation times for experimental interpretation is also original.
- **Scientific importance** The question of how sequence controls material properties is of high importance for understanding condensate biology and for engineering synthetic condensates. A predictive framework would be valuable.
- **Interdisciplinary readership** The work bridges polymer physics, computational biophysics, and cell biology. The conceptual framework is accessible, but the technical details may limit readership to specialists.
- **Technical soundness** The simulation methodology is appropriate and well-described. However, the statistical validation of the central predictive claims is insufficient, and the model fitting procedure raises concerns about overfitting.
- **Readability for nonspecialists** The main text is generally clear, but the Results section assumes familiarity with polymer theory concepts. The distinction between the standard and sticky Rouse models could be explained more explicitly for a broader audience.

### Recommendation posture
Supportive if technical concerns are resolved. The conceptual framework is promising and the simulation data appear to be of high quality. However, the central claim of quantitative prediction requires more rigorous validation, and the interpretation of the scaling exponents needs to be reconciled with the model selection. If the authors can provide held-out validation, quantitative error metrics, and a clearer physical justification for the contact lifetime model, the paper would make a strong contribution.