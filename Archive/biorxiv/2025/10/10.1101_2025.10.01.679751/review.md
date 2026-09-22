## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusions, methods) as provided. Supplementary figures are referenced but not provided.
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by the presented evidence. No assessment of formatting, grammar, or editorial style beyond readability.
- **Shared manuscript claim summary** The authors use MD simulations with alchemical free energy transformations and DFT calculations to show that Arg is consistently a stronger "sticker" than Lys in biomolecular condensates across different dielectric environments, and that this hierarchy is primarily driven by the higher dehydration penalty of Lys rather than by intrinsic cation–π interaction strengths. They also show that the preferred aromatic partner (Phe vs Tyr) for cation–π interactions depends on the dielectric environment.
- **Visible evidence base** Main text Figures 1–6 (described in text), Methods section, and references to Supplementary Figures S1–S11. The supplementary material itself was not provided for review.
- **Missing materials affecting confidence** Supplementary Information (Figures S1–S11, Table S1), which contains convergence data, additional conformational analysis, validation of solvation models, and additional DFT results. Also missing are simulation input files, force field parameters, and analysis scripts.

## Reviewer

### Overall assessment
This manuscript addresses a timely and important question in the field of biomolecular condensates: the molecular origin of the experimentally observed hierarchy between Arg and Lys as stickers. The combination of alchemical free energy calculations and DFT is appropriate and potentially powerful. The central claim, that the dehydration penalty of Lys rather than intrinsic interaction strength drives the Arg > Lys hierarchy, is mechanistically interesting and would be of broad interest. However, the manuscript as presented has several issues that prevent full confidence in the conclusions. The most significant concerns are the lack of convergence analysis for the alchemical transformations (deferred to SI), the use of a simplified peptide model without validation against longer sequences, the treatment of the condensate environment as a homogeneous dielectric in the DFT calculations, and the absence of error estimates for the DFT interaction energies. The distinction between "interaction energy" and "contact energy" is conceptually important but the presentation of these quantities in the main text is at times confusing. The manuscript would be substantially strengthened by presenting key convergence data in the main text and by a more careful discussion of the limitations of the implicit solvent model.

### Who would be interested in the results, and why
Researchers working on biomolecular condensates and phase separation, particularly those interested in sequence determinants of phase behaviour. The results are also relevant to the broader community studying cation–π interactions in proteins, including computational chemists and biophysicists interested in force field development and solvation effects. The finding that dehydration penalties can dominate over intrinsic interaction strengths has implications for understanding molecular recognition in confined and partially dehydrated environments.

