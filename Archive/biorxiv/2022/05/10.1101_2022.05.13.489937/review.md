## Review setup
- **Input scope** Full manuscript text (abstract, main text, methods, results, discussion, conclusions) without supplementary figures or tables
- **Assessment boundary** Scientific soundness, technical validity of NMR methodology, interpretation of results, and alignment with stated conclusions
- **Shared manuscript claim summary** The authors present solid-state NMR approaches to study semi-rigid, solvent-exposed residues in mutant huntingtin exon 1 fibrils, including a new dynamic spectral editing method based on DIPSHIFT-DARR to selectively observe these otherwise masked residues.
- **Visible evidence base** Main text figures (Figures 1-7), tables referenced in text (Tables 1-2, S1-S3), and methods descriptions
- **Missing materials affecting confidence** Supplementary figures (S1-S4) and tables (S1-S3) are referenced but not provided; raw NMR data and processing scripts are not available for independent verification

## Reviewer
- **Overall assessment** This manuscript addresses a technically challenging and biologically relevant problem: the observation of semi-rigid, solvent-exposed residues in amyloid fibrils, specifically in mutant huntingtin exon 1. The authors combine variable-temperature ssNMR with a new DIPSHIFT-based dynamic spectral editing approach to reveal previously masked signals from non-core glutamine residues. The methodological innovation is interesting and potentially useful, but several technical aspects require clarification and the interpretation of the new signals would benefit from additional validation. The work is likely to be of interest to the solid-state NMR and amyloid research communities, though the broader impact may be somewhat limited by the specialized nature of the technique and the preliminary characterization of the newly observed residues.

- **Who would be interested in the results, and why** Solid-state NMR spectroscopists developing dynamic spectral editing methods will find the DIPSHIFT-DARR approach of direct relevance. Researchers studying amyloid fibril structure and dynamics, particularly those working on polyglutamine-containing proteins and huntingtin aggregation, will be interested in the observation of semi-rigid non-core residues. The potential implications for understanding dye binding and PET tracer interactions with amyloid fibrils may also attract researchers in diagnostic imaging and drug development for Huntington disease.

