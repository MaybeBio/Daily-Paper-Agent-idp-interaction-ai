## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) as provided
- **Assessment boundary** Scientific content, methodological soundness, validity of claims, and presentation quality. No assessment of formatting or editorial fit.
- **Shared manuscript claim summary** The authors use atomistic molecular dynamics simulations of model condensates to identify physicochemical determinants of small-molecule partitioning, then develop a coarse-grained approach (MAPPS) to predict partitioning into biologically relevant condensates, validated against atomistic simulations.
- **Visible evidence base** Figures 1-6 (described in text), Tables S3, S4, S6, S7, S8 (referenced), Figures S1, S4, S7, S8, S9, S10, S11, S12 (referenced). No actual figure/table content was provided.
- **Missing materials affecting confidence** Actual figure and table content, simulation parameter details, force field validation data, error analysis details, and the full Supporting Information were not provided. This limits quantitative verification of all claims.

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely problem: predicting small-molecule partitioning into biomolecular condensates. The authors combine atomistic simulations with a coarse-grained modeling approach to derive empirical rules governing partitioning. The work is conceptually interesting and the development of a transferable minimal model (MAPPS) is a valuable contribution. However, several technical concerns need to be addressed, particularly regarding the validation methodology, the treatment of polar condensates, and the generalizability of the empirical relationship. The statistical analysis of the LCD-based condensate comparisons is weak, and the manuscript would benefit from clearer presentation of the limitations of the approach.

- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, drug discovery, and computational biophysics. The work provides a framework for predicting small-molecule partitioning, which is directly relevant to those developing therapeutics targeting condensates. The methodological approach (combining atomistic and coarse-grained simulations) will also interest computational biologists studying phase separation.

- **Major strengths** 1) The study addresses a significant and under-explored problem with clear therapeutic relevance. 2) The combination of atomistic and coarse-grained simulations is a sensible and powerful approach. 3) The development of a minimal, transferable model (MAPPS) is a practical contribution. 4) The identification of condensate polarity as a key determinant of partitioning is an important insight.

- **Major Concerns** 

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that MAPPS "reproduces atomistic partition coefficients" in both model systems and FUS LCD condensates.
- **Evidence pointer** Figures 4 and 5, location not provided
- **Concern** The validation of MAPPS against atomistic simulations is presented as successful, but the quantitative agreement is not rigorously established. For the peptide-based condensates, the authors state "better agreement" for hydrophobic condensates but acknowledge "systematic overestimation" for polar condensates. For the FUS LCD system, only four compounds were tested, and the correlation coefficient (r=0.99) is reported without confidence intervals or a proper error analysis. The claim of "good agreement" is therefore not fully supported by the evidence presented.
- **Why it matters** The central claim of the manuscript is that MAPPS can predict partitioning. If the validation is incomplete or only qualitative, the utility of the approach is not established. The systematic overestimation in polar condensates is particularly concerning, as these are biologically relevant.
- **Resolution test** Provide a quantitative comparison of K values from atomistic and CG simulations for all compounds and condensates, including error bars and a statistical measure of agreement (e.g., mean absolute error, R² with confidence intervals). For the FUS LCD system, test additional compounds with diverse physicochemical properties. Address the systematic overestimation in polar condensates, either by refining the model or by clearly stating the limitations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that the empirical relationship in Eq. 1 (εSM-X = εSM-Yfitted × AX × DX) is a valid approximation for determining SM-X interaction parameters.
- **Evidence pointer** Figure 3d, location not provided
- **Concern** The validation of Eq. 1 relies on a single correlation plot (Fig. 3d) with a reported correlation coefficient of 0.92 and RMSE of 0.12. However, the number of data points, the range of X residues tested, and the statistical significance of the correlation are not reported. The relationship may not hold for all amino acid types, particularly those with charged or polar side chains. The use of a random forest model for certain residues (Fig. S7) introduces an additional layer of approximation that is not fully described.
- **Why it matters** Eq. 1 is the core of the MAPPS approach. If the empirical relationship is not robust, the predictive power of the model is compromised. The lack of detail on the validation makes it difficult to assess the reliability of the approach.
- **Resolution test** Report the number of data points, the specific X residues tested, and the statistical significance of the correlation in Fig. 3d. Validate Eq. 1 for a broader set of amino acids, including charged and polar residues. Provide details on the random forest model, including its training data, features, and accuracy.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The claim that "more polar condensates exhibit selectivity toward certain compounds, suggesting that condensate-specific therapeutics can be engineered."
- **Evidence pointer** Figures 2 and 6, location not provided
- **Concern** The evidence for condensate-specific selectivity is indirect. The authors show that partitioning varies across condensates, but they do not demonstrate that this variation is sufficient for therapeutic selectivity. The differences in K values between condensates for a given compound are modest (e.g., K ranging from 1.1 to 2.1 for thiophenol across LCDs). The claim that this enables "condensate-specific therapeutics" is an overstatement without additional evidence, such as demonstrating that a compound can be designed to partition into one condensate over another with a meaningful therapeutic window.
- **Why it matters** The therapeutic relevance of the work is a key motivation. If the selectivity is not sufficient, the practical impact of the findings is diminished.
- **Resolution test** Provide a more nuanced discussion of the therapeutic implications, acknowledging the limitations of the observed selectivity. If possible, include a proof-of-concept example where a compound is designed to selectively partition into a target condensate.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The claim that the atomistic simulations of model condensates reveal that "solubility becomes a stronger regulator of partitioning in more polar condensates."
- **Evidence pointer** Figure 2, location not provided
- **Concern** The analysis of the determinants of partitioning relies on correlations between K and compound properties (logP, solubility, size). However, the statistical strength of these correlations is not reported, and the analysis does not account for potential confounding factors (e.g., the specific residues present in each condensate). The conclusion that solubility is a "stronger regulator" in polar condensates is based on a qualitative comparison of correlation patterns.
- **Why it matters** The mechanistic insights from the atomistic simulations are a key contribution. If the statistical analysis is weak, the conclusions are not robust.
- **Resolution test** Report correlation coefficients and p-values for the relationships between K and compound properties for each condensate. Use a multivariate analysis to disentangle the effects of different properties. Discuss potential confounding factors.

