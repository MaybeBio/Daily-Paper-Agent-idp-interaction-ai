## Review setup
- **Input scope** Full manuscript text (Abstract, Introduction, Methodology, Results, Discussion, Conclusion) as provided
- **Assessment boundary** Scientific soundness, methodological rigor, validity of claims relative to evidence presented, and alignment with Nature-style criteria
- **Shared manuscript claim summary** The authors report in-silico characterization and expression profiling of four GT-γ trihelix transcription factors (StGTγ-1, StGTγ-2, StGTγ-3, StGTγ-4) in potato under drought stress, including structural modelling, cis-element analysis, subcellular localization prediction, protein-protein interaction and docking, and qRT-PCR validation showing leaf-preferential upregulation after 14 days of drought.
- **Visible evidence base** Main text figures (Figs 1-8), supplementary tables and figures referenced (S1-S13, Supplementary Figs 1-20), methodology descriptions, and statistical annotations as reported
- **Missing materials affecting confidence** Raw qRT-PCR data (Ct values, primer efficiencies), statistical output tables (exact p-values, F-values, effect sizes), multiple sequence alignment data, template identification details for homology modelling, docking scoring function details, and full supplementary content were not available for independent verification

## Reviewer
- **Overall assessment** This manuscript presents a broad, largely descriptive bioinformatics survey of four GT-γ trihelix transcription factors in potato, complemented by a focused qRT-PCR expression experiment. The work is positioned as a first characterization of this subfamily under drought in potato, which is a reasonable gap to address. However, the manuscript suffers from several critical weaknesses that currently prevent the conclusions from being fully supported. The in-silico analyses are mostly standard and descriptive, with limited statistical or experimental validation. The qRT-PCR experiment, while relevant, is underpowered (single cultivar, single time-course, no biological replication details beyond "triplicate"), and the link between the computational predictions and the expression data is largely correlative. Several claims, particularly regarding functional roles in drought tolerance, go beyond what the evidence can support. The manuscript would benefit from substantial revision, additional experimental validation, and more cautious interpretation before it can be considered for publication.
- **Who would be interested in the results, and why** Researchers working on plant transcription factor families, particularly trihelix and GT-element binding proteins, and those interested in drought stress responses in Solanaceae crops. The identification of candidate genes with leaf-preferential drought-responsive expression may be of interest to potato breeders and biotechnologists seeking targets for drought tolerance engineering. The structural and interaction predictions could serve as a starting point for more detailed functional studies.
- **Major strengths**
  1. The study addresses a genuine gap: GT-γ subfamily characterization in potato under drought is lacking.
  2. The multi-pronged in-silico approach (structure, disorder, PTMs, localization, cis-elements, docking) is comprehensive in scope.
  3. The inclusion of both in-silico transcriptome data (GEO) and independent qRT-PCR validation strengthens the expression component.
  4. The manuscript is generally clearly written and logically organized.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental design and statistical rigor
