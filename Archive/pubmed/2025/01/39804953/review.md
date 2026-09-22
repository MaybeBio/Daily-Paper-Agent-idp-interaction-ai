## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, supporting information references)
- **Assessment boundary** Scientific content, methodological rigor, claims versus evidence, and presentation quality as presented in the provided text
- **Shared manuscript claim summary** The authors benchmark six residue-resolution coarse-grained models (HPS, HPS-cation–π, HPS-Urry, CALVADOS2, Mpipi, Mpipi-Recharged) against experimental data for phase behaviour and viscosity of seven A1-LCD variants, concluding that Mpipi, Mpipi-Recharged, and CALVADOS2 perform best, with Mpipi-Recharged most accurate overall.
- **Visible evidence base** Main text figures (Figs 1–8), supplementary figures (S1–S4), tables (Table 1, S1 Table), methods section, and referenced experimental data from Refs [77, 78]
- **Missing materials affecting confidence** Full figure data (numerical values, error bars), simulation convergence metrics, force field parameter tables, experimental fitting procedures, and detailed statistical analysis are not fully available in the provided text

## Reviewer
- **Overall assessment** This manuscript presents a systematic and timely benchmark of six residue-resolution coarse-grained models for simulating biomolecular condensates, using a well-chosen protein system (A1-LCD and variants) with available experimental data. The study addresses an important gap in the field by evaluating not only thermodynamic properties (phase diagrams, critical temperatures, saturation concentrations) but also material properties (viscosity), which are rarely compared across models. The results are clearly presented and the conclusions are largely supported by the data shown. However, several methodological details and statistical considerations need clarification to fully establish the robustness of the claims, particularly regarding the comparison metrics, the treatment of uncertainties, and the generalizability of the findings beyond the A1-LCD system.

- **Who would be interested in the results, and why** Researchers in the fields of computational biophysics, biomolecular condensates, intrinsically disordered proteins, and coarse-grained modelling. The study provides practical guidance for model selection in condensate simulations, which is directly relevant to the growing community studying phase separation and its role in health and disease. The benchmarking approach and the emphasis on viscosity as a stringent test will also interest method developers working on improving coarse-grained force fields.

- **Major Strengths**
  1. Systematic comparison of six models on the same protein system with consistent simulation protocols, enabling fair model assessment.
  2. Inclusion of viscosity as a benchmark property, which is a demanding and under-explored test for CG models.
  3. Use of multiple A1-LCD variants with experimental data provides a robust test of sequence sensitivity.
  4. Clear presentation of results with informative figures (phase diagrams, correlation plots, contact maps).
  5. The study establishes a link between model performance and the ranking of intermolecular interactions, providing mechanistic insight into why certain models perform better.
  6. Provision of simulation scripts and data in a public repository enhances reproducibility.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor and uncertainty quantification
