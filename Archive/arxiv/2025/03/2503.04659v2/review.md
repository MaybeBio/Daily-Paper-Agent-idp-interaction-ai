## Review setup
- **Input scope** Full manuscript text including main text, appendices, and supplemental information descriptions
- **Assessment boundary** Scientific validity, methodological rigor, claims substantiation, and presentation quality of the reported work
- **Shared manuscript claim summary** The authors propose that statistical features derived from two-chain contact maps, particularly the contact-map variance, can predict heteropolymer phase separation more accurately than traditional metrics such as Rg and B22, and demonstrate this across a minimal hydrophobic-polar copolymer model and a chemically specific coarse-grained IDP model
- **Visible evidence base** Main text figures (Figures 1-6), appendices describing simulation models, phase behavior classification, contact-map construction, and logistic regression methodology; supplemental information descriptions
- **Missing materials affecting confidence** Actual figure data, numerical values underlying plots, full simulation parameters, code availability verification, and complete dataset details

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting and potentially useful approach for predicting heteropolymer phase separation using contact-map statistics derived from two-chain simulations. The central idea, that spatial information in interchain contact maps contains predictive power beyond scalar metrics like B22, is well motivated and the results are presented clearly. However, several technical concerns regarding the statistical methodology, the interpretation of the contact-map variance, and the generalizability claims require careful consideration before the case is fully established.

- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, polymer physics, and computational biophysics would find this work relevant. The approach offers a computationally efficient alternative to full phase diagram calculations and could be useful for screening large sequence libraries. The methodological framework may also interest those developing machine learning approaches for biomolecular phase behavior prediction.

