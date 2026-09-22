## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, materials and methods, and author contributions.
- **Assessment boundary** Scientific validity of the claims, technical soundness of the experimental and computational approaches, and alignment with the stated conclusions. Editorial or stylistic aspects are considered only where they affect clarity or interpretability.
- **Shared manuscript claim summary** The authors report that disease-linked C-terminal hyperphosphorylation of TDP-43, mimicked by CK1δ phosphorylation in vitro or by S-to-D phosphomimetic mutations, suppresses TDP-43 phase separation and aggregation, promotes liquid-like and dynamic condensate properties, and does not impair nuclear import or RNA regulatory functions. Multi-scale molecular dynamics simulations attribute this effect to enhanced solvation of phosphomimetic residues reducing homotypic TDP-43 low-complexity domain interactions. The authors speculate that hyperphosphorylation may be a protective cellular response against TDP-43 aggregation.
- **Visible evidence base** In vitro phase separation assays (turbidity, sedimentation, microscopy), FRAP and fusion experiments, in vitro aggregation assays with SDD-AGE, phosphomimetic mutants (2D, 5D, 12D and corresponding A controls), CK1δ phosphorylation experiments, mass spectrometry of phosphorylation sites, coarse-grained and atomistic MD simulations, cellular assays in HeLa, U2OS and primary rat neurons including nuclear import, RNA binding, splicing, solubility fractionation, and filter trap assays.
- **Missing materials affecting confidence** The manuscript text provided does not include the main figures, supplementary figures, or tables referenced (e.g., Fig 1, Fig 2, Fig 3, Fig EV1–EV5, Appendix Figs S1–S8, Appendix Table S1). Movies EV1–EV5 are also not accessible. Quantitative data, statistical details, and exact numerical values for several assays are therefore not directly verifiable from the provided material.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question regarding the role of TDP-43 C-terminal hyperphosphorylation, a hallmark of ALS/FTD pathology, in modulating phase separation and aggregation. The authors present a coherent set of in vitro, in silico, and cellular experiments that collectively support a counterintuitive conclusion: hyperphosphorylation suppresses, rather than promotes, TDP-43 condensation and aggregation. The combination of experimental and computational approaches is a notable strength, and the findings have potential implications for understanding disease mechanisms and therapeutic strategies. However, the provided material lacks the actual figures and quantitative data, which limits the ability to fully assess the robustness of the evidence. Several technical details and potential alternative interpretations require clarification before the case is fully established.
- **Who would be interested in the results, and why** Researchers in the fields of neurodegeneration (ALS, FTD, Alzheimer's disease), RNA-binding protein biology, liquid-liquid phase separation, and post-translational modification biology. The findings challenge the prevailing assumption that TDP-43 hyperphosphorylation is a driver of aggregation and may inform the development of kinase inhibitors or other therapeutic approaches. The multi-scale simulation approach will also be of interest to computational biologists studying biomolecular condensates.
- **Major strengths**
  1. The study combines multiple orthogonal approaches (in vitro biochemistry, cell biology, and multi-scale MD simulations) to address a central question, providing a comprehensive and compelling narrative.
  2. The use of both CK1δ-mediated phosphorylation and phosphomimetic mutations strengthens the relevance of the findings to the disease state.
  3. The inclusion of cellular assays demonstrating preserved nuclear import and RNA regulatory functions of phosphomimetic TDP-43 adds functional context and addresses potential off-target effects.
  4. The multi-scale simulation strategy, from coarse-grained to atomistic, is sophisticated and provides mechanistic insight at the molecular level.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence robustness
  - **Claim pointer** The authors claim that CK1δ-mediated hyperphosphorylation or phosphomimetic mutations reduce TDP-43 phase separation and aggregation, and render condensates more liquid-like and dynamic.
  - **Evidence pointer** Figures 1, 2, and EV1–EV3; location not provided in the text.
  - **Concern** The central quantitative data supporting the phase separation and aggregation claims (e.g., turbidity curves, sedimentation ratios, condensate size/distribution, FRAP recovery curves, fusion event frequencies, SDD-AGE blots) are not visible in the provided material. Without these data, the magnitude and statistical significance of the reported effects cannot be assessed.
  - **Why it matters** The core conclusion of the manuscript rests on the robustness of these quantitative measurements. If the effects are small or variable, the interpretation that hyperphosphorylation suppresses condensation and aggregation would be weakened.
  - **Resolution test** Provide the main and supplementary figures with full quantitative analysis, including statistical tests, error bars, and sample sizes for all key experiments.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Mechanistic interpretation
  - **Claim pointer** The authors state that multi-scale MD simulations reveal reduced homotypic interactions of TDP-43 low-complexity domains through enhanced solvation of phosphomimetic residues.
  - **Evidence pointer** Figure 3, EV3, Appendix S4–S5, Appendix Table S1; location not provided in the text.
  - **Concern** The simulation results are described qualitatively in the text, but the specific data supporting the "enhanced solvation" mechanism (e.g., radial distribution functions, solvent-accessible surface area, interaction energy decompositions, density profiles) are not shown. The claim that reduced interactions are due to solvation, as opposed to other electrostatic or steric effects, requires direct evidence from the simulations.
  - **Why it matters** The proposed molecular mechanism is a key part of the paper's explanatory framework. Without clear simulation data, the mechanism remains speculative.
  - **Resolution test** Present the relevant simulation analyses, including quantitative comparisons of interaction energies, solvation free energies, and contact maps between wild-type and phosphomimetic/phosphorylated systems.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Generalizability
  - **Claim pointer** The authors speculate that TDP-43 hyperphosphorylation may be a protective cellular response to counteract TDP-43 aggregation.
  - **Evidence pointer** Discussion section; location not provided.
  - **Concern** The speculation is based on in vitro and overexpression cell models. The manuscript does not address whether endogenous hyperphosphorylation in disease tissue occurs on soluble, diffuse TDP-43 or only on aggregated, insoluble TDP-43. If hyperphosphorylation is primarily found on aggregates, the protective role would be questionable.
  - **Why it matters** The clinical relevance of the findings depends on the timing and context of hyperphosphorylation in the disease process. The current data do not resolve this.
  - **Resolution test** Discuss and ideally provide data on the temporal relationship between phosphorylation and aggregation in disease models or patient tissue, or temper the speculation accordingly.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Technical detail
  - **Affected element** In vitro phosphorylation
  - **Evidence pointer** Methods, "In vitro phosphorylation"; location not provided.
  - **Issue** The stoichiometry of CK1δ-mediated phosphorylation is not described. It is unclear how many of the 12 potential sites are phosphorylated under the experimental conditions.
  - **Required correction** Provide mass spectrometry data or a quantitative estimate of phosphorylation stoichiometry to support the claim of "hyperphosphorylation."
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical detail
  - **Affected element** Phosphomimetic validation
  - **Evidence pointer** Results, "C-terminal phosphomimetic substitutions"; location not provided.
  - **Issue** The authors use S-to-D mutations as phosphomimetics but do not validate that these mutations accurately mimic the structural and electrostatic effects of true phosphorylation, particularly regarding the dianionic charge of a phosphate group.
  - **Required correction** Acknowledge this limitation and, if possible, include a comparison with a phosphoserine-containing peptide or a more accurate mimic.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Data presentation
  - **Affected element** Cellular solubility assays
  - **Evidence pointer** Figure 6; location not provided.
  - **Issue** The text states that 12D enhances solubility, but the quantification of the S/(S+I) ratio and the statistical analysis are not shown in the provided material.
  - **Required correction** Include the quantitative data and statistical analysis for the solubility fractionation experiments.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Discussion of conflicting literature
  - **Evidence pointer** Discussion; location not provided.
  - **Issue** The authors mention conflicting studies on the role of phosphorylation but do not discuss them in detail. A more thorough comparison would help contextualize the findings.
  - **Required correction** Expand the discussion to address specific conflicting studies and potential reasons for discrepancies.
- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Lack of visible quantitative data for key in vitro and cellular experiments.
  - R1-M2: Insufficient direct evidence from simulations to support the proposed solvation mechanism.
- **Assessment against Nature-style criteria**
  - **Originality** High. The finding that hyperphosphorylation suppresses TDP-43 condensation and aggregation challenges the prevailing view and offers a new perspective on the role of this PTM.
  - **Scientific importance** High. TDP-43 pathology is central to ALS/FTD, and understanding the molecular determinants of its aggregation is of significant clinical relevance.
  - **Interdisciplinary readership** Moderate to high. The topic bridges cell biology, biophysics, and computational biology, and the findings are likely to appeal to a broad audience interested in neurodegeneration and phase separation.
  - **Technical soundness** The experimental design is generally sound, but the lack of visible quantitative data and the incomplete validation of the phosphomimetic approach are concerns. The multi-scale simulation strategy is appropriate, but the mechanistic conclusions require stronger direct evidence.
  - **Readability for nonspecialists** The manuscript is well-written and logically structured, with clear explanations of the concepts. The abstract and introduction are accessible, though the methods and results sections assume some familiarity with the field.
- **Recommendation posture** Supportive if technical concerns are resolved. The central hypothesis is interesting and the multi-pronged approach is commendable. However, the current evidence base, as presented in the provided material, is insufficient to fully establish the claims. The authors must provide the missing quantitative data and strengthen the mechanistic evidence from simulations.

## Risk / unsupported claims
- The claim that hyperphosphorylation suppresses TDP-43 aggregation in a disease-relevant context is not fully supported, as the cellular models rely on overexpression and the relationship to endogenous disease processes is not established.
- The speculation that hyperphosphorylation is a protective cellular response is not directly tested and remains a hypothesis.
- The claim that phosphomimetic mutations do not affect RNA regulatory functions is based on a limited set of assays (autoregulation and two splicing targets) and may not be generalizable.
- The quantitative extent of the "liquid-like" behavior of phosphomimetic condensates, as opposed to wild-type, is not verifiable without the FRAP and fusion data.