## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion, supporting information references)
- **Assessment boundary** Scientific and technical evaluation of the presented methodology, experimental design, results, and claims; no editorial or formatting review
- **Shared manuscript claim summary** The authors propose IDP-LM, a computational predictor that uses embeddings from three pre-trained protein language models (ProtBERT, ProtT5, and a disorder-specific model IDP-BERT) as exclusive inputs to predict protein intrinsic disorder and four disorder functions (protein binding, DNA binding, RNA binding, flexible linkers). They claim that IDP-BERT provides fine-grained disorder features, that the combination of the three language models improves performance, and that transfer learning from the disorder predictor reduces false positives in disorder function prediction. They report competitive or superior performance on CAID and TE176 test datasets.
- **Visible evidence base** Full text including methods, results tables (Tables 1–8), figures (Figs 1–7), supporting information references (S1–S11 Tables, S1 Fig), dataset descriptions, and model architecture details
- **Missing materials affecting confidence** Actual data values in Tables 1–8 and Figures 3–7 are not visible in the provided text; supporting information files (S1–S11 Tables, S1 Fig) are referenced but not provided; no supplementary code or model weights were reviewed; no details on baseline method implementations or hyperparameter tuning for comparative methods

## Reviewer
- **Overall assessment** The manuscript presents a reasonable and timely application of protein language models to the prediction of intrinsic disorder and disorder functions. The core idea of combining general-purpose language models with a disorder-specific pre-trained model is sensible, and the transfer learning strategy for function prediction is well motivated. However, the evidence base available for this review is incomplete, as the actual numerical results in tables and figures are not visible. The methodological description is adequate but lacks some critical details regarding dataset construction, class imbalance handling, and statistical significance testing. The claims of superiority over existing methods cannot be fully verified from the provided material. The work is likely of interest to the computational biology community, but the case for broad significance and novelty relative to existing disorder predictors needs to be strengthened with more rigorous comparisons and accessible presentation of results.

- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein structure and function prediction, particularly those interested in intrinsically disordered proteins and regions. Researchers developing or applying protein language models for downstream prediction tasks would also find the methodology relevant. The disorder function prediction component may interest experimental biologists studying IDP-related diseases, though the practical utility for this group would depend on the availability and usability of the stand-alone package.

- **Major strengths**
  1. The use of a disorder-specific pre-trained language model (IDP-BERT) trained with a restrictive masked language modeling objective is a novel contribution that is well motivated by the known positional bias of disorder toward sequence termini.
  2. The transfer learning approach from disorder prediction to disorder function prediction is conceptually elegant and addresses the scarcity of functionally annotated disordered sequences.
  3. The evaluation follows established community benchmarks (CAID) and includes multiple complementary metrics (AUC, Fmax, MCC, BAC), which strengthens the credibility of the reported performance.
  4. The authors provide both source code and a stand-alone package, which is commendable for reproducibility and practical adoption.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that IDP-LM "performed best among comparable methods for all four common disordered functions" and "significantly outperformed other comparative predictors" on disorder binding prediction.
