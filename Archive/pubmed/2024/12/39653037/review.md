## Review setup
- **Input scope** Full manuscript text including abstract, main text, figure legend, and supplementary declarations
- **Assessment boundary** Scientific claims, methodological soundness, and evidence quality as presented in the provided material
- **Shared manuscript claim summary** The authors argue that intrinsically disordered regions (IDRs) in reticulophagy receptors, specifically RETREG1/FAM134B, exhibit "Janus-like" conformational behavior, acting as either entropic tethers or effector scaffolds depending on their membrane anchor context. They claim this behavior amplifies membrane curvature sensing and remodeling, accelerates spontaneous budding, and enhances receptor clustering, thereby augmenting reticulophagy.
- **Visible evidence base** Abstract, main text narrative, one figure legend (Figure 1), and references to prior work [1]
- **Missing materials affecting confidence** No methods section, no quantitative data tables, no simulation parameters beyond a single MARTINI scaling factor, no statistical analyses, no experimental protocols, no supplementary figures or videos, no raw trajectory data, no cell-based assay details, no liposome assay details, no nsTEM imaging data

## Reviewer
- **Overall assessment** The manuscript presents an intriguing hypothesis regarding the dual functional roles of IDRs in reticulophagy, supported by a combination of coarse-grained molecular dynamics simulations and reanalysis of prior experimental data. However, the current text is a commentary-style article that lacks the methodological depth and quantitative evidence required to substantiate the central claims. The "Janus-like" concept is appealing but is not rigorously defined or quantitatively demonstrated. The link between simulation observations and biological function remains speculative, and several key claims are either under-supported or not directly evidenced in the provided material. The manuscript would benefit from a more complete presentation of methods, data, and statistical validation.
- **Who would be interested in the results, and why** Researchers in autophagy and selective degradation pathways, particularly those studying ER-phagy and receptor-mediated membrane remodeling. Also of interest to computational biophysicists working on membrane-protein interactions, intrinsically disordered proteins, and coarse-grained simulation methodologies. The conceptual framework of IDRs as context-dependent modulators of membrane shape could appeal to a broader cell biology audience interested in the functional versatility of disordered regions.
- **Major strengths** The manuscript addresses a timely and under-explored question regarding the functional role of IDRs beyond canonical LIR-mediated interactions. The use of a coarse-grained model adapted for IDR behavior is a reasonable approach to access timescales relevant to membrane remodeling. The integration of simulation with reanalysis of prior experimental data provides a multi-scale perspective. The "Janus-like" framing is conceptually appealing and could stimulate further research.
- **Major Concerns** 
  - R1-M1: The central claim of "Janus-like" behavior is not quantitatively defined or rigorously demonstrated. The manuscript describes a continuum of conformations but does not provide a clear metric or threshold that distinguishes "expanded" from "compact" states, nor does it show that this behavior is truly bimodal or context-switchable in a statistically meaningful way.
  - R1-M2: The simulation methodology is insufficiently described. Only the MARTINI scaling factor (α = 0.6) is mentioned, with no details on system size, simulation length, number of replicates, equilibration protocols, force field parameters, or analysis methods. This precludes assessment of the robustness and reproducibility of the results.
  - R1-M3: The claim that IDRs "promote and sense membrane curvature" is not directly supported by the presented evidence. The text describes curvature induction in flat bilayers and biased diffusion in buckled bilayers, but no quantitative curvature measurements, free energy calculations, or comparison to control systems (e.g., without IDRs) are provided.
  - R1-M4: The reanalysis of prior experimental data (liposome remodeling and nsTEM) is presented without any methodological detail. The comparison between WT-RETREG1 and RHD alone is mentioned, but the data, sample sizes, statistical significance, and experimental conditions are not described, making the claim of differential vesicle size (~30 nm vs ~60 nm) unverifiable.
  - R1-M5: The cellular assays (confocal microscopy for autophagic puncta) are mentioned only in passing, with no experimental details, quantification methods, or statistical analysis. The claim that the deletion variant (RETREG1Δ12) shows "significantly reduced" puncta is not supported by any presented data.
  - R1-M6: The conclusion that IDR-mediated acceleration of budding is biologically relevant to reticulophagy is speculative. The simulation system uses a simplified asymmetric bilayer with nine proteins, which may not represent the physiological ER membrane environment. The extrapolation to in vivo function requires additional validation.
- **Minor Comments** 
  - R1-m1: The abstract states "IDRs alone are sufficient to promote and sense membrane curvature," but the main text only demonstrates this for membrane-anchored IDRs, not free IDRs. The claim should be clarified or qualified.
  - R1-m2: The term "Janus-like" is used repeatedly but is never explicitly defined in operational terms. A clear definition with quantitative criteria would strengthen the manuscript.
  - R1-m3: The figure legend for Figure 1 is descriptive but lacks quantitative annotations (e.g., time points, curvature values, cluster sizes). The figure itself is not provided, so the visual evidence cannot be assessed.
  - R1-m4: The reference to prior work [1] is vague. The authors should specify which data are reanalyzed and how, to allow readers to trace the evidence.
  - R1-m5: The discussion of post-translational modifications (phosphorylation, ubiquitination) is speculative and not tied to any data presented in this manuscript.
  - R1-m6: The phrase "IDR–IDR interactions intensify volume exclusion" is not explained or supported by any presented analysis.
