## Review setup
- **Input scope** Full manuscript text (abstract/summary only provided)
- **Assessment boundary** The provided summary text; no figures, tables, methods, or supplementary materials were supplied
- **Shared manuscript claim summary** The authors report a proteome-wide analysis of interactions between transactivation domains (TADs) and arginine-glycine-rich (RG/RGG) regions, combining interaction mapping, sequence annotation, coarse-grained simulations, machine learning prediction, and NMR validation. They claim a predominantly electrostatic mode of association and present a quantitative framework for prioritizing TF-RBP partnerships.
- **Visible evidence base** Summary text only; no experimental details, numerical results, figures, or statistical analyses were provided
- **Missing materials affecting confidence** All figures, tables, methods sections, supplementary data, NMR spectra, simulation parameters, machine learning model details, and validation statistics

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question in gene regulation: how intrinsically disordered regions in transcription factors and RNA-binding proteins mediate direct physical coupling. The proposed workflow, from proteome-scale annotation to biophysical validation, is ambitious and potentially impactful. However, based solely on the summary, the evidence base is insufficient to evaluate the robustness of the claims. The central conclusions rest on computational predictions and a small NMR validation set, but no quantitative details, error estimates, or controls are visible. The manuscript may represent a valuable contribution, but the case is not established from the provided material.
- **Who would be interested in the results, and why** Researchers in transcriptional regulation, RNA biology, intrinsically disordered proteins, and biophysical modeling would find these results relevant. The proposed framework for predicting TF-RBP interactions from sequence features could be of practical use to experimentalists seeking candidate partnerships. The work also speaks to the broader community interested in the role of disordered regions in cellular signaling and phase separation.
- **Major strengths** The question is well motivated and addresses a gap in understanding TF-RBP coupling through disordered regions. The combination of multiple approaches, from proteome-wide annotation to coarse-grained simulation to machine learning and NMR validation, is methodologically ambitious. The focus on interpretable sequence features is commendable and could yield broadly applicable rules.
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
- **Assessment against Nature-style criteria** Originality is high, as the systematic mapping of TAD-RG/RGG interactions at proteome scale appears novel. Scientific importance is potentially substantial, given the central role of TF-RBP coupling in gene expression. Interdisciplinary readership is plausible, spanning genomics, biophysics, and computational biology. Technical soundness cannot be assessed from the summary alone, as no quantitative validation or controls are visible. Readability for nonspecialists is adequate in the summary, though the density of methods may challenge general readers. Overall, the work has strong potential but requires full evidence to meet the standards of a high-impact venue.
- **Recommendation posture** Currently not established from the provided evidence. The authors should be invited to submit the full manuscript for a complete review, as the summary alone does not permit a fair assessment of the technical claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that coarse-grained simulations (CALVADOS) quantify interaction propensities and indicate that association is primarily driven by electrostatic complementarity and charge patterning.
- **Evidence pointer** Summary text; location not provided
- **Concern** The summary states that simulations "indicate" a predominantly electrostatic mechanism, but no quantitative results, comparison to experimental data, or error analysis are presented. It is unclear how many TAD-RGG pairs were simulated, what the range of predicted affinities was, and how robust the conclusions are to simulation parameters or force field choices.
- **Why it matters** The central mechanistic claim of the paper rests on the simulation results. Without quantitative evidence, the reader cannot judge whether the electrostatic conclusion is well supported or an artifact of the chosen model.
- **Resolution test** Provide simulation results for all representative pairs, including predicted interaction free energies or affinities, comparison to experimental values, and sensitivity analysis to model parameters. Show that the electrostatic conclusion holds across a diverse sequence set.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that a hybrid machine-learning model predicted simulated interaction strengths from a compact, interpretable set of features and extrapolated these rules to the full combinatorial space.
- **Evidence pointer** Summary text; location not provided
- **Concern** No details are given on the machine learning model architecture, training data size, feature set, cross-validation strategy, or prediction accuracy. The claim of extrapolation to the full combinatorial space is particularly strong and requires demonstration that the model generalizes beyond the training distribution.
- **Why it matters** The predictive framework is a key deliverable of the paper. If the model is overfit or poorly validated, the prioritization of candidate TF-RBP couplings would be unreliable.
- **Resolution test** Provide model performance metrics on held-out test sets, describe the feature set and model selection procedure, and demonstrate that extrapolation to unseen sequence space is validated against independent experimental data.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that NMR titration experiments on a subset of TAD-RGG pairs showed agreement between predicted affinities and NMR-derived dissociation constants.
- **Evidence pointer** Summary text; location not provided
- **Concern** The summary states agreement but provides no numerical values, number of pairs tested, range of affinities, or statistical measures of agreement. It is unclear whether the agreement is qualitative or quantitative and whether the validation set is sufficiently diverse to support the general claims.
- **Why it matters** Experimental validation is the strongest evidence for the predictive framework. Without quantitative details, the reader cannot assess the strength of the validation or whether the model performs well only for a narrow sequence range.
- **Resolution test** Provide a table of predicted versus measured dissociation constants for all tested pairs, including error estimates, and a statistical analysis of the correlation or agreement.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The authors claim to define 230 RG/RGG-binding TAD-like segments across 190 TFs and map 1,008 compact RG/RGG regions across 823 RBPs based on proteome-wide motif spacing.
- **Evidence pointer** Summary text; location not provided
- **Concern** The criteria for defining TAD-like segments and compact RG/RGG regions are not described. The thresholds for sequence grammar, motif spacing, and the definition of "compact" are essential for reproducibility and for interpreting the biological significance of the numbers.
- **Why it matters** The proteome-wide annotation is the foundation of the entire analysis. If the criteria are arbitrary or poorly justified, the subsequent network analysis and predictions would be built on unstable ground.
- **Resolution test** Provide a detailed description of the annotation criteria, including all thresholds and their justification, and demonstrate that the results are robust to reasonable variations in these parameters.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Network analysis
- **Evidence pointer** Summary text; location not provided
- **Issue** The summary mentions "network analysis reveals a global enrichment of RBP partners among TF interactions" but does not specify the statistical test or the magnitude of the enrichment.
- **Required correction** Provide the statistical framework and effect size for the enrichment claim.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Sequence stickiness
- **Evidence pointer** Summary text; location not provided
- **Issue** The term "sequence stickiness" is introduced without definition or quantitative measure.
- **Required correction** Define the metric used to quantify stickiness and explain how it was calculated.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Scope of validation
- **Evidence pointer** Summary text; location not provided
- **Issue** The summary states that NMR validation was performed on "a subset" of pairs but does not indicate how this subset was selected or whether it covers the full predicted affinity range.
- **Required correction** Describe the selection criteria for the validation set and confirm that it spans the dynamic range of predicted affinities.

## Risk / unsupported claims
- The claim that interactions are "primarily driven by electrostatic complementarity and charge patterning" is unsupported without quantitative simulation data and experimental comparison.
- The claim of "systematic prioritization of candidate TF-RBP couplings" is unsupported without model validation metrics.
- The claim of "agreement between predicted affinities and NMR-derived dissociation constants" is unsupported without numerical values.
- The proteome-wide numbers (230 TAD-like segments, 1,008 RG/RGG regions) are unverifiable without the annotation criteria.
- The network-level enrichment of RBP partners among TF interactions is unverifiable without statistical details.