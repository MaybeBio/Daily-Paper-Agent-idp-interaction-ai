## Review setup
- **Input scope** Full manuscript text (preprint, arXiv:2605.26027v1)
- **Assessment boundary** Scientific content, methodology, internal consistency, and support for claims as presented in the provided text. No external literature verification performed.
- **Shared manuscript claim summary** The authors present a minimal explicit-solvent lattice-gas model with quenched disorder to study liquid-liquid phase separation (LLPS) in protein solutions. They report rich phase behavior (UCST, closed-loop, reentrant) modulated by protein-solvent interactions, and examine the effects of static disorder (crowders) on condensate morphology in both single-component and binary protein systems, under equilibrium and non-equilibrium conditions.
- **Visible evidence base** Main text including Introduction, Model and Method Details, Results and Discussion (Sections III.1–III.5), Conclusion, and figure captions (Figs. 1–6). References to Supplementary Material (Figs. S1–S4) are noted but not provided.
- **Missing materials affecting confidence** Supplementary figures (S1–S4) referenced in the text are not included. The Hamiltonian equation in Section II.1 is mentioned but not displayed. Simulation parameters, convergence criteria, and error analysis details are not fully specified. Figure contents are described in captions but the figures themselves are not visible.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important topic, namely the role of solvent and crowder interactions in modulating biomolecular condensate phase behavior and morphology. The explicit-solvent lattice model is a reasonable extension of the authors' prior implicit-solvent work and offers a tractable framework for exploring these effects. The reported phase diagrams, including reentrant and closed-loop behavior, are potentially interesting. However, the manuscript in its current form has several significant weaknesses. The model description is incomplete, particularly the missing Hamiltonian and insufficient parameter details. The non-equilibrium treatment is introduced but not adequately described or justified. The binary mixture results are presented descriptively without quantitative analysis. The connection to real protein systems remains largely qualitative. These issues prevent the case from being fully established from the provided evidence.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, liquid-liquid phase separation, soft matter physics, and computational biophysics would be interested. The work speaks to ongoing efforts to understand how solvent quality and macromolecular crowding modulate phase separation, and to design stimuli-responsive condensates. The lattice model approach may appeal to those seeking minimal statistical mechanical descriptions of these phenomena.
- **Major strengths** 1. The explicit-solvent treatment is a meaningful step beyond implicit-solvent models and addresses a recognized gap in the field. 2. The systematic exploration of protein-solvent interaction parameters reveals a rich variety of phase behaviors (UCST, closed-loop, reentrant) within a single minimal framework. 3. The inclusion of quenched disorder to mimic crowders and the extension to binary mixtures broaden the scope and potential relevance. 4. The qualitative explanations for the origin of phase behavior changes (e.g., via conformational population shifts) are physically plausible and provide a useful conceptual framework.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The model is described as a "lattice-gas Hamiltonian with quenched disorder" and is claimed to represent proteins, solvents, and crowders with specific interaction parameters.
  - **Evidence pointer** Section II.1, "location not provided" for the Hamiltonian equation
  - **Concern** The Hamiltonian is referenced but not actually displayed in the text. The interaction matrix is mentioned in the Fig. 1 caption but the figure is not available. Without the explicit Hamiltonian and a clear definition of all interaction parameters (J_pp, J_ps, J_cp, J_ss, J_cs, J_un, J_us, J_ns, J_AB, J_cA, J_cB), the model is not fully specified and the results cannot be reproduced or independently evaluated.
  - **Why it matters** A central claim of the paper is that this model produces specific phase behaviors. If the model is not completely and unambiguously defined, the technical basis for all subsequent results is compromised. Reproducibility is a core expectation for computational studies.
  - **Resolution test** Provide the complete Hamiltonian and a table of all interaction parameters used in each simulation. Ensure the model description is self-contained and does not rely on unpublished figures or supplementary material for essential definitions.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors state they studied LLPS "at non-equilibrium (driven) conditions, such as non-Boltzmann protein conformational distribution among the two states and enhanced translational mobility of solvent and proteins due to the non-thermal (active) noise."
  - **Evidence pointer** Section III.1, final paragraph; Fig. S1 (not provided)
  - **Concern** The non-equilibrium simulations are mentioned only briefly. The specific protocol for implementing non-Boltzmann distributions and enhanced mobility is not described. The nature of the active noise, its magnitude, and how it is coupled to the dynamics are unclear. The results of these simulations are not presented in the main text, only referenced via a supplementary figure.
  - **Why it matters** The claim that non-equilibrium conditions shape phase behavior is a significant part of the paper's scope. Without a clear description of the methods and presentation of the results, this claim cannot be evaluated. The intracellular environment is inherently out of equilibrium, so this aspect is potentially important but currently underdeveloped.
  - **Resolution test** Provide a detailed description of the non-equilibrium simulation protocol in the main text or methods. Present the key results of these simulations in the main text with appropriate analysis. Clarify how the non-equilibrium conditions differ from equilibrium and what specific new physics emerges.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The binary mixture results are claimed to show "rich phase-separated morphologies, which can be broadly classified as partially wetted, fully wetted, segregative, and associative," and that these are "delicately sensitive to the protein-solvent interaction."
  - **Evidence pointer** Sections III.4 and III.5; Figs. 5 and 6
  - **Concern** The binary mixture results are presented descriptively. The phase diagrams are shown (in captions) but there is no quantitative analysis of the phase boundaries, no free energy calculations, and no systematic characterization of how the morphology transitions occur. The role of J_AB and J_As is discussed qualitatively but not quantified. The effects of disorder are described in terms of "screening" and "selective de-wetting" but these concepts are not rigorously defined or measured.
  - **Why it matters** The paper claims to provide insights into multicomponent condensate morphology, which is a topic of high current interest. However, descriptive phase diagrams without quantitative analysis limit the depth of insight. The field would benefit from a more mechanistic understanding of what controls the morphology transitions.
  - **Resolution test** Provide quantitative measures of the different morphologies (e.g., order parameters, contact angles, domain sizes). Analyze the phase boundaries in terms of the underlying interaction parameters. Consider free energy calculations to support the observed stability of different morphologies.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The paper claims that "protein-solvent and protein-crowder interactions represent key regulatory parameters for condensate morphology modulation" and that the insights "may guide future computational and experimental studies."
  - **Evidence pointer** Sections III.3, III.5, and IV
  - **Concern** The model is highly simplified (2D lattice, two protein states, static disorder). The connection to real protein systems is made only in general terms. The paper does not discuss how the model parameters map onto real amino acid sequences or solution conditions. The predictive power for experimental systems is not demonstrated or critically assessed.
  - **Why it matters** For the work to have broad impact, the authors need to articulate more clearly what specific, testable predictions emerge from the model and how these could be validated experimentally. Without this, the significance remains largely conceptual.
  - **Resolution test** Discuss specific experimental systems where the model predictions could be tested. Propose concrete parameter regimes or sequence features that would lead to distinct morphologies. Acknowledge the limitations of the 2D lattice model and discuss how results might translate to 3D.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Introduction and model description
  - **Evidence pointer** Section I, Section II.1
  - **Issue** The introduction is dense with citations and assumes significant background knowledge. The model description uses notation (e.g., J_pp, J_ps, sigma, epsilon) that is introduced quickly without sufficient context for a general reader.
  - **Required correction** Briefly explain the physical meaning of each interaction parameter in words. Consider a schematic figure (if not already provided) that illustrates the model components and interactions.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Simulation details
  - **Evidence pointer** Section II.2
  - **Issue** The simulation details are sparse. The number of Monte Carlo steps, equilibration time, number of independent runs, and error estimation methods are not stated. The choice of lattice sizes (100x100 and 200x50) is not justified.
  - **Required correction** Provide standard simulation details including system sizes, number of runs, equilibration and production lengths, and how statistical errors were estimated. Justify the choice of lattice dimensions.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interdisciplinary readership
  - **Affected element** Discussion of results
  - **Evidence pointer** Sections III.1–III.5
  - **Issue** The phase diagrams are described in terms of phases (P1, P2, P3, P4, PW, FW, etc.) but the physical meaning of these phases is not always clearly explained. For example, what distinguishes a "partially wetted" from a "fully wetted" phase in terms of the underlying molecular arrangement?
  - **Required correction** Provide clear definitions of each phase type, possibly with schematic illustrations. Explain the physical interpretation of each phase in the context of protein condensates.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Originality
  - **Affected element** Literature context
  - **Evidence pointer** Section I
  - **Issue** The introduction cites many works but does not clearly delineate what is new in this study compared to the authors' previous implicit-solvent model (Ref. 68) and other lattice models.
  - **Required correction** Explicitly state the novel contributions of this work, particularly the role of explicit solvent and quenched disorder, and how they extend beyond prior models.
