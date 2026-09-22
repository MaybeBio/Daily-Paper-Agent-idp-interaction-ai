## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and figure legends
- **Assessment boundary** Scientific content, technical soundness, logical coherence, and support of claims by presented evidence
- **Shared manuscript claim summary** The authors propose that large particles (up to 1 µm) can partition into biomolecular condensates when particle-condensate interactions are sufficiently strong, and that this partitioning can be made orthogonal by using distinct surface chemistries (biotin-streptavidin, oligonucleotide-protein interactions). They support this with experiments using functionalized polystyrene beads, coarse-grained molecular dynamics simulations, and an analytical theory.
- **Visible evidence base** Main text figures 1-6 (as referenced), supplementary figures 1-17, supplementary tables 1-8, methods section
- **Missing materials affecting confidence** Supplementary information content not provided in full; raw data files not accessible; detailed simulation parameter files not provided

## Reviewer
- **Overall assessment** This manuscript addresses a fundamental question in biomolecular condensate biology: whether large particles can partition into condensates when interactions are sufficiently strong. The combination of experiments, simulations, and theory is commendable and the orthogonal partitioning demonstration is novel. However, several technical concerns regarding the interpretation of partition coefficients, the generality of the simulation model, and the biological relevance of the findings need to be addressed before the case is fully established.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, particularly those interested in client partitioning mechanisms; synthetic biologists designing condensate-based systems; drug delivery researchers targeting condensates; and biophysicists studying size-dependent partitioning phenomena.
- **Major strengths** 1) The study systematically varies both particle size and interaction strength, providing a comprehensive phase space exploration. 2) The combination of experiments, coarse-grained simulations, and analytical theory provides complementary evidence. 3) The demonstration of orthogonal partitioning into immiscible condensates is a significant advance. 4) The derived analytical expression (Eq. 3) provides a simple predictive framework.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (partition coefficient quantification), R1-M2 (simulation model limitations), R1-M3 (biological relevance claims)
- **Assessment against Nature-style criteria** 
  - **Originality**: High. The question of whether arbitrarily large particles can partition into condensates given sufficient interaction strength has not been systematically addressed. The orthogonal partitioning demonstration is novel.
  - **Scientific importance**: High. This addresses a fundamental question in condensate biology and has implications for understanding how large complexes (ribosomes, viral capsids) interact with condensates.
  - **Interdisciplinary readership**: Moderate to high. Will appeal to biophysicists, cell biologists, synthetic biologists, and drug delivery researchers.
  - **Technical soundness**: Moderate. The experimental work appears carefully executed, but concerns about partition coefficient quantification and simulation model limitations need resolution.
  - **Readability for nonspecialists**: Good. The manuscript is clearly written with helpful schematics, though some simulation details may be challenging for experimental readers.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding partition coefficient quantification and the generality of the simulation conclusions.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of experimental quantification
