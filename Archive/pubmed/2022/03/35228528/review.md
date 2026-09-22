## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, materials and methods, and supplementary information list.
- **Assessment boundary** Scientific validity, methodological soundness, reproducibility, and support of claims by the provided evidence. No assessment of editorial fit or publication decision.
- **Shared manuscript claim summary** The authors present an unsupervised deep learning strategy based on N-gram modeling of intrinsically disordered regions (IDRs) from 171 osteogenesis-related proteins to generate candidate oligopeptides. One pentapeptide, AIB5P, is reported to promote osteogenesis in vitro and in vivo through binding to integrin α5 and activating FAK signaling, with therapeutic effects in mouse models of osteoporosis, fracture, and implant osseointegration.
- **Visible evidence base** Results sections describing in vitro osteogenic differentiation assays, in vivo bone formation analyses, micro-CT, histology, immunohistochemistry, pulldown/mass spectrometry, western blotting, and siRNA knockdown experiments. Materials and methods sections describing the deep learning model, cell culture, animal models, and statistical analyses.
- **Missing materials affecting confidence** Supplementary figures and tables (Figure S1–S6, Tables S1–S4) are referenced but not provided. Raw data, model training details, hyperparameters, and code are not included. Detailed statistical outputs and effect sizes for several comparisons are not reported in the text.

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting approach that applies unsupervised deep learning to IDR sequences for oligopeptide discovery. The in vitro and in vivo osteogenic effects of AIB5P are described with a plausible mechanistic pathway involving integrin α5 and FAK signaling. However, several technical aspects require clarification and additional evidence before the central claims can be considered fully established. The deep learning methodology is described at a high level, and the validation of the model's predictive utility is limited. The mechanistic evidence, while suggestive, relies on a single pulldown experiment and siRNA knockdown without comprehensive controls. The therapeutic claims in disease models are supported by quantitative data, but the absence of dose-response analyses and long-term safety data tempers the strength of these conclusions.
- **Who would be interested in the results, and why** Researchers in peptide drug discovery, computational biology, and bone biology would find this work of interest. The approach of using IDR-derived semantic patterns for oligopeptide generation could be applicable to other biological processes. Clinicians and translational researchers focused on osteoporosis, fracture healing, and implant osseointegration may also be interested in the potential therapeutic applications of AIB5P.
- **Major strengths** The study addresses a significant challenge in oligopeptide drug development by proposing a novel data source (IDRs) and an unsupervised learning approach. The workflow from computational generation to in vitro screening and in vivo validation is comprehensive. The identification of integrin α5 as a target and the FAK signaling pathway provides a mechanistic basis for the observed effects. The use of multiple animal models strengthens the translational relevance of the findings.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (model validation), R1-M2 (mechanistic evidence), R1-M3 (dose-response and controls), R1-M4 (statistical reporting).
- **Assessment against Nature-style criteria**  
  *Originality*: The concept of using IDRs from process-specific proteins as a training dataset for unsupervised deep learning to generate functional oligopeptides is novel and represents a creative departure from structure-based or sequence-feature-based approaches.  
  *Scientific importance*: If the approach is generalizable, it could address a bottleneck in peptide drug discovery. The identification of a short peptide with osteogenic activity and a defined mechanism has potential translational value. However, the importance is contingent on the robustness of the model and the specificity of the mechanism.  
  *Interdisciplinary readership*: The work bridges computational biology, peptide chemistry, and bone biology. The findings would appeal to readers across these disciplines, though the depth of each component may limit accessibility for nonspecialists in any single field.  
  *Technical soundness*: The in vitro and in vivo experiments are generally well designed, but the deep learning methodology lacks sufficient detail for reproducibility, and the mechanistic studies require additional controls. The statistical analyses are appropriate but underreported in several instances.  
  *Readability for nonspecialists*: The manuscript is clearly written and the figures are referenced appropriately. However, the deep learning section may be challenging for readers without computational background, and the methods section assumes familiarity with specific techniques.

