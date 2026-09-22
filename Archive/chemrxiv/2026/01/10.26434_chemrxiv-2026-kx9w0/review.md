## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the supplied abstract
- **Shared manuscript claim summary** The authors present AMPv3, a next-generation neural network potential with anisotropic message passing, trained on the BMS25 dataset. They claim DFT-level accuracy for condensed-phase biomolecular simulations via a multiscale QM/MM-like electrostatic embedding approach, enabling simulations of proteins with thousands of atoms plus explicit MM solvent for up to hundreds of nanoseconds on a single GPU. They further claim accurate estimation of experimental properties (solvation free energies, protein structural features) and successful prediction of enzyme reaction free-energy profiles for chorismate mutase and fluoroacetate dehalogenase, supported by a cumulative 23 µs simulation time or 48 billion integration steps.
- **Visible evidence base** Abstract text only. No figures, tables, methods, or supplementary materials were provided.
- **Missing materials affecting confidence** Full manuscript, all figures and tables, dataset description (BMS25), model architecture details, training and validation protocols, benchmark definitions, error metrics, simulation setup details, and comparison baselines.

## Reviewer
- **Overall assessment** The abstract describes an ambitious and potentially impactful advance in biomolecular simulation using neural network potentials. The multiscale approach and reported simulation timescales are notable. However, the abstract alone provides insufficient quantitative evidence to evaluate the core claims of accuracy, efficiency, and generalizability. The central assertions regarding DFT-level accuracy and experimental property prediction are presented without numerical benchmarks or statistical validation. The enzyme reaction free-energy results are mentioned but not substantiated with any data. While the work appears promising, the case is not established from the supplied material.
- **Who would be interested in the results, and why** Computational chemists and biophysicists working on molecular dynamics, enzyme mechanism elucidation, and drug discovery would be interested. The potential to simulate large proteins with explicit solvent at DFT-level accuracy for hundreds of nanoseconds addresses a long-standing bottleneck in the field. Researchers developing machine learning potentials and multiscale methods would also find the methodological advances relevant.
- **Major strengths** The multiscale electrostatic embedding approach is conceptually sound and addresses a real limitation of current NNPs for condensed-phase biomolecular systems. The reported cumulative simulation time of 23 µs across proteins is impressive and suggests practical utility. The application to enzyme reactions, specifically chorismate mutase and fluoroacetate dehalogenase, demonstrates a meaningful test of the method beyond equilibrium properties.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The model achieves "DFT accuracy" in condensed-phase simulations of proteins with thousands of atoms.
  - **Evidence pointer** Abstract, location not provided
  - **Concern** The abstract asserts DFT-level accuracy but provides no quantitative comparison against DFT reference calculations, no error metrics (e.g., energy or force errors), and no benchmark results against established methods or datasets. The term "DFT accuracy" is undefined in terms of which functional, basis set, or property is being matched.
  - **Why it matters** The central value proposition of the work rests on this accuracy claim. Without quantitative evidence, readers cannot assess whether the model genuinely achieves the stated accuracy or whether the claim is based on favorable but selective comparisons.
  - **Resolution test** Provide numerical error metrics (e.g., mean absolute errors for energies and forces) against DFT references on held-out test sets, including comparisons with other NNPs and QM/MM baselines.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The model "can be used to accurately estimate experimental properties, including solvation free energies of small molecules and structural features of proteins."
  - **Evidence pointer** Abstract, location not provided
  - **Concern** No numerical results are presented for solvation free energies or protein structural features. The abstract does not specify which molecules were tested, which experimental references were used, what the errors were, or how the structural features were compared (e.g., RMSD, secondary structure content, or ensemble properties).
  - **Why it matters** The claim of experimental property estimation is a key demonstration of practical utility. Without data, the claim is unverifiable and could be based on a small or favorable subset of test cases.
  - **Resolution test** Present tables or figures with computed versus experimental solvation free energies for a defined set of molecules, including error statistics. For protein structure, provide quantitative comparisons of simulated ensembles against experimental structures or experimental observables (e.g., chemical shifts, J-couplings).
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The model "was employed to predict the free-energy profiles of reactions catalyzed by the enzymes chorismate mutase and fluoroacetate dehalogenase."
  - **Evidence pointer** Abstract, location not provided
  - **Concern** The abstract reports that free-energy profiles were predicted but provides no information on the computed barriers, comparison with experimental or high-level computational references, or the methodology used to compute the free-energy profiles (e.g., umbrella sampling, metadynamics, or thermodynamic integration).
  - **Why it matters** Enzyme reaction profiles are a stringent test of the model's ability to describe chemical bond breaking and formation. Without results, the claim is unsubstantiated and the reader cannot judge whether the predictions are accurate or merely plausible.
  - **Resolution test** Provide free-energy profiles for both enzymes, including computed activation barriers and reaction free energies, compared with experimental values or high-level QM/MM reference calculations.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** The multiscale approach is "similar to QM/MM with electrostatic embedding."
  - **Evidence pointer** Abstract, location not provided
  - **Concern** The abstract does not describe how the multiscale partitioning is implemented, how the electrostatic embedding is treated, how the boundary between the NNP region and the MM region is handled, or how long-range electrostatics are computed. The similarity to QM/MM is stated but not detailed.
  - **Why it matters** The technical implementation of the multiscale scheme is critical for reproducibility and for understanding potential artifacts (e.g., boundary effects, polarization treatment). Without this information, the approach cannot be evaluated or replicated.
  - **Resolution test** Provide a detailed methods section describing the multiscale scheme, including the partitioning scheme, embedding treatment, and any approximations or corrections applied.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Model naming
  - **Evidence pointer** Abstract, location not provided
  - **Issue** The abstract uses multiple names for the model (AMPv3, AMPv3-BMS25, AMP-BMS, AMP-BMS/MM) without clearly defining when each name applies.
  - **Required correction** Define the model name and its variants explicitly in the abstract or introduction, and use consistent terminology throughout.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Simulation time claim
  - **Evidence pointer** Abstract, location not provided
  - **Issue** The cumulative simulation time of 23 µs and 48 billion integration steps is stated without context on how this time is distributed across systems, how many independent simulations were performed, or what timestep was used.
  - **Required correction** Provide a breakdown of simulation time per system and specify the integration timestep and any constraints used.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Efficiency claim
  - **Evidence pointer** Abstract, location not provided
  - **Issue** The claim of "excellent scaling to large systems on a single GPU" is vague without specifying system sizes, GPU model, or comparison to other methods.
  - **Required correction** Provide quantitative scaling data, including system sizes, GPU hardware, and comparison with other NNPs or classical force fields.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3. The core claims of accuracy, experimental property estimation, and enzyme reaction prediction are not supported by quantitative evidence in the supplied material. R1-M4 is important for reproducibility but is not strictly blocking if the full manuscript provides the necessary details.
