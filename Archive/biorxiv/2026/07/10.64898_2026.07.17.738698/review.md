## Review setup
- **Input scope** Full manuscript text (main text, methods, figure legends not separately provided)
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and internal consistency based solely on the provided text
- **Shared manuscript claim summary** The authors propose that Drosophila ORC binds HP1a through two SLiMs (R1 and R2) in the Orc1 IDR, which pair with the HP1a HGM and CTE motifs, and that this interaction is required for heterochromatin functions including PEV silencing, rDNA repression, and nucleolar organization.
- **Visible evidence base** Biochemical pull-down assays with recombinant fragments; CRISPR-generated fly strains with R1/R2 mutations or deletion; immunofluorescence and immuno-FISH for nucleolar and rDNA analyses; RT-qPCR for pre-rRNA levels; statistical methods described
- **Missing materials affecting confidence** Figures and supplementary figures not viewable; no raw data, quantification plots, or statistical outputs; no experimental replicates or controls described in sufficient detail; no structural data for the proposed binding model; no chromatin immunoprecipitation or localization data for Orc1 at rDNA

## Reviewer
- **Overall assessment** This manuscript addresses an important question about the non-replicative functions of ORC, specifically its interaction with HP1a and the role of this interaction in heterochromatin structure and function. The identification of specific SLiMs in the Orc1 IDR and corresponding motifs in HP1a is a valuable contribution. However, the evidence as presented has significant gaps. The biochemical data are qualitative and lack equilibrium binding measurements. The in vivo phenotypes are compelling but the mechanistic link between the disrupted interaction and the observed phenotypes is not fully established. The proposed trans-binding model is speculative and not directly tested. The manuscript would benefit from additional quantitative binding data, chromatin-level analyses, and a more direct test of the proposed mechanism.
- **Who would be interested in the results, and why** Researchers studying ORC multifunctionality, heterochromatin biology, HP1 interactions, genome organization, and the role of intrinsically disordered regions in protein-protein interactions. The work also has relevance for understanding how chromatin-associated complexes can have separable functions in replication and gene silencing.
- **Major strengths** The use of CRISPR-generated endogenous mutations to test the in vivo relevance of biochemically defined interactions is rigorous. The identification of a non-canonical, PxVxL-independent binding mechanism is novel. The phenotypic analyses (PEV, rDNA, nucleolus) are well chosen and directly relevant to heterochromatin function. The evolutionary conservation analysis adds confidence to the functional importance of the identified motifs.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that R1 and R2 in the Orc1 IDR are required for HP1a binding based on pull-down assays with deletion and point mutants.
  - **Evidence pointer** Results section "Two separated SLiMs in Orc1 IDR mediate HP1a binding"; Figures 1B, 1C, 2A, 2B; Supplementary Figures 1-3
  - **Concern** The pull-down assays are semi-quantitative at best. The authors acknowledge that mass photometry could not measure a binding constant, but no alternative quantitative binding assay (e.g., ITC, SPR, fluorescence anisotropy) is provided. The classification of binding effects as 'major', 'modest', or 'little to no effect' is subjective and not supported by statistical analysis. Without equilibrium binding constants or at least dose-response curves, the claim that R1 and R2 are "required" for binding is not rigorously established.
  - **Why it matters** The entire manuscript hinges on the specificity and affinity of the Orc1-HP1a interaction. If the binding is not quantitatively characterized, the interpretation of the in vivo phenotypes as being due to loss of this specific interaction is weakened.
  - **Resolution test** Provide quantitative binding data (e.g., Kd values) for WT and mutant Orc1 fragments against HP1a, using a solution-based method. Show that the R1/R2 mutations reduce binding affinity by a defined and significant amount.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that disrupting Orc1-HP1a binding causes increased rDNA transcription, rDNA redistribution, and nucleolar enlargement, and that this is due to loss of Orc1-HP1a interaction specifically.
  - **Evidence pointer** Results section "Reduced Orc1–HP1a interaction suppresses heterochromatin-mediated gene silencing (PEV)" and "Decreased Orc1–HP1a interaction leads to increased nucleolar volume and rRNA transcription"; Figures 5, 6; Supplementary Figure 9
  - **Concern** The manuscript does not provide direct evidence that the observed phenotypes are due to loss of Orc1-HP1a binding at specific loci. No chromatin immunoprecipitation (ChIP) data are shown to demonstrate that Orc1 is normally localized at rDNA or other heterochromatic loci in an HP1a-dependent manner. The possibility that the R1/R2 mutations affect other Orc1 functions (e.g., replication, chromatin binding) is not excluded. The claim that H3K9me2 levels are unchanged is based on immunofluorescence, which may not be sensitive enough to detect local changes at rDNA.
  - **Why it matters** Without locus-specific evidence, the causal link between the biochemical interaction and the observed phenotypes remains correlative. The manuscript's central conclusion that Orc1-HP1a binding is "required for heterochromatin structure and function" is not fully supported.
  - **Resolution test** Perform ChIP-qPCR or ChIP-seq for Orc1 and HP1a in WT and mutant embryos at rDNA and other heterochromatic loci. Show that Orc1 occupancy is reduced at these loci in the R1/R2 mutants, and that this correlates with changes in chromatin state or transcription.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The authors propose a trans-binding model where Orc1 R1 and R2 engage HGM and CTE motifs on different HP1a monomers within a dimer.
  - **Evidence pointer** Discussion section "Why do Orc1–HP1a interactions require HP1 dimerization?"; Figure 7; Supplementary Figure 10
  - **Concern** The trans-binding model is speculative. The distance estimates are based on a human HP1α structure and an AlphaFold prediction of Orc1, neither of which is experimentally validated for the Drosophila complex. The model is not tested with any experiment (e.g., crosslinking, structural analysis, or binding assays with monomeric vs. dimeric HP1a variants).
  - **Why it matters** While the model is interesting, it is presented with more confidence than the data warrant. Overinterpretation of speculative models can mislead the field.
  - **Resolution test** Provide experimental evidence for the trans-binding configuration, such as crosslinking mass spectrometry, or a binding assay using HP1a monomers that cannot dimerize but retain the HGM and CTE motifs.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Introduction
  - **Evidence pointer** Introduction, first paragraph
  - **Issue** The introduction assumes significant background knowledge about ORC, HP1, and heterochromatin. A brief explanation of why ORC's non-replicative functions are surprising or important would help a broader audience.
  - **Required correction** Add one or two sentences explaining the significance of ORC's multifunctionality in the context of genome regulation.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Methods, pull-down assays
  - **Evidence pointer** Methods section "Expression and purification of recombinant proteins"
  - **Issue** The pull-down assay description lacks details on washing stringency, buffer conditions, and how binding was quantified. The statement that "attempts to use the mass photometry method were not successful" is vague.
  - **Required correction** Provide more detail on the pull-down protocol, including wash steps, salt concentration, and detergent. Specify why mass photometry was unsuccessful (e.g., aggregation, low signal).
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Statistical analysis
  - **Evidence pointer** Methods section "Statistical Analysis"
  - **Issue** The use of one-sided p-values is unusual and not justified. For two-group comparisons, two-sided tests are standard unless there is a strong a priori directional hypothesis.
  - **Required correction** Justify the use of one-sided tests or switch to two-sided tests.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Discussion
  - **Evidence pointer** Discussion, final paragraph
  - **Issue** The discussion of condensates and phase separation is brief and may be unclear to readers not familiar with this field.
  - **Required correction** Briefly explain what phase separation is and why it is relevant to heterochromatin function.

