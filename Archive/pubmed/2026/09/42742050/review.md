## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as stated in the abstract; no methods, figures, tables, or supplementary material were provided
- **Shared manuscript claim summary** The authors reconstructed full-length, brain-derived alpha-synuclein fibril ensembles by combining a patient-derived cryo-EM core (residues 31-100) with disordered termini, sampled using the CALVADOS coarse-grained force field. They report that acidic C-terminal tails form transient contacts with solvent-exposed core motifs, intermittently shielding aggregation-prone ladders. Simulations with two validated aSyn-binding peptides (PSMalpha3 and LL-37) suggest a two-step recognition mechanism involving initial capture by the anionic fuzzy coat followed by engagement of hydrophobic/electrostatic hotspots on the structured core. The authors propose that selectivity for aggregated aSyn arises from a mesoscale interface combining a polyelectrolyte brush with recurrent core hotspots.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary information were provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, simulation details, force field parameters, validation data for peptide binding, control experiment details, and any statistical analyses

## Reviewer
- **Overall assessment** The abstract presents an interesting and potentially valuable computational framework for studying ligand recognition at amyloid surfaces. The conceptual advance of treating the full-length fibril with its disordered termini as a dynamic ensemble rather than a static core is timely and relevant. However, the evidence base available for this review is limited to the abstract, which prevents verification of the central claims. The mechanistic model proposed is plausible but rests on simulation results whose technical quality, convergence, and experimental validation cannot be assessed from the supplied material. The work is likely to interest the amyloid and computational biophysics communities, but the strength of the conclusions as stated exceeds what can be evaluated from the abstract alone.
- **Who would be interested in the results, and why** Researchers studying alpha-synuclein aggregation and Parkinson's disease pathogenesis, particularly those interested in molecular recognition at amyloid surfaces. Computational biophysicists working on coarse-grained simulations of intrinsically disordered proteins and fuzzy coat systems would also find the methodological framework relevant. Additionally, groups developing peptide-based diagnostics or therapeutics targeting aSyn aggregates may find the proposed two-step recognition mechanism informative for design strategies.
- **Major strengths** The abstract addresses a genuine gap in the field by moving beyond static core structures to consider the dynamic fuzzy coat in full-length fibril models. The proposed two-step recognition mechanism is mechanistically coherent and provides testable predictions. The use of experimentally validated binding peptides as probes is a sensible approach that connects simulation to known biology.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1 (simulation validation), R1-M2 (experimental support for mechanism), R1-M3 (generality of the model)
- **Assessment against Nature-style criteria** 
  - Originality: The concept of modeling full-length fibrils with disordered termini as dynamic ensembles is not entirely new, but the specific combination of a patient-derived cryo-EM core with CALVADOS sampling and the focus on fuzzy-coat control of peptide recognition appears to be a fresh contribution. The originality is moderate and potentially sufficient for a specialized journal, though the abstract alone does not demonstrate a transformative advance.
  - Scientific importance: The work addresses a relevant question in the amyloid field, namely how molecular partners recognize fibrillar surfaces. The proposed mechanism could have implications for understanding specificity in protein-protein interactions at amyloid interfaces. However, the importance is incremental rather than paradigm-shifting based on the abstract.
  - Interdisciplinary readership: The topic bridges structural biology, computational biophysics, and neurodegeneration research. The abstract is written in a way that is accessible to specialists in these areas, but the broader interdisciplinary appeal is limited by the technical nature of the methods.
  - Technical soundness: Cannot be assessed from the abstract alone. The reliance on coarse-grained simulations raises questions about force field accuracy, sampling convergence, and the sensitivity of conclusions to model parameters. These issues must be addressed in the full manuscript.
  - Readability for nonspecialists: The abstract is clearly written and the key concepts are explained adequately for a scientific audience. The terminology is appropriate for the target readership, though some terms (e.g., "fuzzy coat," "polyelectrolyte brush") may require familiarity with the field.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a plausible and interesting model, but the technical quality of the simulations and the strength of the experimental validation cannot be evaluated. A supportive posture would require the full manuscript to demonstrate robust simulation methodology, convergence, and appropriate validation against experimental data.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that CALVADOS coarse-grained simulations of full-length fibril ensembles reveal transient contacts between acidic C-terminal tails and solvent-exposed core motifs, and that these contacts intermittently shield aggregation-prone ladders.
