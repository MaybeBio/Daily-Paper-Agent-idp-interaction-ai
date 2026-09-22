## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and figure legends as provided.
- **Assessment boundary** Scientific content, methodological rigor, interpretation of results, and alignment with claims. No assessment of editorial fit or publication decision.
- **Shared manuscript claim summary** The authors use all-atom molecular dynamics simulations of an 8-chain system of hnRNPA1 low-complexity domain (A1-LCD) at NaCl concentrations from 50 to 1000 mM to explain the atypical salt-promoted phase separation of this protein. They propose two direct salt effects, namely net charge neutralization and ion-mediated inter-chain bridging, and one indirect effect, namely strengthening of π-type interactions via water withdrawal. They further propose a classification of salt dependence of homotypic phase separation into four classes predictable from amino acid composition.
- **Visible evidence base** Simulation trajectories (four replicates of 1.5 μs per salt concentration), analyses of Dmax, radius of gyration, inter-/intrachain contacts, ion binding via radial distribution functions, bridging ion counts, and water density around π-interaction partners. Supplementary figures referenced but not fully provided.
- **Missing materials affecting confidence** Supplementary figure supplements (Figure 1—figure supplement 1, Figure 3—figure supplements 1 and 2, Figure 5—figure supplement 1) are referenced but not included in the provided text. Source data files and simulation input parameters (e.g., exact ion placement protocol, equilibration details) are not fully described. Experimental validation data (e.g., from Raman spectroscopy) are cited but not shown.

## Reviewer
- **Overall assessment** This manuscript presents a mechanistically detailed and potentially valuable simulation study of salt effects on A1-LCD phase separation. The identification of two direct and one indirect salt action is plausible and supported by the presented analyses. However, the central claim that these mechanisms explain the experimentally observed salt dependence, and the proposed predictive classification, rest on inferences from a small 8-chain system that may not adequately represent phase equilibria. The evidence for the indirect water-withdrawal mechanism is indirect and would benefit from stronger validation. The classification scheme, while heuristic, is only partially validated by literature data and requires more rigorous statistical support.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, intrinsically disordered proteins, and the molecular mechanisms of phase separation. The work is also relevant to those interested in ion-specific effects on protein interactions and the use of all-atom simulations to dissect driving forces in condensate formation. The proposed classification may be of interest to the broader community seeking predictive rules for salt dependence of phase separation.
- **Major strengths** The study addresses a significant and under-explored question, namely the mechanistic basis for atypical salt-promoted phase separation. The use of all-atom explicit-solvent simulations is appropriate and provides a level of detail inaccessible to coarse-grained approaches. The analyses are systematic, and the distinction between direct and indirect salt effects is conceptually clear. The authors connect their findings to a broader classification framework, which is a useful conceptual contribution.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (system size and representativeness), R1-M2 (equilibration and sampling), R1-M3 (indirect mechanism evidence), R1-M4 (classification validation).
- **Assessment against Nature-style criteria**  
  - **Originality** High. The mechanistic dissection of salt effects at atomic resolution, particularly the proposal of ion bridging and water withdrawal strengthening π-interactions, is novel.  
  - **Scientific importance** Moderate to high. The findings could inform understanding of salt-dependent phase behavior in many IDP systems, but the generality is not yet established.  
  - **Interdisciplinary readership** Moderate. The work will appeal to biophysicists, computational chemists, and cell biologists interested in condensates, but the technical nature may limit broader appeal.  
  - **Technical soundness** Generally sound in execution, but the limitations of the 8-chain model and the indirect evidence for the water-withdrawal mechanism temper confidence.  
  - **Readability for nonspecialists** The manuscript is clearly written, but the methods and some analyses assume familiarity with simulation techniques. The conceptual framework is accessible.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding system representativeness, equilibration, and validation of the indirect mechanism and classification scheme.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Experimental design and representativeness  
