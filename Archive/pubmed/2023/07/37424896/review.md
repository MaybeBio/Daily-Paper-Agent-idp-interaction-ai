## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, conclusions, materials and methods, and supplementary material descriptions.
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the provided text. No external data or supplementary figures were available for direct inspection.
- **Shared manuscript claim summary** The authors investigate the conformational behavior of polyzwitterionic chains (poly(sulfobetaine methacrylate)) in dilute aqueous solutions with and without added salt (KBr). They report that these chains adopt Gaussian coil conformations in salt-free conditions despite acquiring a weak net positive charge via protonation. Addition of KBr induces nonmonotonic changes in chain dimensions, with an initial increase (antipolyelectrolyte effect) followed by a decrease (polyelectrolyte effect), attributed to selective ion binding and electrostatic screening, respectively.
- **Visible evidence base** Text descriptions of DLS, SAXS, zeta-potential, TEM, and DFTB simulation results. Figures and tables are referenced but not directly visible.
- **Missing materials affecting confidence** Actual figures, tables, and supplementary data are not provided. Specific numerical values for radii, scattering profiles, and simulation outputs are not available for independent verification.

## Reviewer
- **Overall assessment** The manuscript addresses a fundamental question about polyzwitterion conformations in solution, a topic of relevance to both polymer physics and the analogy with intrinsically disordered proteins. The combination of scattering, hydrodynamic, and simulation techniques is appropriate and potentially powerful. However, the current presentation has several gaps in data reporting, methodological detail, and quantitative analysis that prevent full evaluation of the central claims. The nonmonotonic salt effect is an interesting observation, but the mechanistic interpretation requires stronger support.
- **Who would be interested in the results, and why** Researchers in polymer physics, physical chemistry of polyelectrolytes and polyzwitterions, and those studying intrinsically disordered proteins as biomimetic analogs. The work also has implications for applications involving polyzwitterionic materials in antifouling, drug delivery, and responsive coatings.
- **Major strengths** The study combines multiple complementary techniques (DLS, SAXS, zeta-potential, TEM, and simulations) to address a long-standing question. The comparison between polyzwitterions, polyelectrolytes, and parent polymers with identical backbone lengths is a well-designed control strategy. The observation of nonmonotonic salt effects is novel and potentially significant.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative data reporting), R1-M2 (simulation methodology and timescale), R1-M3 (zeta-potential interpretation), R1-M4 (TEM interpretation).
- **Assessment against Nature-style criteria** 
  - **Originality** The work addresses a question that has been hypothesized but not directly tested, providing new experimental evidence. The nonmonotonic salt effect is a novel observation.
  - **Scientific importance** The findings have implications for understanding polyzwitterion behavior and the analogy with intrinsically disordered proteins, which is a topic of broad interest.
  - **Interdisciplinary readership** The work bridges polymer science, physical chemistry, and biophysics, making it potentially accessible to a broad audience.
  - **Technical soundness** The combination of techniques is appropriate, but the current level of quantitative detail and methodological transparency is insufficient to fully assess technical rigor.
  - **Readability for nonspecialists** The manuscript is generally well-written and accessible, though some sections assume familiarity with scattering and simulation techniques.
