## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, data availability, supplementary data statement)
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text. Figures, tables, and supplementary materials referenced but not provided are assessed only insofar as their described content supports the claims.
- **Shared manuscript claim summary** The authors report that YY1 contains two nucleic acid binding domains: the canonical C-terminal four zinc-finger (ZnF) module and a previously unannotated domain within the REPO region (termed REPO-NAB). They report that the ZnF module binds single-stranded RNA with approximately 10-fold higher affinity than double-stranded DNA, that REPO-NAB binds both DNA and RNA with little sequence specificity, and that the N-terminal IDR of YY1 inhibits nucleic acid binding of both domains in cis and in trans. They propose that this autoinhibition may regulate YY1 function in vivo.
- **Visible evidence base** Fluorescence polarization binding assays (Kd values, Hill coefficients), competition experiments, circular dichroism spectra and melt curves, RoseTTAFold and AlphaFold3 structural predictions, bioinformatic analyses of published ChIP-seq, CLIP-seq, and ATAC-seq datasets, and mutagenesis experiments (ZnF pentamutant, REPO-NAB triple mutant).
- **Missing materials affecting confidence** All figures, tables, and supplementary data (including Supplemental Tables 1 and 2, Figures S1–S7) are referenced but not provided. This includes the full binding curves, raw anisotropy data, protein purification gels, CD spectra, and the complete list of oligonucleotide sequences. Without these, the quantitative claims cannot be independently verified.

