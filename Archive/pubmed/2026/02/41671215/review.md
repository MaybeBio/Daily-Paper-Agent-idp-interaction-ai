## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methodology, results, discussion, conclusion) with figure/table references but no actual figures or tables provided
- **Assessment boundary** Scientific validity, methodological soundness, reproducibility, and claims as stated in the provided text; no code inspection or execution performed
- **Shared manuscript claim summary** The authors present QuPepFold, a Python package for hybrid quantum-classical protein folding simulations using a CVaR-optimized VQE. They claim: (1) the package provides a modular, accessible interface for biologists; (2) CVaR optimization accelerates convergence by approximately 30% compared to standard VQE; (3) hardware execution on IonQ Aria-1 achieves over 90% fidelity in ground-state energy reproduction; (4) results are consistent across simulators and physical devices; (5) the package can generate 3D PDB structures from quantum measurement outcomes; and (6) benchmarking on 1,224 peptide sequences (6-10 residues) demonstrates scalable performance with length-dependent success rates.
- **Visible evidence base** Textual descriptions of methodology, equations (referenced but not fully displayed), benchmark statistics in Section 3.8 and Table 5 (not visible), figure references (Figs 1-6, not visible), and discussion of comparative methods
- **Missing materials affecting confidence** All figures and tables; actual code repository; benchmark dataset details; raw energy distributions; hardware execution parameters; comparison data with classical methods; supplementary information

## Reviewer
- **Overall assessment** The manuscript presents a timely and potentially useful software contribution to the emerging field of quantum-assisted structural biology. The concept of democratizing quantum protein folding through a modular Python package is commendable and addresses a genuine gap in accessibility. However, the manuscript as provided has substantial issues that prevent full evaluation: key equations are referenced but not displayed, all figures and tables are missing, and the benchmark methodology lacks critical details. The central claims regarding CVaR acceleration and hardware fidelity cannot be independently verified from the provided material. The scientific framing around intrinsically disordered regions is compelling but the connection between the demonstrated results and IDR-specific challenges is not rigorously established. The manuscript would benefit from clearer articulation of what is genuinely novel versus incremental, and from more rigorous statistical treatment of the benchmark results.

- **Who would be interested in the results, and why** Computational structural biologists interested in alternative sampling methods for peptide conformations; quantum computing researchers working on near-term applications in chemistry and biology; software developers in the quantum biology space seeking modular tools; drug discovery researchers exploring novel approaches for targeting disordered proteins. The package's accessibility focus could also attract experimental biologists curious about quantum methods, though the practical utility for this group remains unclear.

