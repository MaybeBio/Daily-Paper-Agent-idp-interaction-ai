## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and supplementary materials description
- **Assessment boundary** Scientific claims, experimental design, data interpretation, modeling approach, and consistency between results and conclusions
- **Shared manuscript claim summary** The authors report that LAT condensation on membranes is kinetically frustrated by limited bond availability, leading to dynamically arrested, non-equilibrium condensates with spindle-like structures, as supported by kinetic measurements and coarse-grained simulations
- **Visible evidence base** Experimental kinetic measurements (TIRF, FCS, single-molecule tracking), phase diagram mapping, temperature dependence studies, and coarse-grained model simulations
- **Missing materials affecting confidence** Supplementary figures (figs. S1–S12) and movies (movie S1) are referenced but not provided; detailed analysis procedures for density distribution fitting and phase diagram construction are only partially described; simulation parameter values beyond those stated are not fully specified

## Reviewer
- **Overall assessment** This manuscript presents a compelling and well-structured investigation into the kinetic control of LAT protein condensation on membranes. The combination of quantitative experimental measurements and coarse-grained simulations provides a coherent narrative supporting the central claim of kinetic frustration due to limited bond availability. The work is timely and relevant to the growing field of biomolecular condensates, particularly in the context of membrane-associated signaling complexes. However, the absence of key supplementary materials limits the ability to fully evaluate the robustness of the analysis and the strength of some conclusions. The manuscript would benefit from additional clarity in several areas, particularly regarding the interpretation of the phase diagram and the generalizability of the findings.

- **Who would be interested in the results, and why** Researchers in the fields of membrane biophysics, cell signaling, and biomolecular condensates would find this work of significant interest. The study addresses a fundamental question about how limited valency and 2D confinement influence phase separation kinetics, which has implications for understanding T cell receptor signaling and other membrane-associated signaling processes. Additionally, the methodological approach combining single-molecule tracking with coarse-grained simulations will appeal to biophysicists and computational biologists studying protein self-assembly.

