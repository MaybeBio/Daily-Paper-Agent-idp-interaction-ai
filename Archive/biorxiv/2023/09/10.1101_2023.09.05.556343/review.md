## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, data/code availability, author contributions, competing interests, acknowledgements)
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by presented evidence. Not assessed: editorial style, formatting, or literature completeness beyond what is needed for scientific evaluation.
- **Shared manuscript claim summary** The authors use atomistic molecular dynamics simulations of the FUS-LCD protein domain to decompose the free energy change of liquid-liquid phase separation into protein and water contributions. They report that solvation entropy and protein interaction enthalpy are the dominant favorable driving forces, comparable in magnitude, while protein conformational entropy changes are small and unfavorable.
- **Visible evidence base** Main text figures (Figures 1-8), equations (Eq. 1-17), one table (Table 1, Table 2), references to Supporting Information (Tables S1-S10, Figures S1-S5), methods section, data availability statement.
- **Missing materials affecting confidence** Supporting Information (Tables S1-S10, Figures S1-S5) not provided. Simulation trajectory data not accessible. Force field parameters and input files not directly inspectable. Details of the nearest-neighbor entropy calculation (PDB2ENTROPY) parameters beyond what is stated in Methods are not available.

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question: the molecular thermodynamic driving forces underlying biomolecular condensate formation. The authors present a computational framework to decompose free energy changes into protein and water contributions, applied to FUS-LCD, a well-studied system. The central finding, that solvation entropy and protein interaction enthalpy are comparable and dominant, is potentially significant. However, the manuscript as presented has several technical concerns that need to be addressed before the case is fully established. The reliance on a single force field, the indirect estimation of protein conformational entropy, the neglect of the mixing entropy term, and the lack of direct validation against experimental thermodynamic data are the main issues. The writing is generally clear, and the conceptual framework (the "tug-of-war" between released and retained water) is well presented.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular phase separation, intrinsically disordered proteins, and computational biophysics. The work provides a methodological template for decomposing thermodynamic driving forces in condensate formation, which is of direct relevance to those studying the physical chemistry of membraneless organelles. The findings on the comparable roles of solvation entropy and protein enthalpy will be of interest to experimentalists seeking to interpret their observations on condensate formation in terms of molecular driving forces.
- **Major strengths**
  - Addresses a fundamental and unresolved question: the relative roles of protein and water thermodynamics in LLPS.
  - Uses atomistic MD simulations, which are more detailed than the coarse-grained approaches commonly used for such systems.
  - Provides a clear conceptual framework (released vs. retained water) and a decomposition scheme that is physically motivated.
  - The finding that solvation entropy and protein enthalpy are comparable is a non-trivial and potentially important result.
  - The manuscript is generally well-written and the figures are informative.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the total free energy change for condensate formation is negative, based on the sum of solvation and protein interaction contributions, and that this is consistent with experimentally observed spontaneous LLPS.
