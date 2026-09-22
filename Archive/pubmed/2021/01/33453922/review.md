## Review setup
- **Input scope** Full manuscript text (abstract, introduction, model description, simulation methodology, and acknowledgments)
- **Assessment boundary** Technical and methodological assessment of the described coarse-grained modeling framework and simulation protocol for studying protein LLPS
- **Shared manuscript claim summary** The authors present a sequence-specific, single-bead-per-amino-acid coarse-grained model (HPS) combined with coexistence sampling to study protein liquid-liquid phase separation, and provide practical guidance for implementing this approach in HOOMD-Blue.
- **Visible evidence base** Abstract, Introduction, HPS model description, Simulation strategy sections (including subsections on slab preparation, density profiles, and phase diagram construction), and Acknowledgment
- **Missing materials affecting confidence** Figures referenced (Figs. 1-5) are not provided; simulation scripts and code implementations mentioned as available are not included; no quantitative results or validation data are presented in the text

## Reviewer
- **Overall assessment** This manuscript is a methods-focused book chapter that describes a coarse-grained modeling framework for studying protein LLPS. The authors provide a clear conceptual overview of their HPS model and the coexistence simulation strategy, along with practical implementation details for HOOMD-Blue. The writing is accessible and the methodological logic is sound. However, the absence of figures, quantitative validation data, and direct comparisons with experimental results limits the ability to fully assess the robustness and accuracy of the described approach. The chapter serves as a useful tutorial for practitioners but does not present new scientific findings or benchmark validations that would establish the model's predictive power beyond what has been previously reported.

- **Who would be interested in the results, and why** Computational biophysicists and molecular simulation practitioners studying protein phase separation, particularly those working with coarse-grained models of intrinsically disordered proteins. Researchers interested in implementing LLPS simulations in HOOMD-Blue would find the practical guidance valuable. Experimental biologists studying membraneless organelles may also benefit from understanding the computational approaches available for complementing their experimental observations.

