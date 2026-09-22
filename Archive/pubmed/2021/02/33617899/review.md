## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) with figure references but no actual figures or supplementary material provided.
- **Assessment boundary** Scientific claims, methodological soundness, and interpretive validity based solely on the supplied text. Figures, tables, and supplementary materials referenced but not available for inspection.
- **Shared manuscript claim summary** The authors use coarse-grained AWSEM-DNA simulations to study the binding dynamics of disordered linker histone H1.0b with a nucleosomal particle. They claim that H1 disordered domains (NTD/CTD) restrict the conformational dynamics of the globular H1 domain and linker DNA arms, resulting in a more compact and rigid chromatosome, and that these domains act as "hands" tethering DNA near the entry-exit site.
- **Visible evidence base** Text descriptions of simulation results, statistical test results (Kolmogorov–Smirnov test), quantitative values for angles and distances, and references to figures (Figures 1–6) and supplementary items (Figures S1–S10, Tables S1–S2, Supplemental Movie 1) that were not provided.
- **Missing materials affecting confidence** All figures, supplementary figures, tables, and the supplemental movie. Simulation parameter details in the Supporting Information. The PDB structure 5NL0 is referenced but not examined. The AWSEM-IDP force field parameters and the specific modifications to the Hamiltonian are only partially described in the main text.

## Reviewer
- **Overall assessment** This manuscript presents a computational study of linker histone H1 binding dynamics using a coarse-grained model. The topic is relevant and timely, and the authors address an important gap in understanding the role of disordered H1 tails. However, the evidence base available for this review is incomplete, as all figures and supplementary materials are missing. The claims are plausible but cannot be fully verified from the text alone. The methodological approach is reasonable, but several technical details and validations are not described in sufficient detail. The manuscript would benefit from clearer presentation of quantitative results and more explicit connections between simulation observations and experimental predictions.
- **Who would be interested in the results, and why** Researchers in chromatin biology, structural biology, and computational biophysics would be interested. The study addresses fundamental questions about how disordered histone tails modulate nucleosome dynamics and chromatin compaction, which has implications for understanding gene regulation, epigenetic mechanisms, and cancer biology. The methodological approach using AWSEM-DNA may also interest computational biologists working on protein-DNA complexes.
- **Major strengths** The study addresses an important and understudied question about the role of disordered H1 domains. The use of a coarse-grained model allows for longer simulation timescales than atomistic simulations. The comparison of three systems (nucleosome alone, with globular H1, with full-length H1) provides a clear framework for isolating the effects of disordered domains. The authors connect their findings to experimental observations, including cryo-EM and NMR studies.
- **Major Concerns** 
  - R1-M1: The central claim that H1 disordered domains "restrict" GH1 dynamics and linker DNA conformation is based on simulation data that cannot be fully evaluated without figures and quantitative distributions. The text provides some values (e.g., Rg values, angle distributions) but the statistical robustness and convergence of these measurements are not adequately described.
  - R1-M2: The coarse-grained model includes several modifications to the AWSEM force field, including a weak Gō potential for the histone octamer and AWSEM-IDP for disordered domains. The validity of these modifications and their potential to bias the results toward the observed outcomes is not sufficiently discussed. The authors note that the ansatz from previous studies was too weak to maintain nucleosome stability, requiring additional arginine-phosphate interactions, but the justification for these parameter choices is not fully provided.
  - R1-M3: The claim that the simulation timescale "approximately corresponds to milliseconds" is not well supported. The conversion from coarse-grained to atomistic timescales is nontrivial and the cited references may not directly justify this equivalence for this specific system.
  - R1-M4: The authors propose a biological mechanism for H1-mediated nucleosome repositioning based on the observation of GH1 escaping the dyad and moving toward the acidic patch. This is an interesting hypothesis, but the text does not provide sufficient evidence that this simulation observation is not an artifact of the model or the specific initial conditions.
- **Minor Comments** 
  - R1-m1: The abstract states "near-atomic resolution" but the model is coarse-grained with three beads per residue. This phrasing may overstate the resolution of the method.
  - R1-m2: The introduction cites many references but the transition to the specific aims of this study could be smoother. The rationale for choosing Xenopus laevis H1.0b is not explicitly stated.
  - R1-m3: The methods section describes the Hamiltonian components but does not provide the actual parameter values or functional forms for the modified terms. This limits reproducibility.
  - R1-m4: The discussion of nucleosome repeat lengths and species-specific H1 variants is interesting but somewhat speculative and not directly supported by the simulation results presented.
  - R1-m5: The authors mention that tails of core histones were excluded, but do not discuss the potential impact of this omission on the results.
