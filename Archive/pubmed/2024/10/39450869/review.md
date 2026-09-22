## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors use coarse-grained molecular dynamics simulations of the amyloid-beta fragment Abeta(16-22) with mixed phosphatidylserine/phosphatidylcholine bilayers to propose a dual role for anionic lipids in amyloid aggregation. They report that anionic lipid enrichment enhances peptide adsorption, that aggregation kinetics are modulated by competing factors (local concentration enhancement versus peptide-lipid interactions), and that higher anionic lipid fractions produce smaller, more ordered aggregates and induce lipid demixing with PS cluster formation.
- **Visible evidence base** Abstract text only; no simulation details, system setup, force field parameters, convergence criteria, or quantitative results are visible
- **Missing materials affecting confidence** Full manuscript, simulation methodology, force field validation, system size and timescales, replicate information, quantitative aggregation metrics, lipid demixing analysis, and any comparison to experimental data

## Reviewer
- **Overall assessment** The abstract presents a plausible mechanistic hypothesis for the dual role of anionic lipids in amyloid aggregation, supported by a simulation approach that is appropriate in principle. However, the abstract alone provides insufficient detail to evaluate the technical soundness of the simulations, the robustness of the findings, or the strength of the evidence for the proposed mechanism. The central claims are qualitatively stated without quantitative support, and the relationship to the conflicting experimental literature is asserted rather than demonstrated. The work may be of interest to the membrane biophysics and protein aggregation communities, but the case is not established from the supplied material.
- **Who would be interested in the results, and why** Researchers studying membrane-mediated protein aggregation in neurodegenerative diseases, particularly those focused on amyloid-beta interactions with lipid bilayers. Computational biophysicists interested in coarse-grained simulations of peptide-membrane systems and lipid demixing phenomena would also find the work relevant. The proposed dual mechanism could inform experimental design for studying anionic lipid effects on aggregation kinetics.
- **Major strengths** The abstract addresses a clearly identified knowledge gap regarding conflicting literature on anionic lipid effects. The use of a well-defined model peptide fragment and systematic variation of lipid composition provides a clean framework for isolating the role of anionic lipids. The proposed dual mechanism is mechanistically plausible and offers a potential resolution to conflicting experimental observations.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: The dual mechanism concept is not entirely novel, as competing effects of membrane interactions on aggregation have been discussed in the literature, but the specific combination of adsorption enhancement and kinetic retardation in a single simulation study may offer a fresh perspective. Scientific importance: The topic is relevant to a major disease class, but the abstract does not demonstrate that the findings extend beyond the specific model system. Interdisciplinary readership: The work bridges computational biophysics and neurobiology, but the abstract is written in a specialized manner that may limit accessibility. Technical soundness: Cannot be assessed from the abstract alone; no methodological details or validation are provided. Readability for nonspecialists: The abstract is reasonably clear but uses field-specific terminology without sufficient context for a broad audience.
- **Recommendation posture** Currently not established from the provided evidence. The hypothesis is interesting and the approach is appropriate, but the abstract lacks the quantitative and methodological detail required to assess the validity of the claims. A full manuscript with detailed methods and results would be needed to evaluate whether the case can be made.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The simulations reveal that membranes enriched in anionic lipids enhance peptide adsorption and interaction kinetics.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract provides no information on the simulation methodology, including force field parameters, system size, simulation timescales, number of replicates, or equilibration protocols. Without these details, it is impossible to assess whether the observed adsorption enhancement is robust or an artifact of the specific simulation setup.
- **Why it matters** Coarse-grained simulations are highly sensitive to parameter choices and finite-size effects. The claim of enhanced adsorption with anionic lipid content is central to the proposed mechanism, and if the simulations are underconverged or under-sampled, the conclusion may not be reliable.
- **Resolution test** Provide full methodological details in the manuscript, including force field validation, system composition, simulation length, replicate numbers, and convergence checks. Show that the adsorption enhancement is consistent across independent simulations and robust to reasonable parameter variations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** Aggregation dynamics was modulated by two competing factors: increased local peptide concentration near negatively charged membranes, which promoted aggregation, and peptide-lipid interactions, which slowed it down.
- **Evidence pointer** Abstract, location not provided
- **Concern** The dual mechanism is stated as a finding, but no quantitative data are presented to support the relative contributions of the two competing factors. No metrics for aggregation kinetics, such as cluster size distributions, aggregation rates, or free energy barriers, are provided. The claim that higher anionic lipid percentages lead to smaller and more ordered aggregates is also presented without numerical support.
- **Why it matters** The dual mechanism is the central contribution of the work. Without quantitative evidence distinguishing the two effects and demonstrating their relative magnitudes, the claim remains speculative rather than established.
- **Resolution test** Present quantitative aggregation metrics as a function of lipid composition, such as time-resolved cluster size distributions, aggregation rate constants, and order parameters. Provide a quantitative decomposition of the two competing effects, for example through control simulations or free energy analysis.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** External validity
- **Claim pointer** These findings contribute to understanding membrane-mediated peptide aggregation in neurodegenerative disorders, potentially guiding new therapeutic strategies.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract does not connect the simulation results to experimental observations or to the broader context of neurodegenerative disease. The conflicting literature on anionic lipid effects is mentioned but not reconciled with the present findings. No comparison to experimental aggregation kinetics or membrane binding data is provided.
- **Why it matters** The stated significance of the work depends on its relevance to disease mechanisms and its ability to resolve existing controversies. Without any link to experimental evidence or a discussion of how the simulation results relate to known biological behavior, the broader claims are unsupported.
- **Resolution test** Include a discussion section that explicitly compares the simulation findings to experimental studies on anionic lipid effects on amyloid aggregation. If direct comparison is not possible, clearly state the limitations and the conditions under which the simulation predictions could be tested experimentally.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract, location not provided
- **Issue** The term "interaction kinetics" is used without definition, and it is unclear whether this refers to peptide-lipid binding rates, peptide-peptide encounter rates, or something else.
- **Required correction** Define "interaction kinetics" explicitly in the abstract or use more precise terminology such as "peptide-membrane binding kinetics" or "peptide-peptide association kinetics."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** System description
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract states that 0%, 10%, and 30% PS compositions were examined, but it does not specify the total lipid count, the peptide concentration, or the peptide-to-lipid ratio. These parameters are critical for interpreting the results.
- **Required Correction** Add the system size and peptide-to-lipid ratio to the abstract or refer to a methods section where these details are provided.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Generalizability
- **Affected element** Model system choice
- **Evidence pointer** Abstract, location not provided
- **Issue** The study uses a single peptide fragment, Abeta(16-22), which is a minimal model. The abstract does not discuss how the findings might generalize to full-length Abeta or other amyloidogenic peptides.
- **Required Correction** Add a sentence acknowledging the limitations of the model peptide and discussing the potential for extrapolation to full-length systems, or explicitly state that generalization is not claimed.

## Risk / unsupported claims
- The claim that anionic lipid enrichment enhances peptide adsorption is unsupported without quantitative data or methodological details.
- The dual mechanism of competing factors is presented as a finding but is not quantitatively demonstrated.
- The claim that higher anionic lipid percentages lead to smaller and more ordered aggregates is unsupported without numerical evidence.
- The claim that findings contribute to understanding neurodegenerative disease mechanisms and could guide therapeutic strategies is not supported by any connection to experimental or clinical data.
- The relationship between the simulation results and the conflicting experimental literature is asserted but not demonstrated.