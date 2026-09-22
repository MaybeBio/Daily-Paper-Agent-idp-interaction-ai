## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, technical soundness, and claims as presented in the provided manuscript
- **Shared manuscript claim summary** The authors report the first recombinant expression and purification of the HNF-1A transactivation domain (TAD), characterize its disordered conformation using bioinformatics, SRCD, and SAXS, and present evidence for liquid-liquid phase separation (LLPS) behavior supported by in vitro experiments and molecular dynamics simulations.
- **Visible evidence base** Main text including Methods, Results and Discussion, Figures 1-4 (referenced), Supplementary Tables S1, Supplementary Figures S1-S3, Supplementary Video S1 (referenced)
- **Missing materials affecting confidence** Figures and supplementary materials not provided; raw data not available; detailed simulation parameters partially described but not fully reproducible from text alone

## Reviewer
- **Overall assessment** This manuscript addresses a relevant gap in understanding the structural properties of the HNF-1A TAD, a region important for transcription factor function in pancreatic beta-cells. The authors combine bioinformatic predictions with biophysical characterization and computational simulations to propose that the TAD is intrinsically disordered and capable of driving LLPS. The work is technically sound in several aspects, particularly the successful purification of a challenging protein construct and the use of multiple complementary methods. However, the manuscript falls short of establishing a definitive case for the biological relevance of the observed LLPS, and several technical details require clarification. The study is more descriptive than mechanistic, and the direct link between the in vitro observations and in vivo transcriptional regulation remains speculative. The findings will be of interest to researchers studying transcription factor structure-function relationships and LLPS in gene regulation, but the impact is limited by the lack of functional validation and the preliminary nature of the cellular data.

- **Who would be interested in the results, and why** Researchers studying hepatocyte nuclear factors and MODY diabetes pathogenesis will find the structural characterization of the HNF-1A TAD valuable. The LLPS community, particularly those interested in transcription factor condensation and transcriptional regulation, will be interested in the identification of a new candidate phase-separating transcription factor. Structural biologists working on intrinsically disordered proteins and those developing purification protocols for such proteins may also find methodological value. The work could inform future studies on HNF1A-MODY variants located in the TAD region.

