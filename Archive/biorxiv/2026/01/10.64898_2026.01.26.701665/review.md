## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors propose DMG-PPI, a dual-channel graph neural network framework that jointly models similarity-driven and complementarity-driven protein-protein interactions via two parallel message-passing pathways (AMP and DMP), integrates these signals through adaptive fusion and MixHop-based aggregation, reports a 7.19% Micro-F1 improvement over the second-best method on benchmark datasets, and claims interpretable insights into key binding residues and interfacial mechanisms
- **Visible evidence base** Abstract text only; no quantitative results beyond the single Micro-F1 improvement figure, no dataset names, no baseline details, no statistical significance measures, no interpretability validation
- **Missing materials affecting confidence** Full manuscript, methods section, experimental setup, dataset descriptions, baseline specifications, hyperparameter details, ablation studies, interpretability analyses, code availability, and all figures and tables

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting dual-channel framework for PPI prediction that explicitly distinguishes similarity-based and complementarity-based interaction mechanisms. The idea of disentangling these two modes within a unified graph neural network architecture is timely and potentially valuable for the structural biology and machine learning communities. However, the evidence provided in the abstract is insufficient to evaluate the technical soundness of the approach, the validity of the performance claims, or the biological interpretability assertions. The single performance metric reported lacks context, and no methodological details are available to assess novelty relative to existing heterophilous GNN literature. The interpretability claims are particularly difficult to evaluate without any supporting analysis or validation.
- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on PPI prediction would be the primary audience, as the framework directly targets a core problem in their field. Machine learning researchers interested in graph neural networks, particularly those working on heterophily and multi-channel message passing, would also find the architectural contributions relevant. Structural biologists studying protein binding mechanisms and interfacial recognition principles may be interested in the interpretability aspects, provided the claims are substantiated with rigorous validation.
- **Major strengths** The conceptual framing of PPI interactions as governed by two distinct mechanisms (similarity and complementarity) is biologically motivated and provides a clear rationale for the architectural design. The dual-channel approach with separate message-passing pathways is a principled way to address interaction heterogeneity. The claim of interpretable insights into binding residues, if substantiated, would add practical value beyond predictive performance.
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
- **Technical failings that need to be addressed before the case is established** R1-M1 (performance claim lacks context and statistical validation), R1-M2 (novelty relative to prior heterophilous GNN work is not established), R1-M3 (interpretability claims are unsupported), R1-M4 (methodological details are entirely absent)
- **Assessment against Nature-style criteria** Originality: The dual-channel conceptualization of PPI interaction modes is a potentially original contribution, but the abstract does not provide enough detail to distinguish it from existing heterophilous GNN approaches. Scientific importance: PPI prediction is a high-impact problem, and the biological interpretability angle adds potential significance, but the importance hinges on the validity of the performance and interpretability claims, which cannot be assessed from the abstract alone. Interdisciplinary readership: The work bridges machine learning and structural biology, which could attract a broad readership, but the abstract assumes familiarity with GNN terminology that may limit accessibility. Technical soundness: Cannot be evaluated from the abstract; no architectural details, experimental protocols, or statistical analyses are provided. Readability for nonspecialists: The abstract is reasonably clear for a technical audience but uses specialized terminology without sufficient explanation for a general scientific readership.
- **Recommendation posture** Currently not established from the provided evidence. The conceptual framework is promising, but the abstract alone does not provide sufficient evidence to support the performance, novelty, or interpretability claims. A full manuscript with detailed methods, comprehensive experiments, and rigorous validation would be required to assess whether the case can be established.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Performance claim validity
- **Claim pointer** The abstract claims that DMG-PPI "substantially outperforms state-of-the-art methods on classical benchmark datasets, achieving a 7.19% improvement in Micro-F1 over the second-best method."
- **Evidence pointer** Abstract only; no dataset names, baseline methods, or experimental details provided
- **Concern** The single performance metric reported (7.19% Micro-F1 improvement) is presented without essential context. The abstract does not specify which benchmark datasets were used, which state-of-the-art methods were compared, how many runs were performed, whether the improvement is statistically significant, or what the absolute performance values were. A 7.19% relative improvement could be meaningful or negligible depending on the baseline performance level and the variance across runs.
- **Why it matters** The central claim of the paper is that DMG-PPI outperforms existing methods. Without knowing the experimental setup, the comparison baselines, and the statistical significance of the reported improvement, this claim cannot be evaluated. Overstated performance claims in the absence of rigorous statistical validation are a common source of irreproducibility in machine learning research.
- **Resolution test** Provide the full experimental section including dataset descriptions, baseline implementations, hyperparameter settings, multiple random seeds with standard deviations, and statistical significance tests (e.g., paired t-tests or Wilcoxon signed-rank tests) comparing DMG-PPI against each baseline on each dataset.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Novelty and positioning
- **Claim pointer** The abstract states that DMG-PPI "extends prior heterophilous GNN concepts to explicitly disentangle these dual interaction modes."
- **Evidence pointer** Abstract only; no related work discussion or comparison with specific prior methods provided
- **Concern** The abstract acknowledges that heterophilous GNN concepts exist but does not specify which prior methods are being extended, what their limitations are, or how DMG-PPI differs architecturally from them. The distinction between "extending" and "incrementally modifying" existing approaches is unclear. Without a clear articulation of the technical novelty relative to the closest prior work, the contribution may be perceived as incremental.
- **Why it matters** For a Nature-style audience, establishing clear novelty relative to the state of the art is essential. If the dual-channel architecture is a straightforward combination of existing heterophilous GNN techniques, the scientific contribution would be substantially diminished. The abstract must clearly delineate what is genuinely new.
- **Resolution test** Provide a detailed related work section that identifies the closest prior heterophilous GNN methods, articulates their specific limitations for PPI modeling, and explains with architectural diagrams and mathematical formulations how DMG-PPI's AMP and DMP pathways differ from and improve upon these methods.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretability claim validity
- **Claim pointer** The abstract claims that "the dual-channel framework provides interpretable insights into key binding residues by identifying interfacial mechanisms."
- **Evidence pointer** Abstract only; no interpretability analysis, case studies, or validation against known binding site annotations provided
- **Concern** The interpretability claim is made without any supporting evidence. The abstract does not describe how interpretability is extracted from the model, whether the identified residues are validated against experimental data or known binding site annotations, or whether the "interfacial mechanisms" identified by AMP and DMP correspond to biologically meaningful distinctions. Interpretability claims in deep learning are frequently overstated and require rigorous validation.
- **Why it matters** The interpretability aspect is presented as a key added value of the framework beyond predictive performance. If the identified residues and mechanisms are not validated against ground truth biological data, the claim is speculative. For a biology-oriented audience, unvalidated interpretability claims could mislead downstream applications.
- **Resolution test** Provide a dedicated interpretability section with quantitative validation (e.g., overlap with known binding site annotations, comparison with experimental mutagenesis data, or structural validation using co-crystal structures) and qualitative case studies demonstrating that AMP and DMP identify distinct and biologically meaningful interaction modes.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological reproducibility
- **Claim pointer** The abstract describes the model architecture at a high level, including AMP, DMP, adaptive fusion, and MixHop aggregation.
- **Evidence pointer** Abstract only; no architectural details, mathematical formulations, or implementation specifics provided
- **Concern** The abstract provides only a high-level description of the model components without any mathematical formulations, hyperparameter choices, training procedures, or implementation details. The adaptive fusion strategy and the integration with MixHop are mentioned but not specified. Reproducing the reported results would be impossible from the abstract alone.
- **Why it matters** Reproducibility is a fundamental requirement for scientific claims. Without detailed methodological descriptions, the reported performance improvement cannot be independently verified, and the community cannot build upon the proposed approach. This is particularly critical for a methodological contribution.
- **Resolution test** Provide a complete methods section with formal mathematical definitions of AMP and DMP message-passing operations, the adaptive fusion mechanism, the MixHop integration, training details (optimizer, learning rate, epochs, batch size), hyperparameter values, and code availability.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** Abstract terminology
- **Evidence pointer** Abstract, first paragraph
- **Issue** The terms "similarity-driven" and "complementarity-driven" are introduced as fundamental interaction mechanisms, but the abstract does not define these concepts precisely. The relationship between "similarity" and "symmetric structural motifs" and between "complementarity" and "geometric and physicochemical matching" is stated but not elaborated.
- **Required correction** Provide brief definitions or examples of similarity-driven and complementarity-driven interactions in the introduction to ensure readers understand the biological basis for the architectural design.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Dataset specification
- **Affected element** Performance claim
- **Evidence pointer** Abstract, results statement
- **Issue** The abstract refers to "classical benchmark datasets" without naming them. Different PPI benchmark datasets have different characteristics (e.g., species, interaction types, sparsity), and the choice of datasets significantly affects the interpretation of results.
- **Required correction** Name the specific benchmark datasets used in the abstract or at minimum in the results section of the full manuscript.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Baseline comparison scope
- **Affected element** Performance comparison
- **Evidence pointer** Abstract, results statement
- **Issue** The abstract mentions "state-of-the-art methods" without specifying which methods were compared. The choice of baselines substantially affects the credibility of the performance claim.
- **Required correction** List the specific baseline methods compared in the full manuscript and justify their selection as appropriate state-of-the-art representatives.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Author summary accessibility
- **Affected element** Author summary
- **Evidence pointer** Author summary paragraph
- **Issue** The author summary states that existing approaches "treat all interactions as arising from a dominant pattern" but does not provide examples of such approaches or explain why this assumption is problematic in practice.
- **Required correction** Provide a brief illustrative example of how existing methods fail to capture interaction heterogeneity to strengthen the motivation for the proposed approach.

## Risk / unsupported claims
- The 7.19% Micro-F1 improvement over the second-best method is unsupported without dataset names, baseline specifications, statistical significance testing, or variance estimates.
- The claim that DMG-PPI "substantially outperforms" state-of-the-art methods is unverifiable from the abstract alone.
- The interpretability claim regarding "key binding residues" and "interfacial mechanisms" is entirely unsupported without validation against experimental data or known annotations.
- The claim that the framework "extends prior heterophilous GNN concepts" is unverifiable without a detailed comparison to specific prior methods.
- The assertion that AMP captures "symmetric interfaces" and DMP extracts "complementary binding patterns" is a design assumption that requires empirical validation to confirm that the two channels indeed learn distinct and biologically meaningful representations.
- The generalizability of the approach across different PPI types, species, or interaction contexts is not addressed and cannot be evaluated from the abstract.