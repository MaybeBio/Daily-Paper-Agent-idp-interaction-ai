## Review setup
- **Input scope** Full manuscript text (abstract, main text, methods, references list without full citations)
- **Assessment boundary** Scientific soundness, methodological rigor, validity of claims, and significance of the reported results, based solely on the provided manuscript text
- **Shared manuscript claim summary** The authors present HyRes, a hybrid-resolution (atomistic backbone, intermediate-resolution sidechains) physics-based protein force field, and claim it accurately reproduces experimental observables (chain dimensions, transient contacts, secondary structure) for ~100 IDPs, transfers to complex environments (dilute, condensed, fibril coats), and scales to ~30,000 proteome-wide sequences, providing a public database.
- **Visible evidence base** Main text figures (Fig 1a-g, 2a-c, 3a-g, 4a-g, 5a-f), Extended Data Figures 1-10, Supplementary Tables S1-S12, Supplementary Figures S1-S2, Methods section
- **Missing materials affecting confidence** Full reference list, complete figure legends, actual figure images, Supplementary Tables content, Extended Data Figure content, detailed parameter files, and convergence metrics for individual simulations

## Reviewer

- **Overall assessment** This manuscript describes a significant technical advance in coarse-grained simulation of intrinsically disordered proteins. The hybrid-resolution approach is well-motivated, and the validation strategy is comprehensive in scope. The demonstrated transferability to condensed phases and fibril environments is impressive and addresses a critical gap in the field. However, several technical concerns regarding parameterization details, validation metrics, and the interpretation of proteome-scale results need to be addressed before the claims are fully established. The computational efficiency gains are substantial and well-documented, but the accuracy claims relative to all-atom force fields require more careful statistical treatment.

- **Who would be interested in the results, and why** Researchers in the IDP simulation community, developers of coarse-grained and hybrid-resolution force fields, computational biophysicists studying phase separation and amyloid fibrils, and the broader structural biology community interested in proteome-scale conformational ensembles. The public database will be of interest to machine learning practitioners developing structure prediction tools for disordered proteins.

- **Major strengths** 
  1. The hybrid-resolution design (atomistic backbone, CG sidechains) is a well-reasoned compromise that retains backbone-mediated interactions while achieving substantial computational savings.
  2. The validation set is extensive (~100 IDPs) and covers diverse sequence properties and experimental observables.
  3. The demonstration of transferability across dilute, condensed, and fibril-coat environments is a major strength that distinguishes this work from typical force field development papers.
  4. The computational efficiency gains (orders of magnitude) are clearly documented with concrete examples.
  5. The proteome-scale application and public database represent a valuable community resource.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Parameterization methodology
