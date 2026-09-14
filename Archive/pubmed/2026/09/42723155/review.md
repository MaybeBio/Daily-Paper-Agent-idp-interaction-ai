## Review setup
- **Input scope** Full manuscript (abstract, introduction, results, discussion, experimental section, and references)
- **Assessment boundary** Scientific claims, methodology, experimental design, results, and conclusions as presented in the manuscript
- **Shared manuscript claim summary** The authors propose MolDBG, a unified site-aware framework that integrates drug-target affinity prediction, binding-site identification, and affinity-conditioned molecular generation within a single architecture, using only sequence data and achieving competitive performance across all three tasks.
- **Visible evidence base** Full text including figures (referenced but not provided), tables (Table 1 referenced but not provided), and supplementary materials (referenced but not provided)
- **Missing materials affecting confidence** Figures 1-5, Table 1, Tables S1-S10, and all supplementary sections (S2-S8) are referenced but not provided. The code repository URL is provided but not accessible for verification.

## Reviewer
- **Overall assessment** This manuscript presents an ambitious and technically sophisticated framework that attempts to unify three critical tasks in computational drug discovery. The core idea of using binding-site supervision to guide both affinity prediction and molecular generation is conceptually sound and addresses a genuine limitation in current methods. However, the manuscript suffers from several significant issues that undermine the strength of the claims. The most critical concern is the lack of a rigorous comparison against state-of-the-art methods under identical conditions, particularly for the molecular generation task where key baselines (e.g., REINVENT 2.0, PGMG) are not retrained on the same data. Additionally, the evaluation of site-specific affinity prediction relies on a single case study (CA2) with limited statistical power, and the generalization claims to cryptic pockets and IDPs are based on binding-site prediction alone, not on the full integrated tasks. The technical novelty, while present, is incremental over existing multi-task and pre-training approaches.
- **Who would be interested in the results, and why** Computational chemists, medicinal chemists, and researchers in AI-driven drug discovery would be interested because the framework offers a unified approach to affinity prediction, binding-site identification, and molecular generation, which could streamline the drug design pipeline. The demonstrated ability to handle cryptic pockets and IDPs, even if only for binding-site prediction, is of particular interest to those working on challenging protein targets.
- **Major strengths** 1. The unified multi-task framework is conceptually elegant and addresses a real need in the field. 2. The use of binding-site supervision to guide representation learning is a well-motivated approach that improves interpretability. 3. The extension to challenging protein classes (cryptic pockets, IDPs) is a valuable contribution. 4. The two-stage training strategy (pre-training on large-scale data, fine-tuning on curated data) is practical and well-justified.
- **Major Concerns** 
- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental design and fairness of comparison
- **Claim pointer** "MolDBG achieved competitive performance across all three tasks" and "our approach consistently outperforms baselines across all three base tasks"
- **Evidence pointer** Results sections (Drug-Target affinity Prediction Performance, Small Molecule-Protein Interaction Binding Sites Prediction Performance, Random Molecule Generation Performance)
- **Concern** The baseline comparisons are fundamentally unfair. For the molecular generation task, the authors compare against models like REINVENT 2.0 and PGMG that were trained on different datasets (likely much larger or different chemical spaces) and report their published performance. The authors explicitly state that DeepDTAGen could not converge on the BioLip-BS dataset due to its small size, yet they compare MolDBG (pre-trained on 1.4M pairs) against models that were not pre-trained on the same data. For affinity prediction, all baselines are retrained on BioLip-BS, but this dataset is only 11,045 samples, which is extremely small for training deep learning models from scratch. The authors do not report whether these baselines were also pre-trained or if they were trained from scratch, creating an apples-to-oranges comparison. The claim of "outperforming" is not supported without controlling for training data size and pre-training strategy.
- **Why it matters** The central claim of the paper is that MolDBG achieves superior or competitive performance. If the baselines are not evaluated under equivalent conditions (same training data, same pre-training if applicable), the comparison is invalid and the claims are unsupported. This undermines the entire results section.
- **Resolution test** The authors must retrain all baseline models under identical conditions: either (a) pre-train all baselines on the same 1.4M BindingDB data before fine-tuning on BioLip-BS, or (b) train MolDBG from scratch on BioLip-BS without pre-training and compare against baselines trained from scratch. Alternatively, provide a clear ablation showing the contribution of pre-training by comparing MolDBG with and without pre-training against baselines with and without pre-training.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor and validation
- **Claim pointer** "MolDBG achieved a CI value of 0.7124 and a Pearson of 0.6010, indicating that the model possesses a robust ability to distinguish affinity variations across distinct binding sites"
- **Evidence pointer** Site-Specific Affinity Prediction and the Discrimination of Regional Binding Variations section, Figure 3
- **Concern** The site-specific affinity prediction evaluation is based on a single protein (CA2) with a limited number of binding sites. The authors report CI and Pearson values but do not provide confidence intervals, p-values, or any measure of statistical significance. The comparison against AutoDock Vina docking scores is problematic because Vina scores are not directly comparable to pKd/pIC50 values; the authors negate Vina scores to align correlation direction, but this transformation is not validated. Furthermore, the authors acknowledge a discrepancy between Site 2 and Site 20 but dismiss it as "acceptable" without quantitative justification. A single case study with 20-30 data points is insufficient to support the claim of "robust ability."
- **Why it matters** The ability to discriminate binding affinities across different sites on the same protein is a key claimed advantage of MolDBG over global methods. Without rigorous statistical validation on multiple proteins and a larger number of binding sites, this claim remains anecdotal. The field requires systematic evaluation across diverse multi-site proteins.
- **Resolution test** The authors should evaluate site-specific affinity prediction on at least 5-10 multi-site proteins from UniSite-DS, report per-protein and aggregate statistics with confidence intervals, and provide a statistical test (e.g., permutation test) to assess whether the correlation is significantly better than random. The comparison against docking should use a validated transformation or a common metric.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalization claims vs. evidence
- **Claim pointer** "The framework generalizes to structurally elusive targets, including cryptic pockets and intrinsically disordered proteins"
- **Evidence pointer** Cryptic Pocket Proteins Binding Site Prediction and Disordered Protein Binding Sites Prediction sections, Figure 4b-e
- **Concern** The generalization claims are based solely on binding-site prediction, not on the full integrated tasks of affinity prediction or molecular generation for these challenging targets. For cryptic pockets, the model achieves an AUROC of 0.9014 on PocketMiner, but this is a binding-site prediction benchmark, not a test of whether the model can predict affinity or generate molecules for cryptic pocket proteins. For IDPs, the model achieves an AUROC of 0.8187, but the authors note that most annotated sites bind nucleotides or coenzymes, not clinical drug molecules, and fewer than 15% involve drug molecules. The claim of generalization to "structurally elusive targets" for the full framework (affinity prediction and molecular design) is not supported by the evidence presented.
- **Why it matters** The abstract and introduction frame MolDBG as a unified framework for all three tasks, and the generalization to challenging targets is a major selling point. If the evidence only supports binding-site prediction for these targets, the claims are overstated and misleading. Readers may assume the model can perform affinity prediction and molecular design for IDPs and cryptic pockets, which is not demonstrated.
- **Resolution test** The authors should either (a) provide evidence of affinity prediction and/or molecular generation performance on cryptic pocket and IDP targets, or (b) explicitly qualify the claims to state that generalization is demonstrated only for binding-site prediction, and that affinity prediction and molecular generation for these targets remain to be validated.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Novelty and conservatism in molecular generation
- **Claim pointer** "MolDBG achieved performance comparable to PGMG and REINVENT 2.0 across multiple metrics" and "While the Novelty scores were modest, we attribute this primarily to minor overfitting"
- **Evidence pointer** Random Molecule Generation Performance section, Table 1
- **Concern** The authors report modest Novelty scores and attribute this to "minor overfitting" and the "inherent constraints" of target-specific generation. However, the novelty metric is critical for generative models: a model that generates molecules already in the training set is not truly designing new compounds. The authors do not provide a quantitative analysis of how many generated molecules are truly novel (i.e., not in any training or test set) versus simple variations of known molecules. The claim that "these results confirm the model's ability to generate valid drug candidates" is weakened if the generated molecules are largely known. Furthermore, the comparison against PGMG and REINVENT 2.0 is problematic because these models were not retrained on the same data (see R1-M1).
- **Why it matters** The value of a generative model in drug discovery is its ability to propose novel, synthesizable molecules with desired properties. If the model primarily reproduces known molecules, its practical utility is limited. The authors need to provide a more rigorous analysis of novelty, including Tanimoto similarity to nearest training set molecules and a discussion of whether the generated molecules are truly novel or merely recombinations of known fragments.
- **Resolution test** The authors should provide a detailed novelty analysis: (a) report the distribution of Tanimoto similarities between generated molecules and the nearest training set molecules, (b) provide examples of truly novel molecules (e.g., with Tanimoto < 0.4 to any training molecule), and (c) discuss whether the modest novelty is a fundamental limitation of the approach or can be addressed by future modifications.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Interpretability and validation of binding-site predictions
- **Claim pointer** "MolDBG explicitly models drug-target interactions and predicts binding sites concomitantly with molecule generation" and "the physical interaction sites determined by Vina docking exhibit a high degree of spatial overlap with the binding sites predicted by our model"
- **Evidence pointer** Affinity-Based Conditional Molecular Design section, Figure 5g-l
- **Concern** The claim of interpretability is supported by a qualitative comparison between MolDBG-predicted binding sites and Vina docking poses for two targets (EGFR and VEGFR2). However, the authors do not provide quantitative metrics (e.g., overlap coefficient, distance between predicted and docked residues) to support the claim of "high degree of spatial overlap." The visualization is limited to six molecules (three per target), which is insufficient to demonstrate general interpretability. Additionally, the use of Vina docking as a ground truth for binding sites is questionable because docking predictions can be inaccurate, especially for flexible targets.
- **Why it matters** Interpretability is a key claimed advantage of MolDBG over black-box models. Without quantitative validation on a larger set of protein-ligand complexes, the interpretability claim remains anecdotal. The field needs rigorous benchmarks for evaluating interpretability, such as comparing predicted binding residues against crystallographic data.
- **Resolution test** The authors should provide a quantitative evaluation of binding-site prediction accuracy for the generated molecules, using either (a) crystallographic data from the PDB for known complexes, or (b) a larger set of docking predictions with statistical measures (e.g., mean distance between predicted and docked residues, fraction of predicted residues within 5Å of docked ligand). A minimum of 50-100 protein-ligand pairs should be evaluated.

