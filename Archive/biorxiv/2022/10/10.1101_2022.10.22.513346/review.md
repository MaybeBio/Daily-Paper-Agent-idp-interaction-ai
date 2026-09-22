## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, figure legends, and supplemental figure legends
- **Assessment boundary** Scientific validity, technical soundness, and support of claims based solely on the provided manuscript text; no external data or unpublished materials were consulted
- **Shared manuscript claim summary** The authors propose that a linear N-terminal region of Arabidopsis AGO1, termed the N-coil, is preferentially accessible in the RNA-free state, serves as a direct binding site for the autophagy cargo receptor ATI1, and that mutation of this interaction site reduces the degradation rate of unloaded AGO1 in vivo. They further suggest this mechanism may be conserved in human Ago2 and other eukaryotic AGO proteins.
- **Visible evidence base** Abstract, introduction, results sections (narrative only, no figures or tables included in the provided text), discussion, materials and methods, supplemental figure legends, author contributions, data availability statement
- **Missing materials affecting confidence** All figures and tables (Figures 1-7, Figure S1-S5, Supplemental Tables 1-2) are referenced but not provided; raw data for MST, NMR, pulse-labeling, and immunoprecipitation experiments are not accessible; statistical analysis details and complete experimental parameters are not fully described

## Reviewer
- **Overall assessment** This manuscript addresses a significant and long-standing question in the small RNA field: how unloaded AGO proteins are specifically recognized for degradation. The authors present a compelling hypothesis centered on the N-coil region and provide multiple lines of evidence including antibody accessibility, hydrogen-deuterium exchange reanalysis, direct binding assays, and in vivo degradation kinetics. The conceptual advance is potentially important, and the interdisciplinary approach is commendable. However, the provided text lacks the actual data figures and tables, making it impossible to fully evaluate the technical rigor, statistical significance, and quantitative support for several key claims. The in vivo degradation effect appears modest, and the specificity of the N-coil antibody and the physiological relevance of the ATI1 interaction require closer scrutiny. The manuscript is well-written and logically structured, but the evidence base as presented is incomplete for a definitive assessment.
- **Who would be interested in the results, and why** Researchers studying small RNA pathways, AGO protein biology, RNA-induced silencing complex assembly, autophagy-mediated protein degradation, and plant-microbe interactions would find these results of interest. The potential conservation of the N-coil mechanism across eukaryotes, including humans, broadens the appeal to mammalian RNA interference and gene regulation communities. The study also contributes to understanding how conformational changes in multi-domain proteins create state-specific interaction surfaces, which is relevant to structural biologists and biochemists studying protein dynamics.
- **Major strengths** The study addresses a fundamental and unresolved question in the field with a clear and testable hypothesis. The combination of antibody-based accessibility assays, reanalysis of published HDX data, direct binding measurements by MST, and in vivo degradation kinetics provides a multi-pronged approach. The identification of a specific, linear interaction motif (N-coil) that is conformationally regulated is conceptually elegant and provides a mechanistic framework for future studies. The use of a genetically defined unloaded AGO1 mutant (Y691E) is a thoughtful experimental strategy. The discussion of potential conservation across Piwi-clade proteins and the distinction from prokaryotic AGOs adds valuable perspective.
- **Major Concerns** The most significant concern is the absence of all primary data figures and tables in the provided material, which prevents verification of the quantitative claims, statistical analyses, and experimental quality. The in vivo degradation rate reduction for the KKME mutant appears modest and variable between experiments, raising questions about biological significance. The specificity of the N-coil antibody for the unloaded state is inferred from binding experiments, but the possibility of epitope masking by other factors in the loaded state is not fully excluded. The physiological relevance of the ATI1 interaction for AGO1 degradation in planta is supported by correlation but not by loss-of-function genetics. The HDX data reanalysis is based on published data from a different organism and experimental system, and the interpretation of differential flexibility as evidence for accessibility changes requires careful validation. The claim that the N-coil is "uniquely" accessible in the unloaded state is strong and may not be fully supported by the data presented.
- **Minor Comments** The manuscript would benefit from clearer presentation of the statistical methods used for curve fitting and comparison of degradation rates. The choice of the Y691E mutant as a model for unloaded AGO1 should be justified more thoroughly, particularly regarding potential conformational effects beyond loss of small RNA binding. The discussion of the N-coil in Piwi-clade proteins is speculative and could be more clearly framed as such. The methods section for MST and NMR would benefit from additional experimental details, such as protein concentrations, buffer conditions, and data analysis parameters. The supplemental figure legends are brief and do not fully describe the experimental design or controls.
- **Technical failings that need to be addressed before the case is established** The lack of accessible primary data is a critical failing in the provided material. Specifically, the quantitative MST binding data, the NMR titration spectra, the pulse-labeling kinetics with appropriate replicates and statistical analysis, and the antibody accessibility controls are all referenced but not shown. Without these, the central claims of direct N-coil-ATI1 interaction and reduced degradation rate cannot be fully evaluated. The reanalysis of HDX data requires the original dataset and clear methodology for determining significance of differential exchange.
- **Assessment against Nature-style criteria** Originality: The study presents a novel concept of a state-specific linear motif in AGO proteins that distinguishes loaded from unloaded forms. This is a fresh perspective on a well-studied problem and offers a new mechanistic entry point. Scientific importance: The question of how unloaded AGO is recognized for degradation is fundamental to understanding small RNA pathway homeostasis and has implications for diseases where AGO stability is dysregulated. The potential conservation across eukaryotes elevates the importance. Interdisciplinary readership: The work bridges plant molecular biology, protein biochemistry, structural biology, and autophagy research, and would appeal to a broad readership in these areas. Technical soundness: The experimental approaches are appropriate and state-of-the-art, but the incomplete presentation of data prevents full assessment of technical rigor. Readability for nonspecialists: The manuscript is clearly written and the logic is easy to follow, though some sections assume familiarity with AGO biology and biophysical methods.
- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual advance is significant and the experimental strategy is sound, but the evidence base provided is incomplete. Full evaluation requires access to the primary data, particularly the quantitative binding and degradation kinetics, and clarification of the specificity and physiological relevance of the ATI1 interaction. If the data support the claims as stated, this would be a valuable contribution to the field.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The authors claim that the N-coil is preferentially accessible in the unloaded state of AGO1, supported by antibody binding and HDX data.
- **Evidence pointer** Results sections "The N-coil is uniquely accessible in unloaded AGO1" and "The N-coil-Piwi interface of human Ago2 exhibits reduced solvent exposure upon small RNA binding"; Figures 3 and 3E; location not provided
- **Concern** The primary data for the antibody accessibility experiments and the HDX reanalysis are not included in the provided material. The antibody binding experiments are described as showing a 10-fold difference in recovery between loaded and unloaded AGO1, but the actual blots, quantification, and controls are not shown. Similarly, the HDX reanalysis relies on published data, and the methodology for determining significant differences in exchange rates is not described. Without these data, the central claim of state-dependent N-coil accessibility cannot be verified.
- **Why it matters** This is the foundational observation of the paper. If the accessibility difference is not robust or is confounded by experimental artifacts, the entire model is undermined.
- **Resolution test** Provide the full antibody binding data including representative blots, quantification with replicates, and appropriate controls (e.g., pre-immune serum, peptide competition). For HDX, provide the methodology for data processing and statistical comparison, and show the differential uptake plots for the N-coil and interacting Piwi residues.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative binding evidence
- **Claim pointer** The authors claim a direct interaction between the N-coil of AGO1 and the IDR of ATI1 with a Kd of 11±2 µM, and that the K178E mutation reduces this affinity.
- **Evidence pointer** Results section "The interaction between ATI1 and the N-domain is direct and involves the N-coil"; Figure 4B-C; location not provided
- **Concern** The MST data are described but not shown. The Kd value of 11±2 µM is reported, but the binding curves, the concentration range of the titrated partner, and the number of replicates are not provided. The K178E mutant is reported to have a Kd of 47±12 µM, but again the data are absent. The claim that the interaction is "direct" requires demonstration of a specific, saturable binding interaction, which cannot be assessed without the raw data.
- **Why it matters** The direct interaction between the N-coil and ATI1 is a key mechanistic claim. A weak or non-specific interaction would not support the proposed model of selective recognition.
- **Resolution test** Provide the MST binding curves for both wild-type and K178E mutant, including the concentration ranges, the number of independent experiments, and the fitting parameters. Show that the interaction is saturable and specific, and that the K178E mutation specifically affects the binding affinity.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** In vivo functional relevance
- **Claim pointer** The authors claim that mutation of N-coil residues required for ATI1 interaction reduces the degradation rate of unloaded AGO1 in vivo.
- **Evidence pointer** Results section "Defective ATI1 interaction sites in NcGN AGO1 reduce the degradation rate of unloaded AGO1"; Figure 6B-D; Figure S5; location not provided
- **Concern** The pulse-labeling data are described as showing a "modest, but reproducible reduction" in degradation rate for the KKME mutant compared to Y691E alone. However, the actual data are not shown. The magnitude of the effect, the statistical significance, and the variability between experiments are not presented. The claim that this effect is due specifically to loss of ATI1 interaction is not directly tested, as no ATI1 loss-of-function mutant or ATI1 overexpression experiment is described.
- **Why it matters** The in vivo degradation data are the most direct evidence for the functional relevance of the N-coil-ATI1 interaction. A modest effect that is not statistically robust would weaken the conclusion that this interaction is a major determinant of unloaded AGO1 turnover.
- **Resolution test** Provide the pulse-labeling data with representative blots, quantification from at least three independent experiments, and statistical analysis. Show that the KKME mutation specifically affects the degradation rate of the unloaded form and not the loaded form. Ideally, include genetic evidence (e.g., ati1 mutant) to support the specificity of the effect.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Specificity of antibody recognition
- **Claim pointer** The authors claim that the N-coil antibody recognizes the N-coil specifically and that its binding is enhanced in the unloaded state.
- **Evidence pointer** Results section "The N-coil is uniquely accessible in unloaded AGO1"; Figure 3A-D; location not provided
- **Concern** The specificity of the antibody is demonstrated by loss of reactivity with a K185E/K190E mutant, but the possibility of off-target effects or partial epitope recognition is not fully excluded. The antibody was raised against a 16-aa peptide, and the accessibility difference could be influenced by the antibody's affinity or by steric effects from the small RNA or other bound factors. The claim that the N-coil is "uniquely" accessible is strong and may require additional controls, such as competition with the free peptide or testing of additional N-coil mutants.
- **Why it matters** The antibody is a key tool for assessing N-coil accessibility. If the antibody binding is not truly specific or if the accessibility difference is due to other factors, the interpretation of the results would be compromised.
- **Resolution test** Provide additional controls for antibody specificity, such as peptide competition assays, testing of multiple N-coil mutants, and verification that the antibody does not cross-react with other AGO proteins. Consider using an orthogonal method, such as limited proteolysis or chemical labeling, to confirm the accessibility difference.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Pulse-labeling and MST data
- **Evidence pointer** Methods sections "Microscale thermophoresis (MST)" and "Pulse labeling"; location not provided
- **Issue** The statistical methods for comparing degradation rates and binding affinities are not described in detail. The number of replicates, the error bars, and the statistical tests used are not specified.
- **Required correction** Provide a clear description of the statistical analysis for all quantitative data, including the number of independent experiments, the type of error bars shown, and the statistical tests used to determine significance.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Justification of Y691E mutant
- **Affected element** Results section "The AGO1 Y691E protein mutated in the 5'-phosphate binding pocket is unloaded"
- **Evidence pointer** Figure 2A-B; location not provided
- **Concern** The Y691E mutation is used as a model for unloaded AGO1, but the potential effects of this mutation on protein folding or stability beyond loss of small RNA binding are not discussed. The authors state that the mutant is "unloaded" based on lack of small RNA co-purification, but this does not exclude other conformational changes.
- **Required correction** Discuss the potential limitations of using the Y691E mutant as a model for the unloaded state and consider additional characterization, such as circular dichroism or limited proteolysis, to confirm that the mutant is properly folded.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Conservation claims
- **Affected element** Discussion section "An N-coil in Piwi-clade proteins, but not in prokaryotic Ago proteins"
- **Evidence pointer** Figure 7A-D; location not provided
- **Issue** The claim that the N-coil mechanism may apply to Piwi-clade proteins is based on structural comparisons, but no functional data are presented to support this. The discussion is speculative and could be more clearly framed as a hypothesis.
- **Required correction** Clearly distinguish between structural observations and functional hypotheses in the discussion. Consider adding a statement that functional validation in Piwi-clade proteins is needed.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data and code availability statement
- **Evidence pointer** "Data and code availability" section; location not provided
- **Issue** The data availability statement mentions NMR data deposition but does not mention the availability of other datasets, such as the HDX data or the raw MST and pulse-labeling data.
- **Required correction** Provide a comprehensive data availability statement that includes all datasets generated and analyzed in the study, with appropriate accession numbers or repositories.

## Risk / unsupported claims
- The claim that the N-coil is "uniquely" accessible in the unloaded state is not fully supported by the provided evidence, as the antibody and HDX data are not shown.
- The claim that the N-coil-ATI1 interaction is the primary determinant of unloaded AGO1 degradation is not directly tested, as no loss-of-function or gain-of-function experiments for ATI1 are described.
- The claim that the N-coil mechanism is conserved across eukaryotic AGO proteins, including Piwi-clade proteins, is speculative and based on limited structural comparisons.
- The quantitative Kd values for the N-coil-ATI1 interaction are reported but cannot be verified without the MST data.
- The in vivo degradation rate reduction for the KKME mutant is described as "modest" and the biological significance is not fully established without the underlying data.