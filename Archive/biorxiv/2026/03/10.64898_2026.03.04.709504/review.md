## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, methods, supplementary figure/table legends, and funding/acknowledgment sections.
- **Assessment boundary** Scientific validity, methodological soundness, clarity of claims, and adequacy of evidence as presented in the provided text. No external data or code were accessed.
- **Shared manuscript claim summary** The authors present SLiMMine, a deep learning-based method for predicting short linear motifs (SLiMs) in the human proteome. They claim high accuracy in identifying novel SLiM instances within known classes, elimination of ~80% of pattern-matching false positives, de novo discovery of uncharacterized SLiMs, and linkage of predicted motifs to specific protein-protein interactions via refined partner annotations.
- **Visible evidence base** Abstract, Introduction, Results sections (including descriptions of Figures 1-5), Methods sections (including training, test, and independent datasets), and supplementary table/figure legends. No actual figures, tables, or supplementary data files were provided for inspection.
- **Missing materials affecting confidence** All figures, tables, supplementary materials (STables 1-22, SFigures 1-13, SMaterial), and code/data repositories (Zenodo links) were referenced but not accessible. This severely limits the ability to verify quantitative claims, assess data quality, or evaluate methodological details.

## Reviewer
- **Overall assessment** The manuscript addresses a significant problem in the field of SLiM biology: the high false-positive rate in computational motif identification. The proposed method, SLiMmine, leverages protein embeddings and neural networks, which is a modern and potentially powerful approach. The authors have clearly invested substantial effort in data curation, model development, and validation across multiple independent datasets. However, the manuscript as presented has several critical weaknesses. The most significant is the lack of accessible data and code, making the core claims unverifiable. Furthermore, the description of the methodology is incomplete in key areas, particularly regarding the construction of negative datasets, the handling of class imbalance, and the precise architecture of the neural networks. The claim of "de novo" discovery is also somewhat overstated, as the method still relies on sequence context and does not appear to identify entirely novel motif classes. The case studies are promising but are presented as anecdotal evidence without quantitative benchmarks. The manuscript would be significantly strengthened by making all data and code publicly available, providing a more detailed and rigorous description of the methods, and including a more critical discussion of the limitations and potential biases in the training and evaluation process.
- **Who would be interested in the results, and why** Researchers in the fields of computational biology, bioinformatics, and molecular biology, particularly those studying intrinsically disordered proteins, protein-protein interactions, cell signaling, and regulatory networks. The web server provides a practical tool for experimentalists seeking to identify functional motifs in their proteins of interest. The methodological approach may also be of interest to machine learning researchers working on protein sequence analysis.
- **Major strengths**
    1.  Addresses a critical, well-recognized problem in the field (high false-positive rate in SLiM prediction).
    2.  Employs a modern, sophisticated approach (protein embeddings, neural networks) that is well-suited to the challenge.
        3.  Demonstrates a strong commitment to data curation and refinement of existing annotations (ELM_refined), which is a valuable contribution in itself.
    4.  Validation on multiple independent datasets, including experimental data (ProP-PD, cyclin-binding, phospho-modulated, essential motifs, LMPID), is a major strength.
    5.  The provision of a user-friendly web server is a significant practical contribution to the community.
