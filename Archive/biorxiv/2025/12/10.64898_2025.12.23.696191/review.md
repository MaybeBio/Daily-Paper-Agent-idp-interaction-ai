## Review setup
- **Input scope** Full manuscript text (Abstract, Introduction, Results, Discussion, Methods, Supporting Information description) as provided
- **Assessment boundary** Scientific content, methodological soundness, evidence quality, and internal consistency of the claims as presented in the supplied text
- **Shared manuscript claim summary** The authors use coarse-grained molecular dynamics simulations to show that selective partitioning of client IDRs into MED1 and FUS condensates is driven by favourable client–scaffold interactions, that these interactions compete with scaffold self-interactions, that interaction energies localize to specific sequence regions (charged blocks for MED1, aromatic residues for FUS), and that a sequence-based predictor built on these insights can capture partitioning trends across a dataset of 243 sequences
- **Visible evidence base** Main text Figures 1–5 (referenced), Supplementary Figures S1–S5, Supplementary Table S1, Methods section, Data availability statement
- **Missing materials affecting confidence** Actual figure images and numerical data are not provided; only figure captions and in-text descriptions are available. Supplementary figures and tables are referenced but not included in the supplied material. Simulation input files and analysis code are available via external repositories but were not inspected

## Reviewer

- **Overall assessment** This manuscript addresses a timely and important question in the field of biomolecular condensates: what molecular features determine whether a client protein partitions into a given condensate. The authors combine state-of-the-art coarse-grained simulations with a systematic analysis of interaction energies and propose a sequence-based predictor. The work is conceptually interesting and the simulation approach is appropriate. However, the manuscript as presented has several issues that need to be addressed. The correlation between simulated and experimental partitioning energies is based on a small number of data points and the statistical significance is not reported. The claim that the predictor "captures distinct trends" among the three experimental categories is supported by a figure that is not visible in the supplied material, and the reported Matthews correlation coefficient of 0.18 is modest. The mechanistic interpretation regarding competition between scaffold–scaffold and scaffold–client interactions is plausible but the evidence for the "competition" claim is indirect. The discussion of the role of RNA in modulating partitioning is interesting but somewhat speculative. Overall, the work has potential but the case is not fully established from the provided evidence.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, particularly those interested in the molecular determinants of client partitioning and selectivity. The work is also relevant to the broader community developing coarse-grained models for IDR phase behaviour and to computational biologists interested in sequence-based prediction of condensate interactions. The proposed predictor could be of practical use for interpreting experimental partitioning data and for generating hypotheses about client recruitment in cellular contexts.

- **Major strengths**
  1. The study addresses a fundamental and unresolved question in the field: what determines selective client partitioning into condensates.
  2. The use of a well-established coarse-grained model (CALVADOS 2) with demonstrated predictive utility for IDR phase behaviour is appropriate.
  3. The systematic analysis of per-residue interaction energies provides mechanistic insight beyond simple contact-based analyses.
  4. The development of a sequence-based predictor that incorporates local interaction localization is a useful contribution.
  5. The inclusion of RNA in the simulations for the MED1 system adds a relevant layer of complexity that is often neglected.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** "The partitioning energies obtained from our simulations correlated relatively well with experimental partitioning energies derived from in-vivo measurements of the partition coefficient (Fig. 1e; the Spearman rank-order correlation coefficient=0.71)."
