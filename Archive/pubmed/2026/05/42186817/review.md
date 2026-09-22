## Review setup
- **Input scope** Full manuscript text (abstract, introduction, materials and methods, results, discussion) without figures, tables, or supplementary material
- **Assessment boundary** Scientific soundness, methodological rigor, claim-evidence alignment, and clarity of the reported findings
- **Shared manuscript claim summary** The authors present a coarse-grained nucleosome-resolution model (NICG) that incorporates epigenetic modifications (acetylation, H1, BRD4) to simulate chromatin domain dynamics. They apply this model to the Pou5f1 and Sox2 loci in mouse embryonic stem cells and report that epigenetic-driven nucleosome interactions alone can produce sub-TAD-scale compartmentalization, dynamic liquid-like domains, and enhancer-promoter contacts.
- **Visible evidence base** Main text methods and results sections; references to supplementary figures and tables (not provided)
- **Missing materials affecting confidence** All figures, tables, supplementary information, simulation trajectories, and analysis scripts

## Reviewer
- **Overall assessment** This manuscript presents a computationally efficient coarse-grained model that addresses an important question: whether epigenetic modifications alone can drive chromatin domain organization. The model design is thoughtful, and the validation strategy against experimental data is commendable. However, the central claims regarding the functional relevance of the observed compartmentalization and enhancer-promoter contacts rest heavily on simulation results whose statistical robustness, sensitivity to parameter choices, and biological interpretation require further scrutiny. The manuscript is potentially significant but currently does not fully establish its case from the provided evidence.

- **Who would be interested in the results, and why** Researchers in chromatin biophysics, computational biology, and epigenetics would find this work relevant. The model offers a computationally tractable framework for exploring how epigenetic marks influence 3D genome organization, which is a topic of broad interest given the increasing recognition of phase separation in genome function. The approach may also appeal to experimentalists seeking mechanistic interpretations of Hi-C and Micro-C data.

- **Major strengths**
  1. The model is computationally efficient, enabling simulations of 100 kb regions over second timescales, which is a significant technical achievement.
  2. The parametrization strategy grounded in multiple experimental datasets (DNA persistence length, nucleosome unwrapping, sedimentation coefficients) is rigorous.
  3. The validation against liquid-liquid phase separation experiments and the checkerboard pattern in alternating nucleosome arrays strengthens confidence in the model.
  4. The systematic in silico perturbation studies (Δnucleosome interaction, ΔBRD4, ΔH1, short linker) provide useful mechanistic insights.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical robustness
