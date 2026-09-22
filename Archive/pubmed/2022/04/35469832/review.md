## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors present DisoMine, a recurrent neural network-based method for predicting long disordered regions in proteins. The method uses predictions of protein dynamics, secondary structure, and early folding, requires only a single sequence, is fast, and is claimed to be a top performer in its category, comparable to methods that use evolutionary information. The tool is available via a webserver.
- **Visible evidence base** Abstract text only; no quantitative performance metrics, benchmark datasets, or methodological details are provided
- **Missing materials affecting confidence** Full manuscript, benchmark results, comparison methodology, training and test datasets, statistical significance tests, webserver implementation details, and any figures or tables

## Reviewer
- **Overall assessment** The abstract presents a potentially useful contribution to the field of disordered protein region prediction, addressing a recognized gap by incorporating protein dynamics predictions into a sequence-based method. The claimed performance and applicability are promising, but the abstract provides insufficient quantitative evidence to evaluate the method's actual performance, robustness, or novelty relative to existing tools. The core claims of "top performer" and "compares well" to evolutionary information-based methods cannot be assessed without benchmark details.
- **Who would be interested in the results, and why** Researchers in computational biology and structural bioinformatics, particularly those working on intrinsically disordered proteins, protein function annotation, and large-scale proteome screening. The method's single-sequence requirement and speed would appeal to users studying poorly characterized or orphan proteins, where evolutionary information is limited.
- **Major strengths** The method addresses a relevant and timely problem in IDR prediction. The incorporation of protein dynamics predictions as input features is a conceptually novel angle. The single-sequence requirement and speed are practical advantages for large-scale applications. The provision of a freely available webserver enhances accessibility and utility.
- **Major Concerns** The abstract lacks any quantitative performance metrics, such as accuracy, precision, recall, or area under the ROC curve, making it impossible to verify the "top performer" claim. No benchmark datasets or comparison methods are specified, so the claim of being "comparable to" evolutionary information-based approaches is unsubstantiated. The definition of "long disorder" is not provided, which is critical for interpreting the method's scope. The novelty relative to existing RNN-based disorder predictors is not clearly articulated.
- **Minor Comments** The abstract would benefit from stating the number of proteins or datasets used for training and testing. The webserver URL is provided, but no information on input limits, runtime, or output format is given. The phrase "simple predictions of protein dynamics" is vague and should specify the source or type of dynamics predictions used.
- **Technical failings that need to be addressed before the case is established** The absence of any performance numbers or benchmark comparisons means the central claims of superior or comparable performance are not established from the provided material.
- **Assessment against Nature-style criteria** Originality: The use of protein dynamics predictions as input features is a novel angle, but the abstract does not demonstrate how this differs fundamentally from existing sequence-based methods. Scientific importance: The problem is important, and a fast single-sequence method would be valuable, but the abstract does not show a clear advance over existing tools. Interdisciplinary readership: The topic is of interest to structural biologists and bioinformaticians, but the abstract is too brief to engage a broader audience. Technical soundness: Cannot be assessed without methodological details and benchmark results. Readability for nonspecialists: The abstract is clear and accessible, though terms like "early folding" and "long disorder" could be better defined.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a plausible method, but the lack of quantitative results and benchmark comparisons prevents a supportive recommendation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Performance claim
- **Claim pointer** "DisoMine is a top performer in its category and compares well to disorder prediction approaches using evolutionary information."
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract claims top-tier performance and comparability to evolutionary information-based methods, but no performance metrics, benchmark datasets, or statistical comparisons are provided.
- **Why it matters** Without quantitative evidence, the central claim of the method's utility cannot be verified, and readers cannot judge whether DisoMine offers a genuine advance over existing tools.
- **Resolution test** Provide performance metrics (e.g., AUC, precision, recall) on standard benchmark datasets, with comparisons to at least two existing disorder predictors, including one using evolutionary information, and report statistical significance.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological clarity
- **Claim pointer** "DisoMine, a method that predicts protein'long disorder' with recurrent neural networks from simple predictions of protein dynamics, secondary structure and early folding."
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract does not define "long disorder" or specify the nature of the "simple predictions" of protein dynamics, secondary structure, and early folding. The source and type of these predictions are unclear.
- **Why it matters** The method's scope and input features are central to its applicability and reproducibility. Without clear definitions, the method cannot be replicated or compared fairly with other predictors.
- **Resolution test** Define the length threshold for "long disorder" and specify the exact predictors or algorithms used to generate the dynamics, secondary structure, and early folding inputs, including any training data.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Novelty
- **Claim pointer** "Here we present DisoMine, a method that predicts protein'long disorder' with recurrent neural networks from simple predictions of protein dynamics, secondary structure and early folding."
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract does not clearly articulate how DisoMine differs from existing RNN-based disorder predictors, beyond the inclusion of dynamics predictions. The novelty of the approach is not established.
- **Why it matters** For a new method to be of interest, its unique contribution must be explicit. Without this, the method may be seen as an incremental variation on existing tools.
- **Resolution test** Provide a clear statement of the methodological innovation, ideally with a comparison to a baseline RNN-based predictor that does not use dynamics features, showing a significant improvement.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract text
- **Evidence pointer** Abstract; location not provided
- **Issue** The phrase "simple predictions of protein dynamics" is vague and could be misinterpreted.
- **Required correction** Specify the type of dynamics predictions used (e.g., backbone flexibility, B-factors, or molecular dynamics-derived properties) and the source of these predictions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Webserver description
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract mentions a freely available webserver but provides no details on input requirements, runtime, or output format.
- **Required correction** Add a brief description of the webserver's functionality, including input sequence format, typical runtime, and output interpretation.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scope
- **Affected element** Abstract text
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract does not state the number of proteins or datasets used for training and testing, which limits the reader's ability to gauge the method's generalizability.
- **Required correction** Include a brief statement on the training and test dataset sizes and diversity.

## Risk / unsupported claims
- The claim that DisoMine is a "top performer" is unsupported due to the absence of any performance metrics or benchmark comparisons.
- The claim that DisoMine "compares well" to evolutionary information-based methods is unsupported without specific comparative results.
- The applicability of DisoMine to "poorly studied and orphan proteins" is plausible but not demonstrated with examples or case studies.
- The speed of the method is claimed but not quantified, making the "fast" claim unverifiable.