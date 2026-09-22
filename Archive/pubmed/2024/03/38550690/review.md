## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, data availability, and supplementary figure/table references.
- **Assessment boundary** Scientific validity, methodological soundness, reproducibility, and claims as presented in the provided manuscript text. No external validation or replication was performed.
- **Shared manuscript claim summary** The author presents a differentiable molecular simulation (DMS) approach to jointly optimise 108 parameters of the a99SB-disp force field and GBNeck2 implicit solvent model, producing a new force field (GB99dms) that improves agreement with experimental data for disordered proteins and amyloid peptide aggregation, while showing slightly reduced performance on folded proteins and complexes.
- **Visible evidence base** Figures 1–5 (described in text), Tables S1–S2 (referenced), supplementary Figure S1 (referenced), and methodological descriptions in the Methods section. No raw data, trajectories, or code were inspected.
- **Missing materials affecting confidence** Actual figure content, supplementary tables and figures, training and validation trajectories, code implementation details, and exact numerical results (e.g., Rg values, secondary structure percentages, correlation coefficients) are not available for direct verification.

## Reviewer
- **Overall assessment** This manuscript presents a technically ambitious and novel application of differentiable simulation to optimise a molecular mechanics force field for disordered proteins. The core idea is timely and the results, as described, suggest meaningful improvements over existing implicit solvent models for IDPs. However, several technical details and validation aspects require clarification or additional evidence to fully establish the claims, particularly regarding the robustness of the training procedure, the statistical significance of improvements, and the practical utility of the force field for the intended applications.
- **Who would be interested in the results, and why** Researchers in computational chemistry, biophysics, and molecular dynamics simulation, especially those working on intrinsically disordered proteins, implicit solvent models, force field development, and differentiable programming applied to scientific computing. The work also has potential relevance for drug discovery efforts targeting IDPs.
- **Major strengths** 1. Novel application of DMS to a practically important problem (implicit solvent force fields for IDPs). 2. Joint optimisation of a large parameter set (108 parameters) across multiple interaction terms. 3. Demonstration of improved agreement with experimental data for IDPs and aggregation behaviour. 4. Open availability of the force field, code, and data. 5. Honest reporting of degraded performance on folded proteins.
- **Major Concerns** 
  - R1-M1: Training procedure robustness and generalisability
  - R1-M2: Statistical significance and uncertainty quantification of reported improvements
  - R1-M3: Validation of the differentiable simulation approach and gradient accuracy
  - R1-M4: Practical utility and transferability of GB99dms
- **Minor Comments** 
  - R1-m1: Clarification of the "modified backbone O–H interaction term" omission
  - R1-m2: Details on the choice of training proteins and potential biases
  - R1-m3: Reporting of computational costs and efficiency gains
  - R1-m4: Discussion of limitations and potential failure modes
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3 (as detailed below)
- **Assessment against Nature-style criteria** 
  - **Originality** High. The application of DMS to force field optimisation for IDPs is novel and represents a significant methodological advance.
  - **Scientific importance** High. Improving implicit solvent models for IDPs has broad implications for studying these biologically important proteins, which are challenging to simulate with explicit solvent.
  - **Interdisciplinary readership** Moderate to high. The work bridges machine learning, molecular simulation, and biophysics, and should appeal to researchers in all three areas.
  - **Technical soundness** Moderate. The approach is conceptually sound, but several technical details (training stability, gradient accuracy, statistical validation) require further evidence to be fully convincing.
  - **Readability for nonspecialists** Good. The manuscript is clearly written and the key concepts are explained well, though some familiarity with MD and force fields is assumed.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the results are encouraging, but the manuscript requires additional evidence and clarification to fully establish the robustness and generalisability of the approach.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Differentiable molecular simulations with 5 ns trajectories are used to jointly optimise 108 parameters to better match explicit solvent trajectories."
