## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, and conclusion. Figures are referenced but not provided as images. Supplementary materials are mentioned but not accessible.
- **Assessment boundary** This review evaluates the scientific claims, methodological rigor, and evidentiary support based solely on the provided text. Figure content is assessed only through textual descriptions and legends. Statistical outputs are evaluated as reported without access to raw data.
- **Shared manuscript claim summary** The authors propose that WDR3 undergoes liquid-liquid phase separation (LLPS) and that this process mediates the therapeutic mechanism of Nilotinib against osteosarcoma. They identify five LLPS-related prognostic biomarkers through bioinformatics, validate WDR3 as a risk factor, demonstrate its phase separation behavior in vitro, and show that Nilotinib inhibits both osteosarcoma progression and WDR3 condensate formation.
- **Visible evidence base** Textual descriptions of bioinformatics analyses (differential expression, Cox regression, LASSO, consensus clustering, GSVA, CIBERTORT, TIDE/MSI, drug sensitivity), molecular docking results, qPCR and western blot validation, cell-based functional assays (CCK-8, Transwell), droplet formation assays, FRAP experiments, and in vivo xenograft studies with Nilotinib treatment.
- **Missing materials affecting confidence** Figure images are not available for independent verification of data quality. Supplementary tables (primer sequences, mutation details) and supplementary figures (pathway correlations, mutation schematics) are not accessible. Raw statistical outputs, exact n numbers for each experiment, and detailed animal data (individual tumor measurements, metastasis quantification methods) are not provided. No information on antibody validation or cell line authentication is given.

## Reviewer

- **Overall assessment** This manuscript addresses a potentially interesting connection between LLPS and drug response in osteosarcoma, with WDR3 as a novel candidate. The bioinformatics pipeline is reasonably standard, and the combination of in vitro and in vivo experiments is commendable. However, the central mechanistic claim that WDR3 phase separation specifically mediates Nilotinib's therapeutic effect is not convincingly established from the provided evidence. Several critical controls are missing, the causal link between WDR3 LLPS and osteosarcoma progression is correlative rather than demonstrated, and the specificity of Nilotinib's effect on WDR3 phase separation versus other mechanisms is unclear. The manuscript would benefit from substantial additional experimentation and more rigorous quantitative analysis.

- **Who would be interested in the results, and why** Researchers studying LLPS in cancer biology, particularly those interested in phase separation as a therapeutic target, would find this work relevant. The osteosarcoma community may be interested in the prognostic biomarker panel. Investigators working on drug repurposing or mechanism-of-action studies for tyrosine kinase inhibitors might also find the Nilotinib-WDR3 interaction noteworthy. However, the broad interdisciplinary appeal is limited by the relatively narrow focus and the preliminary nature of the mechanistic claims.

