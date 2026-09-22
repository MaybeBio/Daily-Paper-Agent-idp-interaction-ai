## Review setup
- **Input scope** Full manuscript text (abstract, results and discussion, conclusion, materials and methods, supplementary notes referenced) as provided on bioRxiv.
- **Assessment boundary** Scientific content, methodology, data interpretation, and internal consistency of the provided manuscript. No external data, figures, or supplementary files were independently accessed or verified.
- **Shared manuscript claim summary** The authors use fluorescence microscopy and photobleaching step counting to quantify the behaviour of NELF proteins in living and fixed HeLa cells before and during stress-induced condensation. They report the existence of small, dynamic, heterogeneous clusters in both stressed and unstressed cells, a critical cluster size of ~1500 NELFA molecules for condensate growth, a flat free-energy landscape inconsistent with classical nucleation theory, and a role for p38 kinase in enabling large cluster formation.
- **Visible evidence base** Abstract, full results and discussion section, conclusion, materials and methods, list of supplementary notes and movies, author contributions, competing interests, acknowledgements.
- **Missing materials affecting confidence** All figures, supplementary figures, supplementary notes (full content), supplementary movies, and raw data. The manuscript text references specific figures and notes (e.g., Fig. 1, Fig. 2, Fig. 3, Fig. 4, Suppl. Fig. S5, S7, S9, S11, Suppl. Notes 1-11) but their content is not available in the provided material.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question in the field of biomolecular condensates, namely the behaviour of proteins prior to condensation. The combination of living-cell imaging with photobleaching step counting is a promising approach to obtain quantitative information in a cellular context. The authors present a compelling narrative that pre-condensate clusters are heterogeneous, dynamic, and not governed by classical nucleation theory. However, the strength of the conclusions is heavily dependent on the data presented in the figures and supplementary materials, which were not available for this review. Several methodological details and analytical steps are described only in supplementary notes, making a full assessment of technical soundness impossible. The claim of a flat free-energy landscape is particularly consequential and requires careful scrutiny of the underlying calculations and assumptions. The role of p38 kinase is interesting but the evidence presented in the text is preliminary. Overall, the manuscript has the potential to be a significant contribution, but the current evidence base is insufficient to fully establish the central claims.
- **Who would be interested in the results, and why** Researchers in the fields of phase separation, cell biology, biophysics, and gene regulation would be interested. The work directly addresses the molecular mechanisms of condensate formation in living cells, a topic of broad interest. The methodological approach of combining single-molecule counting with live-cell tracking could be of interest to method developers. The findings on non-classical nucleation and the role of p38 kinase have implications for understanding how cells regulate condensation in response to stress.
- **Major strengths**
    1.  The study tackles a difficult and under-explored problem: the pre-condensate state of proteins in living cells.
    2.  The combination of techniques (HILO microscopy, machine-learning segmentation, single-particle tracking, and photobleaching step counting) is innovative and powerful.
    3.  The use of a physiologically relevant, inducible system (NELF condensation upon arsenic stress) is a strength.
    4.  The observation of small, dynamic clusters in unstressed cells is a potentially important finding.
    5.  The authors are careful to validate their living-cell data against fixed-cell calibrations.
