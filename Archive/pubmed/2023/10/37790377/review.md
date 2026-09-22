## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific claims, methodology, and evidence presented in the manuscript
- **Shared manuscript claim summary** The authors propose that glutamylation of acidic intrinsically disordered regions (IDRs) of histone chaperones Npm2 and Nap1 enhances their function by increasing DNA charge mimicry, thereby improving histone binding, stabilization, and nucleosome assembly.
- **Visible evidence base** Abstract, Introduction, Results, Discussion, Limitations, Experimental Methods, figure legends (figures not provided)
- **Missing materials affecting confidence** Figures, supplementary figures, supplementary tables, movies, and raw data files were not provided. This limits verification of quantitative results and statistical analyses.

## Reviewer
- **Overall assessment** This manuscript presents a compelling hypothesis that glutamylation of histone chaperone acidic IDRs enhances DNA mimicry, thereby improving chaperone efficiency. The combination of biochemical, biophysical, and computational approaches is ambitious and potentially impactful. However, several technical concerns and missing details in the methodology and data presentation prevent full assessment of the claims. The study would benefit from additional controls, clearer quantification, and discussion of alternative interpretations.
- **Who would be interested in the results, and why** Researchers in chromatin biology, histone chaperone function, post-translational modifications, and intrinsically disordered proteins would find this study relevant. The proposed mechanism of DNA charge mimicry via glutamylation could have broader implications for understanding how PTMs modulate protein-nucleic acid interactions.
- **Major strengths** 1) The study addresses a long-standing question about the function of acidic IDRs in histone chaperones. 2) The combination of experimental approaches (biochemistry, NMR, MD simulations) provides complementary evidence. 3) The use of physiologically relevant Xenopus laevis proteins adds biological context. 4) The study introduces a novel concept of PTM-mediated enhancement of DNA mimicry.
- **Major Concerns** 
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that glutamylation of Npm2 and Nap1 acidic IDRs enhances histone binding and promotes histone stabilization.
  - **Evidence pointer** Results section "Chaperone glutamylation enhances histone binding and promotes histone stabilization", Figure 3
  - **Concern** The fluorescence binding assays and thermal shift assays are described, but the actual data (binding curves, melting curves, replicates) are not shown in the provided text. The KD values are reported with standard errors, but the fitting procedure and the number of independent experiments are not clearly stated. Additionally, the claim that glutamylation increases binding affinity by "approximately two orders of magnitude" is based on a single peptide (Npm2 A2) and may not be generalizable to full-length proteins.
  - **Why it matters** Without seeing the raw data and statistical details, it is difficult to evaluate the robustness of the binding and stabilization claims, which are central to the paper's thesis.
  - **Resolution test** Provide representative binding curves, melting curves, and statistical analysis for all replicates. Clarify the number of independent experiments and the fitting model used.
  
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Concern** The MD simulations are described as supporting the experimental findings, but the methods lack critical details. The force field parameters for glutamylated residues are not described, and the simulation setup (e.g., ion concentration, temperature coupling, equilibration protocol) is incomplete. The clustering analysis and contact frequency calculations are mentioned but not fully explained.
  - **Why it matters** Reproducibility of the computational results is essential for validating the mechanistic claims. Without proper parameterization details, the simulations cannot be independently verified.
  - **Resolution test** Provide full simulation parameters, including force field modifications for glutamylated residues, system setup, and analysis scripts. Consider depositing trajectories or providing a detailed methods supplement.
  
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Concern** The authors state that "glutamylation of these chaperone polyelectrolyte acidic stretches functions to enhance DNA electrostatic mimicry," but the direct comparison between glutamylated IDRs and DNA in terms of binding to histones is not quantitatively established. The thermal shift data show that DNA and long acidic peptides stabilize H2A/H2B, but the correlation between charge density and stabilization is not rigorously tested.
  - **Why it matters** The central claim of "DNA charge mimicry" requires a more direct demonstration that glutamylated IDRs behave like DNA in their interactions with histones.
  - **Resolution test** Perform competition assays between glutamylated IDRs and DNA for histone binding, or systematically vary charge density to show a quantitative relationship with stabilization.
  
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Concern** The NMR experiments are described, but the assignment completeness and the quality of the spectra are not discussed. The CSP data are presented qualitatively, and the significance of the observed changes is not quantified. The authors mention that some residues could not be assigned, but the impact of this on the conclusions is not addressed.
  - **Why it matters** NMR is a powerful technique for studying protein interactions, but incomplete assignments or poor spectral quality could lead to misinterpretation of the binding interfaces.
  - **Resolution test** Provide assignment completeness statistics, CSP plots with significance thresholds, and discuss how unassigned residues might affect the interpretation.
  
  - **Concern ID** R1-M5
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Concern** The study is limited to Xenopus laevis proteins and does not test the generality of the proposed mechanism in other organisms or chaperone systems. The authors acknowledge this limitation but do not discuss how their findings might translate to other systems.
  - **Why it matters** The broader relevance of the proposed mechanism depends on its conservation across species and chaperone families.
  - **Resolution test** Discuss the conservation of glutamylation sites in Npm2 and Nap1 orthologs, or provide preliminary data in another system.
  
