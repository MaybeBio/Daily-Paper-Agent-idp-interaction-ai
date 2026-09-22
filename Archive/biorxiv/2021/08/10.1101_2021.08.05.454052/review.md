## Review setup

- **Input scope** Full manuscript text (abstract, introduction, results and discussion, conclusions, methods) without supplementary information or figures beyond those referenced in the text.
- **Assessment boundary** Scientific claims, methodological soundness, and internal consistency of the reported findings as presented in the supplied text. No assessment of data quality beyond what is described in the text.
- **Shared manuscript claim summary** The authors report that the small molecule AM-7209, but not Nutlin-3a, strongly prefers binding to an ordered conformation of the intrinsically disordered N-terminal lid region of MDM2, thereby shifting the disorder-to-order equilibrium toward the ordered state. This preference is quantified via calorimetric measurements (250-fold affinity loss upon lid truncation) and computational free energy calculations using an adaptive alchemical absolute binding free energy method.
- **Visible evidence base** Abstract, Introduction, Results and discussion (four subsections), Conclusions, Methods, Conflict of Interest, Acknowledgements. Referenced figures: Figure 1A, 1B, 2A-C, 3A-D, 4A-D, 5A-B, 6A-C. Referenced tables: Table S1-S3 (in SI, not provided). Referenced supplementary figures: Figure S1-S10 (not provided).
- **Missing materials affecting confidence** Supplementary Information (detailed protocols, convergence plots, additional data tables), all figures (only referenced, not shown), and the full Methods section for computational details. These are essential for verifying the technical soundness of the free energy calculations and the calorimetric analysis.

## Reviewer

- **Overall assessment** The manuscript addresses a timely and important question in molecular recognition, namely how small molecules can exploit disorder-to-order transitions in intrinsically disordered regions. The combination of calorimetry and advanced alchemical free energy calculations is ambitious and potentially impactful. However, the central quantitative claims, particularly the 250-fold affinity difference and the computed free energy preferences, cannot be fully evaluated from the supplied text alone. The adaptive sampling protocol is a potentially valuable methodological contribution, but its validation rests on comparisons to a "standard protocol" whose details are only partially described. The thermodynamic decomposition of the binding free energy into lid-state-specific contributions is conceptually appealing, but the statistical robustness of the computed differences (e.g., 3 kcal/mol preference) is not demonstrated in the text. The manuscript would benefit from clearer presentation of error estimates and convergence criteria for the key computational results.

- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, protein-ligand interactions, and structure-based drug design would find this work of interest. The demonstration that a drug-like molecule can selectively stabilize an ordered conformation of an IDR, and the quantitative framework for understanding such selectivity, could inform future efforts to target disordered regions in therapeutic contexts. The adaptive alchemical free energy method may also appeal to computational chemists developing more efficient binding free energy protocols.

