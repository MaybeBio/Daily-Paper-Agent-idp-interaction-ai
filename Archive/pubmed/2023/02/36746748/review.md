## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusions, methods, data availability)
- **Assessment boundary** Scientific claims, methodological soundness, evidence quality, and alignment with stated conclusions; limited to content provided
- **Shared manuscript claim summary** The authors use microsecond-scale all-atom MD simulations of the full Kir6.2/SUR1 KATP channel complex to characterize the dynamics of intrinsically disordered regions (IDRs), proposing roles in inter-domain signal transduction, ligand binding stabilization, and subunit interface mechanics.
- **Visible evidence base** Simulation trajectories (10 × 0.5 μs, plus 2 × 0.5 μs APO), secondary structure assignments, contact frequency analyses, RMSD/RMSF, PCA, comparison to CryoEM structures (6C3P, 7S60, 7S5X)
- **Missing materials affecting confidence** Supplementary figures referenced but not provided; no raw trajectory data; no force field validation against experimental observables for this specific system; no error bars or statistical significance tests reported for key quantitative claims

## Reviewer
- **Overall assessment** The manuscript addresses a relevant and under-explored question regarding the functional role of IDRs in a medically important ion channel complex. The computational approach is ambitious, using full-complex MD simulations at microsecond timescales. However, the evidence presented is largely descriptive and correlative. Several central claims, particularly regarding the functional significance of observed IDR behaviors, are not directly supported by the simulation data. The manuscript would benefit from clearer hypothesis testing, quantitative comparisons to experimental data, and a more cautious interpretation of functional implications.
- **Who would be interested in the results, and why** Researchers studying KATP channel gating and pharmacology, computational biophysicists interested in IDR dynamics in membrane proteins, and structural biologists investigating multi-subunit channel complexes. The work may also interest those studying the role of disordered regions in allosteric regulation more broadly.
- **Major strengths** The study tackles a genuinely difficult problem, namely the dynamics of regions invisible to conventional structural techniques. The use of a full octameric complex rather than isolated domains is commendable. The simulation length and replication (10 × 0.5 μs) provide reasonable sampling for a system of this size. The authors identify specific, testable hypotheses regarding IDR function, particularly the 900-loop interaction with the MgADP binding site.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence strength
  - **Claim pointer** The authors claim that the 900-loop, particularly the glutamic acid-rich ED domain, stabilizes MgADP binding by interacting with the ligand and reducing its fluctuations, thereby preventing dissociation.
  - **Evidence pointer** Results and Discussion, section "Intrinsically Disordered Loops of SUR1 as a Part of Hypothetical Molecular Bearing"; Figure 7
  - **Concern** The claim of a stabilizing effect on MgADP binding is based on a comparison of ligand RMSD between states with and without ED domain interaction. However, the reported RMSD difference (1.75 Å vs 2.07 Å) is small and no statistical analysis is provided. More critically, the authors state that this hypothesis "requires further computational study," which undermines the strength of the claim as presented. The functional significance of a 0.3 Å RMSD difference in the context of ligand binding affinity or dissociation kinetics is not established. The authors do not demonstrate that this interaction would affect the free energy of binding or the residence time of MgADP.
  - **Why it matters** This is presented as a key finding of the paper, suggesting a novel functional role for a conserved disordered region. If the evidence is only suggestive, the claim should be framed as a hypothesis, not a conclusion. Overstating the significance of small simulation-derived differences could mislead readers and future experimental efforts.
  - **Resolution test** Provide statistical analysis of the RMSD distributions (e.g., bootstrapping or block averaging across replicates). Ideally, compute binding free energies or residence times with and without the ED domain interaction. Alternatively, clearly reframe this as a hypothesis requiring experimental validation.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Model validation
  - **Claim pointer** The authors state that the CHARMM36m force field "gives acceptable results when modeling systems containing both IDR and folded parts" and use this to justify their simulation setup.
  - **Evidence pointer** Methods, MD Simulations section
  - **Concern** The validation of the force field is based on general benchmarking studies, not on validation against experimental data for this specific system. The KATP channel is a large, complex membrane protein with multiple domains, and the behavior of its IDRs in the context of the full complex may differ from isolated IDR peptides used in force field benchmarks. The authors do not compare their simulated IDR ensembles to any experimental observables, such as NMR chemical shifts, SAXS profiles, or FRET efficiencies, which would be necessary to establish that the simulations accurately capture the conformational preferences of these regions in situ.
  - **Why it matters** The entire study relies on the accuracy of the MD simulations. If the force field or the modeling of the missing regions (via I-TASSER and QUARK) introduces biases, all subsequent conclusions about IDR dynamics and interactions could be artifacts. Without validation, the reader cannot assess the reliability of the reported findings.
  - **Resolution test** Compare simulated IDR conformational ensembles to available experimental data, if any exist. If none exist, acknowledge this limitation explicitly and discuss how force field uncertainties might affect the conclusions. At minimum, provide a more detailed analysis of the convergence and equilibration of the IDR conformations across replicates.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Interpretive overreach
  - **Claim pointer** The authors propose that the 600-loop and 900-loop form part of a "hypothetical molecular bearing" that reduces friction between Kir6.2 and SUR1 subunits during channel gating.
  - **Evidence pointer** Results and Discussion, section "Intrinsically Disordered Loops of SUR1 as a Part of Hypothetical Molecular Bearing"
  - **Concern** The "molecular bearing" concept is introduced as an interpretation of observed flexibility and contacts, but no quantitative analysis is provided to support this mechanical analogy. The authors do not measure friction, energy dissipation, or any mechanical property that would justify the bearing metaphor. The claim is speculative and goes beyond what the simulation data can directly show.
  - **Why it matters** While speculative interpretations can be valuable for generating hypotheses, they should be clearly labeled as such. The current text presents this as a plausible function without sufficient evidence, which could be misleading. The mechanical analogy may not be accurate and could constrain thinking about alternative functional roles.
  - **Resolution test** Either provide quantitative analysis supporting the mechanical interpretation (e.g., analysis of correlated motions, energy transfer between domains) or explicitly label this as a speculative hypothesis requiring further investigation.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Completeness of evidence
  - **Claim pointer** The authors state that "the presence of IDRs affects natural ligand binding" in the abstract.
  - **Evidence pointer** Abstract; Results and Discussion, sections on N-ter and 900-loop
  - **Concern** The abstract makes a general claim about IDRs affecting ligand binding, but the evidence presented is limited to the 900-loop interaction with MgADP and the N-ter interaction with the SUR1 binding pocket. The authors do not systematically test how the presence or absence of IDRs affects ligand binding. The APO model is used as a comparison, but this removes the ligand rather than testing the role of IDRs. A more direct test would involve simulations with truncated or mutated IDRs to assess their specific contribution.
  - **Why it matters** The abstract's claim is broader than what the evidence supports. This could overstate the significance of the findings and mislead readers about the strength of the evidence. The manuscript would be more credible if the claims were more carefully matched to the evidence.
  - **Resolution test** Either narrow the claim in the abstract to specifically refer to the 900-loop and N-ter interactions, or provide additional simulations that directly test the role of IDRs in ligand binding (e.g., by deleting or mutating the IDRs).
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Figure 2
  - **Evidence pointer** Results and Discussion, section "Whole KATP System MD Simulations"
  - **Issue** The description of Figure 2 is dense and difficult to follow. The relationship between the different panels and the structural parameters being compared is not immediately clear.
  - **Required correction** Provide a clearer explanation of each panel in the figure legend and in the text, including what structural parameter is being shown and why it is relevant to the comparison with experimental structures.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods, Data Analysis
  - **Evidence pointer** Methods, Data Analysis section
  - **Issue** The description of the contact frequency analysis is brief. The "residue–residue contact score" is referenced but not defined in sufficient detail for reproduction.
  - **Required correction** Provide a more detailed description of the contact score calculation, including the distance cutoff, the definition of a "close contact," and how the 0.1 threshold was chosen.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Statistical rigor
  - **Affected element** Contact frequency claims
  - **Evidence pointer** Results and Discussion, sections on N-ter and 900-loop
  - **Issue** Contact frequencies are reported as percentages (e.g., "40% of the simulation time") without error estimates across the 10 replicates. Given the observed anisotropy between chains, it is important to know the variability.
  - **Required correction** Report contact frequencies as mean ± standard deviation across replicates, or provide a measure of variability.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Literature context
  - **Affected element** Introduction and Discussion
  - **Evidence pointer** Introduction; Results and Discussion
  - **Issue** The discussion of IDR function in ion channels is limited. The authors mention PIEZO2 but do not engage with the broader literature on IDRs in membrane proteins or in KATP channels specifically.
  - **Required correction** Expand the discussion to place the findings in the context of other studies on IDR function in ion channels and membrane proteins, which would strengthen the significance of the work.
