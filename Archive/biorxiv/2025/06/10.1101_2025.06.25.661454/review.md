## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract
- **Shared manuscript claim summary** The authors introduce bAIes, an integrative method combining physics-based force fields with data-driven predictions via Bayesian inference, and claim it outperforms both AlphaFold2 and molecular dynamics-refined models in discriminating binders from non-binders in virtual screening campaigns.
- **Visible evidence base** Abstract text only
- **Missing materials affecting confidence** Full manuscript, methods, figures, tables, validation datasets, benchmark details, statistical analyses, and code availability

## Reviewer
- **Overall assessment** The abstract presents a potentially valuable methodological contribution to structure-based drug discovery. The concept of integrating AlphaFold2 models with physics-based refinement through Bayesian inference is timely and addresses a recognized limitation in the field. However, the abstract provides insufficient detail to evaluate the validity, robustness, and generalizability of the claimed performance improvements. The central claim of superior binder discrimination is presented without quantitative support, benchmark context, or methodological transparency.
- **Who would be interested in the results, and why** Computational chemists, structural biologists, and drug discovery researchers would be interested in this work. The method addresses a practical bottleneck in virtual screening workflows, namely the limited utility of AlphaFold2 models for small molecule docking. If validated, the approach could be adopted by both academic and industrial groups seeking to improve screening accuracy without extensive computational resources.
- **Major strengths** The abstract identifies a clear and well-recognized problem in the field. The proposed solution is conceptually elegant, combining complementary strengths of physics-based and data-driven approaches. The stated goal of improving AlphaFold2 usability without requiring extensive resources is practically relevant and potentially impactful.
- **Major Concerns** The abstract lacks quantitative results, benchmark details, and methodological specifics. The central performance claim is unsupported by any reported metrics, comparison baselines, or dataset descriptions. The scope of validation is unclear, including the number of targets, protein families, and ligand sets tested.
- **Minor Comments** The abstract would benefit from clarifying the specific Bayesian inference framework used and how it integrates force field information with AlphaFold2 predictions. The term "bAIes" is introduced without explanation of its derivation. The abstract does not specify the computational cost of the method relative to alternatives.
- **Technical failings that need to be addressed before the case is established** The absence of any quantitative performance data in the abstract prevents assessment of the central claim. No benchmark details, statistical measures, or comparison protocols are provided.
- **Assessment against Nature-style criteria** Originality is plausible given the integrative approach, but cannot be fully assessed from the abstract alone. Scientific importance is potentially high if the claims hold, as the method addresses a widely acknowledged limitation. Interdisciplinary readership is likely, spanning computational biology, chemistry, and drug discovery. Technical soundness cannot be evaluated without methodological details and validation data. Readability for nonspecialists is adequate, though some technical terms could be clarified.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "bAIes demonstrates a superior ability to discriminate between binders and non-binders in virtual screening campaigns, outperforming both AlphaFold2 and molecular dynamics-refined models"
- **Evidence pointer** Abstract, location not provided
- **Concern** The central performance claim is presented without any quantitative data. No enrichment factors, AUC values, hit rates, or other standard virtual screening metrics are reported. No information is given about the number of targets, ligand libraries, or decoy sets used in the evaluation.
- **Why it matters** Without quantitative benchmarks, the claimed superiority cannot be assessed for statistical significance, practical relevance, or generalizability. The claim may be based on limited or favorable test cases, and the abstract provides no basis for judging the robustness of the result.
- **Resolution test** Provide quantitative performance metrics from benchmark evaluations, including comparison against appropriate baselines, with statistical significance measures and details of the datasets used.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency
- **Claim pointer** "combining physics-based force fields with data-driven predictions through Bayesian inference"
- **Evidence pointer** Abstract, location not provided
- **Concern** The methodological description is too vague to understand what the method actually does. The nature of the Bayesian inference, the specific force fields used, how AlphaFold2 predictions are incorporated, and the relationship between the physics-based and data-driven components are not described.
- **Why it matters** Reproducibility and scientific evaluation require a clear understanding of the method. Without this information, readers cannot assess whether the approach is novel, technically sound, or practically implementable.
- **Resolution test** Provide a detailed methods description in the full manuscript, including the Bayesian framework, force field parameters, integration strategy, and implementation details.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scope of validation
- **Claim pointer** "outperforming both AlphaFold2 and molecular dynamics-refined models"
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract does not specify the breadth of the validation. It is unclear how many protein targets were tested, whether they represent diverse families, and whether the results are consistent across different binding site types and ligand chemistries.
- **Why it matters** Performance claims based on a narrow test set may not generalize. The utility of the method for drug discovery depends on its applicability across a wide range of targets and screening scenarios.
- **Resolution test** Report the number and diversity of targets and ligand sets used in validation, and discuss any cases where the method underperforms relative to baselines.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Method name
- **Evidence pointer** Abstract, location not provided
- **Issue** The name "bAIes" is introduced without explanation of its meaning or derivation.
- **Required correction** Provide a brief explanation of the name or a full expansion of the acronym.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Computational cost
- **Affected element** Resource requirements
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract claims the method does not require "extensive computational resources" but provides no information on actual runtime or resource demands relative to alternatives.
- **Required correction** Include a statement on computational cost, ideally with a comparison to AlphaFold2 and MD-based refinement approaches.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Molecular dynamics-refined models"
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract does not specify the MD simulation length, force field, or refinement protocol used for the comparison baseline.
- **Required correction** Clarify the MD refinement protocol used for the baseline comparison to ensure a fair and interpretable benchmark.

## Risk / unsupported claims
- The claim of superior binder discrimination is unsupported by any quantitative data in the abstract.
- The claim of outperforming both AlphaFold2 and MD-refined models cannot be evaluated without benchmark details.
- The claim that the method does not require extensive resources is unsubstantiated without computational cost data.
- The generalizability of the method across diverse targets and screening scenarios is not assessable from the abstract.