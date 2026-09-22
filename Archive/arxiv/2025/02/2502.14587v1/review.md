## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, end matter, and references.
- **Assessment boundary** Scientific content, methodology, reproducibility of claims, and alignment with stated conclusions. No assessment of formatting or editorial fit.
- **Shared manuscript claim summary** The authors propose a minimal coarse-grained polymer model to show that sequence patterning in intrinsically disordered proteins (IDPs) drives mesoscopic heterogeneity in biomolecular condensates. They identify distinct single-polymer morphologies (expanded, ball-and-chain, globule) and corresponding condensate phases (polymer gas, mono-cluster, poly-cluster, spongey mono-cluster, percolated network), and link these to local coil-to-globule transitions driven by competition between cohesive and spacer regions.
- **Visible evidence base** Simulation results from coarse-grained molecular dynamics, including single-polymer and multi-polymer (Np=100) systems, phase diagrams, crowding density analyses, and scrambling comparisons. Figures referenced: Fig. 1, Fig. 2, Fig. 3, Fig. 4, Fig. S1-S5.
- **Missing materials affecting confidence** No simulation parameter tables, no error bars or statistical replicates, no convergence tests, no sensitivity analysis for interaction strengths, no comparison to experimental data, no code availability statement, and no detailed description of the clustering algorithm parameters.

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting framework linking sequence patterning to mesoscopic condensate organization. The minimal model is well-motivated and the phase diagrams are potentially useful. However, the evidence base is incomplete in several critical areas, particularly regarding statistical robustness, parameter sensitivity, and validation against experimental or atomistic data. The central claim that local coil-to-globule transitions drive condensate heterogeneity is plausible but not fully established from the provided evidence.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, intrinsically disordered proteins, polymer physics, and soft matter. The work offers a conceptual bridge between sequence features and mesoscale organization, which is relevant for understanding condensate function and dysfunction in diseases such as neurodegeneration and cancer.
- **Major strengths** 1. The model is minimal and tractable, allowing systematic exploration of sequence parameter space. 2. The phase diagrams provide a clear organizational framework. 3. The link between single-polymer and multi-polymer behavior is a valuable conceptual contribution. 4. The scrambling control experiments help isolate the role of sequence patterning.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (statistical robustness), R1-M2 (parameter sensitivity), R1-M3 (experimental validation), R1-M4 (thermodynamic limit).
- **Assessment against Nature-style criteria**  
  - Originality: Moderate. The concept of sequence-dependent heterogeneity is not entirely new, but the systematic phase diagram approach is a useful contribution.  
  - Scientific importance: Potentially high if validated, as it could guide experimental studies on condensate organization.  
  - Interdisciplinary readership: Relevant to biophysics, polymer science, and cell biology, but the presentation may be too specialized for a broad audience.  
  - Technical soundness: Currently insufficient due to missing statistical and sensitivity analyses.  
  - Readability for nonspecialists: The main text is accessible, but the end matter is dense and lacks explanatory context.
- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual framework is promising, but the current evidence does not fully establish the central claims.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Statistical robustness  
- **Claim pointer** The authors claim reproducible phase diagrams and distinct morphological classifications based on simulation data.  
- **Evidence pointer** Results section, Fig. 2C, Fig. 3, location not provided  
- **Concern** No error bars, standard deviations, or replicate simulations are reported. It is unclear whether the phase boundaries are robust to stochastic variation in the MD simulations. Single trajectories per parameter set appear to be used, which is insufficient to establish reproducibility.  
- **Why it matters** Without statistical replicates, the phase diagrams and morphological classifications may be artifacts of individual trajectories. This undermines the central claim of predictable sequence-dependent organization.  
- **Resolution test** Provide at least 3-5 independent simulations per parameter set, report mean and standard deviation for all quantitative observables, and demonstrate that phase classifications are stable across replicates.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Parameter sensitivity  
- **Claim pointer** The authors claim that their model captures general principles of sequence-dependent condensate organization.  
- **Evidence pointer** End Matter, model parameters, location not provided  
- **Concern** The model uses fixed interaction strengths (ε_vol, ε_coh, ε_cha) and a single Debye screening length. No sensitivity analysis is provided to show how results depend on these choices. The authors note that ε_cha is not specified in the text, and the relative strengths of cohesive versus charged interactions are not systematically varied.  
- **Why it matters** The conclusions may be specific to the chosen parameter regime rather than general. Without sensitivity analysis, it is unclear whether the observed phase behavior is robust or a consequence of particular parameter values.  
- **Resolution test** Vary interaction strengths over a reasonable range (e.g., 0.5-2x baseline) and show that phase diagrams and key conclusions remain qualitatively unchanged. Report the value of ε_cha used.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Experimental validation  
- **Claim pointer** The authors state their work provides a conceptual framework to understand sequence properties determining mesoscopic organization in biomolecular condensates.  
- **Evidence pointer** Discussion section, location not provided  
- **Concern** No comparison to experimental data or atomistic simulations is provided. The model predictions are not tested against known IDP sequences or experimentally characterized condensates.  
- **Why it matters** The biological relevance of the findings is asserted but not demonstrated. Without validation, the framework remains a theoretical exercise with unclear applicability to real systems.  
- **Resolution test** Apply the model to at least one or two experimentally characterized IDP sequences (e.g., Ddx4, FUS) and compare predicted morphologies with available experimental observations. Alternatively, provide a clear pathway for experimental testing.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Thermodynamic limit  
- **Claim pointer** The authors claim that the observed condensate morphologies represent equilibrium or near-equilibrium phases.  
- **Evidence pointer** Results section, Fig. 2, location not provided  
- **Concern** The simulations use Np=100 polymers in a box of 80 nm, which is a finite-size system. The authors acknowledge uncertainty about the thermodynamic limit for some classifications but do not address this systematically. Finite-size effects could significantly alter phase boundaries and the existence of certain phases.  
- **Why it matters** The phase diagram is presented as a general result, but finite-size effects may limit its validity. The authors' own admission of uncertainty in some regions underscores this concern.  
- **Resolution test** Perform simulations with varying system sizes (e.g., Np=50, 200, 500) and show that phase classifications converge. Alternatively, provide a quantitative analysis of finite-size effects.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Model description  
- **Evidence pointer** End Matter, location not provided  
- **Issue** The value of ε_cha is not explicitly stated, and the conversion factor C is introduced but its numerical value is not given.  
- **Required correction** Provide explicit values for all interaction parameters and conversion factors.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Simulation protocol  
- **Evidence pointer** End Matter, location not provided  
- **Issue** The initialization procedure (dragging polymers to the origin) is described but not quantified. The relaxation time and production time are given, but no equilibration check is reported.  
- **Required correction** Describe the initialization force and duration, and provide evidence of equilibration (e.g., stable energy or radius of gyration over time).

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Presentation  
- **Affected element** Phase diagram classification  
- **Evidence pointer** Results section, Fig. 2C, location not provided  
- **Issue** The classification criteria for the four phases are described as "several conditionals" but the exact inequalities are relegated to SI2. This makes it difficult to assess the robustness of the classification.  
- **Required correction** Include the key classification criteria in the main text or provide a more detailed summary in the figure caption.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Terminology  
- **Affected element** "Mesoscopic heterogeneity"  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The term "mesoscopic" is used but not precisely defined in the context of the model. The length scales of the observed clusters are not quantified.  
- **Required correction** Define the length scale range implied by "mesoscopic" and report typical cluster sizes in the simulations.

## Risk / unsupported claims
- The claim that local coil-to-globule transitions in single polymers directly determine condensate heterogeneity is supported only by correlation, not causation. The mechanism is plausible but not definitively established.
- The assertion that the framework has implications for surface tension, viscosity, aging, thermodynamics, and chemical reactions in condensates is speculative and not supported by any direct evidence in this manuscript.
- The claim that the model explains "nano-scale organisational heterogeneities" in real condensates is not validated against experimental observations.
- The phase diagram for charged-spacer polymers includes a region classified as "polymer gas" for large Lc, which the authors admit is nearly indistinguishable from the gas phase. This classification is therefore uncertain.