## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, and figure legends. Supplementary information referenced but not provided.
- **Assessment boundary** Technical soundness of the proposed method, validity of the training strategy, evidence supporting performance claims, and generalizability of the approach to stated application domains.
- **Shared manuscript claim summary** The authors present DEEP Picker, a deep neural network for automated peak picking and deconvolution of two-dimensional NMR spectra. The network is trained exclusively on synthetic one-dimensional spectra with known ground truth, applied to rows and columns of 2D spectra, and combined via a decision rule to identify 2D cross-peaks. Performance is demonstrated on protein HSQC spectra, an intrinsically disordered protein, and a mouse urine metabolomics sample.
- **Visible evidence base** Main text figures 1 through 8, tables referenced in supplementary information (Table S2, Table S3), and qualitative descriptions of performance. No quantitative benchmarking data, runtime measurements, or comparison tables are present in the supplied material.
- **Missing materials affecting confidence** Supplementary figures and tables (S2, S3, S6, S7, S8, S9), the reporting summary, details of the nonlinear peak fitting procedure, hyperparameter tuning results, and any code or model availability statements. Quantitative performance metrics referenced in the text are not accessible.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant problem in NMR spectroscopy, namely the automated and accurate identification of overlapping peaks, which remains a bottleneck for many downstream analyses. The idea of training a convolutional neural network on synthetic data with mathematically defined ground truth is sensible and avoids the subjectivity of human-annotated training sets. The architecture is appropriately simple and the computational cost appears modest. However, the evidence presented in the main text is largely qualitative. Quantitative performance metrics are relegated to supplementary material that was not provided, making it impossible to assess the central claims of accuracy and robustness. The generalization from 1D to 2D via row and column analysis is pragmatic but introduces potential failure modes that are only partially addressed. The manuscript would benefit from clearer benchmarking against existing methods and a more rigorous treatment of failure cases.
- **Who would be interested in the results, and why** NMR spectroscopists working on protein structure determination, dynamics studies, and metabolomics would be the primary audience. Researchers developing computational tools for spectral analysis would also find the approach relevant. The promise of reduced manual intervention and improved reproducibility in peak picking has broad appeal within the biomolecular NMR community.
- **Major strengths** The use of synthetic training data with mathematically defined ground truth is a clear strength, as it avoids the circularity of human-annotated labels. The network architecture is compact and computationally efficient. The demonstration across multiple sample types, including intrinsically disordered proteins and complex metabolomics mixtures, suggests general applicability. The explicit handling of ambiguous cases, such as spectra that can be explained by different numbers of peaks, shows awareness of the underlying challenges.
- **Major Concerns** The central quantitative claims are not verifiable from the supplied material. The comparison to existing methods is only mentioned qualitatively. The treatment of false positives and false negatives lacks detail. The robustness of the 2D extension via row and column analysis is not systematically characterized. The choice of the 3% threshold for defining resolvable peaks is presented without sensitivity analysis.
- **Minor Comments** The manuscript would benefit from a clearer statement of the limitations of the approach. The discussion of phase error tolerance is vague. The claim that DEEP Picker is the default engine of the COLMAR suite is noted but not substantiated with any usage statistics or user feedback.
- **Technical failings that need to be addressed before the case is established** The absence of quantitative performance metrics in the main text is a significant gap. The lack of a direct comparison with existing peak pickers, such as NMRPipe, Sparky, or NMRViewJ, in terms of accuracy and speed, weakens the case for superiority. The sensitivity of the method to the training data distribution, particularly the range of peak widths and overlap severities, is not explored.
- **Assessment against Nature-style criteria**  
  *Originality*: The application of deep learning to NMR peak picking is not entirely new, but the specific training strategy using synthetic data with a mathematical resolvability criterion is a distinctive contribution.  
  *Scientific importance*: The problem addressed is important and the potential for automation and standardization is significant. However, the importance is not fully established without quantitative evidence of improved accuracy over existing methods.  
  *Interdisciplinary readership*: The topic is of interest to NMR spectroscopists and computational biologists, but the presentation assumes familiarity with NMR terminology that may limit broader readership.  
  *Technical soundness*: The approach is technically plausible, but the evidence base is insufficient to fully assess soundness. The lack of quantitative results and sensitivity analyses is a concern.  
  *Readability for nonspecialists*: The manuscript is generally well written, but the methods section assumes significant prior knowledge of NMR spectroscopy and neural network architectures.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the demonstrations are suggestive, but the current evidence base does not fully establish the claimed accuracy and robustness. Quantitative benchmarking and a more detailed analysis of failure modes are required.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that DEEP Picker is able to correctly identify overlapping peaks, including ones that are challenging for expert spectroscopists and existing computational methods alike.
