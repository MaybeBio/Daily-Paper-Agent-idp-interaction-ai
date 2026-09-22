## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, conclusions, and methods.
- **Assessment boundary** Scientific claims, methodology, data interpretation, and internal consistency as presented in the provided text. No external data or supplementary files were available for verification.
- **Shared manuscript claim summary** The authors propose that the overlap between compositionally biased regions (CBRs) and intrinsically disordered regions (IDRs) in human proteins is functionally informative. They report that two-thirds of IDR residues overlap CBRs, that CBR types differ in their degree and position of overlap with IDRs, that CBR-IDR overlaps are enriched in nuclear proteins and in proteins involved in liquid-liquid phase separation (LLPS), and that analysis of protein interaction networks suggests distinct functional modes for S/P-rich and E-rich CBRs.
- **Visible evidence base** Main text figures (Figures 1–7), Table 1, Table 2, and methodological descriptions. Supplementary files S1–S3 are referenced but not provided.
- **Missing materials affecting confidence** Supplementary Files S1, S2, and S3; full statistical outputs; details of the FuzDrop and DIBS data processing; exact definitions of overlap categories used in Figure 4; and the complete list of hub proteins and enrichment results.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and relevant question in the field of intrinsically disordered proteins, namely whether composition bias can serve as a functional classifier for IDRs. The authors present a systematic, genome-scale analysis in the human proteome and identify several potentially interesting patterns, including type-specific overlap behaviors and enrichment in LLPS-associated proteins. However, the current evidence base is largely descriptive and correlational, and several key claims are not fully supported by the analyses as described. The mechanistic interpretations, particularly regarding protein interaction networks and the functional role of specific CBR types, require stronger statistical and structural support. The manuscript is clearly written and accessible, but the depth of analysis and the robustness of the conclusions need improvement before the case is fully established.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, protein evolution, phase separation, and protein interaction networks would find this work relevant. The proposed link between CBR types and IDR function could inform experimental design for mutational or functional studies. The paper may also be of interest to bioinformaticians developing predictors of protein function from sequence features.
- **Major strengths** The study addresses a significant gap in the field by systematically exploring the relationship between CBRs and IDRs at proteome scale. The use of two independent disorder prediction methods (IUPred2a and MobiDB-lite) and the consistency of results across them is a notable strength. The classification of CBR types by overlap behavior is a useful conceptual framework. The analysis of LLPS drivers and the nuclear enrichment finding provide potentially valuable biological context.
- **Major Concerns** The concerns below identify issues with statistical rigor, interpretative depth, and the strength of the evidence for the central claims.
- **Minor Comments** Several smaller issues regarding presentation, clarity, and methodological detail are listed below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5.
- **Assessment against Nature-style criteria**  
  *Originality*: The question of CBR-IDR overlap is not entirely new, but the systematic, type-resolved analysis at the human proteome level offers a fresh perspective. The study is moderately original.  
  *Scientific importance*: The findings could have implications for understanding IDR function and evolution, but the current descriptive level limits the immediate impact. The importance is moderate and would be enhanced by stronger mechanistic evidence.  
  *Interdisciplinary readership*: The topic bridges protein biophysics, bioinformatics, and cell biology. The paper is likely to appeal to a specialized audience rather than a broad interdisciplinary one.  
  *Technical soundness*: The methods are generally appropriate, but several analyses lack statistical rigor or clear controls, and some interpretations exceed what the data can support.  
  *Readability for nonspecialists*: The manuscript is well written and the main concepts are explained clearly. However, the density of results and the lack of a clear take-home message for a general reader may limit accessibility.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the data are potentially valuable, but the current manuscript does not fully establish the central claims. Major revisions are required to strengthen the statistical basis, clarify the functional interpretations, and address the identified technical issues.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Statistical rigor  
