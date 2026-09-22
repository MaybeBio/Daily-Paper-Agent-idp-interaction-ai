## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, figure legends, appendix)
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and internal consistency based solely on the provided text. No external data or unpublished materials were consulted.
- **Shared manuscript claim summary** The authors propose that the intrinsically disordered region (IDR) of the transcription factor Crz1 has undergone functional divergence between Saccharomyces and more distantly related fungi, while the stochastic pulsatile signaling phenotype has been conserved by stabilizing selection. They report that Saccharomyces IDRs support pulsatility, encode environmental information, and rescue fitness in S. cerevisiae, whereas outgroup IDRs do not, despite all tested IDRs supporting transient nuclear localization. They further identify a calcineurin docking site (PxIxIT) whose increased strength in the Saccharomyces clade appears sufficient to rescue pulsatility and fitness when introduced into a non-pulsing outgroup IDR.
- **Visible evidence base** Abstract, Introduction, Results (four subsections), Discussion, Methods (strain construction, microscopy, image analysis, Gaussian Process modeling, mutual information estimation, sequence analysis), Figure legends (Supplementary Figures 1–5), Appendix (MI estimation details, list of 40 fungi)
- **Missing materials affecting confidence** Main-text figures (Figures 1–6) are referenced but not provided. Supplementary Movies 1 and 2 are referenced but not provided. No raw data, strain lists, or code are included. Statistical details for several comparisons are incomplete (e.g., exact n for some fitness assays, full distributions for MI estimates).

## Reviewer

- **Overall assessment** This manuscript addresses a timely and important question in evolutionary cell biology: how stochastic signaling dynamics are conserved despite rapid sequence divergence in the regulatory regions that encode them. The authors combine comparative genomics, quantitative live-cell imaging, information theory, and fitness assays to build a compelling case that Crz1 pulsatility is conserved across distantly related fungi and that this conservation is maintained by stabilizing selection acting on functionally divergent IDRs. The identification of a single calcineurin docking site whose strength appears to be a key determinant of pulsatility is a notable and potentially generalizable finding. However, the manuscript as presented has several technical and evidentiary gaps that must be addressed before the central claims can be considered fully established. In particular, the reliance on a passive reporter system, the limited number of outgroup species tested, the indirect inference of stabilizing selection, and the incomplete statistical reporting weaken the current version. The work is likely to be of broad interest to cell biologists, evolutionary biologists, and biophysicists, and the conceptual framework is novel, but the evidence base as provided is not yet sufficient for a high-impact general journal.

- **Who would be interested in the results, and why** This work will appeal to researchers studying stochastic gene expression and signaling dynamics, particularly those focused on transcription factor pulsatility and calcium signaling. It will also interest evolutionary biologists working on the evolution of regulatory networks and intrinsically disordered proteins, as it provides one of the first molecular-level descriptions of how a dynamic signaling phenotype can be conserved despite extensive sequence divergence. The use of information theory to quantify information transmission between two stochastic components on the same pathway is a methodological contribution that will interest systems biologists. Finally, the finding that a short linear motif's position and strength can be tuned to rewire signaling dynamics has implications for protein engineering and synthetic biology.

- **Major strengths**
  1. The study addresses a fundamental and under-explored question: how stochastic signaling dynamics evolve. The authors correctly note that most prior work has focused on the evolution of specificity in kinases and receptors, leaving the evolution of dynamic encoding largely uncharacterized.
  2. The combination of comparative functional assays (expression of orthologous IDRs in S. cerevisiae) with native-system validation (pulsing in C. albicans and S. pombe) is a powerful and appropriate design.
  3. The use of information theory to quantify the information encoded in pulsatile dynamics is rigorous and appropriate, and the finding that Saccharomyces IDRs encode more information than outgroup IDRs is a clear and quantitative result.
  4. The identification of a specific PxIxIT site and the demonstration that increasing its strength via three point mutations can rescue pulsatility and fitness is a strong, mechanistically informative result.
  5. The fitness assays are well designed, including the use of a CRZ1 deletion control and a phosphorylation-site mutant to calibrate the sensitivity of the assay.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency for central claim
