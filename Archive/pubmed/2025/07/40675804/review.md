## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods) without figures, tables, or supplementary materials
- **Assessment boundary** Scientific content, experimental logic, structural claims, and consistency between stated results and conclusions; no assessment of figures, statistical outputs, or primary data quality beyond what is described in text
- **Shared manuscript claim summary** The authors report a cryo-EM structure of human PRMT1 as a helical polymer, identify interface residues controlling oligomerization, and propose that oligomerization enhances binding and methylation of RGG-motif-containing RNA-binding proteins, thereby promoting pancreatic ductal adenocarcinoma (PDAC) growth through RNA metabolism regulation
- **Visible evidence base** Text descriptions of cryo-EM reconstruction (3.68 Å), SEC profiles, negative stain EM, co-immunoprecipitation, in vitro pull-downs, in vitro methylation assays, CRISPR knockout/rescue in HeLa and PDAC cell lines, proliferation and colony formation assays, xenograft tumor growth, LC-MS/MS proteomics, RNA-seq, RT-qPCR validation, and GO pathway analysis
- **Missing materials affecting confidence** All figures and supplementary figures; Table 1 (cryo-EM data collection statistics); exact quantification and statistical outputs; proteomics and RNA-seq differential analysis details; shRNA target sequences and validation data; details of the "Picker" and "helixPick" software validation; uncropped Western blots; tumor growth curves with individual data points; details on how "comparable expression" of rescue constructs was verified

## Reviewer
- **Overall assessment** This manuscript addresses a significant and timely question: whether PRMT1 oligomerization beyond the dimer state confers distinct functional properties relevant to cancer. The cryo-EM structure of human PRMT1 as a helical polymer is a valuable contribution, and the authors provide a systematic mutational strategy to separate dimeric and oligomeric functions. However, the manuscript as presented has several critical gaps. The central mechanistic claim that oligomerization enhances substrate binding and methylation of RGG-containing RBPs is supported by in vitro binding and cellular co-immunoprecipitation data, but the enzymatic activity comparison between oligomer and dimer is described as showing "nearly identical activity" in vitro, which appears to contradict the cellular data. The link between oligomerization-dependent methylation changes and the specific RNA metabolism alterations that drive PDAC growth remains correlative. The RNA-seq and proteomics analyses are described at a level that does not allow assessment of robustness, and the connection between the 112 oligomer-state-correlated genes and the 36 differentially enriched proteins is not explicitly established. The in vivo xenograft data are described but key controls and quantitative details are missing. The discussion of the concurrent study by Dang et al. is appropriate but highlights the need for clearer differentiation of novel contributions. Overall, the structural findings are likely solid, but the functional and mechanistic conclusions require substantially more evidence and clearer presentation to be convincing.

- **Who would be interested in the results, and why** Structural biologists studying PRMT family oligomerization and protein arginine methylation; cancer biologists investigating epigenetic and post-translational regulation in pancreatic cancer; researchers studying RNA-binding proteins and RNA metabolism in malignancy; drug developers interested in targeting PRMT1 oligomeric interfaces as a therapeutic strategy in PDAC.

