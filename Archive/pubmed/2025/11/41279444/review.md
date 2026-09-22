## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) without figures or supplementary material
- **Assessment boundary** Scientific claims, methodological soundness, and internal consistency based solely on the provided text; figures, tables, and supplementary data referenced but not directly examined
- **Shared manuscript claim summary** The authors present a coarse-grained molecular dynamics framework, modified from the Mpipi model, to connect sequence-level features of intrinsically disordered proteins to the viscoelastic properties of biomolecular condensates. They propose that condensate elasticity emerges from the interplay between single-molecule shape memory timescales and mesh reconfigurability timescales, formalized as a "condensate Deborah number." They further report exponential scaling laws relating loss tangent to reduced temperature, and identify mesh heterogeneity, sequence hydrophobicity, and network path redundancy as key determinants of elastic response.
- **Visible evidence base** Text descriptions of simulation protocols, model parameters, and qualitative results; references to figures (Fig. 1–6) and supplementary figures (Fig. S1–S38) that were not provided for direct inspection
- **Missing materials affecting confidence** All figures, tables, and supplementary information; quantitative data values; simulation trajectory details; validation statistics; comparison datasets

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question in the biophysics of biomolecular condensates: how sequence-encoded molecular interactions give rise to macroscopic viscoelastic behavior. The conceptual framework centered on a condensate Deborah number is appealing and potentially impactful. However, the current text, without access to the figures and quantitative data, leaves several central claims insufficiently supported. The exponential scaling laws, the relationship between network topology metrics and elasticity, and the proposed timescale ratio as a predictive descriptor all require direct quantitative evidence that is not visible in the text alone. The methodological modifications to the Mpipi model are described but their validation is only partially presented. The manuscript would benefit from clearer articulation of the novelty relative to prior work by the same group and others, and from a more critical discussion of the limitations of the coarse-grained approach for capturing true viscoelastic responses.

- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, intrinsically disordered proteins, soft matter physics, and polymer rheology would find this work relevant. The proposed condensate Deborah number offers a potentially generalizable descriptor that could bridge molecular-level simulations and experimental rheology. The findings on sequence determinants of elasticity could inform the design of synthetic condensates and the interpretation of disease-associated mutations that alter condensate material properties. The methodological advances in coarse-grained modeling of semi-flexible IDPs may also be of interest to the simulation community.

- **Major strengths**
  1. The conceptual framing around a condensate Deborah number is elegant and provides a potentially unifying descriptor for condensate mechanics.
  2. The study spans multiple scales, from single-molecule conformation to network topology, which is ambitious and commendable.
  3. The systematic exploration of sequence space using Y-S variants is a well-designed approach to isolate specific physicochemical determinants.
  4. The connection to experimental observables (e.g., FRET, passive microrheology) enhances the practical relevance of the proposed framework.
  5. The acknowledgment of limitations, particularly regarding hydrodynamic interactions, demonstrates scientific rigor.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that the modified Mpipi model "captures experimentally determined viscoelastic response of A1-LCD variant condensates" and reproduces experimental phase behavior.
