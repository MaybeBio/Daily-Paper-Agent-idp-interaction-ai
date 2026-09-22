## Review setup
- **Input scope** Full manuscript text, including Introduction, Materials and methods, Results, Discussion, and Supplementary Information references
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided manuscript
- **Shared manuscript claim summary** The authors characterize 18 yeast transcriptional repressor proteins for their ability to interact with the pleiotropic corepressors Sin3, Cyc8, and Tup1, map minimal repression domains for several repressors, and analyze sequence features and structural predictions of these domains
- **Visible evidence base** In vitro GST pull-down interaction assays, in vivo lexA-based repression assays, site-directed mutagenesis of Yox1, sequence compilation in Table 2, and AlphaFold structural predictions in Supplementary Figure 2
- **Missing materials affecting confidence** Supplementary Tables S1-S3, Supplementary Figures 1-2, raw data for pull-down assays, full plasmid details, and statistical analysis details were not available for review

## Reviewer
- **Overall assessment** This manuscript presents a systematic survey of repressor-corepressor interactions in S. cerevisiae, expanding the known interaction network and providing new mapping data for several repressors. The work is descriptive and largely confirmatory, extending previous findings for Opi1 and alpha2 to a broader set of repressors. The identification of a minimal functional domain in Yox1 with mutational validation is the most novel contribution. However, the mechanistic insight is limited, and the claim that corepressor interaction domains are intrinsically disordered is speculative and not directly tested. The comparative sequence analysis is useful but does not yield a clear consensus motif, which the authors acknowledge. Overall, the study is solid but incremental, with several technical concerns that need addressing.

- **Who would be interested in the results, and why** Researchers studying transcriptional repression mechanisms in yeast, particularly those focused on corepressor complexes (Sin3/Rpd3, Cyc8-Tup1) and their recruitment by pathway-specific repressors. The compiled list of corepressor interaction domains (Table 2) will serve as a useful reference for the yeast transcription community. Those interested in intrinsically disordered regions in transcriptional regulation may also find the discussion relevant, though the evidence is indirect.

