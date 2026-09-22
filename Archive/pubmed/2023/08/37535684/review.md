## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, data interpretation, and conclusions as presented in the manuscript
- **Shared manuscript claim summary** The authors investigate the intrinsically disordered region (IDR) of Drosophila Canoe and its human homolog Afadin, combining bioinformatic analyses of sequence conservation and structural predictions with genetic analyses of a series of cno mutant alleles to explore IDR evolution and function in linking adherens junctions to the actin cytoskeleton during embryonic morphogenesis.
- **Visible evidence base** Abstract, Introduction, Results, Discussion, Methods, figure legends referenced in text (figures themselves not provided)
- **Missing materials affecting confidence** Figures and supplementary data not provided; raw sequencing data not available for independent verification; statistical details for quantitative comparisons not fully described

## Reviewer
- **Overall assessment** This manuscript presents a comprehensive bioinformatic and genetic analysis of the Canoe/Afadin IDR, providing valuable evolutionary insights and a genetic resource for future functional studies. The work is carefully executed and the conclusions are generally well-supported by the data presented. However, several technical concerns regarding the interpretation of mutant phenotypes and the strength of evolutionary claims require attention. The manuscript would benefit from clearer presentation of quantitative data and more explicit discussion of limitations.

- **Who would be interested in the results, and why** Cell and developmental biologists studying adherens junction dynamics, cytoskeletal linkages, and morphogenesis will find this work relevant. Evolutionary biologists interested in IDR evolution and the functional constraints on disordered regions will also be engaged. The genetic reagents and bioinformatic approach may interest Drosophila geneticists and researchers studying scaffold proteins.

- **Major strengths** The study addresses an important and under-explored question about the function of a large IDR in a key junctional protein. The combination of evolutionary analysis with genetic reagents is powerful. The identification of conserved motifs within otherwise divergent IDRs, and the correlation with predicted alpha-helical structures, provides a solid foundation for future mechanistic studies. The careful documentation of maternal contribution and its impact on phenotypic interpretation is commendable.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Data interpretation
  - **Claim pointer** The authors claim that alleles with stop codons early in the IDR have phenotypes more severe than those of zygotic null alleles, suggesting possible dominant-negative effects.
  - **Evidence pointer** Results section "The zygotic phenotype of the original cno mutant that gave the gene its name is paradoxically stronger than that of the null cno allele"; Figure 10; Table 1
  - **Concern** The interpretation that early IDR truncations produce dominant-negative effects is based on phenotypic severity comparisons between alleles on different genetic backgrounds. While the authors attempt to address this with the cnoR3 allele on the same background as cnoR2, the data are not fully convincing. The claim of antimorphic effects requires direct evidence of protein production from these alleles and demonstration of interference with wild-type function. The authors acknowledge this limitation but do not provide sufficient experimental support for the dominant-negative interpretation.
  - **Why it matters** This interpretation is central to the paper's conclusion that the IDR is functionally important. If the phenotypic differences are due to background effects or haploinsufficiency rather than dominant-negative mechanisms, the conclusions about IDR function would be weakened.
  - **Resolution test** Direct detection of truncated proteins from these alleles (e.g., by western blot with an N-terminal antibody), or genetic rescue experiments with wild-type transgenes, would clarify whether the truncated proteins are produced and whether they interfere with wild-type function.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Evolutionary interpretation
  - **Claim pointer** The authors claim that the IDRs of Canoe and Afadin "differ dramatically in sequence and sequence properties" and that this reflects rapid divergence.
  - **Evidence pointer** Results section "The IDRs of Drosophila Cno and human Afadin have diverged in length, sequence, amino acid composition, and charge"; Figures 1-2
  - **Concern** The comparison between Drosophila and human IDRs is limited to two species at the extremes of a large evolutionary distance. The claim of "dramatic" divergence would be strengthened by including intermediate species to trace the trajectory of change. Additionally, the functional significance of differences in amino acid composition (e.g., glutamine enrichment in Drosophila vs. proline/glutamic acid/arginine in human) is not discussed in terms of potential functional consequences.
  - **Why it matters** Understanding whether the observed differences reflect neutral drift or functional adaptation requires a more nuanced evolutionary analysis. The current comparison cannot distinguish between these possibilities.
  - **Resolution test** Including additional insect and vertebrate species in the analysis, and testing whether the conserved motifs identified within each lineage are functionally interchangeable, would strengthen the evolutionary conclusions.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical methodology
  - **Claim pointer** The authors use AlphaFold predictions to identify alpha-helical regions within the IDR and suggest these may be functional binding sites.
  - **Evidence pointer** Results section "Published evidence supports the idea that structured conserved motifs in the IDR may be the actin and alpha-catenin binding sites"; Figure 7
  - **Concern** AlphaFold predictions of structure within IDRs should be interpreted with caution, as these regions are by definition disordered and predictions may not reflect the conformational ensemble in solution. The authors do not validate these predictions experimentally (e.g., by circular dichroism, NMR, or mutagenesis). The claim that predicted helices correspond to functional binding sites requires experimental support.
  - **Why it matters** The identification of specific functional motifs within the IDR is a key contribution of this work. If the structural predictions are inaccurate, the proposed functional significance of these regions would be called into question.
  - **Resolution test** Experimental validation of the predicted helical regions (e.g., by mutagenesis disrupting the helix and testing binding or function) would confirm their functional relevance.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Figure 11A
  - **Evidence pointer** Results section "The zygotic mutant phenotypes of the alleles vary in their severity and those with the strongest phenotypes cluster near the beginning of the IDR"
  - **Issue** The figure plotting phenotype severity against mutation position is not provided, making it difficult to assess the clustering claim visually.
  - **Required correction** Ensure the figure clearly shows the relationship between mutation position and phenotype severity, with alleles labeled.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** Table 2
  - **Evidence pointer** Results section "Analysis of maternal/zygotic mutants reveals that alleles truncating the coding sequence at different places all lead to very strong loss of function"
  - **Issue** The viability data in Table 2 are described but statistical analysis is not reported. It is unclear whether the differences between alleles are statistically significant.
  - **Required correction** Provide statistical tests for the viability comparisons and report p-values or confidence intervals.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Discussion of F-actin binding site discrepancy
  - **Evidence pointer** Results section "Published evidence supports the idea that structured conserved motifs in the IDR may be the actin and alpha-catenin binding sites"; Discussion
  - **Issue** The authors note discrepancies in the mapping of the F-actin binding site between studies but do not fully resolve or discuss the implications of these discrepancies for their own conclusions.
  - **Required correction** Expand the discussion to address how the conflicting data affect the interpretation of which regions are functionally important for actin binding.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Methodology
  - **Affected element** Antisera validation
  - **Evidence pointer** Methods section "Embryo fixation and immunofluorescence"
  - **Issue** The specificity of the C-terminal anti-Canoe antibody used for immunofluorescence is not discussed. Given that many mutant alleles truncate the protein, antibody specificity is critical for interpreting staining results.
  - **Required correction** Include validation data for the antibody (e.g., staining in null mutant embryos) or reference previous publications where this was established.

