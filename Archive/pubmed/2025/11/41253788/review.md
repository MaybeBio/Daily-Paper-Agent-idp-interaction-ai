## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and figure legends
- **Assessment boundary** Scientific content, technical methodology, data interpretation, and claims as presented in the provided manuscript
- **Shared manuscript claim summary** The authors investigate the conformational behavior of the NUP98-HOXA9 (NHA9) oncoprotein across different assembly states, from dilute monomers to nanoclusters and macroscopic condensates. They report that the FG domain of NHA9 progressively expands as assembly size increases, that nanoclusters form below the saturation concentration, and that these nanoclusters exhibit micelle-like organization with the DNA-binding domain exposed at the periphery. The study combines single-molecule FRET, FCS, FLIM-FRET, coarse-grained simulations, and phase separation assays.
- **Visible evidence base** Figures 1-6, Supplementary Figures 1-21, Supplementary Tables 1-4, Methods section
- **Missing materials affecting confidence** Raw data files, full statistical analysis details, control experiment data for some assays, and complete simulation parameter files were not fully accessible in the provided text

## Reviewer

- **Overall assessment** This manuscript presents a comprehensive and technically sophisticated analysis of conformational changes in the NHA9 oncoprotein across different assembly states. The combination of single-molecule FRET, FCS, FLIM-FRET, and coarse-grained simulations is impressive and appropriate for the questions addressed. The finding that the FG domain progressively expands from monomers to nanoclusters to condensates is novel and potentially significant for understanding oncogenic transcription factor behavior. However, several technical concerns regarding data interpretation, particularly around the use of different labeling strategies and the potential for artifacts in crowded environments, need to be addressed before the conclusions can be fully supported.

- **Who would be interested in the results, and why** Researchers studying transcription factor phase separation, intrinsically disordered proteins, oncoprotein biology, and the biophysics of biomolecular condensates would find this work of interest. The study provides new insights into how conformational ensembles change during multimerization and phase separation, which is relevant to understanding transcriptional regulation in cancer and the general principles of IDP behavior in crowded environments.

- **Major strengths**
  1. The multi-technique approach combining single-molecule and ensemble methods provides complementary views of NHA9 behavior across length scales.
  2. The use of site-specific labeling via genetic code expansion for cellular measurements is technically advanced and minimizes perturbation.
  3. The integration of coarse-grained simulations with experimental data strengthens the interpretation of conformational changes.
  4. The systematic investigation from dilute to condensed states provides a complete picture of the assembly pathway.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the FG domain of NHA9 adopts a more expanded conformation in nanoclusters compared to monomers, based on smFRET measurements showing a second peak at lower transfer efficiency.
