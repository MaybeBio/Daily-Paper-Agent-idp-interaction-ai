## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, data availability)
- **Assessment boundary** Scientific claims, methodological soundness, evidence quality, and reproducibility as presented in the supplied text
- **Shared manuscript claim summary** The authors present Seq2Bind, a webserver that fine-tunes four protein language models (ProtBERT, ProtT5, ESM2, BiLSTM) on SKEMPI 2.0 to predict binding affinity and identify interface residues from sequence alone. They report interface-residue recovery rates on 6,063 PDB dimers and benchmark against HADDOCK3 and five mutation predictors on 14 human health-relevant complexes.
- **Visible evidence base** Abstract, introduction, methods, results, discussion, data availability statements. No figures, tables, or supplementary materials were provided.
- **Missing materials affecting confidence** All figures (Figs 1-5), Table 1, Supplementary Figures S1-S9, Supplementary Table S1, and Supplementary Data files. These are referenced extensively and are essential for evaluating the reported quantitative results.

## Reviewer

- **Overall assessment** The manuscript addresses a relevant problem in protein-protein interaction prediction, namely the identification of binding residues from sequence without structural input. The idea of using fine-tuned PLMs for alanine-scanning-based interface detection is timely and of potential interest to a broad computational biology audience. However, the current text does not provide sufficient evidence to evaluate the central claims. All quantitative results are presented as references to figures and tables that were not supplied. The methods section contains inconsistencies in dataset numbers (6,063 vs 6,069 vs 6,087), and the evaluation protocol is described at a level of abstraction that prevents replication. The comparison against HADDOCK3 and mutation predictors is described but the actual data are not visible. The manuscript would benefit from a clearer articulation of what is genuinely novel relative to existing sequence-based PPI tools, and from a more critical discussion of the modest absolute recovery rates reported.

- **Who would be interested in the results, and why** Computational biologists working on protein-protein interaction prediction, drug discovery researchers interested in identifying binding hotspots from sequence, and developers of webservers for biological sequence analysis. The claim that sequence-based methods can rival docking-based interface prediction, if substantiated, would be of practical interest to researchers studying proteins without experimental structures, including disordered proteins and transmembrane proteins.

- **Major strengths**
  1. The problem is well motivated and practically relevant. The introduction clearly articulates the limitations of structure-based methods and the need for sequence-based alternatives.
  2. The use of multiple PLM architectures, including a BiLSTM baseline, provides a reasonable comparative framework.
  3. The N-factor evaluation metric is a sensible way to assess interface recovery under varying prediction scopes.
  4. The inclusion of an independent panel of 14 human health-relevant complexes for benchmarking against docking and mutation predictors is a good design choice.
  5. The webserver and Colab notebook are made publicly available, which supports reproducibility and community uptake.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The manuscript reports specific interface-residue recovery rates, e.g., "ESM2 achieved 67.4% and ProtBERT 68.2% interface-residue recovery at N-factor = 3" and "ESM (37.2%) and ProtBERT (35.1%) both yielded higher interface recovery rates than blind docking with HADDOCK3 (32.1%)" on the 14-complex benchmark.
