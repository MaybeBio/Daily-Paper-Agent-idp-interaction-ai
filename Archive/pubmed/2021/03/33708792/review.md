## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, and supplementary figure references
- **Assessment boundary** Scientific validity of the computational findings, methodological soundness of the REST2 simulations, and the strength of the claims linking conformational changes to amyloid inhibition
- **Shared manuscript claim summary** The authors use REST2 enhanced sampling molecular dynamics simulations to show that human serum albumin (HSA) binds monomeric Aβ42 at multiple sites with a preference for domain III, reduces β-sheet abundance in the H14-E22 and A30-G33 regions, shortens β-strands, shifts the conformational ensemble toward more disordered states, and disrupts intrapeptide interactions critical for β-hairpin formation, thereby providing a mechanistic basis for HSA's amyloid inhibitory activity
- **Visible evidence base** Full methods section with simulation parameters, convergence analyses (Supplementary Figures S1, S2), secondary structure analyses (Figure 1), conformational clustering (Figures 2, 3), contact probability maps (Figure 4), binding propensity analyses (Figure 5), structural characterization of binding poses (Figure 6, Table 1, Supplementary Table S1), and comparison with prior experimental and computational literature
- **Missing materials affecting confidence** Supplementary figures and tables referenced in the text are not provided; raw simulation trajectories and analysis scripts are not available; force field parameter files and specific REST2 implementation details are not fully described; no experimental validation data are included

