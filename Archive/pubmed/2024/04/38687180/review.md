## Review setup
- **Input scope** Full manuscript text (abstract, introduction, experimental section, results, discussion, supplementary figure/table references) as provided
- **Assessment boundary** Scientific content, technical soundness, claim-evidence alignment, and suitability for a high-impact general journal; no assessment of formatting, grammar, or editorial policy
- **Shared manuscript claim summary** The authors report that a supercharged, intrinsically disordered single-chain antibody fragment (scFv) conjugated to quantum-defect-modified single-walled carbon nanotubes (QWNTs) undergoes a ligand-induced folding transition upon binding interleukin-6 (IL-6), producing a local electric field change that redshifts the E11− defect fluorescence. Quantum chemical modeling is used to support the proposed mechanism.
- **Visible evidence base** Experimental sections for protein design, purification, circular dichroism, microscale thermophoresis, intrinsic tryptophan fluorescence, nanotube purification, covalent functionalization, protein conjugation, and near-infrared fluorescence spectroscopy; results sections for scFv design, binding affinity, folding thermodynamics, QWNT synthesis, and fluorescence response; quantum chemical modeling description; supplementary figure/table references (Figures S1–S8, Table S1)
- **Missing materials affecting confidence** Raw spectra (CD, fluorescence, MST traces), full fitting parameters and error estimates, replicate numbers and statistical analyses, supplementary figures and table contents, detailed computational methodology (basis set validation, convergence criteria, charge placement rationale), characterization data for protein purity and folding state (e.g., SEC, SDS-PAGE), control experiments for non-specific binding, and time-course data for sensor response

