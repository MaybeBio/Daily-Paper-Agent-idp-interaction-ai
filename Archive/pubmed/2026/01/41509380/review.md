## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) with supplementary figure/table references
- **Assessment boundary** Scientific content, methodological rigor, evidence quality, and internal consistency of the reported findings
- **Shared manuscript claim summary** The authors use all-atom MD simulations to show that spermine (Spm) modulates aggregation-associated intramolecular contacts in a residue-specific and protein-dependent manner: inhibiting Tau K18 aggregation, promoting α-synuclein aggregation, and exerting mixed effects on Aβ40. ThT fluorescence assays for K18 and full-length Tau are presented as experimental validation.
- **Visible evidence base** Simulation data (contact maps, Rg, g(r), secondary structure), ThT kinetics for K18 and full-length Tau, comparison with published fibril structures
- **Missing materials affecting confidence** Supplementary figures and tables (S1–S14) referenced but not provided; no experimental data for αS or Aβ40; no raw simulation trajectories or convergence metrics; no error bars on contact probability differences; no statistical significance testing

## Reviewer

- **Overall assessment** This manuscript addresses an important and timely question: how a common cellular polyamine, spermine, differentially modulates the conformational ensembles of three disease-linked intrinsically disordered proteins. The central claim, that Spm acts through residue-specific interactions rather than simple electrostatics, is biologically plausible and potentially significant. However, the evidence presented is largely computational, and the experimental validation is limited to one protein system. Several technical concerns regarding simulation convergence, force field suitability, and the interpretation of contact probability differences need to be addressed before the conclusions can be considered robust. The manuscript is clearly written and the conceptual framework is appealing, but the current evidence base does not fully establish the mechanistic claims.

- **Who would be interested in the results, and why** Researchers studying protein aggregation in neurodegeneration, particularly those focused on Tau, α-synuclein, and amyloid-β; investigators interested in polyamine biology and its role in disease; computational biophysicists working on intrinsically disordered proteins; drug discovery groups seeking small-molecule modulators of IDP conformation. The proposed framework for predicting polyamine effects based on residue-level charge distribution could inform therapeutic strategies targeting polyamine metabolism.

- **Major strengths**
  1. The study addresses a clinically relevant question with potential therapeutic implications, namely how endogenous metabolites modulate IDP aggregation.
  2. The comparative approach across three different IDPs with distinct charge distributions is conceptually strong and allows for mechanistic differentiation.
  3. The use of patient-derived fibril structures as reference states for defining disease-relevant contacts is appropriate and adds biological relevance.
  4. The experimental validation for K18, while limited, provides some direct support for the computational predictions.
  5. The manuscript is generally well-written and the figures are described clearly.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "long all-atom molecular dynamics simulations" provide reliable residue-level changes in intra-chain contacts across a range of Spm concentrations.
