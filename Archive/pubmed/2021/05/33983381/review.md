## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors propose a neural network model, named Droppler, that predicts the outcome of in vitro protein liquid-liquid phase separation (LLPS) experiments under specified experimental conditions (e.g., concentration, pH, temperature). The model is intended to reduce the experimental search space for identifying LLPS-prone proteins. The authors report experimental validation of Droppler's predictions on the TAR DNA-binding protein (TDP-43) across different conditions, claiming consistency between predictions and experimental outcomes.
- **Visible evidence base** Abstract text only; no quantitative results, model architecture details, dataset descriptions, or validation metrics are provided
- **Missing materials affecting confidence** Full manuscript, model implementation details, training and test datasets, performance metrics, experimental protocols for TDP-43 validation, and supplementary information

## Reviewer
- **Overall assessment** The abstract presents a potentially useful computational tool for predicting LLPS behavior under varying experimental conditions, addressing a real bottleneck in the field. However, the evidence provided in the abstract is insufficient to evaluate the model's predictive accuracy, generalizability, or the robustness of the experimental validation. The claims are plausible but not substantiated from the supplied material.
- **Who would be interested in the results, and why** Researchers studying phase separation in biology, particularly those interested in proteome-scale screening of LLPS-prone proteins, and computational biologists developing predictive models for biomolecular condensates. The tool could aid in prioritizing experimental conditions and reducing costly and time-consuming in vitro assays.
- **Major strengths** The problem addressed is timely and relevant, as LLPS is a rapidly growing area with significant functional implications. The idea of incorporating experimental conditions as inputs to a predictive model is practical and could have broad utility. The inclusion of experimental validation on a disease-relevant protein (TDP-43) is a positive step toward demonstrating real-world applicability.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3
- **Minor Comments**  
  - R1-m1  
  - R1-m2
- **Technical failings that need to be addressed before the case is established** The abstract lacks any quantitative performance metrics (e.g., accuracy, sensitivity, specificity, AUC) for the model's predictions. Without these, the predictive power of Droppler cannot be assessed. The experimental validation on TDP-43 is described only qualitatively as showing "consistency," with no details on the number of conditions tested, the range of conditions, or how consistency was measured. The model's generalizability to other proteins is not demonstrated, and the abstract does not specify the training data composition or how the model handles the combinatorial complexity of conditions.
- **Assessment against Nature-style criteria**  
  - Originality: The concept of condition-aware LLPS prediction is not entirely novel, as prior computational tools exist for LLPS prediction, but the explicit focus on predicting experimental outcomes under varying conditions may offer a new angle. However, the abstract does not clearly differentiate Droppler from existing methods.  
  - Scientific importance: The potential to reduce experimental burden in LLPS screening is significant, but the importance is contingent on demonstrated predictive accuracy, which is not provided.  
  - Interdisciplinary readership: The topic bridges computational biology and biophysics, and the abstract is written in a way that is accessible to a broad biological audience, though technical details are lacking.  
  - Technical soundness: Cannot be evaluated from the abstract alone. The model architecture is mentioned as "multi-head neural attention," but no details on training, validation, or performance are given.  
  - Readability for nonspecialists: The abstract is clear and concise, with minimal jargon, making it accessible to nonspecialists in computational methods.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a promising idea, but the lack of quantitative results and detailed validation prevents a supportive recommendation. The case would be strengthened by providing performance metrics and a more detailed description of the experimental validation.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The model "can be used to rapidly screen proteins and experimental conditions searching for LLPS, thus reducing the search space that needs to be covered experimentally."  
- **Evidence pointer** Abstract, Results section; location not provided  
- **Concern** The abstract claims the model is useful for screening, but no quantitative evidence of predictive performance is presented. There are no metrics such as accuracy, precision, recall, or area under the ROC curve, nor any comparison to existing LLPS prediction tools.  
- **Why it matters** Without performance metrics, the claim that the model can effectively reduce experimental search space is unsupported. A model with low predictive accuracy could mislead experimental design and waste resources.  
- **Resolution test** Provide quantitative performance metrics on a held-out test set, including comparisons to baseline or existing methods, and demonstrate that the model's predictions are significantly better than random or heuristic approaches.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Validation rigor  
- **Claim pointer** "We experimentally validate Droppler's prediction on the TAR DNA-binding protein in different experimental conditions, showing the consistency of its predictions."  
- **Evidence pointer** Abstract, Results section; location not provided  
- **Concern** The experimental validation is described only qualitatively. No details are given on the number of conditions tested, the range of concentrations, pH, or temperatures, the number of replicates, or the criteria used to define "consistency" between predictions and experimental outcomes.  
- **Why it matters** A single protein tested under unspecified conditions is insufficient to establish the model's reliability. The lack of quantitative agreement (e.g., correlation, error rates) makes it impossible to judge whether the model's predictions are accurate or merely coincidental.  
- **Resolution test** Provide a detailed description of the experimental setup, including the number and range of conditions, and report quantitative agreement metrics (e.g., percentage of correct predictions, confusion matrix) between Droppler's predictions and experimental observations.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Generalizability  
- **Claim pointer** The model is proposed as a general tool for predicting LLPS behavior of proteins, implying applicability beyond the single validation case.  
- **Evidence pointer** Abstract, Results section; location not provided  
- **Concern** The abstract does not describe the training dataset composition, such as how many proteins, what types of sequences, or how experimental conditions were represented. It is unclear whether the model was trained on a diverse set of LLPS and non-LLPS proteins, and whether the validation on TDP-43 is representative.  
- **Why it matters** Without evidence of generalizability across multiple proteins and conditions, the model's utility for proteome-scale screening is questionable. Overfitting to a narrow training set could lead to poor performance on unseen proteins.  
- **Resolution test** Describe the training dataset in terms of size, diversity, and source, and provide validation results on multiple proteins with varied sequence features and experimental conditions. Show that performance is consistent across different protein families.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Model description  
- **Evidence pointer** Abstract, Results section; location not provided  
- **Issue** The abstract mentions "multi-head neural attention" but does not explain how this architecture is adapted to incorporate experimental conditions as inputs.  
- **Required correction** Briefly describe how experimental conditions are encoded and integrated into the model, or refer to a methods section where this is detailed.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Availability statement  
- **Evidence pointer** Abstract, Availability and Implementation section; location not provided  
- **Issue** The code is available at a Bitbucket link, but the abstract does not specify the software dependencies, input data format, or whether a user-friendly interface is provided.  
- **Required correction** Add a brief note on the required Python packages and a minimal example of input data format, or state that such details are in the documentation.

## Risk / unsupported claims
- The claim that Droppler can "rapidly screen proteins and experimental conditions" is unsupported due to the absence of performance metrics.
- The claim of "consistency" in experimental validation on TDP-43 is unsupported due to lack of quantitative details.
- The general applicability of the model to proteome-scale screening is unsupported without evidence of generalizability across multiple proteins.
- The model's superiority or complementarity to existing LLPS prediction tools is not addressed and cannot be evaluated.