## Review setup

- **Input scope** Full manuscript text, abstract, and references to supplementary material
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the supplied text
- **Shared manuscript claim summary** The authors use atomistic MD simulations of FUS-LCD to show that protein dynamics in condensates are heterogeneously slowed relative to dilute solution, with large-scale motions (translational diffusion, backbone reorientation) more strongly affected than small-scale motions (Cα distance fluctuations, side-chain rotamer jumps), and that hydration water dynamics are modestly slowed.
- **Visible evidence base** Main text equations (1–8), Figures 1–4 (described in text), Figures S1–S9 (referenced), experimental comparisons from cited literature
- **Missing materials affecting confidence** Actual figure data, simulation parameters (force field, water model, system size, simulation length, number of replicas), convergence criteria, error bars, and full supplementary information

## Reviewer

- **Overall assessment** The manuscript addresses a timely and important question in the field of biomolecular condensates: how the dense condensate environment differentially affects protein dynamics across length and time scales. The authors present a clear conceptual framework and use appropriate simulation methodology. The central finding, that dynamic retardation is heterogeneous and scale-dependent, is plausible and consistent with prior work. However, the evidence as presented is incomplete in several respects. Key quantitative results are described without error estimates or convergence analysis, and the absence of simulation details prevents full assessment of technical soundness. The distinction between translational, orientational, and internal dynamics is well motivated, but the interpretation of the Cα–Cα distance fluctuation results as "local" motions requires more careful justification. The hydration water analysis is interesting but the connection to biological function is speculative. Overall, the core claim is likely correct but the current presentation does not fully establish it.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, liquid–liquid phase separation, intrinsically disordered proteins, and the physical chemistry of crowded environments. The results are also relevant to those interested in the coupling between protein dynamics and function in dense cellular compartments, and to computational biophysicists developing and applying MD simulations to condensed-phase systems.

