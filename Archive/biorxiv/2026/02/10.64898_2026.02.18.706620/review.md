## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and supplementary figure legends
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and technical soundness as presented in the provided text
- **Shared manuscript claim summary** The authors propose that ARGONAUTE10 (AGO10) functions as a specialized, immune-responsive Argonaute that enables trans-species RNA interference (tsRNAi) in plant immunity. They report that AGO10 is required for pathogen-induced silencing of pathogen genes, that its protein levels and localization respond to immune activation, that it associates with SGS3 in cytoplasmic condensates, and that this immune-responsive function is dependent on an N-terminal intrinsically disordered region (IDR). They further propose that this function is evolutionarily conserved in the AGO10a subclade.
- **Visible evidence base** Results sections describing mutant screens, pathogen infection assays, protein localization studies, co-immunoprecipitation, small RNA sequencing, structural prediction, and phylogenetic analyses; supplementary figure legends describing supporting data
- **Missing materials affecting confidence** Actual figures and supplementary figures are not provided; numerical data, statistical details, and raw sequencing outputs are not accessible; full methods for several key experiments are abbreviated; no information on replicates for several experiments beyond stated numbers

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question in plant immunity: whether trans-species RNAi is an endogenously regulated immune response. The identification of AGO10 as a specialized Argonaute with immune-responsive behavior is potentially significant. However, several key claims are not fully supported by the evidence as presented. The mechanistic link between AGO10 catalytic activity, SGS3 interaction, and tsRNAi production requires stronger experimental support. The evolutionary conservation claim is based on limited phylogenetic and functional data. The manuscript would benefit from additional experiments and clearer presentation of quantitative data.

- **Who would be interested in the results, and why** Plant pathologists studying innate immunity and small RNA biology would be the primary audience. Researchers working on Argonaute protein functional diversification, RNA silencing mechanisms, and host-induced gene silencing for crop protection would also find these results relevant. The potential translational implications for engineering tsRNAi-based disease resistance in crops would interest the broader plant biotechnology community.

