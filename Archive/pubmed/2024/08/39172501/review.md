## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, and conclusions
- **Assessment boundary** Scientific claims, methodological soundness, and interpretive validity as presented in the supplied text
- **Shared manuscript claim summary** The authors use Hamiltonian replica exchange molecular dynamics (HREMD) to study the conformational behavior of a PfAMA1 domain III epitope in free and antibody-bound states, proposing an extended conformational selection mechanism for antigen-antibody recognition
- **Visible evidence base** Abstract, full methods description, results and discussion sections with figure references (Figures 1-7), conclusions
- **Missing materials affecting confidence** Actual figures and numerical data are not provided; simulation convergence metrics, force field validation details, and quantitative error analysis are not fully described

## Reviewer
- **Overall assessment** The manuscript presents a computationally focused study of conformational selection in an antigen-antibody system of potential relevance to malaria vaccine development. The central claim, that the PfAMA1 epitope undergoes extended conformational selection upon antibody binding, is plausible and consistent with the qualitative descriptions provided. However, the evidence as presented is largely descriptive and lacks quantitative rigor in several areas. The absence of actual figures and numerical data limits the ability to fully assess the strength of the claims. The methodological approach using HREMD is appropriate for enhanced sampling, but the manuscript would benefit from more detailed convergence analysis and clearer presentation of quantitative results.

- **Who would be interested in the results, and why** Researchers in computational biophysics, protein-protein interaction mechanisms, immunology, and malaria vaccine development would find these results relevant. The study addresses fundamental questions about conformational selection versus induced fit in antibody-antigen recognition, which has broad implications for understanding molecular recognition and for structure-based vaccine design. The specific focus on PfAMA1, a malaria vaccine candidate, adds translational relevance.

