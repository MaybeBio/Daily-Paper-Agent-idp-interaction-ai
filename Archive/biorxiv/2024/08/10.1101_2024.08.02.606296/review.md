## Review setup
- **Input scope** Full manuscript text, figure legends, and supplementary figure legends
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and structural predictions as presented
- **Shared manuscript claim summary** The authors propose that the ULK1–ATG13–FIP200 complex is organized by three direct binary interactions, mediated by specific residues predicted by AlphaFold2, and that these interactions are additively important for autophagic flux in mammalian cells
- **Visible evidence base** AlphaFold2 structural predictions, ITC binding assays, in vitro pull-down assays, co-immunoprecipitation experiments, Halo-LC3 processing assays, immunostaining, and knock-in cell line analyses
- **Missing materials affecting confidence** Primary data for several key figures (Figures 1D-F, 2C-E, 3C-I, 4C-E) are not shown in the provided text; exact quantification methods and statistical details for several assays are not fully described; raw images and uncropped blots are not available for assessment

## Reviewer
- **Overall assessment** This manuscript presents a structurally informed analysis of the ULK1–ATG13–FIP200 complex assembly, using AlphaFold2 predictions to guide mutagenesis and functional validation. The work addresses an important gap in the autophagy field, as the molecular architecture of the mammalian ULK complex has remained poorly defined. The combination of computational prediction with in vitro and in vivo validation is commendable. However, the manuscript has several limitations that need to be addressed. The AlphaFold2 predictions, while valuable for hypothesis generation, are not confirmed by high-resolution experimental structures. The functional assays rely heavily on overexpression systems and knock-in cell lines where the quantitative effects are modest. The claim that the triad interaction is "required" for ULK complex formation and autophagy is not fully supported by the data, which show partial rather than complete abrogation of function upon mutation. The manuscript would benefit from clearer presentation of quantitative data and a more nuanced interpretation of the results.

- **Who would be interested in the results, and why** Researchers in the autophagy field, particularly those studying the ULK complex and its regulation, would be the primary audience. Structural biologists interested in protein-protein interactions within autophagy signaling complexes would also find this work relevant. Additionally, investigators studying the evolution of autophagy machinery across species, and those interested in the application of AlphaFold2 for predicting complex assemblies, would find value in this manuscript. The work has potential implications for understanding how autophagy initiation is regulated in physiological and pathological contexts.

