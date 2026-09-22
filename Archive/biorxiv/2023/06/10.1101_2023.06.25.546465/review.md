## Review setup
- **Input scope** Full manuscript text including abstract, main text, methods, and extended data figure legends
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and methodological rigor as presented in the provided manuscript
- **Shared manuscript claim summary** The authors propose that intrinsically disordered regions (IDRs) promote protein refoldability from a denatured state, and that this property facilitates retrieval of proteins from biomolecular condensates such as heat stress granules. They support this with proteome-wide refolding assays in two fungal species, structural proteomics during heat shock, and targeted dispersal experiments.
- **Visible evidence base** Abstract, main text, methods sections, and extended data figure legends as provided
- **Missing materials affecting confidence** All figures and extended data figures are referenced but not provided; supplementary tables are mentioned but not included; proteomics data availability is indicated by placeholder accession codes

## Reviewer
- **Overall assessment** This manuscript presents a compelling and potentially significant hypothesis linking IDRs to protein refoldability and condensate dynamics. The experimental approach is ambitious, combining proteome-wide refolding assays with structural proteomics and targeted validation. However, the absence of all figures and supplementary data prevents full evaluation of the quantitative claims. The correlational nature of several key findings, particularly the link between refoldability and condensate retrieval, requires stronger causal evidence. The manuscript would benefit from clearer presentation of statistical methods and effect sizes, and from explicit discussion of potential confounding factors in the LiP-MS approach.

- **Who would be interested in the results, and why** Researchers in protein folding, intrinsically disordered proteins, biomolecular condensates, and cellular stress responses would find these results of high interest. The work bridges biophysical principles with cell biology, potentially informing understanding of protein homeostasis and condensate function. The methodological approach may also interest proteomics specialists.

- **Major strengths**
  1. The hypothesis is novel and addresses a fundamental question about the function of IDRs in multidomain proteins.
  2. The use of two fungal species strengthens the generality of the findings.
  3. The combination of proteome-wide assays with targeted validation is methodologically rigorous.
  4. The integration of structural proteomics with functional assays provides multiple lines of evidence.
  5. The discussion of Hsp104 mechanism in the context of refoldability is thoughtful and well-contextualized.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The claim that IDRs promote protein refoldability is based on correlational analysis between disorder content and refolding success.
