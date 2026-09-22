## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, or supplementary materials provided
- **Shared manuscript claim summary** The authors introduce OpenCGChromatin, a coarse-grained model enabling near-atomistic simulations of chromatin systems up to tens of kilobases, and claim that it independently predicts linker-DNA-dependent chromatin structures observed by cryo-ET, relative thermodynamic stability of condensates from biochemical assays, resolves histone-tail dynamics and interaction networks, and identifies acetylation pattern-specific effects on chromatin compaction with H4K16 and H3K9 as most disruptive.
- **Visible evidence base** Abstract text only; no quantitative results, methodological details, or validation data
- **Missing materials affecting confidence** Full manuscript, methods description, simulation parameters, validation datasets, comparison details with cryo-ET and biochemical assays, and all figures or tables

## Reviewer
- **Overall assessment** The abstract presents a potentially impactful computational advance in chromatin modeling, with claims of predictive power and novel mechanistic insights. However, the evidence base is limited to the abstract, and the claims are broad and ambitious. The central assertions regarding independent prediction, experimental validation, and mechanistic resolution cannot be evaluated without access to the full methods and results. The work is likely of interest to the chromatin biology and computational biophysics communities, but the current evidence does not establish the case.
- **Who would be interested in the results, and why** Chromatin biologists studying genome organization and phase separation, computational biophysicists developing coarse-grained models, and researchers interested in epigenetic regulation, particularly histone modifications and their structural consequences. The model's claimed capability to bridge molecular detail and emergent organization would appeal to those seeking predictive frameworks for chromatin behavior.
- **Major strengths** The abstract describes a model with a clear advance in system size and resolution, which is a significant technical achievement if substantiated. The claim of independent prediction from physicochemical principles is a strong and testable assertion. The focus on histone-tail dynamics and acetylation effects addresses a biologically relevant and underexplored area.
- **Major Concerns** The abstract lacks quantitative evidence for all major claims. The term "independently predict" is used without specifying the nature of the predictions or the comparison metrics. The claim of resolving experimentally inaccessible dynamics is strong and requires demonstration of accuracy. The identification of H4K16 and H3K9 as most disruptive is presented without energetic or statistical context. The abstract does not describe the model's limitations or the scope of its applicability.
- **Minor Comments** The abstract would benefit from a brief statement of the model's key parameters or resolution. The phrase "near-atomistic" is vague and should be defined. The relationship between the 108-nucleosome fiber simulations and the condensate simulations is unclear. The abstract does not mention any potential artifacts or approximations in the model.
- **Technical failings that need to be addressed before the case is established** The abstract does not provide any quantitative validation data, such as correlation coefficients, error bars, or comparison statistics with cryo-ET and biochemical data. The mechanistic claims about histone-tail dynamics require evidence of convergence and reproducibility. The energetic analysis of acetylation effects needs a clear definition of the energy metric and its uncertainty.
- **Assessment against Nature-style criteria** Originality: The model appears to offer a novel combination of scale and resolution, but the abstract does not distinguish it clearly from existing coarse-grained models. Scientific importance: The questions addressed are of high importance, but the evidence is insufficient to assess the impact. Interdisciplinary readership: The work bridges biophysics and molecular biology, but the abstract is written for specialists and may not be accessible to a broader audience. Technical soundness: Cannot be assessed from the abstract; no methodological details are provided. Readability for nonspecialists: The abstract uses technical jargon without sufficient context, limiting accessibility.
- **Recommendation posture** Currently not established from the provided evidence. The claims are promising but require the full manuscript to verify the technical implementation, validation, and interpretation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "OpenCGChromatin simulations independently predict, from physicochemical principles, the linker-DNA-dependent chromatin structures observed by cryo-ET and the relative thermodynamic stability of condensates inferred from biochemical assays."
- **Evidence pointer** Abstract; location not provided
- **Concern** The claim of independent prediction is central to the paper's significance, but the abstract provides no quantitative details on how predictions were made, what specific structures or stabilities were compared, or what statistical measures were used to establish agreement with experimental data.
- **Why it matters** Without quantitative validation, the claim of predictive power cannot be distinguished from post-hoc fitting or qualitative agreement. The term "independently predict" implies a strong test that must be demonstrated with clear metrics.
- **Resolution test** Provide in the full manuscript a detailed comparison with cryo-ET structures and biochemical stability data, including correlation coefficients, root-mean-square deviations, or other appropriate statistical measures, and specify the model parameters that were not tuned to match these data.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "OpenCGChromatin resolves histone-tail dynamics and interaction networks that remain inaccessible experimentally, explaining how linker-DNA length controls histone tail accessibility and the resulting multiscale structure of chromatin condensates."
- **Evidence pointer** Abstract; location not provided
- **Concern** The claim of resolving experimentally inaccessible dynamics is strong and requires evidence that the model's predictions are physically accurate. The abstract does not describe how the model's resolution of tail dynamics was validated or how the interaction networks were derived.
- **Why it matters** If the model's predictions about tail dynamics are not validated against any known experimental or theoretical benchmarks, the mechanistic explanations may be artifacts of the model's approximations.
- **Resolution test** Include validation of tail dynamics against available experimental data (e.g., NMR or FRET measurements) or against higher-resolution simulations, and provide a clear description of how interaction networks were computed and their sensitivity to model parameters.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "Extending simulations to 108-nucleosome fibers shows that acetylation disrupts chromatin compaction in a pattern-specific manner by weakening key tail-mediated interactions, with H4K16 and H3K9 emerging as the most energetically disruptive modifications."
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract states a specific ranking of acetylation effects but provides no quantitative data, such as free energy differences, compaction metrics, or statistical significance. The term "most energetically disruptive" is undefined.
- **Why it matters** The ranking of H4K16 and H3K9 is a specific and potentially impactful finding, but without quantitative support, it cannot be assessed for robustness or biological relevance.
- **Resolution test** Provide quantitative measures of compaction (e.g., radius of gyration, contact probabilities) and energetic contributions (e.g., interaction energy differences) for each acetylation pattern, with error estimates and statistical tests.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Model description
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "near-atomistic" is used without definition, and the abstract does not specify the resolution of the model or its key approximations.
- **Required correction** Define "near-atomistic" in terms of the model's resolution (e.g., number of beads per amino acid or nucleotide) and state the key approximations in the abstract or introduction.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Scope
- **Affected element** Claim of system size
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract claims simulations "an order of magnitude larger than previously possible" but does not specify the previous state of the art or the computational cost.
- **Required correction** Provide a brief comparison with existing models in terms of system size and simulation time, and state the computational resources required.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability
- **Affected element** Terminology
- **Evidence pointer** Abstract; location not provided
- **Issue** Terms such as "linker-DNA-dependent chromatin structures" and "pattern-specific manner" are used without explanation, which may limit accessibility for nonspecialists.
- **Required correction** Briefly explain these terms in the abstract or provide a schematic figure to illustrate the concepts.

## Risk / unsupported claims
- The claim of "independently predict" is unsupported without quantitative validation data.
- The claim of resolving "histone-tail dynamics and interaction networks that remain inaccessible experimentally" is unsupported without validation or benchmarks.
- The specific ranking of H4K16 and H3K9 as "most energetically disruptive" is unsupported without quantitative energetic data.
- The claim of achieving simulations "an order of magnitude larger than previously possible" is unverifiable without comparison to prior work.
- The overall assertion that the model "links molecular detail to emergent chromatin organization" is a broad conclusion that cannot be assessed from the abstract alone.