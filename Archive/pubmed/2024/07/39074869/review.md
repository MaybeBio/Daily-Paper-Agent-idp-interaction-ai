## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no access to methods, figures, or simulation details
- **Shared manuscript claim summary** The authors use molecular simulations to show that short-range electrostatic interactions between a phosphorylated serine and conserved positively charged residues within the phospho-motif of the NCBD can counteract the compaction induced by long-range electrostatic interactions, thereby rescuing the binding competency of phosphorylated NCBD. They propose that such proximal electrostatic interactions may act as a general regulatory relay in phosphorylated intrinsically disordered proteins.
- **Visible evidence base** Abstract text only; no simulation protocols, force fields, convergence criteria, or quantitative results are provided
- **Missing materials affecting confidence** Full methods, simulation parameters, force field choice, sampling length and convergence assessment, structural ensembles, quantitative comparison of long-range versus short-range interaction contributions, and any experimental validation

## Reviewer
- **Overall assessment** The abstract presents an interesting and potentially significant hypothesis regarding the role of short-range electrostatic interactions in modulating the effects of phosphorylation on disordered proteins. However, the evidence base is limited to a summary of simulation findings without quantitative detail, making it impossible to assess the robustness of the conclusions. The conceptual framework is appealing, but the current presentation does not establish the case with sufficient rigor.
- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, post-translational modification signaling, and computational biophysics would find these results relevant. The proposed relay mechanism could inform understanding of how phosphorylation effects are tuned in disordered regulatory regions, which is of broad interest to cell signaling and drug discovery communities.
- **Major strengths** The study addresses a mechanistically important question about how phosphorylation effects on disordered proteins might be modulated by local sequence features. The focus on distinguishing short-range from long-range electrostatics is conceptually clear and potentially impactful. The proposal of a general relay mechanism based on conserved phospho-motif positive charges is intellectually appealing and testable.
- **Major Concerns**  
  - **Concern ID** R1-M1  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Technical soundness  
  - **Claim pointer** The claim that "empowering proximal electrostatic interactions, as opposed to long-range electrostatics, can reshape the NCBD ensemble rescuing the binding competency of phosphorylated NCBD"  
  - **Evidence pointer** Abstract only; location not provided  
  - **Concern** The abstract provides no quantitative data on the simulation results. There is no indication of how the relative contributions of short-range versus long-range electrostatics were deconvoluted, what metrics were used to define "binding competency," or how the ensemble reshaping was characterized. Without these details, the central claim cannot be evaluated.  
  - **Why it matters** The distinction between short-range and long-range electrostatic effects is subtle and requires careful computational design to isolate. If the simulation setup does not adequately separate these contributions, the conclusion may be an artifact of the chosen methodology.  
  - **Resolution test** Provide quantitative ensemble descriptors (e.g., radius of gyration, contact maps, binding free energy estimates) for phosphorylated NCBD with and without the proximal interactions, and demonstrate that the effect is robust across simulation replicates and force field choices.

  - **Concern ID** R1-M2  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Technical soundness  
  - **Claim pointer** The claim that "proximal electrostatic interactions might dampen the effects of phosphorylation and act as a relay to regulate phosphorylated intrinsically disordered proteins"  
  - **Evidence pointer** Abstract only; location not provided  
  - **Concern** The generalization from a single system (NCBD) to a broad class of phosphorylated disordered proteins is presented without supporting evidence. The abstract does not describe any comparative analysis across different phospho-motifs or proteins that would justify this generalization.  
  - **Why it matters** The proposed relay mechanism is the main conceptual contribution of the work. If it is based solely on one system, the claim is overreaching and may mislead readers into assuming broader applicability than is demonstrated.  
  - **Resolution test** Either temper the claim to be system-specific or provide additional simulations or sequence analysis showing that the relay mechanism operates across diverse phospho-motif contexts.

  - **Concern ID** R1-M3  
  - **Severity** Major  
  - **Blocking** No  
  - **Axis** Reproducibility  
  - **Claim pointer** The overall simulation-based findings  
  - **Evidence pointer** Abstract only; location not provided  
  - **Concern** No information is given about simulation length, convergence, force field, or sampling methodology. Without these details, the reliability of the ensemble predictions cannot be assessed.  
  - **Why it matters** Disordered protein simulations are highly sensitive to force field parameters and sampling adequacy. The absence of this information prevents any assessment of whether the observed effects are physically meaningful or computational artifacts.  
  - **Resolution test** Include a detailed methods section with force field parameters, simulation length, convergence metrics, and validation against experimental data where available.

- **Minor Comments**  
  - **Concern ID** R1-m1  
  - **Severity** Minor  
  - **Axis** Clarity  
  - **Affected element** Terminology  
  - **Evidence pointer** Abstract  
  - **Issue** The term "binding competency" is used without definition. It is unclear whether this refers to a specific computed metric or a qualitative assessment.  
  - **Required correction** Define "binding competency" operationally, for example, in terms of binding free energy estimates or population of binding-competent conformations.

  - **Concern ID** R1-m2  
  - **Severity** Minor  
  - **Axis** Context  
  - **Affected element** Background  
  - **Evidence pointer** Abstract  
  - **Issue** The abstract states that phosphorylation lowers binding affinity but does not specify the magnitude or the binding partners affected.  
  - **Required correction** Provide quantitative context from prior work to establish the baseline effect that the proposed rescue mechanism is counteracting.

  - **Concern ID** R1-m3  
  - **Severity** Minor  
  - **Axis** Precision  
  - **Affected element** Language  
  - **Evidence pointer** Abstract  
  - **Issue** The phrase "empowering proximal electrostatic interactions" is vague and could be interpreted in multiple ways.  
  - **Required correction** Specify what was changed in the simulations to "empower" these interactions, for example, mutation of specific residues or modification of charge parameters.

- **Technical failings that need to be addressed before the case is established** R1-M1 and R1-M2 are blocking. The absence of quantitative simulation data and the overgeneralization from a single system prevent the core claims from being evaluated. R1-M3, while not blocking, is essential for reproducibility and should be addressed.

- **Assessment against Nature-style criteria**  
  - **Originality** The idea of short-range electrostatic interactions acting as a relay to modulate phosphorylation effects is conceptually novel and could be of interest to a broad readership.  
  - **Scientific importance** If substantiated, the proposed mechanism could have implications for understanding phosphorylation signaling in disordered proteins, which is a topic of high current interest.  
  - **Interdisciplinary readership** The topic bridges computational biophysics, structural biology, and cell signaling, which could attract readers from multiple disciplines.  
  - **Technical soundness** Currently not assessable from the abstract alone. The lack of methodological detail and quantitative results is a significant barrier.  
  - **Readability for nonspecialists** The abstract is reasonably accessible, but the vague terminology and lack of quantitative context reduce clarity for nonspecialists.

- **Recommendation posture** Currently not established from the provided evidence. The conceptual framework is promising, but the abstract does not provide sufficient technical detail to support the central claims. The authors should be encouraged to resubmit with full methodological transparency and quantitative results, and with a more tempered generalization of their findings.

## Risk / unsupported claims
- The claim that short-range electrostatics can rescue binding competency of phosphorylated NCBD is unsupported without quantitative ensemble data.
- The generalization to a general relay mechanism for phosphorylated disordered proteins is unsupported from a single system study.
- The statement that "proximal electrostatic interactions might dampen the effects of phosphorylation" is presented as a conclusion but is framed as speculation in the abstract; this distinction should be clarified.