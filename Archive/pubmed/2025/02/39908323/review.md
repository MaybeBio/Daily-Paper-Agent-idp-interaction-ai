## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, methods, results, discussion, and conclusion. No supplementary material, figures, or tables were provided.
- **Assessment boundary** Scientific content, methodological soundness, and claims as presented in the text. No assessment of formatting, grammar, or editorial style.
- **Shared manuscript claim summary** The authors present COCOMO2, an updated residue-based coarse-grained model that extends the original COCOMO model from intrinsically disordered proteins to folded proteins via a surface exposure scaling factor (λ). The model is parametrized directly against solubility and phase separation data, and is claimed to improve prediction of concentration-dependent phase separation and single-chain properties across a range of systems.
- **Visible evidence base** Text descriptions of methods and results, including references to figures (Figures 1–7), tables (Tables 1–2, S1–S11), and equations (eqs 1–9). No actual data, figures, or tables were available for direct inspection.
- **Missing materials affecting confidence** All figures, tables, and supplementary materials. Numerical values for parameters, fitting coefficients, and statistical measures (e.g., RMSD, χ²) are referenced but not shown. This significantly limits the ability to independently verify quantitative claims.

## Reviewer
- **Overall assessment** The manuscript describes a useful and timely extension of a coarse-grained model for biomolecular phase separation, addressing a clear gap in the field. The conceptual approach, particularly the use of a surface exposure scaling factor and direct parametrization against phase separation data, is sensible and potentially impactful. However, the provided text alone does not allow for verification of the quantitative results, and several methodological details and claims require closer scrutiny. The work appears promising but is not fully established from the supplied material.
- **Who would be interested in the results, and why** Researchers in computational biophysics, specifically those studying biomolecular condensates, phase separation, and coarse-grained simulation methods. The work is also relevant to experimentalists studying LLPS who seek computational tools for interpreting and predicting phase behavior. The methodological advance of parametrizing against phase separation data could be of broad interest to the simulation community.
- **Major strengths**
  1. The extension of COCOMO to folded proteins addresses a significant limitation of the original model and fills a clear niche in the coarse-grained modeling landscape.
  2. The introduction of a surface exposure scaling factor is a physically motivated and computationally efficient solution to a known problem.
  3. Direct parametrization against experimental phase separation and solubility data is a notable departure from common practice and could improve predictive accuracy.
  4. The use of a linear relationship between potential energy and log(csat) to guide parametrization is an elegant and potentially generalizable idea.
  5. The model is benchmarked against a range of systems, including IDPs, multidomain proteins, heterotypic systems, and protein-RNA systems, suggesting broad applicability.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence quality
  - **Claim pointer** The claim that COCOMO2 improves prediction of csat and Rg values compared to the original COCOMO is central to the paper.
  - **Evidence pointer** Figures 2, 4, 6; Tables 2, S10, S11; location not provided
  - **Concern** The quantitative evidence supporting the central claims is not visible in the provided text. RMSD and χ² values are cited, but the underlying data, plots, and statistical analyses are not available for inspection. Without seeing the actual comparisons between predicted and experimental values, it is impossible to assess the magnitude of improvement or whether the claims are justified.
  - **Why it matters** The core value proposition of the paper is improved predictive accuracy. If the evidence is not verifiable, the central claims cannot be accepted.
  - **Resolution test** Provide the actual figures and tables with clear comparisons between experimental and predicted values, including error bars and statistical significance tests where appropriate.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Methodological rigor
  - **Claim pointer** The parametrization strategy relies on a linear relationship between potential energy and log(csat) (eq 9), which is used to estimate csat without running full phase separation simulations.
  - **Evidence pointer** Methods section "Parameter Optimization Process"; Figures 5, S9, S10; location not provided
  - **Concern** The validity of the linear relationship between potential energy and log(csat) is asserted but not rigorously demonstrated. The text mentions outliers and the use of RANSAC, but the quality of the fits, the range of validity, and the sensitivity of the results to this assumption are not discussed in sufficient detail. The approach could introduce systematic biases that are not accounted for.
  - **Why it matters** If the linear approximation is not robust, the optimized parameters could be biased, undermining the model's predictive power.
  - **Resolution test** Show the actual fits for all training systems, including the scatter of data points, the RANSAC-selected inliers, and the residuals. Discuss the limitations of the approach and potential sources of systematic error.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scope of validation
  - **Claim pointer** The claim that COCOMO2 is suitable for studying complex assembly processes and can be extended to specific interactions via knowledge-based potentials.
  - **Evidence pointer** Discussion section; location not provided
  - **Concern** The claim about applicability to complex assembly processes is speculative and not supported by any data presented in the text. The suggestion that knowledge-based potentials can be added is plausible but untested. The paper would be strengthened by either including preliminary data on such systems or clearly framing these as future directions rather than current capabilities.
  - **Why it matters** Overstating the model's capabilities could mislead potential users and detract from the solid contributions of the work.
  - **Resolution test** Either add preliminary results on assembly processes or temper the language to clearly indicate these are untested future possibilities.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Comparison with existing methods
  - **Claim pointer** The manuscript compares COCOMO2 to CALVADOS3, noting differences in design philosophy and performance.
  - **Evidence pointer** Discussion section; location not provided
  - **Concern** The comparison with CALVADOS3 is brief and qualitative. The text states that CALVADOS3 predicts csat with similar deviation for multidomain proteins, but no direct quantitative comparison is shown. Given that CALVADOS3 is a key competing model, a more thorough head-to-head comparison would strengthen the case for COCOMO2's utility.
  - **Why it matters** Without a clear quantitative comparison, it is difficult for readers to decide which model is more appropriate for their needs.
  - **Resolution test** Include a direct comparison of csat and Rg predictions for the same set of test systems, with appropriate metrics and discussion of trade-offs.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Methods section "Coarse-Grained Model"
  - **Evidence pointer** Equation 6; location not provided
  - **Issue** The description of the surface exposure scaling factor λ is somewhat terse. The relationship between Sratio, λ, and the resulting interaction strength could be explained more intuitively.
  - **Required correction** Add a brief explanatory paragraph or schematic describing how λ affects the interaction strength for different types of residues (e.g., fully buried, partially exposed, fully exposed).
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods section "Molecular Dynamics Simulations"
  - **Evidence pointer** Location not provided
  - **Issue** The simulation protocol is described, but some details are missing, such as the specific barostat/thermostat settings (if any), the treatment of long-range electrostatics, and the criteria for determining equilibration.
  - **Required correction** Provide a more complete description of the simulation setup to ensure reproducibility.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** Throughout
  - **Evidence pointer** Location not provided
  - **Issue** The term "csat" is used for both saturation concentration and critical concentration. While related, these can be conceptually distinct in some contexts.
  - **Required correction** Clarify the distinction or use consistent terminology throughout.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Results section "Further Evaluation of COCOMO2"
  - **Evidence pointer** Figure 7; location not provided
  - **Issue** The heterotypic phase separation test is described, but the quantitative results are not presented in the text. It is unclear how the conclusion of "consistent with experimental results" is reached.
  - **Required correction** Include the relevant quantitative data or a clear reference to the figure showing the results.
