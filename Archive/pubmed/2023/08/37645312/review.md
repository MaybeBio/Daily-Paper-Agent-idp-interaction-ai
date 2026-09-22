## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, conclusions, and data/software availability statements.
- **Assessment boundary** Scientific and technical evaluation of the model development, parameterization, validation, and claims presented. No assessment of editorial fit or publication venue suitability.
- **Shared manuscript claim summary** The authors present CALVADOS 2, an updated coarse-grained model for intrinsically disordered proteins, which improves predictions of phase separation by tuning the interaction range cutoff of nonionic interactions. The model is parameterized against experimental data on conformational properties and validated against phase separation propensities across diverse sequences and conditions.
- **Visible evidence base** Abstract, full methods section, results and discussion, figures referenced (Figures 1-8, Supplementary Figures S1-S8), tables referenced (Tables 1-4), and data availability statements.
- **Missing materials affecting confidence** The manuscript text was provided without the actual figures, tables, or supplementary materials. Numerical values, statistical details, and visual data representations referenced in the text could not be directly inspected. The training and test set compositions (Tables 1-4) were not available for verification.

## Reviewer
- **Overall assessment** This manuscript presents a systematic and well-motivated investigation of how the interaction range cutoff in coarse-grained models of intrinsically disordered proteins affects predictions of chain compaction and phase separation. The authors identify a practical solution to a known temperature-scale mismatch in their previous model by reducing the nonionic interaction cutoff, and they reparameterize the model accordingly. The work is technically competent and the validation strategy is reasonable, though the evidence base available for this review is limited to text descriptions. The central claims regarding improved predictive accuracy are plausible but cannot be fully verified without access to the figures, tables, and numerical data. The manuscript would benefit from clearer reporting of uncertainty estimates and a more explicit discussion of the limitations of the training data.

- **Who would be interested in the results, and why** Researchers in the fields of computational biophysics, intrinsically disordered proteins, biomolecular condensates, and phase separation. The work is also relevant to those developing coarse-grained models for biological systems and to experimentalists studying phase behavior of IDPs who may use such models for interpretation or prediction. The methodological advance regarding interaction range tuning is of general interest to the molecular simulation community.

- **Major strengths** The systematic investigation of the interaction range cutoff effect is a valuable contribution. The use of a Bayesian optimization framework with regularization against multiple hydrophobicity scales is methodologically sound. The validation across diverse sequences, charge patterning, and salt concentrations demonstrates an effort toward generalizability. The identification of a practical solution to the temperature-scale mismatch is a useful practical advance.

- **Major Concerns** 
  - R1-M1 (Blocking: Yes)
  - R1-M2 (Blocking: No)
  - R1-M3 (Blocking: No)

- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
  - R1-m4

- **Technical failings that need to be addressed before the case is established** The primary technical concern is the inability to verify the quantitative claims without access to the figures and tables. The reported correlation coefficients and error estimates need to be examined in context. The sensitivity of the results to the choice of training data and the robustness of the optimization procedure require closer scrutiny.

- **Assessment against Nature-style criteria** 
  - Originality: The work is incremental rather than conceptually novel, building directly on the authors' previous CALVADOS model. The specific finding regarding interaction range effects is useful but not transformative.
  - Scientific importance: The improvement in predictive accuracy for phase separation of IDPs is of moderate importance to a specialized community. The work does not address fundamental questions that would elevate its significance.
  - Interdisciplinary readership: The manuscript is primarily of interest to computational biophysicists and IDP researchers. The technical nature of the content limits broader interdisciplinary appeal.
  - Technical soundness: The methodology appears sound based on the text description, but verification is limited by missing figures and tables. The statistical treatment and validation strategy are reasonable.
  - Readability for nonspecialists: The manuscript is clearly written for a specialist audience. The introduction provides adequate context, but the methods and results sections assume familiarity with coarse-grained modeling and phase separation concepts.

- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are plausible and the methodological approach is sound, but the evidence base available for this review is insufficient to fully establish the claims. Access to the figures, tables, and numerical data is required for a definitive assessment.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that CALVADOS 2 "accurately predicts conformational properties and propensities to undergo PS for diverse sequences and solution conditions" and that it has "improved predictive accuracy" compared to CALVADOS 1.
- **Evidence pointer** Figures 3, 5, 6, 7, 8; Tables 1-4; location not provided for specific data points
- **Concern** The central claims of improved predictive accuracy cannot be verified from the text alone. The manuscript references correlation coefficients (e.g., Pearson's r of 0.93 and 0.82 for CALVADOS 2 and 1, respectively) and comparisons with experimental data, but the actual figures, tables, and numerical values are not available for inspection. Without these, it is impossible to assess whether the reported improvements are statistically significant, whether the validation set is appropriately diverse, or whether the model performance is genuinely superior to existing alternatives.
- **Why it matters** The primary contribution of this work is the claim of improved predictive accuracy. If this claim cannot be substantiated with transparent and accessible evidence, the scientific value of the manuscript is substantially diminished. The reader must be able to evaluate the quality of the fit, the distribution of errors, and the robustness of the conclusions.
- **Resolution test** Provide the figures and tables with full numerical data, including error bars, sample sizes, and statistical significance tests. The correlation coefficients should be reported with confidence intervals. The validation set composition should be clearly documented, and the performance of CALVADOS 2 should be compared against CALVADOS 1 and other existing models on the same benchmarks.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Methodological robustness
- **Claim pointer** The manuscript states that "the effect of decreasing the cutoff from 4 to 2 nm results in a small increase in the radius of gyration whereas the PS propensity significantly decreases" and that this effect is "relatively insensitive to sequence length and composition."
- **Evidence pointer** Figures 3, 4; location not provided for specific data
- **Concern** The claim that the cutoff effect is "relatively insensitive to sequence length and composition" is based on a limited set of test sequences. The manuscript reports results for α-Synuclein, hnRNPA1 LCD, PNt, and Tau 2N4R, but the diversity of this set in terms of sequence length, charge distribution, and hydrophobicity is not fully characterized. The generalizability of this finding to the broader IDP sequence space is uncertain. Additionally, the mechanism proposed for the cutoff effect (the balance between single-chain and condensed-phase interactions) is plausible but not directly tested.
- **Why it matters** The practical utility of the proposed approach depends on its generalizability. If the cutoff effect varies significantly across sequence space, the model may not be transferable to new systems. A more systematic exploration of sequence space would strengthen the claim.
- **Resolution test** Expand the analysis to a larger and more diverse set of IDP sequences, systematically varying sequence length, charge patterning, and hydropathy. Quantify the variability of the cutoff effect across this set and report the range of observed effects. Consider testing the proposed mechanism directly by analyzing interaction energy distributions in single-chain versus condensed-phase simulations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Validation scope
- **Claim pointer** The manuscript claims that CALVADOS 2 "accurately predicts" phase separation propensities "at different temperatures and salt concentrations" and that it correctly predicts the behavior of Lge1 constructs.
- **Evidence pointer** Figures 3E-G, 6D-F, 8C; Table 4; location not provided for specific data
- **Concern** The validation of the model against phase separation data is limited to a relatively small number of systems. The manuscript reports testing on 26 sequences for phase separation predictions, but the diversity of these systems in terms of sequence features, solution conditions, and experimental methods is not fully described. The Lge1 validation is presented as a single case study with a reported discrepancy of "a hundred times larger c_sat" compared to experiments, which raises questions about the quantitative accuracy of the model even if the qualitative trends are correct.
- **Why it matters** The claim of accurate prediction across diverse conditions requires a sufficiently broad and challenging validation set. A limited validation set may not reveal systematic biases or failure modes of the model. The quantitative discrepancy for Lge1 suggests that the model may have limitations that are not fully acknowledged.
- **Resolution test** Expand the validation set to include more systems with experimentally measured phase separation behavior, covering a wider range of sequence features and solution conditions. Report the distribution of prediction errors and identify any systematic biases. Discuss the implications of the Lge1 discrepancy for the model's quantitative accuracy and consider whether additional parameterization or model refinement is needed.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of reporting
- **Affected element** Methods section, optimization procedure
- **Evidence pointer** Section 2.3, location not provided
- **Issue** The description of the optimization procedure lists items (i), (ii), and (v), but items (iii) and (iv) are missing. This appears to be an editing error that disrupts the logical flow of the methods description.
- **Required correction** Renumber the items sequentially or include the missing items (iii) and (iv) to ensure the description is complete and coherent.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results section, correlation coefficients
- **Evidence pointer** Section 3, Figure 7C, location not provided
- **Issue** The manuscript reports Pearson's correlation coefficients of 0.93 and 0.82 for CALVADOS 2 and CALVADOS 1, respectively, for predicted versus experimental c_sat values. However, no confidence intervals or p-values are reported, and the number of data points (26 sequences) is relatively small.
- **Required correction** Report confidence intervals for the correlation coefficients and specify the number of data points. Consider also reporting the root-mean-square error or median absolute error to provide a more complete picture of prediction accuracy.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of discussion
- **Affected element** Discussion of limitations
- **Evidence pointer** Section 3, Section 4, location not provided
- **Issue** The manuscript acknowledges limitations regarding low salt concentrations but does not discuss other potential limitations, such as the accuracy of the model for sequences with extreme charge content, the sensitivity of results to the choice of training data, or the transferability of the model to conditions outside the training range.
- **Required correction** Add a brief discussion of additional limitations and potential sources of systematic error. This would provide a more balanced assessment of the model's applicability.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section, simulation details
- **Evidence pointer** Section 2.1, location not provided
- **Issue** The manuscript states that simulations are performed using HOOMD-blue v2.9.3 and OpenMM v7.5, but does not provide specific version details for the force field parameters or the exact simulation protocol for the direct-coexistence simulations beyond what is described.
- **Required correction** Provide additional details on the simulation protocol, including the exact form of the nonionic potential, the treatment of long-range electrostatics, and the criteria for determining equilibrium in the direct-coexistence simulations. This would enhance reproducibility.

## Risk / unsupported claims
- The claim that CALVADOS 2 "accurately predicts" phase separation propensities across diverse conditions is not fully supported by the available evidence, as the validation set is limited and the quantitative accuracy varies (e.g., the Lge1 case shows a 100-fold discrepancy).
- The claim that the cutoff effect is "relatively insensitive to sequence length and composition" is based on a limited set of test sequences and may not generalize to the full IDP sequence space.
- The statement that "the range of interaction of the Lennard-Jones potential may be too large" is presented as a speculation and is not directly tested in this work.
- The performance comparison between CALVADOS 2 and CALVADOS 1 is reported only through correlation coefficients without confidence intervals, making it difficult to assess the statistical significance of the improvement.
- The manuscript's claim of "improved predictive accuracy" is relative to CALVADOS 1 only and does not include comparisons with other existing coarse-grained models for IDPs, limiting the assessment of the model's overall standing in the field.