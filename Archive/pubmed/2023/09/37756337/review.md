## Review setup
- **Input scope** Full manuscript text (main text, methods, significance statement) as provided
- **Assessment boundary** Scientific content, methodological soundness, and claims as presented in the provided text; no supplementary figures, tables, or movies were available for direct inspection
- **Shared manuscript claim summary** The authors report that the N-terminal half of the Aux/IAA protein AXR3, despite being intrinsically disordered, exhibits a high population of the cis conformation at the key degron residue Pro87, and that molecular dynamics simulations reveal two dominant partially structured conformational clusters. They further propose that these conformers engage differently with the TIR1 auxin coreceptor and that the binding interface extends beyond the crystallographically defined degron peptide.
- **Visible evidence base** NMR backbone assignments, HSQC-based cis/trans ratio measurements, CD spectroscopy, RXSGLD molecular dynamics simulations, chemical shift back-calculation, coarse-grained simulations of the TIR1 complex, and NMR titration data
- **Missing materials affecting confidence** Supplementary figures (S1–S15), supplementary tables (S1–S5), movies (S1–S2), and the deposited BMRB data were not available for inspection. The full NMR assignment tables and detailed simulation parameters could not be independently verified.

## Reviewer
- **Overall assessment** This manuscript presents a substantial and methodologically ambitious investigation of conformational behavior in an intrinsically disordered region of a plant signaling protein. The combination of NMR spectroscopy and advanced molecular dynamics simulations is appropriate and the central observation, a near 1:1 cis:trans ratio at Pro87 in the unbound state, is striking and potentially significant for understanding auxin perception. However, the manuscript would be strengthened by more direct experimental validation of the simulated conformational clusters, clearer presentation of the statistical significance of the clustering results, and a more critical discussion of the limitations of the computational approaches used. The claims regarding the functional implications of conformational coexistence, while plausible, are somewhat speculative relative to the evidence presented.
- **Who would be interested in the results, and why** Plant biologists studying auxin signaling, particularly those focused on Aux/IAA function and degradation mechanisms. Structural biologists and biophysicists interested in intrinsically disordered proteins and their conformational landscapes. Computational chemists developing and applying enhanced sampling methods for disordered systems. The finding that a nominally disordered protein maintains a high cis-proline population and exhibits discrete conformational substates has broader relevance to the understanding of coupled folding and binding in signaling contexts.
- **Major strengths** The combination of multiple complementary techniques (NMR, CD, MD simulations, coarse-grained modeling) provides a multifaceted view of the system. The observation of a near 1:1 cis:trans ratio at Pro87 is quantitatively striking and well supported by the NMR data presented. The use of replica exchange with self-guided Langevin dynamics is an appropriate and sophisticated choice for sampling disordered protein conformations. The comparison between simulated and experimentally measured chemical shifts provides a valuable validation step. The identification of two dominant conformational clusters with distinct TIR1 binding modes is an interesting hypothesis-generating result.
- **Major Concerns** The following concerns are detailed below.
- **Minor Comments** The following comments are detailed below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (validation of simulated clusters), R1-M2 (statistical robustness of clustering), R1-M3 (force field limitations)
- **Assessment against Nature-style criteria** **Originality:** The work is original in its specific focus on conformational substates within an Aux/IAA disordered region and the high cis-proline population. The concept of conformational coexistence in IDPs is not new, but its application to auxin coreceptors is novel. **Scientific importance:** The findings have potential importance for understanding auxin perception mechanisms, but the direct functional consequences of the observed conformational heterogeneity remain to be demonstrated. The work is more likely to be of strong interest to the plant biology and IDP biophysics communities than to a broad general audience. **Interdisciplinary readership:** The work bridges plant biology, structural biology, and computational chemistry, which could attract readers from multiple disciplines, but the specialized nature of both the system and the methods may limit broader appeal. **Technical soundness:** The NMR methodology appears sound and the simulation approach is state-of-the-art. However, the validation of the simulated conformational clusters against experimental data is indirect and the statistical robustness of the clustering is not fully established. **Readability for nonspecialists:** The manuscript is generally clearly written, but the methods section assumes substantial familiarity with both NMR spectroscopy and advanced MD simulation techniques. The significance statement is accessible, but the main text would benefit from additional context for readers outside the immediate field.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the experimental validation of the simulated conformational clusters and the statistical robustness of the clustering analysis.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The manuscript claims that the N-terminal half of AXR3 exists as two dominant, distinct conformational clusters that together comprise approximately 91% of the simulated ensemble, and that these represent "partially structured conformations" with biological relevance.
- **Evidence pointer** Figure 3, Figure 4, SI Appendix Figures S7–S12
- **Concern** The identification of two dominant conformational clusters from the RXSGLD trajectory is a central result, yet the validation of these clusters against experimental data is indirect. The chemical shift back-calculation (Figure 6A) shows averaged values over the entire trajectory, which would not distinguish between a single broad ensemble and discrete substates. The comparison with NMR data is therefore not sufficient to establish that the specific clusters identified are experimentally meaningful. The authors should provide per-cluster chemical shift predictions and compare these to the experimental values, or use other experimental observables (e.g., RDCs, PREs, or SAXS data if available) that are sensitive to the presence of discrete conformational states. Without such validation, the claim that the two clusters represent real, populated states rather than artifacts of the simulation methodology or clustering algorithm is not fully supported.
- **Why it matters** The existence of discrete conformational substates with different TIR1 binding modes is a central claim of the paper and underpins the proposed model of auxin coreceptor function. If the clusters are not experimentally validated, the functional implications drawn from them are speculative.
- **Resolution test** Provide per-cluster back-calculated chemical shifts and show that they are consistent with the experimental NMR data. Alternatively, use experimental observables that are sensitive to conformational heterogeneity (e.g., RDCs measured in different alignment media, or paramagnetic relaxation enhancement data) to test the predicted cluster populations. If such data are not available, the authors should temper the claim that the clusters represent experimentally meaningful states.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the two largest clusters "have almost the same occupancy and comprise approximately 91% of all frames," implying a robust bimodal distribution of conformations.
- **Evidence pointer** Figure 3B, Methods section (SWRMSD description)
- **Concern** The statistical robustness of the clustering result is not established. The SWRMSD method is introduced in the Methods, but no information is provided about the sensitivity of the clustering to the choice of reference frame, the scoring weights, or the clustering algorithm parameters. It is unclear whether the two dominant clusters would emerge consistently across different simulation runs or with different analysis choices. Additionally, the manuscript does not report error bars or convergence metrics for the cluster populations. Given that the authors themselves note that IDP simulations are challenging due to low energy barriers, it is essential to demonstrate that the observed bimodality is not a sampling artifact.
- **Why it matters** The claim of two dominant, approximately equally populated conformational states is a quantitative result that underpins the proposed model. If the clustering is not robust, the specific structural models presented in Figure 4 may not be representative of the true ensemble.
- **Resolution test** Perform multiple independent RXSGLD simulations (or split the existing trajectory into independent blocks) and show that the same two clusters emerge with similar populations. Provide a convergence analysis of the cluster populations as a function of simulation time. Report the sensitivity of the clustering to the SWRMSD parameters and the clustering algorithm.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The manuscript uses the ff14SBonlysc force field with implicit solvent (GB model) for the RXSGLD simulations and the ff99SB force field with OPC water for the relaxation of full-length models.
- **Evidence pointer** Methods section (Molecular Dynamics Simulations)
- **Concern** The choice of force field and solvent model for IDP simulations is known to significantly influence the resulting conformational ensembles. The authors justify their choice of ff14SBonlysc with the GB model based on a previous study, but it is well established that implicit solvent models can bias IDP conformations toward overly compact or overly extended states. The use of different force fields for the RXSGLD simulations (ff14SBonlysc, implicit solvent) and the full-length model relaxation (ff99SB, explicit water) introduces an inconsistency that could affect the interpretation of the full-length models. The authors should discuss these limitations more explicitly and, ideally, validate their key findings with at least one additional force field or solvent model.
- **Why it matters** The conformational ensemble and the identified clusters may be force-field dependent. If the results are not robust to the choice of simulation parameters, the structural conclusions may not be reliable.
- **Resolution test** Repeat the RXSGLD simulations with an alternative force field (e.g., ff99SB-disp or a CHARMM36m-based parameter set) or with explicit solvent, and show that the key findings (high cis population, two dominant clusters) are reproduced. If this is not feasible, the authors should clearly acknowledge this limitation and temper the strength of their structural claims.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 2B
- **Evidence pointer** Figure 2B
- **Issue** The cis:trans ratio for the axr3-3 mutant is reported as approximately 1:2, but it is unclear whether this change is statistically significant given the error bars shown. The manuscript states that the V89G mutation "notable decrease" in cis population, but no statistical analysis is presented.
- **Required correction** Provide a statistical comparison (e.g., t-test or equivalent) between the wild-type and mutant cis:trans ratios, or clearly state the number of independent measurements and the uncertainty in the ratio determination.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion of functional implications
- **Evidence pointer** Discussion section
- **Issue** The manuscript suggests that the two conformational clusters may have different functional roles in auxin coreceptor assembly, but this is not developed in detail. The authors mention that the trans conformer can engage with TIR1 "in a different pose and substantially outside the pocket," but the functional consequences of this are not discussed.
- **Required correction** Expand the discussion to address the potential functional significance of the two binding modes, including how they might affect auxin sensitivity, degradation kinetics, or interactions with other coreceptor components.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section (SWRMSD)
- **Evidence pointer** Methods section
- **Issue** The description of the SWRMSD method is brief and the rationale for the specific scoring weights (0, 1, 4) is not explained. A reader unfamiliar with the method would have difficulty reproducing it.
- **Required correction** Provide a more detailed description of the SWRMSD method, including the rationale for the scoring scheme, and consider including a pseudocode or a reference to a more detailed description.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure 6
- **Evidence pointer** Figure 6
- **Issue** The comparison between simulated and experimental chemical shifts (Figure 6A vs 6B) is presented as supportive evidence, but the quantitative agreement is not assessed. It is unclear whether the differences between simulated and experimental values are within the expected accuracy of SHIFTX2 for IDPs.
- **Required correction** Provide a quantitative measure of the agreement (e.g., RMSD between predicted and experimental shifts) and discuss whether the level of agreement is consistent with the expected accuracy of the prediction method.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion of the LRT2 isomerase
- **Evidence pointer** Discussion section
- **Issue** The manuscript mentions the rice LRT2 isomerase but does not discuss the implications of its absence in Arabidopsis for the proposed model. If no isomerase is present in Arabidopsis, how is the cis:trans ratio regulated?
- **Required correction** Add a brief discussion of the potential mechanisms that might regulate the cis:trans ratio in Arabidopsis in the absence of a known isomerase, or explicitly state that this remains an open question.

## Risk / unsupported claims
- The claim that the two dominant conformational clusters represent biologically relevant states is not directly supported by experimental evidence; the chemical shift comparison is averaged over the entire ensemble and cannot distinguish discrete substates.
- The claim that the trans conformer engages with TIR1 "in a different pose and substantially outside the pocket" is based on simulation data that has not been experimentally validated.
- The statement that "to the best of our knowledge, no IDP in which the disorder is due to a glassy landscape with multiple semifolded structures has been characterized" is a strong claim that would require a thorough literature search to substantiate.
- The functional significance of the extended binding interface beyond residue K94 is inferred from NMR line broadening and simulation data, but the direct biological relevance is not demonstrated.
- The claim that the high cis population is "unusually high" relative to other IDPs is based on comparisons with published values, but the specific comparison set is not clearly defined.