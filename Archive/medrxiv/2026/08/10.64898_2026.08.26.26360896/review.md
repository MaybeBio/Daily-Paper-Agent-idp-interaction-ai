## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure/table references
- **Assessment boundary** Scientific validity, technical soundness, and support for claims based solely on the provided manuscript text; no external data or unpublished materials were consulted
- **Shared manuscript claim summary** The authors report that a germline SNP (p.S464T, rs10761725) in KDM3C/JMJD1C is associated with favorable chemoradiotherapy outcomes in LARC and LA-HNSCC patients. They propose that this variant disrupts MDC1-RNF8-RAP80-BRCA1 DNA repair complex assembly, leading to impaired DNA repair, increased cGAS-STING signaling, and enhanced sensitivity to DNA-damaging agents. Population cohort analyses suggest increased cancer incidence, particularly skin cancer, among carriers.
- **Visible evidence base** Results sections describing patient cohort genotyping (LARC n=84, HNSCC n=90), isogenic cell line experiments (RCM-1, CAL-27, SCC-9), AlphaFold2/3 structural modeling, transcriptomic analyses, and UK Biobank/All of Us population studies; methods sections for experimental procedures; supplementary table/figure references
- **Missing materials affecting confidence** Supplementary figures and tables (referenced but not provided), detailed statistical outputs for population analyses, raw sequencing data, complete AlphaFold modeling parameters, and full gnomAD/TCGA analysis details; these omissions limit verification of several key claims

## Reviewer
- **Overall assessment** This manuscript presents a potentially interesting observation linking a common germline variant in KDM3C to chemoradiotherapy response, with a proposed mechanistic pathway involving DNA repair complex assembly. The clinical association data, while based on modest cohort sizes, are suggestive. However, the mechanistic evidence is largely indirect, relying on computational modeling and correlative cellular assays rather than direct biochemical validation. The population-level cancer incidence findings, while intriguing, lack sufficient methodological detail to assess robustness. The manuscript would benefit from stronger direct evidence of the proposed molecular mechanism and more rigorous statistical handling of the clinical associations.
- **Who would be interested in the results, and why** Radiation oncologists and medical oncologists treating rectal and head and neck cancers would find the potential predictive biomarker clinically relevant. Cancer biologists studying DNA damage response, particularly the MDC1-RNF8-RAP80-BRCA1 axis, would be interested in the proposed mechanistic link. Genetic epidemiologists studying germline modifiers of cancer risk and treatment response would also find the population-level associations relevant. The work may also interest researchers studying intrinsically disordered regions in DNA repair proteins.
- **Major strengths** The study addresses an important clinical need for predictive biomarkers in chemoradiotherapy. The multi-pronged approach, combining clinical cohorts, isogenic cell models, structural modeling, and population data, is commendable. The identification of a common variant with potential functional consequences in a chromatin regulator is novel. The use of patient-derived lymphoblastoid lines and organoids adds translational relevance. The structural modeling, while computational, provides a plausible mechanistic framework.
- **Major Concerns** The mechanistic claims are not directly validated. The proposed disruption of KDM3C-MDC1 interaction and downstream RAP80-BRCA1 assembly is inferred from colocalization studies and computational modeling, but no direct binding assays, mutagenesis experiments, or rescue experiments are presented. The clinical associations, while statistically significant, are based on relatively small cohorts and lack adjustment for potential confounders. The population-level cancer incidence findings, particularly the skin cancer association, require more rigorous epidemiological analysis. The transcriptomic data show heterogeneous gene expression changes across cell lines, with only two consistently differentially expressed genes, which weakens the claim of a shared transcriptional program.
- **Minor Comments** Several methodological details are missing, including the criteria for defining complete versus poor responders, the handling of multiple testing in the pathway enrichment analyses, and the specific parameters used in AlphaFold modeling. The manuscript would benefit from a more detailed description of the UK Biobank and All of Us analyses, including how cancer incidence was ascertained and how potential confounders were handled. The statement that the SNP is "associated with improved outcomes" in the abstract is somewhat stronger than the data support, given the observational nature of the clinical cohorts.
- **Technical failings that need to be addressed before the case is established** The lack of direct biochemical evidence for the proposed mechanism is a significant gap. The colocalization data, while suggestive, do not demonstrate a causal link between the KDM3C variant and impaired repair complex assembly. The computational modeling, while informative, requires experimental validation. The clinical association data, while statistically significant, need to be replicated in larger, independent cohorts with appropriate adjustment for confounders. The population-level cancer incidence findings require more rigorous epidemiological analysis.
- **Assessment against Nature-style criteria** Originality: The finding of a common germline variant in a chromatin regulator affecting DNA repair and treatment response is novel and potentially significant. Scientific importance: If validated, this could have implications for personalized cancer therapy and understanding of DNA repair regulation. Interdisciplinary readership: The work bridges clinical oncology, DNA repair biology, and genetic epidemiology, which could attract broad interest. Technical soundness: The experimental approaches are generally appropriate, but the lack of direct mechanistic validation and the reliance on computational modeling weaken the technical case. Readability for nonspecialists: The manuscript is generally well-written and accessible, though some sections, particularly the structural modeling, may be challenging for non-experts.
- **Recommendation posture** Supportive if technical concerns are resolved. The clinical observation is potentially important, and the proposed mechanism is plausible. However, the current evidence does not fully establish the mechanistic link, and the clinical associations need replication. The manuscript would be strengthened by direct biochemical validation of the proposed mechanism, more rigorous clinical association analyses, and clearer presentation of the population-level findings.

