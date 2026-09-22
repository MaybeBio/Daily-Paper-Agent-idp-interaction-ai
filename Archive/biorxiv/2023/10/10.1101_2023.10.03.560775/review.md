## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, supplementary statements)
- **Assessment boundary** Scientific and technical claims as presented in the provided text; no external validation performed
- **Shared manuscript claim summary** The authors propose OpenMM-Loss, a custom PyTorch loss function that uses molecular dynamics force fields to compute the potential energy of predicted protein structures, and use its gradients to finetune OpenFold. They claim that finetuning with this loss produces structures with comparable accuracy, lower potential energy, and improved MolProbity metrics relative to the OpenFold baseline.
- **Visible evidence base** Abstract, introduction, methods, results, discussion, author contributions, supplementary links, acknowledgments
- **Missing materials affecting confidence** Figures 1, 3, 4, 5, 6 and Tables 1, 2 are referenced but not provided; no numerical data, error bars, or statistical details are included; no code or dataset contents are directly inspectable; no details on hyperparameters beyond those mentioned; no comparison to other energy-based training methods

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting and potentially useful idea, namely using molecular dynamics force fields as differentiable loss functions for protein structure prediction models. The framing of MD forces as gradients for backpropagation is elegant and the implementation appears technically feasible. However, the evidence provided in the text is insufficient to fully evaluate the claims. Key figures and tables are missing, statistical details are absent, and several methodological choices are not fully justified. The core claim of improved structural quality with comparable accuracy is plausible but not rigorously established from the supplied material.
- **Who would be interested in the results, and why** Researchers in computational structural biology, particularly those working on protein structure prediction, molecular docking, and the integration of physical principles into deep learning models. The work may also interest developers of deep learning frameworks for biomolecular systems and those studying the use of physics-based losses in machine learning.
- **Major strengths** The core idea is novel and well-motivated, addressing a real limitation of current structure prediction models. The implementation is described in sufficient detail to be reproducible in principle. The authors correctly identify the challenge of rugged energy landscapes and propose a reasonable smoothing mechanism. The use of multiple evaluation metrics (accuracy, energy, MolProbity) is appropriate.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
  - R1-M4
  - R1-M5
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
  - R1-m4
  - R1-m5
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** 
  - Originality: The idea of using MD force fields as loss functions is original and not widely explored in the context of protein structure prediction. This is a strength.
  - Scientific importance: If validated, the approach could improve the physical realism of predicted structures, which is important for downstream applications. However, the demonstrated improvements are modest and the broader impact is not yet clear.
  - Interdisciplinary readership: The work bridges deep learning and molecular dynamics, which could appeal to a broad audience. However, the presentation assumes familiarity with both fields, which may limit accessibility.
  - Technical soundness: The technical approach is sound in principle, but the evidence provided is incomplete. Missing figures and tables, lack of statistical details, and unclear baselines prevent a full assessment.
  - Readability for nonspecialists: The manuscript is written for a specialized audience. The abstract is clear, but the methods section is dense and may be difficult for nonspecialists to follow.
