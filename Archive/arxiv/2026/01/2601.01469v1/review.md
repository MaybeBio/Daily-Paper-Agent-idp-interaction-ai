## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, and claims as presented in the manuscript
- **Shared manuscript claim summary** The authors investigate design principles linking specific features of interparticle interactions to structural and dynamic outcomes in two-dimensional self-assembly, using Molecular Dynamics simulations of single- and two-component systems with SALR potentials (isotropic and anisotropic). They report that tuning repulsive barrier height, decorating attractive wells with oscillatory components, and changing particle geometry control cluster size distributions, intra-cluster ordering, cluster geometry, and inter-cluster crystallization. Key claims include decoupling of internal and global dynamics in oscillatory well systems, induction of internal phase segregation via asymmetric interactions in binary mixtures, and the role of patch stoichiometry and geometry in anisotropic models.
- **Visible evidence base** Main text including Introduction, Model and Methods, Results sections for isotropic SALR and patchy SALR systems, Discussion and Conclusions, and references to Supplementary Information
- **Missing materials affecting confidence** Supplementary Information (referenced extensively but not provided), figures (referenced but not visible), simulation trajectory data, quantitative error bars and statistical analysis details

## Reviewer
- **Overall assessment** The manuscript presents a systematic computational study of design principles in two-dimensional self-assembling systems with SALR interactions. The work addresses a timely and relevant topic at the interface of soft matter physics and biology. The authors have performed extensive Molecular Dynamics simulations across multiple model variants, and the qualitative findings regarding the role of repulsive barriers, oscillatory potentials, and patch geometry are potentially interesting. However, the manuscript in its current form has significant issues that prevent a full evaluation of the claims. The lack of quantitative analysis, missing methodological details, and the absence of the Supplementary Information make it impossible to assess the robustness of the conclusions. The connection to biological condensates, while plausible, remains largely speculative and would benefit from more direct comparison with experimental observations or more specific predictions.
- **Who would be interested in the results, and why** Researchers in soft matter physics, computational chemistry, and biophysics would find this work relevant. Specifically, those studying self-assembly, phase behavior of colloidal systems, and biomolecular condensates would be interested in the design principles proposed. The work could also appeal to experimentalists working on synthetic self-assembling materials who might use the identified principles to guide material design.
- **Major strengths** The systematic approach to isolating specific interaction features and their effects is commendable. The use of multiple model variants (SALR, SALR-Gauss, SALR-OPP, and patchy SALR) allows for a comparative analysis. The focus on two-dimensional systems is well justified given the relevance to interfaces and membranes. The connection between polydispersity control and hyperuniformity is an interesting and potentially important observation.
- **Major Concerns** The manuscript lacks quantitative rigor in several areas. The results are described qualitatively without sufficient numerical data or statistical analysis. The connection between simulation findings and biological condensates is speculative and not well-supported. The absence of the Supplementary Information, which is heavily referenced, makes it impossible to verify many claims. The methods section is incomplete, lacking details on system sizes, equilibration criteria, and analysis procedures.
- **Minor Comments** The manuscript would benefit from clearer figure captions and more detailed descriptions of the simulation setups. Some terminology is used inconsistently (e.g., SALR vs SARL). The discussion of biological implications could be more nuanced and better grounded in the existing literature.
- **Technical failings that need to be addressed before the case is established** The lack of quantitative data supporting the qualitative claims, the absence of error analysis, and the incomplete methodological description are the most significant technical issues.
- **Assessment against Nature-style criteria** 
  - Originality: The work presents a systematic study of design principles, which is somewhat original in its scope, though individual components have been studied before.
  - Scientific importance: The potential implications for understanding and engineering self-assembled materials are significant, but the current evidence does not fully establish the importance of the findings.
  - Interdisciplinary readership: The topic bridges soft matter physics and biology, which could attract a broad readership, but the presentation is likely too specialized for a general audience.
  - Technical soundness: The simulation methodology appears sound in principle, but the lack of quantitative analysis and missing details prevent a full assessment.
  - Readability for nonspecialists: The manuscript is written in a technical style that would be challenging for nonspecialists to follow, particularly the methods and results sections.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript has potential but requires substantial revision and additional analysis before the claims can be properly evaluated.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "oscillatory wells promote solid-like order within clusters while maintaining liquid-like cluster mobility" and that "increasing the repulsive barrier reduces cluster size and polydispersity."
