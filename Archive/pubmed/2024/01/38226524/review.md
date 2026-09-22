## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors evaluate AlphaFold2 and ESMFold predictions for de novo, random, and conserved proteins from Drosophila, reporting that de novo and random proteins show distinct structural prediction patterns, a positive disorder-pLDDT correlation (opposite to conserved proteins), performance limitations due to low sequence identity, and length-dependent disorder fluctuations in random proteins. They conclude that current predictors offer limited accuracy for such proteins and suggest the positive correlation may indicate conditional folding or transient binding.
- **Visible evidence base** Abstract text only; no quantitative results, statistical analyses, dataset descriptions, or methodological details are provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, dataset composition and filtering criteria, sequence identity thresholds, disorder prediction methodology, statistical tests and significance values, comparison baselines, and any validation or benchmarking details

## Reviewer
- **Overall assessment** The abstract addresses a timely and relevant question regarding the applicability of state-of-the-art structure prediction tools to non-conserved, de novo, and random proteins. The reported observation of an inverted disorder-pLDDT correlation is potentially interesting and could have implications for understanding the structural behavior of young proteins. However, the abstract alone provides insufficient methodological detail and quantitative support to evaluate the robustness of the findings. The conclusions, particularly the speculative interpretation regarding conditional folding, extend beyond what can be assessed from the provided material.
- **Who would be interested in the results, and why** Researchers in protein evolution, de novo gene birth, structural bioinformatics, and computational biology would find these results relevant. The work speaks to the limits of AlphaFold2 and ESMFold for non-conserved sequences, which is of practical concern for those using these tools on orphan or lineage-specific proteins. The disorder-pLDDT correlation finding may also interest biophysicists studying conformational ensembles and transient interactions.
- **Major strengths** The question is well-motivated and addresses a gap in the applicability of widely used prediction tools. The comparison across de novo, random, and conserved proteins provides a useful framework. The observation of a positive disorder-pLDDT correlation in de novo and random proteins, if robust, would be a novel and potentially significant contribution.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not report any quantitative metrics, statistical significance, or effect sizes. The correlation between disorder and pLDDT is described qualitatively without correlation coefficients or confidence intervals. The claim regarding sequence identity effects lacks supporting data. The length-dependent disorder fluctuations are mentioned without specific values or trends. These omissions prevent assessment of the technical soundness of the analysis.
- **Assessment against Nature-style criteria** 
  - Originality: The question of how structure predictors perform on de novo and random proteins is relatively underexplored, and the reported inverted correlation is potentially novel. However, the abstract does not establish how this extends beyond existing benchmarks of AF2 on orphan proteins.
  - Scientific importance: The topic is important for protein evolution and structural biology, but the abstract does not demonstrate broad implications beyond a specific Drosophila dataset.
  - Interdisciplinary readership: The findings could appeal to evolutionary biologists and computational structural biologists, but the abstract is written in a way that assumes familiarity with pLDDT and disorder prediction, limiting accessibility.
  - Technical soundness: Not assessable from the abstract. No methodological details, validation, or statistical rigor are presented.
  - Readability for nonspecialists: The abstract is concise but uses field-specific terms without explanation. The logical flow is clear, but the speculative conclusion is not clearly separated from the empirical findings.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents interesting observations, but the lack of quantitative support and methodological detail means the core claims cannot be evaluated. A supportive posture would require the full manuscript to demonstrate statistical robustness and appropriate controls.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim a positive correlation between disorder and pLDDT for de novo and random proteins, in contrast to a negative correlation for conserved proteins.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract reports this correlation qualitatively without any correlation coefficients, confidence intervals, or statistical tests. It is unclear whether the correlation is weak or strong, consistent across datasets, or driven by outliers. The direction of the correlation is stated, but the magnitude and robustness are not quantified.
