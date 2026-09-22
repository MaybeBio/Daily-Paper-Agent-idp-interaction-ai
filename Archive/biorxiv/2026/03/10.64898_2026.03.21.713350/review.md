## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors present CGRig, a rigid-body coarse-grained protein model with residue-level interaction sites, designed for long-time and large-scale protein assembly simulations. The model uses overdamped Langevin dynamics with a shape-dependent friction matrix, Gō-like native contacts, Debye–Hückel electrostatics, and volume exclusion. Validation claims include accurate reproduction of translational and rotational diffusion coefficients, maintenance of native dimeric complexes, convergence of separated proteins to correct complexes with all-atom-consistent association rates, and a performance exceeding 17 μs/day for a 1,024-molecule system.
- **Visible evidence base** Abstract text only; no figures, tables, methods sections, or supplementary data were supplied
- **Missing materials affecting confidence** Full manuscript text, all figures and tables, methods details, parameter values, simulation protocols, validation datasets, and performance benchmarking details

## Reviewer
- **Overall assessment** The abstract describes a potentially useful coarse-grained rigid-body protein model with residue-level interaction sites, targeting a genuine gap in the trade-off between computational efficiency and structural fidelity. The reported performance figure is notable, and the validation strategy is sensible in outline. However, the abstract alone provides insufficient detail to assess the technical soundness of the model, the robustness of the validation, or the generalizability of the claims. Several key assertions, particularly regarding association rate consistency and the maintenance of native complex structures, cannot be evaluated without quantitative data and methodological specifics. The work is of interest to the computational biophysics and molecular simulation communities, but the case is not fully established from the supplied material.
- **Who would be interested in the results, and why** Computational biophysicists and molecular modelers working on protein-protein interactions, self-assembly, and cellular-scale simulation. Researchers developing coarse-grained models will be interested in the rigid-body treatment with residue-level interaction sites as a middle ground between single-particle and multi-bead representations. Those studying large-scale biomolecular systems, such as viral capsid assembly or phase separation, may find the reported performance attractive.
- **Major strengths** The model design addresses a clear limitation of existing approaches by retaining residue-level interaction specificity while treating each protein as a single rigid body. The use of a shape-dependent friction matrix is physically appropriate for anisotropic objects. The reported simulation speed of 17 μs/day for a 1,024-molecule system is impressive and suggests practical utility for large-scale studies. The validation strategy, covering single-protein diffusion, dimer stability, and association kinetics, is logically structured.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** "We validated that CGRig accurately reproduces the translational and rotational diffusion coefficients expected from the friction matrix for an isolated protein."
  - **Evidence pointer** Abstract only; location not provided
  - **Concern** The claim of accurate reproduction of diffusion coefficients is presented without quantitative comparison. No error metrics, reference values, or statistical measures are given. The phrase "expected from the friction matrix" is circular unless the friction matrix itself is independently validated against known hydrodynamic properties.
  - **Why it matters** Diffusion coefficients are fundamental to the dynamics of the model. If the friction matrix is not correctly parameterized, all subsequent dynamical properties, including association rates, will be affected. Without quantitative evidence, the reader cannot judge whether the agreement is within acceptable tolerances.
  - **Resolution test** Provide a table or figure comparing computed translational and rotational diffusion coefficients against theoretical predictions or experimental values for multiple proteins of varying shapes and sizes, with quantitative error analysis.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** "For dimeric systems, the model successfully maintained native complex structures."
  - **Evidence pointer** Abstract only; location not provided
  - **Concern** The abstract does not specify the dimeric systems studied, the simulation timescales, the structural metrics used to define "maintained," or the stability criteria. Without this information, the claim is ambiguous. It is unclear whether the native structure was maintained for the entire simulation, what RMSD or contact-map thresholds were used, and whether multiple dimeric systems were tested.
  - **Why it matters** The ability to maintain native complexes is a core requirement for any model intended for assembly simulations. If the model cannot preserve known complexes, its utility for predicting assembly pathways is questionable. The lack of specificity prevents assessment of the robustness of this claim.
  - **Resolution test** Specify the dimeric systems, simulation lengths, structural metrics (e.g., RMSD, fraction of native contacts), and stability criteria. Provide representative trajectories or time series showing structural maintenance.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** "Two initially separated proteins converged into the correct complex with an association rate consistent with all-atom simulations."
  - **Evidence pointer** Abstract only; location not provided
  - **Concern** The claim of association rate consistency with all-atom simulations is a strong quantitative statement, yet no rate constants, error bars, or comparison details are provided. It is unclear which all-atom simulations were used as reference, how many independent association events were simulated, and what statistical confidence is associated with the reported rate.
  - **Why it matters** Association kinetics are highly sensitive to interaction potentials and hydrodynamic treatment. A claim of consistency with all-atom simulations, if substantiated, would be a strong validation of the model. Without quantitative data, this claim cannot be verified and may overstate the model's accuracy.
  - **Resolution test** Provide association rate constants with confidence intervals for CGRig and the reference all-atom simulations, including the number of independent runs and the simulation conditions. Show that the rates agree within statistical uncertainty.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Generalizability
  - **Claim pointer** "CGRig provides an efficient framework for simulating protein assembly while retaining residue-level interaction specificity, making it a valuable tool for investigating large-scale biomolecular self-assembly."
  - **Evidence pointer** Abstract only; location not provided
  - **Concern** The abstract demonstrates validation on isolated proteins and dimeric systems only. The claim of utility for "large-scale biomolecular self-assembly" implies applicability to systems with many proteins and potentially heterogeneous assemblies. No evidence is presented for multi-component systems, concentration-dependent behavior, or assembly beyond dimers.
  - **Why it matters** The stated purpose of the model is long-time and large-scale assembly simulation. If the model has only been tested on dimers, its behavior in crowded, multi-body environments is unknown. The claim of general utility is therefore premature.
  - **Resolution test** Present simulations of larger assemblies (e.g., trimers, tetramers, or higher-order oligomers) or multi-component mixtures, demonstrating that the model captures correct assembly products and kinetics in these more complex scenarios.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Model description
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The abstract states that "intermolecular interactions are calculated using Gō-like native contact potentials, Debye–Hückel electrostatics, and volume exclusion," but does not specify how these terms are combined, whether they are pairwise additive, or how the Gō-like potential is defined for rigid bodies.
  - **Required correction** Provide a brief description of the functional forms and how the interaction sites are distributed on the rigid body, or refer to a methods section where these details are given.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Performance claim
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The performance figure of 17 μs/day for a 1,024-molecule system is reported without specifying hardware, software, parallelization strategy, or the simulation conditions (e.g., box size, cutoff, integration timestep).
  - **Required correction** Specify the hardware and software environment, the number of cores or GPUs used, and the simulation parameters that affect performance.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Scope
  - **Affected element** Validation breadth
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The validation is limited to a single-protein diffusion test and dimeric systems. No mention is made of testing on proteins with different shapes, sizes, or charge distributions, nor on systems with non-native interactions.
  - **Required correction** Acknowledge the limited validation scope in the abstract or add validation results for a more diverse set of proteins.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, and R1-M3 are blocking because the core validation claims are presented without quantitative evidence. R1-M4 is non-blocking but should be addressed to support the stated scope of the model.
