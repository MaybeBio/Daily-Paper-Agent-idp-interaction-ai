## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no figures, tables, methods, or supplementary materials were provided
- **Shared manuscript claim summary** The authors propose a method that incorporates NMR chemical shift-derived backbone dihedral terms into coarse-grained (CG) molecular dynamics simulations to improve the accuracy of interdomain contact predictions in mixed folded–disordered proteins. They apply this approach to a DNAJB6 construct containing a folded J-domain and a disordered GF linker, and report that the resulting ensembles reproduce NMR relaxation data and reveal linker motions resembling the closed state even in the nominally open state, driven by hydrophobic residues in GF. They further claim general applicability of the approach for retrieving physically relevant interdomain contacts.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary information were supplied
- **Missing materials affecting confidence** Full methods, simulation parameters, force field details, NMR data processing and analysis, validation metrics, comparison to experimental data, and any statistical or error analysis

## Reviewer
- **Overall assessment** The abstract presents a potentially valuable methodological advance for studying mixed folded–disordered proteins, a class of systems that is both biologically important and technically challenging. The core idea of using NMR chemical shift-derived dihedral restraints in CG simulations is conceptually sound and could address a recognized limitation of minimalistic CG models. However, the abstract provides insufficient detail to evaluate the technical implementation, the robustness of the results, or the strength of the claims. The central assertion that the method yields "accurate interdomain contact maps" is not supported by quantitative evidence in the supplied material. The claim regarding linker motions resembling the closed state is intriguing but lacks the necessary experimental and simulation detail to be assessed. Overall, the work appears promising but is currently not established from the provided evidence.
- **Who would be interested in the results, and why** Researchers in the fields of computational biophysics, intrinsically disordered proteins, NMR spectroscopy, and molecular chaperone biology would be interested. The methodological advance could benefit those developing or using CG simulations for dynamic protein systems, while the specific application to DNAJB6 is relevant to those studying protein aggregation and chaperone function.
- **Major strengths** The abstract identifies a clear and important problem, namely the limited accuracy of CG simulations for mixed folded–disordered proteins. The proposed solution, integrating NMR-derived dihedral terms into CG simulations, is a logical and potentially generalizable approach. The application to a biologically relevant system, DNAJB6, adds significance. The connection between simulation-derived ensembles and NMR relaxation data provides a basis for experimental validation.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide quantitative metrics for the claimed accuracy of interdomain contact maps, nor does it describe how the dihedral parameters were derived, tuned, or validated. The comparison to NMR relaxation data is mentioned but not substantiated with specific agreement measures. The generality of the approach is asserted without supporting evidence from additional systems.
- **Assessment against Nature-style criteria**  
  Originality: The idea of using NMR chemical shift-derived dihedral terms in CG simulations appears novel, though the abstract does not fully distinguish it from prior restraint-based approaches.  
  Scientific importance: The problem addressed is significant, and the potential to improve CG simulations for mixed folded–disordered proteins is of broad interest.  
  Interdisciplinary readership: The work bridges NMR spectroscopy, simulation methodology, and protein biophysics, which could appeal to a broad audience.  
  Technical soundness: Cannot be assessed from the abstract alone; the lack of methodological detail and quantitative validation is a major limitation.  
  Readability for nonspecialists: The abstract is generally clear, though some terms (e.g., "backbone dihedral terms," "secondary-structure propensities") assume familiarity with the field.
- **Recommendation posture** Currently not established from the provided evidence. The approach is promising, but the abstract does not provide sufficient detail or quantitative support to evaluate the core claims. A full manuscript with methods, validation, and comparison to experimental data would be required to assess whether the case is made.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The abstract claims that the method yields "accurate interdomain contact maps" and that the resulting ensembles are "in agreement with analysis of NMR relaxation data."  
- **Evidence pointer** Abstract text; location not provided  
- **Concern** The abstract provides no quantitative metrics, statistical measures, or comparison benchmarks to support the claim of accuracy. It is unclear how "accurate" is defined, what the reference is, and how the agreement with NMR relaxation data was quantified.  
- **Why it matters** Without quantitative validation, the central claim of the paper cannot be evaluated. The term "accurate" is subjective and requires a defined error metric or comparison to experimental or reference data.  
- **Resolution test** Provide quantitative measures of interdomain contact accuracy (e.g., comparison to experimental distance restraints, contact probability differences, or overlap with known structures) and statistical agreement with NMR relaxation data (e.g., correlation coefficients, reduced chi-squared values).

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Reproducibility  
- **Claim pointer** The abstract states that "backbone dihedral terms directly derived from NMR chemical shift data" were introduced into CG simulations, with residue-specific parameters tuned to match secondary-structure propensities.  
- **Evidence pointer** Abstract text; location not provided  
- **Concern** The abstract does not describe how the dihedral terms were derived, what functional form was used, how the tuning was performed, or how the parameters were validated. Without this information, the method cannot be reproduced or assessed for robustness.  
- **Why it matters** Reproducibility is a core requirement for any methodological advance. The lack of detail prevents other researchers from implementing or testing the approach.  
- **Resolution test** Provide a detailed description of the dihedral term derivation, the simulation protocol, the tuning procedure, and the validation of the parameters against independent data.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Generalizability  
- **Claim pointer** The abstract claims that "by expanding CG-simulations to allow them to capture both local and global structural properties, physically relevant interdomain contacts can be retrieved" and implies general applicability.  
- **Evidence pointer** Abstract text; location not provided  
- **Concern** The generality of the approach is asserted based on a single application to DNAJB6. No evidence is provided that the method would work for other mixed folded–disordered proteins with different sequence compositions, domain architectures, or disorder properties.  
- **Why it matters** A claim of general applicability requires demonstration across multiple systems or at least a clear rationale for why the approach would transfer. Without this, the claim is unsupported.  
- **Resolution test** Apply the method to at least one additional mixed folded–disordered protein system and show that the accuracy of interdomain contacts is maintained, or provide a detailed argument for why the approach is system-independent.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Abstract wording  
- **Evidence pointer** Abstract text; location not provided  
- **Issue** The phrase "motions that resemble those of the closed state" is vague and could be interpreted in multiple ways. It is unclear whether this refers to specific conformational states, dynamic timescales, or contact patterns.  
- **Required correction** Define what is meant by "resemble" and specify the criteria used to compare the open-state linker motions to the closed state.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Abstract content  
- **Evidence pointer** Abstract text; location not provided  
- **Issue** The abstract does not mention the simulation length, number of replicas, or convergence criteria, which are important for assessing the reliability of the conformational ensembles.  
- **Required correction** Include key simulation parameters, such as total simulation time, number of independent runs, and convergence assessment, in the abstract or main text.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Interpretation  
- **Affected element** Abstract claim  
- **Evidence pointer** Abstract text; location not provided  
- **Issue** The statement that hydrophobic residues in GF drive the closed-state-like motions is presented without supporting evidence or a mechanistic explanation.  
- **Required correction** Provide data or analysis that directly links hydrophobic residues to the observed motions, such as mutation studies, contact analysis, or free energy calculations.

## Risk / unsupported claims
- The claim of "accurate interdomain contact maps" is unsupported due to the absence of quantitative validation metrics.
- The claim of agreement with NMR relaxation data is unsupported without specific statistical measures.
- The claim of general applicability of the method is unsupported, as only a single system is presented.
- The mechanistic role of hydrophobic residues in GF in driving closed-state-like motions is asserted without direct evidence.
- The overall effectiveness of the method relative to existing CG approaches cannot be assessed without comparison to baseline simulations or alternative methods.