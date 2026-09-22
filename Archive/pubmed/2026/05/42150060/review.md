## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no methods, figures, tables, or supplementary material were provided
- **Shared manuscript claim summary** The authors propose that evolutionarily conserved molecular features of intrinsically disordered regions (IDRs) can be used to cluster the human disordered proteome into a functional map, enabling functional annotation, prediction of biomolecular condensate localization, and enrichment analysis of interaction partners and disease-associated proteins.
- **Visible evidence base** Abstract text only; no quantitative results, statistical measures, or methodological details are available
- **Missing materials affecting confidence** Full text, methods section, all figures and tables, supplementary data, statistical analyses, and validation details

## Reviewer
- **Overall assessment** The abstract presents a potentially valuable resource concept for the functional annotation of the human IDR-ome, leveraging conserved molecular features rather than primary sequence. The idea is timely and could be of broad interest. However, the abstract alone provides insufficient evidence to evaluate the robustness, novelty, or generalizability of the clustering approach. Key methodological details, validation metrics, and comparative benchmarks are absent, limiting the ability to assess whether the claims are fully supported.
- **Who would be interested in the results, and why** Researchers in protein biophysics, computational biology, and functional genomics would be interested, particularly those studying intrinsically disordered proteins, biomolecular condensates, and disease genetics. The proposed map could serve as a community resource for hypothesis generation in IDR biology.
- **Major strengths** The conceptual shift from sequence conservation to conserved molecular features is a reasonable and potentially powerful approach for IDR classification. The abstract explicitly connects the map to multiple downstream applications, including condensate localization and disease-risk gene enrichment, which broadens its utility. The emphasis on unknown-function proteins is a forward-looking element that could drive discovery.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria**  
  - Originality: The approach is conceptually original in its use of conserved molecular features for IDR clustering, though similar ideas have been explored in the field of disordered protein prediction. The abstract does not clearly differentiate from prior work.  
  - Scientific importance: The potential to functionally annotate a large fraction of the proteome is significant, but the abstract does not demonstrate the scale or accuracy of the annotations.  
  - Interdisciplinary readership: The topic bridges structural biology, genomics, and bioinformatics, and the abstract is written in a way that is broadly accessible.  
  - Technical soundness: Cannot be assessed from the abstract; no methodological or statistical details are provided.  
  - Readability for nonspecialists: The abstract is clear and avoids excessive jargon, making it accessible to a general scientific audience.
- **Recommendation posture** Currently not established from the provided evidence; supportive if technical concerns are resolved with full data and validation.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors claim that conserved molecular features of IDRs enable clustering of the human IDR-ome into a map with strong functional enrichments.  
- **Evidence pointer** Abstract; location not provided  
- **Concern** The abstract provides no quantitative evidence for the strength of functional enrichments, such as effect sizes, p-values, or enrichment scores. Without these, the claim of "strong" enrichments is unsupported.  
- **Why it matters** The central premise of the manuscript rests on the ability of the clustering to produce meaningful functional associations. If the enrichment is weak or driven by confounding factors, the map's utility is compromised.  
- **Resolution test** Provide enrichment statistics (e.g., adjusted p-values, fold changes) for representative functional terms, and demonstrate that these are robust to alternative clustering parameters or feature sets.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors claim that conserved features of IDRs can predict protein localization to different biomolecular condensates.  
- **Evidence pointer** Abstract; location not provided  
- **Concern** No details are given on the prediction method, training data, or performance metrics (e.g., accuracy, AUC, precision-recall). The claim of predictive ability is therefore not assessable.  
- **Why it matters** Prediction of condensate localization is a specific and testable application. If the predictive performance is not demonstrated, this claim cannot be validated.  
- **Resolution test** Report cross-validated performance metrics for condensate localization prediction, including comparison to baseline models and clarification of the number of condensate types and proteins used.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors claim that conserved features of IDRs underlie elevated intracluster connectivity in condensate-associated IDRs and enrich for short-linear motif-binding domains among interaction partners.  
- **Evidence pointer** Abstract; location not provided  
- **Concern** The abstract does not specify how connectivity or enrichment is measured, nor what statistical thresholds are used. The biological relevance of these observations is unclear without context.  
- **Why it matters** These claims suggest a mechanistic link between IDR features and interaction networks, which is a strong statement. Without supporting data, the link remains speculative.  
- **Resolution test** Provide network analysis details, including how connectivity is defined, the statistical significance of the enrichment, and whether the findings are specific to condensate-associated IDRs versus other IDR subsets.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Originality  
- **Claim pointer** The authors imply that their approach is novel because standard bioinformatics cannot classify IDRs due to limited positional sequence conservation.  
- **Evidence pointer** Abstract; location not provided  
- **Concern** The abstract does not discuss prior efforts to classify IDRs using alternative features, such as amino acid composition, physicochemical properties, or evolutionary rates. The novelty claim is therefore not contextualized.  
- **Why it matters** If similar approaches exist, the manuscript's contribution may be incremental rather than transformative.  
- **Resolution test** Include a brief comparison to existing IDR classification methods and clarify what is uniquely enabled by the conserved-feature approach.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Readability  
- **Affected element** Abstract text  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The term "IDRome" is introduced without definition or context, which may confuse nonspecialist readers.  
- **Required correction** Define "IDRome" at first use, for example, as the complete set of intrinsically disordered regions in the human proteome.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Scientific importance  
- **Affected element** Claim of resource value  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The abstract states the map "should be a valuable resource" but does not indicate how it will be made accessible (e.g., database, web tool, or downloadable data).  
- **Required correction** Specify the intended mode of access for the resource, even briefly, to support the claim of utility.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Technical soundness  
- **Affected element** Prediction of annotations  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The abstract mentions "proteome-wide predictions of annotations for IDRs" for a subset of terms, but the size of this subset and the confidence thresholds are not stated.  
- **Required correction** Provide the number of functional terms predicted and the criteria for assigning predictions, to allow assessment of coverage and reliability.

## Risk / unsupported claims
- The claim of "strong functional enrichments" is unsupported without quantitative statistics.
- The claim of predictive ability for condensate localization is unsupported without performance metrics.
- The claim of elevated intracluster connectivity and enrichment for short-linear motif-binding domains is unsupported without network analysis details.
- The novelty of the approach relative to existing IDR classification methods is not established.
- The resource value of the map is asserted but not substantiated with details on accessibility or validation.