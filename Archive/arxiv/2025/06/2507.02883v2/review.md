## Review setup
- **Input scope** Full manuscript text (preprint, arXiv:2507.02883v2)
- **Assessment boundary** Scientific content, methodological soundness, benchmark design, evidence quality, and claims as presented in the provided text
- **Shared manuscript claim summary** The authors introduce DisProtBench, a benchmark for evaluating protein structure prediction models (PSPMs) under intrinsically disordered regions (IDRs) and complex biological contexts. They claim: (1) curated datasets spanning disordered regions, GPCR-ligand pairs, and multimeric complexes; (2) a unified evaluation toolbox benchmarking eleven PSPMs across PPI and drug-binding tasks with pLDDT-based stratification; (3) an interactive portal for visualization and error analysis; and (4) findings that IDRs impair PPI prediction performance, that global accuracy metrics fail to predict task performance in disordered settings, and that drug-binding tasks are relatively robust to disorder.
- **Visible evidence base** Main text sections 1-7, technical appendices 8.1-8.7, references to Figures 2-7, 9, 10, 12, and Tables 1, 2, 9
- **Missing materials affecting confidence** Actual figures and tables are not provided; dataset statistics (e.g., number of proteins, complexes, pairs) are not quantified; detailed methodology for dataset curation (e.g., filtering criteria, redundancy removal) is not fully specified; statistical test details (e.g., effect sizes, confidence intervals) are referenced but not shown; portal implementation and usability evaluation are not described; comparison with existing benchmarks (e.g., CAID, CASP) is qualitative only

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important gap in protein structure prediction evaluation: the systematic assessment of model performance in intrinsically disordered regions and realistic biological contexts. The proposed three-axis framework (data complexity, task diversity, interpretability) is conceptually sound and the inclusion of an interactive portal is a valuable contribution. However, the current manuscript has significant limitations in evidence presentation and methodological transparency. Key claims, particularly regarding the quantitative relationship between pLDDT and disorder, the comparative performance of models, and the robustness of drug-binding tasks, are not fully supported by the data shown in the text. The manuscript would benefit from clearer dataset descriptions, more detailed statistical reporting, and a more critical discussion of the limitations of using pLDDT as a disorder proxy.

- **Who would be interested in the results, and why** Computational biologists and bioinformaticians developing or applying protein structure prediction models would be the primary audience. Researchers studying intrinsically disordered proteins and their roles in disease, signaling, and protein-protein interactions would find the benchmark relevant. Drug discovery scientists interested in structure-based approaches for GPCR targets and ligand binding would also be interested. The benchmark and portal could serve as a community resource for standardized evaluation, making it relevant to method developers and benchmark designers in the structural bioinformatics community.

- **Major strengths**
  1. Addresses a clear and important gap: existing benchmarks (CASP, CAID) do not jointly evaluate structural prediction, disorder, and downstream functional tasks.
  2. The three-axis framework (data, task, user) is well-structured and provides a comprehensive evaluation paradigm.
  3. The inclusion of multiple PSPMs (eleven) with diverse architectures (Evoformer, Transformer, Hybrid) enables meaningful comparative analysis.
  4. The pLDDT-based stratification approach is a practical and scalable strategy for isolating disorder effects, and the empirical validation in Section 5.1 is a useful contribution.
  5. The interactive portal is a significant usability enhancement, addressing a common barrier in benchmark adoption.
  6. The finding that disorder impacts PPI prediction more than drug-binding tasks is an interesting and potentially impactful observation.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that "pLDDT scores follow a clear bimodal distribution: disordered residues cluster around 30–40, while ordered residues peak above 85, with minimal overlap" (Section 5.1), and that this validates pLDDT as a proxy for disorder.
