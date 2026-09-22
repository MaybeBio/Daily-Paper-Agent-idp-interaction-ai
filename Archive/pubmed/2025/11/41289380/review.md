## Review setup
- **Input scope** Full manuscript text (main text, methods, and supplementary figure/table references as provided)
- **Assessment boundary** Scientific validity, methodological soundness, reproducibility, and claims as supported by the provided evidence
- **Shared manuscript claim summary** The authors present a machine learning protocol (TNT-S transformer architecture) that predicts Cα distance maps and 3D backbone structures of amyloidogenic protein segments from simulated 2D IR spectra. The model is trained on MD-derived conformational ensembles from Aβ42, α-synuclein, hIAPP, and TTR fragments, and is applied to an Aβ42-inhibitor (10074-G5) complex to demonstrate generalization. An attention mechanism is used to interpret spectral features most relevant to structural prediction.
- **Visible evidence base** Main text figures (Fig. 1–4), supplementary figures (S1–S7), supplementary tables (S1–S3), methods section, and data/code availability statements
- **Missing materials affecting confidence** Supplementary figures and tables are referenced but not provided in the submitted material. Experimental 2D IR spectra are not included. Full training/validation/test split details are not provided. Hyperparameter settings, training time, and computational cost are not reported. The gradient-based folding algorithm is referenced but not described in sufficient detail.

## Reviewer
- **Overall assessment** The manuscript presents a potentially useful computational framework for linking 2D IR spectra to protein conformational ensembles. The core idea is timely and the choice of transformer-based architecture is reasonable. However, the evidence provided is insufficient to fully evaluate the method's validity, generalizability, and practical utility. Several technical details are missing, and the validation is entirely based on simulated data, which limits the strength of the claims made. The attention-based interpretation is interesting but its physical significance requires more rigorous demonstration.
- **Who would be interested in the results, and why** Researchers in vibrational spectroscopy, computational biophysics, and protein misfolding diseases would find this work relevant. Those developing machine learning approaches for structural biology and spectral interpretation would also be interested. The potential application to drug design for amyloid diseases may attract a broader audience in chemical biology and medicinal chemistry.
- **Major strengths** The problem addressed is important and timely. The use of a transformer-based architecture for spectral-structural mapping is a modern and appropriate choice. The demonstration of generalization to a protein-ligand complex not included in training is a positive feature. The attention mechanism provides a pathway toward interpretability, which is often lacking in deep learning applications to biophysics.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5
- **Assessment against Nature-style criteria**  
  **Originality** The combination of 2D IR spectroscopy with transformer-based deep learning for structural prediction is novel, though the individual components are established. The application to amyloidogenic segments is a reasonable extension.  
  **Scientific importance** If validated, the method could provide a new route for interpreting 2D IR spectra in terms of conformational ensembles, which would be valuable for studying protein misfolding. However, the current evidence is entirely simulation-based, and the practical impact on experimental studies remains unclear.  
  **Interdisciplinary readership** The work bridges spectroscopy, machine learning, and structural biology, which could attract readers from multiple disciplines. However, the presentation assumes familiarity with both 2D IR spectroscopy and transformer architectures, which may limit accessibility.  
  **Technical soundness** The methodology is plausible but insufficiently detailed for reproduction. The validation is limited to simulated data, and the metrics reported are not benchmarked against existing methods. The attention analysis requires more rigorous statistical support.  
  **Readability for nonspecialists** The manuscript is generally well written, but the methods section is dense and assumes significant background knowledge. The significance statement is clear and accessible.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript has potential, but the technical concerns must be resolved and additional validation (ideally against experimental data) is needed before the claims can be considered supported.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The model achieves an average Cα distance map MAE of 0.93 Å and an average Cα RMSD of 1.87 Å on the independent test set, demonstrating strong generalization capability.
