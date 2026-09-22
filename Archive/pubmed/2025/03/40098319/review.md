## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no methods, figures, or quantitative data were available for evaluation
- **Shared manuscript claim summary** The authors use coarse-grained simulations of two multivalent proteins, one containing a coiled-coil domain (CCD), to argue that CCDs promote liquid-liquid phase separation (LLPS) by preventing loop-closure defects and enabling protein networking. They report that replacing the CCD with a flexible linker abolishes LLPS due to oligomeric cluster formation, and that a critical CCD length exists where the system transitions sharply from no LLPS to LLPS at low concentrations. They conclude that CCDs regulate condensate formation and offer a framework for designing synthetic condensates.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary information provided
- **Missing materials affecting confidence** Full manuscript, simulation methodology, force field parameters, system size and concentration ranges, order parameters for LLPS determination, phase diagram data, error analysis, and any comparison with experimental systems

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting hypothesis regarding the role of folded domain geometry, specifically coiled-coil domains, in modulating biomolecular condensate phase behavior. The proposed mechanism, that CCDs prevent loop-closure defects and thereby enhance network formation, is plausible and could be of interest to the condensate community. However, the abstract alone provides insufficient detail to evaluate the robustness of the simulation results, the generality of the conclusions, or the technical soundness of the approach. The claim of a critical CCD length is intriguing but lacks quantitative support in the abstract. The study may offer a useful design principle for synthetic condensates, but the evidence base is too limited to assess whether the case is established.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates and phase separation, particularly those interested in the role of folded domains and multivalent interactions. Computational biophysicists developing coarse-grained models for condensate systems would also find the approach relevant. Additionally, synthetic biologists and protein engineers designing condensate-based materials or compartments with tunable properties may be interested in the proposed design framework.
- **Major strengths** The abstract addresses a relatively underexplored question, namely how the geometry and structure of folded domains, rather than just their interaction strength, influence phase behavior. The proposed mechanism of preventing loop-closure defects is mechanistically specific and testable. The use of a minimal two-component model system is appropriate for isolating the effect of the CCD. The finding of a critical length threshold is potentially valuable for design purposes.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: the question of how folded domain geometry, specifically coiled-coil length and rigidity, affects phase behavior is a relatively fresh angle in the condensate field, though the general role of multivalency in LLPS is well established. Scientific importance: if the findings are robust, they could inform both fundamental understanding of condensate regulation and practical design of synthetic condensates, which is of moderate to high importance. Interdisciplinary readership: the topic bridges biophysics, cell biology, and synthetic biology, and the abstract is written in a way that is broadly accessible. Technical soundness: cannot be assessed from the abstract alone; the lack of methodological detail and quantitative results prevents evaluation of simulation quality, sampling, or finite-size effects. Readability for nonspecialists: the abstract is clear and concise, with jargon kept to a minimum, though terms such as "loop-closure defects" and "oligomeric clusters" would benefit from brief explanation in the full text.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a plausible and interesting hypothesis, but the absence of methodological detail and quantitative results means the core claims cannot be verified. A supportive posture would require access to the full manuscript, including phase diagrams, simulation details, and control analyses.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that CCDs promote LLPS by preventing loop-closure defects, enabling protein networking, and that replacing the CCD with a flexible linker abolishes LLPS due to formation of oligomeric clusters.
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract provides no quantitative data, such as phase diagrams, critical concentrations, or cluster size distributions, to support the claim that CCDs promote LLPS and that flexible linkers abolish it. The distinction between LLPS and oligomeric cluster formation is asserted but not demonstrated with any measurable order parameter or structural analysis.
- **Why it matters** The central mechanistic claim rests on a qualitative contrast between two conditions. Without quantitative evidence, such as coexistence curves or cluster size analysis, the reader cannot assess whether the observed behavior is robust or an artifact of the specific simulation setup, such as system size, concentration range, or force field choice.
- **Resolution test** Provide phase diagrams for both the CCD-containing and flexible-linker systems, including critical concentrations and coexistence regions. Show cluster size distributions or a structural order parameter that distinguishes LLPS from oligomeric clusters. Include error bars or replicate simulations to demonstrate statistical robustness.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that there is a critical length of the CCD where the system rapidly changes from no LLPS to LLPS at low concentrations.
- **Evidence pointer** Abstract; location not provided
- **Concern** The existence of a sharp threshold in CCD length is a strong, potentially non-linear claim. The abstract does not report the range of lengths tested, the resolution of the length scan, or the specific concentrations at which this transition occurs. It is unclear whether the transition is truly sharp or an artifact of coarse sampling in length or concentration space.
- **Why it matters** A critical length threshold is a key design parameter and a mechanistically informative finding. If the transition is gradual or dependent on simulation conditions, the claim of a "critical" length would be overstated and could mislead experimental design efforts.
- **Resolution test** Show a plot of LLPS propensity (e.g., critical concentration or coexistence region) as a function of CCD length, with sufficient sampling density to resolve the transition. Report the concentration range and demonstrate that the threshold is robust across multiple concentrations and simulation replicates.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility and completeness
- **Claim pointer** The authors claim that the study provides insights into the phase behavior of biomolecular condensates and offers a framework for designing synthetic condensates with tunable phase behaviors.
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract provides no information about the simulation methodology, including the coarse-grained model used, the interaction potentials, the system size, the simulation box, the equilibration protocol, or the sampling time. Without these details, the results cannot be reproduced or evaluated for potential artifacts such as finite-size effects or insufficient sampling.
- **Why it matters** Reproducibility is a core requirement for computational studies. The absence of methodological detail in the abstract is expected, but the full manuscript must provide complete simulation parameters and analysis protocols. As it stands, the claims cannot be independently verified from the provided material.
- **Resolution test** In the full manuscript, provide a detailed methods section including model parameters, simulation protocol, system size, and analysis methods. Include a discussion of potential finite-size effects and sampling convergence.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and precision
- **Affected element** Terminology
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "loop-closure defects" is used without definition. It is unclear whether this refers to intramolecular contacts that prevent intermolecular networking, or a specific topological feature of the protein conformation.
- **Required correction** Define "loop-closure defects" explicitly in the full text, ideally with a schematic or a description of the structural criterion used to identify them in the simulations.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Generalizability
- **Affected element** Scope of conclusions
- **Evidence pointer** Abstract; location not provided
- **Issue** The study uses a single model system with two multivalent proteins. The abstract claims general insights into condensate phase behavior, but it is unclear how the findings would transfer to other coiled-coil-containing proteins or to systems with different valencies or interaction motifs.
- **Required correction** In the full text, discuss the generality of the findings, including limitations of the model and potential variations in sequence, valency, or interaction strength that could alter the observed behavior.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Experimental relevance
- **Affected element** Connection to experimental systems
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract does not mention any connection to experimental observations of coiled-coil-containing condensates. Without such a link, the relevance of the simulation findings to real biological systems remains unclear.
- **Required correction** In the full text, include a discussion of how the simulation predictions could be tested experimentally, or compare the findings with existing experimental data on coiled-coil-containing condensates if available.

## Risk / unsupported claims
- The claim that CCDs promote LLPS by preventing loop-closure defects is unsupported in the abstract due to lack of quantitative data.
- The claim of a critical CCD length with a sharp transition is unsupported without a length scan or phase diagram.
- The claim that flexible linkers abolish LLPS due to oligomeric cluster formation is unsupported without cluster size analysis or structural characterization.
- The general framework for designing synthetic condensates is not assessable from the abstract alone.
- The relevance of the findings to biological condensates is not assessable without experimental comparison or discussion of physiological context.