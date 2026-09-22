## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion) without supplementary material or figures.
- **Assessment boundary** Evaluation of the manuscript's claims, methodology, and evidence as presented in the provided text. No external data or unpublished materials were consulted.
- **Shared manuscript claim summary** The authors evaluate three protein docking methods (IDP-LZerD, CABS-Dock, AlphaFold-Multimer) on a dataset of 35 intrinsically disordered protein (IDP)-receptor complexes. They claim that all methods identify general binding sites at low resolution, but AlphaFold outperforms the others at intermediate and high-resolution metrics, particularly Fnat, while still falling short in atomic-level interaction modeling (Fhbond, Fhphobe, Fionic).
- **Visible evidence base** Results sections describing Interface Precision/Recall, LRMSD, Fnat, and interaction-based metrics; four visual examples (Figure 3, Figure 5, Figure 6); numerical values for selected targets; dataset construction details in Methods.
- **Missing materials affecting confidence** Supplementary Table 1 (dataset details), all figures (Figures 1-6), and any statistical analysis or error bars. The manuscript text alone does not allow independent verification of quantitative claims or visual comparisons.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question: how well do current docking and structure prediction methods handle intrinsically disordered protein complexes? The multi-level evaluation framework is thoughtful and well-motivated. However, the evidence presented in the text is insufficient to fully support several key claims, particularly regarding the quantitative performance differences between methods. The lack of statistical analysis, incomplete figure descriptions, and reliance on selected examples weaken the case. The work has potential but requires substantial additional analysis and presentation before the conclusions are fully established.
- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein-protein docking, IDP biology, and structure prediction. Developers of docking software and users of AlphaFold for complex prediction would benefit from understanding the strengths and limitations of these tools for IDP systems. The study also has relevance for experimentalists seeking computational methods to model fuzzy or dynamic interactions.
- **Major strengths** 1) The multi-resolution evaluation framework is a clear strength, providing a nuanced view of method performance beyond simple RMSD. 2) The inclusion of three distinct methods (physics-based, coarse-grained, and deep learning) offers a broad comparison. 3) The focus on IDP-receptor complexes addresses an understudied but biologically important class of interactions. 4) The discussion of fuzzy interactions and the potential for hybrid approaches is insightful and forward-looking.
- **Major Concerns** 
  - R1-M1: Lack of statistical analysis and error quantification for performance metrics.
  - R1-M2: Incomplete description of figures, limiting the reader's ability to assess the evidence.
  - R1-M3: The claim that AlphaFold "outperforms" other methods is not fully supported by the presented data, particularly for high-resolution metrics.
  - R1-M4: The dataset construction and potential biases are not adequately discussed.
  - R1-M5: The interaction-based metrics (Fhbond, Fhphobe, Fionic) are only applied to AlphaFold, limiting the comparative value.
- **Minor Comments** 
  - R1-m1: The abstract states "all three methods are able to properly identify the general binding site," but the results show significant variability, especially for CABS-Dock.
  - R1-m2: The description of the IDP-LZerD algorithm is brief and could benefit from more detail on the fragment stitching and scoring.
  - R1-m3: The manuscript would benefit from a table summarizing performance metrics across all methods and targets.
  - R1-m4: The discussion of "fuzzy" interactions is interesting but not directly tested in this study.
  - R1-m5: The choice of 70% threshold for "successful" identification in Figure 2 is arbitrary and not justified.
- **Technical failings that need to be addressed before the case is established** R1-M1 (statistical analysis), R1-M2 (figure completeness), R1-M3 (claim support), R1-M5 (comparative metrics).
- **Assessment against Nature-style criteria** 
  - Originality: Moderate. The multi-level evaluation approach is not entirely novel, but the specific focus on IDP-receptor docking with three diverse methods adds value.
  - Scientific importance: High. IDPs are increasingly recognized as critical in biology and disease, and understanding computational limits for their complexes is important.
  - Interdisciplinary readership: Moderate. The work is primarily of interest to computational biologists; the biological implications are not deeply explored.
  - Technical soundness: Weak. The lack of statistical rigor and incomplete evidence presentation undermine confidence in the conclusions.
  - Readability for nonspecialists: Moderate. The manuscript is generally clear but assumes familiarity with docking metrics and IDP concepts.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript has merit but requires significant revisions, including statistical analysis, complete figure descriptions, and a more balanced comparison of methods, before the claims can be fully supported.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors claim AlphaFold "outperforms" IDP-LZerD and CABS-Dock in intermediate and high-resolution metrics, and that all methods "perform acceptably well" at low resolution.
