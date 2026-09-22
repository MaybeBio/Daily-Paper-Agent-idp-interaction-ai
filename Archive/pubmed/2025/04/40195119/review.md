## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no full text, figures, tables, or supplementary materials provided
- **Shared manuscript claim summary** The authors use residue-resolution molecular dynamics simulations to study phase separation in mixtures of four transcription factors (Oct4, Sox2, Klf4, Nanog) from embryonic stem cells. They report that condensates are enriched in Sox2, Klf4, and Nanog, with Klf4 as the most abundant and proposed scaffold, while Oct4 remains mostly in the dilute phase and acts as a client via interaction with Sox2. The study concludes that heterogeneous intermolecular interactions among transcription factors are important for condensate formation.
- **Visible evidence base** Abstract text only; no simulation details, force field parameters, system sizes, timescales, convergence criteria, or quantitative results are provided
- **Missing materials affecting confidence** Full manuscript, simulation methodology, force field validation, system setup, equilibration protocols, quantitative composition data, interaction energy analyses, control simulations, and any experimental validation

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting computational study on heterogeneous biomolecular condensates involving four transcription factors. The topic is timely and relevant to the growing field of phase separation in gene regulation. However, the abstract alone provides insufficient detail to evaluate the technical soundness of the simulations or the robustness of the conclusions. The central claims regarding Klf4 as a scaffold and Oct4 as a client rest on interaction analyses that are not described. The study's significance would depend on whether the simulations are adequately sampled, whether the force field is appropriate for disordered or partially disordered proteins, and whether the results are validated against experimental observations.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular phase separation, transcriptional regulation, stem cell biology, and computational biophysics would be interested. The study addresses a gap in understanding heterogeneous multicomponent condensates, which is relevant to nuclear organization and gene control. Computational biophysicists would be interested in the methodological approach, while stem cell biologists would be interested in the specific transcription factor system.
- **Major strengths** The study addresses a relevant and under-explored question about heterogeneous condensates with multiple components. The choice of four master transcription factors in embryonic stem cells is biologically meaningful. The use of residue-resolution molecular dynamics simulations is appropriate for capturing protein-level interactions. The proposed scaffold-client model for Klf4 and Oct4, respectively, provides a testable conceptual framework.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: The study addresses a relevant gap in heterogeneous multicomponent condensates, which is a relatively underexplored area. However, the conceptual advance over existing single- or two-component condensate studies is incremental unless the simulations reveal unexpected mechanisms. Scientific importance: The biological system is important, but the abstract does not establish whether the findings have broad implications beyond this specific set of proteins. Interdisciplinary readership: The topic bridges biophysics and stem cell biology, but the abstract is written in a way that is accessible to both communities. Technical soundness: Cannot be assessed from the abstract alone; no methodological details are provided. Readability for nonspecialists: The abstract is clear and concise, though terms like "residue-resolution" and "dilute phase" may require some background knowledge.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents plausible claims, but the lack of methodological detail and quantitative results prevents a supportive recommendation. A full manuscript with adequate simulation validation and analysis would be required to assess the case.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The study used residue-resolution molecular dynamics simulations to investigate heterogeneous protein assemblies of Oct4, Sox2, Klf4, and Nanog.  
- **Evidence pointer** Abstract, Methods section not provided  
- **Concern** The abstract provides no information about the simulation methodology, including the force field used, the protein models, the system size, the simulation timescale, the number of replicas, or the equilibration protocol. Without these details, it is impossible to assess whether the simulations are adequately converged or whether the results are artifacts of the chosen parameters.  
- **Why it matters** Molecular dynamics simulations of phase separation are highly sensitive to force field parameters and system size. If the simulations are not sufficiently long or large, the observed condensate composition and dynamics may not reflect equilibrium behavior. The central claims about Klf4 as a scaffold and Oct4 as a client depend on the reliability of the simulated interactions.  
- **Resolution test** Provide a detailed Methods section describing the force field, system construction, simulation length, number of replicas, and convergence checks. Show that the condensate composition and protein distributions are stable over time and independent of initial conditions.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence strength  
- **Claim pointer** The condensate forms loosely interacting clusters where Klf4 is the most abundant, suggesting that Klf4 serves as a scaffold of the condensate, and Sox2 and Nanog are bound to Klf4 for stabilizing the condensate.  
- **Evidence pointer** Abstract, Results section not provided  
- **Concern** The abstract states that Klf4 is the most abundant and proposes a scaffold role, but no quantitative data are provided to support this claim. No enrichment ratios, interaction energies, or contact frequencies are reported. The claim that Sox2 and Nanog bind to Klf4 for stabilization is presented without supporting interaction analysis.  
- **Why it matters** The scaffold-client model is the central conceptual contribution of the study. Without quantitative evidence of Klf4's abundance and its specific interactions with Sox2 and Nanog, the claim is unsupported. The distinction between a scaffold and a client is meaningful only if interaction strengths and occupancies are quantified.  
- **Resolution test** Provide quantitative data on protein composition within condensates versus the dilute phase, pairwise interaction energies or contact probabilities, and a comparison of interaction strengths among all protein pairs. Show that Klf4 interactions are stronger or more numerous than others and that removing Klf4 destabilizes the condensate in a control simulation.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence strength  
- **Claim pointer** Oct4 is moderately recruited to the condensate, serving as a client mainly via its interaction with Sox2.  
- **Evidence pointer** Abstract, Results section not provided  
- **Concern** The claim that Oct4 is a client recruited via interaction with Sox2 is presented without supporting data. No interaction analysis between Oct4 and Sox2 is described, and no comparison with Oct4 interactions with other proteins is provided. The term "moderately recruited" is vague and not quantified.  
- **Why it matters** The proposed client role for Oct4 is a specific mechanistic claim. If Oct4's recruitment is instead driven by interactions with Klf4 or Nanog, or by non-specific effects, the model would need revision. The claim also has biological implications for how Oct4 functions in stem cell regulation.  
- **Resolution test** Provide quantitative interaction data for Oct4 with each of the other three proteins, showing that Oct4-Sox2 interactions are the dominant contributor to Oct4 recruitment. Include a control simulation where Sox2 is absent to demonstrate that Oct4 recruitment is reduced.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Scientific importance  
- **Claim pointer** This study highlights the importance of intermolecular interaction between different transcription factors on the condensate formations with heterogeneous biomolecular components.  
- **Evidence pointer** Abstract, Discussion section not provided  
- **Concern** The abstract does not explain how the findings extend beyond the specific system studied. It is unclear whether the proposed scaffold-client mechanism is generalizable to other transcription factor condensates or whether it is specific to Oct4, Sox2, Klf4, and Nanog. No comparison with experimental data or with simpler two-component systems is mentioned.  
- **Why it matters** The broader significance of the study depends on whether the findings provide general principles for heterogeneous condensate formation. If the results are system-specific, the impact is limited to the stem cell transcription factor community.  
- **Resolution test** In the full manuscript, discuss how the observed interaction patterns compare with known properties of these proteins and whether the scaffold-client model could apply to other transcription factor families. If possible, include a comparison with experimental data on these condensates.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Abstract, first sentence  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The phrase "liquid-liquid phase separation" is used without defining whether the simulations model this process explicitly or infer it from clustering behavior.  
- **Required correction** Clarify whether the simulations directly observe phase separation or whether condensate formation is inferred from protein clustering and density distributions.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Terminology  
- **Affected element** Abstract, scaffold and client terminology  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The terms "scaffold" and "client" are used without definition. These terms have specific meanings in the phase separation literature, and it is unclear whether they are used in the standard sense.  
- **Required correction** Define scaffold and client in the context of this study, or use alternative terminology if the intended meaning differs from the standard usage.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Abstract, simulation details  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The abstract does not state the temperature, salt concentration, or other solution conditions used in the simulations. These parameters can strongly affect phase separation behavior.  
- **Required correction** Include key simulation conditions in the abstract or indicate that they are described in the full manuscript.

## Risk / unsupported claims
- The claim that Klf4 serves as a scaffold is unsupported without quantitative abundance and interaction data.
- The claim that Oct4 is a client recruited via Sox2 interaction is unsupported without interaction analysis.
- The claim that Sox2 and Nanog stabilize the condensate via binding to Klf4 is unsupported without stability or interaction data.
- The general statement about the importance of intermolecular interactions between different transcription factors is plausible but not substantiated with comparative or mechanistic evidence in the abstract.
- The overall simulation results cannot be evaluated for reliability without methodological details.