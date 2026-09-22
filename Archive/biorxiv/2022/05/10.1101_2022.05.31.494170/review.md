## Review setup

- **Input scope** Full manuscript text (preprint, bioRxiv, 2022)
- **Assessment boundary** Scientific and technical evaluation of the reported method, experiments, and claims, based solely on the provided manuscript text
- **Shared manuscript claim summary** The authors propose STEP, a Siamese neural network using ProtBERT deep protein sequence embeddings, to predict virus-host protein-protein interactions from primary sequences alone. They report state-of-the-art performance on multiple public datasets and apply the model to predict interactions for JCV VP1 and SARS-CoV-2 spike protein, with biological interpretations supported by literature and Explainable AI analyses.
- **Visible evidence base** Main text including Summary, Introduction, Experimental procedures (partial), Resource availability, Results (partial), Conclusion, Author Contributions, Conflict of Interests, Acknowledgements. Referenced supplementary materials and figures are mentioned but not provided.
- **Missing materials affecting confidence** Full methods section, all figures (Figure 1, 2, S1, S2, S4, S5, S6), all tables (Table 1, 2, 3, S1, S3, S4, S5, S6, S7, S8, S11, S12, S13), supplementary files (S1, S2, S3, S4), and code repository contents. These are essential for verifying methodology, results, and reproducibility.

## Reviewer

