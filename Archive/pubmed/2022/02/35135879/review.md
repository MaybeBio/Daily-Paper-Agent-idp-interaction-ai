## Review setup
- **Input scope** Full manuscript text (main text, figures referenced, tables, methods, discussion)
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and conclusions as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors report that the pathogenic N-terminal Tau mutation R5L does not alter Tau's affinity for microtubules but reduces Tau occupancy and disrupts formation of Tau patches/condensates on Taxol-stabilized microtubules. They attribute this to a local structural change in the N-terminal projection domain, detected by NMR, which weakens interactions between the projection domain and the microtubule surface. They propose that disruption of Tau patch formation, rather than reduced microtubule affinity, is the pathogenic mechanism.
- **Visible evidence base** TIRF microscopy binding assays (Fig. 1A-B), microtubule pelleting assays (Fig. 1C), patch frequency and size quantification (Fig. 2B-D), single-molecule binding behavior at low and high concentrations (Table 1, SI Appendix Figs. S1-S8), TIRF binding on GMPCPP microtubules (Fig. 3B-C), CD and DLS (Fig. 4A), 2D 1H-15N HSQC NMR of full-length Tau (Fig. 4B-D), HSQC of N-terminal peptides (Fig. 4E-F), HSQC in presence of microtubules (Fig. 5A), STD NMR buildup curves and KD determination (Fig. 5B-C)
- **Missing materials affecting confidence** Full SI Appendix content (including Methods details, supplementary figures S1-S9, Movies S1-S6) not provided; raw data and statistical analysis details not provided; exact sample sizes and number of independent replicates for key quantitative comparisons not stated in main text

## Reviewer

- **Overall assessment** This manuscript presents a well-designed and carefully executed study that challenges a prevailing assumption in the Tauopathy field, namely that disease-associated Tau mutations act primarily by reducing microtubule affinity. The combination of TIRF microscopy, pelleting assays, and NMR spectroscopy provides complementary evidence that the R5L mutation has a distinct mechanism: it leaves affinity unchanged but reduces occupancy and disrupts cooperative patch formation. The NMR data localizing the structural change to the N-terminus and demonstrating reduced projection domain-microtubule interaction are compelling. However, several quantitative claims, particularly regarding the magnitude of effects and the mechanistic link between local structural change and patch disruption, would benefit from additional statistical rigor and explicit controls. The study is of high interest to the Tau and microtubule biology communities and has broader implications for understanding how disease mutations can perturb function without altering canonical binding affinity.

- **Who would be interested in the results, and why** Researchers studying Tau biology, microtubule-associated proteins, neurodegeneration, and protein condensation/phase separation. The work is also relevant to those interested in how point mutations can alter protein function through local structural changes without affecting global conformation or canonical binding affinity. The challenge to the prevailing "reduced affinity" model of Tauopathy will be of interest to a broad audience in neuroscience and cell biology.

- **Major strengths**
  1. The study directly challenges a widely held assumption in the field with a well-controlled experimental approach.
  2. The combination of bulk (pelleting, TIRF intensity) and single-molecule (TIRF dynamics) assays provides a comprehensive picture of Tau-microtubule interactions.
  3. The NMR work elegantly localizes the structural effect of the mutation and directly demonstrates reduced projection domain-microtubule interaction.
  4. The use of GMPCPP microtubules as a control condition that does not support patch formation is a thoughtful experimental design that helps dissect the role of patches.
  5. The discussion is balanced and acknowledges alternative mechanisms (e.g., loss of salt bridges with Tau or tubulin) without overclaiming.