- **Major Concerns**

    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness and data interpretation
    - **Claim pointer** The authors claim that the free-energy landscape for cluster formation is "flat" and that this is "best explained as non-classical nucleation with a flat free-energy landscape for clusters of a range of sizes".
    - **Evidence pointer** Figure 3E, Supplementary Note 7, location not provided.
    - **Concern** The calculation of the free-energy landscape, ΔG_n = -k_B T ln(p_n / np_1), is a central piece of evidence for the non-classical nucleation claim. This calculation is based on the probability distribution of cluster sizes, p_n, which is derived from the tracking data. The validity of this calculation depends on several critical assumptions, including the system being in quasi-equilibrium, the correct identification of clusters, and the accurate determination of cluster size in terms of molecule number. The manuscript text does not provide sufficient detail on how p_n was computed, how the equilibrium assumption was justified for a dynamic, non-equilibrium cellular system, or how errors in cluster size determination propagate into the free-energy landscape. The plateau in the free-energy landscape is a striking result that could also arise from artefacts in the measurement or analysis, such as the inability to track very large or very small clusters, or from the heterogeneity of the cellular environment being averaged over. Without a detailed description of the methodology and a rigorous error analysis, this central claim is not established.
    - **Why it matters** The conclusion that NELF condensation proceeds via non-classical nucleation with a flat energy landscape is a major conceptual advance, if true. It challenges the standard picture of a nucleation barrier. If the calculation is flawed or the interpretation is not unique, the central thesis of the paper is weakened. This claim needs to be supported by a robust and transparent analysis.
    - **Resolution test** The authors must provide a detailed description of the calculation of p_n, including the definition of cluster size, the treatment of clusters that move in and out of the focal plane, and the justification for the quasi-equilibrium assumption. They should also provide an error analysis, for example by bootstrapping or by simulating data with known ground truth, to show that the flat landscape is a real feature of the system and not an artefact of the analysis. A discussion of alternative interpretations of the flat landscape, such as the effect of active processes or molecular crowding, would also strengthen the claim.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness and data interpretation
    - **Claim pointer** The authors claim that "once a cluster reaches a critical size, it continues to grow into a larger condensate" and that the critical size is ~1500 NELFA molecules.
    - **Evidence pointer** Figure 2E, Supplementary Note 5, location not provided.
    - **Concern** The determination of a critical cluster size is a key quantitative result. The text states that a critical area of ~10 μm² translates to ~300 NELFA-GFP, and with a labelling ratio of 1 in 5, this gives ~1500 NELFA molecules. This calculation relies on the accuracy of the area-to-molecule-number calibration, which is described as coming from photobleaching step counting in fixed cells. The manuscript text does not provide the details of this calibration, such as the number of cells analysed, the variability in the density measurements, or how the "critical area" was precisely defined and measured. The statement that the critical size "might be different at higher expression levels" introduces uncertainty. The claim that growth is deterministic after reaching the critical size is a strong statement that needs to be supported by trajectory data showing that all clusters that reach this size go on to form condensates, and that no clusters below this size do.
    - **Why it matters** The existence of a well-defined critical size is a hallmark of a nucleation process. If the measurement is not robust, the claim of a nucleation barrier, even a non-classical one, is weakened. The quantitative value of ~1500 molecules is a specific and testable prediction that should be based on solid evidence.
    - **Resolution test** The authors should provide a clear description of how the critical area was determined from the trajectory data, including the criteria used to define a "condensate" versus a "cluster". They should present the distribution of critical sizes across all cells and show that the transition to fast growth is sharp. The calibration of area to molecule number should be described in detail, including the uncertainty in the density measurement and the labelling ratio.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific importance and data interpretation
    - **Claim pointer** The authors claim that "p38 kinase is required to form large clusters" and that it is "involved in the release of the blocking of the nucleation of NELF clusters in stressed cells".
    - **Evidence pointer** Figure 4, Supplementary Note 7, location not provided.
    - **Concern** The role of p38 kinase is presented as a key finding, but the evidence in the text is limited. The authors show that in the presence of a p38 inhibitor, clusters larger than 600 NELFA are not formed. This is a clear result. However, the claim that p38 is "required" is a strong statement. The text does not describe the specificity of the inhibitor, the concentration used, or whether off-target effects were ruled out. Furthermore, the mechanism by which p38 kinase "unblocks" nucleation is not explored. The observation that large clusters dissolve when stress is removed and the inhibitor is added is interesting, but the text notes high cell-to-cell variability and that half the cells died in one experiment. This suggests the system is under significant stress, and the observed effects could be indirect.
    - **Why it matters** Identifying a specific molecular player that regulates the nucleation barrier is a significant step. However, if the effect is not specific to p38 or is an indirect consequence of cell stress, the conclusion is overstated. A more detailed mechanistic understanding is needed to make the claim compelling.
    - **Resolution test** The authors should provide data on the specificity of the p38 inhibitor, perhaps by using a second, structurally distinct inhibitor or by knocking down p38. They should also investigate the downstream targets of p38 that could be involved in regulating NELF clustering. A more detailed time-course of the dissolution experiment, with careful monitoring of cell health, would help to rule out indirect effects.

    - **Concern ID** R1-M4
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical soundness
    - **Claim pointer** The authors claim that the combination of living-cell tracking and fixed-cell photobleaching step counting allows them to "quantify the number of NELFA-GFP molecules in dense regions with near single-molecule accuracy".
    - **Evidence pointer** Figure 2, Supplementary Note 6, location not provided.
    - **Concern** The accuracy of the molecular counting is fundamental to the quantitative claims of the paper. The manuscript text describes the process of photobleaching step counting in fixed cells but does not provide details on the validation of this method. For example, how was the efficiency of the photobleaching process determined? What is the error rate in step detection? How was the conversion from area in living cells to molecule number validated, given that the density in living cells might be different from that in fixed cells? The statement that the total number of NELFA proteins in the nucleus is "within a small multiplicative factor" of the mass spectrometry value is vague and does not constitute a rigorous validation.
    - **Why it matters** The entire quantitative framework of the paper, including the critical cluster size and the free-energy landscape, rests on the accuracy of the molecular counting. If the counting is not accurate, the derived quantities are not reliable.
    - **Resolution test** The authors should provide a detailed validation of their counting method, including control experiments with known numbers of molecules, an analysis of the error in step detection, and a comparison of the density measurements in fixed and living cells. The comparison with mass spectrometry should be presented more rigorously, with a clear statement of the uncertainty in both measurements.

