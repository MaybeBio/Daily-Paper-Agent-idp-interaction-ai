## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, materials and methods, and figure legends (figures themselves not provided)
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and internal consistency based on the provided text; figures and supplementary materials referenced but not directly examined
- **Shared manuscript claim summary** The authors propose that pioneer-factor activity of Grainy head (Grh) requires stable chromatin occupancy mediated by both sequence-specific DNA binding (via the conserved DBD) and the intrinsically disordered N-terminal domain, and that mitotic retention depends solely on sequence-specific DNA binding, separable from the mechanisms required for pioneering function
- **Visible evidence base** In vitro EMSA binding assays with recombinant proteins and nucleosomes; ChIP-seq and ATAC-seq in S2 cells; FRAP and single-particle tracking in Drosophila salivary glands; luciferase reporter assays; statistical methods described
- **Missing materials affecting confidence** Figures and supplementary figures not provided; numerical data, statistical outputs, and quality metrics for ChIP-seq/ATAC-seq not shown; exact FRAP and SPT parameter values and replicate numbers partially described but not fully documented; no source data files

## Reviewer
- **Overall assessment** This manuscript addresses an important question in the pioneer transcription factor field: how structured and disordered domains collectively contribute to pioneering activity. The authors combine multiple complementary approaches, including biochemistry, genomics, and quantitative live-cell imaging, to dissect the contributions of the DBD and the N-terminal disordered region. The central claim that stable chromatin occupancy requires both sequence-specific binding and disordered-domain-mediated interactions is well supported by the convergence of in vitro, cell-based, and imaging data. The separation of mitotic retention from pioneering activity is a notable conceptual advance. However, several technical concerns, particularly regarding the interpretation of FRAP and SPT data, the use of overexpression systems, and the lack of quantitative rigor in some genomic analyses, need to be addressed before the case is fully established.
- **Who would be interested in the results, and why** Researchers studying pioneer transcription factors, chromatin biology, gene regulation, and developmental biology would find these results of interest. The work also has relevance for understanding how disordered protein regions contribute to transcription factor function, a topic of broad interest in the molecular biology community. The potential implications for cancer biology, given the dysregulation of Grh family members in epithelial cancers, may attract translational researchers.
- **Major strengths** The combination of multiple orthogonal assays to dissect domain contributions is a clear strength. The use of quantitative live-cell imaging to assess chromatin occupancy dynamics in vivo provides mechanistic insight beyond static binding assays. The cross-species comparison between Drosophila Grh and human GRHL2 adds evolutionary perspective. The separation of pioneering activity from mitotic retention is conceptually important and challenges assumptions in the field.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (FRAP interpretation), R1-M2 (SPT analysis), R1-M3 (overexpression concerns), R1-M4 (genomic analysis rigor)
- **Assessment against Nature-style criteria** Originality: The work provides a novel conceptual framework for understanding how multiple domains contribute to pioneer activity, particularly the role of disordered regions in stable chromatin occupancy. The separation of mitotic retention from pioneering is an original contribution. Scientific importance: The findings have broad implications for understanding pioneer factor mechanisms and the role of disordered regions in transcription factor function. Interdisciplinary readership: The work bridges biochemistry, genomics, and biophysics, making it of interest to multiple communities. Technical soundness: The experimental approaches are generally appropriate, but several technical concerns need to be addressed, particularly regarding the interpretation of imaging data and the rigor of genomic analyses. Readability for nonspecialists: The manuscript is generally well-written and accessible, though some sections, particularly the imaging analyses, may be challenging for readers without specialized expertise.
- **Recommendation posture** Supportive if technical concerns are resolved. The central claims are plausible and supported by converging evidence, but the technical concerns regarding imaging data interpretation and genomic analysis rigor need to be addressed.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of imaging data interpretation
- **Claim pointer** The authors claim that FRAP recovery kinetics demonstrate that the N-terminus is required for stable chromatin binding, with Grh ΔN recovering dramatically faster (t1/2 = 21s) than wild-type (t1/2 = 291s) and reaching near 100% recovery.
- **Evidence pointer** Results section "Grh requires the DBD and regions outside for stable chromatin occupancy"; Figure 3B
- **Concern** The FRAP interpretation relies on the assumption that the bleached population represents chromatin-bound molecules. However, the authors state that Grh R806A was excluded from analysis because it was not detectably present on chromosomes, yet they do not provide a quantitative threshold for this exclusion. More critically, the FRAP recovery curves are normalized and interpreted without clear discussion of the mobile fraction versus the immobile fraction. The claim that wild-type Grh has a substantial immobile fraction (plateauing at 50%) is used to support stable binding, but the authors do not discuss whether incomplete recovery could be due to ongoing photobleaching during the imaging period or other technical artifacts. Additionally, the comparison between wild-type and Grh ΔN may be confounded by differences in expression levels or subcellular localization, which are not quantitatively addressed.
- **Why it matters** The FRAP data are central to the claim that the N-terminus mediates stable chromatin occupancy. If the interpretation is flawed, the conclusion that the disordered N-terminus is required for stable binding is weakened.
- **Resolution test** Provide quantitative analysis of the immobile fraction with appropriate controls for photobleaching during acquisition. Include expression level measurements and demonstrate that differences in recovery kinetics are not due to differences in protein concentration. Show representative FRAP curves with error bars and statistical analysis across multiple cells and biological replicates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of single-particle tracking analysis
- **Claim pointer** The authors claim that SPT analysis using a three-state Hidden Markov model reveals reduced proportions of Grh R806A and Grh ΔN molecules in the D1 and D2 states, consistent with less stable chromatin engagement, and that wild-type Grh molecules have high angular anisotropy indicating constrained movement and searching behavior.
- **Evidence pointer** Results section "Grh requires the DBD and regions outside for stable chromatin occupancy"; Figure 3C-E
- **Concern** The SPT analysis relies on a three-state HMM with specific diffusion coefficients, but the authors do not provide the actual diffusion coefficient values or the criteria for assigning states. The claim that D1 represents stably bound molecules is an assumption that needs validation, for example through comparison with known chromatin-bound fractions or through dual-color experiments. The angular anisotropy analysis is described as showing that wild-type Grh has high anisotropy, but the statistical comparison between conditions is not clearly described. Additionally, the number of tracks analyzed per condition and the criteria for track selection are not provided. The observation that Grh R806A has very few molecules in D1 is consistent with its lack of chromosome binding, but the quantitative comparison between Grh ΔN and wild-type needs more rigorous statistical treatment.
- **Why it matters** The SPT data provide quantitative support for the claim that the N-terminus stabilizes chromatin occupancy. Without proper validation of the HMM states and statistical rigor, the conclusions drawn from this analysis are not fully supported.
- **Resolution test** Provide diffusion coefficient values for each state with confidence intervals. Validate the assignment of D1 as stably bound through independent methods. Report the number of tracks analyzed, the statistical tests used, and the effect sizes for comparisons between conditions. Include representative trajectories and state assignment probabilities.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Experimental design and physiological relevance
- **Claim pointer** The authors claim that ectopic expression of Grh and its mutants in S2 cells at "physiological levels" allows assessment of pioneering activity, and that the observed effects reflect endogenous mechanisms.
- **Evidence pointer** Results sections "Grh has features of a pioneer transcription factor" and "Grh requires the DBD and regions outside for stable chromatin occupancy"; Materials and Methods "Experimental design"
- **Concern** The manuscript relies heavily on overexpression in S2 cells, which do not endogenously express Grh. While the authors state that expression levels were approximated to physiological levels based on immunoblots, the details of this calibration are not provided. The use of a heterologous system raises concerns about whether the observed effects reflect the endogenous function of Grh, particularly given that pioneer factor activity is context-dependent. The authors also use a copper-inducible promoter, which may not recapitulate endogenous expression dynamics. The claim that the N-terminus is required for pioneering activity in cells is based on overexpression of mutant proteins, which may have different stability or folding properties than the endogenous protein.
- **Why it matters** The physiological relevance of the findings depends on the appropriateness of the expression system. If the overexpression system does not faithfully recapitulate endogenous conditions, the conclusions may not hold in vivo.
- **Resolution test** Provide quantitative comparison of expression levels between overexpressed and endogenous Grh where possible. Include rescue experiments in a grh-null background to demonstrate that the mutants cannot complement endogenous function. Alternatively, use a more physiologically relevant system such as primary cells or in vivo assays.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Genomic analysis rigor
- **Claim pointer** The authors claim that ChIP-seq and ATAC-seq analyses demonstrate that Grh mutants have reduced binding at closed chromatin sites and fail to open chromatin, and that human GRHL2 can bind closed chromatin and promote accessibility in Drosophila cells.
- **Evidence pointer** Results sections "Grh has features of a pioneer transcription factor" and "Diverse N-terminal domains are sufficient for pioneering"; Figures 2E-F, 4C-D, 5B-C
- **Concern** The genomic analyses are described qualitatively, with limited information about the number of peaks, the statistical significance of differences between conditions, and the criteria for classifying sites as class I, II, or III. The comparison between wild-type and mutant binding at closed chromatin sites lacks quantitative metrics such as read enrichment at specific loci or genome-wide correlation analyses. The claim that GRHL2 binds closed chromatin and promotes accessibility is based on peak overlap and accessibility changes, but the extent of these effects relative to Drosophila Grh is not quantified. Additionally, the authors do not address potential confounding factors such as differences in protein expression levels between constructs, which could affect ChIP-seq signal.
- **Why it matters** The genomic data are central to the claim that the N-terminus is required for pioneering activity in cells. Without rigorous quantitative analysis, the conclusions are not fully supported.
- **Resolution test** Provide quantitative metrics for ChIP-seq and ATAC-seq analyses, including peak numbers, read enrichment values, and statistical comparisons between conditions. Include genome-wide correlation analyses and volcano plots or similar visualizations. Address potential confounding factors such as expression level differences.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of experimental design
- **Affected element** Materials and Methods, "Experimental design"
- **Evidence pointer** Materials and Methods section
- **Issue** The description of the EMSA experiments is incomplete. The authors state that "full-length recombinant Grh" was used, but the purification method for full-length Grh is not described in detail. The baculovirus expression system is described for the mutants, but it is unclear if the same system was used for wild-type full-length Grh.
- **Required correction** Clarify the expression and purification methods for all proteins used in EMSA experiments, including wild-type full-length Grh.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Statistical analysis section
- **Evidence pointer** Materials and Methods, "Statistical analysis"
- **Issue** The statistical analysis section describes the bioinformatics pipeline for ChIP-seq and ATAC-seq but does not describe the statistical tests used for comparing conditions in the imaging experiments (FRAP and SPT) or the luciferase assays.
- **Required correction** Add a description of the statistical tests used for all quantitative comparisons, including the number of biological replicates and the criteria for significance.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of GRHL2 results
- **Affected element** Results section "Diverse N-terminal domains are sufficient for pioneering"
- **Evidence pointer** Figure 5
- **Issue** The authors show that human GRHL2 can bind closed chromatin and promote accessibility in Drosophila cells, but the interpretation that this reflects a conserved mechanism is complicated by the fact that GRHL2 has a much shorter and more ordered N-terminus than Drosophila Grh. The authors do not discuss whether the GRHL2 N-terminus is disordered or whether it functions through a different mechanism.
- **Required correction** Discuss the structural differences between the Drosophila and human N-termini and whether the GRHL2 N-terminus is predicted to be disordered. This would strengthen the interpretation of the cross-species comparison.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Figure accessibility
- **Affected element** All figures
- **Evidence pointer** Figures 1-6 and supplementary figures
- **Issue** The figure legends are not provided in the manuscript text, making it difficult to fully assess the data presented. Key details such as the number of replicates, statistical annotations, and the specific constructs used in each panel are not available.
- **Required correction** Ensure that figure legends are included in the manuscript and provide sufficient detail for readers to interpret the data without referring to the main text.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Throughout the manuscript
- **Evidence pointer** Abstract, Results, Discussion
- **Issue** The terms "stable chromatin occupancy," "stable binding," and "stable chromatin engagement" are used somewhat interchangeably. While this is not incorrect, it would be helpful to define these terms clearly and use them consistently to avoid confusion.
- **Required correction** Define the operational meaning of "stable chromatin occupancy" in the context of the imaging and biochemical assays, and use consistent terminology throughout.

