## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and conclusions
- **Assessment boundary** Scientific validity, methodological soundness, reproducibility, and claims-to-evidence alignment
- **Shared manuscript claim summary** The authors use atomistic molecular dynamics simulations of model condensates to identify physicochemical rules governing small-molecule partitioning, then develop a coarse-grained approach (MAPPS) to predict partitioning into biologically relevant condensates, validated against atomistic simulations including FUS LCD condensates
- **Visible evidence base** Abstract, full text of Introduction, Results and Discussion, Conclusions, and Methods sections; figures referenced but not visible; supplementary material referenced but not provided
- **Missing materials affecting confidence** Figures, tables, and supplementary information referenced throughout (Figures 1-5, Tables S1-S10, Figures S1-S16) are not available for inspection; simulation parameter details and validation statistics are partially described but cannot be fully assessed

## Reviewer
- **Overall assessment** The manuscript addresses an important and timely problem in biomolecular condensate research: predicting small-molecule partitioning. The authors combine atomistic simulations with a novel coarse-grained modeling approach (MAPPS) to develop a computationally efficient prediction method. The central claims are plausible and the methodological framework is creative, but the evidence base available for review is incomplete. Several claims regarding transferability, predictive accuracy, and mechanistic insight require closer scrutiny of the actual data. The systematic comparison between atomistic and coarse-grained results is a strength, but the reported limitations in polar condensates and for hydrophilic molecules raise questions about the general applicability of the approach.

- **Who would be interested in the results, and why** Researchers in biomolecular condensate biology, drug discovery targeting condensates, computational biophysics, and coarse-grained simulation method development would find this work relevant. The MAPPS approach offers a practical tool for screening small-molecule partitioning, which could inform drug development strategies. The mechanistic insights into how condensate chemical environment influences partitioning would interest experimentalists studying condensate selectivity.

- **Major strengths** The manuscript addresses a significant gap in the field by moving beyond phenomenological descriptions to mechanistic understanding of small-molecule partitioning. The development of a computationally efficient prediction method (MAPPS) with demonstrated transferability across different condensate types is valuable. The systematic comparison between atomistic and coarse-grained simulations provides a rigorous validation framework. The identification of dipole-mediated interactions as a mechanism for partitioning into polar condensates is a novel insight.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The claim that MAPPS "reproduces atomistic partition coefficients" in both model systems and FUS LCD condensates
  - **Evidence pointer** Figures 4-5, Tables S6-S7, location not provided
  - **Concern** The quantitative agreement between coarse-grained and atomistic partition coefficients is claimed but the actual correlation coefficients, error metrics, and per-compound comparisons are not visible in the provided text. The manuscript states "good agreement" and reports r = 0.95 for FUS LCD, but the range of K values, the number of compounds tested, and the statistical significance of the agreement are not fully described.
  - **Why it matters** The central claim of the paper is that MAPPS can predict partitioning accurately. Without visible quantitative validation data, the reader cannot assess whether the agreement is sufficient for predictive use, particularly given the acknowledged systematic overestimation in polar condensates.
  - **Resolution test** Provide the full comparison data between CG and atomistic K values for all compounds and condensates, including correlation coefficients, mean absolute errors, and confidence intervals. Demonstrate that the agreement holds across the full range of K values and compound types.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Methodological validity
  - **Claim pointer** The claim that the empirical relationship in Equation 1 (εSM-X = εSM-Y fitted × ASM-X × DX) captures the effective small molecule-protein interactions in phase-separated systems
  - **Evidence pointer** Equation 1, Figure 3d, location not provided
  - **Concern** The derivation of Equation 1 is not fully justified. The affinity score ASM-X is computed from single-chain simulations, while DX is derived from condensate density ratios. The manuscript reports a correlation of 0.92 between fitted and predicted εSM-X values, but the physical basis for multiplying these two factors is not clearly explained. The validity of this approximation across different condensate compositions and small molecule types is unclear.
  - **Why it matters** The empirical relationship is the core of the MAPPS method. If the underlying approximation is not physically justified or fails for certain residue types or compound classes, the predictive power of the method is compromised.
  - **Resolution test** Provide a more detailed derivation or physical justification for Equation 1. Show that the approximation holds across a wider range of condensate compositions and small molecule properties, and discuss any cases where the relationship breaks down.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Generalizability
  - **Claim pointer** The claim that "the protein sequence can exert a selective pressure, thereby influencing small-molecule partitioning" based on applying MAPPS to various LCD-based condensates
  - **Evidence pointer** Figure 5, location not provided
  - **Concern** The manuscript demonstrates MAPPS application to FUS, hnRNPA1, EWSR1, and TIA1 LCDs, but the biological significance of the observed differences in partitioning is not discussed in depth. The claim of "selective pressure" implies functional relevance, but the connection to biological function or therapeutic targeting is not established.
  - **Why it matters** The broader significance of the work depends on whether the observed partitioning differences translate to biologically meaningful selectivity that could be exploited therapeutically.
  - **Resolution test** Discuss the biological implications of the observed partitioning differences, and if possible, compare predictions with experimental data on small-molecule partitioning into these condensates.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical completeness
  - **Claim pointer** The claim that the backmapping procedure from CG to atomistic resolution produces reliable all-atom configurations of FUS LCD condensates
  - **Evidence pointer** Methods section, "All-Atom Simulations of FUS LCD", location not provided
  - **Concern** The backmapping procedure using Pulchra and Martini2/backward is described, but the validation of the resulting atomistic configurations is not presented. Questions arise about whether the backmapped structures maintain the correct condensate morphology, density, and dynamics, and whether 600 ns of simulation is sufficient for equilibration of such a large system.
  - **Why it matters** The reliability of the atomistic FUS LCD simulations depends on the quality of the initial configurations. If the backmapping introduces artifacts, the partition coefficients derived from these simulations could be biased.
  - **Resolution test** Provide validation of the backmapped structures (e.g., comparison of structural properties with directly simulated systems, convergence analysis, density profiles) and justify the simulation length.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Abstract and Introduction
  - **Evidence pointer** Abstract, Introduction, location not provided
  - **Issue** The abstract states "we first exploit atomistic molecular dynamics simulations" but the term "exploit" is unusual in this context. The introduction could more clearly distinguish between the model condensates and biologically relevant condensates.
  - **Required correction** Rephrase to "we first use atomistic molecular dynamics simulations" and clarify the relationship between model and biological condensates.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** Results section on peptide-based condensates
  - **Evidence pointer** Figure 4, location not provided
  - **Issue** The manuscript reports "good agreement" and "systematic overestimation" but does not provide quantitative error metrics or statistical tests for the comparison between CG and atomistic results.
  - **Required correction** Report quantitative metrics such as mean absolute error, root-mean-square error, and confidence intervals for the partition coefficient comparisons.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Methodological detail
  - **Affected element** Methods section on PMF calculations
  - **Evidence pointer** Methods, "Potential-of-Mean-Force Calculations", location not provided
  - **Issue** The description of PMF calculations lacks details on the number of umbrella sampling windows, the range of distances sampled, and the convergence criteria used.
  - **Required correction** Provide additional details on the PMF calculation setup and convergence assessment.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Discussion of limitations
  - **Evidence pointer** Conclusions, location not provided
  - **Issue** The limitations of the MAPPS approach are acknowledged but not discussed in sufficient depth. The systematic overestimation in polar condensates and deviations for hydrophilic molecules are mentioned but not analyzed in terms of underlying causes.
  - **Required correction** Expand the discussion of limitations to include potential physical reasons for the observed discrepancies and how they might be addressed in future work.