- **Major strengths** The study combines multiple approaches, including bioinformatics, molecular docking, cell biology, and animal models, which provides a multifaceted view of the problem. The identification of a five-gene prognostic signature with external validation is a solid contribution. The use of IDR mutation and rescue experiments to probe the role of phase separation is a thoughtful experimental design. The inclusion of both in vitro and in vivo data for Nilotinib treatment strengthens the translational relevance.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal mechanism
- **Claim pointer** The conclusion states that "WDR3 phase separation involves in the therapeutic mechanism of Nilotinib against osteosarcoma," implying a causal role for WDR3 LLPS in mediating Nilotinib efficacy.
- **Evidence pointer** Results sections "Phase separation of WDR3 expedited OS metastasis in vitro" and "Nilotinib mitigated osteosarcoma progression via inhibition of WDR3 phase separation"; Figures 5, 6, 7
- **Concern** The causal relationship between WDR3 phase separation and Nilotinib's therapeutic effect is not established. The experiments show that (a) WDR3 knockdown inhibits osteosarcoma phenotypes, (b) WDR3 can form phase-separated condensates, (c) IDR mutation disrupts condensates and reduces malignant phenotypes, and (d) Nilotinib reduces WDR3 condensates and inhibits tumor growth. However, these observations are correlative. The manuscript does not demonstrate that the anti-tumor effect of Nilotinib is specifically mediated through inhibition of WDR3 phase separation rather than through other known or unknown targets of Nilotinib. A critical experiment would be to test whether WDR3-MUT cells (which cannot phase separate) are still responsive to Nilotinib. If Nilotinib's effect is mediated through WDR3 LLPS, then cells with disrupted WDR3 phase separation should show reduced or abrogated response to Nilotinib. This experiment is not described.
- **Why it matters** The central claim of the manuscript is that WDR3 phase separation mediates Nilotinib's mechanism of action. Without demonstrating that the therapeutic effect depends on WDR3 LLPS, the conclusion overreaches the data. Nilotinib is a multi-target kinase inhibitor, and its effects on osteosarcoma could be mediated through numerous pathways independent of WDR3.
- **Resolution test** Perform Nilotinib treatment on U2-OS cells expressing WDR3-MUT (phase separation deficient) and compare the anti-proliferative, anti-migratory, and anti-invasive effects to WDR3-WT expressing cells. If WDR3 LLPS mediates Nilotinib efficacy, the mutant cells should show reduced sensitivity. Additionally, rescue experiments where WDR3 phase separation is restored (e.g., via hnRNPA1 IDR fusion) should restore Nilotinib sensitivity.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental rigor and controls
- **Claim pointer** The authors claim that "Nilotinib treatment significantly reduced the mRNA and protein expression levels of WDR3" and that this correlates with reduced phase separation.
- **Evidence pointer** Results section "Nilotinib mitigated osteosarcoma progression via inhibition of WDR3 phase separation"; Figures 6B-C, 6D-E
- **Concern** The mechanism by which Nilotinib reduces WDR3 expression is not explored. Is this a transcriptional effect, increased protein degradation, or a direct effect on phase separation stability? The manuscript does not distinguish between Nilotinib reducing WDR3 protein levels (which would secondarily reduce condensates) versus directly dissolving existing condensates. This distinction is critical for understanding the mechanism. Additionally, the concentration of Nilotinib used in vitro (5 µM) is relatively high, and the specificity of this concentration for WDR3-related effects versus general cytotoxicity is not addressed. No data on cell viability at the concentrations used for the phase separation experiments are shown, making it difficult to exclude non-specific effects.
- **Why it matters** Understanding whether Nilotinib acts on WDR3 expression or directly on condensate stability has different mechanistic implications. If Nilotinib reduces WDR3 transcription, the effect on phase separation is indirect. If it directly dissolves condensates, this would suggest a more specific biophysical interaction. The high concentration used raises concerns about off-target effects.
- **Resolution test** Perform time-course experiments to determine whether Nilotinib first reduces WDR3 protein levels before condensates disappear, or whether condensates dissolve before protein levels change. Use a broader range of Nilotinib concentrations with corresponding viability assays to establish specificity. Test whether Nilotinib can dissolve pre-formed WDR3 condensates in a cell-free system.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative rigor and statistical reporting
- **Claim pointer** The manuscript reports significant differences in cell viability, migration, invasion, tumor volume, tumor weight, and condensate numbers across multiple experimental conditions.
- **Evidence pointer** Results sections throughout; Figures 3, 5, 6, 7
- **Concern** The statistical methods are described only as "P < 0.05" and "P < 0.01" with asterisks in figure legends. No information is provided on the number of independent biological replicates, the number of technical replicates, the specific statistical tests used for each comparison, or whether assumptions for parametric tests were verified. For the animal experiments, only "n = 6" is stated, but it is unclear whether this refers to biological replicates (mice) or technical replicates. The method of randomization, blinding, and inclusion/exclusion criteria for animals are not described. The Transwell assay quantification is described as "three randomly selected fields," but the criteria for field selection and the number of independent experiments are not stated.
- **Why it matters** Without adequate statistical reporting, the reliability of the conclusions cannot be assessed. The lack of replicate information and test specification prevents readers from evaluating the robustness of the findings. This is particularly important for the in vivo experiments where variability can be substantial.
- **Resolution test** Provide complete statistical details for every figure: exact n values (biological and technical), the specific test used, and effect sizes with confidence intervals. For animal studies, include ARRIVE guidelines reporting. For cell-based assays, state the number of independent experiments and whether representative images or quantified data from all replicates are shown.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Specificity of WDR3 phase separation
- **Claim pointer** The authors state that "WDR3 undergoes phase separation" and that this is relevant to osteosarcoma biology.
- **Evidence pointer** Results section "WDR3 exhibited phase-separated condensates with liquid-like behavior in OS cells"; Figure 4
- **Concern** The evidence for phase separation relies on droplet formation in vitro and FRAP recovery. While these are standard assays, the manuscript does not demonstrate that WDR3 phase separation occurs endogenously in cells under physiological conditions. The immunofluorescence data show puncta, but it is not clear whether these represent bona fide phase-separated condensates or simply protein aggregates. No experiments using established LLPS inhibitors (e.g., 1,6-hexanediol) or genetic perturbations that specifically disrupt phase separation (beyond the IDR mutations) are shown. Additionally, the relevance of WDR3 phase separation to endogenous protein levels is not established, since the experiments rely heavily on overexpression.
- **Why it matters** The field of LLPS is rapidly evolving, and the criteria for demonstrating phase separation in cells are becoming more stringent. Overexpression artifacts are a known concern. Without evidence that endogenous WDR3 forms phase-separated condensates at physiological concentrations, the physiological relevance of the observed phenomenon is uncertain.
- **Resolution test** Perform endogenous immunofluorescence with validated antibodies and demonstrate that puncta are sensitive to 1,6-hexanediol treatment. Use CRISPR-mediated endogenous tagging to visualize WDR3 at native expression levels. Show that WDR3 condensates co-localize with known LLPS markers or are enriched in specific subcellular compartments relevant to its proposed function.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Clinical and translational relevance
- **Claim pointer** The authors conclude that WDR3 "may serve as a potent biomarker to ameliorate adverse events following osteosarcoma treatment."
- **Evidence pointer** Conclusion section; Discussion section
- **Concern** The clinical relevance of the findings is overstated. The study uses cell lines and xenograft models, but no patient-derived data are presented to support the claim that WDR3 expression or phase separation status correlates with clinical outcomes or treatment response. The bioinformatics analysis is based on public datasets, but the connection between WDR3 phase separation and patient prognosis is not directly examined. The claim that WDR3 could serve as a biomarker for treatment-related adverse events is not supported by any data in the manuscript.
- **Why it matters** The translational implications are a key selling point of the study. Without patient data or at least a clear correlation between WDR3 status and clinical parameters, the biomarker claim is speculative. This weakens the potential impact of the work.
- **Resolution test** Analyze WDR3 expression in osteosarcoma patient cohorts with treatment and outcome data. Correlate WDR3 expression or phase separation propensity with response to Nilotinib or other therapies. If patient samples are not available, clearly frame the biomarker claim as a hypothesis requiring future validation.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and terminology
- **Affected element** Title and abstract
- **Evidence pointer** Title; Abstract
- **Issue** The title states that WDR3 "undergoes phase separation to mediate the therapeutic mechanism of Nilotinib against osteosarcoma." This phrasing implies a causal mechanism that is not fully established. The abstract similarly states this as a finding rather than a hypothesis.
- **Required correction** Consider softening the title to reflect the correlative nature of the findings, such as "WDR3 phase separation is associated with the therapeutic response to Nilotinib in osteosarcoma." The abstract should also be revised to distinguish between demonstrated effects and proposed mechanisms.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Molecular docking methods
- **Evidence pointer** Methods section "Molecular docking"
- **Issue** The docking methodology is described briefly. No information is provided on the software version, scoring function, docking parameters, or how the binding pose was validated. The statement that "valid docking results were output if the binding energy was less than -5.0 kcal/mol" is a threshold, but the reliability of this threshold is not discussed.
- **Required correction** Provide full details of the docking protocol, including software versions, search algorithms, scoring functions, and any validation steps. Discuss the limitations of docking predictions and how the threshold was chosen.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure legends
- **Evidence pointer** Figures 1-7 legends
- **Issue** Figure legends are minimal and do not fully describe the experimental conditions, the number of replicates, or the statistical tests used. For example, Figure 3D-E does not specify the assay conditions or the time points for the proliferation and migration assays.
- **Required correction** Expand figure legends to include full experimental details, including cell densities, treatment durations, concentrations, and statistical information. This is essential for reproducibility.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion section
- **Evidence pointer** Discussion
- **Issue** The discussion of WDR3 function is limited. The authors mention its role in ribosome biogenesis and cancer, but the connection between these functions and phase separation is not explored in depth. The potential relationship between WDR3 phase separation and its known WD40 repeat domain structure is not discussed.
- **Required correction** Expand the discussion to address how WDR3's known biochemical functions might relate to its phase separation behavior. Discuss whether phase separation is a general property of WD40 repeat proteins or specific to WDR3.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Language and grammar
- **Affected element** Throughout
- **Evidence pointer** Multiple sections
- **Issue** There are several typographical and grammatical errors. For example, "anbtibody" in the immunofluorescence methods, "wrights" instead of "weights" in the animal methods, and "fold_change" in the DEG filtering criteria. The phrase "punctas per cell" in Figure 6D is awkward.
- **Required correction** Thorough proofreading is needed to correct typographical errors and improve language clarity.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Experimental design
- **Affected element** Cell line selection
- **Evidence pointer** Methods section "Cell culture and treatment"
- **Issue** Only U2-OS cells are used for the functional experiments. While the authors validate expression in HOS and MG-63, the functional studies are limited to a single cell line. This limits the generalizability of the findings.
- **Required correction** Include at least one additional osteosarcoma cell line for the key functional experiments, or justify why U2-OS is the most appropriate model.

