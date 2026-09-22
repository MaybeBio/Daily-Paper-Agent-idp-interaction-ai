## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no figures, tables, methods details, or supplementary materials were provided
- **Shared manuscript claim summary** The authors propose DeepUMQA-PA, a physical-aware deep learning method for residue-wise quality estimation of protein complex models. The method uses Voronoi tessellation-derived contact area and orientation features, geometry-based features, protein language model embeddings, and knowledge-based statistical potentials, fed into a fused graph neural network and ResNet architecture. Reported results on CASP15 show improvements over DeepUMQA3 in Pearson and Spearman correlations, notable gains on nanobody-antigen complexes, and favorable MAE scores compared to AlphaFold-Multimer and AlphaFold3 self-assessment on a subset of targets.
- **Visible evidence base** Abstract text only; no numerical tables, figures, method descriptions, or statistical details are available
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, dataset definitions, baseline implementation details, statistical significance tests, and server validation details

## Reviewer
- **Overall assessment** The abstract presents a potentially valuable contribution to the field of protein complex model quality assessment, with a novel emphasis on physical contact features derived from Voronoi tessellation. The reported performance gains, particularly on nanobody-antigen complexes, are intriguing. However, the abstract alone provides insufficient detail to evaluate the methodological soundness, statistical robustness, or generalizability of the claims. Several key aspects, including dataset composition, baseline fairness, and significance testing, are not assessable from the supplied material.
- **Who would be interested in the results, and why** Structural biologists and computational biologists working on protein complex prediction and model quality assessment would be the primary audience. Developers of deep learning methods for structural biology, particularly those focused on multimer modeling and confidence estimation, would find the physical-aware feature engineering approach relevant. The reported improvements on nanobody-antigen complexes may also interest researchers in therapeutic antibody development.
- **Major strengths** The proposed method introduces a novel combination of physical contact features with deep learning architectures, addressing a recognized gap in model quality estimation for protein complexes. The reported performance improvements over an established state-of-the-art method, DeepUMQA3, are notable. The specific focus on nanobody-antigen complexes, where flexibility poses challenges, suggests a targeted and potentially impactful application.
- **Major Concerns**  
  - **Concern ID** R1-M1  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Statistical robustness  
  - **Claim pointer** The abstract claims that DeepUMQA-PA outperforms DeepUMQA3 by 3.69% and 3.49% on Pearson and Spearman correlations, respectively, on the CASP15 test set.  
  - **Evidence pointer** Abstract, results section; location not provided  
  - **Concern** The abstract reports percentage improvements but does not provide absolute correlation values, sample sizes, confidence intervals, or statistical significance tests. Without these, it is impossible to determine whether the observed differences are meaningful or within noise.  
  - **Why it matters** Quality assessment methods are compared on their ability to rank models accurately; small percentage differences may not be practically significant, and the absence of significance testing undermines the strength of the claim.  
  - **Resolution test** Provide absolute Pearson and Spearman values for both methods, the number of targets used, and appropriate statistical tests (e.g., bootstrap or permutation tests) with reported p-values or confidence intervals.  
  - **Concern ID** R1-M2  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Dataset and baseline comparability  
  - **Claim pointer** The abstract states that DeepUMQA-PA achieved better MAE scores than AlphaFold-Multimer and AlphaFold3 self-assessment methods on 43% and 50% of targets, respectively.  
  - **Evidence pointer** Abstract, results section; location not provided  
  - **Concern** The abstract does not specify the target set used for this comparison, the criteria for selecting targets, or whether the same models were evaluated by all methods. Self-assessment methods may have been applied to different model sets, making the comparison potentially unfair or confounded.  
  - **Why it matters** Without a clearly defined and consistent evaluation protocol, the reported MAE improvements cannot be interpreted as evidence of general superiority.  
  - **Resolution test** Clearly define the target set, describe how models were generated or selected for each method, and ensure identical evaluation conditions across all compared methods.  
  - **Concern ID** R1-M3  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Methodological reproducibility  
  - **Claim pointer** The abstract describes the feature construction using Voronoi tessellation and the fused network architecture with equivalent graph neural network and ResNet.  
  - **Evidence pointer** Abstract, methods summary; location not provided  
  - **Concern** The abstract provides only a high-level description of the method. Critical details, such as the exact definition of contact area and orientation features, the architecture parameters, training procedure, and hyperparameter choices, are not available.  
  - **Why it matters** Reproducibility is a core requirement for computational methods. Without detailed methodological information, independent validation and further development by the community are not possible.  
  - **Resolution test** Provide a full methods section with precise feature definitions, architecture specifications, training details, and code availability.  
  - **Concern ID** R1-M4  
  - **Severity** Major  
  - **Blocking** No  
  - **Axis** Generalizability  
  - **Claim pointer** The abstract suggests that physical-aware information has the potential to capture sequence-structure-quality relationships, especially for flexible proteins.  
  - **Evidence pointer** Abstract, discussion; location not provided  
  - **Concern** The claim about flexible proteins is based on the nanobody-antigen results, but the abstract does not provide a quantitative definition of flexibility or demonstrate that the improvement is specifically attributable to flexibility rather than other properties of these complexes.  
  - **Why it matters** Overgeneralizing from a specific case to a broad principle without mechanistic evidence weakens the scientific contribution.  
  - **Resolution test** Provide a quantitative analysis linking performance gains to flexibility measures, or temper the claim to reflect the specific observations.
