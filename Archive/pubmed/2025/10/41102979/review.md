## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion) for a research article published in *Proteins*.
- **Assessment boundary** Scientific soundness, methodological rigor, validity of conclusions, and clarity of presentation, assessed against the standards of a generalist high-impact journal.
- **Shared manuscript claim summary** The authors report the first blind assessment of computational methods for predicting the distribution of relative orientations and translations (poses) of two protein domains connected by a flexible linker, using CASP16 targets T1200 and T1300. They conclude that none of the 25 participating groups produced ensembles consistent with both NMR RDC and SAXS experimental data, and that this problem remains unsolved.
- **Visible evidence base** Full text including methods for NMR RDC back-calculation, SAXS forward calculation, kernel density estimation, anisotropicity scoring, and Chebyshev distance combination; results tables and figures referenced (Figures 2–9, Tables 1–2, SI Figures S1–S33, SI Tables S1–S5); data availability statement.
- **Missing materials affecting confidence** The actual prediction ensembles from the 25 groups are not provided in the manuscript; the experimental SAXS data are not shown in full; the CDIO fitting details are referenced to prior work (Qi et al.) rather than fully described; the anisotropicity calculation is described only in the SI, which was not provided in full; the manuscript states that some analyses are qualitative (e.g., shoulder identification in P(r) curves) without a quantitative metric.

