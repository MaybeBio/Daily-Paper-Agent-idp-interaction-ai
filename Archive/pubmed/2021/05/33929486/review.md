## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and supplementary figure legends.
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided manuscript text. No external data or unpublished information was consulted.
- **Shared manuscript claim summary** The authors propose that PLCγ1, beyond its canonical enzymatic role in PIP2 hydrolysis, functions as a structural scaffold that promotes phase separation of T cell signaling components. Specifically, they claim that PLCγ1 cross-links LAT molecules via its two SH2 domains, protects LAT from CD45-mediated dephosphorylation, and that its concentration non-monotonically regulates LAT cluster size, as supported by in vitro reconstitution, live-cell imaging, and coarse-grained computer simulations.
- **Visible evidence base** In vitro reconstitution assays on supported lipid bilayers with purified proteins, fluorescence recovery after photobleaching (FRAP) analysis, live-cell TIRF microscopy in Jurkat T cells, immunoblot analysis of signaling downstream of LAT, surface plasmon resonance binding measurements, and coarse-grained molecular dynamics simulations.
- **Missing materials affecting confidence** Full uncropped immunoblots, raw microscopy image data, detailed gating and quantification methods for image analysis, exact peptide sequences used in binding assays, and complete simulation parameter files. The manuscript text does not include figure panels, so visual inspection of data quality was not possible.

## Reviewer
- **Overall assessment** This manuscript presents a compelling and well-structured investigation into the role of PLCγ1 in promoting LAT phase separation. The combination of in vitro reconstitution, cell-based assays, and computational modeling provides a multi-pronged approach that strengthens the central claims. The finding that PLCγ1 acts as a scaffold, in addition to its enzymatic function, is conceptually novel and has implications for understanding T cell signaling dynamics. However, several technical concerns, particularly regarding the quantitative interpretation of the non-monotonic concentration effect and the physiological relevance of the in vitro conditions, need to be addressed before the case is fully established.
- **Who would be interested in the results, and why** Researchers in the fields of T cell immunology, signal transduction, membrane biology, and phase separation. The work is also relevant to those studying the biophysics of protein clustering and the role of multivalent interactions in cellular signaling. The findings may have implications for understanding diseases where PLCγ1 is dysregulated, such as certain leukemias and carcinomas.
- **Major strengths**
    1.  The study uses a powerful combination of techniques, including a well-established in vitro reconstitution system, to dissect the molecular mechanism.
    2.  The identification of a non-monotonic, concentration-dependent effect of PLCγ1 on cluster size is an interesting and non-obvious finding that suggests a regulatory role.
    3.  The use of computer simulations to provide a mechanistic explanation for the experimental observations is a strong point, adding a layer of physical insight.
    4.  The paper is clearly written and the logic of the experimental design is easy to follow.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness / Data interpretation
    - **Claim pointer** The claim that PLCγ1 concentration non-monotonically regulates LAT cluster size, with low concentrations promoting and high concentrations diminishing cluster formation.
    - **Evidence pointer** Figure 5, A and B; Figure 6 B; Videos 3-8.
    - **Concern** The non-monotonic effect is a central finding, but the manuscript text does not provide sufficient quantitative detail on how cluster size is defined and measured in both experiments and simulations. In the experiments, cluster size is inferred from "normalized variance" of fluorescence, which is an indirect measure. In the simulations, cluster size is measured by the number of particles. The text does not clearly explain how these two metrics are related, nor does it provide the actual data points or statistical analysis for the non-monotonic curve. The claim that the effect is "robust" across a wide range of LAT densities is stated, but the supporting data (Figure 7 A) is not shown in the text.
    - **Why it matters** The non-monotonic effect is a key novel finding and is central to the proposed model of size regulation. If the effect is not robustly demonstrated with clear quantitative metrics and statistical support, the main conclusion of the paper is weakened. The lack of clarity on the relationship between the experimental and simulation metrics makes it difficult to assess the validity of the model.
    - **Resolution test** The authors should provide a clear definition of cluster size for both experiments and simulations. They should show the full quantitative data for the non-monotonic curve, including error bars and statistical tests (e.g., ANOVA) for both the experimental and simulation results. They should also explicitly demonstrate how the "normalized variance" metric in experiments corresponds to the "number of particles" metric in simulations.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness / Physiological relevance
    - **Claim pointer** The claim that PLCγ1 protects LAT from CD45-mediated dephosphorylation, and that this is a key mechanism for stabilizing LAT clusters.
    - **Evidence pointer** Figure 9, A-D; Figure S5.
    - **Concern** The in vitro dephosphorylation assay (Figure 9 C, D) is performed with a high concentration of CD45 added to pre-formed LAT clusters. The text does not specify the concentration of CD45 used, nor does it address whether this concentration is physiologically relevant. More importantly, the claim of "protection" is based on the observation that PLCγ1 suppresses dephosphorylation. However, the text does not rule out the alternative explanation that PLCγ1 simply outcompetes CD45 for binding to pY132, rather than actively protecting it. The spatial exclusion mechanism is proposed, but the evidence for it (Figure S5) is not described in sufficient detail in the text.
    - **Why it matters** The protective function of PLCγ1 is presented as a second, independent mechanism for promoting cluster stability. If this mechanism is not convincingly demonstrated, the overall model is weakened. The distinction between passive competition and active protection is important for understanding the molecular mechanism.
    - **Resolution test** The authors should provide the concentration of CD45 used in the assay and justify its physiological relevance. They should design an experiment to distinguish between competitive binding and active protection, for example, by using a catalytically inactive CD45 mutant or a PLCγ1 mutant that cannot bind pY132. The spatial exclusion experiment should be described in more detail, with clear controls.
    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical soundness / Model validation
    - **Claim pointer** The claim that the coarse-grained computer simulations recapitulate the experimental observations and provide a mechanistic explanation for the non-monotonic size regulation.
    - **Evidence pointer** Figure 6, A-E; Figure 7, A-B; Videos 3-8.
    - **Concern** The simulation model is described as "minimal" and uses "patches" to represent binding domains. The text states that the goal is not to capture exact experimental ratios, but the model's ability to predict the non-monotonic effect is presented as a key validation. However, the text does not provide a sensitivity analysis of the model parameters. It is unclear how robust the non-monotonic effect is to changes in binding affinities, valencies, or particle concentrations. The "coalescence likelihood" is a useful concept, but its calculation is not fully detailed in the main text.
    - **Why it matters** The simulations are used to support the experimental findings and to provide a mechanistic framework. If the model's predictions are highly sensitive to parameter choices, its explanatory power is limited. A sensitivity analysis would strengthen the claim that the non-monotonic effect is an emergent property of the interaction network, rather than a specific artifact of the chosen parameters.
    - **Resolution test** The authors should provide a sensitivity analysis for the key model parameters (e.g., binding affinities, valencies, concentrations) and show that the non-monotonic effect is a robust feature of the model. They should also provide a more detailed description of the "coalescence likelihood" calculation in the main text or refer to a specific section in the supplementary information.
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity / Reproducibility
    - **Affected element** Materials and Methods, "Statistical analysis"
    - **Evidence pointer** Materials and Methods, "Statistical analysis"
    - **Issue** The text states that "Unless specified, unpaired two-tailed Student’s t tests were performed on data from at least three individual experiments." It is not clear which specific figures or data points this applies to, and whether multiple comparisons were corrected for.
    - **Required correction** Please specify which experiments were analyzed with t-tests and which were not. If multiple comparisons were made, please state the correction method used (e.g., Bonferroni, Holm).
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Results, "PLCγ1 promotes LAT cluster formation in vitro"
    - **Evidence pointer** Figure 1, C and D.
    - **Issue** The text states that PLCγ1-induced clusters are "less dynamic" than Grb2-induced clusters based on FRAP analysis. The terms "lower recovery frequency" and "longer half-recovery time" are used, but the exact values are not provided in the text.
    - **Required Correction** Please provide the quantitative FRAP data (e.g., mobile fraction, half-time) in the text or in a table, with appropriate statistical analysis.
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Clarity / Reproducibility
    - **Affected element** Materials and Methods, "Computer simulations"
    - **Evidence pointer** Materials and Methods, "Computer simulations"
    - **Issue** The description of the simulation model is brief. The text mentions "patches" and "ghost particles" but does not provide a complete description of the interaction potentials, the integration time step, or the total simulation time.
    - **Required Correction** Please provide a more complete description of the simulation model, including all interaction potentials, simulation parameters, and the number of independent simulations performed. This information is likely in the "Simulation details" section, but it should be summarized in the main text for clarity.
    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Discussion
    - **Evidence pointer** Discussion, paragraph 2
    - **Issue** The discussion of the spatial exclusion mechanism is somewhat speculative. The text states that "PLCγ1-mediated LAT clusters can exclude CD45" but does not provide a clear model for how this exclusion occurs.
    - **Required Correction** Please clarify the proposed mechanism of CD45 exclusion. Is it due to size exclusion, charge repulsion, or specific interactions? A more explicit model would be helpful.
