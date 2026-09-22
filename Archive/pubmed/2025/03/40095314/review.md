## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors present a transferable coarse-grained polymer model (SOP-IDP) for intrinsically disordered proteins, reporting that simulated radii of gyration correlate with SAXS-derived values (correlation coefficient 0.96), hydrodynamic radii match FCS data for two proteins, SAXS profiles are nearly superimposable for 36 IDPs, Flory scaling with exponent 0.588 holds for Rg and Ree with negligible finite-size corrections, finite-size corrections are required for Rh, sequence-specific features emerge from hierarchical clustering of conformational ensembles, and PRE data for alpha-synuclein are reproduced without parameter adjustment.
- **Visible evidence base** Abstract text only; no figures, tables, methods descriptions, or numerical data beyond the stated correlation coefficient, scaling exponents, and prefactors
- **Missing materials affecting confidence** Full manuscript, methods section, simulation details, force field parameters, experimental data sources, statistical analyses, figure panels, and supplementary information

## Reviewer
- **Overall assessment** The abstract describes a potentially useful transferable model for IDP simulations with broad applicability claims. The reported agreement with multiple experimental observables is encouraging. However, the abstract alone provides insufficient detail to evaluate the technical soundness of the model, the statistical rigor of the comparisons, or the robustness of the scaling law conclusions. The claim of negligible finite-size corrections is surprising given established polymer theory and requires careful scrutiny. The clustering analysis and its biological interpretation are presented without methodological context.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, computational biophysicists developing coarse-grained models, experimentalists interpreting SAXS, FCS, and PRE data for IDPs, and investigators interested in phase separation and IDP-nucleic acid interactions. The transferable nature of the model could appeal to a broad community seeking efficient simulations of IDP conformational ensembles.
- **Major strengths** The model appears to achieve agreement with multiple independent experimental observables (Rg, Rh, SAXS profiles, PRE) without parameter re-adjustment, which suggests transferability. The reported correlation coefficient of 0.96 for Rg across many IDPs is strong. The scaling analysis connects simulation results to polymer physics frameworks, providing theoretical context. The clustering analysis hints at sequence-specific features beyond average properties.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3  
  - R1-m4
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria**  
  Originality: The SOP-IDP model appears to be an incremental advance over existing coarse-grained IDP models, though the combination of transferability across multiple observables and the scaling analysis may offer some novelty. The claim of negligible finite-size corrections contradicts theoretical expectations and, if confirmed, would be notable.  
  Scientific importance: IDP characterization is a significant problem in biophysics, and a transferable model with demonstrated accuracy would be valuable. However, the abstract does not establish whether the model outperforms existing approaches.  
  Interdisciplinary readership: The work bridges polymer physics, computational biology, and experimental biophysics, which could attract readers across these fields. The abstract is written in a way that is largely accessible to nonspecialists.  
  Technical soundness: Cannot be adequately assessed from the abstract alone. Key details on model construction, simulation protocols, error analysis, and comparison statistics are missing.  
  Readability for nonspecialists: The abstract is generally clear, though terms such as "self-organized polymer model" and "paramagnetic relaxation enhancement" are used without definition. The phrase "suggestive of of sequence-specific features" contains a typographical error.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents promising results, but the absence of methodological detail and the surprising scaling claims require full manuscript evaluation. A supportive posture would require resolution of the technical concerns identified below.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The claim that "finite size corrections to scaling, expected on theoretical grounds, are negligible for Rg and Ree"  
