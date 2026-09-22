## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full text, figures, or supplementary materials
- **Shared manuscript claim summary** The authors report a synthetic system (micDROP) of multivalent IDRs that phase separate in vivo. They observe a wide range of saturation concentrations correlated with sequence stickiness, and report high promiscuity in IDR-IDR interactions among most tested IDRs, with TDP43 and UBQ2 forming spatially distinct condensates. They attribute TDP43 specificity to a short conserved α-helical segment and conclude that IDR sequence composition tunes phase separation propensity, but discrete condensate formation likely requires additional cellular or structural determinants.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or quantitative data provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, experimental methods, quantitative measurements (e.g., saturation concentrations, stickiness calculations), statistical analyses, and any control experiments

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting synthetic biology approach to a central question in the field of biomolecular condensates, namely whether IDR-IDR interactions alone can confer specificity. The finding of promiscuity among most IDRs, with exceptions, is notable. However, the abstract alone provides insufficient detail to evaluate the robustness of the experimental system, the quantitative basis for the claims, or the strength of the evidence linking the TDP43 α-helical segment to specificity. The conclusions are plausible but not fully established from the supplied material.
- **Who would be interested in the results, and why** Researchers studying phase separation, intrinsically disordered proteins, and biomolecular condensate biology would be interested. The work addresses a fundamental question about the determinants of condensate specificity, which has implications for understanding cellular organization and disease mechanisms involving aberrant phase separation. The synthetic micDROP system may also be of interest to those developing tools for probing IDR interactions.
- **Major strengths** The question addressed is timely and important. The use of a synthetic system to isolate IDR-IDR interactions from other cellular determinants is a conceptually clean approach. The inclusion of ten natural IDRs provides some breadth. The identification of a specific sequence element (the α-helical segment of TDP43) governing self-recognition is a potentially valuable mechanistic insight.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide sufficient methodological detail to assess whether the micDROP system faithfully reports on IDR-IDR interactions without confounding effects from the scaffold or the multivalent display. The quantitative correlation between saturation concentration and stickiness is stated but not shown. The evidence for the TDP43 α-helical segment governing specificity is not described. These gaps prevent full evaluation of the central claims.
- **Assessment against Nature-style criteria** 
  - Originality: The synthetic approach to dissecting IDR-IDR specificity is a creative contribution, though the general question of IDR promiscuity has been raised in prior literature. The originality is moderate to high, but the abstract alone does not fully demonstrate novelty beyond existing work on IDR phase separation.
  - Scientific importance: The question of how condensate specificity arises is of broad importance in cell biology and biophysics. If the claims hold, the work would contribute meaningfully to understanding the determinants of condensate identity. However, the abstract does not yet establish the full significance.
  - Interdisciplinary readership: The topic bridges cell biology, biophysics, and protein biochemistry. The abstract is written in a way that is largely accessible to these communities, though some jargon (e.g., "stickiness") would benefit from clearer definition.
  - Technical soundness: Cannot be fully assessed from the abstract. The correlation between saturation concentration and stickiness is mentioned but not quantified. The promiscuity claim rests on co-expression experiments that are not described in sufficient detail. The TDP43 α-helix finding is stated without supporting evidence.
  - Readability for nonspecialists: The abstract is reasonably clear, but terms like "multivalent IDRs," "micDROP," and "sequence stickiness" are introduced without full explanation. A nonspecialist would struggle to understand the experimental logic without additional context.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents an interesting hypothesis and preliminary findings, but the evidence base is too limited to support the central claims. A full manuscript with detailed methods, quantitative data, and controls would be required to assess whether the case is made.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "IDRs exhibited a wide range of saturation concentrations in vivo, which correlated well with their total sequence stickiness."
