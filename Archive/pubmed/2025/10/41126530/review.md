## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors report parametrization and validation of Drude polarizable force field parameters for phosphorylated serine, threonine, and tyrosine in all protonation states, with validation in two full-length proteins (ERK2 and WNK1) and short polypeptides, showing maintenance of salt-bridge interactions and secondary structure effects consistent with prior findings.
- **Visible evidence base** Abstract text only; no quantitative data, methodological details, or validation metrics provided
- **Missing materials affecting confidence** Full methods, parameter fitting details, QM target data, simulation protocols, validation results, figures, tables, and comparison benchmarks

## Reviewer
- **Overall assessment** The abstract describes a technically important and timely contribution to the Drude polarizable force field ecosystem, addressing a clear gap in chemical space for phosphorylated residues. The scope of parametrization across three residues and all protonation states is commendable. However, the abstract provides insufficient quantitative evidence to evaluate the quality of the parametrization or the robustness of the validation. The claims of agreement with previous findings and maintenance of electrostatic interactions are plausible but not substantiated with data in the supplied material. The work is likely of interest to the molecular simulation community, but the case for its reliability and broad utility is not fully established from the abstract alone.
- **Who would be interested in the results, and why** Computational biophysicists and chemists using molecular dynamics simulations, particularly those studying phosphorylation-dependent conformational changes, intrinsically disordered proteins, and protein-protein or protein-ligand interactions involving phosphorylated residues. Developers of polarizable force fields and users of the Drude model would also find the extension of chemical space valuable. Experimentalists studying phosphorylation signaling may benefit indirectly through improved simulation accuracy.
- **Major strengths** The work addresses a well-defined and important gap in polarizable force field coverage. The inclusion of all protonation states for three residue types is thorough. Validation in full-length proteins and short polypeptides provides a reasonable range of test systems. Compatibility with the existing Drude protein force field is a practical advantage for the community.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative validation evidence absent), R1-M2 (protonation state treatment unclear), R1-M3 (comparison to prior models not shown)
- **Assessment against Nature-style criteria** Originality is moderate to high, as the extension of Drude parameters to phosphorylated residues is a specific and needed contribution, though not conceptually novel. Scientific importance is significant for the simulation community, with potential downstream impact on understanding phosphorylation-driven biology. Interdisciplinary readership is limited to computational and biophysical audiences, which is narrower than typical Nature scope. Technical soundness cannot be fully assessed from the abstract, as no quantitative metrics or methodological details are provided. Readability for nonspecialists is adequate, with clear motivation and context, but the abstract assumes familiarity with force field parametrization concepts.
- **Recommendation posture** Supportive if technical concerns are resolved, specifically if the full manuscript provides robust quantitative validation, clear protonation state handling, and direct comparisons to existing models. Currently not established from the provided evidence alone.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The abstract claims successful parametrization and validation of the force field, including maintenance of strong interactions with lysine and arginine and reduction of disorder in short polypeptides.
- **Evidence pointer** Abstract text; location not provided
- **Concern** The abstract provides no quantitative data, such as root-mean-square deviations from QM targets, interaction energy comparisons, secondary structure populations, or statistical measures of agreement with experimental or prior computational results. The validation claims are stated qualitatively without supporting numbers or figures.
- **Why it matters** Without quantitative evidence, the reader cannot assess the accuracy or reliability of the parameters. Force field parametrization requires demonstration of close reproduction of target properties, and validation claims must be backed by measurable outcomes to be credible.
- **Resolution test** The full manuscript should include tables or figures showing QM versus MM comparisons for electrostatic and dihedral properties, and validation metrics such as RMSD, interaction energies, or secondary structure fractions with uncertainties.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological clarity
- **Claim pointer** The abstract states that parameters were developed for all protonation states (neutral, monoanionic, and dianionic) of phosphorylated serine, threonine, and tyrosine.
- **Evidence pointer** Abstract text; location not provided
- **Concern** The abstract does not specify how protonation states were defined, whether all states were validated in the protein and polypeptide systems, or whether the dianionic state, which is rare at physiological pH, was treated with appropriate attention to its high charge density. The handling of protonation equilibria and possible tautomeric forms is unclear.
- **Why it matters** Protonation state assignment critically affects electrostatic interactions and hydrogen bonding in simulations. If the parametrization does not adequately address the physical relevance or stability of each state, users may misapply the parameters, leading to incorrect biological conclusions.
- **Resolution test** The full manuscript should detail the protonation state definitions, the QM target data used for each state, and any validation specific to each state, including pKa considerations or titration behavior.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Comparative validation
- **Claim pointer** The abstract claims that results agree with previous findings, specifically that phosphorylation reduces disorder and promotes alpha-helical turns in short polypeptides.
- **Evidence pointer** Abstract text; location not provided
- **Concern** The abstract does not specify which previous findings are referenced, nor does it provide a direct comparison to additive force fields or other polarizable models. Without a benchmark against existing parameters, the added value of the Drude model for phosphorylated residues is not demonstrated.
- **Why it matters** The utility of new force field parameters depends on their performance relative to established alternatives. If the Drude parameters do not offer improved accuracy or unique insights, their adoption may not be justified despite the theoretical advantages of polarizability.
- **Resolution test** The full manuscript should include direct comparisons to additive force fields (e.g., CHARMM36) or other polarizable models for the same test systems, with quantitative metrics showing where the Drude model performs better or differently.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of scope
- **Affected element** Abstract statement on "all protonation states"
- **Evidence pointer** Abstract text; location not provided
- **Issue** The abstract does not clarify whether the neutral state refers to the unphosphorylated-like form or a protonated phosphate group, which could confuse users.
- **Required correction** Define the neutral state explicitly, for example as the fully protonated phosphoric acid form, and state the pH conditions under which each state is relevant.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** System selection rationale
- **Affected element** Validation in ERK2 and WNK1
- **Evidence pointer** Abstract text; location not provided
- **Issue** The abstract does not explain why ERK2 and WNK1 were chosen as validation systems, nor whether these proteins represent diverse structural contexts for phosphorylated residues.
- **Required correction** Provide a brief rationale for the choice of validation systems, including their structural features and relevance to phosphorylation biology.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology precision
- **Affected element** "Rigidifying loops" claim
- **Evidence pointer** Abstract text; location not provided
- **Issue** The term "rigidifying" is qualitative and could be interpreted in multiple ways, such as reduced B-factors, decreased RMSF, or altered conformational sampling.
- **Required correction** Specify the metric used to assess rigidity, such as root-mean-square fluctuations or hydrogen bond persistence, and provide the corresponding values.

## Risk / unsupported claims
- The claim that the force field "maintained the expected strong interactions with lysine and arginine" is unsupported without quantitative interaction energy or contact frequency data.
- The claim that phosphorylation "reduced disorder and promoted the formation of alpha-helical turns" is unsupported without secondary structure assignment data or comparison to control simulations.
- The claim of "agreement with previous findings" is unverifiable without citation or direct comparison data.
- The overall assertion of successful parametrization is not assessable from the abstract, as no fitting statistics or validation metrics are provided.