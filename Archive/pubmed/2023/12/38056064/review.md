## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, claims, and evidence as presented in the provided manuscript text
- **Shared manuscript claim summary** The manuscript is a review article that addresses common questions about transcriptional activation domains (ADs), covering their definition, sequence features, acidic nature, disorder, molecular grammar, prediction from sequence, and link to phase separation. The authors argue that ADs are poorly understood relative to DNA binding domains, that acidic ADs are governed by a "weak grammar" involving clusters of hydrophobic residues in acidic contexts, and that current predictive models perform reasonably well but have limitations.
- **Visible evidence base** The manuscript cites published literature and includes one figure (Figure 1, Figure 2) and one supplementary table (Table S1) described in the text. The authors also describe their own analysis of collected AD lists from prior studies, including sequence retrieval and merging of overlapping annotations.
- **Missing materials affecting confidence** Figure 1 and Figure 2 are referenced but not provided. Table S1 is referenced but not provided. No methodological details for the sequence collection and merging analysis are given beyond a brief description. No data or code availability statement is provided.

## Reviewer
- **Overall assessment** This is a well-written, engaging, and timely review that synthesizes recent progress in understanding transcriptional activation domains. The organization around common questions is effective and accessible. The authors offer a clear perspective, particularly the "weak grammar" model and the acidic exposure model, and they are appropriately critical of existing frameworks. However, the review's scientific impact is limited by the lack of a systematic or quantitative synthesis of the literature, and some claims are made without sufficient supporting evidence or with only anecdotal citations. The manuscript would benefit from a more rigorous treatment of the evidence base, including a clearer description of the authors' own analysis in Table S1 and a more balanced discussion of alternative viewpoints.
- **Who would be interested in the results, and why** Researchers in transcriptional regulation, gene expression, chromatin biology, and computational biology would find this review useful. It provides a concise update on AD sequence determinants and prediction tools, which is directly relevant to those studying transcription factor function, designing synthetic transcription factors, or developing predictors of regulatory regions. The discussion of phase separation and multivalency also connects to a broad audience interested in biomolecular condensates.
- **Major strengths**
  - Clear and engaging writing style that makes complex topics accessible.
  - Effective organization around common questions, which helps readers navigate the field.
  - Provides a useful synthesis of recent high-throughput datasets and predictive models.
  - Offers a coherent perspective (acidic exposure model, weak grammar) that integrates multiple lines of evidence.
  - Appropriate emphasis on the limitations of current knowledge and tools.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** No
  - **Axis** Evidence sufficiency
  - **Claim pointer** The authors state that "glutamine-rich activation domains are rare (19/760, 2.50%)" and that "the three other classes overlap highly (Figure 1)" based on their collected list of ADs.
  - **Evidence pointer** Table S1, Figure 1, "Are all activation domains acidic?" section
  - **Concern** The authors describe a collection and merging of AD lists from prior studies, but the methodology is only briefly described. The criteria for inclusion, the sources of the lists, the handling of conflicting annotations, and the validation of the merged set are not detailed. The claim of rarity of Q-rich ADs and the overlap between classes depends entirely on this analysis, which is not fully transparent or reproducible from the text.
  - **Why it matters** The quantitative claim about class frequencies is a novel contribution of this review, but without a clear and reproducible methodology, readers cannot assess its validity. This weakens the scientific foundation of the review's perspective.
  - **Resolution test** Provide a detailed methods section for the AD collection and merging, including source databases, inclusion/exclusion criteria, and a description of how overlapping annotations were resolved. Make Table S1 available with full details of each AD, its source, and the merging decisions.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Claim support
  - **Claim pointer** The authors state that "TURBO-ID experiments... suggest that most activation domains preferentially bind to only 1-2 coactivators" and that "different members of a single DBD family (e.g. FOXO) recruited different combinations of the TFIID, CBP/p300, NuA4, and BAF complexes."
  - **Evidence pointer** "What are transcriptional activation domains?" section, reference [16]
  - **Concern** This is a strong and important claim about AD specificity, but it is presented with a single citation and no discussion of the experimental design, the number of ADs tested, the thresholds used to define "preferential binding," or the potential limitations of the TURBO-ID approach. The claim is central to the authors' argument that ADs should be grouped functionally rather than by DBD family.
  - **Why it matters** If this claim is not robust, the authors' recommendation for an "orthogonal organization system" is weakened. The review should provide enough context for readers to judge the strength of this evidence.
  - **Resolution test** Expand the discussion of the TURBO-ID study, including the number of ADs and coactivators tested, the criteria for defining preferential binding, and any caveats. If possible, compare with other interaction mapping studies to assess concordance.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Balance of perspective
  - **Claim pointer** The authors state that "We do not endorse this model" regarding the detergent model of AD function.
  - **Evidence pointer** "Why are activation domains disordered?" section, reference [8,57]
  - **Concern** The detergent model is dismissed without a substantive discussion of the evidence for or against it. The authors present their own acidic exposure model as the preferred explanation, but they do not critically evaluate the detergent model's predictions or the experimental data that support it.
  - **Why it matters** A review should present a balanced view of competing hypotheses, especially when the authors are advocating for their own model. Dismissing an alternative without discussion reduces the review's objectivity and may leave readers without the information needed to form their own opinion.
  - **Resolution test** Add a paragraph that summarizes the detergent model, its supporting evidence, its limitations, and why the authors find it less compelling than the acidic exposure model.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scope and depth
  - **Claim pointer** The review focuses almost exclusively on acidic ADs, with limited discussion of other classes (e.g., proline-rich, serine-rich, Q-rich) beyond noting their overlap with acidic ADs.
  - **Evidence pointer** Throughout the manuscript
  - **Concern** The title and framing suggest a general discussion of transcriptional activation domains, but the content is heavily weighted toward acidic ADs. The authors note that other classes exist and overlap, but they do not discuss whether the acidic exposure model and weak grammar framework apply to non-acidic ADs, or whether these classes have distinct mechanisms.
  - **Why it matters** The review's scope is broader than its content, which may mislead readers seeking a comprehensive overview. A more explicit statement of the review's focus on acidic ADs, or a brief discussion of other classes, would improve clarity and completeness.
  - **Resolution test** Either revise the title and framing to specify a focus on acidic ADs, or add a section that discusses the features and mechanisms of non-acidic AD classes and how they relate to the proposed models.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Definition of activation domains
  - **Evidence pointer** "What are transcriptional activation domains?" section
  - **Issue** The authors note that the term "activation domain" has been applied to both minimized regions and the entirety of the TF outside the DBD, and they state they will use it to refer to short regions. However, this distinction is not consistently maintained throughout the text, and some discussions (e.g., of multivalency) seem to refer to larger regions.
  - **Required correction** Ensure consistent use of the term "activation domain" as defined, or explicitly note when referring to larger regions.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Sequence analysis
  - **Evidence pointer** "Are all activation domains acidic?" section, Table S1
  - **Issue** The description of the sequence retrieval and merging process is brief and lacks details on how isoforms were selected and how overlapping coordinates were merged.
  - **Required correction** Provide a more detailed description of the analysis, including the number of ADs from each source, the number of isoforms considered, and the criteria for merging.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Referencing
  - **Affected element** Citation of companion review
  - **Evidence pointer** "What is the link between activation domains and phase separation?" section
  - **Issue** The text refers to a "companion review by Berlow and colleagues" but does not provide a full citation or reference number.
  - **Required correction** Add the full citation for the companion review.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Figure accessibility
  - **Affected element** Figure 1 and Figure 2
  - **Evidence pointer** Figure legends not provided
  - **Issue** The figures are described in the text but their legends are not included in the provided material, making it difficult to assess what is shown.
  - **Required correction** Ensure figure legends are included and that they clearly describe the data and any statistical analyses.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** "Weak grammar" concept
  - **Evidence pointer** "What is the molecular grammar in activation domains?" section
  - **Issue** The term "weak grammar" is introduced but not formally defined. The authors describe evidence for and against strict and no grammar, but the boundary of "weak grammar" is not clearly delineated.
  - **Required correction** Provide a more explicit definition of "weak grammar" and how it differs from the extremes.
  - **Concern ID** R1-m6
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Discussion of phosphorylation
  - **Evidence pointer** "Are all activation domains acidic?" section
  - **Issue** The authors mention that phosphorylation can modulate AD activity and speculate about inducible acidic ADs, but this is not developed further.
  - **Required correction** Consider expanding this point or explicitly noting it as an open question.

