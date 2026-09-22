## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) as provided
- **Assessment boundary** Scientific and technical evaluation of the described method, its validation, and the claims made; no assessment of code availability or container functionality beyond what is stated
- **Shared manuscript claim summary** The authors present PredIDR, a deep convolutional neural network for predicting protein intrinsic disorder regions, trained on X-ray missing residues from the PDB. They report that PredIDR participated in CAID2 and performed as well as or better than state-of-the-art methods, and that it outperforms 11 CAID1 methods on the CAID1-DisProt-PDB dataset.
- **Visible evidence base** Tables 1-9, Figures 1-4, equations, dataset descriptions, and comparative performance metrics as described in the text
- **Missing materials affecting confidence** The actual performance data (numerical values in Tables 3-9) are not visible in the provided text; only descriptions of rankings and relative improvements are given. The Additional files (1-17) are referenced but not provided. The CAID2 assessment reference [5] is cited but not available for verification.

## Reviewer
- **Overall assessment** The manuscript describes a reasonable and well-motivated approach to disorder prediction using a convolutional neural network trained on X-ray missing residues. The methodological choices (feature combinations, ensembling, smoothing) are systematically explored, and the participation in CAID2 provides an external benchmark. However, the manuscript as presented has several significant weaknesses. The most critical issue is that the actual performance numbers are not visible in the provided text, making it impossible to independently assess the magnitude of the claimed improvements or the statistical significance of the results. The claim that PredIDR is "as accurate as the top state-of-the-art IDR prediction methods" is not substantiated with specific numerical comparisons. Additionally, the analysis of the two disorder flavors (X-ray vs. non-X-ray) is interesting but the interpretation is somewhat circular, given that the method is trained exclusively on X-ray data. The manuscript would benefit from a more critical discussion of the limitations of using X-ray missing residues as a proxy for disorder, and from a clearer articulation of what biological insight the method provides beyond improved prediction accuracy.

- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein structure prediction and disorder prediction would be the primary audience. Researchers developing deep learning methods for biological sequence analysis would also find the architectural choices and training strategy relevant. The CAID community and users of the CAID Prediction Portal would be interested in a new method that performs competitively on the CAID2 benchmark. The manuscript may also be of interest to structural biologists who use disorder predictions to guide experimental design, particularly those working with X-ray crystallography where missing residues are a common observation.

