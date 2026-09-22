## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, technical soundness, and claims as presented in the provided manuscript
- **Shared manuscript claim summary** The authors present a multi-technique study of the N-terminal low-complexity domain of EWS (EWSLCD), reporting that it is intrinsically disordered, phase separates with a lower saturation concentration than FUSLCD, and that tyrosine residues, particularly in the N- and C-terminal regions, drive both intramolecular compaction and intermolecular interactions underlying phase separation. The authors further claim that dilute-phase intramolecular contacts inform on condensed-phase interactions.
- **Visible evidence base** Abstract, Introduction, Results, Discussion, Conclusion, Experimental Procedures, figure legends referenced in text
- **Missing materials affecting confidence** Figures, tables, and supplementary materials referenced but not provided; raw NMR data, simulation trajectories, and analysis scripts not available

## Reviewer
- **Overall assessment** This manuscript addresses an important gap in understanding the molecular determinants of phase separation in the FET protein family, specifically for EWS, which has been understudied relative to FUS. The combination of NMR, microscopy, and atomistic simulations is appropriate and potentially powerful. However, the absence of all figures, tables, and supplementary materials makes it impossible to evaluate the quality of the data, the validity of the analyses, or the strength of the conclusions. Several claims, particularly regarding the relationship between dilute-phase contacts and condensed-phase behavior, require additional experimental support. The manuscript is potentially significant but currently not fully assessable from the provided material.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates and liquid-liquid phase separation, particularly those focused on FET family proteins, intrinsically disordered proteins, and the molecular grammar of low-complexity domains. Additionally, investigators working on Ewing sarcoma and FET fusion oncoproteins would find the mechanistic insights relevant to understanding oncogenic transformation.
- **Major strengths** The study addresses a clinically relevant protein (EWS) that has been comparatively understudied in the phase separation field. The multi-technique approach combining NMR, microscopy, and simulations is well suited to the question. The comparison between dilute-phase and condensed-phase behavior is conceptually valuable. The mutational analysis targeting tyrosine residues provides a systematic approach to dissecting sequence determinants.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
  - R1-M4
  - R1-M5
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
  - R1-m4
  - R1-m5
  - R1-m6
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** 
  - Originality: The study is original in its focus on EWS LCD, which has been less characterized than FUS. The finding of domain-specific compaction and the relationship between dilute and condensed phases adds new information. However, the overall conceptual framework (tyrosine-driven phase separation in FET proteins) is not entirely novel.
  - Scientific importance: The work has potential importance for understanding FET protein biology and Ewing sarcoma mechanisms. The molecular-level insights could inform therapeutic strategies targeting EWS::FLI1. However, the importance is somewhat incremental given existing knowledge of FUS.
  - Interdisciplinary readership: The topic bridges biophysics, structural biology, and cancer biology, which could attract a broad readership. The clinical relevance to Ewing sarcoma adds to the interdisciplinary appeal.
  - Technical soundness: The combination of techniques is appropriate, but the inability to assess the actual data and analyses prevents a full evaluation. Several methodological details and validations are missing.
  - Readability for nonspecialists: The manuscript is generally well written and accessible, though some sections assume familiarity with NMR and simulation techniques. The clinical context is clearly presented.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript has potential merit, but the absence of figures and supplementary data prevents a proper evaluation. A revised submission with all data available would be required for a fair assessment.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors claim that EWSLCD phase separates at lower protein concentrations than FUSLCD, based on turbidity measurements and pelleting assays.
