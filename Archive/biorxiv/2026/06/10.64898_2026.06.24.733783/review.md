## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions, footnotes)
- **Assessment boundary** Scientific claims, methodology, dataset construction, statistical inference, and interpretation as presented in the provided text
- **Shared manuscript claim summary** The authors argue that performance inconsistencies among IDR protein-binding site predictors across benchmark datasets stem primarily from a systematic selection bias: literature-based annotations (DisProt) capture highly disordered binding sites, while PDB-derived annotations capture less disordered ones. They propose that this "hidden disorder divide" explains why predictors trained on DisProt data perform well on CAID benchmarks but poorly on PDB-derived datasets, and vice versa.
- **Visible evidence base** Abstract, Sections 1–8, Table 1, Figures 1–4, references to Supplementary Notes 1–2, Supplementary Tables 1–7, Supplementary Figures 1–2
- **Missing materials affecting confidence** Supplementary figures and tables (referenced but not provided), full methodological details for CNN architecture and training, exact dataset statistics, per-predictor prediction protocols, and code repository contents

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important problem in the field of IDR binding site prediction: the systematic inconsistency of predictor performance across benchmark datasets. The authors propose a novel explanation—a selection bias based on intrinsic disorder propensity—and support it with a combination of existing predictor evaluations, controlled CNN experiments, and feature analyses. The central claim is plausible and potentially impactful. However, the evidence as presented is incomplete in several respects. The reliance on referenced supplementary materials that are not visible, the limited description of the CNN training protocol, and the absence of statistical significance testing for key comparisons weaken the current case. The manuscript would benefit from clearer presentation of the controlled experiments and a more rigorous treatment of alternative explanations.
- **Who would be interested in the results, and why** Researchers developing computational predictors for IDR function, particularly those working on binding site prediction, disorder prediction, and benchmark design. The findings are also relevant to experimentalists who use these predictors to prioritize candidate interaction sites, as the results imply that predictor choice should be informed by the disorder propensity of the target region. The diagnostic methodology (control models, class-specific residue merging) may interest methodologists in the broader protein function prediction community.
- **Major strengths** 1. The manuscript identifies a previously underappreciated source of benchmark inconsistency and provides a coherent, mechanistically plausible explanation. 2. The use of controlled CNN models with identical architecture and features is a strong design choice for isolating dataset effects from model effects. 3. The inclusion of multiple independent test sets (CAID1u, CAID2&3u, DBs) strengthens the generalizability of the observations. 4. The analysis of ANCHOR-2, a biophysics-based predictor, provides an elegant natural experiment that supports the central hypothesis.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** Originality: The "hidden disorder divide" concept is novel and reframes a known problem in a new light. Scientific importance: The findings have direct implications for benchmark design and predictor training, which are central to progress in this field. Interdisciplinary readership: The topic is of interest to computational biologists, structural biologists, and experimentalists studying IDR function, though the presentation is somewhat specialized. Technical soundness: The core experimental design is sound, but the incomplete reporting of methods and statistics limits the current assessment. Readability for nonspecialists: The manuscript is generally clear, but the heavy reliance on supplementary materials and the density of acronyms may hinder accessibility.
- **Recommendation posture** Supportive if technical concerns are resolved. The central hypothesis is compelling and the experimental approach is appropriate, but the current evidence base is incomplete. The authors should provide the missing supplementary materials, add statistical rigor, and clarify the CNN training protocol before the case is fully established.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The manuscript claims that performance differences between predictor groups across datasets are substantial and systematic (e.g., "average ~32 AUC points" for Group A on CAID2&3uh vs. DBsh).
- **Evidence pointer** Table 1, Table 2, Figure 2, Supplementary Table 3
- **Concern** The manuscript reports AUC differences between datasets and predictor groups but does not provide confidence intervals, standard errors, or statistical tests for these differences. Given the acknowledged stochastic variability in CNN training (Section 3), it is unclear whether the reported differences are statistically significant or could arise from random variation. The violin plots in Figure 2 show distributions, but no formal comparison is made.
- **Why it matters** Without statistical significance testing, the central claim that dataset composition drives performance differences cannot be distinguished from noise, particularly for the smaller effect sizes observed in some comparisons.
- **Resolution test** Provide confidence intervals or bootstrap estimates for all reported AUC differences, and perform appropriate statistical tests (e.g., paired or unpaired tests as appropriate) for the key comparisons in Tables 1 and 2.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency
- **Claim pointer** The manuscript states that "we constructed a convolutional neural network comprising three convolutional and two fully connected layers, based on the IPA predictors and utilizing the same input features" (Section 3).
- **Evidence pointer** Section 3, Supplementary Note 2
- **Concern** The description of the CNN architecture and training protocol is insufficient for replication. Key details are missing, including the specific input features, hyperparameter values, optimization algorithm, learning rate schedule, batch size, number of epochs, and the exact procedure for selecting the 30th-highest AUC model. The reference to Supplementary Note 2 does not resolve this, as the note is not provided.
- **Why it matters** The controlled CNN experiments are central to the claim that dataset properties, not model architecture, drive performance differences. Without full methodological transparency, the results cannot be independently verified or reproduced.
- **Resolution test** Provide a complete description of the CNN architecture, input features, training procedure, and model selection criteria in the main text or a fully accessible supplementary note.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The manuscript references multiple supplementary tables and figures that are essential for evaluating the claims (e.g., Supplementary Tables 1–7, Supplementary Figures 1–2).
- **Evidence pointer** Sections 2–6, Supplementary Tables 1–7, Supplementary Figures 1–2
- **Concern** The supplementary materials are referenced extensively but are not provided in the submitted manuscript. This includes dataset statistics (Supplementary Table 1), full AUC results (Supplementary Tables 2–3), class-specific analyses (Supplementary Tables 5–7), and feature distribution plots (Supplementary Figure 2). Without these materials, the claims cannot be fully evaluated.
- **Why it matters** The main text provides only a summary of the results, and the supplementary materials contain critical details that support or qualify the central claims. Their absence prevents a complete assessment of the evidence.
- **Resolution test** Provide all referenced supplementary materials in the revised submission.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Confounding variables
- **Claim pointer** The manuscript concludes that "disorderness is the main feature that influences IDR-protein binding computational prediction tools" (Section 6.2).
- **Evidence pointer** Section 6, Supplementary Figure 2, Table 4, Figure 4
- **Concern** The analysis of disorder propensity as the primary driver relies on correlational evidence. The manuscript does not adequately rule out other potential confounders, such as differences in annotation quality, sequence redundancy, binding partner type, or functional class of binding sites between DisProt and PDB-derived datasets. The class-merging experiments (Section 4) address class composition but not these other potential differences.
- **Why it matters** If other factors correlate with the disorder divide, the causal claim that disorder propensity is the dominant driver may be overstated. The manuscript's conclusion has direct implications for how future benchmarks should be designed, so the causal interpretation must be well supported.
- **Resolution test** Perform additional analyses that control for potential confounders (e.g., matching on binding site length, sequence redundancy, or functional annotation) or explicitly test alternative explanations.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2, predictor grouping
- **Evidence pointer** Section 2, Table 1
- **Issue** The assignment of predictors to Groups A, B, and C is described in the text, but the rationale for the grouping criteria (e.g., training data source) could be more explicit. The reader must infer the basis for the grouping from the descriptions of each predictor.
- **Required correction** Add a brief statement in Section 2 explicitly defining the grouping criteria (e.g., training data source, architecture type) and how each predictor was assigned.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Section 3, CNN training
- **Evidence pointer** Section 3, Figure 2
- **Issue** The selection of the 30th-highest AUC model is described, but the rationale for this specific rank is not explained. The choice appears arbitrary.
- **Required correction** Provide a brief justification for selecting the 30th rank, or state that it was chosen to avoid overfitting the validation set and to represent a typical model.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Section 5, binding site size analysis
- **Evidence pointer** Section 5, Table 3, Figure 3
- **Issue** The analysis of binding site size uses a threshold of 70 amino acids, but the manuscript does not discuss whether the results are sensitive to this threshold choice.
- **Required correction** Add a sensitivity analysis using alternative thresholds (e.g., 30, 50, 100 amino acids) or discuss why the 70-residue threshold is appropriate.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 7, Discussion
- **Evidence pointer** Section 7
- **Issue** The discussion of practical implications is brief and does not fully explore the consequences of the findings for existing predictors or for the interpretation of previously published benchmark results.
- **Required correction** Expand the discussion to address how the "hidden disorder divide" affects the interpretation of prior CAID results and what specific changes to benchmark design are recommended.

## Risk / unsupported claims
- The claim that "disorderness is the main feature that influences IDR-protein binding computational prediction tools" (Section 6.2) is supported by correlational evidence but not by causal analysis. The manuscript does not fully rule out alternative explanations.
- The claim that "binding-site length and sequence conservation play only minor or negligible roles" (Abstract) is based on analyses that are not fully described in the main text and rely on supplementary materials that are not provided.
- The claim that the "diagnostic techniques introduced here could prove valuable beyond the specific application examined in this study" (Abstract) is speculative and not supported by evidence in the manuscript.
- The performance differences between predictor groups are reported without statistical significance testing, making the magnitude of the effects uncertain.
- The manuscript's conclusion that predictors "generalize poorly" across the two categories of binding sites is based on AUC comparisons, but the practical implications for real-world use are not quantified (e.g., precision-recall trade-offs, calibration).