- **Minor Comments**  
  - **Concern ID** R1-m1  
  - **Severity** Minor  
  - **Axis** Clarity  
  - **Affected element** Abstract, methods summary  
  - **Evidence pointer** Abstract, methods section; location not provided  
  - **Issue** The term "equivalent graph neural network" is ambiguous and may be a typographical or translation error.  
  - **Required correction** Clarify the intended architecture name, likely "equivariant graph neural network," and ensure consistent terminology throughout.  
  - **Concern ID** R1-m2  
  - **Severity** Minor  
  - **Axis** Completeness  
  - **Affected element** Abstract, results  
  - **Evidence pointer** Abstract, results section; location not provided  
  - **Issue** The abstract does not report the number of targets in the CASR15 test set or the nanobody-antigen subset, which limits the reader's ability to contextualize the results.  
  - **Required correction** Include target counts for all reported evaluations.  
  - **Concern ID** R1-m3  
  - **Severity** Minor  
  - **Axis** Accessibility  
  - **Affected element** Abstract, server availability  
  - **Evidence pointer** Abstract, last sentence  
  - **Issue** The server URL is provided, but there is no indication of whether the server is functional, what inputs are accepted, or any usage limitations.  
  - **Required correction** Add a brief description of server functionality and any access restrictions, or note that details are in the full manuscript.
- **Technical failings that need to be addressed before the case is established** R1-M1 (statistical robustness), R1-M2 (dataset and baseline comparability), R1-M3 (methodological reproducibility). These are blocking because the core claims of performance improvement and method novelty cannot be verified from the abstract alone.

## Assessment against Nature-style criteria
- **Originality** The combination of Voronoi tessellation-derived physical contact features with deep learning for complex quality assessment appears novel, but the abstract does not provide enough context to distinguish it from prior work in the field.  
- **Scientific importance** Protein complex quality assessment is a timely and important problem, and the reported gains on nanobody-antigen complexes could have practical implications. However, the importance is not fully established without robust statistical evidence.  
- **Interdisciplinary readership** The topic bridges structural biology, computational biology, and machine learning, and the abstract is written in a way that is broadly accessible to these communities.  
- **Technical soundness** The technical approach is plausible, but the abstract lacks the detail needed to assess soundness. The absence of statistical rigor and evaluation protocol details is a significant concern.  
- **Readability for nonspecialists** The abstract is generally clear, though some terms (e.g., "equivalent graph neural network") may confuse nonspecialists. The physical intuition behind the features is conveyed effectively.

## Recommendation posture
Currently not established from the provided evidence. The abstract presents an interesting idea and promising preliminary results, but the lack of statistical detail, unclear evaluation protocols, and insufficient methodological description prevent a definitive assessment. The authors should provide the full manuscript with detailed methods, complete results, and significance testing before the claims can be evaluated.

## Risk / unsupported claims
- The claim of outperforming DeepUMQA3 by specific percentages is unsupported without absolute values and significance tests.  
- The claim of better MAE scores than AlphaFold-Multimer and AlphaFold3 on 43% and 50% of targets is unverifiable without target set definition and evaluation protocol details.  
- The claim that physical-aware information captures sequence-structure-quality relationships, especially for flexible proteins, is not supported by direct evidence in the abstract.  
- The generalizability of the method beyond CASP15 targets is not assessable from the supplied material.