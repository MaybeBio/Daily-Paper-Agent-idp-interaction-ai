## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract
- **Shared manuscript claim summary** The authors report the use of crosslinking mass spectrometry (XL-MS) and integrative modeling, including an AlphaFold-enabled approach, to determine structural models of the NuRD, SIN3A, and CoREST complexes involving HDAC1/2. They claim that the C-terminal domain (CTD) intrinsically disordered region (IDR) of HDAC1 folds into alpha helices within these complexes, and they present a complete integrative structural model of a NuRD subcomplex containing six IDRs.
- **Visible evidence base** Abstract text only; no figures, tables, or supplementary materials are provided.
- **Missing materials affecting confidence** Full manuscript, all figures and tables, supplementary data (including XL-MS data, crosslink distance constraints, modeling parameters, validation metrics, and AlphaFold outputs), and detailed methods.

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting and technically ambitious approach to studying the structure of large, dynamic chromatin remodeling complexes, with a focus on the role of intrinsically disordered regions. The combination of XL-MS and integrative modeling is timely, and the claim that the HDAC1 CTD IDR adopts alpha-helical conformations in complex contexts is noteworthy. However, the abstract alone provides insufficient evidence to evaluate the validity, rigor, or novelty of the work. The core claims are stated without any quantitative support, and the absence of any structural validation metrics or comparison to existing models is a significant concern. The manuscript may be of interest to the structural biology and chromatin fields, but the current evidence base is too thin to assess its suitability for a high-impact venue.
- **Who would be interested in the results, and why** Structural biologists and biochemists studying chromatin remodeling complexes, particularly the NuRD, SIN3, and CoREST complexes. Researchers interested in the structural biology of intrinsically disordered regions (IDRs) and their folding upon complex assembly. The integrative modeling methodology may also be of interest to computational biologists developing hybrid structural biology approaches.
- **Major strengths** 1. The focus on large, multi-subunit complexes with significant IDR content addresses a challenging and important problem in structural biology. 2. The combination of XL-MS with AlphaFold-enabled modeling is a contemporary and potentially powerful approach. 3. The claim of modeling a subcomplex with six IDRs is ambitious and, if validated, would represent a significant technical achievement.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Evidence sufficiency
    - **Claim pointer** "We show that the CTD IDR of HDAC1 folds into alpha helices in these complexes."
    - **Evidence pointer** Abstract; location not provided
    - **Concern** The abstract provides no quantitative evidence for this claim. There is no mention of the number of crosslinks supporting the alpha-helical conformation, the confidence of the secondary structure prediction, or any validation metrics (e.g., crosslink satisfaction rate, model precision, or comparison to known structures). The claim is stated as a conclusion without any supporting data.
    - **Why it matters** This is a central and novel claim of the work. Without evidence, the reader cannot assess whether the observed alpha-helical folding is a robust, reproducible finding or an artifact of the modeling procedure. The structural state of IDRs in complexes is a key biological question, and unsupported claims undermine the manuscript's credibility.
    - **Resolution test** The authors must provide, in the full manuscript, clear evidence for the alpha-helical folding of the HDAC1 CTD IDR. This should include: (a) the number and distribution of crosslinks that are consistent with an alpha-helical model, (b) the confidence scores from the AlphaFold or other secondary structure prediction, (c) a comparison of the model to a random coil or alternative secondary structure models, and (d) validation metrics such as crosslink satisfaction rates and model precision for the IDR region.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Evidence sufficiency
    - **Claim pointer** "we built a complete integrative structural model of a NuRD subcomplex including the abundant HDAC1:MBD3:MTA1:GATAD2B:RBBP4 subunits, which included 6 IDRs."
    - **Evidence pointer** Abstract; location not provided
    - **Concern** The abstract does not provide any metrics for the quality or completeness of this integrative model. Terms like "complete" are undefined. There is no mention of model precision, crosslink satisfaction rate, sampling convergence, or any other standard validation metric for integrative structural models. The number of IDRs (6) is stated, but their lengths, the number of crosslinks within them, and the confidence of their modeled conformations are not described.
    - **Why it matters** Integrative modeling produces ensembles of models, and the quality of the result is critically dependent on the density and quality of the experimental restraints. Without validation metrics, the reader cannot distinguish between a high-confidence, well-constrained model and a low-resolution, poorly defined model. The claim of a "complete" model is misleading without such context.
    - **Resolution test** The authors must provide, in the full manuscript, standard validation metrics for the integrative model. This should include: (a) the precision of the model (e.g., RMSD of the ensemble), (b) the crosslink satisfaction rate (fraction of crosslinks satisfied by the model), (c) the convergence of the sampling, and (d) a clear definition of what "complete" means in this context (e.g., all residues modeled, all subunits included, etc.).

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Novelty and context
    - **Claim pointer** "How HDAC1/2 assemble into these complexes and the structure of the CTD IDR remains poorly understood."
    - **Evidence pointer** Abstract; location not provided
    - **Concern** The abstract does not place the current work in the context of existing structural knowledge. There are known structures of NuRD, SIN3, and CoREST subcomplexes, including some with HDAC1/2. The abstract does not state what new structural information is being provided beyond what is already known, nor does it explain how the current models differ from or improve upon existing structures.
    - **Why it matters** For a high-impact journal, the novelty and advance over the state of the art must be clearly articulated. Without this context, the reader cannot assess the significance of the work. The claim that the structure is "poorly understood" is vague and may be contradicted by existing literature.
    - **Resolution test** The authors must provide, in the full manuscript, a clear comparison of their models to existing structures (e.g., from cryo-EM or X-ray crystallography). They should explicitly state what new features are revealed by their integrative models (e.g., new IDR conformations, subunit interfaces, or dynamic regions) and how these advance the understanding of complex assembly and function.

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Methodology description
    - **Evidence pointer** Abstract; location not provided
    - **Issue** The phrase "AlphaFold-enabled XL-MS constrained modeling approach" is ambiguous. It is unclear whether AlphaFold is used to generate initial models that are then refined with XL-MS constraints, or whether XL-MS constraints are used to guide or filter AlphaFold predictions.
    - **Required correction** Clarify the exact workflow. For example: "We used AlphaFold to generate initial models of the HDAC1-containing complexes, which were then refined and validated using XL-MS distance constraints" or "We used XL-MS distance constraints to guide the sampling of AlphaFold predictions."

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Scope
    - **Affected element** Claim of broad applicability
    - **Evidence pointer** Abstract; location not provided
    - **Issue** The final sentence states the approaches are "broadly applicable for the study of protein complexes and protein interaction networks that can provide important insights into IDRs." This is a generic statement that is not supported by the abstract alone.
    - **Required correction** Either remove this statement or provide a specific example of how the approach could be applied to a different system, or state a generalizable principle that emerges from the work.

- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3. The central claims of the abstract (alpha-helical folding of the HDAC1 CTD IDR and a complete integrative model of a NuRD subcomplex) are presented without any supporting evidence or validation metrics. The novelty of the work relative to existing structural knowledge is not established.

- **Assessment against Nature-style criteria**
    - **Originality:** Potentially original, as the combination of XL-MS and AlphaFold for modeling IDRs in large complexes is not routine. However, the abstract does not demonstrate that the findings are novel beyond what is already known from existing structures.
    - **Scientific importance:** High, if validated. Understanding the structure and dynamics of IDRs in chromatin remodeling complexes is a major goal in the field. The work could provide important insights into complex assembly and regulation.
    - **Interdisciplinary readership:** Moderate. The work is primarily of interest to structural biologists and chromatin researchers. The methodology may appeal to a broader computational biology audience, but the abstract does not make a strong case for this.
    - **Technical soundness:** Cannot be assessed from the abstract. The lack of any validation metrics or quantitative data prevents evaluation of the technical rigor.
    - **Readability for nonspecialists:** The abstract is reasonably clear for a specialist audience but uses jargon (e.g., "Integrative Modeling Platform," "AlphaFold-enabled") that would be difficult for a nonspecialist to follow without context.

- **Recommendation posture** Currently not established from the provided evidence. The abstract presents an interesting premise, but the core claims are unsupported. The manuscript would need to provide substantial quantitative evidence, validation metrics, and a clear demonstration of novelty to be considered for a high-impact venue. A supportive recommendation would be contingent on the full manuscript addressing the major concerns outlined above.