- **Claim pointer** The authors claim that "CBRs overlap more often IDRs in nuclear proteins and in proteins involved in liquid-liquid phase separation (LLPS)" and that "the enrichment of CBRs in IDRs by tandem repetition of short linear motifs (rich in S or P), and the existence of E-rich polar regions that could support specific protein interactions with non-specific interactions."  
- **Evidence pointer** Section 2.3, Section 2.4, Figure 6, Figure 7, Table 2  
- **Concern** The enrichment analyses for hub interactors and LLPS drivers rely on Fisher's exact tests with a p-value threshold of 0.05, but no correction for multiple testing is described. Given the large number of comparisons (many CBR types across many hubs), the false positive rate is likely to be substantial. Additionally, the selection of the 153 and 49 pairs in Table 2 is not clearly justified, and the criteria for "improved enrichment" in the stricter hub dataset are not defined. The LLPS analysis compares predicted drivers to non-drivers, but the two groups may differ in many confounding properties (e.g., protein length, expression level) that are not controlled for.  
- **Why it matters** The central claims of functional enrichment and interaction specificity depend on these statistical tests. Without proper multiple testing correction and control for confounders, the reported associations may be spurious, undermining the main conclusions.  
- **Resolution test** The authors should apply a multiple testing correction (e.g., Benjamini-Hochberg) to all enrichment tests and report adjusted p-values. They should also provide a clear definition of "improved enrichment" and justify the selection of the 153 and 49 pairs. For the LLPS comparison, they should include appropriate controls (e.g., matching by protein length or expression) or use a regression framework that adjusts for potential confounders.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Interpretative depth  
- **Claim pointer** The authors state that "the most prominent functions that can be assigned have to do with the organization of cellular compartments and protein interactions" and that "the position of CBRs within proteins and relative to each other is not strongly associated with function."  
- **Evidence pointer** Section 2.2, Section 2.4, Figure 4, Figure 7  
- **Concern** The conclusion that position is not strongly associated with function is based on a descriptive analysis of overlap categories (Figure 4) without any statistical test comparing the distribution of overlap types across functional categories. The nuclear enrichment finding (Figure 7) is based on a simple comparison of four broad cellular compartments, which may obscure more nuanced functional differences. The claim that "position is not strongly associated with function" is a negative result that requires a power analysis or at least a demonstration that the analysis would be able to detect such an association if it existed.  
- **Why it matters** The authors use this negative result to argue that composition bias, rather than position, is the key functional determinant. If the analysis is underpowered or confounded, this conclusion is not reliable.  
- **Resolution test** The authors should perform a statistical comparison of overlap positions across functional categories (e.g., Gene Ontology terms) and report effect sizes and confidence intervals. They should also discuss the statistical power of their analysis to detect positional effects, or temper their conclusion accordingly.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence strength  
- **Claim pointer** The authors claim that "the interaction of SUMO1 with an IDR in the E3 SUMO-protein ligase PIAS2" and "the interaction of TSG101 with a fragment of Hrs" and "the interaction of Mob1 with STK3" illustrate distinct functional modes of CBR-mediated interactions.  
- **Evidence pointer** Section 2.3, Table 2, Figure 5  
- **Concern** The three case studies are presented as evidence for functional modes, but the reasoning is largely anecdotal. For the S-rich CBR in PIAS2, the authors note that the interacting motif is not serine-rich and that nearby phosphorylation sites may be relevant, but no direct evidence links the S-rich composition to the interaction. For the P-rich CBR in Hrs, the presence of a proline-rich motif is noted, but the broader P-rich region is not shown to be necessary for binding. For the E-rich CBR in Mst2, the authors speculate that the negatively charged region aids non-specific localization, but this is not tested. The selection of these three cases from the 49 identified is not justified, and it is unclear whether they are representative.  
- **Why it matters** These case studies are used to support the central claim that CBR types have distinct functional roles. If the examples are not representative or the interpretations are speculative, the claim is weakened.  
- **Resolution test** The authors should either provide a systematic analysis of the 49 cases (e.g., testing whether the CBR type correlates with the position of the interacting motif or with the presence of known motifs) or clearly label the case studies as illustrative hypotheses that require experimental validation. They should also justify the selection of the three cases.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Methodological clarity  
- **Claim pointer** The authors state that "we computed CBRs and IDRs for all human proteins using two well accepted methods: CAST and IUPred2a, with default parameters, as well as the disorder predictions made with MobiDB-lite."  
- **Evidence pointer** Section 2, Section 4  
- **Concern** The description of the CBR definition is incomplete. The authors state that CBRs are "regions with at least one enriched amino acid," but the criteria for "enriched" are not specified beyond the use of CAST. It is unclear whether a CBR is defined by a single enriched amino acid type or whether regions with multiple enriched types are handled differently. The overlap analysis appears to treat each CBR as belonging to a single type, but the method for assigning a type when multiple amino acids are enriched is not described. Additionally, the threshold for considering a CBR as overlapping an IDR (e.g., minimum fraction of overlap) is not stated.  
- **Why it matters** The reproducibility of the analysis depends on a precise definition of CBRs and the overlap criteria. Without this information, the results cannot be independently verified or compared with other studies.  
- **Resolution test** The authors should provide a detailed description of the CBR definition, including the enrichment criteria, the handling of multi-enriched regions, and the overlap threshold used. This should be added to the Methods section.

