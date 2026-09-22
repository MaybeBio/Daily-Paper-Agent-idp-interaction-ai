## Review setup
- **Input scope** Full manuscript text including abstract, main text, methods, and supplementary information descriptions
- **Assessment boundary** Scientific validity, methodological rigor, claims versus evidence, and presentation quality of the described deep-learning model ALBATROSS for predicting intrinsically disordered protein conformational properties from sequence
- **Shared manuscript claim summary** The authors present ALBATROSS, a deep-learning model trained on coarse-grained molecular dynamics simulations, that predicts ensemble dimensions of intrinsically disordered regions (IDRs) including radius of gyration, end-to-end distance, polymer-scaling exponent, and asphericity directly from amino acid sequence. The model is claimed to be accurate, high-throughput, and applicable at proteome-wide scale, enabling characterization of sequence-ensemble relationships within and between proteomes.
- **Visible evidence base** Abstract, full main text, methods section, figure legends and descriptions, supplementary information overview
- **Missing materials affecting confidence** Actual figures and supplementary figures not viewable; exact numerical values for many reported statistics not provided in text; supplementary tables referenced but not accessible; code repository not inspected

## Reviewer
- **Overall assessment** This manuscript describes a useful and potentially impactful tool for the IDP community. The combination of rational sequence design, coarse-grained simulations, and deep learning is sensible, and the validation against experimental SAXS data is encouraging. The proteome-wide applications demonstrate clear utility. However, several technical concerns regarding force field modifications, training data generation, model generalization, and the interpretation of proteome-wide results require clarification before the claims can be fully accepted. The manuscript is well-written and the tool appears to fill a genuine gap in accessible prediction of IDR conformational properties.

- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins and regions, including those interested in phase separation, RNA binding, and IDR function. The tool will also be of interest to computational biologists and bioinformaticians working on proteome-scale analyses, as well as experimentalists who need rapid estimates of IDR dimensions for hypothesis generation. The democratization aspect (Google Colab notebooks, no hardware requirements) broadens the potential user base considerably.

- **Major strengths**
  1. Addresses a real and recognized gap: no fast, accessible tool exists for predicting IDR ensemble dimensions from sequence alone at proteome scale.
  2. The training data generation strategy combining rational design with natural sequences is thoughtful and likely improves generalization.
  3. Validation against experimental SAXS data provides important external benchmarking.
  4. The tool is made widely accessible through multiple interfaces (Python package, Google Colab, web server integration).
  5. The proteome-wide analyses generate biologically interesting hypotheses, particularly around RNA-binding proteins and compact IDRs.
  6. The discussion of limitations is honest and appropriately caveated.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of force field modification
