## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and supplementary figure/table references
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided manuscript text. No external data or unpublished materials were consulted.
- **Shared manuscript claim summary** The authors investigate the functional conservation and divergence of the orphan gene goddard (gdrd) across Drosophila species. Using cross-species gene swap assays in D. melanogaster, they show that a highly divergent ortholog from D. mojavensis fully rescues fertility in gdrd null mutants, while other orthologs, including more closely related ones, fail to complement. They further demonstrate that all orthologs retain some ability to localize to axonemes and ring centrioles, but noncomplementing orthologs show weaker axonemal binding and divergent subcellular localization patterns. Computational analyses, including SHARK-based motif detection and molecular dynamics simulations, suggest that physicochemical properties of intrinsically disordered regions and overall structural stability correlate with functional capacity.
- **Visible evidence base** Results sections on sequence divergence, gene swap fertility assays, localization studies, IDR physicochemical analyses, and MD simulations; figures referenced as Fig. 1-8 and supplementary figures S1-S15; methods sections for fly husbandry, sequence analysis, transgenic construction, western blotting, microscopy, and MD simulations
- **Missing materials affecting confidence** Actual figures and supplementary data files were not provided; exact numerical values for fertility counts, statistical test outputs, and MD simulation metrics are referenced but not shown; supplementary text on Unc/Gdrd localization patterns is mentioned but not included; western blot images and confocal micrographs are not viewable

