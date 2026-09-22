## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and figure/table legends as provided.
- **Assessment boundary** Scientific soundness, methodological rigor, validity of claims relative to presented evidence, and suitability for a general interdisciplinary audience. Editorial and stylistic line-editing are outside the scope of this review.
- **Shared manuscript claim summary** The authors present PNABPred, a multi-modal framework combining ESM-2 protein language model embeddings with Atchley factor biophysical descriptors and BLOSUM50 evolutionary substitution scores, processed through a transformer backbone, for two tasks: protein-level classification of nucleic acid-binding proteins and residue-level prediction of nucleic acid-binding sites. The authors claim state-of-the-art performance on multiple benchmark datasets, superior generalization to new data, and meaningful contributions from each feature modality based on ablation studies.
- **Visible evidence base** Results section with performance tables (Tables 1 and 2), ablation study descriptions (Figure 3, Tables S7 and S8), backbone architecture comparisons (Figure S1, Table S9), t-SNE visualizations (Figure 3C-F, Figure S2), amino acid composition analyses (Figure S3), case studies (Figure 4, Figure S5), and additional analyses of binding specificity patterns (Figures S6 and S7). Method details for datasets, feature construction, model architecture, and statistical procedures are provided.
- **Missing materials affecting confidence** The full supplemental document (Document S1) containing Figures S1-S7 and Tables S1-S10 was not provided. This includes critical details such as dataset statistics (Tables S1, S2), new test set construction details (Table S3), full performance tables (Table S4), hyperparameter settings (Table S10), and additional analyses referenced in the main text. Without these, several claims cannot be fully verified. Additionally, no information is provided on how baseline models were reproduced or whether their reported metrics were taken from original publications.

## Reviewer
- **Overall assessment** The manuscript presents a technically sound and potentially useful framework for protein-nucleic acid interaction prediction. The core idea of combining pLM embeddings with classical biophysical and evolutionary features is reasonable and the reported performance improvements are notable. However, the manuscript has several significant weaknesses that prevent full endorsement. The statistical analysis is inadequately described, with no information on how the Mann-Whitney U test was applied across datasets or whether the 10-run procedure was applied to all comparisons. The claim of superiority over state-of-the-art methods is weakened by the lack of detail on baseline reproduction. The generalization experiments, while a strength, are incompletely described without the supplemental tables. The case studies are qualitative and do not provide quantitative comparison with other methods. The discussion of limitations is thoughtful but the framing of the IDR advantage is not directly tested. The manuscript would benefit from clearer articulation of what is genuinely novel compared to existing multi-modal approaches, and from more rigorous statistical reporting.

- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein function prediction, particularly those developing or using sequence-based methods for nucleic acid binding site annotation. Researchers studying DNA-binding proteins, transcription factors, and RNA-binding proteins may find the tool useful for hypothesis generation. The framework's general architecture (multi-modal feature fusion with pLMs) may also interest method developers working on other protein function prediction tasks. The claim of handling intrinsically disordered regions could attract researchers studying IDR function, though this is not directly demonstrated.

