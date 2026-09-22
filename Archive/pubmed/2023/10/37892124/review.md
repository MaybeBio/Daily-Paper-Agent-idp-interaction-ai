## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, data interpretation, and conclusions as presented in the manuscript
- **Shared manuscript claim summary** The authors compare two disorder prediction methods, IUPred and AlphaFold2 (AF2) pLDDT scores, on DisProt database annotations to identify systematic sources of disagreement, including experimental evidence type, functional annotations, secondary structure preferences, and evolutionary conservation, and extend these observations to proteome-level predictions.
- **Visible evidence base** Main text, figures referenced (Figures 1–9), tables (Tables 1–2), supplementary figures referenced (Figures S1–S2), methods section
- **Missing materials affecting confidence** Supplementary figures and tables not provided; specific numerical data underlying figures not available; details of statistical tests not described; full list of DisProt entries and proteome sets not provided

## Reviewer
- **Overall assessment** This manuscript presents a systematic comparison of two widely used disorder prediction approaches, IUPred and AlphaFold2 pLDDT scores, against experimentally annotated disordered regions from the DisProt database. The authors introduce a quadrant-based classification scheme to categorize agreement and disagreement patterns and analyze these patterns across experimental methods, functional annotations, secondary structure content, and evolutionary conservation. The work addresses an important and timely question, as understanding method-specific biases is critical for improving disorder prediction and for interpreting large-scale structural predictions. The analysis is generally well-structured and the conclusions are largely supported by the presented data, though several methodological details and statistical considerations require clarification. The proteome-level extension is interesting but raises questions about the comparability of the two methods at different thresholds. Overall, the manuscript provides a useful contribution to the field, but the case for some of the broader claims would be strengthened by additional quantitative analyses and clearer statistical reporting.

- **Who would be interested in the results, and why** Researchers working on intrinsically disordered proteins, developers and users of disorder prediction methods, structural biologists interpreting AlphaFold2 predictions, and bioinformaticians interested in benchmarking and method evaluation. The findings on AF2's tendency to predict helical structure within disordered regions and its conservation-dependent bias are particularly relevant for those using AF2 for functional annotation of uncharacterized proteins.

- **Major strengths** The study addresses a relevant and under-explored question about the sources of disagreement between prediction methods and experimental annotations. The quadrant-based visualization approach is intuitive and effective for displaying agreement/disagreement patterns. The analysis across multiple dimensions (experimental method, function, secondary structure, conservation) provides a comprehensive view of method-specific biases. The use of the DisProt database as a gold standard is appropriate, and the authors acknowledge its limitations. The proteome-level analysis adds a practical dimension to the findings.

- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Statistical rigor
    - **Claim pointer** The manuscript reports percentages of residues in different quadrants (e.g., 79% agreement, 15% both predict order) and differences between subsets (e.g., experimental methods, functional categories) without providing statistical significance testing or confidence intervals.
    - **Evidence pointer** Section 3.1, Tables 1–2, Figures 1–7
    - **Concern** The manuscript presents numerous quantitative comparisons between subsets (e.g., experimental methods in Figure 2B, functional categories in Figure 5, conservation levels in Figure 7) but does not report any statistical tests to support claims of enrichment or overrepresentation. For example, the statement that "X-ray crystallography-based annotations were largely enriched" in the Q1 quadrant is made without a statistical basis.
    - **Why it matters** Without statistical testing, the reader cannot assess whether observed differences are meaningful or within the range of random variation. This is particularly important given the relatively small sample sizes in some subsets (e.g., only 9 molten globule and 11 pre-molten globule entries).
    - **Resolution test** Provide appropriate statistical tests (e.g., chi-square, Fisher's exact test, or permutation tests) for categorical comparisons, and confidence intervals or effect sizes for proportion estimates. Specify the test used, the comparison made, and the resulting p-values or confidence intervals for each key claim.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Methodological transparency
    - **Claim pointer** The authors state that IUPred and AF2 predictions were compared using specific cutoffs (pLDDT 0.7, IUPred 0.425) and that these cutoffs were chosen so that both methods predict the same amount of residues as disordered.
    - **Evidence pointer** Section 2.3, Section 3.1
    - **Concern** The manuscript does not provide sufficient detail on how the IUPred cutoff of 0.425 was determined. The statement that "IUPred predicted the same amount of residue as disordered" at this cutoff is ambiguous. Was this cutoff calibrated on the DisProt dataset, on the proteome sets, or on some other reference? The sensitivity of the results to this cutoff choice is not explored.
    - **Why it matters** The choice of cutoffs directly affects the quadrant assignments and therefore all subsequent analyses. If the cutoff calibration is circular (e.g., tuned to match AF2 on the same dataset), this could bias the results. The lack of sensitivity analysis makes it impossible to assess the robustness of the findings.
    - **Resolution test** Clearly describe the procedure for determining the IUPred cutoff, including the dataset used for calibration. Provide a sensitivity analysis showing how the main results (e.g., quadrant percentages, enrichment patterns) change with reasonable variations in both cutoffs.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Interpretation and generalizability
    - **Claim pointer** The authors conclude that "AF2 tends to predict intrinsically disordered regions as ordered in the case of strong evolutionary sequence conservation" and that this is due to the larger number of homologous sequences in the AF2 MSA input.
    - **Evidence pointer** Section 3.4, Figure 7, Table 2
    - **Concern** The conservation analysis is limited to mammalian sequences (as stated in Section 2.4), yet the conclusion is framed in general terms. The number of sequences in the Unicellular category is very small (20 regions), making the 60% figure for AF2 predicting order potentially unstable. The proposed mechanism (MSA depth influencing AF2 predictions) is plausible but not directly tested.
    - **Why it matters** The claim about conservation-dependent bias in AF2 is one of the more novel findings, but the evidence base is thin. If the effect is real, it has implications for interpreting AF2 predictions in conserved proteins. However, the current analysis does not rule out alternative explanations (e.g., functional differences in conserved disordered regions).
    - **Resolution test** Expand the conservation analysis to non-mammalian species if possible, or at least acknowledge the limitation more prominently. Provide confidence intervals for the proportions in each conservation category. Consider testing the MSA depth hypothesis directly by correlating MSA depth with prediction outcomes.

    - **Concern ID** R1-M4
    - **Severity** Major
    - **Blocking** No
    - **Axis** Data presentation and reproducibility
    - **Claim pointer** The manuscript refers to specific examples (e.g., DP02515, DP02513, DP00628, DP00393) to illustrate cases where both methods predict order in disagreement with annotations.
    - **Evidence pointer** Section 3.6, Figure 9
    - **Concern** The example-based analysis is qualitative and the selection criteria for these examples are not stated. It is unclear whether these are representative cases or exceptional ones. The manuscript does not provide a systematic analysis of how many cases in each quadrant fall into the proposed categories (weak experimental support, intermediate states, context-dependent behavior).
    - **Why it matters** The examples are used to support the claim that disagreements arise from identifiable biological or methodological causes. Without a systematic categorization, the reader cannot assess how generalizable these explanations are.
    - **Resolution test** Provide a systematic categorization of disagreement cases (e.g., by manual curation or automated criteria) with counts and percentages for each proposed explanation category. State the criteria used for categorization and ideally have them independently validated.

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Section 2.1
    - **Evidence pointer** Section 2.1
    - **Issue** The description of the DisProt dataset filtering is incomplete. The authors state that after merging overlapping entries, 1967 regions spanning 130,678 residues remain, but the relationship between the initial 4193 regions and the merged set is not fully explained.
    - **Required correction** Clarify whether the 4193 regions refer to the non-redundant set before or after merging, and specify how overlapping entries were defined and merged.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Completeness
    - **Affected element** Section 2.2
    - **Evidence pointer** Section 2.2
    - **Issue** The selection of 55 model organisms is mentioned, but the criteria for this selection are not provided. The addition of seven Archaeal species from the QFO database is described, but the rationale for this addition is not stated.
    - **Required correction** Briefly state the criteria for selecting the 55 model organisms and the rationale for including additional Archaeal species.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Interpretation
    - **Affected element** Section 3.3
    - **Evidence pointer** Figure 6
    - **Issue** The observation that AF2 predicts α-helical structure within disordered regions is interesting, but the analysis does not distinguish between different types of disordered regions (e.g., those with transient helical structure vs. those without).
    - **Required correction** Consider discussing whether the predicted helices correspond to regions with known helical propensity or whether they represent a systematic bias of AF2.

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Presentation
    - **Affected element** Section 3.5, Figure 8
    - **Evidence pointer** Section 3.5
    - **Issue** The proteome-level analysis shows differences between AF2 and IUPred for eukaryotic proteomes, but the biological interpretation of this difference is not fully developed.
    - **Required correction** Expand the discussion of why AF2 might predict more disorder in eukaryotic proteomes and what implications this has for the use of AF2 in eukaryotic genome annotation.

    - **Concern ID** R1-m5
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Section 4
    - **Evidence pointer** Section 4
    - **Issue** The discussion of "flavors" of disorder is somewhat brief given the complexity of the concept and its relevance to the findings.
    - **Required correction** Consider expanding the discussion of how the different flavors of disorder relate to the observed prediction patterns, particularly for molten globules and pre-molten globules.

- **Technical failings that need to be addressed before the case is established** R1-M1 (statistical rigor) and R1-M2 (methodological transparency) are the most critical. Without statistical support for the enrichment claims and without a clear description of the cutoff calibration procedure, the core findings cannot be fully evaluated. R1-M3 (conservation analysis limitations) also needs to be addressed to support the generalizability of the conclusions.

## Risk / unsupported claims
- The claim that AF2's tendency to predict order in conserved disordered regions is due to MSA depth is plausible but not directly tested; the mechanism is inferred rather than demonstrated.
- The statement that "these results confirm earlier observations that there are characteristic differences between short and long disordered regions" is presented as a confirmation, but the analysis does not directly compare to the earlier observations in a quantitative manner.
- The proteome-level claim that "AF2 predicted 38% of the residues as disordered in this set, IUPred only predicted 28%" for eukaryotic proteomes is presented without measures of variability or statistical comparison.
- The categorization of disagreement cases into "weak experimental support, the presence of intermediate states, or context-dependent behavior" is presented as explanatory but is not systematically quantified or validated.
- The example-based analysis in Section 3.6 is used to support general conclusions, but the representativeness of these examples is not established.

## Assessment against Nature-style criteria
- **Originality** Moderate. The comparison of IUPred and AF2 on DisProt data is not entirely novel, as previous studies have benchmarked these methods, but the systematic quadrant-based analysis across multiple biological dimensions (experimental method, function, structure, conservation) provides a new perspective on method-specific biases.
- **Scientific importance** Moderate to high. Understanding the limitations and biases of disorder prediction methods, particularly AF2, is important for the field. The findings on AF2's helical bias and conservation-dependent behavior have practical implications for users of AF2 predictions.
- **Interdisciplinary readership** Moderate. The work is primarily of interest to computational biologists, bioinformaticians, and structural biologists. The biological implications are discussed but the work does not have broad interdisciplinary appeal beyond these fields.
- **Technical soundness** The core methodology is sound, but the lack of statistical testing and the incomplete description of cutoff calibration are significant weaknesses. The quadrant approach is valid but would benefit from more rigorous quantitative support.
- **Readability for nonspecialists** The manuscript is generally well-written and accessible, with clear explanations of the methods and findings. The quadrant-based figures are intuitive. However, some sections (e.g., the description of DisProt filtering) could be clearer for readers not familiar with the database.

## Recommendation posture
Supportive if technical concerns are resolved. The manuscript addresses a relevant question and presents interesting findings, but the lack of statistical rigor and incomplete methodological details currently prevent full evaluation of the claims. If the authors add appropriate statistical tests, clarify the cutoff calibration procedure, and strengthen the conservation analysis, the work would be a solid contribution to the field.