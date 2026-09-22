## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and figure legends
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors propose that Aβ40, while not undergoing liquid-liquid phase separation itself, enhances Tau phase separation and accelerates its transition to solid-like aggregates. They propose a mechanism whereby Aβ40 initially solubilizes Tau nanoclusters into smaller species, which then promotes subsequent co-condensation and fibril formation. This is supported by experimental data (turbidity, fluorescence microscopy, FRAP, NMR, mass photometry, ThT assays, cell viability) and coarse-grained molecular dynamics simulations.
- **Visible evidence base** Main text figures 1–7 (as referenced), supplementary figures 1–14 (as referenced), methods section
- **Missing materials affecting confidence** Original figure images and full figure legends for all panels; supplementary figure data; raw NMR spectra and assignments; mass photometry raw distributions; simulation input parameters and trajectory details; statistical analysis details for all comparisons; cell viability raw data

## Reviewer

- **Overall assessment** This manuscript addresses an important and timely question regarding the molecular interplay between Aβ and Tau in Alzheimer's disease, specifically in the context of biomolecular condensates. The combination of experimental biophysics and coarse-grained simulations is appropriate and potentially powerful. The central claim that Aβ40 acts as a catalyst for Tau phase separation and aggregation via an initial nanocluster solubilization step is interesting and mechanistically plausible. However, several technical concerns and gaps in the presented evidence currently limit the strength of the conclusions. The relationship between the proposed "solubilization" step and the subsequent enhancement of phase separation requires further clarification, and the quantitative support for some key claims is not fully established from the provided material.

- **Who would be interested in the results, and why** Researchers in the fields of neurodegeneration, protein phase separation, amyloid biology, and biophysics. The work is also relevant to those studying protein-protein interactions in disease contexts and the development of therapeutic strategies targeting condensate dynamics. The proposed catalytic mechanism for Aβ in Tau aggregation could have broad implications for understanding disease propagation.

- **Major strengths**
  1. The study tackles a clinically relevant and mechanistically underexplored question: how Aβ and Tau interact at the level of phase separation.
  2. The combination of multiple orthogonal experimental techniques (microscopy, FRAP, NMR, mass photometry, ThT) with coarse-grained simulations provides a multi-scale view of the process.
  3. The proposed model, involving an early solubilization step followed by enhanced condensation, is conceptually novel and provides a testable framework for future studies.
  4. The use of physiologically relevant conditions (e.g., 150 mM NaCl, pH 7.4) and crowding agents strengthens the translational relevance.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic coherence
