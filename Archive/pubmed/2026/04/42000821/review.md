## Review setup
- **Input scope** Full manuscript text, including Introduction, Results, Discussion, Methods, and selected figure/table references.
- **Assessment boundary** Scientific content, methodological soundness, data interpretation, and support for claims as presented in the provided text. No assessment of editorial fit or journal-specific policy.
- **Shared manuscript claim summary** The authors design and characterize peptide ligands targeting the SARS-CoV-2 nucleocapsid protein N-terminal region (NTR(1–248)), specifically the N-terminal domain (NTD(44–180)) and its flanking intrinsically disordered regions. They introduce a fluorinated phenylalanine into two peptide variants (P1, P2) to enable 19F NMR-based detection and to probe the role of aromatic interactions. They report binding affinities, conformational preferences, and interaction interfaces using NMR, circular dichroism, and molecular dynamics simulations.
- **Visible evidence base** Main text figures (Figs. 1–12), Tables 1, Methods section, and references to Supplementary Figures S1–S18 and Tables S1–S12. Supplementary material itself was not provided for review.
- **Missing materials affecting confidence** Supplementary figures and tables (S1–S18, S1–S12) are referenced but not available. Raw NMR spectra, relaxation data, MD trajectory details, and complete CSP datasets are not accessible. This limits verification of quantitative claims and reproducibility assessment.

