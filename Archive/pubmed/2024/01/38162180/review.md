## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors investigate the N-terminal intrinsically disordered region (IDR) of the β-hexosyltransferase (BHT) from Hamamotoa singularis, using structural analysis (crystal structure, PDB: 7L74), in silico predictions, and functional assays of deletion and glycosylation mutants expressed in Komagataella phaffii. They conclude that the IDR partially influences secretion and membrane localization but is not essential for enzymatic activity or dimerization.
- **Visible evidence base** Crystal structure (PDB: 7L74), SAXS data (SASBDB: SASDN57, SASDN67), SEC data, kinetic measurements, Western blots, SDS-PAGE, in silico predictions (PSIPRED, GlobPlot, IUPred2A, DISOPRED3, PONDR, Phyre2, GlycoEP, DisPhos1.3)
- **Missing materials affecting confidence** Raw kinetic data (only kcat/Km reported in figure form), original Western blot and SDS-PAGE images, SEC chromatograms, SAXS scattering curves and fit parameters, detailed statistical analysis, plasmid construction maps, and full experimental replicates are not fully described in the provided text

## Reviewer

### Overall assessment
The manuscript addresses a focused question regarding the functional role of an N-terminal intrinsically disordered region in a biotechnologically relevant enzyme. The combination of structural and functional approaches is appropriate, and the crystal structure provides a useful contribution. However, the evidence supporting several key claims is incomplete or indirect. The conclusion that the IDR "partially influences" secretion is based on a single deletion construct showing a modest shift in localization ratio, and the mechanistic basis for this effect is not explored. The glycosylation mutagenesis data are presented as activity reductions but the interpretation that this reflects secretion defects rather than protein instability or expression differences is not fully supported by the data shown. The manuscript would benefit from more rigorous quantitative analysis and additional controls.

### Who would be interested in the results, and why
Researchers working on glycosyl hydrolases, protein secretion in yeast expression systems, and the structural biology of intrinsically disordered regions in enzymes. The biotechnological context (GOS production, human milk oligosaccharides) will also interest applied microbiologists and food biotechnologists. The structural data on a membrane-associated GH1 enzyme with an unusual N-terminal extension may be of interest to the glycoside hydrolase community.

