## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) and metadata (title, authors, journal, DOI, URL)
- **Assessment boundary** Scientific content, methodology, internal consistency, and support of claims based solely on the provided manuscript text; no external literature or unpublished data consulted
- **Shared manuscript claim summary** The authors propose that the cytotoxicity of aging protein condensates can be predicted from amino acid sequence by extending the FuzDrop method. They analyze TDP-43 deep-sequencing data and report that mutations promoting amyloid aggregation decrease cytotoxicity, while mutations promoting droplet formation increase cytotoxicity. They develop a random forest model using changes in droplet-promoting probability (ΔpDP), amyloid-promoting probability (ΔpAP), and multiplicity of binding modes (ΔMBM) to predict cytotoxicity, reporting high Pearson correlations (r = 0.975 for single mutants, r = 0.983 for double mutants).
- **Visible evidence base** Abstract, Introduction, Results (four subsections), Discussion and Conclusions, Methods (five subsections), references to Figures 1–5, Tables 1 and S1–S4, Figure S1, and a GitHub repository link
- **Missing materials affecting confidence** Figures 1–5 and Tables S1–S4 are referenced but not provided; the GitHub repository is not accessible from the supplied material; no raw data or detailed model performance metrics (e.g., error bars, cross-validation details) beyond Pearson correlations are shown; the yeast cytotoxicity assay details are only cited to reference 19, not described

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question, namely the sequence determinants of cytotoxicity in protein condensates, with potential relevance to neurodegenerative disease. The conceptual framework, based on the droplet landscape and binding mode multiplicity, is original and builds logically on prior work by the same group. However, the central claims rest on correlative analyses whose robustness cannot be fully assessed from the provided text, and several methodological details are insufficiently described. The conclusion that amyloid aggregation may be partially protective is provocative but requires stronger evidence, particularly given the indirect nature of the cytotoxicity measurements and the lack of mechanistic validation. The manuscript is likely to interest the phase separation and neurodegeneration communities, but the case is not fully established from the supplied material.
- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation, protein aggregation, and neurodegeneration, especially those focused on TDP-43 biology and ALS. The proposed sequence-based predictor could be of practical use for interpreting disease-associated mutations and for designing experiments. The conceptual claim about the relationship between droplet formation and cytotoxicity may also interest biophysicists and cell biologists working on condensate maturation.
- **Major strengths** The study addresses a clinically relevant problem with a clear conceptual framework. The use of large-scale deep-sequencing data is appropriate and powerful. The extension of an existing, publicly available method (FuzDrop) is a practical contribution. The distinction between droplet-promoting and aggregation-promoting mutations, and the suggestion that they have opposite effects on cytotoxicity, is a testable and potentially important hypothesis.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (model validation), R1-M2 (causality), R1-M3 (data availability), R1-M4 (statistical reporting)
- **Assessment against Nature-style criteria** Originality: high, as the application of the droplet landscape to predict cytotoxicity is novel. Scientific importance: potentially high, given the relevance to ALS and condensate biology, but the impact depends on the robustness of the predictive model and the generality of the findings. Interdisciplinary readership: the topic bridges biophysics, cell biology, and clinical neuroscience, and the writing is largely accessible, though some methodological sections assume specialist knowledge. Technical soundness: currently not fully established due to incomplete validation details and lack of independent testing. Readability for nonspecialists: the abstract and introduction are clear, but the results and methods sections are dense and would benefit from more explanatory text.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding model validation, causality, and data availability. Currently not established from the provided evidence.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim high predictive performance of their model, with Pearson correlation coefficients of r = 0.975 for single mutants and r = 0.983 for double mutants (Results, "Extension of the FuzDrop Method").
- **Evidence pointer** Results, "Extension of the FuzDrop Method"; Table 1; Table S3; Methods, "Extending the FuzDrop Method"
- **Concern** The reported correlations are extremely high, which raises concerns about overfitting. The model is trained and evaluated using out-of-bag (OOB) validation on the same dataset, which is a form of internal validation. No independent test set, cross-validation scheme, or external dataset is described. The OOB error estimate can be optimistic, especially with a large number of features or correlated predictors. The manuscript does not report the number of features, the feature importance, or the model complexity, making it impossible to assess the risk of overfitting. Additionally, the model is tested on a subset of droplet region mutations and on ALS-associated mutants, but these appear to be subsets of the same data used for training, not independent validations.
- **Why it matters** If the model is overfitted, the reported predictive performance will not generalize to new sequences, undermining the central claim of a sequence-based predictor of cytotoxicity. The high correlations may be an artifact of the validation procedure rather than a reflection of true predictive power.
- **Resolution test** The authors should provide a clear description of the model architecture, including the number of features and trees, and perform a rigorous validation using an independent test set (e.g., a held-out portion of the data not used in any training step, or an external dataset). They should report performance metrics such as root mean square error and confidence intervals, and ideally compare their model against simpler baselines (e.g., linear regression or a null model).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance / Causality
- **Claim pointer** The authors conclude that "mutations that promote aggregation tend to decrease cytotoxicity, while those that promote droplet formation tend to increase cytotoxicity" (Abstract) and that "amyloid aggregation within condensates may have a partially protective role against cytotoxicity" (Discussion).
- **Evidence pointer** Abstract; Results, "Cytotoxicity of TDP-43 Mutants Is Linked with Droplet Formation"; Discussion and Conclusions
- **Concern** The analysis is purely correlative. The authors infer a causal relationship between droplet formation and cytotoxicity from statistical associations between predicted biophysical properties (pDP, pAP, MBM) and measured growth rates in yeast. However, the yeast cytotoxicity assay measures a composite phenotype that may not directly reflect the specific molecular mechanism proposed. The authors do not provide any experimental manipulation (e.g., mutations designed to specifically alter droplet formation without affecting aggregation, or vice versa) to test the causal role of droplet formation in cytotoxicity. The claim that aggregation is "partially protective" is a strong interpretation that goes beyond the correlational data.
- **Why it matters** The central conclusion of the paper, namely that the amino acid code for cytotoxicity is linked to droplet formation rather than aggregation, has potential therapeutic implications. If the causal direction is not established, the conclusion may be misleading and could lead to incorrect assumptions about disease mechanisms.
- **Resolution test** The authors should either temper their conclusions to reflect the correlational nature of the analysis, or provide additional evidence for causality. This could include experimental validation using designed mutants that decouple droplet formation from aggregation, or a discussion of why the correlational evidence is sufficient to support the causal claim.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The authors state that "in-house R scripts used to generate data and figures as well as the serialized random forest models can be downloaded from the GitHub repository" (Methods, "Extending the FuzDrop Method").
- **Evidence pointer** Methods, "Extending the FuzDrop Method"
- **Concern** The GitHub repository is referenced but not accessible from the supplied material. The manuscript does not provide a version number, a commit hash, or a DOI for the repository, which makes it difficult to ensure reproducibility. Furthermore, the methods section does not specify the exact version of the FuzDrop, FuzPred, and CamSol programs used, nor the parameters for the random forest grid search beyond the number of trees and variables per split.
- **Why it matters** Reproducibility is a core requirement for scientific claims, especially for a computational predictor. Without access to the code and exact parameters, other researchers cannot verify the results or apply the method to their own data.
- **Resolution test** The authors should provide a stable link to the repository (e.g., with a DOI) and include a detailed description of the software versions, parameters, and data processing steps in the methods or supplementary material.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors report Pearson correlation coefficients between predicted and experimental cytotoxicity values (Results, "Extension of the FuzDrop Method").
- **Evidence pointer** Results, "Extension of the FuzDrop Method"; Table 1; Table S3
- **Concern** The manuscript reports only Pearson correlation coefficients. No other performance metrics are provided, such as root mean square error, mean absolute error, or the coefficient of determination (R²). The correlation coefficient alone can be misleading, as it does not indicate the magnitude of prediction errors. Additionally, the authors do not report confidence intervals or significance levels for the correlations, nor do they describe the distribution of the data (e.g., whether the data are normally distributed, which is an assumption for Pearson correlation).
- **Why it matters** A high correlation does not necessarily imply accurate predictions, especially if the range of cytotoxicity values is narrow or if there are outliers. Without additional metrics, the practical utility of the predictor cannot be assessed.
- **Resolution test** The authors should report additional performance metrics, such as R², root mean square error, and mean absolute error, along with confidence intervals. They should also consider using rank-based correlation measures (e.g., Spearman) if the data are not normally distributed.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that "mutations that promote aggregation tend to decrease cytotoxicity, while those that promote droplet formation tend to increase cytotoxicity." This is a key finding, but the abstract does not mention the predictive model or its performance, which is a major part of the paper.
- **Required correction** Consider adding a sentence in the abstract summarizing the predictive model and its performance to give readers a complete overview of the study.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, "Droplet Landscape Representation"
- **Evidence pointer** Results, "Droplet Landscape Representation"; Figure 2
- **Issue** The description of the droplet landscape and the interpretation of the regions (droplet, amyloid, aggregation hot-spot) is clear, but the figure is not provided. The text refers to "Figure 2A" and "Figure 2B" without describing the axes or the data points in detail.
- **Required correction** Provide a brief description of the figure in the text, including the axes and the meaning of the different regions, so that readers can understand the figure even if it is not immediately visible.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methodology
- **Affected element** Methods, "Analysis of TDP-43 Deep-Sequencing Data"
- **Evidence pointer** Methods, "Analysis of TDP-43 Deep-Sequencing Data"
- **Issue** The methods state that mutations were assigned to regions based on "experimental data σ" (reference 19), but the exact criteria for this assignment are not described. It is unclear how the boundaries of the regions (e.g., residues 312–320 and 331–341) were determined.
- **Required correction** Clarify the criteria used to define the amyloid core, aggregation hot-spot, and droplet regions, and provide the source of these boundaries.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Discussion and Conclusions
- **Evidence pointer** Discussion and Conclusions
- **Issue** The discussion introduces the concept of "promiscuity" in the context of binding modes, but this term is not defined or explained. It is unclear how promiscuity relates to the proposed mechanism of cytotoxicity.
- **Required correction** Define "promiscuity" in this context and explain how it relates to the binding mode analysis and the proposed mechanism.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "Extending the FuzDrop Method"
- **Evidence pointer** Methods, "Extending the FuzDrop Method"
- **Issue** The methods state that "random forest models with the highest Pearson’s correlation coefficients were inferred using grid optimization," but the range of parameters tested (e.g., values of ntree and mtry) is not specified.
- **Required correction** Provide the range of parameters tested in the grid search and the final selected values for the models.

## Risk / unsupported claims
- The claim that "amyloid aggregation within condensates may have a partially protective role against cytotoxicity" is not directly supported by the data, which are correlational and based on a yeast model. This is an interpretation that goes beyond the evidence.
- The claim of high predictive performance (r > 0.90) is not fully supported due to the lack of independent validation and the potential for overfitting.
- The generalizability of the findings beyond TDP-43 is not established, as the analysis is limited to a single protein and a yeast assay.
- The statement that "mutations that promote aggregation tend to decrease cytotoxicity" is based on a subset of mutants with large changes in cytotoxicity (Δetox > 3σ) and may not hold for all mutations.
- The relevance of the yeast cytotoxicity measurements to human disease is not discussed in detail, and the authors do not address potential differences between yeast and human cellular contexts.