## Reviewer
- **Overall assessment** This manuscript presents a systematic in vitro biochemical dissection of the nucleic acid binding properties of the transcription factor YY1. The authors report two notable findings: (1) the ZnF module binds ssRNA with higher affinity than dsDNA, and (2) a previously unannotated nucleic acid binding domain exists within the REPO region. They further report that the N-terminal IDR inhibits both domains. The work addresses a genuine controversy in the literature regarding the RNA binding interface of YY1 and provides quantitative data that could resolve it. However, the manuscript as provided has several significant weaknesses. The most critical is that the key quantitative data (figures, binding curves, raw values) are not available for assessment. Additionally, the claim that the N-terminus inhibits the ZnF domain in trans is not supported by the described competition experiments, which appear to show inhibition only at concentrations where the N-terminus itself begins to bind nucleic acids. The mechanistic model proposed in the Discussion, while interesting, extends well beyond the data presented. The writing is generally clear but the Results section would benefit from more explicit presentation of the quantitative comparisons that support the central claims.
- **Who would be interested in the results, and why** Researchers studying transcription factor biology, particularly those interested in the roles of intrinsically disordered regions in regulating DNA and RNA binding. The work is also relevant to the broader community investigating the functional significance of transcription factor RNA binding, and to those studying YY1 specifically given its involvement in transcriptional activation, repression, and genome architecture. The identification of a new nucleic acid binding domain in a well-studied protein may also interest structural biologists and protein biochemists.
- **Major strengths** The study addresses a specific, well-defined controversy in the literature and does so with quantitative equilibrium binding measurements, which are more rigorous than the semi-quantitative methods used in prior work. The systematic comparison of full-length protein with domain fragments is a sound approach. The use of native purification conditions, rather than denaturing and refolding, is a thoughtful methodological improvement. The identification of a separation-of-function mutant in the REPO-NAB is a useful tool for future in vivo studies. The authors are appropriately cautious in noting the limitations of their in vitro approach.
- **Major Concerns**
- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence availability
- **Claim pointer** The manuscript reports specific Kd values for full-length YY1, the ZnF module, and REPO-NAB against a panel of nucleic acid substrates, and states that the ZnF module binds ssRNA with approximately 10-fold higher affinity than dsDNA.
- **Evidence pointer** Figures 2, 3, 4, S2, S3, S4; location not provided for specific data points
- **Concern** The central quantitative claims of the manuscript rest on fluorescence polarization binding data presented in figures that are not provided. Without access to the binding curves, the reported Kd values, the Hill coefficients, and the statistical treatment of the data, it is impossible to assess whether the reported differences in affinity are robust and whether the conclusions drawn from them are justified. This is particularly important for the claim that the ZnF module binds ssRNA more tightly than dsDNA, which is a surprising result that contradicts some prior reports.
- **Why it matters** The entire manuscript hinges on the accuracy and interpretation of these quantitative measurements. If the figures are not available for review, the core claims cannot be verified. This is a fundamental issue that must be resolved before the manuscript can be considered for publication.
- **Resolution test** Provide all figures and supplementary data for review, including full binding curves with error bars, the number of independent replicates, and the statistical methods used to compare Kd values between conditions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental design and interpretation
- **Claim pointer** The authors claim that the N-terminus of YY1 inhibits nucleic acid binding of the ZnF module in trans, based on competition experiments where the N-terminus was added to the ZnF module in solution.
- **Evidence pointer** Figure 5A and 5B; location not provided for specific data points
- **Concern** The described competition experiments appear to have a critical flaw. The N-terminus itself shows no detectable nucleic acid binding in the concentration range used for the ZnF module binding assays (Figure 3B). However, at higher concentrations, the N-terminus does bind nucleic acids (Figure S7B). If the competition experiments were performed at N-terminus concentrations where it begins to bind the nucleic acid substrate directly, the observed "inhibition" could simply reflect the N-terminus sequestering the nucleic acid rather than a specific interaction with the ZnF module. The manuscript does not describe how this possibility was excluded.
- **Why it matters** The trans inhibition claim is a key part of the proposed autoinhibitory model. If the observed effect is due to substrate sequestration rather than a specific protein-protein interaction, the model would need to be substantially revised. This is a testable concern that the authors should address with appropriate control experiments.
- **Resolution test** Perform competition experiments at N-terminus concentrations where it does not itself bind the nucleic acid substrate, or include a control with a non-interacting protein of similar charge and size. Alternatively, demonstrate that the inhibition is competitive with respect to the ZnF module concentration and not the nucleic acid concentration.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic model
- **Claim pointer** The authors propose that the N-terminal IDR inhibits nucleic acid binding via charge complementarity, and that this autoinhibition may be relieved by protein-protein interactions or RNA binding, potentially regulating YY1's function in transcriptional activation, repression, and genome architecture.
- **Evidence pointer** Discussion section; Figures 5, S6, S7
- **Concern** The mechanistic model proposed in the Discussion is highly speculative and extends well beyond the data presented. The authors show that the N-terminus can inhibit nucleic acid binding, but they do not identify the molecular basis of this inhibition. The charge complementarity hypothesis is not directly tested, and the authors themselves note that mutating the 11 acidic residues (E43-D53) did not abolish the inhibitory effect. The proposal that protein-protein interactions or RNA binding could relieve autoinhibition is entirely hypothetical and not supported by any experimental evidence in this manuscript.
- **Why it matters** While speculative models can be valuable in a Discussion section, the model presented here is presented with a degree of confidence that is not warranted by the data. This could mislead readers into thinking that the proposed regulatory mechanism has been established, when in fact it remains a hypothesis. The authors should clearly distinguish between what their data demonstrate and what they speculate.
- **Resolution test** Revise the Discussion to clearly separate established findings from speculative hypotheses. If the authors wish to maintain the charge complementarity model, they should provide additional experimental evidence, such as testing a broader set of mutations or directly measuring the interaction between the N-terminus and the nucleic acid binding domains.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Data interpretation
- **Claim pointer** The authors state that the REPO-NAB domain binds DNA and RNA with "little apparent sequence specificity" and that the ZnF module shows "little sequence- or length-specificity" for RNA.
- **Evidence pointer** Figures 2, 3, 4, S3, S4; location not provided for specific data points
- **Concern** The manuscript describes testing a panel of nucleic acid substrates, but the full panel is not described in the text. The authors mention specific sequences (ARID1A RNA, polyuridine, Rpl30, AAVP5, SELEX consensus) but it is unclear how many sequences were tested, what range of sequences was covered, and whether the panel was designed to adequately sample sequence space. Without this information, the claim of "little sequence specificity" is difficult to evaluate.
- **Why it matters** The claim of low sequence specificity is important for the interpretation of the biological function of these domains. If the panel was limited, the conclusion may not be generalizable. A more thorough description of the panel and the rationale for its design would strengthen the manuscript.
- **Resolution test** Provide a complete description of the nucleic acid panel, including sequences, lengths, and structural features. If possible, include a more systematic analysis of sequence preferences, such as a SELEX or binding microarray experiment.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Structural characterization
- **Claim pointer** The authors use circular dichroism to show that the REPO-NAB maintains anti-parallel beta-sheet character in isolation, and they use RoseTTAFold and AlphaFold3 to generate structural models of YY1.
- **Evidence pointer** Figure 4D, S5; Methods section
- **Concern** The CD data are described only briefly, and the spectra are not provided. The claim that the REPO-NAB maintains beta-sheet character in isolation is based on a single technique and would be strengthened by additional structural characterization, such as NMR or SAXS. The structural models from RoseTTAFold and AlphaFold3 are mentioned but not shown or discussed in detail. It is unclear how these models inform the interpretation of the experimental data.
- **Why it matters** The structural characterization of the REPO-NAB is a key part of the manuscript's novelty. If the CD data are not available for review, the claim cannot be assessed. The structural models could provide valuable context for understanding how the REPO-NAB binds nucleic acids, but only if they are presented and discussed in sufficient detail.
- **Resolution test** Provide the CD spectra and the structural models. If the models are used to support specific claims, they should be shown and the relevant features discussed.

- **Concern ID** R1-M6
- **Severity** Major
- **Blocking** No
- **Axis** Bioinformatic analysis
- **Claim pointer** The authors state that genomic occupancy of YY1 cannot be explained by a combination of its cognate dsDNA binding motifs and possible RNA binding motifs derived from CLIP-seq.
- **Evidence pointer** Figure 1B; Methods section
- **Concern** The bioinformatic analysis is described only briefly. The authors do not provide details on the datasets used, the analysis pipeline, or the statistical methods employed. It is unclear how the conclusion was reached and whether it is robust to different analysis parameters or datasets.
- **Why it matters** This analysis motivates the entire study, so it is important that it is presented with sufficient detail to be evaluated. If the analysis is flawed or the conclusion is not robust, the rationale for the study is weakened.
- **Resolution test** Provide a detailed description of the bioinformatic analysis, including the datasets, the analysis pipeline, and the statistical methods. Consider including a supplementary figure showing the results of the analysis.

