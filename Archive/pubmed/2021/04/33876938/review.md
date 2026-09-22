## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, conclusion, and supplementary material description
- **Assessment boundary** Scientific validity, methodological soundness, claims versus evidence, and suitability for the stated journal context
- **Shared manuscript claim summary** The authors derive a new data-driven hydrophobicity scale (FB-HPS) for the Hydrophobicity Scale (HPS) coarse-grained model, optimized against experimental radii of gyration of disordered and phase-separating proteins, and claim improved prediction of liquid-liquid phase separation propensity compared to existing scales
- **Visible evidence base** Main text figures referenced (Figures 1-6), supplementary tables and figures described but not provided in full, simulation methodology details, optimization procedure equations
- **Missing materials affecting confidence** Supplementary tables S1-S6 (protein lists, sequences, parameters), supplementary figures S2, S3, S5, full simulation parameter details, exact experimental data values used for fitting

## Reviewer
- **Overall assessment** The manuscript presents a useful and timely contribution to the coarse-grained modeling of liquid-liquid phase separation, with a clear methodological framework and a plausible optimization strategy. The central claim that a data-driven hydrophobicity scale improves phase-separation prediction is supported by the presented comparisons, though several technical aspects require clarification and the evidence base is partially incomplete in the provided material. The work is likely of interest to the biomolecular simulation and phase separation communities, but the strength of the conclusions depends on details not fully visible in the supplied text.
- **Who would be interested in the results, and why** Researchers in computational biophysics, specifically those developing or using coarse-grained models for intrinsically disordered proteins and phase-separating systems. The work also has relevance for experimentalists studying membraneless organelles who seek sequence-based predictors of phase behavior, and for method developers interested in data-driven parameter optimization.
- **Major strengths** The optimization strategy is well motivated by the known limitations of existing hydrophobicity scales for disordered proteins. The use of the Force Balance method is appropriate and clearly described. The validation approach, including explicit slab simulations of a held-out peptide, strengthens the central claim. The analysis of which residues change in hydrophobicity and the connection to π-π interactions provides mechanistic insight.
- **Major Concerns** Several concerns are identified below, primarily relating to the completeness of the evidence presented, the handling of the PSP training data, and the interpretation of the phase-separation prediction metric.
- **Minor Comments** Several minor issues regarding clarity, terminology, and presentation are noted.
- **Technical failings that need to be addressed before the case is established** R1-M1 (PSP training data handling), R1-M2 (phase-separation prediction metric), R1-M3 (off-diagonal optimization interpretation)
- **Assessment against Nature-style criteria** Originality is moderate; the approach is novel in its specific application but builds on established methods. Scientific importance is solid for the target community but not transformative. Interdisciplinary readership is limited to biophysics and computational chemistry. Technical soundness is generally good but with gaps in the visible evidence. Readability for nonspecialists is adequate, though some terminology assumes familiarity with the field.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the handling of PSP training data and the clarity of the phase-separation prediction metric.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological validity
- **Claim pointer** The authors state that the final training set included both PSP and non-PSP proteins, with PSP weighted by a factor of 4.25, and that this was necessary to achieve phase-separation prediction.
- **Evidence pointer** Methods, Optimization Procedure; Results, Optimization section; location not provided for specific figure panels
- **Concern** The manuscript states that PSP proteins were included in the training set using a half-parabola penalty term that assumes their Rg must be less than the theta-condition value, since single-chain experimental data are unavailable. This is a strong assumption that effectively imposes the desired outcome (collapse) on the PSP training set. The weighting factor of 4.25 is stated but not justified. The concern is whether the resulting scale is genuinely predictive or partially circular, since the PSP proteins are trained to be collapsed, and collapse is then used as the predictor of phase separation.
- **Why it matters** If the PSP training constraint is the primary driver of the improved phase-separation prediction, the claim that the scale captures "important interactions" of phase-separating proteins is weakened. The distinction between learning from physical data versus imposing a constraint must be clear for the reader to assess the validity of the central claim.
- **Resolution test** The authors should provide a clear justification for the half-parabola constraint and the weighting factor. Ideally, they should show that the optimization without the PSP constraint (or with a different constraint) does not achieve the same phase-separation prediction, or they should present an analysis of how sensitive the final scale is to the PSP constraint form and weight.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that the FB-HPS scale predicts phase separation with "much higher accuracy" than existing scales, based on classification of proteins as phase-separating or not using the Flory exponent threshold of ν = 0.5.
- **Evidence pointer** Results, Hydrophobicity scales section, Figure 3; location not provided for exact classification counts
- **Concern** The phase-separation prediction is evaluated by whether the simulated single-chain Flory exponent is above or below 0.5, with the assumption that ν < 0.5 indicates phase-separation propensity. The manuscript reports correction of five false positives and seven false negatives relative to the original HPS model, with one remaining false positive and one new false negative. However, the total number of proteins in the validation set is not stated, and the statistical significance of these improvements is not assessed. With a small validation set, the difference between, for example, 12 correct classifications and 10 correct classifications may not be meaningful.
- **Why it matters** The central claim of improved predictive accuracy rests on this classification comparison. Without knowing the total validation set size and the uncertainty in the classification, the reader cannot judge whether the improvement is robust or within noise.
- **Resolution test** The authors should report the full confusion matrix for both the original and new scales, including the total number of validation proteins. They should also discuss the uncertainty in the Floyer exponent estimation and how it affects the classification. A statistical test, even a simple binomial test, would strengthen the claim.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of results
- **Claim pointer** The authors state that optimizing the full interaction matrix (off-diagonal terms) only marginally improves the training and validation error, concluding that the per-residue hydrophobicity with mixing rules is a reasonable approximation.
- **Evidence pointer** Results, Optimization of Off-Diagonal Interactions section, Figure S5; location not provided
- **Concern** The conclusion that mixing rules are adequate is based on a single comparison of training and validation error. The manuscript does not report whether the off-diagonal optimized model changes the phase-separation classification performance, which is the primary claim of the paper. It is possible that the off-diagonal model improves phase-separation prediction even if the Rg error is similar, or vice versa.
- **Why it matters** The choice of a compact per-residue representation versus a full interaction matrix has implications for the transferability and physical interpretability of the model. The conclusion that mixing rules are sufficient should be evaluated against the primary metric of interest, not just the secondary Rg metric.
- **Resolution test** The authors should report the phase-separation classification performance of the off-diagonal optimized model in addition to the Rg error. If the classification is unchanged, the conclusion is strengthened. If it differs, the interpretation of the per-residue scale as capturing the essential physics needs revision.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "macroscale disordered assemblies" is vague and could be misinterpreted. The authors likely mean "mesoscale" or simply "disordered assemblies" in the context of phase-separated droplets.
- **Required correction** Rephrase to "disordered assemblies of biological macromolecules" or specify the length scale more precisely.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph 2
- **Issue** The term "multivalancy" is used, but the correct spelling is "multivalency."
- **Required correction** Correct the spelling.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, Simulation Details
- **Evidence pointer** Methods, Simulation Details section
- **Issue** The manuscript states that the system was equilibrated for 100 ns and statistics collected for 500 ns, but does not specify the number of independent simulations or how statistical uncertainties were estimated for the reported Rg values.
- **Required correction** Provide details on the number of replicates and the method for estimating uncertainties in the simulated Rg values.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Results, Hydrophobicity scales section
- **Evidence pointer** Results, Figure 3 description
- **Issue** The manuscript states that "both of these are very close to the dividing line indicating ν=1/2" for the remaining false positive and new false negative. This is presented qualitatively without numerical values.
- **Required correction** Report the actual Flory exponent values for these two proteins to allow the reader to assess how close they are to the threshold.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, Hydrophobicity scales section
- **Evidence pointer** Results, Figure 4 description
- **Issue** The discussion of which residues increase or decrease in hydrophobicity is qualitative. The authors state that six of seven increased residues are π-π donors, but do not provide the numerical values of the changes.
- **Required correction** Include a table or list of the numerical hydrophobicity values for all 20 residues in the original and optimized scales.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Conclusion
- **Evidence pointer** Conclusion, first paragraph
- **Issue** The sentence "the model's lack of resolution likely limits its expressiveness" is vague. The authors should specify what types of interactions or sequence features are likely missed at one-bead-per-residue resolution.
- **Required correction** Provide specific examples of limitations, such as inability to distinguish backbone versus side-chain contributions or lack of explicit hydrogen bonding.

## Risk / unsupported claims
- The claim that the FB-HPS scale "confirms the importance of π-π interactions" is partially supported by the residue-level analysis, but the connection between increased hydrophobicity of π-π donors and the physical mechanism of phase separation is inferred rather than directly demonstrated.
- The statement that the new scale "could be used to develop new models to describe interactions between PSP and other components, such as nucleic acids" is speculative and not supported by any data in the manuscript.
- The claim that the scale "predicts phase separation in a similar way to prediction of disorder in previous studies" is an analogy that is not quantitatively substantiated.
- The assertion that the original HPS model "is not sufficiently accurate to quantitatively predict" phase separation is based on the presented comparisons, but the quantitative threshold for "sufficiently accurate" is not defined.
- The performance comparison with "a variety of hydrophobicity scales described in the literature" is mentioned but the specific scales and their results are not shown in the provided material, making this claim unverifiable from the supplied text.