## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors present a Monte Carlo framework for simulating biomolecular condensate nucleation in the grand canonical ensemble, combining conformation sampling with bias-enhanced cluster size sampling. They report validation against structural properties of disordered proteins and application to FUS-LC and NDDX4 with two coarse-grained force fields (HPS and MPIPI). They claim capture of both classical and nonclassical nucleation mechanisms, with NDDX4 under MPIPI exhibiting nonclassical behavior including metastable prenucleation clusters and horseshoe-like cluster geometries.
- **Visible evidence base** Abstract text only; no figures, tables, methods details, or numerical results provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, simulation protocols, force field parameters, convergence criteria, error analysis, benchmark details, and comparison with experimental or other computational data

## Reviewer
- **Overall assessment** The abstract describes a potentially valuable methodological advance in simulating biomolecular condensate nucleation within the grand canonical ensemble. The conceptual motivation, namely overcoming fixed particle number limitations and enabling direct control of dilute-phase concentration, is sound and addresses a recognized gap in the field. However, the abstract alone provides insufficient detail to evaluate the technical implementation, the robustness of the validation, or the strength of the mechanistic claims. The reported findings, particularly the force field dependent nucleation pathways, are intriguing but require substantial supporting evidence to be established.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, nucleation theory, and coarse-grained molecular simulation would be interested. The work addresses fundamental questions about how sequence composition and force field parametrization influence nucleation mechanisms, which is relevant to understanding the physical chemistry of intracellular phase behavior and to developing predictive simulation tools.
- **Major strengths** The methodological framing addresses a clear limitation of existing fixed particle number simulations. The combination of conformation sampling with bias-enhanced cluster size sampling is a plausible strategy for resolving nucleation free energy surfaces. The application to two distinct proteins with two force fields provides a comparative framework that could reveal important mechanistic insights.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria**  
  Originality: The grand canonical approach to condensate nucleation is a meaningful departure from standard fixed particle number simulations, though the abstract does not clarify how this differs from existing grand canonical or open ensemble methods in the broader simulation literature.  
  Scientific importance: The question of how nucleation pathways depend on force field and sequence is important for the condensate field, but the abstract does not yet demonstrate generalizable conclusions beyond two test systems.  
  Interdisciplinary readership: The topic bridges physical chemistry, biophysics, and soft matter science, and the abstract is written in a way that is broadly accessible.  
  Technical soundness: Cannot be adequately assessed from the abstract alone. The validation claim is vague, and no convergence or error analysis is presented.  
  Readability for nonspecialists: The abstract is clear and well structured, with technical terms used appropriately, though some jargon such as "bias-enhanced cluster size sampling" and "MPIPI" would benefit from brief clarification.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a promising framework and interesting preliminary observations, but the technical validity and the strength of the mechanistic claims cannot be evaluated without the full manuscript. A supportive posture would require that the technical concerns regarding validation, convergence, and evidence for nonclassical nucleation be resolved.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The method "enables accurate sampling of individual cluster sizes in various conformations" and "resolves nucleation free energy surfaces."  