- **Evidence pointer** Results section "Physiochemical Properties of EWSLCD", Figures 2A-2H (not provided)
- **Concern** The claim of lower saturation concentration for EWSLCD compared to FUSLCD is central to the manuscript's thesis of molecular diversity within the FET family. However, the actual data supporting this comparison are not visible. The turbidity measurements and pelleting assays are described, but the quantitative values, error bars, and statistical comparisons are not presented in the text. Furthermore, the comparison to FUSLCD appears to rely on previously published data, but the specific conditions (temperature, salt, protein concentration ranges) under which the comparison is valid are not clearly stated.
- **Why it matters** The quantitative comparison of phase separation propensity between EWS and FUS is a key finding that distinguishes this work from prior studies. Without visible data, the reader cannot assess whether the difference is robust, reproducible, or within experimental error. This claim underpins the broader conclusion about functional diversity within the FET family.
- **Resolution test** Provide the actual turbidity curves, pelleting assay data, and phase diagrams for both EWSLCD and FUSLCD under matched conditions. Include quantitative Csat values with error bars and statistical analysis. Clearly state the experimental conditions and any differences in protein construct or buffer composition that could affect the comparison.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that PRE NMR data reveal specific intramolecular contacts, particularly involving tyrosine residues, and that these contacts are reduced in tyrosine mutants.
- **Evidence pointer** Results section "Peptide Chain Dynamics and Self-Association of the EWSLCD", Figures 3A-3C, 5A-5B (not provided)
- **Concern** The PRE data are described qualitatively in the text, but the actual spectra, peak assignments, and quantitative PRE rates are not shown. The authors state that "elevated PRE rates were observed" and that "lower PREs are observed in regions that are depleted of tyrosine residues," but without the data, these claims cannot be verified. Additionally, the method for distinguishing intramolecular from intermolecular PRE contributions is described, but the control experiments and their results are not presented. The statement that "intermolecular PREs... did not produce significant PREs beyond the ~2 s−1 background" is critical for the interpretation, but the data supporting this are not visible.
- **Why it matters** The PRE data are the primary experimental evidence for the specific intramolecular contacts that the authors propose drive phase separation. If the PRE analysis is flawed or the data are not robust, the central mechanistic claim of the paper is weakened. The distinction between intra- and intermolecular contributions is essential for the interpretation that dilute-phase contacts inform on condensed-phase behavior.
- **Resolution test** Provide representative PRE spectra, plots of PRE rates versus residue number for each spin label position, and the corresponding diamagnetic controls. Show the data for the tyrosine mutants alongside the wild-type. Include quantitative analysis of the PRE data with uncertainties and clearly describe the criteria for identifying significant PRE effects.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that atomistic simulations reproduce experimental observations and provide mechanistic insight into the role of tyrosine residues in phase separation.
- **Evidence pointer** Results sections "Peptide Chain Dynamics and Self-Association of the EWSLCD" and "Condensed Phase Intermolecular Contacts Mimic Intramolecular Interactions in the Dilute Phase", Figures 3C, 4E-4F, 5C-5E, 6A-6F (not provided)
- **Concern** The simulation methodology is described in the Experimental Procedures, but several critical details are missing. The force field (Amber99SBws-STQ) is stated, but the choice of water model and ion parameters are only briefly mentioned. The simulation length for the single-chain simulations is stated as 15 μs total, but the number of replicas and the convergence criteria are not described. For the condensed-phase simulations, the system preparation, equilibration protocol, and production length are described, but the analysis methods for extracting contact maps, Csat values, and Rg distributions are not detailed. Most importantly, the comparison between simulated and experimental PRE data is described as "qualitatively similar," but the actual comparison plots are not shown.
- **Why it matters** The simulations are used to support the experimental findings and to provide a molecular-level interpretation. If the simulations are not well validated against experimental data, the mechanistic conclusions drawn from them are speculative. The claim that condensed-phase contacts mimic dilute-phase interactions is a strong statement that requires robust simulation evidence.
- **Resolution test** Provide details on simulation convergence, replica counts, and error analysis. Show direct comparisons between simulated and experimental PRE profiles, Rg distributions, and contact maps. Include validation of the force field for this specific system, such as comparison to experimental chemical shifts or scalar couplings if available.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors claim that mutating tyrosine residues, particularly in the YxY and YxxY motifs, reduces phase separation propensity and increases Csat.
- **Evidence pointer** Results section "Tyrosine Residues Mediate Phase Separation of the EWSLCD", Figures 4A-4F, 5A-5E (not provided)
- **Concern** The mutational analysis is a key component of the study, providing causal evidence for the role of tyrosine in phase separation. However, the data supporting the phase diagrams for the mutants are not visible. The text states that "as the number of tyrosines is decreased the phase boundary shifts to the right," but the actual phase diagrams, turbidity curves, and pelleting assay results for the mutants are not shown. Additionally, the choice of which tyrosines to mutate in the 7YS and 13YS mutants is not fully justified, and the potential for structural or electrostatic perturbations beyond the loss of tyrosine is not discussed.
- **Why it matters** The mutational data are essential to establish causality, not just correlation, between tyrosine content and phase separation. Without visible data, the reader cannot assess whether the effect is specific to tyrosine or a general consequence of sequence perturbation. The interpretation that specific tyrosine motifs are important requires a more detailed analysis.
- **Resolution test** Provide phase diagrams, turbidity curves, and pelleting assay data for all mutants alongside the wild-type. Include a table of Csat values with error bars and statistical comparisons. Discuss the rationale for the specific mutations and consider additional controls, such as mutations that preserve aromatic character but alter spacing.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Conceptual framework
- **Claim pointer** The authors claim that "intramolecular interactions leading to the collapse of the C-terminal and N-terminal regions in the dilute phase also contribute to the phase separation of EWSLCD via intermolecular interactions."
- **Evidence pointer** Results section "Condensed Phase Intermolecular Contacts Mimic Intramolecular Interactions in the Dilute Phase", Discussion
- **Concern** This is a strong claim that posits a direct correspondence between dilute-phase intramolecular contacts and condensed-phase intermolecular interactions. While the correlation between contact maps in the two phases is presented as evidence, the causal relationship is not established. The authors acknowledge that the condensed-phase simulations show chain expansion, which complicates the interpretation. The claim would be strengthened by a more nuanced discussion of how intramolecular contacts in the dilute phase relate to intermolecular contacts in the condensed phase, and whether this relationship is unique to EWSLCD or a general property of phase-separating proteins.
- **Why it matters** This claim is central to the conceptual contribution of the paper, as it suggests that dilute-phase measurements can be used to predict condensed-phase behavior. If this relationship is not robust, the practical implications of the work are diminished.
- **Resolution test** Provide a more detailed analysis of the relationship between intra- and intermolecular contacts, such as a quantitative comparison of contact types and strengths in the two phases. Discuss potential caveats and alternative interpretations. Consider whether the relationship holds for the tyrosine mutants.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that "MD simulations revealed the tyrosine-rich termini exhibit compact conformations with unique contact networks," but the term "unique" is vague. It is unclear whether this means unique to EWSLCD, unique compared to FUSLCD, or unique among the FET family.
- **Required correction** Clarify what "unique" refers to and provide a more specific description of the contact networks.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Experimental Procedures, NMR section
- **Evidence pointer** Experimental Procedures, "Nuclear Magnetic Resonance"
- **Issue** The NMR experiments are described, but the specific pulse sequences, temperature calibration, and referencing methods are not provided. The concentration of the protein samples and the buffer conditions for NMR are also not stated.
- **Required correction** Provide complete details of NMR data acquisition and processing, including sample conditions, temperature, and referencing.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Results, pelleting assays
- **Evidence pointer** Results section "Physiochemical Properties of EWSLCD"
- **Issue** The pelleting assays are described as showing that "more than two-thirds is being incorporated into condensates" at 25 μM EWSLCD. However, the number of replicates and the error bars for these measurements are not reported.
- **Required correction** Report the number of replicates and the standard deviation or standard error for the pelleting assay data.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion of the O-linked-N-acetylglucosaminylation (O-GlcNAc) modification is speculative. The authors state that "the addition of a sugar moiety could reduce the probability for π−π contact formation," but no experimental data are presented to support this hypothesis.
- **Required correction** Clearly label this as a hypothesis and consider discussing how it could be tested experimentally.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, condensed phase simulations
- **Evidence pointer** Results section "Condensed Phase Intermolecular Contacts Mimic Intramolecular Interactions in the Dilute Phase"
- **Issue** The condensed phase simulations are described as using 25 EWSLCD chains, but the total simulation time and the number of replicas are not stated in the Results section. This information is only partially available in the Experimental Procedures.
- **Required correction** State the simulation length and number of replicas in the Results section for clarity.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction
- **Evidence pointer** Introduction
- **Issue** The introduction states that "much of our understanding about EWS phase separation has been inferred from studies of FUS," but does not cite specific studies that have directly examined EWS phase separation prior to this work. This makes it difficult to assess the novelty of the current study.
- **Required correction** Provide a more comprehensive literature review of prior EWS phase separation studies, including any conflicting or supporting findings.

## Risk / unsupported claims
- The claim that EWSLCD phase separates at lower concentrations than FUSLCD is not assessable without the actual data and statistical comparisons.
- The claim that specific intramolecular contacts involving tyrosine residues drive phase separation is not fully supported without visible PRE data and mutational analysis results.
- The claim that dilute-phase intramolecular interactions directly inform on condensed-phase intermolecular interactions is a strong interpretation that requires more robust evidence.
- The hypothesis regarding O-GlcNAc modification reducing π−π contact formation is speculative and not supported by experimental data in this manuscript.
- The statement that the simulation force field "adeptly captures the NMR-derived properties of disordered proteins" is not validated for EWSLCD specifically in the provided text.
- The claim that the study provides "insights useful for understanding the pathogenesis of oncogenic fusion proteins such as EWS::FLI1" is a reasonable extrapolation but is not directly tested in this work.