- **Evidence pointer** Tables 4–8, Figure 7; location not provided for actual values
- **Concern** The actual numerical results in Tables 4–8 and Figure 7 are not visible in the provided manuscript text. Without these values, the central performance claims cannot be assessed. Furthermore, the text does not report confidence intervals, statistical significance tests (e.g., DeLong test for AUC differences), or effect sizes for the claimed improvements over baseline methods. The statement "significantly outperformed" implies statistical testing, but no such tests are described in the Methods section.
- **Why it matters** The primary contribution of this work is the claimed performance improvement over existing methods. If the numerical evidence is not presented or the improvements are not statistically validated, the central case for the method's utility is not established.
- **Resolution test** Provide the actual values from Tables 4–8 and Figure 7, and include statistical significance testing (e.g., paired bootstrap or DeLong test) comparing IDP-LM to the best-performing baseline for each disorder function. Report confidence intervals for the primary metrics.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that the training and validation sets were filtered to remove sequences sharing greater than 25% sequence similarity to the test sets, and that the resulting training set contains 412 sequences and validation set 90 sequences.
- **Evidence pointer** Materials and Methods, Datasets section; location not provided
- **Concern** The manuscript does not describe the sequence similarity filtering procedure in sufficient detail. Specifically, it is unclear (a) whether the 25% threshold was applied at the residue level or using a specific alignment tool other than PSI-BLAST, (b) whether the filtering was performed against both test sets simultaneously, and (c) how the final training set of only 412 sequences was derived from the initial collection. A training set of 412 sequences is very small for fine-tuning a model with multiple Bi-LSTM layers, raising concerns about overfitting and generalizability. Additionally, the validation set of 90 sequences is small for reliable hyperparameter selection, particularly for the genetic algorithm used to optimize fusion weights.
- **Why it matters** The reliability of the reported performance depends critically on the absence of test set contamination and on the adequacy of the training data. Insufficient filtering or an undersized training set could lead to inflated performance estimates or poor generalization to new sequences.
- **Resolution test** Provide a detailed description of the filtering pipeline, including the exact tool and parameters used, the order of operations, and the number of sequences removed at each step. Report the distribution of sequence lengths and disorder content in the final training and validation sets. Consider evaluating whether the model performance is stable when trained on different random splits of the available data.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that IDP-BERT, trained with a restrictive masked language model (ReMLM) objective that focuses masking on terminal regions, provides "fine-grained feature representations of disorder" and that its combination with ProtBERT and ProtT5 is "the key to the performance improvement."
- **Evidence pointer** Figure 4, S7 and S11 Tables; location not provided
- **Concern** The ablation analysis is described only qualitatively. The text states that IDP-BERT achieves higher true positive rates and that statistical differences exist among the three language models, but the actual ablation results (e.g., performance of each single model, pairwise combinations, and the full combination) are not presented in the visible text. The claim that the combination is "the key" to improvement requires a systematic ablation study showing the marginal contribution of each component. Additionally, the ReMLM objective is compared only against the full combination, not against a standard masked language model trained on the same disorder-specific data, so the specific benefit of the restrictive masking strategy is not isolated.
- **Why it matters** The novelty of the method rests substantially on the IDP-BERT component and the ReMLM training strategy. Without a clear ablation showing that this component adds value beyond the general-purpose language models, the contribution of the work is diminished.
- **Resolution test** Present a full ablation table showing performance (AUC, Fmax, MCC, BAC) for each individual language model, each pairwise combination, and the full three-model combination. Additionally, compare IDP-BERT against a version trained with standard (non-restrictive) masked language modeling on the same data to isolate the effect of the ReMLM strategy.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The authors state that IDP-LM uses embeddings from three pre-trained language models as "exclusive inputs" and that the prediction layers use Bi-LSTM networks with weights optimized by a genetic algorithm.
- **Evidence pointer** Materials and Methods, IDP-LM for disorder prediction; location not provided
- **Concern** The manuscript does not specify several critical implementation details: (a) the dimensionality of the embeddings extracted from each language model, (b) whether embeddings are concatenated or averaged, (c) the number of Bi-LSTM layers and hidden units, (d) the training procedure for the prediction layers (e.g., learning rate, batch size, number of epochs, early stopping criteria), (e) the genetic algorithm parameters (population size, number of generations, crossover and mutation rates), and (f) how the final threshold for binary classification was selected. Without these details, the method cannot be reproduced by other researchers.
- **Why it matters** Reproducibility is a core requirement for computational biology methods. The absence of these details limits the utility of the released code and prevents independent verification of the results.
- **Resolution test** Provide a complete description of all model architecture and training hyperparameters, either in the main text or in the supplementary materials. If the code is available, ensure it is documented sufficiently to allow reproduction of all reported results.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors state that "the IDP-LM predictor achieved significantly outstanding results than other predictors in all evaluation metrics" for disorder binding prediction, and that IDP-LM "performed best among comparable methods for all four common disordered functions."
- **Evidence pointer** Tables 4–8; location not provided
- **Concern** The comparison with existing methods appears to be limited to a small set of baselines. For disorder binding prediction, the comparison set is not fully described. For disorder function prediction, only fIDPnn is mentioned as providing all four function predictions. It is unclear whether other recent disorder function predictors (e.g., flDPnn, MFSPSSMpred, DisoRDPbind) were included in the comparison. A limited baseline set weakens the claim of state-of-the-art performance.
- **Why it matters** The scientific importance of the work depends on demonstrating clear advantages over the current state of the art. If key existing methods are omitted from the comparison, the claims of superiority are not fully supported.
- **Resolution test** Expand the baseline comparison to include all recently published disorder function predictors with available implementations or published results on the same test sets. Justify the selection of baselines and report results for all methods under identical evaluation conditions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1 description
- **Evidence pointer** Figure 1; location not provided
- **Issue** The overview figure is referenced but not described in sufficient detail in the text. The relationship between the three language model branches and the fusion mechanism is not clearly explained in the figure legend or the text.
- **Required correction** Provide a more detailed figure legend that explains each component of the architecture, including the embedding extraction, Bi-LSTM layers, weight fusion, and output layers.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Correlation analysis
- **Evidence pointer** S5 Table; location not provided
- **Issue** The Pearson correlation coefficient between IDP-LM disorder propensity scores and AlphaFold2 pLDDT is reported as r = -0.307, but no confidence interval or p-value is provided. The interpretation of this correlation is also not discussed.
- **Required correction** Report the p-value and confidence interval for the correlation, and add a brief interpretation of what this correlation means for the relationship between predicted disorder and predicted structural confidence.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Dataset description
- **Evidence pointer** Materials and Methods, Datasets section; S1 Table
- **Issue** The description of the disorder function datasets is deferred to S1 Table, which is not provided. The main text does not state the number of proteins or residues in each function category, nor the class distribution.
- **Required correction** Include a brief summary of the dataset sizes and class distributions in the main text, and ensure S1 Table is complete and self-explanatory.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Code availability
- **Evidence pointer** Conclusion section
- **Issue** The authors state that source code is available at GitHub and a stand-alone package at a lab website, but no version information, license, or usage instructions are provided in the manuscript.
- **Required correction** Add a brief statement about the software license, supported platforms, and basic usage instructions, or refer to a documentation page.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Language precision
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, Introduction; location not provided
- **Issue** The phrase "disorder functions" is used throughout but is not formally defined. The distinction between "disorder functions" and "disorder binding" is not always clear.
- **Required correction** Define "disorder functions" explicitly in the Introduction and use consistent terminology throughout the manuscript.

## Risk / unsupported claims
- The claim that IDP-LM "significantly outperformed" other predictors cannot be assessed without the actual numerical results and statistical testing, which are not visible in the provided material.
- The claim that the combination of three language models is "the key to the performance improvement" is not supported by a visible systematic ablation study.
- The claim that IDP-BERT provides "fine-grained feature representations of disorder" is based on qualitative visual inspection of t-SNE plots and PBC scores, but the statistical significance of these observations is not reported.
- The claim of competitive performance on CAID benchmarks cannot be verified without the actual values in Tables 1–3 and Figures 5–6.
- The generalizability of the method beyond the specific test sets used is not established, given the small training set size (412 sequences).
- The practical utility of the stand-alone package for non-expert users is not demonstrated.