## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure legends
- **Assessment boundary** Scientific claims, methodological soundness, data interpretation, and generalizability of conclusions as presented in the provided text
- **Shared manuscript claim summary** The authors propose that proline cis/trans isomerization in the PRLR 14-3-3 binding motif acts as a conformational selection mechanism, with the cis isomer binding 14-3-3 with approximately 1000-fold higher affinity than the trans isomer. They support this with NMR spectroscopy, ITC, bioinformatic analysis of PDB structures, and MD simulations, and suggest this mechanism has broad implications for 14-3-3 interactome selectivity and signaling dynamics.
- **Visible evidence base** Abstract, full introduction, results and discussion sections, methods descriptions, figure legends referenced in text, supplementary figure references
- **Missing materials affecting confidence** Actual figures and supplementary figures not provided; raw NMR spectra, ITC thermograms, MD simulation trajectories, and analysis scripts not accessible; detailed statistical analysis and error propagation methods not fully described

## Reviewer

- **Overall assessment** This manuscript presents a compelling and potentially significant finding that proline cis/trans isomerization can act as a conformational selection switch in 14-3-3 binding, with the PRLR motif showing an unusually strong cis preference. The combination of bioinformatic analysis, experimental biophysics, and MD simulation is commendable and the conclusions are largely supported by the described data. However, several technical concerns regarding the quantification of isomer-specific affinities, the interpretation of the real-time NMR experiments, and the generalizability of the PDB analysis need to be addressed before the case is fully established. The work is original and likely to be of interest to the IDP and signaling communities, but the current evidence base has some gaps that require clarification.

- **Who would be interested in the results, and why** Structural biologists studying intrinsically disordered proteins and short linear motifs; researchers working on 14-3-3 signaling pathways, particularly in cancer and neurological contexts; biophysicists interested in conformational selection mechanisms and slow timescale dynamics; drug developers targeting protein-protein interactions involving 14-3-3. The methodological approach combining NMR, ITC, and MD will also appeal to those developing tools for studying proline isomerization in other systems.

