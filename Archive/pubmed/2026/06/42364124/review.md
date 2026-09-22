## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no methods, figures, tables, or supplementary material were provided
- **Shared manuscript claim summary** The authors report that berberine and palmatine bind the SARS-CoV-2 nucleocapsid (N) protein via low-affinity, multivalent interactions, induce modest secondary and tertiary structural changes, and slightly increase thermal stability, while the protein retains nucleic acid binding and oligomeric assembly in the presence of the compounds.
- **Visible evidence base** Abstract text only; no experimental details, numerical data beyond those stated, or statistical analyses are available
- **Missing materials affecting confidence** Full methods, all figures and tables, raw biophysical data (CD, ITF, SPR, ITC, BN-PAGE), docking and cofolding outputs, statistical treatment, and any control experiments

## Reviewer
- **Overall assessment** The abstract presents a plausible biophysical characterization of two alkaloid ligands against a recombinant SARS-CoV-2 N protein construct. The topic is of interest to the structural virology and antiviral drug discovery communities. However, the abstract alone provides insufficient detail to evaluate the rigor of the experimental design, the quality of the biophysical data, or the strength of the conclusions. Several claims, particularly regarding multivalency, conformational modulation, and functional retention, are not adequately supported by the evidence summarized here. The manuscript may have merit, but the case is not established from the supplied material.
- **Who would be interested in the results, and why** Researchers studying SARS-CoV-2 nucleocapsid protein structure and function, investigators interested in intrinsically disordered proteins and their ligand interactions, and medicinal chemists exploring natural product modulators of viral proteins. The work could also be relevant to those developing biophysical assays for low-affinity protein-ligand interactions.
- **Major strengths** The study addresses a relevant and under-explored question regarding low-affinity modulators of an intrinsically disordered viral protein. The use of multiple complementary biophysical techniques (CD, ITF, SPR, ITC, BN-PAGE) is appropriate for characterizing protein-ligand interactions and conformational changes. The inclusion of both experimental and computational approaches (docking, Boltz-2 cofolding) is commendable.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** "Both alkaloids have low-affinity, multivalent interactions with the N protein as predicted by in silico docking and Boltz-2 cofolding predictions."
  - **Evidence pointer** Abstract; location not provided
  - **Concern** The claim of multivalent interactions is stated as predicted by computational methods, but the abstract does not describe any experimental validation of multivalency. SPR and ITC are mentioned, but no stoichiometry, binding site mapping, or mutation-based dissection is described. The term "multivalent" implies multiple simultaneous binding sites or modes, which requires experimental evidence beyond affinity measurements.
  - **Why it matters** Multivalency is a central mechanistic claim of the paper. If not experimentally substantiated, the conclusion that these alkaloids act via multivalent interactions is speculative and could mislead subsequent studies.
  - **Resolution test** Provide experimental evidence for binding stoichiometry (e.g., ITC n-values, SPR stoichiometry analysis) or site-directed mutagenesis of predicted binding pockets, or temper the claim to reflect computational prediction only.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** "Both compounds induce slight secondary and tertiary structural changes, including redistribution of secondary structural elements toward increased beta-sheet content, alterations in hydrogen-bonding patterns, and small shifts in intrinsic tryptophan fluorescence."
  - **Evidence pointer** Abstract; location not provided
  - **Concern** The abstract reports structural changes but provides no quantitative data, no spectra, and no statistical comparison to controls. The claim of "alterations in hydrogen-bonding patterns" is particularly strong and would require high-resolution structural data (e.g., NMR, crystallography) or at least detailed HDX-MS analysis, none of which are mentioned. CD and fluorescence can report on secondary and tertiary structure changes, but hydrogen-bonding pattern alterations are not directly measurable by these techniques.
  - **Why it matters** The structural modulation claim is a key conclusion of the study. Without adequate evidence, the interpretation that these compounds meaningfully alter the N protein conformational landscape is not supported.
  - **Resolution test** Provide representative spectra with appropriate controls, quantitative secondary structure deconvolution, and clarify how hydrogen-bonding patterns were inferred. If inferred from CD, state this explicitly and acknowledge the limitation.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** "The native, predominantly unstructured protein still binds nucleic acids and can form dimer, trimer and tetrameric species even in the presence of the compounds."
  - **Evidence pointer** Abstract; location not provided
  - **Concern** This claim implies functional and oligomeric integrity is retained in the presence of the alkaloids, but no data are shown. BN-PAGE is mentioned, but no quantitative comparison of oligomeric distributions with and without compounds is described. Nucleic acid binding is stated but no assay, affinity, or comparative data are provided.
  - **Why it matters** The retention of function in the presence of ligands is important for interpreting whether these compounds are modulators or merely non-specific binders. Without comparative data, the functional relevance of the interaction is unclear.
  - **Resolution test** Provide BN-PAGE data with and without compounds, and nucleic acid binding assays (e.g., electrophoretic mobility shift assay or fluorescence anisotropy) with appropriate controls and quantitative comparisons.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Internal consistency
  - **Claim pointer** "Changes result in a limited increase in thermal stability (0.08-0.1 degrees C)."
  - **Evidence pointer** Abstract; location not provided
  - **Concern** The reported thermal stability increase of 0.08-0.1 degrees C is extremely small and likely within experimental error for most thermal denaturation assays. The abstract does not report error bars, replicates, or statistical significance. This magnitude of change may not be biologically meaningful.
  - **Why it matters** If the thermal shift is not statistically significant, the claim of stabilization is unsupported and could be overinterpreted.
  - **Resolution test** Report the assay used (e.g., DSF, CD thermal melt), the number of replicates, standard deviations, and p-values. If the change is not significant, remove or reframe the claim.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Protein construct description
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The consensus sequence is described with mutations relative to the Wuhan sequence, but the rationale for choosing this particular consensus is not stated.
  - **Required correction** Briefly justify the use of this consensus sequence, or cite the source from which it was derived.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Binding affinity quantification
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The abstract states ITC "confirms the low binding affinity" but does not report the Kd value or thermodynamic parameters.
  - **Required correction** Include the measured Kd and, if available, enthalpy and entropy contributions to support the affinity claim.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Precision
  - **Affected element** Terminology
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The phrase "predominantly unstructured protein" is used, but the N protein is known to contain folded domains (N-terminal domain and C-terminal domain) connected by disordered regions. This oversimplification may mislead readers.
  - **Required correction** Use more precise language, such as "partially disordered" or "containing intrinsically disordered regions," to accurately describe the protein.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Computational methods
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The docking and Boltz-2 cofolding predictions are mentioned but no parameters, scoring functions, or validation are described.
  - **Required correction** Provide brief methodological details or refer to the methods section for reproducibility.
