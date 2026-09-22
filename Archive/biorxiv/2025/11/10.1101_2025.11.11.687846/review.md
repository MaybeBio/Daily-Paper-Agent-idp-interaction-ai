## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors propose a computational pipeline combining a protein-folding algorithm with Monte Carlo optimization to design peptide binders targeting intrinsically disordered epitopes. They claim binding free energies on the order of tens of kBT (comparable to covalent interactions) for multiple targets, and that molecular simulations show induced folding of the epitope upon binding. They suggest this approach extends druggable space to disordered regions.
- **Visible evidence base** Abstract text only; no quantitative data, simulation details, or target descriptions are provided
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, simulation parameters, free energy calculation details, target protein identities, peptide sequences, and any statistical or error analysis

## Reviewer
- **Overall assessment** The abstract presents an intriguing concept with potentially high impact, but the evidence base is entirely insufficient to evaluate the central claims. The reported binding free energies are extraordinary and would require rigorous validation. The claim that a protein-folding algorithm has "learned" induced folding principles is speculative and not supported by the provided material. The significance statement is clear and well-framed, but the technical foundation cannot be assessed from the abstract alone.
- **Who would be interested in the results, and why** Computational biophysicists and drug designers interested in targeting disordered proteins; researchers working on peptide design, protein-protein interactions, and induced folding mechanisms. The potential to expand druggable space to intrinsically disordered regions would attract broad interest in structural biology and medicinal chemistry communities.
- **Major strengths** The conceptual advance is clear and potentially significant. The idea of using protein-folding confidence metrics within an optimization pipeline to design peptides that induce folding is novel. The significance statement is well-written and effectively communicates the potential impact. The claim of extending druggability to disordered regions addresses a well-known limitation in current drug design.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1 (binding free energy magnitude), R1-M2 (induced folding claim), R1-M3 (generality claim)
- **Assessment against Nature-style criteria** 
  - Originality: High. The concept of using protein-folding algorithms to design binders for disordered epitopes is novel and not a straightforward extension of existing methods.
  - Scientific importance: Potentially high if the claims are substantiated, as it would address a major gap in druggable space. However, the extraordinary nature of the claims requires exceptional evidence.
  - Interdisciplinary readership: The topic bridges computational biology, biophysics, and drug design, which would appeal to a broad audience. The abstract is written accessibly.
  - Technical soundness: Cannot be assessed from the abstract. The methods are not described in sufficient detail, and no quantitative evidence is presented.
  - Readability for nonspecialists: The abstract is well-written and the significance statement is particularly clear. Technical terms are used appropriately without excessive jargon.
