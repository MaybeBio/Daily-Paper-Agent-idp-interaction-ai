## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, methods, and supplementary figure/table descriptions
- **Assessment boundary** Scientific claims, methodological soundness, evidence quality, and alignment with stated conclusions; no assessment of editorial fit or publication policy
- **Shared manuscript claim summary** The authors report that a compact generative language model (~17M parameters) trained from scratch on 137 phase-separating protein sequences can learn compositional grammar sufficient to generate novel, chimeric sequences that reproduce physicochemical properties of LLPS-prone IDPs; four of five synthesized short peptides show condensation signatures; computational screening of longer sequences identifies candidates with phase-separation tendencies comparable to hnRNPA1 LCD
- **Visible evidence base** Main text figures 1–9 (described), supplementary figures S1–S16 (described), supplementary tables S1–S3 (described), methods section, data availability statement
- **Missing materials affecting confidence** Actual figure images, supplementary data files (S1–S5), detailed hyperparameter search results, raw simulation trajectories, experimental raw data (turbidity curves, microscopy images, CD spectra), code implementation details

## Reviewer

- **Overall assessment** This manuscript presents a conceptually interesting approach: training a small, task-specific generative model on a curated set of phase-separating proteins rather than fine-tuning large general-purpose language models. The core idea has merit, and the authors provide a reasonable demonstration that their model captures length-dependent physicochemical trends. However, several significant concerns limit the strength of the conclusions. The experimental validation is limited to five short peptides with qualitative readouts, the computational screening relies on a force field with acknowledged quantitative limitations, and the comparison against alternative approaches (e.g., fine-tuned large PLMs) is absent. The chimeric recombination analysis is informative but the interpretation of novelty requires more careful consideration of the training set composition. The manuscript would benefit from additional validation depth and a more critical discussion of what the model has actually learned versus what it reproduces from training data statistics.

- **Who would be interested in the results, and why** Researchers in protein design, biomolecular condensates, and computational biology would find this work relevant. The demonstration that small, task-specific models can learn meaningful sequence grammars from limited data has implications for other protein design problems where curated datasets are small. The specific application to phase-separating proteins is of interest to the LLPS community, particularly those seeking generative approaches for designing condensate-forming sequences. The methodological framework (training, screening, experimental validation) provides a template that could be adapted to other sequence-function problems.

