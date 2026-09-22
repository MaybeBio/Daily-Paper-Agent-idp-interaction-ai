## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) from preprint server
- **Assessment boundary** Scientific validity, technical soundness, and claims as presented in the provided material
- **Shared manuscript claim summary** The authors present a GPU-accelerated hybrid resolution (HyRes) protein model that combines atomistic backbone representation with coarse-grained side chains, and demonstrate its application to simulate liquid-liquid phase separation (LLPS) of two intrinsically disordered proteins, GY-23 and TDP-43 conserved region, capturing mutation effects and secondary structure coupling.
- **Visible evidence base** Main text figures referenced (Figures 1-7), supplementary figures and tables referenced (Figures S1-S13, Tables S1-S4), methods section, simulation protocols
- **Missing materials affecting confidence** Supplementary figures and tables not provided; simulation parameter files not provided; force field parameters not provided; trajectory analysis scripts not provided

## Reviewer
- **Overall assessment** This manuscript describes a significant technical advance in coarse-grained simulation of protein phase separation by introducing a hybrid resolution model that retains atomistic backbone detail. The work addresses a recognized limitation of Cα-only models in capturing backbone-mediated interactions and secondary structure effects. The validation against experimental data for two systems is encouraging, and the mechanistic insights regarding the role of helicity versus side chain hydrophobicity in TDP-43 are potentially important. However, several technical concerns regarding force field rebalancing, simulation convergence, and quantitative comparisons need to be addressed before the case is fully established.
- **Who would be interested in the results, and why** Researchers in computational biophysics and molecular simulation of intrinsically disordered proteins, experimentalists studying phase separation and membraneless organelles, and developers of coarse-grained force fields. The work provides a practical tool for studying secondary structure coupling in LLPS, which is a growing area of interest given recent experimental evidence linking transient structure to condensate properties.
- **Major strengths** The hybrid resolution approach is conceptually well motivated and addresses a clear gap in existing methodology. The GPU implementation provides substantial computational speedup, making direct simulation of phase separation feasible. The validation across multiple IDPs with different properties strengthens confidence in transferability. The mechanistic analysis of TDP-43 mutants provides testable predictions and challenges existing assumptions about helix-helix interactions in condensates.
- **Major Concerns** 
  - R1-M1: Force field rebalancing procedure not fully described
  - R1-M2: Simulation convergence criteria not clearly established
  - R1-M3: Quantitative comparison with experimental Csat values shows systematic deviation
  - R1-M4: Contact analysis methodology may not adequately distinguish specific versus nonspecific interactions
  - R1-M5: Generalizability claims may be premature given limited test set
- **Minor Comments** 
  - R1-m1: Figure numbering inconsistency in text
  - R1-m2: Definition of "semi-quantitative" should be clarified
  - R1-m3: Discussion of limitations could be expanded
  - R1-m4: Some methodological details in supplementary materials not described in main text
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** 
  - Originality: High. The hybrid resolution approach with atomistic backbone is a novel contribution to the field, addressing a recognized limitation of existing models.
  - Scientific importance: High. The ability to accurately simulate secondary structure coupling in LLPS has broad implications for understanding biological condensates and their role in disease.
  - Interdisciplinary readership: Moderate. The work will primarily appeal to computational biophysicists and molecular simulators, though the biological implications for TDP-43 pathology may attract broader interest.
  - Technical soundness: Moderate. The approach is well motivated and validated, but several technical details require clarification and additional validation.
  - Readability for nonspecialists: Good. The manuscript is clearly written with appropriate context for understanding the significance of the work.
