## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) with figure references but no figure files or supplementary materials.
- **Assessment boundary** Scientific claims, methodological soundness, and internal consistency of the reported results and their interpretation. No assessment of data availability, code functionality, or reproducibility beyond what is described in the text.
- **Shared manuscript claim summary** The authors use molecular dynamics simulations and quantum chemistry calculations to explain why tyrosine acts as a stronger sticker than phenylalanine in biomolecular condensates, despite phenylalanine being more hydrophobic. They propose that the crossover in interaction strength depends on the dielectric environment, with phenylalanine favored in low-dielectric media and tyrosine favored in high-dielectric media.
- **Visible evidence base** Text descriptions of simulation protocols, thermodynamic cycle, analysis methods, and quantitative results (e.g., ΔΔGTransfer values, dielectric constants, phase diagram features). Figure references are present but figures themselves are not provided.
- **Missing materials affecting confidence** Figures, figure supplements, supplementary files, and tables referenced in the text are not available. This limits verification of quantitative claims, simulation convergence, and the quality of fits (e.g., phase diagram extraction, density profiles).

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question in the field of biomolecular condensates: the molecular origin of the differential sticker strength between tyrosine and phenylalanine. The authors combine classical MD simulations with quantum chemical calculations to propose a mechanistic explanation based on the dielectric environment. The central claim, that a crossover in interaction strength occurs as a function of medium polarity, is conceptually interesting and potentially impactful. However, the evidence presented in the text alone is insufficient to fully establish this claim. Key quantitative results are described but not shown, and the connection between the model systems and real condensates requires further justification. The manuscript is well-written and the logical flow is clear, but the technical depth and validation are not fully visible from the provided material.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, intrinsically disordered proteins, and the physical chemistry of amino acid interactions. The work is also relevant to those developing coarse-grained or atomistic models for condensate behavior, as it highlights the importance of environment-dependent interaction strengths. The crossover concept may interest a broader physical chemistry audience concerned with solvation effects on molecular interactions.
- **Major strengths** The manuscript addresses a clear and important paradox in the field. The combination of classical and quantum methods is appropriate and complementary. The thermodynamic cycle approach for computing transfer free energies is rigorous. The authors explicitly consider the role of the environment (dielectric constant) in modulating interaction strength, which is a nuanced and valuable perspective. The writing is clear and the logical structure is easy to follow.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (lack of visible quantitative evidence), R1-M2 (model system representativeness), R1-M3 (force field sensitivity), R1-M4 (quantum method validation).
- **Assessment against Nature-style criteria**  
  *Originality*: The question is important and the proposed crossover mechanism is novel, though related ideas exist in the literature on hydrophobicity. The specific application to Tyr/Phe in condensates is original.  
  *Scientific importance*: High, as it addresses a fundamental question about the molecular determinants of condensate formation, with implications for understanding sequence-encoded phase behavior.  
  *Interdisciplinary readership*: Moderate to high. The topic bridges biophysics, physical chemistry, and cell biology. The conceptual message about environment-dependent interactions should be accessible to a broad audience.  
  *Technical soundness*: The methods are appropriate in principle, but the lack of visible data and the limited validation of the model systems prevent a full assessment. The sensitivity to force field and quantum method choices is a concern.  
  *Readability for nonspecialists*: The manuscript is generally well-written and the main message is clear. However, some technical details (e.g., the thermodynamic cycle, dielectric constant calculations) may be challenging for nonspecialists without additional context.
