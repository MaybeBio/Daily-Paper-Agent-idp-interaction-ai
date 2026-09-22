## Review setup
- **Input scope** Full manuscript text (main text, significance statement, methods summary, data availability)
- **Assessment boundary** Technical and scientific evaluation of the presented methods, results, and claims; no assessment of literature context beyond what is cited within the manuscript
- **Shared manuscript claim summary** The authors present a workflow combining high-pressure freezing, cryo-FIB milling, and cryo-electron tomography with a new computational pipeline (CATM) for identifying and orienting nucleosomes within biomolecular condensates. They apply this to reconstituted chromatin condensates and native chromatin in HeLa and NIH3T3 cells, reporting heterogeneous nucleosome packing in both systems and structural resolution of nucleosomes to 6.1-22 Å.
- **Visible evidence base** Main text figures referenced (Figs. 1-6), supplementary figures referenced (Figs. S1-S10), supplementary tables referenced (Table S1), EMDB accession codes, software repository URL
- **Missing materials affecting confidence** Supplementary figures and tables not provided; detailed methods in SI Appendix not provided; movies S1 and S2 not provided; template matching parameters and validation details only partially described in main text

## Reviewer
- **Overall assessment** This manuscript presents a technically ambitious and largely successful effort to address a significant challenge in condensate biology: preserving and analyzing the internal structure of biomolecular condensates at molecular resolution. The authors identify a critical artifact in conventional grid preparation methods and demonstrate that high-pressure freezing combined with cryo-FIB milling preserves condensate morphology. The CATM pipeline represents a genuine methodological advance over existing template matching approaches, with convincing validation on simulated data. The application to both reconstituted and native chromatin yields biologically interesting observations about heterogeneous nucleosome packing. However, several technical aspects require clarification and additional validation before the full strength of the claims can be assessed, particularly regarding the generalizability of the approach and the interpretation of the two nucleosome classes in NIH3T3 cells.

- **Who would be interested in the results, and why** Structural biologists studying chromatin organization, researchers investigating biomolecular condensates across cell biology, cryo-electron tomography method developers, and computational biologists working on particle identification in dense cellular environments. The methodological advances in sample preparation and image analysis will be of broad interest to the cryo-ET community, while the biological findings on chromatin packing heterogeneity speak to fundamental questions in genome organization.

