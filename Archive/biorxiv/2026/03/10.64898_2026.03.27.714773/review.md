## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, conclusions, supplementary sections as provided)
- **Assessment boundary** Scientific validity, methodological soundness, reproducibility, and support of claims based solely on the provided manuscript content
- **Shared manuscript claim summary** The authors present IDBSpred, a sequence-based machine learning method using ESM-2 protein language model embeddings and a multilayer perceptron to predict residue-level IDP-binding sites on structured partner proteins, trained on the DIBS database, achieving an ROC AUC of 0.87 and average precision of 0.61, with structural case studies showing recovery of major binding interfaces
- **Visible evidence base** Abstract, Introduction, Model and Methods (dataset construction, embeddings, classifier architecture, training), Results (amino acid composition analysis, performance metrics, structural case studies), Conclusions, Author Contributions, Competing Interests, Acknowledgement
- **Missing materials affecting confidence** No figures or tables are provided; no quantitative performance breakdown per complex; no baseline comparisons; no cross-validation details; no dataset statistics (e.g., number of proteins, residue counts, class balance); no hyperparameter tuning details; no statistical significance tests; no error analysis; no comparison with existing predictors such as Disobind

## Reviewer
- **Overall assessment** The manuscript addresses a relevant and understudied problem, namely the prediction of IDP-binding sites on structured partner proteins, which complements existing tools focused on disordered regions. The use of ESM-2 embeddings with a simple MLP is a reasonable and modern approach. However, the current manuscript provides insufficient methodological detail and lacks critical validation steps to establish the claimed performance. The absence of figures, baseline comparisons, and rigorous evaluation protocols substantially limits the ability to assess the technical soundness and generalizability of the method. The amino acid composition analysis is descriptive but not statistically validated. The structural case studies are qualitative and lack quantitative overlap metrics. Overall, the core idea is promising, but the evidence presented is not sufficient to support the strong claims made in the abstract and conclusions.
- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein-protein interaction prediction, intrinsically disordered proteins, and machine learning applications in structural biology. Researchers studying IDP-mediated signaling and therapeutic targeting of such interfaces may also find the tool useful. The method could be of interest to those developing sequence-based predictors for interface residues, particularly in the context of disordered partner recognition.
- **Major strengths** The problem is well-motivated and addresses a genuine gap in the field. The use of a protein language model (ESM-2) is current and appropriate. The method is simple and potentially reproducible. The focus on the structured partner side of IDP interactions is a useful complement to existing disorder-centric predictors. The authors acknowledge limitations and suggest future improvements.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (lack of dataset statistics and leakage control), R1-M2 (no baseline comparisons), R1-M3 (no cross-validation or statistical rigor), R1-M4 (qualitative structural validation without quantitative metrics), R1-M5 (descriptive amino acid analysis without statistical testing)
- **Assessment against Nature-style criteria** Originality: The problem is somewhat novel, but the methodological approach (ESM-2 embeddings plus MLP) is not new in itself; the novelty lies in the application to the structured partner side. Scientific importance: The problem is important for understanding IDP-mediated interactions and therapeutic targeting, but the current evidence does not establish a significant advance over existing methods. Interdisciplinary readership: The topic could appeal to structural biologists, computational biologists, and drug discovery researchers, but the manuscript lacks sufficient context and validation for a broad audience. Technical soundness: The methodology is described at a high level but lacks critical details and rigorous evaluation, making the technical claims unverifiable from the provided material. Readability for nonspecialists: The manuscript is generally readable, but the lack of figures and quantitative results makes it difficult for nonspecialists to assess the claims.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript has potential, but major revisions and additional validation are required before the claims can be considered supported.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data and reproducibility
- **Claim pointer** The authors claim the method was trained and evaluated on more than 700 non-redundant complexes from the DIBS database, with residues labeled as binding or non-binding.
- **Evidence pointer** Model and Methods, Based Dataset construction; Results, Figure 3 (not provided)
- **Concern** The manuscript does not provide essential dataset statistics, such as the number of unique proteins, total residue counts, class balance between positive and negative samples, or the redundancy reduction criteria used. More critically, the authors state that all positive and negative residues were randomly divided into training and test sets. This random split at the residue level risks data leakage, as residues from the same protein may appear in both training and test sets, leading to inflated performance estimates. No protein-level splitting or sequence similarity-based partitioning is described.
- **Why it matters** Without proper dataset statistics and leakage control, the reported performance metrics (AUC 0.87, AP 0.61) cannot be interpreted as reliable estimates of generalization to new proteins. This is a fundamental issue that undermines the core claim of the method's effectiveness.
- **Resolution test** Provide detailed dataset statistics, describe the redundancy reduction procedure, and perform protein-level or sequence-identity-based splitting for training and testing. Report performance under this stricter evaluation protocol.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Comparative evaluation
- **Claim pointer** The authors claim IDBSpred provides an effective framework for residue-level prediction of IDP-binding sites on structured proteins.
- **Evidence pointer** Results, Figure 3 (not provided); Introduction, paragraph 3
- **Concern** No comparison with existing methods is provided. The authors mention Disobind as a recent advance in the introduction, but no quantitative or qualitative comparison is made. Without benchmarking against current state-of-the-art predictors, the claimed effectiveness of IDBSpred cannot be established.
- **Why it matters** A new predictor must demonstrate added value over existing tools. The absence of any baseline comparison makes it impossible to assess whether IDBSpred offers any advantage in accuracy, speed, or applicability.
- **Resolution test** Include a comparative evaluation against at least Disobind and other relevant predictors on a common benchmark dataset, reporting standard metrics such as AUC, AP, F1, and Matthews correlation coefficient.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors report an ROC AUC of 0.87 and an average precision of 0.61 for the MLP classifier.
- **Evidence pointer** Results, Figure 3d and 3e (not provided)
- **Concern** The performance metrics are reported as single values without any measure of variance, confidence intervals, or statistical significance testing. No cross-validation is described, and the learning curves in Figure 3a are described qualitatively. It is unclear whether the reported performance is stable across different random seeds or data splits.
- **Why it matters** Single-point estimates without variance or significance testing do not provide sufficient evidence for the robustness of the method. The claims of strong performance may not be reproducible.
- **Resolution test** Perform k-fold cross-validation (e.g., 5-fold or 10-fold) at the protein level, report mean and standard deviation for all metrics, and include statistical tests comparing against baselines or random classifiers.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation of structural predictions
- **Claim pointer** The authors claim that structural case studies show the predicted sites largely overlap with experimentally defined interfaces and recover major binding regions in representative complexes.
- **Evidence pointer** Results, Figure 4 (not provided)
- **Concern** The structural validation is purely qualitative. The authors describe visual overlap but provide no quantitative metrics such as precision, recall, F1 score, or overlap coefficients (e.g., Jaccard index) between predicted and experimentally defined binding sites for the three complexes. The selection criteria for these three complexes are also not stated.
- **Why it matters** Qualitative visual inspection is subjective and does not provide a rigorous assessment of prediction accuracy at the residue level. Without quantitative metrics, the claim that the method recovers major binding interfaces is not substantiated.
- **Resolution test** Provide quantitative overlap metrics for each case study, such as precision, recall, and F1 score, and justify the selection of the representative complexes.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Statistical analysis of sequence composition
- **Claim pointer** The authors claim that IDP-binding sites are enriched in aromatic residues (Trp, Tyr, Phe) and depleted in Ala and small or conformationally restrictive residues.
- **Evidence pointer** Results, Figure 2 (not provided)
- **Concern** The amino acid composition analysis is descriptive. No statistical tests are reported to support the claims of enrichment or depletion. The figure is not provided, and the magnitude of the effects is not quantified.
- **Why it matters** Without statistical testing, the observed composition biases could be due to chance or confounding factors such as overall protein composition. The biological interpretation relies on these claims being statistically robust.
- **Resolution test** Perform statistical tests (e.g., chi-square or Fisher's exact test, or a binomial test with appropriate background correction) and report effect sizes and p-values for each amino acid.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and completeness
- **Affected element** Model and Methods, Based Dataset construction
- **Evidence pointer** Location not provided
- **Issue** The section title "Based Dataset construction" appears to be a typo, likely intended as "Dataset construction" or "Base dataset construction". The section also lacks details on how the DIBS database was accessed, which version was used, and how the binding site annotations were derived.
- **Required correction** Correct the section title and provide details on database version, access date, and annotation criteria.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Model and Methods, Model training
- **Evidence pointer** Location not provided
- **Issue** The manuscript states training was performed for 25 epochs with a batch size of 32, but does not specify the number of training and test samples, the optimization details beyond the learning rate, or whether early stopping was used. The choice of 25 epochs appears arbitrary.
- **Required correction** Provide the number of samples, describe the training procedure in more detail, and justify the number of epochs or describe the early stopping criterion.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Evaluation methodology
- **Affected element** Results, Figure 3
- **Evidence pointer** Location not provided
- **Issue** The manuscript reports AUC and average precision but does not report other standard classification metrics such as precision, recall, F1 score, or specificity at a fixed threshold. The threshold for binary classification is not defined.
- **Required correction** Report additional metrics and specify the classification threshold or provide a range of thresholds with corresponding metrics.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Results, Figure 4
- **Evidence pointer** Location not provided
- **Issue** The figure is described as showing real and predicted binding sites with blue and red coloring, but the color scheme is not defined in the text. The description of "blue marks binding-site residues, while red marks non-binding residues" is ambiguous regarding which panel uses which color.
- **Required correction** Clarify the color scheme in the figure legend and text.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Language and grammar
- **Affected element** Introduction, paragraph 1
- **Evidence pointer** Location not provided
- **Issue** The sentence "At least 33% of eukaryotic proteins contain regions that does not possess any stable structure" contains a subject-verb agreement error ("regions that does" should be "regions that do").
- **Required correction** Correct the grammatical error.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Footnotes
- **Evidence pointer** Location not provided
- **Issue** The footnote states there is a typo in the first author's last name, but the manuscript title and author list use "Jones" while the footnote says it should be "Jones" instead of "Jone". This is confusing and should be resolved.
- **Required correction** Clarify the correct spelling of the author's name and ensure consistency throughout the manuscript.

## Risk / unsupported claims
- The claim that IDBSpred achieves strong overall performance (AUC 0.87, AP 0.61) is unsupported due to the lack of dataset statistics, potential data leakage from random residue-level splitting, and absence of cross-validation or confidence intervals.
- The claim that the method effectively recovers major binding interfaces in structural case studies is unsupported due to the purely qualitative nature of the validation and lack of quantitative metrics.
- The claim that IDP-binding sites are enriched in specific amino acids is unsupported without statistical testing.
- The claim that the method provides a practical framework for identifying potential therapeutic hotspots is speculative and not directly validated by the presented results.
- The generalizability of the method to new proteins is not established given the evaluation protocol described.