- **Major Concerns**
    - **R1-M1**
        - **Severity** Major
        - **Blocking** Yes
        - **Axis** Reproducibility and Data Availability
        - **Claim pointer** The manuscript claims that SLiMMine is a reliable and accurate method, with specific performance metrics (e.g., 94% accuracy for intracellular motifs, 0.98 specificity for de novo prediction).
        - **Evidence pointer** All figures, tables, and supplementary materials (STables 1-22, SFigures 1-13) are referenced but not provided. Code and data are only available via external Zenodo links.
        - **Concern** The core evidence for the manuscript's claims is entirely contained in inaccessible supplementary materials and external repositories. Without access to the data, figures, and code, it is impossible to verify the reported performance metrics, assess the quality of the training and test sets, or evaluate the methodological details. This is a fundamental barrier to scientific review and reproducibility.
        - **Why it matters** A scientific claim is only as strong as its supporting evidence. If the data and code are not available for scrutiny, the claims cannot be validated, and the work cannot be built upon by the community. This is a prerequisite for publication in a high-impact venue.
        - **Resolution test** The authors must provide all supplementary materials, including figures, tables, and detailed legends, as part of the manuscript submission. The code and data must be made publicly available in a stable, accessible repository (e.g., Zenodo, GitHub) and the links must be active and functional.
    - **R1-M2**
        - **Severity** Major
        - **Blocking** Yes
        - **Axis** Methodological Rigor and Clarity
        - **Claim pointer** The manuscript claims that the method can "reliably predict" SLiMs and "eliminate ~80% of the pattern matching-based hits as false-positives."
        - **Evidence pointer** Methods section, "Defining motif labels" and "Architectures and training" sections.
        - **Concern** The description of the negative dataset construction is insufficient. The authors state that negative data were selected based on criteria such as "protein localization is not appropriate," "not conserved," "buried in a monomeric structure," and "did not bind in ProP-PD experiments." However, the exact algorithm for selecting and weighting these negative examples is not described. For instance, how were these criteria combined? What was the ratio of different types of negatives? How was the potential bias introduced by using ProP-PD negatives (which are only available for a limited set of domains) addressed? Furthermore, the architecture of the neural networks is only described as "fully connected and convolutional" with a reference to a supplementary figure. The number of layers, hidden units, activation functions, regularization techniques, and training hyperparameters are not specified. This lack of detail prevents replication and makes it difficult to assess the robustness of the method.
        - **Why it matters** A machine learning method is defined by its training data and architecture. Without a precise description of both, the method is not reproducible, and the reported performance cannot be independently verified. The potential for bias in the negative set is a serious concern that could lead to inflated performance metrics.
        - **Resolution test** The authors must provide a complete and detailed description of the negative dataset construction, including the exact criteria, their relative weights, and the final composition of the negative set. They must also provide a full architectural description of all neural networks used, including layer sizes, activation functions, regularization, and training procedures. This information should be in the main text or a detailed methods supplement.
    - **R1-M3**
        - **Severity** Major
        - **Blocking** No
        - **Axis** Claim Substantiation and Overstatement
        - **Claim pointer** The manuscript claims that SLiMMine "functions as a discovery tool to find uncharacterized SLiMs" and can identify "de novo SLiMs that do not necessarily belong to the already defined classes."
        - **Evidence pointer** Results section, "SLiMMine enables the discovery of novel motifs that may not adhere to existing class definitions" and Discussion.
        - **Concern** The claim of "de novo" discovery is not fully substantiated. The method is trained on known SLiM classes and their properties. The "de novo" mode appears to identify regions that have high "SLiM-like" characteristics based on this learned knowledge, but it does not appear to identify entirely new classes of motifs with novel binding partners or functions. The examples provided (e.g., the Stonin-2 motif, the Dynein 2 intermediate chain 2 motif) are all variations of known motif types (alpha-ear domain-binding, dynein light chain-binding). While identifying atypical variants is valuable, it is not the same as discovering a new class of motif. The term "de novo" is therefore misleading.
        - **Why it matters** Overstating the capabilities of a method can mislead the community and lead to inappropriate use. The distinction between finding novel instances of known classes and discovering entirely new classes is scientifically important.
        - **Resolution test** The authors should either provide evidence that SLiMMine can identify a genuinely novel class of SLiM (e.g., with a new binding partner not previously associated with SLiMs) or temper their claims to accurately reflect that the method identifies atypical variants and new instances of known classes.
    - **R1-M4**
        - **Severity** Major
        - **Blocking** No
        - **Axis** Benchmarking and Comparative Analysis
        - **Claim pointer** The manuscript claims that SLiMMine "reliably predicts" SLiMs and outperforms "traditional conservation and protein disorder-based analyses, as well as AIUPred-binding."
        - **Evidence pointer** Results section, "Accurate prediction of Short Linear Motifs" and Figure 2.
        - **Concern** While the authors benchmark against AIUPred-binding and a "classical approach," they do not compare SLiMMine to other modern SLiM prediction tools, such as SLiMPrints, SLiMSearch, or other deep learning-based methods. A comprehensive comparison against the current state-of-the-art is essential to demonstrate that SLiMMine represents a significant advancement. Furthermore, the evaluation on independent datasets is described, but the details of how these datasets were processed and how the performance metrics (e.g., accuracy, specificity) were calculated are not fully clear.
        - **Why it matters** To establish that a new method is a "large step forward," it must be shown to be superior to existing tools on standard benchmarks. Without such a comparison, the relative value of SLiMMine is unclear.
        - **Resolution test** The authors should include a comparative analysis against at least one or two other modern SLiM prediction methods on the same independent test sets. They should also provide a clear definition of all performance metrics used.
