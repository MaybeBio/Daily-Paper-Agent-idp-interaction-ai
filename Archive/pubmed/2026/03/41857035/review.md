## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary information descriptions
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors propose that membrane interfacial potential, determined by lipid composition, governs the surface condensation and fibrillation of α-Synuclein at physiologically relevant nanomolar concentrations in neurons, via a prewetting-like transition mechanism
- **Visible evidence base** In vitro reconstitution assays (ThT fluorescence, supported lipid bilayers, GUVs, Langmuir monolayers, micropipette aspiration), zeta potential measurements, cell culture experiments (HT22 cells, primary rat cortical neurons), fluorescence microscopy, FRAP, calcium imaging, and lattice-gas Monte Carlo simulations
- **Missing materials affecting confidence** Figures and supplementary figures referenced but not provided; source data files not available; statistical details for several experiments incomplete; no information on replicates for some key experiments; supplementary videos referenced but not viewable

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question regarding the role of membrane surfaces in α-Synuclein phase separation and aggregation. The combination of in vitro reconstitution, cell-based assays, and theoretical modeling is ambitious and potentially impactful. However, several technical concerns and gaps in the presented evidence limit the strength of the conclusions as currently stated. The claim that membrane interfacial potential "governs" condensation is supported by correlative data but lacks direct mechanistic manipulation of interfacial potential in most experiments. The physiological relevance of the findings, while suggested, requires stronger validation. The manuscript would benefit from additional controls, quantitative analyses, and clarification of experimental details.

- **Who would be interested in the results, and why** Researchers in the fields of neurodegeneration, protein aggregation, phase separation biology, and membrane biophysics would find these results of interest. The work bridges biophysical principles of surface condensation with cellular pathology of Parkinson's disease, potentially appealing to a broad readership interested in the molecular mechanisms of protein misfolding diseases and the role of membrane interfaces in cellular organization.