- **Claim pointer** "The HyRes force field is refined using radius of gyration (Rg) measurements on 20 variants of the human hnRNPA1 low-complexity domain (A1-LCD) and NMR-derived residue helicity of 15 IDPs."
- **Evidence pointer** Methods section, "HyRes optimization through hierarchical rebalancing of interactions", Extended Data Fig. 1a-d
- **Concern** The parameterization strategy is described as a hierarchical rebalancing of electrostatic and vdW interactions, but the manuscript does not provide sufficient detail on the optimization procedure. Specifically, the dielectric constant was set to εr = 60.0 based on only 30 random and one alternating EK peptide. The manuscript does not describe how the vdW parameters for each amino acid were systematically optimized against the 20 A1-LCD variants, what objective function was used, whether the optimization was performed iteratively with cross-validation to avoid overfitting, or how the balance between electrostatic and vdW contributions was maintained. The statement "Interaction parameters were then iteratively fine-tuned until the best agreement was reached" is vague and does not constitute a reproducible parameterization protocol.
- **Why it matters** Force field parameterization is the foundation of the entire study. Without a clear description of the optimization procedure, the reproducibility of the method is compromised, and the risk of overfitting to the training set cannot be assessed. The claim that HyRes "matches or outperforms" all-atom force fields depends critically on the rigor of the parameterization and the independence of the validation set.
- **Resolution test** Provide a detailed description of the optimization algorithm, including the objective function, the parameter space explored, the number of optimization iterations, and the convergence criteria. Demonstrate that the validation set of ~100 IDPs is independent of the parameterization set and show that the model does not overfit by, for example, performing leave-one-out cross-validation on the training set.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor of validation
- **Claim pointer** "Across this set, the HyRes model achieves a high correlation of r = 0.97 with an RMSD of 3.2 Å" and "HyRes demonstrates performance comparable to these three state-of-the-art all-atom force fields"
- **Evidence pointer** Fig. 1c, Fig. 3f, Supplementary Tables S3, S11
- **Concern** The manuscript reports correlation coefficients and RMSD values for the comparison between simulated and experimental observables, but does not provide confidence intervals, statistical significance tests, or a systematic comparison of error distributions. For the comparison with all-atom force fields (Fig. 3f), it is unclear how many IDPs were used for the benchmark, whether the same IDPs were used for all force fields, and whether the differences between HyRes and the all-atom force fields are statistically significant. The claim of "comparable" performance requires a statistical test of equivalence or non-inferiority.
- **Why it matters** The central claim of the paper is that HyRes achieves accuracy comparable to all-atom force fields at a fraction of the computational cost. This claim requires rigorous statistical support. Without confidence intervals or significance tests, the reader cannot assess whether the reported correlations and RMSD values are meaningfully different between methods or within the noise of the comparison.
- **Resolution test** Provide confidence intervals for all reported correlation coefficients and RMSD values. Perform a paired statistical comparison (e.g., paired t-test or Wilcoxon signed-rank test) between HyRes and each all-atom force field on the same set of IDPs. Report the number of IDPs used in each comparison and discuss whether the differences are practically significant.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Convergence and sampling adequacy
- **Claim pointer** "at least 2 µs of production simulation was performed to calculate the properties of each IDP" and "the 4-µs HyRes simulation (162,256 beads) required only ~5 days on a single NVIDIA L40s GPU"
- **Evidence pointer** Methods section, "HyRes simulation and analysis of monomeric IDPs", Extended Data Fig. 8g-h
- **Concern** The manuscript does not provide a systematic analysis of convergence for the IDP simulations. While the authors state that "good convergence was achieved" for the tau fibril system, no convergence metrics (e.g., block averaging, autocorrelation times, or split-half comparisons) are shown for the monomeric IDP simulations. For the H1-ProTα condensate, the manuscript states that the 4-µs simulation was "fully converged" but does not show the convergence analysis. Given that IDPs can have slow relaxation times, especially for large chains (up to 477 residues), 2 µs may not be sufficient for all systems.
- **Why it matters** If the simulations are not converged, the reported ensemble averages (Rg, Ree, helicity, PRE profiles) may not be representative of the equilibrium ensemble, and the comparison with experimental data could be misleading. The claim of "fully converged" for the condensate simulation is particularly important because the system is large and complex.
- **Resolution test** Provide convergence analysis for representative IDPs of different lengths, including time series of Rg and helicity, autocorrelation functions, and block-averaged estimates with standard errors. For the condensate and fibril systems, show that key observables (e.g., inter-molecular contacts, chain dimensions) are stable over the simulation time and that independent replicates (if performed) give consistent results.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of PRE validation
- **Claim pointer** "HyRes successfully captures virtually all major features of the experimental PRE profiles for all 9 IDPs" and "average correlation of r ∼ 0.72 and average RMSD of 0.19"
- **Evidence pointer** Fig. 2a-b, Extended Data Fig. 3, Supplementary Table S5
- **Concern** The PRE validation is presented as a key demonstration of HyRes's ability to capture transient long-range contacts. However, the manuscript does not discuss the sensitivity of PRE profiles to the choice of tumbling time (τc), which was optimized in the range of 1-7 ns. The optimization of τc for each IDP could artificially improve the agreement with experiment. Additionally, the average correlation of r ~ 0.72, while positive, leaves substantial unexplained variance, and the manuscript does not discuss whether the discrepancies are systematic (e.g., overestimation of compact states) or random.
- **Why it matters** PRE is a powerful but indirect probe of long-range contacts. If the τc optimization is not properly accounted for, the reported agreement could be overly optimistic. Understanding the nature of the discrepancies is important for assessing the limitations of the model and for guiding future improvements.
- **Resolution test** Report the optimized τc values for each IDP and discuss whether they are physically reasonable. Perform a sensitivity analysis showing how the correlation and RMSD change with τc. Discuss the pattern of residuals (e.g., are discrepancies concentrated in specific sequence regions or contact distances?) and whether they suggest specific model limitations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Proteome-scale database validation
- **Claim pointer** "we leverage HyRes' scalability to generate disordered ensembles for ~30,000 IDPs from the human proteome and DisProt, revealing strong correlation between residual structures and cellular function and localization"
- **Evidence pointer** Fig. 5a-f, Methods section, "HyRes-IDRome database"
- **Concern** The proteome-scale application is a major claim of the paper, but the validation of this large-scale dataset is limited. The authors show correlations between helical content and functional/localization categories, but do not provide statistical significance testing, effect sizes, or comparison with appropriate null models. The biological interpretation of these correlations is also underdeveloped. For example, the finding that actin- and RNA-binding IDPs have longer helices is interesting but the mechanistic explanation is not provided.
- **Why it matters** The proteome-scale database is positioned as a major community resource. If the biological correlations are not rigorously established, the value of the database for hypothesis generation is diminished. Additionally, the claim of "strong correlation" requires statistical support.
- **Resolution test** Provide statistical tests (e.g., ANOVA or Kruskal-Wallis with post-hoc comparisons) for the differences in helical content across functional and localization categories. Report effect sizes and discuss the biological significance of the findings. Consider comparing the observed correlations with those expected from a null model (e.g., randomly permuted labels).

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure presentation
- **Affected element** Fig. 1b-d, Fig. 2a-c, Fig. 3a-g
- **Evidence pointer** Main text figure references
- **Issue** The manuscript text refers to specific panels (e.g., Fig. 1b, Fig. 3d) but does not provide detailed figure legends in the provided text. Without seeing the actual figures, it is difficult to assess the quality of the data presentation.
- **Required correction** Ensure that figure legends are comprehensive and self-contained, clearly describing the data shown, the statistical treatment, and the number of replicates or systems.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Methods section, "HyRes simulation and analysis of monomeric IDPs"
- **Evidence pointer** Methods section
- **Issue** The methods section does not specify the temperature and pressure coupling schemes, the barostat (if any), or the treatment of long-range interactions beyond the cutoff scheme. The Langevin dynamics parameters are given, but the integration scheme and the use of any constraints beyond SHAKE are not described.
- **Required correction** Provide complete simulation parameters, including temperature, pressure (if applicable), integration time step, and any additional constraints or settings.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Comparison with existing models
- **Affected element** Fig. 1e, Discussion
- **Evidence pointer** Fig. 1e, Discussion section
- **Issue** The comparison with "the best machine-learning predictors and data-driven CG models" is mentioned but not shown in the provided text. The manuscript would benefit from a direct, quantitative comparison with at least one or two representative models (e.g., CALVADOS, Mpipi) on the same validation set.
- **Required correction** Include a direct comparison figure or table showing the performance of HyRes versus at least one or two existing models on the same IDP validation set.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Database accessibility
- **Affected element** Methods section, "HyRes-IDRome database"
- **Evidence pointer** Methods section
- **Issue** The database is hosted on Hugging Face, which is appropriate, but the manuscript does not specify the file formats for the trajectory files (e.g., DCD) and whether analysis scripts are provided to read and analyze the data.
- **Required correction** Provide a clear description of the file formats, the software required to read them, and any analysis scripts or notebooks that users can use to access and analyze the data.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract, "intermediate-resolution sidechains"
- **Evidence pointer** Abstract
- **Issue** The term "intermediate-resolution" is used to describe the sidechain representation, but the manuscript does not clearly define what this means in terms of the number of beads per sidechain or the level of detail.
- **Required correction** Define the sidechain resolution explicitly (e.g., one bead per sidechain, two beads for larger sidechains) in the methods section.

## Risk / unsupported claims
- The claim that HyRes "matches or outperforms state-of-the-art all-atom force fields" is not fully supported by the provided data, as the statistical comparison is not shown and the number of IDPs used for the comparison is not stated.
- The claim of "strong correlation between residual structures and cellular function and localization" in the proteome-scale analysis is not supported by statistical tests or effect sizes.
- The statement that the H1-ProTα condensate simulation is "fully converged" is not supported by convergence analysis shown in the provided text.
- The claim that HyRes captures "virtually all major features" of PRE profiles is subjective and not supported by a quantitative analysis of the residuals.
- The manuscript states that the HyRes force field is "refined" and "rebalanced" but does not provide the final parameter set or a description of the parameter files, making the work not fully reproducible.
- The claim of "exceptional transferability" is based on three environments (dilute, condensed, fibril coat), which is a reasonable but limited set; the manuscript should acknowledge that further testing in other environments (e.g., in the presence of osmolytes, post-translational modifications, or nucleic acids) is needed.