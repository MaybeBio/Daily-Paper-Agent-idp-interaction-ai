## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results and discussion, conclusion) and figure references; supplementary material not provided.
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and internal consistency based solely on the supplied text and figure descriptions.
- **Shared manuscript claim summary** The authors propose that RNA modulates phase separation, internal dynamics, and aggregation of FUS LC-RGG1 through diverse molecular contacts, with low RNA concentrations promoting and high concentrations disrupting condensates, and that RNA accelerates liquid-to-solid transition.
- **Visible evidence base** Descriptions of DIC microscopy, turbidity assays, UV spectrophotometry, NMR spectroscopy (HSQC, relaxation, NOE), coarse-grained and atomistic simulations, and aggregation time-course experiments with ThT fluorescence.
- **Missing materials affecting confidence** Supplementary figures (S1–S6), full NMR spectral assignments, simulation parameters and force field details, raw data, statistical analyses, and experimental replicates are not available. Figure panels are referenced but not shown.

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question regarding the molecular mechanisms by which RNA modulates FUS condensate behavior. The integration of biochemical, NMR, and simulation approaches is commendable and the findings are potentially significant. However, several technical concerns and missing details limit the strength of the conclusions as currently presented. The claim that RNA accelerates liquid-to-solid transition appears to conflict with the observed decrease in condensate density and enhanced mobility, and the proposed reconciliation via interfacial effects is speculative without direct evidence. The manuscript would benefit from additional controls, quantitative analyses, and clarification of simulation and NMR methodologies.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, RNA-binding proteins, and neurodegenerative disease mechanisms would find these results of interest. The work provides molecular-level insights into how RNA modulates condensate properties and aggregation, which is relevant for understanding FUS biology and for designing therapeutic strategies targeting aberrant phase transitions.

