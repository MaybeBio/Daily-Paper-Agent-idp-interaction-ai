## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv, 2025)
- **Assessment boundary** Scientific content, methodological soundness, claims vs. evidence, and presentation quality as presented in the provided text
- **Shared manuscript claim summary** The authors present a multi-language (Python, MATLAB, Julia) suite of numerical solvers for the Cahn-Hilliard equation, demonstrate their stability and self-consistency, derive a universal relationship between the interfacial energy coefficient and critical droplet radius, and apply this framework to model the chromosomal passenger complex (CPC) as a biomolecular condensate during mitosis, with predictions compared to experimental imaging data in HeLa and MCF10A-5E cells.
- **Visible evidence base** Full text including Summary, Introduction, Results, Discussion, Resource Availability, STAR Methods (experimental and computational), figure legends referenced in text (Figures 1–6, S1–S6), and statistical details
- **Missing materials affecting confidence** Figures and supplementary figures themselves are not provided; only textual descriptions and legends are available. Raw data, code outputs, and full statistical outputs are not accessible. The original images from Gascoigne et al. are referenced but not shown.

## Reviewer

- **Overall assessment** This manuscript presents a valuable and timely methodological contribution to the field of biomolecular condensate modeling. The development of accessible, cross-language numerical solvers for the Cahn-Hilliard equation addresses a genuine gap in the community. The application to the CPC system is ambitious and the integration of computational predictions with experimental validation is commendable. However, several technical and conceptual concerns must be addressed before the case is fully established, particularly regarding the uniqueness of the parameterization, the robustness of the statistical comparisons, and the strength of the claim that CPC behaves as a Cahn-Hilliard fluid.

- **Who would be interested in the results, and why** Computational biologists, biophysicists, and cell biologists studying phase separation and biomolecular condensates. The numerical tools will be of direct use to researchers seeking to model condensate dynamics without specialized expertise in numerical analysis. The CPC application will interest the mitosis and chromosome biology community. The general framework for constraining model parameters from experimental data will appeal to systems biologists.

