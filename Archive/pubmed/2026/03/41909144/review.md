## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methodology, results, conclusions, supplementary material description, acknowledgements)
- **Assessment boundary** Scientific content, methodological soundness, evidence quality, and alignment with stated claims. Editorial and formatting issues are noted only where they affect scientific clarity.
- **Shared manuscript claim summary** The authors present a systematic all-atom potential-of-mean-force (PMF) study of nucleotide–nucleotide and nucleotide–amino acid interactions, benchmarked across multiple force fields, with the stated goal of providing quantitative data to inform coarse-grained model parametrization for biomolecular condensates.
- **Visible evidence base** Main text figures (referenced as Figure A–H across multiple figure panels), supplementary figures (S1–S7), PMF profiles, free energy minima, force field comparisons, salt concentration dependence data, G-quadruplex PMF calculation
- **Missing materials affecting confidence** Figure files not provided; supplementary information not provided; simulation input files and analysis scripts not provided; convergence criteria and error estimation details not fully described; PDB structure preparation details for G-quadruplex not fully specified

## Reviewer

- **Overall assessment** This manuscript presents a large and potentially valuable dataset of PMF calculations for nucleotide–nucleotide and nucleotide–amino acid interactions. The systematic coverage of all 20 amino acids against 4 nucleotides, combined with force field benchmarking and salt dependence studies, addresses a genuine gap in the field. The work is relevant to the biomolecular condensate community and to those developing coarse-grained models. However, the manuscript as provided has several significant limitations. The absence of actual figure data makes it impossible to evaluate the quantitative claims. The methodology section lacks critical details on convergence, error estimation, and system preparation. The interpretation of certain results, particularly the attribution of binding preferences to specific molecular properties, appears speculative in places. The novelty relative to existing PMF studies of amino acid pairs and nucleotide interactions needs to be more clearly articulated. The manuscript would benefit from a more critical discussion of the limitations of the PMF approach for capturing the multivalent, cooperative interactions that govern condensate formation.

- **Who would be interested in the results, and why** Researchers developing coarse-grained models of biomolecular condensates, particularly those using bottom-up parametrization strategies. Computational biophysicists studying RNA–protein interactions. Experimental groups studying phase separation who seek molecular-level rationalization of their observations. The force field benchmarking data will also be of interest to the molecular simulation community.

- **Major strengths**
  1. Systematic coverage of the interaction space: all 20 amino acids against all 4 RNA nucleotides, plus nucleotide–nucleotide interactions across multiple binding modes.
  2. Force field benchmarking against multiple established models (AMBER03ws, CHARMM36, a99SB-disp) strengthens confidence in the results.
  3. The inclusion of salt concentration effects addresses a physiologically relevant variable.
  4. The G-quadruplex calculation extends the work beyond simple pairwise interactions to a more complex structural motif.
  5. The stated goal of providing a quantitative library for coarse-grained model parametrization is timely and practically valuable.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The manuscript claims systematic characterization of nucleotide–nucleotide and nucleotide–amino acid interactions with quantitative free energy values.
