## Review setup
- **Input scope** Full manuscript text (main text, methods, and references to SI Appendix)
- **Assessment boundary** Scientific validity, methodological soundness, claims versus evidence, and presentation quality of the provided manuscript
- **Shared manuscript claim summary** The authors present two open-source classifiers, amyloid-predict and LLPS-predict, that use ESM2-3B protein language model embeddings and logistic regression to predict amyloid aggregation and liquid-liquid phase separation propensities from sequence. They report high accuracy on benchmark datasets, sensitivity to sequence patterning beyond composition, and apply the models to annotate the human intrinsically disordered proteome, revealing category-level enrichments and mutation effects.
- **Visible evidence base** Main text figures (Fig. 1A-F, Fig. 2A-B, Fig. 3C, Fig. 4), methods section, and references to SI Appendix tables and figures
- **Missing materials affecting confidence** SI Appendix (all tables and figures referenced), benchmark dataset details, CD-CODE and Tesei et al. dataset specifics, full GO analysis results, SNP dataset composition, and code repository contents

## Reviewer

### Overall assessment
This manuscript presents a useful and timely contribution to the field of protein phase separation prediction. The core idea of leveraging ESM embeddings for fast, accurate classification of both amyloid and LLPS propensity is sound and the reported performance is competitive. The application to the human IDRome and the demonstration of category-level enrichments are valuable. However, the manuscript has several weaknesses that need to be addressed. The LLPS model's AUC of 0.79 is modest, and the claim that it captures "transferable sequence signals" is only partially supported by the leave-one-GO-out analysis. The per-residue scoring method, while reasonable, is not benchmarked against alternative approaches. The SNP analysis is interesting but the clinical relevance is not fully developed. The manuscript would benefit from clearer presentation of the limitations of the approach, particularly regarding the interpretability of the models and the potential biases in the training data.

### Who would be interested in the results, and why
Computational biologists and bioinformaticians working on protein sequence-function prediction, particularly those interested in phase separation and aggregation. Researchers studying neurodegenerative diseases, amyloidosis, and biomolecular condensates would find the proteome-wide annotations useful for hypothesis generation. Protein engineers and synthetic biologists designing self-assembling materials or condensate-forming proteins would benefit from the fast, open-source tools. The manuscript is also relevant to method developers in the protein language model application space.

