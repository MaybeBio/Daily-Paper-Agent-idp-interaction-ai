## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) from bioRxiv preprint
- **Assessment boundary** Scientific validity, methodological soundness, evidence quality, and claims as presented in the provided text; no external data or replication attempted
- **Shared manuscript claim summary** The authors introduce TEA, a framework that derives temperature-dependent coarse-grained interaction potentials from all-atom hydration free energies, and demonstrate its ability to capture both UCST- and LCST-type thermoresponsive behavior in IDPs
- **Visible evidence base** All-atom MD simulations (umbrella sampling, hydration free energy calculations), CG single-chain and multi-chain simulations, comparisons with experimental data from Quiroz & Chilkoti and Wuttke et al.
- **Missing materials affecting confidence** Figures and tables referenced but not provided; detailed simulation parameters for CG models; error bars and statistical analysis; exact fitting procedure for γ; comparison with existing temperature-dependent CG models beyond those mentioned

## Reviewer
- **Overall assessment** The manuscript presents a conceptually appealing framework that addresses a genuine limitation in current CG models for IDP phase separation. The central idea, linking hydration free energies to temperature-dependent interaction strengths, is physically motivated and potentially impactful. However, the evidence as presented is incomplete. Key figures and tables are referenced but not visible, making it impossible to assess the quality of the correlations, the magnitude of errors, or the robustness of the claims. The single-parameter fitting approach is elegant, but the validation against experimental data appears limited to a small number of sequences, and the failure to capture highly charged IDPs is acknowledged but not deeply explored. The manuscript would benefit from a more critical discussion of the assumptions underlying the linear mapping and the universality of the κ parameter.

- **Who would be interested in the results, and why** Researchers in the fields of biomolecular phase separation, intrinsically disordered proteins, and coarse-grained simulation method development. The framework offers a path toward simulating thermoresponsive IDPs without extensive phenomenological fitting, which is a recognized bottleneck. The potential to distinguish UCST- and LCST-type sequences from sequence alone is of broad interest to both experimental and computational groups studying synthetic and natural IDPs.

- **Major strengths**
  1. The physical motivation is clear and addresses a well-known limitation of existing CG models (temperature-independent interactions).
  2. The framework is designed to be minimally parameterized (single global scaling factor), which is a significant advantage over data-heavy fitting approaches.
  3. The use of extensive all-atom simulations to derive the underlying energetics provides a rigorous foundation.
  4. The framework is demonstrated to be compatible with multiple existing CG models (HPS-Urry, HPS-FB, CALVADOS), suggesting generalizability.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The manuscript claims that "TEA-augmented CG models robustly distinguish UCST- and LCST-type sequences" and "accurately reproduce LCST-type single-chain compaction trends and phase diagrams."
