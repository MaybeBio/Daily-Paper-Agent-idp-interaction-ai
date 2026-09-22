## Review setup
- **Input scope** Full manuscript text, including abstract, main text, supplementary text, methods, and figure legends as provided.
- **Assessment boundary** The scientific claims, methodology, data interpretation, and presentation within the provided manuscript text. The review is based solely on the supplied material.
- **Shared manuscript claim summary** The authors present the first structure of the MAP kinase p38α in complex with its upstream activator MKK6, determined by cryo-EM. Through integration with MD simulations, HDX-MS, SAXS, and cellular assays, they propose a dynamic, multi-step mechanism for p38α activation, identify new interactions critical for activation, and demonstrate that the disordered N-terminus of MKK6 contributes to pathway specificity.
- **Visible evidence base** Cryo-EM density map and model (PDB-8A8M, EMD-15233), SAXS data, HDX-MS data, MD simulation trajectories, and cell-based reporter assays.
- **Missing materials affecting confidence** The manuscript text references several supplementary figures, tables, and movies (e.g., Fig. S1-S15, Tables S1-S5, Movies S1-S15) that are not fully described in the provided text. The HDX-MS data is only provided as a file name (Table S5). The full methods for the cellular reporter assay are referenced but not detailed. The specific details of the Bayesian/Maximum Entropy reweighting and the kinetic clustering are not fully described in the main text.

## Reviewer
- **Overall assessment** This manuscript addresses a fundamental and long-standing question in cell signaling: how a MAP2K specifically recognizes and phosphorylates its cognate MAPK. The work is ambitious, employing a multi-disciplinary approach to capture a transient kinase-kinase complex. The resulting cryo-EM structure, even at a moderate resolution of 4 Å, provides a valuable new framework for understanding MAPK activation. The integration with MD simulations and SAXS to model the dynamic ensemble is a strength, and the cellular assays provide functional validation for the identified interaction interfaces. However, the manuscript's central claims regarding the detailed activation mechanism and the role of the N-terminus in specificity are not fully established by the evidence presented. The moderate resolution of the cryo-EM map limits the confidence in the atomic details of the interface, and the functional data, while supportive, do not fully dissect the proposed mechanism. The manuscript is of high interest to the signal transduction community but requires substantial revision and additional analysis to fully support its conclusions.
- **Who would be interested in the results, and why** Researchers in the fields of signal transduction, kinase biology, structural biology, and drug discovery would be highly interested. The structure provides a template for understanding MAPK family specificity and a new avenue for designing allosteric inhibitors that disrupt the MKK6-p38α interaction, which is relevant to inflammatory and oncogenic signaling.
- **Major strengths**
    1.  The study tackles a technically challenging problem, the structural characterization of a transient kinase-kinase complex, and provides the first such structure for the p38 pathway.
    2.  The multi-disciplinary approach, combining cryo-EM, MD, HDX-MS, SAXS, and cell biology, is powerful and provides complementary lines of evidence.
    3.  The identification of the αG-helix of MKK6 as a key interaction hub with the p38α MAPK insert is a novel and significant finding with potential therapeutic implications.
    4.  The use of a high-affinity KIM from a pathogen protein to stabilize the complex is an elegant and effective strategy.