- **Major strengths** The identification and systematic characterization of grid preparation artifacts is an important contribution that will benefit the field. The CATM pipeline addresses a real limitation of existing approaches and demonstrates clear improvement over standard template matching. The application to multiple systems (reconstituted, semi-native, and in situ) strengthens the generalizability claims. The resolution achieved for nucleosomes within dense condensates is impressive.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical validation
- **Claim pointer** The claim that CATM achieves F1 scores of 0.99 for position and 0.96 for orientation in simulated data, substantially surpassing standard template matching.
- **Evidence pointer** Figure 3D, SI Appendix Fig. S4 E-H
- **Concern** The validation of CATM is performed exclusively on simulated data. While the simulation appears to incorporate relevant parameters (noise level, missing wedge), the manuscript does not describe how faithfully the simulation represents the complexity of real condensate tomograms, including variations in ice thickness, charging artifacts, or the presence of non-nucleosomal material. The performance drop from simulated to real data is not quantified.
- **Why it matters** Without validation on experimental data with known ground truth (e.g., through correlative light and electron microscopy or through comparison with independent structural methods), the claimed accuracy of CATM on real tomograms remains uncertain. This is particularly important given that the biological conclusions about nucleosome organization depend critically on accurate position and orientation assignment.
- **Resolution test** Provide additional validation using experimental benchmarks, such as tomograms of purified nucleosome arrays with known organization, or cross-validation with an independent method (e.g., subtomogram averaging without orientation assignment, or comparison with cryo-EM structures of the same sample).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Biological interpretation
- **Claim pointer** The claim that the two classes of nucleosome structures observed in NIH3T3 cells represent nucleosomes with and without linker histone H1, based on the presence of density at the dyad axis in Class 1 and the ratio of the two classes (48.7%:51.3%).
- **Evidence pointer** Figure 6G, SI Appendix Fig. S10 and Table S1
- **Concern** The assignment of the Class 1 density to linker histone H1 is presented as a suggestion ("consistent with linker histone") but the subsequent analysis of mixing (ASC value) and the discussion treat this interpretation as sufficiently established to draw conclusions about H1 binding randomness. The resolution of 12 Å for Class 1 may be insufficient to unambiguously identify H1 density, and no orthogonal validation (e.g., immunolabeling, H1 depletion, or comparison with known H1-bound nucleosome structures) is provided.
- **Why it matters** The conclusion about random H1 binding is biologically significant and would be a notable finding. However, if the Class 1/Class 2 distinction is incorrect or if the density attributed to H1 has another origin, this conclusion would be unsupported. The manuscript should either provide additional evidence for the H1 assignment or temper the claims accordingly.
- **Resolution test** Provide orthogonal evidence for H1 assignment, such as comparison with a published H1-bound nucleosome structure at similar resolution, or analysis of nucleosomes from H1-depleted cells. Alternatively, revise the claims to clearly present the H1 assignment as speculative.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Methodological generalizability
- **Claim pointer** The claim that the workflow "should be extendable to other condensates composed of large, recognizable components."
- **Evidence pointer** Discussion section
- **Concern** The manuscript demonstrates the approach on chromatin, where the nucleosome is a large, well-characterized, and stereotypical structure. The extension to other condensates is plausible but not demonstrated. The authors do not discuss what minimum particle size, contrast, or structural regularity would be required for CATM to work, nor do they address potential complications from condensates with heterogeneous composition or less regular components.
- **Why it matters** The generalizability claim is prominent in the significance statement and discussion. If the approach is limited to condensates with large, rigid, and well-defined components, this should be stated more explicitly. Overstating generalizability could mislead researchers attempting to apply the method to less favorable systems.
- **Resolution test** Provide a more nuanced discussion of the applicability limits of the approach, or include a proof-of-principle application to a second condensate system with different characteristics.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative analysis
- **Claim pointer** The claim that the normalized entropy of valence distribution (0.74 ± 0.02 for reconstituted, 0.77 ± 0.01 for cellular chromatin) indicates similar heterogeneity in both systems.
- **Evidence pointer** Figures 5F and 6H-I
- **Concern** The comparison of entropy values between the two systems is presented as evidence of similar packing, but the manuscript does not report the number of tomograms, total nucleosome counts, or statistical methods used to compute the uncertainties. The entropy values are close, and it is unclear whether the difference is statistically significant or biologically meaningful. Additionally, the entropy metric depends on the chosen graph construction parameters (e.g., distance cutoff for edge definition), which are not described in the main text.
- **Why it matters** The similarity of packing between reconstituted and cellular chromatin is a central biological conclusion. If the comparison is not statistically robust or if the metric is sensitive to analysis parameters, this conclusion may not be well supported.
- **Resolution test** Report the number of independent tomograms and nucleosomes analyzed, describe the graph construction parameters, and provide a statistical comparison of the entropy distributions between the two systems.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1E and SI Appendix Fig. S1F
- **Evidence pointer** Figure 1E, SI Appendix Fig. S1F
- **Issue** The description of the orientational bias at the air-water interface is somewhat brief. The text states that nucleosomes at the AWI "displayed a marked orientational bias" with faces parallel to the interface, but the quantitative measure of this bias (e.g., angular distribution plots) is only in the supplementary figures.
- **Required correction** Consider adding a brief quantitative statement in the main text (e.g., the fraction of nucleosomes within a certain angular range of the interface normal) to make the strength of the bias clear without requiring the reader to consult the SI.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** CATM algorithm description
- **Evidence pointer** Figure 3C, SI Appendix Fig. S5
- **Issue** The description of the CATM algorithm in the main text is brief. The distinction between CATM and standard template matching is clear conceptually, but the specific implementation details (e.g., how the steric clash detection is performed, how the alternative orientations are generated and scored) are only in the SI.
- **Required correction** Provide a slightly more detailed description of the algorithm in the main text, or at minimum a pseudocode outline, to make the method accessible to readers who may not consult the SI.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Resolution claims
- **Evidence pointer** Figure 4C, Figure 6C, Figure 6G, Table S1
- **Issue** The resolution values (6.1 Å, 12 Å, 22 Å) are reported without confidence intervals or a description of the gold-standard FSC criterion used. It is also unclear how many particles contributed to each reconstruction beyond the total numbers given.
- **Required correction** Report the FSC cutoff used, and if possible, provide a resolution estimate with uncertainty or a resolution range across the different reconstructions.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Self-wicking" method
- **Evidence pointer** Figure 1A, SI Appendix Fig. S1D-E
- **Issue** The term "self-wicking" is used without a brief explanation of the mechanism. Readers unfamiliar with this technique may not understand how it differs from blotting.
- **Required correction** Add a brief parenthetical explanation of the self-wicking mechanism when first introduced.