- **Evidence pointer** Figures 1–5 (referenced throughout Results); location not provided
- **Concern** The actual figure data is not available in the provided manuscript. All quantitative claims regarding PMF depths, relative binding affinities, and force field comparisons rest on figures that cannot be evaluated. The text describes trends and values, but without the actual PMF profiles, convergence curves, or error bars, the central quantitative claims of the paper cannot be verified.
- **Why it matters** The paper's primary contribution is quantitative: free energy values for interaction pairs. Without access to the actual data, the reliability of these values, the quality of convergence, and the statistical significance of differences between pairs or force fields cannot be assessed. This is a blocking issue for evaluation.
- **Resolution test** Provide the figure files and supplementary information. Include PMF profiles with error estimates, convergence plots, and representative snapshots of the simulated configurations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological completeness
- **Claim pointer** The methodology states that PMF calculations were performed using umbrella sampling with WHAM, with specific force constants and simulation times.
- **Evidence pointer** Methodology section; location not provided
- **Concern** Critical methodological details are missing. The manuscript does not report how many independent simulations were performed, how statistical errors were estimated, whether the 10 ns per window was sufficient for convergence at all distances, how the initial configurations for each window were generated, or how the Bayesian bootstrap error was combined across windows. The choice of force constant (10,000 vs 6,000 kJ mol−1 nm−2) for different systems is not justified. The equilibration time of 2 ns out of 10 ns total is substantial and its adequacy is not discussed.
- **Why it matters** PMF calculations are notoriously sensitive to sampling quality and protocol choices. Without convergence evidence and error quantification, the reported free energy values cannot be trusted as quantitative benchmarks. The manuscript's stated purpose is to provide data for coarse-grained model parametrization, which requires high accuracy.
- **Resolution test** Add a detailed convergence analysis showing PMF stability over time, overlap between adjacent windows, and error estimates for each reported free energy minimum. Justify the choice of simulation parameters and demonstrate that results are robust to reasonable variations in protocol.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretive validity
- **Claim pointer** The manuscript attributes the stronger binding of Arg to G/C over A/U to "the greater effective polarizability of these bases" and explains Lys's weaker phosphate binding through "the entropic penalty associated with displacing tightly bound water molecules."
- **Evidence pointer** Results section, "Characterization of Nucleotide–Amino Acid Interactions"; location not provided
- **Concern** These mechanistic interpretations appear speculative. No calculations of polarizability, no water residence time analysis, and no decomposition of entropic versus enthalpic contributions are presented. The explanations may be plausible, but they are not supported by evidence in the current manuscript.
- **Why it matters** The manuscript aims to provide mechanistic insight into condensate formation. If the interpretations are not evidence-based, they may mislead subsequent model development or experimental design. The distinction between observation and interpretation needs to be clearer.
- **Resolution test** Either provide supporting calculations (e.g., energy decomposition, water dynamics analysis) or reframe these statements as hypotheses requiring further testing.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Novelty and contextualization
- **Claim pointer** The manuscript presents the work as providing a "comprehensive analysis" and "detailed library" of interactions, implying significant novelty.
- **Evidence pointer** Introduction and Discussion; location not provided
- **Concern** The introduction cites several prior PMF studies of amino acid pairs and RNA–protein interactions, but the specific advance of this work over existing datasets is not clearly articulated. What new information does this provide beyond what is already known? Is the systematic coverage of all 20×4 combinations the key novelty, or is it the force field comparison, or the salt dependence? The manuscript would benefit from a clearer statement of what is new and why it matters.
- **Why it matters** For a dataset paper of this type, the novelty and added value relative to existing resources must be explicit. Without this, the contribution may be seen as incremental.
- **Resolution test** Add a paragraph in the introduction or discussion explicitly comparing the scope and content of this dataset with existing PMF datasets, and state clearly what new capabilities or insights this work enables.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Biological relevance
- **Claim pointer** The manuscript claims the results provide "insight into how residue-level interactions influence molecular organization on larger scales in biomolecular condensates" and that the identified interactions are "key contributors to condensate cohesion."
- **Evidence pointer** Conclusions; location not provided
- **Concern** The leap from pairwise PMF calculations in dilute solution to condensate cohesion is substantial. The manuscript does not discuss how multivalency, avidity, crowding, or the polymeric context of proteins and RNA might modify these pairwise interactions. The claim that specific interactions are "key contributors" to condensate cohesion is not directly supported by the data presented.
- **Why it matters** The broader significance of the work depends on its relevance to condensate behavior. Overstating the connection between pairwise interactions and macroscopic phase behavior could mislead readers.
- **Resolution test** Either temper the claims about condensate relevance, or add a discussion section that explicitly addresses the relationship between pairwise PMFs and emergent condensate properties, citing relevant literature on multivalency and cooperativity.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure references
- **Evidence pointer** Throughout Results; location not provided
- **Issue** Figure references are incomplete. The text refers to "Figure A," "Figure B," etc., without specifying the figure number. This makes it impossible to follow which results correspond to which figure panels.
- **Required correction** Use standard figure numbering (Figure 1, Figure 2, etc.) with panel labels, and ensure all figures are cited in the text.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Simulation details
- **Evidence pointer** Methodology section; location not provided
- **Issue** The manuscript does not specify the number of replicate simulations, the random seed strategy, or the criteria for determining when a PMF calculation was considered converged.
- **Required correction** Add a reproducibility statement with details on replicates, seeds, and convergence criteria.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** G-quadruplex calculation
- **Evidence pointer** Results section, "Characterization of the Different Binding Modes in Nucleotide–Nucleotide Interactions"; location not provided
- **Issue** The G-quadruplex PMF calculation is described briefly. The PDB structure used (4XK0) is mentioned, but the preparation protocol, the pulling strategy, and how the "one strand pulled while three restrained" setup relates to a meaningful free energy of dissociation are not fully explained.
- **Required correction** Provide additional detail on the G-quadruplex simulation setup and clarify what physical quantity the calculated PMF represents.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Error estimates
- **Evidence pointer** Methodology section; location not provided
- **Issue** The manuscript states that errors were estimated using Bayesian bootstrap but does not report the magnitude of these errors for the key results. Without error bars, the significance of differences between force fields or between interaction pairs cannot be evaluated.
- **Required correction** Report error estimates for all reported free energy minima, either in the main text or in the supplementary information.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Data availability
- **Evidence pointer** Supplementary Material section; location not provided
- **Issue** The manuscript does not state whether the simulation input files, analysis scripts, and raw PMF data will be made publicly available. For a dataset paper, this is a significant omission.
- **Required correction** Add a data availability statement describing what will be deposited and where.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1 (missing figure data) and R1-M2 (insufficient methodological detail on convergence and error estimation) are the primary technical issues. Without the actual PMF profiles and convergence evidence, the quantitative claims cannot be verified. The manuscript should not be considered for publication until these are addressed.

