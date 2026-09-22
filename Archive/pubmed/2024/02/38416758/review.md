## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, and conclusion. No supplementary figures or tables were provided for assessment.
- **Assessment boundary** Scientific claims, methodological soundness, consistency between stated methods and reported results, and alignment with the stated conclusions. No assessment of formatting, grammar, or journal fit beyond Nature-style criteria.
- **Shared manuscript claim summary** The authors performed sub-millisecond all-atom molecular dynamics simulations of a protein-RNA condensate to compare the diffusion of three guest peptides (Arg-rich, ADMA-rich, Lys-rich). They report that the Arg-rich peptide forms more hydrogen bonds with RNA, binds more strongly, and diffuses more slowly than the other two peptides, and that hydrogen bonding rather than cation-π interactions is the dominant factor regulating peptide diffusion.
- **Visible evidence base** Main text figures referenced as Figure 1, 2, 3, and 4; Table 1; supplementary figures referenced as SI Fig. 1-6 and SI videos 1-2. None of these figures, tables, or supplementary materials were provided in the submitted material.
- **Missing materials affecting confidence** All figures, tables, and supplementary materials are absent. This includes the simulation summary table (Table 1), the structural analysis figures (Fig. 1-2), the hydrogen bond and cation-π interaction quantification (Fig. 3), the kinetic rate and KD calculations (Fig. 4), and all supplementary figures and videos. The force field parameterization details for ADMA are described but the validation of these parameters is not shown.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question in the field of biomolecular condensates, namely the molecular determinants of guest peptide diffusion within protein-RNA condensates. The computational approach, using extensive all-atom MD simulations with a cumulative time of 564.7 μs, is ambitious and potentially valuable. However, the manuscript as presented cannot be adequately evaluated because all figures, tables, and supplementary materials are missing from the provided material. The claims regarding hydrogen bond counts, cation-π interaction numbers, kinetic rates, and dissociation constants are stated in the text but cannot be verified without the corresponding data. The methodological description is incomplete in several key areas, including the number of independent simulations per system, the criteria for defining bound versus dissociated states beyond the distance cutoff, and the validation of the ADMA force field parameters. The comparison with experimental data is mentioned but the quantitative agreement is not presented. The conclusion that hydrogen bonding dominates over cation-π interactions is plausible but the evidence base is not visible.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, liquid-liquid phase separation, and the molecular mechanisms of protein-RNA interactions would be interested. The work is also relevant to those developing and applying all-atom MD simulations to complex biomolecular systems. The specific comparison of Arg, ADMA, and Lys side chains in the context of condensate dynamics is of interest to the post-translational modification and intrinsically disordered protein communities.
- **Major strengths** The use of all-atom MD simulations at this scale is a significant technical effort. The comparison of three chemically related but distinct side chains (Arg, ADMA, Lys) provides a systematic approach to dissecting interaction contributions. The application of the IGME method to extract kinetic rates from the simulation ensemble is a sophisticated analytical approach. The connection to prior experimental observations provides a relevant context for the computational findings.
- **Major Concerns** The absence of all figures and tables makes the core quantitative claims unverifiable. The methodological details for the kinetic analysis are incomplete. The force field parameterization for ADMA lacks validation. The relationship between the simulation timescale and the experimentally observed diffusion timescale is not clearly established.
- **Minor Comments** The text contains some typographical errors and awkward phrasing. The distinction between "hydrogen bond" and "cation-π" contributions is discussed but the quantitative decomposition is not shown. The role of water-mediated interactions is not discussed.
- **Technical failings that need to be addressed before the case is established** The complete absence of all data figures and tables. The lack of validation for the ADMA force field. The incomplete description of the IGME analysis parameters. The absence of convergence analysis for the kinetic quantities.
- **Assessment against Nature-style criteria** Originality: The question of what molecular interactions control guest peptide diffusion in condensates is of high interest, and the systematic comparison of Arg, ADMA, and Lys is a valuable approach. However, the conceptual framework is not entirely novel, as prior work has discussed hydrogen bonding and cation-π interactions in condensates. Scientific importance: The results, if validated, would provide molecular-level insight into a process relevant to condensate biology and could inform the design of peptides with tunable condensate dynamics. The importance is moderate to high. Interdisciplinary readership: The work bridges biophysics, computational chemistry, and cell biology. The topic is of broad interest, but the presentation is heavily technical and may not be accessible to a general scientific audience. Technical soundness: The simulation methodology is generally sound, but the missing validation of the ADMA parameters and the incomplete description of the kinetic analysis prevent a full assessment. Readability for nonspecialists: The manuscript is written for a specialist audience. The abstract is clear, but the methods and results sections assume significant background knowledge.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript cannot be properly evaluated without the figures, tables, and supplementary materials. The core claims are plausible but unverifiable from the submitted text alone. A revised submission with all data included and with additional methodological details would be needed for a fair assessment.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence availability
- **Claim pointer** The manuscript reports quantitative results for hydrogen bond counts, cation-π interaction numbers, kinetic rates (kon, koff), and dissociation constants (KD) for three guest peptides in a protein-RNA condensate.
- **Evidence pointer** Figures 1-4, Table 1, SI Figures 1-6, SI Videos 1-2. Location not provided in the submitted material.
- **Concern** All figures, tables, and supplementary materials are absent from the provided submission. The core quantitative claims of the manuscript, including the differences in hydrogen bond numbers, cation-π interaction counts, and the derived kinetic parameters, cannot be verified. The text refers to specific values and trends, but without the actual data, the claims are unsupported.
- **Why it matters** The central conclusion that hydrogen bonding, rather than cation-π interactions, regulates peptide diffusion rests entirely on the quantitative comparisons shown in the figures. Without access to these data, the manuscript's primary findings cannot be assessed.
- **Resolution test** Provide all figures, tables, and supplementary materials in the revised submission. The figures must clearly show the data distributions, error bars, and statistical comparisons for all three systems.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological completeness
- **Claim pointer** The authors state that they used the IGME method to calculate transition rates between bound and dissociated states, and that they performed bootstrapping with 20 rounds, scanning τK and L between 1 and 50 ns.
- **Evidence pointer** Section "Calculation of transition rates and dissociation constants of guest peptides diffusion in condensates". Location not provided.
- **Concern** The description of the IGME analysis is incomplete. The manuscript does not specify how the bound and dissociated states were defined beyond the 4 Å contact criterion, how the transition probability matrices were constructed from the simulation data, or how the IGME hyperparameters were selected. The convergence of the kinetic estimates is not discussed. The relationship between the simulation timescale (200 ns per trajectory) and the derived lifetimes (microseconds) is not explained.
- **Why it matters** The kinetic parameters are central to the conclusion that binding/unbinding is rate-limiting for diffusion. If the IGME analysis is not properly described or validated, the reliability of these parameters is uncertain.
- **Resolution test** Provide a detailed description of the IGME analysis, including the state definitions, the construction of transition probability matrices, the selection of hyperparameters, and a convergence analysis. Show that the derived rates are robust to the choice of analysis parameters.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Force field validation
- **Claim pointer** The authors state that they obtained force field parameters for ADMA using Gaussian 16, RESP fitting, and the GAFF force field.
- **Evidence pointer** Section "Force field parameters for the asymmetric dimethyl arginine (ADMA) sidechain". Location not provided.
- **Concern** The manuscript does not provide any validation of the ADMA force field parameters. It is not shown that the parameters reproduce known conformational preferences, hydration free energies, or interaction energies with phosphate groups. The choice of the amber99sb-disp force field for the peptides and the amberff99bsc0χOL3 force field for RNA is stated, but the compatibility of the ADMA parameters with these force fields is not discussed.
- **Why it matters** The conclusions depend on the accuracy of the interactions between the guest peptide side chains and RNA. If the ADMA parameters are not validated, the comparison between Arg, ADMA, and Lys may be biased by force field artifacts.
- **Resolution test** Provide validation data for the ADMA force field parameters, such as comparison with quantum mechanical calculations or experimental data. Show that the parameters are compatible with the chosen protein and RNA force fields.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Timescale and sampling
- **Claim pointer** The authors performed approximately 2,000 MD simulations with an average length of 200 ns, accumulating 564.7 μs of simulation time, and used these to characterize the diffusion of guest peptides in the condensate.
- **Evidence pointer** Table 1, Section "MD simulations of the condensate with the guest peptides". Location not provided.
- **Concern** The manuscript does not demonstrate that the simulations have converged with respect to the quantities of interest. The number of independent simulations per system is not clearly stated, and the statistical uncertainty in the reported hydrogen bond counts, interaction numbers, and kinetic rates is not quantified beyond the bootstrapping of the IGME model selection. The timescale of the simulations (200 ns) is short compared to the derived bound-state lifetimes (microseconds), and it is not clear how the kinetic parameters are extrapolated from the simulation data.
- **Why it matters** If the simulations have not converged, the reported differences between the three guest peptides may not be statistically meaningful. The derived kinetic parameters may be unreliable if the simulations do not sample the relevant transitions.
- **Resolution test** Provide a convergence analysis showing that the quantities of interest are stable over the simulation time. Report the number of independent simulations and the statistical uncertainty in the reported values. Show that the derived kinetic parameters are robust to the simulation length.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, Introduction. Location not provided.
- **Issue** The abstract states that the simulations are "sub-millisecond" and the introduction describes the computational challenge of reaching "biologically relevant timescales." The relationship between the cumulative simulation time and the timescale of individual trajectories is not clearly explained.
- **Required correction** Clarify the distinction between cumulative simulation time and the timescale of individual trajectories. State clearly that the 564.7 μs is the total accumulated time across all simulations, not the length of a single trajectory.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Results section
- **Evidence pointer** Section "Guest peptides preferentially interact with the RNA chains in the condensate via hydrogen bonding". Location not provided.
- **Issue** The text states "W2121e observed" which appears to be a typographical error.
- **Required correction** Correct the typographical error to "We observed".

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion of cation-π interactions
- **Evidence pointer** Section "Arg-rich peptides form more hydrogen bonds with RNA of condensate compared to the ADMA-rich and Lys-rich peptides". Location not provided.
- **Issue** The manuscript reports that the number of cation-π interactions is lower for Arg compared to ADMA, but does not discuss the structural or chemical basis for this difference. The potential role of cation-π interactions in the initial recruitment of the peptide into the condensate is not addressed.
- **Required correction** Provide a brief discussion of why Arg forms fewer cation-π interactions than ADMA, and address the potential role of cation-π interactions in the recruitment process.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section
- **Evidence pointer** Section "MD simulations of the protein-RNA condensate". Location not provided.
- **Issue** The methods do not specify the initial configuration of the guest peptide in the condensate, the criteria for placing the guest peptide, or the equilibration protocol for the guest peptide-containing systems.
- **Required correction** Provide details on the initial placement of the guest peptide and the equilibration protocol.

## Risk / unsupported claims
- The claim that hydrogen bonding, rather than cation-π interactions, is the main factor regulating peptide diffusion is unsupported without the quantitative data in Figures 3 and 4.
- The claim that the Arg-rich peptide binds more strongly to the condensate than the ADMA-rich or Lys-rich peptides is unsupported without the KD values in Figure 4d.
- The claim that the simulations reproduce the liquid-like behavior of the condensate is not directly demonstrated with data.
- The claim that the simulation results are consistent with prior fluorescence microscopy experiments is mentioned but the quantitative comparison is not shown.
- The force field parameters for ADMA are not validated, so any conclusions involving ADMA are subject to uncertainty.
- The convergence of the kinetic parameters derived from the IG method is not demonstrated.