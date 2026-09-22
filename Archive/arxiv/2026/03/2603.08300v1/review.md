## Review setup
- **Input scope** Full manuscript text (main text, methods summary, references) as provided
- **Assessment boundary** Scientific content, methodological soundness, claims vs. evidence, and presentation quality of the described framework
- **Shared manuscript claim summary** The authors introduce a thermodynamic metric space, learned via a symmetry-preserving machine-learning model trained on equation-of-state data from coarse-grained simulations, that quantitatively predicts excess chemical potentials, free energies, and multicomponent phase behavior of intrinsically disordered protein regions (IDRs) across arbitrary mixtures, and provides interpretable geometric insights into partitioning, condensation, and mutational effects
- **Visible evidence base** Main text sections I through IV, including descriptions of Figures 1 through 5 and referenced supplementary figures (S1 through S6); no actual figure panels, numerical data tables, or simulation details are visible in the provided material
- **Missing materials affecting confidence** Figure panels and captions; all numerical error values and quantitative comparisons; Extended Methods details; training data generation protocols; hyperparameter choices; code availability; full reference list content

## Reviewer
- **Overall assessment** The manuscript presents a conceptually appealing and potentially significant framework that unifies prediction of IDR mixture thermodynamics within a learned metric space. The core idea, that low-dimensional context-independent sequence representations can predict multicomponent phase behavior, is timely and could be of broad interest. However, the provided text alone does not allow verification of the central quantitative claims. The absence of visible figures, numerical error metrics, and detailed methodological descriptions prevents assessment of whether the stated accuracy (e.g., "comparable to state-of-the-art simulations," "quantitative agreement") is actually achieved. The conceptual framework is well articulated, but the evidence base is incomplete in the supplied material.
- **Who would be interested in the results, and why** Researchers in biomolecular condensate biology, intrinsically disordered protein biophysics, computational biophysics, and machine learning applied to molecular systems. The framework's promise of quantitative prediction of multicomponent phase behavior from sequence alone, without explicit phase-coexistence simulations, would be of practical value to experimentalists studying condensate composition and to theorists developing predictive models. The geometric interpretation of partitioning and mutational effects could also interest a broader biophysics audience.
- **Major strengths** The conceptual framing is elegant and ambitious, unifying several previously disparate problems (partitioning, condensation, mutational effects) within a single geometric framework. The choice to train on equation-of-state data rather than phase-coexistence data is methodologically sensible and could substantially reduce computational cost. The explicit treatment of mixture symmetry and the provable sufficiency argument in the large-dimension limit provide a principled foundation. The analysis of composition-independent patterning effects via composition-preserving mutants is a thoughtful and rigorous approach to a notoriously difficult problem.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (evidence for quantitative accuracy not visible), R1-M2 (dimensionality claim not substantiated), R1-M3 (patterning analysis validation incomplete), R1-M4 (generalization to experimental systems not demonstrated)
- **Assessment against Nature-style criteria** Originality: High. The thermodynamic metric space concept is a novel synthesis of machine learning and mixture thermodynamics applied to IDRs. Scientific importance: Potentially high, if the quantitative claims hold, as it could provide a general predictive framework for a central problem in condensate biology. Interdisciplinary readership: The conceptual accessibility is good, but the technical sections assume significant familiarity with both statistical mechanics and machine learning. Technical soundness: Cannot be fully assessed from the provided material; the methodological logic is coherent, but key validations are not visible. Readability for nonspecialists: The introduction and geometric interpretations are clearly written, but the methods and results sections would be challenging for readers without a computational biophysics background. Overall, the manuscript has the ambition and scope consistent with a high-impact venue, but the evidence as presented is insufficient to establish the central claims.
- **Recommendation posture** Currently not established from the provided evidence. The conceptual framework is promising and the writing is clear, but the absence of visible quantitative results, figures, and methodological details precludes a supportive recommendation. I would need to see the full figures, numerical error metrics, and Extended Methods to assess whether the claims are substantiated.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims "quantitative agreement" with molecular simulations for multicomponent phase diagrams (Section II.3) and accuracy "comparable to state-of-the-art simulations" (Abstract), with EOS predictions in "quantitative agreement" for held-out IDRs (Section II.2).
- **Evidence pointer** Figures 1f, 1j, 2d, 2e, S2, S4; location not provided for numerical values
- **Concern** The central quantitative claims of the manuscript are not verifiable from the provided text. No numerical error values, confidence intervals, or statistical comparisons are visible. The descriptions of "quantitative agreement" and "comparable accuracy" are asserted but not demonstrated in the text. The reader cannot assess whether the agreement is within thermal energy, within simulation uncertainty, or merely correlative.
- **Why it matters** The entire case for the framework's utility rests on its quantitative predictive accuracy. Without visible error metrics and comparisons to baselines, the claims of superiority over pairwise models and hand-crafted approaches cannot be evaluated. This is the core evidence needed to establish the manuscript's central thesis.
- **Resolution test** Provide the actual figure panels with error bars, numerical RMSE values for EOS and free-energy predictions, and the distribution of W1 distances for phase-diagram predictions compared to positive and negative controls. State explicitly how "quantitative agreement" is defined and whether it holds across the full test set or only in selected cases.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim substantiation
- **Claim pointer** The manuscript claims the thermodynamic behavior of IDR mixtures is "intrinsically low dimensional" with "at most d approximately 10 dimensions" required for accuracy (Section II.1).
- **Evidence pointer** Figure 1d, 1e; location not provided for convergence criteria
- **Concern** The dimensionality claim is central to the framework's interpretability and efficiency, but the evidence for the d approximately 10 saturation is not visible. The text states that errors "decrease rapidly" and "saturate," but no quantitative convergence criteria or error-vs-dimension curves are shown. The claim that this reflects an intrinsic property of IDR thermodynamics, rather than a property of the Mpipi force field or the training data distribution, is not addressed.
- **Why it matters** If the low-dimensionality claim is an artifact of the specific force field or training set, the framework's generality would be substantially weakened. The claim of intrinsic low-dimensionality is a strong statement about the physics of IDR mixtures and requires evidence that it holds across diverse sequence ensembles and interaction models.
- **Resolution test** Show the error-versus-dimension curves with clear convergence criteria. Discuss whether the dimensionality is robust to changes in the training sequence distribution, force field parameters, or mixture complexity. Provide evidence that the discovered dimensions correspond to physically meaningful sequence features rather than artifacts of the encoder architecture.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Validation completeness
- **Claim pointer** The manuscript claims the model "clearly discriminates" WT and MUT mixtures and that composition-preserving patterning effects are captured (Section II.6), with a systematic analysis of "when and how patterning matters" (Section II.7).
- **Evidence pointer** Figures 4d through 4h, S6; location not provided for statistical tests
- **Concern** The analysis of composition-independent patterning effects is methodologically interesting, but the validation appears incomplete. The text states that prediction error increases to approximately 0.3 kT when labels are interchanged, but does not state whether this is statistically significant across the test set or whether the effect size is uniform across sequence families. The claim that the model "captures" patterning effects requires demonstration that the learned representations generalize to sequences beyond the training distribution, not merely that they fit the training data.
- **Why it matters** Patterning effects are notoriously subtle and context-dependent. If the model only captures a subset of patterning effects or fails on certain sequence families, the claim of a general framework would be overstated. The practical utility of the counterfactual analysis for guiding experimental design depends on the reliability of these predictions.
- **Resolution test** Provide statistical significance tests for the discrimination of WT versus MUT mixtures. Show that the model generalizes to sequence families or mixture compositions not represented in the training set. Discuss any known limitations or failure cases in capturing patterning effects.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scope of claims
- **Claim pointer** The manuscript claims the framework is "general" and applicable to "arbitrary combinations of IDRs" (Abstract, Section II.1), and that it "establishes a general, interpretable foundation" for sequence-dependent phase behavior (Section III).
- **Evidence pointer** Sections II.1 through II.7; location not provided for scope limitations
- **Concern** The framework is trained and validated exclusively on the Mpipi coarse-grained force field. The claim of generality across IDR systems is not supported by evidence from other force fields, experimental data, or systems with different interaction chemistries. The text acknowledges that the framework "inherits limitations of the underlying force field" but does not discuss how these limitations affect the claimed generality.
- **Why it matters** The broader significance of the work depends on whether the framework captures universal features of IDR thermodynamics or only features specific to Mpipi. If the learned representations are force-field-specific, the framework would require retraining for each new interaction model, limiting its practical utility.
- **Resolution test** Discuss the expected transferability of the framework to other force fields or experimental datasets. Provide evidence, even preliminary, that the learned representations capture features relevant to experimentally observed IDR behavior beyond Mpipi. Clarify the scope of the "generality" claim.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section II.1, Eq. (1) and surrounding text
- **Evidence pointer** Section II.1, Eq. (1)
- **Issue** The notation in Eq. (1) is introduced somewhat abruptly. The text states that the excess chemical potential is "equal to" the expression, but the derivation from the free-energy density is not shown in the main text. The relationship between the gradient of the free-energy density and the chemical potential may not be immediately obvious to all readers.
- **Required correction** Briefly state that Eq. (1) follows from differentiating the free-energy density with respect to concentration, and define all symbols explicitly in the text immediately preceding the equation.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section IV.2, training data description
- **Evidence pointer** Section IV.2, "Training data were generated from simulations of random unary and binary mixtures of IDR fragments"
- **Issue** The description of training data generation is too brief. The number of simulations, the range of concentrations sampled, the system sizes, and the equilibration protocols are not specified in the main text. This information is essential for reproducibility and for assessing the statistical quality of the training data.
- **Required correction** Provide these details in the Extended Methods, and summarize the key parameters (e.g., number of simulations, concentration ranges) in the main text.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Section II.4, Figure 3i
- **Evidence pointer** Section II.4, Figure 3i
- **Issue** The text states that the matrix of mean point-mutation distances (Figure 3i) shows that aromatic and charged residues produce the largest perturbations. However, the text does not discuss whether this result is expected from the underlying force field or whether it provides new physical insight beyond what is already known about IDR interactions.
- **Required correction** Briefly contextualize this finding in terms of known IDR interaction chemistry, and state whether the metric space provides any unexpected or non-obvious insights.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Section II.5, Figure 4a through 4c
- **Evidence pointer** Section II.5, Figures 4a through 4c
- **Issue** The comparison between CCA and mutual information analyses is described, but the text does not explain why the two methods yield different rankings of feature importance. The statement that mutual information "reveals additional structure" is vague.
- **Required correction** Provide a brief explanation of why nonlinear dependencies might be missed by CCA and what type of structure the mutual information analysis uncovers.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section II.3, comparison to FINCHES
- **Evidence pointer** Section II.3, "FINCHES performs comparably to the negative control on these benchmarks"
- **Issue** The comparison to FINCHES is presented as a single sentence without context. It is unclear whether FINCHES was designed for the same type of predictions, whether the comparison is fair, and what the implications are for the field.
- **Required correction** Provide a brief description of FINCHES and its intended use, and discuss whether the comparison is appropriate given the different modeling assumptions.

## Risk / unsupported claims
- The claim of "quantitative agreement" with molecular simulations for phase diagrams and EOS predictions is not verifiable from the provided text, as no numerical error metrics or figure panels are visible.
- The claim that IDR mixture thermodynamics is "intrinsically low dimensional" with d approximately 10 is not substantiated with convergence data or robustness analysis.
- The claim that the framework "establishes a general, interpretable foundation" for sequence-dependent phase behavior is broader than the evidence supports, given that only one force field (Mpipi) is used for training and validation.
- The claim that the model "clearly discriminates" WT and MUT mixtures lacks statistical significance testing in the provided text.
- The statement that pairwise models "incur substantial errors" is made without visible quantitative comparison in the provided material.
- The claim that the framework "can incorporate multicomponent experimental data" is presented as a future possibility without evidence of feasibility.