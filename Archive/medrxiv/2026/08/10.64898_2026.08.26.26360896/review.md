## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure/table references
- **Assessment boundary** Scientific validity of claims, experimental design, statistical rigor, and clinical relevance based solely on the provided manuscript text
- **Shared manuscript claim summary** The authors identify a germline KDM3C polymorphism (p.S464T, rs10761725) associated with favorable chemoradiotherapy outcomes in LARC and LA-HNSCC patients, and propose a mechanism involving impaired MDC1-RNF8-RAP80-BRCA1 DNA repair complex assembly, increased DNA damage sensitivity, and enhanced cGAS-STING signaling
- **Visible evidence base** Clinical genotyping data (LARC n=84, HNSCC n=90), isogenic cell line models (RCM-1, CAL-27, SCC-9), AlphaFold2/3 structural predictions, RNA-seq data, immunocytochemistry, and population cohort analyses (UK Biobank, All of Us, TCGA)
- **Missing materials affecting confidence** Supplementary figures and tables referenced but not provided; detailed statistical methods for population analyses not included; raw sequencing data not accessible; no experimental validation of KDM3C phosphorylation at residue 464

## Reviewer
- **Overall assessment** This manuscript presents a potentially interesting observation linking a common germline polymorphism in KDM3C to chemoradiotherapy response, with a proposed mechanistic framework. The clinical association data are intriguing but based on modest sample sizes and retrospective cohorts. The mechanistic studies are largely descriptive and rely heavily on computational modeling without direct biochemical validation of the key claims. The population-level cancer incidence data are provocative but the effect sizes are small and the analyses appear to lack adequate control for multiple testing and confounding variables. The manuscript would benefit from substantial additional experimental evidence to support the central mechanistic claims and from more rigorous clinical validation before the conclusions can be considered established.

- **Who would be interested in the results, and why** Radiation oncologists and medical oncologists treating rectal and head and neck cancers would find the potential predictive biomarker clinically relevant. Cancer biologists studying DNA damage response pathways, particularly those focused on chromatin regulators and the MDC1-RNF8 axis, would be interested in the proposed mechanism. Genetic epidemiologists studying germline modifiers of cancer treatment response would also find the population-level analyses relevant. The work may also interest researchers studying cGAS-STING signaling in the context of DNA damage and therapeutic response.

