## Review setup
- **Input scope** Full manuscript text including summary, results, discussion, methods, and supplemental figure legends
- **Assessment boundary** Scientific soundness, methodological rigor, validity of claims relative to evidence presented, and alignment with Nature-style criteria
- **Shared manuscript claim summary** The authors use coarse-grained molecular dynamics simulations with the HPS-Urry model to identify residues driving liquid-liquid phase separation (LLPS) of the plant RNA-binding protein PARCL. They predict that tyrosine residues in the prion-like domain are key drivers of phase separation, validate this by showing that a PARCL mutant with six tyrosines mutated to glutamic acid disrupts condensation in silico, in vitro, and in vivo, and further show that a C-terminal serine mutant reduces RNA binding without affecting phase separation, suggesting independent functional domains.
- **Visible evidence base** Full text with results sections, figures (Figures 1–8), tables (Table 1), supplemental figure legends (Figures S1–S6), methods, and data availability statements
- **Missing materials affecting confidence** Actual figure images, supplemental figures, raw simulation trajectories, experimental images, statistical analysis details, and sequence information for PARCL and mutants

## Reviewer

- **Overall assessment** This manuscript presents a potentially valuable computational framework for guiding targeted engineering of phase-separating proteins, using PARCL as a case study. The integration of coarse-grained simulations with in vitro and in vivo validation is commendable and addresses an important gap in the field. However, several technical concerns regarding simulation methodology, quantitative rigor, and the strength of some claims relative to the evidence presented need to be addressed before the case is fully established. The work is likely of interest to researchers studying biomolecular condensates, RNA-binding proteins, and computational protein design, but the current evidence base has limitations that temper enthusiasm.

- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation and biomolecular condensates, particularly those interested in computational prediction of phase behavior and rational protein engineering. The plant biology community may also be interested given the phloem-specific context of PARCL. Additionally, method developers in coarse-grained molecular dynamics simulations and those interested in RNA-protein interactions would find the framework relevant.

