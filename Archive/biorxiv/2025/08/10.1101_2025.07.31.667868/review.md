## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, conclusion, and methods sections
- **Assessment boundary** Scientific content, methodological soundness, evidence quality, and internal consistency of the claims presented. Not assessed: formatting, grammar, or stylistic issues beyond readability for a general audience
- **Shared manuscript claim summary** The authors compare missense MAVE data from 37 human proteins against five state-of-the-art VEPs to quantify and explain points of agreement and disagreement. They report that discordance is systematic, with VEPs overpredicting pathogenicity at buried/hydrophobic residues and underpredicting in disordered regions and charged surface residues, while MAVEs capture context-specific mechanisms but can miss pathogenic variants due to assay design or noise. They propose an integrated, mechanism-aware framework for variant interpretation.
- **Visible evidence base** Abstract, Introduction, Results and discussion (partial), Conclusion, Methods (partial), Supplementary figure legends referenced but not provided
- **Missing materials affecting confidence** Full results section with figures and tables (Figures 1-6, Tables 1, S1, S2, Figures S1-S3, Supplemental file SF1), complete methods for all analyses, detailed statistical procedures, and the full dataset descriptions

## Reviewer
- **Overall assessment** The manuscript addresses a timely and practically important question: why computational predictors and experimental assays of variant effect diverge. The authors have assembled a substantial dataset (37 MAVEs, 5 VEPs) and identify several plausible systematic patterns of discordance. However, the provided text is incomplete, with the results section truncated and all figures and tables absent. The core quantitative evidence supporting the main claims cannot be evaluated from the supplied material. The conceptual framework is interesting and the qualitative observations are plausible, but the manuscript as presented does not establish its central conclusions without access to the missing data and analyses.
- **Who would be interested in the results, and why** Clinical geneticists and molecular diagnosticians who interpret VEP outputs for variant classification; computational biologists developing next-generation VEPs; experimentalists designing MAVE assays; and researchers in the variant effect prediction community broadly. The practical implications for combining VEP and MAVE evidence in ACMG/AMP-style frameworks are directly relevant to clinical practice.
- **Major strengths** The question is well-posed and practically important. The dataset is large and diverse (37 proteins, multiple assay types). The authors distinguish VEP classes and acknowledge the heterogeneity of MAVE designs. The qualitative observations about VEP overprediction at buried residues and underprediction in disordered regions are consistent with known limitations of conservation-based methods. The discussion of assay-design mismatches (e.g., VAMP-seq measuring stability rather than activity) is insightful and well-illustrated with specific examples.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (incomplete evidence), R1-M2 (normalisation methodology), R1-M3 (VEP selection), R1-M4 (ClinVar gold standard), R1-M5 (generalisability)
- **Assessment against Nature-style criteria** Originality: moderate. The observation that VEPs and MAVEs disagree is not new, but the systematic quantification across many proteins and the attempt to attribute discordance to specific protein features is a useful contribution. Scientific importance: high for the clinical variant interpretation community, moderate for a broader readership. Interdisciplinary readership: the topic bridges computational biology, experimental genetics, and clinical genomics, but the presentation is likely to be most accessible to specialists. Technical soundness: cannot be fully assessed from the provided material; the methods described are standard but the key analyses are not visible. Readability for nonspecialists: the writing is generally clear, but the incomplete results section prevents a full assessment of how well complex analyses are explained.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript has potential, but the core quantitative results and figures are missing from the supplied material. A complete version with all figures, tables, and full methods would be required for a fair assessment.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The manuscript claims to quantify and explain points of agreement and disagreement between VEPs and MAVEs across 37 proteins, including specific patterns related to protein burial, disorder, and surface charge.
- **Evidence pointer** Results and discussion section, Figures 1-6, Tables 1, S1, S2, Figures S1-S3, Supplemental file SF1
- **Concern** The results section is truncated after the dataset description. All figures, tables, and the detailed quantitative analyses supporting the main claims are absent from the provided material. The reader cannot verify the central assertions about discordance patterns, effect sizes, or the specific examples discussed in the clinical variants section. The Hedges G effect size analysis (Figure 3), the protein feature comparisons (Figures 4-5), and the clinical variant analysis (Figure 6) are all referenced but not visible.
- **Why it matters** The manuscript's core contribution is empirical: quantifying where and why VEPs and MAVEs diverge. Without the actual data, figures, and statistical analyses, the claims are unverifiable. The qualitative narrative is plausible but cannot substitute for the quantitative evidence.
- **Resolution test** Provide the complete results section with all figures, tables, and statistical outputs. The claims about discordance patterns must be directly supported by the displayed data.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological soundness
- **Claim pointer** The authors state that rank normalisation was applied to make MAVE and VEP scores comparable, with missing values removed from all columns before ranking.
- **Evidence pointer** Methods, Rank normalisation section
- **Concern** The rank normalisation procedure is described but its implications are not discussed. Converting continuous scores to ranks discards information about effect magnitude, which may be particularly problematic when comparing VEPs that output probabilities versus MAVEs that output continuous fitness measurements. The removal of missing values from all columns before ranking could introduce bias if missingness is non-random (e.g., if certain assay types systematically fail for particular variant classes). The choice of rank-based normalisation versus other approaches (e.g., quantile transformation, z-scores) is not justified.
- **Why it matters** The normalisation scheme is the foundation for all cross-method comparisons. If the normalisation distorts the underlying distributions differently for VEPs versus MAVEs, the observed discordance patterns could be artefacts of the transformation rather than genuine biological or methodological differences.
- **Resolution test** Provide a sensitivity analysis comparing the rank-based approach to alternative normalisation methods. Demonstrate that the main conclusions are robust to the choice of normalisation. Discuss the potential impact of non-random missingness.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Representativeness of VEP selection
- **Claim pointer** The authors selected five VEPs described as "state-of-the-art" and representative of diverse methodological approaches.
- **Evidence pointer** Methods, Data acquisition and sources section
- **Concern** The five VEPs chosen (AlphaMissense, ESCOTT, ESM-1v, SaProt, VARITY_R) are all relatively recent and mostly deep learning-based. Older but still widely used methods such as SIFT, PolyPhen-2, and CADD are excluded, with the justification that they are "largely redundant." However, in clinical practice, these older tools remain heavily used, and their inclusion or exclusion materially affects the generalisability of the findings. The claim that these five represent a "diverse methodological cross-section" is questionable, as four of the five are protein language model-based or structure-aware deep learning methods.
- **Why it matters** The conclusions about VEP behaviour are specific to the selected tools. If the authors intend to make general claims about VEPs, a broader and more representative selection is needed. If the claims are specific to these five tools, this should be stated more precisely.
- **Resolution test** Either expand the VEP set to include a wider range of methodological families (including older, clinically entrenched tools) or explicitly limit the conclusions to the five selected predictors and justify why these are the most relevant for current and near-future practice.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Gold standard validity
- **Claim pointer** The authors use ClinVar pathogenic/likely pathogenic labels and gnomAD variants as putatively benign to assess VEP and MAVE performance via AUROC.
- **Evidence pointer** Methods, ROC AUC calculation section
- **Concern** The use of ClinVar as a gold standard for pathogenicity is known to suffer from circularity issues, particularly for VEPs that were trained on ClinVar data. While the authors note that their selected VEPs are "immune or highly resistant" to data circularity, this claim is not substantiated in the provided text. AlphaMissense, for example, was trained on ClinVar-derived labels. The gnomAD "putatively benign" set is acknowledged to contain recessive and low-penetrance pathogenic variants, but the potential impact of this contamination on the AUROC comparisons is not quantified.
- **Why it matters** If the gold standard labels are biased, the AUROC comparisons between VEPs and MAVEs may reflect label biases rather than genuine performance differences. This is particularly relevant for the discordance analysis, where the authors attempt to identify which method is "correct" in cases of disagreement.
- **Resolution test** Provide a more detailed discussion of circularity risks for each VEP. Consider sensitivity analyses using gold-standard subsets that are less likely to be contaminated (e.g., variants with strong functional evidence, or variants curated after VEP training cutoffs).

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Generalisability
- **Claim pointer** The authors state that their findings "provide a framework for interpreting when and why VEPs and MAVEs diverge" and draw general conclusions about VEP limitations in disordered regions and MAVE limitations in assay design.
- **Evidence pointer** Conclusion section
- **Concern** The 37 proteins in the dataset are not described in detail in the provided text. The diversity of protein functions, structures, and disease associations is unclear. The authors note that MAVE performance is heterogeneous across proteins, but the determinants of this heterogeneity are not systematically explored. The generalisability of the discordance patterns to proteins not represented in the dataset is uncertain.
- **Why it matters** The authors make general claims about VEP and MAVE behaviour that extend beyond the specific proteins analysed. Without a clear description of the protein set and its representativeness, the scope of the conclusions is unclear.
- **Resolution test** Provide a detailed characterisation of the 37 proteins (function, structure class, disease association, assay type). Discuss the potential for selection bias in the MAVE literature and how this affects the generalisability of the findings.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Introduction, paragraph 1
- **Evidence pointer** Introduction section
- **Issue** The opening sentence about genetic sequencing is generic and could apply to any genomics paper. The specific motivation for comparing VEPs and MAVEs is not stated until later in the introduction.
- **Required correction** Consider opening with a more specific statement about the challenge of variant interpretation and the specific gap this study addresses.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Results, MAVE and VEP dataset selection and normalisation
- **Evidence pointer** Results and discussion section
- **Issue** The term "fitness" is used to describe MAVE measurements, but the assays measure different properties (growth rate, binding, stability, etc.). The conflation of these different measurements under a single term may obscure important differences.
- **Required correction** Define "fitness" explicitly in the context of each assay type, or use more specific terminology (e.g., "assay score", "functional score") where appropriate.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results, MAVE and VEP dataset selection and normalisation
- **Evidence pointer** Results and discussion section
- **Issue** The AUROC analysis is described as bootstrapped 1000 times, but the presentation of results (confidence intervals, dispersion measures) is not described.
- **Required correction** Specify how bootstrap results are summarised (e.g., 95% confidence intervals) and how AUROC differences between VEPs and MAVEs are tested for statistical significance.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, Data acquisition and sources
- **Evidence pointer** Methods section
- **Issue** The methods state that MAVE datasets were obtained from "several sources" but do not provide a complete list of primary publications or accession numbers for all 37 datasets.
- **Required correction** Provide a supplementary table with full dataset provenance, including primary publication, database accession, and version information.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results, Analysis of discordantly predicted clinical variants
- **Evidence pointer** Results and discussion section
- **Issue** The discussion of the PPARG MAVE dataset's low standard deviation is presented as an observation but the implications for the analysis are not explored. If this dataset behaves differently from others, it may warrant separate treatment or sensitivity analysis.
- **Required correction** Either explain why the PPARG dataset is retained in the main analysis despite its unusual properties, or present a sensitivity analysis excluding it.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction
- **Evidence pointer** Introduction section
- **Issue** The introduction cites several relevant works but does not position this study relative to prior comparative analyses of VEPs and MAVEs (e.g., previous benchmarking studies, meta-analyses of MAVE-VEP concordance).
- **Required correction** Add a brief paragraph situating this work within the existing literature on VEP-MAVE comparisons and stating what new insights this study provides.

## Risk / unsupported claims
- The central quantitative claims about discordance patterns (e.g., VEP overprediction at buried residues, underprediction in disordered regions) are unsupported in the provided material because the relevant figures and statistical analyses are missing.
- The claim that the five selected VEPs are "immune or highly resistant" to data circularity is asserted but not demonstrated with evidence.
- The claim that MAVEs are "more reliable in general" than VEPs is a strong conclusion that requires more careful qualification given the heterogeneity of MAVE assay designs and the potential for assay-specific biases.
- The specific clinical variant examples discussed (A53T in SNCA, splice variants in BRCA1, S2G in SHOC2, S612P in MSH2) are presented as illustrative but the systematic analysis supporting their representativeness is not visible.
- The claim that "flipping" gain-of-function scores improves VEP-MAVE correlation is referenced to a previous study but the applicability to the current dataset is not demonstrated.
- The generalisability of the findings to proteins beyond the 37 analysed is asserted but not supported by a characterisation of the dataset's representativeness.