## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no full manuscript, figures, tables, or supplementary materials provided
- **Shared manuscript claim summary** The authors propose a simulation protocol that predicts whether disordered protein sequences bind to microtubules, identify two categories of strongly interacting subsequences (positively charged hydrophobic clusters and alternating charge sequences), analyze their optimal balance, and validate preferential interaction regions on microtubules against known experimental results.
- **Visible evidence base** Abstract text only; no methodological details, quantitative results, or experimental validation data are available
- **Missing materials affecting confidence** Full manuscript, simulation protocol description, force field parameters, sequence dataset, pattern analysis methodology, validation data, and any figures or tables

## Reviewer
- **Overall assessment** The abstract presents a potentially useful computational approach to a biologically relevant problem, namely the molecular determinants of microtubule-condensate interactions. However, the claims are broad and the evidence base is entirely inaccessible from the abstract alone. The identification of two sequence categories is plausible but lacks quantitative support, and the validation statement is too vague to assess rigor. The work may interest the biomolecular condensate and cytoskeleton communities, but the current abstract does not establish the case.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, microtubule-associated proteins, and cytoskeletal regulation would be interested because the proposed protocol could enable sequence-based prediction of microtubule binding, which has implications for understanding cell division, vesicle transport, and cellular locomotion. Computational biophysicists developing coarse-grained or atomistic simulation methods for disordered proteins may also find the protocol relevant.
- **Major strengths** The abstract addresses a clear gap in the field, namely the lack of systematic molecular-level investigation of condensate-microtubule binding patterns. The proposed simulation protocol has potential practical utility for compound testing. The identification of two distinct sequence categories provides a testable framework.
- **Major Concerns** The abstract provides no quantitative evidence for the predictive accuracy of the protocol, no description of the simulation methodology, and no details on how the two sequence categories were derived or validated. The claim of validation against experimental results is unsupported by specific examples or metrics.
- **Minor Comments** The abstract would benefit from stating the number of sequences tested, the simulation timescales, and the specific experimental datasets used for validation. The term "molecular grammar" is used without definition, which may confuse nonspecialist readers.
- **Technical failings that need to be addressed before the case is established** R1-M1 (predictive accuracy unquantified), R1-M2 (validation claim unsupported), R1-M3 (methodology inaccessible)
- **Assessment against Nature-style criteria** Originality: moderate, as the specific application to microtubule-wetting condensates is novel, but the general concept of sequence-encoded binding is established. Scientific importance: potentially high for the condensate and cytoskeleton fields, but not demonstrated from the abstract. Interdisciplinary readership: likely limited to biophysicists and cell biologists; the abstract does not frame the work for a broader audience. Technical soundness: cannot be assessed without methodological details. Readability for nonspecialists: the abstract is concise but uses jargon without explanation.
- **Recommendation posture** Currently not established from the provided evidence; supportive if technical concerns are resolved with full manuscript data

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "We provide a simulation protocol that is able to predict whether any given disordered protein sequence will bind to microtubules."
- **Evidence pointer** Abstract, location not provided
- **Concern** The claim that the protocol can predict binding for "any given" disordered protein sequence is extremely broad, yet the abstract provides no quantitative metrics such as sensitivity, specificity, or area under the receiver operating characteristic curve. No information is given on the number of sequences tested, the diversity of the test set, or the false positive and false negative rates.
- **Why it matters** Without quantitative performance metrics, the predictive power of the protocol cannot be evaluated, and the claim of general applicability is unsupported. This is the central claim of the work, and its validity is essential for the manuscript's contribution.
- **Resolution test** Provide in the full manuscript a benchmark dataset with known binding and nonbinding sequences, report classification performance metrics, and discuss limitations such as sequence length dependence or conformational variability.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** "Preferential regions of interaction on microtubules are identified and validated with known experimental results."
- **Evidence pointer** Abstract, location not provided
- **Concern** The validation statement is vague. No specific experimental studies, binding affinities, or structural data are cited. It is unclear whether the validation is qualitative (e.g., agreement with known binding sites) or quantitative (e.g., correlation with measured affinities), and whether the validation covers both sequence categories.
- **Why it matters** Validation against experimental data is critical to establish that the simulation predictions are biologically meaningful. Without specific details, the reader cannot judge the strength of the validation or whether it is selective.
- **Resolution test** List the experimental datasets used, describe the comparison method (e.g., overlap with cryo-EM structures, mutation studies), and provide statistical measures of agreement.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** "We provide a simulation protocol that is able to predict whether any given disordered protein sequence will bind to microtubules."
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract does not describe the simulation method, including the level of theory (atomistic, coarse-grained), force field parameters, system setup, or analysis pipeline. Without this information, the protocol cannot be reproduced or assessed for potential artifacts such as force field biases or insufficient sampling.
- **Why it matters** Reproducibility is a core requirement for computational studies. The absence of methodological detail prevents independent verification and limits the protocol's utility to the community.
- **Resolution test** In the full manuscript, provide a detailed methods section with simulation parameters, system construction, equilibration and production run lengths, and analysis scripts or pseudocode.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract terminology
- **Evidence pointer** Abstract, location not provided
- **Issue** The term "molecular grammar" is used without definition, and "wetting condensates" may be unfamiliar to some readers.
- **Required correction** Define "molecular grammar" in the abstract or first paragraph of the introduction, and briefly explain the wetting concept in the context of condensate-microtubule interactions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Abstract content
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract does not state the number of sequences analyzed or the simulation timescales, which are basic descriptors of the study's scope.
- **Required correction** Add a sentence in the abstract or results summary indicating the dataset size and simulation length.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Claim of "optimal balance"
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "their overall optimal balance is analyzed" is vague; it is unclear what metric defines optimality and how it was computed.
- **Required correction** Specify the optimization criterion (e.g., binding free energy, contact frequency) and the method used to determine the balance.

## Risk / unsupported claims
- The claim that the protocol predicts binding for "any given" disordered protein sequence is unsupported without performance metrics.
- The claim of validation against experimental results is unsupported without specific datasets or comparison methods.
- The identification of two sequence categories as "strongly interacting" is unquantified; no binding strength thresholds or statistical significance are provided.
- The "optimal balance" analysis is not described, making the claim unassessable.
- The suitability of the protocol for "compound testing" is asserted without evidence of throughput, cost, or accuracy in a screening context.