## Review setup
- **Input scope** Full manuscript text including abstract, results, discussion, methods, and supplementary file descriptions
- **Assessment boundary** Scientific content, methodological rigor, and claims as presented in the manuscript; no external data or literature verification performed
- **Shared manuscript claim summary** The authors report that intrinsically disordered regions (IDRs) in Mycobacterium tuberculosis are enriched in virulence-related, secreted, and membrane-associated proteins that interact with human host factors. They report that Mtb IDRs evolve faster than folded domains, are poorly antigenic, and that human interaction partners are evolutionarily constrained, essential, and highly connected. They extend analyses to 540 human-infecting bacteria and report wide variation in IDR representation and conformational properties.
- **Visible evidence base** Main text figures 1-6, supplementary tables S1-S9, supplementary datasets S1-S11, methods section
- **Missing materials affecting confidence** Raw data files, code for analyses, complete supplementary tables (only descriptions provided), details of the benchmarking procedure, and the full list of human-Mtb PPIs with their sources

## Reviewer
- **Overall assessment** This manuscript addresses a timely and underexplored topic: the role of intrinsically disordered regions in bacterial pathogens, specifically Mycobacterium tuberculosis. The authors combine structural predictions, evolutionary analyses, and interaction data to propose that Mtb uses fast-evolving IDRs to engage conserved host factors. The study is broad in scope and generates several testable hypotheses. However, the manuscript has substantial methodological concerns that need to be addressed before the central claims can be considered established. The reliance on predicted disorder without experimental validation, the potential circularity in the PPI analysis, and the incomplete treatment of confounding variables in the evolutionary analyses are the main issues. The comparative analysis across 540 bacteria is interesting but underdeveloped in its interpretation. Overall, the work is potentially important but requires major revisions to substantiate its claims.

- **Who would be interested in the results, and why** Researchers studying host-pathogen interactions, particularly those focused on Mycobacterium tuberculosis biology and virulence mechanisms. The work will also be of interest to the intrinsically disordered protein community, as it extends IDR analysis to bacterial pathogens. Evolutionary biologists studying host-pathogen coevolution and the molecular determinants of host adaptation may find the evolutionary rate analyses relevant. Additionally, those working on vaccine development or immunogenicity prediction may be interested in the antigenicity findings, though the authors themselves note the limitations of their epitope analysis.

