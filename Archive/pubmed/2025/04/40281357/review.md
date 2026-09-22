## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary information listing
- **Assessment boundary** Scientific content, technical soundness, and logical coherence of the claims as presented in the provided manuscript text; no assessment of editorial fit or journal-specific policy
- **Shared manuscript claim summary** The authors investigate the molecular mechanism by which 1,6-hexanediol and related alkanediols disrupt FUS phase separation. They report that alkanediols of varying chain length and configuration all suppress FUS low-complexity domain phase separation to different extents, that this suppression correlates with measured hydrophobicity (logP), that charge-charge driven condensates are insensitive to 1,6-HD, and that atomistic simulations reveal direct alkanediol-protein contacts involving hydrophobic and polar residues.
- **Visible evidence base** DIC and fluorescence microscopy of FUS LC droplets; saturation concentration measurements; NMR chemical shift perturbation and relaxation data; CD thermal stability measurements of lysozyme; octanol-water partition coefficient measurements; atomistic MD simulations of single-chain FUS LC with and without hexanediols
- **Missing materials affecting confidence** Full NMR spectra and assignments; simulation trajectory details and convergence analysis; replicate statistics for several key measurements; raw microscopy images; details of the TEV activity assay; force field validation data beyond density comparisons; statistical analysis details for correlation coefficients

## Reviewer
- **Overall assessment** This manuscript addresses a question of considerable interest to the phase separation community: how does 1,6-hexanediol, the most widely used small-molecule probe for condensate liquidity, actually work at the molecular level? The authors combine a commendable range of techniques, including quantitative phase separation assays, NMR spectroscopy, CD, and atomistic simulations, to build a coherent picture in which alkanediols act primarily through hydrophobic interactions with the protein, with chain geometry playing a secondary role. The correlation between measured logP values and both NMR perturbations and phase separation suppression is a particularly valuable contribution, as these hydrophobicity values have been assumed but never directly measured. The demonstration that charge-charge driven condensates are insensitive to 1,6-HD is an important control that strengthens the mechanistic interpretation. However, several technical concerns need to be addressed before the conclusions can be considered fully established. The simulation analysis relies on single-chain simulations, which may not capture the relevant multivalent interactions in the condensed phase. The statistical treatment of some correlations is not fully described. The claim that 1,6-HD does not disrupt charge-mediated phase separation is based on a limited set of model systems. The mechanistic distinction between hydrophobicity and geometry effects, while plausible, rests on a small number of alkanediol variants. These issues are addressable but require additional analysis or experiments.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates and phase separation, particularly those who use 1,6-hexanediol as a tool to probe condensate properties in cells and in vitro. The results will also interest biophysicists studying the molecular determinants of phase separation, computational chemists developing force fields for disordered proteins, and cell biologists who interpret hexanediol sensitivity as evidence for liquid-like behavior. The direct measurement of alkanediol hydrophobicity and its correlation with biological activity provides a useful reference for the broader community.