- **Evidence pointer** Figure 3, Section 5.1
- **Concern** The claim of a "clear bimodal distribution" and "minimal overlap" is presented as a key methodological foundation, but the actual figure is not provided in the manuscript text. The quantitative basis for this claim (e.g., overlap coefficients, separation metrics, number of residues analyzed) is not reported. Furthermore, the analysis appears to be based solely on AF3 predictions on the DisProt-based dataset, and it is unclear whether this bimodality generalizes across other PSPMs or datasets. The use of pLDDT as a proxy for disorder is a strong assumption that requires more rigorous validation, including comparison with experimentally validated disorder annotations (e.g., from DisProt or MobiDB) and discussion of known limitations (e.g., pLDDT may not capture all types of disorder or dynamic behavior).
- **Why it matters** The entire benchmark's stratification strategy depends on the validity of pLDDT as a disorder proxy. If this relationship is not robustly established, all downstream conclusions about disorder effects on model performance are undermined. The claim is central to the manuscript's contribution and must be supported by quantitative evidence.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency
- **Claim pointer** The manuscript claims to benchmark "eleven state-of-the-art PSPMs" (Section 1, point 2) and later states "eleven diverse PSPMs (Table 1)" (Section 5.2), but the abstract and introduction also mention "twelve leading PSPMs" (abstract).
- **Evidence pointer** Abstract, Section 1, Section 5.2, Table 1
- **Concern** There is an internal inconsistency in the number of models benchmarked: the abstract states "twelve leading PSPMs," while the main text and table description state "eleven." This discrepancy is not explained. Additionally, Table 1 is not provided, so the reader cannot verify which models were included, their versions, or their input requirements. The selection criteria for including these specific models (e.g., availability, performance, architectural diversity) are not stated.
- **Why it matters** The number and identity of benchmarked models are central to the manuscript's claims about comparative performance and generalizability. An inconsistency in this basic fact undermines the manuscript's credibility and suggests a lack of careful proofreading. Without the table, the reader cannot assess whether the model selection is appropriate or representative.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that "global accuracy metrics often fail to predict task performance in disordered settings" (abstract) and that "disorder disrupts tasks involving extended interaction interfaces (e.g., PPIs) far more than localized ones (e.g., ligand binding)" (Section 5.3, Key Insights).
- **Evidence pointer** Figures 4-7, Tables 2 and 9, Section 5.3
- **Concern** These are the manuscript's central findings, but the supporting evidence is not presented in sufficient detail. The figures and tables are referenced but not shown, and the text provides only qualitative descriptions (e.g., "substantially improves," "persistent deficits," "minimal variation"). No effect sizes, confidence intervals, or statistical test results are reported in the text. The claim that global metrics "fail to predict" task performance requires a formal correlation or regression analysis between global accuracy metrics (e.g., TM-score, RMSD) and task-specific performance (e.g., PPI accuracy, binding affinity error), which is not described. The comparison between PPI and drug-binding tasks is also confounded by different datasets and evaluation protocols, making the "disorder disrupts PPI more" claim difficult to interpret without more controlled comparisons.
- **Why it matters** These findings are the primary scientific contribution of the manuscript. Without detailed quantitative evidence, the claims are not verifiable and the manuscript's contribution is significantly weakened. The reader cannot assess the magnitude of the effects, the statistical significance, or the robustness of the conclusions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Dataset description
- **Claim pointer** The manuscript claims to curate "a diverse benchmark dataset covering multiple biologically complex scenarios involving IDRs" (Section 1, point 1), including "thousands of disease-associated human proteins with disordered regions" (Section 1, point 1).
- **Evidence pointer** Section 4, Section 8.4
- **Concern** The dataset description is insufficiently detailed. The manuscript does not provide: (1) the exact number of proteins, complexes, and ligand pairs in each dataset; (2) the criteria for selecting disease-associated proteins (e.g., which diseases, what evidence of disease association); (3) the threshold and source for defining "long disordered segments" (≥20 residues is mentioned, but the annotation source and version are not specified); (4) the redundancy removal protocol (e.g., sequence identity cutoff); (5) the train/test split strategy, if any; and (6) the overlap between the DisProt-based dataset and the GPCR/PPI datasets. The filtering criteria for GPCR-ligand pairs (e.g., Ki value range, activity types) are mentioned but not fully specified.
- **Why it matters** A benchmark's value depends critically on the quality and transparency of its datasets. Without detailed dataset descriptions, the benchmark cannot be reproduced, compared with other benchmarks, or assessed for potential biases. The claim of "thousands" of proteins is not verifiable without exact numbers.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the DisProtBench toolbox "supports unified classification, regression, and interface metrics" (Section 1, point 2) and that it enables "systematic evaluation of functional reliability" (Section 1, point 2).
- **Evidence pointer** Section 5.2, Section 8.1, Section 8.3
- **Concern** The description of the evaluation toolbox is high-level and lacks technical detail. The manuscript does not specify: (1) how PPI predictions are generated from the predicted structures (e.g., which interface detection algorithm is used, what threshold defines an interface); (2) how binding affinity is estimated from structures (e.g., which scoring function or model is used); (3) how the "unified" metrics are computed across different tasks and models with different output formats; (4) the exact definitions of the interface metrics (PP, PR, LP, LR) and how they differ from standard precision/recall; and (5) how the pLDDT stratification is applied in practice (e.g., are residues filtered out, or are separate evaluations run on different strata?). The reference to "LISA-CPI" in Section 8.3 is not explained or cited.
- **Why it matters** The toolbox is a core contribution, but without technical specifications, it cannot be evaluated for correctness, reproducibility, or generalizability. The reader cannot determine whether the evaluation is fair and unbiased across models.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract mentions "twelve leading PSPMs" while the main text consistently states "eleven." This inconsistency should be resolved.
- **Required correction** Correct the number to be consistent throughout the manuscript.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 4
- **Evidence pointer** Section 4
- **Issue** The description of the "Individual Protein Dataset" mentions "71,757 GPCR–ligand pairs (top 20 GPCRs) and 33,212 pain-related pairs" but does not explain how "top 20 GPCRs" were selected or what "pain-related" means in terms of specific targets or ligands.
- **Required correction** Provide a brief explanation of the selection criteria for GPCRs and the definition of "pain-related" pairs.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Section 8.3
- **Evidence pointer** Section 8.3
- **Issue** The "LISA-CPI" model is mentioned as part of the drug discovery pipeline but is not described or cited. The reader cannot assess its relevance or validity.
- **Required correction** Provide a citation and brief description of LISA-CPI, or remove the reference if it is not essential.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section 8.4
- **Evidence pointer** Section 8.4
- **Issue** The manuscript states that "All experiments in our benchmark were conducted using NVIDIA A100 GPUs" and that "the total computation time across all tasks amounts to approximately 2,000 GPU hours," but does not provide per-model or per-task computational costs, which would be useful for assessing feasibility.
- **Required correction** Provide a breakdown of computational costs by model and task, or state that this information is available in the repository.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Section 6
- **Evidence pointer** Section 6
- **Issue** The portal description is detailed but the manuscript does not report any user evaluation or usability testing. The claim that the portal "facilitates both expert and non-expert engagement" is not supported by evidence.
- **Required correction** Either add a brief user study or soften the claim to indicate that the portal is designed for this purpose.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 8.2
- **Evidence pointer** Section 8.2
- **Issue** The model descriptions are brief and do not include version numbers or specific training configurations. For example, "AlphaFold2 (AF2) [6]" does not specify which version or whether the authors used the original or a reimplementation.
- **Required correction** Provide version numbers and relevant configuration details for each model.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: The pLDDT-disorder relationship is not quantitatively validated; the bimodal distribution claim is unsupported by shown data.
  - R1-M2: Inconsistent model count (eleven vs. twelve) and missing Table 1.
  - R1-M3: Central findings on disorder effects and global metric limitations are not supported by detailed quantitative results.
  - R1-M4: Dataset descriptions are insufficient for reproduction and assessment of potential biases.