## Reviewer
- **Overall assessment** The manuscript presents a systematic and technically sound approach to designing peptide ligands for a challenging intrinsically disordered protein target. The combination of 19F NMR, protein-based CSP analysis, CD spectroscopy, and MD simulations provides a multi-perspective view of the interaction. The work is competent and the data appear internally consistent. However, the scientific advance over prior work (particularly the previously reported P0 and the PNA chimera) is incremental, and several quantitative claims require additional validation or clarification. The manuscript would benefit from stronger evidence that the designed peptides engage the target with meaningful specificity and from a more critical discussion of the limitations of the affinity measurements.
- **Who would be interested in the results, and why** Researchers working on SARS-CoV-2 nucleocapsid protein biology, intrinsically disordered proteins, peptide ligand design, and NMR-based screening of protein-ligand interactions. The methodological combination of 19F NMR with MD simulations may interest structural biologists and medicinal chemists exploring fluorinated probes for disordered targets.
- **Major strengths**
  1. The dual-perspective NMR approach (protein 15N CSP and ligand 19F detection) is elegant and provides complementary information.
  2. The systematic variation of peptide sequence (P0 vs P1 vs P2) allows attribution of binding differences to specific structural features.
  3. The integration of experimental (NMR, CD) and computational (REMD, MD) methods is appropriate and well-executed.
  4. The manuscript is clearly written and the figures are informative.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Quantitative claim support
  - **Claim pointer** The authors report Kd values of 847 ± 222 μM (NTD(44–180) with P0), 120 ± 14 μM (NTR(1–248) with P0), 223.1 ± 13.50 μM (NTD(44–180) with P1), and 156.8 ± 5.80 μM (NTD(44–180) with P2), and state that P2 binds more tightly than P1.
  - **Evidence pointer** Results section, Figs. 1D, 7, Table S3
  - **Concern** The Kd values are derived from CSP fitting, but the manuscript does not provide sufficient detail on the fitting procedure, the number of residues used for each fit, the error propagation, or the goodness-of-fit. The reported errors are surprisingly small given the weak affinities (hundreds of μM), and no replicate measurements are described. Additionally, the comparison between P0 binding to NTD(44–180) (847 μM) and to NTR(1–248) (120 μM) is based on data from different experimental sessions and potentially different conditions, yet this difference is used to support a major conclusion about the role of IDRs. The statistical significance of the difference between P1 and P2 Kd values (223 vs 157 μM) is not established.
  - **Why it matters** The central quantitative claims of the paper, namely that IDRs enhance binding and that P2 binds more tightly than P1, rest on these Kd values. Without rigorous error analysis and demonstration of reproducibility, these conclusions are not firmly established.
  - **Resolution test** Provide full fitting details, including the number of residues used, the fitting equation and assumptions, error estimates from Monte Carlo or bootstrap analysis, and replicate titrations. Demonstrate that the Kd differences are statistically significant (e.g., via a t-test or non-overlapping confidence intervals).
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Specificity and selectivity
  - **Claim pointer** The authors state that the peptides target the RNA-binding region of NTD(44–180) and that the interaction is relevant for potential antiviral development.
  - **Evidence pointer** Results section, Figs. 4, 5, 12
  - **Concern** The manuscript does not demonstrate binding specificity. No control experiments with a scrambled peptide sequence, a non-fluorinated phenylalanine variant, or an unrelated protein are shown. The CSP patterns overlap with RNA-binding regions, but this does not exclude non-specific electrostatic interactions, which are a major concern for highly charged peptides (P1 and P2 are rich in glutamate). The claim that these peptides could serve as "molecular probes" or "possible inhibitors" requires evidence that binding is specific and not merely a consequence of charge-charge interactions.
  - **Why it matters** For a peptide to be useful as a probe or lead for inhibitor design, specificity is essential. Non-specific electrostatic binding would limit the translational relevance and the interpretability of the interaction data.
  - **Resolution test** Include control titrations with a scrambled-sequence peptide, a peptide lacking the fluorinated phenylalanine, and/or an unrelated negatively charged peptide. Show that the observed CSPs are not reproduced with these controls. Alternatively, perform competition experiments with RNA to demonstrate that the peptides compete for the same binding site.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Interpretive gap between computation and experiment
  - **Claim pointer** The authors use MD simulations to describe the conformational preferences of P1 and P2 and to propose a "pincer grasp" binding mode.
  - **Evidence pointer** Results section, Figs. 2, 9, 10
  - **Concern** The MD simulations are used to support structural interpretations, but the connection between the simulated free-energy landscapes and the experimentally observed binding behavior is not rigorously established. The "pincer grasp" description is based on a single trajectory or a limited set of trajectories initiated from docking poses, and no quantitative comparison between simulated and experimental observables (e.g., predicted vs measured CSPs, predicted vs measured binding free energies) is provided. The claim that P2 binds more tightly because of its "elongated and flexible core" is speculative and not directly supported by the simulation data.
  - **Why it matters** The manuscript presents the MD simulations as providing mechanistic insight, but without validation against experimental data, the proposed binding mode remains a hypothesis. Over-interpretation of simulation results can mislead readers.
  - **Resolution test** Provide a quantitative comparison between simulation and experiment, such as predicted chemical shift perturbations from the simulated ensembles compared to measured CSPs, or calculated binding free energies compared to experimental Kd values. Alternatively, temper the language to clearly indicate that the binding mode is a hypothesis requiring further validation.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Completeness of interaction characterization
  - **Claim pointer** The authors state that the peptides engage both the NTD(44–180) and the flanking IDRs, and that this is a key feature of the design.
  - **Evidence pointer** Results section, Fig. 1
  - **Concern** The evidence for IDR engagement is based on CSPs observed in the NTR(1–248) construct, but the manuscript does not provide residue-level assignments for the IDR regions. Without assignments, it is not possible to determine which specific residues in the IDRs are perturbed. The claim that the "poly-leucine region" and "SR-rich region" are involved relies on the assumption that the observed CSPs correspond to these regions, but this is not explicitly demonstrated.
  - **Why it matters** A central claim of the paper is that the peptide design successfully engages disordered regions. If the IDR assignments are not established, this claim is weakened.
  - **Resolution test** Provide evidence for IDR residue assignments, such as a table of assigned residues in the IDR regions or a reference to previously published assignments. If assignments are not available, acknowledge this limitation and temper the claim accordingly.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of methods
  - **Affected element** CD spectroscopy methods
  - **Evidence pointer** Methods section, "Circular dichroism"
  - **Issue** The CD methods section is brief and does not specify the concentration of peptides used, the path length of the cuvette, or how the α-helical content was estimated from the spectra.
  - **Required correction** Provide full experimental details for CD measurements and specify the method used to estimate helical content (e.g., the equation or software used).
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Data presentation
  - **Affected element** Figure 1C
  - **Evidence pointer** Results section, Fig. 1C
  - **Issue** The CSP plot in Fig. 1C compares P0 binding to NTD(44–180) and NTR(1–248), but the residue numbering for the two constructs may not align, as NTR(1–248) includes additional residues. It is unclear whether the CSP values are plotted against the same residue numbering scheme.
  - **Required correction** Clarify the residue numbering used in Fig. 1C and ensure that the comparison is meaningful. If the numbering differs, indicate this in the figure legend.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** "Pincer grasp" description
  - **Evidence pointer** Results section, Fig. 10
  - **Issue** The term "pincer grasp" is used to describe the binding mode, but this is not a standard term in the field and may be confusing to readers.
  - **Required correction** Define the term clearly or use more standard terminology (e.g., "clamp-like" or "wrap-around" binding mode).
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** MD simulation details
  - **Evidence pointer** Methods section, "Peptide-protein affinity simulations"
  - **Issue** The Methods section for MD simulations is detailed but lacks information on the number of independent simulations performed for each system beyond the eight mentioned, the total simulation time per replica, and the criteria for selecting the "highest-affinity docking pose."
  - **Required correction** Provide complete simulation parameters, including the number of replicas, total simulation time, and the selection criteria for starting structures.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** Table S3
  - **Evidence pointer** Results section, "Dual-perspective analysis"
  - **Issue** The Kd values in Table S3 are reported with errors, but the number of independent measurements (n) is not stated.
  - **Required correction** Report the number of replicates for each Kd determination and specify whether the errors represent standard deviations or standard errors.