- **Major strengths** The study addresses an important clinical problem with a clear translational goal. The identification of a common polymorphism with potential predictive value across two cancer types is clinically meaningful. The use of patient-derived lymphoblastoid cell lines and isogenic CRISPR-edited models adds credibility. The integration of structural modeling with functional assays is a thoughtful approach. The population-level analyses in UK Biobank and All of Us provide additional context for the clinical relevance of the variant.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Clinical association validity
- **Claim pointer** The authors claim that KDM3C p.S464T (T/T genotype) is significantly associated with favorable CRT outcomes in LARC and LA-HNSCC patients.
- **Evidence pointer** Results section, Figure 1E-G, Supplementary Tables 9-10
- **Concern** The initial discovery cohort is very small (n=30 LARC patients), and the expanded LARC cohort (n=84) and HNSCC cohort (n=90) are still modest. The authors report p<0.0001 for the LARC association and p<0.000001 for HNSCC, but the manuscript does not provide details on how multiple testing was handled given that 77 genes harbored candidate variants. The analysis appears to be a candidate gene approach, but the selection of the 161-gene panel and the statistical framework for testing associations across multiple genes and variants is not clearly described. Additionally, the HNSCC cohort analysis uses recurrence as the endpoint, which is reasonable, but the manuscript does not specify whether this was a pre-specified analysis or a post-hoc finding. The lack of a validation cohort from an independent institution is a significant limitation.
- **Why it matters** The central clinical claim of the manuscript rests on these associations. If the statistical framework is not robust or the findings cannot be replicated, the entire premise of the study is undermined. Small cohorts with multiple testing can produce spurious associations.
- **Resolution test** The authors should provide a clear description of the multiple testing correction applied, ideally with a pre-specified analysis plan. Independent validation in an external cohort is essential. Sensitivity analyses adjusting for known clinical prognostic factors (e.g., stage, HPV status in HNSCC) should be performed.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic evidence
- **Claim pointer** The authors claim that the S464T substitution impairs MDC1-RNF8-RAP80-BRCA1 complex assembly, leading to defective DNA repair.
- **Evidence pointer** Results section, Figure 3A-G, Supplementary Figure 2
- **Concern** The mechanistic evidence relies heavily on co-immunoprecipitation and colocalization studies. The key claim that S464T impairs KDM3C-MDC1 interaction is supported by a single Co-IP experiment (Figure 3A) without quantitative analysis or replicates shown. The mass spectrometry data (Figure 3B) is described but the actual phosphopeptide data is not presented in sufficient detail. The colocalization studies (Figure 3C-E) show differences but the magnitude of the effects and the statistical significance are not clearly reported. Most critically, the authors do not directly demonstrate that the S464T variant affects DNA repair kinetics or repair pathway choice. The claim that "impaired DNA repair" occurs is inferred from γH2AX persistence and cell survival, but direct measurement of homologous recombination or non-homologous end joining efficiency is not provided.
- **Why it matters** The mechanistic model is the core scientific contribution of the manuscript. Without direct evidence of impaired DNA repair, the link between the polymorphism and treatment sensitivity remains correlative. The proposed mechanism must be experimentally validated to support the conclusions.
- **Resolution test** The authors should provide quantitative Co-IP data with replicates and statistical analysis. Direct measurement of DNA repair efficiency (e.g., reporter assays for HR and NHEJ, neutral comet assay, or pulsed-field gel electrophoresis) in isogenic cell lines is essential. Phosphorylation of S464 should be directly demonstrated or refuted using phospho-specific antibodies or mass spectrometry.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Structural modeling interpretation
- **Claim pointer** The authors claim that AlphaFold3 modeling predicts that the S464T substitution enhances phospho-dependent interaction with the RNF8 FHA domain, potentially trapping the complex.
- **Evidence pointer** Results section, Figure 4A-M, Supplementary Table 15
- **Concern** The structural modeling is presented as a key mechanistic insight, but the interpretation is speculative. The claim that a "kinetic trap" prevents proper complex assembly is not supported by any experimental data. The AlphaFold3 predictions are computational and have not been validated biochemically. The binding free energy calculations using PISA are based on static structures and do not account for the dynamic nature of protein-protein interactions. The authors acknowledge that phosphorylation of S464 is not experimentally confirmed, yet the entire structural argument depends on this modification. The NetPhos prediction of a PKC site is in silico only and requires experimental validation.
- **Why it matters** The structural model provides the proposed explanation for how a single amino acid substitution in an intrinsically disordered region could have functional consequences. If the model is incorrect or the phosphorylation does not occur, the mechanistic framework collapses.
- **Resolution test** The authors should experimentally test whether S464 is phosphorylated in cells, particularly after DNA damage. Mutational analysis (e.g., S464A to prevent phosphorylation, S464E to mimic phosphorylation) should be performed to test the functional consequences. Isothermal titration calorimetry or surface plasmon resonance could directly measure binding affinity between KDM3C peptides and the RNF8 FHA domain.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Population analysis rigor
- **Claim pointer** The authors claim that the S464T variant is associated with increased cancer incidence, particularly skin cancer, in UK Biobank and All of Us cohorts.
- **Evidence pointer** Results section, Figure 7A-B
- **Concern** The population analyses are described only briefly in the main text with details relegated to supplementary materials that were not provided. The effect sizes appear small (the manuscript states "modest but significant increase") and the analyses may not have adequately controlled for ancestry, which is critical given the strong ancestry-dependent allele frequency differences reported. The UK Biobank analysis reports increased skin cancer risk in both younger and older age groups, but the manuscript does not specify whether this is melanoma, non-melanoma skin cancer, or both. The All of Us analysis reports increased overall cancer risk, breast cancer, and colorectal cancer, but the consistency between cohorts is limited to skin cancer.
- **Why it matters** The population-level claims extend the clinical relevance beyond treatment response to cancer predisposition. If these analyses are not rigorously controlled, they could mislead readers about the cancer risk associated with this very common variant.
- **Resolution test** The authors should provide full details of the population analyses including ancestry adjustment, multiple testing correction, and sensitivity analyses. The specific cancer types should be clearly defined. Replication in additional cohorts would strengthen the claims.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Clinical translation readiness
- **Claim pointer** The authors suggest that the KDM3C S464T variant could serve as a biomarker for patient stratification in chemoradiotherapy.
- **Evidence pointer** Discussion section
- **Concern** The clinical association data are based on retrospective cohorts with modest sample sizes. The manuscript does not report whether the association is independent of other known predictive factors. The sensitivity analysis in the HNSCC cohort does not appear to account for HPV status, which is the dominant prognostic factor in this disease. The LARC analysis does not appear to adjust for clinical stage or other established prognostic variables. The predictive (as opposed to prognostic) value of the variant is not established, as the authors do not compare outcomes between treatment arms or demonstrate that the variant specifically predicts benefit from CRT rather than overall prognosis.
- **Why it matters** The clinical utility of a biomarker depends on its ability to inform treatment decisions. A prognostic marker that correlates with outcome regardless of treatment is less useful for stratification. The current data do not distinguish between prognostic and predictive value.
- **Resolution test** The authors should perform multivariable analyses adjusting for known prognostic factors. Ideally, they should test for an interaction between genotype and treatment to establish predictive value. Prospective validation would be the gold standard.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 1E
- **Evidence pointer** Results section, Figure 1E
- **Issue** The figure legend describes the segregation of patients into CR and PoR groups based on NAR score, but the specific NAR score cutoffs are not provided in the main text.
- **Required correction** Provide the NAR score thresholds used to define CR and PoR groups in the figure legend or methods.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 2A-D
- **Evidence pointer** Results section, Figure 2A-D
- **Issue** The lymphoblastoid cell line experiments use n=6 per genotype group, but the manuscript does not specify whether these are independent biological replicates or technical replicates. The statistical test used for these comparisons is not stated.
- **Required correction** Clarify the experimental design and specify the statistical tests used for each comparison.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data interpretation
- **Affected element** Figure 3C-G
- **Evidence pointer** Results section, Figure 3C-G
- **Issue** The colocalization data are normalized to WT at baseline, but the baseline values are not shown. It is unclear whether the differences observed are driven by changes in the WT or the SNP cells.
- **Required correction** Show absolute values or provide baseline values in the figure or supplementary materials.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The discussion states that the S464T variant is "associated with improved CRT outcomes" but also that it is "associated with increased cancer incidence." This apparent paradox is not addressed.
- **Required correction** Provide a brief explanation of how a variant that increases cancer risk could also improve treatment response, or acknowledge the apparent contradiction and discuss possible explanations.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Methods, CRISPR-Cas9 gene editing
- **Evidence pointer** Methods section
- **Issue** The methods state that CRISPR-Cas9 editing was performed by Synthego Corporation, but do not specify whether the edited cell lines were validated for the absence of off-target effects or whether the editing was confirmed by sequencing.
- **Required correction** Provide details on the validation of edited cell lines, including sequencing confirmation and off-target analysis.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data availability statement
- **Evidence pointer** Data availability statement
- **Issue** The data availability statement indicates that data is available on reasonable request, but does not mention whether the RNA-seq data have been deposited in a public repository.
- **Required correction** Consider depositing RNA-seq data in a public repository such as GEO or ArrayExpress and provide the accession number.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 4
- **Evidence pointer** Results section, Figure 4
- **Issue** The AlphaFold3 models are described in the text but the figure is not provided in the manuscript text. It is unclear whether the models show clear structural differences between the WT and SNP variants.
- **Required correction** Ensure that the figure clearly shows the predicted structural differences and provide a more detailed description of the models in the figure legend.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction
- **Evidence pointer** Introduction section
- **Issue** The introduction does not discuss the allele frequency of rs10761725 in different populations, which is relevant given the ancestry-dependent differences reported later.
- **Required correction** Add a brief discussion of the population genetics of this variant in the introduction or results.

