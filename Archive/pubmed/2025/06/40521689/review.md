## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors propose a new method for selecting the beta parameter in variational autoencoders (VAEs) using the Fraction of Variation Explained (FVE) score, and claim that training annealed VAEs at the optimal beta in a single cycle outperforms nonannealed counterparts on folded and intrinsically disordered proteins, as measured by VAMP-2 and GMRQ scores, free energy surfaces, state space discretization, Markov State Models, and contact maps
- **Visible evidence base** Abstract text only; no numerical results, methodological details, or figure/table references are available
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, numerical performance metrics, dataset descriptions, and code or reproducibility details

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting approach to a known limitation in VAE-based protein dynamics modeling, namely the fixed beta value and posterior collapse. The proposed use of FVE to select the optimal beta is plausible and could be a useful contribution. However, the abstract alone provides insufficient evidence to evaluate the validity, robustness, or generalizability of the claims. The performance improvements are stated qualitatively without quantitative support, and key methodological details are absent. The case is not established from the provided material.
- **Who would be interested in the results, and why** Computational chemists, biophysicists, and machine learning researchers working on protein conformational dynamics, dimensionality reduction, and Markov State Models would be interested. The work addresses a practical problem in applying deep generative models to biomolecular simulations, and a systematic beta selection strategy could benefit those using VAEs for molecular systems.
- **Major strengths** The problem is well-motivated and relevant. The proposed FVE-based beta selection is a principled idea that could address a recognized limitation in VAE training. The application to both folded and intrinsically disordered proteins suggests a broad scope of potential applicability.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality is moderate; the FVE-based beta selection is a novel contribution but builds on existing annealing approaches. Scientific importance is potentially high for the computational biophysics community, but the abstract does not demonstrate a transformative advance. Interdisciplinary readership is plausible given the intersection of machine learning and biophysics, but the abstract is written for a specialized audience. Technical soundness cannot be assessed from the abstract alone. Readability for nonspecialists is limited due to heavy use of field-specific jargon without sufficient context.
- **Recommendation posture** Currently not established from the provided evidence. The idea is promising, but the abstract does not provide enough quantitative or methodological detail to support the claims. A full manuscript with detailed methods and results would be required for a supportive assessment.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that annealed VAEs at their optimum beta consistently outperformed nonannealed counterparts, as evident from higher VAMP-2 and GMRQ scores and distinct free energy surface minima.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract states performance improvements but provides no numerical values, statistical significance tests, or comparisons across multiple systems. The terms "consistently outperformed" and "higher scores" are qualitative and cannot be verified without data.
- **Why it matters** The central claim of the work is the performance advantage of the proposed method. Without quantitative evidence, the reader cannot assess the magnitude of improvement, its consistency across systems, or whether the differences are meaningful or within noise.
- **Resolution test** Provide numerical VAMP-2 and GMRQ scores for both annealed and nonannealed VAEs across all tested proteins, including error bars or confidence intervals, and statistical tests demonstrating significance.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological clarity
- **Claim pointer** The authors propose using the FVE score to identify the optimal beta value and state that training annealed VAEs at this optimum in a single cycle is effective.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract does not describe how the FVE score is computed, how the optimal beta is identified from it, what the annealing schedule is, or what "single cycle" means in practice. The relationship between FVE and beta is not explained.
- **Why it matters** Reproducibility is a core requirement for any methodological contribution. Without a clear description of the beta selection procedure and annealing protocol, other researchers cannot implement or validate the approach.
- **Resolution test** Provide a detailed methods section describing the FVE computation, the beta search procedure, the annealing schedule, and the training protocol, with sufficient detail for independent replication.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability and robustness
- **Claim pointer** The authors claim the approach improves state space discretization, refines Markov State Models, and provides more accurate insights into conformational landscapes, as reflected in distinct contact maps, on both folded and intrinsically disordered proteins.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract mentions "both folded and intrinsically disordered proteins" but does not specify how many systems were tested, their diversity, or whether the results are consistent across all of them. The claim of improved contact maps is qualitative and lacks a clear metric for comparison.
- **Why it matters** The generalizability of the method is a key selling point. If the approach only works on a narrow set of systems or shows variable performance, the practical utility is limited. The abstract does not provide enough information to judge the breadth of applicability.
- **Resolution test** Specify the number and types of proteins tested, provide quantitative metrics for state space discretization and contact map accuracy, and show results for each system individually to demonstrate consistency.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Terminology clarity
- **Affected element** "posterior collapse"
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "posterior collapse" is used without definition or context for readers who may not be familiar with VAE training dynamics.
- **Required correction** Add a brief explanation of posterior collapse in the context of VAEs, or provide a reference for the term.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Acronym usage
- **Affected element** "VAMP-2" and "GMRQ"
- **Evidence pointer** Abstract; location not provided
- **Issue** The acronyms VAMP-2 and GMRQ are introduced without expansion or explanation, which may hinder readability for nonspecialists.
- **Required correction** Expand the acronyms at first use and provide a one-sentence description of what each metric measures.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scope of comparison
- **Affected element** "nonannealed counterparts"
- **Evidence pointer** Abstract; location not provided
- **Issue** The comparison is only against nonannealed VAEs. It is unclear whether the proposed method was compared to other annealing strategies or beta selection approaches.
- **Required correction** Clarify whether comparisons were made against other annealing schedules or beta selection methods, and if not, acknowledge this as a limitation.

## Risk / unsupported claims
- The claim that annealed VAEs at optimal beta "consistently outperformed" nonannealed counterparts is unsupported without quantitative data.
- The claim that the approach "provides more accurate insights into conformational landscapes" is unsupported without a defined accuracy metric or ground truth comparison.
- The claim that the method "augment[s] the potential of annealed VAEs in resolving complex conformational landscapes" is speculative and not directly evidenced.
- The generalizability to "both folded and intrinsically disordered proteins" is not assessable without system details and per-system results.