### Major Strengths
1. The question addressed is of clear importance and the experimental hierarchy (Arg > Lys) is well established, making the computational investigation timely and relevant.
2. The combination of alchemical free energy calculations and DFT is methodologically appropriate and complementary.
3. The conceptual distinction between intrinsic interaction energy and contact energy (which includes transfer penalties) is valuable and provides a clear mechanistic framework.
4. The authors are appropriately cautious about the limitations of classical force fields for cation–π interactions and justify their use of DFT.
5. The finding that the aromatic partner preference depends on dielectric environment is novel and interesting.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that ΔΔG_Transfer is negative in both GSF and GSY condensates, indicating Arg is favoured over Lys, with values of approximately 5 ± 2 kJ/mol.
- **Evidence pointer** Figure 2C, Methods section "Molecular simulations", SI Figure S4 (referenced)
- **Concern** The alchemical free energy calculations are the cornerstone of the manuscript, yet no convergence analysis is presented in the main text. The authors state that boxes take up to 500 ns to equilibrate and that they exclude the first 500 ns, but no information is provided about the number of switches, the length of the switches, the statistical uncertainty of the free energy estimates, or the convergence of the Bennett acceptance ratio estimates. The error bar of ±2 kJ/mol is mentioned but its origin is not described. For a claim of this importance, convergence data must be shown in the main text or the claim cannot be properly evaluated.
- **Why it matters** Free energy estimates from non-equilibrium switching are only reliable if the switches are sufficiently slow and the sampling is converged. Without this information, the central quantitative claim of the paper is not verifiable.
- **Resolution test** Present the convergence of the free energy estimates as a function of the number of switches, the distribution of work values, and the statistical error bars in the main text. Show that the results are robust to the choice of the equilibration time and the number of switches.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that the DFT calculations with implicit solvation provide quantitatively reliable contact energies, and that the trends in ΔE_contact across dielectric values support the conclusion that dehydration penalties dominate.
- **Evidence pointer** Methods section "Quantum chemical calculations", Figures 5 and 6, SI Figures S10 and S11 (referenced)
- **Concern** The DFT calculations use a continuum solvent model with a single dielectric constant to represent the condensate environment. The authors justify this by citing their previous work, but the condensate is a heterogeneous, partially dehydrated environment, not a homogeneous dielectric. The use of a single ε value for the entire condensate is a significant approximation that is not discussed in sufficient depth. Furthermore, the validation of the SMD solvation model is only presented for neutral molecules in water and cyclohexane, and for charged mimics in water. No validation is shown for the transfer between water and the intermediate-dielectric solvents that are most relevant to the condensate environment. The authors also do not discuss the known limitations of continuum solvation models for charged species, particularly the treatment of ion pairing and the lack of explicit hydrogen bonding.
- **Why it matters** The central mechanistic conclusion, that dehydration penalties rather than intrinsic interaction strengths drive the Arg > Lys hierarchy, depends critically on the reliability of the solvation free energies. If the solvation model is inaccurate for charged species in intermediate-dielectric environments, the conclusion may be an artifact of the model.
- **Resolution test** Provide additional validation of the SMD model for charged species in intermediate-dielectric solvents, or discuss the known limitations more thoroughly. Consider performing test calculations with explicit solvent or with a more sophisticated treatment of the environment to assess the robustness of the conclusions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The claim that the results "provide a clear molecular-level explanation for the distinct contributions of interactions between cationic and aromatic residues to condensate stability."
- **Evidence pointer** Conclusions section, Abstract
- **Concern** The manuscript uses a minimal model system: a pentapeptide GGXGG in a condensate formed by capped Gly, Ser, and Phe or Tyr. While this is a reasonable starting point, the authors do not discuss how their results might transfer to real condensate-forming sequences, which contain multiple Arg and Lys residues in diverse sequence contexts. The claim that this provides a "clear molecular-level explanation" for condensate behaviour is somewhat overstated given the simplicity of the model. The authors do acknowledge this limitation in the Conclusions, but the framing in the Abstract and Introduction is more assertive.
- **Why it matters** The broader significance of the work depends on the extent to which the findings from the minimal model can be extrapolated to real systems. If the hierarchy is context-dependent in more complex sequences, the conclusions would need to be qualified.
- **Resolution test** Add a more detailed discussion of the limitations of the minimal model and how the results might be tested in more complex systems. Alternatively, perform additional simulations with a more complex peptide sequence to test the robustness of the findings.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The claim that the MD simulations show a "clear propensity to form stacked arrangements between the Tyr/Phe and Arg sidechains" and that this supports a role for π-stacked interactions.
- **Evidence pointer** Figure 4, SI Figures S6 and S7 (referenced)
- **Concern** The analysis of stacking propensity is based on geometric criteria (distance and angle between ring planes), but the authors do not provide a quantitative comparison with a reference state. It is not clear whether the observed stacking propensity is significantly different from what would be expected by chance given the density of the condensate. The authors also do not report the fraction of time spent in stacked configurations or the free energy of the stacked state relative to other configurations.
- **Why it matters** The claim that stacking is a preferred interaction mode is used to support the interpretation of the DFT results. Without a proper statistical analysis, this claim is not well supported.
- **Resolution test** Provide a comparison of the observed stacking frequencies with a reference distribution (e.g., from a simulation with randomized interactions or from the unbound state). Report the fraction of time in stacked configurations and the associated uncertainties.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Results section, subsection "Alchemical transformations reproduce the experimental hierarchy of sticker strengths"
- **Evidence pointer** Figure 2C
- **Issue** The notation for the free energy differences is inconsistent. The text uses ΔΔG_Transfer, ΔG_K→R, and other symbols without a clear definition of the sign convention. The reader must infer from context whether a negative value means Arg is favoured or disfavoured.
- **Required correction** Define all free energy symbols explicitly in the text or in a table, including the sign convention, and use them consistently throughout.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods section, "Molecular simulations"
- **Evidence pointer** Methods, "Molecular simulations" paragraph
- **Issue** The authors state that they used the Amber99SB*-ILDN force field but do not specify the water model used for the condensate simulations. They mention TIP3P for simulations including water molecules, but it is unclear whether the condensate simulations also use TIP3P or a different model.
- **Required correction** Specify the water model used in the condensate simulations and any other relevant simulation parameters (e.g., temperature, pressure coupling).

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability
- **Affected element** Results section, subsection "Context independence of Arg and Lys transfer free energies"
- **Evidence pointer** Figure 3
- **Issue** The text states that "we cannot establish a systematic dependence of ΔΔG_Transfer on ε" but the figure appears to show a trend. The authors should either quantify the lack of correlation or explain why the apparent trend is not considered systematic.
- **Required correction** Provide a quantitative analysis of the relationship between ΔΔG_Transfer and ε, or clarify the statement.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods section, "Quantum chemical calculations"
- **Evidence pointer** Methods, "Quantum chemical calculations" paragraph
- **Issue** The authors state that they used the ωB97XD functional and the 6-311++G(d,p) basis set for geometry optimization, but do not specify the level of theory used for the single-point energy calculations or the calculation of solvation free energies. The SMD calculations are mentioned as using B3LYP/6-31+G(d,p), but it is unclear whether the interaction energies are calculated at the same level.
- **Required correction** Specify the level of theory for all calculations, including single-point energies and solvation free energies.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability
- **Affected element** Results section, subsection "Permutation of cationic and aromatic residues"
- **Evidence pointer** Figure 6B
- **Issue** The text describes a "crossover" in the preference between Arg and Lys as a function of dielectric, but the figure is not clear about the exact location of this crossover. The authors should indicate the crossover point more explicitly.
- **Required correction** Add a marker or annotation to the figure to indicate the crossover point, or describe it more precisely in the text.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract
- **Evidence pointer** Abstract, last sentence
- **Issue** The abstract states that the results "provide a clear molecular-level explanation" but the manuscript itself is more cautious. The abstract should be consistent with the level of confidence expressed in the main text.
- **Required correction** Soften the language in the abstract to match the qualifications in the main text.

