## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, experimental procedures, data availability, supplementary figure legends referenced but not provided)
- **Assessment boundary** Scientific soundness, technical rigor, internal consistency, and support of claims based solely on the provided manuscript text. Supplementary figures (Fig. S1-S7) and raw data referenced but not available for review.
- **Shared manuscript claim summary** The authors describe a pipeline for optimizing a single-domain antibody (VHH) targeting the PHF6 linear motif within the Tau intrinsically disordered protein. Starting from a parent VHH (Z70), random mutagenesis and yeast two-hybrid screening yielded variants with improved affinity (up to 23 nM), conserved epitope recognition, and variable effects on Tau aggregation inhibition. The authors conclude that affinity alone does not predict functional efficacy, and that a multi-assay pipeline (affinity, structure, stability, cellular aggregation) is required for rational selection of optimized VHHs.
- **Visible evidence base** Abstract, Introduction, Results (narrative), Discussion, Experimental Procedures, Data availability statement, Conflict of interest, Author contributions, Acknowledgements. No figures, tables, or supplementary materials were provided.
- **Missing materials affecting confidence** All figures (Fig. 1-10), supplementary figures (Fig. S1-S7), raw SPR sensorgrams, NMR spectra, crystallographic data validation reports, and statistical analysis details. Without these, quantitative claims cannot be independently verified.

## Reviewer

### Overall assessment
The manuscript presents a systematic and pragmatic approach to VHH optimization for targeting a linear epitope within an intrinsically disordered protein. The experimental pipeline is logical and the authors appropriately emphasize the importance of multi-parameter evaluation beyond affinity. However, the absence of all figures and supplementary data in the provided material severely limits the ability to assess the validity of the quantitative claims, the quality of the structural data, and the robustness of the statistical correlations. The narrative is coherent and the conclusions are cautiously stated, but several claims regarding structure-function relationships and predictive correlations require the missing evidence to be fully evaluated.

### Who would be interested in the results, and why
Researchers in the fields of antibody engineering, nanobody development, neurodegenerative disease therapeutics, and protein aggregation biology would find this work relevant. The emphasis on the disconnect between affinity and functional efficacy, and the importance of cellular stability, is of broad interest to those developing intracellular antibodies or biologics targeting aggregation-prone proteins. The structural insights into how framework mutations can modulate CDR loop dynamics and affinity may also interest structural biologists and protein engineers.