- **Major Concerns**

    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical Soundness
    - **Claim pointer** The authors claim to have generated "the first structure of p38α in complex with its MAP2K MKK6" and that this structure "defines the basis of MAPK specificity and activation."
    - **Evidence pointer** Figure 1, Figure 2, and associated text.
    - **Concern** The cryo-EM reconstruction is reported at a nominal resolution of 4 Å, with a local resolution range of 2.7-6.5 Å. At this resolution, while the overall fold and secondary structure elements can be reliably placed, the side-chain orientations and the precise nature of the interactions at the protein-protein interface cannot be unambiguously determined. The manuscript builds a detailed model of the interaction, including specific hydrogen bonds and a hydrophobic pocket, but the evidence presented does not demonstrate that the resolution in the interface region is sufficient to support these atomic-level claims. The validation of the model relies heavily on cross-correlation with the map, which may not be a stringent test for a model built into a moderate-resolution map.
    - **Why it matters** The central claims of the paper, including the specific interactions that drive specificity and the mechanism of activation, are based on the atomic model derived from this map. If the model is not accurately positioned, the mechanistic conclusions drawn from it are not reliable. The authors need to provide a more detailed local resolution analysis, particularly for the interface, and demonstrate that the key interactions are supported by the density.
    - **Resolution test** Provide a figure showing the local resolution of the map, with the interface region highlighted. Show representative density for the key interacting residues (e.g., MKK6 αG-helix and p38α MAPK insert) to demonstrate that the side-chain conformations are well-supported. A quantitative validation metric, such as a Q-score or a model-vs-map correlation for the interface residues, should be provided.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical Soundness
    - **Claim pointer** The authors state that "MD simulations confirm the complex is metastable and show how catalytically competent states can be formed" and that a "rotated complex might facilitate the phosphorylation of p38α T180."
    - **Evidence pointer** Figure 3, Figure 4, and associated text.
    - **Concern** The MD simulations are used to propose a detailed mechanism involving a rotated intermediate state that is critical for T180 phosphorylation. However, the manuscript does not provide sufficient evidence that this rotated state is significantly populated or functionally relevant. The simulations are initiated from the cryo-EM structure, and the observation of a rotated state in a few microseconds of simulation does not establish its physiological relevance. The functional validation relies on a single point mutation (K17A) that shows a modest 26% increase in activity, which is interpreted as evidence for the rotated state's role. This is a weak link. The authors need to provide more robust evidence, such as mutations that specifically stabilize or destabilize the rotated state and show a corresponding effect on T180 versus Y182 phosphorylation.
    - **Why it matters** The proposed activation mechanism is a central claim of the paper. If the rotated state is an artifact of the simulation setup or a minor population, the proposed mechanism for T180 phosphorylation is incorrect. The current evidence is not sufficient to distinguish between the proposed model and alternative mechanisms.
    - **Resolution test** Provide a more detailed analysis of the free energy landscape of the rotated state, including error bars. Design and test mutations that are predicted to specifically affect the stability of the rotated state and measure their effect on the phosphorylation of T180 and Y182 separately, not just on downstream reporter activity.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific Importance
    - **Claim pointer** The authors claim that the "MAP2K disordered N-termini determine pathway specificity" and that the length of the linker is "finely tuned for MAP kinase pairs."
    - **Evidence pointer** Figure 5 and associated text.
    - **Concern** The conclusion that the N-terminal linker length determines specificity is based on chimeric constructs where the MKK6 linker is replaced with those from other MAP2Ks. While this shows that the linker is important, it does not demonstrate that it is the primary determinant of specificity. The kinase core domains also differ between MAP2Ks and are likely to contribute to specificity. The experiments show a reduction in activity with different linkers, but this could be due to a general disruption of the complex rather than a specific loss of selectivity. The authors do not test whether the chimeric MKK6 constructs can now activate the MAPKs of the linker donor pathway.
    - **Why it matters** The claim of determining specificity is a major conclusion. The current experiments are not designed to directly test specificity, only activity. To support the claim, the authors need to show that swapping the linker changes the MAPK substrate preference of the kinase.
    - **Resolution test** Perform an in vitro kinase assay with the chimeric MKK6 constructs (e.g., MKK6 with MEK1 linker) against a panel of MAPKs (p38α, ERK1/2, JNK1/2) to demonstrate a change in substrate specificity. This would directly test the claim.

    - **Concern ID** R1-M4
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical Soundness
    - **Claim pointer** The authors state that "HDX-MS... confirmed that the engineering increases the population of the transphosphorylation-competent state of the complex and that its nature is consistent with that of the wild-type."
    - **Evidence pointer** Figure 2G, Figure S8, Table S5.
    - **Concern** The HDX-MS data is presented as a key validation that the engineered complex is representative of the wild-type interaction. However, the details of the experiment are not provided in the main text, and the data is only available as a supplementary file. The criteria for significance (15% and 1.5 Da) are stated, but the differential HDX data between the wild-type and engineered complexes is not shown. It is unclear if the protection patterns are truly similar or just broadly overlapping. The authors need to present a more direct comparison of the HDX data for the two complexes.
    - **Why it matters** The use of a chimeric KIM is a major experimental manipulation. The validity of the entire structural and mechanistic study depends on the assumption that the engineered complex faithfully mimics the native interaction. The HDX-MS data is the primary evidence for this, and it needs to be presented more rigorously.
    - **Resolution test** Provide a supplementary figure directly comparing the differential HDX data (e.g., a heatmap or a difference plot) for the wild-type MKK6-p38α complex and the MKK6 DD GRA-p38α complex. This will allow the reader to assess the similarity of the interaction surfaces.

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability for Nonspecialists
    - **Affected element** Abstract and Introduction
    - **Evidence pointer** Abstract, Main Text, first paragraph.
    - **Issue** The abstract and introduction are dense with jargon (e.g., "TxY motif," "DFG-in BLA-conformation," "αG-helix") that may be inaccessible to a broader scientific audience. The significance of the work, while clear to specialists, could be framed more generally.
    - **Required correction** Briefly explain the significance of the TxY motif and the conformational states in the introduction. The abstract could be slightly rephrased to emphasize the conceptual advance (e.g., "we show how a kinase specifically recognizes and activates its partner") before introducing the structural details.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Methods, MD simulations
    - **Evidence pointer** "MD simulations setup" section.
    - **Issue** The description of the MD simulations is missing key parameters for reproducibility. The specific version of the force field, water model, and the length of the simulations are mentioned, but the temperature and pressure coupling algorithms are not fully described. The method for generating the initial coordinates for the MKK6-p38α complex with the WT KIM is not fully detailed.
    - **Required correction** Provide a complete list of simulation parameters, including the specific algorithms used for temperature and pressure coupling, the time constants, and the method used to model the WT KIM.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Scientific Importance
    - **Affected element** Discussion
    - **Evidence pointer** Discussion section.
    - **Issue** The discussion on the therapeutic implications of targeting the dimerization interface is somewhat speculative. While the idea is interesting, the manuscript does not provide any evidence that disrupting this interface is feasible or would be therapeutically beneficial.
    - **Required correction** Soften the claims about therapeutic potential and instead focus on how this structure provides a new framework for understanding the biology of MAPK signaling, which could inform future drug discovery efforts.

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Methods, SAXS
    - **Evidence pointer** "SAXS" section.
    - **Issue** The SAXS data is used to validate the ensemble from MD simulations. However, the manuscript does not state the concentration of the complex used for the SAXS experiments, which is critical for assessing potential aggregation or concentration-dependent effects.
    - **Required correction** Add the protein concentration used for the SAXS measurements.

## Risk / unsupported claims
- The claim that the structure "defines the basis of MAPK specificity" is not fully supported. The structure shows the interaction between one specific MAP2K-MAPK pair. The specificity determinants are inferred from sequence conservation and chimeric constructs, but not directly demonstrated.
- The claim that the "rotated complex" is a key intermediate in the activation mechanism is not fully supported by the functional data. The K17A mutation has a modest effect, and its interpretation is speculative.
- The claim that the N-terminus of MKK6 "determines pathway specificity" is not directly tested. The experiments show that the linker is important for activity, but not that it determines which MAPK is targeted.
- The statement that the complex is "metastable" is based on MD simulations and SAXS, but the timescales of the simulations may not be sufficient to fully characterize the stability of the complex.
- The assertion that the p38α active site is "already in an active conformation" based on the presence of a nucleotide is not fully established, as the functional state of the kinase cannot be determined from a static structure alone.