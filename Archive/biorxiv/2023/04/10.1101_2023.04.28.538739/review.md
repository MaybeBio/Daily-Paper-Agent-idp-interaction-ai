## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, or supplementary materials were provided
- **Shared manuscript claim summary** The authors propose a computational algorithm for designing intrinsically disordered protein regions (IDRs) by minimizing the distance of a random amino acid sequence to a known IDR in a high-dimensional space of molecular properties (repeat content, charge, hydrophobicity). They validate the approach by testing designed IDRs for mitochondrial targeting and heat-induced condensate formation, reporting that several showed expected patterns in cells.
- **Visible evidence base** Abstract text only; no experimental details, statistical analyses, or algorithmic specifications are available
- **Missing materials affecting confidence** Full methods, algorithm description, sequence design details, experimental protocols, imaging data, quantification, controls, and statistical tests are absent; the abstract provides no numerical results or effect sizes

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting approach to a challenging problem in protein design, namely the design of intrinsically disordered regions without stable 3D structures. The idea of matching bulk molecular properties in a high-dimensional space is plausible and could be of value to the protein engineering and cell biology communities. However, the abstract provides insufficient detail to evaluate the technical soundness of the algorithm, the robustness of the validation, or the generalizability of the approach. The claim that "several showed the expected patterns in cells" is vague and lacks quantitative support. The case for a broadly applicable design strategy is not established from the supplied material.
- **Who would be interested in the results, and why** Researchers in computational protein design, synthetic biology, and cell biology would be interested. Those working on intrinsically disordered proteins, subcellular targeting signals, and biomolecular condensates would find the approach potentially useful for generating synthetic IDRs with tailored functions. The method could also appeal to groups interested in sequence-to-property relationships in disordered regions.
- **Major strengths** The problem addressed is timely and important, as IDR design remains underexplored relative to structured protein design. The proposed strategy, based on matching bulk molecular properties rather than 3D structure, is conceptually simple and potentially general. The choice of two distinct functional targets, mitochondrial targeting and condensate formation, suggests an attempt to demonstrate versatility.
- **Major Concerns**  
  - **Concern ID** R1-M1  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Technical soundness  
  - **Claim pointer** The algorithm designs synthetic IDRs by minimizing the distance of an initially random amino acid sequence to a known IDR in a high-dimensional space of molecular properties.  
  - **Evidence pointer** Abstract; location not provided  
  - **Concern** The abstract does not describe the specific molecular properties used, the distance metric, the optimization procedure, or how the "known IDR" reference is selected. Without these details, the algorithm cannot be assessed for reproducibility, convergence, or bias.  
  - **Why it matters** A computational design method must be fully specified to be useful and credible. The absence of algorithmic details prevents evaluation of whether the method is novel, robust, or likely to generalize beyond the tested cases.  
  - **Resolution test** Provide a complete description of the property space, distance function, optimization algorithm, and reference IDR selection criteria, ideally with pseudocode or a code repository.  
  - **Concern ID** R1-M2  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Evidence strength  
  - **Claim pointer** Several designed IDRs showed the expected patterns in cells for mitochondrial targeting and heat-induced condensates.  
  - **Evidence pointer** Abstract; location not provided  
  - **Concern** The validation is described only qualitatively. No quantitative data, such as colocalization statistics, fluorescence intensity measurements, or fraction of cells showing the expected phenotype, are provided. The phrase "several showed" implies that not all designs worked, but the success rate and criteria for success are undefined.  
  - **Why it matters** Without quantitative validation and clear success criteria, the claim that the designs function as intended is not supported. The reader cannot judge the reliability or efficiency of the method.  
  - **Resolution test** Include quantitative results with appropriate statistical tests, define success criteria a priori, and report the number of designs tested and the fraction that passed.  
  - **Concern ID** R1-M3  
  - **Severity** Major  
  - **Blocking** No  
  - **Axis** Generalizability  
  - **Claim pointer** The strategy is described as "general" for design of intrinsically disordered regions.  
  - **Evidence pointer** Abstract; location not provided  
  - **Concern** Only two functional targets are tested, and the abstract does not indicate whether the algorithm was applied to a diverse set of IDR properties or functions. The generality of the approach is asserted but not demonstrated.  
  - **Why it matters** A general design strategy should be shown to work across a range of IDR types, property combinations, and cellular contexts. The current evidence is too limited to support the generality claim.  
  - **Resolution test** Apply the algorithm to additional IDR targets with distinct functional requirements and report success rates and limitations.

- **Minor Comments**  
  - **Concern ID** R1-m1  
  - **Severity** Minor  
  - **Axis** Clarity  
  - **Affected element** Abstract wording  
  - **Evidence pointer** Abstract; location not provided  
  - **Issue** The phrase "minimizing the distance of an initially random amino acid sequence to a known IDR" is ambiguous regarding whether the reference IDR is a single sequence or a distribution of sequences.  
  - **Required correction** Clarify whether the target is a specific sequence or a property distribution derived from a set of known IDRs.  
  - **Concern ID** R1-m2  
  - **Severity** Minor  
  - **Axis** Completeness  
  - **Affected element** Abstract scope  
  - **Evidence pointer** Abstract; location not provided  
  - **Issue** The abstract does not mention any negative controls or tests of specificity, such as whether designed sequences with mismatched properties fail to show the expected patterns.  
  - **Required correction** Add a statement about controls or indicate where they are described in the full manuscript.  
  - **Concern ID** R1-m3  
  - **Severity** Minor  
  - **Axis** Reproducibility  
  - **Affected element** Algorithm availability  
  - **Evidence pointer** Abstract; location not provided  
  - **Issue** No mention is made of code or data availability, which is important for a computational method.  
  - **Required correction** State whether the algorithm and design scripts will be made publicly available.

## Risk / unsupported claims
- The claim that the algorithm is "general" for IDR design is unsupported given only two functional targets are mentioned.
- The claim that "several showed the expected patterns in cells" is unsupported without quantitative data or defined success criteria.
- The specific molecular properties listed (repeat content, charge, hydrophobicity) are asserted as the design space, but their sufficiency for functional IDR design is not demonstrated.
- The performance of the algorithm relative to existing IDR design methods cannot be assessed from the abstract.

## Assessment against Nature-style criteria
- **Originality** The approach of designing IDRs by matching bulk molecular properties rather than structure is a reasonable conceptual contribution, though the abstract does not clarify how it differs from prior sequence optimization methods for disordered regions. Originality is plausible but not fully established.
- **Scientific importance** The problem of IDR design is significant for synthetic biology and understanding sequence-function relationships in disordered proteins. If the method proves robust, it could have broad utility. However, the current evidence is too preliminary to assess importance.
- **Interdisciplinary readership** The topic bridges computational biology, protein engineering, and cell biology, and the abstract is written in a way that is accessible to nonspecialists. The potential readership is broad.
- **Technical soundness** Not assessable from the abstract. The algorithm is underspecified, and the validation lacks quantitative detail. This is the primary weakness.
- **Readability for nonspecialists** The abstract is clear and concise, with minimal jargon. The one-sentence summary is effective.

## Recommendation posture
Currently not established from the provided evidence. The conceptual idea is interesting, and the work could be suitable for a high-impact venue if the full manuscript provides a complete algorithmic description, rigorous quantitative validation, and evidence of generalizability. I would be supportive if these technical concerns are resolved in the full manuscript.