## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary information descriptions
- **Assessment boundary** Scientific validity, technical soundness, claims-to-evidence alignment, methodological rigor, and clarity of the presented work
- **Shared manuscript claim summary** The authors present LLPSense, a machine learning framework that integrates protein language model embeddings with environmental parameters (concentration, temperature, pH, crowding agents, salts, glycerol) to predict condition-dependent protein phase separation. They claim accurate predictions validated experimentally for SGTA, RAD23A, α-synuclein variants, and UBQLN4, including the ability to guide mutagenesis to modulate phase behavior.
- **Visible evidence base** Main text figures 1–6, supplementary figures 1–23 (described), supplementary tables 1–7 (described), methods section, and source data statement
- **Missing materials affecting confidence** Supplementary figures, tables, and data files are referenced but not provided in the submitted material. Experimental protocols for protein expression, purification, and turbidity assays are described only in summary form. No raw data or statistical analysis details are available for independent verification.

## Reviewer
- **Overall assessment** This manuscript presents a potentially valuable advance in condition-aware prediction of protein phase separation. The integration of environmental parameters with protein language model embeddings is conceptually sound and addresses a recognized limitation of sequence-only predictors. The experimental validations, particularly the identification of SGTA as a novel phase-separating protein and the LCST-to-UCST reprogramming of UBQLN4, are compelling demonstrations of the framework's utility. However, several technical concerns regarding dataset construction, model evaluation, and the strength of some experimental claims require clarification before the case is fully established.

- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, and membraneless organelles would find this work directly relevant. Additionally, the machine learning community focused on protein property prediction, and researchers studying neurodegenerative diseases where phase separation plays a role (e.g., Parkinson's disease, ALS), would be interested. The demonstrated ability to engineer phase behavior through guided mutagenesis has potential applications in synthetic biology and biotechnology.

- **Major strengths** 1) The conceptual advance of incorporating environmental conditions into phase separation prediction addresses a critical gap in existing tools. 2) The use of protein language model embeddings provides a modern, scalable representation. 3) Multiple independent experimental validations across different proteins and conditions strengthen the claims. 4) The identification of SGTA as a previously unrecognized phase-separating protein with complex reentrant behavior is a notable discovery. 5) The demonstration of bidirectional prediction (enhancement and suppression) for α-synuclein mutations has direct disease relevance. 6) The successful reprogramming of UBQLN4 from LCST to UCST behavior is a striking proof-of-concept for design applications.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Dataset construction and curation
- **Claim pointer** The authors claim to have assembled "a rigorously curated, ML-ready dataset by filtering LLPSDB v2 specifically for single-protein entries" with 13 condition variables.
- **Evidence pointer** Methods section, "Sampling of experimental condition data"; Supplementary Table 5
- **Concern** The dataset curation process is described only at a high level. Critical details are missing: How many total entries were obtained after filtering? What was the distribution of positive versus negative examples? How were conflicting or ambiguous experimental records (e.g., a protein reported as both phase-separating and non-phase-separating under similar conditions) resolved? The range-expansion strategy for open-ended values (10-fold above or below the boundary) could introduce unrealistic or physically meaningless training instances. The random subsampling for combinatorial expansions exceeding 100 configurations may bias the dataset toward certain conditions.
- **Why it matters** The quality and balance of the training dataset directly determine the reliability of the model and the validity of all downstream predictions. Without a clear description of dataset size, class balance, and handling of ambiguous records, the reported performance metrics cannot be properly interpreted. Biased or unrealistic training data could lead to overconfident predictions that do not generalize.
- **Resolution test** Provide a detailed breakdown of the final dataset: number of unique proteins, number of condition-specific entries, positive/negative ratio, and the distribution of each condition variable. Describe the resolution process for conflicting records. Justify the range-expansion strategy with examples and demonstrate that it does not introduce artifacts. Ideally, make the curated dataset publicly available for independent inspection.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Model evaluation and generalization
- **Claim pointer** The authors claim LLPSense "achieves accurate, condition-aware predictions of phase separation" and outperforms Droppler, including when Droppler is retrained with ProtT5 embeddings.
- **Evidence pointer** Figure 1f–h; Supplementary Figures 1–2
- **Concern** The evaluation methodology is not fully described. The cluster-based cross-validation using MMseqs2 at 20% identity is appropriate for sequence-level generalization, but it is unclear whether the condition variables in the test folds overlap with training folds. If the same condition combinations appear in both training and test sets, the model could be memorizing condition-specific patterns rather than learning to generalize across the condition space. Additionally, the comparison with Droppler is presented as a bar chart and scatter plot, but no statistical significance testing is reported. The performance difference, while seemingly large, needs formal evaluation.
- **Why it matters** The central claim of the paper is that LLPSense provides superior condition-aware predictions. If the evaluation protocol allows information leakage between training and test folds, or if the performance advantage over Droppler is not statistically robust, the main conclusion is weakened. The field needs reliable benchmarks to adopt new tools.
- **Resolution test** Clarify whether condition variables were stratified across cross-validation folds. Report confidence intervals or statistical tests for the performance comparisons. Consider additional evaluation on a held-out set of proteins and conditions not present in LLPSDB v2. Provide a detailed description of the Droppler retraining procedure to ensure a fair comparison.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Experimental validation of SGTA reentrant behavior
- **Claim pointer** The authors state that SGTA displays "complex, temperature-dependent reentrant behavior" that was "accurately predicted and subsequently confirmed experimentally."
- **Evidence pointer** Figure 2c–f
- **Concern** The experimental validation of SGTA's reentrant phase behavior is presented in a condensed form. The turbidity data in Figure 2e show increased turbidity at both low (4°C) and high (≥40°C) temperatures, but the interpretation of this as "reentrant" behavior requires careful consideration. Reentrant phase separation typically implies a non-monotonic phase boundary where a system transitions from one-phase to two-phase and back to one-phase as a condition is varied. The data presented show turbidity at discrete temperatures, but it is unclear whether the system fully returns to a single-phase state at intermediate temperatures. Additionally, the microscopy images in Figure 2f are described qualitatively; quantitative analysis of droplet size, number, and morphology would strengthen the claim.
- **Why it matters** The identification of SGTA as a novel phase-separating protein with unusual reentrant behavior is a significant claim that extends beyond simple prediction accuracy. If the experimental evidence for reentrant behavior is not robust, this claim is overstated. The phase diagram of a protein is a fundamental biophysical property, and accurate characterization is essential.
- **Resolution test** Provide a more complete phase diagram for SGTA, including turbidity measurements at finer temperature intervals and multiple protein concentrations. Include quantitative image analysis of droplet formation (e.g., number, size distribution, circularity) as a function of temperature. Consider complementary techniques such as fluorescence recovery after photobleaching (FRAP) or differential interference contrast microscopy to confirm liquid-like properties.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** α-synuclein mutational analysis
- **Claim pointer** The authors claim that LLPSense "accurately predicts mutations in Parkinson's disease-associated α-synuclein that either enhance or suppress phase separation" and that the experimental trend mirrors predictions.
- **Evidence pointer** Figure 4d–f; Supplementary Figures 9–11
- **Concern** The mutational analysis is a key demonstration of the framework's utility for disease-relevant proteins. However, the experimental validation is limited to turbidity measurements at a single time point (30 minutes) and a limited set of conditions. The claim of "single-residue resolution" is supported by the computational screen, but the experimental validation only tests a small number of variants. The authors note that E4 and E8 exhibited "pronounced aggregation and structural instability," which complicates the interpretation of turbidity as a direct measure of phase separation. The distinction between liquid-liquid phase separation and aggregation is critical, and the manuscript acknowledges this limitation but does not fully address it for the α-synuclein variants.
- **Why it matters** The ability to predict the effect of disease-associated mutations on phase separation has direct translational relevance. If the experimental validation does not clearly distinguish between phase separation and aggregation, the conclusions about specific mutations may be misleading. The field has learned that turbidity alone is insufficient to characterize phase behavior.
- **Resolution test** Include microscopy images for the α-synuclein variants to confirm the liquid-like nature of the condensates. Perform additional characterization such as FRAP or fluorescence microscopy with a labeled protein. Clarify the relationship between turbidity and phase separation for these variants, particularly for E4 and E8 where aggregation is noted. Consider testing additional mutations from the predicted landscape to strengthen the correlation.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** UBQLN4 engineering
- **Claim pointer** The authors claim that LLPSense-guided mutagenesis "shifted its phase behavior toward an upper critical solution temperature (UCST)-like regime" for UBQLN4.
- **Evidence pointer** Figure 6c–d; Supplementary Figure 14
- **Concern** The reprogramming of UBQLN4 from LCST to UCST behavior is a striking result, but the experimental evidence is limited. The turbidity data in Figure 6c show a comparison of WT, m10, and UCST variants, but the temperature range and number of conditions tested are not fully described. The claim of a "shift toward UCST-like regime" implies a qualitative change in the phase diagram, but the data presented may not fully support this. Additionally, the selection of mutations is based on the slope of ΔProbability, but the rationale for choosing 10 mutations per round and the potential for epistatic effects among the accumulated mutations are not discussed.
- **Why it matters** The ability to engineer phase behavior through computational guidance is a major advance with potential applications in synthetic biology. However, the claim of reprogramming the thermodynamic character of a protein is strong and requires robust experimental evidence. If the observed changes are subtle or condition-specific, the claim may be overstated.
- **Resolution Test** Provide a more complete characterization of the phase diagrams for WT, m10, and UCST variants, including turbidity measurements across a wider temperature range and multiple protein concentrations. Include microscopy images to confirm the nature of the condensates. Discuss the potential for epistatic interactions among the 30 accumulated mutations and whether the individual contributions are additive.

