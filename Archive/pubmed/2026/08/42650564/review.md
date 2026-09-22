## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the provided manuscript
- **Shared manuscript claim summary** The study investigates binding interactions between two milk proteins (β-casein and β-lactoglobulin) and two flavonoids (catechin and naringin) using spectroscopic, computational, and electronic tongue methods, and reports that both proteins reduce bitterness- and astringency-related sensor responses, with β-CN showing greater attenuation than β-LG.
- **Visible evidence base** Abstract, Introduction, Materials and Methods, Results and Discussion, Conclusions, figure captions referenced in text, Table 1 and Table 2 mentioned
- **Missing materials affecting confidence** Actual figures and tables (data values), raw spectra, electronic tongue sensor output values, docking pose coordinates, statistical output tables, supplementary materials

## Reviewer
- **Overall assessment** The manuscript presents a systematic multi-technique investigation of milk protein-flavonoid interactions with a practical focus on taste masking. The experimental design is logical and the combination of spectroscopic, computational, and sensory-analytical methods is appropriate for the research question. However, the study has several limitations that affect the strength of the conclusions. The absence of quantitative binding parameters (e.g., binding constants from fluorescence quenching analysis), the lack of protein-only controls in electronic tongue measurements, and the purely descriptive integration of structural and sensory data limit the mechanistic claims. The manuscript is technically sound in its execution but falls short of establishing a definitive structure-function relationship between protein-flavonoid binding and taste modulation. The work is of interest to researchers in food chemistry and formulation science, but the conclusions are somewhat overstated relative to the evidence presented.

- **Who would be interested in the results, and why** Researchers in food science, particularly those working on flavor modulation, protein-polyphenol interactions, and functional beverage development. The study is also relevant to the growing field of plant-based ingredient utilization in dairy products. The electronic tongue methodology and the comparative analysis of two structurally distinct proteins provide useful reference data for formulation scientists. The pandan context adds value for researchers working on tropical food ingredients.