- **Evidence pointer** Figures 5, 6, 7, S9-S14; location not provided
- **Concern** The core validation results are presented in figures that are not included in the provided text. Without seeing the actual data, it is impossible to evaluate the quality of the separation between UCST and LCST sequences, the agreement with experimental Rg values, or the accuracy of the phase diagrams. The claim of "robustly distinguish" and "accurately reproduce" cannot be assessed.
- **Why it matters** The entire premise of the paper rests on the quantitative and qualitative success of these validations. If the separation is marginal or the phase diagrams are only qualitatively correct, the impact of the work is substantially diminished.
- **Resolution test** Provide the referenced figures and tables. The separation between RLP and ELP sequences should be clear and statistically significant. The simulated Rg values and phase boundaries should be compared quantitatively with experimental data, including error estimates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological justification
- **Claim pointer** The manuscript states that "interaction strengths of the interacting species exhibit a linear dependence on their hydration free energies" and that this allows for "derivation of temperature-dependent potentials across continuous temperature space."
- **Evidence pointer** Figure 3, Table 1; location not provided
- **Concern** The linear correlation between ΔGE and Δu_h is the cornerstone of the TEA framework. The manuscript reports a mean absolute error of 0.007 kcal/mol for the fit, but the correlation coefficients (r_i) are not provided in the text. More critically, the physical justification for this linearity is not discussed. Why should the excess free energy of interaction scale linearly with hydration free energy? Is this expected from theory? The manuscript also notes that a single universal κ cannot connect all species, implying a residue-specific parameter, which weakens the claim of a "physics-based" derivation.
- **Why it matters** If the linear relationship is purely empirical and not physically justified, the framework's predictive power for sequences outside the training set is questionable. The residue-specific κ values reintroduce a degree of fitting that the authors claim to minimize.
- **Resolution test** Provide the correlation coefficients and a scatter plot of ΔGE vs Δu_h for all species. Discuss the physical origin of the linear relationship. Justify the need for residue-specific κ values and explain how these are obtained without overfitting.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Validation scope
- **Claim pointer** The manuscript claims the framework "successfully identifies experimental outliers" and "captures both the LCST-type and UCST-type phase behaviors."
- **Evidence pointer** Figures 5, 6, 7; location not provided
- **Concern** The validation is performed on a limited set of sequences (23 RLPs, 16 ELPs, 5 IDPs from Wuttke, and A1-LCD variants). While this is a reasonable start, the claim of "significant predictive power" is strong. The framework is not tested on a diverse set of sequences with varied compositions, lengths, or charge distributions. The failure on highly charged IDPs (ProTa N, ProTa C) is acknowledged but not addressed, limiting the generalizability of the approach.
- **Why it matters** A framework that cannot handle highly charged IDPs, which are a significant fraction of biological IDPs, has limited utility. The predictive power claim needs to be tempered or the limitations need to be more thoroughly investigated and discussed.
- **Resolution test** Test the framework on a broader set of IDPs, including those with high net charge, and discuss the conditions under which the framework is expected to fail. Provide a more nuanced discussion of the framework's limitations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The manuscript states that "the resultant PMFs after subtraction quantify the vdW interactions mediated by water molecules between the charged analogues."
- **Evidence pointer** Methods section, "Temperature-dependent homotypic interactions" subsection; location not provided
- **Concern** The procedure for subtracting the direct Coulombic interaction from the PMF for charged species is described only briefly. The details of this subtraction are critical, as the resulting PMF is used to parameterize the modified Lennard-Jones potential. It is unclear how the Coulombic term is calculated (e.g., using what dielectric constant) and whether the subtraction introduces artifacts. The statement that "the direct electrostatic interactions still implicitly influence the resultant PMFs" is vague and needs clarification.
- **Why it matters** If the subtraction procedure is flawed, the derived temperature-dependent potentials for charged residues will be incorrect, affecting the accuracy of simulations for any sequence containing charged amino acids.
- **Resolution test** Provide a detailed description of the subtraction procedure, including the functional form of the Coulombic term used and the justification for this approach. Show a representative PMF before and after subtraction to demonstrate the procedure's validity.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "including both upper critical solution temperature (UCST) and lower critical solution temperature (LCST) transitions" is slightly redundant, as UCST and LCST are defined by their transition types.
- **Required correction** Consider simplifying to "including both upper (UCST) and lower (LCST) critical solution temperature transitions."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph 2
- **Issue** The sentence "An approach to address this challenge is using implicit solvent model" is grammatically awkward.
- **Required correction** Revise to "One approach to address this challenge is the use of implicit solvent models."

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Results, "Temperature-dependent homotypic interactions" section
- **Evidence pointer** Results, first subsection; location not provided
- **Issue** The text states "we demonstrate that interaction strengths of the interacting species exhibit a linear a linear dependence on their hydration free energies." The phrase "a linear a linear" is a typographical error.
- **Required correction** Correct to "a linear dependence."

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods, "Details of all-atom molecular dynamics simulations"
- **Evidence pointer** Methods, first subsection; location not provided
- **Issue** The methods state that "We compared the Lennard-Jones parameters (σ and ε) and partial charges against those from CHARMM36m protein force field (Fig. S15-S18)." However, the text later refers to "Fig. S15" in the context of the cutoff analysis, creating a potential numbering conflict or confusion.
- **Required correction** Ensure figure numbering is consistent and unambiguous throughout the manuscript and supplementary materials.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion, "Fit lambda values from all-atom energetics" section
- **Evidence pointer** Discussion, second subsection; location not provided
- **Issue** The sentence "By combining Eq. 2, Eq. 3 and Eq. 6, λ becomes an analytical function of thermodynamic observables Δu_h(T0), Δc_p, Δh., the scaling factor κ, and the fitting parameter γ." The period after "Δh." is misplaced.
- **Required correction** Remove the period after "Δh" and ensure the list is grammatically correct.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, "Heterotypic interactions" section
- **Evidence pointer** Results, third subsection; location not provided
- **Issue** The manuscript states that 43 heterotypic pairs were simulated, but the selection criteria for these pairs are not described. It is unclear if they are representative of all possible pair types.
- **Required correction** Briefly describe how the 43 pairs were selected and whether they cover the chemical diversity of amino acid side chains.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, "Mapping temperature-dependent atomistic energetics" section
- **Evidence pointer** Results, fourth subsection; location not provided
- **Issue** The term "Ashbaugh-Hatch function" is used without a citation or a brief description of its form.
- **Required correction** Provide a citation for the Ashbaugh-Hatch potential and briefly define its functional form.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion, "Robustness and limitations" section
- **Evidence pointer** Discussion, third subsection; location not provided
- **Issue** The discussion of limitations focuses on the lack of explicit ions. Other potential limitations, such as the neglect of backbone conformational entropy or the transferability of the κ parameters to other force fields, are not discussed.
- **Required correction** Add a brief discussion of other potential limitations and how they might affect the framework's applicability.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: The core validation data (Figures 5-7) are not visible, making the central claims unverifiable.
  - R1-M2: The physical basis for the linear correlation between ΔGE and Δu_h is not established, and the residue-specific κ values introduce a fitting element that is not fully justified.
  - R1-M4: The procedure for subtracting Coulombic interactions from PMFs of charged species is not described in sufficient detail to assess its validity.

- **Assessment against Nature-style criteria**
  - **Originality**: The concept of deriving temperature-dependent CG potentials from hydration free energies is novel and addresses a clear gap in the field. The approach is distinct from existing data-driven fitting methods.
  - **Scientific importance**: The ability to simulate thermoresponsive IDPs, particularly LCST-type behavior, is of significant importance for understanding both natural and synthetic IDP phase behavior. The framework has the potential to be widely adopted.
  - **Interdisciplinary readership**: The work is relevant to biophysics, computational chemistry, and protein engineering. The writing is generally accessible, though some sections assume familiarity with CG simulation methods.
  - **Technical soundness**: The all-atom simulation methodology appears sound, but the key validation and the Coulombic subtraction procedure are not fully transparent. The single-parameter fitting is elegant, but the justification for the linear mapping needs strengthening.
  - **Readability for nonspecialists**: The abstract and introduction are clear, but the results and methods sections are dense and would be challenging for a nonspecialist. The manuscript would benefit from a more explicit statement of the key findings and their implications.

- **Recommendation posture** Supportive if technical concerns are resolved. The framework is conceptually promising and addresses a real need, but the current evidence is insufficient to fully establish its validity and predictive power. The authors must provide the missing figures, clarify the physical basis of the linear correlation, and detail the Coulombic subtraction procedure. If these issues are addressed, the work could be a valuable contribution to the field.