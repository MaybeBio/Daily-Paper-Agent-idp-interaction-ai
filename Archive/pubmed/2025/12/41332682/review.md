## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv)
- **Assessment boundary** Scientific content, methodology, claims, and presentation as provided in the preprint. No line numbers were available; section and figure references are used.
- **Shared manuscript claim summary** The authors present a computational model combining coarse-grain polymer simulations of formin FH1 domains with a simplified kinetic model of actin polymerization. They investigate how N-terminal dimerization of FH1 domains affects binding site accessibility and local effective concentration at the FH2 domain, and consequently overall polymerization rates. They report four possible effects (acceleration/deceleration via accessibility/concentration changes), identify parameter regimes where each dominates, fit the model to published Bni1 experimental data, and make predictions for other formins.
- **Visible evidence base** Abstract, Introduction, Methods, Results, Discussion, Data Availability, Acknowledgements. Figures referenced but not fully described in text; Supplementary Material mentioned but not provided.
- **Missing materials affecting confidence** Figures 1–7 and Tables S1–S2 are referenced but not included in the provided text. Supplementary figures (S1–S4) and tables are not available. This limits verification of quantitative results, model outputs, and fitting quality.

## Reviewer
- **Overall assessment** This manuscript addresses a relevant and under-explored question in formin biology: the functional impact of N-terminal dimerization on FH1 domain dynamics and actin assembly. The authors develop a multiscale computational framework that is conceptually sound and clearly presented. The finding that N-terminal dimerization can either accelerate or decelerate polymerization depending on parameter regime and binding site location is interesting and potentially important. However, the manuscript has several technical and conceptual issues that need to be addressed before the case is fully established. The lack of included figures and supplementary materials significantly limits the ability to assess the strength of the evidence. The model fitting to experimental data appears preliminary, with acknowledged posterior multimodality. The treatment of the "off-center" delivery site and its implications for the model's conclusions requires more careful justification. Overall, the work is promising but currently not fully established from the provided evidence.

- **Who would be interested in the results, and why** Researchers studying formin-mediated actin polymerization, cytoskeletal dynamics, and intrinsically disordered protein function. The modeling approach may also interest computational biologists working on polymer physics and coarse-grain simulations of IDRs. The potential disease relevance (e.g., hypertrophic cardiomyopathy mutations in Fhod3) broadens the audience to cell biologists and clinicians interested in actin-related pathologies.

- **Major strengths** 
  1. Addresses a genuinely under-studied aspect of formin biology (N-terminal dimerization) with a clear and focused research question.
  2. The multiscale modeling approach (fast polymer dynamics + slow kinetics) is well-motivated and clearly explained.
  3. The identification of four distinct mechanistic effects of N-terminal dimerization provides a useful conceptual framework.
  4. The model is made accessible via public code repositories, supporting reproducibility.
  5. The discussion of how scientific illustrations may mislead conceptual understanding is thoughtful and relevant.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The manuscript claims specific quantitative results for how N-terminal dimerization impacts polymerization rates across parameter regimes and formin family members (Figures 2, 3, 5, 7).
