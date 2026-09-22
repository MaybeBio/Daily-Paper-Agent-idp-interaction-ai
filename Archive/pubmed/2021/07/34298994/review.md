## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods) as provided by the user.
- **Assessment boundary** Scientific content, methodological soundness, validity of claims, and presentation quality of the manuscript as submitted. No assessment of editorial fit or publication decision is made.
- **Shared manuscript claim summary** The authors use conventional molecular dynamics (MD) simulations to study the kinase insert domain (KID) of the receptor tyrosine kinase KIT. They compare three forms: a cleaved unconstrained peptide (KIDC), a cleaved peptide with restrained terminal distance (KIDCR), and the KID embedded in the kinase domain (KIDD). They report that KID is intrinsically disordered, that its helical fold is mainly sequence dependent, that the native KID shows reduced folding compared to the cleaved forms, and that KIDCR better reproduces the native KID than KIDC. They propose KIDCR as a suitable model for future studies of KID post-translational effects.
- **Visible evidence base** Abstract; Sections 1 (Introduction), 2 (Results, subsections 2.1–2.6), 3 (Discussion), 4 (Materials and Methods, subsections 4.1–4.2); Figures 1–7 referenced; Tables S1 and Figures S1–S8 referenced as supplementary; no supplementary material provided.
- **Missing materials affecting confidence** Supplementary figures (S1–S8) and tables (S1) are referenced but not provided. Force field validation data, convergence assessments, and detailed simulation setup parameters (e.g., temperature coupling, pressure coupling, equilibration details) are partially described but not fully specified. No experimental validation data are provided.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant and timely question about the conformational behavior of the KIT kinase insert domain, an important signaling hub. The use of conventional MD simulations to characterize intrinsic disorder is appropriate, and the comparison between cleaved and native forms is a useful approach. However, the study has significant limitations in sampling, validation, and statistical rigor. The central claims about sequence-dependent folding and allosteric control by the kinase domain are plausible but not fully established from the provided evidence. The free energy landscape analysis is descriptive rather than quantitative, and the recommendation of KIDCR as a generic model requires stronger justification. The manuscript is clearly written and accessible, but the technical soundness needs improvement before the conclusions can be considered robust.
- **Who would be interested in the results, and why** Researchers studying receptor tyrosine kinase signaling, particularly KIT and its downstream pathways, would be interested in the structural characterization of the KID. The broader community studying intrinsically disordered proteins and their conformational ensembles would also find the methodological approach relevant. Computational biologists using MD simulations to study flexible domains would benefit from the comparative analysis of cleaved versus native forms.
- **Major strengths** The study addresses an important and understudied region of KIT. The use of multiple simulation replicas and the comparison of three different KID forms (cleaved, restrained, native) is a thoughtful design. The analysis of intramolecular contacts and the identification of "pseudo-rigid" segments provide useful insights. The free energy landscape approach using multiple collective variables is a reasonable strategy for describing conformational ensembles. The manuscript is well-written and the figures are informative.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (sampling convergence), R1-M2 (force field validation), R1-M3 (statistical analysis of free energy landscapes), R1-M4 (support for the KIDCR recommendation).
- **Assessment against Nature-style criteria** **Originality**: Moderate. The application of MD to study KID disorder is not entirely new, but the systematic comparison of cleaved versus native forms adds some novelty. **Scientific importance**: Moderate to high. Understanding KID conformational behavior is relevant for KIT signaling, but the direct biological implications are not demonstrated. **Interdisciplinary readership**: Limited. The manuscript is primarily of interest to computational structural biologists and KIT signaling researchers. **Technical soundness**: Needs improvement. Sampling convergence, force field validation, and statistical rigor are insufficiently addressed. **Readability for nonspecialists**: Good. The manuscript is clearly written and the concepts are explained well, though some methodological details may be challenging for non-experts.
- **Recommendation posture** Supportive if technical concerns are resolved. The core question is relevant and the approach is reasonable, but the current evidence does not fully support the central claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the MD simulations provide "accurate atomistic models" and that the observed conformational ensembles are representative of KID behavior.
- **Evidence pointer** Section 2.1, Section 2.2, Figures 2A–B
- **Concern** The manuscript does not provide evidence that the MD simulations have converged. The RMSD plots (Figure 2A) show variations along each trajectory, but no convergence criteria are defined, and the authors do not demonstrate that the sampled conformations are statistically representative of the equilibrium ensemble. With simulation times of 1.8–2 µs for a disordered domain, convergence is not guaranteed, and the lack of convergence analysis undermines the reliability of all subsequent analyses.
- **Why it matters** If the simulations have not converged, the observed differences between KIDC, KIDCR, and KIDD may reflect incomplete sampling rather than genuine biophysical differences. The central claim that KIDCR better reproduces the native KID would be invalid if the ensembles are not converged.
- **Resolution test** Provide convergence assessments such as block averaging of key observables (RMSD, Rg, helicity), split-half analysis of free energy landscapes, or comparison of independent replicas using statistical tests. Show that the ensembles are stable over time and that the key conclusions are robust to simulation length.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors use the ff99SB force field and claim that the models are "accurate."
- **Evidence pointer** Section 4.2.1, Section 4.2.3
- **Concern** The choice of the ff99SB force field is not justified, and no validation against experimental data or alternative force fields is provided. For intrinsically disordered proteins, force field choice is known to significantly affect conformational ensembles. The authors do not discuss whether ff99SB is appropriate for studying disordered regions, nor do they compare with newer force fields (e.g., ff14SB, CHARMM36m) that are often better optimized for IDPs.
- **Why it matters** If the force field biases the conformational ensemble, the conclusions about KID disorder and folding would be artifacts of the simulation setup rather than genuine properties of the system.
- **Resolution test** Justify the force field choice with references or preliminary validation. Ideally, repeat key simulations with an alternative force field and show that the main conclusions are unchanged. At minimum, discuss the limitations of the chosen force field for IDP studies.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The free energy landscapes (FELs) are described as providing "a direct evaluation of conformational ensembles" and the authors compare the deepest wells across different KID forms.
- **Evidence pointer** Section 2.6, Figure 6, Table S1
- **Concern** The FELs are constructed from the concatenated replicas, but the statistical uncertainty of these landscapes is not assessed. The authors do not report error bars or confidence intervals for the free energy values, and the comparison of the deepest wells between KIDC, KIDCR, and KIDD is based on visual inspection rather than quantitative statistical tests. The number of replicas (4 for KIDC, 2 for KIDD and KIDCR) is small, and the authors do not demonstrate that the FELs are reproducible.
- **Why it matters** Without statistical assessment, the differences in the FELs between the three KID forms could be within sampling noise. The claim that KIDCR better reproduces the native KID requires quantitative evidence that the FELs are significantly different.
- **Resolution test** Provide bootstrap or block-averaged estimates of the FELs with confidence intervals. Use statistical tests (e.g., Kolmogorov-Smirnov or permutation tests) to compare the distributions of key observables between the different KID forms.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The authors suggest that "a cyclic, generic KID would be best suited for future studies of KID post-transduction effects."
- **Evidence pointer** Section 3 (Discussion), Section 2.3
- **Concern** The recommendation of KIDCR as a suitable model for future studies is based on the observation that its FEL is similar to that of KIDD. However, the authors do not provide a quantitative measure of this similarity, and the comparison is based on a limited set of observables (RMSD, Rg, helicity, SASA). The functional relevance of the conformational ensemble is not addressed, and the authors do not demonstrate that KIDCR preserves the key features required for phosphorylation and protein binding.
- **Why it matters** If the recommendation is to be used by other researchers, it must be supported by robust evidence that KIDCR faithfully reproduces the native KID's functionally relevant conformations. Without this, the recommendation is premature.
- **Resolution test** Provide a quantitative comparison of the conformational ensembles (e.g., overlap coefficients, Jensen-Shannon divergence) and demonstrate that key functional features, such as the accessibility of phosphorylation sites and the geometry of tyrosine residues, are preserved in KIDCR relative to KIDD.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.2, Figure 2C
- **Evidence pointer** Figure 2C
- **Issue** The description of the "camel double-humped" contour in the RMSF profiles is not clearly explained. The authors mention this feature but do not provide a detailed interpretation of its structural or functional significance.
- **Required correction** Clarify what the "camel double-humped" contour represents and discuss its implications for KID dynamics.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2.4, Figure 3
- **Evidence pointer** Figure 3A–F
- **Issue** The contact maps are described as "sufficiently different between replicas" and "strikingly similar between distinct KID entities," but the criteria for these qualitative assessments are not defined. The Fisher-Rao distance and MDS analysis are mentioned but not explained in sufficient detail for the reader to understand the methodology.
- **Required correction** Provide a brief explanation of the Fisher-Rao distance and MDS methodology, and define the criteria used to assess similarity or difference in the contact maps.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Section 2.5, Figure 5
- **Evidence pointer** Figure 5F
- **Issue** The statement that the "great dispersion of the hydroxyl groups" of tyrosine residues is a consequence of the variability of their geometry is not well supported. The authors do not provide a quantitative measure of this dispersion or its relationship to the tetrahedron geometry.
- **Required correction** Provide quantitative data on the dispersion of hydroxyl groups and its correlation with the tetrahedron geometry, or soften the claim.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Methodology
- **Affected element** Section 4.2.2
- **Evidence pointer** Section 4.2.2
- **Issue** The equilibration protocol is described briefly, but the temperature and pressure coupling parameters are not specified. The use of the Berendsen thermostat and Monte Carlo barostat is mentioned, but the coupling constants are not given.
- **Required correction** Provide the specific coupling parameters and any other relevant simulation details to ensure reproducibility.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Section 3 (Discussion)
- **Evidence pointer** Section 3
- **Issue** The discussion of the functional implications of KID disorder is somewhat speculative. The authors suggest that transient helices "maximize their recognisability" to signaling proteins, but this hypothesis is not directly tested or supported by the data.
- **Required correction** Clearly distinguish between data-supported conclusions and hypotheses, and consider discussing alternative interpretations.

## Risk / unsupported claims
- The claim that the MD models are "accurate" is not supported by validation against experimental data or alternative methods.
- The claim that KIDCR "better reproduces the native KID" is based on qualitative comparison of FELs without statistical testing.
- The suggestion that a "cyclic, generic KID" is suitable for future studies is not fully justified by the presented data.
- The statement that the helical fold of KID is "mainly sequence dependent" is inferred from the observation that some helices are conserved across forms, but this is not directly tested (e.g., by mutation or sequence analysis).
- The claim that the "collapse induced by the intramolecular force conquers the solvent-induced expansion" is not quantitatively supported by the data presented.
- The functional significance of the "pseudo-rigid" segments and their role in KID signaling is speculative and not experimentally validated.