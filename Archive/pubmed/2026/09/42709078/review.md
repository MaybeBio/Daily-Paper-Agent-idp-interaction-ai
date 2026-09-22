## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no methods, figures, or data tables were available for evaluation
- **Shared manuscript claim summary** The authors report that alpha-synuclein (alphaSyn) membrane binding is jointly regulated by membrane phase, charge, and curvature. Under zwitterionic conditions, alphaSyn preferentially binds highly curved gel-phase membranes via curvature-dependent packing defects from faceted vesicle morphologies. Anionic lipids enhance binding in liquid-phase membranes but attenuate curvature-dependent partitioning in gel-phase membranes. FRAP and simulations indicate that gel-phase membranes and anionic lipids promote kinetically stabilized states, and that curvature-induced defect formation is amplified in gel-phase membranes but largely charge-insensitive.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary materials provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, experimental protocols, simulation parameters, statistical analyses, and raw data

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting and integrative study of how membrane phase, charge, and curvature jointly influence alphaSyn binding dynamics. The combination of experimental and simulation approaches is appropriate for the stated questions. However, the abstract alone provides insufficient detail to evaluate the rigor of the methods, the quality of the data, or the robustness of the conclusions. Several claims are stated without quantitative support, and the relationship between the simulation results and experimental observations is not fully articulated. The work may be of interest to the membrane biophysics and protein-misfolding communities, but the case is not fully established from the supplied material.
- **Who would be interested in the results, and why** Researchers studying alpha-synuclein membrane interactions in the context of Parkinson's disease and other synucleinopathies, as well as biophysicists interested in membrane curvature sensing, lipid phase behavior, and protein-lipid binding kinetics. The combined experimental and simulation approach may also appeal to computational biologists working on coarse-grained models of protein-membrane systems.
- **Major strengths** The study addresses a gap in the literature by examining the combined effects of membrane phase, charge, and curvature rather than treating these properties independently. The use of multiple complementary techniques (fluorescence microscopy, CD, FRAP, and coarse-grained simulations) is appropriate for probing both equilibrium and dynamic aspects of binding. The finding that anionic lipids differentially affect liquid-phase versus gel-phase membranes is a potentially novel and mechanistically interesting result.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative support for binding preferences), R1-M2 (mechanistic basis for charge effects), R1-M3 (kinetic stabilization claims), R1-M4 (simulation-experiment integration)
- **Assessment against Nature-style criteria**  
  - Originality: The integrative approach is somewhat novel, but the individual components (curvature sensing, phase-dependent binding, charge effects) are well established. The claim of cooperative interplay is potentially original but not fully substantiated from the abstract.  
  - Scientific importance: The topic is relevant to understanding alphaSyn physiology and pathology, but the abstract does not clearly articulate the broader implications beyond the specific system.  
  - Interdisciplinary readership: The work bridges biophysics, lipid chemistry, and neurobiology, which could appeal to a broad audience, but the abstract is written in a specialized manner that may limit accessibility.  
  - Technical soundness: Cannot be fully assessed from the abstract. The combination of methods is reasonable, but no details on controls, replicates, or statistical treatment are provided.  
  - Readability for nonspecialists: The abstract is dense and assumes familiarity with membrane biophysics terminology. Key concepts such as "faceted vesicle morphologies" and "packing defects" are not explained.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a plausible and potentially interesting story, but the lack of quantitative detail and the inability to assess methodological rigor preclude a supportive recommendation at this stage.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Quantitative support  