- **Minor Comments**
- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the N-terminus "regulates DNA and RNA binding affinity" but does not specify whether this regulation is positive or negative. The abstract would be clearer if it explicitly stated that the N-terminus inhibits binding.
- **Required correction** Revise the abstract to explicitly state that the N-terminus inhibits nucleic acid binding.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph 1
- **Issue** The term "transcription factor binding paradox" is used without definition. This term may not be familiar to all readers.
- **Required correction** Define the term or use a more descriptive phrase.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Results, section 1
- **Evidence pointer** Figure 2
- **Issue** The text states that the ZnF module binds ssRNA with "nearly 10-fold higher affinity" than dsDNA, but the specific Kd values are not given in the text. This makes it difficult for the reader to assess the magnitude of the effect.
- **Required correction** Include the specific Kd values in the text or in a table.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Nomenclature
- **Affected element** Results, section 2
- **Evidence pointer** Figure 4
- **Issue** The term "REPO-NAB" is introduced, but the rationale for this name is not explained. The authors should clarify what "NAB" stands for and why this name was chosen.
- **Required correction** Add a brief explanation of the nomenclature.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods
- **Evidence pointer** Methods section
- **Issue** The methods section does not describe the statistical analysis used to compare Kd values between different conditions. It is unclear whether the reported differences are statistically significant.
- **Required correction** Add a description of the statistical methods used.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion
- **Evidence pointer** Discussion, paragraph 2
- **Issue** The discussion of the overlap between DNA and RNA binding interfaces in the ZnF module is somewhat convoluted. The authors should more clearly state what is known and what is new from their work.
- **Required correction** Revise this paragraph for clarity.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion
- **Evidence pointer** Discussion, paragraph 3
- **Issue** The authors mention that the N-terminus may regulate YY1 function in vivo, but they do not discuss how their findings might be tested in a cellular context. A brief discussion of potential experimental approaches would strengthen the manuscript.
- **Required correction** Add a brief discussion of potential future experiments.

- **Technical failings that need to be addressed before the case is established** The most critical technical issue is the lack of available data (figures, tables, supplementary materials) to support the quantitative claims. The trans inhibition experiments (Figure 5) need to be carefully controlled to exclude substrate sequestration. The bioinformatic analysis (Figure 1B) needs to be described in sufficient detail to be evaluated. The CD data need to be provided to support the structural claims about REPO-NAB.
- **Assessment against Nature-style criteria** 
  - Originality: The identification of a second nucleic acid binding domain in YY1 and the observation that the N-terminus inhibits both domains is novel and would be of interest to the field. However, the concept of autoinhibition in transcription factors is not new, and the manuscript does not yet establish the mechanistic basis of this inhibition.
  - Scientific importance: The work addresses a specific controversy in the YY1 field and provides quantitative data that could resolve it. The identification of a new nucleic acid binding domain in a well-studied protein is potentially important. However, the in vitro nature of the study limits its immediate impact, and the authors do not yet demonstrate the functional relevance of their findings in a cellular context.
  - Interdisciplinary readership: The work is primarily of interest to biochemists and molecular biologists studying transcription factors. The methods used (fluorescence polarization, CD) are standard in the field. The broader significance to genome biology is discussed but not demonstrated.
  - Technical soundness: The experimental approach is generally sound, but the lack of available data prevents a full assessment. The trans inhibition experiments have a potential confound that needs to be addressed. The bioinformatic analysis is not described in sufficient detail.
  - Readability for nonspecialists: The manuscript is generally well-written and accessible to a broad scientific audience. The introduction provides sufficient background, and the results are presented in a logical order. However, some sections of the Discussion are speculative and could be more clearly distinguished from the established findings.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses a genuine controversy and presents a systematic approach that could resolve it. However, the lack of available data and the potential confound in the trans inhibition experiments prevent a full assessment of the claims. The authors should provide all data for review, address the trans inhibition concern with appropriate controls, and more clearly distinguish established findings from speculation in the Discussion.

## Risk / unsupported claims
- The claim that the ZnF module binds ssRNA with approximately 10-fold higher affinity than dsDNA is not verifiable without the binding data.
- The claim that the N-terminus inhibits the ZnF module in trans is not fully supported by the described experiments, as the possibility of substrate sequestration has not been excluded.
- The claim that the REPO-NAB maintains anti-parallel beta-sheet character in isolation is based on CD data that are not provided.
- The claim that the N-terminus inhibits nucleic acid binding via charge complementarity is speculative and not directly tested.
- The proposal that protein-protein interactions or RNA binding could relieve autoinhibition and regulate YY1 function in vivo is entirely hypothetical and not supported by data in this manuscript.
- The claim that genomic occupancy of YY1 cannot be explained by known DNA and RNA binding motifs is based on a bioinformatic analysis that is not described in sufficient detail to be evaluated.