- **Major strengths** 
  1. Systematic and comprehensive interaction survey covering 18 repressors across three corepressors, providing a useful network map
  2. Detailed mapping of minimal repression domains for multiple repressors, with Yox1 being the most thoroughly characterized
  3. Mutational analysis of Yox1 provides functional validation of the mapped domain
  4. Compilation of 16 corepressor interaction domain sequences (Table 2) is a valuable resource
  5. Clear demonstration that many repressors interact with multiple corepressors, supporting functional redundancy

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "13 out of 18 repressor proteins were able to interact with Cyc8, 12 with Sin3 and 11 with Tup1" and that specific repressors bind to three, two, or one corepressor(s)
- **Evidence pointer** Figure 1, Results section "Pathway-specific repressor proteins are able to physically interact with pleiotropic corepressors Sin3, Cyc8 and Tup1"
- **Concern** The pull-down assays are presented as a binary positive/negative readout, but no quantitative data, loading controls, or replicates are shown. The figure legend mentions "SD" but no statistical analysis is described. For a survey claiming to establish interaction patterns, the lack of quantitative assessment and replicate information is a significant limitation. Additionally, the use of bacterial extracts for both bait and prey proteins, while demonstrating direct interactions, may not reflect physiologically relevant conditions (e.g., post-translational modifications, proper folding, or chaperone requirements).
- **Why it matters** The central claim of the paper, that specific repressors interact with specific corepressors, rests entirely on these pull-down results. Without quantitative data or replicates, the reliability of the interaction matrix cannot be assessed. False negatives due to protein misfolding in E. coli or false positives due to non-specific binding could substantially alter the conclusions.
- **Resolution test** Provide quantitative pull-down data (e.g., densitometry) with at least three independent biological replicates, include appropriate negative controls (e.g., GST alone, unrelated prey proteins), and show loading controls. Ideally, confirm a subset of key interactions by an orthogonal method (e.g., co-immunoprecipitation from yeast).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "we conclude that PAH1 and PAH2 are indeed redundant for mediating Opi1-dependent gene repression" based on Table 1 data
- **Evidence pointer** Table 1, Results section "Sin3-binding repressor proteins interact with PAH1 or PAH2"
- **Concern** The conclusion of redundancy is based on a single experiment with Sin3 deletion variants. The data show that deletion of both PAH1 and PAH2 leads to increased expression under repressing conditions (19.0 vs 4.9 for wild-type), but the D/R ratio is 1.6, indicating loss of regulation. However, the individual deletions (∆PAH1 and ∆PAH2) still show substantial repression (D/R ratios of 5.9 and 9.4, respectively). This is interpreted as redundancy, but an alternative interpretation is that both domains contribute additively, and only their combined deletion abolishes function. The experiment does not distinguish between redundancy and additive effects. Furthermore, only one reporter gene (ICRE-CYC1-lacZ) was tested, and the physiological relevance of the lexA-based assay for Opi1 function at native promoters is not established.
- **Why it matters** The claim of functional redundancy between PAH1 and PAH2 is a key conclusion of the paper and has implications for understanding Sin3-mediated repression mechanisms. If the conclusion is based on an underpowered or confounded experiment, it may be incorrect. The distinction between redundancy and additivity is mechanistically important.
- **Resolution test** Perform a more detailed deletion analysis, including combinations of PAH deletions with quantitative dose-response measurements. Test Opi1-dependent repression at a native target promoter (e.g., INO1) in the same Sin3 mutant backgrounds. Include complementation experiments with PAH1-only or PAH2-only constructs to directly test sufficiency.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors state that "structural predictions provide no precise evidence for a conserved folding pattern common to all repressor proteins tested" and suggest that corepressor interaction domains are intrinsically disordered regions
- **Evidence pointer** Discussion section, Supplementary Figure 2
- **Concern** The AlphaFold predictions are described only in the text with reference to Supplementary Figure 2, which was not available for review. The conclusion that the domains are intrinsically disordered is based on visual inspection of predicted structures, which is not a rigorous method for assessing disorder. No computational disorder prediction tools (e.g., IUPred, PONDR) are used, and no experimental validation (e.g., circular dichroism, NMR) is provided. The authors cite previous CD experiments on other CID peptides, but this does not directly support their claims about the specific domains studied here.
- **Why it matters** The claim that CIDs are intrinsically disordered is presented as a general principle but is not directly tested. If this is a central message of the paper, it requires stronger evidence. If it is speculative, it should be clearly framed as a hypothesis rather than a conclusion.
- **Resolution test** Use established disorder prediction algorithms on the compiled CID sequences and present the results quantitatively. If possible, perform CD spectroscopy on a subset of the mapped minimal domains to test for disorder-to-order transitions upon corepressor binding. Alternatively, reframe the claim as a hypothesis in the discussion.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "Sko1 could bind Cyc8 and Tup1" in contrast to a previous report that Sko1 merely interacts with Tup1
- **Evidence pointer** Figure 1, Results section "Pathway-specific repressor proteins are able to physically interact with pleiotropic corepressors Sin3, Cyc8 and Tup1"
- **Concern** This discrepancy with published data is noted but not discussed in detail. The authors do not address potential reasons for the discrepancy (e.g., different experimental conditions, different protein fragments used, or different Sko1 isoforms). The Sko1 interaction with Cyc8 is reported as positive, but the mapping data for Sko1 (Figure S1d) shows that the Cyc8 interaction domain is within aa 201-427, which is a large region. Without further validation, this discrepancy remains unresolved.
- **Why it matters** The paper claims to correct or extend a previous finding, but without addressing the discrepancy, readers cannot assess which result is more reliable. This is particularly important because Sko1 is a well-studied repressor, and the nature of its corepressor interactions has functional implications.
- **Resolution test** Discuss the discrepancy explicitly in the Discussion section, considering differences in experimental approaches. Ideally, validate the Sko1-Cyc8 interaction by an independent method (e.g., co-immunoprecipitation from yeast) and test whether the interaction is functionally relevant for Sko1-mediated repression.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction
- **Evidence pointer** Introduction, first paragraph
- **Issue** The introduction assumes significant background knowledge of yeast transcriptional regulation. Terms such as "pleiotropic corepressors," "PAH domains," and "TPR motifs" are introduced without brief explanations for readers outside the immediate field.
- **Required correction** Add brief explanations or a schematic figure illustrating the domain structures of Sin3, Cyc8, and Tup1, and the general mechanism of corepressor recruitment.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Materials and methods
- **Evidence pointer** Materials and methods, "Plasmid constructions"
- **Issue** The methods for plasmid construction are described only briefly, with reference to Supplementary Tables S2 and S3. The details of how truncation boundaries were chosen and how constructs were verified are not provided in the main text.
- **Required correction** Provide a brief description of the cloning strategy and verification methods (e.g., sequencing) in the main text, or ensure the supplementary tables contain sufficient detail.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, Figure 1
- **Evidence pointer** Figure 1 legend
- **Issue** The figure legend states "SD standard deviation" but no error bars are visible in the described figure, and the number of replicates is not stated. It is unclear what the SD refers to.
- **Required correction** Clarify what the SD represents and ensure error bars are shown in the figure, or remove the mention of SD if not applicable.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion
- **Evidence pointer** Discussion, paragraph on sequence analysis
- **Issue** The sequence motif analysis (Table 3) identifies heptad-like patterns in all 16 CIDs, but the authors do not assess whether these patterns are statistically enriched compared to random sequences or unrelated proteins. The significance of finding at least one pattern in each CID is unclear without a background model.
- **Required correction** Perform a statistical analysis comparing the frequency of heptad patterns in CIDs versus control sequences (e.g., random proteins or non-interacting domains) to support the claim that these patterns are meaningful.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Results, Table 2
- **Evidence pointer** Table 2
- **Issue** Table 2 lists 16 repressor sequences with minimal domains, but the functional significance of the underlined hydrophobic residues is not explained in the table legend or the main text.
- **Required correction** Add a brief explanation in the table legend or text describing what the underlining indicates and why these residues are of interest.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, Yox1 mutagenesis
- **Evidence pointer** Figure 4
- **Issue** The mutagenesis of Yox1 focuses on hydrophobic residues, but the rationale for choosing specific residues (V257, L262, V266, I270, L271) is not explained. The authors mention a "heptad-like sequence pattern" but do not show how these residues fit the pattern.
- **Required correction** Provide a clearer explanation of the heptad pattern and how the mutated residues were selected, possibly with a schematic alignment.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion
- **Evidence pointer** Discussion, final paragraph
- **Issue** The discussion of intrinsic disorder in CIDs is interesting but does not address the functional implications of this property. How does disorder contribute to the ability of a single domain to interact with multiple structurally distinct corepressors?
- **Required correction** Expand the discussion to address the functional significance of disorder for multi-corepressor binding and how this might relate to the observed redundancy.

## Risk / unsupported claims
- The claim that "most repressors are able to contact more than a single corepressor" is based on binary pull-down data without quantitative support or replicates, making the interaction network potentially unreliable
- The conclusion of PAH1/PAH2 redundancy for Opi1 function is based on a single reporter assay and does not distinguish between redundancy and additive effects
- The statement that CIDs are intrinsically disordered is not directly supported by the data presented; AlphaFold predictions are not a validated method for assessing disorder, and no experimental validation is provided
- The discrepancy with the previous report on Sko1-Cyc8 interaction is noted but not resolved or discussed
- The functional significance of the heptad-like sequence patterns in Table 3 is not statistically validated
- The claim that "structural predictions provide no precise evidence for a conserved folding pattern" is based on visual inspection of predictions that were not available for review