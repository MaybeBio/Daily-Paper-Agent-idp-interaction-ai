## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, methods, and supplementary figure/table references as provided)
- **Assessment boundary** Scientific claims, methodological soundness, and evidence quality as presented in the provided text; no external data or unpublished materials were consulted
- **Shared manuscript claim summary** The authors propose that PP2A-B55 substrate recognition is mediated by α-helical binding elements that engage conserved hydrophobic and electrostatic patches on the B55 regulatory subunit, and that this mechanism is evolutionarily conserved. They further claim that a designed peptide inhibitor (B55i) can competitively block these interactions and that PP2A-B55 regulates the nuclear exosome targeting (NEXT) complex via a helical recruitment module in RBM7.
- **Visible evidence base** Abstract, introduction, results sections (narrative only), methods (partial), figure legends referenced but not shown, supplementary figure/table references, author contributions, acknowledgements
- **Missing materials affecting confidence** All figures and supplementary figures/tables are referenced but not provided; detailed numerical data (e.g., Kd values, statistical outputs, mass spectrometry quantification) are absent; full methods for AlphaFold modelling, mutagenesis scans, and inhibitor design are incomplete; no raw data or reproducibility details are available

## Reviewer
- **Overall assessment** The manuscript addresses a significant gap in understanding PP2A-B55 substrate recognition and presents a compelling conceptual framework supported by a combination of computational modelling and experimental validation. The central claim that α-helical elements, rather than short linear motifs, mediate substrate binding to B55 is novel and potentially field-changing. However, the evidence base as provided is insufficient to fully evaluate the robustness of the conclusions. Key figures, quantitative data, and methodological details are missing, which limits the ability to assess technical soundness and reproducibility. The biological validation in the RBM7/NEXT context is promising but incomplete, with functional outcomes not fully demonstrated.
- **Who would be interested in the results, and why** Cell cycle researchers, phospho-signaling biologists, and structural biologists studying protein phosphatase specificity would find this work highly relevant. The proposed mechanism of α-helical recruitment could inform studies on PP2A-B55 function in mitosis, DNA damage responses, and RNA metabolism. Additionally, the engineered peptide inhibitor has potential utility as a research tool and therapeutic lead, appealing to chemical biologists and drug discovery groups. The evolutionary conservation claim broadens interest to comparative genomics and evolutionary biology audiences.
- **Major strengths** The integration of AlphaFold2 modelling with high-resolution mutational scanning is a powerful and modern approach. The identification of a conserved binding mechanism across diverse substrates, including yeast, human, and viral proteins, is conceptually important. The design of a specific peptide inhibitor using deep learning methods is innovative and provides a practical tool. The validation in a physiologically relevant context (NEXT complex) adds functional significance.
- **Major Concerns** The absence of all figures and supplementary data is a critical limitation. The claim of "comprehensive" mutational scanning is not substantiated without the actual data. The functional significance of the RBM7 interaction is inferred but not directly tested (e.g., no rescue experiments or phenotypic assays). The inhibitor's specificity is only partially demonstrated; off-target effects on other PP2A-B55 substrates or related phosphatases are not addressed. The evolutionary conservation claim relies on a limited set of examples and lacks phylogenetic depth.
- **Technical failings that need to be addressed before the case is established** The manuscript cannot be fully assessed without the figures and supplementary materials. The methods for AlphaFold modelling and inhibitor design are incomplete, preventing replication. The mass spectrometry data for global interactor dependencies are not shown, and statistical details are missing. The Kd values for B55i are reported but the experimental conditions and replicates are not fully described.
- **Assessment against Nature-style criteria** Originality: High. The α-helical binding paradigm for PP2A-B55 is a novel contribution that challenges the prevailing SLiM-centric view. Scientific importance: High. PP2A-B55 regulates numerous pathways, and understanding substrate recognition has broad implications. Interdisciplinary readership: Moderate to high. The work bridges structural biology, cell signaling, and protein engineering, but the current presentation may be too specialized for a general audience. Technical soundness: Not fully assessable due to missing data; the approach is sound in principle but requires verification. Readability for nonspecialists: The narrative is clear but relies heavily on jargon and assumes familiarity with phosphatase biology; the abstract is accessible but the results section is dense.
- **Recommendation posture** Supportive if technical concerns are resolved and all missing data are provided. The conceptual advance is significant, but the current evidence base is insufficient to establish the claims without full access to figures, quantitative data, and complete methods.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The authors claim "comprehensive high resolution mutational scanning" and "experimental validation" of 19 predicted binding elements, but no figures or data are provided to support this.
- **Evidence pointer** Results section, Figure 1, Figures S1-S10, Supplemental Tables 1-2 (all referenced but not provided)
- **Concern** The manuscript relies entirely on figures and supplementary materials that are not included in the provided text. Without these, the mutational scanning results, the AlphaFold model quality metrics, and the validation data cannot be evaluated. The claim of "comprehensive" scanning is unverifiable.
- **Why it matters** The central conclusion that α-helices engage specific patches on B55 depends on the quality and completeness of the mutational data. If the scanning is not truly comprehensive or the validation is incomplete, the proposed binding principles may be overstated.
- **Resolution test** Provide all figures and supplementary data, including mutational scan heatmaps, AlphaFold confidence scores, and validation blots. Ensure that the number of mutants tested per protein and the criteria for "validated" are clearly stated.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Functional validation
- **Claim pointer** The authors state that PP2A-B55 regulates the NEXT complex by binding a helical domain in RBM7, and that this is important for RNA metabolism.
- **Evidence pointer** Results section, Figure 4, Figure S16 (referenced but not provided)
- **Concern** The functional significance of the RBM7-PP2A-B55 interaction is inferred from binding assays and RNA level changes, but no direct functional experiments are shown. The claim that PP2A-B55 regulates NEXT complex function is not supported by rescue experiments, knockdown/knockout phenotypes, or direct measurement of exosome activity.
- **Why it matters** The manuscript aims to establish a biological role for the identified binding mechanism. Without functional validation, the physiological relevance of the RBM7 interaction remains speculative.
- **Resolution test** Include experiments showing that disruption of the RBM7-PP2A-B55 interaction (e.g., via RBM7 R143A or B55i) leads to measurable defects in NEXT-dependent RNA decay, and that these defects can be rescued by restoring the interaction.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Inhibitor specificity
- **Claim pointer** The authors claim that B55i is a "specific and potent" inhibitor of PP2A-B55 substrate interactions.
- **Evidence pointer** Results section, Figure 3, Figure S14 (referenced but not provided)
- **Concern** The specificity of B55i is only demonstrated against a limited set of PP2A-B55 interactors. It is unclear whether B55i affects other PP2A holoenzymes (e.g., B56-containing complexes) or other phosphatases. The Kd values from SPR and FP differ by an order of magnitude, which is not explained.
- **Why it matters** A specific inhibitor is a key tool for dissecting PP2A-B55 function. If B55i has off-target effects, conclusions drawn from its use in cellular assays would be compromised.
- **Resolution test** Test B55i against a panel of related phosphatases and PP2A holoenzymes. Provide a reconciliation of the SPR and FP Kd values, and include a discussion of potential off-target effects.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Evolutionary conservation
- **Claim pointer** The authors claim the α-helical binding mechanism is "evolutionary conserved" based on examples from yeast, humans, and viruses.
- **Evidence pointer** Results section, Figure S11 (referenced but not provided)
- **Concern** The evolutionary claim is based on a limited set of examples spanning "close to a billion years," but the phylogenetic sampling is not described. It is unclear whether the conservation is sequence-based, structural, or functional, and whether the mechanism is truly universal across eukaryotes.
- **Why it matters** The claim of evolutionary conservation strengthens the generalizability of the findings. If the sampling is biased or the conservation is only superficial, the conclusion may be overreaching.
- **Resolution test** Provide a phylogenetic analysis of B55-binding α-helices across a diverse set of eukaryotes, and clarify the criteria for conservation (e.g., structural similarity vs. sequence identity).

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, "One sentence summary"
- **Issue** The one-sentence summary is grammatically awkward and redundant with the abstract's final sentence.
- **Required correction** Revise the summary for clarity, e.g., "α-Helical motifs in substrates bind a conserved pocket on B55 via a mechanism conserved across eukaryotes."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Methods, "Computational methods Screen of binders"
- **Evidence pointer** Methods section
- **Issue** The description of the AlphaFold2 screening is incomplete. The parameters for "iPAE< 10 and average interface pLDDT > 70" are stated, but the rationale for these cutoffs and the handling of borderline cases are not explained.
- **Required correction** Provide a justification for the confidence thresholds and describe how models that did not meet the criteria were treated.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Results, "A conserved pocket on the B55 subunit binds α helices in interactors"
- **Evidence pointer** Results section, Figure 1
- **Issue** The text mentions "hydrophobic and electrostatic patches" but does not specify which residues constitute each patch beyond a partial list for patch 1. The patch definitions are not consistently applied across all binders.
- **Required correction** Clearly define the residues for each patch and state whether the same residues are used by all binders or if there is variability.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Methods, "Mass spectrometry"
- **Evidence pointer** Methods section
- **Issue** The statistical analysis is described as a "two-tailed Student's t-test," but the number of replicates, the correction for multiple testing, and the criteria for significance are not stated.
- **Required correction** Specify the number of biological and technical replicates, the multiple testing correction method, and the significance threshold.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Results, "Generation of an engineered B55 inhibitor blocking binding of helical elements"
- **Evidence pointer** Results section, Figure 3
- **Issue** The term "inhibitor" is used for B55i, but the mechanism is competitive displacement of substrates, not direct inhibition of phosphatase activity. This distinction should be clarified.
- **Required correction** Use "competitive peptide inhibitor" or "substrate-competitive inhibitor" throughout to avoid ambiguity.

## Risk / unsupported claims
- The claim of "comprehensive high resolution mutational scanning" is unsupported without the actual data.
- The functional role of PP2A-B55 in regulating NEXT complex function is not directly demonstrated; only correlative evidence is presented.
- The evolutionary conservation claim is not substantiated with a rigorous phylogenetic analysis.
- The specificity of B55i is not fully established; off-target effects on other PP2A complexes or phosphatases are not ruled out.
- The Kd values for B55i from SPR and FP are inconsistent and not reconciled, raising questions about the accuracy of the affinity measurements.
- The claim that α-helical binding is a "novel mechanism" for PPP substrate recognition is plausible but requires comparison with existing SLiM-based models to be fully contextualized.