- **Overall assessment** The manuscript addresses a relevant problem in virus-host interaction prediction and proposes a reasonable deep learning architecture combining ProtBERT embeddings with a Siamese network. The application to two clinically relevant viruses and the use of Explainable AI are commendable. However, the provided text lacks critical methodological details and all supporting data, making it impossible to verify the core claims of state-of-the-art performance and biological relevance. The evaluation design, particularly the use of pseudo-negatives and the comparison to existing methods, raises concerns that need clarification. The manuscript is potentially interesting but currently not established from the provided evidence.
- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein-protein interaction prediction, virus-host interaction modeling, and applications of protein language models. Researchers studying JCV and SARS-CoV-2 pathogenesis may also find the predicted interactions and their biological interpretations relevant for hypothesis generation. The work could interest those developing therapeutic strategies involving virus-like particles or targeting viral entry mechanisms.
- **Major strengths** The use of a modern, pre-trained protein language model (ProtBERT) within a Siamese architecture is a sensible and timely approach. The application to two distinct and clinically important viruses demonstrates practical utility. The inclusion of Explainable AI to interpret predictions is a valuable addition that addresses the black-box criticism of deep learning. The authors make their code publicly available, supporting reproducibility.
- **Major Concerns** The concerns are listed below.
- **Minor Comments** The minor comments are listed below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5
- **Assessment against Nature-style criteria** Originality: The combination of ProtBERT with a Siamese network for virus-host PPI prediction is a novel contribution, though the individual components are established. Scientific importance: The problem is important, and the potential for new biological insights is high, but the current evidence does not fully establish the method's reliability or the validity of the predictions. Interdisciplinary readership: The topic bridges virology, bioinformatics, and machine learning, which could appeal to a broad audience, but the technical presentation may be challenging for non-specialists. Technical soundness: The core idea is sound, but the provided text lacks sufficient detail to assess the implementation, evaluation, and statistical rigor. Readability for nonspecialists: The abstract and summary are accessible, but the results and methods sections assume significant domain expertise. Overall, the manuscript has potential but requires substantial revision and additional evidence to meet the standards of a high-impact journal.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript addresses a relevant problem with a plausible approach, but the missing methods, data, and figures prevent verification of the central claims. I would be supportive if the technical concerns are resolved with a complete and rigorous revision.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that STEP achieves "state-of-the-art performance" and "high prediction performance" on multiple datasets, including comparisons to existing methods.
- **Evidence pointer** Results section, Table 1, Table S4, location not provided
- **Concern** The results section reports performance metrics but the actual values, the specific datasets used, and the details of the comparison are not fully described in the provided text. The claim of state-of-the-art performance cannot be evaluated without seeing the numerical results, the baselines, and the statistical significance of any differences. Furthermore, the use of pseudo-negatives generated by random sampling is a critical methodological choice. The authors acknowledge that this can lead to overoptimistic performance, but they do not provide any analysis of how this affects their reported results or how it compares to the dissimilarity-based sampling used by the competing method (Tsukiyama et al.). Without this information, the reported performance may not reflect real-world applicability.
- **Why it matters** The central claim of the paper is that STEP outperforms existing methods. If this claim is not rigorously supported with transparent and appropriate evaluation, the contribution of the work is significantly diminished. The choice of negative sampling strategy directly impacts the validity of the performance metrics and the model's ability to generalize to unseen, real virus-host interactions.
- **Resolution test** Provide the full results tables with all performance metrics (AUC, AUPR, and others) for all datasets and all compared methods. Include a detailed description of the datasets, the number of positive and negative samples, and the exact protocol for generating pseudo-negatives. Conduct and report statistical significance tests (e.g., confidence intervals, p-values) for the performance differences. Discuss the potential bias introduced by random negative sampling and, ideally, provide a comparison using a more realistic negative sampling strategy.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that their method can predict interactions for JCV VP1 and SARS-CoV-2 spike protein, and that these predictions are biologically relevant and supported by literature.
- **Evidence pointer** Results section, Tables 2, S11-S13, Figures S2, S4, S5, S6, location not provided
- **Concern** The biological validation of the predicted interactions is presented as a key outcome, but the provided text only offers a brief narrative summary. The actual predicted interaction lists, the scores, and the enrichment analyses are not shown. The claim that the predictions are "in line with the current literature" is not substantiated with specific evidence or a systematic comparison. For example, the prediction of sigma receptor 2 interaction with SARS-CoV-2 spike is interesting, but the text does not provide the full list of predictions, the ranking, or how this prediction was selected from potentially many others. The enrichment analyses (GO, InterPro) are mentioned but the results are not presented. Without this data, it is impossible to assess the biological plausibility and significance of the findings.
- **Why it matters** The paper's impact relies on demonstrating that the model can generate novel, testable hypotheses. If the biological interpretation is not rigorously supported with data, the claims remain anecdotal and the practical value of the method is unclear.
- **Resolution test** Provide the full tables of predicted interactions with scores for all viruses and receptors. Show the results of the GO and InterPro enrichment analyses, including the statistical significance and the list of enriched terms. For the key predictions (e.g., sigma receptor 2), provide a more detailed discussion of the supporting literature and any additional evidence that strengthens the claim.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that they used a "Siamese Tailored deep sequence Embedding of Proteins" architecture and performed "extensive Bayesian hyperparameter optimization."
- **Evidence pointer** Experimental procedures, Architecture and Transfer Learning of STEP, Supplementary Tables S1, S3, S5, S8, location not provided
- **Concern** The description of the model architecture and training procedure is incomplete. The text mentions ProtBERT, a Hadamard product integration layer, and a bottleneck classification head, but lacks critical details such as the exact number of layers, hidden dimensions, dropout rates, learning rates, batch sizes, and the optimization algorithm. The hyperparameter optimization is mentioned but the search space, the number of trials, and the criteria for selecting the best model are not described. The details of the train/validation/test splits for each dataset are also missing. This level of detail is essential for reproducibility and for assessing the soundness of the methodology.
- **Why it matters** Without a complete description of the model and training process, other researchers cannot replicate the work or build upon it. The lack of detail also makes it difficult to identify potential sources of bias or overfitting in the model development.
- **Resolution test** Provide a complete and detailed description of the model architecture, including all hyperparameters and the training procedure. Describe the hyperparameter optimization process, including the search space, the number of trials, and the selection criteria. Clearly specify the data splits for all datasets and the exact number of samples in each set.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the Explainable AI (XAI) analysis using integrated gradients can identify parts of sequences that contribute to predictions.
- **Evidence pointer** Making STEP Models Explainable, Figures S4, S6, location not provided
- **Concern** The XAI analysis is presented as a way to interpret model predictions, but the results are not shown or described in detail. The text mentions that "large parts of the VP1 sequence contribute" and that specific domains in the sigma receptor have positive or negative contributions, but the actual figures and a detailed interpretation are missing. It is unclear how the integrated gradients were aggregated across the sequence, how the baseline was chosen, and how the results were validated. The claim that the XAI analysis provides meaningful biological insights is not supported by the evidence presented.
- **Why it matters** The XAI component is a claimed contribution of the paper. If the analysis is not clearly presented and validated, its value is questionable. The interpretation of which sequence parts are important is a key part of the biological narrative and needs to be rigorously demonstrated.
- **Resolution test** Show the integrated gradients results for the key predictions, with clear visualizations and a detailed explanation of the patterns observed. Describe the methodology for aggregating gradients and the choice of baseline. Provide a validation of the XAI results, for example, by comparing them to known functional domains or mutational data.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The authors state that the data and source code are available at a GitHub repository.
- **Evidence pointer** Resource availability, location not provided
- **Concern** The manuscript states that the code is available, but the repository contents are not described. It is unclear if the code includes the trained models, the scripts for data processing, the hyperparameter optimization, and the XAI analysis. The availability of the data is also ambiguous, as some datasets are from public sources but the processed versions used in this study are not described. Without a clear description of the repository and the data, the reproducibility of the work is in question.
- **Why it matters** Reproducibility is a core requirement for scientific progress. The authors' claim of public availability is not sufficient without a clear description of what is available and how to use it.
- **Resolution test** Provide a detailed description of the GitHub repository, including the structure, the main scripts, the dependencies, and the instructions for reproducing the results. Clearly state which datasets are included and how they were processed. Ensure that the code is well-documented and can be run by an independent researcher.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract and Summary
- **Evidence pointer** Summary, location not provided
- **Issue** The Summary and Abstract are somewhat repetitive and could be more concise. The phrase "high prediction performance" is used without specific numbers, which is vague.
- **Required correction** Consider providing a specific performance metric (e.g., AUC) in the abstract to give readers a concrete sense of the results. Streamline the Summary to avoid redundancy.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Introduction
- **Evidence pointer** Introduction, location not provided
- **Issue** The Introduction is well-written but could benefit from a clearer statement of the limitations of existing methods and how STEP specifically addresses them. The novelty of using ProtBERT over other embeddings is mentioned but not deeply discussed.
- **Required correction** Add a brief paragraph explicitly contrasting the limitations of existing sequence-based methods (e.g., handcrafted features, older embeddings) with the advantages of using a large pre-trained model like ProtBERT.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, JCV prediction section
- **Evidence pointer** Results, location not provided
- **Issue** The description of the JCV prediction results is brief. The text mentions an enrichment of neurotransmitter receptors but does not provide the specific enriched terms or the p-values.
- **Required correction** Include a summary of the top enriched GO terms and their adjusted p-values in the main text or refer more explicitly to the supplementary tables.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, SARS-CoV-2 prediction section
- **Evidence pointer** Results, location not provided
- **Issue** The claim that the sigma receptor 2 interaction is "outstanding" is subjective. It is unclear how this prediction was selected from the full list and what the scores for other receptors were.
- **Required correction** Provide the distribution of prediction scores for all receptors and explain the criteria for highlighting this specific interaction.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figures and Tables
- **Evidence pointer** All figures and tables, location not provided
- **Issue** The manuscript refers to several figures and tables that are not included in the provided text. This makes it impossible to follow the results.
- **Required correction** Ensure that all figures and tables are included in the final submission and are properly referenced in the text.

## Risk / unsupported claims

- The claim of "state-of-the-art performance" is unsupported without the full results tables and statistical analysis.
- The claim that predicted interactions are "biologically relevant" and "in line with the literature" is unsupported without the detailed results of the enrichment analyses and a systematic comparison to known interactions.
- The claim that the XAI analysis identifies "parts of sequences that most likely contribute" is unsupported without the actual XAI results and a validation of the method.
- The claim that the model can be "easily trained to predict interactions of other viruses" is plausible but not demonstrated in the provided text.
- The statement that the observed antiviral effect of sigma receptor ligands "might be due to a modulated binding of the spike protein" is highly speculative and not directly supported by the model's predictions or any experimental evidence.