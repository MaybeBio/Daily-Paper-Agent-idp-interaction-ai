## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions, supplementary references)
- **Assessment boundary** Scientific validity, methodological soundness, reproducibility, and claims as supported by the provided evidence
- **Shared manuscript claim summary** The authors present a deep learning framework (G4REP) for predicting human RNA G-quadruplex-binding proteins (RG4BPs), integrating ESM-2 embeddings with an LSTM architecture. They report 84-86% accuracy, apply the model to the human proteome identifying 2160 high-confidence candidates enriched in intrinsically disordered regions and stress granule proteins, and provide a web server for community access.
- **Visible evidence base** Main text sections 1-5, tables referenced as S1-S4, figures referenced as 1-2 and S1-S4, supplementary methods referenced but not provided
- **Missing materials affecting confidence** Supplementary figures and tables (S1-S4, Fig S1-S4), detailed model architecture specifications, hyperparameter settings, full training curves, the length-extreme test set composition, AlphaFold3 confidence metrics, and the complete list of 2160 predicted candidates

## Reviewer

- **Overall assessment** The manuscript addresses a relevant problem in RNA biology and presents a plausible computational approach. The core claim of accurate RG4BP prediction is supported by the reported metrics, but several methodological details and validation steps are insufficiently described to fully assess robustness and generalizability. The proteome-wide application and the stress granule enrichment analysis are interesting, though the biological interpretation relies heavily on correlational evidence. The structural modeling section is preliminary and would benefit from quantitative validation. Overall, the work is potentially useful to the community, but the current evidence base does not fully establish all stated claims.

- **Who would be interested in the results, and why** Researchers studying RNA G-quadruplex biology, RNA-binding proteins, stress granule dynamics, and computational biology. The web server provides a practical tool for experimentalists seeking candidate RG4BPs in their systems of interest. The methodological comparison of encoding strategies and architectures may also interest those developing deep learning approaches for protein function prediction.

- **Major strengths**
  1. The problem is well-motivated and experimentally relevant, addressing a gap in RG4BP identification.
  2. The systematic comparison of five architectures and two encoding strategies is a reasonable model selection approach.
  3. The application to the human proteome and the stress granule analysis provide biologically meaningful context.
  4. The provision of a public web server enhances accessibility and potential community impact.
  5. The disorder enrichment analysis is a sensible validation strategy given known RG4BP properties.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data quality and label reliability
