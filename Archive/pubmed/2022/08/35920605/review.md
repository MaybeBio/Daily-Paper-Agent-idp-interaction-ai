## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors propose a parametrization strategy, CHARMM36m-SBFIX, using NBFIX to optimize Lennard-Jones parameters for solvent-exposed salt-bridge ion pairs against QM/MM PMF reference data. They report improved structural and thermodynamic descriptions of solvent-exposed salt bridges in tests on association constants, osmotic pressures, and protein simulations, but note poor transferability to solvent-excluded salt bridges in a protein-ligand binding free-energy calculation.
- **Visible evidence base** Abstract text only; no numerical data, methodological details, or figures provided
- **Missing materials affecting confidence** Full methods, all quantitative results, simulation protocols, system details, error estimates, and comparison benchmarks; without these, the validity of the parametrization and the reported outcomes cannot be independently assessed

## Reviewer
- **Overall assessment** The abstract presents a conceptually relevant and practically motivated approach to a well-known limitation of non-polarizable force fields. The strategy of using QM/MM PMFs to derive NBFIX parameters is reasonable and aligns with established practices in the field. However, the abstract provides insufficient quantitative detail to evaluate the robustness of the parametrization, the statistical significance of the improvements, or the generality of the conclusions. The reported failure for solvent-excluded salt bridges is an important caveat, but its treatment in the abstract is too brief to judge whether the conclusion is well supported.
- **Who would be interested in the results, and why** Researchers in biomolecular simulation, particularly those working on force field development, protein electrostatics, and the modeling of ionic interactions in aqueous and heterogeneous environments. The work is also relevant to computational chemists studying intrinsically disordered proteins and to those interested in the limits of transferability of pairwise additive potentials.
- **Major strengths** The problem addressed is of high practical importance. The use of QM/MM PMFs as a reference for parameter optimization is a sound and defensible approach. The inclusion of multiple test systems, including folded and disordered proteins, adds breadth. The explicit acknowledgment of the transferability limitation for solvent-excluded salt bridges is a candid and scientifically valuable observation.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide any quantitative results, such as association constants, osmotic pressure values, or binding free energies, nor does it describe the statistical treatment or error analysis. Without these, the claimed improvements cannot be verified. The method for optimizing LJ parameters is not described in sufficient detail to assess reproducibility.
- **Assessment against Nature-style criteria** 
  - Originality: The approach is not entirely novel, as NBFIX and QM/MM-based parameter optimization are known techniques, but the specific application to solvent-exposed salt bridges with a systematic test across multiple systems adds some originality.
  - Scientific importance: The topic is important for the accuracy of biomolecular simulations, but the abstract does not demonstrate a breakthrough or a broadly applicable solution.
  - Interdisciplinary readership: The work is primarily of interest to computational chemists and biophysicists; the abstract is not framed to attract a broader audience.
  - Technical soundness: Cannot be assessed from the abstract alone; the lack of quantitative evidence is a major limitation.
  - Readability for nonspecialists: The abstract is reasonably clear but uses field-specific terminology without sufficient context for a general scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract suggests a potentially useful contribution, but the absence of quantitative results and methodological detail prevents a supportive recommendation. A revised version with full data and analysis would be needed to evaluate the claims properly.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The abstract claims that CHARMM36m-SBFIX improves the description of solvent-exposed salt-bridge interactions, both structurally and thermodynamically.
- **Evidence pointer** Abstract text; location not provided
- **Concern** The claim of improvement is made without any numerical data. No association constants, osmotic pressure values, or structural metrics are reported. The magnitude of the improvement, the statistical significance, and the comparison to experimental or reference values are all absent.
- **Why it matters** A central claim of the work is that the new parameters improve accuracy. Without quantitative evidence, the reader cannot judge whether the improvement is meaningful or within error. This is essential for establishing the validity of the parametrization.
- **Resolution test** Provide quantitative results for at least one test system, including values from CHARMM36m-SBFIX, the base force field, and experimental or QM/MM reference data, with appropriate error estimates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency
- **Claim pointer** The abstract states that Lennard-Jones parameters are optimized to match reference QM/MM PMFs through the NBFIX feature.
- **Evidence pointer** Abstract text; location not provided
- **Concern** The optimization procedure is not described. Details such as the number of ion pairs considered, the range of distances sampled, the fitting algorithm, the treatment of uncertainties in the PMFs, and the criteria for convergence are missing. Without this information, the parametrization cannot be reproduced or critically evaluated.
- **Why it matters** Reproducibility is a fundamental requirement for any parametrization study. The lack of methodological detail prevents other researchers from applying or testing the approach.
- **Resolution test** Include a full description of the optimization protocol, including the functional form, fitting targets, and validation steps, in the main text or supplementary materials.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The abstract concludes that modeling salt-bridge interactions with a single universal set of LJ parameters remains a daunting challenge, based on the poor transferability to solvent-excluded salt bridges.
- **Evidence pointer** Abstract text; location not provided
- **Concern** The conclusion about transferability is based on a single protein-ligand complex. The abstract does not specify the system, the nature of the salt bridge, or the magnitude of the discrepancy from the experimental value. A single example may not be sufficient to support a general conclusion about the limits of transferability.
- **Why it matters** The conclusion has implications for the broader use of the parameters. If the failure is specific to a particular system or type of interaction, the conclusion may be overstated.
- **Resolution test** Provide details of the protein-ligand system, the experimental binding free energy, and the calculated value. If possible, include additional test cases with solvent-excluded salt bridges to strengthen the generalizability claim.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract text; location not provided
- **Issue** The term "nonbonded FIX, or NBFIX" is introduced without a brief explanation of what NBFIX does or why it is suitable for this purpose.
- **Required correction** Add a short parenthetical explanation, such as "a feature that allows specific pairwise Lennard-Jones parameters to be adjusted independently of the rest of the force field."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Test systems
- **Evidence pointer** Abstract text; location not provided
- **Issue** The abstract mentions simulations of "both folded and intrinsically disordered proteins" but does not specify which proteins or what properties were evaluated.
- **Required correction** Name the proteins and describe the key observables used to assess the performance of the force field.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Abstract structure
- **Evidence pointer** Abstract text; location not provided
- **Issue** The abstract is dense and mixes methodological description with results and conclusions in a single paragraph, which reduces readability.
- **Required correction** Consider restructuring the abstract into distinct sections for background, methods, results, and conclusions, as is common in the target journal.

## Risk / unsupported claims
- The claim that CHARMM36m-SBFIX improves structural and thermodynamic descriptions of solvent-exposed salt bridges is unsupported by quantitative data in the abstract.
- The claim that the parameters are not transferable to solvent-excluded salt bridges is based on a single unspecified example and is therefore not fully supported.
- The general conclusion that a universal set of LJ parameters for salt bridges is a daunting challenge is an interpretation that extends beyond the evidence presented in the abstract.