- **Major strengths** The multi-technique approach provides complementary perspectives on protein-flavonoid interactions. The selection of two structurally contrasting flavonoids and two proteins with different conformational properties is well reasoned. The authors are appropriately cautious in several places, acknowledging limitations such as the absence of flavonoid background subtraction in UV-Vis and the computational nature of docking results. The electronic tongue data address a practical gap in the literature, which has largely focused on binding parameters rather than sensory outcomes. The exploratory integration analysis is appropriately framed as descriptive rather than inferential.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Quantitative binding analysis
  - **Claim pointer** The manuscript claims that fluorescence quenching indicates interactions between flavonoids and milk proteins, and the abstract states that β-CN exhibited "more pronounced interaction-related spectroscopic responses than β-LG."
  - **Evidence pointer** Section 3.4, Figure 4
  - **Concern** Fluorescence quenching data are presented qualitatively (intensity decreases and wavelength shifts) without quantitative analysis. The Stern-Volmer quenching constant, binding constant (Ka), and number of binding sites (n) are not reported, despite these being standard parameters derivable from the titration data described in the methods. Without these values, the claim of "more pronounced" interaction for β-CN is not quantitatively supported. Additionally, the type of quenching (static vs. dynamic) is not established, which is essential for interpreting the binding mechanism.
  - **Why it matters** The central mechanistic claim of the paper depends on demonstrating differential binding affinity between the two proteins. Qualitative spectral changes cannot distinguish between binding affinity differences and other effects such as inner filter artifacts or protein aggregation. Quantitative binding parameters are the field-standard evidence for interaction strength and would substantially strengthen the structure-function interpretation.
  - **Resolution test** Provide Stern-Volmer plots, calculated Ka and n values for all four protein-flavonoid combinations, and a statement on quenching mechanism (e.g., from temperature-dependent measurements or lifetime data). If Ka values cannot be reliably calculated, state this explicitly and temper the comparative claims accordingly.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Electronic tongue experimental design
  - **Claim pointer** The manuscript claims that "the addition of the milk proteins reduced the bitterness- and astringency-related sensor responses of catechin and naringin" and that "β-CN produced greater attenuation of these responses than β-LG."
  - **Evidence pointer** Section 3.7, electronic tongue data
  - **Concern** The electronic tongue measurements compare free flavonoid solutions to protein-flavonoid complexes, but no protein-only controls are reported. Without measuring the sensor response to β-CN and β-LG alone, it is impossible to determine whether the reduced bitterness/astringency signals are due to specific binding interactions or simply to the presence of protein altering the sensor membrane response through non-specific effects (e.g., fouling, charge effects, competitive adsorption). The manuscript acknowledges this limitation in the conclusions but still presents the attenuation as a binding-related effect in the results and abstract.
  - **Why it matters** The practical claim of taste masking is the most translational aspect of the study. If the sensor response reduction is not specifically attributable to protein-flavonoid complexation, the formulation implications are weakened. The absence of protein-only controls undermines the causal interpretation.
  - **Resolution test** Include electronic tongue measurements of β-CN and β-LG alone at the same concentrations used in the complex samples. If protein-only responses are non-negligible, subtract them or discuss the implications. Alternatively, perform a competitive binding experiment or use a different sensory validation approach.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Structural interpretation of CD data
  - **Claim pointer** The manuscript states that for β-CN, catechin "increased the estimated α-helix fraction from 22.3% to 24.4-25.0% and decreased the total β-sheet fraction from 42.3% to 39.0-39.2%," and interprets this as ligand-induced conformational change.
  - **Evidence pointer** Section 3.3, Table 2
  - **Concern** The CD-derived secondary structure estimates for β-CN are surprising given that β-CN is described as an intrinsically disordered protein. The reported values of 42.3% β-sheet and 22.3% α-helix for the control are inconsistent with the expected predominantly random coil structure of an IDP. The manuscript notes that β-CN shows a "pronounced negative ellipticity centered at approximately 200 nm, which is characteristic of intrinsically disordered proteins," yet the CDNN estimates suggest a highly structured protein. This discrepancy is not addressed. The choice of analysis range (195-260 nm for β-CN vs. 190-260 nm for β-LG) may introduce artifacts, and the reliability of CDNN for IDPs is questionable.
  - **Why it matters** The structural interpretation forms part of the mechanistic narrative. If the secondary structure estimates are unreliable for β-CN, the claims about ligand-induced conformational changes in this protein are not well supported. The discrepancy between the spectral signature and the deconvolution results needs explanation.
  - **Resolution test** Provide a critical discussion of CDNN limitations for intrinsically disordered proteins. Consider using alternative analysis methods (e.g., BeStSel, SELCON3) or explicitly state the uncertainty in the estimates. If the estimates are not reliable, temper the structural claims and focus on the qualitative spectral changes.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Docking methodology and interpretation
  - **Claim pointer** The manuscript reports AutoDock Vina scores of -5.2, -6.1, -6.1, and -7.4 kcal/mol for β-CN-C, β-CN-NAR, β-LG-C, and β-LG-NAR, respectively, and interprets these as indicating "protein- and ligand-dependent differences in predicted interaction favorability."
  - **Evidence pointer** Section 3.6, Figure 7
  - **Concern** The docking methodology has several limitations that are not fully addressed. First, the use of a predicted AlphaFold structure for β-CN, an intrinsically disordered protein, is problematic because IDPs do not have a single stable conformation, and docking to a single predicted structure may not represent the relevant binding conformations. Second, the search space definition is described vaguely ("defined around the potential ligand-binding regions"), which affects reproducibility. Third, the manuscript does not report whether multiple docking runs were performed, how convergence was assessed, or whether the top-ranked poses were consistent across runs. Fourth, the comparison of scores across different proteins is not statistically validated.
  - **Why it matters** The docking results are used to support the binding mechanism narrative. If the methodology is not robust, the specific interaction patterns (hydrogen bonds, hydrophobic contacts) reported may not be reliable. The authors do appropriately caution that Vina scores are computational estimates, but the presentation of specific residue-level interactions implies a level of confidence that may not be warranted.
  - **Resolution test** Provide more detail on docking protocol (search space dimensions, exhaustiveness, number of runs). Acknowledge the limitations of docking to a single IDP conformation. Consider ensemble docking or molecular dynamics simulations to account for protein flexibility. If not feasible, present the docking as purely exploratory and de-emphasize specific residue interactions.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Reproducibility of methods
  - **Affected element** Section 2.2, sample preparation
  - **Evidence pointer** Section 2.2
  - **Issue** The manuscript states that flavonoid stock solutions were prepared in DMSO and diluted with PBS, with final DMSO concentration maintained at ≤5% (v/v). However, the exact DMSO concentration in the final measurement samples is not specified, and the effect of 5% DMSO on protein conformation or flavonoid solubility is not discussed. Additionally, the incubation time of 30 min is stated as "a minimum," but the actual incubation time used is not reported.
  - **Required correction** Specify the exact DMSO concentration in all samples and provide justification for its use. Report the precise incubation time and temperature. Consider including a DMSO-only control for spectroscopic measurements.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Data presentation
  - **Affected element** Table 2
  - **Evidence pointer** Section 3.3, Table 2
  - **Issue** The manuscript states that "the data in Table 2 were reported descriptively and were not subjected to inferential statistical analysis." However, it is unclear whether the secondary structure percentages are from a single measurement or averaged from replicates. If replicates were performed, standard deviations should be reported.
  - **Required correction** Clarify the number of replicates for CD measurements and report standard deviations for the secondary structure estimates. If only single measurements were performed, state this explicitly.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Terminology consistency
  - **Affected element** Throughout
  - **Evidence pointer** Abstract, Sections 3.1-3.7
  - **Issue** The manuscript uses "polyphenol" and "flavonoid" interchangeably in several places. While catechin and naringin are both flavonoids and thus polyphenols, the inconsistent terminology may confuse readers. Additionally, the term "taste-masking" is used in the title and abstract, but the electronic tongue measures sensor responses, not human taste perception. The manuscript does acknowledge this distinction in the conclusions, but the title may overstate the findings.
  - **Required correction** Standardize terminology throughout. Consider whether the title should be revised to reflect that the study measures sensor responses rather than human taste perception, or add a qualifier such as "sensor-based taste assessment."

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Literature context
  - **Affected element** Introduction
  - **Evidence pointer** Section 1
  - **Issue** The introduction cites literature on milk protein-polyphenol interactions but does not provide a critical comparison with previous studies that have reported binding constants or structural changes for similar systems. The novelty of the present work is asserted but not clearly positioned against existing quantitative data.
  - **Required correction** Add a brief comparison with key previous studies, noting how the present work extends or differs from them. If quantitative binding data exist for similar systems, discuss how the present findings compare.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Figure quality and accessibility
  - **Affected element** Figures 1-8
  - **Evidence pointer** Figure legends referenced in text
  - **Issue** The figure legends are not provided in the manuscript text, making it difficult to assess the completeness of the figure descriptions. Additionally, the manuscript references "Figure 7a-d" for docking poses but does not describe the visualization parameters (e.g., distance cutoffs for hydrogen bonds, surface representations).
  - **Required correction** Ensure figure legends are complete and self-explanatory. For docking figures, specify the criteria used to identify hydrogen bonds and other interactions.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Absence of quantitative fluorescence quenching analysis (Stern-Volmer constants, binding constants)
  - R1-M2: Missing protein-only controls in electronic tongue experiments
  - R1-M3: Unresolved discrepancy between CD spectral signature and secondary structure estimates for β-CN
  - R1-M4: Incomplete docking methodology details and lack of statistical validation

## Risk / unsupported claims
- The claim that β-CN exhibits "more pronounced interaction-related spectroscopic responses than β-LG" is not quantitatively supported without binding constants or other quantitative metrics.
- The claim that milk proteins "effectively reduce" bitterness and astringency is based solely on electronic tongue sensor responses without protein-only controls or human sensory validation.
- The interpretation of specific residue-level interactions from docking (e.g., Asn22, Ser37 for β-CN-NAR) is not robust given the use of a single predicted structure for an intrinsically disordered protein.
- The statement that "β-LG-NAR2 showed the highest standardized apparent reductions in bitterness and astringency" is based on a descriptive analysis of only four formulations and should not be presented as a robust ranking.
- The structural interpretation of CD data for β-CN (α-helix increase from 22.3% to 24.4-25.0%) is questionable given the unreliability of CD deconvolution for intrinsically disordered proteins.
- The manuscript's title claims a "binding mechanism" is revealed, but the study does not provide direct evidence of binding stoichiometry, affinity, or site-specific interactions beyond computational predictions.