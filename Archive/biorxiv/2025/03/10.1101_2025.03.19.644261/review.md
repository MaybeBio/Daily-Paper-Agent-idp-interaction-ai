## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results and discussion, methods, data availability, competing interests, acknowledgements)
- **Assessment boundary** Scientific content, methodological soundness, evidence quality, and claims as presented in the provided text
- **Shared manuscript claim summary** The authors present a coarse-grained molecular dynamics model compatible with CALVADOS for simulating phosphorylated disordered proteins. They parameterise the model using experimental data on global dimensions of phosphorylated IDRs, find that the dominant effect of phosphorylation on chain compaction is electrostatic (additional negative charge), with a smaller contribution from altered hydropathy, and propose the model for studying phosphorylation effects on phase separation and proteome-scale properties.
- **Visible evidence base** Abstract, Introduction, Results and Discussion (partial), Methods (partial), Data and Code Availability, Competing Interests, Acknowledgements
- **Missing materials affecting confidence** Full Results and Discussion section (only section headings and partial text visible), all figures and tables, all supplementary information (Tables S1–S8, Figures S1–S4), detailed methods for experimental data collection and analysis, simulation protocols beyond basic parameters, statistical analysis details

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important problem: enabling coarse-grained simulations of phosphorylated intrinsically disordered proteins within the CALVADOS framework. The top-down parameterisation strategy is appropriate and consistent with the philosophy of the original CALVADOS model. The central claim that charge effects dominate the conformational response to phosphorylation is plausible and consistent with prior work. However, the provided text is incomplete, with the Results and Discussion section largely missing, and no figures or tables available for inspection. The parameterisation dataset is small (9 proteins, 11 phosphorylation states), and the decision to optimise a single shared Δλ parameter for both pSer and pThr, while pragmatic, may limit the model's accuracy. The comparison with phosphomimetics is conceptually useful but the presented results are preliminary. The manuscript would benefit from additional validation, including tests against data not used in parameterisation, and a more detailed discussion of the limitations of the single-parameter approach. The writing is clear and accessible, and the work is likely to be of interest to the IDP simulation community.

- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, coarse-grained molecular dynamics simulation, post-translational modification biology, and biomolecular phase separation. The model provides a practical tool for simulating phosphorylated IDRs at scale, which is relevant for understanding signalling networks, transcriptional regulation, and condensate biology. The methodological approach of top-down parameterisation against experimental data will also interest computational biophysicists developing transferable coarse-grained models.