- **Major strengths**
  1. The study addresses a significant gap in understanding how membranes influence α-Synuclein phase behavior at physiologically relevant concentrations
  2. The combination of multiple experimental approaches (in vitro, cellular, computational) provides a multi-scale perspective
  3. The identification of a specific lipid stoichiometry (PC:PS 6:4) that promotes condensation is a notable finding
  4. The application of a lattice-gas model to explain surface condensation as a prewetting-like transition provides a theoretical framework
  5. The demonstration of depolarization-induced α-Synuclein condensation and release in primary neurons has potential translational relevance

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental evidence
- **Claim pointer** "membranous interfaces promote α-Synuclein condensation at physiologically relevant sub-critical concentrations (~10 nM) without crowding agents"
- **Evidence pointer** Figure 1j, Results section "Membrane composition dictates surface-mediated condensation of α-Syn at nanomolar concentrations"
- **Concern** The claim that condensation occurs at 10 nM α-Synuclein is based on fluorescence microscopy of labeled protein on supported lipid bilayers. However, the manuscript does not provide sufficient details on how condensation was distinguished from non-specific adsorption or protein aggregation artifacts. The use of Hilyte-488-labeled α-Synuclein at such low concentrations raises questions about the fraction of labeled versus unlabeled protein, potential effects of labeling on phase behavior, and whether the observed puncta represent true condensates versus surface-bound aggregates. Additionally, the threshold between 5 nM (no condensation) and 10 nM (condensation) appears to be based on a single concentration series without statistical validation.
- **Why it matters** The central claim of the paper rests on the observation of condensation at sub-critical concentrations. If this observation is an artifact of labeling, surface preparation, or imaging conditions, the entire premise of the study would be undermined.
- **Resolution test** Provide unlabeled protein validation experiments (e.g., label-free detection methods), demonstrate that condensation is reversible and concentration-dependent in a systematic manner, include statistical analysis across multiple independent experiments, and show that the labeled protein behaves identically to unlabeled protein in control experiments.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic evidence
- **Claim pointer** "Membrane interfacial potential governs surface condensation and fibrillation of α-Synuclein"
- **Evidence pointer** Figure 5a, Results section "Interfacial potential drives lipid stoichiometry-dependent surface condensation of α-Syn"
- **Concern** The manuscript establishes a correlation between zeta potential and condensation propensity across different lipid compositions, but does not directly manipulate interfacial potential to demonstrate causality. The zeta potential measurements are performed on vesicles, while the condensation experiments are performed on supported bilayers, which may have different surface properties. Additionally, the relationship between zeta potential and the actual interfacial potential experienced by α-Synuclein at the membrane surface is not rigorously established. The authors acknowledge this distinction but do not provide experimental approaches to directly test the role of interfacial potential, such as varying ionic strength systematically, using charged lipid analogs, or applying external electric fields.
- **Why it matters** The title and central thesis claim that interfacial potential "governs" the observed phenomena. Correlation alone, without causal manipulation, is insufficient to support this strong claim.
- **Resolution test** Perform experiments where interfacial potential is systematically varied (e.g., through ionic strength gradients, pH changes, or incorporation of charged lipids) while keeping lipid composition constant, and demonstrate that condensation correlates with the measured interfacial potential. Alternatively, use computational approaches to predict how changes in interfacial potential would affect condensation and test these predictions experimentally.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative analysis
- **Claim pointer** "condensates serve as nucleation sites for fibril formation, leading to membrane deformation and rupture"
- **Evidence pointer** Figure 2d, Results section "Membrane surface-induced condensation of α-Synuclein drives transition to fibrillar aggregates"
- **Concern** The transition from condensates to fibrils is described qualitatively, but quantitative evidence is lacking. The manuscript does not provide: (1) time-resolved measurements of fibril formation from condensates, (2) characterization of the fibrillar structures (e.g., electron microscopy, atomic force microscopy, or X-ray diffraction), (3) kinetic analysis of the liquid-to-solid transition, or (4) quantitative assessment of membrane deformation and rupture. The FRAP data (Figure 3) show reduced mobility over time but do not establish a direct link between condensate maturation and fibril formation.
- **Why it matters** The proposed mechanism linking surface condensation to fibrillation and membrane damage is a key aspect of the paper's significance for understanding neurodegeneration. Without rigorous characterization of the fibrillar species and the kinetics of the transition, this link remains speculative.
- **Resolution test** Provide electron microscopy images of fibrils emerging from condensates, perform thioflavin T binding assays on isolated condensates over time, quantify the kinetics of the liquid-to-solid transition using rheology or other biophysical methods, and use advanced imaging (e.g., cryo-electron tomography) to visualize membrane deformation at high resolution.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Physiological relevance
- **Claim pointer** "altering membrane interfacial potential via lipids in hippocampal neuronal cells alters preformed α-Synuclein condensate size" and "membrane depolarization drives α-Synuclein condensate formation and extracellular secretion in primary cortical neurons"
- **Evidence pointer** Figures 6 and 7, Results sections "Perturbing membrane interfacial potential via lipids in hippocampal neuronal cells alters preformed α-Synuclein condensate size" and "Membrane depolarization drives α-Synuclein condensate formation and extracellular secretion in primary cortical neurons"
- **Concern** While the cellular experiments are valuable, the physiological relevance of the findings requires stronger validation. The HT22 cell line is a hippocampal neuronal cell line, but its relevance to dopaminergic neurons affected in Parkinson's disease is limited. The primary cortical neuron experiments use overexpression of α-Synuclein, which may not reflect endogenous conditions. The concentrations of PS liposomes used (70-150 μM) are relatively high and may have non-specific effects on cell viability or membrane integrity. The manuscript does not address whether the observed effects are specific to α-Synuclein or would occur with other amyloidogenic proteins.
- **Why it matters** The translational implications of the study depend on the physiological relevance of the cellular models. Overexpression artifacts and non-physiological lipid concentrations could lead to conclusions that do not apply to disease conditions.
- **Resolution test** Validate key findings in dopaminergic neurons (e.g., midbrain cultures or iPSC-derived neurons), use endogenous α-Synuclein levels where possible, perform dose-response experiments with PS liposomes to establish specificity, and include control experiments with other amyloidogenic proteins or mutant α-Synuclein variants.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Theoretical model validation
- **Claim pointer** "A lattice gas model reveals this behavior as a prewetting-like transition, where an attractive membrane induces local phase separation below the bulk saturation concentration"
- **Evidence pointer** Figure 5b-f, Results section "Interfacial potential drives lipid stoichiometry-dependent surface condensation of α-Syn", Methods section "Model for surface condensation of α-synuclein on a lipid bilayer membrane"
- **Concern** The lattice-gas model is presented as supporting the prewetting transition interpretation, but the connection between model parameters and experimental conditions is not clearly established. The model parameters (Jp, Jm, Jt, Lt, φm, φt) are not directly measured or constrained by experimental data. The manuscript does not demonstrate that the model quantitatively reproduces the experimental observations, such as the concentration dependence of condensation or the specific lipid composition effects. The model appears to be used illustratively rather than as a quantitative predictive tool.
- **Why it matters** The prewetting transition interpretation is a central conceptual contribution of the paper. If the model is not quantitatively validated against experimental data, the interpretation remains speculative.
- **Resolution test** Fit the model parameters to experimental data, demonstrate that the model can predict condensation behavior for new lipid compositions or protein concentrations, and provide quantitative comparisons between model predictions and experimental measurements.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Experimental detail
- **Affected element** ThT fluorescence assay
- **Evidence pointer** Figure 1a, Methods section "Thioflavin T assay for the measurement of fibrillation kinetics of α-Synuclein"
- **Issue** The ThT assay uses 50 μM α-Synuclein, which is far above the concentrations used in the condensation experiments (10-100 nM). The relationship between the high-concentration fibrillation kinetics and the low-concentration surface condensation is not discussed.
- **Required correction** Clarify how the ThT fibrillation data relate to the surface condensation observations, or provide ThT data at lower concentrations in the presence of membranes.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Quantification of puncta
- **Evidence pointer** Figure 6d, Results section "Perturbing membrane interfacial potential via lipids in hippocampal neuronal cells alters preformed α-Synuclein condensate size"
- **Issue** The manuscript reports p-values for puncta size comparisons but does not specify the number of cells analyzed, the number of independent experiments, or the statistical test used for Figure 6d.
- **Required correction** Provide complete statistical details including sample sizes, number of independent replicates, and specific statistical tests used for all quantifications.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Control experiments
- **Affected element** PS liposome treatment
- **Evidence pointer** Figure 6, Methods section "Mammalian cell culture and treatment with monomeric α-Syn"
- **Issue** The manuscript does not report whether PS liposome treatment affects cell viability or membrane integrity, which could confound the interpretation of puncta size changes.
- **Required correction** Include cell viability assays (e.g., LDH release, MTT) and membrane integrity controls for the PS liposome treatments.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Model description
- **Affected element** Lattice-gas model
- **Evidence pointer** Methods section "Model for surface condensation of α-synuclein on a lipid bilayer membrane"
- **Issue** The model description is brief and lacks details on the simulation protocol, equilibration criteria, finite-size effects, and how the excess density is calculated from simulation trajectories.
- **Required correction** Provide a more detailed description of the simulation methodology, including system size, number of independent runs, error estimation, and convergence criteria.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion does not adequately contextualize the findings with respect to recent studies on surface-mediated phase separation of other proteins or the role of membranes in α-Synuclein aggregation.
- **Required correction** Expand the discussion to include relevant recent literature on membrane-mediated phase separation and α-Synuclein aggregation at membranes.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 1j
- **Evidence pointer** Figure 1j, Results section "Membrane composition dictates surface-mediated condensation of α-Syn at nanomolar concentrations"
- **Issue** The confocal images at 5 nM and 10 nM concentrations appear to have different contrast settings, making direct comparison difficult.
- **Required correction** Ensure consistent contrast and brightness settings across all images in the concentration series, or provide quantitative image analysis to support the qualitative observations.

## Risk / unsupported claims
- The claim that condensation occurs at 10 nM α-Synuclein is based on limited concentration points and lacks statistical validation across independent experiments
- The causal role of interfacial potential in governing condensation is not directly demonstrated; only correlative evidence is provided
- The transition from condensates to fibrils and subsequent membrane damage is described qualitatively without rigorous structural or kinetic characterization
- The physiological relevance of the findings to Parkinson's disease is suggested but not directly tested in disease-relevant models
- The lattice-gas model is used to support the prewetting transition interpretation but is not quantitatively validated against experimental data
- The relationship between zeta potential measurements on vesicles and the interfacial potential experienced by α-Synuclein on supported bilayers is not established
- The specificity of the observed effects to α-Synuclein (versus other amyloidogenic proteins) is not addressed
- The manuscript does not provide evidence that the observed membrane deformation and rupture occur in cellular contexts, only in vitro