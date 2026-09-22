## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusion, experimental section) as provided
- **Assessment boundary** Scientific content, methodology, data interpretation, and internal consistency of the claims as presented in the provided text
- **Shared manuscript claim summary** The authors propose that proteins adsorbed to polystyrene nanoparticles (PSNPs) form a highly solvated, disordered corona anchored at a limited number of attachment sites. They report that binding affinity decreases with increasing nanoparticle size, that proteins are destabilized more on smaller (higher curvature) PSNPs, and that these trends extrapolate to flat polystyrene surfaces. They further propose an "adsorbotope" model to explain corona structure and prior fibrillation observations.
- **Visible evidence base** DLS, ITC, intrinsic tryptophan fluorescence (GdmCl denaturation), far-UV CD, ANS fluorescence, MD simulations (GB3 only), TEM, zeta potential measurements
- **Missing materials affecting confidence** Figures and tables referenced but not provided (Figures 1–6, Tables 1, S1–S8); MD simulation details incomplete (force field parameters for polystyrene not fully specified); no raw data or statistical output tables; no information on protein purity or folding state post-purification

## Reviewer

- **Overall assessment** This manuscript addresses an important and timely question in nanobiointerfaces: the conformational state of proteins in the nanoparticle corona. The authors combine multiple biophysical techniques to build a case for a solvated, disordered corona on polystyrene nanoparticles, with curvature-dependent effects. The conceptual model is interesting and potentially impactful. However, the evidence as presented has several gaps. The most significant concerns are: (1) the interpretation of ITC stoichiometry relies on assumptions about nanoparticle concentration and monodispersity that are not fully validated; (2) the claim of "disorder" is inferred indirectly from hydrodynamic size and thermodynamic parameters, without direct structural evidence (e.g., NMR, H/D exchange, or single-molecule FRET); (3) the extrapolation to flat surfaces is based on a single ANS fluorescence experiment with acknowledged quantitative limitations; and (4) the MD simulations are preliminary (50 ns analysis from 100 ns runs, two models only) and do not directly demonstrate unfolding. The manuscript is well-written and the logical flow is clear, but the core claims require stronger direct evidence or more cautious framing.

- **Who would be interested in the results, and why** Researchers in nanomedicine, protein biophysics, and bionanoscience would find this relevant. The question of corona structure directly impacts how nanoparticles are recognized by cells and the immune system, and the proposed "adsorbotope" model could inform predictive design of nanoparticle surfaces. The curvature-dependent destabilization trend is also of interest to those studying protein-surface interactions more broadly.

- **Major strengths**
  1. The study addresses a fundamental and under-explored question: the degree of disorder and solvation in the protein corona, using a well-controlled model system (PSNPs with two proteins of different size and charge).
  2. The combination of techniques (ITC, DLS, fluorescence, CD, ANS, MD) provides a multi-pronged approach, and the authors are careful to note limitations of individual methods.
  3. The ratiometric comparison of stoichiometry (NGB3/NR2ab) against polymer scaling predictions is a clever and relatively model-independent way to support the disordered polymer hypothesis.
  4. The authors control for total nanoparticle surface area across experiments, which is a methodological strength often missing in the literature.
  5. The discussion of prior fibrillation data in light of their model is thoughtful and provides a testable framework.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength for central claim
