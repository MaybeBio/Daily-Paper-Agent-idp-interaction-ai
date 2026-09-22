## Review setup
- **Input scope** Full manuscript text including abstract, main text, methods, and figure references
- **Assessment boundary** Scientific content, methodological rigor, validity of conclusions, and suitability for the stated journal scope
- **Shared manuscript claim summary** The authors evaluate 20 molecular dynamics force field models for simulating the intrinsically disordered protein COR15A, validate the best six against SAXS and NMR data, and identify DES-amber as the most accurate model for capturing both structure and dynamics, including subtle differences between wild-type and a G68A mutant.
- **Visible evidence base** Abstract, full main text, methods section, figure and table references, supplementary figure references
- **Missing materials affecting confidence** Actual figures and tables are not provided; supplementary figures referenced but not available; experimental NMR data files not accessible; specific numerical values for key comparisons are not fully detailed in text

## Reviewer
- **Overall assessment** This manuscript presents a systematic and comprehensive force field validation study for a challenging IDP system. The two-step approach of initial screening followed by extended simulations is well designed. The inclusion of dynamics validation via NMR relaxation is a notable strength that goes beyond typical structural comparisons. However, the manuscript would benefit from clearer presentation of quantitative results and a more critical discussion of the limitations of the validation metrics used. The conclusion that DES-amber is the best-performing model is supported by the evidence presented, but the generalizability of this finding to other IDPs remains uncertain.

- **Who would be interested in the results, and why** Researchers in the molecular dynamics simulation community, particularly those working on force field development and validation for IDPs. Also relevant to experimentalists studying COR15A and other LEA proteins who use simulations to interpret their data. The methodological framework for combining SAXS and NMR validation could be of interest to the broader biophysics community studying disordered proteins.