- **Major strengths** The manuscript addresses a genuinely understudied question: the role of IDRs in bacterial pathogens. The integration of multiple data types (structural predictions, evolutionary rates, PPI data, epitope mapping) is ambitious and provides a multi-faceted view. The benchmarking of disorder prediction tools is a valuable contribution, particularly the observation that AlphaFold2-based predictions differ substantially from other methods for PE-PGRS proteins. The extension to 540 bacterial species provides a useful comparative framework. The authors are appropriately cautious in some interpretations, particularly regarding the limitations of prediction-based approaches.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of disorder prediction
- **Claim pointer** The authors claim that AlphaFold2-based predictions are reliable for identifying IDRs in Mtb, and use these predictions for all downstream analyses.
- **Evidence pointer** Figure 1, Methods section "Disorder prediction"
- **Concern** The benchmarking against PDB structures is limited to 229 proteins with X-ray structures, which is a small and potentially biased subset of the Mtb proteome. Proteins amenable to crystallization are likely depleted for IDRs, creating a systematic bias in the benchmark. The authors report that AlphaFold2 performs best on this benchmark, but this does not establish that AlphaFold2 is accurate for the full proteome, particularly for proteins with unusual amino acid composition like PE-PGRS. The authors themselves note that AlphaFold2 fails to predict IDRs in PE-PGRS proteins that are predicted as disordered by other methods, yet they proceed to use AlphaFold2 predictions for all downstream analyses. This is a critical inconsistency. If AlphaFold2 systematically underestimates disorder in PE-PGRS proteins, then the evolutionary rate analyses, antigenicity analyses, and functional enrichment analyses are all affected for this important protein family.
- **Why it matters** The central claims of the manuscript depend entirely on accurate IDR identification. If the prediction method is biased, all downstream conclusions are potentially compromised. The PE-PGRS family is specifically highlighted as important for Mtb virulence, so the failure to accurately predict disorder in these proteins is not a minor issue.
- **Resolution test** The authors should provide a more comprehensive validation of their disorder predictions, including: (1) analysis of the benchmark set composition and its representativeness; (2) sensitivity analyses showing that their main conclusions hold when using different disorder prediction methods; (3) explicit discussion of how the PE-PGRS discrepancy affects their results; (4) if possible, experimental validation of disorder for a subset of proteins using techniques such as limited proteolysis or circular dichroism.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor and confounding
- **Claim pointer** The authors claim that IDRs are enriched in proteins involved in virulence, immune response modulation, and lipid metabolism, and that IDR-containing proteins have higher dN/dS.
- **Evidence pointer** Figure 2, Figure 3, Methods sections "Functional characterization" and "Evolutionary rates"
- **Concern** The evolutionary rate analyses do not adequately control for known confounders. Protein expression level, protein-protein interaction degree, and protein length are all known to correlate with dN/dS. The authors show that IDR-containing proteins have higher dN/dS, but do not test whether this relationship holds after controlling for these variables. Similarly, the enrichment of IDRs in virulence factors and immune-related proteins could be confounded by the fact that these proteins are more likely to be secreted or membrane-associated, which may have different evolutionary constraints. The comparison between essential and non-essential proteins is informative but does not address the other confounders. The authors also do not account for the phylogenetic non-independence of the bacterial species in their comparative analysis.
- **Why it matters** Without controlling for these confounders, the claim that IDRs specifically evolve faster cannot be distinguished from the possibility that IDR-containing proteins evolve faster because they are, for example, more highly expressed or have different functional constraints. The comparative analysis across 540 bacteria similarly needs phylogenetic correction.
- **Resolution test** The authors should perform multiple regression analyses that include expression level, interaction degree, protein length, and other relevant covariates as predictors of dN/dS, with IDR content as the variable of interest. For the comparative analysis, they should use phylogenetic generalized least squares or similar methods that account for evolutionary relationships among species.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of PPI data
- **Claim pointer** The authors claim that Mtb proteins involved in PPIs with human proteins have higher IDR fractions, and that human interaction partners are evolutionarily constrained.
- **Evidence pointer** Figure 2C, Figure 5, Methods section "Protein-protein interaction analysis"
- **Concern** The PPI dataset is assembled from multiple sources with different experimental methodologies and confidence levels. The authors state that they used "high-confidence" interactions, but the criteria for this are not clearly described. The majority of interactions come from two large-scale studies, which may have different false-positive rates. The analysis of human interaction partners is particularly concerning: the authors compare evolutionary rates of human proteins that interact with Mtb versus those that do not, but this comparison is only meaningful if the "non-interacting" set is appropriately matched. Human proteins that interact with Mtb are likely to be enriched for certain functional categories (e.g., immune-related), which may have different baseline evolutionary rates. The finding that Mtb-interacting human proteins are more conserved could reflect their functional importance rather than a specific adaptation to Mtb.
- **Why it matters** The interpretation that Mtb targets conserved host factors is central to the manuscript's thesis. If the comparison is confounded by functional category or other variables, this conclusion is not supported.
- **Resolution test** The authors should: (1) provide a clear description of the PPI confidence criteria; (2) match the interacting and non-interacting human protein sets for functional category, expression level, and other relevant variables; (3) perform sensitivity analyses excluding lower-confidence interactions; (4) test whether the conservation finding holds within functional categories.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Antigenicity analysis
- **Claim pointer** The authors claim that Mtb IDRs are poorly antigenic, as epitopes are depleted within IDRs.
- **Evidence point** Figure 3D, Methods section "Epitope analysis"
- **Concern** The epitope data come from two studies with potentially different methodologies and coverage. The authors do not describe how epitopes were mapped to proteins, what proportion of the proteome is covered by the epitope data, or whether the epitope set is biased toward certain protein families. The finding that epitopes are depleted in IDRs could reflect technical biases in epitope identification (e.g., peptides from IDRs may be less stable or less likely to be presented) rather than a biological property. The authors also do not address the relationship between antigenicity and the evolutionary rate findings: if IDRs are fast-evolving and poorly antigenic, this is an unusual combination that deserves more discussion.
- **Why it matters** The antigenicity claim is presented as a significant finding, but the analysis may be confounded by technical biases in epitope identification. The interpretation of this finding for vaccine development or immune evasion is underdeveloped.
- **Resolution test** The authors should: (1) describe the epitope mapping methodology in detail; (2) assess the coverage and potential biases of the epitope dataset; (3) perform sensitivity analyses using different epitope prediction methods or datasets; (4) discuss the implications of fast-evolving, poorly antigenic IDRs in the context of immune evasion.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Comparative analysis across bacteria
- **Claim pointer** The authors report wide variation in IDR representation and conformational properties among 540 human-infecting bacteria.
- **Evidence pointer** Figure 6, Methods section "Proteomes and structure models"
- **Concern** The comparative analysis is presented as a descriptive result, but the interpretation is limited. The authors do not investigate what factors might explain the variation in IDR content across species. Is IDR content related to genome size, pathogenicity, lifestyle, or phylogenetic position? The selection of 540 species is based on availability in the AlphaFold database, which may introduce biases. The analysis of conformational properties is limited to 10 species, and the criteria for this selection are not described.
- **Why it matters** The comparative analysis could provide important context for understanding the role of IDRs in bacterial pathogenesis, but as presented, it is largely descriptive and does not generate strong hypotheses.
- **Resolution test** The authors should: (1) test whether IDR content correlates with ecological or genomic variables; (2) describe the criteria for selecting the 10 species for conformational analysis; (3) discuss the implications of the observed variation for understanding IDR function in bacteria.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Disorder prediction threshold
- **Evidence point** Methods section "Disorder prediction"
- **Issue** The authors state that residues with ⟨pLDDT⟩ > 0.8 are considered folded and those with ⟨pLDDT⟩ < 0.7 are disordered, with a gap region in between. The rationale for these specific thresholds is not provided, and the sensitivity of results to these thresholds is not tested.
- **Required correction** Provide justification for the chosen thresholds and perform sensitivity analyses with alternative thresholds.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Multiple testing
- **Evidence point** Figure 2, Figure 4
- **Concern** The GO enrichment analyses involve many statistical tests, but the authors do not describe how multiple testing correction was applied.
- **Required correction** Describe the multiple testing correction method used for GO analyses, or state if no correction was applied.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Code and data
- **Evidence point** Methods section
- **Issue** The manuscript does not state whether analysis code is available or provide a link to a repository.
- **Required correction** Provide a data and code availability statement.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation of conformational properties
- **Affected element** Figure 4E
- **Concern** The comparison of sequence-ensemble relationships between Mtb and human IDRs is interesting, but the interpretation of the differences (e.g., lower charge content in Mtb IDRs) is limited. The authors do not discuss what functional implications these differences might have.
- **Required correction** Expand the discussion of the observed differences in conformational properties between Mtb and human IDRs and their potential functional significance.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 1C
- **Concern** The ribbon diagram of PE_PGRS16 is difficult to interpret in grayscale; the color coding of pLDDT scores may not be accessible to color-blind readers.
- **Required correction** Consider using a colorblind-safe palette or adding labels to the figure.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Issue** The term "fast evolving" is used to describe IDRs, but the authors do not specify whether this refers to the nucleotide level, amino acid level, or both. The dN/dS measure is used, but the distinction between different evolutionary rate measures could be clarified.
- **Required correction** Clarify the evolutionary rate measure used and consider discussing whether the findings are robust to different measures.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Issue** The limitations section is brief and does not address the potential biases in the PPI dataset or the limitations of the epitope analysis in sufficient detail.
- **Required correction** Expand the limitations section to address these concerns.

## Risk / unsupported claims
- The claim that Mtb uses IDRs to "sense and interact with its environment" is speculative and presented in the conclusions without direct evidence. The authors themselves note this "awaits experimental validation," but the claim is still presented prominently.
- The claim that the "classical arms race paradigm is not universal in host-pathogen interactions" is a broad generalization based on a single bacterial species and may overstate the implications of the findings.
- The finding that human proteins interacting with Mtb are evolutionarily constrained is presented as a key result, but the analysis may be confounded by functional category and other variables, as noted in R1-M3.
- The comparative analysis across 540 bacteria is presented as evidence of "wide variations in IDR representation," but the functional significance of this variation is not established.
- The benchmarking conclusion that AlphaFold2-based predictions are superior for Mtb IDR identification is based on a limited and potentially biased benchmark set, as noted in R1-M1.