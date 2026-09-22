## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv, 2024)
- **Assessment boundary** Scientific content, technical soundness, and claims as presented in the provided manuscript text; no external validation or replication attempted
- **Shared manuscript claim summary** The authors characterize the interaction between the intrinsically disordered protein SERF and a folded RNA (HIV-1 TAR) using complementary biophysical methods and simulations, finding that binding is not accompanied by major structural changes in either molecule, but is associated with modest compaction of the SERF ensemble, and that the system undergoes liquid-liquid phase separation at high concentrations or with crowding agents.
- **Visible evidence base** Abstract; Introduction; Results sections (Conformational properties of SERF; Dynamic SERF-TAR complexes are globally compact; SERF and TAR exhibit two-phase behavior at high concentrations); Discussion; Materials and Methods (oligonucleotides, labeled RNA preparation, protein expression/purification, fluorescence anisotropy, spin-labeling cysteine mutants, NMR spectroscopy, SAXS, native IM-MS, CG simulations in LAMMPS, all-atom simulations in CAMPARI, simulation processing/analysis); Data and code availability; Acknowledgements
- **Missing materials affecting confidence** Supplementary figures and tables (Fig. S1–S8, Tables S1–S6) referenced but not provided; source data files not accessible; specific numerical values for some fitted parameters (e.g., KD from NMR titrations) not fully reported in text; details of SAXS data analysis (e.g., Guinier fits, Kratky plots) not shown; simulation convergence and error analysis not fully described

