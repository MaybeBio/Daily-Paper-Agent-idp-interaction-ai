## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific and technical soundness of the proposed method, validity of claims relative to presented evidence, and quality of comparison against baseline tools
- **Shared manuscript claim summary** The authors propose a topology-based rigid-body docking algorithm that extracts topological and geometric features from protein surface models to predict binding poses for intrinsically disordered proteins (IDPs). They claim improved computational performance and binding affinity compared to HawkDock and HDOCK across nine Plasmodium falciparum proteins and six IDPs, with 95% of cases showing better binding affinity.
- **Visible evidence base** Abstract, Introduction, Results (Sections 2.1, 2.2 with subsections), Discussion, Materials and Methods (Section 4), Conclusions. Figures referenced but not visible. Tables referenced but not visible. Algorithm pseudocode provided.
- **Missing materials affecting confidence** Figures 1-8 not visible; Tables 1-2 not visible; no statistical analysis details; no raw data or error bars; no detailed description of scoring function derivation; no code availability statement; no supplementary materials

## Reviewer

- **Overall assessment** The manuscript addresses a relevant problem in structural biology, namely the computational prediction of IDP binding behavior, which is challenging due to the lack of stable 3D structures. The proposed approach of using topological data analysis on protein surface models is conceptually interesting and potentially useful. However, the manuscript has substantial technical and presentational weaknesses that prevent the case from being fully established. The comparison against baseline tools is incomplete, the evaluation metrics are not rigorously defined, and several claims are not supported by the evidence presented. The work may have merit as a preliminary methodological contribution, but the current form does not provide sufficient validation.

- **Who would be interested in the results, and why** Computational structural biologists, researchers studying protein-protein interactions involving IDPs, and developers of docking algorithms would find this work relevant. The potential application to host-pathogen interactions, specifically malaria, may also interest researchers in infectious disease biology. However, the audience is likely limited to specialists in computational docking and IDP biology rather than a broad interdisciplinary readership.