- **Evidence pointer** Methods section, Figure 1A, Table S1
- **Concern** The training procedure relies on 5 ns simulations, which are short relative to the timescales of conformational changes in disordered proteins. The manuscript does not provide evidence that the optimised parameters are stable across different initial conditions, random seeds, or longer simulation times. Additionally, the choice of 5 epochs and the stopping criteria are not justified.
- **Why it matters** If the optimised parameters are not robust to training details or simulation length, the force field may not be transferable to other systems or conditions, limiting its practical utility.
- **Resolution test** Provide additional training runs with different random seeds and initial parameter perturbations to demonstrate convergence to similar parameter sets. Show that the optimised parameters produce consistent results in longer simulations (e.g., 100 ns or 1 μs) for the training proteins and a held-out validation set.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigour
- **Claim pointer** "Simulations with the improved force field better reproduce the radius of gyration and secondary structure content seen in experiments."
- **Evidence pointer** Figures 2, 3, and 4 (described in text)
- **Concern** The manuscript reports improvements in Rg and secondary structure content but does not provide quantitative measures of uncertainty or statistical significance. It is unclear whether the differences between GB99dms and the baseline force fields are within the variability of the simulations or the experimental measurements. The number of replicates and the variability across replicates are not reported.
- **Why it matters** Without uncertainty quantification, it is difficult to assess whether the reported improvements are meaningful or could arise from stochastic variability in the simulations.
- **Resolution test** Report the mean and standard deviation (or confidence intervals) of Rg and secondary structure content across multiple independent simulations for each force field. Perform statistical tests (e.g., t-tests or bootstrap) to compare GB99dms with the baselines. If possible, compare with experimental uncertainties.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "This work is the first to show that gradients can be obtained directly from nanosecond-length differentiable simulations of biomolecules."
- **Evidence pointer** Methods section, Discussion section
- **Concern** The manuscript claims to be the first to obtain gradients from nanosecond-length differentiable simulations, but the evidence for the accuracy and reliability of these gradients is limited. The gradient noise, the effect of the stochastic Langevin integrator, and the potential for biased gradients due to the short simulation length are not thoroughly discussed. The comparison of gradient directions (80% same sign, correlation > 0.85) is mentioned but not shown in detail.
- **Why it matters** If the gradients are noisy or biased, the optimisation may converge to suboptimal parameter sets, and the approach may not be reliable for other applications.
- **Resolution test** Provide a more detailed analysis of gradient quality, including the distribution of gradient magnitudes, the effect of simulation length on gradient accuracy, and a comparison with gradients obtained from longer simulations or alternative methods (e.g., finite differences). Show that the optimisation is robust to gradient noise.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Applicability
- **Claim pointer** "GB99dms, which can be used in OpenMM, is available at https://github.com/greener-group/GB99dms."
- **Evidence pointer** Data availability section
- **Concern** While the force field is made available, the manuscript does not provide guidance on the range of systems for which GB99dms is expected to be reliable. The degraded performance on folded proteins and complexes is acknowledged, but the boundaries of applicability (e.g., protein size, sequence composition, temperature range) are not discussed.
- **Why it matters** Users need to know when GB99dms is appropriate to use and when it may produce unreliable results, especially for systems that are not similar to the training set.
- **Resolution test** Provide a more detailed characterisation of the performance of GB99dms across a broader range of systems, including different protein sizes, sequence compositions, and simulation conditions. Discuss potential limitations and recommend best practices for users.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section
- **Evidence pointer** Methods section, first paragraph
- **Issue** The manuscript states that the "modified backbone O–H interaction term" from a99SB-disp is omitted, but the rationale for this omission and its potential impact on the results are not explained.
- **Required correction** Provide a brief explanation for why this term was omitted and whether this choice was tested or justified.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodology
- **Affected element** Training set selection
- **Evidence pointer** Results section, Figure 1B
- **Issue** The choice of training proteins (4 folded, 4 disordered) is described, but the criteria for selecting these specific proteins are not given. It is unclear whether they are representative of the broader population of IDPs and folded proteins.
- **Required correction** Justify the selection of training proteins, including considerations of sequence diversity, structural coverage, and relevance to the intended applications.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Computational cost
- **Evidence pointer** Methods section, Discussion section
- **Issue** The manuscript mentions that the Julia code is 100–1000× slower than optimised codes when gradients are required, but the total computational cost of training (e.g., GPU-hours) is not reported.
- **Required correction** Report the total computational cost of training and validation, which will help readers assess the practical feasibility of the approach.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion section
- **Evidence pointer** Discussion section, final paragraph
- **Issue** The discussion of limitations is brief and does not address potential failure modes of the DMS approach, such as the risk of overfitting to the training data or the sensitivity of the results to the choice of loss function.
- **Required correction** Expand the discussion of limitations, including potential overfitting, sensitivity to hyperparameters, and the generalisability of the approach to other force fields and solvent models.

## Risk / unsupported claims
- The claim that GB99dms "reproduces the results of a small molecule binding study" is based on a single example (α-synuclein with fasudil) and may not be generalisable to other IDP-ligand systems.
- The claim that GB99dms "improves agreement with experiment for the aggregation of amyloid peptides" is based on a single peptide system (Aβ16–22) and may not be representative of other amyloidogenic peptides.
- The statement that "the current case of optimising 108 parameters is around the crossover point" for DMS versus finite differences is speculative and not supported by a systematic comparison.
- The claim that "gradients can be obtained directly from nanosecond-length differentiable simulations" is presented as a first, but the practical utility of such short simulations for force field optimisation is not fully established.