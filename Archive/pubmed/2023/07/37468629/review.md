## Review setup
- **Input scope** Full manuscript text, including abstract, main text, methods, and supplementary material descriptions
- **Assessment boundary** Scientific content, technical soundness, and claims as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors study the molecular dynamics of the ProTα-H1 biomolecular condensate, combining single-molecule FRET experiments with all-atom molecular dynamics simulations. They report that despite a bulk viscosity ~300 times that of water, intrachain dynamics of the disordered proteins remain rapid (sub-microsecond reconfiguration times), explained by short-lived interchain contacts that exchange on pico- to nanosecond timescales.
- **Visible evidence base** Main text figures (Figs. 1–4), Extended Data figures (1–10), Table 1, methods section, simulation details
- **Missing materials affecting confidence** Raw data files, full figure panels with error bars and statistical details, simulation trajectory analysis scripts, exact fitting procedures for FRET data, and complete methodological parameters for some experiments

## Reviewer
- **Overall assessment** This manuscript presents a compelling and technically sophisticated study of molecular dynamics within a biomolecular condensate. The combination of single-molecule FRET measurements inside individual droplets with large-scale all-atom simulations is innovative and provides a rare direct view of molecular behavior in phase-separated systems. The central finding, that rapid intrachain dynamics persist despite high macroscopic viscosity, is well-supported by the convergence of experimental and computational approaches. The work addresses a fundamental question in the condensate field and the methodology sets a new standard for studying molecular-scale behavior in these systems. However, several technical aspects require clarification and additional analysis to fully establish the quantitative claims.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates and phase separation, particularly those interested in the molecular-scale dynamics and internal organization of these structures. The work will also appeal to the single-molecule biophysics community, as it demonstrates advanced FRET methodologies in complex environments. Computational biophysicists working on IDP simulations and force field validation will find the large-scale simulation results valuable. The findings have broader implications for understanding how biochemical reactions proceed within condensates, which is relevant to cell biology and biotechnology.

