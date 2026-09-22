## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and data availability statement.
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by presented evidence. Editorial or stylistic preferences are noted only where they affect comprehension.
- **Shared manuscript claim summary** The authors present an optical nanopore assay based on freestanding palladium zero-mode waveguides functionalized with the FG-nucleoporin Nsp1 to measure single-molecule transport. They report that Nsp1-coated pores exhibit significant selectivity for the transport receptor Kap95 over the inert probe BSA for pore diameters below approximately 55 nm, with selectivity gradually lost at larger diameters. Coarse-grained molecular dynamics simulations reproduce the experimental trend and attribute the loss of selectivity to the formation of a central channel in the Nsp1 mesh at large pore diameters. The authors also report that high concentrations of Kap95 modulate BSA permeability in a pore-size-dependent manner.
- **Visible evidence base** Main text figures 1–6, supplementary appendices 1–13 (referenced), equations 1–13, methods descriptions, and data availability links.
- **Missing materials affecting confidence** Supplementary figures and videos (Appendix 1–13, Figure 5—video 1) are referenced but not provided in the submitted text. Exact numerical values for all individual pore measurements are not included in the main text. Details of the change point detection algorithm parameters are only partially described. The fitting procedure for the parameter b in Equation 3 is not fully specified.

## Reviewer
- **Overall assessment** This manuscript presents a technically sophisticated optical approach to studying transport through biomimetic nuclear pore complexes, addressing an important question about the relationship between pore diameter and selectivity. The experimental system is well conceived, and the combination of single-molecule fluorescence measurements with coarse-grained simulations provides complementary perspectives. The central finding, that selectivity decreases with pore diameter with a transition around 55 nm, is interesting and potentially significant for understanding NPC function. However, several technical concerns regarding data analysis, control experiments, and the interpretation of the simulation results need to be addressed before the conclusions are fully established. The manuscript is generally well written and accessible, though some methodological details require clarification.
- **Who would be interested in the results, and why** Researchers studying nucleocytoplasmic transport, particularly those interested in the biophysical mechanisms of FG-nucleoporin selectivity. The work will also appeal to scientists developing biomimetic platforms for studying transport across nanopores, and to computational biologists working on coarse-grained models of intrinsically disordered proteins. The methodological advance of using optical nanopores for single-molecule transport measurements may interest the broader single-molecule biophysics community.
- **Major strengths** The experimental platform is innovative and addresses limitations of previous conductance-based approaches, particularly the ability to measure larger pores and distinguish multiple molecular species simultaneously. The systematic variation of pore diameter over a wide range (35–160 nm) is a significant advance over previous studies. The combination of experiments with CGMD simulations provides mechanistic insight into the observed behavior. The authors are transparent about data exclusion criteria and potential artifacts.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (control experiments for Nsp1 functionalization), R1-M2 (quantitative comparison of experimental and simulated rates), R1-M3 (interpretation of Kap95 concentration effects), R1-M4 (statistical treatment of pore-to-pore variability).
- **Assessment against Nature-style criteria**  
  *Originality*: The optical nanopore approach for NPC mimics is novel and represents a methodological advance. The systematic diameter dependence study is original.  
  *Scientific importance*: The question of how NPC diameter affects selectivity is timely and relevant given recent findings on NPC dilation. The results have implications for understanding NPC regulation.  
  *Interdisciplinary readership*: The work bridges biophysics, nanoscience, and cell biology, and should appeal to readers across these fields.  
  *Technical soundness*: The experimental design is generally sound, but several technical concerns (detailed below) need to be addressed. The simulation approach is appropriate but requires more careful quantitative comparison with experiments.  
  *Readability for nonspecialists*: The manuscript is well structured and clearly written. The figures are informative. Some methodological details may be challenging for nonspecialists but are presented in a logical manner.
- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are potentially important, but several issues regarding controls, quantitative comparisons, and interpretation need to be addressed before the conclusions are fully established.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental controls
- **Claim pointer** The authors claim that Nsp1 functionalization of the palladium pore walls creates a selective barrier, and that observed selectivity differences between Kap95 and BSA are due to the Nsp1 mesh.
- **Evidence pointer** Results section "NPC mimics show transport selectivity", Figure 3, Materials and methods "Cleaning and surface grafting of Pd"
- **Concern** The manuscript does not provide a direct control demonstrating that the observed selectivity is specifically due to Nsp1 and not to other factors such as differential surface interactions of the two proteins with the palladium walls or the PEG passivation layer. The authors compare Nsp1-coated pores to open pores passivated with MUHEG, but this does not isolate the effect of Nsp1. A control using a non-FG protein (e.g., a protein of similar size and charge to Nsp1 but lacking FG repeats) grafted to the pore walls would strengthen the claim that selectivity is due to the FG-repeat mesh. Additionally, the authors do not report any direct characterization of the Nsp1 layer on the palladium surface (e.g., surface density, layer thickness) in the actual pore geometry, relying instead on QCM-D measurements on flat surfaces.
- **Why it matters** Without appropriate controls, the observed selectivity differences could be attributed to non-specific protein-surface interactions rather than the specific properties of the Nsp1 FG-repeat mesh. This is central to the manuscript's main claim.
- **Resolution test** Provide control experiments with a non-FG protein coating, or direct evidence (e.g., fluorescence imaging, electron microscopy) of the Nsp1 layer within the pores. Alternatively, demonstrate that the selectivity is abolished when FG repeats are mutated or when the Nsp1 layer is removed.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative comparison of experiment and simulation
- **Claim pointer** The authors state that CGMD simulations "reproduce the trend of the experimental data well" and that the offset parameter b from the experimental fit (11.5 ± 0.4 nm) compares well with the simulation value (9.9 ± 0.1 nm).
- **Evidence pointer** Results section "Selectivity is lost at large-pore diameters", Figure 5C and D, Materials and methods "CGMD simulations"
- **Concern** The comparison between experimental and simulated rates relies on two independent scaling factors, k0,BSA and k0,Kap95, which are fitted to the experimental data for open pores. This means the simulations are not fully predictive; they are calibrated to match the open-pore rates. The agreement for Nsp1-coated pores is therefore not a stringent test of the model. Additionally, the authors do not provide a quantitative measure of the agreement between experimental and simulated rates (e.g., chi-squared, R² values). The visual agreement in Figure 5C appears reasonable, but the scatter in the experimental data is substantial, and it is unclear whether the simulations capture the pore-to-pore variability.
- **Why it matters** The claim that simulations support the experimental findings is weakened if the comparison is not quantitatively rigorous. The use of fitted scaling factors reduces the predictive power of the model.
- **Resolution test** Provide a statistical measure of the agreement between experimental and simulated rates. Discuss the sensitivity of the conclusions to the choice of scaling factors. If possible, use independent estimates of k0 (e.g., from diffusion theory) to reduce the number of free parameters.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of Kap95 concentration effects
- **Claim pointer** The authors report that increasing Kap95 concentration from 0 to 1000 nM increases BSA leakage for pores larger than 60 nm, and attribute this to a collapse of the Nsp1 mesh upon Kap95 binding.
- **Evidence pointer** Results section "Kap95 modulates the permeability for BSA", Figure 6
- **Concern** The interpretation that Kap95 binding causes Nsp1 mesh collapse is presented as the likely explanation, but alternative mechanisms are not thoroughly discussed or ruled out. For example, at high Kap95 concentrations, the high occupancy of Kap95 within the pore could lead to competitive displacement of BSA or to changes in the local ionic environment that affect BSA transport. The authors do not provide direct evidence for mesh collapse, such as measurements of Nsp1 layer thickness or density in the presence of Kap95. The observation that the effect is only seen for pores larger than 60 nm is interesting but not fully explained.
- **Why it matters** The claim that Kap95 modulates Nsp1 mesh structure has implications for understanding the dynamic behavior of the NPC barrier. If the interpretation is incorrect, the conclusions about the mechanism of selectivity modulation would be affected.
- **Resolution test** Provide direct evidence of Nsp1 mesh collapse in the presence of Kap95, e.g., through fluorescence correlation spectroscopy measurements of Nsp1 mobility, or through simulations that explicitly include Kap95 binding. Alternatively, discuss and rule out alternative explanations for the observed increase in BSA leakage.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical treatment of pore-to-pore variability
- **Claim pointer** The authors report significant pore-to-pore variability in the measured event rates and attribute this to variations in Nsp1 grafting density.
- **Evidence pointer** Results section "Selectivity is lost at large-pore diameters", Figure 4, Discussion
- **Concern** The manuscript reports large variability between pores of similar size, but the statistical treatment of this variability is not fully described. The authors state that the spread is likely due to variations in grafting density, but they do not quantify this relationship. The number of pores measured at each diameter is not clearly stated, and it is unclear whether the reported error bars represent standard deviations, standard errors, or confidence intervals. A more rigorous statistical analysis, including a clear statement of sample sizes and the use of appropriate statistical tests, would strengthen the conclusions.
- **Why it matters** The variability between pores affects the reliability of the reported diameter dependence. Without proper statistical treatment, it is difficult to assess the significance of the observed trends.
- **Resolution test** Provide a clear description of the number of pores measured at each diameter, the statistical measures used, and the results of appropriate statistical tests (e.g., ANOVA, regression analysis) to support the claimed diameter dependence.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Data analysis section
- **Evidence pointer** Materials and methods "Data analysis"
- **Issue** The description of the change point detection algorithm is brief. The authors state that it was "adapted" from Watkins and Yang, 2005, but do not specify the parameters used (e.g., penalty function, minimum event duration, threshold for significance). This makes it difficult for others to reproduce the analysis.
- **Required correction** Provide a more detailed description of the algorithm parameters and any modifications made to the original method. Alternatively, cite a more detailed methods paper or provide code documentation.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Figure clarity
- **Affected element** Figure 4
- **Evidence pointer** Results section "Selectivity is lost at large-pore diameters"
- **Issue** In Figure 4E, the selectivity ratio for individual pores is plotted, but the symbols for open and Nsp1-coated pores are not clearly distinguished in the legend. This makes it difficult to compare the two conditions.
- **Required correction** Ensure that the legend clearly distinguishes between open and Nsp1-coated pores, and consider using different symbols or colors for clarity.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of absolute rates
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The authors compare their measured event rates to those from previous studies, but the comparison is somewhat cursory. A more detailed discussion of the differences in experimental conditions (e.g., pore geometry, protein concentrations, buffer conditions) would help contextualize the results.
- **Required correction** Expand the comparison with previous studies, explicitly discussing differences in experimental setup and how these might affect the measured rates.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** Abstract, Introduction
- **Issue** The term "selectivity" is used to describe the ratio of Kap95 to BSA event rates. However, this term could be confused with the selectivity of the NPC for specific cargoes in the biological context. A more precise term, such as "transport selectivity ratio" or "Kap95/BSA permeability ratio," might be clearer.
- **Required correction** Consider using a more specific term throughout the manuscript to avoid ambiguity.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data availability statement
- **Evidence pointer** Data availability section
- **Issue** The data availability statement provides a repository link, but it is not clear whether the analysis code is also deposited. The authors mention code in the methods, but the link provided appears to be for data only.
- **Required correction** Clarify whether the analysis code is available and provide a link if so. If not, state that code is available upon request.

## Risk / unsupported claims
- The claim that the Nsp1 mesh collapses upon Kap95 binding (R1-M3) is presented as the likely explanation for the observed increase in BSA leakage, but direct evidence is not provided.
- The quantitative agreement between experimental and simulated event rates is not rigorously established due to the use of fitted scaling factors (R1-M2).
- The attribution of pore-to-pore variability to variations in grafting density is plausible but not directly demonstrated (R1-M4).
- The claim that the assay provides "single-molecule translocations through individual pores" is supported by the methods, but the detection efficiency and potential for missed events are not fully quantified.
- The statement that the approach "could easily be expanded to other FG-nucleoporins" is speculative and not supported by specific evidence in this manuscript.