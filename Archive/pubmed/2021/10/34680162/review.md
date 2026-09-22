## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, technical soundness, and clarity of the review article as provided
- **Shared manuscript claim summary** The authors review computational methods for modeling fuzzy complexes, where ordered proteins interact with intrinsically disordered regions, and discuss two case studies (microtubules and RecA filaments) to illustrate how molecular dynamics simulations can bridge experimental ensemble data and individual disordered chain behavior.
- **Visible evidence base** Abstract, Introduction, Sections 2.1-2.5, 3.1-3.2, Conclusions, Acknowledgments
- **Missing materials affecting confidence** Figures referenced (Figures 2 and 3) are not provided; specific simulation parameters and detailed methods for the discussed MD simulations are not included; no supplementary information is available

## Reviewer
- **Overall assessment** This review article addresses a timely and important topic in structural biology, namely the modeling and function of fuzzy complexes where ordered and disordered protein regions interact. The authors provide a useful overview of computational tools, including force field developments, coarse-grained models, enhanced sampling methods, and integrative approaches. The two case studies, on tubulin C-terminal tails and RecA C-terminal tails, are well chosen and reflect the authors' own expertise. However, the manuscript has several weaknesses. The transition from general methodology to specific examples is somewhat abrupt, and the depth of discussion varies considerably between sections. The case studies, while interesting, rely heavily on the authors' own unpublished or preliminary simulation data, which limits the ability to independently assess the claims. The review would benefit from a more critical comparison of available methods and a clearer articulation of open challenges in the field.
- **Who would be interested in the results, and why** Researchers in structural biology, computational biophysics, and molecular dynamics simulation development would find this review useful. Specifically, those studying intrinsically disordered proteins, protein-protein interactions, and cytoskeletal systems (microtubules) or DNA repair mechanisms (homologous recombination) would benefit from the methodological overview and the specific examples. The review could also serve as an entry point for experimentalists seeking to understand how computational approaches can complement their work on disordered systems.
- **Major strengths** The topic is highly relevant and timely, given the growing recognition of the functional importance of intrinsic disorder. The authors provide a broad and reasonably current overview of computational methods, including recent force field developments and enhanced sampling techniques. The choice of two specific case studies from the authors' own work adds a personal and practical perspective that is often missing in general reviews. The discussion of frustration as a concept in fuzzy complexes is thought-provoking and could stimulate new research directions.
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
  - R1-m5