- **Major strengths** 1) The cryo-EM structure of human PRMT1 as a helical polymer is a novel and significant structural contribution, addressing a gap between known dimeric crystal structures and observed higher-order species in solution. 2) The systematic generation of interface-specific mutants (dimer versus monomer) provides a clean experimental strategy to dissect the functional contributions of oligomerization. 3) The combination of structural, biochemical, cellular, and in vivo approaches is comprehensive. 4) The focus on full-length RGG-containing RBPs rather than peptides is a strength for physiological relevance. 5) The acknowledgment and contextualization of the concurrent study by Dang et al. is appropriate.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim-evidence alignment
- **Claim pointer** "Oligomerization enhances the enzymatic activity of PRMT1 toward substrates containing RGG motifs" (Results section heading and associated text)
- **Evidence pointer** Results section "Oligomerization enhances the enzymatic activity of PRMT1 toward substrates containing RGG motifs"; Figure S5A–D (described in text)
- **Concern** The text states that "PRMT1oligomer and PRMT1dimer exhibited nearly identical activity with histone H4, hnRNPA1, and fibrillarin under our experimental conditions" in the in vitro methylation assay. This directly contradicts the section heading and the overall thesis that oligomerization enhances enzymatic activity. The authors then pivot to cellular assays showing differences in ADMA levels, but the in vitro result undermines the mechanistic claim that enhanced activity is due to oligomerization per se. The discrepancy is not adequately explained. Possible explanations such as substrate concentration effects, assay conditions, or the possibility that the cellular differences are due to binding/recruitment rather than catalytic rate are not discussed.
- **Why it matters** The central mechanistic claim of the paper is that oligomerization enhances PRMT1 activity toward RGG substrates. If the in vitro enzymatic activity is identical between oligomer and dimer, the mechanism by which oligomerization promotes methylation in cells is unclear. This is a fundamental inconsistency that affects the interpretation of all downstream functional data.
- **Resolution test** The authors must either (a) provide in vitro conditions under which oligomerization enhances catalytic activity toward RGG substrates, (b) clearly demonstrate that the cellular differences are due to enhanced binding/recruitment rather than catalytic rate, or (c) revise the mechanistic model to reflect that oligomerization affects substrate binding and methylation indirectly through other factors present in cells. Direct comparison of kinetic parameters (kcat, Km) for oligomer versus dimer toward RGG substrates would be informative.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency for in vivo relevance
- **Claim pointer** "PRMT1 oligomerization regulates RNA-binding protein cascade to promote pancreatic cancer" (title); "disruption of PRMT1 oligomerization inhibits PDAC tumor growth through affecting RNA metabolism" (Results section)
- **Evidence pointer** Results section "Disruption of PRMT1 oligomerization inhibits PDAC tumor growth through affecting RNA metabolism"; Figures 6 and 7 (described in text); Figure S8A–G
- **Concern** The causal link between oligomerization-dependent methylation of RBPs and PDAC growth is not established. The proteomics identified 36 proteins differentially enriched in the oligomer state, and RNA-seq identified 112 genes correlated with oligomerization state. However, the manuscript does not demonstrate that any specific RBP's methylation status is altered in a way that directly affects its function in RNA metabolism, nor that these changes are causally responsible for the observed growth phenotypes. The overlap between the 36 proteins and the 112 genes is not reported. The RT-qPCR validation of 7 genes is described but the functional significance of these specific genes is not explored. The xenograft data show growth differences but do not establish the mechanism.
- **Why it matters** The title and central conclusion claim a specific mechanism: oligomerization regulates an RBP cascade that promotes PDAC. Without demonstrating that (a) specific RBPs have altered methylation, (b) this altered methylation changes their RNA-related functions, and (c) these functional changes drive proliferation, the mechanistic claim is not supported. The current data support a correlation between oligomerization state and growth, but not the proposed cascade mechanism.
- **Resolution test** The authors should identify specific RBP substrates whose methylation is altered by oligomerization state in PDAC cells, demonstrate functional consequences (e.g., changes in RNA binding, splicing, or stability of specific target RNAs), and show that these changes are necessary for the growth phenotype. At minimum, the overlap between proteomics and transcriptomics datasets should be analyzed and presented.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Structural interpretation and validation
- **Claim pointer** "PRMT1 forms functional helical oligomers" and "the cryo-EM structure of human PRMT1, which adopts a homo-oligomeric architecture featuring a novel helical polymer"
- **Evidence pointer** Results section "Cryo-EM structure of the human PRMT1 helical polymer"; Figures 1 and 2 (described in text); Table 1 (not visible)
- **Concern** The cryo-EM reconstruction is reported at 3.68 Å resolution, but the manuscript does not provide sufficient detail on map quality, model validation, or how the helical symmetry was determined and verified. The authors mention a "program developed by the author" for helical symmetry estimation, but no validation of this program is provided. The local resolution is stated to be "sufficient to determine" the repeating unit, but the criteria for this determination are not specified. The manuscript also does not describe how the model was built, refined, and validated (e.g., MolProbity scores, Ramachandran statistics, map-model correlation).
- **Why it matters** The structural claim is foundational to the entire paper. Without adequate validation of the cryo-EM structure and the helical symmetry determination, the structural basis for the functional claims is not established. The use of an in-house program without validation is a particular concern.
- **Resolution test** Provide full cryo-EM data collection and refinement statistics (Table 1), including Fourier shell correlation curves, model validation metrics, and a description of how helical symmetry was determined and cross-validated. If the in-house program is used, provide benchmarks against established methods or independent validation.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative rigor and statistical reporting
- **Claim pointer** "Substantial tumor growth inhibition was observed over 21 d" and "PRMT1 depletion significantly inhibited proliferation" and "marked changes in peptide abundance"
- **Evidence pointer** Results sections on PDAC growth and proteomics; Figures 6 and 7 (described in text); Materials and Methods "Quantification and statistical analysis"
- **Concern** The manuscript describes statistical methods (one-way and two-way ANOVA with Tukey's tests) but does not report exact p-values, effect sizes, sample sizes (n), or the number of independent biological replicates for most experiments. The tumor xenograft experiment is described as having "substantial" growth inhibition but no quantitative data (tumor volumes over time, final weights, statistical comparisons) are provided in the text. The proteomics analysis reports "marked changes in peptide abundance" without specifying the threshold for differential enrichment, the statistical test used, or the false discovery rate control. The RNA-seq analysis criteria are stated (|Log2FC| ≥ 1.5, p < 0.05) but the number of replicates and the differential expression analysis method are not described.
- **Why it matters** The conclusions rely heavily on quantitative comparisons between oligomer, dimer, and monomer states. Without proper reporting of sample sizes, effect sizes, and statistical details, the robustness of these conclusions cannot be assessed. This is particularly important for the in vivo data, which are central to the translational relevance claim.
- **Resolution test** Provide complete statistical reporting for all experiments, including exact p-values, n numbers, and effect sizes. For the xenograft study, provide tumor growth curves with individual data points and statistical comparisons at each time point. For proteomics and RNA-seq, provide details on the analysis pipeline, thresholds, and multiple testing correction.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Specificity of oligomerization effects
- **Claim pointer** "PRMT1 oligomerization regulates RNA-binding protein cascade" and "PRMT1 and PRMT8 displayed notably higher affinities for RGG-rich substrates compared with other PRMT family members"
- **Evidence pointer** Results sections on substrate binding and family comparison; Figure S4G–J (described in text)
- **Concern** The manuscript does not address whether the effects of oligomerization on substrate binding are specific to RGG-containing substrates or represent a general avidity effect that would apply to any multivalent substrate. The comparison with other PRMT family members is described but the basis for this comparison (e.g., whether other PRMTs were tested in the same oligomeric states) is unclear. Additionally, the physiological relevance of the helical polymer is not directly demonstrated; the authors show that endogenous PRMT1 elutes at high molecular weight, but whether this represents the same helical polymer observed in vitro is not established.
- **Why it matters** The specificity of the oligomerization effect is central to the proposed model. If oligomerization enhances binding to all substrates non-specifically, the model would need to be revised. The claim that this mechanism is specific to RGG-containing RBPs requires direct evidence.
- **Resolution test** Test whether oligomerization enhances binding to non-RGG substrates or to substrates with fewer RGG repeats. Provide a more detailed comparison of PRMT family members under matched conditions. Use cross-linking or other methods to demonstrate that the endogenous high-molecular-weight species corresponds to the helical polymer.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and terminology
- **Affected element** Nomenclature of PRMT1 variants
- **Evidence pointer** Results section "Multiple types of contacts stabilize the PRMT1 dimer"
- **Issue** The text introduces "PRMT1WT" and then refers to "PRMT1Oligomer," "PRMT1Dimer," and "PRMT1Monomer." The relationship between "PRMT1WT" and "PRMT1Oligomer" is stated but the terminology is potentially confusing, especially since "WT" could be interpreted as the native sequence regardless of oligomeric state.
- **Required correction** Clarify the nomenclature early in the results, perhaps with a table or schematic, and consistently use the defined terms throughout. Consider whether "PRMT1WT" is needed at all if "PRMT1Oligomer" is the wild-type sequence.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Cryo-EM data processing
- **Evidence pointer** Materials and Methods "Data processing"
- **Issue** The description of cryo-EM data processing is brief and does not mention key steps such as particle picking strategy, 2D/3D classification details, refinement procedures, or resolution assessment. The use of "laboratory-made programs" (mrcReference, Picker, helixPick) is mentioned but these are not described or validated.
- **Required correction** Expand the data processing section to include standard cryo-EM workflow details and provide validation for any in-house software, or deposit the software with documentation.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Proteomics and RNA-seq results
- **Evidence pointer** Results section "Disruption of PRMT1 oligomerization inhibits PDAC tumor growth through affecting RNA metabolism"; Figures 7 (described in text)
- **Issue** The proteomics and RNA-seq results are described in aggregate terms ("marked changes," "112 genes closely correlated") without presenting specific examples of affected genes or proteins. The heat map (Figure 7G) is mentioned but its content is not described in the text.
- **Required correction** Provide specific examples of differentially enriched proteins and differentially expressed genes, with their identities and functional annotations, to give the reader a concrete sense of the biological pathways affected.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion
- **Issue** The discussion of the concurrent study by Dang et al. is brief and does not fully contextualize how the two studies complement or differ beyond the stated differences in mutant strategy and focus on PDAC. The broader literature on PRMT1 oligomerization is not discussed in depth.
- **Required correction** Expand the discussion to more thoroughly compare and contrast with Dang et al. and to place the findings in the context of other studies on PRMT oligomerization and substrate recognition.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure callouts
- **Affected element** Results text
- **Evidence pointer** Throughout Results
- **Issue** Several figure callouts are to supplementary figures (e.g., Figure S1A, S3A–F, S4A–J, S5A–D, S6A–G, S7A–F, S8A–G) without corresponding main figure callouts for key data. This makes it difficult for the reader to follow the main narrative without constantly referring to supplementary material.
- **Required correction** Consider moving at least one representative example of each key experiment (structure, binding, methylation, growth) to a main figure, or restructure the text to better guide the reader through the supplementary figures.

## Risk / unsupported claims
- The claim that oligomerization "enhances enzymatic activity" is not supported by the in vitro data described, which show nearly identical activity between oligomer and dimer.
- The claim that PRMT1 oligomerization regulates an "RNA-binding protein cascade" is not directly demonstrated; the data show differential binding and methylation of RBPs, but the downstream functional consequences on RNA metabolism are inferred rather than shown.
- The claim that the helical polymer is the physiologically relevant form in cells is not directly demonstrated; the high-molecular-weight species observed by SEC could represent other complexes.
- The claim that targeting PRMT1 oligomeric forms has therapeutic potential in PDAC is speculative, as no pharmacological or genetic evidence for therapeutic efficacy of disrupting oligomerization is presented.
- The specificity of the oligomerization effect for RGG-containing substrates over other substrates is not established.
- The overlap and functional relationship between the 36 differentially enriched proteins (proteomics) and the 112 oligomerization-correlated genes (RNA-seq) is not reported, leaving the mechanistic link between these datasets unexamined.