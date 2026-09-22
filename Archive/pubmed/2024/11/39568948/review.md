## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results and discussion, conclusions, data availability, author contributions, conflicts of interest, acknowledgements)
- **Assessment boundary** Scientific content and technical claims as presented in the main text; supplementary material referenced but not provided
- **Shared manuscript claim summary** The authors use coarse-grained polyampholyte simulations of 15 sequence variants (EKV1-15) and four natural IDPs to show that (1) chain conformations in the dense phase are near-ideal and weakly sequence-dependent, (2) conformations gradually expand from dilute to dense phase following a universal sigmoidal curve when normalized by saturation concentration, and (3) chains at the condensate interface are more compact than in the dense phase but more extended than in the dilute phase, with strong sequence dependence.
- **Visible evidence base** Main text figures (Fig. 1-5), equations (Eq. 1-3), and text descriptions; supplementary figures and methods referenced but not available
- **Missing materials affecting confidence** Supplementary Information (Figs. S1-S18, methods for cluster analysis, normalization of SCD, slab simulation details); simulation parameter details (force field parameters, integration time steps, equilibration protocols); quantitative error estimates for key measurements

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question about how IDP conformations change during condensation. The systematic approach using a well-defined polyampholyte model series is appropriate and the finding that dense-phase conformations converge to near-ideal behavior regardless of sequence is potentially significant. However, the evidence presented in the main text is insufficient to fully evaluate several key claims, particularly regarding the universality of the observed trends, the quantitative agreement with ideal chain behavior, and the robustness of the interfacial results. The manuscript would benefit from more detailed presentation of methods and quantitative comparisons in the main text.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, and IDP biophysics would find these results valuable. The finding that dense-phase conformations are near-ideal and weakly sequence-dependent has implications for understanding condensate material properties and function. The universal scaling behavior described could provide a framework for predicting conformational changes in other IDP systems. The interfacial results are relevant to understanding how surface properties of condensates might differ from their interiors, which has implications for cellular organization and function.

