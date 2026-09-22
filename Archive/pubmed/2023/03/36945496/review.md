## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, and methods sections.
- **Assessment boundary** The review is limited to the scientific content, methodology, and conclusions presented in the provided manuscript. No external literature or unpublished data were consulted.
- **Shared manuscript claim summary** The manuscript explores the evolution and function of the intrinsically disordered region (IDR) of Drosophila Canoe and its human homolog Afadin. The authors combine bioinformatic sequence analysis, structural predictions, and genetic phenotypic analysis of a series of cno mutants to propose that the IDR, particularly conserved alpha-helical motifs within it, plays important roles in linking cell-cell junctions to the cytoskeleton during embryonic morphogenesis.
- **Visible evidence base** The evidence base includes: (1) sequence alignments and conservation analyses of Canoe/Afadin orthologs across insects and vertebrates; (2) AlphaFold structural predictions of the IDR; (3) identification of molecular lesions in 18 classical cno mutants via whole-genome sequencing; (4) cuticle phenotype scoring of zygotic mutants; (5) immunofluorescence analysis of maternal/zygotic mutant embryos; (6) AlphaFold-Multimer modeling of the afadin/alpha-catenin interaction.
- **Missing materials affecting confidence** The manuscript does not provide: (1) direct biochemical evidence for the proposed actin-binding or alpha-catenin-binding activities of the conserved IDR motifs; (2) quantitative data on mRNA or protein stability for the truncation alleles; (3) detailed statistical analysis of phenotype distributions beyond mean scores; (4) raw sequencing data or variant calling details; (5) information on whether the alternative splice isoforms are translated into stable proteins.

## Reviewer
- **Overall assessment** This manuscript presents a comprehensive and well-structured analysis of the Canoe/Afadin IDR, combining evolutionary sequence analysis with genetic resources to generate testable hypotheses about IDR function. The bioinformatic work is thorough, and the identification of conserved motifs, some of which align with predicted alpha-helices and known binding sites, is a valuable contribution. The phenotypic analysis of the classical mutants provides a useful resource, and the observation that truncations early in the IDR produce stronger phenotypes than the null allele is intriguing. However, the manuscript is largely descriptive and hypothesis-generating. The central claims about the functional importance of specific IDR motifs, particularly the proposed actin-binding and alpha-catenin-binding regions, are not directly tested. The interpretation of the mutant phenotypes is complicated by the lack of protein-level data for the truncation alleles, leaving open the possibility that mRNA decay, rather than the position of the truncation, drives the observed severity. The manuscript would be significantly strengthened by direct biochemical or cell biological experiments to test the proposed functions of the conserved motifs.

- **Who would be interested in the results, and why** This work will be of interest to cell and developmental biologists studying adherens junction dynamics, cytoskeletal linkage, and morphogenesis. The evolutionary analysis of the IDR will also appeal to researchers interested in the evolution of intrinsically disordered regions and their role in protein function. The detailed characterization of the cno mutant alleles provides a valuable genetic resource for the Drosophila community. The use of AlphaFold to predict structured motifs within IDRs is a timely methodological contribution that may be of broader interest.

- **Major strengths**
    1. The bioinformatic analysis is rigorous and clearly presented, with a logical progression from overall sequence divergence to identification of conserved motifs.
    2. The combination of evolutionary analysis with a panel of classical mutants is a powerful approach to generate functional hypotheses.
    3. The observation that the IDR is under different selective pressures in insects versus vertebrates, and the identification of a shared potential actin-binding region, is a novel and interesting finding.
    4. The phenotypic analysis is carefully scored and quantified, and the comparison between zygotic and maternal/zygotic phenotypes is informative.
    5. The discussion of the discrepancies in the literature regarding the F-actin binding site is thoughtful and highlights important unresolved questions.

