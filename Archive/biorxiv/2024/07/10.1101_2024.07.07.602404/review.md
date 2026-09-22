## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract, with reference to cited prior work
- **Shared manuscript claim summary** The authors propose a deep learning (multilayer perceptron) model trained on Brownian dynamics simulation-derived gyration radii for ~6500 intrinsically disordered protein sequences, claim 97% accuracy on 33 test IDPs, and use the model to predict gyration radii for all missense mutations, identifying mutation-prone regions validated by targeted simulations, with a reported 10^4 to 10^6-fold computational speedup.
- **Visible evidence base** Abstract text; no figures, tables, methods details, or simulation parameters are provided beyond the abstract.
- **Missing materials affecting confidence** Full manuscript, training/validation data splits, model architecture details, hyperparameters, simulation protocol specifics, mutation enumeration methodology, validation simulation results, statistical error bars, and comparison to baseline methods.

## Reviewer
- **Overall assessment** The abstract presents a potentially useful computational pipeline for prioritizing missense mutations in IDPs based on predicted changes in gyration radius. However, the evidence provided is insufficient to assess the robustness of the claimed 97% accuracy, the generalizability of the model, the biological relevance of the identified mutation-prone regions, and the validity of the speedup claim. The work is of interest to the IDP and computational biology communities, but the current abstract does not establish the case without additional technical details and validation.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, protein misfolding diseases, and computational mutagenesis; developers of machine learning tools for biophysical property prediction; and clinicians or pharmaceutical scientists interested in rapid variant prioritization for therapeutic targeting.
- **Major strengths** The combination of physics-based simulation (HPS2 model) with deep learning is a pragmatic approach to address the computational cost of exhaustive mutation screening. The use of a large training set (~6500 sequences) from a public database (MobiDB) is a reasonable foundation. The explicit claim of computational speedup (10^4 to 10^6-fold) is a clear and testable metric.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
  - R1-M4
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1 (accuracy claim), R1-M2 (mutation enumeration), R1-M3 (validation scope), R1-M4 (speedup claim)
- **Assessment against Nature-style criteria** 
  - Originality: Moderate. The use of DL to predict gyration radii from sequence is not entirely new, but the specific application to exhaustive missense mutation screening in IDPs is a novel angle.
  - Scientific importance: Potentially high for IDP biology and variant interpretation, but the abstract does not demonstrate biological or clinical impact beyond a computational prediction.
  - Interdisciplinary readership: The work bridges biophysics, machine learning, and molecular biology, which could attract a broad audience if the claims are substantiated.
  - Technical soundness: Not assessable from the abstract alone. The 97% accuracy figure lacks context (e.g., error bars, baseline comparisons, overfitting checks).
  - Readability for nonspecialists: The abstract is generally clear, but terms like "HPS2 model" and "gyration radii" may require prior knowledge. The speedup claim is accessible.
