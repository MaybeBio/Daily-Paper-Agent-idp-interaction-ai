## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv)
- **Assessment boundary** Scientific claims, methodology, evidence quality, and internal consistency as presented in the provided text
- **Shared manuscript claim summary** The authors use the ESM2 protein language model to map mutational tolerance across intrinsically disordered regions (IDRs) of human proteins associated with membraneless organelles. They report that a substantial subset of disordered residues exhibit low ESM2 scores (high predicted mutational constraint), that these scores correlate with sequence conservation from multiple sequence alignments, that phase-separation-driving IDRs are enriched for such conserved residues, and that these residues form contiguous motifs containing both "sticker" and "spacer" amino acids. They propose these motifs as evolutionarily selected functional units.
- **Visible evidence base** Main text figures referenced (Figures 1–5), supplementary figures referenced (Figures S1–S12), methods descriptions, appendix file names
- **Missing materials affecting confidence** Actual figure images, supplementary figure content, appendix CSV files, exact numerical values, statistical test details, dataset composition details, and code outputs are not provided in the supplied text

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting application of a protein language model to a biologically important problem, with a plausible pipeline from prediction to conservation analysis to motif identification. However, the evidence as described has several gaps that prevent full evaluation of the central claims. The correlation between ESM2 scores and conservation is asserted but not quantified in the text. The enrichment analysis in Figure 4 lacks statistical detail. The motif definition and merging procedure are described but their biological validation rests on previously published experimental data that is not directly assessed here. The authors are appropriately cautious in the Discussion, acknowledging that the link between conserved residues and phase-separation regions is not statistically significant in their own analysis. Overall, the work is promising but the case for evolutionarily selected functional motifs is not fully established from the provided evidence.
- **Who would be interested in the results, and why** Researchers studying phase separation and membraneless organelles, computational biologists working on protein language model applications, evolutionary biologists interested in disordered protein regions, and scientists studying the molecular grammar of condensate formation. The potential clinical link via ClinVar analysis would also interest researchers in human genetics and disease mechanisms.
- **Major strengths** 1) Novel application of a protein language model to IDR analysis, addressing a known alignment challenge. 2) Integration of multiple computational approaches (ESM2, AlphaFold2 pLDDT, HHblits MSA) to triangulate on conserved disordered residues. 3) The finding that "spacer" residues are conserved within motifs challenges simple stickers-and-spacers models and offers a refined view. 4) The authors acknowledge limitations and include a quantitative caveat about the enrichment analysis in the Discussion.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantification of ESM2-conservation correlation), R1-M2 (statistical support for enrichment claim), R1-M3 (motif definition sensitivity and validation)
- **Assessment against Nature-style criteria** **Originality:** High. Applying ESM2 to IDR mutational landscapes and linking to phase separation is a fresh angle. **Scientific importance:** Potentially high, as it could refine the stickers-and-spacers framework and offer a predictive tool for functional IDR elements. **Interdisciplinary readership:** Moderate to high, spanning computational biology, biophysics, cell biology, and evolutionary biology. **Technical soundness:** Partially established. The methods are reasonable but key quantitative validations are missing from the text. **Readability for nonspecialists:** Generally clear, though some methods details (e.g., ESM2 score definition) could be better contextualized for a broad audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is valuable and the pipeline is sensible, but the manuscript needs stronger quantitative evidence and clearer statistical framing to establish the central claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** "Our findings reveal a strong correlation between ESM2 scores and conservation scores" (Results, section "ESM2 Scores Correlate with Sequence Conservation")
- **Evidence pointer** Figure 3B, Figure 3C; location not provided for specific values
- **Concern** The text asserts a "strong correlation" between ESM2 scores and conservation scores but provides no correlation coefficient, significance value, or effect size. Figure 3B is described as histograms, and Figure 3C shows average values per amino acid type, but neither is quantified in the text.
- **Why it matters** The correlation between ESM2 predictions and evolutionary conservation is the foundational validation for using ESM2 as a proxy for functional constraint in IDRs. Without quantitative evidence, the reader cannot assess the strength or reliability of this relationship, which underpins all subsequent claims.
- **Resolution test** Provide the correlation coefficient (e.g., Spearman's rho) with confidence intervals and p-values for the ESM2-conservation relationship, both at the per-residue level and per-amino-acid level. Report these for each structural order group separately.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical support
- **Claim pointer** "Regions Driving Phase Separation Are Enriched with Conserved, Disordered Residues" (Results section title); "there is a progressive increase in the fraction of conserved disordered residues and a corresponding decline in flexible disordered residues from non-phase-separating proteins to clients and drivers" (Results, section "Regions Driving Phase Separation Are Enriched with Conserved, Disordered Residues")
- **Evidence pointer** Figure 4A, Figure S7; location not provided for statistical details
- **Concern** The enrichment claim is central to the paper's thesis, but no statistical test is described for the comparison across groups (nMOL-hIDR, cMLO-hIDR, dMLO-hIDR, dMLO-IDR). The text mentions "progressive increase" and "significant" in the abstract, but the methods do not specify what test was used, how multiple comparisons were handled, or what the effect sizes were.
- **Why it matters** The claim that phase-separation-driving IDRs are enriched for conserved residues is the key biological finding. Without proper statistical support, the reader cannot determine whether the observed differences are robust or could arise from dataset composition, sample size, or confounding variables.
- **Resolution test** Describe the statistical test used (e.g., Mann-Whitney U, permutation test), report p-values with multiple-comparison correction, and provide effect sizes (e.g., Cohen's d or median differences) for pairwise comparisons between groups. Also address potential confounders such as IDR length, amino acid composition, or protein expression levels.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological robustness
- **Claim pointer** "Conserved, Disordered Residues Form Motifs" (Results section title); "we identified ESM2 'motifs' as continuous sequence regions with average ESM2 scores below 0.5"
- **Evidence pointer** Figure 5, Methods section "Motif Identification"; location not provided for sensitivity analyses
- **Concern** The motif definition relies on an arbitrary threshold (average ESM2 score below 0.5) and a merging rule (within 8 residues). The text states that varying minimal motif length does not alter conclusions (Figure S10B), but no sensitivity analysis is described for the score threshold or the merging distance. The biological validation rests on overlap with previously published experimentally verified segments, but the text does not specify how many motifs overlap, what fraction of the experimentally defined regions are covered, or whether the overlap is statistically significant.
- **Why it matters** The motif concept is the paper's main output and proposed functional unit. If the definition is highly sensitive to arbitrary parameters, the motifs may not be robust biological features. The validation against experimental data is crucial for establishing that these computational motifs have functional relevance, but the current description is insufficient to assess this.
- **Resolution test** Perform and report a sensitivity analysis varying the ESM2 score threshold (e.g., 0.3, 0.4, 0.6, 0.7) and merging distance (e.g., 4, 6, 10, 12 residues), showing that the enrichment and motif properties are stable. For experimental validation, report the number of motifs overlapping experimentally verified segments, the fraction of experimental regions covered, and a statistical test (e.g., permutation or hypergeometric test) for enrichment of overlap.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "mutational tolerance landscapes landscape" contains a duplicated word.
- **Required correction** Remove the duplicate: "mutational tolerance landscapes."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Internal consistency
- **Affected element** Results, section "ESM2 Identifies Conserved, Disorderd Residues"
- **Evidence pointer** Section title
- **Issue** The section title contains a typo: "Disorderd" should be "Disordered."
- **Required correction** Correct the spelling in the section title.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, section "Regions Driving Phase Separation Are Enriched with Conserved, Disordered Residues"
- **Evidence pointer** Text describing Figure 4B
- **Issue** The classification of IDRs as "driving," "participating," or "non-participating" based on the 50% overlap threshold is described, but the number of IDRs in each category is only given in Figure S8, not in the main text.
- **Required correction** Report the number of IDRs in each category in the main text for clarity.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods, section "Evolutionary Sequence Analysis"
- **Evidence pointer** Methods text
- **Issue** The conservation score is defined as the ratio of occurrence of the reference residue across aligned sequences, but it is unclear whether gaps are treated as non-occurrences or excluded. The definition of "non-gap residues" in the denominator is given, but the numerator handling of gaps is not explicit.
- **Required correction** Clarify whether gaps in the reference sequence position are counted as non-matches in the numerator.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results, section "ESM2 Scores Correlate with Sequence Conservation"
- **Evidence pointer** Figure 3C
- **Issue** The text states that methionine was excluded from correlation analysis due to its frequent position as the initial residue, but it is unclear whether this exclusion applies to all analyses or only the per-amino-acid correlation.
- **Required correction** Specify the scope of the methionine exclusion across all analyses.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, section "Data Collection and Preprocessing"
- **Evidence pointer** Methods text
- **Issue** The threshold for selecting proteins with "at least 10% of their residues exhibiting a pLDDT score ≤ 70" is stated, but the rationale for this threshold is not provided.
- **Required correction** Provide a brief justification for the 10% threshold or cite prior work using a similar criterion.

## Risk / unsupported claims
- The claim of a "strong correlation" between ESM2 scores and conservation scores is unsupported without quantitative statistics.
- The enrichment of conserved residues in phase-separation-driving IDRs is asserted without reported statistical tests.
- The biological relevance of the identified motifs is inferred from overlap with previously published experimental data, but the overlap statistics are not provided.
- The ClinVar analysis (Figure S12) is mentioned only briefly in the Discussion; its methodology and results are not described in the main text, making the claim about pathogenic enrichment unevaluable.
- The statement that "many of these motifs have been experimentally validated as essential for phase separation" is not quantified; the number of motifs with experimental support and the nature of that support are not specified.
- The generalizability of the findings beyond human proteins is not assessed; the dMLO-IDR dataset includes multiple species, but cross-species comparisons are not reported.