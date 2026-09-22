## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) from bioRxiv preprint
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text; no supplementary figures or raw data were available for independent verification
- **Shared manuscript claim summary** The authors characterize the molecular architecture of the mouse REC114-MEI4-IHO1 complex, proposing specific stoichiometries (REC114-MEI4 2:1 and 4:2; IHO1 tetramer), identifying interaction interfaces via AlphaFold2 and mutagenesis, and demonstrating that IHO1, ANKRD31, and TOPOVIBL bind competitively to the REC114 PH domain
- **Visible evidence base** Results sections describing SEC-MALLS, native MS, AUC, pull-down assays, ITC, and AlphaFold2 predictions; figures referenced but not provided in the submitted text
- **Missing materials affecting confidence** Figures and supplementary figures (referenced as Fig. 1-7, Supplementary Fig. 1-13) were not included; raw SEC-MALLS, MS, AUC, and ITC data not available; experimental replicates and statistical analyses not described; full methods details for AlphaFold2 modeling not provided

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question in meiosis research: the molecular organization of the REC114-MEI4-IHO1 complex that regulates meiotic DNA double-strand break formation. The authors combine biochemical and biophysical approaches with AlphaFold2 modeling to propose a structural framework for this complex. The work is potentially valuable, as it provides the first detailed molecular characterization of these interactions in mouse. However, the manuscript has several significant limitations. The absence of figures and raw data prevents full evaluation of the claims. The proposed stoichiometries are based on solution measurements that show heterogeneity and fast exchange, making definitive conclusions difficult. The AlphaFold2 models, while useful for hypothesis generation, are not validated by high-resolution structures. The functional significance of the proposed complex and the competitive binding model, while intriguing, is not directly tested. The claim of a "ternary IHO1-REC114-MEI4 complex" is supported by co-elution experiments, but the affinity measurements (Kd ~30 µM) suggest a weak interaction that may not be physiologically relevant without additional stabilizing factors. Overall, the work represents a solid biochemical characterization but falls short of providing definitive structural or functional insights.

- **Who would be interested in the results, and why** Meiosis researchers, particularly those studying the regulation of programmed DNA double-strand breaks and chromosome dynamics. Structural biologists interested in protein-protein interactions in meiotic recombination. Evolutionary biologists studying conservation of meiotic machinery across species. The findings on competitive binding of IHO1, ANKRD31, and TOPOVIBL to REC114 could inform models of how meiotic DSB formation is regulated spatially and temporally.

- **Major strengths** 
  1. The study addresses a significant gap in understanding the molecular architecture of the pre-DSB recombinosome, a complex central to meiotic recombination.
  2. The combination of multiple biophysical techniques (SEC-MALLS, native MS, AUC, ITC) provides complementary evidence for the proposed stoichiometries and interactions.
  3. The use of AlphaFold2 to guide mutagenesis experiments is a modern and effective approach, and the validation of predicted interface residues by functional assays strengthens the conclusions.
  4. The demonstration that IHO1, ANKRD31, and TOPOVIBL share a binding site on REC114 PH domain, with mutually exclusive binding, provides a potential mechanistic basis for the regulation of DSB formation.
  5. The evolutionary perspective, showing conservation of interaction interfaces across species, adds breadth to the findings.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency for stoichiometry claims
