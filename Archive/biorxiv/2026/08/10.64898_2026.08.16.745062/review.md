## Review setup
- **Input scope** Full manuscript text (abstract, introduction, models and methods, results and discussion, conclusions, acknowledgements)
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by presented evidence. No assessment of formatting, grammar, or editorial quality beyond what affects scientific clarity.
- **Shared manuscript claim summary** The authors develop a two-level coarse-grained model of human synapsin-1, deriving an effective one-particle-per-protein interaction from residue-level CALVADOS 3 simulations via umbrella sampling. They compare two mesoscopic models differing only in retention of a weak outer repulsive tail and show via Langevin dynamics that this tail markedly alters collective aggregation, morphology, and internal mobility.
- **Visible evidence base** Abstract, Introduction, Models and Methods, Results and Discussion, Conclusions, Acknowledgements. Figures 1–8 are referenced but not provided. Tables 1 is referenced but not provided.
- **Missing materials affecting confidence** All figures and tables are absent. Simulation parameter details (box size, equilibration protocols, number of replicates) are partially described but not fully specified. No supplementary information is provided.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question in biomolecular condensate research: how weak features of effective protein-protein interactions propagate to mesoscale collective behavior. The hierarchical coarse-graining strategy is conceptually sound and the comparison between two models differing only in the outer interaction tail is a clean design. However, the absence of all figures and tables makes it impossible to evaluate the quantitative claims, the morphological assignments, or the quality of the PMF fit. The manuscript is promising but currently not fully assessable from the provided material.
- **Who would be interested in the results, and why** Researchers in biomolecular condensate physics, coarse-grained simulation method development, and synaptic biology. The work speaks to the broader question of how interaction potential shape controls phase behavior and cluster morphology, which is relevant to the condensate field generally. The specific application to synapsin-1 connects to experimental studies of synaptic vesicle clustering.
- **Major Strengths** The hierarchical approach from residue-level to one-particle-per-protein is a sensible and increasingly important strategy. The controlled comparison between two models that differ only in the outer tail is a rigorous way to isolate the effect of that feature. The dynamical analysis distinguishing aggregate-associated from free particle mobility adds a useful dimension beyond static structure. The authors are appropriately cautious about not overinterpreting their results as equilibrium phase behavior.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence availability
  - **Claim pointer** The manuscript claims specific aggregation morphologies, cluster statistics, and mobility ratios that are presented in Figures 3–8.
  - **Evidence pointer** Figures 3–8, location not provided
  - **Concern** All figures are missing from the provided material. The central claims of the paper, including the qualitative difference between Model A and Model B aggregation behavior, the morphological assignments (droplet, cylinder, slab, inverted), and the mobility ratio analysis, cannot be evaluated without the actual data.
  - **Why it matters** The entire scientific case rests on these figures. Without them, the claims are unverifiable.
  - **Resolution test** Provide all figures with appropriate captions and axis labels. The figures must clearly show the described trends and support the morphological assignments.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Methodological completeness
  - **Claim pointer** The PMF is obtained by umbrella sampling and represented by an analytical function with parameters listed in Table 1.
  - **Evidence pointer** Models and Methods, Table 1, location not provided
  - **Concern** Table 1 is not provided, so the fitted parameters cannot be examined. Additionally, the umbrella sampling details are incomplete: the number of windows is stated (88), but the window spacing, the convergence criteria beyond the self-consistency tolerance, the initial configuration preparation, and the treatment of long-range electrostatics are not described. The analytical form of the potential is only partially given.
  - **Why it matters** The quality of the PMF and its analytical representation is foundational to all subsequent simulations. Without the parameters and full functional form, the work cannot be reproduced or assessed.
  - **Resolution test** Provide Table 1 with all fitted parameters, the complete analytical form of the potential, and full umbrella sampling details including window spacing, equilibration, and error analysis.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Interpretive caution
  - **Claim pointer** The manuscript states that Model B behavior is "consistent with the competition characteristic of SALR-like interactions" and cites references 36 and 38.
  - **Evidence pointer** Results and Discussion, location not provided
  - **Concern** The connection to SALR physics is plausible but the manuscript does not quantify how closely the effective potential resembles canonical SALR models. The oscillatory features in the PMF are noted but not analyzed. The claim of consistency is qualitative and not supported by any quantitative comparison.
  - **Why it matters** The SALR interpretation is a key conceptual framing. Without quantitative support, it remains speculative.
  - **Resolution test** Provide a quantitative comparison of the effective potential to SALR forms, or temper the claim to reflect the qualitative nature of the analogy.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Finite-size and protocol effects
  - **Claim pointer** The manuscript states that Model B "sustains multiple finite-size aggregates over a broad range of conditions" and that this contrasts with Model A.
  - **Evidence pointer** Results and Discussion, Figures 7 and 8, location not provided
  - **Concern** The simulations use a sequential cooling protocol in a finite periodic box. The manuscript acknowledges sensitivity to metastability and geometry but does not address whether the observed differences between models could be influenced by the cooling rate, the box size, or the specific density grid. No systematic study of these effects is presented.
  - **Why it matters** The central claim of the paper is that the outer tail changes collective organization. If the difference is an artifact of the protocol or finite-size effects, the conclusion would be weakened.
  - **Resolution test** Provide evidence that the qualitative differences between models are robust to box size, cooling rate, and initial conditions, or discuss these limitations explicitly.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Models and Methods, umbrella sampling description
  - **Evidence pointer** Models and Methods, location not provided
  - **Issue** The sentence describing the harmonic biasing potential is incomplete. The equation is referenced but not shown.
  - **Required correction** Provide the full equation for the biasing potential.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Simulation parameters
  - **Evidence pointer** Models and Methods, location not provided
  - **Issue** The damping parameter is stated as 1.0 but the reduced units are not fully defined. The time step is given as 0.001 but the unit system is not explicit.
  - **Required correction** Define the reduced unit system completely, including the relationship to physical units.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interpretive precision
  - **Affected element** Results and Discussion, connection to experiments
  - **Evidence pointer** Results and Discussion, location not provided
  - **Issue** The connection to Hoffmann et al. is described as "qualitative" but the specific experimental conditions and how they map to the simulation parameters are not discussed.
  - **Required correction** Clarify the mapping between simulation conditions and the experimental context, or state more explicitly the limits of the comparison.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Internal consistency
  - **Affected element** Results and Discussion, reference to references 35, 36, 38
  - **Evidence pointer** Results and Discussion, location not provided
  - **Issue** The text cites references 35, 36, and 38 in the context of SALR behavior, but the same references are cited earlier for the cluster identification criterion. It is unclear if these are the same references or if the citation numbering is inconsistent.
  - **Required correction** Verify citation numbering and ensure each reference is cited in the appropriate context.
