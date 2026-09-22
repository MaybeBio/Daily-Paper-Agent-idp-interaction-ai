## Review setup
- **Input scope** Full manuscript text including Significance, Results, Discussion, Methods, and supplementary figure references
- **Assessment boundary** Scientific claims, model validity, experimental design, data interpretation, and alignment with stated conclusions. Not assessed: grammar, formatting, or editorial style.
- **Shared manuscript claim summary** The authors propose that liquid-liquid phase separation of phosphorylated LAT (pLAT) into condensates downstream of the T cell receptor (TCR) provides a unified mechanism for three key signaling properties: single-molecule sensitivity, kinetic proofreading (selectivity for high-affinity ligands), and dynamic range in antigen dose detection. A computational model of LAT diffusion, phosphorylation, and multivalent clustering is developed and compared to published single-molecule imaging data. A novel 2D protein array platform is used to test the model prediction of an optimal pMHC spacing for LAT condensation.
- **Visible evidence base** Full text of Results, Discussion, and Methods; figure references (Figs. 1–6); supplementary figure references (Figs. S1–S8); equations referenced in SI (Eqs. 14–20); data/code availability statement
- **Missing materials affecting confidence** Supplementary figures and movies (S1–S16) not provided; full model parameter values and derivation of SI equations not visible; raw imaging data not shown; experimental replicates and statistical details for imaging data not fully specified; details of the Gaussian fit comparison (F-test) not fully described

## Reviewer

- **Overall assessment** This manuscript presents a conceptually appealing and timely hypothesis: that LAT condensation, rather than a sequence of biochemical steps, can serve as the kinetic proofreading mechanism in TCR signaling. The computational model is well-motivated and the authors make a genuine effort to connect simulation outputs to quantitative single-molecule data. The 2D protein array platform is an innovative experimental tool that allows independent control of pMHC density and spacing, and the observation of an optimal spacing for LAT phosphorylation is potentially significant. However, the manuscript has several important weaknesses. The model omits upstream signaling steps (e.g., ZAP70 recruitment and activation) that are known to contribute to kinetic proofreading, and the authors do not adequately address whether the reported effects are specific to condensation or could arise from simpler spatial effects. The experimental validation is limited to a single cell line and a single peptide-MHC, and the comparison between model and experiment is qualitative. The statistical analysis of the optimal spacing is underpowered and the F-test comparison is not fully described. The claim of "single-molecule sensitivity" is supported by simulation but the experimental data do not directly demonstrate single-molecule detection. Overall, the work is interesting and potentially important, but the case is not fully established from the provided evidence.

- **Who would be interested in the results, and why** Immunologists studying T cell activation and antigen discrimination; biophysicists and computational biologists interested in phase separation and signaling; researchers developing synthetic antigen-presenting platforms for immunotherapy or basic immunology. The work bridges a gap between biophysical principles of phase separation and quantitative immunology, and the 2D array platform could be broadly useful.