- **Technical failings that need to be addressed before the case is established** R1-M2 (methodological detail), R1-M4 (experimental reanalysis detail), R1-M5 (cellular assay detail), and R1-M3 (quantitative curvature evidence) are the most critical. Without these, the core claims cannot be evaluated.
- **Assessment against Nature-style criteria** 
  - Originality: The concept of IDRs as context-dependent modulators of membrane remodeling is novel and potentially original, but the presentation does not fully distinguish it from prior work on IDR-mediated membrane interactions.
  - Scientific importance: The question of IDR function in ER-phagy is important, and the proposed mechanism could have broad implications. However, the current evidence is insufficient to establish the importance of the specific claims.
  - Interdisciplinary readership: The topic bridges cell biology and computational biophysics, which could appeal to a broad audience. However, the lack of methodological detail may alienate experimentalists, while the speculative biological extrapolation may frustrate computational readers.
  - Technical soundness: The technical approach is reasonable in principle, but the lack of methodological transparency and quantitative validation undermines confidence in the results.
  - Readability for nonspecialists: The text is generally clear and accessible, but the heavy reliance on simulation jargon without explanation may hinder nonspecialist comprehension.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript presents an interesting hypothesis but lacks the methodological detail, quantitative data, and experimental validation required to support the central claims. Substantial revision with full methods, data, and statistical analyses would be necessary to make the case convincing.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim substantiation
- **Claim pointer** "Extensive analysis of the RETREG1-IDR indicates a continuum of conformations between expanded and compact structures, displaying a Janus-like feature."
- **Evidence pointer** Main text, paragraph 3; location not provided
- **Concern** The "Janus-like" behavior is described as a continuum of conformations, but the term "Janus-like" implies a bimodal or context-dependent switch between two distinct functional states. The manuscript does not provide a quantitative definition of "expanded" vs "compact" states, nor does it demonstrate that these states are functionally distinct or that the transition between them is regulated by the membrane anchor context.
- **Why it matters** The central thesis of the manuscript rests on this concept. Without a clear operational definition and quantitative evidence of bimodality or context-dependence, the claim is not falsifiable and cannot be rigorously evaluated.
- **Resolution test** Provide a quantitative metric (e.g., radius of gyration, end-to-end distance, or contact maps) with statistical distributions for IDR conformations in different anchor contexts, and demonstrate that the populations are statistically distinct and functionally relevant.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency
- **Claim pointer** "Using an adapted coarse-grained MARTINI model (α = 0.6; with reduced protein-protein interaction strength), we captured the conformational landscape of the RETREG1-IDR and its correct ensemble properties consistent with atomistic simulations."
- **Evidence pointer** Main text, paragraph 3; location not provided
- **Concern** The simulation methodology is described in a single sentence. No details are provided on system construction, force field parameters, simulation length, temperature/pressure coupling, number of replicates, equilibration, or analysis protocols. The claim of consistency with atomistic simulations is not supported by any comparative data.
- **Why it matters** Reproducibility is a cornerstone of computational research. Without full methodological details, the results cannot be replicated or independently verified, and the validity of the conclusions cannot be assessed.
- **Resolution test** Provide a complete methods section including all simulation parameters, system compositions, simulation lengths, replicate numbers, and a comparison of ensemble properties (e.g., radius of gyration, secondary structure propensity) against atomistic simulation data.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "IDRs alone are sufficient to promote and sense membrane curvature and can act as entropic tethers."
- **Evidence pointer** Abstract; main text, paragraph 4; location not provided
- **Concern** The claim that IDRs promote and sense membrane curvature is not directly evidenced. The text describes curvature induction in flat bilayers and biased diffusion in buckled bilayers, but no quantitative data (e.g., curvature values, free energy profiles, or comparison to controls without IDRs) are presented. The "entropic tether" function is also not quantitatively demonstrated.
- **Why it matters** These are central functional claims that distinguish the proposed mechanism from prior work. Without quantitative evidence, the claims remain speculative.
- **Resolution test** Provide quantitative measurements of membrane curvature (e.g., local curvature maps) for systems with and without IDRs, and free energy calculations or other metrics demonstrating the entropic tether effect.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "By revisiting data collected from previous in vitro liposome remodeling and nsTEM imaging assays, we found that the full-length WT-RETREG1 containing an intact C-terminal IDR is more effective in remodeling liposomes into smaller vesicles (~30 nm) than the RETREG1 RHD alone (~60 nm)."
- **Evidence pointer** Main text, paragraph 4; location not provided
- **Concern** The reanalysis of prior experimental data is mentioned without any methodological detail. The source of the data, the experimental conditions, the sample sizes, the statistical analysis, and the criteria for vesicle size measurement are not described. The claim of differential vesicle size is presented as a finding but is not verifiable from the provided material.
- **Why it matters** This is a key piece of experimental evidence linking the simulation results to biological function. Without proper documentation, the claim cannot be evaluated or reproduced.
- **Resolution test** Provide a detailed description of the reanalysis methods, including the original data source, experimental protocols, quantification methods, and statistical tests. Ideally, include the data or a reference to a publicly available dataset.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "We found that the deletion variant induces fewer budding events in our simulations and also displays a significantly reduced number of autophagic puncta in our confocal-microscopy-based cellular assays."
- **Evidence pointer** Main text, paragraph 5; location not provided
- **Concern** The cellular assays are described in a single sentence with no experimental details. The cell type, transfection method, fixation/staining protocol, imaging parameters, quantification method, and statistical analysis are all absent. The claim of "significantly reduced" puncta is not supported by any presented data or statistical test.
- **Why it matters** This is the only direct experimental validation of the proposed mechanism in a cellular context. Without proper documentation, the claim is unverifiable.
- **Resolution test** Provide a full description of the cellular assays, including cell lines, constructs, transfection, imaging, quantification, and statistical analysis. Include representative images and quantitative data with error bars and p-values.

