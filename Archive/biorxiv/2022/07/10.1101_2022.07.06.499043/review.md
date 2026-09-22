## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary file descriptions
- **Assessment boundary** Scientific validity, methodological rigor, interpretability claims, and comparative performance claims of the LLPhyScore predictor
- **Shared manuscript claim summary** The authors present LLPhyScore, a machine learning-based predictor of IDR-driven protein phase separation, trained on 16 biophysical features derived from PDB statistics, with a 3-layer neural network-like architecture optimized via genetic algorithm. They claim strong predictive performance (AUROC 0.978), physical interpretability through feature contribution breakdowns, and robustness across three negative training sets.
- **Visible evidence base** Main text figures referenced (Figures 1-13), supplementary tables and figures described, methods section, GitHub repository link
- **Missing materials affecting confidence** Actual figure images, supplementary tables S1-S10 contents, supplementary figures S1-S11, training/test data splits, hyperparameter details, baseline comparison data, and code implementation details were not provided in the submitted material

## Reviewer
- **Overall assessment** The manuscript addresses an important problem in the phase separation field by attempting to create a physically interpretable predictor that moves beyond black-box approaches. The conceptual framework of combining multiple biophysical features with competitive training is sound and potentially valuable. However, the current manuscript has several critical gaps that prevent full evaluation of the claims. The most significant concerns relate to the lack of detailed validation methodology, potential circularity in feature derivation, unclear handling of sequence redundancy, and insufficient evidence for the interpretability claims. The comparison with existing predictors is incomplete and the reported performance metrics may not be directly comparable across methods. The manuscript would benefit from more rigorous benchmarking, clearer description of the training procedure, and validation on independent experimental datasets beyond the training set.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates and phase separation, computational biologists developing sequence-based predictors, and experimentalists seeking to identify phase-separating proteins or understand the biophysical drivers of specific condensates. The tool could be valuable for generating hypotheses about which physical interactions dominate in particular phase-separating systems and for screening proteins for phase separation propensity.