- **Major strengths** The question is well posed and of broad interest. The use of atomistic MD simulations on a biologically relevant system (FUS-LCD) is appropriate. The analysis separates different dynamic modes (translational, orientational, internal, side-chain) in a systematic way. The comparison to experimental translational diffusion data adds credibility. The hydration water analysis extends the scope beyond protein dynamics alone. The writing is clear and the conceptual framing is accessible.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors report a translational diffusion coefficient of 0.26 × 10–3 nm2/ns from a linear fit to the MSD of the center of mass, and state this is within the range of experimental values.
- **Evidence pointer** Main text, Figure S2
- **Concern** The diffusion coefficient is derived from a single linear fit with no reported uncertainty, no description of the fitting range, and no assessment of whether the MSD is in the diffusive regime. For a polymer chain in a dense phase, subdiffusive behavior is common and the apparent diffusion coefficient can depend strongly on the time window used. The agreement with experiment may be fortuitous if the simulation is not long enough to reach the diffusive limit.
- **Why it matters** The translational diffusion coefficient is a key quantitative anchor for the entire manuscript. If the fitting procedure is not robust or the simulation is not converged, the central claim of "up to 2 orders of magnitude" slowdown is not reliable.
- **Resolution test** Provide the MSD curve with the fitting range indicated, report the statistical uncertainty (e.g., from block averaging or multiple replicas), and demonstrate that the MSD is linear in time over the fitted interval. If subdiffusive, state this explicitly and discuss implications.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that biexponential fits accurately describe the orientational and distance fluctuation autocorrelation functions, and that triexponential fits were not superior.
- **Evidence pointer** Main text, Figures S3–S6
- **Concern** The choice of fitting function and the assessment of fit quality are described only qualitatively. No fit parameters, residuals, or statistical comparison (e.g., AIC or BIC) are provided. The statement that "triexponential fits were not superior" is not supported by any quantitative criterion. For a study whose conclusions depend on comparing time scales between two conditions, the fitting procedure must be transparent and reproducible.
- **Why it matters** The time constants extracted from these fits are the primary quantitative output of the study. If the fitting is not robust, the reported slowdown factors (5–15 for reorientation, ~2 for side chains) are not trustworthy.
- **Resolution test** Provide the fit parameters for all reported time constants, include residuals or goodness-of-fit metrics, and justify the choice of biexponential over alternatives with a statistical test.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors conclude that side-chain rotamer dynamics are "not significantly slowed" in the condensate, with an average retardation of about 2-fold.
- **Evidence pointer** Main text, Figure 3
- **Concern** No error bars or statistical significance tests are reported for the side-chain correlation times. A 2-fold retardation may or may not be significant depending on the spread across residues and the uncertainty in the fits. The statement "not significantly slowed" is therefore not supported by the evidence presented. Additionally, the averaging over all side chains and dihedral angles may mask residue-specific or position-specific effects that could be biologically relevant.
- **Why it matters** The heterogeneity of the slowdown is a central claim. If the 2-fold retardation is within noise, the conclusion that small-scale motions are "less affected" is weakened.
- **Resolution test** Report per-residue or per-dihedral time constants with uncertainties, and perform a statistical comparison (e.g., a t-test or bootstrap) between dilute and condensate conditions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation
- **Claim pointer** The authors interpret the Cα–Cα distance fluctuation time scales as reflecting "local motions of the Cα atoms around their average positions" and use this to argue that these motions are not strongly affected by the condensate.
- **Evidence pointer** Main text, Figure 2D–F
- **Concern** The distance between two Cα atoms separated by n residues is not a purely local quantity for large n. For separations up to 162 residues, the distance fluctuation includes contributions from chain-level motions. The interpretation that these are "local" is only valid for small separations. The authors do not show how the time scales depend on the separation n, nor do they justify the interpretation across the full range.
- **Why it matters** The distinction between "local" and "large-scale" motions is central to the paper's conceptual framework. If the distance fluctuation analysis conflates different length scales, the conclusion about heterogeneous retardation is less clean.
- **Resolution test** Show the time scales as a function of separation n, and identify the range of n for which the motions are genuinely local. Discuss how the interpretation changes for larger separations.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors report that hydration water rotational dynamics are slowed by a factor of 2 in the condensate, while collective dipole relaxation is slowed by a factor of ~6.6 (101 ps vs 670 ps).
- **Evidence pointer** Main text, Figure 4
- **Concern** The definition of the protein hydration layer (within 0.5 nm of the protein surface) and the tracking of water molecules within this layer are described only briefly. It is unclear how the layer is defined for a dynamic protein surface, how long water molecules remain in the layer, and whether the results are sensitive to the layer thickness. The collective dipole relaxation time of 670 ps in the condensate is substantially longer than the single-molecule time, but the interpretation of this difference is not fully developed.
- **Why it matters** The hydration water analysis is presented as a significant extension of the work. If the layer definition or tracking procedure is not robust, the reported time scales are not reliable.
- **Resolution test** Provide details of the layer definition, the residence time distribution of water molecules in the layer, and a sensitivity analysis with respect to layer thickness.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states "large-amplitude motions being strongly slowed by up to 2 orders of magnitude" but does not specify which motions these are. The reader must read the main text to understand the distinction.
- **Required correction** Briefly specify in the abstract that translational diffusion and backbone reorientation are the affected motions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Simulation details
- **Evidence pointer** Main text, Methods (not provided)
- **Issue** No simulation parameters are given in the main text: force field, water model, temperature, pressure, box size, number of molecules, simulation length, equilibration protocol, and number of replicas are all absent.
- **Required correction** Add a Methods section or refer to the Supporting Information with full simulation details.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion of biological relevance
- **Evidence pointer** Main text, final paragraph
- **Issue** The statement that retained dynamics "might be important for the biological function of FUS" is speculative and not tied to any specific functional mechanism.
- **Required correction** Either remove or substantially qualify this speculation, or connect it to specific known functional roles of FUS dynamics.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Equation 1
- **Evidence pointer** Main text, Equation 1
- **Issue** The notation in Equation 1 is incomplete. The positions r_j(t) and r_j(0) are not explicitly defined as functions of time, and the averaging procedure is not fully specified.
- **Required correction** Define all symbols and specify the averaging procedure (over time origins, over molecules, etc.).

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Comparison to experiment
- **Evidence pointer** Main text, translational diffusion coefficient
- **Issue** The comparison to experimental values is made for the translational diffusion coefficient only. No comparison is made for the other dynamic quantities, which limits the validation of the simulation.
- **Required correction** If experimental data are available for side-chain dynamics or backbone reorientation in condensates, include a comparison. If not, state this explicitly.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1B
- **Evidence pointer** Main text, Figure 1B
- **Issue** The ratio R_i(t) is described as a function of N_i at selected lag times, but the selected lag times are not specified in the text.
- **Required correction** Specify the lag times used in Figure 1B.

## Risk / unsupported claims

- The claim that the translational diffusion coefficient is "within the range of experimental values" is not fully supported without error bars and fitting details.
- The claim that side-chain rotamer dynamics are "not significantly slowed" is unsupported without statistical testing.
- The interpretation of Cα–Cα distance fluctuations as "local" motions is not justified for all separations.
- The claim that the results "support the notion of a liquid-like character of the condensates" is not directly tested; the simulations do not measure macroscopic viscosity or material properties.
- The statement that the findings "might be transferable to other biocondensates" is speculative and not supported by comparative data.
- The hydration water analysis is presented without sufficient methodological detail to assess robustness.
- The connection between water dynamics and thermodynamic driving forces of condensate formation is speculative and not quantitatively developed.