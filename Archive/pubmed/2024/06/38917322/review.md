## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, data availability)
- **Assessment boundary** Scientific content, methodological rigor, validity of claims, and presentation quality as presented in the provided text
- **Shared manuscript claim summary** The authors refine the pool of RNA-binding domains (RBDs) by combining published lists with InterPro data, apply a three-step selection procedure based on enrichment in experimentally detected RNA-binding proteins (RBPs) across 13 species, identify 15 new RBD candidates validated by peptide-level RNA-binding data, and introduce an RBP2GO composite score integrating RBD/Rfam information to produce a high-confidence list of 2018 human RBPs.
- **Visible evidence base** Methods and results sections describing the selection procedure, statistical analyses, GO enrichment, peptide validation, and composite score construction; figures referenced (Figures 1–8) and supplementary tables cited but not provided
- **Missing materials affecting confidence** Supplementary tables (S1–S20), figures themselves, exact statistical outputs, code/scripts, and the RBP2GO database interface were not available for inspection

## Reviewer
- **Overall assessment** This manuscript presents a useful bioinformatics resource and a systematic approach to refining RBD annotations and predicting RBPs. The integration of multiple data sources and the composite scoring scheme are sensible. However, several methodological details are underspecified, validation is partially circular, and the novelty relative to existing tools (e.g., SONAR, HydRA, RBPbase) is not fully articulated. The claims of prediction improvement and new RBD discovery require stronger statistical and experimental support.
- **Who would be interested in the results, and why** Researchers studying RNA-protein interactions, computational biologists developing RBP prediction tools, and experimentalists seeking candidate RBPs for validation. The updated RBP2GO database with domain-level annotations and composite scores will be a practical resource for the community.
- **Major strengths** 1) Pan-species scope covering 13 organisms with 176,896 proteins. 2) Systematic filtering of RBD candidates using empirical RBP data. 3) Integration of multiple evidence types (RBDs, Rfam IDs, IDRs, interaction data) into a composite score. 4) Public availability of the updated database and scripts. 5) Identification and peptide-based validation of 15 new RBD candidates.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (circularity in RBD selection), R1-M2 (insufficient validation of new RBDs), R1-M3 (composite score weighting not justified), R1-M4 (comparison with existing tools incomplete)
- **Assessment against Nature-style criteria**  
  - *Originality*: Moderate. The concept of refining RBD lists using empirical data is not entirely new, but the scale and integration are commendable.  
  - *Scientific importance*: Moderate to high. A reliable RBP catalog and improved domain annotations would benefit the field.  
  - *Interdisciplinary readership*: Moderate. Primarily of interest to RNA biology and bioinformatics communities.  
  - *Technical soundness*: Needs improvement. Several methodological choices lack justification or rigorous validation.  
  - *Readability for nonspecialists*: Acceptable. The text is generally clear, though some methods sections are dense.
