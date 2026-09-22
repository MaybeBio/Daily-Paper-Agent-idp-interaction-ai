## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, methods, supplementary figure references, and back matter.
- **Assessment boundary** Scientific claims, methodological soundness, statistical rigor, and interpretability of results as presented. No assessment of code functionality or reproducibility beyond what is described.
- **Shared manuscript claim summary** The authors investigate how the protein language model ESM-2 represents intrinsically disordered proteins (IDPs). They report that ESM-2 attends less to disordered regions, yet retains biologically meaningful information, including heightened attention to disease-relevant residues, correlation with contact maps, and predictive power for radius of gyration.
- **Visible evidence base** Main text figures 1–5 (referenced but not provided), tables 1–4 (referenced but not provided), supplementary figures 6–8 (referenced but not provided), and methods sections 6.1–6.10.
- **Missing materials affecting confidence** All figures, tables, and supplementary materials are absent from the provided text. Statistical details (e.g., exact p-values, confidence intervals, sample sizes per analysis) are partially reported in text but cannot be verified. Code repository is referenced but not reviewed.

## Reviewer

- **Overall assessment** This manuscript addresses a timely and underexplored question: how do protein language models behave on intrinsically disordered proteins, which are abundant and disease-relevant yet often excluded from structural bioinformatics analyses. The authors present a systematic exploration across embeddings, attention, and downstream prediction tasks. The central finding that ESM-2 under-attends to disordered regions while still encoding useful biological signal is plausible and potentially valuable. However, the evidence as presented in the text alone is insufficient to fully evaluate the strength of the claims. Several analyses rely on indirect proxies (e.g., MD-derived contact maps as ground truth), and the statistical framework for some comparisons is not fully described. The electrostatics ablation analysis is the most mechanistically interesting but also the most methodologically complex, and the current description leaves important ambiguities. Overall, the work is promising but requires substantial clarification and additional validation before the claims can be considered established.

- **Who would be interested in the results, and why** Researchers in protein language model interpretability, computational biology of disordered proteins, and machine learning for biophysics would find this work relevant. The finding that PLMs encode disorder-relevant information despite a training bias toward structured regions has implications for downstream task design, such as variant effect prediction or IDP function annotation. The electrostatics ablation analysis may interest those studying mechanistic interpretability of transformers beyond protein domains. Clinically oriented computational biologists studying disease variants in disordered regions may also find the disease-relevance attention results useful.