- **Major strengths** The manuscript addresses a significant gap in understanding the molecular architecture of the ULK complex. The use of AlphaFold2 to generate testable predictions is timely and demonstrates the utility of computational approaches in structural biology. The combination of in vitro binding assays, cell-based co-immunoprecipitation, and functional autophagy assays provides multiple lines of evidence. The generation of knock-in cell lines with point mutations is a rigorous approach that allows assessment at near-physiological expression levels. The comparison with cryo-EM structures adds credibility to the predictions. The identification of specific residues mediating each interaction provides a clear framework for future studies.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors claim that AlphaFold2 predictions reveal the core interactions organizing the ULK complex, including specific residue-level contacts between ATG13 and FIP200, ATG13 and ULK1, and ULK1 and FIP200
- **Evidence pointer** Figure 1B-C, Figure 2A-B, Figure 3A-B; location not provided
- **Concern** The manuscript relies heavily on AlphaFold2 predictions as the structural basis for the proposed interaction model. While AlphaFold2 has proven valuable for predicting protein structures, its accuracy for predicting protein-protein interaction interfaces, particularly involving intrinsically disordered regions, is less established. The authors do not provide experimental validation of the predicted atomic contacts, such as mutagenesis of the predicted hydrophobic pockets in FIP200 or ULK1 to confirm the binding mode. The comparison with cryo-EM structures is mentioned but not shown in detail, and the cryo-EM structures themselves are at relatively low resolution (4.2-5.85 Å), which may not be sufficient to validate specific side-chain interactions. The authors should either provide higher-resolution experimental structural data or temper their claims about the structural basis of the interactions.
- **Why it matters** The structural model is the foundation for all subsequent mutagenesis and functional studies. If the predicted interfaces are incorrect, the interpretation of the functional data would be compromised. The field requires reliable structural information to understand the molecular mechanism of ULK complex assembly and to design future experiments.
- **Resolution test** Provide experimental validation of the predicted interfaces, such as mutagenesis of the predicted binding pockets in FIP200 and ULK1, or obtain higher-resolution structural data (e.g., X-ray crystallography or cryo-EM at better than 4 Å resolution) that confirms the predicted contacts. Alternatively, clearly state the limitations of the computational predictions and present them as a model requiring further validation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Functional significance
- **Claim pointer** The authors claim that the triad interaction is "required" for ULK complex formation and autophagy, and that each interaction is "additively important" for autophagic flux
- **Evidence pointer** Figure 3G-H, Figure 4D-E; location not provided
- **Concern** The functional data show partial reductions in autophagic flux rather than complete abrogation. For example, the ULK1 FIP2A mutant shows "partially but significantly reduced" processed Halo bands, and the ATG13 FU5A mutant shows flux "almost equivalent to that in the knock-out cells" but the actual quantitative values are not provided. The claim that the triad interaction is "required" is too strong given the partial phenotypes observed. Additionally, the authors do not assess whether the mutations affect ULK complex stability or assembly directly, or whether the effects on autophagy are secondary to other defects. The additive model is inferred but not rigorously tested, as double and triple mutant combinations are not systematically compared.
- **Why it matters** The central claim of the manuscript is that the triad interaction is essential for ULK complex function. If the effects are only partial, the conclusion needs to be revised. Understanding the quantitative contribution of each interaction is important for developing a mechanistic model of ULK complex regulation.
- **Resolution test** Provide quantitative data for all functional assays, including exact values and statistical comparisons. Test whether the mutations affect ULK complex assembly directly (e.g., by size exclusion chromatography or native gel analysis). Systematically compare single, double, and triple mutants to rigorously test the additive model. Revise the language to accurately reflect the magnitude of the observed effects.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Experimental rigor
- **Claim pointer** The authors claim that the ULK1 FIP2A mutation specifically disrupts ULK1-FIP200 binding without significantly affecting ULK1-ATG13 affinity, based on ITC analysis
- **Evidence pointer** Figure S2B; location not provided
- **Concern** The ITC data for the ULK1 FIP2A mutant are described as not having a precisely determined Kd value, which is concerning. The authors state that the mutant "retains substantial affinity" for ATG13, but without a precise Kd, it is difficult to assess whether the mutation has any effect on ATG13 binding. The specificity of the FIP2A mutation is critical for interpreting the functional data, as off-target effects on ATG13 binding would confound the conclusions. The authors should provide a more rigorous characterization of the mutant's binding properties.
- **Why it matters** The interpretation of the functional data depends on the specificity of the mutations. If the FIP2A mutation also affects ATG13 binding, the observed functional defects cannot be attributed solely to disruption of the ULK1-FIP200 interaction.
- **Resolution test** Provide a more detailed ITC analysis, including the actual thermograms and fitted parameters. If the Kd cannot be determined precisely, use an alternative method (e.g., fluorescence polarization or surface plasmon resonance) to quantify the binding affinity. Clearly state the limitations of the ITC data and how they support the conclusion of specificity.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Biological relevance
- **Claim pointer** The authors suggest that the triad interaction is important for autophagy in mammals and may have implications for understanding tissue-specific autophagic activity
- **Evidence pointer** Discussion section; location not provided
- **Concern** The functional studies are performed exclusively in HeLa cells and MEFs, which are immortalized cell lines. The authors do not assess the importance of the triad interaction in primary cells or in vivo. The discussion speculates about tissue-specific regulation through splicing variants, but no experimental evidence is provided to support this claim. The physiological relevance of the identified interactions remains unclear.
- **Why it matters** Autophagy is a highly context-dependent process, and findings in immortalized cell lines may not translate to physiological settings. The authors' speculation about tissue-specific regulation requires experimental support to be meaningful.
- **Resolution test** Perform experiments in primary cells or animal models to assess the importance of the triad interaction in a more physiologically relevant context. Alternatively, clearly state that the physiological relevance remains to be determined and avoid overinterpretation.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1A
- **Evidence pointer** Figure 1A; location not provided
- **Issue** The domain organization diagram is mentioned but not shown in the provided text. The authors should ensure that the figure clearly indicates the regions used for AlphaFold2 predictions and the locations of the mutations.
- **Required correction** Provide a clear and detailed domain organization diagram that includes the boundaries of the constructs used and the positions of all mutations.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Figure 3H, Figure 4E
- **Evidence pointer** Figure 3H, Figure 4E; location not provided
- **Issue** The statistical methods are described as being in the figure legends, but the legends are not fully provided. The authors should ensure that all statistical details, including the number of independent experiments, the specific test used, and the exact p-values, are clearly stated.
- **Required correction** Provide complete statistical information for all quantitative data, including the number of replicates and the specific statistical tests used.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods section
- **Evidence pointer** Materials and Methods; location not provided
- **Issue** The methods for the AlphaFold2 predictions are described, but the authors do not provide details on the confidence metrics used to assess the reliability of the predicted interfaces, such as the predicted aligned error (PAE) values for the specific interfaces.
- **Required correction** Include a more detailed description of the AlphaFold2 confidence metrics for the predicted interfaces, including PAE values and pLDDT scores for the key residues.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion section
- **Issue** The authors discuss the difference between the mammalian ULK complex and the yeast Atg1 complex, but the evolutionary implications are not fully explored. The statement that the triad interaction is "likely beneficial for cells that form the complicated cellular communities that comprise the metazoans" is speculative and not supported by data.
- **Required correction** Either provide evidence to support the evolutionary claims or temper the language to clearly indicate that this is speculation.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 4B
- **Evidence pointer** Figure 4B; location not provided
- **Issue** The authors mention a correction to Figure 4B regarding a previously misinterpreted ULK1 expression change. The current version of the figure should be carefully checked to ensure that the data are accurately presented.
- **Required correction** Verify that the corrected Figure 4B accurately represents the data and that the text description matches the figure.