### Technical failings that need to be addressed before the case is established
1. Lack of convergence analysis for alchemical free energy calculations (R1-M1).
2. Insufficient validation of the implicit solvation model for charged species in intermediate-dielectric environments (R1-M2).
3. No statistical analysis of stacking propensity in MD simulations (R1-M4).

### Assessment against Nature-style criteria
- **Originality**: The work is original in its systematic comparison of Arg vs Lys in the context of condensates, and the emphasis on dehydration penalties as the dominant factor is a valuable contribution. The finding that the aromatic partner preference is dielectric-dependent is novel.
- **Scientific importance**: The question of what determines sticker strength in condensates is of central importance to the field. The results have implications for understanding sequence-encoded phase behaviour and for the design of condensate-modulating mutations.
- **Interdisciplinary readership**: The work bridges physical chemistry, biophysics, and cell biology. The concepts are accessible, but the presentation of the free energy calculations may be challenging for non-specialists.
- **Technical soundness**: The combination of methods is appropriate, but the lack of convergence data and the limitations of the implicit solvent model are significant concerns that must be addressed.
- **Readability for nonspecialists**: The manuscript is generally well written, but the free energy notation and the distinction between interaction and contact energies could be explained more clearly.

### Recommendation posture
Supportive if technical concerns are resolved. The central question is important, the approach is appropriate, and the conclusions are potentially significant. However, the lack of convergence data for the alchemical calculations and the insufficient validation of the solvation model prevent full confidence in the quantitative claims. The manuscript would be suitable for publication in a high-impact journal after these issues are addressed.

## Risk / unsupported claims
1. The claim that ΔΔG_Transfer is approximately 5 ± 2 kJ/mol is not verifiable without convergence data and error analysis.
2. The claim that the DFT calculations provide quantitatively reliable contact energies in condensate-like environments is not fully supported, given the limited validation of the solvation model.
3. The claim that the MD simulations show a "clear propensity" for stacked arrangements is not quantitatively supported.
4. The extrapolation from the minimal peptide model to real condensate-forming sequences is not discussed in sufficient depth to assess its validity.