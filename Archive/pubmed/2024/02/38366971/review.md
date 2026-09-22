## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors report microsecond molecular dynamics simulations of six oppositely charged peptide pairs with alternating backbone chirality, characterizing sequence-dependent effects on peptide size, hydrogen bonding, secondary structure, and conformation. They claim that backbone conformation at the single amino acid level is strongly influenced by neighboring sequence, that hydrophobic side chain size and chirality modulate interchain hydrogen bonding and secondary structure, and that principal component analysis reveals sequence-dependent modulation of minimum energy structures.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or simulation details provided
- **Missing materials affecting confidence** Full manuscript, simulation methodology, force field parameters, system setup details, convergence criteria, all figures and tables, comparison with experimental data, and statistical analyses

## Reviewer
- **Overall assessment** The abstract presents a plausible and potentially useful computational study of sequence-dependent behavior in polyelectrolyte complexes. The topic is timely given interest in membraneless organelles and peptide-based materials. However, the abstract alone provides insufficient detail to evaluate the technical soundness of the simulations, the robustness of the conclusions, or the strength of the claimed agreement with experimental results. Several claims are stated without supporting quantitative evidence, and the relationship between simulation observables and experimentally reported properties is not specified. The work may be of interest to the biomolecular simulation and peptide materials communities, but the case is not established from the supplied material.
- **Who would be interested in the results, and why** Researchers in biomolecular simulation, peptide self-assembly, polyelectrolyte complexation, and biomaterials design would be interested. The sequence-dependent insights could inform rational design of peptide-based drug delivery vehicles and contribute to understanding phase behavior relevant to membraneless organelles. The use of alternating chirality and hydrophobic side chain variation is a specific design axis that may appeal to experimental groups working on peptide materials.
- **Major strengths** The study addresses a relevant and under-explored question regarding sequence-dependent conformational behavior in PECs. The use of microsecond simulations is appropriate for capturing conformational sampling in these systems. The design of six peptide pairs with systematic variation in hydrophobicity and chirality provides a structured approach to isolating sequence effects. The connection to previously reported experimental work by Tabandeh et al. suggests an attempt to ground the simulations in empirical observations.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: The question of sequence-dependent conformation in PECs is not entirely new, but the specific focus on alternating chirality and hydrophobic side chain size offers a distinct angle. Scientific importance: Potentially moderate to high for the peptide materials community, but the broader significance beyond this niche is not established from the abstract. Interdisciplinary readership: The abstract is written in a way that is accessible to polymer scientists and biophysicists, but the lack of quantitative detail limits its appeal to a wider audience. Technical soundness: Cannot be assessed from the abstract alone; no force field, simulation protocol, or convergence analysis is provided. Readability for nonspecialists: The abstract is generally clear, though terms such as "Ramachandran plots" and "principal component analysis" are used without explanation, which may limit accessibility for readers outside computational biophysics.
- **Recommendation posture** Currently not established from the provided evidence. The abstract suggests a potentially sound study, but the absence of methodological detail and quantitative results prevents a supportive recommendation. A full manuscript with detailed methods, convergence checks, and explicit comparison to experimental data would be required to assess the claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "microsecond molecular dynamic simulations" were used to characterize sequence-dependent peptide conformation, and that the analysis "recapitulates sensible trends in peptide conformation and degree of hydrogen bonding, consistent with experimentally reported results."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract provides no information on the force field, water model, salt concentration, temperature, pressure coupling, or simulation box size. Without these details, the reliability of the simulations cannot be evaluated. Furthermore, the claim of consistency with experimental results is stated without specifying which experimental observables were compared, how the comparison was made, or what quantitative agreement was achieved.
- **Why it matters** Molecular dynamics results are highly sensitive to force field choice and simulation conditions. A claim of experimental consistency is only meaningful if the comparison is explicit and quantitative. Without this information, readers cannot judge whether the observed trends are robust or artifacts of the simulation setup.
- **Resolution test** Provide full simulation methodology in the manuscript, including force field parameters, system composition, equilibration and production protocols, and convergence metrics. Include a quantitative comparison between simulation-derived observables (e.g., radius of gyration, hydrogen bond counts, secondary structure fractions) and the corresponding experimental measurements, with error estimates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors claim that "Ramachandran plots reveal that backbone conformation at the single amino acid level is highly influenced by the neighboring sequence in the chain."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract states this as a finding but provides no quantitative support. No data are shown on the distribution of backbone dihedral angles, the magnitude of the neighboring-sequence effect, or how this effect varies across the six peptide pairs. The term "highly influenced" is vague and not backed by statistical measures.
- **Why it matters** This claim is central to the sequence-dependent design premise of the study. Without quantitative evidence, such as per-residue Ramachandran distributions or a comparison of dihedral angle populations across sequences, the claim remains anecdotal.
- **Resolution test** Include Ramachandran plots for each residue type in each sequence context, with population statistics and a quantitative measure of the neighboring-sequence effect (e.g., difference in dihedral angle distributions or a statistical test comparing residue conformations across sequence contexts).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors claim that "principal component analysis reveals that the minimum energy structures may be subtly modulated by the underlying sequence."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The claim is hedged with "may be subtly modulated," which is appropriately cautious, but the abstract provides no information on how the principal component analysis was performed, which degrees of freedom were included, how many principal components were retained, or how the minimum energy structures were identified. The term "minimum energy structures" is ambiguous in the context of an ensemble simulation.
- **Why it matters** Principal component analysis is a powerful tool, but its interpretation depends heavily on the choice of variables and the convergence of the sampled ensemble. Without methodological detail, the claim cannot be evaluated, and the reader cannot determine whether the observed modulation is significant or within statistical noise.
- **Resolution test** Describe the principal component analysis procedure in the methods, including the selection of atoms or coordinates, the number of components analyzed, and the criteria for identifying minimum energy structures. Provide a quantitative comparison of the principal component projections across the six peptide pairs, with uncertainty estimates.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract wording
- **Evidence pointer** Abstract; location not provided
- **Issue** The phrase "recapitulates sensible trends" is vague. It is unclear what "sensible" means in this context and whether the trends are statistically significant or merely qualitative.
- **Required correction** Replace "sensible trends" with a more precise description, such as "trends consistent with experimental measurements within statistical uncertainty," and specify the observables and comparison metrics.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Abstract scope
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract mentions "peptide size, degree of hydrogen bonding, secondary structure, and conformation" as characterized properties, but does not define how these are measured or which specific metrics are used (e.g., radius of gyration, hydrogen bond occupancy, DSSP assignment).
- **Required correction** Briefly define the key observables in the abstract or refer to the methods section for definitions, so that readers can interpret the claims without accessing the full text.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Context
- **Affected element** Abstract framing
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states that the sequences were "previously reported by Tabandeh et al." but does not indicate whether the current study uses the same simulation conditions or force field as that prior work, or whether the comparison is purely experimental.
- **Required correction** Clarify the relationship to the prior study, including whether the same simulation protocol was used and whether the experimental data are from that prior publication.

## Risk / unsupported claims
- The claim of consistency with experimental results is unsupported in the abstract because no specific experimental data or comparison metrics are provided.
- The claim that backbone conformation is "highly influenced" by neighboring sequence is unsupported without quantitative dihedral angle data.
- The claim that minimum energy structures are "subtly modulated" by sequence is unverifiable without details on the principal component analysis and energy landscape characterization.
- The overall relevance to membraneless organelles and drug delivery is stated as motivation but not connected to any specific finding in the abstract.