### Major strengths
1. The use of ESM2-3B embeddings with simple logistic regression is elegant and demonstrates that complex protein language models can be effectively leveraged for phase transition prediction without heavy fine-tuning.
2. The dual prediction framework (amyloid and LLPS) in a single manuscript provides a unified view of protein phase transitions, which is conceptually appealing.
3. The throughput advantage over existing tools is clearly demonstrated and practically important.
4. The application to the human IDRome with per-residue scoring is a useful resource for the community.
5. The sensitivity analyses (permutation tests, composition controls) strengthen the claim that the models capture sequence patterning beyond composition.
6. The open-source availability and permissive licensing are commendable.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Our LLPS model, trained specifically on intrinsically disordered regions (IDRs), shows strong performance in identifying condensate-driving segments across the disordered human proteome."
- **Evidence pointer** Fig. 1F, SI Appendix Fig. S8
- **Concern** The LLPS-predict model achieves a ROC AUC of 0.79, which is described as "strong performance." However, this is a modest AUC, and the positive class is defined by only 180 IDRs from 118 CD-CODE LLPS drivers. The manuscript does not report precision-recall curves or other metrics that would be more informative for imbalanced classification problems. The claim of "strong performance" is not fully supported by the evidence presented.
- **Why it matters** The utility of LLPS-predict for identifying novel LLPS drivers depends on its precision at the operating threshold used for the IDRome annotation. A modest AUC with a small positive class could lead to many false positives in the proteome-wide analysis.
- **Resolution test** Report precision-recall curves, F1 scores, and calibration plots. Provide the distribution of scores for positive and negative classes. Discuss the practical operating point chosen for the IDRome annotation and the expected false discovery rate at that threshold.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "To test this, we performed leave-one-GO-molecular-function-out evaluation, withholding all IDRs annotated with each of 39 well-represented GO molecular function terms during training and evaluating on the held-out term. Performance remains substantial (median held-out ROC-AUC = 0.73; 'nucleic acid binding' held out: ROC-AUC = 0.73), supporting that LLPS-predict captures transferable sequence signals beyond any single dominant functional category."
- **Evidence pointer** SI Appendix Table S4
- **Concern** The leave-one-GO-out analysis is a reasonable approach, but the interpretation is limited. A median held-out AUC of 0.73 is lower than the full model's 0.79, and the range of AUCs across the 39 GO terms is not reported. It is possible that performance drops substantially for some GO categories, which would indicate that the model is learning category-specific features rather than general LLPS-driving properties. The manuscript does not report the variance or the worst-performing categories.
- **Why it matters** The claim that the model captures "transferable sequence signals" is central to its generalizability. If performance is highly variable across GO categories, the model may not be suitable for predicting LLPS propensity in under-represented protein families.
- **Resolution test** Report the full distribution of held-out AUCs, identify the best and worst performing GO categories, and discuss whether the model is learning general LLPS features or category-specific patterns. Consider also performing a leave-one-protein-family-out analysis.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "We find that our 6aa amyloid classifier exceeds the classification performance with this test set of several other amyloid predictors from the literature: PASTA, CANYA, TANGO, WALTZ."
- **Evidence pointer** Fig. 1D
- **Concern** The comparison to existing amyloid predictors is made only on the 6aa dataset. The manuscript does not report comparisons on the 10aa and 15aa datasets, where the performance of other tools may be different. Additionally, the comparison to PASTA is made against the web server, which includes network and server overhead, making the throughput comparison potentially misleading.
- **Why it matters** A fair and comprehensive comparison is essential to establish the advantage of the proposed method. The current comparison is limited and may not reflect the true relative performance across different peptide lengths and datasets.
- **Resolution test** Provide comparisons on all three datasets (6aa, 10aa, 15aa) against all baseline methods. For throughput, compare against a local installation of PASTA or clearly separate the model inference time from the web server overhead.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** "Applying them to all intrinsically disordered regions in the human proteome reveals protein categories enriched for amyloid or LLPS potential, including receptors, nucleic-acid-binding proteins, and prions."
- **Evidence pointer** Fig. 3C, SI Appendix Tables S5 and S6
- **Concern** The GO enrichment analysis is descriptive and the biological interpretation is somewhat speculative. The manuscript does not validate any of the predicted category-level enrichments experimentally or against independent datasets. The discussion of why certain categories are enriched (e.g., GPCRs) is plausible but not rigorously supported.
- **Why it matters** The proteome-wide annotation is a key contribution, but its value depends on the reliability of the predictions and the biological insights derived from them. Without validation, the enrichments may reflect biases in the training data or the model rather than true biological properties.
- **Resolution test** Validate a subset of the predicted high-propensity proteins from enriched categories using independent experimental data or orthogonal prediction methods. Discuss potential biases in the training data that could lead to spurious enrichments.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "Pathogenic SNPs are enriched for larger predicted changes in aggregation propensity compared with benign variants."
- **Evidence pointer** SI Appendix Figs. S19 and S20
- **Concern** The SNP analysis is interesting but the methodology is not fully described. The manuscript does not specify how many SNPs were analyzed, how the pathogenic/benign classification was determined, or whether the analysis was corrected for potential confounders beyond those mentioned. The effect sizes (odds ratios 2-4) are moderate, and the clinical relevance is not discussed.
- **Why it matters** The SNP analysis has potential translational relevance, but the current presentation is insufficient to assess its robustness and significance.
- **Resolution test** Provide a detailed description of the SNP dataset, including the number of variants, the source of pathogenicity annotations, and the distribution of Δaggregation values. Discuss the potential clinical implications of the findings and any limitations of the analysis.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Significance section
- **Evidence pointer** Main text, Significance
- **Issue** The Significance section is well-written but could be more accessible. The term "phase transitions" is used without explaining that it encompasses both aggregation and LLPS, which are distinct phenomena.
- **Required correction** Briefly define both amyloid aggregation and LLPS in the Significance section to orient readers from different backgrounds.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, Model Training
- **Evidence pointer** Methods section
- **Issue** The description of the training procedure for the combined 6/10/15aa model is unclear. The manuscript states that "class and dataset weights were balanced" but does not specify how this was implemented.
- **Required correction** Provide a more detailed description of the weighting scheme and the cross-validation procedure for the combined model.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, amyloid-Predict and LLPS-Predict
- **Evidence pointer** Fig. 1D
- **Concern** The ROC AUC for the 6aa model is reported as 0.91, but the confidence intervals are not shown in the figure. The manuscript mentions error bars for the LLPS model but not for the amyloid model.
- **Required correction** Add confidence intervals or error bars to all performance metrics in Fig. 1.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, amyloid-Predict and LLPS-Predict
- **Evidence pointer** SI Appendix Table S1
- **Issue** The throughput comparison is presented as a single number (sequences per second), but the dependence on sequence length and batch size is not discussed.
- **Required correction** Provide a more detailed analysis of throughput as a function of sequence length and batch size.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Discussion, IDRome Analysis
- **Evidence pointer** Discussion section
- **Issue** The discussion of GPCRs and membrane-associated proteins is somewhat speculative and could be more clearly framed as hypotheses rather than conclusions.
- **Required correction** Use more cautious language when discussing the biological implications of the category-level enrichments.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, SNP Analysis
- **Evidence pointer** Methods section
- **Issue** The description of the SNP analysis is brief and does not specify how the "local windows spanning ±14 residues" were defined relative to the SNP position.
- **Required correction** Clarify the window definition and provide a schematic or example.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, Visualizing Protein LLPS and Aggregation Scores
- **Evidence pointer** Fig. 4
- **Issue** The four classes of IDPRs described in the text are not clearly delineated in the figure. The axes and color coding are not described in the figure legend.
- **Required correction** Improve the figure legend to explain the axes, color coding, and how the four classes are distinguished.