- **Evidence pointer** Figure 2B, Extended Data Figure 4A
- **Concern** The central claim relies on correlational data. While the trend is statistically significant, correlation does not establish causation. The authors do not provide direct experimental manipulation of IDRs to demonstrate their causal role in refoldability. For example, deletion or insertion of IDRs in specific proteins followed by refolding assays would strengthen the causal claim.
- **Why it matters** The title and abstract assert a causal relationship. Without direct evidence, the conclusion may overreach the data.
- **Resolution test** Provide targeted experiments where IDRs are deleted, inserted, or swapped in specific proteins, and demonstrate corresponding changes in refoldability.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical validity
- **Claim pointer** The LiP-MS approach is used to assess protein refoldability and structural changes during heat shock.
- **Evidence pointer** Methods sections 2a-2c, 4a-4c
- **Concern** The LiP-MS methodology relies on the assumption that changes in proteolytic susceptibility reflect conformational differences. However, protein concentration, aggregation state, and interactions with other molecules in the complex lysate could confound these measurements. The authors do not provide adequate validation that the observed differences are specifically due to conformational changes rather than other factors. Additionally, the threshold for calling a protein "refoldable" (two or more significant peptides) may be arbitrary and could misclassify proteins with limited coverage.
- **Why it matters** The entire refoldability classification system depends on this methodology. If the approach is not robust, all downstream conclusions are affected.
- **Resolution test** Provide validation experiments using purified proteins with known refolding behavior, and demonstrate that the LiP-MS readout correlates with established biophysical measurements. Also, perform sensitivity analysis on the classification threshold.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal inference
- **Claim pointer** The claim that refoldability facilitates retrieval from heat stress granules is based on correlational analysis between refoldability and dispersal kinetics.
- **Evidence point** Figure 5D-G, Extended Data Figure 12
- **Concern** The association between refoldability and rapid dispersal from condensates is correlational. The authors do not demonstrate that refoldability is causally required for retrieval. Alternative explanations, such as IDRs directly affecting condensate properties or interactions with chaperones, are not excluded. The "re-aggregator" category is defined post hoc and may reflect multiple distinct mechanisms.
- **Why it matters** The title claims a facilitative role for IDRs in retrieval. Without causal evidence, this remains a hypothesis.
- **Resolution test** Perform experiments where refoldability is modulated (e.g., by mutating specific residues in IDRs) and demonstrate corresponding changes in dispersal kinetics.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor
- **Claim pointer** Various statistical comparisons are made between groups (e.g., refoldable vs. non-refoldable proteins).
- **Evidence point** Throughout results, specific P-values cited
- **Concern** The statistical methods are not fully described. For example, it is unclear whether multiple testing corrections were applied when analyzing thousands of proteins. The use of chi-square tests for trend analysis may not account for potential confounding variables. Effect sizes are reported but confidence intervals are not consistently provided.
- **Why it matters** Without proper statistical rigor, the significance of reported differences may be overstated.
- **Resolution test** Provide full details of statistical tests, including multiple testing corrections, and report effect sizes with confidence intervals.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence point** Abstract, first sentence
- **Issue** The abstract states that IDRs "promote" refoldability, which implies causation, but the data are largely correlational.
- **Required correction** Soften the language to "are associated with" or "correlate with" unless causal evidence is provided.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods
- **Evidence point** Methods section 7d
- **Issue** The criteria for classifying a protein as "refoldable" or "non-refoldable" are described but the rationale for these thresholds is not justified.
- **Required correction** Provide justification for the chosen thresholds, possibly with reference to prior work or sensitivity analysis.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence point** Discussion, paragraph 3
- **Issue** The discussion of Hsp104 mechanism is speculative and goes beyond the data presented.
- **Required correction** Clearly label speculative statements as such and distinguish them from data-supported conclusions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence point** Methods section 5a
- **Issue** The description of the yeast strain engineering is brief; details on verification of correct integration are not provided.
- **Required correction** Add details on how correct genomic integration was verified (e.g., PCR, sequencing).

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figures
- **Evidence point** Extended Data Figure 12
- **Issue** The definitions of "fast" and "re-aggregator" proteins are complex and may be difficult to follow without clear visual representation.
- **Required correction** Consider adding a schematic diagram to illustrate the classification criteria.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Lack of causal evidence for IDR role in refoldability
  - R1-M2: Potential confounds in LiP-MS methodology
  - R1-M3: Correlational link between refoldability and condensate retrieval
  - R1-M4: Incomplete statistical reporting

- **Assessment against Nature-style criteria**
  - **Originality** High. The hypothesis linking IDRs to refoldability and condensate retrieval is novel and addresses a fundamental question.
  - **Scientific importance** High. If substantiated, the findings would have broad implications for understanding protein homeostasis, condensate biology, and the function of IDRs.
  - **Interdisciplinary readership** Moderate to high. The work bridges biophysics, cell biology, and proteomics, and would appeal to researchers across these fields.
  - **Technical soundness** Currently insufficient. The correlational nature of key claims and potential methodological confounds need to be addressed.
  - **Readability for nonspecialists** Good. The manuscript is generally well-written and accessible, though some methodological details are dense.

- **Recommendation posture** Supportive if technical concerns are resolved. The hypothesis is compelling and the experimental approach is ambitious, but the current evidence is largely correlational. The authors should provide causal evidence for the role of IDRs in refoldability and demonstrate that refoldability directly facilitates condensate retrieval. Additionally, the LiP-MS methodology requires validation and the statistical reporting needs to be more complete.

## Risk / unsupported claims
- The claim that IDRs "promote" refoldability is not directly supported by causal experiments.
- The claim that refoldability "facilitates" retrieval from condensates is correlational and does not exclude alternative mechanisms.
- The assertion that interdomain linkers act as "spacers or lubricants" is speculative and not directly tested.
- The generalization of findings from two fungal species to "possibly all eukaryotes" is not supported by the data presented.
- The claim that the data support a "loop-extrusion model" for Hsp104 is based on indirect evidence and should be presented as hypothesis-generating.