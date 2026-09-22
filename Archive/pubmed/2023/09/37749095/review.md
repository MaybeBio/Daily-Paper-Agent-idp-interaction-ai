## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and figure legends
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and conclusions as presented in the manuscript
- **Shared manuscript claim summary** The authors propose that multivalent tyrosine-mediated interactions, particularly tyrosine-proline contacts, drive the phase separation of the carboxy-terminal domain (CTD) of RNA polymerase II, and that these interactions also mediate co-recruitment of the human Mediator complex into condensates.
- **Visible evidence base** Phase separation assays (DIC and fluorescence microscopy, DLS), NMR spectroscopy (NOESY, TROSY, HSQC, RDC), Rosetta structure calculations, hierarchical chain growth ensembles, all-atom MD simulations, site-directed mutagenesis, and structural analysis of a preinitiation complex (PDB 7ENC)
- **Missing materials affecting confidence** Supplementary figures and tables referenced but not provided; source data not available; detailed NMR assignment tables not shown; MD simulation input parameters only partially described; statistical analysis details for FRAP and DLS experiments not fully specified

## Reviewer

- **Overall assessment** This manuscript addresses a timely and important question regarding the molecular driving forces of CTD phase separation. The combination of experimental and computational approaches is commendable, and the identification of tyrosine-proline interactions as key mediators of CTD condensation is a potentially significant advance. However, several technical concerns regarding the interpretation of NMR data in condensed phases, the specificity of the proposed interaction network, and the quantitative support for the co-recruitment model need to be addressed before the conclusions can be fully accepted.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, transcription regulation, RNA polymerase II biology, and intrinsically disordered proteins. The findings may also be relevant to those investigating the role of tyrosine-based interactions in other low-complexity domains and to computational biologists developing models of protein condensation.