- **Evidence pointer** Results section, Figures 5 through 8, Table S2 (not provided)
- **Concern** The central performance claim is supported only by qualitative visual inspection of selected spectral regions. The quantitative metrics referenced in Table S2 are not available in the supplied material. Without these data, it is not possible to verify the accuracy of peak identification, the rate of false positives and false negatives, or the comparison with existing methods.
- **Why it matters** The claim of superiority over existing methods is a key selling point of the manuscript. If the quantitative data do not support this claim, the contribution is substantially weakened.
- **Resolution test** Provide the full quantitative results from Table S2 in the main text or as accessible supplementary material, including precision, recall, and F1 scores for each test case, and a direct comparison with at least one existing peak picker.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological validation
- **Claim pointer** The training strategy relies on a mathematical criterion, based on nonlinear peak fitting with a 3% maximal error threshold, to define resolvable peaks and exclude ambiguous cases.
- **Evidence pointer** Results section, "Generation of the training set", Figure 1
- **Concern** The choice of the 3% threshold is presented without justification or sensitivity analysis. It is unclear how this threshold affects the performance of the trained network on experimental data with different noise levels, linewidths, or baseline distortions. The manuscript also does not discuss how the threshold interacts with the network's ability to generalize to spectra that deviate from the training distribution.
- **Why it matters** The threshold determines the boundary between resolvable and non-resolvable peaks in the training data, and therefore directly shapes the network's behavior. An arbitrary or poorly chosen threshold could lead to systematic biases in peak identification.
- **Resolution test** Provide a sensitivity analysis showing how the network's performance on experimental spectra varies as a function of the threshold. Justify the chosen value with reference to the distribution of fitting errors in the training set.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability
- **Claim pointer** The manuscript states that DEEP Picker can be applied to 2D spectra by analyzing rows and columns separately and combining the results, and that this approach is remarkably accurate and robust for very different NMR samples.
- **Evidence pointer** Results section, "Generalization to 2D spectra", Figures 4 through 8
- **Concern** The row and column approach is a heuristic that may fail for certain classes of 2D peak shapes, such as those with significant overlap in both dimensions simultaneously, or for peaks that are not aligned with the spectral grid. The manuscript does not characterize the conditions under which this approach breaks down, nor does it provide a systematic evaluation of the error introduced by the 2D reconstruction procedure.
- **Why it matters** The 2D extension is essential for the practical utility of the method. If the approach fails for common spectral patterns, the claimed generalizability is not justified.
- **Resolution test** Provide a systematic evaluation of the 2D reconstruction on synthetic 2D spectra with controlled overlap patterns, including cases where peaks overlap in both dimensions. Quantify the error in peak position and amplitude as a function of overlap severity.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Comparison with existing methods
- **Claim pointer** The manuscript implies that DEEP Picker outperforms existing peak pickers, but no direct quantitative comparison is presented in the main text.
- **Evidence pointer** Results section, Figures 5 through 8, Figure S6 (not provided)
- **Concern** The only comparison mentioned is in Figure S6, which is not provided. Without a direct comparison on the same datasets, it is difficult to assess whether DEEP Picker offers a meaningful improvement over established tools.
- **Why it matters** The novelty of the approach is partly based on its claimed superiority. A fair comparison is essential to establish this.
- **Resolution test** Provide the results of a direct comparison with at least two existing peak pickers on the same experimental datasets, using identical evaluation criteria.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section, "Design and training of DEEP Picker"
- **Evidence pointer** Figure 2
- **Issue** The description of the network architecture is brief. The number of filters per layer, the stride, and the padding are not specified. The statement that the network has 8037 trainable parameters is given, but the layer-wise breakdown is not.
- **Required correction** Provide a table or text listing the number of filters, kernel sizes, strides, and padding for each layer.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section, "Generation of the training set"
- **Evidence pointer** Location not provided
- **Issue** The procedure for generating synthetic spectra is described, but the exact ranges for peak widths, amplitudes, and overlap severities are not given. The noise model is not specified.
- **Required correction** Provide the full parameter ranges and the noise model used for synthetic data generation.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section, "Application to 15N–1H HSQC spectra of proteins"
- **Evidence pointer** Figure 6
- **Issue** The manuscript states that DEEP Picker works well for globular proteins, but the number of spectra tested and the diversity of protein sizes and shapes are not described.
- **Required correction** Provide a summary table listing the proteins tested, their molecular weights, and the number of cross-peaks expected versus identified.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results section, "Application to NOESY and TOCSY spectra"
- **Evidence pointer** Figure 8
- **Issue** The claim that DEEP Picker identifies individual multiplet components due to J-splittings is interesting, but it is not clear whether this is always desirable, as multiplet components may not correspond to distinct chemical species.
- **Required correction** Clarify whether multiplet components are reported as separate peaks in the final output, and discuss the implications for downstream analysis.

## Risk / unsupported claims
- The claim that DEEP Picker outperforms existing computational methods is not supported by the supplied material, as the relevant comparison data are in the unavailable Figure S6.
- The claim that DEEP Picker is remarkably accurate and robust for very different NMR samples is not quantitatively supported in the main text.
- The statement that DEEP Picker can tolerate phase errors of a few degrees is not supported by any experimental evidence in the supplied material.
- The claim that DEEP Picker is the default peak picking and peak fitting engine of the COLMAR suite is noted but not substantiated.
- The assertion that the 3% threshold best reproduces the consensus among a group of NMR experts is not supported by any data or analysis.