- **Claim pointer** The manuscript claims that Mpipi-Recharged is the most accurate model for predicting critical temperatures, saturation concentrations, and viscosities, with quantitative accuracy (e.g., deviations of less than ~3% for critical temperatures).
- **Evidence pointer** Figures 2, 3, 5, 6; Section 2.1–2.3; Section 4.6
- **Concern** The comparison between simulation predictions and experimental data relies on metrics (D, Pearson correlation coefficient) that are computed without explicit treatment of uncertainties. The manuscript does not report error bars or confidence intervals for the simulated quantities (e.g., critical temperatures, saturation concentrations, viscosities) or for the derived metrics. Without this information, it is difficult to assess whether the differences between models (e.g., Mpipi vs. Mpipi-Recharged) are statistically significant. Additionally, the experimental data from Refs [77, 78] may have their own uncertainties that are not propagated into the comparison.
- **Why it matters** The central claim of the paper is that Mpipi-Recharged outperforms other models. If the differences between models are within the combined uncertainties of simulations and experiments, the conclusion would be weakened. Rigorous uncertainty quantification is essential for a benchmarking study that aims to guide model selection.
- **Resolution test** Provide error bars or confidence intervals for all simulated quantities (e.g., from block averaging or multiple independent simulations) and for the comparison metrics (e.g., bootstrap or jackknife resampling). Report the statistical significance of differences between models (e.g., via a t-test or ANOVA on the D values). If uncertainties are large, discuss whether the ranking of models is robust.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological completeness and reproducibility
- **Claim pointer** The manuscript states that "none of the six employed models includes explicit solvent, hence, effectively in our DC simulations the protein diluted phase corresponds to a vapour phase" (Section 2.1).
- **Evidence pointer** Section 2.1; Section 4.2; Section 4.3
- **Concern** The use of implicit solvent models without explicit water means that the simulations describe a protein vapour–liquid equilibrium rather than a solution–condensate equilibrium. While this is acknowledged, the implications for the comparison with experimental data (which are measured in aqueous solution) are not fully discussed. The vapour phase may have different intermolecular interactions and packing compared to a dilute solution, potentially affecting the predicted saturation concentrations and critical temperatures. The manuscript does not address whether this approximation introduces systematic biases that could affect the ranking of models.
- **Why it matters** The validity of the benchmark depends on the assumption that the vapour–liquid equilibrium simulated here is a reasonable proxy for the solution–condensate equilibrium measured experimentally. If this approximation introduces model-dependent biases, the conclusions about model accuracy could be compromised.
- **Resolution test** Discuss the potential impact of the implicit solvent approximation on the results. If possible, compare predictions from one or two models with explicit solvent simulations (even for a subset of systems) to assess the magnitude of the effect. Alternatively, cite previous work that validates the use of implicit solvent for phase equilibrium calculations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of conclusions
- **Claim pointer** The manuscript concludes that "Mpipi-Recharged stands out as the most accurate potential" for predicting phase behaviour and viscosity of A1-LCD variants.
- **Evidence pointer** Figures 2–6; Section 3
- **Concern** The benchmark is limited to a single protein system (A1-LCD and its variants). While this system is well-characterized experimentally, it is unclear whether the conclusions generalize to other proteins with different sequence compositions, lengths, or interaction motifs. The authors acknowledge this limitation in the Discussion but do not provide any evidence or argument for why the ranking of models should be expected to hold for other systems.
- **Why it matters** The practical value of the benchmark is to guide model selection for condensate simulations in general. If the performance ranking is system-specific, the recommendations would be of limited use.
- **Resolution test** Add a discussion of the sequence features of A1-LCD that may influence model performance (e.g., aromatic content, charge distribution) and how these features relate to other phase-separating proteins. If possible, include preliminary data for one or two additional proteins to test generalizability, or clearly state the scope of the conclusions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of contact map analysis
- **Claim pointer** The manuscript states that "the Mpipi-Recharged model predicts that cation–π interactions such as R–Y and R–F are stronger contributors than Y–Y, F–F, and Y–F to the stability of A1-LCD condensates" (Section 2.4).
- **Evidence pointer** Figure 8; Section 2.4; Section 4.4
- **Concern** The contact map analysis uses a sequence-dependent cutoff (1.2σij) and weights contact frequencies by interaction energies. However, the manuscript does not clearly explain how the "interaction strength" metric (Eq 13) relates to the actual free energy contribution of each contact pair. The normalization by occurrence frequency (NiNj) may not fully account for the different numbers of each residue type in the sequence, potentially biasing the ranking of important contacts. Additionally, the analysis is performed at a single temperature (0.95Tc) for each system, and it is unclear whether the ranking of contacts is temperature-dependent.
- **Why it matters** The contact map analysis is used to provide mechanistic insight into why certain models perform better. If the metric is not a reliable proxy for free energy contributions, the interpretation could be misleading.
- **Resolution test** Clarify the physical meaning of the "interaction strength" metric and its limitations. Consider performing the analysis at multiple temperatures or comparing with a more rigorous free energy decomposition (e.g., using umbrella sampling or thermodynamic integration) for a subset of systems.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 1
- **Evidence pointer** Figure 1A
- **Issue** The description of the direct coexistence simulation setup in Figure 1A is brief. The figure shows a density profile, but it is not clear how the density is calculated (e.g., along which axis, bin size) or how the coexistence densities are extracted from the profile.
- **Required correction** Add a more detailed description of the density profile calculation in the figure caption or in Section 4.3, including the bin size and the method for determining the plateau densities.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Section 2.2, Figure 5
- **Evidence pointer** Figure 5; Section 4.6
- **Issue** The D metric for comparing saturation concentrations is defined in Section 4.6, but the manuscript does not report the individual D values for each model in the main text. Only the ranking is mentioned.
- **Required correction** Report the D values (and possibly their uncertainties) for each model in the main text or in a table, to allow readers to assess the magnitude of the differences.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of model descriptions
- **Affected element** Table 1
- **Evidence pointer** Table 1; Section 4.1
- **Issue** Table 1 summarizes the potentials used by each model, but the specific parameters (e.g., λi values for hydrophobicity, energy scales for Wang-Frenkel) are not provided in the main text. The reader is referred to the original publications, but this makes it difficult to assess the differences between models without consulting multiple references.
- **Required correction** Consider providing the full parameter sets in the Supporting Information, or at least a more detailed summary of the key parameters that differ between models.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Section 3
- **Evidence pointer** Section 3
- **Issue** The Discussion mentions that the study is limited to A1-LCD but does not discuss other potential limitations, such as the neglect of nucleic acids (which are present in many condensates) or the use of a single force field family (all models are derived from the HPS framework).
- **Required correction** Add a brief discussion of these additional limitations and how they might affect the conclusions.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Referencing
- **Affected element** Section 1, Section 2.1
- **Evidence pointer** Refs [77, 78]
- **Issue** The experimental data from Refs [77, 78] are used extensively for comparison, but the manuscript does not describe how the experimental critical temperatures and saturation concentrations were obtained (e.g., fitting procedures, uncertainties).
- **Required correction** Add a brief description of the experimental methods used in Refs [77, 78] in the Methods section, or at least cite the relevant sections of those papers.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Lack of uncertainty quantification for simulated quantities and comparison metrics.
  - R1-M2: Insufficient discussion of the implicit solvent approximation and its potential impact on the results.
  - R1-M3: Limited evidence for generalizability of conclusions beyond the A1-LCD system.
  - R1-M4: Ambiguity in the interpretation of the contact map "interaction strength" metric.