### Major strengths
- The crystal structure of BHT (PDB: 7L74) is a valuable resource, particularly given the limited structural information on membrane-associated GH1 enzymes from basidiomycetous yeasts
- The combination of structural, biophysical (SAXS), and functional approaches is methodologically sound
- The systematic deletion strategy based on predicted disorder boundaries is logical and well-motivated
- The glycosylation site mutagenesis addresses an important question about PTM requirements for secretion
- The study provides practical insights for engineering this enzyme for improved soluble secretion

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "the disordered region only partially influences the secretion and membrane localization of BHT"
- **Evidence pointer** Table 4, Results section "Expression and secretion of truncated N-terminal rBHT variants"
- **Concern** The central claim that the IDR "partially influences" secretion is based on a comparison of localization ratios between variants, but the data presentation is incomplete. The manuscript reports a shift from 40% to 53% soluble fraction for rBHT(57-594) compared to shorter deletions, but no statistical analysis is provided, no replicate numbers are given, and the variability across experiments is not shown. Furthermore, the claim that the IDR is not essential for membrane interaction is based on the observation that all variants still partition between soluble and membrane-associated forms, but the mechanism by which the IDR contributes to this partitioning is not investigated. The conclusion is therefore underdetermined by the evidence presented.
- **Why it matters** The primary conclusion of the paper rests on this localization ratio data. Without proper statistical treatment and replication, the claim that the IDR "partially influences" secretion cannot be robustly established. This is the central finding that would justify the study's significance.
- **Resolution test** Provide quantitative data with at least three independent biological replicates, include statistical analysis (e.g., ANOVA with post-hoc tests), and show the distribution of individual data points. Additionally, perform a more detailed analysis of the membrane association mechanism, such as liposome binding assays or membrane fractionation with marker proteins, to directly test the IDR's role in membrane interaction.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "functional analysis of each glycosylation site found within the C-terminal domain revealed reduced total secreted protein activity by 58%–97% in both the presence and absence of the IDR, indicating that glycosylation at all four locations is required by the host for the secretion of active enzyme"
- **Evidence pointer** Table 4, Results section "Are N-glycans essential for secretion?"
- **Concern** The interpretation that reduced secreted activity reflects a secretion defect is confounded by potential effects on protein stability, folding, or intracellular degradation. The authors state that purified glycosylation mutants had "similar specific activities as the non-mutated forms," which suggests the mutations do not affect catalytic activity per se. However, the reduced secreted activity could be due to intracellular retention, ER-associated degradation, or reduced protein synthesis, none of which are directly assessed. The claim that glycosylation is "required by the host for the secretion of active enzyme" is too strong given that the authors did not measure secretion efficiency directly (e.g., by pulse-chase experiments or by measuring intracellular vs. extracellular protein levels).
- **Why it matters** The glycosylation results are presented as a major finding, but the mechanistic interpretation is not supported by the experimental design. If the mutations simply reduce protein stability, the conclusion would be different from a specific role in secretion. This distinction is important for understanding the biology and for practical applications in protein engineering.
- **Resolution test** Measure intracellular and extracellular protein levels by quantitative Western blot to distinguish between reduced secretion and reduced protein production/stability. Perform cycloheximide chase experiments to assess protein half-life. Alternatively, use a secretion reporter system (e.g., GFP fusion) to directly measure secretion efficiency independent of enzymatic activity.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Data interpretation
- **Claim pointer** "The confirmation of dimer formation of rBHT(23–594)-HIS, rBHT(32–594)-HIS, rBHT(54–594)-HIS, and rBHT(57–594)-HIS, suggested that the unstructured regions spanning residues 23–56 are not involved in dimerization"
- **Evidence pointer** Results section "Influence of N-terminal deletions on rBHT dimerization", Figure 6
- **Concern** The SEC data are described as showing a single peak at 12.5 min with calculated MW of 150 kDa, but the data are not shown ("Data not shown"). The SAXS data provide molecular mass estimates (~169 kDa) that are consistent with a dimer, but the comparison between SAXS-derived Rg/Dmax values and those calculated from the crystal structure shows discrepancies (39 Å vs 34 Å for Rg; 124 Å vs 110 Å for Dmax). The authors attribute this to the disordered N-terminus leading to a "more expanded dimer in solution," but this interpretation is speculative without additional validation, such as ensemble modeling or comparison with a construct lacking the IDR in SAXS.
- **Why it matters** The claim that the IDR is not involved in dimerization is important for understanding the structural role of this region. However, the evidence is indirect and the discrepancy between SAXS and crystal structure dimensions could also be explained by flexibility in other regions or by the presence of the His-tag. The conclusion would be strengthened by direct comparison of SAXS data for constructs with and without the IDR.
- **Resolution test** Perform SAXS analysis on a construct lacking the IDR (e.g., rBHT(57-594)) and compare the Rg and Dmax values directly. Alternatively, perform analytical ultracentrifugation to confirm dimerization across all variants. If the IDR is truly not involved in dimerization, the SAXS profiles of constructs with and without the IDR should show similar dimeric states with differences only in the disordered region.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility and completeness
- **Claim pointer** "The results of the respective kcat/km for all four truncated enzyme variants indicate a temperature optimum of 42°C"
- **Evidence pointer** Figure 4, Results section "Kinetic parameters of secreted rBHT variants"
- **Concern** The kinetic data are presented only in figure form, and the actual values, error bars, and statistical comparisons are not described in the text. The claim that all variants have "similar affinity" and "turnover activity" is not supported by any quantitative comparison. Additionally, the kinetic measurements were performed at four temperatures, but the rationale for choosing these temperatures and the number of replicates are not stated.
- **Why it matters** Kinetic parameters are central to the claim that the IDR does not affect catalytic activity. Without proper statistical treatment and reporting of the actual values, this claim cannot be evaluated. The temperature dependence data could also reveal differences in thermal stability that are not captured by the current analysis.
- **Resolution test** Provide a table with kinetic parameters (Km, kcat, kcat/Km) for each variant at each temperature, including standard errors and number of replicates. Perform statistical comparisons (e.g., two-way ANOVA) to test for differences between variants and temperatures. Report the raw data or make them available in a repository.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the IDR "may not be essential for stable homodimerization" based on in silico analysis, but the experimental data on dimerization are presented later. This creates a slight inconsistency in the logical flow.
- **Required correction** Rephrase to indicate that the in silico analysis suggested this possibility, which was then tested experimentally, or move the statement to the results section.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodology detail
- **Affected element** Materials and Methods, "Enzyme assays"
- **Evidence pointer** Materials and Methods section
- **Issue** The assay conditions for determining kinetic parameters are not fully described. The substrate concentration range, enzyme amount, reaction time, and buffer composition are not specified.
- **Required correction** Provide complete assay conditions, including substrate concentration range (relative to Km), enzyme concentration, reaction time, and buffer composition, to allow reproducibility.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 3
- **Evidence pointer** Results section "Expression and secretion of truncated N-terminal rBHT variants"
- **Issue** The Western blot and SDS-PAGE data are described but the figure itself is not available for review. The description mentions "barely visible" bands for some variants, which is subjective without the actual image.
- **Required correction** Ensure the figure is included with appropriate molecular weight markers and loading controls. Consider providing densitometry analysis to quantify band intensities.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** Multiple sections
- **Issue** The term "ß-hexosyltransferase" is used inconsistently with "β-hexosyltransferase" in different places. The enzyme is also referred to as BHT, BglA, and rBHT, which can be confusing.
- **Required correction** Standardize the terminology throughout the manuscript. Define all abbreviations at first use and use them consistently.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Table 4
- **Evidence pointer** Table 4
- **Issue** The table reports activity ratios and percentages, but no error estimates or statistical comparisons are provided.
- **Required correction** Add standard deviations or confidence intervals to all quantitative values in the table, and indicate which comparisons are statistically significant.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion of IDRs in membrane-associated proteins is brief and could benefit from more specific comparisons with other characterized systems where IDRs have been shown to modulate membrane binding or secretion.
- **Required correction** Expand the discussion to include specific examples from the literature and how the current findings compare or contrast with those systems.

