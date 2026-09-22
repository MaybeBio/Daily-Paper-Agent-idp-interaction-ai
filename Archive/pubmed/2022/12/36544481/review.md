## Review setup
- **Input scope** Full manuscript text (including abstract, results, discussion, and methods sections)
- **Assessment boundary** Scientific validity, methodological rigor, and support of claims based solely on the provided manuscript content
- **Shared manuscript claim summary** The authors report the first description of a Prosystemin (ProSys) protein-protein interaction (PPI) network in tomato, identified through a combination of in silico prediction (using PTIR and STRING databases) and in vitro affinity purification mass spectrometry (AP-MS), with selected interactions validated in vivo via bimolecular fluorescence complementation (BiFC). The network is proposed to explain the pleiotropic stress resistance observed in ProSys-overexpressing plants.
- **Visible evidence base** Results section (sub-network description, AP-MS findings, BiFC validation), Discussion section, Materials and Methods section, Figure 1 (ProSys sub-network), Figure 2 (BiFC confocal images), Figure 3 (network topology parameters), Table 1 (interactor detection summary), Table 2 and 3 (primer sequences)
- **Missing materials affecting confidence** Supplementary figures (Fig. S1, S2) and tables (Table A, B, C) are referenced but not provided; raw mass spectrometry data are not included; full list of 98 in silico interactors and ~70 AP-MS candidates is not available for independent assessment; statistical details for AP-MS analysis are incomplete; negative controls for BiFC are not described

## Reviewer

- **Overall assessment** This manuscript addresses a relevant question in plant stress biology by attempting to map the molecular network of the tomato defense peptide precursor ProSys. The combination of computational prediction and experimental validation is a reasonable strategy. However, the current presentation has substantial gaps in methodological detail, quantitative support, and critical controls that prevent full evaluation of the claims. The central conclusion that a robust ProSys PPI network has been identified is only partially supported by the evidence provided.

- **Who would be interested in the results, and why** Researchers studying plant defense signaling, particularly systemic wound responses and the role of peptide hormones in stress adaptation, would find this work of interest. The potential connection between ProSys and diverse pathways (calcium signaling, MAPK cascades, hormone crosstalk, sugar metabolism) could inform future functional studies. The methodological approach combining in silico and in vitro interactomics may also interest plant proteomics specialists.

- **Major strengths**
  1. The study addresses a clear knowledge gap: no ProSys interactors were previously known, despite the importance of this precursor in plant defense.
  2. The multi-pronged approach (in silico prediction, AP-MS, BiFC validation) is appropriate and mutually reinforcing when results converge.
  3. The identification of specific interactors with plausible functional links to known ProSys-mediated phenotypes (e.g., NaDED, HSP70, MAPK6) provides testable hypotheses for future work.
  4. The discussion contextualizes findings within established literature on plant defense pathways, strengthening the biological interpretation.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "more than three hundred proteins able to bind ProSys were identified" by AP-MS and that "candidate interactors with a fold change greater than four, around seventy, were selected."