- **Major Strengths** 
  1. Addresses a real accessibility gap in quantum-enhanced structural biology by providing a modular, pip-installable package
  2. The CVaR-VQE approach is a sensible adaptation of established quantum optimization techniques to the protein folding problem
  3. Backend-agnostic design (Qiskit, Braket, IonQ) demonstrates forward-thinking architecture
  4. The benchmarking across 1,224 sequences provides a substantial test corpus
  5. The discussion of limitations (hardware noise, sampling costs, short peptide lengths) is honest and appropriately contextualized

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "The CVaR-optimized VQE reached the ground state roughly 30 percent faster than a standard VQE based on expectation values"
- **Evidence pointer** Section 3.8, Table 5 (not visible)
- **Concern** The 30% acceleration claim is central to the paper's value proposition but is presented without sufficient methodological detail. The comparison protocol is not described: what constitutes "reaching the ground state"? How many independent runs were performed? What were the variance and statistical significance of this 30% figure? Was the comparison made on identical circuits, identical initial parameters, and identical optimization algorithms? The claim appears in both the abstract and results but the supporting evidence (Table 5) is not visible.
- **Why it matters** This is the primary quantitative claim differentiating QuPepFold from standard approaches. Without rigorous statistical backing, the claim cannot be assessed, and the reader cannot determine whether the 30% figure represents a robust effect or a single favorable run.
- **Resolution test** Provide the full comparison protocol, including number of runs, variance measures, statistical tests (e.g., confidence intervals or p-values), and the raw data underlying the 30% figure. Ideally, include convergence curves for both CVaR-VQE and standard VQE across multiple seeds.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Concern** The manuscript references equations (Eqs 1-5) and figures (Figs 1-6) that are not provided in the submitted text. The Hamiltonian formulation, qubit encoding scheme, and CVaR objective function are described verbally but the actual mathematical definitions are absent. The "modified Miyazawa-Jernigan potential" is mentioned but the modification is not specified. The turn-to-qubit mapping is described but the exact encoding (one-hot vs. dense) and its implications for circuit depth are not quantified.
- **Why it matters** Reproducibility is a core requirement for software contributions. Without the explicit equations, encoding schemes, and parameter values, another research group cannot implement or verify the method. The manuscript cannot be properly evaluated for correctness of the physics or the quantum formulation.
- **Resolution test** Include all equations in full mathematical notation. Specify the exact form of the modified MJ potential, including how it differs from the standard MJ matrix. Provide the complete turn-to-qubit mapping table. Include circuit diagrams or at minimum gate counts and depth for representative peptides.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim substantiation
- **Claim pointer** "When run on the IonQ Aria-1 quantum computer, it reproduced ground-state energies with over 90 percent fidelity"
- **Evidence pointer** Section 2.4, Section 3.8 (location not provided)
- **Concern** The hardware demonstration on IonQ Aria-1 is a significant claim but is described only in passing. The text states "In our previous experimental results [21,22]" suggesting this is not new data from this study, yet it is presented as a validation of QuPepFold. The specific peptides tested, the number of shots, the error mitigation techniques employed, and the definition of "fidelity" (state fidelity? energy fidelity? probability of correct ground state?) are not specified.
- **Why it matters** Hardware validation is critical for establishing that the package works beyond simulators. If the 90% fidelity claim is from prior work, it needs to be clearly attributed and its relevance to QuPepFold specifically demonstrated. The definition of fidelity materially affects interpretation.
- **Resolution test** Provide the hardware execution details: which peptides were run, how many qubits were used, what error mitigation was applied, and the exact definition of fidelity. If this is prior work, clarify the connection to QuPepFold and whether the package was used in those experiments.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific framing
- **Claim pointer** "QuPepFold offers an approachable yet extendable framework for integrating quantum techniques into peptide folding studies, particularly for sampling the ensembles of intrinsically disordered regions"
- **Evidence pointer** Section 1, Section 4
- **Concern** The manuscript repeatedly emphasizes the relevance to intrinsically disordered regions, but the benchmark results show that success rates drop dramatically with peptide length (99.6% for N=6 to 1.5% for N=10). IDRs are typically much longer than 10 residues. The connection between the demonstrated capabilities and the stated motivation is not established. Additionally, the claim that ground-state optimization is relevant for IDR ensemble sampling is questionable, since IDRs are characterized by ensembles of many nearly degenerate conformations rather than a single ground state.
- **Why it matters** The IDR framing is the primary biological motivation. If the method cannot address IDR-scale problems and the ground-state paradigm does not match IDR physics, the significance of the contribution is substantially weakened.
- **Resolution test** Either demonstrate relevance to IDR-like sequences (e.g., longer peptides, or explicit ensemble generation rather than single ground state) or reframe the motivation to match the demonstrated capabilities. Discuss how ground-state optimization relates to ensemble sampling for disordered regions.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Validation rigor
- **Claim pointer** "The agreement of results across simulators and physical devices indicates that the package yields consistent and transferable energies"
- **Evidence pointer** Section 3.8 (location not provided)
- **Concern** The claim of cross-platform consistency is made but no quantitative comparison is shown. What was the agreement metric? Were energies compared directly, or only the ranking of low-energy states? How many peptides were run on each backend? The benchmarking section focuses on success rates and mean energies but does not present a systematic cross-platform validation.
- **Why it matters** Transferability across backends is a key architectural claim for the package. Without quantitative agreement metrics, the reader cannot assess whether the package produces consistent physics across different execution environments.
- **Resolution test** Provide a direct comparison table showing energies for the same peptides on Aer, TN1, and IonQ Aria-1, with appropriate error bars and agreement statistics (e.g., mean absolute error, correlation coefficients).

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.5, CVaR definition
- **Evidence pointer** Section 2.5
- **Issue** The CVaR parameter alpha is described as "e.g., 5%" in one place and "0.025 in noiseless simulations and 0.05 on hardware" in another. The relationship between these values and the choice of alpha is unclear.
- **Required correction** Clarify the default alpha values, how they were chosen, and whether results are sensitive to this parameter.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2.6, Table 1
- **Evidence pointer** Section 2.6, Table 1 (not visible)
- **Issue** The manuscript states "The comprehensive list of the modular functions are provided in the Table 1" but the table is not visible. Without it, the package architecture cannot be fully assessed.
- **Required correction** Ensure Table 1 is included with the final submission, listing all functions, their inputs, outputs, and dependencies.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Section 3.8, benchmark results
- **Evidence pointer** Section 3.8, Table 5 (not visible)
- **Issue** The benchmark reports mean best energies and success rates but no measures of variance or statistical significance. The differences between peptide lengths (e.g., -2.97 vs -5.57 kcal/mol for N=6 vs N=7) are presented without error bars.
- **Required correction** Include standard deviations, confidence intervals, or other variance measures for all reported metrics.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Comparison fairness
- **Affected element** Section 4, comparison with classical methods
- **Evidence pointer** Section 4
- **Issue** The discussion mentions that quantum methods can sample lower-energy states more efficiently than MD but does not provide a direct comparison in this study. The referenced comparison [12,31] is not visible.
- **Required correction** Either include a direct comparison in this manuscript or clearly state that the comparison is from prior work and summarize the relevant findings.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Section 2.7, "modified Miyazawa-Jernigan potential"
- **Evidence pointer** Section 2.7
- **Issue** The term "modified" is used but the modification is never specified. This is important for reproducibility and for understanding what physics is being captured.
- **Required correction** Specify the exact modification to the MJ potential, including any scaling, shifting, or additional terms.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Section 2.6, package requirements
- **Evidence pointer** Section 2.6, Tables 3-4 (not visible)
- **Issue** The hardware requirements (16 GB RAM minimum) and software dependencies are listed in tables that are not visible. For a package aimed at democratization, these requirements are important for potential users.
- **Required correction** Ensure Tables 3 and 4 are included and consider discussing the accessibility implications of the resource requirements in the text.