- **Major strengths** The manuscript addresses a clear gap in the literature, as prior interpretability studies have largely excluded IDPs. The multi-pronged approach, spanning embeddings, attention, and predictive modeling, provides a broad view of what the model encodes. The use of matched PDB and DisProt datasets is a reasonable design choice. The comparison to an existing state-of-the-art model (STARLING) for Rg prediction is appropriate. The authors acknowledge several limitations of their methods, including assumptions in attention rollout and the use of MD-derived contact maps as approximations.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor and confounding control
- **Claim pointer** The authors claim that "disease-relevant residues tended to fall in a higher attention percentile" and that this effect persists across disorder levels.
- **Evidence pointer** Section 2.5, Figure 3 (not provided)
- **Concern** The analysis comparing attention to disease-relevant versus non-disease-relevant residues does not appear to control for amino acid identity, sequence position, or local sequence context. Disease-associated variants are known to be enriched in certain amino acids (e.g., Arg, Gly) and in specific functional domains. Given that the authors themselves show amino acid identity affects attention allocation (Section 2.4), the disease-relevance effect could be confounded by amino acid composition. The regression framework described in Section 6.7 includes conservation as a covariate, but it is unclear whether amino acid identity or position-specific effects are included.
- **Why it matters** If the attention signal attributed to disease relevance is actually driven by amino acid composition or other confounders, the central claim that the model encodes pathogenicity information would be substantially weakened.
- **Resolution test** Provide a version of the analysis that includes amino acid identity as a fixed effect or stratifies by amino acid. Report the disease-relevance coefficient before and after such adjustment. Alternatively, perform a permutation test where disease labels are randomly assigned to residues within the same amino acid class.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Ground truth validity
- **Claim pointer** The authors claim that ESM-2 embeddings correlate with "individual dynamic contact maps" derived from coarse-grained MD simulations, and that this indicates the model captures structural information about IDPs.
- **Evidence pointer** Section 2.6, Figure 4 (not provided)
- **Concern** The use of CALVADOS 2 coarse-grained MD simulations as ground truth for IDP contacts is a strong assumption. While CALVADOS 2 is parameterized for IDPs, coarse-grained models are known to have limited accuracy for specific contact predictions, especially for transient interactions. The authors report a median Spearman correlation of 0.28, which is modest. The permutation test shows significance, but the effect size is small. The claim that this represents "structural information" may be overstated given the proxy nature of the ground truth and the modest correlation.
- **Why it matters** If the correlation is driven by trivial sequence features (e.g., chain length, charge patterning) rather than specific structural contacts, the interpretation that ESM-2 encodes IDP structure would be misleading.
- **Resolution test** Compare the Jacobian-based contact predictions against a simpler baseline, such as a sequence-based predictor using amino acid composition or a random contact model matched for sequence length. Report whether the Jacobian method outperforms such baselines. Additionally, validate on a subset of IDPs with experimental structural data (e.g., NMR or SAXS-derived ensembles) if available.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological clarity and causal attribution
- **Claim pointer** The authors claim that ablating attention heads that attend most to charged residues reduces Rg prediction performance, and that this indicates these heads encode electrostatic information.
- **Evidence pointer** Section 2.8, Figure 5B, Tables 3 and 4 (not provided)
- **Concern** The ablation analysis is described in limited detail. The authors state that heads were ranked by average attention to charged residues and progressively ablated. However, it is unclear how the ranking was computed across the 33 layers and 20 heads (660 total heads), whether the ranking was stable across proteins, and how the random control was matched. The residualization analysis is a good idea, but the description is dense and the interpretation of the asymmetry between negative and positive charge heads is not fully justified. Specifically, the claim that positive-charge heads encode "composition-independent information" relies on the residualization analysis, but the details of how the residual was computed and how the bootstrap confidence interval was derived are not provided.
- **Why it matters** The electrostatics claim is the most mechanistically specific finding in the paper. If the ablation methodology is not robust or the residualization is not properly described, the claim cannot be evaluated or reproduced.
- **Resolution test** Provide a detailed description of the head ranking procedure, including whether it was based on training or held-out data. Report the stability of the ranking across random seeds or dataset splits. For the residualization, specify the exact regression model used, how the residual was computed, and how the bootstrap was performed. Show the full distribution of performance changes across individual heads, not just cumulative ablations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability and dataset bias
- **Claim pointer** The authors state that their findings apply to "intrinsically disordered proteins" broadly, and they use the human IDRome for Rg prediction.
- **Evidence pointer** Sections 2.1, 2.6, 2.7; Methods 6.1, 6.8
- **Concern** The human IDRome is a specific set of sequences, and the DisProt dataset is curated and may not represent the full diversity of IDPs across organisms or sequence space. The matched PDB dataset is a proxy for "folded" proteins, but PDB entries are biased toward well-behaved, crystallizable proteins. The generalizability of the findings to other IDP families, especially those with low complexity or repetitive sequences, is unclear. Additionally, the Rg prediction model was trained and tested on the same IDRome distribution, so performance on out-of-distribution IDPs is unknown.
- **Why it matters** If the findings are specific to the human IDRome or to the particular sequence distribution in DisProt, the broader claims about PLM behavior on IDPs would be overstated.
- **Resolution test** Validate the Rg prediction model on an independent IDP dataset from a different organism or a different source (e.g., a subset of DisProt not used in training). Report performance stratified by sequence complexity or compositional bias.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** Section 2.2, use of "perplexity"
- **Evidence pointer** Section 2.2, Methods 6.3
- **Issue** The term "perplexity" is used without defining whether it refers to the geometric mean of inverse token probabilities, the average negative log-likelihood, or a normalized variant. The regression reports a coefficient of 6.20 with a specific scale, but the reader cannot interpret this without knowing the exact metric.
- **Required correction** Define perplexity precisely, state the range and distribution of values in the dataset, and report the regression in standardized units (e.g., per standard deviation change in disorder probability) to aid interpretation.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Section 2.1, classification accuracy
- **Evidence pointer** Section 2.1, Methods 6.1
- **Issue** The classification accuracy of 89.9% is reported with a 5-fold cross-validation scheme, but no confidence interval or variability across folds is provided. Given the potential for leakage due to homologous sequences despite CD-HIT clustering, the variance across folds is important.
- **Required correction** Report the mean and standard deviation of accuracy across the five folds, and state the number of sequences in each fold.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of effect sizes
- **Affected element** Section 2.4, Cohen's d values
- **Evidence pointer** Table 1 (not provided)
- **Issue** The text states that "all of the amino acids saw statistically-significant differences" but the effect sizes are mostly small. The biological relevance of small effect sizes in attention allocation is not discussed. Statistical significance with large sample sizes (n = 4,240 proteins) is expected, but the practical importance is unclear.
- **Required correction** Discuss the practical significance of the observed effect sizes. Consider reporting the proportion of variance explained or using a threshold for meaningful effect sizes.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Missing methodological detail
- **Affected element** Section 2.7, Rg prediction
- **Evidence pointer** Section 2.7, Methods 6.9
- **Issue** The MLP architecture is described, but the training details are incomplete. The number of epochs, batch size, learning rate schedule, and the specific early stopping criterion are not fully specified. The text mentions "cosine annealing" and "mixed-precision training" but does not state the peak learning rate or the number of warmup steps.
- **Required correction** Provide the full training configuration, including optimizer hyperparameters, batch size, number of epochs, and the exact early stopping condition.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure accessibility
- **Affected element** All figures
- **Evidence pointer** Figures 1–5, Tables 1–4 (not provided)
- **Issue** The figures and tables are referenced but not included in the provided text. This review cannot assess the visual quality, axis labels, or statistical annotations in the figures.
- **Required correction** Ensure all figures include clear axis labels, units, and statistical annotations. Provide figure captions that are self-contained and explain all panels.

## Risk / unsupported claims
- The claim that ESM-2 "exhibits reduced attention on disordered regions" is supported by the described analysis but cannot be fully verified without Figure 1C and 1D.
- The claim that disease-relevant residues receive heightened attention independent of amino acid composition is not established from the text alone, as the confounding analysis is not described.
- The claim that ESM-2 embeddings "correlate with individual dynamic contact maps" is based on a proxy ground truth (coarse-grained MD) and a modest median correlation; the interpretation as "structural information" may be overstated.
- The claim that ablating positive-charge-attending heads removes "composition-independent information" relies on a residualization analysis that is not fully described and cannot be evaluated.
- The generalizability of the Rg prediction results beyond the human IDRome is not established.
- The statement that "PLMs capture valuable information relevant to IDP biology despite their bias toward structured residues" is a reasonable synthesis of the findings but depends on the strength of the individual analyses, several of which have unresolved methodological concerns.