- **Technical failings that need to be addressed before the case is established** R1-M1 (multivalency not experimentally validated), R1-M2 (structural changes not quantitatively supported), R1-M3 (functional retention not demonstrated with comparative data), R1-M4 (thermal stability change likely within error)
- **Assessment against Nature-style criteria**  
  *Originality*: Moderate. The application of known alkaloids to a viral protein is not entirely novel, but the focus on low-affinity multivalent interactions with an intrinsically disordered protein is a relatively underexplored angle.  
  *Scientific importance*: Moderate. The findings could inform understanding of ligand interactions with disordered viral proteins, but the clinical or translational significance of low-affinity binding with minimal thermal stabilization is unclear.  
  *Interdisciplinary readership*: Limited. The work is primarily of interest to biophysicists and structural virologists; the broader readership appeal is modest.  
  *Technical soundness*: Not assessable from the abstract. The techniques are appropriate, but the absence of data, controls, and statistical analysis prevents evaluation.  
  *Readability for nonspecialists*: The abstract is reasonably clear but uses specialized terminology without sufficient context for a general scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract describes a plausible study, but the key mechanistic claims require experimental substantiation that is not visible in the supplied material. A full manuscript with complete data may change this assessment.

## Risk / unsupported claims
- Multivalent interactions are claimed but only computationally predicted; no experimental stoichiometry or binding site evidence is provided.
- "Alterations in hydrogen-bonding patterns" is stated without any method capable of directly measuring this.
- The thermal stability increase of 0.08-0.1 degrees C is presented without error analysis or statistical significance.
- The retention of nucleic acid binding and oligomeric assembly in the presence of compounds is asserted without comparative data.
- The overall conclusion that these alkaloids "alter the N protein conformational landscape" is not supported by the limited quantitative information in the abstract.