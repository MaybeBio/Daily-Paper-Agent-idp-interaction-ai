## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv)
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the provided text
- **Shared manuscript claim summary** The authors systematically tested 16 commonly used protein tags (fluorescent proteins, peptide tags, ligand-binding tags) fused to several condensation-prone proteins across human cells, yeast, E. coli, in vitro, and via coarse-grained simulations. They report that tagging can strongly influence condensate formation in a tag- and protein-dependent manner, with mCherry generally reducing and EGFP/EYFP often enhancing condensation. They propose that the charge of fluorescent protein tags is a critical factor modulating condensation behavior and provide recommendations for experimental design.
- **Visible evidence base** Results sections describing cell-based assays (DDX3X, EDC3, G3BP1, SRMR2), yeast experiments (Pab1), in vitro condensation assays (DDX3X, CsdA, FUS, Nab2), and CALVADOS 3 coarse-grained simulations. Methods sections for cell culture, protein purification, condensation assays, FRAP, AUC, and simulation details. Supplementary table descriptions.
- **Missing materials affecting confidence** Figures and supplementary figures are referenced but not provided. Quantitative data (e.g., exact fold changes, statistical tests, p-values) are not fully described in the text. Supplementary tables S1-S8 are listed but their contents are only partially described. No raw data or analysis scripts are provided.

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question in the condensate field: the extent to which commonly used protein tags perturb biomolecular condensate formation. The systematic approach across multiple proteins, tags, and experimental systems is commendable and fills a clear gap in the literature. The finding that tag effects are protein-dependent and can be substantial is likely to be of broad interest. However, the manuscript as presented has several significant weaknesses. The lack of quantitative data and statistical analysis in the text makes it difficult to assess the robustness of the claims. The mechanistic interpretation, particularly the role of charge, is supported by simulations but the connection to experimental observations is not fully developed. The recommendations for tag selection, while sensible, are not always clearly derived from the presented data. The manuscript would benefit from a more rigorous presentation of quantitative results and a clearer articulation of how the experimental and computational results together support the conclusions.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, and membraneless organelles, as well as cell biologists who use fluorescent protein tags for localization studies. The results provide practical guidance for tag selection and highlight potential artifacts in condensate experiments. The findings are also relevant to the broader community interested in protein engineering and the biophysical properties of fusion proteins.
- **Major strengths** 1) Systematic and comprehensive approach: testing 16 tags across multiple proteins and experimental systems is a significant effort. 2) Relevance: addresses a widely recognized but poorly characterized problem in the field. 3) Combination of experimental and computational approaches: the use of CALVADOS 3 simulations to explore mechanisms is a strength. 4) Practical recommendations: the manuscript provides actionable advice for researchers.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Quantitative data and statistical rigor
  - **Claim pointer** The manuscript claims that tagging "strongly influenced condensation for some proteins, while others remained unaffected" and describes specific effects (e.g., "mCherry consistently reduces condensate formation, while EGFP or EYFP tend to induce larger and more aggregated structures").
  - **Evidence pointer** Results sections (e.g., "Fluorescent protein, peptide or ligand-binding tags strikingly alter DDX3X stress granule appearance", "Comparison of in vitro condensation results for mEGFP and mCherry"), Figures 1-6 (referenced but not provided)
  - **Concern** The text describes qualitative observations (e.g., "larger", "smaller", "reduced", "increased") but does not provide quantitative data such as mean values, effect sizes, confidence intervals, or statistical tests. For a study that aims to systematically characterize tag effects, this is a major omission. The reader cannot assess the magnitude of the effects or the reliability of the conclusions. For example, the claim that mCherry "consistently reduces" condensation needs quantitative support across all tested conditions.
  - **Why it matters** Without quantitative data and statistical analysis, the central claims of the manuscript are not verifiable. The conclusions about which tags are "safe" or "problematic" depend on the magnitude and consistency of the effects, which cannot be evaluated from the current text.
  - **Resolution test** Provide quantitative data (e.g., mean ± SD/SEM, effect sizes, p-values or confidence intervals) for all key comparisons. Include statistical analysis (e.g., ANOVA, t-tests with multiple testing correction) where appropriate. Present the data in a way that allows the reader to assess the magnitude and consistency of tag effects across proteins and conditions.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Mechanistic interpretation
  - **Claim pointer** The manuscript claims that "Coarse-grained simulations suggest that the charge of the fluorescent protein tags is a critical factor modulating condensation behavior."
  - **Evidence pointer** Results section "Phase coexistence simulations of fusion proteins", Figures 7, S7-S11, Supplementary Tables S2-S3
  - **Concern** The simulations are used to support a charge-based mechanism, but the connection between the simulation results and the experimental observations is not clearly established. The text states that "we find a systematic variation in the propensity to phase separate" for the DDX4 IDR with different GFP charge variants, but it is not clear how this relates to the experimental results with full-length proteins. The simulations are performed on simplified systems (IDRs, specific GFP variants), and the extrapolation to the complex experimental systems (full-length proteins, cellular environments) is not justified. The claim that charge is "critical" is not supported by a systematic analysis of other potential factors (e.g., size, shape, hydrophobicity, specific interactions).
  - **Why it matters** The mechanistic claim is a key part of the paper's contribution. If the charge-based mechanism is not well-supported, the paper's significance is diminished. The authors need to more rigorously connect the simulation results to the experimental data and rule out alternative explanations.
  - **Resolution test** Provide a more detailed analysis of the simulation results, including a systematic comparison of different tag properties (charge, size, hydrophobicity) and their correlation with condensation propensity. Directly compare simulation predictions with experimental results for the same protein-tag combinations. Discuss alternative mechanisms and explain why the charge-based explanation is preferred.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Generalizability and scope
  - **Claim pointer** The manuscript claims to have tested "the effects of sixteen widely used tags on condensate formation in various model organisms, in vitro, in cells and by computational modelling" and concludes that "tagging should be avoided whenever possible or cautiously evaluated when experimentally required."
  - **Evidence pointer** Results sections across the manuscript
  - **Concern** The scope of the study is broad, but the depth of analysis for each protein-tag combination is limited. For example, only a subset of tags was tested for each protein (e.g., 16 tags for DDX3X, 4 tags for EDC3, 6 tags for Pab1, 9 tags for CsdA). The conclusion that tagging should be avoided is a strong recommendation that may not be warranted given the limited number of proteins and conditions tested. The authors do not provide a clear framework for how to "cautiously evaluate" tags, and the criteria for determining when a tag is "acceptable" are not defined.
  - **Why it matters** The manuscript aims to provide general guidance for the field. If the scope is too limited to support the broad conclusions, the recommendations may be overinterpreted. The authors need to be more careful in stating the limits of their study and in providing actionable criteria for tag selection.
  - **Resolution test** Clearly state the limitations of the study in terms of the number of proteins, tags, and conditions tested. Provide a more nuanced discussion of when tagging is likely to be problematic and when it may be acceptable. Develop a decision tree or set of criteria for evaluating tag effects based on the data presented.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Experimental design and controls
  - **Claim pointer** The manuscript describes experiments with transient transfection and stable cell lines, and compares tagged constructs to antibody staining of endogenous proteins.
  - **Evidence pointer** Methods sections, Results sections (e.g., "Fluorescent protein, peptide or ligand-binding tags strikingly alter DDX3X stress granule appearance", "Titrating expression levels results in milder and less variable effects on DDX3X stress granule appearance")
  - **Concern** The text mentions that transient transfection leads to variable expression levels, and that stable cell lines with titratable expression were generated. However, it is not clear how the expression levels were matched to endogenous levels, and whether the observed effects are due to the tag or to overexpression. The comparison to antibody staining of endogenous protein is useful, but the text does not describe how the antibody staining was validated or whether the antibody recognizes all forms of the protein. The potential for the tag to affect protein stability or turnover is not discussed.
  - **Why it matters** The interpretation of the results depends on the assumption that the observed effects are due to the tag and not to other factors such as expression level or protein stability. Without proper controls and validation, the conclusions may be confounded.
  - **Resolution test** Provide details on how expression levels were quantified and matched to endogenous levels. Include controls such as untagged protein expressed at the same level, and validate that the tag does not affect protein stability or turnover. Describe the validation of the antibodies used for immunostaining.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of presentation
  - **Affected element** Results section "Fluorescent protein, peptide or ligand-binding tags strikingly alter DDX3X stress granule appearance"
  - **Evidence pointer** Figure 1 (referenced but not provided)
  - **Issue** The text describes the effects of 16 tags on DDX3X SG appearance but does not provide a clear summary of the results. A table or figure summarizing the effects of each tag on SG number, size, and morphology would be helpful.
  - **Required correction** Consider adding a summary table or figure that clearly presents the effects of each tag on the measured parameters.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** Throughout the manuscript
  - **Evidence pointer** Not applicable
  - **Issue** The term "condensation" is used to describe both the process of phase separation and the formation of visible condensates. This could be confusing. The authors should clarify their use of terminology.
  - **Required correction** Define "condensation" and "condensate formation" clearly in the introduction and use consistent terminology throughout.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Discussion of limitations
  - **Affected element** Discussion section
  - **Evidence pointer** Not applicable
  - **Issue** The discussion does not adequately address the limitations of the study, such as the limited number of proteins tested, the use of overexpression systems, and the potential for the tag to affect protein function beyond condensation.
  - **Required correction** Add a paragraph discussing the limitations of the study and the potential for unmeasured effects of tagging.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods section
  - **Evidence pointer** Methods sections
  - **Issue** The methods section does not provide sufficient detail for replication. For example, the exact conditions for the condensation assays (protein concentrations, buffer compositions, time points) are not fully described.
  - **Required correction** Provide more detailed methods, including exact concentrations, buffer compositions, and time points for all assays.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Figure quality
  - **Affected element** Figures (referenced but not provided)
  - **Evidence pointer** Figures 1-7, S1-S11
  - **Issue** The figures are not provided, so it is not possible to assess their quality or clarity.
  - **Required correction** Ensure that all figures are of high quality and clearly present the data. Consider adding scale bars, error bars, and statistical annotations where appropriate.

