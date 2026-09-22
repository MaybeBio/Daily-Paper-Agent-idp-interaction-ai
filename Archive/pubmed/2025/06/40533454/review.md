## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, figure legends, and table legends. Supplementary figures and tables are referenced but not fully provided.
- **Assessment boundary** Scientific validity, technical soundness, logical coherence, and support of claims by presented evidence. Statistical analyses and experimental designs are assessed where described.
- **Shared manuscript claim summary** The authors investigate the mechanistic basis for divergent co-TF (Pho2) dependence between two orthologous yeast transcription factors, ScPho4 and CgPho4. They identify three key differences: (1) CgPho4 binds the same DNA motif with 3-4 fold higher affinity; (2) CgPho4 contains two activation enhancer domains (AEDs) in intrinsically disordered regions that boost the main activation domain; (3) ScPho4 contains a dual-functional Pho2 interaction domain (P2ID) that both enables Pho2-dependent activation and restricts activity without Pho2. The authors conclude that divergence in intrinsically disordered regions drives evolution of co-TF dependence.
- **Visible evidence base** Main text figures 1-7, Table 1, Table 2, Methods section, and referenced supplementary figures (S1-S9) and supplementary data. Full supplementary materials not provided.
- **Missing materials affecting confidence** Supplementary Figures 1-9, Supplementary Data 1, source data files, and full statistical output tables. These are referenced for key claims including sequence alignments, PADDLE predictions for all constructs, gating strategies, and raw data distributions.

## Reviewer
- **Overall assessment** This manuscript addresses an important and underexplored question in eukaryotic gene regulation: how does co-TF dependence evolve? The authors use a systematic chimeric approach to dissect functional differences between two Pho4 orthologs, and their identification of AEDs as novel regulatory elements in IDRs is potentially significant. The work is generally well-designed and the conclusions are largely supported by the data presented. However, several technical concerns need to be addressed, particularly regarding the interpretation of the chimeric experiments, the statistical treatment of the flow cytometry data, and the generalizability of the findings given the limited phylogenetic sampling. The manuscript would be strengthened by additional mechanistic insight into how the AEDs function and by addressing the potential confounding effects of protein stability and folding in the chimeric constructs.

- **Who would be interested in the results, and why** Researchers studying eukaryotic transcription factor function and evolution, particularly those interested in intrinsically disordered regions, combinatorial control of gene expression, and the molecular basis of regulatory network divergence. The work may also be of interest to those studying fungal pathogenesis, given the inclusion of C. glabrata, and to computational biologists developing predictors of activation domains or TF functional evolution.

- **Major strengths**
  1. The study addresses a fundamental and understudied question in regulatory evolution: how co-TF dependence itself evolves.
  2. The systematic chimeric approach (50 constructs) is comprehensive and well-designed, allowing for the identification of specific regions responsible for functional differences.
  3. The identification of AEDs as novel functional elements in IDRs is a potentially important contribution to the field.
  4. The dual fluorescence reporter system provides a robust quantitative readout of TF activity.
  5. The authors test both the enhanced activity and autoinhibition models, providing a more complete picture of the mechanisms involved.
  6. The work has clear implications for understanding how IDR divergence can drive regulatory network rewiring.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of chimeric construct interpretation
