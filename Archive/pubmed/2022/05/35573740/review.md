## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Structural characterization of the Int8 domain of herstatin using biophysical methods and computational prediction
- **Shared manuscript claim summary** The authors report that the intron-8-encoded 79-residue Int8 domain of herstatin is intrinsically disordered with residual helical structure, based on CD, NMR, SAXS, and structure prediction. They further report that the R371I mutant, defective in HER2 binding, is prone to aggregation.
- **Visible evidence base** Full text including Methods, Results (Figures 2-8), and Discussion. Supplementary figures referenced but not provided.
- **Missing materials affecting confidence** Supplementary Figures S1-S3; raw NMR, CD, and SAXS data; experimental details for SEC-MALS; AlphaFold2 prediction confidence metrics

## Reviewer
- **Overall assessment** The manuscript presents a straightforward biophysical characterization of a 79-residue domain from herstatin, concluding that it is intrinsically disordered with residual helical structure. The experimental approach is appropriate and the data largely support the main conclusion. However, several technical concerns regarding data interpretation, particularly the aggregation claim for the R371I mutant and the quantitative comparison of Rg values, need to be addressed. The novelty is modest, as intrinsic disorder in HER-family regulatory domains has been previously reported, but the intron-encoded origin of this IDR is an interesting angle.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins and their functional roles, particularly in receptor tyrosine kinase signaling. The work may also interest those investigating alternatively spliced variants and intron-encoded functional domains. The potential therapeutic angle (Int8 as an antitumor agent) could attract a broader cancer biology audience.
- **Major strengths** 1) Multi-technique approach (CD, NMR, SAXS) providing complementary evidence for disorder. 2) Inclusion of structure prediction methods (PSIPRED, AGADIR, AlphaFold2) that corroborate experimental findings. 3) The observation that an intron-encoded domain is intrinsically disordered is conceptually interesting. 4) The aggregation phenotype of the R371I mutant provides a potential functional rationale for loss of binding.
- **Major Concerns** 1) The claim that the R371I mutant is "prone to aggregation" is based on limited evidence and may reflect experimental conditions rather than intrinsic properties. 2) The comparison of Rg values to theoretical values for unfolded states relies on scaling laws that may not be directly applicable to a 79-residue peptide with residual structure. 3) The functional significance of the residual helical structure is speculative and not experimentally tested. 4) The statement that this is "the first report of an IDR encoded by an intron" is a strong claim that requires careful literature verification.
- **Minor Comments** 1) The N-terminal 5x Lys-tag and C-terminal 6x His-tag could influence the conformational properties of such a small domain; this should be discussed. 2) The Rg/Rh ratio interpretation could be strengthened by comparison to additional disordered protein standards. 3) The EOM analysis would benefit from reporting the ensemble distribution and selected conformer populations. 4) The manuscript would benefit from a more detailed description of the SEC-MALS experimental conditions and analysis.
- **Technical failings that need to be addressed before the case is established** R1-M1 (aggregation claim), R1-M2 (Rg comparison), R1-M3 (novelty claim)
- **Assessment against Nature-style criteria** Originality: Moderate. While the specific finding (Int8 is disordered) is new, intrinsic disorder in HER-family regulatory proteins has been previously described. The intron-encoded aspect is a novel angle. Scientific importance: Moderate. The work provides structural characterization of a functionally relevant domain but does not significantly advance mechanistic understanding of HER regulation. Interdisciplinary readership: Limited. The work is primarily of interest to structural biologists and protein chemists. Technical soundness: Generally sound, but with concerns about the aggregation claim and quantitative comparisons. Readability for nonspecialists: Acceptable, though some sections assume familiarity with biophysical methods.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data interpretation
- **Claim pointer** "the R371I mutant of Int8, which is defective in binding to HER2, is prone to aggregation"
- **Evidence pointer** Section 3.3, Figures 3C-D, 7
- **Concern** The conclusion that the R371I mutant is "prone to aggregation" is based on a single PFG NMR measurement at 150 uM showing a large Rh (72 A) and SEC data showing aggregates at high concentration (500 uM). However, the SEC data also show that at low concentration (100 uM), the mutant is largely monomeric. The concentration-dependent behavior could reflect a general property of partially folded or disordered proteins rather than a specific effect of the R371I mutation. Additionally, the wild-type was measured at 350 uM in NMR without apparent aggregation, but the mutant was only measured at 150 uM, making the comparison incomplete. The claim of "prone to aggregation" implies an intrinsic property, but the evidence suggests concentration-dependent behavior that may not be specific to the mutation.
- **Why it matters** The aggregation claim is presented as a "rationale for the loss of function" of the R371I mutant. If this is not robustly established, the functional interpretation is weakened. Moreover, the claim could mislead readers about the mechanism of loss of function.
- **Resolution test** Provide additional biophysical characterization of the R371I mutant, such as concentration-dependent SEC-MALS or dynamic light scattering over a range of concentrations, and compare directly to the wild-type under identical conditions. Alternatively, temper the claim to state that the mutant shows increased aggregation propensity under specific conditions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative analysis
- **Claim pointer** "The Rg of Int8 was almost the same as that of fully unfolded states"
- **Evidence pointer** Section 3.1, Figure 4F
- **Concern** The comparison of the experimentally determined Rg (29.9 A) to theoretical values for fully unfolded proteins relies on scaling laws (Rg = R0N^nu) that were derived for larger proteins. For a 79-residue peptide, finite-size effects and the presence of residual secondary structure (4% helix) may make such comparisons unreliable. The authors do not report the uncertainty in the Rg determination or the range of expected Rg values for disordered proteins of this size. Additionally, the Rg/Rh ratio of 0.91 is intermediate between the values for a compact sphere (0.78) and a random coil (1.2-1.6), which the authors interpret as "less flexible than random coils," but this interpretation is not quantitatively justified.
- **Why it matters** The central claim of the manuscript is that Int8 is intrinsically disordered. If the quantitative comparison to unfolded states is not robust, the strength of this conclusion is weakened, particularly given the evidence for residual structure.
- **Resolution test** Provide a more rigorous comparison, such as reporting the Rg relative to a panel of known disordered proteins of similar length, or using polymer theory with appropriate corrections for finite chain length. Report uncertainties in the Rg determination and discuss the limitations of the scaling law comparison.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Literature support
- **Claim pointer** "To our knowledge, this is the first report of an IDR encoded by an intron"
- **Evidence pointer** Section 4, Discussion
- **Concern** This is a strong novelty claim that requires thorough literature verification. Intron-encoded domains and peptides have been described in various contexts, and it is unclear whether any have been characterized as intrinsically disordered. The authors do not provide a systematic literature search or cite evidence that this claim has been verified. Given the broad interest in IDRs and alternative splicing, it is plausible that similar findings exist.
- **Why it matters** If this claim is inaccurate, it undermines the novelty of the work and the credibility of the authors' literature assessment.
- **Resolution test** Conduct a systematic literature search and either provide evidence supporting the claim or temper the statement to acknowledge prior related findings.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Experimental design
- **Affected element** Protein construct
- **Evidence pointer** Section 2.1
- **Issue** The Int8 construct includes an N-terminal 5x Lys-tag and a C-terminal 6x His-tag. For a 79-residue domain, these tags represent a substantial fraction of the total sequence and could influence conformational properties, including the propensity for residual structure or aggregation.
- **Required correction** Discuss the potential influence of the tags on the structural conclusions and, if possible, provide data on the untagged domain or justify the tag choice.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** EOM analysis
- **Evidence pointer** Section 3.1, Figure 5
- **Issue** The EOM analysis is described but the selected ensemble conformations are not shown in detail. The Rg and Dmax distributions are presented, but the specific conformations and their populations are not described.
- **Required correction** Provide a more detailed description of the EOM results, including the number of conformations in the ensemble, their populations, and representative structures.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data interpretation
- **Affected element** Helix content calculation
- **Evidence pointer** Section 2.2, Figure 2
- **Issue** The helix content is estimated from the MRE at 222 nm using a single equation. The accuracy of this estimate depends on the choice of reference values and may be affected by the presence of other secondary structure elements.
- **Required correction** Provide the reference values used for the calculation and discuss the limitations of the estimate.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1
- **Evidence pointer** Figure 1
- **Issue** Figure 1 is not described in the Results section, and its content is not fully explained in the text. It appears to show the domain architecture of herstatin, but the relationship between the schematic and the experimental work is not explicitly stated.
- **Required correction** Add a brief description of Figure 1 in the Results or Introduction and clarify its relevance to the study.

## Risk / unsupported claims
- The claim that Int8 is "the first report of an IDR encoded by an intron" is not supported by a systematic literature search and may be inaccurate.
- The claim that the R371I mutant is "prone to aggregation" as a rationale for loss of function is not fully supported by the data, as the aggregation appears concentration-dependent and was not directly compared to the wild-type under identical conditions.
- The statement that the residual helical structure "may serve as the putative HER-binding site" is speculative and not experimentally tested.
- The comparison of Rg to theoretical values for fully unfolded states is based on scaling laws that may not be reliable for a 79-residue peptide with residual structure.
- The functional significance of the intrinsic disorder of Int8 for its tumor-suppressive activity is not experimentally addressed and remains speculative.