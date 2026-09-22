## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors propose PULPS, a positive unlabeled (PU) learning framework combining ProbTagging and penalty logistic regression (PLR) with hybrid multimodal features, to predict scaffold proteins driving liquid-liquid phase separation (LLPS) in the human proteome. They report an AUC of 0.8353, an area under the lift curve (AUL) of 0.8339, a partial recovery with 2.85% AUL increase to 0.8577, a 45.7% AUL improvement over PLR, and an 8.2% superiority over existing tools. They claim this is the first demonstration that PU learning is more suitable for scaffold prediction and that the profile reveals widespread phase separation states and potential scaffolds.
- **Visible evidence base** Abstract text only; no methodological details, dataset descriptions, baseline specifications, or numerical results beyond those stated
- **Missing materials affecting confidence** Full manuscript, all figures and tables, supplementary data, detailed feature definitions, training and test set compositions, baseline tool names and versions, statistical significance tests, and code or web server validation

## Reviewer
- **Overall assessment** The abstract presents a potentially useful application of PU learning to a biologically relevant prediction problem. However, the evidence provided is insufficient to evaluate the validity of the core claims. Key methodological details, dataset characteristics, and comparative baselines are not described. The reported performance metrics, while plausible, cannot be assessed for robustness or significance without access to the full methods and results. The claim of being the first to show PU learning suitability for scaffold prediction is strong and requires careful contextualization against existing literature, which is not provided.
- **Who would be interested in the results, and why** Researchers in computational biology and bioinformatics focused on protein function prediction, particularly those studying phase separation and biomolecular condensates. Experimental biologists studying LLPS may also find the predicted scaffold candidates useful for prioritization. Methodologists interested in PU learning applications to imbalanced biological datasets could be interested in the framework.
- **Major strengths** The problem is well motivated, addressing a gap in scaffold-specific predictors. The use of PU learning to handle the extreme label imbalance is conceptually appropriate. The reported partial recovery with recent experimental data suggests some practical utility. The provision of a free web server is a positive contribution to the community.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The framework achieves an AUC of 0.8353 and an AUL of 0.8339, with a 45.7% improvement in AUL over PLR and 8.2% superiority over other tools.
  - **Evidence pointer** Abstract, performance metrics section; location not provided
  - **Concern** The abstract does not describe the dataset composition, including the number of positive scaffolds, the number of unlabeled candidates, the source of negative examples (if any), or the feature set used. Without this information, the reported AUC and AUL cannot be interpreted. The improvement over PLR and other tools is stated without naming the baselines, their configurations, or the statistical significance of the differences.
  - **Why it matters** Performance metrics are only meaningful in the context of the data and baselines. If the positive set is very small or the unlabeled set is not representative, the reported numbers may not generalize. The lack of baseline details prevents readers from judging whether the comparison is fair.
  - **Resolution test** Provide a detailed description of the dataset, including positive and unlabeled set sizes, feature types, and the exact baselines used. Report confidence intervals or significance tests for the AUC and AUL differences.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Scientific importance
  - **Claim pointer** The study first proved that PU learning is more suitable for scaffold prediction and demonstrated the widespread existence of phase separation states.
  - **Evidence pointer** Abstract, concluding claims; location not provided
  - **Concern** The claim of being the first to prove PU learning suitability is a strong novelty statement that requires a thorough literature review to support. The abstract does not mention any prior PU learning applications to LLPS or scaffold prediction, nor does it discuss why PU learning would be theoretically preferred over other approaches. The claim of widespread phase separation states is vague and not tied to any specific quantitative result.
  - **Why it matters** Novelty claims are central to the paper's contribution. If prior work has already applied PU learning to similar problems, the claim is overstated. The biological conclusion about widespread phase separation states needs a clear definition and supporting evidence.
  - **Resolution test** Cite and discuss prior PU learning applications in related prediction tasks. Define what is meant by widespread phase separation states and provide specific evidence, such as the number of predicted scaffolds or enrichment analyses.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The partial recovery with recent experimentally verified scaffolds showed a 2.85% increase in AUL from 0.8339 to 0.8577.
  - **Evidence pointer** Abstract, partial recovery statement; location not provided
  - **Concern** The partial recovery procedure is not described. It is unclear how recent scaffolds were selected, how they were incorporated into the evaluation, and whether this recovery is a validation or a re-training step. The 2.85% increase is small and may not be statistically meaningful.
  - **Why it matters** If the recovery involves updating the model with new positives, the AUL increase may reflect overfitting to the new data rather than genuine predictive improvement. The evaluation protocol must be clear to interpret this result.
  - **Resolution test** Describe the partial recovery protocol in detail, including the selection criteria for recent scaffolds and whether the model was retrained. Report significance testing for the AUL change.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Abstract, methods description
  - **Evidence pointer** Abstract, framework description; location not provided
  - **Issue** The terms ProbTagging and penalty logistic regression are introduced without explanation. Nonspecialist readers may not understand what these methods do or why they are combined.
  - **Required correction** Provide a brief explanation of ProbTagging and PLR in the abstract or refer to a methods section with clear definitions.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Interdisciplinary readership
  - **Affected element** Abstract, biological claims
  - **Evidence pointer** Abstract, concluding claims; location not provided
  - **Issue** The claim that the profile uncovered potential scaffolds that co-drive LLPS is not quantified. No number of predicted scaffolds or examples are given.
  - **Required correction** State the number of predicted scaffolds or provide a representative example to make the claim concrete.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Abstract, performance metrics
  - **Evidence pointer** Abstract, performance metrics section; location not provided
  - **Issue** The AUL is described as an estimation of true performance, but the abstract does not explain why AUL is preferred over other metrics like precision-recall AUC, which is common for imbalanced problems.
  - **Required correction** Justify the choice of AUL as the primary metric and report additional metrics such as precision, recall, or F1 score.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3. The lack of dataset and baseline details, the unsupported novelty claim, and the unclear partial recovery protocol collectively prevent the core claims from being evaluated.

## Risk / unsupported claims
- The claim that PU learning is more suitable for scaffold prediction is unsupported without a literature comparison and theoretical justification.
- The claim of widespread existence of phase separation states is unsupported without a clear definition and quantitative evidence.
- The reported performance improvements over PLR and other tools are unverifiable without baseline names and significance testing.
- The partial recovery result is uninterpretable without a description of the protocol.
- The generalizability of the framework to the human proteome is not assessable from the abstract alone.

## Assessment against Nature-style criteria
- **Originality** The application of PU learning to scaffold prediction appears novel, but the abstract does not provide enough context to confirm this. The claim of being first is not substantiated.
- **Scientific importance** The problem is important, and a reliable scaffold predictor would be valuable. However, the biological conclusions are vague and not tied to specific findings.
- **Interdisciplinary readership** The work bridges computational methods and cell biology, which could attract a broad audience. The abstract is accessible but lacks methodological clarity for nonspecialists.
- **Technical soundness** The core technical claims cannot be assessed due to missing dataset, baseline, and protocol details. The reported metrics are not contextualized.
- **Readability for nonspecialists** The abstract is generally readable but introduces technical terms without explanation and makes broad claims without quantification.

## Recommendation posture
Currently not established from the provided evidence. The abstract suggests a potentially useful framework, but the lack of methodological detail, baseline information, and statistical validation means the core claims cannot be verified. A revised version with full methods, dataset descriptions, and significance testing would be needed to assess whether the case is established.