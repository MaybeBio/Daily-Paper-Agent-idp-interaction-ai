## Review setup
- **Input scope** Full manuscript text, including abstract, main text, figure legends, and supplementary materials description
- **Assessment boundary** Scientific claims, methodological soundness, evidence quality, and alignment with stated conclusions
- **Shared manuscript claim summary** The authors propose that internucleosomal DNA linker length (25 bp vs 30 bp) controls nucleosome arrangement and histone tail interactions, which in turn determines the balance between intra- and intermolecular interactions, governing the molecular network, thermodynamic stability, and material properties of chromatin condensates. They further claim that native mammalian nuclei contain dense nucleosome clusters whose non-random organization mirrors the reconstituted condensates.
- **Visible evidence base** Cryo-electron tomography (cryo-ET) data of 25 bp and 30 bp chromatin in low and high salt conditions; coarse-grained molecular dynamics simulations; context-aware template matching (CATM) for nucleosome placement; subtomogram averaging; FRAP and fusion assays; passive microrheology using optical traps; trypsin digestion experiments; cryo-FIB milling and cryo-ET of HeLa and NIH 3T3 cells
- **Missing materials affecting confidence** Full methods section not provided; detailed simulation parameters not provided; statistical analysis details not provided; figure panels referenced but not fully visible in text; supplementary tables and movies referenced but not accessible

## Reviewer
- **Overall assessment** This manuscript presents a comprehensive and technically sophisticated investigation of chromatin condensate structure across multiple scales, from amino acid-level interactions to network architecture. The combination of cryo-ET with chemically specific coarse-grained simulations is innovative and provides mechanistic insight that is difficult to achieve with either approach alone. The central claim, that linker length determines the balance between intra- and intermolecular interactions and thereby governs condensate properties, is well supported by the data presented. The work has significant implications for understanding chromatin organization in cells and the physical principles underlying biomolecular condensates. However, several technical concerns and limitations in the evidence base need to be addressed before the case is fully established.

- **Who would be interested in the results, and why** This work will be of substantial interest to researchers in chromatin biology, phase separation, biophysics, and cell biology. The structural insights into how linker length modulates nucleosome packing and histone tail interactions will inform studies of chromatin organization and gene regulation. The methodological framework combining cryo-ET with simulations will be valuable to the broader condensate community. The findings on native chromatin organization have implications for understanding nuclear architecture and the role of phase separation in genome function.

- **Major strengths**
  1. The multiscale approach, integrating cryo-ET with simulations, provides a powerful framework for understanding condensate structure.
  2. The systematic comparison of 25 bp and 30 bp chromatin, which differ in a single parameter (linker length), allows for clear attribution of observed differences.
  3. The validation of simulation predictions with experimental perturbations (H4 tail deletion, trypsin digestion, acetylation) strengthens the mechanistic conclusions.
  4. The connection to native chromatin organization in cells provides biological relevance.
  5. The material properties measurements (rheology, single-molecule tracking) are comprehensive and well-integrated with structural data.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "the most frequent tail interactions arise from energetically favorable pairs—lysines and arginines contacting negatively charged histone residues and DNA" based on simulation analyses.