- **Evidence pointer** Figures 3, 4, 5A; Table 1; Supplementary Figures S1-S9; Supplementary Table S1; location not provided
- **Concern** All quantitative results are presented only as references to figures and tables that were not included in the supplied material. The core claims of the paper, namely the recovery rates, the comparison against HADDOCK3, and the per-complex performance, cannot be verified from the text alone. Without the actual data, the reader cannot assess whether the reported differences are meaningful, whether error bars or confidence intervals are present, or whether the comparisons are fair.
- **Why it matters** The central contribution of the paper is empirical. If the data are not visible, the claims are not testable. This is a blocking issue for any assessment of the manuscript's validity.
- **Resolution test** Provide all figures and tables with clear axis labels, legends, and statistical annotations. Include per-complex results for the 14-complex benchmark and the full distribution of recovery rates across the 6,063 dimers.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The methods state: "We fine-tuned four different pre-trained architectures and subsequently queried the trained models to pinpoint key amino acids from each protein in a pair, which, when altered, compromises the binding strength." The training procedure is described as using SKEMPI 2.0, with 5,387 pairs after filtering.
- **Evidence pointer** Methods, Datasets section; location not provided
- **Concern** The description of the fine-tuning procedure is insufficient for replication. Key details are missing: the exact train/validation/test split, the hyperparameter search space, the number of epochs for each model, the learning rate schedules, the batch sizes, the optimizer used, and the criteria for early stopping. The loss functions tested are mentioned (MSE, MAE, Huber) but the final choice is not stated. The architecture of the regression head is described only as "three dropouts and linear layers" without specifying dimensions or dropout rates. The BiLSTM baseline is described with a "latent dimension of 10" but no other architectural details are given.
- **Why it matters** A central claim of the paper is that fine-tuned PLMs can predict binding affinity and interface residues. If the training procedure cannot be reproduced, the scientific contribution is severely weakened. The webserver and Colab are provided, but the underlying training code and hyperparameters are not described in sufficient detail.
- **Resolution test** Provide a complete description of the training protocol, including all hyperparameters, data splits, and the final loss function. Make the training code available in a public repository with clear documentation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Internal consistency
- **Claim pointer** The abstract states "6063 dimer proteins from Protein Data Bank" were used for evaluation. The introduction states "We analyzed 6069 heterodimers from Protein Data Bank." The methods state "The final corpus contained 7,620,872 per-residue predictions across 6063 PDBs."
- **Evidence pointer** Abstract, Introduction, Methods, Evaluation section; location not provided
- **Concern** The number of dimers used for evaluation is inconsistent across the manuscript: 6,063 in the abstract and methods, 6,069 in the introduction. This discrepancy is not explained. Additionally, the methods state that 5,387 pairs were used for training after filtering, but the relationship between the training set and the 6,063-complex evaluation set is not clarified. It is unclear whether the evaluation set overlaps with the training set, which would be a serious methodological flaw.
- **Why it matters** Inconsistent numbers undermine confidence in the rigor of the manuscript. If the evaluation set overlaps with the training set, the reported recovery rates would be inflated and the comparison against HADDOCK3 would be unfair.
- **Resolution test** Reconcile the numbers across the abstract, introduction, and methods. Clearly state the relationship between the training set and the evaluation set, and confirm that no evaluation complexes were used in training.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Methodological validity
- **Claim pointer** The manuscript states: "We iteratively altered amino acid types along the polypeptide backbones of both proteins in a pair to alanine (one at a time) to glean those residue positions which lead to highest drops in binding energy." The evaluation uses "N factor" where "N factor = 3 evaluates whether true residues appear within 3n top predictions for n-interface residues."
- **Evidence pointer** Methods, Evaluation section; location not provided
- **Concern** The evaluation protocol is described at a high level but several details are unclear. First, the definition of "true interface residues" is not stated. Is it based on a distance threshold in the PDB structure? If so, what threshold? Second, the N-factor metric as described appears to be a recall-based measure, but the authors do not report precision or any combined F-score. A method that predicts many residues trivially achieves high recall at large N. Third, the comparison against HADDOCK3 is described as "the number of native interaction residues that the top HADDOCK3 pose recovers," but it is unclear how this is normalized or whether it is directly comparable to the N-factor metric used for Seq2Bind.
- **Why it matters** The evaluation metric determines whether the reported results are meaningful. If the metric is biased toward methods that predict many residues, the comparison against HADDOCK3 and mutation predictors may be misleading. The lack of precision reporting makes it difficult to assess the practical utility of the method.
- **Resolution test** Clearly define the ground truth interface residues, report precision and F-score in addition to recall, and describe how the HADDOCK3 comparison is normalized to be comparable with the N-factor metric.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Novelty and positioning
- **Claim pointer** The introduction states: "training a binding affinity predictor between two proteins, and using it downstream to directly predict the hotspot amino acids that are key for the interaction between proteins has thus far remained mostly unaddressed."
- **Evidence pointer** Introduction; location not provided
- **Concern** The claim that this approach is "mostly unaddressed" is not supported by a systematic comparison with existing sequence-based PPI prediction tools. Several established methods, such as Dscript, PIPR, and SPRINT, predict protein-protein interactions from sequences. The manuscript does not discuss how Seq2Bind differs from or improves upon these methods. The comparison is limited to mutation predictors and docking, but not to other sequence-based deep learning approaches.
- **Why it matters** The novelty of the contribution is a key criterion for a high-impact journal. If the authors do not position their work relative to the existing literature, the reader cannot assess whether the contribution is genuinely new or incremental.
- **Resolution test** Add a systematic comparison with existing sequence-based PPI prediction methods, either in the introduction or as a benchmark in the results. Discuss the differences in methodology and performance.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states "eliminating the structural requirements that limit affinity prediction tools" but does not clarify whether this refers to the need for experimental structures or predicted structures. The phrase "binding affinity between proteins" is used, but the method predicts a normalized binding strength, not an absolute affinity constant.
- **Required correction** Clarify the distinction between predicted binding strength and experimentally measured affinity, and specify what "structural requirements" are being eliminated.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods, Datasets section
- **Evidence pointer** Methods, Datasets section; location not provided
- **Issue** The formula for computing negative delta G from KD is referenced but not shown. The text states "we computed the negative delta G as the target affinity score using the formula" and then the formula is missing.
- **Required correction** Include the formula explicitly in the text.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Results section
- **Evidence pointer** Results section; location not provided
- **Issue** The manuscript reports mean recovery rates but does not mention any measure of variance, such as standard deviation or confidence intervals, across the 6,063 dimers or the 14 benchmark complexes.
- **Required correction** Report variance measures or at least state whether the differences between models are statistically significant.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Webserver URL
- **Evidence pointer** Abstract, Data availability; location not provided
- **Issue** The webserver URL (https://agrivax.onrender.com/seq2bind/scan) is provided, but there is no description of the user interface, input format, or output format. The Colab link is also provided without a description of what the user should expect.
- **Required correction** Add a brief description of the webserver interface and the expected input/output formats, or refer to a user manual.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Results section
- **Evidence pointer** Results section; location not provided
- **Issue** The term "zero-shot models" is used in the results section ("identifying H-bonds from sequence alone presents a significant challenge for these zero-shot models"), but the models are fine-tuned on SKEMPI 2.0, so they are not zero-shot in the strict sense.
- **Required correction** Replace "zero-shot" with a more accurate term, such as "fine-tuned" or "sequence-only."

- **Technical failings that need to be addressed before the case is established**
  1. All figures and tables must be provided. The quantitative claims are not assessable without them.
  2. The dataset number inconsistency (6,063 vs 6,069) must be resolved.
  3. The training and evaluation data split must be clarified to rule out leakage.
  4. The evaluation metric must be defined precisely, including the ground truth interface definition and the reporting of precision.
  5. The missing formula for delta G computation must be included.

- **Assessment against Nature-style criteria**
  - **Originality** Moderate. The application of fine-tuned PLMs to alanine-scanning-based interface prediction is a reasonable extension of existing work, but the manuscript does not clearly differentiate itself from prior sequence-based PPI methods. The claim of novelty is not fully substantiated.
  - **Scientific importance** Moderate. Reliable sequence-based interface prediction would be valuable, but the reported recovery rates (67.4% at N=3) are modest, and the practical utility depends on precision, which is not reported.
  - **Interdisciplinary readership** Moderate. The topic bridges machine learning and structural biology, which could attract readers from both communities. However, the manuscript assumes familiarity with both PLMs and protein interaction terminology without sufficient background for a general audience.
  - **Technical soundness** Not assessable from the supplied material. The methods are described at a level that prevents evaluation of their correctness. The missing figures and tables are a critical gap.
  - **Readability for nonspecialists** Adequate but improvable. The introduction is clear, but the methods and results sections rely heavily on jargon and references to unseen figures. A brief explanation of the N-factor metric and the alanine-scanning concept would help nonspecialist readers.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript addresses a relevant problem and the general approach is sensible, but the absence of all figures, tables, and supplementary data makes it impossible to verify the central claims. The dataset number inconsistency and the lack of detail on the training procedure further undermine confidence. The authors should be invited to resubmit a revised version with all data visible, a complete methods description, and a clearer positioning relative to existing sequence-based PPI methods.

## Risk / unsupported claims
- The specific recovery rates (67.4% for ESM2, 68.2% for ProtBERT at N=3) are unsupported because the figures are not provided.
- The claim that Seq2Bench outperforms HADDOCK3 and mutation predictors is unsupported because the comparison data are not visible.
- The claim that "subtle point mutations are difficult to be translated into local changes in protein geometry" is presented as a finding but is not backed by any visible analysis.
- The claim that the models capture "allosterically coupled sites" is speculative and not supported by any experimental validation.
- The statement that the webserver is "freely accessible" cannot be verified from the supplied material.
- The claim that the approach handles "disordered proteins" is not supported by any specific analysis or benchmark on disordered proteins.