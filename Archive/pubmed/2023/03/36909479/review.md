## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) and metadata
- **Assessment boundary** Scientific claims, methodological soundness, evidence quality, and accessibility of the FREEDA pipeline as presented in the preprint
- **Shared manuscript claim summary** The authors present FREEDA, an automated computational pipeline that detects positive selection in protein-coding genes from user-provided gene names, maps results onto AlphaFold-predicted structures, and is designed for non-specialist cell biologists. They validate the pipeline on a dataset of primate genes with known evolutionary histories, apply it to >100 mouse centromere proteins, and experimentally test a prediction of functional innovation in CENP-O centromere binding.
- **Visible evidence base** Full text including methods, supplementary figure/table references, and descriptions of validation datasets and experimental results
- **Missing materials affecting confidence** Supplementary figures and tables (S1–S9), supplementary tables 1–4, raw data files, and the FREEDA software itself were not provided for direct inspection. Experimental images and quantitative data for the CENP-O localization experiments are described but not shown in the provided text.

## Reviewer

### Overall assessment
This manuscript presents a timely and potentially valuable tool for the cell biology community. The authors address a real gap: making positive selection detection accessible to experimental biologists without computational expertise. The validation strategy is thoughtful, and the application to centromere proteins yields biologically interesting hypotheses. However, the evidence provided in this preprint is insufficient to fully establish the reliability and generalizability of the pipeline. Key validation details, software availability, and experimental data are referenced but not shown. The central claim that FREEDA can guide experimental testing of protein innovation is supported in principle but not yet rigorously demonstrated from the provided material.

### Who would be interested in the results, and why
Cell biologists studying protein function, particularly those working on centromeres, kinetochores, and chromosome segregation, would be the primary audience. Evolutionary biologists interested in positive selection in mammalian proteins may also find the pipeline useful. The tool's accessibility could broaden the adoption of evolutionary analyses in cell biology, which is a community the authors explicitly target.