- **Evidence pointer** Results sections "Intermediate-Resolution Accuracy" and "Atomic Level Interactions"; location not provided for specific data points.
- **Concern** The manuscript reports average values (e.g., average Fnat of 0.78 for AlphaFold) and counts (e.g., 31 targets with LRMSD < 10 Å) without any measure of variance, confidence intervals, or statistical tests. It is impossible to determine whether observed differences between methods are significant or within noise. For example, the claim that AlphaFold outperforms CABS-Dock in Fnat (0.78 vs 0.13) is striking, but no error bars or per-target distributions are shown.
- **Why it matters** Without statistical analysis, the reader cannot assess the reliability or generalizability of the findings. The conclusions may be driven by a few outliers or by systematic biases in the dataset.
- **Resolution test** Provide per-target performance distributions (e.g., box plots or scatter plots) for each metric and method. Include appropriate statistical tests (e.g., paired Wilcoxon signed-rank test) comparing methods across the 35 targets. Report effect sizes and confidence intervals.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The manuscript references Figures 1-6 to support claims about method performance and specific examples (e.g., Figure 3A-D, Figure 5A-C, Figure 6B-D).
- **Evidence pointer** Figures 1-6; location not provided in the text.
- **Concern** The figures are not included in the provided material, and the text descriptions are insufficient to fully understand the data. For example, Figure 2A-D is described as showing "receptor precision and recall" and "ligand precision and recall," but the exact definitions, axes, and data points are unclear. Similarly, Figure 6A is described as a plot comparing Fnat to interaction metrics, but the reader cannot see the data or the magnitude of discrepancies.
- **Why it matters** Figures are central to the evidence. Without them, the claims cannot be independently verified, and the reader cannot judge whether the visual examples are representative or cherry-picked.
- **Resolution test** Include all figures in the manuscript with detailed captions. Ensure each figure clearly shows the data for all 35 targets (or a representative subset with justification). Provide axis labels, legends, and statistical annotations where applicable.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The abstract and discussion state that "AlphaFold was able to outperform the other two methods, particularly in the residue and high-resolution metrics."
- **Evidence pointer** Results sections "Intermediate-Resolution Accuracy" and "Atomic Level Interactions"; location not provided.
- **Concern** While the text reports higher average Fnat for AlphaFold, the high-resolution metrics (Fhbond, Fhphobe, Fionic) are only computed for AlphaFold, not for IDP-LZerD or CABS-Dock. Therefore, the claim of "outperformance" at high resolution is not supported by comparative data. Additionally, the text notes that AlphaFold sometimes places ligands backwards (Figure 5B), which is a significant error not captured by Fnat alone.
- **Why it matters** The central conclusion of the paper is that AlphaFold is superior at higher resolutions. Without comparative high-resolution metrics for all methods, this conclusion is incomplete and potentially misleading.
- **Resolution test** Compute Fhbond, Fhphobe, and Fionic for IDP-LZerD and CABS-Dock models as well. If this is not feasible, clearly state the limitation and adjust the claims accordingly. Discuss the backward placement issue and its impact on the overall assessment.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Dataset bias
- **Claim pointer** The dataset is described as containing 35 IDP-receptor complexes from pepBDB, filtered by resolution, chain length, and single ligand chain.
- **Evidence pointer** Methods section "IDP Dataset"; Supplementary Table 1 (not provided).
- **Concern** The dataset construction is described briefly, but potential biases are not discussed. For example, the requirement for experimental resolution ≤3.0 Å or NMR structures may favor well-ordered complexes, which could bias against fuzzy IDP interactions. The removal of two cases due to covalent binding or globular ligand is mentioned but not justified in detail.
- **Why it matters** Dataset composition directly affects the generalizability of the conclusions. If the dataset is biased toward ordered complexes, the findings may not apply to the broader class of IDP-receptor interactions.
- **Resolution test** Provide a detailed analysis of dataset characteristics, including the distribution of IDP lengths, disorder predictions, and binding site properties. Discuss potential biases and their implications. Consider including a sensitivity analysis with subsets of the data.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Methodological consistency
- **Claim pointer** The authors state that "we evaluated the ability to model high-resolution interactions between the ligand and the receptor" using Fhbond, Fhphobe, and Fionic, but these are only applied to AlphaFold.
- **Evidence pointer** Results section "Atomic Level Interactions"; location not provided.
- **Concern** The rationale for applying high-resolution metrics only to AlphaFold is not clearly explained. If the goal is to compare methods, all should be evaluated with the same metrics. If the goal is to assess AlphaFold's atomic-level accuracy, this should be framed as a separate analysis, not as a comparative result.
- **Why it matters** The inconsistency undermines the comparative nature of the study and makes it difficult to draw conclusions about the relative strengths of the methods.
- **Resolution test** Either compute the high-resolution metrics for all methods or clearly separate the analyses into "comparative evaluation" and "AlphaFold-specific atomic-level assessment." Justify the choice in the Methods.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Claim precision
- **Affected element** Abstract
- **Evidence pointer** Abstract; location not provided.
- **Issue** The abstract states "all three methods are able to properly identify the general binding site," but the results show that CABS-Dock only achieved this for 8 (22.86%) of top-ranked models (Figure 2A). This is a low success rate and does not support "all three methods" performing acceptably.
- **Required correction** Qualify the statement, e.g., "IDP-LZerD and AlphaFold were able to identify the general binding site in most cases, while CABS-Dock showed lower success rates."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Methods section "IDP-LZerD"
- **Evidence pointer** Methods section; location not provided.
- **Issue** The description of IDP-LZerD is brief. The fragment generation, docking, and stitching process is mentioned but not detailed. This makes it difficult to assess the method's novelty or potential limitations.
- **Required correction** Expand the description of IDP-LZerD, including key parameters, scoring function details, and any differences from the original LZerD method.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Results section "Global Positioning of an IDP Ligand on the Receptor Surface"
- **Evidence pointer** Results section; location not provided.
- **Issue** The text reports counts and percentages (e.g., "13 (37.14%)") but does not provide a clear summary table. This makes it difficult for the reader to compare methods across all metrics.
- **Required correction** Add a summary table (e.g., in the main text or supplementary) listing the performance of each method for each metric, with appropriate statistical measures.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion section
- **Evidence pointer** Discussion; location not provided.
- **Issue** The discussion of "fuzzy" interactions is interesting but speculative. The study does not directly test fuzzy interactions, and the dataset may not include many such cases.
- **Required correction** Clearly distinguish between findings from this study and hypotheses about fuzzy interactions. Suggest future work to directly address this.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Methodology
- **Affected element** Methods section "Evaluation Metrics"
- **Evidence pointer** Methods section; location not provided.
- **Issue** The threshold of 5 Å for defining interface residues is used without justification. Different thresholds could affect the results.
- **Required correction** Justify the choice of 5 Å or cite relevant literature. Consider a sensitivity analysis with different thresholds.

## Risk / unsupported claims
- The claim that "all three methods are able to properly identify the general binding site" is not fully supported by the data, particularly for CABS-Dock.
- The claim that AlphaFold "outperforms" other methods at high resolution is unsupported because high-resolution metrics were only computed for AlphaFold.
- The statement that "AlphaFold was able to outperform the other two methods, particularly in the residue and high-resolution metrics" is not fully supported without comparative high-resolution data.
- The discussion of "fuzzy" interactions and the suitability of different methods for such cases is speculative and not directly tested.
- The dataset is described as representative of IDP-receptor complexes, but potential biases (e.g., toward ordered complexes) are not discussed, making the generalizability of the findings uncertain.