## Reviewer
- **Overall assessment** This manuscript presents a thorough, multi-technique characterization of a model IDR-RNA system, with a commendable integration of experimental and computational approaches. The choice of SERF and TAR as a tractable system for studying IDR-RNA interactions is well justified, and the central finding—that binding occurs without major structural rearrangement but with modest compaction of the disordered protein—is plausible and supported by the data presented. However, several technical concerns, particularly regarding the interpretation of NMR relaxation data, the quantitative rigor of the binding affinity measurements, and the transferability of coarse-grained simulation results, need to be addressed before the case is fully established. The manuscript is generally well written and accessible, though some methodological details require clarification.
- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, RNA-binding proteins, biomolecular condensates, and biophysical chemistry would find this work of interest. The study provides a detailed example of how a disordered protein engages a structured RNA, with implications for understanding the molecular grammar of IDR-RNA interactions in phase separation and gene regulation. The methodological framework combining NMR, SAXS, IM-MS, and simulations may serve as a template for similar investigations.
- **Major strengths** 1) The use of a small, well-defined system (SERF and a 29-nt TAR fragment) that permits high-resolution interrogation without the complications of larger multi-domain RBPs. 2) The integration of multiple complementary techniques (NMR, SAXS, IM-MS, fluorescence anisotropy, CG and all-atom simulations) to provide a multi-scale view of the complex. 3) The demonstration that the SERF-TAR system undergoes phase separation at accessible concentrations, bridging dilute-phase binding studies to condensed-phase behavior. 4) The careful consideration of the limitations of each method, particularly the coarse-grained simulations.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (NMR relaxation interpretation), R1-M2 (binding affinity quantification), R1-M3 (simulation-to-experiment mapping)
- **Assessment against Nature-style criteria** **Originality:** The work is original in its specific system and integrated approach, though the general concept of IDR-RNA interactions is not new. The finding that SERF compacts upon binding without folding is a useful contribution. **Scientific importance:** Moderate to high; the study provides mechanistic insight into a common but under-characterized class of interactions, with potential relevance to understanding RBP function and phase separation. **Interdisciplinary readership:** The work bridges protein biophysics, RNA biology, and computational chemistry, and should appeal to a broad readership in these areas. **Technical soundness:** Generally sound, but with notable concerns in the interpretation of NMR relaxation data and the quantitative treatment of binding affinities (see Major Concerns). **Readability for nonspecialists:** The manuscript is well organized and clearly written, with appropriate context provided in the introduction. Some methodological sections are dense but understandable.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the interpretation of NMR relaxation data and the quantitative rigor of the binding affinity measurements.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data interpretation
- **Claim pointer** The authors state that "the T2 values in the CTR of SERF are depressed (Fig. 2B), likely reflecting the high contact density between spin systems arising from the α-helical structure" and that "the marked differences in T2 times between the two halves of SERF suggest that the molecular motions of these regions are decorrelated."
- **Evidence pointer** Results section "Conformational properties of SERF", Figure 2B
- **Concern** The interpretation of reduced T2 values in the C-terminal region as evidence for α-helical structure and decorrelated motions is not straightforward. T2 relaxation in disordered proteins is influenced by multiple factors, including chemical exchange, local dynamics, and overall tumbling. The authors do not provide a quantitative analysis (e.g., reduced spectral density mapping or model-free analysis) to support the claim that the T2 profile reflects structural features rather than dynamics. Furthermore, the statement that "molecular motions of these regions are decorrelated" is not directly supported by the T2 data alone; this would require additional measurements (e.g., relaxation dispersion or cross-correlation rates).
- **Why it matters** The interpretation of the T2 data underpins the description of the SERF ensemble and its regional differences, which is central to the paper's characterization of the unbound state. If the T2 differences are due to dynamics rather than structure, the conclusions about the CTR being more structured would be weakened.
- **Resolution test** Provide a more quantitative analysis of the relaxation data, such as reduced spectral density mapping or model-free analysis, to separate contributions from structure and dynamics. Alternatively, present additional data (e.g., relaxation dispersion) to support the claim of decorrelated motions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative rigor
- **Claim pointer** The authors report an apparent KD of 0.67 ± 0.04 μM for the SERF-TAR interaction from fluorescence anisotropy, and a KD of 1.9 ± 0.2 μM for SERF-(rU)30.
- **Evidence pointer** Results section "Dynamic SERF-TAR complexes are globally compact", Figure 3A, Table S3
- **Concern** The fluorescence anisotropy binding experiments are described, but the fitting procedure and the assumptions of the 1:1 binding model are not fully detailed. The authors do not report the stoichiometry of the complex independently (e.g., via mass spectrometry or analytical ultracentrifugation), and the IM-MS data show evidence of a 2:1 SERF-TAR complex. The presence of higher-order species could complicate the interpretation of the anisotropy data, which assumes a simple 1:1 equilibrium. Additionally, the error bars on the KD values are reported as standard errors from the fit, but the number of replicates and the reproducibility of the measurements are not stated.
- **Why it matters** The KD values are used to compare binding affinities between TAR and (rU)30, and to support the claim that SERF binds TAR with modest affinity. If the binding model is incorrect or the measurements are not reproducible, the quantitative conclusions are not reliable.
- **Resolution test** Provide a more detailed description of the fitting procedure, including the model used and the treatment of the fluorescent signal. Report the number of independent replicates and the reproducibility of the KD values. Consider performing additional experiments (e.g., ITC or MST) to validate the KD values and to determine the stoichiometry of the complex.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Simulation-to-experiment mapping
- **Claim pointer** The authors state that "CG simulations of 'SERF' and 'TAR' show the highest contact frequency within NTR" and that "CG simulations of 'SERF (1–34)' with 'TAR' yielded the same relative dissociation constant as the full-length 'SERF' with TAR'."
- **Evidence pointer** Results section "Dynamic SERF-TAR complexes are globally compact", Figure 4C, Table S3
- **Concern** The coarse-grained simulations use a simplified representation of both protein and RNA, and the authors acknowledge that the nucleotide identity is not distinguished in the model. The claim that the simulations reproduce the experimental binding interface and affinity is not well supported. The contact frequency analysis is qualitative, and the calculation of relative dissociation constants from simulations relies on assumptions about the relationship between simulation-derived populations and experimental binding affinities. The authors do not provide a quantitative comparison between the simulated and experimental binding free energies or a validation of the simulation model against the experimental data beyond the qualitative agreement in the binding interface.
- **Why it matters** The simulations are used to support the experimental findings and to provide a mechanistic interpretation of the binding interface. If the simulations are not quantitatively reliable, the conclusions drawn from them are weakened.
- **Resolution test** Provide a more quantitative comparison between the simulated and experimental binding affinities, including an estimate of the uncertainty in the simulated KD values. Consider performing additional simulations with a more detailed model (e.g., all-atom simulations of the complex) to validate the coarse-grained results.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section "Protein NMR experiments on the SERF-TAR complex"
- **Evidence pointer** Materials and Methods
- **Issue** The description of the NMR experiments on the complex is brief, and it is not clear how the assignments of SERF in the presence of TAR were obtained, given the line broadening mentioned in the Results.
- **Required correction** Provide more detail on the assignment strategy for the bound state, including the specific experiments used and how the assignments were validated.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section "SERF and TAR exhibit two-phase behavior at high concentrations"
- **Evidence pointer** Figure 5
- **Issue** The phase diagram for SERF-TAR is mentioned, but the full phase diagram is not shown in the main text or described in detail. The authors state that the threshold for phase separation is "sufficiently high" to study the dilute phase, but the actual concentrations used for the phase separation experiments are not clearly stated in the Results.
- **Required correction** Include a more complete description of the phase behavior, including the concentrations used and the full phase diagram, either in the main text or in the supplementary material.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Methods section "Coarse-grained (CG) Simulations in LAMMPS"
- **Evidence pointer** Materials and Methods
- **Issue** The description of the coarse-grained simulations is somewhat terse, and the parameters used for the Mpiri force field are not fully specified. The authors state that the effective NaCl concentration was set to 0.05 M, but the method for mapping this to the simulation parameters is not described.
- **Required correction** Provide more detail on the simulation parameters, including the specific values used for the interaction strengths and the method for setting the ionic strength.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure 2
- **Evidence pointer** Figure 2
- **Issue** The figure is not provided in the manuscript text, so it is difficult to assess the quality of the data presentation.
- **Required correction** Ensure that all figures are clearly labeled and that the data are presented in a way that is easy to interpret.

## Risk / unsupported claims
- The claim that "the marked differences in T2 times between the two halves of SERF suggest that the molecular motions of these regions are decorrelated" is not directly supported by the data presented and requires additional analysis.
- The claim that "CG simulations of 'SERF (1–34)' with 'TAR' yielded the same relative dissociation constant as the full-length 'SERF' with TAR'" is not quantitatively validated, as the uncertainty in the simulated KD values is not reported.
- The claim that "the threshold for demixing is sufficiently high that we could use solution-state biophysical methods to interrogate the stoichiometric complexes" is plausible but not fully quantified; the exact concentrations used for the dilute-phase studies are not clearly stated.
- The claim that "SERF and TAR primarily form a binary complex at concentrations suitable for biophysical characterization" is supported by the IM-MS data, but the presence of a 2:1 complex suggests that higher-order species may be present even in the dilute phase, which could complicate the interpretation of the binding data.