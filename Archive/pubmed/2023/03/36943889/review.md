## Review setup
- **Input scope** Full manuscript text (main text, methods, and references to supplementary figures)
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and modeling as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors report that short-duration (2–10 min) local mechanical stress applied via integrins elevates chromatin and nucleoplasm protein diffusivity for tens of minutes after force cessation, and that this "mechanomemory" is regulated by nuclear pore complex (NPC) transport. They further propose that force reverses heterochromatin protein 1 alpha (HP1α) condensation via chromatin unjamming, and support their interpretation with a dissipative particle dynamics (DPD) model.
- **Visible evidence base** Main text figures referenced (Figs. 1–6), supplementary figures referenced (Figs. S1–S14), methods descriptions for cell culture, magnetic twisting cytometry, FCS, MSD, FLIM-FRET, and DPD simulation
- **Missing materials affecting confidence** Actual figure images and numerical data values are not provided; supplementary figures are referenced but not viewable; statistical details (exact p-values, n numbers, error bar definitions) are not fully specified in the text; DPD model parameters are described as in Materials and Methods but the full parameter table is not visible

## Reviewer

- **Overall assessment** This manuscript addresses an interesting and potentially important question: whether mechanical force applied briefly to cells can produce persistent changes in nuclear protein diffusivity after force removal. The experimental approach combining single-molecule imaging, pharmacological perturbations, osmotic challenges, and computational modeling is ambitious and the findings, if robust, would be of interest to the mechanobiology and chromatin biology communities. However, the manuscript as presented has several significant weaknesses. The evidence for the central claim of "mechanomemory" relies on measurements at limited time points (5 min and 60 min post-stress), and the mechanistic interpretation involving HP1α phase separation reversal is inferred rather than directly demonstrated. The DPD model, while qualitatively consistent, has acknowledged limitations that reduce its confirmatory power. The pleiotropic effects of the pharmacological agents used (Pitloc 2, JIC-04) are acknowledged but not fully addressed. Statistical reporting is incomplete in several places. These issues need to be resolved before the case for mechanomemory in nuclear protein diffusivity is fully established.

- **Who would be interested in the results, and why** Researchers in mechanobiology, nuclear architecture, chromatin dynamics, and cell signaling would find these results of interest. The concept that brief mechanical stimuli can produce persistent changes in nuclear protein mobility, and that NPCs regulate the duration of this effect, has implications for understanding how cells integrate mechanical signals over time. The potential link between force, chromatin condensation state, and phase separation of HP1α could also interest investigators studying liquid-liquid phase separation in the nucleus. The findings may have broader relevance for understanding how mechanical cues from the microenvironment influence gene expression and nuclear function.