- **Technical failings that need to be addressed before the case is established** R1-M1 (missing figures), R1-M2 (missing table and incomplete methodological details). These are blocking because the core claims cannot be evaluated without the data and the methods cannot be reproduced without full parameterization.
- **Assessment against Nature-style criteria**  
  *Originality*: The hierarchical approach is not entirely novel but the specific application to synapsin-1 and the systematic comparison of outer-tail effects is a fresh contribution. The originality is moderate.  
  *Scientific importance*: The question of how weak interaction features control collective behavior is important for the condensate field. The potential implications for understanding synaptic vesicle clustering are significant.  
  *Interdisciplinary readership*: The work bridges biophysics, soft matter physics, and neuroscience. The writing is accessible to a broad physical science audience, though the neuroscience context is somewhat thin.  
  *Technical soundness*: The methodology is appropriate in principle, but the missing data and incomplete parameterization prevent a full assessment. The lack of systematic finite-size and protocol checks is a concern.  
  *Readability for nonspecialists*: The manuscript is generally well written and the logic is clear. The abstract is effective. However, the incomplete equations and missing figures hinder comprehension.
- **Recommendation posture** Currently not established from the provided evidence. The conceptual framework and methodological design are sound, but the absence of all figures and the key table, combined with incomplete methodological details, prevents verification of the central claims. The manuscript could become supportive if the missing material is provided and the technical concerns are addressed.

## Risk / unsupported claims
- The claim that Model B sustains multiple aggregates over a broad range of conditions is unsupported without Figures 7 and 8.
- The claim that the dynamical contrast between aggregate-associated and free particles depends on aggregate size in Model B is unsupported without Figure 5.
- The claim that pressure anomalies correlate with structural boundaries is unsupported without Figure 6.
- The qualitative connection to experimental observations of Hoffmann et al. is not assessable without the data in Figure 5 and a more detailed mapping to experimental conditions.
- The statement that the effective potential is "reminiscent of SALR interactions" is a qualitative interpretation that is not quantitatively supported.
- The claim that the PMF is "state specific" and "reference" is appropriately cautious, but the extent to which this limits transferability is not discussed.