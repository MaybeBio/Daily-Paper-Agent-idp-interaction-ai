## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, conclusions, acknowledgments)
- **Assessment boundary** Scientific and methodological soundness of the reported comparison between ABFE and MSM protocols for binding free energy calculations on an IDP-ligand system
- **Shared manuscript claim summary** The authors compare alchemical absolute binding free energy (ABFE) calculations and Markov-State Modeling (MSM) protocols to estimate the binding free energy of the small molecule 10058-F4 to a disordered c-Myc peptide. ABFE results are sensitive to reference structure choice and yield weak or unfavorable binding estimates, while MSM results produce more reproducible estimates consistent with weak mM binding affinities reported in the literature.
- **Visible evidence base** Abstract, full methods section, results and conclusions sections, figure captions referenced in text, supplementary figure/table references
- **Missing materials affecting confidence** Supplementary figures and tables (Figures S1–S15, Tables S1–S4) are referenced but not provided; no raw simulation data, convergence diagnostics, or error analysis details beyond standard error of the mean; no experimental binding data for direct comparison beyond literature values cited

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question: whether established alchemical free energy methods can be applied to intrinsically disordered proteins, where the bound state is conformationally heterogeneous. The comparison between ABFE and MSM approaches is conceptually valuable and the system choice (c-Myc/10058-F4) is well justified by prior experimental and computational work. However, the manuscript has several significant methodological weaknesses that limit the strength of its conclusions. The ABFE protocol appears to be applied in a relatively standard manner without adequate consideration of the conformational heterogeneity problem that the authors themselves identify as central. The MSM construction relies on simple distance metrics and a two-state coarse-graining that may not capture the complexity of the binding process. The comparison between methods is not entirely fair, as the ABFE calculations use a single reference structure while the MSM approach naturally samples the full ensemble. The reported binding free energies from both methods deviate substantially from experimental values, and the authors do not provide sufficient analysis to determine whether these deviations reflect force field inaccuracies, methodological limitations, or genuine physical features of the system. The manuscript would benefit from more rigorous convergence assessment, a clearer treatment of the standard state correction, and a more nuanced discussion of what the computed values can and cannot tell us about the binding process.

- **Who would be interested in the results, and why** Computational chemists and biophysicists working on binding free energy calculations, particularly those interested in extending established methodologies to challenging systems such as IDPs. Researchers studying c-Myc as a drug target would also find the system-specific results relevant. The methodological comparison is of general interest to the molecular simulation community, as the question of how to compute binding affinities for conformationally heterogeneous systems is widely recognized as an open problem.

