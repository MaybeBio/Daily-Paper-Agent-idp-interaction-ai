## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, acknowledgments)
- **Assessment boundary** Scientific claims, methodological adequacy, and interpretive validity as presented in the provided text
- **Shared manuscript claim summary** The authors report the first molecular modeling study of protein polyphosphorylation, using replica exchange molecular dynamics (REMD) simulations to show that covalent attachment of a polyphosphate chain to lysine residues in the disordered charged linker of human endoplasmin (GRP-94) alters the conformational ensemble, loop flexibility, and interactions with the globular N-terminal domain, with potential implications for HSP90 chaperone function.
- **Visible evidence base** Methods section (force field, counterion choice, simulation protocols, homology modeling), Results section (Figures 2–5 referenced), Discussion section (interpretive claims)
- **Missing materials affecting confidence** Figures and tables are referenced but not provided; no simulation convergence metrics, no error estimates, no statistical analysis of ensemble differences, no raw data or trajectory analysis details, no validation of the polyphosphorylated lysine parameterization

## Reviewer
- **Overall assessment** This manuscript presents a plausible and potentially useful computational exploration of a poorly understood post-translational modification. The choice of system (HSP90 charged linker) is biologically motivated, and the use of REMD is appropriate for sampling disordered conformations. However, the evidence as presented is insufficient to support several key claims. The absence of figures, quantitative ensemble comparisons, and convergence assessments prevents verification of the central conclusions. The manuscript reads more as a preliminary computational report than a fully established study.
- **Who would be interested in the results, and why** Researchers studying post-translational modifications, particularly polyphosphorylation; computational biophysicists interested in disordered protein regions and polyelectrolyte interactions; and the HSP90 chaperone community, given the proposed link between the charged linker and client protein interactions.
- **Major strengths** The study addresses a novel and under-explored modification with potential biological significance. The use of REMD with explicit water is methodologically appropriate for disordered systems. The authors identify a real technical issue (sodium counterion crystallization) and propose a reasonable alternative. The comparison between bacterial and human HSP90 provides a useful contrast.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (parameterization validation), R1-M2 (convergence and sampling), R1-M3 (quantitative ensemble comparison), R1-M4 (counterion choice justification)
- **Assessment against Nature-style criteria** Originality: high, as this is the first modeling study of polyphosphorylation. Scientific importance: moderate, as the biological relevance of polyphosphorylation remains speculative. Interdisciplinary readership: limited, as the work is primarily of interest to computational biophysicists and HSP90 researchers. Technical soundness: not established from the provided evidence, due to missing validation and quantitative analysis. Readability for nonspecialists: adequate, though the Discussion contains speculative extrapolations that are not clearly separated from findings.
- **Recommendation posture** Currently not established from the provided evidence. The study has potential, but the central claims require substantial additional analysis and validation before the case is convincing.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Polyphosphorylated lysine was parameterized using CGenFF service"
- **Evidence pointer** Methods section, location not provided
- **Concern** The parameterization of polyphosphorylated lysine is described in a single sentence with no validation. CGenFF parameters for non-standard residues require verification against quantum mechanical reference data or experimental observables. No partial charges, bond parameters, or validation results are provided.
- **Why it matters** The entire study depends on the accuracy of these parameters. If the polyphosphate chain or its linkage to lysine is misparameterized, all subsequent conclusions about conformational changes are unreliable.
- **Resolution test** Provide validation of the CGenFF parameters, such as comparison of optimized geometries, electrostatic potentials, or torsional profiles against ab initio calculations. Alternatively, demonstrate that the simulation results are robust to reasonable parameter variations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Replica exchange molecular dynamics simulations" were used to study conformational ensembles
- **Evidence pointer** Methods section, location not provided
- **Concern** No convergence metrics are reported. For REMD simulations of disordered regions, it is essential to demonstrate that replica exchange rates are adequate, that the temperature range is sufficient, and that the conformational ensembles are converged. Simulation lengths of 50–65 ns per replica may be short for converged sampling of a disordered loop.
- **Why it matters** Without convergence evidence, the observed differences between native and polyphosphorylated forms could be sampling artifacts rather than genuine physical effects.
- **Resolution test** Report replica exchange acceptance rates, effective exchange probabilities, and convergence of ensemble properties (e.g., radius of gyration, secondary structure content) over time. Consider extending simulations or using multiple independent runs to confirm reproducibility.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** "A significant difference between conformational ensembles of this disordered loop in native and polyphosphorylated forms was observed"
- **Evidence pointer** Results section, Figures 4 and 5, location not provided
- **Concern** The claim of significant differences is not supported by quantitative analysis. The text describes percentages (e.g., 33% vs. 53–55% for contact distances) but provides no error bars, statistical tests, or measures of ensemble overlap. The figures are referenced but not available for inspection.
- **Why it matters** The central conclusion of the paper rests on this claim. Without statistical rigor, the observed differences may not be meaningful given the inherent variability of disordered ensembles.
- **Resolution test** Provide quantitative ensemble comparisons with uncertainty estimates, such as bootstrapped confidence intervals, Jensen-Shannon divergence between conformational distributions, or permutation tests. Include the actual figures with clear statistical annotations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "To avoid artificial crystallization of polyphosphate and counterions observed for sodium ions, methylammonium CH3NH3+ was used as a counterion"
- **Evidence pointer** Methods section, location not provided
- **Concern** The choice of methylammonium as a counterion is justified by a known artifact with sodium, but the physiological relevance of this choice is not discussed. Methylammonium is not a biologically abundant cation, and its use may alter electrostatic interactions in ways that affect the conclusions.
- **Why it matters** If the counterion choice significantly influences the conformational ensemble, the results may not reflect in vivo conditions where sodium and potassium dominate.
- **Resolution test** Justify the counterion choice with reference to physiological conditions, or perform control simulations with alternative cations (e.g., potassium) to demonstrate that the qualitative conclusions are robust.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section, simulation details
- **Evidence pointer** Methods section, location not provided
- **Issue** The number of replicas (60) and temperature range (300–380 K) are stated, but the temperature distribution and the rationale for this range are not explained.
- **Required correction** Provide the temperature spacing and justify the range with respect to the expected energy barriers and the stability of the protein.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Interpretive validity
- **Affected element** Discussion section, speculative claims
- **Evidence pointer** Discussion section, location not provided
- **Issue** The Discussion extrapolates to neurodegenerative diseases and client protein interactions without direct evidence from the simulations. These claims are presented as plausible hypotheses but are not clearly labeled as such.
- **Required correction** Clearly distinguish between simulation-derived findings and speculative implications. Consider moving disease-related discussion to a clearly marked "outlook" subsection.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section, homology modeling
- **Evidence pointer** Methods section, location not provided
- **Issue** The homology modeling procedure is described briefly. The choice of templates and the quality of the resulting models are not assessed.
- **Required correction** Report model quality metrics (e.g., QMEAN, GMQE scores) and describe how the disordered loop was constructed and validated.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section, Figure 2
- **Evidence pointer** Results section, Figure 2, location not provided
- **Issue** The radial distribution function and RMSF data for counterions are described qualitatively. No quantitative comparison between sodium and methylammonium cases is provided.
- **Required correction** Provide numerical values or statistical measures to support the claim that methylammonium yields realistic behavior.

## Risk / unsupported claims
- The claim that polyphosphorylation "might affect interaction of HSP90 with client proteins" is speculative and not directly supported by the simulation data.
- The claim that polyphosphorylation "might influence the behavior of the ATP-binding pocket lid" is based on proximity observations but lacks direct evidence of functional impact.
- The hypothesis linking polyphosphorylation to neurodegenerative diseases is unsupported by any data presented in this study.
- The statement that "our data unambiguously indicates the difference in the charged linker behavior" is overstated given the lack of statistical analysis and convergence assessment.
- The biological relevance of the methylammonium counterion choice is not established.