## Technical failings that need to be addressed before the case is established
- The methodology for the AD collection and merging analysis (Table S1) is not described in sufficient detail to be reproducible or to assess the validity of the quantitative claims (R1-M1).
- The claim about AD-coactivator binding preferences from TURBO-ID experiments is presented with insufficient context and critical evaluation (R1-M2).
- The dismissal of the detergent model lacks a balanced discussion of the evidence (R1-M3).

## Risk / unsupported claims
- The quantitative claim that "glutamine-rich activation domains are rare (19/760, 2.50%)" is not fully supported by the provided methodology and is not reproducible from the text.
- The claim that "most activation domains preferentially bind to only 1-2 coactivators" is presented with a single citation and no discussion of experimental limitations.
- The statement that "shuffling activation domain sequence can increase activity in a third of examples" is presented without specifying the exact number or the conditions of the experiments.
- The claim that "scanning for clusters of W,F,L residues in acidic regions performs nearly as well as CNN models for human TFs" is made without quantitative comparison or details of the benchmark.
- The speculation that "acidic activation domains existed in the ancestor of all eukaryotes" is presented as a plausible inference but is not supported by direct evidence.

## Assessment against Nature-style criteria
- **Originality** The review offers a useful synthesis of recent work and introduces a coherent perspective (acidic exposure model, weak grammar) that is not entirely novel but is presented in an accessible and integrative manner. The analysis of AD class frequencies is a new contribution, though its rigor is currently insufficient.
- **Scientific importance** The topic is of broad importance to gene regulation research. The review addresses key questions and highlights open problems, which is valuable for the community. However, the lack of a systematic or quantitative synthesis limits its depth.
- **Interdisciplinary readership** The review is likely to appeal to molecular biologists, biochemists, and computational biologists. The writing is clear and avoids excessive jargon, making it accessible to nonspecialists.
- **Technical soundness** The technical content is generally accurate, but the methodology for the authors' own analysis is not fully described, and some claims are made with insufficient supporting evidence. The review would benefit from a more rigorous treatment of the evidence base.
- **Readability for nonspecialists** The question-based organization and clear prose make the review highly readable. The authors do an excellent job of explaining complex concepts without oversimplifying.

## Recommendation posture
Supportive if technical concerns are resolved. The review is well-written and provides a valuable perspective, but the quantitative claims and the dismissal of alternative models need to be better supported. Specifically, the authors should provide a detailed methodology for their AD collection analysis, expand the discussion of the TURBO-ID evidence, and offer a more balanced treatment of the detergent model. With these revisions, the review would be a strong contribution to the field.