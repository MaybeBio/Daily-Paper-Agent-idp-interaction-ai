## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods, data deposition)
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and technical soundness as presented in the provided text; no supplementary figures or tables were available for direct inspection
- **Shared manuscript claim summary** The authors map transcriptome-wide mRNA binding of 16 RNA-binding proteins in budding yeast using an upscaled RNA-tagging method, then perform domain and IDR deletions in eight of these proteins to dissect the relative contributions of predicted RBDs and IDRs to in vivo binding affinity and specificity. They report that most predicted RBDs are not individually essential, while multiple IDRs lacking predicted RNA-binding potential are essential for binding or specificity.
- **Visible evidence base** Main-text figures referenced (Figures 1–5), supplemental figures and tables referenced but not provided, methods descriptions, data deposition statement
- **Missing materials affecting confidence** Supplementary figures and tables (S1–S9), raw sequencing data, strain tables, detailed bioinformatic parameters, and the GitHub repository contents were not accessible for verification

## Reviewer

- **Overall assessment** This manuscript addresses an important and timely question in RNA biology: the relative contributions of canonical RNA-binding domains versus intrinsically disordered regions to in vivo RNA binding. The authors apply a technically demanding approach (RNA-tagging) at a scale that exceeds previous efforts, and their central observation that IDRs contribute substantially to binding specificity challenges simple domain-centric models of RBP function. However, the manuscript as presented has several weaknesses that limit the strength of the conclusions. The selection criteria for the 34 screened RBPs are described as "rather loose," and the failure rate (18 of 34) is not systematically explained. The target-calling threshold (modification level above a fixed dPup2 background) may conflate weak binding with nonspecific background. Most critically, the deletion experiments, while extensive, do not fully disentangle direct RNA-binding contributions of IDRs from indirect effects on protein stability, folding, or interactions with partner proteins. The claim that IDRs contain "determinants" of binding would be strengthened by point-mutation or minimal-domain experiments. The evolutionary conservation analysis is descriptive and does not establish functional significance. Despite these concerns, the dataset itself is a valuable resource, and the conclusions, if supported by additional controls, would be of broad interest.

- **Who would be interested in the results, and why** RNA biologists studying RBP function and specificity, computational biologists developing RBP binding prediction tools, and researchers interested in the role of intrinsically disordered regions in macromolecular interactions. The transcriptome-wide binding maps for 16 yeast RBPs, several of which are poorly characterized, provide a resource for the community. The finding that IDRs contribute to binding specificity has implications for understanding how RBPs achieve selectivity in vivo and for interpreting disease-associated mutations in disordered regions.

- **Major strengths**
  1. The upscaling of the RNA-tagging method to 16 RBPs represents a substantial technical advance and provides a valuable community resource.
  2. The systematic deletion analysis across eight RBPs, distinguishing clustered versus dispersed RBD architectures, is a thoughtful experimental design.
  3. The observation that IDR deletions can abolish binding or alter specificity, even when RBDs remain intact, is a conceptually important finding.
  4. The inclusion of evolutionary conservation analysis across Saccharomycetaceae adds a comparative dimension.
  5. The authors acknowledge limitations of the RNA-tagging method and provide clear descriptions of their computational pipeline.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental design and controls