- **Major strengths** The combination of experimental and computational approaches is well matched to the question. The direct measurement of logP values for the alkanediol series fills a gap in the literature. The correlation between hydrophobicity, NMR perturbations, and phase separation suppression provides a quantitative framework for understanding alkanediol action. The control experiments with charge-charge driven condensates are important for establishing specificity. The simulation analysis provides a plausible molecular mechanism for how alkanediols interact with different residue types.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of simulation conclusions
- **Claim pointer** The authors claim that atomistic simulations reveal that hydroxyl groups in alkanediols mediate interactions with the protein backbone and polar side chains, while the aliphatic chain contacts hydrophobic and aromatic residues, providing a molecular picture of how amphiphilic interactions disrupt FUS phase separation.
- **Evidence pointer** Figure 5, Methods section "Single chain MD simulations of FUS LC with or without hexanediol additives"
- **Concern** The simulations are performed on a single chain of FUS LC in solution, not in the condensed phase. Phase separation is inherently a collective phenomenon involving multivalent interactions between many chains. The relevance of single-chain simulations to understanding how alkanediols disrupt phase separation is not self-evident. The authors show that alkanediols expand the single chain and reduce intramolecular contacts, but the connection between this observation and the suppression of phase separation requires a mechanistic bridge that is not provided. Specifically, it is unclear whether the relevant action of alkanediols is to destabilize intramolecular contacts that stabilize the compact conformations favored in the condensed phase, or to compete for intermolecular interaction surfaces. The simulation analysis also does not address whether the observed contacts are specific or simply reflect the high concentration of cosolvent. The authors should either provide a more direct connection between single-chain behavior and phase separation propensity, or temper the claims about what the simulations demonstrate.
- **Why it matters** The simulation results are presented as providing the molecular mechanism for alkanediol action. If the single-chain simulations do not capture the relevant physics of phase separation, the mechanistic conclusions drawn from them may be misleading. The distinction between intramolecular and intermolecular effects has implications for how the field thinks about cosolvent action on condensates.
- **Resolution test** The authors should demonstrate, either through additional analysis of the existing simulations or through new simulations, that the alkanediol-induced changes in single-chain conformations correlate with changes in the computed or measured phase behavior. Alternatively, they could perform simulations of two or more chains to directly assess how alkanediols affect intermolecular contacts. If this is not feasible, the claims should be revised to clearly state that the simulations provide a model for how alkanediols interact with the protein, not a direct demonstration of how they disrupt phase separation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor of correlation analyses
- **Claim pointer** The authors report strong correlations between measured logP values and both NMR chemical shift perturbations and saturation concentrations, with PCC values of 0.85, 0.77, and 0.92.
- **Evidence pointer** Figure 3F, Figure 4C
- **Concern** The correlation analyses are performed on a small number of data points (six alkanediols at most, and fewer for some comparisons). The PCC values are reported without confidence intervals or p-values. With such small sample sizes, a single outlier can dominate the correlation. The authors also report that removing two outliers improves the correlation from 0.76 to 0.99, which raises questions about the robustness of the relationship. The choice of which points to exclude appears post hoc. The authors should provide a more rigorous statistical treatment, including confidence intervals, p-values, and a sensitivity analysis that shows the correlation is not driven by a single compound.
- **Why it matters** The correlation between hydrophobicity and biological activity is a central claim of the manuscript. If this correlation is not robust, the conclusion that hydrophobicity is the dominant determinant of alkanediol potency is weakened.
- **Resolution test** Provide p-values and confidence intervals for all reported correlation coefficients. Show the correlation plots with all data points labeled. Perform a leave-one-out analysis to demonstrate that no single compound drives the correlation. If outliers are excluded, justify the exclusion criteria a priori rather than post hoc.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of charge-charge insensitivity claim
- **Claim pointer** The authors claim that 1,6-HD does not disrupt charge-mediated phase separation, based on experiments with FUS RGG3-RNA and polyK-polyD condensates.
- **Evidence pointer** Figure 2
- **Concern** The claim that charge-charge mediated phase separation is insensitive to 1,6-HD is based on two model systems: FUS RGG3 with RNA, and polyK-polyD. While these are reasonable models, the conclusion is stated quite broadly. The FUS RGG3-RNA system involves both charge-charge and other interactions (e.g., pi-cation, hydrogen bonding), and the polyK-polyD system is a highly simplified model. The authors should either acknowledge the limited generalizability of this conclusion or provide additional evidence that a range of charge-driven condensates are insensitive to 1,6-HD. Additionally, the modest decrease in phase separation observed for FUS RGG3-RNA with 1,6-HD (Fig. 2B) is described as "not effectively disrupted," but the statistical significance of this decrease is not reported.
- **Why it matters** The insensitivity of charge-driven condensates to 1,6-HD is used to support the claim that the mechanism of action is specific to hydrophobic interactions. If this conclusion is too broad, it could mislead researchers who use 1,6-HD to probe condensate properties in systems where both hydrophobic and charge interactions contribute.
- **Resolution test** Either temper the claim to state that the tested charge-driven systems were insensitive to 1,6-HD, or add additional charge-driven model systems to strengthen the generalizability. Report the statistical significance of the modest decreases observed in Fig. 2B.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic interpretation of NMR data
- **Claim pointer** The authors state that NMR chemical shift perturbations induced by 1,6-HD are consistent with weak interactions throughout the protein, and that the pattern of perturbations does not reveal specific binding sites.
- **Evidence pointer** Figure 3, Appendix Figures S4, S5, S7
- **Concern** The NMR data show small, widespread chemical shift perturbations without clear residue-type specificity. The authors interpret this as evidence for weak, non-specific interactions. However, an alternative interpretation is that the perturbations reflect solvent effects or changes in the conformational ensemble of the protein rather than direct alkanediol-protein interactions. The comparison with the FUS RGG3 construct, which shows similar perturbation magnitudes, is used to argue that the effects are not sequence-specific, but this comparison is made at a single concentration. A more informative experiment would be a titration to determine whether the perturbations saturate or continue to increase with alkanediol concentration, which would distinguish between specific and non-specific effects. The authors should also consider whether the perturbations could be explained by changes in solution dielectric constant or other bulk solvent properties.
- **Why it matters** The NMR data are used to support the claim that alkanediols interact weakly and non-specifically with the protein. If the perturbations are due to bulk solvent effects rather than direct interactions, the mechanistic interpretation would need to be revised.
- **Resolution test** Perform a concentration-dependent NMR titration with 1,6-HD and analyze whether the chemical shift changes follow a binding isotherm or a linear dependence consistent with a bulk solvent effect. Compare the observed perturbations with those induced by a non-interacting cosolvent such as glycerol or ethylene glycol at matched concentrations.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Completeness of the mechanistic model
- **Claim pointer** The authors propose that alkanediols disrupt phase separation by competing for hydrophobic and polar contacts that drive FUS LC self-association, with the aliphatic chain interacting with hydrophobic residues and hydroxyl groups interacting with polar residues.
- **Evidence pointer** Figures 4, 5, Discussion
- **Concern** The proposed mechanism is plausible but incomplete. The authors do not directly demonstrate that alkanediols compete with protein-protein interactions. The CD data with lysozyme show that alkanediols destabilize a folded protein, which is consistent with a general effect on hydrophobic interactions, but lysozyme is not a phase-separating protein and its relevance to FUS phase separation is indirect. The correlation between lysozyme Tm reduction and FUS phase separation suppression is moderate (PCC = 0.77) and based on a small number of compounds. The authors should consider whether the mechanism is truly competitive (i.e., alkanediols occupy interaction surfaces) or whether it is more accurately described as a solvent-mediated effect that alters the driving forces for phase separation. These two models have different implications for how alkanediols would affect other condensate systems.
- **Why it matters** The mechanistic model is the central intellectual contribution of the manuscript. If the model is incomplete or the evidence does not distinguish between competing models, the impact of the work is diminished.
- **Resolution test** Provide additional evidence that directly tests the competitive mechanism, such as measurements of alkanediol binding to FUS LC by ITC or NMR, or simulations that directly compare alkanediol-protein contacts with protein-protein contacts in the condensed phase. Alternatively, the authors could test a prediction of their model, such as the expectation that alkanediols with longer aliphatic chains would be more effective at disrupting condensates stabilized by larger hydrophobic interaction surfaces.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure presentation
- **Affected element** Figure 1
- **Evidence pointer** Figure 1A, 1B
- **Issue** The DIC micrographs in Figure 1A show a qualitative decrease in droplet density with increasing 1,6-HD concentration, but the quantification in Figure 1B is presented as "droplet area" without specifying whether this is total droplet area per field of view, average droplet size, or another metric. The y-axis label is not visible in the text description.
- **Required correction** Clarify the metric being quantified in Figure 1B and ensure the axis labels are explicit. Consider showing representative images at matched time points after sample preparation to control for potential differences in droplet coalescence kinetics.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of methods for NMR relaxation
- **Affected element** Methods section "NMR spectroscopy"
- **Evidence pointer** Methods section
- **Issue** The NMR relaxation experiments (R1, R2, hetNOE) are described, but the analysis details are incomplete. The authors state that data are plotted as "best model parameter and uncertainty corresponding to one s.d. from single replicate," which is unclear. It is not specified how many time points were used for R1 and R2 fitting, whether the data were fit to monoexponential decays, or how uncertainties were propagated.
- **Required correction** Provide complete details of the relaxation data analysis, including the fitting procedure, the number of time points, and how uncertainties were estimated. If only a single replicate was performed, this should be stated explicitly and the limitations acknowledged.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical treatment of CD data
- **Affected element** Figure 4D, 4E
- **Evidence pointer** Figure 4
- **Issue** The CD melting curves in Figure 4D appear to show a single representative experiment, and the Tm values in Figure 4E are presented without error bars or statistical comparison. The text states that "the melting temperature of lysozyme decreases with the addition of simple alcohols as well as diols," but it is not clear whether these differences are statistically significant.
- **Required correction** Report the number of replicates for the CD experiments and provide error bars on the Tm values. Perform and report appropriate statistical tests comparing Tm values across conditions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarification of simulation system composition
- **Affected element** Methods section "Single chain MD simulations"
- **Evidence pointer** Methods section
- **Issue** The simulation methods state that 330 hexanediol molecules were added to achieve a concentration of ~5%, but the exact concentration in molar units is not given. The box size is stated as 12 x 12 x 12 nm, which would give a volume of 1728 nm3. The resulting hexanediol concentration should be calculated and stated. Additionally, it is not clear whether the simulations included ions beyond counterions, and at what concentration.
- **Required correction** State the exact molar concentration of hexanediol in the simulations and specify the ionic conditions. This is important for comparing simulation conditions with experimental conditions.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The Discussion does not explicitly address the limitations of the study. For example, the use of a single-chain simulation, the limited number of alkanediol variants tested, and the use of lysozyme as a model folded protein are not discussed as limitations.
- **Required correction** Add a paragraph acknowledging the limitations of the study and how they might affect the generalizability of the conclusions.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Consistency of terminology
- **Affected element** Throughout
- **Evidence pointer** Abstract, Results, Discussion
- **Issue** The terms "hydrophobic interactions," "hydrophobic contacts," and "hydrophobic driving forces" are used somewhat interchangeably. The authors should be more precise about what they mean by "hydrophobic" in the context of phase separation, particularly given the ongoing debate in the field about the relative contributions of hydrophobic, pi-pi, and cation-pi interactions to FUS phase separation.
- **Required correction** Define what is meant by "hydrophobic" in the context of this work and consider whether the data support a distinction between hydrophobic and aromatic interactions.

## Risk / unsupported claims
- The claim that simulations "show that hydroxyl groups in alkanediols mediate interactions with the protein backbone and polar amino acid side chains, while the aliphatic chain allows contact with hydrophobic and aromatic residues" is based on single-chain simulations and may not capture the relevant interactions in the condensed phase. The connection between single-chain contact preferences and phase separation disruption is not directly demonstrated.
- The claim that "alkanediols decrease the proteins' thermal stability" is based on lysozyme as a model protein. The relevance of this finding to FUS phase separation is indirect, and the manuscript does not demonstrate that 1,6-HD affects the thermal stability of FUS itself.
- The statement that "charge-charge interactions mediating phase separation are not impacted by amphiphilic alcohols" is based on two model systems and may not generalize to all charge-driven condensates.
- The claim that "the magnitude of the CSPs is strongly correlated with the Csat" is based on a small number of data points, and the statistical significance of this correlation is not reported.
- The statement that "1,6-HD and 2,5-HD show the same pattern of effects on FUS LC with different magnitudes" is used to argue for a shared mechanism, but the data supporting this claim are not shown in the main text.
- The Discussion speculates about the implications for cellular studies and the interpretation of hexanediol sensitivity without providing new experimental data to support these speculations.