- **Technical failings that need to be addressed before the case is established** R1-M1 (dominant-negative interpretation requires direct evidence), R1-M3 (AlphaFold predictions require experimental validation)

- **Assessment against Nature-style criteria**
  - **Originality** The work addresses a relatively under-explored area, the function of a large IDR in a junctional scaffold protein, and provides a novel genetic resource. However, the conceptual framework is not entirely new, as IDR function in other proteins has been studied.
  - **Scientific importance** The findings are of interest to the cell and developmental biology community, but the significance is incremental rather than transformative. The work provides a foundation for future studies rather than a major conceptual advance.
  - **Interdisciplinary readership** The work will primarily appeal to specialists in Drosophila genetics, adherens junction biology, and IDR evolution. The interdisciplinary reach is moderate.
  - **Technical soundness** The bioinformatic analyses are appropriate, and the genetic approach is sound. However, the lack of experimental validation for structural predictions and the unresolved dominant-negative question are technical weaknesses.
  - **Readability for nonspecialists** The manuscript is generally well-written and accessible, though some sections assume familiarity with Drosophila genetics and morphogenesis. The abstract effectively summarizes the key findings.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a valuable resource and interesting evolutionary observations, but the central claims about IDR function would be strengthened by addressing the concerns raised, particularly regarding the dominant-negative interpretation and experimental validation of predicted structural motifs.

## Risk / unsupported claims
- The claim that early IDR truncations may have dominant-negative effects is not directly supported by the data presented; it remains a hypothesis requiring experimental testing.
- The suggestion that AlphaFold-predicted alpha-helical regions in the IDR represent functional binding sites is speculative without experimental validation.
- The statement that the IDR is "critical for protein function" based on maternal/zygotic mutant phenotypes is supported, but the specific contributions of individual conserved motifs remain untested.
- The evolutionary interpretation that IDR divergence reflects different selective pressures in insects versus vertebrates is plausible but not rigorously tested with appropriate statistical methods.