## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods, conclusions)
- **Assessment boundary** Scientific content, methodological soundness, evidence quality, and interpretation as presented in the manuscript
- **Shared manuscript claim summary** The authors report the first comprehensive in silico characterisation of 318 late embryogenesis abundant (LEA) proteins from the resurrection plant *Ramonda serbica*, integrating transcriptomic data, physicochemical analysis, structural prediction, and differential expression to propose functional roles in desiccation tolerance
- **Visible evidence base** Supplementary Tables S1–S5, Supplementary Figures S1–S12, Table 1, Table 2, Table 3, Table 4, Figure 1, Figure 2, Figure 3, Figure 4, Figure 5, Figure 6
- **Missing materials affecting confidence** Raw RNA-seq data quality metrics (only summarised in Table S1), detailed statistical outputs for differential expression analysis, validation data for structural predictions, experimental confirmation of predicted functions, and complete motif analysis parameters

## Reviewer
- **Overall assessment** This manuscript presents a substantial bioinformatics effort characterising LEA protein families in a resurrection plant species. The scale of analysis (318 proteins) and the integration of multiple prediction tools represent a useful contribution to the field. However, the study is entirely computational, and the functional claims extend considerably beyond what the evidence can support. The differential expression analysis is presented with insufficient methodological detail, and the connection between structural predictions and proposed physiological functions remains speculative. The manuscript would benefit from clearer presentation of the statistical framework and more cautious interpretation of predicted functions.

- **Who would be interested in the results, and why** Researchers studying desiccation tolerance mechanisms in plants, particularly those working on resurrection species and LEA proteins. The comprehensive catalogue of LEA proteins in *R. serbica* and the structural predictions could serve as a reference dataset for comparative studies. Plant biotechnology researchers interested in drought tolerance improvement may find the identification of candidate genes for further testing useful. The study also provides a methodological template for similar transcriptome-based analyses in non-model species.

