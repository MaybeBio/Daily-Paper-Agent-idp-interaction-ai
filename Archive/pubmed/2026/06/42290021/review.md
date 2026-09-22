## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors report a proteome-wide analysis of intrinsic disorder in 2055 unique human proteins that interact with SARS-CoV-2, integrating five experimentally validated interaction datasets. They used disorder prediction, structural confidence assessment, functional and domain annotation, protein-protein interaction network analysis, phase-separation propensity estimation, and D(2)P(2) platform validation on a selected subset. They report a balanced distribution of ordered and disordered host proteins, distinct functional and domain signatures across disorder classes, inverse relationships between disorder and structural confidence, and increased network connectivity and phase-separation propensity among highly disordered interactors. They conclude that SARS-CoV-2 exploits structural diversity rather than preferentially targeting a single disorder class.
- **Visible evidence base** Abstract text only; no quantitative results, statistical measures, dataset identifiers, or methodological details are available
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, supplementary datasets, D(2)P(2) validation details, interaction dataset sources and filtering criteria, disorder prediction tool versions and thresholds, statistical analysis details, and any control or comparison analyses

## Reviewer
- **Overall assessment** The abstract presents a potentially valuable systems-level analysis of intrinsic disorder in the SARS-CoV-2 human interactome. The topic is timely and the integration of multiple interaction datasets is a reasonable approach. However, the abstract provides no quantitative evidence, no methodological specifics, and no statistical validation for any of the stated findings. The central conclusion that SARS-CoV-2 exploits structural diversity rather than preferentially targeting a single disorder class is not supported by any data shown in the abstract. The manuscript may have merit, but the case is not established from the supplied material.
- **Who would be interested in the results, and why** Researchers studying viral-host interactions, intrinsically disordered proteins, and systems virology would be interested. The work could inform understanding of how SARS-CoV-2 engages host proteome structural diversity, which has implications for therapeutic targeting and for understanding viral evolution. The methodological framework combining disorder prediction with network analysis may also interest computational biologists working on interactome characterization.
- **Major strengths** The study addresses a relevant and under-explored question about the structural properties of host proteins in the SARS-CoV-2 interactome. The integration of five experimentally validated interaction datasets to assemble 2055 unique host proteins suggests a systematic approach. The multi-method analytical strategy, including disorder prediction, network analysis, and phase-separation propensity estimation, is comprehensive in scope.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: The question of whether SARS-CoV-2 preferentially targets disordered versus ordered host proteins is not entirely novel, but the systems-level integration of multiple datasets and the focus on structural diversity as a general principle has some originality. Scientific importance: Potentially moderate to high if the findings are robust, as they could inform understanding of viral-host interaction mechanisms. Interdisciplinary readership: The topic bridges virology, structural biology, and computational biology, which could attract a broad readership. Technical soundness: Cannot be assessed from the abstract alone; no methodological details or statistical validations are provided. Readability for nonspecialists: The abstract is clearly written and accessible, though some terms such as "phase-separation propensity" and "D(2)P(2) platform" may require definition for a general audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract describes a potentially interesting study, but the absence of any quantitative results, methodological details, or statistical support means the core claims cannot be evaluated. A full manuscript review would be required to determine whether the case can be made.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim "a balanced distribution of ordered and disordered host proteins" and "distinct functional and domain signatures across disorder classes."
- **Evidence pointer** Abstract only; no figures or tables provided
- **Concern** The abstract states these findings but provides no quantitative data, such as the proportion of proteins classified as ordered versus disordered, the specific functional categories enriched in each class, or any statistical measures of significance. Without these data, the claims of balance and distinctness cannot be evaluated.
- **Why it matters** These claims are central to the conclusion that SARS-CoV-2 exploits structural diversity rather than targeting a single disorder class. If the distribution is not actually balanced or the functional signatures are not statistically distinct, the interpretation would change substantially.
- **Resolution test** Provide the distribution of disorder classes with confidence intervals or statistical tests, and show enrichment analyses with effect sizes and p-values for functional and domain annotations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency
- **Claim pointer** The authors state they used "disorder prediction, structural confidence assessment, functional and domain annotation, protein-protein interaction network analysis, phase-separation propensity estimation, and independent validation with the D(2)P(2) platform."
- **Evidence pointer** Abstract only; methods section not provided
- **Concern** No details are given on which disorder prediction tools were used, what thresholds defined "disordered" versus "ordered," how structural confidence was assessed, which network metrics were computed, or how phase-separation propensity was estimated. The D(2)P(2) validation is mentioned but its scope and criteria are unspecified.
- **Why it matters** Intrinsic disorder prediction is highly tool-dependent and threshold-sensitive. Without knowing the specific methods and parameters, the results cannot be reproduced or compared with other studies, and the validity of the conclusions cannot be assessed.
- **Resolution test** Provide a detailed methods section specifying all tools, versions, parameters, thresholds, and validation criteria. Include a sensitivity analysis showing that results are robust to reasonable variations in these choices.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical and comparative rigor
- **Claim pointer** The authors claim "increased network connectivity and phase-separation propensity among highly disordered interactors" and conclude that SARS-CoV-2 "exploits structural diversity within the host proteome rather than preferentially targeting a single disorder class."
- **Evidence pointer** Abstract only; no comparison data provided
- **Concern** The abstract reports increased connectivity and phase-separation propensity but provides no statistical measures, no comparison with a control set of non-interacting human proteins, and no assessment of whether the observed enrichment is significant. The conclusion that SARS-CoV-2 does not preferentially target a single disorder class requires a formal comparison against the background proteome distribution, which is not described.
- **Why it matters** Without a proper control comparison, the observed patterns could reflect general properties of the human proteome rather than specific features of SARS-CoV-2 interactors. The central conclusion depends on demonstrating that the interactome differs from expectation.
- **Resolution test** Provide statistical comparisons of disorder distribution, network metrics, and phase-separation propensity between the SARS-CoV-2 interactome and a matched control set of human proteins, with appropriate multiple-testing corrections.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract wording
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "associated with it multifunctionality" is grammatically awkward and may confuse readers.
- **Required correction** Revise to "associated with multifunctionality" or "associated with their multifunctionality."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract, methods description
- **Evidence pointer** Abstract, methods sentence
- **Issue** The term "D(2)P(2) platform" is used without definition or expansion. Nonspecialist readers will not know what this refers to.
- **Required correction** Define the platform on first use, for example "Database of Disordered Protein Predictions (D(2)P(2))" or provide a brief explanatory phrase.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Abstract, dataset description
- **Evidence pointer** Abstract, methods sentence
- **Issue** The abstract states "five experimentally validated interaction datasets" but does not name or describe these datasets, their sources, or how they were validated.
- **Required correction** Briefly identify the datasets or provide a reference in the abstract, or clarify that full details are in the methods section.

## Risk / unsupported claims
- The claim of a "balanced distribution of ordered and disordered host proteins" is unsupported by any quantitative data in the abstract.
- The claim of "distinct functional and domain signatures across disorder classes" is unsupported without enrichment statistics.
- The claim of "increased network connectivity and phase-separation propensity among highly disordered interactors" is unsupported without statistical measures or control comparisons.
- The conclusion that SARS-CoV-2 "exploits structural diversity rather than preferentially targeting a single disorder class" is not established without a formal comparison against the background proteome.
- The overall validity of the analytical pipeline cannot be assessed due to the absence of methodological details.