## Reviewer
- **Overall assessment** This manuscript addresses a fundamental question in evolutionary biology: whether orphan genes, which evolve rapidly, retain conserved functions or undergo functional divergence. The study is well-designed, combining functional assays with computational predictions to dissect the evolutionary trajectory of the goddard gene. The finding that a highly divergent ortholog from D. mojavensis can fully rescue fertility in D. melanogaster, while more closely related orthologs cannot, is striking and counterintuitive, challenging simple models of sequence-function relationships. The work is technically sound in its use of standardized transgenic integration, codon optimization, and multiple independent assays. However, several concerns limit the strength of the conclusions, particularly regarding the interpretation of negative results in complementation assays, the correlative nature of the computational analyses, and the lack of direct mechanistic evidence linking specific sequence features to functional outcomes. The manuscript would benefit from additional experiments or more cautious interpretation in several areas.
- **Who would be interested in the results, and why** Evolutionary biologists studying de novo gene emergence and orphan gene function will find this work directly relevant. Researchers interested in the relationship between protein sequence divergence and functional conservation, particularly in the context of intrinsically disordered proteins, will also be interested. The Drosophila community, especially those studying spermatogenesis and male fertility, will value the functional characterization of gdrd orthologs. The methodological approach combining gene swaps, computational motif analysis, and MD simulations may serve as a template for similar studies in other systems.
- **Major strengths** The study addresses a timely and important question in evolutionary genomics. The experimental design is thoughtful, using standardized genomic integration to control for position effects and codon optimization to ensure comparable expression. The inclusion of multiple orthologs spanning different divergence times and phylogenetic distances strengthens the comparative framework. The combination of functional fertility assays with subcellular localization studies provides complementary evidence. The use of alignment-free, physicochemical-based motif detection (SHARK tools) is innovative and appropriate for analyzing rapidly evolving disordered regions. The MD simulations add a structural dynamics perspective that is often missing in evolutionary studies.
- **Major Concerns**
- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental design and interpretation of negative results
- **Claim pointer** The authors claim that noncomplementing orthologs "cannot substitute for the melanogaster gene" and interpret this as evidence of functional divergence or loss.
- **Evidence pointer** Results section "A gdrd ortholog from the Drosophila subgenus is functional in D. melanogaster, while other orthologs of lesser or equal divergence are not"; Figure 4a
- **Concern** The interpretation of failed complementation as functional divergence is complicated by the observation that two orthologs (D. ananassae and D. grimshawi) show reduced protein expression on western blots. The authors acknowledge this but do not adequately address whether the failure to rescue could be due to insufficient protein levels rather than intrinsic functional differences. The D. yakuba ortholog, which partially rescues, shows robust expression, while the D. ananassae ortholog, which fails to rescue, shows weak expression. This confound is particularly problematic for the D. ananassae ortholog, which is more closely related to D. melanogaster than D. mojavensis yet fails to complement. The authors suggest that MD simulation instability may explain reduced expression, but this is speculative. Without experiments that equalize protein levels (e.g., using stronger drivers, different integration sites, or protein stabilization strategies), the conclusion that sequence divergence has "diminished functional capabilities" is not fully supported.
- **Why it matters** The central claim of the paper, that functional capacity varies among orthologs in a way that does not correlate with phylogenetic distance, depends critically on the interpretation of negative results in complementation assays. If the failures are due to expression level differences rather than functional divergence, the evolutionary conclusions would be substantially weakened.
- **Resolution test** Provide quantitative protein expression data (e.g., western blot band intensities normalized to loading controls) for all orthologs. If possible, generate multiple independent transgenic lines for each ortholog and test whether expression levels correlate with rescue capacity. Alternatively, use a heterologous expression system (e.g., cultured cells) to assess protein stability independent of Drosophila testis context.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Statistical analysis and data presentation
- **Claim pointer** The authors report significant differences in fertility rescue and IDR physicochemical properties, but the statistical methods and effect sizes are not fully described in the visible text.
- **Evidence pointer** Results sections on fertility assays and IDR analyses; Figure 4a, Figure 6, Figure 7c
- **Concern** The manuscript reports p-values for fertility comparisons (e.g., P < 0.0001) but does not describe the statistical model used (e.g., whether data were transformed, whether nonparametric tests were considered, how multiple comparisons were handled). For the MD simulation analyses, the methods state that Kruskal-Wallis H tests and Dunn's post hoc tests were used, but the results section does not report the test statistics or effect sizes. The claim that D. mojavensis is "the most stable" ortholog is based on visual inspection of RMSD and Rg plots, but no quantitative comparison across orthologs is provided. Similarly, the SHARK-Dive score for the D. mojavensis C-terminus is described as a "high outlier," but the distribution of scores across all orthologs is not shown.
- **Why it matters** The conclusions about which orthologs are functionally competent and which physicochemical features correlate with function depend on robust statistical comparisons. Without clear reporting of statistical methods and effect sizes, readers cannot assess the strength of the evidence.
- **Resolution test** Provide detailed statistical methods for all comparisons, including the specific tests used, whether assumptions were checked, and how multiple testing was addressed. For MD simulations, report mean and confidence intervals for RMSD, RMSF, and Rg for each ortholog, and perform formal statistical comparisons across orthologs. For SHARK-Dive scores, show the full distribution of scores and indicate how the D. mojavensis value compares to the distribution.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic link between computational predictions and functional outcomes
- **Claim pointer** The authors propose that "lineage-specific changes in the termini contribute to functional divergence" and that "intrinsic protein qualities" such as structural stability and physicochemical properties of IDRs explain differences in rescue capacity.
- **Evidence pointer** Results sections on IDR analyses and MD simulations; Discussion section "Extant Gdrd orthologs may have distinct, lineage-specific features"
- **Concern** The computational analyses identify correlations between predicted structural stability, IDR physicochemical properties, and functional outcomes, but no direct experimental test of these predictions is provided. The authors suggest that domain-swap experiments could test these predictions but do not perform them. The claim that the D. mojavensis ortholog's ability to rescue is due to its IDR properties resembling those of D. melanogaster is correlative. Alternative explanations, such as differences in the central helix sequence (which the authors note is the most conserved region), are not fully explored. The MD simulations are performed on isolated proteins in solution, which may not reflect the in vivo context where gdrd interacts with other proteins at the axoneme and ring centriole.
- **Why it matters** The paper's contribution to understanding how orphan gene function evolves would be strengthened by direct experimental evidence linking specific sequence features to functional outcomes. Without such evidence, the mechanistic claims remain speculative.
- **Resolution test** Perform domain-swap experiments between rescuing and nonrescuing orthologs (e.g., swapping N- and C-terminal IDRs between D. mojavensis and D. virilis) to test whether IDR properties determine rescue capacity. Alternatively, use site-directed mutagenesis to alter specific residues or motifs identified by SHARK analysis and test the effects on function.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of conclusions
- **Claim pointer** The authors conclude that "the ancestral gdrd gene likely already performed the core functions found in extant D. melanogaster" and that "functional conservation can be equally long-standing" as structural conservation.
- **Evidence pointer** Discussion section "Ancestral Gdrd at the base of the genus was most likely functional"
- **Concern** The conclusion that the ancestral gdrd was functional is based on the observation that a D. mojavensis ortholog can rescue D. melanogaster mutants. However, this inference assumes that the D. mojavensis ortholog's function in D. melanogaster reflects its ancestral function. It is possible that the D. mojavensis ortholog has evolved new functions or promiscuous interactions that allow it to substitute for the D. melanogaster protein, rather than retaining the ancestral function. The authors acknowledge this possibility but do not address it experimentally. Additionally, the study only tests a limited number of orthologs (seven total), and the conclusions about the ancestral state are based on a single successful cross-genus complementation.
- **Why it matters** The evolutionary narrative presented in the paper depends on the inference that the ancestral gdrd was functional and that functional conservation has been maintained over deep timescales. If the D. mojavensis ortholog's ability to rescue is due to convergent evolution or promiscuous interactions, the conclusions about ancestral function would be less secure.
- **Resolution test** Test additional orthologs from more divergent species or from intermediate phylogenetic positions to determine whether the pattern of rescue capacity is consistent with ancestral function. Alternatively, use ancestral sequence reconstruction to infer the ancestral gdrd sequence and test its function directly.

