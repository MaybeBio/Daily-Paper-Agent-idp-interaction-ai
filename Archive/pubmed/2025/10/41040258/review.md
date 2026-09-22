## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) and metadata
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by presented evidence
- **Shared manuscript claim summary** The authors use enhanced sampling all-atom MD simulations to characterize binding modes of two small molecules (YX-I-1, an aggregation inhibitor, and YX-A-1, an aggregation accelerator) to monomeric WT and S20G hIAPP. They report differential binding affinities, conformational changes, and propose that buried ligand moieties confer monomer binding affinity while solvent-exposed moieties modulate aggregation kinetics.
- **Visible evidence base** Simulation trajectories, convergence analyses, chemical shift comparisons, contact analyses, circuit topology clustering, KD estimates
- **Missing materials affecting confidence** Supplementary figures and tables referenced but not provided; experimental data from prior work referenced but not shown; no experimental validation of new predictions

## Reviewer
- **Overall assessment** This manuscript presents a computationally intensive and methodologically sophisticated analysis of small molecule binding to monomeric hIAPP. The work addresses an important gap in understanding how small molecules modulate hIAPP aggregation. The central hypothesis regarding distinct roles of buried versus solvent-exposed ligand moieties is intriguing and potentially valuable for drug design. However, several technical concerns and interpretive gaps need to be addressed before the conclusions are fully supported.
- **Who would be interested in the results, and why** Researchers in the fields of amyloid biology, intrinsically disordered proteins, computational drug discovery, and Type II Diabetes therapeutics. The work provides a framework for understanding ligand interactions with disordered protein monomers, which is relevant beyond hIAPP.
- **Major strengths** 1) Use of enhanced sampling methods appropriate for disordered proteins; 2) Validation of the apo WT ensemble against experimental NMR data; 3) Systematic comparison of two ligands with opposite effects on aggregation; 4) Novel application of circuit topology analysis to ligand binding; 5) Clear articulation of a testable hypothesis linking molecular features to kinetic effects.
- **Major Concerns** See items below.
- **Minor Comments** See items below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** **Originality** Moderate to high. The application of circuit topology to ligand binding is novel, and the specific hypothesis about buried versus exposed moieties is original. However, the general concept of IDP ligand binding via dynamic, multi-site interactions has been previously described. **Scientific importance** High. Understanding how small molecules modulate hIAPP aggregation has direct therapeutic relevance for T2D. The work provides a mechanistic framework that could guide drug design. **Interdisciplinary readership** Moderate. The work bridges computational chemistry, biophysics, and diabetes research. The writing is accessible but assumes familiarity with MD simulation methodology. **Technical soundness** Generally sound but with concerns about force field accuracy, convergence, and interpretation of binding affinities (see Major Concerns). **Readability for nonspecialists** The abstract and introduction are clear. The results section is dense and may be challenging for non-specialists, particularly the circuit topology analysis. Figures are referenced but not available for assessment.
- **Recommendation posture** Supportive if technical concerns are resolved

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The simulated KD values (2.35 mM for YX-I-1, 5.00 mM for YX-A-1) are presented as quantitative estimates of binding affinity.
- **Evidence pointer** Table 3, Results section "Comparing binding modes of YX-I-1 and YX-A-1 to WT and S20G hIAPP"
- **Concern** The KD values are derived from bound fractions in simulations with 6.25 mM concentrations of both protein and ligand. At these concentrations, the system is far from dilute conditions, and the calculated KD values may not be thermodynamically meaningful. The authors acknowledge this in the text but still present these as quantitative estimates. More importantly, the simulated KD for YX-I-1 binding to S20G hIAPP is similar to WT, which contradicts experimental data showing much weaker binding to S20G. The authors attribute this to force field overestimation, but this discrepancy undermines confidence in the quantitative claims.
- **Why it matters** The quantitative binding affinities are used to support the central claim that YX-I-1 binds more strongly to WT hIAPP. If the simulated affinities are unreliable, the quantitative comparison between ligands and between protein variants is weakened.
- **Resolution test** Provide a more rigorous treatment of binding affinity, such as potential of mean force calculations, or clearly frame the bound fractions as qualitative indicators of relative binding propensity rather than quantitative KD values. Address the discrepancy with experimental data more thoroughly, possibly with additional simulations or analysis.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the inhibitor exhibits substantially higher affinity for monomeric wild-type hIAPP than the accelerator, consistent with previously reported biophysical experiments."
- **Evidence pointer** Table 3, Results section "Comparing binding modes of YX-I-1 and YX-A-1 to WT and S20G hIAPP"
- **Concern** The bound fractions for YX-I-1 (71.6%) and YX-A-1 (53.2%) to WT hIAPP differ by less than 20 percentage points. The corresponding KD values differ by approximately 2-fold. Whether this constitutes "substantially higher affinity" is debatable, especially given the large statistical uncertainties that would be expected from such simulations. The authors do not report confidence intervals or statistical significance tests for these differences.
- **Why it matters** The claim of substantially higher affinity is a key finding that supports the overall narrative. If the difference is not statistically robust, the interpretation is weakened.
- **Resolution test** Report statistical uncertainties on bound fractions and KD values. Perform additional independent simulations or bootstrapping analysis to establish whether the observed differences are significant.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors hypothesize that "buried ligand moieties confer hIAPP monomer binding affinity while solvent-exposed ligand moieties modulate the kinetics of intermolecular association."
- **Evidence pointer** Results section "YX-I-1 and YX-A-1 binding modes leave specific ligand moieties exposed to the solvent", Discussion
- **Concern** This is the central hypothesis of the paper, but it is presented as a speculation based on the observation that certain moieties are solvent-exposed. No direct evidence links the solvent-exposed moieties to effects on aggregation kinetics. The authors cite one experimental study (Taylor et al.) showing that removal of certain groups abolishes activity, but this is a single data point and does not directly test the proposed mechanism.
- **Why it matters** The hypothesis is the main conceptual contribution of the paper. Without direct testing or at least a more detailed mechanistic argument, it remains speculative.
- **Resolution test** Provide additional analysis linking specific solvent-exposed moieties to potential intermolecular interactions, or propose specific, testable predictions that could distinguish this hypothesis from alternatives.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "in all ligand-bound ensembles, distinct fragments of YX-I-1 and YX-A-1 are sequestered from solvent upon binding while other fragments remain solvent-exposed."
- **Evidence pointer** Results section "YX-I-1 and YX-A-1 binding modes leave specific ligand moieties exposed to the solvent", Figure 4
- **Concern** The analysis of solvent exposure is based on a 5 Å cutoff for protein-ligand contacts. This is a somewhat arbitrary definition of "buried" versus "exposed." The authors do not report the distribution of solvent accessible surface area (SASA) for individual ligand atoms, which would be a more rigorous measure. Additionally, the analysis appears to be performed on the ensemble as a whole, but it is unclear whether individual binding modes consistently show the same pattern of buried versus exposed moieties.
- **Why it matters** The claim about consistent burial and exposure patterns is central to the proposed hypothesis. If the pattern is not consistent across binding modes, the hypothesis is weakened.
- **Resolution test** Report SASA calculations for ligand atoms in bound versus unbound states. Show that the burial/exposure pattern is consistent across individual binding modes, not just in the ensemble average.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section "Simulation Methods"
- **Evidence pointer** Methods section
- **Issue** The description of the equilibration protocol is somewhat unclear. The text states "structures were equilibrated for at least 20 ns at 300 K in the NPT ensemble" but does not specify how many structures were used for the production runs or how the 20 starting structures were selected from the equilibration.
- **Required correction** Clarify the number of independent simulations and the selection criteria for starting structures.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section "Simulation Methods"
- **Evidence pointer** Methods section
- **Issue** The ligand parameterization is described as using GAFF1 with AM1-BCC charges, but the specific charge calculation method is not stated. This is important for reproducibility.
- **Required correction** Specify the charge calculation method (e.g., AM1-BCC, RESP) and the software used.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results section "Comparing conformational ensembles of wild-type and S20G hIAPP"
- **Evidence pointer** Results section, Figure 1
- **Issue** The authors report increased β-sheet populations in S20G hIAPP but do not discuss whether these β-sheets are in regions known to be amyloidogenic or whether they represent off-pathway conformations.
- **Required correction** Provide additional analysis or discussion of the location and nature of the increased β-sheet populations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The authors mention that simulations of oligomer assembly will be the subject of future investigations, but do not discuss how the current findings might inform those studies.
- **Required correction** Add a brief discussion of how the monomer binding modes might relate to oligomer formation.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure 5 and Figure 6
- **Evidence pointer** Results section "Visualizing Multisite Binding Modes of YX-I-1 and YX-A-1"
- **Issue** The figures are described as showing representative structures, but the selection criteria for these structures are not described.
- **Required correction** Describe how representative structures were selected (e.g., most populated cluster centroid, lowest energy structure).

## Risk / unsupported claims
- The claim that solvent-exposed moieties of YX-I-1 and YX-A-1 modulate aggregation kinetics is speculative and not directly supported by the simulation data presented.
- The quantitative KD values derived from simulations are presented with more confidence than is warranted given the known limitations of force field-based binding affinity calculations for IDPs.
- The statement that the simulated binding affinity of YX-I-1 to S20G hIAPP is "comparable" to WT, despite experimental evidence to the contrary, is acknowledged as a limitation but not adequately resolved.
- The claim that the apo WT ensemble is in "excellent agreement" with NMR data is based on chemical shift comparisons, but the authors note a 10-15% underestimation of helical propensity in the disulfide-constrained region, which may be significant for the binding analysis.