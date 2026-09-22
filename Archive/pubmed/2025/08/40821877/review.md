## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, limitations, conclusion, data availability)
- **Assessment boundary** Bioinformatics-based structural analysis of CYP1B1 intrinsic disorder and its correlation with predicted pathogenicity of missense mutations in primary congenital glaucoma
- **Shared manuscript claim summary** The authors report that CYP1B1 contains intrinsically disordered regions (IDPRs), that disorder decreases exponentially relative to AlphaMissense-predicted pathogenicity (R² = 0.62), and that these features may explain variable clinical outcomes in primary congenital glaucoma and offer therapeutic targets
- **Visible evidence base** Methods and Results sections describing use of UniProt, AlphaFold2, AlphaMissense, PONDR predictors via RIDAO, FuzDrop, D2P2, and STRING; figures referenced (Figs. 1–7) but not provided
- **Missing materials affecting confidence** Figures 1–7 not available for inspection; no supplementary data files; no raw numerical outputs from prediction tools; no statistical software details or code; no accession numbers for STRING network analysis

## Reviewer
- **Overall assessment** This manuscript presents a descriptive bioinformatics analysis of intrinsic disorder in CYP1B1 and its relationship to predicted pathogenicity of missense mutations. The topic is potentially relevant to the congenital glaucoma community, and the application of multiple disorder predictors is methodologically reasonable. However, the study is entirely computational and descriptive, with no experimental validation. The central correlation finding (R² = 0.62) is presented without confidence intervals or formal hypothesis testing. The clinical implications stated in the abstract and discussion substantially exceed what the data can support. The manuscript would benefit from clearer presentation of methods, inclusion of figure content in the text, and tempering of claims about therapeutic relevance.
- **Who would be interested in the results, and why** Researchers studying CYP1B1 structure-function relationships, clinicians and geneticists interested in primary congenital glaucoma genotype-phenotype correlations, and computational biologists working on intrinsic disorder prediction. The potential link between disorder and mutation pathogenicity could inform variant interpretation efforts, though this remains speculative.
- **Major strengths** 1) Addresses a relatively unexplored aspect of CYP1B1 biology (intrinsic disorder) in the context of PCG. 2) Uses multiple complementary bioinformatics tools for disorder prediction. 3) Integrates structural (AlphaFold2), pathogenicity (AlphaMissense), and interaction network (STRING) analyses. 4) Discusses specific founder mutations in relation to predicted disorder, providing concrete examples.
- **Major Concerns** 1) The central quantitative claim (exponential decay, R² = 0.62) lacks statistical rigor. 2) The manuscript claims clinical relevance and therapeutic implications that are not supported by computational predictions alone. 3) The analysis of specific mutations is post hoc and descriptive, without systematic testing. 4) The relationship between disorder and pathogenicity is presented as a general principle but may be an artifact of the specific prediction tools used. 5) The protein-protein interaction network analysis is presented without functional enrichment or pathway context.
- **Minor Comments** 1) The abstract states "spaghetti-like entities" which is informal for a scientific manuscript. 2) The introduction contains extensive background on PCG that could be condensed. 3) The methods section is written at a high level without sufficient detail for reproducibility. 4) The discussion speculates about gene therapy without direct evidence. 5) Figure 7 is mentioned in the text but not described. 6) The limitations section is brief and does not address the lack of experimental validation adequately.
- **Technical failings that need to be addressed before the case is established** The correlation analysis between disorder and pathogenicity needs formal statistical treatment including confidence intervals, appropriate hypothesis testing, and sensitivity analysis. The manuscript should clarify whether the exponential decay model was pre-specified or selected post hoc. The claim that "disorder decreases exponentially relative to predicted pathogenicity" requires demonstration that this relationship is not driven by a few influential points or by the specific choice of smoothing window.
- **Assessment against Nature-style criteria** Originality: Moderate. The application of disorder analysis to CYP1B1 in PCG is novel, but the general concept of disorder-pathogenicity correlations has been explored in other proteins. Scientific importance: Limited at present. The findings are descriptive and do not establish a mechanistic link between disorder and PCG pathogenesis. Interdisciplinary readership: The manuscript may appeal to structural biologists, ophthalmology researchers, and bioinformaticians, but the clinical framing may overstate relevance for a broad audience. Technical soundness: The computational methods are appropriate but the statistical analysis of the central correlation is insufficient. Readability for nonspecialists: The manuscript is generally readable but includes some informal language and would benefit from clearer explanation of disorder concepts for a clinical audience.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript presents a descriptive computational analysis with a central correlation claim that lacks statistical rigor. The clinical and therapeutic implications are overstated relative to the evidence. Substantial revision and additional analysis would be needed to support the claims made.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor of central claim
- **Claim pointer** "Correlation analysis showed that disorder decreases exponentially relative to AlphaMissense predicted pathogenicity, with an exponential decay fit (R² = 0.62)"
- **Evidence pointer** Results, "Correlation analysis between disorder and pathogenicity" section; Figure 4
- **Concern** The central quantitative finding of the manuscript is an exponential decay relationship between disorder and pathogenicity with R² = 0.62. However, no confidence intervals, p-values, or formal goodness-of-fit tests are reported. The manuscript does not state whether the exponential model was pre-specified or selected after examining the data. The smoothing approach (moving mean with window of ten residues) may introduce autocorrelation that inflates the apparent fit. The analysis appears to treat each residue as an independent observation, which is inappropriate given the local correlation structure of protein sequences.
- **Why it matters** The entire premise of the manuscript rests on this correlation. Without proper statistical treatment, the claim that "highly disordered regions tend to harbor benign mutations" is not established. Overinterpretation of a descriptive correlation could mislead readers about the strength of evidence for a disorder-pathogenicity relationship in CYP1B1.
- **Resolution test** Provide formal statistical analysis including: (1) confidence intervals for the exponential decay parameters, (2) a test of whether the exponential model significantly outperforms a null model (e.g., no relationship), (3) sensitivity analysis varying the smoothing window, (4) appropriate handling of non-independence of neighboring residues (e.g., block bootstrap or mixed-effects model), and (5) assessment of influential points.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Overstated clinical and therapeutic implications
- **Claim pointer** "These insights enhance our understanding of the molecular basis of PCG and offer potential targets for novel therapeutic interventions to combat this blinding childhood disorder" (Abstract); "these structural domains could provide novel targets for gene therapy" (Discussion)
- **Evidence pointer** Abstract; Discussion, final paragraphs
- **Concern** The manuscript claims that identifying IDPRs in CYP1B1 "offers potential targets for novel therapeutic interventions" and discusses gene therapy directed at these regions. However, the study is purely computational and provides no experimental evidence that IDPRs in CYP1B1 are functionally relevant to PCG pathogenesis, that modulating them would alter disease course, or that they represent druggable targets. The leap from descriptive bioinformatics to therapeutic implications is not justified.
- **Why it matters** Overstating clinical relevance can mislead readers, particularly clinicians and patients, about the readiness of these findings for translation. It also distracts from the actual contribution of the manuscript, which is a descriptive structural analysis.
- **Resolution test** Either remove or substantially temper claims about therapeutic implications, or provide a clear rationale for how IDPRs in CYP1B1 could be targeted based on existing evidence. The discussion should clearly distinguish between speculation and evidence-based conclusions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Post hoc interpretation of specific mutations
- **Claim pointer** "The most common mutation found is p.Gly61Glu... According to our RIDO analysis, residue 61 is in an ordered region... This mutation from a disordered residue (Gly) to a more disordered residue (Glu) in an order-promoting region may contribute to pathogenesis" (Discussion)
- **Evidence pointer** Discussion, paragraph on founder mutations
- **Concern** The manuscript discusses four specific founder mutations (p.Gly61Glu, p.Glu387Lys, p.Arg390His, p.Val320Leu) and interprets their pathogenicity in terms of disorder properties. However, these interpretations are entirely post hoc and are not tested against a null distribution. For example, the claim that p.Gly61Glu "may contribute to pathogenesis" because it changes a disordered residue to a more disordered residue in an ordered region is speculative. The manuscript does not compare these mutations to benign variants in the same regions or test whether the observed patterns are statistically significant.
- **Why it matters** Post hoc interpretations of specific cases can be misleading, especially when they are presented as supporting evidence for the general correlation claim. Without a systematic analysis, the reader cannot assess whether these examples are representative or cherry-picked.
- **Resolution test** Either present a systematic analysis of all known PCG-associated missense mutations in CYP1B1 (e.g., from ClinVar or a curated database) comparing disorder properties of pathogenic versus benign variants, or clearly label the discussion of specific mutations as illustrative speculation rather than evidence.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Incomplete description of methods for reproducibility
- **Claim pointer** "We utilized an approach to integrate various computational tools and databases" (Methods)
- **Evidence pointer** Methods section, all subsections
- **Concern** The methods section is written at a high level without sufficient detail for reproducibility. For example: (1) The exact version and parameters for each disorder prediction tool are not specified. (2) The procedure for calculating "average AlphaMissense pathogenicity score for each residue" is not described (e.g., how many variants per residue were averaged, how ambiguous scores were handled). (3) The STRING analysis parameters (e.g., network type, confidence score threshold justification) are incomplete. (4) The statistical methods for the correlation analysis are not described in the Methods section at all.
- **Why it matters** Reproducibility is a core requirement for scientific manuscripts. Without detailed methods, other researchers cannot replicate or build upon this work. The lack of statistical methods description is particularly problematic given the centrality of the correlation claim.
- **Resolution test** Provide a detailed methods section including: (1) software versions and URLs for all tools, (2) exact parameters used, (3) description of how average pathogenicity scores were computed, (4) full statistical methods including model specification and software used, (5) details of STRING analysis including any filtering steps.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Language and terminology
- **Affected element** Abstract, Results
- **Evidence pointer** Abstract, "spaghetti-like entities"; Results, "string, spaghetti-like segments"
- **Issue** The term "spaghetti-like" is informal and not standard scientific terminology for describing disordered regions. It may be appropriate for a general audience but is out of place in a technical manuscript.
- **Required correction** Replace with more precise terminology such as "extended, flexible regions" or "unstructured segments" and reserve informal analogies for explanatory text if needed.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Figure referencing
- **Affected element** Results, "Protein–protein interaction network" section
- **Evidence pointer** Results, final paragraph; "Figure 7" mentioned without description
- **Issue** Figure 7 is referenced in the text but no description of its content is provided. It is unclear what this figure shows and how it relates to the STRING analysis described in the preceding sentences.
- **Required correction** Either describe Figure 7 in the text or remove the reference if it is not essential.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Consistency of disorder classification
- **Affected element** Results, "Prediction of disorder using commonly used predictors" section
- **Issue** The manuscript reports that CYP1B1 is "moderately disordered" by PONDR VLXT (15.65%) and VSL2 (17.86%), but "highly ordered" by PONDR VL3 (8.47%), FIT (8.29%), IUPred-Long (1.10%), and IUPred-Short (2.39%). The discrepancy between predictors is not discussed. The classification thresholds are arbitrary and the implications of divergent predictions are not addressed.
- **Required correction** Add a brief discussion of the variability between predictors and its implications for the interpretation of disorder in CYP1B1. Consider whether a consensus approach would be more appropriate.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data availability statement
- **Affected element** Data availability section
- **Issue** The statement "No datasets were generated or analysed during the current study" is technically correct for a computational study using public databases, but it is misleading because the authors did generate derived data (e.g., disorder scores, pathogenicity averages, STRING network) that are not publicly available.
- **Required correction** Clarify that all source data are from public databases and provide access to derived data or state that derived data are available upon request.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reference to "RIDO" vs "RIDAO"
- **Affected element** Discussion, paragraph on founder mutations
- **Evidence pointer** Discussion, "According to our RIDO analysis"
- **Issue** The tool is introduced as "RIDAO" in the Methods section but referred to as "RIDO" in the Discussion. This inconsistency could confuse readers.
- **Required correction** Use the correct acronym consistently throughout the manuscript.

## Risk / unsupported claims
- The claim that IDPRs in CYP1B1 "may buffer against deleterious effects" and "provide a possible explanation for the variability in clinical outcomes" is speculative and not directly supported by the data presented. The correlation between disorder and pathogenicity does not establish a buffering mechanism.
- The statement that "these insights... offer potential targets for novel therapeutic interventions" is unsupported by any experimental evidence or mechanistic rationale.
- The interpretation of specific founder mutations (p.Gly61Glu, p.Glu387Lys, p.Arg390His, p.Val320Leu) in terms of disorder properties is post hoc and not systematically tested.
- The claim that the STRING network "underscores the significance of CYP1B1's interactions in the cellular context and its implications in ocular development and pathologies" is overstated; network statistics alone do not establish biological significance.
- The assertion that this is "one of the first studies to predict the pathogenicity of the missense mutations seen in CYP1B1" is difficult to evaluate without a literature search, and the phrasing is vague.