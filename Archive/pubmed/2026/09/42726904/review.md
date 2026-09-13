## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors present a computational pipeline (LIR-DP) integrating sequence pattern matching, IUPred3 disorder prediction, and AlphaFold3 modeling to identify putative LC3-interacting region (LIR) motifs in proteins from highly virulent viruses (HVVs). They report 43 putative LIRs across 166 proteins from 22 HVVs, with 18 predicted functional. Experimental validation (in vitro and in cellulo) is claimed for LIRs from Marburg virus nucleoprotein, Nipah virus phosphoprotein, Ebola virus VP35, and Rift Valley fever virus NSs, with the aromatic residue at position one shown to be critical for binding.
- **Visible evidence base** Abstract text only; no experimental data, statistical analyses, sequence alignments, structural models, or validation details are available
- **Missing materials affecting confidence** Full methods, all figures and tables, experimental protocols, binding assay data, statistical details, AlphaFold3 modeling parameters, IUPred3 thresholds, and any negative or control results

## Reviewer
- **Overall assessment** The abstract describes a potentially useful integrative pipeline for identifying LIR motifs in viral proteins, addressing a genuine gap in the field. The combination of sequence pattern matching, disorder prediction, and structural modeling is logical, and the inclusion of experimental validation for selected candidates strengthens the premise. However, the abstract alone provides insufficient detail to assess the technical rigor, false-positive rates, or biological significance of the findings. The claim that 18 of 43 LIRs would be functional is not supported by any visible evidence, and the experimental validation appears limited to four candidates. The broader utility of the pipeline for understanding viral modulation of autophagy is plausible but not established from the supplied material.
- **Who would be interested in the results, and why** Virologists studying host-pathogen interactions, particularly those focused on hemorrhagic fever viruses and Nipah virus; autophagy researchers interested in LIR motif biology and Atg8/LC3 family interactions; computational biologists developing SLiM prediction tools; and researchers working on antiviral therapeutic targets involving host autophagy pathways.
- **Major strengths** The abstract addresses a clear gap in the field, as functional LIR motifs in viral proteins remain under-characterized. The pipeline integrates complementary computational approaches (sequence, disorder, structure) which is methodologically sensible. The inclusion of experimental validation for multiple viral proteins across different virus families adds credibility. The identification of the aromatic residue at position one as critical for binding provides mechanistic insight.
- **Major Concerns** None identified from the supplied material beyond those listed below, given the abstract-only scope.
- **Minor Comments** None identified from the supplied material beyond those listed below, given the abstract-only scope.
- **Technical failings that need to be addressed before the case is established** The abstract does not provide sufficient evidence to evaluate the pipeline's sensitivity, specificity, or false-discovery rate. The prediction of 18 functional LIRs out of 43 putative motifs is presented without any supporting metrics. The experimental validation is described only qualitatively, with no binding affinities, replicates, or statistical comparisons. The claim that the aromatic residue is critical is made without showing mutagenesis data or quantitative binding results.
- **Assessment against Nature-style criteria** Originality: moderate to high, as the integrative approach is novel in this specific application. Scientific importance: potentially high if the pipeline proves reliable, given the pandemic threat posed by HFVs and the under-explored role of viral LIRs in autophagy modulation. Interdisciplinary readership: the work bridges virology, cell biology, and computational biology, which could attract a broad audience. Technical soundness: not assessable from the abstract alone; the lack of methodological detail and validation metrics prevents evaluation. Readability for nonspecialists: the abstract is generally clear, though terms such as SLiM and IUPred3 may require familiarity with the field.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a promising approach and preliminary validation, but the absence of methods, data, and statistical details means the core claims cannot be evaluated. A full manuscript with comprehensive results would be required to assess whether the pipeline performs as claimed.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The pipeline identified 43 putative LIR motifs in 166 proteins from 22 HVVs and predicted that 18 of these LIRs would be functional.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract provides no information on how the 43 putative LIRs were scored, what thresholds were applied for IUPred3 disorder prediction, how AlphaFold3 models were used to filter candidates, or what criteria defined a "functional" prediction. The ratio of 18 functional out of 43 putative motifs implies a predictive model, but no performance metrics (sensitivity, specificity, precision, recall) or validation against known LIRs are presented.
- **Why it matters** Without these details, the pipeline's reliability cannot be assessed. If the false-positive rate is high, the 43 putative LIRs may largely represent noise, undermining the central claim of the tool's utility. Conversely, if the threshold is overly stringent, the pipeline may miss true LIRs, limiting its practical value.
- **Resolution test** Provide a detailed description of the pipeline parameters, a benchmark against a curated set of known LIR motifs (positive and negative controls), and report precision-recall or ROC-type analyses. Show the distribution of scores for predicted functional versus non-functional LIRs.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** In vitro and in cellulo laboratory experiments demonstrated that LIRs from Marburg virus nucleoprotein, Nipah virus phosphoprotein, Ebola virus VP35, and Rift Valley fever virus NSs bind to Atg8/LC3 family proteins.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract states that binding was demonstrated but provides no experimental details. It is unclear which Atg8/LC3 family members were tested, what binding assays were used (e.g., pull-down, co-immunoprecipitation, surface plasmon resonance, isothermal titration calorimetry), what concentrations were used, or whether binding was quantified. No negative controls or specificity tests against non-LIR peptides are mentioned.
- **Why it matters** Binding claims require quantitative or at least semi-quantitative evidence to be convincing. Without knowing the assay type, affinity range, or specificity, the reader cannot determine whether the observed interactions are biologically meaningful or merely weak, non-specific associations common with short linear motifs.
- **Resolution test** Present representative binding data for each of the four LIRs, including dose-response curves or affinity measurements, appropriate negative controls (e.g., mutated LIRs or unrelated peptides), and statistical analysis comparing binding to controls.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The aromatic amino acid in the first position of each LIR motif was found to be critical for these interactions.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract asserts that the aromatic residue at position one is critical, but no mutagenesis data are shown. It is not stated whether single-point mutations were made, whether all four LIRs were tested, or what the magnitude of the effect was (complete loss versus partial reduction in binding).
- **Why it matters** This claim is mechanistically important because it suggests a conserved binding mode across diverse viral proteins. If the evidence is incomplete or the effect is modest, the conclusion may be overstated. The claim also implies a general principle that could guide future predictions, so it must be rigorously supported.
- **Resolution test** Provide mutagenesis data for all four validated LIRs, showing binding of wild-type versus aromatic-to-alanine (or equivalent) mutants, with quantitative readouts and statistical significance. Ideally, include a structural rationale from AlphaFold3 models showing the aromatic residue in the canonical LIR binding pocket of LC3.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Definition of HVV set
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract states that 166 proteins from 22 HVVs were analyzed but does not specify which viruses are included beyond the examples of Nipah virus and the hemorrhagic fever viruses mentioned.
- **Required correction** List the 22 viruses included in the analysis, either in the abstract or in a supplementary table, so readers can assess the breadth and relevance of the dataset.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Pipeline availability
- **Evidence pointer** Abstract, location not provided
- **Issue** The LIR-DP pipeline is described as newly developed, but no mention is made of code availability, web server access, or deposition of the pipeline scripts.
- **Required correction** State where the pipeline code or a web-based implementation can be accessed, or indicate that it will be made available upon publication, to facilitate adoption by other researchers.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Functional significance of predicted LIRs
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract suggests that the identified LIRs may play a role in hijacking or evading autophagy, but no functional assays (e.g., autophagy flux measurements, viral replication assays with LIR-mutant viruses) are described.
- **Required correction** Clarify whether functional validation in the context of viral infection is planned or included in the full manuscript, or temper the claim to reflect that the study identifies candidate motifs requiring further functional testing.

## Risk / unsupported claims
- The prediction that 18 of 43 LIRs would be functional is unsupported by any visible metrics or validation data.
- The claim that the aromatic residue at position one is critical for binding is unsupported without mutagenesis data.
- The statement that the pipeline provides "evidence for its utility" is not assessable from the abstract alone, as no benchmarking or comparison to existing LIR prediction tools is presented.
- The biological relevance of the identified LIRs for viral modulation of autophagy during infection is speculative, as no infection-based functional data are described.