- **Major strengths** The manuscript addresses a clear need for accessible, validated numerical tools for the Cahn-Hilliard equation. The dual-solver approach (NMG and SAV) with cross-validation is rigorous. The derivation of a universal relationship between epsilon_m and critical radius is a useful contribution. The application to CPC is well-motivated and the integration of experimental data to constrain the model is thoughtful. The multi-language implementation (Python, MATLAB, Julia) broadens accessibility.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the relationship between epsilon_m and Req (Figure 3E) is "universal" and can be used to constrain the model for any Cahn-Hilliard system.
- **Evidence pointer** Results section, Figures 3D and 3E, STAR Methods "Defining Ri and Req"
- **Concern** The universality of the epsilon_m-Req relationship is asserted but not rigorously demonstrated. The relationship is derived from simulations on a specific mesh size (2^7 or 2^8) with specific boundary conditions and initial conditions. The authors do not show that this relationship holds across different domain sizes, mesh resolutions, or boundary condition types. The "universal" claim is central to the CPC application, as it is used to estimate epsilon_m from experimental measurements of Req. If the relationship is mesh-dependent or geometry-dependent, the estimated epsilon_m could be systematically biased.
- **Why it matters** The entire CPC parameterization rests on this relationship. If it is not truly universal, the subsequent simulations and their agreement with experiments could be fortuitous or driven by an incorrect epsilon_m. The claim of universality is a strong one that requires more extensive validation.
- **Resolution test** The authors should demonstrate the epsilon_m-Req relationship is invariant (or quantify its variation) across a range of mesh sizes (e.g., 2^6 to 2^10), domain aspect ratios, and boundary conditions (periodic, Neumann, mixed). They should also test whether the relationship holds for different initial condition geometries (e.g., multiple droplets, non-circular droplets).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance / Claim strength
- **Claim pointer** The authors conclude that "the Cahn-Hilliard equation tests whether condensate dynamics behave as a phase-separated liquid, and its numerical solutions advance generalized modeling of biomolecular systems" and that CPC behavior is "fully consistent with Cahn-Hilliard dynamics."
- **Evidence pointer** Results sections "Cahn-Hilliard models accurately predict spacing of CPC foci in multiple cellular contexts" and Discussion
- **Concern** The agreement between model predictions and experimental measurements of droplet spacing is presented as strong evidence for the Cahn-Hilliard model. However, the comparison is based on a single summary statistic (droplet spacing distribution). The model is not tested against other observable features, such as droplet size distribution, growth/shrinkage kinetics, or the temporal evolution of the system. Furthermore, the model is calibrated using the size of inner centromere foci (to estimate epsilon_m) and then tested on the spacing of non-inner centromere foci. This is a reasonable approach, but the predictive power is limited to one aspect of the system. The claim that the system "behaves as a phase-separated liquid" is a strong interpretation that may not be uniquely supported by the data, as other models (e.g., reaction-diffusion with aggregation) could potentially reproduce similar spacing patterns.
- **Why it matters** The central scientific claim of the paper is that CPC dynamics are consistent with Cahn-Hilliard (phase separation) behavior. If the evidence is based on a single, potentially non-unique observable, the claim is overstated. The paper would be strengthened by a more comprehensive comparison between model and experiment, or by a more cautious interpretation of the results.
- **Resolution test** The authors should either (a) provide additional experimental comparisons (e.g., time-lapse data showing droplet dynamics, size distributions, or response to perturbations) that further discriminate between Cahn-Hilliard and alternative models, or (b) temper the conclusion to state that the observed spacing is "consistent with" rather than "evidence for" Cahn-Hilliard dynamics.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that the SAV solver is "generally faster than NMG and represents the only practical option for Python" and that the NMG solver is "largely unusable" in Python, requiring 10^5-10^6 seconds by extrapolation.
- **Evidence pointer** Results section "Numerical solvers for the Cahn-Hilliard equation", Figure 2B
- **Concern** The performance comparison between NMG and SAV is presented for a specific set of conditions (spinodal decomposition, specific mesh sizes, specific hardware). The claim that NMG is "largely unusable" in Python is a strong statement that may be implementation-specific. The authors attribute the poor performance to a "non-tail recursive function," but it is unclear if this is an inherent limitation of the algorithm or a limitation of their specific implementation. A more thorough performance analysis, including profiling and potential optimizations, would be needed to support this strong claim.
- **Why it matters** The choice of solver is a practical concern for users. If the claim that NMG is unusable in Python is inaccurate or implementation-specific, it could mislead users into avoiding a potentially useful tool. Conversely, if the claim is accurate, it highlights a significant limitation of the NMG approach in a popular language.
- **Resolution test** The authors should provide a more detailed performance analysis, including profiling data, and discuss whether the NMG implementation could be optimized for Python (e.g., using just-in-time compilation with Numba or Cython). They should also clarify whether the performance gap is algorithmic or implementation-specific.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors use the upper 95th percentile of non-inner centromere foci to estimate Req = 168 ± 2 nm for HeLa cells, and then use this to determine epsilon_m = 21.6 ± 0.6 nm.
- **Evidence pointer** Results section "Cahn-Hilliard models accurately predict spacing of CPC foci in multiple cellular contexts", Figures 4C and 4D
- **Concern** The choice of the 95th percentile of the non-inner centromere foci distribution to represent Req is not rigorously justified. The authors state that these foci "ultimately dissolve," but the 95th percentile of a distribution of dissolving droplets is not necessarily the critical radius. The critical radius is the threshold above which droplets grow and below which they shrink. The 95th percentile of a population of shrinking droplets could be an arbitrary point on the distribution, depending on the initial size distribution and the time of observation. A more principled approach would be to directly measure the size of droplets that are at the threshold between growth and shrinkage, or to fit the full size distribution to a theoretical model.
- **Why it matters** The estimated epsilon_m is directly proportional to Req. If the 95th percentile is a biased estimator of the true critical radius, then epsilon_m will be biased, and all subsequent simulations will be affected. This is a critical step in the parameterization, and the choice of estimator needs to be better justified.
- **Resolution test** The authors should provide a sensitivity analysis showing how the model predictions change with different choices of percentile (e.g., 90th, 99th) or with alternative methods for estimating Req. They should also discuss the physical rationale for using the 95th percentile.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors state that "the epsilon_m for CPC is not fixed" and that it is ~30% larger in MCF10A-5E cells compared to HeLa cells, potentially relating to "chromatin compaction or differences in CPC modification state."
- **Evidence pointer** Results section "Cahn-Hilliard models accurately predict spacing of CPC foci in multiple cellular contexts", Figures S6A and S6B
- **Concern** The observation that epsilon_m differs between cell types is interesting but is not mechanistically explored. The authors speculate about potential causes (chromatin compaction, modification state) but do not provide any experimental evidence to support these hypotheses. The claim that the difference is "~30% larger" is based on a single cell line comparison, and the uncertainty in this difference is not reported. This limits the interpretability of the finding.
- **Why it matters** The cell-type dependence of epsilon_m is presented as a key finding, but without mechanistic insight or a broader survey of cell lines, it remains an observation rather than a robust biological conclusion. The paper would be strengthened by either (a) providing experimental evidence linking epsilon_m to a specific molecular property, or (b) framing this as a preliminary observation that warrants future investigation.
- **Resolution test** The authors should either provide additional experimental data (e.g., measuring chromatin compaction or modification state in both cell lines) or soften the claim to state that epsilon_m "appears to vary between cell types" and that the mechanistic basis is an open question.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Box 1 and Box 2
- **Evidence pointer** Introduction, Boxes 1 and 2
- **Issue** The boxes are referenced in the text but their content is not provided in the manuscript text. It is unclear what information they contain and how they support the main text.
- **Required correction** The boxes should be included in the manuscript or their content should be summarized in the text.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Statistical comparison of model and experiment
- **Evidence pointer** Results section "Cahn-Hilliard models accurately predict spacing of CPC foci in multiple cellular contexts", Figures 6E and 6H
- **Issue** The comparison between model predictions and experimental measurements of droplet spacing is described as "nearly superimposable" and "excellent agreement," but no statistical test is reported. It is unclear whether the agreement is quantified or is based on visual inspection.
- **Required correction** A formal statistical comparison (e.g., Kolmogorov-Smirnov test, chi-square test, or calculation of a similarity metric) should be reported to support the claim of agreement.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Code availability and reproducibility
- **Evidence pointer** Data and Code Availability section
- **Issue** The code is available on GitHub, but there is no mention of a versioned release, a DOI, or a software license. This limits the long-term accessibility and reproducibility of the work.
- **Required correction** The authors should provide a versioned release with a DOI (e.g., via Zenodo) and specify a software license.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Discussion of the "dogleash" and its role
- **Evidence pointer** Discussion section
- **Issue** The discussion of the "dogleash" (single alpha-helical region) is brief and assumes prior knowledge. The relevance of this structural feature to the epsilon_m value is not fully explained.
- **Required correction** A brief explanation of what the dogleash is and how its length relates to the interfacial energy coefficient would improve accessibility.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Sensitivity analysis of simulation parameters
- **Evidence pointer** STAR Methods, CPC droplet simulations
- **Issue** The simulations use specific values for dt, mesh size, and domain size. No sensitivity analysis is presented to show that the results are robust to reasonable variations in these parameters.
- **Required correction** A brief sensitivity analysis or a statement that the results are robust to parameter variations would strengthen the conclusions.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Generalizability of the framework
- **Evidence pointer** Discussion section
- **Issue** The authors state that the framework can be extended to other phase-separated systems, but no specific examples or guidance are provided.
- **Required correction** A brief discussion of how the framework could be adapted to other systems (e.g., what parameters would need to be measured) would increase the impact of the work.

## Risk / unsupported claims
- The "universal" relationship between epsilon_m and Req is not sufficiently validated across different numerical conditions.
- The claim that CPC "behaves as a Cahn-Hilliard fluid" is based on a single observable (droplet spacing) and may be non-unique.
- The use of the 95th percentile of the non-inner centromere foci distribution as an estimate of Req is not rigorously justified.
- The mechanistic interpretation of the cell-type difference in epsilon_m is speculative and unsupported by direct evidence.
- The claim that NMG is "largely unusable" in Python is potentially implementation-specific and not fully supported by the presented performance data.
- The agreement between model and experiment is not quantified with formal statistical tests.