### Major strengths
1. The manuscript addresses a clear and important need: making positive selection detection accessible to non-specialists.
2. The pipeline is fully automated, requiring only a gene name, which is a significant usability improvement over existing tools.
3. The validation using genes with known evolutionary histories is a sound approach.
4. The application to centromere proteins is biologically relevant and generates testable hypotheses.
5. The experimental follow-up on CENP-O provides a proof-of-principle that computational predictions can be tested in the lab.
6. The authors acknowledge limitations and provide guidance for users.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that FREEDA reliably detects positive selection and correctly identifies orthologous sequences, validated on a dataset of 23 primate genes.
- **Evidence pointer** Results section "FREEDA validation using genes with previously defined evolutionary histories"; Supplementary Table 1
- **Concern** The validation results are summarized in text but the actual data (Supplementary Table 1) is not provided. The authors report that FREEDA found positive selection in 10 of 19 genes with known signatures, but the criteria for "consistent with the literature" are not fully specified. For example, the weak signal in BST2 (p=0.0864) is described as possibly due to lineage-specific selection, but this interpretation is not tested. The detection of positive selection in TREX1, which was previously reported as not adaptively evolving, is attributed to alignment algorithm differences, but this claim is not substantiated with comparative analyses.
- **Why it matters** The reliability of the pipeline is the central claim of the manuscript. Without access to the full validation data and a clear explanation of discrepancies with previous studies, the reader cannot assess whether FREEDA's automated approach produces results comparable to manual expert analyses.
- **Resolution test** Provide Supplementary Table 1 with full results for all 23 genes, including the specific codons identified, p-values, and a comparison with published results. For TREX1, perform a direct comparison of alignment methods to demonstrate that the discrepancy is due to algorithmic differences.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that FREEDA can resolve ancient and recent gene duplications, demonstrated using HERC5/HERC6, H4C1/H4C2, and KIF4A/KIF4B.
- **Evidence pointer** Results section "FREEDA validation using genes with previously defined evolutionary histories"; "Additional Supplementary Materials"
- **Concern** The duplication resolution tests are described in text but the actual data is not shown. The authors state that FREEDA "successfully distinguished" these paralogous genes, but the specific criteria for success are not defined. For H4C1/H4C2, the authors note that one orthologue lost its start codon and likely pseudogenized, but it is unclear how this was determined and whether this affected the positive selection analysis.
- **Why it matters** Gene duplication is a common source of false positive signals in positive selection detection. If FREEDA cannot reliably distinguish orthologues from paralogues, its results on novel genes would be unreliable. The manuscript's claim that FREEDA is dependable for non-specialist users depends on this validation.
- **Resolution test** Provide the alignment and phylogenetic tree data for HERC5/HERC6, H4C1/H4C2, and KIF4A/KIF4B, showing how FREEDA distinguished orthologues from paralogues. Define the success criteria explicitly.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors claim that applying FREEDA to >100 mouse centromere proteins reveals positive selection in intrinsically disordered regions of ancient domains, suggesting innovation of essential functions.
- **Evidence pointer** Results section "Using FREEDA to derive evolution-guided hypotheses"; Figure 4; Supplementary Figure S3–S5
- **Concern** The analysis of centromere proteins is presented as a key result, but the full list of 104 genes and the specific results for each are not provided. The authors highlight three examples (MIS18β, AURKC, CENP-O) but do not provide a systematic analysis of how many genes show positive selection, how many of those have signals in disordered regions, or how this compares to a null expectation. The claim that positive selection acts on intrinsically disordered regions is based on a small number of examples.
- **Why it matters** The biological conclusions about centromere protein evolution depend on the full dataset analysis. Without a systematic presentation, the reader cannot evaluate whether the highlighted examples are representative or cherry-picked.
- **Resolution test** Provide a supplementary table with results for all 104 genes, including the number of codons under positive selection, their location in structured vs. disordered regions, and a statistical comparison to a genome-wide or appropriate null distribution.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors claim that the experimental CENP-O experiments demonstrate that positive selection in the C-terminal RWD domain regulates centromere binding.
- **Evidence pointer** Results section "Experimental testing of functional protein innovation"; Figure 6; Supplementary Figures S7–S9
- **Concern** The experimental results are described in text but the actual data (Figure 6, S7–S9) is not shown. The authors report that rat CENP-O fails to localize to mouse centromeres and that the C-terminal RWD domain is responsible, but the quantification, statistical analysis, and controls are not described in sufficient detail. The statement that "only the mouse C-terminal RWD domain could rescue, albeit not fully, the localization" suggests a partial effect that is not clearly interpreted.
- **Why it matters** This is the key proof-of-principle experiment that connects the computational predictions to functional biology. Without seeing the data, the reader cannot assess the strength of the evidence or whether alternative interpretations are possible.
- **Resolution test** Provide the experimental images and quantification for all constructs tested, including statistical analysis and appropriate controls. Clarify what "albeit not fully" means quantitatively.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that FREEDA is fully automated and requires only a gene name, making it accessible to non-specialists.
- **Evidence pointer** Results section "Overview of the FREEDA pipeline"; Methods section "Input extraction and identification of potential orthologous exons"
- **Concern** The manuscript describes the pipeline's features but does not provide a detailed assessment of its runtime, failure rate, or the proportion of genes for which the pipeline produces reliable results. The authors note that "at least 100 GB of storage space is needed" and that the first run triggers large downloads, but the computational requirements and potential failure modes are not systematically characterized. The claim that the pipeline is "fully automated" is qualified by the need for manual verification of alignments.
- **Why it matters** For a tool aimed at non-specialists, reliability and ease of use are critical. If the pipeline frequently fails or requires substantial manual intervention, its accessibility claim is weakened.
- **Resolution test** Provide a systematic evaluation of the pipeline's performance across a larger set of genes, including success rate, runtime, and common failure modes. Clarify the level of user expertise required for manual verification steps.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that FREEDA "maps results onto protein structures predicted by AlphaFold" but does not mention that this feature is only available when the AlphaFold model matches the Ensembl sequence. This limitation is described in the Methods but should be noted in the abstract for accuracy.
- **Required correction** Add a brief qualification in the abstract, such as "when a matching structure is available."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Methods section "Input extraction and identification of potential orthologous exons"
- **Issue** The Methods state that FREEDA uses a "modified MAFFT protocol" but do not specify the exact modifications. This makes it difficult for others to reproduce the alignment procedure.
- **Required correction** Provide a detailed description of the modified MAFFT protocol or a reference to a published description.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results
- **Evidence pointer** Results section "Using FREEDA to derive evolution-guided hypotheses"
- **Issue** The authors state that positive selection in intrinsically disordered regions of ancient domains suggests "innovation of essential functions." This interpretation assumes that positive selection in disordered regions necessarily implies functional innovation, but it could also reflect relaxed constraint or other evolutionary processes.
- **Required correction** Acknowledge alternative interpretations and discuss how the experimental data help distinguish between them.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The Discussion mentions limitations of FREEDA but does not discuss the potential for false positives due to alignment errors or the choice of species set. These are known issues in positive selection detection and should be addressed.
- **Required correction** Add a paragraph discussing known limitations of dN/dS-based methods and how FREEDA addresses or does not address them.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Software availability
- **Evidence pointer** Methods section "Input extraction and identification of potential orthologous exons"
- **Issue** The software is available on GitHub, but the manuscript does not specify the license, version, or DOI for citation. This makes it difficult for users to cite and for the software to be properly credited.
- **Required correction** Provide a license, version number, and a DOI or other persistent identifier for the software.

