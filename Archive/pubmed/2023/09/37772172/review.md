## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion) as provided
- **Assessment boundary** Scientific content, methodological soundness, evidence consistency, and alignment with stated claims; no assessment of editorial fit or publication decision
- **Shared manuscript claim summary** The authors use coarse-grained molecular dynamics simulations to show that ATP acts as a hydrotrope to regulate the phase separation of NBDY clusters, with a dual effect: nonsaturated ATP concentrations promote phase separation, while oversaturated ATP concentrations inhibit it. They propose that ATP mediates interactions between NBDY residues at low concentrations and disrupts them at high concentrations, and that ATP clustering hinders NBDY diffusion.
- **Visible evidence base** Main text figures referenced (Figures 1–7), supplementary figures S1–S3, methods descriptions, and discussion text; no raw data, simulation trajectories, or parameter files were provided
- **Missing materials affecting confidence** Simulation parameter files, force field details beyond references, convergence criteria, error bars or statistical analysis of replicates, raw trajectory data, and full supplementary information were not available for independent verification

## Reviewer
- **Overall assessment** The manuscript addresses a timely and interesting question regarding the role of ATP as a hydrotrope in regulating protein phase separation, using a coarse-grained simulation approach. The central claim of a dual effect of ATP concentration on NBDY phase separation is plausible and potentially significant. However, the evidence presented has several weaknesses. The simulation methodology is described at a level that prevents full reproducibility, the quantitative analysis relies on a single metric (ΔP) without clear statistical treatment, and the mechanistic interpretation, while reasonable, is not uniquely supported by the data. The link between simulation observations and the proposed molecular model requires stronger validation. The manuscript would benefit from additional analyses, clearer presentation of uncertainties, and a more rigorous connection between the observed metrics and the claimed mechanisms.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, intrinsically disordered proteins, and the role of small molecules such as ATP in cellular organization. The work may also interest computational biophysicists developing coarse-grained models for IDP systems. The potential dual role of ATP as both promoter and inhibitor of phase separation could have implications for understanding cellular stress responses and ATP-dependent regulation of membraneless organelles.
- **Major strengths** The topic is relevant and timely. The use of a coarse-grained model to explore ATP concentration effects on NBDY is a reasonable approach. The identification of a critical concentration ratio with a dual effect is an interesting finding. The authors attempt to provide a mechanistic explanation involving ATP-mediated bridging and disruption of NBDY interactions. The inclusion of ATP clustering as a factor is a thoughtful addition.
- **Major Concerns** The concerns below detail issues with methodological transparency, statistical rigor, mechanistic interpretation, and consistency of evidence.
- **Minor Comments** Several smaller issues regarding presentation, figure clarity, and terminology are listed below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (methodological transparency), R1-M2 (statistical rigor), R1-M3 (mechanistic interpretation), R1-M4 (ATP clustering claim)
- **Assessment against Nature-style criteria** Originality: moderate. The application of a hydrotrope framework to NBDY is novel, but the general concept of ATP as a hydrotrope is established. Scientific importance: moderate. The findings could be of interest to the condensate field, but the impact is limited by the lack of experimental validation and the narrow focus on one protein. Interdisciplinary readership: limited. The work is primarily computational and will appeal mainly to specialists. Technical soundness: weak. The methodology is not fully described, and the analysis lacks statistical rigor. Readability for nonspecialists: acceptable. The text is generally clear, but some terms and metrics are not fully explained.
- **Recommendation posture** Currently not established from the provided evidence. The core claims are plausible but not sufficiently supported by the presented analysis. Major revisions addressing methodological transparency, statistical treatment, and mechanistic validation are required before the case can be considered established.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency
- **Claim pointer** The authors claim to have used a coarse-grained model combining MOFF for NBDY and a two-bead ATP model to simulate NBDY-ATP interactions, with results showing a dual effect of ATP concentration on phase separation.
- **Evidence pointer** Methods section, "Coarse-Grained Model of NBDY and ATP"; "Slab Simulation Model and Simulation Details"
- **Concern** The methods section does not provide sufficient detail to reproduce the simulations. The MOFF force field is referenced, but the specific parameters for the NBDY-ATP interaction potential are only described as "refer to the Supporting Information (SI)," which was not provided. The ATP model is described as two beads connected by a harmonic spring, but the spring constant, equilibrium distance, and the functional form of the hydrophobic and electrostatic interactions between ATP and NBDY are not specified. The simulation protocol (e.g., equilibration time, number of replicates, system size, salt concentration) is incomplete. Without these details, the results cannot be independently verified or reproduced.
- **Why it matters** Reproducibility is a fundamental requirement for computational studies. The lack of parameter details and simulation protocols undermines confidence in the reported findings and prevents other researchers from building on this work.
- **Resolution test** Provide a complete description of all force field parameters, interaction potentials, simulation setup, and analysis protocols, either in the main text or in a fully accessible supplementary information file. Include the number of independent simulations, equilibration procedures, and any convergence checks.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors report ΔP values as a function of ATP concentration and state that "the ΔP of the system with ATP is always higher than that of the NBDY system without ATP when the concentration(A:N) is lower than 10" and that "oversaturated ATP concentration promotes the diffusion of NBDY."
- **Evidence pointer** Results section, "ATP Regulates the Phase Separation of NBDY Clusters"; Figure 2
- **Concern** The analysis relies on ΔP, defined as the average of |Pmax – Pmin| over "all three NVT parallel simulations." However, no error bars, standard deviations, or statistical tests are reported. It is unclear whether the observed differences between conditions are statistically significant or within the noise of the simulations. The claim of a "critical point" at concentration(A:N) ≈ 10 is based on visual inspection of trends, but no quantitative criterion is provided. Additionally, the number of replicates (three) is small, and no information is given about the variability between replicates.
- **Why it matters** Without statistical treatment, the reader cannot assess the robustness of the reported trends. The central claim of a dual effect depends on the reliability of the ΔP measurements, and the lack of uncertainty quantification weakens the conclusions.
- **Resolution test** Report the mean and standard deviation (or standard error) for ΔP, Rg, and RMSF across replicates. Perform appropriate statistical tests (e.g., t-tests or ANOVA) to support claims of significant differences between conditions. Provide a clear definition of the "critical point" and justify it with quantitative analysis.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic interpretation
- **Claim pointer** The authors propose that "nonsaturated ATP-NBDY interactions may favor these interactions and make the cluster of NBDY more compact below concentration(A:N) = 10" and that "oversaturated ATP-NBDY interaction impedes the phase separation of NBDY."
- **Evidence pointer** Results section, "Oversaturated ATP-NBDY Interaction Disfavors the Phase Separation of NBDY Clusters"; "ATP-NBDY Interaction Affects the Interaction among NBDYs in the Clusters"; Figures 3 and 4
- **Concern** The mechanistic model is inferred from contact counts between specific residue pairs. However, the analysis is descriptive and does not establish causality. For example, the decrease in LYS-GLY or ARG-GLY contacts with increasing ATP concentration could be a consequence of overall cluster expansion rather than a direct effect of ATP competition. The claim that ATP acts as a "bridge" between residues at low concentrations is supported only by indirect contact counts, and no direct evidence of bridging (e.g., ATP simultaneously contacting two NBDY residues) is presented. The interpretation that "ATP can act as the junction between different NBDYs" is speculative and not uniquely determined by the data.
- **Why it matters** The proposed mechanism is a key contribution of the manuscript. If the interpretation is not well supported, the significance of the findings is diminished. A more rigorous analysis is needed to distinguish between competing explanations.
- **Resolution test** Perform additional analyses to directly test the bridging hypothesis, such as computing the fraction of ATP molecules in simultaneous contact with two or more NBDY residues, or comparing the observed contact patterns to a null model. Discuss alternative explanations and rule them out with data.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence consistency
- **Claim pointer** The authors state that "increasing the energy coupling parameter ε(a) led to a reduction in the RMSF of NBDY" and that "ATP clustering hinders the diffusion of NBDY and promotes the phase separation of NBDY clusters."
- **Evidence pointer** Results section, "ATP Cluster Disfavors the Diffusion of NBDY"; Figures 5B and 6
- **Concern** The claim that ATP clustering promotes phase separation appears to contradict the earlier finding that high ATP concentrations (which would favor clustering) inhibit phase separation. The authors do not reconcile these two observations. If ATP clustering promotes phase separation, then at high ATP concentrations, where clustering is more likely, one might expect enhanced phase separation, not inhibition. The manuscript does not address this apparent inconsistency, and the relationship between ATP clustering, ATP concentration, and NBDY phase separation is not clearly explained.
- **Why it matters** The internal consistency of the proposed model is essential for the credibility of the conclusions. An unresolved contradiction undermines the mechanistic framework.
- **Resolution test** Provide a coherent explanation for how ATP clustering and ATP concentration independently or jointly affect NBDY phase separation. Discuss the conditions under which clustering promotes versus inhibits phase separation, and support the explanation with additional simulations or analyses.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** Definition of "concentration(A:N)"
- **Evidence pointer** Results section, "ATP Regulates the Phase Separation of NBDY Clusters"
- **Issue** The term "concentration(A:N)" is used throughout but is not clearly defined. It appears to be a ratio of ATP to NBDY molecule numbers, but the relationship to actual concentration (e.g., molarity) is not explained.
- **Required correction** Define "concentration(A:N)" explicitly in the methods or results, and clarify whether it refers to a number ratio, molar ratio, or something else.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Figure presentation
- **Affected element** Figures 2–6
- **Evidence pointer** Results section, Figures 2–6
- **Issue** The figures are referenced but not described in sufficient detail in the text. For example, it is unclear what error bars represent (if present) and what the axes of each panel show.
- **Required correction** Provide detailed figure captions and refer to specific panels in the text. Clearly label axes, units, and any statistical information.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Consistency of temperature description
- **Affected element** Methods section, "Slab Simulation Model and Simulation Details"
- **Evidence pointer** Methods section
- **Issue** The text states that simulations were performed at "temperatures of 0.4 and 0.8 (reduced units)," but the relationship between reduced temperature and physical temperature is not explained. This may confuse readers unfamiliar with reduced units.
- **Required correction** Explain the conversion between reduced and physical temperature, or state that only reduced units are used and provide context for their meaning.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion and Conclusion
- **Evidence pointer** Discussion and Conclusion
- **Issue** The discussion does not acknowledge the limitations of the coarse-grained model, such as the simplified representation of ATP and the implicit solvent treatment. These limitations could affect the generality of the conclusions.
- **Required correction** Add a paragraph discussing the limitations of the model and the potential impact on the findings.

## Risk / unsupported claims
- The claim that "ATP can act as a hydrotrope to regulate the phase separation of NBDY clusters" is supported by simulation data but lacks experimental validation; the term "hydrotrope" is used in a general sense and the specific mechanism is not directly measured.
- The claim of a "critical point" at concentration(A:N) ≈ 10 is based on visual inspection of trends without quantitative criteria or statistical support.
- The mechanistic model involving ATP-mediated bridging at low concentrations and disruption at high concentrations is inferred from contact counts but not directly demonstrated.
- The claim that "ATP clustering hinders the diffusion of NBDY and promotes the phase separation" is not reconciled with the finding that high ATP concentrations inhibit phase separation.
- The statement that "ATPs can bind to the protein surface by aggregating into ATP clusters" is presented as a finding but is not quantitatively characterized in the provided text.
- The relationship between the simulation results and the experimental observations cited from prior work is asserted but not critically evaluated.