- **Major strengths** The manuscript addresses a previously understudied region of an important transcription factor. The development of a purification protocol for the TAD-containing construct is a practical contribution. The combination of multiple biophysical techniques (SRCD, SAXS) with bioinformatic predictions provides complementary evidence for intrinsic disorder. The inclusion of molecular dynamics simulations to support LLPS behavior adds a computational dimension that strengthens the overall argument. The authors are appropriately cautious in interpreting their cellular imaging data and acknowledge limitations.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that the purified DBD-TAD protein is suitable for biophysical characterization and that the observed properties reflect the native behavior of the TAD.
  - **Evidence pointer** Section 3.4, Section 3.5, Figure 2
  - **Concern** The manuscript reports significant protein degradation from the C-terminus, with the purified product containing degradation products. The authors state they conducted experiments "immediately after purification" to avoid gradual degradation, but it is unclear what proportion of the final sample was full-length DBD-TAD versus degradation products. If a substantial fraction of the sample is truncated, the SRCD and SAXS data may not accurately represent the full TAD. The authors do not provide quantitative assessment of sample homogeneity (e.g., densitometry of the final gel, mass spectrometry quantification).
  - **Why it matters** The central structural conclusions (disorder, dimensions, LLPS) depend on the integrity of the purified protein. If degradation products dominate, the observed biophysical properties could be artifacts of truncated species rather than properties of the intact TAD.
  - **Resolution test** Provide quantitative analysis of the final purified sample composition (e.g., gel densitometry, intact mass spectrometry). If degradation is significant, repeat key experiments with a more stable construct (e.g., with C-terminal tag or protease inhibitor optimization) or demonstrate that the degradation products do not confound the interpretations.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence strength
  - **Claim pointer** The authors state that "HNF-1A undergoing liquid-liquid phase separation" is supported by their data and "may be of biological relevance for gene transcriptional processes in pancreatic beta-cells."
  - **Evidence pointer** Section 3.6, Figure 3, Section 3.7, Figure 4
  - **Concern** The evidence for LLPS is indirect. The DIC microscopy shows droplet-like structures, but no experiments demonstrate liquid properties (e.g., fusion, dripping, fluorescence recovery after photobleaching). The authors acknowledge this limitation but still present LLPS as a central finding. The molecular dynamics simulations use a coarse-grained model with parameters that may not accurately capture the specific sequence properties of the HNF-1A TAD. The cellular imaging data show punctae in fixed cells, which could be artifacts of fixation or represent other nuclear structures. The claim that LLPS "may be of biological relevance" is speculative without functional experiments linking phase separation to transcriptional activity.
  - **Why it matters** LLPS is a major claim of the manuscript and is highlighted in the abstract. Without direct evidence of liquid properties and functional relevance, the claim is not established. Overinterpretation of preliminary data could mislead the field.
  - **Resolution test** Perform FRAP experiments on the in vitro droplets to demonstrate liquid behavior. Conduct live-cell imaging to verify nuclear punctae in living cells. If possible, test whether mutations that disrupt LLPS affect HNF-1A transcriptional activity in a reporter assay.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Reproducibility
  - **Claim pointer** The authors describe molecular dynamics simulations of LLPS using the 1BPA model, with parameters from Driver et al. 2022.
  - **Evidence pointer** Section 2.7, Section 3.7, Figure 4
  - **Concern** The simulation details are insufficient for reproduction. The manuscript does not specify the number of independent simulations, the equilibration criteria, the system size beyond the number of molecules, the force field parameters specific to the HNF-1A TAD sequence, or how the initial condensed phase was generated. The convergence assessment is described only as "sampled every 5 ns to determine whether convergence was reached" without defining the criteria.
  - **Why it matters** Reproducibility is a core requirement for computational studies. Without sufficient detail, other groups cannot verify or build upon these simulations.
  - **Resolution test** Provide complete simulation parameters, including system preparation, equilibration protocol, production run details, and convergence criteria. Consider depositing simulation input files and trajectories in a public repository.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Section 3.5, Table 2
  - **Evidence pointer** Table 2
  - **Issue** The secondary structure percentages from BeStSel and DichroIDP differ substantially (e.g., beta-sheet content). The authors do not discuss the discrepancies or explain which algorithm is more reliable for this protein.
  - **Required correction** Add a brief discussion of the differences between the two deconvolution methods and justify the interpretation.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Section 3.2, Figure 1C
  - **Evidence pointer** Figure 1C
  - **Issue** The charge distribution analysis shows very few charged residues in the TAD, but the authors do not provide a quantitative comparison to other known disordered regions or transcription factor TADs.
  - **Required correction** Include a quantitative comparison (e.g., mean net charge, fraction of charged residues) to contextualize the finding.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interpretation
  - **Affected element** Section 3.6, Figure 3C
  - **Evidence pointer** Figure 3C
  - **Issue** The nuclear punctae in fixed MIN6 cells are interpreted as potential condensates, but the authors do not discuss alternative explanations such as replication foci, splicing speckles, or antibody aggregation artifacts.
  - **Required correction** Add a sentence acknowledging alternative interpretations and suggesting future experiments to distinguish them.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Technical detail
  - **Affected element** Section 2.4, Supplementary Table S1
  - **Evidence pointer** Supplementary Table S1
  - **Issue** The SAXS data analysis mentions molecular weight estimates from different methods with varying results, but the authors do not explain which estimate is most reliable for a disordered protein.
  - **Required correction** Briefly discuss the reliability of each molecular weight estimation method for intrinsically disordered proteins.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Literature context
  - **Affected element** Section 3.2, Section 3.6
  - **Evidence pointer** Not applicable
  - **Issue** The discussion of alternative activation domains and LLPS in transcription factors could be strengthened by citing more recent work on the sequence determinants of phase separation and the role of TADs in condensate formation.
  - **Required correction** Add relevant recent references to contextualize the findings within the broader LLPS field.

- **Technical failings that need to be addressed before the case is established** R1-M1 (sample homogeneity), R1-M2 (LLPS evidence), R1-M3 (simulation reproducibility)

## Risk / unsupported claims
- The claim that the TAD "may be of biological relevance for gene transcriptional processes" is speculative and not directly tested.
- The interpretation of nuclear punctae in fixed cells as potential condensates is not supported by live-cell data or co-localization studies.
- The statement that the TAD "promotes LLPS" is based on indirect evidence and simulations, not direct demonstration of liquid properties.
- The biological implications for HNF1A-MODY are mentioned but not developed or supported by experimental data.
- The claim that the purification protocol is "the first" for the HNF-1A TAD cannot be fully verified without a more comprehensive literature search, though it appears plausible based on the cited literature.