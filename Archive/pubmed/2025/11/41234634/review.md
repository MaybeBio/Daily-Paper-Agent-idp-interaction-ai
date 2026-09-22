## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, computational methods, results and discussion, conclusions, and supplementary declarations.
- **Assessment boundary** Scientific soundness, methodological rigor, validity of claims relative to the provided evidence, and clarity of presentation. No assessment of editorial fit or publication policy.
- **Shared manuscript claim summary** The authors report a computational study in which three flavonoids (hesperidin, morin, myricetin) were screened against an α-synuclein dimer (PDB 2N0A) using molecular docking and molecular dynamics simulations. They report that hesperidin binds most strongly, reduces β-sheet content, disrupts interpeptide hydrogen bonding, and induces conformational changes that may inhibit amyloid aggregation. MM-PBSA and ADMET analyses are presented to support hesperidin as a lead anti-Parkinsonian polyphenol.
- **Visible evidence base** Docking binding energies (Fig. 1), docking poses and interaction diagrams (Figs. 2, 3; Table 1), RMSD (Fig. 4), SASA (Fig. 5), RMSF (Fig. 6), Rg (Fig. 7), hydrogen bond counts (Fig. 8), secondary structure content (Table 2; Fig. 9), PCA and FEL plots (Figs. 10, 11), MM-PBSA energy components (Table 3), and ADMET predictions (Table 4).
- **Missing materials affecting confidence** No simulation input files, force field parameter details for ligands, docking grid coordinates, convergence criteria, error bars on ensemble averages, or raw trajectory data are provided. No experimental validation is included. The manuscript states "Data will be made available on request," which limits reproducibility assessment.

## Reviewer
- **Overall assessment** The manuscript presents a straightforward computational screening workflow combining docking, MD simulation, and MM-PBSA analysis. The central claim that hesperidin is a potent inhibitor of α-synuclein aggregation is plausible but is supported only by in silico evidence, with several methodological ambiguities and internal inconsistencies that weaken the case. The study is descriptive rather than mechanistic, and the link between the observed simulation metrics and actual anti-amyloidogenic activity is asserted rather than demonstrated. The work may be of interest to the computational drug discovery community, but the current evidence base does not establish hesperidin as a validated lead compound.
- **Who would be interested in the results, and why** Computational chemists and structural biologists working on protein aggregation inhibitors, particularly those focused on Parkinson's disease and polyphenolic compounds. Researchers in natural product-based drug discovery may also find the ADMET profiling useful. The study may serve as a preliminary screen for experimental follow-up, but its impact is limited by the absence of experimental validation.
- **Major strengths** The study addresses a relevant and timely topic, namely the search for small-molecule inhibitors of α-synuclein aggregation. The use of multiple complementary computational techniques (docking, MD, MM-PBSA, ADMET) is appropriate for an initial screening effort. The comparison of three flavonoids under the same protocol is a reasonable design. The reporting of energy components in Table 3 and secondary structure changes in Table 2 provides useful quantitative detail.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (docking methodology), R1-M2 (simulation protocol), R1-M3 (interpretation of β-sheet changes), R1-M4 (MM-PBSA reporting), R1-M5 (ADMET interpretation).
- **Assessment against Nature-style criteria**  
  - **Originality** Limited. The application of hesperidin to α-synuclein has been explored in prior computational and experimental studies, and the general approach of flavonoid screening against amyloid proteins is well established. The study does not introduce a new method, a new target site, or a novel mechanistic hypothesis.  
  - **Scientific importance** Moderate. If validated experimentally, hesperidin could be a candidate for further development, but the current study does not provide evidence beyond in silico predictions, which are known to have limited predictive power for aggregation inhibitors.  
  - **Interdisciplinary readership** Narrow. The work is primarily of interest to computational biologists and medicinal chemists. The lack of experimental data limits its appeal to the broader neuroscience or clinical community.  
  - **Technical soundness** Weak. Several methodological details are missing or ambiguous, and some interpretations are not supported by the presented data. The simulation protocol has potential errors (see R1-M2), and the docking analysis lacks validation.  
  - **Readability for nonspecialists** Acceptable but improvable. The manuscript is generally readable, but some sections are verbose and contain redundant statements. The figures are not all clearly described, and the connection between computational metrics and biological outcomes is not explained for a general audience.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript requires substantial revision and additional analysis to support its claims. The authors should address the methodological concerns, provide clearer evidence for the anti-amyloidogenic mechanism, and temper the conclusions to match the in silico nature of the study.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that hesperidin has the best binding effectiveness with α-synuclein based on docking scores, and that the binding site is in aggregation-prone regions.