## Technical failings that need to be addressed before the case is established
- R1-M1: Lack of quantitative binding data for Orc1-HP1a interaction
- R1-M2: No locus-specific evidence (e.g., ChIP) linking Orc1-HP1a binding to phenotypes at rDNA or heterochromatin

## Risk / unsupported claims
- The claim that Orc1-HP1a binding is "required for heterochromatin structure and function" is not fully supported without locus-specific chromatin analyses.
- The trans-binding model (Figure 7) is speculative and not experimentally tested.
- The statement that "bulky side-chain residues" in R1 and R2 are critical is based on qualitative pull-down data without statistical support.
- The claim that H3K9me2 levels are "largely unchanged" in mutants is based on immunofluorescence, which may not detect local changes; this is acknowledged but not addressed with more sensitive methods.
- The evolutionary conservation argument is suggestive but does not directly demonstrate functional importance in vivo.

## Assessment against Nature-style criteria
- **Originality** The identification of a non-canonical, PxVxL-independent binding mechanism between Orc1 and HP1a is novel and of interest. The finding that ORC has a specific role in heterochromatin function beyond replication is conceptually important.
- **Scientific importance** The work addresses a fundamental question about how a replication initiator can have separable functions in chromatin regulation. The results have implications for understanding genome organization and gene silencing. However, the importance is somewhat limited by the lack of mechanistic depth at the chromatin level.
- **Interdisciplinary readership** The topic is relevant to researchers in DNA replication, chromatin biology, epigenetics, and gene regulation. The use of Drosophila genetics and biochemistry makes it accessible to a broad audience in these fields.
- **Technical soundness** The genetic approach is sound, but the biochemical characterization is incomplete. The lack of quantitative binding data and locus-specific chromatin analyses are significant weaknesses.
- **Readability for nonspecialists** The manuscript is generally well-written but assumes significant background knowledge. The introduction and discussion could be improved to make the significance clearer to a broader audience.

## Recommendation posture
Supportive if technical concerns are resolved. The manuscript addresses an important question and the genetic data are compelling. However, the lack of quantitative binding data and locus-specific chromatin analyses prevents the central claims from being fully established. If the authors can provide quantitative binding measurements and ChIP-level evidence for Orc1 localization at heterochromatic loci, the manuscript would be suitable for a high-impact journal.