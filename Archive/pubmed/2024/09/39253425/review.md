## Review setup
- **Input scope** Full manuscript text including abstract, results, discussion, methods, and figure legends (figures themselves not provided)
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the text; no assessment of figures or supplementary materials beyond what is described
- **Shared manuscript claim summary** The authors investigate the molecular basis for divergence in co-TF (Pho2) dependence between two Pho4 orthologs in yeast. They identify three key differences: (1) CgPho4 binds DNA with 3-4-fold higher affinity; (2) CgPho4 contains two activation enhancer domains (AEDs) in intrinsically disordered regions; (3) ScPho4 has a dual-function Pho2 interaction domain (P2ID) that both enhances activity with Pho2 and inhibits activity without it. The authors conclude that IDR divergence drives evolution of TF interdependence.
- **Visible evidence base** Text descriptions of results from: sequence analysis, ChIP-seq motif identification, universal and genomic context protein binding microarrays, biolayer interferometry, EMSA, yeast one-hybrid assays, yeast two-hybrid assays, and a chimeric TF library of 50 constructs with flow cytometry readouts
- **Missing materials affecting confidence** Figures and supplementary figures not provided; raw data not accessible; statistical details partially reported; exact construct boundaries only in Table 1 (not provided); nuclear localization data described but not shown

## Reviewer

- **Overall assessment** This manuscript addresses an important and underexplored question in eukaryotic gene regulation: how TF interdependence on co-factors evolves. The authors use a well-designed chimeric approach to dissect functional differences between two Pho4 orthologs. The identification of two novel activation enhancer domains in CgPho4 and the dual-function P2ID in ScPho4 is potentially significant. However, several claims are not fully supported by the evidence as presented, particularly regarding the mechanistic interpretation of the AEDs and the in vivo relevance of the DNA binding affinity difference. The manuscript would benefit from additional experiments to directly test the proposed models and from clearer presentation of quantitative data.

- **Who would be interested in the results, and why** Researchers studying eukaryotic transcription factor function, combinatorial control of gene regulation, intrinsically disordered regions in transcriptional regulation, and regulatory evolution. The work is also relevant to those interested in the PHO signaling pathway and comparative genomics of fungal pathogens.