- **Major strengths**
  1. Systematic design of model sequences spanning a wide range of charge patterning, enabling clear analysis of sequence effects
  2. Multi-scale validation using both designed polyampholytes and natural IDP sequences
  3. Novel focus on conformational transitions across concentrations, not just endpoint states
  4. Clear demonstration that dense-phase conformations converge to near-ideal behavior, contrasting with strong sequence dependence in dilute phase
  5. Identification of universal scaling behavior when normalized by saturation concentration

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "For single chains, Rg decreased with increasing nSCD (Fig. 1a), which is consistent with many previous studies that examined this behavior in detail."
- **Evidence pointer** Fig. 1a; location not provided
- **Concern** The manuscript states that Rg decreases with increasing nSCD for single chains, but the actual Rg values, their uncertainties, and the statistical significance of the differences between adjacent sequences are not reported in the main text. The claim of consistency with previous studies is made without quantitative comparison to literature values. Additionally, the range of Rg values across the 15 EKVs is not clearly stated, making it difficult to assess the magnitude of the reported effects.
- **Why it matters** The quantitative relationship between nSCD and single-chain Rg is foundational to the entire study. If the differences between sequences are not statistically robust, the subsequent comparisons between dilute and dense phase behavior lose their interpretive power. The lack of reported uncertainties prevents assessment of whether the observed trends are meaningful.
- **Resolution test** Provide a table or figure with mean Rg values and standard errors for all 15 EKVs in both dilute and dense phases. Include statistical tests (e.g., ANOVA or pairwise comparisons) demonstrating significant differences between sequences. Compare quantitatively with published Rg values for similar polyampholyte sequences.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "In the dense phase, however, the chain conformation approaches that of an ideal chain, regardless of the sequence."
- **Evidence pointer** Fig. 1a-d; location not provided
- **Concern** The claim that dense-phase conformations approach ideal chain behavior is central to the paper, but the quantitative criteria for "approaching ideal" are not defined. The manuscript shows that Rg in the dense phase varies by only ~12.6% across sequences, but does not provide a statistical comparison to the theoretical ideal chain Rg value. The comparison of Re to ideal chain scaling (Fig. 1d) is mentioned but the quantitative agreement (e.g., R² values, residuals) is not reported. The statement that P(Rg) is "much broader" in the dense phase is not supported by quantitative measures such as variance or standard deviation.
- **Why it matters** The near-ideal behavior in the dense phase is the key finding of the paper. Without clear quantitative criteria for what constitutes "ideal" behavior and statistical evidence that the observed conformations are consistent with this prediction, the central claim is not rigorously established. This is particularly important because the authors argue this behavior is universal across sequences.
- **Resolution test** Define quantitative criteria for ideal chain behavior (e.g., expected Rg for a 50-residue chain with given bond length and excluded volume). Provide statistical comparison between observed dense-phase Rg values and the ideal chain prediction, including confidence intervals. Report quantitative measures of P(Rg) width (e.g., standard deviation, interquartile range) for both dilute and dense phases.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "The normalized Rg values for all EKVs collapse onto a single sigmoidal curve (R² = 0.95), exhibiting a uniform trend of increase from the dilute to the dense phase."
- **Evidence pointer** Fig. 2c; location not provided
- **Concern** The claim of universal collapse onto a single sigmoidal curve is based on a reported R² value of 0.95, but the fitting procedure, the functional form of the sigmoid, and the residuals are not described. The manuscript does not report the parameters of the fit (e.g., midpoint, steepness) or their uncertainties. The extrapolated csat values for EKV10-15 are acknowledged but the potential impact of this extrapolation on the collapse is not discussed. The R² value alone is insufficient to establish universality, especially given that the data span a wide range of nSCD values.
- **Why it matters** The universal scaling behavior is a major conclusion with potential predictive power. If the collapse is not robust or depends on the extrapolation method, the generality of the finding is questionable. The lack of fitting details prevents readers from assessing the quality of the collapse or reproducing the analysis.
- **Resolution test** Provide the full fitting details including the functional form, fitting algorithm, parameter values with uncertainties, and residual analysis. Show the collapse with and without the extrapolated csat values to demonstrate robustness. Consider reporting an alternative measure of collapse quality (e.g., reduced chi-squared, AIC) rather than R² alone.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Within the interface region, Rg decreased and remained smaller than those observed for the chains within the bulk phase."
- **Evidence pointer** Fig. 4b; location not provided
- **Concern** The interfacial analysis relies on defining interface boundaries using a hyperbolic tangent fit to the concentration profile. The manuscript does not report the uncertainties in the fitted interface positions or how sensitive the Rg measurements are to the choice of boundary definitions. The statement that Rg "decreased and remained smaller" is qualitative; no statistical comparison between interfacial and bulk Rg values is provided. The authors note "pronounced fluctuations" in the dilute phase due to limited statistics, but similar concerns may apply to the interfacial region where the number of chains is also limited.
- **Why it matters** The interfacial results are presented as a novel finding with potential functional implications. If the observed compaction at the interface is not statistically robust or depends on arbitrary boundary choices, the conclusion is not reliable. The limited statistics in the interfacial region could lead to biased estimates of Rg.
- **Resolution test** Report the number of chains sampled in the interfacial region and the statistical uncertainty in the mean Rg. Perform sensitivity analysis by varying the interface boundary definition (e.g., ±δ/2 vs. ±δ/3) and show that conclusions are unchanged. Provide statistical comparison (e.g., t-test or bootstrap) between interfacial and bulk Rg values.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Originality
- **Claim pointer** "This study provides detailed insights into how the conformations of a specific subclass of IDPs (lacking secondary structures) change within condensates and in solution, as governed by their sequences."
- **Evidence pointer** Abstract; location not provided
- **Concern** The manuscript claims to provide "detailed insights" but the mechanistic understanding is limited. The authors attribute the observed behavior to "attractive interactions between monomers" and "maximizing conformational entropy," but these explanations are qualitative and not directly tested. The study does not systematically vary interaction strengths or other physical parameters to probe the underlying mechanisms. The connection between sequence patterning and the observed universal behavior in the dense phase is not mechanistically explained.
- **Why it matters** For a Nature-style audience, the significance of the findings depends on the depth of mechanistic understanding. Without a clear physical explanation for why dense-phase conformations converge to ideal behavior regardless of sequence, the results remain descriptive rather than explanatory. This limits the broader impact and predictive power of the work.
- **Resolution test** Provide additional analysis or simulations that directly test the proposed mechanisms (e.g., varying interaction strengths, analyzing contact maps, computing free energy contributions). Alternatively, clearly state the limitations of the current mechanistic understanding and propose specific testable predictions for future work.