- **Minor Comments** 
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability
  - **Affected element** Abstract
  - **Evidence pointer** Abstract
  - **Issue** The abstract is dense and uses jargon that may be inaccessible to non-specialists.
  - **Required correction** Simplify language and define key terms such as "DNA charge mimicry" and "polyelectrolyte."
  
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Methods
  - **Evidence pointer** Experimental Methods, "Competitive pull-down assays"
  - **Issue** The pull-down assay description lacks details on the stoichiometry of the components and the washing conditions.
  - **Required correction** Provide more detailed experimental conditions, including buffer compositions, incubation times, and washing steps.
  
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Methods
  - **Evidence pointer** Experimental Methods, "Histone capture disaggregation assay"
  - **Issue** The assay is described, but the quantification method (e.g., densitometry) and the statistical analysis are not specified.
  - **Required correction** Describe how the gels were quantified and how statistical significance was determined.
  
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Readability
  - **Affected element** Discussion
  - **Evidence pointer** Discussion
  - **Issue** The discussion of the broader implications of the findings is somewhat speculative and could be more focused.
  - **Required correction** Tighten the discussion and connect the findings more directly to the proposed model.
  
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Methods
  - **Evidence pointer** Experimental Methods, "Molecular dynamics simulations"
  - **Issue** The simulation time (1 μs) is mentioned, but the convergence of the simulations is not discussed.
  - **Required correction** Provide evidence of convergence, such as RMSD plots or block analysis.
  
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** 
  - **Originality** The concept of glutamylation enhancing DNA mimicry in histone chaperones is novel and could open new avenues for understanding PTM function. However, the idea of acidic IDRs as DNA mimics is not entirely new, and the study builds on prior work.
  - **Scientific importance** The findings have potential implications for chromatin biology and the regulation of histone dynamics. The mechanism proposed could be broadly relevant, but the study's limited scope (Xenopus only) tempers its immediate impact.
  - **Interdisciplinary readership** The study bridges biochemistry, biophysics, and computational biology, which could appeal to a broad audience. However, the technical depth may limit accessibility to non-specialists.
  - **Technical soundness** The experimental design is generally sound, but several technical details are missing, and the lack of raw data prevents full evaluation. The MD simulations require more rigorous validation.
  - **Readability for nonspecialists** The manuscript is well-written but uses specialized terminology that may be challenging for readers outside the field. The abstract and introduction could be more accessible.
- **Recommendation posture** Supportive if technical concerns are resolved. The core hypothesis is interesting and the experimental approach is appropriate, but the current evidence is insufficient to fully support the claims. The authors should address the technical concerns and provide additional data to strengthen the case.

## Risk / unsupported claims
- The claim that glutamylation increases binding affinity by "approximately two orders of magnitude" is based on limited data and may not be generalizable.
- The direct comparison between glutamylated IDRs and DNA in terms of histone binding is not quantitatively established.
- The MD simulation results are presented as supporting evidence, but the lack of methodological details prevents independent verification.
- The NMR CSP data are presented qualitatively, and the significance of the observed changes is not quantified.
- The study's conclusions are based on Xenopus laevis proteins, and the generality of the proposed mechanism to other organisms is not demonstrated.