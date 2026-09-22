## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and supplementary figure/table legends.
- **Assessment boundary** Scientific validity, technical soundness, clarity of claims, and alignment with stated conclusions. No assessment of editorial fit or publication decision.
- **Shared manuscript claim summary** The authors identify nuclear RNA-binding proteins that interact with G-quadruplex (G4) RNA structures using a combination of pull-down experiments, mass spectrometry, and computational predictions. They classify proteins based on binding preference for folded versus unfolded G4 RNA, develop a prediction tool (G4-FUNNIES), and propose roles in transcription and phase separation.
- **Visible evidence base** Main text figures 1, 2, 4, 5, 6 (as referenced); supplementary figures 1, 2, 3; supplementary data files 1 through 10; methods section.
- **Missing materials affecting confidence** Raw mass spectrometry data, full lists of identified proteins, detailed statistical outputs, and complete supplementary data files were not provided. The manuscript text references these but they are not accessible for independent verification.

## Reviewer
- **Overall assessment** The manuscript presents a potentially useful resource for predicting G4 RNA-binding proteins and provides experimental data supporting the identification of nuclear G4 interactors. The combination of experimental and computational approaches is commendable. However, several technical concerns regarding data interpretation, validation depth, and methodological clarity limit the strength of the conclusions. The claim of universal physicochemical signatures for G4 binding requires stronger cross-validation. The phase separation link is suggestive but not directly tested.
- **Who would be interested in the results, and why** Researchers studying RNA-binding proteins, G-quadruplex biology, transcriptional regulation, and biomolecular condensates. The G4-FUNNIES tool may be of practical use to the broader RNA biology community. The identification of chromatin-associated G4 binders could interest those working on gene regulation and chromatin structure.
- **Major strengths** 1. The study addresses an under-explored area: nuclear G4 RNA-protein interactions. 2. The combination of experimental pull-down with computational modeling is a reasonable strategy. 3. The development of a publicly accessible prediction tool is a valuable contribution. 4. The inclusion of multiple validation steps, including western blot and RIP, strengthens the core findings.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5.
- **Assessment against Nature-style criteria** **Originality**: Moderate. The concept of predicting G4 RNA-binding proteins is not entirely new, but the nuclear focus and the specific tool are novel. **Scientific importance**: Moderate to high. The findings could inform future studies on G4-mediated regulation, but the functional implications are not fully demonstrated. **Interdisciplinary readership**: The topic bridges RNA biology, structural biology, and computational biology, which may attract a broad audience. **Technical soundness**: Adequate but with notable gaps in validation and methodological detail. **Readability for nonspecialists**: The manuscript is generally well-written, but some sections, particularly the computational methods, may be challenging for non-experts. The abstract is clear and accessible.
- **Recommendation posture** Supportive if technical concerns are resolved. The core experimental data are promising, but the computational claims and the phase separation link require stronger evidence and clearer presentation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that 182 of 283 chromatin-associated RBPs exhibit a preference for folded G4 RNA based on catRAPID predictions (Figure 1c).
- **Evidence pointer** Figure 1c, Supplementary Data 1, Methods section "catRAPID predictions of protein-RNA interactions"
- **Concern** The threshold for classifying a protein as a "preferential binder of folded G4A4" is defined as more than 75% of contacts within each 50-amino-acid fragment showing higher interaction propensities for folded versus unfolded G4A4. This criterion is arbitrary and not justified. The manuscript does not report how sensitive the classification is to this threshold. Additionally, the catRAPID algorithm is used to predict interactions with a specific RNA sequence (G4A4), but the predictions are generalized to all G4 structures. The authors do not validate catRAPID's accuracy for G4 RNA specifically, despite citing a general performance metric (AUC 0.78) from other studies.
- **Why it matters** The central claim that many chromatin-associated proteins prefer folded G4 RNA rests on this computational classification. If the threshold is not robust or the predictions are not accurate for G4 structures, the conclusion may be overstated.
- **Resolution test** Provide a sensitivity analysis showing how the number of predicted G4 binders changes with different thresholds. Validate catRAPID predictions against a subset of experimentally confirmed G4 binders (e.g., NCL) and non-binders. Justify the choice of the 75% threshold with reference to prior work or a statistical rationale.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that proteins enriched in K+ conditions are "bona fide G4RBPs" and that the pull-down assay specifically identifies G4 RNA-binding proteins.
- **Evidence pointer** Figure 2, Methods section "G-quadruplex pull-down"
- **Concern** The pull-down experiment compares K+ (G4-stabilizing) and Li+ (G4-destabilizing) conditions. However, the manuscript does not demonstrate that the differential binding is due specifically to G4 structure rather than to other cation-dependent effects on protein-RNA interactions. The authors use NCL as a positive control, but no negative control (e.g., a known non-G4-binding protein) is shown. The mass spectrometry analysis identifies proteins enriched in K+ versus Li+, but the criteria for "significantly enriched" are not fully described in the main text (only referenced to Methods). The manuscript does not report the number of replicates used for the mass spectrometry beyond stating "in triplicate," nor does it provide a clear list of the 151 K+-enriched and 83 Li+-enriched proteins.
- **Why it matters** The experimental identification of G4RBPs is the foundation for the computational model. If the assay is not specific to G4 structure, the training data for G4-FUNNIES may be contaminated with false positives.
- **Resolution test** Include a negative control protein known not to bind G4 RNA in the western blot validation. Provide a detailed description of the mass spectrometry data analysis, including the statistical thresholds used to define enrichment. Show that the K+/Li+ differential binding is abolished when using a G4-mutant RNA that cannot form the structure.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that G4-FUNNIES can distinguish G4 binders from non-binders based on validation with eCLIP data (Figure 5).
- **Evidence pointer** Figure 5, Methods section "cleverMachine classification of protein sets and G4-FUNNIES"
- **Concern** The validation in Figure 5 uses eCLIP data to show that proteins classified as G4 binders have more G4-containing RNA targets than non-binders. However, the eCLIP data are not specific to G4 RNA; they are general RNA-binding data. The authors use pqsfinder to predict G4 motifs in the eCLIP targets, but this is a computational prediction, not an experimental validation. The manuscript does not report the number of proteins in each class (G4 binder vs. non-binder) used for this analysis, nor does it provide statistical measures beyond a general statement of "positive correlation." The threshold for classifying proteins as G4 binders (score >= -15) is arbitrary and not justified.
- **Why it matters** The claim that G4-FUNNIES has predictive power relies on this validation. If the validation is circular (using computational predictions to validate a computational model) or statistically weak, the tool's utility is not established.
- **Resolution test** Provide a more rigorous validation using an independent experimental dataset of experimentally confirmed G4 binders and non-binders. Report the number of proteins in each class and the statistical significance of the correlation. Justify the score threshold of -15 with a clear rationale or sensitivity analysis.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The authors suggest that predicted G4RBPs are involved in transcription and phase separation, and that G4 RNA binding may mediate localization to membraneless organelles.
- **Evidence pointer** Figure 4e, 4f, Discussion section
- **Concern** The link between G4 binding and phase separation is based on computational predictions (catGRANULE) and correlation with known phase-separated proteins. No experimental evidence is provided to directly test whether G4 RNA binding promotes phase separation. The authors mention that G4 can drive phase separation in other studies, but they do not test this in their system. The claim that G4RBPs are involved in transcription is based on the presence of chromatin-associated proteins in the dataset, but no functional assays are performed to demonstrate a role in transcription.
- **Why it matters** The title and abstract emphasize roles in transcription and phase separation, but the data do not directly support these functional claims. Overstating the implications could mislead readers.
- **Resolution test** Either add experimental data (e.g., phase separation assays with G4 RNA, transcription reporter assays) or temper the claims to reflect that these are predictions based on computational analysis and literature correlation.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that the G3A2 predictor and G4-FUNNIES show "convergence in the physicochemical property patterns" (Supplementary Figure 2).
- **Evidence pointer** Supplementary Figure 2, Methods section "cleverMachine classification of protein sets and G4-FUNNIES"
- **Concern** The manuscript reports that the G3A2 predictor identifies 90% of folded G4 binders and 10% of unfolded ones within the G4A4 dataset, while G4-FUNNIES detects 65% of non-binders and 45% of binders within the G3A2 dataset. These numbers are not clearly explained. It is unclear what "detects" means in this context (e.g., sensitivity, specificity, positive predictive value). The overlap between the two predictors is not quantified in a statistically meaningful way. The manuscript does not explain why the performance metrics differ so substantially between the two directions.
- **Why it matters** The claim of a universal physicochemical signature for G4 binding depends on the consistency between the two predictors. If the cross-validation is weak, the generalizability of the model is questionable.
- **Resolution test** Provide a clear confusion matrix for the cross-validation between the G3A2 and G4A4 datasets. Report sensitivity, specificity, and positive predictive value for each direction. Explain the discrepancies in performance metrics.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, last sentence
- **Issue** The abstract states that G4-FUNNIES is available at a URL, but the URL is not provided in the abstract. It appears only in the Discussion and Methods.
- **Required correction** Include the URL in the abstract or remove the mention from the abstract and keep it in the main text.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "G-quadruplex pull-down"
- **Evidence pointer** Methods section
- **Issue** The manuscript states that "5' biotinylated oligonucleotides were received from Integrated DNA Technologies, or alternatively 3' biotinylation of G-quadruplex forming RNA oligonucleotides was carried out." It is unclear which oligonucleotides were used for which experiments and whether the 5' and 3' biotinylation methods yield comparable results.
- **Required correction** Specify which oligonucleotides were used for the pull-down experiments and whether the biotinylation position affects the results.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 2b
- **Evidence pointer** Figure 2b legend
- **Issue** The legend states that statistical significance was determined by a two-tailed paired t-test (p = 0.032), but the number of independent experiments (n = 4) is only mentioned in the text, not in the legend. The figure legend should include the n number.
- **Required correction** Add the n number to the figure legend.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 6d
- **Evidence pointer** Figure 6d legend
- **Issue** The legend states that statistical significance was estimated using two-way ANOVA with Šídák's multiple comparisons test, but the specific comparisons and their p-values are not shown in the figure or legend.
- **Required correction** Indicate which comparisons are significant and provide the p-values in the figure or legend.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "Data analysis"
- **Evidence pointer** Methods section
- **Issue** The manuscript states that "proteins with less than 70% of valid values in at least one group were filtered out." It is unclear what constitutes a "valid value" and how missing values were handled before this filtering step.
- **Required correction** Clarify the definition of "valid value" and describe the missing value handling procedure.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion
- **Evidence pointer** Discussion, paragraph 3
- **Issue** The statement "G4RBPs can accumulate in membraneless organelles as the nucleolus" is presented as a conclusion, but the data only show a correlation with nucleolar proteins. The wording should be softened to reflect the speculative nature.
- **Required correction** Rephrase to indicate this is a hypothesis or suggestion, not a demonstrated finding.

## Risk / unsupported claims
- The claim that 182 of 283 chromatin-associated RBPs prefer folded G4 RNA is based on an arbitrary threshold in catRAPID predictions and is not experimentally validated.
- The claim that G4-FUNNIES can accurately predict G4-binding propensity is not sufficiently validated with independent experimental data.
- The claim that G4RBPs are involved in phase separation is speculative and not directly tested.
- The claim that G4RBPs play a role in transcription is inferred from the presence of chromatin-associated proteins but not functionally demonstrated.
- The cross-validation between the G3A2 and G4A4 predictors is not clearly quantified, making the claim of a universal physicochemical signature unsubstantiated.