## Review setup
- **Input scope** Full manuscript text (main text, figure legends not provided, supplementary figure legends not provided)
- **Assessment boundary** Scientific content, experimental logic, data interpretation, and claims as presented in the provided manuscript text. Statistical details, full figure panels, and supplementary data are not available for verification.
- **Shared manuscript claim summary** The authors identify two previously uncharacterized intrinsically disordered proteins, SAID1/2, as interaction partners of SERRATE (SE) in Arabidopsis. They propose that SAID1/2 inhibit miRNA biogenesis through a dual mechanism: (1) sequestering pri-miRNAs from SE via high-affinity binding, and (2) promoting SE phosphorylation and degradation via PRP4KA. They further propose that these events occur in nuclear condensates formed by SAID1/2 on SE.
- **Visible evidence base** Main text results sections, figure callouts (Figs. 1-6), SI Appendix figure callouts, methods summaries, RNA-seq and sRNA-seq data descriptions.
- **Missing materials affecting assessment confidence** Full figure panels and legends, SI Appendix figures and legends, Dataset S1 A-D contents, detailed statistical analyses, primer and vector lists, raw sequencing data, detailed methods for RNA-seq/sRNA-seq analysis, and the complete Materials and Methods section.

## Reviewer

- **Overall assessment** This manuscript presents a potentially interesting finding that two previously uncharacterized IDPs, SAID1/2, act as negative regulators of miRNA biogenesis in Arabidopsis through interaction with SE. The work combines genetics, biochemistry, cell biology, and transcriptomics to build a case for a dual-inhibition model. However, several key claims are not fully supported by the evidence presented in the text, and important controls and quantitative analyses are missing. The mechanistic model, while attractive, relies on correlative data and in vitro experiments that may not fully recapitulate in vivo conditions. The manuscript would benefit from additional experiments to strengthen the causal links between SAID1/2 condensation, SE phosphorylation, and miRNA suppression.

- **Who would be interested in the results, and why** Plant molecular biologists studying miRNA biogenesis, RNA metabolism, and gene regulation will find this work relevant. Researchers interested in intrinsically disordered proteins and their roles in cellular condensates and phase separation will also be interested, as this study provides a plant example of IDP-mediated regulation of a core RNA processing factor. The potential connection to DSPP-like proteins in metazoans may attract broader interest from researchers studying RNA silencing across kingdoms.

- **Major strengths**
  1. The identification and functional characterization of two previously unannotated genes (SAID1/2) addresses a clear gap in Arabidopsis functional genomics.
  2. The dual-inhibition model (pri-miRNA sequestration + promotion of SE degradation) is conceptually novel and provides a new framework for understanding miRNA biogenesis regulation.
  3. The combination of genetic, biochemical, and cell biological approaches is commendable.
  4. The observation that SAID1/2 condensate on SE in an SE-dependent manner is interesting and potentially significant for understanding spatial regulation of miRNA processing.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength for in vivo mechanism