## Reviewer
- **Overall assessment** This manuscript presents a computationally intensive study of Aβ42-HSA interactions using REST2 enhanced sampling simulations. The work addresses an important question regarding the molecular mechanism of HSA-mediated amyloid inhibition. The methodological approach is appropriate and the simulations appear to be reasonably converged based on the reported metrics. However, several technical concerns regarding the interpretation of the REST2 results, the statistical robustness of the binding site analysis, and the strength of the claims linking specific conformational changes to amyloid inhibition need to be addressed. The study is potentially valuable but the current evidence does not fully establish the proposed mechanism.
- **Who would be interested in the results, and why** Researchers studying amyloid aggregation and its inhibition, computational biophysicists interested in enhanced sampling methods for IDP-protein interactions, and investigators working on Alzheimer's disease therapeutics targeting Aβ aggregation. The methodological demonstration of REST2 for IDP-globular protein complexes may also interest method developers.
- **Major strengths** The study addresses a biologically and clinically relevant question with an appropriate computational approach. The REST2 method is well-suited for sampling the conformational ensemble of an IDP in a large complex. The convergence analyses are thoughtful and include multiple metrics. The comparison with previous experimental data on HSA-Aβ interactions provides useful context. The discussion of promiscuous interactions in the context of IDP biology is insightful.
- **Major Concerns** The concerns below identify issues with the interpretation of the REST2 results, the statistical robustness of the binding site analysis, the strength of the mechanistic claims, and the generalizability of the findings.
- **Minor Comments** Several presentation and analysis details could be improved to strengthen the manuscript.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** Originality: The application of REST2 to an IDP-globular protein complex is a methodological contribution, but the overall conceptual framework of HSA inhibiting Aβ aggregation through conformational modulation is not entirely novel. Scientific importance: The question of how HSA inhibits Aβ aggregation is clinically relevant, but the study only addresses monomeric Aβ and does not directly connect to the aggregation process. Interdisciplinary readership: The work will primarily interest computational biophysicists and AD researchers, with limited broader appeal. Technical soundness: The simulations appear technically sound, but several analysis and interpretation issues need resolution. Readability for nonspecialists: The manuscript is generally well-written but assumes familiarity with enhanced sampling methods and IDP concepts.
- **Recommendation posture** Supportive if technical concerns are resolved

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of the REST2 interpretation
- **Claim pointer** The authors claim that the REST2 simulations provide a reliable representation of the Aβ42 conformational ensemble in the presence and absence of HSA, and that the last 200 ns of the unscaled replica represents a converged ensemble.
- **Evidence pointer** Methods section "Details of REST2 Protocol"; Results section "Convergence of Simulations"; Supplementary Figures S1, S2
- **Concern** The authors state that only data from the unscaled replica (300 K) are meaningful for analysis, yet they use the last 200 ns of this replica to compute all reported properties. The convergence analysis compares two 100 ns blocks within this 200 ns window, which is a relatively short time for an IDP. The authors do not report the autocorrelation times of key observables, the effective sample size, or the statistical uncertainty of the reported quantities. Additionally, the authors do not discuss how the REST2 scaling of only Aβ42 interactions affects the effective temperature experienced by the peptide in the complex, and whether the chosen temperature ladder (300-600 K) is sufficient to overcome the energy barriers relevant to Aβ42 conformational transitions. The claim that the simulations are converged is not fully supported by the evidence presented.
- **Why it matters** The central conclusions of the study depend on the reliability of the conformational ensembles extracted from the simulations. If the sampling is insufficient or the interpretation of the REST2 replica is incorrect, the reported changes in β-sheet propensity, conformational clustering, and contact patterns may not be statistically meaningful.
- **Resolution test** Provide quantitative convergence metrics, including autocorrelation times, effective sample sizes, and block-averaged uncertainties for key observables. Show that the results are stable over longer time windows or multiple independent simulations. Discuss the effective temperature experienced by Aβ42 in the complex and justify the adequacy of the temperature ladder.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical robustness of binding site analysis
- **Claim pointer** The authors claim that Aβ42 binds to five major sites on the HSA surface with a preference for domain III, and that the K28-M35 segment is the primary interaction site.
- **Evidence pointer** Results section "Charged and Polar Residues in the N-Terminal Region and the K28-M35 Segment are More Likely to Interact With HSA"; Figure 5; Supplementary Figure S4
- **Concern** The binding site analysis is based on clustering of Aβ42 positions from the last 200 ns of a single REST2 simulation. The authors do not report the populations of the five binding poses, the free energy differences between them, or the statistical uncertainties of the binding propensities. The mapping between conformational clusters (C1' to C6') and binding poses is described qualitatively, but the robustness of this mapping is not quantified. The authors also do not discuss whether the binding poses are kinetically stable or whether they represent transient encounters. The claim that domain III is the preferred binding site is based on a single trajectory and may not be statistically reliable.
- **Why it matters** The proposed mechanism of promiscuous interactions relies on the identification of multiple binding sites and the preference for domain III. If the binding site analysis is not statistically robust, the mechanistic conclusions are not well supported.
- **Resolution test** Report the populations and free energies of the five binding poses with uncertainties. Show that the binding site preferences are reproducible across independent simulations or over longer time scales. Quantify the kinetic stability of the binding poses.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Strength of the mechanistic claims
- **Claim pointer** The authors claim that HSA shifts the conformational ensemble of Aβ42 towards more disordered states and that this conformational change is the mechanism by which HSA inhibits amyloid aggregation.
- **Evidence pointer** Results sections "HSA Reduces the β-Sheet Abundance of the H14-E22 and A30-G33 Regions of Aβ42 and Prevents Formation of Long β-Strands" and "HSA Shifts the Conformational Ensemble of Aβ42 Towards Less β-Sheet-Rich States and Modifies the β-Sheet Associations"; Discussion section
- **Concern** The study only examines monomeric Aβ42 and does not directly study aggregation. The claim that the observed conformational changes explain amyloid inhibition is an extrapolation. The authors show that HSA reduces β-sheet propensity and disrupts specific intrapeptide interactions, but they do not demonstrate that these changes are sufficient to inhibit aggregation. The connection between the monomeric conformational ensemble and the aggregation process is not established. The authors also do not discuss alternative mechanisms, such as steric blocking of aggregation-prone surfaces or chaperone-like effects, which could contribute to HSA's inhibitory activity.
- **Why it matters** The title and discussion make strong claims about the implications for amyloid inhibition. If the link between the observed conformational changes and aggregation inhibition is not demonstrated, the claims are overstated.
- **Resolution test** Qualify the claims to reflect that the study addresses the monomeric state only. Discuss how the observed conformational changes might relate to aggregation, and acknowledge alternative mechanisms. If possible, perform additional simulations of Aβ42 oligomerization in the presence of HSA or discuss the limitations of the current approach.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability of the findings
- **Claim pointer** The authors claim that the promiscuous interaction mechanism may apply to other modulators of Aβ aggregation and is likely prevalent in amyloid regulation by endogenous proteins.
- **Evidence pointer** Discussion section
- **Concern** The study is based on a single force field (Amber99sb-ILDN), a single starting structure for Aβ42, and a single HSA crystal structure. The authors do not discuss the sensitivity of their results to these choices. The claim that the mechanism is generalizable to other modulators and proteins is speculative and not supported by the data presented. The authors also do not compare their results with other computational studies of Aβ-HSA interactions or with experimental data on the binding interface.
- **Why it matters** The broader implications of the study depend on the generalizability of the findings. If the results are force field dependent or specific to the particular simulation setup, the conclusions may not be widely applicable.
- **Resolution test** Discuss the limitations of the force field and structural choices. Compare the results with other computational and experimental studies. Qualify the claims about generalizability or provide additional simulations with different force fields or starting structures.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of the methods
- **Affected element** Methods section "Details of REST2 Protocol"
- **Evidence pointer** Methods section
- **Issue** The description of the REST2 implementation is brief. The authors state that they used the PLUMED plug-in for REST simulations but do not provide the specific parameters used for the scaling, the exchange attempt frequency, or the criteria for choosing the temperature ladder.
- **Required correction** Provide a more detailed description of the REST2 implementation, including the specific PLUMED commands or input parameters, the exchange attempt frequency, and the rationale for the chosen temperature range.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results sections reporting quantitative values
- **Evidence pointer** Figures 1, 4, 5
- **Issue** The manuscript reports average values for β-sheet propensities, contact probabilities, and binding propensities without error bars or confidence intervals. It is unclear whether the differences between the free and HSA-bound states are statistically significant.
- **Required correction** Report uncertainties for all quantitative results, such as standard errors or confidence intervals, and perform statistical tests to support claims of significant differences.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figures 2 and 3
- **Evidence pointer** Figures 2, 3
- **Issue** The representative conformations in Figures 2 and 3 are described in the text but the figures themselves are not provided in the manuscript text. The reader cannot assess the structural claims without seeing the figures.
- **Required correction** Ensure that all figures are included in the manuscript and that the structural features described in the text are clearly visible and labeled in the figures.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The discussion does not address the limitations of using a single simulation per system, the potential force field dependence of the results, or the fact that the simulations only probe the monomeric state.
- **Required correction** Add a paragraph discussing the limitations of the study and the potential impact of these limitations on the conclusions.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout the manuscript
- **Evidence pointer** Abstract, Results, Discussion
- **Issue** The term "promiscuous interactions" is used to describe the binding of Aβ42 to multiple sites on HSA. This term is appropriate but could be more precisely defined in the context of the study.
- **Required correction** Define what is meant by "promiscuous interactions" in the introduction or methods and clarify whether this refers to multiple binding sites, multiple conformations at a single site, or both.

## Risk / unsupported claims
- The claim that HSA "shifts the conformational ensemble towards more disordered states" is supported by the simulation data but the statistical significance of this shift is not established.
- The claim that the disruption of β-hairpin formation between Q15-V24 and N27-V36 is "critical for aggregation" is based on prior literature but the direct link to aggregation inhibition is not demonstrated in this study.
- The claim that the proposed mechanism "may apply to other modulators of Aβ aggregation" is speculative and not supported by the data.
- The claim that the REST2 method is "suitable for studying IDPs" is supported by the convergence analysis but the general applicability to other IDP-protein complexes is not established.
- The statement that "HSA could interfere with Aβ nucleation in several ways" is presented as a conclusion but the study only provides evidence for the monomeric interaction mechanism.