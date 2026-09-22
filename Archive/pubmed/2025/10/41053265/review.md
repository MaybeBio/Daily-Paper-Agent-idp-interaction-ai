## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, conclusions, methods, and figure captions. Supplementary information referenced but not provided.
- **Assessment boundary** Scientific content, methodological soundness, interpretation of results, and alignment with claims. Not assessed: editorial quality, formatting, or literature completeness beyond what is visible.
- **Shared manuscript claim summary** The authors propose that transient non-local interactions between regions distant in the sequence of the intrinsically disordered measles virus NTAIL domain dominate its conformational dynamics. They combine photo-induced electron transfer (PET) experiments, coarse-grained and all-atom simulations, and co-evolutionary analysis to identify specific interactions that stabilize distinct conformational states, and they propose mechanisms by which these interactions regulate binding to the phosphoprotein and thus viral transcription and replication.
- **Visible evidence base** PET relaxation times under three conditions (reference, high salt, low pH); CD spectra at two pH values; coarse-grained simulations with salt and pH variation; all-atom simulations with two force fields validated against SAXS, CD, and NMR; free-energy landscape; contact probability maps; co-evolutionary analysis (results partially shown).
- **Missing materials affecting confidence** Supplementary figures and tables (S1–S28), full co-evolutionary results, simulation parameter details, and raw data files were not provided. These are essential for verifying several quantitative claims.

## Reviewer
- **Overall assessment** This manuscript presents a technically sophisticated and multi-pronged investigation of an intrinsically disordered protein domain. The combination of experiment, simulation, and evolutionary analysis is commendable and appropriate for the question. The central claim, that non-local interactions dominate NTAIL dynamics, is plausible and supported by the convergence of several independent lines of evidence. However, the strength of the conclusions is limited by the small number of PET probe positions, the reliance on a single simulation force field for the key mechanistic claims, and the absence of direct functional validation. The manuscript is well written and the figures are informative, but several quantitative claims require additional scrutiny and the presentation of uncertainties.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, particularly those involved in viral replication complexes. The work will also interest biophysicists developing and applying combined experimental-simulation approaches to disordered systems, and virologists interested in the molecular mechanisms of paramyxovirus transcription and replication. The methodological framework, especially the use of PET to probe non-local interactions, may be of broader interest to the IDP community.
- **Major strengths**
  1. The combination of multiple orthogonal techniques (PET, CD, CG and all-atom simulations, co-evolution) to address a single question is a significant strength and increases confidence in the conclusions.
  2. The identification of specific conformational states with distinct interaction patterns, and the correlation of these states with PET observables, provides a mechanistic and testable model.
  3. The careful validation of force fields against multiple independent experimental datasets (SAXS, CD, NMR) is exemplary and addresses a common weakness in IDP simulations.
  4. The proposal of concrete, biologically plausible mechanisms linking intramolecular interactions to polymerase function adds significance and provides a framework for future studies.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the all-atom simulations "accurately describe the NTAIL dynamics causing the C3W2/C4W2 dynamic heterogeneity" and that the free-energy landscape reveals four distinct conformational states.
