## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors construct a database of phase-separating (PS) and non-PS intrinsically disordered proteins (IDPs), use molecular dynamics (MD) simulations to compute a quantitative "multivalence" value, and report that this simulation-derived metric classifies LLPS propensity with high consistency against experimental observations. They further propose a cutoff for multivalence to distinguish high-LLPS-propensity IDPs, and analyze amino acid type contributions in FUS and its mutants, revealing context-dependent interactions in prion-like and RNA-binding domains.
- **Visible evidence base** Abstract text only; no quantitative results, methodological details, or validation statistics are provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, simulation protocols, force field parameters, database composition and curation criteria, statistical analyses, and comparison datasets

## Reviewer
- **Overall assessment** The abstract presents a potentially valuable computational framework for predicting LLPS propensity from MD-derived multivalence, addressing a topic of broad interest in the IDP and phase separation communities. However, the abstract alone provides insufficient detail to evaluate the validity, robustness, or generalizability of the claims. Key methodological choices, the definition and calculation of multivalence, the nature of the database, and the statistical basis for the proposed cutoff are not described. The claim of "high consistency" with experiments is unquantified. The FUS analysis is mentioned only in passing, with no results or interpretation. The work may be of interest if the full manuscript substantiates these claims, but the current evidence base does not establish the case.
- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation, intrinsically disordered proteins, biomolecular condensates, and computational biophysics. The proposed cost-effective MD-based framework could appeal to those seeking predictive tools for LLPS propensity without extensive experimental screening. The FUS mutational analysis may interest groups focused on neurodegeneration and RNA-binding protein aggregation.
- **Major strengths** The topic is timely and of high relevance. The idea of quantifying multivalence via MD simulations and linking it to LLPS propensity is conceptually appealing and potentially transformative if validated. The inclusion of both PS and non-PS IDPs in a database suggests a systematic approach. The proposed cutoff for multivalence could provide a practical guideline for the community.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
  - R1-M4
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1 (definition and calculation of multivalence), R1-M2 (unquantified classification accuracy), R1-M3 (cutoff derivation and validation), R1-M4 (FUS analysis incompletely reported)
- **Assessment against Nature-style criteria** Originality: The concept of using MD-derived multivalence as a quantitative predictor of LLPS propensity appears novel, though the abstract does not clarify how it differs from existing sequence-based predictors. Scientific importance: Potentially high, as a reliable computational predictor would accelerate LLPS research, but importance cannot be fully assessed without validation details. Interdisciplinary readership: The topic bridges biophysics, computational chemistry, and cell biology, and the abstract is written accessibly for a broad audience. Technical soundness: Cannot be evaluated from the abstract; no methodological details, error estimates, or validation statistics are provided. Readability for nonspecialists: The abstract is clear and well-structured, with minimal jargon, though terms like "multivalence" and "graph theoretical approach" are introduced without definition.
- **Recommendation posture** Currently not established from the provided evidence. The abstract describes a promising framework, but the absence of quantitative results, methodological transparency, and validation details prevents a supportive recommendation. A revised assessment would require the full manuscript.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "we introduced a framework to calculate the exact value of multivalence with molecular dynamics (MD) simulations"
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract claims the calculation of an "exact value of multivalence" but provides no definition of multivalence in this context, no description of how it is derived from MD simulations, and no indication of the simulation protocol (e.g., force field, system size, sampling time, number of replicas). The term "exact" is particularly problematic without a clear operational definition and error analysis.
- **Why it matters** Multivalence is the central metric of the proposed framework. If its definition or calculation is ambiguous, non-reproducible, or system-dependent, the entire classification scheme collapses. The claim of "exact" calculation raises the bar for precision and requires explicit validation.
- **Resolution test** Provide a precise mathematical definition of multivalence, describe the MD simulation setup in full, and demonstrate convergence and reproducibility of the calculated values across independent simulations and system sizes.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** "the simulation-based classification of the LLPS propensity can achieve high consistency with experimental observations despite varying experimental conditions"
- **Evidence pointer** Abstract, location not provided
- **Concern** The claim of "high consistency" is unquantified. No accuracy, sensitivity, specificity, or correlation coefficients are reported. The phrase "despite varying experimental conditions" suggests robustness, but no details on the range of conditions, the number of proteins compared, or the criteria for experimental PS/non-PS assignment are given.
- **Why it matters** Without quantitative metrics, the reader cannot judge whether the consistency is statistically meaningful or merely anecdotal. The claim is central to the paper's contribution and must be supported by rigorous benchmarking against a well-defined experimental reference set.
- **Resolution test** Report confusion matrix, accuracy, precision, recall, F1 score, or ROC-AUC for the classification against experimental data, and specify the experimental criteria and dataset size.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "inspired by a graph theoretical approach, we determined a recommended cutoff of multivalence for effectively differentiating IDPs with a high LLPS propensity"
- **Evidence pointer** Abstract, location not provided
- **Concern** The derivation of the multivalence cutoff is not described. The connection to graph theory is mentioned but not explained. No information is given on how the cutoff was optimized, whether it was validated on an independent dataset, or how sensitive the classification is to the choice of cutoff.
- **Why it matters** A cutoff is only useful if it is robust and generalizable. Without details on its derivation and validation, the recommended value may be overfitted to the specific database and may not transfer to other IDP sets.
- **Resolution test** Describe the graph-theoretical method, show the optimization procedure, and validate the cutoff on a held-out or independent dataset with sensitivity analysis.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Completeness
- **Claim pointer** "studies on the role of amino acid types in the fused in sarcoma (FUS) protein and its mutants reveal context-dependent interactions in prion-like and RNA-binding domains"
- **Evidence pointer** Abstract, location not provided
- **Concern** The FUS analysis is mentioned as a final point but no results, specific mutants, or interaction patterns are described. The claim of "context-dependent interactions" is vague and cannot be evaluated.
- **Why it matters** This section appears to be a secondary contribution. If it is meant to provide mechanistic insight, the abstract should at least summarize the key findings. As written, it adds little to the main claim and may distract from the core framework.
- **Resolution test** Provide a concise summary of the FUS results, including which mutants were studied, what interactions were identified, and how they relate to LLPS propensity.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract, first sentence
- **Evidence pointer** Abstract, location not provided
- **Issue** The opening sentence references P-granules in C. elegans as a historical anchor, but this is well-known background and does not add value to the abstract.
- **Required correction** Consider removing or shortening this sentence to focus on the novel contribution.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract, "multivalence"
- **Evidence pointer** Abstract, location not provided
- **Issue** The term "multivalence" is used without definition. It may be confused with "valency" in chemistry or "multivalency" in biology.
- **Required correction** Define multivalence explicitly in the abstract or use a more standard term with a brief operational definition.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Abstract, database description
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract states "we constructed a comprehensive database of PS and non-PS IDPs" but gives no information on database size, source, or curation criteria.
- **Required correction** Add a sentence describing the number of proteins, their sources, and how PS/non-PS status was assigned.

## Risk / unsupported claims
- The claim of "high consistency" with experimental observations is unsupported without quantitative metrics.
- The claim of calculating an "exact value of multivalence" is unsupported without a definition and convergence analysis.
- The "recommended cutoff" for multivalence is unsupported without derivation and validation details.
- The FUS analysis claim of "context-dependent interactions" is unsupported without specific results.
- The overall utility of the framework as "cost-effective" is not assessable without runtime or resource comparisons.