- **Assessment against Nature-style criteria**
  - **Originality**: The concept of a disorder-aware, task-rich benchmark is a novel contribution. While individual components (pLDDT-based analysis, PPI prediction, drug binding) exist in the literature, their integration into a unified framework with an interactive portal is original. However, the novelty is somewhat diminished by the lack of detailed comparison with existing benchmarks beyond qualitative statements.
  - **Scientific importance**: The problem addressed is important. IDRs are increasingly recognized as critical for function and disease, and current evaluation methods are inadequate. The manuscript's findings, if substantiated, could influence how the community evaluates PSPMs. However, the importance is contingent on the validity of the central claims, which are currently not fully supported.
  - **Interdisciplinary readership**: The topic is relevant to structural biology, computational biology, bioinformatics, and drug discovery. The manuscript is written in a way that is accessible to these communities, though some technical details (e.g., specific metrics) may require familiarity with the field. The portal is a positive step for broader engagement.
  - **Technical soundness**: The overall framework is reasonable, but the manuscript lacks sufficient technical detail to assess the soundness of the evaluation methodology. The pLDDT proxy validation is insufficient, the statistical analysis is not described in detail, and the dataset construction is not fully transparent. These are significant technical shortcomings.
  - **Readability for nonspecialists**: The manuscript is generally well-written and the structure is clear. The use of figures and tables (if provided) would help. However, some sections (e.g., Section 8.2) are dense and may be challenging for nonspecialists. The abstract is accessible.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important gap and proposes a valuable framework, but the current evidence is insufficient to support the central claims. The authors must provide: (1) quantitative validation of the pLDDT-disorder relationship; (2) detailed dataset descriptions; (3) full statistical reporting for all results; and (4) resolution of the model count inconsistency. If these issues are addressed, the manuscript could make a significant contribution to the field.

## Risk / unsupported claims
- The claim that "pLDDT scores follow a clear bimodal distribution... with minimal overlap" is unsupported without the actual figure and quantitative metrics.
- The claim that "global accuracy metrics often fail to predict task performance in disordered settings" is not supported by any shown correlation or regression analysis.
- The claim that "disorder disrupts tasks involving extended interaction interfaces (e.g., PPIs) far more than localized ones (e.g., ligand binding)" is not supported by controlled comparisons.
- The claim that the benchmark includes "thousands of disease-associated human proteins" is not verifiable without exact dataset statistics.
- The claim that the portal "facilitates both expert and non-expert engagement" is not supported by any user evaluation.
- The claim that DisProtBench is "the first benchmark to formalize and operationalize" pLDDT-based stratification across multiple tasks is not verifiable without a more thorough literature comparison.