- **Technical failings that need to be addressed before the case is established**
  1. Lack of control experiments to establish binding specificity (R1-M2).
  2. Insufficient detail on Kd fitting and error analysis to support quantitative claims (R1-M1).
  3. Unvalidated connection between MD simulations and experimental observations (R1-M3).
  4. Unclear residue assignments for IDR regions in the NTR(1–248) construct (R1-M4).
- **Assessment against Nature-style criteria**
  - **Originality** Moderate. The application of 19F-labeled peptides to probe interactions with a disordered multidomain protein is a useful methodological contribution, but the conceptual advance over prior work on polyanionic ligands and the previously reported P0 peptide is incremental.
  - **Scientific importance** Moderate. The SARS-CoV-2 nucleocapsid protein remains a relevant target, and understanding its ligand-binding properties has value. However, the therapeutic implications are speculative, and the affinity values reported are weak (μM range), limiting immediate translational significance.
  - **Interdisciplinary readership** Moderate. The work bridges peptide chemistry, NMR spectroscopy, and computational biology, and may appeal to researchers in these areas. The broader readership interest is limited by the narrow focus on a single protein target.
  - **Technical soundness** Generally sound, but with notable gaps. The NMR experiments appear well-executed, and the MD simulations are state-of-the-art. However, the lack of specificity controls and the incomplete statistical treatment of Kd values are significant weaknesses.
  - **Readability for nonspecialists** Good. The manuscript is clearly written, and the figures are well-designed. The introduction provides sufficient context for readers unfamiliar with disordered proteins or NMR-based screening.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a competent and potentially useful methodological contribution, but the quantitative claims require strengthening, and the specificity of the interaction must be demonstrated. If the authors address the major concerns, particularly the control experiments and the statistical rigor of the Kd determinations, the work could be suitable for publication.

## Risk / unsupported claims
- The claim that P2 binds more tightly than P1 is not statistically supported as presented.
- The claim that the peptides specifically engage the IDR regions (poly-leucine and SR-rich) is not fully supported without residue-level assignments.
- The "pincer grasp" binding mode is presented as a finding but is only a computational hypothesis without experimental validation.
- The statement that the peptides could serve as "molecular probes" or "possible inhibitors" is speculative given the lack of specificity data and the weak binding affinities.
- The comparison of Kd values between NTD(44–180) and NTR(1–248) for P0 is based on data that may not be directly comparable due to different experimental conditions, yet this comparison underpins a key conclusion.