## Reviewer
- **Overall assessment** This manuscript describes a carefully designed and executed blind assessment of computational methods for predicting conformational ensembles of a two-domain protein connected by a flexible linker. The use of complementary experimental techniques (NMR RDC and SAXS) is appropriate and the back-calculation approach is methodologically sound. The conclusion that current methods fail to predict the pose distribution is supported by the data presented. However, the manuscript has several limitations: the assessment is based on a single protein system, the comparison between NMR and SAXS results is not fully quantitative, and the lack of a clear success metric for "good" predictions weakens the strength of the conclusions. The work is of interest to the structural biology and protein prediction communities, but its scope is narrow and the generalizability of the findings is uncertain.
- **Who would be interested in the results, and why** Computational structural biologists developing methods for conformational ensemble prediction; experimentalists using NMR and SAXS to characterize flexible proteins; researchers studying protein A and its role in *S. aureus* virulence; CASP organizers and participants; developers of deep learning and molecular dynamics methods for protein structure prediction.
- **Major strengths** (1) The study addresses a novel and important problem: predicting not just a single structure but a distribution of conformations. (2) The use of blind prediction with experimental ground truth is rigorous. (3) The combination of NMR RDC and SAXS provides complementary information, and the back-calculation approach is appropriate. (4) The analysis is thorough, with multiple metrics considered (Pearson correlation, slope, intercept, anisotropicity) and a clear explanation of why each matters. (5) The manuscript is well-written and accessible to a broad audience.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Generalizability
  - **Claim pointer** The authors state that "predicting the distribution of poses of rigid domains connected by flexible linkers remains an unsolved problem" (Conclusion).
  - **Evidence pointer** Results, CASP experiment; Discussion, Evaluation of predictions
  - **Concern** The conclusion is based on a single protein system (SpA-derived ZLBT-C with two linker variants). While the results are clear for this system, the claim that the problem is "unsolved" in general is a strong generalization from one case. The authors do not discuss how representative this system is of the broader class of D-L-D proteins, nor do they consider whether the difficulty observed here might be specific to the properties of this particular linker or domain pair.
  - **Why it matters** A general claim about the state of the field requires evidence from multiple systems. If the problem is solved for some classes of linkers but not others, the conclusion would need to be qualified. The manuscript's title and conclusion make a broad claim that is not fully supported by the evidence presented.
  - **Resolution test** The authors should either (a) qualify their conclusion to refer specifically to the ZLBT-C system, or (b) provide evidence or argument that this system is representative of a broader class of D-L-D proteins. Alternatively, they could cite additional unpublished or published data from other systems that support the general claim.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Quantitative rigor of SAXS assessment
  - **Claim pointer** The authors state that "none were close fits to the combined NMR and SAXS data" (Abstract) and that "the predictors captured neither the preferred distance of the WT protein nor the loss of this preferred distance in the Gly6 mutant" (Results, SAXS).
  - **Evidence pointer** Results, SAXS; Figure 7
  - **Concern** The SAXS assessment relies on visual inspection of P(r) curves and qualitative identification of "shoulders" to determine whether predictions captured preferred interdomain distances. The authors acknowledge that "no metrics that can quantitatively measure bias or preferred distances have been developed for SAXS analysis." This means the SAXS-based conclusions are subjective and not reproducible. The χ² metric is used, but the authors note that χ² can obscure subtle differences, and the threshold for "close fit" is not defined.
  - **Why it matters** A central conclusion of the paper is that predictions fail to capture the preferred distances observed experimentally. If this conclusion rests on qualitative visual inspection, it is not possible for other researchers to independently verify the finding or to compare future methods against a quantitative benchmark.
  - **Resolution test** The authors should develop or adopt a quantitative metric for comparing predicted and experimental P(r) curves (e.g., a distance-based similarity measure, or a statistical test for the presence of shoulders). Alternatively, they could provide the experimental P(r) data and the predicted P(r) curves for all predictors as supplementary material, so that readers can perform their own quantitative comparisons.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Completeness of NMR assessment
  - **Claim pointer** The authors state that "none were close fits to the combined NMR and RDC data" and that the best predictor had a Chebyshev distance of 0.30 from ideal (Results, NMR).
  - **Evidence pointer** Results, NMR; Table 2; Figure 8
  - **Concern** The NMR assessment is based on RDC data from the WT protein only. The Gly6 variant was not characterized by NMR, so the assessment of the Gly6 predictions relies solely on SAXS. This means that the two targets are assessed with different levels of rigor, and the comparison between WT and Gly6 predictions is not symmetric. Additionally, the manuscript does not report the experimental uncertainty in the RDC data, which is needed to interpret the Chebyshev distances.
  - **Why it matters** The authors emphasize the complementarity of NMR and SAXS, but the Gly6 target is only assessed by one method. This limits the strength of the conclusion that predictions for Gly6 are inaccurate, since the SAXS assessment is qualitative (see R1-M2). The lack of reported experimental uncertainty also makes it difficult to judge whether a Chebyshev distance of 0.30 is meaningfully different from a perfect fit.
  - **Resolution test** The authors should either (a) collect and report NMR RDC data for the Gly6 variant, or (b) clearly state the limitation that the Gly6 target is assessed by SAXS only and discuss the implications for the conclusions. They should also report the experimental uncertainty in the RDC data and, if possible, provide a statistical framework for interpreting the Chebyshev distances.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Reproducibility
  - **Claim pointer** The authors state that "all data processing scripts will be uploaded to https://github.com/donaldlab/CASP16 upon acceptance" (Data availability).
  - **Evidence pointer** Data availability
  - **Concern** The data availability statement indicates that scripts will be uploaded "upon acceptance," but the manuscript is already published. The repository is not yet available, and the manuscript does not provide a version of the code or a permanent DOI. This makes it impossible for readers to reproduce the analysis or to apply the assessment methodology to their own predictions.
  - **Why it matters** Reproducibility is a core requirement for scientific publications. The assessment methodology described here is novel and could be valuable to the community, but it is not usable until the code and data are made available.
  - **Resolution test** The authors should make the repository publicly available immediately and provide a permanent link (e.g., a DOI from Zenodo or Figshare) in the manuscript. They should also ensure that the repository includes all necessary data (e.g., experimental RDC and SAXS data, prediction ensembles, and processing scripts).
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Abstract
  - **Evidence pointer** Abstract
  - **Issue** The abstract states that "the range of interdomain distances and orientations (poses) of such domain-linker-domain (D-L-D) proteins can play an important role in protein function, allostery, aggregation, and the thermodynamics of binding." This is a broad claim that is not directly supported by the data presented in the manuscript.
  - **Required correction** Consider softening the claim or providing a citation to support it.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Methods, NMR Computational Methods
  - **Evidence pointer** Materials and Methods, NMR Computational Methods
  - **Issue** The description of the CDIO fitting procedure is brief and refers to prior work. The manuscript states that "two distinct solutions were found with similar goodness-of-fit" but does not explain how these solutions differ or how the α parameter interpolates between them.
  - **Required correction** Provide a brief explanation of the two solutions and the meaning of α, or refer the reader to a specific section of the SI where this is described in more detail.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Results, SAXS
  - **Evidence pointer** Results, SAXS; Figure 4
  - **Issue** The description of the SAXS data collection mentions that "details will be published in an experimental paper." This is appropriate, but the manuscript should state whether the SAXS data are available at a public repository (e.g., SASBDB) and provide an accession code if available.
  - **Required correction** Add a statement about data availability for the SAXS data, including a repository and accession code if applicable.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Discussion, Evaluation of predictions
  - **Evidence pointer** Discussion, Evaluation of predictions
  - **Issue** The discussion of the Pareto frontier is interesting but brief. The authors state that the frontier "contains predictions 308, 136, 304, and 345" but do not discuss what these predictions have in common or what lessons can be drawn from their relative success.
  - **Required correction** Expand the discussion of the Pareto frontier to provide more insight into the methods that performed well on different axes.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Conclusion
  - **Evidence pointer** Conclusion
  - **Issue** The conclusion states that "the prediction of protein conformational dynamics driving biological function is an important frontier in structural biology." This is a general statement that is not directly connected to the specific findings of the manuscript.
  - **Required correction** Consider connecting this statement more explicitly to the findings of the study, e.g., by noting that the failure of current methods highlights the need for new approaches.
