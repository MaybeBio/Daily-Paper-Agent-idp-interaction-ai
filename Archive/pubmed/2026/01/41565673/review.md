## Review setup
- **Input scope** Full manuscript text including abstract, main text, methods, and figure legends
- **Assessment boundary** Scientific validity, methodological soundness, claims versus evidence, and suitability for a general interdisciplinary audience
- **Shared manuscript claim summary** The authors present IFUM, a deep neural network that jointly predicts protein folding free energy (ΔG) and the equilibrium ensemble of folded and unfolded states represented as residue-pair distance distributions. They claim that this joint learning improves accuracy over ΔG-only prediction, that IFUM generalizes across protein types, handles complex mutations including indels, and outperforms existing methods in real-world protein engineering and de novo design screening tasks.
- **Visible evidence base** Main text figures 1-4, supplementary figures 1-19, supplementary tables 1-11, methods section, and source data references
- **Missing materials affecting confidence** Source data files, supplementary information details, and code repository contents were not provided for direct verification. The full set of benchmark predictions and statistical analysis details are not fully visible.

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting approach to protein stability prediction by explicitly modeling the unfolded state ensemble, which addresses a recognized limitation in current deep learning methods. The joint prediction of ΔG and equilibrium ensembles is a novel architectural choice. However, the evidence provided has several gaps that prevent full confidence in the claims. The benchmark comparisons are incomplete, the statistical rigor of some analyses is unclear, and the practical application demonstrations rely on small sample sizes. The dependence on input structure quality is acknowledged but not fully characterized. The work has potential for significant impact in protein engineering and design, but the current evidence does not fully establish the superiority of IFUM over existing methods across all claimed scenarios.

- **Who would be interested in the results, and why** Computational protein scientists and bioinformaticians developing or using stability prediction tools would be the primary audience. Protein engineers and synthetic biologists involved in therapeutic protein development, enzyme engineering, and de novo design would find the practical applications relevant. The methodological approach of explicitly modeling unfolded states could interest researchers working on protein folding theory and deep learning architectures for biophysical property prediction. The demonstrated utility in design screening could attract the broader protein design community.

- **Major strengths**
  1. The conceptual framing of explicitly modeling unfolded states is well motivated and addresses a genuine gap in existing methods.
  2. The joint learning of ΔG and equilibrium ensembles is a novel architectural contribution.
  3. The evaluation spans multiple scenarios including point mutations, indels, disordered proteins, and real-world engineering tasks.
  4. The practical demonstrations on protein engineering and de novo design screening show potential utility beyond benchmark performance.
  5. The ablation studies provide insight into the contribution of key components.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that IFUM achieves a PCC of 0.78 and RMSE of 1.16 kcal/mol on the Mega-scale test set, and that this represents accurate ΔG prediction.
