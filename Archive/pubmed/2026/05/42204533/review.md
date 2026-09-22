## Review setup
- **Input scope** Full manuscript text, including abstract, methods, results, discussion, and figure legends
- **Assessment boundary** Scientific validity, methodological rigor, evidence quality, and alignment with claims; no assessment of editorial fit or publication decision
- **Shared manuscript claim summary** The authors propose that thyroid-stimulating hormone receptor (TSHR) acts as a molecular hub mediating peripheral-central neuroimmune crosstalk in Graves' disease (GD) and Graves' orbitopathy (GO), based on integrated multi-omics, neuroimaging, genetic, and structural analyses
- **Visible evidence base** GWAS summary statistics (FinnGen), in-house rs-fMRI cohort (12 GD, 32 GO, 28 HC), bulk RNA-seq (20 per group), scRNA-seq (1 per group), public snRNA-seq datasets (caudate/putamen), mouse E16.5 spatial transcriptomics, immunofluorescence in GO mouse model, and computational docking/dynamics
- **Missing materials affecting confidence** Supplementary files (Additional files 1 and 2) not provided; detailed clinical criteria, quality control metrics, full statistical outputs, and methodological parameters referenced but not visible; no raw data or code availability statement

## Reviewer
- **Overall assessment** This manuscript presents an ambitious integrative analysis combining genetic, transcriptomic, neuroimaging, and structural biology approaches to investigate TSHR-mediated neuroimmune crosstalk in GD and GO. The conceptual framework of a "disease-molecule axis" is interesting and potentially valuable. However, the evidence chain contains several critical gaps. The causal inference from MR is based on very small case numbers (GD N=3,962; GO N=858), the neuroimaging validation cohort is extremely limited (N=12 and 32), and the single-cell RNA-seq validation includes only one sample per group. The structural biology and drug screening components are purely computational and presented without experimental validation. The immunofluorescence data in the mouse model, while providing tissue-level evidence, does not directly test the functional claims of neuroimmune crosstalk. The manuscript would benefit from substantial additional validation and more careful alignment between the strength of claims and the evidence provided.
- **Who would be interested in the results, and why** Researchers in autoimmune thyroid disease, neuroimmunology, and neuroendocrinology would find the integrative framework and the identification of TSHR as a potential neuroimmune mediator of interest. The multi-omics methodology may appeal to computational biologists working on disease-gene prioritization. Clinicians managing GD and GO patients with neuropsychiatric symptoms may find the brain imaging associations clinically relevant. The drug repurposing predictions could interest translational researchers, though these remain highly preliminary.
- **Major strengths** 1) The integration of multiple data modalities (genetics, transcriptomics, imaging, structural biology) is comprehensive and methodologically ambitious. 2) The bidirectional MR design and sensitivity analyses represent a rigorous approach to causal inference. 3) The convergence of MR, neuroimaging, and transcriptomic evidence on basal ganglia structures is internally consistent. 4) The authors appropriately acknowledge limitations and avoid over-claiming in several sections. 5) The concept of a "disease-molecule axis" provides a useful framework for understanding organ-specific autoimmunity with CNS involvement.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (MR power and instrument validity), R1-M2 (neuroimaging sample size and multiple comparisons), R1-M3 (scRNA-seq validation sample size), R1-M4 (immunofluorescence specificity and quantification), R1-M5 (structural predictions without experimental validation)
- **Assessment against Nature-style criteria** **Originality**: Moderate. The concept of TSHR as a neuroimmune mediator is not entirely novel, as TSHR expression in brain has been previously reported, but the systematic integration across multiple data types is a new contribution. **Scientific importance**: Potentially high if the claims are substantiated, as it could reframe understanding of GD and GO as conditions with CNS involvement mediated by a defined molecular pathway. However, the current evidence is insufficient to establish this. **Interdisciplinary readership**: The topic bridges endocrinology, immunology, and neuroscience, which could attract broad interest. **Technical soundness**: Several methodological concerns undermine confidence, particularly in the MR analysis, neuroimaging statistics, and single-cell validation. **Readability for nonspecialists**: The manuscript is generally well-written and accessible, with clear figure legends and logical flow, though some methods sections assume specialized knowledge.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript presents an interesting hypothesis-generating framework, but the evidence chain has critical gaps that prevent the central claims from being supported. Major revisions with substantial additional validation would be required.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical power and causal inference validity
- **Claim pointer** The authors claim bidirectional causal relationships between GD/GO and brain IDPs based on MR analysis
- **Evidence pointer** Methods: "Genetic association and causal inference"; Results: "Bidirectional MR analysis of GD, GO and IDPs"; Figure 2a-b
- **Concern** The MR analysis for GO uses only 858 cases, which is a very small sample for GWAS-based instrumental variable selection. With such limited case numbers, the number of genome-wide significant instruments will be extremely small, potentially leading to weak instrument bias. The authors do not report the number of SNPs used as instruments for each trait, F-statistics for individual instruments, or the results of MR-Egger intercept tests for pleiotropy. Additionally, the bidirectional MR design requires careful handling of sample overlap between the exposure and outcome GWAS, which is not described.
- **Why it matters** MR conclusions are only valid if instruments are strong and pleiotropy is adequately addressed. With small case numbers and incomplete reporting of instrument properties and sensitivity analyses, the causal claims are not adequately supported. This is the foundational layer of the entire evidence chain.
- **Resolution test** Report the number of instruments used for each exposure, their F-statistics, and the proportion of variance explained. Provide MR-Egger intercept tests, weighted median estimates, and leave-one-out analyses. If the number of instruments is very small, consider using alternative methods such as colocalization or latent causal variable analysis to strengthen causal inference. If power is insufficient, temper the causal language accordingly.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Neuroimaging statistical rigor
- **Claim pointer** The authors claim that rs-fMRI analysis independently validates MR-identified brain alterations in GD and GO
- **Evidence pointer** Methods: "Neuroimaging data acquisition and analysis"; Results: "Rs-fMRI and cross-species spatial transcriptomics validation"; Figure 2c-f
- **Concern** The neuroimaging cohort is very small (12 GD, 32 GO, 28 HC). Whole-brain voxel-wise or vertex-wise analyses with such sample sizes are severely underpowered and prone to false positives. The authors state that "multiple comparison correction was conducted within the whole brain" using Gaussian Random-Field correction, but do not report the smoothness estimates, the number of comparisons, or the specific clusters with peak coordinates and effect sizes. The overlap between MR and neuroimaging findings is described qualitatively, but no formal conjunction analysis or quantitative assessment of concordance is provided.
- **Why it matters** The neuroimaging data are presented as independent validation of the MR findings. If the imaging analysis is underpowered or not rigorously corrected, the claimed convergence of evidence is not established. Small-sample neuroimaging studies are particularly susceptible to inflated effect sizes and poor reproducibility.
- **Resolution test** Provide full cluster tables with peak coordinates, cluster sizes, and effect sizes. Report the smoothness estimates used for GRF correction. Consider whether the sample size is adequate for the analyses performed, and if not, reframe the neuroimaging results as exploratory. Provide a formal quantitative assessment of concordance between MR and neuroimaging findings, such as spatial overlap analysis or correlation of effect sizes.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Single-cell validation sample size
- **Claim pointer** The authors claim that scRNA-seq of PBMCs reveals immune landscape changes and supports the role of TSHR in peripheral immune dysregulation
- **Evidence pointer** Methods: "Bulk and single-cell RNA-seq profiling"; Results: "PBMC scRNA-seq revealed immune landscape changes of GD and GO"; Figure 5
- **Concern** The scRNA-seq data were generated from one GD patient, one GO patient, and one HC. With n=1 per group, no statistical inference is possible. The observed differences between groups cannot be distinguished from inter-individual variation. The authors do not acknowledge this limitation in the results section, and the figure presents group comparisons as if they are meaningful.
- **Why it matters** Single-cell data with n=1 per condition cannot support claims about disease-associated cellular or molecular changes. This is a fundamental limitation that affects the validity of the immune landscape characterization and the interpretation of TSHR expression patterns in peripheral immune cells.
- **Resolution test** Either provide additional scRNA-seq samples to enable statistical comparison, or explicitly reframe these results as descriptive case observations. If additional samples are not feasible, the claims about peripheral immune cell alterations should be substantially tempered and the n=1 limitation clearly stated in the results and figure legends.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Immunofluorescence validation rigor
- **Claim pointer** The authors claim that immunofluorescence staining in a GO mouse model confirms colocalization of TSHR with FN1 and GNAS in the basal ganglia
- **Evidence pointer** Methods: "Immunofluorescence validation in an adenovirus-induced GO mouse model"; Results: "TSHR was identified as the core molecule in brain changes of GD and GO"; Figure 6e, 6k
- **Concern** The immunofluorescence experiments are described as validating the predicted interactions, but no quantification is provided. The images show colocalization, but there is no assessment of the proportion of cells showing colocalization, no negative controls (e.g., antibody specificity controls, knockout tissues), and no comparison between GO model mice and wild-type controls. The use of three rabbit-derived primary antibodies with TSA multiplexing requires rigorous validation of antibody specificity and sequential staining controls, which are not described.
- **Why it matters** Colocalization by immunofluorescence is a qualitative observation that requires appropriate controls and quantification to be meaningful. Without these, the claim that TSHR interacts with FN1 and GNAS in the basal ganglia is not adequately supported. The TSA multiplexing approach is technically demanding and prone to artifacts if not properly validated.
- **Resolution test** Provide quantitative colocalization analysis (e.g., Manders coefficients) with appropriate thresholds. Include negative controls (e.g., secondary antibody only, isotype controls, or tissues from TSHR knockout animals if available). Describe the validation of antibody specificity for TSA multiplexing, including single-stain controls and sequential staining order. If possible, include wild-type control animals for comparison with the GO model.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Structural predictions without experimental validation
- **Claim pointer** The authors claim that small-molecule screening identified three repurposable compounds with favorable docking scores and stable binding poses as potential modulators of TSHR
- **Evidence pointer** Methods: "Structural biological analysis and drug screening"; Results: "Structural analysis of FN1-TSHR and GNAS-TSHR"; Figure 7
- **Concern** The docking scores and molecular dynamics simulations are purely computational predictions. No experimental validation is provided, such as binding assays, cellular signaling assays, or in vivo studies. The claim that these compounds are "repurposable" implies therapeutic potential, which is not supported by any functional data. The docking scores are presented without comparison to known binders or decoys, and the significance of the specific scores is unclear.
- **Why it matters** Computational predictions of drug binding are notoriously unreliable without experimental confirmation. Presenting these as potential therapeutic leads without any functional validation could mislead readers and is not consistent with the standards of evidence required for drug repurposing claims.
- **Resolution test** Either provide experimental validation (e.g., surface plasmon resonance, isothermal titration calorimetry, cAMP assays, or cell-based functional assays) or clearly reframe these results as purely hypothesis-generating computational predictions with no therapeutic implications. If experimental validation is not possible, remove the "repurposable" language and temper the claims substantially.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Reporting transparency
- **Affected element** Methods: "Study cohorts and data acquisition"
- **Evidence pointer** Methods section, first paragraph
- **Issue** The authors state that detailed clinical data and eligibility criteria are provided in Additional file 1 and Additional file 2, but these files were not available for review. Key information about patient recruitment, inclusion/exclusion criteria, and clinical characteristics is therefore not assessable.
- **Required correction** Provide the supplementary materials for review, or include the essential clinical characteristics and eligibility criteria in the main text.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results: "Bidirectional MR analysis of GD, GO and IDPs"
- **Evidence pointer** Figure 2a-b; Additional file 2: Tables S3-S6
- **Issue** The MR results are presented only as significant/non-significant in the figures. Effect sizes, confidence intervals, and exact p-values are not reported in the main text.
- **Required correction** Report effect sizes with confidence intervals for the key MR findings in the main text or in a summary table.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology precision
- **Affected element** Title and throughout
- **Evidence pointer** Title; Abstract; Discussion
- **Issue** The term "mediates" in the title implies a causal mechanistic role that is not directly demonstrated by the observational and computational data presented. The evidence supports associations and correlations, not mediation in the strict causal sense.
- **Required correction** Consider revising the title to use more cautious language, such as "associates with" or "is implicated in," unless direct mechanistic evidence is provided.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Methods; Data availability statement
- **Evidence pointer** Not explicitly stated in the manuscript
- **Issue** No data availability statement or code availability statement is provided. Given the multi-omics nature of the study, this is a significant omission for reproducibility.
- **Required correction** Add a data availability statement specifying where all datasets can be accessed, and a code availability statement if custom code was used.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 6e, 6k
- **Evidence pointer** Figure 6
- **Issue** The immunofluorescence images appear to be representative single fields. Without scale bars, magnification information, or multiple fields shown, the reader cannot assess the quality and representativeness of the images.
- **Required correction** Add scale bars and magnification information to all immunofluorescence images. Consider showing multiple representative fields or providing a quantification panel.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion
- **Evidence pointer** Discussion, first paragraph
- **Issue** The discussion of previous neuroimaging findings in GD and GO is brief and does not systematically compare the current findings with prior studies in terms of specific regions and direction of effects.
- **Required correction** Expand the discussion to include a more detailed comparison with prior neuroimaging studies, noting concordant and discordant findings.

## Risk / unsupported claims
- The claim that TSHR "mediates" peripheral-central neuroimmune crosstalk is not supported by direct functional evidence; the data are associative and computational
- The claim that FN1-TSHR and GNAS-TSHR interactions occur in the basal ganglia is based on computational prediction and qualitative colocalization without quantification or appropriate controls
- The claim that venetoclax, irinotecan, and dutasteride are potential TSHR modulators is unsupported by any experimental validation
- The claim of causal relationships between GD/GO and brain IDPs is based on MR with very small case numbers and incomplete sensitivity analyses
- The scRNA-seq findings are based on n=1 per group and cannot support claims about disease-associated immune landscape changes
- The neuroimaging validation is based on a very small cohort and lacks detailed statistical reporting
- The gsMap analysis uses mouse embryonic data, and the authors acknowledge cross-species limitations, but the interpretation of developmental relevance remains speculative
- The claim that TSHR expression is "notably enriched" in spiny projection neurons is based on public snRNA-seq data from non-disease tissues, which may not reflect disease states