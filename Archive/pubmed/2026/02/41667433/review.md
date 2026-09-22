## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, materials and methods, and supplementary figure/table legends
- **Assessment boundary** Scientific validity, technical soundness, and support of claims by presented evidence; no assessment of editorial fit or formatting
- **Shared manuscript claim summary** The authors propose that oxidized mitochondrial DNA (ox-mtDNA) released from stressed microglia directly binds to the NLRP3 inflammasome sensor via its intrinsically disordered region (IDR, residues 180-187), thereby activating the NLRP3-IL-1β axis and driving dopaminergic neurodegeneration in mouse models of Parkinson's disease
- **Visible evidence base** In vivo mouse models (stereotactic ox-mtDNA injection; LPS-primed rotenone model), transcriptomic profiling of MACS-sorted microglia and neurons, immunoblotting, immunofluorescence, ELISA, RT-qPCR, EMSA, in vitro PYD-caspase-1 cleavage assays, molecular docking predictions, and bioinformatic IDR analysis
- **Missing materials affecting confidence** Supplementary figures S1-S8 and Supplementary Table 1 are referenced but not provided; raw RNA-seq data and analysis scripts not provided; full western blot images not shown; statistical details for several comparisons not fully reported; no data on primary microglia; no data on human PD tissue

## Reviewer
- **Overall assessment** This manuscript addresses an important question in PD neuroimmunology: how mitochondrial stress in microglia translates into NLRP3 inflammasome activation and neurodegeneration. The central claim, that ox-mtDNA directly binds to the NLRP3 IDR to trigger activation, is novel and potentially field-shifting. However, the evidence as presented has several critical gaps. The direct binding claim rests on computational docking and EMSA data that are not fully controlled or quantified. The in vivo causal chain from ox-mtDNA release to NLRP3 activation to neurodegeneration is supported largely by correlative data, with only one loss-of-function approach (NLRP3 knockdown in vitro) and one pharmacological inhibitor (MCC950) used. The reliance on BV2 cells for mechanistic studies, without confirmation in primary microglia, weakens the translational relevance. The transcriptomic data are presented descriptively without clear statistical frameworks. Several key controls are missing, including specificity controls for the NLRP3 immunoprecipitation and appropriate negative controls for the EMSA. The manuscript is well-written and the figures are generally clear, but the mechanistic claims outpace the experimental evidence in several places.

- **Who would be interested in the results, and why** Researchers in neuroinflammation, innate immunity, mitochondrial biology, and Parkinson's disease pathogenesis would find these results of interest. The proposed direct ox-mtDNA-NLRP3 interaction mechanism, if validated, would be relevant to the broader inflammasome field, particularly those studying non-canonical NLRP3 activation. The potential therapeutic angle of targeting the NLRP3 IDR could attract drug discovery groups. The study also contributes to the growing literature on mtDNA as a DAMP in neurodegenerative disease.

