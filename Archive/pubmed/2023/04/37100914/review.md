## Review setup
- **Input scope** Full manuscript text including abstract, main text, methods, and supplementary information descriptions.
- **Assessment boundary** Scientific content, technical soundness, methodological rigor, and support of claims based solely on the provided manuscript text. No external literature or unpublished data were consulted.
- **Shared manuscript claim summary** The authors present a method combining genetic code expansion, site-specific click labelling, and FLIM-FRET to measure intramolecular distance distributions of the FG domain of NUP98 within the nuclear pore complex (NPC) in permeabilized cells. They report a scaling exponent ν = 0.56 ± 0.03, indicating a "good solvent" environment in the NPC, contrasting with a collapsed state (ν = 0.29 ± 0.01) for isolated NUP98 in solution. Coarse-grained molecular dynamics simulations calibrated to these data suggest FG-NUPs form a dynamic, extended network near a critical interaction strength.
- **Visible evidence base** Abstract, main text, methods section, figure legends (Figs. 1, 2, 3, 4), extended data figure legends, supplementary information descriptions, and video descriptions.
- **Missing materials affecting confidence** The actual figures, extended data figures, and supplementary figures are not provided. The full supplementary text, including equations and detailed analysis protocols, is not available. The peer review file is not provided. This limits verification of data quality, statistical analysis, and simulation details.

