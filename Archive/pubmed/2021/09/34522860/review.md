## Review setup
- **Input scope** Full manuscript text, including Summary, Introduction, Results, Discussion, Methods, and figure legends
- **Assessment boundary** Scientific claims, methodological soundness, data interpretation, and alignment with stated conclusions
- **Shared manuscript claim summary** The authors use machine learning analyses of two published yeast tAD datasets to derive sequence features governing tAD function, and interpret these features as supporting a "nucleosome detergent" model of transcriptional activation over the direct recruitment model
- **Visible evidence base** Two publicly available tAD datasets (Gcn4, HSF1); regression and neural network analyses; figure panels referenced in text
- **Missing materials affecting confidence** Raw data files, full figure images, supplemental figures S1–S5, code implementation details, hyperparameter settings, and validation metrics beyond AUC

## Reviewer

- **Overall assessment** This manuscript addresses a long-standing question in eukaryotic transcription: how transcriptional activation domains function despite lacking sequence conservation and specific target interactions. The authors apply machine learning to existing large-scale datasets and derive interpretable sequence features. The analysis is competent and the findings are potentially interesting, but the central interpretive leap from sequence statistics to a mechanistic model of nucleosome distortion is not directly tested. The manuscript would be strengthened by clearer acknowledgment of what the analysis can and cannot establish, and by tempering claims that exceed the evidence.

- **Who would be interested in the results, and why** Researchers studying transcriptional regulation, intrinsically disordered proteins, and the biochemistry of activation domains. The machine learning approach and the derived sequence rules may also interest computational biologists working on sequence-function relationships in disordered regions. The proposed "near-noise interaction" framework could attract attention from those studying phase separation and weak multivalent interactions.