### Major Concerns
- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic validation
- **Claim pointer** The authors claim that the KDM3C S464T variant "disrupts assembly of the MDC1–RNF8–RAP80–BRCA1 repair complex" and that this is the mechanistic basis for enhanced chemoradiotherapy sensitivity.
- **Evidence pointer** Results sections "KDM3C SNP-S464T disrupts MDC1–RNF8–RAP80-BRCA1 pathway assembly" and "The highly conserved S464 residue localizes to an intrinsically disordered region associated with BRCA1 repair"; Figure 3; Supplementary Figure 2
- **Concern** The evidence for disrupted complex assembly is indirect. The authors show reduced colocalization of MDC1-RAP80 and RAP80-BRCA1 by immunofluorescence, but do not directly demonstrate that the KDM3C variant impairs the physical interaction between KDM3C and MDC1, or that this leads to defective recruitment of downstream repair factors. The AlphaFold modeling is computational and requires experimental validation. No direct binding assays, co-immunoprecipitation with purified proteins, or mutagenesis studies are presented to confirm the proposed mechanism.
- **Why it matters** The central mechanistic claim is the foundation of the paper's significance. Without direct evidence that the S464T variant disrupts KDM3C-MDC1 interaction and downstream repair complex assembly, the link between the genetic variant and the observed cellular phenotypes remains correlative rather than causal.
- **Resolution test** The authors should provide direct biochemical evidence, such as co-immunoprecipitation or pull-down assays showing reduced binding between KDM3C (S464T) and MDC1 compared to wild-type, and demonstrate that this leads to impaired recruitment of RAP80 and BRCA1 to damage sites. Ideally, rescue experiments where wild-type KDM3C is reintroduced into S464T cells should restore normal repair complex assembly and sensitivity.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Clinical association robustness
- **Claim pointer** The authors claim that the KDM3C S464T variant is "associated with improved response to CRT in patients with LARC and LA-HNSCC" based on the initial discovery cohort and expanded genotyping.
- **Evidence pointer** Results section "Germline missense polymorphism in KDM3C associates significantly with favorable outcomes"; Figure 1E-G; Supplementary Tables 9-10
- **Concern** The clinical cohorts are relatively small (LARC n=84, HNSCC n=90) and the analyses do not appear to adjust for potential confounders such as age, sex, tumor stage, HPV status (for HNSCC), or treatment regimen. The definition of complete versus poor responders based on NAR score is described, but the distribution of clinical and demographic characteristics across genotype groups is not fully presented. The HNSCC analysis uses recurrence as an endpoint, which is reasonable, but the details of how recurrence was ascertained and the follow-up duration are not provided.
- **Why it matters** The clinical association is the primary translational finding. If the association is confounded or not robust, the clinical utility of the biomarker is questionable. Small cohorts with potential confounding can lead to false-positive associations.
- **Resolution test** The authors should provide a more detailed description of the clinical cohorts, including baseline characteristics by genotype group, and perform multivariable analyses adjusting for relevant confounders. Ideally, the association should be validated in an independent, larger cohort. The authors should also report the sensitivity and specificity of the genotype as a predictive biomarker.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Population-level cancer incidence
- **Claim pointer** The authors claim that the S464T variant is "associated with increased cancer incidence, particularly skin cancer" based on UK Biobank and All of Us analyses.
- **Evidence pointer** Results section "KDM3C SNP-S464T is associated with increased cancer incidence in population cohorts"; Figure 7A-B
- **Concern** The population-level analyses are presented with limited methodological detail. The specific cancer types, the number of cases, the statistical models used, and how potential confounders (e.g., sun exposure, skin type, family history) were handled are not described. The relative risk estimates are presented without confidence intervals or effect sizes. The finding of increased cervical carcinoma in situ in the UK Biobank but not in All of Us, and the inconsistent findings for breast and colorectal cancer across cohorts, raise questions about the robustness of the associations.
- **Why it matters** The population-level findings support the broader relevance of the variant to cancer susceptibility. If these associations are not robust, they could be spurious and detract from the main clinical finding.
- **Resolution test** The authors should provide a detailed description of the population cohort analyses, including the specific cancer types, number of cases and controls, statistical models, and adjustment for confounders. They should report effect sizes with confidence intervals and p-values. Ideally, the analyses should be replicated in additional independent cohorts.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Transcriptomic evidence
- **Claim pointer** The authors state that transcriptomic analyses identified "hundreds of differentially expressed genes" but that only DAPK1 and CXCL8 were consistently changed across all three isogenic cell lines.
- **Evidence pointer** Results section "KDM3C SNP-S464T induces S-phase stalling and γH2AX accumulation"; Supplementary Figure 5; Supplementary Table 17
- **Concern** The transcriptomic data are presented as supporting evidence for a shared functional consequence of the variant, but the finding that only two genes are consistently differentially expressed across cell lines is a weak basis for this claim. The authors do not discuss whether the lack of overlap reflects biological heterogeneity, technical variability, or insufficient statistical power. The functional significance of DAPK1 downregulation and CXCL8 upregulation in the context of DNA repair is not explored.
- **Why it matters** The transcriptomic data are used to support the claim that the variant has a consistent functional impact. If the transcriptional response is highly heterogeneous, it is difficult to attribute the observed phenotypes specifically to the KDM3C variant.
- **Resolution test** The authors should provide a more detailed analysis of the transcriptomic data, including the number of differentially expressed genes in each cell line, the overlap between cell lines, and the statistical thresholds used. They should also discuss the potential reasons for the limited overlap and explore the functional relevance of the consistently changed genes.