- **Evidence pointer** Figure 2a, Results section "IFUM can predict unfolding free energy with a low mean error"
- **Concern** The reported performance metrics are presented without confidence intervals, error bars, or statistical significance testing. The RMSE of 1.16 kcal/mol is substantial given the experimental dynamic range of [-1, 5] kcal/mol, and it is unclear whether this level of error is practically useful for the claimed applications. The comparison to baseline methods in Figure 2b is limited to a single baseline (IFUMbaseline) and does not include a comprehensive comparison to other state-of-the-art ΔG prediction methods beyond ESMtherm. The manuscript does not report whether the improvement over IFUMbaseline is statistically significant.
- **Why it matters** Without statistical rigor, the claimed improvement from unfolded state modeling cannot be distinguished from random variation. The practical utility of the method depends on whether the error level is acceptable for real applications, which is not demonstrated.
- **Resolution test** Provide confidence intervals for all reported metrics, perform statistical significance testing for the improvement over baselines, and include a more comprehensive benchmark against existing ΔG prediction methods.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The claim that IFUM "can accurately predict complex mutational effects like insertions or deletions" and that it outperforms other methods for these mutation types.
- **Evidence pointer** Figure 3a-c, Results section "IFUM can accurately predict ΔΔG for various types of mutants"
- **Concern** The evaluation of indel mutations is limited to the Mega-scale test set, and the comparison to other methods for indels is incomplete. The manuscript states that ThermoMPNN cannot handle indels, but does not provide a thorough comparison to other methods that can. The PCC values for double mutants (0.63) and indels (0.80) are reported without context on what constitutes acceptable performance. The case studies in Figure 3b show PCC values ranging from 0.63 to 0.75, but the sample sizes and statistical significance are not reported. The claim of "accurate" prediction is not supported by a clear threshold or comparison to experimental error.
- **Why it matters** The ability to handle complex mutations is a key differentiator claimed by the authors. If the performance is not rigorously benchmarked against all relevant methods and shown to be statistically superior, this claim is not established.
- **Resolution test** Provide a comprehensive benchmark for indel and double mutant prediction against all applicable methods, report sample sizes and statistical significance for case studies, and define what constitutes "accurate" prediction in this context.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that IFUM "effectively guides real-world design challenges, exhibiting strong correlation with experimental melting temperatures in protein engineering and outperforming AlphaFold-based metrics in de novo design selection."
- **Evidence pointer** Figure 4a-c, Results section "Practical application 1" and "Practical application 2"
- **Concern** The protein engineering demonstrations have very small sample sizes (9 IFN-λ3 variants, 8 IL-10 variants, 6 UGT76G1 variants). The p-values reported (0.005, 0.104, 0.023) indicate that the IL-10 correlation is not statistically significant. The de novo design screening comparison uses AUC values, but the number of sequences in each fold category and the statistical significance of AUC differences are not reported. The comparison to AlphaFold-based metrics is limited to plDDT and does not include other relevant metrics. The claim of "outperforming" is not supported by statistical testing.
- **Why it matters** The practical utility claims are central to the paper's significance. Small sample sizes and lack of statistical testing undermine confidence in these claims. The comparison to existing methods must be comprehensive and statistically rigorous.
- **Resolution test** Increase sample sizes where possible, report confidence intervals for all correlations and AUC values, perform statistical testing for AUC differences, and include a more comprehensive comparison to existing design screening metrics.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The claim that the unfolded state ensemble modeling, based on the Flory random coil model, is responsible for the improved performance.
- **Evidence pointer** Figure 2c, Supplementary Table 3, Results section "IFUM can predict unfolding free energy with a low mean error"
- **Concern** The ablation study comparing IFUM to IFUMbaseline shows a performance difference, but the manuscript does not fully explore alternative explanations for this improvement. The Flory model parameters are taken from literature, and the sensitivity of results to these parameters is not tested. The representation of the unfolded state as a single average distance per residue pair may be an oversimplification that could limit the model's accuracy. The manuscript does not discuss whether the improvement comes specifically from the unfolded state modeling or from other differences between IFUM and IFUMbaseline.
- **Why it matters** The central conceptual contribution is the explicit modeling of unfolded states. If the improvement cannot be definitively attributed to this component, the paper's main claim is weakened.
- **Resolution test** Perform additional ablations that vary the Flory model parameters, test alternative unfolded state representations, and ensure that IFUMbaseline differs only in the absence of unfolded state modeling.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The claim that IFUM is "robust to various protein types" and can handle proteins up to 869 amino acids.
- **Evidence pointer** Figure 2f-g, Results section "IFUM is broadly applicable to various types of proteins"
- **Concern** The evaluation on the CATH dataset shows that a considerable portion of proteins have ΔGpred < 1 kcal/mol, which the authors attribute to context effects. The performance on larger proteins (>200 amino acids) shows a tendency to overestimate stability, which is acknowledged but not fully characterized. The manuscript does not provide a systematic analysis of how performance varies with protein length, fold type, or other properties. The claim of robustness is not supported by a comprehensive analysis of failure modes.
- **Why it matters** Understanding the limitations of the method is essential for users to apply it appropriately. The manuscript acknowledges limitations but does not provide sufficient characterization to guide users.
- **Resolution test** Provide a systematic analysis of performance across protein lengths, fold classes, and other relevant properties. Characterize the conditions under which IFUM is reliable and when it is not.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Figure 1
- **Evidence pointer** Figure 1a-d
- **Issue** The figure is information-dense and the relationship between the different panels is not immediately clear. The schematic in panel a does not clearly show how the unfolded state is incorporated into the architecture.
- **Required correction** Consider simplifying the figure or adding a more explicit flow diagram showing how the unfolded state information enters the model.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods section "Dataset preparation"
- **Evidence pointer** Methods section
- **Issue** The filtering criteria for the Mega-scale dataset are described, but the exact number of sequences remaining after each filtering step is not reported. The rationale for the 0.5 kcal/mol threshold for scrambled sequences is not explained.
- **Required correction** Report the number of sequences at each filtering step and provide a justification for the threshold choice.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods section "IFUM architecture"
- **Evidence pointer** Methods section
- **Issue** The architecture description is brief and lacks details on hyperparameter choices, training duration, and convergence criteria. The number of parameters in the model is not reported.
- **Required correction** Provide a more complete description of the architecture and training procedure, including hyperparameter values and model size.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The discussion of limitations is somewhat scattered and could be more organized. The comparison to other methods in the discussion is brief.
- **Required correction** Consider reorganizing the limitations into a more structured format and expanding the comparison to related work.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Figure 3
- **Evidence pointer** Figure 3a-c
- **Issue** The exclusion of data points with extreme ΔΔG values from visualization is mentioned, but the number of excluded points and their impact on the reported statistics is not clear.
- **Required correction** Report the number of excluded points and show the analysis with and without these exclusions.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract is dense and uses technical terms without definition. The phrase "explicit consideration of unfolded states" is not explained for a general audience.
- **Required correction** Consider adding a brief explanation of why unfolded states matter for stability prediction in the abstract.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods section "Other predictors"
- **Evidence pointer** Methods section
- **Issue** The description of how FoldX and Rosetta were used is brief. The specific protocols and parameters for these methods are not fully described.
- **Required correction** Provide more detail on the exact protocols used for FoldX and Rosetta calculations.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Readability
- **Affected element** Figure 4
- **Evidence pointer** Figure 4a-c
- **Issue** The figure legend does not clearly explain the statistical methods used for the correlations and AUC calculations.
- **Required correction** Add statistical details to the figure legend, including the type of correlation used and how confidence intervals were calculated.

## Risk / unsupported claims
- The claim that IFUM "outperforms AlphaFold-based metrics in de novo design selection" is not fully supported by the evidence presented, as the statistical significance of AUC differences is not reported.
- The claim that IFUM "can accurately predict complex mutational effects like insertions or deletions" is not fully established, as the benchmark for indels is limited and no comparison to other methods capable of handling indels is provided.
- The claim that the improvement from unfolded state modeling is statistically significant is not supported by significance testing.
- The practical utility of IFUM for proteins larger than 200 amino acids is not established, as the manuscript acknowledges a tendency to overestimate stability for such proteins.
- The claim of robustness across protein types is not fully characterized, as the analysis of failure modes is incomplete.
- The performance on the literature dataset (PCC of 0.53) is notably lower than on the Mega-scale test set, and the reasons for this discrepancy are not fully explored.