- **Major Concerns**

  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** No
  - **Axis** Statistical rigor and quantitative support
  - **Claim pointer** The authors claim a "twofold difference in fluorescence intensity between WT-Tau and R5L-Tau at binding saturation" and that WT-Tau formed "twice as many patches per micrometer" with "~50% more molecules per patch."
  - **Evidence pointer** Fig. 1B, Fig. 2B-C, location not provided for exact statistical values
  - **Concern** The key quantitative claims (twofold intensity difference, twofold patch frequency difference, 50% molecule number difference) are presented without explicit statistical analysis in the main text. It is unclear whether these differences are statistically significant, what the sample sizes are, how many independent experiments were performed, and whether the variability is appropriately represented. The error bars in the figures are mentioned but the statistical tests used and the resulting P values are not stated in the main text.
  - **Why it matters** The central conclusion that R5L reduces occupancy without altering affinity rests on these quantitative comparisons. Without clear statistical support, the reader cannot assess the robustness of the effect, and the magnitude of the reported differences may be overinterpreted.
  - **Resolution test** Provide explicit statistical analysis (test used, P values, effect sizes, confidence intervals) for all key comparisons in Figs. 1B-C, 2B-D, and 3B-C. State sample sizes and number of independent replicates. If the differences are not statistically significant, the conclusions should be tempered accordingly.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Mechanistic link between local structural change and patch disruption
  - **Claim pointer** The authors state that "the decrease in the frequency and density of Tau patches on the microtubule surface observed by TIRF microscopy is due to changes in the local structure of the projection domain upon introduction of the R5L mutation."
  - **Evidence pointer** Fig. 4C-F, Fig. 5A-C, Discussion
  - **Concern** The NMR data demonstrate a local structural change and reduced projection domain-microtubule interaction, and the TIRF data demonstrate reduced patch formation. However, the causal link between these two observations is inferred rather than directly demonstrated. The authors do not provide a mechanistic model for how reduced projection domain-microtubule interaction leads to fewer and smaller patches. Is the projection domain directly involved in inter-Tau interactions within patches? Or does reduced microtubule interaction of the projection domain indirectly affect patch stability? The discussion offers plausible hypotheses (salt bridge disruption) but these are not tested.
  - **Why it matters** The title and central claim of the paper is that the R5L mutation disrupts patch formation by altering local N-terminal structure. Without a direct mechanistic link, the conclusion remains correlative. The field would benefit from a clearer understanding of how the projection domain contributes to patch formation.
  - **Resolution test** Provide additional experiments or analyses that directly test the role of the projection domain in patch formation, such as mutagenesis of residues in the projection domain that are not involved in microtubule binding, or experiments with truncated Tau lacking the projection domain. Alternatively, provide a more detailed structural model supported by data showing how the local change disrupts inter-Tau interactions.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Generalizability of findings to disease-relevant conditions
  - **Claim pointer** The authors conclude that "the mechanism by which the R5L mutation leads to disease is through disruption of physiological Tau function, such as cargo transport."
  - **Evidence pointer** Discussion, no direct experimental evidence in the manuscript
  - **Concern** The manuscript does not include any functional assays (e.g., axon transport, neuronal viability, Tau aggregation) that would directly link the observed biophysical changes to disease pathogenesis. The claim that disruption of Tau patches leads to disease via altered cargo transport is entirely speculative and not supported by data presented in this manuscript.
  - **Why it matters** The title and significance statement frame the work as relevant to understanding disease mechanisms. While the biophysical characterization is valuable, the leap to disease mechanism is not supported by the evidence presented. Overstating the disease relevance could mislead readers and the field.
  - **Resolution test** Either temper the disease-related claims in the discussion to clearly state them as hypotheses requiring further testing, or include functional assays (e.g., motor protein motility assays, cellular models) that directly test the impact of R5L on Tau function.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Interpretation of KD values from STD NMR
  - **Claim pointer** The authors report KD values of 1.3 ± 0.3 and 0.9 ± 0.2 mM for WT-Tau peptide and 3.3 ± 1.5 and 2.7 ± 0.4 mM for R5L-Tau peptide binding to microtubules.
  - **Evidence pointer** Fig. 5C, Methods
  - **Concern** The KD values are in the millimolar range, which is unusually weak for a specific protein-protein interaction. The authors do not discuss whether these values are physiologically relevant or whether the peptide model accurately reflects the behavior of the full-length protein. Additionally, the error bars on the R5L KD values are large (up to 45% of the mean), which may limit the confidence in the reported difference between WT and R5L.
  - **Why it matters** The claim that R5L reduces projection domain-microtubule interaction is based on these KD measurements. If the measurements are not robust or the peptide model is not representative, this key conclusion is weakened.
  - **Resolution test** Provide additional validation of the peptide model, such as competition experiments with full-length Tau, or discuss the limitations of the millimolar KD values. Report confidence intervals for the KD values and discuss whether the difference between WT and R5L is statistically significant given the large error bars.

