## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors present ColabDock, a framework built on ColabDesign, that inverts an AlphaFold structure prediction model for protein-protein docking under experimental restraints. They claim that ColabDock outperforms HADDOCK and ClusPro in complex structure prediction using simulated residue and surface restraints, NMR chemical shift perturbation, and covalent labeling data, and that it improves antibody-antigen interface prediction using emulated interface scan restraints. The authors further claim that ColabDock provides a general approach to integrate sparse interface restraints of different experimental forms and sources into one optimization framework.
- **Visible evidence base** Abstract text only. No quantitative results, benchmark details, dataset descriptions, or methodological specifications are available.
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, benchmark definitions, training and validation splits, comparison protocols, statistical significance tests, and any code or data availability statements.

## Reviewer
- **Overall assessment** The abstract describes a potentially useful approach for integrating experimental restraints into protein-protein docking via an AlphaFold-based generative framework. The core idea, using a generation-prediction architecture with a trained ranking model, is plausible and could be of interest to the structural biology and computational biology communities. However, the abstract provides no quantitative evidence, no benchmark specifications, and no methodological detail sufficient to evaluate the validity of the performance claims. The central claims of outperformance over HADDOCK and ClusPro, and the generalizability of the restraint integration approach, are currently unsupported by the supplied material.
- **Who would be interested in the results, and why** Structural biologists and computational biologists working on protein-protein interaction prediction, docking method development, and integrative modeling with experimental data. Researchers using NMR, cross-linking, or mutagenesis data to inform complex structure prediction would also be interested, as would developers of deep learning-based structure prediction tools.
- **Major strengths** The conceptual framing is clear and addresses a recognized limitation in current docking methods, namely the limited use of sparse experimental restraints. The proposed framework appears to offer a unified optimization scheme for diverse restraint types, which is a valuable goal. The application to antibody-antigen interface prediction with emulated deep mutation scan data is a potentially impactful direction.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria**  
  Originality: The idea of inverting AlphaFold for docking with restraints is not entirely new, but the specific integration of multiple restraint types into a single optimization framework may offer a novel contribution. However, the abstract does not clearly differentiate ColabDock from prior work such as AlphaFold-Multimer with custom loss functions or other restraint-based docking approaches.  
  Scientific importance: If the performance claims hold, the work could be important for integrative structural biology. However, the abstract does not demonstrate the magnitude of improvement or the practical significance of the gains.  
  Interdisciplinary readership: The topic is relevant to structural biology, computational biology, and bioinformatics. The abstract is written in a way that is accessible to these audiences, but the lack of quantitative detail limits its broader appeal.  
  Technical soundness: Cannot be assessed from the abstract alone. No methodological details, validation procedures, or statistical analyses are provided.  
  Readability for nonspecialists: The abstract is concise and understandable, but terms such as "generation-prediction architecture" and "emulated interface scan restraints" are not explained sufficiently for a general scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a promising framework, but the performance claims and the generalizability statement require substantial additional evidence, including benchmark details, comparison protocols, and statistical validation.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** "ColabDock outperforms HADDOCK and ClusPro not only in complex structure predictions with simulated residue and surface restraints, but also in those assisted by NMR chemical shift perturbation as well as covalent labeling."  