- **Claim pointer** "SAID1/2 act to hijack pri-miRNAs from SE and inhibit microprocessor activity, whereas promoting phosphorylation and degradation of SE protein, leading to repression of production for a majority of miRNAs."
- **Evidence pointer** Figures 3, 4, 5; Discussion section
- **Concern** The claim that SAID1/2 "hijack" pri-miRNAs from SE in vivo is primarily supported by in vitro EMSA competition experiments (Fig. 4H). The in vivo RIP assay (Fig. 4G) shows that SAID1/2 associate with pri-miRNAs, but does not demonstrate that they displace SE from pri-miRNAs. The authors do not provide evidence for a ternary complex versus mutually exclusive binding in vivo, nor do they show that SAID1/2 overexpression or knockout alters the SE-pri-miRNA interaction in planta. The in vitro microprocessor assays (Fig. 5) show inhibition of processing, but the physiological relevance of the protein concentrations used is unclear.
- **Why it matters** The "hijacking" model is central to the proposed mechanism. Without direct in vivo evidence that SAID1/2 displace SE from pri-miRNAs, the model remains speculative. Alternative explanations, such as SAID1/2 simply competing with DCL1/HYL1 for substrate access or acting as general RNA sponges, are not excluded.
- **Resolution test** Perform RNA immunoprecipitation (RIP) followed by quantitative PCR in plants expressing tagged SE in wild-type versus said1/2 mutant backgrounds to show that SE-pri-miRNA association increases in the absence of SAID1/2. Alternatively, use a competitive EMSA with purified SE, SAID1/2, and pri-miRNA at physiologically relevant concentrations to demonstrate displacement. A crosslinking-based approach (e.g., CLIP) could also distinguish direct versus indirect binding.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal relationship between SE phosphorylation and degradation
- **Claim pointer** "SAID1/2 promote degradation and phosphorylation of SE" and "SAID1/2 could promote SE phosphorylation via PRP4KA and facilitate its degradation."
- **Evidence pointer** Figure 3A-D; SI Appendix Figures S5, S6
- **Concern** The text states that SE protein levels are increased in said1/2 mutants and that SE is hypo-phosphorylated, but the causal link between phosphorylation status and protein stability is not directly established. The cell-free decay assay (Fig. 3B-C) shows that SE is more stable in said1/2 extracts, but does not demonstrate that this stability difference is due to altered phosphorylation. The in vitro kinase assays (Fig. 3E-H) show that SAID1/2 can enhance PRP4KA-mediated phosphorylation of SE, but the relevance of the protein concentrations used and whether this occurs in vivo is not shown. The authors do not test whether a phospho-dead or phospho-mimetic SE mutant rescues the said1/2 phenotype.
- **Why it matters** The model proposes that SAID1/2 promote SE degradation through enhanced phosphorylation. Without direct evidence that phosphorylation triggers SE degradation, the connection between these two observations is correlative. The authors themselves note that SAID1/2 might have "additional regulatory roles," which weakens the specificity of the proposed mechanism.
- **Resolution test** Express phospho-dead (Ser/Thr to Ala) or phospho-mimetic (Ser/Thr to Asp/Glu) versions of SE in the said1/2 mutant background and test whether they rescue the miRNA accumulation phenotype. Alternatively, use a proteasome inhibitor in the cell-free decay assay to show that the SAID1/2-dependent degradation is proteasome-mediated and phosphorylation-dependent. Mass spectrometry to identify SAID1/2-dependent phosphorylation sites on SE would also strengthen the model.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative analysis of miRNA and pri-miRNA changes
- **Claim pointer** "SAID1/2 Reduce Accumulation of a Majority of miRNAs In Vivo" and "the general inverse accumulation between pri-miRNA debris and miRNAs suggested possible efficient processing of pri-miRNAs in said1-3; said2-3."
- **Evidence pointer** Figure 2H-L; SI Appendix Figure S4
- **Concern** The manuscript reports that approximately 110 miRNAs are upregulated and fewer than 50 are downregulated in said1-3; said2-3, but the total number of miRNAs analyzed, the criteria for significance, and the magnitude of fold changes are not stated in the text. The statement that "a majority of miRNAs" are affected is not quantified. The pri-miRNA analysis is limited to 22 selected loci, and the authors acknowledge that RNA-seq reads for pri-miRNA debris were too low for rigorous differential expression analysis. The RT-qPCR data for pri-miRNAs (SI Appendix Fig. S4H) show significant reduction for 15 of 22 tested, but the correlation between pri-miRNA reduction and miRNA increase is not systematically analyzed.
- **Why it matters** The claim that SAID1/2 regulate "a majority of miRNAs" is a strong statement that requires quantitative support. If only a subset of miRNAs is affected, the model may need refinement. The inverse correlation between pri-miRNA and mature miRNA levels is suggestive but not definitive evidence for processing enhancement.
- **Resolution test** Provide a complete list of differentially expressed miRNAs with fold changes and adjusted p-values. Perform a correlation analysis between pri-miRNA and mature miRNA changes across all affected loci. Use a global run-on or metabolic labeling approach to directly measure pri-miRNA processing rates in wild-type versus said1/2 mutants.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Functional significance of condensation
- **Claim pointer** "These biochemical events likely take place in SAID1/2-SE condensates in vivo" and "SAID1/2 nucleate on SE to form condensates, which in turn promote SE degradation or deprive pri-miRNAs from SE."
- **Evidence pointer** Figure 6; SI Appendix Figures S9-S13
- **Concern** The manuscript shows that SAID1/2 and SE can form nuclear condensates when overexpressed, and that endogenous SAID1/2 condensates are reduced in se mutants. However, the functional significance of these condensates for miRNA biogenesis is not directly tested. The authors do not show that disrupting condensation (e.g., via IDR mutations that abolish condensate formation) affects miRNA levels. The FRAP experiments demonstrate phase separation behavior, but the relationship between condensate formation and the biochemical activities (pri-miRNA sequestration, SE phosphorylation) is not established.
- **Why it matters** The condensation model is a major conceptual contribution of this work. Without functional evidence linking condensate formation to miRNA regulation, the physiological relevance of the observed phase separation remains unclear. The authors themselves note that SE-GFP is "distributed homogenously in nucleus" under native expression, raising questions about whether condensates are the physiologically relevant sites of action.
- **Resolution test** Generate SAID1/2 mutants that cannot form condensates (e.g., IDR deletions that abolish phase separation but retain SE binding) and test whether they still repress miRNA accumulation. Alternatively, use an optogenetic approach to induce or disrupt condensate formation and measure effects on pri-miRNA processing.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Specificity of SAID1/2 function
- **Claim pointer** "SAID1/2 are bona fide partners of SE protein" and "SAID1/2 represent a unique mode of action of controlling SE function."
- **Evidence pointer** Figure 1; SI Appendix Figure S1
- **Concern** The manuscript demonstrates that SAID1/2 interact with SE, but the specificity of this interaction is not fully addressed. The authors show that SAID1/2 do not interact with DCL1 or HYL1 in Y2H assays, but they do not test whether SAID1/2 interact with other components of the miRNA pathway or with other SE-containing complexes. The observation that SAID1/2 have "interdependent and independent regulatory roles" in gene expression suggests that their function may not be limited to SE regulation. The physiological relevance of the SAID1/2-SE interaction is not tested through complementation experiments with interaction-defective mutants.
- **Why it matters** If SAID1/2 have functions beyond SE regulation, the interpretation of the miRNA phenotypes becomes more complex. The claim of a "unique mode of action" requires evidence that the effects on miRNA biogenesis are specifically mediated through the SAID1/2-SE interaction.
- **Resolution test** Perform genetic epistasis analysis by expressing SAID1/2 variants that cannot bind SE in the said1/2 mutant background and testing whether they rescue the miRNA phenotype. Use co-immunoprecipitation followed by mass spectrometry to identify the full interactome of SAID1/2 and assess whether SE is the predominant partner.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 2A-C
- **Evidence pointer** Figure 2A-C
- **Issue** The Venn diagram and heatmap presentations of DEGs are described but the actual numbers in each category are not clearly stated in the text. The overlap statistics between said1/2 and se mutants are not quantified.
- **Required correction** Provide explicit numbers for DEG overlaps and non-overlaps in the text or figure legend, and include a statistical test for overlap significance.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Experimental detail
- **Affected element** CRISPR-Cas9 knockout generation
- **Evidence pointer** Materials and Methods, Plant Materials
- **Issue** The text states that CRISPR-Cas9 knockout lines were generated but does not specify the number of independent lines, the guide RNA sequences, or the nature of the mutations (frameshift, deletion, etc.) for the lines used in phenotypic and molecular analyses.
- **Required correction** Include guide RNA target sequences, mutation details for each line, and the number of independent lines analyzed in the Materials and Methods or SI Appendix.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 2K-M, Figure 3A-D
- **Evidence pointer** Figure 2K-M, Figure 3A-D
- **Issue** The text describes differences in miRNA accumulation and protein levels between genotypes but does not report the number of biological replicates, error bars, or statistical tests used for these comparisons.
- **Required correction** Add statistical information to figure legends, including n values, error bar definitions, and p-values with the specific tests used.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data interpretation
- **Affected element** Figure 3I-J
- **Evidence pointer** Figure 3I-J
- **Issue** The SEC analysis shows comparable elution profiles between wild-type and said1/2 mutants, which the authors interpret as indicating that "assembly of SE-scaffolded macrocomplexes is not altered." However, the resolution of SEC may not be sufficient to detect subtle changes in complex composition.
- **Required correction** Acknowledge the limitation of SEC resolution and consider complementary approaches (e.g., native PAGE, crosslinking) to strengthen this conclusion.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Model clarity
- **Affected element** Figure 6F
- **Evidence pointer** Figure 6F
- **Issue** The model diagram is described but not shown in the text. The relationship between the two proposed inhibitory mechanisms (sequestration and degradation) and their temporal or spatial coordination is not clearly explained.
- **Required correction** Provide a more detailed description of the model in the text, including whether the two mechanisms are proposed to act simultaneously, sequentially, or under different conditions.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion of SAID1/2 as IDPs that regulate SE function would benefit from comparison with other known IDP regulators of RNA processing factors in plants and animals. The authors mention CARP9 but do not discuss other examples of IDP-mediated regulation of miRNA biogenesis.
- **Required correction** Add a brief paragraph contextualizing SAID1/2 within the broader literature on IDPs in RNA metabolism and phase-separated regulation of gene expression.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data, Materials, and Software Availability
- **Evidence pointer** Data, Materials, and Software Availability section
- **Issue** The RNA-seq and sRNA-seq data are deposited in SRA under PRJNA938906, but the authors do not state whether the analysis code or pipelines are publicly available.
- **Required correction** Provide information on code availability or state that analysis code is available upon request.

