## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and funding information. No figures, tables, or supplementary files were provided for review.
- **Assessment boundary** The review is limited to the scientific claims, methodology, and interpretation as presented in the text. Experimental data, figure quality, and statistical analyses cannot be independently verified without access to the primary data and figures.
- **Shared manuscript claim summary** The authors test the hypothesis that intrinsically disordered regions (IDRs) in transcription factors drive subnuclear clustering. Using a custom hidden Markov model to predict IDRs in the Drosophila proteome, they generate a library of 75 IDRs and screen their localization in S2 cells. They find that most IDRs are uniformly distributed, while full-length transcription factors often cluster. These findings are corroborated in live embryos, and deletion of IDRs from full-length transcription factors does not abolish clustering. The authors conclude that IDRs are neither necessary nor sufficient for subnuclear clustering of transcription factors.
- **Visible evidence base** The manuscript text describes results but does not include the actual figures, tables, or supplementary files. The methods section provides details on computational prediction, cell culture, cloning, transgenesis, and imaging. No quantitative data, statistical tests, or control experiments are shown in the text.
- **Missing materials affecting confidence** Figures 1-5 and their supplements, Tables 1, Supplementary files 1-3, and Source code 1 are referenced but not provided. Without these, the validity of the computational model, the imaging data, and the conclusions cannot be fully assessed.

