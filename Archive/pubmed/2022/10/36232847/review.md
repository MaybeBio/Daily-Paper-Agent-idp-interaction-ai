## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and conclusions
- **Assessment boundary** Scientific validity of the computational approach, accuracy of binding site predictions relative to experimental data, and interpretation of conformational ensemble analyses
- **Shared manuscript claim summary** The authors report atomistic replica exchange molecular dynamics (REMD) simulations of full-length alpha-synuclein with three ligands (fasudil, phthalocyanine tetrasulfonate, and spermine) to predict binding sites and infer effects on amyloid conversion. They claim accurate binding site prediction for fasudil and spermine, partial accuracy for PcTS, and propose mechanisms of anti- or pro-amyloid action based on conformational ensemble changes.
- **Visible evidence base** Full text with figures referenced (Figures 1-5), methods section, and discussion. No supplementary materials or raw simulation data provided.
- **Missing materials affecting confidence** Simulation parameter files, force field validation details, convergence criteria, error estimates for binding probabilities, raw trajectory analyses, and comparison of simulation timescales with experimental binding kinetics

## Reviewer
- **Overall assessment** The manuscript presents a technically ambitious computational study addressing a relevant problem in Parkinson's disease research. The use of full-length intrinsically disordered alpha-synuclein with explicit ligands in REMD simulations is commendable. However, several methodological concerns regarding simulation convergence, statistical robustness of binding site predictions, and the interpretation of conformational changes as mechanistic evidence require careful consideration. The claims of accurate binding site prediction are partially supported, but the mechanistic conclusions about amyloid conversion effects are not fully established from the provided evidence.
- **Who would be interested in the results, and why** Researchers in computational biophysics studying intrinsically disordered proteins, medicinal chemists interested in structure-based drug design for Parkinson's disease, and experimentalists studying alpha-synuclein aggregation mechanisms would find this work relevant. The methodological approach could inform future computational screening strategies for disordered protein targets.
- **Major strengths** 1) Use of full-length protein rather than fragments, addressing a known limitation in the field. 2) Application of REMD to capture conformational diversity of an intrinsically disordered protein. 3) Selection of three ligands with distinct experimental binding data allows benchmarking. 4) Analysis of binding dynamics beyond static poses provides insight into the dynamic nature of ligand-protein interactions.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (simulation convergence), R1-M2 (statistical robustness of binding site predictions), R1-M3 (mechanistic interpretation of conformational changes)
- **Assessment against Nature-style criteria** **Originality** Moderate. The application of REMD to full-length alpha-synuclein with ligands is novel, but the overall approach of ensemble-based binding prediction is not unprecedented. **Scientific importance** Moderate. The findings could inform drug development for synucleinopathies, but the mechanistic conclusions require stronger validation. **Interdisciplinary readership** Limited. The work is primarily of interest to computational biophysicists and specialists in protein aggregation. **Technical soundness** Adequate but with notable gaps in convergence assessment and statistical validation. **Readability for nonspecialists** Acceptable. The manuscript is generally clear, though some technical details could be better explained for a broader audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The core approach has merit, but the current evidence does not fully establish the mechanistic claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that REMD simulations provide a "realistic conformational ensemble" of alpha-synuclein with ligands, enabling accurate binding site prediction and mechanistic insight.
- **Evidence pointer** Section 4.1, Methods; Section 2.1, Results
- **Concern** The manuscript does not provide evidence of simulation convergence. REMD simulations of intrinsically disordered proteins are notoriously difficult to converge, especially for a 140-residue protein with only 84 replicas over 100 ns. The authors do not report replica exchange acceptance rates beyond a single probability value (0.22-0.28), nor do they show convergence of structural observables over time. Without convergence assessment, the conformational ensembles may not be representative, undermining all subsequent analyses.
- **Why it matters** Non-converged simulations can produce biased conformational ensembles, leading to incorrect binding site predictions and erroneous mechanistic conclusions. The validity of the entire approach depends on the quality of the sampling.
- **Resolution test** Provide replica exchange acceptance rates per temperature pair, show time evolution of key observables (Rg, end-to-end distance, secondary structure content) to demonstrate equilibration, and compare ensembles from independent simulation runs or extended simulation times.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical robustness
- **Claim pointer** The authors claim "accurate prediction of the binding sites" for fasudil and spermine, and "moderate accuracy" for PcTS, based on comparison with experimental data.
- **Evidence pointer** Section 2.1, Results; Figure 1
- **Concern** The binding site predictions are based on contact frequency analysis, but the manuscript does not report statistical uncertainties or significance testing for these predictions. The authors state that some residues show "relatively high number of total binding frames" but do not provide error bars, confidence intervals, or statistical comparisons between candidate binding sites. The filtering threshold of 3 ns for "stable" binding appears arbitrary and is not justified. Additionally, the comparison with experimental data is qualitative, with no quantitative metric of agreement.
- **Why it matters** Without statistical validation, the binding site predictions could be artifacts of limited sampling or arbitrary analysis thresholds. The claim of "accurate prediction" requires quantitative support.
- **Resolution test** Provide bootstrap or block-averaging error estimates for binding probabilities, perform statistical tests to distinguish preferred binding residues from background, and quantify agreement with experimental data using a defined metric (e.g., fraction of experimentally identified residues recovered).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation and mechanistic claims
- **Claim pointer** The authors claim that PcTS binding "significantly shifts the peak on the distribution to a more expanded conformation" and that spermine binding "enhanced the formation of beta-structured elements in the NAC domain," leading to conclusions about anti- and pro-amyloid mechanisms.
- **Evidence pointer** Section 2.2, Results; Figures 3 and 4
- **Concern** The mechanistic conclusions are based on differences in conformational ensembles between ligand-bound and free states, but the manuscript does not establish that these differences are statistically significant or biologically relevant. The reported differences in beta-hairpin probabilities (up to 11.5%) and contact map changes (up to 7%) lack error estimates. Furthermore, the connection between enhanced beta-hairpin formation in the NAC region and pro-amyloid activity is inferred but not directly demonstrated. The authors acknowledge that "the type of effect cannot be predicted from this model" for PcTS, yet still propose a mechanism of action.
- **Why it matters** The central claim of the manuscript is that the simulations provide insight into the mechanism of ligand effects on amyloid conversion. If the conformational differences are not statistically robust or mechanistically validated, this claim is not supported.
- **Resolution test** Provide statistical significance testing for all reported ensemble differences, include error bars on all probability profiles, and either strengthen the mechanistic link between observed conformational changes and amyloid conversion or temper the conclusions accordingly.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Technical clarity
- **Affected element** Methods section
- **Evidence pointer** Section 4.1, Methods
- **Issue** The manuscript states that "84 conformations were randomly selected" from the Protein Ensemble Database but does not specify the selection criteria or whether the selected conformations are representative of the full ensemble. Additionally, the protonation state assignment is described only as "corresponding to a physiological pH value" without specifying the method used.
- **Required correction** Provide details on the selection criteria for initial conformations and the method for assigning protonation states (e.g., PROPKA, PDB2PQR).

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 1
- **Evidence pointer** Figure 1
- **Issue** The binding probability profiles in Figure 1 are presented as raw values without normalization or error estimates. The comparison with experimental data at the bottom of the figure is qualitative and lacks a clear legend explaining how the experimental binding regions were defined.
- **Required correction** Add error bars or confidence intervals to the binding probability profiles, and provide a clear description of how experimental binding regions were determined and mapped to the figure.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion section
- **Evidence pointer** Section 3, Discussion
- **Issue** The discussion of the "dynamic shuttling" behavior of fasudil is interesting but is not quantitatively characterized. The authors mention that the ligand "moves around this part of the binding site" but do not provide metrics such as residence times, transition rates, or free energy barriers.
- **Required correction** Provide quantitative characterization of ligand dynamics (e.g., residence time distributions, transition rates between binding poses) to support the qualitative description.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical completeness
- **Affected element** Methods section
- **Evidence pointer** Section 4.1, Methods
- **Issue** The manuscript does not report the total simulation time per replica, the total aggregate simulation time, or the computational cost. This information is important for assessing the feasibility of the approach for other systems.
- **Required correction** Report the total simulation time per replica and the aggregate simulation time across all replicas.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction and Discussion
- **Evidence pointer** Sections 1 and 3
- **Issue** The manuscript does not discuss recent advances in enhanced sampling methods for intrinsically disordered proteins, such as metadynamics or accelerated molecular dynamics, which could provide context for the choice of REMD.
- **Required correction** Add a brief discussion of alternative enhanced sampling approaches and justify the choice of REMD in this context.

## Risk / unsupported claims
- The claim that the approach enables "accurate prediction of the binding sites" is not fully supported for PcTS, as the authors acknowledge only partial agreement with experimental data.
- The mechanistic conclusion that PcTS inhibits amyloid conversion through chain expansion is speculative, as the authors state that "the type of effect cannot be predicted from this model."
- The claim that spermine's pro-amyloid action arises from enhanced beta-hairpin formation in the NAC region is inferred from ensemble differences without direct experimental validation.
- The statement that the binding of ligands "did not narrow the distribution" of conformations, supporting the "truly disordered" nature of alpha-synuclein, is based on qualitative visual inspection of free energy surfaces without quantitative comparison.
- The extrapolation of the approach to other intrinsically disordered proteins and ligands is presented as promising but is not demonstrated with additional test cases.