## Risk / unsupported claims
1. The claim that SAID1/2 "hijack" pri-miRNAs from SE in vivo is not directly supported by the presented data. In vitro EMSA competition experiments (Fig. 4H) suggest this possibility, but in vivo evidence is lacking.
2. The claim that SAID1/2 promote SE degradation through enhanced phosphorylation is correlative. The cell-free decay assay shows increased SE stability in said1/2 extracts, and the in vitro kinase assay shows SAID1/2 can enhance PRP4KA activity, but the causal link between these observations is not established.
3. The statement that "these biochemical events likely take place in SAID1/2-SE condensates in vivo" is speculative. The manuscript does not provide functional evidence that condensation is required for the proposed biochemical activities.
4. The claim that SAID1/2 regulate "a majority of miRNAs" is not quantitatively supported in the text. The number of affected miRNAs relative to the total analyzed and the magnitude of changes are not stated.
5. The assertion that SAID1/2 and SE have "interdependent and independent regulatory roles" is based on DEG overlap analysis, but the functional significance of the non-overlapping DEGs is not explored.
6. The statement that SAID1/2 are "hypothetic dentin sialophosphoprotein-like proteins" and the speculation about DSPP function in metazoans is not experimentally tested and should be clearly labeled as speculation.
7. The claim that SAID1/2 "represent a unique mode of action" is not fully supported, as the authors do not comprehensively compare their mechanism with all known regulators of miRNA biogenesis.
8. The text states that "the inhibition might be even more severe" when SE is preincubated with pri-miRNA before SAID1/2 addition (SI Appendix Fig. S8E-F), but this observation is not quantified or statistically tested.