- **Evidence pointer** Fig. 2B, Fig. 2C, SI Appendix Fig. S3, Fig. S4, Table S2
- **Concern** The reported performance metrics are presented as averages across all tested segments, but the variance and per-segment breakdown are not provided in the main text. Without this information, it is impossible to assess whether the model performs uniformly well or whether certain segments are poorly predicted. Additionally, no comparison is made to existing structure prediction methods or simpler baselines, so the added value of the 2D IR-based approach is not established.
- **Why it matters** The central claim of the paper is that the model accurately predicts structural distributions. If performance varies significantly across segments or is not better than existing methods, the claim is weakened. A baseline comparison is essential to justify the complexity of the proposed approach.
- **Resolution test** Provide per-segment performance metrics with standard deviations. Compare the model's performance to at least one established structure prediction method (e.g., AlphaFold, or a simpler spectral inversion approach) on the same test set. Show that the 2D IR-based approach offers a meaningful advantage.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The training dataset consists of 160,910 conformational snapshots from four amyloidogenic proteins, sampled every 10 to 355 femtoseconds from MD simulations.
- **Evidence pointer** Methods, Dataset construction (Fig. 1A), SI Appendix Table S1
- **Concern** The sampling interval range (10 to 355 fs) is unusually wide and the rationale for choosing different intervals for different systems is not explained. More critically, the MD simulation details (force field, water model, temperature, simulation length, equilibration protocol) are not provided in the main text and are only referenced to the SI Appendix, which was not supplied. Without these details, the training data cannot be reproduced or assessed for adequacy of conformational sampling.
- **Why it matters** The quality and representativeness of the training data directly determine the model's validity. If the MD simulations are not well-converged or the sampling is biased, the model may learn artifacts rather than physically meaningful spectral-structural relationships.
- **Resolution test** Provide full MD simulation parameters in the main text or ensure the SI Appendix includes all necessary details. Justify the choice of sampling intervals for each system. Demonstrate that the conformational ensembles are converged (e.g., via block analysis or multiple independent runs).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The model successfully captured dynamic conformational transitions induced by ligand binding in the Aβ42-10074-G5 complex, with MAE of 1.00 Å and RMSD of 1.57 Å for the 17-23 segment, and MAE of 0.37 Å and RMSD of 0.69 Å for the 37-42 segment.
- **Evidence pointer** Fig. 3, SI Appendix Fig. S6, Fig. S7
- **Concern** The application to the ligand-bound complex is presented as a demonstration of generalization, but the model was trained on monomeric segments only. The physical basis for expecting the spectral-structural mapping learned from monomers to transfer to a ligand-bound state is not discussed. Moreover, the reported errors for the ligand-bound case are not compared to the errors on the monomeric test set, so it is unclear whether the model's performance degrades in this new context. The selection of the five time points (t1–5) is described as "uniformly selected," but the criteria for choosing these specific points are not given.
- **Why it matters** The claim of generalization to ligand-bound states is a key selling point of the paper. If the model's accuracy in this context is significantly worse than on the training distribution, the claim of generalization is overstated. The lack of comparison to monomeric performance makes this impossible to evaluate.
- **Resolution test** Provide a direct comparison of model performance on the ligand-bound complex versus the monomeric test set. Discuss the physical rationale for transferability. Justify the selection of time points and show that the results are robust to this choice.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The attention mechanism identifies spectral features most indicative of local folding transitions, and the attention maps exhibit a systematic shift toward lower vibrational frequencies near 1,650 cm⁻¹, consistent with α-helix formation.
- **Evidence pointer** Fig. 4, SI Appendix Table S3
- **Concern** The attention analysis is presented as providing mechanistic insights, but the statistical significance of the observed attention patterns is not established. It is unclear whether the attention shifts are consistent across multiple time points or runs, or whether they could arise from noise. The claim that the model has learned a "physically meaningful mapping" is a strong interpretation that requires more rigorous validation. For example, the authors could test whether the attention maps correlate with known spectral markers of secondary structure in a quantitative manner.
- **Why it matters** The interpretability of the model is a major claimed contribution. If the attention analysis is not statistically robust, the mechanistic insights derived from it are unreliable. This would undermine the paper's contribution to understanding spectral-structural relationships.
- **Resolution test** Provide quantitative analysis of attention map consistency across multiple runs or time points. Correlate attention weights with known secondary structure markers (e.g., amide I frequency shifts) using a statistical test. Show that the attention patterns are not artifacts of the model architecture.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The model's predicted distance maps are converted to 3D structures via a gradient-based folding algorithm.
- **Evidence pointer** Methods, Machine Learning Protocol
- **Concern** The gradient-based folding algorithm is referenced (36, 37) but not described in the main text. The details of how distance maps are converted to 3D coordinates, the objective function used, and the constraints applied are essential for reproducibility. Without this information, the structural reconstruction step cannot be evaluated or reproduced.
- **Why it matters** The final output of the model is a 3D structure, and the folding algorithm is a critical component of the pipeline. If this step is not well-described, the entire method is not reproducible, which is a fundamental requirement for a computational methods paper.
- **Resolution test** Provide a full description of the gradient-based folding algorithm in the main text or SI Appendix, including the objective function, constraints, and any parameters. Ideally, provide code or a detailed pseudocode.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Dataset construction
- **Evidence pointer** Fig. 1A, Methods
- **Issue** The description of the dataset construction mentions "uniform sampling" with intervals of 10 to 355 femtoseconds, but the rationale for this range is unclear. The term "uniform" is ambiguous in this context.
- **Required correction** Clarify the sampling strategy and justify the choice of intervals for each system.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Model evaluation
- **Evidence pointer** Fig. 2, SI Appendix Table S2
- **Issue** The manuscript reports average MAE and RMSD values but does not provide confidence intervals or error bars. It is unclear how stable these metrics are across different random seeds or initializations.
- **Required correction** Report standard deviations or confidence intervals for the performance metrics, ideally across multiple model training runs.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Attention analysis
- **Evidence pointer** Fig. 4
- **Issue** The attention maps are described as showing a "systematic shift" toward lower frequencies, but the figure is not provided in the submitted material. It is difficult to assess this claim without seeing the actual maps.
- **Required correction** Ensure the figure clearly shows the attention maps and the frequency shift. Consider adding a quantitative measure of the shift.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Data availability
- **Evidence pointer** Data, Materials, and Software Availability
- **Issue** The data and code are deposited in Zenodo and GitHub, but the manuscript does not specify the license or version of the code. This is important for reproducibility and reuse.
- **Required correction** Specify the software license and provide a versioned release of the code.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion claims the framework is "expected to be broadly applicable beyond amyloid-forming systems," but no evidence is provided to support this speculation.
- **Required correction** Either temper this claim or provide a brief justification based on the physicochemical properties of the segments studied.

## Risk / unsupported claims
- The claim that the model "demonstrates that it is possible to accurately interpret 2D IR spectra" is not fully supported, as all validation is performed on simulated spectra with no experimental comparison.
- The claim that the attention mechanism provides "mechanistic insights" into spectral-structural relationships is not statistically validated.
- The claim of broad applicability beyond amyloid-forming systems is speculative and not supported by the presented data.
- The performance metrics (MAE 0.93 Å, RMSD 1.87 Å) are presented without comparison to existing methods, making it impossible to assess whether the approach offers a meaningful improvement.
- The generalization to ligand-bound states is claimed but not rigorously compared to monomeric performance, and the physical rationale for transferability is not discussed.