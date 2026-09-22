## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, experimental section) as provided
- **Assessment boundary** Scientific content, experimental logic, evidence sufficiency, and claims as presented in the supplied text
- **Shared manuscript claim summary** The authors propose that HOXA1 and PITX2 form liquid-liquid phase separation condensates that drive lysosomal exocytosis-mediated SASP in gastric cancer, and that the antidepressant nortriptyline disrupts this interaction to suppress tumor progression
- **Visible evidence base** Results sections 1-7, figures referenced as Figure 1-8 and supplementary figures S1-S11, tables S1-S5, experimental methods summary
- **Missing materials affecting confidence** Full figure panels, supplementary tables and figures, raw data files, statistical details, proteomics dataset, RNA-seq dataset (GSE305469), molecular docking parameters, and detailed experimental protocols

## Reviewer
- **Overall assessment** This manuscript presents a potentially interesting connection between phase-separated transcription factor complexes and lysosomal exocytosis-mediated SASP in gastric cancer, with a drug repurposing angle. The central claim that HOXA1-PITX2 phase separation drives a specific secretory phenotype and that nortriptyline disrupts this process is ambitious and could be of interest to the cancer biology and senescence fields. However, the evidence as presented has several gaps that prevent full confidence in the conclusions. The phase separation data appear largely descriptive, the specificity of the nortriptyline effect is not rigorously established, and several key mechanistic links are asserted rather than directly demonstrated. The clinical relevance claims rest on correlative expression data that are not fully presented.

- **Who would be interested in the results, and why** Researchers studying cellular senescence and SASP in tumor biology, investigators interested in phase separation as a regulatory mechanism in cancer, and those exploring drug repurposing for cancer therapy. The connection between lysosomal exocytosis and SASP is an emerging area, and the identification of a small molecule that disrupts a phase-separated transcriptional complex could attract attention from chemical biology and translational oncology communities.

