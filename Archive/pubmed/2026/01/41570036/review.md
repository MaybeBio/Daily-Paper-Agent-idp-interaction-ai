## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, supporting information references)
- **Assessment boundary** Scientific claims, methodological soundness, evidence quality, and presentation as presented in the supplied manuscript
- **Shared manuscript claim summary** The authors use AlphaFold2 Multimer to predict structures for 27,711 Drosophila melanogaster protein pairs from STRING (score ≥0.9), identify 3,621 high-confidence physical interactions (pDockQ ≥0.5), and report that intrinsically disordered regions (IDRs) are frequently involved in these predicted interfaces, with multiple binding modes (disordered, coil-to-order, conditionally folded). They provide a web resource for exploration.
- **Visible evidence base** Abstract, full results text, methods descriptions, figure references (Fig 1–5), supporting information references (S1–S6 Figs, S1–S4 Tables, S1–S5 Appendices)
- **Missing materials affecting confidence** Figures and supporting information files are referenced but not provided. Numerical data underlying key claims (e.g., exact counts of IDR-involved interfaces per binding mode) are not fully specified in text. Details of the web interface implementation and validation are not assessable.

## Reviewer
- **Overall assessment** This manuscript presents a large-scale structural prediction effort for Drosophila PPIs, with a focus on the role of IDRs. The work is timely and the resource could be valuable. However, the central claims about IDR involvement and binding mode classification rest on computational definitions and thresholds that are not fully validated against experimental data. The lack of quantitative detail in the text, combined with the absence of figures and supporting data, limits the ability to fully assess the strength of the evidence. The manuscript would benefit from clearer presentation of the classification criteria, validation against known complexes, and a more critical discussion of the limitations of AlphaFold2 Multimer for IDR-mediated interactions.
- **Who would be interested in the results, and why** Researchers in structural biology, computational biology, and proteomics, particularly those studying protein-protein interaction networks, intrinsically disordered proteins, and the application of deep learning to interactome prediction. The Drosophila community may find the resource useful for hypothesis generation. The methodological approach may also interest those developing or applying AlphaFold-based pipelines for interactome-scale studies.
- **Major strengths** 1. The study addresses a significant gap by applying AlphaFold2 Multimer at scale to a non-mammalian model organism. 2. The integration of functional association data (STRING) with structural prediction is a thoughtful approach. 3. The focus on IDRs in PPIs is timely and important. 4. The provision of a web interface is a practical contribution to the community.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (validation of IDR classification), R1-M2 (lack of quantitative detail), R1-M3 (generalizability of binding mode definitions), R1-M4 (web resource accessibility and documentation)
- **Assessment against Nature-style criteria** 
  - **Originality** Moderate. The application of AlphaFold2 Multimer to a Drosophila interactome is not entirely novel, but the specific focus on IDR binding modes at scale adds a new angle.
  - **Scientific importance** Potentially high, if the predictions are reliable. The role of IDRs in PPIs is a major question, and a predicted structural interactome could be a useful resource. However, the importance is contingent on the validity of the computational predictions.
  - **Interdisciplinary readership** The topic bridges structural biology, bioinformatics, and cell biology, and could appeal to a broad audience. However, the presentation is somewhat specialized and may not be fully accessible to nonspecialists without clearer explanations of the methods and implications.
  - **Technical soundness** The methods are generally sound in principle, but the lack of validation against experimental data and the absence of quantitative details weaken the technical case. The reliance on pDockQ and the specific definitions of IDR binding modes need more rigorous justification.
  - **Readability for nonspecialists** The manuscript is reasonably well-written but includes technical jargon and concepts (e.g., pDockQ, PAE, conditionally folded binding) that may be challenging for readers outside the immediate field. A more accessible summary of the key findings and their implications would improve readability.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea and resource are promising, but the current evidence does not fully establish the central claims about IDR involvement and binding mode classification. The authors need to provide stronger validation and clearer quantitative support.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / Validation
