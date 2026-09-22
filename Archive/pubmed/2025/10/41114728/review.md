## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and figure legends as provided.
- **Assessment boundary** Scientific content, methodological soundness, validity of claims relative to evidence presented, and alignment with Nature-style criteria. No assessment of formatting, grammar, or editorial policy.
- **Shared manuscript claim summary** The authors use the ESM2 protein language model to map residue-level mutational tolerance in intrinsically disordered regions (IDRs) of proteins associated with membraneless organelle (MLO) formation. They report that a subset of disordered residues shows high evolutionary conservation, that these conserved residues are enriched in regions experimentally implicated in driving phase separation, and that they form continuous motifs containing both traditional "sticker" and "spacer" residues. The authors propose these motifs as functional units under evolutionary selection to support stable MLO formation.
- **Visible evidence base** Main text figures 1–5 and supplementary figures as referenced; methods descriptions for dataset construction, ESM2 scoring, conservation analysis, and motif identification; supplementary files referenced but not provided in full.
- **Missing materials affecting confidence** Supplementary figure files (Figure 2—figure supplements 1–2, Figure 3—figure supplement 1, Figure 4—figure supplements 1–6, Figure 5—figure supplements 1–3) were not provided. Supplementary data files (MLO-hIDR.csv, dMLO-IDR.csv, ESM2_motif_with_exp_ref.csv) were referenced but not provided. Statistical test details and effect sizes for comparisons in Figures 2C–D, 3B–C, and 4C were not fully described in the visible text.

## Reviewer

- **Overall assessment** This manuscript presents a conceptually interesting application of a protein language model to study evolutionary constraints in IDRs relevant to phase separation. The central observation, that ESM2 identifies conserved disordered residues enriched in phase-separating regions, is potentially valuable. However, the evidence as presented has several gaps that prevent full confidence in the conclusions. The statistical robustness of key comparisons is not fully documented, the functional interpretation of conserved motifs relies on indirect evidence, and the authors themselves acknowledge a non-significant difference in their main enrichment analysis (Figure 4—figure supplement 6). The work is likely of interest to the phase separation and IDP communities, but the strength of the claims currently exceeds what the visible evidence supports.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates and phase separation, particularly those interested in sequence determinants of MLO formation. Also relevant to computational biologists working on protein language model applications beyond folded domains, and evolutionary biologists studying constraints in disordered regions. The potential clinical link via ClinVar analysis may interest those studying disease-associated mutations in IDRs.

- **Major Strengths**
  - Novel application of ESM2 to IDR analysis, addressing a known alignment challenge in disordered regions.
  - Integration of multiple computational approaches (ESM2, AlphaFold2 pLDDT, HHblits MSA) to cross-validate findings.
  - The concept of conserved motifs combining stickers and spacers is a useful refinement of the stickers-and-spacers framework.
  - The authors are transparent about limitations, including the non-significant enrichment result and the lack of direct experimental validation.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical validity
