## Review setup
- **Input scope** Full manuscript text including abstract, main text, methods, and figure legends
- **Assessment boundary** Scientific content, technical soundness, and claims as presented in the provided manuscript
- **Shared manuscript claim summary** The authors report that linker histone H1 preferentially binds and phase separates with single-stranded nucleic acids, forming gel-like condensates distinct from the more liquid-like droplets formed with dsDNA or nucleosomes. They propose that multivalent transient interactions between H1 disordered tails and ssDNA drive enhanced phase separation, and provide cell-based evidence suggesting H1:ssDNA coacervation occurs at stalled replication forks.
- **Visible evidence base** Single-molecule fluorescence and force microscopy, optical tweezer-based droplet fusion assays, coarse-grained molecular dynamics simulations, live-cell confocal imaging, turbidity assays, FRAP experiments
- **Missing materials affecting confidence** Statistical details and exact p-values in figure legends (referenced but not shown), uncropped gel image for Extended Data Fig. 1c (referenced but not shown), full source data files, Supplementary Videos, detailed simulation parameter tables, exact sample sizes for some experiments

## Reviewer

- **Overall assessment** This manuscript presents a comprehensive and technically sophisticated investigation of H1 interactions with nucleic acid substrates, revealing a novel preference for single-stranded nucleic acids that leads to distinct material properties of the resulting condensates. The combination of single-molecule assays, controlled droplet fusion measurements, and molecular dynamics simulations provides a compelling multi-scale approach. The work addresses an important gap in understanding H1's diverse cellular functions beyond chromatin compaction. However, several technical concerns regarding the interpretation of the droplet fusion kinetics, the physiological relevance of the in vitro conditions, and the strength of the in vivo evidence require clarification before the central claims can be fully established.

- **Who would be interested in the results, and why** Chromatin biologists studying linker histone functions, researchers in the phase separation field interested in nucleic acid-mediated condensate formation, DNA damage response investigators, and biophysicists developing quantitative assays for biomolecular condensates. The work provides new insights into H1's potential roles at replication forks and establishes a framework for studying differential nucleic acid interactions.