- **Major strengths**
  1. The study addresses an important and under-explored question about kinetic control of membrane-associated protein condensation, moving beyond equilibrium thermodynamic descriptions
  2. The combination of experimental measurements (TIRF, FCS, single-molecule tracking) with coarse-grained simulations provides complementary evidence for the proposed mechanism
  3. The identification of spindle-like structures as kinetic traps is a novel and mechanistically insightful finding
  4. The temperature dependence studies and activation energy measurement provide quantitative insight into the rate-limiting step
  5. The discussion of biological implications, particularly regarding PLC-γ recruitment and signaling timing, is thoughtful and well-contextualized

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that the LAT condensation phase transition is kinetically frustrated and that the final state is not an equilibrium free-energy minimum, based on deviations from classical phase diagram behavior
- **Evidence pointer** Figure 2C, 2D; fig. S5, S6 (not provided)
- **Concern** The central claim of kinetic frustration relies heavily on the observation that coexisting phase compositions deviate from classical tie-line behavior and depend on initial conditions. However, the analysis methodology for constructing the phase diagram and determining cc and cd is only briefly described, and the key supplementary figures (figs. S5 and S6) are not available for evaluation. The distinction between true kinetic trapping and slow equilibration that would eventually reach equilibrium is not clearly established. The authors state that the system is "dynamically arrested" but do not provide direct evidence that the system would not reach equilibrium over longer time scales.
- **Why it matters** The central thesis of the paper rests on the claim that the observed state is kinetically trapped and out of equilibrium. If the system is merely slow to equilibrate but would eventually reach the equilibrium state, the interpretation would be fundamentally different. The evidence for kinetic trapping needs to be more definitive, such as demonstrating that the system does not evolve toward equilibrium over extended observation times or that the final state depends on the initial conditions in a way that is inconsistent with equilibrium.
- **Resolution test** Provide the full analysis of the phase diagram construction, including the fitting procedures and error analysis. Include time-course data showing that the system reaches a stable steady state that does not evolve further over extended times. Demonstrate explicitly that the final state depends on the initial protein density or preparation pathway, which would be inconsistent with equilibrium behavior.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Model validation
- **Claim pointer** The authors claim that the coarse-grained model "proved capable of recovering key experimental observations" and that it identifies spindle-like structures as kinetic traps
- **Evidence pointer** Figure 5; figs. S9–S11 (not provided)
- **Concern** The validation of the coarse-grained model against experimental data is not presented in sufficient detail. The manuscript states that the model reproduces kinetic profiles, coarsening dynamics, and dynamics within condensates, but the quantitative comparison between model predictions and experimental measurements is not shown. Key model parameters (e.g., bond energy, attempt rates, diffusion coefficients) are not systematically varied or compared to experimental estimates. The claim that spindles act as kinetic traps is based on model observations, but the connection to experimental structures is not directly demonstrated.
- **Why it matters** The modeling component is essential for providing mechanistic insight into the experimental observations. Without a clear demonstration that the model quantitatively reproduces the experimental data and that the spindle structures are experimentally verifiable, the mechanistic conclusions remain speculative. The model's predictive power and the robustness of its conclusions to parameter variations need to be established.
- **Resolution test** Provide quantitative comparisons between model predictions and experimental measurements (e.g., kinetic curves, cluster size distributions, diffusion behavior). Show sensitivity analysis for key model parameters. If possible, provide experimental evidence for spindle-like structures, such as super-resolution imaging or electron microscopy of the condensed phase.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretive clarity
- **Claim pointer** The authors state that "the observed slowed mobility within LAT condensates indicates kinetic frustration as a probable cause" and that the system exhibits "glass-like" dynamics
- **Evidence pointer** Figure 4; fig. S8 (not provided)
- **Concern** The interpretation of reduced mobility within condensates as evidence for kinetic frustration is not fully developed. Reduced mobility could also arise from high local viscosity or crowding effects in a dense phase, which would be consistent with equilibrium phase separation. The distinction between glassy dynamics arising from kinetic frustration and simple slow diffusion in a viscous medium is not clearly articulated. The single-molecule tracking data showing heterogeneous dynamics are interesting but the connection to the specific mechanism of limited bond availability is not made explicit.
- **Why it matters** The claim of glassy dynamics and kinetic frustration is a strong statement that distinguishes this system from typical phase-separating systems. The evidence needs to clearly differentiate between these possibilities. If the reduced mobility is simply due to high density and viscosity, the novelty of the kinetic frustration mechanism would be diminished.
- **Resolution test** Provide a more detailed analysis of the single-molecule tracking data, including the distribution of diffusion coefficients and the time-dependence of mobility. Compare the observed dynamics to predictions from the model for both kinetically frustrated and equilibrium systems. Discuss how the specific molecular mechanism of limited bond availability leads to the observed dynamic heterogeneity.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Introduction, paragraph 2
- **Evidence pointer** Location not provided
- **Issue** The description of the biological context and the rationale for studying the LAT:Grb2:SOS system could be more concise. The connection between the physical principles being studied and the biological relevance is somewhat implicit.
- **Required correction** Briefly clarify why understanding the physical principles of LAT condensation is important for understanding T cell signaling, perhaps by explicitly stating how kinetic control might affect signaling outcomes.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Materials and Methods, Simulation methods
- **Evidence pointer** Location not provided
- **Issue** The simulation methods section provides the basic equations but lacks details on system size, number of particles, simulation duration, and the range of parameters explored. The relationship between simulation time and experimental time is not discussed.
- **Required correction** Provide additional details on simulation setup, including system dimensions, particle numbers, simulation lengths, and how these relate to the experimental system. Specify the range of parameters tested and the criteria for determining steady state.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Results, phase diagram section
- **Evidence pointer** Figure 2C, 2D
- **Issue** The phase diagram appears to be constructed from a limited number of experimental conditions, and the error bars or confidence intervals for the phase boundaries are not shown. The number of independent experiments for each condition is not stated.
- **Required correction** Provide information on the number of replicate experiments for each condition and include error estimates for the phase boundaries. If the number of replicates is limited, acknowledge this limitation and discuss its potential impact on the conclusions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion
- **Evidence pointer** Location not provided
- **Issue** The discussion of biological implications, while thoughtful, is somewhat speculative. The claim that "the final state of a LAT condensate may be dominated by local conditions and signaling activity at the moment of its formation" is interesting but not directly supported by the experimental data presented.
- **Required correction** Clearly distinguish between conclusions directly supported by the data and speculative implications. Consider adding a brief paragraph on limitations of the study and future directions to test the proposed biological implications.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure 1
- **Evidence pointer** Location not provided
- **Issue** The description of Figure 1 in the text is somewhat brief. The figure appears to show the experimental setup and the phase transition, but the key features and the time course are not clearly described in the text.
- **Required correction** Expand the figure legend and the in-text description to clearly explain what is shown in each panel, including the time points, the labeling scheme, and the key observations.

