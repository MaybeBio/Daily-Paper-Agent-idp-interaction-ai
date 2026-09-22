## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors present SAKE-PP, a spatial-attention equivariant graph neural network that directly regresses interface RMSD (iRMSD) for protein–protein interaction models without native references. The model is trained on docking decoys generated via a hierarchical sampling strategy applied to the PDB-Bind dataset. On the 2024PDB benchmark (176 heterodimers), SAKE-PP reportedly improves AF3 decoy selection by 13.75% (iRMSD statistics) and 12.5% (DockQ scores), outperforms the AF3 ranking score on overlap, hit rate, and correlation, and improves score–iRMSD correlation by 0.4 in zero-shot evaluation of 139 antibody–antigen complexes.
- **Visible evidence base** Abstract text only. No figures, tables, methods details, benchmark definitions, or statistical analyses are available for inspection.
- **Missing materials affecting confidence** Full manuscript, methods section, training and validation data splits, benchmark construction details, baseline definitions, statistical significance tests, hyperparameter settings, model architecture specifics, and all quantitative results with error bars or confidence intervals.

## Reviewer
- **Overall assessment** The abstract describes a potentially useful scoring function for protein–protein interaction model ranking, with a plausible design that couples spatial attention with Laplacian eigenvector orientation. However, the evidence provided in the abstract is insufficient to evaluate the validity, robustness, or generalizability of the reported improvements. Several quantitative claims lack essential context, including baseline definitions, statistical significance, and comparison protocols. The work may be of interest to the structural biology and computational drug design communities, but the current abstract alone does not establish the case.
- **Who would be interested in the results, and why** Structural biologists and computational biophysicists working on protein–protein docking and model scoring would be the primary audience. Researchers developing machine learning scoring functions for biomolecular complexes, as well as those using AlphaFold3 or similar tools for complex structure prediction, would find the plug-and-play scoring function concept attractive. The potential application to antibody–antigen complex ranking is also relevant to therapeutic antibody design groups.
- **Major strengths** The design concept of combining physics-inspired attention with Laplacian eigenvector orientation to couple local interaction forces with global topology is intellectually appealing and potentially novel. The zero-shot evaluation on antibody–antigen complexes is a useful test of generalization. The reported improvements over the AF3 ranking score, if reproducible, would be practically valuable.
- **Major Concerns** The abstract provides insufficient methodological detail to assess the validity of the training and evaluation protocols. The reported improvements lack statistical context, and the baseline comparisons are not clearly defined. The zero-shot improvement of 0.4 in correlation is presented without the baseline value, making the magnitude difficult to interpret.
- **Minor Comments** The abstract would benefit from clearer definitions of the metrics used (overlap, hit rate, correlation). The phrase "physics-inspired" is used but the specific physical constraints incorporated are not described. The hierarchical sampling strategy is mentioned but not explained.
- **Technical failings that need to be addressed before the case is established** The absence of any statistical significance testing, error bars, or confidence intervals for the reported improvements. The lack of a clear description of the baseline AF3 ranking score and how it was computed. The absence of any description of the training/validation split to rule out data leakage between the PDB-Bind training set and the 2024PDB or antibody–antigen test sets.
- **Assessment against Nature-style criteria**  
  *Originality*: The combination of spatial attention with Laplacian eigenvector orientation for PPI scoring appears novel, though the abstract does not provide enough detail to fully assess novelty against existing equivariant graph neural network scoring functions.  
  *Scientific importance*: Reliable PPI model ranking is a recognized bottleneck, and improvements in this area would be scientifically valuable. However, the magnitude and robustness of the reported improvements are not established from the abstract alone.  
  *Interdisciplinary readership*: The work bridges structural biology, machine learning, and drug design, which could attract a broad readership if the claims are substantiated.  
  *Technical soundness*: Cannot be assessed from the abstract. The training strategy, architecture details, and evaluation protocols are not described in sufficient depth.  
  *Readability for nonspecialists*: The abstract is reasonably accessible, though terms such as "Laplacian-eigenvector orientation" and "equivariant graph neural network" may require background knowledge.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents promising results, but the lack of methodological detail and statistical context prevents a supportive recommendation. A full manuscript with detailed methods, benchmark descriptions, and statistical analyses would be required to evaluate the claims properly.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Statistical validity  
