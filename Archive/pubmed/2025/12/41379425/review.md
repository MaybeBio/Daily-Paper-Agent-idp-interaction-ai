## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors state that AlphaFold2 and AlphaFold3 predict beta-roll structures for all designed RTX sequence variants, but experimental characterization (molecular dynamics simulations, circular dichroism spectroscopy, small-angle x-ray scattering, and x-ray crystallography) shows that these variants adopt diverse, sequence-dependent structures in the absence and presence of calcium. The authors conclude that current structure prediction algorithms fail for conformationally dynamic proteins and call for predictive tools that account for intrinsically disordered states.
- **Visible evidence base** Abstract text only; no quantitative data, statistical analyses, or methodological details are available
- **Missing materials affecting confidence** Full manuscript, all figures and tables, experimental protocols, sequence design details, simulation parameters, crystallographic statistics, and any control experiments

## Reviewer
- **Overall assessment** The abstract presents a potentially important observation regarding the limitations of AlphaFold2 and AlphaFold3 for conformationally dynamic proteins. The central claim, that predictions diverge from experimental observations, is plausible and of interest to the structural biology and protein design communities. However, the abstract provides no quantitative evidence, no description of experimental rigor, and no details on the extent of disagreement between predictions and experiments. The case is not established from the supplied material alone.
- **Who would be interested in the results, and why** Researchers in protein structure prediction, computational biology, and protein engineering would be interested because the findings challenge the general applicability of AlphaFold-class tools. Additionally, those studying intrinsically disordered proteins and calcium-responsive biomaterials would value the experimental characterization of RTX variants. The work may also inform developers of next-generation prediction algorithms.
- **Major strengths** The study addresses a timely and important limitation of widely used prediction tools. The use of multiple complementary experimental techniques (simulation, spectroscopy, scattering, crystallography) is a strong approach for validating structural claims. The focus on a biologically and biotechnologically relevant protein class (RTX) adds practical significance.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract lacks quantitative comparison between predicted and experimental structures (e.g., RMSD values, agreement metrics). No information is provided on the number of variants tested, the reproducibility of experimental results, or the statistical significance of observed differences. The crystallographic evidence is mentioned but no resolution or refinement statistics are given. Without these, the central claim of prediction failure cannot be rigorously evaluated.
- **Assessment against Nature-style criteria** 
  - Originality: The observation that AlphaFold fails for dynamic proteins is not entirely new, but the systematic design and multi-technique validation of RTX variants may offer a novel contribution. The originality is moderate based on the abstract alone.
  - Scientific importance: The potential to inform improvements in prediction algorithms for disordered and stimuli-responsive proteins is significant, but the abstract does not yet demonstrate the breadth or depth needed to establish broad importance.
  - Interdisciplinary readership: The topic bridges computational biology, biophysics, and protein engineering, which could attract a wide audience. However, the abstract does not clearly articulate implications beyond the specific system.
  - Technical soundness: The use of multiple experimental methods is commendable, but the abstract provides no evidence of technical rigor, such as error bars, controls, or validation of simulation parameters. Technical soundness is not assessable from the abstract.
  - Readability for nonspecialists: The abstract is generally clear and accessible, with key terms defined. However, the significance of the findings for nonspecialists is not fully explained.
- **Recommendation posture** Currently not established from the provided evidence. The abstract suggests a potentially valuable study, but the lack of quantitative data and methodological detail prevents a supportive recommendation. A full manuscript with rigorous evidence could change this assessment.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that AlphaFold2 and AlphaFold3 predicted beta-roll structures for all RTX variants, but experimental characterization revealed diverse, sequence-dependent structures.
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract states that predictions and experiments disagree, but no quantitative data are presented to support this claim. There is no indication of how many variants were tested, how the predicted and experimental structures were compared, or what metrics were used to define disagreement.
- **Why it matters** The central conclusion of the paper rests on the demonstration that prediction algorithms fail for these proteins. Without quantitative comparison, the claim is anecdotal and cannot be verified or reproduced by readers.
- **Resolution test** Provide a table or figure showing predicted versus experimental structures for each variant, with quantitative metrics such as RMSD, TM-score, or secondary structure agreement. Include statistical analysis of the differences.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency
- **Claim pointer** The authors used molecular dynamics simulations, circular dichroism spectroscopy, small-angle x-ray scattering, and x-ray crystallography to characterize the variants.
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract lists these techniques but provides no details on experimental conditions, sample preparation, data analysis, or quality controls. For crystallography, no resolution or refinement statistics are mentioned. For simulations, no force field, simulation length, or convergence criteria are given.
- **Why it matters** The reliability of the experimental evidence is central to the claim that predictions are wrong. Without methodological details, the reader cannot assess whether the experimental structures are accurate or whether the simulations were performed appropriately.
- **Resolution test** Include a methods section with full experimental protocols, crystallographic data collection and refinement statistics, simulation parameters, and validation of the experimental structures.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scope of claim
- **Claim pointer** The authors conclude that it is critical to build predictive tools that consider intrinsically disordered protein states and validate these tools with multi-mode, multi-scale experimental data.
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract generalizes from a single class of proteins (RTX variants) to a broad conclusion about the need for new predictive tools. It is unclear whether the observed failures are specific to RTX proteins or indicative of a general limitation of AlphaFold for all conformationally dynamic proteins.
- **Why it matters** The broader significance of the work depends on the generality of the finding. If the failure is unique to RTX proteins, the implications for the field are more limited.
- **Resolution test** Discuss the generalizability of the findings, possibly by testing additional classes of dynamic proteins or by providing a mechanistic explanation for why AlphaFold fails for RTX variants.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Definition of RTX consensus sequences
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract mentions "tandem repeats of consensus sequences GGAGXDTLY" and "scrambled sequences GGAGXDTYL" but does not explain the difference between these and the native RTX repeat motif GGXGXDXUX.
- **Required correction** Clarify the relationship between the designed sequences and the native motif, and explain the rationale for the specific substitutions and scrambling.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Use of "evade"
- **Evidence pointer** Title; location not provided
- **Issue** The title states that proteins "evade structural prediction algorithms," which implies a deliberate or active mechanism. This is likely not the intended meaning.
- **Required correction** Rephrase the title to use more neutral language, such as "are not accurately predicted by" or "pose challenges for."

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Context for calcium-dependent behavior
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states that RTX proteins fold into beta-roll structures upon calcium binding, but it is unclear whether the designed variants retain this calcium responsiveness or whether the observed structural diversity occurs in both conditions.
- **Required correction** Specify the conditions under which each variant was characterized and whether calcium-dependent folding was observed for the designed variants.

## Risk / unsupported claims
- The claim that AlphaFold2 and AlphaFold3 fail to predict structures of all tested RTX variants is unsupported without quantitative comparison data.
- The claim that the variants adopt "diverse, sequence-dependent structures" is unsupported without detailed structural characterization data.
- The general conclusion that new predictive tools are needed for intrinsically disordered proteins is not established from the abstract alone.
- The relevance of the findings to biotechnology and sustainability applications is stated but not substantiated.