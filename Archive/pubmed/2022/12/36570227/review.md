## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the manuscript
- **Shared manuscript claim summary** The authors use unsupervised k-means clustering on six physicochemical and genomic features of 2,819 uncharacterized proteins from three Gram-negative "superbug" species to define six clusters. They report that these clusters differ in functional properties, workability, and proximity to known biomedical targets, and propose that this classification scheme can prioritize uncharacterized proteins for antibiotic target and vaccine development.
- **Visible evidence base** Abstract, Introduction, Experimental Section, Results, Discussion, figure legends (figures not fully visible), table 1 (referenced), supplementary tables (referenced but not provided)
- **Missing materials affecting confidence** Figures (only legends visible), supplementary tables S1-S4, full protein lists, structural models, and detailed bioinformatics outputs

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting approach to organizing the "dark proteome" of clinically critical pathogens using unsupervised machine learning. The feature selection is rational and the integration of multiple post-classification analyses (codon usage, operon membership, interactomics, solubility, structural coverage) adds depth. However, the study is largely descriptive and computational, with no experimental validation. The central claim that these clusters are "amenable for distinct scientific applications" rests on indirect correlations with known biomedical targets rather than direct functional evidence. Several methodological details are insufficiently described, and the lack of accessible figures and supplementary data limits full evaluation. The work may be of interest to researchers in antimicrobial discovery and computational biology, but the case for practical utility is not yet established.
- **Who would be interested in the results, and why** Researchers in antimicrobial drug discovery, vaccine development, and bacterial genomics may find the clustering scheme useful as a triage tool for prioritizing uncharacterized proteins. Computational biologists working on protein classification and feature-based approaches may also be interested. The work could inform experimental groups seeking novel targets in A. baumannii, K. pneumoniae, and P. aeruginosa.
- **Major strengths** 1) Addresses a relevant and understudied problem: the functional dark proteome of critical pathogens. 2) Uses a transparent, unsupervised approach with interpretable features. 3) Integrates multiple orthogonal data types (genomic, proteomic, structural, interactomic) to characterize clusters. 4) Provides a practical output: prioritized candidate lists for antibiotic targets and vaccine antigens. 5) The comparison with known biomedical targets (drug targets, antigens, virulence factors) is a useful benchmarking strategy.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (lack of experimental validation), R1-M2 (insufficient methodological detail for reproducibility), R1-M3 (cluster stability and robustness not demonstrated), R1-M4 (selection criteria for candidate targets not fully justified)
- **Assessment against Nature-style criteria** Originality: Moderate. The application of unsupervised clustering to hypothetical proteins is not entirely novel, but the specific focus on multidrug-resistant pathogens and the integration of biomedical application criteria adds a new angle. Scientific importance: Moderate. The work addresses a real gap but does not provide functional validation, limiting its immediate impact. Interdisciplinary readership: Moderate. The topic bridges microbiology, bioinformatics, and drug discovery, but the presentation is heavily computational. Technical soundness: Weak to moderate. The methodology is generally reasonable, but key details are missing and robustness is not demonstrated. Readability for nonspecialists: Weak. The manuscript assumes significant familiarity with bioinformatics and machine learning concepts; the abstract is dense and the results are not easily accessible to a broad audience.
- **Recommendation posture** Currently not established from the provided evidence. The conceptual framework is promising, but the lack of experimental validation, incomplete methodological transparency, and unaddressed robustness concerns prevent endorsement. Major revisions are required.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The authors claim that specific clusters are "amenable for distinct scientific applications," including antibiotic target identification and vaccine development, and that five proteins are "potential druggable targets" and eighteen are "strong B-cell and T-cell immunogen candidates."
- **Evidence pointer** Results sections "Clusters Show Distinct Distances to Biomedical Control Proteins" and "Examples of Uncharacterized Antibacterial Target Candidates"; Table 1; Figure 8; Figure 9
- **Concern** The central claim of practical utility is based entirely on computational predictions and indirect correlations. No experimental validation is provided for any of the proposed druggable targets or vaccine candidates. The druggability scores from DogSiteScorer and immunogenicity predictions from epitope prediction tools are in silico only and do not demonstrate actual binding, inhibition, or immune response. The proximity of cluster centroids to known biomedical targets is an interesting observation but does not establish functional equivalence.
- **Why it matters** The stated purpose of the study is to facilitate the exploration of uncharacterized proteins for therapeutic development. Without any experimental evidence, the claim that these proteins are "amenable" for such applications is speculative. The manuscript risks overstating the readiness of these candidates for downstream work.
- **Resolution test** Provide at least one experimental validation, such as expression and biochemical characterization of a predicted druggable target, or in vitro immunogenicity assay for a predicted vaccine candidate. Alternatively, temper the claims to clearly state that these are computational predictions requiring experimental follow-up.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The methods section describes the calculation of six clustering features and the k-means procedure, but several parameters and thresholds are not fully specified.
- **Evidence pointer** Experimental Section, "Calculation of Protein Clustering Features" and "Unsupervised Classification"
- **Concern** The description of the k-means procedure lacks critical details. The number of seeds (10) is mentioned, but the initialization method, convergence criteria, and number of iterations are not fully specified. The method for determining the optimal k (inter- vs intra-cluster distance) is described qualitatively, but the exact metric and threshold are not given. The robustness of the clustering to parameter choices is not assessed. The thresholds for defining "high" structural disorder, "low" species distribution, and "anomalous" AT content are not explicitly stated. The criteria for selecting the 12 antibacterial target candidates and the 18 vaccine candidates are described in the text but the full decision rules are not formalized.
- **Why it matters** Reproducibility is a core requirement for computational studies. Without complete methodological detail, other researchers cannot replicate the analysis or assess its validity. The lack of robustness testing raises concerns about whether the six clusters are stable or an artifact of specific parameter choices.
- **Resolution test** Provide a complete description of all parameters, thresholds, and decision rules. Include a robustness analysis (e.g., varying k, different initialization seeds, bootstrapping) to demonstrate cluster stability. Make the code and data publicly available.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "unsupervised learning renders six optimal clusters" and that these clusters are "natural."
- **Evidence pointer** Results section "Unsupervised Learning Renders Six Optimal Clusters"; Figure 2
- **Concern** The choice of k=6 is based on the "difference between the average of inter-cluster with respect to the average of intra-cluster distances." This is an unusual metric and its statistical properties are not described. No formal cluster validation indices (e.g., silhouette score, Davies-Bouldin index, gap statistic) are reported. The comparison with hierarchical clustering and DBSCAN is mentioned, but the results are only briefly described and the figure (Supporting Figure S1) is not available for evaluation. The claim that clusters are "natural" is not supported by any statistical test.
- **Why it matters** The entire study rests on the validity of the six-cluster solution. If the clustering is not robust or the number of clusters is not well-justified, all downstream analyses and conclusions are compromised.
- **Resolution test** Apply standard cluster validation metrics to justify the choice of k. Provide a more detailed comparison of clustering methods, including quantitative measures of agreement. Show that the six-cluster solution is stable across different subsamples of the data.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Claim support
- **Claim pointer** The authors state that Cluster 5 proteins are "likely spurious genes resulting from false positives by gene detection algorithms or part of mobile genetic elements, pseudogenes, or small untranslated RNAs."
- **Evidence pointer** Results section "Clusters Show Distinct Genetic Trends: Codon Usage and Presence in Operons"; Discussion
- **Concern** This is a strong claim based on indirect evidence (codon usage bias, low conservation, small size, absence from operons). While these features are consistent with spurious ORFs, they are not definitive. Some genuine small proteins or recently evolved genes could share these characteristics. The authors do not provide any direct evidence (e.g., ribosome profiling, mass spectrometry) to confirm that these ORFs are not translated.
- **Why it matters** If Cluster 5 proteins are dismissed as spurious, they will be excluded from future studies. If this classification is incorrect, potentially functional proteins could be overlooked. The claim should be framed as a hypothesis rather than a conclusion.
- **Resolution test** Soften the language to indicate that Cluster 5 proteins are "candidates for spurious ORFs" and suggest experimental validation (e.g., translation assays) to confirm their status.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract is dense and uses jargon without definition (e.g., "functional dark proteome," "nonworkable membrane proteins"). The key finding is not immediately clear to a non-specialist reader.
- **Required correction** Simplify the abstract, define key terms, and state the main conclusion more directly.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figures
- **Evidence pointer** Figures 1-9 (legends only)
- **Issue** The figures are not visible in the provided material, making it impossible to assess the quality of the visualizations or the validity of the data presentation.
- **Required correction** Ensure all figures are accessible and clearly labeled. Consider adding a summary figure that illustrates the overall workflow.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Supplementary materials
- **Evidence pointer** Supplementary Tables S1-S4
- **Issue** The supplementary tables are referenced but not provided. These are essential for evaluating the data, particularly the list of 2,819 proteins and their feature values.
- **Required correction** Make all supplementary materials available for review.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Language
- **Affected element** Throughout
- **Evidence pointer** Location not provided
- **Issue** The manuscript contains some awkward phrasing and grammatical errors that impede readability.
- **Required correction** Thorough language editing is recommended.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Context
- **Affected element** Introduction
- **Evidence pointer** Introduction
- **Issue** The introduction does not sufficiently discuss prior computational efforts to classify hypothetical proteins, making it difficult to assess the novelty of the approach.
- **Required correction** Add a brief review of existing classification schemes for uncharacterized proteins and clearly state the novelty of the present work.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Validation
- **Affected element** Results, "Clusters Show Distinct Distances to Biomedical Control Proteins"
- **Evidence pointer** Figure 7
- **Issue** The comparison with biomedical control proteins is based on distance to cluster centroids, but the statistical significance of these distances is not assessed. It is unclear whether the observed proximities are meaningful or could occur by chance.
- **Required correction** Add statistical tests (e.g., permutation tests) to assess the significance of the observed distances.

## Risk / unsupported claims
- The claim that five proteins are "potential druggable targets" is unsupported by experimental evidence; druggability scores are purely computational.
- The claim that eighteen proteins are "strong B-cell and T-cell immunogen candidates" is unsupported by experimental immunogenicity data.
- The claim that Cluster 5 proteins are "likely spurious" is a hypothesis, not a demonstrated conclusion.
- The claim that the six clusters are "natural" and "optimal" is not supported by formal cluster validation metrics.
- The generalizability of the clustering scheme to other bacterial species or strains is not demonstrated.
- The practical utility of the proposed scheme for guiding experimental work is not validated.