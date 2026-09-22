## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, tables, or supplementary material were provided
- **Shared manuscript claim summary** The authors propose unsupervised random forest (URF), a self-supervised adaptation of random forests, for learning functionally relevant protein conformational representations without labeled data. They claim URF matches or surpasses supervised counterparts and 15 baseline methods, includes an internal metric (learning coefficient) for automated hyperparameter optimization, and was validated on 10 protein systems including folded and intrinsically disordered proteins. They further claim URF representations are functionally meaningful compared to deep learning methods and integrate with downstream analyses such as Markov state models.
- **Visible evidence base** Abstract text only; no quantitative results, methodological details, or validation data are visible
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, benchmark definitions, hyperparameter details, learning coefficient formulation, and downstream analysis results

## Reviewer
- **Overall assessment** The abstract presents a potentially useful methodological contribution in unsupervised representation learning for protein biophysics. The core idea of adapting random forests to an unsupervised setting with an internal hyperparameter optimization metric is interesting and could appeal to a broad computational biology audience. However, the abstract alone provides insufficient evidence to evaluate the validity of the central claims. Key quantitative comparisons, methodological specifics, and validation details are absent. The claim of outperforming 15 baseline methods and matching supervised counterparts requires rigorous benchmarking evidence that is not visible here. The learning coefficient, presented as a central innovation, is not defined or characterized. The validation across 10 systems and comparison to deep learning methods are stated without supporting data. The manuscript may have merit, but the case is not established from the supplied material.
- **Who would be interested in the results, and why** Computational biophysicists and structural biologists working on conformational dynamics of proteins, particularly those using Markov state models or other downstream analyses. Researchers developing unsupervised feature learning methods for biomolecular simulations would also find this relevant. The potential to reduce reliance on labeled data and prior knowledge in feature selection could interest method developers in the broader machine learning for science community.
- **Major strengths** The conceptual framing of an unsupervised adaptation of random forests is novel and potentially impactful. The emphasis on removing user supervision and prior labels addresses a real limitation in current practice. The claim of an internal metric for hyperparameter optimization, if valid, would enhance usability. The stated validation across diverse protein systems including intrinsically disordered proteins suggests broad applicability.
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
- **Assessment against Nature-style criteria** Originality is potentially high given the novel adaptation of random forests to unsupervised learning in this context. Scientific importance could be substantial if the method genuinely reduces bias and improves representation learning, but this is not verifiable from the abstract. Interdisciplinary readership appeal is plausible given the intersection of machine learning and biophysics. Technical soundness cannot be assessed without methodological details and benchmark results. Readability for nonspecialists is adequate in the abstract, though the learning coefficient is introduced without explanation. Overall, the work has potential but the evidence base is insufficient for a definitive assessment.
- **Recommendation posture** Currently not established from the provided evidence. The abstract suggests a promising method, but the absence of quantitative results, methodological detail, and validation data prevents any conclusion about the validity of the central claims. A full manuscript review would be required to assess whether the technical concerns can be resolved.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** URF performs at par or surpasses its traditional supervised counterpart and 15 other leading baseline methods.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract claims superior or comparable performance against a supervised random forest and 15 baseline methods, but no quantitative results, benchmark definitions, or statistical comparisons are provided. The nature of the baselines, the evaluation metrics, and the specific systems used for comparison are unspecified.
- **Why it matters** This is the central performance claim of the manuscript. Without visible benchmarking data, the reader cannot assess whether the claim is justified or whether the comparison was fair and comprehensive. The claim of outperforming 15 methods is strong and requires transparent evidence.
- **Resolution test** Provide a benchmark table or figure with performance metrics for URF, supervised random forest, and all 15 baselines across the 10 protein systems, including statistical significance tests and clear definitions of evaluation metrics.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** URF is supplemented by an internal metric, the learning coefficient, which automates the process of hyper-parameter optimization.
- **Evidence pointer** Abstract, location not provided
- **Concern** The learning coefficient is introduced as a key innovation, but its definition, mathematical formulation, and mechanism for guiding hyperparameter selection are not described. No evidence is shown that this metric reliably identifies optimal hyperparameters across different systems.
- **Why it matters** The learning coefficient is presented as a distinguishing feature that makes the method robust and user-friendly. If this metric is not well-defined or validated, the claimed advantage over other methods is weakened. The reproducibility of the method depends on a clear description of this component.
- **Resolution test** Provide a formal definition of the learning coefficient, explain how it is computed, and show validation results demonstrating that it selects appropriate hyperparameters across multiple protein systems, ideally with comparisons to manual tuning or grid search.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** URF was validated against 10 independent protein systems including both folded and intrinsically disordered states.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract states validation on 10 systems but provides no details on which proteins were used, how the systems were selected, what conformational states were sampled, or what metrics were used to assess the quality of learned representations. The claim of functional meaningfulness compared to deep learning methods is also unsupported.
- **Why it matters** Validation across diverse systems is a core strength claim. Without specifics, the reader cannot judge whether the systems are representative, whether the validation is rigorous, or whether the comparison to deep learning methods is fair. The claim of functional meaningfulness requires a clear definition of what constitutes functional relevance and how it was measured.
- **Resolution test** List the 10 protein systems, describe the simulation or experimental data used, define the metrics for representation quality and functional meaningfulness, and provide comparative results against deep learning methods with appropriate statistical analysis.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** URF can be seamlessly integrated with downstream analyses pipeline such as Markov state models to attain better resolved outputs.
- **Evidence pointer** Abstract, location not provided
- **Concern** The integration with Markov state models is mentioned as an application, but no results are shown to demonstrate improved resolution. The nature of the improvement, the systems used, and the comparison to standard approaches are absent.
- **Why it matters** This application claim suggests practical utility beyond representation learning. Without evidence, the reader cannot assess whether the integration is indeed seamless or whether the improvements are meaningful. This claim also implies a workflow that should be reproducible from the manuscript.
- **Resolution test** Provide a case study showing URF-based features used in a Markov state model analysis, with quantitative comparison to a standard feature selection approach, including metrics such as implied timescales, metastable state identification, or validation of the resulting model.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract wording
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "both both folded and intrinsically disordered states" contains a duplicated word, which suggests the abstract may not have been carefully proofread.
- **Required correction** Remove the duplicated "both" to read "including both folded and intrinsically disordered states."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Method description
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract mentions a "memory-efficient implementation" of URF but provides no detail on the computational complexity or memory footprint compared to standard random forests. This is relevant for users applying the method to large biomolecular systems.
- **Required correction** Add a brief statement in the abstract or methods about the computational advantages, or provide benchmark runtime and memory usage data in the full manuscript.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Learning coefficient
- **Evidence pointer** Abstract, location not provided
- **Issue** The learning coefficient is introduced without any intuitive explanation of what it measures or why it is named as such. This may confuse readers unfamiliar with the concept.
- **Required correction** Provide a one-sentence explanation of the learning coefficient in the abstract, such as what property of the model it quantifies and how it relates to hyperparameter selection.

## Risk / unsupported claims
- The claim that URF performs at par or surpasses supervised random forest and 15 baseline methods is unsupported by visible evidence.
- The claim that the learning coefficient automates hyperparameter optimization is unsupported and the metric is undefined.
- The claim of validation on 10 protein systems is unverifiable without system details and results.
- The claim that URF representations are functionally meaningful compared to deep learning methods is unsupported.
- The claim of seamless integration with Markov state models and improved resolution is unsupported.
- The overall assertion that URF is a leading tool for unsupervised representation learning in protein biophysics is not established from the abstract alone.