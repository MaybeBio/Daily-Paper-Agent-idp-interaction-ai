## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods summary, and supplemental information descriptions
- **Assessment boundary** Scientific validity, methodological rigor, conceptual novelty, and clarity of claims as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors define a new class of condensation-prone RNAs ("smOOPs") identified by semi-extractability and OOPS assays across three early developmental stages in mouse. They report that smOOPs form larger intracellular foci, are more interconnected in RNA-RNA interaction networks, are heavily bound by RBPs, and can be predicted by a deep learning model from sequence and regulatory features. They further report that smOOPs encode proteins enriched in intrinsically disordered regions with high predicted condensate propensity.
- **Visible evidence base** Results sections describing Figures 1–5, supplemental figure descriptions (S1–S5), methods summaries, and data availability statements
- **Missing materials affecting confidence** Full figure panels, exact statistical outputs, model performance tables, supplemental tables, and detailed method parameters were not fully visible in the provided text

## Reviewer
- **Overall assessment** This manuscript presents a potentially valuable resource and a novel integrative framework for identifying condensation-prone RNAs. The combination of two orthogonal biochemical assays (semi-extractability and OOPS) with network analysis and deep learning is conceptually appealing and could be of broad interest. However, several technical concerns need to be addressed, particularly regarding the specificity of the assays, the interpretation of the deep learning feature importance, and the strength of the causal claims about condensation propensity. The developmental aspect is somewhat underdeveloped beyond descriptive staging, and the functional significance of smOOPs remains largely speculative.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, RNA-binding proteins, phase separation, and post-transcriptional gene regulation would be the primary audience. The resource of smOOPs across developmental stages could be useful for those studying early embryogenesis and pluripotency. The deep learning framework for integrating multi-modal RNA features may also interest computational biologists working on RNA biology. The link between RNA sequence features and encoded protein disorder could attract researchers interested in the co-evolution of coding and non-coding features.

- **Major strengths**
  1. The combination of two complementary biochemical assays (semi-extractability and OOPS) to define a candidate RNA class is methodologically thoughtful and addresses limitations of each individual approach.
  2. The integration of multiple data types (RNA-seq, iCLIP, RIC-seq, sequence features) within a single deep learning framework is ambitious and provides a template for similar integrative analyses.
  3. The identification of two distinct clusters of smOOPs with different nucleotide composition, RBP-binding patterns, and functional annotations is a potentially important finding.
  4. The link between RNA-level features and encoded protein disorder is intriguing and could have implications for understanding how RNA and protein properties co-evolve to support condensate formation.
  5. The validation of smOOPs by orthogonal methods (HCR-FISH, RIC-seq networks) strengthens the core claims.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation
- **Claim pointer** The authors claim that smOOPs "localize to larger intracellular foci" and that this supports their condensation-prone nature.
- **Evidence pointer** Figure 1I, 1J, S1H–S1I; Table S2
- **Concern** The HCR-FISH experiments were performed for 17 candidate transcripts, but the selection criteria for these transcripts are not clearly described. Were they chosen to represent both clusters? Were they matched for expression level and length? The authors state that smOOPs form "larger foci" compared to non-smOOPs, but the quantification appears to be based on a relatively small number of transcripts. More importantly, the authors do not demonstrate that these foci are actually condensates or that they represent phase-separated compartments. Larger foci could arise from many mechanisms unrelated to condensation, such as increased transcription, mRNA stability, or clustering at the endoplasmic reticulum.
- **Why it matters** The claim that smOOPs are "condensation-prone" rests heavily on the interpretation that larger foci reflect condensate formation. Without direct evidence of phase separation (e.g., FRAP, fusion/fission assays, or sensitivity to 1,6-hexanediol), the functional significance of the observed foci remains unclear. The authors acknowledge this limitation in the discussion but the title and framing of the paper assert condensation-proneness as a defining feature.
- **Resolution test** Provide a more detailed description of transcript selection for HCR-FISH. Include additional validation experiments, such as co-staining with known condensate markers, or explicitly reframe the claims to be about "foci formation" rather than "condensation" where direct evidence is lacking.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Deep learning interpretation
- **Claim pointer** The authors claim that the deep learning model identifies "characteristic sequence composition, with lower sequence complexity, increased intramolecular folding, and specific RBP-binding patterns" as features of smOOPs.
- **Evidence pointer** Figure 3, S3; Table S3
- **Concern** The deep learning analysis is central to the paper's claims about the defining features of smOOPs, but the interpretability of the model is not fully established. The integrated gradients approach provides importance scores, but the authors do not demonstrate that these scores are stable across model initializations or that they reflect causal features rather than correlations. The clustering of smOOPs into two groups based on importance scores is interesting, but the robustness of this clustering is not assessed. Furthermore, the claim that "lower sequence complexity" is a feature of smOOPs is somewhat counterintuitive given that the model also identifies "increased intramolecular folding" as important, and the relationship between these features is not explored.
- **Why it matters** The deep learning framework is presented as a key methodological contribution. If the feature importance scores are not robust or if the model is overfitting to idiosyncratic features of the training set, the biological conclusions drawn from the model would be unreliable. The paper's claim to provide a "versatile resource" for identifying condensation-prone RNAs depends on the model's generalizability.
- **Resolution test** Provide stability analyses for the integrated gradients (e.g., across random seeds or model initializations). Validate the identified features on an independent dataset or through targeted mutagenesis experiments. Assess whether the two clusters are robust to different clustering methods and parameter choices.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Network analysis interpretation
- **Claim pointer** The authors claim that smOOPs "form denser RNA subnetworks than expected" based on RIC-seq data.
- **Evidence pointer** Figure 2C, 2D, S2
- **Concern** The network analysis shows that smOOPs are more interconnected than degree-matched controls, but the interpretation of this finding is not entirely clear. The authors suggest this reflects "their proximity to one another and potential spatial organization." However, RIC-seq captures RNA-RNA interactions that may be mediated by proteins or reflect co-localization in any cellular compartment, not necessarily condensates. The degree-matching controls are appropriate, but the authors do not discuss whether the observed connectivity could be explained by other factors, such as shared transcription factories or common subcellular localization driven by mRNA targeting signals.
- **Why it matters** The network analysis is used to support the claim that smOOPs are spatially organized in a way that is consistent with condensate formation. If the connectivity is driven by other mechanisms, the interpretation would need to be revised.
- **Resolution test** Perform additional analyses to determine whether the enhanced connectivity is specific to smOOPs or reflects general properties of long, highly expressed RNAs. Consider whether the connectivity pattern is consistent with known condensate organization or could be explained by alternative models.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Developmental relevance
- **Claim pointer** The authors claim that smOOPs are "developmentally regulated" and that their properties change across the three stages examined.
- **Evidence pointer** Figures 1B–1E, 5A, S5
- **Concern** The developmental aspect of the study is presented as a key feature, but the analysis is largely descriptive. The authors show that the number and identity of smOOPs change across stages, and that the ratio of C-rich to A/U-rich clusters shifts. However, they do not investigate the functional consequences of these changes. Are the stage-specific smOOPs involved in stage-specific processes? Do the changes in smOOPs correlate with changes in condensate formation or function during development? The GO analysis is performed on the combined set of smOOPs, not on stage-specific sets, which limits the developmental insights.
- **Why it matters** The title emphasizes "early development," and the developmental staging is a distinguishing feature of this study compared to previous work on condensation-prone RNAs. If the developmental aspect is not functionally explored, the paper's contribution is primarily descriptive.
- **Resolution test** Perform stage-specific GO or pathway analysis. Investigate whether the shift from C-rich to A/U-rich smOOPs correlates with known developmental transitions. Consider functional experiments, such as knockdown or overexpression of stage-specific smOOPs, to test their role in developmental processes.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Definition of "smOOPs"
- **Evidence pointer** Abstract, Introduction, Results
- **Issue** The acronym "smOOPs" is defined as "semi-extractable, orthogonal-organic-phase-separation-enriched RNAs," but the term "orthogonal-organic-phase-separation" is not standard terminology. The OOPS method is described as capturing RNA-protein interactions, but the "orthogonal" aspect is not clearly explained in the main text.
- **Required correction** Clarify the terminology, either by providing a more standard description of the OOPS method or by explaining what "orthogonal" refers to in this context.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 1H, S1
- **Evidence pointer** Figure 1H, S1
- **Issue** The authors report p values for the comparison of iCLIP signal between smOOPs and non-smOOPs, but the statistical test used is not consistently described across figures. In some cases, a one-sided Wilcoxon test is mentioned, but it is unclear whether multiple testing corrections were applied.
- **Required correction** Provide a consistent description of statistical tests used, including whether multiple testing corrections were applied and how.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Code and model availability
- **Evidence pointer** Data and code availability section
- **Concern** The authors state that code is available at a GitHub repository, but the specific version or DOI is not provided. The trained deep learning models are deposited at Zenodo, but it is unclear whether the code to reproduce the training and analysis is fully documented.
- **Required correction** Provide a versioned release of the code with a DOI or specific commit identifier, and ensure that the code is sufficiently documented to reproduce the analyses.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Figure accessibility
- **Affected element** Figure 4H
- **Evidence pointer** Figure 4H
- **Issue** The importance scores for individual RBPs are shown, but the full names of the RBPs are not provided in the figure or legend. This makes it difficult for readers to interpret the biological significance of the findings.
- **Required correction** Provide full gene names for all RBPs shown in Figure 4H, either in the figure itself or in the legend.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion depth
- **Affected element** Discussion section
- **Evidence pointer** Discussion
- **Concern** The discussion is relatively brief and does not fully explore the implications of the two clusters. For example, what might explain the existence of two distinct types of condensation-prone RNAs? Are there known differences in how C-rich and A/U-rich RNAs interact with condensates?
- **Required correction** Expand the discussion to address the potential functional significance of the two clusters and how they might relate to different types of condensates or different mechanisms of RNA recruitment.

## Risk / unsupported claims
- The claim that smOOPs are "condensation-prone" is supported by indirect evidence (foci size, RBP binding, network connectivity) but not by direct demonstration of phase separation behavior. The authors acknowledge this in the limitations but the framing of the paper implies a stronger causal link.
- The claim that the deep learning model identifies "characteristic" features of smOOPs is based on a single dataset with no external validation. The generalizability of the model to other cell types or conditions is untested.
- The developmental significance of the observed changes in smOOPs is not functionally validated. The claim that smOOPs are "developmentally regulated" is supported by descriptive data but the functional consequences are not explored.
- The use of human condensate datasets for enrichment analysis (Figure 1C, 1D) relies on ortholog gene transfer, which may introduce species-specific biases that are not fully discussed.
- The statement that "smOOPs encode proteins bearing extensive intrinsically disordered regions" is based on computational predictions and has not been experimentally validated at the protein level.