## Assessment against Nature-style criteria
- **Originality** The identification of SAID1/2 as novel negative regulators of miRNA biogenesis through a dual mechanism is original. The finding that IDPs can regulate SE function through both substrate sequestration and promotion of degradation represents a new concept in plant miRNA biology. However, the individual components of the model (IDP-mediated regulation, condensate formation, phosphorylation-dependent degradation) have been described in other systems.
- **Scientific importance** The work addresses a significant gap in understanding how miRNA biogenesis is negatively regulated in plants. The identification of two previously uncharacterized genes with clear functions in miRNA regulation is valuable. The potential connection to DSPP-like proteins in metazoans could have broader implications, though this remains speculative.
- **Interdisciplinary readership** The work will primarily interest plant molecular biologists and RNA biologists. The IDP/condensate angle may attract cell biologists studying phase separation, but the plant-specific context may limit broader appeal. The significance statement is accessible, but the results section requires specialized knowledge.
- **Technical soundness** The experimental approaches are generally appropriate and well-executed. However, several key claims lack direct in vivo evidence, particularly the hijacking model and the causal link between phosphorylation and degradation. The quantitative analysis of miRNA changes is incomplete. The in vitro experiments may not fully recapitulate physiological conditions.
- **Readability for nonspecialists** The significance statement is clear and accessible. The results section is dense but logically organized. The discussion effectively contextualizes the findings. However, the manuscript assumes significant background knowledge of miRNA biogenesis and Arabidopsis genetics.

## Recommendation posture
**Supportive if technical concerns are resolved.** The core finding that SAID1/2 are novel negative regulators of miRNA biogenesis is potentially significant and of interest to the plant RNA biology community. However, the central mechanistic claims (hijacking of pri-miRNAs, phosphorylation-dependent degradation, functional significance of condensates) require additional experimental support. The manuscript would be strengthened by: (1) in vivo evidence for the hijacking model, (2) direct demonstration that SAID1/2-dependent phosphorylation leads to SE degradation, (3) functional tests of condensation in miRNA regulation, and (4) complete quantitative analysis of miRNA changes. With these additions, the manuscript could make a strong contribution to the field.