- **Recommendation posture** Supportive if technical concerns are resolved

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that removal of the SASA term in HyRes-GPU is "compensated by recalibrating the backbone LJ parameters" and that this allows reproduction of conformational properties.
- **Evidence pointer** Methods section, Table S1, Figure S1
- **Concern** The recalibration procedure for backbone LJ parameters is not described in sufficient detail. The authors state that parameters were adjusted to reproduce properties of two model peptides, but the specific optimization protocol, target properties, and acceptance criteria are not provided. This makes it difficult to assess whether the rebalancing is robust or system-specific.
- **Why it matters** The removal of the SASA term represents a significant change to the energy function. Without a clear description of the rebalancing procedure, it is unclear whether the model will transfer to other systems or whether the reported accuracy is coincidental for the test cases examined.
- **Resolution test** Provide a detailed description of the parameter optimization procedure, including target data, objective function, optimization algorithm, and validation on held-out systems. Demonstrate that the rebalanced parameters are not overfit to the two test peptides.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "the system reached similar phase separated states within ~1 µs regardless of the initial configurations" and that simulations are sufficient to reach phase equilibrium.
- **Evidence pointer** Results section "HyRes-GPU simulation of spontaneous phase separation of GY-23", Figure 3, Figure S3
- **Concern** The convergence criteria for phase equilibrium are not clearly defined. The authors state that simulations reached similar states from different initial conditions, but do not provide quantitative measures of convergence such as time evolution of order parameters, block averaging analysis, or comparison of multiple independent replicas. The 2-µs simulation time may be insufficient for systems with slow relaxation dynamics.
- **Why it matters** Reliable determination of phase equilibrium is essential for accurate calculation of coexistence densities and critical parameters. If simulations are not fully converged, the reported phase diagrams and derived quantities may be systematically biased.
- **Resolution test** Provide quantitative convergence analysis including time evolution of key observables (e.g., cluster size, density), comparison of multiple independent simulations, and demonstration that results are stable over extended simulation times.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative accuracy
- **Claim pointer** The authors state that "HyRes simulations successfully recapitulate the effect of these mutants on the helicity and LLPS propensity of TDP-43 CR" and report a correlation coefficient of r = 0.77 between simulated and experimental Csat values.
- **Evidence pointer** Results section "Phase separation of TDP-43", Figure 6B, Table S4
- **Concern** The reported correlation between simulated and experimental Csat values shows a systematic overestimation of approximately 2-3 fold. While the correlation is encouraging, the systematic bias suggests that the model may not accurately capture the absolute free energies of phase separation. The authors attribute this to the use of a shorter construct in simulations, but this explanation requires quantitative support.
- **Why it matters** Accurate prediction of absolute Csat values is important for quantitative comparison with experiments and for predicting the effects of mutations in a predictive manner. A systematic bias limits the utility of the model for quantitative predictions.
- **Resolution test** Provide a quantitative analysis of the systematic deviation, including comparison of simulation results with the full-length construct if possible, or a rigorous argument for why the shorter construct explains the observed discrepancy. Discuss whether the systematic bias affects the relative ranking of mutants.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretational validity
- **Claim pointer** The authors conclude that "the balance between backbone and sidechain-mediated interactions, but not helicity itself, actually determines LLPS propensity" based on analysis of contact probabilities and artificial mutants.
- **Evidence pointer** Results section "How residual helicity modulates TDP-43 CR LLPS propensity", Figures 7, S10-S13
- **Concern** The conclusion that helicity itself does not contribute to LLPS propensity is based on indirect evidence from contact probability analysis and artificial mutants with imposed dihedral restraints. The artificial mutants may not accurately represent the conformational ensemble of naturally occurring variants, and the contact analysis may not capture all relevant interactions.
- **Why it matters** This conclusion challenges existing hypotheses about the role of helicity in LLPS and has implications for understanding disease-associated mutations. If the conclusion is not robust, it could mislead future experimental and computational studies.
- **Resolution test** Provide additional validation of the conclusion using alternative approaches, such as mutational analysis that separates helicity changes from side chain effects, or comparison with experimental data that directly probes the role of helicity in LLPS.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The authors state that "HyRes-GPU dramatically expands the capability of CG simulations of IDP phase separation" and imply broad applicability of the model.
- **Evidence pointer** Throughout the manuscript
- **Concern** The model is validated on only two IDP systems, GY-23 and TDP-43 CR, both of which are relatively short and have specific sequence features. The generalizability of the model to longer IDPs, multi-domain proteins, or systems with different amino acid compositions is not demonstrated.
- **Why it matters** The claimed broad applicability of the model is not supported by the evidence presented. If the model fails for other systems, its utility would be significantly limited.
- **Resolution test** Demonstrate the model's performance on additional IDP systems with diverse sequence properties, or provide a clear discussion of the expected limitations and applicability domain of the model.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure numbering
- **Evidence pointer** Results section "GPU acceleration of the HyRes protein model"
- **Issue** The text refers to "Figure 1A" for the HyRes model illustration, but the figure layout is not described in the text. Additionally, the text mentions "Figure 1B" for speedup data, but the figure caption is not provided.
- **Required correction** Ensure all figure panels are clearly described in the text and that figure captions are complete and self-contained.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Throughout the manuscript
- **Issue** The term "semi-quantitative" is used to describe the model's accuracy, but the specific meaning is not defined. It is unclear whether this refers to accuracy within a factor of 2, order-of-magnitude agreement, or some other metric.
- **Required correction** Define the term "semi-quantitative" in the context of the model's performance, or use more specific quantitative descriptors.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Limitations discussion
- **Evidence pointer** Conclusion section
- **Issue** The discussion of limitations is brief and does not address potential issues such as the sensitivity of results to force field parameters, the effect of system size on phase behavior, or the accuracy of the implicit solvent model.
- **Required correction** Expand the discussion of limitations to include these and other relevant considerations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Methods section
- **Issue** Several methodological details are only described in supplementary materials, which are not provided. This includes the specific protocol for generating initial configurations, the criteria for identifying phase separation, and the analysis scripts used.
- **Required correction** Ensure that all essential methodological details are included in the main text or that supplementary materials are made available for review.

## Risk / unsupported claims
- The claim that "HyRes-GPU fully retains the ability of HyRes II in predicting residual helical propensities" is not fully supported by the data presented, as only a limited number of IDPs were tested and the comparison to HyRes II is not shown directly.
- The statement that "the balance between backbone and sidechain-mediated interactions, but not helicity itself, actually determines LLPS propensity" is a strong conclusion that may not be fully supported by the indirect evidence presented.
- The claim that the model "dramatically expands the capability of CG simulations of IDP phase separation" is not quantitatively supported by comparison with existing state-of-the-art models.
- The assertion that "HyRes-GPU is sufficiently balanced to capture rapid peptide exchange between the dilute and condensed phases" is based on qualitative observations and lacks quantitative comparison with experimental exchange rates.
- The generalizability of the model to other IDP systems beyond the two tested is not demonstrated and should be considered an open question.