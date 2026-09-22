## Review setup

- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors report an in silico analysis of conserved RxLR effectors (CREs) across five Phytophthora species, identifying a subset that combines WY domains with embedded short linear motifs (SLiMs). They further characterize one representative effector, PpRxLR6 from Phytophthora nicotianae, using Agrobacterium-mediated transient expression assays and structural predictions, concluding that SLiM-mediated interactions can occur within structured WY-like domains and that this architecture may represent an adaptive strategy enhancing effector versatility.
- **Visible evidence base** Abstract text only; no experimental details, statistical analyses, structural prediction parameters, or assay readouts are available
- **Missing materials affecting confidence** Full manuscript, all figures and tables, methods section, structural prediction outputs, experimental replicates and controls, sequence alignment data, and any statistical analyses

## Reviewer

- **Overall assessment** The abstract presents a potentially interesting observation regarding the coexistence of SLiMs within structured WY domains of conserved RxLR effectors. However, the evidence base available for review is limited to the abstract, which precludes verification of the central claims. The functional characterization of PpRxLR6 is described only in general terms, and the structural predictions are not accompanied by any metrics of confidence. The conceptual advance over existing literature is not clearly delineated. The manuscript may have merit, but the case as presented is not fully established from the supplied material.
- **Who would be interested in the results, and why** Researchers studying oomycete plant pathogens, effector biology, host-pathogen interactions, and plant innate immunity would find these results relevant. The potential demonstration that SLiMs can function within structured domains rather than exclusively in intrinsically disordered regions could also interest structural biologists and molecular evolution researchers focused on protein interaction modules.
- **Major strengths** The abstract addresses a timely and important question in effector biology, namely the structural basis of conserved RxLR effector function. The focus on WY domains and SLiMs is a specific and mechanistically meaningful angle. The inclusion of a representative functional characterization, albeit briefly described, adds a translational component to the computational analysis.
- **Major Concerns** The following concerns are identified from the abstract alone. Several are marked as blocking because the current evidence base cannot support the stated conclusions.
- **Minor Comments** The abstract would benefit from clearer articulation of what is genuinely novel relative to prior work on WY domains and SLiMs. The phrase "previously recognized architectural feature" suggests prior knowledge, yet the novelty claim is not sharply defined. Also, the abstract does not specify which five Phytophthora species were analyzed, which would help readers assess the breadth of the claim.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** Originality: The concept of SLiMs within structured WY domains is not entirely new, as the abstract itself acknowledges prior recognition of this architectural feature. The specific claim that SLiM-mediated interactions may occur within structured domains is interesting but requires stronger evidence to be considered a significant advance. Scientific importance: The topic is important for understanding effector evolution and host manipulation, but the abstract does not demonstrate a major conceptual leap. Interdisciplinary readership: The work sits at the interface of structural biology, plant pathology, and molecular evolution, which could attract a broad audience if the evidence is robust. Technical soundness: Cannot be assessed from the abstract alone; no methodological details or validation metrics are provided. Readability for nonspecialists: The abstract is reasonably clear but uses field-specific terminology without sufficient context for a general scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract describes a plausible and potentially valuable study, but the absence of methodological detail, structural prediction confidence metrics, and functional assay specifics prevents verification of the central claims. A full manuscript review would be required to determine whether the technical concerns can be resolved.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "SLiM-mediated interactions may occur within structured effector domains rather than being confined to intrinsically disordered regions" based on structural predictions of PpRxLR6.
- **Evidence pointer** Abstract; location not provided
- **Concern** The structural prediction is described only as revealing that PpRxLR6 "harbors its SLiM within a well-ordered WY-like helical core region." No details are given regarding the prediction method, confidence scores, or validation against experimental structures. The claim that SLiM-mediated interactions can occur within structured domains is a strong mechanistic statement that requires robust structural evidence.
- **Why it matters** The central conceptual contribution of the abstract rests on this structural claim. If the prediction is low-confidence or ambiguous, the conclusion that structured WY domains can serve as scaffolds for SLiM interactions is not supported.
- **Resolution test** Provide the structural prediction method, confidence metrics (e.g., pLDDT scores, template modeling scores), and ideally experimental validation such as mutagenesis or binding assays demonstrating that the SLiM within the structured domain is accessible and functional for interactions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors state that PpRxLR6 "activates key immune defense networks in Nicotiana and Solanum species" based on Agrobacterium-mediated transient expression assays.
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract provides no information on the specific assays used, the readouts measured, the magnitude of immune activation, or the statistical significance of the results. Without these details, it is impossible to evaluate whether the observed effects are robust, specific, or biologically meaningful.
- **Why it matters** The functional characterization is a key component of the study, linking the structural observations to a biological role. If the immune activation is weak, non-specific, or not statistically validated, the functional claim is not established.
- **Resolution test** Describe the assays (e.g., reactive oxygen species burst, defense gene expression, cell death), include quantitative data with appropriate statistical tests, and show appropriate controls including empty vector and known positive or negative controls.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that the identified WY-SLiM architecture "may represent an adaptive strategy in Phytophthora evolution, potentially enhancing effector versatility in host interactions."
- **Evidence pointer** Abstract; location not provided
- **Concern** This evolutionary claim is presented as a conclusion but is not supported by any comparative or phylogenetic analysis described in the abstract. No data are shown regarding the distribution of WY-SLiM effectors across species, their evolutionary rates, or evidence of positive selection.
- **Why it matters** The evolutionary interpretation is a major framing of the study's significance. Without explicit evolutionary analyses, this claim is speculative and not evidence-based.
- **Resolution test** Provide comparative genomic or phylogenetic analyses demonstrating that WY-SLiM architecture is conserved or under selection across Phytophthora species, and discuss alternative explanations for the observed patterns.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors state that the in silico analysis "revealing a conserved subset that integrates WY domains with embedded short linear motifs" across five Phytophthora species.
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract does not specify the number of effectors analyzed, the criteria for defining conservation, the methods used to identify SLiMs, or the statistical significance of the enrichment. The claim of a "conserved subset" is central to the study but cannot be evaluated without these details.
- **Why it matters** The identification of a conserved WY-SLiM subset is the foundation of the entire study. If the bioinformatic methods are not robust or the conservation criteria are arbitrary, the subsequent structural and functional claims lose their context.
- **Resolution test** Provide details on the effector datasets, sequence search and alignment methods, SLiM prediction tools and thresholds, and a clear definition of conservation with supporting statistics.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Novelty claim
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract acknowledges that WY domains with embedded SLiMs are a "previously recognized architectural feature," yet the novelty of the current study is not clearly articulated. It is unclear what new insight is being added beyond prior recognition.
- **Required correction** Clarify in the abstract what specific aspect of the WY-SLiM architecture is newly discovered or newly characterized, such as the demonstration of functional immune activation or the structural prediction of SLiM accessibility within a folded domain.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Species list
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract refers to "five agriculturally significant Phytophthora species" but does not name them. This omission limits the reader's ability to assess the breadth and relevance of the comparative analysis.
- **Required correction** List the five Phytophthora species in the abstract or provide a reference to a table or figure where they are specified.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Precision
- **Affected element** Terminology
- **Evidence pointer** Abstract; location not provided
- **Issue** The phrase "key immune defense networks" is vague. It is not clear which specific pathways or components are meant, nor how they were measured.
- **Required correction** Specify the immune responses measured, such as specific defense genes, hormone signaling pathways, or cell death markers, to provide a concrete description of the observed effects.

## Risk / unsupported claims

- The claim that SLiM-mediated interactions occur within structured WY domains is unsupported without structural prediction confidence metrics or experimental validation.
- The claim that PpRxLR6 activates key immune defense networks is unsupported without assay details and statistical evidence.
- The claim that the WY-SLiM architecture represents an adaptive evolutionary strategy is unsupported without comparative or phylogenetic analyses.
- The claim of a conserved WY-SLiM subset across five species is unsupported without bioinformatic details and conservation criteria.
- The overall conclusion that this architecture "may represent an adaptive strategy" is speculative and not testable from the abstract alone.