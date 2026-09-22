## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods) as provided by the user. Figures and figure supplements are referenced but not directly viewable.
- **Assessment boundary** Scientific content, experimental logic, data interpretation, and technical soundness as inferable from the text. No assessment of formatting, grammar, or editorial fit.
- **Shared manuscript claim summary** The manuscript proposes that multiple polarity kinases (Pom1, Kin1, Shk1, and Pck1) phosphorylate the F-BAR protein Cdc15 on overlapping but distinct sites within its intrinsically disordered region, and that cumulative phosphorylation inhibits Cdc15 phase separation, membrane binding, and cytokinetic ring assembly. Dephosphorylation promotes liquid-liquid phase separation of Cdc15, which is proposed to be a mechanism underlying cytokinetic ring assembly.
- **Visible evidence base** Text descriptions of results from immunoblotting, in vitro kinase assays, mass spectrometry, phosphopeptide mapping, coarse-grained molecular dynamics simulations, in vitro LLPS assays, and live-cell fluorescence microscopy. Figure references are given but figures themselves are not available for direct inspection.
- **Missing materials affecting confidence** Figures, figure supplements, videos, and source data files are not provided. Statistical details (exact n, p-values, error bar definitions) are only partially described in the text. The simulation code is available at a GitHub repository but was not inspected.

## Reviewer
- **Overall assessment** This is a well-conceived and carefully executed study that addresses a significant question in cytokinesis: how phosphorylation by multiple polarity kinases regulates the F-BAR protein Cdc15. The combination of in vitro biochemistry, cell biology, and coarse-grained simulations provides a multi-pronged approach that strengthens the central hypothesis. The identification of Pck1 as a fourth Cdc15 kinase is a novel contribution. The phase separation data are compelling and add to a growing body of evidence that LLPS is important for cytokinetic ring assembly. However, several concerns regarding the quantitative rigor of the imaging data, the interpretation of the simulation results, and the directness of the in vivo evidence for phase separation need to be addressed before the case is fully established.
- **Who would be interested in the results, and why** Cell biologists studying cytokinesis, the cytoskeleton, and membrane-cytoskeleton interactions. Researchers interested in the role of intrinsically disordered proteins and phase separation in cellular organization. The work is also relevant to those studying kinase signaling networks and how multisite phosphorylation regulates protein function.
- **Major strengths**
  1. The study systematically identifies and compares the contributions of four polarity kinases to Cdc15 phosphorylation, providing a comprehensive view of the regulatory network.
  2. The combination of experimental approaches (biochemistry, cell biology, and simulation) is powerful and mutually reinforcing.
  3. The in vitro LLPS experiments are well-designed, with appropriate controls (e.g., phosphomimetic mutants, binding partner recruitment).
  4. The observation that Cdc15 phosphomutants form cortical condensates in cells that recruit other CR components is a significant finding that links the in vitro observations to in vivo function.
  5. The manuscript is clearly written and the logic is easy to follow.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength / quantitative rigor