- **Evidence pointer** Abstract only, location not provided  
- **Concern** The abstract states that ColabDock outperforms HADDOCK and ClusPro across multiple restraint types, but no quantitative metrics, benchmark datasets, or statistical significance tests are provided. It is unclear what metric was used (for example, interface RMSD, DockQ, or fraction of native contacts), how the benchmarks were constructed, and whether the comparisons were performed under identical conditions.  
- **Why it matters** Without quantitative results and a clear benchmark protocol, the claim of outperformance cannot be evaluated or reproduced. This is the central claim of the work and is essential for establishing the method's utility.  
- **Resolution test** Provide a table or figure with performance metrics for ColabDock, HADDOCK, and ClusPro on defined benchmark sets, including the number of test cases, the evaluation metrics, and statistical significance tests (for example, paired tests or confidence intervals).

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Methodological clarity  
- **Claim pointer** "ColabDock, a framework that makes use of ColabDesign, but reimplements it for the purpose of restrained complex conformation prediction. With a generation-prediction architecture and trained ranking model..."  
- **Evidence pointer** Abstract only, location not provided  
- **Concern** The abstract does not describe how the generation-prediction architecture works, how the ranking model is trained, what the input and output representations are, or how experimental restraints are encoded and incorporated into the optimization. The term "reimplements" is vague and does not clarify the differences from ColabDesign or AlphaFold.  
- **Why it matters** The methodological novelty and the technical soundness of the approach cannot be assessed without a detailed description of the architecture, training procedure, and restraint integration mechanism. This is necessary for readers to understand the method and for others to reproduce it.  
- **Resolution test** Provide a methods section that details the architecture, the training data and procedure for the ranking model, the representation of restraints, and the optimization algorithm. Include a schematic figure if possible.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Generalizability claim  
- **Claim pointer** "ColabDock provides a general approach to integrate sparse interface restraints of different experimental forms and sources into one optimization framework."  
- **Evidence pointer** Abstract only, location not provided  
- **Concern** The claim of generality is broad and is supported only by results with simulated restraints, NMR chemical shift perturbation, covalent labeling, and emulated deep mutation scan data. It is unclear whether the framework can handle other restraint types, such as cross-linking mass spectrometry or cryo-EM density maps, and whether the performance holds across different protein complex types and sizes.  
- **Why it matters** The generality claim is a key selling point of the work. If the framework is limited to specific restraint types or complex classes, the claim would be overstated. The abstract does not provide evidence to support the breadth of applicability.  
- **Resolution test** Provide a discussion of the types of restraints that can be integrated, and include results on at least one additional restraint type or a diverse set of complexes to demonstrate generality. Alternatively, temper the claim to reflect the tested scope.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Validation of simulated and emulated data  
- **Claim pointer** "ColabDock outperforms HADDOCK and ClusPro not only in complex structure predictions with simulated residue and surface restraints... It further assists antibody-antigen interface prediction with emulated interface scan restraints, which could be obtained by experiments such as Deep Mutation Scan."  
- **Evidence pointer** Abstract only, location not provided  
- **Concern** The abstract relies heavily on simulated and emulated restraints, but it does not describe how these were generated, whether they reflect realistic experimental noise and sparsity, or how the emulated deep mutation scan data were produced. The relevance of the results to real experimental data is therefore unclear.  
- **Why it matters** If the simulated and emulated restraints are idealized, the performance gains may not translate to real experimental settings. The abstract does not provide evidence that the method performs well with realistic, noisy, or incomplete data.  
- **Resolution test** Describe the simulation and emulation procedures in detail, and include at least one validation case with real experimental restraints to demonstrate that the method works under realistic conditions.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity of terminology  
- **Affected element** "generation-prediction architecture"  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The term "generation-prediction architecture" is not defined and may be ambiguous to readers unfamiliar with the specific design.  
- **Required correction** Define the term in the abstract or methods, or use more standard terminology such as "generative model with a scoring function" to improve clarity.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness of comparison  
- **Affected element** Comparison to AlphaFold-Multimer  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The abstract mentions that AlphaFold-Multimer has limited surface prediction accuracy, but it does not include AlphaFold-Multimer in the performance comparisons.  
- **Required correction** Include AlphaFold-Multimer as a baseline in the benchmark comparisons, or explain why it was excluded, to provide a more complete context for the claimed improvements.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Accessibility of resources  
- **Affected element** Code and data availability  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The abstract does not mention whether the code, trained models, or benchmark datasets will be made publicly available.  
- **Required correction** State the availability of code and data in the abstract or the main text, as this is important for reproducibility and community adoption.

## Risk / unsupported claims
- The claim that ColabDock outperforms HADDOCK and ClusPro is unsupported by quantitative evidence in the abstract.
- The claim that ColabDock provides a general approach for integrating different experimental restraint types is unsupported by evidence beyond the tested cases.
- The relevance of results obtained with simulated and emulated restraints to real experimental data is not established.
- The methodological novelty relative to ColabDesign and AlphaFold-Multimer is not clearly articulated or supported.