- **Claim pointer** "alphaSyn preferentially binds highly curved gel-phase membranes, driven by curvature-dependent enrichment of packing defects arising from faceted vesicle morphologies"  
- **Evidence pointer** Abstract only; no figures or tables provided  
- **Concern** The claim of preferential binding to highly curved gel-phase membranes is stated without any quantitative data. No binding affinities, enrichment ratios, or statistical comparisons are provided. The mechanistic link to "faceted vesicle morphologies" is asserted but not demonstrated.  
- **Why it matters** Without quantitative support, the reader cannot assess the magnitude of the effect or whether the preference is statistically significant. The mechanistic claim requires direct evidence of faceted morphologies and their correlation with binding.  
- **Resolution test** Provide quantitative binding data (e.g., binding isotherms, partition coefficients, or fluorescence intensity ratios) with appropriate statistical analysis. Include imaging or scattering data demonstrating faceted morphologies and their correlation with alphaSyn enrichment.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Mechanistic interpretation  
- **Claim pointer** "Incorporation of anionic lipids selectively enhances binding in liquid-phase membranes while attenuating curvature-dependent partitioning in gel-phase membranes"  
- **Evidence pointer** Abstract only; no figures or tables provided  
- **Concern** The differential effect of anionic lipids on liquid-phase versus gel-phase membranes is a central finding, but the mechanistic basis is not explained. Why would anionic lipids enhance binding in liquid-phase but attenuate curvature-dependent partitioning in gel-phase? The abstract does not offer a hypothesis or supporting data.  
- **Why it matters** This differential effect is the core novel claim of the study. Without a mechanistic explanation or supporting data, the finding remains descriptive and its significance is unclear.  
- **Resolution test** Provide experimental or simulation data that directly tests a mechanistic hypothesis (e.g., electrostatic interactions, lipid packing, or protein conformational changes). Include control experiments with different anionic lipid species or concentrations.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Kinetic claims  
- **Claim pointer** "gel-phase membranes and anionic lipids promoting kinetically stabilized states"  
- **Evidence pointer** Abstract mentions FRAP; no data provided  
- **Concern** The claim of kinetically stabilized states is based on FRAP measurements, but no recovery curves, mobile fractions, or exchange rate constants are provided. The term "kinetically stabilized" is vague and could refer to slower off-rates, reduced mobility, or other phenomena.  
- **Why it matters** The dynamic aspect of binding is a key differentiator of this study from prior work. Without quantitative FRAP data, the claim cannot be evaluated, and the distinction between thermodynamic and kinetic stabilization is not established.  
- **Resolution test** Provide FRAP recovery curves with fitted parameters (e.g., mobile fraction, half-time of recovery) for all conditions. Clearly define what "kinetically stabilized" means operationally and show that the effect is statistically significant.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Simulation-experiment integration  
- **Claim pointer** "Simulations show that curvature-induced defect formation is strongly amplified in gel-phase membranes but largely insensitive to charge"  
- **Evidence pointer** Abstract mentions coarse-grained molecular dynamics simulations; no simulation details or data provided  
- **Concern** The simulation results are stated as a single sentence without any details on the simulation system, force field, system size, or analysis methods. The claim that defect formation is "largely insensitive to charge" appears to contradict the experimental finding that anionic lipids attenuate curvature-dependent partitioning in gel-phase membranes. This potential discrepancy is not addressed.  
- **Why it matters** The simulations are presented as supporting evidence for the experimental findings, but the lack of detail and the apparent contradiction undermine their utility. The relationship between simulated defect formation and experimental binding behavior needs to be clarified.  
- **Resolution test** Provide simulation methods and convergence checks. Directly compare simulated defect densities with experimental binding data. Address the apparent discrepancy between charge insensitivity in simulations and charge-dependent effects in experiments.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Terminology clarity  
- **Affected element** "faceted vesicle morphologies"  
- **Evidence pointer** Abstract  
- **Issue** The term "faceted" is not defined and may be unfamiliar to some readers. It is unclear whether this refers to polyhedral shapes, buckled vesicles, or another morphology.  
- **Required correction** Define the term or provide a brief description of the observed morphologies.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Scope of conclusions  
- **Affected element** "cooperative interplay between membrane phase, curvature, and charge"  
- **Evidence pointer** Abstract  
- **Issue** The abstract concludes a "cooperative interplay" but does not specify whether the effects are additive, synergistic, or antagonistic. The term "cooperative" implies a specific relationship that is not demonstrated.  
- **Required correction** Clarify the nature of the interplay, or use more neutral language such as "combined effects" unless a specific interaction is demonstrated.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Generalizability  
- **Affected element** "highlight the importance of resolving both thermodynamic and kinetic contributions"  
- **Evidence pointer** Abstract  
- **Issue** The broader significance of the findings for understanding alphaSyn function or pathology is not articulated. The abstract does not state how these results might inform models of vesicle trafficking, synaptic function, or disease mechanisms.  
- **Required correction** Add a sentence in the discussion or conclusion that connects the findings to broader biological or pathological contexts.

## Risk / unsupported claims
- The claim that alphaSyn preferentially binds highly curved gel-phase membranes is unsupported without quantitative binding data.
- The mechanistic link between faceted vesicle morphologies and binding preference is asserted but not demonstrated.
- The differential effect of anionic lipids on liquid-phase versus gel-phase membranes is stated without mechanistic explanation or supporting data.
- The claim of kinetically stabilized states is not supported by quantitative FRAP data.
- The simulation results are presented without sufficient detail to evaluate their validity or relevance.
- The apparent contradiction between simulation results (charge insensitivity) and experimental findings (charge-dependent effects) is not addressed.
- The term "cooperative interplay" implies a specific relationship that is not demonstrated.