- **Evidence pointer** Figures 2–7, Tables S1–S2, Figures S1–S4 (not provided)
- **Concern** The core quantitative results of the paper are presented in figures and supplementary materials that are not included in the provided manuscript text. Without these, it is impossible to evaluate the magnitude of the reported effects, the quality of the model fits, the validity of the parameter regimes explored, or the basis for cross-formin predictions.
- **Why it matters** The central claims of the paper are quantitative. The reader cannot assess whether the predicted accelerations/decelerations are biologically meaningful, whether the model fits the experimental data adequately, or whether the predictions for other formins are robust. This is a fundamental barrier to evaluating the manuscript's contribution.
- **Resolution test** Provide all figures and supplementary materials. The claims should be re-evaluated with the full visual and tabular evidence available.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Model validation
- **Claim pointer** The authors claim the model "can be fit to experimental data" using Bni1 single-binding-site constructs, and that best-fit parameters fall in a sensitive regime where capture and delivery compete.
- **Evidence pointer** Section "Single Binding Site Bni1 Experiments", Section "Parameter Learning and Model Evaluation", Figure 6, Figure S3
- **Concern** The model fitting is described as yielding a posterior distribution with "multiple regions of high likelihood" (Figure 6a), indicating that the data do not uniquely constrain the parameters. The authors acknowledge this but do not discuss its implications for the reliability of their predictions. The best-fit parameters are used for all subsequent cross-formin predictions, yet the uncertainty in these parameters is not propagated. The choice of a single experimental dataset (5 µM profilin) and the use of WebPlotDigitizer to extract data points introduce additional sources of error that are not addressed.
- **Why it matters** If the parameters are not well-constrained, the predictions for other formins (Figure 7) may be highly uncertain. The claim that the model can be "fit to experimental data" is weak if the fit is non-unique. The manuscript needs to address parameter identifiability and uncertainty propagation to support the predictive claims.
- **Resolution test** Perform a formal identifiability analysis (e.g., profile likelihoods or posterior predictive checks). Propagate parameter uncertainty through the cross-formin predictions and report credible intervals. Discuss the sensitivity of conclusions to the choice of experimental dataset and data extraction method.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Model assumptions
- **Claim pointer** The authors state that the "off-center" delivery site, based on a cryo-EM structure of Cdc12, supports a mechanism where N-terminal dimerization pulls FH1 density away from the delivery site.
- **Evidence pointer** Discussion section; reference to cryo-EM structure (ref 35)
- **Concern** The model uses a delivery site location at the FH1-FH2 attachment point in the main simulations, with the "off-center" location only discussed qualitatively. The authors acknowledge that using an off-center delivery site "may yield different results" but do not test this in the model. The cryo-EM structure is from Cdc12, not Bni1, and its relevance to the modeled system is not established.
- **Why it matters** The location of the delivery site is a critical geometric parameter in the model. If the off-center location is physiologically relevant, the model's predictions could change qualitatively. The current treatment leaves the model's conclusions potentially sensitive to an untested assumption.
- **Resolution test** Perform simulations with an off-center delivery site location and report how the results in Figures 2, 3, 5, and 7 change. Justify the choice of delivery site location for each formin modeled.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that for dimerized simulations of long FH1 domains (>200–300 amino acids), the Monte Carlo algorithm did not converge within computational constraints, but that "smooth big-picture trends" were observed.
- **Evidence pointer** Section "Coarse-Grain Polymer Model", Figures 2 and 3
- **Concern** The lack of convergence for long FH1 domains is a significant technical limitation. The authors use these non-converged results to draw conclusions about trends in the upper-right portions of Figures 2 and 3. The criterion for "smooth big-picture trends" is subjective and not quantified. The decision to limit predictions to FH1 domains of 400 amino acids or less is presented as a precaution, but the non-converged data still inform the qualitative conclusions.
- **Why it matters** If the polymer simulations are not converged, the derived parameters (accessibility, local effective concentration) may be inaccurate, which would propagate through the kinetic model and affect all downstream predictions. The manuscript needs to demonstrate that the non-converged results are reliable enough to support the qualitative claims.
- **Resolution test** Provide convergence diagnostics (e.g., trace plots, autocorrelation times, or comparison with longer runs for a subset of parameters). Quantify the uncertainty in the non-converged results and show that the qualitative conclusions are robust to this uncertainty.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Throughout
- **Issue** The term "local effective concentration" is used to describe the probability density Pri,0. While the authors define this, the term could be confused with other uses of "effective concentration" in the literature (e.g., in enzyme kinetics or molecular crowding).
- **Required correction** Consider using a more specific term, such as "binding site probability density at the delivery site," or explicitly state the definition at first use and in the abstract.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Model parameters
- **Evidence pointer** Section "Coarse-Grain Polymer Model", Section "Kinetic Model"
- **Issue** The manuscript does not provide a complete table of all model parameters, their values, and their sources. Some parameters (e.g., Kuhn length, FH2 domain width, binding site size) are mentioned, but a consolidated list would aid reproducibility.
- **Required correction** Add a table summarizing all model parameters, their values, and justifications (with references where applicable).

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Likelihood function
- **Evidence pointer** Equation (5)
- **Issue** The likelihood function is defined as a mean squared error normalized by SEM. This is not a standard likelihood and its statistical justification is unclear. It is not equivalent to a Gaussian likelihood unless the SEM is the same for all points.
- **Required correction** Clarify the statistical model underlying the likelihood. If a Gaussian likelihood is intended, write it explicitly. If a different error model is used, justify it.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion of disease relevance (e.g., Fhod3 mutations) is brief and not well-integrated with the model's predictions. The authors mention hypertrophic cardiomyopathy mutations but do not discuss how their model could inform understanding of these mutations.
- **Required correction** Expand the discussion of disease implications, or remove the brief mention if it is not substantively developed.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure references
- **Evidence pointer** Results section
- **Issue** The text frequently refers to "Figure 2 and Figure 3" and "Figure 5" without describing the specific panels or features being referenced. This makes the text difficult to follow without the figures.
- **Required correction** Add more specific references to panels (e.g., "Figure 2c") and briefly describe the key features in the text.

- **Technical failings that need to be addressed before the case is established** R1-M1 (missing evidence), R1-M2 (model validation and uncertainty), R1-M3 (untested delivery site assumption), R1-M4 (non-converged simulations).

- **Assessment against Nature-style criteria**
  - **Originality**: The question of N-terminal dimerization effects on FH1 dynamics is relatively unexplored, and the multiscale modeling approach is a novel contribution. However, the core modeling framework builds on existing work (Vavylonis et al., Bryant et al.), and the novelty lies primarily in the specific application.
  - **Scientific importance**: The work has potential importance for understanding formin regulation and IDR function. The finding that dimerization can have context-dependent effects (acceleration vs. deceleration) is conceptually interesting. However, the importance is currently limited by the lack of experimental validation and the preliminary nature of the fitting.
  - **Interdisciplinary readership**: The work bridges polymer physics, computational biology, and cell biology. It could appeal to readers in all three fields, but the presentation is likely most accessible to computational biologists. The biological implications are discussed but not deeply developed.
  - **Technical soundness**: The modeling approach is reasonable, but there are significant technical concerns: non-converged simulations for long FH1 domains, non-standard likelihood function, and lack of uncertainty propagation. These need to be addressed.
  - **Readability for nonspecialists**: The manuscript is generally well-written and the concepts are explained clearly. The abstract is accessible. However, the Methods section assumes familiarity with polymer physics and kinetic modeling, which may limit accessibility for a broad Nature readership.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an interesting question with a plausible modeling approach, but the current evidence is insufficient to fully establish the claims. The missing figures and supplementary materials are a major barrier. The model validation and uncertainty analysis need to be strengthened. If these issues are addressed, the work could be a valuable contribution to the field.