- **Claim pointer** The authors claim that "Crz1 IDRs from the Saccharomyces clade support pulsatility, encode extra information, and rescue fitness, while the Crz1 IDRs from distantly related fungi do none of the three."
- **Evidence pointer** Results section "Evolutionary changes in Crz1 IDRs are associated with changes in Crz1 pulsing"; Figure 2 (not provided); Supplementary Figure 1
- **Concern** The central claim that outgroup IDRs do not support pulsatility is based on experiments in which outgroup IDRs are expressed in S. cerevisiae. This is a chimeric context, and the lack of pulsatility could be due to the absence of species-specific interaction partners or post-translational modifications in S. cerevisiae, rather than an intrinsic property of the outgroup IDRs. The authors do not provide evidence that the relevant interaction partners (e.g., calcineurin, exportins, importins) are functionally conserved between S. cerevisiae and the outgroup species. Without this control, the conclusion that the outgroup IDRs are functionally divergent is not fully supported.
- **Why it matters** The claim of functional divergence is the foundation for the entire paper. If the outgroup IDRs fail to pulse simply because of incompatibility with the S. cerevisiae environment, then the conclusion that pulsatility is a derived trait in Saccharomyces is weakened, and the interpretation of stabilizing selection becomes less secure.
- **Resolution test** The authors should either (a) demonstrate that the relevant interaction partners are conserved and functional in S. cerevisiae, for example by showing that a known S. cerevisiae interaction partner can bind the outgroup IDRs, or (b) perform reciprocal experiments in which S. cerevisiae IDRs are expressed in an outgroup species, or (c) provide evidence that the outgroup IDRs are unable to interact with S. cerevisiae calcineurin despite the presence of a consensus PxIxIT site. Alternatively, the authors could temper the claim to state that the outgroup IDRs do not support pulsatility in the S. cerevisiae context, which is a weaker but still informative statement.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor and reporting
- **Claim pointer** The authors report mutual information estimates (mean MI = 0.41 bits vs. 0.04 bits, p = 0.004; mean MI = 0.72 bits vs. 0.13 bits, p < 10⁻³) and fitness differences (selection coefficients) between constructs.
- **Evidence pointer** Results section "Evolutionary changes in Crz1 IDRs are associated with changes in Crz1 pulsing"; Figure 2E and 2F (not provided); Methods "Estimation of mutual information and pulse-triggered averaging"
- **Concern** The statistical reporting is incomplete. For the mutual information estimates, the authors report means and p-values but do not report the variance, the number of cells or replicates, or the distribution of the estimates. For the fitness assays, the number of replicates is stated as n = 16 and n = 6 for one comparison, but the variance and the method of calculating the p-value are not described. The authors also do not report whether the MI estimates were normally distributed or whether non-parametric tests were used. The bootstrap procedure is described, but the number of bootstrap iterations and the confidence intervals are not reported.
- **Why it matters** The quantitative claims are central to the paper. Without proper reporting of variance and replication, the reader cannot assess the robustness of the differences or the reliability of the conclusions drawn from them.
- **Resolution test** The authors should provide full statistical details for all reported comparisons, including the number of biological and technical replicates, the variance (e.g., standard deviation or confidence intervals), the statistical test used, and the exact p-values. For the MI estimates, the authors should report the distribution of the bootstrap estimates and the confidence intervals. For the fitness assays, the authors should report the standard error of the selection coefficients and the method used to compare them.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Inference of evolutionary model
- **Claim pointer** The authors conclude that "the conservation of phenotype but lack of conservation of IDR functions indicates that, within the disordered region, evolutionary changes in some elements needed for complex signaling dynamics have compensated for evolutionary changes in others. This pattern of compensatory evolution in the context of preserved function is a hallmark of stabilizing selection."
- **Evidence pointer** Results section "Pulsing has been under stabilizing selection, but the underlying mechanisms have changed"; Discussion
- **Concern** The inference of stabilizing selection is indirect. The authors observe that pulsatility is present in S. cerevisiae, C. albicans, and S. pombe, and that the IDRs from the latter two do not function in S. cerevisiae. They interpret this as evidence for compensatory evolution under stabilizing selection. However, an alternative explanation is that the pulsatility in the outgroup species is driven by different molecular mechanisms that do not rely on the IDR in the same way, and that the conservation of the phenotype is due to convergent evolution or to the conservation of upstream signaling components rather than to stabilizing selection on the IDR itself. The authors acknowledge the convergent evolution possibility but dismiss it as less parsimonious without providing a formal test.
- **Why it matters** The claim of stabilizing selection is a major conceptual contribution of the paper. If the evidence is not sufficient to distinguish stabilizing selection from other evolutionary models, the broader significance of the work is diminished.
- **Resolution test** The authors should either (a) provide a formal phylogenetic test of stabilizing selection, for example by comparing the ratio of nonsynonymous to synonymous substitution rates (dN/dS) in the IDR across the phylogeny, or (b) provide additional experimental evidence that the IDR is under functional constraint in the outgroup species, for example by showing that mutations in the outgroup IDR affect pulsatility in the native context, or (c) soften the claim to state that the data are consistent with stabilizing selection but that other models cannot be excluded.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic sufficiency of PxIxIT claim
- **Claim pointer** The authors claim that "a calcineurin docking site in a specific part of the IDRs appears to be sufficient for pulsing" and that increasing PxIxIT strength via three point mutations rescues pulsatility and fitness.
- **Evidence pointer** Results section "Increasing PxIxIT strength in the homologous region of S. cerevisiae IDR is sufficient to rescue pulsing phenotype and fitness"; Figure 5 (not provided)
- **Concern** The claim that PxIxIT strength is sufficient for pulsatility is based on a single chimeric construct (Ca High) and a single comparison with the wild-type C. albicans IDR. The authors do not test whether the position of the PxIxIT site is critical, nor do they test whether other mutations in the IDR that do not affect PxIxIT strength can also rescue pulsatility. The authors also do not directly measure the binding affinity of the mutant PxIxIT site to calcineurin; they rely on a predicted strength from a PSSM. The correlation between predicted strength and measured affinity is based on only 10 data points (R² = 0.74), which is a modest sample size.
- **Why it matters** The PxIxIT claim is the most mechanistically specific finding in the paper. If the evidence is not sufficient to establish that PxIxIT strength is the causal determinant of pulsatility, the paper's contribution is reduced to a descriptive observation.
- **Resolution test** The authors should (a) provide direct binding measurements (e.g., isothermal titration calorimetry or surface plasmon resonance) for the wild-type and mutant PxIxIT sites, (b) test additional mutations in the IDR that do not affect PxIxIT strength as negative controls, and (c) test whether the position of the PxIxIT site relative to other IDR features is important by generating additional chimeric constructs.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of findings
- **Claim pointer** The authors state that "our results are also the first molecular description of the evolutionary flexibility of post-translationally controlled pulsatility and stochastic dynamic signal processing."
- **Evidence pointer** Discussion
- **Concern** The study is limited to a single transcription factor (Crz1) in a single signaling pathway (calcium/calcineurin) in fungi. While the authors are appropriately cautious in their language, the claim of being the "first molecular description" is broad and may be difficult to verify. More importantly, the generalizability of the finding that IDR divergence underlies conserved pulsatility is not tested in other systems. The authors do not discuss whether similar mechanisms might operate in other pulsatile transcription factors (e.g., Msn2, NFAT) or in other organisms.
- **Why it matters** The broader significance of the work depends on whether the findings are likely to apply to other signaling systems. Without a discussion of generalizability or a comparative analysis, the impact of the work is limited.
- **Resolution test** The authors should either (a) provide a comparative analysis of IDR sequences and pulsatility across a broader set of transcription factors or organisms, or (b) discuss in the Discussion section the extent to which their findings are likely to generalize, citing relevant literature on other pulsatile systems.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of reporting
- **Affected element** Methods, "Yeast strains"
- **Evidence pointer** Methods section "Yeast strains"
- **Issue** The description of the construction of the chimeric IDR constructs is incomplete. The authors state that "the chimeric IDRs were constructed through two-fragment transformations," but they do not specify the exact boundaries of the chimeric junctions, the primers used, or the verification method (e.g., Sanger sequencing).
- **Required correction** Provide a detailed description of the cloning strategy, including the exact amino acid positions of the chimeric junctions, the primers used, and the sequencing verification.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Figure accessibility
- **Affected element** Figure 2
- **Evidence pointer** Results section "Evolutionary changes in Crz1 IDRs are associated with changes in Crz1 pulsing"; Figure 2 (not provided)
- **Issue** The main text refers to Figure 2E and 2F for the MI and fitness results, but the figure itself is not provided in the manuscript. The reader cannot assess the data visually.
- **Required correction** Ensure that all main-text figures are included in the manuscript submission and that the figure legends are sufficiently detailed to allow interpretation without the main text.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract; Introduction
- **Issue** The term "stochastic signaling" is used throughout, but it is not explicitly defined. The authors may wish to clarify whether they refer to stochastic dynamics in the concentration of a signaling molecule, stochastic nuclear localization, or stochastic gene expression.
- **Required correction** Define "stochastic signaling" at first use and clarify the specific stochastic process being measured.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Consistency of supplementary materials
- **Affected element** Supplementary Figure 4
- **Evidence pointer** Supplementary Figure 4 legend
- **Issue** The legend for Supplementary Figure 4 states that "plots are broken to indicate when each experiment switched to a different microscope field to avoid laser-induced nuclear localization." This is an important detail, but it is not described in the Methods section.
- **Required correction** Add a description of the field-switching procedure to the Methods section and explain how this affects the data analysis.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical reporting in supplementary
- **Affected element** Supplementary Figure 3
- **Evidence pointer** Supplementary Figure 3 legend
- **Issue** The legend for Supplementary Figure 3 reports a selection coefficient of -0.05 for the 5A mutant, but the main text reports a value of -0.038 from the original publication. The discrepancy is not explained.
- **Required correction** Clarify whether the -0.05 value is from a single experiment or an average, and explain the difference from the published value.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Methods
- **Evidence pointer** Methods section (all subsections)
- **Issue** No statement is provided regarding data availability, code availability, or the availability of strains and plasmids.
- **Required correction** Add a Data Availability statement and, if applicable, a Code Availability statement.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Language precision
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The phrase "ruling out misfolding or misexpression effects" is too strong. The fitness assay can rule out large effects on protein stability or expression, but it cannot rule out subtle effects on folding or expression that might still affect function.
- **Required correction** Rephrase to "suggesting that the fitness differences are not due to gross misfolding or misexpression."

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: The lack of evidence for functional conservation of interaction partners in the S. cerevisiae context undermines the central claim of functional divergence.
  - R1-M2: Incomplete statistical reporting for MI and fitness comparisons prevents assessment of robustness.
  - R1-M4: The sufficiency claim for PxIxIT strength is based on a single construct and a predicted, not measured, binding strength.

