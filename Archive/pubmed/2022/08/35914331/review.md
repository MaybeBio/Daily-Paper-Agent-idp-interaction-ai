## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors use approximately 8 microseconds of all-atom molecular dynamics simulations to investigate how the intrinsically disordered region (IDR) of Bcl-2 communicates with its structured region, particularly the ligand binding site. They report that in wild type Bcl-2, no direct communication exists between the IDR and the binding site, but phosphorylation at S70 establishes a communication channel, as inferred from network analysis, leading to increased correlation among binding pocket residues, redistributed conformational sampling, and enhanced binding affinity for Bax. Truncation of the IDR further highlights this hidden pathway.
- **Visible evidence base** Abstract text only; no methodological details, simulation parameters, analysis protocols, or quantitative results are provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, simulation setup and force field details, convergence criteria, network analysis methodology, binding affinity calculations, and any statistical validation

## Reviewer
- **Overall assessment** The abstract presents an intriguing hypothesis regarding IDR-mediated allosteric communication in Bcl-2, with potential relevance to apoptosis regulation. However, the evidence base is limited to a summary of qualitative findings, and the core claims regarding communication pathways, conformational redistribution, and enhanced Bax binding are not quantitatively substantiated within the provided material. The mechanistic narrative is plausible but currently lacks the detail required to assess technical rigor or reproducibility.
- **Who would be interested in the results, and why** Researchers in computational biophysics, intrinsically disordered proteins, and apoptosis signaling would find these results relevant. The work could inform studies on post-translational modification effects on protein dynamics and allosteric regulation in disordered systems, with potential implications for drug design targeting Bcl-2 family proteins.
- **Major strengths** The study addresses a significant gap in understanding how IDRs influence Bcl-2 function, a topic with experimental support but limited molecular-level insight. The use of long-timescale all-atom simulations (approximately 8 microseconds) is appropriate for capturing conformational dynamics. The comparative design involving wild type, phosphorylated, and truncated systems provides a logical framework for isolating the IDR's role.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that "a communication channel between the IDR and the binding site has been established, as evidenced from the network analysis"
  - **Evidence pointer** Abstract; location not provided
  - **Concern** The abstract does not describe the network analysis methodology, including how nodes and edges were defined, what correlation metric was used, or how statistical significance was assessed. Without this information, the claim of an established communication channel cannot be evaluated for robustness or biological meaning.
  - **Why it matters** Network-based inference of allosteric communication is highly sensitive to methodological choices, such as correlation thresholds and community detection algorithms. If the analysis is not rigorously validated, the central mechanistic claim may be an artifact of the chosen parameters.
  - **Resolution test** Provide a detailed description of the network construction and analysis, including validation against null models or alternative methods, and demonstrate that the identified channel is statistically significant and reproducible across independent simulation replicates.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that phosphorylation "redistributs the sampling of conformations of the system" and leads to "enhanced affinity for binding with its partner Bax"
  - **Evidence pointer** Abstract; location not provided
  - **Concern** No quantitative data are provided to support the claims of altered conformational sampling or enhanced binding affinity. The abstract does not specify how conformational sampling was measured, what metric was used to compare distributions, or how binding affinity was calculated (e.g., free energy perturbation, MM-PBSA, or experimental validation).
  - **Why it matters** These are the primary functional consequences of the proposed mechanism. Without quantitative evidence, such as free energy differences, binding constants, or statistically significant changes in conformational populations, the claims remain speculative and cannot be distinguished from simulation noise.
  - **Resolution test** Present quantitative comparisons of conformational ensembles (e.g., principal component analysis projections, free energy landscapes) with statistical tests, and provide binding affinity estimates with error bars, ideally validated against experimental data or at least multiple independent methods.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Reproducibility
  - **Claim pointer** The authors state that "~8micros conformational sampling of Bcl-2" was performed using molecular dynamics
  - **Evidence pointer** Abstract; location not provided
  - **Concern** The abstract lacks essential simulation details, including the number of independent trajectories, system setup, force field parameters, water model, temperature and pressure coupling, and equilibration protocol. It is also unclear whether the 8 microseconds represent a single trajectory or aggregated sampling across multiple systems.
  - **Why it matters** Reproducibility is a cornerstone of computational studies. Without these details, readers cannot assess whether the sampling is sufficient for convergence, whether the results are system-specific artifacts, or whether the study can be replicated.
  - **Resolution test** Provide a complete simulation protocol in the methods section, including trajectory lengths per system, number of replicates, and convergence assessments (e.g., block averaging, RMSD stability, or cluster analysis).
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability
  - **Affected element** Abstract wording
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The phrase "redistributs the sampling" contains a typographical error, and the sentence structure in the latter half of the abstract is convoluted, which may hinder comprehension for nonspecialist readers.
  - **Required correction** Revise the abstract for grammatical accuracy and clarity, particularly the sentence describing the consequences of phosphorylation.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Scientific context
  - **Affected element** Abstract framing
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The abstract does not explicitly state how the findings relate to existing experimental evidence on IDR function in Bcl-2, which would help position the work within the broader literature.
  - **Required correction** Add a brief sentence in the introduction or discussion section of the abstract that connects the simulation results to prior experimental observations.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3. The absence of methodological detail and quantitative support for the central claims means the mechanistic case is not currently established from the provided evidence.

## Risk / unsupported claims
- The claim of an established communication channel between the IDR and binding site is unsupported without network analysis details and validation.
- The claim of enhanced binding affinity for Bax is unsupported without quantitative binding free energy or experimental data.
- The claim of redistributed conformational sampling is unsupported without quantitative ensemble comparisons.
- The overall mechanistic narrative is plausible but not verifiable from the abstract alone.

## Assessment against Nature-style criteria
- **Originality** The concept of IDR-mediated allosteric communication in Bcl-2 is not entirely novel, as experimental studies have suggested such regulation, but the molecular-level mechanistic insight from long-timescale simulations could offer a fresh perspective. The originality is moderate and depends on the novelty of the network analysis findings.
- **Scientific importance** The work addresses a fundamental question in protein biophysics with potential implications for apoptosis regulation and therapeutic targeting. If the claims are substantiated, the importance would be significant for the IDP and Bcl-2 communities.
- **Interdisciplinary readership** The topic bridges computational biology, biophysics, and cell biology, and could appeal to a broad audience if presented with sufficient context and clarity. However, the abstract currently assumes familiarity with simulation and network analysis concepts.
- **Technical soundness** Not assessable from the abstract alone. The lack of methodological detail and quantitative results prevents evaluation of the technical rigor.
- **Readability for nonspecialists** The abstract is partially accessible but contains jargon and grammatical issues that may impede understanding. The mechanistic narrative is clear in concept but not in execution.
- **Recommendation posture** Currently not established from the provided evidence. The hypothesis is interesting and the simulation approach is appropriate, but the abstract lacks the quantitative and methodological detail necessary to support the central claims. A revised manuscript with full methods, statistical validation, and quantitative results could change this assessment.