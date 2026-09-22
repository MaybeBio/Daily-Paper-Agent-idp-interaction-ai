## Review setup

- **Input scope** Full manuscript text, including main text, appendices, and figure captions as provided.
- **Assessment boundary** Scientific content, theoretical derivation, computational methodology, data interpretation, and claims as presented in the provided material. No external literature or supplementary information was consulted.
- **Shared manuscript claim summary** The authors propose a residue-accessibility parameter (RAP) derived from a perturbed mean-field Flory-Huggins theory that incorporates a correlation-hole repulsion between polymer centers of mass. They claim that RAP quantitatively captures the sequence dependence of critical temperatures for phase separation in two-letter polymer solutions, as validated against extensive Monte Carlo simulations.
- **Visible evidence base** Main text (Sections I–IV), Appendices A–C, and references to Figures 1–4. Simulation details and derivations are partially provided.
- **Missing materials affecting confidence** Figure contents are not directly viewable; only captions are referenced. Simulation data files and code are mentioned but not included. The exact form of the interaction potential and the fitting procedure for the parameter C_K are not fully detailed in the visible text.

## Reviewer

- **Overall assessment** The manuscript addresses a timely and important problem: understanding how sequence encodes phase behavior in biopolymers. The authors propose a physically motivated, analytically tractable correction to mean-field theory that yields a single scalar parameter (RAP) claimed to collapse sequence-dependent critical temperature data. The idea is elegant and the potential impact is high. However, the manuscript as presented has several gaps that prevent full assessment of the central claims. The derivation is phenomenological and relies on assumptions that are not fully justified. The validation against simulations is described but the quantitative quality of the collapse (e.g., residuals, error bars) is not presented in the text. The claim that RAP reduces the dimensionality of the sequence problem from 2^N to 1 is strong and requires more careful statistical testing. The writing is generally clear but some technical details are missing. Overall, the work is promising but the case is not yet fully established from the provided material.

- **Who would be interested in the results, and why** Researchers in biophysics, soft matter physics, and polymer science, particularly those studying intrinsically disordered proteins, phase separation, and condensate biology. The work offers a simple, interpretable parameter that could aid in predicting sequence-dependent phase behavior, which is of direct relevance to experimentalists designing sequences with tunable phase properties and to theorists seeking coarse-grained descriptions of sequence-encoded behavior.

- **Major Strengths**
  1. The central idea is novel and physically intuitive: connecting residue accessibility to sequence-dependent interaction strengths via a correlation-hole argument.
  2. The theoretical framework is minimal and analytically tractable, offering a clear departure from purely computational or purely empirical approaches.
  3. The validation against a large simulation dataset (2408 data points) is a significant effort and lends credibility to the approach.
  4. The manuscript is well-structured and the writing is accessible, with clear motivation and a logical flow from theory to results.

- **Major Concerns**

  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Theoretical justification
  - **Claim pointer** The authors claim that the correlation-hole repulsion, modeled via a phenomenological kernel K(r), quantitatively captures the sequence dependence of critical temperatures.
  - **Evidence pointer** Section II, Equations (6), (9), and (10); Appendix C.
  - **Concern** The derivation of Equation (9) relies on a hierarchy of length scales (ℓ_U ≪ ℓ_ch ≪ σ_i) and on the assumption that the polymer internal structure remains Gaussian and uncorrelated when conditioned on the CM separation. The authors acknowledge that ℓ_ch and σ_i both scale as N^{1/2}b, which undermines the strict hierarchy. The leading-order result may therefore be uncontrolled. Moreover, the form of K(r) is not specified beyond its scaling; the derivation is explicitly phenomenological. It is unclear how sensitive the final expression for RAP is to the specific choice of K(r) and whether other reasonable choices would yield qualitatively different predictions.
  - **Why it matters** The central theoretical claim rests on this derivation. If the approximation is not controlled, the agreement with simulations may be fortuitous or specific to the chosen form of K(r). The manuscript does not provide a sensitivity analysis or a more rigorous justification for the leading-order truncation.
  - **Resolution test** The authors should either (a) provide a more rigorous derivation that justifies the hierarchy, perhaps by computing the next-order correction and showing it is small, or (b) test the robustness of the RAP prediction against different functional forms of K(r) (e.g., different decay profiles) and show that the qualitative conclusions are unchanged.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Validation strength
  - **Claim pointer** The authors claim that RAP strongly correlates with critical temperatures across thousands of two-letter chains of varying length, composition, and solvent quality.
  - **Evidence pointer** Section III, Figure 4.
  - **Concern** The manuscript states that the data collapse in Figure 4 is a "reasonable fit" with R² = 0.63, but no further statistical analysis is provided. A correlation of 0.63, while non-trivial, leaves substantial unexplained variance. The authors do not report residuals, confidence intervals, or a comparison against simpler predictors (e.g., composition alone, blockiness, or single-chain parameters). The claim of dimensionality reduction from 2^N to 1 is strong and requires a more rigorous demonstration that RAP outperforms existing descriptors.
  - **Why it matters** The practical utility of RAP depends on its predictive power relative to existing, simpler metrics. Without a comparative analysis, it is unclear whether RAP adds genuine value or merely repackages known correlations.
  - **Resolution test** The authors should provide a more detailed statistical analysis, including: (a) residuals plotted against sequence features (e.g., blockiness, composition) to identify systematic deviations; (b) a comparison of RAP against existing single-chain predictors (e.g., sequence charge decoration, hydropathy decoration) in terms of correlation with T_c; (c) cross-validation or out-of-sample testing to assess predictive power.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scope of validation
  - **Claim pointer** The authors claim that RAP may be effective for predicting sequence dependence of phase diagrams for any polymer length, monomer type set, and polymer mixtures.
  - **Evidence pointer** Section IV, Discussion.
  - **Concern** The validation is limited to two-letter polymers on a lattice with a specific interaction scheme. The generalization to multi-letter systems, off-lattice models, and mixtures is asserted but not demonstrated. The authors note that some sequences exhibit micellization or microphase separation, which are excluded from the analysis, but the boundary of applicability of RAP is not clearly delineated.
  - **Why it matters** The stated scope of the claim extends well beyond the tested systems. Without evidence of transferability, the claim is speculative.
  - **Resolution test** The authors should either (a) temper the claim to reflect the tested systems, or (b) provide preliminary evidence (e.g., simulations of three-letter systems or off-lattice models) that RAP remains predictive.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Reproducibility
  - **Claim pointer** The authors state that simulation codes and data are freely available.
  - **Evidence pointer** Appendix A, Data Availability.
  - **Concern** The manuscript mentions a GitHub repository and a DOI for simulation codes, but the exact version of the code, the simulation parameters (e.g., box sizes, number of independent runs, equilibration times), and the criteria for identifying critical points are not fully specified in the text. The reproducibility of the 2408 data points is therefore difficult to assess.
  - **Why it matters** Reproducibility is a cornerstone of scientific claims. Without full details, independent verification is hindered.
  - **Resolution test** The authors should provide a more detailed description of the simulation protocol in the main text or appendix, including all relevant parameters and the criteria for determining critical points.