- **Assessment against Nature-style criteria**
  - **Originality**: Moderate. The systematic coverage of all amino acid–nucleotide pairs is a useful extension of existing work, but the methodological approach (PMF calculations with umbrella sampling) is well established. The field would benefit from a comprehensive dataset, but the conceptual novelty is limited.
  - **Scientific importance**: Moderate to high. Quantitative interaction data for amino acid–nucleotide pairs are needed for coarse-grained model development, and this work could serve as a reference dataset. The salt dependence and force field benchmarking add practical value.
  - **Interdisciplinary readership**: Moderate. The work will appeal primarily to computational biophysicists and those developing coarse-grained models. Experimental biologists studying condensates may find the data useful but may struggle with the technical detail.
  - **Technical soundness**: Currently not fully assessable. The methodology is standard, but the missing convergence analysis and error reporting prevent a full evaluation. The force field benchmarking is a strength.
  - **Readability for nonspecialists**: Adequate. The manuscript is generally well written, but the incomplete figure references and the density of results make it difficult to follow. A summary table of key interaction energies would improve accessibility.

- **Recommendation posture** Supportive if technical concerns are resolved. The dataset has clear value for the community, and the force field benchmarking is a strength. However, the missing figure data and insufficient methodological detail on convergence and error estimation must be addressed before the quantitative claims can be accepted. The mechanistic interpretations should also be either supported with additional analysis or reframed as hypotheses.

## Risk / unsupported claims
- The claim that Arg's stronger binding to G/C over A/U is due to "greater effective polarizability" is unsupported by direct evidence in the manuscript.
- The claim that Lys's weaker phosphate binding is due to "entropic penalty associated with displacing tightly bound water molecules" is unsupported by water dynamics or entropy decomposition analysis.
- The claim that the identified interactions are "key contributors to condensate cohesion" is not directly supported by the pairwise PMF data presented.
- The quantitative values of all free energy minima are unverifiable without the figure data.
- The claim of "excellent agreement" between AMBER03ws and CHARMM36 for base-pairing predictions cannot be fully evaluated without the actual comparison data.
- The statement that ribose–ribose interactions are "largely insensitive to the specific nucleotide pair" is presented as a general conclusion but is based on a limited set of tested pairs.