- **Major strengths**
  1. The study addresses a significant gap in the field: the precise molecular mechanism linking microglial mitochondrial dysfunction to NLRP3 activation in PD
  2. The combination of in vivo models, transcriptomics, and biochemical approaches provides a multi-level perspective
  3. The identification of a specific IDR region (180-187) in NLRP3 as a potential ox-mtDNA binding site is novel and testable
  4. The use of both genetic (shRNA) and pharmacological (MCC950) approaches to validate NLRP3 involvement is commendable
  5. The authors acknowledge limitations of their in vivo models and discuss alternative interpretations

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency for direct binding claim
- **Claim pointer** "ox-mtDNA interacts with the positively charged IDR of NLRP3" and "ox-mtDNA can directly bind to the truncated NLRP3 (180-1033) and activate NLRP3"
- **Evidence pointer** Figure 7, EMSA and molecular docking sections
- **Concern** The central mechanistic claim of direct ox-mtDNA-NLRP3 binding rests on three lines of evidence: molecular docking predictions, EMSA, and in vitro cleavage assays. The docking predictions are computational and not experimentally validated. The EMSA shows binding but lacks key controls: no competition assay with unlabeled DNA, no testing of non-oxidized mtDNA in the same EMSA system, and no quantification of binding affinity. The in vitro cleavage assay demonstrates that ox-mtDNA plus NLRP3 (180-1033) can induce caspase-1 cleavage, but it is unclear whether this is specific to the IDR region or a general property of the truncated protein. The claim that the 180-187 region is the binding site is supported only by the docking prediction and the comparison between 180-1033 and 188-1033 constructs, but the latter comparison is shown only in supplementary data not provided.
- **Why it matters** The direct binding mechanism is the most novel and significant claim of the manuscript. If this is not rigorously established, the manuscript reduces to a descriptive study of mtDNA-induced NLRP3 activation, which has been previously reported. The specificity of the interaction (oxidized vs. non-oxidized, IDR-dependent) is critical for the proposed therapeutic strategy.
- **Resolution test** Provide quantitative EMSA data with purified components, including a titration series to estimate binding affinity, competition with unlabeled ox-mtDNA and non-oxidized mtDNA, and a mutant NLRP3 construct lacking the 180-187 region. Include a negative control protein (e.g., a non-DNA-binding protein) in the EMSA. For the cleavage assay, include a construct with a scrambled or mutated IDR sequence to demonstrate sequence specificity.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal evidence for in vivo pathway
- **Claim pointer** "ox-mtDNA drives NLRP3-IL-1β axis activation in microglia, leading to neurodegeneration in Parkinson's disease models"
- **Evidence pointer** Figures 1-3, 5
- **Concern** The causal chain from ox-mtDNA release to NLRP3 activation to neurodegeneration is not fully established. In the in vivo ox-mtDNA injection model, the authors show that ox-mtDNA injection causes behavioral deficits and TH+ neuron loss, and that microglia show NLRP3 pathway activation. However, they do not demonstrate that the neuronal damage is specifically mediated by microglial NLRP3 activation rather than direct effects of ox-mtDNA on neurons or other cell types. The MCC950 experiment (Fig. S5) is presented only in supplementary data and is not described in sufficient detail in the main text. In the LPS + rotenone model, the authors show correlation between ox-mtDNA release and NLRP3 activation, but the only loss-of-function evidence is in BV2 cells in vitro. No microglia-specific NLRP3 knockout or conditional knockout mouse is used to establish the causal role of microglial NLRP3 in vivo.
- **Why it matters** The title and abstract claim that mtDNA drives NLRP3 activation "leading to neurodegeneration." Without genetic or pharmacological evidence specifically in microglia in vivo, the causal direction and cellular specificity of this pathway remain uncertain. The authors themselves acknowledge that rotenone has direct effects on neurons, complicating interpretation.
- **Resolution test** Use microglia-specific NLRP3 conditional knockout mice (e.g., CX3CR1-Cre; NLRP3-flox) in the LPS + rotenone and/or ox-mtDNA injection models. Alternatively, use bone marrow chimeras or microglia depletion/repletion approaches. At minimum, provide the MCC950 data in the main text with full experimental details and demonstrate that MCC950 treatment does not affect neuronal survival directly.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Cell type specificity of ox-mtDNA effects
- **Claim pointer** "the injection of mtDNA into the substantia nigra pars compacta induces PD pathology in mice, characterized by the loss of dopaminergic (DA) neurons and the activation of microglia"
- **Evidence pointer** Figure 1, Figure 2
- **Concern** The authors use MACS to isolate microglia and neurons for transcriptomics, which is a strength. However, the claim that ox-mtDNA specifically activates microglia is not fully supported. The transcriptomic data show NLRP3 pathway upregulation in microglia, but the authors also note changes in neurons (Fig. 1B). The immunofluorescence data (Fig. 2A, B) show Iba-1 activation, but it is unclear whether ox-mtDNA is taken up by microglia specifically or by other cell types. The in vitro experiments use BV2 cells, which are a microglia-like cell line, but no comparison is made with primary microglia or other glial cell types (astrocytes, oligodendrocytes). The possibility that ox-mtDNA acts on neurons directly, or via astrocytes, is not excluded.
- **Why it matters** The manuscript claims a microglia-specific mechanism. If ox-mtDNA also acts on other cell types, the therapeutic strategy of targeting microglial NLRP3 may be incomplete. The field has learned that cell-type specificity is critical for understanding neuroinflammatory mechanisms.
- **Resolution test** Perform uptake experiments with fluorescently labeled ox-mtDNA in mixed glial cultures or brain sections to demonstrate microglia-specific uptake. Include astrocyte or mixed glial cultures in the in vitro experiments. If possible, use primary microglia to confirm key findings from BV2 cells.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Oxidized vs. non-oxidized mtDNA specificity
- **Claim pointer** "oxidized mtDNA is superior to nonoxidized mtDNA in activating the NLRP3-IL-1β axis"
- **Evidence pointer** Figure 6H-J, Figure S6
- **Concern** The claim that oxidized mtDNA is a more potent NLRP3 activator than non-oxidized mtDNA is important for the mechanistic model. However, the data supporting this are limited. The synthetic mtDNA was oxidized with H2O2, but the extent and nature of oxidation (8-OHdG levels) are only shown in supplementary data. The comparison between oxidized and non-oxidized mtDNA is shown only for the synthetic D-loop mtDNA, not for the endogenous mtDNA extracted from treated cells. The dose-response relationship is not explored. It is unclear whether the difference is quantitative (more oxidation = more activation) or qualitative (specific oxidation products).
- **Why it matters** The specificity for oxidized mtDNA is a key part of the model linking oxidative stress to NLRP3 activation. If non-oxidized mtDNA is equally potent, the model needs revision. The therapeutic implication of targeting oxidation would also be affected.
- **Resolution test** Provide a dose-response curve for both oxidized and non-oxidized mtDNA. Characterize the oxidation products (e.g., 8-OHdG, abasic sites, strand breaks) and correlate with activation potency. Test whether specific oxidation products (e.g., 8-OHdG-containing oligonucleotides) are sufficient for activation.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor and transparency
- **Claim pointer** Multiple claims throughout rely on statistical significance
- **Evidence pointer** All figures
- **Concern** The statistical methods are described in general terms, but specific details are lacking. For example, in Figure 1, the n numbers are stated (n=8 for behavior, n=5 for IHC), but it is unclear whether these are biological or technical replicates. The statistical tests used for each comparison are not consistently specified in the figure legends. The transcriptomic analysis lacks details on multiple testing correction, fold-change thresholds, and how the "NLRP3 pathway genes" were defined. The EMSA and docking results are not quantified statistically.
- **Why it matters** Reproducibility and rigor are essential for a high-impact claim. Without clear statistical reporting, readers cannot assess the robustness of the findings. This is particularly important for the transcriptomic data, which appear to be a major component of the evidence.
- **Resolution test** Provide complete statistical details for each figure panel, including the specific test used, the n and what it represents, and the exact p-values. For transcriptomics, provide details on the differential expression analysis, including the model, thresholds, and multiple testing correction. Add statistical analysis to the EMSA quantification.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of experimental design
- **Affected element** Figure 1A, Figure 3A
- **Evidence pointer** Figure legends
- **Issue** The experimental timelines for the in vivo models are not clearly described. For the ox-mtDNA injection model, it is unclear when behavior tests were performed relative to injection, and when tissues were collected. For the LPS + rotenone model, the timing of LPS priming versus rotenone treatment is not specified in the main text.
- **Required correction** Add a clear timeline schematic for each in vivo experiment, indicating the timing of injections, treatments, behavioral tests, and tissue collection.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Interpretation of transcriptomic data
- **Affected element** Figure 1B, Figure 2D-H
- **Evidence pointer** Results section
- **Issue** The transcriptomic analysis is described as showing "pronounced upregulation" of NLRP3 pathway genes, but the specific genes and their fold-changes are not presented in the main text. The heatmap in Figure 1B shows PD-related genes, but the selection criteria for these genes are not stated.
- **Required correction** Provide a table of the key differentially expressed genes in the NLRP3 pathway with fold-changes and adjusted p-values. State the criteria for gene selection in the heatmap.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Control for LPS effects
- **Affected element** Figure 3, Figure 4
- **Issue** LPS alone is shown to induce some NLRP3 activation (Fig. 3G, H), and the authors note this. However, the additive or synergistic effect of rotenone is not quantified relative to LPS alone. The statistical comparison between LPS alone and LPS + rotenone is not clearly reported.
- **Required correction** Clearly report the statistical comparison between LPS alone and LPS + rotenone for all key readouts, and discuss whether the effect is additive or synergistic.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Docking methodology
- **Affected element** Figure 7B-D
- **Evidence pointer** Methods section
- **Issue** The molecular docking methodology is described briefly. The Z-dock program is mentioned, but details on the input structures, scoring function, and how the "dominant binding conformation" was selected are not provided. The ΔG values are reported without error estimates.
- **Required correction** Provide more detail on the docking protocol, including the preparation of the ox-mtDNA and NLRP3 structures, the search parameters, and how the top hit was selected. If possible, provide multiple independent docking runs to assess robustness.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Nomenclature and consistency
- **Affected element** Throughout
- **Evidence pointer** Text
- **Issue** The manuscript uses "ox-mtDNA" and "oxidized mtDNA" interchangeably. The term "NLRP3-IL-1β axis" is used frequently but not always clearly defined. The distinction between "binding" and "activation" of NLRP3 is sometimes blurred.
- **Required correction** Use consistent terminology throughout. Define "NLRP3-IL-1β axis" at first use. Be precise about whether experiments measure binding, activation, or downstream signaling.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Generalizability of findings
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion focuses heavily on the proposed mechanism but does not adequately address the generalizability of the findings. The authors use LPS + rotenone as a PD model, but rotenone is not a common PD model in mice (MPTP and α-synuclein models are more widely used). The relevance to sporadic PD, where the trigger is unknown, is not discussed.
- **Required correction** Add a paragraph discussing the limitations of the LPS + rotenone model and the potential relevance of the findings to other PD models and to human PD.

## Risk / unsupported claims
- The claim that ox-mtDNA directly binds to the NLRP3 IDR (residues 180-187) is not fully supported by the provided evidence. The EMSA and docking data are suggestive but lack necessary controls and quantification.
- The claim that ox-mtDNA binding to NLRP3 "leads to" neurodegeneration in vivo is not causally established. The evidence is correlative, and the only loss-of-function data are in vitro or pharmacological.
- The claim that microglia are the specific cell type mediating ox-mtDNA effects in vivo is not fully supported, as no cell-type-specific manipulations were performed.
- The transcriptomic data are presented descriptively, and the claim of "pronounced upregulation" of NLRP3 pathway genes is not quantitatively supported in the main text.
- The superiority of oxidized over non-oxidized mtDNA in activating NLRP3 is based on limited data with a single synthetic construct and no dose-response analysis.
- The relevance of the findings to human PD is not established, as no human tissue or patient-derived samples were examined.