- **Evidence pointer** Results section "Non-local NTAIL interactions explain dynamic heterogeneity"; Figure 3; Figure 4
- **Concern** The central mechanistic conclusion rests on the all-atom simulations with the CHARMM36m force field. While the force field was validated against ensemble-averaged properties (SAXS Rg, CD helicity, NMR chemical shifts), the key claim is about dynamics and specific transient interactions. The uncertainty on the simulated C3W2 relaxation time is very large (5.3 ± 3.3 μs), and the manuscript does not demonstrate that the specific interaction clusters identified in Figure 4 are robust to force field choice, simulation length, or analysis methodology. The claim that the simulations "accurately describe" the dynamics is therefore not fully established.
- **Why it matters** The entire mechanistic interpretation, including the proposed regulatory role of region B, depends on the reliability of the simulated conformational states and their interconversion kinetics. If the specific interactions are artifacts of the force field or insufficient sampling, the biological conclusions are unsupported.
- **Resolution test** The authors should demonstrate that the four conformational states and their relative populations are reproducible across at least two independent force fields and across multiple independent simulation replicas with converged sampling. Additionally, the uncertainty on the simulated relaxation times should be propagated into the comparison with experiment, and the manuscript should explicitly state whether the differences between C3W2 and C4W2 are statistically significant given the simulation uncertainties.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "increasing the salt concentration from 150 mM to 500 mM results in a τCW decrease from 7.6 μs to 5.8 μs for C3W2, and an increase from 3.2 μs to 3.9 μs for C3W1, bringing both data points close to the homopolymer curve."
- **Evidence pointer** Results section "Charged amino acids partially account for NTAIL dynamic heterogeneity"; Figure 1D
- **Concern** The interpretation of the salt dependence relies on the assumption that the observed changes in τCW are due to changes in protein conformation and dynamics, and not due to direct effects of salt on the PET process itself. While the authors address pH effects on electron transfer efficiency, they do not report a similar control experiment for salt concentration. High salt concentrations can affect the triplet state lifetime, the electron transfer rate, or the quenching mechanism independently of protein conformation.
- **Why it matters** If the salt-induced changes in τCW are partly or wholly due to non-conformational effects, the conclusion that electrostatic interactions between charged residues are a major contributor to the observed dynamic heterogeneity would be weakened.
- **Resolution test** The authors should perform a bimolecular quenching study (as done for pH) at high salt concentration, using NATA and free cysteine, to demonstrate that the electron transfer efficiency is unchanged. Alternatively, they should provide a quantitative correction for any salt-dependent effects on the PET rate.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors propose that "non-local interactions may be extended to other IDPs, where non-local intra-protein interactions affect the conformational preferences of intermolecular binding sites."
- **Evidence pointer** Abstract; Discussion
- **Concern** The generalizability of the findings to other IDPs is asserted but not critically examined. The authors do not discuss what sequence features or physicochemical properties of NTAIL make it particularly prone to such non-local interactions, nor do they compare their findings to other IDP systems where non-local interactions have been studied. The claim of generalizability is therefore speculative.
- **Why it matters** The broader significance of the work, and its appeal to a wide readership, depends on the extent to which the findings can inform our understanding of other IDPs. Without a more nuanced discussion of generalizability, the significance may be overstated.
- **Resolution test** The authors should either temper the claim of generalizability or provide a more detailed discussion of the conditions under which such non-local interactions are likely to be important, drawing on existing literature on other IDP systems.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The co-evolutionary analysis "independently shows that correlated mutations across regions were only found between regions B and D."
- **Evidence pointer** Results section "Functional relevance of non-local interactions is supported by co-evolutionary analysis"; Figure S28
- **Concern** The co-evolutionary analysis is presented as a key independent line of evidence, but the results are only briefly described and the full details are relegated to the supplementary material. The number of sequences, the alignment quality, the significance thresholds, and the specific pairs identified are not presented in the main text. The claim that correlations are "only found between regions B and D" is strong and requires a clear demonstration that the analysis had sufficient power to detect correlations elsewhere.
- **Why it matters** The co-evolutionary analysis is used to support the functional relevance of the identified interactions. If the analysis is underpowered or the thresholds are not well justified, the conclusion that these specific interactions are evolutionarily conserved is not robust.
- **Resolution test** The authors should present the key co-evolutionary results in the main text, including the number of aligned sequences, the significance threshold used, and a clear visualization of the top-scoring pairs. They should also discuss the potential for false negatives in their analysis.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and presentation
- **Affected element** Figure 1D
- **Evidence pointer** Figure 1D
- **Issue** The error bars on the experimental τCW values are not defined in the figure caption. It is unclear whether they represent standard deviations, standard errors, or confidence intervals from the global fitting procedure.
- **Required correction** Define the error bars in the figure caption and state the number of independent measurements.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, "Coarse-grained MDs"
- **Evidence pointer** Methods section
- **Issue** The description of the coarse-grained model states that it was "optimized using the experimental radius of gyration of NTAIL." It is not clear whether this optimization was performed for NTAIL specifically or whether the original HPS parameters were used. If the model was re-parameterized, the details of the optimization procedure are missing.
- **Required correction** Clarify whether the HPS model parameters were adjusted for NTAIL and, if so, provide the details of the optimization procedure.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity and presentation
- **Affected element** Discussion, "Tether shortening"
- **Evidence pointer** Discussion section
- **Issue** The discussion of the "cartwheeling" mechanism and the proposed role of region B in polymerase progression is highly speculative and goes beyond the data presented. While such speculation is acceptable in a discussion, it should be clearly labeled as a hypothesis.
- **Required correction** Explicitly label the proposed mechanisms as speculative hypotheses that require direct testing.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, "PET reveals the heteropolymeric nature of NTAIL dynamics"
- **Evidence pointer** Results section
- **Issue** The manuscript states that "the general trend of the estimated τCW at physiological pH follows the simple homopolymer scaling." The quantitative measure of "following" is not defined. A statistical test or a quantitative metric (e.g., R² value) for the agreement with the homopolymer model would strengthen this claim.
- **Required correction** Provide a quantitative measure of the agreement between the experimental data and the homopolymer model prediction.

## Risk / unsupported claims
- The claim that the all-atom simulations "accurately describe" the dynamics causing the C3W2/C4W2 heterogeneity is not fully supported given the large uncertainties and the lack of cross-force-field validation.
- The claim that non-local interactions "dominate" NTAIL dynamics is supported for the C-terminal region but may be overstated for the entire domain, given the limited number of probe positions.
- The proposed mechanisms for the functional role of non-local interactions in polymerase recruitment and progression are speculative and not directly tested.
- The generalizability of the findings to other IDPs is asserted without sufficient comparative analysis.
- The co-evolutionary analysis is claimed to "independently" support the functional relevance, but the full details and power of the analysis are not presented in the main text, making this claim difficult to evaluate.