## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors report that classical all-atom force fields overestimate cation-phosphate interaction strength in model salts, introduce new Electronic Continuum Correction (ECC) parameters for CHARMM36m and AmberFF99SB-ILDN that improve osmotic coefficient agreement, and show preliminary improvements in conformational ensembles for a phosphorylated peptide, concluding that long-lived cation-phosphate bridges (nP-collabs) are artifacts of missing explicit polarization.
- **Visible evidence base** Abstract text only; no numerical data, methodological details, or experimental comparisons are provided beyond qualitative statements
- **Missing materials affecting confidence** Full methods, force field parameter tables, osmotic coefficient data, secondary chemical shift comparisons, simulation protocols, error estimates, and any statistical analyses

## Reviewer
- **Overall assessment** The abstract presents a potentially important finding for the molecular simulation community, namely that classical force fields may produce artifactual cation-phosphate clustering in phosphorylated IDPs. The proposed ECC-based reparameterization is a plausible strategy. However, the abstract provides insufficient quantitative evidence to evaluate the strength of the claims. The central conclusion that nP-collabs are artifacts rests on indirect evidence from model salts and a single peptide test, and the abstract does not demonstrate that the observed improvements are statistically robust or generalizable. The work is likely of interest to computational biophysicists and those studying phosphorylation in IDPs, but the case is not fully established from the supplied material.
- **Who would be interested in the results, and why** Computational chemists and biophysicists using molecular dynamics to study IDPs, post-translational modifications, and ion-protein interactions. Researchers developing or refining force fields for phosphorylated systems, particularly those studying neurodegenerative disease-related proteins, would find the proposed ECC parameters and the cautionary note about nP-collabs directly relevant.
- **Major strengths** The study addresses a timely and underappreciated issue in biomolecular simulation, namely cation-mediated clustering in multiphosphorylated systems. The use of osmotic coefficient calculations as a thermodynamic benchmark is a rigorous and physically meaningful approach. The proposal of ECC-based parameters is a concrete, actionable solution that could be widely adopted. The preliminary test on a biologically relevant peptide (rhodopsin 7PP) adds translational relevance.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract lacks quantitative osmotic coefficient data, error bars, and statistical comparisons between force fields. The single-peptide test is insufficient to generalize the conclusion that nP-collabs are artifacts. The relationship between model salt behavior and IDP behavior is asserted but not demonstrated mechanistically. No information is provided on the transferability of the new parameters to other phosphorylation sites or sequence contexts.
- **Assessment against Nature-style criteria** Originality: High, as the identification of nP-collabs as artifacts and the ECC-based remedy is a novel contribution. Scientific importance: Moderate to high, given the widespread use of classical force fields for phosphorylated IDPs and the implications for disease-related research. Interdisciplinary readership: Moderate, primarily appealing to computational chemists, biophysicists, and structural biologists, with limited reach beyond these fields. Technical soundness: Not fully assessable from the abstract; the osmotic coefficient approach is sound in principle, but the evidence presented is qualitative. Readability for nonspecialists: The abstract is accessible but assumes familiarity with force fields and osmotic coefficients, which may limit broader readability.
- **Recommendation posture** Supportive if technical concerns are resolved, specifically if the authors provide quantitative data, statistical validation, and broader tests of parameter transferability. Currently not established from the provided evidence.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "All force fields were found to overestimate the strength of the interaction to various degrees" and "provide remarkable agreement for varphi values for both cation types and over a range of concentrations"
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract states that all force fields overestimate cation-phosphate interaction strength and that the new ECC parameters provide "remarkable agreement" for osmotic coefficients, but no numerical values, comparison plots, or statistical measures are provided. The magnitude of overestimation, the degree of improvement, and the concentration range tested are all unspecified.
- **Why it matters** Without quantitative data, the reader cannot assess whether the overestimation is biologically significant or whether the ECC parameters achieve agreement within experimental uncertainty. The claim of "remarkable agreement" is subjective and unverifiable from the abstract alone.
- **Resolution test** Provide osmotic coefficient values for each force field and the ECC variants across the tested concentration range, with experimental reference data and error estimates. Show that the ECC parameters fall within experimental uncertainty and that the improvement is statistically significant.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability
- **Claim pointer** "We thus conclude that long-lasting nP-collabs are artifacts for classical force fields born from the lack of explicit polarization"
- **Evidence pointer** Abstract, location not provided
- **Concern** The conclusion that nP-collabs are artifacts is based on osmotic coefficient measurements on simple model salts (2Na+HPO4(2-) and 2K+HPO4(2-)) and a preliminary test on a single peptide (7PP). The abstract does not demonstrate that the behavior observed in model salts translates directly to the complex, heterogeneous environment of a multiphosphorylated IDP, nor that the 7PP test is representative of other sequences or phosphorylation patterns.
- **Why it matters** The central claim of the paper is that nP-collabs are artifacts, which has broad implications for interpreting existing simulations. If the evidence is limited to one peptide and simple salts, the conclusion may be premature and could mislead researchers who rely on these force fields.
- **Resolution test** Test the ECC parameters on multiple multiphosphorylated peptides with different sequences, phosphorylation densities, and cation types. Show that the reduction in nP-collab lifetimes is consistent across systems and that the conformational ensembles match experimental data (e.g., chemical shifts, SAXS) in each case.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic interpretation
- **Claim pointer** "nP-collabs are artifacts for classical force fields born from the lack of explicit polarization"
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract attributes the overbinding to "lack of explicit polarization" but does not provide a mechanistic analysis, such as comparing ion-water vs. ion-phosphate coordination numbers, charge distributions, or polarization effects between the full-charge and ECC force fields. The causal link between missing polarization and nP-collab formation is asserted, not demonstrated.
- **Why it matters** Understanding the mechanism is crucial for designing better force fields and for interpreting whether the ECC approach addresses the root cause or merely compensates for it. Without this analysis, the proposed strategy may not be generalizable to other ion types or modifications.
- **Resolution test** Include a comparative analysis of ion coordination environments, radial distribution functions, and interaction energies between full-charge and ECC force fields. Show that the ECC parameters reduce the thermodynamic driving force for cation-phosphate binding in a way consistent with polarization effects.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract, location not provided
- **Issue** The term "n-phosphate collaborations (nP-collabs)" is introduced without a clear operational definition. It is unclear whether this refers to a specific lifetime threshold, a coordination number, or a free energy criterion.
- **Required correction** Define nP-collabs explicitly, including the criteria used to identify them in simulations (e.g., minimum residence time, distance cutoff, number of bridging cations).

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Parameter details
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract states that new ECC parameters were designed for CHARMM36m and AmberFF99SB-ILDN, but no details are given on which atoms or interactions were modified, or how the ECC approach was applied to phosphorylations specifically.
- **Required correction** Provide a brief summary of the parameterization strategy, including which partial charges or Lennard-Jones parameters were adjusted and the rationale for these changes.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scope
- **Affected element** Biological relevance
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract mentions relevance to Alzheimer's and Parkinson's diseases but does not connect the findings to specific pathological mechanisms or sequences. This appears as a general statement rather than a substantive link.
- **Required correction** Either remove the disease reference or provide a specific example of how nP-collab artifacts could affect interpretations of disease-related IDP simulations.

## Risk / unsupported claims
- The claim that "all force fields overestimate the strength of the interaction" is unsupported without quantitative data.
- The claim of "remarkable agreement" for ECC parameters is unverifiable without numerical values and error estimates.
- The conclusion that nP-collabs are "artifacts" is not established from the abstract, as it relies on indirect evidence and a single peptide test.
- The assertion that the artifacts arise from "lack of explicit polarization" is mechanistically unsupported.
- The generalizability of the ECC parameters to other phosphorylation sites, sequences, or force fields is not assessable from the abstract.