- **Claim pointer** The claim that "regions associated with phase separation are significantly enriched in these conserved residues" (Abstract and Results section "Regions driving phase separation are enriched with conserved, disordered residues").
- **Evidence pointer** Figure 4C and Figure 4—figure supplement 6; Discussion section
- **Concern** The authors state in the Discussion that the difference between the distribution of p (probability of finding conserved residues in phase-separating regions) and 1-p is "not statistically significant." This directly contradicts the claim of significant enrichment made in the Abstract and Results. The main evidence for enrichment (Figure 4C) appears to be a visual comparison without reported statistical testing. The manuscript does not provide effect sizes, confidence intervals, or test statistics for the key comparisons in Figure 4C.
- **Why it matters** The central conclusion of the paper, that phase-separating IDRs are enriched in conserved residues, rests on this comparison. If the enrichment is not statistically significant, the primary claim is unsupported.
- **Resolution test** Provide appropriate statistical tests (e.g., permutation tests, mixed-effects models accounting for within-protein correlation) for the comparison of conserved residue density between dMLO-IDR, cMLO-IDR, and nMLO-IDR groups. Report effect sizes and confidence intervals. If the difference is not significant, revise the claims accordingly.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal inference
- **Claim pointer** The claim that conserved motifs "may act as functional units under evolutionary selection to support stable MLO formation" (Abstract) and that "conserved motifs likely engage in stronger interactions that drive phase separation" (Discussion).
- **Evidence pointer** Results section "Conserved, disordered residues form motifs"; Figure 5; Discussion section
- **Concern** The manuscript demonstrates correlation between conserved motifs and experimentally mapped phase-separating regions, but does not provide direct evidence that these motifs are causal for phase separation. The authors acknowledge this in the Limitations section, yet the Abstract and Discussion present the functional role as a finding rather than a hypothesis. The ClinVar analysis (Figure 5—figure supplement 3) is suggestive but does not establish mechanism.
- **Why it matters** The proposed functional significance of the motifs is a key part of the paper's impact. Without direct experimental evidence (e.g., mutagenesis of motifs within phase-separating regions), the claim remains speculative.
- **Resolution test** Either temper the language to clearly frame the functional role as a hypothesis, or provide additional evidence such as computational predictions of interaction strength for motif versus non-motif regions, or cite existing experimental data that directly tests motif function.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Methodological validation
- **Claim pointer** The claim that ESM2 scores effectively capture evolutionary conservation in IDRs, independent of alignment.
- **Evidence pointer** Results section "ESM2 scores correlate with sequence conservation"; Figure 3B–C
- **Concern** The correlation between ESM2 scores and conservation scores is presented, but the manuscript does not report the correlation coefficient or its significance. The analysis excludes methionine due to its position as a start codon, but other potential confounders (e.g., low-complexity regions, repeat sequences) are not addressed. The use of HHblits for MSA in disordered regions, while reasonable, may still introduce alignment biases that the authors do not fully discuss.
- **Why it matters** The validity of ESM2 as a proxy for conservation in IDRs underpins the entire analysis. If the correlation is weak or confounded, the interpretation of low ESM2 scores as indicating conservation is compromised.
- **Resolution test** Report the correlation coefficient (e.g., Spearman's rho) with confidence intervals for the ESM2-conservation relationship. Perform sensitivity analyses excluding low-complexity regions or using alternative alignment methods. Discuss potential biases in HHblits alignments for disordered sequences.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Definition of "conserved disordered" residues
- **Evidence pointer** Results section "ESM2 identifies conserved, disordered residues"; Figure 2C–D
- **Issue** The threshold for classifying a residue as "conserved disordered" (low ESM2 score) is not explicitly defined. The text refers to "region I" in Figure 2D but does not state the numerical ESM2 score cutoff used.
- **Required correction** State the specific ESM2 score threshold used to define conserved residues, and justify this choice.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Motif identification algorithm
- **Evidence pointer** Methods section "Motif identification"
- **Issue** The bidirectional overlap procedure for motif identification is described, but the merging criterion (within 8 residues) appears arbitrary. The sensitivity of results to this parameter is not tested.
- **Required correction** Provide a sensitivity analysis for the merging distance parameter, or justify the choice based on prior literature.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Supplementary data files
- **Evidence pointer** Data availability section
- **Issue** The manuscript references supplementary files (MLO-hIDR.csv, dMLO-IDR.csv, ESM2_motif_with_exp_ref.csv) that were not provided for review. These files are essential for verifying the motif lists and experimental references.
- **Required correction** Ensure all supplementary data files are made available for review and publication.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** ClinVar analysis
- **Evidence pointer** Discussion section; Figure 5—figure supplement 3
- **Issue** The ClinVar analysis is presented as supporting clinical relevance, but the text does not specify how many variants were analyzed, the proportion of pathogenic variants within motifs versus outside, or whether the enrichment is statistically significant.
- **Required correction** Provide quantitative details of the ClinVar analysis, including sample sizes and statistical tests.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: The central enrichment claim is contradicted by the authors' own statement of non-significance. This must be resolved with appropriate statistics or revised claims.
  - R1-M2: The functional interpretation of motifs as drivers of phase separation is not directly supported by the evidence presented.
  - R1-M3: The correlation between ESM2 scores and conservation is not quantified, and potential confounders are not addressed.

- **Assessment against Nature-style criteria**
  - **Originality**: Moderate to high. Applying protein language models to IDR analysis is a relatively novel approach, and the concept of conserved motifs spanning stickers and spacers offers a new perspective. However, the idea that IDRs contain functionally important conserved elements is not entirely new.
  - **Scientific importance**: Moderate. Understanding sequence determinants of phase separation is an active and important area. If the claims were fully supported, this could provide a useful computational tool for identifying functional elements in IDRs. However, the current evidence does not establish the central claim of enrichment.
  - **Interdisciplinary readership**: The topic bridges computational biology, biophysics, and cell biology. The use of ESM2 may attract readers from the machine learning community. However, the presentation assumes familiarity with phase separation concepts and may not be fully accessible to nonspecialists.
  - **Technical soundness**: The computational pipeline is reasonable, but key statistical analyses are missing or underreported. The reliance on a single protein language model and a single conservation metric limits robustness. The lack of direct experimental validation is a significant gap.
  - **Readability for nonspecialists**: The manuscript is generally well-written, but the methods sections are dense. The abstract and introduction are accessible, but the results would benefit from clearer explanations of the statistical approaches and their limitations.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript presents an interesting approach and potentially valuable observations, but the central claim of enrichment of conserved residues in phase-separating regions is not statistically supported as presented. The functional interpretation of motifs requires additional evidence. The authors should be encouraged to revise with appropriate statistical analyses and more cautious claims, or to provide additional data that directly tests the functional role of the identified motifs.

## Risk / unsupported claims
- The claim of "significant enrichment" of conserved residues in phase-separating regions is unsupported and contradicted by the authors' own statement of non-significance.
- The claim that conserved motifs "act as functional units under evolutionary selection to support stable MLO formation" is not directly supported by the evidence; it is a reasonable hypothesis but presented as a finding.
- The claim that ESM2 effectively captures evolutionary conservation in IDRs is only weakly supported without reported correlation coefficients or sensitivity analyses.
- The clinical relevance implications drawn from the ClinVar analysis are not quantitatively supported in the visible text.
- The generalizability of findings beyond the specific dataset (939 human MLO-associated proteins) is not established.