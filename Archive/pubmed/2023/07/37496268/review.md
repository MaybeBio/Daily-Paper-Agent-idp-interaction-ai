## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors use mesoscopic simulations of a model postsynaptic density (PSD) system, comprising the AMPAR-TARP complex and PSD-95, to compare protein assembly behavior in three dimensions (3D, cytosol-like) and two dimensions (2D, membrane-associated). They report that the same domain interactions produce phase-separated condensates in 3D but only clustered, non-phase-separated assemblies in 2D, and they generalize this to suggest that stable phase separation is more difficult in or beneath membranes than in 3D.
- **Visible evidence base** Abstract text only; no simulation details, parameter values, quantitative results, or experimental comparisons are visible
- **Missing materials affecting confidence** Full manuscript, simulation methodology, model parameters, quantitative phase diagrams, cluster size distributions, comparison with experimental data, and any statistical or error analysis

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting comparative simulation study of protein assembly in 3D versus 2D, using the PSD as a biologically relevant model. The central observation, that identical domain interactions yield different assembly outcomes in 3D versus 2D, is plausible and could be of interest to the biophysics and cell biology communities. However, the abstract alone provides insufficient detail to evaluate the technical soundness of the simulations, the robustness of the claimed contrast, or the validity of the broader generalization. The claim that stable phase separation is generally more difficult in 2D than in 3D is presented as a suggestion but is not supported by the limited evidence shown.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, membrane-associated protein organization, and synaptic biology would be interested. The work addresses a fundamental question about dimensionality effects on phase behavior, which is relevant to understanding how condensates form at membranes versus in the cytosol. The PSD context adds specific relevance for neuroscientists interested in receptor clustering and synaptic plasticity.
- **Major strengths** The study addresses a timely and important question about dimensionality effects on phase separation. The use of a biologically relevant model system (PSD) grounds the work in a concrete context. The comparative design, using identical domain interactions in 3D and 2D, is a clean approach to isolate the effect of dimensionality.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide any quantitative evidence, simulation details, or validation against experimental data. Without these, the core claim of a qualitative difference between 3D and 2D assembly cannot be assessed. The generalization to broader systems is not supported by the presented evidence.
- **Assessment against Nature-style criteria** 
  - Originality: The question of dimensionality effects on phase separation is not entirely new, but the specific application to PSD proteins and the comparative simulation approach may offer a fresh perspective. However, the abstract does not clearly articulate what is novel beyond the specific system.
  - Scientific importance: If the claims are robust, the work could have implications for understanding membrane-associated condensates, which are biologically widespread. The importance is moderate to high, but the abstract does not establish the broader impact convincingly.
  - Interdisciplinary readership: The topic bridges biophysics, cell biology, and neuroscience, which could attract a broad audience. However, the abstract is written in a way that assumes familiarity with PSD and phase separation concepts, which may limit accessibility.
  - Technical soundness: Not assessable from the abstract. No simulation methodology, parameter choices, or validation are provided.
  - Readability for nonspecialists: The abstract is reasonably clear but uses jargon (e.g., AMPAR-TARP, PSD-95, mesoscopic simulations) without sufficient context for a general reader.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents an interesting hypothesis but lacks the technical detail and quantitative support needed to evaluate the claims. A full manuscript with detailed methods and results would be required to assess whether the case is made.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "with identical domain interactions, AMPAR-TARP embedded in the membrane formed clusters with PSD-95, but did not form a stable separated phase," implying a qualitative difference in phase behavior between 3D and 2D.
