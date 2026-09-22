## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and supporting information references.
- **Assessment boundary** Scientific soundness, methodological validity, reproducibility, and alignment of claims with presented evidence. No assessment of editorial fit or publication decision.
- **Shared manuscript claim summary** The authors present two complementary numerical solvers (NMG and SAV) for the Cahn-Hilliard equation in Python, MATLAB, and Julia, and apply them to model the chromosomal passenger complex (CPC) as a phase-separating system on mitotic chromosomes. They claim that fully constrained Cahn-Hilliard simulations predict droplet spacing and dynamics consistent with experimental observations in HeLa and MCF10A-5E cells, supporting the hypothesis that CPC behaves as a simple Cahn-Hilliard fluid.
- **Visible evidence base** Abstract, full introduction, full results, full discussion, full materials and methods, figure legends referenced in text, supporting information references.
- **Missing materials affecting confidence** Figures and supporting information files (S1–S6, Movies S1–S3) are referenced but not provided. Raw data, code, and source data are available via external links but were not inspected. Statistical details for some comparisons (e.g., KS tests) are partially reported but effect sizes and confidence intervals are not fully described in text.

## Reviewer
- **Overall assessment** This manuscript presents a valuable methodological contribution by providing accessible, cross-language implementations of Cahn-Hilliard solvers tailored for biological applications. The application to the CPC is conceptually interesting and the authors make a reasonable effort to constrain model parameters with experimental data. However, the central claim that CPC behaves as a simple Cahn-Hilliard fluid is not fully established from the provided evidence. The manuscript would benefit from clearer articulation of the model's assumptions, more rigorous statistical comparisons between predictions and experiments, and additional validation of the parameter estimation procedure. The work is likely to interest researchers in systems biology, biophysics, and cell biology, but the current evidence base is insufficient to fully support the strong conclusions drawn.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates and phase separation, particularly those interested in quantitative modeling of subcellular organization. Computational biologists seeking accessible numerical tools for Cahn-Hilliard-type models will find the software packages useful. Cell biologists studying chromosome dynamics and the CPC may be interested in the proposed framework for understanding centromere localization. The cross-language implementation (Python, MATLAB, Julia) broadens the potential user base.
- **Major strengths** 1. The development of stable, self-consistent Cahn-Hilliard solvers in three widely used programming languages is a practical and valuable contribution. 2. The authors provide a clear relationship between the interfacial energy coefficient and critical droplet radius, which is useful for parameterizing future models. 3. The application to a specific biological system (CPC) with experimental data is commendable and demonstrates a pathway for using such models in cell biology. 4. The authors acknowledge limitations of the standard Cahn-Hilliard equation and discuss potential extensions.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Claim-evidence alignment
  - **Claim pointer** The authors claim that "the fully constrained Cahn-Hilliard simulations predicted spatiotemporal dewetting and coarsening behaviors that matched experiments in cell types with different interfacial energy coefficients."
  - **Evidence pointer** Results section, Figures 4–6, S4–S6; location not provided
  - **Concern** The claim of quantitative agreement between simulations and experiments is not supported by the evidence presented in the text. The authors report qualitative comparisons (e.g., "nearly superimposable" distributions) but do not provide statistical measures of agreement, such as goodness-of-fit tests, correlation coefficients, or explicit error metrics between predicted and measured droplet spacing distributions. The KS test is mentioned for comparing experimental distributions between cell types, but no comparable test is described for comparing model predictions to experimental measurements.
  - **Why it matters** The central scientific claim of the paper rests on the assertion that the model accurately predicts experimental observations. Without quantitative evidence of agreement, the claim that CPC behaves as a Cahn-Hilliard fluid is not established. The distinction between qualitative similarity and quantitative predictive accuracy is critical for the validity of the model as a test of phase separation.
  - **Resolution test** Provide explicit statistical comparisons between predicted and measured droplet spacing distributions (e.g., KS test, overlap coefficient, or Bayesian model comparison). Report effect sizes and confidence intervals for the agreement. If the model is intended to be predictive, demonstrate that predictions fall within experimental uncertainty for a held-out dataset.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Parameter identifiability
  - **Claim pointer** The authors state that "we constrained the interfacial energy coefficient by leveraging the general relationship between ϵm and Req" and estimate Req from the 95th percentile of non-inner centromere foci.
  - **Evidence pointer** Results section, Figure 4C–4D; location not provided
  - **Concern** The procedure for estimating Req from experimental data is not fully justified. The authors use the upper 95th percentile of non-inner centromere foci as an estimate of Req, but the rationale for this choice is not explained. It is unclear why the 95th percentile, rather than the maximum, mean, or another quantile, is appropriate. Additionally, the sensitivity of the resulting ϵm estimate to this choice is not assessed. The authors also do not report uncertainty in the Req estimate or propagate this uncertainty through to the model predictions.
  - **Why it matters** The model's predictions depend critically on the value of ϵm, which is derived from the Req estimate. If the Req estimation is arbitrary or highly sensitive to the chosen percentile, the model's predictions may not be robust. Without uncertainty quantification, it is impossible to assess whether the agreement between predictions and experiments is meaningful or coincidental.
  - **Resolution test** Justify the choice of the 95th percentile with a principled argument or sensitivity analysis. Report the range of ϵm values consistent with the experimental data and demonstrate that model predictions are robust across this range. Provide confidence intervals for Req and ϵm.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Model validation
  - **Claim pointer** The authors claim that "the algorithms simulated the complete time evolution of condensed droplets as they dissolved or persisted, relating critical equilibrium droplet size to the Cahn-Hilliard interfacial energy coefficient."
  - **Evidence pointer** Results section, Figures 3, S3; location not provided
  - **Concern** The validation of the numerical solvers is described primarily through self-consistency checks between NMG and SAV, and through comparison to a forward Euler method for early times. However, no comparison to analytical solutions or benchmark problems with known exact solutions is presented. The authors also do not report convergence studies with respect to mesh size or time step for the specific CPC simulations, despite noting that "27 elements were insufficient" for small ϵm values.
  - **Why it matters** For a methodological paper, the reliability of the numerical solvers is paramount. Self-consistency between two implementations is necessary but not sufficient to establish accuracy. Without benchmarks against known solutions or rigorous convergence studies, users cannot be confident that the solvers produce correct results for their own applications.
  - **Resolution test** Include at least one benchmark problem with an analytical or highly accurate reference solution, and report convergence rates for both NMG and SAV. Provide a convergence study for the CPC simulations showing that results are converged with respect to mesh size and time step.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Biological interpretation
  - **Claim pointer** The authors conclude that "the CPC behaves as a simple Cahn-Hilliard fluid early in mitosis."
  - **Evidence pointer** Results section, Discussion; location not provided
  - **Concern** The conclusion that CPC behaves as a "simple" Cahn-Hilliard fluid is a strong statement that goes beyond the evidence. The model assumes constant mass, a single order parameter, and a specific free energy form. The authors acknowledge the lack of source/sink terms but do not discuss whether other model features (e.g., active transport, binding kinetics, or multi-component effects) could also explain the observed droplet dynamics. The agreement between model and experiment is consistent with Cahn-Hilliard behavior but does not rule out alternative mechanisms.
  - **Why it matters** The broader significance of the work depends on whether the Cahn-Hilliard framework is uniquely supported or merely one of several possible explanations. Overstating the conclusion could mislead readers about the strength of evidence for phase separation as the underlying mechanism.
  - **Resolution test** Soften the conclusion to state that the observations are "consistent with" Cahn-Hilliard behavior, or provide additional experiments or analyses that discriminate between Cahn-Hilliard dynamics and alternative models (e.g., reaction-diffusion with localized sources).
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Materials and methods, CPC droplet simulations
  - **Evidence pointer** Materials and methods section; location not provided
  - **Issue** The description of the CPC simulation initialization states that "W was selected from a normal distribution (µ = 90 nm, σ = 10 nm) at each vertical position and initialized for five simulations with the random seed set to the simulation number (50 total)." It is unclear whether the random seed was set per simulation or per vertical position, and how the 50 total simulations were distributed across the 10 RIC values.
  - **Required correction** Clarify the random seeding procedure and specify how many simulations were run for each RIC value. Provide the exact random seed values or a reproducible seeding strategy.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** Results, Figure 4C
  - **Evidence pointer** Results section, Figure 4C; location not provided
  - **Issue** The KS test P-value for comparing inner centromere and non-inner centromere foci radii is reported (P = 1.2e-15), but the sample sizes and effect size (e.g., median difference) are not stated.
  - **Required correction** Report sample sizes for each group and a measure of effect size (e.g., median difference or Cohen's d) alongside the P-value.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Results, Figure 6E and 6H
  - **Evidence pointer** Results section, Figures 6E, 6H; location not provided
  - **Issue** The comparison between predicted and measured droplet spacing distributions is described as "nearly superimposable," but the figure is not provided. It is unclear whether the comparison is qualitative or quantitative.
  - **Required correction** Provide the figure or describe the quantitative comparison in the text, including any statistical measures used.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Discussion
  - **Evidence pointer** Discussion section; location not provided
  - **Issue** The discussion mentions "a consistent 2–3-fold difference in overall abundance" of a CPC subunit between cell types, but this is not linked to the model parameters or predictions.
  - **Required correction** Either explain how this abundance difference relates to the model (e.g., through ϵm or initial conditions) or remove the statement as it is not integrated into the main argument.
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative agreement not demonstrated), R1-M2 (parameter estimation not justified), R1-M3 (solver validation incomplete).
- **Assessment against Nature-style criteria**  
  *Originality*: Moderate. The application of Cahn-Hilliard models to the CPC is novel, and the cross-language solver package is a practical contribution. However, the underlying mathematical framework is well established.  
  *Scientific importance*: Moderate. If the claims are substantiated, the work could provide a useful framework for testing phase separation in biological systems. The current evidence does not fully establish the central claim.  
  *Interdisciplinary readership*: The work bridges mathematics, computational biology, and cell biology, and the solver package could attract users from multiple fields. The biological application is likely to interest cell biologists.  
  *Technical soundness*: The numerical methods are based on published algorithms, and the self-consistency checks are encouraging. However, the lack of benchmark validation and convergence studies weakens the technical foundation.  
  *Readability for nonspecialists*: The manuscript is generally well written, but the mathematical sections (Boxes 1–3) may be challenging for readers without a background in partial differential equations. The biological context is clearly explained.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a potentially useful tool and an interesting application, but the central claim of predictive accuracy is not currently established from the provided evidence. The authors should provide quantitative comparisons, justify parameter choices, and strengthen solver validation before the case is convincing.

## Risk / unsupported claims
- The claim that CPC "behaves as a simple Cahn-Hilliard fluid" is not fully supported; the model is consistent with observations but alternative mechanisms are not ruled out.
- The claim of quantitative agreement between model predictions and experimental measurements is not supported by statistical evidence in the text.
- The estimate of Req from the 95th percentile of non-inner centromere foci is not justified, and the sensitivity of ϵm to this choice is not assessed.
- The statement that "the fully constrained Cahn-Hilliard simulations predicted spatiotemporal dewetting and coarsening behaviors that matched experiments" is not verifiable without the figures and quantitative comparisons.
- The claim that the solvers are "stable, self-consistent" is supported by internal consistency checks but not by external benchmarks.