### Major Strengths
1. The manuscript addresses a clinically relevant and technically challenging problem: optimizing a VHH for intracellular use against a linear epitope in an intrinsically disordered protein.
2. The multi-assay pipeline (yeast two-hybrid, SPR, NMR, X-ray crystallography, thermal stability, cellular aggregation, seeding inhibition) is comprehensive and represents a rigorous approach to VHH characterization.
3. The authors honestly report that improved affinity does not always translate to improved functional efficacy, and they identify cellular stability as a critical parameter.
4. The structural analysis of three mutant VHHs in complex with the epitope peptide provides a molecular rationale for the observed affinity improvements.
5. The correlation analyses between thermal stability, cellular aggregation propensity, and functional efficacy are valuable and provide practical guidance for future VHH selection.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The authors claim that all eight selected mutants show improved affinity compared to Z70, with mutant 1 achieving the best overall affinity (23 nM), and that kinetic parameters (k_on, k_off) vary by mutant.
- **Evidence pointer** Figure 2, Figure S3; location not provided
- **Concern** The quantitative affinity and kinetic data are presented only as figure references. No numerical values, error estimates, replicates, or sensorgram quality assessments are visible in the provided text. The claim that mutant 1 has 23 nM affinity and that this is the best in the series cannot be verified without the actual SPR data and statistical analysis.
- **Why it matters** The central premise of the manuscript is that affinity optimization was achieved. Without verifiable quantitative data, the foundation of the entire study is unsubstantiated. Furthermore, the comparison of kinetic parameters across mutants is essential for the structure-function discussion.
- **Resolution test** Provide the SPR data in tabular form with mean ± SD, number of independent experiments, and representative sensorgrams. State the statistical test used to compare Kd values between mutants and Z70.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The authors claim that the NMR epitope mapping confirms conservation of the PHF6 motif as the main interaction site for all mutants, with the exception of mutant 15 where aggregation prevented definitive confirmation.
- **Evidence pointer** Figure 3B, Figure S4; location not provided
- **Concern** The NMR data are described only qualitatively. The intensity loss profiles are stated to be "well conserved" but no quantitative analysis, such as chemical shift perturbation values or intensity ratio thresholds, is provided. The claim that subtle differences are due to kinetics is speculative without supporting data. The exclusion of mutant 15 from definitive epitope confirmation is acknowledged, but the impact of this on the overall conclusion is not discussed.
- **Why it matters** Epitope conservation is critical for ensuring that the optimized VHHs retain the same binding site as the parent, which is essential for their intended mechanism of action. Without quantitative NMR analysis, the claim of epitope conservation is not rigorously supported.
- **Resolution test** Provide quantitative intensity ratio plots with statistical thresholds for significant perturbation. Show overlay spectra for at least one mutant vs. Z70. Discuss the implications of mutant 15's indeterminate epitope status.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The authors claim that the crystal structures of mutants 1, 3, and 20 in complex with the Tau[301-312] peptide show no major conformational differences from Z70, and that the G115E mutation tightens a flexible loop, potentially via a salt bridge with K47 in mutant 20.
- **Evidence pointer** Figure 4, Figure 5; location not provided
- **Concern** The structural analysis is presented without any crystallographic statistics. Resolution, R-work/R-free values are mentioned in the methods, but no electron density maps, B-factor analyses, or structural alignment figures are visible. The claim that E115 forms a salt bridge with K47 in mutant 20 is stated as a possibility, but the evidence for this interaction (e.g., distance measurements, electrostatic surface representations) is not shown. The functional significance of the loop tightening is inferred but not directly tested.
- **Why it matters** The structural data are used to rationalize the affinity improvements. Without proper validation of the structures and the specific interactions described, the mechanistic conclusions are not robust.
- **Resolution test** Provide crystallographic data collection and refinement statistics table. Show electron density for the mutated residues and the proposed salt bridge. Include a structural superposition figure with Z70. Consider mutational analysis to test the functional role of the proposed salt bridge.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The authors claim a strong correlation between thermal stability (Tm) and cellular aggregation propensity (Pearson r = -0.87), and between in vitro aggregation inhibition and cellular seeding inhibition (Pearson r = 0.78, or 0.87 without mutant 9).
- **Evidence pointer** Figure 7B, Figure 10; location not provided
- **Concern** The correlation coefficients are stated, but the underlying data points, the number of mutants included, and the statistical significance (p-values, confidence intervals) are not provided. The outlier status of mutant 9 is mentioned but not quantitatively justified. The claim that mutant 12 is an exception to the Tm-aggregation correlation is noted but not explored mechanistically.
- **Why it matters** These correlations are central to the authors' conclusion that a multi-assay pipeline is necessary. If the correlations are weak or driven by a few outliers, the conclusion may be overstated. The mechanistic basis for the exceptions is not addressed.
- **Resolution test** Provide scatter plots with all data points, regression lines, and 95% confidence intervals. Report p-values for all correlations. Discuss the mechanistic basis for the observed outliers.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The authors claim that mutants 1 and 3 are the best candidates for further in vivo testing based on their combined performance across all assays.
- **Evidence pointer** Figure 8, Figure 9, Figure 10; location not provided
- **Concern** The selection of mutants 1 and 3 as the final candidates is presented as the outcome of the pipeline, but the decision-making criteria are not explicitly defined. It is unclear whether the selection was based on a weighted scoring system, a threshold for each assay, or a qualitative assessment. The performance of mutant 20, which was specifically constructed to combine the two most common mutations, is not clearly compared to mutants 1 and 3 in the final recommendation.
- **Why it matters** The manuscript's practical value lies in its ability to guide VHH selection. Without transparent and reproducible selection criteria, the recommendation is not actionable.
- **Resolution test** Define the selection criteria explicitly. Provide a summary table of all mutants' performance across all assays. Justify the final choice of mutants 1 and 3 over mutant 20.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states that the optimized VHHs have "improved binding affinities" but does not provide the range of improvement or the best Kd value. The phrase "could not be predicted from their affinity alone" is somewhat vague.
- **Required correction** Include the range of Kd values for the optimized mutants and the Kd of Z70 for comparison. Specify the degree of improvement (e.g., "up to 6-fold").

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Internal consistency
- **Affected element** Results section, "Affinity measurement" subsection
- **Evidence pointer** Results, "Affinity measurement"; location not provided
- **Issue** The text states that mutant 5 and mutant 15 had only either k_off or k_on improved, respectively. However, the subsequent discussion of the correlation between affinity and efficacy does not explicitly address whether these mutants' functional performance was consistent with their kinetic profiles.
- **Required correction** Briefly discuss whether the kinetic differences (k_on vs. k_off improvements) had any observable impact on functional outcomes.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methodology
- **Affected element** Experimental Procedures, "Affinity measurement"
- **Evidence pointer** Experimental Procedures; location not provided
- **Issue** The SPR method describes single-cycle kinetics with regeneration between each VHH injection. This is unusual, as single-cycle kinetics typically does not include regeneration between analyte injections. The description may be ambiguous.
- **Required correction** Clarify whether regeneration was performed between each concentration step or only after the full cycle. If regeneration was used, specify the regeneration conditions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Results section, "Self-aggregation of the VHH-mCherry constructs in HEK293 cells"
- **Evidence pointer** Results, "Self-aggregation"; location not provided
- **Issue** The text states that "puncta" appear in a percentage of cells, but the criteria for defining a punctum and the number of cells counted per condition are not specified.
- **Required correction** Provide the quantification criteria and the total number of cells analyzed per condition.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Results section, "Inhibition of Tau seeding in HEK293 Tau repeat domain (RD) P301S FRET Biosensor reporter cells"
- **Evidence pointer** Results, "Inhibition of Tau seeding"; location not provided
- **Issue** The results are presented as mean ± SEM, but the number of independent experiments and the statistical test used to compare mutants to Z70 are not stated.
- **Required correction** State the number of independent experiments and the statistical test used. Report p-values for comparisons to Z70.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data availability statement
- **Evidence pointer** Data availability; location not provided
- **Issue** The statement says raw data are deposited in Zenodo, but the link is not provided in the text. The PDB access codes are given, but the Zenodo DOI is only in the footnote.
- **Required correction** Include the Zenodo DOI in the Data availability statement for clarity.