- **Evidence pointer** Figure 2b, 2d, 2e; Supplementary Figure 5
- **Concern** The interpretation of the lower-efficiency FRET peak as evidence of conformational expansion within nanoclusters relies on the assumption that the labeled protein behaves identically to unlabeled protein within the cluster. However, the authors note acceptor quenching during nanocluster formation (Supplementary Figure 4), which could affect the FRET efficiency measurements. The authors state they used lifetime-based analysis to avoid this issue, but the potential for differential quenching effects on different labeling positions is not fully addressed. Additionally, the possibility that the lower-efficiency peak represents a subpopulation of partially unfolded or misfolded protein within clusters, rather than a uniformly expanded conformation, is not discussed.
- **Why it matters** The central conclusion of progressive conformational expansion depends on accurate FRET measurements within heterogeneous, crowded environments. If quenching or other environmental effects systematically bias the measurements, the interpretation of expansion could be incorrect.
- **Resolution test** Provide control experiments demonstrating that the lifetime-based analysis is insensitive to acceptor quenching across all labeling positions. Additionally, show that the lower-efficiency peak is not due to protein degradation or misfolding by performing SDS-PAGE analysis of protein extracted from clusters and by testing whether the FRET efficiency distribution is stable over time.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that DNA binding reduces nanocluster formation, with specific DNA having a stronger effect than shuffled DNA.
- **Evidence pointer** Figure 3a, 3b; Supplementary Figure 6
- **Concern** The FCS and smFRET experiments showing reduced nanocluster formation in the presence of DNA are performed at concentrations where the DNA may not be fully saturated with protein. The apparent KD of 0.3 μM for DNA binding is close to the protein concentrations used (1-2 μM), meaning a significant fraction of protein may be unbound. The authors' explanation for the weaker effect at lower protein concentration (compensatory mechanism) is speculative and not directly tested. Furthermore, the effect of DNA on condensate formation at higher concentrations (above the saturation threshold) is not examined, leaving open the question of whether DNA promotes or inhibits phase separation under more physiologically relevant conditions.
- **Why it matters** The claim that DNA binding modulates nanocluster formation has implications for understanding how NHA9 interacts with chromatin in cells. If the effect is primarily due to non-specific electrostatic interactions rather than specific DNA binding, the biological significance would be different.
- **Resolution test** Perform DNA binding experiments across a wider range of protein and DNA concentrations to establish the stoichiometry of the interaction. Test whether the effect on nanocluster formation correlates with the fraction of protein bound to DNA. Additionally, examine the effect of DNA on condensate formation above the saturation concentration.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that the micelle-like organization of NHA9 nanoclusters, with the DNA-binding domain exposed at the periphery, is functionally significant for DNA interactions.
- **Evidence pointer** Figure 6c, 6d; Supplementary Figures 14-18
- **Concern** The micelle-like organization is inferred primarily from coarse-grained simulations, with limited direct experimental validation. The density profiles in Figure 6d show a preference for HOXA9 at the interface, but this is based on simulations with a specific force field and elastic network constraints that may not accurately capture the behavior of the folded domain. The authors acknowledge limitations of the force field but do not provide experimental evidence for surface exposure of the DNA-binding domain, such as antibody accessibility or crosslinking experiments.
- **Why it matters** The proposed functional significance of the micelle-like structure, particularly for DNA binding, is a key claim of the paper. Without experimental validation, this remains a simulation-based prediction rather than an established finding.
- **Resolution test** Perform experiments to test surface exposure of the DNA-binding domain in nanoclusters, such as limited proteolysis, chemical crosslinking, or immunofluorescence with antibodies against the HOXA9 domain. Alternatively, use FRET between a label on the DNA-binding domain and a membrane-impermeable quencher to assess accessibility.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the FG domain remains disordered and dynamic within nanoclusters and condensates, based on the observation of dynamic quenching in 2D histograms.
- **Evidence pointer** Supplementary Figure 5c, 8a, 8b
- **Concern** The conclusion that the FG domain remains dynamic within condensed phases is based on indirect evidence from FRET measurements. The authors do not directly measure dynamics, such as fluorescence correlation spectroscopy within condensates or NMR relaxation measurements. The observation of dynamic quenching could also be explained by static heterogeneity within the cluster, where different molecules adopt different conformations, rather than rapid interconversion between conformations.
- **Why it matters** The claim of dynamic behavior within condensates is important for understanding the physical properties of these assemblies and their potential function. If the FG domain is static within clusters, this would have different implications for how NHA9 interacts with other molecules.
- **Resolution test** Perform fluorescence recovery after photobleaching (FRAP) experiments within individual nanoclusters to measure the mobility of NHA9 molecules. Alternatively, use fluorescence correlation spectroscopy with a focused laser to measure diffusion within clusters.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract uses the term "macrophases" which is unusual and not clearly defined. The term "macroscopic phase" or "condensate" would be more standard and clearer.
- **Required correction** Replace "macrophases" with "macroscopic condensates" or "macroscopic phases" for clarity and consistency with the main text.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, FCS measurements
- **Evidence pointer** Methods section, FCS measurements
- **Issue** The FCS measurements are described as using 120 repeated measurements with 10-second sampling times, but the total measurement duration and the criteria for selecting which measurements to include in the analysis are not specified. This could affect the reproducibility of the results.
- **Required correction** Provide details on the total measurement time, the criteria for data inclusion/exclusion, and how the distribution of diffusion coefficients was calculated from the repeated measurements.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 2e
- **Evidence pointer** Figure 2e
- **Issue** The scaling law fit in Figure 2e appears to have a very large confidence interval, which may indicate that the data are not well described by a simple power law. The authors should discuss this and consider whether alternative models might better describe the data.
- **Required correction** Provide the goodness-of-fit parameters and discuss the appropriateness of the power law model for the data. Consider showing individual data points rather than only the fitted line.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion of the biological implications of the findings is somewhat speculative, particularly regarding the role of micelle-like structures in oncogenic transcription. The authors should more clearly distinguish between what is directly supported by their data and what is speculative.
- **Required correction** Revise the discussion to clearly separate findings supported by experimental evidence from hypotheses that require further testing.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Methods, simulations
- **Evidence pointer** Methods section, simulations
- **Issue** The description of the simulation setup mentions that the HPS-Urry force field was used, but the specific parameters for the elastic network constraints and the choice of the number of chains in each simulation are not fully detailed. This limits the reproducibility of the simulations.
- **Required correction** Provide a more detailed description of the simulation parameters, including the elastic network spring constants, the number of chains in each simulation, and the criteria for determining cluster membership.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** Figure 3a
- **Evidence pointer** Figure 3a
- **Issue** The FCS data in Figure 3a show distributions of diffusion coefficients, but it is not clear how many independent experiments were performed and whether the differences between conditions are statistically significant.
- **Required correction** Provide statistical analysis of the FCS data, including the number of independent experiments and appropriate significance tests.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, cellular measurements
- **Evidence pointer** Figure 5
- **Issue** The cellular measurements are performed on a limited number of cells (approximately 30 per variant), and the authors do not report the variability between cells or the criteria for selecting cells for analysis. This could introduce bias.
- **Required correction** Provide information on the cell-to-cell variability and the criteria for cell selection, and consider reporting the distribution of measured values across cells.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction
- **Evidence pointer** Introduction
- **Issue** The introduction could benefit from a more thorough discussion of previous studies on NUP98 fusion proteins and their phase behavior, to better contextualize the novelty of the current findings.
- **Required correction** Expand the introduction to include a more comprehensive review of relevant literature on NUP98 fusions and IDP phase separation.

## Risk / unsupported claims
- The claim that the FG domain of NHA9 progressively expands with increasing assembly size is supported by the data, but the quantitative values of the scaling exponents in different states should be interpreted with caution given the potential for environmental effects on FRET measurements.
- The claim that nanoclusters are micelle-like with the DNA-binding domain exposed at the periphery is primarily based on simulations and requires experimental validation.
- The claim that DNA binding reduces nanocluster formation through specific interactions is supported by the differential effect of specific vs. shuffled DNA, but the stoichiometry and mechanism are not fully established.
- The claim that the FG domain remains dynamic within condensates is inferred from indirect evidence and requires direct measurement of dynamics.
- The biological significance of the findings for transcriptional regulation in cancer is discussed in a speculative manner and is not directly tested in this manuscript.
- The use of the term "macrophases" in the title and abstract is not standard and may be confusing to readers.