## Reviewer
- **Overall assessment** The manuscript addresses an important and timely question about the role of IDRs in transcription factor clustering. The experimental design is logical and the use of both cultured cells and live embryos is commendable. However, the absence of figures and data prevents a thorough evaluation of the claims. The conclusion that IDRs are neither necessary nor sufficient for clustering is strong and requires robust evidence, which cannot be verified from the text alone. The manuscript is well-written and the methods are described in sufficient detail to be reproducible, but the scientific case is not fully established from the provided material.
- **Who would be interested in the results, and why** Researchers studying transcriptional regulation, nuclear organization, phase separation, and intrinsically disordered proteins would find these results relevant. The work challenges a prevailing model that IDRs drive clustering and may influence future studies on the molecular mechanisms of transcription factor dynamics. The computational tool for IDR prediction could also be of interest to the broader genomics and proteomics community.
- **Major strengths** The study addresses a significant hypothesis with a direct and systematic approach. The use of a high-throughput screen in S2 cells followed by validation in live embryos is a strong experimental strategy. The inclusion of IDR deletion experiments in vivo is a rigorous test of necessity. The manuscript is clearly written and the methods are detailed.
- **Major Concerns** The primary concern is the lack of access to the figures and data, which are essential for evaluating the claims. Specific concerns include the validation of the HMM, the criteria for classifying clustering, the representativeness of the IDR library, and the interpretation of deletion experiments. These are detailed below.
- **Minor Comments** Several minor issues regarding clarity and interpretation are noted.
- **Technical failings that need to be addressed before the case is established** The absence of figures and data is a fundamental failing that prevents the case from being established. Additionally, the lack of quantitative analysis and statistical comparisons in the text weakens the support for the conclusions.
- **Assessment against Nature-style criteria** Originality: The work is original in its systematic test of a widely held hypothesis. Scientific importance: The findings are important for understanding transcription factor dynamics and the role of IDRs. Interdisciplinary readership: The topic is of interest to cell biologists, biochemists, and computational biologists. Technical soundness: The methods are sound in principle, but the lack of data prevents verification. Readability for nonspecialists: The manuscript is accessible, though some jargon is used. Overall, the manuscript has potential but is not fully supported by the provided material.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript may be supportable if the figures and data are provided and the concerns are addressed.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The authors claim that their HMM successfully predicts IDRs in the Drosophila proteome, as shown in Figure 1.
- **Evidence pointer** Figure 1, location not provided
- **Concern** The manuscript references Figure 1 to support the HMM's predictive power, but the figure is not provided. The text states that IUPred scores are lower in structured domains and that the HMM output agrees with known annotations, but no quantitative metrics (e.g., sensitivity, specificity, ROC curves) are given.
- **Why it matters** The HMM is the foundation for identifying the IDRs used in the entire study. Without evidence of its accuracy, the selection of IDRs and the subsequent conclusions are not reliable.
- **Resolution test** Provide Figure 1 and a quantitative evaluation of the HMM's performance, including comparison to existing predictors and known IDR annotations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental evidence
- **Claim pointer** The authors state that in S2 cells, most IDRs are distributed homogeneously, while full-length TFs often cluster (Figure 2 and 3).
- **Evidence pointer** Figures 2 and 3, location not provided
- **Concern** The classification of "clustering" versus "homogeneous" is not defined in the text. No criteria, thresholds, or quantitative measures are provided. The images are not available for review.
- **Why it matters** The central conclusion that IDRs are insufficient for clustering depends on a clear and objective distinction between clustered and non-clustered localization. Without defined criteria, the interpretation is subjective.
- **Resolution test** Provide the images and a clear definition of clustering, including any quantitative analysis (e.g., fluorescence intensity profiles, particle analysis) used to classify the patterns.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental evidence
- **Claim pointer** The authors claim that deletion of IDRs from full-length TFs does not affect clustering in embryos (Figure 6).
- **Evidence pointer** Figure 6, location not provided
- **Concern** The text states that four TFs had reduced expression upon IDR deletion, but the clustering behavior of the remaining TFs is described qualitatively. The images are not provided, and no quantitative comparison between full-length and deletion constructs is shown.
- **Why it matters** The conclusion that IDRs are not necessary for clustering relies on this experiment. If the deletion constructs are not expressed at comparable levels or if the clustering is not quantitatively assessed, the conclusion is weakened.
- **Resolution test** Provide images and quantitative analysis of clustering for full-length vs. deletion constructs, including expression level controls.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability
- **Claim pointer** The authors generalize their findings to state that IDRs are unlikely to be the primary drivers of clustering in transcription factors.
- **Evidence pointer** Discussion, location not provided
- **Concern** The study examines a limited set of 75 IDRs and 9 full-length TFs, all from Drosophila. The authors do not discuss potential limitations of this sample size or the possibility that IDRs may be important in other contexts or for other proteins.
- **Why it matters** The broad conclusion may be overreaching given the limited scope of the study. A more nuanced discussion of the conditions under which IDRs might contribute to clustering is needed.
- **Resolution test** Add a discussion of the limitations and potential exceptions, and consider whether the conclusions can be generalized beyond the tested proteins and cell types.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods, HMM description
- **Evidence pointer** Materials and methods, location not provided
- **Issue** The description of the HMM training and Viterbi prediction is brief. It is unclear how the initial state probabilities and transition probabilities were set, and how the model was validated.
- **Required correction** Provide more detail on the HMM implementation, including parameter estimation and validation steps.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results, Brk IDR localization
- **Evidence pointer** Results, location not provided
- **Concern** The Brk IDR localizes to the HLB in embryos, but the authors do not fully explore why this might occur. The discussion mentions DNA binding but does not address the specificity of this localization.
- **Required correction** Consider discussing potential mechanisms for the Brk IDR localization to the HLB and whether this is related to its DNA-binding domain.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, S2 cell screen
- **Evidence pointer** Results, location not provided
- **Concern** The text states that "very few" IDRs resemble the fine-scale clusters of TF hubs, but the number is not specified. It would be helpful to know how many IDRs showed any non-uniformity.
- **Required correction** Provide a quantitative summary of the screen results, such as the number of IDRs with different localization patterns.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, imaging
- **Evidence pointer** Materials and methods, location not provided
- **Concern** The imaging parameters (e.g., laser power, exposure time, number of cells imaged) are not specified. This limits the reproducibility of the experiments.
- **Required correction** Include detailed imaging parameters and any image analysis steps.

## Risk / unsupported claims
- The claim that IDRs are neither necessary nor sufficient for subnuclear clustering is not fully supported without the figures and quantitative data.
- The claim that the HMM successfully predicts IDRs is not verifiable without Figure 1 and performance metrics.
- The claim that full-length TFs cluster in S2 cells and embryos is not verifiable without images and defined criteria.
- The claim that IDR deletion does not affect clustering is not verifiable without images and quantitative comparison.
- The general conclusion that IDRs are unlikely to be primary drivers of clustering may be overstated given the limited sample size and lack of discussion of potential exceptions.