- **Evidence pointer** Section III.1, Section III.2, Figures 5-9 (location not provided)
- **Concern** The claims are presented qualitatively without quantitative support. No numerical values for order parameters, cluster size distributions, or diffusion coefficients are provided in the text. The figures are referenced but not visible, and the Supplementary Information (which presumably contains the quantitative data) is not provided. Without these data, it is impossible to assess the magnitude of the reported effects or their statistical significance.
- **Why it matters** The central claims of the manuscript rest on the ability to distinguish between different structural and dynamic regimes. Without quantitative data and error analysis, the reader cannot determine whether the observed differences between models are significant or within statistical noise.
- **Resolution test** Provide quantitative values for key observables (e.g., order parameters, cluster size distributions, diffusion constants) with appropriate error bars for all systems and temperatures studied. Include statistical analysis demonstrating the significance of the reported differences.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The authors state that "we have used the LAMMPS Molecular Dynamics package to perform NVT simulations" and describe simulation protocols.
- **Evidence pointer** Section II.2 (location not provided)
- **Concern** The methods section is incomplete. Key details are missing, including: the specific integration algorithm and time step used for the patchy systems, the thermostat employed and its parameters, the criteria for equilibration, the number of independent runs performed, and the methods used for cluster analysis. The definition of the reduced time unit for the patchy systems is unclear. Without these details, the simulations cannot be reproduced by other researchers.
- **Why it matters** Reproducibility is a fundamental requirement for computational studies. The lack of methodological detail prevents other researchers from verifying or building upon this work.
- **Resolution test** Provide a complete description of all simulation parameters, including integration algorithms, thermostats, equilibration criteria, and analysis methods. Include details on the number of independent runs and how statistical uncertainties were estimated.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The authors claim that "the extracted principles provide a causal road-map for engineering self-assembled materials and a set of basic physical concepts for interpreting the complex phase behavior of biomolecular condensates."
- **Evidence pointer** Section V (location not provided)
- **Concern** The connection between the simulation results and biological condensates is made through qualitative analogies without direct evidence or specific predictions. For example, the claim that the SALR-OPP model "mirrors the behavior of stress granules" is not supported by any quantitative comparison with experimental data. The authors do not provide specific, testable predictions that would allow experimentalists to validate or falsify their proposed design principles in biological systems.
- **Why it matters** The stated significance of the work depends on its relevance to biological condensates. Without a more rigorous connection to experimental observations or specific predictions, the biological implications remain speculative.
- **Resolution test** Provide specific, quantitative predictions that could be tested experimentally, or compare simulation results with existing experimental data on condensate properties. Alternatively, clearly state the limitations of the model in capturing biological complexity.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "the smaller the polydispersity the more the low-Q behavior tends to hyperuniformity" and that the SALR-Gauss system shows behavior "qualitatively recalling the behavior of stealthy hyperuniform systems."
- **Evidence pointer** Section III.3, Figure 10 (location not provided)
- **Concern** The analysis of hyperuniformity appears to rely on a limited range of Q values and a single temperature. The claim of "stealthy hyperuniform" behavior is made based on qualitative similarity without a rigorous definition or quantitative criterion. The relationship between polydispersity and hyperuniformity is stated as a general principle but is only demonstrated for a limited set of conditions.
- **Why it matters** Hyperuniformity is a specific and well-defined property. Claiming its presence or absence requires rigorous analysis over an appropriate range of length scales and careful consideration of finite-size effects.
- **Resolution test** Provide a more complete analysis of the structure factor at low Q for all systems and temperatures, including finite-size scaling analysis. Define the criterion used to assess hyperuniformity and stealthy hyperuniformity quantitatively.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "asymmetric interactions in a binary SALR mixture can be designed to induce internal phase segregation within condensates" and that this "resembles" observations in TDP-43 condensates.
- **Evidence pointer** Section III.4, Figures 11-13 (location not provided)
- **Concern** The analysis of the binary mixture is presented for a limited set of parameters (two densities, three compositions). The claim that this represents a general design principle is not supported by a systematic exploration of parameter space. The connection to TDP-43 is made through visual similarity of simulation snapshots to fluorescence microscopy images, which is a weak form of evidence.
- **Why it matters** The generality of the proposed design principles is a key claim of the manuscript. Without a more systematic parameter study, it is unclear whether the observed behaviors are specific to the chosen parameters or represent general principles.
- **Resolution test** Provide a more systematic exploration of parameter space (e.g., varying interaction strengths, ranges, and compositions) to demonstrate the generality of the observed phenomena. Provide quantitative comparison with experimental data on TDP-43 condensates rather than qualitative visual similarity.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Throughout the manuscript (location not provided)
- **Issue** The acronym SARL is used inconsistently. In the title and some sections, SALR is used, while in other places (e.g., Section IV), SARL appears. This is confusing and should be corrected.
- **Required correction** Use SALR consistently throughout the manuscript.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Readability
- **Affected element** Introduction
- **Evidence pointer** Section I (location not provided)
- **Issue** The introduction is dense and covers a wide range of topics without a clear narrative thread. The connection between the different motivations (self-assembly, biological condensates, soft matter) could be made more explicit.
- **Required correction** Restructure the introduction to provide a clearer logical flow from the general importance of self-assembly to the specific questions addressed in this work.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Model and Methods
- **Evidence pointer** Section II.1 (location not provided)
- **Issue** The equations for the interaction potentials are not fully written out. The text refers to "an analytic part" and "a strongly repulsive inverse potential" without providing the explicit functional forms.
- **Required correction** Provide the complete mathematical expressions for all interaction potentials used in the simulations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results
- **Evidence pointer** Section III.1 (location not provided)
- **Issue** The description of the vibrational density of states and its interpretation would benefit from a more detailed explanation. The connection between the features in Z(ν) and the underlying physical processes is not fully explained.
- **Required correction** Expand the discussion of the vibrational density of states to make the interpretation more accessible to readers who may not be familiar with this analysis technique.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion
- **Evidence pointer** Section V (location not provided)
- **Issue** The discussion of future directions is brief and does not address some important limitations of the current study, such as the neglect of hydrodynamic interactions, the use of purely pairwise potentials, and the absence of explicit solvent.
- **Required correction** Add a more thorough discussion of the limitations of the models and how they might be addressed in future work.

## Risk / unsupported claims
- The claim that the SALR-OPP model "mirrors the behavior of stress granules" is not supported by quantitative evidence or direct comparison with experimental data.
- The claim that the binary SALR mixture "shows that internal phase segregation, as seen in TDP-43 droplets, can arise purely from asymmetric interaction ranges" is based on qualitative visual similarity and lacks quantitative comparison.
- The claim of "stealthy hyperuniform" behavior for the SALR-Gauss system is not rigorously established.
- The general design principles stated in the Discussion and Conclusions are presented as universal but are only demonstrated for a limited set of parameters and conditions.
- The relevance of the two-dimensional results to three-dimensional biological systems is asserted but not critically examined.