- **Major strengths** The study combines multiple orthogonal techniques to address a mechanistically challenging question. The use of physiologically relevant conditions (no crowding agents for CTD alone) strengthens the relevance of the findings. The systematic mutagenesis approach to dissect the role of tyrosine residues is well designed. The extension to the Mediator complex adds biological significance beyond in vitro phase separation of isolated CTD.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of NMR interpretation in condensed phases
- **Claim pointer** The authors claim that "Tyr-Pro, Tyr-Ser and Tyr-Thr contacts are abundant inside CTD condensates" based on 2D 1H-1H NOESY spectra recorded in phase-separated conditions.
- **Evidence pointer** Figure 1e, Supplementary Figure 2e-g, Methods section "Nuclear magnetic resonance"
- **Concern** The interpretation of NOESY spectra in phase-separated samples is complicated by several factors that are not fully addressed. The authors acknowledge chemical shift heterogeneity and magnetic susceptibility effects, but the assignment of cross-peaks in the condensed phase relies on comparison to the dilute state. Given that the condensed phase is a distinct environment, the assumption that assignments transfer directly may be problematic. Additionally, the authors do not report how they distinguished intra- versus intermolecular contacts in the condensed state, which is critical for the claim of "multivalent interactions." The statement that "The contacts can be either intra- or intermolecular" is vague and does not provide quantitative support for the proposed intermolecular interaction network.
- **Why it matters** The central claim of the paper is that multivalent intermolecular interactions drive phase separation. Without clear evidence that the observed contacts are intermolecular and not simply intramolecular contacts that persist in the condensed state, the mechanistic conclusion is not fully supported.
- **Resolution test** Provide isotope-filtered NOESY experiments (e.g., 13C-edited/12C-filtered) with mixtures of labeled and unlabeled CTD to unambiguously identify intermolecular contacts. Alternatively, provide quantitative analysis of NOE build-up curves to distinguish intra- from intermolecular contributions, or perform mutagenesis of specific tyrosine residues and demonstrate loss of specific cross-peaks in the condensed phase.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative support for phase separation behavior
- **Claim pointer** The authors state that hCTD and yCTD undergo "temperature- and concentration-dependent self-coacervation" with critical concentrations of ~25 and ~100 μM, respectively.
- **Evidence pointer** Figure 1b-c, Supplementary Figure 2a-b, Methods section "Phase separation assays"
- **Concern** The phase diagrams are presented qualitatively through DLS and microscopy, but no quantitative turbidity measurements, sedimentation assays, or fluorescence recovery data are shown to define the phase boundaries precisely. The critical concentrations are stated but the method for determining them from the DLS data is not described. Furthermore, the temperature dependence is shown only for a limited range, and the effect of protein concentration on the critical temperature is not systematically explored.
- **Why it matters** The quantitative phase behavior is foundational to the claim that CTD undergoes liquid-liquid phase separation. Without rigorous determination of phase boundaries and demonstration of reversibility, the assignment of the observed phenomena to phase separation rather than aggregation or other forms of clustering is not fully established.
- **Resolution test** Provide quantitative phase diagrams with multiple techniques (e.g., turbidity, fluorescence microscopy with droplet counting, sedimentation assays) and demonstrate reversibility of phase separation upon temperature cycling. Include error analysis and statistical treatment of replicate measurements.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Specificity of tyrosine-proline interactions
- **Claim pointer** The authors claim that "multivalent interactions involving tyrosine impart temperature- and concentration-dependent self-coacervation" and that Tyr-Pro interactions are specifically enriched in condensed states.
- **Evidence pointer** Figures 4-7, Supplementary Figures 7-8
- **Concern** The mutagenesis data show that replacing all tyrosines with leucine abolishes phase separation, while phenylalanine substitution preserves it. This suggests that aromaticity, not specifically tyrosine, is important. The claim that Tyr-Pro interactions are specifically enriched relies on MD simulations, but the force field parameters for aromatic interactions in disordered proteins are known to be challenging. The comparison to other low-complexity proteins (LGE1, FUS) is interesting but does not establish specificity for Tyr-Pro over other aromatic-aliphatic interactions.
- **Why it matters** The proposed mechanism of Tyr-Pro interactions as the specific driving force has implications for understanding CTD phase separation and for designing interventions. If the effect is simply due to general aromatic interactions, the conclusions need to be reframed.
- **Resolution test** Perform additional mutagenesis experiments with tryptophan or other aromatic residues to test whether the effect is specific to tyrosine. Provide experimental validation of the MD-predicted contact preferences using NMR or other biophysical methods in the dilute phase where assignments are more reliable.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Relevance of Mediator co-recruitment experiments
- **Claim pointer** The authors claim that "the network of multivalent interactions involving tyrosine is responsible for the co-recruitment of the human Mediator complex and CTD during phase separation."
- **Evidence pointer** Figure 8, Supplementary Figure 9
- **Concern** The co-recruitment experiments are performed with a 10-fold excess of CTD over Mediator (5 μM CTD vs 500 nM Mediator), and the conditions used (16% w/v dextran for WT and variants) differ from those used for CTD alone. The claim that tyrosine residues are responsible for co-recruitment is based on the observation that Tyr-to-Ser variants co-localize less with Mediator condensates, but the quantitative analysis is not shown. Additionally, the structural analysis of the preinitiation complex (PDB 7ENC) is used to support the interaction model, but the relevance of these static structures to the dynamic condensate state is not established.
- **Why it matters** The Mediator co-recruitment is presented as a key biological implication of the findings. If the experimental conditions are not carefully controlled and the quantitative analysis is not provided, the strength of this claim is weakened.
- **Resolution test** Provide quantitative co-localization analysis with statistical significance testing. Perform titration experiments to determine the stoichiometry of CTD and Mediator in mixed condensates. Use CTD variants with specific tyrosine mutations to map the residues required for Mediator recruitment.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Computational model validation
- **Claim pointer** The authors state that "the NMR-biased ensembles fulfill the experimentally determined hydrodynamic radii" and that the calculated ensembles reproduce experimental observations.
- **Evidence pointer** Figure 3, Supplementary Figure 6, Methods section "Rosetta structure calculations" and "Hierarchical chain growth ensembles"
- **Concern** The validation of the computational ensembles against experimental data is limited to hydrodynamic radius and a subset of NOE contacts. The Rosetta calculations used only 36 NOE restraints and 16 RDCs for a 63-residue peptide, which may be insufficient to define the conformational ensemble uniquely. The agreement between the hierarchical chain growth ensemble and the Rosetta ensemble is not quantitatively compared. The selection of the final 24 models from 200 is not described with clear criteria.
- **Why it matters** The computational models are used to support the proposed interaction network. If the ensembles are not well-validated, the structural interpretations derived from them are uncertain.
- **Resolution test** Provide cross-validation of the computational ensembles against additional experimental data (e.g., paramagnetic relaxation enhancement, small-angle X-ray scattering). Report the convergence of the structure calculations and the uncertainty in the ensemble. Compare the two computational approaches quantitatively using ensemble overlap metrics.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 1c
- **Evidence pointer** Figure 1c
- **Issue** The phase diagram in Figure 1c is difficult to interpret. The dotted lines indicating "tendencies in conditions where sedimentation occurred" are not clearly defined, and the reader cannot determine the exact phase boundaries from the figure.
- **Required correction** Provide a clear phase diagram with labeled regions (one-phase vs. two-phase) and indicate the method used to determine the boundaries. Consider using a contour plot or a table of conditions tested.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Multiple figures
- **Evidence pointer** Figures 1, 4, 8; Supplementary Figures 2, 7, 9
- **Issue** The number of replicates and statistical tests used are not consistently reported across experiments. For example, the DLS measurements in Figure 1c show error bars but the number of independent measurements is not stated in the legend.
- **Required correction** Add statistical details to all figure legends, including the number of replicates, the type of statistical test used, and the definition of error bars.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** FRAP experiments
- **Evidence pointer** Methods section "Fluorescence recovery after photobleaching (FRAP)"
- **Issue** The FRAP methodology is described briefly, and the differences in conditions between the CTD variants (16% dextran) and WT/Y1F/Y1L (16% dextran) are noted but not explained. The recovery curves in Figure 4b show only two conditions, and the fitting procedure is not described.
- **Required correction** Provide a more detailed description of the FRAP experiments, including the fitting model used, the number of replicates, and the rationale for the different conditions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation of MD simulations
- **Affected element** Figures 6-7
- **Evidence pointer** Figures 6-7
- **Issue** The MD simulation analysis focuses on Tyr-Pro contacts, but the authors do not discuss the potential contribution of other interaction types (e.g., pi-pi stacking between tyrosines, cation-pi interactions with lysine/arginine) that may also be present in the condensed phase.
- **Required correction** Acknowledge the potential contribution of other interaction types and discuss how the proposed Tyr-Pro interactions fit within the broader context of known forces driving phase separation of low-complexity domains.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion of the relationship between CTD phase separation and transcription regulation could be expanded to include more recent work on the role of phosphorylation in modulating condensate properties and the potential connection to disease-associated mutations in the CTD.
- **Required correction** Add a brief discussion of how the findings relate to recent studies on CTD phosphorylation and phase separation, and consider mentioning any known disease-associated CTD mutations that might affect the proposed interaction network.

## Risk / unsupported claims
- The claim that Tyr-Pro interactions are "responsible for the co-recruitment of the human Mediator complex and CTD" is not fully supported by the data presented, as the quantitative co-localization analysis is not shown and the mechanistic link is inferred rather than demonstrated.
- The statement that "the network of multivalent interactions involving tyrosine is responsible for the co-recruitment" overstates the evidence, as the experiments show correlation (reduced co-localization with Tyr-to-Ser variants) but not causation.
- The assertion that the NMR-observed contacts in the condensed phase are "abundant" is not quantified, and the relative contribution of intra- versus intermolecular contacts is not established.
- The claim that the computational ensembles "fulfill the experimentally determined hydrodynamic radii" is based on a single observable and may not provide sufficient validation for the proposed structural model.
- The extrapolation from the in vitro phase separation of isolated CTD to the behavior of full-length Pol II in cells is not directly supported by the experimental data presented.