- **Minor Comments** 
- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and completeness
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states "MolDBG achieves competitive performance across all three tasks" but does not specify which metrics or datasets were used. This is too vague for a Nature-style abstract.
- **Required correction** Include specific performance numbers (e.g., MSE, Pearson, AUROC) for at least the primary task in the abstract.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Experimental Section - Datasets
- **Evidence pointer** Datasets section
- **Issue** The authors state that the BioLip-BS dataset was constructed by "performing rigorous structure, sequence, and binding-site alignment checks on Q-BioLiP" but do not provide the exact filtering criteria or thresholds used. This makes it difficult for others to reproduce the dataset.
- **Required correction** Provide the exact filtering criteria (e.g., sequence identity threshold, structure alignment RMSD cutoff, binding-site overlap requirement) in the main text or supplementary materials.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Drug-Target affinity Prediction Performance section
- **Evidence pointer** Figure 2c-h
- **Issue** The authors report MSE, Pearson, and CI for MolDBG but do not provide standard deviations or confidence intervals for these metrics, even though 5-fold cross-validation was performed.
- **Required correction** Report mean and standard deviation (or 95% confidence intervals) for all metrics across the 5 folds.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity of methodology
- **Affected element** Model Architecture - Drug-Target Interaction Learning Module
- **Evidence pointer** Equation 2 and surrounding text
- **Issue** The LSQM module uses cross-attention with molecular embedding as Query and protein embedding as Key/Value. However, the authors do not explain how the "pseudo-ligand embedding" is generated for the molecular design task. They mention "random sampling" but do not specify the distribution or dimensionality.
- **Required correction** Clearly specify the distribution (e.g., N(0,I)) and dimensionality of the pseudo-ligand embedding, and explain how it is sampled during training and inference.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data Availability Statement
- **Evidence pointer** Data Availability Statement
- **Issue** The code repository URL is provided, but the authors do not state whether the data (BioLip-BS, processed BindingDB) will be made available. Given the complexity of dataset construction, this is essential for reproducibility.
- **Required correction** State explicitly that all datasets (raw and processed) will be made available upon publication, and provide a plan for data deposition (e.g., Zenodo, Figshare).

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Overclaiming
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The authors state "MolDBG can not only predict affinity but also dynamically distinguish binding strengths across distinct pockets for the same ligand." This is supported by only a single case study (CA2), which is insufficient for such a strong claim.
- **Required correction** Qualify the claim by adding "as demonstrated in a case study on Carbonic Anhydrase II" or provide additional validation.