- **Evidence pointer** Results section, "Experimental identification of ProSys interactors"; Materials and Methods, "LC-MS data analysis"
- **Concern** The AP-MS methodology is described with insufficient detail to assess its rigor. The authors state that SAINT algorithm and CRAPome software were used, but do not provide the number of biological replicates, the specific SAINT probability thresholds, the criteria for distinguishing specific from non-specific interactors beyond FC-A values, or how the GFP control was processed. The filtering of "ribosomal proteins and translation-related proteins" is mentioned but the rationale and the number of proteins removed are not quantified. Without these details, the reliability of the ~70 candidate list cannot be evaluated.
- **Why it matters** AP-MS is prone to false positives, particularly with highly abundant or sticky proteins. The authors' filtering strategy appears to rely heavily on fold-change thresholds, which may not adequately control for background binding. If the interactor list is not robust, downstream interpretations and the BiFC validation targets are compromised.
- **Resolution test** Provide a complete description of AP-MS experimental design including replicate numbers, SAINT score cutoffs, CRAPome parameters, and a detailed account of the filtering pipeline with protein counts at each step. Include a supplementary table listing all identified proteins with their FC-A scores, SAINT probabilities, and the criteria used to exclude or include them.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Support for claims
- **Claim pointer** The authors state that "The results demonstrate that ProSys interacts with multiple proteins" and that the network "reveals new key molecular events in the ProSys-dependent defence response."
- **Evidence pointer** Results section, "In vivo validation of interactions"; Table 1; Figure 2
- **Concern** Only five proteins were tested by BiFC, and of these, only three are listed as validated (NaDED, HSP70, MYB transcription factor, MAPK6, and ATP-dependent clp protease are listed in Table 1, but the text indicates that four were selected from in silico/in vitro overlap and one from in silico alone). The BiFC results are presented as a single confocal image (Figure 2) without quantification, negative controls (e.g., co-expression with empty vector or a non-interacting protein), or demonstration of specificity. The claim that these interactions are "validated" is therefore overstated. Furthermore, the selection criteria for these five proteins from the ~70 candidates are not clearly justified.
- **Why it matters** BiFC is a valuable validation method, but without proper controls and quantification, the results only demonstrate that the proteins can be brought into proximity when overexpressed, not that they interact endogenously. The leap from five tested proteins to a general claim of a validated network is not supported.
- **Resolution test** Include negative controls for each BiFC pair (e.g., a known non-interacting protein or a mutant version), provide quantitative data on fluorescence signal intensity across multiple cells/experiments, and clearly state the criteria used to select the five proteins for validation. If possible, include an independent validation method (e.g., co-immunoprecipitation from plant extracts) for at least one interaction.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors describe the in silico network as containing 99 nodes and 98 interactions, with ProSys as a central hub based on degree distribution, betweenness centrality, and clustering coefficient.
- **Evidence pointer** Results section, "Description of the ProSys sub-network and in silico identification of its main interactors"; Figure 3
- **Concern** The network analysis is presented descriptively without statistical context. The authors state that the network is "scale-free" and that ProSys has a central role, but no comparison is made to random networks or to other nodes' properties. The betweenness centrality and clustering coefficient values are not reported numerically, and the significance of ProSys's position is not tested. Additionally, the criteria for including interactions from PTIR and STRING (confidence scores, evidence types) are not specified.
- **Why it matters** Network topology claims require statistical benchmarking to be meaningful. Without such analysis, the assertion that ProSys is a "hub" is anecdotal. Moreover, the quality of the input data (predicted vs. experimentally derived interactions) directly affects the reliability of the network.
- **Resolution test** Provide quantitative network statistics (degree, betweenness, clustering coefficient) for ProSys and other key nodes, compare these to a null model (e.g., randomized networks with same degree distribution), and specify the confidence thresholds used to include interactions from PTIR and STRING.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The authors state that "the strategy adopted was successful, allowing us to describe the ProSys PPI network for the first time."
- **Evidence pointer** Materials and Methods, "cDNA cloning and vector construction" and "Protein extraction for AP-MS"
- **Concern** Several methodological details essential for reproducibility are missing. The exact composition of lysis buffers is partially given but not fully specified. The conditions for the AP-MS binding and washing steps are not described. The LC-MS gradient and run time are not provided. The BiFC imaging parameters (e.g., laser power, gain, pinhole) are not stated. The age and growth conditions of N. benthamiana and tomato plants are only partially described.
- **Why it matters** Reproducibility is a cornerstone of scientific publication. The current level of detail is insufficient for another laboratory to replicate the experiments, which undermines the utility of the work.
- **Resolution test** Expand the Materials and Methods to include complete buffer compositions, incubation times, temperatures, instrument settings, and plant growth conditions. Consider providing a step-by-step protocol as supplementary material.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1
- **Evidence pointer** Results section, "Description of the ProSys sub-network"
- **Issue** The figure legend is minimal and does not explain the meaning of node colors, shapes, or edge types beyond what is in the main text. The distinction between "up-regulated genes," "down-regulated genes," and "putative interactors" is mentioned but not visually clear.
- **Required correction** Expand the figure legend to fully describe all visual elements, including the color scheme for sub-cellular localization, the shape coding for gene expression status, and the source of each interaction (PTIR vs. STRING vs. both).

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion section, "ProSys interacts with genes involved in early defence responses"
- **Evidence pointer** Discussion section
- **Issue** The authors state that the absence of SYR1 and SYR2 from the network is due to the receptors' affinity for the processed Sys peptide rather than the precursor. This is a reasonable hypothesis, but it is presented as an explanation without acknowledging alternative possibilities (e.g., technical limitations of the databases, low expression levels).
- **Required correction** Soften the language to present this as a plausible interpretation and briefly note alternative explanations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Table 1
- **Evidence pointer** Results section, "In vivo validation of interactions"
- **Issue** Table 1 lists five proteins but does not indicate which detection method (AP-MS, in silico, or both) identified each protein for the initial selection. The column headers are ambiguous.
- **Required correction** Add a column or modify the table to clearly indicate the detection method(s) for each protein and whether the interaction was validated by BiFC.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Materials and Methods, "LC-MS data analysis"
- **Evidence pointer** Materials and Methods
- **Issue** The authors state that "Statistical analysis for this dataset was performed using the Student's t-test" but do not specify what comparisons were made, how multiple testing was handled, or what significance thresholds were applied.
- **Required correction** Provide details on the statistical tests used, including the comparisons performed, the correction for multiple testing (if any), and the significance cutoffs.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Language
- **Affected element** Throughout
- **Evidence pointer** Entire manuscript
- **Issue** There are several typographical and grammatical errors (e.g., "salycilic acid" should be "salicylic acid", "epim\dehyd" appears to be a formatting error, inconsistent use of italics for gene names).
- **Required correction** Perform a thorough language edit to correct typographical errors and ensure consistent formatting of gene names and chemical compounds.

## Risk / unsupported claims
- The claim that "more than three hundred proteins able to bind ProSys were identified" is not fully supported as the raw data and analysis parameters are not provided.
- The claim that the five tested proteins represent validated interactions is overstated given the lack of negative controls and quantification in the BiFC experiments.
- The assertion that ProSys acts as a central hub in the network is not statistically substantiated.
- The statement that the ProSys PPI network is described "for the first time" is plausible but cannot be fully verified without a more comprehensive literature search being documented.
- The functional interpretations linking specific interactors to ProSys-mediated phenotypes (e.g., NaDED to sugar-mediated defense) are speculative and should be framed as hypotheses rather than conclusions.
- The claim that the absence of SYR1/SYR2 from the network is explained by receptor specificity for the processed peptide is presented as fact rather than hypothesis.