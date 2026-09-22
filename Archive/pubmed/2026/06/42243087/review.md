## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and figure legends
- **Assessment boundary** Scientific validity, technical soundness, and significance of the structural and dynamic characterization of the β-cardiac myosin auto-inhibited state
- **Shared manuscript claim summary** The authors integrate cryo-EM and all-atom MD simulations to characterize the conformational dynamics of the β-cardiac myosin Interacting-Heads Motif (CarIHM), showing that the DCM mutation E525K stabilizes the off-state by restricting S2 coiled-coil flexibility, while the HCM mutation E903K destabilizes it. They further model CarIHM docking in the thick filament and propose a mechanism for RLC phosphorylation-dependent regulation.
- **Visible evidence base** Cryo-EM structures of WT and E525K CarIHM at 3.6–3.8 Å and 3.02 Å resolution respectively; 3DFlex and 3DVA analyses; all-atom MD simulations of isolated CarIHM (135 ns) and thick filament (140 ns); refined model of the human cardiac relaxed thick filament; ClinVar variant analysis
- **Missing materials affecting confidence** Supplementary figures, tables, videos, and data files referenced but not provided; no experimental validation of MD predictions (e.g., mutagenesis, functional assays); no statistical analysis of MD replicates beyond qualitative description; no raw cryo-EM validation metrics (FSC curves, directional resolution) in main text

## Reviewer

- **Overall assessment** This manuscript presents a technically impressive integration of high-resolution cryo-EM with all-atom MD simulations to address the dynamic nature of the cardiac myosin off-state. The structural data are of high quality, and the identification of distinct conformational clusters at the S2/BH interface provides a plausible framework for understanding how mutations in different regions can have opposing effects on CarIHM stability. However, the central claims regarding the pathogenic mechanism of E525K and the role of Cluster 3 in thick filament docking rest heavily on MD simulations that are relatively short (135–140 ns) and lack experimental validation. The manuscript would be strengthened by functional assays or longer-timescale simulations to support the proposed equilibrium shifts. The thick filament model, while improved, is built on a 6 Å map and the interpretation of specific side-chain interactions should be tempered accordingly.

- **Who would be interested in the results, and why** Structural biologists studying muscle proteins and macromolecular complexes; cardiovascular researchers investigating the molecular basis of cardiomyopathies; computational biologists interested in integrating cryo-EM with MD simulations; pharmaceutical scientists developing myosin modulators for cardiac diseases. The work provides a framework for interpreting the pathogenicity of MYH7 variants and could inform drug development targeting the myosin off-state.