- **Major strengths** The manuscript addresses a relevant problem in structural biology with a clear practical application. The systematic exploration of feature combinations, ensembling, and smoothing is methodologically sound and provides useful guidance for practitioners. The participation in CAID2, a community-driven benchmark, lends external validity to the evaluation. The creation of two additional test sets (CAID2-Xray-PDB and CAID2-NoX-PDB) to dissect performance on different disorder flavors is a thoughtful analytical approach. The method is made freely available through the CAID Prediction Portal and as a container, which supports reproducibility and community adoption.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The abstract states that PredIDR "was as accurate as the top state-of-the-art IDR prediction methods" in CAID2, and Section 3.5 claims specific rankings (e.g., "PredIDR_long ranked first and fourth and PredIDR_short fourth and sixth when considering AUC_ROC and AUC_PR, respectively").
- **Evidence pointer** Tables 7, 8, and 9; location not provided for numerical values
- **Concern** The actual numerical values for AUC_ROC and AUC_PR in Tables 7-9 are not visible in the provided text. Without these numbers, it is impossible to assess the magnitude of the differences between PredIDR and other methods, whether these differences are meaningful, or whether the claimed rankings are robust. The text describes rankings but does not provide the underlying data needed to evaluate statistical significance or practical relevance.
- **Why it matters** The central claim of the manuscript is that PredIDR performs competitively with or better than state-of-the-art methods. This claim cannot be evaluated without the actual performance metrics. Rankings alone are insufficient, as small differences in AUC values may not be practically significant, and the variance across methods is not reported.
- **Resolution test** Provide the full numerical results for all methods on all datasets, including confidence intervals or statistical tests where appropriate. The authors should also report the variance across the ten ensemble members to demonstrate the stability of the rankings.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim substantiation
- **Claim pointer** Section 3.4 states that "PredIDR_long and PredIDR_short outperform 11 IDR prediction methods in both measures" on the CAID1-DisProt-PDB dataset.
- **Evidence pointer** Table 6; location not provided for numerical values
- **Concern** The claim of outperforming 11 CAID1 methods is made without presenting the actual performance values. It is unclear whether this comparison includes all 11 methods that provided outputs, or only a subset. The text notes that 31 methods participated in CAID1 but only 11 provided outputs over all 646 sequences, which raises the question of whether the comparison is biased by excluding methods that did not complete the benchmark.
- **Why it matters** The comparison to CAID1 methods is used to support the general claim of state-of-the-art performance. If the comparison is incomplete or the differences are marginal, the claim is overstated. The exclusion of methods that did not provide full outputs could introduce selection bias.
- **Resolution test** Present the full comparison table with all methods that participated in CAID1, including those that did not provide complete outputs, and discuss any potential biases. Report the numerical values and, where possible, statistical significance of the differences.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Methodological rigor
- **Claim pointer** Section 2.2 describes the construction of the training set, including the balancing algorithm and the creation of artificial negative examples from structured regions.
- **Evidence pointer** Section 2.2, Figures 2 and 3, Tables 1 and 2
- **Concern** The balancing procedure is described in detail, but the rationale for some choices is not fully justified. For example, the decision to cut longer structured regions to match the length of paired disordered regions, and the random choice of cutting direction for non-IDR_M regions, could introduce artifacts. The text does not discuss whether the balancing procedure was validated, e.g., by comparing performance on the original unbalanced data versus the balanced data.
- **Why it matters** The training data construction directly affects the learned model. If the balancing procedure introduces biases or artifacts, the model's performance on real-world data may be compromised. The manuscript should demonstrate that the balancing procedure does not negatively impact generalization.
- **Resolution test** Provide an analysis of the model's performance with and without the balancing procedure, or at least a discussion of the potential artifacts and why they are unlikely to affect the results. The authors should also report the distribution of sequence lengths and disorder segment lengths in the training set to help readers assess the representativeness of the data.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretability and biological relevance
- **Claim pointer** Section 3.5 concludes that PredIDR performs best on X-ray-derived disorder but not on non-X-ray disorder, "probably because they are trained only on X-ray missing residues."
- **Evidence pointer** Tables 8 and 9, Section 3.5
- **Concern** The interpretation that the performance difference is due to training data is plausible but not rigorously tested. The authors do not explore whether the difference could be due to other factors, such as the length distribution of disorder segments in the two datasets, the sequence context, or the annotation quality. The conclusion is presented as self-evident, but alternative explanations are not considered.
- **Why it matters** The manuscript's main contribution is a method trained on X-ray missing residues. If the performance difference is not solely due to training data, the authors' interpretation may be misleading, and the proposed future work (training on non-X-ray annotations) may not yield the expected improvement.
- **Resolution test** Conduct additional analyses to isolate the effect of training data, e.g., by training a model on non-X-ray annotations and comparing performance on both datasets, or by analyzing the characteristics of the disorder segments in each dataset that correlate with prediction performance.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.2, description of CAID2-Xray-PDB and CAID2-NoX-PDB construction
- **Evidence pointer** Section 2.2, Figure 1
- **Issue** The description of how the two datasets were derived from CAID2-Disorder-PDB is somewhat unclear. The text states that CAID2-Xray-PDB is "generated by subtracting the Disorder-NOX dataset to the CAID2-Disorder-PDB," but the exact procedure (e.g., how overlapping regions are handled, how sequences with mixed annotations are treated) is not specified.
- **Required correction** Provide a more detailed and precise description of the dataset construction, including a step-by-step procedure and the criteria for including or excluding sequences and residues.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2.6, training details
- **Evidence pointer** Section 2.6
- **Issue** The manuscript does not report the number of trainable parameters, the training time, or the computational resources required. This information is useful for readers who may want to reproduce or adapt the method.
- **Required correction** Add a brief description of the model size, training time, and hardware used.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Section 3.2, ensemble improvement
- **Evidence pointer** Table 4
- **Issue** The text states that the ensemble leads to "a clear significant improvement" but no statistical test is reported. The improvement in AUC_ROC is described as 0.8-2.0%, which may or may not be statistically significant depending on the variance.
- **Required correction** Report the variance across ensemble members and, if possible, perform a statistical test (e.g., a paired test across the validation sets) to support the claim of significance.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Section 3.3, smoothing analysis
- **Evidence pointer** Table 5
- **Issue** The text notes that the optimal window size varies across datasets and is proportional to the fraction of disordered residues. However, the practical guidance for users is unclear: should users select the window size based on the expected disorder content of their target proteins?
- **Required correction** Provide a clear recommendation for users on how to choose the window size, or state that the default window size of 9 is appropriate for most applications.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section 2.1, data filtering
- **Evidence pointer** Section 2.1
- **Issue** The text states that proteins were filtered to have sequence identity lower than 25% and length longer than 51 residues, but the exact version of CD-HIT and the parameters used are not specified.
- **Required correction** Provide the exact software version and parameters used for CD-HIT clustering.

## Risk / unsupported claims
- The claim that PredIDR is "as accurate as the top state-of-the-art IDR prediction methods" is not supported by visible numerical data; only rankings are provided.
- The claim that PredIDR "outperforms 11 CAID1 methods" is not supported by visible numerical data.
- The interpretation that the performance difference between X-ray and non-X-ray disorder datasets is due to training data is plausible but not rigorously tested.
- The statement that "the higher the fraction of disordered residues, the better the performance" is based on only three validation sets and may not generalize.
- The claim that the optimal smoothing window size is proportional to the fraction of disordered residues is based on a limited number of observations and lacks a mechanistic explanation.