- **Assessment against Nature-style criteria**
  - **Originality**: The manuscript is original in its systematic comparison of six CG models on both thermodynamic and material properties of condensates. While individual models have been benchmarked before, the comprehensive multi-model comparison on the same system with multiple experimental observables is a novel contribution.
  - **Scientific importance**: The study addresses a critical need in the condensate simulation community: which CG model to choose for a given application. The finding that Mpipi-Recharged performs best for A1-LCD is practically useful, and the link between model performance and interaction ranking provides mechanistic insight.
  - **Interdisciplinary readership**: The topic is of interest to computational biophysicists, experimentalists studying condensates, and researchers in soft matter physics. The manuscript is written in a way that is accessible to these groups, though some familiarity with CG modelling is assumed.
  - **Technical soundness**: The simulation protocols are standard and well-described, and the use of direct coexistence and Green-Kubo methods is appropriate. However, the lack of uncertainty quantification and the limited discussion of the implicit solvent approximation are technical weaknesses that need to be addressed.
  - **Readability for nonspecialists**: The manuscript is generally well-written and the figures are informative. However, the Methods section is dense and may be challenging for readers not familiar with CG simulations. The abstract and introduction are accessible to a broad audience.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important question and provides valuable data, but the lack of uncertainty quantification and the limited discussion of methodological limitations currently prevent full confidence in the conclusions. If the authors can address these concerns, the manuscript would be a strong contribution to the field.