- **Minor Comments**

  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Equation (4) and surrounding text
  - **Evidence pointer** Section II, Equation (4).
  - **Issue** The definition of the rescaled critical temperature T̃_c is given but the physical interpretation of the rescaling is not fully explained. It would help to state explicitly that T̃_c = 1 corresponds to the mean-field prediction and that deviations reflect non-mean-field effects.
  - **Required correction** Add a sentence clarifying the interpretation of T̃_c.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Presentation
  - **Affected element** Figure 2 and Figure 4
  - **Evidence pointer** Section III, Figures 2 and 4.
  - **Issue** The manuscript states that Figure 2 shows data for N=8 and N=24 only, but the full dataset spans N=8, 12, 14, 18, 24. It is unclear why intermediate lengths are omitted from the figure. Additionally, the color coding and symbols in the figures are not described in the captions.
  - **Required correction** Clarify the selection of data shown in Figure 2 and describe the symbols/colors in the captions.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical detail
  - **Affected element** Appendix A
  - **Evidence pointer** Appendix A.
  - **Issue** The description of the grand canonical Monte Carlo simulation is brief. The Rosenbluth scheme for chain insertion/deletion is mentioned, but the specific implementation (e.g., how the athermal Rosenbluth weight is computed) is not detailed.
  - **Required correction** Provide a more detailed description of the simulation algorithm, or cite a reference where the method is fully described.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Language
  - **Affected element** Section III, first paragraph
  - **Evidence pointer** Section III.
  - **Issue** The phrase "validy" appears to be a typo for "validity."
  - **Required correction** Correct the typo.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Section IV, Discussion
  - **Evidence pointer** Section IV.
  - **Issue** The discussion of blind spots of RAP is brief. The example of reverse-complement symmetry is interesting but the implications for practical use are not explored.
  - **Required correction** Expand the discussion of limitations, perhaps with a concrete example of a sequence pair that RAP cannot distinguish.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: The uncontrolled nature of the leading-order approximation in the derivation of Equation (9).
  - R1-M2: The lack of a rigorous statistical comparison of RAP against existing predictors.
  - R1-M3: The overextension of claims beyond the tested systems.
  - R1-M4: Insufficient detail for full reproducibility of the simulation data.

- **Assessment against Nature-style criteria**
  - **Originality** High. The concept of a residue-accessibility parameter derived from correlation-hole physics is a novel contribution to the field of sequence-dependent phase behavior.
  - **Scientific importance** High. If validated, RAP could provide a simple, interpretable tool for predicting phase behavior of disordered proteins and other polymers, with implications for understanding biological condensates.
  - **Interdisciplinary readership** Moderate to high. The work bridges polymer physics, biophysics, and computational chemistry, and the conceptual message is accessible to a broad audience.
  - **Technical soundness** Currently insufficient. The theoretical derivation is not fully controlled, and the validation is not statistically rigorous. These issues must be resolved before the claims are fully supported.
  - **Readability for nonspecialists** Good. The manuscript is well-written and the main ideas are clearly explained. The technical appendices are appropriately relegated to the end.

- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the work addresses an important problem. However, the current manuscript does not fully establish the central claims due to the concerns outlined above. The authors should address the theoretical justification, strengthen the statistical validation, and temper the scope of their claims.