## Review setup
- **Input scope** Full manuscript text, including abstract, results, discussion, experimental procedures, and data availability statements.
- **Assessment boundary** Scientific soundness, validity of claims relative to presented evidence, methodological rigor, and clarity of the central hypothesis regarding O-GlcNAc transferase substrate recognition via compositional bias.
- **Shared manuscript claim summary** The authors propose that OGT recognizes intrinsically disordered protein regions based on amino acid compositional bias over extended sequence windows, rather than exclusively through short linear motifs. They support this with an experimentally derived negative dataset, a computational predictor (OGTcomPred), mutagenesis of FUS, and NMR binding studies.
- **Visible evidence base** Intact mass spectrometry of FET proteins, LC-MS/MS glycosylation site mapping, computational matrix optimization, FUS mutant glycosylation assays, NMR HSQC titrations, and dataset composition analyses.
- **Missing materials affecting confidence** Raw mass spectra, detailed NMR peak assignments, full list of negative dataset peptide sequences, code for OGTcomPred, and statistical details of correlation analyses were not fully provided in the manuscript text.

## Reviewer
- **Overall assessment** The manuscript addresses a significant gap in OGT substrate prediction by introducing a compositional bias framework supported by experimental validation. The concept is timely and the combination of negative dataset generation, computational modeling, and biophysical validation is commendable. However, several technical concerns regarding dataset size, statistical rigor, and the interpretation of NMR data limit the strength of the conclusions as currently presented.
- **Who would be interested in the results, and why** Researchers studying O-GlcNAc biology, intrinsically disordered proteins, enzyme substrate specificity, and computational predictors of post-translational modifications. The findings may also interest those developing tools for glycoproteomics and studying phase separation regulation.
- **Major strengths** The study provides a novel negative dataset for OGT substrates, which is a valuable community resource. The integration of computational prediction with experimental mutagenesis and NMR binding studies is a rigorous approach. The identification of compositional bias as a determinant of OGT recognition offers a new conceptual framework that could improve future prediction algorithms.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4.
- **Assessment against Nature-style criteria**  
  - **Originality** High. The concept of compositional bias in OGT substrate selection is a novel contribution that extends beyond existing sequence motif-based models.  
  - **Scientific importance** Moderate to high. Improving OGT site prediction has broad implications for understanding O-GlcNAc signaling, but the current evidence base is too limited to fully establish the paradigm.  
  - **Interdisciplinary readership** Moderate. The work bridges enzymology, bioinformatics, and biophysics, but the technical depth may limit accessibility to a general biochemistry audience.  
  - **Technical soundness** Adequate but with notable gaps. The mass spectrometry and NMR experiments are generally well executed, but the computational optimization and statistical validation require strengthening.  
  - **Readability for nonspecialists** The manuscript is clearly written, but the methods and results sections assume familiarity with MS, NMR, and computational prediction tools. A brief primer on OGT structure and substrate recognition would improve accessibility.