- **Assessment against Nature-style criteria**
  - **Originality** The question of how stochastic signaling dynamics evolve is largely unexplored, and the authors provide a novel conceptual framework linking IDR divergence to conserved dynamics via stabilizing selection. The use of information theory to quantify information transmission between two stochastic components is also novel. The work is original in its approach and conclusions.
  - **Scientific importance** The findings have implications for understanding the evolution of signaling dynamics, the functional role of IDRs, and the mechanisms of stabilizing selection. The work could influence how researchers think about the evolution of dynamic encoding in signaling pathways. However, the importance is somewhat limited by the focus on a single transcription factor and the lack of generalizability testing.
  - **Interdisciplinary readership** The work bridges cell biology, evolutionary biology, and systems biology. The use of information theory and quantitative imaging will appeal to biophysicists and systems biologists, while the evolutionary framework will appeal to evolutionary biologists. The writing is generally accessible, but the Methods section is dense and may be challenging for non-specialists.
  - **Technical soundness** The experimental design is generally sound, with appropriate controls (e.g., CRZ1 deletion, phosphorylation-site mutant). The use of Gaussian Process regression and mutual information estimation is appropriate. However, the statistical reporting is incomplete, and the sufficiency claim for PxIxIT is not fully supported by the data. The lack of direct binding measurements and the limited number of outgroup species are additional weaknesses.
  - **Readability for nonspecialists** The abstract and introduction are clear and accessible. The Results section is well-structured, but the Methods section is highly technical and may be difficult for readers without a background in quantitative biology. The Discussion is readable and places the work in a broader context.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important and novel question, and the conceptual framework is compelling. However, the central claim of functional divergence is not fully supported by the evidence as presented, and the statistical reporting needs to be improved. If the authors can address these concerns, the work would be suitable for a high-impact journal.

## Risk / unsupported claims
- The claim that outgroup IDRs "do none of the three" (support pulsatility, encode information, rescue fitness) is not fully supported because the experiments were performed in a chimeric S. cerevisiae context without demonstrating functional conservation of interaction partners.
- The claim that "increasing PxIxIT strength in the homologous region of S. cerevisiae IDR is sufficient to rescue pulsating phenotype and fitness" is based on a single construct and a predicted binding strength, not a direct measurement.
- The inference of stabilizing selection is indirect and not formally tested against alternative models such as convergent evolution.
- The claim of being the "first molecular description of the evolutionary flexibility of post-translationally controlled pulsatility" is broad and not verifiable from the provided materials.
- The statement that the fitness assay rules out "misfolding or misexpression effects" is too strong, as the assay can only detect large effects.