- **Recommendation posture** Currently not established from the provided evidence. The concept is promising and worthy of consideration, but the abstract alone does not provide sufficient evidence to support the extraordinary claims. A full manuscript with detailed methods and rigorous validation would be required for a supportive recommendation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality and interpretation
- **Claim pointer** "we show by accurate free energy calculations that our approach is able to design peptides with binding free energies on the order of tens of kBT, i.e., with strengths comparable to covalent interactions"
- **Evidence pointer** Location not provided
- **Concern** The claim of binding free energies on the order of tens of kBT (approximately 10 to 100 kBT, or roughly 6 to 60 kcal/mol) is extraordinary. For comparison, typical non-covalent protein-ligand binding free energies are on the order of 5 to 15 kBT. Values approaching covalent bond strengths (approximately 50 to 100 kcal/mol) would represent an unprecedented regime for non-covalent peptide-protein interactions. The abstract provides no details on the free energy calculation method, the error estimates, or the specific values obtained.
- **Why it matters** If the binding free energies are indeed this large, it would represent a fundamental advance in peptide design. However, such claims require exceptional evidence, including convergence checks, multiple independent methods, and comparison with experimental validation. Without these details, the claim is not credible.
- **Resolution test** Provide the specific free energy values for each target, the method used (e.g., umbrella sampling, metadynamics, FEP), convergence criteria, and error bars. Ideally, include experimental validation or at least a clear discussion of why such large binding affinities are physically plausible.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of simulation results
- **Claim pointer** "Direct observation of the bound complex through molecular simulations shows that the targeted epitope folds into structured domains with lowered thermal fluctuations upon binding, while remaining unstructured and dynamic in the unbound state, suggesting that the protein-folding algorithm must have learned the principles of induced (co-)folding"
- **Evidence pointer** Location not provided
- **Concern** The claim that the protein-folding algorithm "must have learned the principles of induced (co-)folding" is a strong interpretive leap. The observation that the epitope folds upon binding in simulations could arise from the optimization process itself, which selects for sequences that stabilize a folded conformation. This does not necessarily imply that the algorithm has learned general principles of induced folding. The abstract provides no details on the simulation protocol, the order parameters used to assess folding, or the comparison with appropriate controls.
- **Why it matters** The mechanistic interpretation is central to the novelty of the approach. If the algorithm merely optimizes for a pre-defined folded state, the claim of "learning" is overstated. The distinction between optimization and learning has implications for the generality and transferability of the method.
- **Resolution test** Provide detailed simulation data showing the folding transition, including free energy profiles along relevant reaction coordinates. Include control simulations with random or scrambled peptide sequences to demonstrate that the observed folding is specific to the designed peptides. Discuss whether the algorithm's confidence metrics correlate with experimentally known induced folding cases.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Generality and scope of claims
- **Claim pointer** "For different protein targets, we show by accurate free energy calculations that our approach is able to design peptides with binding free energies on the order of tens of kBT" and "Given the ubiquitous presence of unstructured regions in proteins, our results suggest a potential pathway to design drugs targeting a large variety of previously untargetable epitopes"
- **Evidence pointer** Location not provided
- **Concern** The abstract claims success for "different protein targets" but provides no information on the number of targets, their identity, the diversity of their disordered regions, or the success rate. The generalization to "a large variety of previously untargetable epitopes" is a significant extrapolation from an unspecified number of test cases. The abstract does not discuss potential failure modes or limitations of the approach.
- **Why it matters** The broad claim of general applicability is a key part of the significance statement. Without knowing the number and diversity of test cases, and the success rate, the reader cannot assess whether the approach is truly general or only works for a narrow set of favorable cases.
- **Resolution test** Specify the number of targets tested, their protein identities, the length and sequence composition of the disordered regions, and the success rate. Discuss any cases where the approach failed and the reasons for failure. Provide a clear statement of the scope and limitations of the method.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** "protein-folding algorithm"
- **Evidence pointer** Abstract, first sentence
- **Issue** The abstract does not specify which protein-folding algorithm is used. Given the rapid evolution of this field, the specific algorithm (e.g., AlphaFold, ESMFold, RoseTTAFold) is critical for reproducibility and for assessing the novelty of the approach.
- **Required correction** Name the specific protein-folding algorithm and version used, and briefly justify its selection.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Quantitative detail
- **Affected element** "binding free energies on the order of tens of kBT"
- **Evidence pointer** Abstract, results section
- **Issue** The phrase "tens of kBT" is imprecise. A range of 10 to 90 kBT spans an enormous range of binding affinities, from moderate to essentially irreversible. The abstract should provide a more specific range or representative values.
- **Required correction** Provide the range of binding free energies observed, or representative values for each target, with units clearly stated.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Experimental validation
- **Affected element** "we show by accurate free energy calculations"
- **Evidence pointer** Abstract, results section
- **Issue** The abstract relies entirely on computational predictions. No mention is made of experimental validation, which would be expected for a claim of this magnitude. Even a single experimental confirmation would substantially strengthen the case.
- **Required correction** State whether any experimental validation was performed, and if not, explicitly acknowledge this as a limitation and discuss the computational evidence that supports the reliability of the predictions.

## Risk / unsupported claims
- The claim of binding free energies comparable to covalent interactions is unsupported by any quantitative data in the abstract.
- The claim that the protein-folding algorithm "must have learned the principles of induced (co-)folding" is an unsupported interpretive leap.
- The claim of general applicability to "a large variety of previously untargetable epitopes" is unsupported given the unspecified number and diversity of test cases.
- The overall efficacy of the approach cannot be assessed without details on the Monte Carlo optimization pipeline, the confidence metrics used, and the simulation protocols.
- No information is provided on the computational cost or scalability of the method, which would be relevant for practical drug design applications.