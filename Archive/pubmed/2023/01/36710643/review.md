## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, computational methods, and supplementary figure references.
- **Assessment boundary** Evaluation is limited to the scientific content, methodology, and claims presented in the provided manuscript. No external data or unpublished materials were consulted.
- **Shared manuscript claim summary** The authors use molecular dynamics simulations to characterize the binding of tau K19 to acidic POPC/POPS membranes, identifying three amphipathic helices that anchor the protein to the membrane. They report partial mimicry between tau's membrane binding and its microtubule binding, particularly involving conserved Lys and Val residues, and propose that this mimicry facilitates membrane-mediated microtubule anchoring and tau transfer.
- **Visible evidence base** Figures 1–5, supplementary figures S1–S2, and computational methods section. Experimental validation is drawn from published EPR (Georgieva et al., 2014) and solid-state NMR (Kunze et al., 2012) data, as well as the cryo-EM structure of the tau-microtubule complex (PDB 7PQC).
- **Missing materials affecting confidence** Raw simulation trajectories, force field parameter files, input coordinates, and convergence analyses are not provided. The manuscript states that raw data are available upon request, but this cannot be independently verified. Additionally, the cryo-EM structure used for comparison is referenced but not analyzed in detail within the provided text.

## Reviewer
- **Overall assessment** This manuscript presents a well-structured computational study of tau K19 binding to acidic membranes, with careful validation against published experimental data. The identification of three amphipathic helices and the partial mimicry with microtubule binding is a novel and biologically relevant finding. However, several technical aspects of the simulations, including force field choice, sampling convergence, and the interpretation of the mimicry, require further scrutiny before the conclusions can be fully accepted.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, tau biology, membrane-protein interactions, and neurodegenerative disease mechanisms would find this work relevant. The study also contributes to the broader understanding of how IDPs achieve binding specificity across multiple negatively charged surfaces, which is of interest to the biophysics and computational chemistry communities.
- **Major strengths** The study addresses an important and under-explored question regarding tau's dual binding to membranes and microtubules. The use of multiple complementary analyses (Z tip, contact probabilities, DEER distance comparisons) strengthens the characterization. The validation against published EPR and NMR data is a significant asset, lending credibility to the simulation results. The proposed biological implications, particularly regarding tau transfer between membranes and microtubules, are thought-provoking and well contextualized.
- **Major Concerns** The concerns below focus on the robustness of the simulation methodology, the interpretation of the mimicry, and the strength of the conclusions relative to the evidence provided.
- **Minor Comments** Several minor issues regarding clarity, figure presentation, and methodological details are noted.
- **Technical failings that need to be addressed before the case is established** R1-M1 (force field and water model choice), R1-M2 (sampling convergence), R1-M3 (interpretation of partial mimicry), R1-M4 (generalizability of findings).
- **Assessment against Nature-style criteria**  
  - *Originality*: The concept of partial mimicry between tau's membrane and microtubule binding is novel and not previously reported. This is a fresh perspective on tau's multifunctionality.  
  - *Scientific importance*: The findings have implications for understanding tau's physiological roles and pathological aggregation, which is a topic of high importance in neurodegeneration research.  
  - *Interdisciplinary readership*: The work bridges computational biophysics, membrane biology, and neurobiology, making it accessible to a broad audience. However, the heavy reliance on simulation details may limit accessibility for experimentalists.  
  - *Technical soundness*: The methodology is generally sound, but concerns about force field accuracy, sampling convergence, and the interpretation of the mimicry need to be addressed.  
  - *Readability for nonspecialists*: The manuscript is clearly written, but the results section assumes familiarity with MD simulation concepts and EPR/NMR techniques. A brief primer or more contextual explanation would improve accessibility.
- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are interesting and potentially significant, but the current evidence does not fully establish the robustness of the simulation results or the strength of the mimicry claim.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors state that the MD simulations "show that three amphipathic helices, one in each repeat, stably bind to the membrane" and that the results are validated by EPR data.  
- **Evidence pointer** Computational Methods section, Figures 2–4, Figure S1.  
- **Concern** The choice of the ff14SB force field and TIP4P-D water model, while reasonable, is not justified in the context of membrane-protein simulations. The authors do not discuss whether these parameters accurately reproduce lipid-protein interactions, particularly for charged lipid headgroups like POPS. Additionally, the use of a 12.0 Å cutoff for nonbonded interactions may introduce artifacts in long-range electrostatic interactions, which are critical for membrane binding.  
- **Why it matters** Force field inaccuracies can lead to incorrect binding orientations, depths of insertion, and interaction energies, which would undermine the central claims of the study. The validation against EPR data is encouraging, but it does not guarantee that all aspects of the simulation are accurate.  
- **Resolution test** The authors should provide a justification for the force field and water model choices, possibly with reference to benchmark studies. They should also test the sensitivity of their results to the cutoff distance and, if feasible, perform a short simulation with an alternative force field (e.g., CHARMM36) to confirm the robustness of the findings.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors claim that the three amphipathic helices "stably bind" to the membrane, and they report distance distributions and contact probabilities as evidence.  
- **Evidence pointer** Figures 3–5, Computational Methods section.  
- **Concern** The simulation lengths (600–1300 ns) may be insufficient to achieve convergence for a system of this size, particularly for an IDP that undergoes large conformational fluctuations. The authors do not provide any convergence analysis, such as block averaging or time-dependent drift of key observables. Without such analysis, it is unclear whether the reported distance distributions and contact probabilities are representative of the equilibrium ensemble.  
- **Why it matters** If the simulations are not converged, the quantitative comparisons to EPR data and the conclusions about binding stability and mimicry may be unreliable.  
- **Resolution test** The authors should provide a convergence analysis, such as plotting the time evolution of Z tip values, contact probabilities, or distance distributions, and demonstrate that these quantities have reached a plateau. They could also consider extending one or more simulations to longer timescales to confirm stability.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** No  
- **Axis** Interpretation of results  
- **Claim pointer** The authors propose that "partial mimicry facilitates both the membrane anchoring of microtubules by tau and the transfer of tau from membranes to microtubules."  
- **Evidence pointer** Discussion section, Figures 2 and 5.  
- **Concern** The concept of "partial mimicry" is based on similarities in the interactions of conserved Lys and Val residues with membranes and microtubules. However, the manuscript does not provide a quantitative comparison of the interaction energies or contact patterns between the two systems. The claim that this mimicry "facilitates" anchoring and transfer is speculative and not directly tested.  
- **Why it matters** The biological implications are a key selling point of the manuscript, but they are not supported by direct evidence. Overstating the functional significance of the mimicry could mislead readers.  
- **Resolution test** The authors should either temper the language in the discussion or provide additional analysis, such as comparing the interaction energies of the conserved residues in both systems, or discussing how the mimicry could be tested experimentally (e.g., via mutagenesis).

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Generalizability  
- **Claim pointer** The authors state that "the three amphipathic helices, along with flanking residues, tether the protein to the membrane interface" and imply that this is a general mechanism for tau-membrane binding.  
- **Evidence pointer** Results section, Figures 2 and 4.  
- **Concern** The study uses a single lipid composition (POPC/POPS 1:1) and a single tau construct (K19). It is unclear whether the findings would hold for other physiologically relevant membrane compositions (e.g., with different anionic lipid fractions) or for other tau isoforms. The authors do not discuss the potential variability in binding behavior.  
- **Why it matters** The conclusions are presented as general features of tau-membrane interactions, but the evidence is limited to one specific condition. This limits the broader applicability of the findings.  
- **Resolution test** The authors should acknowledge this limitation and discuss how the results might vary with different lipid compositions or tau constructs. They could also suggest future simulations to test these variables.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Figure 1  
- **Evidence pointer** Figure 1a,b.  
- **Issue** The figure legend does not clearly explain the color coding or the significance of the underlined residues.  
- **Required correction** Add a clear legend explaining the color scheme and the meaning of the underlines.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Computational Methods section  
- **Evidence pointer** Computational Methods section.  
- **Issue** The manuscript states that "raw data from molecular dynamics simulations are available from the corresponding author upon reasonable request," but this is not a standard data availability statement for a computational study.  
- **Required correction** Provide a more detailed data availability statement, including where the simulation inputs and analysis scripts can be accessed (e.g., a repository like Zenodo or GitHub).

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Presentation  
- **Affected element** Figure 5  
- **Evidence pointer** Figure 5a,b.  
- **Issue** The comparison between membrane contact probabilities and microtubule contact numbers is presented in separate panels, making it difficult to directly compare the two.  
- **Required correction** Consider overlaying the two datasets in a single plot or using a combined figure to facilitate direct comparison.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Terminology  
- **Affected element** Abstract and Discussion  
- **Evidence pointer** Abstract, Discussion section.  
- **Issue** The term "partial mimicry" is used without a precise definition. It is unclear whether this refers to structural mimicry, energetic mimicry, or functional mimicry.  
- **Required correction** Define "partial mimicry" explicitly in the introduction or discussion, and clarify which aspects of binding are being compared.

## Risk / unsupported claims
- The claim that "partial mimicry facilitates both the membrane anchoring of microtubules by tau and the transfer of tau from membranes to microtubules" is speculative and not directly tested in this study.
- The assertion that the three amphipathic helices "stably bind" to the membrane is not supported by a formal convergence analysis of the simulations.
- The generalizability of the findings to other lipid compositions or tau isoforms is not established, as only one condition was tested.
- The comparison between membrane binding and microtubule binding is qualitative; no quantitative metrics (e.g., interaction energies) are provided to support the mimicry claim.