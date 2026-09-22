## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the provided manuscript text
- **Shared manuscript claim summary** The manuscript investigates the role of extended regions flanking the RNA recognition motif (RRM) of the spliceosomal protein U1-70K in binding to SL1 RNA. Using thermal dissociation experiments, temperature-jump kinetics, and molecular dynamics simulations, the authors propose that the N-terminal helix and C-terminal intrinsically disordered region contribute to complex stability under stress conditions such as elevated temperature and high salt concentration, acting through distributed interactions rather than simple local contacts.
- **Visible evidence base** Experimental thermal denaturation monitored by FRET and tryptophan fluorescence; temperature-jump relaxation kinetics; over 20 μs of MD simulations; sequence alignments; supplementary tables and figures referenced
- **Missing materials affecting confidence** Supplementary figures and tables (S1–S21) are referenced but not provided; full experimental replicates and error analysis details are not visible; MD simulation force field parameters and convergence criteria are only partially described; raw data files are not accessible

## Reviewer
- **Overall assessment** This manuscript addresses a relevant question in RNA-protein recognition, namely how regions flanking a canonical RRM contribute to binding affinity and stability. The combination of equilibrium thermodynamics, kinetics, and atomistic simulations is appropriate and potentially powerful. However, the central claim that the flanking regions act via "distributed interactions" under stress is not fully supported by the data as presented. The experimental design is sound, but several quantitative analyses and control experiments are not described in sufficient detail to evaluate robustness. The manuscript would benefit from clearer presentation of error analysis, additional validation of the simulation findings against experimental observables, and a more cautious interpretation of the mechanistic conclusions.
- **Who would be interested in the results, and why** Researchers studying RNA-protein interactions, particularly those focused on spliceosomal assembly and function, will find this work relevant. The methodological combination of FRET-based thermal denaturation, kinetic measurements, and MD simulations may also interest biophysicists studying biomolecular recognition. The potential implications for understanding how RNA-protein complexes respond to cellular stress could attract a broader readership in RNA biology and cell biology.
- **Major strengths** The study addresses a gap in understanding of extended RRM contributions to RNA binding. The use of complementary experimental probes (FRET for global, tryptophan for local) is thoughtful. The inclusion of multiple salt and temperature conditions provides a systematic view of stress effects. The MD simulations are extensive and directly tied to experimental conditions.
- **Major Concerns** The mechanistic interpretation is not fully supported by the data. The claim that truncations stabilize stacking interactions while destabilizing the complex is counterintuitive and requires more direct evidence. The relationship between the MD-derived "distributed interactions" and the experimentally measured thermodynamic parameters is not quantitatively established. The choice of the double mutant RNA for kinetic studies and the extrapolation to wild-type behavior needs justification. The manuscript does not provide sufficient statistical analysis of the experimental replicates or convergence assessment for the simulations.
- **Minor Comments** The writing is generally clear but some methodological details are ambiguous. The use of "eRRM" and related abbreviations could be defined more explicitly. The figures are referenced but not visible in the provided text, making it difficult to assess data presentation quality.
- **Technical failings that need to be addressed before the case is established** The quantitative link between experimental observables and simulation-derived quantities is missing. The error bars and replicate numbers for the thermodynamic and kinetic measurements are not stated. The MD simulation analysis lacks a clear demonstration that the observed differences between constructs are statistically significant and converged.
- **Assessment against Nature-style criteria** Originality: The concept of extended RRM contributions is not entirely new, but the specific focus on stress-dependent roles is a fresh angle. Scientific importance: The findings could inform understanding of spliceosomal dynamics under stress, which is of moderate importance. Interdisciplinary readership: The work bridges biophysics, RNA biology, and computational biology, which could attract a broad audience. Technical soundness: The experimental and computational approaches are appropriate, but the analysis and interpretation have gaps that need addressing. Readability for nonspecialists: The manuscript is largely accessible, though some sections assume familiarity with biophysical methods.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding quantitative rigor and the interpretation of simulation results.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative rigor
- **Claim pointer** The manuscript claims that truncation of the N-helix increases Kd by about 150-fold and that the double mutant RNA shows additive destabilization effects.
- **Evidence pointer** Results section, Table 1, Supplementary Figures S6 and S7
- **Concern** The reported Kd values and fold-changes are presented without error bars or confidence intervals. It is unclear how many independent replicates were performed and whether the differences between constructs are statistically significant. The additive effect of the two RNA mutations is stated but no statistical test is described.
- **Why it matters** Without proper error analysis, the reader cannot assess whether the observed differences are meaningful or within experimental noise. This is particularly important for the central claim that the N-helix contributes significantly to binding under stress conditions.
- **Resolution test** Provide replicate numbers, standard deviations or confidence intervals for all reported Kd and T1/2 values, and perform appropriate statistical tests (e.g., t-tests or ANOVA) to support claims of significant differences between constructs.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of simulation results
- **Claim pointer** The manuscript claims that MD simulations show that truncations stabilize the F148-C32 stacking interaction, and that this stabilization is due to the linker region interacting with the RNA.
- **Evidence base** Results section, Figure 6 and 7
- **Concern** The simulation finding that truncations stabilize a key stacking interaction while experimentally destabilizing the complex is counterintuitive. The manuscript does not provide a quantitative explanation for how this local stabilization relates to the overall loss of binding affinity. The claim that the linker region "transiently interacts" with the RNA is based on qualitative observations without quantitative metrics (e.g., contact frequencies, residence times).
- **Why it matters** The mechanistic conclusion rests on this counterintuitive result. Without a clear quantitative link between the simulation observations and the experimental thermodynamics, the interpretation remains speculative.
- **Resolution test** Provide quantitative analysis of the simulation trajectories, such as contact maps, interaction energies, or free energy calculations, that directly connect the observed stacking stabilization to the experimentally measured binding affinities. Alternatively, perform additional simulations or experiments to test the proposed mechanism.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental design and controls
- **Claim pointer** The manuscript uses a double mutant RNA (A32C/G34U) for kinetic studies and states that this mutant is suitable for comparison with future in-cell studies requiring dissociation temperatures below 45°C.
- **Evidence base** Results section, Supplementary Figure S7
- **Concern** The rationale for using the double mutant RNA for kinetic studies is not fully justified. The manuscript does not demonstrate that the double mutant behaves similarly to the wild-type RNA in terms of binding mechanism or structure. The claim that the mutant is suitable for future in-cell studies is speculative and not supported by data.
- **Why it matters** If the double mutant does not faithfully represent the wild-type interaction, conclusions drawn from kinetic studies may not be generalizable. The suitability claim for future studies needs to be grounded in evidence.
- **Resolution test** Provide structural or biophysical evidence that the double mutant RNA binds in a manner similar to the wild-type RNA, or clearly state the limitations of using the mutant and how conclusions are affected.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Simulation methodology
- **Claim pointer** The manuscript states that 22.5 μs of MD simulations were performed across multiple conditions and replicas.
- **Evidence base** Methods section, Supplementary Figure S5
- **Concern** The description of the simulation setup is incomplete. The force field parameters, water model, salt concentration treatment, and equilibration protocol are only partially described. The convergence of the simulations is not demonstrated beyond RMSD plots, which are insufficient to establish sampling adequacy for the conclusions drawn.
- **Why it matters** The reliability of the simulation-based conclusions depends on the quality and convergence of the simulations. Incomplete methodological details prevent the reader from assessing the validity of the results.
- **Resolution test** Provide complete simulation parameters, demonstrate convergence through multiple metrics (e.g., block averaging, replica convergence), and discuss the limitations of the sampling.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence base** Abstract
- **Issue** The abstract states that truncation of the N-helix "strongly reduces overall binding" but does not quantify this effect or mention the specific conditions under which this was observed.
- **Required correction** Include a quantitative statement (e.g., fold-change in Kd) and specify the conditions (e.g., salt concentration, temperature) in the abstract.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodology
- **Affected element** Methods section, RNA handling
- **Evidence base** Methods section
- **Issue** The RNA construct is described as 32 bp, but SL1 RNA is a stem-loop structure. The term "bp" is ambiguous for a single-stranded RNA that forms a hairpin.
- **Required correction** Clarify the RNA construct description, e.g., "32-nucleotide stem-loop" or provide the exact sequence and secondary structure.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Results section, Figure 3
- **Evidence base** Results section
- **Issue** The near-linear dependence of log(Kd) on log([KCl]) with a slope of 7.4 is interpreted as evidence for approximately seven salt bridges. This interpretation assumes a simple electrostatic model that may not be valid for a complex RNA-protein interface.
- **Required correction** Acknowledge the limitations of this interpretation and discuss alternative explanations for the observed salt dependence.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion
- **Evidence base** Discussion
- **Issue** The discussion speculates about the role of extended RRMs in other spliceosomal and ribosomal complexes without citing specific examples or evidence.
- **Required correction** Either provide supporting references for this speculation or temper the statement to clearly indicate it as a hypothesis.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence base** Throughout
- **Issue** The term "eRRM" is used to describe the extended RRM, but the definition of "extended" is not explicitly stated in terms of residue ranges or structural boundaries.
- **Required correction** Define the boundaries of the eRRM construct and clarify what constitutes the "extended" region relative to the minimal RRM.

## Risk / unsupported claims
- The claim that the N-helix acts as a "guardian under stress" is speculative and not directly supported by the data presented.
- The statement that the C-IDR is "potentially more important in-cell than in vitro" is not supported by any in-cell experiments or data.
- The interpretation of the salt dependence slope as indicating exactly seven salt bridges is an oversimplification and not fully justified.
- The suitability of the double mutant RNA for future in-cell studies is asserted without supporting evidence.
- The claim that distributed interactions, rather than local contacts, govern the observed effects is not quantitatively established.