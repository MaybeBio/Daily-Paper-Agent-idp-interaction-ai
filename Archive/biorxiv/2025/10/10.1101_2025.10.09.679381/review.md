## Review setup

- **Input scope** Full manuscript text, including abstract, introduction, methods, results, discussion, conclusions, and supporting information descriptions. No figures, tables, or supplementary data files were provided for direct inspection.
- **Assessment boundary** The assessment is limited to the claims as stated in the text and the methodological descriptions provided. No independent verification of simulation trajectories, force field parameters, or analysis scripts was possible.
- **Shared manuscript claim summary** The authors claim that palmitoylation of PSD95 at Cys3 and Cys5 induces a conformational transition from a compact to an extended state in solution, reverses the membrane juxtaposition of PDZ1 and PDZ2 domains, and promotes stable dimerization and clustering on synaptic-like membranes, as revealed by multiscale molecular dynamics simulations.
- **Visible evidence base** Text descriptions of results from all-atom and coarse-grained MD simulations, including references to Figures 2-6, Tables 1-2, and supplementary figures S1-S6. Simulation trajectories and input files are stated to be available on Zenodo.
- **Missing materials affecting confidence** Figures, tables, supplementary information, and simulation trajectory data were not provided. Quantitative metrics (e.g., free energy estimates, contact lifetimes, statistical uncertainties) are not reported in the text. The Zenodo repository link was not accessible for verification.

## Reviewer

