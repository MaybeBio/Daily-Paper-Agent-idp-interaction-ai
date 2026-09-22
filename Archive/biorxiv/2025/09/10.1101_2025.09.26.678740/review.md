## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods, end matter) as provided
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text; no assessment of supplementary figures or tables beyond what is referenced
- **Shared manuscript claim summary** The authors investigate the molecular interaction between the meiotic DSB protein Mer2 and the H3K4me3 reader Spp1 in S. cerevisiae. Using AlphaFold modeling, biochemical reconstitution, biophysical assays (AFM, SEC-MALS, SAXS), and in vivo genetics, they propose a structural model of the Mer2-Spp1 complex with 4×2 stoichiometry, describe an allosteric mechanism governing Spp1 binding to Mer2 tetramers, and identify a positively charged motif (R5K) in Spp1 that contributes to DNA binding within Mer2-Spp1-DNA complexes. They further show that this motif is dispensable for meiotic DSB formation in vivo.
- **Visible evidence base** Results sections describing AFM force spectroscopy, pulldown assays, SEC-MALS, SAXS, AlphaFold modeling, gel shift assays, condensation assays, and Southern blot analysis; figures referenced as Figures 1-8 and Supplementary Figures 1-12; Supplementary Tables 1-5
- **Missing materials affecting confidence** Actual figure panels and data plots; supplementary figures and tables; experimental replicates and statistical details; AlphaFold confidence metrics; SAXS data quality metrics; strain validation data; raw AFM force curves