- **Major strengths** The multi-modal feature fusion strategy is well-motivated and the ablation studies support the contribution of each modality. The use of LoRA for parameter-efficient fine-tuning of ESM-2 is a sensible practical choice. The inclusion of newly curated test sets from BioLiP with a recent cutoff (January 2025) is a genuine strength for assessing generalization. The case studies span diverse protein families and organisms, demonstrating broad applicability. The authors are transparent about the limitation that the model does not predict nucleic acid sequence specificity.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor and reproducibility
- **Claim pointer** The manuscript claims PNABPred significantly outperforms other methods (p < 0.05, Mann-Whitney U test) across all evaluations.
- **Evidence pointer** Results section, "PNABPred improves the accuracy of protein-nucleic acid binding prediction"; Methods, "Statistical analysis"
- **Concern** The statistical analysis section states that PNABPred and a second-best baseline were trained 10 times and compared using the Mann-Whitney U test, but it is unclear whether this 10-run procedure was applied to all baseline methods across all datasets, or only to a single comparison. The p-values reported in the text are not accompanied by effect sizes, confidence intervals, or information on which specific comparisons were tested. The Benjamini-Hochberg procedure is mentioned but the number of hypotheses tested and the adjusted p-values are not reported. Without this information, the claim of significant superiority cannot be evaluated.
- **Why it matters** The central claim of the manuscript is that PNABPred outperforms existing methods. If the statistical comparison is incomplete or improperly applied, the claim is not established. Readers cannot assess the robustness of the reported improvements.
- **Resolution test** Provide a complete description of the statistical testing procedure, including: (1) which methods were reproduced with 10 runs and which were taken from literature values, (2) the exact number of hypotheses tested per dataset, (3) all raw and adjusted p-values, and (4) effect sizes or confidence intervals for the key comparisons. If literature values were used for some baselines, state this explicitly and discuss the limitations of such comparisons.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence for generalization claims
- **Claim pointer** The manuscript claims PNABPred shows "rigorous generalization assessment" and outperforms CLAPE-DB on newly curated BioLiP datasets and cross-training experiments.
- **Evidence pointer** Results section, "PNABPred has better generalization ability"; Figure 2E-F; Tables S3 and S4
- **Concern** The generalization experiments are described only briefly in the main text, with all details relegated to supplemental tables that were not provided. The construction of the new BioLiP test sets is described in one sentence, and the sequence identity filtering procedure is not detailed. The cross-training experiments are mentioned but the setup is unclear: were both models trained on both training sets and evaluated on both test sets? The results in Figure 2E-F are referenced but the actual values are not given in the main text. Without the supplemental data, the strength of the generalization claim cannot be assessed.
- **Why it matters** Generalization to new data is a key differentiator for practical utility. If the new test sets are not carefully constructed or the cross-training protocol is flawed, the generalization claim is weakened. The reader cannot verify the claim without the missing tables.
- **Resolution test** Provide the full details of the new test set construction, including the number of proteins, the sequence identity filtering procedure, and the overlap removal process. Describe the cross-training protocol explicitly, including which training and test set combinations were used. Report the actual performance values for the generalization experiments in the main text or ensure the supplemental tables are available for review.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Novelty and positioning relative to existing work
- **Claim pointer** The introduction states that existing pLM-based methods have limitations and that the multi-modal integration of biophysical and evolutionary features is a novel contribution.
- **Evidence pointer** Introduction section; Discussion section
- **Concern** The manuscript does not clearly articulate what is genuinely novel about the multi-modal fusion approach compared to existing methods that also combine pLM embeddings with additional features. Several published methods (e.g., DNAPred, NCBRPred, and others cited in Tables 1 and 2) already incorporate evolutionary information such as PSSM profiles. The specific contribution of Atchley factors and BLOSUM50 in the context of pLMs is not clearly distinguished from prior work. The authors should more explicitly state what is new about their feature combination strategy and why it is expected to work better than alternatives.
- **Why it matters** For a methods paper, the novelty of the approach is a primary criterion for significance. If the contribution is primarily incremental (adding two classical feature types to a pLM), the impact is reduced. The authors need to make a clearer case for why this specific combination is non-obvious and technically innovative.
- **Resolution test** Revise the introduction and discussion to explicitly compare the proposed multi-modal strategy with existing multi-feature approaches, highlighting the specific architectural or conceptual innovations. If the novelty is primarily in the systematic evaluation or the specific feature combination, state this clearly and justify why it matters.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** IDR claim support
- **Claim pointer** The abstract and discussion claim PNABPred can identify binding sites in intrinsically disordered regions, which is presented as an advantage over structure-based methods.
- **Evidence pointer** Abstract; Discussion section; Case studies (Figure 4B, 2GZK)
- **Concern** The claim that PNABPred handles IDRs is based on a single case study (2GZK) and is not systematically evaluated. No quantitative comparison is provided showing that PNABPred performs better on IDR-containing proteins than other sequence-based methods or that it specifically outperforms structure-based methods on such proteins. The discussion states this as a potential advantage but the evidence is anecdotal.
- **Why it matters** The IDR advantage is a potentially important differentiator, as many nucleic acid binding proteins contain disordered regions. If this claim is not rigorously supported, it should be softened or explicitly labeled as preliminary.
- **Resolution test** Either provide a systematic analysis of PNABPred performance on proteins with known IDRs compared to proteins without, or revise the claim to be more cautious, stating that the case study suggests potential utility in IDR-containing proteins that requires further validation.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Baseline comparison fairness
- **Claim pointer** The manuscript claims PNABPred outperforms "other state-of-the-art sequence-based methods" across multiple benchmarks.
- **Evidence pointer** Tables 1 and 2; Methods, "Datasets"
- **Concern** The performance values for baseline methods in Tables 1 and 2 are stated to be "taken from ref." (references 35-49), meaning they are literature-reported values rather than independently reproduced results. This is a common practice but introduces potential bias: different studies may use different data splits, evaluation protocols, or post-processing steps. The manuscript does not discuss this limitation or attempt to control for it. Only CLAPE was reproduced with 10 runs for statistical comparison, but the details of this reproduction are not given.
- **Why it matters** Fair comparison is essential for establishing superiority. If baselines are not reproduced under identical conditions, the reported improvements may be due to differences in evaluation protocol rather than genuine model superiority.
- **Resolution test** Either reproduce all baseline methods under identical conditions, or explicitly acknowledge the limitation of comparing against literature values and discuss the potential impact on the conclusions. Provide details of the CLAPE reproduction, including the training data, hyperparameters, and evaluation protocol.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of writing
- **Affected element** Results section, "PNABPred improves the accuracy of protein-nucleic acid binding prediction"
- **Evidence pointer** Location not provided
- **Issue** The sentence "These results suggest that PNABPred can capture binding features in primary protein sequence relevant to nucleic acid binding more effectively than a geometric model relying on imperfect or noisy predicted structures" is a strong claim based on a single comparison with GraphNet using predicted structures. The wording implies a general conclusion but the evidence is limited to one dataset.
- **Required correction** Soften the claim or add qualifying language, such as "on the tested benchmark" or "in this comparison."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of reporting
- **Affected element** Methods, "Multi-modal feature representation"
- **Evidence pointer** Location not provided
- **Issue** The description of the Atchley factors and BLOSUM50 embedding procedures is brief. It is not clear how the 5-dimensional Atchley vector is projected to 512 dimensions, what the exact architecture of the intra-modal refinement layers is, or how the three feature streams are concatenated and fed into the backbone. The hyperparameter table (Table S10) is not available.
- **Required correction** Provide more detail on the feature projection and refinement architecture, or ensure the supplemental information is accessible to reviewers.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 3C-F
- **Evidence pointer** Figure 3C-F
- **Issue** The t-SNE visualizations are described as showing "distinct, well-separated clusters" but the figure is not available for inspection. The claim of clear separation is subjective without seeing the plots.
- **Required correction** Ensure the figure is of sufficient quality and resolution to support the claim, or provide quantitative measures of cluster separation (e.g., silhouette score).

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** Location not provided
- **Issue** The term "semantic representations" is used to describe ESM-2 embeddings. This is potentially confusing, as "semantic" in the context of protein language models is not universally defined. The authors should clarify what they mean by "semantic" in this context.
- **Required correction** Define the term or use a more neutral descriptor such as "contextual embeddings from ESM-2."

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "Training procedure"
- **Evidence pointer** Location not provided
- **Issue** The training procedure states that the model was trained on an NVIDIA A100 GPU, but no information is given on training time, number of parameters, or computational cost. This information is useful for readers considering using the method.
- **Required correction** Add a brief statement on computational requirements, including approximate training time and model size.

## Risk / unsupported claims
- The claim that PNABPred "outperforms other state-of-the-art sequence-based methods" is based on comparisons with literature-reported values for most baselines, which may not be directly comparable. This is a significant limitation that is not adequately discussed.
- The claim that PNABPred can handle intrinsically disordered regions is supported only by a single case study and is not systematically evaluated.
- The statistical significance claim (p < 0.05) is not fully supported by the described methodology, as the details of the testing procedure are incomplete.
- The claim that the multi-modal feature fusion strategy is "novel" is not clearly established relative to existing multi-feature approaches in the literature.
- The performance improvements from adding biophysical and evolutionary features, while reported as significant in ablation studies, are not accompanied by confidence intervals or effect sizes, making the magnitude of the improvement unclear.
- The generalization experiments are described but the actual results are not presented in the main text, making the claim of superior generalization unverifiable from the provided material.