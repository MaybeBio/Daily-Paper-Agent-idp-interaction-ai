## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and figure legends. Supplementary figure and table legends are referenced but not fully provided.
- **Assessment boundary** Scientific content, experimental design, data interpretation, and consistency of claims with presented evidence. Not assessed: grammar, formatting, or editorial scope decisions.
- **Shared manuscript claim summary** The authors propose a multistep, induced-fit mechanism for binding of the intrinsically disordered HBV/HDV preS1 domain to the NTCP receptor. They identify Asn9, Gly12, and His17 in preS1 as critical residues forming a "core" structure that docks into the NTCP bile acid tunnel, and Trp41 as a secondary stabilizer interacting with the extracellular surface. The mechanism is supported by binding assays, infection assays in cell culture and mice, molecular dynamics simulations, and a statistical mechanical model.
- **Visible evidence base** Figure 1 (domain binding assays, alanine mutagenesis, competition assays), Figure 2 (NTCP mutant analysis, structural contacts), Figure 3 (MD simulation PCA and distance analyses), Figure 4 (HDV infectivity in cells and mice), Figure 6 (WSME-L model predictions), Supplementary Figures 1-6 (referenced), Supplementary Tables 1-4 (referenced), Methods section.
- **Missing materials affecting confidence** Supplementary figures and tables are referenced but not provided in the submitted text. Raw MD trajectory data, statistical analysis details for mouse experiments, and the full WSME-L model parameters are not available. The exact number of replicates for mouse experiments is not stated in the visible text.

## Reviewer
- **Overall assessment** This manuscript presents a compelling and well-integrated study combining structural biology, computational simulation, and virological validation to address a fundamental question in HBV entry: how an intrinsically disordered peptide achieves high-affinity receptor binding. The identification of specific residues (Asn9, Gly12, His17, Trp41) with distinct functional roles is a significant advance. The combination of experimental and theoretical approaches is ambitious and largely successful. However, several concerns regarding the strength of causal claims, the generalizability of the MD findings, and the statistical treatment of some experiments need to be addressed before the case is fully established.
- **Who would be interested in the results, and why** Virologists studying HBV/HDV entry and host tropism; structural biologists interested in protein-protein interactions involving intrinsically disordered regions; computational biologists developing models of coupled folding and binding; and pharmaceutical scientists developing entry inhibitors targeting the preS1-NTCP interface. The proposed multistep mechanism has direct implications for understanding species specificity and for designing inhibitors that block specific steps of the binding process.
- **Major strengths**
  1. The study addresses a genuinely important and unresolved question: how a disordered viral peptide achieves high-affinity, specific receptor binding.
  2. The combination of multiple orthogonal approaches (biochemistry, virology, MD simulation, statistical mechanics) provides a rich and multifaceted view of the problem.
  3. The identification of specific residues with distinct mechanistic roles (core formation vs. surface stabilization) is a clear and testable advance over previous models.
  4. The validation in both cell culture and an in vivo mouse model strengthens the biological relevance of the findings.
  5. The authors are appropriately cautious in presenting the binding order as a hypothesis, acknowledging alternative possibilities.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal inference