- **Technical failings that need to be addressed before the case is established** The manuscript cannot be fully assessed without the figures and supplementary materials. The statistical analysis of the simulation data (e.g., error bars, convergence checks, block averaging) is not described. The sensitivity of the results to model parameters (e.g., the strength of the Gō potential, the Debye-Hückel screening length, the contact distance threshold) is not explored. The timescale conversion claim needs more rigorous justification.
- **Assessment against Nature-style criteria** 
  - Originality: The study addresses a question that has been partially explored but the specific focus on the differential roles of globular versus disordered H1 domains using a near-atomic coarse-grained model is somewhat novel. However, similar conclusions about H1 tail function have been suggested by experimental studies, so the originality is moderate.
  - Scientific importance: Understanding H1 dynamics is important for chromatin biology, and the potential mechanism for nucleosome repositioning is of interest. However, the importance is somewhat limited by the coarse-grained nature of the model and the lack of direct experimental validation.
  - Interdisciplinary readership: The topic bridges structural biology, biophysics, and chromatin biology. The manuscript is likely to appeal to a specialized audience rather than a broad interdisciplinary readership.
  - Technical soundness: The methodological approach is reasonable but the lack of detail on parameterization and validation, combined with the missing figures, prevents a full assessment of technical soundness.
  - Readability for nonspecialists: The manuscript is generally well-written but assumes familiarity with chromatin structure and simulation methods. Some terms (e.g., "winged-helix motif", "AWSEM") are not explained for a general audience.