### Technical failings that need to be addressed before the case is established
1. The LLPS model's modest AUC (0.79) and small positive training set (180 IDRs) require more rigorous evaluation, including precision-recall analysis and assessment of calibration.
2. The leave-one-GO-out analysis needs to report the full distribution of results, not just the median, to support the claim of transferability.
3. The comparison to existing tools is incomplete, particularly for the 10aa and 15aa datasets.
4. The SNP analysis methodology is under-specified and the results are not contextualized with respect to known disease mechanisms.

### Assessment against Nature-style criteria
- **Originality** The use of ESM embeddings for dual amyloid/LLPS prediction is a novel combination, though the individual components (pLM embeddings, logistic regression) are established. The unified framework is a conceptual contribution.
- **Scientific importance** The tools address a real need in the field, and the proteome-wide annotations could be a useful community resource. However, the biological insights derived from the analysis are largely confirmatory of known trends rather than surprising.
- **Interdisciplinary readership** The manuscript bridges computational biology, biophysics, and cell biology, and the tools could be used by researchers in all three communities. The writing is generally accessible.
- **Technical soundness** The core methodology is sound, but several technical aspects need strengthening, as detailed in the Major Concerns. The lack of precision-recall analysis and incomplete benchmarking are notable gaps.
- **Readability for nonspecialists** The manuscript is generally well-written, but the Significance section could be more accessible, and some methodological details are presented too briefly.

### Recommendation posture
Supportive if technical concerns are resolved. The core idea is promising and the tools are likely to be useful, but the current evidence does not fully support all the claims made, particularly regarding the LLPS model's performance and the transferability of its features. The manuscript would be strengthened by more rigorous evaluation, more comprehensive benchmarking, and clearer presentation of limitations.

## Risk / unsupported claims
1. The claim that LLPS-predict shows "strong performance" is not fully supported by the reported AUC of 0.79, especially given the small positive training set.
2. The claim that the models capture "sequence patterning beyond amino acid composition" is supported by the permutation analyses, but the extent to which this translates to improved biological predictions is not demonstrated.
3. The biological interpretation of the GO enrichments (e.g., GPCRs, membrane-associated proteins) is speculative and not validated.
4. The SNP analysis claims that pathogenic variants are enriched for larger predicted changes, but the clinical relevance and the robustness of the finding are not fully established.
5. The statement that the models "match or exceed the accuracy of physics-based tools" is only demonstrated for the 6aa dataset and may not generalize to other datasets or peptide lengths.
6. The claim that the tools enable "rapid hypothesis generation" is reasonable but not directly demonstrated with any experimental validation.