- **Minor Comments**
    - **R1-m1**
        - **Severity** Minor
        - **Axis** Clarity and Presentation
        - **Affected element** Figure 1
        - **Evidence pointer** Results section, "Refinement of ELM class annotations..." and Figure 1.
        - **Issue** The description of Figure 1 is complex and refers to multiple panels (A, B, C, D) without a clear explanation of the workflow. The text mentions "Figure 1/A", "Figure 1/B", "Figure 1/C", and "Figure 1/D" but the overall flow of the figure is not described in the text.
        - **Required correction** The authors should provide a more detailed and structured description of Figure 1 in the text, explaining the purpose of each panel and how they relate to the overall method.
    - **R1-m2**
        - **Severity** Minor
        - **Axis** Clarity and Presentation
        - **Affected element** Results section, "SLiMMine predictions can be linked to protein-protein interaction (PPI) data..."
        - **Evidence pointer** Results section, "SLiMMine predictions can be linked to protein-protein interaction (PPI) data..."
        - **Issue** The claim that the method can "explain underlying binding mechanisms" for "more than 50 000 human PPIs" is very strong. The text states that the method "suggests" interaction mechanisms, which is more appropriate. The initial phrasing is an overstatement.
        - **Required correction** The authors should consistently use language that reflects the predictive and suggestive nature of their results, rather than definitive explanations.
    - **R1-m3**
        - **Severity** Minor
        - **Axis** Clarity and Presentation
        - **Affected element** Methods section, "Independent test sets"
        - **Evidence pointer** Methods section, "Independent test sets"
        - **Issue** The description of the independent test sets is brief. For example, the criteria for "high-confidence hits" from the cyclin-binding dataset and the "high-confidence non-redundant peptide hits" from the phospho-modulated dataset are not defined.
        - **Required correction** The authors should provide the specific criteria used to define "high-confidence" for each independent dataset.
    - **R1-m4**
        - **Severity** Minor
        - **Axis** Clarity and Presentation
        - **Affected element** Discussion
        - **Evidence pointer** Discussion section.
        - **Issue** The Discussion section is somewhat general and does not critically evaluate the limitations of the method. For example, the potential for bias in the training data, the performance on different types of SLiMs, and the generalizability to non-human proteomes are not discussed in depth.
        - **Required correction** The authors should add a more balanced discussion of the limitations and potential failure modes of their method.

## Risk / unsupported claims
- The claim of "reliably predicts" is not fully supported without access to the data and detailed methodology.
- The claim of "de novo" discovery of SLiMs is overstated, as the method appears to identify variants of known classes rather than entirely new classes.
- The claim of "explain underlying binding mechanisms" for 50,000 PPIs is too strong; the method "suggests" mechanisms.
- The quantitative performance metrics (e.g., 94% accuracy, 0.98 specificity) are unverifiable without the actual data and figures.
- The claim that SLiMMine "eliminates ~80% of the pattern matching-based hits as false-positives" is a key quantitative result that cannot be assessed without the underlying data.
- The generalizability of the method to other organisms, as suggested in the Discussion, is not tested and is therefore an unsupported claim.