- **Major strengths** The study combines multiple complementary techniques to address a complex question. The use of NMR to probe residue-specific interactions in both dispersed and condensed phases is particularly valuable. The identification of diverse amino acid types, including polar residues such as glutamine, in RNA contacts within condensates extends current understanding beyond simple electrostatic models. The reentrant phase behavior is well-documented and consistent with prior work on related systems.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "RNA accelerates the liquid-to-solid transition of FUS LC-RGG1 condensates, promoting fibrillar aggregate formation."
- **Evidence pointer** Figure 5A–D, Results section "RNA accelerates FUS LC-RGG1 liquid-to-solid transition"
- **Concern** The claim that RNA accelerates aggregation is based on DIC microscopy and ThT fluorescence, but the authors also report that RNA decreases condensate density and increases molecular mobility. These observations appear contradictory, as enhanced mobility and reduced density would typically be expected to slow aggregation. The authors propose that aggregation occurs preferentially at the condensate interface, but no direct evidence for interfacial localization of aggregates or RNA is provided.
- **Why it matters** The central conclusion regarding RNA's pro-aggregation effect is not mechanistically supported by the presented data. If the effect is real but occurs via an interfacial mechanism, direct evidence is required. Without this, the conclusion remains speculative and potentially misleading.
- **Resolution test** Provide time-resolved imaging showing where aggregates first appear relative to the condensate interface. Quantify aggregate formation in bulk versus surface regions. Alternatively, perform experiments with varying surface-to-volume ratios to test the interfacial hypothesis.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "NMR and simulation data show diverse interactions between amino acids and RNA moieties, including prominent glutamine-RNA contacts, that stabilize FUS-RNA co-condensates."
- **Evidence pointer** Figure 4A–G, Results section "Many types of amino acids mediate RNA contact in FUS-RNA condensed phase"
- **Concern** The NOE experiments are described qualitatively, and the quantitative analysis appears limited to intensity comparisons at specific chemical shifts. The assignment of NOEs to specific amino acid types is not fully described, and the possibility of spin diffusion or indirect effects is not addressed. The simulation results are presented as supporting the experimental findings, but the force field and sampling methodology are not described in sufficient detail to assess their reliability.
- **Why it matters** The identification of specific amino acid types mediating RNA contacts is a key finding. If the NOE assignments are ambiguous or the simulations are not converged, the conclusions regarding the diversity of molecular contacts may be overstated.
- **Resolution test** Provide a detailed description of NOE assignment procedures, including controls for spin diffusion. Include convergence metrics for simulations and validation of force field parameters against experimental data.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** "At a 6:1 protein-to-RNA ratio, approximately 64% of polyU RNA molecules partitioned into the WT FUS condensates, whereas only 43% the RNA entered the Q→G condensates."
- **Evidence pointer** Figure 5B, Results section "Glutamine residues in FUS LC stabilize FUS-RNA co-phase separation"
- **Concern** The partitioning experiments are described for a single condition, and no error bars or statistical analyses are provided. The number of independent replicates is not stated. The claim of a significant reduction in RNA partitioning for the Q→G variant requires statistical support.
- **Why it matters** The conclusion that glutamine residues are critical for RNA recruitment into condensates depends on the robustness of this measurement. Without replicates and statistics, the finding may not be reliable.
- **Resolution test** Provide mean and standard deviation from at least three independent experiments, with appropriate statistical testing.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "The substantially lower phase density with incorporation of only relatively small amounts of RNA by mass fraction may be used by cells to alter material properties of phases."
- **Evidence pointer** Figure 1E, Results section "FUS LC-RGG1 phase separation is modulated by RNA"
- **Concern** The density measurements are based on UV spectrophotometry of urea-dissolved condensates, which provides a bulk average. The claim that small amounts of RNA cause substantial density reduction is not quantitatively supported, as the relationship between RNA mass fraction and density change is not systematically explored.
- **Why it matters** The proposed biological relevance of density modulation depends on the magnitude of the effect. If the effect is small or within experimental error, the conclusion may be overstated.
- **Resolution test** Provide a titration of RNA concentration versus condensate density, with error analysis, to demonstrate the magnitude and significance of the effect.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** "RNA-containing samples transitioned from liquid-like droplets to increasingly solid aggregates far more rapidly than FUS-only controls."
- **Evidence pointer** Figure 5A–B, Results section "RNA accelerates FUS LC-RGG1 liquid-to-solid transition"
- **Concern** The aggregation experiments are described for both shaking and quiescent conditions, but the time points and criteria for "visible aggregates" are not defined. The quantification of aggregation kinetics is not provided beyond representative images.
- **Why it matters** The claim of accelerated aggregation requires quantitative kinetic data. Without defined criteria and time-resolved measurements, the conclusion is not robust.
- **Resolution test** Provide time-resolved turbidity or ThT curves with fitted kinetic parameters for multiple replicates.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1A
- **Evidence pointer** Figure 1A
- **Issue** The domain architecture schematic is referenced but not described in the text. The boundaries of LC and RGG1 domains are not explicitly stated.
- **Required correction** Add a brief description of the domain boundaries and residue numbers in the text or figure legend.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section "Comparing the location and effects of RNA interactions with FUS in the dispersed and condensed phases"
- **Evidence pointer** Figure 2A–F
- **Issue** The comparison between dispersed and condensed phase CSPs is described, but the criteria for "comparable magnitude" are not defined quantitatively.
- **Required correction** Provide a quantitative comparison, such as average CSP values or a correlation plot, to support the claim.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods
- **Evidence pointer** Location not provided
- **Issue** The manuscript lacks a detailed Methods section. Simulation parameters, NMR acquisition parameters, and sample preparation details are not described.
- **Required correction** Include a comprehensive Methods section or reference prior publications with full methodological details.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Conclusion
- **Evidence pointer** Conclusion section
- **Issue** The statement that "RNA promotes a reorganization of the protein interaction network within the condensate to favor nucleation of amyloid aggregation" is presented as a conclusion, but it is one of several possible interpretations.
- **Required correction** Soften the language to indicate this is a proposed model rather than an established conclusion.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 3C
- **Evidence pointer** Figure 3C
- **Issue** The diffusion coefficients are reported with error bars, but the number of replicates and the method of error calculation are not stated.
- **Required correction** Specify the number of replicates and the error calculation method in the figure legend or text.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Supplementary material
- **Evidence pointer** Supplementary figures S1–S6
- **Issue** Supplementary figures are referenced but not provided in the manuscript text. Their content is not described.
- **Required correction** Ensure supplementary figures are available and briefly describe their content in the main text.

## Risk / unsupported claims
- The claim that RNA accelerates liquid-to-solid transition via interfacial effects is not directly supported by the presented data and requires additional evidence.
- The identification of specific amino acid types mediating RNA contacts in the condensed phase relies on NOE assignments and simulations that are not fully described, making the claim difficult to evaluate.
- The quantitative relationship between RNA concentration and condensate density reduction is not established with statistical rigor.
- The biological relevance of the observed density changes is speculative and not tested in cellular contexts.
- The claim that glutamine residues are critical for RNA partitioning is based on a single condition without replicates or statistical analysis.