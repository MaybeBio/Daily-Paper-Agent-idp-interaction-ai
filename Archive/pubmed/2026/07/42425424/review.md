## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors report atomistic molecular dynamics simulations of the human SOST-LRP6 E1E2 ectodomain complex, proposing that SOST engages LRP6 through two coordinated regions, namely loop 2 (including the NAI motif) interacting with the E1 domain and the C-terminal region (including the HNQS motif and downstream residues) interacting with the E2 domain. They further claim that these extended interactions explain the higher binding affinity of full-length SOST relative to truncated variants, and that their findings reveal an anchor-stabilized, chemically diverse interaction network that contrasts with prior structural studies.
- **Visible evidence base** Abstract text only; no simulation parameters, system setup, convergence criteria, statistical analyses, or comparative experimental data are provided
- **Missing materials affecting confidence** Full methods, simulation duration and replicates, force field parameters, system size and solvation details, binding free energy calculations, structural figures, validation against experimental mutagenesis or binding data, and any statistical uncertainty estimates

## Reviewer
- **Overall assessment** The abstract presents a plausible and potentially valuable computational investigation of a clinically relevant protein-protein interaction. The proposed two-region binding model is biologically reasonable and consistent with prior biochemical hints of multivalent engagement. However, the current evidence base is insufficient to evaluate the technical rigor of the simulations or the robustness of the central claims. The abstract makes strong mechanistic assertions without providing quantitative metrics, convergence evidence, or experimental corroboration. The claim of contrast with prior structural studies is particularly under-supported given the absence of specific comparative details.
- **Who would be interested in the results, and why** Researchers in bone biology and Wnt signaling, structural biologists studying protein-protein interactions involving intrinsically disordered regions, computational biophysicists developing methods for simulating flexible protein complexes, and pharmaceutical scientists targeting SOST-LRP6 for osteoporosis therapeutics would find these results relevant. The proposed mechanistic model could inform future drug design efforts and experimental validation studies.
- **Major strengths** The study addresses a biologically important and therapeutically relevant question with clear translational implications. The focus on full-length SOST including disordered regions is a methodological improvement over truncated constructs. The proposed two-region binding model provides a testable hypothesis that reconciles prior biochemical observations. The abstract is clearly written and accessible to a broad readership.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3  
  - R1-m4
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria**  
  Originality: The proposed two-region binding model with anchor-stabilized dynamic remodeling is moderately original, but the abstract does not clearly differentiate it from prior computational or structural work beyond a general statement of contrast.  
  Scientific importance: The biological question is important, and a validated mechanistic model would be valuable, but the abstract does not yet establish the significance of the specific findings.  
  Interdisciplinary readership: The topic bridges structural biology, computational biophysics, and bone biology, which could attract broad interest if the evidence were robust.  
  Technical soundness: Cannot be assessed from the abstract alone; critical simulation details and validation metrics are absent.  
  Readability for nonspecialists: The abstract is well written and understandable, though some domain-specific terms (e.g., NAI motif, HNQS motif) are used without definition.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents an interesting hypothesis, but the technical basis and validation are insufficient to support the strong mechanistic claims. A supportive posture would require access to the full manuscript demonstrating simulation rigor and experimental corroboration.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The simulations indicate that SOST engages LRP6 through two coordinated regions with stable interactions.  