- **Claim pointer** "achieving improvements of 13.75% based on iRMSD statistics and 12.5% based on DockQ scores" and "improves the score–iRMSD correlation by 0.4"  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The reported improvements are presented as point estimates without any measure of uncertainty, statistical significance, or confidence intervals. It is unclear whether these improvements are consistent across the benchmark or driven by a subset of cases.  
- **Why it matters** Without statistical context, the reported improvements cannot be distinguished from noise, particularly given the relatively small benchmark sizes (176 heterodimers and 139 antibody–antigen complexes).  
- **Resolution test** Provide per-case distributions, bootstrap confidence intervals, or paired statistical tests (e.g., Wilcoxon signed-rank test) comparing SAKE-PP against the AF3 ranking score.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Baseline definition  
- **Claim pointer** "It consistently outperforms the AF3 ranking score in multiple metrics, including overlap, hit rate, and correlation"  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The AF3 ranking score is referenced as a baseline, but its exact definition, how it was computed, and whether it was used in a comparable manner (e.g., same decoy sets, same normalization) are not described.  
- **Why it matters** A fair comparison requires that the baseline is well-defined and that both methods are evaluated under identical conditions. Without this, the claimed outperformance cannot be verified.  
- **Resolution test** Clearly define the AF3 ranking score, describe how it was obtained for each decoy set, and confirm that identical decoy inputs were used for both methods.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Data leakage and generalization  
- **Claim pointer** "Trained on docking decoys generated through our novel hierarchical sampling strategy applied to PDB-Bind dataset" and "On the 2024PDB benchmark" and "zero-shot evaluation of 139 antibody–antigen complexes"  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The abstract does not describe how the 2024PDB benchmark and the antibody–antigen complexes relate to the PDB-Bind training set. If any of the test complexes or their near-native decoys share sequence or structural similarity with training examples, the reported performance could be inflated.  
- **Why it matters** Generalization to unseen complexes is a core claim of the work. Without a clear description of how sequence and structural redundancy was controlled between training and test sets, the zero-shot claim cannot be assessed.  
- **Resolution test** Describe the redundancy filtering procedure (e.g., sequence identity thresholds, structural similarity cutoffs) applied between the PDB-Bind training set and both test sets, and confirm that no test complex or decoy was used during training.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Metric interpretation  
- **Claim pointer** "improves the score–iRMSD correlation by 0.4"  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The baseline correlation value is not reported, so the absolute improvement of 0.4 cannot be interpreted. A change from 0.2 to 0.6 is very different from a change from 0.5 to 0.9.  
- **Why it matters** The practical significance of the improvement depends on the starting point. Without the baseline value, the claim is ambiguous.  
- **Resolution test** Report the baseline AF3 ranking score correlation alongside the SAKE-PP correlation, and specify which correlation coefficient (e.g., Pearson or Spearman) was used.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Metric definitions  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The terms "overlap" and "hit rate" are used without definition.  
- **Required correction** Define these metrics explicitly, including any thresholds used (e.g., iRMSD cutoff for a "hit").

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Terminology  
- **Affected element** "physics-inspired"  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The abstract claims the model is "physics-inspired" but does not specify which physical principles are incorporated.  
- **Required correction** Briefly state which physical constraints or priors are embedded in the attention mechanism or the loss function.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Hierarchical sampling strategy  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The "novel hierarchical sampling strategy" is mentioned but not described.  
- **Required correction** Provide a brief description of the sampling strategy in the abstract or indicate where full details can be found in the manuscript.

## Risk / unsupported claims
- The claim of "effective optimization and selection of AF3 decoys" is unsupported without details on how optimization was performed and what "effective" means quantitatively.
- The claim of "consistently outperforms" is unsupported without statistical testing or per-metric breakdowns.
- The zero-shot improvement of 0.4 in correlation is uninterpretable without the baseline value.
- The generalizability of the model beyond the tested benchmarks is not established from the abstract alone.
- The claim of "robust, plug-and-play scoring function" is not supported by the evidence presented in the abstract.