- **Major strengths** 1) The hypothesis that condensation itself provides kinetic proofreading is novel and conceptually important, offering a physical mechanism distinct from traditional biochemical proofreading models. 2) The computational model is spatially explicit and stochastic, capturing emergent behaviors (nucleation delay, all-or-none clustering) that are not accessible in well-mixed models. 3) The model is tested against quantitative single-molecule data (delay times, cluster sizes, clustering probability), which is a high standard for the field. 4) The 2D protein array platform is an innovative experimental approach that allows independent manipulation of pMHC density and spacing, and the prediction of an optimal spacing is a strong, testable model output. 5) The authors are appropriately cautious in comparing model and experiment, acknowledging differences between array-displayed and membrane-bound pMHC.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Model completeness and validity
- **Claim pointer** The model is presented as capturing "the key physical and chemical processes underlying TCR-induced LAT clustering" and is used to draw conclusions about kinetic proofreading in TCR signaling.
- **Evidence pointer** Methods, Computational Model; Results, "The LAT Condensation Model"
- **Concern** The model omits all upstream signaling events between TCR-pMHC binding and LAT phosphorylation, including ZAP70 recruitment, phosphorylation, and activation. The authors justify this by citing evidence that LAT phosphorylation is rate-limiting, but this is an assumption that is not tested. More critically, the model assumes that TCR-pMHC binding immediately leads to local LAT phosphorylation, which bypasses the well-established kinetic proofreading steps upstream of LAT (e.g., ZAP70 activation, CD45 exclusion). The authors claim to isolate the contribution of LAT condensation to proofreading, but by omitting upstream steps, they cannot rule out that the observed delay in clustering is simply a consequence of the time required for LAT phosphorylation to reach a critical threshold, which would occur in any spatially extended model regardless of condensation. The model also does not include negative feedback mechanisms that deactivate TCRs, which are instead imposed as a first-order inactivation rate. The authors should test whether the model's qualitative conclusions (e.g., optimal spacing, kinetic proofreading) are robust to inclusion of upstream signaling steps or to alternative mechanisms of LAT clustering (e.g., simple aggregation without phase separation).
- **Why it matters** The central claim is that condensation provides a specific and necessary mechanism for kinetic proofreading. If the observed delay and selectivity arise from simpler spatial effects (e.g., diffusion-limited phosphorylation), the novelty and importance of the work are substantially reduced.
- **Resolution test** The authors should either (a) include a minimal representation of upstream signaling (e.g., ZAP70 activation as a stochastic step) and show that conclusions are unchanged, or (b) perform a control simulation where LAT clustering is driven by a non-condensation mechanism (e.g., irreversible aggregation) and show that the model no longer reproduces the experimental data. Alternatively, they could provide experimental evidence that LAT condensation is required for the observed delay, e.g., using a LAT mutant that cannot undergo phase separation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation and generalizability
- **Claim pointer** The authors state that "these results explain how LAT clustering dynamics could give rise to digital activation for signal amplification and single molecule sensitivity, as well as analog tuning for dynamic range in pMHC dose detection."
- **Evidence pointer** Results, "Cluster Growth Allows Wide Dynamic Range" and "pMHC Arrays Reveal Optimal Antigen Spacing for LAT Condensation"; Figs. 4 and 6
- **Concern** The experimental validation is limited to a single cell line (P14 Jurkat) and a single peptide-MHC (gp33/H-2D(b)). The claim of "single-molecule sensitivity" is supported by simulations showing that a single TCR can nucleate a cluster, but the experiments do not directly demonstrate single-molecule detection. The imaging data show population-level phosphorylation responses to arrays with varying pMHC density, but the relationship between array density and the number of TCRs engaged per cell is not directly measured. The authors infer an optimal spacing from the density-response curve, but the statistical analysis is weak: the F-test comparing Gaussian vs. flat line is mentioned but the details (degrees of freedom, confidence intervals, number of independent experiments) are not provided. Moreover, the model predicts an optimal spacing based on the pLAT gradient length scale, but the experimental data show a broad peak and the authors do not report the fitted optimal spacing value or its uncertainty. The generality of the finding is unclear: would the same optimal spacing be observed for other peptide-MHCs, other TCRs, or primary T cells?
- **Why it matters** The claim of a general mechanism for TCR signaling requires demonstration across multiple ligand-receptor systems and ideally in primary cells. The current data are consistent with the model but do not strongly discriminate it from alternative explanations (e.g., simple density-dependent signaling without a true optimum).
- **Resolution test** The authors should (1) provide a quantitative estimate of the optimal spacing with confidence intervals from the Gaussian fit, (2) test at least one additional peptide-MHC with different affinity, and (3) ideally perform experiments with primary T cells or a more physiological antigen-presenting surface. If primary cells are not feasible, they should explicitly acknowledge this limitation and temper the generality of their claims.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Model-experiment comparison rigor
- **Claim pointer** The authors state that "the close agreement in these measurements between our simulated results and experimental data suggest that our model is able to accurately capture these key aspects of early TCR signaling."
- **Evidence pointer** Results, "Simulated LAT Cluster Sizes and Dynamics Match Single-Molecule Imaging"; Fig. 3
- **Concern** The comparison between simulation and experiment for cluster size distributions and delay times is visual and qualitative. The authors state that the distributions are "strikingly similar" but do not provide quantitative goodness-of-fit metrics or statistical tests. For the cluster size comparison, the experimental data are truncated at the detection limit (~200 molecules), and the authors compare only the upper tail of the simulated distribution. For the delay time comparison, the experimental data are from a published study (ref 27) and the authors do not report the number of events, the fitting procedure, or the uncertainty in the experimental distribution. The model has multiple free parameters (e.g., phosphorylation rates, dephosphorylation rates, binding energies) that are presumably tuned to match the data, but the authors do not report a parameter sensitivity analysis or discuss identifiability.
- **Why it matters** Without quantitative comparison metrics, it is difficult to assess whether the model is genuinely predictive or merely descriptive. The claim of "close agreement" is not falsifiable as presented.
- **Resolution test** The authors should provide (1) a quantitative comparison metric (e.g., Kolmogorov-Smirnov test, log-likelihood ratio) for the delay time and cluster size distributions, (2) a parameter sensitivity analysis showing which parameters most strongly affect the outputs, and (3) a discussion of parameter identifiability given the available data.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Alternative explanations and specificity of condensation
- **Claim pointer** The authors claim that "LAT nucleation constitutes a key kinetic proofreading step in T cell signaling" and that the model "directly demonstrate[s] kinetic proofreading by LAT condensation."
- **Evidence pointer** Results, "Kinetic Proofreading by Condensate Nucleation in TCR Signaling"; Fig. 4
- **Concern** The simulations show that longer pMHC-TCR binding lifetimes lead to more clustering, which is interpreted as kinetic proofreading. However, this result could arise from any mechanism that requires accumulation of pLAT over time, not specifically from condensation. The authors do not compare their model to a control model without condensation (e.g., where pLAT molecules do not cluster but simply accumulate). The claim that condensation specifically enables proofreading is therefore not directly tested. Additionally, the authors state that "the proofreading is carried out solely by LAT condensation" because upstream steps are omitted, but this is a circular argument: by construction, the model has no other proofreading mechanism, so the conclusion is trivially true.
- **Why it matters** The specificity of the mechanism is central to the paper's significance. If any time-delayed accumulation mechanism would produce similar results, the role of condensation is less distinctive.
- **Resolution test** The authors should run a control simulation where pLAT molecules do not form clusters (e.g., no multivalent interactions) but where the readout is the total amount of pLAT in the vicinity of the TCR. If this control also shows kinetic proofreading, the specific role of condensation is not established.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of model assumptions
- **Affected element** Methods, Computational Model
- **Evidence pointer** Methods, Computational Model
- **Issue** The model assumes that TCR-pMHC binding immediately initiates LAT phosphorylation in the local neighborhood, but the spatial range of "local" is not defined. The grid spacing is 30 nm, but the phosphorylation radius is not specified.
- **Required correction** Please specify the spatial range over which an active TCR can phosphorylate LAT, and justify this choice based on known biology (e.g., ZAP70 substrate access).

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results, "pMHC Arrays Reveal Optimal Antigen Spacing for LAT Condensation"
- **Evidence pointer** Fig. 6F–H; SI Appendix, Fig. S8
- **Issue** The F-test comparing Gaussian vs. flat line fits is mentioned but the test statistic, degrees of freedom, and p-value are not reported in the main text.
- **Required correction** Report the F-statistic, degrees of freedom, and p-value for the comparison, and state the number of independent experiments (n) used for the analysis.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of experimental data
- **Affected element** Results, "pMHC Arrays Reveal Optimal Antigen Spacing for LAT Condensation"
- **Evidence pointer** Fig. 6D–E
- **Issue** The authors report that larger arrays (higher GFP copy number) induce higher phosphorylation levels. This could be due to increased total pMHC number rather than a spacing effect. The authors use "activation efficiency" (slope of phosphorylation vs. pMHC number) to correct for this, but the rationale and derivation of this metric are not fully explained.
- **Required correction** Provide a clearer explanation of why the slope (activation efficiency) is the appropriate metric, and discuss potential confounding effects of array size on cell contact area.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion
- **Evidence pointer** Discussion, first paragraph
- **Issue** The authors state that "it has not been clear how these mechanisms can simultaneously balance the opposing constraints imposed by all three of these properties" but do not cite specific prior models that have addressed trade-offs between sensitivity, selectivity, and dynamic range.
- **Required correction** Add citations to prior theoretical work on kinetic proofreading in TCR signaling (e.g., McKeithan 1995, Rabinowitz et al. 1996, Lever et al. 2016) and explicitly state how the condensation mechanism differs from these prior models.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data, Materials, and Software Availability
- **Evidence pointer** Data, Materials, and Software Availability
- **Issue** The code is available on GitHub, but the manuscript does not specify the version or commit hash, and there is no documentation of the software environment required to run the simulations.
- **Required correction** Provide a versioned release of the code with a README describing dependencies and instructions for reproducing the main figures.

