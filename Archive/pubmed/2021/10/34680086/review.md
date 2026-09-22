## Review setup
- **Input scope** Full manuscript text including abstract, introduction, materials and methods, results, discussion, and conclusions.
- **Assessment boundary** Evaluation of the scientific claims, experimental design, data interpretation, and conclusions as presented in the provided text. No external data or supplementary materials were assessed beyond what is described in the manuscript.
- **Shared manuscript claim summary** The authors report the design and synthesis of nine derivatives of the NUPR1-binding drug ZZW-115, with modifications to the piperazine ring substituent. They report in vitro binding affinities measured by isothermal titration calorimetry (ITC), computational docking and molecular dynamics (MD) simulations, and three cellular assays (nuclear translocation inhibition, sensitization to DNA damage, and cancer cell growth inhibition). The central claim is that improved ligand affinity does not necessarily correlate with improved biological function, suggesting a trade-off between affinity and functional control for intrinsically disordered protein (IDP) targets.
- **Visible evidence base** The manuscript provides ITC-derived dissociation constants (Table 1), computational binding scores from docking and MD (Section 3.1, Figure 2), cellular assay results (Figures 4, 5, 6, Table 2), and synthetic characterization data (NMR, MS, HPLC) for the compounds.
- **Missing materials affecting confidence** Supplementary figures (Figure S1, S2) and scheme (Scheme S1) are referenced but not provided. Raw ITC thermograms beyond representative examples, detailed statistical outputs, and full computational parameters are not included. No structural characterization data (e.g., X-ray or NMR structures of protein-ligand complexes) are presented.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question in IDP drug discovery: whether optimizing binding affinity is sufficient for functional efficacy. The experimental design is logical, and the synthesis of a focused series of derivatives is appropriate. However, the central conclusion that affinity and function are decoupled is based on a limited dataset with several methodological caveats. The computational predictions are acknowledged by the authors to have limited predictive power, and the cellular assays, while relevant, do not directly measure NUPR1 function in a mechanistic way. The manuscript is clearly written and the data are presented transparently, but the strength of the conclusions exceeds what the evidence can support.
- **Who would be interested in the results, and why** Researchers in the fields of drug discovery, particularly those targeting intrinsically disordered proteins, will find this work relevant. The study also has implications for medicinal chemists interested in structure-activity relationships and for cancer biologists studying NUPR1 as a therapeutic target. The finding that affinity does not predict function could inform future screening strategies for IDP-targeting compounds.
- **Major strengths** The study addresses a conceptually important question in IDP drug design. The use of multiple orthogonal techniques (ITC, computational modeling, cellular assays) is commendable. The authors are transparent about the limitations of their computational approach. The synthesis of a focused compound series with systematic structural variation is methodologically sound. The manuscript is well-organized and clearly written.
- **Major Concerns** The central claim of a dissociation between affinity and function is based on a small number of compounds with modest differences in both parameters. The cellular assays measure phenotypic outcomes (nuclear localization, DNA damage foci, cell viability) that are indirect readouts of NUPR1 function and may be influenced by off-target effects. The computational modeling is acknowledged to have limited predictive power, yet it is used to rationalize the experimental results. The lack of a direct mechanistic link between binding affinity and the specific functional outcomes measured weakens the conclusion.
- **Minor Comments** The statistical analysis section is brief and does not specify which tests were used for which comparisons. The manuscript would benefit from a more detailed discussion of the potential off-target effects of the compounds. The choice of cell lines and concentrations for the cellular assays could be better justified. The authors mention "fuzziness" of the binding site but do not provide a quantitative measure of this property.
- **Technical failings that need to be addressed before the case is established** The manuscript does not provide direct evidence that the compounds bind to NUPR1 in cells, nor does it demonstrate that the observed cellular effects are mediated specifically through NUPR1. The ITC experiments were performed with a single protein construct and buffer condition, and the stoichiometry values are not discussed in detail. The computational predictions for the bulkier compounds (ZZW-130, 131, 132) are stated to be unreliable, yet these compounds are included in the biological assays without clear justification.
- **Assessment against Nature-style criteria** Originality: The question of whether affinity optimization is sufficient for IDP-targeting drugs is relatively novel, but the approach is incremental. Scientific importance: The findings could have implications for IDP drug discovery, but the evidence is not yet strong enough to establish a general principle. Interdisciplinary readership: The work bridges chemistry, biophysics, and cell biology, which is appealing, but the technical depth in each area is limited. Technical soundness: The experimental methods are appropriate, but the interpretation is overextended. Readability for nonspecialists: The manuscript is accessible, but the significance of the findings is overstated relative to the data.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript presents an interesting hypothesis but does not provide sufficient evidence to support the central claim that affinity and function are decoupled for NUPR1 inhibitors. The authors should either strengthen the mechanistic link between binding and function or temper their conclusions.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim-evidence mismatch
- **Claim pointer** The authors claim that "small improvements of the compound affinity towards NUPR1, as measured by ITC, did not result in a corresponding improvement in their inhibitory properties and in cellulo functions."
- **Evidence pointer** Section 3.3, Table 1; Section 3.4, Figure 4; Section 3.5, Figure 5; Section 3.6, Figure 6, Table 2
- **Concern** The claim of a dissociation between affinity and function is based on a comparison of ITC-derived Kd values with cellular assay outcomes. However, the range of Kd values across the compounds is narrow (approximately 1.7 to 5 µM), and the differences in cellular outcomes are modest and not consistently quantified. For example, ZZW-130 and ZZW-132 have similar Kd values (1.7 µM), yet they show different effects on nuclear translocation and cell growth. The authors do not provide a statistical comparison of the cellular assay results across compounds, nor do they account for potential differences in cellular uptake, metabolism, or off-target effects.
- **Why it matters** The central conclusion of the paper rests on the assertion that affinity does not predict function. If the differences in cellular outcomes are within experimental noise or are due to factors unrelated to NUPR1 binding, the conclusion is not supported.
- **Resolution test** The authors should provide a quantitative comparison of the cellular assay results (e.g., with error bars and statistical tests) and demonstrate that the differences between compounds are significant. They should also measure intracellular compound concentrations or perform a target engagement assay to confirm that the compounds are acting on NUPR1 in cells.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the protein pockets used to model the binding... have a larger conformational variety (or 'fuzziness') compared to well-defined binding sites" and that "no reliable predictions could be obtained when bulkier chemical moieties were added."
- **Evidence pointer** Section 3.1, Figure 2
- **Concern** The computational modeling is acknowledged to have limited predictive power, yet it is used to rationalize the experimental results. Specifically, the authors use the docking and MD results to explain why certain compounds (e.g., ZZW-142) have improved affinity, while others do not. However, the uncertainties in the scoring function are on the order of 0.1-0.2 kcal/mol, which is comparable to the differences in binding scores reported. The authors do not provide a sensitivity analysis or a validation of the computational predictions against the ITC data.
- **Why it matters** If the computational predictions are not reliable, they cannot be used to support the mechanistic interpretation of the experimental results. The paper's conclusion that "a delicate compromise between favoring ligand affinity and controlling protein function may be required" is partly based on these computational insights.
- **Resolution test** The authors should either provide a more robust computational approach (e.g., enhanced sampling or free energy calculations) or clearly state that the computational results are only hypothesis-generating and not confirmatory. They should also show a direct correlation between the computed binding scores and the experimentally measured Kd values.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental design
- **Claim pointer** The authors claim that the compounds "hinder nuclear translocation of NUPR1" and "sensitize cells against DNA damage mediated by NUPR1."
- **Evidence pointer** Section 3.4, Figure 4; Section 3.5, Figure 5
- **Concern** The cellular assays measure phenotypic outcomes that are indirect readouts of NUPR1 function. Nuclear translocation inhibition is assessed by immunofluorescence, but the authors do not provide a quantitative measure of translocation efficiency (e.g., nuclear-to-cytoplasmic ratio). The DNA damage sensitization assay relies on γH2AX foci counting, but the authors do not specify how many cells were counted or whether the counting was blinded. Furthermore, the authors do not demonstrate that the effects are specific to NUPR1, as they do not use a NUPR1-knockdown or knockout control.
- **Why it matters** Without evidence of target specificity, the observed cellular effects could be due to off-target interactions. This undermines the claim that the compounds are functioning through NUPR1 and that the affinity-function relationship is relevant to NUPR1 biology.
- **Resolution test** The authors should include a NUPR1-knockdown or knockout cell line as a control, or use a competitive binding assay to show that the compounds specifically engage NUPR1 in cells. They should also provide quantitative data for the immunofluorescence and foci counting assays.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Section 2.10, Statistics
- **Evidence pointer** Section 2.10
- **Issue** The statistics section states that "statistical analyses were performed by using the unpaired two-tailed Student t test or one-way ANOVA with Tukey's post hoc test," but it does not specify which test was used for which comparison or how many replicates were performed.
- **Required correction** Provide a detailed description of the statistical methods, including the number of replicates, the specific tests used for each comparison, and the criteria for significance.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Section 3.3, Table 1
- **Evidence pointer** Section 3.3, Table 1
- **Issue** The Kd values in Table 1 are presented without error bars or confidence intervals. The authors state that "experiments were performed in replicate," but the variability is not shown.
- **Required correction** Include the standard deviation or standard error for each Kd value, and specify the number of independent experiments.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Mechanistic interpretation
- **Affected element** Section 4, Discussion
- **Evidence pointer** Section 4
- **Issue** The authors propose that "a compound binding with a high affinity may freeze the inherent internal flexibility of NUPR1, impacting its activity in other ways." This is a plausible hypothesis, but it is not directly tested in the manuscript.
- **Required correction** Either provide experimental evidence to support this hypothesis (e.g., conformational dynamics measurements) or clearly label it as a speculative explanation.

## Risk / unsupported claims
- The claim that "the best drug is not necessarily the best binder" for IDPs is not fully supported by the data, as the correlation between affinity and function is not systematically analyzed.
- The statement that "no reliable predictions could be obtained when bulkier chemical moieties were added" is an admission of a limitation, but the authors still use the computational results to interpret the experimental data for these compounds.
- The suggestion that "a delicate compromise between favoring ligand affinity and controlling protein function may be required" is presented as a general principle, but it is based on a single protein and a small series of compounds.
- The claim that the compounds "hinder nuclear translocation of NUPR1" is based on qualitative immunofluorescence data without quantitative analysis or target specificity controls.