- **Evidence pointer** Figure 1e, Section 2.1
- **Concern** The correlation coefficient of 0.71 is reported for what appears to be a small number of data points (six client proteins). The statistical significance of this correlation is not reported. With n=6, a Spearman correlation of 0.71 may not be statistically significant (p-value would be approximately 0.11 for a two-sided test). The authors should report the p-value and confidence interval. Additionally, the experimental data are derived from in-vivo measurements, which may involve additional factors not captured in the simulations. The authors should discuss the limitations of this comparison more explicitly.
- **Why it matters** The correlation with experimental data is a key validation of the simulation approach. If the correlation is not statistically significant, the claim that the simulations "capture" experimental partitioning behaviour is weakened.
- **Resolution test** Report the p-value and confidence interval for the Spearman correlation. If the correlation is not significant, temper the claim accordingly. Consider also reporting the correlation excluding any potential outliers.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** "Our predictor captured the distinct trends among the three categories (Fig. 5) and, when used as a classifier of partitioning, performed at least as well as a previously proposed model as measured by AUC (Fig. S4)."
- **Evidence pointer** Figure 5, Figure S4, Table S1, Section 2.4
- **Concern** The performance of the predictor is a central claim of the manuscript, but the actual data supporting this claim are not visible in the supplied material. The Matthews correlation coefficient of 0.18 is reported in the text, which is low. The claim that the predictor "performed at least as well as a previously proposed model" is vague. The authors should provide the actual AUC values, the full confusion matrix, and a more detailed comparison with the FINCHES method. The choice of thresholds for classification should be justified. The manuscript should also discuss what level of performance would be considered practically useful for this type of prediction.
- **Why it matters** The predictor is presented as a key outcome of the work. Without clear evidence of its performance, the utility of the predictor is not established.
- **Resolution test** Provide the actual data behind Figure 5 and Figure S4, including AUC values with confidence intervals, the confusion matrix, and a clear description of the classification thresholds. Discuss the practical utility of the achieved performance.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation
- **Claim pointer** "We reasoned that the surface enrichment of FUS clients originated from the interaction of the client with RNA present in the dilute phase, and therefore performed additional simulations using RNA-free FUS systems."
- **Evidence pointer** Section 2.1, Figure 1d
- **Concern** The interpretation that surface enrichment is due to RNA in the dilute phase is presented as a "reasoning" but is not directly tested. The authors do not provide a quantitative analysis of the interaction between the clients and RNA in the dilute phase, nor do they show that removing RNA eliminates the surface enrichment. The claim that "in the experiments, the dilute phase occupies a large volume fraction, resulting in low RNA concentrations outside of the condensates" is speculative and not supported by data presented in the manuscript.
- **Why it matters** The role of RNA in modulating partitioning is an important aspect of the work. If the interpretation is incorrect, the conclusions about the FUS system may be affected.
- **Resolution test** Provide a direct test of the hypothesis, e.g., by calculating client–RNA interaction energies in the dilute phase, or by performing simulations with varying RNA concentrations. Alternatively, temper the claim and present it as a hypothesis.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "The client–scaffold interaction energy was negatively correlated with the scaffold–scaffold interaction energy (Figs. 2e and f), indicating that client interactions partially replaced homotypic scaffold interactions."
- **Evidence pointer** Figures 2e and 2f, Section 2.2
- **Concern** The claim of "competition" between scaffold–scaffold and scaffold–client interactions is based on a negative correlation between two quantities that are both derived from the same simulation trajectories. This correlation could arise trivially from the way the interaction energies are computed or from the finite size of the simulation box. The authors should provide a more direct test of the competition hypothesis, e.g., by comparing the total interaction energy of the system with and without clients, or by analysing the scaffold network structure in the presence and absence of clients.
- **Why it matters** The competition mechanism is a central conceptual claim of the paper. If the evidence is only correlative, the mechanistic interpretation is weakened.
- **Resolution test** Provide a direct test of the competition hypothesis, such as a comparison of scaffold–scaffold interaction energies in the presence and absence of clients, or an analysis of the scaffold network connectivity.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.1, Figure 1d
- **Evidence pointer** Figure 1d
- **Issue** The assignment of "ΔG = 8 RT" to systems exhibiting substantial partitioning or exclusion is described in the Methods, but the threshold for "substantial" is not clearly defined. It would be helpful to state the criteria used for this assignment.
- **Required correction** Define the criteria for assigning the qualitative ΔG value of 8 RT in the Methods or in the Figure 1 caption.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2.4, Figure 4
- **Evidence pointer** Figure 4b
- **Issue** The comparison between the predicted interaction map and the contact energy map from MD simulations is described qualitatively. A quantitative measure of agreement (e.g., a correlation coefficient) would strengthen the claim that the predictor captures the interaction pattern.
- **Required correction** Provide a quantitative comparison between the predicted and simulated interaction maps.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.1, Figure 1e
- **Evidence pointer** Figure 1e
- **Issue** The experimental partitioning energies are derived from in-vivo measurements. The authors should clarify whether these are the same data as reported in reference 36, and whether any re-analysis was performed.
- **Required correction** Clarify the source of the experimental data and any processing steps applied.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section 4.2
- **Evidence pointer** Section 4.2
- **Issue** The use of biased simulations with dragging external forces to accelerate convergence is mentioned, but the details of the bias (e.g., the magnitude of the force, the duration of the biased phase) are not provided. This information is important for reproducibility.
- **Required correction** Provide details of the biased simulation protocol, including the force constant and the duration of the biased phase.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Section 3, Discussion
- **Evidence pointer** Section 3
- **Issue** The statement "we speculate the dilute phases within the cells may have a similar modulating effect" is presented without supporting evidence. While speculation is acceptable in a Discussion, it should be clearly flagged as such and distinguished from the findings of this work.
- **Required correction** Clearly label this as speculation and consider discussing how it could be tested.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2.2, Figure 2
- **Evidence pointer** Figure 2c
- **Issue** The decomposition of interaction energies by macromolecule type (MED1, RNA, and surrounding client molecules) is shown for a subset of clients. It would be useful to show this decomposition for all six clients to assess the generality of the observation.
- **Required correction** Consider showing the decomposition for all clients, either in the main figure or in the supplementary material.