- **Technical failings that need to be addressed before the case is established** R1-M1 (causal link between WDR3 phase separation and Nilotinib efficacy), R1-M2 (mechanism of Nilotinib action on WDR3), R1-M3 (inadequate statistical reporting), R1-M4 (lack of evidence for endogenous phase separation). These issues collectively prevent the manuscript from establishing its central claim.

- **Assessment against Nature-style criteria** 
  - Originality: Moderate. The application of LLPS concepts to osteosarcoma drug response is relatively novel, but the approach of identifying prognostic biomarkers through bioinformatics is well-established. The specific focus on WDR3 is new, but the conceptual framework is not groundbreaking.
  - Scientific importance: Moderate. If the causal mechanism were fully established, this could be important for understanding drug resistance in osteosarcoma. However, the current evidence is correlative, and the clinical relevance is speculative.
  - Interdisciplinary readership: Limited. The work sits at the intersection of cancer biology, biophysics, and pharmacology, but the narrow focus on a single gene and drug may limit broader appeal. The LLPS angle could attract biophysicists, but the depth of biophysical characterization is insufficient.
  - Technical soundness: The bioinformatics pipeline is standard and appears sound. The in vitro and in vivo experiments are appropriate but lack critical controls and quantitative rigor. The molecular docking is preliminary and not experimentally validated.
  - Readability for nonspecialists: The manuscript is generally readable, but the methods section is dense and assumes familiarity with multiple specialized techniques. The logical flow from bioinformatics to mechanistic studies is clear, but the causal claims outpace the evidence.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript addresses an interesting question and has a reasonable experimental framework, but the central mechanistic claim is not supported by the data as presented. The authors need to provide direct evidence that WDR3 phase separation is necessary and sufficient for Nilotinib's anti-tumor effects, improve statistical reporting, and address the specificity concerns. With substantial revision and additional experimentation, the manuscript could become a solid contribution to the field.

## Risk / unsupported claims
- The claim that WDR3 phase separation "mediates" the therapeutic mechanism of Nilotinib is unsupported. The data show correlation, not causation.
- The claim that WDR3 "may serve as a potent biomarker to ameliorate adverse events" is unsupported by any clinical or patient-derived data.
- The speculation that WDR3 phase separation is linked to SNRPB expression and lysosomal degradation pathways is presented without direct experimental evidence.
- The statement that Nilotinib "inhibiting the production of WDR3 phase-separated condensates" is the mechanism of action is not distinguished from general effects on WDR3 expression or cell viability.
- The molecular docking result showing WDR3-Nilotinib binding is not validated experimentally and should be treated as a prediction, not a demonstrated interaction.