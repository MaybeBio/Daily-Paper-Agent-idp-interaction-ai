## Review setup

- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as stated in the abstract, without access to full methods, figures, or supplementary data
- **Shared manuscript claim summary** The authors propose C11orf42 as a computationally inferred, conditionally relevant therapeutic target in triple-negative breast cancer (TNBC), supported by sequence and structural characterisation, protein-protein interaction network analysis, structure-based druggability assessment, molecular docking, molecular dynamics simulations, and functional genomics analysis of DepMap CRISPR-Cas9 data.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary materials provided
- **Missing materials affecting confidence** Full manuscript, methods details, docking scores and poses, MD simulation parameters and trajectories, DepMap data processing and statistical thresholds, compound sourcing and validation data, and any experimental validation

## Reviewer

- **Overall assessment** The abstract presents a broad, hypothesis-generating in silico study that integrates multiple computational methods to characterise a poorly understood gene, C11orf42, in the context of TNBC. The work is timely and potentially useful as a prioritisation screen for experimental follow-up. However, the abstract alone does not establish the central claim of therapeutic relevance. Key limitations include the absence of experimental validation, the speculative link between structural features and function, the lack of context-specific TNBC dependency evidence, and the unclear translational significance of the identified phytochemicals given poor drug-likeness properties. The manuscript may be suitable for a specialised computational biology journal, but the evidence as presented is insufficient to support the strong conclusion of a "potential therapeutic target."
- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on target discovery in cancer, particularly those using integrative structural and network approaches. Researchers studying undercharacterised genes in TNBC may find the prioritisation framework useful. The druggability and docking components may interest medicinal chemists focused on natural product screening, though the poor drug-likeness of the lead compounds limits immediate appeal.
- **Major strengths** The study integrates a wide range of computational methods, from sequence and structural analysis to network biology, docking, MD simulations, and functional genomics. The use of DepMap data to assess dependency context is a valuable addition that tempers overinterpretation of essentiality. The authors appropriately acknowledge the hypothesis-generating nature of several claims, such as the functional role of intrinsic disorder and the regulatory rather than core survival function of C11orf42.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (therapeutic relevance not established), R1-M2 (TNBC-specific dependency not demonstrated), R1-M3 (docking and MD evidence insufficient), R1-M4 (compound claims overreach the data)
- **Assessment against Nature-style criteria** Originality is moderate; the integrative approach is not novel, though the focus on C11orf42 is new. Scientific importance is limited by the lack of experimental validation and the speculative functional link. Interdisciplinary readership is possible but narrow, given the computational-only scope. Technical soundness cannot be fully assessed from the abstract, but several methodological details are missing. Readability for nonspecialists is acceptable, though the abstract is dense with technical terms and numerical results that may obscure the main message.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a plausible prioritisation framework, but the central claim of therapeutic relevance requires experimental validation and clearer TNBC-specific evidence. Supportive if technical concerns are resolved and the scope is reframed as hypothesis-generating.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim validity
- **Claim pointer** "C11orf42 as a potential therapeutic target in triple-negative breast cancer" and "prioritise C11orf42 as a computationally inferred, conditionally relevant regulatory candidate"
- **Evidence pointer** Abstract overall; no experimental validation reported
- **Concern** The central claim of therapeutic relevance is based entirely on computational inference. No experimental evidence, such as knockdown or overexpression studies, is provided to show that modulating C11orf42 affects TNBC cell viability, proliferation, or drug sensitivity. The abstract itself acknowledges the role is "hypothesis-generating" and "regulatory or modulatory," which is inconsistent with the strong framing of a "therapeutic target."
- **Why it matters** A therapeutic target must be functionally validated to justify further investment. Without experimental evidence, the claim is premature and could mislead readers into overestimating the translational potential of C11orf42.
- **Resolution test** Provide experimental data, such as siRNA or CRISPR knockdown in TNBC cell lines, showing a measurable phenotype. Alternatively, reframe the conclusion to clearly state that C11orf42 is a candidate for experimental prioritisation, not a validated target.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "context-restricted dependency profile" and relevance to TNBC
- **Evidence pointer** DepMap CRISPR-Cas9 screening data; no specific cell lines or cancer types named
- **Concern** The abstract states that C11orf42 is not pan-essential but displays a "context-restricted dependency profile." However, no details are given on which contexts show dependency, whether TNBC cell lines are among them, or the statistical significance and effect sizes. Without this information, the link to TNBC is speculative.
- **Why it matters** The TNBC relevance of the study hinges on showing that C11orf42 dependency is enriched in TNBC models. If the dependency is observed in unrelated lineages, the therapeutic rationale for TNBC is weakened.
- **Resolution test** Specify the cell lines and cancer types where dependency is observed, and provide statistical comparison showing enrichment in TNBC relative to other subtypes. If TNBC-specific dependency is not demonstrated, temper the conclusion accordingly.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "molecular docking identified four phytochemicals with favorable binding affinities" and "100-ns MD simulations" showing stability
- **Evidence pointer** Abstract only; no docking scores, poses, or MD simulation details provided
- **Concern** The docking and MD results are presented as key evidence for druggability, but the abstract lacks critical details: docking software and scoring function, receptor preparation, ligand protonation states, simulation temperature and pressure coupling, force field, and convergence criteria. The RMSD values for the full-length protein (10-12 Å) are high and attributed to C-terminal disorder, but it is unclear whether the ligand binding is stable in the TED core over the simulation. The binding affinity range (-8.9 to -9.6 kcal/mol) is reported without error estimates or comparison to known inhibitors.
- **Why it matters** Reproducibility and interpretation of computational results require full methodological transparency. Without these details, the reliability of the docking and MD findings cannot be assessed, and the claim of "favorable" binding is unsupported.
- **Resolution test** Provide full methods for docking and MD, including software versions, parameters, and validation steps. Show ligand RMSD and interaction persistence over the simulation, and compare docking scores to a positive control or known binder.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Overinterpretation
- **Claim pointer** "Chamaejasmin is a beyond-Ro5, high-affinity, long-residence C11orf42 inhibitor (t(1/2) = 118.07 h; logP = 2.87)"
- **Evidence pointer** Abstract; no kinetic or functional assay data
- **Concern** The term "inhibitor" implies functional inhibition, but no enzymatic or cellular activity assay is reported. The residence time (t(1/2) = 118.07 h) is likely derived from MD simulations, not experimental kinetics, and the abstract does not specify the method. The compound also has poor solubility, low oral bioavailability, and multiple drug-likeness violations, which the authors acknowledge, but the framing as a "high-affinity, long-residence inhibitor" overstates the evidence.
- **Why it matters** Calling a computationally docked compound an "inhibitor" without functional validation is misleading and could lead to inappropriate prioritisation for experimental testing.
- **Resolution test** Reframe the compound as a "predicted binder" or "candidate ligand" and specify that the residence time is a computational estimate. If experimental data exist, provide them.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract title and framing
- **Evidence pointer** Title and first sentence
- **Issue** The title states "potential therapeutic target," but the abstract concludes with "computationally inferred, conditionally relevant regulatory candidate." This inconsistency may confuse readers about the strength of the claim.
- **Required correction** Align the title and conclusion to reflect the hypothesis-generating nature of the study, or provide stronger evidence to justify the "therapeutic target" framing.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Protein function inference
- **Evidence pointer** "Intrinsic disorder supports conformational flexibility; however, specific functional roles remain hypothesis-generating"
- **Issue** The abstract mentions the TED domain and disordered C-terminal region but does not explain what a TED domain is or why it is relevant to TNBC. This may limit accessibility for nonspecialist readers.
- **Required correction** Briefly define the TED domain and its known or predicted function, and clarify how it relates to the proposed regulatory role in TNBC.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Network analysis results
- **Evidence pointer** "highly enriched network (71 nodes, 432 edges; p < 1.0 x 10(-16))"
- **Issue** The p-value is reported without specifying the enrichment test or the background set used. This makes it difficult to interpret the significance.
- **Required correction** Specify the enrichment method and background, and report the expected number of edges or a comparable metric.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Precision
- **Affected element** Compound properties
- **Evidence pointer** "logP = 2.87" and "logS = -6.36"
- **Issue** The units and calculation methods for logP and logS are not stated, and the solubility value is very low, which is acknowledged but not discussed in terms of medicinal chemistry implications beyond "formulation/scaffold optimisation."
- **Required correction** State the software or method used for these predictions and briefly discuss the feasibility of addressing the solubility issue.

## Risk / unsupported claims

- The claim that C11orf42 is a "potential therapeutic target" in TNBC is unsupported without experimental validation.
- The claim that the four phytochemicals are "inhibitors" is unsupported; they are predicted binders at best.
- The "context-restricted dependency profile" is unverifiable without specific cell line and cancer type details.
- The functional role of the disordered C-terminal region is speculative and acknowledged as such, but the abstract still implies relevance to TNBC signalling.
- The druggability assessment is based on predicted pockets and docking, with no experimental confirmation of ligand binding or cellular activity.
- The translational relevance of the compounds is questionable given the reported poor solubility, low bioavailability, and drug-likeness violations.