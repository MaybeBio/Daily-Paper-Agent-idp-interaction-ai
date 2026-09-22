## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) as provided
- **Assessment boundary** Scientific content, methodological soundness, claims versus evidence, and alignment with Nature-style criteria. No line numbers were provided; references to figures and tables are based on the manuscript text.
- **Shared manuscript claim summary** The authors use a minimalist coarse-grained model to show that heterotypic protein–DNA interactions, DNA length, and DNA flexibility jointly control the phase behavior, internal multiphasic organization, and differential protein dynamics within protein–DNA biomolecular condensates. They report up to five distinct protein diffusion modes in condensates with strong heterotypic interactions.
- **Visible evidence base** Simulation results described in the text, including phase diagrams, radius of gyration measurements, radial density profiles, and displacement distribution analyses. Figures are referenced but not directly viewable in the provided material. Supporting Information is referenced for several analyses.
- **Missing materials affecting confidence** Figures and tables are not included in the provided text. Supporting Information (Figures S1–S14) is referenced but not available. Simulation parameter details, convergence criteria, and fitting procedures are only partially described. The exact definitions of "bridging contacts" and the cluster detection algorithm are not fully specified.

## Reviewer
- **Overall assessment** This manuscript presents a systematic computational study of how heterotypic protein–DNA interactions and DNA physical properties shape the organization and dynamics of biomolecular condensates. The work addresses a timely and important question, and the use of a minimalist coarse-grained model is appropriate for exploring a broad parameter space. The identification of multiphasic condensate architectures and up to five distinct protein diffusion modes is potentially interesting. However, the manuscript has several significant weaknesses. The evidence for the five diffusion modes is based on a fitting procedure whose robustness is not fully established. The interpretation of the diffusion modes is speculative and not directly validated against known experimental observables. The phase diagram analysis for the nonconverging regime is not fully explained, and the relationship between the reported "phase-in-phase" organization and experimentally observed multiphasic condensates is asserted rather than demonstrated. The model's simplifications, while acknowledged, limit the direct biological relevance of the findings. Overall, the core claims are plausible but not fully established from the provided evidence.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, chromatin organization, and genome regulation would be interested. The work provides a mechanistic framework for interpreting heterogeneous protein dynamics in chromatin-associated condensates, which is relevant to experimentalists using FRAP and single-molecule tracking. Computational biophysicists developing coarse-grained models of condensates would also find the methodology and parameter scans useful.