## Reviewer
- **Overall assessment** This manuscript presents a technically ambitious and innovative approach to a long-standing problem in nuclear pore complex biology: the structural and dynamic characterization of the intrinsically disordered FG-NUP network that constitutes the permeability barrier. The combination of genetic code expansion, site-specific labelling, and quantitative FLIM-FRET is a significant methodological advance, and the integration with coarse-grained simulations provides a compelling framework for interpreting the experimental data. The central finding, that the NPC environment behaves as a "good solvent" leading to expanded FG domain conformations, is an important contribution that challenges or refines existing models. However, the strength of the conclusions depends critically on details of the data analysis, control experiments, and simulation parameterization that are not fully visible in the provided text. The manuscript is well-written and the logic is clear, but several technical aspects require careful scrutiny before the claims can be fully accepted.
- **Who would be interested in the results, and why** This work will be of high interest to researchers in the fields of nuclear transport, nucleoporin biology, intrinsically disordered proteins, and biophysics of cellular barriers. It provides the first in situ measurements of FG-NUP conformational properties within the functional NPC, which is a major goal in the field. The methodological approach, combining synthetic biology with advanced fluorescence techniques, will also appeal to researchers developing tools for studying protein conformation in living cells. The findings have implications for understanding the physical basis of nucleocytoplasmic transport selectivity and for models of IDP behavior in crowded, confined cellular environments.
- **Major strengths**
    1.  The methodological innovation is substantial. The combination of genetic code expansion with click chemistry for site-specific dual labelling of an IDP inside a cellular structure is a significant technical achievement.
    2.  The study addresses a critical and unresolved question: the conformational state of FG-NUPs in their native environment. The in situ measurements are a major step forward from in vitro studies.
    3.  The integration of experimental FRET data with coarse-grained simulations is a powerful approach, allowing the authors to build a plausible molecular model of the FG-NUP network that is constrained by experimental measurements.
    4.  The finding that the NPC environment is a "good solvent" and that FG-NUPs operate near a critical interaction strength is conceptually elegant and provides a new framework for understanding the permeability barrier.
    5.  The manuscript is clearly written and the logical flow from experimental design to data interpretation to modeling is easy to follow.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness / Data analysis
    - **Claim pointer** The authors claim to have measured the distance distribution for 18 labelled chain segments of NUP98 in the NPC using FLIM-FRET and extracted a scaling exponent ν = 0.56 ± 0.03.
    - **Evidence pointer** Main text, section "FLIM-FRET measurements of NUP98"; Figure 2e, 2f; Supplementary Figures 3-6; Methods section "FLIM-FRET for cell measurements".
    - **Concern** The accuracy of the derived scaling exponent depends entirely on the conversion of measured FRET efficiencies to absolute distances. This conversion requires precise knowledge of the Förster radius (R0), the orientation factor (κ²), and the assumption of a specific polymer model (Gaussian chain) for the distance distribution. The manuscript states that κ² is assumed to be 2/3 based on measured anisotropies, but the error analysis for this assumption and its impact on the final ν value is not fully detailed in the provided text. More critically, the use of a Gaussian chain model to interpret the FRET data is a strong assumption that could bias the derived ν. The authors mention a global fit to the Gaussian chain model, but the quality of these fits, the residuals, and the justification for this model over others (e.g., worm-like chain, self-avoiding walk) are not presented. The robustness of the derived ν to the choice of polymer model is a key question that is not addressed in the visible text.
    - **Why it matters** The central quantitative conclusion of the paper, the "good solvent" condition (ν > 0.5), rests on the accuracy of the distance distributions extracted from the FLIM-FRET data. If the analysis is biased by the model assumptions, the conclusion could be an artifact of the data processing rather than a true property of the system.
    - **Resolution test** The authors should provide a detailed analysis of the sensitivity of the derived ν to the choice of polymer model and to the uncertainty in R0 and κ². This could include fitting the data with alternative models and showing that the derived ν is robust, or providing a quantitative estimate of the systematic error. The quality of the global fits should be shown, including residuals and goodness-of-fit parameters.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness / Simulation methodology
    - **Claim pointer** The authors claim that coarse-grained MD simulations with an effective interaction strength of ε̃ = 0.42 reproduce the experimental FRET data and that this value is near the critical interaction strength for condensation, leading to a dynamic barrier.
    - **Evidence pointer** Main text, section "FG-NUP motions revealed by modelling"; Figure 4a; Supplementary Figures 9-13, 18; Methods section "MD simulation methods".
    - **Concern** The simulation results are highly sensitive to the parameterization of the coarse-grained model, particularly the effective interaction strength ε̃. The authors calibrated ε̃ = 0.44 to match in vitro condensate properties, but then had to adjust it to ε̃ = 0.42 to match the in situ FRET data. This is a very small change, and the manuscript does not clearly explain why the in vitro-derived parameter fails to predict the in situ behavior. The claim that the optimal value (0.42) is "nearly coincident" with the critical value (0.42) is presented as a key finding, but the precision of this coincidence is unclear. The critical value is likely dependent on the details of the simulation model (e.g., chain length, grafting density, box size), and the uncertainty in determining it is not reported. The manuscript also does not discuss whether other parameter sets (e.g., different ε̃_scaffold values) could also reproduce the experimental data.
    - **Why it matters** The conclusion that FG-NUPs operate near a critical point, leading to a highly dynamic barrier, is a major conceptual claim of the paper. If the simulation model is not robustly parameterized, or if the proximity to the critical point is not rigorously established, this conclusion is weakened.
    - **Resolution test** The authors should provide a more detailed analysis of the sensitivity of the simulation results to the model parameters. This could include a phase diagram showing how the system behavior (e.g., collapsed vs. extended) depends on ε̃ and ε̃_scaffold, and a clear demonstration that the experimental data uniquely point to a parameter set near the critical point. The uncertainty in the critical interaction strength should be quantified.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness / Experimental controls
    - **Claim pointer** The authors claim that the NPCs in permeabilized cells are functional and that the labelling is specific, based on transport assays and control experiments.
    - **Evidence pointer** Main text, section "In-cell site-specific labelling of NUP98"; Figure 1b; Extended Data Figures 1-3.
    - **Concern** The manuscript states that transport assays were performed to show functionality, but the details of these assays and the quantitative results are not provided in the visible text. The statement that "n = 3 experiments were repeated independently with the same conclusion" is insufficient to assess the robustness of the functional data. Furthermore, the potential for the labelling itself to perturb the structure or dynamics of the FG domain is a critical concern. The manuscript mentions that the dyes have a C5 flexible linker, but it does not discuss whether the bulky dye molecules could alter the conformational preferences of the FG domain, especially in the crowded environment of the NPC. The control experiments for labelling specificity (e.g., Western blots, mass spectrometry) are not described in detail.
    - **Why it matters** The validity of the in situ measurements depends on the assumption that the labelled NUP98 is functional and that the dye labels do not significantly perturb the system. If the labelling perturbs the FG domain, the measured distances may not reflect the native state.
    - **Resolution test** The authors should provide more detailed data on the functionality of the labelled NPCs, including quantitative results from the transport assays. They should also discuss and, if possible, provide evidence that the dye labels do not significantly alter the conformational properties of the FG domain, for example by comparing the in vitro behavior of labelled and unlabelled protein.

    - **Concern ID** R1-M4
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific importance / Generalizability
    - **Claim pointer** The authors claim that their approach "opens a window into resolving disorder-function relationships of IDPs in situ" and can be applied generally to other IDPs.
    - **Evidence pointer** Abstract; Main text, section "Discussion".
    - **Concern** While the methodological advance is significant, the generalizability of the approach to other IDPs is not fully demonstrated. The success of the method relies on the ability to genetically encode non-canonical amino acids at specific sites in the target protein, which may not be straightforward for all IDPs. Furthermore, the requirement for the target protein to be present in a sufficiently high local concentration (as in the NPC) for FLIM-FRET measurements may limit its application to other, less abundant IDPs. The manuscript does not discuss these potential limitations in detail.
    - **Why it matters** The broader impact of the work, beyond the specific case of NUP98, depends on the generalizability of the method. If the approach is limited to a small subset of IDPs, its significance is reduced.
    - **Resolution test** The authors should provide a more balanced discussion of the potential and limitations of their approach for studying other IDPs, addressing issues of labelling efficiency, protein abundance, and the need for specialized equipment.

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity / Reproducibility
    - **Affected element** Methods section, "MD simulation methods"
    - **Evidence pointer** Methods section, "MD simulation methods".
    - **Issue** The description of the coarse-grained model is brief. The exact form of the non-bonded interaction potential, the mapping of amino acids to beads, and the treatment of the scaffold are not fully specified in the provided text.
    - **Required correction** The authors should provide a more detailed description of the model, including the functional form of all interaction potentials, the parameters used, and the method for mapping the NUP98 sequence to the coarse-grained beads. This is essential for reproducibility.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Clarity / Data presentation
    - **Affected element** Figure 2f
    - **Evidence pointer** Figure 2f legend.
    - **Issue** The phasor plot in Figure 2f is described as showing data on a single-cell basis, but the number of cells and the statistical treatment of the phasor coordinates are not described.
    - **Required correction** The authors should clarify how the phasor points are calculated and displayed, and whether the spread in the phasor plot represents cell-to-cell variability or measurement noise.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Technical soundness / Data analysis
    - **Affected element** Main text, section "FG-NUP motions revealed by modelling"
    - **Evidence pointer** Main text, section "FG-NUP motions revealed by modelling".
    - **Issue** The manuscript states that the model was "parameterized" using in vitro condensate data, but the specific experimental data used for this parameterization are not described.
    - **Required correction** The authors should specify which experimental measurements (e.g., condensate density, surface tension) were used to determine the interaction strength ε̃ = 0.44.

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Clarity / Terminology
    - **Affected element** Main text, section "Extracting chain dimensions of NUP98"
    - **Evidence pointer** Main text, section "Extracting chain dimensions of NUP98".
    - **Issue** The term "good solvent" is used to describe the environment inside the NPC. While this is a useful analogy, it may be misleading, as the "solvent" inside the NPC is not a simple liquid but a complex, crowded environment of other FG-NUPs, scaffold proteins, and potentially other macromolecules.
    - **Required correction** The authors should briefly clarify that "good solvent" is an operational term from polymer physics, referring to conditions where polymer-solvent interactions are favored, and that in the NPC context, this is an effective description of the environment.

## Risk / unsupported claims
- The claim that the NPC environment provides a "good solvent" condition is supported by the derived scaling exponent, but this is dependent on the model-based analysis of the FRET data, which is not fully visible.
- The claim that FG-NUPs operate near a critical interaction strength is based on the simulation results, but the robustness of this finding to model parameterization is not fully demonstrated.
- The claim that the approach can be generally applied to study other IDPs is a reasonable extrapolation but is not directly supported by data in the manuscript.
- The claim that the "disordered nuclear transport machinery" is "visualized" is somewhat overstated. The study measures ensemble-averaged distance distributions, not direct visualization of individual conformations.