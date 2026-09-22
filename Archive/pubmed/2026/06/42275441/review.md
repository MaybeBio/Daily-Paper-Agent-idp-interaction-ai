## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion, supporting information descriptions)
- **Assessment boundary** Scientific validity, methodological soundness, clarity of claims, and adequacy of evidence as presented in the provided text
- **Shared manuscript claim summary** The authors present "Gate & Channel," a zero-parameter, first-principles framework for interpreting TP53 missense variants using explicit IF-THEN gates derived from physicochemistry and structural biology. The framework claims 84.5% sensitivity and 89.1% PPV across 1,369 TP53 variants, with cross-protein transferability to KRAS, TDP-43, and BRCA1.
- **Visible evidence base** Abstract, full methods description, results narrative, discussion, conclusion, supporting information table descriptions
- **Missing materials affecting confidence** Actual data tables (S1–S6), figures (Fig 1–5), code repository, ClinVar dataset version and filtering criteria, detailed gate threshold derivations, per-variant audit details, statistical comparison against existing predictors

## Reviewer
- **Overall assessment** This manuscript presents a conceptually interesting and potentially valuable framework for interpretable variant effect prediction. The core idea of replacing fitted statistical models with explicit physical gates is philosophically appealing and addresses a real limitation of black-box predictors. However, the manuscript as provided has several critical gaps that prevent full evaluation. The performance metrics are presented without comparison to established predictors, the cross-protein validation appears anecdotal rather than systematic, and the post hoc audit methodology is described but not shown in sufficient detail. The "zero-parameter" claim is somewhat misleading given that thresholds are clearly set, even if not fitted to labels. The manuscript would benefit from substantial revision and additional validation before publication.

- **Who would be interested in the results, and why** Computational biologists developing variant effect predictors, clinical geneticists interpreting TP53 variants, and researchers interested in interpretable AI for molecular biology. The framework's explicit gate architecture could appeal to those seeking mechanistic explanations for variant effects rather than statistical associations. The cross-protein transferability claim, if substantiated, would interest researchers working on other cancer genes.

