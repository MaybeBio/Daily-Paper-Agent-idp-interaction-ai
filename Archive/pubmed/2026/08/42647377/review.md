## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodological soundness, interpretation of results, and alignment with stated conclusions
- **Shared manuscript claim summary** The authors present a computational analysis of intrinsically disordered regions (IDRs) in human PIEZO1 and PIEZO2 mechanosensitive ion channels, integrating multiple disorder predictors, phase separation propensity tools, interaction network analysis, evolutionary conservation, ClinVar variant mapping, and peptide structural modeling. They report moderate intrinsic disorder in both proteins, with PIEZO2 showing higher disorder and phase separation potential, and find that pathogenic variants predominantly localize to ordered regions while disordered regions harbor proportionally more benign variants. They propose that IDRs contribute to PIEZO channel regulation and that some disease variants may disrupt dynamic interaction interfaces.
- **Visible evidence base** Full text including abstract, introduction, methods, results, discussion, and conclusions. Figures and tables are referenced but not directly viewable. No supplementary materials provided.
- **Missing materials affecting confidence** Figures 1-12 and Table 1-2 are referenced but not available for direct inspection. PEP-FOLD4 structural models are described qualitatively without quantitative metrics. Raw data, prediction scores per residue, and statistical analysis outputs are not provided. The specific ClinVar variant list and their exact genomic positions are not included.