- **Technical failings that need to be addressed before the case is established**
  1. Statistical significance of the correlation between simulated and experimental partitioning energies (R1-M1).
  2. Lack of visible data supporting the predictor performance claims (R1-M2).
  3. Indirect evidence for the competition mechanism (R1-M4).
  4. Insufficient detail on the biased simulation protocol (R1-m4).

- **Assessment against Nature-style criteria**
  - **Originality** The work addresses a question of high current interest and proposes a novel sequence-based predictor that incorporates local interaction localization. The concept of competition between scaffold–scaffold and scaffold–client interactions is not entirely new but is applied here in a systematic manner. The originality is moderate to high.
  - **Scientific importance** Understanding the molecular determinants of client partitioning into condensates is of significant importance for the field. The work has the potential to inform experimental design and to provide a framework for predicting partitioning behaviour. The importance is high.
  - **Interdisciplinary readership** The work is primarily of interest to researchers in biophysics, computational biology, and cell biology. The use of coarse-grained simulations and the development of a sequence-based predictor may also appeal to a broader readership interested in predictive models of biomolecular behaviour. The interdisciplinary reach is moderate.
  - **Technical soundness** The simulation methodology is appropriate and the use of CALVADOS 2 is well justified. However, the statistical analysis of the correlation with experimental data is incomplete, and the evidence for the competition mechanism is indirect. The technical soundness is moderate.
  - **Readability for nonspecialists** The manuscript is generally well written and the concepts are explained clearly. However, some sections, particularly the description of the sequence-based predictor, may be challenging for nonspecialists. The readability is moderate.

- **Recommendation posture** Supportive if technical concerns are resolved. The work addresses an important question and the approach is promising. However, the statistical significance of the key correlation needs to be established, the performance of the predictor needs to be documented more clearly, and the evidence for the competition mechanism needs to be strengthened. Once these issues are addressed, the manuscript could be suitable for publication in a high-impact journal.

## Risk / unsupported claims
- The claim that the simulations "capture" experimental partitioning behaviour is not fully supported due to the lack of statistical significance testing for the reported correlation.
- The claim that the predictor "captured the distinct trends among the three categories" is not verifiable from the supplied material, as the relevant figure is not visible.
- The claim that "client interactions partially replaced homotypic scaffold interactions" is based on a correlative analysis and is not directly tested.
- The speculation that "the dilute phases within the cells may have a similar modulating effect" is not supported by data presented in this manuscript.
- The claim that "the surface enrichment of FUS clients originated from the interaction of the client with RNA present in the dilute phase" is presented as a reasoning but is not directly tested.