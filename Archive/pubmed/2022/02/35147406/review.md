## Review setup
- **Input scope** Full manuscript text (abstract, experimental procedures, results, discussion) as provided
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims based solely on the supplied material
- **Shared manuscript claim summary** The authors describe a computational-experimental pipeline to identify small-molecule ligands for the intrinsically disordered protein tau. They report structure-activity relationships for a lead aggregation inhibitor (compound 1) and characterize a fibril-binding compound (compound 6) that does not alter aggregation kinetics. They estimate the fibril-binding affinity of compound 6 using a novel equilibrium model and discuss implications for targeting disordered proteins.
- **Visible evidence base** Abstract; Experimental Procedures (Chemicals, Protein Expression and Purification, Aggregation Assays, Tyrosine Fluorescence Assays, Determination of compound 6 concentrations, Gel Densitometry, Computational Docking, Estimating Fibril-binding Affinity); Results; Discussion; references to Supplementary Figures S1–S6 and Supplementary Table 1
- **Missing materials affecting confidence** Supplementary figures and tables (S1–S6, Table 1) are referenced but not provided; raw data for aggregation assays, dose-response curves, gel densitometry scans, and compound 6 absorbance measurements are not available; no compound synthesis or purity characterization data are shown; no negative control data for compound 6 in the absence of protein are shown in the main text

## Reviewer
- **Overall assessment** The manuscript presents a useful extension of prior work identifying tau ligands, with a clear SAR study around a lead aggregation inhibitor and a novel quantitative treatment of fibril-binding affinity for a non-inhibitory ligand. The conceptual distinction between passive fibril binders and active aggregation inhibitors is valuable. However, several technical aspects require clarification and additional data before the central claims can be considered fully established. The affinity estimate for compound 6 relies on a model with assumptions that are only partially validated, and the SAR conclusions are based on a small number of analogs without detailed binding or structural characterization. The computational docking results are presented qualitatively and are not rigorously compared with experimental outcomes. Overall, the work is of interest to the tau and protein-misfolding communities, but the evidence as presented is not yet sufficient to fully support all claims.

- **Who would be interested in the results, and why** Researchers studying tau aggregation and neurodegeneration, particularly those interested in small-molecule modulators of intrinsically disordered proteins. The work may also appeal to medicinal chemists exploring SAR approaches for challenging targets, and to biophysicists developing quantitative binding models for ligand-fibril interactions. The distinction between fibril binders and aggregation inhibitors could inform future drug discovery strategies for tauopathies.