- **Evidence pointer** Abstract; location not provided  
- **Concern** The abstract provides no information on simulation length, number of replicates, force field selection, system preparation, equilibration protocol, or convergence criteria. Without these details, the stability of the proposed interactions cannot be evaluated. Molecular dynamics simulations of protein complexes with disordered regions are notoriously sensitive to sampling limitations, and the absence of any convergence assessment is a critical gap.  
- **Why it matters** The central claim of stable, coordinated interactions depends entirely on the adequacy of conformational sampling. If the simulations are too short or under-sampled, the observed contacts may be artifacts of the initial configuration rather than equilibrium properties.  
- **Resolution test** Provide simulation duration, replicate count, RMSD and contact convergence plots, and a demonstration that the key interactions are reproducible across independent simulations.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence strength  
- **Claim pointer** These extended interactions provide a mechanistic explanation for the higher binding affinity observed for full-length SOST compared with truncated variants.  
- **Evidence pointer** Abstract; location not provided  
- **Concern** The abstract claims that the simulation results explain experimentally observed affinity differences, but no quantitative binding free energy calculations, experimental binding data, or direct comparison between full-length and truncated constructs are presented. The causal link between observed contacts and affinity is asserted rather than demonstrated.  
- **Why it matters** The explanatory claim is a key translational element of the study. Without quantitative energetic analysis or experimental correlation, the mechanistic explanation remains speculative.  
- **Resolution test** Include binding free energy calculations (e.g., MM-PBSA or thermodynamic integration) comparing full-length and truncated SOST, or cite and directly compare with published experimental affinity data.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Claim accuracy  
- **Claim pointer** In contrast to prior structural studies, this work reveals an anchor-stabilized, chemically diverse interaction network.  
- **Evidence pointer** Abstract; location not provided  
- **Concern** The abstract states a contrast with prior structural studies but does not specify which studies, what their findings were, or how the present results differ. This claim is unverifiable without specific comparative details. Additionally, the phrase "chemically diverse interaction network" is vague and not operationally defined.  
- **Why it matters** The novelty claim rests on this contrast. If the prior studies already described similar dynamic or multivalent features, the claimed novelty is overstated.  
- **Resolution test** Clearly identify the prior structural studies, summarize their specific findings, and provide a point-by-point comparison with the present results, including structural figures or contact maps.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Experimental validation  
- **Claim pointer** The simulations reveal residue-level interaction behavior that maintains receptor engagement.  
- **Evidence pointer** Abstract; location not provided  
- **Concern** The abstract does not mention any experimental validation, such as mutagenesis of the NAI or HNQS motifs, binding assays, or biophysical characterization. For a study making mechanistic claims about a therapeutic target, the absence of any experimental corroboration weakens the overall case.  
- **Why it matters** Computational predictions of interaction interfaces require experimental testing to establish biological relevance. Without validation, the identified motifs may not be functionally important in vivo.  
- **Resolution test** Include mutagenesis data showing that disruption of the NAI or HNQS motifs reduces binding affinity, or clearly state that experimental validation is planned as future work.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Terminology  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The terms "NAI motif" and "HNQS motif" are used without definition or sequence context. Nonspecialist readers cannot evaluate the significance of these motifs.  
- **Required correction** Provide the full amino acid sequences of these motifs and briefly state their conservation or functional relevance.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Precision  
- **Affected element** Language  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The phrase "anchor-stabilized, chemically diverse interaction network" is imprecise and could describe many protein interfaces. The operational meaning of "anchor" and "chemically diverse" is unclear.  
- **Required correction** Define these terms operationally, for example by specifying the number of persistent contacts, their chemical character, and the criteria for classifying a contact as an anchor.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Methods summary  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The abstract does not state the source or construction of the SOST-LRP6 complex model, including whether the disordered regions were modeled de novo or taken from experimental structures.  
- **Required correction** Briefly describe the model construction approach and the treatment of disordered regions in the methods section of the full manuscript.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Context  
- **Affected element** Literature comparison  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The abstract does not cite or discuss prior computational studies of SOST-LRP6, if any exist, which would help position the novelty of this work.  
- **Required correction** Add a brief statement in the introduction or discussion comparing the present approach and findings with any prior computational investigations.

## Risk / unsupported claims
- The claim that the simulations provide a mechanistic explanation for higher binding affinity of full-length SOST is unsupported without quantitative energetic analysis or direct experimental comparison.
- The claim of contrast with prior structural studies is unverifiable from the abstract alone.
- The assertion of stable, coordinated interactions is unsupported without convergence and sampling evidence.
- The biological relevance of the identified NAI and HNQS motifs is unsubstantiated without experimental validation.
- The overall mechanistic model of anchor-stabilized dynamic remodeling is plausible but currently not established from the provided evidence.