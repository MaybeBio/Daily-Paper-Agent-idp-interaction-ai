## Review setup
- **Input scope** Full manuscript text (abstract and main text, excluding supplementary information)
- **Assessment boundary** Claims, evidence, and conclusions as presented in the provided text
- **Shared manuscript claim summary** The authors propose that biomolecular condensates alter the folding landscape of protein alpha-helices through a balance of multivalent interactions (unfolding) and crowding (folding), and that these effects are sequence-dependent and kinetically frustrated due to coupling with co-condensate protein dynamics.
- **Visible evidence base** Atomistic simulations, Bayesian optimization for a residue-resolution model, characterization of helices from TDP-43, Annexin A11, and Androgen Receptor in condensates of varying physicochemical properties
- **Missing materials affecting confidence** No supplementary information, figures, tables, or detailed methods are provided. The manuscript lacks quantitative data (e.g., free energy differences, kinetic rates, simulation parameters) and experimental validation. The Bayesian optimization model is mentioned but not described in sufficient detail to assess its validity.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question about how biomolecular condensates influence protein folding, using alpha-helices as a model system. The conceptual framework—balancing multivalent interactions and crowding—is plausible and interesting. However, the evidence presented in the abstract and main text is insufficient to support the strong claims made. The lack of quantitative data, detailed methods, and experimental validation severely limits the ability to evaluate the work. The manuscript would benefit from a more rigorous presentation of simulation results, model validation, and a clearer link to biological relevance.
- **Who would be interested in the results, and why** Researchers in biophysics, protein folding, phase separation, and cell biology would be interested. The work has potential implications for understanding condensate-mediated proteinopathies (e.g., neurodegenerative diseases) and for designing condensates to control protein function. The conceptual framework could inspire further studies on how cellular environments modulate protein structure.
- **Major strengths** 1. The question is fundamental and timely, addressing a gap in understanding how condensates affect protein structure. 2. The proposed balance between multivalent interactions (unfolding) and crowding (folding) is a clear and testable hypothesis. 3. The use of Bayesian optimization to develop a residue-resolution model is a novel methodological approach. 4. The focus on disease-associated proteins (TDP-43, Annexin A11, Androgen Receptor) adds biological relevance.
- **Major Concerns**  
  - **Concern ID** R1-M1  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Evidence sufficiency  
  - **Claim pointer** "Atomistic simulations suggest the helix-coil transition within condensates differs markedly from its behavior in dilute solution or in the presence of inert crowders."  
  - **Evidence pointer** Location not provided (abstract only)  
  - **Concern** The claim is based on "atomistic simulations," but no details are given about the simulation system (e.g., force field, condensate composition, simulation length, sampling method). Without these details, it is impossible to assess whether the simulations are reliable or whether the observed differences are statistically significant.  
  - **Why it matters** This claim is foundational to the entire study. If the simulations are not robust, the subsequent model and conclusions are undermined.  
  - **Resolution test** Provide a detailed description of the simulation setup, including system size, force field, equilibration protocol, and error analysis. Show quantitative data (e.g., free energy profiles, helix content as a function of condensate composition) with error bars.  

  - **Concern ID** R1-M2  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Model validation  
  - **Claim pointer** "We then use Bayesian optimization to develop a chemically specific, residue-resolution model for quantification of alpha-helical folding and apply it to characterize diverse helices... within condensates of varying physicochemical properties."  
  - **Evidence pointer** Location not provided  
  - **Concern** The Bayesian optimization model is described only in passing. No details are given about the training data, the features used, the optimization procedure, or the validation metrics. It is unclear whether the model is accurate, transferable, or overfitted.  
  - **Why it matters** The model is central to the quantitative analysis. Without validation, the predictions for helices in condensates are unsubstantiated.  
  - **Resolution test** Provide a full description of the model, including training data (e.g., from simulations or experiments), cross-validation results, and a comparison to experimental or known folding data. Show that the model can reproduce known helix-coil transitions in dilute solution.  

  - **Concern ID** R1-M3  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Experimental validation  
  - **Claim pointer** "Our results support a framework in which multivalent interactions drive unfolding while crowding promotes folding, and alpha-helix conformational ensembles inside condensates emerge from this balance."  
  - **Evidence pointer** Location not provided  
  - **Concern** The entire study appears to be based on simulations and a computational model. No experimental data (e.g., circular dichroism, NMR, or single-molecule FRET) are presented to validate the predictions. The claim that condensates dictate folding landscapes is strong and requires experimental corroboration.  
  - **Why it matters** Without experimental validation, the biological relevance of the findings remains speculative. The field of condensate biology is rapidly evolving, and computational predictions alone are insufficient to establish a new framework.  
  - **Resolution test** Include experimental measurements of alpha-helix folding in condensates (e.g., using model peptides or proteins) to confirm the predicted balance between unfolding and crowding. Alternatively, provide a clear plan for such experiments.  

  - **Concern ID** R1-M4  
  - **Severity** Major  
  - **Blocking** No  
  - **Axis** Kinetic frustration claim  
  - **Claim pointer** "Helix folding transitions are kinetically frustrated inside condensates because they are coupled to the time scale of contact rearrangement with co-condensate proteins."  
  - **Evidence pointer** Location not provided  
  - **Concern** The claim about kinetic frustration is intriguing but unsupported. No data on time scales (e.g., from simulations or experiments) are presented to show that folding is slower or more heterogeneous in condensates. The coupling to "contact rearrangement" is not defined or quantified.  
  - **Why it matters** Kinetic effects are a key part of the proposed framework. Without evidence, this claim weakens the overall narrative.  
  - **Resolution test** Provide simulation or experimental data showing that folding rates in condensates are slower than in dilute solution, and that this correlates with the dynamics of co-condensate proteins. Define "contact rearrangement" and measure it.  

