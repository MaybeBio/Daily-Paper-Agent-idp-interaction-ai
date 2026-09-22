## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion) as provided.
- **Assessment boundary** Scientific and technical evaluation of the software package SOURSOP as described, including its design, demonstrated analyses, and claims of utility for the IDP simulation community. No code execution or independent testing was performed.
- **Shared manuscript claim summary** The authors present SOURSOP, an open-source Python package for analyzing simulations of intrinsically disordered proteins (IDRs). The package is built on MDTraj, offers polymer-physics-inspired analysis routines, and is designed to be extensible and user-friendly. The authors demonstrate its application to previously published simulation ensembles, highlighting sequence-dependent conformational biases, the role of specific residue types, and context-dependent molecular accessibility.
- **Visible evidence base** The manuscript text, including equations for asphericity (δ*) and the dimensionless parameter t, descriptions of functions (e.g., get_asphericity, get_t, get_local_collapse, get_distance_map, get_regional_SASA), and figures referenced (Fig. 1A, 1B, 2A, 2B, 3, 4, 5A, 5B, 6, S1). Supplementary Table S1 is mentioned but not provided.
- **Missing materials affecting confidence** The actual code repository, documentation, unit tests, and example Jupyter notebooks were not provided for review. The full set of simulation trajectories and force field parameters used in the demonstration analyses are not described in sufficient detail. Supplementary Table S1 (survey of analysis packages) and Figure S1 are referenced but not included. No performance benchmarks or comparisons against existing tools are provided.

