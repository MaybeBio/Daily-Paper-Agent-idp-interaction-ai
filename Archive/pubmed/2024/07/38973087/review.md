## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, objectives, methodology, results and discussion, conclusion, and supplementary material references.
- **Assessment boundary** Scientific content, methodological rigor, validity of claims relative to the evidence presented, and alignment with Nature-style criteria. Editorial or formatting issues are noted only where they affect scientific clarity.
- **Shared manuscript claim summary** The authors use fully atomistic explicit water molecular dynamics simulations to investigate the intrinsically disordered regulatory domain (REG, residues 351–393) of the tumor suppressor p53. They compare unmodified, singly phosphorylated (S392), and multisite phosphorylated variants, with and without N-terminal restraint, to assess conformational dynamics, secondary structure propensities, salt bridge formation, and energy landscapes. They report that single phosphorylation induces specific structural features and enhanced functionality, while overphosphorylation leads to conformational restriction and dysfunction.
- **Visible evidence base** Main text figures (Figures 1–8), tables (Tables 1–2), and referenced supplementary figures and tables (Figures S1–S31, Tables S1–S5). Experimental validation via chemical shift predictions compared to published NMR data and crystallographic reference structures.
- **Missing materials affecting confidence** Supplementary figures and tables are referenced but not provided in the submitted material. Simulation input parameters, force field modification details, and convergence criteria are described only partially. No raw trajectory data or reproducibility scripts are included.

