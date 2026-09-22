## Review setup
- **Input scope** Full manuscript text including main text, methods appendix, and supplementary figure descriptions
- **Assessment boundary** Scientific claims, methodology, and evidence presented in the provided text; no external validation performed
- **Shared manuscript claim summary** The authors propose that net charge asymmetry between biomolecular condensate constituents can control droplet size by suppressing coarsening, leading to stable coexistence of equal-sized droplets at equilibrium, via a trade-off between short-ranged attraction and long-ranged electrostatic repulsion.
- **Visible evidence base** Molecular dynamics simulations (LAMMPS), equilibrium field theory with numerical minimization, linear stability analysis, and supporting figures referenced in the text (Figs. 1-4, S1-S28)
- **Missing materials affecting confidence** Actual figure data, numerical values, simulation parameters beyond those described, convergence criteria, and the full supplementary information document

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting mechanism for droplet size control in biomolecular condensates, combining molecular dynamics simulations with field-theoretic analysis. The central claim that net charge asymmetry can stabilize finite-sized droplets at equilibrium is plausible and potentially significant. However, the evidence as presented is incomplete, with several technical details and quantitative validations missing. The connection to biological relevance is speculative and requires more careful articulation. The work may be suitable for a specialized physics or soft-matter journal, but the current form does not fully establish the case for a broad interdisciplinary audience.

- **Who would be interested in the results, and why** Researchers in biomolecular condensates, soft matter physics, and polymer physics would find this work relevant. The mechanism proposed could inform understanding of size control in membraneless organelles and guide design of synthetic condensate systems. The field-theoretic approach may also interest theorists working on pattern formation in phase-separating systems.

- **Major strengths**
  1. The combination of MD simulations and field theory provides complementary evidence for the proposed mechanism.
  2. The identification of a specific parameter (charge asymmetry) that controls droplet size is a clear and testable prediction.
  3. The work addresses a gap in understanding long-ranged electrostatic effects in condensates, which are often neglected.
  4. The authors acknowledge limitations and discuss robustness of the mechanism to parameter variations.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that "droplets expel ions, so they cannot screen electrostatics effectively, implying droplets acquire a net charge and cannot grow indefinitely" is central to the mechanism.
