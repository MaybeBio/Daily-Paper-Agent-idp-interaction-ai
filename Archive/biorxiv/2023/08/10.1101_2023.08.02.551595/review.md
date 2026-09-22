## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the supplied abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors use molecular dynamics simulations and cell culture experiments to characterize the membrane binding of the disordered C-terminal polybasic motif of LKB1 to model membranes containing POPC and phosphatidic acid. They report that electrostatic interactions drive binding, that the first three lysines are dispensable for significant binding, that binding induces non-monotonous structural changes in both protein and membrane, and that a statistical fluctuation model captures the thermodynamics of the dynamic protein-lipid interplay.
- **Visible evidence base** Abstract text only; no quantitative data, simulation parameters, experimental protocols, or statistical analyses are visible
- **Missing materials affecting confidence** Full manuscript, simulation methodology and convergence criteria, force field parameters, experimental details for cell culture and GFP-LKB1 variants, quantitative binding measurements, structural analysis details, and the statistical model formulation

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting biophysical study of how a disordered polybasic region binds anionic membranes, with relevance to LKB1 activation. The combination of MD simulations and cell culture experiments is commendable in principle. However, the abstract alone provides insufficient quantitative detail to evaluate the robustness of the central claims. The claim that the first three lysines are dispensable is presented without supporting data, and the statistical model is mentioned but not described. The non-monotonous structural changes are asserted without specifics. While the topic is timely and the approach is reasonable, the evidence base visible here does not establish the case.
- **Who would be interested in the results, and why** Researchers studying peripheral membrane protein binding, intrinsically disordered proteins, lipid-protein interactions, and signaling pathways involving LKB1. The work could also interest computational biophysicists developing models for protein-membrane interactions and experimentalists working on anionic lipid signaling.
- **Major strengths** The study addresses a biologically relevant question with clear mechanistic focus. The combination of simulation and experiment is appropriate for the problem. The identification of a statistical fluctuation model to capture the thermodynamics of dynamic binding is conceptually appealing. The potential transferability of findings to other polybasic region-containing proteins broadens the impact.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: The specific system (LKB1 polybasic motif with PA-containing membranes) appears novel, and the dynamic interplay model is potentially original, but the abstract does not clearly differentiate from prior work on polybasic lipid-binding motifs. Scientific importance: LKB1 is a relevant kinase, and understanding its membrane recruitment mechanism has biological significance, but the abstract does not establish broader importance beyond the specific system. Interdisciplinary readership: The work bridges computational biophysics and cell biology, which could appeal to multiple communities, but the abstract is too terse to engage nonspecialists effectively. Technical soundness: Cannot be assessed from the abstract alone; no quantitative validation or methodological detail is visible. Readability for nonspecialists: The abstract is reasonably clear but uses jargon without sufficient context, and the logical flow from simulation to experiment to model is compressed.
- **Recommendation posture** Currently not established from the provided evidence. The abstract suggests a potentially valuable study, but the visible material is insufficient to support the central claims. A full manuscript with quantitative data and methodological detail would be required for a supportive assessment.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The claim that "for significant binding the first three lysines turn out to be dispensable, which was also recapitulated in cell culture using transfected GFP-LKB1 variants" is central to the paper's mechanistic conclusion.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract asserts that the first three lysines are dispensable for significant binding, but no quantitative data are provided. It is unclear what threshold defines "significant binding," how binding was measured in simulations (e.g., contact counts, free energy, residence times), and what experimental readout was used in cell culture (e.g., membrane localization, phosphorylation, activity). Without these details, the claim cannot be evaluated.
- **Why it matters** This claim is the primary mechanistic finding of the study. If the evidence is weak or the threshold arbitrary, the conclusion about which residues matter for binding would be unsupported, undermining the paper's contribution.
- **Resolution test** Provide quantitative binding data for full-length and truncated variants, including statistical comparisons, in both simulations and experiments. Specify the binding metric and the significance threshold used.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Model validation
- **Claim pointer** The claim that "the thermodynamics of this interplay is captured by a statistical fluctuation model, which allows the estimation of both energies" implies the model is validated and provides reliable energy estimates.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The statistical fluctuation model is mentioned but not described. No equations, assumptions, fitting procedures, or comparison to simulation or experimental data are provided. It is impossible to assess whether the model is physically justified, whether it reproduces the observed dynamics, or whether the estimated energies are reliable.
- **Why it matters** The model is presented as a key outcome that quantifies the interplay between PA-PA repulsion and protein-PA attraction. Without model details and validation, this part of the work is not assessable and could be an overinterpretation of simulation data.
- **Resolution test** Present the model formulation, its assumptions, and a quantitative comparison of model predictions to simulation or experimental measurements, including error estimates for the derived energies.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The claim that "LKB1-membrane binding results in non-monotonous changes in the structure of the protein as well as of the membrane, in particular accumulation of PAs and reduced thickness at the protein-membrane contact area" is presented as a key finding.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract states non-monotonous structural changes but does not specify what is non-monotonous (e.g., as a function of time, lipid concentration, or peptide length). The PA accumulation and reduced membrane thickness are mentioned without quantitative measures or context. The term "non-monotonous" is ambiguous here.
- **Why it matters** Structural changes in the membrane and protein are central to the proposed mechanism. Without clear definition and quantitative support, the claim is vague and cannot be verified.
- **Resolution test** Define the variable over which changes are non-monotonous, provide quantitative measurements (e.g., membrane thickness profiles, lipid density maps, protein conformational metrics) with error bars, and show the non-monotonic trend explicitly.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Background statement
- **Evidence pointer** Abstract, first sentence
- **Issue** The opening sentence states that intrinsically disordered regions are responsible for many biological processes, but the connection to LKB1 is abrupt. The relevance of the disordered C-terminal region to LKB1 function is stated but not contextualized.
- **Required correction** Briefly explain why LKB1 membrane recruitment is biologically important and how the disordered region contributes, to orient the reader.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Non-monotonous"
- **Evidence pointer** Abstract, structural changes sentence
- **Issue** The term "non-monotonous" is used without specifying the independent variable. This is ambiguous and could confuse readers.
- **Required correction** Specify the variable over which changes are non-monotonous, e.g., "as a function of peptide concentration" or "over simulation time."

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Generalizability
- **Affected element** Transferability claim
- **Evidence pointer** Abstract, final sentence
- **Issue** The claim that "these results can be likely transferred to other proteins" is speculative and not supported by any comparative analysis in the abstract.
- **Required correction** Either soften the claim to a suggestion for future work or provide a brief rationale based on sequence or structural similarities with other polybasic regions.

## Risk / unsupported claims
- The dispensability of the first three lysines for significant binding is unsupported without quantitative binding data and a defined significance threshold.
- The statistical fluctuation model and its energy estimates are unassessable from the abstract alone.
- The non-monotonous structural changes in protein and membrane are asserted without definition of the variable or quantitative evidence.
- The transferability of results to other proteins is speculative and not supported by comparative data.
- The claim that binding effects are "due to" electrostatic interactions is plausible but not quantitatively demonstrated in the abstract.