- **Recommendation posture** Supportive if technical concerns are resolved. The core concept is promising and the experimental data are largely consistent with the claims, but the deep learning methodology requires more rigorous validation and the mechanistic evidence needs additional support before the case is fully established.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of the deep learning methodology
- **Claim pointer** The authors claim that the N-gram model learned semantic patterns from IDRs of 171 osteogenic proteins and generated functional oligopeptides, with AIB5P showing strong osteogenic activity.
- **Evidence pointer** Results section "A deep learning-based strategy to screen for functional oligopeptides"; Materials and methods "Functional peptide learning using a deep neural network"
- **Concern** The description of the deep learning model is insufficient to evaluate its validity or reproducibility. The N-gram model architecture, training procedure, hyperparameters, and the specific implementation of the Monte Carlo simulation are not described in adequate detail. The authors do not provide information on how the model was validated internally (e.g., perplexity, held-out data) or how the generated oligopeptides were ranked and selected. The claim that the model "learned a semantic pattern" is not supported by any quantitative evaluation of the learned representations. Additionally, the comparison between IDR-derived and full-length-sequence-derived oligopeptides (mentioned in the Discussion) is not shown in the results, making it impossible to assess the claimed advantage of using IDRs.
- **Why it matters** The central premise of the manuscript is that the deep learning approach is responsible for the discovery of AIB5P. Without adequate model description and validation, the reproducibility of the method is questionable, and the causal link between the model and the identified peptide cannot be established. This undermines the generalizability claim of the approach.
- **Resolution test** Provide a detailed description of the model architecture, training data, hyperparameters, and Monte Carlo simulation parameters. Include internal validation metrics (e.g., loss curves, perplexity) and a comparison of generated peptides from IDR versus non-IDR training sets. Ideally, provide code or a repository for reproducibility.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic evidence
- **Claim pointer** The authors claim that AIB5P promotes osteogenesis by binding to integrin α5 and activating FAK signaling.
- **Evidence pointer** Results section "AIB5P interacts with integrin α5 to promote osteogenesis"; Figure 6
- **Concern** The pulldown/mass spectrometry experiment identified integrin α5 as a putative interactor, but the evidence for direct binding is indirect. The western blot in Figure 6c shows that AIB5P interacts with Itga5 but not with other integrins, yet the experimental conditions (e.g., concentrations, specificity controls, competition assays) are not described. The siRNA knockdown experiments demonstrate that Itga5 is required for AIB5P-mediated osteogenesis, but this does not prove direct binding. The FAK signaling data (Figure 6h) show increased phosphorylation, but the time course and dose-response are not provided. The inhibitor experiment (Figure 6i, j) uses a single concentration of PF-573228 without demonstrating specificity for FAK over other kinases.
- **Why it matters** The mechanistic claim is a key part of the manuscript's contribution. If the interaction is not direct or if the signaling pathway is not specific, the proposed mechanism may be incorrect, which would affect the interpretation of the therapeutic effects and the generalizability of the approach.
- **Resolution test** Provide additional evidence for direct binding, such as surface plasmon resonance, isothermal titration calorimetry, or a competition assay with a known integrin α5 ligand. Include dose-response and time-course experiments for FAK phosphorylation. Use a more specific FAK inhibitor or genetic knockout to confirm the pathway. Provide details on the pulldown conditions and include appropriate negative controls.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Dose-response and experimental controls
- **Claim pointer** The authors claim that AIB5P has strong bone-formation-promoting effects in multiple mouse models at a dose of 100 μg·kg⁻¹ every 3 days.
- **Evidence pointer** Results sections "AIB5P promotes osteogenic differentiation of BMSCs in vitro and in vivo" and "AIB5P enhances bone formation in vivo"; Figures 3, 4, 5
- **Concern** The in vivo studies use a single dose of AIB5P (100 μg·kg⁻¹) without a dose-response analysis. The positive control (PTH) is used only in the osteoporosis model, not in the fracture or implant models. The vehicle control is described, but the composition of the vehicle is not specified. The duration of treatment varies across models (1.5 months for osteoporosis and wild-type, 3 weeks for fracture and implant), and the rationale for these differences is not provided. The sample sizes are stated as n=6, but the power calculation is not reported.
- **Why it matters** A single-dose study limits the interpretation of the therapeutic window and the potency of AIB5P. Without dose-response data, it is unclear whether the observed effects are specific to the chosen dose or whether lower doses would be equally effective. The lack of consistent positive controls across models makes it difficult to benchmark the efficacy of AIB5P against established treatments.
- **Resolution test** Include a dose-response study (e.g., 10, 50, 100, 200 μg·kg⁻¹) in at least one in vivo model. Use PTH or another established osteogenic agent as a positive control in all models. Specify the vehicle composition and provide justification for the treatment duration in each model. Report power calculations or justify the sample size.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical reporting and data availability
- **Claim pointer** The authors report significant increases in bone formation parameters, osteogenic marker expression, and bone mass in multiple experimental settings.
- **Evidence pointer** Figures 3, 4, 5; Materials and methods "Statistics"
- **Concern** The statistical methods are described, but the results sections do not consistently report exact p-values, effect sizes, or confidence intervals. For several comparisons, only asterisks indicating significance levels are shown in the figures, without corresponding numerical values in the text. The number of independent experiments for in vitro studies is not consistently stated. The supplementary tables and figures, which likely contain additional data, are not provided for review.
- **Why it matters** Transparent and complete statistical reporting is essential for evaluating the robustness of the findings. Without exact p-values and effect sizes, readers cannot assess the magnitude of the observed effects or the precision of the estimates. The absence of supplementary data limits the ability to verify the claims.
- **Resolution test** Report exact p-values, effect sizes, and confidence intervals for all key comparisons. State the number of independent experiments for each in vitro assay. Provide the supplementary materials for review.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of model description
- **Affected element** Materials and methods "Functional peptide learning using a deep neural network"
- **Evidence pointer** Materials and methods section
- **Issue** The description of the N-gram model and Monte Carlo simulation is brief and lacks specific details on the implementation, such as the value of n in the N-gram, the size of the training corpus, and the criteria for stopping the Monte Carlo simulation.
- **Required correction** Provide a more detailed description of the model, including the specific N-gram order, training data size, and simulation parameters. Consider including a pseudocode or a diagram of the algorithm.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, Introduction
- **Issue** The terms "unsupervised deep learning" and "N-gram model" are used interchangeably. An N-gram model is a statistical language model and may not be considered "deep learning" in the conventional sense. This inconsistency may confuse readers.
- **Required correction** Clarify the relationship between the N-gram model and deep learning. If the N-gram is implemented as a neural network, specify this. Otherwise, adjust the terminology to accurately describe the method.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Figure quality and labeling
- **Affected element** Figures 3, 4, 5
- **Evidence pointer** Results sections
- **Issue** The figures are referenced but not provided in the manuscript text. Based on the descriptions, the figures appear to contain multiple panels with complex data. The figure legends are not included in the text, making it difficult to interpret the results.
- **Required correction** Ensure that figure legends are comprehensive and self-explanatory. Consider providing representative images and quantification in a clear and accessible format.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The Discussion acknowledges some limitations (e.g., dose, injection frequency) but does not address the potential limitations of the deep learning approach itself, such as the risk of overfitting to the training set or the generalizability of the model to other biological processes.
- **Required correction** Add a paragraph discussing the limitations of the computational approach and the potential for bias in the training data.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reference to supplementary materials
- **Affected element** Results and Materials and methods
- **Evidence pointer** Results sections, Materials and methods
- **Issue** Several supplementary tables and figures are referenced, but their content is not described in the text. This makes it difficult to understand what data are presented in the supplementary materials.
- **Required correction** Briefly describe the content of each supplementary table and figure in the text where they are first referenced.

## Risk / unsupported claims
- The claim that the deep learning model "learned a semantic pattern" from IDRs is not quantitatively supported by any evaluation of the learned representations.
- The claim that AIB5P directly binds to integrin α5 is not fully supported by the provided evidence, which relies on pulldown and knockdown experiments without direct binding assays.
- The claim that AIB5P has "strong bone-formation-promoting effects" is based on a single dose in each model, without dose-response data.
- The generalizability of the approach to other biological processes is asserted but not demonstrated.
- The comparison between IDR-derived and non-IDR-derived peptides (mentioned in the Discussion) is not shown in the results, making the claimed advantage of IDRs unverifiable.
- The statement that "many of the output candidate oligopeptides exerted the anticipated effects" is not quantified; the number of active peptides out of the 28 tested is not reported.