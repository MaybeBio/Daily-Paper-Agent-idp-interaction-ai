## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, experimental section) without figures, tables, or supplementary materials.
- **Assessment boundary** Scientific claims, methodological soundness, experimental design, and interpretation as presented in the provided text. Visual elements (figures, tables) and supplementary data are referenced but not directly assessable.
- **Shared manuscript claim summary** The authors propose MolDBG, a unified sequence-based framework that jointly performs drug-target affinity prediction, binding-site identification, and affinity-conditioned molecular generation. The central claim is that explicit binding-site supervision improves performance across all three tasks, enables site-specific affinity discrimination, and generalizes to structurally challenging targets such as cryptic pockets and intrinsically disordered proteins.
- **Visible evidence base** Textual descriptions of results, including quantitative metrics (e.g., AUROC 0.9014 on PocketMiner, sample-level success rate 72.62% on UniProtKB-IDP, MSE 0.6933, Pearson 0.9009, CI 0.8850 on affinity prediction), comparisons against named baselines, and methodological details in the Experimental Section.
- **Missing materials affecting confidence** All figures (Figure 1-5), all tables (Tables 1, S1-S10), supplementary sections (S2-S8), and the GitHub repository contents. Without these, statistical significance, effect sizes, baseline configurations, and visual evidence for key claims cannot be independently verified.

