## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as stated in the abstract; no methods, figures, or quantitative results were available for verification
- **Shared manuscript claim summary** The authors present a minimal lattice-gas model with two internal protein states (native and unfolded) and use Monte-Carlo simulations to capture reentrant phase separation with both upper and lower critical solution temperatures. They further report that non-equilibrium effects (non-Boltzmann state populations and enhanced diffusion from non-thermal noise) modulate condensate morphologies, and that an extended binary mixture version reproduces wetted, partially wetted, segregative, and associative phase-separated states.
- **Visible evidence base** Abstract text only; no figures, tables, methods section, or supplementary material provided
- **Missing materials affecting confidence** Full manuscript, simulation details, model Hamiltonian, parameter values, phase diagram figures, quantitative definitions of phase states, and any comparison data from prior computational or experimental studies

## Reviewer
- **Overall assessment** The abstract describes a potentially useful minimal model for thermoresponsive protein phase behavior. The conceptual framework, particularly the two-state internal representation and the exploration of non-equilibrium effects, is interesting and could appeal to the biomolecular condensate community. However, the abstract alone does not provide sufficient quantitative or methodological detail to assess the validity of the central claims. The reentrant phase behavior, the role of non-equilibrium effects, and the binary mixture phase states are all stated without supporting evidence. The case is plausible but not established from the supplied material.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, protein phase separation, and sequence-encoded stimuli-responsive behavior would be interested. The model's simplicity and extensibility to multiple internal states could also attract computational biophysicists and those interested in coarse-grained approaches to intracellular organization. The binary mixture results may interest groups working on multiphase condensate organization.
- **Major strengths** The model is conceptually minimal and tractable, which is valuable for extracting general principles. The inclusion of non-equilibrium effects as a tunable dimension for condensate morphology is a forward-looking idea. The extension to binary mixtures and the reproduction of multiple experimentally observed phase states suggests broad applicability. The proposed extensibility to multiple internal states indicates a scalable framework.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria**  
  Originality: The two-state lattice model with reentrant phase behavior is not entirely novel, as reentrant phase separation has been reported in other protein models, but the specific combination with non-equilibrium effects and binary mixtures adds a fresh angle. Scientific importance: The topic is timely and relevant to the condensate field, but the abstract does not demonstrate that the findings advance fundamental understanding beyond existing models. Interdisciplinary readership: The work could appeal to physicists, chemists, and biologists, but the abstract is written in a specialized language that may limit accessibility. Technical soundness: Cannot be assessed from the abstract alone; no methodological detail or quantitative results are provided. Readability for nonspecialists: The abstract is concise but assumes familiarity with phase separation terminology and lattice models, which may hinder broader readership.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a coherent narrative, but the absence of any quantitative results, methodological detail, or comparison to prior work prevents validation of the core claims. A full manuscript with phase diagrams, simulation protocols, and error analysis would be required to assess whether the case can be supported.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The computed phase diagrams reveal an anomalous reentrant phase separation behavior with both upper and lower critical solution temperatures.  
