## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, materials and methods, and figure legends (figures themselves not provided)
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and technical soundness based on the provided text. Figures, tables, and supplementary materials referenced but not directly assessable.
- **Shared manuscript claim summary** The authors identify two orphan kinesins, KIN-A and KIN-B, as bona fide components of the chromosomal passenger complex (CPC) in Trypanosoma brucei. They propose that KIN-A and KIN-B form a scaffold for CPC assembly, that the C-terminal tail of KIN-A recruits the CPC to kinetochores via the KKT7-KKT8 complex pathway, and that the N-terminal motor domain of KIN-A promotes chromosome alignment and CPC translocation to the central spindle in anaphase.
- **Visible evidence base** IP-MS interaction data, IP-CLMS crosslinking data, AlphaFold2 structural predictions, fluorescence microscopy localization studies, RNAi depletion experiments, domain deletion and point mutant rescue experiments, microtubule co-sedimentation assays, and bioinformatic sequence analyses.
- **Missing materials affecting confidence** Figures and supplementary tables (Tables S1, S2) not provided; quantification details for localization assays not fully described; statistical methods and replicate numbers not stated; raw mass spectrometry data not assessable; details of the LacO/LacI tethering experiments partially described.

## Reviewer
- **Overall assessment** This manuscript presents a compelling and well-integrated study identifying two orphan kinesins as novel components of the CPC in trypanosomes, with a proposed mechanism for CPC recruitment to kinetochores and translocation to the central spindle. The combination of biochemical, structural, and cell biological approaches is appropriate and generally rigorous. The finding that trypanosomes use a kinesin-based localization module instead of the histone-modification-based system found in other eukaryotes is evolutionarily significant. However, several technical concerns, particularly regarding the interpretation of the KIN-A rigor mutant phenotype, the incomplete rescue data, and the lack of direct evidence for the proposed "two-in-one" model, need to be addressed before the case is fully established.
- **Who would be interested in the results, and why** Cell biologists studying chromosome segregation, kinetochore biology, and the evolution of mitosis would be interested. Parasitologists working on Trypanosoma brucei and related kinetoplastids would also find this relevant, as the CPC components identified could represent potential drug targets. The evolutionary implications regarding the diversity of CPC localization mechanisms across eukaryotes would appeal to a broader evolutionary cell biology audience.
- **Major strengths** The study addresses a clear and important gap in understanding CPC assembly and localization in a divergent eukaryote. The combination of unbiased proteomics, structural prediction, and functional assays is powerful. The identification of a kinesin-based CPC localization module is novel and evolutionarily significant. The use of endogenous tagging and domain-specific mutants strengthens the functional conclusions. The authors are appropriately cautious in interpreting their data and acknowledge limitations.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (rigor mutant interpretation), R1-M2 (incomplete rescue data), R1-M3 (lack of direct binding evidence), R1-M4 (quantification and statistics).
- **Assessment against Nature-style criteria**  
  *Originality*: High. The identification of kinesins as CPC components in trypanosomes is novel and challenges the assumption that histone-modification-based recruitment is universal.  
  *Scientific importance*: High. The work provides insight into the diversity of CPC localization mechanisms and has potential implications for understanding chromosome segregation in divergent eukaryotes.  
  *Interdisciplinary readership*: Moderate to high. The topic is of interest to cell biologists, evolutionary biologists, and parasitologists, though the specialized nature of trypanosome biology may limit broader appeal.  
  *Technical soundness*: Generally good, but several concerns need to be resolved, particularly regarding the interpretation of the rigor mutant phenotype and the lack of direct binding data.  
  *Readability for nonspecialists*: The manuscript is well-written and accessible, with clear explanations of the significance of the findings. The figures, if consistent with the text, would aid comprehension.
- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are likely correct and significant, but the interpretation of the rigor mutant phenotype and the incomplete rescue data need to be addressed.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data interpretation
- **Claim pointer** "The ATPase activity of KIN-A promotes chromosome alignment in prometaphase and CPC translocation to the central spindle upon anaphase onset" and "CPC targeting to the central spindle in anaphase depends on KIN-A's ATPase activity"
- **Evidence pointer** Figure 6, Figures S6C-H
- **Concern** The interpretation that the G210A rigor mutation specifically affects CPC translocation to the central spindle is complicated by the observation that this mutant also causes chromosome misalignment in metaphase. The authors report that KIN-A G210A -YFP marked kinetochores were misaligned in ~50% of metaphase-arrested cells. This raises the possibility that the failure of CPC to translocate to the central spindle in anaphase is a secondary consequence of defective chromosome congression, rather than a direct effect of the rigor mutation on CPC transport. The authors do not adequately address this alternative interpretation.
- **Why it matters** The central claim that KIN-A's motor activity directly drives CPC translocation to the central spindle depends on distinguishing between a direct transport function and an indirect effect of chromosome misalignment. Without this distinction, the mechanistic model is not fully supported.
- **Resolution test** The authors should either (a) provide evidence that CPC translocation to the central spindle is impaired in the rigor mutant even in cells where chromosome congression is relatively normal, or (b) use a different approach, such as a conditional or inducible rigor mutant that can be activated after metaphase, to separate the two phenotypes. Alternatively, they could use a mutant that specifically affects processivity or directionality without affecting ATP binding, if such a mutant can be designed.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental completeness
- **Claim pointer** "We were unable to obtain a rescue cell line lacking both CD1 and CD2 as the double-mutant protein was not properly expressed" and the use of single-deletion mutants to infer the roles of CD1 and CD2
- **Evidence pointer** Figure 5, Figures S5C-G
- **Concern** The inability to generate a double-deletion mutant (ΔCD1ΔCD2) leaves a significant gap in the analysis. The authors show that ΔCD1 alone causes loss of kinetochore localization in metaphase but reappearance in anaphase, and ΔCD2 alone causes moderate reduction in metaphase and complete loss in anaphase. However, the synergistic or additive effects of deleting both domains cannot be assessed. Moreover, the authors do not provide a clear explanation for why the double mutant is not properly expressed, which could indicate protein misfolding or instability that confounds interpretation.
- **Why it matters** The proposed model that CD1 and CD2 act synergistically to promote kinetochore localization is inferred from single deletions. Without the double mutant, the model remains incomplete, and alternative explanations (e.g., that CD1 and CD2 have redundant functions) cannot be excluded.
- **Resolution test** The authors should attempt to generate the double mutant using alternative strategies (e.g., different tags, shorter deletions, or point mutations within CD1 and CD2 rather than full deletion). If the double mutant remains unattainable, they should provide additional evidence, such as in vitro binding assays showing that CD1 and CD2 bind to different partners, to support the synergistic model.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Evidence strength
- **Claim pointer** "The C-terminal unstructured tail of KIN-A serving as a key interaction partner for the KKT8 complex" and "KIN-A and KIN-B serve as the scaffold for the assembly of the remaining CPC subunits"
- **Evidence pointer** Figure 5, Figures S5A-B, Table S2
- **Concern** The evidence for the direct interaction between KIN-A CD1 and the KKT8 complex relies primarily on AlphaFold2 predictions and IP-MS co-enrichment. While the IP-CLMS data support the overall architecture of the CPC, the authors do not provide direct biochemical evidence (e.g., pull-down with purified components, isothermal titration calorimetry, or surface plasmon resonance) for the specific interaction between KIN-A CD1 and KKT9:KKT11. The AlphaFold2 prediction, while useful, is not a substitute for experimental validation.
- **Why it matters** The proposed model that KIN-A CD1 directly binds to KKT9:KKT11 is a key mechanistic claim. Without direct binding data, the model remains speculative, and alternative explanations (e.g., indirect interactions through other CPC components) cannot be excluded.
- **Resolution test** The authors should perform in vitro binding assays with purified recombinant KIN-A CD1 and KKT9:KKT11 to demonstrate direct interaction. Alternatively, they could use a proximity ligation assay or a two-hybrid system in vivo to support the interaction.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Quantification and statistics
- **Claim pointer** "KIN-A and KIN-B exhibited a CPC-like localization pattern similar to that of Aurora B AUK1" and "knockdown of KKT7 or KKT9 resulted in dispersal of YFP-Aurora B AUK1 from kinetochores in ~70% of cells"
- **Evidence pointer** Figures 1, 2, 4, Figures S1, S2, S4
- **Concern** The manuscript relies heavily on qualitative or semi-quantitative fluorescence microscopy data. The authors state percentages (e.g., ~70% of cells) but do not provide details on how these percentages were quantified, how many cells were counted, whether the counting was blinded, or what statistical tests were used. The number of biological replicates is not stated for most experiments.
- **Why it matters** The conclusions regarding the effects of RNAi depletion and domain deletions on CPC localization depend on reliable quantification. Without proper statistical analysis, the robustness of these conclusions cannot be assessed.
- **Resolution test** The authors should provide detailed quantification methods, including the number of cells counted, the number of independent experiments, and the statistical tests used. They should also consider providing a measure of inter-observer variability or automated image analysis to reduce bias.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that KIN-A constitutes a "unique 'two-in-one' CPC localization module" but this term is not defined or used consistently in the main text.
- **Required correction** Define the term "two-in-one" in the abstract or use more standard terminology such as "bifunctional localization module."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Experimental detail
- **Affected element** Materials and Methods, Fluorescence microscopy
- **Evidence pointer** Materials and Methods, Fluorescence microscopy
- **Issue** The microscopy methods state that "typically, ~20 optical slices spaced 0.2 or 0.24 μm apart were collected" but do not specify how the images were deconvolved or whether the shown images are maximum intensity projections or single slices.
- **Required correction** Specify the image processing steps and whether the images shown are projections or single slices.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 1F
- **Evidence pointer** Figure 1F
- **Issue** The bioinformatic analysis of KIN-A and KIN-B homologs across Euglenozoa is presented as a single panel, but the methods for this analysis are not described in the Materials and Methods section.
- **Required correction** Add a description of the bioinformatic methods used for the homolog search and phylogenetic analysis.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The discussion speculates that "kinesins may have served as the original transport vehicles for Aurora B kinases in early eukaryotes." This is an interesting idea but is not supported by direct evidence and could be seen as overreach.
- **Required correction** Soften this claim or provide additional evolutionary analysis to support it.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Results, "KIN-A and KIN-B are bona fide CPC proteins in trypanosomes"
- **Evidence pointer** Results, "KIN-A and KIN-B are bona fide CPC proteins in trypanosomes"
- **Issue** The authors state that KIN-A and KIN-B were "previously reported to localize to the spindle but not to kinetochores or the new FAZ tip" (Li et al., 2008), but they do not discuss why their results differ from this earlier report.
- **Required correction** Add a brief discussion of the possible reasons for the discrepancy (e.g., different tagging strategies, cell cycle staging, or antibody specificity).

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Materials and Methods, IP-MS
- **Evidence pointer** Materials and Methods, IP-MS
- **Issue** The mass spectrometry data are deposited in PRIDE (PXD045987), but the authors do not state whether the search parameters and databases used are fully described in the methods or available as supplementary files.
- **Required correction** Ensure that all search parameters and database versions are described in the methods or provided as supplementary files.

## Risk / unsupported claims
- The claim that KIN-A's ATPase activity directly drives CPC translocation to the central spindle is not fully supported due to the confounding effect of chromosome misalignment in the rigor mutant (R1-M1).
- The claim that KIN-A CD1 directly interacts with the KKT8 complex is based on AlphaFold2 predictions and co-immunoprecipitation, but lacks direct biochemical validation (R1-M3).
- The claim that KIN-A and KIN-B are "bona fide CPC proteins" is supported by co-immunoprecipitation and localization data, but the functional significance of their incorporation into the CPC is not fully explored.
- The evolutionary speculation that kinesins were the "original transport vehicles" for Aurora B kinases is not supported by direct evidence.
- The statement that "trypanosomes rely on kinetochore proteins to recruit the CPC onto kinetochores" is supported by the KKT7/KKT8 depletion data, but the authors do not exclude the possibility that other, unidentified pathways also contribute to CPC recruitment.