- **Recommendation posture** Supportive if technical concerns are resolved. The central hypothesis is promising and the experimental approach is sound, but the current evidence does not fully establish the claim that compositional bias is a primary determinant of OGT substrate recognition.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The negative dataset of five IDRs is used to infer a general compositional bias for OGT substrates.  
- **Evidence pointer** Results, "Computational optimization of OGT substrate prediction"; Figure 2  
- **Concern** The negative dataset consists of only five IDR proteins, yielding 135 peptides. This is a very small sample size from which to derive a general compositional bias. The authors acknowledge the dataset is "small" and "noisy," but the central claim of the paper rests on this dataset. The bias could be an artifact of the specific proteins chosen rather than a general property of OGT nonsubstrates.  
- **Why it matters** If the compositional bias is not generalizable, the OGTcomPred algorithm and the proposed model of OGT recognition would have limited utility. The paper's main contribution depends on the representativeness of this negative set.  
- **Resolution test** Expand the negative dataset to include a larger and more diverse set of IDRs from different functional classes and organisms. Alternatively, validate the compositional bias using an independent, larger dataset of experimentally confirmed non-substrates from published studies.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Statistical rigor  
- **Claim pointer** The correlation between predicted and observed glycosylation sites for FUS mutants (Pearson r = 0.84, p = 0.038) is presented as validation of OGTcomPred.  
- **Evidence pointer** Results, "Testing compositional bias"; Figure 4B  
- **Concern** The correlation is based on only six data points (WT plus five mutants). With such a small n, the p-value is highly sensitive to individual data points, and the confidence interval is likely very wide. The comparison to O-GlcNAcPredII (r = 0.59, p = 0.21) is also underpowered. No confidence intervals or effect sizes are reported.  
- **Why it matters** The claim that OGTcomPred outperforms existing predictors is not statistically supported. A reader cannot assess whether the difference between r = 0.84 and r = 0.59 is meaningful.  
- **Resolution test** Increase the number of FUS mutants tested, or use a bootstrap or permutation approach to estimate confidence intervals for the correlation coefficients. Report effect sizes and confidence intervals.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Interpretive validity  
- **Claim pointer** NMR data are interpreted as evidence that OGT-TPR binds FUS and that compositional mutations enhance binding.  
- **Evidence pointer** Results, "NMR evidence for direct interaction between OGT-TPR and FUS"; Figure 5  
- **Concern** The NMR experiments show signal loss in HSQC spectra upon addition of OGT-TPR, which is interpreted as binding. However, the authors note that samples phase separated in the absence of SUMO, and the experiments with SUMO-tagged TPR may not reflect physiological conditions. The average intensity ratio for WT (0.48 ± 0.24) and Mut-F (0.36 ± 0.22) have overlapping standard deviations, and no statistical test is reported to support the claim that Mut-F binds more strongly.  
- **Why it matters** The NMR data are central to the mechanistic model that TPR binding is enhanced by compositional changes. Without statistical support and with potential artifacts from phase separation, this conclusion is not robust.  
- **Resolution test** Perform replicate NMR titrations and report statistical significance of intensity ratio differences. Use conditions that avoid phase separation, or characterize the phase-separated state separately. Consider alternative biophysical methods (e.g., ITC, MST) to confirm binding affinity differences.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical validation  
- **Claim pointer** The optimized matrix (OGTcomPred) is presented as a predictive tool, but its performance is only tested on a small set of FUS mutants and four CBP IDRs.  
- **Evidence pointer** Results, "Test case: CREB-binding protein"; Figure 6; Table 3  
- **Concern** The CBP test case shows that OGTcomPred predicts many sites that are not experimentally glycosylated (e.g., 34 predicted in ID3, but only 5 confirmed). The authors acknowledge a "high false positive rate," but this undermines the utility of the predictor. No formal performance metrics (sensitivity, specificity, precision, ROC curves) are provided for the CBP dataset.  
- **Why it matters** A predictor with a high false positive rate is not practically useful. The paper claims to provide "insight into the broad specificity of OGT," but the predictive tool does not yet demonstrate sufficient accuracy to support this.  
- **Resolution test** Provide formal performance metrics for OGTcomPred on the CBP dataset and compare to existing predictors. Discuss strategies to reduce false positives, such as incorporating structural information or using a larger training set.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Abstract  
- **Evidence pointer** Abstract  
- **Issue** The abstract states that the negative dataset "suggests an amino acid compositional bias," but the strength of this suggestion is not qualified.  
- **Required correction** Add a phrase such as "based on a limited dataset" to temper the claim.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Methods  
- **Evidence pointer** Experimental procedures, "Matrix optimization and score calculation"  
- **Issue** The optimization algorithm is described only briefly. The starting matrix, convergence criteria, and number of iterations are not specified.  
- **Required correction** Provide a more detailed description of the optimization procedure, or reference a prior publication with full details.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Data presentation  
- **Affected element** Figure 3C  
- **Evidence pointer** Figure 3C  
- **Issue** The boxplots show separation between positive and negative sets, but the overlap is not quantified.  
- **Required correction** Report the median and interquartile ranges for both distributions, and consider adding a statistical test (e.g., Mann-Whitney U).

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Discussion  
- **Evidence pointer** Discussion, "Catalytic site interactions"  
- **Issue** The discussion of catalytic site interactions is speculative and does not directly reference new data from this study.  
- **Required correction** Either connect this section more explicitly to the current results or shorten it to avoid overreach.

- **Concern ID** R1-m5  
- **Severity** Minor  
- **Axis** Terminology  
- **Affected element** Throughout  
- **Evidence pointer** Results, "Computational optimization of OGT substrate prediction"  
- **Issue** The term "negative dataset" is used, but the authors do not define what constitutes a "non-glycosylated" protein. Is it based on lack of detection by MS?  
- **Required correction** Define the criteria for inclusion in the negative dataset explicitly.

## Risk / unsupported claims
- The claim that compositional bias is a general determinant of OGT substrate recognition is not fully supported by the limited negative dataset.
- The claim that OGTcomPred outperforms existing predictors is not statistically validated.
- The claim that compositional mutations enhance TPR binding is not statistically supported by the NMR data.
- The claim that the negative dataset "suggests" a bias is appropriately hedged, but the broader implications drawn in the discussion go beyond the evidence.
- The performance of OGTcomPred on CBP IDRs is not formally evaluated, and the high false positive rate is acknowledged but not addressed.