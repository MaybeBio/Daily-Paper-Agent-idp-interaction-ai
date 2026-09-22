## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no access to methods, figures, or supplementary data
- **Shared manuscript claim summary** The authors use molecular dynamics simulations to study how the multidomain architecture of TDP-43 (IDR, RRMs, NTD) and RNA (polyA) modulate intermolecular interactions and viscoelastic properties of biomolecular condensates. They report that IDR interactions dominate, with a hotspot at residues R268-F276; RRM2 increases condensate packing while NTD decreases it; RNA binding replaces some TDP-43 self-interactions with TDP-43-polyA interactions; and RNA increases elasticity while RRMs enhance viscosity and NTD reduces it.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or simulation details provided
- **Missing materials affecting confidence** Full manuscript, simulation parameters, force field details, system compositions, analysis methods, validation of condensate formation, and quantitative data supporting the reported trends

## Reviewer
- **Overall assessment** The abstract presents a plausible and potentially interesting computational study on TDP-43 condensate regulation by multidomain architecture and RNA. However, the evidence base is limited to a summary of findings without methodological detail or quantitative support. The central claims regarding domain-specific effects on packing and viscoelasticity are stated as conclusions but cannot be independently evaluated from the supplied material. The work addresses a relevant question in the phase separation field, but the current evidence is insufficient to establish the case.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation mechanisms, RNA-binding proteins, and neurodegenerative diseases linked to TDP-43. The findings could inform understanding of how protein architecture and RNA modulate condensate material properties, which is relevant to both fundamental cell biology and disease mechanisms.
- **Major strengths** The study addresses a timely and important question about how multidomain proteins and RNA jointly regulate condensate properties. The use of molecular dynamics simulations to dissect domain-specific contributions is a reasonable approach. The abstract clearly identifies specific residues and domain-level effects, suggesting a systematic analysis.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract lacks any quantitative data, simulation details, or validation of condensate formation. Without these, the reported trends in packing and viscoelasticity cannot be assessed for robustness or statistical significance. The claim that IDR interactions are dominant requires supporting interaction energy or contact frequency data. The effect of RNA on viscoelasticity needs rheological or dynamical measurements that are not described.
- **Assessment against Nature-style criteria** 
  - Originality: The question of how multidomain architecture and RNA jointly modulate condensate viscoelasticity is not entirely new, but the specific focus on TDP-43 with all three domains is a reasonable contribution. The originality is moderate.
  - Scientific importance: The topic is important for understanding TDP-43 biology and phase separation generally. However, the abstract does not demonstrate a conceptual advance beyond existing knowledge that IDRs drive phase separation and RNA modulates properties.
  - Interdisciplinary readership: The work bridges biophysics, molecular simulation, and cell biology, which could appeal to a broad readership. However, the abstract is written in a specialized manner that may limit accessibility.
  - Technical soundness: Cannot be evaluated from the abstract alone. No methods, parameters, or validation are provided.
  - Readability for nonspecialists: The abstract is concise but uses domain-specific terminology without sufficient context. It is readable for experts but not for a general scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents plausible findings, but the lack of methodological detail and quantitative support prevents a definitive assessment. A supportive posture would require access to the full manuscript and verification of the reported trends.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that IDR interactions are dominant in all domain constructs, particularly around residues R268-F276.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract states that IDR interactions dominate but provides no quantitative measure, such as interaction energies, contact frequencies, or residence times. The specific hotspot at R268-F276 is mentioned without supporting data or context on how this was determined.
- **Why it matters** The claim of IDR dominance is central to the paper's message. Without quantitative evidence, the reader cannot assess whether this is a robust finding or an artifact of the simulation setup, force field, or system composition.
- **Resolution test** Provide interaction energy decomposition or contact probability maps for each domain construct, with statistical analysis across replicate simulations. Show that the R268-F276 hotspot is significant relative to other regions and consistent across constructs.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that RRM2 increases condensate packing, NTD decreases it, and RNA binding alters viscoelastic properties (RRMs enhance viscosity, NTD reduces it, polyA increases elasticity).
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract reports qualitative trends in packing and viscoelasticity without any numerical values, error bars, or statistical tests. It is unclear how packing was quantified, how viscoelasticity was measured in simulations, and whether the differences between constructs are significant.
- **Why it matters** These are the main quantitative findings of the study. Without data, the claims are unverifiable and could be due to simulation noise, insufficient sampling, or system-specific artifacts.
- **Resolution test** Provide quantitative measures of packing (e.g., density, coordination number) and viscoelasticity (e.g., shear viscosity, elastic modulus) for each construct, with uncertainties and statistical comparisons. Describe the simulation protocol used to extract these properties.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The study uses molecular dynamics simulations to investigate TDP-43 condensates, but no simulation details are provided.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract does not mention the simulation method (e.g., coarse-grained vs. all-atom), force field, system size, salt concentration, temperature, or simulation length. It is also unclear how condensates were formed and equilibrated in the simulations.
- **Why it matters** Reproducibility is a fundamental requirement for computational studies. Without these details, the results cannot be replicated or compared with other work, and the validity of the simulation approach cannot be assessed.
- **Resolution test** Include a methods section with full simulation parameters, system construction, equilibration protocol, and analysis details. Provide access to input files or a description sufficient for reproduction.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract wording
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "form biomolecular condensates with RNA through phase separation" is somewhat redundant, as condensate formation is typically defined by phase separation.
- **Required correction** Rephrase to "RNA-binding proteins and RNA form biomolecular condensates through phase separation" or similar.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Abstract
- **Evidence pointer** Abstract, last sentence
- **Issue** The conclusion that "multidomain structure and RNA interactions orchestrate condensate organization" is broad and not directly supported by the specific findings listed. The link between the observed molecular interactions and the macroscopic viscoelastic properties is not explicitly explained.
- **Required correction** Add a sentence connecting the molecular-level findings (e.g., replacement of TDP-43 self-interactions with TDP-43-polyA interactions) to the observed changes in viscoelasticity.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Context
- **Affected element** Abstract
- **Evidence pointer** Abstract, second sentence
- **Issue** The statement that "additional factors such as folded domains and RNA also influence condensate formation" is presented as background, but no prior work is cited or discussed. This limits the reader's ability to place the study in context.
- **Required correction** Add brief references or a sentence summarizing prior findings on the role of folded domains and RNA in condensate properties.

## Risk / unsupported claims
- The claim that IDR interactions are dominant in all domain constructs is unsupported without quantitative interaction data.
- The specific hotspot at residues R268-F276 is stated without evidence of its significance or functional relevance.
- The reported effects of RRM2, NTD, and polyA on packing and viscoelasticity are unsupported without numerical data and statistical analysis.
- The statement that "RRMs enhance viscosity, whereas the NTD reduces it" and "polyA increases elasticity" are presented as definitive but lack supporting measurements.
- The overall conclusion that multidomain structure and RNA "orchestrate condensate organization" is a reasonable interpretation but is not directly demonstrated by the abstract's findings.