- **Evidence pointer** Abstract text; location not provided
- **Concern** The abstract states a correlation between saturation concentrations and sequence stickiness but provides no quantitative data, no definition of "stickiness," and no description of how either parameter was measured. Without these details, the strength and significance of the correlation cannot be evaluated.
- **Why it matters** This correlation is a central piece of evidence supporting the claim that IDR sequence composition tunes phase separation propensity. If the correlation is weak or based on a biased metric, the conclusion would be undermined.
- **Resolution test** Provide the full dataset of saturation concentrations and stickiness values for all ten IDRs, the correlation coefficient and statistical significance, and a clear definition of the stickiness metric used.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "we observed a high degree of promiscuity, particularly among IDRs from the proteins Ddx4, DYRK3, ERα, FUS, hnRNPA1, HspB8, RBM14 and TAF15, whereas TDP43 and UBQ2 formed spatially distinct condensates regardless of their partner."
- **Evidence pointer** Abstract text; location not provided
- **Concern** The experimental basis for this claim is not described. The abstract mentions co-expression of IDR pairs fused to homologous scaffolds that "did not co-assemble," but the reader cannot assess how promiscuity was scored, how many pairwise combinations were tested, whether all pairs were tested in both orientations, or how spatial distinctness was determined. The distinction between "promiscuous" and "specific" behavior is central to the paper's thesis, yet the criteria are undefined.
- **Why it matters** The promiscuity versus specificity distinction is the core finding of the abstract. If the assay cannot reliably distinguish between co-assembly and independent phase separation, the conclusion would be unsupported.
- **Resolution test** Provide a detailed description of the co-expression assay, including the scaffold design, the number of pairwise combinations tested, the imaging and quantification methods used to score co-assembly, and appropriate controls demonstrating that the scaffolds do not co-assemble on their own.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "the short and conserved α-helical segment of TDP43's IDR was governing its specific self-recognition."
- **Evidence pointer** Abstract text; location not provided
- **Concern** No experimental evidence is presented to support this mechanistic claim. The abstract does not describe how the α-helical segment was identified, whether mutations or deletions were tested, or how the effect on specificity was measured. The claim is stated as a conclusion without visible support.
- **Why it matters** This is the only positive mechanistic finding in the abstract and is presented as a key insight. Without evidence, it remains an unsupported assertion.
- **Resolution test** Provide the experimental data identifying the α-helical segment, including sequence alignments, mutagenesis studies, and functional assays demonstrating that disruption of this segment abolishes TDP43 self-recognition.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Definition of "stickiness"
- **Evidence pointer** Abstract text; location not provided
- **Issue** The term "sequence stickiness" is used without definition. It is unclear whether this refers to a published metric, a new calculation, or a qualitative assessment.
- **Required correction** Define "stickiness" explicitly, including the algorithm or parameters used to compute it, and cite any relevant prior work.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Description of the micDROP system
- **Evidence pointer** Abstract text; location not provided
- **Issue** The micDROP system is introduced as "Multivalent IDRs forming Constitutive DROPlets," but the abstract does not explain how the system works, what the scaffold is, or how multivalency is achieved. This limits the reader's ability to interpret the results.
- **Required correction** Provide a brief description of the micDROP design in the abstract, including the nature of the scaffold and the valency of the IDR display.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Generalization of findings
- **Evidence pointer** Abstract text; location not provided
- **Concern** The abstract concludes that "IDRs can tune their phase separation propensity through sequence composition, while their formation of discrete condensates likely requires additional cellular or structural determinants." This is a broad generalization based on ten IDRs in a synthetic system. The abstract does not acknowledge potential limitations of the synthetic context.
- **Required correction** Add a sentence acknowledging that the synthetic system may not fully recapitulate the cellular environment and that conclusions about "additional determinants" are inferred rather than directly tested.

## Risk / unsupported claims
- The correlation between saturation concentration and sequence stickiness is stated but not supported by any visible data.
- The claim of high promiscuity among most IDRs is not supported by a description of the assay or quantitative results.
- The claim that TDP43's α-helical segment governs self-recognition is unsupported by any visible experimental evidence.
- The conclusion that discrete condensate formation requires "additional cellular or structural determinants" is an inference not directly tested in the abstract.
- The generalizability of the findings beyond the ten tested IDRs and the synthetic micDROP system is not established.