- **Major strengths**
  1. The core concept of training a compact, task-specific generative model on curated LLPS data is well-motivated and addresses a genuine gap in the field
  2. The length-ablation analysis (Fig. 2) provides a rigorous test of whether the model captures length-dependent compositional rules rather than just global averages
  3. The chimeric recombination analysis (Fig. 4) directly addresses the memorization concern and provides quantitative evidence for novelty
  4. The inclusion of both experimental (short peptides) and computational (longer sequences) validation attempts demonstrates awareness of the need for multi-scale assessment
  5. The model ablation study (Fig. 3) provides mechanistic insight into which components contribute to biophysical fidelity

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation depth
- **Claim pointer** "Four of them show condensate-like signatures under near-physiological conditions, including droplet-like assemblies and increased turbidity"
- **Evidence pointer** Figure 6, Figures S4–S9
- **Concern** The experimental validation is limited to five short peptides (20–25 residues) with qualitative readouts (turbidity, DIC microscopy). The claim that four of five show "condensate-like signatures" is based on visual inspection of droplet formation and OD600 measurements. There is no quantitative characterization of condensate properties, no fluorescence recovery after photobleaching (FRAP) to confirm liquid-like behavior, no concentration-dependent phase boundary determination, and no control experiments with the PDB* GPT-derived peptide under identical conditions. The authors acknowledge this limitation in the text but the strength of the claim in the abstract and conclusion exceeds what the evidence supports.
- **Why it matters** The central claim of the paper is that the model generates sequences with condensate-forming propensity. Without rigorous experimental validation, the connection between model output and functional behavior remains suggestive rather than demonstrated. The field of LLPS research has established standards for demonstrating phase separation, and the current evidence falls short of these standards.
- **Resolution test** Provide quantitative characterization of condensate formation: fluorescence recovery after photobleaching (FRAP) to demonstrate liquid-like properties, determination of saturation concentrations, comparison with a negative control (e.g., a PDB* GPT-derived peptide or a scrambled sequence), and ideally, validation at multiple concentrations and conditions. Alternatively, temper the claims to state that the peptides show "droplet-like assemblies consistent with, but not definitive of, liquid-liquid phase separation."

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Computational validation methodology
- **Claim pointer** "12 of 89 sequences comparable to the strongly phase-separating hnRNPA1 low-complexity domain"
- **Evidence pointer** Figure 7, Figure 8, Tables S1–S2, Methods section
- **Concern** The computational screening relies on CALVADOS-3 coarse-grained simulations, and the authors themselves note that "they carry significant errors in estimating the free energy of condensation." The interpretation of the Gini coefficient (Cg) as a proxy for phase-separation tendency is not well-established in the literature. The authors compare against hnRNPA1 A1-LCD as a positive control, but do not include a negative control (e.g., a known non-phase-separating disordered protein) to calibrate the Cg scale. The threshold for "comparable to A1-LCD" is not clearly defined, and the relationship between Cg values and actual phase-separation propensity is not validated against experimental data.
- **Why it matters** The computational screening is the primary evidence for the model's ability to generate longer sequences with phase-separation propensity. If the Cg metric is not properly calibrated or validated, the claim that 12 of 89 sequences are "comparable to A1-LCD" is not interpretable. The authors' own caveat about CALVADOS-3 limitations undermines the strength of this conclusion.
- **Resolution test** Include negative controls (known non-phase-separating disordered proteins) in the simulation set to establish the Cg scale. Validate the Cg metric against experimentally characterized sequences with known phase-separation behavior. Provide a clear definition of the threshold for "comparable to A1-LCD" and justify it based on the distribution of Cg values. Alternatively, present the results as relative rankings rather than absolute claims of phase-separation propensity.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Comparison with alternative approaches
- **Claim pointer** "Existing protein language models are typically trained on large, folded-protein-rich sequence corpora and may not optimally capture the compositional biases of LLPS-prone disordered proteins"
- **Evidence pointer** Figure S1, Introduction
- **Concern** The motivation for training a small model from scratch rather than fine-tuning a large PLM is stated but not empirically tested. The authors show that ProtT5-XL embeddings do not separate LLPS+ from PDB* sequences in UMAP space (Fig. S1), but this is a weak test. A direct comparison between the proposed approach and fine-tuned large PLMs (e.g., ESM-2, ProtGPT2) on the same generation and screening tasks would strengthen the claim that the compact approach is advantageous. The authors mention that "fine-tuning a considerably larger, general-purpose PLM on this same small dataset would likely be far more prone to overfitting and memorization" but this is speculation, not demonstrated.
- **Why it matters** The paper's central premise is that a compact, task-specific model is preferable to large general-purpose models for this problem. Without a direct comparison, the reader cannot assess whether this claim is justified. If a fine-tuned large PLM performs comparably or better, the practical value of the proposed approach is diminished.
- **Resolution test** Fine-tune a large PLM (e.g., ESM-2) on the same LLPS+ dataset and compare: (a) physicochemical property reproduction in generated sequences, (b) novelty/chimerism rates, (c) computational screening outcomes, and (d) experimental validation results. This would provide a direct test of the stated motivation.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor and reproducibility
- **Claim pointer** "LLPS+ GPT faithfully reproduces the training-set trends for all the calculated sequence properties"
- **Evidence pointer** Figure 2, Figures S2–S3
- **Concern** The length-ablation analysis compares training and generated sequences across 21 bins for 8 properties. The authors state that the curves are "statistically indistinguishable" but do not provide the statistical test used, the test statistics, or the p-values. The shaded error regions are described but their calculation method is not specified. Additionally, the analysis is performed on a single model instance (or possibly multiple, but this is not stated), and the seed-stability analysis is only mentioned in the supplementary information without details on how it was incorporated into the main results.
- **Why it matters** The claim of faithful reproduction of physicochemical properties is a cornerstone of the paper. Without transparent statistical methodology, the reader cannot assess whether the agreement is meaningful or could arise by chance. The lack of detail on error calculation and statistical testing undermines the reproducibility of the analysis.
- **Resolution test** Provide explicit statistical tests (e.g., Kolmogorov-Smirnov, Mann-Whitney U) with test statistics and p-values for each property and length bin. Specify how error regions are calculated (e.g., standard deviation across seeds, bootstrap confidence intervals). Report the number of model instances used and how seed variability was incorporated into the main results.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Hyperparameter optimization description
- **Evidence pointer** Methods section, Table S3
- **Issue** The hyperparameter optimization is described as a "search over embedding dimension, number of layers, and number of attention heads" but the search space, the number of configurations tested, and the selection criteria beyond "lowest absolute validation loss" are not specified. The statement that "increasing depth beyond two layers degraded validation loss" is presented without supporting data in the main text.
- **Required correction** Provide the full search space, the number of configurations evaluated, and a table or figure showing validation loss for all tested configurations in the main text or clearly reference the supplementary material with specific details.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Experimental controls
- **Affected element** Peptide selection and controls
- **Evidence pointer** Methods section, Figure 6
- **Concern** The selection criteria for the five peptides (seq-0 to seq-4) are described as based on "feasibility for solid-phase peptide synthesis" but the specific criteria (e.g., length, hydrophobicity, aggregation propensity) are not detailed. The manuscript does not describe whether a negative control peptide (e.g., a sequence predicted to be non-phase-separating) was included in the experimental assays.
- **Required correction** Specify the exact selection criteria for the five peptides. Include a negative control peptide in the experimental validation, or explicitly state why a negative control was not included and discuss the implications for interpreting the results.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 5
- **Evidence pointer** Figure 5, Results section
- **Concern** The comparison of physicochemical properties between LLPS+ and PDB* GPT sequences (Fig. 5) is presented as distributions, but the statistical significance of the differences is not reported. The text states "stark differences" but does not provide quantitative measures of separation or overlap.
- **Required correction** Add statistical tests (e.g., Kolmogorov-Smirnov test) for each property comparison in Figure 5 and report the test statistics and p-values either in the figure or in the text.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility of simulations
- **Evidence pointer** Methods section, Phase coexistence simulation details
- **Concern** The simulation protocol is described but key parameters such as the number of independent simulations per sequence, the equilibration time, the criteria for determining steady state, and the method for calculating Cg from concentration profiles are not fully specified. The choice of 200 copies of the peptide and the box dimensions are stated but not justified.
- **Required correction** Provide complete simulation parameters, including the number of replicates, simulation length, convergence criteria, and the exact procedure for calculating Cg from the concentration profiles. Justify the choice of system size and peptide copy number.