- **Evidence pointer** Abstract only; no methods or figures provided  
- **Concern** The abstract claims accurate sampling and resolution of free energy surfaces but provides no details on the bias-enhanced sampling scheme, the order parameters used, the convergence criteria, or the uncertainty quantification. Without this information, it is impossible to assess whether the sampling is indeed unbiased and converged across the relevant cluster size range.  
- **Why it matters** Nucleation free energy profiles are highly sensitive to sampling quality. Inadequate sampling or poorly chosen bias parameters can produce artifacts such as spurious local minima or incorrect barrier heights, which would directly undermine the central mechanistic conclusions.  
- **Resolution test** The full manuscript must provide a detailed description of the sampling method, convergence tests (e.g., block averaging, multiple independent runs), and error bars on free energy profiles. Ideally, the method should be benchmarked against known analytical or reference results for a simple system.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Validation strength  
- **Claim pointer** "We validated our method by reproducing structural properties of disordered proteins across a diverse benchmark set."  
- **Evidence pointer** Abstract only; benchmark set not specified  
- **Concern** The validation claim is vague. No information is given about which proteins constitute the benchmark set, which structural properties were compared, against what reference data, or what level of agreement was achieved. The phrase "diverse benchmark set" is not substantiated.  
- **Why it matters** Validation is the foundation for trusting the method's predictions on new systems. If the benchmark is narrow or the agreement is qualitative only, the method's general applicability and the reliability of the FUS-LC and NDDX4 results remain uncertain.  
- **Resolution test** The full manuscript must list the benchmark proteins, the specific structural observables (e.g., radius of gyration, end-to-end distance, secondary structure propensities), the reference data source, and quantitative agreement metrics (e.g., root mean square deviation, correlation coefficients).

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence for mechanistic claims  
- **Claim pointer** "NDDX4 follows a nonclassical nucleation pathway under the MPIPI force field: the free-energy profile versus cluster size is convex and exhibits a local minimum, indicating the presence of metastable prenucleation clusters."  
- **Evidence pointer** Abstract only; no free energy profiles shown  
- **Concern** The central mechanistic finding, namely the nonclassical pathway for NDDX4 with MPIPI, is stated without any quantitative support. The abstract does not report the magnitude of the local minimum, its statistical significance, or how it compares to the classical profiles for the other systems. The interpretation of a convex profile with a local minimum as evidence for metastable prenucleation clusters requires careful analysis of cluster definitions and finite size effects.  
- **Why it matters** This is the most novel and potentially impactful claim in the abstract. If the local minimum is within statistical noise or arises from an artifact of the cluster definition or the bias scheme, the conclusion would be invalid. The claim also has implications for understanding how force field choice alters physical predictions, which is a sensitive issue.  
- **Resolution test** The full manuscript must show the free energy profiles for all systems and force fields, with error bars, and provide a statistical test for the existence and significance of the local minimum. The cluster definition and its sensitivity to parameters should be discussed. Ideally, the nonclassical behavior should be corroborated by additional observables such as cluster size distributions or structural analysis of the prenucleation clusters.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Generalizability and scope  
- **Claim pointer** "results from our initial test systems underscore the critical role of sequence composition and force-field parametrization in shaping nucleation pathways and demonstrate the utility of our framework for uncovering complex, mechanism-rich free energy landscapes."  
- **Evidence pointer** Abstract only; two test systems  
- **Concern** The abstract generalizes from two proteins and two force fields to broad statements about sequence composition and force field parametrization. With only two systems, it is not possible to disentangle sequence effects from force field effects, and the claim that sequence composition plays a critical role is not directly supported by any comparative analysis.  
- **Why it matters** Overgeneralization from limited test cases can mislead the field. The utility of the framework is plausible, but the specific conclusions about sequence and force field effects require a more systematic study or at least a careful discussion of confounding factors.  
- **Resolution test** The full manuscript should either include additional systems to support the general claims or temper the conclusions to reflect the limited scope. A discussion of how sequence and force field effects are disentangled in the current design would also help.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Terminology  
- **Evidence pointer** Abstract, first sentence  
- **Issue** The term "grand canonical ensemble" is used without explaining its relevance to condensate nucleation. Readers unfamiliar with statistical mechanics may not immediately grasp why controlling the chemical potential rather than particle number is advantageous.  
- **Required correction** Add a brief phrase explaining that the grand canonical ensemble allows the dilute phase concentration to be set directly, which is more natural for nucleation studies where the supersaturation is the key control parameter.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Force field description  
- **Evidence pointer** Abstract, results section  
- **Issue** The acronyms HPS and MPIPI are introduced without definition. While specialists may recognize HPS, MPIPI is less standard and its nature is not described.  
- **Required correction** Define both acronyms at first use, for example "HPS (hydrophobic-polar scale) and MPIPI (a recently developed transferable coarse-grained model)".

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Interpretation  
- **Affected element** Morphological observation  
- **Evidence pointer** Abstract, last sentence of results  
- **Issue** The observation that larger NDDX4 clusters with MPIPI adopt a "curved, horseshoe-like geometry" is presented without any interpretation of its physical significance or connection to the nonclassical nucleation pathway.  
- **Required correction** Briefly state whether this morphology is expected to be a general feature of nonclassical nucleation or specific to this system, and how it relates to the free energy profile.

## Risk / unsupported claims
- The claim that the method "enables accurate sampling of individual cluster sizes in various conformations" is unsupported without convergence and error analysis.
- The claim of validation against a "diverse benchmark set" is unsupported without specification of the set and quantitative agreement metrics.
- The claim of a nonclassical nucleation pathway for NDDX4 with MPIPI, including metastable prenucleation clusters, is unsupported without shown free energy profiles and statistical significance testing.
- The general claim that sequence composition plays a critical role in shaping nucleation pathways is not supported by the two-system comparison presented.
- The morphological observation of horseshoe-like geometries is presented without quantitative characterization or connection to the nucleation mechanism.