- **Concern ID** R1-M5  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Data availability  
- **Claim pointer** The authors reference Supplementary Files S1, S2, and S3 as the source of detailed results, including the full list of CBRs, enrichment results, and the 153 pairs of hubs and interactors.  
- **Evidence pointer** Section 2, Section 4  
- **Concern** The supplementary files are not provided for review. The main text relies heavily on these files for the completeness of the results, particularly for the enrichment analyses and the case studies. Without access to these data, the claims cannot be fully evaluated.  
- **Why it matters** The availability of the underlying data is essential for assessing the validity of the statistical analyses and the representativeness of the presented examples.  
- **Resolution test** The authors should provide the supplementary files as part of the review process, or at minimum, include the key summary statistics in the main text or an appendix.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Abstract  
- **Evidence pointer** Abstract  
- **Issue** The abstract states that "a total of 2/3 of residues in IDRs overlap CBRs," but it is not clear whether this fraction is computed over all IDR residues or only those in IDRs that overlap at least one CBR.  
- **Required correction** Clarify the denominator in the abstract or in the corresponding results section.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Presentation  
- **Affected element** Figure 3  
- **Evidence pointer** Figure 3  
- **Issue** The three groups of CBR types defined by overlap extent are described in the text, but the figure does not clearly indicate the grouping boundaries.  
- **Required correction** Add visual indicators or a legend to Figure 3 to show the grouping of CBR types.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Terminology  
- **Affected element** Section 2.1  
- **Evidence pointer** Section 2.1  
- **Issue** The term "overlap length" is used, but it is not defined whether this refers to the fraction of the CBR covered by the IDR, the fraction of the IDR covered by the CBR, or the absolute number of overlapping residues.  
- **Required correction** Define "overlap length" explicitly in the Methods or in the figure legend.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Section 2.3  
- **Evidence pointer** Section 2.3  
- **Issue** The analysis of hub interactors is described, but the number of hubs tested and the total number of significant enrichments (before the stricter selection) are not reported.  
- **Required correction** Report the total number of hubs and the number of significant enrichments at each stage of the filtering process.

- **Concern ID** R1-m5  
- **Severity** Minor  
- **Axis** Interpretation  
- **Affected element** Section 2.4  
- **Evidence pointer** Figure 6  
- **Issue** The comparison between predicted and experimentally verified LLPS drivers is interesting, but the authors do not discuss the potential differences in how these two sets were defined and how that might affect the observed overlap patterns.  
- **Required correction** Add a brief discussion of the potential biases in the two LLPS datasets and how they might influence the results.

## Risk / unsupported claims
- The claim that "there is selection pressure against those CBR types" that do not overlap IDRs is speculative and not directly tested. No evolutionary analysis is presented to support this claim.
- The claim that "the position of CBRs within proteins and relative to each other is not strongly associated with function" is a negative result that is not supported by a formal statistical analysis.
- The functional interpretations of the three case studies (S-rich, P-rich, E-rich) are speculative and not experimentally validated.
- The claim that "the nucleus is enriched in proteins with higher overlap of CBRs and IDRs" is based on a simple categorical comparison and may be confounded by other protein properties.
- The statement that "the results and conclusions produced were independent of the disorder prediction tool used" is only supported by a general statement and not by a detailed comparison of the two prediction methods across all analyses.