- **Minor Comments**
- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure references
- **Affected element** Results section on IDR analyses
- **Evidence pointer** Figure 6a, Figure S14
- **Issue** The text states that "the D. mojavensis N terminus shares a motif with Sophophora subgenus orthologs" and lists specific motif sequences, but it is unclear whether these motifs are shown in the figure or only described in text. The figure legend is not visible in the provided material.
- **Required correction** Clarify in the text which motifs are depicted in Figure 6a and ensure that the motif sequences are clearly labeled in the figure.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reporting of sample sizes
- **Affected element** Fertility assay results
- **Evidence pointer** Figure 4a, Methods section "Fertility assay"
- **Issue** The methods state that final sample sizes were n = 25 to 30 males per genotype, but the results do not specify the exact n for each genotype or whether all genotypes had similar sample sizes. The fertility data appear to be presented as means with error bars, but the type of error bar (SD, SEM, CI) is not stated.
- **Required correction** Report exact sample sizes for each genotype in the results or figure legend, and specify the type of error bars used.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Throughout the manuscript
- **Evidence pointer** Abstract, Introduction, Results
- **Issue** The terms "function" and "functional capacity" are used somewhat loosely. The authors equate rescue of fertility with "function" but also discuss "functional divergence" and "functional conservation" without clearly defining what aspects of function they are referring to (e.g., biochemical activity, protein-protein interactions, subcellular localization).
- **Required correction** Define what is meant by "function" in the context of this study, and consider using more specific terms such as "fertility rescue capacity" or "axoneme-binding ability" where appropriate.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of alternative explanations
- **Affected element** Discussion section "Extant Gdrd orthologs may have distinct, lineage-specific features"
- **Evidence pointer** Discussion, paragraph 2
- **Issue** The authors discuss the possibility that noncomplementing orthologs may have evolved lineage-specific functions but do not consider the possibility that the failure to rescue could be due to improper folding or post-translational processing in the D. melanogaster testis environment, independent of the protein's intrinsic properties.
- **Required correction** Add a brief discussion of this alternative explanation and how it might be distinguished from intrinsic functional differences.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Supplementary material accessibility
- **Affected element** Supplementary figures and tables
- **Evidence pointer** Multiple references to Figure S1-S15, File S1
- **Issue** The manuscript references numerous supplementary figures and tables, but the content of these files is not described in the text. For example, Figure S1 is described as showing "lineage-specific alterations in length" but the specific species and sequence features are not summarized.
- **Required correction** Provide brief descriptions of each supplementary figure/table in the text or in a supplementary figure legend list, so readers can understand what information is contained in each file.

## Risk / unsupported claims
- The claim that "the ancestral gdrd gene likely already performed the core functions found in extant D. melanogaster" is an inference based on a single successful cross-genus complementation and is not directly supported by experimental evidence.
- The claim that "lineage-specific changes in the termini contribute to functional divergence" is correlative and not directly tested.
- The claim that "intrinsic protein qualities" such as structural stability explain differences in rescue capacity is supported only by computational predictions and indirect experimental observations (e.g., western blot band intensities).
- The statement that "all tested orthologs maintain localization to the transition zones" is based on qualitative immunofluorescence observations; no quantitative analysis of localization intensity or frequency is provided.
- The claim that the D. ananassae ortholog "may have evolved new interaction preferences" is speculative and not supported by direct experimental evidence.
- The interpretation of the D. yakuba partial rescue phenotype is not fully explored; the authors do not discuss whether the reduced fertility is due to partial function or to a different functional defect.