- **Evidence pointer** Results and Discussion, "Thermodynamic signatures of FUS-LCD condensate formation", Figure 8, Eq. 4-17.
- **Concern** The free energy decomposition presented in Eq. 4 and Figure 8 appears to omit the entropic cost of mixing (the translational/positional entropy of the proteins themselves). The authors mention a "demixing" entropy term (RT ln(ρ_cond/ρ_dil)) but state it is neglected because it is small. However, this term is not small: for ρ_cond = 350 mg/mL and ρ_dil = 1 mg/mL, RT ln(350) ≈ 14.5 kJ/mol per mole of protein. This is of the same order of magnitude as the other contributions shown in Figure 8. The authors dismiss this term, but it is a fundamental part of the free energy of phase separation. The total free energy change must include this term, and its omission means the reported total ΔG is incomplete. The claim that the total free energy is negative and consistent with experiment is therefore not established by the presented analysis.
- **Why it matters** The central claim of the paper is that a complete thermodynamic picture is provided. Omitting a term of the same magnitude as the ones discussed undermines this claim and the quantitative conclusions about the balance of driving forces.
- **Resolution test** The authors must include the mixing entropy term in their free energy balance. They should either compute it explicitly and show that the total ΔG remains negative, or provide a rigorous justification for why it can be neglected in the context of their decomposition. The revised Figure 8 should include this term.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the protein conformational entropy change upon condensate formation is small and unfavorable, estimated using a nearest-neighbor method.
- **Evidence pointer** Methods, "Analyses", Figure 8, Table S9.
- **Concern** The estimation of protein conformational entropy is a known hard problem, and the nearest-neighbor method used here (PDB2ENTROPY) is an approximate approach. The manuscript does not provide sufficient detail on the convergence of this estimate with respect to simulation length. The authors state that a 400 ns extension of two trajectories gave a value within error bars, but this is a weak test. The conformational entropy of an IDP is expected to be large, and the difference between two dense states (25 vs 350 mg/mL) could be subtle. The error bars reported are based on three independent simulations, but the systematic error of the method itself is not assessed. The claim that this term is "much smaller" than the other contributions is therefore not robustly supported.
- **Why it matters** The relative magnitude of the protein conformational entropy term is a key part of the conclusion that solvation and protein enthalpy dominate. If this term is underestimated, the balance of driving forces could be different.
- **Resolution test** The authors should provide a more thorough convergence analysis of the conformational entropy estimate, e.g., by block averaging over longer timescales and by comparing with an alternative estimation method. They should also discuss the known limitations of the nearest-neighbor approach for IDPs.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the 2PT method provides accurate entropy values for water in these systems, validated by a comparison with FEP for bulk water.
- **Evidence pointer** Methods, "Analyses", Table 1.
- **Concern** The validation of the 2PT method is performed for bulk water only. The entropy of water confined in a protein condensate is the quantity of interest, and it is not clear that the 2PT method performs equally well under such highly confined and heterogeneous conditions. The decomposition of water entropy into translational and rotational components, and the use of the hard-sphere and rigid-rotor models, may be less accurate in a dense protein environment. The manuscript does not address this potential source of error.
- **Why it matters** The central quantitative result is the entropy change of water upon condensation. If the 2PT method is biased in confined environments, the reported values for the retained water entropy could be systematically wrong, affecting the conclusion of the "tug-of-war".
- **Resolution test** The authors should provide additional validation of the 2PT method for water in a confined environment, e.g., by comparing with a more rigorous method (such as thermodynamic integration) for a test system, or by comparing with experimental data on water dynamics/entropy in concentrated protein solutions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The authors state that the initial structures were generated by AlphaFold and that the systems were equilibrated using coarse-grained simulations followed by back-mapping.
- **Evidence pointer** Methods, "Setup of simulation systems".
- **Concern** The manuscript does not provide sufficient detail on the equilibration protocol. Specifically, the criteria for judging that the coarse-grained simulations had reached equilibrium before back-mapping are not stated. The back-mapping procedure itself can introduce artifacts, and the subsequent equilibration time (100 ns) may not be sufficient for the atomistic system to relax, especially at high protein concentrations. The authors do not report on the structural convergence of the atomistic simulations (e.g., radius of gyration, contact maps) as a function of time.
- **Why it matters** The thermodynamic quantities are computed as averages over the atomistic trajectories. If the systems are not fully equilibrated, the reported values could be biased.
- **Resolution test** The authors should provide a more detailed description of the equilibration protocol, including convergence criteria. They should also show that the key observables (e.g., interaction energies, water entropy) are converged with respect to simulation time.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that their findings are transferable to biological cells, at least qualitatively.
- **Evidence pointer** Results and Discussion, final paragraph.
- **Concern** The simulations are performed in simple binary systems (protein + water + ions) at a single temperature and pressure. Real cells contain a complex mixture of macromolecules, osmolytes, and other components. The authors acknowledge this, but the claim of transferability is not supported by any additional evidence. The effect of other cellular components on the thermodynamic balance could be significant.
- **Why it matters** The broader significance of the work depends on its relevance to the cellular context. Overstating the transferability could mislead readers.
- **Resolution test** The authors should temper this claim or provide a more nuanced discussion of the limitations of their model system in relation to the cellular environment.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states "Both protein and water components are found to have comparably sizeable thermodynamic contributions" but does not specify whether this refers to enthalpy, entropy, or free energy. This is ambiguous.
- **Required correction** Specify the thermodynamic quantity (e.g., "comparable contributions to the free energy change" or "comparable enthalpic and entropic contributions").

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results and Discussion, "Solvent rearrangements upon condensate formation"
- **Evidence pointer** Figure 3a
- **Issue** The y-axis label of Figure 3a is not described in the text. The text refers to "the number of hydration waters per protein molecule" but it is unclear if this is an absolute number or normalized. The figure caption should be explicit.
- **Required correction** Clarify the y-axis label and the normalization in the figure caption.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, "Setup of simulation systems"
- **Evidence pointer** Table 2
- **Issue** The number of water molecules and ions for each system is not reported in Table 2. This information is essential for reproducing the simulations and for assessing the ionic strength.
- **Required correction** Add the number of water molecules and ions to Table 2.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results and Discussion, "Thermodynamic signatures of FUS-LCD condensate formation"
- **Evidence pointer** Eq. 12-14
- **Issue** The notation for the entropy change is confusing. The authors use ΔS_tot, ΔS_PW, and then define ΔS_tot as the sum of released and retained contributions. It would be clearer to use distinct subscripts for the total, released, and retained components.
- **Required correction** Use clearer notation, e.g., ΔS_released, ΔS_retained, and ΔS_total.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Data Availability
- **Evidence pointer** Data Availability statement
- **Issue** The data availability statement says data are available "upon request". For a computational study, it is standard practice to deposit trajectories and analysis scripts in a public repository.
- **Required correction** Deposit the relevant simulation inputs, outputs, and analysis scripts in a public repository (e.g., Zenodo, OSF) and provide the accession link.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Omission of the mixing entropy term in the free energy balance.
  - R1-M2: Insufficient validation of the protein conformational entropy estimate.
  - R1-M3: Lack of validation of the 2PT method for confined water.
  - R1-M4: Insufficient detail on equilibration and convergence of simulations.

