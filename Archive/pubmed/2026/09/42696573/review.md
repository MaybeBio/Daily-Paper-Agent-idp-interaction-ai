## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, materials and methods, and supplementary figure legends as provided.
- **Assessment boundary** Scientific content, experimental design, data interpretation, and internal consistency of the claims as presented in the provided text. No external validation or replication was performed.
- **Shared manuscript claim summary** The authors propose a multistep model for ULK1 complex recruitment to membranes in autophagy, in which PI3P-bound WIPI3 (and WIPI2) engages the ATG13:ATG101 HORMA dimer, the ATG101 WF finger and C-terminal helix insert into the membrane, and a PVP motif in the ULK1 intrinsically disordered region docks onto the ATG13:ATG101 dimer to bring the ULK1 kinase domain close to the membrane surface for substrate phosphorylation.
- **Visible evidence base** In vitro binding assays (GST pull-down), GUV membrane recruitment assays, atomistic molecular dynamics simulations, AlphaFold structural predictions, cell-based autophagy and mitophagy assays, immunoprecipitation, and immunofluorescence microscopy.
- **Missing materials affecting confidence** Figures and supplementary figures are referenced but not provided in the submitted text. Quantitative data (e.g., exact fluorescence intensities, statistical values, Western blot images) are described but not shown. Molecular dynamics simulation parameters and convergence metrics are only partially described. The manuscript text does not include full figure legends or supplementary figure legends.