- **Recommendation posture** Supportive if technical concerns are resolved. The central idea is promising and the methodology is appropriate, but the evidence as presented is not fully convincing. The authors should provide the missing quantitative data, address the representativeness of their model systems, and discuss the robustness of their conclusions to methodological choices.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The manuscript reports specific quantitative results, including ΔΔGTransfer values (e.g., -2.9 ± 0.5 kJ/mol for GSY, -2.5 ± 0.5 kJ/mol for GSF, 13.2 ± 0.3 kJ/mol for cyclohexane) and dielectric constants for condensates (30-50), but these are only described in text.  
- **Evidence pointer** Results section, Figures 3, 6, and associated supplements (figures not provided)  
- **Concern** The central quantitative claims are not verifiable from the provided material. The text describes results but the actual data (plots, distributions, fits) are not shown. This is particularly problematic for the phase diagram extraction (Figure 5C), the dielectric constant calculations, and the transfer free energy estimates, where the quality of the data and the fitting procedures are critical.  
- **Why it matters** Without the actual data, it is impossible to assess the statistical significance, the convergence of the simulations, or the robustness of the reported values. The reader cannot evaluate whether the small differences in ΔΔGTransfer (e.g., -2.9 vs -2.5 kJ/mol) are meaningful or within error.  
- **Resolution test** Provide the figures and supplementary data. Include error bars, convergence tests, and details of the fitting procedures. Show the actual distributions of work values from the non-equilibrium switching simulations and the density profiles used for phase diagram extraction.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Model system representativeness  
- **Claim pointer** The authors use GGXGG pentapeptides and dipeptide condensates (GSY, GSF) as models for biomolecular condensates, and extrapolate their findings to full-length IDRs.  
- **Evidence pointer** Methods (Molecular models), Results (Transfer free energies into a condensate slab)  
- **Concern** The model systems are extremely simplified compared to real condensates. The authors acknowledge this limitation, but the extrapolation from dipeptide condensates to full-length IDRs is a large leap. The density of the condensates, the local environment around the stickers, and the multivalency effects are all different. The claim that "biomolecular condensates... operate in the second regime" (high dielectric) is based on these simplified models.  
- **Why it matters** The central conclusion about the crossover in interaction strength is meant to explain experimental observations in real condensates. If the model systems do not capture the essential physics of real condensates, the conclusions may not be transferable. The authors need to justify why the dipeptide condensate is a good proxy for the environment in full-length IDR condensates.  
- **Resolution test** Discuss the limitations more thoroughly. Compare the density and dielectric constant of the model condensates to those of real condensates. If possible, perform a test with a longer peptide or a more realistic sequence to check whether the conclusions hold.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** No  
- **Axis** Methodological robustness  
- **Claim pointer** The authors use the Amber ff99SB*-ILDN force field for most simulations and note that results may vary with different force fields.  
- **Evidence pointer** Methods (Molecular models), Conclusions  
- **Concern** The sensitivity of the results to the choice of force field is acknowledged but not tested. Given that the conclusions depend on subtle differences in interaction energies (a few kJ/mol), it is important to know whether the observed crossover is robust across different force fields. The authors mention that hydrophobicity varies substantially across force fields, which directly impacts their argument.  
- **Why it matters** If the crossover position or even its existence depends on the force field, the conclusions are not general. The authors should test at least one additional force field to demonstrate robustness.  
- **Resolution test** Repeat the key calculations (transfer free energies, dielectric constants) with an alternative force field (e.g., CHARMM36m or a newer Amber variant) and show that the qualitative conclusions are unchanged.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Quantum method validation  
- **Claim pointer** The quantum chemistry calculations use the ωB97XD functional and specific basis sets to compute interaction energies of side-chain analogues.  
- **Evidence pointer** Methods (Quantum chemical calculations), Results (Quantum calculations confirm a crossover in interaction strength)  
- **Concern** The choice of functional and basis set is reasonable, but no validation against higher-level methods (e.g., CCSD(T)) or experimental data is provided. The interaction energies are used to support the crossover argument, so their accuracy is important.  
- **Why it matters** DFT functionals can have significant errors for dispersion-dominated interactions, which are central to aromatic-aromatic contacts. Without validation, the quantitative reliability of the quantum results is uncertain.  
- **Resolution test** Validate the DFT results against a higher-level method (e.g., CCSD(T) at the complete basis set limit) for a subset of the dimers. Alternatively, compare with experimental binding energies if available.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Introduction, Figure 1  
- **Evidence pointer** Figure 1 (not provided)  
- **Issue** The introduction references Figure 1 to illustrate the conflicting data (hydrophobicity scales, contact matrices, solubility). Without the figure, it is difficult to follow the argument.  
- **Required correction** Ensure the figure clearly shows the conflicting trends and is self-explanatory. Consider adding a schematic summary of the paradox in the main text.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Methodological detail  
- **Affected element** Methods, Simulation setup  
- **Evidence pointer** Methods section, Supplementary file 1  
- **Issue** The description of the simulation systems is brief and relies heavily on Supplementary file 1. Key details such as the number of molecules in the condensate slab, the exact composition, and the equilibration times are not fully described in the main text.  
- **Required correction** Provide a summary table of all simulation systems in the main text, including system size, composition, and simulation length.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Interpretation  
- **Affected element** Results, Condensates as hydrated peptide solvents  
- **Evidence pointer** Figure 6 (not provided)  
- **Issue** The dielectric constant of the condensates is reported as 30-50, but the relationship between this value and the local environment around the stickers is not discussed in detail. The dielectric constant is a macroscopic property, and its relevance to local interactions is not obvious.  
- **Required correction** Discuss the connection between the macroscopic dielectric constant and the local solvation environment around the aromatic residues. Consider calculating a local dielectric or solvation free energy around the stickers.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Literature context  
- **Affected element** Introduction, Discussion  
- **Evidence pointer** References cited in the text  
- **Issue** The manuscript cites relevant literature, but the discussion of the "sticker" framework and the specific role of Tyr vs. Phe could be more comprehensive. In particular, the relationship to recent experimental work on Tyr phosphorylation and its effect on condensate formation is not mentioned.  
- **Required correction** Add a brief discussion of how the findings relate to post-translational modifications of Tyr and to other recent work on aromatic sticker strength.

## Risk / unsupported claims
- The claim that "biomolecular condensates... operate in the second regime" (high dielectric, Tyr-favored) is not fully supported by the provided evidence, as it relies on simplified model systems and the dielectric constant of the condensate is not directly measured.
- The extrapolation from dipeptide condensates to full-length IDR condensates is not justified in detail.
- The robustness of the crossover to force field choice is not demonstrated.
- The accuracy of the quantum chemical interaction energies is not validated against higher-level methods or experiment.
- The specific values of ΔΔGTransfer for the condensates (e.g., -2.9 ± 0.5 kJ/mol) are presented without showing the underlying data, making them unverifiable from the provided material.