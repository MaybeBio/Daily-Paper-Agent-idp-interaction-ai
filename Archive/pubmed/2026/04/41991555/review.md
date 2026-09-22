## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and figure captions. Supplementary information referenced but not provided.
- **Assessment boundary** Scientific content, methodological rigor, validity of claims relative to presented evidence, and alignment with Nature-style criteria. Not assessed: editorial quality, formatting, or literature completeness beyond what is visible.
- **Shared manuscript claim summary** The authors use Martini3-IDP coarse-grained molecular dynamics simulations to compare the internal structure and dynamics of biomolecular condensates formed by full-length multidomain proteins (MDPs) versus those formed by IDRs/LCDs alone. They report that MDP-based condensates exhibit significant structural heterogeneity, conserved residue interaction specificity relative to solution state, and attenuated global and local dynamics, and propose folded domains act as "architectural keystones" in natural condensates.
- **Visible evidence base** Main text figures 1–6 with captions, methods section, and figure source data statements. Supplementary figures and tables are referenced but not available for review.
- **Missing materials affecting confidence** Supplementary Information (figures, tables, discussion), source data files, simulation topology/parameter files, and the Transparent Peer Review file. These are essential for verifying model calibration, convergence, and quantitative claims.

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely gap in the condensate field: the systematic comparison of IDR-only versus full-length MDP-based condensates using a state-of-the-art coarse-grained model. The central observations, namely that folded domains impose structural heterogeneity, preserve interaction specificity, and attenuate dynamics, are potentially significant and of broad interest. However, the strength of the conclusions is currently limited by several factors: the reliance on a single, recently modified force field without full calibration details visible; the use of relatively short simulation timescales for systems with slow relaxation; the absence of direct experimental validation for the MDP systems; and the lack of quantitative error analysis for key claims. The manuscript is well-written and the logic is clear, but the evidence as presented does not yet fully establish the generality of the claims. The work is promising and likely suitable for publication after substantial revision and clarification.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, intrinsically disordered proteins, and coarse-grained simulation. The work is also relevant to cell biologists studying the role of folded domains in condensate function and to computational biophysicists developing and benchmarking models for multicomponent systems. The claim that folded domains act as "architectural keystones" has implications for understanding condensate composition, rheology, and function in health and disease.
- **Major strengths**
  1. The study addresses a critical and under-explored question: how do folded domains, which are ubiquitous in natural condensates, alter the internal organization and dynamics compared to simplified IDR-only models?
  2. The use of a systematic comparison across multiple systems (FUS, HSPB2, PGL1) and the inclusion of both IDR-only and full-length constructs is a strong design.
  3. The observation of conserved interaction specificity between condensate and solution states, despite structural heterogeneity, is a novel and potentially important finding.
  4. The analysis of spatial heterogeneity (core vs. interface) in dynamics adds depth and connects to emerging experimental work on condensate internal organization.
  5. The manuscript is clearly written and the figures are informative.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / Model validation