- **Recommendation posture** Supportive if technical concerns are resolved and the full evidence base is provided. The core claims are plausible and the study addresses an important question, but the current submission cannot be fully evaluated without the missing materials and additional methodological details.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** "H1 disordered domains restrict the dynamics and conformation of both globular H1 and linker DNA arms, resulting in a more compact and rigid chromatosome particle."
- **Evidence pointer** Figures 2, 3, 5; location not provided for quantitative values
- **Concern** The central claim of the paper is that disordered H1 domains restrict GH1 dynamics and linker DNA conformation. However, the evidence for this claim is presented in figures that are not available for review. The text provides some quantitative values (e.g., Rg of 13.6 ± 4.2 Å vs. 10.4 ± 3.2 Å, angle distributions) but does not describe the statistical methods used to compute these values, the number of independent samples, or the convergence of the simulations. Without seeing the actual distributions and error estimates, it is impossible to assess whether the observed differences are statistically significant and biologically meaningful.
- **Why it matters** The central conclusion of the paper rests on the quantitative comparison between systems with and without disordered H1 domains. If the differences are not robust or are within statistical noise, the main claim would be unsupported.
- **Resolution test** Provide the figures with full distributions, error bars, and statistical tests. Describe the convergence criteria and the number of independent simulations used for each measurement. Show that the differences between systems are reproducible across independent runs and are not sensitive to the choice of analysis parameters.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological rigor
- **Claim pointer** "We used a coarse-grained computational model, AWSEM-DNA, to simulate the H1.0b-nucleosome complex."
- **Evidence pointer** Methods section, "Hybrid coarse-grained model for the H1-nucleosome complex"; location not provided
- **Concern** The model includes several modifications to the standard AWSEM force field: an explicit Debye-Hückel electrostatic term, a weak Gō potential for the histone octamer, and AWSEM-IDP for the disordered domains. The authors also added additional Lennard-Jones interactions between arginine Cβ and DNA phosphate beads to maintain nucleosome stability. These modifications are described qualitatively but the parameter values, the rationale for their selection, and the sensitivity of the results to these parameters are not provided. The authors note that previous ansatz interactions were "too weak" to maintain stability, but do not describe how the new parameters were chosen or validated.
- **Why it matters** The conclusions depend on the accuracy and appropriateness of the force field. If the modifications introduce biases (e.g., over-stabilizing certain conformations), the observed dynamics may not reflect the true behavior of the H1-nucleosome complex. Without parameter details and validation, the reliability of the results cannot be assessed.
- **Resolution test** Provide the full Hamiltonian with all parameter values. Describe the validation of the modified force field against experimental data or atomistic simulations. Show that the results are robust to reasonable variations in the key parameters (e.g., the strength of the Gō potential, the Debye-Hückel screening length, the contact distance threshold).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation
- **Claim pointer** "This coarse-grained timescale approximately corresponds to milliseconds of simulation time when explicit solvent atomistic molecular dynamics are carried out for the same systems."
- **Evidence pointer** Methods section, "Simulation details"; location not provided
- **Concern** The claim that 3 μs of coarse-grained simulation corresponds to milliseconds of atomistic simulation timescale is not well justified. The conversion between coarse-grained and atomistic timescales is system-dependent and requires careful analysis of the effective friction and diffusion coefficients. The cited references (95–97) may provide general guidance, but the specific applicability to this protein-DNA system is not demonstrated.
- **Why it matters** The biological interpretation of the observed dynamics depends on the actual timescales being probed. If the effective timescale is much shorter than claimed, the observed conformational changes may not be relevant to biological processes.
- **Resolution test** Provide a more rigorous justification for the timescale conversion, either through direct comparison with atomistic simulations of similar systems or through analysis of the effective diffusion coefficients in the coarse-grained model. Alternatively, temper the claim to reflect the uncertainty in the mapping.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Biological relevance
- **Claim pointer** "Our observation of H1 breaking symmetry at the center of the nucleosome might subtly lower the energetic barrier at the pseudo-dyad, allowing nucleosomal looping in advance of sliding and repositioning along the DNA fiber."
- **Evidence pointer** Discussion section; location not provided
- **Concern** The authors propose a mechanistic hypothesis for H1-mediated nucleosome repositioning based on the observation that GH1 can escape the dyad and move toward the acidic patch. While this is an interesting idea, the text does not provide sufficient evidence that this observation is not an artifact of the model or the specific initial conditions. The authors note that this behavior is "novel" but do not discuss whether it has been observed in other simulations or experiments.
- **Why it matters** The biological significance of the study is enhanced if the observed dynamics can be linked to known functions of H1. However, if the escape behavior is a rare event or an artifact, the proposed mechanism would be weakened.
- **Resolution test** Provide quantitative analysis of the frequency and duration of GH1 escape events. Discuss whether this behavior is robust across different initial conditions and model parameters. Compare with any available experimental or computational evidence for H1 dynamics near the dyad.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first paragraph
- **Issue** The abstract states "near-atomic resolution" but the model is coarse-grained with three beads per residue. This phrasing may overstate the resolution of the method and could mislead readers.
- **Required correction** Replace "near-atomic resolution" with a more accurate description, such as "residue-level resolution" or "near-residue resolution."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Introduction
- **Evidence pointer** Introduction, last paragraph
- **Issue** The rationale for choosing Xenopus laevis H1.0b is not explicitly stated. The authors mention that different H1 subtypes bind to different locations on the nucleosome, but do not explain why this particular variant was selected for study.
- **Required correction** Add a sentence explaining the choice of H1.0b, such as its relevance to previous experimental studies or its distinct structural features.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Methods, "Hybrid coarse-grained model" section
- **Issue** The methods section describes the Hamiltonian components but does not provide the actual parameter values or functional forms for the modified terms. This limits reproducibility.
- **Required correction** Provide the full Hamiltonian with all parameter values, either in the main text or in the Supporting Information.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Focus
- **Affected element** Discussion
- **Evidence pointer** Discussion, last paragraph
- **Issue** The discussion of nucleosome repeat lengths and species-specific H1 variants is interesting but somewhat speculative and not directly supported by the simulation results presented. This section could be shortened or more clearly framed as speculation.
- **Required correction** Clearly distinguish between findings from this study and broader speculation about evolutionary implications. Consider moving some of this material to a "Future Directions" section.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods
- **Evidence pointer** Methods, "Simulation details" section
- **Issue** The authors mention that tails of core histones were excluded from the simulations, but do not discuss the potential impact of this omission on the results.
- **Required correction** Add a brief discussion of the potential effects of excluding core histone tails and justify this choice.

## Risk / unsupported claims
- The claim that H1 disordered domains "act as hands" to grasp DNA is a metaphorical interpretation that is not directly supported by the data presented in the text.
- The proposed mechanism for H1-mediated nucleosome repositioning via symmetry breaking at the dyad is speculative and not directly tested in this study.
- The claim that the simulation timescale corresponds to milliseconds is not well supported and should be treated with caution.
- The statement that the on-dyad binding mode is "the most preferable thermodynamic state" is based on simulation data that cannot be fully evaluated without figures and convergence analysis.
- The comparison between H1.0 and H1.5ΔC50 results is mentioned but not described in sufficient detail to assess its validity.