- **Technical failings that need to be addressed before the case is established** The primary technical concern is the lack of experimental validation for CATM accuracy on real tomograms (R1-M1). The simulation-based validation is necessary but not sufficient to establish the reliability of the method for biological interpretation. Additionally, the H1 assignment in NIH3T3 cells (R1-M2) requires orthogonal support or more cautious interpretation. The statistical robustness of the entropy comparison (R1-M4) needs to be established.

- **Assessment against Nature-style criteria** 
  - **Originality**: The combination of HPF, cryo-FIB milling, and a new computational pipeline for particle identification in dense condensates is novel. The systematic demonstration of grid preparation artifacts is an important contribution.
  - **Scientific importance**: The work addresses a fundamental gap in condensate biology: the internal structure of condensates at molecular resolution. The findings on nucleosome packing heterogeneity have implications for understanding chromatin organization and condensate biophysics.
  - **Interdisciplinary readership**: The work bridges structural biology, cell biology, and computational methods. The methodological advances will interest cryo-ET practitioners, while the biological findings speak to a broader cell biology audience.
  - **Technical soundness**: The experimental design is generally sound, with appropriate controls (e.g., comparison of preparation methods). The computational validation on simulated data is thorough, but the lack of experimental validation is a gap. The resolution achieved is credible given the number of particles.
  - **Readability for nonspecialists**: The manuscript is clearly written and the significance statement is accessible. However, some technical sections (e.g., CATM description) may be challenging for readers without cryo-ET or computational background. The figures appear well-designed based on the text descriptions.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a significant methodological advance and biologically interesting findings, but the lack of experimental validation for CATM and the tentative H1 assignment need to be addressed before the full strength of the claims can be accepted.

## Risk / unsupported claims
- The claim that the two nucleosome classes in NIH3T3 cells represent H1-bound and H1-free nucleosomes is not fully supported by the evidence presented; the density at the dyad axis is suggestive but not conclusive at 12 Å resolution.
- The claim that the workflow "should be extendable to other condensates" is plausible but not demonstrated and may overstate the generalizability.
- The comparison of packing heterogeneity between reconstituted and cellular chromatin relies on an entropy metric whose statistical robustness is not fully established.
- The statement that "the overall density of HPF condensates was intermediate between blotted samples and wicked samples" is presented without quantitative density measurements in the main text.
- The claim that the random orientation distribution of nucleosomes in native chromatin indicates that "higher-order organization of chromatin may not be strongly influenced by neighboring cellular structures" is an interpretation that extends beyond the direct evidence.