- **Claim pointer** "Our simulations reveal that chromatin folds into liquid-like domains characterized by similar histone modifications" and "the simulated Pou5f1 locus clearly separated into three domains consistent with acetylation profile"
- **Evidence pointer** Results section "Nucleosome interactions induce 10-kilobase scale compartmentalization"; Figure 4 (not provided)
- **Concern** The claim of domain separation is based on visual inspection of contact maps and PCA from 9 replicas. The manuscript reports that replicas sample distinct metastable basins and that individual trajectories do not converge. This raises the question of whether the observed compartmentalization is a robust ensemble property or an artifact of limited sampling. The statistical significance of the domain boundaries, the reproducibility of the three-domain pattern across replicas, and the quantitative criteria for defining "domains" are not described in the provided text.
- **Why it matters** The central conclusion that epigenetics alone can drive sub-TAD compartmentalization depends on the reliability of the domain identification. Without statistical measures of domain stability, reproducibility across replicas, and comparison to null models (e.g., shuffled epigenetic marks), the claim is not fully supported.
- **Resolution test** Provide quantitative domain assignment criteria, show domain boundaries for each replica individually, report confidence intervals for domain boundaries, and compare against control simulations with randomized epigenetic patterns.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Parameter sensitivity
- **Claim pointer** "The model describes the effects of DNA linker length, histone tail acetylation, linker histone H1, and multibromodomain proteins such as BRD4" and the in silico mutation studies in Figure 6
- **Evidence pointer** Methods section "Force field parametrization and validation"; Results section "Regulatory factors of nucleosome interactions are essential for chromatin hierarchical organization"; Figure 6 (not provided)
- **Concern** The Lennard-Jones interaction strengths (ε values) are parametrized to match specific experimental data, but the sensitivity of the simulation outcomes to these parameters is not reported. For example, the reduction of εac to half of ε0 is based on sedimentation data, but it is unclear how sensitive the predicted domain formation and enhancer-promoter contacts are to this specific value. Similarly, the εB value for BR4-mediated bridging is not described in the provided text.
- **Why it matters** If the observed compartmentalization and enhancer-promoter contacts only emerge within a narrow parameter window, the biological conclusions would be fragile. The manuscript should demonstrate that the qualitative findings are robust to reasonable parameter variations.
- **Resolution test** Perform systematic parameter sweeps around the chosen ε values and show that the qualitative conclusions (domain formation, enhancer-promoter contacts) are preserved across a reasonable range.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Model validation against in vivo data
- **Claim pointer** "Our physics-based modeling establishes that epigenetic-dependent nucleosome interactions play a key role in shaping the functional organization of genomic loci"
- **Evidence pointer** Results sections on Pou5f1 and Sox2; Supplementary Figures S7 and S9 (not provided)
- **Concern** The comparison between simulated and experimental contact maps is described only qualitatively. The manuscript states that the correlation between simulated and experimental PC1 is not statistically significant (r = 0.08, p = 0.38) for Pou5f1, yet the overall conclusion is that the model captures functional organization. The discrepancy between simulated and experimental insulation scores is acknowledged but not quantitatively addressed.
- **Why it matters** The claim that the model "establishes" a role for epigenetics in functional organization requires stronger quantitative agreement with experimental data. The current comparison suggests the model captures some features but not others, and the manuscript does not provide a balanced assessment of what the model fails to reproduce.
- **Resolution test** Provide quantitative metrics of agreement between simulated and experimental contact maps (e.g., stratum-adjusted correlation coefficient, HiCRep), discuss discrepancies in insulation scores, and temper the conclusion to reflect the partial agreement.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Biological interpretation of enhancer-promoter contacts
- **Claim pointer** "In silico mutation studies further clarify the roles of individual epigenetic factors" and "contacts between distant acetylated enhancers and promoters are observed"
- **Evidence pointer** Results section "Nucleosome interactions induce 10-kilobase scale compartmentalization"; Figure 4C and 4D (not provided)
- **Concern** The manuscript reports that enhancer-promoter contacts are observed in simulations, but the functional significance of these contacts is inferred rather than demonstrated. The clustering analysis identifies three structural states, but the relationship between these states and transcriptional activity is not established. The claim that these contacts could "rescue" enhancer-promoter communication in the absence of cohesin is speculative.
- **Why it matters** The manuscript's broader significance depends on the claim that epigenetic-driven contacts are functionally relevant. Without linking the observed contacts to transcriptional outcomes or at least to known regulatory mechanisms, the functional interpretation remains speculative.
- **Resolution test** Discuss the limitations of inferring function from structural contacts, and either provide additional analysis linking contact frequency to known regulatory interactions or temper the functional claims.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section "Coarse-grained simulation"
- **Evidence pointer** Location not provided
- **Issue** The time mapping between simulation and real time is described only briefly. The scale factor of 1.4 ns/timestep is mentioned, but the derivation and validation of this mapping are not fully explained.
- **Required correction** Provide a more detailed explanation of how the time scale factor was determined and validated.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section "Pou5f1 and Sox2 loci model"
- **Evidence pointer** Location not provided
- **Issue** The procedure for assigning acetylation states, H1 binding, and BR4 association from ChIP-seq data is described at a high level, but the specific thresholds and processing steps are not detailed in the main text.
- **Required correction** Provide a more detailed description of the mapping procedure, or refer more explicitly to the supplementary methods.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Results section "Chromatin forms highly dynamic domains"
- **Evidence pointer** Figure 5 (not provided)
- **Issue** The use of Infomap community detection for domain assignment is mentioned, but the resolution parameter and its influence on domain sizes are not discussed.
- **Required correction** Describe the choice of resolution parameter and its effect on the results.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion
- **Evidence pointer** Location not provided
- **Issue** The discussion of the model's limitations is brief. The absence of cohesin, transcription factors, and other nuclear proteins is acknowledged, but the potential impact of these omissions on the conclusions is not fully explored.
- **Required correction** Expand the limitations section to discuss how the absence of these factors might affect the interpretation of the results.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section "Epigenetic-dependent nucleosomes clutches along the chromatin fiber"
- **Evidence pointer** Location not provided
- **Issue** The definition of "clutch" based on a four-nucleosome sliding window is clear, but the relationship between clutches and the larger domains identified by Infomap is not explicitly discussed.
- **Required correction** Clarify the relationship between clutches and domains.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Lack of statistical robustness analysis for domain identification
  - R1-M2: Absence of parameter sensitivity analysis
  - R1-M3: Weak quantitative agreement with experimental data

- **Assessment against Nature-style criteria**
  - **Originality**: The model is not entirely novel in concept, as other coarse-grained chromatin models exist, but the specific combination of nucleosome resolution, epigenetic modifications, and phase separation behavior offers a useful contribution.
  - **Scientific importance**: The question of whether epigenetic modifications alone can drive chromatin domain organization is important and timely. The model provides a testable framework.
  - **Interdisciplinary readership**: The work bridges biophysics, computational biology, and epigenetics, and would appeal to researchers across these fields.
  - **Technical soundness**: The parametrization strategy is sound, but the lack of statistical robustness and parameter sensitivity analyses weakens the technical foundation of the central claims.
  - **Readability for nonspecialists**: The manuscript is generally well-written and accessible, though some methodological details are dense. The figures (not provided) would likely aid comprehension.

- **Recommendation posture** Supportive if technical concerns are resolved. The model and approach are promising, and the manuscript addresses an important question. However, the central claims regarding domain formation and functional organization require stronger statistical support, parameter sensitivity analysis, and a more balanced quantitative comparison with experimental data.