## Risk / unsupported claims
- The claim that "mitotic retention depends solely on sequence-specific DNA binding" is supported by the data showing that Grh ΔN is retained on mitotic chromosomes, but the authors do not test whether the N-terminus contributes to retention in any context. The claim of "solely" may be too strong given the limited number of mutants tested.
- The claim that "the disordered N-terminus supports pioneer activity through interactions that do not rely on strict amino acid sequence but instead overall composition" is based on the scrambled N-terminus experiment, but the authors do not test whether the scrambled sequence retains any residual sequence-specific interactions. The conclusion that composition, rather than sequence, is the key determinant is not fully established.
- The claim that "human GRHL2 can function as a pioneer factor in Drosophila cells" is based on binding and accessibility assays, but the authors do not demonstrate that GRHL2 can drive transcriptional activation or cell-fate changes in this context. The functional significance of GRHL2 binding and opening chromatin is not established.
- The claim that "stable chromatin occupancy mediated by multiple protein domains is necessary for pioneering function" is supported by the correlation between stable binding and pioneering activity, but the authors do not demonstrate causality. It is possible that stable occupancy is a consequence rather than a cause of pioneering activity.
- The claim that "in vitro binding to mononucleosomes only partially reflects the requirements of pioneer factors to occupy the more complex chromatin environment in cells" is supported by the discrepancy between in vitro and in vivo results, but the authors do not provide a mechanistic explanation for this discrepancy.