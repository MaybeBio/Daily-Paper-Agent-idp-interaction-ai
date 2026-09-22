## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) as provided
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the provided text; no external data or supplementary materials were assessed
- **Shared manuscript claim summary** The authors explore the evolution and function of the intrinsically disordered region (IDR) of Drosophila Canoe and human Afadin, combining bioinformatic sequence analyses, structural predictions, and phenotypic characterization of a series of classical cno mutant alleles to argue that the IDR, particularly conserved motifs within it, is important for protein function during embryonic morphogenesis
- **Visible evidence base** Sequence alignments (Table 1; Figures 2-5), AlphaFold structural predictions (Figure 6), cuticle phenotype scoring (Table 2; Figures 9-10), immunofluorescence imaging (Figures 7, 11, 13), whole-genome sequencing and Sanger verification (Figure 8), and genetic interaction data (Figure 14)
- **Missing materials affecting confidence** Figure panels referenced but not fully described in text (e.g., exact composition of Figures 2, 3, 5); statistical details for phenotype scoring comparisons; raw sequencing data and variant calling metrics; details on antibody validation; exact sample sizes for some experiments; supplementary tables or datasets

## Reviewer
- **Overall assessment** This manuscript presents a thorough and well-structured analysis of the Canoe/Afadin IDR, combining evolutionary sequence comparisons with phenotypic analysis of a valuable allelic series. The bioinformatic work is careful and the identification of conserved motifs, some predicted to be helical, provides a useful foundation. The phenotypic data are descriptive but consistent with the hypothesis that the IDR contributes to Canoe function. However, the manuscript currently lacks direct functional evidence linking specific conserved motifs to biochemical activities, and the interpretation of the allelic series is complicated by the possibility of nonsense-mediated decay and the strong maternal contribution. The distinction between the "FAB" region and the newly highlighted internal actin-binding candidate is an important point that needs clearer experimental resolution. Overall, the work is of interest to the cell adhesion and morphogenesis community, but the central claims about IDR function are not yet fully established from the evidence provided.

- **Who would be interested in the results, and why** Cell and developmental biologists studying adherens junctions, cytoskeletal linkages, and morphogenesis will find this work relevant. Researchers interested in the evolution and function of intrinsically disordered regions in scaffolding proteins will also be interested. The allelic series and the bioinformatic approach provide a resource for those studying Canoe/Afadin function. The work may also appeal to those using AlphaFold predictions to generate hypotheses about IDR function.

