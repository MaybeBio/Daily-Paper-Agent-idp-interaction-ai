## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, limitations, materials and methods, figure legends, and supplementary figure legends
- **Assessment boundary** Scientific content, experimental logic, data interpretation, and technical soundness as presented in the provided manuscript text. No external data or unpublished information was consulted.
- **Shared manuscript claim summary** The authors identify Pln1, a perilipin in Saccharomyces cerevisiae, as an essential regulator of microlipophagy. They propose that Pln1 tethers lipid droplets to vacuoles via its N-terminal PAT domain and a hydrophobic region, with a specific semi-hydrophobic LD Interacting Motif (LIM) within the PAT domain being critical. They further show that Pln1-mediated lipophagy regulates lipid droplet size and distribution, but not total TAG levels, and that Pln1 deletion can partially rescue survival defects in autophagy-defective cells.
- **Visible evidence base** Results sections 1-7, Figures 1-7 (described in text), Supplementary Figures S1-S6, Materials and Methods, Discussion, Limitations
- **Missing materials affecting confidence** Actual figure images and raw data are not available for direct inspection. Statistical details beyond stated p-values are not provided. The full results section is not written out in the provided text, only section headings. No source data files or numerical values for quantitative claims are available.

## Reviewer
- **Overall assessment** This manuscript presents a potentially important finding that Pln1, previously known for its role in lipid droplet biogenesis, also functions as a key regulator of microlipophagy in yeast. The identification of a specific motif within the PAT domain that mediates lipid droplet-vacuole tethering is novel and could have implications for understanding lipophagy mechanisms across species. However, several technical concerns and gaps in the evidence need to be addressed before the central claims are fully established. The manuscript would benefit from clearer presentation of quantitative data and additional mechanistic experiments to support the proposed tethering model.
- **Who would be interested in the results, and why** Researchers studying lipid droplet biology, autophagy, and organelle contact sites would find this work of interest. The identification of a specific tethering mechanism for microlipophagy could inform studies in higher eukaryotes where lipophagy is implicated in metabolic diseases. The finding that Pln1 plays dual roles in both lipid droplet biogenesis and degradation may also interest those studying perilipin family proteins.
- **Major strengths** 1. The study addresses an important and understudied question regarding the molecular mechanisms of microlipophagy. 2. The identification of a specific LIM motif within the PAT domain provides a concrete molecular handle for future studies. 3. The use of multiple complementary approaches (fluorescence microscopy, electron microscopy, biochemical assays) strengthens the conclusions. 4. The finding that Pln1 functions across multiple nutrient stress conditions suggests broad physiological relevance.
- **Major Concerns** 
- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that Pln1 is essential for lipophagy based on reduced Erg6-GFP processing in pln1Δ cells, with severity comparable to atg1Δ and atg8Δ deletions.
- **Evidence pointer** Figure 1A-C, Figure S1A-C
- **Concern** The Erg6-GFP processing assay is presented as the primary quantitative measure of lipophagy, but the manuscript does not provide the actual quantification data or statistical analysis for these experiments. The text states "significantly reduced" and "similar levels" without showing the numerical values, error bars, or statistical test results. Additionally, the authors do not address whether the reduced Erg6-GFP processing in pln1Δ cells could be due to indirect effects on vacuolar function or general protein degradation rather than specific effects on lipophagy.
- **Why it matters** The central claim of the paper rests on this assay. Without clear quantitative evidence and appropriate controls, the conclusion that Pln1 is essential for lipophagy cannot be properly evaluated.
- **Resolution test** Provide the actual quantification data for Erg6-GFP processing with appropriate statistical analysis. Include controls demonstrating that vacuolar function and general autophagy are unaffected in pln1Δ cells, such as assays for vacuolar protease activity and processing of other vacuolar substrates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors identify a specific LIM motif within the PAT domain (residues 16-33) that is essential for Pln1 localization to lipid droplets and for lipophagy.
- **Evidence pointer** Figure 4, Figure S3, Figure S4
- **Concern** The mutational analysis identifying the LIM motif is described, but the manuscript does not provide sufficient detail on how the mutations were designed and validated. The text mentions "site-specific mutagenesis" and "semi-hydrophobic LD Interacting Motif" but does not explain the rationale for choosing specific residues or provide structural context. Furthermore, the authors do not show whether the Pln1-LIM mutant protein, when overexpressed, could act as a dominant negative or whether the phenotype is solely due to loss of lipid droplet localization.
- **Why it matters** The identification of a specific functional motif is a key contribution of this work. Without proper validation of the mutant constructs and clear demonstration that the phenotype is due to loss of tethering function rather than protein misfolding or mislocalization, the conclusion is not fully supported.
- **Resolution test** Provide detailed information on the design of the LIM mutations, including structural predictions or sequence alignments. Include experiments showing that the Pln1-LIM mutant protein is properly folded and expressed at similar levels to wild-type. Consider testing whether the LIM mutant can still interact with other known binding partners.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors propose that Pln1 tethers lipid droplets to vacuoles by simultaneously interacting with both organelles, potentially through Vac8 binding.
- **Evidence pointer** Figure 4I, Discussion
- **Concern** The proposed tethering model is supported primarily by computational predictions (ColabFold) of Vac8-GAP1 interaction. No direct biochemical or genetic evidence is provided to demonstrate that Pln1 physically interacts with Vac8 or any other vacuolar protein. The authors acknowledge this is a hypothesis but do not provide experimental validation. Additionally, the relationship between Pln1 and the previously identified Ldo16/Ldo45 tethering complex is not experimentally addressed.
- **Why it matters** The tethering model is central to the proposed mechanism of Pln1 function. Without direct evidence of physical interaction between Pln1 and vacuolar components, the model remains speculative.
- **Resolution test** Perform co-immunoprecipitation or in vitro binding assays to test Pln1-Vac8 interaction. Use genetic approaches such as overexpression of the GAP1 domain to compete with endogenous interactions. Test whether Pln1 and Ldo16/Ldo45 function in the same or parallel pathways using double mutants.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors state that Pln1-mediated lipophagy regulates lipid droplet size and distribution, and that this is important for cellular physiology.
- **Evidence pointer** Figure 6B-I
- **Concern** While the observation that lipophagy affects lipid droplet size is interesting, the physiological significance of this finding is not clearly established. The authors show that pln1Δ cells have larger lipid droplets, but do not demonstrate any functional consequences of this size change. The connection to cell survival is correlative rather than causal.
- **Why it matters** The broader significance of the findings depends on understanding why lipid droplet size regulation matters for cellular function. Without demonstrating functional consequences, the importance of this observation is unclear.
- **Resolution test** Investigate whether the enlarged lipid droplets in pln1Δ cells affect lipid metabolism, membrane trafficking, or stress responses. Test whether restoring normal lipid droplet size in pln1Δ cells (e.g., by modulating lipolysis) rescues any observed phenotypes.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors conclude that Pln1 deletion improves survival in atg8Δ cells under nitrogen starvation.
- **Evidence pointer** Figure 7A, Figure S6
- **Concern** The survival data are presented as growth curves, but the manuscript does not provide the actual survival percentages or statistical comparisons between strains. The claim of "enhanced viability" is not supported by clear quantitative data. Additionally, the mechanism by which reduced lipid droplet content would improve survival in autophagy-deficient cells is not explained.
- **Why it matters** This is an interesting and potentially important finding, but without proper quantification and mechanistic insight, the conclusion is not well supported.
- **Resolution test** Provide survival curves with actual cell viability counts and statistical analysis. Include experiments to test the hypothesis that reduced lipid droplet content reduces toxic lipid species or metabolic burden in autophagy-deficient cells.

