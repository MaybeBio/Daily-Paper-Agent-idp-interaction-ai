## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors report a computational prediction of 56,515 human-fungal pathogen protein-protein interactions (HF-PPIs) between Homo sapiens and Candida albicans, involving 6,830 human and 486 C. albicans proteins. They identify 16 key virulence factors, including SOD1, ERG10, GFA1, and VPS4, as potential therapeutic targets. They further claim that dual RNA-Seq data from infection time points (15, 30, 60, 120, 240 min) show these fungal genes interact with down-regulated human immunomodulatory genes (ADRM1, DAXX, RYBP, SGTA, SRGN), which are enriched in intrinsically disordered regions and thus susceptible to fungal manipulation.
- **Visible evidence base** Abstract text only; no methodological details, validation statistics, or data descriptions are available
- **Missing materials affecting confidence** Full manuscript, methods section, figures, tables, supplementary data, dual RNA-Seq analysis details, interaction prediction parameters, and validation procedures

## Reviewer
- **Overall assessment** The abstract presents a potentially useful computational resource for host-pathogen interaction studies, but the claims as stated cannot be evaluated for technical soundness or biological validity from the supplied material. The central assertion that dual RNA-Seq data demonstrate interactions between fungal virulence factors and down-regulated human genes conflates transcriptional correlation with physical interaction evidence. The scale of predicted interactions (56,515) without described filtering or confidence thresholds raises concerns about false positive rates inherent to homology and domain-based methods. The abstract would benefit from clearer separation of computational predictions from experimental observations.
- **Who would be interested in the results, and why** Researchers studying Candida albicans pathogenesis, host immune evasion mechanisms, fungal virulence factor biology, and computational prediction of host-pathogen interactions. Clinicians and drug developers focused on antifungal therapeutic targets may also find the identified virulence factors relevant, provided the predictions are experimentally validated.
- **Major strengths** The abstract addresses a genuine knowledge gap in H. sapiens-C. albicans PPI data. The integration of computational prediction with dual RNA-Seq expression data represents a reasonable multi-omics approach. The identification of specific virulence factors and human interaction partners provides testable hypotheses for experimental follow-up.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3  
  - R1-m4
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria**  
  Originality: Moderate. Computational PPI prediction for C. albicans is not novel in itself, though the specific integration with dual RNA-Seq time course data may offer some new perspective.  
  Scientific importance: Potentially relevant to fungal pathogenesis and therapeutic development, but the importance depends on whether the predicted interactions are experimentally validated and functionally meaningful.  
  Interdisciplinary readership: The topic bridges computational biology, microbiology, and immunology, which could attract a broad audience if the evidence is robust.  
  Technical soundness: Cannot be assessed from the abstract alone. The lack of methodological detail and validation metrics prevents evaluation of prediction reliability.  
  Readability for nonspecialists: The abstract is generally readable, though terms such as "intrinsically disordered regions" and "pathobiont" may require background knowledge. The logical flow from prediction to experimental evidence is clear but the causal language is problematic.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents an interesting hypothesis-generating resource, but the core claims require substantial additional evidence and methodological transparency before the case is convincing.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence quality  
