## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, supplementary information descriptions)
- **Assessment boundary** Scientific validity, methodological soundness, claim substantiation, and presentation quality of the described algorithm and its results
- **Shared manuscript claim summary** The authors present Morpheus, a fragment-based algorithm that predicts metamorphic (fold-switching) behaviour in proteins from sequence alone, achieving 84.7% cross-validation accuracy and identifying ~10% of proteins across 57 proteomes as fold-switching capable
- **Visible evidence base** Abstract, introduction, methods sections 2.1–2.6, results sections 3.1–3.3, scope/limitations, supplementary figure/table descriptions, data availability statements
- **Missing materials affecting confidence** Actual figures and tables (Figures 1–6, Tables 1–3), full supplementary information content, training dataset details, proteome prediction data, web server functionality, code implementation details

## Reviewer
- **Overall assessment** The manuscript presents a potentially useful computational approach for predicting metamorphic proteins from sequence, addressing a genuine gap in the field. However, the current version lacks critical details needed to evaluate the method's validity, reproducibility, and performance claims. The absence of actual figures, tables, and quantitative results makes it impossible to assess the core claims. The conceptual framing around fragment-based structural diversity is interesting, but several methodological choices require justification and the evaluation appears limited to internal cross-validation without external benchmarking.
- **Who would be interested in the results, and why** Researchers studying protein conformational diversity, fold-switching proteins, and the "metamorphome" would find this relevant. Computational biologists developing protein function prediction tools and those interested in large-scale proteome annotation would also be interested. Experimentalists seeking candidate metamorphic proteins for validation could use the predictions. The web server aspect increases practical utility for the broader protein science community.
- **Major strengths**
  - Addresses an important and timely problem: systematic identification of metamorphic proteins at proteome scale
  - Novel combination of fragment-based structural database mining with machine learning classification
  - Computational efficiency improvements (Trie-based search) enable proteome-wide application
  - Provides practical resources: web server and public prediction data
  - Thoughtful discussion of the spectrum between monomorphic and disordered proteins
- **Major Concerns**
  - **R1-M1** (Blocking): The central performance claim of 84.7% accuracy and MCC 0.698 cannot be evaluated without seeing the actual results, figures, and tables. The manuscript text describes these metrics but provides no visible data, confusion matrices, or comparative analysis.
  - **R1-M2** (Blocking): The training dataset construction is inadequately described. The authors state 189 fold-switching and 198 monomorphic sequences were used, but the criteria for inclusion, the source of negative examples, and how potential biases were addressed are not specified. The reliance on "existing curated literature" without describing the curation process is insufficient.
  - **R1-M3** (Blocking): No external validation or benchmarking against existing methods is presented. The authors claim superiority over "purely sequence based algorithm" but do not name or compare against specific existing predictors (e.g., the diversity index method from Chen et al. that they cite). Internal cross-validation alone is insufficient to establish generalizability.
  - **R1-M4** (Major): The biological interpretation of the ~10% prediction rate across proteomes is problematic. This rate is substantially higher than the 0.5–4% estimate cited for PDB, and the authors do not adequately address this discrepancy. The inclusion of IDPs in the positive predictions confounds the interpretation of what "metamorphic" means in their predictions.
  - **R1-M5** (Major): The choice of 7-mer fragments and the use of the 3rd residue rather than the middle residue is presented as an empirical optimization, but the biological rationale is unclear. The manuscript does not explain why a 7-residue window is optimal for capturing fold-switching determinants, nor why the 3rd position outperforms the central position.
  - **R1-M6** (Major): The handling of proteins with no fragment hits in the database is problematic. Setting diversity to 1, entropy and substitution to 0, and uncertainty to 1.0 for these cases appears to arbitrarily classify them as metamorphic, which could inflate predictions for novel or poorly represented protein families.
- **Minor Comments**
  - **R1-m1** Axis: Presentation. The manuscript references many figures and tables that are not included in the provided text, making it impossible to follow the results. All figures and tables must be included in the main text or clearly referenced with their content described.
  - **R1-m2** Axis: Methodology. The description of the substitution matrix optimization is vague. The parameters a, b, c, d are mentioned but their biological meaning and the range of values tested are not clearly explained.
  - **R1-m3** Axis: Methodology. The choice of SVM with quadratic kernel is justified by "lower model complexity," but no comparison of model complexity metrics or overfitting analysis is presented.
  - **R1-m4** Axis: Reproducibility. The manuscript states code is available on Zenodo, but the specific repository structure, dependencies, and usage instructions are not described.
  - **R1-m5** Axis: Interpretation. The claim that CXCL11 and MAD2B are good candidates because they are "related to already known metamorphic proteins" is confusing, as the authors also state the sequences are not similar. The relationship rationale needs clarification.
  - **R1-m6** Axis: Literature context. The introduction cites previous prediction approaches but does not clearly articulate how Morpheus differs methodologically from the diversity index approach it builds upon, beyond the proteome-scale application.
  - **R1-m7** Axis: Statistics. The use of Hoeffding's inequality to model uncertainty is mentioned but the derivation and validation of the final uncertainty function are not shown.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5, R1-M6
- **Assessment against Nature-style criteria**
  - **Originality**: Moderate. The fragment-based approach with structural database mining is a reasonable extension of existing ideas, but the combination of specific elements (Trie search, multiple scoring metrics, SVM classification) has some novelty. However, the conceptual advance over the cited diversity index method is not clearly articulated.
  - **Scientific importance**: Potentially high if the method works as claimed, given the growing interest in fold-switching proteins and the need for proteome-scale prediction tools. However, the current evidence does not establish this importance.
  - **Interdisciplinary readership**: The topic bridges structural biology, bioinformatics, and protein science, which could attract broad interest. The web server and proteome predictions increase practical relevance.
  - **Technical soundness**: Cannot be adequately assessed from the provided text. Key methodological details are missing, and the evaluation appears limited to internal cross-validation without external benchmarking or independent validation.
  - **Readability for nonspecialists**: The manuscript is generally well-written and accessible, with clear explanations of concepts. However, some methodological sections assume familiarity with machine learning and structural biology terminology.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript requires major revisions including full presentation of results, detailed methodology, external validation, and clearer articulation of the biological significance of predictions before the claims can be evaluated.

## Risk / unsupported claims
- The 84.7% accuracy and MCC 0.698 performance claims are unsupported without visible results data
- The claim that Morpheus "outperforms" existing sequence-based predictors is unsupported without named comparators and statistical comparison
- The ~10% metamorphic protein rate across proteomes is presented without adequate discussion of its relationship to prior estimates of 0.5–4%
- The claim that residue-level diversity scores can localize fold-switching regions is not demonstrated with specific examples
- The biological significance of the shortlisted candidate proteins is asserted without experimental validation or detailed structural analysis
- The statement that Morpheus is "the first implementation of a proteome-wide metamorphic protein predictor" is a strong claim that requires more careful literature verification
- The uncertainty function derived from Hoeffding's inequality is presented without derivation or validation
- The claim that the method can distinguish metamorphic proteins from IDPs is not supported by the described methodology, which appears to conflate these categories