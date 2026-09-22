## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and conclusions
- **Assessment boundary** Scientific validity, technical soundness, and support of claims based solely on the provided manuscript content
- **Shared manuscript claim summary** The authors propose that the USH1G protein SANS directly binds spliceosomal proteins PRPF31 and PRPF6 via two distinct conserved regions of its CENTn domain, that these interactions occur sequentially, that PRPF6 binding induces a conformational change from an intrinsically disordered region to an α-helix in SANS CENTn2, and that pathogenic USH1G/SANS variants perturb these interactions, implicating disrupted splicing in USH1G pathophysiology
- **Visible evidence base** FRET acceptor photobleaching assays in HEK293T cells, AlphaFold2-multimer structural predictions, Metapredict disorder predictions, CIDER sequence analysis, multiple sequence alignments, Western blot validation, and statistical analyses
- **Missing materials affecting confidence** Supplementary figures and tables (Figures S1-S9, Tables S1-S3) are referenced but not provided; raw numerical data for FRET efficiencies are not shown; statistical test details are only partially described; the GitHub repository for structural predictions is referenced but not accessible in this review

## Reviewer
- **Overall assessment** This manuscript addresses a relevant question in Usher syndrome pathophysiology by investigating the molecular interaction between SANS and two spliceosomal proteins. The combination of cellular FRET assays with in silico structural predictions is a reasonable approach. However, several technical concerns limit the strength of the conclusions. The AlphaFold2-multimer predictions for the full-length complexes show low confidence, which weakens the structural claims. The FRET data, while suggestive, lack sufficient methodological detail to fully assess robustness. The claim of sequential binding is inferred from competition experiments but is not directly tested. The finding that a truncated SANS variant lacking the proposed PRPF31 binding site still interacts with PRPF31 is internally inconsistent with the structural model and is not adequately resolved. The evolutionary conservation analysis is descriptive and does not directly support the functional claims. Overall, the manuscript presents interesting observations but the core conclusions are not fully established from the provided evidence.

- **Who would be interested in the results, and why** Researchers studying Usher syndrome genetics and pathophysiology would be interested, as the work attempts to link USH1G mutations to splicing defects. The spliceosome and pre-mRNA processing community would also find relevance given the proposed interaction between a Usher protein and core splicing factors. Additionally, those interested in protein-protein interaction prediction methods, particularly AlphaFold2 applications to disordered proteins, may find the approach of interest.

