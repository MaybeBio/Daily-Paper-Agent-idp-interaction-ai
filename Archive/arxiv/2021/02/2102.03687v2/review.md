## Review setup
- **Input scope** Full manuscript text (main text, equations, figure captions, and references as provided).
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support for claims based solely on the provided manuscript text. No external literature or unpublished data were consulted.
- **Shared manuscript claim summary** The authors present a simplified explicit-solvent model of polyampholyte phase behavior, using explicit dipoles to represent a polar solvent. They compare simulated phase diagrams with implicit-solvent models using a uniform dielectric constant, finding only minor to moderate differences in phase separation propensity. They develop RPA and FTS analytical theories to rationalize these observations, attributing the small net effect to a compensation between enhanced dipole-dipole interactions in the condensed phase and enhanced polymer-solvent interactions in the dilute phase. They also compute the effective dielectric constant inside condensates, finding it can be high and sequence-dependent, with implications for client molecules.
- **Visible evidence base** Simulation results (MD and FTS) presented in Figures 4-6, 13, and 14; RPA analytical results in Figures 7-12; Table 1 with critical temperatures; equations 1-72.
- **Missing materials affecting confidence** Simulation parameter details (e.g., exact values for all interaction strengths, integration time steps, system size effects) are partially described but not fully tabulated. Details of the FTS numerical implementation (e.g., convergence criteria, lattice size effects) are not fully provided. The manuscript does not include a detailed comparison of the model's predictions with experimental data on specific IDP systems.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question in the field of biomolecular condensates: the role of spatially varying dielectric environments in modulating liquid-liquid phase separation. The authors employ a combination of explicit-solvent coarse-grained simulations and analytical theory to argue that the net effect of dielectric heterogeneity on phase separation propensity is relatively minor, due to a compensation of opposing interactions. The work is conceptually interesting and the theoretical development is a valuable contribution. However, the manuscript has several significant weaknesses that need to be addressed before the central claims are fully established. The connection between the simplified model and real biomolecular systems is not sufficiently developed, and the quantitative robustness of the key conclusions to model parameters and system size is not adequately demonstrated. The presentation is dense and at times difficult to follow, which may limit its accessibility to the broad readership of a general journal.
- **Who would be interested in the results, and why** Researchers in the fields of biophysics, physical chemistry, and soft matter physics, particularly those studying phase separation, intrinsically disordered proteins, and biomolecular condensates. The theoretical framework (RPA and FTS with explicit dipoles) will be of interest to theorists and computational scientists working on polymer solutions and polyelectrolyte complexes. The findings on the minor net effect of dielectric heterogeneity and the high internal dielectric constant of condensates are relevant to experimentalists interpreting the physical forces driving condensate formation and the behavior of client molecules.
- **Major strengths**
    1.  The study tackles a significant and debated question regarding the role of dielectric effects in biomolecular condensates.
    2.  The combination of explicit-solvent simulations and analytical theory (RPA, FTS) is a powerful and complementary approach.
    3.  The theoretical analysis provides a clear mechanistic explanation (compensation of dipole-dipole and polymer-solvent interactions) for the observed minor net effect.
    4.  The work goes beyond just phase diagrams to consider the internal dielectric environment of the condensate, which has implications for client molecule behavior.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The claim that the explicit-solvent model predicts only minor to moderate differences in phase behavior compared to implicit-solvent models with a uniform dielectric constant.
    - **Evidence pointer** Figures 6, 11, 12; Table 1.
    - **Concern** The comparison between explicit and implicit solvent models is confounded by the presence of attractive Lennard-Jones (LJ) interactions in the explicit-solvent model (U_LJ,pp) that are not present in the implicit-solvent models. The authors acknowledge this for the RPA comparison but the MD comparison in Figure 6 also includes this difference. The observed differences in phase behavior could be significantly influenced by this difference in the non-electrostatic interaction potential, rather than solely by the treatment of the solvent dielectric. The authors need to isolate the effect of the dielectric treatment by, for example, comparing explicit-solvent models with and without the attractive LJ term, or by adding an equivalent attractive term to the implicit-solvent model.
    - **Why it matters** The central conclusion of the paper is that dielectric heterogeneity has a minor effect. If this conclusion is confounded by differences in the non-electrostatic interaction model, the primary message of the paper is not supported by the presented evidence.
    - **Resolution test** The authors should perform additional simulations or analyses that directly control for the non-electrostatic interactions. For example, they could compare the phase diagram of model (ii) with a model where the polymer-polymer LJ attraction is turned off, or they could add a short-range attraction to the implicit-solvent model to match the explicit-solvent model's U_LJ,pp. The comparison should be made on a like-for-like basis to isolate the dielectric effect.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Scientific importance
    - **Claim pointer** The claim that the findings have "ramifications for dielectric effects in biomolecular condensates" and that the model provides insight into the internal dielectric environment experienced by client molecules.
    - **Evidence pointer** Figure 14; Discussion section.
    - **Concern** The model uses a very low effective dielectric constant (epsilon_r ≈ 4) for the condensed phase, which is far from the value for water (≈80). While the authors justify this choice for computational tractability, it is unclear how the conclusions would change for more realistic dielectric contrasts. More critically, the calculation of the overall droplet dielectric constant (Figure 14) includes contributions from the highly charged polyampholyte chains themselves, which are not representative of typical, less-charged IDPs. The relevance of these findings to real biomolecular condensates, which are composed of complex mixtures of proteins and nucleic acids with varying charge densities, is not established. The authors need to more carefully discuss the limitations of their model in representing real systems and temper their claims about biological ramifications.
    - **Why it matters** The paper's significance for a broad audience hinges on its relevance to real biological systems. If the model parameters are too far from realistic values, the conclusions may be of limited interest to the broader community studying biomolecular condensates.
    - **Resolution test** The authors should either (a) perform simulations with higher dielectric constants or more realistic model parameters to test the robustness of their conclusions, or (b) significantly revise the discussion to more clearly articulate the limitations of the model and avoid overgeneralizing the findings to real biological systems. A more detailed analysis of how the internal dielectric constant depends on the charge density and sequence of the polyampholyte would also strengthen the paper.
    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical soundness
    - **Claim pointer** The claim that the RPA and FTS results are in agreement with the MD simulations, supporting the robustness of the findings.
    - **Evidence pointer** Figures 7-12.
    - **Concern** The RPA and FTS models are for a compressible system with a specific form of the excluded volume interaction, while the MD simulations use a different, incompressible model. The comparison between these different models is not straightforward. The authors note that the RPA and FTS models do not include the attractive LJ interactions present in the MD model, which is a major difference. The agreement between the models is only qualitative, and the differences in the models make it difficult to assess the significance of the agreement. The authors should more clearly delineate the differences between the models and discuss the extent to which the agreement is meaningful.
    - **Why it matters** The paper claims that the combination of MD, RPA, and FTS provides a robust and consistent picture. If the models are too different, the agreement may be coincidental and the conclusions may not be as robust as claimed.
    - **Resolution test** The authors should provide a more detailed comparison of the models, including a discussion of the parameter mapping between them. They could also perform RPA or FTS calculations for a model that more closely mimics the MD model (e.g., by including an attractive polymer-polymer interaction) to see if the qualitative conclusions hold.
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability for nonspecialists
    - **Affected element** Introduction and Discussion
    - **Evidence pointer** Introduction, Discussion
    - **Issue** The manuscript is dense and assumes a high level of familiarity with polymer physics and field-theoretic methods. The introduction could do more to explain the biological context and the specific questions being addressed for a broader audience. The discussion of the "self-energy" term and its implications is particularly technical and may be difficult for non-specialists to follow.
    - **Required correction** The authors should consider adding a brief, non-technical summary of the key findings and their implications at the beginning or end of the paper. The discussion of the self-energy term could be simplified or moved to a more appropriate section.
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Methods, Figure 14
    - **Evidence pointer** Figure 14
    - **Issue** The calculation of the local dielectric constant using Equation 16 relies on the total dipole moment of the system, which includes contributions from both the solvent and the polyampholytes. The authors should clarify how the "local" dipole moment density is defined and how the boundary effects at the droplet interface are handled. The convergence of this calculation with respect to the slab thickness (10a) should also be discussed.
    - **Required correction** The authors should provide more details on the calculation of the local dielectric constant, including the definition of the local dipole moment and the treatment of boundary effects. A brief discussion of the sensitivity of the results to the slab thickness would be helpful.
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Methods, Equation 15
    - **Evidence pointer** Equation 15
    - **Issue** The empirical formula for the dielectric constant (Equation 15) is used to tune the dipole charges to maintain a constant epsilon_r. The authors should provide more details on the fitting procedure and the range of validity of this formula.
    - **Required correction** The authors should briefly describe how the parameters C1 and C2 in Equation 15 were determined and discuss the accuracy of the fit over the range of parameters used in the simulations.
    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Scientific importance
    - **Affected element** Discussion
    - **Evidence pointer** Discussion
    - **Issue** The authors discuss the potential implications of their findings for client molecules but do not provide any quantitative analysis. A simple calculation or simulation showing how a client molecule's interaction with the condensate would be affected by the local dielectric environment would significantly strengthen this part of the paper.
    - **Required correction** The authors should consider adding a simple model calculation or simulation to illustrate the potential effects of the dielectric environment on client molecule partitioning or interactions.

## Risk / unsupported claims
- The claim that the explicit-solvent model's predictions are directly relevant to biomolecular condensates is not fully supported, given the use of a very low dielectric constant (epsilon_r ≈ 4) and highly charged model polyampholytes.
- The claim that the "self-energy" term is "physically unwarranted" is a strong statement that is based on the analysis of a specific model. The generality of this conclusion is not established.
- The quantitative agreement between the MD simulations and the RPA/FTS theories is not rigorously established, and the differences between the models are not fully accounted for.
- The calculation of the overall droplet dielectric constant (Figure 14) is based on a specific model and may not be generalizable to real condensates. The claim that the dielectric environment inside a condensate can be "complex" is supported, but the specific values and trends may be model-dependent.