- **Major strengths** The study addresses a mechanistically important question about conformational selection in a therapeutically relevant system. The use of HREMD is an appropriate enhanced sampling technique for exploring conformational ensembles. The analysis considers multiple structural descriptors (RMSD, RG, SASA, secondary structure distances) providing a multidimensional view of conformational behavior. The identification of specific hydrogen bonds contributing to complex stability offers testable predictions.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The claim that HREMD simulations "suggest an extended conformational selection mechanism" relies on the adequacy of sampling and convergence of the simulations
  - **Evidence pointer** Methods section, Results and Discussion section
  - **Concern** The manuscript does not provide sufficient evidence for simulation convergence. No replica exchange acceptance rates beyond the initial "∼30%" are reported, no time-evolution of key observables is shown, and no block averaging or other convergence metrics are described. Without demonstrated convergence, the conformational ensembles described may not be representative of the true equilibrium distributions, which would undermine the central mechanistic claim.
  - **Why it matters** The extended conformational selection mechanism is inferred from the comparison of conformational ensembles in free and bound states. If the simulations have not converged, the observed differences in conformational sampling could be artifacts of insufficient sampling rather than genuine biophysical differences.
  - **Resolution test** Provide convergence analysis including time series of RMSD and RG for each replica, block-averaged estimates of key observables with uncertainties, and demonstration that the conformational distributions are stable over the latter portion of the trajectories.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim** The claim that specific hydrogen bonds (Tyr(H33)-Asp493, His(L94)-Val510, Ser(L93)-Glu511, Tyr(H56)-Asp485, Tyr(H35)-Asp493) are "the most important interactions observed" and "remain stabilized throughout the trajectory"
  - **Evidence pointer** Results and Discussion section, Figure 7d
  - **Concern** The manuscript states these hydrogen bonds were "observed in greater proportions and remain stabilized throughout the trajectory" but provides no quantitative data on occupancy, distances, or interaction energies. The criteria for defining a hydrogen bond, the threshold for "stabilized," and the statistical significance of these interactions relative to other possible contacts are not specified. Without quantitative metrics, the relative importance of these specific interactions cannot be evaluated.
  - **Why it matters** These hydrogen bonds are presented as key mechanistic determinants of the extended conformational selection process. If the identification of these interactions is not rigorously supported, the mechanistic interpretation is weakened.
  - **Resolution test** Provide hydrogen bond occupancy percentages with standard errors, distance distributions for each interaction, and comparison with a null model or with all possible epitope-paratope contacts to demonstrate that these specific interactions are statistically enriched.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim** The study provides "insights into the antigen-antibody interactions and conformational changes associated with the development of antimalarial mechanisms"
  - **Evidence pointer** Introduction, Conclusions
  - **Concern** The translational relevance to antimalarial development is asserted but not developed. The manuscript does not discuss how the identified conformational selection mechanism or specific hydrogen bonds could inform vaccine design, therapeutic antibody engineering, or other practical applications. The connection between the molecular findings and potential antimalarial strategies remains vague.
  - **Why it matters** The broader significance of the work depends on its implications for malaria intervention. Without articulating these implications, the study risks being a purely biophysical characterization with limited applied relevance.
  - **Resolution test** Add a discussion section that explicitly connects the conformational selection findings to vaccine design strategies, antibody engineering principles, or other translational applications, with specific recommendations based on the results.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability
  - **Affected element** Methods section
  - **Evidence pointer** Methods section
  - **Issue** The description of the HREMD setup is incomplete. The manuscript states "a Hamiltonian scaling factor λ ranging from 0.6 to 1.0" was tested and then "λ ≅ 0.71 to 1.0, with steps of 0.029" was used, but does not specify which interactions were scaled (e.g., only nonbonded, only protein-protein, etc.) or how the scaling was applied in the PLUMED implementation.
  - **Required correction** Provide a complete description of the Hamiltonian perturbation scheme, including which energy terms are modified, how the scaling is applied, and the rationale for the chosen λ range.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Methods section
  - **Evidence pointer** Methods section
  - **Issue** The manuscript does not report the total simulation time per replica beyond "500 ns" and does not specify the number of replicas that exchanged successfully. The equilibration protocol is not described.
  - **Required correction** Specify the equilibration procedure, the total production time per replica, the number of replicas, and the exchange statistics (e.g., average acceptance probability, number of round trips).

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Results and Discussion section
  - **Evidence pointer** Results and Discussion section, Figure 2
  - **Issue** The claim that "60% of the residues can be aligned with structural deviations smaller than 0.1 nm" in the free state and "80%" in the bound state is presented without statistical uncertainty. It is unclear whether this difference is significant given the sample sizes.
  - **Required correction** Provide confidence intervals or statistical tests for these percentages, and specify how many independent trajectory segments were used for the analysis.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interdisciplinary readership
  - **Affected element** Introduction
  - **Evidence pointer** Introduction
  - **Issue** The introduction assumes familiarity with conformational selection terminology and its distinction from induced fit. For a broader readership, a more explicit definition and a brief explanation of why this distinction matters for antibody-antigen recognition would improve accessibility.
  - **Required correction** Add one or two sentences defining conformational selection and induced fit, and explain the significance of distinguishing between them in the context of immune recognition.

- **Technical failings that need to be addressed before the case is established** R1-M1 (simulation convergence not demonstrated), R1-M2 (hydrogen bond analysis lacks quantitative support)

## Risk / unsupported claims
- The claim of an "extended conformational selection mechanism" is not fully supported without demonstrated simulation convergence and quantitative comparison of free and bound state ensembles
- The identification of specific hydrogen bonds as "most important" is unsupported without occupancy data or statistical analysis
- The statement that the antibody "has a structure with few flexible regions" is presented without quantitative flexibility metrics
- The claim that "the interaction occurred with the most likely conformation of the molecules before the formation of the complex" is an inference that requires more direct evidence, such as comparison of pre-binding populations with bound-state populations
- The translational relevance to "development of antimalarial mechanisms" is asserted but not substantiated with specific implications or recommendations