- **Major Strengths** The study addresses a previously underappreciated aspect of 14-3-3 binding, namely proline isomer-specific affinity, and provides quantitative evidence for a strong cis preference in the PRLR motif. The combination of bioinformatic analysis of the PDB with experimental validation is powerful. The real-time NMR approach to directly observe isomer-specific binding kinetics is innovative. The use of multiple complementary techniques (NMR, ITC, MD) strengthens the conclusions. The evolutionary conservation analysis of the PRLR motif adds biological relevance.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantification of isomer-specific binding affinities
- **Claim pointer** The authors claim a Kd,trans/Kd,cis ratio of 700 ± 200 for the WT PRLR peptide, and subsequently derive individual Kd values of 130 ± 40 nM (cis) and 80 ± 20 μM (trans) from COPASI modeling.
- **Evidence pointer** Results section "PRLR:14–3–3 Binding Depends on the Proline Concentration", Figure 2, Table 1
- **Concern** The real-time NMR experiment used to derive the affinity ratio relies on extrapolating t0 concentrations from a single-exponential decay fit. The authors state that the first spectrum was obtained ~5 min after mixing, and the extrapolation to t0 assumes that the initial binding event is instantaneous and that only the re-equilibration process is observed. However, given that the binding of the cis isomer is reported to be very fast (millisecond timescale), it is unclear whether the initial binding of both isomers is fully captured by this extrapolation. The error on the extrapolated t0 values, and hence on the affinity ratio, may be larger than reported. Furthermore, the COPASI model used to fit the ITC data incorporates the Kd ratio from the NMR experiment as a fixed parameter, meaning any error in the NMR-derived ratio propagates into the individual Kd values. The authors should provide a more detailed error analysis, including confidence intervals for the fitted parameters, and ideally validate the model with independent experiments.
- **Why it matters** The central claim of the manuscript, that the cis isomer binds with ~1000-fold higher affinity than the trans isomer, rests on this quantification. If the error is larger than reported, or if the model is not uniquely constrained by the data, the magnitude of the selectivity could be substantially different, which would weaken the conclusions about the biological significance of the effect.
- **Resolution test** Provide a full error analysis of the NMR-derived affinity ratio, including bootstrap or Monte Carlo resampling of the fitted decay curves. Show that the COPASI model is identifiable, e.g., by performing a profile likelihood analysis or by fitting the ITC data without fixing the Kd ratio and demonstrating that the data alone can constrain the individual Kd values. Ideally, validate the model with an independent method, such as competition ITC or surface plasmon resonance.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of PDB analysis
- **Claim pointer** The authors state that "around 20% of these crystallize in their cis isomer" for 14-3-3 bound peptides with a proline at the +2 position, and that this is an "overrepresentation compared to the general cis proline frequency."
- **Evidence pointer** Results section "Structural Analysis Reveals High cis Proline Frequency in 14–3–3 Binding Peptides", Figure 1A
- **Concern** The PDB analysis is based on crystal structures, which may not reflect the solution-state equilibrium of the free peptides. The authors acknowledge this limitation, but the comparison to the "general cis proline frequency" of ~6% in proteins may not be appropriate. The 6% figure is typically derived from high-resolution structures of folded proteins, where the local environment constrains the isomer state. For IDRs, the cis population can be much higher, as the authors themselves note for Trp-Pro motifs (up to 40%). The relevant comparison for the 14-3-3 bound peptides would be the cis population of the free peptide in solution, not the global average. The authors should clarify this and, if possible, compare their bound-state observations to the known solution-state cis populations of the specific motifs they identify.
- **Why it matters** The claim that 14-3-3 binding peptides are enriched in cis proline conformations is used to support the general relevance of the phenomenon. If the comparison is not appropriate, the strength of this claim is diminished.
- **Resolution test** Revise the analysis to compare the cis proline frequency in 14-3-3 bound peptides to the expected cis population of the same motifs in solution, using published data or NMR measurements of representative free peptides. Alternatively, clearly state the limitation and temper the claim of "overrepresentation."

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** MD simulation methodology and interpretation
- **Claim pointer** The authors claim that MD simulations "identify structural constraints in the narrow 14-3-3 binding groove that provide an explanation for the observed isomer selectivity" and that the trans proline peptide adopts a strained conformation.
- **Evidence pointer** Results section "Limited Space in the Narrow Binding Groove Dictates Isomer Specificity", Figure 5
- **Concern** The MD simulations are described briefly and the force field, simulation length, and analysis methods are not fully detailed. The authors state that the trans proline peptide "undergoes significant restructuring" after ~600 ns, but it is unclear how many independent simulations were performed and whether the observed restructuring is reproducible. The claim of "steric clashes" between PRLR and 14-3-3 residues Asn42, Ser45, and Val46 is based on a single trajectory or a small number of trajectories. The authors should provide more details on the simulation setup, convergence, and reproducibility, and ideally show that the strained conformation is consistently observed across multiple independent simulations.
- **Why it matters** The MD simulations provide the structural rationale for the observed selectivity. If the simulations are not robust, the mechanistic explanation is weakened.
- **Resolution test** Provide full details of the MD simulation protocol, including force field parameters, water model, ion concentration, simulation length, and number of replicates. Show that the observed restructuring and steric clashes are reproducible across replicates. Consider enhanced sampling methods to ensure the conformational space is adequately explored.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Biological relevance and generalizability
- **Claim pointer** The authors suggest that "proline isomerization constitutes a previously unrecognized selective component relevant to the ubiquitous 14-3-3 interactome" and that the cis preference of WT PRLR introduces a slow kinetic component relevant to signal propagation.
- **Evidence pointer** Results section "Implications of Isomer-Selective Steps in Signal Transduction", Figure 6
- **Concern** The biological relevance is inferred from the in vitro biophysical data and the PDB analysis, but no cellular or in vivo experiments are presented. The claim that the slow kinetic component is "relevant to signal propagation" is speculative. The authors should either provide direct evidence for the biological role of the cis preference, or clearly frame this as a hypothesis. Additionally, the generalizability to the broader 14-3-3 interactome is based on a limited number of motifs analyzed in the PDB, and the authors have not demonstrated that the cis preference is a common feature of 14-3-3 interactions.
- **Why it matters** The broader significance of the work depends on the claim that this mechanism is relevant beyond the specific PRLR motif. Without direct biological evidence, the impact of the study is reduced.
- **Resolution test** Provide experimental evidence in a cellular context, such as mutational studies in cells showing that the cis preference affects signaling output. Alternatively, expand the bioinformatic analysis to a larger set of 14-3-3 binding motifs and show that the cis preference is a general feature.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** ITC data analysis
- **Evidence pointer** Methods section "Isothermal Titration Calorimetry"
- **Issue** The description of the ITC data analysis is brief. The authors state that data were analyzed using Origin and in-house scripts, but do not specify the exact model used for the one-set-of-sites fit, the number of replicates, or how the stoichiometry (N-value) was determined.
- **Required correction** Provide more detail on the ITC fitting procedure, including the model equation, the number of independent experiments, and the uncertainty on the fitted parameters.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Figure accessibility
- **Affected element** All figures
- **Evidence pointer** Figures 1-6 and supplementary figures
- **Issue** The figures are not provided in the manuscript text, making it difficult to fully assess the data quality and the validity of the claims.
- **Required correction** Ensure that all figures are included in the final submission and that the figure legends are sufficiently detailed to allow independent interpretation.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** NMR-derived rate constants
- **Evidence pointer** Results section "PRLR:14–3–3 Binding Depends on the Proline Concentration", Figure 2C
- **Issue** The reported exchange rate constant of (9.7 ± 0.7) × 10-4 s-1 is stated as the mean ± standard deviation of all available traces, but the number of traces and the reproducibility across independent experiments are not specified.
- **Required correction** Report the number of independent experiments and the number of traces used for the rate constant determination.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Binary selectivity"
- **Evidence pointer** Conclusion section
- **Issue** The term "binary selectivity" is used to describe the near-complete preference for the cis isomer. This term may be misleading, as it implies a digital on/off behavior, whereas the actual selectivity is a continuum.
- **Required correction** Consider using a more precise term, such as "strong cis preference" or "high cis selectivity," to avoid overstatement.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction section
- **Issue** The introduction cites several references on proline isomerization in IDPs, but the discussion of previous work on 14-3-3 binding and proline isomerization is limited. The authors should more thoroughly discuss prior studies that have examined proline isomer effects in 14-3-3 interactions, if any exist.
- **Required correction** Expand the discussion to include any prior work on proline isomerization in 14-3-3 binding, and clearly differentiate the current findings from previous studies.

