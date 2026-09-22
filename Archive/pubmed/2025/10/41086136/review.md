## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors propose a hybrid machine learning framework combining sequence-based hidden states with 23 physical features via attention-guided fusion to predict radius of gyration and other conformational properties of intrinsically disordered proteins (IDPs). Models are trained on Brownian dynamics simulations of approximately 7000 IDPs from MobiDB. Sequence-based models outperform feature-only models; hybrid biGRU achieves best performance. SHAP and integrated gradient analyses identify key physical features and sequence parameters.
- **Visible evidence base** Abstract text only; no quantitative results, model architecture details, dataset splits, or validation procedures are provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, model hyperparameters, training/validation protocols, baseline comparisons, statistical significance tests, and code or data availability statements

## Reviewer
- **Overall assessment** The abstract presents a plausible and potentially useful approach for fast prediction of IDP conformational properties. The integration of sequence and physics-based features with attention mechanisms is a reasonable strategy, and the use of explainability tools is commendable. However, the abstract alone provides insufficient detail to assess the technical soundness, the robustness of the claimed improvements, or the generalizability of the framework. Several claims are made without supporting quantitative evidence, and the lack of comparison to established methods or experimental benchmarks limits the current assessment.
- **Who would be interested in the results, and why** Researchers in computational biophysics, protein biophysics, and machine learning applied to molecular systems would find this work relevant. Practitioners studying intrinsically disordered proteins, particularly those needing rapid screening tools before expensive simulations, would benefit. The interpretability aspects may also appeal to those developing explainable AI for biological sequence data.
- **Major strengths** The hybrid approach combining sequence and physics-based features is conceptually sound and addresses a real need for fast IDP property prediction. The use of attention mechanisms to weight residue contributions is a thoughtful design choice. The inclusion of SHAP and integrated gradient analyses for model interpretability is a strength, as it moves beyond black-box prediction. The scale of training data (approximately 7000 IDPs) is substantial.
- **Major Concerns** The abstract lacks quantitative performance metrics, making it impossible to evaluate the claimed improvements. The training and evaluation protocol is not described, raising questions about potential data leakage or overfitting. The claim that the framework enables "efficient initial screening" is not supported by runtime or scalability data. The novelty relative to existing IDP prediction tools is not established.
- **Minor Comments** The abstract would benefit from stating the specific performance metrics values. The choice of MobiDB with >99% disorder score is mentioned but the rationale for this threshold is not given. The relationship between the 23 physical features and the three parameters (SCD, SHD, f*) identified by integrated gradients is unclear.
- **Technical failings that need to be addressed before the case is established** R1-M1 (lack of quantitative results), R1-M2 (insufficient methodological detail), R1-M3 (unsubstantiated practical claims)
- **Assessment against Nature-style criteria** Originality: moderate; the combination of attention-based fusion with physics-informed features is not entirely novel but has merit. Scientific importance: potentially high for the IDP community, but not demonstrated from the abstract alone. Interdisciplinary readership: likely to appeal to both ML and biophysics audiences, though the abstract assumes familiarity with IDP-specific terminology. Technical soundness: cannot be assessed without full methods and results. Readability for nonspecialists: the abstract is dense and uses field-specific jargon without sufficient context.
- **Recommendation posture** Currently not established from the provided evidence. The approach is promising, but the abstract does not provide enough information to evaluate the validity of the claims. A full manuscript with detailed methods, results, and comparisons would be required for a supportive assessment.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "This attention-guided fusion significantly improves predictive accuracy across multiple metrics, including mean absolute percentage error and mean squared error"
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract claims significant improvement in predictive accuracy but provides no numerical values, no baseline comparisons, and no statistical significance tests. Without these, the claim of "significant" improvement is unverifiable.
- **Why it matters** The central contribution of the work is the claimed performance gain from the hybrid approach. Without quantitative evidence, readers cannot judge whether the improvement is meaningful or within noise.
- **Resolution test** Provide specific metric values (e.g., MAPE, MSE) for all compared models, with confidence intervals or error bars, and statistical tests (e.g., paired t-tests or Wilcoxon) demonstrating significance.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency
- **Claim pointer** "We trained and evaluated our models on Brownian dynamics (BD) simulation results for approximately 7000 IDPs from the MobiDB database"
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract does not describe how the dataset was split into training, validation, and test sets, whether sequences were clustered to avoid homology bias, or how the BD simulations were generated and validated. The risk of data leakage or overfitting cannot be assessed.
- **Why it matters** Machine learning models for protein properties are highly sensitive to dataset construction. Without clear protocols, the reported performance may not generalize to unseen IDPs.
- **Resolution test** Describe the dataset split strategy, any sequence clustering or redundancy reduction, the simulation protocol, and how the BD model was validated against experimental data.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Claim substantiation
- **Claim pointer** "Our framework provides a fast, interpretable, and scalable tool for predicting IDP behavior, enabling efficient initial screening prior to costly molecular simulations"
- **Evidence pointer** Abstract; location not provided
- **Concern** The claims of "fast" and "scalable" are not supported by any runtime measurements, complexity analysis, or comparison to simulation costs. The practical utility for screening is asserted but not demonstrated.
- **Why it matters** The stated application of the tool is screening before simulations. Without evidence of computational efficiency, this practical claim is speculative.
- **Resolution test** Provide inference time per sequence, scaling behavior with sequence length, and a comparison to the cost of BD simulations or other prediction tools.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract text
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states "23 physical features" and later "the three parameters (SCD and SHD, and charge asymmetry parameter f*)" without clarifying whether these three are among the 23 or additional sequence-derived quantities.
- **Required correction** Clarify the relationship between the 23 features and the three parameters, and define all terms at first use.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Contextualization
- **Affected element** Abstract text
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract does not compare the proposed method to existing IDP property predictors, such as those based on sequence alone or other ML approaches.
- **Required correction** Add a brief statement in the abstract or introduction situating the method relative to prior work.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Abstract text
- **Evidence pointer** Abstract; location not provided
- **Issue** No mention of code or data availability, which is important for a methods-driven paper.
- **Required correction** State whether code and trained models will be made publicly available.

## Risk / unsupported claims
- The claim of "significant" improvement in predictive accuracy is unsupported without quantitative metrics and statistical tests.
- The claim that the framework is "fast" and "scalable" is unsupported without runtime or complexity data.
- The claim that the hybrid biGRU model delivers "the best overall predictive performance" is unverifiable without performance tables.
- The generalizability of the model to IDPs outside the MobiDB training set is not assessable from the abstract.
- The interpretability findings from SHAP and integrated gradient analyses are mentioned but not substantiated with specific results.