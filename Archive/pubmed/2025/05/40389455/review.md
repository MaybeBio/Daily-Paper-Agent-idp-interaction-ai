## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary information descriptions.
- **Assessment boundary** Scientific validity, methodological rigor, clarity of claims, and alignment with stated conclusions. No assessment of editorial fit or publication decision.
- **Shared manuscript claim summary** The authors present coarse-grained molecular dynamics simulations combined with Monte Carlo phosphorylation steps to study how the kinase CK1δ phosphorylates the disordered protein TDP-43, both in dilute solution and in condensates. They introduce a Markov state model approach to validate thermodynamic consistency of their non-equilibrium simulations, and report that C-terminal serines are preferentially phosphorylated, that phosphorylation facilitates CK1δ binding, and that hyperphosphorylation dissolves TDP-43 condensates.
- **Visible evidence base** Full text with figures referenced (Figs. 1–5), methods section, and descriptions of supplementary materials. No supplementary files, source data, or movies were provided for direct inspection.
- **Missing materials affecting confidence** Supplementary figures, tables, notes, movies, and source data are referenced but not available. This limits verification of statistical analyses, model validation details, and simulation parameters.

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question: how enzymatic phosphorylation of disordered proteins is modulated by sequence and by condensation. The methodological contribution, using Markov state models to validate thermodynamic consistency of chemically driven coarse-grained simulations, is potentially valuable and broadly applicable. The biological findings, particularly the preferential phosphorylation of C-terminal serines and the dissolution of condensates upon hyperphosphorylation, are interesting and consistent with experimental observations. However, the evidence presented in the main text is largely descriptive, and several key claims rely on analyses whose details are only in the supplementary material. The causal link between phosphorylation and condensate dissolution, while plausible, is not rigorously established from the data shown. The manuscript is well-written and accessible, but the depth of validation and the strength of some conclusions need reinforcement.

- **Who would be interested in the results, and why** Researchers in computational biophysics, specifically those studying intrinsically disordered proteins, biomolecular condensates, and non-equilibrium simulation methods. The Markov state model validation approach will interest method developers. Biologists studying TDP-43 phosphorylation, neurodegeneration, and post-translational modifications in condensates will find the biological predictions relevant. The work bridges a gap between simulation methodology and biological hypothesis generation.

- **Major strengths**
  1. The introduction of a generalizable Markov state model approach to verify thermodynamic consistency in chemically driven simulations is a significant methodological advance.
  2. The study addresses a biologically important and unresolved question: how kinases interact with disordered proteins and condensates.
  3. The use of multiple simulation variants (different force fields, sequence modifications) strengthens the robustness of the qualitative findings.
  4. The writing is clear and the figures are informative, making the work accessible to a broad readership.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that their Markov state model approach can validate the thermodynamic consistency of chemically driven simulations, and that the dissipated heat per cycle equals the applied chemical potential difference.