- **Major strengths** The study addresses a significant gap in understanding how DNA modulates condensate structure and dynamics. The systematic parameter scans across interaction strengths, DNA lengths, and flexibilities are thorough. The use of a minimalist model allows for broad exploration of parameter space. The identification of distinct protein populations with different diffusion modes is a novel contribution. The authors connect their findings to experimental observations of HP1α and FUS systems, which helps contextualize the results.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "we identified up to five distinct diffusion modes" in the multiphasic condensate, and that these modes correspond to proteins that are "strongly bound to DNA," "bound on the DNA surface," "diffusing within the condensed phase but not in contact with DNA," "at the interface," and "in the dilute phase."
- **Evidence pointer** Results section "Differential Protein Dynamics within the Protein–DNA Condensate"; Figures A–C; Figures S11–S14
- **Concern** The identification of five diffusion modes relies entirely on fitting the displacement distribution to a sum of Gaussian components. The manuscript does not provide sufficient detail on the fitting procedure, such as the initial guesses, the optimization algorithm, the criteria for determining the optimal number of components, or the statistical significance of adding a fifth component. The claim that "any fewer Gaussian components failed to capture the peaks and troughs" is qualitative and not supported by quantitative metrics. The assignment of each diffusion mode to a specific physical population (e.g., DNA-bound vs. interface) is speculative and not directly verified by any independent analysis, such as computing the diffusion coefficient separately for proteins in different spatial regions. The robustness of the five-mode decomposition to the choice of fitting range, time window, and bin size is only partially addressed (Figure S14). Without a more rigorous and transparent fitting analysis, the claim of five distinct diffusion modes is not established.
- **Why it matters** The differential dynamics claim is a central result of the manuscript and is used to argue for spatially heterogeneous protein mobility in condensates. If the five-mode decomposition is an artifact of overfitting or the assignment of modes to physical populations is incorrect, the main conclusion is weakened.
- **Resolution test** Provide a detailed description of the fitting procedure, including the algorithm, initial conditions, and convergence criteria. Show quantitative model selection metrics (e.g., AIC, BIC, or chi-squared per degree of freedom) for n = 1 through n = 6 components. Validate the assignment of diffusion modes to physical populations by computing diffusion coefficients separately for proteins in different spatial regions (e.g., within a certain distance of DNA vs. far from DNA) and comparing these to the fitted modes. Demonstrate that the five-mode result is robust to changes in the fitting range, time window, and bin size.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "when the protein–DNA interaction is strong (λPD = 2.0), we observe a striking difference: the phase envelope does not converge," and they interpret this as evidence for a fundamentally different condensate nature under strong heterotypic interactions.
- **Evidence pointer** Results section "Multiphasic Nature of Protein–DNA Condensates at Higher Heterotypic Interaction Strengths"; Figure A; Figure S6
- **Concern** The nonconverging phase envelope is a key observation, but the manuscript does not provide a clear explanation for why the phase envelope does not converge. The authors do not discuss whether this is a finite-size effect, a kinetic trapping artifact, or a genuine thermodynamic signature of multiphasic behavior. The coexistence concentrations are computed from the largest cluster, but the criteria for identifying the largest cluster and the sensitivity of the phase envelope to the cluster definition are not discussed. The authors also do not show whether the nonconvergence persists at longer simulation times or with different system sizes. Without a more thorough analysis, the interpretation of the nonconverging phase envelope as evidence for multiphasic organization is not fully supported.
- **Why it matters** The multiphasic organization claim is a central finding. If the nonconvergence is an artifact of the simulation protocol or analysis method, the claim of phase-in-phase organization is not established.
- **Resolution test** Show that the nonconvergence is robust to simulation length, system size, and cluster definition. Provide a thermodynamic or kinetic explanation for the nonconvergence, such as the presence of two distinct dense phases with different compositions. Compare the phase envelope to that of a control system with purely repulsive DNA–DNA interactions to rule out artifacts. If possible, compute the free energy or chemical potential of the components to demonstrate that the nonconvergence reflects a genuine multiphasic equilibrium.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that "DNA is not merely a passive scaffold but an active modulator of condensate architecture and dynamics."
- **Evidence pointer** Conclusions section; Results sections on DNA length and flexibility
- **Concern** While the simulations show that DNA length and flexibility affect condensate properties, the biological relevance of these findings is not clearly established. The model uses a minimalist representation of proteins as single beads, which lacks sequence specificity and multivalency. The authors acknowledge this limitation but do not discuss how their findings might translate to real protein–DNA systems with specific DNA-binding domains and post-translational modifications. The connection to experimental systems is made through qualitative comparisons (e.g., HP1α, FUS), but no quantitative predictions are made that could be tested experimentally. The claim that DNA is an "active modulator" is supported by the simulations but the broader significance for understanding genome organization and gene expression is not developed.
- **Why it matters** The manuscript aims to provide "mechanistic insight into principles underlying nuclear organization." If the model is too simplified to capture the relevant biology, the significance of the findings for understanding real biological systems is limited.
- **Resolution test** Discuss how the model parameters map to specific experimental systems and provide quantitative predictions that could be tested, such as the dependence of protein diffusion coefficients on DNA length or flexibility. Compare the simulation results to experimental measurements of protein dynamics in condensates, if available. Discuss how the model could be extended to include sequence-specific interactions and multivalency.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "DNA recruitment into the condensate significantly alters protein mobility, giving rise to differential dynamics of proteins within the condensate."
- **Evidence pointer** Results section "Differential Protein Dynamics within the Protein–DNA Condensate"; Figures A–C
- **Concern** The comparison between the dynamics of proteins in condensates with and without DNA is not shown directly. The authors compare the number of diffusion modes in a system with weak heterotypic interactions (λPD = 0.3, three modes) to a system with strong heterotypic interactions (λPD = 2.0, five modes). However, the two systems differ not only in the presence of DNA in the condensate but also in the strength of protein–DNA interactions. It is not clear whether the additional two diffusion modes are due to DNA recruitment or simply to the stronger protein–DNA interactions. A more direct comparison would be to analyze the dynamics of proteins in a condensate with strong heterotypic interactions but with DNA that is not recruited (e.g., by using a very long DNA that cannot enter the condensate) or to compare systems with the same λPD but different DNA lengths.
- **Why it matters** The claim that DNA recruitment alters protein dynamics is a key finding. If the additional diffusion modes are due to stronger protein–DNA interactions rather than DNA recruitment per se, the interpretation is different.
- **Resolution test** Perform control simulations where DNA is present but not recruited into the condensate (e.g., by using a very long DNA or by making DNA–DNA interactions repulsive) and compare the number of diffusion modes. Alternatively, analyze the dynamics of proteins in the dense phase only, separating proteins that are in contact with DNA from those that are not, and compute their respective diffusion coefficients.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "DNA length and flexibility critically modulate the phase separation and the internal organization of condensates."
- **Evidence pointer** Results sections "Role of DNA Length" and "Role of DNA Flexibility"; Figures A–B; Figures S4–S5
- **Concern** The results for DNA length and flexibility are presented as normalized radius of gyration and bound protein fractions, but the manuscript does not provide a clear physical explanation for the observed trends. For example, the peak in the radius of gyration ratio at 100 bp for λPP = 3.0 and 4.0 is described as "intriguing" but not explained. The authors do not discuss whether this peak is due to a change in the condensate morphology, a competition between protein–protein and protein–DNA interactions, or a finite-size effect. Similarly, the effect of DNA flexibility on protein binding is described but not mechanistically interpreted. The lack of a clear physical picture for these observations weakens the impact of the findings.
- **Why it matters** The manuscript aims to provide a mechanistic understanding of how DNA physical properties modulate condensate properties. Without a clear physical explanation for the observed trends, the findings are descriptive rather than mechanistic.
- **Resolution test** Provide a physical interpretation of the observed trends, supported by additional analyses such as radial distribution functions, contact maps, or free energy calculations. Discuss how the competition between protein–protein and protein–DNA interactions leads to the observed nonmonotonic behavior. If possible, compare the simulation results to theoretical predictions or scaling arguments.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section, protein model
- **Evidence pointer** Methods section "Protein Model"
- **Issue** The choice of protein bead diameter (σP = 50 Å) is justified by the radius of gyration of DNA-binding proteins, but the mass is set to 5000 g/mol, which is much lower than the mass of a typical protein of that size. The authors state that this is for computational efficiency, but the effect of this reduced mass on the dynamics is not discussed.
- **Required correction** Discuss the potential effect of the reduced mass on the diffusion coefficients and the timescales of the simulations. If the reduced mass affects the dynamics, the quantitative values of the diffusion coefficients may not be directly comparable to experimental measurements.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section, phase behavior
- **Evidence pointer** Results section "Phase Behavior of Protein–DNA Condensates as a Function of Homotypic and Heterotypic Interactions"; Figure A–B
- **Issue** The phase diagrams are presented as protein fraction and DNA fraction within the largest cluster, but the criteria for defining the "largest cluster" are not fully described. The distance cutoff of 1.5 σPD is mentioned, but it is not clear how this cutoff was chosen or how sensitive the results are to this choice.
- **Required correction** Provide a sensitivity analysis for the cluster detection cutoff. Discuss how the phase diagrams change with different distance criteria.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section, multiphasic organization
- **Evidence pointer** Results section "Multiphasic Nature of Protein–DNA Condensates at Higher Heterotypic Interaction Strengths"; Figure B–C
- **Issue** The radial density profile is fitted to a double hyperbolic tangent function, but the fitting parameters and their uncertainties are not reported. The authors do not show how the fit quality varies across different conditions.
- **Required correction** Report the fitting parameters and their uncertainties. Show the fit quality for representative conditions, including the residuals.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section, differential dynamics
- **Evidence pointer** Results section "Differential Protein Dynamics within the Protein–DNA Condensate"; Figure C
- **Issue** The authors state that the diffusion coefficients remained constant across lag times, but the range of lag times used is not specified. It is not clear whether the diffusion coefficients are truly constant or whether they vary at short or long lag times.
- **Required correction** Specify the range of lag times used for the analysis. Show the diffusion coefficients as a function of lag time for each mode.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Conclusions section
- **Evidence pointer** Conclusions section
- **Issue** The conclusions section states that the model "can be readily adapted to protein–RNA systems," but this claim is not supported by any specific discussion of how the model parameters would need to be changed.
- **Required correction** Provide a brief discussion of how the model could be adapted to protein–RNA systems, including which parameters would need to be reparameterized.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods section, simulation protocol
- **Evidence pointer** Methods section "Simulation Protocol"
- **Issue** The manuscript does not report the number of independent simulations performed for each condition, nor the statistical uncertainties in the reported quantities (e.g., protein fraction, DNA fraction, radius of gyration).
- **Required correction** Report the number of independent simulations and the statistical uncertainties for all reported quantities.

## Risk / unsupported claims
- The claim of "up to five distinct diffusion modes" is not fully supported due to the lack of a rigorous and transparent fitting analysis.
- The interpretation of the five diffusion modes as corresponding to specific physical populations (e.g., DNA-bound, interface, dilute) is speculative and not directly validated.
- The nonconverging phase envelope at strong heterotypic interactions is not fully explained and could be an artifact of the simulation protocol or analysis method.
- The claim that "DNA is not merely a passive scaffold but an active modulator" is supported by the simulations but the biological significance is not developed.
- The claim that the model "can be readily adapted to protein–RNA systems" is not supported by any specific discussion.
- The quantitative values of the diffusion coefficients may not be directly comparable to experimental measurements due to the reduced protein mass used in the simulations.
- The statistical uncertainties for the reported quantities are not provided, making it difficult to assess the robustness of the findings.