- **Major strengths** The manuscript addresses a genuinely important and under-explored question in computational drug discovery. The choice of a well-characterized IDP-ligand system with available experimental data provides a meaningful test case. The comparison between two fundamentally different approaches (alchemical and kinetic-based) is conceptually informative. The use of multiple force fields for the MSM calculations adds robustness to that part of the study. The authors are appropriately cautious in their conclusions and acknowledge the limitations of their approach.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The ABFE protocol yields binding free energy estimates of −0.8 ± 0.2 kcal/mol (GAFF2) and −1.3 ± 0.2 kcal/mol (custom parameters), which the authors describe as "only a very weak affinity" that "contrasts with the previously reported experimental results."
- **Evidence pointer** Results section, "Binding Free Energies from the Alchemical ABFE Protocol"; Figure 1; Table S1 (referenced)
- **Concern** The ABFE calculations are performed using a single reference structure as the starting point, with no apparent attempt to account for the conformational heterogeneity of the IDP. The authors acknowledge this limitation in the conclusions but do not address it in the methods or results. The sensitivity of ABFE results to the choice of reference structure is demonstrated by the difference between the two sets of calculations (using the Hammoudeh pose versus the most representative pose from 500 ns MD), yet the authors do not systematically explore this dependence. The manuscript does not report convergence diagnostics for the alchemical calculations, such as overlap between adjacent windows, hysteresis between forward and reverse directions, or the statistical efficiency of the free energy estimate.
- **Why it matters** The central claim of the manuscript is that ABFE methods are problematic for IDP systems because of conformational heterogeneity. However, the ABFE protocol as implemented does not appear to have been designed to address this challenge. Without convergence assessment and a systematic exploration of reference structure dependence, the reader cannot determine whether the poor ABFE results reflect a fundamental limitation of the method or simply an incomplete application of it. The comparison with MSM results is therefore potentially unfair.
- **Resolution test** The authors should provide convergence diagnostics for the alchemical calculations, report the dependence of ABFE results on the choice of reference structure (ideally using multiple starting conformations), and demonstrate that the alchemical protocol is fully converged before drawing conclusions about method applicability.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The MSM-derived binding free energies are reported as "more reproducible" and "consistent with weak mM binding affinities," with the most negative estimate of −2.7 kcal/mol (approximately 10 mM Kd) obtained with AmberIDP/GAFF2.
- **Evidence pointer** Results section, "Binding Free Energies from Markov-State Modeling Protocols"; Figure 2; Tables S2 and S4 (referenced)
- **Concern** The MSM construction relies on simple distance-based metrics between the ligand and protein Cα atoms. The authors acknowledge that tICA retained ten out of eleven dimensions for the first metric, which suggests that the dimensionality reduction was not effective. The two-state coarse-graining using PCCA++ may not adequately capture the binding process, particularly for a system where the bound state is described as "fuzzy" and conformationally heterogeneous. The standard state correction in eq 1 depends on the definition of the bound volume, which is estimated from the average distance between ligand and protein centers of mass. This is a crude approximation that could introduce significant error. The authors do not report uncertainties on the MSM-derived free energies beyond the spread across metrics and force fields.
- **Why it matters** The claim that MSM methods are more suitable than ABFE for IDP systems rests on the reliability of the MSM-derived binding free energies. If the MSM construction is not rigorously validated, the comparison is not meaningful. The sensitivity of the results to the choice of metric, the number of clusters, the lag time, and the definition of bound volume should be systematically explored. The authors note deviations in the Chapman-Kolmogorov tests, indicating that the models are only approximately Markovian, but do not discuss the implications of this for the reliability of the computed free energies.
- **Resolution test** The authors should validate the MSM construction more thoroughly, including a systematic exploration of the dependence of results on the number of clusters, lag time, and feature choice. The bound volume definition should be justified more carefully, and uncertainties on the reported free energies should be provided. The implications of the approximate Markovianity for the reliability of the results should be discussed.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors state that "this study suggests that MSM protocols may have an advantage over ABFE protocols to characterize the binding energies of ligands to IDPs owing to the 'fuzziness' of the bound state."
- **Evidence pointer** Conclusions section
- **Concern** The manuscript compares two methods on a single system with a single ligand. The conclusion that MSM methods "may have an advantage" over ABFE is based on limited evidence. The ABFE results are sensitive to the choice of reference structure, but this is a known limitation that could potentially be addressed by averaging over multiple starting conformations. The MSM results are more consistent across force fields, but the absolute values still deviate from experimental measurements. The authors do not provide a clear framework for when one method should be preferred over the other, nor do they discuss the computational cost of each approach in sufficient detail.
- **Why it matters** The broader claim of the manuscript is that the field needs to develop new approaches for IDP-ligand binding free energy calculations. This is an important message, but it requires stronger evidence than a single system comparison. The authors should either temper their conclusions or provide additional evidence, such as a second system or a more systematic analysis of the factors that determine method performance.
- **Resolution test** The authors should either expand the study to include additional IDP-ligand systems or provide a more detailed analysis of why the observed differences between methods are expected to generalize. Alternatively, the conclusions should be revised to be more cautious about the general applicability of the findings.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors report kon values of approximately 10^8 s^-1 M^-1, which they note are "close to diffusion limit," and koff values that are "at the upper range of what is experimentally observed."
- **Evidence pointer** Results section, "Binding Free Energies from Markov-State Modeling Protocols"; Figure 3; Table S4 (referenced)
- **Concern** The kinetic rate constants are derived from MFPTs calculated from the MSM. The conversion from MFPT to rate constants assumes first-order kinetics and requires the concentration of the ligand in the simulation box. The authors state that the ligand concentration is 0.02 M given the box dimensions, but the relationship between this concentration and the standard state concentration used in the free energy calculation is not clearly explained. The physical interpretation of the rate constants for a system where the bound state is described as "fuzzy" and involves multiple binding modes is not straightforward.
- **Why it matters** The kinetic analysis is presented as an additional benefit of the MSM approach, but the reliability of the derived rate constants is not established. If the rate constants are not physically meaningful, their inclusion may detract from the main message of the manuscript.
- **Resolution test** The authors should provide a more careful derivation of the rate constants from the MFPTs, including a discussion of the assumptions involved and the sensitivity of the results to the choice of bound state definition. The relationship between the simulation box concentration and the standard state should be clarified.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraphs 1-3
- **Issue** The introduction provides a thorough review of the challenges of IDP drug discovery and the limitations of current computational approaches, but the transition from the general discussion of IC50/Ki discrepancies to the specific focus on computational methods is abrupt. The discussion of Cheng-Prusoff equations and assay variability, while relevant, could be streamlined to maintain focus on the computational methodology.
- **Required correction** Consider condensing the discussion of experimental assay variability and focusing more directly on the computational challenges that motivate the study.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, MD Simulations section
- **Evidence pointer** Methods, "MD Simulations of c-Myc/Ligand Complexes"
- **Issue** The description of the equilibration protocol for the first set of simulations mentions energy minimization with 1000 steps of steepest gradients, followed by NVT and NPT equilibration, but the total equilibration time and the criteria for judging equilibration are not stated. For the second set of simulations, the equilibration protocol is described as "similar" without specifying the exact parameters.
- **Required correction** Provide complete details of the equilibration protocol for both sets of simulations, including the duration of each phase and the criteria used to assess equilibration.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, Markov-State Modeling Protocol section
- **Evidence pointer** Methods, "Markov-State Modeling protocol"
- **Issue** The choice of 75 clusters for k-means clustering is stated without justification. The sensitivity of the MSM results to the number of clusters is not explored. The lag time of 200 ps is chosen based on the ITS plots, but the criteria for this choice are not explicitly stated.
- **Required correction** Provide a brief justification for the number of clusters and the lag time choice, and ideally include a sensitivity analysis in the Supporting Information.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Conclusions
- **Evidence pointer** Conclusions section
- **Issue** The conclusions mention that "further efforts are required to assess the ability of a range of modern protein, ligand and water force fields to rank-order by binding affinity data sets of diverse ligands for IDPs," but the manuscript does not provide a clear roadmap for how such efforts should be structured.
- **Required correction** Consider adding a brief discussion of what specific force field combinations and validation strategies would be most informative for future studies.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Results, Binding Free Energies from Markov-State Modeling Protocols section
- **Evidence pointer** Results, "Binding Free Energies from Markov-State Modeling Protocols"
- **Issue** The description of the three metrics used for MSM construction is somewhat unclear. The authors state that the first metric involves 11 distances between the nitrogen atom of the ligand and the Cα atoms of each amino acid, but the exact definition of the "nitrogen atom of the ligand" is not specified (which nitrogen atom in 10058-F4?). The second and third metrics are described as using the "shortest distance" but the reference atoms are not clearly defined.
- **Required correction** Provide a clear definition of the atoms used for each metric, possibly with a figure or a more detailed textual description.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, Binding Free Energies from Markov-State Modeling Protocols section
- **Evidence pointer** Results, "Binding Free Energies from Markov-State Modeling Protocols"; Figure 4
- **Issue** The analysis of residue-specific contacts (Figure 4) is based on 1000 snapshots extracted from the bound state. The authors do not specify how these snapshots were selected (e.g., evenly spaced in time, random, or based on some other criterion) or whether the results are converged with respect to the number of snapshots.
- **Required correction** Provide details on the snapshot selection procedure and ideally include a convergence analysis for the contact statistics.

## Risk / unsupported claims
- The claim that ABFE results are "sensitive to the choice of reference structure" is supported by the data presented, but the systematic exploration of this sensitivity is not provided.
- The claim that MSM results are "more reproducible" than ABFE results is supported by the spread of values across force fields and metrics, but the statistical significance of this difference is not established.
- The statement that the computed binding free energies are "consistent with weak mM binding affinities" is based on comparison with literature values for other IDP-ligand systems, not direct experimental measurements for this specific system.
- The claim that the MSM-derived conformational ensembles are "consistent with" a previous metadynamics study is based on qualitative comparison and is not quantitatively validated.
- The suggestion that MSM protocols "may have an advantage" over ABFE for IDP systems is presented as a conclusion but is not supported by a systematic comparison across multiple systems or conditions.
- The kinetic rate constants (kon and koff) are reported without uncertainty estimates, and their physical interpretation for a system with a "fuzzy" bound state is not fully established.
- The statement that "the picture that emerges is one of weak affinity and very fast binding/unbinding kinetics" is based on the computed values, but the relationship between these computed values and experimentally observable kinetics is not discussed in detail.