- **Concern ID** R1-M6
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** "Our findings highlight the conformational changes these IDPs undergo as they transition from the dilute phase to a dense state, including their behavior at the interface."
- **Evidence pointer** Conclusions; location not provided
- **Concern** The manuscript does not adequately discuss the biological implications of the findings. While the introduction mentions that conformational changes can impact function (e.g., Dcp2, Tau), the discussion does not return to these examples or explore how the observed universal behavior might inform our understanding of condensate function in cells. The potential relevance to disease (e.g., neurodegeneration) is mentioned only briefly in the context of Tau.
- **Why it matters** For a broad readership, the significance of the work depends on its relevance to biological function and disease. The current manuscript is largely biophysical in focus, which is appropriate, but the lack of connection to biological context limits its impact for a general audience. The authors should more explicitly articulate why these findings matter for understanding condensate biology.
- **Resolution test** Add a discussion section that connects the findings to specific biological processes or disease mechanisms. For example, discuss how the universal expansion in the dense phase might affect molecular interactions, enzymatic activity, or aggregation propensity in condensates.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction
- **Evidence pointer** Introduction; location not provided
- **Issue** The introduction assumes familiarity with polymer physics concepts (e.g., ideal chain, Rg, scaling) without providing brief definitions or context for nonspecialist readers.
- **Required correction** Add brief explanations of key polymer physics terms when first introduced, or provide a short primer in the introduction to make the work accessible to a broader biological audience.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods description
- **Evidence pointer** Data availability; location not provided
- **Issue** The main text provides minimal information about the simulation methodology, including force field parameters, simulation length, temperature control, and system size. While details are promised in the ESI, the main text should include sufficient information for readers to understand the basic setup.
- **Required correction** Add a brief methods summary in the main text (or a methods section) covering the key simulation parameters, including the coarse-grained model details, simulation box sizes, and equilibration protocols.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Fig. 2c
- **Evidence pointer** Fig. 2c; location not provided
- **Issue** The sigmoidal fit shown in Fig. 2c is described as having R² = 0.95, but the figure does not show the fit curve, confidence intervals, or individual data points with error bars. This makes it difficult to visually assess the quality of the collapse.
- **Required correction** Update Fig. 2c to show the fitted curve, individual data points with error bars, and confidence intervals. Consider using different symbols or colors to distinguish between EKVs with different nSCD values.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Results and discussion
- **Evidence pointer** Results and discussion; location not provided
- **Issue** The manuscript frequently refers to "SCD" and "nSCD" without consistently reminding readers of their definitions and physical meaning. This may be confusing for readers unfamiliar with charge patterning metrics.
- **Required correction** Briefly restate the definition and significance of SCD/nSCD when first used in the results section, and consider adding a schematic figure showing examples of sequences with different nSCD values.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Fig. 3
- **Evidence pointer** Fig. 3; location not provided
- **Issue** The natural IDP simulations are described as being performed at different temperatures (300 K for three proteins, 260 K for LAF-1 RGG), but the rationale for this difference is not explained in the main text.
- **Required correction** Add a brief explanation for why different temperatures were used for different proteins, and discuss any potential implications for comparing results across systems.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Interdisciplinary readership
- **Affected element** Discussion
- **Evidence pointer** Conclusions; location not provided
- **Issue** The conclusions do not discuss limitations of the coarse-grained model, such as the lack of explicit solvent, absence of post-translational modifications, or simplified electrostatics. These limitations may affect the generality of the findings.
- **Required correction** Add a paragraph discussing the limitations of the model and how they might affect the conclusions, as well as potential avenues for future work with more detailed models.

## Risk / unsupported claims
1. The claim that dense-phase conformations are "akin to that of an ideal chain" is not quantitatively supported with statistical comparisons to theoretical predictions.
2. The universal sigmoidal collapse (R² = 0.95) is reported without fitting details, parameter uncertainties, or demonstration of robustness to extrapolation of csat values.
3. The statement that interfacial chains are "always more compact" than dense-phase chains is made without statistical testing or sensitivity analysis of interface boundary definitions.
4. The claim that findings are "further validated with naturally occurring protein sequences" is not fully supported, as the natural IDP results are presented only briefly and without the same level of quantitative analysis as the EKV systems.
5. The mechanistic explanation (entropy maximization, attractive interactions) is qualitative and not directly tested through systematic variation of model parameters.
6. The biological implications of the findings are asserted but not developed, with no specific connections made to functional consequences in cellular contexts.

## Assessment against Nature-style criteria
- **Originality** The study addresses a question that has received limited systematic attention: how IDP conformations change during the condensation process itself, rather than just comparing endpoint states. The finding that dense-phase conformations converge to near-ideal behavior regardless of sequence is potentially novel. However, the mechanistic understanding is limited, and the originality is somewhat tempered by the use of a simplified model system without experimental validation.
- **Scientific importance** The results have potential importance for understanding condensate biophysics and function. If the universal scaling behavior holds broadly, it could provide a predictive framework for IDP behavior in condensates. However, the importance is not fully realized in the current manuscript, as the biological implications are not developed and the mechanistic basis is not established.
- **Interdisciplinary readership** The topic bridges polymer physics, biophysics, and cell biology, and the findings could interest researchers across these fields. However, the manuscript is written primarily for a biophysics audience and may be challenging for cell biologists or biochemists without background in polymer theory. The lack of connection to biological function limits its appeal to a broader readership.
- **Technical soundness** The simulation approach is appropriate for the questions asked, and the use of multiple sequence variants and natural IDPs strengthens the study. However, several key claims lack quantitative support, including the near-ideal behavior in the dense phase, the universal collapse, and the interfacial results. The absence of detailed methods in the main text and the reliance on the ESI (not provided) limit the ability to assess technical rigor.
- **Readability for nonspecialists** The manuscript is clearly written but assumes familiarity with polymer physics concepts. The abstract and introduction are accessible, but the results section may be challenging for readers without a biophysics background. The figures are generally clear, but some (e.g., Fig. 2c) lack sufficient annotation to be interpretable without extensive text reading.

## Recommendation posture
Supportive if technical concerns are resolved. The manuscript addresses an important question with a systematic approach and presents potentially significant findings. However, the central claims require stronger quantitative support, including statistical comparisons, fitting details, and sensitivity analyses. The mechanistic understanding should be deepened, and the biological implications should be more explicitly developed. If these concerns are addressed, the work could make a valuable contribution to the field.