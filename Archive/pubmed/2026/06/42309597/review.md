## Review setup
- **Input scope** Full manuscript text (abstract, methodology, results, discussion, conclusions, supplementary figure legends) as provided.
- **Assessment boundary** Scientific content, methodological rigor, validity of claims relative to the evidence presented, and alignment with Nature-style criteria. Editorial and formatting issues are noted only where they affect scientific clarity.
- **Shared manuscript claim summary** The authors integrate AlphaFold3 structural prediction with multi-algorithm immunoinformatic profiling to characterize the structure, disorder, and immunogenic potential of eight Bombyx mori silk proteins (FibL, FibH, P25, Ser-1 to Ser-5). They report that FibL and P25 adopt well-defined structures, FibH and sericins are predominantly disordered, and that P25 is uniquely hypoimmunogenic while FibL, FibH, Ser-4, and Ser-1 are the primary immunogenic drivers. They propose a disorder-to-order templating mechanism for fiber assembly and suggest strategies for engineering hypoimmunogenic silk biomaterials.
- **Visible evidence base** Main text, Tables 1, 5, 6; Figures 1-16; Supplementary Figures 1-8; Supplementary Tables 1-3 (tables referenced but not fully visible in the provided material).
- **Missing materials affecting confidence** Supplementary Tables 1-3 (peptide lists) are referenced but not provided. Supplementary Methods 1 (BLAST strategies) is referenced but not provided. No experimental validation data are included. Sequence accession numbers and exact database retrieval dates are not specified. The full list of predicted peptides and their sequences is not available for independent verification.

## Reviewer
- **Overall assessment** This manuscript presents a purely computational analysis of silk protein structure and immunogenicity. The work is methodologically straightforward, combining established bioinformatics tools in a sequential pipeline. The main scientific value lies in the comparative immunogenic profiling across the eight silk proteins and the identification of P25 as a potentially hypoimmunogenic component. However, the study is entirely predictive, with no experimental validation, and several claims extend beyond what the computational evidence can support. The interpretation of low-confidence AlphaFold3 predictions as evidence of biological disorder, and the proposal of a "fuzzy complex" mechanism, are speculative. The manuscript would benefit from a more cautious framing of conclusions and a clearer acknowledgment of the limitations of in silico predictions for guiding biomaterial design.
- **Who would be interested in the results, and why** Researchers in biomaterials science, particularly those working on silk-based medical devices, would be interested in the comparative immunogenic profiling. The identification of P25 as potentially hypoimmunogenic and the ranking of immunogenic risk across proteins could inform material selection. Computational biologists developing or applying immunoinformatics pipelines may also find the multi-algorithm approach of interest. However, the lack of experimental validation limits the direct utility for clinical translation.
- **Major strengths**
  - Comprehensive coverage of all major silk protein components, including both fibroin subunits and all five sericin isoforms.
  - Integration of state-of-the-art structural prediction (AlphaFold3) with multiple immunoinformatic tools, providing a multi-layered analysis.
  - Clear presentation of confidence metrics (pLDDT, pTM, ipTM) and appropriate caution in interpreting low-confidence regions.
  - The identification of P25 as a uniquely hypoimmunogenic component is a potentially useful finding for biomaterial design.
  - The discussion of limitations, including AlphaFold3's constraints and the need for experimental validation, is thoughtful.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Validity of claims
