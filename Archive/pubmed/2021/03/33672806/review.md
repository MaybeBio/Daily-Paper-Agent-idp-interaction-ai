## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods summary, results, conclusions) without supplementary materials or appendices
- **Assessment boundary** Scientific claims, methodology, evidence quality, and internal consistency based solely on the provided text
- **Shared manuscript claim summary** The authors use a minimal coarse-grained patchy particle model to show that variations in valency and binding affinity among multivalent proteins can regulate the multilayered organization of multicomponent protein condensates, with high-valency species enriched at the core and low-valency species at the interface, driven by maximization of binding site saturation and minimization of interfacial free energy.
- **Visible evidence base** Simulation results described in Sections 3.1–3.3, including density profiles, surface tension values (Table 1), exchange rate order parameters (Figure 5), and phase diagram references (Figure 1)
- **Missing materials affecting confidence** Full methods details (Appendix A), order parameter definitions (Appendix B), simulation parameters, error analysis, and all figures are not provided in the supplied text

## Reviewer
- **Overall assessment** The manuscript presents a systematic computational study using a well-established minimal patchy particle model to explore how valency and binding affinity variations shape the internal organization of multicomponent condensates. The central finding, that high-valency scaffolds localize to the core and low-valency clients to the interface, is physically plausible and consistent with prior experimental observations. However, the evidence base is limited by the absence of figures, detailed methods, and quantitative error analysis. The claim that interfacial free energy minimization is a key driving force is supported by surface tension calculations, but the mechanistic interpretation would benefit from more direct causal evidence. The manuscript is of interest to the biomolecular condensate community, but the current presentation does not fully establish the case without access to the missing methodological and visual details.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, liquid-liquid phase separation, multivalent protein interactions, and the physical chemistry of intracellular organization. The findings on how valency and binding affinity modulate condensate architecture and exchange dynamics are relevant for understanding scaffold-client systems, stress granules, nucleoli, and related membraneless organelles. The work also appeals to computational biophysicists developing coarse-grained models for phase-separating systems.
- **Major strengths** The use of a minimal, well-characterized model allows systematic exploration of a large parameter space. The study addresses a biologically important question with clear translational relevance. The identification of surface tension as a key thermodynamic driver is a valuable contribution. The comparison of four distinct binding scenarios provides a useful framework for interpreting diverse experimental systems.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1 (missing methodological details), R1-M2 (lack of quantitative validation), R1-M3 (insufficient causal evidence for surface tension mechanism)
- **Assessment against Nature-style criteria** Originality: The work offers a novel systematic exploration of valency and affinity effects on multilayered condensate organization, though the model itself is established. Scientific importance: The findings have implications for understanding condensate function and regulation, but the direct biological impact is not demonstrated. Interdisciplinary readership: The topic bridges biophysics, cell biology, and soft matter physics, appealing to a broad audience. Technical soundness: The model is appropriate, but the lack of full methods and error analysis limits confidence. Readability for nonspecialists: The text is generally clear, but the absence of figures makes it difficult for nonspecialists to follow the results.
- **Recommendation posture** Supportive if technical concerns are resolved, specifically the provision of full methods, figures, and quantitative validation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim to use a minimal coarse-grained model for multivalent proteins and perform molecular dynamics simulations, but the provided text lacks sufficient methodological detail to evaluate the validity of the simulations.
- **Evidence pointer** Section 2 (Methods), Appendix A (referenced but not provided)
- **Concern** The methods section is a summary that references Appendix A for details, but the appendix is not included in the supplied material. Key parameters such as simulation box size, number of particles, integration time step, equilibration protocol, and temperature control are not specified. The patchy particle model is described only briefly, and the mapping of valency to patch number and binding affinity to interaction strength is not quantified.
- **Why it matters** Without full methodological transparency, the reproducibility and reliability of the simulation results cannot be assessed. The conclusions depend critically on the model parameters and simulation setup, and any artifacts or inappropriate choices could undermine the findings.
- **Resolution test** Provide the full Appendix A with all simulation parameters, model definitions, and protocols. Include details on system size, sampling, and convergence checks.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors report surface tension values (e.g., γ=0.05±0.04 kBT/σ² for the six-component condensate) and exchange rate order parameters, but the text does not provide the associated figures or tables with full data.
- **Evidence pointer** Section 3.2 (Table 1), Section 3.3 (Figure 5)
- **Concern** The surface tension values are presented with uncertainties, but the methodology for their calculation is not described in the main text. The exchange rate order parameter is defined only in Appendix B, which is not provided. The figures that would show density profiles, exchange dynamics, and phase behavior are referenced but absent from the supplied material.
- **Why it matters** Quantitative claims require transparent presentation of data and analysis methods. Without the figures and detailed definitions, the reader cannot verify the reported values or understand the statistical significance of the results. The error bars on surface tension are large (e.g., 0.05±0.04), which raises questions about the robustness of the comparisons.
- **Resolution test** Include all figures and tables with full data. Provide detailed descriptions of how surface tension and exchange rates were computed, including error estimation methods.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors propose that multilayered organization maximizes the density of LLPS-stabilizing interactions and reduces surface tension, but the causal link between these factors and the observed architecture is not directly tested.
- **Evidence pointer** Section 3.1, Section 3.2, Section 4 (Conclusions)
- **Concern** The manuscript presents correlations between valency, binding affinity, and condensate structure, and shows that surface tension is lower when low-valency proteins are at the interface. However, the claim that this organization "maximizes" interaction density and "reduces" surface tension as a driving force is inferred rather than demonstrated through controlled perturbations or free energy decomposition.
- **Why it matters** The central mechanistic hypothesis would be strengthened by direct evidence, such as comparing the free energy of alternative architectures or systematically varying surface tension while holding other factors constant. Without this, the interpretation remains plausible but not fully established.
- **Resolution test** Perform additional simulations or analyses that directly test the causal role of surface tension, such as computing free energy differences between different spatial arrangements or varying interaction strengths to isolate the effect.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section 3.1 (description of four mixtures)
- **Evidence pointer** Section 3.1, Figure 2 (referenced but not provided)
- **Issue** The descriptions of the four mixtures (valency-driven, like-valency, non-competing scaffolds, competing scaffolds) are clear in text, but without Figure 2, the reader cannot visualize the interaction matrices or the differences between scenarios.
- **Required correction** Ensure Figure 2 is included and referenced clearly in the final version, with a caption that explains the interaction patterns.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section 3.3 (exchange rate order parameter)
- **Evidence pointer** Section 3.3, Appendix B (referenced but not provided)
- **Issue** The exchange rate order parameter is mentioned but not defined in the main text. The reader is referred to Appendix B, which is not available in the supplied material.
- **Required correction** Provide a brief definition or description of the order parameter in the main text, or ensure Appendix B is included.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Section 4 (Conclusions)
- **Evidence pointer** Section 4
- **Issue** The conclusions mention biological examples (e.g., Embryo Defective 1579 condensates) but do not discuss potential limitations of the model in capturing real biological complexity, such as sequence-specific effects or the role of RNA.
- **Required correction** Add a brief discussion of model limitations and how the findings might translate to more complex biological systems.

## Risk / unsupported claims
- The claim that multilayered organization "maximizes the density of LLPS-stabilizing molecular interactions" is not directly quantified in the provided text; it is inferred from the observed architecture.
- The claim that surface tension reduction is a key driving force is supported by surface tension values but lacks direct causal testing.
- The generalizability of the findings to real biological condensates, which include RNA and sequence-specific interactions, is not established from the model alone.
- The stability of the two separate condensates in the non-competing scaffolds scenario is stated but not quantitatively demonstrated in the provided text.