- **Overall assessment** The manuscript addresses a timely and important question regarding the molecular mechanism of PSD95 palmitoylation in synaptic organization. The multiscale simulation approach is appropriate and the central hypothesis is clearly stated. However, the evidence presented in the text is largely qualitative, with no quantitative analysis of simulation data, no convergence assessment, and no validation against experimental data. The claim that palmitoylation "flips" the bilayer juxtaposed domain is not rigorously supported by the described analyses. The manuscript requires substantial revision to establish the case.
- **Who would be interested in the results, and why** Researchers in synaptic biology, membrane protein biophysics, and computational biophysics would be interested. The study addresses a fundamental question about how a reversible lipid modification controls protein conformation and self-assembly at membranes, which is relevant to understanding synaptic plasticity and neuropsychiatric disorders.
- **Major strengths** The study tackles a biologically important problem with a multiscale simulation strategy. The hypothesis is mechanistically plausible and the authors have made an effort to connect simulation findings to experimental observations. The public availability of simulation data is commendable.
- **Major Concerns** The concerns are detailed below.
- **Minor Comments** The minor comments are detailed below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5.
- **Assessment against Nature-style criteria** Originality is moderate; the question is important but the approach is not novel. Scientific importance is high if the claims are correct, but the evidence is insufficient. Interdisciplinary readership is plausible, but the manuscript is not accessible to non-specialists due to missing methodological detail. Technical soundness cannot be fully assessed without data. Readability for nonspecialists is limited by jargon and lack of context.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript could become publishable after major revisions that provide quantitative evidence, validation, and clearer presentation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that palmitoylation induces a conformational transition from a compact to an extended state in solution, supported by radius of gyration and end-to-end distance analyses (Section 3.2, Figure 2).
- **Evidence pointer** Section 3.2, Figure 2
- **Concern** The text describes qualitative differences in Rg distributions and end-to-end distances but provides no quantitative values, statistical analysis, or convergence assessment. It is unclear how many independent simulations were performed, what the simulation lengths were, and whether the observed differences are statistically significant. Without these details, the claim of a distinct conformational state is not supported.
- **Why it matters** The central conclusion of the paper rests on the existence of distinct conformational states. If the differences are within thermal fluctuations or simulation artifacts, the entire mechanistic model is invalid.
- **Resolution test** Provide quantitative Rg and end-to-end distance distributions with standard errors, report the number of independent simulations and their lengths, and include a convergence analysis (e.g., block averaging or time evolution of Rg). Show that the differences are statistically significant.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that palmitoylation reverses the membrane juxtaposition of PDZ1 and PDZ2 domains, with PDZ1 anchored to the membrane and PDZ2 distal in the palmitoylated state (Section 3.3, Figure 3).
- **Evidence pointer** Section 3.3, Figure 3
- **Concern** The "flipping" behavior is described qualitatively. The text mentions "time-dependent membrane distance plots" but does not report the actual distances, the time scales of flipping events, or the free energy differences between states. The claim that PDZ1 is "anchored" to the membrane is not supported by quantitative data such as contact probabilities, residence times, or binding free energies.
- **Why it matters** The reversal of domain juxtaposition is a key mechanistic claim. Without quantitative evidence, it is impossible to assess whether the observed behavior is a robust feature or a rare event.
- **Resolution test** Provide time series of membrane distances for each domain, calculate contact probabilities and residence times, and estimate free energy differences between the two orientations. Show that the flipping is reversible and that the palmitoylated state is thermodynamically favored.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that lipid composition modulates PSD95-membrane interactions, with negatively charged lipids influencing domain orientation (Section 3.4, Figure 5).
- **Evidence pointer** Section 3.4, Figure 5
- **Concern** The text states that simulations with a POPC-only membrane showed similar stability for PDZ1 and PDZ2, but no quantitative data are provided. The claim that "charge interactions within synaptic membranes" contribute to the flipping behavior is speculative without a systematic analysis of lipid composition effects.
- **Why it matters** The role of lipid composition is presented as a key finding, but the evidence is insufficient to support the claim. The authors do not show how varying lipid composition changes the behavior.
- **Resolution test** Provide quantitative comparisons of domain-membrane distances, contact probabilities, and orientation distributions for different lipid compositions. Include a systematic variation of anionic lipid content and show a dose-dependent effect.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that palmitoylation promotes stable dimerization of PSD95 on the membrane, as shown by coarse-grained simulations (Section 3.5, Figure 6).
- **Evidence pointer** Section 3.5, Figure 6
- **Concern** The text describes a decrease in inter-protein distance and extensive contact maps for the palmitoylated system, but no quantitative analysis is provided. It is unclear how many simulations were performed, what the dimerization free energy is, and whether the dimer is stable on relevant time scales. The claim that unmodified PSD95 "fails to form a stable dimeric arrangement" is not supported by quantitative data.
- **Why it matters** The promotion of dimerization is a central claim of the paper. Without quantitative evidence, the conclusion is not established.
- **Resolution test** Provide time series of inter-protein distances for multiple independent simulations, calculate dimerization free energies or potentials of mean force, and show that the dimer is stable over the simulation time scale. Include a statistical analysis of dimer lifetimes.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The authors state that all input files and trajectories are available on Zenodo (Section 2, Data Availability).
- **Evidence pointer** Section 2, Section 6
- **Concern** The Zenodo link was not accessible for verification. The text does not describe the specific files, their organization, or the software versions used. Without access to the data, the reproducibility of the simulations cannot be assessed.
- **Why it matters** Reproducibility is a core requirement for computational studies. The authors must ensure that the data are accessible and that sufficient metadata are provided.
- **Resolution test** Verify that the Zenodo repository is publicly accessible and contains all necessary input files, topologies, and trajectories. Provide a detailed description of the file structure and software versions in the manuscript.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that palmitoylation "flips the bilayer juxtaposed domain" but this terminology is not defined in the abstract and may be confusing to readers.
- **Required correction** Define the term "bilayer juxtaposed domain" or rephrase to "reverses the membrane-proximal orientation of PDZ domains."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods
- **Evidence pointer** Section 2.1
- **Issue** The methods section does not specify the simulation lengths for the all-atom membrane-bound systems, the number of replicates, or the temperature and pressure coupling parameters.
- **Required correction** Provide full simulation parameters, including simulation time, number of replicates, and coupling schemes.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Accuracy
- **Affected element** Section 3.3
- **Evidence pointer** Section 3.3
- **Issue** The text states "This was quite an interesting and unexpected observation" which is informal and not appropriate for a scientific manuscript.
- **Required correction** Rephrase to a neutral statement, e.g., "This observation was unexpected given the domain architecture."

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 3.3
- **Evidence pointer** Section 3.3
- **Issue** The phrase "steric freedoma" appears to be a typographical error.
- **Required correction** Correct to "steric freedom."

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 3.5
- **Evidence pointer** Section 3.5
- **Issue** The text mentions "contact map generated at 5 µs" but does not specify the simulation length or whether this is the total simulation time.
- **Required correction** Specify the total simulation time and the time point at which the contact map was generated.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Accuracy
- **Affected element** Section 4
- **Evidence pointer** Section 4
- **Issue** The text contains a question mark in the sentence "which remains closer to the membrane when palmitoylated. ?" which appears to be a formatting error.
- **Required correction** Remove the stray question mark.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 3.1
- **Evidence pointer** Section 3.1
- **Issue** The text states that I-TASSER was selected over AlphaFold2 for the final model, but no quantitative comparison of model quality is provided.
- **Required correction** Provide a brief comparison of model quality metrics (e.g., RMSD to known structures, QMEAN scores) to justify the choice.

## Risk / unsupported claims

- The claim that palmitoylation induces a "significant" conformational change in solution is unsupported without quantitative analysis.
- The claim that palmitoylation "reverses" the domain juxtaposition is unsupported without free energy calculations.
- The claim that lipid composition "modulates" PSD95-membrane interactions is unsupported without systematic variation of lipid composition.
- The claim that palmitoylation "promotes" stable dimerization is unsupported without quantitative dimerization analysis.
- The claim that the findings "provide a mechanistic model" for PSD95 clustering is overstated given the qualitative nature of the evidence.
- The statement that the results "are not easily accessible through current experimental methods" is speculative and not substantiated.