- **Claim pointer** The manuscript claims that "98.8% (3580/3621) [of high-confidence PPIs] involve IDRs, either entirely or in part" and that specific binding modes (disordered, coil-to-order, conditionally folded) can be reliably classified.
- **Evidence pointer** Results section "Most predicted dimers involve binding through disordered regions"; Methods section "Infer disordered, coil, and conditionally folded regions" and "Structure prediction and structural analysis"
- **Concern** The classification of IDR involvement and binding modes relies on computational definitions (e.g., ISD >0.5, pLDDT >70, secondary structure changes) that are not validated against experimental data. The authors do not provide any benchmark or comparison with known IDR-mediated complexes to demonstrate that their criteria correctly identify true IDR binding modes. The use of AlphaFold2 Multimer predictions for IDRs is particularly concerning, as these regions are often poorly predicted and may have high uncertainty.
- **Why it matters** The central claim of the paper is that IDRs are prevalent in PPIs and exhibit diverse binding modes. If the classification criteria are not validated, the quantitative claims (e.g., 98.8% involvement) could be artifacts of the prediction pipeline rather than biological reality. This would undermine the main contribution of the study.
- **Resolution test** The authors should validate their classification against a set of experimentally characterized IDR-mediated complexes (e.g., from PDB or literature). They should report sensitivity, specificity, and accuracy of their criteria. Additionally, they should discuss how prediction uncertainty (e.g., low pLDDT in IDRs) affects the reliability of the binding mode assignments.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality / Reproducibility
- **Claim pointer** The manuscript states that "27,711 protein pairs" were predicted, with "3,621 pairs (13.1%) at high confidence with pDockQ ≥0.5," and that "81% of AlphaFold's high-confidence predictions aligned with some physical evidence in STRING (score ≥0.4, with about half ≥0.9)."
- **Evidence pointer** Results sections "Predicted high-confidence D. melanogaster physical protein-protein interaction network" and "AlphaFold2 Multimer predicts core physical interaction networks"; Methods section "Extracting representative PPIs from the STRING database"
- **Concern** The manuscript lacks detailed quantitative breakdowns of the results. For example, the distribution of pDockQ scores, the number of predictions per STRING evidence category, and the exact overlap between predicted high-confidence PPIs and STRING physical evidence are not fully reported in the text. The figures and supporting information are referenced but not provided, making it impossible to verify the numbers or assess the quality of the predictions.
- **Why it matters** The quantitative claims are central to the paper's conclusions. Without access to the underlying data and detailed statistics, the reader cannot evaluate the robustness of the findings or reproduce the analysis. This is a significant barrier to assessing the scientific contribution.
- **Resolution test** The authors should provide a comprehensive table or supplementary file with the full list of predictions, including pDockQ scores, STRING evidence categories, and overlap with physical evidence. They should also report the distribution of scores and the criteria for defining "high confidence" more explicitly.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness / Generalizability
- **Claim pointer** The manuscript claims that "over 98% of predicted high confidence PPIs involve at least some level of intrinsic disorder" and that "IDR interfaces exhibit remarkable diversity, from being highly conserved to lineage specific."
- **Evidence pointer** Results sections "Most predicted dimers involve binding through disordered regions" and "Example of IDR interfaces with different binding mechanisms and evolutionary origins"; Methods section "Sequence conservation analysis"
- **Concern** The definitions of "disordered binding," "coil-to-order binding," and "conditionally folded binding" are based on computational predictions and may not be generalizable across different protein families or interaction types. The authors do not discuss how these definitions might bias the results, nor do they compare their classification with experimental observations of IDR binding modes. The evolutionary analysis is based on a limited set of examples and may not be representative.
- **Why it matters** The claim that IDRs are prevalent and diverse in PPIs is a major conclusion. If the classification is not robust or generalizable, the conclusions may be overstated or misleading. The evolutionary claims, in particular, require a more systematic analysis to be convincing.
- **Resolution test** The authors should apply their classification to a diverse set of known IDR-mediated complexes and compare the results with experimental data. They should also perform a more systematic evolutionary analysis across a larger set of IDR interfaces, rather than relying on a few examples.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Resource accessibility / Reproducibility
- **Claim pointer** The manuscript states that "we developed an interactive web platform for scientists to explore and generate new hypotheses from all the 27,711 predicted interactions," accessible at https://melppi.github.io.
- **Evidence pointer** Results section "An interactive web interface for exploring, validating, and expanding protein interaction hypotheses"
- **Concern** The web interface is a key deliverable of the paper, but its functionality, data availability, and usability are not described in sufficient detail. The authors do not specify the data format, the criteria for displaying interactions, or how users can download the full dataset. The interface is not assessable from the manuscript alone.
- **Why it matters** The resource is intended to be a major contribution. If the interface is not user-friendly or the data are not readily accessible, the practical value of the paper is diminished. The lack of documentation also hinders reproducibility.
- **Resolution test** The authors should provide a detailed description of the web interface, including its features, data schema, and download options. They should also ensure that the interface is publicly accessible and functional at the time of publication.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity / Presentation
- **Affected element** Abstract and Results section "Predicted high-confidence D. melanogaster physical protein-protein interaction network"
- **Evidence pointer** Abstract; Results section, first paragraph
- **Issue** The abstract states that "functional associations contribute significantly to high-confidence predictions," but the specific contribution of each STRING evidence category is not clearly quantified in the text. The statement is vague and could be misinterpreted.
- **Required correction** Provide a clear quantitative statement, e.g., "X% of high-confidence predictions were supported by experimental evidence, Y% by co-expression, etc.," in the abstract or results.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical clarity
- **Affected element** Methods section "Infer disordered, coil, and conditionally folded regions"
- **Evidence pointer** Methods section, paragraph on disorder inference
- **Issue** The definition of "conditionally folded" regions as "predicted to have both high pDockQ (>70) and high structural disorder (ISD >0.5)" is confusing. pDockQ is a metric for complex prediction confidence, not for individual regions. The authors likely mean pLDDT, not pDockQ, for the monomer prediction.
- **Required correction** Clarify the metric used for defining conditionally folded regions. If pLDDT is intended, correct the text accordingly.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section "Example of IDR interfaces with different binding mechanisms and evolutionary origins"
- **Evidence pointer** Results section, fourth paragraph
- **Issue** The evolutionary analysis is based on only three examples (Sec61alpha/CG13426, Roc1b/Cul5, Jra/Stat92E). This is a very small sample size to support the claim that IDR interfaces "exhibit remarkable diversity" in evolutionary origins.
- **Required correction** Either expand the evolutionary analysis to a larger set of IDR interfaces or temper the claim to reflect the limited scope of the analysis.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Discussion section
- **Evidence pointer** Discussion, first paragraph
- **Issue** The discussion of the discrepancy between computational predictions and experimental data is somewhat repetitive and could be more concise. The point about AlphaFold2 Multimer potentially overlooking transient interactions is important but could be stated more directly.
- **Required correction** Streamline the discussion to focus on the key implications and avoid redundancy.

## Risk / unsupported claims
- The claim that "98.8% of predicted high-confidence PPIs involve IDRs" is unsupported without validation of the IDR classification criteria against experimental data.
- The claim that "IDR interfaces exhibit remarkable diversity, from being highly conserved to lineage specific" is based on a limited number of examples and is not systematically supported.
- The claim that "81% of AlphaFold's high-confidence predictions aligned with some physical evidence in STRING" is not fully verifiable without the underlying data and figures.
- The functional significance of the predicted IDR-mediated interactions is not experimentally validated, and the authors do not provide evidence that these predictions correspond to biologically relevant interactions.
- The web interface is described as a resource, but its functionality and data accessibility are not assessable from the manuscript.