- **Major strengths** 
  1. Addresses a clear gap in the field by providing physical interpretability that other predictors lack
  2. Thoughtful consideration of the negative training set problem with multiple approaches
  3. Broad feature set covering diverse biophysical interactions
  4. The clustering-based train/test split addresses sequence redundancy concerns
  5. The feature breakdown analysis provides a useful framework for understanding different phase separation drivers

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that LLPhyScore achieves AUROC of 0.978 on Evaluation set 1 and strong performance across evaluation sets
- **Evidence pointer** Results section, Figure 6, Supplementary Figures S3-S5, location not provided
- **Concern** The evaluation methodology appears to have a critical flaw. The PDB negative set used for evaluation (Evaluation set 1) contains the same sequences used for feature derivation. Since the physical features are derived from PDB statistics, the model may be artificially favored on PDB-derived negatives. More critically, the positive training set (305 sequences) and test set (260 sequences) are split by clustering, but the negative sets are split randomly at the sequence level. This asymmetry in splitting methodology could lead to inflated performance estimates. The authors need to clarify whether the negative sequences in the test set share similarity with training negatives, and if so, how this affects the reported AUROC values.
- **Why it matters** If the evaluation protocol is biased, the reported performance metrics cannot be trusted, and the claimed superiority over other predictors may not hold in real-world applications where novel sequences are encountered.
- **Resolution test** Provide a clear description of how negative sequences were split between training and test sets, including whether clustering was applied to negatives. Re-evaluate performance using a truly independent test set where neither positives nor negatives share significant sequence similarity with training data. Report performance stratified by sequence similarity to training sets.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that the 3-layer neural network-like model with genetic algorithm optimization provides meaningful physical interpretability through feature weights
- **Evidence pointer** Methods section, Predictor training subsection, location not provided
- **Concern** The interpretability claim is not sufficiently supported. The model uses threshold-based binary scoring (upper/lower weights per feature per residue type), which is a highly simplified representation. The genetic algorithm optimizes 640 weights (16 features x 20 residues x 2 thresholds) with only 305 positive training sequences. This creates a severe overfitting risk that the authors acknowledge but do not adequately address. More critically, the "competitive training" approach that ranks feature importance is not clearly distinguished from the weight optimization, and the stability of feature rankings across different random seeds or initial conditions is not reported. The claim that feature contributions can be quantitatively interpreted requires demonstration that the weights are stable and meaningful, not just that they produce good AUROC.
- **Why it matters** The central value proposition of LLPhyScore over other predictors is its physical interpretability. If the feature weights are unstable or overfit, the interpretability claims are unfounded, and the tool provides no advantage over black-box predictors.
- **Resolution test** Report feature weight stability across multiple runs with different random seeds. Provide validation that the feature importance rankings are consistent when trained on different subsets of the data. Demonstrate that the feature contributions for specific proteins align with experimental knowledge (e.g., known drivers of phase separation for well-characterized proteins).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that LLPhyScore outperforms first-generation predictors and is comparable to PSPredictor
- **Evidence pointer** Results section, Figure 9, location not provided
- **Concern** The comparison with other predictors is inadequately described. The authors state that LLPhyScore outperforms PScore and catGRANULE and is comparable to PSPredictor, but the exact comparison methodology is unclear. Were all predictors evaluated on the same test sets? Were the same evaluation metrics used? The authors mention that PSPredictor was trained on different data, which could affect fair comparison. Additionally, the comparison with FuzDrop is only described qualitatively ("comparable recall trends"), without quantitative metrics. The choice of evaluation sets (PDB vs. human proteome) may favor different predictors depending on their training data.
- **Why it matters** Without rigorous, fair benchmarking against existing tools, the claimed advantages of LLPhyScore cannot be substantiated. The phase separation field already has multiple predictors, and a new tool must demonstrate clear advantages to be adopted.
- **Resolution test** Provide a detailed comparison table showing AUROC, precision, recall, and other relevant metrics for all predictors on identical evaluation sets. Describe the exact protocol for running each predictor, including any parameter tuning. Discuss potential biases in the comparison and how they were addressed.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The claim that the feature breakdown analysis provides insights into how different physical interactions drive phase separation in different proteins
- **Evidence pointer** Results section, Feature breakdown subsection, Figure 10, location not provided
- **Concern** The clustering of proteins based on their feature scores and the identification of distinct clusters (e.g., FUS, Nup98, ELP, MEG-3) is presented as evidence of the tool's ability to differentiate phase separation drivers. However, the biological validation of these clusters is limited. The authors do not provide experimental evidence that proteins in the same cluster share similar phase separation mechanisms, nor do they demonstrate that the feature-based clustering provides information beyond what could be obtained from sequence composition alone. The connection between the identified features and the actual biophysical mechanisms of phase separation for these specific proteins is asserted but not experimentally verified.
- **Why it matters** The claim that LLPhyScore can provide mechanistic insights into phase separation is a key selling point. If the feature-based clustering does not correspond to biologically meaningful differences in phase separation mechanisms, the interpretability advantage is largely cosmetic.
- **Resolution test** Provide experimental validation for at least a few proteins in different clusters, demonstrating that the predicted dominant features align with experimentally determined drivers of phase separation. Alternatively, compare the feature-based clustering with known functional classifications of phase-separating proteins.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The claim that the negative training set issue is addressed by using three different negative sets
- **Evidence pointer** Results section, Model performance comparison subsection, Figure 6, location not provided
- **Concern** While the authors train models on three different negative sets (PDB, human, PDB+human), the analysis of how these different training conditions affect the model's behavior is superficial. The authors note that the PDB model performs best on Evaluation set 1 and worst on Evaluation set 2, but do not provide a deeper analysis of why this occurs or what it means for practical use. More critically, the human negative set was filtered using CRAPome scores, but the rationale for this specific filtering threshold and its impact on the negative set composition is not discussed. The authors also do not address whether the choice of negative set affects the feature importance rankings, which would be crucial for the interpretability claims.
- **Why it matters** The choice of negative training set is a critical methodological decision that affects both performance and interpretability. Without a thorough analysis of how this choice impacts the model, users cannot make informed decisions about which model to use for their specific application.
- **Resolution test** Provide a detailed comparison of feature importance rankings across the three models. Discuss the biological rationale for the CRAPome filtering threshold. Provide guidance on which model should be used in different application scenarios.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Methods section, Physical feature collection
- **Evidence pointer** Methods section, location not provided
- **Issue** The description of the 16 physical features is dense and lacks sufficient detail for reproducibility. For example, the definition of "kinked-beta similarity" and "kinked-beta non-similarity" is vague, and the exact procedure for calculating these values from PDB structures is not fully specified.
- **Required correction** Provide a more detailed description of each feature, including the exact algorithms and parameters used. Consider adding a supplementary table with feature definitions and calculation procedures.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods section, Predictor training
- **Evidence pointer** Methods section, location not provided
- **Issue** The description of the genetic algorithm is incomplete. The authors do not specify population size, mutation rate, crossover rate, convergence criteria, or the number of generations used. This makes it impossible to reproduce the training procedure.
- **Required correction** Provide complete details of the genetic algorithm parameters and implementation. If the code is available on GitHub, reference specific files and functions that implement the training procedure.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Results section, Gene Ontology enrichment
- **Evidence pointer** Results section, Gene Ontology term enrichment subsection, Figure 11, location not provided
- **Issue** The GO enrichment analysis is presented as supporting evidence for the biological relevance of LLPhyScore predictions, but the analysis is described only briefly. The authors do not discuss whether the enriched GO terms are specific to phase separation or whether they reflect general properties of the proteins in the positive set.
- **Required correction** Provide a more detailed discussion of the GO enrichment results, including comparison with GO enrichments from other predictors and discussion of whether the enriched terms are phase-separation-specific.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Introduction
- **Evidence pointer** Introduction, location not provided
- **Issue** The introduction provides a good overview of the field but could benefit from a clearer statement of the specific limitations of existing predictors that LLPhyScore addresses. The distinction between "first-generation" predictors and more recent tools like PSPredictor is mentioned but not fully elaborated.
- **Required correction** Expand the introduction to more clearly articulate the specific gaps in existing tools that LLPhyScore fills, particularly regarding interpretability and the breadth of biophysical features considered.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results section, Predictor training
- **Evidence pointer** Results section, Predictor training subsection, location not provided
- **Issue** The authors report AUROC values for training and test sets but do not report other performance metrics such as precision, recall, F1 score, or calibration. AUROC alone can be misleading, especially with imbalanced datasets.
- **Required correction** Report additional performance metrics, including precision-recall curves and calibration plots. Discuss the practical implications of the precision-recall trade-off for users of the tool.

## Risk / unsupported claims
- The claim that LLPhyScore provides "quantitative breakdown of the contribution from each physical feature" is not fully supported. The feature weights are optimized for classification performance, not for accurately estimating the true biophysical contribution of each interaction. The weights may reflect correlations and redundancies among features rather than causal contributions.
- The claim that the tool can "provide hypotheses regarding key interactions driving phase separation" is plausible but not validated. No experimental validation is provided to confirm that the feature contributions predicted by LLPhyScore align with experimentally determined drivers of phase separation.
- The claim that LLPhyScore "has strong phase separation prediction recall statistics" is based on AUROC values, but the practical utility depends on the precision-recall trade-off at relevant thresholds, which is not reported.
- The comparison with FuzDrop is described only qualitatively, without quantitative metrics, making it impossible to assess the relative performance.
- The statement that "up to 40% of the human proteome potentially can undergo phase separation" is attributed to FuzDrop, but the authors do not critically evaluate this estimate or discuss its implications for their own results.
- The claim that the model provides "physical interpretability not possible with another comprehensive predictor, PSPredictor" is not substantiated. The authors do not demonstrate that the feature contributions from LLPhyScore provide insights that could not be obtained from other analysis methods applied to PSPredictor or other predictors.