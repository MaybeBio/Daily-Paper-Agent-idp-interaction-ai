## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusion, methods) without figures, tables, or supplementary files
- **Assessment boundary** Statistical methodology, evidence quality, claims of modular architecture in IDRs, generalizability claims, comparison to existing methods
- **Shared manuscript claim summary** The authors present a new computational method (Chi-Score Analysis) that uses the Chi-Square test of homogeneity in a sliding-window, matrix-based approach to identify compositionally distinct subsequences ("modules") within protein intrinsically disordered regions (IDRs). They claim that IDRs possess a non-random, modular architecture characterized by local compositional bias, and that this modularity is broadly generalizable across IDRs of both low and high sequence complexity.
- **Visible evidence base** Abstract, introduction, results sections 2.1-2.3, conclusion, methods section 4.1-4.3, figure legends referenced but figures not visible, GitHub repository link
- **Missing materials affecting confidence** All figures and figure supplements, Table 1, Supplemental File 1, actual code implementation, statistical output details, validation datasets

## Reviewer

- **Overall assessment** The manuscript presents an interesting and potentially useful computational approach for identifying compositionally distinct regions within IDRs. The core idea of applying the Chi-Square test of homogeneity in a sliding-window framework is methodologically reasonable and the authors demonstrate its utility on several well-known IDR-containing proteins. However, the central claim that IDRs have a "non-random, modular architecture" as a generalizable organizational principle is not adequately supported by the evidence presented. The manuscript lacks systematic validation, quantitative benchmarks against existing methods, and a clear statistical framework for determining significance thresholds. The absence of figures and supplementary data in the provided material severely limits the ability to assess the quality of the results.

- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, protein phase separation, and IDR function would find this method potentially useful for identifying compositionally distinct sub-regions within IDRs. The approach could complement existing tools for IDR annotation and may be of interest to computational biologists developing sequence analysis methods. The potential link between modular organization and functional sub-domains in IDRs could interest those studying transcription factors, RNA-binding proteins, and proteins involved in neurodegenerative diseases.

