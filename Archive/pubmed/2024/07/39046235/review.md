## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) without supplementary material
- **Assessment boundary** Scientific claims, methodological soundness, and interpretive validity as presented in the main text; supplementary material referenced but not independently evaluated
- **Shared manuscript claim summary** The authors compare coarse-grained (Martini3, Sirah2) and all-atom (Amber99sb, Charmm36m) force fields for describing the structure and aggregation of alpha-synuclein, finding that Sirah2 with enhanced protein-water interactions and neutral termini is most suitable for studying protein-protein and protein-drug aggregation, while Martini3 fails to capture aggregation behavior.
- **Visible evidence base** Main text figures (Figures 1-9), equations (1-17), and methodological descriptions; supplementary tables and figures referenced but not provided
- **Missing materials affecting confidence** Supplementary material (Tables S1-S2, Figures S1-S3), simulation input files, force field parameter files, raw trajectory data, convergence metrics, and experimental comparison datasets

## Reviewer
- **Overall assessment** This manuscript addresses a timely and practically important question: whether coarse-grained force fields, specifically Martini3 and Sirah2, can reliably describe both the conformational ensemble and aggregation behavior of alpha-synuclein. The comparative framework across multiple resolutions and the inclusion of enhanced sampling and umbrella sampling calculations are commendable. However, several technical concerns limit the strength of the conclusions. The claim that Sirah2 with enhanced protein-water interactions is "suitable" for aggregation studies rests on a single peptide system and a limited set of observables. The instability of the Martini3 fibril, while interesting, is not mechanistically dissected beyond referencing prior work on small peptides. The all-atom comparisons, while useful, are limited in sampling time and may not provide a robust reference. The manuscript would benefit from additional validation metrics, clearer convergence assessments, and a more nuanced discussion of the limitations of the conclusions drawn.
- **Who would be interested in the results, and why** Researchers in the molecular simulation community, particularly those working on intrinsically disordered proteins, coarse-grained force field development, and protein aggregation. The practical recommendation regarding Sirah2 suitability for drug screening applications would also interest computational medicinal chemists targeting alpha-synuclein aggregation. The comparative force field assessment provides useful guidance for method selection in future studies.
- **Major strengths** The systematic comparison of two coarse-grained models with two all-atom force fields is valuable. The inclusion of enhanced sampling (REST2) to distinguish force field accuracy from sampling limitations is methodologically rigorous. The umbrella sampling calculations for both a peptide fragment and full-length alpha-synuclein provide quantitative aggregation free energy profiles. The analysis of secondary structure conservation during aggregation adds mechanistic insight. The practical recommendation regarding terminal charge states in Sirah2 is actionable.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (fibril stability interpretation), R1-M2 (PMF convergence and reference validity), R1-M3 (generality of conclusions from limited systems)
- **Assessment against Nature-style criteria** **Originality**: Moderate. The comparative force field assessment is useful but builds on prior work by the same group and others. The specific finding regarding Martini3 aggregation failure is novel but not transformative. **Scientific importance**: Moderate. The practical guidance for force field selection in alpha-synuclein studies is valuable for the simulation community but does not fundamentally advance understanding of aggregation mechanisms. **Interdisciplinary readership**: Limited. The manuscript is primarily of interest to computational biophysicists and force field developers. The connection to drug discovery is mentioned but not developed. **Technical soundness**: Adequate but with notable gaps. The simulation protocols are generally appropriate, but convergence assessments and reference validations are incomplete. **Readability for nonspecialists**: Acceptable. The manuscript is clearly written, but the technical depth and lack of contextual framing for non-simulation readers limit broader accessibility.
- **Recommendation posture** Supportive if technical concerns are resolved. The core comparative framework is valuable, and the practical recommendations are potentially useful. However, the concerns regarding fibril stability interpretation, PMF convergence, and generality of conclusions must be addressed before the claims are fully established.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of simulation results
- **Claim pointer** The authors claim that "the Martini3 fibril is not stable" and that this indicates Martini3 "cannot describe protein or peptide aggregation."
- **Evidence pointer** Section "Fibril Stability", Figure 7
- **Concern** The fibril stability assessment is based on a single 4 microsecond simulation per force field. The authors report that the Martini3 fibril "rapidly disaggregated" but do not provide quantitative criteria for what constitutes stability or disaggregation. The distance measurements between three specific residue pairs (Ala29, Val63, Asp98) may not capture the full complexity of fibril integrity. Furthermore, the initial fibril structure was presumably built from the experimental cryo-EM structure, but the equilibration protocol and the criteria for judging the system as "equilibrated" are not described in sufficient detail. The conclusion that Martini3 "cannot describe" aggregation is strong and may be sensitive to the specific system setup, the choice of salt concentration, or the finite simulation time.
- **Why it matters** The claim that Martini3 is unsuitable for aggregation studies is a central conclusion of the manuscript. If this conclusion is based on a single, potentially under-equilibrated simulation, it may be premature. A more robust assessment would include multiple independent simulations, a quantitative definition of fibril stability (e.g., contact maps, hydrogen bond persistence), and a demonstration that the disaggregation is not an artifact of the initial setup or the specific simulation conditions.
- **Resolution test** Provide multiple independent simulations (at least 3) for each force field, quantify fibril stability using multiple structural metrics (e.g., inter-chain contact maps, beta-sheet content over time, RMSD from the initial fibril structure), and demonstrate that the disaggregation is reproducible and not dependent on the initial velocities or the specific system preparation. Additionally, test the sensitivity of the result to salt concentration and box size.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative accuracy of free energy calculations
- **Claim pointer** The authors claim that Sirah2 with enhanced protein-water interactions and neutral termini provides "a peptide aggregation free energy profile similar to that found with all-atom models."
- **Evidence pointer** Section "Potentials of Mean Force", Figure 8
- **Concern** The comparison between coarse-grained and all-atom PMFs is central to the recommendation of Sirah2. However, the all-atom PMFs are based on 70 ns of sampling per window, which may be insufficient for convergence, especially for a peptide that can sample multiple conformational states. The authors do not provide convergence metrics for the PMFs (e.g., block error analysis, overlap between adjacent windows, or comparison of PMFs from independent simulations). Furthermore, the all-atom reference PMFs are themselves force field dependent, and the choice of Amber99sb and Charmm36m as references is not justified. The claim of "similarity" between Sirah2* and all-atom PMFs is qualitative; no quantitative comparison (e.g., root-mean-square difference between PMFs, comparison of well depths and locations) is provided.
- **Why it matters** The recommendation that Sirah2 is suitable for aggregation studies is based on the agreement between Sirah2* and all-atom PMFs. If the all-atom PMFs are not converged, or if the comparison is only qualitative, the recommendation is not firmly grounded. A quantitative comparison with converged all-atom references is essential to support the claim.
- **Resolution test** Provide convergence metrics for all PMFs (e.g., block error analysis, cumulative average plots, or comparison of PMFs from independent simulations). Extend the all-atom sampling if necessary to demonstrate convergence. Provide a quantitative comparison between Sirah2* and all-atom PMFs, such as the root-mean-square difference over the reaction coordinate range, and the difference in well depths and locations. Justify the choice of all-atom reference force fields.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Generality of conclusions
- **Claim pointer** The authors conclude that "Sirah2 with enhanced protein-water interactions is suitable for studying protein-protein and protein-drug aggregation."
- **Evidence pointer** Sections "Potentials of Mean Force" and "Conclusions"
- **Concern** The conclusion is based on a single peptide system (NACore, 11 residues) and a single full-length protein (alpha-synuclein). The aggregation of NACore is studied in isolation, and the full-length protein aggregation is only assessed through a single dimer PMF. The authors do not test whether the conclusions hold for other amyloidogenic peptides or for higher-order oligomers. The recommendation for drug screening applications is particularly strong, given that drug binding may involve different interaction patterns than peptide-peptide aggregation. The authors also do not discuss the transferability of the enhanced protein-water interaction scaling to other systems or conditions.
- **Why it matters** The practical recommendation for Sirah2 use in drug discovery is a key takeaway. If the conclusion is based on a limited set of systems, it may not be generalizable. A more cautious interpretation, acknowledging the need for validation on additional systems, would be more appropriate.
- **Resolution test** Test the Sirah2* model on at least one additional amyloidogenic peptide (e.g., amyloid-beta fragment) and compare the aggregation free energy profile with all-atom references. Discuss the potential limitations of the enhanced protein-water interaction scaling for other systems. Soften the recommendation for drug screening applications or provide additional validation for drug-like molecule binding.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Force field scaling factors
- **Evidence pointer** Section "Force Fields"
- **Issue** The manuscript states that for Sirah2, protein-water interactions are scaled by a factor of 1.3, and for Martini3, by 1.1. However, the specific implementation of this scaling is not described. For Sirah2, it is unclear whether the scaling applies to Lennard-Jones parameters, partial charges, or both. For Martini3, the scaling is described as "protein-water interactions," but the specific interaction terms that are modified are not specified.
- **Required correction** Provide a detailed description of the scaling procedure, including which interaction terms are modified and how the scaling factors are applied. Reference the original publications where these scaling factors were proposed and justify the choice of scaling factors for this study.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** Error estimation
- **Evidence pointer** Section "Umbrella Sampling", Figure 8
- **Issue** The PMFs are presented with error bars, but the method for error estimation is not described. It is unclear whether the errors are from Bayesian bootstrap, block averaging, or another method. The number of independent samples used for error estimation is not stated.
- **Required correction** Describe the error estimation method in the Methods section. State the number of independent samples or blocks used for error estimation.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Comparison with experiment
- **Affected element** Radius of gyration
- **Evidence pointer** Section "Structure of Alpha-Synuclein", Figure 2
- **Issue** The manuscript compares simulated radius of gyration values with experimental ranges but does not provide a quantitative comparison. It is unclear whether the simulated values fall within the experimental range, and if so, by what margin.
- **Required correction** Provide a quantitative comparison, such as the mean and standard deviation of the simulated Rg values and the experimental range. State whether the differences are statistically significant.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 8
- **Evidence pointer** Section "Potentials of Mean Force", Figure 8
- **Issue** The orientation of the two NACore peptides at ~3 nm is shown in Figure 8a and 8b, but the difference between the zwitterionic and non-zwitterionic forms is not clearly described in the figure caption. The reader is left to infer the structural differences from the figure.
- **Required correction** Expand the figure caption to explicitly describe the structural differences between the zwitterionic and non-zwitterionic forms, particularly the orientation of the termini.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Simulation setup
- **Evidence pointer** Section "Molecular Dynamics"
- **Issue** The manuscript does not specify the number of ions added to neutralize the system or the salt concentration. The box size and the minimum distance between the protein and the box edges are also not stated.
- **Required correction** Provide the salt concentration, the number of ions, the box dimensions, and the minimum protein-box distance in the Methods section.

## Risk / unsupported claims
- The claim that "Martini3 cannot describe protein or peptide aggregation" is not fully supported, as it is based on a single fibril simulation and a single peptide PMF, without mechanistic analysis of the disaggregation pathway.
- The claim that Sirah2 with enhanced protein-water interactions is "suitable for studying protein-protein and protein-drug aggregation" is not fully supported, as it is based on a limited set of systems and a qualitative comparison with all-atom results.
- The statement that "Sirah2, with enhanced protein-water interactions and neutral termini, provides a peptide aggregation free energy profile similar to that found with all-atom models" is not quantitatively demonstrated.
- The assertion that the results "indicate that this force field should be suitable to explore alpha-synuclein aggregation pathways and screen protein-drug binding free energies" is an extrapolation beyond the presented data, as no drug-like molecules were tested.
- The claim that "the enhancement of protein-water interactions by 30% in Sirah2* provides an enhanced description of the monomer while still providing a description of the aggregation tendency similar to that observed with the all-atom models" is not fully supported, as the comparison is qualitative and limited to a single system.