- **Major strengths** The study addresses a fundamental question about whether tsRNAi is a regulated immune response. The identification of AGO10 as a specific Argonaute involved in this process is novel. The combination of genetic, cell biological, and biochemical approaches is commendable. The finding that AGO10 responds to immune activation at the post-transcriptional level and relocalizes to cytoplasmic condensates is intriguing. The evolutionary analysis of AGO10a and AGO10b subclades provides a framework for understanding functional specialization.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental support for causal role
- **Claim pointer** "Loss of AGO10 in Arabidopsis abolished pathogen gene silencing during infection, leading to hypersusceptibility to oomycete and fungal pathogens."
- **Evidence pointer** Figure 1a-e, Figure S1a-f
- **Concern** The claim that AGO10 is required for tsRNAi is based on the ago10-1 and ago10-2 mutant phenotypes. However, the manuscript does not provide direct evidence that the observed hypersusceptibility is specifically due to loss of tsRNAi rather than other AGO10 functions. The authors show that siR1310 induction is abolished in ago10-1 and that the target gene Phyca_554980 is derepressed, but this is only one example. The manuscript does not demonstrate that the hypersusceptibility phenotype is caused by the failure to silence pathogen genes, as opposed to other potential defense-related functions of AGO10.
- **Why it matters** The central claim of the paper is that AGO10 enables tsRNAi as a defense mechanism. If the hypersusceptibility is due to other functions of AGO10, the conclusion that tsRNAi is a bona fide immune response would be weakened. The causal link between AGO10-dependent tsRNAi and resistance needs to be established more directly.
- **Resolution test** The authors should provide evidence that restoration of tsRNAi specifically, for example by expressing a pathogen-targeting sRNA in the ago10 mutant background, rescues resistance. Alternatively, they could show that the hypersusceptibility phenotype correlates with the degree of loss of silencing of multiple pathogen target genes.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic link between IDR and immune response
- **Claim pointer** "This immune responsiveness relies on the N terminal intrinsically disordered region (IDR) of AGO10, which is responsible for sensing and responding to immune activation."
- **Evidence pointer** Figure 4a-g, Figure S6a-d
- **Concern** The manuscript shows that AGO10 lacking the N-terminal IDR fails to form condensates and does not rescue the ago10-1 hypersusceptibility phenotype. However, the claim that the IDR is responsible for "sensing and responding to immune activation" is not directly tested. The authors do not identify what the IDR senses or how it mediates the response. The chimera experiments with AGO1 are informative but do not establish the molecular mechanism by which the IDR confers immune responsiveness. The claim that the IDR is "necessary and sufficient" for sensing immune activation is overstated given that the authors only show relocalization, not sensing per se.
- **Why it matters** The mechanistic model proposed in the paper depends on the IDR acting as a sensor for immune activation. Without understanding what the IDR senses or how it transduces this signal, the model remains speculative. The distinction between the IDR being required for condensate formation versus being a true sensor of immune signals is important.
- **Resolution test** The authors should identify post-translational modifications or interacting partners of the IDR that change upon immune activation. Alternatively, they could show that the IDR alone is sufficient to confer immune-responsive relocalization when fused to a non-responsive protein.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Evolutionary conservation claim
- **Claim pointer** "Together, these findings establish tsRNAi as a bona fide, evolutionarily conserved immune response"
- **Evidence pointer** Figure 4h-i, Figure S8a-f
- **Concern** The evolutionary conservation claim is based on experiments in N. benthamiana showing that NbAGO10a but not NbAGO10b forms condensates and contributes to defense. However, the manuscript does not demonstrate that the N. benthamiana AGO10a proteins actually function in tsRNAi, only that silencing them leads to hypersusceptibility. The phylogenetic analysis is limited to a small number of species, and the functional data are restricted to two species. The claim of "evolutionarily conserved" immune function is broader than what the data support.
- **Why it matters** The title and abstract emphasize the evolutionary conservation of this immune function. If the conservation is not firmly established, the broader significance of the finding is reduced. The distinction between AGO10a and AGO10b subclades is interesting but the functional significance across diverse plant species is not demonstrated.
- **Resolution test** The authors should test AGO10a orthologs from additional plant families for immune-responsive condensate formation and defense function. They could also demonstrate that NbAGO10a is required for tsRNAi of pathogen genes during infection, not just for resistance.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Specificity of AGO10 in tsRNAi
- **Claim pointer** "AGO10 rapidly responds to pathogen infection through increased protein accumulation and re-location into discrete cytoplasmic condensates, thus promoting the production of trans-species sRNAs at the pathogen infection sites."
- **Evidence pointer** Figure 2a-g, Figure 3a-e, Figure S2a-h, Figure S4a-c
- **Concern** The manuscript shows that AGO10 protein levels increase and that AGO10 relocalizes to condensates upon immune activation. However, the direct link between AGO10 relocalization and the production of trans-species sRNAs is not demonstrated. The authors show that AGO10 binds to miRNAs that can trigger secondary siRNA production, but they do not show that AGO10 is required for the production of these sRNAs in the condensates. The co-localization with SGS3 is suggestive but does not prove that AGO10 is actively involved in sRNA production at these sites.
- **Why it matters** The model proposed in the discussion depends on AGO10 being recruited to siRNA bodies to promote sRNA production. Without direct evidence that AGO10 is required for sRNA production at these sites, the model remains correlative. The distinction between AGO10 being a passive passenger in condensates versus an active participant in sRNA biogenesis is important.
- **Resolution test** The authors should perform experiments showing that sRNA production from specific loci is reduced in ago10 mutants specifically at infection sites, or that AGO10 is required for the processing of specific precursor RNAs in the condensates.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Catalytic activity requirement
- **Claim pointer** "It is worth noting that there are no visible developmental defects in the ago10 mutants in Col-0 background... These results indicate that AGO10 functions through a catalytic activity-dependent mechanism in plant immunity"
- **Evidence pointer** Figure 1c, Figure S1e-f
- **Concern** The conclusion that AGO10 functions through a catalytic activity-dependent mechanism is based on the observation that catalytic mutants cannot rescue the ago10-1 phenotype. However, the manuscript does not directly demonstrate that the catalytic activity of AGO10 is required for sRNA production or target silencing. The catalytic mutants may affect protein stability, localization, or interactions independently of their catalytic activity. The authors do not show that the catalytic mutants are properly expressed and localized.
- **Why it matters** The mechanistic model depends on AGO10 acting as a slicer to initiate secondary siRNA production. If the catalytic mutants are misfolded or mislocalized, the conclusion that catalytic activity is required would be weakened. The distinction between catalytic activity and other functions of the protein is important for understanding the mechanism.
- **Resolution test** The authors should demonstrate that the catalytic mutants are expressed at similar levels and localize similarly to wild-type AGO10. They could also perform in vitro slicing assays to confirm that the catalytic mutants lack activity.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 1d-e, Figure S1d, Figure S5d
- **Evidence pointer** Figure legends
- **Issue** The manuscript states statistical significance for some experiments but does not consistently report effect sizes, confidence intervals, or exact p-values. For the pathogen infection assays, it is unclear how many independent biological replicates were performed and whether the data are representative or pooled.
- **Required correction** Provide full statistical details including exact p-values, test statistics, and numbers of replicates for all quantitative experiments. State clearly whether data are representative or pooled across experiments.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Control experiments
- **Affected element** Figure 2a-c, Figure 3a-e
- **Evidence pointer** Figure legends
- **Issue** The manuscript does not describe negative controls for the co-immunoprecipitation experiments, such as a non-specific antibody control or a control with a different Argonaute protein. The specificity of the AGO10-SGS3 interaction is not fully established.
- **Required correction** Include appropriate negative controls for co-immunoprecipitation experiments and state whether the interaction is specific to AGO10 or shared with other AGOs.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Quantification of localization data
- **Affected element** Figure 2d-g, Figure 3c
- **Evidence pointer** Figure legends
- **Concern** The manuscript describes relocalization of AGO10 to cytoplasmic puncta but does not provide quantitative analysis of this phenomenon. It is unclear how many cells were examined, what proportion showed puncta, and whether the quantification was blinded.
- **Required correction** Provide quantitative analysis of puncta formation including numbers of cells examined, proportion of cells with puncta, and statistical comparison between conditions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Methods section
- **Evidence pointer** Methods
- **Issue** The methods for the small RNA sequencing analysis are abbreviated. It is unclear how differentially expressed sRNAs were identified, what thresholds were used, and how the analysis of AGO10-bound sRNAs was performed.
- **Required correction** Expand the methods for small RNA sequencing analysis to include bioinformatics pipelines, thresholds, and statistical methods.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure accessibility
- **Affected element** All figures
- **Evidence pointer** Figure legends
- **Issue** The figure legends are brief and do not fully describe the experimental design, genotypes, treatments, and time points for each panel. This makes it difficult to evaluate the data without referring back to the main text.
- **Required correction** Expand figure legends to include full experimental details for each panel.