- **Evidence pointer** Results section, first subsection; Fig. 1a–f; Fig. S1, S2, S4, S37
- **Concern** The text states that the model reproduces experimental data, but the quantitative comparison is not presented in the text. Without seeing the actual data overlays, error metrics, or statistical measures of agreement, it is impossible to assess whether the agreement is qualitative or quantitative, and whether it is sufficient to support the subsequent claims built on this validation.
- **Why it matters** The entire subsequent analysis depends on the reliability of the modified model. If the validation is weak or only qualitative, all derived conclusions about sequence determinants of viscoelasticity are compromised.
- **Resolution test** Provide quantitative comparison metrics (e.g., RMSD, correlation coefficients) between simulated and experimental viscoelastic spectra, phase diagrams, and radii of gyration. Show that the model captures not just trends but also magnitudes within acceptable uncertainty.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The manuscript claims that "G′/G′′ increases with T/Tc following exponential scaling laws" and that this is sequence-dependent.
- **Evidence pointer** Results section, second subsection; Fig. 2c,g–i
- **Concern** The exponential scaling relationship is a central quantitative finding, yet the text provides no functional form, no fitted parameters, no goodness-of-fit statistics, and no error bars. The claim that the scaling is "sequence-dependent" is stated but the supporting data are not visible. It is unclear whether the exponential form is theoretically motivated or purely empirical, and whether alternative functional forms were tested.
- **Why it matters** Exponential scaling laws are strong claims that require robust statistical support. If the scaling is not universal or if the functional form is not well-constrained, the predictive power of the framework is diminished.
- **Resolution test** Present the fitted exponential functions with parameters and confidence intervals for each sequence. Show residual plots and compare against alternative functional forms (e.g., power law, stretched exponential). Demonstrate that the exponential form is statistically justified.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Conceptual validity
- **Claim pointer** The manuscript proposes the condensate Deborah number, Decon = τκ2/τξ, as a descriptor that "dictates" the viscoelastic response, with Decon ≪ 1 giving viscous behavior and Decon ≫ 1 giving elastic behavior.
- **Evidence pointer** Results section, final subsection; Fig. 6l,m
- **Concern** The causal claim implied by "dictates" is strong. The text presents correlations between Decon and G′/G′′, but correlation does not establish causation. Moreover, the two timescales τκ2 and τξ are both derived from the same simulations, so they may be internally correlated through the same underlying dynamics. The manuscript does not discuss whether Decon provides predictive power beyond its individual components, or whether it is simply a reparameterization of existing correlations.
- **Why it matters** The condensate Deborah number is positioned as the central conceptual contribution. If it is not demonstrated to be a genuinely predictive and non-redundant descriptor, the novelty of the framework is significantly weakened.
- **Resolution test** Show that Decon predicts viscoelastic response in sequences not used to establish the correlation. Compare predictive power of Decon against τκ2 and τξ individually. Discuss whether the ratio provides information beyond its components and address potential confounding correlations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Methodological rigor
- **Claim pointer** The manuscript states that "most amino acids" in the original Mpipi implementation have μi,j = 1 and νi,j = 1, and that the model was modified with a harmonic angle potential parameterized from CHARMM36m simulations.
- **Evidence pointer** Methods section, first subsection; Fig. S1
- **Concern** The parameterization of the angle potential is described as reproducing the bending potential from atomistic simulations, but the text does not specify how the target bending potential was extracted, how the fitting was performed, what the resulting parameters are, or how sensitive the results are to the choice of κ0 = 20kBT and θ0 = 130°. The transferability of these parameters to other sequences is also not discussed.
- **Why it matters** The angle potential is a key modification that enables viscoelastic behavior. If the parameterization is not rigorously described and tested, the reproducibility and generalizability of the approach are in question.
- **Resolution test** Provide the full parameterization procedure, including the extraction of the target distribution, the fitting method, and the resulting parameters. Show sensitivity analyses for κ0 and θ0. Demonstrate transferability to sequences not used in the parameterization.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation and discussion
- **Claim pointer** The manuscript claims that "entropy-driven structural heterogeneity and reduced IDP hydrophobicity favor condensate elasticity" and that "network path redundancy enhances energy storage."
- **Evidence pointer** Results sections 3 and 4; Fig. 3, 4, 5
- **Concern** The mechanistic interpretations are plausible but the text does not clearly distinguish correlation from causation. For example, reduced hydrophobicity leading to enhanced elasticity is counterintuitive given that stronger interactions typically stiffen materials. The manuscript mentions a "competing effect" but does not provide a quantitative decomposition of the competing contributions. Similarly, the network analysis is purely descriptive; no generative model or perturbation analysis is presented to show that path redundancy causally enhances energy storage.
- **Why it matters** The mechanistic claims are the primary scientific contribution. If they are not rigorously established, the manuscript reads as a set of correlations rather than a mechanistic framework.
- **Resolution test** Perform perturbation analyses (e.g., selectively removing edges in the network, mutating specific residues) to demonstrate causal roles. Provide a quantitative decomposition of enthalpic and entropic contributions to elasticity.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, final sentence
- **Issue** The phrase "opening avenues for the design of condensates with programmable material properties" is vague and not substantiated by specific design rules or predictions in the text.
- **Required correction** Either provide specific, testable design predictions or soften the claim to reflect the exploratory nature of the findings.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Introduction and Results
- **Evidence pointer** Introduction, paragraph 2; Results, subsection 4
- **Issue** The term "condensate Deborah number" is introduced but the manuscript does not discuss its relationship to the classical Deborah number in rheology, nor does it address potential confusion with other dimensionless numbers used in soft matter physics.
- **Required correction** Add a brief discussion of the classical Deborah number and explicitly state how Decon differs or extends the concept.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Internal consistency
- **Affected element** Results, subsection 2
- **Evidence pointer** Fig. 2c,g–i
- **Issue** The text states that "G′/G′′ increases with T/Tc" but the loss tangent is defined as G′′/G′. The notation appears inconsistent between the text and the definition.
- **Required correction** Ensure consistent use of G′/G′′ versus G′′/G′ throughout the text and figure descriptions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods, subsection on viscoelasticity
- **Evidence pointer** Methods, "Determination of viscosity and viscoelasticity"
- **Issue** The description of the Green–Kubo formalism and the subsequent Fourier transform is brief. The choice of correlation time, the number of samples, and the statistical uncertainty of the computed moduli are not reported.
- **Required correction** Provide details on the statistical convergence of G(t) and the uncertainty in the derived moduli.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion
- **Evidence pointer** Discussion, paragraph 1
- **Issue** The discussion of prior theoretical predictions on network heterogeneity cites reference [93] but does not contextualize the present findings against more recent computational studies of condensate viscoelasticity.
- **Required correction** Expand the discussion to include recent relevant work and explicitly state what is new in the present framework.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "Coarse-grained simulation of dense phase systems"
- **Evidence pointer** Methods, subsection 3
- **Issue** The equilibration protocol is described but the criteria for equilibration (e.g., convergence of density, energy, or structural observables) are not specified.
- **Required correction** State the equilibration criteria and provide evidence of convergence.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Results, subsection 5
- **Evidence pointer** Fig. 6l,m
- **Issue** The relationship between Decon and G′/G′′ is presented as a scatter plot, but the text does not report correlation coefficients, significance levels, or the number of independent samples.
- **Required correction** Report statistical measures of the correlation and discuss the independence of the data points.

## Risk / unsupported claims
- The claim that the modified Mpipi model "captures experimentally determined viscoelastic response" is not quantitatively verifiable from the text alone; the comparison data are not shown.
- The exponential scaling laws for G′/G′′ versus T/Tc are stated without functional forms, fitted parameters, or goodness-of-fit statistics.
- The causal claim that Decon "dictates" viscoelastic response is not supported by the text; only correlational evidence is described.
- The mechanistic interpretation that "entropy-driven structural heterogeneity favors elasticity" is presented without a quantitative decomposition of entropic versus enthalpic contributions.
- The claim that "network path redundancy enhances energy storage" is based on descriptive network analysis without perturbation or causal testing.
- The statement that "minimum sequence blockiness is crucial for maintaining fluidity" is presented as a general principle but is only demonstrated for a limited set of Y-S sequences.
- The transferability of the angle potential parameters to sequences beyond those tested is not demonstrated.
- The relationship between simulation timescales and experimentally accessible timescales is not discussed, limiting the direct comparability of Decon to experimental measurements.