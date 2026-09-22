## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods/results narrative, discussion, conclusion) as provided
- **Assessment boundary** Scientific content, data analysis, claims, and presentation quality of the review article; database utility and bioinformatic analyses described
- **Shared manuscript claim summary** The authors present an updated literature-curated database of mammalian stress granule proteins (RNAgranuleDB v2.0), analyze the phase separation and aggregation propensities of these proteins using multiple prediction tools, characterize sequence features of their intrinsically disordered regions, and review the regulatory roles of post-translational modifications and RNA-level determinants in stress granule dynamics
- **Visible evidence base** Text describing database curation (approximately 650 articles retrieved, 100 primary articles curated, 4,731 proteins, 13,552 entries), bioinformatic analyses (GO enrichment, domain enrichment, IDR feature analysis, phase separation predictions), and cited literature
- **Missing materials affecting confidence** Figures and tables referenced but not provided; supplementary tables (S1–S8) not accessible; detailed methods for bioinformatic analyses not fully described; statistical details and software parameters not fully specified

## Reviewer
- **Overall assessment** This is a comprehensive and timely review that provides a valuable community resource in the form of an updated stress granule database. The authors combine literature curation with quantitative bioinformatic analyses to generate new insights into the compositional and regulatory features of stress granules. The manuscript is well-structured and covers a broad range of topics from biophysical principles to disease relevance. However, the scientific claims derived from the bioinformatic analyses are difficult to fully evaluate without access to the referenced figures, tables, and detailed methods. The review would benefit from clearer presentation of the analytical workflow and more explicit discussion of the limitations of prediction tools. The balance between original analysis and literature synthesis is appropriate for a review article, though the novelty of the analytical findings is somewhat limited by the reliance on existing prediction tools and previously published datasets.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, RNA biology, and stress responses would find this review valuable. The updated database (RNAgranuleDB v2.0) will be a practical resource for the stress granule community. Investigators interested in the molecular mechanisms of neurodegeneration, particularly ALS and FTD, would also benefit from the compilation of disease-associated proteins and their regulatory features. The analysis of IDR features and phase separation predictions may interest computational biologists working on protein disorder and condensate prediction.

