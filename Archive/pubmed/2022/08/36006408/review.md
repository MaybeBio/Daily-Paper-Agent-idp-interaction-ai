## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, summary) and references to supplementary figures and tables
- **Assessment boundary** Scientific claims, methodological soundness, consistency between experimental data and simulation results, and interpretation of molecular dynamics simulations
- **Shared manuscript claim summary** The authors report that Nvjp-1 hydrogels can bind zinc at low pH and exhibit enhanced mechanical properties when pH is raised, and use polarizable all-atom MD simulations to propose a mechanism involving polar residue coordination at low pH, histidine-mediated coordination at alkaline pH, and anion-dependent modulation of zinc uptake.
- **Visible evidence base** Mechanical testing data (Figure 1), MD simulation results (Figures 2–8), DFT interaction energies (Table T1, Figure S8), PROPKA protonation predictions (Figure S2), RMSD equilibration (Figure S4), radial distribution functions (Figure 3), nonbonded interaction energy distributions (Figure 4), zinc coordination counts (Figures 5, 7), radius of gyration data (Figures 6, S10, S11)
- **Missing materials affecting confidence** Supplementary figures and tables referenced but not provided (Figures S1–S13, Table T1); simulation input parameters and force field details only partially described; no error bars or statistical analysis reported for MD observables; no raw data for mechanical testing beyond summary statistics; no information on force field parameters for Zn2+ ions

## Reviewer
- **Overall assessment** This manuscript addresses an interesting and timely question regarding the molecular basis of metal binding in an intrinsically disordered protein relevant to biomimetic materials. The combination of experimental rheology and polarizable MD simulations is appropriate and potentially valuable. However, the manuscript has several significant weaknesses that currently prevent the conclusions from being fully established. The experimental data are limited to a single set of conditions with no replicates or statistical analysis reported. The MD simulations, while extensive, lack key validation steps and the interpretation of some results appears to overreach the simulation evidence. The claim of being the first computational study of Nvjp-1 with explicit polarization is likely correct but is not by itself a strong scientific contribution. The mechanistic model proposed is plausible but requires additional support, particularly regarding the role of acetate and the relationship between simulated coordination patterns and macroscopic mechanical properties.

- **Who would be interested in the results, and why** Researchers in the fields of biomaterials, intrinsically disordered proteins, metal-protein interactions, and computational biophysics would find this work relevant. The study provides molecular-level hypotheses for how pH and counteranions modulate metal binding in a histidine-rich protein, which could inform the design of stimuli-responsive hydrogels and synthetic biomimetic materials. The methodological approach combining polarizable MD with experimental rheology may also interest computational chemists working on metal-protein systems.

- **Major strengths**
  1. The study addresses a biologically and materials-relevant question with a combination of experimental and computational approaches.
  2. The use of a polarizable force field is appropriate for studying metal-protein interactions where charge redistribution is important.
  3. The finding that polar residues, rather than acidic residues, dominate zinc coordination at low pH is counterintuitive and potentially significant.
  4. The comparison of chloride versus acetate counteranions provides insight into anion-specific effects on metal binding.
  5. The authors acknowledge limitations of their approach and suggest directions for future work.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental reproducibility and statistical rigor