- **Minor Comments**  
  - **Concern ID** R1-m1  
  - **Severity** Minor  
  - **Axis** Clarity  
  - **Affected element** Abstract  
  - **Evidence pointer** Location not provided  
  - **Issue** The phrase "horizontal line dense macromolecular assemblies" appears to be a formatting error (likely a typo for "—dense macromolecular assemblies").  
  - **Required correction** Correct the typo to read "biomolecular condensates—dense macromolecular assemblies."  

  - **Concern ID** R1-m2  
  - **Severity** Minor  
  - **Axis** Readability  
  - **Affected element** Abstract  
  - **Evidence pointer** Location not provided  
  - **Issue** The term "dually sequence-dependent" is ambiguous. It is not clear whether this means dependence on both the helix sequence and the co-condensate protein sequence, or something else.  
  - **Required correction** Clarify the meaning, e.g., "alpha-helix folding landscapes within condensates are dependent on both the sequence of the alpha-helical domain and the sequence of co-condensate proteins."  

  - **Concern ID** R1-m3  
  - **Severity** Minor  
  - **Axis** Completeness  
  - **Affected element** Abstract  
  - **Evidence pointer** Location not provided  
  - **Issue** The abstract mentions "diverse helices" but only lists three proteins (TDP-43, Annexin A11, Androgen Receptor). It is unclear how many helices were studied and whether they are representative.  
  - **Required correction** Specify the number and diversity of helices studied, or clarify that these are examples.  

- **Technical failings that need to be addressed before the case is established** R1-M1 (simulation details), R1-M2 (model validation), R1-M3 (experimental validation), R1-M4 (kinetic data). These concerns collectively indicate that the current evidence is insufficient to support the central claims.

- **Assessment against Nature-style criteria**  
  - **Originality**: The concept of condensates dictating protein folding landscapes is novel and addresses a gap in the field. However, the idea of a balance between crowding and interactions is not entirely new (e.g., studies on macromolecular crowding).  
  - **Scientific importance**: If validated, the work could have significant implications for understanding proteinopathies and designing condensates. However, the current lack of evidence limits its impact.  
  - **Interdisciplinary readership**: The topic is relevant to biophysics, cell biology, and biochemistry, but the abstract is accessible to a broad audience.  
  - **Technical soundness**: The technical foundation is weak due to missing details on simulations and model validation. The work is not technically sound as presented.  
  - **Readability for nonspecialists**: The abstract is clear and well-written, but the lack of quantitative data makes it difficult for nonspecialists to assess the strength of the claims.  
  Overall, the manuscript does not meet Nature-style criteria for publication in its current form due to insufficient evidence and technical validation.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript requires substantial additional data (simulation details, model validation, and experimental confirmation) before it can be considered for publication in a high-impact journal.

## Risk / unsupported claims
- The claim that "atomistic simulations suggest the helix-coil transition within condensates differs markedly" is unsupported without simulation details and quantitative results.
- The claim that the Bayesian optimization model is "chemically specific" and "residue-resolution" is unsupported without model description and validation.
- The claim that "multivalent interactions drive unfolding while crowding promotes folding" is a plausible hypothesis but is not quantitatively supported.
- The claim that "helix folding transitions are kinetically frustrated" is unsupported without kinetic data.
- The claim that the work has "implications for understanding condensate-mediated proteinopathies" is speculative without experimental evidence linking the findings to disease mechanisms.