- **Minor Comments** 

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Introduction
- **Evidence pointer** Location not provided
- **Issue** The introduction is well-written but could benefit from a clearer statement of the specific gap in knowledge that this work addresses. The statement "the molecular mechanisms underlying small-molecule partitioning remain largely unknown" is somewhat generic.
- **Required correction** Briefly summarize what is known and what is unknown, and explicitly state how this work advances the field.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Location not provided
- **Issue** The methods section describes the simulation protocols but lacks some details necessary for reproduction, such as the exact number of simulation repeats, the criteria for determining equilibration, and the specific parameters for the random forest model.
- **Required correction** Provide additional details in the methods or supplementary information to ensure reproducibility.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Results
- **Evidence pointer** Figure 4, location not provided
- **Issue** The comparison between atomistic and CG results in Figure 4 is presented as a scatter plot, but the axes and units are not clearly described in the text. It is unclear whether the comparison is on a linear or logarithmic scale.
- **Required correction** Clarify the axes and scale in the figure legend and text.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Location not provided
- **Issue** The discussion of the limitations of the MAPPS approach is brief. The authors mention the overestimation in polar condensates but do not discuss the potential reasons in depth or suggest possible improvements.
- **Required correction** Expand the discussion of limitations and future directions.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Results
- **Evidence pointer** Figure 6, location not provided
- **Issue** The Kruskal-Wallis test result (H=7.60, p=0.055) is reported as "suggesting that while some differences may exist... the overall statistical evidence is weak." This is an appropriate interpretation, but the post-hoc comparison between EWSR1 and TIA1 (p=0.046) is reported without correction for multiple comparisons beyond the Bonferroni correction. The number of pairwise comparisons and the adjusted p-values should be reported.
- **Required correction** Report the number of pairwise comparisons and the adjusted p-values.

## Risk / unsupported claims
- The claim that "condensate-specific therapeutics can be engineered" is not directly supported by the data, as the observed selectivity is modest and no therapeutic proof-of-concept is provided.
- The claim that MAPPS "reproduces atomistic partition coefficients" is not fully supported due to the acknowledged systematic overestimation in polar condensates and the limited validation in the FUS LCD system.
- The generalizability of Eq. 1 to a wide range of small molecules and condensates is not established, as the validation is limited to a specific set of compounds and model systems.
- The statistical significance of the correlations between K and compound properties (logP, solubility, size) is not reported, making the mechanistic conclusions difficult to assess.
- The performance comparison of MAPPS to atomistic simulations (400 GPU hours vs. >1000 GPU hours) is presented as an advantage, but the comparison is not a like-for-like assessment of accuracy versus computational cost.