## Reviewer
- **Overall assessment** This manuscript presents a systematic computational study of phosphorylation effects on the p53 regulatory domain, with a useful comparison of single versus multisite modification and an innovative test of N-terminal restraint. The work is technically competent and addresses a biologically relevant question. However, the central claims regarding functional implications are extrapolated from limited simulation evidence, and several methodological details are insufficiently described to fully assess robustness. The study is a solid contribution to the computational biophysics literature but does not yet establish the broad functional conclusions implied by the title and abstract.
- **Who would be interested in the results, and why** Researchers in computational biophysics and molecular dynamics simulation of intrinsically disordered proteins, as well as biochemists and cell biologists studying p53 regulation and post-translational modification. The methodological findings on terminal restraint and phosphorylation effects on conformational ensembles are relevant to those developing simulation protocols for IDPs.
- **Major strengths** 1. Systematic comparison of three phosphorylation states with multiple analysis metrics (RG, EEDIST, SASA, DSSP, salt bridges, free energy landscapes). 2. Inclusion of N-terminal restraint as a methodological variable, addressing a realistic boundary condition for terminal IDRs. 3. Attempt to validate simulations against experimental data via chemical shift predictions and crystallographic references. 4. Clear presentation of energy landscape differences between phosphorylation states.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (simulation length and convergence), R1-M2 (force field validation for phosphorylated residues), R1-M3 (statistical treatment of single trajectories), R1-M4 (overinterpretation of functional implications).
- **Assessment against Nature-style criteria** Originality: Moderate. The application of MD to p53 REG phosphorylation is not entirely new, but the systematic comparison and restraint methodology offer some novelty. Scientific importance: Moderate. The findings are relevant to understanding p53 regulation but are largely confirmatory of existing hypotheses rather than paradigm-shifting. Interdisciplinary readership: Limited. The work is primarily of interest to computational biophysicists and p53 specialists, with limited accessibility to a broader biological audience. Technical soundness: Adequate but with concerns about convergence, force field validation, and statistical power. Readability for nonspecialists: The manuscript is written in a technical style that assumes familiarity with MD methods and IDP concepts, which may limit accessibility.
- **Recommendation posture** Supportive if technical concerns are resolved. The core computational work appears sound, but the functional claims require stronger evidence and the methodological limitations must be addressed.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the trajectories provide a detailed understanding of phosphorylation effects on conformational dynamics, flexibility, structural effects, protein interactivity, and energy landscapes.
- **Evidence pointer** Methodology section, Results and Discussion section, Tables 1–2, Figures 4–8
- **Concern** Each system is simulated for 1.1 microseconds with five replicates. For an intrinsically disordered protein of 43 residues, this sampling may be insufficient to achieve converged conformational ensembles, particularly for the free energy landscapes and rare conformational states described. The authors do not provide convergence metrics, block analysis, or comparison of replicate variability to support that the observed differences between phosphorylation states exceed statistical noise.
- **Why it matters** The central conclusions about phosphorylation-induced changes in conformational ensembles and energy landscapes depend on the assumption that the simulations have adequately sampled the accessible conformational space. Without demonstrated convergence, the reported differences between REGNP, REGSP, and REGFP could be artifacts of insufficient sampling.
- **Resolution test** Provide convergence analysis, such as time-dependent block averaging of key observables, comparison of independent replicate distributions, and assessment of whether the free energy landscapes stabilize over the simulation time. If convergence is not achieved, extend simulation times or employ enhanced sampling methods.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that phosphorylated residues were integrated into the AMBER99SB-ILDN force field by adding new parameters, and that this approach was adequate for IDP simulations.
- **Evidence pointer** Methodology section, force field description
- **Concern** The manuscript does not provide details on how the phosphorylated residue parameters were derived, validated, or tested. Phosphoserine and phosphothreonine parameters are not standard in AMBER99SB-ILDN, and the accuracy of these parameters is critical for the validity of the results. No comparison to experimental data for phosphorylated IDPs is provided to validate the force field choice.
- **Why it matters** The entire study hinges on the accurate representation of phosphorylated residues. If the parameters are inaccurate, all conclusions about phosphorylation effects are compromised.
- **Resolution test** Provide the source of the phosphorylated residue parameters, validation against experimental data (e.g., NMR chemical shifts, J-couplings, or SAXS for phosphorylated IDPs), and a discussion of potential limitations. If parameters are from a published source, cite and justify their use.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors report quantitative differences in salt bridge occupancies, secondary structure propensities, and free energy landscape features between phosphorylation states.
- **Evidence pointer** Tables 1–2, Figures 4–8, Supplementary Figures S5–S12, S27–S29
- **Concern** The analysis appears to be based on pooled data from five replicate trajectories, but the authors do not report standard errors, confidence intervals, or statistical tests for the reported differences. For example, the claim that salt bridges between R363 and K381 increase by 10–20% upon single phosphorylation is presented without error estimates. Similarly, the secondary structure percentages in Table 2 lack uncertainty quantification.
- **Why it matters** Without statistical treatment, the reader cannot assess whether the observed differences between systems are meaningful or within the range of natural fluctuation for IDPs.
- **Resolution test** Report mean and standard deviation or standard error for all quantitative metrics across replicates. Perform statistical tests (e.g., bootstrap or permutation tests) to assess the significance of differences between phosphorylation states.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The abstract and conclusion state that the study provides a detailed understanding of the impact of phosphorylation on protein interactivity and functional implications for p53, including a potential explanation for dysfunction associated with multisite phosphorylation.
- **Evidence pointer** Abstract, Conclusion section
- **Concern** The simulations are performed on an isolated REG fragment, not on full-length p53 or in complex with binding partners. The claims about "protein interactivity" are based on inferred changes in solvent accessibility and salt bridge formation, not on direct measurements of binding. The functional implications for p53 dysfunction are speculative and not directly tested.
- **Why it matters** Overstating functional conclusions from isolated domain simulations may mislead readers about the biological relevance of the findings.
- **Resolution test** Soften the language in the abstract and conclusion to clearly distinguish between simulation-observed phenomena and hypothesized biological implications. Alternatively, add discussion of how the findings relate to existing experimental data on p53 function.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "the intrinsically disordered regulatory domain of p53" is used without specifying the residue range, which is only introduced later in the methodology. This may confuse readers unfamiliar with p53 domain architecture.
- **Required correction** Specify the residue range (e.g., "the intrinsically disordered regulatory domain (residues 351–393) of p53") in the abstract.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical clarity
- **Affected element** Methodology, force field modification
- **Evidence pointer** Methodology section, paragraph on phosphorylation
- **Issue** The description of how phosphorylated residues were added to the force field is vague. The authors state that "new parameters" were added but do not specify the atom types, charge derivation method, or whether parameters were taken from existing literature.
- **Required correction** Provide a detailed description of the parameterization process, including the source of parameters, charge derivation method, and any validation performed.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Table 1
- **Evidence pointer** Table 1
- **Issue** The table reports average values for RG, EEDIST, and SASA but does not include standard deviations or standard errors, making it impossible to assess variability across replicates.
- **Required correction** Add standard deviation or standard error columns to Table 1.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Scientific context
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph on salt bridges
- **Issue** The introduction cites general references for salt bridge importance in IDPs but does not specifically discuss prior computational studies of p53 REG phosphorylation. This makes it difficult to assess the novelty of the current work.
- **Required correction** Add a brief review of prior MD studies on p53 REG or other phosphorylated IDPs to contextualize the current contribution.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical clarity
- **Affected element** Methodology, simulation setup
- **Evidence pointer** Methodology section, simulation parameters
- **Issue** The authors state that a rhombic box with a minimum distance of 10 nm from the residues was used, but this is unusually large for a 43-residue peptide and may be computationally wasteful. The rationale for this choice is not explained.
- **Required correction** Justify the box size or clarify whether this was necessary to avoid periodic image artifacts.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methodology, analysis details
- **Evidence pointer** Methodology section, analysis paragraph
- **Issue** The manuscript does not specify the software versions for analysis tools (e.g., MdTraj, PyEMMA, SciPy, Scikit-learn) or the exact parameters used for clustering and tICA.
- **Required correction** Provide software versions and analysis parameters to ensure reproducibility.

## Risk / unsupported claims
- The claim that single phosphorylation at S392 "enhances protein functionality" is not directly supported by the simulation data, which only show structural and dynamic changes in an isolated domain.
- The claim that multisite phosphorylation provides "a potential explanation for the functional malfunctions associated with multisite phosphorylation" is speculative and not tested against functional assays.
- The statement that the N-terminal restraint method "challenges the modern approach" to simulating terminal IDRs is overstated, as the authors only demonstrate a modest effect on one system.
- The assertion that the simulations "show the wealth of information and detailed understanding that can be obtained" is not fully supported given the lack of convergence analysis and statistical treatment.
- The comparison of simulated distances to crystallographic structures (8f2i) is presented as validation, but the manuscript does not discuss the limitations of comparing an isolated, unrestrained simulation to a crystal lattice context.