- **Claim pointer** The authors claim that swapping individual regions between ScPho4 and CgPho4 allows them to identify the functional contributions of each region to Pho2-dependence. Specifically, they conclude that "R1:Cg and NLS:Cg each had significant, positive effects on their own on both APHO2 and Apho2∆" and that the P2ID is a "double-edged sword."
- **Evidence pointer** Figure 5, Figure 6, Table 1
- **Concern** The interpretation of the chimeric experiments assumes that the functional effects of each region are largely independent and additive. However, the authors do not adequately address the possibility that swapping regions between two divergent proteins (which share only ~40% identity overall) could disrupt protein folding, stability, or inter-domain interactions in ways that are not directly related to the specific functions being studied. The observation that some chimeras show higher activity than either parental protein (Figure 5A) is intriguing but also raises questions about whether the chimeric proteins are properly folded. The authors should provide evidence that the chimeric proteins are expressed at similar levels and are properly folded, perhaps through western blotting or a functional assay that does not depend on the specific activity being measured.
- **Why it matters** If the effects of region swaps are confounded by protein misfolding or instability, the conclusions about which regions contribute to Pho2-dependence would be compromised. This is particularly important given that the authors are drawing conclusions about the evolutionary significance of specific regions.
- **Resolution test** Provide western blot or quantitative fluorescence data demonstrating comparable protein expression and stability across all chimeric constructs. Additionally, include a control experiment where a functionally neutral region (e.g., a region with no predicted function) is swapped to assess the baseline effect of chimeric construction on protein function.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical analysis of flow cytometry data
- **Claim pointer** The authors state that "APHO2 and Apho2∆ values for ScPho4 and CgPho4 across 6 different days of experiments showing consistent results" and use these data to make quantitative comparisons between chimeras (e.g., "1.2-fold increase," "71% reduction," "1.76-fold increase").
- **Evidence pointer** Figure 4C, 4D, Figure 5, Figure 6, Methods "Statistical analyses"
- **Concern** The statistical analysis of the flow cytometry data is not described in sufficient detail. The authors mention fitting linear models and applying Holm-Bonferroni corrections, but do not specify how many biological replicates were used for each chimeric construct, whether the data were transformed (e.g., log-transformed) before analysis, or how the linear model assumptions were verified. Given that the authors are making quantitative claims about fold-changes and reductions, it is critical to know the confidence intervals and effect sizes for these comparisons. The bootstrap confidence intervals shown in Figures 5 and 6 are helpful, but the statistical framework for comparing between chimeras is not fully described.
- **Why it matters** The quantitative claims about the effects of specific regions (e.g., the "71% reduction" in activity when P2ID:Sc is swapped into CgPho4) are central to the paper's conclusions. Without a clear description of the statistical methods and the variability in the data, it is difficult to assess the robustness of these claims.
- **Resolution test** Provide a detailed description of the statistical analysis, including the number of replicates per construct, the model fitting procedure, how the data were transformed, and how the assumptions of the linear model were checked. Include effect sizes and confidence intervals for all key comparisons.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of findings
- **Claim pointer** The authors conclude that "divergence in a eukaryotic transcription factor's co-TF dependence involves multiple intrinsically disordered regions" and suggest that this represents a general mechanism for the evolution of combinatorial control.
- **Evidence pointer** Figure 7, Discussion
- **Concern** The study compares only two Pho4 orthologs, and while the authors mention that Pho2-dependence varies across other species (referencing their previous work), they do not provide data on whether the specific regions identified here (AEDs, P2ID) are responsible for the variation in other species. The preliminary analysis in Supplementary Figure 8 is mentioned but not shown in the main text. The claim that IDR divergence drives co-TF dependence evolution would be substantially strengthened by demonstrating that the same regions are involved in other species with intermediate levels of Pho2-dependence.
- **Why it matters** The paper's title and framing suggest a general principle about IDR evolution and co-TF dependence. If the findings are specific to the C. glabrata lineage, the broader significance would be diminished.
- **Resolution test** Include the data from Supplementary Figure 8 in the main text or provide additional analysis of Pho2-dependence in other species. Alternatively, temper the claims in the title and discussion to reflect the two-species comparison.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic understanding of AED function
- **Claim pointer** The authors state that "two intrinsically disordered regions (IDRs) in CgPho4 that boost its activation domain's activity" and that these AEDs "can enhance the activation potential of the main AD."
- **Evidence pointer** Figure 3, Figure 5
- **Concern** The mechanism by which the AEDs enhance activation domain activity is not explored. The authors show that the AEDs enhance activity when fused to a minimal activation domain, but they do not investigate whether this occurs through direct co-activator recruitment, through effects on protein stability, through conformational changes, or through some other mechanism. Given that the authors are proposing a new functional class of elements (AEDs), a more detailed mechanistic characterization would be valuable.
- **Why it matters** Without understanding how AEDs function, it is difficult to predict their prevalence and importance in other transcription factors. The claim that this is a novel mechanism would be strengthened by some insight into the biochemical basis of AED activity.
- **Resolution test** Perform additional experiments to investigate the mechanism of AED function, such as testing whether the AEDs interact with known co-activators, whether they affect the conformation of the activation domain, or whether they influence protein stability.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of P2ID autoinhibition
- **Claim pointer** The authors conclude that "an IDR next to the DNA binding domain both allows for enhanced activity with Pho2 and inhibits activity without Pho2" and describe this as a "double-edged sword."
- **Evidence pointer** Figure 6, Figure 7
- **Concern** The evidence for autoinhibition is indirect. The authors show that swapping P2ID:Sc into CgPho4 reduces activity without Pho2, and that swapping P2ID:Cg into ScPho4 increases activity without Pho2. However, they do not directly demonstrate that the P2ID:Sc physically inhibits the activation domain in the absence of Pho2. The observation that the first half of P2ID:Sc enhances activity with Pho2 while the second half restricts activity without Pho2 is interesting, but the mechanism of this dual function is not explored.
- **Why it matters** The autoinhibition model is one of the two main models proposed in the introduction, and the authors claim to provide support for it. However, the evidence is correlative and does not establish a direct physical mechanism of autoinhibition.
- **Resolution test** Perform experiments to directly test whether the P2ID:Sc physically interacts with the activation domain in the absence of Pho2, such as cross-linking or FRET-based assays. Alternatively, use mutations that specifically disrupt the putative autoinhibitory interaction to test whether this relieves the inhibition.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure presentation
- **Affected element** Figure 5A
- **Evidence pointer** Figure 5A
- **Issue** The scatter plot in Figure 5A shows many data points, but it is difficult to distinguish between the different chimeric constructs. The color coding is not described in the legend, and the labels are small.
- **Required correction** Provide a clear legend explaining the color coding and consider labeling individual data points or using a different visualization method (e.g., a heatmap) to make the data more accessible.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Yeast one-hybrid assay
- **Evidence pointer** Methods "Yeast one-hybrid and yeast two-hybrid"
- **Issue** The description of the yeast one-hybrid assay is brief. It is not clear how the GAL1pr-mCherry reporter was constructed, how the flow cytometry gating was performed, or how the background fluorescence was subtracted.
- **Required correction** Provide a more detailed description of the yeast one-hybrid assay, including the reporter construction, gating strategy, and data analysis.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of binding affinity data
- **Affected element** Figure 2E
- **Evidence pointer** Figure 2E
- **Issue** The authors report a 3-4 fold difference in binding affinity between ScPho4 and CgPho4, but the biological significance of this difference is not discussed. The authors note that the difference is "modest" but do not explore whether this difference would be expected to have a significant impact on gene regulation in vivo.
- **Required correction** Add a discussion of the potential biological significance of the observed affinity difference, considering factors such as nuclear concentration and the number of binding sites.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** "Activation Enhancer Domains (AEDs)"
- **Evidence pointer** Figure 3, Discussion
- **Issue** The term "Activation Enhancer Domain" is new, and it is not immediately clear how it differs from other terms used in the field, such as "activation subdomain" or "auxiliary activation domain."
- **Required correction** Provide a clear definition of AEDs and explain how they differ from previously described functional elements in transcription factors.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 3C, 3D
- **Evidence pointer** Figure 3C, 3D
- **Issue** The statistical analysis for the yeast one-hybrid data in Figure 3 is not described in the figure legend. It is not clear what test was used and what the error bars represent.
- **Required correction** Add a description of the statistical analysis to the figure legend, including the test used, the number of replicates, and what the error bars represent.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The authors do not discuss the limitations of their study, such as the use of a heterologous system (S. cerevisiae) to test C. glabrata proteins, the potential for context-dependent effects, and the limited number of species compared.
- **Required correction** Add a paragraph discussing the limitations of the study and how they might affect the generalizability of the conclusions.

## Risk / unsupported claims
1. The claim that the AEDs "boost its activation domain's activity" is supported by the yeast one-hybrid data, but the mechanism of this enhancement is not explored, making the claim incomplete.
2. The claim that P2ID:Sc "allows for enhanced activity with Pho2 and inhibits activity without Pho2" is supported by the chimeric data, but the direct physical mechanism of autoinhibition is not demonstrated.
3. The claim that "IDR divergence drives TF interdependence evolution" is based on a comparison of only two species and is not directly tested in other species with intermediate Pho2-dependence.
4. The claim that the binding affinity difference between ScPho4 and CgPho4 is functionally significant is not directly tested in vivo.
5. The generalizability of the findings to other transcription factors is speculative and not supported by data from other systems.