- **Major strengths** The manuscript addresses a genuine technical gap in amyloid structural biology, namely the difficulty of observing semi-rigid residues at the core-water interface. The combination of variable-temperature studies with a purpose-designed dynamic filter is a logical and well-motivated approach. The authors are transparent about the limitations of their method, including sensitivity issues and the non-quantitative nature of the observed signals. The work builds appropriately on prior studies from the same group and others, providing continuity with established knowledge of HttEx1 fibril structure.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the DIPSHIFT-DARR experiment selectively reveals semi-rigid residues by suppressing rigid core signals, and that the newly observed positive cross-peaks (Qc and Qd) represent solvent-exposed, semi-rigid glutamine residues.
- **Evidence pointer** Results section "Revealing residues with intermediate dynamics", Figure 7
- **Concern** The assignment of the new positive cross-peaks to specific glutamine populations (Qc and Qd) relies on chemical shift comparisons with prior work and on PLUQ-based predictions. However, the manuscript does not provide sufficient evidence to exclude the possibility that these signals arise from other residues or from artifacts of the filtering process. The Qd assignment is described as having "highest probability (~90%)" for Gln, which leaves non-negligible uncertainty. Additionally, the authors note that methyl groups and non-protonated carbons are not properly dephased by the filter, yet the potential contribution of such groups to the positive signals is not systematically addressed. The claim that these residues are "part of the polyQ segment, but not buried" is inferred rather than directly demonstrated.
- **Why it matters** The central novelty of the manuscript is the observation of these previously invisible semi-rigid residues. If the assignments are incorrect or the signals arise from artifacts, the main conclusion would be substantially weakened.
- **Resolution test** Provide additional validation of the Qc and Qd assignments, for example through site-specific isotope labeling experiments, or through complementary experiments (e.g., INEPT-based spectra at low temperature) that would independently confirm the presence of these semi-rigid glutamine populations. Alternatively, provide a more detailed analysis of the filter selectivity, including control experiments on model compounds or on samples with known dynamics.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that the DIPSHIFT-DARR experiment is a new DYSE method and that it is complementary to INEPT- and CP-based measurements.
- **Evidence pointer** Results section "Revealing residues with intermediate dynamics", Figure 6
- **Concern** The manuscript does not provide a quantitative characterization of the filter performance. Specifically, the relationship between the DIPSHIFT dephasing time (0.2 ms) and the range of correlation times or order parameters that are selected is not established. The authors state that the filter is "optimized for dephasing of protonated, immobile aliphatic carbons" but do not provide simulations or calibration experiments showing the expected selectivity as a function of mobility. Without this information, it is difficult to assess whether the observed positive signals indeed correspond to the claimed intermediate mobility regime, or whether they could arise from a broader range of dynamics than intended.
- **Why it matters** The selectivity of the filter is the foundation of the method. If the filter does not cleanly separate rigid from semi-rigid residues, the interpretation of the resulting spectra is ambiguous.
- **Resolution test** Provide numerical simulations of the DIPSHIFT dephasing behavior as a function of order parameter or correlation time, and/or experimental calibration on model systems with known dynamics. This would establish the range of mobilities that are selected and suppressed by the filter.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors suggest that the semi-rigid glutamine residues at the fibril-core surface are relevant to the binding of amyloid-specific dyes and PET tracers, and may be implicated in secondary nucleation events.
- **Evidence pointer** Discussion section
- **Concern** The connection between the observed semi-rigid residues and dye/PET tracer binding or secondary nucleation is speculative and not supported by direct experimental evidence in this manuscript. While the authors appropriately frame these as implications for future work, the relevance of the specific residues identified (Qc and Qd) to these processes is not established. The manuscript would be strengthened by a more focused discussion of what specific structural or functional insights the observation of these residues provides, beyond the general statement that they are surface-exposed.
- **Why it matters** The broader significance of the work depends in part on the functional relevance of the observed residues. If the connection to dye binding or nucleation is purely speculative, the impact of the work is more limited to the methodological contribution.
- **Resolution test** Provide additional context from prior studies on dye binding or nucleation that specifically implicates the residues or structural features identified here. Alternatively, temper the claims in the discussion to more clearly distinguish between established findings and speculative implications.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors interpret the increase in CP signal intensity upon freezing as evidence for immobilization of semi-rigid residues, and attribute the changes in polyQ signal to solvent-exposed residues rather than the rigid core.
- **Evidence pointer** Results section "Variable dynamics of distinct segments in the fibrils", Figures 2, S1, S2
- **Concern** The quantitative analysis of signal intensity changes upon freezing is not fully described. The authors mention that the polyQ signal increased in intensity upon freezing, but the magnitude of this increase and its consistency across different residues is not systematically presented. The deconvolution analysis referenced in Table S2 is not visible to the reader. Without this quantitative information, it is difficult to assess the strength of the claim that the observed changes are due to surface residues rather than partial changes in the core dynamics.
- **Why it matters** The interpretation of the temperature-dependent data underpins the conclusion that solvent dynamics couple to protein dynamics in a residue-specific manner. If the quantitative analysis is not robust, this conclusion is weakened.
- **Resolution test** Present the quantitative intensity and linewidth data for the key resonances at different temperatures, including the deconvolution results, in the main text or in a clearly referenced supplementary table.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and presentation
- **Affected element** Figure 2
- **Evidence pointer** Results section "Variable dynamics of distinct segments in the fibrils"
- **Issue** The figure caption does not clearly indicate which panels correspond to which temperature conditions, and the color coding of the different spectra is not explained in the caption.
- **Required correction** Provide a complete figure caption that identifies all panels, temperature conditions, and color codes.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section
- **Evidence pointer** Materials and Methods, NMR experiments
- **Issue** The methods section does not specify the sample volume, rotor filling factor, or the exact sample temperature calibration procedure used for the variable-temperature experiments.
- **Required correction** Add these experimental details to the methods section or to the supplementary information.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The statement that the "dehydrated core multiple nanometers thick" is based on prior EM and ssNMR studies is presented without a specific citation to the relevant prior work in this context.
- **Required correction** Add the appropriate citation to support this statement.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity and presentation
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the IMS-DYMS element can be integrated "in standard CP-based ssNMR experiments" but does not specify which types of experiments were actually performed in this work beyond DARR.
- **Required correction** Clarify in the abstract or introduction which specific experiments were performed and which are proposed as future applications.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Figure 5
- **Evidence pointer** Results section "Temperature-dependent changes in dipolar order parameters"
- **Issue** The DIPSHIFT data are presented as dephasing curves, but the error bars or reproducibility of the measurements are not shown or discussed.
- **Required correction** Include error estimates or state the number of replicate measurements used to generate the curves.

## Risk / unsupported claims
- The assignment of the Qd cross-peak to a glutamine residue with ~90% probability is not fully supported; the remaining uncertainty is not discussed in the context of alternative assignments.
- The claim that the observed semi-rigid glutamine residues are relevant to dye binding, PET tracer detection, and secondary nucleation is speculative and not directly tested in this work.
- The statement that the DIPSHIFT-DARR experiment is "new" and "to the best of our knowledge" not previously reported is appropriately hedged, but the novelty claim would be strengthened by a more thorough literature search.
- The quantitative relationship between the observed signal intensity changes and the fraction of residues affected is not established.
- The claim that the core is "dehydrated" is based on prior work, but the current manuscript does not provide direct evidence for water exclusion from the core in the samples studied here.