- **Major strengths**
  1. The methodological approach is conceptually novel in applying the Chi-Square test of homogeneity in a sliding-window, matrix-based framework to identify compositional boundaries within IDRs
  2. The method is unbiased and does not require a priori knowledge of compositional "flavors," addressing a genuine limitation of existing candidate-based approaches
  3. The authors provide open-source code and a Google Colab notebook, which enhances reproducibility and accessibility
  4. The application to multiple biologically significant proteins (FUS, TDP-43, Orc1, Spt6, Nucleolin, KMT2B, RNase E) demonstrates broad potential utility
  5. The comparison to scrambled sequences provides a reasonable null model for assessing statistical significance

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical validity
- **Claim pointer** "IDRs have a non-random, modular organization" and "local compositional bias is an organizational principle unique to disordered sequences"
- **Evidence pointer** Section 2.2, Figure 2, Figure 2-figure supplement 1
- **Concern** The claim that IDRs are non-randomly organized into modules rests on the comparison to scrambled sequences, but the manuscript does not provide sufficient detail on the scrambling procedure, the number of scrambles used for the null distribution, or the statistical thresholds applied. The z-score calculation is described but the manuscript does not state what z-score threshold constitutes a "significant" boundary, how multiple testing is controlled across the many boundaries tested, or how the method performs on negative controls beyond the single Orc1 example. The statement that "compositionally biased modules are absent from Orc1's folded domains" is based on a single protein and cannot support the general claim that this organization is "unique to disordered sequences."
- **Why it matters** The central conclusion of the manuscript depends entirely on the statistical validity of the boundary detection. Without clear significance thresholds, multiple testing correction, and systematic validation on known negative and positive controls, the claim of non-random modular organization cannot be evaluated. The generalizability claim about folded domains requires analysis of a larger and more diverse protein set.
- **Resolution test** Provide a clear description of the null model, the z-score threshold used for significance, and multiple testing correction. Apply the method to a benchmark set of at least 20-50 proteins with known domain structures and IDRs, and demonstrate that the method correctly identifies compositional boundaries in IDRs while not detecting them in folded domains. Report sensitivity and specificity metrics.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation and benchmarking
- **Claim pointer** "local compositional bias is pervasive amongst IDRs and bestows disordered sequences with a modular architecture"
- **Evidence pointer** Section 2.3, Figure 3A-E
- **Concern** The manuscript claims that modularity is "pervasive" based on analysis of only six additional proteins (TDP-43, Spt6, Nucleolin, KMT2B, RNase E, plus FUS and Orc1 from earlier sections). This is a very small sample from which to draw generalizable conclusions about IDR organization across the proteome. Furthermore, there is no quantitative comparison to existing IDR annotation methods (e.g., IUPred, DISOPRED, PLAAC) or to existing compositional bias detection tools. The claim that the method identifies modules "not annotated in Uniprot" is presented as a strength, but without validation that these novel modules correspond to functional or structural features, this could simply reflect over-segmentation of the sequence.
- **Why it matters** The manuscript's central claim is that modular architecture is a generalizable organizational principle of IDRs. A sample of 7-8 proteins is insufficient to establish this. Without benchmarking against existing methods and without functional validation of identified modules, the biological significance of the findings remains speculative.
- **Resolution test** Expand the analysis to a large, diverse dataset of IDRs (e.g., at least 100-500 proteins from different functional classes and organisms). Compare the method's performance to existing IDR sub-classification tools. Provide evidence that identified modules correlate with known functional features (e.g., post-translational modification sites, protein-protein interaction interfaces, disease-associated mutations) beyond the single TDP-43 example.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Methodological robustness
- **Claim pointer** "The Chi-Score Analysis... can identify sequence-spanning compositional heterogeneity to parse a protein sequence into regions of distinct amino acid composition, regardless of what those compositions are"
- **Evidence pointer** Section 2.1, Figure 1A, Section 4.2
- **Concern** The method relies on several parameters that are not systematically evaluated: the choice of window sizes (6-22, even integers only), the insulation score window size, the clustering approach for boundaries across window sizes, and the iterative removal criteria for low-scoring boundaries. The manuscript does not report how sensitive the results are to these parameter choices. Additionally, the method's performance on sequences with gradual compositional transitions (as opposed to sharp boundaries) is not addressed. The language discrimination example (Figure 1B) is a useful proof-of-concept but does not establish performance on protein sequences where compositional differences may be more subtle.
- **Why it matters** Parameter sensitivity directly affects the reliability and reproducibility of the method. If results change dramatically with different parameter choices, the biological conclusions may not be robust. The method's ability to handle gradual transitions is important for real IDRs where compositional boundaries may not be sharp.
- **Resolution test** Perform a systematic parameter sweep (window sizes, insulation window sizes, clustering thresholds) on a test set of sequences with known compositional boundaries. Report the stability of identified boundaries across parameter choices. Test the method on simulated sequences with known gradual and sharp compositional transitions to characterize its resolution and limitations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Biological significance
- **Claim pointer** "individual IDR modules and their combinations may represent the functional analog of the globular protein's domain"
- **Evidence pointer** Section 3, Figure 3F
- **Concern** The manuscript proposes that modules are functionally significant units analogous to domains, but provides limited functional evidence. The TDP-43 example identifies a module corresponding to the amyloidogenic core, and the Spt6 example connects alternating charge modules to phase separation, but these are only two examples. The claim that modules "may represent the functional analog of the globular protein's domain" is highly speculative and not supported by systematic functional analysis. The manuscript does not address whether modules are evolutionarily conserved, whether they correspond to genetic recombination units, or whether they have independent biophysical properties.
- **Why it matters** The proposed analogy to globular domains is a strong claim with significant implications for how the field views IDR organization. Without systematic evidence for functional independence, evolutionary conservation, or genetic mobility of modules, this claim remains speculative and could mislead future research directions.
- **Resolution test** Provide additional functional validation across multiple proteins. Test whether modules are evolutionarily conserved across orthologs. Investigate whether modules can function independently when expressed in isolation. Analyze whether module boundaries correspond to intron-exon boundaries or recombination hotspots, which would support the domain analogy.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section 4.1
- **Evidence pointer** Section 4.1
- **Issue** The description of the Chi-Square test application is incomplete. The manuscript states that "the test statistic is normalized between zero and 1" but does not provide the exact normalization formula or explain how the maximum possible score is calculated for sequences of different lengths. The equation for the expected value is referenced but not shown in the text provided.
- **Required correction** Provide the complete mathematical formulation for the Chi-Square test statistic, the normalization procedure, and the calculation of the maximum possible score. Include the actual equations in the methods section.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section 4.2
- **Evidence pointer** Section 4.2
- **Issue** The description of the boundary clustering and optimization procedure is vague. The manuscript states that boundaries are "clustered by residue proximity" and that "optimal boundary positions are determined by selecting the placements within each group that maximize the mean chi-score" but does not specify the clustering algorithm, the distance threshold for clustering, or the optimization procedure.
- **Required correction** Provide a detailed algorithmic description of the clustering and optimization steps, including any parameters and thresholds used. Pseudocode or a flowchart would be helpful.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure 1B
- **Evidence pointer** Section 2.1, Figure 1B
- **Issue** The language discrimination example is described as demonstrating the method's effectiveness, but the manuscript does not report quantitative metrics for this analysis. It is unclear how well the method performed in terms of correctly identifying language boundaries.
- **Required correction** Provide quantitative results for the language discrimination test, such as the number of correctly identified boundaries, the precision and recall of language identification, or a confusion matrix.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2.3
- **Evidence pointer** Section 2.3, Figure 3A-E
- **Issue** The manuscript states that "local compositional bias appears largely absent from folded domains, at least for the proteins under consideration here" but does not provide a systematic analysis of folded domains. The figure supplement is referenced but not visible in the provided material.
- **Required correction** Provide a clear description of the folded domain analysis, including the number of domains analyzed, the criteria for determining absence of modularity, and representative examples.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Section 2.2, Table 1
- **Evidence pointer** Section 2.2, Table 1
- **Issue** The manuscript states that "a more careful investigation of module sequences reveals greater complexity than a simple alternation of charge, with non-charged residues also being differentially patterned" but does not elaborate on what these patterns are or how they were identified.
- **Required correction** Provide a more detailed analysis of the module sequences, including specific examples of non-charged residue patterning and how this contributes to module identity.

## Risk / unsupported claims
- The claim that "local compositional bias is an organizational principle unique to disordered sequences" is unsupported, as it is based on analysis of only one folded domain set (Orc1) and the figure supplement is not visible in the provided material.
- The claim that modularity is "pervasive amongst IDRs" is unsupported, as it is based on only 7-8 proteins.
- The claim that modules "may represent the functional analog of the globular protein's domain" is speculative and not supported by systematic functional evidence.
- The claim that the method identifies modules "not annotated in Uniprot" is presented without validation that these novel modules have biological significance.
- The statistical significance of identified boundaries cannot be fully evaluated without details on the z-score threshold, multiple testing correction, and null model construction.
- The performance of the method compared to existing IDR annotation and compositional bias detection tools is not assessed.
- The biological relevance of modules is only demonstrated for TDP-43 (amyloidogenic core) and Spt6 (phase separation), which is insufficient to support generalizable conclusions.