- **Major strengths** 
  1. High-resolution cryo-EM structures of WT CarIHM in two conformations and E525K mutant, representing a significant technical achievement given the known flexibility of this complex
  2. The integration of 3DFlex analysis with MD simulations to describe conformational ensembles rather than static structures is methodologically innovative
  3. The identification of Cluster 3 as a dynamic interface involving FHLoop-2 and FHHCM-loop provides new mechanistic insight into CarIHM regulation
  4. The refined thick filament model with improved correlation coefficient (72% vs 60%) represents a useful resource for the field
  5. The clinical correlation with ClinVar data adds translational relevance

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** "The DCM-causing mutation E525K greatly stabilizes CarIHM" and "E525K strongly biases the conformational ensemble to enrich it in conformations close to WTConfA"
- **Evidence pointer** Figure 1C–E, Figure 2H–I, Supplementary Videos 1 and 3
- **Concern** The central claim that E525K stabilizes CarIHM is based primarily on the observation that only one conformation was observed in cryo-EM for the mutant, whereas two were observed for WT. However, the authors do not provide quantitative measures of conformational distribution or occupancy. The MD simulations (135 ns) are relatively short for drawing conclusions about equilibrium shifts, and only two replicates were performed. The claim that E525K "greatly stabilizes" the off-state is not supported by quantitative free energy calculations or experimental measurements of off-state stability (e.g., equilibrium constants from solution studies).
- **Why it matters** The pathogenic mechanism proposed for E525K rests on this stabilization claim. If the stabilization is not robustly demonstrated, the mechanistic interpretation of DCM pathogenesis is weakened. The distinction between "stabilization" and "reduced conformational sampling" is important for understanding how the mutation affects myosin function.
- **Resolution test** Provide quantitative analysis of conformational populations from cryo-EM (e.g., 3DVA occupancy analysis), longer MD simulations (≥500 ns) with multiple replicates, or experimental validation using techniques such as hydrogen-deuterium exchange, limited proteolysis, or single-molecule FRET to directly measure off-state stability differences between WT and E525K.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Molecular dynamics simulations based on high quality CryoEM maps provide predictions on CarIHM stability" and "the MD simulations can predict the opposite effects on the stability of CarIHM structure depending on the presence of distinct missense mutations"
- **Evidence pointer** Figure 2H–I, Supplementary Figure 9, Supplementary Videos 5 and 6
- **Concern** The MD simulations are used to make strong claims about the differential effects of E525K (stabilizing) and E903K (destabilizing) on CarIHM. However, the simulations are only 135 ns, which is likely insufficient to capture the full conformational landscape of such a large and dynamic complex. The RMSD and RMSF differences between conditions are described qualitatively without statistical testing. The choice of starting from WTConfA for both mutants may bias the simulations, and no equilibration validation is shown. The force field parameters and protonation states are not discussed in sufficient detail.
- **Why it matters** The predictive power of the MD simulations is a key pillar of the manuscript's claims. If the simulations are not sufficiently converged or statistically robust, the conclusions about mutation effects on CarIHM stability are not reliable. This is particularly important given that the authors use these predictions to explain clinical phenotypes.
- **Resolution test** Provide convergence analysis (e.g., block averaging, multiple independent runs with different initial velocities), extended simulation times (≥500 ns), free energy perturbation or umbrella sampling calculations to quantify binding free energy differences, and statistical comparison of RMSD/RMSF distributions between conditions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Evidence strength
- **Claim pointer** "We next performed all-atom MD calculations using the refined model of the thick filament to evaluate the stability of the interfaces and the dynamics of the crowns in their physiological context" and "The crowns are thus docked using several dynamic interfaces with the thick filament involving mainly their FH motor domains"
- **Evidence pointer** Figure 5, Figure 6, Figure 7, Supplementary Table 4, Supplementary Videos 11–15
- **Concern** The thick filament model is built on a 6 Å cryo-EM map (EMDB-29734), which limits the confidence in specific side-chain interactions. The authors claim to have improved the model (correlation coefficient 72% vs 60%), but the resolution is still insufficient to validate the detailed atomic interactions they describe. The MD simulations of the filament (140 ns) are short for a system of this size, and the interpretation of specific contacts (e.g., R9-E179, S15-E88) as functionally significant may be overinterpreted given the resolution limitations.
- **Why it matters** The claims about how CarIHM docks in different crown environments and how phosphorylation affects this docking are based on this model. If the model is not sufficiently accurate, the proposed regulatory mechanisms may be incorrect. The distinction between genuine interactions and artifacts of model building at 6 Å resolution is critical.
- **Resolution test** Validate key interactions with higher-resolution data (e.g., focused refinement of the crown regions), cross-validate with cross-linking mass spectrometry, or use complementary techniques such as hydrogen-deuterium exchange to confirm the proposed interfaces. Alternatively, temper the claims about specific side-chain interactions and focus on the overall architecture.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** "The transient nature of these interactions, combined with the flexibility of FHLoop-2, makes it possible to maintain the global interface despite changes in the orientation of S2"
- **Evidence pointer** Figure 3, Supplementary Figure 10, Supplementary Videos 7 and 8
- **Concern** The identification of Cluster 3 is based on a subset of particles from 3D classification (8 classes from 416k particles). The authors state that Cluster 3 is "highly dynamic" but do not provide quantitative measures of the occupancy or stability of this interface across the different classes. The distinction between genuine conformational states and classification artifacts is not fully addressed. The MD simulations predict Cluster 3 formation, but the timescale of formation and the frequency of these interactions are not quantified.
- **Why it matters** Cluster 3 is presented as a novel finding with implications for understanding how mutations in this region cause disease. If the evidence for this interface is not robust, the conclusions about its functional importance are weakened. The dynamic nature of this interface is central to the proposed model of CarIHM regulation.
- **Resolution test** Provide quantitative occupancy analysis of Cluster 3 across the 8 classes, validate with independent cryo-EM datasets or different classification strategies, and provide quantitative measures of interaction frequency and duration from MD simulations.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, last sentence
- **Issue** The abstract states "facilitates predictions of the effects of genetic variants in inherited cardiomyopathies" but does not specify the predictive accuracy or provide examples. This overstates the current capability.
- **Required correction** Qualify the statement to indicate that the framework provides a basis for generating testable predictions, rather than implying validated predictive power.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, MD simulations
- **Evidence pointer** Methods section, "General parameters used for all-atom molecular dynamics"
- **Issue** The methods state that 500 ps NVT equilibration was performed, but no details are given about the equilibration protocol (e.g., temperature coupling scheme, pressure coupling during equilibration, any prior energy minimization steps). The production run parameters are also not fully described (e.g., barostat coupling constants, thermostat coupling constants).
- **Required correction** Provide complete simulation parameters including energy minimization protocol, equilibration steps, thermostat and barostat settings, and any restraints applied during equilibration.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Figure 2H–I
- **Evidence pointer** Figure 2H–I
- **Issue** The distance plots (525Cα-903Cα) are shown for three conditions, but the number of replicates and the variability between replicates are not shown. The reader cannot assess the reproducibility of the MD results from the figure alone.
- **Required correction** Show individual replicate traces or error bars/confidence intervals for the distance measurements, and state the number of replicates in the figure legend.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion, RLC phosphorylation
- **Evidence pointer** Discussion, paragraph 4
- **Issue** The proposed mechanism for RLC phosphorylation-dependent destabilization is speculative and not directly tested. The statement "we propose a mechanism by which RLC phosphorylation could further destabilize the off state" is presented without experimental evidence.
- **Required correction** Clearly label this as a hypothesis and suggest specific experiments that could test it, or soften the language to indicate this is a speculative proposal.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Evidence strength
- **Affected element** Results, "Cardiomyopathy-causing mutations in the context of the filament"
- **Evidence pointer** Supplementary Table 5
- **Issue** The analysis of cardiomyopathy mutations relies on ClinVar classifications, but the authors do not discuss the limitations of ClinVar data, including potential misclassification or lack of functional validation for many variants.
- **Required correction** Acknowledge the limitations of ClinVar-based analysis and consider cross-referencing with other databases or functional studies where available.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1
- **Evidence pointer** Figure 1B
- **Issue** The description of the ~20° twist in S2 position between WTConfA and WTConfB is not clearly illustrated in the figure. The reader cannot easily visualize this difference from the provided figure.
- **Required correction** Add a clearer representation of the S2 twist, possibly with an inset or a separate panel showing the two conformations overlaid with the twist angle indicated.

## Risk / unsupported claims
- The claim that E525K "greatly stabilizes" CarIHM is not quantitatively supported; only qualitative cryo-EM observations and short MD simulations are provided.
- The claim that MD simulations can "predict" the effects of mutations on CarIHM stability is overstated given the short simulation times and lack of statistical validation.
- The specific side-chain interactions proposed in the thick filament model (e.g., R9-E179, S15-E88) are based on a 6 Å map and should be considered tentative.
- The statement that "the transient nature of these interactions... enables rapid activation/deactivation of the heads" is a functional inference not directly tested in this study.
- The proposed mechanism for RLC phosphorylation-dependent regulation is speculative and not experimentally validated.
- The claim that the refined thick filament model "represents a significant advance required to evaluate how mutations may impact relaxation" is not directly demonstrated; no functional validation is provided.
- The assertion that "24% of WT-IHM adopt the off-state on our grids" is presented as comparable to SRX measurements, but the relationship between cryo-EM particle populations and physiological off-state occupancy is not established.