### Technical failings that need to be addressed before the case is established
1. **Missing quantitative SPR data** (R1-M1): The core claim of affinity improvement is unverifiable without the actual Kd, k_on, k_off values and their statistical analysis.
2. **Missing quantitative NMR analysis** (R1-M2): Epitope conservation is claimed but not quantitatively demonstrated.
3. **Missing crystallographic validation** (R1-M3): The structural interpretations require the full crystallographic statistics and electron density maps.
4. **Missing correlation statistics** (R1-M4): The Pearson correlation coefficients are stated without p-values, confidence intervals, or underlying data points.
5. **Undefined selection criteria** (R1-M5): The final recommendation of mutants 1 and 3 is not based on transparent, reproducible criteria.

### Assessment against Nature-style criteria
- **Originality**: Moderate. The application of a multi-assay pipeline to VHH optimization against a linear Tau epitope is not entirely novel, but the systematic comparison of affinity, stability, and functional efficacy provides a useful framework. The structural analysis of framework mutations affecting CDR dynamics is a valuable contribution.
- **Scientific importance**: Moderate. The work addresses a real challenge in developing intracellular antibodies for neurodegenerative diseases. However, the clinical relevance is indirect, and the improvements over the parent VHH are incremental. The conclusion that affinity alone is insufficient is important but not surprising.
- **Interdisciplinary readership**: Limited. The manuscript is primarily of interest to antibody engineers and structural biologists. The relevance to a broader neuroscience or clinical audience is not strongly articulated.
- **Technical soundness**: Cannot be fully assessed. The experimental design is logical, but the absence of all figures and quantitative data prevents verification of the claims. The statistical rigor of the correlation analyses is unclear.
- **Readability for nonspecialists**: Acceptable. The manuscript is clearly written, and the concepts are explained adequately. However, the lack of figures makes it difficult for any reader to follow the results.

### Recommendation posture
**Currently not established from the provided evidence.** The manuscript presents a well-conceived pipeline and a plausible narrative, but the complete absence of figures, tables, and supplementary data in the provided material makes it impossible to verify the quantitative claims, the structural interpretations, or the statistical correlations. The authors must provide the full dataset, including SPR values, NMR analysis, crystallographic statistics, and correlation plots, before the scientific case can be properly evaluated. If the missing data are consistent with the narrative, the manuscript could be considered for publication after major revisions.

## Risk / unsupported claims
1. **Claim that all eight mutants have improved affinity compared to Z70** - Unsupported without SPR data.
2. **Claim that mutant 1 has the best affinity (23 nM)** - Unsupported without SPR data.
3. **Claim that the NMR epitope mapping confirms PHF6 conservation for all mutants** - Unsupported without quantitative NMR analysis.
4. **Claim that the G115E mutation tightens the CDR3 loop via a salt bridge with K47 in mutant 20** - Unsupported without detailed structural evidence.
5. **Claim that thermal stability correlates with cellular aggregation propensity (r = -0.87)** - Unsupported without underlying data and statistical significance.
6. **Claim that in vitro aggregation inhibition correlates with cellular seeding inhibition (r = 0.78)** - Unsupported without underlying data and statistical significance.
7. **Claim that mutants 1 and 3 are the best candidates for in vivo testing** - Unsupported without defined selection criteria.
8. **Claim that the pipeline permits rational selection of optimized VHHs** - The concept is reasonable, but the evidence for its predictive power is incomplete.