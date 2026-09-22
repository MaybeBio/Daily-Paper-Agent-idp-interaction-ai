## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors use molecular dynamics (MD) simulations and density functional theory (DFT) calculations to propose a mechanism by which disulfiram ejects zinc from the zinc finger (Zf) site of HCV NS5A domain-1, involving disulfiram-induced conformational changes and weakening of the Cys39–Zn interaction.
- **Visible evidence base** Abstract text only; no quantitative results, methodological details, or validation data are provided
- **Missing materials affecting confidence** Full manuscript, simulation parameters, force fields, DFT functional/basis set details, convergence criteria, statistical analyses, figures, and any experimental validation

## Reviewer
- **Overall assessment** The abstract presents a plausible computational study addressing a biologically and therapeutically relevant question, namely the mechanism of zinc ejection from NS5A by disulfiram. However, the level of detail provided is insufficient to evaluate the technical soundness of the MD and DFT approaches, the robustness of the conclusions, or the novelty relative to existing literature. The central mechanistic claim, that disulfiram acts primarily through conformational ensemble changes and specific weakening of the Cys39–Zn interaction, is stated without supporting quantitative evidence. As presented, the case is not established.
- **Who would be interested in the results, and why** Researchers in computational biophysics and drug discovery, particularly those studying zinc finger proteins, viral replication complexes, and repurposing of approved drugs such as disulfiram. The proposed mechanism could inform structure-based design of NS5A inhibitors, which is relevant to HCV therapeutic development.
- **Major strengths** The study addresses a clinically relevant target and a repurposed drug with known anti-HCV activity. The combination of MD and DFT is appropriate for probing both dynamic and electronic aspects of metal ejection. The three-state design (apo, holo, and drug-bound) provides a logical framework for dissecting the mechanism.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that MD results indicate disulfiram triggers Zn ejection predominantly through altering the overall conformation ensemble.
  - **Evidence pointer** Abstract, location not provided
  - **Concern** No quantitative metrics are provided to support this claim. It is unclear what conformational changes were observed, how they were quantified, whether replicate simulations were performed, and whether the ensemble shift is statistically significant relative to the apo and holo states.
  - **Why it matters** The central mechanistic conclusion rests on this claim. Without evidence of convergence, sampling adequacy, and statistical comparison across states, the assertion that conformational ensemble alteration is the predominant trigger cannot be assessed.
  - **Resolution test** Provide quantitative descriptors of conformational ensembles, such as RMSD, RMSF, principal component projections, or free energy surfaces, with error bars and statistical tests comparing A, B, and C states. Demonstrate that observed differences exceed thermal fluctuations and are reproducible across independent simulations.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that DFT assessment demonstrates a tetrahedral configuration of Zn with four Cys residues, indicating a stable protein structure morphology.
  - **Evidence pointer** Abstract, location not provided
  - **Concern** The DFT calculation is described only in terms of its conclusion. No information is provided on the model system, level of theory, basis set, solvation treatment, or how the protein environment was represented. The claim of stability based on geometry alone is insufficient without energetic or vibrational analysis.
  - **Why it matters** DFT results are used to support the structural stability of the Zf site. If the model or method is inappropriate, the conclusion may be artefactual. The absence of methodological detail prevents any assessment of reliability.
  - **Resolution test** Specify the DFT protocol, including functional, basis set, solvation model, and truncation scheme. Provide computed Zn–S bond lengths and angles, binding energies, and comparison with experimental or high-level reference data. Show that the tetrahedral geometry is energetically preferred over alternative coordination states.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Support for conclusions
  - **Claim pointer** The authors claim that disulfiram binding introduces new interactions of Cys39 with disulfiram and weakens the interaction of this residue with Zn, causing zinc ejection.
  - **Evidence pointer** Abstract, location not provided
  - **Concern** The specific role of Cys39 is asserted without any quantitative data, such as interaction energies, distance trajectories, or occupancy analyses. It is unclear whether Cys39 is the only residue affected, whether other Cys residues contribute, and whether the observed weakening is sufficient to explain ejection.
  - **Why it matters** This is the proposed molecular mechanism. If the evidence for Cys39-specific effects is weak or confounded by other factors, the mechanism may be incorrect or incomplete.
  - **Resolution test** Provide time-resolved distances between Zn and each Cys sulfur, interaction energy decomposition for Cys39 versus other residues, and a clear correlation between disulfiram binding and loss of Zn coordination. Show that the effect is specific to Cys39 and not a general consequence of conformational change.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Terminology
  - **Evidence pointer** Abstract, location not provided
  - **Issue** The term "zinc ejection" is used without operational definition. It is unclear whether this refers to complete loss of Zn from the binding site, partial dissociation, or a shift in coordination geometry.
  - **Required correction** Define "ejection" in terms of a measurable criterion, such as a distance threshold or coordination number change, and apply it consistently.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Comparison to prior work
  - **Evidence pointer** Abstract, location not provided
  - **Issue** The abstract states the mechanism is "poorly understood" but does not summarize prior computational or experimental studies on disulfiram and NS5A. This makes it difficult to judge novelty.
  - **Required correction** Briefly state what is known and what specific gap this study fills, with reference to key prior findings.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Simulation details
  - **Evidence pointer** Abstract, location not provided
  - **Issue** No information is given on simulation length, number of replicas, temperature, pressure, or force field. These details are essential for reproducibility.
  - **Required correction** Include key simulation parameters in the abstract or indicate that they are fully described in the main text.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3. The abstract does not provide sufficient quantitative or methodological evidence to support the central mechanistic claims. Without these details, the conclusions are not verifiable.
- **Assessment against Nature-style criteria**  
  Originality: The question of disulfiram-mediated zinc ejection in NS5A is of interest, but the abstract does not demonstrate how this work advances beyond existing knowledge. The proposed mechanism, while plausible, is not shown to be novel.  
  Scientific importance: The topic is relevant to HCV therapeutics and drug repurposing, but the significance of the findings cannot be assessed without evidence of mechanistic insight that would change current understanding or guide experimental testing.  
  Interdisciplinary readership: The work bridges computational chemistry and virology, which could appeal to a broad audience. However, the abstract is written in a way that assumes familiarity with both MD and DFT, and the lack of context may limit accessibility.  
  Technical soundness: Not assessable from the abstract. The absence of methodological detail and quantitative results prevents evaluation of the reliability of the simulations and calculations.  
  Readability for nonspecialists: The abstract is concise but uses domain-specific terms without explanation. A nonspecialist would struggle to understand the significance of the three states or the meaning of "conformational ensemble alteration."
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a plausible hypothesis but does not provide the technical or quantitative support needed to validate the proposed mechanism. A revised manuscript with full methodological detail, statistical analysis, and clear evidence linking disulfiram binding to zinc ejection would be required for a supportive assessment.

## Risk / unsupported claims
- The claim that disulfiram triggers zinc ejection predominantly through conformational ensemble alteration is unsupported by any quantitative data in the abstract.
- The claim that DFT demonstrates a stable tetrahedral Zn coordination is unsupported without specification of the computational protocol and energetic analysis.
- The claim that Cys39 interactions with disulfiram weaken the Zn–Cys39 bond and cause ejection is asserted without evidence of specificity or causality.
- The therapeutic potential of disulfiram is stated as a conclusion but is not supported by any functional or experimental data in the abstract.