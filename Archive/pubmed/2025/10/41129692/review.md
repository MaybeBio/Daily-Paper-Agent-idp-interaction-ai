## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Methodology, results, and conclusions as presented in the manuscript
- **Shared manuscript claim summary** The authors present a protocol integrating DRIDmetric and freenet Python packages with PATHSAMPLE and disconnectionDPS to analyze MD simulations of IDPs via energy landscapes, metastable states, and transition pathways. They demonstrate this workflow on Aβ42 in neat solution, with a GAG chain, and with POPC lipids, reporting environment-dependent shifts in conformational preferences and kinetics.
- **Visible evidence base** Abstract, Introduction, Theory and Methods, Practical Applications, Results, Discussion and Conclusion sections. Figures referenced but not provided. No supplementary material included.
- **Missing materials affecting confidence** Figures 1-4 (disconnectivity graphs and FPT distributions) are cited but not available. Simulation parameters for the previously published neat solution run are not fully detailed. No convergence analysis or error estimates are provided. The manuscript states "location not provided" for several key quantitative results.

## Reviewer
- **Overall assessment** The manuscript presents a potentially useful integration of existing computational tools for energy landscape analysis of IDP simulations. The methodological framework is clearly described and the application to Aβ42 in different environments yields interesting qualitative insights. However, the work is primarily a protocol demonstration rather than a new scientific discovery, and the absence of figures and quantitative validation metrics limits the ability to fully assess the robustness of the reported findings. The claims about environment-dependent reshaping of energy landscapes would be strengthened by convergence analysis and comparison with alternative analysis methods.
- **Who would be interested in the results, and why** Researchers in computational biophysics and molecular simulation, particularly those studying IDPs and amyloid aggregation. The protocol offers a practical workflow for extracting kinetic and thermodynamic information from MD trajectories, which is a common challenge in the field. The Aβ42 case study may also interest experimentalists studying Alzheimer's disease mechanisms who seek molecular-level interpretations of aggregation modulation by lipids and GAGs.
- **Major strengths** The manuscript addresses an important methodological gap by providing an integrated, modular workflow for energy landscape analysis of IDPs. The combination of DRID-based dimensionality reduction with kinetic network analysis tools is sensible and builds on established methods. The choice of Aβ42 as a case study is relevant given its biological importance. The protocol-style presentation with installation instructions and configuration examples enhances practical utility. The comparison across three environments (neat, GAG, POPC) demonstrates the versatility of the approach.
- **Major Concerns** The manuscript lacks quantitative validation of the kinetic model, including convergence assessment of the clustering and transition matrix estimates. The claim that results are "directly comparable" across systems despite "minor differences in simulation protocols" requires justification. The physical interpretation of the disconnectivity graph features, particularly the assignment of specific states to functional roles, is presented without sufficient structural characterization. The FPT analysis relies on the Markov assumption, which is not tested. The absence of figures prevents evaluation of the actual energy landscape topologies and FPT distribution shapes.
- **Minor Comments** The manuscript would benefit from a more explicit statement of what is genuinely new versus what is a re-analysis of previously published simulations. The choice of six specific Cα atoms as centroids is justified by reference to prior work, but a brief rationale would help readers applying the protocol to new systems. The Discussion section is somewhat general and could more directly address limitations of the approach, such as sensitivity to clustering parameters and force field dependence.
- **Technical failings that need to be addressed before the case is established** The manuscript does not provide evidence that the kinetic model is converged or that the reported free energy differences are statistically meaningful. The comparison across systems with different simulation protocols undermines the claim of direct comparability. The Markov state model assumption underlying the FPT analysis is not validated.
- **Assessment against Nature-style criteria** Originality: Moderate. The integration of existing tools is useful but not conceptually novel. Scientific importance: Moderate. The protocol addresses a practical need but does not reveal fundamentally new biophysical principles. Interdisciplinary readership: Limited. The manuscript is primarily of interest to computational biophysicists. Technical soundness: Not fully established from the provided material. The absence of convergence analysis and validation metrics is a significant gap. Readability for nonspecialists: Adequate. The manuscript is clearly written, though the methods section assumes familiarity with energy landscape theory.
- **Recommendation posture** Supportive if technical concerns are resolved. The protocol has clear utility, but the manuscript must demonstrate that the kinetic model is converged and that the reported differences across environments are statistically robust. The authors should also provide the missing figures and quantitative validation metrics.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the workflow provides "a robust and interpretable way to extract thermodynamic and kinetic insights from MD data" and that the three systems are "directly comparable."
- **Evidence pointer** Theory and Methods, Molecular Dynamics Simulations; Results sections
- **Concern** The manuscript does not provide any convergence analysis for the clustering or the transition matrix estimates. The number of states, the statistical uncertainty in free energy differences, and the sensitivity of results to the clustering cutoff are not reported. Furthermore, the claim of direct comparability across systems is undermined by the statement that "minor differences in simulation protocols" exist, without specifying what these differences are or demonstrating that they do not affect the results.
- **Why it matters** Without convergence assessment, the reported free energy differences and kinetic timescales cannot be considered reliable. The comparison across environments is central to the manuscript's conclusions, and if the simulation protocols differ, the observed differences could be artifacts of the protocols rather than genuine physical effects.
- **Resolution test** The authors should provide a detailed convergence analysis, including the number of states as a function of clustering cutoff, the statistical error in free energy estimates (e.g., via bootstrapping), and a demonstration that the transition matrix is Markovian. They should also specify the exact differences in simulation protocols and justify that these do not affect comparability.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The manuscript claims that in the presence of GAG, "Aβ42 preferentially adopts ordered β-hairpin conformations, with disordered states energetically disfavored," and that in the presence of POPC, the landscape is "notably flatter" with a β-sheet-rich global minimum.
- **Evidence pointer** Results, Free Energy Landscape sections; Figures 2 and 3 (not provided)
- **Concern** The key results are presented through figures that are not available in the provided material. The free energy differences are reported in units of kBT, but the absolute values and their uncertainties are not given in the text. The structural characterization of the states (e.g., the "β-hairpin" and "S-shaped" motifs) is described qualitatively without quantitative measures such as secondary structure content or contact maps.
- **Why it matters** The conclusions about environment-dependent reshaping of the energy landscape rest entirely on the visual interpretation of disconnectivity graphs and the assignment of structural motifs to states. Without the figures and quantitative structural data, the reader cannot verify these claims.
- **Resolution test** The authors should provide the figures and include quantitative structural characterization of the key states, such as average secondary structure propensities, radius of gyration, and contact probabilities. They should also report the free energy differences with associated uncertainties.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The manuscript states that "the resulting FPT distributions for the three systems under study are shown in Figure 4" and reports specific timescales such as τD→Bmon∼15ns and τB→DGAG∼2800ns.
- **Evidence pointer** Results, Time Scale Analysis section; Figure 4 (not provided)
- **Concern** The FPT analysis is presented as a key outcome, but the details of how the rate matrix was constructed and how the FPT distributions were computed are not fully described. The manuscript refers to PATHSAMPLE but does not explain the input parameters, the number of pathways considered, or the criteria for defining the reactant and product states. The reported timescales are given without error estimates.
- **Why it matters** For the protocol to be reproducible and the kinetic results to be credible, the analysis parameters must be specified. The absence of error estimates on the timescales prevents assessment of whether the reported differences between systems are significant.
- **Resolution test** The authors should provide a complete description of the FPT analysis parameters, including the rate matrix construction, the definition of reactant and product states, and the number of pathways sampled. They should also report the statistical uncertainty in the timescales.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Theory and Methods, Molecular Dynamics Simulations
- **Evidence pointer** "Despite minor differences in simulation protocols, all systems share the same force field, ion concentration, and temperature, so the results are directly comparable."
- **Issue** The phrase "minor differences in simulation protocols" is vague. The reader cannot assess whether these differences might affect the results.
- **Required correction** Specify the exact differences in simulation protocols (e.g., box size, equilibration time, simulation length) and provide a brief justification for why these do not affect comparability.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Practical Applications, Installation
- **Evidence pointer** "The required Python modules DRIDmetric and freenet can then be installed directly from their respective repositories using the following commands"
- **Issue** The installation commands are not shown in the provided text. The reader cannot follow the protocol without this information.
- **Required correction** Include the actual installation commands or provide a link to the repositories where they can be found.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results, Free Energy Landscape of Aβ42 in the Presence of POPC Lipids
- **Evidence pointer** "The comparable time scales between D → B and D → BPOPC suggest that state B may act as an intermediate in the transition pathway toward the global minimum."
- **Issue** This interpretation is speculative and not supported by direct pathway analysis. The similar timescales could also arise from independent parallel pathways.
- **Required correction** Either provide direct evidence for the intermediate role of state B (e.g., via transition path analysis) or soften the claim to acknowledge alternative interpretations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Language
- **Affected element** Discussion and Conclusion
- **Evidence pointer** "The case of Aβ42 illustrated that our energy landscape and kinetics analysis approach can uncover unprecedented details of its multifunneled energy landscape."
- **Issue** The term "unprecedented" is an overstatement. The manuscript does not compare its findings with previous energy landscape analyses of Aβ42 in sufficient detail to support this claim.
- **Required correction** Replace "unprecedented" with a more measured term such as "detailed" or "comprehensive," and provide a comparison with prior studies to contextualize the novelty.

## Risk / unsupported claims
- The claim that the workflow is "robust" is not supported by convergence analysis or validation against alternative methods.
- The claim of "direct comparability" across systems is not justified given the stated differences in simulation protocols.
- The specific timescales reported (e.g., τD→Bmon∼15ns) are presented without error estimates, making their reliability unassessable.
- The structural assignments of states (e.g., "β-hairpin," "S-shaped") are qualitative and not supported by quantitative structural metrics in the provided text.
- The interpretation that state B acts as an intermediate in the POPC system is speculative and not directly tested.