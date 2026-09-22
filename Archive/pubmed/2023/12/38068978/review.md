## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, data interpretation, and conclusions as presented in the manuscript
- **Shared manuscript claim summary** The authors investigate whether the localization of SCN5A mutations (in transmembrane/structured domains vs. intra-domain loops) correlates with clinical severity in 36 high-risk Brugada Syndrome patients. They report that in silico prediction tools frequently classify IDL mutations as benign despite severe clinical phenotypes, and they characterize IDLs as enriched in intrinsically disordered regions and post-translational modification sites, arguing for their functional importance.
- **Visible evidence base** Abstract, Introduction, Results (Sections 2.1–2.3), Discussion, Conclusions, Materials and Methods (Sections 4.1–4.6), Tables 1–3, Figures 1–2, Supplementary Tables S1–S3, Supplementary Figures S1–S2
- **Missing materials affecting confidence** Raw clinical data per patient, complete variant list with genomic coordinates, detailed statistical outputs, full supplementary tables content, cryoEM structure alignment details, and information on how the 36 patients were selected from the larger cohort

## Reviewer
- **Overall assessment** The manuscript addresses a clinically relevant question regarding genotype-phenotype correlations in Brugada Syndrome, specifically focusing on mutation location within SCN5A. The observation that in silico tools may misclassify IDL mutations as benign is potentially important. However, the study is limited by a small sample size, lack of functional validation, and a statistical approach that does not adequately support the main claims. The bioinformatics characterization of IDRs and PTMs is descriptive and does not directly link to the clinical findings. The conclusions extend beyond what the data can support.
- **Who would be interested in the results, and why** Clinicians managing BrS patients, genetic counselors, and researchers studying cardiac sodium channelopathies would be interested. The potential implication that IDL mutations should not be dismissed as benign could affect clinical risk stratification. Researchers studying intrinsically disordered regions in ion channels may also find the bioinformatics analysis relevant.
- **Major strengths** The clinical question is relevant and addresses a gap in the literature. The study combines clinical phenotyping with genetic analysis and bioinformatics. The observation regarding the discrepancy between in silico predictions and clinical severity in IDL mutations is noteworthy and could have practical implications. The characterization of IDRs in NaV1.5 across the sodium channel family is a useful contribution.
- **Major Concerns** The small sample size (n=36, with only 9 IDL mutations) severely limits statistical power. The statistical analysis is inadequate, relying primarily on chi-square tests without correction for multiple comparisons or adjustment for confounders. The claim that clinical phenotypes are similar between IDL and TD mutation groups is based on descriptive comparisons without formal statistical testing for most variables. The bioinformatics predictions are not experimentally validated. The causal link between IDR/PTM enrichment and clinical outcomes is speculative. The study does not include functional studies to support the claim that IDL mutations are pathogenic.
- **Technical failings that need to be addressed before the case is established** Inadequate statistical analysis for group comparisons; lack of functional validation; insufficient detail on patient selection criteria; no correction for multiple testing; the claim that IDL mutations are clinically significant is not supported by direct evidence.
- **Assessment against Nature-style criteria** Originality: Moderate. The question of mutation location and clinical phenotype in BrS has been explored, though the specific focus on IDLs is somewhat novel. Scientific importance: Moderate. The findings could influence clinical practice if confirmed, but the evidence is not yet compelling. Interdisciplinary readership: Limited. The work is primarily relevant to cardiology and genetics specialists. Technical soundness: Weak. The statistical approach and lack of functional validation undermine the conclusions. Readability for nonspecialists: Acceptable. The manuscript is generally clear, though some sections assume specialized knowledge.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript addresses an important question but the evidence presented is insufficient to support the main claims. Major revisions including appropriate statistical analysis, functional validation, or at minimum a much larger cohort would be needed.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical analysis
- **Claim pointer** The authors claim that patients with IDL mutations display clinical symptoms similar to those with TD mutations, and that there were no significant variations in clinical features when mutations were categorized by predicted pathogenicity.
- **Evidence pointer** Section 2.1, Table 1, Supplementary Tables S2 and S3
- **Concern** The statistical analysis is inadequate to support the claim of similarity between groups. The authors state that a chi-square test was used, but it is unclear which variables were tested, whether continuous variables were compared appropriately, and whether any adjustment for multiple comparisons was made. The small sample size (n=9 for IDL mutations) means that the study is underpowered to detect differences, and the absence of statistically significant differences does not demonstrate equivalence. The claim that clinical features are similar between groups requires equivalence testing or at least confidence intervals for effect sizes.
- **Why it matters** The central conclusion that mutation location does not predict clinical severity depends on demonstrating that the groups are clinically comparable. Without appropriate statistical methods, the conclusion is not supported.
- **Resolution test** Provide a detailed statistical analysis plan including tests used for each variable, effect sizes with confidence intervals, and either equivalence testing or a clear statement of the power limitations. If the sample size is insufficient, this should be acknowledged and the conclusions tempered accordingly.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Functional validation
- **Claim pointer** The authors claim that mutations in IDL regions, previously deemed benign, can disrupt NaV1.5 channel function and contribute to BrS development.
- **Evidence pointer** Section 3 (Discussion), Section 2.1
- **Concern** The manuscript provides no functional data to support the claim that IDL mutations affect channel function. The authors reference previous in vitro studies for one specific mutation (Q1832E), but do not provide functional characterization of the mutations identified in their cohort. The claim that IDL mutations are pathogenic is inferred from clinical phenotype alone, which is insufficient given that BrS has incomplete penetrance and variable expressivity.
- **Why it matters** The central thesis that IDL mutations are clinically significant requires evidence that these mutations alter channel function. Without functional validation, the claim remains speculative.
- **Resolution test** Provide functional studies (e.g., patch clamp, trafficking assays) for at least a subset of the identified IDL mutations, or clearly reframe the conclusions as hypothesis-generating.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Patient selection and cohort description
- **Claim pointer** The authors describe a cohort of 36 high-risk BrS patients, 9 with IDL mutations and 27 with TD mutations.
- **Evidence pointer** Section 4.1, Table 1
- **Concern** The criteria for "high risk" are not clearly defined beyond reference to "latest guidelines." It is unclear how these 36 patients were selected from the larger BrS population, what the total number of BrS patients screened was, and whether there was selection bias. The exclusion criteria are described but the number of patients excluded for each reason is not provided. The clinical characteristics of the two groups are presented in Table 1, but the completeness of these data is not clear.
- **Why it matters** Selection bias could significantly affect the observed clinical phenotypes and the distribution of mutations. Without a clear description of the cohort selection process, the generalizability of the findings is uncertain.
- **Resolution test** Provide a flow diagram of patient selection, including the total number of BrS patients assessed, the number excluded at each stage, and the reasons for exclusion. Clarify the specific criteria used to define "high risk."

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Bioinformatics methodology
- **Claim pointer** The authors claim that NaV1.5 has the highest IDR content among the nine sodium channel family members and that IDLs are enriched in PTM sites.
- **Evidence pointer** Section 2.2, Section 2.3, Tables 2 and 3, Figure 2
- **Concern** The bioinformatics analysis is descriptive and lacks validation. The authors use multiple prediction tools but do not provide a consensus approach or discuss the limitations of each tool. The comparison of IDR content across the sodium channel family is based on predictions, not experimental data. The PTM analysis relies on prediction algorithms and database annotations, but the functional significance of the predicted sites is not explored. The claim that PTM disruption leads to loss of channel function is speculative and not directly tested.
- **Why it matters** The characterization of IDRs and PTMs is presented as supporting evidence for the functional importance of IDL regions. If the bioinformatics predictions are not robust or validated, this support is weakened.
- **Resolution test** Provide a more rigorous bioinformatics approach, including consensus predictions from multiple tools, validation against known experimental data where available, and a discussion of the limitations. Consider experimental validation of at least a subset of predicted PTM sites.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Clinical significance and generalizability
- **Claim pointer** The authors suggest that patients with IDL mutations should not be assured of a benign phenotype and that improved risk stratification tools are needed.
- **Evidence pointer** Section 3 (Discussion), Section 5 (Conclusions)
- **Concern** The clinical implications are stated strongly given the small sample size and lack of functional data. The study includes only 9 patients with IDL mutations, and the clinical outcomes are heterogeneous. The claim that IDL mutations are associated with severe phenotypes is based on a small number of cases and may not be generalizable. The recommendation for caution in using predictive tools is reasonable but the evidence base is limited.
- **Why it matters** Overstated clinical implications could lead to changes in patient management based on insufficient evidence.
- **Resolution test** Temper the conclusions to reflect the hypothesis-generating nature of the study. Clearly state the limitations of the sample size and the need for larger, multi-center studies to confirm the findings.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of reporting
- **Affected element** Section 2.1, Table 1
- **Evidence pointer** Table 1
- **Issue** The clinical variables presented in Table 1 are not all clearly defined. For example, "f-QRSd," "RMS40," and "LAS40" are mentioned but their clinical significance is not explained in the text.
- **Required correction** Provide brief definitions or references for these electrocardiographic parameters in the text or table legend.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Section 2.1, Supplementary Tables S2 and S3
- **Evidence pointer** Supplementary Tables S2 and S3
- **Issue** The supplementary tables are referenced but their content is not described in the main text. It is unclear what additional information they provide.
- **Required correction** Add a brief description of the supplementary tables in the main text, summarizing the key findings presented in them.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methodology detail
- **Affected element** Section 4.2
- **Evidence pointer** Section 4.2
- **Issue** The genetic analysis section states that a "Next Generation Sequencing panel of genes" was used, but the specific genes included in the panel are not listed.
- **Required correction** List the genes included in the panel or provide a reference to the panel design.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Section 4.6
- **Evidence pointer** Section 4.6
- **Issue** The statistical analysis section is very brief and does not specify which tests were used for which comparisons. It is also unclear whether any corrections for multiple testing were applied.
- **Required correction** Provide a more detailed description of the statistical methods, including the specific tests used for each comparison and whether any adjustments were made for multiple testing.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Language and clarity
- **Affected element** Section 3 (Discussion)
- **Evidence pointer** Section 3
- **Issue** The discussion contains some speculative statements that are not clearly linked to the data. For example, the claim that PTM disruption "could lead to loss of flexibility and docking" is not directly supported by the results.
- **Required correction** Clearly distinguish between findings and speculation. Use phrases such as "we hypothesize" or "it is possible that" for speculative statements.

## Risk / unsupported claims
- The claim that IDL mutations are clinically significant and should not be considered benign is not supported by direct functional evidence.
- The claim that NaV1.5 has the highest IDR content among sodium channel family members is based solely on in silico predictions without experimental validation.
- The claim that PTM disruption in IDLs contributes to BrS pathogenesis is speculative and not tested in this study.
- The assertion that in silico tools "often underestimate" the impact of IDL mutations is based on a small number of cases and lacks a systematic evaluation of prediction tool performance.
- The clinical similarity between IDL and TD mutation groups is not statistically established due to inadequate power and analysis methods.