- **Major strengths** 
  1. The study addresses a fundamental and understudied question: how TF interdependence evolves
  2. The chimeric TF library approach is systematic and powerful for dissecting functional domains
  3. The identification of AEDs as a new class of regulatory elements in IDRs is novel
  4. The dual-function P2ID concept (enhancement with co-TF, inhibition without) is elegant
  5. Multiple complementary assays (Y1H, BLI, EMSA, PBM, flow cytometry) strengthen the conclusions
  6. The work has potential implications for understanding regulatory evolution and disease

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim** The authors claim that the two AEDs in CgPho4 "boost its activation domain's activity" and contribute to reduced Pho2 dependence.
- **Evidence pointer** Results section "CgPho4 encodes two additional Activation Enhancer Domains (AEDs)", Figure 3
- **Concern** The Y1H assay measures activation potential of isolated regions fused to Gal4 DBD, but the mechanism by which AEDs enhance AD activity is not investigated. The authors propose two hypotheses (weak ADs vs. conformational effects) but provide no experiments to distinguish them. More critically, the claim that AEDs contribute to reduced Pho2 dependence in the native context is inferred from chimeric constructs, but the direct contribution of each AED to Pho2 independence is not quantified. The epistasis analysis (Fig. 5D) shows positive interactions but the effect sizes and confidence intervals are not reported in the text.
- **Why it matters** Without mechanistic understanding or clear quantification of AED contribution, the central claim that IDR divergence drives co-TF dependence evolution remains correlative rather than causal.
- **Resolution test** Provide experiments that directly test AED mechanism (e.g., swapping AEDs into ScPho4 and measuring Pho2 dependence; mutagenesis of AED residues; testing AEDs with heterologous ADs). Report effect sizes and confidence intervals for the epistasis analysis.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim** The authors state that "CgPho4 binds the same consensus motif with a higher affinity compared to ScPho4" and that this difference is functionally relevant.
- **Evidence pointer** Results section "CgPho4 binds the same consensus motif with a higher affinity compared to ScPho4", Figures 2D-E, Supplementary Figure 4
- **Concern** The KD values are reported as 5.2 nM vs 1.2 nM (BLI) and 5.5 nM vs 1.9 nM (EMSA), but the text acknowledges this is a modest difference (ΔΔG = -0.87 kcal/mol). The authors then state that swapping DBD alone "failed to yield the expected results" in the chimeric context. This directly contradicts the hypothesis that binding affinity contributes to Pho2 independence. The authors suggest this may be due to the pho80∆ background, but this is speculative. The functional relevance of the affinity difference is therefore not established.
- **Why it matters** The enhanced activity model requires that higher DNA binding affinity contributes to reduced Pho2 dependence. If the DBD swap does not affect Pho2 dependence, the model is not supported by the data.
- **Resolution test** Test DBD swaps in a background where Pho4 nuclear concentration is limiting (e.g., varying phosphate conditions or PHO80 expression). Alternatively, measure Pho2 dependence of chimeras with DBD swaps at multiple expression levels.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim** The authors conclude that "IDR divergence drives TF interdependence evolution by influencing activation potential and autoinhibition."
- **Evidence pointer** Discussion section, Figure 7
- **Concern** The study examines only two orthologs, and the evolutionary conclusions are based on a single comparison. The authors mention preliminary analysis of eight orthologs (Supplementary Fig. 8) but this is not described in sufficient detail. The claim that IDR divergence "drives" evolution implies causality that cannot be established from a two-species comparison. Additionally, the relationship between the identified mechanisms and the previously reported correlation between Pho2 dependence and target gene number is not directly tested.
- **Why it matters** The broader evolutionary significance of the findings depends on whether the identified mechanisms generalize across species and whether they explain the observed variation in Pho2 dependence.
- **Resolution test** Expand the analysis to additional Pho4 orthologs with varying Pho2 dependence levels. Test whether the presence/absence of AEDs and P2ID features correlates with Pho2 dependence across species. Ideally, perform ancestral reconstruction or directed evolution experiments.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim** The authors state that "ScPho4's DBD requires both ScPho4's P2ID and Pho2 for full activity" based on chimeric constructs.
- **Evidence pointer** Results section "A double-edged sword", Figure 6C
- **Concern** The conclusion that DBD requires P2ID and Pho2 for function is based on chimeric constructs where P2ID and DBD are from different species. The authors show that inserting P2ID:Sc between P2ID:Cg and DBD:Sc rescues activity, but this does not demonstrate that the DBD itself requires P2ID. It could be that the P2ID provides a necessary interaction surface for Pho2 that is independent of the DBD. The claim challenges the modularity of TFs, which is a strong statement that requires more direct evidence.
- **Why it matters** The conclusion about TF modularity has broad implications for understanding TF evolution and engineering. If the claim is not well-supported, it could mislead future studies.
- **Resolution test** Perform domain-swap experiments with more precise boundaries, test DBD alone with and without Pho2 in a heterologous system, and measure DNA binding in the presence and absence of P2ID and Pho2 directly.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim** The authors use ChIP-seq data to identify binding motifs for both Pho4 orthologs and conclude they bind the same E-box motif.
- **Evidence pointer** Results section "CgPho4 binds the same consensus motif with a higher affinity compared to ScPho4", Figure 2B
- **Concern** The ChIP-seq data were previously published (reference 15) and were generated in S. cerevisiae with both Pho4s expressed from the same locus. The number of peaks is small (74 for ScPho4 and 118 for CgPho4), and the motif analysis may not be robust with such small numbers. The authors do not report whether the motif enrichment is statistically significant or how the motif comparison was performed.
- **Why it matters** The conclusion that both orthologs have identical DNA binding specificity is important for interpreting the functional differences. If the specificities differ subtly, this could affect the interpretation of the chimeric experiments.
- **Resolution test** Perform more comprehensive motif analysis with additional replicates or use in vitro methods (e.g., SELEX, MITOMI) to compare binding specificities more thoroughly.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states "CgPho4 binds the same motif with 3–4 fold higher affinity" but does not mention the modest effect size or the fact that DBD swapping did not produce expected results in chimeras.
- **Required correction** Add a qualifier such as "modestly" or "approximately 3-4 fold" and consider mentioning the DBD swap result to avoid overstating the contribution of binding affinity.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results, Figure 5D
- **Evidence pointer** Results section "The two Activation Enhancer Domains (AEDs) in CgPho4 increased the activity of the chimeric TFs but were insufficient to make them Pho2-independent"
- **Issue** The epistasis analysis is described but effect sizes, confidence intervals, and the proportion of variance explained are not reported.
- **Required correction** Report the full statistical output of the linear model, including coefficients, standard errors, and R² values.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, Y1H assay
- **Evidence pointer** Methods section "Yeast one-hybrid and yeast two-hybrid"
- **Issue** The Y1H assay description lacks details on the number of biological replicates, how the reporter activity was normalized, and the exact statistical test used for Figure 3C-D.
- **Required correction** Provide complete details on replicates, normalization, and statistical analysis for the Y1H experiments.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The authors discuss the potential role of IDRs in forming molecular condensates but do not provide any experimental evidence for this in their system. This is speculative and could be removed or clearly labeled as speculation.
- **Required correction** Either remove the condensate discussion or clearly state it as a hypothesis requiring future testing.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 6C
- **Evidence pointer** Results section "A double-edged sword"
- **Issue** The rescue experiment with P2ID:Sc insertion is described but the number of constructs tested and the reproducibility of the results are not clear.
- **Required correction** Clarify how many independent constructs were tested and whether the rescue was observed consistently.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction/Discussion
- **Evidence pointer** Introduction, Discussion
- **Issue** The authors do not discuss the potential role of phosphorylation in modulating the IDR functions they identified, despite noting that phosphorylation sites are conserved.
- **Required correction** Add a brief discussion of how phosphorylation might regulate AED and P2ID function, given the known role of Pho80/85 in phosphorylating these regions.

## Risk / unsupported claims
1. The claim that AEDs "boost" AD activity is supported by Y1H data, but the mechanism is unknown and the two proposed hypotheses are not tested.
2. The claim that DNA binding affinity differences contribute to Pho4 independence is not supported by the DBD swap experiments, which showed no effect.
3. The evolutionary conclusion that "IDR divergence drives TF interdependence evolution" is based on a two-species comparison and is not causally established.
4. The claim that ScPho4's DBD "requires" P2ID and Pho2 for function challenges TF modularity but is based on indirect chimeric evidence.
5. The preliminary analysis of eight Pho4 orthologs (Supplementary Fig. 8) is mentioned but not described in sufficient detail to evaluate.
6. The functional relevance of the modest binding affinity difference (ΔΔG = -0.87 kcal/mol) is not established, and the authors acknowledge this depends on nuclear concentration, which was not varied in their experiments.