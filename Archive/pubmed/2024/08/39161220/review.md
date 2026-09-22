## Review setup
- **Input scope** Full manuscript text (abstract, results, discussion, methods summary) without figures, figure supplements, or supplementary files
- **Assessment boundary** Scientific claims, experimental logic, modeling approach, and internal consistency based on the provided text; figures, tables, and supplementary materials referenced but not directly assessable
- **Shared manuscript claim summary** The authors propose that target-specific requirements for RNA interference (RNAi) in C. elegans can be explained by a single intersecting regulatory network with quantitative contributions from multiple proteins, rather than by parallel or specialized pathways. They support this with genetic epistasis-like experiments, quantitative modeling, and tests of model predictions including cis-regulatory swaps, recovery from silencing in non-dividing cells, and pUG zone mapping.
- **Visible evidence base** Text descriptions of genetic screens, CRISPR-generated mutants, RNAi phenotyping, RT-PCR for pUG RNA, and three modeling approaches (network constraint satisfaction, equilibrium model, dynamic ODE model); references to figures and supplements that were not provided
- **Missing materials affecting confidence** All figures, figure supplements, tables, source data, and code; exact quantitative phenotyping data; statistical details; strain genotypes beyond text descriptions; the full methods for modeling parameter selection and constraint satisfaction

## Reviewer
- **Overall assessment** This manuscript addresses an important question in RNAi biology: whether target-specific differences in genetic requirements reflect specialized pathways or quantitative thresholds within a shared network. The authors present a compelling conceptual framework supported by a combination of genetic experiments and modeling. The central claim, that a single intersecting network with quantitative contributions can explain selective requirements, is plausible and well-argued. However, the strength of the conclusion depends critically on data not visible in the text alone, particularly the quantitative phenotyping, the constraint satisfaction analysis, and the pUG zone experiments. The modeling sections are described at a level that makes independent evaluation difficult. The manuscript is likely to be of interest to the RNAi and gene-silencing community, and the conceptual advance is significant if the data support the claims as described.
- **Who would be interested in the results, and why** Researchers studying RNAi mechanisms, small RNA biology, gene regulation, and therapeutic applications of dsRNA. The finding that target-specific requirements can arise from quantitative thresholds rather than dedicated pathways has implications for understanding why some genes are more amenable to silencing than others, which is directly relevant to designing effective RNAi-based therapeutics and understanding resistance mechanisms.
- **Major strengths**
  - The conceptual framework is elegant and parsimonious, offering a unified explanation for diverse observations in the RNAi field.
  - The combination of genetics, modeling, and predictive testing is a strong methodological approach.
  - The use of CRISPR-mediated genome editing to generate clean mutants avoids confounds from multi-mutation strains.
  - The discovery of recovery from silencing in non-dividing cells and the pUG zone concept are potentially important contributions.
  - The authors are appropriately cautious in acknowledging the limits of their model and the need for future mechanistic studies.
- **Major Concerns**
  - **R1-M1** (Blocking: Yes)
  - **R1-M2** (Blocking: Yes)
  - **R1-M3** (Blocking: No)
  - **R1-M4** (Blocking: No)
- **Minor Comments**
  - **R1-m1**
  - **R1-m2**
  - **R1-m3**
  - **R1-m4**
  - **R1-m5**
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria**
  - **Originality** High. The idea that target-specific requirements reflect quantitative thresholds in a shared network rather than dedicated pathways is a novel synthesis that challenges existing assumptions in the field.
  - **Scientific importance** High. The findings have implications for understanding RNAi mechanism, predicting silencing efficacy, and designing therapeutic strategies. The recovery-from-silencing observation is particularly significant.
  - **Interdisciplinary readership** Moderate. The work will primarily interest RNAi and C. elegans researchers. The modeling aspects may attract computational biologists, but the presentation is not sufficiently accessible for a broad interdisciplinary audience.
  - **Technical soundness** Cannot be fully assessed from the text alone. The genetic logic is sound, but the quantitative data, modeling details, and statistical analyses are not visible. The modeling sections are described at a level that prevents independent verification.
  - **Readability for nonspecialists** The abstract and introduction are accessible, but the results and methods sections assume substantial background in RNAi biology and C. elegans genetics. The modeling sections are particularly dense and would benefit from clearer exposition.
- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual advance is significant and the experimental approach is appropriate, but the manuscript cannot be fully evaluated without access to the figures, quantitative data, and modeling details. The authors should be encouraged to provide a revised version with clearer presentation of the modeling and more complete data reporting.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "any two of these proteins are sufficient for silencing unc-22" and that "each is singly required for silencing bli-1," based on experiments with single and double mutants.
- **Evidence pointer** Results section "Two genes with different thresholds for silencing reveal an intersecting network of regulators that mediate RNA interference"; Figures 1D and 2B (not provided)
- **Concern** The central genetic claim rests on quantitative phenotyping data that are not visible in the text. The authors state that single mutants silence unc-22 but not bli-1, and that double mutants fail to silence both, but the actual extent of silencing, the statistical significance of differences, and the reproducibility of these phenotypes are not reported. The text mentions "residual silencing" and "partial silencing" but does not provide quantitative thresholds or criteria for these classifications. Without the underlying data, it is impossible to verify that the observed differences are robust and not due to subtle quantitative variations.
- **Why it matters** The entire conceptual framework depends on the distinction between genes that are "singly required" versus those that are "redundantly required." If the quantitative differences are small or variable, the conclusion that a single intersecting network explains the data would be weakened. The claim that "any two are sufficient" is a strong statement that requires rigorous quantitative support.
- **Resolution test** Provide the full quantitative phenotyping data for all single and double mutant combinations, including the distribution of phenotypes, statistical comparisons, and the criteria used to classify silencing as present, absent, partial, or residual. Ideally, show dose-response curves or time-course data for silencing to demonstrate the robustness of the observed differences.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Modeling validity
- **Claim pointer** The authors claim that "quantitative models and their exploratory simulations led us to find that (1) changing cis-regulatory elements of the target gene can reduce the dependence on NRDE-3, (2) animals can recover from silencing in non-dividing cells, and (3) cleavage and tailing of mRNAs with UG dinucleotides... are enriched within 'pUG zones' matching the dsRNA."
- **Evidence pointer** Results sections "Quantitative modeling of RNA interference and mRNA production provides rationales for a variety of target-specific outcomes" and "Gene expression can recover after knockdown despite the presence of amplification mechanisms"; Figures 4, 4-figure supplements 1 and 2, 6 (not provided)
- **Concern** The modeling sections are described at a level of abstraction that prevents independent evaluation. The authors state that they used a "sequential equilibrium model" and a "dynamic model" with "ordinary differential equations," but the equations, parameter values, initial conditions, and fitting procedures are not presented in the text. The claim that simulations "led us to find" specific predictions is not verifiable without access to the code and a clear description of the parameter space explored. Furthermore, the relationship between the model predictions and the experimental tests is not always explicit. For example, how exactly does the model predict that changing cis-regulatory elements reduces NRDE-3 dependence? What specific parameter changes correspond to this prediction?
- **Why it matters** The modeling is presented as a key component of the paper's contribution, and the predictions are used to motivate experiments. If the model is not transparent or reproducible, the strength of the paper's conclusions is diminished. The claim that the model "led" to the discoveries suggests a tight coupling between theory and experiment that needs to be demonstrated.
- **Resolution test** Provide the full model equations, parameter definitions, and the code used for simulations. Describe the parameter space explored and the criteria for identifying predictions. For each experimental test, explicitly state which model prediction it is testing and how the experimental outcome confirms or refutes the prediction. Consider including a supplementary figure that shows the model output for key simulations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretive clarity
- **Claim pointer** The authors propose that "the Maelstrom domain-containing protein RDE-10, the intrinsically disordered protein MUT-16, and the Argonaute protein NRDE-3 work together so that any two are required for silencing one somatic gene, but each is singly required for silencing another somatic gene."
- **Evidence pointer** Results section "Two genes with different thresholds for silencing reveal an intersecting network of regulators that mediate RNA interference"; Figures 1D, 2B, 2C (not provided)
- **Concern** The interpretation of the genetic data in terms of an "intersecting network" is presented as the only viable explanation, but the authors do not thoroughly discuss alternative models. For example, could the differences between bli-1 and unc-22 be explained by differences in mRNA abundance, stability, or subcellular localization that affect the requirement for specific factors, without invoking a network architecture? The authors mention "differences in their RNA metabolism" but do not elaborate on what these differences might be or how they would quantitatively impact the requirement for each factor. The distinction between a "network" and a "pathway" is conceptually important, but the experimental data may not be able to distinguish between them as cleanly as the authors suggest.
- **Why it matters** The paper's central claim is that the data support a single intersecting network rather than parallel pathways. If alternative explanations are not adequately considered, the conclusion may be overstated. The distinction between network and pathway has implications for how the field thinks about RNAi mechanism and for predicting the effects of mutations in different genetic backgrounds.
- **Resolution test** Expand the discussion to explicitly consider alternative models, such as differential mRNA stability, subcellular localization, or expression levels of the target genes, and explain why the data favor the network interpretation. If possible, include experiments or analyses that directly test these alternatives, such as measuring mRNA half-lives or localization of bli-1 and unc-22 transcripts.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The authors state that "similar crosstalk between pathways and restricted amplification could result in apparently selective silencing by endogenous RNAs."
- **Evidence pointer** Discussion section (not explicitly labeled in the provided text, but implied in the abstract and final paragraph of the Results)
- **Concern** The claim that the findings extend to endogenous RNAi pathways is speculative and not supported by direct evidence in the manuscript. The authors have studied two exogenous targets (bli-1 and unc-22) in response to ingested dsRNA. The extrapolation to endogenous small RNA pathways, which may have different mechanisms and requirements, is a significant leap. While the authors are appropriately cautious in using the word "could," the statement is presented as a conclusion of the paper rather than a hypothesis for future work.
- **Why it matters** The broader significance of the paper depends in part on whether the framework applies to endogenous RNAi. If the claim is overstated, it may mislead readers into thinking the findings have broader applicability than is warranted.
- **Resolution test** Either provide direct evidence that the framework applies to endogenous RNAi targets, or soften the claim to clearly indicate that it is a hypothesis. If the latter, consider adding a paragraph in the discussion that outlines what experiments would be needed to test this hypothesis.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, sentence "Quantitative models and their exploratory simulations led us to find that..."
- **Issue** The phrase "led us to find" is vague. It is unclear whether the models generated predictions that were then tested experimentally, or whether the models were used to interpret experimental results. This distinction is important for understanding the logical structure of the paper.
- **Required correction** Rephrase to clarify the relationship between modeling and experiment. For example: "Quantitative modeling predicted that..., and we confirmed this experimentally by..." or "Quantitative modeling, combined with experimental tests, revealed that..."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, Modeling section
- **Evidence pointer** Materials and methods, "Modeling and simulation"
- **Issue** The methods state that simulations were conducted in R and Python, but no version numbers, package versions, or random seeds are provided. This makes it difficult to reproduce the simulations exactly.
- **Required correction** Add version information for R, Python, and all relevant packages. If stochastic elements are present, provide random seeds or state that the results are deterministic.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results, genetic experiments
- **Evidence pointer** Results section "Two genes with different thresholds for silencing reveal an intersecting network of regulators that mediate RNA interference"
- **Issue** The text describes silencing as "+++", "+", or "-" but does not explain the scale or how these categories were determined. The number of biological replicates and the statistical tests used are not stated in the text.
- **Required correction** Define the scoring system clearly, state the number of replicates, and describe the statistical methods used to compare silencing between genotypes.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** Results, Discussion
- **Issue** The term "pUG zones" is introduced without a formal definition. It is unclear whether this is a new concept or a descriptive term for a known phenomenon.
- **Required correction** Define "pUG zones" explicitly when first used, and clarify whether this is a novel concept or a descriptive term.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Methods, Modeling
- **Evidence pointer** Materials and methods, "Modeling and simulation"
- **Issue** The description of the three models is brief and assumes familiarity with the field. A reader without a modeling background may struggle to understand the differences between the models and why they were used.
- **Required correction** Provide a brief, accessible summary of each model, its purpose, and its limitations. Consider adding a schematic figure that illustrates the models and their relationships.

## Risk / unsupported claims
- The claim that "any two of these proteins are sufficient for silencing unc-22" is not fully supported by the text alone, as the quantitative data are not provided.
- The claim that "changing cis-regulatory elements of the target gene can reduce the dependence on NRDE-3" is presented as a model prediction, but the experimental evidence is not described in sufficient detail to evaluate its strength.
- The claim that "animals can recover from silencing in non-dividing cells" is supported by a single experiment (Figure 6A), but the text does not provide details on the kinetics, the extent of recovery, or whether this is specific to unc-22 or generalizable.
- The claim that "cleavage and tailing of mRNAs with UG dinucleotides... are enriched within 'pUG zones' matching the dsRNA" is based on RT-PCR data (Figure 6C), but the text does not provide quantitative comparisons or statistical analyses.
- The extrapolation to endogenous RNAi pathways ("similar crosstalk... could result in apparently selective silencing by endogenous RNAs") is speculative and not directly supported by the data presented.