- **Technical failings that need to be addressed before the case is established** R1-M1 (missing Hamiltonian and parameter definitions) is the most critical. R1-M2 (inadequate non-equilibrium description) also needs to be addressed. The lack of quantitative analysis in the binary mixture sections (R1-M3) weakens the case but may be addressable with additional analysis.
- **Assessment against Nature-style criteria**  
  *Originality*: Moderate. The explicit-solvent lattice model with quenched disorder is a reasonable extension of prior work, but the conceptual framework (lattice models for LLPS) is well-established. The specific findings on morphology modulation are potentially novel but not groundbreaking.  
  *Scientific importance*: Moderate. The topic is important, and the systematic exploration of parameter space could be valuable. However, the simplified model and lack of quantitative analysis limit the depth of insight. The paper does not yet provide a clear mechanistic understanding that would elevate its importance.  
  *Interdisciplinary readership*: Moderate. The topic bridges soft matter physics and biophysics, but the presentation is likely to be most accessible to computational physicists. The connection to experimental biology is not sufficiently developed.  
  *Technical soundness*: Currently insufficient. The missing Hamiltonian and incomplete simulation details prevent full evaluation. The non-equilibrium treatment is underdeveloped.  
  *Readability for nonspecialists*: Below the standard for a general journal. The paper assumes significant background and does not provide sufficient context for the model and its implications.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript addresses a relevant topic and contains potentially interesting results, but the incomplete model description, underdeveloped non-equilibrium treatment, and lack of quantitative analysis prevent a full assessment. The authors should be encouraged to revise and resubmit with a complete model specification, detailed methods, and more rigorous analysis of the binary mixture results.

## Risk / unsupported claims
- The claim that non-equilibrium conditions "play a key role in shaping the rich phase behavior" is not supported by results presented in the main text; only a supplementary figure is referenced.
- The claim that the model "may guide future computational and experimental studies" is speculative and not substantiated with specific predictions.
- The assertion that the observed morphologies are "consistent with recent computational studies" is made without detailed comparison.
- The statement that the model "improves upon our previous implicit solvent model" is not quantitatively demonstrated.
- The claim that the phase behavior is "invariant to modifications in the initial configurations" is stated but the data is not shown in the main text.