### Technical failings that need to be addressed before the case is established
- R1-M1: Lack of statistical analysis and replication for the central localization ratio claim
- R1-M2: Confounded interpretation of glycosylation mutant phenotypes without direct secretion measurements
- R1-M3: Incomplete biophysical characterization of dimerization across variants
- R1-M4: Inadequate reporting of kinetic data

### Assessment against Nature-style criteria
- **Originality**: Moderate. The structural characterization of a membrane-associated GH1 enzyme with an N-terminal IDR is relatively novel, but the functional conclusions are incremental and do not reveal fundamentally new principles about IDR function or protein secretion.
- **Scientific importance**: Moderate. The enzyme has biotechnological relevance, and understanding its secretion could have practical applications. However, the mechanistic insights are limited and the findings are unlikely to change paradigms in the field.
- **Interdisciplinary readership**: Limited. The manuscript will primarily appeal to glycoside hydrolase researchers and those working on yeast expression systems. The broader structural biology community may find the IDR analysis of interest, but the functional data are too preliminary to attract wide attention.
- **Technical soundness**: The structural work appears technically sound, but the functional assays lack the rigor needed to support the conclusions. The kinetic and localization data are underpowered and incompletely reported.
- **Readability for nonspecialists**: The manuscript is generally well-written and accessible, but the significance of the findings is not clearly articulated for a broad audience. The abstract and introduction do a reasonable job of framing the biotechnological context.

### Recommendation posture
**Not currently established from the provided evidence.** The structural data are valuable, but the central functional claims regarding the IDR's role in secretion and membrane localization are not sufficiently supported by the experimental evidence as presented. The manuscript requires substantial additional experimentation and analysis to address the concerns raised above. If the authors can provide robust quantitative data with proper statistical treatment, direct measurements of secretion efficiency, and a more thorough biophysical characterization of the variants, the manuscript could become a solid contribution to the field.

## Risk / unsupported claims
- The claim that the IDR "partially influences" secretion is not quantitatively supported due to lack of statistical analysis and replication
- The claim that glycosylation at all four sites is "required by the host for the secretion of active enzyme" is not directly supported, as the experiments do not distinguish between reduced secretion, reduced protein stability, or reduced expression
- The claim that the IDR is not involved in dimerization is based on indirect evidence and is not fully established
- The statement that the IDR "may not be essential for stable homodimerization" based on in silico analysis is presented without sufficient detail on the methods used
- The interpretation that the IDR contains "membrane binding potential" is based on in silico predictions and is not experimentally validated
- The claim that the "disordered region only partially influences the secretion and membrane localization" is presented as a definitive conclusion, but the mechanism and extent of this influence are not characterized