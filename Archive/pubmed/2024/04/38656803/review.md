## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) as provided
- **Assessment boundary** Scientific content, technical soundness, and claims as presented in the supplied text; no external data or supplementary materials were available for verification
- **Shared manuscript claim summary** The authors propose that BRD4 condensation in the nucleus is modulated by its binding to acetylated chromatin, which enhances both the kinetics (nucleation rate) and thermodynamics (lower required valence) of condensation, and that acetylated chromatin acts as a heterogeneous nucleation seed, providing a mechanism for targeting transcriptional condensates to specific chromatin loci.
- **Visible evidence base** Live-cell imaging (immunofluorescence, Corelet optogenetic system, BRD4FL-mCherry/BRD4ΔN-mCherry constructs), quantitative image analysis (puncta count, size, volume, nucleation rate, delay time, number density, Pearson correlation coefficients), coarse-grained molecular dynamics simulations (LAMMPS), and drug treatments (JQ1, A485, TSA)
- **Missing materials affecting confidence** Supplementary figures (S1–S4), supplemental movies, full methods details (referred to Bio-protocol), raw data files, and statistical analysis details (e.g., exact n values, error bar definitions, significance tests) were not provided; these are needed to fully assess reproducibility and robustness

## Reviewer
- **Overall assessment** This manuscript presents a compelling and well-structured investigation into the interplay between chromatin binding and phase separation of BRD4, combining quantitative live-cell experiments with coarse-grained simulations. The central claim—that acetylated chromatin enhances both thermodynamic and kinetic aspects of BRD4 condensation—is supported by multiple complementary approaches, including a shift in critical valence upon JQ1 treatment, altered nucleation kinetics, and positional correlation of condensate reformation. The simulation results provide a plausible mechanistic framework that aligns with experimental observations. However, several technical concerns, particularly around the quantification methods, statistical rigor, and the interpretation of the phase diagram in the presence of chromatin, need to be addressed before the case is fully established. The manuscript is of high interest to the biophysics and cell biology communities, and the findings have potential implications for understanding transcriptional regulation and disease mechanisms.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, chromatin biology, transcription regulation, and biophysics. The work provides a mechanistic link between epigenetic marks and condensate targeting, which is relevant to understanding gene regulation, development, and diseases such as cancer where BRD4 is a therapeutic target. The combined experimental-simulation approach will also appeal to those interested in quantitative cell biology and coarse-grained modeling of intracellular processes.
- **Major strengths** (1) The combination of live-cell experiments and coarse-grained simulations provides a powerful, complementary approach to dissect the role of chromatin binding in condensation. (2) The use of the Corelet system allows for controlled induction of condensation and quantitative measurement of kinetic and thermodynamic parameters. (3) The study addresses an underexplored question—how substrate binding modulates condensation—and provides a clear conceptual model (heterogeneous nucleation on acetylated chromatin). (4) The findings are supported by multiple independent experimental manipulations (JQ1, A485, TSA, BRD4ΔN) and simulation conditions.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "chromatin binding provides a thermodynamic enhancement of BRD4's phase separation tendency," evidenced by a shift in critical valence from 5 (JQ1-treated) to 2 (control) in the Corelet phase diagram (Figure 2E, F).
- **Evidence pointer** Figure 2E, F; Methods: "Phase diagram data acquisition" and "Corelet system image analysis and phase diagram construction"
- **Concern** The phase diagram is constructed using a qualitative "Yes PS/No PS" classification by two observers, with disagreements excluded. This subjective thresholding could introduce bias, especially when comparing conditions (control vs. JQ1) where the observer may not be fully blinded (only one observer was blinded). The critical valence is then determined by logistic regression on this binary classification. The robustness of the reported critical valence shift (2 vs. 5) depends heavily on the consistency and objectivity of this classification. Furthermore, the lack of a left-hand boundary at low Core concentration in the control condition is interpreted as the nucleus being "poised" for phase separation, but this could also be an artifact of the limited concentration range probed or the sensitivity of the assay.
- **Why it matters** The thermodynamic enhancement is a central claim of the paper. If the phase boundary determination is not robust or is biased, the conclusion that chromatin binding lowers the saturation concentration (or required valence) is not firmly established. This would undermine the proposed mechanism of chromatin-mediated thermodynamic stabilization of condensates.
- **Resolution test** Provide a more quantitative and objective method for defining phase separation (e.g., based on fluorescence intensity thresholds, particle size, or a machine-learning classifier) with clear criteria. Report inter-observer variability and include a sensitivity analysis showing that the critical valence determination is stable across different classification thresholds. Ideally, provide a quantitative measure of condensate formation (e.g., fraction of cells with condensates as a function of concentration and valence) with error bars and statistical comparisons.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "acetylated chromatin binding aids BRD4FL condensate nucleation" based on reduced nucleation rates, longer delay times, and lower number density in JQ1-treated cells (Figure 4C–E).
- **Evidence pointer** Figure 4C–E; Methods: "Nucleation measurements" and "Slope, delay time, and number density"
- **Concern** The nucleation rate is estimated from the slope of the linear portion of the puncta count versus time curve, and the delay time is defined as the time before puncta increase consistently for two frames. These definitions are somewhat arbitrary and may be sensitive to the imaging frame rate, the thresholding method, and the choice of the "linear portion." The authors do not report the exact number of cells analyzed, the variability between cells, or the statistical significance of the differences in nucleation rate and delay time between control and JQ1-treated conditions. The claim of "significantly lower" nucleation rates requires statistical support.
- **Why it matters** The kinetic enhancement (faster nucleation on chromatin) is a key part of the proposed mechanism. If the differences in nucleation parameters are not statistically robust or are influenced by the analysis methodology, the conclusion that chromatin acts as a kinetic seed is weakened.
- **Resolution test** Report the number of cells (n) for each condition, the distribution of nucleation rates and delay times, and the results of appropriate statistical tests (e.g., t-test or Mann-Whitney U test). Provide a more rigorous definition of nucleation rate and delay time, and show that the conclusions are insensitive to the choice of analysis parameters (e.g., different linear fitting windows, different thresholds for puncta detection).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "the presence of acetylated chromatin allows for the formation of finite-size condensates at low valence, where off-chromatin condensation is not observed" (Figure 3C).
- **Evidence pointer** Figure 3C; Methods: "Phase diagram calculations" and "Nucleation simulations"
- **Concern** The simulation phase diagram in the presence of chromatin (Figure 3C) is based on a "quantitative definition for detecting finite-size condensates" that relies on a 3-fold difference in maximum and minimum densities along the z-axis. This definition is somewhat arbitrary and may not correspond to a true thermodynamic phase transition. The authors note that these clusters "do not grow to be much larger than the globule of compacted chromatin," suggesting they may be subsaturated clusters rather than equilibrium condensates. The distinction between a stable condensate and a transient cluster is not clearly defined in the simulations.
- **Why it matters** The simulation results are used to support the interpretation that chromatin-bound clusters are noncanonical condensates. If the detection criterion is not physically meaningful, the simulation may be overinterpreting the nature of these clusters, and the comparison to experimental observations may be misleading.
- **Resolution test** Provide a more rigorous thermodynamic analysis of the simulated clusters, such as computing the free energy barrier for nucleation, the size distribution of clusters, or the interfacial tension. Show that the detected clusters are indeed metastable or stable condensates with a well-defined dense phase, rather than transient fluctuations. Alternatively, discuss the limitations of the detection criterion and how it relates to experimental observables.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The authors state that "calibrated fluorescence microscopy" was used to construct the phase diagram, and that the simulations were parameterized to "reproduce the experimental phase diagram."
- **Evidence pointer** Methods: "Phase diagram data acquisition" and "Coarse-grained model"
- **Concern** The calibration of fluorescence intensity to absolute concentration (micromolar) is a critical step for the quantitative phase diagram. The details of this calibration (e.g., how the conversion factor was determined, the accuracy and precision of the calibration, whether it was validated across experiments) are not fully described. Similarly, the simulation parameters (interaction strengths, radii of gyration) are stated to be "chosen to reproduce the experimental phase diagram," but the specific values and the fitting procedure are not provided. This makes it difficult to assess the uniqueness of the simulation results and the robustness of the conclusions.
- **Why it matters** The quantitative agreement between experiments and simulations is a major strength of the paper. If the calibration and parameterization are not transparent or reproducible, the validity of the comparison is questionable, and other researchers cannot build on this work.
- **Resolution test** Provide full details of the fluorescence calibration procedure, including the FCS measurements, the conversion factors, and the error estimates. Provide the simulation parameters (interaction strengths, radii, etc.) in a table or supplementary file, and describe how they were fitted to the experimental data. Ideally, show that the simulation results are robust to reasonable variations in the parameters.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors propose a general model where "epigenetic modification of chromatin allows for rapid condensation of transcriptional activators like BRD4 at specific chromatin sites."
- **Evidence pointer** Discussion
- **Concern** The manuscript focuses on BRD4 and its interaction with acetylated chromatin. While the authors suggest this may be a general phenomenon, the evidence presented is specific to BRD4. The generality of the model is not tested, and the discussion does not adequately address potential alternative mechanisms (e.g., specific protein-protein interactions with other transcriptional machinery, or the role of chromatin architecture) that could also contribute to targeting.
- **Why it matters** The broader significance of the work depends on whether the proposed mechanism is generalizable. If the model is only applicable to BRD4, the impact is more limited. The authors should either provide evidence for generality or temper their claims.
- **Resolution test** Add a discussion of how the proposed mechanism might apply to other chromatin-binding proteins with similar dual modalities, or acknowledge the limitations of the current study in establishing generality. Alternatively, include preliminary data on another protein or a mutant BRD4 to test the model's predictions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1C
- **Evidence pointer** Figure 1C
- **Issue** The panel showing "a panel of cells arranged by expression level" is described but the figure itself is not provided in the text. It is unclear how the expression level was quantified and how the "gates" for analysis were determined.
- **Required correction** Clarify in the figure legend and text how expression levels were measured and how the gating was performed. Provide the actual figure panel for reference.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figures 4C–E, 6E, 6H
- **Evidence pointer** Figures 4C–E, 6E, 6H
- **Issue** The text states that differences are "significant" (e.g., "significantly decreased number," "significantly faster") but does not report the statistical test used, the p-values, or the number of replicates.
- **Required correction** Add statistical details to the figure legends and text, including the test used, the p-values, and the number of cells or biological replicates.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Methods: "Drug treatments"
- **Evidence pointer** Methods: "Drug treatments"
- **Issue** The concentration of JQ1 used in the washout experiments is stated as 100 nM, while in other experiments it is 1 μM. The rationale for this difference is not explained.
- **Required correction** Explain why different concentrations were used in different experiments, or use a consistent concentration.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The discussion of the clinical implications of JQ1 is brief and somewhat speculative. The statement that JQ1 "leads to randomized localization of BRD4 nucleation" could be interpreted as a potential mechanism of action, but this is not directly tested in a disease-relevant context.
- **Required correction** Either expand on the potential clinical implications with more nuance, or clearly state that this is speculative and requires further investigation.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods: "Coarse-grained model"
- **Evidence pointer** Methods: "Coarse-grained model"
- **Issue** The simulation model is described qualitatively, but the specific parameters (e.g., interaction strengths, radii, spring constants) are not provided in the text.
- **Required correction** Provide the simulation parameters in a table or supplementary file to ensure reproducibility.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 2E, F
- **Evidence pointer** Figure 2E, F
- **Issue** The phase diagrams in Figure 2E and F are described as having a "shaded area" to guide the eye, but the criteria for the shaded region are not defined.
- **Required correction** Define what the shaded area represents (e.g., the region of phase separation) and how it was determined.

## Risk / unsupported claims
- The claim that "chromatin binding provides a thermodynamic enhancement" is supported by the phase diagram shift, but the robustness of this shift is not fully established due to the qualitative nature of the phase separation classification (R1-M1).
- The claim that "acetylated chromatin acts as a heterogeneous seed" is supported by the nucleation kinetics and positional correlation data, but the statistical significance of the kinetic differences is not reported (R1-M2).
- The claim that "epigenetic modification of chromatin allows for rapid condensation" is presented as a general mechanism, but the evidence is specific to BRD4 and the generality is not tested (R1-M5).
- The simulation results are used to support the interpretation of noncanonical condensates, but the detection criterion for condensates in simulations is arbitrary and may not correspond to a true thermodynamic phase (R1-M3).
- The quantitative agreement between experiments and simulations is a key claim, but the calibration and parameterization details are not fully provided, making this agreement difficult to assess (R1-M4).
- The statement that "the presence of BRD4 interactors like MED1 in the nucleus could contribute to the preexisting puncta" is speculative and not directly tested.
- The claim that "overexpression increasing the supersaturation" explains the reduced significance in exogenous expression experiments is plausible but not directly demonstrated.