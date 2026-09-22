## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplemental figure legends
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided manuscript text
- **Shared manuscript claim summary** The N-terminal region of plant ARGONAUTE1 (AGO1), specifically the N-coil and globular N-terminal domain, serves as a hub for interactions with regulatory factors, particularly those involved in regulated proteolysis. Two distinct interaction modes are proposed: one dependent on the N-coil and one independent of it, requiring distinct sets of amino acid residues in the globular N domain.
- **Visible evidence base** Yeast two-hybrid screening results, directed yeast two-hybrid interaction assays, site-directed mutagenesis analysis, BiFC experiments in plant cells, pulse-labeling protein stability assays, CRISPR-Cas9 generated knockout lines, sequence alignments, and structural modeling
- **Missing materials affecting confidence** Figures 1-8 and Supplemental Figures S1-S5 are referenced but not provided; Table 1 and Supplemental Tables 1-2 are referenced but not provided; quantitative data for pulse-labeling experiments and statistical analyses are not fully described; details of BiFC quantification are not provided

## Reviewer
- **Overall assessment** This manuscript presents a systematic identification and characterization of protein-protein interaction partners for the N-terminal region of Arabidopsis AGO1, with a focus on factors involved in regulated proteolysis. The work identifies two distinct interaction modes mediated by the N-coil and the globular N domain, supported by mutagenesis and in vivo stability assays. The findings are potentially significant for understanding AGO1 regulation, but several technical concerns and missing data limit the strength of the conclusions as currently presented.
- **Who would be interested in the results, and why** Researchers studying RNA interference mechanisms, ARGONAUTE protein biology, plant stress responses, and regulated protein degradation pathways. The identification of specific interaction surfaces on AGO1 could inform studies on AGO protein regulation across eukaryotes, and the connection to autophagy receptors and ubiquitin-proteasome pathway components may interest cell biologists studying protein quality control.
- **Major strengths** The study addresses a poorly understood region of AGO proteins and provides a systematic approach to identify interaction partners. The combination of unbiased screening with targeted mutagenesis and in vivo validation is methodologically sound. The distinction between N-coil-dependent and N-coil-independent interaction modes provides a conceptual framework for future studies. The use of multiple independent validation methods (yeast two-hybrid, BiFC, protein stability assays) strengthens the conclusions.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (incomplete evidence for in vivo relevance), R1-M2 (inadequate validation of interaction specificity), R1-M3 (insufficient mechanistic distinction between interaction modes)
- **Assessment against Nature-style criteria** Originality: The work provides novel insights into AGO1 N-terminal domain function, which has been relatively understudied compared to other AGO domains. The identification of the N-coil as an interaction hub is a new contribution. Scientific importance: The findings have implications for understanding AGO1 regulation and RNAi pathway control, which is relevant to plant biology and potentially broader eukaryotic systems. However, the significance is somewhat limited by the focus on a single AGO protein and the lack of functional characterization beyond protein stability. Interdisciplinary readership: The work will primarily interest plant molecular biologists and RNAi researchers. The connection to autophagy and ubiquitin-proteasome pathways may attract cell biologists, but the scope is relatively narrow. Technical soundness: The experimental approaches are generally appropriate, but several technical concerns (detailed below) need to be addressed. Readability for nonspecialists: The manuscript is generally well-written and accessible, though some sections assume familiarity with yeast two-hybrid and plant transformation methodologies.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the in vivo relevance of the identified interactions and the specificity of the interaction modes.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength for in vivo relevance
- **Claim pointer** The authors claim that "Mutation of AGO1 residues necessary for interaction with protein degradation factors in yeast stabilizes reporters fused to the AGO1 N-terminal domain in plants, supporting their in vivo relevance."
- **Evidence pointer** Results section, Figure 8 (location not provided)
- **Concern** The in vivo validation relies on protein/mRNA ratios from transgenic lines expressing NcGN AGO1-YFP fusions. The authors report approximately 2-fold higher protein/mRNA levels in ati1-1 ati2-3 mutants compared to wild type, and higher ratios for the 3m and 6m mutants. However, the manuscript does not provide sufficient detail on the number of independent transgenic lines analyzed, the statistical significance of the differences, or the variability between lines. Additionally, the authors acknowledge they "cannot formally exclude an indirect effect of loss of ATI1/ATI2 on the translation of the NcGN AGO1-YFP mRNA," which weakens the direct link between the identified interactions and protein degradation.
- **Why it matters** The central claim of the manuscript is that the identified interactions have biological relevance in plants. Without robust quantitative data demonstrating significant and reproducible effects on protein stability, the in vivo significance of the yeast two-hybrid findings remains uncertain.
- **Resolution test** Provide quantitative data from multiple independent transgenic lines with statistical analysis. Include a more direct assessment of protein degradation rates (e.g., cycloheximide chase assays) rather than steady-state protein/mRNA ratios. Address the potential indirect effects of ATI1/ATI2 loss on translation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Interaction specificity
- **Claim pointer** The authors claim that "most of the candidate interactors isolated by yeast two-hybrid screening are specific to AGO1" based on testing against NcGN AGO4 and NcGN AGO10.
- **Evidence pointer** Results section, Figure 3 (location not provided)
- **Concern** The specificity testing was performed only for a subset of interactors (ATI1, ATI2, AUF1, AUF3, UBI, HUB1, PP2C, Hsp90.3) against only two other AGO paralogs. The manuscript does not report testing against all 10 Arabidopsis AGO paralogs, nor does it address potential non-specific interactions with unrelated proteins. Additionally, the criteria for "preferential or exclusive" interaction are not clearly defined with quantitative thresholds.
- **Why it matters** The claim of AGO1 specificity is important for the proposed model that the N-terminal region serves as a specific regulatory hub. If interactions are shared across multiple AGO paralogs, the biological implications would be different.
- **Resolution test** Test the interactors against a broader panel of AGO paralogs, particularly those most closely related to AGO1. Provide quantitative interaction data with clear thresholds for specificity. Include appropriate negative controls for non-specific protein-protein interactions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic distinction between interaction modes
- **Claim pointer** The authors claim that "NcGN AGO1 uses at least two distinct modes for binding to regulatory factors: one that depends critically on the N-coil as well as a subset (P259, E307) of GN residues, and one that is independent of the N-coil and requires a distinct subset (D205, M304) of GN residues."
- **Evidence pointer** Results section, Figures 6-7 (location not provided)
- **Concern** The distinction between the two interaction modes is based on differential effects of point mutations on yeast two-hybrid interactions. However, the manuscript does not provide structural or biophysical evidence that these residues are part of distinct binding surfaces. The possibility that mutations indirectly affect protein folding or stability is not fully addressed, although the authors do show expression of mutant proteins in yeast.
- **Why it matters** The proposed model of two distinct interaction modes has implications for understanding how AGO1 might be differentially regulated by different factors. If the distinction is not robust, the model may need revision.
- **Resolution test** Provide additional evidence for distinct binding surfaces, such as competitive binding assays, structural analysis, or demonstration that mutations do not globally disrupt protein structure. Consider testing whether the two modes can be simultaneously engaged.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Experimental detail
- **Affected element** Yeast two-hybrid screening methodology
- **Evidence pointer** Methods section (location not provided)
- **Issue** The manuscript states that three prey cDNA libraries were used for screening but does not specify the tissue sources or developmental stages from which these libraries were generated. This information is important for interpreting the biological relevance of the identified interactors.
- **Required correction** Specify the tissue sources and developmental stages for each of the three cDNA libraries used in the yeast two-hybrid screens.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** BiFC quantification
- **Evidence pointer** Results section, Figure 5 (location not provided)
- **Issue** The BiFC experiments are described qualitatively ("YFP fluorescence was specifically detected"), but no quantitative data or statistical analysis is provided. It is unclear how many independent experiments were performed and whether the differences between positive and negative controls were statistically significant.
- **Required correction** Provide quantitative fluorescence measurements with statistical analysis for the BiFC experiments, including the number of independent biological replicates.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion of N-coil accessibility
- **Evidence pointer** Discussion section (location not provided)
- **Issue** The authors speculate that the G186R mutation in the AGO1 N-coil may make the N-coil accessible in the loaded conformation, leading to increased degradation. This is presented as a plausible explanation, but the manuscript does not provide experimental evidence to support this specific mechanism.
- **Required correction** Clearly distinguish between speculation and evidence-based conclusions in the discussion. If possible, provide preliminary data or cite relevant literature supporting this mechanism.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Interactor validation
- **Evidence pointer** Results section, Table 1 (location not provided)
- **Issue** The manuscript identifies 15 potential interactors from the yeast two-hybrid screens but only validates a subset through directed assays and mutagenesis. The fate of the remaining interactors is not discussed.
- **Required correction** Provide a brief statement addressing whether the remaining interactors were validated and, if not, why they were excluded from further analysis.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Pulse-labeling experiments
- **Evidence pointer** Methods section (location not provided)
- **Issue** The pulse-labeling experiments use 35S-methionine/cysteine labeling, but the manuscript does not specify the specific activity of the label, the duration of the pulse, or the chase conditions. This limits the reproducibility of the experiments.
- **Required correction** Provide complete details of the pulse-labeling protocol, including specific activity, pulse duration, chase conditions, and the number of biological replicates.

## Risk / unsupported claims
- The claim that the N-coil is "of special importance" for interactions is supported by mutagenesis data, but the relative contribution of the N-coil versus the globular N domain to overall AGO1 regulation in planta is not directly assessed.
- The speculation that the N-coil-independent interaction mode may be used by small RNA-bound AGO1 is explicitly acknowledged as unsupported by evidence and should be clearly framed as speculation.
- The statement that "the N-coil is only accessible for interaction in the free state of AGO1" is attributed to an accompanying study, but this claim cannot be evaluated from the provided material.
- The functional significance of the identified interactions for AGO1-mediated RNA silencing is not directly tested, and the manuscript does not demonstrate that the identified regulatory factors affect AGO1 function in RNAi pathways.
- The claim that "the N-coil also stands out in collections of arabidopsis ago1 mutant alleles defective in miRNA function" is presented as prior knowledge, but the specific evidence is not provided in this manuscript.