- **Major strengths** The study addresses a novel question with a multi-pronged approach. The combination of single-molecule tracking (MSD) and FCS provides complementary measures of protein diffusivity. The use of pharmacological agents (JIC-04, chaetocin) to manipulate chromatin condensation state is a reasonable strategy. The inclusion of a computational model (DPD) to explore mechanism is commendable. The authors are appropriately cautious in some of their interpretations, acknowledging limitations of their model and the pleiotropic effects of their pharmacological tools.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency for central claim
- **Claim pointer** The central claim is that "mechanomemory" in protein diffusivity persists "tens of minutes after cessation of force" (Significance section and Results).
- **Evidence pointer** Figures 1F, 1G, 3A–C; text states measurements at "5 min after the cessation of stress" and "1 h post stress application"
- **Concern** The manuscript reports diffusivity measurements at only two post-stress time points: 5 min and 60 min. The claim of "tens of minutes" of mechanomemory is inferred from the difference between these two time points, but no intermediate time points are shown. The recovery to baseline at 60 min is demonstrated, and elevation at 5 min is demonstrated, but the duration of the elevated state between these points is not characterized. The phrase "tens of minutes" implies a gradual decay process that is not directly shown.
- **Why it matters** The temporal profile of the mechanomemory effect is central to the paper's thesis. Without intermediate time points, the reader cannot assess whether the effect decays gradually, persists at a plateau, or has a more complex time course. This limits the ability to evaluate the proposed mechanism involving NPC-regulated recovery.
- **Resolution test** Provide diffusivity measurements at additional intermediate time points (e.g., 15, 30, 45 min post-stress) to directly characterize the duration and decay kinetics of the mechanomemory effect.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic interpretation
- **Claim pointer** The manuscript claims that force "dissociated clusters of heterochromatin protein 1 alpha (HP1α), likely by reversing protein–protein condensation in phase separation via unjamming of the chromatin" (Significance section) and that this is supported by FRET measurements (Figure 4A, B).
- **Evidence pointer** Figure 4A, B; text in "HP1-Mediated Heterochromatin Diffusivity Elevates after Force Cessation" section
- **Concern** The FRET efficiency changes (from approximately 5% to 1%) are interpreted as evidence for decondensation of HP1α-dependent chromatin. However, the manuscript does not provide a direct demonstration that the observed FRET changes correspond to dissolution of phase-separated condensates. The link between FRET efficiency, HP1α clustering, and phase separation is inferred. The authors do not show images of HP1α condensates before and after stress, nor do they provide evidence that the clusters observed are indeed phase-separated condensates rather than other types of protein assemblies. The claim that force "reverses" phase separation is therefore not directly supported.
- **Why it matters** The connection between mechanical force and phase separation reversal is a novel and potentially important claim. If the evidence for this is indirect, the claim should be tempered or additional experiments should be provided. Overinterpretation of FRET data as evidence for phase separation reversal could mislead the field.
- **Resolution test** Provide direct imaging evidence of HP1α condensates (e.g., confocal or super-resolution images) before and after stress, with quantification of condensate size, number, and dynamics. Alternatively, perform in vitro or in cellulo phase separation assays with purified HP1α under mechanical perturbation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Pharmacological specificity
- **Claim pointer** The manuscript uses JIC-04 (a histone demethylase inhibitor) and chaetocin (a methyltransferase inhibitor) to manipulate chromatin condensation and shows that stress can reverse JIC-04-induced condensation (Figure 2A, B).
- **Evidence pointer** Figure 2A–D; text in "Force Reverses Chemically Induced Chromatin and Nucleoplasm Condensation" section
- **Concern** The manuscript acknowledges that JIC-04 is also a Wnt/β-catenin signaling inhibitor and that Pitloc 2 affects clathrin-mediated endocytosis. However, the potential contribution of these off-target effects to the observed diffusivity changes is not experimentally addressed. For example, could JIC-04's effects on Wnt signaling independently alter chromatin state or protein mobility? Could Pitloc 2's effects on endocytosis indirectly affect nuclear transport or chromatin organization?
- **Why it matters** The pharmacological perturbations are used to support the mechanistic model that force reverses condensation. If off-target effects contribute to the observed phenotypes, the interpretation of these experiments is compromised.
- **Resolution test** Use additional, more specific pharmacological agents or genetic approaches (e.g., siRNA knockdown of specific demethylases or methyltransferases) to confirm the specificity of the observed effects. Alternatively, perform control experiments with Wnt pathway inhibitors or endocytosis inhibitors alone to rule out contributions from these pathways.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Model validity
- **Claim pointer** The DPD model is presented as supporting the experimental findings and providing mechanistic insight into NPC-regulated mechanomemory.
- **Evidence pointer** Figure S13, S14; text in "To elucidate the mechanism of the mechanomemory, we developed a dissipative particle dynamics (DPD) model" section
- **Concern** The DPD model has acknowledged limitations: the simulation timescale is only ~100 ms, which is orders of magnitude shorter than the experimental timescale of minutes. The model also shows a much smaller difference between chromatin and nucleoplasm diffusivity than observed experimentally. The authors state that increasing chromatin folding in the model could reduce this discrepancy, but this is presented as a calculation, not a revised simulation. The model's ability to qualitatively recapitulate the experimental results is encouraging, but its quantitative limitations and the lack of a direct mapping between simulation time and experimental time weaken its confirmatory value.
- **Why it matters** The model is used to support the claim that NPC transport regulates the duration of mechanomemory. If the model cannot quantitatively capture the experimental observations, its mechanistic predictions should be treated with caution.
- **Resolution test** Extend the DPD model to longer timescales or develop a multi-scale model that can bridge the gap between simulation and experimental timescales. Provide a more detailed mapping between model parameters and experimental conditions.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Statistical reporting
- **Claim pointer** The manuscript reports statistically significant differences in diffusivity between conditions (e.g., "increased from 6.54 × 10⁻⁸ µm²/s to 9.11 × 10⁻⁸ µm²/s after 2-min stress").
- **Evidence pointer** Figures 1D, 1F, 1G, 2A–D, 3A–C; Statistical Analysis section
- **Concern** The manuscript does not consistently report the number of biological replicates, the number of cells measured, the number of technical replicates, or the exact p-values for each comparison. Error bars are shown in figures but their meaning (SEM, SD, confidence interval) is not always specified in the figure legends. The statistical tests used are mentioned in the Methods but the specific test used for each comparison is not always indicated in the text or figures.
- **Why it matters** Incomplete statistical reporting prevents the reader from assessing the robustness and reproducibility of the findings. This is particularly important given the relatively small effect sizes reported (e.g., diffusivity changes of ~1.4–2-fold).
- **Resolution test** Provide complete statistical details for all comparisons, including n numbers, exact p-values, and the specific test used. Specify the meaning of error bars in all figure legends.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** Use of "mechanomemory"
- **Evidence pointer** Throughout the manuscript
- **Issue** The term "mechanomemory" is used to describe the persistent elevation of diffusivity after force cessation. However, "memory" typically implies a stored information that can be recalled. Here, the phenomenon is a persistent physical change in diffusivity. The term may be misleading.
- **Required correction** Consider defining "mechanomemory" explicitly at first use, or using a more descriptive term such as "persistent force-induced diffusivity elevation" or "mechanical hysteresis."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** DPD model parameters
- **Evidence pointer** Materials and Methods, DPD model description
- **Issue** The manuscript states that "all relevant parameters used in the model were estimated from those of the live cell" but does not provide a table of parameters or a detailed description of how each parameter was estimated. This limits the reproducibility of the simulations.
- **Required correction** Provide a table of all DPD model parameters with their values and the basis for their estimation.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of control experiments
- **Affected element** Osmotic challenge experiments
- **Evidence pointer** Figure 6; text in "Diffusivity Mechanomemory Is Regulated by Nuclear Pore Complex" section
- **Issue** The osmotic challenge experiments are used to modulate NPC size. However, osmotic stress can have broad effects on cell volume, cytoskeletal organization, and chromatin structure, which could independently affect protein diffusivity. The manuscript does not fully address these potential confounds.
- **Required correction** Discuss the potential broader effects of osmotic stress and, if possible, include control experiments that separate NPC-specific effects from general osmotic effects.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Generalizability
- **Affected element** Cell type specificity
- **Evidence pointer** Cell Culture section
- **Issue** The study uses CHO and MCF7 cell lines. It is unclear whether the observed mechanomemory phenomenon is generalizable to other cell types, particularly primary cells or cells in more physiologically relevant 3D contexts.
- **Required correction** Acknowledge this limitation in the Discussion and suggest future experiments in additional cell types or tissue models.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure accessibility
- **Affected element** Supplementary figures
- **Evidence pointer** References to Figures S1–S14
- **Issue** The manuscript relies heavily on supplementary figures, but these are not provided in the submitted text. The reader cannot evaluate the data presented in these figures.
- **Required correction** Ensure that all supplementary figures are included with the submission and are clearly referenced in the text.

## Risk / unsupported claims
- The claim that force "reverses" HP1α phase separation is not directly supported by the data presented; FRET changes are an indirect measure and no direct imaging of condensate dissolution is shown.
- The claim of "tens of minutes" of mechanomemory is not directly supported by time-course data; only 5-min and 60-min time points are shown.
- The DPD model's prediction that NPC number regulates the duration of mechanomemory is qualitatively consistent with experiments but quantitatively limited; the model's timescale (~100 ms) is far shorter than the experimental timescale (minutes).
- The statement that "the observed elevation of the diffusivity was a result of the applied stress" (Results) is supported by the no-stress control, but the possibility that the magnetic bead itself (independent of stress) could affect diffusivity is not explicitly addressed.
- The claim that "the continued chromatin and nucleoplasm mobility 15 to 30 min after cessation of the applied force" can explain "continued transcriptional activity" is speculative and not directly tested in this study.