- **Major strengths** The study addresses a timely and important question: whether coarse-grained simulations can guide targeted engineering of phase-separating proteins. The use of multiple simulation models (HPS-Urry, Tesei, HPS-FB) to cross-validate contact predictions strengthens the computational approach. The combination of in silico, in vitro, and in vivo validation is a significant strength, as many computational predictions are never experimentally tested. The demonstration that phase separation and RNA binding can be independently manipulated is biologically interesting and potentially useful for engineering applications.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of simulation methodology
- **Claim pointer** The authors claim that coarse-grained MD simulations can successfully reproduce condensate formation of PARCL and that the HPS-Urry model provides reliable predictions of phase separation behavior.
- **Evidence pointer** Results section "Phase separation of eYFP-PARCL can be attributed to PARCL", Figure 2, Methods section "Building and running CG MD simulations"
- **Concern** The simulation methodology has several potential issues that are not adequately addressed. First, the protein concentration in simulations (3.4 mM) is stated to be much higher than the 10 μM used in vitro, yet the authors do not explain how this concentration difference affects the comparability of results. Second, the authors note that eYFP-PARCL simulations failed to maintain stable slabs, rendering results inconclusive, but they do not provide a satisfactory explanation for this discrepancy beyond speculating about force field limitations. Third, the simulation time of 100 ns may be insufficient to capture equilibrium phase behavior, particularly for systems with slow dynamics. The authors state simulations were "checked for convergence and extended where necessary" but provide no quantitative convergence criteria or details on which simulations required extension.
- **Why it matters** The central claim of the paper is that simulations can guide engineering of phase separation. If the simulation methodology has unaddressed limitations, particularly regarding concentration effects, force field accuracy, and equilibration, the reliability of the predictions is uncertain. The inability to simulate the actual experimental construct (eYFP-PARCL) is a significant gap that undermines the direct comparability between simulation and experiment.
- **Resolution test** Provide quantitative convergence metrics (e.g., density profiles over time, block averaging), justify the concentration choice and its relationship to experimental conditions, and either improve the eYFP-PARCL simulations or explicitly discuss the limitations this imposes on the conclusions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Strength of experimental validation
- **Claim pointer** The authors claim that the PARCLPLD Y−E mutant (six tyrosines mutated to glutamic acid) prevents condensate formation in vitro and in vivo, validating the simulation predictions.
- **Evidence pointer** Results section "Targeted engineering of PARCL validates the predicted phase separation behavior", Figure 4
- **Concern** The experimental validation is presented qualitatively. The in vitro data show "single aggregates or protein precipitate" for the mutant, which the authors distinguish from the "typical spherical appearance" of condensates. However, no quantitative analysis is provided, such as turbidity measurements, counting of droplets, size distributions, or fluorescence recovery after photobleaching (FRAP) to demonstrate liquid-like properties. The in vivo data similarly rely on visual inspection. Additionally, the authors state that crowding agents were used in experiments but not in simulations, yet they do not discuss how this methodological difference might affect the comparison. The claim that the mutant "prevents" condensate formation is strong, but the evidence appears to show altered aggregation behavior rather than complete prevention.
- **Why it matters** The validation of computational predictions with experimental data is the core strength of this paper. If the experimental characterization is not quantitative and does not rigorously distinguish between different types of aggregates (liquid droplets vs. solid aggregates vs. amorphous precipitates), the conclusions about successful prediction are weakened. The distinction between "no phase separation" and "different phase separation behavior" is critical for the claims made.
- **Resolution test** Provide quantitative in vitro data (e.g., turbidity assays, droplet counts, size distributions, FRAP measurements) and quantitative in vivo analysis (e.g., number of condensates per cell, size distributions) for both wild-type and mutant proteins. Clarify whether the mutant forms no condensates or forms non-liquid aggregates.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** RNA binding experiments
- **Claim pointer** The authors claim that simulations of PARCL with miRNA identified a short C-terminal region rich in arginine, histidine, and lysine as the RNA binding site, and that this is consistent with experimental data.
- **Evidence pointer** Results section "Simulations of miRNA-PARCL interactions align with experiments in both the RNA interaction site and phase separation behavior", Figure 6, Table 1
- **Concern** The RNA binding experiments are referenced from previous work (Ostendorp et al. 37), but no new experimental validation of the RNA binding site prediction is presented in this manuscript. The simulation results showing reduced RNA binding for the C-terminal serine mutant are compared to "experimental data" but the experimental data are not shown or described in sufficient detail. The claim that "phase separation and RNA binding can be independently targeted" relies on comparing simulation predictions with previously published experimental results, but the current manuscript does not provide direct experimental evidence for this independence.
- **Why it matters** The claim of independent manipulation of phase separation and RNA binding is a key finding with potential applications. However, if this claim relies primarily on simulation predictions compared to previously published data, rather than new experiments in this manuscript, the strength of the evidence is reduced. The manuscript would be strengthened by including the relevant experimental data or clearly stating the reliance on prior work.
- **Resolution test** Include the relevant experimental RNA binding data in this manuscript, or clearly state that the comparison is between new simulations and previously published experimental results, and discuss the limitations of this approach.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the framework
- **Claim pointer** The authors claim that the workflow presented "may be of general applicability for targeted engineering of condensate formation and protein-RNA interactions."
- **Evidence pointer** Discussion section
- **Concern** The generalizability claim is based on a single protein case study. While the framework is interesting, the authors do not test it on additional proteins or discuss potential limitations for other systems. Different proteins may have different phase separation mechanisms (e.g., charge-charge interactions vs. hydrophobic interactions vs. pi-pi stacking), and the HPS-Urry model may not be equally accurate for all of these. The claim of general applicability is therefore not well supported by the evidence presented.
- **Why it matters** The broader impact of this work depends on its generalizability. If the framework only works for proteins with similar sequence features to PARCL, the significance is reduced. The authors should either provide evidence of generalizability or temper their claims.
- **Resolution test** Either test the framework on additional proteins with different sequence features, or revise the generalizability claim to be more modest and discuss potential limitations.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure presentation
- **Affected element** Figure 2
- **Evidence pointer** Figure 2
- **Issue** The figure legend mentions panels A–G, but the text refers to "Figures 2D–2F and 2G" in a way that is slightly confusing. Additionally, the rendering of simulation results in panels A–C would benefit from scale bars or size indicators to help readers understand the scale of the simulated systems.
- **Required correction** Clarify the figure panel references in the text and add scale information to the simulation renderings.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** Table 1
- **Evidence pointer** Table 1
- **Issue** Table 1 reports average interactions per frame but provides no error estimates or information on variability across simulation replicates. It is unclear whether the differences between wild-type and mutant are statistically significant.
- **Required correction** Provide standard deviations or confidence intervals for the interaction counts, and state whether simulations were replicated.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Throughout
- **Evidence pointer** Throughout
- **Issue** The terms "condensate," "droplet," and "cluster" are used somewhat interchangeably. The authors should define these terms and use them consistently, particularly when distinguishing between liquid-like condensates and other types of aggregates.
- **Required correction** Define terminology at first use and use consistently throughout.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data and code availability section
- **Evidence pointer** Data and code availability section
- **Issue** The authors state that "all raw data are available on request from the lead contact" but do not provide a persistent repository for the experimental data. The simulation input files are provided on GitHub, but the trajectory data and analysis scripts are not fully described.
- **Required correction** Consider depositing experimental data in a persistent repository and providing more detailed documentation of analysis scripts.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 5
- **Evidence pointer** Figure 5
- **Issue** The figure combines a point plot with a chart indicating which residues are mutated. The relationship between the two panels could be made clearer, and the color scheme for the mutation chart could be more intuitive.
- **Required correction** Improve the visual connection between the point plot and the mutation chart, and consider using a more intuitive color scheme.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The limitations section is brief and focuses primarily on force field choices. Other limitations, such as the lack of quantitative experimental validation, the concentration mismatch between simulations and experiments, and the reliance on previously published RNA binding data, are not discussed.
- **Required correction** Expand the limitations section to address these additional concerns.