- **Technical failings that need to be addressed before the case is established** (1) The SAXS assessment lacks a quantitative metric for comparing predicted and experimental P(r) curves, making the central conclusion partially subjective. (2) The Gly6 target is assessed by SAXS only, while the WT target is assessed by both NMR and SAXS, creating an asymmetry in the assessment. (3) The data availability statement is not yet fulfilled, preventing independent verification of the analysis. (4) The manuscript does not report experimental uncertainties for the RDC data, which are needed to interpret the Chebyshev distances.
- **Assessment against Nature-style criteria**  
  *Originality*: The work is original in its approach to assessing conformational ensemble predictions as distributions rather than single structures. The use of CDIOs and the combination of NMR and SAXS back-calculation is novel. However, the underlying problem (predicting flexible linker conformations) is not new, and the manuscript does not introduce a new computational method.  
  *Scientific importance*: The findings are important for the protein structure prediction community, as they establish a benchmark for ensemble prediction and demonstrate that current methods are inadequate. However, the importance is limited by the narrow scope (one protein system) and the lack of a quantitative SAXS metric.  
  *Interdisciplinary readership*: The manuscript is likely to appeal primarily to computational structural biologists and NMR/SAXS experimentalists. The broader biological community may find the protein A context interesting, but the technical nature of the assessment limits its appeal.  
  *Technical soundness*: The NMR RDC back-calculation and CDIO fitting are technically sound and well-described. The SAXS back-calculation using FoXS is appropriate. However, the lack of a quantitative SAXS metric and the asymmetry between WT and Gly6 assessments are weaknesses.  
  *Readability for nonspecialists*: The manuscript is generally well-written and accessible. The introduction provides sufficient context, and the methods are explained clearly. However, some sections (e.g., the CDIO fitting) assume familiarity with specialized concepts.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important problem and the NMR-based assessment is rigorous. However, the qualitative nature of the SAXS assessment and the lack of data availability prevent the conclusions from being fully established. If the authors can provide a quantitative SAXS metric, make the data and code available, and qualify their conclusions appropriately, the manuscript would be suitable for publication.

## Risk / unsupported claims
- The claim that "none were close fits to the combined NMR and SAXS data" is partially unsupported because the SAXS assessment is qualitative and no quantitative threshold for "close fit" is defined.
- The claim that "predicting the distribution of poses of rigid domains connected by flexible linkers remains an unsolved problem" is a generalization from a single protein system and is not fully supported.
- The statement that "the conserved sequence of the WT linker encodes constrained flexibility" is presented as a hypothesis but is not directly tested in this manuscript.
- The claim that "about half of the predictors performed better on the WT compared to the Gly6 mutant" is based on visual inspection of Figure 6D and is not supported by a statistical test.
- The manuscript states that "the introduction of such targets to CASP recognizes the importance of predicting distributions of conformations realized in solution," but this is an interpretation of CASP's intentions that is not verifiable from the data presented.