- **Claim pointer** "we find evidence for a highly disordered, solvent accessible protein corona on PSNPs" (Abstract, Results section "GB3 and R2ab are Well-Solvated, Disordered Polymers when Adsorbed to PSNPs")
- **Evidence pointer** Results section "GB3 and R2ab are Well-Solvated, Disordered Polymers when Adsorbed to PSNPs"; Figure 1F; Table S5
- **Concern** The central claim of a "disordered, solvated" corona is inferred from (a) low ITC stoichiometry relative to geometric predictions, (b) large ΔdH from DLS, and (c) thermodynamic parameters. However, none of these measurements directly reports on protein conformation at residue-level resolution. The authors acknowledge that ITC stoichiometry could be affected by nanoparticle concentration uncertainty, and DLS ΔdH is an indirect measure. The ratio NGB3/NR2ab is consistent with a disordered polymer, but it is also consistent with other models (e.g., partial unfolding, anisotropic adsorption, or multilayer formation with different packing). Direct structural evidence (e.g., NMR, H/D exchange mass spectrometry, or single-molecule FRET) would be needed to firmly establish the "disordered polymer" claim.
- **Why it matters** The entire conceptual model and its implications for immune recognition and fibrillation depend on the corona being genuinely disordered and solvated. If the corona is instead a partially structured or molten-globule-like state, the proposed "adsorbotope" model and the explanation of fibrillation data would need substantial revision.
- **Resolution test** Provide direct structural evidence of disorder (e.g., NMR chemical shift perturbations, missing amide protons in H/D exchange, or FRET-based distance distributions) for at least one protein on PSNPs. Alternatively, re-frame the claim as "consistent with a disordered state" rather than definitive, and discuss alternative interpretations explicitly.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative rigor of ITC analysis
- **Claim pointer** "the binding affinity decreases as nanoparticle size increases" and "the stoichiometry of binding... support a highly solvated, disordered protein corona" (Abstract, Results sections)
- **Evidence pointer** Results section "As Nanoparticle Curvature Decreases, the Apparent Binding Affinity Decreases..."; Figure 1C–E; Table S2
- **Concern** The ITC-derived binding affinities and stoichiometries are central to the manuscript's conclusions. However, the authors note that nanoparticle concentration is based on manufacturer's counts and gravimetric analysis, with an uncertainty of ~5%. For 50 nm PSNPs, a 5% error in concentration could translate to a significant error in N and K, given the steep dependence of fitted parameters on active site concentration. Additionally, the two-site model used for GB3 on 50 nm PSNPs introduces additional parameters (K1, K2, N1, N2) that may not be uniquely determined by the data, especially if the endothermic hump is small. The authors do not report confidence intervals for fitted parameters or discuss parameter identifiability.
- **Why it matters** If the absolute values of N and K are uncertain, the comparison of N across particle sizes and the conclusion that N is "far less than geometric predictions" may be quantitatively unreliable. The trend in binding affinity with size is a key result, and its robustness to concentration errors should be demonstrated.
- **Resolution test** Perform a sensitivity analysis of fitted N and K to ±10% variation in nanoparticle concentration. Report confidence intervals for all fitted parameters. If possible, validate nanoparticle concentration by an independent method (e.g., nanoparticle tracking analysis or UV-vis with known extinction coefficient).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Extrapolation to flat surfaces
- **Claim pointer** "Our observations hold for proteins on flat polystyrene surfaces, which have the lowest hydrophobic exposure" (Abstract, Results section "Trends in Protein Structural Changes Can Be Extrapolated to Macroscopic Surfaces on Treated Polystyrene Plates")
- **Evidence pointer** Results section "Trends in Protein Structural Changes Can Be Extrapolated to Macroscopic Surfaces on Treated Polystyrene Plates"; Figure 4A–C
- **Concern** The extrapolation to flat surfaces is based on a single ANS fluorescence experiment comparing PSNPs to a 6-well plate. The authors acknowledge that the plate surface is not perfectly smooth and that the comparison is approximate. However, the conclusion that "the trend in ANS fluorescence follows the trend we observed for nanoparticles" is used to support the generalizability of the model. The experiment does not control for differences in surface chemistry (tissue culture-treated vs. plain PSNPs), potential differences in protein concentration at the surface, or the possibility that ANS fluorescence is affected by the plate material itself. The statistical significance of the difference between "Plate Only" and "200 nm PSNPs" is not reported.
- **Why it matters** The claim that the model extends to macroscopic surfaces is important for the proposed biological implications (e.g., biofilm formation on medical devices). If the flat-surface data are not robust, this part of the conclusion is overstated.
- **Resolution test** Provide statistical comparison (with p-values) between plate and PSNP conditions. Include a control with an untreated polystyrene plate or a plate with a different surface treatment. Discuss the potential confounding effect of surface chemistry differences.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** MD simulation support
- **Claim pointer** "Molecular Dynamics Simulations Reveal Attractive Protein-PSNP Interactions that Can Potentially Induce Unfolding" (Results section)
- **Evidence pointer** Results section "Molecular Dynamics Simulations Reveal Attractive Protein-PSNP Interactions that Can Potentially Induce Unfolding"; Figure 5A–C
- **Concern** The MD simulations are presented as supporting evidence, but the analysis is limited to 50 ns of simulation (from 100 ns runs), with only two independent models of the polystyrene surface. The authors report RMSF differences in loop regions but do not demonstrate actual unfolding events. The force field parameters for polystyrene are not fully described (only "GAFF2" is mentioned, but the derivation of partial charges is described in the Experimental section). The authors correctly note that "it is unreasonable to expect a significant degree of protein unfolding" in this timescale, but then use the simulations to support the unfolding narrative. This is a weak link in the evidence chain.
- **Why it matters** The simulations are used to provide a "plausible picture" of early unfolding, but they do not add quantitative support to the central claim. If the simulations are not conclusive, they should be presented as illustrative rather than evidential, or the authors should clarify what specific hypothesis the simulations test.
- **Resolution test** Either extend simulations to longer timescales with enhanced sampling (e.g., replica exchange), or re-frame the simulation section as a qualitative illustration of surface contacts, clearly stating that they do not provide evidence of unfolding.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** "adsorbotope" (Discussion, Conclusion)
- **Evidence pointer** Discussion section
- **Issue** The term "adsorbotope" is introduced without a formal definition or citation. It is used to describe regions of high binding affinity, but the relationship to epitopes (as in the antibody analogy) is not fully explained.
- **Required correction** Define the term explicitly when first used, and provide a citation if it has been used previously, or acknowledge it as a new term proposed by the authors.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** ANS fluorescence data
- **Evidence pointer** Results section "Trends in Protein Structural Changes Can Be Extrapolated to Macroscopic Surfaces on Treated Polystyrene Plates"; Figure 3C–D
- **Issue** The authors state that "the overall ANS intensity was reduced as the size of the nanoparticles increased" but do not report statistical significance for these comparisons. Given that the differences between 100 nm and 200 nm conditions appear small, it is unclear if these are meaningful.
- **Required correction** Report p-values or confidence intervals for pairwise comparisons between nanoparticle sizes.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** GdmCl denaturation experiments
- **Evidence pointer** Experimental section "Intrinsic Tryptophan Fluorescence"
- **Issue** The authors state that "the linear extrapolation model was used to extract ΔG°H2O and an m-value" but do not specify the protein concentration, the range of GdmCl concentrations used, or how the baseline and post-transition baselines were defined. This limits reproducibility.
- **Required correction** Provide full experimental details, including protein concentration, GdmCl concentration range, and fitting procedure.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Internal consistency
- **Affected element** Figure numbering
- **Evidence pointer** Results section "When Total Nanoparticle Surface Area Is Held Constant..."
- **Issue** The text refers to "Figure 4A–B" for CD data and "Figure 3C–D" for ANS data, but the order of figure references in the text is not sequential (Figure 3 is referenced after Figure 4). This may be a formatting issue, but it could confuse readers.
- **Required correction** Ensure figure numbering is sequential in the order of first mention.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness of simulation methods
- **Affected element** MD simulation parameters
- **Evidence pointer** Experimental section "Molecular Dynamics (MD) simulations"
- **Issue** The authors state that "the ESP charges were then averaged over all chemically equivalent atoms across all ten styrene monomers" but do not specify how the polystyrene surface was constructed (e.g., density, arrangement of chains, whether the surface is planar or curved). This is important for reproducibility.
- **Required correction** Provide details on the construction of the polystyrene models, including chain length, arrangement, and any equilibration steps.

## Risk / unsupported claims
- The claim that the corona is "highly disordered" is not directly supported by the presented data; it is inferred from indirect measurements. This is the central claim of the manuscript and requires stronger evidence.
- The extrapolation to flat polystyrene surfaces is based on a single experiment with acknowledged limitations and no statistical comparison.
- The MD simulations are described as "revealing" attractive interactions, but the analysis is preliminary and does not demonstrate unfolding; the claim that they support the unfolding model is overstated.
- The statement that "the scaling of the stoichiometry vs. nanoparticle size is consistent with disordered polymer dimensions" is plausible but relies on the accuracy of the ITC-derived N values, which are subject to concentration uncertainties.
- The explanation of prior fibrillation data is speculative and presented as a post-hoc rationalization; it is not tested in this manuscript.