- **Major strengths** The conceptual framework is genuinely novel and addresses a real gap in the field. The explicit gate architecture provides a level of interpretability that is absent from most machine learning approaches. The extension to IDRs is thoughtful and mechanistically grounded. The open-source implementation and commitment to auditable predictions are commendable. The "Geta" concept for handling exceptions without weakening primary gates is elegant.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "The v18 framework consists of 12 channels and 2 Getas spanning structured domains and IDRs... the framework achieved 84.5% sensitivity and 89.1% positive predictive value"
- **Evidence pointer** Results section, Table 1 (location not provided)
- **Concern** The performance metrics are presented without any comparison to existing TP53 variant predictors. The field has established tools such as SIFT, PolyPhen-2, REVEL, and ClinPred that achieve comparable or better performance on similar benchmarks. Without a head-to-head comparison, the practical utility of this framework is unclear.
- **Why it matters** The central claim of the paper is that this framework provides useful predictive performance. "Useful" is relative; without benchmarking against the state of the art, the reader cannot assess whether the interpretability gains come at an acceptable performance cost.
- **Resolution test** Provide a comparison table showing sensitivity, specificity, PPV, and NPV for Gate & Channel versus at least 3-4 established predictors on the same variant set. If such comparison is not possible due to the "zero-parameter" design philosophy, state this explicitly and justify why the performance is still clinically or scientifically useful.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Applied to KRAS, TDP-43, and BRCA1, the same channels capture the dominant pathogenic mechanisms in each protein as a proof of principle"
- **Evidence pointer** Results section, Table 12, Fig 5 (location not provided)
- **Concern** The cross-protein validation is described as a "proof of principle" but the actual results are not shown in the provided text. The number of variants tested per protein, the performance metrics, and the specific channels that fired are not described. This is insufficient to support the claim of cross-protein transferability.
- **Why it matters** The claim that the framework "carries meaning beyond TP53" is a significant part of the paper's broader significance. If the cross-protein results are anecdotal or based on very few variants, this claim is overstated.
- **Resolution test** Provide the full cross-protein results including number of variants, sensitivity, specificity, and PPV for each protein. If the sample sizes are small, acknowledge this limitation and frame the results as preliminary.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "A post hoc audit of discordant IDR calls indicated that many apparent false positives had plausible molecular rationales, consistent with a distinction between molecular mechanism disruption and clinical penetrance"
- **Evidence pointer** Results section, Tables 8-10 (location not provided)
- **Concern** The post hoc audit methodology is described but the actual audit criteria are not specified. How was "plausible molecular rationale" determined? Was this done by the author alone, or was there independent review? The reclassification of false positives as "true molecular positives" is a significant interpretive move that requires transparent methodology to avoid circular reasoning.
- **Why it matters** The distinction between "molecular disruption" and "clinical penetrance" is conceptually important, but if the audit is subjective, the reclassification of 19 variants could be seen as moving the goalposts to improve apparent performance.
- **Resolution test** Provide the audit criteria in a reproducible form. Ideally, have the audit performed by at least one independent expert blinded to the ClinPad labels. Show the specific rationale for each of the 19 reclassified variants.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "zero-parameter, first-principles framework"
- **Evidence pointer** Throughout, especially Methods (location not provided)
- **Concern** The "zero-parameter" claim is misleading. While no weights are learned from data, the framework clearly has many thresholds and cutoffs (e.g., distance cutoffs for DNA contact, ΔQ≥0.3, ΔV≥30 Å³, Δh≥1.5, pLDDT>70). These are parameters in any meaningful sense; they are simply set by physical reasoning rather than fitted. This is a legitimate design choice, but the terminology obscures it.
- **Why it matters** The "zero-parameter" framing is a key selling point of the paper. If the claim is overstated, it undermines the credibility of the entire manuscript.
- **Resolution test** Either rename the framework to something like "physically parameterized" or provide a clear definition of what "zero-parameter" means in this context, acknowledging that thresholds exist but are not fitted to outcome labels.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** "These results show that a substantial fraction of full-length TP53 missense variation can be resolved through explicit, auditable physical gates"
- **Evidence pointer** Abstract, Discussion
- **Concern** The claim of "substantial fraction" is supported by 84.5% sensitivity, but the specificity of 50.0% is quite low. This means half of all benign variants are predicted as disruptive. For a framework intended for clinical or scientific use, this false positive rate is concerning.
- **Why it matters** The low specificity limits the practical utility of the framework. If the authors are claiming this is useful for variant interpretation, the high false positive rate in benign variants needs to be addressed or contextualized.
- **Resolution test** Discuss the implications of 50% specificity. If the framework is intended as a screening tool, state this explicitly. If it is intended for clinical use, the false positive rate needs to be substantially improved.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods, "Gate outputs, channels, and decision rule"
- **Evidence pointer** Methods section (location not provided)
- **Issue** The mathematical notation for the decision rule is incomplete in the provided text. The equations are referenced but not shown.
- **Required correction** Provide the full equations for nclosed and the final prediction rule.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "Input data and residue scope"
- **Evidence pointer** Methods section (location not provided)
- **Issue** The ClinVar version and download date are not specified. Variant classifications change over time, and reproducibility requires a fixed dataset version.
- **Required correction** Specify the ClinVar version, download date, and filtering criteria used to obtain the 1,369 variants.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, "Post hoc audit"
- **Evidence pointer** Results section, Tables 8-10 (location not provided)
- **Issue** The distinction between "True Molecular Positives" and "Genuine False Positives" is introduced but the criteria for this partition are not fully explained in the text.
- **Required correction** Provide a clear operational definition of TMP versus Genuine FP, ideally with a decision tree or checklist.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion, "Next gates to be written"
- **Evidence pointer** Discussion section
- **Issue** The discussion of future gates is interesting but somewhat speculative. It would be strengthened by a timeline or priority ranking.
- **Required correction** Consider adding a brief prioritization of which gates are most likely to improve performance and why.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract does not mention the low specificity (50.0%) or the cross-protein validation limitations. This gives an overly optimistic impression.
- **Required correction** Add a sentence acknowledging the specificity limitation and the preliminary nature of cross-protein results.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "AlphaFold compatibility"
- **Evidence pointer** Methods section (location not provided)
- **Issue** The pLDDT>70 threshold for AlphaFold acceptance is stated but not justified. Different thresholds may be appropriate for different structural contexts.
- **Required correction** Provide a brief justification for the pLDDT threshold or cite literature supporting this cutoff.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Supporting information
- **Evidence pointer** Supporting information section
- **Issue** The supporting information tables are described but their contents are not summarized in the text. This makes it difficult to assess the completeness of the data.
- **Required correction** Add a brief summary of the key findings from each supporting table in the main text.

- **Technical failings that need to be addressed before the case is established** The lack of comparison to existing predictors (R1-M1), insufficient cross-protein validation data (R1-M2), and subjective audit methodology (R1-M3) are the most significant technical issues. The "zero-parameter" terminology (R1-M4) also needs clarification. These issues must be addressed before the core claims of the manuscript can be fully evaluated.

- **Assessment against Nature-style criteria** 
  - Originality: High. The gate-based approach is genuinely novel and distinct from both statistical and machine learning approaches.
  - Scientific importance: Moderate. If validated, the framework could provide interpretable variant predictions, but the current evidence is insufficient to establish its importance relative to existing tools.
  - Interdisciplinary readership: Moderate. The framework could interest computational biologists, structural biologists, and clinical geneticists, but the current presentation is somewhat narrow.
  - Technical soundness: Currently insufficient. The missing comparisons, incomplete cross-validation, and subjective audit methodology prevent full assessment.
  - Readability for nonspecialists: Good. The writing is clear and the conceptual framework is accessible, though some methods sections are dense.

- **Recommendation posture** Currently not established from the provided evidence. The conceptual framework is promising and the work is potentially publishable, but the manuscript requires substantial revision and additional validation before the core claims can be accepted. I would be supportive if the technical concerns are resolved, particularly the comparison to existing predictors and the strengthening of cross-protein validation.