### Minor Comments
- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Clinical association analyses
- **Evidence pointer** Figure 1E-G; Results section "Germline missense polymorphism in KDM3C associates significantly with favorable outcomes"
- **Issue** The p-values for the clinical associations are reported, but effect sizes, odds ratios, or confidence intervals are not provided. The authors state "p<0.0001" and "p<0.000001" but do not report the magnitude of the association.
- **Required correction** Report effect sizes (e.g., odds ratios) with 95% confidence intervals for the genotype-outcome associations in both the LARC and HNSCC cohorts.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodology clarity
- **Affected element** AlphaFold modeling
- **Evidence pointer** Methods section "Molecular modeling studies"; Figure 4
- **Issue** The description of the AlphaFold modeling is brief. The specific parameters used, the selection of the peptide length, and the criteria for selecting the top models are not fully described. The use of binding free energy calculations from the PISA server is mentioned, but the limitations of this approach are not discussed.
- **Required correction** Provide more detail on the modeling parameters, model selection criteria, and the limitations of the computational approach. Consider including a supplementary figure showing the distribution of model scores.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Population cohort analyses
- **Evidence pointer** Figure 7A-B; Results section "KDM3C SNP-S464T is associated with increased cancer incidence in population cohorts"
- **Issue** The figure appears to show relative risk estimates, but the specific cancer types and the number of cases for each are not clearly labeled. The figure legend is not provided in the manuscript text.
- **Required correction** Ensure that the figure clearly labels the cancer types, the number of cases, and the statistical significance. Provide a detailed figure legend.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion of clinical implications
- **Evidence pointer** Discussion section
- **Issue** The authors suggest that the variant could be used for "biomarker-driven stratification of patients receiving chemoradiotherapy," but they do not discuss the practical considerations, such as the prevalence of the variant in different populations, the number needed to test, or how the biomarker would be implemented in clinical practice.
- **Required correction** Add a brief discussion of the practical considerations for clinical implementation, including the prevalence of the variant and potential study designs for prospective validation.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction; Discussion
- **Issue** The authors mention that KDM3C has been implicated in DNA repair, but the discussion of prior work is brief. A more thorough review of the literature on KDM3C's role in DNA repair and cancer would strengthen the context.
- **Required correction** Expand the discussion of prior work on KDM3C, particularly studies that have directly examined its role in DNA repair or its association with cancer outcomes.

## Risk / unsupported claims
- The claim that the S464T variant "disrupts assembly of the MDC1–RNF8–RAP80–BRCA1 repair complex" is not directly supported by the provided evidence, which relies on colocalization studies and computational modeling rather than direct biochemical validation.
- The claim that the variant is "associated with improved response to CRT" in LARC and HNSCC is based on relatively small cohorts and lacks adjustment for potential confounders; the robustness of this association is not fully established.
- The claim that the variant is "associated with increased cancer incidence, particularly skin cancer" in population cohorts is based on analyses with limited methodological detail; the consistency and robustness of these findings are not fully established.
- The claim that the variant "creates a neo-phosphorylation motif" is based solely on in silico prediction and has not been experimentally validated.
- The claim that the variant leads to "increased cGAS-cGAMP-STING signaling" is based on a limited set of experiments and the functional link to the proposed mechanism is not fully established.