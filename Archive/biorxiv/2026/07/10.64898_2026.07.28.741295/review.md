## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors present Ptarmigan-1, a contrastive learning model that co-embeds protein residues and small molecules in a shared latent space from sequence and 2D chemistry alone, without constructing protein structures or poses. They claim it trains on mixed-resolution chemoproteomic and bioactivity data, scores compounds in ten milliseconds, resolves predictions to residue level, performs comparably to co-folding and docking models on orthosteric targets, matches or exceeds them on covalent, cryptic, and disordered sites, localizes inhibitors to engaged pockets for withheld targets, and screens the human proteome against 3.4 billion compounds in under a day.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary data provided
- **Missing materials affecting confidence** Full manuscript, methods description, training data details, benchmark definitions, evaluation protocols, baseline specifications, computational infrastructure details, and all quantitative results

## Reviewer
- **Overall assessment** The abstract presents an ambitious and potentially impactful approach to structure-free virtual screening. The core idea of co-embedding protein residues and small molecules in a shared latent space is conceptually interesting and could address genuine limitations of structure-based methods. However, the abstract makes numerous strong quantitative and comparative claims without providing any supporting evidence. The absence of methods, benchmark details, and baseline specifications makes it impossible to evaluate the validity of the performance comparisons, the generalizability of the approach, or the significance of the claimed capabilities. The abstract reads more as a promotional summary than a scientific report, with several claims that appear internally inconsistent or overstated.
- **Who would be interested in the results, and why** Computational chemists and medicinal chemists working on virtual screening and drug discovery would be the primary audience. Researchers developing machine learning methods for molecular recognition, particularly those working on structure-free or sequence-based approaches, would find the methodology relevant. Biologists studying cryptic, allosteric, or intrinsically disordered protein sites could be interested in the potential to identify ligands for targets that lack well-defined pockets. The claim of proteome-wide screening at scale would interest those working on polypharmacology and target identification.
- **Major strengths** The conceptual framing is clear and addresses a real gap in the field. The idea of decoupling molecular recognition from structure is well motivated. The claimed speed advantage (ten milliseconds per compound) and the ability to resolve predictions to residue level are potentially valuable capabilities. The breadth of claimed applicability, from orthosteric to cryptic and disordered sites, suggests a general framework rather than a narrow solution.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** The abstract provides no quantitative results, no benchmark descriptions, no baseline specifications, and no methodological details. All performance claims are unverifiable from the supplied material.
- **Assessment against Nature-style criteria** Originality: The concept of residue-level contrastive co-embedding without structure is novel and potentially original. Scientific importance: If the claims are substantiated, the approach could be important for drug discovery, particularly for challenging target classes. Interdisciplinary readership: The work bridges machine learning, chemistry, and biology, which could attract broad interest. Technical soundness: Cannot be assessed from the abstract alone; no methodological or validation details are provided. Readability for nonspecialists: The abstract is generally readable, though some terms (e.g., "co-folding models," "chemoproteomic data") assume domain familiarity.
- **Recommendation posture** Currently not established from the provided evidence. The abstract makes many strong claims but provides no supporting data. A full manuscript with methods, benchmarks, and results would be required to assess whether the case is made.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The claim that Ptarmigan-1 "performs comparably to a collection of co-folding and docking models" on orthosteric targets and "matches or exceeds them" on covalent, cryptic, and disordered sites.
- **Evidence pointer** Abstract only; location not provided
- **Concern** No quantitative results, benchmark datasets, evaluation metrics, or baseline specifications are provided. The abstract states comparative performance without any numbers, statistical measures, or description of the evaluation protocol. It is unclear which co-folding and docking models were used, on which targets, with what data splits, or how performance was measured.
- **Why it matters** Comparative performance claims are the central evidence for the utility of the method. Without knowing the benchmarks, baselines, and metrics, the claims cannot be verified or reproduced. The choice of baselines and evaluation protocols can dramatically affect conclusions in machine learning for drug discovery.
- **Resolution test** Provide a detailed benchmark description including target lists, data splits, baseline model versions and configurations, evaluation metrics with confidence intervals, and statistical significance testing.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim consistency
- **Claim pointer** The claim that Ptarmigan-1 "trains directly on chemoproteomic and bioactivity data of mixed resolution" and the claim that it "resolves each prediction to the residues a compound engages."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract does not explain how training on "mixed resolution" data enables residue-level predictions. Chemoproteomic data can provide residue-level information, but bioactivity data typically does not. The mechanism by which the model learns residue-specific engagement from data that may lack residue-level annotations is not described. This is a critical methodological gap.
- **Why it matters** The residue-level resolution is a key differentiator of the method and is central to its claimed advantage over structure-based approaches. If the model cannot actually attribute predictions to specific residues in a reliable way, the core value proposition is undermined.
- **Resolution test** Describe the training data composition, the fraction of data with residue-level annotations, the learning signal that drives residue-level resolution, and provide validation experiments showing that predicted residue engagement matches experimental evidence.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim consistency
- **Claim pointer** The claim that Ptarmigan-1 "screens the entire human proteome against a library of 3.4 billion compounds in under a day."
- **Evidence pointer** Abstract only; location not provided
- **Concern** This claim implies a computational scale that is difficult to reconcile with the stated per-compound scoring time of ten milliseconds. Screening 3.4 billion compounds against the human proteome (approximately 20,000 proteins) would require 6.8 x 10^13 scoring events. At ten milliseconds per event, this would take approximately 21,500 years on a single processor. Even with massive parallelization, the claim requires extraordinary computational resources that are not described.
- **Why it matters** The scale claim is a headline result that suggests unprecedented throughput. If the arithmetic does not hold, it raises questions about the accuracy of other quantitative claims in the abstract.
- **Resolution test** Provide details on the computational infrastructure, the degree of parallelization, the actual wall-clock time, and clarify whether the screening was performed on the full proteome and full library or on a reduced set.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The claim that Ptarmigan-1 "localizes reversible and covalent inhibitors to the pockets they engage, even for targets withheld from training."
- **Evidence pointer** Abstract only; location not provided
- **Concern** No experimental validation is described. The abstract does not state how localization was verified, whether against crystallographic structures, mutagenesis data, or other experimental evidence. The claim of generalization to withheld targets is central to the method's utility but is presented without any supporting data.
- **Why it matters** Generalization to unseen targets is the key test of a machine learning model's utility. Without validation data, the claim is unsupported and may not hold in practice.
- **Resolution test** Provide experimental validation results, including comparison to known binding sites, mutagenesis confirmation, or other orthogonal evidence, for a set of withheld targets.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "co-folding models" is used without definition. It presumably refers to protein-ligand co-folding or co-folding complex prediction models, but this is not stated.
- **Required correction** Define the term on first use, for example "co-folding models (models that predict the joint 3D structure of a protein-ligand complex)."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Benchmark description
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states performance "comparably" and "matches or exceeds" without specifying the comparison metric. It is unclear whether this refers to enrichment factors, AUC, hit rates, or another metric.
- **Required correction** Specify the evaluation metrics used for comparison in the abstract or indicate where they are defined in the full manuscript.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Data description
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract mentions "chemoproteomic and bioactivity data of mixed resolution" but does not specify the data sources, sizes, or how "mixed resolution" is defined.
- **Required correction** Provide a brief description of the training data sources and the meaning of "mixed resolution" in the abstract or refer to a methods section.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Model architecture
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract describes Ptarmigan-1 as a "contrastive model" but provides no information about the architecture, training objective, or how the shared latent space is constructed.
- **Required correction** Include a brief architectural description or refer to a methods section where these details are provided.

## Risk / unsupported claims
- The claim of comparable or superior performance to co-folding and docking models is unsupported by any quantitative data in the abstract.
- The claim of proteome-wide screening of 3.4 billion compounds in under a day is arithmetically questionable and unsupported by infrastructure details.
- The claim of residue-level localization for withheld targets is unsupported by any validation data.
- The claim of training on "mixed resolution" data enabling residue-level predictions is methodologically unexplained.
- The claim of scoring in ten milliseconds per compound is stated without benchmarking details or hardware specifications.
- The general claim that Ptarmigan-1 "recasts virtual screening as a nearest-neighbor query" is a conceptual statement that cannot be evaluated without understanding the embedding space properties.