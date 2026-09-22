## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, data/code availability, supporting information list)
- **Assessment boundary** Scientific validity, methodological soundness, novelty, clarity, and consistency of claims relative to the provided evidence
- **Shared manuscript claim summary** The authors present CoVAMPnet, a computational framework combining VAMPnet-based Markov state models with optimal transport alignment and gradient-based feature interpretation, to compare conformational ensembles of disordered biomolecules with and without drug candidates. Applied to Aβ42 with TMP and SPA, the framework predicts that both ligands, especially SPA, stabilize α-helical conformations and reduce β-strand propensity, with partial experimental validation via CD, FTIR, NMR, and ThT assays.
- **Visible evidence base** Methods descriptions for MD simulations, VAMPnet training, alignment, and gradient analysis; results on secondary structure content, radius of gyration, MSM kinetics, molecular interactions, and experimental validation; figures referenced but not shown; supplementary materials listed but not provided
- **Missing materials affecting confidence** All figures and supplementary materials (figures S1-S31, tables S1-S3, notes 1-10) are referenced but not included; no numerical data tables in the main text; no convergence metrics for the VAMPnet training or alignment; no details on the experimental protocols beyond brief descriptions

## Reviewer
- **Overall assessment** This manuscript presents a potentially useful methodological contribution in the form of CoVAMPnet, which extends VAMPnet-based MSM analysis with cross-system alignment and gradient-based interpretability. The application to Aβ42 with TMP and SPA is timely and relevant. However, the main text as provided is insufficient to fully evaluate the technical soundness of the new methods, and several claims appear stronger than the visible evidence supports. The experimental validation is partial and, in some cases, appears to contradict the computational predictions, which the authors acknowledge but do not fully resolve. The manuscript would benefit from clearer presentation of the methodological novelty, more rigorous validation of the alignment and gradient approaches, and a more balanced discussion of the discrepancies between computation and experiment.
- **Who would be interested in the results, and why** Researchers in computational biophysics and drug discovery, particularly those studying intrinsically disordered proteins and peptides, would be interested in the CoVAMPnet framework as a tool for comparing conformational ensembles across different conditions. The application to Aβ42 and Alzheimer's disease-related drug candidates would also attract researchers in neurodegeneration and amyloid biology. Methodologists working on Markov state models, deep learning for molecular dynamics, and optimal transport applications in biophysics would find the methodological contributions relevant.
- **Major strengths** The manuscript addresses a genuine gap in the field, namely the lack of methods for aligning and comparing MSMs across different systems. The combination of optimal transport for alignment and gradient-based feature importance is conceptually elegant and leverages the differentiability of neural network-based MSMs. The application to a clinically relevant system (Aβ42 with phase 3 drug candidates) adds practical significance. The authors are transparent about the limitations of conventional MSM approaches and provide a clear rationale for using VAMPnets. The inclusion of multiple experimental techniques for validation, even if results are mixed, is commendable.
- **Major Concerns** The concerns below detail issues with methodological validation, claim support, and presentation.
- **Minor Comments** The minor comments below address clarity and presentation issues.
- **Technical failings that need to be addressed before the case is established** R1-M1 (alignment method validation), R1-M2 (gradient interpretation validation), R1-M3 (computational-experimental discrepancy), R1-M4 (generalizability claim)
- **Assessment against Nature-style criteria** Originality: The CoVAMPnet framework is original in its specific combination of elements, though each component (VAMPnets, optimal transport, gradient-based interpretation) exists separately. The novelty is incremental rather than paradigm-shifting. Scientific importance: The application to Aβ42 and drug candidates is important, but the conclusions are limited by the partial experimental validation and the acknowledged discrepancies. The methodological contribution could be important if rigorously validated, but the current evidence is insufficient. Interdisciplinary readership: The work bridges computational biophysics, machine learning, and drug discovery, which could appeal to a broad audience. However, the technical depth may limit accessibility to non-specialists. Technical soundness: The methods are described in sufficient detail to be reproducible, but the lack of validation metrics and the absence of figures and supplementary data prevent a full assessment of technical soundness. Readability for nonspecialists: The manuscript is generally well-written, but the methods section assumes significant familiarity with MSMs, VAMPnets, and optimal transport. The abstract and introduction are accessible, but the results and discussion require specialized knowledge.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a potentially valuable contribution, but the current evidence does not fully establish the validity of the new methods or the strength of the biological conclusions. Major revisions are required.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological validation
- **Claim pointer** The alignment method based on optimal transport is claimed to be a novel and useful approach for comparing MSMs across different systems, and the authors state that it "proved useful in quantifying the similarities and differences in Aβ42 conformations in response to the presence or absence of the small molecules."
- **Evidence pointer** Methods section "Comparative Markov State Analysis (CoVAMPnet)", Results section "Conformational analysis of ligand effects using Markov state models", Supplementary Figures S19
- **Concern** The alignment method is a central methodological contribution, but the main text provides no validation of its accuracy or robustness. The threshold T_e = 6 is described as "selected empirically," but no justification is given for this value, and no sensitivity analysis is presented. It is unclear how the alignment results would change with different thresholds, different numbers of states, or different initializations of the VAMPnet training. The authors do not compare their alignment method to any alternative approach, such as simple clustering of concatenated trajectories or alignment based on structural similarity. Without such validation, it is difficult to assess whether the alignment produces biologically meaningful correspondences or is an artifact of the optimization procedure.
- **Why it matters** The alignment of states across systems is the foundation for all subsequent comparative claims. If the alignment is unreliable, the conclusions about which states are preserved, which are new, and how the ligands alter the conformational landscape are not trustworthy. The method must be shown to be robust and to produce alignments that are consistent with independent structural or dynamical criteria.
- **Resolution test** The authors should provide a validation of the alignment method, including: (1) a sensitivity analysis of the threshold T_e, (2) a comparison with alternative alignment approaches, (3) a demonstration that aligned states share similar structural features (e.g., secondary structure content, contact maps) beyond the alignment cost, and (4) an assessment of the stability of the alignment across different VAMPnet training runs and different numbers of states.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological validation
- **Claim pointer** The gradient-based analysis is claimed to provide "interpretability and biophysical context to the learned MSMs" and to identify "the directional importance of inter-residue distances for the assignment to different conformational states."
- **Evidence pointer** Methods section "Comparative Markov State Analysis (CoVAMPnet)", Results section "Conformational analysis of ligand effects using Markov state models", Figures 3, Supplementary Figures S22-S23
- **Concern** The gradient-based feature importance method is presented as a novel contribution, but the main text does not explain how the gradients are aggregated across the ensemble of models, how the significance of the gradient values is assessed, or how the results are validated. The authors state that "the consistently red or blue color of the two subdiagonals closest to the white diagonal" indicates the presence or absence of helices, but this interpretation is not quantitatively supported. It is unclear whether the gradient patterns are stable across different training runs, whether they are sensitive to the choice of input features, or whether they correlate with known structural features of Aβ42. The claim that the gradient analysis "was able to pinpoint similar conformational events as the ones captured by NMR" is based on a qualitative comparison and lacks statistical rigor.
- **Why it matters** The gradient analysis is presented as a key advantage of the CoVAMPnet framework, providing interpretability that conventional MSMs lack. If the gradient results are not robust or not quantitatively validated, this claimed advantage is not established. The comparison with NMR data is a potentially powerful validation, but it needs to be made more rigorous.
- **Resolution test** The authors should provide a detailed description of the gradient aggregation procedure, an assessment of the variability of gradients across models and training runs, and a quantitative comparison between the gradient-identified important residues and the NMR-identified perturbed residues. Statistical measures of agreement (e.g., overlap coefficients, correlation) should be reported.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim-evidence consistency
- **Claim pointer** The abstract states that "both TMP and SPA preserved more structured conformations of Aβ42" and that "SPA impacted Aβ42 more than TMP, protecting α-helices and suppressing the formation of aggregation-prone β-strands." The discussion claims that the computational results "suggested that TMP and SPA may affect the conformational equilibrium of Aβ42 in the brain and prolong its monomeric soluble state."
- **Evidence pointer** Results sections "Secondary structure content in simulations of free Aβ42 and Aβ42 with ligands" and "Conformational analysis of ligand effects using Markov state models", Experimental validation section, Figures 1, 2, 5
- **Concern** The computational predictions of increased α-helix content and decreased β-strand content in the presence of ligands are not consistently supported by the experimental data. The CD spectroscopy results show no major changes in secondary structure upon ligand addition, and the FTIR results are described as showing only subtle changes. The NMR results show small CSPs for SPA but not for TMP. The ThT assay shows no significant effect on fibril formation. The authors acknowledge these discrepancies but attribute them to differences in time scales and concentrations. While this is a plausible explanation, it means that the experimental validation does not confirm the computational predictions. The claim that the ligands "preserved more structured conformations" is therefore not directly supported by the experimental evidence presented.
- **Why it matters** The biological conclusions are the primary motivation for the study. If the experimental data do not confirm the computational predictions, the significance of the findings is weakened. The authors need to either provide stronger experimental evidence or temper their claims to reflect the level of support.
- **Resolution test** The authors should either (1) provide additional experimental data that more directly test the computational predictions, such as NMR-derived secondary structure propensities in the presence of ligands, or (2) revise the claims to clearly state that the computational predictions are not fully confirmed by the experimental results and discuss the possible reasons for the discrepancies in more detail.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The discussion states that "The CoVAMPnet method is broadly applicable to study the effects of drug candidates on the conformational behavior of intrinsically disordered biomolecules."
- **Evidence pointer** Discussion section
- **Concern** The generalizability claim is based on a single application to one peptide (Aβ42) with two related ligands (TMP and SPA). While the method is conceptually general, the authors do not discuss potential limitations or challenges that might arise when applying it to other systems. For example, the choice of input features (inter-residue distances), the number of states, the alignment threshold, and the interpretation of gradients may all need to be adapted for different systems. The authors also do not discuss the computational cost of the method or its scalability to larger proteins or longer simulations.
- **Why it matters** A claim of broad applicability should be supported by a discussion of the method's limitations and the conditions under which it is likely to work or fail. Without this, the claim is speculative.
- **Resolution test** The authors should add a discussion of the method's limitations, including potential challenges for other systems, computational cost, and the need for parameter tuning. They should also consider demonstrating the method on a second, distinct system to strengthen the generalizability claim.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the framework "quantify changes in the conformational distribution and dynamics" but does not specify what quantitative metrics are used. The term "quantify" is vague.
- **Required correction** Specify the quantitative outputs of the framework, such as changes in state populations, transition rates, or free energy differences.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, MD simulations
- **Evidence pointer** Methods section "Molecular dynamics (MD) simulations"
- **Issue** The stoichiometry of 100 ligand molecules per Aβ42 peptide is stated, but the box size, ionic strength, and temperature/pressure coupling details are not provided in the main text. These are critical for reproducing the simulations.
- **Required Correction** Provide these details in the main text or refer explicitly to the supplementary methods where they are described.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Results, Secondary structure content
- **Evidence pointer** Results section "Secondary structure content in simulations of free Aβ42 and Aβ42 with ligands", Figure 1B
- **Issue** The differences in secondary structure content between systems are described qualitatively (e.g., "increased by 11.1%"), but no error bars or statistical significance tests are reported for these values.
- **Required Correction** Report the variability across the ensemble of models or across simulation replicates, and provide statistical tests for the significance of the observed differences.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, Molecular interactions
- **Evidence pointer** Results section "Molecular interactions", Figure 4
- **Issue** The interaction energy values are reported in kcal/mol, but the text does not clarify whether these are per-ligand averages, per-residue averages, or total values. The range for SPA (-114 to 71 kcal/mol) is very wide, and the interpretation is unclear.
- **Required Correction** Clarify the definition of the reported interaction energies and discuss the significance of the wide range.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion contains a duplicated phrase: "but they promoted the exposure of polar residues (similar to a 'solvation' effect), but they promoted the exposure of polar residues (similar to a 'solvation' effect)". This appears to be a typographical error.
- **Required Correction** Remove the duplicated phrase.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, Experimental validation
- **Evidence pointer** Experimental validation section
- **Issue** The experimental methods are described only briefly, with no details on sample preparation, instrument parameters, or data analysis procedures. The reader is referred to the supplementary materials, but these are not provided.
- **Required Correction** Provide sufficient experimental details in the main text or ensure the supplementary materials are accessible and complete.

## Risk / unsupported claims
- The claim that CoVAMPnet is "broadly applicable" to study drug effects on disordered biomolecules is not supported by evidence from multiple systems.
- The claim that the gradient analysis "was able to pinpoint similar conformational events as the ones captured by NMR" is based on a qualitative comparison and lacks statistical support.
- The claim that TMP and SPA "preserved more structured conformations" of Aβ42 is not directly confirmed by the experimental data presented, which show only mild effects.
- The claim that the alignment method "proved useful" is not supported by quantitative validation or comparison with alternative methods.
- The statement that "the size of our datasets was thus sufficient for VAMPnet training" is based on the observation that additional data did not significantly affect implied timescales, but no formal convergence criterion is provided.
- The claim that the computational results "suggest that TMP/SPA may also target other biomolecules than Aβ peptides" is speculative and not directly supported by the data presented.