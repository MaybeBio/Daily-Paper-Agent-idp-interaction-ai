## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract
- **Shared manuscript claim summary** The authors introduce PSICHIC, a physicochemical graph neural network that predicts protein-ligand binding affinity and functional effects using only sequence data, without structural information. They claim state-of-the-art accuracy, interpretability, and emergent capabilities in identifying interaction mechanisms, supported by a case study on adenosine A1 receptor agonists.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary materials provided
- **Missing materials affecting confidence** Full manuscript, methods details, dataset descriptions, baseline comparisons, statistical analyses, and the screening case study results are not available

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting approach to protein-ligand interaction prediction from sequence data alone, with claims of state-of-the-art performance and interpretability. However, the evidence provided is insufficient to evaluate the validity of these claims. The central novelty, methodological soundness, and robustness of the reported results cannot be assessed without the full manuscript. The screening case study, while promising, lacks quantitative detail. The abstract is well written and accessible, but the scientific case is not established from the supplied material.
- **Who would be interested in the results, and why** Computational chemists, medicinal chemists, and structural biologists involved in virtual screening and drug discovery would be interested, as the method promises to bypass the need for high-resolution protein structures. Researchers working on graph neural networks for molecular property prediction and interpretable AI in chemistry would also find the approach relevant.
- **Major strengths** The proposed framework addresses a practical limitation in drug discovery, namely the reliance on structural data. The claim of interpretable fingerprints is valuable for mechanistic understanding. The screening case study, if robust, demonstrates a functional application beyond affinity prediction.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality is potentially high, as the combination of physicochemical constraints with sequence-only input for interaction fingerprint decoding appears novel. Scientific importance is significant if the claims hold, given the broad applicability to drug discovery. Interdisciplinary readership is plausible, spanning machine learning, chemistry, and pharmacology. Technical soundness cannot be evaluated from the abstract alone. Readability for nonspecialists is good, with clear language and a logical flow, though some terms such as "interaction fingerprints" and "physicochemical constraints" may require further explanation in the full text.
- **Recommendation posture** Currently not established from the provided evidence. The abstract is promising, but the core claims require full manuscript evaluation. A supportive posture is possible if the technical concerns are resolved.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "PSICHIC matched and even surpassed leading structure-based methods in binding affinity prediction"
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract claims that PSICHIC outperforms structure-based methods, but no quantitative results, benchmark datasets, or baseline method names are provided. It is unclear which structure-based methods were compared, on which datasets, and with what metrics.
- **Why it matters** Without specific performance numbers and a clear comparison protocol, the claim of state-of-the-art accuracy cannot be verified. This is central to the paper's contribution.
- **Resolution test** Provide a table or figure in the full manuscript with binding affinity prediction results on standard benchmarks, including error bars, statistical significance tests, and a list of compared methods.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "PSICHIC discerned functional effects effectively, ranking the sole novel agonist within the top three"
- **Evidence pointer** Abstract, location not provided
- **Concern** The screening case study is described in a single sentence without details on the library size, the number of known agonists, the assay used, or the criteria for ranking. The claim of "effective" discrimination is not supported by any quantitative measure such as enrichment factor or ROC curve.
- **Why it matters** Functional effect prediction is a key differentiator of the method. Without a clear experimental design and quantitative outcome, the claim remains anecdotal.
- **Resolution test** Include a detailed description of the screening experiment, including library composition, hit criteria, and a statistical evaluation of the ranking performance.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** "PSICHIC’s interpretable fingerprints identified protein residues and ligand atoms involved in interactions"
- **Evidence pointer** Abstract, location not provided
- **Concern** The interpretability claim is not accompanied by any example, validation, or comparison with known interaction data. It is unclear how the fingerprints are derived and whether they are biologically meaningful.
- **Why it matters** Interpretability is a major selling point. Without evidence that the identified residues and atoms correspond to known interaction sites, the claim is unsubstantiated.
- **Resolution test** Provide a figure showing predicted interaction fingerprints for a known complex, with validation against crystallographic or mutagenesis data.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract, first sentence
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "determining the binding affinity and functional effects" is broad and could be clarified to specify the types of functional effects (e.g., agonism, antagonism).
- **Required correction** Specify the range of functional effects considered in the study.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract, "interaction fingerprints"
- **Evidence pointer** Abstract, location not provided
- **Issue** The term "interaction fingerprints" is not defined in the abstract, which may confuse nonspecialist readers.
- **Required correction** Provide a brief definition or example of what constitutes an interaction fingerprint in this context.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Abstract, "emergent capabilities"
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "first-of-its-kind emergent capabilities" is vague and not supported by specific examples in the abstract.
- **Required correction** Clarify what emergent capabilities are demonstrated and how they differ from existing methods.

## Risk / unsupported claims
- The claim of "state-of-the-art accuracy" is unsupported without quantitative benchmarks.
- The claim of "effective" functional effect discrimination is unsupported without experimental details.
- The claim of "interpretable fingerprints" identifying specific residues and atoms is unsupported without validation examples.
- The claim of "first-of-its-kind emergent capabilities" is not verifiable from the abstract alone.