- **Technical failings that need to be addressed before the case is established** R1-M1 (structural validation), R1-M2 (functional significance and quantitative data), R1-M3 (ITC specificity)

- **Assessment against Nature-style criteria** 
  - Originality: The work is original in its application of AlphaFold2 to predict the ULK complex architecture and in identifying specific residues mediating the three binary interactions. However, the overall concept of the ULK complex composition is not novel, and the structural predictions require experimental validation to be considered a significant advance.
  - Scientific importance: The ULK complex is central to autophagy initiation, and understanding its molecular architecture is important for the field. The work has the potential to inform future studies on autophagy regulation, but the current evidence does not fully establish the proposed model.
  - Interdisciplinary readership: The work will primarily appeal to autophagy researchers and structural biologists. The use of AlphaFold2 may attract computational biologists, but the overall scope is relatively narrow.
  - Technical soundness: The experimental approaches are generally sound, but there are concerns about the strength of the functional data and the lack of high-resolution structural validation. The ITC data for the FIP2A mutant are incomplete, and the quantitative effects on autophagy are modest.
  - Readability for nonspecialists: The manuscript is generally well-written and accessible, but the heavy reliance on structural details and the lack of clear quantitative summaries may make it challenging for nonspecialists to fully appreciate the significance of the findings.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important question and presents a plausible model, but the current evidence is insufficient to fully support the claims. The authors need to provide stronger experimental validation of the predicted interfaces, more quantitative functional data, and a more nuanced interpretation of the results. If these concerns are addressed, the work could make a valuable contribution to the autophagy field.

## Risk / unsupported claims
- The claim that the triad interaction is "required" for ULK complex formation and autophagy is not fully supported by the data, which show partial rather than complete effects
- The claim that the AlphaFold2 predictions reveal the structural basis of the interactions is not experimentally validated at high resolution
- The speculation about tissue-specific regulation through splicing variants is not supported by experimental evidence
- The claim that the triad interaction is "likely beneficial for cells that form the complicated cellular communities that comprise the metazoans" is speculative
- The statement that the ULK1 FIP2A mutation specifically disrupts ULK1-FIP200 binding without affecting ATG13 binding is not rigorously supported due to incomplete ITC data
- The functional significance of the identified interactions in physiological contexts is not assessed, as all experiments are performed in immortalized cell lines