- **Claim pointer** The authors claim significant drought-responsive upregulation of StGTγ genes in leaves based on qRT-PCR data (Abstract; Results section "Expression profiling analysis"; Fig. 8).
- **Evidence pointer** Methodology section "RNA extraction and qRT-PCR validation"; Fig. 8
- **Concern** The qRT-PCR experimental design is inadequately described and appears underpowered. Only one cultivar (Kuroda) was used, and while "three biological replicates" are mentioned, no information is provided on the number of technical replicates, the number of independent experiments, the statistical model used (two-way ANOVA is mentioned but with unusual significance thresholds), or whether assumptions for ANOVA were tested. The significance notation "NEJM: 0.12 (ns), 0.033 (*), 0.002 (**), <0.001 (***)" is non-standard and confusing. Most critically, the claim of "high expression in leaves" is based on fold-changes relative to a single reference gene (actin) without validation of reference gene stability under drought conditions. Without proper statistical reporting (exact p-values, confidence intervals, effect sizes) and a clear description of replication, the central experimental claim is not verifiable.
- **Why it matters** The qRT-PCR data constitute the only direct experimental evidence in the manuscript. If this evidence is not statistically robust, the central conclusion that these genes are involved in drought response is not established.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Overinterpretation of in-silico predictions
- **Claim pointer** The authors state that "GT-γ proteins likely regulate genes due to structural variations" and that docking results "provide strong evidence for the involvement of GT-γ proteins in a complex regulatory network governing plant responses to drought stress" (Abstract; Discussion).
- **Evidence pointer** Results sections "Protein–protein interaction prediction and docking"; Discussion
- **Concern** The manuscript consistently overstates the evidential weight of computational predictions. Molecular docking scores, particularly from web-based servers without rigorous validation, do not constitute "strong evidence" for biological function. The predicted interactions with drought-related proteins are purely computational and have not been validated by any biochemical or genetic experiment (e.g., Y2H, Co-IP, EMSA). Similarly, the presence of cis-elements in promoters is suggestive but not proof of regulation. The phrase "likely regulate genes" is speculative and should be clearly framed as a hypothesis, not a finding.
- **Why it matters** Overinterpretation of in-silico data can mislead readers and the broader community, and it weakens the scientific credibility of the manuscript. The distinction between prediction and validation must be explicit.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Gene nomenclature and identification rigor
- **Claim pointer** The authors identify and name four genes StGTγ-1, StGTγ-2, StGTγ-3, and StGTγ-4 and refer to them as "GT-γ trihelix transcription factors" (throughout).
- **Evidence pointer** Methodology section "Identification of GT-γ trihelix genes"; Results section "Functional annotation"
- **Concern** The manuscript does not provide sufficient evidence that the four genes studied are bona fide GT-γ subfamily members. The identification method is described as "homology-based" using Arabidopsis queries, but no phylogenetic analysis, domain architecture comparison, or sequence alignment is shown in the main text. The naming convention (StGTγ-1 through StGTγ-4) does not follow any established nomenclature for potato trihelix genes, and it is unclear how these relate to previously identified potato trihelix genes (e.g., the 7 GT-γ members mentioned in the Introduction). The relationship between the names used in the in-silico analysis (StTH-1, StTH-16, StTH-21, StTH-26) and the gene names in the title/abstract (StGTγ-1, StGTγ-2, StGTγ-3, StGTγ-4) is confusing and inconsistent. This inconsistency appears in figure legends and text, making it difficult to track which gene is being discussed.
- **Why it matters** Accurate gene identification and consistent nomenclature are fundamental to the validity of the study. If the genes are not correctly assigned to the GT-γ subfamily, the entire premise of the manuscript is undermined.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** In-silico transcriptome analysis methodology
- **Claim pointer** The authors state that "In-silico transcription profiling in Fig. 7 enables the comparative analysis of gene expression under various conditions" and draw conclusions about cultivar-specific responses (Results section "In-silico transcriptome analysis").
- **Evidence pointer** Results section "In-silico transcriptome analysis of trihelix GT-γ transcription factors"; Fig. 7
- **Concern** The description of the GEO dataset analysis is insufficient. It is unclear how the data were processed (e.g., normalization method, statistical threshold for differential expression, how multiple probes/transcripts were handled), whether the analysis was performed by the authors or extracted from the original publication, and whether any statistical testing was applied to the expression differences shown in Fig. 7. The figure appears to show bar charts without error bars or significance indicators. The claim that expression "significantly decreases" in one cultivar is not supported by any statistical evidence.
- **Why it matters** Without a clear and reproducible description of the bioinformatics analysis, the in-silico transcriptome results cannot be evaluated or reproduced, which is a core expectation for computational work.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Structural modelling validation
- **Claim pointer** The authors state that "The quality of the refined model was then evaluated using Root-Mean-Square Deviation (RMSD) analysis" and that models were validated using Procheck, Errat, QMEAN, and WHATIF (Methodology; Results "Model validation and quality assessment").
- **Evidence pointer** Methodology section "Protein structure modelling and refinement"; Results section "Model validation and quality assessment"; Supplementary Tables S4-S7
- **Concern** The use of RMSD to evaluate model quality is conceptually problematic. RMSD between a model and its template measures similarity to the template, not model accuracy or quality. A low RMSD to the template does not indicate a good model; it simply indicates the model closely resembles the template. The manuscript does not report the sequence identity between the target and template, which is the primary determinant of homology model reliability. Additionally, the Ramachandran plot statistics are reported as percentages in the "favourable and allowed regions" but the specific numbers for each model are not clearly presented in the main text. The claim that models are of "good quality" is not adequately supported by the metrics reported.
- **Why it matters** Structural models are used to support functional inferences. If the models are not rigorously validated, the structural claims (e.g., alpha-helix prevalence, disordered regions) and downstream docking results are built on an unreliable foundation.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and consistency
- **Affected element** Gene nomenclature throughout
- **Evidence pointer** Title; Abstract; Results; Figures 3, 7, 8
- **Issue** The manuscript uses two different naming systems (StGTγ-1/2/3/4 and StTH-1/16/21/26) without clearly explaining the correspondence. This creates confusion for the reader.
- **Required correction** Provide a clear mapping table or statement explaining the relationship between the two naming systems and use one consistent nomenclature throughout the manuscript.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** qRT-PCR results
- **Evidence pointer** Fig. 8; Methodology "RNA extraction and qRT-PCR validation"
- **Issue** The statistical significance notation is non-standard and the exact p-values are not reported. The threshold "0.12 (ns)" is unusual and not a conventional significance level.
- **Required correction** Report exact p-values for all comparisons, use standard significance thresholds (e.g., p < 0.05), and describe the statistical test and post-hoc corrections used.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reference gene validation
- **Affected element** qRT-PCR normalization
- **Evidence pointer** Methodology "RNA extraction and qRT-PCR validation"
- **Issue** The stability of the reference gene (actin) under drought conditions is not validated. Drought stress can affect expression of housekeeping genes.
- **Required correction** Validate reference gene stability under the experimental conditions (e.g., using geNorm or NormFinder) or cite previous validation in potato under drought.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Fig. 7
- **Evidence pointer** Fig. 7
- **Issue** The in-silico transcriptome figure appears to lack error bars and significance indicators, making it difficult to assess variability or statistical support for the reported differences.
- **Required correction** Add error bars and statistical annotations, or clearly state that the data are from a single biological sample per condition.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Docking score interpretation
- **Affected element** Results "Protein–protein interaction prediction and docking"
- **Evidence pointer** Results section; Supplementary Table S13
- **Issue** The manuscript reports docking scores but does not provide a threshold or context for what constitutes a "good" or "meaningful" docking score. The units and scoring function are not clearly described.
- **Required correction** Provide the scoring function used, a clear interpretation of the score range, and a justification for why the reported scores indicate meaningful interactions.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Language and grammar
- **Affected element** Throughout
- **Evidence pointer** Introduction; Discussion
- **Issue** There are several grammatical errors and awkward phrasings (e.g., "and enzymes crucial for coping with drought stress. and enzymes crucial for coping with drought stress." duplicated in Introduction; "notarization" in Methodology likely meant "normalization").
- **Required correction** Careful proofreading and language editing are needed.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Missing methodological details
- **Affected element** Homology modelling
- **Evidence pointer** Methodology "Protein structure modelling and refinement"
- **Issue** The template used for homology modelling is not identified, and the sequence identity between target and template is not reported.
- **Required correction** Specify the PDB template(s) used, sequence identity, and coverage for each model.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Inconsistent reporting of significance
- **Affected element** Fig. 8
- **Evidence pointer** Fig. 8
- **Issue** The figure legend mentions "significance indicated by ns (0.12), * (0.033), ** (0.002), and *** (<0.001)" but it is unclear which comparisons these refer to and whether these are p-values or adjusted values.
- **Required correction** Clarify the annotation system in the figure legend and ensure it matches the statistical analysis described in the text.

## Risk / unsupported claims
- The claim that GT-γ proteins "likely regulate genes due to structural variations" is unsupported by direct experimental evidence and is speculative.
- The claim that docking results provide "strong evidence" for involvement in drought stress response is an overstatement of computational predictions.
- The claim that "StGT-γ genes play a critical role in modulating drought response" is not fully supported by the data, which show correlative expression patterns without functional validation.
- The functional significance of predicted ligand binding (e.g., zinc, glucose, retinol) is speculative and not experimentally validated.
- The statement that "all proteins exhibited a slightly alkaline nature" is based on predicted pI values and is presented as a functional conclusion without experimental verification.
- The claim that "the absence of beta turns suggests that these proteins may adopt more linear or elongated structures" is an unsupported structural inference.
- The in-silico transcriptome analysis conclusions about cultivar-specific responses are not supported by reported statistical analysis.
- The relationship between the GEO dataset analysis and the qRT-PCR results is not clearly established, and the authors do not discuss discrepancies between the two datasets.