- **Minor Comments**

    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability for nonspecialists
    - **Affected element** Introduction and Results
    - **Evidence pointer** Abstract, Results and Discussion, location not provided.
    - **Issue** The manuscript uses several technical terms and concepts (e.g., "non-classical nucleation", "flat free-energy landscape", "HILO microscope") without fully explaining them for a broader scientific audience. The distinction between "pre-condensate clusters" and "condensates" is made early on, but the physical basis for this distinction could be clearer.
    - **Required correction** Consider adding a brief, accessible explanation of classical nucleation theory and its limitations in the introduction. Define "HILO" and explain why it is advantageous for this type of imaging. Clarify the operational definition of a "pre-condensate cluster" versus a "condensate" in terms of size, dynamics, or response to inhibitors.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Materials and Methods
    - **Evidence pointer** Materials and Methods, location not provided.
    - **Issue** The Materials and Methods section is brief and refers to supplementary notes for many critical details. For example, the details of the machine-learning segmentation, the single-particle tracking algorithm, and the photobleaching step counting are all in the supplementary information. This makes it difficult to assess the methodology from the main text.
    - **Required correction** While it is common to put detailed methods in the supplementary information, the main text should provide a summary of the key parameters and steps. For example, state the number of cells analysed, the frame rate, the tracking parameters, and the key steps in the photobleaching analysis.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Data interpretation
    - **Affected element** Results and Discussion
    - **Evidence pointer** Figure 3A, location not provided.
    - **Issue** The authors state that the MSD analysis shows a range of diffusion behaviours, from free diffusion to sub-diffusion and directed diffusion. The text does not discuss the physical meaning of this heterogeneity or how it relates to the proposed model of cluster formation.
    - **Required correction** A brief discussion of the different types of diffusion observed and their potential physical origins (e.g., interactions with chromatin, active transport, crowding) would strengthen the interpretation.

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Scientific importance
    - **Affected element** Conclusion
    - **Evidence pointer** Conclusion, location not provided.
    - **Issue** The conclusion is somewhat brief and does not fully discuss the broader implications of the findings. For example, what does the presence of pre-condensate clusters in unstressed cells mean for our understanding of cellular organisation? How might the proposed "blocking" mechanism be regulated in different contexts?
    - **Required correction** Expand the conclusion to discuss the potential functional significance of the observed pre-condensate clusters and the proposed mechanism of nucleation blocking. This would increase the impact of the work.

## Risk / unsupported claims
- The claim of a "flat free-energy landscape" is unsupported without the detailed data and analysis in Figure 3E and Supplementary Note 7.
- The claim that p38 kinase is "required" for large cluster formation is not fully supported by the evidence described in the text, which shows an effect of a single inhibitor.
- The quantitative value of the critical nucleus size (~1500 NELFA molecules) is not fully supported without details on the calibration and validation of the counting method.
- The statement that the total number of NELFA proteins in the nucleus is "within a small multiplicative factor" of the mass spectrometry value is vague and does not constitute a rigorous validation.
- The generalisability of the findings beyond the specific NELF system and arsenic stress is not discussed and cannot be assessed from the provided material.