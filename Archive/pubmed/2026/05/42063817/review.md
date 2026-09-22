## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusion, methods) as provided
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by presented evidence; no assessment of editorial fit or publication decision
- **Shared manuscript claim summary** The authors use PPI-GaMD simulations to characterize dissociation pathways of three AF9-binding peptides (BCOR, CBX8, DOT1L) and propose that sequence-encoded hydrophobic and electrostatic features govern differential binding affinities and dissociation mechanisms, with implications for inhibitor design in MLL-rearranged leukemia
- **Visible evidence base** Main text figures (referenced but not all visible), tables (referenced), supplementary figures and tables (referenced but not provided), MM-GBSA calculations, PPI-GaMD simulation trajectories, clustering analyses, pocket detection
- **Missing materials affecting confidence** Supplementary figures and tables (S1–S21, Tables S1–S13) are referenced but not provided; specific figure panels are cited without visible data; methodological details for MM-GBSA and reweighting are deferred to supplementary methods; no simulation input files or parameter details are included

## Reviewer
- **Overall assessment** The manuscript presents a computational study of AF9-peptide dissociation mechanisms using PPI-GaMD, a method appropriate for studying protein-peptide unbinding. The work addresses a relevant question in MLL-rearranged leukemia biology. However, the manuscript as provided has significant limitations: key data are in inaccessible supplementary materials, convergence and validation evidence is described rather than shown, and several claims extend beyond what the presented evidence can support. The central mechanistic conclusions may be sound, but the current presentation does not allow full verification.
- **Who would be interested in the results, and why** Researchers studying MLL-rearranged leukemias, particularly those interested in the AF9 interaction network as a therapeutic target; computational biophysicists working on protein-protein/peptide dissociation mechanisms and enhanced sampling methods; structural biologists studying YEATS domain proteins and their complexes; drug discovery groups targeting transcriptional complexes in leukemia
- **Major strengths** 1) Addresses a clinically relevant and mechanistically important question about AF9-partner dissociation; 2) Uses an appropriate enhanced sampling method (PPI-GaMD) designed for protein-peptide unbinding; 3) Compares three peptide partners of equal length, enabling systematic analysis of sequence determinants; 4) Integrates multiple analysis approaches (MM-GBSA, FELs, clustering, pocket detection); 5) Acknowledges limitations of the reduced peptide model and single-structure starting point
- **Major Concerns** See detailed items below
- **Minor Comments** See detailed items below
- **Technical failings that need to be addressed before the case is established** R1-M1 (validation of method against experimental data), R1-M2 (convergence evidence), R1-M3 (accessibility of key data), R1-M4 (statistical treatment of replicates)
- **Assessment against Nature-style criteria** Originality: moderate; the application of PPI-GaMD to AF9 partners is novel, but the conceptual framework (sequence-encoded binding determinants) is not new. Scientific importance: potentially high for the leukemia field, but the advance is incremental and computational. Interdisciplinary readership: limited; the work is primarily of interest to computational biophysicists and leukemia biologists. Technical soundness: cannot be fully assessed from the provided material; key validation and convergence data are missing. Readability for nonspecialists: the main text is generally clear, but the heavy reliance on supplementary material and specialized terminology limits accessibility.
- **Recommendation posture** Supportive if technical concerns are resolved; the core approach is appropriate and the question is relevant, but the evidence as presented is insufficient to fully establish the mechanistic claims

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / validation
- **Claim pointer** The manuscript claims that PPI-GaMD simulations "revealed" dissociation mechanisms and that the relative binding affinities from MM-GBSA are "consistent with experimental evidence" (Results section, first subsection)
- **Evidence pointer** Results and Discussion, first subsection; Methods, PPI-GaMD Simulations section; Figure 1 (referenced); Table 1 (referenced)
- **Concern** The manuscript does not provide a direct quantitative comparison between simulated and experimental binding affinities. The text states that MM-GBSA results are "consistent with experimental evidence" but no numerical comparison, correlation analysis, or statistical test is presented. Furthermore, the validation of PPI-GaMD parameters (σOP = 1.2, σOD = 6.0 kcal/mol) is not justified with reference to experimental data for these specific systems. The claim that the simulations reproduce the experimental binding hierarchy (DOT1L > CBX8 > BCOR) requires explicit demonstration, not just qualitative assertion.
- **Why it matters** The central conclusion of the paper depends on the reliability of the computational predictions. Without quantitative validation against experimental binding data, the mechanistic interpretations and the proposed binding hierarchy cannot be considered established. The choice of PPI-GaMD parameters directly affects the accuracy of the free energy surfaces and dissociation pathways.
- **Resolution test** Provide a quantitative comparison of MM-GBSA ΔG values with experimental KD values (e.g., a table with both sets of values and a correlation coefficient). Justify the choice of σOP and σOD parameters with reference to experimental binding data or systematic parameter testing. If possible, show that the simulated binding free energy ranking matches experimental ranking across all three peptides.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / convergence
- **Claim pointer** The manuscript claims that "five independent 500 ns PPI-GaMD simulations were performed for each AF9-peptide complex" and that the resulting FELs reveal distinct dissociation pathways and intermediate states
- **Evidence pointer** Methods, PPI-GaMD Simulations section; Results, subsections on each peptide; Table S8 (referenced); Figures S1–S3, S7–S9, S12–S14 (referenced)
- **Concern** The manuscript states that "block averaging of the center-of-mass distance across independent PPI-GaMD replicas shows that several trajectories stabilize at similar intermediate separations" but does not present the block-averaging data or convergence metrics. For enhanced sampling simulations, demonstrating convergence is essential; without it, the FELs and identified intermediates may be artifacts of insufficient sampling. The text also acknowledges that "the FELs for AF9-DOT1L are not fully converged" but does not specify the extent of non-convergence or its impact on the conclusions.
- **Why it matters** The identification of metastable intermediates and the proposed dissociation pathways are the primary mechanistic claims. If the simulations are not converged, the specific intermediates and their relative populations may not be reliable, undermining the mechanistic interpretations and the proposed druggable conformations.
- **Resolution test** Present the block-averaging data (e.g., plots of mean and standard deviation of key observables as a function of simulation time) for all three systems. Show that the FELs are stable with respect to simulation length, or clearly state the limitations and how they affect the conclusions. If possible, extend simulations or provide additional replicates to demonstrate convergence of the key features.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence accessibility
- **Claim pointer** The manuscript makes numerous specific claims about intermediate states, residue-residue contacts, pocket properties, and interaction energies that are supported by supplementary figures and tables
- **Evidence pointer** Throughout Results and Discussion; Supplementary Figures S1–S21; Supplementary Tables S1–S13
- **Concern** The manuscript relies heavily on supplementary material that was not provided for review. Key evidence for the dissociation pathways (Figures S1–S3, S7–S9, S12–S14), interaction maps (Figures S4, S10, S15–S16), structural comparisons (Figure S20), and quantitative data (Tables S1–S13) is inaccessible. Without these materials, the specific claims about intermediate states, residue-level interactions, and pocket properties cannot be verified.
- **Why it matters** The core findings of the paper are presented in the supplementary material. The main text provides summaries and interpretations, but the actual data supporting these interpretations is not available for assessment. This prevents verification of the claims and limits the ability to assess the robustness of the conclusions.
- **Resolution test** Provide the supplementary material for review. Ensure that all figures and tables referenced in the main text are included and that the data presented in the main text is fully supported by the supplementary information.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor
- **Claim pointer** The manuscript claims that "five independent 500 ns PPI-GaMD simulations were performed for each AF9-peptide complex" and uses these to characterize dissociation pathways and intermediate states
- **Evidence pointer** Methods, PPI-GaMD Simulations section; Results, subsections on each peptide
- **Concern** The manuscript does not report statistical measures of variability across the five independent simulations. For example, the FELs are presented as combined or representative, but the variability of key observables (e.g., COM distance, native contacts, intermediate populations) across replicates is not quantified. The clustering analysis is performed on concatenated trajectories, which may obscure replicate-to-replicate variability.
- **Why it matters** The reproducibility of the dissociation pathways and intermediate states across independent simulations is critical for the reliability of the conclusions. Without measures of variability, it is unclear whether the identified features are robust or specific to particular trajectories.
- **Resolution test** Report the mean and standard deviation (or other appropriate statistics) of key observables across the five replicates. Show that the identified intermediate states and dissociation pathways are consistently observed across replicates, or discuss the variability and its implications.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity / reproducibility
- **Affected element** Methods, PPI-GaMD Simulations section
- **Evidence pointer** Methods section, "PPI-GaMD Simulations" subsection
- **Issue** The manuscript states that "the σOP and σOD parameters were set to 1.2 and 6.0 kcal/mol, respectively" but does not explain how these values were chosen or whether they were optimized for these specific systems. The choice of these parameters can significantly affect the simulation results.
- **Required correction** Provide a brief justification for the chosen σOP and σOD values, or cite the original PPI-GaMD methodology paper and explain how the values were adapted for these systems.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Internal consistency
- **Affected element** Results, first subsection (MM-GBSA Analysis)
- **Evidence pointer** Results and Discussion, first subsection; Table 1 (referenced)
- **Issue** The text states that "the total binding free energy was predominantly driven by van der Waals and electrostatic interactions" but the relative contributions of these two components are not quantified in the main text. The text also mentions "a modest favorable contribution from nonpolar solvation energy" without providing specific values.
- **Required correction** Provide the numerical values for the energy components (van der Waals, electrostatic, polar solvation, nonpolar solvation) for each complex, either in the main text or in a table, to support the qualitative statements.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity / interpretation
- **Affected element** Results, subsection on DOT1L dissociation
- **Evidence pointer** Results and Discussion, "FELs Indicate Strong Binding of DOT1L Peptide" subsection
- **Issue** The text states that "the FELs for AF9-DOT1L are not fully converged" but then proceeds to draw conclusions about the dissociation mechanism and intermediate states. This creates tension between the acknowledged limitation and the strength of the subsequent claims.
- **Required correction** Clarify the extent of non-convergence and explicitly state which conclusions are robust despite this limitation and which should be considered preliminary. Alternatively, provide additional evidence of convergence.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods, Simulation Analysis section
- **Evidence pointer** Methods, "Simulation Analysis" subsection
- **Issue** The manuscript mentions that "the binding free energies of the three AF9 complexes were calculated with the MM-GBSA method (see Supplementary methods)" but the main text does not describe the MM-GBSA protocol, including the number of frames used, the dielectric constant, or the entropy treatment.
- **Required correction** Provide a brief description of the MM-GBSA protocol in the main text or ensure that the supplementary methods contain all necessary details for reproducibility.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interpretation / overstatement
- **Affected element** Conclusion section
- **Evidence pointer** Conclusion, final paragraph
- **Issue** The conclusion states that the study "provides the first atomistic description of AF9-partner dissociation." While this may be true, the claim of "first" is difficult to verify and is not essential to the scientific contribution. Additionally, the statement that the findings "establish a rational computational framework for the design of selective peptide or covalent inhibitors" is somewhat overstated given the computational nature of the study and the lack of experimental validation of the proposed druggable pockets.
- **Required correction** Soften the "first" claim or provide a literature search to support it. Temper the statement about inhibitor design to reflect that the proposed pockets are computational predictions requiring experimental validation.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Methods, Classical Molecular Dynamics Simulations section
- **Evidence pointer** Methods, "Classical Molecular Dynamics Simulations" subsection
- **Issue** The manuscript states that simulations were performed at 303.15 K for the classical MD equilibration but at 310 K for the PPI-GaMD simulations. The reason for this temperature difference is not explained.
- **Required correction** Briefly explain the choice of different temperatures for the classical MD and PPI-GaMD simulations, or justify why the temperature difference does not affect the conclusions.

## Risk / unsupported claims
- The claim that MM-GBSA results are "consistent with experimental evidence" is not quantitatively supported; no numerical comparison is provided.
- The claim that "five independent 500 ns PPI-GaMD simulations" provide reliable FELs is not supported by convergence data, which are referenced but not shown.
- The claim that specific intermediate states represent "druggable conformations" is speculative; no binding or screening calculations are presented to support druggability.
- The claim that the dissociation mechanism for DOT1L is "likely representative of AF4-AF9 unbinding" is an extrapolation not directly tested in this study.
- The claim that the study provides "the first atomistic description of AF9-partner dissociation" is unverifiable from the provided material.
- The specific pocket properties (druggability scores, volumes) are reported in the text but the underlying data is in inaccessible supplementary figures.
- The statement that "the overall interfacial contact pattern remained stable" in the bound state during PPI-GaMD simulations is not supported by visible quantitative data.