- **Claim pointer** The authors claim that "90% of PS-PEG-biotin beads with 500 nm diameter partitioned into SA-RGG condensates" and use partition fractions throughout as quantitative measures.
- **Evidence pointer** Figure 3b, Figure 1d, Methods section "Image analysis"
- **Concern** The partition fraction is defined as particles "inside the condensate or at its interface" counted as inside. This conflates true internalization with surface adsorption. Given that the authors themselves demonstrate intermediate interaction strengths lead to interfacial localization (Figure 2b), this definition may overestimate partitioning. For the claim of "partitioning into" condensates, a stricter criterion distinguishing internal from interfacial particles is needed. Additionally, the optical resolution limit (~200-300 nm) may misclassify small beads near the interface as internal.
- **Why it matters** The central claim of the paper is that large particles can partition into condensates. If a significant fraction of counted particles are actually at the interface rather than internal, the conclusion would be substantially weakened. The distinction between internalization and surface adsorption is critical for the biological and drug delivery implications.
- **Resolution test** Provide separate quantification of internal vs. interfacial particles using z-stack analysis or super-resolution imaging. Alternatively, use fluorescence correlation spectroscopy or single-particle tracking to confirm internal diffusion. Re-analyze key experiments (Figures 1d, 3b, 3c) with the stricter criterion and show that conclusions remain valid.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Generality of simulation conclusions
- **Claim pointer** The authors conclude that "arbitrarily large particles can partition into condensates given sufficiently strong condensate-particle interactions" based on their LJ simulation model.
- **Evidence pointer** Figure 2, Methods section "Molecular dynamics simulations"
- **Concern** The simulation model uses a simple LJ potential with implicit solvent and no explicit representation of multivalency, charge patterning, or sequence-specific interactions that characterize real condensate systems. The claim of "arbitrarily large" particles is an extrapolation from simulations with size ratios up to σ2/σ1 = 3 (27x volume). Real condensates have mesh sizes, viscoelastic properties, and heterogeneous internal environments that may impose additional constraints not captured by this model. The theory (Eq. 3) predicts a linear relationship between required interaction strength and particle size, but this has not been tested experimentally beyond 1 µm particles.
- **Why it matters** The claim of "arbitrarily large" particles is a strong statement with implications for drug delivery and understanding biological processes. If the simulation model misses key physics (e.g., jamming, entanglement, or mesh-size effects), the conclusion may not hold for real systems. The extrapolation from the tested size range to "arbitrary" sizes is not justified by the data.
- **Resolution test** Acknowledge the limitations of the LJ model more explicitly. Either test larger size ratios in simulations (if computationally feasible) or temper the claim to "particles up to the sizes tested (1 µm) and potentially larger." Discuss how mesh size, viscoelasticity, and sequence-specific effects might modify the predictions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Biological relevance and generality
- **Claim pointer** The authors state their findings "may provide insights into how various cellular processes are achieved based on partitioning of large clients into biomolecular condensates" and suggest implications for ribosomes and viral capsids.
- **Evidence pointer** Discussion section, Introduction
- **Concern** The experimental system uses synthetic polystyrene beads with controlled surface chemistry, which is appropriate for a biophysical study. However, the leap to biological relevance (ribosomes, HIV capsids) is speculative. Real biological particles have complex surfaces with multiple interaction types, are often deformable, and exist in crowded cellular environments with competing interactions. The authors do not test any biological particles beyond ribosomes, and the ribosome results show heterogeneous partitioning that is not fully explained.
- **Why it matters** The broader significance of the work depends on its relevance to biological condensates. If the principles only apply to rigid, synthetically functionalized particles, the impact is more limited. The authors should either provide additional evidence for biological relevance or more carefully qualify their claims.
- **Resolution test** Either add experiments with biological particles (e.g., ribosomes with controlled surface modifications, viral-like particles) or revise the discussion to clearly distinguish between demonstrated principles for synthetic particles and hypothesized implications for biological systems.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of experimental conditions
- **Affected element** Figure 1b, ribosome experiments
- **Evidence pointer** Figure 1b, Methods
- **Issue** The ribosome experiments use E. coli ribosomes labeled with DyLight 650. The buffer includes 1 mM MgCl2, which differs from the standard buffer used for other experiments. The authors note heterogeneous partitioning into N protein condensates but do not fully explain this observation. Is the heterogeneity due to ribosome aggregation, variations in ribosome surface charge, or condensate heterogeneity?
- **Required correction** Provide additional characterization of ribosome behavior (e.g., dynamic light scattering to check aggregation, zeta potential measurements) and discuss possible sources of heterogeneous partitioning.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Figure 1c, antibody partitioning
- **Evidence pointer** Figure 1c
- **Issue** The antibody partitioning experiment shows a partition coefficient of about 5 for anti-N IgG versus about 1.5 for isotype control. While the difference is clear, the number of replicates and statistical test used are not stated in the figure legend.
- **Required correction** Add statistical analysis (e.g., t-test or ANOVA) and state the number of independent experiments and replicates in the figure legend.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of simulation description
- **Affected element** Simulation methods
- **Evidence pointer** Methods section "Molecular dynamics simulations"
- **Issue** The simulation description does not specify the number of independent simulation runs, error bars on partition coefficients in Figure 2c, or how the phase diagram boundaries were determined. The equilibration time (2 million steps out of 10 million) seems short for large particles that may diffuse slowly.
- **Required correction** Provide details on the number of replicates, error estimation, and convergence checks. Consider longer equilibration or demonstrate that results are converged.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation of salt dependence
- **Affected element** Figure 4d
- **Evidence pointer** Figure 4d, Discussion
- **Issue** The authors show that lower salt concentration favors partitioning of PS-PEG-polyA20 into RGG condensates. They attribute this to electrostatic interactions. However, salt also affects condensate properties (e.g., viscosity, mesh size) and RGG phase behavior. The authors note that low salt promotes RGG phase separation but high salt promotes (GRGNSPYS)25 phase separation, yet in both cases lower salt favored partitioning. This is somewhat counterintuitive and deserves more discussion.
- **Required correction** Discuss alternative explanations for the salt dependence, such as changes in condensate mesh size or viscosity, and how these might be distinguished from purely electrostatic effects.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation of theory
- **Affected element** Equations 1-3
- **Evidence pointer** Results section, Supplementary Notes
- **Issue** The derivation of the analytical theory is only briefly summarized in the main text with details in Supplementary Notes. The assumptions (e.g., negligible entropic contribution) are stated but not justified. The theory predicts a linear relationship between ε12 and σ2, but the physical interpretation of this linearity is not discussed.
- **Required correction** Briefly discuss the physical meaning of the linear relationship and the conditions under which the entropic contribution can be neglected.

## Risk / unsupported claims
- The claim that "arbitrarily large particles can partition into condensates" is an extrapolation beyond the tested size range and simulation capabilities. The data support particles up to 1 µm, but "arbitrary" is not justified.
- The statement that findings "may provide insights into how various cellular processes are achieved" is speculative and not directly supported by the experimental data.
- The suggestion that the principles could inform drug delivery to disease-related condensates is plausible but not demonstrated; no disease-relevant condensates or conditions were tested.
- The claim that the simulation model captures the essential physics of condensate partitioning is not fully supported given the simplicity of the LJ model compared to real condensate systems.
- The interpretation of ribosome partitioning as evidence for the general principle is weakened by the heterogeneous partitioning observed, which is not fully explained.