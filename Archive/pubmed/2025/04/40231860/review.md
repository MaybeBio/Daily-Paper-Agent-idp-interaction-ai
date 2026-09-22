## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) as provided by the author
- **Assessment boundary** Scientific and technical soundness of the proposed deep ensemble docking pipeline, validity of the reported results, and support for the stated conclusions
- **Shared manuscript claim summary** The authors present a computational pipeline combining AlphaFold-Metainference ensemble generation, binding site detection and filtering, molecular docking, and multilabel QSAR classification to screen for small molecule binders targeting the partially disordered protein AR-V7. They report identification of 41 functional binding sites, a 17-fold improvement in multibinding site hit rate versus naive docking, and a specific compound (ChEMBL22003) that modulates AR-V7 conformational dynamics in atomistic simulations.
- **Visible evidence base** Full text including methods, results, discussion, and conclusions; references to supplementary figures and tables (S1–S16, Tables S1–S2) are made but their content is not provided
- **Missing materials affecting confidence** Supplementary figures and tables (S1–S16, Tables S1–S2) are referenced but not included; GitHub repository with screening results is mentioned but not accessible; no experimental validation data; no code or model parameters provided

## Reviewer
- **Overall assessment** The manuscript presents a methodologically interesting and potentially useful computational pipeline for targeting partially disordered proteins, with AR-V7 as a relevant and timely test case. The integration of ensemble generation, binding site reduction, and machine learning acceleration is conceptually sound and addresses a genuine bottleneck in structure-based drug discovery for disordered targets. However, the evidence provided is insufficient to fully establish the central claims. Key limitations include the lack of accessible validation data, the absence of a rigorous comparison against established methods, the questionable biological relevance of the selected binding sites, and the limited scope of the molecular dynamics analysis. The manuscript would benefit from substantial additional validation and clarification before the claims can be considered fully supported.

- **Who would be interested in the results, and why** Computational chemists and structural biologists working on intrinsically disordered proteins and their role in disease would find the methodological framework relevant. Researchers in the drug discovery community, particularly those focused on transcription factors and cancer targets such as AR-V7, would be interested in the potential for identifying modulators of phase separation. The machine learning community working on QSAR and virtual screening may also find the multilabel classification approach of interest.

- **Major strengths**
  1. The problem addressed is significant and timely: targeting partially disordered proteins is a recognized challenge in drug discovery, and AR-V7 is a clinically relevant target in castration-resistant prostate cancer.
  2. The pipeline is well-structured and integrates multiple established computational techniques in a logical workflow.
  3. The use of AlphaFold-Metainference to generate structural ensembles is a reasonable and increasingly accepted approach.
  4. The reduction of binding sites from thousands to 41 through physicochemical and dynamics-based filters is a sensible strategy to make the problem tractable.
  5. The comparison between naive docking and the screened set showing improved hit rates is a useful demonstration of the method's potential.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that the identified binding sites are "functionally relevant" and located at "phase separation-prone regions that have been experimentally shown to contribute to enhanced transcription activity and the onset of tumor growth."
