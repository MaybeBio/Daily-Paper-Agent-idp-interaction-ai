## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and supplementary data description.
- **Assessment boundary** Assessment is limited to the scientific content, methodology, and claims presented in the provided manuscript. No external validation or replication of simulations was performed.
- **Shared manuscript claim summary** The authors evaluate four transferable, nonpolarizable protein forcefields (ff14SB-TIP3P, CHARMM36m-TIP3P*, ff19SB-OPC, a99SBdisp-TIP4PD) for their ability to reproduce solubility, aggregation propensity, disordered state dimensions, and secondary structure propensities. They report that modern forcefields (ff19SB-OPC, a99SBdisp-TIP4PD) improve description of disordered states and secondary structure propensities, while older forcefields (ff14SB-TIP3P) over-stabilize compact states. They also suggest that multi-protein systems remain a challenge for forcefield optimization.
- **Visible evidence base** Results from molecular dynamics simulations of four systems: ubiquitin solutions (3 and 9 molecules), Htt-1-19 peptide, Aβ16-22 peptide solutions, and Aβ16-40 fibril. Data include interprotein distances, solvent-accessible surface areas, RMSD from helical or fibril references, and per-residue secondary structure propensities. Figures 1-4 and Table 1 are referenced.
- **Missing materials affecting confidence** The manuscript states that coordinates are provided in the Supplementary Information, but the actual files were not available for review. No raw simulation trajectories, forcefield parameter files, or analysis scripts were provided. The exact definitions of "helix propensity" and "β-content" calculations are not fully detailed. The criteria for classifying "aggregation" versus "dynamic interaction" are described qualitatively but not quantified.

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question in the molecular dynamics community: how well do current state-of-the-art forcefields perform on systems that test solubility and aggregation, in addition to the more commonly assessed disordered state dimensions and secondary structure propensities. The study design is thoughtful, using extreme cases of solubility and insolubility to provide clear qualitative readouts. The results are largely consistent with prior literature, confirming known issues with older forcefields and showing improvements in newer ones. However, the study is limited by short simulation timescales, a small number of systems, and a lack of quantitative metrics for some key claims. The suggestion that multi-protein systems are the next challenge is reasonable but not strongly supported by the data presented, as only one multi-protein system (ubiquitin) was tested in a limited manner. The manuscript is clearly written and accessible to a broad audience, but the conclusions would be strengthened by more rigorous quantitative analysis and longer simulations.
- **Who would be interested in the results, and why** Researchers in the molecular dynamics simulation community, particularly those developing or using forcefields for protein simulations. The results are also relevant to experimentalists studying protein solubility, aggregation, and disordered proteins, as they provide guidance on which forcefields are most appropriate for their systems. The study's focus on multi-protein systems may be of interest to those studying protein-protein interactions and biomolecular condensates.
- **Major strengths**
  1. The study addresses a critical gap in forcefield benchmarking by including multi-protein systems and extreme solubility cases, which are often overlooked.
  2. The choice of test systems is well-justified, providing clear qualitative expectations (e.g., ubiquitin should remain soluble, Aβ16-22 should aggregate).
  3. The comparison of four forcefields from different families (Amber, CHARMM, DEShaw) is comprehensive and timely.
  4. The manuscript is well-written and the figures are clear and informative.
  5. The authors provide starting coordinates for all simulated systems, which is a valuable resource for the community.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that "the two modern forcefields (ff19SB-OPC and a99SBdisp-TIP4PD) seem to better reproduce a real solution of concentrated ubiquitin" based on the absence of aggregation in 2-3 microsecond simulations.
  - **Evidence pointer** Figure 1B, Table 1
  - **Concern** The conclusion that a99SBdisp-TIP4PD and ff19SB-OPC correctly predict ubiquitin solubility is based on the absence of aggregation in simulations of only 2-3 microseconds. Given that the experimental Kd for ubiquitin dimerization is 4.4 mM, and the simulations are at 5-6 mM, one would expect to see some dimer formation. The authors acknowledge this, but the lack of any aggregation with a99SBdisp-TIP4PD could also indicate that this forcefield under-stabilizes protein-protein interactions, which is a known issue. The claim that these forcefields "better reproduce" reality is therefore not strongly supported without a more quantitative analysis of the frequency and duration of intermolecular contacts, and a comparison to the expected population of dimers at this concentration.
  - **Why it matters** This is a central claim of the paper. If the conclusion is not robust, the overall message about forcefield performance is weakened. The distinction between "correctly predicting solubility" and "under-stabilizing interactions" is crucial for forcefield development.
  - **Resolution test** The authors should provide a quantitative analysis of the intermolecular contacts, such as the number of contacts per unit time, the lifetime of contacts, and the population of dimers vs. monomers. This should be compared to the expected values based on the experimental Kd. Alternatively, the authors could run longer simulations or use enhanced sampling to better sample the dimerization equilibrium.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The authors state that "multi-protein systems as the next challenge for optimization" based on the observation that some forcefields fail to keep ubiquitin soluble.
  - **Evidence pointer** Discussion section
  - **Concern** While the results do show that older forcefields cause ubiquitin aggregation, the evidence that this is a general problem for multi-protein systems is limited. Only one multi-protein system (ubiquitin) was tested, and the newer forcefields performed reasonably well. The claim that multi-protein systems are "the next challenge" is speculative and not strongly supported by the data. A more comprehensive study with multiple protein systems of varying solubility and interaction affinities would be needed to make this claim convincingly.
  - **Why it matters** This claim frames the future direction of the field. If it is not well-supported, it could misdirect research efforts.
  - **Resolution test** The authors should either soften this claim or provide additional evidence, such as simulations of other multi-protein systems (e.g., a protein known to be monomeric at high concentrations, or a system with a known weak interaction).
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** The authors state that "all four forcefields could correctly capture the secondary structures preferred by the two peptides involved in the studies."
  - **Evidence pointer** Figure 2D, Figure 3B
  - **Concern** The statement that all forcefields "correctly capture" secondary structure propensities is an overstatement. For Htt-1-19, the authors report that ff14SB-TIP3P over-stabilizes helix (45% vs. 20-30% expected), which is not "correct." For Aβ16-22, the authors report that a99SBdisp-TIP4PD and ff19SB-OPC do not aggregate, and thus do not form β-structure, which is also not "correct" given the peptide's known insolubility. The authors do acknowledge these discrepancies, but the summary statement is misleading.
  - **Why it matters** The summary statement could be misinterpreted as a more positive assessment of forcefield performance than is warranted.
  - **Resolution test** The authors should rephrase this statement to be more nuanced, e.g., "all forcefields captured the qualitative preference for β-structure in the aggregating peptides, but with varying degrees of over- or under-stabilization."
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Introduction
  - **Evidence pointer** Introduction, first paragraph
  - **Issue** The introduction is dense and assumes a high level of familiarity with forcefield development history. Terms like "CMAP corrections" and "grid-based energy additions" are introduced without sufficient explanation for a general reader.
  - **Required correction** Provide a brief, plain-language explanation of what CMAP corrections are and why they are important, or move this technical detail to the Methods section.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Methods
  - **Evidence pointer** Methods section
  - **Issue** The Methods section states that simulations were run with "no special mass repartitioning" but does not specify the hydrogen mass repartitioning scheme used, if any. This is a minor detail but could affect reproducibility.
  - **Required correction** Specify whether hydrogen mass repartitioning was used and, if so, the scheme.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Results, Figure 1C
  - **Evidence pointer** Figure 1C
  - **Issue** The y-axis scale for a99SBdisp-TIP4PD in Figure 1C is 10 times smaller than for the other forcefields. This makes direct visual comparison difficult.
  - **Required correction** Use a consistent y-axis scale for all panels, or clearly indicate the different scales and explain why they are used.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Scientific importance
  - **Affected element** Discussion
  - **Evidence pointer** Discussion, paragraph on water models
  - **Issue** The discussion of water models is brief and does not fully explore the implications of the results for water model development. For example, the authors note that CHARMM36m-TIP3P* performs well despite using a 3-point water model, but do not discuss why this might be the case.
  - **Required correction** Expand the discussion on water models to provide more insight into the relationship between water model and forcefield performance.