## Reviewer
- **Overall assessment** This manuscript addresses a significant question in meiotic recombination: how the H3K4me3 reader Spp1 is recruited to the meiotic DSB machinery through interaction with Mer2. The work combines multiple biophysical and biochemical approaches to characterize the Mer2-Spp1 interaction, proposes a structural model, and tests functional implications in vitro and in vivo. The study is technically ambitious and the combination of AlphaFold with experimental validation is timely. However, several concerns limit the strength of the conclusions as presented. The allosteric model for 4×2 stoichiometry is inferred rather than directly demonstrated, the discrepancy between AFM-derived and ensemble-derived affinities is not fully resolved, and the in vivo relevance of the identified DNA-binding motif is explicitly shown to be negligible, weakening the functional significance of a central finding. The manuscript would benefit from additional direct evidence for the proposed allosteric mechanism and a clearer articulation of what the in vivo negative result implies for the model.
- **Who would be interested in the results, and why** Researchers in the fields of meiosis, DNA double-strand break formation, chromatin biology, and biomolecular condensation. The work provides molecular-level insight into how a chromatin mark reader is recruited to the DSB machinery, which is relevant to understanding the loop-axis organization of meiotic chromosomes. The biophysical characterization of a protein-protein interaction involved in meiotic recombination will also interest structural biologists and biophysicists studying protein-DNA and protein-protein interactions. The use of AlphaFold combined with experimental validation is of general methodological interest.
- **Major strengths** 1) The combination of AlphaFold modeling with multiple experimental approaches (AFM, SEC-MALS, SAXS, mutagenesis, pulldowns) provides a multi-pronged strategy for characterizing the Mer2-Spp1 interaction. 2) The identification and validation of specific interface residues through mutagenesis strengthens the structural model. 3) The single-molecule AFM approach provides kinetic parameters not easily obtained from ensemble methods. 4) The inclusion of in vivo experiments to test the functional relevance of in vitro findings is commendable, even when results are negative. 5) The manuscript is generally clearly written and the logic of the experimental approach is easy to follow.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** The allosteric model for 4×2 stoichiometry is not directly tested; the discrepancy between AFM and MST affinities is not mechanistically resolved; the in vivo data show the R5K motif is dispensable, which undermines the functional significance of the DNA-binding finding; the contribution of the Mer2 C-terminal IDR to Spp1 binding is not quantified.
- **Assessment against Nature-style criteria** **Originality:** Moderate to high. The specific molecular details of the Mer2-Spp1 interaction and the proposed allosteric mechanism are novel, though the general framework of Spp1-Mer2 interaction was previously established. **Scientific importance:** Moderate. The work advances understanding of meiotic DSB formation, but the in vivo negative result for the R5K motif limits the broader significance. **Interdisciplinary readership:** Moderate. The topic is of interest to meiosis and chromatin biologists, but the biophysical detail may limit broader appeal. **Technical soundness:** Generally sound in execution, but the inference of allostery from limited data and the unresolved affinity discrepancy are weaknesses. **Readability for nonspecialists:** The manuscript is accessible to a specialized audience but would require significant simplification for a general readership. The abstract is clear, but the results sections assume substantial background knowledge.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly the direct testing of the allosteric model and a clearer interpretation of the in vivo negative result.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The authors claim that "binding of one Spp1 subunit appears to allosterically modulate the affinity for the adjacent sites, leading to the assembly of 4×2 Mer2-Spp1 complexes" and propose this as the mechanism explaining the observed stoichiometry.
- **Evidence pointer** Results section "The stoichiometry of Mer2-Spp1 complexes"; Figure 4; Discussion section "Assembly of the Mer2-Spp1 complex"
- **Concern** The allosteric model is presented as a central finding, but the evidence provided is indirect. The authors infer allostery from the discrepancy between single-molecule AFM affinity (K_D = 1.9 ± 1.6 µM) and ensemble MST affinity, and from the observation that only 4×2 complexes form regardless of input ratio. However, no direct experiment tests the allosteric mechanism. For example, the authors do not measure whether binding of the first Spp1 subunit changes the conformation of the Mer2 tetramer, nor do they test whether Spp1 binding to one site affects the on-rate or off-rate at adjacent sites in a controlled manner. Alternative explanations for the 4×2 stoichiometry, such as steric constraints that simply prevent simultaneous occupancy of all four sites, are not excluded. The statement that "the low binding affinity obtained with our AFM assay, compared to the ones previously obtained by MST" supports allostery is speculative, as the discrepancy could arise from technical differences between the assays (e.g., surface immobilization effects, avidity effects in ensemble measurements, or differences in buffer conditions).
- **Why it matters** The allosteric mechanism is a key conceptual contribution of the paper. If the claim is not adequately supported, the mechanistic insight is weakened, and the paper becomes largely descriptive. The distinction between allostery and simple steric exclusion has implications for how the field thinks about Mer2-Spp1 complex assembly and its regulation.
- **Resolution test** The authors should either (a) provide direct experimental evidence for allostery, such as measuring Spp1 binding to Mer2 tetramers with one site pre-occupied or mutated, or using a conformational sensor (e.g., FRET, EPR, or HDX-MS) to detect structural changes upon Spp1 binding; or (b) temper the claim and explicitly discuss alternative explanations for the 4×2 stoichiometry, such as steric occlusion, and present the allosteric model as one of several possibilities.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The authors state that "the cost associated with Spp1 binding to Mer2 is compensated for by direct interactions of Spp1 with DNA" and propose an "occlusion-compensation" model where Spp1 reduces Mer2 DNA-binding but compensates via its own DNA-binding motif (R5K).
- **Evidence pointer** Results section "Spp1 directly contributes to DNA binding"; Figure 7; Discussion section "An occlusion-compensation mechanism for Mer2-Spp1-DNA interactions"
- **Concern** The occlusion-compensation model is built on the observation that full-length Spp1 does not bind DNA alone, but the C-terminal domain (residues 161-353) does. The authors then show that the R5K motif is required for this DNA binding in vitro. However, the in vivo experiments demonstrate that the R5K mutation does not recapitulate the spp1Δ phenotype, meaning the motif is not required for meiotic DSB formation. The authors interpret this as evidence that "the amount of Spp1 recruitment to Mer2 condensates is not a limiting factor in shaping the DSB landscape." This interpretation is reasonable but undercuts the functional significance of the DNA-binding activity they characterize in vitro. The occlusion-compensation model is presented as a mechanistic explanation for how Mer2-Spp1-DNA complexes assemble, but if the R5K motif is dispensable in vivo, the model's physiological relevance is unclear. The authors do not provide an alternative in vivo function for the R5K motif or explain why the in vitro DNA-binding activity exists if it is not required for DSB formation.
- **Why it matters** The in vivo negative result is a critical piece of data that directly contradicts the expectation that the R5K motif is functionally important. The authors need to reconcile this discrepancy more thoroughly. If the DNA-binding activity of Spp1 is not important for meiotic function, then the occlusion-compensation model may be an in vitro artifact, and the paper's central mechanistic claim is weakened.
- **Resolution test** The authors should either (a) provide additional in vivo experiments that test the R5K motif under conditions where Spp1 function is limiting (e.g., sensitized genetic backgrounds, competitive assays), or (b) revise the model to acknowledge that the in vitro DNA-binding activity may not be physiologically relevant and discuss alternative explanations for the observed in vitro phenomena.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical rigor
- **Claim pointer** The authors report an AFM-derived K_D of 1.9 ± 1.6 µM for the Spp1-Mer2 interaction, which is "about two orders of magnitude lower than the ensemble average affinity previously obtained by MST."
- **Evidence pointer** Results section "Single-molecule probing of Mer2-Spp1 interaction by atomic force spectroscopy"; Figure 1H-I; Supplementary Table 1
- **Concern** The discrepancy between AFM and MST affinities is noted but not resolved. The authors suggest it may reflect the allosteric model, but this is speculative. The AFM measurements involve immobilization of Mer2 on a surface and Spp1 on a tip, which can introduce artifacts such as steric hindrance, altered protein conformation, or avidity effects. The MST measurements were performed in solution and may reflect a different binding mode or oligomeric state. The authors do not discuss potential technical reasons for the discrepancy, such as differences in protein concentration, buffer composition, or the presence of crowding agents. Additionally, the error on the AFM K_D is large (±1.6 µM), and the kinetic parameters are derived from a Bell-Evans model that assumes a single energy barrier, which may not be valid for a multi-domain interaction.
- **Why it matters** The quantitative discrepancy between two biophysical methods is important because the authors use it to support the allosteric model. If the discrepancy is due to technical artifacts, the allosteric interpretation is weakened. The field needs confidence in the reported affinity to build on these results.
- **Resolution test** The authors should either (a) perform additional biophysical measurements (e.g., ITC, SPR, or MST under similar conditions) to cross-validate the affinity, or (b) provide a detailed discussion of potential technical reasons for the discrepancy and present the AFM-derived affinity as a lower bound or estimate rather than a definitive value.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical rigor
- **Claim pointer** The authors state that "the coiled-coil domain of Mer2 has four rotationally symmetrical sites that can bind a C-terminal α-helix of Spp1" and that AlphaFold models show two Spp1 subunits bound to opposite sides of the Mer2 tetramer.
- **Evidence pointer** Results section "Structural model of a minimal Mer2-Spp1 complex"; Figure 2; Supplementary Figures 3-5
- **Concern** The AlphaFold models are presented as high-confidence, but the authors do not provide confidence metrics (e.g., pLDDT scores, PAE values) or discuss the limitations of AlphaFold for predicting protein-protein interfaces, particularly for disordered regions. The models are used to guide mutagenesis, which is appropriate, but the structural claims should be tempered given that AlphaFold predictions are not experimentally determined structures. The authors also note that the position of the Spp1 PHD finger and Set1-ID varied between models, indicating uncertainty in the full-length complex structure. The SAXS data are used to validate the models, but the resolution of SAXS is limited, and the authors do not provide a quantitative comparison between the SAXS data and the models beyond chi-squared values.
- **Why it matters** The structural model is a key output of the paper. If the model is not robustly validated, the conclusions drawn from it, including the identification of interface residues and the occlusion-compensation model, are less reliable. The field needs confidence in the structural basis of the Mer2-Spp1 interaction.
- **Resolution test** The authors should provide AlphaFold confidence metrics and discuss their limitations, and/or obtain higher-resolution structural data (e.g., cryo-EM, X-ray crystallography) to validate the model. At minimum, the authors should clearly state the limitations of the AlphaFold models and avoid overinterpreting the predictions.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that "binding of one Spp1 subunit appears to allosterically modulate the affinity for the adjacent sites," but the evidence for this is indirect and the claim is presented as more definitive than the data support.
- **Required correction** Consider softening the language to "is consistent with allosteric modulation" or "suggests allosteric modulation" to better match the strength of the evidence.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section "Spp1 directly contributes to DNA binding"
- **Evidence pointer** Figure 7
- **Issue** The authors show that full-length Spp1 does not bind DNA alone, but the C-terminal domain does. The mechanism of auto-inhibition is not addressed. The authors state "how this auto-inhibition may take place is not clear," but do not provide any experimental or computational insight into this phenomenon.
- **Required correction** Add a brief discussion of potential mechanisms of auto-inhibition, or acknowledge this as a limitation and suggest future experiments to address it.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** AFM force spectroscopy data
- **Evidence pointer** Figure 1F-I; Supplementary Table 1
- **Issue** The number of independent experiments, number of force curves analyzed, and statistical methods for comparing binding frequencies are not clearly stated in the text.
- **Required correction** Provide details on sample sizes, replicates, and statistical tests used for the AFM data in the figure legends or methods.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** In vivo experiments
- **Evidence pointer** Figure 8C; Supplementary Figure 11
- **Issue** The in vivo experiments are limited to a single genetic background and a single time point. The authors do not assess whether the R5K mutation affects DSB formation at other loci or under different conditions.
- **Required correction** Acknowledge this limitation and suggest future experiments to test the generality of the findings.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion section "Assembly of the Mer2-Spp1-DNA complexes"
- **Evidence pointer** Discussion
- **Issue** The discussion of the occlusion-compensation model is somewhat convoluted and could be streamlined for clarity.
- **Required correction** Consider reorganizing the discussion to present the model more clearly, with a step-by-step explanation of the proposed mechanism.

## Risk / unsupported claims
- The allosteric modulation of Spp1 binding to Mer2 tetramers is inferred from indirect evidence and is not directly tested; this claim should be considered speculative.
- The occlusion-compensation model is presented as a mechanistic explanation, but the in vivo data show the R5K motif is dispensable for DSB formation, making the physiological relevance of this model unclear.
- The AFM-derived K_D of 1.9 ± 1.6 µM is presented as a quantitative measure of the interaction, but the large discrepancy with MST values and the potential for surface-immobilization artifacts mean this value should be interpreted with caution.
- The AlphaFold models are described as "high-confidence," but no confidence metrics are provided, and the variability in the position of the Spp1 PHD finger and Set1-ID between models indicates uncertainty in the full-length complex structure.
- The claim that "Spp1 recruitment reduces DNA binding by Mer2" is based on in vitro experiments with truncated constructs and may not reflect the behavior of full-length proteins in a cellular context.