- **Major strengths** The manuscript addresses a timely and important problem in the prediction of biomolecular phase separation. The use of two-chain simulations to extract predictive features is computationally efficient and physically grounded. The demonstration across two different model systems, from a minimal HP model to a chemically specific IDP model, strengthens the generalizability argument. The systematic comparison with traditional metrics and the careful attention to statistical validation through repeated train-test splits are commendable.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Statistical methodology
  - **Claim pointer** The claim that contact-map variance "significantly outperforms" Rg and B22 in predicting phase separation
  - **Evidence pointer** Figure 3, Appendix D
  - **Concern** The logistic regression models are evaluated using AUC from randomized 80/20 train-test splits. However, the manuscript does not report the number of samples in each dataset relative to the number of features used, nor does it address potential class imbalance issues beyond noting AUC robustness. More critically, the comparison between models with different numbers of features (e.g., univariate vs. bivariate) may be confounded by model complexity. The manuscript should report confidence intervals for AUC differences and perform statistical significance testing between models rather than relying on overlapping standard errors.
  - **Why it matters** Without proper statistical comparison, the claim that contact-map variance outperforms traditional metrics may not be rigorously supported. The practical utility of the approach depends on demonstrating that the improvement is statistically meaningful and not an artifact of the specific dataset or model selection procedure.
  - **Resolution test** Provide formal statistical tests (e.g., DeLong test for correlated AUCs) comparing model performances, report sample sizes and feature counts, and demonstrate that the observed AUC differences are robust across multiple random seeds and cross-validation schemes.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Interpretation of contact-map variance
  - **Claim pointer** The interpretation that higher contact-map variance indicates "hot spots" that stabilize finite-sized clusters rather than phase separation
  - **Evidence pointer** Section II.2, Section III
  - **Concern** The physical interpretation of the contact-map variance as a predictor of phase separation versus aggregation is not fully developed. The manuscript states that higher variance tends to be associated with aggregation, but the mechanistic explanation is speculative. The connection between contact-map variance and the microscopic interactions that drive phase separation versus cluster formation is not rigorously established. The authors should provide a more detailed physical rationale or additional analysis to support this interpretation.
  - **Why it matters** The interpretability of the approach is a key selling point. If the physical meaning of the contact-map variance is not clearly established, the approach risks being a black-box predictor without mechanistic insight, which would limit its utility for understanding sequence determinants of phase behavior.
  - **Resolution test** Provide additional analysis linking contact-map variance to specific interaction patterns, such as examining which types of monomer pairs contribute most to the variance in phase-separating versus aggregating sequences, or comparing contact-map variance to known structural features of the aggregates.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Generalizability claims
  - **Claim pointer** The claim that the approach is "transferable across different heteropolymer models" and "independent of the chemical details or coarse-graining resolution"
  - **Evidence pointer** Section II.4, Section III
  - **Concern** The generalizability claim is based on only two model systems: a minimal HP model and a single CG IDP model. The HP model has only two monomer types, while the IDP model has 20 amino acid types but is still a single coarse-graining scheme. The manuscript does not demonstrate transferability across different force fields, different coarse-graining resolutions, or different types of heteropolymers (e.g., nucleic acids, synthetic copolymers with different chemistries). The claim of model independence is therefore not adequately supported.
  - **Why it matters** The stated goal of providing a "transferable" method is central to the paper's significance. If the approach only works for these specific models, its practical utility is substantially reduced.
  - **Resolution test** Demonstrate the approach on at least one additional model system with different interaction chemistry or coarse-graining resolution, or provide a theoretical argument for why the contact-map statistics should be model-independent.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Contact-map construction details
  - **Claim pointer** The claim that contact maps are constructed from configurations within the PMF well
  - **Evidence pointer** Appendix C
  - **Concern** The definition of the PMF well as the range where u(r) is within 1 kBT (HP model) or 0.4 kJ/mol (IDP model) of the minimum appears arbitrary. The manuscript does not justify these specific thresholds or demonstrate that the results are robust to this choice. Additionally, the number of configurations sampled (at least 2400) and the criteria for decorrelation are not fully specified.
  - **Why it matters** The contact-map statistics are the core of the proposed method. If the construction is sensitive to arbitrary parameter choices, the reliability and reproducibility of the approach are compromised.
  - **Resolution test** Perform a sensitivity analysis varying the PMF well definition and the number of configurations, and demonstrate that the predictive performance is stable across reasonable parameter ranges.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Presentation
  - **Affected element** Figure 3
  - **Evidence pointer** Figure 3
  - **Issue** The figure panels are not described in sufficient detail in the text. The reader cannot easily determine which specific models and features correspond to each panel without referring back and forth between text and figure.
  - **Required correction** Add explicit panel references in the text and provide more detailed figure captions describing the exact models, features, and datasets used in each panel.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Methodology
  - **Affected element** Appendix D
  - **Evidence pointer** Appendix D
  - **Issue** The regularization parameter λ = 6.0 × 10⁻⁵ is introduced for the B22-combined dataset but the justification for this specific value and the sensitivity of results to this choice are not discussed.
  - **Required correction** Provide a brief justification for the chosen regularization strength and report results for a range of λ values to demonstrate robustness.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Supplemental Information
  - **Evidence pointer** Supplemental Information
  - **Issue** The manuscript states that datasets are available at a GitHub repository, but the specific version of the code and data used for the reported results is not pinned or versioned.
  - **Required correction** Provide a specific version tag or commit hash for the repository, and consider archiving the code and data in a permanent repository such as Zenodo.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Interpretation
  - **Affected element** Section III
  - **Evidence pointer** Section III
  - **Issue** The discussion of potential applications to multicomponent mixtures is speculative and not supported by any preliminary results or analysis.
  - **Required correction** Either provide preliminary evidence for the extension to multicomponent systems or clearly label this as future work without implying feasibility.

- **Technical failings that need to be addressed before the case is established** R1-M1 (statistical comparison methodology), R1-M2 (physical interpretation of contact-map variance), R1-M3 (generalizability evidence)

- **Assessment against Nature-style criteria**
  - **Originality** The approach of using contact-map statistics from two-chain simulations as predictive features for phase separation is novel and represents a meaningful advance over using scalar metrics alone. The Fourier decomposition analysis adds a useful methodological contribution.
  - **Scientific importance** The problem of predicting phase separation from sequence is of significant current interest in the IDP and biomolecular condensate fields. A reliable and computationally efficient predictor would be valuable. However, the demonstrated scope is limited to two model systems.
  - **Interdisciplinary readership** The work bridges polymer physics, computational biophysics, and machine learning, and would appeal to researchers across these areas. The presentation is accessible to nonspecialists in each field.
  - **Technical soundness** The simulation methodology appears sound, but the statistical validation of the predictive models requires strengthening. The sensitivity of the contact-map construction to parameter choices needs to be addressed.
  - **Readability for nonspecialists** The manuscript is generally well-written and the logical flow is clear. The key concepts are introduced appropriately. Some figure descriptions could be improved for clarity.

- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the results are suggestive, but the statistical rigor of the model comparisons and the evidence for generalizability need to be strengthened before the claims can be fully accepted. The physical interpretation of the contact-map variance also requires more careful development.