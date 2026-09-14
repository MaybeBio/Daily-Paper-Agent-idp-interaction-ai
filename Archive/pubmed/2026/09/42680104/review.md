## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract
- **Shared manuscript claim summary** The authors report the use of crosslinking mass spectrometry (XL-MS) and integrative modeling, including an AlphaFold-enabled approach, to determine structural models of HDAC1/2-containing chromatin remodeling complexes (NuRD, SIN3A, CoREST). They claim that the C-terminal domain (CTD) intrinsically disordered region (IDR) of HDAC1 folds into alpha helices within these complexes, and they present a complete integrative structural model of a NuRD subcomplex containing six IDRs.
- **Visible evidence base** Abstract text only; no figures, tables, or supplementary materials are provided.
- **Missing materials affecting confidence** Full manuscript, all figures, tables, supplementary data, methods details, and validation statistics are absent. The abstract does not provide quantitative evidence (e.g., crosslink distances, model scores, confidence metrics) or any comparative analysis.

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting application of integrative structural biology to a challenging family of chromatin complexes. The combination of XL-MS and AlphaFold is timely, and the focus on IDR structure is a notable strength. However, the abstract lacks the quantitative detail and validation evidence necessary to assess the robustness of the claims. The central claim that the HDAC1 CTD IDR folds into alpha helices is stated without any supporting metrics (e.g., crosslink satisfaction, model precision, or comparison to alternative conformations). The "complete integrative structural model" of the NuRD subcomplex is mentioned but not described in terms of resolution, coverage, or validation. Without the full manuscript, the technical soundness and scientific importance of this work cannot be fully evaluated.
- **Who would be interested in the results, and why** Structural biologists, chromatin researchers, and biochemists studying protein complexes and intrinsically disordered regions. The work is relevant to those interested in the architecture of HDAC-containing complexes and the application of integrative modeling to large, dynamic assemblies.
- **Major strengths** 1. The use of XL-MS to constrain integrative models of multiple HDAC1/2 complexes is a technically sound and relevant approach. 2. The focus on the CTD IDR of HDAC1 and its potential folding within complexes addresses an important gap in the field. 3. The combination of AlphaFold with experimental crosslinking data is a promising methodological advance.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Evidence sufficiency
    - **Claim pointer** "We show that the CTD IDR of HDAC1 folds into alpha helices in these complexes."
    - **Evidence pointer** Abstract; location not provided
    - **Concern** The abstract provides no quantitative evidence to support the claim that the CTD IDR folds into alpha helices. No crosslink distances, model scores, or comparison to unfolded or alternative conformations are presented. The claim is stated as a conclusion without any supporting data.
    - **Why it matters** This is a central and non-obvious claim. IDRs are typically disordered, and demonstrating a specific folded state requires robust experimental and computational validation. Without evidence, the claim is unsubstantiated.
    - **Resolution test** Provide quantitative metrics: crosslink satisfaction rates, model precision (e.g., RMSD across ensemble), and comparison to a control (e.g., a model where the IDR is forced to be disordered). Show that the alpha-helical model is statistically preferred over alternative conformations.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Completeness of evidence
    - **Claim pointer** "we built a complete integrative structural model of a NuRD subcomplex including the abundant HDAC1:MBD3:MTA1:GATAD2B:RBBP4 subunits, which included 6 IDRs."
    - **Evidence pointer** Abstract; location not provided
    - **Concern** The abstract does not describe the model's resolution, coverage, or validation. The term "complete" is ambiguous and may be misleading. No information is given on how the six IDRs were modeled, what fraction of each IDR is resolved, or how the model was validated against independent data.
    - **Why it matters** The value of an integrative model depends on its precision, accuracy, and coverage. Without these details, the reader cannot assess whether the model is a reliable representation of the complex.
    - **Resolution test** Provide model statistics: precision (e.g., per-residue RMSD), coverage (percentage of residues modeled with high confidence), and validation against held-out crosslinks or other experimental data. Clarify what "complete" means in this context.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Methodological novelty and validation
    - **Claim pointer** "we implemented an AlphaFold-enabled XL-MS constrained modeling approach to investigate how HDAC1 could assemble into these complexes."
    - **Evidence pointer** Abstract; location not provided
    - **Concern** The abstract does not explain how AlphaFold and XL-MS were combined. Was AlphaFold used to generate initial models that were then refined with crosslink restraints? Or were crosslinks used to filter AlphaFold predictions? The novelty and effectiveness of this approach cannot be assessed.
    - **Why it matters** The methodological contribution is a key selling point. Without a clear description, the reader cannot evaluate whether the approach is a genuine advance or a routine application.
    - **Resolution test** Provide a clear workflow and validation: show that the combined approach outperforms AlphaFold alone or XL-MS alone in terms of model accuracy (e.g., against a known structure or crosslink satisfaction).

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Claim about broad applicability
    - **Evidence pointer** Abstract; location not provided
    - **Issue** The final sentence states that the approaches "are broadly applicable for the study of protein complexes and protein interaction networks that can provide important insights into IDRs." This is a generic statement that is not supported by evidence in the abstract.
    - **Required correction** Either remove this sentence or provide a specific example of how the approach could be applied to a different system.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Completeness
    - **Affected element** Description of the NuRD subcomplex model
    - **Evidence pointer** Abstract; location not provided
    - **Issue** The abstract mentions "a NuRD subcomplex" but does not specify which subcomplex (e.g., the full NuRD or a subassembly). This is ambiguous.
    - **Required correction** Clarify the exact composition of the modeled subcomplex and how it relates to the full NuRD complex.

- **Technical failings that need to be addressed before the case is established** R1-M1 and R1-M2 are blocking. The central claims about IDR folding and model completeness are not supported by the abstract. The full manuscript must provide quantitative validation for both.

- **Assessment against Nature-style criteria** 
    - **Originality**: Potentially high. The combination of XL-MS and AlphaFold for IDR modeling in large complexes is not routine. However, the abstract does not demonstrate that the approach yields novel insights beyond what is known.
    - **Scientific importance**: High, if validated. HDAC complexes are central to gene regulation, and the structure of the CTD IDR is a long-standing question.
    - **Interdisciplinary readership**: Moderate. The work is primarily of interest to structural biologists and chromatin researchers. The abstract does not make a case for broader appeal.
    - **Technical soundness**: Cannot be assessed from the abstract. The lack of quantitative evidence is a major concern.
    - **Readability for nonspecialists**: The abstract is clear and well-written, but the technical details are insufficient for a nonspecialist to evaluate the claims.

- **Recommendation posture** Currently not established from the provided evidence. The abstract presents an interesting premise, but the central claims are unsubstantiated. A full manuscript with quantitative validation is required to assess the work's suitability for a high-impact journal. Supportive if technical concerns are resolved.

## Risk / unsupported claims
- The claim that the CTD IDR of HDAC1 folds into alpha helices is unsupported.
- The claim that a "complete integrative structural model" of a NuRD subcomplex was built is unsupported.
- The claim that the approach is "broadly applicable" is unsupported.