- **Technical failings that need to be addressed before the case is established** R1-M1 and R1-M2 are the primary technical concerns. The lack of visible quantitative data prevents verification of the central claims, and the validity of the linear approximation for csat estimation needs to be more rigorously demonstrated.
- **Assessment against Nature-style criteria**
  - **Originality** The work presents a novel combination of ideas: extending a coarse-grained model to folded proteins via surface exposure scaling and parametrizing directly against phase separation data. This is a meaningful contribution, though the individual components are not entirely new.
  - **Scientific importance** The ability to model interactions between folded and disordered proteins is important for understanding phase separation and complex assembly. The work addresses a real need in the field.
  - **Interdisciplinary readership** The work is primarily of interest to computational biophysicists and physical chemists. It may also appeal to experimentalists studying phase separation, but the technical nature of the methods may limit broader readership.
  - **Technical soundness** The methodological approach is sound in principle, but the lack of verifiable quantitative evidence and the potential limitations of the linear approximation for csat estimation are concerns that must be addressed.
  - **Readability for nonspecialists** The manuscript is generally well-written and accessible to a technical audience. The introduction and discussion provide good context. However, some methodological details could be explained more clearly for nonspecialists.
- **Recommendation posture** Supportive if technical concerns are resolved. The work addresses a relevant problem and presents a plausible solution, but the evidence base must be made available and the methodological assumptions more rigorously validated before the claims can be fully accepted.

## Risk / unsupported claims
- The claim that COCOMO2 provides "significant improvements in accuracy" for phase separation and single-chain properties is not verifiable from the provided text, as the quantitative data are not shown.
- The claim that the linear relationship between potential energy and log(csat) is a reliable proxy for estimating csat is not sufficiently demonstrated.
- The claim that COCOMO2 is suitable for studying complex assembly processes is speculative and not supported by data.
- The comparison with CALVADOS3 is qualitative and lacks direct quantitative evidence.
- The statement that COCOMO2 "agrees qualitatively with the experiment for three out of the four systems" for protein-RNA phase separation is not supported by visible data.