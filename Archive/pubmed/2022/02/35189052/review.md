## Review setup
- **Input scope** Full manuscript text as provided
- **Assessment boundary** Scientific claims, evidence quality, and internal consistency of the supplied text only
- **Shared manuscript claim summary** The authors argue that AlphaFold's protein structure predictions are unreliable for disordered regions and membrane proteins, and propose a new concept termed "epigenetic dimension of protein structure" to account for structural determinants not encoded in the amino acid sequence.
- **Visible evidence base** The provided text contains no figures, tables, methods, or data. It is a short opinion-style piece with qualitative assertions.
- **Missing materials affecting confidence** No methods, datasets, structural comparisons, quantitative metrics, or literature citations are provided. The manuscript appears to be a perspective or commentary, but the absence of supporting references and technical details limits verification.

## Reviewer
- **Overall assessment** The manuscript presents a provocative but underdeveloped argument. The core claim that AlphaFold models contain serious flaws in disordered and membrane protein regions is plausible but unsupported by any concrete examples or systematic analysis. The proposed concept of an "epigenetic dimension of protein structure" is interesting but vaguely defined and overlaps with existing terminology in structural biology. The text reads as an opinion piece rather than a scientific study, and the evidence base is insufficient to establish the case.
- **Who would be interested in the results, and why** Structural biologists, computational biologists, and researchers using AlphaFold for protein structure prediction would find the critique relevant. The proposed concept may interest those studying protein disorder, membrane protein folding, and the limits of sequence-based prediction. However, the lack of data limits its utility for these audiences.
- **Major strengths** The manuscript addresses a timely and important topic, namely the limitations of AlphaFold. The writing is clear and accessible. The proposal to distinguish sequence-encoded features from other structural determinants is conceptually useful and could stimulate discussion.
- **Major Concerns** The manuscript lacks any empirical evidence or detailed case studies to support the claim of "serious flaws" in AlphaFold models. The definition of "epigenetic dimension" is ambiguous and not operationalized. The exclusion of post-translational modifications from the concept is arbitrary and not justified. The text does not engage with existing literature on protein structure prediction limitations or alternative frameworks.
- **Minor Comments** The phrase "triumphal statement" is editorializing and could be softened. The comparison to the human genome sequencing is not substantiated. The final sentence about "uncertainty and anarchy" is rhetorical and lacks scientific precision.
- **Technical failings that need to be addressed before the case is established** No quantitative or qualitative evidence is provided for the claimed AlphaFold failures. No examples of specific proteins or structures are given. No criteria are defined for what constitutes an "unrealistic structure." The concept of "epigenetic dimension" is not defined with sufficient precision to be testable.
- **Assessment against Nature-style criteria** Originality: The concept is somewhat novel but not clearly distinguished from existing ideas about protein dynamics and environment-dependent folding. Scientific importance: The topic is important, but the manuscript does not provide new data or a rigorous framework. Interdisciplinary readership: The text is accessible but lacks depth for specialists. Technical soundness: Not applicable, as no technical analysis is presented. Readability for nonspecialists: The writing is clear, but the lack of evidence makes it unconvincing.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript would require substantial revision, including concrete examples, a systematic analysis of AlphaFold failures, and a clearer definition of the proposed concept, before it could be considered for publication.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors claim that "we identified serious flaws in some AlphaFold models" and that disordered regions are "often represented by large loops that clash with the overall protein geometry."
- **Evidence pointer** Location not provided
- **Concern** The claim of serious flaws is made without presenting any specific examples, structural comparisons, or quantitative analysis. No proteins are named, no figures are shown, and no metrics are given to support the assertion.
- **Why it matters** Without concrete evidence, the central critique of AlphaFold is unverifiable and could be dismissed as anecdotal. The scientific community requires reproducible examples to evaluate the validity of such a strong claim.
- **Resolution test** Provide at least two or three specific protein examples with AlphaFold predictions compared to experimental structures, including quantitative measures of clash or geometric distortion.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Conceptual clarity
- **Claim pointer** The authors propose to coin "epigenetic dimension of protein structure" for "all parameters controlling the structure of a protein without being strictly encoded in its amino acid sequence."
- **Evidence pointer** Location not provided
- **Concern** The definition is too broad and vague. It includes solvation by membrane lipids and ligand-induced structuration but excludes post-translational modifications. The rationale for these inclusions and exclusions is not explained, and the term "epigenetic" is used metaphorically without a clear mechanistic link to epigenetics.
- **Why it matters** A new scientific concept must be precisely defined to be useful. As stated, the concept could encompass almost any environmental or cellular factor, making it unfalsifiable and of limited practical value.
- **Resolution test** Provide a formal definition with explicit criteria for what counts as "epigenetic" in this context, and justify the exclusion of post-translational modifications with specific examples or reasoning.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Literature engagement
- **Claim pointer** The manuscript implies that AlphaFold's limitations are not widely recognized and that the "epigenetic dimension" is a novel paradigm.
- **Evidence pointer** Location not provided
- **Concern** The text does not cite any prior work on AlphaFold limitations, protein disorder prediction, or environment-dependent folding. This omission makes it impossible to assess the novelty of the claims or the proposed concept.
- **Why it matters** Scientific claims must be situated in the existing literature. Without references, the manuscript cannot demonstrate that the issue is underappreciated or that the proposed concept adds value beyond known frameworks.
- **Resolution test** Add a literature review section citing relevant studies on AlphaFold accuracy, membrane protein prediction, and protein disorder, and explicitly state how the proposed concept differs from existing ideas.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Tone
- **Affected element** Introduction
- **Evidence pointer** Location not provided
- **Issue** The phrase "triumphal statement" and the comparison to the human genome sequencing are editorial and not supported by evidence.
- **Required correction** Rephrase to a neutral description of AlphaFold's achievements and claims, and remove or substantiate the genome sequencing comparison.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Precision
- **Affected element** Definition of "epigenetic dimension"
- **Evidence pointer** Location not provided
- **Issue** The term "epigenetic" is used without defining its relationship to the established meaning in molecular biology, which may confuse readers.
- **Required correction** Clarify whether the term is used metaphorically or literally, and provide a brief justification for its use.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Conclusion
- **Evidence pointer** Location not provided
- **Issue** The final sentence about "uncertainty and anarchy" is vague and does not follow logically from the preceding argument.
- **Required correction** Replace with a concrete statement about the implications of the proposed concept for protein structure prediction or biology.

## Risk / unsupported claims
- The claim that AlphaFold produces "serious flaws" in disordered and membrane protein regions is unsupported by any data or examples.
- The assertion that AlphaFold "comes up against" the notion that folding is not solely determined by genomic information is presented as fact without evidence.
- The proposed "epigenetic dimension of protein structure" is not defined with sufficient precision to be evaluated or tested.
- The exclusion of post-translational modifications from the concept is arbitrary and unjustified.
- The comparison of AlphaFold to the human genome sequencing is unsupported and likely overstated.