- **Concern ID** R1-M6
- **Severity** Major
- **Blocking** No
- **Axis** Proteome-wide analysis
- **Claim pointer** The authors claim to have applied LLPSense to "map the global landscape of protein phase separation across the human proteome under diverse physicochemical conditions."
- **Evidence pointer** Supplementary Figures 6–7, 15–17, 20, 23
- **Concern** The proteome-wide analysis is presented as a demonstration of the framework's scalability and utility. However, the results are only described in supplementary figures, and the main text provides limited interpretation. The claim that increasing NaCl from 500 mM to 1000 mM results in a "statistically significant increase in predicted probability" is interesting but requires context. What is the biological relevance of such high salt concentrations? The correlation analyses between sequence features and salt sensitivity are potentially valuable but are not discussed in sufficient detail.
- **Why it matters** The proteome-wide analysis positions LLPSense as a tool for hypothesis generation and large-scale screening. If the results are not properly interpreted and contextualized, the claims may be seen as superficial. The field would benefit from clear guidance on how to use these predictions.
- **Resolution Test** Provide a more detailed discussion of the proteome-wide results in the main text. Highlight specific findings that are novel or unexpected. Discuss the limitations of the predictions at extreme conditions. Consider validating a subset of the proteome-wide predictions experimentally to demonstrate the framework's utility at scale.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of model architecture
- **Affected element** Figure 1a
- **Evidence pointer** Figure 1a
- **Issue** The schematic overview of the LLPSeq and LLPSense architectures is described in the figure legend but the figure itself is not provided in the submitted text. The description in the main text is brief.
- **Required correction** Ensure the figure clearly shows the flow from sequence to ProtT5 embeddings, the concatenation with condition variables, and the XGBoost classifier. Consider adding a panel showing the dimensionality of each feature vector.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 1f
- **Evidence pointer** Figure 1f
- **Issue** The performance comparison with Droppler is shown as bar charts with error bars, but the statistical significance of the differences is not reported.
- **Required correction** Add statistical significance indicators (e.g., p-values from paired tests across cross-validation folds) to the bar charts or state in the text that the differences are significant.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Experimental reproducibility
- **Affected element** Methods, "Turbidity assays"
- **Evidence pointer** Methods section
- **Issue** The turbidity assay description states that measurements were taken 30 minutes after induction, but the rationale for this time point is not given. The number of replicates and the variability between replicates are not reported.
- **Required correction** Provide a justification for the 30-minute time point. Report the number of independent replicates and the standard deviation or standard error for each turbidity measurement.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data availability statement
- **Evidence pointer** Not explicitly stated in the text
- **Issue** The manuscript states that "All curated datasets and preprocessing scripts used in this study are publicly available" but the specific repository or accession numbers are not provided in the main text.
- **Required correction** Provide the specific repository name and accession numbers or DOIs for the datasets and code in the Data Availability section.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Comparison with existing tools
- **Affected element** Introduction, Discussion
- **Evidence pointer** Introduction, Discussion
- **Issue** The comparison with catGRANULE 2.0 is mentioned in the context of α-synuclein mutations, but a broader comparison with other existing tools (e.g., PSPer, FuzDrop) is not provided.
- **Required correction** Add a brief discussion of how LLPSense compares with other available prediction tools, highlighting the unique features of the condition-aware approach.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** Throughout
- **Issue** The term "reentrant" is used to describe SGTA's phase behavior, but the definition of this term in the context of phase separation is not provided for readers unfamiliar with the concept.
- **Required correction** Define "reentrant phase behavior" when first used, explaining that it refers to a non-monotonic phase boundary where phase separation occurs in two distinct regions of parameter space.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 2e
- **Evidence pointer** Figure 2e
- **Issue** The turbidity data for SGTA are presented as a line graph, but the individual data points are not shown. This makes it difficult to assess the variability and the robustness of the observed trends.
- **Required correction** Show individual data points overlaid on the line graphs, or provide error bars representing the standard deviation of replicate measurements.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The discussion mentions limitations related to high-salt conditions and data scarcity, but the broader limitations of the approach (e.g., the binary nature of the training labels, the inability to predict material properties) are not fully addressed.
- **Required correction** Expand the discussion of limitations to include the inherent challenges of training on binary phase separation data and the potential for false positives in predictions.

## Risk / unsupported claims
- The claim that LLPSense "establishes a robust computational framework for interrogating phase landscapes" is supported by the presented validations but is somewhat broad given the limited number of proteins experimentally tested.
- The statement that LLPSeq's high prediction for α-synuclein WT is "likely driven by overfitting to the homologous β-synuclein sequence" is speculative and not directly tested.
- The claim that the proteome-wide analysis reveals "the underlying physicochemical rules governing LLPS" is not fully supported by the presented analyses, which are primarily correlational.
- The assertion that the UBQLN4-UCST variant "formed condensates resembling percolated clusters" is based on qualitative microscopy observations and lacks quantitative characterization.
- The statement that "LLPSense accurately predicts the LCST behavior of both UBQLN1 and UBQLN4" is based on a single experimental validation for UBQLN4 and no experimental validation for UBQLN1.
- The claim that the framework can "facilitate mechanistic disease studies" is a reasonable inference but is not directly demonstrated in this work.