- **Evidence pointer** Figure 2f, Methods section "Thermodynamic consistency validation simulations"
- **Concern** The validation is performed only for a single-enzyme, single-substrate system with one reactive serine. The authors show agreement between Δμcycle and ΔμP for six different serines, but the statistical power and the range of conditions tested are limited. The method's general applicability to multi-chain condensate systems, where many-body effects and crowding could alter the kinetics, is not demonstrated. The authors do not show that the Markov state model remains valid in the condensate simulations, where the assumption of memoryless transitions may break down.
- **Why it matters** The central methodological claim is that this validation approach is "generally applicable." Without demonstrating its performance in the more complex condensate systems where it is actually used, the claim is not fully supported. If the thermodynamic consistency is not verified in the condensate simulations, the quantitative results from those simulations may be unreliable.
- **Resolution test** The authors should apply the Markov state model validation to the condensate simulations, or at least to a system with multiple interacting chains, and show that the cycle relation holds. Alternatively, they should explicitly state the limitations of the validation and discuss how the lack of validation in condensates affects the interpretation of those results.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The authors claim that "hyperphosphorylation of TDP-43 leads to the dissolution of TDP-43 condensates" and that this is a key finding of the study.
- **Evidence pointer** Figure 4a, 4b, Results section "CK1δ phosphorylates TDP-43 in condensates"
- **Concern** The evidence for condensate dissolution is based on the percentage of chains in the largest cluster over time. However, the authors do not provide a quantitative measure of condensate size or stability beyond this metric. The dissolution could be an artifact of the simulation setup, such as the finite box size or the specific number of enzymes used. The authors also do not compare the dissolution kinetics to a control simulation without phosphorylation or with a non-phosphorylatable TDP-43 variant. The claim that dissolution is caused by phosphorylation, rather than by the mere presence of enzymes or by finite-size effects, is not rigorously established.
- **Why it matters** The biological relevance of the study hinges on this claim. If the dissolution is not robustly demonstrated, the significance of the work for understanding TDP-43 pathology is diminished. The claim is presented as a definitive result, but the evidence is suggestive rather than conclusive.
- **Resolution test** The authors should include control simulations (e.g., with catalytically inactive CK1δ or with TDP-43 lacking phosphorylation sites) to show that dissolution is specifically due to phosphorylation. They should also provide a more detailed analysis of condensate properties, such as density profiles or cluster size distributions over time, to support the dissolution claim.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "contact rates in equilibrium largely account for the phosphorylation rates" and that this correlation supports a simple kinetic model.
- **Evidence pointer** Figure 3c, 3d, Results section "C-terminus of TDP-43 is preferentially phosphorylated"
- **Concern** The correlation between contact rates and phosphorylation rates is reported as a Pearson correlation coefficient of 0.84, but the authors do not provide confidence intervals or a statistical test of significance. More importantly, the correlation is based on a small number of data points (14 serines), and the relationship may be driven by a few outliers. The authors also do not test whether the correlation holds in the condensate simulations, where the environment is different. The claim that contact rates "largely account" for phosphorylation rates is an overstatement given the limited analysis.
- **Why it matters** This correlation is used to argue that the phosphorylation pattern is determined by the sequence-specific interactions of TDP-43 with CK1δ. If the correlation is weak or not robust, the interpretation of the phosphorylation pattern becomes less clear. The authors should provide a more rigorous statistical analysis and test the predictive power of the contact rate model.
- **Resolution test** The authors should provide confidence intervals for the correlation coefficient and perform a permutation test or similar to assess significance. They should also show the correlation for the condensate simulations and discuss any discrepancies.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction, paragraph 4
- **Evidence pointer** Location not provided
- **Issue** The introduction discusses Markov state models and non-equilibrium steady states in a way that may be dense for readers not familiar with these concepts. The connection between the methodological innovation and the biological question could be made more explicit earlier.
- **Required correction** Consider adding a brief, plain-language explanation of why validating thermodynamic consistency is important for the credibility of the simulations, and how this relates to the biological question of phosphorylation in condensates.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, "Phosphorylation reaction through a Monte Carlo step"
- **Evidence pointer** Location not provided
- **Issue** The choice of the contact criterion (all three distances to Asp149, Phe150, Gly151 less than 1 nm) is not justified. The sensitivity of the results to this choice is not discussed.
- **Required correction** Provide a brief justification for the contact criterion and, if possible, a sensitivity analysis showing that the results are robust to reasonable variations in this parameter.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion, paragraph 2
- **Evidence pointer** Location not provided
- **Issue** The authors speculate on the biological implications of their findings for TDP-43 pathology, but the link between the simulation timescales and physiological timescales is not discussed. The reader is left wondering how the microsecond timescales of the simulations relate to the hours-to-days timescales of phosphorylation in cells.
- **Required correction** Add a brief discussion of the timescale limitations of the coarse-grained model and how the qualitative findings might extrapolate to physiological conditions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Figure 2f
- **Evidence pointer** Location not provided
- **Issue** The figure shows the relationship between Δμcycle and ΔμP, but the units and the meaning of the error bars are not fully explained in the caption.
- **Required correction** Clarify in the caption what the error bars represent and how the best-fit line was obtained.

## Risk / unsupported claims
- The claim that the Markov state model approach is "generally applicable" is not fully supported, as it is only validated in a single-enzyme, single-substrate system.
- The claim that hyperphosphorylation dissolves TDP-43 condensates is not rigorously established due to the lack of control simulations and the limited analysis of condensate properties.
- The claim that contact rates "largely account" for phosphorylation rates is an overstatement given the limited statistical analysis.
- The biological relevance of the findings, particularly the link to TDP-43 pathology, is speculative and not directly tested.
- The quantitative agreement between simulated phosphorylation patterns and experimental data is stated but not shown in the main text; the comparison is only qualitative.