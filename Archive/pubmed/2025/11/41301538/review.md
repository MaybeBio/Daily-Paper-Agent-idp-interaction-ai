## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) as provided
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the supplied text; no supplementary figures or raw data were available for independent verification
- **Shared manuscript claim summary** The authors report that LIMCH1 and its C-terminal variant ΔLIM-ALP are intrinsically disordered proteins that nonetheless exhibit Mn2+-dependent agmatinase activity and thermal hyperactivation, features characteristic of canonical ureohydrolases. They further propose candidate Mn2+-coordinating residues and test them via site-directed mutagenesis, finding altered kinetics but no loss of activity.
- **Visible evidence base** CD spectroscopy data (Figures 4-6), kinetic measurements (Figure 7, Table 1), TXRF metal analysis, AlphaFold2/3 predictions (Figure 3), mutagenesis results (Figures 7-8)
- **Missing materials affecting confidence** Raw CD spectra and deconvolution parameters, full kinetic datasets with replicates, TXRF calibration details, molecular dynamics simulation parameters and trajectories, purification yields and purity assessments, supplementary figures referenced (Figures S1-S3), statistical analysis details for kinetic comparisons

## Reviewer
- **Overall assessment** This manuscript addresses an intriguing and timely question: whether a highly disordered protein can retain enzymatic function. The topic is of broad interest to the enzymology and structural biology communities. However, the evidence presented is insufficient to firmly establish the central claims. The CD data are acknowledged by the authors to be technically challenging, the mutagenesis results are difficult to interpret without structural context, and the metal-binding conclusions rest on indirect evidence. The manuscript would benefit from additional orthogonal approaches to validate the disorder and activity claims.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins and their functional roles; enzymologists interested in non-canonical catalysis; structural biologists using or developing prediction tools; pharmacologists studying agmatine signaling pathways. The potential demonstration of catalysis in a disordered protein would challenge current paradigms and could inform drug discovery efforts targeting LIMCH1.
- **Major strengths** The study addresses a genuinely novel and important question. The combination of computational prediction, biophysical characterization, and mutagenesis is appropriate in principle. The authors are transparent about technical limitations. The comparison with E. coli agmatinase provides useful context. The observation of altered kinetics without loss of activity in mutants is interesting and potentially informative.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (CD data quality and interpretation), R1-M2 (mutagenesis interpretation without structural context), R1-M3 (metal binding evidence), R1-M4 (activity assay validation)
- **Assessment against Nature-style criteria** Originality: high, the question of catalysis in disordered proteins is novel and significant. Scientific importance: potentially high if claims are substantiated, as it would challenge structural paradigms of enzyme catalysis. Interdisciplinary readership: the topic bridges structural biology, enzymology, and neurobiology, which could attract broad interest. Technical soundness: currently insufficient, with several methodological concerns that need addressing. Readability for nonspecialists: the manuscript is generally well-written and accessible, though some sections assume familiarity with enzymology terminology.
- **Recommendation posture** Currently not established from the provided evidence. The central claims require stronger experimental support. Supportive if technical concerns are resolved.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors claim that CD spectroscopy demonstrates LIMCH1 and ΔLIM-ALP are largely disordered, with approximately 60% disordered regions and 30% beta-structure.
- **Evidence pointer** Section 3.2, Figures 4-6
- **Concern** The CD data for ΔLIM-ALP are acknowledged to have a signal nearly tenfold weaker than theoretically expected, with low signal-to-noise ratio. This raises serious questions about data reliability. The authors also note that BeStSel deconvolution may be biased for disordered proteins, yet they rely on this method for quantitative claims. The discrepancy between experimental and theoretical spectra could arise from protein aggregation, improper folding, or experimental artifacts rather than intrinsic disorder. No independent validation (e.g., SEC-MALS, NMR, or limited proteolysis) is provided to confirm the disordered state.
- **Why it matters** The central claim of the manuscript is that these proteins are highly disordered yet catalytically active. If the CD data are unreliable, this claim is not substantiated. The quantitative estimates of secondary structure content are used throughout the discussion to support the disorder hypothesis.
- **Resolution test** Provide raw CD data with signal-to-noise estimates, repeat measurements with independent protein preparations, validate disorder using orthogonal methods (e.g., SEC-MALS, NMR, or protease sensitivity), and include proper controls for protein quality and aggregation state.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation
- **Claim pointer** The authors state that mutations of putative Mn2+-binding residues (N213A, Q215A, D217A, E288A, K290A) affect kinetics but do not abolish activity, implying these residues are near but not essential for the active site.
- **Evidence pointer** Section 3.4, Figure 7, Table 1
- **Concern** Without a structural model of the active site, the interpretation of the mutagenesis results is speculative. The authors acknowledge that AlphaFold failed to produce reliable models, yet they interpret kinetic changes as evidence for active-site proximity. Alternative explanations include long-range allosteric effects, protein stability changes, or altered oligomerization. The observation that four mutants show decreased Km is counterintuitive for mutations in a substrate-binding site and is not adequately explained. Additionally, the statement that "no significant differences were observed compared to the wild-type enzyme" in metal-dependence assays contradicts the earlier claim that these residues are functionally important.
- **Why it matters** The mutagenesis data are the only functional evidence linking specific residues to catalysis. If the interpretation is not justified, the conclusions about active-site architecture are unsupported.
- **Resolution test** Provide structural or computational evidence for the active-site location, measure protein stability and oligomerization state of mutants, and perform detailed kinetic analysis including substrate saturation curves with proper error analysis.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors report that LIMCH1 contains 1.3 Mn2+ ions per subunit based on TXRF analysis, and that dialysis leads to loss of activity consistent with removal of a loosely bound Mn2+.
- **Evidence pointer** Section 3.4, Section 2.4
- **Concern** The TXRF analysis is described in minimal detail. No calibration information, detection limits, or replicate measurements are provided. The value of 1.3 Mn2+ per subunit is unusual and not explained. The dialysis experiments show activity loss, but the authors do not demonstrate that this is specifically due to Mn2+ removal rather than protein denaturation or other factors. The claim of "strongly and weakly bound Mn2+ ions" is inferred from behavior but not directly demonstrated.
- **Why it matters** The Mn2+ dependence is a key feature linking these proteins to canonical ureohydrolases. If the metal-binding evidence is not robust, this connection is weakened.
- **Resolution test** Provide detailed TXRF methodology with calibration and replicates, measure Mn2+ content before and after dialysis, and demonstrate that activity loss upon dialysis is reversible by Mn2+ addition.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental design
- **Claim pointer** The authors claim that both LIMCH1 and ΔLIM-ALP exhibit agmatinase activity with Michaelis-Menten kinetics.
- **Evidence pointer** Section 3.3, Section 3.4, Figures 5, 7
- **Concern** The activity assays are described briefly. No information is provided on the purity of the recombinant proteins used in kinetic assays, the specific activity values, or the detection method for urea. The possibility of contaminating E. coli agmatinase or other hydrolases is not addressed. The kinetic parameters in Table 1 are presented without confidence intervals or statistical comparisons between mutants and wild-type. The claim that all mutants follow Michaelis-Menten kinetics is based on visual inspection of hyperbolic curves without formal statistical testing.
- **Why it matters** The enzymatic activity is the central functional claim. If the assays are not rigorously validated, the entire premise of the manuscript is compromised.
- **Resolution test** Provide detailed assay methodology, demonstrate protein purity (e.g., SDS-PAGE with densitometry), include negative controls (e.g., empty vector lysate), and provide statistical analysis of kinetic parameters with replicates.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that "four mutants exhibited a decreased Km for agmatine and a reduced Vmax" but does not specify which mutant was the exception or the magnitude of changes.
- **Required correction** Specify which mutant did not show decreased Km and provide quantitative values for the kinetic changes.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodology
- **Affected element** Section 2.2
- **Evidence pointer** Section 2.2
- **Issue** The purification protocol mentions DEAE-cellulose, Ni-NTA, and size-exclusion chromatography but does not provide column dimensions, flow rates, or yield information.
- **Required correction** Add sufficient methodological detail to allow replication.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 8
- **Evidence pointer** Figure 8
- **Issue** The results of the dialysis and hyperactivation experiments are described in text but the figure is not described in sufficient detail to understand the experimental conditions for each panel.
- **Required correction** Provide a clear figure legend describing each panel and the experimental conditions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction
- **Evidence pointer** Introduction
- **Issue** The introduction mentions that "predictive artificial intelligence algorithms such as AlphaFold have failed to model it reliably" but does not discuss why this might be the case or what implications this has for the field.
- **Required correction** Add a brief discussion of the limitations of AlphaFold for disordered proteins and cite relevant literature.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Section 2.7
- **Evidence pointer** Section 2.7
- **Issue** The statistical methods section mentions ANOVA and t-tests but does not specify which comparisons were made with which tests or how multiple comparisons were handled.
- **Required correction** Clarify the statistical approach for each comparison reported in the results.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** Throughout
- **Issue** The term "agmatinase-like protein" (ALP) is used interchangeably with "ΔLIM-ALP" in some sections, which may confuse readers.
- **Required correction** Define the relationship between ALP, LIMCH1, and ΔLIM-ALP clearly at first use and maintain consistent terminology.

## Risk / unsupported claims
- The claim that LIMCH1 and ΔLIM-ALP are "highly disordered" is based on CD data that the authors acknowledge are technically challenging and on AlphaFold predictions that are acknowledged to be unreliable for disordered proteins. This claim is not fully supported by the provided evidence.
- The claim that the mutated residues are "involved in or near the active site" is speculative without structural data or additional functional evidence.
- The claim of "strongly and weakly bound Mn2+ ions" is inferred from dialysis behavior but not directly demonstrated.
- The statement that these proteins represent "a striking case of convergent evolution with canonical ureohydrolases" is not supported by any evolutionary analysis.
- The claim that "no significant differences were observed" between mutants and wild-type in metal-dependence assays is not supported by statistical analysis presented in the text.
- The quantitative secondary structure estimates (60% disordered, 30% beta-structure) are not reliable given the acknowledged limitations of the CD measurements and deconvolution methods.