- **Assessment against Nature-style criteria**  
  *Originality*: The rigid-body treatment with residue-level interaction sites is a reasonable incremental contribution, but similar concepts exist in other coarse-grained models. The originality is moderate and depends on the specific implementation details, which are not fully visible.  
  *Scientific importance*: The potential to simulate large-scale protein assembly with residue-level specificity is scientifically important, but the demonstrated scope (dimers only) limits the current importance.  
  *Interdisciplinary readership*: The work is primarily of interest to computational biophysicists and modelers. The abstract is written in a way that is accessible to this audience, but the lack of quantitative results reduces its appeal to a broader readership.  
  *Technical soundness*: Cannot be fully assessed from the abstract. The blocking concerns above indicate that the technical validation is not yet established.  
  *Readability for nonspecialists*: The abstract is clearly written and avoids excessive jargon, but the lack of quantitative context makes it difficult for nonspecialists to gauge the significance of the claims.
- **Recommendation posture** Currently not established from the provided evidence. The model concept is promising and the performance figure is attractive, but the core validation claims require quantitative support. I would be supportive if the blocking concerns are resolved with detailed data and methods.

## Risk / unsupported claims
- The claim of accurate reproduction of diffusion coefficients is unsupported without quantitative comparison data.
- The claim of maintaining native dimeric structures is unsupported without specification of systems, timescales, and structural metrics.
- The claim of association rate consistency with all-atom simulations is unsupported without rate constants and statistical analysis.
- The claim of general utility for large-scale biomolecular self-assembly is not supported by the demonstrated validation scope (single proteins and dimers only).
- The performance figure of 17 μs/day is not reproducible without hardware and software specifications.