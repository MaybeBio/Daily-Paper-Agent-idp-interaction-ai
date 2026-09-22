## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, materials and methods, computational methods, and supplementary figure references.
- **Assessment boundary** Scientific content, methodological rigor, internal consistency, and support of claims by presented evidence. No assessment of editorial fit or publication decision.
- **Shared manuscript claim summary** The authors report that phosphomimetic substitutions at TDP-43 LCD C-terminal residues S403/S404/S409/S410 alter the salt dependence of liquid-liquid phase separation from monotonic to biphasic. They propose a mechanism in which long-range attractive electrostatic interactions, arising from a polarized charge distribution, modulate short-range hydrophobic interactions that drive phase separation.
- **Visible evidence base** Turbidity measurements, fluorescence microscopy, far-UV CD spectroscopy, coarse-grained simulations, and pairwise force analysis from simulations.
- **Missing materials affecting confidence** Supplementary figures and tables (Figures S1-S5, Tables S1-S2) referenced in the text but not provided. Raw data and statistical analysis details for turbidity and microscopy experiments not included. Simulation parameter files and analysis scripts not directly inspectable.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant question regarding the impact of pathologically relevant C-terminal phosphorylation on TDP-43 LCD phase separation. The experimental observation of a biphasic salt dependence in phosphomimetic variants is novel and potentially important. However, the mechanistic interpretation relies heavily on coarse-grained simulations with a parameter adjustment that may introduce circularity, and the experimental validation of the proposed mechanism is incomplete. The claim that electrostatic forces "tune" hydrophobic interactions is plausible but not definitively established by the presented evidence.
- **Who would be interested in the results, and why** Researchers studying TDP-43 biology, liquid-liquid phase separation mechanisms, and the molecular basis of neurodegenerative proteinopathies. The work may also interest computational biophysicists developing coarse-grained models of phase-separating systems.
- **Major strengths** The study addresses a clinically relevant question with a combination of experimental and computational approaches. The observation of a biphasic salt response in phosphomimetic variants is unexpected and well-documented across multiple experimental readouts. The pairwise force analysis provides a detailed mechanistic picture that goes beyond simple phenomenological descriptions.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (simulation parameter adjustment), R1-M2 (mechanistic claim support), R1-M3 (quantitative validation).
- **Assessment against Nature-style criteria** Originality: The finding of a biphasic salt dependence in phosphomimetic TDP-43 LCD is novel and not previously reported. Scientific importance: The work has potential significance for understanding how disease-associated phosphorylation may alter TDP-43 phase behavior, though the physiological relevance of the phosphomimetic model requires further validation. Interdisciplinary readership: The topic bridges biophysics, cell biology, and neurodegeneration, and should appeal to a broad audience. Technical soundness: The experimental methods are standard and appropriate, but the simulation approach contains a parameter adjustment that requires justification. Readability for nonspecialists: The manuscript is generally well-written and accessible, though the simulation methodology may be challenging for experimental readers.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the simulation parameter adjustment and the directness of the mechanistic evidence.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the biphasic salt dependence of phosphomimetic TDP-43 LCD LLPS is recapitulated by their coarse-grained simulations, and that this arises from a specific mechanism involving electrostatic modulation of hydrophobic interactions.
- **Evidence pointer** Computational Methods, Figure 2c, Figure S1
- **Concern** The simulation model incorporates an explicit salt-dependent adjustment of the Lennard-Jones well depth (epsilon), which is tuned so that simulated phase diagrams match experimental results at 0 and 1250 mM NaCl. This parameterization may introduce circularity: the model is adjusted to reproduce the experimental phenomenon, and then used to explain the mechanism of that same phenomenon. The authors should clarify whether the salt-dependent epsilon adjustment is independently justified by physical principles or experimental data, or whether it is a fitting parameter. If it is a fitting parameter, the mechanistic conclusions drawn from the simulations are substantially weakened.
- **Why it matters** The central mechanistic claim of the paper depends on the simulations. If the key parameter is adjusted to force agreement with experiment, the simulations cannot independently validate the proposed mechanism.
- **Resolution test** Provide independent justification for the salt-dependent epsilon values, or demonstrate that the qualitative conclusions are robust to reasonable variations in the epsilon parameterization. Alternatively, perform simulations with a fixed epsilon and show that the biphasic behavior still emerges from electrostatic interactions alone.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The authors propose that attractive electrostatic interactions between N- and C-terminal regions of phosphomimetic TDP-43 bring monomers together, thereby promoting hydrophobic interactions that drive phase separation.
- **Evidence pointer** Figures 3-6, Discussion
- **Concern** The pairwise force analysis is performed exclusively in silico. The experimental evidence that electrostatic interactions play a modulatory role in the phosphomimetic variants is indirect. The authors do not experimentally test the proposed mechanism, for example by mutating charged residues to disrupt the proposed attractive electrostatic interactions, or by varying pH to alter charge states. The claim that electrostatic forces "tune" hydrophobic interactions would be strengthened by direct experimental manipulation of electrostatic interactions.
- **Why it matters** The proposed mechanism is the central conceptual advance of the paper. Without experimental validation, the mechanism remains a simulation-based hypothesis.
- **Resolution test** Provide experimental data testing the role of electrostatic interactions, such as phase separation assays with charge-altering mutations or at different pH values, that would confirm or refute the proposed mechanism.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative rigor
- **Claim pointer** The authors state that the simulated phase diagrams match the qualitative features of the experimental diagrams, with only minor quantitative differences.
- **Evidence pointer** Figure 2b,c, Computational Methods
- **Concern** The comparison between simulated and experimental phase diagrams is presented qualitatively. No quantitative metrics are provided to assess the agreement between simulation and experiment. Additionally, the saturation concentrations (c_sat) are determined from turbidity measurements, but the statistical uncertainty in these values is not reported. The authors should provide quantitative measures of agreement and uncertainty.
- **Why it matters** Quantitative rigor is essential for establishing the validity of the simulation model and the reliability of the experimental measurements.
- **Resolution test** Provide quantitative comparison metrics (e.g., root-mean-square deviation between simulated and experimental phase boundaries) and report confidence intervals or standard deviations for c_sat values.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1c
- **Evidence pointer** Figure 1c
- **Issue** The authors state that droplets formed by 4-PM TDP-43 LCD were much smaller than those formed by other proteins, but no quantitative analysis of droplet size is provided.
- **Required correction** Provide quantitative droplet size measurements or a representative image with scale bars and statistical analysis.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods
- **Evidence pointer** Materials and Methods, Turbidity measurements
- **Issue** The turbidity measurements are described as being performed at 25°C, but no information is provided about the time course of measurements or whether equilibrium was reached.
- **Required correction** Specify the time point at which turbidity was measured and provide evidence that measurements reflect equilibrium conditions.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion, paragraph 2
- **Issue** The authors discuss the potential physiological relevance of their findings but do not address the limitation that phosphomimetic substitutions may not fully recapitulate the effects of authentic phosphorylation, which they acknowledge only briefly.
- **Required correction** Expand the discussion of the limitations of the phosphomimetic approach and its implications for interpreting the physiological relevance of the findings.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Computational Methods
- **Evidence pointer** Computational Methods, Simulation framework
- **Issue** The simulation methodology references a GitHub repository, but the specific version of the code and input parameters used for the reported results are not specified.
- **Required correction** Provide a version identifier or DOI for the code repository, and include input parameter files as supplementary material.

## Risk / unsupported claims
- The claim that the biphasic salt dependence of phosphomimetic TDP-43 LCD LLPS is mechanistically explained by electrostatic modulation of hydrophobic interactions is not fully supported, as it relies on simulations with a potentially circular parameter adjustment and lacks direct experimental validation.
- The claim that the coarse-grained simulations "recapitulate" the experimental phase diagrams is only qualitatively supported; no quantitative comparison is provided.
- The statement that "the droplets formed by 4-PM TDP-43 LCD were also much smaller than those formed by the other proteins" is not quantitatively supported.
- The physiological relevance of the findings, discussed in the final paragraph, is speculative and not directly tested.