- **Technical failings that need to be addressed before the case is established** 
  R1-M1 (30% acceleration claim without statistical backing), R1-M2 (missing equations and encoding details), R1-M3 (hardware fidelity claim not substantiated with current data). These three issues must be resolved before the central claims of the manuscript can be evaluated.

- **Assessment against Nature-style criteria**
  - **Originality**: Moderate. The application of CVaR-VQE to protein folding is not entirely new (referenced in [12]), and the lattice-based approach follows established work. The package itself is a software contribution rather than a fundamental scientific advance. The originality lies primarily in the integration and accessibility, which is valuable but not groundbreaking.
  - **Scientific importance**: Moderate. The potential to democratize quantum folding simulations is meaningful, but the demonstrated capabilities (peptides up to 10 residues, low success rates for longer chains) limit the immediate scientific impact. The IDR motivation is compelling but not matched by demonstrated capabilities.
  - **Interdisciplinary readership**: The manuscript bridges quantum computing and structural biology, which could attract readers from both communities. However, the technical depth in each area may limit accessibility for the other. The package's focus on biologist-friendly interfaces is a positive step.
  - **Technical soundness**: Cannot be fully assessed from the provided material. The missing equations, figures, and tables prevent evaluation of the core methodology. The benchmark results show expected trends (decreasing success with length) but lack statistical rigor.
  - **Readability for nonspecialists**: The abstract and introduction are accessible, but the methodology sections assume familiarity with both quantum computing and protein folding. The package's stated goal of accessibility is not fully reflected in the manuscript's presentation.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a potentially useful software tool with a sensible design and honest acknowledgment of limitations. However, the central quantitative claims (30% acceleration, 90% hardware fidelity) require rigorous substantiation, and the missing equations and figures must be provided. The IDR framing should be either better supported or moderated. If these issues are addressed, the manuscript could make a solid contribution to the quantum biology software ecosystem. Currently, the case is not fully established from the provided evidence.

## Risk / unsupported claims
- The 30% acceleration claim for CVaR-VQE over standard VQE is unsupported without the comparison protocol and statistical analysis
- The "over 90 percent fidelity" on IonQ Aria-1 is attributed to prior work [21,22] and cannot be verified as applying to QuPepFold specifically
- The claim of "consistent and transferable energies" across platforms is asserted without quantitative cross-platform comparison data
- The relevance to IDR ensemble sampling is asserted but not demonstrated; the ground-state optimization paradigm may not be appropriate for IDR physics
- The statement that QuPepFold "can theoretically access the global minimum" for N=10 peptides is based on a 1.5% success rate, which is too low to support this claim
- The "modified Miyazawa-Jernigan potential" is referenced but the modification is never specified, making the physics claims unverifiable
- The claim that the package "democratizes" quantum protein folding is plausible but requires demonstration of usability beyond the authors' own testing
- The benchmark dataset of 1,224 sequences is described but the selection criteria and representativeness are not discussed