- **Technical failings that need to be addressed before the case is established** R1-M1 (validation data not visible), R1-M2 (physical basis of Equation 1 not fully justified)

- **Assessment against Nature-style criteria** 
  - Originality: The work is original in its systematic approach to understanding small-molecule partitioning mechanisms and the development of a minimal coarse-grained model for prediction. The combination of atomistic and coarse-grained simulations for this purpose is novel.
  - Scientific importance: The problem addressed is of high importance for drug discovery targeting condensates. The mechanistic insights and predictive tool could significantly advance the field.
  - Interdisciplinary readership: The work bridges computational biophysics, chemical biology, and drug discovery, making it relevant to a broad readership.
  - Technical soundness: The methodological framework is sound in principle, but the incomplete visibility of validation data and the empirical nature of Equation 1 raise concerns that need to be addressed.
  - Readability for nonspecialists: The manuscript is generally well-written and accessible, though some methodological details may be challenging for nonspecialists. The figures and tables would likely aid comprehension but are not available for review.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a valuable contribution to the field with a novel approach and important insights. However, the central claims of predictive accuracy and the physical basis of the empirical model need to be more rigorously demonstrated and clearly presented. The authors should provide complete validation data and a more thorough discussion of the limitations and applicability of the MAPPS approach.

## Risk / unsupported claims
- The claim that MAPPS "reproduces atomistic partition coefficients" cannot be fully assessed without the actual comparison data
- The claim that "the protein sequence can exert a selective pressure" implies biological significance that is not established
- The claim that the empirical relationship in Equation 1 captures the essential physics of small molecule-protein interactions in condensates is not fully supported by the provided text
- The claim that the backmapping procedure produces reliable atomistic configurations is not validated in the visible text
- The claim that the model condensates "capture the phase separation behavior of biomolecular condensates" is stated but not demonstrated in the provided text