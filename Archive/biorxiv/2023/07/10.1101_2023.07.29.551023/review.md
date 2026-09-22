## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as stated in the abstract; no methods, figures, or supplementary materials were provided
- **Shared manuscript claim summary** The authors use AlphaFold2 (AF2) and molecular dynamics (MD) simulations to model monomer and dimer structures of an intrinsically disordered protein (IDP), Nvjp-1. They report relatively rigid dimeric structures compared to monomers, coherent conformational trends across AF2 models and MD trajectories distinguishing IDPs from folded proteins, transient versus persistent residue-residue interactions, and consistent pLDDT score profiles across disordered and ordered proteins. They propose a protocol for justifying IDP predictions based on multiple AF2 models and MD simulations.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary data were provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, methods description, MD simulation parameters, AF2 model details, pLDDT score distributions, contact map definitions, and any statistical analyses

## Reviewer
- **Overall assessment** The abstract presents an interesting and potentially useful observation regarding the use of AF2 and MD simulations for IDP characterization. However, the claims as stated are broad and lack sufficient methodological detail to assess their validity. The central assertion that conformational variability across AF2 models and MD trajectories can distinguish IDPs from folded proteins is plausible but requires quantitative support. The observation of consistent pLDDT profiles across disordered and ordered proteins is counterintuitive given established literature and needs careful explanation. The proposed protocol is not described in sufficient detail to be evaluated or reproduced.
- **Who would be interested in the results, and why** Researchers working on intrinsically disordered proteins, computational structural biology, and protein structure prediction. The work could be of interest to those developing or applying AF2-based approaches to IDPs, a challenging class of proteins for structure prediction methods. The potential protocol for justifying IDP predictions may be useful for the broader structural biology community.
- **Major strengths** The topic is timely and relevant given the widespread adoption of AF2. The combination of AF2 and MD simulations is a sensible approach for studying IDPs. The comparison between disordered and ordered proteins is a useful framework. The observation of rigid dimeric structures in an IDP is potentially interesting.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
  - R1-M4
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
  - R1-m4
- **Technical failings that need to be addressed before the case is established** The lack of quantitative metrics for conformational variability, the absence of details on how pLDDT profiles were compared, the undefined criteria for "transient" versus "persistent" interactions, and the missing description of the proposed protocol are all technical gaps that prevent the claims from being evaluated.
- **Assessment against Nature-style criteria** 
  - Originality: Moderate. The combination of AF2 and MD for IDPs is not entirely new, but the specific comparison framework and the proposed protocol may offer some novelty.
  - Scientific importance: Moderate. IDP structure prediction is an active area, and any reliable approach would be valuable. However, the abstract does not demonstrate a clear advance over existing methods.
  - Interdisciplinary readership: Limited. The work is primarily of interest to computational structural biologists and IDP researchers.
  - Technical soundness: Not assessable from the abstract alone. Key methodological details are missing.
  - Readability for nonspecialists: The abstract is reasonably clear but uses technical terms without sufficient context for a general audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents interesting ideas but lacks the quantitative and methodological detail needed to assess the validity of the claims. A full manuscript review would be required to determine whether the case can be made.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "protein conformations from multiple AF2 models and those from MD trajectories exhibit a coherent trend: the conformations of an IDP are deviated from each other and the conformations of a well-folded protein are consistent with each other."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The claim of a "coherent trend" is presented without any quantitative measure of conformational variability. No metrics such as root-mean-square deviation (RMSD), radius of gyration, or other structural descriptors are mentioned. The comparison between IDP and folded protein conformations is not supported by any statistical analysis.
- **Why it matters** Without quantitative metrics, the reader cannot assess whether the observed differences are meaningful or within expected noise. The claim is central to the proposed protocol and must be rigorously supported.
- **Resolution test** Provide quantitative measures of conformational variability for both AF2 models and MD trajectories, with appropriate statistical comparisons between IDP and folded protein cases.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the AF2 models of both disordered and ordered proteins exhibit highly consistent profiles of the pLDDT scores."
- **Evidence pointer** Abstract only; location not provided
- **Concern** This claim is surprising given that pLDDT scores are widely reported to be lower for disordered regions. The abstract does not explain how "highly consistent profiles" are defined or quantified. If the profiles are consistent in shape but differ in absolute values, the claim is misleading. If they are consistent in absolute values, this contradicts established literature and requires a detailed explanation.
- **Why it matters** This observation, if true, would be a significant finding. However, as stated, it is ambiguous and potentially contradicts known behavior of AF2 on disordered proteins. The claim needs clarification and robust evidence.
- **Resolution test** Show the actual pLDDT profiles for both disordered and ordered proteins, define what "highly consistent" means quantitatively, and discuss how this relates to known AF2 behavior on IDPs.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "the residue-residue interactions in Nvjp-1 are mainly transient; however, those in a well-folded protein are mainly persistent."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The terms "transient" and "persistent" are not defined. No criteria are given for classifying interactions as one or the other. The contact map and RIN methodology are mentioned but not described. Without clear definitions and thresholds, this claim cannot be evaluated.
- **Why it matters** This distinction between transient and persistent interactions is a key part of the proposed protocol. Without operational definitions, the claim is not testable or reproducible.
- **Resolution test** Define the criteria for transient versus persistent interactions, describe the RIN construction and analysis, and provide quantitative evidence supporting the classification.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The authors propose "a potential protocol to justify the IDPs based on multiple AF2 models and MD simulations."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The protocol is not described. No details are given on how many AF2 models are needed, what MD simulation length is required, how the conformational analysis is performed, or how the results are interpreted. The protocol as stated is not reproducible.
- **Why it matters** A protocol must be described in sufficient detail to be implemented by others. Without this, the practical value of the work is limited.
- **Resolution test** Provide a step-by-step description of the protocol, including parameters, thresholds, and decision criteria.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract wording
- **Evidence pointer** Abstract; location not provided
- **Issue** The phrase "relatively rigid dimeric structures" is vague. It is unclear what "relatively rigid" means in quantitative terms.
- **Required correction** Provide quantitative measures of rigidity, such as RMSF or B-factors, and compare them between monomer and dimer states.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Abstract content
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract mentions a TOC figure but does not describe its content. This is an incomplete element.
- **Required correction** Either describe the TOC figure in the abstract or remove the reference to it.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Use of "justify"
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "justify" in the context of IDP prediction is unclear. It is not standard terminology in structural biology.
- **Required correction** Replace with a more precise term such as "validate," "assess," or "characterize."

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Context
- **Affected element** Background information
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract does not provide any context on why Nvjp-1 is of interest or what its biological function is.
- **Required correction** Add a brief statement on the biological relevance of Nvjp-1 to help readers understand the significance of the work.

## Risk / unsupported claims
- The claim of a "coherent trend" distinguishing IDP and folded protein conformations is unsupported without quantitative metrics.
- The claim of "highly consistent profiles" of pLDDT scores across disordered and ordered proteins is unsupported and potentially contradicts established literature.
- The classification of interactions as "transient" versus "persistent" is unsupported without defined criteria.
- The proposed protocol is not described and therefore cannot be evaluated.
- The observation of "relatively rigid dimeric structures" is unsupported without quantitative measures.
- The biological relevance of Nvjp-1 is not stated, limiting the assessment of the work's significance.