- **Technical failings that need to be addressed before the case is established** The primary technical failing is the lack of validation of the simulated IDR ensembles against experimental data. The modeling of missing regions using I-TASSER and QUARK introduces uncertainty that is not addressed. Additionally, the absence of statistical analysis for key quantitative claims (e.g., RMSD differences, contact frequencies) weakens the evidence. The manuscript would be substantially strengthened by including error estimates and, ideally, some form of experimental validation or comparison.
- **Assessment against Nature-style criteria**  
  *Originality*: The application of full-complex MD simulations to study IDR dynamics in KATP channels is novel and addresses a genuine gap in the field. The focus on IDRs in this context is timely and original.  
  *Scientific importance*: The KATP channel is a critical therapeutic target, and understanding its gating mechanism is of high importance. However, the current evidence is largely descriptive, and the functional significance of the observed IDR behaviors is not firmly established. The importance of the findings is therefore potential rather than demonstrated.  
  *Interdisciplinary readership*: The work bridges structural biology, computational biophysics, and ion channel physiology. It would appeal to researchers in these fields, though the technical detail may limit broader appeal.  
  *Technical soundness*: The simulation setup is reasonable, but the lack of validation and statistical rigor are significant weaknesses. The use of a single force field and the modeling of missing regions without cross-validation reduce confidence in the results.  
  *Readability for nonspecialists*: The manuscript is generally well-written but assumes significant background knowledge in both MD simulation methodology and KATP channel biology. The abstract is accessible, but the results section is dense and would be challenging for nonspecialists.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important question with a novel approach, but the evidence as presented does not fully support the functional claims. Addressing the concerns regarding validation, statistical rigor, and interpretive restraint would substantially strengthen the manuscript.

## Risk / unsupported claims
- The claim that IDRs "affect natural ligand binding" is broader than the evidence supports; only the 900-loop interaction with MgADP and N-ter interactions are examined.
- The "molecular bearing" hypothesis is presented without quantitative mechanical analysis.
- The stabilizing effect of the ED domain on MgADP binding is based on a small RMSD difference without statistical significance testing.
- The statement that the simulation setup is appropriate for IDR-containing systems relies on general force field benchmarks rather than system-specific validation.
- The functional significance of observed N-ter helical propensity is not directly tested or linked to channel gating outcomes.