- **Recommendation posture** Currently not established from the provided evidence. The abstract is promising, but the core claims require full manuscript details and additional validation before the case is convincing.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "we develop a multilayer perceptron neural net (NN) architecture that predicts the gyration radii of 33 IDPs previously studied using BD simulation with 97% accuracy"
- **Evidence pointer** Abstract, location not provided
- **Concern** The 97% accuracy claim is presented without defining the metric (e.g., R^2, mean absolute error, percentage within a threshold), the number of test sequences (33) is small, and there is no mention of cross-validation, train/test leakage, or comparison to a baseline model. The abstract does not state whether the 33 IDPs were excluded from the training set of ~6500 sequences.
- **Why it matters** A high accuracy on a small, potentially non-representative test set does not guarantee generalizability to the broader IDP sequence space, especially for mutation prediction where the model must extrapolate to unseen variants.
- **Resolution test** Provide the exact accuracy metric, error bars, a description of the train/test split (including whether the 33 IDPs were held out), and a comparison to a simple baseline (e.g., sequence-length-based prediction or a linear model). Show a scatter plot of predicted vs. simulated gyration radii for the test set.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "we utilize this NN to predict gyration radii of every permutation of missense mutations in IDPs"
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract does not specify how "every permutation" is defined. For a protein of length L, the number of single missense mutations is 19L, but the abstract implies all permutations, which could mean all possible single, double, or higher-order mutations. The computational feasibility of enumerating all permutations for IDPs of length 20-300 is not discussed, and the model's input features (sequence and HPS parameters) may not capture the effect of multiple simultaneous mutations.
- **Why it matters** The scope of the mutation search space directly affects the claimed speedup and the biological relevance of the results. If only single mutations are considered, the claim of "every permutation" is misleading.
- **Resolution test** Clearly define the mutation set (e.g., all single missense mutations, or a specific subset). Provide the total number of mutations evaluated and the computational time for the DL prediction vs. BD simulation for a representative IDP.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** "Our approach successfully identifies mutation-prone regions that induce significant alterations in the radius of gyration when compared to the wild-type IDP sequence. We further validate the prediction by running BD simulations on the subset of identified mutants."
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract does not define what constitutes a "significant alteration" in gyration radius (e.g., a threshold in percentage change or absolute difference). The validation subset size and the agreement between predicted and simulated changes are not reported. Without this, the claim of successful identification is unsubstantiated.
- **Why it matters** The biological relevance of the method hinges on whether predicted large structural changes are confirmed by simulation. If the validation is limited or shows poor agreement, the method's utility for disease-related mutation identification is questionable.
- **Resolution test** Specify the threshold for "significant alteration," report the number of mutants selected for validation, and provide a correlation or error metric between predicted and simulated gyration radii for the validation set.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "The neural network yields a (10^4 − 10^6)-fold faster computation in the search space for potentially harmful mutations."
- **Evidence pointer** Abstract, location not provided
- **Concern** The speedup claim is not contextualized. It is unclear whether this compares the DL prediction time to BD simulation time for a single mutation, or the total time to screen all mutations. The abstract does not account for the training time of the NN, which could be substantial, nor the time to generate the training data via BD simulation.
- **Why it matters** A speedup claim that ignores training and data generation costs is misleading for practical applications. The actual end-to-end time savings for a new IDP sequence may be much smaller.
- **Resolution test** Provide a breakdown of computational time: (a) BD simulation for one sequence, (b) NN prediction for one mutation, (c) total time to screen all mutations for a representative IDP, and (d) training time for the NN. Clarify whether the speedup is for inference only or includes amortized training costs.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract text
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract uses "∼ 6500" and "20 − 300" without defining the range notation clearly. The use of "⟨ R g ⟩" is standard but may be unclear to non-specialists.
- **Required correction** Define the notation explicitly, e.g., "approximately 6500 sequences with lengths ranging from 20 to 300 amino acids" and "average radius of gyration (⟨R_g⟩)".

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Model description
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract mentions "the corresponding parameters from the HPS model" but does not specify which parameters (e.g., interaction strengths, temperature) are used as input features.
- **Required correction** List the specific HPS model parameters used as input features in the full manuscript, and state whether they are fixed or sequence-dependent.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Claims of disease relevance
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract states "substantial implications for rapid identification and understanding diseases related to missense mutations" but provides no example or link to a specific disease or known pathogenic mutation.
- **Required correction** Add a brief example or reference to a disease-associated IDP mutation that the method correctly identifies, or temper the claim to be more speculative.

## Risk / unsupported claims
- The 97% accuracy claim is unsupported without a defined metric, error bars, and test set details.
- The claim of identifying "mutation-prone regions" is unsupported without a definition of significance and validation results.
- The speedup claim (10^4 to 10^6-fold) is unsupported without a clear comparison methodology and consideration of training/data generation costs.
- The extension to "accurate predictions of other mutation effects" is speculative and not evidenced in the abstract.
- The biological and clinical implications are overstated given the lack of demonstrated disease relevance.