- **Major strengths** The manuscript addresses a genuine gap in docking methodology, namely the handling of IDPs which are poorly represented by traditional rigid-body docking approaches. The use of topological data analysis to extract surface features is a creative and potentially powerful idea. The authors consider both quantitative (computational time) and qualitative (binding affinity) performance metrics. The inclusion of path planning as part of the docking pipeline is a distinctive feature that could provide additional biological insight.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The algorithm identifies a geometrically favorable binding pose for the IDP and plans a feasible trajectory to evaluate its transition to the docking position.
- **Evidence pointer** Section 4.2, Algorithm 1, Equation (2)
- **Concern** The scoring function in Equation (2) uses the Hausdorff distance between the protein surface and the IDP conformation. However, the manuscript does not provide a clear justification for why the Hausdorff distance is an appropriate proxy for binding affinity or geometric complementarity. The Hausdorff distance is sensitive to outliers and may not capture the local geometric complementarity that is typically important for protein-protein binding. Furthermore, the manuscript does not explain how the "geometrically favorable" pose is validated against known binding sites or experimental structures.
- **Why it matters** The core claim of the method is that it identifies geometrically favorable binding poses. If the scoring function is not well-justified or validated, the entire methodological contribution is called into question. Without evidence that the Hausdorff distance correlates with actual binding affinity or known binding sites, the results cannot be interpreted as meaningful predictions.
- **Resolution test** The authors should validate their scoring function against a set of known protein-protein complexes with experimentally determined binding interfaces, demonstrating that the Hausdorff distance-based ranking correlates with known binding sites. Alternatively, they should provide a more rigorous theoretical justification for why this metric captures binding-relevant geometric features.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** Our method outperformed the compared methods in computational performance and binding affinity in experimental conformations.
- **Evidence pointer** Section 2.2, Figures 5 and 6, Table 2
- **Concern** The comparison against HawkDock and HDOCK is not adequately described. The manuscript does not specify the exact input formats, parameter settings, or versions of the baseline tools used. It is unclear whether the baseline tools were given the same starting conformations or whether they were allowed to run to convergence. The claim of "95% of compared cases" showing better binding affinity is presented without statistical significance testing or error analysis. Additionally, the binding affinity values are not compared against experimentally determined values, only against the predictions of other computational tools.
- **Why it matters** A fair and rigorous comparison is essential to support the claim of superiority. Without detailed experimental setup, statistical analysis, and validation against experimental data, the performance claims are not convincing. The comparison may be biased if the baseline tools were not optimally configured.
- **Resolution test** The authors should provide a detailed description of the comparison protocol, including parameter settings, input preparation, and any preprocessing steps. They should perform statistical significance testing (e.g., paired t-tests or Wilcoxon signed-rank tests) on the binding affinity differences. They should also validate their predicted binding affinities against experimentally determined values for at least a subset of the complexes.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** We performed experiments for nine globular proteins interacting with six IDP molecules in the conformation space.
- **Evidence pointer** Section 2.1, Table 1
- **Concern** The manuscript does not provide sufficient details about the dataset. The PDB identifiers for the nine proteins and six IDPs are not listed in the text. The criteria for selecting these specific proteins and IDPs are not explained. The source of the IDP conformations (whether from PDB structures, AlphaFold predictions, or molecular dynamics simulations) is not clearly stated. The manuscript also does not specify how the "high-dimensional surface models" were constructed from the PDB structures.
- **Why it matters** Reproducibility is a fundamental requirement for scientific contributions. Without complete dataset information, other researchers cannot replicate the experiments or assess the generalizability of the findings. The selection of test cases may introduce bias if not justified.
- **Resolution test** The authors should provide a table listing all PDB IDs, chain identifiers, and relevant details for each protein and IDP used in the study. They should describe the criteria for dataset selection and the procedure for constructing surface models.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The feature extraction process was independent of the globular protein's size and had minimal effect on the performance of our algorithm.
- **Evidence pointer** Section 2.2.1
- **Concern** This claim is made without presenting any data that directly tests the relationship between protein size and feature extraction time. The statement appears to be an inference from the overall results rather than a controlled analysis. The manuscript does not show a plot of feature extraction time versus protein size, nor does it provide correlation coefficients or other statistical measures.
- **Why it matters** The scalability of the method is an important practical consideration. If the claim of size independence is incorrect, the method may not be suitable for larger protein complexes, which are common in biological systems.
- **Resolution test** The authors should present a direct analysis of feature extraction time as a function of protein size, with appropriate statistical measures, to support or qualify this claim.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Evidence quality
- **Claim pointer** Our findings revealed that our geometrically fitting binding conformation exhibited binding affinities that were highly similar to the known binding affinities of these protein complexes.
- **Evidence pointer** Section 2.2.2, Table 2
- **Concern** The comparison to known IDP complexes (4HTP, 3W1G, 3ALO, 1SB0) is presented in a table, but the table is not visible. The manuscript does not describe how the "known binding affinities" were obtained, whether from experimental measurements or previous computational studies. The criteria for "highly similar" are not defined quantitatively. It is unclear whether the comparison is against the same binding mode or a different one.
- **Why it matters** This validation against known complexes is potentially the strongest evidence for the method's utility. However, without visible data and clear criteria for similarity, the claim cannot be evaluated.
- **Resolution test** The authors should present the data in a visible table with clear labels for the source of known binding affinities, the predicted values, and the quantitative measure of similarity. They should also discuss any discrepancies and their potential causes.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 4.1, Mathematical Definitions
- **Evidence pointer** Section 4.1
- **Issue** The mathematical definitions section is incomplete and difficult to follow. The text states "The elements of the set are called vertices, and the set itself is a simplex" without defining what set is being referred to. Definitions 5, 6, and 7 are referenced but not stated in the text. The discrete Morse function is mentioned but not explicitly defined.
- **Required correction** The authors should provide complete and self-contained mathematical definitions, including the referenced definitions, so that the methodology can be understood without external references.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.2.1, Computational Time
- **Evidence pointer** Figure 5
- **Issue** The description of the computational time comparison is vague. The manuscript states that the method was faster "in all PF pathogen protein conformation spaces except for 2LE3" but does not provide specific numbers or a quantitative summary of the speedup.
- **Required correction** The authors should provide specific time values or a summary statistic (e.g., median speedup factor) in the text, in addition to the figure.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2.2.2, Binding Affinity Measure
- **Evidence pointer** Figure 6
- **Issue** The manuscript states that HawkRawkDock exhibited positive binding affinity for the 7KPI IDP with 1SQ6 and 4JUE proteins, but does not explain why this occurred or what it implies about the baseline method's limitations.
- **Required correction** The authors should provide a brief interpretation of why the baseline method produced positive binding affinities in these cases and what this indicates about the method's applicability.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 3, Discussion
- **Evidence pointer** Section 3
- **Issue** The discussion of related work is somewhat disjointed and does not clearly position the proposed method relative to existing approaches. The connection between the cited works and the proposed method is not always explicit.
- **Required correction** The authors should strengthen the discussion by explicitly stating how their method differs from and improves upon each cited approach.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 4.2, Algorithm 1
- **Evidence pointer** Algorithm 1
- **Issue** The pseudocode is not fully self-explanatory. The notation "◃" is used without explanation, and the references to "Definition 2", "Definitions 5 and 6", and "Definition 7" are not resolvable from the text.
- **Required correction** The authors should either include the referenced definitions in the text or provide sufficient explanation within the pseudocode so that it can be understood independently.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 5, Conclusions
- **Evidence pointer** Section 5
- **Issue** The conclusion mentions "structure-based vaccine design processes" as a potential application, but this is not discussed anywhere else in the manuscript. This appears to be an unsupported extrapolation.
- **Required correction** The authors should either provide a brief explanation of how their method could contribute to vaccine design or remove this claim.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.1, Experimental Data
- **Evidence pointer** Section 2.1
- **Issue** The manuscript states that IDPs were selected "based on their highly disordered behavior shown in the protein feature view plot available in the PDB database" but does not provide specific criteria or thresholds for what constitutes "highly disordered."
- **Required correction** The authors should provide quantitative criteria for IDP selection, such as disorder prediction scores or percentage of disordered residues.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2.2, Experimental Analysis
- **Evidence pointer** Section 2.2
- **Issue** The manuscript mentions that 1250 experiments were executed with values averaged over 10 runs, but does not explain why this specific number of experiments was chosen or how the 10 runs were configured (e.g., different random seeds, different initial conformations).
- **Required correction** The authors should clarify the experimental design, including the rationale for the number of runs and the sources of variability across runs.