- **Claim pointer** The claim that "the number of sites correlated with each kinases' abilities to influence Cdc15 PM localization" and the quantitative comparisons of Cdc15 localization between different kinase mutants and phosphomutants.
- **Evidence pointer** Figure 5A, Figure 5—figure supplement 1A and 1B, Figure 4A and 4B. Location not provided for specific data points.
- **Concern** The text describes that the PM-to-cytoplasmic ratio of mNG-Cdc15 increases when kinases are inhibited and that this increase correlates with the number of phosphorylation sites targeted by each kinase. However, the statistical analysis and effect sizes are not described in the text. It is unclear how many cells were analyzed, whether the differences are statistically significant, and what the magnitude of the changes is. Similarly, for the phosphomutant localization data (Figure 5B), the text mentions a "significant jump" between 11A and 22A mutants, but the statistical test and p-values are not provided. Without this information, it is difficult to assess the robustness of the correlation and the significance of the threshold effect.
- **Why it matters** The correlation between phosphorylation site number and localization is a key piece of evidence supporting the model that cumulative phosphorylation is the primary regulatory mechanism. If the quantitative differences are small or not statistically robust, the model is weakened. The threshold effect is also a central claim that needs strong quantitative support.
- **Resolution test** Provide the statistical details for the localization measurements, including the number of cells analyzed, the statistical test used, and the p-values for the relevant comparisons. Show the distribution of the data (e.g., scatter plots) rather than just bar graphs. For the threshold effect, perform a statistical test that specifically compares the 11A and 22A mutants and report the effect size.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / interpretation of simulations
- **Claim pointer** The claim that "simulations indicated that the overall negative charge of phosphorylation masks positively charged amino acids necessary for F-BAR oligomerization and membrane interaction" and the related claim that "cumulative IDR phosphorylation moves the IDRs of a dimer apart and toward the F-BAR tips."
- **Evidence pointer** Figure 6, Figure 6—figure supplements 1-5. Location not provided for specific simulation parameters.
- **Concern** The simulation results are used to support a mechanistic model, but the text does not provide sufficient detail to evaluate the robustness of the findings. Specifically, the simulations were performed with two different coarse-grained models (HPS and KH D), and the text notes that the KH D model did not fully equilibrate. This is a significant caveat. The text also does not describe how the "masking" of positive charges was assessed in the simulations. Was this a direct calculation or an inference from the observed conformational changes? The relationship between the simulated conformational changes and the experimentally observed inhibition of membrane binding and oligomerization is not made explicit.
- **Why it matters** The simulations are a key part of the paper's mechanistic model. If the simulation results are not robust or the interpretation is not well-supported, the model is weakened. The lack of equilibration in the KH D model is a particular concern, as it suggests the results may depend on the choice of model and initial conditions.
- **Resolution test** Provide more detail on the simulation analysis, including how the "masking" of positive charges was quantified. Discuss the implications of the lack of equilibration in the KH D model. Show that the key conclusions are robust to the choice of model and initial conditions. If possible, perform additional simulations or analyses to directly test the proposed mechanism.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Evidence strength / in vivo relevance
- **Claim pointer** The claim that "Cdc15 phosphomutants also formed cortical condensates that recruited other CR components within cells" and the implication that these condensates are analogous to the in vitro droplets and represent a mechanism for CR assembly.
- **Evidence pointer** Figure 10, Figure 9—videos 1 and 2. Location not provided.
- **Concern** The text describes that Cdc15 phosphomutants form cortical condensates that recruit Fic1 and Rlc1. However, it is not clear whether these condensates are truly liquid-like in cells. The text mentions "apparent fission and fusion events," but this is qualitative. The relationship between these condensates and the normal process of CR assembly is also not fully explored. Do these condensates form at the correct time and place? Are they functional, or are they aberrant aggregates? The text does not address whether the condensates are reversible or whether they interfere with normal cell division.
- **Why it matters** The in vivo relevance of the phase separation mechanism is a key claim of the paper. If the condensates are not truly liquid-like or are not functionally relevant to CR assembly, the significance of the in vitro observations is diminished.
- **Resolution test** Provide more quantitative analysis of the condensate dynamics (e.g., FRAP in cells, tracking of fusion/fission events). Address whether the condensates form at the correct time and place during the cell cycle. Test whether the condensates are functional by, for example, examining whether they can recruit other CR components in a dynamic manner or whether their formation is required for CR assembly.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness / in vitro kinase assays
- **Claim pointer** The claim that Pck1 is a direct kinase of Cdc15 and the identification of its phosphorylation site(s).
- **Evidence pointer** Figure 2, Figure 2—figure supplement 1, Figure 3, Figure 3—figure supplement 3. Location not provided.
- **Concern** The text states that Pck1 phosphorylates Cdc15 on a single major site (S668). However, the evidence for this is not described in detail. It is unclear how the site was identified (e.g., by mass spectrometry of a phosphopeptide, by mutagenesis of candidate sites, or by a combination). The text also does not state whether the in vitro phosphorylation by Pck1 was confirmed to be direct (i.e., no other kinase present in the assay). The stoichiometry of phosphorylation is also not described.
- **Why it matters** The identification of Pck1 as a new Cdc15 kinase is a novel finding. The rigor of the site identification is important for the validity of the phosphomutant studies that rely on mutating these sites.
- **Resolution test** Provide a clear description of how the Pck1 phosphorylation site was identified. Show that the phosphorylation is direct (e.g., using a kinase-dead Pck1 or a highly purified kinase preparation). Provide evidence for the stoichiometry of phosphorylation.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, last sentence
- **Issue** The abstract states "a threshold of Cdc15 phosphorylation by assorted kinases prevents Cdc15 condensation on the PM and antagonizes CR assembly." The term "threshold" is used, but the concept of a threshold is not clearly defined in the abstract. It is also not clear if this threshold is a specific number of phosphorylation events or a more general concept.
- **Required correction** Clarify what is meant by "threshold" in the abstract. For example, "a critical level of phosphorylation" or "a minimum number of phosphorylation events."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity / completeness
- **Affected element** Results section, "Multiple polarity kinases modulate Cdc15 phosphostatus"
- **Evidence pointer** Figure 1, location not provided
- **Issue** The text describes the use of analog-sensitive kinase alleles and inhibitors, but it is not clear whether the inhibitors were used at concentrations that fully inhibit the kinases. The text also does not describe the specificity of the inhibitors.
- **Required correction** Provide a brief statement about the inhibitor concentrations and specificity, or refer to the Materials and methods for details.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion, paragraph 3
- **Issue** The discussion speculates about the role of phase separation in CR assembly but does not fully address alternative models. For example, the text states that "initial Cdc15 condensates develop into more stable structures if assembled with Mid1 or other proteins," but it is not clear how this would be tested.
- **Required correction** Briefly mention alternative models and how the proposed model could be distinguished experimentally.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Materials and methods, "Coarse-grained molecular dynamics simulations"
- **Evidence pointer** Materials and methods, location not provided
- **Issue** The text describes the simulation models but does not provide the force field parameters or the simulation length. This makes it difficult to reproduce the simulations.
- **Required correction** Provide the force field parameters and simulation length, or refer to a previous publication where these are described.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 4
- **Evidence pointer** Figure 4C and 4D, location not provided
- **Issue** The text describes that cdc15-31A cells have altered cytokinesis dynamics, with shorter maturation and constriction periods. However, it is not clear whether these differences are statistically significant.
- **Required correction** Report the statistical test and p-values for the comparisons of cytokinesis timing.

## Risk / unsupported claims
- The claim that "the number of sites correlated with each kinases' abilities to influence Cdc15 PM localization" is not fully supported by the quantitative data presented in the text. The correlation is described qualitatively, and the statistical significance is not reported.
- The claim that "simulations indicated that the overall negative charge of phosphorylation masks positively charged amino acids necessary for F-BAR oligomerization and membrane interaction" is an interpretation of the simulation results that is not directly demonstrated. The text does not describe how the "masking" was assessed.
- The claim that "Cdc15 phosphomutants also formed cortical condensates that recruited other CR components within cells" is supported by the data, but the functional significance of these condensates is not fully established. It is not clear whether they are required for CR assembly or are a consequence of it.
- The claim that "a threshold of Cdc15 phosphorylation by assorted kinases prevents Cdc15 condensation on the PM" is a central hypothesis, but the existence of a specific threshold is not directly tested. The data show a correlation between phosphorylation level and localization, but a threshold implies a nonlinear response that is not explicitly demonstrated.