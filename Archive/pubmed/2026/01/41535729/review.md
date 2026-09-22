## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors use molecular dynamics simulations to compare wild-type and phosphorylated FUS condensates, proposing that full-length FUS avoids LLPS impairment via domain-specific compensatory regulation, that FUS-LCD LLPS reduction scales with phosphorylation site number, and that a new viscoelasticity model reveals altered interaction patterns affect condensate viscoelasticity.
- **Visible evidence base** Abstract text only; no methodological details, simulation parameters, quantitative results, or validation data provided
- **Missing materials affecting confidence** Full manuscript, simulation protocols, force field parameters, system construction details, quantitative phase diagrams, viscoelasticity model derivation, validation against experimental data, and all figures and tables

## Reviewer
- **Overall assessment** The abstract addresses a biologically relevant question regarding phosphorylation-dependent modulation of FUS phase behavior, with a potentially interesting mechanistic hypothesis involving inter-domain compensation. However, the current abstract provides insufficient technical detail to evaluate the validity of the simulation approach, the robustness of the conclusions, or the novelty relative to existing computational studies of FUS LLPS. The viscoelasticity model is mentioned but not described, and no quantitative outcomes are presented. The case for a domain-specific compensation mechanism is plausible but not established from the supplied material.
- **Who would be interested in the results, and why** Researchers in biomolecular condensates, phase separation biophysics, and neurodegeneration, particularly those studying post-translational modification effects on LLPS. The proposed compensatory mechanism and viscoelasticity analysis could interest computational biophysicists developing coarse-grained or atomistic models of disordered proteins.
- **Major strengths** The question is well motivated by experimental observations of differential phosphorylation effects between FUS-LCD and full-length FUS. The focus on molecular mechanisms underlying domain-specific responses is timely. The inclusion of viscoelasticity as a condensate property beyond simple phase boundaries adds a potentially valuable dimension.
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
- **Assessment against Nature-style criteria** Originality cannot be fully assessed from the abstract alone, but the proposed compensatory mechanism appears potentially novel. Scientific importance is moderate to high given the relevance to ALS and LLPS regulation. Interdisciplinary readership is plausible, spanning biophysics, cell biology, and computational chemistry. Technical soundness is not assessable from the abstract due to missing methodological detail. Readability for nonspecialists is adequate, though the abstract assumes familiarity with FUS domain architecture and LLPS concepts.
- **Recommendation posture** Currently not established from the provided evidence. Supportive if technical concerns are resolved with full methodological transparency and quantitative validation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that molecular dynamics simulations reveal molecular details of how full-length FUS avoids LLPS impairment through synergistic compensatory regulation among various domains.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract provides no information on the simulation methodology, including force field, water model, salt concentration representation, system size, simulation length, or equilibration criteria. Without these details, the reliability of the simulated condensate structures and the inferred compensatory mechanism cannot be evaluated.
- **Why it matters** Molecular dynamics results for disordered proteins are highly sensitive to force field choice and sampling adequacy. Claims about domain-specific interactions and compensation require demonstration that the simulations are converged and that the observed differences between WT and phosphorylated systems are not artifacts of insufficient sampling or force field bias.
- **Resolution test** Provide full methodological details in the manuscript, including force field validation against experimental data, convergence tests, and replicate simulations. Show that the compensatory interactions are robust across simulation conditions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that for the FUS-LCD system, the extent of LLPS reduction by phosphorylation is associated with the number of phosphorylation sites.
- **Evidence pointer** Abstract only; location not provided
- **Concern** No quantitative data are presented to support this dose-dependent claim. The abstract does not specify how many phosphorylation sites were tested, what range of site numbers was explored, or how LLPS propensity was quantified (e.g., critical concentration, saturation concentration, or binodal curves).
- **Why it matters** A dose-dependent relationship is a strong quantitative claim that requires systematic variation of phosphorylation site number and a clear metric for LLPS propensity. Without such data, the claim remains speculative.
- **Resolution test** Present a systematic series of simulations with varying phosphorylation site counts and show a quantitative relationship between site number and a defined LLPS metric, with statistical significance.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim to have developed a model for analyzing condensate viscoelasticity, which revealed that altered interaction patterns impact condensate viscoelasticity.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The viscoelasticity model is mentioned but not described. No equations, assumptions, or validation are provided. The claim that altered interaction patterns impact viscoelasticity is presented without any quantitative results or comparison to experimental rheological data.
- **Why it matters** Viscoelasticity is a complex property that requires careful definition in the context of coarse-grained or atomistic simulations. Without a clear description of the model and its validation, the viscoelasticity findings cannot be assessed for correctness or significance.
- **Resolution test** Provide a full derivation of the viscoelasticity model, describe how it is applied to simulation trajectories, and validate against experimental measurements or established theoretical predictions for similar systems.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors imply that the domain-specific compensation mechanism explains the experimental observation that phosphorylation does not block initial LLPS of full-length FUS but inhibits conversion to toxic aggregates.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract does not explicitly connect the simulation findings to the experimental observation of inhibited liquid-to-solid conversion. The mechanistic link between altered condensate structure or viscoelasticity and the suppression of fibrous aggregation is not articulated.
- **Why it matters** The biological relevance of the study hinges on explaining the differential experimental outcomes. Without a clear mechanistic bridge from simulated condensate properties to aggregation propensity, the significance of the findings for ALS biology remains unclear.
- **Resolution test** Explicitly discuss how the observed changes in condensate structure, dynamics, or viscoelasticity relate to the kinetic or thermodynamic barriers for fibril formation, and ideally compare with experimental aggregation data.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Abstract background
- **Evidence pointer** Abstract first two sentences
- **Issue** The abstract assumes familiarity with FUS domain architecture and the distinction between LCD and full-length protein without defining these terms.
- **Required correction** Briefly define FUS-LCD and full-length FUS in the abstract or provide context for readers outside the immediate field.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity of claims
- **Affected element** Abstract results statement
- **Evidence pointer** Abstract sentence on "synergistic compensatory regulation"
- **Issue** The term "synergistic compensatory regulation" is vague and not defined in the abstract. It is unclear which domains are involved and what specific interactions are compensated.
- **Required correction** Specify which domains participate in the compensation and describe the nature of the compensatory interactions in concrete terms.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of reporting
- **Affected element** Abstract methods
- **Evidence pointer** Abstract final sentence
- **Issue** The abstract does not state the simulation type (e.g., coarse-grained vs. atomistic), which is critical for interpreting the relevance of the findings.
- **Required correction** State the simulation resolution and any relevant approximations in the abstract or ensure this is prominently described in the full manuscript.

## Risk / unsupported claims
- The claim that full-length FUS avoids LLPS impairment via domain-specific compensation is unsupported from the abstract alone, as no quantitative evidence is provided.
- The dose-dependent relationship between phosphorylation site number and LLPS reduction for FUS-LCD is unsupported without systematic data.
- The viscoelasticity model and its findings are unassessable due to lack of description.
- The mechanistic link between simulated condensate properties and inhibition of toxic aggregation is not established from the abstract.