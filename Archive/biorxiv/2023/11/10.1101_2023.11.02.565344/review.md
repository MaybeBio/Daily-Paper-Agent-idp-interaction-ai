## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and appendices as provided.
- **Assessment boundary** Scientific validity, methodological soundness, claims versus evidence, and presentation quality based solely on the supplied material.
- **Shared manuscript claim summary** The authors propose GPSite, a multi-task deep learning framework that predicts protein binding sites for ten ligand types (DNA, RNA, peptide, protein, ATP, HEM, and four metal ions) using sequence embeddings from ProtTrans and predicted structures from ESMFold. They claim substantial improvements over state-of-the-art sequence- and structure-based methods across benchmark datasets, robustness to low-quality predicted structures, and scalability to genome-scale annotation of over 568,000 Swiss-Prot sequences. They further claim that their annotations can reveal associations with molecular functions, biological processes, and genetic variants.
- **Visible evidence base** Abstract, Introduction, Results sections (including figures referenced but not shown), Discussion, Methods, and Appendix notes and tables referenced but not fully visible. Figures and tables are cited but their contents are not provided in the supplied material.
- **Missing materials affecting confidence** All figures (Figures 1-5) and appendix figures are referenced but not included. Appendix tables (Appendix 2-tables 1-10) are cited but not shown. Detailed numerical results for comparisons, ablation studies, and statistical tests are not visible. The exact architecture hyperparameters and training details are partially described but not fully reproducible from the text alone.

