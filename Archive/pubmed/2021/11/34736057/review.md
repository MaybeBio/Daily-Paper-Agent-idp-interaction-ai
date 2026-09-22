## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract, with no access to the full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors propose that combining classical molecular dynamics (MD) and ab initio quantum mechanics (QM) at the molecular orbital scale provides improved models for understanding protein misfolding and amyloid aggregation in neurodegenerative diseases, using prion as a case study. They report MD-based binding free energy analyses of misfolded versus native prion complexes, QM-based binding free energy calculations of a hydrophobic binding site, and QM-based docking to propose a mechanism for nanofibril assembly and elongation.
- **Visible evidence base** Abstract text only; no quantitative results, methodological details, or experimental comparisons are provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, computational methods and parameters, force field and basis set specifications, error estimates, experimental validation data, and any statistical analyses

## Reviewer
- **Overall assessment** The abstract presents an ambitious methodological framework that integrates classical MD and ab initio QM to study protein misfolding and amyloid aggregation. The conceptual motivation is timely and the prion case study is relevant. However, the abstract lacks quantitative results, methodological specificity, and validation against experimental data. The claims of improved accuracy and the proposed aggregation mechanism cannot be assessed from the supplied material. The work may have merit, but the evidence base is insufficient to establish the central conclusions.
- **Who would be interested in the results, and why** Computational biophysicists and chemists working on protein misfolding and aggregation, researchers in neurodegenerative disease modeling, and developers of multiscale simulation methods. The potential integration of MD and QM for binding free energy and docking could interest those seeking more accurate descriptions of protein-protein interactions in aggregation contexts.
- **Major strengths** The abstract addresses a significant problem, namely the limitations of classical MD for capturing electronic effects in protein misfolding. The proposal to use frontier molecular orbitals for docking is conceptually novel. The focus on a specific disease-relevant system, prion, provides a concrete application. The generalization to other misfolding diseases is a reasonable extension.
- **Major Concerns** The abstract provides no numerical results, no methodological details, and no comparison with experimental data. The claim that QM achieves "much better accuracy" than MD is unsupported without error analysis or benchmarks. The proposed aggregation mechanism is described qualitatively without structural or energetic evidence. The relationship between the MD and QM components is not clearly articulated.
- **Minor Comments** The abstract uses terms such as "outdated hypotheses" without specifying which hypotheses are outdated. The phrase "not experimentally achievable" regarding molecular orbitals is imprecise, as experimental orbital imaging exists in limited contexts. The abstract would benefit from stating the system size, simulation timescales, and QM level of theory.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: The integration of QM-based docking with MD for misfolded protein complexes is potentially original, but the abstract does not demonstrate novelty beyond prior multiscale approaches. Scientific importance: The topic is important for neurodegenerative disease research, but the abstract does not establish a new biological or mechanistic insight. Interdisciplinary readership: The abstract is accessible to a broad biophysical audience, but lacks technical depth for specialists. Technical soundness: Cannot be evaluated from the abstract alone; no methods or error analysis are provided. Readability for nonspecialists: The abstract is generally readable, though some terms such as "frontier MOs" and "beta-sheets oligomers" may require background knowledge.
- **Recommendation posture** Currently not established from the provided evidence. The abstract suggests a potentially valuable approach, but the absence of quantitative results and methodological detail prevents any assessment of validity or impact. A full manuscript with data would be required to evaluate the claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that QM computes the binding free energy of the hydrophobic binding site "with a much better accuracy than that of MD."
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract provides no quantitative comparison between MD and QM binding free energy values, no reference to experimental measurements, and no error estimates or convergence criteria. The claim of superior accuracy is therefore unsupported.
- **Why it matters** The central methodological advantage of the proposed approach rests on this accuracy claim. Without benchmarks or error analysis, readers cannot judge whether the QM results are reliable or whether the MD results were inadequate.
- **Resolution test** Provide a table or figure comparing MD and QM binding free energies for the same system, with experimental values or high-level reference calculations, including statistical uncertainties and convergence checks.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "successive aggregation of multiple monomers leads to an amyloid-like nanofibril that grows along a principal elongation direction, as also observed experimentally."
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract states that the proposed mechanism matches experimental observation, but no experimental data, references, or structural comparisons are provided. The mechanism is described only qualitatively, with no coordinates, free energy profiles, or kinetic data.
- **Why it matters** The aggregation mechanism is a core outcome of the study. Without structural or energetic evidence, the claim that the model reproduces experimental fibril growth cannot be verified.
- **Resolution test** Show computed fibril structures with growth direction, compare with experimental fibril morphologies or cryo-EM structures, and provide free energy or kinetic data supporting the elongation pathway.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The abstract describes MD simulations of misfolded and native prion complexes and QM calculations of binding free energy and docking.
- **Evidence pointer** Abstract, location not provided
- **Concern** No methodological details are given, including force field, water model, simulation length, QM level of theory, basis set, solvation model, or docking algorithm. The system size and the specific residues involved in the hydrophobic binding site are not identified.
- **Why it matters** Reproducibility is a fundamental requirement for computational studies. Without these details, the results cannot be replicated or independently verified.
- **Resolution test** Include a methods section with all simulation and QM parameters, software versions, and input file availability, or provide these in supplementary materials.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Introduction
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "outdated hypotheses on protein folding must be revised" is vague and does not specify which hypotheses are considered outdated or how the proposed models revise them.
- **Required correction** Identify the specific hypotheses being challenged and briefly state how the proposed models address their limitations.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Precision
- **Affected element** Methods description
- **Evidence pointer** Abstract, location not provided
- **Issue** The statement that molecular orbitals are "not experimentally achievable" is imprecise, as techniques such as scanning tunneling microscopy and photoemission tomography can probe orbital densities in certain systems.
- **Required correction** Rephrase to indicate that molecular orbitals are not directly accessible in the context of solvated proteins or at the required resolution, rather than making a general claim.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results summary
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract mentions "a conversion of residues to toxic beta-sheets" in the optimized misfolded complex, but does not specify which residues, how the conversion was detected, or its structural consequences.
- **Required correction** Provide residue-level details and the method used to identify beta-sheet conversion, or refer to a specific figure in the full manuscript.

## Risk / unsupported claims
- The claim that QM provides "much better accuracy" than MD for binding free energy is unsupported without comparative data or benchmarks.
- The claim that the proposed aggregation mechanism matches experimental observation is unsupported without experimental references or structural comparisons.
- The claim that the models "can be generalized to other misfolding diseases" is plausible but not demonstrated with any additional examples.
- The statement that the observed beta-sheet conversion occurs in the optimized misfolded complex is unverifiable without residue-level data.
- The overall assertion that the models "improve our understanding" of protein-protein interactions leading to misfolding is not substantiated by any quantitative results in the abstract.