- **Major strengths** The study combines cutting-edge experimental techniques with state-of-the-art simulations to address a question that has been difficult to tackle experimentally. The single-molecule FRET measurements inside individual droplets represent a significant technical achievement. The convergence of experimental and computational results strengthens the conclusions. The authors provide a clear physical picture, supported by multiple lines of evidence, for why molecular dynamics remain rapid despite high viscosity. The work is clearly written and the logic is easy to follow.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the bulk viscosity of the dense phase is 0.30 ± 0.06 Pa s, approximately 300 times that of water, based on bead tracking experiments.
- **Evidence pointer** Fig. 1d, Methods section "Nanorheology"
- **Concern** The viscosity measurement relies on tracking 100 nm and 500 nm beads in the dense phase. The manuscript does not provide sufficient details on how many beads were tracked, how many droplets were measured, and whether the beads might perturb the local condensate structure. Additionally, the Stokes-Einstein relation assumes a homogeneous continuum, which may not be valid for a condensate with a correlation length of ~2.4–4.3 nm when using beads of 100 nm diameter. The authors do mention the size-dependent viscosity effect, but the specific correction for the 100 nm beads is not clearly described.
- **Why it matters** The bulk viscosity value is a central quantitative claim that anchors the entire narrative of the paper. If the viscosity is overestimated, the contrast between macroscopic viscosity and molecular dynamics would be less dramatic, weakening the central message.
- **Resolution test** Provide detailed statistics on bead tracking (number of beads, droplets, replicates), demonstrate that bead motion is not affected by interactions with the condensate network, and show that the viscosity measurement is robust to the choice of bead size and analysis method.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors report reconfiguration times of 380 ± 39 ns for ProTα in the dense phase, measured by nsFCS, and compare this to 126 ± 43 ns in the dimer and 14 ± 2 ns for free ProTα.
- **Evidence pointer** Fig. 2h, Methods section "Nanosecond fluorescence correlation spectroscopy (nsFCS)"
- **Concern** The nsFCS measurements in the dense phase require scanning the sample to compensate for photobleaching. The manuscript does not fully describe how the scanning affects the correlation analysis, particularly at short lag times where the conformational dynamics are expected to appear. The conversion from the correlation time τcd to the reconfiguration time τr relies on assumptions about the diffusive process in a potential of mean force, and the manuscript does not provide a detailed validation of this conversion for the dense phase case where the environment is complex.
- **Why it matters** The reconfiguration time is the key experimental observable supporting the central claim of rapid molecular dynamics. If the measurement or analysis is flawed, the conclusion would be compromised.
- **Resolution test** Provide a more detailed description of the scanning procedure and its effect on the correlation functions, show control experiments demonstrating the reliability of the τcd to τr conversion in the dense phase, and provide a more thorough error analysis.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the all-atom simulations reproduce the experimental observations, including the reconfiguration times and transfer efficiencies.
- **Evidence pointer** Table 1, Fig. 3b, Methods section "Molecular dynamics simulations"
- **Concern** The simulation of the dense phase was performed for 6.02 μs, with the first 1.5 μs treated as equilibration. Given the large system size (~4 million atoms) and the need to sample conformational dynamics of 96 ProTα chains, it is unclear whether 4.5 μs of production is sufficient to obtain converged statistics for the reconfiguration times. The manuscript reports a wide distribution of reconfiguration times and omits chains with low variance, which could introduce bias. The force field (Amber99SBws with TIP4P/2005s) has been validated for single IDPs, but its performance for concentrated multi-chain systems is less established.
- **Why it matters** The simulation results are used to provide mechanistic insight into the experimental observations. If the simulations are not fully converged or the force field is not appropriate for this system, the mechanistic conclusions could be unreliable.
- **Resolution test** Provide convergence analysis (e.g., block averaging, splitting the trajectory into segments), demonstrate that the results are robust to the choice of analysis parameters, and discuss the limitations of the force field for concentrated IDP systems.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors suggest that their findings may be generalizable to other charge-driven condensates and that the approach could be transferred to synthetic polymers.
- **Evidence pointer** Discussion section
- **Concern** The manuscript studies a single model system (ProTα-H1). While the authors discuss the potential generality of their findings, no experimental or computational evidence is provided to support this generalization. The claim that "charge-driven condensates... can comprise surprisingly rapid dynamics" is based on one example.
- **Why it matters** The broader significance of the work depends on whether the findings are specific to this system or reflect a general principle of condensate biology.
- **Resolution test** Add a more careful discussion of the limitations of generalizing from a single system, or provide preliminary data on another charge-driven condensate system.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the dense phase is "1000 times more concentrated than the dilute phase" but does not specify the concentration units or the absolute concentrations. This makes it difficult for readers to contextualize the result.
- **Required correction** Provide the absolute concentrations in the abstract or refer to a figure/table where these are given.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** FRET analysis
- **Evidence pointer** Methods section "Single-molecule fluorescence spectroscopy"
- **Issue** The manuscript mentions that the Förster radius R0 was corrected for the refractive index in the droplets, but the exact value used and the method for determining the refractive index are not described in detail.
- **Required correction** Provide the value of R0 used for the dense phase analysis and describe how the refractive index was estimated.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Simulation analysis
- **Evidence pointer** Methods section "Analysis of MD simulations"
- **Issue** The manuscript states that chains with variance of transfer efficiency below 0.05 were omitted from the analysis, but does not provide a justification for this threshold or a sensitivity analysis.
- **Required correction** Justify the threshold and show that the results are robust to reasonable variations in this cutoff.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Fig. 1e
- **Evidence pointer** Fig. 1e
- **Issue** The figure shows the size-dependent viscosity, but the transition between the two regimes is not clearly marked or explained in the figure legend.
- **Required correction** Add a clear annotation or description of the transition region and its significance.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** FRAP analysis
- **Evidence pointer** Methods section "Fluorescence recovery after photobleaching (FRAP)"
- **Issue** The FRAP recovery curves were fit with a single-exponential function, but the manuscript does not discuss whether a more complex model might be more appropriate given the complex environment of the condensate.
- **Required correction** Discuss the choice of fitting model and its potential limitations.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Data availability
- **Evidence pointer** Data availability section
- **Issue** The simulation trajectories are deposited, but the analysis scripts and the experimental raw data (e.g., FRET histograms, FCS curves) are not explicitly mentioned as being available.
- **Required correction** Clarify the availability of all raw data and analysis scripts.

## Risk / unsupported claims
- The claim that the findings are generalizable to other charge-driven condensates is not supported by data from other systems.
- The claim that the approach could be transferred to synthetic polymers is speculative and not demonstrated.
- The quantitative comparison between simulation and experiment for reconfiguration times relies on assumptions in the conversion from FRET observables to physical timescales that are not fully validated for the dense phase.
- The statement that "local biomolecular rearrangements required for efficient reactions at the molecular scale can remain rapid" is a reasonable inference but is not directly tested in this work.
- The claim that the force field is suitable for describing "complex multimolecular interactions in condensates" is based on agreement with a limited set of observables and may not hold for all properties.