## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) as provided
- **Assessment boundary** Scientific claims, methodology, data interpretation, and internal consistency based solely on the supplied text
- **Shared manuscript claim summary** The authors use molecular dynamics simulations of 20 fibril structures from 6 proteins to show that post-translational modification sites are enriched in hydrophilic cavities of amyloid fibrils, that these sites have longer hydrogen bond lifetimes with confined water, and that hydrophobic mutations at cavity sites correlate with increased toxicity and aggregation in alpha-synuclein, with similar features observed in tau, FUS, and TDP-43.
- **Visible evidence base** Figures 1–6 referenced; Supplemental Tables T1–T3; Supplemental Figures S1–S7; statistical methods described in Methods section
- **Missing materials affecting confidence** Figure panels and actual data values not provided; Supplemental Tables and Figures not accessible; specific numerical results (means, confidence intervals, p-values) not included in text; simulation parameters for non-aSyn proteins not fully detailed; criteria for cavity detection thresholds not specified

## Reviewer
- **Overall assessment** The manuscript presents a potentially interesting hypothesis that PTM sites in amyloid fibril cavities are functionally relevant through hydration effects. The extension from prior aSyn work to multiple neurodegeneration-associated proteins is a reasonable direction. However, the evidence as presented is largely correlative, with several analytical steps that require clearer justification and quantitative support. The central claim that cavity PTM sites have exceptional hydrogen bond properties and that this generalizes across proteins is not fully established from the provided material, particularly given the limited description of methods for the non-aSyn systems and the absence of key numerical data.
- **Who would be interested in the results, and why** Researchers studying amyloid structure, protein aggregation mechanisms, post-translational modification biology, and computational biophysics of intrinsically disordered proteins. The potential link between hydration, PTM sites, and aggregation outcomes could inform therapeutic strategies targeting modification enzymes or fibril surfaces.
- **Major strengths** The study addresses a novel and mechanistically plausible connection between fibril cavity hydration and PTM site function. The use of multiple aSyn polymorphs and extension to other disease proteins adds breadth. The integration of published deep mutational scanning and aggregation rate datasets with structural simulations is a creative approach. The authors are appropriately cautious in some interpretations and acknowledge the need for experimental validation.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (cavity detection criteria), R1-M2 (hydrogen bond lifetime methodology), R1-M3 (statistical treatment of aggregated data), R1-M4 (generalization to other proteins)
- **Assessment against Nature-style criteria** Originality: moderate to high, as the specific link between cavity hydration and PTM sites is not widely explored. Scientific importance: potentially significant if the claims are robust, but current evidence is insufficient to establish broad relevance. Interdisciplinary readership: the topic bridges structural biology, biophysics, and neurodegeneration, which could attract a broad audience, but the presentation is heavily computational and may not be accessible to experimentalists without clearer biological framing. Technical soundness: several methodological details are under-specified, and the statistical approach for key comparisons is not fully rigorous as described. Readability for nonspecialists: the manuscript is generally clear but relies on specialized terminology and would benefit from more explicit explanation of cavity concepts and their biological relevance.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding cavity detection, HBL calculations, and statistical rigor. Currently not fully established from the provided evidence.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodology
- **Claim pointer** The authors claim that hydrophilic cavities are present across all 8 aSyn polymorphs and 5 additional proteins, and that cavity residues are enriched in PTM sites.
- **Evidence pointer** Results section "aSyn fibril cavities are present across 8 distinct polymorphs"; Methods section "Cavity amino acid detection, volume, KD hydropathicity, hbonds and RMSD"
- **Concern** The criteria for defining a "cavity" using the ANA2 package are not described in sufficient detail. The authors state that cavities were detected using the last 25 ns of simulation but do not specify the geometric or energetic thresholds used by ANA2 to identify cavities, nor how the boundary between cavity and non-cavity residues was determined. Without this information, the classification of residues as cavity or non-cavity cannot be reproduced or evaluated. This is a foundational issue, as all subsequent analyses depend on this binary classification.
- **Why it matters** If the cavity definition is arbitrary or overly permissive, the reported enrichment of PTM sites and the differences in hydrogen bond lifetimes could be artifacts of the classification scheme rather than genuine biophysical features. Reproducibility is a core expectation for computational studies.
- **Resolution test** Provide explicit parameters used in ANA2 (e.g., probe radius, minimum cavity volume, definition of lining residues). Ideally, show sensitivity analysis demonstrating that results are robust to reasonable variations in these parameters. Alternatively, provide a validation against an independent cavity detection method.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodology
- **Claim pointer** The authors claim that PTM sites within cavities have hydrogen bond lifetimes approximately three-fold greater than non-PTM cavity sites, and that cavity residues generally have longer HBLs than non-cavity residues.
- **Evidence pointer** Results section "PTM sites within aSyn fibril cavities have largest hydrogen bond lifetimes to solvent water"; Methods section "Hydrogen bond analysis"
- **Concern** The hydrogen bond lifetime calculation is described only briefly. The authors reference "Equations 1–3" but these are not provided in the manuscript text. The autocorrelation function approach is standard, but the specific implementation (e.g., definition of a hydrogen bond, time window, treatment of intermittent vs. continuous lifetimes) is not fully specified. Additionally, the authors state that HBLs were calculated using a 30 ps sliding window, but it is unclear how this window length was chosen and whether results are sensitive to this choice. The comparison between cavity and non-cavity HBLs is presented as a global average, but the distribution of HBLs across residues is not shown, making it difficult to assess whether the reported differences are driven by outliers.
- **Why it matters** Hydrogen bond lifetimes are central to the mechanistic claim that cavity PTM sites have exceptional hydration properties. If the calculation is not robust or the comparison is not statistically sound, the central conclusion is weakened. The lack of equations and distribution data prevents independent evaluation.
- **Resolution test** Provide the full equations and algorithmic details for HBL calculation. Show distributions of HBLs (e.g., box plots or histograms) for cavity vs. non-cavity and PTM vs. non-PTM residues, with statistical test results. Demonstrate that the reported differences are not sensitive to the choice of time window or hydrogen bond definition.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors claim that hydrophobic mutations in cavity residues have a larger effect on fitness and aggregation rate than mutations in non-cavity residues, supported by odds ratios of ~12 and ~3 for cavity vs. NAC comparisons.
- **Evidence pointer** Results section "Hydrophobic and not hydrophilic mutations in aSyn fibril cavities cause enhanced toxicity" and "Mutations within aSyn fibril cavities are more sensitive to increases in hydrophobicity"; Methods section "Statistical analysis"
- **Concern** The statistical analysis as described has several potential issues. First, the authors use a global average to dichotomize residues into low and high fitness groups, but this approach can introduce bias if the distribution is skewed. Second, the odds ratios are reported with confidence intervals referenced in figure captions, but the actual values are not provided in the text, preventing assessment of precision. Third, the comparison between cavity and NAC groupings involves overlapping residue sets, and it is unclear how the authors accounted for this non-independence. Fourth, the linear regression in Figure 5A appears to treat each mutation as an independent data point, but mutations at the same residue are not independent, which could inflate significance. Finally, the aggregation rate dataset from Pancoe et al. covers only ~5% of the mutational landscape, and the authors acknowledge the wide confidence intervals, but the implications for the strength of the conclusion are not discussed.
- **Why it matters** The claim that cavity residues are particularly sensitive to hydrophobic mutations is a key translational finding. If the statistical treatment is flawed, the conclusion may not be supported. Overlapping residue sets and non-independent data points are common pitfalls in mutational scanning analyses that require appropriate mixed-effects models or permutation-based approaches.
- **Resolution test** Provide the actual odds ratios with confidence intervals. Describe how non-independence of mutations at the same residue was handled. Consider using a mixed-effects model with residue as a random effect. Show that the results are robust to the dichotomization threshold. For the aggregation data, discuss the limitations of the small sample size more explicitly.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability
- **Claim pointer** The authors claim that tau, FUS, and TDP-43 fibrils recapitulate the PTM enrichment in cavities observed in aSyn, and that this suggests a common role of PTMs in hydrated fibril cavities.
- **Evidence pointer** Results section "Cavities with PTM sites are present in other neurodegenerative disease-related amyloid fibrils"; Figure 6
- **Concern** The extension to other proteins is based on simulations of 12 additional structures, but the details of these simulations are not provided in the main text. The authors state that all proteins contain hydrophilic cavities with PTM or familial mutation sites, but the criteria for identifying cavities in these systems are not described separately from the aSyn analysis. The number of PTM sites per protein is small (often one or a few), and the statistical power to claim enrichment is limited. Additionally, the authors note that prion and hnRNPA1 did not show PTM sites in cavities, which is a potential counterexample that is not discussed in depth. The claim of a "common role" requires stronger evidence across a larger and more diverse set of proteins.
- **Why it matters** The generalizability of the finding is central to the manuscript's broader significance. If the observation is limited to a subset of proteins or is driven by a small number of sites, the claim of a common mechanism is overstated.
- **Resolution test** Provide detailed simulation and cavity detection parameters for each non-aSyn protein. Report the number of PTM sites identified in cavities for each protein and the statistical significance of enrichment relative to the total number of PTM sites in the fibril. Discuss the negative results for prion and hnRNPA1 explicitly, including possible reasons for the absence of PTM sites in cavities.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "hydration plays a crucial role in the refolding of intrinsically disordered proteins into amyloid fibrils" is somewhat vague. The authors likely mean that water interactions influence the conformational conversion, but "refolding" implies a specific folding pathway that may not be accurate for all IDPs.
- **Required correction** Rephrase to "Hydration plays a crucial role in the conformational conversion of intrinsically disordered proteins into amyloid fibrils" or similar.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Results section "aSyn fibril cavities are present across 8 distinct polymorphs"
- **Evidence pointer** Figure 1
- **Issue** The figure is described as showing cavity volumes in gray, green, and red, but the text does not explain what these colors represent or how the volumes were calculated. The reader is left to infer the meaning.
- **Required correction** Add a sentence in the text or figure legend explaining the color coding and the volume calculation method.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion, paragraph 2
- **Evidence pointer** Discussion, "It is important to note that waters within hydrophilic cavities experience elevated HBLs due to confinement."
- **Issue** The authors attribute elevated HBLs to confinement, but this is an assumption. Confinement can also reduce mobility and thus increase HBLs, but the relationship is not always straightforward. The authors should either provide a citation for this claim or soften the language.
- **Required correction** Add a reference or rephrase to "waters within hydrophilic cavities may experience elevated HBLs due to confinement, consistent with previous observations."

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods section "MD simulations of amyloid fibrils"
- **Evidence pointer** Methods, first paragraph
- **Issue** The authors state that simulations were conducted "following the exact workflow detailed previously" but do not provide the key parameters (e.g., simulation length, ensemble, thermostat/barostat settings) in the current manuscript. While referencing prior work is acceptable, the reader should not need to consult another paper to understand the basic setup.
- **Required correction** Briefly summarize the key simulation parameters in the current manuscript, even if a full description is available in the prior publication.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Methods section "Statistical analysis"
- **Evidence pointer** Methods, last paragraph
- **Issue** The authors state that "odds and likelihood ratios with 95% confidence intervals" were calculated, but the results are only referenced in figure captions. This makes it difficult to assess the precision of the estimates without accessing the figures.
- **Required correction** Provide the actual values in the text or in a table, or at minimum include them in the main text for the key comparisons.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Results section "Hydrophobic and not hydrophilic mutations in aSyn fibril cavities cause enhanced toxicity"
- **Evidence pointer** Figure 4
- **Issue** The title of this section is somewhat misleading. The data show that hydrophobic mutations at cavity sites have lower fitness, but the authors do not directly test whether hydrophilic mutations have no effect. The title overstates the finding.
- **Required correction** Rephrase to "Hydrophobic mutations in aSyn fibril cavities are associated with enhanced toxicity" or similar.

## Risk / unsupported claims
- The claim that cavity residues are more evolutionarily conserved than non-cavity residues is based on a single analysis with a reported ~14% difference, but the statistical significance and effect size are not fully reported in the text.
- The claim that PTM sites within cavities have three-fold longer HBLs than non-PTM cavity sites is presented without distribution data or statistical tests in the main text.
- The generalization of the PTM enrichment finding to tau, FUS, and TDP-43 is based on a small number of PTM sites per protein and lacks detailed statistical support.
- The statement that "cavities may be a common feature of fibril structures" based on preliminary inspection of non-neurological proteins is speculative and not supported by data presented in the manuscript.
- The therapeutic suggestions in the Discussion (e.g., using proximity-directed enzymes or PROTACs) are speculative and not directly supported by the data presented.