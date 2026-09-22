## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, conclusions) as provided
- **Assessment boundary** Scientific content, methodological soundness, evidence quality, and internal consistency of the claims as presented in the provided text
- **Shared manuscript claim summary** The authors propose that disease-associated missense mutations in bHLH-PAS transcription factors are predominantly located within intrinsically disordered regions (IDRs), and that these mutations may affect post-translational modification (PTM) sites, liquid-liquid phase separation (LLPS) propensity, or aggregation propensity, thereby contributing to disease development. The claim is based on in silico analyses of selected family members (AhR, AhRR, SIM1, SIM2, Hif-2α, NPAS4, ARNT2, BMAL1) using disorder predictors, PTM databases, LLPS predictors, and aggregation predictors.
- **Visible evidence base** Results sections 2.1–2.5 with figures referenced (Figures 2–5), Table 1, Supplementary Materials (referenced but not provided), Methods section 4, Discussion section 3, Conclusions section 5
- **Missing materials affecting confidence** Supplementary Materials (detailed mutation lists, per-protein data), Figures 1–8 (referenced but not visible), Table 1 (referenced but not visible), specific statistical outputs, raw predictor scores, HuVarBase query details, and any experimental validation data

## Reviewer
- **Overall assessment** The manuscript addresses a potentially interesting question regarding the localization of disease-associated missense mutations in IDRs of bHLH-PAS transcription factors. The authors have compiled and analyzed existing database information using multiple in silico tools. However, the central claim that mutation location in IDRs is "clearly related" to disease mechanisms is not quantitatively established. The analysis is descriptive and correlative, lacking statistical testing, effect sizes, or comparison against appropriate null models. The manuscript reads more as a hypothesis-generating review with embedded bioinformatic observations than as a definitive research article. The absence of visible figures and supplementary data prevents full verification of the presented results.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, transcription factor biology, phase separation in gene regulation, and the molecular basis of diseases linked to bHLH-PAS family members (cancer, circadian disorders, neurodevelopmental conditions). The work may also interest computational biologists developing predictors for disorder, PTM, and LLPS. The hypothesis that IDR-localized mutations in this family may act through PTM disruption or LLPS alteration could guide future experimental studies.
- **Major strengths** The manuscript addresses an understudied aspect of bHLH-PAS biology, namely the functional importance of their C-terminal IDRs. The use of multiple complementary in silico tools (disorder predictors, MoRF prediction, LLPS predictors, aggregation predictors) is appropriate for a hypothesis-generating study. The authors correctly acknowledge the limitations of computational approaches and emphasize the need for experimental validation. The inclusion of both class I and class II family members allows for comparative observations. The discussion of specific mutation examples (e.g., BMAL1 K537R, NPAS3 V304I) grounds the analysis in known biology.
- **Major Concerns** The central claim is not quantitatively supported. The authors state that mutations are "mostly" in IDRs but provide no statistical comparison against the proportion of the protein that is disordered, no enrichment analysis, and no control set of benign polymorphisms. The relationship between mutation location and PTM sites or LLPS regions is asserted based on visual inspection rather than formal proximity analysis. The manuscript lacks a clear hypothesis-testing framework. The figures and Table 1, which presumably contain the core evidence, are not visible in the provided material, making verification impossible. The choice of family members is not justified, and the exclusion of other bHLH-PAS proteins (e.g., NPAS1, NPAS3, CLOCK) is not explained. The clinical relevance of the specific mutations listed is not systematically assessed.
- **Minor Comments** The abstract states "we assume" rather than presenting a testable conclusion. The introduction is overly long relative to the results presented. The distinction between documented PTMs and predicted phosphorylation sites is not always clear in the text. The discussion of LLPS would benefit from more specific mechanistic hypotheses. The methods section does not specify parameters for all predictors used. The statement that "no disease-associated missense mutation was reported in the disordered C-terminal region of BMAL1" is presented as unexpected but the implications are not developed.
- **Technical failings that need to be addressed before the case is established** Absence of statistical enrichment analysis for mutation density in IDRs versus ordered regions; absence of a null model or control dataset; lack of quantitative proximity analysis between mutations and PTM sites or LLPS-predicted regions; incomplete reporting of predictor parameters and thresholds; no sensitivity analysis for the choice of disorder predictors.
- **Assessment against Nature-style criteria** Originality: moderate. The application of disorder-focused analysis to this specific family is somewhat novel, but the general concept that disease mutations cluster in IDRs is established in the literature. Scientific importance: moderate. The work is hypothesis-generating but does not provide definitive mechanistic insight. Interdisciplinary readership: limited. The work is primarily of interest to structural biologists and bioinformaticians, with limited appeal to the broader readership. Technical soundness: weak. The lack of statistical rigor and the descriptive nature of the analysis undermine the technical foundation. Readability for nonspecialists: acceptable. The text is generally clear, though the introduction assumes familiarity with the bHLH-PAS family and IDR concepts.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript presents a plausible hypothesis supported by descriptive observations, but the central claim requires quantitative analysis and the key evidence (figures, Table 1, supplementary data) is not available for verification. The work may be suitable for a specialized journal after substantial revision, but it does not meet the standard for a high-impact general journal.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors claim that disease-associated missense mutations are "mostly" located within IDRs of the analyzed bHLH-PAS proteins.
- **Evidence pointer** Results sections 2.1–2.5, Figures 2–5, Table 1, Supplementary Materials
- **Concern** The claim that mutations are predominantly in IDRs is presented without any statistical analysis. The authors do not report the proportion of each protein that is disordered, nor do they compare mutation density in disordered versus ordered regions. Without an enrichment analysis (e.g., Fisher's exact test or a permutation-based approach) and a control set of benign polymorphisms, the observation could simply reflect the fact that IDRs constitute a large fraction of these proteins. The figures and Table 1, which presumably contain the relevant data, are not visible in the provided material.
- **Why it matters** The central conclusion of the manuscript rests on this claim. If mutation distribution simply mirrors the disorder distribution, the finding is trivial. The authors must demonstrate that mutations are enriched in IDRs beyond what would be expected by chance.
- **Resolution test** Provide a quantitative analysis showing mutation density per residue in IDRs versus ordered regions, with appropriate statistical tests and a control dataset of benign variants. Report the fraction of each protein predicted as disordered and the number of mutations in each region.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors state that mutations are located "in close proximity to the regions important for LLPS regulation, or susceptible to PTMs."
- **Evidence pointer** Results sections 2.1–2.5, Table 1, Supplementary Materials
- **Concern** The proximity between mutation sites and PTM sites or LLPS-predicted regions is asserted but not quantified. No distance thresholds are defined, no statistical test for co-localization is performed, and no comparison against random expectation is provided. The statement that "in some cases" proximity "seems to be crucial" is vague and not supported by specific examples with mechanistic depth.
- **Why it matters** The authors propose a mechanistic link between mutation location and PTM disruption or LLPS alteration. Without a formal co-localization analysis, this link remains speculative. The reader cannot assess whether the observed co-occurrence is meaningful or coincidental.
- **Resolution test** Define a distance threshold for "proximity," perform a permutation test or similar analysis to show that mutations are significantly closer to PTM sites or LLPS-predicted regions than expected by chance, and provide specific examples with mechanistic discussion.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The authors used multiple in silico tools (disorder predictors, MoRF prediction, LLPS predictors, aggregation predictors) and databases (HuVarBase, PhosphoSitePlus).
- **Evidence pointer** Methods section 4
- **Concern** The methods section does not provide sufficient detail for reproducibility. For the disorder predictors, the specific versions and parameters are not fully described. For the LLPS predictors (catGranule, PScore), the output metrics and thresholds for "positive" predictions are not defined. For the Waltz predictor, the settings are given but the interpretation of results is not explained. The HuVarBase query strategy is not described (e.g., which fields were searched, how mutations were filtered, how disease association was determined).
- **Why it matters** Reproducibility is a fundamental requirement for scientific publication. Without detailed methods, other researchers cannot replicate the analysis or assess its validity.
- **Resolution test** Provide complete details for all tools and databases used, including version numbers, parameters, thresholds, and access dates. Describe the HuVarBase query strategy and the criteria for including or excluding mutations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scope justification
- **Claim pointer** The authors selected eight bHLH-PAS proteins for analysis (AhR, AhRR, SIM1, SIM2, Hif-2α, NPAS4, ARNT2, BMAL1).
- **Evidence pointer** Methods section 4, Results sections 2.1–2.5
- **Concern** The selection of these eight proteins is not justified. The bHLH-PAS family includes additional members (e.g., NPAS1, NPAS3, CLOCK, HIF-1α, HIF-3α). The authors do not explain why these particular proteins were chosen or why others were excluded. This raises concerns about potential selection bias.
- **Why it matters** If the selection is biased toward proteins with known disease associations or well-characterized IDRs, the conclusions may not generalize to the entire family.
- **Resolution test** Justify the selection criteria, or expand the analysis to include all human bHLH-PAS family members. If a subset is used, demonstrate that it is representative.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of negative result
- **Claim pointer** The authors note that no disease-associated missense mutation was reported in the disordered C-terminal region of BMAL1.
- **Evidence pointer** Section 2.5
- **Concern** This observation is presented as "unexpected" but the implications are not explored. The authors do not discuss whether this reflects a true biological difference, a gap in the database, or a limitation of the analysis. The absence of mutations in a region could be as informative as their presence, but the authors do not develop this point.
- **Why it matters** A thorough analysis should address both positive and negative findings. The BMAL1 observation could challenge the central hypothesis or reveal important nuances.
- **Resolution test** Discuss possible explanations for the absence of mutations in the BMAL1 C-terminal IDR, including database coverage, functional constraints, or alternative disease mechanisms.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, final sentence
- **Issue** The abstract concludes with "we assume" rather than a definitive statement. This weakens the impact of the findings.
- **Required correction** Rephrase to present the conclusion more assertively, or explicitly frame the work as hypothesis-generating.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Introduction
- **Evidence pointer** Section 1.1, paragraph on IDRs
- **Issue** The introduction discusses IDRs and LLPS but does not clearly define the specific gap in knowledge that this study addresses.
- **Required correction** Add a clear statement of the research question and the specific hypothesis being tested.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Results sections
- **Evidence pointer** Sections 2.1–2.5
- **Issue** The presentation of results is inconsistent across proteins. For some proteins, detailed descriptions of mutation locations are given; for others, the text is brief. The criteria for the level of detail are unclear.
- **Required correction** Standardize the presentation of results for each protein, or explain why different levels of detail are provided.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Section 2.5
- **Evidence pointer** Section 2.5, description of BMAL1
- **Issue** The term "polySUMOylation" is used without definition or context.
- **Required correction** Define the term or provide a brief explanation of its relevance.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Referencing
- **Affected element** Discussion
- **Evidence pointer** Section 3, paragraph on NPAS3
- **Issue** The discussion of NPAS3 V304I mentions schizophrenia but does not provide a reference for this association.
- **Required correction** Add the appropriate citation for the NPAS3 V304I and schizophrenia association.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods
- **Evidence pointer** Section 4, description of PhosphoSitePlus
- **Issue** The text states "PhophoSitePlus" (misspelled) and does not specify the version or access date.
- **Required correction** Correct the spelling and provide the version and access date.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Section 3, paragraph on PTMs
- **Issue** The statement that mutations "could affect" PTM patterns is speculative and not tied to specific examples from the analyzed proteins.
- **Required correction** Provide specific examples from the analyzed proteins where a mutation is known or predicted to affect a PTM site.

## Risk / unsupported claims
- The claim that disease-associated missense mutations are predominantly located in IDRs is unsupported without statistical enrichment analysis.
- The claim that mutations are located in proximity to PTM sites or LLPS-predicted regions is unsupported without formal co-localization analysis.
- The claim that mutations in IDRs "could affect" PTM patterns, protein stability, shuttling, or aggregation is speculative and not directly tested.
- The statement that "most of the disease-associated missense mutations occur in IDRs" (Conclusions) is presented as a finding but is not quantitatively established.
- The relevance of specific mutations to disease states is asserted based on database entries without independent verification of pathogenicity.
- The observation regarding BMAL1 lacking mutations in the C-terminal IDR is presented without interpretation or context.