- **Technical failings that need to be addressed before the case is established** The review's central claim that MD simulations can bridge experimental ensemble data and individual disordered chain behavior is not fully substantiated. The case studies rely on preliminary or unpublished simulation data, and the methodological details are insufficient for readers to evaluate the robustness of the findings. The lack of figures and specific simulation parameters further weakens the evidence base.
- **Assessment against Nature-style criteria** Originality: The review covers a niche but growing area, and the focus on fuzzy complexes specifically is relatively novel. However, much of the methodological content has been reviewed elsewhere, and the original contribution is mainly in the case studies. Scientific importance: The topic is important for understanding protein function, but the review does not fully establish the broader significance of fuzzy complexes beyond the two examples. Interdisciplinary readership: The review is likely to appeal to a specialized audience of computational and structural biologists, but may be less accessible to a broader readership due to the technical depth. Technical soundness: The methodological descriptions are generally accurate, but the reliance on unpublished data in the case studies is a concern. Readability for nonspecialists: The writing is clear but assumes familiarity with molecular dynamics and structural biology concepts, which may limit accessibility.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the presentation of the case study data and the clarity of the methodological comparisons.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that their MD simulations of RecA filaments show that the C-terminal tail can penetrate the filament interior and reach the secondary DNA binding site under conditions of ATP hydrolysis and 5 mM magnesium.
- **Evidence pointer** Section 3.2, Figure 3 (not provided)
- **Concern** The claim that the RecA C-terminal tail can penetrate the filament interior is based on two 100-ns MD simulations, which the authors themselves describe as "preliminary." The simulations start from a modified model with an ADP interface at the central monomer, but the details of this modification and its biological relevance are not fully explained. The authors also note that force fields for magnesium interactions need to be tested, which undermines confidence in the results. Without additional replicates, convergence analysis, or experimental validation, this claim is not sufficiently supported.
- **Why it matters** This is a key finding of the review, as it proposes a mechanism for how the RecA tail regulates homologous recombination. If the evidence is not robust, the central thesis of the case study is weakened.
- **Resolution test** The authors should provide additional simulation replicates, demonstrate convergence of the observed tail penetration, and discuss the sensitivity of the results to force field parameters and the initial model construction. Ideally, they should also compare with experimental data or provide testable predictions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scope and depth
- **Claim pointer** The review claims to present "a review of the computational methods developed to provide us with information on such fuzzy interfaces, and how they integrate experimental information."
- **Evidence pointer** Section 2
- **Concern** The methodological overview in Section 2 is uneven. While force field developments and enhanced sampling methods are discussed, other important approaches such as Markov state models, metadynamics variants beyond basic descriptions, and machine learning potentials are only briefly mentioned or omitted. The section on integrating experimental data is relatively short and does not critically compare the strengths and limitations of different integrative approaches. The review would benefit from a more systematic and critical treatment of the available methods.
- **Why it matters** A review article should provide a comprehensive and balanced overview of the field. The current treatment may mislead readers about the relative maturity and applicability of different methods.
- **Resolution test** The authors should expand the methodological sections to include a more complete coverage of available techniques, with a critical assessment of their advantages and limitations. They should also clarify the criteria used to select the methods discussed.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Conceptual clarity
- **Claim pointer** The authors propose that "long range frustration" is a concept that extends to the interaction between disordered tails and protein cores, and that it may facilitate tail unbinding.
- **Evidence pointer** Section 3.1
- **Concern** The concept of "long range frustration" is introduced but not rigorously defined. The authors draw an analogy to frustration in folded proteins, but it is unclear how this concept applies to the long-range electrostatic interactions described. The discussion would benefit from a more precise definition and a clearer explanation of how this concept differs from or extends existing ideas about frustration in disordered systems.
- **Why it matters** This is a potentially novel conceptual contribution, but as presented, it is vague and may be difficult for readers to apply or test.
- **Resolution test** The authors should provide a formal definition of long range frustration, discuss its relationship to existing concepts, and outline how it could be quantified or tested in simulations or experiments.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The authors describe MD simulations of tubulin and RecA systems, including specific simulation lengths and conditions.
- **Evidence pointer** Sections 3.1 and 3.2
- **Concern** The manuscript lacks sufficient methodological detail for the simulations described. For example, the force fields used, the system setup, the equilibration protocol, and the analysis methods are not specified. This makes it impossible for readers to reproduce or independently evaluate the simulations.
- **Why it matters** Reproducibility is a core principle of scientific research. Without adequate methodological details, the simulation results cannot be verified or built upon by others.
- **Resolution test** The authors should provide a detailed description of the simulation protocols, including software, force field versions, water models, ion concentrations, and analysis tools, either in the main text or as supplementary material.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract is dense and could benefit from a clearer statement of the review's scope and main conclusions.
- **Required correction** Consider restructuring the abstract to explicitly state the two main aims: (1) reviewing computational methods and (2) presenting two case studies, and summarize the key take-home messages.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2.4
- **Evidence pointer** Section 2.4
- **Issue** The discussion of the Protein Ensemble Database (PED) and FuzDB is brief and does not explain how these resources can be used in practice.
- **Required correction** Provide a few examples of how these databases can be queried or used to support modeling efforts.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Accuracy
- **Affected element** Section 3.1
- **Evidence pointer** Section 3.1
- **Issue** The statement that "the ability of the disordered protein tails to bind the protein core surface but also to unbind from it is key to their function" is somewhat tautological and could be made more specific.
- **Required correction** Clarify what specific functional outcomes depend on this binding/unbinding ability, with reference to the tubulin or RecA examples.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section 3.2
- **Evidence pointer** Section 3.2
- **Issue** The discussion of the RecA tail's role in strand exchange is complex and could be difficult for non-specialists to follow.
- **Required correction** Consider adding a schematic figure or a step-by-step description of the proposed mechanism to aid comprehension.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Conclusions
- **Evidence pointer** Section 4
- **Issue** The conclusions are brief and do not fully synthesize the main points of the review or discuss future directions in a concrete way.
- **Required correction** Expand the conclusions to summarize the key methodological advances, the main findings from the case studies, and the most pressing open questions in the field.

## Risk / unsupported claims
- The claim that the RecA C-terminal tail can penetrate the filament interior and reach the secondary DNA binding site is based on preliminary simulations and is not fully supported by the evidence provided.
- The concept of "long range frustration" is introduced without a rigorous definition or supporting evidence.
- The statement that "high level of disorder in fuzzy interfaces are not necessarily associated to low affinity" is supported by a single example (histone H1 and prothymosin-α) and may not be generalizable.
- The claim that MD simulations can bridge the gap between experimental ensemble properties and individual chain behavior is asserted but not systematically demonstrated across the examples discussed.