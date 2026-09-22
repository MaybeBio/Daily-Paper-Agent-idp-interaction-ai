## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusion, methods) as provided.
- **Assessment boundary** Scientific content, methodology, internal consistency, and support for claims based solely on the supplied text. No external validation or replication was performed.
- **Shared manuscript claim summary** The authors propose that "largest positive like-charge regions" (lpLCRs), conserved sequence features in FG nucleoporins, regulate the conformation of FG Nups, their interactions with each other, and their transient interactions with cargo complexes, thereby contributing to NPC selectivity. They use coarse-grained molecular dynamics simulations and time-resolved force distribution analysis (TRFDA) to support this.
- **Visible evidence base** Simulation results presented as density maps, TRFDA heatmaps, time-averaged plots, correlation coefficients, and qualitative descriptions of trajectories. Figures and tables are referenced but not fully visible in the provided text.
- **Missing materials affecting confidence** Full figures, supplementary figures, tables, videos, and detailed simulation parameters (e.g., force field parameters, system size, equilibration protocols) are not available. This limits quantitative verification of the reported results.

## Reviewer
- **Overall assessment** The manuscript addresses a significant and timely question in NPC biology, namely the sequence determinants of FG Nup behavior and cargo selectivity. The use of a coarse-grained model combined with TRFDA is a reasonable approach given the size and disorder of the system. However, the central claims regarding the regulatory role of lpLCRs in cargo selectivity are only partially supported by the evidence presented. The results are largely descriptive, and the link between simulated conformational changes and the functional property of "selectivity" is not rigorously established. The manuscript would benefit from clearer quantitative metrics, a more systematic analysis of the mutant effects, and a more cautious interpretation of the functional implications.
- **Who would be interested in the results, and why** Researchers in nucleocytoplasmic transport, intrinsically disordered proteins, and computational biophysics. The work provides a sequence-based hypothesis for FG Nup behavior that could inform experimental designs and the engineering of synthetic nanopores.
- **Major strengths** The study addresses a fundamental and unresolved question. The use of a coarse-grained model is appropriate for the system scale. The systematic comparison of wild-type and mutant lpLCRs across multiple Nups is a useful approach. The application of TRFDA to disordered proteins is novel and could be of methodological interest.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4.
- **Assessment against Nature-style criteria**  
  - **Originality** Moderate. The concept of lpLCRs is introduced in prior work by the same group, and this manuscript extends that analysis. The application of TRFDA to this system is novel.  
  - **Scientific importance** Potentially high, as understanding NPC selectivity is a major goal. However, the current evidence does not yet establish a clear mechanistic link.  
  - **Interdisciplinary readership** The topic is of interest to cell biologists, biophysicists, and computational biologists. The writing is generally accessible, though some simulation details may be opaque to nonspecialists.  
  - **Technical soundness** The methodology is plausible, but the lack of detailed parameters and the qualitative nature of many analyses reduce confidence.  
  - **Readability for nonspecialists** The introduction and discussion are clear, but the results section is dense and would benefit from more explicit explanations of the methods and metrics used.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is interesting, but the evidence presented is not yet sufficient to fully support the claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** "Our results suggest that the number of charged residues in the lpLCR domain directly governs the average distance between Phe residues and the intensity of interaction between them."
