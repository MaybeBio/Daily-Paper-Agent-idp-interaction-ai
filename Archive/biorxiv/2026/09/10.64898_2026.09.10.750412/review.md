## Review setup

- **Input scope** Full manuscript text including abstract, main text, methods, and supplementary figure/table references
- **Assessment boundary** Scientific validity, methodological soundness, reproducibility, and claims as supported by the provided evidence
- **Shared manuscript claim summary** The authors present ICARus, a positive-unlabelled learning framework that integrates protein language model-derived protein-protein interaction predictions to refine a genome-wide RNAi screen for vaccinia virus host factors. They report improved prioritisation of known host factors, altered functional landscape of top-ranked genes, and provide an agentic-AI-enabled community resource (ICARusPox).
- **Visible evidence base** Abstract, main text sections (Results, Discussion, Methods), figure legends referenced but figures not provided, tables referenced but not provided, supplementary materials referenced but not provided
- **Missing materials affecting confidence** All figures, tables, and supplementary materials are referenced but not included in the provided text. This substantially limits the ability to verify quantitative claims, model performance metrics, and visual evidence.

## Reviewer

- **Overall assessment** The manuscript addresses a relevant problem in functional genomics screens, namely the mitigation of off-target effects and assay noise through computational refinement. The conceptual idea of using pLM-derived PPI predictions as a prior for PU learning is interesting and potentially useful. However, the provided text alone does not contain sufficient evidence to evaluate the central claims. Key quantitative results, model comparisons, and validation data are all located in figures and tables that were not supplied. The methodological description is incomplete in several critical areas, including the construction of negative training data, the handling of multi-protein genes, and the precise architecture of the PU learning model. The manuscript would benefit from clearer articulation of what is novel relative to existing PPI-guided hit prioritisation approaches.

- **Who would be interested in the results, and why** Researchers in functional genomics and RNAi screening would be interested in the methodological contribution of PPI-guided refinement. The poxvirus community would value the genome-wide host factor dataset. The agentic-AI resource may appeal to bioinformaticians developing AI-assisted data exploration tools. However, the broad interdisciplinary appeal claimed in the abstract is not fully substantiated by the provided evidence.