- **Recommendation posture** Supportive if technical concerns are resolved. The idea is promising and the implementation is plausible, but the current evidence does not fully establish the claims. Additional data, statistical analysis, and clarifications are needed.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The authors claim that finetuning with OpenMM-Loss produces structures with lower potential energy and improved MolProbity metrics while maintaining comparable accuracy.
- **Evidence pointer** Figures 3, 4, 5, 6 and Tables 1, 2 are referenced but not provided in the supplied material.
- **Concern** The central claims of the manuscript rest on figures and tables that are not available for review. Without these data, it is impossible to assess the magnitude of the reported improvements, the variability across seeds, or the statistical significance of the differences.
- **Why it matters** The claims of improved structural quality and comparable accuracy are the core contribution of the work. Without the actual data, the case is not established.
- **Resolution test** Provide the missing figures and tables with full numerical details, including error bars, p-values, and sample sizes.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors state that lDDT AA is "not significantly different (p=0.8)" between methods and that improvements in MolProbity and Clash scores are observed.
- **Evidence pointer** Results section, Figures 4, 5, 6, Table 1.
- **Concern** Only a single p-value is reported, and it is for a metric that is not the primary outcome of interest. No statistical analysis is presented for the MolProbity or Clash score differences. The use of a one-sided t-test is mentioned, but the details of the test (e.g., paired vs. unpaired, multiple testing correction) are not provided.
- **Why it matters** Without proper statistical analysis, it is unclear whether the observed improvements are robust or could be due to chance, especially given the small number of seeds (three).
- **Resolution test** Provide full statistical details for all reported comparisons, including effect sizes, confidence intervals, and correction for multiple testing where appropriate.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Baseline and comparison validity
- **Claim pointer** The authors compare their method to the OpenFold baseline, but the baseline is not clearly defined in terms of training data, finetuning procedure, or evaluation protocol.
- **Evidence pointer** Methods section, Training subsection.
- **Concern** The manuscript does not specify whether the baseline OpenFold model was finetuned on the same data (scnunmin) or on the original training data. It is also unclear whether the baseline was evaluated on the same test set and with the same relaxation procedure. Without this information, the comparison may not be fair.
- **Why it matters** A fair comparison is essential to attribute any observed improvements to the proposed loss function rather than to differences in training data or protocol.
- **Resolution test** Clearly describe the baseline model, its training procedure, and the evaluation protocol. Ensure that all models are compared under identical conditions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological justification
- **Claim pointer** The authors use a modified sigmoid function to smooth the energy landscape and scale the loss, but the choice of parameters is described as heuristic.
- **Evidence pointer** Methods section, OpenMM-based loss function.
- **Concern** The parameters of the sigmoid function (maximum value 1, minimum value -4, crossover at -20,000 kJ/mol) are chosen heuristically. The manuscript does not provide a sensitivity analysis or justification for these specific values. It is unclear how sensitive the results are to these choices.
- **Why it matters** If the results depend strongly on the sigmoid parameters, the method may not be robust or generalizable to other systems or force fields.
- **Resolution test** Provide a sensitivity analysis for the sigmoid parameters or a principled method for selecting them.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scope of claims
- **Claim pointer** The authors suggest that their framework "may enhance the ability of deep learning models to recapitulate fundamental biophysical principles" and "pave the way for more effective downstream applications."
- **Evidence pointer** Abstract, Discussion.
- **Concern** These statements are speculative and go beyond the demonstrated results. The manuscript does not test downstream applications such as docking, nor does it demonstrate that the model has learned general physical principles beyond the specific metrics reported.
- **Why it matters** Overstating the implications of the work could mislead readers about its current capabilities and potential impact.
- **Resolution test** Either provide evidence for downstream improvements or temper the claims to match the demonstrated results.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the method "demonstrates efficacy" but does not provide quantitative results. A brief summary of key numbers would strengthen the abstract.
- **Required correction** Include one or two key quantitative results in the abstract.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Methods, Training subsection
- **Issue** The manuscript mentions that models were finetuned for about 12 days on four A100s, but does not specify the number of training steps, learning rate schedule, or other hyperparameters.
- **Required correction** Provide full hyperparameter details to enable reproduction.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Introduction
- **Evidence pointer** Introduction
- **Issue** The term "violation loss" is used without a formal definition or reference to the original description.
- **Required correction** Define the term and cite the relevant source.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Supplementary Material
- **Evidence pointer** Supplementary Material
- **Issue** The manuscript states that code is available on GitHub, but does not specify the version or provide a DOI for archival purposes.
- **Required correction** Provide a versioned release with a DOI or permanent identifier.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Results
- **Evidence pointer** Results section
- **Issue** The text refers to "OMM/OMM ∗" without explaining the difference between the two variants.
- **Required correction** Clarify the distinction between OMM and OMM ∗ in the text.

## Risk / unsupported claims
- The claim that finetuning with OpenMM-Loss improves structural quality while maintaining accuracy is not fully supported without the missing figures and tables.
- The claim that the method "may enhance the ability of deep learning models to recapitulate fundamental biophysical principles" is speculative and not directly tested.
- The claim that the method "paves the way for more effective downstream applications" is not supported by any downstream experiments.
- The claim that the sigmoid function parameters were "heuristically chosen" without sensitivity analysis leaves the robustness of the method unassessed.
- The claim that the baseline comparison is fair is not verifiable without a clear description of the baseline training and evaluation protocol.