- **Claim pointer** "The majority of the predicted RBDs tested were not individually essential for mRNA binding. However, multiple IDRs that lacked predicted RNA-binding potential appeared essential for binding affinity or specificity."
- **Evidence pointer** Results section "Differential contribution of RBDs to binding affinity and specificity"; Figures 4 and 5; Supplemental Figures S5, S6
- **Concern** The deletion experiments remove large regions (40–400 residues) that include both IDRs and, in some cases, structured elements. The authors attribute loss of binding or specificity to the deleted IDR, but large deletions can disrupt protein folding, stability, or interactions with cofactors, producing indirect effects on RNA binding. The claim that IDRs contain "determinants" of binding requires more precise mapping. For example, in Puf4, deletion of ~300 residues abolishes binding, but this region may be required for proper folding of the adjacent RBDs or for interaction with a protein partner that bridges RNA binding. The authors do not report protein expression levels for the deletion mutants, nor do they test whether the deleted IDRs can confer binding when transplanted to a heterologous protein.
- **Why it matters** The central conclusion of the paper, that IDRs contribute directly to RNA binding specificity, depends on the interpretation of these deletion phenotypes. Without controls for protein stability and folding, the results are consistent with alternative explanations, including indirect structural effects.
- **Resolution test** Provide western blot or other quantitative protein level measurements for all deletion mutants. Include at least one domain-swap or minimal-IDR experiment showing that a deleted IDR can confer binding or specificity when fused to a different RBD. Alternatively, identify specific residues within the IDR that, when mutated, recapitulate the deletion phenotype.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Data analysis and target calling
- **Claim pointer** "We then defined, for each RBP, the set of target genes. The number of significantly modified targets ranged from ten (Gbp2) to 2744 (Pub1)."
- **Evidence pointer** Results section "Binding profiles of RBPs provide new insights into their function"; Figure 3E; Materials and Methods "Target determination and GO-term analysis"
- **Concern** The target-calling procedure uses a fixed threshold of modification level > 0.15 (log2 scale, relative to dPup2 background) for all RBPs. This approach does not account for RBP-specific differences in expression, RNA accessibility, or the dynamic range of the assay. For highly expressed RBPs like Pub1, the large number of targets (2744, nearly half of the yeast transcriptome) may reflect promiscuous low-level binding rather than specific targeting. Conversely, for Gbp2 with only 10 targets, the threshold may be too stringent. The authors do not report false discovery rates, permutation-based significance, or comparison to a null model. The GO enrichment analysis uses a hypergeometric test but does not correct for multiple testing across the large number of terms and RBPs examined.
- **Why it matters** The definition of "targets" underpins all downstream analyses, including the assessment of whether IDR deletions alter specificity. If the target set is noisy or biased, the conclusions about specificity changes may be artifacts.
- **Resolution test** Implement a statistical framework for target calling that models the relationship between binding score and expression, using a permutation-based null or a mixture model. Report FDR-adjusted p-values for target identification and GO enrichment. Show that the number of targets is robust to threshold choice, or justify the threshold with a formal statistical rationale.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of specificity changes
- **Claim pointer** "Generally, this binding to nontargets increased gradually as larger regions were truncated, indicating that specificity depends on multiple determinants distributed within the truncated IDRs."
- **Evidence pointer** Results section "mRBP-binding profiles depend on IDRs outside predicted RBDs"; Figure 5A,D; Supplemental Figure S6A
- **Concern** The observation that IDR truncations lead to increased binding of nontarget transcripts is interpreted as a loss of specificity. However, an alternative explanation is that the truncations increase the accessibility or affinity of the RBDs for RNA in a nonspecific manner, perhaps by removing autoinhibitory interactions or by altering the conformational ensemble of the protein. The authors do not distinguish between "loss of specificity determinants" and "gain of promiscuous binding." Additionally, the correlation between the degree of truncation and the number of gained targets is not quantified, and the authors do not test whether the gained targets share any features (e.g., expression level, length, secondary structure) that might indicate a mechanism.
- **Why it matters** The mechanistic interpretation of how IDRs control specificity is central to the paper's conceptual contribution. If the effect is indirect (e.g., conformational changes), the conclusion that IDRs contain "determinants" in a sequence-specific sense is weakened.
- **Resolution test** Analyze the sequence features of gained targets versus lost targets. Test whether the gained targets are enriched for a particular motif or structural feature. Perform limited proteolysis or circular dichroism on selected deletion mutants to assess conformational changes. Compare the binding profiles of IDR deletions to those of RBD point mutations that are known to reduce specificity.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Evolutionary conservation analysis
- **Claim pointer** "We found a high level of conservation in both RBD composition, including identity, sequence, and location, with more than 80% of orthologs of most mRBPs sharing the same domain composition. Moreover, the presence and size of the associated IDRs were also conserved between orthologs with IDR conservation of most orthologs varying by less than 30%."
- **Evidence pointer** Results section "Predicted RBDs and IDRs occupy a large fraction of the mRBP sequences and are conserved throughout evolution"; Figure 1E,F; Supplemental Figure S2
- **Concern** The conservation analysis is descriptive and does not establish functional significance. The statement that IDR "presence and size" are conserved is based on disorder prediction (IUPred2), which is a coarse measure. The authors do not report sequence-level conservation within IDRs, which is typically low, nor do they test whether the conserved IDR features correlate with the experimentally determined binding phenotypes. The comparison to TFs is interesting but underdeveloped; the authors do not discuss whether the observed differences in IDR composition between RBPs and TFs have functional implications for their respective DNA versus RNA binding mechanisms.
- **Why it matters** The conservation analysis is used to argue that the IDRs are functionally important. Without a link between conservation and function, this argument is circumstantial.
- **Resolution test** Perform a more detailed sequence analysis of conserved IDR regions, identifying short linear motifs or conserved hydrophobic patches. Correlate the degree of IDR conservation with the severity of the deletion phenotype across the eight experimentally tested RBPs. If possible, test whether conserved IDR elements are sufficient to confer binding when transferred to a heterologous context.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and presentation
- **Affected element** Figure 1A
- **Evidence pointer** Results section "Predicted RBDs and IDRs occupy a large fraction of the mRBP sequences and are conserved throughout evolution"
- **Issue** The comparison of RBD/IDR occupancy between mRBPs, genRBPs, and TFs is presented as a key motivation, but the figure is not available for inspection. The text states that mRBPs have a higher fraction of IDR than genRBPs, but the statistical significance of this difference is not reported.
- **Required correction** Report the statistical test and p-values for the comparisons in Figure 1A. Clarify whether the differences are driven by a few outliers or are consistent across the protein sets.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methods transparency
- **Affected element** Target-calling threshold
- **Evidence pointer** Materials and Methods "Target determination and GO-term analysis"
- **Issue** The choice of the dPup2 background threshold (0.15 in linear scale) is stated but not justified. It is unclear how this value was derived and whether it is appropriate for all 16 RBPs.
- **Required correction** Provide a rationale for the threshold choice, ideally with a sensitivity analysis showing how the number of targets changes with the threshold. If a fixed threshold is used, state this as a limitation.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data interpretation
- **Affected element** Discussion of Pub1 and Sro9
- **Evidence pointer** Results section "Binding profiles of RBPs provide new insights into their function"
- **Issue** The authors state that Pub1 and Sro9 have "limited specificity and a general role in translation" based on the large number of targets and the expression-level dependence of binding. However, the GO analysis shows enrichment for ribosomal protein transcripts, which could indicate specific targeting of a functionally coherent class of mRNAs rather than general binding.
- **Required correction** Clarify the distinction between "limited specificity" and "specificity for a large class of functionally related mRNAs." Consider whether the enrichment for ribosomal protein transcripts reflects a biological function rather than a lack of specificity.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** RNA-tagging method
- **Evidence pointer** Materials and Methods "RNA extraction and library construction"
- **Issue** The description of the library construction mentions Tn5 cleavage and adapter insertion, but the details of how the poly(U) stretches are preserved and sequenced are not fully described. The authors state that read 2 contains the poly(U) information, but the sequencing depth and read length requirements are not discussed.
- **Required correction** Provide additional detail on how poly(U) stretches are called from the sequencing data, including error rates and how homopolymer sequencing errors are handled. State the minimum sequencing depth required for reliable target identification.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** GO enrichment analysis
- **Evidence pointer** Materials and Methods "Target determination and GO-term analysis"
- **Issue** The hypergeometric test is described, but the multiple testing correction is not mentioned. With 16 RBPs and many GO terms, the false positive rate could be substantial.
- **Required correction** Report whether multiple testing correction was applied (e.g., Benjamini-Hochberg FDR) and provide adjusted p-values or q-values for the enriched terms in Figure 3F.