- **Technical failings that need to be addressed before the case is established**
  R1-M1 (experimental validation depth), R1-M2 (computational validation methodology), R1-M3 (comparison with alternative approaches), R1-M4 (statistical rigor)

- **Assessment against Nature-style criteria**
  - **Originality**: The approach of training a compact, task-specific generative model on curated LLPS data is a novel contribution. The chimeric recombination analysis provides a useful framework for assessing model novelty. However, the conceptual advance over existing approaches is incremental rather than transformative.
  - **Scientific importance**: The work addresses a relevant problem (sequence grammar of phase-separating proteins) and demonstrates a potentially useful methodology. However, the limited experimental validation and the acknowledged limitations of the computational screening reduce the immediate impact. The broader applicability to other protein design problems is plausible but not demonstrated.
  - **Interdisciplinary readership**: The work bridges machine learning, biophysics, and protein chemistry, which could attract readers from multiple communities. However, the technical depth in each area may limit accessibility for nonspecialists in any single discipline.
  - **Technical soundness**: The model training and evaluation approach is generally sound, but the statistical methodology for comparing training and generated distributions is incomplete. The computational screening relies on a force field with acknowledged quantitative limitations, and the experimental validation is qualitative. The ablation study is informative but limited in scope.
  - **Readability for nonspecialists**: The manuscript is generally well-written and the logical flow is clear. However, some sections (particularly the model architecture description and the simulation details) assume significant technical background. The abstract and introduction are accessible, but the results section may be challenging for readers without expertise in both machine learning and biophysics.

- **Recommendation posture** Supportive if technical concerns are resolved. The core concept is promising and the authors have made a reasonable initial demonstration. However, the experimental validation needs to be substantially strengthened, the computational screening methodology needs better calibration and controls, and the statistical analysis needs to be more rigorous. A direct comparison with fine-tuned large PLMs would significantly strengthen the paper's central claim. The manuscript is not currently established from the provided evidence, but the approach warrants further development and validation.

## Risk / unsupported claims
- The claim that four of five peptides show "condensate-like signatures" is based on qualitative evidence (turbidity, DIC microscopy) without quantitative characterization of liquid-like properties; the claim exceeds what the evidence supports
- The claim that 12 of 89 sequences are "comparable to" hnRNPA1 A1-LCD in phase-separation tendency relies on a Gini coefficient metric that is not validated against experimental data and uses a simulation method with acknowledged quantitative limitations
- The statement that fine-tuning large PLMs "would likely be far more prone to overfitting and memorization" is speculative and not tested empirically
- The claim that the model has "internalized higher-order sequence correlations" is supported by the length-ablation analysis, but the statistical methodology for this claim is not fully specified
- The novelty classification (87.28% chimeric) depends on BLAST thresholds and database composition; the sensitivity of this classification to parameter choices is not assessed
- The model's ability to generate sequences with "condensate-forming" properties is only demonstrated for short peptides (20-25 residues) experimentally; the connection to longer sequences is purely computational
- The statement that the model "learns the compositional grammar" of phase-separating proteins implies a level of mechanistic understanding that is not directly demonstrated; the model may be capturing statistical regularities without explicit grammatical rules