- **Claim pointer** The positive set comprises 1135 sequences from literature and QUADRaTlas, and the negative set 2015 sequences selected based on literature, UniProt annotations, and structural characteristics.
- **Evidence pointer** Section 2.1, Section 3.1
- **Concern** The construction of the training labels is described only superficially. The criteria for defining a protein as an RG4BP from literature sources are not specified, and the negative set selection relies on "thorough literature searches" without clear inclusion or exclusion criteria. The overlap between positive and negative sets, or potential contamination from unannotated RG4BPs in the negative set, is not addressed.
- **Why it matters** Label quality is the foundation of supervised learning. If the negative set contains undiscovered RG4BPs, the model may learn to discriminate based on annotation status rather than biological properties, inflating performance metrics and undermining the validity of proteome-wide predictions.
- **Resolution test** Provide explicit criteria for positive and negative set construction, including literature sources, experimental evidence types, and any manual curation steps. Report the number of proteins excluded at each filtering stage and assess potential contamination by searching the negative set against known RG4BP databases or using sequence similarity to positive set members.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evaluation methodology and generalizability
- **Claim pointer** The best model achieved 84% accuracy on the test set and 86% accuracy in distinguishing RG4BPs from non-binders.
- **Evidence pointer** Section 3.2, Tables S1-S3
- **Concern** The test set is derived from the same homology-reduced clustering procedure as the training set. While this prevents trivial sequence leakage, the manuscript does not report whether the test set was held out before model selection or used iteratively during development. The reported accuracy of 84% on the test set and 86% in the abstract are inconsistent, and the source of this discrepancy is not explained. Additionally, no external validation on independent experimentally derived datasets is presented.
- **Why it matters** Without a clearly held-out test set and external validation, the reported performance may reflect overfitting to the specific data distribution. The inconsistency between abstract and results values raises concerns about reporting rigor.
- **Resolution test** Clarify the exact test set composition and the timing of its use relative to model selection. Reconcile the accuracy discrepancy between abstract and results. Provide external validation on independent RG4BP datasets, such as those from recent experimental screens or curated databases not used in training.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Biological validation and interpretability
- **Claim pointer** The model uncovered 2160 high-confidence RG4BP candidates, many with IDRs and enrichment in stress granule organelles, and structural modeling of FAM98B revealed a cap-like interaction over the G-quadruplex core.
- **Evidence pointer** Section 3.3, Section 3.4, Figure 2A
- **Concern** The proteome-wide predictions are presented as biologically meaningful, but no experimental validation is provided for any of the novel candidates. The AlphaFold3 modeling of FAM98B is qualitative, with no confidence scores, no comparison to known RG4BP structures, and no mutational or binding assays to support the proposed interaction mode. The enrichment of IDRs and stress granule proteins is correlational and does not establish functional relevance.
- **Why it matters** The central claim of "uncovering novel players in RNA regulation" requires at least some experimental or orthogonal computational validation. Without it, the predictions remain speculative, and the structural model, while illustrative, does not constitute evidence of binding.
- **Resolution test** Provide experimental validation for at least a subset of novel candidates, such as pull-down or binding assays for 3-5 predicted RG4BPs. For the structural modeling, report AlphaFold3 confidence metrics (ipTM, pLDDT), compare the predicted complex to known G4-protein structures, and ideally test the effect of mutating key predicted contact residues on binding.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Methodological completeness and reproducibility
- **Claim pointer** The G4REP Score integrates neural network-based disorder profiles and residue-specific compositional biases to localize potential G4-binding regions.
- **Evidence pointer** Section 2.10, Section 3.5, Section 3.6
- **Concern** The mathematical formulation of the G4REP Score is incomplete. The equations are presented without full definitions of all variables, the window size n is not specified, the threshold T is described as "empirically chosen" without reporting its value or selection procedure, and the combination operator Φ is not formally defined. The validation of the score on experimentally mapped RG4-binding regions is limited to two examples, which is insufficient to establish generalizability.
- **Why it matters** Reproducibility is a core requirement for computational tools. Incomplete method descriptions prevent others from implementing or benchmarking the approach, and the limited validation does not support the claim that the score reliably identifies binding regions.
- **Resolution test** Provide complete mathematical definitions, report all parameter values and selection procedures, and validate the G4REP Score on a larger set of experimentally mapped RG4-binding regions, ideally with statistical comparison against a baseline method.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and consistency
- **Affected element** Abstract versus results accuracy values
- **Evidence pointer** Abstract, Section 3.2
- **Issue** The abstract reports 86% accuracy while the results section reports 84% mean accuracy on the test set. This discrepancy is not explained.
- **Required correction** Reconcile the values or clarify whether they refer to different evaluation conditions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Data balancing procedure
- **Evidence pointer** Section 2.3
- **Issue** The balancing procedure is described as "randomly removing only negative sequences," but the number of negatives removed and the final class distribution are not reported.
- **Required correction** Report the number of sequences before and after balancing for each set.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Biological interpretation
- **Affected element** Stress granule analysis
- **Evidence pointer** Section 3.3
- **Issue** The analysis of stress granule proteins uses a "gold standard" set of 473 proteins, but the criteria for this classification and the source database are not described in sufficient detail.
- **Required correction** Provide the version of the RNA Granule Database used and the definition of "gold standard" classification.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Model training
- **Evidence pointer** Section 2.6
- **Issue** The number of epochs varies between 250-1400 for OHE models and 200-400 for ESM-2 models, but early stopping criteria and the final selected epoch for each model are not reported.
- **Required correction** Report early stopping patience, the metric monitored, and the final epoch count for the selected model.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Structural modeling
- **Affected element** AlphaFold3 parameters
- **Evidence pointer** Section 2.8
- **Issue** AlphaFold3 was used with "default parameters," but no details are given on the input preparation, the number of models generated, or the selection criteria for the final model.
- **Required correction** Provide the AlphaFold3 version, input format, and any filtering or ranking steps applied.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Web server
- **Evidence pointer** Section 2.9
- **Issue** The server is described as "freely accessible," but no usage limits, input size restrictions, or expected runtime are mentioned.
- **Required correction** Add practical usage information for prospective users.

## Risk / unsupported claims
- The claim of "comprehensive prediction" of human RG4BPs is not fully supported, as the model was trained on a limited set of known RG4BPs and the negative set construction may introduce bias.
- The statement that the model "uncovered 2160 high-confidence RG4BP candidates" implies biological discovery, but no experimental validation is provided for any candidate.
- The proposed link between RG4 recognition and stress granule assembly is speculative and based on correlational enrichment analysis.
- The AlphaFold3 structural model of FAM98B-RG4 interaction is presented without confidence metrics or experimental support, making the proposed binding mode unverified.
- The G4REP Score is claimed to highlight experimentally defined RG4-binding regions, but validation is limited to two examples, which is insufficient to establish generalizability.
- The claim that ESM-2 embeddings "capture rich biochemical and evolutionary information" is plausible but not directly demonstrated in this study.
- The statement that the model provides "a generalizable, scalable framework" is not supported by tests on diverse protein families or cross-species validation.