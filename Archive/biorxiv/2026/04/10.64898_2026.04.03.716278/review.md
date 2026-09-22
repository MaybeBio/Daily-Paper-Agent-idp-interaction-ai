## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors present ProMaya, a hierarchical multi-scale Graph-transformer framework for protein-protein interaction (PPI) identification, integrating 3D atomic geometry, electronic distribution, residue-level structure and disorder, surface mass-density signatures, and protein language-model embeddings. They report benchmarking across nine species and 47 GB of experimentally validated data, achieving consistently greater than 95% average accuracy and outperforming state-of-the-art tools by more than 12%. They further claim that explainability-driven inclusion of atomic and protein language information dramatically improved performance, potentially bypassing costly experiments. A web server is stated to be freely accessible.
- **Visible evidence base** Abstract text only; no quantitative results, benchmark details, baseline specifications, statistical analyses, or methodological descriptions are visible
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, benchmark dataset descriptions, baseline tool versions and configurations, statistical significance tests, ablation study details, and web server validation

## Reviewer
- **Overall assessment** The abstract presents an ambitious and potentially valuable framework for PPI identification, with a plausible architectural rationale and a broad feature integration strategy. However, the evidence base available for this review is limited to the abstract, which contains several strong claims that cannot be verified or fully assessed without the underlying methods and results. The performance claims, particularly the consistent greater than 95% accuracy across nine species and the greater than 12% improvement over state-of-the-art tools, require detailed benchmarking documentation, including dataset splits, cross-validation procedures, baseline configurations, and statistical significance testing. The claim that the system could "bypass costly experiments" is speculative and not supported by the evidence presented. The abstract also contains imprecise language and potential overstatements that would need clarification in the full manuscript.
- **Who would be interested in the results, and why** Computational biologists, bioinformaticians, and researchers in structural biology and systems biology would be interested in a generalizable and interpretable PPI prediction framework. The integration of multiple biophysical and sequence-derived features, combined with explainability, could appeal to those seeking to understand the molecular determinants of PPIs and to apply such tools across species. The freely accessible web server may also attract experimental biologists seeking computational prioritization of interaction candidates.
- **Major strengths** The proposed framework integrates a diverse and physically motivated set of features, including 3D atomic geometry, electronic distribution, and protein language-model embeddings, which is conceptually more comprehensive than many existing approaches. The emphasis on interpretability is a notable strength, as it addresses a common limitation in deep learning applications to biology. The reported benchmarking across multiple species suggests an intention toward generalizability, which is a key requirement for practical utility.
- **Major Concerns**  
  - **Concern ID** R1-M1  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Evidence sufficiency  
    **Claim pointer** "Highly comprehensively benchmarked across nine species and 47 GB experimentally validated data, ProMaya achieved consistently >95% average accuracy, outperforming state-of-the-art tools by >12%."  
    **Evidence pointer** Abstract only; no figures, tables, or methods provided  
    **Concern** The abstract reports exceptional performance metrics without any accompanying methodological detail or result presentation. No information is provided on how the nine species were selected, how the 47 GB dataset was curated and split, what constitutes "experimentally validated" data, which state-of-the-art tools were compared, or how the greater than 12% improvement was computed. The term "consistently" implies robustness across conditions, but no variance measures, confidence intervals, or statistical tests are reported.  
    **Why it matters** These performance claims are the central basis for the paper's significance. Without detailed benchmarking methodology and statistical validation, the claims cannot be independently assessed or reproduced. Overstated or insufficiently supported performance claims in computational biology can mislead the community and undermine trust in the tool.  
    **Resolution test** Provide a full benchmarking section with dataset descriptions, train-validation-test splits, cross-validation schemes, baseline tool versions and hyperparameters, per-species performance tables, and statistical significance tests (e.g., paired tests across multiple runs). Report confidence intervals or standard deviations for all accuracy metrics.  
  - **Concern ID** R1-M2  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Claim substantiation  
    **Claim pointer** "As driven by its explainability, the first time introduced atomic and protein language information dramatically boosted it to an outstanding level for PPI discovery in any species, potent to even bypass costly experiments."  
    **Evidence pointer** Abstract only; no ablation study or explainability analysis provided  
    **Concern** The abstract claims that the introduction of atomic and protein language information "dramatically boosted" performance and that this was "driven by its explainability." No ablation study is described that would isolate the contribution of each feature type. The phrase "first time introduced" is a novelty claim that cannot be evaluated without a literature comparison. The statement that the system is "potent to even bypass costly experiments" is a speculative extrapolation with no supporting evidence.  
    **Why it matters** The claimed contribution of specific feature types is a key scientific finding that requires systematic ablation to substantiate. The novelty claim requires a thorough literature review to establish precedence. The suggestion that computational predictions could replace experimental validation is a strong claim with significant implications and must be supported by evidence of predictive reliability far beyond what is presented.  
    **Resolution test** Include a comprehensive ablation study showing performance with and without each feature type, with statistical comparisons. Provide a literature review demonstrating the novelty of the feature combination. Reframe or remove the claim about bypassing experiments, or support it with prospective validation on newly discovered interactions confirmed experimentally.  
  - **Concern ID** R1-M3  
    **Severity** Major  
    **Blocking** No  
    **Axis** Interpretability validation  
    **Claim pointer** "ProMaya, a hierarchical multi-scale Graph-transformer framework that integrates 3D atomic geometry, electronic distribution, residue-level structure and disorder, surface mass-density signatures, and large protein language-model embeddings" and "As driven by its explainability"  
    **Evidence pointer** Abstract only; no interpretability analysis described  
    **Concern** The abstract emphasizes interpretability as a driving factor, but no details are provided on what interpretability mechanisms are used, how they are validated, or what biological insights they yield. The claim that interpretability "drove" the performance boost is unclear and not supported by any described analysis.  
    **Why it matters** Interpretability is a stated selling point of the framework. Without a clear description of the interpretability methods and their validation, the claim remains unsubstantiated. For the framework to be useful beyond prediction, the interpretability outputs must be shown to be biologically meaningful and reliable.  
    **Resolution test** Describe the interpretability methods (e.g., attention weights, gradient-based attribution, feature importance) and provide examples of interpretability outputs on specific PPI predictions, with validation against known biological knowledge or experimental evidence.  
  - **Concern ID** R1-M4  
    **Severity** Major  
    **Blocking** No  
    **Axis** Generalizability scope  
    **Claim pointer** "a hierarchical universal Deep Learning framework" and "PPI discovery in any species"  
    **Evidence pointer** Abstract only; nine species mentioned but no details on phylogenetic diversity  
    **Concern** The abstract claims universality and applicability to "any species," but benchmarking across nine species, while commendable, does not establish universality. The species selection criteria, the diversity of the species (e.g., evolutionary distance, representation of different kingdoms), and the coverage of interaction types are not described.  
    **Why it matters** The claim of universality is a strong generalization that requires evidence of performance across a broad and representative range of species and interaction types. Overgeneralization could lead to inappropriate use of the tool in contexts where it has not been validated.  
    **Resolution test** Provide a detailed description of the nine species, including their phylogenetic relationships and the diversity of interaction types represented. Discuss limitations and potential failure modes for species or interaction types not covered in the benchmark.  