- **Evidence pointer** Results section, Figures 2 and 3, Table 1, Supplemental Tables S1 and S2
- **Concern** The claim that the number of charged residues "directly governs" the Phe-Phe distance and interaction intensity is a strong causal statement. The evidence presented is based on comparisons between wild-type and two mutant conditions (negative and positive controls). However, the manuscript does not provide a systematic dose-response analysis (e.g., varying the number of charges incrementally) to support a "direct" relationship. The reported changes in density and TRFDA metrics are qualitative or presented as single values, and the statistical significance of these differences is not reported.
- **Why it matters** A "direct governance" claim implies a quantitative, monotonic relationship. Without a graded series of mutations or a clear statistical framework, the claim is overstated and could mislead future experimental designs.
- **Resolution test** Provide a series of mutants with varying numbers of charged residues in the lpLCR and show a monotonic relationship between charge number and Phe-Phe distance or interaction force. Alternatively, provide statistical analysis (e.g., confidence intervals, effect sizes) for the differences between the three conditions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** "Moreover, changing the number of charged residues in an lpLCR domain can interfere with ultrafast and transient interactions between FG Nups and the cargo complex."
- **Evidence pointer** Results section, Figure 4, Supplemental Figures S1-S3
- **Concern** The claim that lpLCR mutations "interfere with" cargo interactions is based on TRFDA boxplots and density maps. However, the manuscript does not provide a quantitative measure of interaction "interference," such as residence times, binding/unbinding rates, or interaction energies. The boxplots show distributions of punctual stress, but the biological relevance of these values to the "ultrafast and transient" nature of the interactions is not established. The claim is therefore not directly supported by the presented metrics.
- **Why it matters** The transient nature of FG Nup-cargo interactions is a key functional property. Without a direct measure of interaction kinetics or strength, the claim that mutations "interfere" with these interactions remains speculative.
- **Resolution test** Calculate and report interaction lifetimes, binding/unbinding rates, or potential of mean force between the cargo and FG Nups for each condition. Alternatively, clearly define how punctual stress relates to interaction kinetics and validate this relationship.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "This study is the first to apply TRFDA to disordered proteins."
- **Evidence pointer** Introduction, Materials and Methods
- **Concern** The novelty claim is not verifiable from the provided text. No literature search or comparison with prior TRFDA applications is presented. While this may be true, the claim is made without supporting evidence.
- **Why it matters** Novelty claims are important for establishing the contribution of the work. An unsubstantiated claim could be challenged by reviewers or readers familiar with the literature.
- **Resolution test** Provide a brief literature review demonstrating that TRFDA has not been applied to disordered proteins before, or soften the claim to "to our knowledge."

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "The results of the simulations are as follows." (and subsequent results)
- **Evidence pointer** Results section, all figures and tables
- **Concern** The manuscript does not report the statistical significance of the differences between wild-type and mutant conditions. For example, the 25% increase in density for Nsp1 negative control, the 100% increase for Nup42, and the 10-fold difference in punctual stress for Nup49 are presented as observations, but no error bars, confidence intervals, or p-values are provided. It is unclear if these differences are robust or within the noise of the simulation.
- **Why it matters** Without statistical analysis, it is impossible to assess the reliability of the reported effects. This is a fundamental requirement for quantitative simulation studies.
- **Resolution test** Provide statistical analysis of the key metrics (e.g., density, punctual stress, Phe-Phe distance) across multiple independent simulations or trajectory blocks. Report mean, standard deviation, and appropriate significance tests.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section, Nsp1 paragraph
- **Evidence pointer** Figure 2
- **Issue** The description of the density maps is qualitative ("occupies most of the space", "slightly decreases the movement"). This makes it difficult to compare across conditions.
- **Required correction** Provide quantitative measures of the density distribution, such as radial distribution functions or occupancy maps, to support the qualitative descriptions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Materials and Methods, Coarse-grained model
- **Evidence pointer** "A timestep of 0.02 ps was used in simulations."
- **Issue** The manuscript does not specify the total simulation time for the ring and whole-NPC simulations, nor the number of independent replicates. This is essential for assessing convergence and reproducibility.
- **Required correction** Report the total simulation time, equilibration time, and number of replicates for each simulation condition.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section, Nup42 paragraph
- **Evidence pointer** Supplemental Figure S1
- **Issue** The statement "the cargo’s movement is a little less uniform compared with the wild-type system" is vague. It is unclear what metric was used to assess uniformity.
- **Required correction** Define the metric used to assess movement uniformity (e.g., mean squared displacement, occupancy variance) and report the values.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion, Cargo interactions
- **Evidence pointer** "Our results suggest that removing charged residues in lpLCR causes the FG Nups to form highly aggregated conformations in which FG Nups are less likely to unbind and form new interactions, effectively reducing the plasticity (viscoelasticity) of the ultrafast interactions between the cargo complex and the FG Nups."
- **Issue** The term "plasticity (viscoelasticity)" is used without definition or connection to the simulation metrics. This is a conceptual leap that is not directly measured.
- **Required correction** Either define how plasticity/viscoelasticity is inferred from the simulation data or remove this interpretation and stick to the observed metrics.

## Risk / unsupported claims
- The claim that lpLCRs "regulate" cargo selectivity is not directly tested. The simulations show changes in FG Nup conformation and interaction metrics, but the link to the functional property of selectivity is inferred, not demonstrated.
- The claim that the effect of mutations on cargo interactions is "nonuniversal" is based on a small number of Nups (four categories, but only a few representatives analyzed in detail). This is insufficient to establish a general principle.
- The claim that the wild-type system with a cargo complex behaves differently from the system without a cargo (compared to prior work) is based on a qualitative comparison and is not rigorously quantified.
- The statement that "the number of charged residues in the lpLCR regulates the spacing between the Phe residues and influence the force distribution of Nups in this way" is a causal interpretation that is not directly tested. The correlation between Phe-Phe distance and force is shown, but causality is not established.