- **Recommendation posture** Supportive if technical concerns are resolved. The resource has value, but the current evidence does not fully establish the claimed improvements in classification and prediction.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Validity of RBD selection  
- **Claim pointer** The authors claim that the three-step selection procedure identifies RBDs enriched in RBPs, and that these selected RBDs are strong indicators of RNA-binding potential.  
- **Evidence pointer** Methods "Selection of the RNA-binding domains"; Results "The proportion of RBPs and RBD-containing proteins in proteomes differs across species"; Figure 1  
- **Concern** The selection procedure uses the same RBP datasets (from RBP2GO) to both define RBPs and test for RBD enrichment. This creates a circularity problem: RBDs are selected because they are enriched in proteins already classified as RBPs, and then the same RBDs are used to validate the RBP classification. The authors do not address this circularity or provide an independent validation set.  
- **Why it matters** If the selection is circular, the reported enrichment and predictive power of the selected RBDs may be inflated, undermining the central claim that these RBDs are reliable indicators of RNA-binding potential.  
- **Resolution test** Provide a validation strategy that uses independent datasets (e.g., hold-out RBP datasets, cross-species validation, or experimental RNA-binding data) to demonstrate that the selected RBDs predict RNA-binding in proteins not used in the selection process.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Validation of new RBDs  
- **Claim pointer** The authors claim to have identified 15 new RBDs validated by RNA-bound peptide datasets.  
- **Evidence pointer** Methods "Identification of new RBDs using the human RBPs lacking canonical RBDs"; Results "New RBDs can be predicted in RBPs without known RBDs and high RBP2GO score"; Figure 7F–G  
- **Concern** The validation of the 15 new RBDs relies on overlap with RNA-bound peptides from published datasets. However, the statistical significance of this overlap is not rigorously established. The authors do not report effect sizes, confidence intervals, or comparison against a null model (e.g., random expectation based on protein length or amino acid composition). Additionally, the peptide datasets themselves may have biases (e.g., toward abundant or highly crosslinkable proteins) that are not accounted for.  
- **Why it matters** Without rigorous statistical validation, the claim that these 15 domains are bona fide RBDs is not supported. Overlap with peptide data could occur by chance or due to dataset biases.  
- **Resolution test** Perform a permutation or bootstrap analysis to show that the observed peptide overlap is significantly higher than expected by chance, controlling for protein length, amino acid composition, and dataset biases. Report effect sizes and confidence intervals.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Composite score construction  
- **Claim pointer** The RBP2GO composite score combines three components (listing count, interaction-based score, and RBD/Rfam-based score) to improve RBP classification.  
- **Evidence pointer** Methods "Selection of the RNA-binding domains"; Methods "RBP2GO composite score"; Figure 8  
- **Concern** The weighting of the three components in the composite score is not justified. The authors state that a Random Forest algorithm was used to determine weights, but do not provide details on the training data, feature importance, or model performance. It is unclear whether the composite score outperforms simpler alternatives (e.g., the original RBP2GO score alone) and whether the improvement is statistically significant.  
- **Why it matters** If the composite score does not provide a meaningful improvement over existing scores, the claim of "advancing classification" is not substantiated.  
- **Resolution test** Provide a detailed description of the Random Forest model, including training/validation splits, feature importance, and a comparison of the composite score against the original RBP2GO score and other existing tools (e.g., HydRA, RBPbase) using appropriate metrics (e.g., AUROC, precision-recall).

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Comparison with existing tools  
- **Claim pointer** The authors imply that their approach improves RBP prediction and classification, but do not systematically compare against existing prediction tools.  
- **Evidence pointer** Results "A new RBP2GO composite score helps defining a high-confidence human RBP list"; Discussion  
- **Concern** The manuscript does not include a direct comparison of the RBP2GO composite score or the new RBD list against existing resources such as HydRA, RBPbase, or other RBP prediction methods. Without such a comparison, it is difficult to assess the added value of this work.  
- **Why it matters** The field already has multiple RBP prediction tools and databases. To claim advancement, the authors must demonstrate that their approach provides improved accuracy, coverage, or utility relative to existing methods.  
- **Resolution test** Add a comparative analysis using benchmark datasets (e.g., known RBPs and non-RBPs) to evaluate the performance of the RBP2GO composite score and the new RBD list against existing tools, reporting standard metrics and statistical tests.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity of terminology  
- **Affected element** Use of "RBP aspirants"  
- **Evidence pointer** Results "New RBP candidates can be identified from non-RBPs with RBD"  
- **Issue** The term "RBP aspirants" is informal and not defined precisely. It is unclear whether these are predicted RBPs, candidate RBPs, or something else.  
- **Required correction** Define the term explicitly and use a more standard terminology (e.g., "candidate RBPs" or "predicted RBPs").

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Statistical reporting  
- **Affected element** Correlation analyses  
- **Evidence pointer** Results "Disordered regions are enriched in proteins with RBD"; Figure 5  
- **Issue** Correlation coefficients are mentioned but no confidence intervals or p-values are reported for the key correlations (e.g., between IDR content and RBD presence).  
- **Required correction** Report confidence intervals and p-values for all correlation analyses, and specify the statistical test used.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Data availability  
- **Affected element** Supplementary tables  
- **Evidence pointer** Data availability section  
- **Issue** The manuscript references many supplementary tables (S1–S20) but they were not provided for review. It is impossible to verify the underlying data.  
- **Required correction** Ensure all supplementary tables are made available for review and include a summary of their contents in the main text.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Figure quality  
- **Affected element** Figures 1–8  
- **Evidence pointer** Results sections referencing figures  
- **Issue** The figures are not included in the provided text, so their quality and clarity cannot be assessed.  
- **Required correction** Provide the figures for review and ensure they are legible, with clear labels and legends.

- **Concern ID** R1-m5  
- **Severity** Minor  
- **Axis** Discussion of limitations  
- **Affected element** Discussion section  
- **Evidence pointer** Discussion  
- **Issue** The discussion does not address potential limitations of the study, such as the circularity issue, dataset biases, or the generalizability of the findings to non-model organisms.  
- **Required correction** Add a limitations paragraph acknowledging these issues and suggesting future directions to address them.

## Risk / unsupported claims
- The claim that the 15 newly identified RBDs are validated by peptide data is not statistically substantiated (R1-M2).
- The claim that the RBP2GO composite score improves RBP classification is not demonstrated through comparison with existing tools (R1-M4).
- The claim that RBDs are strong indicators of RNA-binding potential is weakened by the circularity in the selection procedure (R1-M1).
- The statement that "RBP aspirants seem to interact more with RBPs than the non-RBPs lacking any RNA-related annotation" is based on indirect evidence and requires direct statistical testing.
- The generalizability of the findings to all 13 species is not fully established, as some species have very few RBP datasets, and the analysis may be underpowered for those species.