- **Claim pointer** The authors claim that the 8-chain system at an initial concentration of 3.5 mM models the dense phase and allows comparison between low salt (no phase separation) and high salt (phase separation).  
- **Evidence pointer** Results, Figure 1B, Methods (MD simulations)  
- **Concern** The 8-chain system is a very small model for a phase-separated system. The initial concentration of 3.5 mM is stated to be close to the critical concentration, but the system may not represent a true dense phase, especially at intermediate salt concentrations. The authors acknowledge that the number of chains is too low for proper representation of a homogeneous solution or full equilibration between phases, but this limitation directly affects the interpretation of the simulated condensation as phase separation.  
- **Why it matters** The central claim that the simulations explain salt-promoted phase separation depends on the assumption that the observed condensation in the 8-chain system is equivalent to phase separation. Finite-size effects and the absence of a dilute phase in equilibrium could lead to artifacts that are not representative of macroscopic phase behavior.  
- **Resolution test** The authors should demonstrate that the observed condensation is not a finite-size artifact, for example by showing that the results are robust to system size (e.g., simulations with more chains) or by comparing with a system where phase separation is known to be absent. Alternatively, they could temper their claims to be about condensation in a finite system rather than phase separation per se.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Sampling and equilibration  
- **Claim pointer** The authors claim that the systems maintain a loose configuration at 50 mM NaCl but condense at higher salt, and that the last 500 ns of each 1.5 μs trajectory was used for analysis.  
- **Evidence pointer** Methods (MD simulations), Results (Figure 1C, D; Figure 2)  
- **Concern** The simulation time of 1.5 μs may be insufficient for the 8-chain system to reach equilibrium, particularly at low salt where the chains are diffuse and may require longer times to explore configurational space. The use of only the last 500 ns for analysis assumes that the system has converged, but no convergence tests (e.g., block averaging, comparison of early vs. late trajectory segments) are presented. The RMSF analysis (Figure 1—figure supplement 1) suggests large-scale reconfiguration at low salt, which may indicate that the system is not well equilibrated.  
- **Why it matters** If the systems are not equilibrated, the reported differences between salt concentrations could reflect kinetic trapping rather than thermodynamic driving forces. This would undermine the mechanistic conclusions.  
- **Resolution test** The authors should provide evidence of convergence, such as time evolution of key observables (Dmax, Rg, contact numbers) and block-averaged uncertainties. If convergence is not achieved, longer simulations or enhanced sampling methods may be required.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence for indirect mechanism  
- **Claim pointer** The authors claim that high salt strengthens π-type interactions by drawing water away from the interaction partners, based on decreased water density around Tyr residues involved in π-interactions.  
- **Evidence pointer** Results (Figure 5D, E; Figure 5—figure supplement 1A–C)  
- **Concern** The evidence for the water-withdrawal mechanism is correlative. The authors show that water density around Tyr residues decreases with increasing salt, and that π-interaction counts increase, but they do not establish a causal link. Alternative explanations, such as direct ion-π interactions or changes in protein conformation, are not ruled out. The control (Figure 5—figure supplement 1D) shows no decrease around Asp in salt bridges, but this does not directly validate the mechanism for π-interactions.  
- **Why it matters** The indirect mechanism is a key novel claim of the paper. If the causal link is not established, the mechanistic model is incomplete and the classification scheme based on it is less credible.  
- **Resolution test** The authors could perform additional analyses, such as calculating water residence times, free energy calculations for π-interaction formation with and without salt, or simulations with modified water models. Alternatively, they could compare with a system where water withdrawal is not expected (e.g., a mutant with fewer π-interaction partners).

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Validation of classification scheme  
- **Claim pointer** The authors propose four classes of salt dependence of homotypic phase separation and claim these can be predicted from amino acid composition, with validation from literature data in Table 1.  
- **Evidence pointer** Discussion (Figure 6, Table 1)  
- **Concern** The classification scheme is heuristic and based on three determinants (charged residue count, net charge, aromatic residue count). The validation in Table 1 is qualitative and uses arbitrary thresholds (e.g., 8% aromatic content, 6% net charge, 20% charged content). The statistical significance of the classification accuracy is not assessed, and the number of proteins in each class is small. The scheme may not be robust to variations in sequence context or solution conditions.  
- **Why it matters** The predictive classification is a major conceptual contribution, but if it is not rigorously validated, it may be seen as speculative and could mislead future studies.  
- **Resolution test** The authors should provide a more quantitative validation, such as a statistical test of classification accuracy, and test the scheme on a larger set of proteins with known salt dependence. They should also discuss the limitations of the thresholds and the potential for exceptions.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity of methods  
- **Affected element** Methods (MD simulations)  
- **Evidence pointer** Methods (MD simulations)  
- **Issue** The method for placing ions to achieve the desired salt concentration is not fully described. It is stated that "appropriate number of water molecules were randomly selected and replaced with Cl– and Na+ ions," but the protocol for ensuring a homogeneous ion distribution and avoiding artifacts is not detailed.  
- **Required correction** Provide a more detailed description of the ion placement protocol, including any equilibration steps to ensure ion distribution is randomized and representative.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Statistical reporting  
- **Affected element** Results (Figures 2, 3, 4, 5)  
- **Evidence pointer** Results (Figures 2, 3, 4, 5)  
- **Issue** Error bars are described as standard deviations among four replicate simulations, but the number of independent samples (e.g., number of frames, number of chains) used for each observable is not always clear. For example, in Figure 3A, the ion counts per residue are averaged over residues, but the variability across residues is not shown.  
- **Required correction** Clarify the statistical treatment for each observable, including the number of independent samples and how error bars are computed.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Interpretation of Dmax  
- **Affected element** Results (Figure 2A)  
- **Evidence pointer** Results (Figure 2A)  
- **Issue** The Dmax calculation is described as the maximum side length of a rectangular box circumscribing the multi-chain system, with the smallest of 8 values (each centered on a different chain) reported. This is an unusual metric, and its interpretation as a measure of condensation is not immediately intuitive.  
- **Required correction** Provide a brief justification for why this metric is appropriate and how it relates to more standard measures of condensation (e.g., radius of gyration of the entire system, inter-chain contact density).

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Literature context  
- **Affected element** Introduction, Discussion  
- **Evidence pointer** Introduction, Discussion  
- **Issue** The authors cite experimental work on A1-LCD phase separation (Martin et al., 2021) but do not discuss potential discrepancies between simulation and experiment in detail, such as the exact salt concentration at which phase separation begins or the nature of the dense phase.  
- **Required correction** Add a brief discussion of how the simulation results compare quantitatively with experimental observations, and note any limitations in direct comparability.

## Risk / unsupported claims
- The claim that the 8-chain system at 3.5 mM initial concentration represents the dense phase and that condensation in the simulations is equivalent to phase separation is not fully supported, given the acknowledged limitations of system size and lack of a dilute phase.
- The claim that high salt strengthens π-type interactions by drawing water away from the interaction partners is not causally established; the evidence is correlative.
- The proposed four-class classification of salt dependence and its predictability from amino acid composition is not rigorously validated; the statistical basis is weak and thresholds are arbitrary.
- The statement that "the simulations do not show condensation at low salt, thus mimicking a homogeneous solution" is an inference that may not be valid given the small system size and potential finite-size effects.
- The relevance of the observed ion coordination to channels and transporters (Discussion) is speculative and not directly supported by the data presented.