- **Evidence pointer** Figure 2, Figure S1, Section B.4
- **Concern** The mechanism relies on the inability of ions to screen charges within droplets. However, the evidence for ion expulsion is presented qualitatively. The authors state that "interactions between polymers prevent ions from moving into the droplet to neutralize it," but the quantitative extent of this expulsion and its dependence on system parameters is not clearly demonstrated. The field theory assumes charge neutrality within each phase via Lagrange multipliers, which may artificially enforce the charge separation that drives the mechanism.
- **Why it matters** If ion screening is more effective than claimed, the proposed mechanism would fail, and droplet size would not be controlled by charge asymmetry. The assumption of local charge neutrality in the field theory may bias the results toward the predicted patterned states.
- **Resolution test** Provide quantitative measures of ion concentration profiles inside and outside droplets for multiple charge asymmetries and interaction strengths. Demonstrate that the field theory results are robust to relaxing the local charge neutrality constraint. Show that the predicted droplet sizes match MD results quantitatively, not just qualitatively.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that "many droplets of equal size coexist at equilibrium" is a strong statement about the equilibrium nature of the observed states.
- **Evidence pointer** Figure 1b, Figure 4a, Section A.3
- **Concern** The demonstration of equilibrium is only briefly described in the appendix. The authors compare droplet size distributions from different initial conditions, but the details of this comparison are not provided in the main text. The timescales for equilibration, the criteria for determining equilibrium, and the statistical significance of the comparisons are not clearly stated. Finite-size effects are acknowledged but not systematically addressed.
- **Why it matters** If the observed multi-droplet states are metastable rather than equilibrium states, the central claim of the paper would be incorrect. The distinction between kinetic arrest and thermodynamic stabilization is crucial for the proposed mechanism.
- **Resolution test** Provide a more detailed description of the equilibrium tests, including quantitative comparisons of droplet size distributions from different initial conditions, analysis of temporal fluctuations, and demonstration that the systems are not trapped in metastable states. Address finite-size effects more systematically, perhaps by simulating multiple system sizes.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The claim that "electrostatic effects control droplet size, which is relevant for understanding biomolecular condensates" implies biological significance.
- **Evidence pointer** Discussion section
- **Concern** The biological relevance is asserted but not developed. The model uses simplified polymers with uniform charge distributions, while real biomolecular condensates contain complex, heterogeneous charged molecules. The authors acknowledge this limitation but do not provide a clear pathway for how their findings might translate to biological systems. The connection to specific biological phenomena (e.g., why size control matters for cellular function) is vague.
- **Why it matters** For a Nature-style audience, the significance of the work must be clearly articulated. If the mechanism only operates under idealized conditions that are unlikely in biological contexts, the broader impact is limited.
- **Resolution test** Provide a more concrete discussion of how the proposed mechanism could be tested in biological systems or how it might explain known phenomena. Discuss the parameter regimes relevant to actual biomolecular condensates and whether the predicted effects would be observable.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The claim that "the strength of the short-ranged attractions has a weak influence" on droplet size is presented as a key finding.
- **Evidence pointer** Figure 3d, Figure 4b
- **Concern** The evidence for the weak influence of interaction strength is not fully presented. The authors show that droplet size varies weakly with interaction strength in both field theory and MD, but the range of interaction strengths tested, the quantitative measure of "weak influence," and the comparison between theory and simulation are not clearly described. The claim that this is a robust feature of the mechanism requires more systematic analysis.
- **Why it matters** If the weak dependence on interaction strength is not robust, the proposed mechanism would be less general and the predictions less useful for experimental design.
- **Resolution test** Provide a systematic scan of interaction strengths in both MD and field theory, with quantitative measures of droplet size and its variation. Show that the weak dependence holds across a wide range of parameters and is not an artifact of the specific parameter choices.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Introduction
- **Evidence pointer** Main text, first two paragraphs
- **Issue** The introduction is dense and assumes significant background knowledge. Terms like "coacervates," "Flory-Huggins," and "Debye-Hückel" are used without brief explanations, which may limit accessibility for a broad readership.
- **Required correction** Add brief explanations or intuitive descriptions of key concepts to make the work accessible to nonspecialists.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Field theory formulation
- **Evidence pointer** Section B.1, equations (1)-(3)
- **Issue** The field theory is presented with limited derivation. The connection between the free energy terms and the physical interactions is not fully explained, and the choice of parameters (e.g., the form of the gradient term) is not justified.
- **Required correction** Provide a more detailed derivation or at least a clear physical motivation for each term in the free energy. Justify the parameter choices and discuss their relationship to the MD simulation parameters.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** MD simulation details
- **Evidence pointer** Section A.1
- **Issue** The MD simulation parameters are described but not all are justified. For example, the choice of box size, the number of polymers, and the equilibration protocol are stated but not discussed in terms of their adequacy for the questions addressed.
- **Required correction** Provide justification for the simulation parameters, including why the chosen system sizes are sufficient to avoid finite-size effects and why the equilibration times are adequate.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Figures
- **Evidence pointer** Figures 1-4
- **Issue** The figure captions are brief and do not fully explain the key features of each panel. Some panels are referenced in the text but not described in the captions.
- **Required correction** Expand figure captions to clearly describe what is shown in each panel, the parameters used, and the key conclusions to be drawn.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion
- **Evidence pointer** Final paragraph
- **Issue** The speculation about the origin of life and droplet division is intriguing but not well-supported by the presented work. This may distract from the main findings.
- **Required correction** Either remove the speculation or clearly label it as speculation and connect it more explicitly to the presented results.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: The mechanism of ion expulsion and its quantitative basis requires stronger evidence.
  - R1-M2: The demonstration of equilibrium needs more rigorous and detailed support.
  - The quantitative agreement between MD simulations and field theory predictions is not clearly established; the authors should provide direct comparisons of droplet sizes and other observables.

- **Assessment against Nature-style criteria**
  - **Originality**: The idea of using charge asymmetry to control droplet size is novel and not commonly explored in the condensate literature. The combination of MD and field theory is appropriate.
  - **Scientific importance**: The mechanism could be important for understanding size control in biomolecular condensates, but the biological relevance is not yet convincingly demonstrated. The work is more likely to appeal to a specialized physics/soft-matter audience than a broad biological readership.
  - **Interdisciplinary readership**: The work bridges physics, chemistry, and biology, but the presentation is heavily weighted toward the physics. Biologists may find the model too idealized and the connection to real systems too speculative.
  - **Technical soundness**: The methods are appropriate, but the evidence presented is incomplete. The equilibrium demonstration and the quantitative comparison between theory and simulation need strengthening.
  - **Readability for nonspecialists**: The manuscript is not easily accessible to nonspecialists. The introduction and methods require significant background knowledge, and the figures are not self-explanatory.

- **Recommendation posture** Currently not established from the provided evidence. The central claims are plausible and the approach is promising, but the evidence as presented is insufficient to fully support the conclusions. The authors should address the major concerns, particularly the quantitative validation of the mechanism and the demonstration of equilibrium, before the work can be considered for publication in a high-impact journal.