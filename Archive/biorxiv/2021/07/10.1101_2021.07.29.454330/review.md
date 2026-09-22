## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) as provided
- **Assessment boundary** Scientific content, methodology, claims, and evidence as presented in the provided text; no external data or figures were available for inspection
- **Shared manuscript claim summary** The authors present "reverse homology," a self-supervised contrastive learning approach that uses evolutionary conservation among homologous intrinsically disordered regions (IDRs) as a training signal. The method is claimed to discover interpretable molecular features of IDRs, including motifs, repeats, and bulk physicochemical properties, without prior knowledge or supervision. The authors demonstrate feature diversity in yeast and human models, show correlation with literature-curated features, and provide case studies suggesting the method can generate novel biological hypotheses.
- **Visible evidence base** Text descriptions of results, figures referenced but not provided, supplementary files referenced but not provided, methods section
- **Missing materials affecting confidence** All figures, supplementary files, tables, and supplementary methods are referenced but not provided; no quantitative results (e.g., performance metrics, statistical test outputs beyond p-values) are visible in the text; no code or data were inspected

## Reviewer
- **Overall assessment** This manuscript presents a conceptually interesting and potentially valuable approach to feature discovery in intrinsically disordered regions. The core idea of using evolutionary conservation as a contrastive learning signal is well-motivated and distinct from existing self-supervised protein language models. The authors demonstrate that their method learns features that align with known biology and can generate testable hypotheses. However, the provided text alone is insufficient to fully evaluate the technical soundness and robustness of the claims. Key quantitative results, figure contents, and supplementary analyses are not visible, limiting the ability to assess the strength of the evidence. The manuscript would benefit from clearer presentation of validation metrics, baselines, and the biological significance of the discovered features.
- **Who would be interested in the results, and why** Researchers in computational biology, particularly those working on intrinsically disordered proteins, protein function prediction, and self-supervised learning for biological sequences. The approach may also interest experimental biologists studying IDR function, as the method offers a systematic, unbiased way to generate hypotheses about functional features in poorly characterized regions. The interpretability focus distinguishes this work from purely predictive deep learning approaches and may appeal to a broad readership interested in explainable AI in biology.
- **Major strengths** The conceptual framing of "reverse homology" is novel and well-articulated. The use of evolutionary conservation as a self-supervised signal is biologically principled and avoids the need for labeled data. The authors explicitly address the interpretability of learned features, which is often neglected in deep learning studies. The demonstration that the method can rediscover known features and suggest new ones (e.g., the RG/aromatic preference in phase-separating proteins) is compelling. The inclusion of both yeast and human models suggests generalizability.
- **Major Concerns** The most significant concern is the lack of visible quantitative evidence. The text describes results but does not provide the actual data, figures, or tables needed to evaluate the strength of the claims. The comparison to literature-curated features is described qualitatively, and the benchmark against DALEL is mentioned but not shown. The claim that the method outperforms or is comparable to existing approaches cannot be assessed. Additionally, the biological significance of the discovered features is presented through selected examples, but the systematic evaluation of all 512 features is not visible. The robustness of the method to different homology definitions, alignment quality, and dataset biases is not discussed in the visible text.
- **Minor Comments** The manuscript would benefit from a more explicit statement of the limitations of the approach, particularly regarding species-specific features and the reliance on accurate homology detection. The discussion of why language model-based representations underperform in interpretability could be expanded. The authors mention that some features are redundant, but the implications of this redundancy for downstream analyses are not fully explored. The methods section is detailed but would benefit from a clearer description of the hyperparameter choices and their justification.
- **Technical failings that need to be addressed before the case is established** The absence of visible quantitative results is a critical gap. The authors must provide the actual figures, tables, and supplementary analyses to support their claims. Specifically, the correlation analysis with literature-curated features, the benchmark against DALEL, the classification performance on downstream tasks, and the enrichment analyses need to be shown. Without these, the technical soundness of the approach cannot be fully evaluated.
- **Assessment against Nature-style criteria**  
  *Originality*: High. The reverse homology concept is a novel contribution that combines evolutionary biology with contrastive learning in a way not previously reported.  
  *Scientific importance*: Potentially high. IDRs are poorly understood and a systematic, unbiased feature discovery method could have broad impact. However, the importance depends on the robustness and generalizability of the method, which cannot be fully assessed from the provided text.  
  *Interdisciplinary readership*: Moderate to high. The work bridges computational biology, evolutionary biology, and deep learning, and the interpretability focus may attract experimentalists. However, the presentation assumes familiarity with both deep learning and IDR biology, which may limit accessibility.  
  *Technical soundness*: Cannot be fully assessed. The methodology is described in detail, but the lack of visible results prevents evaluation of whether the claims are supported.  
  *Readability for nonspecialists*: Moderate. The abstract and introduction are accessible, but the results and methods sections are dense and assume significant background knowledge.
- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual contribution is strong and the approach is promising, but the current submission does not provide sufficient visible evidence to establish the case. The authors should provide the missing figures, tables, and supplementary analyses, and clarify the quantitative basis for their claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that reverse homology learns features that are "significantly more correlated with literature-curated features than a random model" and that the method achieves comparable performance to DALEL on motif discovery benchmarks.
- **Evidence pointer** Results section, Figures 3 and 5, Supplementary Files 3, 4, and 6 (none visible in provided text)
- **Concern** The text describes these results but does not provide the actual data, figures, or tables. The reader cannot see the correlation values, the benchmark results, or the statistical tests. Without this evidence, the claims of quantitative performance cannot be verified.
- **Why it matters** The central claim of the paper is that reverse homology discovers meaningful features. This claim rests on the quantitative comparisons to literature-curated features and existing motif finders. If these results are not shown, the reader cannot assess whether the method actually works as described.
- **Resolution test** Provide the actual figures and tables showing the correlation analysis, the DALEL benchmark, and the classification performance. Include the specific numbers, statistical tests, and confidence intervals.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical validation
- **Claim pointer** The authors claim that the reverse homology task induces the model to learn "a wide diversity of biochemically sensible features" and that these features are enriched for functional terms.
- **Evidence pointer** Results section, Figures 2 and 4, Supplementary Files 1, 2, and 5 (none visible in provided text)
- **Concern** The text describes the feature diversity and enrichment analyses but does not show the UMAP plot, the sequence logos, the enrichment tables, or the mutation maps. The reader cannot evaluate whether the features are indeed diverse, sensible, and biologically relevant.
- **Why it matters** The qualitative claims about feature interpretability are a key differentiator of this work. Without seeing the actual visualizations and enrichment data, the reader cannot judge whether the features are meaningful or whether the interpretation methods are effective.
- **Resolution test** Provide the UMAP plot, sequence logos, mutation maps, and enrichment tables. Include the specific enrichment scores, p-values, and the criteria used to define "highly activating" features.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological robustness
- **Claim pointer** The authors claim that the method is "unbiased by prior knowledge" and that it can discover features "without having to pre-specify motifs/features of interest."
- **Evidence pointer** Introduction, Discussion, Methods (no specific location provided)
- **Concern** The text does not discuss the sensitivity of the method to key hyperparameters, such as the number of homologs per set, the query set size, the target set size, or the choice of convolutional architecture. The authors also do not address how the results might change with different homology detection methods or alignment quality. The claim of being "unbiased" is strong and requires a more thorough discussion of potential biases introduced by the data processing steps.
- **Why it matters** The generalizability and robustness of the method are central to its utility. If the method is highly sensitive to these choices, the conclusions may not be broadly applicable. The claim of being "unbiased" is particularly important and needs to be qualified with a discussion of the limitations.
- **Resolution test** Provide a sensitivity analysis or at least a discussion of how the results depend on key hyperparameters and data processing choices. Address the potential biases in the homology detection and alignment steps.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Biological significance
- **Claim pointer** The authors claim that their analysis of specific features (e.g., the RG/aromatic preference in phase-separating proteins, the doubly phosphorylated PKA consensus) generates novel biological hypotheses.
- **Evidence pointer** Results section, Figures 4 and 5, Supplementary Figure 1 (none visible in provided text)
- **Concern** The text describes these case studies but does not provide the full data or the statistical support. For example, the claim about the doubly phosphorylated PKA consensus is based on a Fisher exact test, but the actual numbers and the full analysis are not shown. The biological significance of the features is presented through selected examples, but the systematic evaluation of all features is not visible.
- **Why it matters** The biological insights are a major selling point of the paper. Without the full data, the reader cannot assess whether these hypotheses are well-supported or whether they are anecdotal.
- **Resolution test** Provide the full data for the case studies, including the mutation maps, the enrichment analyses, and the statistical tests. Include a more systematic evaluation of the biological significance of the discovered features.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The abstract is dense and uses technical jargon ("reverse homology," "contrastive learning") without sufficient context for a general reader.
- **Required correction** Consider adding a brief explanation of what "reverse homology" means and why it is a novel approach in the abstract.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "Training datasets"
- **Evidence pointer** Methods, "Training datasets" section
- **Issue** The description of the human IDR dataset filtering is complex and relies on several heuristics. The exact parameters and the rationale for these choices are not fully explained.
- **Required correction** Provide a more detailed description of the filtering steps, including the specific thresholds and the reasoning behind them.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results, "Reverse homology learns a diverse range of features"
- **Evidence pointer** Results, Figure 2 description
- **Issue** The UMAP plot is described as showing "four major axes of features," but the text does not explain how these axes were defined or how the clusters were identified.
- **Required correction** Clarify the methodology for identifying the axes and clusters in the UMAP plot.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Comparison to prior work
- **Affected element** Discussion
- **Evidence pointer** Discussion, first paragraph
- **Issue** The discussion compares the approach to language model-based representations but does not provide a detailed comparison of the types of features learned by each method.
- **Required correction** Consider adding a more explicit comparison of the features learned by reverse homology versus those learned by language models, perhaps with examples.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Limitations
- **Affected element** Discussion
- **Evidence pointer** Discussion, "A more general limitation" paragraph
- **Issue** The discussion of limitations is brief and does not address the potential for the method to miss species-specific or lineage-specific features.
- **Required correction** Expand the discussion of limitations to include the issue of species-specific features and the potential for the method to be biased toward conserved features.

## Risk / unsupported claims
- The claim that reverse homology learns features "significantly more correlated with literature-curated features than a random model" is unsupported in the provided text, as the actual correlation data are not shown.
- The claim that the method achieves "comparable performance to DALEL" on motif discovery benchmarks is unsupported, as the benchmark results are not shown.
- The claim that the method is "unbiased by prior knowledge" is not fully supported, as the potential biases introduced by the data processing and homology detection steps are not discussed.
- The claim that the analysis of specific features generates "novel biological hypotheses" is not fully supported, as the full data and statistical analyses for these case studies are not shown.
- The claim that the method can be used for "hypothesis discovery at an unprecedented scale" is not supported by the visible evidence, as the systematic evaluation of all 512 features is not shown.