- **Major strengths** The manuscript provides a clear and accessible description of a practical coarse-grained simulation approach for studying protein LLPS. The step-by-step guidance on setting up coexistence simulations, including practical considerations such as system size selection and convergence assessment, is valuable for practitioners. The discussion of potential pitfalls (e.g., slab drift, critical temperature estimation) demonstrates practical experience. The authors are transparent about the limitations of their approach and provide reasonable justifications for methodological choices.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that the HPS model with coexistence sampling can reliably produce thermodynamic phase diagrams for sequence-specific protein LLPS.
  - **Evidence pointer** Section "Generating phase diagrams", location not provided
  - **Concern** The manuscript does not present any quantitative results, validation data, or comparison with experimental phase diagrams. While the authors reference their previous work, the current chapter provides no evidence that the described methodology produces accurate or converged phase boundaries for any specific protein system. The critical temperature estimation procedure (Eq. 5) is stated to be asymptotically valid only near Tc, but no guidance is given on how to assess whether the simulated temperature range satisfies this condition.
  - **Why it matters** Without validation data or convergence metrics, readers cannot assess whether the described protocol will yield reliable results for their system of interest. The claim that this method "can allow one to simulate biomolecular LLPS using general-purpose hardware" requires demonstration of accuracy and reproducibility.
  - **Resolution test** Provide representative phase diagrams for at least one protein system with comparison to experimental data or previously published results. Include convergence metrics (e.g., block average analysis showing plateau) and sensitivity analysis for system size and simulation length.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors state that the coexistence method with a pre-formed slab configuration is efficient and that 5 μs simulations are sufficient for convergence.
  - **Evidence pointer** Section "Obtaining density profiles", location not provided
  - **Concern** The manuscript asserts that 5 μs simulation time is sufficient based on "stopping seeing any significant deviations in the density profile when comparing 1 μs block averages." However, no quantitative criteria for "significant deviations" are provided, and the authors acknowledge that this choice is "system-specific." The claim that the pre-formed slab approach saves time compared to spontaneous phase separation is plausible but not quantified. The benchmark of 36 hours on a GTX1080 for a 100-chain system is useful but does not address whether this is representative across different protein sequences and conditions.
  - **Why it matters** Practitioners need clear convergence criteria and expected computational costs to design their own simulations. Without quantitative guidance, users may either under-sample (producing unreliable phase boundaries) or over-sample (wasting computational resources).
  - **Resolution test** Provide explicit convergence criteria (e.g., tolerance thresholds for density profile fluctuations) and demonstrate convergence for multiple protein systems with different sequence properties. Report scaling of computational cost with system size and protein length.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Reproducibility
  - **Claim pointer** The authors state that they provide implementations of the coarse-grained potentials in HOOMD-Blue and associated Python scripts.
  - **Evidence pointer** Abstract and Introduction, location not provided
  - **Concern** While the authors mention providing scripts and implementations, no repository link, version information, or usage examples are included in the manuscript text. The referenced azplugins component is mentioned with a URL, but the main simulation scripts are not described in sufficient detail for reproduction.
  - **Why it matters** Reproducibility is a core requirement for methods papers. Without access to the actual scripts or detailed input file examples, readers cannot implement the described protocol without significant reverse-engineering.
  - **Resolution test** Include a dedicated section with repository access information, script usage examples, and input file templates. Provide version numbers for all software dependencies.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Model parameterization
  - **Evidence pointer** Section "HPS model", location not provided
  - **Issue** The description of how σ (amino acid diameter) is computed from van der Waals volume is brief. The mapping procedure and any adjustments made for consistency with the Lennard-Jones potential are not detailed.
  - **Required correction** Provide a more detailed description of the σ calculation, including the specific van der Waals volume data source and the conversion formula used.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Temperature dependence
  - **Evidence pointer** Section "Obtaining density profiles", location not provided
  - **Issue** The authors mention an extension of the model to capture thermoresponsive behavior with temperature-dependent nonbonded interactions but do not describe this extension or its validation.
  - **Required correction** Either provide a brief description of the temperature-dependent extension or clearly state that it is beyond the scope of this chapter and reference the relevant publication.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Practical guidance
  - **Affected element** System size selection
  - **Evidence pointer** Section "Preparing an initial slab configuration", location not provided
  - **Issue** The authors mention that system size selection is a balance between accuracy and computational cost but provide no quantitative guidance on how to choose the number of chains or box dimensions for a new system.
  - **Required correction** Provide a table or heuristic for initial system size selection based on protein length and expected phase behavior, with examples from their previous work.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Statistical analysis
  - **Affected element** Error estimation
  - **Evidence pointer** Section "Obtaining density profiles", location not provided
  - **Issue** The use of block averaging for error estimation is mentioned but no details are given on block size selection or how to determine when the block average has converged.
  - **Required correction** Provide specific guidance on block size selection (e.g., relative to autocorrelation time) and criteria for determining convergence of block averages.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Lack of validation data demonstrating the accuracy of the described methodology
  - R1-M2: Insufficient quantitative convergence criteria for simulation length and system size
  - R1-M3: Incomplete reproducibility information for the provided scripts and implementations

## Risk / unsupported claims
- The claim that the HPS model "can allow one to simulate biomolecular LLPS using general-purpose hardware" is not quantitatively supported in this chapter, as no benchmark results or hardware requirements are provided.
- The statement that 100 FUS LC chains are "sufficient to achieve reasonable accuracy" is presented without statistical justification or comparison to experimental data in this chapter.
- The assertion that the coexistence method with pre-formed slabs is more efficient than spontaneous phase separation is plausible but not demonstrated with comparative data.
- The claim that the model can capture "sequence-specific characteristics contributing to the phase separation propensity" is not validated with specific examples in this chapter.
- The extension to temperature-dependent interactions for capturing thermoresponsive behavior is mentioned but not described or validated, making this claim unassessable from the provided material.