- **Minor Comments**  
  - **Concern ID** R1-m1  
    **Severity** Minor  
    **Axis** Clarity  
    **Affected element** Abstract wording  
    **Evidence pointer** Abstract, first sentence  
    **Issue** The phrase "molecular lego" is informal and imprecise for a scientific abstract.  
    **Required correction** Replace with a more formal description, such as "molecular building blocks that define the physical states of cells."  
  - **Concern ID** R1-m2  
    **Severity** Minor  
    **Axis** Precision  
    **Affected element** Performance claim  
    **Evidence pointer** Abstract, benchmarking sentence  
    **Issue** The phrase "consistently >95% average accuracy" is ambiguous. It is unclear whether this refers to the mean across all species, the minimum across species, or another aggregation.  
    **Required correction** Specify the exact metric, the aggregation method, and the range or variance across species.  
  - **Concern ID** R1-m3  
    **Severity** Minor  
    **Axis** Accessibility  
    **Affected element** Web server claim  
    **Evidence pointer** Abstract, final sentence  
    **Issue** The web server URL is provided, but no information is given on its availability, usability, or whether it has been tested by external users.  
    **Required correction** Provide a brief description of the web server interface, input requirements, and any usage statistics or external testing results.  
  - **Concern ID** R1-m4  
    **Severity** Minor  
    **Axis** Terminology  
    **Affected element** Framework description  
    **Evidence pointer** Abstract, framework description  
    **Issue** The term "hierarchical multi-scale Graph-transformer" is used without definition or context for nonspecialist readers.  
    **Required correction** Provide a brief explanation of what "hierarchical multi-scale" means in this context and how the Graph-transformer architecture is applied.  
- **Technical failings that need to be addressed before the case is established** R1-M1 and R1-M2 are blocking. The central performance claims and the attributed contribution of specific feature types cannot be assessed from the abstract alone. The lack of any methodological detail, statistical analysis, or ablation study means the core case for the paper's significance is not established from the provided evidence.
- **Assessment against Nature-style criteria**  
  - **Originality** The integration of multiple biophysical features with protein language-model embeddings in a hierarchical Graph-transformer is a plausible and potentially novel combination. However, the novelty claim cannot be fully assessed without a detailed comparison to existing methods and a literature review.  
  - **Scientific importance** Accurate and interpretable PPI prediction is an important problem in molecular biology. If the performance claims are substantiated, the framework could be a valuable resource. However, the importance is contingent on the validity of the reported results.  
  - **Interdisciplinary readership** The topic is relevant to computational biology, structural biology, and systems biology. The abstract is written in a way that is partially accessible to nonspecialists, but some terminology requires clarification.  
  - **Technical soundness** Cannot be assessed from the abstract. The lack of methodological detail and statistical analysis prevents evaluation of the technical rigor.  
  - **Readability for nonspecialists** The abstract is generally readable but contains informal language and undefined technical terms that would benefit from clarification.  
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents an interesting framework and ambitious claims, but the absence of methods, results, and statistical validation means the core case cannot be evaluated. A full manuscript with detailed benchmarking, ablation studies, and interpretability analysis would be required to assess whether the claims are supported. The recommendation is supportive in principle if the technical concerns are resolved in the full manuscript.

## Risk / unsupported claims
- The claim of "consistently >95% average accuracy" across nine species is unsupported without detailed benchmarking data and statistical analysis.
- The claim of outperforming state-of-the-art tools by greater than 12% is unsupported without specification of baselines, datasets, and evaluation protocols.
- The claim that atomic and protein language information "dramatically boosted" performance is unsupported without an ablation study.
- The claim that the system is "potent to even bypass costly experiments" is speculative and unsupported.
- The claim of "universal" applicability to "any species" is not supported by the limited benchmarking description.
- The novelty claim of "first time introduced" atomic and protein language information cannot be evaluated without a literature comparison.
- The web server's functionality and accessibility cannot be verified from the abstract alone.