## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the supplied abstract
- **Shared manuscript claim summary** The authors propose PepInter, a sequence-based deep learning framework for protein-peptide interaction (PpI) prediction. The method uses a two-stage pretraining strategy on structurally derived pseudo protein-peptide pairs, built on the ESM-Cambrian (ESMC) architecture, and is fine-tuned for classification and bioactivity regression tasks. The authors claim consistent outperformance over baselines across multiple benchmarks and strong generalization in identifying biologically meaningful PpIs.
- **Visible evidence base** Abstract text only; no figures, tables, methods details, or quantitative results provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, benchmark descriptions, baseline definitions, dataset statistics, hyperparameter settings, ablation studies, code availability, and any quantitative performance metrics

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting approach to a relevant problem in computational biology. The idea of using structurally derived pseudo protein-peptide pairs for pretraining is plausible and potentially valuable. However, the abstract lacks quantitative results, detailed methodological descriptions, and clear benchmark comparisons. The core claims of outperformance and generalization cannot be evaluated from the supplied material. The work may be of interest to the computational biology community, but the evidence base is insufficient to assess technical soundness or scientific impact.
- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein interaction prediction, peptide-based drug discovery, and representation learning for biological sequences. The approach of leveraging structural information through pretraining could also interest researchers developing foundation models for proteins.
- **Major strengths** The conceptual framing of using energy-dominant peptide fragments from PDB complexes to construct pseudo interaction pairs is a creative solution to the data scarcity problem. The two-stage pretraining strategy that combines masked language modeling with Rosetta-derived energetic score prediction is a reasonable design choice. The focus on both classification and regression tasks suggests potential practical utility.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria**  
  Originality: The pseudo protein-peptide pair construction from structural data is a novel contribution, though the underlying idea of using structural priors for sequence models is not entirely new.  
  Scientific importance: Protein-peptide interactions are biologically significant and prediction tools have practical value, but the abstract does not demonstrate a substantial advance over existing methods.  
  Interdisciplinary readership: The work bridges structural biology, machine learning, and drug discovery, which could appeal to a broad audience if the results are compelling.  
  Technical soundness: Cannot be assessed from the abstract alone. The lack of quantitative results and methodological details prevents evaluation.  
  Readability for nonspecialists: The abstract is generally clear, though some terms such as "ESM-Cambrian" and "Rosetta-derived energetic scores" may require domain knowledge.
- **Recommendation posture** Currently not established from the provided evidence. The conceptual approach is promising, but the abstract does not provide sufficient evidence to support the claims of consistent outperformance and strong generalization. A full manuscript with quantitative results would be required to assess the work properly.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** "Across multiple benchmark datasets, including protein-peptide binding affinity prediction, PepInter consistently outperforms existing baseline methods"  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The claim of consistent outperformance is made without any quantitative results. No performance metrics, baseline names, dataset identifiers, or statistical significance tests are provided.  
- **Why it matters** The central claim of the work is that PepInter is superior to existing methods. Without numerical evidence, this claim is unverifiable and cannot support the paper's conclusions.  
- **Resolution test** Provide performance tables with metrics such as AUC, accuracy, correlation coefficients, and p-values across all benchmark datasets, with clear baseline definitions and statistical comparisons.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Methodological clarity  
- **Claim pointer** "energy-dominant peptide fragments are extracted from protein complexes curated from non-redundant Protein Data Bank (PDB) structures, enabling the construction of pseudo protein-peptide interaction pairs"  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The abstract does not explain how "energy-dominant" fragments are defined, how the non-redundant set is constructed, how pseudo pairs are generated, or how the authors ensure that these pseudo pairs capture interaction patterns relevant to true protein-peptide interactions.  
- **Why it matters** The validity of the entire pretraining strategy depends on the quality and biological relevance of the pseudo interaction pairs. Without methodological details, the approach cannot be reproduced or evaluated.  
- **Resolution test** Provide a detailed methods section describing fragment extraction criteria, redundancy filtering thresholds, pseudo pair construction, and validation that the pseudo pairs recapitulate known interaction features.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Generalization evidence  
- **Claim pointer** "demonstrates strong generalization in identifying biologically meaningful PpIs" and "Case studies further highlight its ability to recover known interaction patterns and predict novel protein-peptide interactions"  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The claim of strong generalization is supported only by unspecified case studies. No details are given about the case study design, the novelty of the predicted interactions, or how biological meaningfulness was validated.  
- **Why it matters** Generalization to unseen and biologically relevant interactions is a key selling point of the method. Without experimental validation or clear benchmarks, this claim is speculative.  
- **Resolution test** Provide case study details including the specific proteins and peptides studied, the prediction confidence, and any experimental or literature-based validation of the predicted interactions.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Title and terminology  
- **Evidence pointer** Abstract title  
- **Issue** The title states "Protein-peptide Interaction Representation Learning" but the abstract focuses on prediction tasks. The relationship between representation learning and downstream prediction could be clarified.  
- **Required correction** Clarify whether the contribution is primarily in representation learning or in the downstream prediction performance, and adjust the title or framing accordingly.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Model availability  
- **Evidence pointer** Abstract only; location not provided  
- **Issue** No mention of code or model availability, which is important for reproducibility in the machine learning community.  
- **Required correction** State whether code, pretrained models, and training data will be made publicly available.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Baseline description  
- **Evidence pointer** Abstract only; location not provided  
- **Issue** The abstract mentions "existing baseline methods" without naming them, making it impossible to assess the fairness of comparisons.  
- **Required correction** List the specific baseline methods used in the full manuscript and justify the choice of baselines.

## Risk / unsupported claims
- The claim of consistent outperformance over baselines is unsupported by any quantitative data.
- The claim of strong generalization is unsupported by specific case study details or validation evidence.
- The claim that pseudo protein-peptide pairs "capture interaction interface patterns shared with canonical protein-protein interactions" is asserted without supporting analysis.
- The potential to "accelerate peptide-based drug discovery" is speculative and not supported by any application-oriented results.
- The overall effectiveness of the two-stage pretraining strategy cannot be evaluated without ablation studies or comparisons to alternative pretraining approaches.