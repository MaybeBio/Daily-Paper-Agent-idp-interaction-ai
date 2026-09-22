## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors present pLMMoRF, a sequence-based web server that predicts membrane-interacting molecular recognition features (MemMoRFs) in intrinsically disordered regions. The predictor uses an Ankh-based protein language model with feature selection feeding a deep convolutional neural network. The authors claim higher accuracy than the existing predictor CoMemMoRFPred on low similarity test datasets, a relatively small computational footprint, and availability of human proteome predictions.
- **Visible evidence base** Abstract text only; no quantitative performance metrics, dataset descriptions, or validation details are provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, dataset construction details, benchmark protocols, statistical significance tests, web server implementation details, and human proteome prediction analysis

## Reviewer
- **Overall assessment** The abstract describes a potentially useful bioinformatics tool for predicting lipid-interacting regions in disordered proteins. The methodological approach, combining a protein language model with feature selection and a convolutional neural network, is reasonable and timely. However, the abstract provides no quantitative evidence to support the central claims of accuracy, speed, or utility. The comparison to CoMemMoRFPred is mentioned but not substantiated with any metrics. The human proteome analysis is described but no findings are summarized. The work may be of interest to the membrane protein and intrinsically disordered protein communities, but the case is not established from the abstract alone.
- **Who would be interested in the results, and why** Researchers studying membrane protein interactions, intrinsically disordered regions, and protein lipid binding. Computational biologists developing sequence-based predictors for protein function. Experimentalists seeking to prioritize candidate MemMoRFs for validation. The human proteome predictions could be of broad interest to cell biologists studying membrane associated processes.
- **Major strengths** The problem is biologically relevant and experimentally challenging. The use of a protein language model is current and appropriate. The explicit consideration of multiple pLMs and feature selection to reduce model complexity is a thoughtful design choice. The provision of a web server and public predictions is a practical contribution. The focus on computational efficiency is commendable.
- **Major Concerns** None can be fully assessed from the abstract alone, but the absence of any quantitative results is a significant limitation for evaluation.
- **Minor Comments** None can be assessed from the abstract alone.
- **Technical failings that need to be addressed before the case is established** No quantitative performance data are provided. The claim of higher accuracy than CoMemMoRFPred is unsupported. The computational footprint claim is unquantified. The human proteome analysis is not summarized.
- **Assessment against Nature-style criteria** Originality: moderate. The application of pLMs to MemMoRF prediction is novel but builds on established methods. Scientific importance: moderate. The tool addresses a real need but the biological impact is not demonstrated in the abstract. Interdisciplinary readership: limited. The abstract is written for a specialist computational biology audience. Technical soundness: not assessable from the abstract. Readability for nonspecialists: the abstract is clear but assumes familiarity with pLMs and IDR terminology.
- **Recommendation posture** Currently not established from the provided evidence. The abstract describes a plausible and potentially valuable tool, but without quantitative results, the central claims cannot be evaluated.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that pLMMoRF is more accurate than CoMemMoRFPred on low similarity test datasets.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract states that pLMMoRF outperforms CoMemMoRFPred but provides no performance metrics, such as AUC, precision, recall, or F1 score. No statistical significance is reported. The size and composition of the test datasets are not described.
- **Why it matters** The central claim of the paper is the improved predictive accuracy of pLMMoRF. Without quantitative evidence, the reader cannot assess whether the improvement is meaningful or statistically robust. This claim is the primary justification for the tool's existence.
- **Resolution test** Provide performance metrics for pLMMoRF and CoMemMoRFPred on the same low similarity test datasets, including confidence intervals or statistical tests. Describe the dataset construction and sequence identity thresholds.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that pLMMoRF has a relatively small computational footprint due to compact network size and use of dedicated GPU nodes.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract mentions computational efficiency but provides no quantitative data, such as inference time, memory usage, or model parameter count. The comparison baseline for "small" is not defined.
- **Why it matters** Computational efficiency is presented as a key advantage enabling human proteome predictions. Without quantification, this claim cannot be verified, and the practical utility of the tool for large scale applications remains unclear.
- **Resolution test** Report model size in parameters, inference time per sequence, and total runtime for the human proteome prediction. Compare these metrics to CoMemMoRFPred or other relevant baselines.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors state that they analyzed human proteome predictions and made them publicly available, facilitating improved understanding of membrane coupled protein functions.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract does not summarize any findings from the human proteome analysis. No biological insights, enrichment patterns, or functional correlations are mentioned.
- **Why it matters** The human proteome analysis is presented as a significant outcome of the work. Without any description of the results, the reader cannot judge whether the predictions provide novel biological information or are merely a technical exercise.
- **Resolution test** Summarize key findings from the human proteome analysis, such as the number of predicted MemMoRFs, their distribution across protein families, or functional enrichment results.

### Minor Comments

None identified from the supplied material.

## Risk / unsupported claims
- The claim of higher accuracy than CoMemMoRFPred is unsupported by any quantitative data.
- The claim of a relatively small computational footprint is unquantified.
- The claim that human proteome predictions facilitate improved understanding is not substantiated with any analysis summary.
- The general statement that feature selection enhances predictive performance and reduces computational footprint is plausible but not demonstrated with comparative data in the abstract.