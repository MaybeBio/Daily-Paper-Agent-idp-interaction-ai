## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, methods, and figure legends
- **Assessment boundary** Scientific content, technical soundness, structural biology methodology, functional validation, and claims as presented in the provided manuscript
- **Shared manuscript claim summary** The authors present cryo-EM structures of human APC/CCDH1:EMI1 at 2.9 Å and apo-APC/C at 3.2 Å resolution, improving on their previous 3.6 Å structures. They report four main findings: (1) assignment of an N-terminal α-helix of CDH1 (CDH1α1) that interacts with APC1WD40; (2) identification of a zinc-binding module in APC2 (APC2ZBM) coordinated by four cysteine residues; (3) building of several intrinsically disordered regions aided by AlphaFold predictions; and (4) a reinterpretation of the APC1 auto-inhibitory segment (APC1AI) mechanism, supported by mutagenesis and activity assays.
- **Visible evidence base** Cryo-EM density maps, model building details, PIXE spectroscopy data, ubiquitination and SUMOylation assays, multiple sequence alignments, AlphaFold predictions, and supplementary figures and tables as referenced
- **Missing materials affecting confidence** Supplementary figures and tables referenced throughout (Supplementary Figs 1-8, Supplementary Tables 1-3, Supplementary Movie 1) were not provided. Full experimental details for some assays are abbreviated. The APC/CCDC20:CyclinA2 map reinterpretation relies on previously published data (PDB 6Q6H, EMD-4466) not re-analyzed here. Statistical details for activity assays are limited.