## Technical failings that need to be addressed before the case is established
R1-M1 (scoring function justification), R1-M2 (comparison rigor), R1-M3 (dataset completeness), R1-M4 (size independence claim), R1-M5 (validation against known complexes)

## Assessment against Nature-style criteria
**Originality**: Moderate. The application of topological data analysis to IDP docking is somewhat novel, but the underlying concepts of surface-based docking and path planning are well-established. The novelty is incremental rather than transformative.

**Scientific importance**: Moderate. IDP binding is an important problem, and improved computational tools would be valuable. However, the manuscript does not demonstrate that the method provides biological insights beyond what existing tools offer.

**Interdisciplinary readership**: Limited. The manuscript is written for a specialized audience of computational structural biologists. The methodology and evaluation are not accessible to a broader scientific readership.

**Technical soundness**: Weak. The scoring function is not well-justified, the comparison against baselines is not rigorously described, and the statistical analysis is insufficient. The mathematical foundations are incompletely presented.

**Readability for nonspecialists**: Poor. The manuscript assumes significant prior knowledge of topological data analysis, docking algorithms, and IDP biology. Key concepts are not explained for readers outside the immediate field.

## Risk / unsupported claims
- The claim that the method "outperformed the compared methods in computational performance and binding affinity" is not fully supported due to incomplete comparison details and lack of statistical testing.
- The claim that "the feature extraction process was independent of the globular protein's size" is not directly tested.
- The claim that binding affinities were "highly similar" to known values is not quantifiable without the visible table.
- The statement that the method "presents the potential for advancing the development of structure-based vaccine design processes" is unsupported by any evidence in the manuscript.
- The claim that the method "successfully captures the geometric features of the protein surfaces" is not validated against known surface features or binding sites.