- **Major strengths** 1) Comprehensive evaluation of 20 force field models, which is more extensive than most validation studies. 2) Two-tier validation approach that first screens broadly then validates deeply is efficient and well reasoned. 3) Inclusion of dynamics validation via NMR relaxation times at two field strengths is a significant methodological advance. 4) The use of a point mutant with known subtle structural differences provides a stringent test of force field sensitivity. 5) The study addresses an important gap in force field validation for IDPs that undergo conformational changes.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that "only DES-amber and ff99SBws capture helicity differences between wild-type and mutant, but ff99SBws overestimates helicity" and that DES-amber is the best model overall.
  - **Evidence pointer** Figure 3, Figure S14, location not provided
  - **Concern** The quantitative criteria for determining whether a force field "captures" the helicity difference are not clearly defined. The manuscript states that DES-amber "precisely capture[d] the small helicity difference" but does not provide statistical measures of agreement or uncertainty estimates for the per-residue helicity comparisons. Without defined thresholds or statistical tests, the ranking of force fields appears somewhat subjective.
  - **Why it matters** The central conclusion of the paper depends on the ability to distinguish between force fields that adequately capture subtle structural differences and those that do not. Without quantitative criteria, the ranking cannot be independently assessed or reproduced by other researchers.
  - **Resolution test** Provide quantitative metrics such as root-mean-square deviation between simulated and experimental per-residue helicity, with confidence intervals. Define a priori thresholds for what constitutes acceptable agreement. Consider statistical tests to determine whether differences between force fields are significant given the simulation uncertainty.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors state that "DES-amber was the only model that yielded good results for both magnetic fields" and that it "adequately reproduces the COR15A dynamics, as assessed by NMR relaxation times at two different magnetic field strengths."
  - **Evidence pointer** Figure 5, Figures S18-S20, location not provided
  - **Concern** The comparison of simulated and experimental NMR relaxation parameters is presented qualitatively. The manuscript does not provide quantitative measures of agreement such as chi-squared values, correlation coefficients, or reduced residuals for T1, T2, and hetNOE comparisons. The statement that DES-amber performs well at both field strengths while others do not requires quantitative support.
  - **Why it matters** NMR relaxation parameters are sensitive probes of dynamics, and the claim that only one force field captures dynamics at both field strengths is a strong statement. Without quantitative metrics, it is difficult to assess whether the differences between force fields are meaningful or within simulation uncertainty.
  - **Resolution test** Provide quantitative agreement metrics for T1, T2, and hetNOE comparisons at both field strengths for all six force fields. Include uncertainty estimates from the 10 independent trajectories. Consider reduced chi-squared statistics that account for experimental errors.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The authors claim that "our work pioneers the use of ensemble dynamics in comprehensive force field comparison studies on IDPs."
  - **Evidence pointer** Introduction, Discussion, location not provided
  - **Concern** While the inclusion of dynamics validation is commendable, the claim of "pioneering" may be overstated. Previous force field comparison studies have included dynamics validation, albeit perhaps not as comprehensively. The novelty lies more in the combination of approaches and the specific system studied rather than in the use of ensemble dynamics per se.
  - **Why it matters** Overstating novelty can undermine the credibility of the work and may invite unnecessary criticism. The scientific contribution is already significant without this claim.
  - **Resolution test** Soften the novelty claim and more carefully situate the work within the existing literature on force field validation for IDPs, acknowledging prior studies that have included dynamics validation.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** The authors state that "improving solvation via adapted water models seems to work better than attenuating protein-protein interactions" based on the comparison of force field performance.
  - **Evidence pointer** Figures 1-2, location not provided
  - **Concern** This conclusion is drawn from comparing force fields that differ in multiple aspects simultaneously (protein parameters, water model, and interaction terms). The manuscript does not isolate the specific contribution of water model improvements versus protein parameter modifications. The CUFIX force fields, which attenuate protein-protein interactions, also use different protein parameters than the other tested models.
  - **Why it matters** The mechanistic interpretation of why certain force fields perform better is important for guiding future force field development. Without isolating variables, the conclusion may be premature.
  - **Resolution test** Acknowledge the confounding variables more explicitly. Consider additional simulations that isolate specific parameter changes, or temper the conclusion to reflect the uncertainty in attributing performance differences to specific parameter modifications.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Abstract
  - **Evidence pointer** Abstract, location not provided
  - **Issue** The abstract is dense and assumes significant background knowledge about force field nomenclature and IDP simulation challenges. Terms like "DES-amber" and "ff99SBws" are introduced without context.
  - **Required correction** Briefly explain what these force field names represent (e.g., "the DES-amber model, which modifies protein-water interactions") to make the abstract more accessible to a broader readership.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Methods, NMR relaxation calculations
  - **Evidence pointer** Experimental Section, location not provided
  - **Concern** The description of how NMR relaxation parameters were calculated from simulations is brief. The manuscript states that the spectral density was obtained via "regularized inverse Laplace transformation" but does not provide details on the regularization parameter choice or validation of this approach.
  - **Required correction** Provide additional details on the inverse Laplace transformation procedure, including the regularization method and any validation against known analytical solutions.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Results, SAXS analysis
  - **Evidence pointer** Figure 2, location not provided
  - **Concern** The manuscript mentions that four force fields achieved chi-squared values of 10 or less for SAXS profile agreement, but does not provide the actual chi-squared values for all 20 force fields. This would be useful for readers to assess the full range of performance.
  - **Required correction** Include a table or supplementary figure showing chi-squared values for all 20 force field models.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Discussion of directional correlation
  - **Evidence pointer** Results section, Figure 6, location not provided
  - **Concern** The concept of "directional correlation of Cα vectors" is introduced without sufficient explanation of what this metric physically represents and why it is informative for IDP dynamics.
  - **Required correction** Add a brief explanation of what directional correlation measures and how it relates to chain stiffness or conformational preferences.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Methods, simulation setup
  - **Evidence pointer** Experimental Section, Table 1, location not provided
  - **Concern** The manuscript does not report the ionic strength used in the simulations, despite acknowledging that ionic strength could affect the results. The statement that "minor ionic strength differences between simulations and experiments should not substantially impact the results" is not supported by a control simulation or sensitivity analysis.
  - **Required correction** Report the ionic strength in the simulations and either provide justification for why it should not affect the results or include a sensitivity analysis.

  - **Concern ID** R1-m6
  - **Severity** Minor
  - **Axis** Scientific importance
  - **Affected element** Discussion
  - **Evidence pointer** Discussion section, location not provided
  - **Issue** The discussion of the biological implications of the findings for COR15A function is limited. The authors mention that the G68A mutation affects helicity and dynamics but do not discuss what this might mean for the protein's function in freezing tolerance.
  - **Required correction** Add a brief paragraph discussing the potential functional implications of the observed structural and dynamic differences between wild-type and mutant COR15A.

- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative criteria for helicity comparison), R1-M2 (quantitative metrics for NMR relaxation agreement)

## Risk / unsupported claims
- The claim that DES-amber is the "best" force field for COR15A is supported by the presented evidence but is limited to this specific protein and the tested conditions. Generalization to other IDPs is not warranted from this study alone.
- The statement that "improving solvation via adapted water models seems to work better than attenuating protein-protein interactions" is not fully supported because the force field comparisons do not isolate these variables.
- The claim of "pioneering" use of ensemble dynamics in force field comparison studies is potentially overstated and not fully supported by the literature review presented.
- The assertion that the G68A mutation "locally affects molecular motions with time scales slower than about 10 ns" is based on simulated data from a single force field (DES-amber) and cannot be verified experimentally due to data limitations.
- The statement that "relying solely on chemical shifts is not sufficient for force field evaluation" is supported by the data but is presented as a general conclusion from a single protein system.