- **Major strengths** The problem addressed is genuine and important. The use of pLM-derived PPI predictions as a prior for PU learning is a sensible and potentially generalisable strategy. The authors acknowledge limitations of their approach, including dependence on the positive reference set and potential biases in PPI data. The decision to publish raw and refined data as a community resource is commendable.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The claim that ICARus "enhances the identification of human genes with potential antiviral function" and "improves host factor prioritisation" relative to the uncorrected screen.
- **Evidence pointer** Results sections "Benchmarking protein-protein interaction models" and "A PU learning framework enables PPI-informed VACV host factor prioritisation"; Tables 1-3; Figures 2a-c; location not provided
- **Concern** The central quantitative claims of the manuscript are presented exclusively in tables and figures that were not included in the provided material. Table 1 reports benchmark comparisons, Table 2 reports fine-tuning results, Table 3 reports PU learning performance, and Figure 2 presents ROC curves, PR curves, and enrichment analyses. Without these data, the reader cannot verify that ICARus outperforms the uncorrected screen or that the PPI features contain meaningful signal. The text states performance metrics but provides no numerical values in the body text.
- **Why it matters** The entire scientific contribution rests on the demonstration that the proposed method improves hit prioritisation. Without access to the actual performance numbers, the claim is unverifiable.
- **Resolution test** Provide the actual performance metrics in the text or ensure figures and tables are available for review. The authors should state specific AUROC, PR AUC, and enrichment values in the main text.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological completeness
- **Claim pointer** The claim that ICARus is a "positive-unlabelled read-out refinement framework" that uses PPI information to refine screen results.
- **Evidence pointer** Methods sections "Construction of the PU learning data set" and "Architecture and training of the multimodal MLP"; location not provided
- **Concern** The description of the PU learning framework is incomplete in several respects. First, the positive set is described as "confirmed VACV host factors curated from published literature" but the size, curation criteria, and literature sources are not specified. Second, the negative set construction is not described at all for the PU learning task, which is a critical omission given that PU learning by definition operates without negative labels. Third, the aggregation of protein-level PPI predictions to gene-level features via max-pooling is described, but the rationale for this choice over other aggregation methods is not given. Fourth, the architecture of the PU learning model itself is not described beyond being a "multimodal MLP" with switchable branches.
- **Why it matters** Reproducibility is a core requirement for methodological contributions. Without a complete description of the positive set, the PU learning setup, and the model architecture, other researchers cannot implement or evaluate the method.
- **Resolution test** Provide a complete description of the positive set curation process, the PU learning setup including how unlabelled data are handled, and the full architecture of the model including layer sizes, activation functions, and training details.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Validation rigour
- **Claim pointer** The claim that the PPI features contain "meaningful predictive signal" and that the model "consistently assigns higher scores to known host factors than to unlabelled genes".
- **Evidence pointer** Results section "A PU learning framework enables PPI-informed VACV host factor prioritisation"; Figure 2; location not provided
- **Concern** The evaluation of the PU learning model relies on known host factors as positives and treats all other genes as negatives. The authors acknowledge this is conservative because some unlabelled genes are likely undiscovered host factors. However, the text does not describe any additional validation of the prioritised hits, such as experimental validation of a subset of novel candidates, comparison to independent datasets, or assessment of whether the prioritised genes are enriched for functionally relevant categories beyond the known host factors. The functional enrichment analysis in Figure 3c is descriptive but does not constitute independent validation.
- **Why it matters** Without independent validation, the practical utility of the prioritisation for discovering novel host factors remains uncertain. The conservative evaluation may overstate or understate performance in ways that are not quantifiable from the provided text.
- **Resolution test** Include additional validation, such as experimental confirmation of a subset of novel high-confidence predictions, or comparison of prioritised genes with independent genome-scale datasets (e.g., CRISPR screens, transcriptomic studies).

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Benchmarking adequacy
- **Claim pointer** The claim that xCAPT5 was selected as the PPI prediction model based on benchmark results showing it "consistently outperformed the other models across multiple metrics."
- **Evidence pointer** Results section "Benchmarking protein-protein interaction models"; Table 1; location not provided
- **Concern** The benchmark compares three pLM-based models on a "curated VACV-specific PPI test set." The text does not describe the size, composition, or curation of this test set. It is unclear whether the test set is sufficiently large and diverse to draw reliable conclusions about model performance. Additionally, the choice of models benchmarked is limited to pLM-based approaches, and it is unclear how these compare to simpler sequence-based or structure-based PPI prediction methods that might be computationally more efficient.
- **Why it matters** The selection of the PPI prediction model is a critical design choice. If the benchmark is based on a small or biased test set, the conclusions may not generalise. A comparison to non-pLM baselines would strengthen the case for the specific model choice.
- **Resolution test** Describe the test set in detail, including size, composition, and curation criteria. Consider adding non-pLM baselines to the benchmark to demonstrate the added value of pLM-based approaches.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Screen quality assessment
- **Claim pointer** The claim that the genome-wide RNAi screen was performed and that the Z'-score of 0.43 indicates "marginal" linear separability.
- **Evidence pointer** Results section "Genome-wide RNAi screen for human host genes involved in VACV infection"; Figure 1a; location not provided
- **Concern** The Z'-score of 0.43 is reported as indicating marginal quality, yet the screen is used as the foundation for the entire study. The text does not describe any quality control measures beyond the Z'-score, such as plate-level variability, batch effects, replicate concordance, or confirmation of knockdown efficiency. It is unclear whether the screen data are of sufficient quality for the downstream analysis to be meaningful.
- **Why it matters** A screen with marginal quality metrics may produce unreliable primary data. The refinement method can only be as good as the underlying screen data. If the screen quality is poor, the refinement may be fitting noise rather than recovering true signals.
- **Resolution test** Provide additional quality control metrics for the screen, including replicate correlations, plate-level variability, and any confirmatory experiments demonstrating the screen's ability to detect known host factors.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states that ICARus "boosts the discovery of vaccinia virus-host interactions" but does not quantify the improvement. A specific metric, such as the increase in recall or precision relative to the uncorrected screen, would strengthen the abstract.
- **Required correction** Include a quantitative statement of improvement in the abstract.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "VACV screening assay"
- **Evidence pointer** Methods section "VACV screening assay"; location not provided
- **Issue** The screening assay is described as following "an identical protocol to (Rämö et al. 2014)" but the reference is not listed in the provided text. The reader cannot verify the protocol details.
- **Required correction** Provide the full citation for Rämö et al. 2014 and ensure it is included in the reference list.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results, "A PU learning framework enables PPI-informed VACV host factor prioritization"
- **Evidence pointer** Results section "A PU learning framework enables PPI-informed VACV host factor prioritization"; Figure 3c; location not provided
- **Concern** The functional enrichment analysis shows increased representation of categories such as "Membrane trafficking & vesicular transport" and "Ubiquitin-mediated protein degradation" after refinement. The authors state this is consistent with established VACV biology, but the text does not discuss whether any categories were depleted after refinement or whether the broadening is always beneficial. The limitation section mentions reduced representation of autophagy-related genes, but this is not connected to the enrichment analysis.
- **Required correction** Discuss both gains and losses in functional category representation after refinement, and address whether the broadening is always desirable or could introduce false positives.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Resource description
- **Affected element** Results, "An interactive community resource"
- **Evidence pointer** Results section "An interactive community resource"; Figure 4; location not provided
- **Issue** The description of ICARusPox is brief. The text mentions a dashboard, script execution, and LLM connectivity, but does not describe the underlying data model, the specific functions exposed, or the technical architecture. The claim that it is "agentic" is not clearly defined.
- **Required correction** Provide a more detailed description of the resource, including the data schema, the API or function set, and a clear definition of what makes it "agentic".

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical rigour
- **Affected element** Methods, "Evaluation metrics"
- **Evidence pointer** Methods section "Evaluation metrics"; location not provided
- **Issue** The evaluation metrics are defined in equations 1-4, but the text does not describe how statistical significance of differences between models or between refined and unrefined results was assessed. Confidence intervals or significance tests for the reported metrics are not mentioned.
- **Required correction** Describe the statistical methods used to assess the significance of performance differences, or state that no significance testing was performed.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data availability statement
- **Evidence pointer** Data availability section; location not provided
- **Issue** The data availability statement provides a Zenodo link but does not specify what data are included (raw screen data, refined scores, model weights, code). The GitHub repository is mentioned in the Code availability section but the relationship between the two is unclear.
- **Required correction** Clarify what data and code are available at each location and provide a clear description of the contents.

## Risk / unsupported claims

- The claim that ICARus "enhances the identification of human genes with potential antiviral function" is unsupported in the provided text because the quantitative results are in missing figures and tables.
- The claim that the PPI features contain "meaningful predictive signal" is unsupported without the permutation test results shown in Table 3 and Figure 2.
- The claim that the refinement "broadens the functional landscape" of top-ranked genes is based on Figure 3c, which was not provided.
- The claim that ICARusPox is an "agentic-AI-enabled community resource" is not fully supported by the description provided, as the term "agentic" is not defined and the technical capabilities are only briefly described.
- The claim that the screen Z'-score of 0.43 indicates "marginal" quality is presented without comparison to typical values for similar screens or discussion of whether this level of quality is sufficient for the downstream analysis.
- The claim that the multimodal variant "did not outperform the PPI-only model" is stated without providing the actual comparison data (Figure S7, Tables S3 and S5 are referenced but not provided).
- The claim that the framework is "the first application of PU learning to host factor prioritisation in viral RNAi screens" is a strong novelty claim that would require a thorough literature search to substantiate.