- **Evidence pointer** Methods section, Table S1 (referenced but not provided)
- **Concern** The manuscript does not report simulation convergence metrics. For intrinsically disordered proteins, which sample highly heterogeneous conformational ensembles, it is essential to demonstrate that the simulations have reached equilibrium and that the observed contact probability differences are not artifacts of insufficient sampling. The authors state that initial 500 ns (K18, Aβ40) or 200 ns (αS) were discarded, but the total simulation lengths and the number of independent replicates are not stated in the main text. Without convergence assessment (e.g., block averaging of contact maps, comparison of independent trajectories), the quantitative contact probability differences reported in Figures 2 and 5 cannot be evaluated for statistical reliability.
- **Why it matters** The central conclusions depend on detecting differences in contact probabilities between Spm-free and Spm-containing systems. If these differences are within the noise of the sampling, the mechanistic interpretations are not supported. The absence of convergence analysis undermines the quantitative claims throughout the manuscript.
- **Resolution test** Provide total simulation lengths, number of replicates, and convergence metrics (e.g., contact map convergence over time, standard errors from block averaging). Show that the reported contact probability differences exceed the estimated sampling uncertainty.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "Spm acts in a sequence- and region-specific manner, not simply through overall net charge" and that in K18, Spm "disrupts intra-chain contacts associated with Alzheimer's fibril structures and thereby inhibiting aggregation."
- **Evidence pointer** Figure 2A, Figure 5A (left panel), ThT data in Figure 3
- **Concern** The experimental validation is limited to K18 and full-length Tau. No experimental data are provided for αS or Aβ40, despite the manuscript making strong claims about Spm promoting aggregation in αS and exerting mixed effects in Aβ40. The ThT assay for K18 shows inhibition, but the mechanistic link between the observed contact changes and the ThT result is inferred rather than demonstrated. Specifically, the claim that Spm "inhibits aggregation" of K18 is based on ThT fluorescence, which reports on amyloid fibril formation, but the simulations are of monomeric K18. The connection between monomeric conformational changes and aggregation outcomes requires additional experimental support or a more explicit mechanistic model.
- **Why it matters** The manuscript presents a unified framework for predicting Spm effects across three proteins, but the experimental validation covers only one. Without experimental confirmation for αS and Aβ40, the generality of the proposed mechanism remains speculative. The disconnect between monomer simulations and aggregation assays also weakens the causal interpretation.
- **Resolution test** Provide experimental aggregation data for αS and Aβ40 in the presence of Spm, or clearly reframe the claims as predictions requiring validation. Alternatively, provide a more explicit mechanistic model linking monomeric contact changes to aggregation kinetics.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors state that "net charge alone cannot predict polyamine influence on IDPs" and that "residue-specific binding hotspots and local reweighting of aggregation-linked contacts determine whether Spm promotes or suppresses fibril-like conformations."
- **Evidence pointer** Figures 2, 4, 5
- **Concern** The manuscript does not provide a quantitative or predictive framework that would allow a reader to anticipate Spm effects on other IDPs or mutants. The conclusion that residue-specific interactions matter is supported, but the authors do not distill their findings into testable rules or a model that could be applied prospectively. For example, what features of the K18 sequence make it susceptible to Spm-mediated disruption, and could these be identified a priori in other proteins? The discussion mentions potential therapeutic implications but does not articulate how the findings could guide intervention strategies.
- **Why it matters** The stated significance of the work is that it provides "a mechanistic basis for how small molecules reprogram IDP conformational ensembles and suggests principles for designing ligands." Without a more generalizable framework, the impact is limited to the three specific proteins studied.
- **Resolution test** Articulate specific sequence or structural features that predict Spm sensitivity, and ideally test these predictions on additional protein constructs or mutants.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors compare computed 15N chemical shifts with experimental data and state that "the overall patterns suggest good qualitative agreement between simulation and experiment."
- **Evidence pointer** Figure S2 (referenced but not provided)
- **Concern** The validation of the simulation force field against NMR chemical shifts is described only qualitatively. The authors do not report quantitative agreement metrics (e.g., RMSD between computed and experimental shifts, correlation coefficients). Moreover, the comparison is only for K18, not for αS or Aβ40. Given that the force field choice (AMBER ff99SBws) is critical for the reliability of IDP simulations, a more rigorous validation is needed.
- **Why it matters** The conclusions depend on the accuracy of the simulated conformational ensembles. If the force field does not accurately reproduce experimental observables, the contact probability differences may not reflect real biophysical behavior.
- **Resolution test** Provide quantitative agreement metrics for the chemical shift comparison, and ideally validate the simulations against additional experimental observables (e.g., SAXS, FRET) for all three proteins.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "Spm binds mainly to acidic residues in the C-terminal half of the sequence" for αS and that this "redistributes intramolecular contacts in a way that increases contact propensity in the central aggregation-prone region."
- **Evidence pointer** Figure 5A (middle panel), Figure 5B (middle panel)
- **Concern** The manuscript does not report binding affinities or occupancies for Spm-protein interactions. The NSpm metric (average number of Spm molecules interacting with each residue) is presented, but the threshold for defining an interaction is not clearly justified. Additionally, the relationship between Spm binding and the observed contact changes is correlative; the authors do not demonstrate causality, for example by mutating key acidic residues and showing loss of the Spm effect.
- **Why it matters** The mechanistic claims rely on the identification of specific binding sites. Without quantitative binding data or mutagenesis experiments, the proposed mechanism remains speculative.
- **Resolution test** Provide binding free energies or occupancies for Spm at key sites, and/or perform simulations or experiments with mutant proteins lacking key acidic residues.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction, first paragraph
- **Evidence pointer** Introduction, paragraph 1
- **Issue** The opening paragraph is somewhat generic and does not clearly motivate why spermine specifically is an important molecule to study in the context of neurodegeneration. The connection between polyamine metabolism and disease is mentioned only briefly.
- **Required correction** Expand the introduction to provide more context on the biological relevance of spermine in neurons, its concentration ranges, and prior evidence linking polyamines to protein aggregation.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, simulation protocol
- **Evidence pointer** Methods section, "All-atom MD simulation"
- **Issue** The manuscript states that simulations were run at different temperatures for different proteins (283 K for K18, 288 K for αS, 278 K for Aβ40) to match NMR conditions. However, the ThT experiments were performed at 37 °C. The temperature mismatch between simulations and experiments is not discussed, and its potential impact on the interpretation is not addressed.
- **Required correction** Discuss the temperature difference and justify why the simulation temperatures are appropriate for making predictions about aggregation behavior at physiological or experimental temperatures.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, ThT kinetics
- **Evidence pointer** Methods section, "ThT kinetics"
- **Issue** The ThT assay description does not specify the buffer conditions for the aggregation experiments beyond 25 mM HEPES pH 7.4. It is unclear whether the experiments included any aggregation-inducing agents (e.g., heparin for Tau) or co-factors, which are commonly required for Tau aggregation in vitro.
- **Required correction** Provide full details of the aggregation assay conditions, including any co-factors, salt concentrations, and the concentration of protein and spermine used.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interdisciplinary readership
- **Affected element** Discussion, paragraph 2
- **Evidence pointer** Discussion, paragraph 2
- **Issue** The discussion of LLPS is brief and does not fully integrate the findings with the broader literature on polyamine-induced phase separation. The connection between the observed monomeric contact changes and LLPS behavior is not clearly articulated.
- **Required correction** Expand the discussion of how the observed conformational changes might relate to LLPS, and cite relevant prior work on polyamines and phase separation.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Figure 2, Figure 5
- **Evidence pointer** Figure 2, Figure 5
- **Issue** The contact map representations are described in the text but the figures are not provided in the manuscript. The color scales and the meaning of the difference maps are not explained in the text.
- **Required correction** Ensure that figure legends clearly explain the color scales and the interpretation of the difference maps.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, section "Residue-Specific Interactions Patterns"
- **Evidence pointer** Results, section "Residue-Specific Interactions Patterns"
- **Issue** The manuscript states that "the binding patterns observed here suggest that the changes in extended-state conformation seen in Fig. 4C are a direct consequence of Spm interactions." This causal language is not supported by the correlative data presented.
- **Required correction** Soften the causal language and acknowledge that the relationship between Spm binding and conformational changes is inferred from correlation.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, simulation analysis
- **Evidence pointer** Methods section, "Simulation analysis"
- **Issue** The contact definition (distance cutoff of 0.45 nm for intra-chain contacts and 0.6 nm for Spm-mediated contacts) is stated, but the rationale for these specific cutoffs is not provided.
- **Required correction** Justify the choice of distance cutoffs or cite prior work using similar definitions.