### Technical failings that need to be addressed before the case is established
1. Validation data (Supplementary Table 1) not provided, preventing assessment of pipeline accuracy.
2. Duplication resolution data not shown, despite being a key validation claim.
3. Full results for the 104-gene centromere analysis not provided.
4. Experimental data for CENP-O localization experiments not shown.
5. The modified MAFFT protocol is not described in sufficient detail for reproducibility.

### Assessment against Nature-style criteria
- **Originality** The concept of an automated, user-friendly pipeline for positive selection detection is not entirely new, but the specific combination of features (fully automated orthologue finding from non-annotated genomes, AlphaFold structure mapping, GUI) is a novel contribution. The application to centromere proteins and the experimental follow-up add originality.
- **Scientific importance** The tool addresses a real barrier to the adoption of evolutionary analyses in cell biology. If validated, it could have broad impact on how cell biologists study protein function. The biological findings on centromere protein evolution are of interest to the chromosome biology community.
- **Interdisciplinary readership** The manuscript bridges evolutionary biology and cell biology, which is a strength. The tool is designed for non-specialists, which could broaden its readership. However, the current presentation assumes familiarity with both fields, which may limit accessibility.
- **Technical soundness** The pipeline design is reasonable, and the validation approach is appropriate. However, the lack of access to key data prevents a full assessment of technical soundness. The experimental data, while described, cannot be evaluated without the figures.
- **Readability for nonspecialists** The manuscript is generally well-written and the motivation is clear. However, some sections assume familiarity with evolutionary methods (e.g., dN/dS, site models) that may be unfamiliar to cell biologists. A brief primer or glossary would improve accessibility.

### Recommendation posture
Supportive if technical concerns are resolved. The manuscript presents a potentially valuable tool and biologically interesting findings, but the evidence provided is insufficient to fully establish the reliability of the pipeline and the strength of the experimental conclusions. Access to the validation data, full results, and experimental figures is essential for a complete assessment.

## Risk / unsupported claims
1. The claim that FREEDA "reliably" detects positive selection is not fully supported without access to the complete validation data.
2. The claim that positive selection acts on intrinsically disordered regions of ancient domains is based on a small number of highlighted examples and is not systematically demonstrated.
3. The claim that the C-terminal RWD domain of CENP-O is responsible for species-specific centromere binding is not fully supported without seeing the experimental data.
4. The claim that FREEDA is "fully automated" is qualified by the need for manual verification and is not systematically characterized.
5. The interpretation that positive selection in disordered regions implies "innovation of essential functions" is an inference that is not directly tested.