- **Evidence pointer** Section "Salt differentially reorganizes histone tail interactions", Figure 2, Figure S3
- **Concern** The manuscript states that "interaction statistics do not directly report on energies," yet the authors use these statistics to infer energetic favorability. The connection between contact frequency and thermodynamic stability is not rigorously established. The simulations are performed with restraints from cryo-ET data, which may bias the interaction distributions. It is unclear how the authors distinguish between interactions that are frequent because they are energetically favorable versus those that are frequent due to geometric constraints imposed by the nucleosome positions.
- **Why it matters** The central mechanistic claim of the paper is that the balance between intra- and intermolecular interactions determines condensate stability. If the energetic interpretation of contact frequencies is not well-founded, the mechanistic conclusions are weakened.
- **Resolution test** Provide free energy calculations or potential of mean force analyses for the key interactions. Alternatively, perform simulations without restraints and compare interaction distributions to the restrained simulations to assess bias. Quantify the energetic contributions of specific tail interactions using alchemical free energy perturbation or similar methods.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "the 25 bp network is more densely connected than the 30 bp network" based on graph analysis of simulations, and that this difference in connectivity, combined with interaction strength, explains the material properties.
- **Evidence pointer** Section "Linker length determines connectivity of the condensate network", Figure 5, Figure S9
- **Concern** The graph abstraction of the simulation trajectories is not described in sufficient detail. It is unclear how nodes and edges are defined, what constitutes an "interaction" between arrays, and how the network metrics (e.g., algebraic connectivity) are calculated. The authors state that "differences in connectivity between the 25 bp and 30 bp condensates were insufficient to account for their different material properties" and that interaction strength (polymer friction coefficient) was needed. This suggests that the network analysis alone does not explain the observations, and the role of the friction coefficient is not well-justified physically.
- **Why it matters** The material properties of condensates are a key outcome of the study. If the network model cannot fully explain the observed differences, the mechanistic link between molecular structure and material properties is incomplete.
- **Resolution test** Provide a detailed description of the graph construction and network metrics. Perform sensitivity analyses to show that the conclusions are robust to the choice of interaction cutoff and network definition. Justify the use of the polymer friction coefficient and show that it is not simply a fitting parameter.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "native chromatin from these cellular sources forms ~100-300 nm scale dense domains composed mostly of nucleosomes that are packed non-randomly and have an excess of contacts involving nucleosome faces, with occasional instances of two-start helical fibers."
- **Evidence pointer** Section "Native chromatin forms domains with nucleosome organization similar to 25 bp condensates", Figure 6, Figure S13, Figure S14
- **Concern** The comparison between native chromatin and reconstituted condensates is based on limited sampling. The number of cells analyzed, the number of domains examined, and the statistical power of the comparisons are not reported. The authors state that the domains "may be inactive chromatin" based on prior literature, but no direct evidence is provided in this study. The claim that native chromatin organization "mirrors" the reconstituted condensates requires quantitative comparison of structural metrics (e.g., radial distribution functions, orientation distributions) with appropriate statistical testing.
- **Why it matters** The relevance of the in vitro findings to cellular chromatin organization is a major claim of the paper. If the comparison is not rigorously established, the broader implications are weakened.
- **Resolution test** Provide detailed statistics on the number of cells, domains, and nucleosomes analyzed. Perform quantitative comparisons between native and reconstituted chromatin using appropriate statistical tests. Provide direct evidence for the identity of the dense domains (e.g., epigenetic marks, chromatin state).

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that "our data show that native chromatin from these cellular sources forms ~100-300 nm scale dense domains composed mostly of nucleosomes that are packed non-randomly and have an excess of contacts involving nucleosome faces."
- **Evidence pointer** Section "Native chromatin forms domains with nucleosome organization similar to 25 bp condensates", Figure 6
- **Concern** The authors do not discuss alternative interpretations of the dense domains observed in native cells. These could arise from technical artifacts of cryo-FIB milling or vitrification, or from non-phase-separation mechanisms such as chromatin tethering to nuclear structures. The authors also do not address how these domains relate to known chromatin structures such as chromocenters, nucleolar-associated domains, or lamina-associated domains.
- **Why it matters** The interpretation of native chromatin organization as phase-separated domains is a significant claim with implications for understanding nuclear architecture. Alternative explanations need to be considered and ruled out.
- **Resolution test** Discuss and rule out alternative mechanisms for dense domain formation. Provide evidence that the domains are dynamic and exchange with the surrounding nucleoplasm, as expected for phase-separated condensates.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract uses technical terms such as "internucleosomal DNA linker length" and "intra- and intermolecular interactions" without brief definitions, which may limit accessibility for readers outside the chromatin field.
- **Required correction** Provide brief contextual definitions or rephrase to make the abstract more accessible to a broad scientific audience.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Figure 1
- **Evidence pointer** Figure 1
- **Issue** The fusion and FRAP data are presented qualitatively. The number of replicates, error bars, and statistical significance are not reported in the text.
- **Required correction** Provide quantitative analysis of fusion and FRAP data with appropriate statistics.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Figure 2
- **Evidence pointer** Figure 2
- **Issue** The contact frequency data in Figure 2H are presented as standard deviations, but the number of independent simulations or samples is not stated.
- **Required correction** Report the number of independent simulations and the method for calculating standard deviations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Figure 4
- **Evidence pointer** Figure 4
- **Issue** The radial distribution functions in Figure 4A are not normalized or compared to a reference (e.g., ideal gas) distribution, making it difficult to assess the significance of the observed peaks.
- **Required correction** Provide normalized g(r) with appropriate reference and confidence intervals.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Figure 5
- **Evidence pointer** Figure 5
- **Issue** The viscoelastic moduli data in Figure 5E are presented without error bars or statistical comparison between 25 bp and 30 bp conditions.
- **Required correction** Provide error estimates and statistical tests for the rheology data.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Figure 6
- **Evidence pointer** Figure 6
- **Issue** The comparison between native chromatin and reconstituted condensates in Figure 6G-I is qualitative. The authors state that the radial distribution functions are "similar" but do not provide a quantitative measure of similarity.
- **Required correction** Provide quantitative comparison metrics (e.g., Kullback-Leibler divergence, correlation coefficient) with appropriate statistical testing.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods
- **Evidence pointer** Methods section (not fully provided)
- **Issue** The description of the coarse-grained model is incomplete. The force field parameters, simulation box size, and equilibration protocol are not described in sufficient detail for reproducibility.
- **Required correction** Provide a complete description of the simulation methodology, including all parameters and protocols.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The authors state that "future studies examining 1-D to 3-D relationships in chromatin containing other regulatory post-translational modifications could yield general principles" but do not discuss specific predictions or hypotheses that could be tested.
- **Required correction** Provide more specific suggestions for future experiments or predictions from the model.

- **Concern ID** R1-m9
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Figure legends
- **Evidence pointer** Figure legends
- **Issue** Some figure legends are dense and use jargon without explanation, which may hinder comprehension for readers outside the field.
- **Required correction** Simplify figure legends and define technical terms.

- **Concern ID** R1-m10
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Supplementary Materials
- **Evidence pointer** Supplementary Materials
- **Issue** The supplementary tables and movies are referenced but not described in the text. It is unclear what information they contain and how they support the main conclusions.
- **Required correction** Provide brief descriptions of supplementary materials in the main text.

## Risk / unsupported claims
- The claim that "the most frequent tail interactions arise from energetically favorable pairs" is not directly supported by the data, as contact frequency does not necessarily reflect thermodynamic stability.
- The claim that native chromatin domains "mirror" the reconstituted 25 bp condensates is based on limited sampling and qualitative comparison.
- The claim that "phase separation may not strongly impact the conformation and flexibility of individual molecules" is based on a small number of traced molecules and may not be statistically robust.
- The claim that acetylation-induced pore formation "could facilitate transcriptional activation by enhancing accessibility" is speculative and not directly tested.
- The relationship between the graph network metrics and material properties is not fully established, as the authors note that connectivity alone is insufficient and the friction coefficient is needed.
- The generalizability of the findings to other chromatin states (e.g., different linker lengths, post-translational modifications) is not demonstrated.