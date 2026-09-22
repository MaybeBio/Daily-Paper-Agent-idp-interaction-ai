## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no full text, figures, tables, or supplementary materials provided
- **Shared manuscript claim summary** The authors use coarse-grained molecular dynamics simulations with the HPS-Urry model to study phase separation of the plant-specific RNA-binding protein PARCL, incorporating folded eYFP tags into simulations for the first time. They identify key residues driving phase separation, validate predictions experimentally via mutations, and extend simulations to RNA binding with miRNA, finding a consistent contact region supported by predictions and experiments.
- **Visible evidence base** Abstract text only; no quantitative results, simulation details, experimental protocols, or statistical analyses provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, simulation parameter details, experimental methods, mutation constructs, microscopy images, RNA-binding assays, and any statistical or reproducibility data

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting integration of simulation and experiment to map phase-separation-driving residues in a plant RBP and to test the effect of fluorescent tags on condensate properties. However, the current evidence base is too limited to evaluate the technical soundness or robustness of the claims. The central claims of residue-level identification, experimental validation, and RNA-binding site determination are stated without quantitative support, effect sizes, or controls. The work may appeal to researchers in biomolecular condensates and plant biology, but the case is not established from the supplied material.
- **Who would be interested in the results, and why** Researchers studying biomolecular phase separation, particularly those interested in prion-like domains and RNA-binding proteins, would value residue-level determinants of condensation and the inclusion of fluorescent tags in simulations. Plant biologists studying phloem biology or stress responses involving PARCL may also find the RNA-binding and condensate engineering aspects relevant. The methodological advance of simulating tagged proteins could interest computational biophysicists.
- **Major strengths** The abstract identifies a clear gap in the field, namely the exclusion of fluorescent tags from phase-separation simulations, and proposes a practical solution. The combination of simulation-derived predictions with experimental mutation validation is a strong design. The extension to RNA-binding adds functional relevance beyond purely biophysical characterization.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract lacks any quantitative metrics for phase separation (e.g., saturation concentrations, droplet sizes, contact frequencies), no statistical comparisons between wild-type and mutant conditions, no details on simulation convergence or force-field validation, and no description of experimental replicates or controls. Without these, the central claims cannot be assessed.
- **Assessment against Nature-style criteria** Originality is moderate, as the residue-level mapping and tag inclusion are incremental advances. Scientific importance is potentially high for the condensate field, but not demonstrated from the abstract. Interdisciplinary readership is plausible, spanning biophysics, cell biology, and plant science. Technical soundness is unassessable due to missing methods and data. Readability for nonspecialists is adequate, though some jargon (e.g., HPS-Urry, PLD) is not defined in the abstract.
- **Recommendation posture** Currently not established from the provided evidence. Supportive if the full manuscript provides robust quantitative data, controls, and methodological transparency.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "mutations of the most contacted residues... prevent the formation of condensate droplets."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract states that mutations prevent droplet formation but provides no quantitative data, such as the number of mutants tested, the degree of inhibition, or comparison to controls. It is unclear whether "prevent" means complete abolition or significant reduction, and whether this was observed across all replicates.
- **Why it matters** This is the key experimental validation of the simulation predictions. Without quantitative evidence and statistical support, the claim of successful validation is unsupported and could be misleading if the effect is partial or variable.
- **Resolution test** Provide in the full manuscript the number of mutants, droplet formation assays with representative images, quantification of droplet area or number, and statistical tests comparing mutant to wild-type under identical conditions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "adjust the parameters of the simulations to allow the inclusion of folded eYFP tags... these trajectories suggest minor changes to droplet and network structure."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract does not describe how the HPS-Urry model was modified to accommodate folded eYFP, nor how the folded domain was represented. The claim of "minor changes" is vague and lacks quantitative comparison, such as differences in cluster size distributions, density profiles, or contact maps.
- **Why it matters** The methodological novelty rests on this modification. If the approach is not rigorously described and validated, the simulation results cannot be reproduced or trusted, undermining the residue-level predictions derived from these trajectories.
- **Resolution test** In the full manuscript, detail the eYFP representation (e.g., rigid body, Go-model, or explicit beads), provide validation against experimental condensate properties, and report quantitative metrics comparing tagged versus untagged simulations with error estimates.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The authors claim that "a short region of PARCL consistently making contact with the miRNA, which is also in agreement with predictions and experiments."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract provides no details on the simulation setup for RNA, the length of the miRNA, the number of independent simulations, or the criteria for "consistent" contact. The agreement with "predictions and experiments" is asserted without specifying which predictions or experiments, or how agreement was quantified.
- **Why it matters** RNA-binding is a secondary claim but adds functional significance. Without evidence of reproducibility and external validation, this claim is not verifiable and may overstate the confidence in the identified region.
- **Resolution test** Provide simulation parameters for RNA, contact frequency maps with statistical thresholds, and a clear description of the experimental or computational predictions used for comparison, including quantitative agreement metrics.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract terminology
- **Evidence pointer** Abstract text
- **Issue** The term "course-grained" appears to be a typo for "coarse-grained."
- **Required correction** Correct the typo to "coarse-grained."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Abstract context
- **Evidence pointer** Abstract text
- **Issue** The abstract does not define PARCL's biological context, such as its tissue-specific expression or known functions, which would help nonspecialist readers understand the significance.
- **Required correction** Add one or two sentences in the introduction of the abstract to briefly state PARCL's biological role and why its phase separation matters.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Simulation details
- **Evidence pointer** Abstract text
- **Issue** The abstract mentions "HPS-Urry model" but does not specify the version or parameter set used, which is essential for reproducibility.
- **Required correction** In the full manuscript, cite the exact model version and parameter values, and consider mentioning the parameter source in the abstract if space permits.

## Risk / unsupported claims
- The claim that eYFP inclusion causes "minor changes" to droplet and network structure is unsupported without quantitative comparison.
- The claim that specific mutations "prevent" droplet formation is unsupported without quantitative and statistical evidence.
- The claim of agreement between simulation, predictions, and experiments for RNA-binding is unverifiable without details on the external data.
- The general statement that the findings have implications for "model-guided engineering" is speculative and not substantiated in the abstract.