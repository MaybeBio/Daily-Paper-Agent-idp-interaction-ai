## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, and conclusions as presented in the manuscript
- **Shared manuscript claim summary** The authors report that de novo proteins in rice evolve rapidly in structural features, including decreases in intrinsic disorder, increases in structured elements, hydrophobicity, and molecular recognition features, and form stable complexes with older proteins, all within a short evolutionary timeframe of 1 to 2 million years.
- **Visible evidence base** Abstract, Introduction, Materials and Methods, Results, Discussion, Conclusion, Data Availability statement
- **Missing materials affecting confidence** Supplementary figures and tables referenced throughout the text were not provided. These include supplementary figures S1 to S11 and supplementary tables S1 to S7. The absence of these materials limits the ability to fully evaluate statistical analyses, structural predictions, and interaction data.

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question regarding the structural evolution of de novo proteins. The authors leverage a well-characterized set of de novo genes in Oryza and apply state-of-the-art computational tools to infer structural properties and protein complex formation. The central finding, that de novo proteins undergo rapid structural maturation within a remarkably short evolutionary window, is potentially significant. However, the manuscript relies heavily on computational predictions without experimental validation, and several key analyses are presented with insufficient detail to assess their robustness. The statistical framework for comparing evolutionary rates between de novo genes and duplicates requires clarification. The claim that de novo proteins form stable complexes with older proteins is based on a small number of predicted interactions and would benefit from additional validation or at least a more cautious interpretation. The proposed EIS and EIC models are conceptually interesting but are presented with limited direct evidence. Overall, the manuscript presents a compelling hypothesis supported by preliminary computational evidence, but the case is not fully established from the provided materials.

- **Who would be interested in the results, and why** Evolutionary biologists studying gene origination and protein evolution would find these results of direct interest. Researchers working on de novo gene birth, particularly in plants, would value the detailed temporal analysis of structural changes. The broader community interested in protein disorder and its evolutionary dynamics would also find relevance. Additionally, those studying protein-protein interactions and the emergence of new functional modules in biological networks would be interested in the proposed EIS and EIC models. The findings have implications for understanding how new genes integrate into existing cellular pathways.

