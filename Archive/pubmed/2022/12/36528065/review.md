## Review setup
- **Input scope** Full manuscript text, including abstract, results, discussion, experimental procedures, and data availability sections.
- **Assessment boundary** Evaluation of the scientific claims, methodology, data analysis, and interpretation as presented in the provided manuscript. No external data or literature beyond the manuscript content is considered.
- **Shared manuscript claim summary** The authors propose that intrinsically disordered regions (IDRs) driving phase separation (PS) constitute a robustly distinct protein class, distinguishable from conventional IDRs and folded domains using sequence-based physicochemical properties. They present ParSe v2, an updated predictor leveraging these properties, and demonstrate its utility in identifying PS IDRs across proteomes and predicting mutation effects on phase separation.
- **Visible evidence base** The manuscript includes curated sequence datasets (PS ID, ID, folded), statistical comparisons using amino acid property scales, PCA, and performance evaluations of ParSe v2 against published datasets and other predictors. Figures 1-5 and supporting tables are referenced.
- **Missing materials affecting confidence** The manuscript references supporting information (Tables S1-S7, Figures S1-S13) that are not provided in the submitted text. This limits full verification of dataset details, complete results, and supplementary analyses.

## Reviewer
- **Overall assessment** This manuscript presents a valuable and timely contribution to the field of protein phase separation. The authors address a critical need for accurate identification of PS-driving IDRs and provide compelling evidence that these regions are a distinct protein class. The methodological approach is sound, and the development of ParSe v2 offers a practical tool for the community. However, several technical aspects, particularly regarding dataset curation, the interpretation of PCA results, and the generalizability of the mutation predictions, require clarification and additional validation to fully support the claims.
- **Who would be interested in the results, and why** This work will be of significant interest to researchers in the fields of biophysics, cell biology, and computational biology, specifically those studying phase separation, intrinsically disordered proteins, and organelle biogenesis. The findings provide a framework for understanding the sequence determinants of phase separation and offer a new bioinformatic tool for genome-wide screens. The study also has implications for understanding diseases linked to aberrant phase separation.
- **Major strengths**
    1.  The study addresses a significant problem with a well-defined approach, using expanded and carefully considered datasets for training and validation.
    2.  The finding that numerous amino acid property scales can distinguish PS IDRs is robust and provides a strong foundation for the main claim.
    3.  The development of ParSe v2, with its speed and demonstrated performance, represents a practical and useful advancement for the field.
    4.  The analysis of mutation effects, including the incorporation of interaction terms (Uπ, Uq), is a forward-looking step toward predicting the impact of sequence changes.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical Soundness
    - **Claim pointer** The claim that the curated datasets are robust and that the PS ID set is distinct from the ID set is central to the paper's premise.
    - **Evidence pointer** Results section "Construction of protein sequence datasets", Tables 1, 2, and Figure 1A.
    - **Concern** The curation of the negative control "ID" set is a potential source of bias. The authors state that BMRB entries are likely to have low phase separation propensity because NMR experiments are done at high concentrations. However, this is an assumption, and some BMRB entries could still contain regions capable of phase separation under different conditions. More critically, the ID set is derived from DisProt entries lacking phase separation annotation. As the authors note, this is a "nominal" depletion. The manuscript would be strengthened by a more detailed analysis of the potential for false negatives in the ID set and a discussion of how this could impact the training and evaluation of ParSe v2. The reliance on "nominal" depletion is a significant weakness in establishing the distinctness of the PS ID class.
    - **Why it matters** If the ID set contains undiscovered PS IDRs, the training data for the "non-PS" class is contaminated. This could lead to a predictor that is less accurate than reported and weaken the fundamental claim that PS IDRs are a "robustly distinct" class. The distinction between the classes is the core of the paper, and the quality of the negative set is paramount.
    - **Resolution test** The authors should provide a more rigorous validation of the ID set. This could include (1) a computational analysis to show that the ID set is depleted for known PS-promoting features, (2) a comparison of the ID set against a set of IDRs that have been experimentally shown *not* to phase separate, or (3) a clear statement of the limitations and a sensitivity analysis showing that the main conclusions are not dependent on the exact composition of the ID set.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical Soundness
    - **Claim pointer** The claim that ParSe v2 can predict the effects of mutations on phase separation behavior, particularly with the inclusion of Uπ and Uq.
    - **Evidence pointer** Results section "Predicting the effects from mutation on phase separation behavior", Figure 5.
    - **Concern** The method for training and validating the interaction parameters (Uπ, Uq) is circular. The parameters (a, b, c) are fit to optimize the correlation with the experimental data (ΔH°, ΔS°, ΔG°, or csat) from the same mutant datasets that are then used to report the prediction accuracy. This is not a valid test of predictive power. The reported ~90% accuracy for directional change is therefore an overestimate of the model's true predictive ability on unseen mutations.
    - **Why it matters** A key claim of the paper is that ParSe v2 can be used to understand and predict the effects of mutations. If the performance is evaluated on the training data, the reported accuracy is not a reliable indicator of how the model will perform on new, unseen mutations. This limits the practical utility of the tool for experimentalists.
    - **Resolution test** The authors must use a proper cross-validation scheme. For example, they could perform leave-one-out cross-validation on the mutant datasets, where the model parameters are fit on all but one mutant and then used to predict the held-out mutant. This would provide an unbiased estimate of the model's predictive performance.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific Importance
    - **Claim pointer** The claim that the classification of PS IDRs as a "robustly distinct protein class" provides "further insight into the elements involved in protein phase separation."
    - **Evidence pointer** Abstract, Discussion.
    - **Concern** While the data robustly show statistical differences in the mean values of certain physicochemical properties, the biological significance of this "distinct class" is not fully explored. The authors show that PS IDRs are different, but do not deeply discuss *why* this difference matters for the mechanism of phase separation. The paper would be significantly strengthened by a more mechanistic interpretation. For example, what specific interactions (e.g., cation-pi, hydrophobic) are most enriched, and how does the combination of properties lead to the physical chemistry of phase separation? The current discussion is somewhat superficial.
    - **Why it matters** The paper's title makes a strong claim about a "robustly distinct protein class." For this to be a significant conceptual advance, the authors need to move beyond statistical classification and provide a deeper biophysical or functional rationale for this distinctness. Without this, the claim, while supported, feels descriptive rather than mechanistic.
    - **Resolution test** The authors should expand the discussion to connect their findings to specific molecular mechanisms. For example, they could analyze which specific amino acid interactions are most over-represented in PS IDRs and discuss how these contribute to the multivalent interactions that drive phase separation. They could also discuss the implications of this distinct class for the evolution of phase-separating proteins.

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability for Nonspecialists
    - **Affected element** Abstract and Introduction
    - **Evidence pointer** Abstract, Introduction
    - **Issue** The abstract and introduction assume a high level of familiarity with the field. Terms like "vmodel" and "β-turn propensity" are used without a clear, intuitive explanation of their physical meaning for a general reader.
    - **Required correction** Provide a brief, plain-language explanation of these key metrics in the introduction or abstract. For example, "vmodel, a measure of how expanded or compact a disordered protein chain is," and "β-turn propensity, a measure of the likelihood of a region to form a tight turn structure."

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Results section "Predicting the effects from mutation on phase separation behavior"
    - **Evidence pointer** Figure 5A
    - **Issue** The method for ranking mutants "from left-to-right, in decreasing phase separation 'potential' as reported within each individual study" is not clearly defined. It is unclear how the different experimental metrics (e.g., csat, ΔH°) were normalized or compared to create a single rank order.
    - **Required Correction** Clarify the exact procedure used to establish the experimental rank order for each study. State whether the ranking is based on a single metric or a combination, and how ties were handled.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Experimental Procedures, "Calculation of Uπ"
    - **Evidence pointer** Equation 3
    - **Issue** The equation for Uπ is complex and the rationale for the specific weighting scheme (3:2:1) is not fully justified. It is stated that it "followed the observed rank order," but the mapping from a rank order to these specific weights is not explained.
    - **Required Correction** Provide a more detailed justification for the chosen weights. A sensitivity analysis showing how the results change with different weighting schemes would also be valuable.

- **Technical failings that need to be addressed before the case is established**
    - R1-M1: The potential for contamination in the negative control "ID" set needs to be addressed with a more rigorous validation or a clear statement of limitations.
    - R1-M2: The evaluation of mutation effect prediction is circular and must be replaced with a proper cross-validation approach.

## Risk / unsupported claims
- The claim that ParSe v2 can predict the effects of mutations on phase separation behavior with ~90% accuracy is unsupported due to the circular training and evaluation method.
- The claim that the ID set is a robust negative control is not fully supported, as the depletion of PS-promoting elements is only "nominal."
- The biological significance of the "robustly distinct protein class" is not fully established, as the discussion lacks a deep mechanistic interpretation of the findings.
- The performance comparison with other predictors (e.g., PScore, CatGranule, PLAAC) is mentioned but the full results are in the supplementary materials, which were not provided for review. This makes a full assessment of the comparative claims impossible.