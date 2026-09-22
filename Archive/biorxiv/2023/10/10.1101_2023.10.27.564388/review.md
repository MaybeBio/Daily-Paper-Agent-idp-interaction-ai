## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, acknowledgments) as provided
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims based solely on the supplied material
- **Shared manuscript claim summary** The authors report that short peptides derived from conserved motifs of tardigrade CAHS proteins are disordered in aqueous buffer but adopt α-helical conformations under desolvating conditions (TFE titration and air/water interface), whereas a control peptide from a non-CAHS protein does not. They propose that these peptides mimic the structural adaptability of full-length CAHS proteins and suggest arginine is a key residue for this behavior.
- **Visible evidence base** CD spectra (Fig. 1A, Fig. 2), FTIR spectra (Fig. 1B, Fig. S3), 2D-IR spectra (Fig. 1C-E, Fig. 3), SFG spectra (Fig. 4), molecular dynamics simulations (Fig. 1E-F, Fig. S2), peptide sequences (Table 1, referenced but not shown in provided text)
- **Missing materials affecting confidence** Table 1 (peptide sequences) not provided; supplementary figures (Fig. S1-S3) not provided; full 2D-IR spectra for all peptides except CAHS11aa not shown in main text; no quantitative fitting parameters for CD or SFG spectra in the provided text; no error bars or statistical analysis reported; no raw data or reproducibility metrics

