## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion) as provided
- **Assessment boundary** Technical soundness, methodological validity, evidence quality, and claims as presented in the supplied text; no external validation performed
- **Shared manuscript claim summary** The authors present IDRWalker, a Python tool based on self-avoiding random walks, for generating initial structures of intrinsically disordered regions (IDRs) in large protein complexes. They claim linear time complexity, successful application to three test systems (SARS-CoV-2 spike, RyR1, human NPC), and generation of IDRs in over 800 chains of the NPC within minutes.
- **Visible evidence base** Methods description, three application case studies, runtime data (Table 1), force minimization results, supplementary figures referenced (Figures S1, S2)
- **Missing materials affecting confidence** No code repository or software availability statement; no validation against experimental data or known IDR conformations; no comparison with existing tools; no statistical analysis of generated conformations; no details on Ramachandran plot sampling strategy; no information on parameter selection (e.g., grid resolution, step limits); no reproducibility details

## Reviewer
- **Overall assessment** The manuscript addresses a practical need in integrative modeling of large protein complexes, namely the rapid generation of initial IDR conformations. The random walk approach is conceptually simple and computationally efficient, and the application to the NPC demonstrates scalability. However, the manuscript lacks rigorous validation of the generated conformations, provides no comparison with existing methods, and omits critical technical details that would allow reproduction. The claims of utility for integrative modeling are plausible but not established from the evidence presented.
- **Who would be interested in the results, and why** Researchers in structural biology, particularly those working on integrative modeling of large macromolecular complexes (e.g., nuclear pore complex, viral spike proteins, ion channels). The tool could be useful for generating starting structures for molecular dynamics simulations or for building complete models of complexes where IDRs are missing from cryo-EM maps. Computational biologists developing pipelines for integrative structure determination may also find the approach relevant.
- **Major strengths** The problem addressed is timely and relevant. The self-avoiding random walk approach is computationally efficient, as demonstrated by the NPC application. The tool automates a process that would otherwise require substantial manual effort. The authors identify and address practical issues such as knotting and chain connectivity. The manuscript is clearly written and accessible.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (no validation of conformational quality), R1-M2 (no comparison with existing methods), R1-M3 (insufficient technical detail for reproducibility), R1-M4 (no assessment of conformational diversity or ensemble representativeness)
- **Assessment against Nature-style criteria** 
  - **Originality** Moderate. Random walk approaches for IDR generation are not new, but the application to large complexes with automated processing is a practical contribution. The originality lies primarily in the engineering rather than the conceptual method.
  - **Scientific importance** Moderate. The tool addresses a bottleneck in integrative modeling, but the lack of validation limits the demonstrated impact. The importance is conditional on the tool being shown to produce useful conformations.
  - **Interdisciplinary readership** Limited. The manuscript is primarily of interest to structural biologists and computational biophysicists. The presentation assumes familiarity with protein structure and integrative modeling concepts.
  - **Technical soundness** The algorithmic description is plausible, but key details are missing (see R1-M3). The validation is insufficient to establish technical soundness (see R1-M1).
  - **Readability for nonspecialists** The manuscript is generally clear, but some sections (e.g., the random walk equations) assume specialized knowledge. The abstract and introduction are accessible to a broad scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The tool may be useful, but the manuscript requires substantial additional validation, comparison, and technical detail before the claims can be assessed.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation
- **Claim pointer** The authors claim that generated IDR structures are suitable for subsequent computational simulations and integrative modeling, and that spatial conflicts are "significantly eliminated."
- **Evidence pointer** Results sections for spike protein, RyR1, and NPC; Figure 3; Figure 4; Figure 5
- **Concern** The manuscript provides no quantitative validation of the generated IDR conformations. The only quality metric reported is maximum force after energy minimization, which is a necessary but insufficient check. There is no assessment of whether the generated conformations are physically reasonable (e.g., Ramachandran angles, side chain packing, secondary structure propensity), whether they sample a representative ensemble, or whether they are compatible with experimental data (e.g., cross-links, FRET distances). The claim that structures are suitable for integrative modeling is therefore unsupported.
- **Why it matters** Without validation, readers cannot assess whether the tool produces useful starting structures. A tool that generates conformations with severe steric clashes or unrealistic geometry would not be useful despite fast runtime. The suitability for integrative modeling is the central claim of the manuscript and must be demonstrated.
- **Resolution test** Provide quantitative validation of generated conformations, including: (1) Ramachandran angle distributions compared to known IDR ensembles; (2) radius of gyration distributions compared to experimental or theoretical expectations; (3) contact maps or distance distributions compared to available experimental data (e.g., cross-links); (4) assessment of steric clashes beyond maximum force; (5) comparison of generated ensembles to those from established methods (e.g., flexible-meccano, EOM).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Comparative benchmarking
- **Claim pointer** The authors imply that existing tools are "sometimes unsuitable for IDRs in large systems" and that IDRWalker addresses this gap.
- **Evidence pointer** Introduction, paragraph 3; Results sections
- **Concern** No comparison with existing IDR generation tools is provided. The claim that existing methods are unsuitable for large systems is not substantiated with specific examples or benchmarks. Without a head-to-head comparison, the advantage of IDRWalker over existing approaches (e.g., flexible-meccano, EOM, SASSIE, or even simple loop modeling tools) is not demonstrated.
- **Why it matters** The manuscript positions IDRWalker as a solution to a gap in existing methods. This claim requires evidence. If existing tools can handle large systems with comparable speed and quality, the contribution of IDRWalker is diminished. Conversely, if IDRWalker is faster or produces better conformations, this should be quantified.
- **Resolution test** Provide a benchmark comparing IDRWalker to at least one established IDR generation tool on the same test systems. Report runtime, success rate, conformational quality metrics, and suitability for downstream simulation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The manuscript describes the IDRWalker algorithm and its implementation.
- **Evidence pointer** Methods section, all subsections
- **Concern** Critical technical details are missing. Specifically: (1) the Ramachandran plot sampling strategy is not described (e.g., which regions are sampled, how probabilities are assigned); (2) the grid resolution for the occupancy matrix is not specified; (3) the criteria for "too many failed attempts" beyond the stated 1000 are not given; (4) the backtracking algorithm is not described in detail; (5) no information is provided on how the random seed is handled for reproducibility; (6) the software dependencies and installation instructions are not provided; (7) no statement on software availability or licensing is given.
- **Why it matters** Reproducibility is a core requirement for scientific software. Without these details, other researchers cannot implement or use the method. The manuscript cannot be evaluated for correctness if the algorithm is underspecified.
- **Resolution test** Provide a complete description of the algorithm, including pseudocode or a detailed flow diagram, specify all parameters and their default values, and make the code publicly available with documentation and installation instructions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Conformational sampling
- **Claim pointer** The authors state that IDRWalker can generate conformations for IDRs and that these can be used for integrative modeling, implying that the generated conformations are representative of the IDR ensemble.
- **Evidence pointer** Methods, "Residue Generation Loop"; Results sections; Conclusion
- **Concern** The manuscript does not address whether repeated runs of IDRWalker produce diverse conformations that sample the IDR ensemble. The authors note in the Conclusion that "each run of IDRWalker will generate only one conformation" and suggest running the program multiple times, but no data are shown on the diversity of conformations generated across runs. The self-avoiding random walk may produce conformations that are biased by the starting point and the backtracking mechanism, potentially leading to limited sampling.
- **Why it matters** IDRs exist as ensembles, and integrative modeling requires a representative set of starting conformations. If IDRWalker produces conformations that are not diverse or are biased, the downstream modeling may be compromised. The authors' own acknowledgment that the conformations "may not fully represent the native conformation ensembles" underscores this concern.
- **Resolution test** Generate multiple conformations for the same IDR using different random seeds and report the distribution of key properties (e.g., radius of gyration, end-to-end distance, secondary structure content). Compare this distribution to known IDR behavior or to ensembles generated by established methods.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods, "The Coordinates of Backbone Atoms"
- **Evidence pointer** Equations 1-3; Figure 2a
- **Issue** The equations are referenced but not shown in the provided text. The description of the rotation matrix and the Rodrigues formula is brief and assumes familiarity. The relationship between the variables in the equations and the terms in Figure 2a is not fully explained.
- **Required correction** Include the equations explicitly in the text or as numbered equations, and provide a more detailed explanation of the variables and their relationships to the figure.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods, "Spatial Conflicts Check"
- **Evidence pointer** Figure 2b
- **Issue** The manuscript mentions that "there is a risk of misjudging reasonable configurations as spatial conflicts" and refers to Figure 2b, but the figure is not described in the text. The specific scenario leading to misjudgment is unclear.
- **Required correction** Add a description of Figure 2b in the text, explaining the scenario and how the algorithm avoids or handles this misjudgment.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Results, "The Human NPC"
- **Evidence pointer** Figure 5
- **Issue** The figure is described as showing the NPC with added IDRs, but no quantitative information is provided about the quality of the generated conformations in this large system. The runtime is given in Table 1, but no metrics on steric clashes, chain connectivity, or conformational reasonableness are reported for the NPC.
- **Required correction** Provide quantitative metrics for the NPC-generated IDRs, such as the number of steric clashes before energy minimization, the success rate of chain connectivity, and the distribution of generated conformations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Software availability
- **Affected element** Abstract; Methods; Conclusion
- **Evidence pointer** Location not provided
- **Issue** No statement is made regarding the availability of the IDRWalker software, including whether it is open-source, where it can be downloaded, or under what license it is distributed.
- **Required correction** Add a "Data and Software Availability" statement providing the repository URL, license, and any dependencies.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Parameter sensitivity
- **Affected element** Methods, "Residue Generation Loop"
- **Evidence pointer** Location not provided
- **Issue** The manuscript does not discuss the sensitivity of the results to key parameters, such as the grid resolution of the occupancy matrix, the maximum number of failed attempts, or the Ramachandran sampling distribution.
- **Required correction** Include a brief discussion of parameter choices and their rationale, or provide a sensitivity analysis for at least one test system.

## Risk / unsupported claims
- The claim that IDRWalker "significantly eliminates" spatial conflicts is not quantitatively supported; only maximum force values are reported, and no comparison to a baseline or threshold is provided.
- The claim that existing tools are "sometimes unsuitable for IDRs in large systems" is not substantiated with specific examples or benchmarks.
- The claim that generated structures "can be further used to run computational simulations for integrative modeling" is plausible but not demonstrated; no downstream simulation or integrative modeling results are shown.
- The claim of "linear time complexity" is stated but not formally proven or empirically demonstrated with scaling data.
- The claim that the tool addresses "computational efficiency" is supported by runtime data, but the lack of comparison to other tools limits the strength of this claim.
- The statement that "only a few hundred atoms exhibited significantly high forces" in the spike protein is presented without a clear definition of "significantly high" or a comparison to typical values for acceptable starting structures.