- **Major strengths** The study addresses a relevant topic with potential applications in crop improvement. The authors have generated a substantial dataset of 318 LEA proteins, which represents a significant resource. The use of multiple prediction tools for structural analysis is methodologically thorough. The classification into seven families with detailed physicochemical characterisation provides a systematic framework. The integration of expression data with structural predictions, while speculative in places, offers hypotheses for future experimental testing.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that 88 genes were differentially expressed upon desiccation with a threshold of FDR < 0.05 and log2 fold change > 2, and that 76% were upregulated and 24% downregulated
- **Evidence pointer** Section 2.7, Table 4, location not provided
- **Concern** The differential expression analysis is described with insufficient methodological detail. The authors state thresholds but do not provide information on the number of biological replicates, the statistical model used, how library size normalisation was performed, or how the FDR was calculated. The DEGseq package is mentioned, but the specific parameters and the quality of the underlying read counts are not described. Without this information, the reliability of the differential expression results cannot be assessed.
- **Why it matters** The differential expression data form a core component of the functional interpretation. If the statistical framework is inadequate, the conclusions about which LEA genes are desiccation-responsive may be unreliable, undermining the central claims of the study.
- **Resolution test** The authors should provide complete details of the experimental design, including replicate numbers, sequencing depth per sample, the exact statistical model and parameters used in DEGseq, and the distribution of p-values. Ideally, the raw count data and analysis scripts should be made available for independent verification.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The authors propose specific physiological functions for LEA protein families, including roles in liquid-liquid phase separation, membrane stabilisation, metal chelation, and DNA binding during desiccation
- **Evidence pointer** Sections 3.5.1-3.5.7, Figure 5, Supplementary Table S3
- **Concern** The functional claims extend well beyond what computational predictions can establish. While the authors acknowledge that their findings are in silico, the discussion presents proposed functions with a level of confidence that is not warranted by the evidence. For example, the claim that specific proteins "might be involved in LLSP-related dynamic assembly of nuclear compartments" is based solely on disorder predictions and sequence motifs, with no experimental validation. The leap from predicted structural features to physiological function is substantial and requires experimental support.
- **Why it matters** The stated aim of the study is to understand the role of LEA proteins in desiccation tolerance. If the functional interpretations are not adequately supported, the study provides a catalogue of sequences but does not meaningfully advance mechanistic understanding. Overinterpretation of computational predictions can mislead subsequent research efforts.
- **Resolution test** The authors should either provide experimental evidence supporting at least some of the proposed functions, or substantially temper their functional claims, clearly distinguishing between hypotheses generated by the analysis and established findings. The discussion should explicitly state which claims require experimental validation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "more than 55% of the identified LEA proteins were found to be disordered (>50% of the sequence length)" and that specific families show characteristic secondary structure propensities
- **Evidence pointer** Section 2.4, Figure 3, Supplementary Table S3
- **Concern** The manuscript reports results from five secondary structure predictors and four disorder estimators but does not describe how disagreements between predictors were resolved. It is unclear whether the reported values represent consensus predictions, averages, or results from a single preferred tool. The variability between prediction methods for intrinsically disordered proteins is well documented, and the choice of method can substantially affect the results.
- **Why it matters** The structural predictions form the basis for the functional interpretations. If the methodology for combining predictions is not transparent, the reliability of the structural characterisation is uncertain, and the downstream functional claims are correspondingly weakened.
- **Resolution test** The authors should describe how results from multiple predictors were integrated, provide information on inter-method agreement, and justify the choice of methods. Ideally, the per-protein predictions from each tool should be made available as supplementary data.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interdisciplinary readership
- **Claim pointer** The authors claim that the "comprehensive LEA proteins structural characterisation is essential to understanding their function and regulation during desiccation aiming at crop drought tolerance improvement"
- **Evidence pointer** Abstract, Section 3, Section 5
- **Concern** The manuscript does not adequately address how the findings translate to crop improvement strategies. The connection between the characterisation of LEA proteins in a resurrection plant and practical applications in crop drought tolerance is asserted but not developed. The discussion does not consider how the identified candidate genes might be tested in crop species, what specific traits might be targeted, or what the limitations of such translational approaches might be.
- **Why it matters** The stated motivation for the study includes crop improvement, and this framing is used to justify the importance of the work. If the translational relevance is not substantively addressed, the broader significance of the study is diminished, and the manuscript may not engage readers beyond the specialist resurrection plant community.
- **Resolution test** The authors should either provide a more developed discussion of how their findings could inform crop improvement efforts, including specific candidate genes and testing strategies, or reframe the significance of the study to focus on the fundamental understanding of desiccation tolerance mechanisms.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction, Section 1
- **Evidence pointer** Location not provided
- **Issue** The introduction assumes familiarity with LEA protein classification and desiccation tolerance mechanisms. Terms such as "intrinsically disordered proteins," "molecular shields," and "liquid-liquid phase separation" are introduced without sufficient context for readers outside the immediate field.
- **Required correction** Provide brief definitions or explanations of key concepts when first introduced, and consider adding a short paragraph on the biological context of desiccation tolerance in plants.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section 4.3, identification and classification of LEA proteins
- **Evidence pointer** Location not provided
- **Issue** The criteria for including proteins in the LEA list are described as requiring sequence identity > 90% to known LEA proteins, but the reference set used for this comparison is not clearly defined. It is unclear whether this threshold was applied against the best hit in the NCBI NR database or against a curated LEA protein set.
- **Required correction** Clarify the reference database and the exact criteria used for inclusion, including how the 90% identity threshold was applied and whether coverage of the query sequence was considered.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section 4.8, 3D protein structure modelling
- **Evidence pointer** Location not provided
- **Issue** The description of Colabfold and AlphaFold2 usage is minimal. The authors do not specify whether templates were used, what confidence metrics were applied beyond PAE, or how many models were generated per protein.
- **Required correction** Provide additional details on the modelling parameters, including the number of recycles, whether relaxation was performed, and how model quality was assessed.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Section 3.5.5, LEA4 protein family group
- **Evidence pointer** Location not provided
- **Issue** The discussion of LEA4 proteins and their potential role in membrane stabilisation relies heavily on analogy with other species. The authors do not discuss potential alternative explanations for the observed sequence features or consider whether the predicted amphipathic helices might have other functions.
- **Required correction** Acknowledge alternative interpretations and discuss the limitations of drawing functional conclusions from sequence-based predictions alone.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Figure 5
- **Evidence pointer** Location not provided
- **Issue** The figure presents 3D models of representative proteins but the caption does not explain how to interpret the colouring, the PAE values, or the significance of the structural features highlighted.
- **Required correction** Expand the figure caption to explain the visual elements and what conclusions can be drawn from the models.

## Risk / unsupported claims
- The claim that specific LEA proteins "might be involved in LLSP-related dynamic assembly of nuclear compartments" is unsupported by direct evidence and relies entirely on computational prediction
- The assertion that the study "will pave the way for identifying LEA proteins endogenous partners and their target molecules" is speculative and not substantiated by the presented data
- The functional distinction between desiccation-upregulated and downregulated LEA families is presented as biologically meaningful, but the statistical robustness of the differential expression analysis cannot be verified from the information provided
- The claim that the high number of LEA proteins in *R. serbica* "indicate that they confer an evolutionary advantage" is an interpretation that cannot be tested with the current data
- The proposed mechanism of membrane stabilisation via amphipathic alpha-helices for LEA4 proteins is presented with more certainty than the computational evidence warrants