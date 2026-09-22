## Review setup
- **Input scope** Full manuscript text (main text, figure captions referenced, acknowledgments, references list)
- **Assessment boundary** Scientific content, methodology, claims, and evidence as presented in the provided manuscript text. Figures and supplementary materials are referenced but not directly inspected.
- **Shared manuscript claim summary** The authors use coarse-grained molecular dynamics simulations of FUS-LCD and DDX4-DR droplets to show that intrinsically disordered proteins within biomolecular condensates exhibit transient subdiffusion, anticorrelated motion consistent with fractional Brownian motion, non-Gaussian displacement distributions, and fluctuating diffusivity that varies between droplet interior and interface regions. They propose that these effects arise from the viscoelastic nature of the droplet environment and confinement, and suggest universality across protein types and force fields.
- **Visible evidence base** Main text descriptions of Figures 1–4, references to Supplementary Figures S1–S8, methodological descriptions in text, discussion of prior work in references.
- **Missing materials affecting confidence** Actual figures and their data values, supplementary information details (simulation parameters, force field specifics, analysis protocols), exact numerical results, error bars, statistical analysis details, and the full methods section. The manuscript appears to be a preprint version (arXiv v1) and may differ from the published version.

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question in the biology and physics of biomolecular condensates: how do intrinsically disordered proteins diffuse within these viscoelastic, membraneless organelles? The authors combine state-of-the-art coarse-grained simulations with rigorous physical analysis frameworks (TAMSD, displacement autocorrelation functions, ergodicity breaking parameters, propagator analysis) to characterize anomalous diffusion in protein droplets. The work is technically competent and the conclusions are largely supported by the described evidence, though several concerns regarding quantitative rigor, interpretation of the non-Gaussianity, and the universality claim require attention. The topic is of broad interest to the soft matter physics, biophysics, and cell biology communities.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates and phase separation (both experimental and computational), soft matter physicists interested in anomalous diffusion in viscoelastic media, biophysicists studying protein dynamics in crowded environments, and cell biologists interested in the physical mechanisms governing reactions and transport within membraneless organelles. The work provides a molecular-scale picture of diffusion in condensates that complements experimental measurements from FRAP, single-molecule tracking, and NMR.
- **Major strengths** The study addresses a fundamental question about the physical nature of diffusion in biomolecular condensates using a well-established coarse-grained model system. The combination of multiple complementary analysis techniques (TAMSD, DAF, RSD, propagators) provides a comprehensive characterization of the anomalous diffusion. The comparison between FUS-LCD and DDX4-DR, different temperatures, and different force fields strengthens the generality of the findings. The discussion of the timescale mismatch between simulations and experiments, and the attempt to reconcile this via friction coefficient adjustment, is honest and useful.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative rigor and statistical validation
- **Claim pointer** The authors claim that proteins exhibit subdiffusion with exponent α ≈ 0.85 within the droplets, and that this is distinct from Brownian motion.
- **Evidence pointer** Figure 1C, described in text; location not provided
- **Concern** The subdiffusion exponent α ≈ 0.85 is reported without error bars, confidence intervals, or information on the distribution of exponents across individual proteins. The text states that TAMSDs of "each protein" exhibit sublinear increase, but no statistical analysis is presented to show how robust this exponent is across the ensemble, across different simulation runs, or across the two proteins studied. Furthermore, the plateau in TAMSD after 1 μs is attributed to confinement, but the transition from subdiffusive to plateau behavior is not quantitatively characterized.
- **Why it matters** The central claim of the paper is that proteins exhibit transient subdiffusion. Without proper statistical characterization of the exponent and its variability, it is impossible to assess whether the observed behavior is truly anomalous or could arise from finite-size effects, insufficient sampling, or the specific choice of analysis window. The exponent value also feeds into the comparison with fractional Brownian motion predictions, so its uncertainty directly affects the strength of the FBM interpretation.
- **Resolution test** Provide the distribution of fitted exponents across individual proteins and across independent simulation replicates, with appropriate error estimates. Show that the exponent is stable across different fitting windows and that the plateau behavior is robust. If possible, compare the measured exponent distribution with expectations from FBM simulations in confined geometries.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of non-Gaussianity
- **Claim pointer** The authors claim that non-Gaussian displacement distributions arise from fluctuating diffusivity due to differences between interior and interface regions, and that this is consistent with FBM with fluctuating diffusivity.
- **Evidence pointer** Figure 2B, described in text; location not provided
- **Concern** The manuscript attributes the observed non-Gaussianity to fluctuating diffusivity, but the analysis does not directly demonstrate that the fluctuations in diffusivity are the cause of the non-Gaussian propagator. The authors show that the DAF is consistent with FBM and that the RSD exhibits slow decay, but they do not perform a quantitative decomposition of the propagator into contributions from different regions or from diffusivity fluctuations. The claim that "individual proteins within the droplet diffuse non-uniformly" is plausible but not directly tested. Additionally, the timescale at which non-Gaussianity is observed (up to Δ = 0.1 μs) is the same timescale at which confinement effects become significant, so the relative contributions of confinement versus diffusivity fluctuations to the non-Gaussianity are not separated.
- **Why it matters** The non-Gaussianity is a key finding of the paper and is presented as evidence for fluctuating diffusivity. If the non-Gaussianity can be explained by confinement alone or by the superposition of populations with different mobilities, the interpretation in terms of fluctuating diffusivity would be weakened. The distinction matters for the physical model proposed and for how these results inform experimental observations.
- **Resolution test** Perform a quantitative decomposition of the propagator, e.g., by conditioning on the region (interior vs. interface) or by comparing with simulations where diffusivity fluctuations are artificially suppressed. Alternatively, fit the propagator with a model that explicitly includes a distribution of diffusivities and show that this model outperforms a simple FBM or confined Brownian model.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Universality claim
- **Claim pointer** The authors claim universality of the fluctuating diffusivity behavior across different proteins (FUS-LCD and DDX4-DR), temperatures, and force fields, and suggest that sequence-specific interactions may not be the primary determinant of diffusion behavior.
- **Evidence pointer** Figures S2–S7, described in text; location not provided
- **Concern** The universality claim is based on qualitative comparisons described in the text ("no clear differences are observed") and presented in supplementary figures that are not directly inspected. The text notes that DDX4-DR has lower density and larger droplet size, leading to faster diffusivity and longer relaxation times, which suggests that quantitative differences do exist. The claim that "diffusive behavior might be more determined by the size of the protein and the density of the droplet than by the sequence-specific interactions" is presented as a tentative conclusion but is not tested systematically. Only two proteins are compared, and the force field variation is not described in detail.
- **Why it matters** The universality claim, if correct, would have significant implications for understanding condensate dynamics across different biological systems. However, the evidence presented is insufficient to support a strong universality claim. The differences between FUS-LCD and DDX4-DR that are acknowledged in the text could be the beginning of a systematic dependence on sequence or density, rather than evidence for universality.
- **Resolution test** Provide quantitative comparisons of the key observables (exponent α, RSD decay, relaxation times) across all conditions, with statistical significance testing. If possible, include a third protein or systematic sequence variants to test the dependence on sequence composition. Clearly state the range of conditions over which the behavior is claimed to be universal.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Timescale mapping and experimental relevance
- **Claim pointer** The authors state that the simulated diffusion coefficients are three orders of magnitude larger than experimental values and that increasing the friction coefficient by factors of 10 to 1000 brings the values into the experimental range, while "the physical mechanism underlying the diffusion process remains qualitatively consistent."
- **Evidence pointer** Discussion section, Figure S8; location not provided
- **Concern** The adjustment of the friction coefficient by up to three orders of magnitude is a significant intervention that could affect the dynamics in ways beyond simply rescaling the diffusion coefficient. The claim that the physical mechanism remains "qualitatively consistent" is not demonstrated quantitatively. For example, the exponent α, the DAF shape, and the RSD behavior could all change when the friction is increased, especially if the dynamics are affected by inertial effects or if the coupling to the viscoelastic environment is altered. The timescale mapping (20 μs simulation to 20 ms real time) is presented without discussion of whether the viscoelastic response of the droplet environment itself would be affected by the friction change.
- **Why it matters** The manuscript aims to provide insights into experimentally relevant timescales. If the friction adjustment changes the qualitative nature of the dynamics, then the conclusions drawn from the simulations may not apply to real systems. The validity of the timescale mapping is central to the broader relevance of the findings.
- **Resolution test** Show quantitatively that the key observables (α, DAF, RSD, propagator shape) are invariant under the friction coefficient variation, or explain how they change and why the conclusions remain valid. Discuss whether the viscoelastic properties of the droplet (e.g., the plateau modulus, relaxation times) are affected by the friction change.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Model limitations and interpretation
- **Claim pointer** The authors interpret the subdiffusion as arising from the viscoelastic nature of the droplet and confinement effects, and attribute the difference in conformation between interior and interface to hydrophobicity.
- **Evidence pointer** Figures 1C, 4A, 4C, described in text; location not provided
- **Concern** The coarse-grained model used (residue-level, implicit solvent) is a significant simplification of real protein systems. The authors acknowledge the absence of side-chain entanglements and hydrodynamic interactions, but the potential impact of these missing interactions on the specific conclusions is not discussed in depth. The attribution of the larger Rg in the interior to "hydrophobicity" is not supported by direct evidence, as the model's interaction parameters are not described in sufficient detail in the main text. The definition of the interface region (based on a radial density cutoff at 20 nm) is reasonable but the sensitivity of the conclusions to this choice is not tested.
- **Why it matters** The physical interpretation of the observed phenomena depends on the fidelity of the model. If the missing interactions (hydrodynamic, entanglements) would qualitatively change the dynamics, the conclusions may not transfer to real systems. The hydrophobicity claim is a specific molecular interpretation that requires more direct evidence.
- **Resolution test** Provide a more detailed description of the model's interaction parameters and how they relate to hydrophobicity. Test the sensitivity of the results to the interface definition. Discuss the potential impact of hydrodynamic interactions and entanglements on the observed dynamics, and whether the conclusions are expected to hold in more detailed models.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Simulation details
- **Evidence pointer** Main text, "We performed coarse-grained (CG) MD simulations... using a residue-revel CG model" (location not provided)
- **Issue** The description of the simulation methodology is brief. Key details such as the specific model parameters, the number of independent simulation runs, the equilibration protocol, and the criteria for determining that the system reached steady state are not provided in the main text.
- **Required correction** Provide a more complete description of the simulation setup in the main text or refer readers to specific sections of the Supplementary Information where these details are fully described.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 1C and related analysis
- **Evidence pointer** Figure 1C, described in text; location not provided
- **Issue** The subdiffusion exponent α is reported as a single value (α ≈ 0.85) without indication of the spread across individual proteins or the uncertainty in the fit.
- **Required correction** Report the mean and standard deviation of α across the protein ensemble, and indicate the number of proteins analyzed and the fitting procedure used.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of ergodicity
- **Affected element** Statement that the diffusion process is ergodic
- **Evidence pointer** Text referring to Figure S1; location not provided
- **Issue** The claim of ergodicity is based on the consistency between ensemble-averaged MSD and TAMSD. However, for finite observation times and confined systems, this consistency can be misleading. The RSD analysis in Figure 3 shows slow decay at short times, which is not fully consistent with a simple ergodic picture.
- **Required correction** Clarify the distinction between ergodicity in the strict sense and the observed consistency between ensemble and time averages, and discuss the implications of the RSD behavior for the ergodicity claim.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Use of "viscoelastic" to describe the droplet environment
- **Evidence pointer** Throughout the manuscript
- **Issue** The term "viscoelastic" is used to describe the droplet environment, but the manuscript does not directly measure or characterize the viscoelastic properties of the droplet (e.g., storage and loss moduli, relaxation spectra). The inference of viscoelasticity is indirect, based on the observed subdiffusive behavior.
- **Required correction** Clarify that the viscoelastic interpretation is inferred from the observed dynamics rather than directly measured, or provide additional analysis that characterizes the viscoelastic response of the droplet.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Comparison with experiments
- **Affected element** Discussion of experimental relevance
- **Evidence pointer** Discussion section; location not provided
- **Issue** The manuscript discusses the timescale mismatch between simulations and experiments but does not provide a detailed comparison with specific experimental measurements of protein diffusion in condensates. The discussion of how the findings relate to experimental observations (e.g., FRAP, single-molecule tracking) is limited.
- **Required correction** Add a more explicit comparison with relevant experimental studies, discussing how the simulation findings could be tested or validated experimentally.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Figure quality and accessibility
- **Affected element** Figures 1–4
- **Evidence pointer** Figure captions not provided in the manuscript text
- **Issue** The figure captions are not included in the provided text, making it difficult to fully assess the figures. The text descriptions are helpful but incomplete.
- **Required correction** Ensure that figure captions are complete and self-contained, clearly describing the data shown, the analysis performed, and the statistical information (error bars, number of replicates).

## Risk / unsupported claims
- The claim that the subdiffusion exponent α ≈ 0.85 is robust and representative of the system is not statistically supported with the information provided.
- The attribution of the non-Gaussian displacement distribution to fluctuating diffusivity is plausible but not directly demonstrated; alternative explanations (confinement, population heterogeneity) are not excluded.
- The universality claim across proteins, temperatures, and force fields is based on qualitative comparisons and is not quantitatively supported.
- The claim that increasing the friction coefficient by factors of 10–1000 does not alter the physical mechanism is not demonstrated with quantitative evidence.
- The attribution of the larger Rg in the droplet interior to "hydrophobicity" is not directly supported by the described analysis.
- The statement that the diffusion process is ergodic requires more careful qualification given the observed RSD behavior and the finite observation times.