- **Technical failings that need to be addressed before the case is established**
  R1-M1 (deletion experiments lack protein-level controls and mechanistic resolution), R1-M2 (target-calling threshold lacks statistical rigor), R1-M3 (specificity changes not distinguished from promiscuous binding). These are the primary technical issues that must be resolved before the central claims can be considered established.

- **Assessment against Nature-style criteria**
  - **Originality** The question of IDR contributions to RBP binding specificity is not entirely new, but the systematic experimental dissection across multiple RBPs in a single study is a valuable and relatively original contribution. The upscaling of RNA-tagging to 16 proteins is technically novel.
  - **Scientific importance** The findings have the potential to shift thinking about how RBPs achieve specificity, with implications for understanding posttranscriptional regulation and for interpreting disease-associated mutations. However, the importance is contingent on the robustness of the deletion phenotypes, which is currently uncertain.
  - **Interdisciplinary readership** The topic is of interest to molecular biologists, biochemists, and computational biologists. The methods and conclusions are accessible to these audiences, though the statistical details of the target-calling pipeline may be challenging for non-specialists.
  - **Technical soundness** The RNA-tagging method is well-established, and the upscaling appears carefully executed. However, the deletion analysis lacks critical controls (protein stability, folding, interaction partners), and the target-calling threshold is not statistically justified. These issues undermine the technical soundness of the central claims.
  - **Readability for nonspecialists** The manuscript is generally well-written and logically organized. The introduction and discussion are accessible. The results section is dense but understandable. The methods are described in sufficient detail for specialists, though some steps (e.g., Tn5-based library construction) could be clarified.

- **Recommendation posture** Supportive if technical concerns are resolved. The dataset and conceptual framework are valuable, and the central hypothesis is worth testing. However, the current evidence does not fully establish that IDRs directly determine binding specificity, given the lack of controls for indirect effects of large deletions and the statistical weaknesses in target calling. If the authors can provide protein-level controls, more precise mapping of IDR determinants, and a more rigorous statistical framework, the manuscript would be suitable for publication in a high-impact journal.

## Risk / unsupported claims
- The claim that "multiple IDRs that lacked predicted RNA-binding potential appeared essential for binding affinity or specificity" is not fully supported because the deletion phenotypes could arise from indirect structural or stability effects, and protein levels were not reported.
- The claim that "the majority of the predicted RBDs tested were not individually essential for mRNA binding" is weakened by the lack of a statistical framework for determining whether residual binding after RBD deletion is significant.
- The statement that "the binding profiles of these proteins highlight their central role in cell physiology" is supported by GO enrichment, but the lack of multiple testing correction makes the significance of these enrichments uncertain.
- The evolutionary conservation analysis (Figure 1E,F) is descriptive and does not establish functional relevance of the conserved IDR features.
- The claim that the RNA-tagging method "can be used as a measure for the reliability of the observed mRNA binding" based on the correlation of poly(U) stretches is reasonable but not formally validated against an orthogonal method (e.g., CLIP or RIP) in this study.