- **Claim pointer** The authors claim that "P25 emerged as uniquely hypoimmunogenic" and that "FibL and FibH showed the highest potential for inducing CD8+ and CD4+ cell responses among the fibroin subunits, respectively."
- **Evidence pointer** Results section, Tables 2-4, Figures 9-12; Supplementary Tables 1-2 (not provided)
- **Concern** The central immunogenic ranking is based entirely on in silico predictions from a single epitope prediction pipeline (NetMHCpan-4.1, NetMHCIIpan-4.0). No experimental validation, such as peptide-MHC binding assays, T-cell activation studies, or in vivo models, is provided. The predictive accuracy of these tools, while improved, is not absolute, and the biological relevance of predicted epitopes depends on many factors not captured here, including antigen processing, presentation kinetics, T-cell receptor repertoire, and immunological tolerance. The claim that P25 is "uniquely hypoimmunogenic" is a strong statement that cannot be supported by computational prediction alone.
- **Why it matters** The central conclusion of the manuscript, and its potential utility for biomaterial design, rests on the reliability of these immunogenic rankings. If the predictions are inaccurate, the proposed design strategies (e.g., P25 enrichment, HLA-matched selection) would be based on faulty premises. Overstating the confidence in purely computational predictions could mislead readers and future research directions.
- **Resolution test** The authors should either (a) provide experimental validation of at least the key predicted epitopes and the hypoimmunogenic nature of P25, or (b) substantially temper their claims, explicitly stating that these are hypotheses requiring experimental confirmation, and avoid definitive language such as "uniquely hypoimmunogenic."

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Validity of claims
- **Claim pointer** The authors propose a "disorder-to-order templating mechanism" for fiber assembly, stating that "the interaction of this metalloprotein complex with intrinsically disordered sericins induced dramatic conformational ordering" and that the low confidence scores reflect "genuine conformational heterogeneity in the bound state, a hallmark of 'fuzzy complexes'."
- **Evidence pointer** Results section, Figures 6-8; Discussion section
- **Concern** This is a significant mechanistic claim derived entirely from AlphaFold3 predictions. The observation that predicted structures of sericins become more ordered when modeled in complex with the FibL-P25-Cu2+ unit is an artifact of the modeling process, not direct evidence of a biological mechanism. AlphaFold3 generates a single static prediction per input; comparing predictions of monomers versus complexes does not demonstrate conformational dynamics or induced folding. The interpretation of low pLTM/pTM scores as evidence of "fuzzy complexes" is speculative. There is no experimental data (e.g., circular dichroism, NMR, SAXS, HDX-MS) to support the proposed conformational transitions.
- **Why it matters** This mechanistic proposal is a major part of the manuscript's conceptual contribution. If it is presented as a finding rather than a hypothesis, it overstates what computational modeling can establish. The distinction between algorithmic uncertainty and biological disorder is critical and the authors themselves acknowledge this elsewhere, but the strength of the claim in the discussion is not consistent with that caution.
- **Resolution test** The authors should reframe this section as a hypothesis-generating observation, clearly stating that the proposed mechanism is speculative and requires experimental testing. They should avoid definitive statements about conformational dynamics and "fuzzy complexes" that are not supported by the evidence.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "BLAST analysis successfully identified distant homologs for each silk protein" and report specific numbers of homologs (e.g., 101 for FibL, 12 for FibH, 168 for P25).
- **Evidence pointer** Results section, "Sequence characterization" subsection; Supplementary Figure 1; Supplementary Methods 1 (not provided)
- **Concern** The methodology for identifying distant homologs is not fully described. The specific BLAST strategies, databases used, and filtering criteria are mentioned, but the details of the searches (e.g., which database versions, how redundancy was handled, how the 20% identity and 70% coverage thresholds were applied) are not fully transparent. The number of homologs varies widely between proteins (e.g., 168 for P25 vs. 3 for Ser-3), and the reasons for this variation are not discussed. Without the full methods, the reproducibility of this step is questionable.
- **Why it matters** The homolog analysis is used to support the generalizability of the structural and immunogenic findings. If the homolog identification is not reproducible or is biased, the comparative conclusions may be affected. The wide variation in homolog numbers also raises questions about the completeness of the searches.
- **Resolution test** The authors should provide the full details of the BLAST strategies in the main text or supplementary materials, including database versions, search parameters, and a discussion of the variation in homolog numbers across proteins.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "Refinement with ModRefiner and FG-MD did not yield consistent improvements over the original AlphaFold3 models, as no systematic enhancement was observed across the evaluated quality indicators."
- **Evidence pointer** Results section, "Structural characterization" subsection
- **Concern** The specific quality indicators used to compare pre- and post-refinement models are not named or described. The statement is vague and does not allow the reader to assess the validity of the conclusion. It is unclear whether the comparison was based on pLDDT, pTM, RMSD, or other metrics.
- **Why it matters** The decision to report unrefined AlphaFold3 models is a methodological choice that should be justified with specific data. Without knowing which quality indicators were used, the reader cannot evaluate whether the refinement was adequately tested.
- **Resolution test** The authors should specify the quality indicators used for comparison and provide the relevant data (e.g., a supplementary table or figure showing pre- and post-refinement scores).

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The authors state that "All analyses were performed in Python (v3.12.9)" and list specific library versions for some tools.
- **Evidence pointer** Methodology section, "Data analysis" subsection
- **Concern** While some software versions are provided, the exact versions of key tools (e.g., AlphaFold3, NetMHCpan-4.1, NetMHCIIpan-4.0, VaxiJen 2.0, BepiPred-3.0, AllerTOP v.2, ToxinPred v3.0) are not specified. The specific parameters used for each tool (e.g., HLA allele sets, peptide length, thresholds) are not fully described. This limits the reproducibility of the study.
- **Why it matters** Reproducibility is a core requirement for computational studies. Without precise tool versions and parameters, other researchers cannot replicate the analysis or verify the results.
- **Resolution test** The authors should provide a complete list of all software tools with versions and all relevant parameters, either in the main text or as a supplementary table.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states "P25 emerged as uniquely hypoimmunogenic" without mentioning that this is a computational prediction. The abstract also does not mention the lack of experimental validation.
- **Required correction** Add a phrase such as "in silico" or "computationally predicted" to the abstract, and consider adding a sentence noting that experimental validation is required.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 9 legend
- **Evidence pointer** Figure 9 legend
- **Issue** The legend states "HLA alleles were arranged alphabetically in ascending order" but the figure itself is not shown in the provided material. The legend also does not specify the number of peptides analyzed or the threshold for "strong" vs "weak" binding.
- **Required correction** Clarify the figure legend to include the number of peptides and the specific thresholds used for classification.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Table 4
- **Evidence pointer** Table 4
- **Issue** The table title is "Distribution of high-priority predicted MHC-II peptides for proteolytic cleavage across silk proteins and HLA alleles." The criteria for "high-priority" are not defined in the table or its legend.
- **Required correction** Define "high-priority" in the table legend, including the specific score thresholds used.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The discussion is lengthy and contains some repetition, particularly in the sections describing the immunogenic hierarchy and the proposed design strategies. The mechanistic discussion of "fuzzy complexes" is speculative and could be more clearly labeled as a hypothesis.
- **Required correction** Condense the discussion and clearly separate established findings from speculative interpretations.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** References
- **Evidence pointer** Reference list
- **Issue** The reference list is not provided in the submitted material, so it is not possible to assess the completeness and appropriateness of the citations.
- **Required correction** Ensure all claims are supported by appropriate references and that the reference list is complete and formatted correctly.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 5
- **Evidence pointer** Figure 5
- **Issue** The figure shows truncated FibH models with and without copper ions and FibL. The legend mentions "FibH N-terminally truncated, with copper ions and FibL (C)" and "FibH C-terminally truncated, with copper ions and FibL (D)". It is unclear why the N- and C-terminally truncated models were generated and whether the truncation affects the interpretation.
- **Required correction** Clarify the rationale for generating two truncation variants and discuss the potential impact of truncation on the predicted structures.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methodology section
- **Evidence pointer** Methodology section, "Structural characterization" subsection
- **Issue** The authors state that "we selected copper as the metal ion for the structural modeling" and justify this choice based on literature. However, the specific AlphaFold3 settings for incorporating metal ions (e.g., how the ions were specified in the input) are not described.
- **Required correction** Provide details on how metal ions were included in the AlphaFold3 input and whether any special parameters were used.

## Risk / unsupported claims
- The claim that P25 is "uniquely hypoimmunogenic" is unsupported by experimental evidence and is based solely on computational prediction.
- The proposed "disorder-to-order templating mechanism" and the interpretation of low-confidence AlphaFold3 predictions as evidence of "fuzzy complexes" are speculative and not supported by direct experimental data.
- The immunogenic risk hierarchy (e.g., Ser-4 as the highest-risk component) is presented with a degree of certainty that is not justified by the purely computational approach.
- The claim that "these findings challenge the paradigm that sericins exclusively drive silk immunogenicity" is an overstatement, as the findings are predictive and do not directly test this paradigm.
- The statement that "P25's compact beta-sheet architecture... likely resists endosomal proteolysis" is presented as an explanation but is itself a hypothesis without experimental support.
- The generalizability of the findings to clinical biomaterial design is asserted without acknowledging the substantial gap between computational predictions and in vivo immune responses.