## Reviewer
- **Overall assessment** This manuscript describes a timely and potentially valuable software contribution to the IDP simulation community. The package addresses a clear gap: the lack of a dedicated, lightweight, and extensible analysis toolkit for disordered protein ensembles. The design choices, such as building on MDTraj and using polymer physics principles, are sensible and well-motivated. The demonstration analyses are illustrative but largely retrospective, and the manuscript would benefit from a more rigorous validation of the software's correctness and performance. The claims of extensibility and community benefit are plausible but not fully substantiated by the evidence provided. Overall, the work is of interest to a specialized but growing community, and the software could become a useful resource if the technical concerns are addressed.
- **Who would be interested in the results, and why** Researchers in the field of intrinsically disordered proteins and unfolded states, particularly those who perform all-atom or coarse-grained simulations. This includes computational biophysicists, physical chemists, and structural biologists interested in sequence-ensemble relationships. The package's focus on polymer physics metrics and its integration with MDTraj will appeal to those seeking standardized, reproducible analysis workflows. The broader community of software developers in computational chemistry may also be interested in the architectural choices and extensibility model.
- **Major strengths**
  1. The software addresses a clear and important need in the IDP simulation field, where analysis tools are often fragmented or not tailored to disordered systems.
  2. The design is thoughtful, leveraging MDTraj for trajectory handling and offering a clean, object-oriented interface (SSTraj, SSProtein) that promotes ease of use and extensibility.
  3. The inclusion of polymer-physics-based metrics (e.g., t, δ*, scaling maps) provides a physically meaningful framework for comparing ensembles across different sequences and conditions.
  4. The commitment to open-source development, documentation, unit testing, and community contribution is commendable and aligns with best practices in scientific software.
  5. The demonstration of the package on multiple previously published ensembles, including a case with phosphomimetic mutations, shows its practical utility in generating biological insights.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness and validation
  - **Claim pointer** The manuscript implies that SOURSOP provides correct and reliable analyses, as it is presented as a ready-to-use toolkit.
  - **Evidence pointer** Methods section, Results section, Figures 2-6, location not provided
  - **Concern** The manuscript does not provide any validation of the numerical correctness of the implemented analyses. There are no comparisons against analytical solutions, established software (e.g., CAMPARI's built-in analysis, MDTraj, or other packages), or hand-calculated examples. The unit tests are mentioned but not described or made available for review. Without such validation, the reliability of the results produced by SOURSOP is unsubstantiated.
  - **Why it matters** For a software package intended for scientific use, numerical accuracy is paramount. Users must be confident that the metrics calculated (e.g., t, δ*, scaling exponents, SASA) are correct. A single error in an implementation could lead to incorrect biological conclusions. The lack of validation is a critical gap that prevents the case for the software's utility from being established.
  - **Resolution test** The authors should provide a clear validation section, including (1) comparisons of SOURSOP outputs against analytical results for simple polymer models, (2) cross-validation against existing tools (e.g., CAMPARITraj, MDTraj) on identical trajectories, and (3) a description of the unit test suite with examples. Ideally, the test code and results should be made available in the repository.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Reproducibility and completeness of demonstration
  - **Claim pointer** The Results section claims to demonstrate the package's utility by analyzing a collection of ensembles generated by CAMPARI and Desmond.
  - **Evidence pointer** Results section, Figures 2-6, location not provided
  - **Concern** The details of the simulation ensembles used for the demonstrations are insufficient. The specific sequences, force fields, simulation lengths, and convergence criteria are not described. This makes it impossible to reproduce the analyses or assess whether the observed conformational biases are robust or artifacts of the specific simulations. The choice of the p53-derived peptide for the phosphomimetic study is mentioned, but the rationale and simulation details are lacking.
  - **Why it matters** Reproducibility is a cornerstone of scientific software. Without detailed information on the input data, the demonstration analyses cannot be independently verified or extended. This limits the manuscript's value as a scientific contribution and undermines the credibility of the biological insights presented.
  - **Resolution test** The authors should provide a supplementary table or section detailing the sequences, simulation protocols, and force fields for all ensembles analyzed. The trajectories and analysis notebooks should be made publicly available, as suggested in the Methods, but this must be explicitly stated and verified.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Comparative advantage and novelty
  - **Claim pointer** The Introduction and Discussion imply that SOURSOP fills a gap in the analysis software landscape for IDPs.
  - **Evidence pointer** Introduction, Discussion, Supplementary Table S1 (not provided), location not provided
  - **Concern** The manuscript does not provide a systematic comparison of SOURSOP against existing analysis tools. While it mentions that some routines overlap with CAMPARI and that general-purpose tools exist, it does not clearly articulate what specific analyses are unique to SOURSOP or what advantages it offers over, for example, using MDTraj directly with custom scripts. The referenced survey of ~100 packages (Table S1) is not included, making it impossible to assess the competitive landscape.
  - **Why it matters** For a new software package to be adopted, its unique value proposition must be clear. If all analyses can be performed with existing tools, the case for SOURSOP is weakened. A clear comparison of features, performance, and ease of use against at least one or two key alternatives is necessary to establish its niche.
  - **Resolution test** The authors should include a table comparing SOURSOP's features against a few representative existing tools (e.g., CAMPARI, MDTraj, LOOS, and perhaps a dedicated IDP analysis package if one exists). This should highlight unique functionalities, performance benchmarks, and user experience.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity and completeness of documentation
  - **Affected element** Methods section, software architecture description
  - **Evidence pointer** Methods section, Figure 1A, location not provided
  - **Issue** The description of the software architecture is brief. While the object model (SSTraj, SSProtein) is mentioned, the role of peripheral modules (ssnmr, sspre) is not explained. The relationship between these modules and the core objects is unclear.
  - **Required correction** Provide a more detailed description of the architecture, including a diagram or explanation of how the peripheral modules interact with the core objects and what specific analyses they enable.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Introduction, Discussion
  - **Evidence pointer** Introduction, Discussion, location not provided
  - **Issue** The manuscript assumes familiarity with polymer physics concepts (e.g., blob length, theta solvent, scaling exponent) without providing brief definitions or intuitive explanations. This may limit accessibility for researchers new to the field or from experimental backgrounds.
  - **Required correction** Add a short paragraph in the Introduction or a glossary in the Supplementary Material defining key polymer physics terms used throughout the manuscript.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Equation 3, definition of t
  - **Evidence pointer** Methods section, Equation 3, location not provided
  - **Issue** The definition of t is given as a formula with parameters f1, f2, and f3, but the physical meaning of these parameters and the derivation of the formula are not explained. The reference to Vitalis and Pappu is given, but the formula appears to be a normalization that is not immediately intuitive.
  - **Required correction** Briefly explain the rationale behind the definition of t and the role of each parameter, or refer the reader to a specific section of the cited work for a detailed derivation.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Results section, Figure 5
  - **Evidence pointer** Results section, Figure 5, location not provided
  - **Issue** The phosphomimetic study on p53 is presented as a demonstration, but the choice of this specific system and the mutations is not justified. The statement that glutamic acid is an "imperfect analog" for phosphate is made, but the implications of this limitation for the interpretation are not discussed.
  - **Required correction** Provide a brief rationale for the choice of this system and discuss the potential limitations of using glutamic acid as a phosphomimetic in the context of the observed results.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Interdisciplinary readership
  - **Affected element** Discussion, SOURSOP in the broader ecosystem
  - **Evidence pointer** Discussion, location not provided
  - **Issue** The discussion of coarse-grained simulations is brief and somewhat tangential. The statement that SOURSOP "unofficially" works for coarse-grained simulations is vague and could be misleading.
  - **Required correction** Either provide a clear statement of which routines are applicable to coarse-grained simulations and any known limitations, or remove this section to avoid ambiguity.

## Risk / unsupported claims
- The claim that SOURSOP is a "unique collection" of analysis routines is not fully supported, as the manuscript does not provide a comprehensive comparison with existing tools.
- The claim that the package is "easy to use" and "extensible" is plausible but not quantitatively demonstrated; no usability studies or developer testimonials are provided.
- The biological insights presented (e.g., the role of aromatic, charged, and proline residues) are based on retrospective analyses of previously published simulations and are not novel findings of this work. The manuscript should clarify that these are illustrative examples, not new discoveries.
- The statement that SOURSOP can analyze "simulations of intrinsically disordered proteins" is broad; the manuscript only demonstrates its use on all-atom ensembles from CAMPARI and Desmond. Its applicability to other simulation types (e.g., coarse-grained, lattice models) is not rigorously tested.
- The claim that the package supports "the development and implementation of new analysis routines" is not verified; no examples of third-party contributions or a plugin architecture are shown.