- **Evidence pointer** Abstract only; no methods, figures, or tables provided
- **Concern** The central mechanistic claims rest entirely on coarse-grained simulations. The abstract provides no information on force field validation for this specific system, sampling convergence, the number of independent simulations, or the sensitivity of the observed contacts to model parameters. Coarse-grained models involve significant approximations, and the balance between electrostatic and hydrophobic interactions in the fuzzy coat is likely to be sensitive to the parameterization. Without evidence that the simulations have converged and that the observed contacts are robust to reasonable parameter variations, the mechanistic conclusions cannot be considered established.
- **Why it matters** The proposed model of fuzzy-coat control of peptide recognition depends on the reliability of the simulated ensemble. If the transient contacts are artifacts of the force field or insufficient sampling, the entire mechanistic framework collapses. The claim that aggregation-prone ladders are "intermittently shielded" is a specific structural statement that requires demonstration of statistical robustness.
- **Resolution test** Provide evidence of simulation convergence (e.g., block analysis, multiple independent runs), validation of CALVADOS for disordered termini in fibrillar contexts, and a sensitivity analysis showing that the key contacts and shielding behavior are robust to reasonable changes in force field parameters or system setup.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental support
- **Claim pointer** The authors claim that simulations with PSMalpha3 and LL-37 show a two-step recognition process, and that PSMalpha3 variants and LL-37 controls support the importance of positive charge, peptide flexibility, and full-length fibril architecture for persistent binding.
- **Evidence pointer** Abstract only; no experimental data, figures, or tables provided
- **Concern** The abstract states that "PSMalpha3 variants and LL-37 controls support" the proposed mechanism, implying experimental validation. However, no experimental results are presented in the abstract, and the nature of these experiments (binding assays, mutagenesis, competition experiments) is not described. The claim that "full-length fibril architecture" is required for persistent binding is a strong statement that requires comparison with truncated or core-only constructs, which is not described.
- **Why it matters** The two-step mechanism and the role of the fuzzy coat are the central claims of the work. If the experimental support is limited or indirect, the conclusions are overreaching. The distinction between the fuzzy coat acting as a general electrostatic capture mechanism versus a specific recognition element is critical for the proposed model, and this distinction requires experimental discrimination.
- **Resolution test** Provide detailed descriptions of the experimental systems, including binding assays with appropriate controls, quantitative measurements of binding affinity or kinetics, and direct comparisons between full-length fibrils and constructs lacking the fuzzy coat. Show that the experimental results are quantitatively consistent with the simulation predictions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generality and scope
- **Claim pointer** The authors claim that "these results establish full-length, brain-derived fibril ensembles as a practical framework for understanding ligand recognition at amyloid surfaces."
- **Evidence pointer** Abstract only; no comparative data with other amyloid systems
- **Concern** The abstract presents results for a single fibril type (aSyn Lewy-fold) and two peptides. The claim that this establishes a general framework for amyloid surfaces is a significant extrapolation. Amyloid fibrils from different proteins have different core structures, different fuzzy coat compositions, and different charge distributions. The generality of the proposed mechanism across amyloid systems is not demonstrated.
- **Why it matters** The broader significance of the work depends on whether the proposed mechanism is specific to aSyn or generalizable. If the framework is only applicable to aSyn, the impact is more limited. The claim of establishing a "practical framework" implies transferability that is not supported by the evidence described.
- **Resolution test** Either temper the claim to be specific to aSyn fibrils, or provide additional simulations or experiments with other amyloid systems demonstrating that the proposed mechanism operates more broadly.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract
- **Issue** The term "fuzzy-coat control" is used in the title and throughout the abstract, but the precise meaning of "control" is not defined. Does it imply that the fuzzy coat actively regulates recognition, or merely that it modulates access to the core?
- **Required correction** Define the intended meaning of "control" in the context of the proposed mechanism, or use a more neutral term such as "modulation" or "influence."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Simulation details
- **Evidence pointer** Abstract
- **Issue** The abstract mentions "recurrent, transient contacts" and "intermittently shielded" but provides no quantitative information about the frequency, duration, or occupancy of these contacts.
- **Required correction** Include quantitative measures of contact lifetimes, occupancies, or free energy estimates in the abstract or indicate where such data are presented in the full manuscript.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Mechanistic model
- **Evidence pointer** Abstract
- **Issue** The two-step mechanism is described as "retained by the anionic fuzzy coat" followed by "engagement of exposed hydrophobic/electrostatic hotspots." The distinction between these two steps is not fully clear, as electrostatic interactions could contribute to both steps.
- **Required correction** Clarify the molecular determinants that distinguish the capture step from the engagement step, and specify whether the two steps are kinetically separable or represent a continuum of interactions.

## Risk / unsupported claims
- The claim that aggregation-prone ladders are "intermittently shielded rather than permanently buried" is unsupported without evidence of simulation convergence and ensemble statistics.
- The claim that "full-length fibril architecture" is required for persistent peptide binding is unsupported without direct comparisons to truncated constructs.
- The claim that the results "establish full-length, brain-derived fibril ensembles as a practical framework for understanding ligand recognition at amyloid surfaces" is an overgeneralization from a single fibril type and two peptides.
- The mechanistic model of two-step recognition is plausible but cannot be evaluated for technical soundness without access to simulation details and validation data.
- Any quantitative claims about contact frequencies, binding affinities, or kinetic parameters are not assessable from the abstract.