- **Major strengths** The study addresses an under-explored mechanism linking phase separation to lysosomal exocytosis and SASP. The combination of transcriptomic, proteomic, and functional approaches is comprehensive in scope. The drug screening strategy using FDA-approved compounds is pragmatic and potentially clinically translatable. The identification of specific protein domains involved in the HOXA1-PITX2 interaction adds mechanistic depth.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental evidence for phase separation
- **Claim pointer** The authors claim that HOXA1 and PITX2 form biomolecular condensates via liquid-liquid phase separation in gastric cancer cells
- **Evidence pointer** Figure 5, location not provided
- **Concern** The evidence for phase separation is limited to fluorescence microscopy showing puncta formation and sensitivity to 1,6-hexanediol. The manuscript does not report key biophysical validation experiments that are standard for establishing LLPS, such as fluorescence recovery after photobleaching (FRAP) with quantitative recovery curves, fusion events, or in vitro turbidity assays with purified proteins. The FRAP data are mentioned but not shown with sufficient quantitative detail. Additionally, the functional relevance of the condensates versus simple protein-protein interaction is not dissected.
- **Why it matters** The central mechanistic claim of the paper rests on phase separation being the operative mechanism. If the observed puncta represent aggregates or simple colocalization rather than bona fide liquid condensates, the mechanistic framework and the proposed mode of action for nortriptyline would need substantial revision.
- **Resolution test** Provide quantitative FRAP data with mobile fraction calculations, show fusion events, perform in vitro droplet formation assays with purified proteins under controlled conditions, and include a mutant that disrupts phase separation but not direct binding to demonstrate functional relevance.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Specificity of nortriptyline mechanism
- **Claim pointer** The authors claim that nortriptyline specifically disrupts HOXA1-PITX2 phase separation and that this is the mechanism of its anti-tumor effects
- **Evidence pointer** Figure 7, location not provided
- **Concern** The manuscript does not establish that nortriptyline's effects are specific to the HOXA1-PITX2 interaction. Nortriptyline is a known antidepressant with multiple cellular targets, including monoamine transporters and various receptors. The paper does not rule out off-target effects that could independently suppress lysosomal exocytosis or SASP. The molecular docking data are presented with a single score and no validation of the predicted binding site through mutagenesis. The concentration of nortriptyline used in cellular assays is not clearly stated relative to its known pharmacological profile.
- **Why it matters** The therapeutic claim depends on nortriptyline acting through this specific mechanism. If the drug works through other pathways, the proposed model and the rationale for clinical translation would be substantially weakened.
- **Resolution test** Perform mutagenesis of the predicted nortriptyline binding site on PITX2 and show loss of drug effect. Include dose-response experiments with appropriate controls. Test structurally related antidepressants that do not bind PITX2 to show specificity. Consider genetic ablation of HOXA1 or PITX2 to show that nortriptyline has no additional effect in those backgrounds.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal link between lysosomal exocytosis and SASP
- **Claim pointer** The authors claim that lysosomal exocytosis of LGALS1 and IGFBP7 from senescent cells drives tumor progression through SASP
- **Evidence pointer** Figures 3 and 6, location not provided
- **Concern** The causal relationship between lysosomal exocytosis and the observed tumor-promoting effects is not directly established. The experiments show that conditioned medium from senescent cells with PITX2 overexpression promotes proliferation and invasion, and that this is reduced by vacuolin-1 or neutralizing antibodies. However, it is not demonstrated that the effects are specifically due to lysosomal exocytosis of LGALS1 and IGFBP7 rather than other secreted factors. The manuscript does not show that recombinant LGALS1 or IGFBP7 alone can recapitulate the effects, nor that knockdown of these factors in the senescent cells abolishes the phenotype.
- **Why it matters** The model proposes a specific secretory mechanism with defined mediators. Without direct evidence that LGALS1 and IGFBP7 are the functionally relevant cargo, the mechanistic chain from phase separation to tumor progression remains incomplete.
- **Resolution test** Perform rescue experiments with recombinant LGALS1 and IGFBP7 added to conditioned medium from cells with inhibited lysosomal exocytosis. Knock down LGALS1 and IGFBP7 individually and in combination in senescent cells and assess the conditioned medium effects. Use inhibitors of lysosomal exocytosis that are more specific than vacuolin-1.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Clinical relevance and patient data
- **Claim pointer** The authors claim that elevated expression of HOXA1, PITX2, MCOLN1, RAB3A, LGALS1, and IGFBP7 constitutes a prognostic signature correlating with poor outcomes in gastric cancer patients
- **Evidence pointer** Figure S10, location not provided
- **Concern** The clinical correlation data are only briefly mentioned and the supporting figure is in supplementary material. The manuscript does not describe the patient cohort, the number of samples, the statistical methods used for survival analysis, or whether the analysis was adjusted for confounding factors such as tumor stage and treatment. The claim of a "prognostic signature" implies a multivariate model, but no details of such a model are provided.
- **Why it matters** The translational significance of the findings depends on the robustness of the clinical correlation. Without adequate description of the patient cohort and statistical approach, the prognostic claim cannot be evaluated.
- **Resolution test** Provide full details of the patient cohort, including sample size, clinical characteristics, and follow-up. Describe the statistical methods for survival analysis, including multivariate adjustment. Show the prognostic value of the combined signature compared to individual markers.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** In vivo efficacy and dosing
- **Claim pointer** The authors claim that nortriptyline administration reduces tumor growth and metastasis in mouse models
- **Evidence pointer** Figure 8, location not provided
- **Concern** The in vivo experiments are described briefly without details on dosing regimen, route of administration, pharmacokinetics, or toxicity. The manuscript does not state whether the nortriptyline concentrations achieved in tumors are consistent with the in vitro effective concentrations. The specificity of the in vivo effect to the proposed mechanism is not addressed.
- **Why it matters** For a drug repurposing claim, the in vivo data need to be convincing with respect to dosing, tolerability, and mechanism. Without these details, the therapeutic potential cannot be properly assessed.
- **Resolution test** Provide full experimental details for in vivo studies, including dose, route, schedule, and tolerability. Measure drug levels in plasma and tumor tissue. Include a control group with a structurally related but inactive compound.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Nomenclature consistency
- **Affected element** Section heading
- **Evidence pointer** Results section 6, location not provided
- **Issue** The section heading reads "HOAX1/PITX2 Liquid Condensates Promote Gastric Cancer Progression Via Lysosomal Exocytosis" but the gene is referred to as HOXA1 elsewhere in the manuscript.
- **Required correction** Correct the typographical error in the section heading to read "HOXA1/PITX2".

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure legends and results text
- **Evidence pointer** Figures 1-8, location not provided
- **Issue** The manuscript frequently states statistical significance without reporting exact p-values, effect sizes, or the number of independent biological replicates. The statistical methods section is brief and does not describe how normality was assessed or which post-hoc tests were used for multiple comparisons.
- **Required correction** Provide exact p-values, effect sizes, and replicate numbers in figure legends. Expand the statistical analysis section to describe the specific tests used and any corrections for multiple testing.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data Availability Statement
- **Evidence pointer** Data Availability Statement, location not provided
- **Issue** The data availability statement indicates that data are available in supplementary material, but the RNA-seq dataset is deposited in GEO under GSE305469. The proteomics data do not appear to have a deposition identifier.
- **Required correction** Provide the accession number for the proteomics data and clarify which datasets are in GEO versus supplementary material.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Experimental detail
- **Affected element** Molecular docking section
- **Evidence pointer** Results section 7, location not provided
- **Issue** The molecular docking analysis is described with minimal detail. The software version, scoring function, and the criteria for selecting the binding pose are not stated. The reported binding energy is presented with an unusual format.
- **Required correction** Provide full details of the docking protocol, including software version, search parameters, and scoring function. Clarify the units and meaning of the reported score.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 5
- **Evidence pointer** Figure 5, location not provided
- **Issue** The manuscript describes fluorescence images showing puncta formation but does not include scale bars or quantification of puncta size, number, or distribution in the text description.
- **Required correction** Include scale bars in all microscopy images and provide quantitative analysis of puncta characteristics across conditions.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Author contribution
- **Affected element** Author Contributions section
- **Evidence pointer** Author Contributions, location not provided
- **Issue** The author contributions list W.J., X.L.W., J.Q., B.Z., and S.Z. as performing experiments but the corresponding author contributions for Q.T. and L.Z. are limited to writing. The specific contributions of each author are not fully delineated.
- **Required correction** Provide a more detailed breakdown of author contributions, including who performed the bioinformatics analyses, the in vivo studies, and the clinical data analysis.