- **Technical failings that need to be addressed before the case is established**
    - R1-M1: Lack of quantitative data and statistical analysis for the central non-monotonic effect.
    - R1-M2: The "protection" mechanism is not fully distinguished from competitive binding, and the physiological relevance of the CD45 concentration is not established.
- **Assessment against Nature-style criteria**
    - **Originality** High. The work challenges the traditional view of PLCγ1 as a purely enzymatic downstream effector and proposes a novel structural role in promoting phase separation. This is a significant conceptual advance.
    - **Scientific importance** High. The findings have broad implications for understanding the mechanisms of T cell activation, the regulation of membrane-associated signaling complexes, and the general principles of phase separation in biology.
    - **Interdisciplinary readership** High. The work bridges immunology, cell biology, and biophysics, and will be of interest to researchers in all three fields.
    - **Technical soundness** Moderate. The combination of techniques is powerful, but the lack of quantitative detail and the potential alternative explanations for the "protection" mechanism are significant weaknesses that need to be addressed.
    - **Readability for nonspecialists** Good. The paper is well-written and the concepts are explained clearly, making it accessible to a broad scientific audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The central hypothesis is novel and important, and the multi-pronged approach is commendable. However, the current manuscript does not fully establish the case due to the lack of quantitative rigor in presenting the key non-monotonic effect and the ambiguity in the "protection" mechanism. Addressing these concerns would significantly strengthen the paper.

## Risk / unsupported claims
- The claim that PLCγ1 concentration non-monotonically regulates LAT cluster size is not fully supported by the quantitative data presented in the text.
- The claim that PLCγ1 "protects" LAT from dephosphorylation is not fully distinguished from a simple competitive binding mechanism.
- The physiological relevance of the in vitro reconstitution conditions, particularly the concentrations of PLCγ1 and CD45, is not fully established.
- The claim that the computer simulations "recapitulate" the experimental observations is not fully supported without a sensitivity analysis of the model parameters.