## Reviewer
- **Overall assessment** This manuscript presents a conceptually interesting integration of protein engineering and carbon nanotube photophysics, with a plausible mechanism supported by a combination of biophysical characterization and quantum chemical modeling. The central claim, that a supercharged scFv undergoing ligand-induced folding can sensitize quantum defect emission to local electric field changes, is novel and potentially significant. However, the evidence as presented has several gaps that prevent full confidence in the conclusions. Key concerns include the lack of direct structural characterization of the disordered-to-folded transition on the nanotube surface, the absence of statistical rigor in the spectral measurements, the limited control experiments, and the reliance on a simplified computational model without experimental validation of charge distributions or distances. The work is likely to interest researchers in nanosensor development, protein engineering, and carbon nanotube photophysics, but the current evidence does not fully establish the mechanistic claims.
- **Who would be interested in the results, and why** Researchers in nanosensor development, particularly those working on carbon nanotube-based optical biosensors, will find the concept of using phase-changing proteins to amplify quantum defect responses attractive. The protein engineering community, especially those interested in supercharging and intrinsically disordered proteins, will be interested in the demonstration that a scFv can be converted into a ligand-induced folder. Additionally, the photophysics community studying quantum defects in carbon nanotubes will be interested in the evidence for electric field sensitivity of defect emission. The potential clinical application for IL-6 detection in serum may also appeal to those in translational diagnostics.
- **Major strengths** The concept of coupling a phase-changing supercharged protein to a quantum defect is creative and addresses an underexplored area, namely the control of local electric fields at defect sites. The use of a physiologically relevant target (IL-6) and demonstration of detection in serum adds practical significance. The combination of experimental biophysics (CD, MST, fluorescence) with quantum chemical modeling provides a multi-pronged approach to the problem. The comparative experiments with the non-supercharged scFv (α-IL6wt) provide a useful control that strengthens the claim that supercharging is important. The reported stability of the sensor over one week is a practical advantage.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that α-IL6sc undergoes a full ligand-induced folding transition from an intrinsically disordered state to a compact folded state upon binding IL-6, and that this transition is responsible for the observed spectral shifts.
- **Evidence pointer** Results section "Design of signal-amplifying scFvs"; Figures 2C–2F; Supplementary Figures S2, S3
- **Concern** The evidence for the disordered-to-folded transition is indirect. Circular dichroism is only mentioned in the supplementary materials (Figure S2) and the data are not shown in the main text. The intrinsic tryptophan fluorescence measurements (Figure 2C) monitor folding via a single tryptophan residue, which may not report on global folding. The claim of a "full" transition is not supported by direct structural evidence (e.g., size-exclusion chromatography, analytical ultracentrifugation, or NMR). Furthermore, the folding behavior is characterized in solution, not when conjugated to the QWNT surface, where the local environment and crowding effects may alter the folding equilibrium.
- **Why it matters** The central mechanism of the sensor relies on the ligand-induced folding transition. If the protein does not undergo a full disorder-to-order transition, or if the transition is different on the nanotube surface, the proposed mechanism for the spectral shift is not valid. The quantitative relationship between folding free energy and binding affinity (Figure 2F) is used to support the mechanism, but this is based on solution measurements that may not reflect the surface-conjugated state.
- **Resolution test** Provide direct biophysical evidence of the conformational change, both in solution and when conjugated to QWNTs. This could include SEC-MALS, SAXS, or hydrogen-deuterium exchange mass spectrometry. For the surface-bound state, single-molecule FRET or AFM-based height analysis before and after IL-6 addition would be informative. Additionally, show CD spectra in the main text with clear evidence of a cooperative transition.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the E11− fluorescence wavelength shifts quantitatively with IL-6 concentration, with a detection limit of 80 nM and sensitivity up to 189 nM.
- **Evidence pointer** Results section "Fluorescence response of scFv-coupled QWNTs"; Figure 4A–4B
- **Concern** The spectral shift data are presented without statistical analysis. It is unclear how many independent experiments were performed, what the error bars represent, and whether the shifts are reproducible across different batches of QWNTs or scFv conjugations. The claim of a "quantitative" response requires a calibration curve with error estimates and a demonstration of batch-to-batch reproducibility. The detection limit of 80 nM is stated but the method for its determination (e.g., 3σ of blank) is not described.
- **Why it matters** For a sensor platform, the quantitative relationship between analyte concentration and signal is critical. Without statistical rigor, the reader cannot assess the reliability or precision of the measurement. The claim of a detection limit is a quantitative statement that requires a defined methodology.
- **Resolution test** Provide replicate measurements (at least n=3 independent experiments) with error bars on the calibration curve. State the method for determining the detection limit. Show the raw spectra for at least one titration series. Demonstrate reproducibility across at least two independent QWNT preparations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the spectral shift is specific to IL-6, as non-target proteins (BSA, TNF-α, TGFβ1) did not induce wavelength shifts.
- **Evidence pointer** Results section "Fluorescence response of scFv-coupled QWNTs"; Figure 4D
- **Concern** The specificity control is limited to three proteins at a single concentration. It is not clear whether these proteins were tested at concentrations comparable to the IL-6 concentrations used. Additionally, the effect of other cytokines or serum proteins that may be present at high concentrations in serum is not addressed. The claim of specificity is also complicated by the fact that the response is attributed to a folding transition, which could potentially be triggered by non-specific interactions with other proteins under certain conditions.
- **Why it matters** Specificity is a key requirement for a biosensor intended for use in complex biological media such as serum. If the sensor responds to other proteins at physiologically relevant concentrations, its utility is compromised.
- **Resolution test** Test a panel of cytokines and abundant serum proteins (e.g., albumin, immunoglobulins, transferrin) at concentrations spanning the physiological range. Include a negative control with a non-binding scFv conjugated to QWNTs. Show the response of the sensor in serum without spiked IL-6 to establish the baseline.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that quantum chemical modeling shows that the spectral shift is due to the electric field from the charged protein, and that the E11− peak is more sensitive than the E11 peak.
- **Evidence pointer** Results section "Quantum Chemical Modeling"; Figure 5
- **Concern** The computational model uses point charges at a fixed distance (1.41 nm) from the defect center, with charges varied from 0 to 1 e−. The justification for this distance and the number of charges is not provided. The model does not account for the actual charge distribution on the folded protein, the orientation of the protein relative to the nanotube, or the dielectric environment of the protein-nanotube interface. The claim that the model "supports" the experimental observations is therefore qualitative at best.
- **Why it matters** The modeling is used to provide a mechanistic explanation for the experimental observations. If the model is not representative of the physical system, the proposed mechanism remains speculative. The quantitative agreement between the modeled shift (~5.5 nm) and the experimental shift (up to 4 nm) is suggestive but not conclusive without a more realistic model.
- **Resolution test** Provide a more detailed description of the model, including justification for the charge placement and distance. Perform a sensitivity analysis varying the distance and number of charges. If possible, use a more realistic representation of the protein charge distribution (e.g., from a Poisson-Boltzmann calculation) and account for the dielectric environment.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that this work demonstrates a new approach to modulate quantum defect emission for biomarker sensing and to engineer proteins to modulate binding signal transduction.
- **Evidence pointer** Discussion section
- **Concern** While the concept is interesting, the demonstrated performance (detection limit 80 nM, dynamic range 0.08–10 μM) is modest compared to existing IL-6 detection methods, such as ELISA or other optical sensors, which can achieve picomolar or lower detection limits. The authors do not discuss how this approach compares to existing technologies or what specific advantages it offers beyond the novelty of the mechanism.
- **Why it matters** For the work to have significant impact, the authors need to articulate the practical advantages of this approach over existing methods. If the sensitivity is inferior, the value of the work lies primarily in the fundamental understanding of quantum defect photophysics, which should be stated more clearly.
- **Resolution test** Add a discussion comparing the analytical performance of this sensor to existing IL-6 detection methods. Clearly state whether the primary contribution is the fundamental mechanism or the practical sensor performance, and frame the claims accordingly.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Experimental Section "Supercharged scFv design"
- **Evidence pointer** Location not provided
- **Issue** The description of the disulfide bond removal states that cysteines were mutated to valine and alanine, but the text in the Results section says "valine and alanine" while the Experimental Section says "alanine-leucine pairs." This inconsistency is confusing.
- **Required correction** Reconcile the amino acid substitutions described in the Experimental Section and Results section.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results section "Design of signal-amplifying scFvs"
- **Evidence pointer** Figure 2B
- **Issue** The KD value for α-IL6wt is reported as 400 ± 100 nM, but the error is not defined (e.g., standard deviation, standard error, 95% confidence interval). The number of replicates is not stated.
- **Required correction** Define the error term and state the number of independent measurements.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results section "Fluorescence response of scFv-coupled QNTs"
- **Evidence pointer** Figure 4C
- **Issue** The time course for the spectral response shows saturation within 4 hours, but the kinetics are not analyzed. The authors attribute the slow response to screening by serum proteins and interactions with deoxycholate, but no experiments are shown to support this explanation.
- **Required correction** Either provide experimental evidence for the proposed explanation of the slow kinetics or temper the statement to acknowledge it as a hypothesis.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Results section "Fluorescence response of scFv-coupled QNTs"
- **Evidence pointer** Figure 4F
- **Issue** The comparison between α-IL6sc and α-IL6wt is described as showing a "much smaller shift" for α-IL6wt, but the actual values are not given in the text. The reader must infer the magnitude from the figure.
- **Required correction** State the numerical values of the shifts for both constructs in the text.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Experimental Section "Near-infrared fluorescence spectroscopy of scFv-QNTs"
- **Evidence pointer** Location not provided
- **Issue** The excitation wavelength is stated as 808 nm, but the emission spectra are fitted with Lorentzian functions. The fitting procedure, including the number of peaks fitted and the constraints applied, is not described.
- **Required correction** Provide details of the fitting procedure, including the number of peaks, initial parameters, and goodness-of-fit metrics.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section "Quantum Chemical Modeling"
- **Evidence pointer** Figure 5B
- **Issue** The placement of point charges at 1.41 nm from the defect center is described, but the direction of the charges relative to the nanotube axis is not specified. The figure is not available for inspection.
- **Required correction** Describe the geometry of the charge placement in the text, including the direction relative to the nanotube axis.

## Risk / unsupported claims
- The claim that α-IL6sc undergoes a "full" ligand-induced folding transition is not supported by direct structural evidence; the available data (CD, intrinsic tryptophan fluorescence) are indirect and not shown in full.
- The claim that the spectral shift is due to the electric field from the folded protein is supported only by a simplified point-charge model; the model parameters are not justified and the model is not experimentally validated.
- The claim of specificity for IL-6 is based on a limited set of control proteins at unspecified concentrations.
- The quantitative relationship between the folding free energy and binding affinity (Figure 2F) is based on solution measurements that may not reflect the surface-conjugated state of the protein on the QWNT.
- The detection limit of 80 nM is stated without a defined methodology for its determination.
- The long-term stability claim (1 week) is based on a single time point and does not address potential degradation mechanisms.
- The statement that the sensor can be implemented in underresourced settings is speculative and not supported by any data on cost, ease of use, or field performance.