- **Technical failings that need to be addressed before the case is established** R1-M1 (unfair baseline comparison), R1-M2 (insufficient statistical validation for site-specific affinity prediction), R1-M3 (overclaimed generalization), R1-M4 (insufficient novelty analysis), R1-M5 (unvalidated interpretability claim)

- **Assessment against Nature-style criteria** 
  - **Originality**: Moderate. The idea of unifying affinity prediction, binding-site identification, and molecular generation in a single framework is not entirely novel (DeepDTAGen and other multi-task models exist), but the specific use of binding-site supervision to guide representation learning is a meaningful contribution. The extension to cryptic pockets and IDPs, while limited, adds some originality.
  - **Scientific importance**: High. The problem of integrating multiple tasks in drug discovery is important, and the potential to improve interpretability and reduce false positives is valuable. However, the importance is diminished by the lack of rigorous validation and the overclaimed generalization.
  - **Interdisciplinary readership**: Moderate. The work is relevant to computational chemistry, structural biology, and machine learning, but the technical depth and lack of clear biological validation may limit appeal to a broader audience.
  - **Technical soundness**: Low to moderate. The methodology is well-motivated and technically sophisticated, but the experimental validation is flawed (unfair comparisons, insufficient statistics, overclaimed results). The technical soundness of the core claims is not established from the provided evidence.
  - **Readability for nonspecialists**: Moderate. The manuscript is well-written and the concepts are explained clearly, but the heavy reliance on technical jargon and the lack of a clear summary of key results for a general audience are limitations.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript presents a promising framework with a sound conceptual basis, but the experimental validation is insufficient to support the major claims. The authors must address the critical concerns regarding baseline fairness, statistical rigor, and overclaimed generalization before the case can be considered established. A major revision with additional experiments and more careful claims is required.

## Risk / unsupported claims
- "MolDBG achieves competitive performance across all three tasks" - unsupported due to unfair baseline comparisons (R1-M1)
- "robust ability to distinguish affinity variations across distinct binding sites" - unsupported due to single case study and lack of statistical rigor (R1-M2)
- "The framework generalizes to structurally elusive targets, including cryptic pockets and intrinsically disordered proteins" - unsupported for affinity prediction and molecular generation; only binding-site prediction is demonstrated (R1-M3)
- "the physical interaction sites determined by Vina docking exhibit a high degree of spatial overlap with the binding sites predicted by our model" - unsupported due to lack of quantitative metrics and small sample size (R1-M5)
- "MolDBG effectively generates drug candidates with specified binding affinities for given protein sequences" - partially supported but weakened by modest novelty scores and lack of rigorous novelty analysis (R1-M4)