- **Claim pointer** The authors state they made "several small modifications" to the Mpiri force field, yielding Mpiri-GG, which "modestly" outperforms the original with R2 of 0.921 versus 0.896.
- **Evidence pointer** Results section, "Mpiri-GG accurately recapitulates IDR ensemble dimensions"; Supplementary Figures 1-5
- **Concern** The nature and extent of the modifications to the Mpiri force field are not described in sufficient detail in the main text. The reader is referred to Supplementary Information, but the specific changes, their rationale, and their potential impact on the transferability of the force field are not summarized. This is critical because the entire training dataset for ALBATROSS is generated using this modified force field.
- **Why it matters** If the force field modifications are not well-justified or are overfitted to the specific test set used for validation, the training labels for ALBATROSS could be systematically biased. The reported improvement from 0.896 to 0.921 R2, while modest, needs to be understood in the context of what was changed and why. Without this information, the reliability of the underlying simulation data cannot be fully assessed.
- **Resolution test** Provide a clear summary of the modifications made to Mpiri, the rationale for each change, and a comparison of Mpiri-GG performance against the original Mpiri on a broader set of validation cases beyond those shown. Ideally, include a discussion of whether the modifications improve agreement with experimental data across multiple IDR types.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalization and potential for circularity
- **Claim pointer** The authors claim ALBATROSS shows "excellent agreement" with simulation data on held-out test sets (R2 = 0.995 for Rg, 0.986 for Re, 0.817 for asphericity, 0.967 and 0.930 for scaling exponent and prefactor).
- **Evidence pointer** Results section, "Training a sequence-to-ensemble deep-learning model"; Figure 2
- **Concern** The held-out test set appears to be drawn from the same distribution as the training set, since both include synthetic sequences generated with the same design parameters and natural IDRs from the same proteomes. This means the reported accuracy may reflect interpolation within a well-sampled region of sequence space rather than true generalization to novel sequence types. The claim of "generalizability of sequence-ensemble relationships" needs to be tested more rigorously.
- **Why it matters** A model that performs well on in-distribution test data but poorly on out-of-distribution sequences would have limited utility for the broader IDP community, where sequences can be highly diverse. The authors do test on experimental SAXS data, which is encouraging, but the number of experimental comparisons appears limited. The distinction between interpolation and extrapolation is crucial for establishing the true scope of the tool's applicability.
- **Resolution test** Perform additional validation on sequences that are deliberately out-of-distribution, such as IDRs with unusual amino acid compositions, extreme lengths, or from organisms not represented in the training set. Report performance on these cases separately. Additionally, provide a more extensive comparison against experimental data, ideally including IDRs with known compact or expanded conformations from diverse sequence families.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of proteome-wide results
- **Claim pointer** The authors state that "most IDRs behave as relatively expanded chains" and that compact IDRs are enriched for aromatic residues while expanded IDRs are enriched for proline and/or have higher absolute net charge per residue.
- **Evidence pointer** Results section, "Proteome-wide predictions of IDR ensemble properties"; Figure 4
- **Concern** The proteome-wide analysis is based on predictions from ALBATROSS, which is itself trained on simulations. The conclusions about which sequence features drive compaction or expansion are therefore somewhat circular: the model has learned these relationships from the training data, and the proteome-wide analysis simply reflects those learned associations. The authors do compare with experimental data, but the interpretation of proteome-wide trends as biological insights needs to be carefully framed as model predictions rather than independent observations.
- **Why it matters** If the underlying force field (Mpiri-GG) has systematic biases in how it treats certain amino acid interactions, those biases will propagate through ALBATROSS and appear as "biological insights" in the proteome-wide analysis. The authors acknowledge some limitations in the discussion, but the framing of these results as discoveries rather than model predictions could mislead readers.
- **Resolution test** Clearly distinguish between model predictions and experimental observations throughout the proteome-wide analysis. Where possible, validate key claims (e.g., RNA-binding proteins having compact IDRs) against experimental data for a subset of proteins. Discuss how the conclusions might change if the underlying force field has known biases.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Benchmarking and comparison to existing methods
- **Claim pointer** The authors claim ALBATROSS is "comparable to or more accurate than the current state-of-the-art methods for radii of gyration prediction."
- **Evidence pointer** Results section, "Training a sequence-to-ensemble deep-learning model"; Supplementary Figure 8
- **Concern** The comparison to existing methods appears limited and is only briefly mentioned. The specific methods compared against, the datasets used for comparison, and the metrics used are not described in the main text. A more thorough benchmarking against existing predictors would strengthen the claims of superiority or equivalence.
- **Why it matters** For a tool to be adopted by the community, it needs to demonstrate clear advantages over existing approaches, whether in accuracy, speed, or accessibility. The current description of the benchmarking is insufficient to evaluate whether ALBATROSS genuinely represents an advance over existing methods.
- **Resolution test** Provide a detailed benchmarking section describing the methods compared, the datasets used, the evaluation metrics, and the results. Include runtime comparisons to demonstrate the speed advantage. If possible, benchmark on a standardized dataset used by the community for IDR property prediction.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure descriptions
- **Affected element** Figure 1
- **Evidence pointer** Figure 1 description
- **Issue** The figure description is dense and combines multiple concepts (model architecture, workflow, sequence design strategy) in a way that may be difficult for non-specialist readers to follow.
- **Required correction** Consider splitting Figure 1 into separate panels with clearer sub-labels, or providing a more structured legend that guides the reader through the workflow step by step.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Throughout
- **Evidence pointer** Main text
- **Issue** The terms "ensemble dimensions," "global dimensions," and "conformational properties" are used somewhat interchangeably. While this is not incorrect, consistent terminology would improve readability.
- **Required correction** Define these terms clearly at first use and use them consistently throughout the manuscript.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Accessibility of supplementary information
- **Affected element** Supplementary information
- **Evidence pointer** Supplementary Figures 1-20, Supplementary Tables 1-8
- **Issue** The supplementary information is extensive but the main text does not always clearly indicate which supplementary items support specific claims.
- **Required correction** Add explicit references to specific supplementary figures and tables at the points in the main text where the corresponding claims are made.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Evidence pointer** Discussion
- **Issue** While the discussion does acknowledge limitations, the treatment of potential biases in the training data and force field could be more thorough.
- **Required correction** Expand the discussion of how the choice of training sequences and force field might affect the generalizability of ALBATROSS predictions, and suggest strategies for users to assess when predictions are likely to be reliable.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Code availability
- **Affected element** Methods, "ALBATROSS implementation and distribution"
- **Evidence pointer** Methods section
- **Issue** The manuscript mentions code availability but does not provide a clear statement about the license, versioning, or long-term maintenance plans for the software.
- **Required correction** Add a clear code availability statement including the license, version, and a link to the repository. Consider adding a statement about planned maintenance and support.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results section
- **Evidence pointer** Figure 2 and associated text
- **Issue** The R2 values are reported but confidence intervals or other measures of uncertainty are not provided for the model performance metrics.
- **Required correction** Report confidence intervals for the R2 values, or at minimum, describe the variability across cross-validation folds.