- **Evidence pointer** Abstract only; no figure or table provided  
- **Concern** The central claim of reentrant phase behavior with both upper and lower critical solution temperatures is stated without any quantitative data, phase diagram, or parameter range. No information is given on the model Hamiltonian, interaction strengths, or how the two internal states are coupled to temperature.  
- **Why it matters** Reentrant phase behavior is a nontrivial and potentially significant result. Without a phase diagram or a description of the conditions under which it emerges, the claim cannot be evaluated or reproduced.  
- **Resolution test** Provide a phase diagram in temperature versus density or interaction parameter space, with clear labeling of the upper and lower critical solution temperatures, and specify all model parameters and simulation conditions.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Methodological transparency  
- **Claim pointer** We also explored non-equilibrium effects, such as non-Boltzmann population distributions of native and unfolded states, and enhanced translational diffusion due to non-thermal noise on the phase separation.  
- **Evidence pointer** Abstract only; methods not provided  
- **Concern** The abstract claims that non-equilibrium effects modulate condensate morphologies, but no details are given on how these effects are implemented in the Monte-Carlo scheme, how non-Boltzmann distributions are generated, or how non-thermal noise is modeled. The magnitude and direction of the reported effects are unspecified.  
- **Why it matters** Non-equilibrium effects are a distinguishing feature of this work. Without a clear description of the simulation protocol, the results cannot be reproduced, and the claim that these factors offer an additional dimension for modulation remains unsupported.  
- **Resolution test** Describe the specific Monte-Carlo moves or update rules that generate non-Boltzmann populations and enhanced diffusion, and provide quantitative comparisons of phase diagrams or morphology metrics with and without these effects.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Validation and comparison  
- **Claim pointer** We further extended our model to study phase separation in binary protein mixtures and successfully reproduced complex phase-separated states, including wetted, partially wetted, segregative, and associative phases.  
- **Evidence pointer** Abstract only; no comparison data provided  
- **Concern** The claim of reproducing four distinct phase states in binary mixtures is made without any visual or quantitative evidence. No definition of these phase states is given in the abstract, and no comparison to the computational studies referenced is provided.  
- **Why it matters** The binary mixture results are presented as a key outcome, but without phase diagrams, representative configurations, or a quantitative match to prior work, the claim of successful reproduction cannot be verified.  
- **Resolution test** Provide representative simulation snapshots or order parameters that distinguish the four phase states, and include a quantitative comparison to the referenced computational studies, such as phase boundaries or coexistence regions.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Generalizability and design relevance  
- **Claim pointer** Our findings offer important insights into designing solvent-mediated effective interactions between proteins for controlled phase separation, relevant for engineering functional condensates.  
- **Evidence pointer** Abstract only; no design rules or parameter mapping provided  
- **Concern** The abstract concludes with design implications, but no specific design rules, parameter ranges, or mapping from model parameters to physical protein properties are presented. The connection between the lattice model and real protein sequences or solvent conditions is not articulated.  
- **Why it matters** The stated relevance to engineering functional condensates is a strong claim. Without a clear pathway from model parameters to experimental observables, the design insights remain speculative.  
- **Resolution test** Specify how model parameters map to physical quantities such as interaction energies, solvent quality, or sequence features, and provide at least one concrete prediction that could be tested experimentally.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Terminology  
- **Evidence pointer** Abstract, first sentence  
- **Issue** The term "minimal lattice-gas model" is used without defining what "minimal" means in this context, such as the number of interaction parameters or the lattice dimensionality.  
- **Required correction** Briefly specify the lattice type and the number of free parameters in the model.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Model extensibility  
- **Evidence pointer** Abstract, final sentence  
- **Issue** The claim that the model can be extended to multiple internal states is stated but not elaborated. It is unclear whether this extension is straightforward or requires new interaction terms.  
- **Required correction** Add one sentence describing how additional internal states would be incorporated and what new physics is expected.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Contextualization  
- **Affected element** Literature comparison  
- **Evidence pointer** Abstract, second sentence  
- **Issue** The abstract mentions "computational and experimental studies on disordered proteins" but does not cite or specify which studies are being referenced, making it difficult to assess the novelty of the observed phase behavior.  
- **Required correction** Include explicit references or a brief description of the prior observations that this model aims to capture.

## Risk / unsupported claims
- The existence of reentrant phase separation with both upper and lower critical solution temperatures is unsupported without a phase diagram.
- The claim that non-equilibrium effects modulate condensate morphologies is unsupported without simulation details or quantitative results.
- The reproduction of wetted, partially wetted, segregative, and associative phases in binary mixtures is unsupported without visual or quantitative evidence.
- The design implications for solvent-mediated interactions are speculative without a mapping from model parameters to physical properties.
- The extensibility to multiple internal states is stated but not demonstrated or described.