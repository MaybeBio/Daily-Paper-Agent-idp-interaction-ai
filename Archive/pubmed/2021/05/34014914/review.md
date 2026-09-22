## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, supporting information references)
- **Assessment boundary** Scientific claims, methodological soundness, evidence quality, and alignment with stated conclusions; limited to content provided in the manuscript
- **Shared manuscript claim summary** The authors use coarse-grain and atomistic molecular dynamics simulations to characterize the conformational dynamics of the intrinsically disordered N-terminal domain of CXCR1 in apo and IL8-bound states. They report that ligand binding restricts conformational plasticity, induces an open C-shaped conformation, and that predicted chemical shift perturbations correlate with NMR data. They further argue that chemical shift perturbations do not directly report residue contacts in dynamic protein-protein interfaces.
- **Visible evidence base** Simulation trajectories (coarse-grain: 200 μs apo, 400 μs complex; atomistic: 1.6 μs), contact probability maps, RMSD/distance projections, SHIFTX2 chemical shift predictions, comparison with published NMR data
- **Missing materials affecting confidence** No simulation trajectory files, force field parameter details, convergence metrics, error bars on contact probabilities, or raw chemical shift prediction values; no explicit statistical treatment of simulation replicates; no direct experimental validation beyond literature comparison

## Reviewer
- **Overall assessment** The manuscript addresses a relevant and timely question regarding the conformational behavior of an intrinsically disordered region in a GPCR and its role in ligand recognition. The combination of coarse-grain and atomistic simulations is appropriate, and the comparison with NMR chemical shift data is a valuable attempt at experimental corroboration. However, several technical aspects require clarification and strengthening before the central claims can be considered fully established. The claim that chemical shift perturbations do not report contact interfaces is interesting but would benefit from more rigorous quantitative support.
- **Who would be interested in the results, and why** Researchers in GPCR biology, intrinsically disordered proteins, and computational biophysics would find this work relevant. Those studying chemokine receptor signaling and drug design targeting extracellular receptor regions would also be interested. The methodological approach of combining coarse-grain simulations with NMR chemical shift prediction could be of broader interest to the molecular simulation community.
- **Major strengths** The study addresses a structurally challenging and functionally important region of a GPCR. The use of microsecond-scale coarse-grain simulations with multiple replicates provides substantial sampling. The comparison with published NMR data is a constructive attempt to bridge simulation and experiment. The observation that chemical shift perturbations may not directly map to contact interfaces is a potentially important caveat for the field.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (convergence and statistical robustness), R1-M2 (force field and mapping validation), R1-M3 (quantitative comparison with NMR data)
- **Assessment against Nature-style criteria** Originality: moderate to high; the application to CXCR1 N-terminal domain is novel, though the general concept of disordered region plasticity is established. Scientific importance: moderate; relevant to GPCR signaling but not a paradigm shift. Interdisciplinary readership: limited; primarily computational biophysics and GPCR structural biology. Technical soundness: adequate but with gaps in convergence and validation. Readability for nonspecialists: acceptable; the writing is clear but assumes familiarity with simulation and NMR terminology.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding convergence, force field validation, and quantitative NMR comparison.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the N-terminal region of apo-CXCR1 samples multiple conformational states and that ligand binding restricts this plasticity to a single C-shaped conformation.
- **Evidence pointer** Results sections "Conformational plasticity of the N-terminal region of apo-CXCR1" and "Conformational restriction in the N-terminal region upon ligand binding"; Figures 3 and 4
- **Concern** The manuscript does not provide convergence metrics for the coarse-grain simulations. It is unclear whether the observed conformational ensembles are converged or whether additional sampling would reveal additional states. The contact probability maps are presented as averaged quantities without error estimates or block analysis. The claim of a single dominant C-shaped state in the ligand-bound form relies on the assumption that 40 μs of sampling per condition is sufficient, which is not demonstrated.
- **Why it matters** Without demonstrated convergence, the central claim of conformational restriction upon ligand binding cannot be distinguished from insufficient sampling in the bound state. The interpretation of the free energy landscape and the proposed conformational selection mechanism depends critically on the statistical robustness of the sampled ensembles.
- **Resolution test** Provide convergence metrics such as block-averaged contact probabilities with standard errors, time evolution of key order parameters, and a demonstration that the observed states are stable over the simulation time. Alternatively, perform additional independent simulations to confirm reproducibility.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors use coarse-grain simulations with the Martini force field and map selected structures to atomistic representations for chemical shift prediction.
- **Evidence pointer** Methods section "System setup and simulation parameters"; Results section "Mapping the N-terminal region interactions: Corroboration by NMR chemical shift perturbations"
- **Concern** The manuscript does not validate the coarse-grain model against atomistic simulations for the specific system studied. The atomistic simulations are described as a "control set" but no direct comparison of structural ensembles or key contacts between coarse-grain and atomistic resolutions is shown. The back-mapping procedure for chemical shift prediction is described but not validated against known structures or experimental data for the apo state.
- **Why it matters** The Martini force field is known to have limitations in reproducing detailed conformational ensembles of disordered regions. Without validation against atomistic simulations or experimental data, the coarse-grain results may be force field artifacts. The chemical shift predictions depend on the accuracy of the back-mapped atomistic structures, which is not established.
- **Resolution test** Provide a direct comparison of contact maps, secondary structure propensities, or radius of gyration distributions between coarse-grain and atomistic simulations. Validate the back-mapping procedure by comparing predicted chemical shifts for the apo state against experimental values, or by showing that the atomistic simulations reproduce known structural features.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors state that "we corroborated the dynamic complex sampled in our simulations against chemical shift perturbations reported by previous NMR studies and show that the trends are similar."
- **Evidence pointer** Results section "Mapping the N-terminal region interactions: Corroboration by NMR chemical shift perturbations"; Figure 5B and S7
- **Concern** The comparison between predicted and experimental chemical shift perturbations is qualitative. No quantitative correlation coefficient, root-mean-square deviation, or statistical test is provided. The statement that "trends are similar" is subjective. Furthermore, the manuscript does not specify which experimental data were used for comparison, the exact conditions of those experiments, or how the simulation conditions match those experiments.
- **Why it matters** The claim of experimental corroboration is a key pillar of the manuscript's validity. Without quantitative comparison, the agreement could be coincidental or driven by trivial factors. The authors' additional claim that chemical shift perturbations do not report contact interfaces requires a more rigorous demonstration that the discrepancies between contact maps and chemical shift data are meaningful rather than artifacts of prediction inaccuracies.
- **Resolution test** Provide a quantitative comparison, such as a Pearson correlation coefficient or a scatter plot of predicted versus experimental chemical shift perturbations with a fitted line and confidence intervals. Specify the experimental data source and conditions. Perform a sensitivity analysis of the chemical shift prediction method to assess its accuracy for disordered regions.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 4
- **Evidence pointer** Results section "Conformational restriction in the N-terminal region upon ligand binding"
- **Issue** The two-dimensional free energy projections in Figure 4 are described but the choice of collective variables is not fully justified. The manuscript states that RMSD and distance between residues 1-26 were used, but it is unclear why these specific variables were chosen and whether they capture the relevant conformational changes.
- **Required correction** Provide a brief justification for the choice of collective variables and consider showing projections along alternative variables to demonstrate robustness.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods section "Analysis"
- **Evidence pointer** Methods section "Analysis"
- **Issue** The clustering method is described as using the GROMOS algorithm, but the specific parameters (e.g., cutoff, number of clusters) are not provided. The manuscript states that a reference structure was chosen from the highest population cluster, but the criteria for selecting this cluster are not described.
- **Required correction** Provide the clustering parameters and the criteria for selecting the reference structure. This will allow readers to assess the sensitivity of the results to these choices.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion section
- **Evidence pointer** Discussion section, paragraph 2
- **Issue** The authors suggest a conformational selection mechanism based on the overlap between apo and bound state ensembles. However, the evidence for conformational selection versus induced fit is indirect, as no kinetic or transition path analysis is provided.
- **Required correction** Soften the language regarding the mechanism or provide additional analysis (e.g., transition path sampling or Markov state models) to support the conformational selection interpretation.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section "System setup and simulation parameters"
- **Evidence pointer** Methods section "System setup and simulation parameters"
- **Issue** The manuscript states that the Martini force field versions 2.0 and 2.2 were used for lipids and proteins, respectively. It is unclear why different versions were used and whether this choice affects the results.
- **Required correction** Clarify the rationale for using different force field versions and discuss any potential implications for the simulations.

## Risk / unsupported claims
- The claim that the N-terminal region is the "first site of ligand binding" is based on simulation observations but lacks direct experimental validation. The temporal ordering of contact formation is not rigorously established.
- The statement that "chemical shift perturbation is often not a reporter of residue contacts in such dynamic associations" is a general claim that extends beyond the specific system studied. The evidence provided supports a cautionary note for this system but does not justify a general principle.
- The suggestion of conformational selection as the binding mechanism is plausible but not directly demonstrated by the data presented.
- The claim that the coarse-grain simulations "corroborate" NMR data is overstated given the qualitative nature of the comparison.