- **Claim pointer** The authors claim that REC114 and MEI4 form predominantly a 2:1 complex that can dimerize to 4:2, and that IHO1 forms tetramers.
- **Evidence pointer** Results sections "Characterization of the REC114-MEI4 complex" and "IHO1 tetramerizes via a four-stranded coiled-coil"; Figures 1d-f, 3a-b, 4b (figures not provided)
- **Concern** The stoichiometry determinations rely on SEC-MALLS and native MS, but the authors acknowledge that the observed molecular weights are unstable and represent mixtures of different oligomeric states. The AUC data show fast exchange between 2:1 and 4:2 states, making the assignment of a "predominant" stoichiometry questionable. For IHO1, the tetramer assignment is based on MALLS measurements of fragments, but the full-length protein could not be studied. The possibility of concentration-dependent artifacts or non-specific aggregation is not fully addressed.
- **Why it matters** The proposed stoichiometries are central to the model of the pre-DSB recombinosome architecture. If the stoichiometry assignments are incorrect or represent only one of several possible states, the proposed model of the complex (4 IHO1:4 REC114:2 MEI4) would be unsupported. This affects the interpretation of how the complex functions in DSB formation.
- **Resolution test** Provide additional biophysical characterization, such as sedimentation equilibrium AUC at multiple concentrations to determine true solution stoichiometry, or cross-linking mass spectrometry to define the oligomeric states in a more definitive manner. For IHO1, attempts to study the full-length protein or a larger fragment that includes the tetramerization domain should be made. Clear presentation of the raw data and error analysis for all stoichiometry determinations is essential.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Functional relevance of the proposed complex
- **Claim pointer** The authors state that their results "provide strong evidence for the existence of a ternary IHO1-REC114-MEI4 complex" and that REC114 is "a potential regulatory platform mediating mutually exclusive interactions with several partners."
- **Evidence pointer** Results sections "IHO1 binds to the REC114 PH domain with its conserved N-terminus" and "IHO1, ANKRD11 and TOPOVIBL bind to the same REC114 surface"; Figures 5-6 (figures not provided)
- **Concern** The functional significance of the proposed ternary complex is not directly tested. The Kd of ~30 µM for the IHO1-REC114 interaction is relatively weak, and the authors do not address whether this affinity is sufficient for complex formation under physiological conditions. The competitive binding experiments are performed with purified fragments, not full-length proteins, and the physiological relevance of the competition is not established. The authors do not test whether mutations that disrupt the IHO1-REC114 interaction affect DSB formation in vivo.
- **Why it matters** The manuscript's central claim is that these interactions are important for meiotic DSB formation. Without functional validation, the biochemical observations remain descriptive. The weak affinity raises questions about whether the ternary complex forms in vivo, especially given that other factors (e.g., post-translational modifications, DNA, chromatin context) may be required.
- **Resolution test** Perform in vivo experiments, such as co-immunoprecipitation of endogenous proteins from meiotic cells, or complementation assays in mice or cell lines with mutations in the identified interface residues. Alternatively, use a more physiologically relevant in vitro system (e.g., with full-length proteins, or in the presence of DNA or chromatin) to demonstrate complex formation under conditions that better mimic the cellular environment.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** AlphaFold2 model reliability
- **Claim pointer** The authors use AlphaFold2 to predict the structures of the REC114-MEI4 complex, REC114 dimer, and IHO1 tetramer, and use these models to guide mutagenesis.
- **Evidence pointer** Results sections "REC114-MEI4 complex structure prediction" and "IHO1 tetramerizes via a four-stranded coiled-coil"; Figures 2, 3c-f, 4c (figures not provided)
- **Concern** The AlphaFold2 models are presented as supporting evidence, but the confidence metrics are not fully described. For the REC114-MEI4 complex, the model is described as "very convincing," but the authors do not provide pLDDT scores or predicted aligned error (PAE) plots for the reader to assess. For the IHO1 tetramer, the prediction is described as "less convincing" after residue 245, yet the tetramerization domain is mapped to residues 130-245. The low-confidence prediction for the IHO1-REC114 complex is acknowledged, but the model is still used to guide mutagenesis. The authors do not discuss the limitations of AlphaFold2 for predicting interactions between flexible or disordered regions.
- **Why it matters** The AlphaFold2 models are used to rationalize the mutagenesis results and to propose the architecture of the complex. If the models are unreliable, the interpretation of the mutagenesis data could be incorrect, and the proposed model of the complex would be weakened.
- **Resolution test** Provide detailed confidence metrics for all AlphaFold2 models, including pLDDT and PAE plots. For the IHO1-REC114 complex, consider using alternative prediction methods or experimental validation (e.g., cross-linking, HDX-MS) to confirm the interaction interface. Clearly state the limitations of the models and avoid over-interpreting low-confidence predictions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Completeness of interaction analysis
- **Claim pointer** The authors conclude that IHO1, ANKRD31, and TOPOVIBL bind to the same surface of REC114 PH domain and that these interactions are mutually exclusive.
- **Evidence pointer** Results section "IHO1, ANKRD11 and TOPOVIBL bind to the same REC114 surface"; Figures 6d-f (figures not provided)
- **Concern** The competitive binding experiments are only performed pairwise (IHO1 vs. ANKRD31, IHO1 vs. TOPOVIBL). The authors do not test whether ANKRD31 and TOPOVIBL compete with each other, nor do they test whether all three can bind simultaneously under any conditions. The stoichiometry of the ternary complex (if it exists) is not defined. The authors also do not address whether the binding of these factors is regulated by post-translational modifications or other cellular cues.
- **Why it matters** The model of REC114 as a "regulatory platform" implies that the exchange of binding partners is a key regulatory mechanism. Without a more complete analysis of the competitive interactions, this model remains speculative. Understanding whether ANKRD31 and TOPOVIBL compete with each other is important for understanding how DSB formation is regulated.
- **Resolution test** Perform competition experiments with all pairwise combinations of IHO1, ANKRD31, and TOPOVIBL. Use a ternary complex assay (e.g., pull-down with all three proteins) to determine if simultaneous binding is possible. Investigate whether phosphorylation or other modifications affect the binding affinities or competition.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Results section "Characterization of the REC114-MEI4 complex"
- **Evidence pointer** Figure 1 (not provided)
- **Issue** The description of the SEC-MALLS data is difficult to follow without the figure. The authors mention "two major peaks" and a "wider peak shoulder" but do not clearly describe the elution profile or how the molecular weights were calculated for each peak. The relationship between the peaks and the proposed 2:1 and 4:2 complexes is not explicitly stated.
- **Required correction** Provide a clearer description of the SEC-MALLS data, including the elution volumes, calculated molecular weights for each peak, and how these correspond to the proposed stoichiometries. Consider including a table summarizing the measured and theoretical molecular weights.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Methods section "Isothermal Titration Calorimetry (ITC)"
- **Evidence pointer** Methods section, ITC paragraph
- **Issue** The ITC methods describe the experimental setup but do not provide details on the fitting model used, the stoichiometry (n) obtained from the fits, or the thermodynamic parameters (ΔH, ΔS) beyond the Kd values. The authors also do not state how many replicates were performed or how errors were calculated.
- **Required correction** Provide complete ITC fitting parameters, including stoichiometry and thermodynamic values, and state the number of replicates and error analysis. This is important for assessing the reliability of the reported Kd values.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of competition experiments
- **Affected element** Results section "IHO1, ANKRD11 and TOPOVIBL bind to the same REC114 surface"
- **Evidence pointer** Figure 6g-i (not provided)
- **Issue** The gel filtration competition experiment with ANKRD31 shows that IHO1 does not bind REC114-MEI4 in the presence of ANKRD31. However, the authors do not discuss whether this is due to direct competition for the same binding site or to steric hindrance or conformational changes. The experiment with TOPOVIBL is described as "less interpretable" due to overlapping peaks, but the authors still conclude that binding is incompatible.
- **Required correction** Acknowledge the limitations of the competition experiments and discuss alternative explanations for the observed results. For the TOPOVIBL experiment, either provide a more quantitative analysis or temper the conclusion.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of physiological relevance
- **Affected element** Discussion section
- **Evidence pointer** Discussion, paragraphs on complex formation and regulation
- **Issue** The discussion speculates about the physiological relevance of the proposed complex and the competitive binding model but does not adequately address the weak affinity of the IHO1-REC114 interaction or the lack of in vivo validation. The authors also do not discuss how their findings relate to the known functions of these proteins in DSB formation.
- **Required correction** Add a more balanced discussion of the limitations of the study, including the weak affinity and lack of functional data. Discuss how the proposed model could be tested in future studies and how it relates to existing knowledge of meiotic DSB regulation.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure quality and accessibility
- **Affected element** All figures
- **Evidence pointer** Figures 1-7 (not provided)
- **Issue** The figures are not included in the submitted text, making it impossible to assess the quality of the data presentation. Based on the text descriptions, some figures appear to be complex (e.g., Figure 6 with multiple panels) and may be difficult to interpret.
- **Required correction** Ensure that all figures are clearly labeled, with appropriate annotations and legends that allow readers to understand the data without referring to the text. Consider simplifying complex figures or providing additional explanatory panels.

## Risk / unsupported claims
- The claim of a "ternary IHO1-REC114-MEI4 complex" is supported by co-elution experiments, but the stoichiometry of this complex is not definitively established. The proposed 4:4:2 stoichiometry is speculative and not directly measured.
- The statement that REC114 is "a potential regulatory platform mediating mutually exclusive interactions with several partners" is an interpretation based on in vitro binding data. The physiological relevance of this competitive binding is not demonstrated.
- The claim that the AlphaFold2 model of the REC114-MEI4 complex is "very convincing" is not supported by the provided data, as confidence metrics are not shown.
- The conclusion that IHO1 binding to REC114 is incompatible with TOPOVIBL binding is based on an experiment described as "less interpretable" by the authors themselves.
- The evolutionary conservation of the interaction interfaces is claimed based on AlphaFold2 predictions for other species, but these predictions are not experimentally validated.
- The functional significance of the identified interaction interfaces is not tested in vivo, so any claims about the role of these interactions in DSB formation are unsupported.