- **Recommendation posture** Supportive if technical concerns are resolved. The core observations are interesting, but the current evidence base is insufficient to fully establish the mechanistic claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative data reporting
- **Claim pointer** The manuscript claims nonmonotonic changes in Rg and Rh with added salt, with an increase followed by a decrease.
- **Evidence pointer** Figure 5, described in text but not visible
- **Concern** The manuscript reports trends in Rg and Rh but does not provide specific numerical values, error bars, or statistical significance for these measurements. The magnitude of the observed changes and the salt concentrations at which maxima occur are not stated.
- **Why it matters** Without quantitative data, the reader cannot assess the robustness of the nonmonotonic effect or compare it with theoretical predictions. The claim of "antipolyelectrolyte" and "polyelectrolyte" effects requires quantitative support.
- **Resolution test** Provide a table or figure with numerical values for Rg and Rh at each salt concentration, including error estimates and the number of independent measurements.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Simulation methodology
- **Claim pointer** The manuscript claims that DFTB simulations reveal potassium binding to sulfonate groups and show conformational changes consistent with the antipolyelectrolyte effect.
- **Evidence pointer** Figure 6, described in text but not visible
- **Concern** The simulation methodology is described only briefly. The system size, simulation length (100 ps is very short for polymer conformational sampling), number of replicas, and equilibration protocol are not specified. The calculation of Rg and an "approximate hydrodynamic radius" from a 100 ps trajectory is questionable.
- **Why it matters** The simulation results are used to support the mechanistic interpretation. If the sampling is inadequate, the conclusions drawn from the simulations may not be reliable.
- **Resolution test** Provide details on system size, simulation length, equilibration, and sampling. Show convergence of Rg and Rh with simulation time. Ideally, extend simulations to longer timescales or use enhanced sampling methods.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Zeta-potential interpretation
- **Claim pointer** The manuscript claims that zeta-potential measurements confirm a weak net positive charge on polyzwitterions in salt-free conditions.
- **Evidence pointer** Table 2, described in text but not visible
- **Concern** The zeta-potential values are not reported numerically. The interpretation of a "weak" positive charge is qualitative. The relationship between zeta-potential and the actual net charge on the polymer chain is not straightforward and depends on the position of the shear plane.
- **Why it matters** The claim of net positive charge is central to the proposed mechanism. Without quantitative zeta-potential values and a discussion of their limitations, the interpretation is not fully supported.
- **Resolution test** Report zeta-potential values with standard deviations. Discuss the limitations of zeta-potential as a measure of net polymer charge and consider complementary methods such as electrophoretic mobility or charge titration.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** TEM interpretation
- **Claim pointer** The manuscript claims that TEM measurements show structural changes in polyzwitterions with added salt, with feature sizes increasing from 1.3±0.5 nm to 3.5±1.2 nm.
- **Evidence pointer** Figure 7, described in text but not visible
- **Concern** TEM imaging of polymer chains in solution is challenging due to drying artifacts and contrast limitations. The interpretation of "feature sizes" as representing polymer chain dimensions is not straightforward. The relationship between the observed features and the actual chain conformation in solution is unclear.
- **Why it matters** The TEM results are used to support the conformational changes inferred from scattering. If the TEM interpretation is ambiguous, it does not add strong support to the central claims.
- **Resolution test** Provide control experiments (e.g., imaging of parent polymer and polyelectrolyte) and discuss potential drying artifacts. Correlate TEM feature sizes with Rg values from SAXS to establish a consistent picture.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of nomenclature
- **Affected element** Polymer naming convention
- **Evidence pointer** Results section, first paragraph
- **Issue** The naming convention (e.g., PDMAEMA10k-zwitterion, PZ10K) is introduced but the relationship between the full name and shorthand is not explicitly stated in a single place.
- **Required correction** Provide a clear table or statement defining all abbreviations and their corresponding full names and molecular weights.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** DLS data analysis
- **Evidence pointer** Materials and methods, DLS section
- **Issue** The method for extracting decay rates from the intensity correlation function is described only briefly. The choice of single versus double exponential fits is mentioned but not justified in detail.
- **Required correction** Provide more detail on the fitting procedure, including the range of delay times used, the criteria for choosing the number of exponentials, and the uncertainty in the extracted decay rates.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data repository link
- **Evidence pointer** Data availability section
- **Issue** The data availability statement provides a Dropbox link, which is not a permanent or citable repository.
- **Required correction** Deposit the data in a permanent repository (e.g., Zenodo, Figshare) and provide a DOI.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Consistency of terminology
- **Affected element** Use of "antipolyelectrolyte" and "polyelectrolyte" effects
- **Evidence pointer** Throughout the manuscript
- **Issue** The terms are used to describe the nonmonotonic salt effect, but the transition between the two regimes is not clearly defined in terms of salt concentration.
- **Required correction** Define the salt concentration ranges for each effect and discuss the crossover behavior more explicitly.

## Risk / unsupported claims
- The claim that polyzwitterions in salt-free solutions behave as Gaussian coils in good solvent is supported by the Rg/Rh ratio, but the numerical values and error bars are not provided.
- The mechanistic interpretation of the antipolyelectrolyte effect via selective potassium binding is supported by simulations, but the simulation methodology is insufficiently detailed to assess reliability.
- The claim that the polyzwitterions acquire a net positive charge in salt-free conditions is supported by zeta-potential measurements, but the values are not reported and the interpretation is qualitative.
- The TEM results are used to support conformational changes, but the interpretation of feature sizes as polymer dimensions is not well-established.
- The statement that "the chains do not exhibit a polyelectrolyte peak in SAXS and two modes in DLS" is presented as evidence of weak charging, but the absence of a peak could also be due to low contrast or concentration effects.