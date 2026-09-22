## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, methods, data availability, author contributions, acknowledgements)
- **Assessment boundary** Scientific content, methodological soundness, validity of claims, and completeness of evidence as presented in the provided manuscript
- **Shared manuscript claim summary** The authors present a computational pipeline combining a random forest classifier (DMI predictor) with AlphaFold structural modelling to identify and characterize short linear motif (SLiM)-mediated protein-protein interactions in intrinsically disordered regions, and use this to predict deleterious effects of missense variants, including uncertain variants that state-of-the-art tools like AlphaMissense classify as benign.
- **Visible evidence base** Abstract, Introduction, Results (partial, with figure references), Methods, Data and Code Availability, Author Contributions, Acknowledgements
- **Missing materials affecting confidence** Figures and Extended Data figures are referenced but not provided; supplementary tables (S1-S10) and datasets (S1-S3) are referenced but not provided; no quantitative results, performance metrics beyond AUC/AP, or detailed experimental outcomes are visible

## Reviewer
- **Overall assessment** This manuscript addresses an important gap in variant effect prediction by focusing on intrinsically disordered protein regions, which are poorly handled by existing tools. The combination of a DMI predictor with AlphaFold structural modelling is a sensible and potentially powerful approach. However, the manuscript as provided is incomplete: all figures, extended data, and supplementary materials are missing, making it impossible to evaluate the core claims quantitatively. The methodological description is detailed and suggests rigorous work, but the visible evidence is insufficient to establish the central claims of the paper.
- **Who would be interested in the results, and why** Researchers in human genetics, variant interpretation, and precision medicine would be interested, as the work addresses the challenge of interpreting variants of uncertain significance in disordered regions. Computational biologists developing variant effect predictors and structural biologists using AlphaFold for interaction modelling would also find the approach relevant. Clinicians and diagnostic laboratories dealing with VUS interpretation in rare disease settings may benefit from improved tools for disordered regions.
- **Major strengths** The manuscript identifies a clear and important problem: the poor performance of variant effect predictors in intrinsically disordered regions. The approach of combining motif prediction with AlphaFold structural modelling is innovative and addresses a real gap. The authors demonstrate awareness of limitations, such as the failure to predict a known degron in MYD88 due to restrictive motif definitions. The experimental validation strategy using BRET titration is appropriate and rigorous. The inclusion of edgetic effects and multivalency considerations shows biological sophistication.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (missing figures and data), R1-M2 (unverifiable performance claims), R1-M3 (incomplete experimental validation details), R1-M4 (unclear generalizability)
- **Assessment against Nature-style criteria** Originality: The approach of combining motif prediction with AlphaFold for variant effect prediction in disordered regions is novel and distinct from existing tools. Scientific importance: The problem addressed is significant, given the high proportion of VUS in disordered regions and the limitations of current predictors. Interdisciplinary readership: The work bridges computational biology, structural biology, and clinical genetics, which could attract broad interest. Technical soundness: The methods described are generally sound, but the missing evidence prevents full assessment. Readability for nonspecialists: The manuscript is written clearly, with appropriate context for the problem, though some technical sections assume familiarity with the tools used.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript shows promise and the approach is potentially valuable, but the missing figures, extended data, and supplementary materials prevent evaluation of the core claims. A revised submission with complete evidence would be needed to assess whether the claims are supported.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The manuscript claims successful prediction and experimental validation of multiple DMIs and deleterious variant effects, but all supporting figures, extended data, and supplementary tables are referenced without being provided.
- **Evidence pointer** Figures 1-5, Extended Data Figures 1-3, Tables S1-S10, Datasets S1-S3 (all referenced but not provided)
- **Concern** The manuscript cannot be evaluated without the figures and supplementary materials. Key claims about DMI prediction performance (AUC=0.94, AP=0.93), the distribution of variants in disordered regions, structural models, and experimental validation results are all presented through references to missing materials. This is a fundamental barrier to assessment.
- **Why it matters** The central claims of the paper, including the number of validated DMIs, the accuracy of predictions, and the specific variant effects, cannot be verified without the visual and tabular evidence. The reader cannot assess whether the conclusions follow from the data.
- **Resolution test** Provide all figures, extended data, and supplementary materials in the revised submission. The claims should be traceable to specific data points in these materials.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Performance validation
- **Claim pointer** The DMI predictor is claimed to achieve high accuracy (AUC=0.94, AP=0.93), and the structural modelling approach is claimed to enable reliable prediction of deleterious effects for 1,187 uncertain variants.
- **Evidence pointer** Results section, Figure 1c-d, Extended Data Figure 1b (referenced but not provided)
- **Concern** The performance metrics for the DMI predictor are presented without details on the training and test set compositions, cross-validation procedures, or comparison to baseline methods. The claim that 1,187 uncertain variants can be reliably predicted as deleterious is a strong claim that requires detailed supporting evidence, including the distribution of predictions, confidence intervals, and any independent validation.
- **Why it matters** Without understanding how the predictor was trained and evaluated, the reader cannot assess whether the reported accuracy is robust or overfitted. The claim of reliable prediction for 1,187 variants is central to the paper's contribution and must be supported by rigorous evidence.
- **Resolution test** Provide detailed performance evaluation, including cross-validation results, precision-recall curves, comparison to existing methods, and a clear description of how the 1,187 predictions were derived and validated.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation
- **Claim pointer** The manuscript claims extensive experimental validation of predicted DMIs and variant effects using BRET titration, including validation of six new DMIs and eleven uncertain variants.
- **Evidence pointer** Results section, Figures 2-3, Extended Data Figure 2 (referenced but not provided)
- **Concern** The experimental validation section is described only in text. The specific BRET results, including titration curves, calculated BRET50 and maxBRET values, statistical comparisons, and the criteria for determining "disruptive" effects, are not visible. The claim that eleven uncertain variants are deleterious requires clear experimental evidence for each variant.
- **Why it matters** Experimental validation is the cornerstone of this paper's contribution. Without the actual data, the reader cannot assess whether the validation is convincing, whether the effect sizes are meaningful, or whether the conclusions about specific variants are justified.
- **Resolution test** Provide all BRET titration data, including raw curves, fitted parameters, statistical tests, and a clear summary of which variants were tested and their effects.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The manuscript claims that the approach provides "a clear avenue towards its system-wide implementation" for variant effect prediction in disordered regions.
- **Evidence pointer** Abstract, Discussion
- **Concern** The manuscript demonstrates the approach on a limited set of examples. The claim of system-wide implementation is ambitious and requires evidence that the approach scales, that the DMI predictor generalizes beyond the training data, and that the structural modelling pipeline can be applied at scale. No such evidence is presented in the visible text.
- **Why it matters** The broader impact of the work depends on its scalability and generalizability. Without evidence that the approach can be applied genome-wide, the claim of system-wide implementation remains speculative.
- **Resolution test** Provide a discussion of scalability, potential limitations, and any preliminary evidence of genome-wide applicability, or temper the claim to match the demonstrated scope.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods, DMI predictor development
- **Evidence pointer** Methods section, "DMI predictor development"
- **Issue** The description of the random forest model training mentions four versions of random reference sets (RRSv1-v4) with different sampling strategies, but the rationale for testing these different versions and the criteria for selecting RRSv4 as the best are not explained in the visible text.
- **Required correction** Briefly explain why different RRS versions were tested and what specific performance differences led to the selection of RRSv4.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, BRET assay
- **Evidence pointer** Methods section, "BRET assay"
- **Issue** The BRET assay description mentions that "student's T-test was applied" for comparing wildtype and mutant BRET50 values, but the number of biological replicates, the threshold for significance, and how multiple testing was handled are not specified.
- **Required correction** Specify the number of biological replicates, the significance threshold used, and whether any correction for multiple testing was applied.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results, "Experimental assessment of variant effects"
- **Evidence pointer** Results section, Figure 3 (referenced but not provided)
- **Issue** The text states that the uncertain variant R178H in DMRTB1 and V8M in FAM167A "strongly perturbed binding," but the magnitude of the effect and the comparison to controls are not described in the text.
- **Required correction** Provide quantitative details of the effect sizes in the text, such as fold-change in BRET50 or maxBRET relative to wildtype.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, "Identification of missense variants in motif-mediated protein interfaces"
- **Evidence pointer** Results section, Figure 1h (referenced but not provided)
- **Issue** The text mentions "known and putative disease mechanisms involving mutated motifs" with examples, but the full set of pathogenic variants overlapping with motifs is not enumerated in the visible text.
- **Required correction** Provide a summary table or list of all pathogenic variants found in motifs, with their associated diseases and proposed mechanisms.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract, Introduction
- **Evidence pointer** Abstract, Introduction
- **Issue** The term "uncertain variants" is used throughout, but the standard clinical term is "variants of uncertain significance" (VUS). The abbreviation VUS is not introduced.
- **Required correction** Use the standard term "variants of uncertain significance (VUS)" at first mention and consider using the abbreviation consistently.

## Risk / unsupported claims
- The claim that 1,187 uncertain variants in disordered regions can be reliably predicted as deleterious is unsupported without the underlying prediction data and validation.
- The claim that AlphaMissense evaluates most motif interface variants as benign is presented without quantitative comparison data.
- The claim that the approach provides "a clear avenue towards its system-wide implementation" is speculative without evidence of scalability.
- The specific number of experimentally validated DMIs (six new) and variant effects (eleven uncertain variants) cannot be verified without the experimental data.
- The claim that the DMI predictor achieves AUC=0.94 and AP=0.93 is unverifiable without details on the evaluation procedure and test set.
- The statement that "37% of all annotated missense variants reside in 25% of the proteome that is intrinsically disordered" is presented without citation or supporting analysis in the visible text.