- **Claim pointer** The authors claim their refined Martini3-IDP model "reliably recapitulates both structural and thermodynamical properties of biomolecular condensates" and that the predicted saturation concentrations deviate by less than 1.5 logarithmic units from experiment.
- **Evidence pointer** Results section "Martini3-IDP model captures condensate formation with near-quantitative accuracy", Figure 1a, Supplementary Figs. 1–4, Supplementary Table 1. Location not provided for supplementary materials.
- **Concern** The validation of the refined model is presented in a compressed form. The calibration of side-chain interactions via PMFs is described only briefly, and the benchmark against all-atom force fields is not shown. The claim of "near-quantitative accuracy" is based on a single metric (saturation concentration) for a limited set of systems, and the deviation of up to 1.5 log units is substantial. It is unclear how the model performs for the specific MDP systems studied here (FUS, HSPB2, PGL1) in terms of reproducing known experimental phase behavior. Without the supplementary details, the reader cannot assess whether the model is sufficiently accurate for the strong structural and dynamic claims made.
- **Why it matters** The entire study rests on the fidelity of the simulation model. If the model overestimates or underestimates interaction strengths, the observed structural heterogeneity and dynamic attenuation could be artifacts of the force field rather than genuine physical properties of MDP condensates. The claim of "near-quantitative accuracy" is not supported by the visible evidence.
- **Resolution test** Provide the full calibration details in the main text or supplement, including the PMF comparisons, the benchmark against all-atom simulations, and a more extensive validation of the model against experimental data for the specific systems studied. Quantify the uncertainty in the saturation concentration predictions and discuss the implications of the 1.5 log unit deviation for the conclusions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / Sampling and convergence
- **Claim pointer** The authors claim that IDR-only condensates exhibit "uniformly expanded conformations" and that MDP-based condensates exhibit "significant heterogeneity" and "attenuated dynamics" based on tens of microseconds of simulation.
- **Evidence pointer** Results sections "IDR-only condensates exhibit extended monomer conformations" and "Full-length MDP-based condensates preserve interaction profile despite offering a heterogeneous environment", Figures 1, 3, 4, 6, Supplementary Figs. 6, 12, 13, 21. Location not provided for supplementary materials.
- **Concern** The simulation timescales (20–28 μs) are short for dense, viscous condensate systems, especially those containing large folded domains. The authors acknowledge this for PGL1 (insufficient sampling) but do not systematically address whether the observed heterogeneity and dynamic attenuation are converged or reflect non-equilibrium states. The use of elevated-temperature equilibration for HSPB2 and PGL1 (333 K and 363 K) followed by production at 303 K raises questions about whether the systems have fully relaxed to the target temperature and whether the observed structures are representative of equilibrium. The analysis of core vs. interface dynamics relies on a static definition of regions, but the manuscript does not show that these regions are stable over the analysis window.
- **Why it matters** If the systems are not fully equilibrated, the reported structural heterogeneity and dynamic differences between core and interface could be transient artifacts. The claim that MDP condensates are "structurally heterogeneous" is a central finding and must be robust to sampling limitations.
- **Resolution test** Provide convergence analysis, such as block averaging of key observables (Rg distributions, contact maps, MSD curves) over successive time windows. Show that the core/interface designation is stable over time. Discuss the equilibration protocol in more detail and justify the use of elevated temperatures. If possible, extend simulations or use enhanced sampling to demonstrate that the observed heterogeneity is an equilibrium property.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance / Generalizability
- **Claim pointer** The authors propose that "folded domains act as architectural keystones in natural condensates" and that their findings "enrich the understanding of endogenous condensates internal structural and dynamic properties."
- **Evidence pointer** Discussion section, Abstract.
- **Concern** The study is based on three specific proteins (FUS, HSPB2, PGL1) in simplified single-component systems. While these are relevant models, the claim of a general principle ("architectural keystones") is a significant extrapolation. The authors do not discuss how the specific nature of the folded domains (e.g., size, shape, interaction propensity) might modulate the observed effects. The potential role of RNA, client proteins, and other cellular components in altering the balance between folded-domain and IDR interactions is not addressed. The study is a valuable starting point, but the generality of the "keystone" concept is not established.
- **Why it matters** The title and abstract make a broad claim about the role of folded domains in natural condensates. If the effect is specific to the systems studied, the impact of the work is reduced. The field needs to know how generalizable these findings are.
- **Resolution test** Soften the claims in the title and abstract to reflect the specific systems studied. Add a discussion of the potential range of behaviors depending on folded domain properties and system composition. If possible, include simulations of additional MDPs with diverse folded domain architectures to test the generality of the findings.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness / Comparison to experiment
- **Claim pointer** The authors state that their findings "align with experimental observation from native ion mobility mass spectrometry" for FUS compaction and cite prior work on condensate dynamics.
- **Evidence pointer** Results section "Full length FUS protein imposes different condensate structure and FUSLCD segment behavior", Discussion section.
- **Concern** The comparison to experiment is qualitative and limited. For FUS, the authors cite a single experimental study. For HSPB2 and PGL1, no direct experimental comparison is made. The claim of "attenuated dynamics" is not compared to any experimental measurement of condensate viscosity or molecular mobility. The authors do not discuss whether the magnitude of the dynamic slowdown they observe is consistent with experimental estimates.
- **Why it matters** A key strength of simulation studies is the ability to make predictions that can be tested experimentally. The lack of quantitative comparison to experiment weakens the impact of the work and leaves open the question of whether the observed effects are physiologically relevant.
- **Resolution test** Add a more detailed comparison to available experimental data, such as FRAP, FCS, or rheology measurements, for the systems studied. If quantitative data are not available, discuss the expected experimental signatures of the predicted heterogeneity and dynamic attenuation and how they could be measured.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity / Reproducibility
- **Affected element** Methods section "Analysis of MD simulations"
- **Evidence pointer** Methods section, location not provided.
- **Issue** The description of the KL and JS divergence calculations is brief. It is not clear how the distributions were binned or how statistical uncertainties were estimated.
- **Required correction** Provide more detail on the calculation of KL and JS divergences, including binning schemes and error estimation. Consider adding a supplementary figure showing example distributions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness / Force field
- **Affected element** Methods section "MD simulation protocol"
- **Evidence pointer** Methods section, location not provided.
- **Issue** The use of an elastic network model for folded domains is standard, but the choice of parameters (force constant, cutoff) is not justified. The potential impact of the elastic network on the dynamics of the folded domains and their interactions with IDRs is not discussed.
- **Required correction** Justify the choice of elastic network parameters and discuss the potential limitations of this approach for studying the dynamics of folded domains in condensates.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance / Context
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction, Discussion.
- **Issue** The discussion of prior simulation work on MDP condensates is brief. The authors mention a few studies but do not clearly delineate what is new in their work compared to, for example, studies on hnRNPA1 or TDP-43.
- **Required correction** Expand the discussion of prior simulation work to clearly state the novel contributions of this study.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity / Presentation
- **Affected element** Figure 3
- **Evidence pointer** Figure 3 caption.
- **Issue** The color coding in Figure 3a is described as "Monomers are color-coded", but it is not clear if this is by chain or by domain type. The snapshot in Figure 3b would benefit from a scale bar.
- **Required correction** Clarify the color coding in the figure caption and add a scale bar to the snapshot.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness / Analysis
- **Affected element** Results section "Both local and global dynamics are attenuated in full-length MDP-based condensates"
- **Evidence pointer** Figure 6, Supplementary Table 4.
- **Issue** The calculation of the "local effective diffusion constant" from MSD curves over a 5–20 ns window is described, but the choice of this window is not justified. The manuscript does not show the MSD curves or the fits.
- **Required correction** Show representative MSD curves and fits in a supplementary figure. Justify the choice of fitting window and discuss the limitations of this approach for extracting diffusion constants in heterogeneous systems.

## Risk / unsupported claims
- The claim that the refined Martini3-IDP model achieves "near-quantitative accuracy" is not fully supported by the visible evidence, as the calibration details and full validation are in the supplementary materials.
- The claim that folded domains act as "architectural keystones" in natural condensates is a general statement extrapolated from three specific model systems and is not fully established.
- The claim that "both local and global dynamics are attenuated" in MDP condensates is based on short simulations and may not be converged.
- The comparison to experimental data is qualitative and limited to a single study for FUS; no direct experimental validation is provided for HSPB2 or PGL1.
- The statement that "interaction specificity remains conserved between the condensed and solution states" is based on correlation coefficients and divergence measures, but the statistical significance of these measures is not fully discussed.