- **Major strengths** The study addresses a biologically and therapeutically relevant problem with a combination of experimental and computational approaches. The calorimetric data provide a clear and striking phenotype (250-fold affinity difference) that motivates the computational analysis. The development of an adaptive sampling protocol for alchemical free energy calculations is a practical contribution that could reduce computational costs for similar systems. The authors are careful to note limitations of force fields for IDR simulations and provide a rationale for their choice.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "Calorimetric measurements revealed that truncation of the lid region of MDM2 increases the apparent dissociation constant of AM-7209 250-fold."
- **Evidence pointer** Figure 2A, Table S1 (location not provided for table)
- **Concern** The 250-fold affinity difference is a central experimental result, but the text does not provide the actual Kd values for both constructs, the number of replicates, or the error analysis beyond a stated "ca. 5±1 pM" for the full-length construct. The Kd for the truncated construct is not given. Without these details, the magnitude of the effect cannot be independently assessed.
- **Why it matters** This quantitative claim underpins the entire narrative that AM-7209 specifically engages the lid region. If the affinity difference is smaller or associated with larger uncertainty than implied, the subsequent computational analysis loses its experimental anchor.
- **Resolution test** Provide the measured Kd values (with standard errors) for both MDM2-Lid and MDM2-Lid/short for AM-7209 and Nutlin-3a, including the number of independent titrations. State whether the 250-fold difference is statistically significant given the error estimates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Results statistically indistinguishable from the brute-force calculation are achieved with an almost six-fold decrease in computing resources requirement."
- **Evidence pointer** Figure 4D, Figure S7 (location not provided)
- **Concern** The validation of the adaptive sampling protocol rests on a single comparison to a "standard protocol" for one ligand (Pip-2). The text does not specify the statistical test used to establish "indistinguishable" results, nor the magnitude of the difference between the adaptive and standard estimates. The threshold parameter τ is described as chosen based on "additional experiments," but the sensitivity of the final binding free energy to τ is not quantified.
- **Why it matters** The methodological contribution is a key selling point of the paper. If the adaptive protocol's accuracy is not rigorously demonstrated, the broader utility of the method is questionable.
- **Resolution test** Provide a quantitative comparison (e.g., mean and standard deviation of binding free energy from both protocols) and state the statistical criterion for equivalence. Show how the final binding free energy for Pip-2 varies with τ across a range of values.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "AM-7209 shows a significant energetic preference for ordered lid conformations, thus shifting the balance towards ordering of the lid in the AM-7209/MDM2 complex."
- **Evidence pointer** Figure 5A-B, Figure 6A-C
- **Concern** The computed free energy preference of AM-7209 for the ordered lid state (ca. 3 kcal/mol over closed-disordered) is presented as the mechanistic explanation for the experimental observations. However, the text does not report the statistical uncertainty on this difference, nor the convergence criteria for the alchemical calculations in the ordered versus disordered lid states. The analysis of interactions (e.g., hydrogen bonding with Thr10) is qualitative and based on trajectory inspection, without quantitative metrics.
- **Why it matters** The central mechanistic claim depends on the reliability of the computed free energy differences. If the uncertainty is comparable to the reported preference (e.g., ±2 kcal/mol), the conclusion is not robust.
- **Resolution test** Report the mean and standard error of the binding free energy for each ligand-state combination, and state the number of independent replicates. Provide a convergence plot or similar evidence that the free energy estimates have plateaued.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** "The methodology reported herein should facilitate broader targeting of intrinsically disordered regions in medicinal chemistry."
- **Evidence pointer** Methods section, SI text (location not provided)
- **Concern** The Methods section provides a high-level summary of the computational approach, but the specific parameters for the adaptive protocol (e.g., epoch length, number of epochs, λ-schedule, restraint definitions) are not given in the main text. The authors refer to the SI for details, which is not provided for this review.
- **Why it matters** Reproducibility is a core requirement for a methodological contribution. Without the full protocol, other groups cannot implement or test the adaptive sampling method.
- **Resolution test** Ensure the SI contains all necessary parameters and that the main text includes a clear reference to where each parameter is defined.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Introduction, paragraph 1
- **Evidence pointer** Location not provided
- **Issue** The statement "Nearly half of all proteins contain significant intrinsically disordered regions (IDRs), i.e. contiguous stretches of 20-50 amino acids that remain disordered in native conditions" is imprecise. The definition of IDRs is broader than a specific length range, and the cited length range is not standard.
- **Required correction** Revise to a more standard definition, e.g., "regions lacking a stable tertiary structure under physiological conditions," and cite appropriate reviews.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results and discussion, subsection 1
- **Evidence pointer** Location not provided
- **Issue** The sentence "We prepared protein constructs for human MDM2 6-125 and MDM2 17-125 (Figure S1, Figure S2, referred to as MDM2-Lid and MDM2-Lid/short from here on)" is missing a period after "binding" in the following sentence, and the transition to the next sentence is abrupt.
- **Required correction** Add the missing punctuation and consider splitting the long sentence for readability.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results and discussion, subsection 2
- **Evidence pointer** Location not provided
- **Issue** The text states that the "open and ordered" lid macrostate accounts for ca. 6-8% of the ensemble, but the free energy difference of 1.4±0.2 kcal/mol implies a population of approximately 8-9% at 298 K. The text should reconcile these numbers or clarify the temperature used for the population estimate.
- **Required correction** State the temperature at which the population estimate is made and ensure consistency between the free energy difference and the reported population.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results and discussion, subsection 4
- **Evidence pointer** Location not provided
- **Issue** The phrase "the lid lies more frequently above helix α 2" is vague. It is unclear what "above" means in a structural context and how this was quantified.
- **Required correction** Provide a more precise description of the geometric criterion used to define the lid position relative to helix α2.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Conclusions
- **Evidence pointer** Location not provided
- **Issue** The conclusion states that the adaptive protocol "warrants further methodological investigation," but does not mention any limitations or potential failure modes of the approach.
- **Required correction** Add a sentence acknowledging potential limitations (e.g., sensitivity to force field, system-specificity) to provide a balanced perspective.

- **Technical failings that need to be addressed before the case is established** The lack of reported statistical uncertainties on the computed binding free energy differences (R1-M3) and the incomplete reporting of the calorimetric data (R1-M1) are the most significant technical gaps. The validation of the adaptive protocol (R1-M2) also needs more rigorous quantitative support.

## Risk / unsupported claims

- The claim that AM-7209's preference for the ordered lid state is "significant" (R1-M3) is not supported by reported error estimates.
- The claim that the adaptive protocol produces results "statistically indistinguishable" from the standard protocol (R1-M2) is not supported by a described statistical test.
- The statement that the "open and ordered" lid macrostate accounts for ca. 6-8% of the ensemble (R1-m3) is not reconciled with the reported free energy difference.
- The mechanistic interpretation of specific interactions (e.g., Thr10 hydrogen bonding) is based on qualitative trajectory analysis and is not quantitatively supported.
- The generalizability of the adaptive protocol to other systems is asserted without evidence beyond a single test case.