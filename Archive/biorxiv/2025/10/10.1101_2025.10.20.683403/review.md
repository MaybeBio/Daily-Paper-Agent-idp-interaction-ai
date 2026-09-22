## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no figures, methods, or supplementary material were provided
- **Shared manuscript claim summary** The authors use a near-atomistic coarse-grained chromatin model to propose that Oct4 increases DNA accessibility in chromatin fibres by driving them into compact liquid-like states, rather than by decondensing chromatin. They describe a three-stage cluster formation process involving nucleation, attachment via DNA binding domains, and growth amplified by long linkers, and conclude that Oct4 exploits multivalency, nucleosome breathing, and chromatin flexibility to reconcile condensation with enhanced accessibility.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary information were supplied
- **Missing materials affecting confidence** Full manuscript, all figures and tables, model parameterization details, simulation protocols, validation against experimental data, and any quantitative analyses

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting and potentially significant hypothesis that Oct4 promotes accessibility through liquid-like chromatin condensation rather than decondensation. However, the evidence base is limited to the abstract, and the claims are largely qualitative. The mechanistic model is plausible but requires rigorous validation, particularly regarding the relationship between simulated liquid-like states and experimentally observed chromatin behaviour. The relevance to the "search problem" and reprogramming is stated but not substantiated in the provided material.
- **Who would be interested in the results, and why** Researchers in chromatin biology, transcription factor mechanisms, genome organization, and computational biophysics would find these results relevant. The proposed mechanism could inform studies on pioneer factor function, epigenetic reprogramming, and the physical principles underlying gene activation in development and disease.
- **Major strengths** The abstract addresses a fundamental and unresolved question about how pioneer factors act beyond single nucleosomes. The proposed mechanism is novel in suggesting that condensation and accessibility are not mutually exclusive. The use of a near-atomistic model with full-length Oct4 and varying nucleosomal repeat lengths is a technically ambitious approach that could provide mechanistic insight.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria**  
  Originality: The proposed mechanism is original in framing Oct4 action as condensation-driven accessibility, which contrasts with prevailing decondensation models. Scientific importance: The question of how pioneer factors access chromatin is of high importance, and the potential resolution of the "search problem" is significant. Interdisciplinary readership: The work bridges biophysics, chromatin biology, and transcription regulation, which could attract broad interest. Technical soundness: Cannot be fully assessed from the abstract; the model's predictive power and validation are not shown. Readability for nonspecialists: The abstract is largely accessible but uses specialized terms (e.g., "near-atomistic coarse-grained", "nucleosomal repeat lengths") that may require some background.
- **Recommendation posture** Currently not established from the provided evidence; supportive if technical concerns are resolved with full data

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The abstract claims that Oct4 increases DNA accessibility by driving fibres into compact liquid-like states in which nucleosomes breathe, reorient, exchange neighbours, and transiently expose DNA.  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The central claim that liquid-like compaction enhances accessibility is presented without quantitative evidence. No metrics for accessibility, compaction, or liquid-like behaviour are described, and no comparison to alternative mechanisms (e.g., partial decondensation) is shown.  
- **Why it matters** This claim is the core of the paper and directly contradicts intuitive expectations that compaction reduces accessibility. Without quantitative support, the conclusion is not established.  
- **Resolution test** Provide quantitative measures of DNA accessibility (e.g., solvent-accessible surface area, nucleosome unwrapping frequencies) and compaction (e.g., radius of gyration) across conditions, with statistical comparisons to control simulations.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Model validity  
- **Claim pointer** The abstract states that the near-atomistic coarse-grained chromatin model is used to dissect Oct4 interactions with chromatin fibres of varying nucleosomal repeat lengths.  
- **Evidence pointer** Abstract, location not provided  
- **Concern** No information is provided on model parameterization, force field accuracy, timescales simulated, or validation against experimental data (e.g., single-molecule or structural studies). The predictive power of the model for liquid-like states is unclear.  
- **Why it matters** The conclusions depend entirely on the model's fidelity. If the model overestimates clustering or breathing, the proposed mechanism may be an artifact.  
- **Resolution test** Include a detailed methods section with parameter values, validation against known chromatin structures or experimental measurements, and a discussion of model limitations.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Mechanistic specificity  
- **Claim pointer** The abstract claims that Oct4 binds preferentially to linker DNA through its structured POU domains, while its disordered activation domains mediate cluster formation, and that growth is amplified when long DNA linkers enable fibre bending and looping.  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The three-stage mechanism is described qualitatively, but no data are shown to support the distinct roles of POU domains versus activation domains, or the linker length dependence. The claim that long linkers amplify growth is plausible but not demonstrated.  
- **Why it matters** The mechanistic model is a key contribution, but without domain-specific mutagenesis or comparative simulations, the roles of different Oct4 regions are speculative.  
- **Resolution test** Provide simulations with truncated or mutated Oct4 variants to isolate domain contributions, and systematically vary linker length to show dose-dependent effects on cluster size and accessibility.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Biological relevance  
- **Claim pointer** The abstract concludes that the mechanism provides a physical route to overcome the transcription-factor "search problem" and activate silenced genes during reprogramming.  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The link to the "search problem" and reprogramming is stated without direct evidence. No experimental context (e.g., cellular data, chromatin immunoprecipitation, or accessibility assays) is provided to connect the simulations to in vivo function.  
- **Why it matters** The broader significance claim extends beyond the simulation results and may overstate the implications without experimental validation.  
- **Resolution test** Add a discussion of how the simulation predictions could be tested experimentally, or include preliminary experimental data if available.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Terminology  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The term "liquid-like states" is used without a clear operational definition.  
- **Required correction** Define "liquid-like" in terms of measurable properties (e.g., dynamic rearrangements, lack of long-range order) and specify how these were assessed in the simulations.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Scope of claims  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The abstract mentions "varying nucleosomal repeat lengths" but does not specify the range or the number of conditions tested.  
- **Required correction** State the specific repeat lengths used and the rationale for their selection.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Model availability  
- **Evidence pointer** Abstract, location not provided  
- **Issue** No mention of code or model availability, which is important for reproducibility.  
- **Required correction** Include a statement on data and code availability in the full manuscript.

## Risk / unsupported claims
- The claim that Oct4 increases accessibility via liquid-like compaction is unsupported without quantitative data.
- The distinct roles of POU domains and activation domains in cluster formation are unsupported without domain-specific simulations.
- The link to the "search problem" and reprogramming is not substantiated by the provided evidence.
- The generalizability of the findings to in vivo chromatin states is not assessable from the abstract.