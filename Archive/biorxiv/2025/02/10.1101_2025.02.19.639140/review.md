## Review setup
- **Input scope** Full manuscript text including abstract, results, discussion, methods, and supplementary figure/table references
- **Assessment boundary** Scientific claims, methodology, data interpretation, and internal consistency based solely on the provided manuscript text
- **Shared manuscript claim summary** The authors use the ParSe algorithm to predict phase-separating intrinsically disordered regions (PS IDRs) in human proteins, and report that pathogenic missense mutations are approximately three-fold enriched in PS IDRs compared to non-PS IDRs, that disease-associated proteins are enriched for predicted phase separation behavior across many disease categories, that SLiMs within PS IDRs show exceptionally high pathogenicity, and that phosphorylation sites in PS IDRs are mostly benign when mutated.
- **Visible evidence base** Abstract, full results section, discussion, methods, references to Figures 1-6, Figure S1-S14, Tables S1-S3, and supplementary information
- **Missing materials affecting confidence** Figures 1-6 and all supplementary figures/tables are referenced but not provided; no raw data or statistical output tables are included; no accession numbers or version details for the ParSe algorithm beyond a weblink; no details on the exact composition of disease sub-groupings beyond what is stated

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question regarding the relationship between missense mutations in intrinsically disordered regions, phase separation, and disease. The authors leverage their previously developed ParSe algorithm to perform a large-scale bioinformatics analysis. The central finding, a three-fold enrichment of pathogenic mutations in predicted PS IDRs relative to non-PS IDRs, is potentially significant. However, the manuscript as presented has several critical gaps. The most significant concern is that the key figures and supplementary materials, which contain the actual data supporting the claims, are not available for assessment. Additionally, the analysis relies heavily on computational predictions without experimental validation, and the authors' own data show that substitution preferences are largely similar across region classes, which somewhat undermines the specificity of the phase-separation link. The statistical approach, while described, cannot be fully evaluated without the figures. The manuscript is well-written and logically structured, but the evidence base is incomplete for a definitive assessment.
- **Who would be interested in the results, and why** Researchers in the fields of protein biophysics, intrinsically disordered proteins, phase separation, human genetics, and clinical genomics would find these results relevant. The work provides a computational framework for prioritizing missense variants in disordered regions, which is a known gap in variant interpretation. Clinicians and geneticists interested in variant classification, particularly for diseases like cancer, neurodevelopmental disorders, and neurodegeneration, would also be interested in the potential predictive value of the approach.
- **Major strengths** The manuscript addresses a significant and understudied problem: the functional interpretation of missense mutations in IDRs. The use of a previously validated algorithm (ParSe) provides a consistent computational framework. The study design includes multiple control analyses, such as testing for bias from research intensity and computational predictor bias, which strengthens the internal validity of the claims. The finding that SLiMs in PS IDRs show exceptionally high pathogenicity is a novel and potentially impactful observation. The authors also provide a clear and logical narrative connecting their findings to the broader literature on phase separation and disease.
- **Major Concerns** The major concerns are detailed below. The most critical is the lack of access to the primary data figures and tables, which prevents verification of the statistical claims. Beyond that, the reliance on computational prediction without experimental validation, the potential confounding effect of protein length and composition, and the authors' own finding that substitution preferences are similar across regions all raise questions about the specificity of the phase-separation link.
- **Minor Comments** Several minor issues are noted below, including the need for clearer definitions of certain terms, the handling of multiple testing, and the presentation of some statistical details.
- **Technical failings that need to be addressed before the case is established** The primary technical failing is the inaccessibility of the data. Without Figures 1-6 and Tables S1-S3, the core claims cannot be verified. Additionally, the analysis does not appear to control for potential confounding variables such as protein length, amino acid composition, or gene expression levels, which could influence mutation rates. The predictive model's performance is only assessed on the training set, with no independent validation cohort.
- **Assessment against Nature-style criteria** **Originality:** The question of whether phase-separating IDRs are enriched for pathogenic mutations is not entirely new, as the authors acknowledge prior work linking phase separation to cancer and autism. However, the systematic, proteome-wide analysis using a specific predictor and the focus on SLiMs within PS IDRs provides a degree of novelty. **Scientific importance:** If the findings are robust, they could have significant implications for variant interpretation in clinical genetics and for understanding the role of phase separation in disease. The potential to predict pathogenicity of variants in a previously understudied class of protein regions is important. **Interdisciplinary readership:** The topic bridges biophysics, molecular biology, and clinical genetics, and would likely appeal to a broad readership. **Technical soundness:** The technical soundness cannot be fully assessed due to missing data. The described methods are reasonable, but the lack of control for confounders and the absence of independent validation are concerns. **Readability for nonspecialists:** The manuscript is generally well-written and accessible, with clear explanations of the concepts. The use of figures would likely aid comprehension, but they are not available for review.
- **Recommendation posture** Currently not established from the provided evidence. The central claims are plausible and potentially important, but the lack of access to the primary data, combined with the concerns about confounding variables and the lack of experimental validation, means that the case is not yet made. A revised manuscript with the data available for review and with additional analyses addressing the confounders would be needed to support the claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence accessibility
- **Claim pointer** The manuscript claims a three-fold elevation of pathogenic mutation rate in predicted PS IDRs relative to non-PS IDRs, and a 5.6-fold odds ratio for pathogenicity of SLiM mutations in PS IDRs.
- **Evidence pointer** Figures 1B, 2B, Tables S1 and S2, location not provided
- **Concern** The primary data supporting the central claims are not available for review. Figures 1-6 and all supplementary figures and tables are referenced but not included in the provided material. Without these, it is impossible to verify the statistical significance, effect sizes, or the validity of the comparisons made. The authors state that normalized mutation rates were calculated with standard errors, but the actual values and the statistical tests used to compare rates across regions are not visible.
- **Why it matters** The entire argument rests on the quantitative comparisons shown in these figures and tables. A reviewer cannot assess whether the claimed three-fold enrichment is real, whether the confidence intervals overlap, or whether the odds ratios are calculated correctly. This is a fundamental barrier to evaluation.
- **Resolution test** Provide the full set of figures and tables with clear axis labels, error bars, and statistical annotations. Include the raw counts of mutations and residues for each region class and each dataset, and the results of the statistical tests used to compare rates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Confounding variables
- **Claim pointer** The manuscript claims that the elevated pathogenic mutation rate in PS IDRs is linked to phase separation behavior, and that this is not due to bias from the computational predictor or research intensity.
- **Evidence pointer** Results section "Mutations in IDRs link pathogenicity and phase separation", location not provided
- **Concern** The analysis does not appear to control for potential confounding variables that could explain the elevated mutation rate in PS IDRs. The authors note that PS proteins are longer and have higher ID content, but they do not explicitly control for protein length or overall amino acid composition in their mutation rate calculations. Longer proteins have more opportunities for mutations, and IDRs are known to have different amino acid compositions than folded regions. The authors mention a correlation analysis (r = 0.17) between the ratio of pathogenic mutation rates and fold enrichment for PS, but this is a weak correlation and does not rule out confounding. Furthermore, the analysis of substitution preferences shows that the same types of mutations are pathogenic across all regions, suggesting that the effect may not be specific to phase separation.
- **Why it matters** If the elevated mutation rate is simply a consequence of protein length or composition, rather than a specific property of phase-separating regions, then the central claim of the paper is weakened. The authors need to demonstrate that the effect is specific to PS IDRs and not just a general property of long, disordered proteins.
- **Resolution test** Perform a multivariable analysis that includes protein length, ID content, and amino acid composition as covariates. Alternatively, match PS and non-PS IDRs for length and composition and compare mutation rates. Show that the enrichment of pathogenic mutations in PS IDRs persists after controlling for these factors.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** External validation
- **Claim pointer** The manuscript claims that substitution frequency data can predict pathogenicity of missense variants, with a 72% combined true positive and true negative rate for PS IDRs.
- **Evidence pointer** Results section "Sequence dependence to pathogenicity does not depend on region identity" and Figure 6, location not provided
- **Concern** The predictive model is assessed only on the training set (the humsavar index). The authors do not validate the model on an independent dataset, such as the natural variants index, which is used only for a qualitative comparison. The authors acknowledge a high error rate (36%) and state that clinical significance depends on additional input variables, but the lack of independent validation is a significant limitation. The claim that the model can predict pathogenicity is therefore not well supported.
- **Why it matters** A model that performs well on the training set but is not validated on independent data may be overfitted and may not generalize. The authors' own acknowledgment of a high error rate suggests that the model is not yet clinically useful. Independent validation is essential to establish the utility of the approach.
- **Resolution test** Apply the substitution frequency model to the natural variants index and report the true positive and true negative rates for this independent dataset. If the performance is significantly lower, this should be discussed as a limitation.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Experimental validation
- **Claim pointer** The manuscript claims that mutations in PS IDRs are pathogenic because they disrupt phase separation, and that the agreement between amino acid types known to facilitate phase separation and pathogenicity reflects adverse effects on condensate function.
- **Evidence pointer** Discussion section, location not provided
- **Concern** The entire analysis is computational. There is no experimental validation showing that any of the identified pathogenic mutations actually alter phase separation behavior. The authors infer a mechanistic link based on the amino acid types involved, but this is indirect. The literature cited (references 52-54) provides evidence for the role of arginine and aromatics in phase separation, but the authors do not test any specific mutations from their dataset.
- **Why it matters** The title of the manuscript claims a link between pathogenicity and phase separation. Without experimental evidence that specific mutations in PS IDRs alter phase separation, the claim remains speculative. The authors need to provide at least some experimental validation to support the mechanistic interpretation.
- **Resolution test** Select a few pathogenic mutations in PS IDRs from the dataset and test their effect on phase separation in vitro or in cells. Show that these mutations alter condensate formation or properties compared to wild-type.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of definitions
- **Affected element** Definition of "PS IDR" and "non-PS IDR"
- **Evidence pointer** Methods section "Sequence-calculated Phase Separation Potential", location not provided
- **Issue** The manuscript uses a cutoff of PS potential of 100 to define PS proteins, but it is not clear how this cutoff was chosen beyond a reference to Figure S2. It is also not clear whether the classification of individual IDRs within a protein is based on the same cutoff, or whether a protein-level classification is used for all downstream analyses.
- **Required correction** Clarify the exact criteria for classifying a region as a PS IDR versus a non-PS IDR. State whether the cutoff of 100 was applied to individual windows, to entire IDRs, or to proteins, and how this choice affects the interpretation of the results.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Multiple testing
- **Evidence pointer** Results section "Disease-associated proteins are enriched for phase separation" and Figure 3, location not provided
- **Issue** The authors report that 32 of 100 disease types have AUC values more than 2 standard deviations above the mean random AUC. Given that 100 disease types are tested, some number of false positives would be expected by chance. The authors do not appear to correct for multiple testing.
- **Required correction** Report whether any multiple testing correction was applied, such as a Benjamini-Hochberg correction, and discuss how this affects the interpretation of the significant disease types.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Source data
- **Evidence pointer** Data Availability section, location not provided
- **Issue** The data availability statement only mentions source code for the ParSe algorithm. It does not mention the availability of the datasets used in the analysis, such as the lists of disease-associated proteins, the mutation annotations, or the computed PS potentials for all proteins.
- **Required correction** Provide a clear statement on the availability of the datasets used in the analysis, or explain why they cannot be made available.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation of odds ratios
- **Affected element** Odds ratio interpretation
- **Evidence pointer** Results section "Mutations in SLiMs within PS IDRs exhibit exceptionally high pathogenicity" and Figure 2B, location not provided
- **Issue** The authors report an odds ratio of 5.6 for pathogenic versus benign mutations in SLiMs in PS IDRs. However, the absolute number of such mutations is small (44 of 32,665). The authors should discuss the clinical relevance of this finding given the small absolute numbers.
- **Required correction** Add a sentence discussing the absolute number of mutations and the practical implications of the high odds ratio in the context of the small sample size.

## Risk / unsupported claims
- The claim that pathogenic mutations in PS IDRs are specifically linked to phase separation, rather than to other properties of these regions, is not fully supported due to the lack of control for confounding variables such as protein length and composition.
- The claim that the model can predict pathogenicity of missense mutations is not supported by independent validation.
- The mechanistic claim that mutations in PS IDRs cause disease by disrupting phase separation is not supported by experimental evidence.
- The claim that 32 disease types show significant enrichment for phase separation is potentially affected by multiple testing, which is not addressed.
- The overall quantitative results, including the three-fold enrichment and the odds ratios, cannot be verified without access to the figures and tables.