## Technical failings that need to be addressed before the case is established
- R1-M1: Lack of quantitative data and statistical analysis for key claims.
- R1-M2: Insufficient connection between simulation results and experimental observations to support the charge-based mechanism.
- R1-M3: Overly broad conclusions relative to the scope of the study.
- R1-M4: Inadequate description of experimental controls and validation.

## Risk / unsupported claims
- The claim that "mCherry consistently reduces condensate formation" is not supported by quantitative data.
- The claim that "the charge of the fluorescent protein tags is a critical factor modulating condensation behavior" is not fully supported by the presented evidence.
- The recommendation that "tagging should be avoided whenever possible" is a strong statement that may not be warranted given the limited scope of the study.
- The claim that "some POI are more affected than others" is not quantified or statistically tested.
- The statement that "the effects of other tags can become negligible" at endogenous expression levels is not supported by quantitative data.

## Assessment against Nature-style criteria
- **Originality** The manuscript addresses a question that is widely recognized but not systematically studied. The comprehensive approach is original and valuable.
- **Scientific importance** The findings have significant implications for the design and interpretation of condensate experiments, which is a rapidly growing field. The results are likely to influence experimental practice.
- **Interdisciplinary readership** The topic is relevant to cell biology, biophysics, and molecular biology. The use of multiple model systems and computational methods broadens the appeal.
- **Technical soundness** The technical approach is generally sound, but the lack of quantitative data and statistical analysis is a major weakness. The connection between simulations and experiments needs to be strengthened.
- **Readability for nonspecialists** The manuscript is generally well-written and accessible, but the lack of quantitative summaries and clear figures makes it difficult for nonspecialists to assess the strength of the conclusions.

## Recommendation posture
Supportive if technical concerns are resolved. The manuscript addresses an important question and has the potential to be a valuable contribution. However, the lack of quantitative data, statistical analysis, and a clear mechanistic connection between simulations and experiments prevents the case from being fully established. The authors should address these concerns before the manuscript can be considered for publication.