- **Technical failings that need to be addressed before the case is established** R1-M1 (quantification of isomer-specific affinities) is the primary technical concern that must be resolved. The error analysis and model validation described in the resolution test are essential. R1-M3 (MD simulation robustness) also needs to be addressed to support the structural interpretation.

- **Assessment against Nature-style criteria** 
  - Originality: High. The concept of proline cis/trans conformational selection in 14-3-3 binding is novel and has not been quantitatively demonstrated before. The real-time NMR approach to directly measure isomer-specific binding is innovative.
  - Scientific importance: Moderate to high. If the findings are generalizable, they could have significant implications for understanding 14-3-3 signaling dynamics and for drug development targeting these interactions. However, the biological relevance is not yet directly demonstrated.
  - Interdisciplinary readership: Moderate. The work will appeal to structural biologists, biophysicists, and cell signaling researchers, but the technical nature of the methods may limit broader appeal.
  - Technical soundness: The combination of methods is appropriate and the overall approach is sound, but the concerns about error analysis and MD simulation robustness need to be addressed.
  - Readability for nonspecialists: The manuscript is generally well-written and the concepts are explained clearly, but the methods sections are dense and may be challenging for nonspecialists.

- **Recommendation posture** Supportive if technical concerns are resolved. The core finding, that the PRLR 14-3-3 motif shows a strong cis proline preference, is likely correct and significant. However, the quantification of the affinity ratio and the individual Kd values needs to be more rigorously established, and the MD simulation interpretation needs to be more robust. If these concerns are addressed, the manuscript would be suitable for publication in a high-impact journal.