- **Claim pointer** The abstract states that dual RNA-Seq data show fungal genes "interact with" down-regulated human immunomodulatory genes.  
- **Evidence pointer** Abstract text, location not provided  
- **Concern** The abstract conflates transcriptional co-occurrence or correlation with physical protein-protein interaction. Dual RNA-Seq measures gene expression levels, not protein-protein binding. The claim that fungal genes "interact with" down-regulated human genes based on expression data is not supported by the described methodology.  
- **Why it matters** This is the central integrative claim of the abstract. If the interaction claim is based solely on expression correlation, it is a logical error that undermines the biological interpretation. Physical PPI evidence requires experimental methods such as co-immunoprecipitation, yeast two-hybrid, or at minimum structural prediction with confidence scores.  
- **Resolution test** Clarify whether the dual RNA-Seq data are used only to filter or prioritize computationally predicted PPIs based on co-expression, or whether they are presented as direct evidence of interaction. If the former, rephrase the claim to state that expression data support the relevance of predicted interactions. If the latter, provide experimental interaction data.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The abstract claims 56,515 predicted HF-PPIs involving 6,830 human and 486 C. albicans proteins.  
- **Evidence pointer** Abstract text, location not provided  
- **Concern** No information is provided on the prediction methodology, confidence thresholds, or false positive control. Homology and domain-based methods typically produce large numbers of predictions with high false positive rates. The number 56,515 is presented without any indication of precision, recall, or validation against known interactions.  
- **Why it matters** Without confidence metrics or benchmarking, the predicted interaction set cannot be distinguished from random background. The subsequent identification of 16 virulence factors depends on the reliability of this interaction set. If the set is noisy, the prioritization of specific virulence factors is compromised.  
- **Resolution test** Provide details on the prediction pipeline, including databases used, homology and domain criteria, interaction scores or thresholds, and any benchmarking against known H. sapiens-C. albicans interactions. Report precision and recall if available.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence quality  
- **Claim pointer** The abstract states that human genes ADRM1, DAXX, RYBP, SGTA, and SRGN are "particularly susceptible to fungal manipulation" due to their intrinsically disordered regions.  
- **Evidence pointer** Abstract text, location not provided  
- **Concern** The causal link between intrinsic disorder and susceptibility to fungal manipulation is asserted without evidence. No data are shown demonstrating that these regions are functionally relevant for interaction with fungal proteins, nor that disorder correlates with manipulation in any experimental setting.  
- **Why it matters** This claim extends beyond the data into speculative mechanism. Intrinsically disordered regions are known to mediate protein-protein interactions, but the leap from sequence feature to "susceptibility to fungal manipulation" requires functional validation or at least structural evidence of binding.  
- **Resolution test** Provide evidence that the disordered regions in these human proteins are directly involved in binding to the identified fungal virulence factors, or soften the claim to state that these regions are predicted to be interaction-prone based on disorder propensity.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Completeness  
- **Claim pointer** The abstract claims identification of 16 key virulence factors as potential therapeutic targets.  
- **Evidence pointer** Abstract text, location not provided  
- **Concern** The criteria for defining "key" virulence factors are not stated. It is unclear whether these 16 factors were selected based on network centrality, expression changes, known virulence roles, or a combination of criteria. The abstract lists SOD1, ERG10, GFA1, and VPS4 as examples but does not explain why these are prioritized over other predicted interactors.  
- **Why it matters** The therapeutic target claim depends on the biological relevance of these 16 factors. Without explicit selection criteria, the prioritization appears arbitrary and cannot be reproduced or evaluated.  
- **Resolution test** Describe the prioritization criteria, including any scoring scheme, literature curation, or experimental evidence supporting the virulence role of these 16 factors.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Abstract wording  
- **Evidence pointer** Abstract text, location not provided  
- **Issue** The phrase "project 56,515 human-fungal pathogen protein-protein interactions" uses "project" in an unusual way. The intended meaning is likely "predict" or "infer."  
- **Required correction** Replace "project" with "predict" or "infer" for clarity.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Statistical reporting  
- **Affected element** Dual RNA-Seq analysis  
- **Evidence pointer** Abstract text, location not provided  
- **Issue** The abstract mentions time points (15, 30, 60, 120, 240 min) but does not report the number of biological replicates, differential expression thresholds, or statistical significance criteria used to define "down-regulated."  
- **Required correction** Add brief statistical details, such as fold-change cutoff and adjusted p-value threshold, or refer to methods and supplementary tables.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Terminology  
- **Affected element** "Pathobiont"  
- **Evidence pointer** Abstract text, location not provided  
- **Issue** The term "pathobiont" is used without definition. While common in microbiology, nonspecialist readers may not be familiar with the distinction between pathobiont and opportunistic pathogen.  
- **Required correction** Add a brief parenthetical definition, such as "a commensal organism that can cause disease under certain conditions."

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Scope  
- **Affected element** Abstract conclusion  
- **Evidence pointer** Abstract text, location not provided  
- **Issue** The final sentence claims the work "will improve our knowledge of human-fungal pathogen protein-protein interactions" but does not specify what new biological insight was gained beyond the interaction list itself.  
- **Required correction** State a specific conceptual advance, such as the identification of a network motif, a novel interaction hub, or a mechanistic hypothesis that can be tested.

## Risk / unsupported claims
- The claim that dual RNA-Seq data demonstrate interactions between fungal genes and down-regulated human genes is unsupported and logically conflates expression correlation with physical interaction.
- The claim that human genes with intrinsically disordered regions are "particularly susceptible to fungal manipulation" is unsupported by any functional or structural evidence.
- The claim of 56,515 predicted PPIs is unverifiable without methodological details and confidence metrics.
- The designation of 16 "key virulence factors" as potential therapeutic targets is not justified without explicit selection criteria.
- The overall biological significance of the predicted interaction network cannot be assessed from the abstract alone.