- **Claim pointer** The authors state that Asn9, Gly12, and His17 "primarily mediate the NTCP binding" and that mutation in these residues "abolishes virion infectivity."
- **Evidence pointer** Figure 1d, 1e, Figure 4b, 4c
- **Concern** The alanine mutagenesis experiments show that N9A, G12A, and H17A mutations abolish binding and infectivity. However, the authors do not demonstrate that these mutations specifically disrupt the proposed "core" structure without causing global misfolding or aggregation of the preS1 peptide. The MD simulations show structural destabilization, but these are performed on the isolated 2-19 fragment, not on the full-length preS1 in the context of the viral particle. The claim that these residues "primarily mediate" binding is strong; the data show they are necessary, but not that they are the primary drivers of the interaction energy.
- **Why it matters** Without ruling out global structural disruption, the specific mechanistic role of these residues in forming a "core" structure is not fully established. The distinction between residues that are critical because they form a specific structural element versus those that are critical because their mutation destabilizes the entire peptide is important for understanding the mechanism and for drug design.
- **Resolution test** Provide biophysical characterization (e.g., circular dichroism, size-exclusion chromatography, or NMR) of the mutant peptides to show they retain overall disorder and do not aggregate. Alternatively, perform MD simulations on the full-length preS1 mutants to show that the destabilization is localized to the core region.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative support
- **Claim pointer** The authors claim that the WSME-L model "predicts that 2-19preS1 region undergoes robust folding (up to 0.75), followed by the late 20-48preS1 folding."
- **Evidence pointer** Figure 6, Methods (Statistical mechanical model)
- **Concern** The WSME-L model is a coarse-grained model that uses the final bound structure as input. The prediction of folding order is therefore dependent on the input structure and the model's parameters. The authors state that the model was "calibrated" using the experimentally obtained dissociation constant, but the details of this calibration and the sensitivity of the predicted folding order to model parameters are not presented. The claim of a specific folding order (2-19 before 20-48) is a key part of the proposed mechanism, but the evidence for this specific order from the model is not quantitatively robust as presented.
- **Why it matters** The proposed "multistep" mechanism relies on a specific temporal order of folding events. If the model is highly sensitive to parameters or if the predicted order is not robust, the claim of a sequential, ordered process is weakened.
- **Resolution test** Provide a sensitivity analysis of the WSME-L model predictions to key parameters (e.g., contact energy scaling, entropy cost). Show that the predicted folding order is robust across a reasonable range of parameter values. Alternatively, provide an independent experimental test of the folding order (e.g., hydrogen-deuterium exchange or time-resolved FRET).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor
- **Claim pointer** The authors state that "mutation in these key residues abolishes virion infectivity in cell culture and mouse models."
- **Evidence pointer** Figure 4b, 4c
- **Concern** The statistical analysis for the mouse experiments is not described in the visible text. The figure legend states "n=5" and "**p<0.05" but the specific test used, the variance structure, and whether the data met test assumptions are not stated. For the cell culture infectivity data, the number of independent experiments and the statistical test are also not fully described in the visible text.
- **Why it matters** The in vivo data are a key strength of the study, but without clear statistical reporting, the robustness of the conclusion that the mutants abolish infectivity cannot be fully evaluated.
- **Resolution test** Provide full statistical details for all experiments, including the specific test used, the number of independent biological replicates, and the variance structure. For the mouse data, report individual animal data points and the exact p-values.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic completeness
- **Claim pointer** The authors propose that Trp41 stabilizes the preS1 33-48 region on the NTCP outerface, involving Asn87 and Tyr146.
- **Evidence pointer** Figure 5, Supplementary Table 3
- **Concern** The functional validation of the Trp41 interaction is weaker than for the core residues. The authors show that W41A mutation reduces binding and infectivity, but the effect is described as partial ("reduced" not "abolished"). The specific contribution of the Trp41-Asn87/Tyr146 interaction to the overall binding affinity is not quantified. The MD simulations show contacts, but the energetic contribution of this interaction is not assessed.
- **Why it matters** The proposed two-step mechanism (core formation followed by surface stabilization) requires that both steps contribute meaningfully to the overall affinity. If the Trp41 interaction contributes only marginally, the "multistep" aspect of the mechanism is less compelling.
- **Resolution test** Perform a double mutant cycle analysis to quantify the energetic coupling between Trp41 and Asn87/Tyr146. Alternatively, use surface plasmon resonance or isothermal titration calorimetry to measure the binding affinity of the 33-48 peptide alone and with mutations.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1c, 1d
- **Evidence pointer** Figure 1c, 1d
- **Issue** The quantification of fluorescence intensity is described as "percentages relative to the signals for myr-2-48preS1" but the normalization method is not fully described. It is unclear whether the values are background-subtracted and how the background was determined.
- **Required correction** Clarify the image analysis and normalization procedure in the Methods or figure legend.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion
- **Evidence pointer** Discussion, paragraph 2
- **Issue** The discussion of the "binding maturation" concept would benefit from a more explicit comparison with other known IDP-receptor interactions that involve coupled folding and binding. The authors mention this is a "unique" mechanism but do not place it in the broader context of IDP biology.
- **Required correction** Add a brief paragraph comparing the proposed mechanism with other well-characterized IDP binding mechanisms (e.g., p53-MDM2, ACTR-NCBD) to highlight what is truly novel.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Methods, MD simulations
- **Evidence pointer** Methods, Molecular dynamics simulations
- **Issue** The methods state that three independent 1 μs simulations were performed, but the convergence of the simulations is not demonstrated. No RMSD time series or block averaging analysis is shown.
- **Required correction** Provide a figure or statement demonstrating that the simulations converged and that the observed differences between WT and mutants are not due to insufficient sampling.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Figure 3d
- **Evidence pointer** Figure 3d
- **Issue** The contact frequency analysis in Figure 3d shows reduced contacts for mutants, but the threshold for defining a "contact" is not stated in the visible text.
- **Required correction** State the contact definition (distance cutoff, atom types) in the Methods or figure legend.

## Risk / unsupported claims
- The claim that the proposed mechanism is "multistep" with a specific temporal order (core formation before surface stabilization) is not fully supported by the data. The WSME-L model prediction is model-dependent, and the experimental data do not directly measure the temporal order of events.
- The claim that Asn9, Gly12, and His17 "primarily mediate" binding is not fully supported without ruling out global structural effects of the mutations.
- The functional significance of the Trp41 interaction is demonstrated but not quantified; the claim that it "stabilizes" the complex is inferred from reduced binding, not directly measured.
- The statement that the mechanism "ensures high virion infectivity and strict host specificity" is an extrapolation. The data show that the residues are important for infectivity, but the link to host specificity is not directly tested.
- The mouse experiment data are presented with minimal statistical detail, making the strength of the in vivo claim difficult to fully assess.