- **Assessment against Nature-style criteria**
  - **Originality**: The work is original in its specific decomposition of thermodynamic driving forces in an atomistic simulation of a condensate-forming IDP. The "tug-of-war" concept is a useful framing. However, the general idea that both protein and solvent contributions matter is not new.
  - **Scientific importance**: The question of what drives LLPS is of high importance. The finding that solvation entropy and protein enthalpy are comparable is potentially important, but the technical concerns (especially the missing mixing entropy) prevent a definitive conclusion. The work is a step forward but does not yet provide a complete and robust answer.
  - **Interdisciplinary readership**: The topic is of interest to biophysicists, cell biologists, and soft matter physicists. The writing is accessible to a broad scientific audience, although the thermodynamic formalism may be challenging for some.
  - **Technical soundness**: The use of atomistic MD and the 2PT method is appropriate, but the validation is incomplete. The main technical issues are the missing mixing entropy, the approximate nature of the conformational entropy estimate, and the lack of validation of the water entropy in confined environments.
  - **Readability for nonspecialists**: The manuscript is generally well-written and the figures help convey the main concepts. The abstract is clear, but the results section is dense and may be difficult for nonspecialists to follow.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important question and presents a potentially valuable framework. However, the current evidence does not fully support the central quantitative claims. The authors must address the missing mixing entropy term, provide stronger validation of the entropy estimates, and demonstrate convergence of their simulations. If these issues are resolved, the work could be a significant contribution.