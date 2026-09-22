## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and figure legends (as provided).
- **Assessment boundary** Scientific validity, technical soundness, methodological novelty, clarity of claims, and alignment with stated evidence. Editorial and stylistic suggestions are secondary.
- **Shared manuscript claim summary** The authors present idpSAM, a latent diffusion model with a transformer backbone, trained on ABSINTH implicit-solvent simulations of intrinsically disordered protein regions. They claim high transferability to sequences absent from training, improved accuracy over their prior GAN-based model (idpGAN), robustness to limited training sampling, and the ability to recover near-converged ensembles for unseen peptides.
- **Visible evidence base** Main text figures (Fig 1-6), tables (Table 1), supplementary figure and table references (S1-S16, S1-S6 Tables), and methodological descriptions in the Methods section.
- **Missing materials affecting confidence** The full supplementary information (figures, tables, and detailed methods) is referenced but not provided. This includes S1-S16 Figs, S1-S6 Tables, and S1-S4 Texts. Without these, quantitative validation of reconstruction accuracy, statistical significance tests, and detailed architectural choices cannot be independently assessed.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important problem: the efficient generation of conformational ensembles for intrinsically disordered proteins with transferability to unseen sequences. The methodological shift from GANs to latent diffusion models, combined with a substantially expanded training set, is a logical and promising direction. The reported results, if fully supported by the supplementary material, would represent a meaningful advance over prior work. However, the current manuscript leaves several critical technical questions unanswered, particularly regarding the completeness of generated ensembles, the statistical robustness of the comparisons, and the generalizability of the method to longer or more structured systems. The claims of "high transferability" and "faithful capture" of ensembles require more rigorous quantitative evidence than is currently visible in the main text.
- **Who would be interested in the results, and why** Computational biophysicists and structural biologists studying IDPs/IDRs, developers of machine learning methods for biomolecular conformation generation, and researchers interested in integrative structural biology. The potential for rapid ensemble generation from sequence alone, without the need for expensive simulations, is broadly appealing.
- **Major strengths**
  1. The problem is well-motivated and significant.
  2. The methodological choice of a latent diffusion model with SE(3)-invariant encodings is sensible and potentially more stable and scalable than GANs.
  3. The systematic comparison with the previous idpGAN model, including a controlled re-training on the same data, is a strong and commendable feature.
  4. The analysis of training set size and sampling completeness addresses key practical questions for the field.
  5. The manuscript is generally well-written and accessible.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness / Evidence for core claim
  - **Claim pointer** The manuscript claims that idpSAM "faithfully captures" and "closely reproduces" the 3D structural ensembles of test sequences, including the ability to "approximately recover the full ensemble" for a challenging case like drk_sh3.
  - **Evidence pointer** Results section "Completeness of generated conformational ensembles", Fig 5, Table 1.
  - **Concern** The central claim of transferability and accurate ensemble reproduction rests on a comparison between idpSAM-generated ensembles and reference MCMC ensembles. While visual agreement in PCA projections and similarity in summary statistics (e.g., Rg, contact maps) are shown for a few examples, the quantitative evidence for "completeness" is not fully presented in the main text. The comparison against the "MCMC-5" strategy is interesting, but the specific metrics used (aJSD_d, aJSD_t, etc.) are only briefly defined. The claim that idpSAM recovers the "full" or "converged" ensemble for drk_sh3 is particularly strong and requires a more detailed demonstration that the generated ensemble covers the same conformational space as the extensively sampled reference, not just similar average properties. The potential for mode collapse or over-smoothing in the generated distribution, which is a known challenge for diffusion models, is not explicitly addressed.
  - **Why it matters** The primary value proposition of idpSAM is its ability to generate accurate and complete ensembles for unseen sequences. If the generated ensembles are only similar in low-order statistics but miss important minor conformational states, the method's utility for downstream applications (e.g., understanding function) is significantly diminished. This is the core scientific claim of the paper.
  - **Resolution test** Provide a more detailed quantitative analysis of ensemble overlap, such as a comparison of the distribution of conformations in a reduced dimensional space (e.g., using a metric like the Earth Mover's Distance on PCA projections) or a direct comparison of the population of specific conformational states identified in the reference ensemble. Show that the generated ensemble for drk_sh3 contains the same set of major and minor states as the reference, with similar populations. A more detailed description of the aJSD metrics and their interpretation would also be necessary.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness / Generalizability
  - **Claim pointer** The manuscript states that idpSAM is a "transferable deep generative model" and implies general applicability to IDPs/IDRs.
  - **Evidence pointer** Results section "Case studies illustrating sequence and structure transferability", Discussion.
  - **Concern** The test set, while carefully selected, is limited to peptides of relatively short length (8-59 residues) and mostly low sequence complexity. The manuscript acknowledges limitations for longer peptides but does not provide a clear path forward. The claim of "transferability" is demonstrated for sequences within the training distribution's length and complexity range. The performance on a longer, more complex IDR, or an IDR with a known functional fold, is not tested. The discussion of this limitation is brief and somewhat dismissive.
  - **Why it matters** The ultimate goal is to model biologically relevant IDPs, many of which are longer than 60 residues and may contain regions of transient structure. A model that only works well for short, simple sequences has limited practical utility. The paper's claim of being a general solution is therefore not fully supported by the evidence.
  - **Resolution test** Include at least one test case of a longer IDR (e.g., >100 residues) or an IDR with a more complex sequence composition. If performance degrades, this should be discussed as a clear limitation with potential solutions (e.g., hierarchical generation, sequence-conditioned generation with positional embeddings).
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness / Reproducibility
  - **Claim pointer** The Methods section describes the training and evaluation protocol, and the Data Availability statement provides a link to code and weights.
  - **Evidence pointer** Methods section "Training and validation sets", "Test set", "Data Availability".
  - **Concern** The description of the training data is incomplete. The authors state that the dataset includes 1,089 peptides from a previous study and 2,170 new peptides, but the selection criteria for the new peptides are only in the supplementary text (S1 Text). The details of the simulation protocol are also deferred to S2 Text. While this is common practice, the main text should provide enough information for a reader to understand the scope and potential biases of the training data. More critically, the evaluation metrics (MSE_c, MSE_d, aKLD_d, etc.) are only briefly defined in the main text, with details in S4 Text. For a rigorous review, the precise definitions of these metrics are essential.
  - **Why it matters** Reproducibility is a cornerstone of scientific progress. Without clear definitions of the data, simulation, and evaluation protocols, it is difficult for other researchers to build upon this work or to fully assess the validity of the claims.
  - **Resolution test** Move the essential details of the data selection, simulation protocol, and metric definitions from the supplementary text into the main Methods section, or provide a more detailed summary that allows for a critical evaluation without requiring the reader to constantly refer to the supplement.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Abstract and Introduction
  - **Evidence pointer** Abstract, Introduction.
  - **Issue** The term "transferable" is used frequently but not formally defined. Does it mean generalization to unseen sequences, unseen conditions, or both?
  - **Required correction** Provide a clear, operational definition of "transferability" in the Introduction.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Results section "Sampling speed"
  - **Evidence pointer** Fig 3.
  - **Issue** The comparison of sampling speed between idpSAM and MCMC is useful, but the hardware and software environment for the MCMC simulations (CPU-only) vs. the deep learning model (GPU) are different. This is acknowledged, but a more direct comparison of the computational cost (e.g., in terms of total CPU/GPU hours) would be more informative.
  - **Required correction** Provide a more detailed breakdown of the computational cost, including the time for training the model and the cost of generating a single ensemble, in a common unit (e.g., GPU-hours and CPU-hours).
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Readability
  - **Affected element** Results section "Case studies illustrating sequence and structure transferability"
  - **Evidence pointer** Fig 4.
  - **Issue** The choice of the CGRP wild-type/mutant pair is a good example, but the biological significance of the observed differences is not discussed. Why is it important that the model captures the effect of these specific mutations?
  - **Required correction** Add a sentence or two explaining the biological context of the CGRP example and why the ability to model this mutation is relevant.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Methods section "Invariant structural AE"
  - **Evidence pointer** Methods.
  - **Issue** The choice of the latent dimension c=16 is stated to be empirical, but no data is shown for the exploration of this hyperparameter.
  - **Required correction** Briefly mention the range of values tested and the criterion used for selection, or state that a sensitivity analysis is provided in the supplement.
- **Technical failings that need to be addressed before the case is established**
  - R1-M1: The evidence for "complete" ensemble generation is insufficient. The claim of recovering the full ensemble for drk_sh3 needs stronger quantitative support.
  - R1-M2: The generalizability of the model to longer, more complex IDRs is not demonstrated.
  - R1-M3: The main text lacks sufficient detail on data selection, simulation protocols, and evaluation metrics for full reproducibility and critical assessment.

## Risk / unsupported claims
- The claim that idpSAM "achieves high levels of transferability" is supported for the tested sequence space but is overgeneralized in the abstract and discussion.
- The claim that idpSAM "faithfully captures" the full ensemble of drk_sh3 is not fully supported by the evidence presented in the main text.
- The claim that the model "learned general principles about the conformational sampling of peptides" is a plausible interpretation but is not directly tested or proven.
- The statement that "generative models trained on sufficiently large datasets can achieve a level of transferability necessary for accurately modeling the impact of single amino acid mutations" is supported by the CGRP example but may not hold for all mutations or sequence contexts.
- The performance of idpSAM on ensembles generated by other force fields or solvent models is not assessed, so the claim of general applicability to "intrinsically disordered protein conformations" is limited to the ABSINTH model.