## Risk / unsupported claims
- The claim that ALBATROSS predictions correlate "extremely well" with experimental SAXS data is supported by only a limited number of comparisons shown in Figure 1b; the full extent of experimental validation is not clear from the text.
- The claim of "conformational buffering" in yeast homologs is based on a small number of examples and is presented as a proof of concept, which is appropriate, but the broader significance is not yet established.
- The statement that "most IDRs behave as relatively expanded chains" in the human proteome is a model prediction that has not been independently verified experimentally.
- The comparison to "state-of-the-art methods" is not sufficiently detailed to evaluate whether this claim is fully supported.
- The assertion that ALBATROSS "offers predictive power equivalent to the current state of the art in coarse-grained simulations" is based on comparison to simulation data, but the relationship between simulation accuracy and experimental reality is not fully addressed.

## Assessment against Nature-style criteria
- **Originality** The work is original in its specific combination of approaches. While individual components (coarse-grained simulations, deep learning, sequence design) are established, their integration into a fast, accessible predictor for IDR ensemble properties is novel. The proteome-wide applications and the concept of "conformational buffering" add original contributions.
- **Scientific importance** The work addresses a significant need in the IDP field. The ability to predict ensemble properties from sequence alone has broad implications for understanding IDR function, interpreting mutations, and designing experiments. The proteome-wide analyses provide a useful resource for the community.
- **Interdisciplinary readership** The work bridges computational biophysics, machine learning, and molecular biology. The tool will be of interest to researchers across these disciplines, and the accessible implementation (Google Colab) lowers barriers for non-specialists.
- **Technical soundness** The technical approach is generally sound, but several concerns need to be addressed: the force field modifications require more detailed justification, the generalization testing needs to be more rigorous, and the benchmarking against existing methods needs to be more comprehensive. The deep learning architecture and training approach appear appropriate.
- **Readability for nonspecialists** The manuscript is generally well-written and accessible. The authors do a good job of explaining concepts for readers who may not be experts in polymer physics or deep learning. However, some sections (particularly the description of the training data generation and the force field modifications) could benefit from additional clarification for non-specialist readers.