- **Evidence pointer** Abstract, scaling law discussion; location not provided  
- **Concern** The assertion that finite-size corrections are negligible for Rg and Ree contradicts well-established polymer theory, which predicts significant corrections for chains of finite length, particularly for N values typical of IDPs (often 50 to 500 residues). The abstract provides no data on the range of N studied, the magnitude of deviations from the asymptotic scaling law, or the statistical power of the test used to conclude that corrections are negligible.  
- **Why it matters** If finite-size corrections are indeed negligible, this would be a surprising result requiring robust evidence. If the conclusion is an artifact of insufficient sampling, limited N range, or inappropriate fitting procedures, the scaling analysis would be misleading. This claim is central to the paper's theoretical contribution.  
- **Resolution test** Provide a plot of Rg/N^0.588 versus N showing flat behavior across the full N range, with error bars and a statistical test for the slope. Alternatively, show that including a correction term of the form N^(-0.5) does not improve the fit using an information criterion. Report the N range and number of IDPs at each length.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The claim that "the calculated SAXS profiles for 36 IDPs are also nearly superimposable on the experimental profiles"  
- **Evidence pointer** Abstract, SAXS comparison; location not provided  
- **Concern** The abstract does not specify the metric used to quantify "nearly superimposable," the tolerance for agreement, or whether the comparison was performed on absolute or normalized intensity scales. SAXS profile comparisons are sensitive to background subtraction, concentration effects, and the q-range considered. Without a defined goodness-of-fit measure (e.g., chi-squared, reduced chi-squared, or Cramer-von Mises statistic) and the q-range used, this claim cannot be evaluated.  
- **Why it matters** The SAXS agreement is a primary validation of the model. If the comparison is qualitative or uses a lenient metric, the claim of transferability is weakened. This is a central pillar of the paper's evidence.  
- **Resolution test** Report a quantitative goodness-of-fit statistic for each of the 36 IDPs, the q-range used, and the experimental uncertainty in the SAXS data. Show representative overlays with residuals.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The claim that "the values of the radius of gyration (Rg) obtained from SOP-IDP simulations are in excellent agreement (correlation coefficient of 0.96) with those estimated from SAXS experiments"  
- **Evidence pointer** Abstract, Rg comparison; location not provided  
- **Concern** A correlation coefficient of 0.96 indicates a strong linear association but does not establish accuracy. Systematic offsets or scaling errors would not be captured by the correlation coefficient alone. The abstract does not report the root-mean-square deviation, the mean absolute error, or whether the slope of the regression line is consistent with unity and the intercept with zero.  
- **Why it matters** The Rg agreement is a headline result. If the model systematically overestimates or underestimates Rg by a constant factor, the correlation could still be high while the accuracy is poor. This affects the validity of the scaling analysis and the model's predictive power.  
- **Resolution test** Report the slope, intercept, and root-mean-square deviation of the Rg comparison, along with a Bland-Altman plot or equivalent analysis of agreement.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Scientific importance  
- **Claim pointer** The claim that "the ensemble of conformations partitions into three distinct clusters, having different equilibrium populations and structural properties"  
- **Evidence pointer** Abstract, clustering analysis; location not provided  
- **Concern** The abstract does not describe the clustering method, the similarity metric used, the criteria for determining the number of clusters, or the structural properties that distinguish the clusters. Without this information, the biological significance of the three clusters cannot be assessed. The claim that this reveals "sequence-specific features" is not substantiated by any specific examples.  
- **Why it matters** The clustering analysis is presented as a novel contribution beyond average properties. If the clustering is an artifact of the method or if the clusters are not robust across simulation replicates, the conclusion would be weakened. This aspect may be of interest to readers seeking sequence-structure relationships in IDPs.  
- **Resolution test** Describe the clustering algorithm, validation of cluster number (e.g., silhouette analysis), and show that clusters are reproducible across independent simulations. Provide specific examples of sequence features that correlate with cluster membership.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Readability  
- **Affected element** Abstract text  
- **Evidence pointer** Abstract, scaling law discussion; location not provided  
- **Issue** The phrase "suggestive of of sequence-specific features" contains a duplicated preposition.  
- **Required correction** Revise to "suggestive of sequence-specific features."

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Model description  
- **Evidence pointer** Abstract, model introduction; location not provided  
- **Issue** The abstract states the SOP-IDP model is "transferable" but does not specify what parameters were transferred from previous work or whether any fitting to the current dataset was performed.  
- **Required correction** Clarify in the abstract or methods whether any parameters were optimized against the experimental data used for validation.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Simulation details  
- **Evidence pointer** Abstract, methods reference; location not provided  
- **Issue** No information is provided on simulation length, number of independent trajectories, temperature, or solvent model, which are essential for reproducing the results.  
- **Required correction** Include key simulation parameters in the methods section or supplementary information.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Statistical rigor  
- **Affected element** Rh comparison  
- **Evidence pointer** Abstract, hydrodynamic radius comparison; location not provided  
- **Issue** The claim of "nearly quantitative agreement" for Rh is based on only two proteins (AP180 and Epsin). The abstract does not report the magnitude of the deviation or the experimental uncertainty.  
- **Required correction** Report the percent difference between predicted and measured Rh values and the experimental error bars. Consider acknowledging the limited sample size in the abstract.

## Risk / unsupported claims
- The claim of negligible finite-size corrections for Rg and Ree is unsupported by the abstract alone and contradicts theoretical expectations; requires full data and statistical analysis.
- The claim of "nearly superimposable" SAXS profiles for 36 IDPs is unsupported without a quantitative goodness-of-fit metric and q-range specification.
- The claim of "excellent agreement" for Rg based solely on a correlation coefficient is insufficient; accuracy metrics are needed.
- The biological significance of the three clusters from hierarchical clustering is unsupported without methodological details and specific examples.
- The claim that the model "sets the stage for several applications" is speculative and not directly supported by the presented results.
- The transferability of the model without parameter re-adjustment for PRE data is stated but not verifiable from the abstract.