## Reviewer
- **Overall assessment** The manuscript addresses a timely and potentially useful question: whether short peptides derived from conserved tardigrade CAHS motifs can recapitulate the desiccation-induced structural transitions of the full-length proteins. The experimental approach combining CD, FTIR, 2D-IR, and SFG is appropriate and complementary. However, the evidence as presented is incomplete in several respects. The central claim that these peptides "mimic" full-length CAHS protein behavior rests on qualitative spectral comparisons without quantitative structural characterization. The role of arginine is presented as a hypothesis but is not tested experimentally. The control peptide choice is reasonable but its lack of surface activity is reported without concentration-dependent studies. The manuscript would benefit from clearer quantitative analysis and additional controls to substantiate the conclusions.
- **Who would be interested in the results, and why** Researchers in the fields of biomimetic materials, peptide self-assembly, desiccation tolerance mechanisms, and biopreservation. The work could inform the design of synthetic peptides for stabilizing sensitive biologics, which is of interest to the pharmaceutical and biotechnology communities. The methodological combination of linear and nonlinear spectroscopies may also appeal to biophysical chemists studying peptide structure at interfaces.
- **Major strengths** The combination of multiple spectroscopic techniques (CD, FTIR, 2D-IR, SFG) provides complementary views of peptide structure in bulk and at interfaces. The use of a non-CAHS control peptide is a thoughtful experimental design. The molecular dynamics simulations add a computational perspective that supports the experimental findings. The study addresses a practical application (biopreservation) with clear relevance.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative structural assignment), R1-M2 (arginine hypothesis untested), R1-M3 (control peptide surface activity not concentration-dependent), R1-M4 (SFG spectral interpretation)
- **Assessment against Nature-style criteria** Originality: moderate. While the application of CAHS-derived peptides is relatively novel, the general concept of desiccation-induced helix formation in peptides is known. Scientific importance: potentially high if the cytoprotective function can be demonstrated, but the current manuscript does not establish this. Interdisciplinary readership: the topic bridges biophysics, materials science, and biology, which could attract a broad audience. Technical soundness: the spectroscopic methods are appropriate, but the analysis is largely qualitative and lacks quantitative rigor. Readability for nonspecialists: the manuscript is generally clear, though some spectroscopic details may be dense for a general audience. Overall, the manuscript does not yet meet the standard for a high-impact general journal.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising, but the evidence base needs strengthening with quantitative analysis, additional controls, and direct testing of the proposed arginine hypothesis.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors claim that CAHS model peptides are "mostly disordered at 0% TFE" and "adopt a more α-helical structure upon the addition of the desolvating agent," and that this behavior is "similar to what is observed for full CAHS proteins."
- **Evidence pointer** Fig. 1A-D, Fig. 2, Fig. 3A-B
- **Concern** The structural assignments are based on qualitative inspection of CD and 2D-IR spectral shapes. No quantitative deconvolution of CD spectra (e.g., using reference databases such as DichroWeb or BeStSel) is reported. The 2D-IR diagonal slices show band shifts, but the assignment of the 1655 cm⁻¹ band to α-helix is inferred from a single literature reference on LEA proteins, not from independent calibration. The claim that the peptides "adopt a more α-helical structure" requires quantitative estimates of helical content (e.g., mean residue ellipticity at 222 nm) and ideally corroboration from a second structural method (e.g., NMR or vibrational circular dichroism).
- **Why it matters** The central conclusion of the manuscript, that these peptides mimic the structural behavior of full-length CAHS proteins, depends on accurate structural assignment. Without quantitative analysis, the reader cannot assess the magnitude of the structural change or compare it to the full-length protein behavior.
- **Resolution test** Provide quantitative secondary structure estimates from CD deconvolution for all peptides at each TFE concentration. Report mean residue ellipticity values at key wavelengths. For 2D-IR, provide a calibration of the amide I band positions using model peptides of known structure, or support the assignment with additional spectroscopic evidence.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The authors state that "arginine might be a crucial element in defining the strong propensity of these peptides to adopt a helical structure" and suggest this as a design rule for future peptides.
- **Evidence pointer** Discussion section, peptide sequences (Table 1, not provided)
- **Concern** The arginine hypothesis is based solely on sequence comparison between the CAHS-derived peptides and the control. No experiments are performed to test this hypothesis, such as alanine scanning, arginine-to-lysine substitution, or testing of additional peptides with varying arginine content. The correlation between arginine presence and helix propensity is not established quantitatively, and other sequence features (e.g., charge patterning, hydrophobicity) are not controlled for.
- **Why it matters** The proposed design rule is a key take-home message of the manuscript. If it is not supported by direct evidence, it should be presented as a speculative observation rather than a conclusion. Overstating this claim could mislead future peptide design efforts.
- **Resolution test** Perform mutagenesis or design additional peptides with systematic arginine variations and measure their helix propensity under desolvating conditions. Alternatively, rephrase the claim as a hypothesis requiring further testing and remove it from the conclusions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Experimental design
- **Claim pointer** The authors report that the control peptide "does not display interfacial activity at the measured concentration, yielding a spectrum indistinguishable from buffer subphase."
- **Evidence pointer** Fig. 4
- **Concern** The lack of surface activity for the control peptide is reported at a single concentration (0.09 mg/mL). It is possible that the control peptide is surface-active at higher concentrations, or that the absence of signal is due to slow adsorption kinetics rather than intrinsic inability to adsorb. No surface pressure measurements or concentration-dependent SFG studies are provided.
- **Why it matters** The contrast between CAHS peptides and the control at the interface is used to support the claim that CAHS-derived sequences have unique surface activity. Without concentration-dependent data, this conclusion is premature.
- **Resolution test** Measure SFG spectra and surface pressure as a function of peptide concentration for both CAHS and control peptides. If the control remains inactive at all concentrations tested, the claim is strengthened.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation
- **Claim pointer** The authors assign the SFG peak at ~1645 cm⁻¹ to α-helical structure at the air/water interface and the mode at ~1720 cm⁻¹ to protonated glutamic and aspartic acid side chains.
- **Evidence pointer** Fig. 4
- **Concern** The assignment of the 1645 cm⁻¹ peak to α-helix at the interface is not rigorously justified. SFG spectra of peptides at interfaces can be influenced by orientation effects, and the amide I frequency can shift due to the hydrophobic environment. The 1720 cm⁻¹ assignment to side-chain carbonyls is plausible but not verified, for example by isotope labeling or pH-dependent measurements.
- **Why it matters** The interfacial structure is a key finding of the manuscript. Misassignment of spectral features would undermine the conclusion that the peptides adopt helical conformations at the interface.
- **Resolution test** Provide additional evidence for the assignments, such as SFG spectra of model helical peptides at the interface, or pH-dependent SFG measurements to confirm the side-chain carbonyl assignment.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section, peptide synthesis
- **Evidence pointer** Materials and Methods, peptide synthesis
- **Issue** The synthesis description for CAHS11aa and CAHS22aa is detailed, but the source and purity of CAHS1M1, CAHS1M2, and SAHS1C3 are only stated as "purchased via custom peptide synthesis" with 95% purity. No information is given on the counterion (e.g., TFA) or on verification of peptide identity (e.g., mass spectrometry).
- **Required correction** Provide details on peptide characterization (e.g., HPLC trace, mass spec) and note whether TFA removal was performed, as TFA absorbs in the amide I region and could interfere with IR measurements.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, bulk structure
- **Evidence pointer** Fig. 1A
- **Issue** The CD spectrum of CAHS1M1 is described as showing "a positive signal at 190 nm, followed by two negative peaks around 210 and 225 nm," which is stated to indicate α-helical structure. However, the typical α-helical CD spectrum has a positive peak near 190 nm and negative peaks near 208 and 222 nm. The reported 225 nm peak is slightly red-shifted from the canonical 222 nm, which is not discussed.
- **Required correction** Address the slight discrepancy in peak position or provide a reference for the assignment.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** All figures
- **Evidence pointer** Fig. 1-4
- **Issue** No error bars, standard deviations, or replicate numbers are reported for any of the spectroscopic measurements. It is unclear whether the spectra are representative single measurements or averages.
- **Required correction** Report the number of replicates and include error estimates or at least state that spectra are representative of at least three independent measurements.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion
- **Evidence pointer** Discussion and conclusion
- **Issue** The statement "we hypothesize that arginine is crucial to ensure the coil-to-helical transition" is presented in the conclusion, but the preceding discussion does not provide a mechanistic rationale for why arginine would be crucial. The reader is left to infer the basis for this hypothesis.
- **Required correction** Provide a brief mechanistic explanation, such as arginine's hydrogen-bonding capacity or its role in stabilizing helix macrodipoles, to make the hypothesis more compelling.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, molecular dynamics
- **Evidence pointer** Fig. 1E-F, Fig. S2
- **Issue** The molecular dynamics simulations are described only briefly. It is unclear what force field parameters were used for TFE, how the simulations were validated, and whether the simulation times were sufficient for convergence of secondary structure populations.
- **Required correction** Provide additional simulation details, including force field parameters, simulation length, and convergence criteria.

## Risk / unsupported claims
- The claim that the peptides "show similarities in the physicochemical behavior to full CAHS proteins" is not directly supported by experiments comparing the peptides to the full-length proteins under identical conditions.
- The claim that "arginine might be a crucial element" is speculative and not tested experimentally.
- The claim that the peptides adopt "a helical structure at the air/water interface" is based on a single SFG peak assignment without independent verification.
- The statement that the selected peptides "represent promising model peptides" for future applications is forward-looking and not supported by functional assays in this manuscript.
- The assertion that the control peptide "does not show any surface activity" is based on a single concentration and cannot be generalized.