- **Evidence pointer** Abstract, no specific section or figure provided; location not provided
- **Concern** The abstract provides no details on the simulation model, such as the representation of protein domains, interaction potentials, system size, simulation time, or how phase separation versus clustering was operationally defined. Without this information, it is impossible to assess whether the observed difference is a genuine physical effect or an artifact of the model setup, such as finite-size effects, insufficient sampling, or inappropriate interaction parameters.
- **Why it matters** The central conclusion rests on the reliability of the simulations. If the 2D system was not simulated long enough or with sufficient spatial resolution, the absence of phase separation could be a false negative. Conversely, the 3D phase separation could be an artifact of the chosen parameters. The claim of a dimensional contrast is only meaningful if the model is validated and the simulation conditions are shown to be equivalent in all respects except dimensionality.
- **Resolution test** The full manuscript must provide a detailed description of the mesoscopic model, including interaction potentials, parameter values, system sizes, and simulation durations. The authors should show that the 3D system reaches a stable phase-separated state and that the 2D system is simulated under comparable conditions with adequate sampling. Ideally, they would also vary parameters (e.g., interaction strength, concentration) to demonstrate that the qualitative difference is robust.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors state that "a mixture of a soluble variant of the AMPAR-TARP complex and PSD-95 in the 3D system resulted in a phase-separated condensate, which was consistent with the experimental results."
- **Evidence pointer** Abstract, reference to "recent in vitro studies" but no specific citation or quantitative comparison; location not provided
- **Concern** The abstract claims consistency with experimental results but provides no quantitative comparison, such as matching droplet sizes, concentrations, or phase boundaries. It is unclear whether the simulation reproduces experimental observations in a meaningful way or merely produces a qualitatively similar outcome. Without a direct comparison, the claim of consistency is unsubstantiated.
- **Why it matters** The experimental consistency is used to validate the model. If the model is not quantitatively validated, the subsequent claim about 2D behavior lacks a credible foundation. A qualitative match could be coincidental, and the model might not capture the relevant physics.
- **Resolution test** The full manuscript should include a quantitative comparison between simulation results and experimental data, such as phase diagrams, critical concentrations, or cluster size distributions. The authors should specify which experimental studies were used and how the comparison was performed.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scope of claim
- **Claim pointer** The authors generalize that "stable phase separation can be more difficult to achieve in and beneath the membrane than in 3D systems."
- **Evidence pointer** Abstract, concluding statement; location not provided
- **Concern** This generalization extends beyond the specific system studied (AMPAR-TARP and PSD-95) to all membrane-associated systems. The abstract provides no basis for such a broad conclusion, as it is based on a single model system with specific interaction parameters. The claim is presented as a suggestion, but even as a suggestion, it requires more support than a single simulation study.
- **Why it matters** Overgeneralization can mislead readers into thinking the finding is universal when it may be system-specific. The dimensionality effect could depend on the nature of the interactions, the membrane model, or the specific proteins involved. Without additional systems or theoretical arguments, the claim is speculative.
- **Resolution test** The authors should either temper the claim to be specific to their system or provide additional evidence, such as simulations with different protein pairs or a theoretical analysis explaining why 2D systems generally suppress phase separation. At minimum, they should discuss the conditions under which their conclusion might not hold.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract, first sentence
- **Evidence pointer** Abstract, opening statement; location not provided
- **Issue** The phrase "cellular biomolecular condensates formed via phase separation have received considerable attention" is vague and does not specify the context or why this attention is relevant to the study.
- **Required correction** Provide a more specific framing, such as mentioning the role of condensates in cellular organization or the open question of dimensionality effects, to better orient the reader.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract, use of "3D" and "2D"
- **Evidence pointer** Abstract, throughout; location not provided
- **Issue** The terms "3D" and "2D" are used to refer to cytosol and membrane-associated systems, respectively, but this is not explicitly defined. A reader unfamiliar with the field may be confused.
- **Required correction** Define "3D" as solution/cytosol conditions and "2D" as membrane-associated conditions at first use, or use more descriptive terms.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Abstract, methods description
- **Evidence pointer** Abstract, "mesoscopic model of protein-domain interactions"; location not provided
- **Issue** The abstract does not explain what "mesoscopic" means in this context or what level of detail the model captures. This is important for assessing the relevance of the results.
- **Required correction** Briefly describe the model resolution, such as whether it uses coarse-grained domains or explicit molecules, to help the reader understand the scope of the simulations.

## Risk / unsupported claims
- The claim of a qualitative difference in phase behavior between 3D and 2D is unsupported without simulation details and quantitative results.
- The claim of consistency with experimental results is unsupported without a specific quantitative comparison.
- The generalization that stable phase separation is more difficult in or beneath membranes than in 3D is unsupported and speculative based on the abstract alone.
- The relevance of the findings to synaptic plasticity, mentioned in the abstract, is not substantiated by any evidence presented.