- **Major strengths** The manuscript addresses an important and difficult problem, namely ligand discovery for intrinsically disordered proteins. The SAR approach around compound 1 is logical and provides useful information about which structural features are important for activity. The development of a quantitative model to estimate fibril-binding affinity from depletion measurements is conceptually interesting and could be broadly applicable. The use of orthogonal methods (ThT, tyrosine fluorescence, gel densitometry) to validate aggregation outcomes is commendable. The authors are appropriately cautious about the limitations of their affinity estimate and the uncertainty in Ks.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that compound 6 binds to tau fibrils with an affinity of Kf = 0.31 μM (95% CI: 0.21–1.0 μM), based on the model described in equations 1–6.
- **Evidence pointer** Methods section "Estimating Fibril-binding Affinity"; Results section; Figure 4 (referenced but not shown)
- **Concern** The affinity estimate depends critically on the model assumptions, including that equilibrium is reached, that binding to soluble species is negligible or accounted for, and that the measured depletion of compound 6 from solution is entirely due to fibril binding. The authors state that the resolution of the data was insufficient to determine Ks, yet the model requires simultaneous fitting of Ks and Kf. The resampling protocol is described but the underlying data (Figure 4) are not shown, and the sensitivity of the Kf estimate to the assumed value of Ks is not discussed. Without this information, the confidence interval for Kf may be misleading.
- **Why it matters** The central claim that compound 6 is a potent fibril binder with nanomolar affinity is a key result of the paper. If the model is not robust to assumptions or if the data do not strongly constrain Kf, the claim is not established.
- **Resolution test** Provide the raw data for the depletion experiments (Figure 4), show the fitted curves and residuals, and perform a sensitivity analysis varying Ks over a plausible range. Demonstrate that Kf is well-constrained by the data and that the confidence interval is robust to model assumptions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that compounds 1.4, 1.5, and 1.7 have notable and consistent activity in inhibiting tau aggregation, and that compound 1.7 shows a direct dose-response relationship.
- **Evidence pointer** Results section; Figure 2 (referenced but not shown); Supplementary Figures 1–3
- **Concern** The dose-response data for compounds 1.4 and 1.5 are described as "somewhat less consistent," yet these compounds are still grouped with compound 1.7 as having notable activity. The criteria for "notable and consistent" activity are not defined. The orthogonal validation (tyrosine fluorescence, gel densitometry) is only mentioned for compounds 1, 1.4, 1.5, and 1.7 collectively, and it is unclear whether all compounds were tested in all assays. Without the actual dose-response curves and quantitative endpoints, the SAR conclusions regarding which structural features are critical for activity are not well supported.
- **Why it matters** The SAR analysis is a primary contribution of the paper. If the activity assignments are not robust or are based on inconsistent data, the conclusions about which molecular features are important for inhibition are unreliable.
- **Resolution test** Provide the full dose-response data for all compounds, including the less active analogs, with quantitative endpoints (e.g., IC50 values or extent of inhibition at a fixed concentration). Show the orthogonal validation data for each compound individually. Define the criteria for "notable" activity.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that the computational docking results predicted most compounds to bind in a similar position as compound 1 with good docking scores, and that this information suggests targeting segments 3 and 21 may lead to more active compounds.
- **Evidence pointer** Results section; Supplementary Table 1 (not provided)
- **Concern** The docking results are presented only qualitatively. No docking scores are given, and the relationship between predicted binding poses and experimental activity is not systematically analyzed. The claim that targeting segments 3 and 21 is a useful strategy is speculative without a clear correlation between predicted binding sites and observed activity across the compound series.
- **Why it matters** The computational predictions are used to rationalize the SAR results and to propose future directions. If the docking data are not presented or analyzed rigorously, this part of the argument is not testable.
- **Resolution test** Provide the docking scores for all compounds, show the predicted binding poses for active versus inactive compounds, and perform a statistical comparison of docking scores between active and inactive compounds. Discuss whether the predicted binding sites correlate with experimental activity.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that compound 6 and its analogs increase ThT fluorescence but do not affect the amount of aggregation, as shown by gel densitometry.
- **Evidence pointer** Results section; Figure 5 (referenced but not shown)
- **Concern** The mechanism by which compound 6 amplifies ThT fluorescence is not investigated beyond the statement that it is "likely a photophysical effect." The possibility that compound 6 binds to ThT itself, or that the fluorescence enhancement is due to an interaction with soluble oligomers rather than fibrils, is not excluded. The gel densitometry data are mentioned but not shown, and it is unclear whether this method is sufficiently sensitive to detect small changes in aggregation.
- **Why it matters** The classification of compound 6 as a "passive fibril binder" rather than an aggregation inhibitor depends on the demonstration that it does not affect aggregation. If the orthogonal method is not adequately sensitive or if the mechanism of fluorescence enhancement is not understood, this classification is not secure.
- **Resolution test** Provide the gel densitometry data for compound 6 and its analogs. Perform control experiments to test whether compound 6 interacts with ThT directly. Use additional orthogonal methods (e.g., sedimentation assay, electron microscopy) to confirm that aggregation is unaffected.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the procedure "efficiently identifies active small-molecule ligands for disordered proteins" but does not quantify the efficiency or compare it to conventional methods.
- **Required correction** Provide a quantitative comparison or temper the claim to reflect the specific context of this study.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "Chemicals"
- **Evidence pointer** Methods section "Chemicals"
- **Issue** Compound purity and source details are only given in Supplementary Table 1, which is not provided. Purity is critical for interpreting biological activity.
- **Required correction** State purity information in the main text or ensure the supplementary table is available for review.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Methods, "Estimating Fibril-binding Affinity"
- **Evidence pointer** Methods section "Estimating Fibril-binding Affinity"
- **Issue** The resampling protocol is described but the number of experimental replicates and the level of noise in the data are not stated.
- **Required correction** Report the number of replicates and the noise level used in the resampling protocol.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The statement that "the activity and structure of the ligands guides our understanding of their interactions without the need for high resolution representations" is somewhat overstated, as the SAR data are limited and no direct binding data are presented.
- **Required correction** Soften the claim or provide additional supporting evidence.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, compound 6 analogs
- **Evidence pointer** Results section; Figure 5 (referenced but not shown)
- **Issue** The three analogs of compound 6 are mentioned but not described in terms of their structural relationship to the parent compound.
- **Required correction** Briefly describe the structural differences between compound 6 and its analogs.

## Risk / unsupported claims
- The claim that compound 6 binds tau fibrils with Kf = 0.31 μM is not fully supported without the raw data and sensitivity analysis (R1-M1).
- The claim that compounds 1.4, 1.5, and 1.7 are "notable" inhibitors is not quantitatively supported without dose-response data and defined criteria (R1-M2).
- The claim that targeting segments 3 and 21 is a promising strategy is speculative without a rigorous analysis of docking results (R1-M3).
- The claim that compound 6 and its analogs do not affect aggregation is not fully supported without showing the gel densitometry data and excluding alternative mechanisms (R1-M4).
- The statement that the computational approach was "more quickly and with less expense" than conventional methods is not supported by any comparative data.
- The relevance of the cryo-EM fibril structures to the docking predictions is discussed but not quantitatively assessed; the single RMSD value for segment 21 is presented without context or statistical significance.