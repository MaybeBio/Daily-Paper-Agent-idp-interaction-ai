## Review setup
- **Input scope** Full manuscript text (main text, methods, and partial supplementary figure/table references)
- **Assessment boundary** Scientific claims, methodological soundness, and evidence consistency as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors propose that the intrinsically disordered region (IDR) of FAM134B, when tethered to its reticulon homology domain (RHD), amplifies membrane remodeling during selective ER-phagy. They support this with atomistic and coarse-grained molecular dynamics simulations, reanalysis of prior experimental data, and a cell-based functional assay.
- **Visible evidence base** Main text figures (Figs. 1–7), supplementary figures (Figs. S1–S15), supplementary tables (Tables S1–S7), and methods section
- **Missing materials affecting confidence** Full supplementary figures and tables, simulation parameter files, raw trajectory data, and complete experimental protocols for cell-based assays

## Reviewer

- **Overall assessment** The manuscript presents a compelling computational and experimental case for the role of the FAM134B IDR in enhancing membrane curvature generation and selective ER-phagy. The combination of atomistic and coarse-grained simulations with reanalysis of prior experimental data and a targeted cell-based assay is a strength. However, several technical concerns regarding simulation methodology, statistical treatment, and the strength of the experimental validation need to be addressed before the central claims can be fully established.

- **Who would be interested in the results, and why** Researchers in membrane biology, autophagy, and intrinsically disordered protein function would find this work relevant. The demonstration that a disordered region can actively modulate membrane shape through entropic and interaction-based mechanisms has implications for understanding how disordered regions contribute to cellular membrane dynamics beyond simple tethering or scaffolding roles.

- **Major strengths**
  1. The study addresses a significant and under-explored question: the functional role of intrinsic disorder in membrane remodeling.
  2. The methodological approach is multi-scale, combining atomistic simulations, coarse-grained simulations, reanalysis of experimental data, and a new cell-based assay.
  3. The use of hybrid scaling in the coarse-grained model to account for the different interaction properties of structured and disordered regions is a thoughtful methodological advance.
  4. The reanalysis of prior experimental data (liposome remodeling) provides a direct link between simulation predictions and observable outcomes.

- **Major Concerns**

  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness of simulation methodology
  - **Claim pointer** The authors claim that the coarse-grained model with α=0.6 reproduces the atomistic ensemble of the IDR in solution, and that this scaling is appropriate for studying membrane-anchored IDRs.
  - **Evidence pointer** Fig. 2B, 2E; SI Appendix, Fig. S3
  - **Concern** The validation of the α=0.6 scaling is based on comparison of free energy surfaces and Rg/Re distributions between atomistic and coarse-grained simulations of the IDR in solution. However, the manuscript does not provide a quantitative measure of the agreement (e.g., overlap coefficient, Kullback-Leibler divergence). More critically, the validation is performed for the IDR in solution, but the model is then used for membrane-anchored IDRs where the interaction environment is different. The manuscript does not demonstrate that the scaling remains valid when the IDR is tethered to a membrane or to the RHD.
  - **Why it matters** If the coarse-grained model does not accurately capture the conformational ensemble of the membrane-anchored IDR, all subsequent conclusions about IDR-induced membrane curvature, sensing, and budding could be artifacts of the model rather than genuine physical behavior.
  - **Resolution test** Provide quantitative comparison metrics between atomistic and coarse-grained ensembles. Additionally, perform a sensitivity analysis by repeating key membrane simulations (e.g., curvature induction, budding) at different α values (e.g., α=0.5, 0.7) to demonstrate that the qualitative conclusions are robust to the choice of scaling parameter.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Statistical rigor of experimental data
  - **Claim pointer** The authors claim that deletion of the R12 segment from the IDR significantly reduces the number of puncta per cell, supporting the role of the IDR in ER-phagy.
  - **Evidence pointer** SI Appendix, Fig. S15C, S15D
  - **Concern** The statistical analysis of the puncta data is described only briefly. The manuscript states that "nonparametric one-way ANOVA tests" were used, but does not specify which test (e.g., Kruskal-Wallis), how multiple comparisons were handled, or whether the data met the assumptions for the chosen test. The number of independent experiments and the total number of cells analyzed are not stated. The representative images shown are from "duplicate IF experiments," which is a low number of biological replicates.
  - **Why it matters** The cell-based assay is the only direct experimental validation of the functional role of the IDR. If the statistical analysis is not rigorous or the number of replicates is insufficient, the claim that the IDR deletion impairs ER-phagy is not well supported.
  - **Resolution test** Provide a detailed description of the statistical methods, including the specific test used, the number of independent experiments, the number of cells analyzed per condition, and how multiple comparisons were corrected. If the number of replicates is low, additional experiments should be performed.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Evidence strength for mechanistic claims
  - **Claim pointer** The authors claim that the IDR "amplifies membrane remodeling" and "boosts RHD-mediated membrane budding" through a combination of entropic forces, protein-protein interactions, and membrane interactions.
  - **Evidence pointer** Figs. 4, 6; SI Appendix, Figs. S7, S10–S14
  - **Concern** The simulations demonstrate correlations between the presence of the IDR and enhanced membrane deformation/budding. However, the manuscript does not provide a clear mechanistic decomposition of the contributions from different physical factors (entropic pressure, electrostatic interactions, hydrophobic insertion, protein-protein clustering). The discussion mentions these factors but does not quantitatively attribute the observed effects to them.
  - **Why it matters** Without a mechanistic decomposition, the claim that the IDR "amplifies" membrane remodeling remains descriptive rather than explanatory. Understanding the physical basis of the IDR's effect is important for generalizing these findings to other IDR-containing membrane proteins.
  - **Resolution test** Perform additional simulations or analyses that isolate specific contributions, e.g., by mutating key hydrophobic residues in the IDR, varying the length of the IDR, or using a purely repulsive (non-interacting) IDR as a control. Alternatively, provide a quantitative analysis of the forces acting on the membrane in the presence and absence of the IDR.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Generalizability of findings
  - **Claim pointer** The authors state that the context-dependent behavior of the FAM134B IDR is "shared among other proteins involved in ER-phagy" based on sequence analysis.
  - **Evidence pointer** Fig. 1B; SI Appendix, Fig. S1, Table S1
  - **Concern** The sequence analysis groups ER-phagy receptors based on charge properties in the Das-Pappu diagram, but this is a purely sequence-based classification. The manuscript does not provide any simulation or experimental evidence that the IDRs of other ER-phagy receptors (e.g., TEX264, SEC62, RTN3, CCPG1) exhibit the same membrane remodeling behavior as the FAM134B IDR.
  - **Why it matters** The claim of shared behavior across ER-phagy receptors is an important generalization that extends the significance of the work beyond FAM134B. Without direct evidence, this claim is speculative.
  - **Resolution test** Either soften the claim to indicate that the sequence properties are shared but the functional consequences are not directly tested, or provide additional simulations of at least one other ER-phagy receptor IDR to demonstrate similar membrane remodeling behavior.

