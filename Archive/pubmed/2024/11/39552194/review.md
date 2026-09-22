## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors use molecular dynamics simulations and a deep neural network to explain why two alpha-synuclein fibril polymorphs, "rod" and "twister", differ in stability and in their response to the E46K charge-swapping mutation. They attribute the differential stability to distinct quaternary arrangements of peptide monomers, which alter inter-residue interaction networks, dynamic correlations, sidechain mobilities, and principal modes of internal motion. The DNN identifies residue pairs whose spatial proximity distinguishes the two polymorphs, revealing a "feedback loop" from quaternary structure to sequence-level key residues, with implications for designing fibril-breaking molecules.
- **Visible evidence base** Abstract text only; no methodological details, simulation parameters, convergence criteria, DNN architecture, training/validation procedures, or quantitative results are provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, simulation protocols, force field parameters, system preparation details, DNN feature selection and performance metrics, statistical analyses, and any comparison with experimental data

## Reviewer
- **Overall assessment** The abstract presents an interesting and potentially valuable hypothesis about the molecular basis of polymorph-specific stability in alpha-synuclein fibrils, linking quaternary structure to sequence-level functional roles via simulation and machine learning. However, the abstract alone provides insufficient evidence to evaluate the technical soundness of the simulations, the validity of the DNN analysis, or the robustness of the conclusions. The central claims are plausible but currently not established from the supplied material.
- **Who would be interested in the results, and why** Researchers studying protein misfolding and aggregation, particularly those focused on alpha-synuclein and Parkinson's disease, would be interested in the mechanistic insight into polymorph-specific stability and mutation effects. Computational biophysicists and machine learning practitioners applying deep learning to biomolecular simulations would also find the methodological combination relevant. The potential for identifying key residues for therapeutic targeting could attract drug discovery groups.
- **Major strengths** The study addresses a clinically relevant question, namely why a pathogenic mutation has differential effects across fibril polymorphs. The combination of molecular dynamics and deep learning is a modern and potentially powerful approach. The proposed concept of a "feedback loop" from quaternary structure to sequence-level residue importance is conceptually novel and could have broader implications for sequence-structure relationships.
- **Major Concerns** The abstract lacks quantitative evidence for any of the central claims. No simulation details, no measures of statistical uncertainty, no validation of the DNN, and no direct comparison of predicted key residues with experimental data are provided. The causal link between the identified residue pairs and differential stability is asserted but not demonstrated.
- **Minor Comments** The abstract uses terms such as "apparently stable structures" and "intrinsically assigns key roles" that are vague and could be more precise. The phrase "feedback loop from quaternary structure to sequence level" is evocative but not clearly defined. The final statement about benefiting "planned design of fibril breaking molecules" is speculative and not supported by the presented evidence.
- **Technical failings that need to be addressed before the case is established** The absence of any quantitative results, simulation convergence criteria, DNN performance metrics, or statistical validation means that the core claims cannot be assessed. The abstract does not report how the DNN was trained, tested, or whether the identified features are robust across independent simulations.
- **Assessment against Nature-style criteria** Originality: the concept of using DNN to extract polymorph-distinguishing residue pairs is original, though the underlying simulation approach is standard. Scientific importance: the question of polymorph-specific mutation effects is important for understanding Parkinson's disease pathology, but the abstract does not establish the significance of the findings beyond a plausible hypothesis. Interdisciplinary readership: the work bridges biophysics and machine learning, which could appeal to a broad audience, but the abstract is too technical and lacks context for nonspecialists. Technical soundness: not assessable from the abstract alone; no evidence of convergence, sampling adequacy, or DNN validation is provided. Readability for nonspecialists: the abstract is dense and uses jargon without sufficient explanation, making it difficult for a general scientific audience to follow.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a promising framework, but the lack of quantitative support and methodological detail prevents any assessment of validity. A revised version with concrete results and validation would be needed to consider the claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that molecular dynamics-based conformational sampling reveals the molecular basis of differential stabilities of the two polymorphs.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract provides no information on simulation length, force field, temperature, pressure, system size, number of replicas, or convergence criteria. Without these details, it is impossible to judge whether the conformational sampling was adequate to support conclusions about stability differences.
- **Why it matters** Molecular dynamics results are only meaningful if the simulations are converged and statistically robust. If the sampling is insufficient, the observed differences between polymorphs could be artifacts of inadequate exploration of conformational space.
- **Resolution test** Provide simulation protocols, convergence metrics (e.g., root-mean-square deviation over time, block averaging), and replicate analyses demonstrating that the observed differences are reproducible and not dependent on initial conditions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that a Deep Neural Network-based analysis extracted residue pairs and their spatial proximities as features to distinguish the states of the two polymorphs.
- **Evidence pointer** Abstract only; location not provided
- **Concern** No details are given about the DNN architecture, input features, training data, validation procedure, or performance metrics. It is unclear how the network was trained, whether it was tested on independent data, and how the identified residue pairs were selected as important.
- **Why it matters** Without proper validation, the DNN may be overfitting or identifying spurious correlations. The claim that specific residue pairs are key features depends entirely on the reliability of the machine learning analysis.
- **Resolution test** Describe the DNN architecture, training/validation split, feature importance method, and report accuracy, precision, recall, or other relevant metrics. Show that the identified residue pairs are stable across multiple training runs and independent simulation data.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors claim that differences in molecular arrangements assign key roles to different sets of residues in the two polymorphs, and that this is a "feedback loop from quaternary structure to sequence level".
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract asserts a causal relationship between quaternary arrangement and residue-level importance, but no quantitative data are presented to support this. The concept of a "feedback loop" is not defined or demonstrated.
- **Why it matters** This is the central conceptual claim of the work. If it is not supported by clear evidence, the entire premise of the study is weakened. The claim goes beyond simple correlation and implies a mechanistic link that requires direct demonstration.
- **Resolution test** Provide quantitative evidence, such as comparative interaction energy analyses, per-residue stability metrics, or mutation effect predictions, that directly link the quaternary arrangement to the differential importance of specific residues. Define and illustrate the "feedback loop" with concrete data.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors claim that the E46K mutation has a differential impact on the two polymorphs and that the molecular reason has been probed.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract mentions the E46K mutation but provides no results on how the mutation affects stability, dynamics, or interaction networks in each polymorph. No comparison of mutant versus wild-type systems is described.
- **Why it matters** The differential impact of E46K is a key motivation for the study. Without any data on the mutation's effects, the claim that the molecular basis has been probed is unsupported.
- **Resolution test** Present comparative simulation results for wild-type and mutant systems in both polymorphs, including changes in free energy, interaction energies, or structural metrics, with appropriate statistical analysis.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "apparently stable structures" is ambiguous. It is unclear whether the authors mean experimentally observed stability, computationally predicted stability, or something else.
- **Required correction** Clarify the basis for calling the structures "apparently stable" and specify the operational definition of stability used in the study.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract structure
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract is dense and mixes multiple concepts (polymorph stability, mutation effects, DNN features, dynamic correlations, sidechain mobilities, principal modes) without a clear logical flow. Nonspecialists may struggle to follow the main argument.
- **Required correction** Restructure the abstract to present the hypothesis, methods, key results, and implications in a more sequential and accessible manner, with brief explanations of technical terms.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Speculation
- **Affected element** Implication statement
- **Evidence pointer** Abstract; location not provided
- **Issue** The final statement that identification of key residues "is likely to benefit the planned design of fibril breaking molecules" is speculative and not directly supported by the presented findings.
- **Required correction** Either provide a concrete example of how the identified residues could be targeted or soften the claim to indicate a potential future application rather than a direct benefit.

## Risk / unsupported claims
- The claim that the DNN has "revealed" a feedback loop from quaternary structure to sequence level is unsupported because no DNN results or validation are presented.
- The claim that the molecular basis of differential stabilities has been probed is unsupported because no quantitative stability data are provided.
- The claim that the E46K mutation has a differential impact on the two polymorphs is unsupported because no mutant simulation results are described.
- The claim that differences in dynamic correlation, sidechain mobility, and principal modes contribute to stability differences is unsupported because no data on these analyses are presented.
- The claim that the findings will benefit the design of fibril-breaking molecules is speculative and not evidence-based.