## Risk / unsupported claims
- The claim that "single-molecule sensitivity" is demonstrated experimentally is not supported; the experiments show population-level responses to arrays, and single-molecule detection is only shown in simulations.
- The claim that the model "directly demonstrate[s] kinetic proofreading by LAT condensation" is not fully supported because the model omits all upstream proofreading steps and does not include a control without condensation.
- The claim of an "optimal pMHC spacing" is supported by the data but the statistical significance is not fully reported; the fitted optimal spacing value and its uncertainty are not provided.
- The generalizability of the findings to primary T cells or other peptide-MHC systems is not demonstrated and should not be implied.
- The model's ability to "accurately capture" experimental data is asserted based on visual comparison; no quantitative goodness-of-fit metrics are provided.
- The assumption that LAT phosphorylation is rate-limiting and that upstream steps can be omitted is not tested or justified with direct evidence.
- The claim that the model "explains" the observed distribution shapes of pCD3ζ and pLAT (Fig. 6E) is speculative; the authors do not provide a quantitative model for CD3ζ phosphorylation to compare against.

## Assessment against Nature-style criteria
- **Originality** High. The idea that condensation itself, rather than a sequence of biochemical modifications, provides kinetic proofreading is a novel conceptual contribution. The 2D protein array platform is also an innovative experimental tool.
- **Scientific importance** Potentially high. If the condensation-based proofreading mechanism is validated, it would change how the field thinks about TCR signal discrimination and could have implications for other signaling systems that involve phase separation. However, the importance is contingent on the specificity of the mechanism being established, which is currently not fully done.
- **Interdisciplinary readership** Moderate to high. The work bridges immunology, biophysics, and computational biology. The phase separation angle will attract interest from the broader cell biology community. However, the manuscript is written primarily for a specialist audience and may be challenging for nonspecialists to follow, particularly the model description.
- **Technical soundness** Moderate. The model is well-constructed and the experimental platform is clever, but the validation is incomplete. The lack of quantitative model-experiment comparison, the omission of upstream signaling, and the limited experimental scope (one cell line, one ligand) weaken the technical case.
- **Readability for nonspecialists** Moderate. The Significance statement is clear and accessible. The Results section is generally well-written but assumes familiarity with TCR signaling and phase separation concepts. The Methods section is dense and would be difficult for a nonspecialist to follow. Figures are well-designed but some (e.g., Fig. 5) require careful study.

## Recommendation posture
**Supportive if technical concerns are resolved.** The core hypothesis is interesting and the experimental platform is innovative, but the case is not fully established from the provided evidence. The authors should address the following before the claims can be considered supported: (1) test the specificity of the condensation mechanism by including a control without condensation or with upstream signaling steps; (2) provide quantitative model-experiment comparisons; (3) strengthen the statistical analysis of the optimal spacing; (4) demonstrate generalizability to at least one additional ligand-receptor system or acknowledge the limitation. If these concerns are addressed, the work could be suitable for publication in a high-impact journal.