- **Minor Comments**
- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states Pln1 is "essential for lipophagy" but the data show it is specifically required for microlipophagy, not macrolipophagy. This distinction should be made clear.
- **Required correction** Revise the abstract to specify that Pln1 is essential for microlipophagy, not all forms of lipophagy.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Statistical analysis
- **Evidence pointer** Materials and Methods, Statistical analyses
- **Issue** The statistical methods section mentions both "One-Way ANOVA" and "Brown-Forsythe and Welch ANOVA tests" but does not clarify which test was used for which experiment. The figure legends also do not consistently indicate the statistical test used.
- **Required correction** Clearly specify which statistical test was used for each experiment in the figure legends and ensure consistency between the methods and results.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 3
- **Evidence pointer** Figure 3A-C
- **Issue** The text states that deletion of LDOs led to reduction of A-LDs under glucose starvation (13%), but the comparison to pln1Δ (15%) is confusing. It is unclear if these are absolute percentages or relative reductions.
- **Required correction** Clarify whether these numbers represent absolute percentages of A-LDs or relative reductions compared to wild-type, and present the data consistently.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Materials and Methods
- **Evidence pointer** Materials and Methods, Yeast strains and genetics
- **Issue** The description of plasmid construction is overly complex and difficult to follow. The use of "PLN1△-1, PLN1△-2, PLN1△-4, PLN1△-3and 4, PLN1△-4 and 5, PLN1△-3,4 and 5, LIM1 mutant and LIM2 mutant and LIM mutants" is confusing without a clear table or diagram.
- **Required correction** Provide a clear table or schematic showing the deletion constructs and their corresponding domains, and use consistent nomenclature throughout.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion
- **Evidence pointer** Discussion, Mechanism of Pln1-Dependent LD-Vacuole Association
- **Issue** The discussion of whether Pln1's role is conserved in mammals is speculative and not well supported by the data presented. The authors mention PLIN3 as the closest homolog but do not provide any experimental evidence or strong sequence analysis to support this claim.
- **Required correction** Either provide additional analysis supporting the conservation claim or clearly state that this is speculative and requires further investigation.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Figure 6
- **Evidence pointer** Figure 6B-D
- **Issue** The electron microscopy data are described as showing enlarged lipid droplets in pln1Δ cells, but the quantification method is not described in sufficient detail. The text mentions "quantified manually by measuring the area of LDs" but does not specify how many cells or lipid droplets were measured.
- **Required correction** Provide details on the number of cells and lipid droplets measured, and describe the blinding procedure used to avoid bias in manual measurements.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Limitations
- **Evidence pointer** Limitations
- **Issue** The limitations section is very brief and only mentions the resolution limit of confocal microscopy. Other limitations, such as the lack of direct biochemical evidence for the tethering model and the correlative nature of the survival data, should be acknowledged.
- **Required correction** Expand the limitations section to address the key technical and conceptual limitations of the study.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Materials and Methods
- **Evidence pointer** Materials and Methods, Structural modelling
- **Issue** The description of the ColabFold modeling is brief and does not provide sufficient details on the parameters used or the confidence of the predictions. The authors state "all five top models" showed interaction but do not provide the confidence scores or the range of predicted structures.
- **Required correction** Provide additional details on the modeling parameters, confidence scores, and the variability among the top models.

## Risk / unsupported claims
- The claim that Pln1 is "essential" for lipophagy is not fully supported by the data presented, as the severity of the defect in pln1Δ cells is stated to be "similar" to atg1Δ and atg8Δ but the actual quantitative comparison is not shown.
- The proposed tethering mechanism involving Vac1 binding is based solely on computational predictions and is not experimentally validated.
- The claim that Pln1 deletion "enhances viability" in atg8Δ cells is not supported by clear quantitative survival data.
- The statement that Pln1's role may be conserved in mammals is speculative and not supported by experimental evidence.
- The claim that Pln1 regulates lipophagy "under various nutrient conditions" is based on data from nitrogen starvation and glucose restriction, but the manuscript does not clearly show that the same mechanism operates under all conditions tested.
- The conclusion that lipid droplet size regulation by lipophagy is physiologically important is correlative and lacks direct functional evidence.