## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific and technical soundness of the DIPEND pipeline, its validation, and the claims made about its utility for ensemble generation of disordered protein segments
- **Shared manuscript claim summary** The authors present DIPEND, an open-source Python-based pipeline that generates conformational ensembles of disordered protein segments by sampling neighbor-dependent Ramachandran distributions, with optional user-defined biasing. They demonstrate its use on Cd3ϵ and a single α-helical (SAH) region of myosin VI, selecting subensembles against experimental NMR data via CoNSEnsX+.
- **Visible evidence base** Full text including Methods, Results, two tables (referenced), three figures (referenced), and discussion. No supplementary material was provided.
- **Missing materials affecting confidence** Supplementary figures/tables, actual parameter files, code repository contents, detailed CoNSEnsX+ selection parameters, and the full set of experimental data used for validation were not available for review.

## Reviewer
- **Overall assessment** The manuscript describes a useful and timely open-source tool for generating conformational pools of disordered protein segments. The pipeline is modular, uses well-established components, and addresses a real need in the field. However, the validation is limited in scope and depth, and several technical details are insufficiently described to fully assess reproducibility and performance. The claims about enhanced sampling efficiency and the utility of the biasing approach are plausible but not rigorously demonstrated. The comparison with MD-derived ensembles is interesting but under-analyzed. Overall, the work is a solid contribution to the methodological toolbox, but the evidence presented does not fully establish the superiority or general utility of the approach over existing methods.
- **Who would be interested in the results, and why** Researchers working on intrinsically disordered proteins, ensemble-based modeling, and integrative structural biology. The open-source nature and modular design will appeal to method developers and users seeking customizable tools for generating initial conformer pools for selection-based ensemble refinement.
- **Major strengths** 1. Addresses a clear need for open-source, maintainable tools for generating conformational pools of disordered segments. 2. Uses well-established, publicly available components (ChimeraX, Scwrl4, GROMACS, Dunbrack distributions). 3. Provides a flexible biasing mechanism to incorporate prior knowledge. 4. Demonstrates application on two biologically relevant systems with different structural propensities. 5. The separation of generation from selection is a sensible design choice.
- **Major Concerns** 1. Validation is limited to two systems and lacks quantitative benchmarks against existing methods. 2. The biasing approach is described but its effect on ensemble quality is not systematically evaluated. 3. The comparison with MD is under-analyzed and potentially misleading. 4. Computational cost and scalability are only briefly mentioned. 5. The manuscript does not provide sufficient detail on parameter choices and their impact on results.
- **Minor Comments** 1. The abstract mentions "efficient and exhaustive" sampling but this is not quantified. 2. The description of the unknotting step is vague. 3. The choice of RMSD as a selection metric is not justified. 4. The manuscript would benefit from a more detailed discussion of limitations and potential failure modes.
- **Technical failings that need to be addressed before the case is established** The lack of quantitative comparison with existing methods (e.g., Flexible Meccano, TraDes) and the absence of a systematic evaluation of the biasing parameters undermine the claim that DIPEND enhances sampling efficiency. The MD comparison is not adequately controlled (e.g., different force fields, sampling protocols) to draw meaningful conclusions.
- **Assessment against Nature-style criteria** Originality: Moderate. The pipeline combines existing tools in a new way, but the underlying concept (neighbor-dependent sampling) is not novel. Scientific importance: Moderate. Useful for a niche community but not likely to shift paradigms. Interdisciplinary readership: Limited. Primarily of interest to structural biologists and computational chemists. Technical soundness: Adequate but with gaps in validation and reproducibility. Readability for nonspecialists: Good. The manuscript is clearly written and accessible.
- **Recommendation posture** Supportive if technical concerns are resolved. The pipeline is a valuable contribution, but the validation needs to be strengthened and the claims more carefully qualified.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation
- **Claim pointer** The authors claim that DIPEND provides "efficient and exhaustive" sampling and that the biasing approach allows "consideration of a priori known conformational preferences."
- **Evidence pointer** Section 3.4, Section 3.5, Table 1, Table 2
- **Concern** The validation is limited to two systems and does not include a quantitative comparison with existing ensemble generation methods (e.g., Flexible Meccano, TraDes, or unbiased MD). The claim of enhanced sampling efficiency is not supported by any metric (e.g., convergence time, diversity of sampled conformations, or coverage of relevant conformational space). The biasing approach is demonstrated on the SAH region, but the effect of different weights, standard deviations, or the choice of biased residues on the final ensemble quality is not systematically explored.
- **Why it matters** Without a benchmark against existing methods, it is unclear whether DIPEND offers any advantage over current approaches. The biasing mechanism is a key feature, but its utility is not rigorously demonstrated. This limits the generalizability of the claims and the practical guidance for users.
- **Resolution test** Provide a quantitative comparison of DIPEND-generated pools with those from at least one established method (e.g., Flexible Meccano) on the same systems, using metrics such as conformational diversity, coverage of Ramachandran space, and agreement with experimental data after selection. Additionally, perform a sensitivity analysis of the biasing parameters (weight, standard deviation) on the SAH system and report how these affect the selected ensemble's agreement with experimental data.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The manuscript states that DIPEND is "open-source and extendable" and provides a detailed description of the pipeline steps.
- **Evidence pointer** Section 2.1, Section 3.1
- **Concern** The description of the pipeline is insufficient for reproduction. Key parameters are not specified: the exact ChimeraX commands for structure building and dihedral angle setting, the Scwrl4 options, the GROMACS energy minimization settings (e.g., integrator, number of steps, convergence criteria), and the criteria for the CA-CA clash check. The "unknotting" step is described only heuristically, and the algorithm for choosing which residues to adjust is not detailed. The code repository is mentioned but not accessible for review.
- **Why it matters** Reproducibility is a core requirement for a methodological contribution. Without precise parameter specifications, users cannot reliably apply the pipeline to their own systems, and the results cannot be independently verified.
- **Resolution test** Provide a complete list of all parameters and commands used for each step, either in the main text or as supplementary material. Include a link to the code repository and ensure it contains example input/output files and a README with detailed usage instructions. Ideally, provide a test case with expected outputs to allow users to verify their installation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of results
- **Claim pointer** The authors state that for Cd3ϵ, the DIPEND-generated ensemble shows "relatively low RMSD values" and that the selected subensemble from MD "exhibits considerably worse correspondence to experimental data."
- **Evidence pointer** Section 3.4, Figure 2
- **Concern** The comparison between DIPEND and MD is not adequately controlled. The MD simulation was performed with a specific force field (Amber ff99SB) and a single 1 μs trajectory, which may not be representative of the conformational sampling achievable with other MD protocols or force fields. The authors do not discuss whether the MD simulation was converged or whether the observed compact state is an artifact of the force field or sampling length. The PCA analysis (Figure 2) is mentioned but not described in detail, and the criteria for "even sampling" are not defined.
- **Why it matters** The claim that DIPEND provides better sampling than MD is a strong statement that could mislead users. If the MD simulation is not converged or uses a biased force field, the comparison is unfair and the conclusion is not generalizable.
- **Resolution test** Acknowledge the limitations of the MD comparison and either (a) provide evidence of MD convergence (e.g., block averaging, multiple independent trajectories) or (b) soften the claim to state that DIPEND provides a complementary approach to MD. Additionally, provide a more detailed description of the PCA analysis and the criteria used to assess sampling uniformity.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the pipeline generates "initial protein structure pools for use with selection-based tools," but the term "initial" is ambiguous. It could be interpreted as a limitation (i.e., the pools are not directly usable) or as a design choice.
- **Required correction** Clarify that the pools are intended as input for downstream selection/refinement methods and are not meant to be final structural models.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Section 2.1.2
- **Evidence pointer** Equation (1)
- **Issue** The equation for the triplet probability is not fully explained. The terms p_l_all and p_r_all are not defined clearly, and the normalization step is described only briefly.
- **Required correction** Provide a clear definition of all terms in the equation and explain the normalization procedure in more detail.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Section 3.3
- **Evidence pointer** Section 3.3
- **Issue** The statement that "selection based on one atom type typically does not result in considerable improvement in other shift types" is interesting but not elaborated. It would be helpful to discuss the implications of this observation for practical use.
- **Required correction** Add a brief discussion of why this might be the case and whether this is a limitation of the selection method or a property of the systems studied.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 3.5
- **Evidence pointer** Section 3.5
- **Issue** The manuscript mentions that the SAH region was modeled with a biased distribution, but the specific choice of residues and the rationale for the chosen weights are not fully explained.
- **Required correction** Provide a more detailed description of how the biased distribution was set up for the SAH region, including the choice of residues and the justification for the weight values.

## Risk / unsupported claims
- The claim that DIPEND provides "efficient and exhaustive" sampling is not supported by quantitative evidence.
- The claim that DIPEND-generated pools are superior to MD-derived pools is based on a single, potentially non-converged simulation and is not generalizable.
- The utility of the biasing mechanism is demonstrated but not systematically evaluated, so its general applicability is uncertain.
- The computational cost of the pipeline is mentioned but not benchmarked against other methods, making it difficult to assess its practicality for large systems.