- **Major strengths** The study addresses a relatively unexplored aspect of USH1G function beyond the canonical stereocilia role. The use of orthogonal approaches (cellular FRET and in silico prediction) is commendable. The identification of distinct binding regions for PRPF31 and PRPF6 within the CENTn domain provides a testable model. The inclusion of pathogenic variants links the basic science to clinical relevance.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of structural predictions
- **Claim pointer** The authors claim that AlphaFold2-multimer predicts high-confidence complexes of SANS CENTn with PRPF31 NOP domain and PRPF6 C-terminal domains, and that these predictions support direct binding.
- **Evidence pointer** Section 2.2, Figures 4A-B, S2-S4
- **Concern** The authors report that full-length SANS-PRPF31 and SANS-PRPF6 complex predictions had low confidence (PAEmean ≥ 25.66 Å and ≥ 31.02 Å, respectively), yet they proceed to use truncated domain predictions to support their binding model. The PAEmean values for the high-confidence truncated predictions (≥ 11.83 Å and ≥ 10.21 Å) are still relatively high for atomic-level structural claims. More critically, the authors do not provide any experimental validation of the predicted interfaces, such as mutagenesis of predicted contact residues. The structural model is therefore largely speculative.
- **Why it matters** The central claim of distinct, non-overlapping binding sites for PRPF31 and PRPF6 in the CENTn domain rests on these predictions. Without experimental validation or higher-confidence models, the proposed binding architecture is not established.
- **Resolution test** Provide experimental validation of predicted interfaces (e.g., alanine scanning mutagenesis of predicted contact residues followed by binding assays), or present higher-confidence structural data (e.g., NMR, X-ray crystallography, or cross-linking mass spectrometry).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Internal consistency of binding data
- **Claim pointer** The authors claim that PRPF31 binds to SANS CENTn1 (aa 140-165), yet the truncated SANSV132Gfs*3 variant, which lacks this region, still shows interaction with PRPF31 in FRET assays.
- **Evidence pointer** Section 2.4, Figures 6D-E, S8
- **Concern** This is a direct contradiction between the structural model and the functional data. The authors acknowledge this discrepancy and propose an alternative binding site in the N-terminal ankyrin repeats, but they do not provide structural evidence for this alternative site. The AlphaFold2-multimer predictions for the SANS N-terminus with PRPF31 were not high confidence (Figure S8A-B). The manuscript does not adequately resolve this inconsistency.
- **Why it matters** If PRPF31 can bind to the N-terminal ankyrin repeats independently of CENTn1, then the proposed model of distinct binding regions is incomplete or incorrect. This affects the interpretation of how pathogenic variants disrupt binding and the proposed mechanism of splicing dysregulation.
- **Resolution test** Provide direct binding data (e.g., pull-down or ITC) with purified N-terminal SANS fragments and PRPF31, and/or high-confidence structural predictions of the SANS N-terminus with PRPF31.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Support for sequential binding claim
- **Claim pointer** The authors claim that SANS binds sequentially to PRPF31 and PRPF6 based on FRET competition experiments.
- **Evidence pointer** Section 2.1, Figures 3D-F
- **Concern** The FRET competition experiments show that PRPF31 reduces the SANS-PRPF6 FRET signal by approximately 16%, which the authors interpret as competition or conformational change. However, this modest reduction does not strongly support a sequential binding model. The experiments do not directly test the order of binding or whether binding is mutually exclusive. Alternative explanations, such as steric hindrance in a ternary complex or FRET artifacts due to acceptor-donor ratios, are not fully excluded.
- **Why it matters** The sequential binding model is a key conceptual advance of the paper, but the evidence is indirect and the effect size is small. Overinterpretation of this data could mislead the field.
- **Resolution test** Perform direct binding assays with purified proteins to determine binding stoichiometry and affinity, or use kinetic binding assays (e.g., surface plasmon resonance) to test for ordered binding.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Functional relevance of disrupted binding
- **Claim pointer** The authors claim that disrupted binding of SANS to PRPF31 and PRPF6 in pathogenic variants implies significance for USH1G pathophysiology.
- **Evidence pointer** Section 2.4, Figure 6
- **Concern** The manuscript does not demonstrate a functional consequence of the disrupted binding. No splicing assays, transcriptomic analyses, or cellular phenotypes are shown for the pathogenic variants. The link between altered protein-protein interaction and disease mechanism remains correlative.
- **Why it matters** The clinical relevance of the findings depends on demonstrating that disrupted SANS-PRPF interactions lead to splicing defects or cellular dysfunction. Without functional data, the pathophysiological significance is speculative.
- **Resolution test** Perform splicing assays (e.g., minigene reporters or RNA-seq) in cells expressing wild-type versus mutant SANS, or show that the variants fail to rescue splicing defects in SANS-deficient cells.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** FRET methodology
- **Evidence pointer** Section 4.5
- **Issue** The FRET efficiency calculation and normalization are described, but the number of biological replicates, the number of cells analyzed per condition, and the statistical test used are not specified in the main text. The figure legends are not available for review.
- **Required correction** Provide complete statistical details, including the number of independent experiments, the number of cells per condition, and the specific statistical tests used for each comparison.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Interpretation of co-localization
- **Affected element** Co-localization analysis
- **Evidence pointer** Section 2.1, Figure 2
- **Issue** The authors use Pearson correlation coefficients to support co-localization, but the values are not reported in the text. The co-localization of SANS with harmonin is described as predominantly cytoplasmic, which is inconsistent with the nuclear localization of the PRPFs, but this is not discussed in the context of the proposed nuclear function of SANS.
- **Required correction** Report the Pearson coefficient values and discuss the implications of the cytoplasmic SANS-harmonin co-localization for the proposed nuclear role of SANS.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Evolutionary conservation analysis
- **Affected element** Conservation claims
- **Evidence pointer** Section 2.3, Figure 5B
- **Issue** The authors state that SANS is highly conserved across mammals and vertebrates, including the IDRs, but the specific conservation scores or statistical measures are not provided. The claim that IDR conservation supports functional importance is not quantitatively supported.
- **Required correction** Provide conservation scores or statistical measures to support the claim of high conservation, and discuss the limitations of conservation analysis for IDRs.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Structural figures
- **Evidence pointer** Figures 4, S2-S4
- **Issue** The structural figures are described but not visible in the text. The authors should ensure that the predicted interfaces and key residues are clearly labeled and that the figures are interpretable without reference to the text.
- **Required correction** Ensure that all structural figures include clear labels for domains, residues, and predicted interactions, and that the color scheme is accessible to color-blind readers.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction and Discussion
- **Evidence pointer** Sections 1 and 3
- **Issue** The manuscript does not discuss the broader context of splicing factor mutations in retinal degeneration beyond PRPF31 and PRPF6. A brief mention of other spliceosomal proteins implicated in retinitis pigmentosa would strengthen the introduction.
- **Required correction** Add a brief discussion of other spliceosomal factors linked to retinal disease to contextualize the findings.

## Risk / unsupported claims
- The claim that SANS binds sequentially to PRPF31 and PRPF6 is not directly supported by the data; the competition experiments are indirect and the effect size is small.
- The claim that a conformational change from IDR to α-helix occurs upon PRPF6 binding is based solely on AlphaFold2 predictions and is not experimentally validated.
- The claim that pathogenic variants disrupt binding in a way that underlies USH1G pathophysiology is correlative; no functional splicing or cellular assays are provided.
- The proposed alternative binding site for PRPF31 in the SANS N-terminal ankyrin repeats is not supported by high-confidence structural predictions or direct binding data.
- The evolutionary conservation analysis is descriptive and does not quantitatively support the claim that conserved IDRs are functionally important for protein-protein interactions.