- **Claim pointer** The authors claim that "zinc binding to Nvjp-1 is stable at both acidic and alkaline pH conditions" and that mechanical properties are modulated by pH, based on compressive modulus measurements.
- **Evidence pointer** Figure 1, "Mechanical Testing of Nvjp-1 Hydrogels" section
- **Concern** The mechanical testing data are presented without any indication of the number of replicates, error bars, or statistical significance testing. The text states experiments were performed on "at least three different hydrogels" and standard error was calculated, but no error bars are visible in Figure 1 as described, and no statistical comparisons are reported. The claim of significant differences between Zn2+ and Na+ treated hydrogels at different pH values cannot be evaluated without this information.
- **Why it matters** The central experimental claim of the manuscript, that pH-dependent mechanical modulation occurs and is reversible, rests entirely on these measurements. Without proper statistical treatment, the reader cannot assess whether the observed differences are meaningful or within experimental noise.
- **Resolution test** Provide replicate data with error bars and appropriate statistical tests (e.g., ANOVA or t-tests) for all comparisons claimed to be significant. Report exact p-values or confidence intervals.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Simulation validation and force field accuracy
- **Claim pointer** The authors claim that "zinc binding to Nvjp-1 is stable at both acidic and alkaline pH conditions" and that the simulations reveal the mechanism of pH-dependent metal binding.
- **Evidence pointer** "Force Field" and "Nvjp-1 Simulation Setup" sections; Table T1; Figure S8
- **Concern** The manuscript does not provide sufficient validation of the Drude polarizable force field parameters for Zn2+ in protein environments. The comparison with DFT shows differences of 5–67 kcal/mol in interaction energies, which is a very large range. The authors acknowledge this discrepancy but do not address whether the force field can accurately capture the coordination geometries and energetics that are central to their conclusions. No information is provided on how Zn2+ parameters were derived or tested against experimental data.
- **Why it matters** The entire mechanistic interpretation depends on the accuracy of the simulated Zn2+ coordination. If the force field over- or under-binds certain residues, the conclusions about which residues coordinate zinc at different pH values could be incorrect.
- **Resolution test** Provide validation of Zn2+ force field parameters against experimental binding energies or high-level QM calculations for relevant model systems. Report the range of errors and discuss how they affect the confidence in the coordination assignments.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Simulation length and equilibration
- **Claim pointer** The authors claim that "the results of these studies suggest a system where polar residues mediate metal binding at low pH conditions and pass them to a carboxylate/imidazole coordination pocket as the pH approaches neutrality."
- **Evidence pointer** "Nvjp-1 Zinc Binding at pH 5" and "Zinc, Counterions and Nvjp-1 Radius of Gyration at Varying pH" sections; Figures 2, 5, 7
- **Concern** The simulations are described as "over 300 ns" in length, but no information is provided on whether this is sufficient for convergence of the observables reported. For an intrinsically disordered protein, conformational sampling is notoriously slow, and 300 ns may not be adequate to capture the equilibrium ensemble. No block averaging, convergence tests, or multiple independent simulations are reported. The claim of "passing" zinc ions between residue types implies a dynamic process that would require careful kinetic analysis.
- **Why it matters** If the simulations are not converged, the coordination patterns and radius of gyration values reported may be artifacts of the initial conditions or insufficient sampling, rather than equilibrium properties.
- **Resolution test** Provide convergence analysis (e.g., time evolution of key observables, block error estimates) and ideally multiple independent simulations starting from different initial configurations. If possible, extend simulation times or use enhanced sampling methods.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of radius of gyration changes
- **Claim pointer** The authors claim that "the Rg of Nvjp-1 appears to decrease at early times from its starting value but fluctuates strongly over time" in ZnCl2 at pH 5, and that at pH 8 the Rg stabilizes, "indicating a contraction of Nvjp-1 due to an increase in coordination with zinc ions."
- **Evidence pointer** Figure 6, Figure S10
- **Concern** The relationship between Rg changes and zinc coordination is inferred but not directly demonstrated. The authors do not show a correlation between the number of coordinated zinc ions and Rg over time, nor do they rule out other factors such as changes in protonation state or counterion binding that could affect protein compaction. The claim that Rg stabilization at pH 8 is due to increased zinc coordination is not supported by direct evidence.
- **Why it matters** The connection between molecular-level coordination and macroscopic hydrogel contraction is a key part of the proposed mechanism. Without demonstrating this link, the relevance of the Rg data to sclerotization is unclear.
- **Resolution test** Plot Rg against the number of coordinated zinc ions over time to show a direct correlation. Alternatively, perform simulations without zinc to isolate the effect of metal binding on Rg.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the proposed mechanism
- **Claim pointer** The authors propose that "the sequestration of acidic residues by protonated histidines at pH 5 in zinc chloride, where the salt bridges would create future metal coordination pockets within the protein by spatially localizing both coordinating carboxylates and imidazoles."
- **Evidence pointer** "Summary" section
- **Concern** This is a speculative mechanistic proposal that goes beyond the simulation data presented. While it is a reasonable hypothesis, the authors do not provide direct evidence for the formation of such "pockets" or their functional relevance. The claim that this explains the "asymmetrical sclerotization response" is not tested.
- **Why it matters** This is presented as a central conclusion of the work, but it is not directly supported by the data. Overinterpretation of simulation results can mislead readers and future research directions.
- **Resolution test** Design simulations or experiments that directly test the formation and function of these proposed coordination pockets, such as mutational analysis or targeted simulations with modified sequences.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Simulation setup
- **Evidence pointer** "Nvjp-1 Simulation Setup" section
- **Issue** The description of how pH was modeled in the simulations is vague. The authors state that PROPKA was used to determine protonation states, but do not specify which residues were protonated at each pH, how many histidines were in each protonation state, or whether the protonation states were held fixed or allowed to change during the simulation.
- **Required correction** Provide a table or detailed description of the protonation states used for each simulation condition, and clarify whether these were fixed throughout the simulation.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 1
- **Evidence pointer** "Mechanical Testing of Nvjp-1 Hydrogels" section
- **Issue** The description of Figure 1 is incomplete. The text refers to panels a–d but does not clearly describe what each panel shows. The reader cannot determine what data are presented in each panel without referring to the figure itself.
- **Required correction** Expand the figure caption and text description to clearly explain each panel, including the conditions, time points, and what is being measured.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Sclerotization" usage
- **Evidence pointer** Throughout the manuscript
- **Issue** The term "sclerotization" is used to describe the increase in mechanical properties of hydrogels, but sclerotization in biological systems typically refers to a specific chemical cross-linking process involving quinone tanning. The authors do not demonstrate that the same chemical process occurs in their hydrogels.
- **Required correction** Clarify whether "sclerotization" is used in a general sense to mean hardening, or whether a specific chemical mechanism is implied. If the latter, provide evidence for the chemical cross-linking mechanism.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction
- **Evidence pointer** "Introduction" section
- **Issue** The introduction does not adequately discuss previous computational studies of metal binding to intrinsically disordered proteins or histidine-rich proteins. The claim of being the "first computational study of the Nvjp-1 protein in microscopic detail where polarization effects are taken into account explicitly" is narrow and does not position the work within the broader literature.
- **Required correction** Add a brief discussion of prior computational studies of metal binding to disordered proteins and how the present work advances beyond them.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Supplementary material accessibility
- **Affected element** Figures S1–S13, Table T1
- **Evidence pointer** "Supplementary Material" section
- **Issue** The manuscript relies heavily on supplementary figures and tables, but these are not provided for review. Key data, such as the DFT interaction energies in Table T1 and the Rg distributions in Figure S10, are only available in the supplementary material.
- **Required correction** Ensure that all supplementary material is available to reviewers and readers, and consider moving the most critical data (e.g., Table T1) to the main text.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Simulation temperature
- **Affected element** Simulation conditions
- **Evidence pointer** "Force Field" section
- **Issue** The simulations were performed at 500 K, which is far above physiological temperature. The authors justify this choice as a means to enhance sampling, but this raises questions about whether the observed coordination patterns are relevant at lower temperatures where the protein would be less mobile.
- **Required correction** Discuss the potential effects of the elevated temperature on the conclusions, and ideally perform at least one simulation at a more relevant temperature to confirm the key findings.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Statistical analysis of coordination numbers
- **Affected element** Figure 7
- **Evidence pointer** "pH and Counteranion Effects on Zinc Coordination" section
- **Issue** The coordination number distributions in Figure 7 are presented as counts, but no error estimates or statistical comparisons are provided. It is unclear whether the differences between chloride and acetate conditions are statistically significant.
- **Required correction** Provide error bars or confidence intervals for the coordination number distributions, and perform statistical tests to support claims of significant differences.

## Risk / unsupported claims
- The claim that "zinc binding to Nvjp-1 is stable at both acidic and alkaline pH conditions" is not fully supported by the experimental data, as no statistical analysis is reported and the EDS data show a significant drop in zinc content when pH is lowered from 8 to 5.
- The claim that "acetate ions facilitate the capture of more zinc ions" is based on simulation data without experimental validation of zinc content in acetate versus chloride treated hydrogels.
- The proposed mechanism of "sequestration of acidic residues by protonated histidines" creating "future metal coordination pockets" is speculative and not directly tested.
- The claim of being the "first computational study of the Nvjp-1 protein in microscopic detail where polarization effects are taken into account explicitly" is a narrow claim that does not establish scientific significance.
- The relationship between simulated Rg changes and macroscopic hydrogel sclerotization is inferred but not demonstrated.
- The DFT comparison in Table T1 shows large discrepancies with the Drude model, and the authors acknowledge that "direct comparison may not be warranted," which undermines the validation of the force field.
- The relevance of simulations at 500 K to the experimental conditions (room temperature) is not adequately addressed.