- **Major strengths** The manuscript addresses a previously underexplored question with a well-designed comparative framework. The use of a large, previously identified set of de novo genes with clear origination times provides a solid foundation. The application of multiple complementary computational tools, including Metapredict, AUCpreD, AlphaFold2, and AlphaFold2-multimer, strengthens the analysis. The comparison with gene duplicates provides an appropriate baseline for assessing evolutionary rates. The authors are appropriately cautious in acknowledging limitations of computational predictions. The proposed EIS and EIC models provide a useful conceptual framework for future studies.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that de novo proteins evolve faster than gene duplicates in structural features, with specific rates of change per million years.
- **Evidence pointer** Results sections "The Levels of ISD in De Novo Proteins Reduce Gradually Over Evolutionary Time" and "Rapid Evolution of Structural Elements in De Novo Proteins", Figures 2 and 3
- **Concern** The statistical comparison of evolutionary rates between de novo genes and gene duplicates is not fully described. The authors report linear regression slopes for de novo genes but do not clearly describe how the comparison with gene duplicates was performed statistically. The claim that de novo genes evolve "faster" requires a formal statistical test comparing the two groups, not just separate regressions. Additionally, the sample sizes for each age group are not reported, and it is unclear whether the regression analyses account for phylogenetic non-independence or variable numbers of genes per age group.
- **Why it matters** The central conclusion of the manuscript depends on demonstrating a statistically significant difference in evolutionary rates between de novo genes and gene duplicates. Without a proper comparative statistical framework, the claim of "faster evolution" is not rigorously supported.
- **Resolution test** Provide a formal statistical comparison of slopes or rates between de novo genes and gene duplicates, including confidence intervals. Report sample sizes per age group and describe how phylogenetic relationships were handled. If possible, apply a mixed-effects model with age group as a random factor.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that most de novo proteins readily form low-energy and compact complexes with other proteins, facilitated by extensive residue contacts and conformational flexibility.
- **Evidence pointer** Results section "Protein Complex Interaction Could Facilitate the Structural Evolution of De Novo Protein", Figures 5, supplementary figures S9 to S11, supplementary tables S6 and S7
- **Concern** The protein-protein interaction analysis is based on only 30 predicted pairs for de novo genes and 30 for duplicates. The criteria for selecting interaction partners, while described, appear to be applied in a way that may introduce bias. The comparison of binding affinities between de novo and duplicate complexes is reported as a single median comparison without clear effect sizes or confidence intervals. The claim that 83% of de novo complexes have high binding affinity is based on a small sample and a computational threshold. The conformational change example in Figure 5a is a single case and may not be representative.
- **Why it matters** The claim that de novo proteins form stable complexes is a major conclusion of the manuscript. If the interaction analysis is based on a small, potentially biased sample with limited statistical power, the conclusion is not robust.
- **Resolution test** Increase the number of interaction pairs analyzed or provide a power analysis justifying the current sample size. Report effect sizes and confidence intervals for binding affinity comparisons. Validate a subset of predicted interactions using an independent method, such as docking simulations or experimental data from public databases.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that de novo proteins have higher positive charges and smaller molecular weights than gene duplicates, and that these properties facilitate faster diffusion and interaction.
- **Evidence pointer** Results section "The Properties of Amino Acids in De Novo Genes Are Consistent with the Structural Changes", Figure 4, supplementary figure S8
- **Concern** The analysis of physicochemical properties relies on comparisons of medians across age groups. The statistical tests used for these comparisons are not fully described. The claim of "higher positive charges" is based on isoelectric point calculations, which are indirect measures. The relationship between these properties and diffusion rates is speculative and not directly tested. The authors do not account for potential confounding factors such as gene length or expression level.
- **Why it matters** The physicochemical property analysis supports the proposed mechanism for rapid interaction. If the statistical basis is weak or the mechanistic link is speculative, this part of the argument is not convincing.
- **Resolution test** Clearly describe the statistical tests used for each comparison. Consider controlling for gene length and expression level in the analysis. If possible, directly test the relationship between charge, size, and diffusion using biophysical models or experimental data.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Originality
- **Claim pointer** The authors propose two models, EIS and EIC, to interpret the structural evolution of de novo proteins.
- **Evidence pointer** Discussion section "Two Models for Structural Evolution of De Novo Proteins", Figure 6
- **Concern** The EIS and EIC models are presented as novel conceptual contributions. However, similar ideas have been proposed in the literature regarding the role of disorder in protein evolution and the importance of binding-induced folding. The authors do not clearly distinguish their models from these earlier proposals. The models are also presented with limited direct evidence, as the data are primarily correlational.
- **Why it matters** The conceptual framework is a key contribution of the manuscript. If the models are not clearly differentiated from existing ideas or are not well supported by the data, their impact is diminished.
- **Resolution test** Strengthen the discussion of how EIS and EIC differ from previous models. Provide additional evidence, such as analysis of evolutionary rates in specific protein families or experimental validation of binding-induced folding for a subset of de novo proteins.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction
- **Evidence pointer** Introduction, first paragraph
- **Issue** The introduction uses several technical terms without definition, such as "intrinsic structural disorder" and "molecular recognition features." While these are defined later in the text, a brief definition in the introduction would improve accessibility.
- **Required correction** Add brief definitions or parenthetical explanations for these terms when first introduced.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods
- **Evidence pointer** Methods section "Gene Coexpression Analysis"
- **Issue** The description of the coexpression analysis is brief. The threshold for significance (P < 10^-5) is stated, but the multiple testing correction method is not described.
- **Required correction** Describe the multiple testing correction approach used for the coexpression analysis.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results
- **Evidence pointer** Results section "The Levels of ISD in De Novo Proteins Reduce Gradually Over Evolutionary Time"
- **Issue** The authors state that 37.57% of de novo proteins exhibit complete ISD, but the threshold for "complete ISD" is not clearly defined. It is stated as "100% of residues in disordered states," but it is unclear how this was determined.
- **Required correction** Clarify the definition of complete ISD and how the 100% threshold was applied.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results
- **Evidence pointer** Results section "Rapid Evolution of Structural Elements in De Novo Proteins"
- **Issue** The authors report rates of change for secondary structure elements but do not provide confidence intervals for these rates.
- **Required correction** Provide confidence intervals for the reported rates of change.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Discussion
- **Evidence pointer** Discussion section "De Novo Proteins Initially Exhibit High Disorder But Rapidly Evolve Toward Structured Forms"
- **Issue** The discussion of the biological implications of the findings is somewhat dense and could be more accessible to a broader audience.
- **Required correction** Consider adding a brief summary of the broader implications for understanding protein evolution and function.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results
- **Evidence pointer** Results section "Protein Complex Interaction Could Facilitate the Structural Evolution of De Novo Protein"
- **Issue** The authors report that "only one de novo protein (Osjap01g35740, br4) with median TM score less than 0.17" but do not provide the distribution of TM scores for all proteins.
- **Required correction** Provide a summary of the TM score distribution for all de novo proteins.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods
- **Evidence pointer** Methods section "The Analyses of Protein Complex Based on AlphaFold2-Multimer"
- **Issue** The criteria for selecting interaction partners are described, but the number of potential partners screened and the filtering process are not fully detailed.
- **Required correction** Provide more detail on the partner selection process, including the number of candidates considered and the filtering steps.

## Risk / unsupported claims
- The claim that de novo proteins evolve faster than gene duplicates in structural features is not fully supported by the statistical analyses presented, as the comparison method is not clearly described.
- The claim that most de novo proteins form stable complexes with older proteins is based on a small sample of 30 predicted interactions and requires additional validation.
- The proposed EIS and EIC models are presented as novel but are not clearly differentiated from existing concepts in the literature.
- The relationship between physicochemical properties (charge, size) and diffusion rates is speculative and not directly tested.
- The claim that de novo proteins require no longer than 5 million years to attain intrinsic structural order comparable to gene duplicates is an extrapolation from a linear model and should be presented with appropriate caveats.
- Several analyses rely on computational predictions without experimental validation, and the limitations of these methods are acknowledged but not fully addressed.