- **Major strengths** 
  1. The single-molecule approach directly visualizes H1 behavior on DNA under tension, revealing a striking preference for ssDNA that was previously unappreciated
  2. The droplet fusion assay with force measurement provides quantitative material property characterization, going beyond standard qualitative observations
  3. The combination of experiments and simulations provides mechanistic insight into why ssDNA promotes enhanced phase separation
  4. The in vivo experiments connect the biochemical observations to potential cellular functions

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of droplet fusion interpretation
- **Claim pointer** The authors claim that H1:ssDNA droplets are more viscous and gel-like based on slower fusion times compared to H1:dsDNA droplets
- **Evidence pointer** Figure 3, Extended Data Fig. 5
- **Concern** The interpretation of fusion time as a direct proxy for viscosity assumes that the fusion process is limited by viscous flow rather than by molecular rearrangements at the droplet interface or by differences in droplet size, surface tension, or interfacial energy. The authors report fusion times of 0.96 ± 0.37 s for ssDNA30 versus 0.0046 ± 0.0013 s for dsDNA30, a ~200-fold difference. However, the droplets may have different sizes, and the force measurement during fusion could be influenced by the optical trap stiffness and the droplet's refractive index, which may differ between ssDNA and dsDNA condensates. The authors do not report droplet size distributions or control for potential differences in refractive index.
- **Why it matters** The central claim that ssDNA promotes gel-like condensates with distinct material properties rests on this fusion assay. If the observed differences are due to experimental artifacts rather than intrinsic material properties, the interpretation of the entire study would be affected.
- **Resolution test** Provide droplet size distributions for each condition, measure surface tension or interfacial energy independently, perform rheological measurements on bulk condensates, or use alternative methods such as microrheology to confirm the viscosity differences.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Physiological relevance of in vitro conditions
- **Claim pointer** The authors claim that H1:ssDNA coacervation may be relevant at stalled replication forks based on in vitro experiments and cell-based observations
- **Evidence pointer** Figure 5, Extended Data Fig. 10
- **Concern** The in vitro experiments use high concentrations of H1 (2.5 μM) and DNA (10 μM) with 200 mM NaCl and 10% PEG8000. These conditions may not reflect the nuclear environment where H1 is present at estimated concentrations of ~1-5 μM but where DNA is chromatinized and associated with many other proteins. The cell-based experiments show H1 puncta that increase upon replication stress, but the colocalization with PCNA is not quantified, and the specificity of this interaction is not demonstrated. The claim that H1:ssDNA coacervation stabilizes replication forks is speculative and not directly tested.
- **Why it matters** The authors propose a new biological function for H1 at replication forks. If the in vitro conditions are not representative of the cellular environment, the relevance of the proposed mechanism remains uncertain.
- **Resolution test** Perform experiments at more physiologically relevant salt and crowding conditions, test whether H1:ssDNA condensates form in the presence of RPA and other replication fork proteins, quantify colocalization with PCNA and other fork markers, and directly test whether H1 depletion affects fork stability.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Simulation-experiment consistency
- **Claim pointer** The authors claim that molecular dynamics simulations support the experimental observations and reveal that multivalent H1:ssDNA interactions drive enhanced phase separation
- **Evidence pointer** Figure 4, Extended Data Fig. 6
- **Concern** The coarse-grained simulations use a simplified model with implicit solvent and a rescaling of DNA parameters to reproduce persistence lengths. The force field for H1 is based on MOFF with additional structure-based potentials. While the critical temperatures match the experimental A350 trends, the simulations do not directly model the experimental conditions (e.g., salt concentration, PEG). The claim that simulations "corroborate" the experimental results is somewhat overstated given the significant simplifications. Additionally, the simulations show that H1 forms extensive contacts with dsDNA, which would seem to predict strong phase separation with dsDNA, yet the experiments show the opposite. The authors explain this by arguing that multivalency is key, but this explanation is not directly tested in the simulations.
- **Why it matters** The simulations are used to provide mechanistic insight, but if the model does not capture the key physics, the proposed mechanism may be incorrect.
- **Resolution test** Perform simulations that more directly mimic the experimental conditions, test the multivalency hypothesis by systematically varying the number of binding sites, or provide additional validation of the simulation predictions through experiments.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** In vivo evidence for phase separation
- **Claim pointer** The authors claim that H1 forms phase-separated puncta in cells and that these increase upon replication stress
- **Evidence pointer** Figure 5, Extended Data Fig. 7-9
- **Concern** The evidence for phase separation in cells relies on puncta formation and fusion events. However, puncta could also represent aggregates or protein accumulations at specific genomic loci. The fusion events are shown in a single time-lapse series, and the frequency of such events is not quantified. The claim that H1 puncta are distinct from chromatin is based on the observation that some puncta do not colocalize with H2B, but the fraction of such puncta is not reported. The increase in puncta upon HU/AZD6738 treatment is quantified, but the specificity of this response is not demonstrated.
- **Why it matters** The in vivo experiments are important for establishing biological relevance, but the current evidence does not definitively demonstrate that the puncta are phase-separated condensates.
- **Resolution test** Perform fluorescence recovery after photobleaching (FRAP) on individual puncta in cells, use optical highlighting or photoactivation to demonstrate exchange, test sensitivity to 1,6-hexanediol, and quantify the fraction of puncta that are chromatin-free.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 1
- **Evidence pointer** Figure 1b, d
- **Issue** The description of the single-molecule experiments is somewhat unclear regarding the distinction between "slack" and "taut" ssDNA. The authors state that H1 binds to relaxed ssDNA but not ssDNA under tension, but the exact force ranges and how "slack" is defined are not clearly specified.
- **Required correction** Provide a clear definition of the force ranges for slack versus taut ssDNA and describe how the transition between these states was determined.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure legends
- **Evidence pointer** Figure legends (location not provided)
- **Issue** The manuscript states that statistical tests and p-values are reported in figure legends, but the legends are not included in the provided text. This makes it impossible to assess the statistical rigor of the comparisons.
- **Required correction** Include the full figure legends with statistical details in the manuscript.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Droplet fusion assay
- **Evidence pointer** Methods section
- **Issue** The droplet fusion assay description does not specify how droplets were selected for fusion experiments, whether there was any size selection, or how many independent experiments were performed.
- **Required correction** Provide details on droplet selection criteria, number of replicates, and any potential biases in droplet selection.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation of RNA results
- **Affected element** Figure 3d, e
- **Evidence pointer** Figure 3
- **Issue** The authors report that H1:RNA droplets take much longer to fuse, if at all, but do not discuss potential reasons for this difference or its biological implications.
- **Required correction** Add a brief discussion of the RNA results and their potential significance.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract and Discussion
- **Evidence pointer** Abstract, Discussion
- **Issue** The term "coacervation" is used in the title and throughout, but the distinction between coacervation and liquid-liquid phase separation is not clearly defined. These terms are sometimes used interchangeably but can have different connotations.
- **Required correction** Clarify the use of terminology and define what is meant by coacervation in this context.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness of simulation description
- **Affected element** Methods, MD simulations
- **Evidence pointer** Methods section
- **Issue** The simulation methods do not specify the number of independent simulation runs, the equilibration protocol in detail, or how the critical temperature was extracted from the density data.
- **Required correction** Provide additional details on simulation setup, number of replicates, and analysis procedures.

## Risk / unsupported claims
- The claim that H1:ssDNA coacervation stabilizes replication forks is not directly tested and is presented as speculation in the Discussion
- The claim that H1 and RPA occupy separate nuclear regions is based on qualitative observations and is not quantified
- The claim that H1 puncta in cells represent phase-separated condensates is not definitively established, as alternative explanations (e.g., aggregates, protein accumulations) are not excluded
- The physiological relevance of the in vitro phase separation conditions is not demonstrated
- The quantitative relationship between fusion time and material properties (viscosity, elasticity) is not established through independent measurements