- **Why it matters** This is the central novel finding of the study. Without quantitative support, the claim cannot be verified or compared to existing literature. A spurious correlation could arise from dataset composition, sequence length effects, or predictor artifacts, none of which can be ruled out from the abstract.
- **Resolution test** Provide Pearson or Spearman correlation coefficients with p-values for each protein class, along with scatter plots or binned analyses. Show that the correlation holds after controlling for sequence length and sequence identity. Report the number of proteins in each class and the distribution of pLDDT and disorder scores.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the performance of structure predictors for de novo and random proteins is hampered by the lack of sequence identity.
- **Evidence pointer** Abstract, location not provided
- **Concern** No quantitative evidence is provided to support this claim. It is unclear what metric was used to assess performance (e.g., pLDDT, TM-score, RMSD), what threshold of sequence identity was considered, and how the comparison to conserved proteins was made. The claim is plausible given the known dependence of AF2 on evolutionary information, but it is not substantiated here.
- **Why it matters** This claim is central to the conclusion that predictors have limited applicability to de novo and random proteins. Without a clear performance metric and a controlled comparison, the claim is not testable and could be an overgeneralization.
- **Resolution test** Report performance metrics (e.g., median pLDDT, predicted TM-score) for each protein class, stratified by sequence identity bins. Show a statistical comparison between classes, and demonstrate that the performance difference is specifically attributable to sequence identity rather than other sequence features.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility and data availability
- **Claim pointer** The authors state that they investigate structural predictions for de novo and conserved proteins from Drosophila and a dataset of comparable random proteins.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract does not describe the dataset composition, including the number of proteins, the criteria for defining de novo and random proteins, the source of the Drosophila sequences, or how the random proteins were generated to be "comparable." Without this information, the generalizability of the findings is unclear, and the study cannot be reproduced.
- **Why it matters** The validity of the comparison between de novo, random, and conserved proteins depends entirely on the dataset design. If the random proteins are not matched for length, amino acid composition, or other properties, the observed differences could be artifacts.
- **Resolution test** Provide a detailed description of the dataset in the full manuscript, including accession numbers or sequence availability, generation of random sequences, and matching criteria. Include a table summarizing sequence counts, length distributions, and sequence identity levels for each class.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and precision
- **Affected element** Abstract wording
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "fluctuating median predicted disorder among different sequence length quartiles" is vague. It is unclear whether the fluctuation is statistically significant, monotonic, or non-monotonic, and what the magnitude of the fluctuation is.
- **Required correction** Specify the direction and magnitude of the fluctuation, and report whether the differences between quartiles are statistically significant. If the effect is small, state this explicitly.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Concluding statement
- **Evidence pointer** Abstract, location not provided
- **Concern** The final sentence suggests that the positive disorder-pLDDT correlation "could imply a potential for conditional folding and transient binding interactions." This is a speculative interpretation that is not directly supported by the reported data. The abstract does not provide any experimental or functional evidence for such behavior.
- **Required correction** Clearly label this as a hypothesis or speculation, and separate it from the empirical findings. Alternatively, remove it from the abstract if it is not developed in the full manuscript.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability
- **Affected element** Terminology
- **Evidence pointer** Abstract, location not provided
- **Issue** Terms such as "pLDDT" and "de novo proteins" are used without definition. While the target audience may be familiar with these terms, the abstract could benefit from brief clarification to improve accessibility for a broader readership.
- **Required correction** Add a brief parenthetical definition for pLDDT (e.g., predicted local distance difference test) and clarify that de novo proteins are those encoded by lineage-specific or newly emerged genes.

## Risk / unsupported claims
- The positive disorder-pLDDT correlation for de novo and random proteins is unsupported by quantitative data in the abstract.
- The claim that performance is hampered by lack of sequence identity is unsupported by any performance metrics or statistical comparisons.
- The observation of length-dependent disorder fluctuations is reported without specific values or significance testing.
- The interpretation that the positive correlation implies conditional folding and transient binding is speculative and not supported by the presented evidence.
- The generalizability of the findings beyond the specific Drosophila dataset and the random protein generation method is not assessable from the abstract.