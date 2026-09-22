## Review setup
- **Input scope** Full manuscript text, including abstract, results, discussion, and materials and methods
- **Assessment boundary** Scientific claims, methodology, data interpretation, and internal consistency based solely on the provided manuscript text
- **Shared manuscript claim summary** The authors use two orthogonal approaches, HyperTRIBE and iCLIP, to define high-quality mRNA targets of the Arabidopsis m6A-binding protein ECT2. They conclude that ECT2 binds to m6A in the canonical DR(m6A)CH context, that U-rich motifs flanking m6A sites are important for ECT2 binding via its intrinsically disordered region, and that URUAY-type motifs may represent sites of competition with other RNA-binding proteins. The study refutes a prior claim that ECT2 binds to a plant-specific URU(m6A)Y motif.
- **Visible evidence base** Abstract, full results section, discussion, and materials and methods. Figures are referenced but not provided. Supplementary files are referenced but not provided.
- **Missing materials affecting confidence** Figures and figure supplements, supplementary files (including motif lists, target sets, and machine learning details), and the referenced companion paper (Rennie et al., 2021) describing the hyperTRIBER statistical method. Without these, quantitative assessments of data quality, effect sizes, and statistical robustness cannot be independently verified.

## Reviewer
- **Overall assessment** This manuscript addresses a significant and timely question in plant RNA biology: the sequence context and binding principles of the m6A reader ECT2. The combination of HyperTRIBE and iCLIP is methodologically strong and appropriate. The central claim that ECT2 binds to DR(m6A)CH, not URU(m6A)Y, is well argued and would resolve a controversy in the field. The evidence for IDR involvement in RNA binding is suggestive but relies on indirect observations. The machine learning analysis is a valuable addition but its details are not fully visible. Overall, the manuscript is potentially important, but several technical and interpretive concerns must be addressed before the case is fully established.
- **Who would be interested in the results, and why** Plant molecular biologists studying epitranscriptomics, RNA-binding proteins, and post-transcriptional gene regulation. Also, the broader m6A community working on YTH domain proteins in animals and yeast, as the findings bear on the universality of m6A recognition principles. Methodologists interested in HyperTRIBE and iCLIP applications in plants would also find value.
- **Major strengths** 1. Use of two orthogonal methods (HyperTRIBE and iCLIP) with convergent target sets strengthens confidence in the conclusions. 2. The study resolves a field controversy by providing evidence that ECT2 binds to the canonical DR(m6A)CH motif, aligning plant biology with the general eukaryotic framework. 3. The analysis of IDR-dependent crosslinks provides novel insight into multivalent RNA recognition by YTHDF proteins. 4. The machine learning approach to distinguish m6A and ECT2 binding sites is innovative and adds quantitative rigor.
- **Major Concerns** 1. The claim that ECT2 binds to DR(m6A)CH relies on motif enrichment analyses whose statistical details and effect sizes are not fully visible. 2. The evidence for IDR involvement in RNA binding is indirect and based on differential crosslinking patterns; direct biochemical validation is lacking. 3. The URUAY competition model is speculative and not directly tested. 4. The manuscript does not address the functional consequences of ECT2 binding to its targets, which limits the biological significance of the findings.
- **Minor Comments** 1. The term "URUAY-type motifs" is used but the precise definition and membership of this motif family are not clearly specified. 2. The relationship between the 110-kDa and 55-kDa band analyses and the conclusions drawn from each could be clarified. 3. The discussion of FA-CLIP limitations is useful but could be more balanced, acknowledging potential strengths of that method. 4. The manuscript would benefit from a schematic model figure summarizing the proposed binding mode.
- **Technical failings that need to be addressed before the case is established** 1. Statistical details of motif enrichment analyses (background models, multiple testing corrections) are not provided. 2. The hyperTRIBER method is described in a companion paper, but key parameters and validation metrics are not summarized here. 3. The machine learning model's feature importance and cross-validation performance are not fully reported. 4. The manuscript does not report the number of iCLIP peaks and HyperTRIBE sites that overlap with m6A sites at nucleotide resolution, which is central to the main claim.
- **Assessment against Nature-style criteria** Originality: High. The study provides a new, high-quality dataset and challenges a previous claim, offering a fresh perspective on plant m6A biology. Scientific importance: High. Resolving the ECT2 binding motif controversy has implications for understanding m6A function in plants and for comparative biology across eukaryotes. Interdisciplinary readership: Moderate. The topic is specialized, but the methodological advances and conceptual insights could attract readers from RNA biology, epitranscriptomics, and plant sciences. Technical soundness: Moderate. The experimental design is sound, but the lack of visible statistical details and validation metrics prevents full assessment. Readability for nonspecialists: Good. The manuscript is clearly written, with a logical flow and appropriate context for the general reader.
- **Recommendation posture** Supportive if technical concerns are resolved. The core claims are plausible and potentially important, but the current manuscript does not provide sufficient statistical and methodological detail to fully establish the case.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors claim that "RRACH and its variant DRACH are unequivocally the most highly enriched motifs at m6A sites in Arabidopsis" and that "ECT2 binds to m6A predominantly in the DR(m6A)CH sequence context in vivo."
- **Evidence pointer** Results section "DRACH/GGAH and U/Y-rich motifs are the most enriched around m6A/ECT2 sites"; Figure 5 and Figure 5—figure supplements; Supplementary file 3
- **Concern** The central claim of the paper rests on motif enrichment analyses, but the statistical framework is not fully described. The authors do not report how background models were constructed, whether multiple testing corrections were applied, or what the effect sizes and confidence intervals are for the enrichments. The statement "unequivocally" is strong and requires robust statistical support. Additionally, the overlap between iCLIP peaks and m6A sites at nucleotide resolution is not quantified, which is essential to support the claim that ECT2 binds at m6A sites.
- **Why it matters** Without rigorous statistical evidence, the main conclusion that ECT2 binds to DR(m6A)CH rather than URU(m6A)Y cannot be fully evaluated. The field controversy this paper aims to resolve requires definitive quantitative support.
- **Resolution test** Provide detailed statistical methods for motif enrichment, including background model construction, multiple testing corrections, and effect sizes. Report the number and proportion of iCLIP peaks that overlap with m6A sites at single-nucleotide resolution, with appropriate statistical tests comparing observed versus expected overlap.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence for IDR function
- **Claim pointer** The authors claim that "the IDR of ECT2 participates in RNA binding as it crosslinks to target mRNAs at U-rich elements highly abundant upstream of m6A sites."
- **Evidence pointer** Results section "The N-terminal IDR of ECT2 is involved in preferential crosslinking at U-rich sequences and in URURU-repulsion immediately upstream m6A sites"; Figure 7C and D; Figure 7—figure supplement 2
- **Concern** The evidence for IDR involvement in RNA binding is indirect. The authors infer IDR function from differences in crosslinking patterns between full-length ECT2 and a truncated version lacking the IDR. However, the truncation may affect protein stability, folding, or subcellular localization, which could confound the interpretation. Direct biochemical evidence, such as in vitro binding assays with purified IDR, is not provided.
- **Why it matters** The claim that the IDR contributes to RNA binding is a novel and important aspect of the paper. If this claim is not robustly supported, the model of multivalent recognition by ECT2 is weakened.
- **Resolution test** Provide direct biochemical evidence for IDR-RNA interaction, such as electrophoretic mobility shift assays or isothermal titration calorimetry with purified IDR and U-rich RNA. Alternatively, perform mutagenesis of key IDR residues and test effects on RNA binding in vivo.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Functional significance
- **Claim pointer** The authors state that "our study provides coherence between genetic and molecular studies of m6A-YTH function in plants" but do not directly address the functional consequences of ECT2 binding to its targets.
- **Evidence pointer** Discussion section; no specific figure or table
- **Concern** The manuscript focuses on defining binding sites and motifs but does not investigate the functional impact of ECT2 binding on target mRNA stability, translation, or downstream biological processes. The title mentions "principles of mRNA targeting," which is addressed, but the broader significance of these principles for plant development or stress responses is not explored.
- **Why it matters** For a Nature-style audience, the biological relevance of the molecular findings is important. Without functional data, the significance of the binding principles remains correlative.
- **Resolution test** Include experiments that perturb ECT2 binding (e.g., mutations in the m6A pocket or IDR) and measure effects on target mRNA expression, stability, or translation. Alternatively, connect ECT2 targets to known developmental phenotypes of ect2 mutants.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility and data availability
- **Claim pointer** The authors state that "all sequencing data have been deposited in the European Nucleotide Archive under accession code PRJEB44359" and that code is available on GitHub.
- **Evidence pointer** Data Availability section
- **Concern** While data deposition is commendable, the manuscript does not provide key intermediate data products, such as the list of iCLIP peaks, HyperTRIBE sites, and the results of the machine learning model. These are referenced as Supplementary files but are not visible in the provided material.
- **Why it matters** Independent verification and reanalysis of the data are essential for a high-impact claim. Without access to the peak lists and model outputs, reviewers and readers cannot fully assess the robustness of the conclusions.
- **Resolution test** Ensure that all relevant data files, including peak lists, target gene lists, and machine learning feature importance scores, are provided as supplementary files or in a public repository.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Definition of URUAY-type motifs
- **Evidence pointer** Results section "URUAY as sites of competitive interaction between ECT2 and other RNA-binding proteins"
- **Issue** The term "URUAY-type motifs" is used repeatedly, but the precise sequence definition and the criteria for inclusion in this motif family are not clearly specified.
- **Required correction** Provide a clear definition of URUAY-type motifs, including the exact consensus sequence and any variations, and specify how these motifs were identified and distinguished from other U-rich motifs.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Comparison of 110-kDa and 55-kDa band analyses
- **Evidence pointer** Results section "The N-terminal IDR of ECT2 is involved in preferential crosslinking at U-rich sequences and in URURU-repulsion immediately upstream m6A sites"; Figure 7C and D
- **Issue** The distinction between the 110-kDa and 55-kDa band analyses is not always clear. The authors should clarify which conclusions are drawn from each band and how the two analyses complement each other.
- **Required correction** Add a clear statement in the results or figure legends specifying which band each analysis refers to and what the key differences in conclusions are.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion of FA-CLIP limitations
- **Evidence pointer** Discussion section
- **Issue** The authors criticize FA-CLIP for generating false positives and missing genuine targets, but the discussion is one-sided. A more balanced treatment acknowledging potential strengths of FA-CLIP would strengthen the argument.
- **Required correction** Add a sentence acknowledging that FA-CLIP can capture protein-protein crosslinks and may be useful for studying indirect interactions, while noting its limitations for direct binding site identification.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure accessibility
- **Evidence pointer** All figures
- **Issue** The manuscript references many figures and supplements, but these are not provided in the submitted material. This makes it difficult to follow the results.
- **Required correction** Ensure that all figures and figure supplements are included in the submission, with clear legends that allow the reader to understand the data without referring to the main text.

## Risk / unsupported claims
- The claim that ECT2 binds to DR(m6A)CH "unequivocally" is not fully supported by the visible evidence, as statistical details are missing.
- The claim that the IDR of ECT2 participates in RNA binding is based on indirect evidence and requires direct biochemical validation.
- The model of URUAY as a site of competition between ECT2 and other RNA-binding proteins is speculative and not directly tested.
- The statement that "plants do not constitute an exception to the general biochemical framework" is a strong conclusion that depends on the robustness of the motif analysis, which is not fully verifiable from the provided material.
- The functional significance of ECT2 binding to its targets is not addressed, so any claims about biological relevance beyond binding are unsupported.