- **Major strengths** The manuscript is clearly written and logically organized. The combination of evolutionary analysis with a genetic allelic series is a strength. The identification of conserved motifs within the IDR, particularly those predicted to be helical, provides a useful framework for future studies. The careful documentation of the phenotypic differences between zygotic and maternal/zygotic mutants is valuable. The authors are appropriately cautious in interpreting their data and acknowledge limitations, such as the potential for mRNA decay.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Functional evidence
- **Claim pointer** The manuscript claims that conserved motifs in the IDR, particularly those predicted to be alpha-helical, are likely to serve as binding sites for alpha-catenin and F-actin, and that these regions are important for Canoe function.
- **Evidence pointer** Results section "Published evidence supports the idea that structured conserved motifs in the IDR may be the actin and alpha-catenin binding sites"; Figures 4, 5, 6
- **Concern** The manuscript relies heavily on sequence conservation and AlphaFold predictions to suggest that specific motifs are functional binding sites. While the alpha-catenin binding site in Afadin aligns with a predicted helix, the manuscript does not provide direct biochemical or cell biological evidence that the corresponding region in Canoe binds alpha-catenin or F-actin. The discussion of the F-actin binding site is particularly problematic, as the authors themselves note discrepancies between different mapping studies. The claim that the internal conserved helices represent a bona fide actin-binding site is speculative without direct binding assays or mutagenesis experiments.
- **Why it matters** The central hypothesis of the manuscript is that the IDR, and specific motifs within it, are functionally important. Without direct evidence that these motifs mediate the proposed interactions, the functional significance of the conserved sequences remains correlative. The manuscript would be substantially strengthened by experimental validation of at least one of these predicted interactions.
- **Resolution test** Provide direct biochemical evidence (e.g., co-sedimentation, pull-down, or binding assays with purified proteins) that the conserved helical region in Canoe binds F-actin and/or alpha-catenin. Alternatively, generate mutations in the endogenous gene that specifically disrupt these motifs and show that they phenocopy the null or exhibit specific defects in junction-cytoskeleton linkage.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of genetic data
- **Claim pointer** The manuscript claims that the stronger phenotypes of alleles with stop codons early in the IDR (e.g., cno2, cnoR3, cnoR17) suggest that the IDR, including its C-terminal conserved motifs, is important for protein function, and that these alleles may have antimorphic effects.
- **Evidence pointer** Results sections "The zygotic phenotype of the original cno mutant..." and "Analysis of maternal/zygotic mutants..."; Figures 9, 10, 12
- **Concern** The interpretation of the allelic series is confounded by the lack of data on whether the truncated mRNAs or proteins are stable. The authors acknowledge this caveat but do not address it experimentally. If all truncation alleles are subject to nonsense-mediated decay, then the phenotypic differences between alleles may reflect differences in mRNA stability rather than the function of specific protein domains. The suggestion of antimorphic effects for early IDR truncations is speculative without evidence for stable truncated proteins.
- **Why it matters** The phenotypic differences between alleles are a key piece of evidence for the importance of the IDR. If these differences are due to mRNA decay rather than protein function, the conclusions about IDR function are weakened. The manuscript needs to rule out this alternative explanation to make the case that the IDR has specific functions.
- **Resolution test** Measure mRNA levels for each allele (e.g., by qPCR or RNA-seq) to determine if the truncation alleles are subject to nonsense-mediated decay. If possible, use antibodies that recognize N-terminal epitopes to detect truncated proteins. This would allow the authors to distinguish between loss-of-function and antimorphic effects.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative rigor
- **Claim pointer** The manuscript claims that the zygotic phenotypes of the different cno alleles vary in severity, with some alleles having stronger phenotypes than the null.
- **Evidence pointer** Results section "The zygotic phenotype of the original cno mutant..."; Figure 9, 10; Table 2
- **Concern** The phenotype scoring is presented as average cuticle scores, but the statistical analysis is not described in detail. It is unclear if the differences between alleles are statistically significant, and how many embryos were scored per genotype. The variability between experiments is not reported. The claim that certain alleles are "stronger" than the null would be more convincing with appropriate statistical tests and effect sizes.
- **Why it matters** The phenotypic comparisons are central to the argument that the IDR is important. Without rigorous quantitative analysis, it is difficult to assess the reliability of the reported differences. This is particularly important given the subtle nature of some of the phenotypes.
- **Resolution test** Provide a detailed description of the statistical methods used, including the number of embryos scored, the number of independent experiments, and the statistical tests performed. Report effect sizes and confidence intervals for the differences between alleles.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Evolutionary interpretation
- **Claim pointer** The manuscript claims that the IDRs of Canoe and Afadin have diverged dramatically in sequence and properties, yet both retain conserved motifs that are likely functionally important.
- **Evidence pointer** Results sections "The IDRs of Drosophila Cno and human Afadin have diverged..." and "Comparisons of IDRs reveals strong sequence conservation..."; Figures 2-5; Table 1
- **Concern** The manuscript documents the divergence of the IDR but does not provide a clear evolutionary framework for interpreting this divergence. The observation that the IDR is conserved within insects but not between insects and vertebrates is interesting, but the authors do not discuss what this means for the evolution of function. The identification of conserved motifs is useful, but the manuscript does not test whether these motifs are functionally equivalent across species.
- **Why it matters** The evolutionary analysis is a major component of the manuscript. A more nuanced interpretation of the patterns of conservation and divergence would strengthen the paper. The authors could discuss whether the IDR is under selective pressure to maintain certain features (e.g., helical propensity, charge) even as the sequence diverges.
- **Resolution test** Perform a more detailed evolutionary analysis, such as comparing the predicted structural features (e.g., helical propensity, disorder) across species, or testing whether the conserved motifs from different species can functionally substitute for each other in transgenic rescue experiments.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 6
- **Evidence pointer** Results section "Published evidence supports the idea..."
- **Issue** The description of Figure 6 is somewhat difficult to follow, particularly the relationship between the predicted helices, the conserved motifs, and the mapped binding sites. The figure itself is not provided, but the text could be clearer about which helices correspond to which motifs and binding sites.
- **Required correction** Consider revising the text to more clearly guide the reader through Figure 6, perhaps by explicitly stating which predicted helix corresponds to which conserved motif and which binding site.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods
- **Evidence pointer** Methods section "Antigen intensity comparison"
- **Issue** The description of the antigen intensity comparison is incomplete. The text mentions a Taylor's expansion to find the variance of the ratio, but the equation is not fully written out, and the statistical justification for this approach is not explained.
- **Required correction** Provide the full equation and a brief explanation of why this approach was used instead of a more standard method (e.g., bootstrap or a t-test on log-transformed values).

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion section "The IDRs of Cno and Afadin share very few commonalities"
- **Issue** The statement that the IDRs "share very few commonalities" is somewhat contradicted by the later discussion of conserved motifs and the shared FAB region. The authors should clarify what they mean by "commonalities" (e.g., sequence identity vs. structural features).
- **Required correction** Rephrase to distinguish between overall sequence identity and the presence of specific conserved motifs or features.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results
- **Evidence pointer** Results section "A series of classical cno mutants provide a potential resource..."
- **Issue** The text states that "one of these was no longer Balanced" but does not explain what this means for the analysis. It would be helpful to clarify whether this allele was excluded from the analysis.
- **Required correction** Add a brief explanation of the implications of the loss of the balancer and how this was handled in the analysis.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results
- **Evidence pointer** Results section "Loss of Sdk enhances the cno null zygotic phenotype..."
- **Issue** The genetic interaction between sdk and cno is presented as a single experiment. It would be helpful to know if this was replicated and if the effect was quantified in a way that allows comparison with the other alleles.
- **Required correction** Provide details on the number of embryos scored and whether the experiment was repeated. Consider presenting the data in a way that allows direct comparison with the other alleles.

## Risk / unsupported claims
- The claim that the conserved internal helices in the IDR represent a bona fide actin-binding site is unsupported by direct experimental evidence; the manuscript itself notes discrepancies in the literature.
- The suggestion that alleles with stop codons early in the IDR may have antimorphic effects is speculative and not supported by data on protein stability.
- The claim that the IDR is important for protein function is based on phenotypic correlations, but the lack of data on mRNA or protein stability for the truncation alleles weakens this claim.
- The evolutionary interpretation of IDR divergence is descriptive and does not test for functional conservation or selective pressures.
- The statistical significance of the differences in cuticle phenotype scores between alleles is not established from the provided text.