- **Minor Comments**

  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of figure presentation
  - **Affected element** Fig. 1B
  - **Evidence pointer** Fig. 1B, location not provided
  - **Issue** The binding curves in Fig. 1B appear to show saturation, but it is unclear whether the fitted curves are from a single representative experiment or pooled data. The figure legend does not specify the number of replicates or the fitting model used.
  - **Required correction** Clarify in the figure legend whether the data are from a representative experiment or pooled, and specify the fitting model and the number of replicates.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness of methods
  - **Affected element** Statistical analysis
  - **Evidence pointer** Methods, location not provided
  - **Issue** The Methods section does not include a dedicated statistical analysis subsection describing the tests used, the software, and the criteria for significance.
  - **Required correction** Add a statistical analysis subsection to the Methods detailing all statistical tests used, the software, and the significance thresholds.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interpretation of single-molecule data
  - **Affected element** Table 1
  - **Evidence pointer** Table 1, SI Appendix Figs. S1-S8
  - **Issue** The single-molecule data in Table 1 report static-diffusive equilibrium, diffusion coefficients, and dwell times. It is unclear how many molecules were analyzed per condition and whether the analysis was blinded to the Tau variant.
  - **Required correction** State the number of molecules analyzed per condition and whether the analysis was performed blinded.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Discussion of alternative interpretations
  - **Affected element** Discussion
  - **Evidence pointer** Discussion, location not provided
  - **Issue** The authors do not discuss the possibility that the reduced occupancy of R5L-Tau could be due to altered Tau-Tau interactions on the microtubule surface rather than reduced projection domain-microtubule interaction. The two mechanisms are not mutually exclusive but are not explicitly distinguished.
  - **Required correction** Add a brief discussion of alternative mechanisms and how the current data might distinguish between them.

- **Technical failings that need to be addressed before the case is established**
  1. Lack of explicit statistical analysis for key quantitative comparisons (R1-M1).
  2. The causal link between local structural change and patch disruption is inferred, not demonstrated (R1-M2).
  3. The disease relevance claims extend beyond the data presented (R1-M3).
  4. The robustness of the STD NMR KD measurements needs additional validation (R1-M4).

- **Assessment against Nature-style criteria**
  - **Originality** High. The work challenges a prevailing model and provides a new perspective on how a disease-associated Tau mutation could act. The finding that a mutation can reduce occupancy without altering affinity is conceptually novel.
  - **Scientific importance** High for the Tau and microtubule biology fields. The work has implications for understanding Tau function in health and disease and for the broader concept of how protein condensates on microtubules are regulated. However, the direct disease relevance is not established in this manuscript.
  - **Interdisciplinary readership** Moderate to high. The work bridges biophysics, cell biology, and neuroscience. The NMR and single-molecule approaches will appeal to biophysicists, while the Tau and disease context will attract neuroscientists. The writing is accessible, though some specialized techniques may require background knowledge.
  - **Technical soundness** Generally strong. The experimental design is thoughtful, with appropriate controls (e.g., GMPCPP microtubules). However, the lack of explicit statistical analysis and the reliance on a peptide model for the STD NMR experiments are weaknesses that need to be addressed.
  - **Readability for nonspecialists** Good. The manuscript is clearly written, and the significance statement effectively frames the work for a broad audience. The figures are well-designed, though the main text could benefit from more explicit descriptions of the statistical results.

- **Recommendation posture** Supportive if technical concerns are resolved. The core finding, that R5L reduces occupancy and disrupts patch formation without altering affinity, is well-supported by the data. However, the manuscript would be strengthened by addressing the statistical rigor, providing a more direct mechanistic link, and tempering the disease relevance claims. With these revisions, the work would be a valuable contribution to the field.