## Risk / unsupported claims
- The claim that the system is "dynamically arrested" and would not reach equilibrium over longer time scales is not directly supported by the data presented, as long-term stability experiments are not shown
- The identification of spindle-like structures as the primary kinetic trap is based on model predictions without direct experimental verification
- The statement that "the observed kinetic feature is reminiscent of the non-equilibrium phase transitions, such as gelation and glass transitions" is an analogy that is not quantitatively supported
- The claim that PLC-γ recruitment could "help break kinetic barriers limiting LAT condensation" is speculative and not tested in this study
- The assertion that "multiple, distinct types of LAT condensate that may be able to coexist within a single cell" is a speculative implication not directly supported by the data

## Assessment against Nature-style criteria
- **Originality** The work presents a novel perspective on membrane-associated protein condensation by emphasizing kinetic control and frustration effects arising from limited bond availability. This contrasts with the more common equilibrium thermodynamic descriptions of phase separation and offers a fresh conceptual framework. The identification of spindle-like structures as kinetic traps is an original contribution.
- **Scientific importance** The findings have significant implications for understanding how membrane-associated signaling complexes form and function. The demonstration that kinetic factors, rather than purely thermodynamic ones, can determine the final state of protein condensates is important for the broader field of biomolecular condensates. The potential biological relevance to T cell signaling adds to the importance.
- **Interdisciplinary readership** The work bridges biophysics, cell biology, and computational modeling, making it relevant to a broad readership. The combination of experimental and simulation approaches is likely to appeal to researchers in multiple disciplines. However, the technical depth in both experimental and computational methods may limit accessibility to non-specialists.
- **Technical soundness** The experimental methods appear sound, and the combination of techniques is appropriate. The modeling approach is reasonable, but the validation against experimental data needs to be more thorough. The lack of access to supplementary materials limits the ability to fully assess the technical rigor of the analysis.
- **Readability for nonspecialists** The manuscript is generally well-written and logically organized. The introduction provides sufficient context, and the results are presented in a clear manner. However, some sections, particularly the simulation methods, may be challenging for readers without a computational background. The discussion of glassy dynamics and kinetic frustration could benefit from more accessible explanations.

## Recommendation posture
Supportive if technical concerns are resolved. The manuscript presents a compelling and novel investigation into the kinetic control of LAT condensation, with a strong combination of experimental and computational approaches. However, the central claim of kinetic frustration and non-equilibrium behavior needs to be more rigorously supported, particularly through a more detailed presentation of the phase diagram analysis and a clearer demonstration that the system is truly kinetically trapped. The modeling component would benefit from more thorough validation against experimental data. If these concerns are addressed, the work would make a significant contribution to the field.