- **Minor Comments**

  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of methods
  - **Affected element** Methods section, "Rescaling Protein–Protein Interactions"
  - **Evidence pointer** Methods, "Rescaling Protein–Protein Interactions"
  - **Issue** The description of the hybrid scaling approach is somewhat unclear. The text states that "two different ϵα for self-interactions" are used, but it is not immediately clear how the boundary between the structured and disordered regions is defined, or how cross-interactions between the two regions are treated beyond the Lorentz-Berthelot combination rule.
  - **Required correction** Provide a more detailed description of the hybrid scaling implementation, including how the boundary between regions is defined and how cross-interactions are handled.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness of figure legends
  - **Affected element** Figure legends
  - **Evidence pointer** Figs. 4, 5, 6
  - **Issue** The figure legends do not specify the number of replicates for each simulation condition, nor do they indicate whether error bars or confidence intervals are shown.
  - **Required correction** Add information about the number of replicates and the meaning of any error bars or shaded regions in the figure legends.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interpretation of simulation timescales
  - **Affected element** Results, "FAM134B-IDR Boosts RHD-Mediated Membrane Budding"
  - **Evidence pointer** Fig. 6; SI Appendix, Fig. S11
  - **Issue** The manuscript reports budding rates in units of ns⁻¹ and μs⁻¹, but the simulation timescales are relatively short (microseconds). The biological relevance of these rates is not discussed.
  - **Required correction** Add a brief discussion of the limitations of the simulation timescales and how the observed rates might relate to biologically relevant timescales.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Consistency of terminology
  - **Affected element** Throughout
  - **Evidence pointer** Figs. 1, 3, 4
  - **Issue** The terms "IDR," "C-terminal IDR," and "FAM134B-IDR" are used somewhat interchangeably. It would be clearer to consistently use one term, or to define the abbreviations at first use.
  - **Required correction** Standardize terminology throughout the manuscript.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Validation of the coarse-grained model for membrane-anchored IDRs is insufficient.
  - R1-M2: Statistical analysis of the cell-based assay is under-reported.

- **Assessment against Nature-style criteria**
  - **Originality** The work addresses a novel question about the role of intrinsic disorder in membrane remodeling, which is a relatively unexplored area. The concept that an IDR can actively amplify membrane curvature generation is original and extends beyond the traditional view of IDRs as passive linkers or scaffolds.
  - **Scientific importance** The findings have implications for understanding the molecular mechanisms of ER-phagy and, more broadly, for how disordered regions contribute to membrane dynamics. This is a topic of growing interest in cell biology and biophysics.
  - **Interdisciplinary readership** The work bridges computational biophysics, membrane biology, and autophagy research. The methods and concepts are likely to be of interest to researchers in all three fields, though the technical depth of the simulation work may limit accessibility for some experimental biologists.
  - **Technical soundness** The simulation methodology is generally sound, but the validation of the coarse-grained model for the membrane-anchored context is a significant gap. The experimental validation is limited to a single cell-based assay with under-reported statistics.
  - **Readability for nonspecialists** The manuscript is generally well-written and the main findings are presented clearly. However, the methods section is highly technical and may be difficult for nonspecialists to follow. The significance statement and introduction do a good job of framing the work for a broad audience.

- **Recommendation posture** Supportive if technical concerns are resolved. The central hypothesis is interesting and the multi-scale approach is appropriate, but the validation of the coarse-grained model for the membrane-anchored context and the statistical rigor of the experimental data need to be addressed before the claims can be fully accepted.

## Risk / unsupported claims
- The claim that the context-dependent behavior of the FAM134B IDR is "shared among other proteins involved in ER-phagy" is not directly supported by functional evidence for those other proteins.
- The claim that the IDR accelerates budding by a factor of 3.3 and 2.0 is based on simulation-derived rates, but the manuscript does not provide confidence intervals or a statistical comparison between conditions.
- The statement that "membrane anchoring alone enables disordered regions to sense and influence local membrane shape" is supported by the KALP25–IDR simulations, but the magnitude of the effect is modest and its biological significance is not discussed.
- The reanalysis of prior experimental data (liposome remodeling) is used to support the simulation findings, but the manuscript does not provide a quantitative comparison between the simulated and experimental vesicle size distributions.