- **Evidence pointer** Results and Discussion, "Binding Site Selection"; Figure 2; Table S2 (not provided)
- **Concern** The claim of functional relevance rests on the identification of binding sites in regions predicted to be phase separation-prone. However, the evidence linking these specific binding sites to experimentally validated functional regions is indirect. The authors reference NMR data for a truncated AR-V7 variant (WT*) but acknowledge that a one-to-one comparison with the full-length protein is difficult. The FuzDrop predictions are computational and not experimentally validated. The criteria for selecting binding sites (RMSF, hydropathy, volume) are reasonable but their relationship to functional relevance is not established.
- **Why it matters** The entire premise of the pipeline is to target functionally relevant sites. If the binding sites are not demonstrably functional, the significance of the screening results is substantially weakened.
- **Resolution test** Provide direct evidence that the identified binding sites overlap with experimentally validated functional regions, such as known interaction interfaces, post-translational modification sites, or regions demonstrated to be critical for phase separation in cellular or in vitro assays. Alternatively, provide experimental validation showing that compounds binding to these sites modulate AR-V7 function.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the multilabel QSAR model can "swiftly screen" a larger chemical space and that the screened set shows a 17-fold improvement in multibinding site hit rate compared to naive docking.
- **Evidence pointer** Results and Discussion, "Deep Learning Multilabel Classification Model"; Figures 4 and 5; Table S1 (not provided)
- **Concern** The evaluation of the QSAR model is incomplete. The authors report MCC values but do not provide sufficient detail on model selection, hyperparameter tuning, or the variability of performance across different train/test splits. The comparison between naive docking and screened docking is based on a single screening round, and the statistical significance of the 17-fold improvement is not established. The threshold of 70% of binding sites for selecting hits appears arbitrary and its impact on the results is not discussed. Furthermore, the model is trained on docking energies from a single docking program (AutoDock Vina), which may introduce systematic bias.
- **Why it matters** The claimed acceleration and improved hit rate are central to the method's utility. Without rigorous evaluation and statistical analysis, the superiority of the approach over naive docking is not convincingly demonstrated.
- **Resolution test** Provide a more comprehensive evaluation of the QSAR model, including cross-validation results, confidence intervals for performance metrics, and an analysis of the impact of the 70% threshold. Compare the screened set against a properly matched control set using appropriate statistical tests. Ideally, validate the model on an independent set of compounds with experimentally known activity.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that ChEMBL22003 is a "potential AR-V7 phase separation modulator" based on the observation that its presence reduces conformational entropy and alters solvent exposure of LLPS-prone regions.
- **Evidence pointer** Results and Discussion, "Structural Ensemble Modulation of AR-V7 by ChEMBL22003"; Figure 6; Figure S4 (not provided)
- **Concern** The molecular dynamics analysis is based on a single compound and a limited set of starting configurations (33 out of 41). The reported entropy differences, while statistically significant, are small (0.08 and 0.15 kJ/mol·K) and their biological relevance is unclear. The solvent-accessible surface area changes are reported as averages without measures of variance. The convergence of the PB-MetaD simulations is referenced to Figure S4 but this figure is not provided. Most critically, no experimental validation is presented to support the claim that ChEMBL22003 actually modulates phase separation in a biological context.
- **Why it matters** The claim of phase separation modulation is the most significant biological conclusion of the study. Without experimental evidence, this remains a purely computational prediction with uncertain relevance.
- **Resolution test** Provide experimental data demonstrating that ChEMBL22003 modulates AR-V7 phase separation, for example using in vitro phase separation assays, cellular imaging, or transcriptional activity assays. At minimum, provide a more thorough computational analysis including multiple compounds, longer simulation times, and a clear demonstration of convergence.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that the backmapped structures have "on average, 10% Ramachandran outliers (PDB threshold 0.05%), poor rotamers 2.34% (PDB threshold 0.3%), and bad angles 3.2% (PDB threshold 0.1%)" and attribute these to "model predictions rather than structure determination."
- **Evidence pointer** Methods, "Backmapping"; Figure S3 (not provided)
- **Concern** The reported structural quality metrics are far outside acceptable ranges for high-quality structures. While the authors acknowledge this, the implications for the downstream docking and MD results are not discussed. Poor quality structures could lead to inaccurate binding site detection and docking results. The authors do not address whether the specific regions with poor geometry overlap with the identified binding sites.
- **Why it matters** The reliability of the entire pipeline depends on the quality of the input structures. If the backmapped structures are of poor quality, the subsequent results may be compromised.
- **Resolution test** Provide a detailed analysis of the structural quality, including a comparison of the backmapped structures to the original coarse-grained structures and an assessment of whether the poor geometry regions affect the identified binding sites. Consider using alternative backmapping methods or energy minimization protocols to improve structural quality.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods, "Machine Learning"
- **Evidence pointer** Location not provided
- **Issue** The description of the QSAR model training is incomplete. The authors do not specify the exact architecture of the neural network, the optimization algorithm, the learning rate, the number of epochs, or the batch size. The process for oversampling the active molecules is also not described in detail.
- **Required correction** Provide a complete description of the model architecture and training procedure, including all hyperparameters and the oversampling strategy.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "Molecular Docking"
- **Evidence pointer** Location not provided
- **Issue** The docking protocol is not fully specified. The authors do not state the exhaustiveness setting for AutoDock Vina, the search space dimensions, or the number of poses generated per compound per binding site.
- **Required correction** Provide complete docking parameters to ensure reproducibility.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results and Discussion, "Structural Ensemble Modulation of AR-V7 by ChEMBL22003"
- **Evidence pointer** Figure 6
- **Issue** The description of the solvent-accessible surface area analysis is unclear. The authors report average ratios but do not specify how these were calculated or what statistical test was used to assess significance.
- **Required correction** Clarify the methodology for the SASA analysis and provide statistical details.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Conclusions
- **Evidence pointer** Location not provided
- **Issue** The conclusions section does not discuss the limitations of the study, such as the lack of experimental validation, the potential biases in the computational methods, or the generalizability of the approach to other partially disordered proteins.
- **Required correction** Add a limitations paragraph to provide a balanced perspective on the findings.

- **Technical failings that need to be addressed before the case is established**
  1. Lack of accessible validation data: The supplementary figures and tables are referenced but not provided, and the GitHub repository is not accessible. This prevents independent verification of the results.
  2. Incomplete evaluation of the QSAR model: The model performance is not rigorously assessed, and the statistical significance of the claimed improvement is not established.
  3. Insufficient evidence for functional relevance of binding sites: The link between the identified binding sites and experimentally validated functional regions is indirect.
  4. Limited molecular dynamics analysis: The analysis is based on a single compound and the biological relevance of the observed changes is unclear.
  5. Poor structural quality of backmapped models: The reported quality metrics are far outside acceptable ranges and the implications are not discussed.

- **Assessment against Nature-style criteria**
  - **Originality**: The combination of ensemble generation, binding site reduction, and machine learning acceleration for targeting partially disordered proteins is a novel contribution. The application to AR-V7 is timely and relevant. However, the individual components are established techniques, and the novelty lies primarily in their integration.
  - **Scientific importance**: The problem of targeting partially disordered proteins is of significant importance in drug discovery. If the method is validated, it could have broad applicability. However, the current evidence is insufficient to establish the method's utility beyond the specific test case.
  - **Interdisciplinary readership**: The work bridges computational chemistry, machine learning, and structural biology, and would appeal to researchers in these fields. The clinical relevance to prostate cancer adds to its potential appeal.
  - **Technical soundness**: The technical approach is generally sound, but there are significant gaps in the evaluation and validation. The lack of accessible data and the incomplete description of methods hinder a full assessment.
  - **Readability for nonspecialists**: The manuscript is generally well-written and accessible, with clear explanations of the methods and results. However, some sections, particularly the machine learning and MD descriptions, may be challenging for nonspecialists.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript presents a promising methodological framework, but the central claims are not fully supported by the evidence provided. The lack of accessible validation data, the incomplete evaluation of the QSAR model, and the absence of experimental validation for the phase modulation claim are significant gaps. The authors should be encouraged to resubmit after addressing these concerns, particularly by providing the supplementary data, conducting a more rigorous evaluation, and either providing experimental validation or tempering the claims accordingly.