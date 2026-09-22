## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors present an integrated method combining small-angle neutron scattering (SANS) under full contrast and contrast-matching conditions with residue-specific deuterium labeling, microsecond all-atom molecular dynamics (MD) simulations using four force fields, and an autoencoder-based deep learning (DL) algorithm to characterize the structural ensemble of a complex formed by two intrinsically disordered regions (IDRs). They report that selective deuteration provides additional information, that a99SB-disp and CHARMM36m show strongest agreement with SANS and NMR experiments, that their DL algorithm complements conventional analysis and differentiates NMR and MD structures indistinguishable on the free energy surface, and that a final ensemble describes experimental data better than any single-force-field MD ensemble, revealing three distinct conformational clusters.
- **Visible evidence base** Abstract text only; no quantitative results, methodological details, or experimental validation are provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, SANS data and fitting details, MD simulation parameters and convergence criteria, DL architecture and training details, NMR data and comparison metrics, ensemble selection methodology, and any statistical or error analysis

## Reviewer
- **Overall assessment** The abstract describes a potentially valuable integrated approach for characterizing IDP/IDR structural ensembles, combining complementary experimental and computational techniques. The concept of using contrast-matching SANS with selective deuteration to constrain MD ensembles is scientifically interesting and timely. However, the abstract provides insufficient quantitative evidence to evaluate the validity of the central claims. Key assertions regarding force field performance, DL algorithm capabilities, and ensemble quality are presented without supporting metrics, error estimates, or comparisons to established methods. The work may be of interest to the structural biology and computational biophysics communities, but the case is not established from the abstract alone.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins and regions, particularly those interested in structural ensemble characterization; computational biophysicists developing and benchmarking force fields for disordered systems; method developers in small-angle scattering with contrast variation; and researchers applying deep learning to structural biology problems. The integrated approach could provide a template for combining multiple experimental and computational data types.
- **Major strengths** The integration of multiple complementary techniques is conceptually strong and addresses a real challenge in IDP structural biology. The use of residue-specific deuterium labeling with contrast-matching SANS is a sophisticated experimental design that could provide unique constraints. The systematic comparison of four force fields is a useful contribution. The application of an autoencoder-based DL approach to differentiate structures that are indistinguishable on the free energy surface is an innovative idea.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
  - R1-M4
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** Originality: The integrated use of contrast-matching SANS with selective deuteration combined with MD and DL is novel in its specific combination, though each component technique is established. Scientific importance: The problem of characterizing IDP ensembles is significant, and improved methods would be valuable, but the abstract does not demonstrate a clear advance over existing approaches. Interdisciplinary readership: The work bridges neutron scattering, molecular dynamics, and machine learning, which could appeal to multiple communities, but the abstract is too brief to convey the technical depth required. Technical soundness: Cannot be assessed from the abstract; no quantitative validation or error analysis is presented. Readability for nonspecialists: The abstract is reasonably clear for a technical audience but assumes familiarity with SANS contrast matching, force fields, and autoencoders.
- **Recommendation posture** Currently not established from the provided evidence. The approach is promising and the abstract suggests potentially valuable results, but the absence of quantitative support for the central claims prevents a supportive recommendation. Full manuscript review would be required to assess technical soundness.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that a99SB-disp and CHARMM36m show the strongest agreement with SANS and NMR experiments among the four force fields.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract states this finding without any quantitative metrics, such as chi-squared values, root-mean-square deviations, or statistical comparison against the other two force fields. No error bars or confidence intervals are provided.
- **Why it matters** This is a central comparative claim that would guide force field selection for IDP simulations. Without quantitative support, the reader cannot assess whether the differences between force fields are meaningful or within experimental uncertainty.
- **Resolution test** Provide quantitative agreement metrics for all four force fields against SANS and NMR data, including statistical significance tests or at least error estimates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that selective deuteration provides additional information that helps characterize structural ensembles.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract does not specify what additional information was obtained, how it changed the ensemble characterization, or how it was quantified. The claim is presented as a conclusion without supporting data.
- **Why it matters** This is a key methodological contribution of the work. If selective deuteration does not meaningfully constrain the ensemble, the added experimental complexity may not be justified. The claim needs to be substantiated with a direct comparison of ensembles derived with and without the contrast-matching data.
- **Resolution test** Show a quantitative comparison of ensemble properties or experimental agreement with and without inclusion of the contrast-matching SANS data.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that their DL algorithm successfully differentiates NMR and MD structures which are indistinguishable on the free energy surface.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract provides no details on the DL architecture, training data, validation procedure, or the nature of the differentiation. It is unclear what "differentiates" means in this context, whether it is classification accuracy, clustering, or some other metric. No performance measures are given.
- **Why it matters** This is a novel claim that could have broad implications for how structural ensembles are analyzed. Without validation details, the claim is not assessable and could be an artifact of the specific implementation.
- **Resolution test** Provide DL model details, training and test set descriptions, and quantitative performance metrics such as classification accuracy, precision, recall, or area under the curve.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that their final ensemble describes experimental SANS and NMR data better than MD ensembles generated by a single force field and reveals three clusters of distinct conformations.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract does not specify how the final ensemble was constructed, what "better" means quantitatively, or how the three clusters were identified and validated. No comparison metrics or cluster validation statistics are provided.
- **Why it matters** This is the culminating claim of the work. Without quantitative comparison to single-force-field ensembles and evidence that the three clusters are robust and meaningful, the claim cannot be evaluated.
- **Resolution test** Provide quantitative agreement metrics for the final ensemble versus each single-force-field ensemble, and cluster validation measures such as silhouette scores or bootstrap analysis.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract wording
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "characterizing structural ensembles of intrinsically disordered proteins (IDPs) and intrinsically disordered regions (IDRs) of proteins is essential for studying structure–function relationships" is a broad statement that could be more specific about what aspects of structure-function relationships are addressed.
- **Required correction** Clarify the specific structure-function question being addressed, such as binding, folding upon interaction, or post-translational modification.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Abstract methodology description
- **Evidence pointer** Abstract, methods description
- **Issue** The abstract mentions "microsecond all-atom molecular dynamics (MD) simulations with four molecular mechanics force fields" but does not name the other two force fields beyond a99SB-disp and CHARMM36m.
- **Required correction** Name all four force fields in the abstract or state that the other two are described in the full text.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Abstract DL description
- **Evidence pointer** Abstract, DL algorithm description
- **Issue** The abstract refers to "an autoencoder-based deep learning (DL) algorithm" without specifying the input features, output representation, or how it was trained and validated.
- **Required correction** Provide at least a brief description of the DL input and output, or refer to a methods section with full details.

## Risk / unsupported claims
- The claim that selective deuteration provides additional information is unsupported without a direct comparison of ensembles with and without contrast-matching data.
- The claim that a99SB-disp and CHARMM36m show the strongest agreement with SANS and NMR is unsupported without quantitative metrics.
- The claim that the DL algorithm differentiates NMR and MD structures is unsupported without performance metrics and validation details.
- The claim that the final ensemble describes experimental data better than single-force-field ensembles is unsupported without quantitative comparison.
- The claim of three distinct conformational clusters is unsupported without cluster validation.
- The overall claim of demonstrating "a new integrated approach" is not assessable from the abstract alone, as the novelty and utility depend on the technical details and results presented in the full manuscript.