- **Technical failings that need to be addressed before the case is established** R1-M1 (simulation methodology details), R1-M2 (quantitative experimental validation), and R1-M3 (RNA binding evidence) are the primary technical issues that need to be addressed. The lack of quantitative convergence criteria, the qualitative nature of the experimental validation, and the reliance on previously published data for RNA binding are the most significant gaps.

- **Assessment against Nature-style criteria** 
  - **Originality**: The application of coarse-grained MD simulations with contact analysis to guide targeted engineering of phase-separating proteins is a novel approach. While individual components (coarse-grained simulations, contact analysis, mutagenesis) are established, their integration into a predictive framework for protein engineering is original.
  - **Scientific importance**: The ability to predict and control phase separation behavior has significant implications for understanding condensate biology and for engineering proteins with desired phase properties. The demonstration that phase separation and RNA binding can be independently manipulated is potentially important.
  - **Interdisciplinary readership**: The work bridges computational biophysics, molecular biology, and plant biology, and would appeal to researchers in these fields. The methods and findings are likely to be of interest beyond the immediate plant community.
  - **Technical soundness**: The technical soundness is currently not fully established due to the concerns raised above regarding simulation methodology, quantitative validation, and reliance on prior data. The framework is promising but requires additional rigor.
  - **Readability for nonspecialists**: The manuscript is generally well-written and accessible. The summary and introduction provide appropriate context, and the figures are helpful. However, some simulation details may be challenging for nonspecialists, and the terminology could be more consistent.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a promising framework with interesting findings, but the current evidence base has limitations that need to be addressed. Specifically, the simulation methodology needs more rigorous validation, the experimental characterization needs to be more quantitative, and the RNA binding claims need to be better supported. If these concerns are addressed, the work would be a valuable contribution to the field.

## Risk / unsupported claims
- The claim that the PARCLPLD Y−E mutant "prevents" condensate formation is not fully supported by the qualitative experimental data presented; the data appear to show altered aggregation behavior rather than complete prevention.
- The claim that "phase separation and RNA binding can be independently targeted" is not directly supported by new experimental evidence in this manuscript; it relies on comparison with previously published data.
- The claim that the workflow "may be of general applicability" is not supported by evidence from multiple protein systems.
- The statement that simulations "successfully reproduce condensate formation" is weakened by the failure to simulate the eYFP-PARCL construct used in experiments.
- The claim that the identified C-terminal region is the RNA binding site is based on simulation predictions and prior experimental work, but the current manuscript does not provide direct experimental validation of this specific prediction.