- **Assessment against Nature-style criteria**  
  *Originality*: The multiscale approach combining an NNP with electrostatic embedding for large biomolecular systems is a meaningful advance over existing NNPs, which typically operate on smaller scales. The application to enzyme reactions is a valuable extension. However, the conceptual framework is not entirely new, as QM/MM and related multiscale methods are well established.  
  *Scientific importance*: If the claims are substantiated, the work would be highly important, as it addresses a major bottleneck in simulating large biomolecules at high accuracy. The reported simulation timescales would represent a significant step forward.  
  *Interdisciplinary readership*: The work would appeal to computational chemists, biophysicists, and enzymologists. The abstract is written in a way that is accessible to these audiences, though some technical terms (e.g., anisotropic message passing) may require prior knowledge.  
  *Technical soundness*: Cannot be assessed from the abstract alone. The lack of quantitative results and methodological details prevents evaluation of the technical implementation.  
  *Readability for nonspecialists*: The abstract is concise and generally clear, but the significance of the claims is difficult to gauge without numbers. A nonspecialist would understand the broad goal but not the evidence.
- **Recommendation posture** Currently not established from the provided evidence. The work is potentially significant, but the abstract alone does not provide sufficient quantitative support for the central claims. A full review of the complete manuscript would be required to assess whether the technical concerns are resolved.

## Risk / unsupported claims
- The claim of "DFT accuracy" is unsupported without quantitative error metrics.
- The claim of accurate estimation of solvation free energies and protein structural features is unsupported without numerical results.
- The claim of predicting enzyme reaction free-energy profiles is unsupported without barrier heights or comparisons.
- The claim of "excellent scaling" is unsupported without specific performance data.
- The cumulative simulation time of 23 µs is stated but not contextualized with system details or simulation conditions.