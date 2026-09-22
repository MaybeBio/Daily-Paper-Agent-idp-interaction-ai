## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, tables, or supplementary material were provided
- **Shared manuscript claim summary** The authors use coarse-grained molecular dynamics simulations of polyPR peptides and a yeast NPC model to propose that polyPR does not aggregate or bind permanently to FG-Nups, but translocates through the central low-density region, with longer polyPRs experiencing a higher energy barrier and narrower translocation channel, and that interactions are predominantly steric with minor contributions from cation-pi, hydrophobic, and electrostatic forces.
- **Visible evidence base** Abstract text only; no quantitative results, simulation parameters, or validation data are visible
- **Missing materials affecting confidence** Full methods, simulation details (force field, system size, timescales, replicates), quantitative energy barrier values, trajectory analysis, comparison to experimental data, and all figures or tables

## Reviewer
- **Overall assessment** The abstract presents a plausible computational study addressing a relevant question in C9orf72-linked neurodegeneration. The central claims are internally consistent and potentially interesting, but the abstract alone provides insufficient detail to evaluate the technical rigor, statistical robustness, or biological relevance of the findings. The conclusions are stated with confidence that exceeds what can be verified from the supplied material.
- **Who would be interested in the results, and why** Researchers studying nucleocytoplasmic transport defects in amyotrophic lateral sclerosis and frontotemporal dementia, computational biophysicists modeling intrinsically disordered proteins and nuclear pore complexes, and experimentalists investigating dipeptide repeat protein toxicity would find these results relevant. The proposed mechanism of size-dependent steric translocation could inform hypotheses about polyPR pathology and guide experimental validation.
- **Major strengths** The study addresses a timely and important question with a well-established computational approach. The abstract clearly states the main findings and distinguishes them from prior proposals of aggregation or permanent binding. The focus on the yeast NPC model is a reasonable simplification that may allow systematic analysis.
- **Major Concerns** The abstract lacks quantitative details that are essential to assess the strength of the claims. No simulation parameters, error estimates, or comparisons to experimental data are provided. The claim that interactions are "mainly steric" with "small contribution" of specific interactions is not supported by any numerical evidence in the abstract. The biological relevance of the yeast NPC model for human C9orf72 pathology is not discussed.
- **Minor Comments** The abstract would benefit from stating the specific polyPR lengths studied and the range of energy barriers observed. The phrase "size-dependent manner" is vague without quantitative context. The relationship between the simulation findings and the proposed mechanisms of NCT disruption listed in the introduction is not explicitly clarified.
- **Technical failings that need to be addressed before the case is established** The absence of any quantitative results, simulation validation, or convergence analysis in the visible material means the core claims cannot be independently assessed. The abstract alone does not establish that the simulations are statistically robust or that the model faithfully represents the relevant biophysical environment.
- **Assessment against Nature-style criteria** Originality: moderate, as computational studies of polyPR and NPC interactions exist, but the specific focus on steric translocation is a useful contribution. Scientific importance: high, given the disease relevance and ongoing debate about polyPR mechanisms. Interdisciplinary readership: the topic bridges biophysics, cell biology, and neurodegeneration, but the abstract is written primarily for a specialized computational audience. Technical soundness: not assessable from the abstract alone. Readability for nonspecialists: the abstract is clear but assumes familiarity with FG-Nups and coarse-grained modeling.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a coherent narrative, but the lack of quantitative support and methodological detail prevents a definitive assessment. A supportive posture would require access to the full manuscript.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that polyPR translocates through the NPC following a trajectory through the central low-density region, with longer polyPRs experiencing a higher energy barrier and narrower translocation channel.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract provides no quantitative data on energy barriers, channel widths, or trajectory statistics. Without these values, it is impossible to assess whether the observed differences between polyPR lengths are statistically significant or biologically meaningful.
- **Why it matters** The central mechanistic claim depends on quantitative comparisons. If the energy barrier differences are within simulation noise, the conclusion of size-dependent translocation is unsupported.
- **Resolution test** Provide numerical values for energy barriers and channel widths for each polyPR length, with error estimates and statistical tests, in the full manuscript.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that polyPR and FG-Nups are mainly engaged in steric interactions with only a small contribution of specific cation-pi, hydrophobic, and electrostatic interactions.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract does not report any interaction energy decomposition or contact analysis. The relative contributions of different interaction types are stated without supporting numbers.
- **Why it matters** This claim distinguishes the proposed mechanism from prior work emphasizing specific interactions. Without quantitative decomposition, the claim is not verifiable.
- **Resolution test** Include a breakdown of interaction energies by type (steric, cation-pi, hydrophobic, electrostatic) with standard deviations, and show that steric contributions dominate across all polyPR lengths.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The study uses coarse-grained molecular dynamics models of polyPR and the yeast NPC lined with FG-Nups.
- **Evidence pointer** Abstract, location not provided
- **Concern** No simulation parameters are given, including force field, system size, simulation length, number of replicates, or temperature and ionic conditions. The yeast NPC model is not described in terms of its composition or validation.
- **Why it matters** Reproducibility is a core requirement for computational studies. Without these details, the results cannot be replicated or compared to other models.
- **Resolution test** Provide full simulation methods in the manuscript, including all parameters, system construction, equilibration protocol, and production run lengths, plus a validation of the NPC model against experimental or prior computational data.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors imply that their findings provide insight into polyPR-mediated NCT defects, but the abstract does not connect the simulation results to the proposed mechanisms of NCT disruption.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract lists several proposed mechanisms (NPC accumulation, nucleolar accumulation, transport receptor interactions) but does not explain how the observed steric translocation relates to these mechanisms or to the toxicity of polyPR.
- **Why it matters** The disease relevance of the study depends on this connection. Without it, the findings remain a biophysical observation with unclear biological implications.
- **Resolution test** In the discussion, explicitly state how the simulation results support or refute each proposed mechanism and what the implications are for polyPR toxicity in cellular models.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract, first sentence
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract states that polyPR is "the most toxic" among the five dipeptide repeat proteins, but this is presented without citation or context.
- **Required correction** Add a citation or specify the experimental context in which this toxicity ranking was established.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract, final sentence
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "size-dependent manner" is vague and could refer to polyPR length, molecular weight, or another property.
- **Required correction** Specify that the size dependence refers to polyPR chain length and provide the range of lengths studied.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scope
- **Affected element** Abstract, model choice
- **Evidence pointer** Abstract, location not provided
- **Issue** The use of a yeast NPC model is mentioned, but the rationale for this choice and its relevance to human disease is not explained.
- **Required correction** Add a sentence justifying the yeast model and noting any expected differences from the human NPC.

## Risk / unsupported claims
- The claim that polyPR does not aggregate within the NPC or bind permanently to FG-Nups is unsupported in the abstract, as no binding or aggregation analysis is described.
- The claim that polyPR follows a trajectory through the central low-density region is unsupported without trajectory density maps or quantitative analysis.
- The claim that longer polyPRs have a higher energy barrier and narrower translocation channel is unsupported without numerical values.
- The claim that interactions are mainly steric with small contributions from specific interactions is unsupported without energy decomposition data.
- The biological relevance of the findings to C9orf72-mediated NCT defects is not established from the abstract alone.