- **Major Concerns**

    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Functional validation of proposed binding motifs
    - **Claim pointer** The manuscript claims that conserved alpha-helical motifs in the IDR, particularly those matching the alpha-catenin binding site and the actin-binding region identified by Carminati et al., are likely to be functionally important for linking junctions to the cytoskeleton.
    - **Evidence pointer** Results section "Published evidence supports the idea that structured conserved motifs in the IDR may be the actin and alpha-catenin binding sites"; Figures 4, 5, and 6.
    - **Concern** The manuscript identifies conserved motifs and correlates them with previously mapped binding sites, but provides no direct experimental evidence that these motifs in Canoe or Afadin actually bind alpha-catenin or F-actin. The AlphaFold-Multimer prediction of the afadin/alpha-catenin interaction is suggestive but not a substitute for biochemical validation. The claim that these motifs are "likely to be functionally important" is therefore speculative.
    - **Why it matters** The central hypothesis of the paper is that specific regions of the IDR mediate critical protein-protein interactions. Without direct binding assays (e.g., co-immunoprecipitation, pull-downs, or in vitro binding with purified proteins), the functional significance of these conserved motifs remains unproven. The paper's contribution is weakened by not testing its own central hypothesis.
    - **Resolution test** Provide direct biochemical evidence that the identified conserved motifs bind to alpha-catenin and F-actin. This could be achieved through co-immunoprecipitation of full-length and truncated constructs, or in vitro binding assays with purified recombinant proteins. Mutating key conserved residues within these motifs should abolish or reduce binding.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Interpretation of mutant phenotypes without protein-level data
    - **Claim pointer** The manuscript claims that the position of the truncation in the IDR correlates with phenotypic severity, with truncations early in the IDR producing stronger phenotypes than the null allele, suggesting a dominant-negative or antimorphic effect.
    - **Evidence pointer** Results section "The zygotic mutant phenotypes of the alleles vary in their severity and those with the strongest phenotypes cluster near the beginning of the IDR"; Figures 9 and 10.
    - **Concern** The interpretation of the phenotypic differences between alleles relies on the assumption that the truncated proteins are expressed. However, the manuscript does not provide any data on mRNA or protein levels for the mutant alleles. It is possible that the stronger phenotypes observed for early truncations are due to more efficient nonsense-mediated mRNA decay, resulting in a more complete loss of function, rather than a dominant-negative effect of a stable truncated protein. The authors acknowledge this caveat but do not address it experimentally.
    - **Why it matters** The conclusion that the IDR has specific functions beyond simple tethering, and that certain truncations have antimorphic activity, is a key finding. Without evidence that the truncated proteins are actually produced, this conclusion is not supported. The alternative explanation of differential mRNA decay is equally consistent with the data.
    - **Resolution test** Measure mRNA levels (e.g., by qRT-PCR) and protein levels (e.g., by western blot with an N-terminal antibody) for each mutant allele. If truncated proteins are not detected, the phenotypic differences must be attributed to differences in mRNA stability, not protein function.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Generalizability of findings to Afadin function
    - **Claim pointer** The manuscript uses the evolutionary conservation between Drosophila Canoe and human Afadin to suggest that the identified motifs, particularly the potential actin-binding region, are functionally relevant in both organisms.
    - **Evidence pointer** Results section "Sequence comparison reveals conserved motifs in both insect and vertebrate IDRs..."; Figures 4 and 5.
    - **Concern** While the sequence conservation is interesting, the manuscript does not test whether the identified motifs in Afadin have similar functions to those proposed for Canoe. The functional data is entirely from Drosophila. The claim that these motifs are important for Afadin function is an extrapolation.
    - **Why it matters** The title and introduction frame the study as relevant to both Canoe and Afadin. To support this, some functional validation in a vertebrate system, or at least a more detailed discussion of the potential differences, is needed. Without it, the relevance of the findings to mammalian systems is unclear.
    - **Resolution test** Perform a comparable functional analysis of the Afadin IDR in a mammalian cell culture system, or at minimum, test whether the conserved motifs in Afadin can bind to alpha-catenin and F-actin in vitro.