## Risk / unsupported claims
- The claim that AGO10 is "a specialized ARGONAUTE" is not fully supported, as the manuscript does not demonstrate that AGO10 has a unique or specialized function compared to other AGOs in tsRNAi.
- The claim that the N-terminal IDR is "responsible for sensing and responding to immune activation" is not directly tested; the data show that the IDR is required for relocalization and function, but not that it senses immune signals.
- The claim that tsRNAi is "evolutionarily conserved" is based on limited data from two species and a small phylogenetic analysis.
- The claim that AGO10 "promotes the production of trans-species sRNAs at the pathogen infection sites" is not directly demonstrated, as the manuscript does not show spatial localization of sRNA production.
- The statement that "AGO10 functions through a catalytic activity-dependent mechanism in plant immunity" is inferred from mutant rescue experiments but is not directly tested with biochemical assays.
- The claim that "specificity of AGO10 in tsRNAi" is established is not fully supported, as the manuscript does not rule out roles for other AGOs in this process.

## Assessment against Nature-style criteria
- **Originality** The concept of a specialized Argonaute mediating immune-responsive tsRNAi is novel and would be of interest to the field. The identification of AGO10 as a regulator of tsRNAi is a new finding. However, the broader concept of tsRNAi in plant immunity has been previously described, and the novelty lies primarily in the specific molecular player identified.
- **Scientific importance** The findings have potential importance for understanding plant immunity and for engineering disease resistance. If the mechanistic claims are fully supported, this could be a significant advance. However, the current evidence does not fully establish the causal role of AGO10 in tsRNAi-mediated resistance.
- **Interdisciplinary readership** The topic would appeal to plant pathologists, RNA biologists, and researchers interested in host-pathogen interactions. The potential translational applications in crop protection would broaden the appeal. However, the manuscript is written in a way that assumes substantial background knowledge in plant small RNA biology.
- **Technical soundness** The experimental approaches are generally appropriate, but several key claims lack direct experimental support. The reliance on correlative data for the link between AGO10 relocalization and sRNA production is a weakness. The lack of quantitative data for several experiments reduces confidence in the conclusions.
- **Readability for nonspecialists** The manuscript is clearly written but would be challenging for nonspecialists due to the heavy use of specialized terminology and the assumption of background knowledge in small RNA biology and plant pathology. The abstract is accessible, but the results section would benefit from additional context.

## Recommendation posture
Supportive if technical concerns are resolved. The manuscript addresses an important question and presents a potentially significant finding. However, the causal link between AGO10 function and tsRNAI-mediated resistance needs to be strengthened, the mechanistic role of the IDR requires more direct testing, and the evolutionary conservation claim needs broader support. The manuscript would be suitable for publication in a high-impact journal if these concerns are addressed with additional experiments and clearer presentation of quantitative data.