- **Claim pointer** "Aβ40 transiently solubilizes Tau nanoclusters into smaller species" and this "ultimately promot[es] pathogenic aggregation" and enhances phase separation.
- **Evidence pointer** Results section "Molecular insights into the interaction between Tau and Aβ40"; Figure 3; Supplementary Figure 6
- **Concern** The manuscript presents a two-step model: (1) Aβ40 dissolves Tau nanoclusters, and (2) this solubilization promotes subsequent phase separation and aggregation. However, the logical connection between these two steps is not clearly established. If Aβ40 dissolves Tau nanoclusters, one might expect a reduction in aggregation-prone species, not an enhancement. The authors need to explain how the transient solubilization step mechanistically leads to a more aggregation-prone state. Is the solubilized Tau in a different conformational state? Does the interaction with Aβ40 prime Tau for subsequent self-association? The current narrative appears somewhat contradictory and requires a more detailed mechanistic model.
- **Why it matters** The proposed catalytic mechanism is the central novel claim of the manuscript. If the link between solubilization and enhanced phase separation/aggregation is not mechanistically clear, the overall model is weakened. The reader is left wondering whether the solubilization is a cause or a consequence of the interaction, and how it relates to the observed enhancement of phase separation.
- **Resolution test** The authors should provide a more explicit mechanistic model, potentially supported by additional data (e.g., conformational analysis of Tau in the presence of Aβ40, or a detailed kinetic model showing how the solubilization step feeds into the nucleation of new condensates). A clear explanation of how a solubilization step can be a precursor to enhanced condensation is required.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative support for claims
- **Claim pointer** "Aβ40 significantly enhances Tau phase separation" and "accelerates liquid-to-solid maturation."
- **Evidence pointer** Figure 1C, 1F; Figure 2C–F
- **Concern** The quantitative support for the key claims of enhanced phase separation and accelerated maturation is not fully presented in the text. For example, the turbidity data in Figure 1C shows a three-fold increase, but the statistical analysis and the concentration dependence are not described in the text. Similarly, the FRAP data in Figure 1F and 2D–F are described qualitatively ("reduced fluorescence recovery"), but the recovery half-times or mobile fractions are not reported. The quantification of condensate area in Figure 2C is presented, but the statistical significance for the day 1 comparison is not stated. Without these quantitative details, it is difficult to assess the robustness of the conclusions.
- **Why it matters** The central claims of the manuscript are based on quantitative differences in phase behavior and material properties. Without clear statistical reporting and effect sizes, the reader cannot evaluate the strength of the evidence.
- **Resolution test** Provide full statistical details for all quantitative comparisons, including exact p-values, effect sizes, and the number of independent replicates. Report FRAP recovery parameters (e.g., mobile fraction, half-time) with appropriate fitting errors. Clarify the statistical significance of all comparisons in Figure 2C.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Simulation-experiment consistency
- **Claim pointer** "Simulations further indicate that early interactions are non-specific and mediated by Tau repeat domains, ultimately promoting pathogenic aggregation."
- **Evidence pointer** Results section "Molecular mechanisms underlying the enhancement of Tau phase separation by Aβ40"; Figure 4; Figure 5
- **Concern** The coarse-grained simulations are used to support the experimental findings, but the connection between the two is not always clear. For example, the simulations show that Aβ40 alone has low phase separation propensity, consistent with experiments. However, the simulations also show that the mixed system forms a denser condensate than Tau alone. The text states that Aβ40 "reduces the dynamics of Tau molecules," but the experimental FRAP data show reduced recovery, which is consistent. However, the key claim that the interaction is "non-specific" and "mediated by Tau repeat domains" needs more support. The contact analysis in Figure 5 shows which residues are involved, but the text does not explain how this relates to the "solubilization" step observed experimentally. The simulations appear to start from a pre-formed dense phase, so they may not capture the initial solubilization event.
- **Why it matters** The simulations are a key part of the evidence for the proposed mechanism. If the simulations do not directly model the solubilization step, or if the connection between the simulated interactions and the experimental observations is not clear, the support for the mechanism is weakened.
- **Resolution test** Clarify what specific aspect of the experimental observations the simulations are intended to reproduce. If the simulations do not capture the initial solubilization step, state this limitation explicitly. Provide a more direct comparison between simulated and experimental observables (e.g., predicted FRAP recovery vs. measured).

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Biological relevance
- **Claim pointer** "Aβ40 enhances Tau phase separation, accelerates liquid-to-solid transitions, and promotes amyloid fibril formation" and "increases Tau-mediated cytotoxicity."
- **Evidence pointer** Figure 6; Results section "Aβ40 promote Tau induced toxicity"
- **Concern** The cytotoxicity data are presented in a somewhat confusing manner. The text states that in the absence of PEG, Aβ40 appears to reduce toxicity by dissolving Tau aggregates, while in the presence of PEG, it enhances toxicity by promoting phase separation. However, the data in Figure 6C show that the 1:1 mixture has similar toxicity to Tau alone, and the 1:2 mixture is more toxic. The relationship between the in vitro phase separation assays (which use PEG) and the cell-based assays (which do not) is not clearly established. The authors should clarify how the conditions in the cell assays relate to the phase separation conditions.
- **Why it matters** The cytotoxicity data are used to support the pathological relevance of the proposed mechanism. If the connection between the in vitro phase behavior and the cellular outcomes is not clear, the translational significance of the findings is weakened.
- **Resolution test** Provide a clearer explanation of how the conditions in the cell-based assays relate to the phase separation conditions. Discuss whether the observed cytotoxicity is due to the condensates themselves, the fibrils, or the soluble oligomers. Consider performing cell-based assays under crowding conditions to more directly test the role of phase separation in toxicity.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of writing
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, Introduction
- **Issue** The abstract and introduction contain some long and complex sentences that could be simplified for clarity. For example, the sentence "Although the co-occurrence and synergistic effects of Aβ and Tau are well established, the mechanisms underlying their interplay in a biomolecular condensate environment remain unclear" could be broken into two sentences.
- **Required correction** Revise for clarity and conciseness, particularly in the abstract, to ensure the key findings are accessible to a broad readership.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Figure presentation
- **Affected element** Figure 1, Figure 2
- **Evidence pointer** Figure 1, Figure 2
- **Issue** The figure legends are not fully provided in the manuscript text. It is difficult to assess the data without the complete legends, including the definitions of all abbreviations and the specific conditions for each panel.
- **Required correction** Provide complete figure legends for all main and supplementary figures, including all experimental conditions, concentrations, and statistical annotations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Methods section
- **Evidence pointer** Methods section
- **Issue** The methods section for the NMR experiments is brief. It is not clear how the chemical shift perturbations were calculated and which residues were included in the analysis. The assignment of the Tau spectrum is referenced to a BMRB entry, but the specific conditions (e.g., pH, temperature) should be stated.
- **Required correction** Expand the NMR methods to include details on data processing, CSP calculations, and the criteria for identifying significant perturbations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 2C, Figure 6
- **Evidence pointer** Figure 2C, Figure 6
- **Issue** The statistical tests used for the comparisons in Figure 2C and Figure 6 are not fully described. It is stated that t-tests were used, but it is not clear whether these were one- or two-tailed, and whether corrections for multiple comparisons were applied.
- **Required correction** Provide full details of the statistical tests used, including the type of test, the number of replicates, and any corrections for multiple comparisons.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** Throughout
- **Issue** The term "nanocluster" is used throughout, but its definition is not explicitly provided. It would be helpful to define this term early in the manuscript, particularly in the context of the mass photometry and NMR data.
- **Required correction** Define "nanocluster" in the introduction or results section, and clarify the size range and physical nature of these species.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The discussion does not explicitly address the limitations of the study, such as the use of a truncated Tau construct (K18) in some experiments, the in vitro nature of the system, and the potential differences between the artificial crowding conditions and the cellular environment.
- **Required correction** Add a paragraph discussing the limitations of the study and the potential impact of these limitations on the interpretation of the results.

## Risk / unsupported claims
- The claim that Aβ40 acts as a "catalyst" for Tau aggregation is not fully supported. A catalyst is typically defined as a substance that increases the rate of a reaction without being consumed. The manuscript does not demonstrate that Aβ40 is not consumed or incorporated into the final aggregates. The term "catalyst" may be an overstatement based on the presented data.
- The claim that the early interaction is "non-specific" is not fully supported. While the simulations suggest that interactions are mediated by multiple residue types, the experimental data do not directly address the specificity of the interaction.
- The relationship between the "solubilization" step observed by NMR and mass photometry and the subsequent enhancement of phase separation is not mechanistically established. The manuscript does not provide a clear explanation for how dissolving nanoclusters leads to enhanced condensation.
- The claim that Aβ40 "promotes amyloid fibril formation" is based on ThT fluorescence data, but the manuscript does not provide structural evidence (e.g., electron microscopy, X-ray diffraction) that the ThT-positive species are indeed amyloid fibrils.
- The statement that "Aβ40 enhances Tau phase separation" is supported by turbidity and microscopy data, but the quantitative extent of this enhancement and its concentration dependence are not fully reported.
- The claim that the findings "offer a potential therapeutic strategy" is speculative and not directly supported by the data presented.