- **Minor Comments**

    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Statistical analysis of phenotype scores
    - **Affected element** Figure 10 and Table 2
    - **Evidence pointer** Results section "The zygotic mutant phenotypes of the alleles vary in their severity..."
    - **Issue** The manuscript reports average cuticle scores for each allele but does not provide a statistical comparison between alleles. It is unclear if the differences in mean scores are statistically significant, particularly for alleles with similar scores.
    - **Required correction** Provide a statistical analysis (e.g., ANOVA with post-hoc tests) to compare the distribution of phenotype scores between genotypes. This would strengthen the claim that certain alleles are significantly stronger or weaker than others.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Clarity of mutant allele nomenclature
    - **Affected element** Results section "A series of classical cno_mutants provide a potential resource for assessing regions of the IDR"
    - **Evidence pointer** Figure 8B
    - **Issue** The manuscript refers to the cnoRX alleles but does not clearly explain the nomenclature or the genetic background of each allele. This makes it difficult for readers to understand the origin and potential differences between the alleles.
    - **Required correction** Add a supplementary table or a more detailed description in the text that lists each allele, its mutagenesis method, genetic background, and the specific molecular lesion identified.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Discussion of alternative splice isoforms
    - **Affected element** Results section "The IDRs of Drosophila Cno and human Afadin have diverged..."
    - **Evidence pointer** Location not provided
    - **Issue** The manuscript mentions alternative splice isoforms of Cno that replace the IDR, but does not discuss the potential functional implications of these isoforms in any detail. This is an interesting observation that could be relevant to the function of the IDR.
    - **Required correction** Expand the discussion to consider the potential roles of the alternative isoforms, such as whether they might have dominant-negative or neomorphic functions, and how their expression is regulated.

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Methodological detail for AlphaFold-Multimer
    - **Affected element** Methods section "Structural predictions"
    - **Evidence pointer** Methods section
    - **Issue** The methods for the AlphaFold-Multimer prediction are brief. It is unclear how the input sequences were selected, how many models were generated, and what the confidence scores were for the top-ranked model beyond the single value reported.
    - **Required correction** Provide more details on the AlphaFold-Multimer run, including the input sequences used, the number of models generated, and a plot or table of the confidence scores for the top models.

- **Technical failings that need to be addressed before the case is established**
    1. Lack of direct biochemical validation of the proposed actin-binding and alpha-catenin-binding motifs (R1-M1).
    2. Absence of protein-level data for the truncation alleles, which is essential for interpreting the phenotypic differences (R1-M2).
    3. The statistical significance of the phenotype scoring differences is not established.

- **Assessment against Nature-style criteria**
    - **Originality** The work is original in its comprehensive approach to analyzing the Canoe/Afadin IDR, combining evolutionary analysis with a genetic resource. The identification of a potential shared actin-binding motif between insects and vertebrates is a novel observation.
    - **Scientific importance** The manuscript addresses an important question about the function of IDRs in a key developmental protein. However, the lack of direct functional testing limits the immediate impact of the findings. The work is more hypothesis-generating than hypothesis-testing.
    - **Interdisciplinary readership** The topic is of interest to cell and developmental biologists, and the evolutionary analysis may appeal to a broader audience. However, the specialized nature of the Drosophila genetics and the lack of direct biochemical data may limit its appeal to a very broad interdisciplinary readership.
    - **Technical soundness** The bioinformatic and genetic analyses appear technically sound. The whole-genome sequencing and variant calling are appropriate. The phenotypic analysis is carefully done. The main technical weakness is the lack of protein-level data and direct binding assays.
    - **Readability for nonspecialists** The manuscript is generally well-written and accessible. The introduction and discussion are clear. However, the results section is dense with detail and may be challenging for a nonspecialist to follow. The figures are helpful but some are complex.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a valuable resource and generates interesting hypotheses, but the central claims about the function of specific IDR motifs are not directly tested. The authors should be encouraged to add direct biochemical or cell biological experiments to validate the proposed binding interactions and to provide protein-level data for the mutant alleles. With these additions, the manuscript would be significantly strengthened and would make a more compelling contribution.

## Risk / unsupported claims
- The claim that the conserved alpha-helical motifs in the IDR are the actin-binding and alpha-catenin-binding sites is unsupported by direct experimental evidence.
- The claim that truncations early in the IDR have a dominant-negative or antimorphic effect is unsupported without data on protein expression levels.
- The claim that the identified motifs are functionally important in Afadin is an extrapolation from Drosophila data and is not directly supported.
- The suggestion that the alternative splice isoforms of Cno may have distinct functions is speculative and not tested.