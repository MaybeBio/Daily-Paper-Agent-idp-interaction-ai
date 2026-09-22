## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusions, methods) as provided
- **Assessment boundary** Scientific claims, methodological soundness, and interpretation of results as presented in the provided text; no external data or supplementary figures were available for independent verification
- **Shared manuscript claim summary** The authors combine label-free optical spectroscopies (UV-resonance Raman, confocal Raman, THz-TDS, SRS) with deep-learning-based ensemble prediction (STARLING) to characterize the conformational and chemical properties of DDX4[1-245] condensates. They report chain collapse correlating with phase separation, reduced dielectric constant inside condensates, and reduced water content, proposing a positive feedback model for phase separation driven by these factors.
- **Visible evidence base** Figures 1–5 (referenced but not shown), Tables S1–S2 (referenced but not shown), Figures S1–S9 (referenced but not shown), Methods section, Discussion section
- **Missing materials affecting confidence** All figures and supplementary tables were not provided; raw data, fitting parameters, and statistical analyses were not accessible; details of the constrained Debye model fitting and SRS quantification were incomplete

## Reviewer
- **Overall assessment** This manuscript addresses a significant and timely question in the field of biomolecular condensates: the quantitative characterization of intra-condensate chemical and physical properties using non-perturbative methods. The combination of multiple label-free optical techniques with computational ensemble prediction is innovative and potentially impactful. However, the current version has several technical concerns that need to be addressed before the central claims can be fully established. The interpretation of the DLS data, the quantitative accuracy of the THz dielectric measurements, and the SRS water content quantification require additional scrutiny and supporting evidence.
- **Who would be interested in the results, and why** Researchers in the fields of phase separation, intrinsically disordered proteins, biophysical chemistry, and cellular organization would find these results of interest. The methodological advances in applying THz-TDS and SRS to condensate systems could also appeal to the broader spectroscopy and imaging communities. The proposed model of chain collapse, reduced dielectric, and water release as driving forces for phase separation has implications for understanding condensate biology and for designing synthetic condensates.
- **Major strengths** 1) The use of multiple complementary label-free techniques to probe condensate properties is a significant methodological advance. 2) The integration of experimental measurements with deep-learning-based ensemble prediction provides a multi-scale perspective. 3) The direct measurement of reduced dielectric constant inside condensates using THz-TDS is novel. 4) The proposed positive feedback model is conceptually appealing and testable.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (DLS interpretation), R1-M2 (THz dielectric quantification), R1-M3 (SRS water content quantification)
- **Assessment against Nature-style criteria** **Originality**: High. The application of THz-TDS to directly measure dielectric properties of condensates is novel, and the combination of techniques is unique. **Scientific importance**: High. Understanding the physical chemistry of condensate interiors is a central question in the field. **Interdisciplinary readership**: Moderate to high. The work bridges biophysics, physical chemistry, and cell biology. **Technical soundness**: Currently insufficient. Several key quantitative claims require additional validation and controls. **Readability for nonspecialists**: Good. The manuscript is generally well-written and accessible, though some technical details could be clarified.
- **Recommendation posture** Supportive if technical concerns are resolved. The core concept and methodological approach are promising, but the quantitative claims require additional evidence and analysis.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data interpretation
- **Claim pointer** "we observed a distinct protein population with dramatically reduced apparent ⟨Rh⟩ = 1.6 ± 0.2 nm" and "the appearance of a new, highly compact DDX4[1-245] monomer population correlates strongly with DDX4[1-245] phase separation"
- **Evidence pointer** Figure 3, location not provided
- **Concern** The DLS data interpretation is not fully convincing. The authors attribute the 1.6 nm species to a collapsed monomer, but the polydispersity of the sample and the potential presence of oligomers or clusters could complicate this assignment. The width of the size distribution and the fitting model used to extract ⟨Rh⟩ are not described in sufficient detail. Additionally, the claim that this collapsed state "correlates strongly with phase separation" is based on a limited set of conditions (temperature, concentration, ionic strength), and the correlation is not quantitatively established.
- **Why it matters** The identification of a collapsed monomer state is a central claim of the manuscript. If this assignment is incorrect or the correlation is not robust, the proposed model of chain collapse driving phase separation is weakened.
- **Resolution test** Provide a detailed description of the DLS data analysis, including the autocorrelation function fitting model, the regularization method, and the criteria for distinguishing monomer, oligomer, and cluster populations. Show the full size distribution profiles for all conditions tested, and provide a quantitative measure of the correlation between the collapsed state population and phase separation (e.g., a phase diagram overlay). Consider performing concentration-dependent DLS to rule out concentration-dependent oligomerization.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative accuracy
- **Claim pointer** "the condensed phase static dielectric constant (εscondensed,H2O=67±6 and εscondensed,D2O=49±2) was significantly reduced relative to the dilute phase"
- **Evidence pointer** Figure 4, Tables S1–S2, location not provided
- **Concern** The quantitative accuracy of the THz-TDS dielectric measurements is not fully established. The authors acknowledge that the static dielectric constant is overestimated for H2O and underestimated for D2O relative to literature values, but the impact of these systematic errors on the reported condensed phase values is not discussed. The constrained Debye model fitting procedure, including the choice of fixed parameters and the sensitivity of the results to these constraints, is not described in sufficient detail. The potential contribution of scattering from condensate droplets to the THz spectra is not addressed.
- **Why it matters** The reduced dielectric constant inside condensates is a key quantitative claim. If the measurement is not accurate or the fitting model is not robust, the magnitude of the reported reduction may be incorrect, affecting the interpretation of its role in strengthening protein-protein interactions.
- **Resolution test** Provide a detailed description of the Debye model fitting procedure, including the constraints applied, the uncertainty analysis, and the goodness-of-fit metrics. Discuss the potential systematic errors in the measurement and their impact on the reported values. Address the potential contribution of scattering to the THz spectra, possibly by measuring at multiple sample thicknesses or using a scattering correction model. Validate the approach on a well-characterized system (e.g., a protein solution of known dielectric properties).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative accuracy
- **Claim pointer** "water content within the condensate core was ~2.5% lower compared to bulk, while water content at condensate perimeters was ~4% lower"
- **Evidence pointer** Figure 5, location not provided
- **Concern** The quantification of water content using SRS is not fully described. The calibration procedure for converting SRS signal intensity to absolute water concentration is not provided. The potential contribution of protein CH3 signal to the OH stretching channel, and vice versa, is not discussed. The spatial resolution and the potential for out-of-focus contributions to the SRS signal are not addressed. The authors report a small reduction in water content (2.5-4%), which is within the range of potential systematic errors.
- **Why it matters** The quantification of water release is a central claim of the manuscript. If the SRS measurements are not accurately calibrated or are subject to systematic errors, the reported water content reduction may not be reliable.
- **Resolution test** Provide a detailed description of the SRS calibration procedure, including the use of standard solutions and the correction for cross-phase modulation. Discuss the potential spectral overlap between protein and water signals and how it was addressed. Provide an estimate of the measurement uncertainty and demonstrate that the reported differences are statistically significant. Consider performing SRS imaging at multiple focal planes to assess out-of-focus contributions.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods, THz spectroscopy
- **Evidence pointer** Methods section, location not provided
- **Issue** The description of the THz-TDS setup and data processing is brief. The authors state that the complex refractive index was extracted "as previously described" but do not provide sufficient detail for reproducibility.
- **Required correction** Expand the Methods section to include a more detailed description of the THz-TDS setup, including the generation and detection scheme, the sample cell geometry, and the data processing steps. Provide a reference to the previous work or include the relevant equations.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, UV-resonance Raman
- **Evidence pointer** Figure 2, location not provided
- **Issue** The interpretation of the UV-resonance Raman data is somewhat qualitative. The authors state that the presence of a band at 1300 cm−1 suggests deviation from random coil behavior, but the assignment of this band and its quantitative relationship to conformational preferences are not fully explained.
- **Required correction** Provide a more detailed discussion of the UV-resonance Raman band assignments and how the presence of the 1300 cm−1 band is interpreted in terms of specific conformational features. Consider providing a quantitative comparison of the Raman spectra with simulated spectra from the STARLING ensembles.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, STARLING predictions
- **Evidence pointer** Figures S4–S5, location not provided
- **Issue** The STARLING predictions are used to support the interpretation of intramolecular interactions, but the specific interaction types (e.g., cation-π, π-π, electrostatic) are not directly quantified. The authors state that the mutants show "a substantial reduction of interactions" but do not provide a detailed analysis of which interactions are most affected.
- **Required correction** Provide a more detailed analysis of the STARLING ensembles, including contact maps or interaction energy decompositions, to identify the specific types of interactions that are altered in the mutants.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion, D2O isotope effect
- **Evidence pointer** Discussion section, location not provided
- **Issue** The discussion of the D2O isotope effect on phase separation is brief and somewhat speculative. The authors mention that D2O strengthens hydrogen bonds but do not provide a quantitative framework for how this would affect the phase diagram.
- **Required correction** Expand the discussion of the D2O isotope effect, considering both the thermodynamic and kinetic implications. If possible, provide a quantitative estimate of the expected shift in the phase boundary based on the measured dielectric and water content differences.

## Risk / unsupported claims
- The claim that the collapsed monomer state is a "previously unreported" species is not fully supported, as the authors do not provide a comprehensive literature search or comparison with prior observations of compact states in IDPs.
- The claim that the reduction in dielectric constant and water content "enhance the strength of multivalent protein-protein interactions" is inferred from the data but not directly tested. The proposed positive feedback model is speculative and requires further experimental validation.
- The quantitative relationship between the measured reduction in dielectric constant and the predicted increase in cation-π interaction strength is based on a single computational reference and may not be generalizable.
- The claim that the SRS measurements quantify "water release" is not fully supported, as the measurements report water content, not the dynamic process of water release. The authors should clarify this distinction.