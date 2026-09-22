## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, materials and methods, and figure legends as provided.
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and internal consistency based solely on the supplied text. No external data, figures, or supplementary files were accessed.
- **Shared manuscript claim summary** The authors propose that pathologic polyglutamine (polyQ) aggregation is initiated by a monomeric, intramolecular steric zipper ("Q zipper") that self-poisons its own growth, leading to kinetically trapped aggregates. They support this with DAmFRET assays in yeast, systematic sequence perturbations, and molecular dynamics simulations.
- **Visible evidence base** Text descriptions of DAmFRET results, sequence design logic, SDD-AGE analyses, and simulation outcomes. Figure references are cited but figures themselves were not provided.
- **Missing materials affecting confidence** All figures, figure supplements, supplementary files, and raw data. Simulation parameters are partially described but trajectory analyses and validation metrics are absent. Statistical details and replicate numbers are not reported in the text.

## Reviewer
- **Overall assessment** This manuscript presents a compelling and potentially transformative model for polyQ aggregation nucleation. The central claim that nucleation occurs via a monomeric, intramolecular Q zipper is well-motivated by the sequence perturbation data described, and the self-poisoning concept elegantly explains several puzzling features of polyQ aggregation. However, the absence of the actual figures and supplementary data prevents full verification of the quantitative claims. The molecular dynamics simulations, as described, are preliminary and would need more rigorous validation to support the structural conclusions. The clinical and translational implications are thoughtfully discussed, though somewhat speculative. Overall, this is an important contribution that merits consideration, but the evidence as presented in the text alone is not fully sufficient to establish all claims.
- **Who would be interested in the results, and why** Researchers studying amyloid nucleation mechanisms, protein misfolding diseases (particularly Huntington's disease and other polyQ disorders), and those interested in the physical chemistry of protein aggregation. The self-poisoning concept may also appeal to polymer physicists and biophysicists studying crystallization phenomena. The DAmFRET methodology is broadly applicable and will interest investigators studying protein self-assembly in cells.
- **Major strengths** 1) The DAmFRET approach provides a powerful, high-throughput means to interrogate nucleation events in living cells, overcoming limitations of in vitro assays. 2) The systematic sequence perturbation strategy is elegant and logically rigorous. 3) The self-poisoning model is conceptually novel and provides a unifying framework for understanding polyQ aggregation kinetics and pathology. 4) The integration of experimental and computational approaches is commendable. 5) The discussion of clinical implications and therapeutic strategies is thoughtful and forward-looking.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** **Originality**: High. The monomeric intramolecular nucleation model and the self-poisoning concept are novel and depart from prevailing models that emphasize intermolecular interactions in nucleation. **Scientific importance**: High. If substantiated, this work would fundamentally change understanding of polyQ aggregation and potentially other amyloid systems. The clinical implications for Huntington's disease are significant. **Interdisciplinary readership**: Moderate to high. The work bridges cell biology, biophysics, and polymer science. The self-poisoning analogy to polymer crystallization will appeal to physical scientists, while the disease relevance will attract biomedical researchers. **Technical soundness**: The DAmFRET methodology appears well-established from prior work, and the sequence perturbation logic is sound. However, the simulation component, as described, lacks the rigor and validation expected for structural claims. **Readability for nonspecialists**: The manuscript is generally well-written and accessible, though some sections (particularly the simulation descriptions) assume specialized knowledge. The conceptual framework is clearly explained.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding simulation validation and presentation of quantitative data.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The claim that "nucleation of pathologically expanded polyQ involves segments of three glutamine (Q) residues at every other position" is central to the paper.
- **Evidence pointer** Results section "A hidden pattern of glutamines governs amyloid nucleation"; Figure 1E; Figure 1—figure supplement 1B
- **Concern** The text describes an "odd-even effect" where sequences with q=1, 3, 5 nucleate but q=2, 4 do not, and that this saturates at q≥6. However, the actual DAmFRET data are not shown in the provided text. The distinction between "nucleation" and "aggregation" is not always clear. For q=1, the sequence would be QNQNQN... which has only single Qs separated by Ns. It is surprising that this would nucleate a Q zipper requiring Qs at every other position. The authors need to clarify how a single Q between Ns satisfies the "every other position" requirement. Additionally, the claim that the pattern encodes a "single unique steric zipper" is strong, but the evidence for uniqueness (as opposed to multiple possible zipper geometries) is not presented.
- **Why it matters** This is the foundational observation of the paper. If the pattern interpretation is incorrect or overinterpreted, the entire model collapses. The odd-even effect is counterintuitive and requires robust, clearly presented data to be convincing.
- **Resolution test** Provide the actual DAmFRET plots for all sequence variants, with statistical replicates. Clarify the structural interpretation of how QNQNQN sequences (q=1) can form a Q zipper. Demonstrate that the observed pattern is specific to Q zipper formation and not an artifact of the assay or sequence design.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical rigor
- **Claim pointer** The claim that molecular dynamics simulations demonstrate a "four-stranded steric zipper with interdigitated Q side chains" that is "poisoned" by orthogonal engagement.
- **Evidence pointer** Results section "The Q zipper grows both laterally and axially"; Figure 2D; Figure 2—figure supplement 1A-B; Materials and methods "Molecular Simulations"
- **Concern** The simulation methodology is described only briefly. Key details are missing: force field validation, simulation length, number of replicas, convergence criteria, and how the "poisoned" state was identified and characterized. The claim that the zipper "dissolved" upon N substitution is based on visual inspection of trajectories, but no quantitative metrics (e.g., RMSD, contact maps, free energy profiles) are provided. The simulations are used to support a very specific structural model, but the evidence presented is insufficient to distinguish between the proposed model and alternative interpretations.
- **Why it matters** The simulations are used to provide mechanistic insight into the experimental observations. If the simulations are not rigorously validated, the structural conclusions are speculative. The self-poisoning mechanism is a key conceptual advance, and its credibility depends on the quality of the simulation evidence.
- **Resolution test** Provide detailed simulation protocols, including convergence analysis, multiple independent replicates, and quantitative analysis of zipper stability (e.g., hydrogen bond occupancy, side chain contact maps). Show that the observed dissolution is statistically significant and not a single trajectory artifact. Consider enhanced sampling methods to explore the free energy landscape.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The claim that "self-poisoning can be exploited to block amyloid formation, by genetically oligomerizing polyQ prior to nucleation."
- **Evidence pointer** Results section "The nucleus forms within a single molecule"; Figure 5B; Figure 5—figure supplement 1B-F
- **Concern** The text states that fusing polyQ to oligomeric modules (oDi dimer, FTH1 24-mer) reduced or eliminated amyloid formation. However, the mechanism is not fully established. The authors interpret this as evidence for monomeric nucleation, but alternative explanations are possible: the fusion partners could sterically block aggregation, alter protein folding, or affect degradation/localization. The control experiments described (varying terminus, linker, and a monomerization mutation) are good, but the quantitative data are not shown. The claim that this "can be exploited to block amyloid formation" is presented as a therapeutic strategy, but no data on disease-relevant models are provided.
- **Why it matters** This is a key piece of evidence for the monomeric nucleation model. If the inhibition is due to non-specific effects of the fusion partners, the conclusion is weakened. The therapeutic implication is significant but currently speculative.
- **Resolution test** Provide quantitative DAmFRET data for all fusion constructs, including dose-response curves. Perform additional controls, such as fusing to a non-oligomeric but similarly sized protein, to rule out steric effects. Discuss how this strategy could be translated to therapeutic approaches in disease models.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The claim that the clinical threshold for polyQ disease (approximately 36 Qs) corresponds to the minimum length required for the intramolecular Q zipper.
- **Evidence pointer** Discussion section "PolyQ amyloid begins within a molecule"; Results section "A hidden pattern of glutamines governs amyloid nucleation"
- **Concern** The authors state that the clinical threshold of ~36 residues is the minimum length that encompasses the pattern of Qs at every other position. However, the logic is not fully explained. The proposed zipper has four strands of six Qs, which would require 24 Qs, not 36. The relationship between the sequence pattern, the zipper structure, and the clinical threshold needs to be made explicit. Additionally, the clinical threshold varies among the nine polyQ diseases (e.g., SCA6 has a threshold of ~21, SCA2 ~32), which is not addressed. The authors mention SCA2 and SCA6 as atypical, but do not explain how their model accommodates these exceptions.
- **Why it matters** The connection between the molecular model and the clinical threshold is a major selling point of the paper. If this connection is not rigorously established, the clinical relevance of the model is weakened.
- **Resolution test** Provide a clear structural model showing how the 36-residue threshold arises from the proposed zipper geometry. Discuss how variations in threshold among different polyQ diseases can be explained by the model, or acknowledge limitations.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "self-poisoning polymer crystal" is evocative but may be confusing to readers unfamiliar with polymer physics. The abstract would benefit from a brief explanation of what self-poisoning means in this context.
- **Required correction** Add a brief parenthetical explanation, e.g., "a process whereby the growing crystal inhibits its own further growth."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical clarity
- **Affected element** Results section "The Q zipper grows both laterally and axially"
- **Evidence pointer** Figure 3B; Figure 3—figure supplement 1A
- **Issue** The distinction between "axial" and "lateral" growth of the zipper is not clearly defined. The text mentions "lamellar" architecture but does not explain how this relates to the proposed zipper structure.
- **Required correction** Provide a schematic diagram or clear verbal description of the axial and lateral growth directions and how they relate to the β-sheet and zipper geometry.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion section "Proteotoxic multimers may be self-poisoned polymer crystals"
- **Evidence pointer** Discussion, paragraph 2
- **Issue** The discussion of proteotoxicity is speculative and does not cite specific experimental evidence linking the proposed self-poisoned aggregates to toxicity. The authors mention "kinetically trapped aggregates" but do not discuss how these might differ from mature fibrils in terms of toxicity.
- **Required correction** Add a brief discussion of how the proposed model could be tested in toxicity assays, or acknowledge the speculative nature of this section more explicitly.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Materials and methods "DAmFRET automated analysis"
- **Evidence pointer** Materials and methods, DAmFRET automated analysis section
- **Issue** The gating strategy is described in detail, but the specific parameters for the "polyline kymograph jru v1" and "normalize trajectories jru v1" plugins are not provided. This limits reproducibility.
- **Required correction** Provide the full code or detailed parameter settings for these custom plugins, or cite a source where they are available.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Results section "A hidden pattern of glutamines governs amyloid nucleation"
- **Evidence pointer** Figure 1C-D
- **Issue** The text describes "two discontinuous populations" in the DAmFRET plots, but the quantitative threshold for defining these populations is not stated. The criteria for classifying cells as "high AmFRET" versus "no AmFRET" should be explicit.
- **Required correction** State the specific AmFRET threshold used to define positive versus negative populations, and how this threshold was determined.

## Risk / unsupported claims
- The claim that the identified Q zipper is the "single unique" nucleation structure is not fully supported; other structures may also be competent for nucleation.
- The extrapolation from yeast DAmFRET data to human disease mechanisms is plausible but not directly demonstrated.
- The therapeutic suggestion that oligomerizing polyQ could delay disease is speculative and not tested in any disease model.
- The claim that the clinical threshold of ~36 Qs directly corresponds to the minimal zipper length requires more explicit structural and quantitative justification.
- The interpretation of the "self-poisoned" state as the toxic species is inferred, not directly tested.