## Reviewer
- **Overall assessment** The manuscript presents a timely and potentially impactful approach to protein binding site prediction, leveraging recent advances in protein language models and predicted structures. The multi-task framework and geometric feature engineering are thoughtful and well-motivated. However, the core claims of substantial improvement over existing methods and genome-scale utility cannot be fully verified from the supplied material, as all quantitative results are contained in figures and tables that were not provided. The methodological description is generally clear, but several technical details require clarification to assess reproducibility and generalizability.
- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein function annotation, binding site prediction, and genome-scale analysis would be the primary audience. Researchers in structural biology and drug discovery may also find the approach useful for prioritizing residues for experimental validation. The genome-scale annotation database could serve as a community resource for exploring protein-ligand interactions across diverse organisms.
- **Major strengths** The use of predicted structures from ESMFold rather than experimental structures or MSA is a practical and forward-looking choice that aligns with the goal of genome-scale applicability. The multi-task learning framework is a sensible strategy to leverage shared binding characteristics across ligand types, potentially improving data efficiency. The geometric featurizer that captures both intra- and inter-residue geometry is more comprehensive than many existing approaches. The demonstration of robustness to low-quality predicted structures is an important practical consideration. The genome-scale annotation effort and the analysis of genetic variant associations add translational value.
- **Major Concerns** The most significant concern is that all performance comparisons and ablation results are presented only in figures and tables that were not included in the supplied material, making the central claims unverifiable. Additionally, the comparison methodology against existing methods is not fully described, particularly regarding whether the same training and test splits were used and whether hyperparameters were optimized fairly for all methods. The claim of robustness to low-quality structures is based on a single case study and aggregate statistics that are not visible. The genome-scale analysis relies on predicted structures and automated annotations, and the potential error propagation from these sources is not thoroughly discussed.
- **Minor Comments** Several methodological details require clarification, including the exact definition of the radius graph, the handling of proteins with multiple chains, and the threshold selection procedure. The discussion of limitations is relatively brief and could be expanded to address potential biases in the benchmark datasets and the interpretability of the learned representations.
- **Technical failings that need to be addressed before the case is established** The absence of visible quantitative results is a critical failing that prevents assessment of the core claims. The lack of detailed comparison protocols and statistical significance testing further weakens the evidence base. The reproducibility of the method is compromised by incomplete descriptions of some architectural components and training procedures.
- **Assessment against Nature-style criteria** Originality: The combination of language model embeddings, predicted structures, and multi-task learning for binding site prediction is a novel integration of existing ideas, though individual components have been explored separately. Scientific importance: The potential for genome-scale binding site annotation is significant, and the association with genetic variants adds biological relevance. Interdisciplinary readership: The work bridges computational biology, structural biology, and genomics, and is likely to attract interest across these fields. Technical soundness: The methodological framework is plausible, but the lack of visible results prevents a full assessment of technical rigor. Readability for nonspecialists: The manuscript is generally well-written and accessible, though some technical jargon in the methods section may be challenging for a broader audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The approach is promising and the manuscript is well-structured, but the central claims cannot be evaluated without the missing figures and tables. The authors should provide the full set of results and clarify the comparison methodology before the case is established.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The claim that GPSite substantially surpasses state-of-the-art sequence-based and structure-based approaches on various benchmark datasets.
- **Evidence pointer** Figure 2, Appendix 2-tables 2 and 3, location not provided
- **Concern** All quantitative results supporting the central performance claim are contained in figures and tables that were not included in the supplied material. Without these data, it is impossible to verify the magnitude of improvement, the statistical significance, or the consistency of performance across ligand types and benchmark datasets.
- **Why it matters** The primary contribution of the manuscript is the claimed superiority of GPSite over existing methods. If this claim is not substantiated with visible, reproducible results, the scientific case for the method is not established.
- **Resolution test** Provide the full figures and tables with numerical values, including error bars or confidence intervals, and describe the statistical tests used to compare methods.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological rigor
- **Claim pointer** The claim that GPSite is robust to low-quality predicted structures and outperforms other structure-based methods under such conditions.
- **Evidence pointer** Figure 3, Appendix 1-note 3, location not provided
- **Concern** The robustness analysis is based on stratifying proteins by TM-score and comparing performance on subsets with TM-score ≤ 0.7. However, the number of proteins in these subsets, the distribution of TM-scores, and the specific performance metrics are not visible. The single case study of ERB1 is illustrative but not sufficient to establish general robustness.
- **Why it matters** Robustness to imperfect predicted structures is a key practical advantage claimed by the authors, especially for genome-scale applications where experimental structures are unavailable. Without quantitative evidence, this claim remains anecdotal.
- **Resolution test** Provide the full results of the robustness analysis, including the number of proteins in each TM-score bin, the performance metrics for GPSite and comparison methods, and the statistical significance of differences.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Comparison fairness
- **Claim pointer** The claim that GPSite outperforms 8 sequence-based and 15 structure-based predictors.
- **Evidence pointer** Methods section, Appendix 1-note 1, location not provided
- **Concern** The comparison protocol is not fully described. It is unclear whether all methods were trained and tested on the same data splits, whether hyperparameters were optimized for each method on the validation sets, and whether the same evaluation metrics and thresholds were used. Some comparison methods may have been used with default parameters rather than optimized ones, which could bias results in favor of GPSite.
- **Why it matters** Fair and consistent comparison is essential for establishing that the observed improvements are due to the method itself rather than to differences in training protocols or evaluation procedures.
- **Resolution test** Describe the exact training and evaluation protocol for each comparison method, including hyperparameter tuning, data splits, and threshold selection. Provide results with and without hyperparameter optimization for all methods.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The claim that GPSite enables rapid genome-scale binding residue annotations for over 568,000 sequences, providing opportunities to uncover unexplored associations with molecular functions, biological processes, and genetic variants.
- **Evidence pointer** Figure 5, Methods section, location not provided
- **Concern** The genome-scale analysis is presented as a demonstration of utility, but the validation of the predicted annotations is limited. The authors show that predicted binding scores correlate with existing functional annotations and that pathogenic variants are enriched in predicted binding sites, but the false positive rate and the biological significance of the novel predictions are not assessed. The analysis relies on predicted structures with pTM > 0.7, and the impact of excluding lower-confidence structures is not discussed.
- **Why it matters** The genome-scale annotation is a major selling point of the manuscript. If the predictions are not sufficiently accurate or if the analysis is biased by the quality of predicted structures, the conclusions drawn from this analysis may be unreliable.
- **Resolution test** Provide additional validation of the genome-scale predictions, such as comparison with experimental binding data for a subset of proteins, analysis of the false positive rate, and discussion of the limitations of using predicted structures.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods, radius graph construction
- **Evidence pointer** Methods section, location not provided
- **Issue** The radius graph is defined with a cutoff of 15 Å between Cα atoms, but the rationale for this specific cutoff is not provided. It is also unclear whether the graph is constructed based on the predicted structure or the native structure, and how the graph connectivity affects the model's sensitivity to structural errors.
- **Required correction** Justify the choice of the radius cutoff and discuss its impact on model performance and robustness.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, training details
- **Evidence pointer** Methods section, location not provided
- **Issue** The training procedure is described in general terms, but specific details such as the learning rate schedule, batch size, number of training epochs, and data augmentation strategies are not fully specified. The random seed for data splitting and model initialization is not mentioned.
- **Required correction** Provide complete training details to ensure reproducibility, including all hyperparameters and the random seed.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results, ablation studies
- **Evidence pointer** Figure 4, Appendix 2-table 7, location not provided
- **Issue** The ablation studies are described in the text, but the specific contributions of each component (e.g., geometric featurizer, multi-task learning) are not quantified in the visible text. It is unclear whether the improvements are statistically significant and whether they are consistent across ligand types.
- **Required correction** Present the ablation results with numerical values and statistical tests to support the claims about the importance of each component.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Scope
- **Affected element** Discussion, limitations
- **Evidence pointer** Discussion section, location not provided
- **Issue** The discussion of limitations is brief and does not address potential biases in the benchmark datasets, such as the overrepresentation of certain protein families or the redundancy between training and test sets. The interpretability of the learned representations and the potential for overfitting are not discussed.
- **Required correction** Expand the discussion of limitations to include dataset biases, model interpretability, and potential sources of overfitting.

## Risk / unsupported claims
- The claim of substantial improvement over state-of-the-art methods is unsupported in the supplied material, as all quantitative results are in missing figures and tables.
- The claim of robustness to low-quality predicted structures is only partially supported by a single case study and requires the full robustness analysis to be verified.
- The claim that GPSite annotations can uncover unexplored associations with genetic variants is suggestive but not fully validated, as the analysis relies on predicted structures and automated annotations without experimental confirmation.
- The claim that GPSite is computationally efficient is mentioned but not quantified in the visible text, and the comparison of computational cost with other methods is not provided.
- The generalizability of GPSite to proteins with very low sequence similarity to the training set is not assessed, and the potential impact of domain shifts in the predicted structures is not discussed.