## Reviewer
- **Overall assessment** This manuscript presents technically impressive cryo-EM structures at improved resolution that provide incremental but meaningful advances in understanding APC/C regulation. The identification of the CDH1 N-terminal α-helix, the APC2 zinc-binding module, and the EMI1 KEN box interaction with CDH1 are valuable contributions. However, several claims require additional experimental support or clearer presentation. The functional significance of the APC2ZBM remains unclear given the negative results presented. The APC1AI phosphorylation mechanism, while plausible, is supported by indirect evidence. The manuscript would benefit from more rigorous quantitative analysis of the activity assays and clearer discussion of the limitations of the structural interpretations.
- **Who would be interested in the results, and why** Cell cycle biologists, structural biologists studying large multi-subunit complexes, and researchers interested in ubiquitin ligase regulation. The improved structures provide a more complete framework for understanding APC/C assembly and regulation, which is central to cell division control. The methodological approaches for combining cryo-EM with AlphaFold predictions will also interest the structural biology community.
- **Major strengths** (1) Improved resolution over previous structures enabling unambiguous assignment of previously ambiguous regions. (2) Identification of a conserved zinc-binding module in APC2 with experimental confirmation of zinc content via PIXE. (3) Discovery of the EMI1 KEN box interaction with CDH1, providing a new mechanism for EMI1-mediated inhibition. (4) The APC1AI structural model provides a clear mechanistic explanation for phosphorylation-dependent regulation. (5) Rigorous use of multiple approaches including cryo-EM, AlphaFold, mutagenesis, and biochemical assays.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (functional significance of APC2ZBM), R1-M2 (quantitative rigor of activity assays), R1-M3 (APC1AI mechanism evidence strength)
- **Assessment against Nature-style criteria** **Originality**: Moderate. The structures are improved over previous work but represent incremental advances rather than paradigm-shifting discoveries. The EMI1 KEN box finding is the most novel aspect. **Scientific importance**: High for the cell cycle field. APC/C is a master regulator, and improved structural understanding has broad implications. **Interdisciplinary readership**: Moderate. Primarily of interest to structural biologists and cell cycle researchers. The methodological aspects may attract a broader structural biology audience. **Technical soundness**: Generally strong. Cryo-EM data collection and processing appear rigorous. The PIXE experiments are well designed. However, some functional assays lack quantitative rigor. **Readability for nonspecialists**: Adequate but could be improved. The introduction provides good context, but the results section assumes significant background knowledge of APC/C architecture and terminology.
- **Recommendation posture** Supportive if technical concerns are resolved. The structural work is solid and the EMI1 KEN box finding is novel, but the functional significance of several findings needs strengthening and the quantitative analysis of activity assays needs improvement.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** No
- **Axis** Functional significance
- **Claim pointer** The authors state that the APC2ZBM "confers structural stability to the complex" and that its identification is an "important insight," but the functional data show no effect on ubiquitination or SUMOylation activity when the zinc-binding cysteines are mutated.
- **Evidence pointer** Figure 3, Supplementary Figure 4, Table 1
- **Concern** The authors identify a zinc-binding module in APC2 and confirm zinc content via PIXE, but the functional characterization is entirely negative. Mutation of the four coordinating cysteines (APC/CAPC2ΔZBM) showed no impairment in ubiquitination activity or SUMOylation. The claim that this module "confers structural stability" is not directly tested. The authors suggest it "likely does not directly mediate SUMO and APC2WHB binding" and that "whether the ZBM in APC2 plays a role in APC/C activity under physiological conditions will require future studies." This is an honest assessment, but it raises the question of why this finding is presented as a major result. The structural observation is interesting, but without any demonstrated functional role, its significance is unclear. The authors should either provide evidence for a functional role (e.g., stability assays, cellular phenotypes) or present this as a more modest structural observation.
- **Why it matters** The manuscript presents the APC2ZBM as a key finding, but the lack of functional evidence weakens the claim that it is biologically important. For a structures paper, structural observations can stand alone, but the framing here suggests functional relevance that is not demonstrated.
- **Resolution test** Provide direct evidence for a functional role of APC2ZBM, such as thermal stability assays comparing wild-type and mutant APC/C, cellular assays examining APC/C function in cells expressing the mutant, or at minimum, a clear statement that this is a structural observation without known functional significance.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative rigor
- **Claim pointer** The authors state that the CDH1CDC20α1 chimeric mutant "stimulated the same ubiquitination activity for both unphosphorylated and phosphorylated APC/C, similar to CDH1" and use this to conclude that the α1 helix is not a primary factor in determining CDH1's higher activity with unphosphorylated APC/C.
- **Evidence pointer** Supplementary Figure 3
- **Concern** The ubiquitination assays are described qualitatively. The authors state that experiments were performed in triplicate, but no quantification, statistical analysis, or error bars are shown in the described results. The conclusion that the α1 helix is not a primary factor relies on a visual comparison of gel bands. This is insufficient for a quantitative claim. The authors should provide densitometry quantification with statistical analysis to support this conclusion.
- **Why it matters** The conclusion about the relative roles of CDH1α1 versus CDC20α1 in determining coactivator affinity is a key mechanistic claim. Without quantitative support, the conclusion is not rigorously established.
- **Resolution test** Provide quantified ubiquitination data (e.g., densitometry of substrate or product bands) with statistical analysis (e.g., mean ± SD from at least three independent experiments, with appropriate statistical tests) for the chimeric mutant experiments.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Evidence strength
- **Claim pointer** The authors propose that phosphorylation of APC1 at Ser345, Ser351, and Ser355 relieves APC1AI autoinhibition by disrupting the APC1AI-APC8 interaction, thereby allowing CDC20 binding. They support this with the APC/CAPC1-3E mutant that shows constitutive activity with CDC20.
- **Evidence pointer** Figure 8, Supplementary Figures 7-8
- **Concern** The APC1AI mechanism is supported by structural observation and a single phosphomimetic mutant. While the APC/CAPC1-3E result is consistent with the model, it does not directly demonstrate that phosphorylation at these sites is the physiological mechanism. The authors note "considerable redundancy in the capacity of widely spaced APC1 phospho-sites" from prior studies, which complicates the interpretation. Direct evidence that phosphorylation at these specific sites disrupts the APC1AI-APC8 interaction would strengthen the claim. Additionally, the authors should address whether the APC1AI mechanism is specific to CDC20 or also affects CDH1 binding, given that CDH1 can bind unphosphorylated APC/C.
- **Why it matters** The phosphorylation-dependent switch from APC/CCDC20 to APC/CCDH1 is a central regulatory mechanism in mitosis. The proposed mechanism is plausible but requires stronger evidence to be fully convincing.
- **Resolution test** Provide direct biochemical evidence that phosphorylation of APC1 at Ser345, Ser351, and Ser355 (or phosphomimetic mutations) disrupts the APC1AI-APC8 interaction, such as pull-down or cross-linking experiments. Alternatively, test the APC1AI peptide with and without phosphorylation in binding assays to APC8.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the structures provide "insights into APC/C regulation" but does not specify what those insights are. The abstract would be stronger if it briefly mentioned the key findings (CDH1 N-terminal helix, APC2 zinc-binding module, EMI1 KEN box).
- **Required correction** Add one or two sentences in the abstract summarizing the key structural findings and their implications.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section, "Apo-APC/C" subsection
- **Evidence pointer** Figure 7, Supplementary Figure 2
- **Issue** The apo-APC/C structure is described as being rebuilt based on the revised APC/CCDH1:EMI1 structure, but the specific differences between the new apo-APC/C model and the previous one (PDB 5G05) are not clearly enumerated. The authors state that "major remodelling involved regions of APC/C that undergo conformational change" but do not provide a detailed comparison.
- **Required correction** Provide a more detailed description of the conformational differences between the new and old apo-APC/C structures, possibly with a supplementary figure showing the superposition and highlighting the changed regions.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Methods, PIXE experiments
- **Evidence pointer** Table 1
- **Issue** The PIXE data are presented as mean ± standard deviation from triplicate measurements on the same protein spot. This is not true experimental replication. The authors should clarify whether these are technical replicates and whether independent sample preparations were measured.
- **Required correction** Clarify the replication strategy in the Methods section. If only technical replicates were performed, acknowledge this limitation.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Figure 2
- **Evidence pointer** Figure 2d
- **Issue** The CDC20α1 model is based on an AlphaFold prediction fitted into density from a previously published map (EMD-4466). The authors should clarify the confidence in this assignment, given the lower resolution of the original map and the use of a predicted model.
- **Required correction** Add a statement in the text or figure legend about the confidence level of the CDC20α1 assignment and any limitations.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Results section, "An N-terminal α-helix of metazoan CDH1 interacts with APC1"
- **Evidence pointer** Figure 2
- **Issue** The authors use the term "fenestration" to describe the gap between APC6 and APC8 through which the CDH1 N-terminus threads. This is an unusual term in this context and may be confusing to readers.
- **Required correction** Consider using a more standard term such as "opening" or "channel" and define it clearly in the text.

## Risk / unsupported claims
- The claim that APC2ZBM "confers structural stability to the complex" is not directly supported by experimental evidence. The negative functional results suggest it may not play a critical role in the tested activities.
- The reinterpretation of the CDC20 N-terminal α-helix in the APC/CCDC20:CyclinA2 structure (PDB 6Q6H) relies on fitting an AlphaFold model into a previously published map at lower resolution. The confidence in this assignment is not fully discussed.
- The proposal that phosphorylation of APC1 at Ser345, Ser351, and Ser355 relieves autoinhibition is supported by a phosphomimetic mutant but lacks direct biochemical evidence for the phosphorylation-dependent mechanism.
- The claim that EMI1KEN binding to CDH1WD40 "presumably also" contributes to EMI1-mediated inhibition of APC/C is speculative, as no direct inhibition assay was performed to test this.
- The statement that the improved structures provide "the most complete and accurate structural models of the APC/C available to date" is difficult to evaluate without a systematic comparison to all other available APC/C structures.