- **Major strengths** 
  1. The use of large, unbiased in vivo datasets is a significant improvement over anecdotal analyses of individual activation domains
  2. The cross-validation between two different activator contexts (Gcn4 and HSF1) strengthens the generality of the derived rules
  3. The interpretability of the ML models (ridge/lasso coefficients) provides concrete, testable sequence features
  4. The attention-LSTM approach adds methodological novelty and modestly improves prediction accuracy

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim-evidence alignment
- **Claim pointer** The manuscript repeatedly states that the findings are "compatible with" and "consistent with" the nucleosome detergent model, and the title asserts that detergent-like protein domains activate gene expression
- **Evidence pointer** Discussion section, "Comparison of models describing gene activation"; Summary
- **Concern** The analysis is purely bioinformatic and correlative. No direct experimental test distinguishes the nucleosome detergent model from the direct recruitment model. The sequence features identified (enrichment of aromatic and acidic residues, depletion of basic residues) are equally compatible with models involving weak multivalent interactions with coactivators, phase separation, or other mechanisms. The title and framing overstate what the data can establish.
- **Why it matters** The central mechanistic claim is not tested. Readers may be misled into thinking the study provides direct evidence for a specific mechanism when it provides sequence correlations that are interpreted through one particular lens.
- **Resolution test** Either (a) add direct experimental evidence (e.g., in vitro nucleosome distortion assays with designed tAD variants), or (b) substantially reframe the claims to explicitly state that the analysis identifies sequence features consistent with, but not proof of, the detergent model, and revise the title accordingly.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Methodological transparency
- **Claim pointer** The attention-LSTM model achieves 98.3% AUC, presented as an improvement over prior methods
- **Evidence pointer** Results section, "tAD function"; Figure 7B; STAR Methods
- **Concern** The description of the attention-LSTM architecture and training procedure is incomplete. Key details such as embedding dimensions, number of LSTM layers, dropout rates, and the specific attention mechanism formulation are not fully specified. The comparison between ridge regression and LSTM uses different decision thresholds, which complicates direct comparison. The claim of "slightly better accuracy" is based on a single metric (AUC) without confidence intervals or statistical testing.
- **Why it matters** Reproducibility is a core expectation for computational analyses. Without complete methodological detail, other groups cannot replicate or build upon this work. The performance comparison may not be robust.
- **Resolution test** Provide complete architecture specifications, hyperparameter values, and code documentation. Report confidence intervals for AUC or perform statistical comparison of model performances. Clarify whether the threshold optimization procedure was applied consistently across methods.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The derived rules are presented as general principles of tAD function ("the functionality rules are similar" across Gcn4 and HSF1 contexts)
- **Evidence pointer** Results section, "Absence of basic and presence of acidic and aromatic amino acid residues"; Figure 2B
- **Concern** Only two activator contexts are analyzed, both from yeast. The correlation of feature importance between datasets is presented without statistical quantification. The claim of generality across eukaryotic transcription is not supported by the taxonomic and contextual diversity of the data.
- **Why it matters** Overgeneralization from two datasets could mislead the field about the universality of the proposed rules. Different activators in different organisms may use different strategies.
- **Resolution test** Either analyze additional datasets from diverse contexts, or explicitly limit the claims to the yeast systems studied and note that broader generality remains to be tested.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Alternative explanations
- **Claim pointer** The analysis of net-positively charged functional sequences is interpreted as consistent with the same general rule, with cysteine acquiring importance due to deprotonation
- **Evidence pointer** Results section, "Within the basic microenvironment, cysteine becomes more important for tAD function"; Figure 8
- **Concern** The interpretation of cysteine's role is speculative. The pKa argument is plausible but untested. Alternative explanations (e.g., disulfide bonding, metal coordination, or context-dependent effects) are not considered. The claim that "the functionality rules are the same" for this subpool is asserted but the analysis shows notable differences (diminished role of acidic residues).
- **Why it matters** The interpretation may be incorrect, and the assertion of unified rules may obscure meaningful differences in how different tAD subpopulations function.
- **Resolution test** Provide direct biochemical evidence for cysteine deprotonation in the context of these sequences, or soften the interpretation and acknowledge alternative possibilities.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Title
- **Evidence pointer** Title
- **Issue** The title asserts a mechanistic conclusion ("detergent-like protein domains") that the study does not directly test
- **Required correction** Revise to reflect the correlative nature of the findings, e.g., "Sequence features of functional transcriptional activation domains revealed by machine learning"

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 2B correlation
- **Evidence pointer** Figure 2B
- **Issue** The correlation between ridge coefficients for the two datasets is described qualitatively ("similar") without a correlation coefficient or significance test
- **Required correction** Report the correlation coefficient and p-value, or state that the similarity is qualitative

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Detergent-like" and "near-noise" terminology
- **Evidence pointer** Throughout
- **Issue** These terms are used without precise operational definitions. "Detergent-like" is metaphorical, and "near-noise" is not quantitatively defined
- **Required correction** Provide explicit definitions or use more neutral descriptive language

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Limitations section
- **Evidence pointer** Discussion
- **Issue** The limitations of the study are acknowledged only briefly in the "Limitations of the study" subsection, but several additional limitations (e.g., binary functional classification, potential dataset biases, lack of direct mechanistic tests) are not discussed
- **Required correction** Expand the limitations discussion to include these points

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure accessibility
- **Affected element** Figures 1–8
- **Evidence pointer** Figure legends
- **Issue** Figure legends are present but some are terse and do not fully explain all panels, statistical annotations, or color scales
- **Required correction** Expand figure legends to be self-contained

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Code availability
- **Evidence pointer** Data and code availability section
- **Issue** Code is deposited but the manuscript does not specify the computing environment, package versions, or random seeds used
- **Required correction** Add environment specifications and random seeds to the methods or code repository

## Risk / unsupported claims
- The title's assertion of "detergent-like protein domains" activating gene expression is not directly supported by the data presented
- The claim that findings support the nucleosome detergent model over the direct recruitment model is an interpretive preference, not a tested hypothesis
- The interpretation of cysteine's role in net-positively charged tADs via deprotonation is speculative and untested
- The claim of general rules for tAD function across eukaryotes is extrapolated from two yeast datasets
- The statement that "near-noise interactions can be central for the fundamental function of gene expression initiation" is a philosophical framing rather than an empirically established conclusion
- The comparison between ridge regression and LSTM performance lacks statistical rigor (no confidence intervals, no significance testing)