- **Technical failings that need to be addressed before the case is established** The phase separation claim requires rigorous biophysical validation. The specificity of nortriptyline needs to be established through mutagenesis and appropriate controls. The causal link between lysosomal exocytosis of specific cargo proteins and tumor promotion needs direct experimental support. The clinical correlation data need full methodological transparency.

- **Assessment against Nature-style criteria** 
  - Originality: The connection between phase-separated transcription factor complexes and lysosomal exocytosis-mediated SASP is a novel angle. The drug repurposing approach for disrupting phase separation is creative. However, the individual components (HOXA1 in cancer, PITX2 in cancer, lysosomal exocytosis in SASP) have been previously studied.
  - Scientific importance: If fully substantiated, the findings could have implications for understanding SASP regulation and for therapeutic strategies targeting senescence in cancer. The potential clinical relevance is significant given the prognostic correlations and drug repurposing angle.
  - Interdisciplinary readership: The work spans cancer biology, senescence research, phase separation biophysics, and pharmacology. This breadth could attract readers from multiple communities, but the current presentation may not fully satisfy specialists in each area.
  - Technical soundness: The experimental approach is broad but the depth of validation for key claims is insufficient. The phase separation evidence is descriptive, the drug mechanism lacks specificity controls, and the in vivo data are presented without sufficient detail.
  - Readability for nonspecialists: The manuscript is generally well-organized and the logic is clear. However, some sections assume familiarity with phase separation concepts and the significance of specific experimental approaches may not be immediately apparent to a broad audience.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript presents an interesting hypothesis with preliminary supporting data, but several key claims require substantially stronger experimental validation. The phase separation mechanism, the specificity of nortriptyline, and the causal link between lysosomal exocytosis of specific cargo and tumor progression all need to be addressed. The clinical correlation data need more rigorous presentation. With these concerns addressed, the work could become a solid contribution to the field.

## Risk / unsupported claims
- The claim that HOXA1 and PITX2 form bona fide liquid-liquid phase separation condensates is not fully supported by the evidence presented
- The claim that nortriptyline specifically disrupts HOXA1-PITX2 phase separation as its primary mechanism of action is not established
- The claim that lysosomal exocytosis of LGALS1 and IGFBP7 is the causal mechanism driving tumor progression in this context is not directly demonstrated
- The prognostic signature claim is not adequately supported by the clinical data presentation
- The statement that "nortriptyline impedes gastric cancer progression by suppressing HOXA1-PITX2 phase separation" overstates the strength of the evidence
- The discussion of potential off-target effects of nortriptyline is acknowledged but not experimentally addressed