## Reviewer
- **Overall assessment** The manuscript presents a technically ambitious and potentially valuable contribution to computational drug discovery. The idea of unifying affinity prediction, binding-site identification, and conditional generation within a single site-aware framework is timely and addresses a real limitation in existing sequence-based methods. The reported results, if reproducible, would represent a meaningful advance. However, the provided text alone is insufficient to fully evaluate the validity of the core claims. Several critical details regarding baseline fairness, statistical rigor, and the interpretation of key results are either missing or under-specified. The generalization claims to cryptic pockets and IDPs, while intriguing, rest on metrics that are not fully contextualized. The manuscript is well-written and the conceptual framing is clear, but the evidence base as presented does not yet fully establish the superiority or broad applicability of the proposed method.
- **Who would be interested in the results, and why** Computational biologists, medicinal chemists, and AI researchers working on drug discovery. The unified framework is directly relevant to those developing deep learning models for virtual screening, de novo design, and binding-site prediction. The emphasis on interpretability and generalization to dynamic proteins would also appeal to structural biologists and researchers studying intrinsically disordered proteins or cryptic allosteric sites.
- **Major Strengths** The conceptual unification of three distinct tasks within a single architecture is a clear strength. The explicit incorporation of binding-site supervision to guide representation learning is a well-motivated design choice. The inclusion of challenging test cases (cryptic pockets, IDPs) demonstrates an ambition beyond standard benchmarks. The use of external validation (docking) for site-specific affinity predictions adds a practical dimension. The writing is clear and the methodological rationale is well-articulated.
- **Major Concerns** The concerns below detail issues with baseline fairness, statistical validation, and the interpretation of generalization results.
- **Minor Comments** Several minor issues regarding clarity and reporting are listed below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (baseline fairness), R1-M2 (statistical significance), R1-M3 (interpretation of generalization metrics), R1-M4 (novelty assessment).
- **Assessment against Nature-style criteria** **Originality:** The unified site-aware framework is a novel combination of existing ideas (ESM-2, MolFormer, cross-attention, MoE, autoregressive generation). The specific mechanism of using binding-site prediction to constrain the latent interaction space appears original. However, the individual components are well-established, and the novelty lies in their integration. **Scientific importance:** If validated, the framework could streamline drug discovery pipelines by providing a single model for screening and design with interpretable outputs. The potential to handle dynamic proteins is scientifically important. **Interdisciplinary readership:** The topic is of high interest to both computational and experimental drug discovery communities. The writing is accessible to a broad scientific audience, though some familiarity with deep learning terminology is assumed. **Technical soundness:** The architecture is plausible, but the provided evidence is insufficient to fully assess soundness. Key concerns include baseline fairness, statistical rigor, and the interpretation of generalization metrics. **Readability for nonspecialists:** The abstract and introduction are clear. The results and methods sections are dense but generally comprehensible. The use of acronyms is heavy but standard for the field.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the preliminary results are encouraging, but the current evidence base does not fully establish the claims of superiority and broad applicability. A revised manuscript with more rigorous baseline comparisons, statistical validation, and clearer interpretation of generalization results would be needed to make a compelling case.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that MolDBG "consistently outperforms baselines across all three base tasks" and achieves "competitive performance" in affinity prediction.
- **Evidence pointer** Results section, Figure 2c-h, Table 1, Section S5, Table S4.
- **Concern** The fairness of the baseline comparisons is not established. For affinity prediction, the baselines (DeepDTA, GraphDTA, WGNN-DTA, AttentionDTA, DTIAM, DeepDTAGen) are retrained on the BioLip-BS dataset. However, it is unclear if these baselines were given the same pre-training opportunities, hyperparameter tuning, or data augmentation (e.g., SMILES randomization) as MolDBG. For generation, the comparison set (PGMG, REINVENT 2.0, SyntaLinker, Pocket2Mol, DEVELOP, LS-MolGen) is heterogeneous, with some methods being structure-based and others sequence-based. The text notes DeepDTAGen was excluded due to convergence issues, which raises questions about the comparability of the training setup. Without a clear statement of the experimental protocol for each baseline, the reported improvements could be attributed to unfair advantages rather than architectural merit.
- **Why it matters** The central claim of the paper is that the proposed framework is superior to existing methods. If the baselines are not optimally configured or fairly compared, the reported performance gains are not convincing. This is a fundamental issue that undermines the validity of the main conclusions.
- **Resolution test** The authors should provide a detailed description of the training and evaluation protocol for each baseline, including hyperparameter search, pre-training strategies, and data augmentation. Ideally, they should also report results with baselines using their recommended settings from the original papers. A table summarizing the configuration of each baseline would be helpful.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that MolDBG achieves "competitive performance" in affinity prediction with MSE 0.6933, Pearson 0.9009, and CI 0.8850, and that it "consistently outperforms baselines."
- **Evidence pointer** Results section, Figure 2c-h.
- **Concern** No statistical significance testing is reported for the affinity prediction results. The text mentions "5-fold cross-validation" but does not provide standard deviations, confidence intervals, or p-values for the differences between MolDBG and the baselines. The observed improvements, particularly the 10% MSE reduction over MolDBG-Vanilla, could be within the range of random variation. The same issue applies to the binding-site prediction and generation metrics.
- **Why it matters** Without statistical validation, it is impossible to determine if the reported improvements are meaningful or merely noise. This is a critical omission for a paper claiming superior performance.
- **Resolution test** The authors should report the mean and standard deviation (or confidence intervals) for all metrics across the cross-validation folds. They should also perform appropriate statistical tests (e.g., paired t-test or Wilcoxon signed-rank test) to compare MolDBG against each baseline and report the resulting p-values.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The claim that MolDBG "generalizes to structurally elusive targets, including cryptic pockets and intrinsically disordered proteins."
- **Evidence pointer** Results section, "Cryptic Pocket Proteins Binding Site Prediction" and "Disordered Protein Binding Sites Prediction", Figure 4b-e, Table S5.
- **Concern** The interpretation of the results on cryptic pockets and IDPs is not fully convincing. For cryptic pockets, the comparison is made against the PocketMiner model, which is a specialized tool. The text reports an AUROC of 0.9014 for MolDBG versus 0.87 for PocketMiner, but it is unclear if this difference is statistically significant. More importantly, the text does not explain how MolDBG, a sequence-based method, can predict cryptic pockets that are defined by conformational changes. The claim that the model "generalizes" to these targets is not well-supported by the provided description. For IDPs, the text reports a sample-level success rate of 72.62% at a specific threshold, but the choice of threshold and the definition of "success" are not fully justified. The text also acknowledges that the IDP dataset contains mostly nucleotide or coenzyme binders, which may not be representative of drug-like molecules.
- **Why it matters** The generalization to challenging targets is a key selling point of the paper. If the evidence for this claim is weak or misinterpreted, the broader impact of the work is diminished.
- **Resolution test** The authors should provide a more detailed analysis of the cryptic pocket predictions, including a discussion of the mechanism by which a sequence-based model can identify conformationally hidden pockets. They should also report statistical significance for the AUROC comparison. For IDPs, they should justify the choice of threshold and provide a breakdown of performance by binder type (e.g., nucleotide vs. drug-like).

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Originality
- **Claim pointer** The claim that MolDBG is a "new model" and a "unified site-aware framework."
- **Evidence pointer** Introduction, Results, Experimental Section.
- **Concern** The novelty of the proposed framework is not fully established. The text cites prior work on multi-task learning for DTI prediction and generation (e.g., DeepDTAGen) and on binding-site prediction (e.g., LABind). The key innovation appears to be the integration of these tasks with explicit binding-site supervision. However, the text does not clearly articulate how this integration differs from or improves upon existing multi-task approaches. The use of ESM-2 and MolFormer as frozen encoders is standard practice. The MoE decoder for affinity prediction is a known technique. The authors should more clearly delineate the specific novel contributions of their architecture.
- **Why it matters** For a high-impact journal, the novelty of the contribution must be clearly articulated. If the framework is largely a combination of existing components, the significance of the work is reduced.
- **Resolution test** The authors should add a dedicated section or paragraph that explicitly states the novel contributions of their work, contrasting it with the closest existing methods (e.g., DeepDTAGen, LABind) and highlighting the specific design choices that lead to improved performance.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that MolDBG "achieves competitive performance across all three tasks" but does not provide any quantitative results. This is common for abstracts, but given the space constraints, a single headline metric (e.g., AUROC on PocketMiner) would strengthen the impact.
- **Required correction** Consider adding one or two key quantitative results to the abstract to support the claims.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Experimental Section, "Training Details and Parameter Settings"
- **Evidence pointer** Experimental Section
- **Issue** The text mentions that the model was trained on 8 NVIDIA V100 GPUs for 5 days but does not provide the total number of parameters, the inference time, or the computational cost of the baseline models. This information is important for assessing the practical utility of the method.
- **Required correction** Add a table or paragraph detailing the model size, training time, and inference speed for MolDBG and all baselines.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data Availability Statement
- **Evidence pointer** Data Availability Statement
- **Issue** The statement says code and data are available at a GitHub link, but the link is not included in the provided text. Also, it is unclear if the BioLip-BS dataset is publicly available or if it is a new dataset created by the authors.
- **Required correction** Include the full URL in the final version. Clarify the provenance of the BioLip-BS dataset and provide a detailed description of how it was constructed.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results, "Site-Specific Affinity Prediction and the Discrimination of Regional Binding Variations"
- **Evidence pointer** Results section
- **Issue** The CA2 case study is interesting, but the text does not explain how the "perturbation window strategy" works in detail. The reader is left to infer the mechanism from the name alone.
- **Required correction** Provide a brief description of the perturbation window strategy in the main text or refer the reader to a specific supplementary section.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, "Random Molecule Generation Performance"
- **Evidence pointer** Results section
- **Issue** The text states that MolDBG "surpassed PGMG by approximately 2.5% in validity" but does not provide the absolute values for either method. This makes it difficult to gauge the practical significance of the improvement.
- **Required correction** Report the absolute values for all metrics in Table 1 and refer to them explicitly in the text.

## Risk / unsupported claims
- The claim of "consistent outperformance" across all tasks is not supported without statistical significance testing and a clear description of baseline configurations.
- The claim of generalization to cryptic pockets is not fully supported by the provided evidence, as the mechanism by which a sequence-based model predicts conformationally hidden pockets is not explained.
- The claim of generalization to IDPs is based on a dataset where most binders are nucleotides or coenzymes, which may not be representative of drug-like molecules. The relevance of this result to drug discovery is not fully established.
- The claim of "interpretable binding-site discovery" is plausible but not directly demonstrated in the text. The visualization in Figure 3 is referenced but not assessable.
- The novelty of the framework relative to existing multi-task approaches is not clearly articulated, making it difficult to assess the originality of the contribution.