## Reviewer
- **Overall assessment** This manuscript presents a comprehensive computational survey of intrinsic disorder in PIEZO1 and PIEZO2, addressing a genuinely under-explored aspect of these important mechanosensitive channels. The multi-predictor approach and integration of diverse bioinformatics tools is commendable and provides a useful resource for the field. However, the study is entirely computational and descriptive, with no experimental validation. The central claims regarding the functional significance of IDRs in PIEZO gating and channelopathies remain speculative. The statistical analyses are underpowered by small variant numbers in disordered regions, and the peptide modeling is qualitative. The manuscript would benefit from clearer hypothesis-driven framing, quantitative structural comparisons, and a more cautious interpretation of the phase separation findings given the known limitations of prediction tools in this area.
- **Who would be interested in the results, and why** Researchers studying mechanotransduction and PIEZO channel biology would find the IDR mapping useful for designing mutagenesis experiments. Clinicians and geneticists working on PIEZO-associated channelopathies may appreciate the variant distribution analysis. The broader intrinsically disordered protein community would be interested in the application of disorder prediction to a large membrane protein complex. However, the lack of experimental validation limits the impact for most of these audiences.
- **Major strengths** 1) Comprehensive multi-predictor approach for disorder assessment, reducing tool-specific bias. 2) Integration of diverse data types including disorder, phase separation, interactions, conservation, and clinical variants. 3) The observation that pathogenic variants concentrate in ordered regions is potentially informative for variant interpretation. 4) The evolutionary conservation analysis of disordered regions is thoughtful and appropriately nuanced. 5) The authors acknowledge limitations and avoid overclaiming in several places.
- **Major Concerns** 1) The central functional claims are not supported by experimental evidence. 2) Statistical power for the variant distribution analysis is limited by small numbers. 3) The phase separation predictions are presented with more confidence than the tools warrant. 4) The peptide modeling is qualitative and lacks quantitative comparison metrics. 5) The proteoform discussion in the abstract and conclusions appears disconnected from the actual analyses performed.
- **Minor Comments** 1) The introduction is overly long and contains substantial background that could be condensed. 2) Some terminology is used imprecisely (e.g., "moderate disorder" without clear operational definition). 3) The relationship between specific IDRs and known PIEZO structural domains could be more clearly articulated. 4) The discussion of acquired channelopathies (DOMS, POIS) seems tangential to the main analysis. 5) Figure quality cannot be assessed but the descriptions suggest dense, complex figures that may be difficult to interpret.
- **Technical failings that need to be addressed before the case is established** The manuscript does not provide quantitative evidence that the identified IDRs are functionally relevant. The claim that "some disease variants may disrupt dynamic interaction interfaces" is based on qualitative peptide modeling of only two variants. The phase separation predictions from FuzDrop and MolPhase are presented as convergent evidence, but these tools have known false positive rates and the authors do not discuss this adequately. The statistical comparison of variant distributions between ordered and disordered regions does not account for the different lengths of these regions or the mutational target size.
- **Assessment against Nature-style criteria** Originality: Moderate. The application of disorder prediction to PIEZO channels is novel, but the general approach of mapping IDRs in disease-associated proteins is well established. Scientific importance: Moderate. The findings are potentially useful but do not fundamentally change understanding of PIEZO biology. Interdisciplinary readership: Limited. The manuscript is primarily of interest to the IDP and mechanotransduction communities. Technical soundness: Adequate for a computational study, but the lack of experimental validation and the qualitative nature of the structural modeling weaken the conclusions. Readability for nonspecialists: The manuscript is dense and assumes substantial background knowledge in both IDP biology and ion channel structure. The abstract is accessible but the main text would be challenging for nonspecialists.
- **Recommendation posture** Currently not established from the provided evidence. The computational analyses are competently executed and the descriptive findings may be publishable in a specialized journal, but the functional claims require experimental validation or substantial reframing as hypothesis-generating observations.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors claim that IDRs in PIEZO1 and PIEZO2 play roles in "regulatory functions" and that mutations in these regions "may disrupt dynamic interaction interfaces rather than global structure."
- **Evidence pointer** Section 3.6, Figures 9-10
- **Concern** The functional significance of the identified IDRs is inferred entirely from computational predictions. The peptide modeling using PEP-FOLD4 is qualitative, with no quantitative metrics such as RMSD, radius of gyration, or free energy differences between wild-type and mutant conformations. The claim that mutations alter "local conformational tendencies" is based on visual inspection of predicted structures for two variants. No experimental data (e.g., electrophysiology, FRET, crosslinking) is provided to support functional claims.
- **Why it matters** The central thesis of the paper is that IDRs contribute to PIEZO channel regulation and disease. Without experimental validation, this remains a hypothesis. The qualitative nature of the structural modeling does not provide convincing evidence that the observed conformational differences are biologically meaningful.
- **Resolution test** Provide quantitative structural comparisons (e.g., ensemble overlap, secondary structure propensity differences with error estimates) and/or experimental validation such as mutagenesis coupled with functional assays. Alternatively, reframe the claims as purely hypothesis-generating.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors state that pathogenic variants are "predominantly" in ordered regions and that disordered regions contain "proportionally more benign variants and relatively few pathogenic mutations."
- **Evidence pointer** Section 3.4, Section 3.5, Figures 7-8
- **Concern** The statistical analysis of variant distribution does not appear to account for the relative lengths of ordered versus disordered regions. With only 22 pathogenic variants in PIEZO1 and 24 in PIEZO2, the power to detect enrichment or depletion in disordered regions is extremely limited. The Fisher's exact test p-values reported (e.g., p = 0.075 for PIEZO1) are marginal and the authors acknowledge the trend is not significant, yet the abstract and conclusions present this as a key finding.
- **Why it matters** The distribution of pathogenic versus benign variants is a central result of the paper. If the statistical analysis is underpowered or improperly normalized, the conclusion that pathogenic variants concentrate in ordered regions may be an artifact of small sample sizes or region length differences.
- **Resolution test** Provide a properly normalized analysis accounting for region lengths (e.g., variants per residue in ordered vs. disordered regions), with confidence intervals. Report effect sizes and power analysis. If the trend remains, present it as a preliminary observation requiring larger cohort validation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation
- **Claim pointer** The authors state that "PIEZO proteins also perfectly illustrate the proteoform concept, where one gene yields a highly diverse kit of mechanosensitive molecular tools."
- **Evidence pointer** Abstract, Section 4
- **Concern** The proteoform concept is mentioned in the abstract and conclusions but is not developed or supported by any specific analysis in the results. The authors do not identify specific proteoforms, quantify their diversity, or link them to the IDR analysis. This claim appears disconnected from the actual data presented.
- **Why it matters** The proteoform claim is presented as a key conceptual contribution but is not substantiated. This weakens the paper's framing and may mislead readers about the scope of the findings.
- **Resolution test** Either remove the proteoform claim or provide specific evidence for proteoform diversity (e.g., splice variants, PTM combinations, conformational states) linked to the IDR analysis.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical validity
- **Claim pointer** The authors present FuzDrop and MolPatch predictions of phase separation propensity as convergent evidence that PIEZO1 and PIEZO2 may participate in biomolecular condensates.
- **Evidence pointer** Section 3.2, Figures 2C, 3C
- **Concern** Phase separation prediction tools are known to have high false positive rates, particularly for large multi-pass membrane proteins where the prediction algorithms were not designed or validated. The authors acknowledge the need for experimental validation but still present the phase separation findings as a significant result. The biological plausibility of a transmembrane channel undergoing liquid-liquid phase separation in the cytoplasm is not critically examined.
- **Why it matters** The phase separation claims could be misleading if presented without adequate caveats. The tools used are not validated for membrane proteins, and the functional implications of phase separation for a mechanosensitive channel are unclear.
- **Resolution test** Add explicit discussion of the limitations of phase separation prediction for membrane proteins. Consider whether the phase separation analysis adds sufficient value to justify inclusion, or whether it should be moved to supplementary material with stronger caveats.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 1.1
- **Evidence pointer** "location not provided"
- **Issue** The introduction contains extensive background on mechanotransduction and PIEZO structure that is well known to the target audience. The section could be condensed by approximately 30-40% without losing essential information.
- **Required correction** Streamline the introduction to focus on the gap in knowledge regarding IDRs in PIEZO channels and the specific questions addressed.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Section 3.1
- **Evidence pointer** Table 1
- **Issue** The terms "moderate disorder" and "moderate-to-high disorder" are used without a clear operational definition. Different predictors give different ranges, and the classification of a protein as "moderately disordered" is not standardized.
- **Required correction** Define the classification thresholds explicitly (e.g., based on PPIDR ranges) and report the range across predictors for each protein.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section 2.2
- **Evidence pointer** "location not provided"
- **Issue** The RIDAO platform version is specified, but the specific parameters and settings for each predictor are not described. The D2P2 platform access date is given, but the specific version or build is not.
- **Required correction** Provide the exact software versions, parameters, and any non-default settings used for each prediction tool to ensure reproducibility.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Section 3.5
- **Evidence pointer** "location not provided"
- **Issue** The Fisher's exact test p-values are reported, but odds ratios and confidence intervals are not consistently provided. The comparison between PIEZO1 and PIEZO2 variant distributions is not formally tested.
- **Required correction** Report odds ratios with 95% confidence intervals for all comparisons, and include a formal test comparing the two proteins' variant distributions.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 3.7
- **Evidence pointer** Table 2
- **Issue** The ConSurf analysis is described as using 150 homologs, but the selection criteria for these homologs (e.g., sequence identity range, taxonomic distribution) are not specified. The "major disordered region" analyzed is not clearly defined.
- **Required correction** Specify the homolog selection criteria and define the boundaries of the major disordered region analyzed.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Section 3.3
- **Evidence pointer** Figures 4-6
- **Issue** The PPI network analysis identifies associations with DNA replication and cell cycle proteins, but the authors do not discuss potential mechanisms or whether these are likely to be direct physical interactions or indirect functional associations.
- **Required correction** Add a brief discussion of the potential significance of these unexpected associations, or explicitly note that they may reflect indirect functional relationships.

## Risk / unsupported claims
- The claim that IDRs in PIEZO1 and PIEZO2 serve "regulatory functions" in channel gating is unsupported by experimental evidence.
- The claim that mutations in disordered regions "may disrupt dynamic interaction interfaces" is based on qualitative modeling of only two variants and is not quantitatively substantiated.
- The proteoform claim in the abstract and conclusions is not supported by any specific analysis in the results.
- The phase separation predictions are presented with more confidence than the validation status of the tools warrants, particularly for large membrane proteins.
- The statement that "pathogenic variants are predominantly in ordered regions" is presented as a key finding despite marginal statistical significance and potential confounding by region length.
- The evolutionary conservation analysis of IDRs is descriptive and does not establish functional significance.