- **Major strengths** The work addresses a clear gap in the CALVADOS modelling framework. The top-down parameterisation strategy is well-motivated and consistent with the model's development philosophy. The authors are transparent about the limitations of their dataset and the single-parameter simplification. The comparison with phosphomimetics provides a useful benchmark for understanding the physical basis of phosphorylation effects. The model is made available through open-source code, which will facilitate adoption.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence completeness
  - **Claim pointer** The manuscript claims that the parameterised model improves agreement with experimental data on phosphorylation-induced changes in chain dimensions.
  - **Evidence pointer** Figures 2A–D, S1–S3, Table S6; location not provided in the visible text
  - **Concern** The core evidence for the model's performance is presented in figures and tables that are not included in the provided material. Without access to the parameter scan results, the comparison between Δλ = 0.0 and Δλ = −0.37, and the per-protein breakdown of model performance, the central claim of improved agreement cannot be evaluated.
  - **Why it matters** The entire parameterisation strategy rests on the demonstration that the chosen Δλ value improves agreement with experiment. Without the actual data, the reader cannot assess the quality of the fit, the magnitude of the improvement, or whether the choice of Δλ = −0.37 is well-supported or arbitrary.
  - **Resolution test** Provide the full parameter scan figure, the comparison between models, and the per-protein error analysis. The improvement in agreement should be quantified with appropriate error metrics and, ideally, statistical significance testing.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Validation adequacy
  - **Claim pointer** The manuscript claims the model can be applied to study phosphorylation effects on phase separation and proteome-scale properties.
  - **Evidence pointer** Conclusion section; location not provided
  - **Concern** The model is parameterised and tested only against single-chain global dimensions (Rg) for a small set of 9 proteins. No validation is presented for phase separation behaviour, multi-chain systems, or proteome-scale predictions. The claim of applicability to these contexts is speculative.
  - **Why it matters** Coarse-grained models that perform well for single-chain properties do not necessarily transfer to phase separation predictions, which depend on multi-chain interactions and are sensitive to the balance of attractive and repulsive interactions. The authors themselves note that the model does not capture local structural changes, which may be relevant for some phosphorylation effects.
  - **Resolution test** Provide at least one demonstration of the model's performance in a context beyond single-chain Rg, such as a phase separation prediction for a phosphorylated IDR compared to experiment, or a proteome-scale analysis with clear benchmarks.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Parameterisation robustness
  - **Claim pointer** The manuscript claims that a single shared Δλ parameter for both pSer and pThr is sufficient to capture phosphorylation effects on chain dimensions.
  - **Evidence pointer** Methods, Parameterisation section; location not provided
  - **Concern** The decision to optimise a single Δλ for both pSer and pThr is a strong simplification. The authors acknowledge this but do not provide a thorough discussion of its consequences. The chemical differences between pSer and pThr (e.g., the extra methyl group in pThr) may lead to different hydropathy changes upon phosphorylation, and a single shared parameter may not capture these differences.
  - **Why it matters** If the model is to be used for quantitative predictions, the accuracy of the per-residue parameters matters. A single shared parameter may introduce systematic errors for proteins enriched in one residue type over the other. The authors note that a two-parameter fit was not attempted due to limited data, but the implications of this choice are not fully explored.
  - **Resolution test** Provide a sensitivity analysis showing how model predictions change with different Δλ values for pSer and pThr separately, or a discussion of the expected magnitude of the difference based on chemical reasoning or available data.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Dataset adequacy
  - **Claim pointer** The manuscript claims the dataset of 9 proteins with 11 phosphorylation states is sufficient for parameterisation.
  - **Evidence pointer** Results, Dataset section; location not provided
  - **Concern** The dataset is small and heterogeneous, comprising proteins of different lengths, sequence compositions, and degrees of phosphorylation. The authors exclude one dataset (CPPAGE4) due to high experimental error, further reducing the effective sample size. The diversity of the dataset in terms of sequence context around phosphorylation sites is not discussed.
  - **Why it matters** A small dataset limits the generalisability of the parameterisation. The model may be biased toward the specific proteins in the training set and may not perform well for IDRs with different sequence features. The lack of discussion of sequence context effects is a gap, as the local environment of a phosphorylation site may influence its conformational impact.
  - **Resolution test** Provide a more detailed characterisation of the dataset, including sequence diversity metrics, and discuss the potential for overfitting. If possible, include a leave-one-out cross-validation analysis.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Abstract
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The abstract states the model is "compatible with the CALVADOS protein simulation model" but does not specify which version of CALVADOS is used. The conclusion mentions "CALVADOS 2" but the abstract is ambiguous.
  - **Required correction** Specify the CALVADOS version in the abstract for clarity.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods, CALVADOS simulations
  - **Evidence pointer** Methods section; location not provided
  - **Issue** The methods state that "approximately 5000 independent frames" were collected per system, but the method for determining statistical independence of frames is not described.
  - **Required correction** Describe the method used to assess frame independence (e.g., autocorrelation analysis, block averaging).

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Results and Discussion
  - **Evidence pointer** Results and Discussion section; location not provided
  - **Issue** The Results and Discussion section is largely missing from the provided text, with only section headings and a few paragraphs visible. This makes it impossible to evaluate the full argument.
  - **Required correction** Provide the complete Results and Discussion section for full evaluation.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Technical accuracy
  - **Affected element** Methods, Parameterisation
  - **Evidence pointer** Methods section; location not provided
  - **Issue** The text states "p K a ≈ 6 ( Eq. 7 )" and "p K a = 6.01 for pSer and p K a = 6.30 for pThr" in different places. The relationship between these values is unclear, and the equation numbering is not visible.
  - **Required correction** Clarify the source of the pKa values and ensure consistency between the text and equations.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Presentation
  - **Affected element** Data and Code Availability
  - **Evidence pointer** Data and Code Availability section; location not provided
  - **Issue** The GitHub repository link is provided, but there is no statement about the license under which the code is released.
  - **Required correction** Add a software license statement to the repository and manuscript.

- **Technical failings that need to be addressed before the case is established** R1-M1 (missing evidence for model performance), R1-M2 (lack of validation beyond single-chain properties)

## Risk / unsupported claims
- The claim that the model can be applied to study phase separation of phosphorylated IDRs is unsupported by any data presented in the provided text.
- The claim that the model can be applied at proteome scale is plausible but unsupported by any demonstration in the provided text.
- The claim that the effect of phosphorylation on chain dimensions is "mostly driven by the additional charge" is supported only by the comparison with the charge model, but the quantitative details of this comparison are not visible.
- The claim that Δλ = −0.37 is the optimal value is not verifiable without the parameter scan data.
- The statement that the model "will be useful" for various applications is forward-looking and not a claim requiring evidence, but the basis for this expectation is not fully established.