- **Concern ID** R1-M6
- **Severity** Major
- **Blocking** No
- **Axis** Biological relevance
- **Claim pointer** "The presence of membrane-anchored IDRs accelerates the kinetics of RHD-mediated spontaneous budding."
- **Evidence pointer** Main text, paragraph 5; Figure 1; location not provided
- **Concern** The simulation system uses a simplified asymmetric bilayer with nine proteins on a 40x40 nm patch. The physiological relevance of this system to the ER membrane, which is complex and crowded, is not discussed. The extrapolation from this simplified system to in vivo reticulophagy requires justification.
- **Why it matters** The biological significance of the findings depends on the relevance of the simulation system to the native environment. Without this context, the claims may be overinterpreted.
- **Resolution test** Discuss the limitations of the simulation system and provide evidence or arguments that the observed behavior is likely to occur in the physiological ER membrane environment.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Claim precision
- **Affected element** Abstract
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states "IDRs alone are sufficient to promote and sense membrane curvature," but the main text only demonstrates this for membrane-anchored IDRs, not free IDRs in solution.
- **Required correction** Qualify the claim to specify that IDRs anchored to a membrane are sufficient, or provide evidence for free IDRs.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Definitional clarity
- **Affected element** Main text, paragraph 3
- **Evidence pointer** Main text, paragraph 3; location not provided
- **Issue** The term "Janus-like" is used repeatedly but is never explicitly defined in operational terms. It is unclear whether it refers to a bimodal conformational distribution, a context-dependent functional switch, or both.
- **Required correction** Provide a clear definition of "Janus-like" with quantitative criteria that can be tested.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 1
- **Evidence pointer** Figure 1 legend; location not provided
- **Issue** The figure legend is descriptive but lacks quantitative annotations such as time points, curvature values, or cluster sizes. The figure itself is not provided, so the visual evidence cannot be assessed.
- **Required correction** Add quantitative annotations to the figure and ensure the figure is available for review.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reference clarity
- **Affected element** Main text, paragraph 2
- **Evidence pointer** Main text, paragraph 2; reference [1]
- **Issue** The reference to prior work [1] is vague. It is unclear which data are reanalyzed and how, and whether the reanalysis is novel or simply a restatement of previous findings.
- **Required correction** Specify the source of the reanalyzed data and describe the reanalysis methods in detail.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Speculative content
- **Affected element** Main text, paragraph 6
- **Evidence pointer** Main text, paragraph 6; location not provided
- **Issue** The discussion of post-translational modifications (phosphorylation, ubiquitination) is speculative and not tied to any data presented in this manuscript.
- **Required correction** Either remove the speculation or provide supporting evidence or a clear hypothesis for future testing.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Explanation clarity
- **Affected element** Main text, paragraph 6
- **Evidence pointer** Main text, paragraph 6; location not provided
- **Issue** The phrase "IDR–IDR interactions intensify volume exclusion" is not explained or supported by any presented analysis.
- **Required correction** Provide a mechanistic explanation or data supporting this claim, or remove it.

## Risk / unsupported claims
- The claim that IDRs "promote and sense membrane curvature" is not directly supported by quantitative data in the provided material.
- The claim that IDRs act as "entropic tethers" is not quantitatively demonstrated.
- The claim that WT-RETREG1 is more effective than RHD alone in remodeling liposomes is based on reanalysis of prior data with no methodological detail.
- The claim of "significantly reduced" autophagic puncta in the deletion variant is not supported by any presented data or statistical analysis.
- The extrapolation from simplified simulation systems to physiological reticulophagy is speculative without additional validation.
- The discussion of post-translational modifications as modulators of IDR behavior is speculative and not tied to data.