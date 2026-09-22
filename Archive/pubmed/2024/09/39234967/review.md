## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no full text, figures, tables, or supplementary materials provided
- **Shared manuscript claim summary** The authors develop a multiscale coarse-grain model for NISTmAb, lysozyme, and lactoferrin, precomputing anisotropic interactions between rigid bodies from atomistic models, and demonstrate that this approach predicts experimental radius of gyration and second osmotic virial coefficient data, enabling efficient Monte Carlo simulations at medically relevant protein concentrations.
- **Visible evidence base** Abstract text only; no quantitative results, methodological details, or validation data are available
- **Missing materials affecting confidence** Full manuscript, all figures and tables, simulation parameters, force field details, validation datasets, and comparison with experimental methods

## Reviewer
- **Overall assessment** The abstract presents a conceptually promising multiscale coarse-graining strategy that could address a significant computational bottleneck in simulating high-concentration protein solutions. The idea of precomputing orientation-dependent interactions between rigid bodies and interpolating during Monte Carlo simulations is technically sound in principle and has potential for broad applicability. However, the abstract provides insufficient quantitative evidence to evaluate the accuracy, efficiency, or robustness of the method. The claim that the approach predicts experimental data is stated without any numerical support, and the scope of validation appears limited to two model proteins and one antibody. The methodological novelty relative to existing coarse-graining approaches is not clearly articulated. The work may be of interest to computational biophysicists and soft matter scientists, but the current evidence base is too thin to establish the case.
- **Who would be interested in the results, and why** Computational biophysicists and soft matter physicists studying protein interactions, phase behavior, and aggregation at high concentrations would be the primary audience. Researchers developing coarse-graining methodologies for biomolecular simulations would also find the approach relevant. Additionally, the pharmaceutical community investigating monoclonal antibody formulation stability could benefit from a computationally efficient tool to explore concentration-dependent phenomena.
- **Major strengths** The multiscale strategy that preserves atomistic detail while enabling orders-of-magnitude efficiency gains is conceptually attractive. The decomposition of NISTmAb into three rigid bodies with a flexible hinge is a sensible structural approximation. The use of an open-source software framework enhances reproducibility and accessibility. The focus on medically relevant concentrations addresses a practical need in biopharmaceutical development.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: The precomputation of anisotropic interaction tables for rigid bodies is a creative extension of existing coarse-graining methods, though the abstract does not clearly distinguish it from prior work on orientation-dependent potentials. Scientific importance: The potential to simulate high-concentration protein systems with atomistic fidelity is significant for understanding aggregation and phase separation, but the demonstrated impact is not yet established. Interdisciplinary readership: The work bridges molecular simulation, biophysics, and pharmaceutical formulation science, which could attract a broad audience if the results are compelling. Technical soundness: The approach is plausible, but the abstract provides no quantitative validation, error analysis, or comparison with alternative methods, leaving technical rigor unassessed. Readability for nonspecialists: The abstract is reasonably clear for a technical audience, but the significance and limitations are not framed in a way that would engage nonspecialists.
- **Recommendation posture** Currently not established from the provided evidence. The abstract alone does not provide sufficient quantitative support for the central claims. A supportive posture would require full manuscript review with detailed validation data.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The abstract claims that the coarse-graining strategy "predicts experimentally measured radius of gyration and second osmotic virial coefficient data."
- **Evidence pointer** Abstract only; no figures or tables provided
- **Concern** The abstract states that the method predicts experimental data but provides no numerical values, error margins, or statistical measures of agreement. It is unclear how many experimental datasets were used for comparison, over what concentration ranges, and whether the predictions fall within experimental uncertainty.
- **Why it matters** The central validation claim of the manuscript rests on this comparison. Without quantitative evidence, the reader cannot assess whether the agreement is meaningful or coincidental, and the claim cannot be independently verified.
- **Resolution test** Provide in the full manuscript a table or figure showing predicted versus experimental values for radius of gyration and second osmotic virial coefficient for all three systems, including uncertainties and the number of independent measurements.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological completeness
- **Claim pointer** The abstract states that "interactions between arbitrarily oriented rigid bodies to be interpolated from the precomputed table during coarse-grained Monte Carlo simulations."
- **Evidence pointer** Abstract only; no methodological details provided
- **Concern** The abstract does not describe the discretization scheme for relative orientations, the interpolation method, the grid resolution, or the associated interpolation errors. It is also unclear how the implicit solvent model is parameterized and whether it is consistent across the three systems.
- **Why it matters** The accuracy and efficiency of the method depend critically on these technical choices. Without this information, the reader cannot judge whether the approach is robust, transferable, or prone to systematic errors.
- **Resolution test** In the full manuscript, specify the orientation grid size, interpolation order, error benchmarks against direct atomistic calculations, and the solvent model parameters with sensitivity analysis.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scope of validation
- **Claim pointer** The abstract claims the method "enables routine Monte Carlo simulation of medically relevant concentrations of interacting proteins."
- **Evidence pointer** Abstract only; no simulation results at high concentrations provided
- **Concern** The abstract does not report any simulation results at medically relevant concentrations, such as phase boundaries, clustering statistics, or aggregation kinetics. The claim of enabling such simulations is aspirational rather than demonstrated.
- **Why it matters** The stated motivation is to investigate high-concentration physical instabilities. Without demonstrating that the method can actually produce meaningful results in this regime, the practical utility of the approach remains unverified.
- **Resolution test** Include in the full manuscript at least one example simulation at a high protein concentration showing a relevant observable, such as a radial distribution function, cluster size distribution, or osmotic pressure, compared with experimental data where available.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract wording
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "systematic computational investigations of high-concentration physical instabilities" is vague and does not specify which instabilities are targeted beyond listing examples.
- **Required correction** Specify the exact phenomena to be investigated, such as liquid-liquid phase separation, reversible self-association, or irreversible aggregation, to set clear expectations.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Software availability statement
- **Evidence pointer** Abstract, last sentence
- **Issue** The abstract mentions the open-source software Free Energy and Advanced Sampling Simulation Toolkit but does not indicate the version, the specific module, or the input file requirements.
- **Required correction** Provide a version number, a citation to the software paper, and a brief description of the user interface or input format in the full manuscript.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Generalizability
- **Affected element** Model applicability
- **Evidence pointer** Abstract, third sentence
- **Issue** The method assumes rigid bodies with known fixed structures, which limits applicability to flexible or intrinsically disordered proteins. This limitation is not acknowledged in the abstract.
- **Required correction** Add a sentence in the abstract or introduction acknowledging this assumption and discussing potential extensions to flexible systems.

## Risk / unsupported claims
- The claim that the method "predicts experimentally measured radius of gyration and second osmotic virial coefficient data" is unsupported in the abstract due to the absence of quantitative results.
- The claim that the approach is "orders of magnitude more efficient than atomistic models" is stated without benchmark timing data or comparison protocols.
- The claim that the method "enables routine Monte Carlo simulation of medically relevant concentrations" is not demonstrated by any reported simulation output.
- The generalizability of the method to other proteins beyond the three tested systems is not assessable from the abstract.