## Reviewer
- **Overall assessment** The manuscript addresses a long-standing question in autophagy research: how the ULK1 complex, which lacks canonical PI3P-binding domains, is recruited to PI3P-enriched membranes. The proposed multistep model is conceptually attractive and integrates structural prediction, biophysical simulation, biochemical reconstitution, and cell-based validation. However, the evidence as presented in the text is incomplete. Key figures are not available for inspection, and several quantitative claims are made without visible supporting data. The central novelty, the PVP motif interaction with the ATG13 HORMA domain, is supported by AlphaFold prediction and mutagenesis, but the mechanistic detail and the physiological relevance require stronger experimental evidence. The manuscript is potentially important but currently not fully established from the provided material.
- **Who would be interested in the results, and why** Researchers in autophagy, membrane trafficking, and kinase signaling. The work provides a mechanistic framework for ULK1 recruitment that has been missing for over a decade. The proposed role of WIPI3 in ULK1 complex recruitment and the identification of a PVP motif as a docking element will be of interest to those studying autophagy initiation, mitophagy, and the molecular basis of Parkinson's disease, given the genetic links between autophagy and this condition.
- **Major strengths** 1. The study tackles a fundamental and unresolved question in autophagy: the mechanism of PI3P-dependent ULK1 complex recruitment. 2. The combination of AlphaFold prediction, MD simulations, biochemical reconstitution, and cell-based assays provides a multidisciplinary approach. 3. The identification of a specific PVP motif in the ULK1 IDR that docks onto the ATG13:ATG101 HORMA dimer is a novel and testable hypothesis. 4. The use of GUVs for membrane recruitment assays provides a physiologically relevant in vitro system. 5. The inclusion of both autophagy and mitophagy assays strengthens the physiological relevance of the findings.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (missing quantitative data for binding and membrane recruitment), R1-M2 (lack of direct evidence for PVP motif binding), R1-M3 (incomplete MD simulation validation), R1-M4 (unclear specificity of WIPI3 over WIPI2).
- **Assessment against Nature-style criteria** **Originality:** High. The proposed multistep recruitment model is novel and provides a mechanistic explanation for a long-standing observation. The identification of the PVP motif as a docking element is original. **Scientific importance:** High. The work addresses a central question in autophagy and has implications for understanding disease-associated mutations. **Interdisciplinary readership:** Moderate to high. The work will appeal to cell biologists, biochemists, and structural biologists. The use of MD simulations may attract computational biologists. **Technical soundness:** Currently not fully assessable. The experimental design is reasonable, but the lack of visible quantitative data and incomplete methodological details for the simulations prevent a full assessment. **Readability for nonspecialists:** The manuscript is generally well-written and the logic is clear. However, some sections (e.g., MD simulation details) may be challenging for non-specialists. The abstract is accessible.
- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual model is attractive and the experimental approach is appropriate, but the evidence as presented is incomplete. The authors must provide the missing quantitative data, direct binding evidence for the PVP motif, and more detailed simulation validation before the case is fully established.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The authors claim that ATG13:ATG101 binds to WIPI3 with a clear preference over WIPI4 (Fig. 1, F and G), and that membrane recruitment of ATG13:ATG101 to GUVs is robust in the presence of WIPI3 (Fig. 2, B and C).
- **Evidence pointer** Results section "ATG13 contains a DHF motif that binds to WIPI3 at a different site than WIPI2"; Figures 1F, 1G, 2B, 2C; location not provided
- **Concern** The quantitative data supporting these claims are not visible in the provided text. The authors state that binding was assessed by microscopy-based assays and that fluorescence intensity was quantified, but no numerical values, representative images, or statistical comparisons are shown. Similarly, for the GUV experiments, the claim of "robust recruitment" is not supported by visible data. Without these data, the strength of the WIPI3 preference and the efficiency of membrane recruitment cannot be evaluated.
- **Why it matters** These are foundational claims for the entire model. If the binding preference is weak or the membrane recruitment is inefficient, the proposed mechanism would be undermined. The reader must be able to assess the magnitude and reproducibility of these effects.
- **Resolution test** Provide representative fluorescence images and quantified intensity values (with standard deviations and statistical tests) for the binding and GUV recruitment assays. Show that the WIPI3 preference is statistically significant and that membrane recruitment is concentration-dependent and saturable.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic evidence
- **Claim pointer** The authors claim that the PVP motif in the ULK1 IDR docks onto the ATG13:ATG101 HORMA dimer, bringing the ULK1 kinase domain close to the membrane (Results section "The ULK1-IDR interaction with ATG13HD drives proximity of ULK1 KD to the membrane").
- **Evidence pointer** Results section "ULK1 IDR binds directly to the ATG13 HORMA domain"; Figures 5B, 5D, 5E; location not provided
- **Concern** The evidence for the PVP motif binding to ATG13 is based on AlphaFold prediction and a single mutagenesis experiment (ADA mutation) showing loss of binding in a GST pull-down assay. However, the text does not provide direct binding data (e.g., isothermal titration calorimetry, surface plasmon resonance, or quantitative pull-down with varying concentrations) to demonstrate a specific and direct interaction. The AlphaFold prediction is useful but not sufficient. Furthermore, the text does not show that the PVP motif is sufficient for binding (e.g., a peptide competition experiment or a chimeric construct).
- **Why it matters** The PVP motif is a central novel finding of the manuscript. If the interaction is not direct and specific, the proposed mechanism for bringing the kinase domain to the membrane would be incorrect. The functional importance of this interaction is also not fully established, as the ADA mutation may have pleiotropic effects on ULK1 structure or stability.
- **Resolution test** Provide quantitative binding data (e.g., ITC or MST) for the ULK1 PVP peptide binding to the ATG13:ATG101 HORMA dimer. Show that the ADA mutation abolishes binding in a dose-dependent manner. Demonstrate that the PVP motif is sufficient to recruit a heterologous protein to the membrane in a WIPI3-dependent manner.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical validation
- **Claim pointer** The authors claim that atomistic MD simulations show stable membrane association of the ATG13-ATG101-WIPI3 complex and cooperative stabilization by WIPI3 and the WF finger (Results section "ATG13-ATG101-WIPI3 complexes stably interact with membrane in molecular dynamics simulations").
- **Evidence pointer** Results section "ATG13-ATG101-WIPI3 complexes stably interact with membrane in molecular dynamics simulations"; Figures 3A, 3E, 3F, 3I; location not provided
- **Concern** The MD simulation methodology is described in the Materials and Methods, but key validation metrics are missing. The authors state that four replicas were run for 1 μs each, but do not report convergence criteria, error bars on RMSD values, or whether the simulations reached equilibrium. The claim of "stable" association is based on RMSD values below ~1 Å, but the time evolution of these values is not shown. Furthermore, the initial placement of the complex on the membrane is described, but the equilibration protocol is complex and may introduce biases. The text does not describe how the membrane-bound state was distinguished from non-specific adsorption.
- **Why it matters** The MD simulations are used to support the structural model and the cooperative stabilization mechanism. If the simulations are not properly validated, the conclusions drawn from them are not reliable. The reader must be able to assess the quality and convergence of the simulations.
- **Resolution test** Provide RMSD and RMSF plots over time for all replicas, with error bars. Show that the system reached equilibrium and that the key interactions (DHF motif, WF finger, LRRG motif) are stable. Provide control simulations with mutant complexes (e.g., WF|DD) to show that the loss of membrane association is specific.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Specificity
- **Claim pointer** The authors claim that WIPI3 is the primary WIPI family member that recruits ATG13:ATG101 to membranes, and that WIPI2 also binds but at a different site (Results section "ATG13 contains a DHF motif that binds to WIPI3 at a different site than WIPI2").
- **Evidence pointer** Results section "ATG13 contains a DHF motif that binds to WIPI3 at a different site than WIPI2"; Figures 1F, 1G; location not provided
- **Concern** The text states that ATG13:ATG101 binds to WIPI3 with a clear preference over WIPI4, but the comparison to WIPI1 and WIPI2 is not fully described. The authors mention that WIPI2 also binds, but the relative affinities and the functional significance of the WIPI2 interaction are not clear. The text states that the WIPI2 binding site is different from the WIPI3 binding site, but the evidence for this is not presented in detail. The specificity of the interaction for WIPI3 over WIPI2 is important for the model, as WIPI2 is more abundant and better studied.
- **Why it matters** If WIPI2 also binds ATG13:ATG101 with similar affinity, the proposed model would need to account for the relative contributions of WIPI2 and WIPI3. The specificity of the interaction is also important for understanding the distinct roles of WIPI family members in autophagy.
- **Resolution test** Provide quantitative binding data for ATG13:ATG101 against all four WIPI family members. Show the relative affinities and demonstrate that the WIPI2 interaction is functionally distinct from the WIPI3 interaction (e.g., by showing that WIPI2 binding is not affected by the DHF motif mutation).

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states that "PI3P is essential to recruit ULK1 complex to membranes" but the mechanism is not described in the abstract. The abstract would benefit from a brief statement of the proposed multistep model.
- **Required correction** Add a sentence in the abstract summarizing the multistep recruitment model, e.g., "We show that PI3P-bound WIPI3 engages the ATG13:ATG101 HORMA dimer, which inserts into the membrane via the ATG101 WF finger, and that a PVP motif in the ULK1 IDR docks onto ATG13 to position the kinase domain at the membrane."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results section "ATG13 contains a DHF motif that binds to WIPI3 at a different site than WIPI2"
- **Evidence pointer** Figure 1G; location not provided
- **Issue** The text states that statistical significance was determined by one-way ANOVA with Bonferroni post hoc test, but the exact p-values and the number of independent experiments are not stated in the text.
- **Required correction** Provide exact p-values and the number of independent experiments (n) for each comparison in the figure legend or in the text.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Materials and Methods, "Modeling of ULK1C"
- **Evidence pointer** Materials and Methods, "Modeling of ULK1C"; location not provided
- **Issue** The description of the hierarchical chain growth (HCG) and cyclic coordinate descent (CCD) methods is brief. The text states that "we iteratively select a random residue on the chain modeled by HCG and a phi or psi dihedral angle and then perform a small rotation drawn from a Gaussian distribution with a mean of zero and a standard deviation of 1 degree." The acceptance criteria for the CCD moves are not fully described.
- **Required correction** Provide a more detailed description of the CCD algorithm, including the acceptance criteria, the number of iterations, and the convergence criteria.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Materials and Methods, "Quantification of immunofluorescence image"
- **Evidence pointer** Materials and Methods, "Quantification of immunofluorescence image"; location not provided
- **Issue** The code for quantification is deposited in GitHub, but the specific version and the date of access are not provided.
- **Required correction** Provide the specific version of the code and the date of access in the Data and Materials Availability statement.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion; location not provided
- **Issue** The discussion mentions that the PVP motif is "important" for autophagy and mitophagy, but the text does not discuss the quantitative contribution of this interaction compared to other membrane-binding mechanisms (e.g., the WF finger, palmitoylation).
- **Required correction** Add a paragraph in the discussion that quantitatively compares the contributions of the different membrane-binding mechanisms and discusses the potential redundancy or cooperativity.

## Risk / unsupported claims
- The claim that the ATG13:ATG101 HORMA dimer "does not bind to PI3P" is based on GUV assays, but the data are not shown. This is a negative result and should be supported by a positive control (e.g., a known PI3P-binding protein) to demonstrate the assay's sensitivity.
- The claim that the PVP motif is "essential" for ULK1 function is based on the ADA mutation, but the text does not show that the ADA mutation does not affect ULK1 kinase activity directly or that it does not disrupt the overall folding of the ULK1 IDR.
- The claim that WIPI3 is "critical" for ULK1 recruitment in cells is based on the co-IP and colocalization data, but the text does not show a loss-of-function experiment (e.g., WIPI3 knockdown) to demonstrate causality.
- The MD simulation results are used to support the model, but the simulations are not validated against experimental data (e.g., mutagenesis of the DHF motif or WF finger in the simulation context).
- The quantitative contribution of the PVP motif to the overall membrane recruitment is not directly measured. The text states that the ADA mutation reduces phosphorylation, but the reduction in membrane recruitment is inferred, not directly shown.