- **Evidence pointer** Fig. 1, Fig. 2, Fig. 3, Table 1
- **Concern** The docking methodology is not described in sufficient detail. The authors do not specify the docking software version beyond "AutoDock version 4.2.3", the search space dimensions, the grid box center, the number of runs, or the scoring function used. More critically, the docking was performed on a dimeric structure (PDB 2N0A), but the authors do not clarify which chains or which interface were used as the binding site. The choice of "aggregation-prone regions" as the binding site is mentioned but not defined or justified with reference to prior literature or structural analysis. Without this information, the docking results cannot be reproduced or evaluated.
- **Why it matters** Docking scores are highly sensitive to the search space and scoring function. If the binding site is not properly defined, the ranking of ligands may be arbitrary. The claim that hesperidin binds best is therefore not robustly supported.
- **Resolution test** The authors should provide a complete docking protocol, including grid box coordinates, search space dimensions, number of genetic algorithm runs, and the criteria for selecting the binding site. They should also validate the docking protocol by redocking a known ligand or comparing with experimental binding data if available.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors report MD simulation results (RMSD, RMSF, Rg, SASA, hydrogen bonding) over 250 ns and use these to claim that hesperidin destabilizes the α-synuclein structure and reduces β-sheet content.
- **Evidence pointer** Figs. 4-9, Table 2
- **Concern** The MD simulation protocol is described with several ambiguities and potential errors. The text states: "This was then followed by system equilibration for 10 ns in an NVT ensemble at a temperature of 310 K, with the number of particles, volume, and temperature being constant. Before this step, the systems were subjected to an unconstrained 250-ns MD simulation in NPT conditions." This sequence is contradictory. The 250-ns production run is described as occurring "before" the equilibration step, which is not a standard workflow. Additionally, the authors state that 35 Na+ and 27 Cl- ions were added to obtain a physiological concentration of 0.15 mM, but 0.15 mM is not physiological (physiological is approximately 150 mM). The ion count is also inconsistent with a typical simulation box size, suggesting a possible unit error. The force field used for the protein is not specified, and the ligand parameterization method is not described. These issues make the simulation results unreliable.
- **Why it matters** MD simulation results are only meaningful if the protocol is correctly designed and reported. The contradictory description of the simulation workflow and the incorrect salt concentration suggest a lack of rigor. The results cannot be trusted without clarification.
- **Resolution test** The authors should provide a corrected and complete MD protocol, including the force field, water model, ion concentration (with correct units), equilibration and production phases in the correct order, and the method for ligand parameterization. They should also state the total simulation time and the number of replicates.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim-evidence alignment
- **Claim pointer** The authors claim that hesperidin reduces β-sheet content from 35% to 29%, and interpret this as evidence of anti-amyloidogenic activity.
- **Evidence pointer** Table 2, Fig. 9
- **Concern** The secondary structure analysis is presented as a single percentage value per system, with no error estimates or time evolution. The DSSP analysis is typically performed over the entire trajectory, and the reported values should be averaged over time with standard deviations. The authors do not specify whether the percentages are averaged over the last frame, over the entire trajectory, or over a specific time window. Furthermore, the Ramachandran plots in Fig. 9 are described as "secondary structure content Ramachandran plot," which is not a standard representation. Ramachandran plots show the distribution of phi/psi angles, not secondary structure content. The figure legend is unclear, and the figure itself is not described in the text. The claim that a 6% reduction in β-sheet content is biologically meaningful is not supported by any statistical analysis.
- **Why it matters** The reduction in β-sheet content is a central piece of evidence for the anti-amyloidogenic claim. If the analysis is not properly performed or reported, the claim is not supported.
- **Resolution test** The authors should provide time-averaged secondary structure percentages with standard deviations, and clarify the methodology. The Ramachandran plots should be properly labeled and described, or removed if they do not add information.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors report MM-PBSA binding free energies (ΔE binding) of −92.69, −83.95, and −77.54 kJ/mol for hesperidin, morin, and myricetin, respectively, and use these to rank the ligands.
- **Evidence pointer** Table 3
- **Concern** The MM-PBSA calculation is described in a single sentence with no methodological detail. The authors do not specify the number of frames used for the calculation, the dielectric constants, the solvent probe radius, or whether entropy contributions were included. The reported values are presented as "ΔE binding," which is ambiguous. MM-PBSA typically reports a free energy (ΔG), not just an energy (ΔE). The authors also do not provide standard deviations for the energy components, despite reporting values with ± signs. The lack of detail makes the results impossible to evaluate or reproduce.
- **Why it matters** MM-PBSA results are highly sensitive to the choice of parameters and the number of frames. Without this information, the ranking of ligands based on binding free energy is not reliable.
- **Resolution test** The authors should provide a complete description of the MM-PBSA protocol, including the number of frames, the dielectric constants, the entropy calculation method (if any), and the standard deviations of the reported values.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim-evidence alignment
- **Claim pointer** The authors state that hesperidin "may be a promising treatment option" for Parkinson's disease based on the computational results.
- **Evidence pointer** Conclusions section
- **Concern** The conclusion overreaches the evidence. The study is purely computational, with no experimental validation of the predicted binding or anti-aggregation activity. The authors themselves acknowledge that "there is no experimental evidence for such flavonoid-protein interactions." The claim that hesperidin is a "potent" inhibitor is not supported by the data, as the docking scores and MM-PBSA energies are not calibrated against any known inhibitor or experimental binding affinity. The conclusion should be tempered to reflect the preliminary, in silico nature of the study.
- **Why it matters** Overstated conclusions can mislead readers and are not appropriate for the level of evidence provided.
- **Resolution test** The authors should revise the conclusions to clearly state that the findings are computational predictions that require experimental validation.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states "ΔE binding −92.69 ± 0.31 kJ mol−1" but the units are inconsistent with the docking score reported earlier in the same paragraph (6.58 kcal/mol). The reader is left to convert units manually.
- **Required correction** Use consistent units throughout the abstract, or clearly state the conversion.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Computational methods section
- **Issue** The authors state that the α-synuclein structure was "optimized and refined" using GROMACS, but no details are provided on the energy minimization protocol, the force field, or the criteria for convergence.
- **Required correction** Provide a brief description of the minimization protocol, including the force field and the number of steps.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results and discussion
- **Evidence pointer** Section "PD-associated α-synuclein and flavonoid-based therapeutic potential"
- **Issue** The text states "The more the drug or ligand exerts control over its bound target, the more effectively the drug and protein bond." This sentence is vague and not scientifically precise.
- **Required correction** Rephrase to describe the relationship between binding affinity and inhibitory activity more accurately.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Fig. 9
- **Evidence pointer** Fig. 9
- **Issue** The figure legend describes "secondary structure content Ramachandran plot," which is not a standard representation. The figure appears to show Ramachandran plots, but the relationship to secondary structure content is unclear.
- **Required correction** Clarify the figure legend and describe what is shown in the figure.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** ADMET section
- **Evidence pointer** Table 4
- **Issue** The ADMET table includes a parameter "Caco2 permeability" with a value of 0.505 for hesperidin, but the units are not specified. The text also does not interpret the ADMET results in the context of drug-likeness.
- **Required correction** Specify units for all ADMET parameters and add a brief interpretation of the results.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Language
- **Affected element** Throughout
- **Evidence pointer** Entire manuscript
- **Issue** The manuscript contains several grammatical errors and awkward phrasings, e.g., "A significant part of amyloidogenic illnesses is played by protein misfolding" and "The initial data from MD simulations strongly suggest that flavonoids like Morin, Myricetin and Hesperidin interfered with the native conformational structure of α-synuclein."
- **Required correction** The manuscript should be carefully edited for grammar and clarity.

## Risk / unsupported claims
- The claim that hesperidin is a "potent" inhibitor of α-synuclein aggregation is unsupported by the evidence, as no experimental validation or comparison to known inhibitors is provided.
- The claim that hesperidin "destabilizes the native aggregation-prone α-syn structure" is based on MD simulations with a potentially flawed protocol (see R1-M2) and is not statistically validated.
- The claim that the reduction in β-sheet content (35% to 29%) is biologically meaningful is unsupported, as no error estimates or statistical analysis are provided.
- The ADMET predictions are presented as favorable, but the authors do not compare them to any reference compounds or discuss their implications for drug development.
- The statement that "hesperidin may be a promising treatment option" for Parkinson's disease is an overreach given the purely computational nature of the study.
- The manuscript states "Data will be made available on request," which limits the ability of reviewers and readers to verify the results.