- **Major strengths**
  1. The manuscript provides a comprehensive and up-to-date compilation of the stress granule proteome, representing a significant community resource
  2. The integration of multiple phase separation prediction tools provides a multi-perspective analysis of the proteome
  3. The hierarchical clustering of IDR features reveals potentially meaningful subgroups of SG proteins with shared sequence properties
  4. The review of post-translational modifications is thorough and well-organized by modification type
  5. The discussion of RNA-level regulation, including m6A modifications and RNA structure, adds depth beyond typical protein-centric reviews
  6. The authors appropriately acknowledge controversies and conflicting findings in the field, presenting a balanced perspective

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility and methodological transparency
- **Claim pointer** The authors claim to have performed comprehensive bioinformatic analyses including GO enrichment, domain enrichment, phase separation prediction, and IDR feature analysis of the SG proteome
- **Evidence pointer** Section "Analysis of the SG Proteome"; Methods referenced but not fully provided
- **Concern** The manuscript describes multiple bioinformatic analyses but does not provide sufficient methodological detail to evaluate or reproduce them. The specific parameters, thresholds, and statistical methods for the phase separation predictors are not described. The IDR feature analysis methodology is unclear, including how IDRs were defined, which features were calculated, and how the hierarchical clustering was performed. The GO enrichment analysis parameters and background set are not specified.
- **Why it matters** Without detailed methods, the analytical results cannot be independently verified or reproduced. This limits the scientific utility of the database and the validity of the derived conclusions about SG protein properties.
- **Resolution test** Provide a detailed Methods section describing all bioinformatic analyses, including software versions, parameters, thresholds, statistical tests, and multiple testing corrections. Make the analysis scripts and input data publicly available.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality and validation
- **Claim pointer** The authors state that the SG proteome is defined by a weighted scoring system with a cutoff of 7 for Tier 1 proteins, yielding 407 proteins
- **Evidence pointer** Section "Update of the SG Proteome"; Table 1; Table S1
- **Concern** The weighted scoring system is described but the rationale for the specific weights and the cutoff of 7 is not justified. The validation of this scoring approach against independent experimental data is not presented. The authors note that proteins with high scores often localize to both SGs and PBs, but the criteria for excluding PB-specific proteins from the SG proteome are not clearly described beyond stating that 66 proteins were excluded.
- **Why it matters** The reliability of the entire downstream analysis depends on the accuracy of the SG proteome definition. An arbitrary or poorly validated scoring system could introduce systematic bias into the proteome and all subsequent analyses.
- **Resolution test** Provide justification for the scoring weights and cutoff, including sensitivity analyses with different thresholds. Validate the Tier 1 classification against independent experimental datasets (e.g., orthogonal proteomic studies or published validation experiments).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation and overreach
- **Claim pointer** The authors suggest that SG proteins contain significantly more aggregation-prone regions than general droplet drivers, implying a link between SG composition and pathological aggregation
- **Evidence pointer** Section "Analysis of the SG Proteome Using Phase Separation Predictors"; Figure 7
- **Concern** The finding that SG proteins have more aggregation-prone regions is interpreted as potentially relevant to disease, but the authors do not adequately discuss alternative explanations. For example, aggregation-prone regions may be enriched simply because SG proteins are RNA-binding proteins with intrinsically disordered regions, which are inherently aggregation-prone. The comparison to "human droplet drivers" may not be the most appropriate control group.
- **Why it matters** Overinterpretation of correlative bioinformatic findings could mislead the field and generate unsupported hypotheses about disease mechanisms.
- **Resolution test** Add a more nuanced discussion of alternative interpretations, including the possibility that aggregation-proneness is a byproduct of RNA-binding function. Include appropriate control analyses, such as comparison to other RNA-binding protein sets or to proteins in other condensate types.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Completeness and balance
- **Claim pointer** The review claims to cover the regulatory dynamics of stress granules, including assembly and disassembly mechanisms
- **Evidence pointer** Section "Regulation of Stress Granule Dynamics"
- **Concern** The section on post-translational modifications is comprehensive, but the coverage of RNA-level regulation is comparatively brief. The discussion of RNA modifications focuses heavily on m6A, with limited discussion of other modifications (e.g., pseudouridine, inosine) that may also affect SG dynamics. The section on RNA structure and its role in SG assembly is underdeveloped given the stated importance of RNA in SG biology.
- **Why it matters** The title promises a comprehensive treatment of regulatory dynamics. An imbalanced coverage may give readers a skewed view of the field and understate the importance of RNA-level regulation.
- **Resolution test** Expand the RNA-level regulation section to include a more balanced discussion of different RNA modifications and their potential roles in SG dynamics. Consider adding a subsection on RNA structure and its contribution to SG assembly and organization.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and accessibility
- **Affected element** Introduction, section on biomolecular condensates
- **Evidence pointer** Section "Biomolecular Condensates: A Source of Cellular Organization and Responsiveness"
- **Issue** The introduction assumes significant prior knowledge of phase separation concepts. Terms such as "percolation," "stickers," and "Csat" are introduced rapidly without sufficient explanation for non-specialist readers.
- **Required correction** Consider adding a brief primer on phase separation concepts or a glossary of key terms to improve accessibility for readers from diverse backgrounds.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Database update description
- **Evidence pointer** Section "Update of the SG Proteome"
- **Issue** The description of the database update process is clear but the practical usage of RNAgranuleDB v2.0 is not described. Readers are not told how to search, filter, or download data from the database.
- **Required correction** Add a brief subsection or figure describing the database interface and functionality, including how users can access the new features.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** IDR feature analysis
- **Evidence pointer** Section "Feature Analysis of SG IDRs"; Figure 8
- **Issue** The statistical comparison of SG IDR features against the human IDRome is described as using the Wilcoxon rank-sum test, but the multiple testing correction method is not stated. With 87 features tested, uncorrected p-values would be problematic.
- **Required correction** State the multiple testing correction method used (e.g., Benjamini-Hochberg FDR) and report adjusted p-values.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature coverage
- **Affected element** Discussion of SG function
- **Evidence pointer** Section "Introduction to Stress Granules"
- **Issue** The authors acknowledge the lack of consensus on SG function but do not provide a systematic overview of the proposed functions and the evidence for and against each. This is a missed opportunity given the comprehensive nature of the review.
- **Required correction** Consider adding a table or figure summarizing proposed SG functions with key supporting and contradicting evidence.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Throughout
- **Evidence pointer** Multiple sections
- **Issue** The terms "phase separation," "condensation," and "aggregation" are sometimes used interchangeably, which could confuse readers about the distinct biophysical processes involved.
- **Required correction** Define these terms clearly at first use and maintain consistent usage throughout the manuscript.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Future directions
- **Affected element** Conclusion
- **Evidence pointer** Section "Conclusion and Perspectives"
- **Issue** The conclusion raises important open questions but does not provide a prioritized or structured agenda for future research. The questions are presented as a list without discussion of which are most tractable or impactful.
- **Required correction** Consider organizing the open questions by theme (e.g., mechanistic, functional, disease-related) and discussing which experimental approaches are best suited to address each.

## Risk / unsupported claims
- The claim that SG proteins have significantly more aggregation-prone regions than droplet drivers is based on FuzDrop predictions, which have not been experimentally validated for most SG proteins; the biological significance of this finding remains speculative
- The assertion that nearly 15% of the SG proteome has evidence linking them to ALS relies on database annotations (KEGG, OMIM, ClinVar, etc.) that may include indirect or weak associations; the strength and quality of these associations are not assessed
- The claim that m6A modification plays a relatively minor role in SG targeting is presented as a conclusion, but the authors acknowledge conflicting data; this should be framed as an open question rather than a settled finding
- The statement that pre-existing proximal interactions among SG proteins suggest functions independent of visible SG assembly is speculative and not directly supported by the data presented
- The hierarchical clustering of SG IDR features is presented as revealing meaningful subgroups, but the statistical significance and biological relevance of these clusters are not established
- The claim that the updated database represents a "consensus" SG proteome may be overstated given the heterogeneity of experimental conditions across the curated studies and the arbitrary scoring cutoff used