## Risk / unsupported claims
- The claim that S464T "impairs DNA repair" is not directly supported by functional DNA repair assays; it is inferred from γH2AX persistence and cell survival data
- The claim that the S464T substitution creates a "neo-phosphorylation motif" is based solely on in silico prediction (NetPhos) without experimental validation
- The claim that AlphaFold3 predicts a "kinetic trap" mechanism is speculative and not supported by experimental data
- The population-level cancer incidence associations are based on analyses whose details are not fully provided and may not adequately control for ancestry and multiple testing
- The clinical association between KDM3C genotype and CRT outcomes is based on retrospective cohorts without independent validation
- The predictive (as opposed to prognostic) value of the KDM3C variant for CRT response is not established
- The claim that the S464T variant is associated with both improved CRT outcomes and increased cancer incidence presents an apparent paradox that is not addressed

## Assessment against Nature-style criteria
- **Originality** Moderate. The identification of a germline polymorphism in a chromatin regulator affecting DNA repair and treatment response is a novel concept, though the general principle that DNA repair defects sensitize to genotoxic therapy is well established. The specific link to KDM3C and the proposed mechanism involving the MDC1-RNF8-RAP80-BRCA1 axis adds originality, but the mechanistic depth is insufficient to claim a major conceptual advance.
- **Scientific importance** Potentially high if the clinical associations are validated. A common germline variant that predicts CRT response would have significant clinical utility. However, the current evidence is not sufficient to establish clinical relevance, and the mechanistic basis is incompletely validated.
- **Interdisciplinary readership** The topic bridges oncology, DNA repair biology, and pharmacogenomics, which could attract readers from multiple disciplines. The clinical relevance to rectal and head and neck cancers broadens the potential audience. However, the technical depth in structural modeling may limit accessibility for some readers.
- **Technical soundness** The experimental approaches are generally appropriate but the execution is incomplete. The lack of direct DNA repair assays, the absence of quantitative Co-IP data, and the reliance on computational predictions without experimental validation are significant weaknesses. The statistical framework for the clinical associations is not fully described.
- **Readability for nonspecialists** The manuscript is generally well-written and the logical flow is clear. However, the structural modeling sections may be challenging for readers without a computational biology background. The clinical sections are accessible, but the statistical details are not fully explained.