- **Technical failings that need to be addressed before the case is established**
  R1-M1 (simulation convergence), R1-M2 (limited experimental validation), R1-M4 (force field validation)

- **Assessment against Nature-style criteria**
  - **Originality**: The study is moderately original. While polyamine effects on individual proteins have been studied, the comparative approach across three IDPs with different charge distributions is a useful contribution. However, the conceptual framework of charge-based modulation is not entirely new.
  - **Scientific importance**: The question of how endogenous metabolites modulate IDP aggregation is important for understanding neurodegeneration and for therapeutic development. The findings could have implications for polyamine-based interventions, but the current evidence is not strong enough to establish clinical relevance.
  - **Interdisciplinary readership**: The manuscript bridges computational biophysics, protein chemistry, and neurodegeneration research. The findings would interest researchers in these fields, but the limited experimental validation may reduce its appeal to a broader audience.
  - **Technical soundness**: The computational methodology is appropriate in principle, but the lack of convergence analysis and the limited force field validation are significant weaknesses. The experimental component is well-executed but covers only one of the three proteins.
  - **Readability for nonspecialists**: The manuscript is generally well-written and the conceptual framework is accessible. However, some technical details (e.g., contact map analysis) may be challenging for readers without a computational background.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important question and the conceptual framework is appealing. However, the lack of simulation convergence analysis and the limited experimental validation prevent the conclusions from being fully established. If the authors can provide convergence metrics, additional experimental data for αS and Aβ40, and a more rigorous force field validation, the manuscript would be suitable for publication in a high-impact journal. Currently, the evidence base is not sufficient to support the strong mechanistic claims made throughout the manuscript.

## Risk / unsupported claims
- The claim that Spm "inhibits aggregation" of K18 is supported by ThT data, but the mechanistic link to specific contact changes is inferred, not demonstrated.
- The claim that Spm "promotes aggregation" of αS is based solely on simulations and prior literature, with no new experimental data.
- The claim that Spm "exerts mixed effects" on Aβ40 is based solely on simulations, with no experimental validation.
- The statement that "net charge alone cannot predict polyamine influence on IDPs" is supported by the data, but the alternative predictive framework is not articulated.
- The claim that Spm binding "disrupts intra-chain contacts associated with Alzheimer's fibril structures" in K18 is based on contact probability differences that lack statistical significance testing.
- The comparison of computed and experimental chemical shifts is described only qualitatively, and the agreement is not quantified.
- The manuscript states that "the overall patterns suggest good qualitative agreement" but does not provide the actual comparison data in the main text.