- **Technical failings that need to be addressed before the case is established**
  1. The lack of quantitative analysis of intermolecular contacts in the ubiquitin simulations (R1-M1).
  2. The overstatement of the claim that all forcefields "correctly capture" secondary structure propensities (R1-M3).
  3. The speculative nature of the claim about multi-protein systems being the next challenge (R1-M2).
- **Assessment against Nature-style criteria**
  - **Originality** The study is original in its focus on multi-protein systems and extreme solubility cases, which are not commonly included in forcefield benchmarks. However, the overall approach of comparing forcefields on disordered proteins is not new.
  - **Scientific importance** The results are important for the molecular dynamics community, as they provide guidance on forcefield selection and highlight areas for improvement. The study is likely to be cited and used by others.
  - **Interdisciplinary readership** The study is primarily of interest to computational biophysicists and chemists. It may also be of interest to experimentalists studying protein aggregation and solubility, but the technical nature of the manuscript may limit its accessibility.
  - **Technical soundness** The simulations appear to be well-executed, but the analysis is largely qualitative. The lack of quantitative metrics for key claims (e.g., dimerization kinetics) weakens the technical soundness.
  - **Readability for nonspecialists** The manuscript is generally well-written, but the introduction and some technical details may be challenging for nonspecialists.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important question and provides useful data, but the central claims need to be supported by more rigorous quantitative analysis. The authors should address the concerns raised in R1-M1, R1-M2, and R1-M3 before the case is fully established.

## Risk / unsupported claims
- The claim that a99SBdisp-TIP4PD and ff19SB-OPC "better reproduce" a real solution of concentrated ubiquitin is not strongly supported due to the lack of quantitative analysis of intermolecular interactions and the short simulation timescales.
- The claim that "multi-protein systems as the next challenge for optimization" is speculative and not fully supported by the data, as only one multi-protein system was tested.
- The statement that "all four forcefields could correctly capture the secondary structures preferred by the two peptides" is an overstatement, as ff14SB-TIP3P over-stabilizes helix and a99SBdisp-TIP4PD/ff19SB-OPC fail to aggregate Aβ16-22.
- The claim that "the optimal balance between stabilizing and destabilizing interactions requires exquisite tuning" is a reasonable interpretation but is not directly tested in this study.