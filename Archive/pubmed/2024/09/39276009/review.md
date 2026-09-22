## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and figure legends as provided.
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided manuscript. No external data or unpublished materials were consulted.
- **Shared manuscript claim summary** The authors propose that MeCP2, an intrinsically disordered protein, is a naturally supercharged protein capable of transducing across cell membranes via its unstructured regions, localizing to heterochromatic foci in the nucleus, and recruiting HDAC3. They map the transduction activity to a specific sequence (M3) resembling the TAT peptide and demonstrate enhanced uptake with endosome-disrupting agents.
- **Visible evidence base** Figures 1–6, Supplementary Figures S1–S5, Tables 1, and Materials and Methods as described in the manuscript text.
- **Missing materials affecting confidence** Raw imaging data, quantitative fluorescence intensity distributions, gating strategies for imaging flow cytometry, full Western blot images, and statistical output details (e.g., exact p-values, effect sizes) are not provided. Supplementary figure legends are referenced but not fully included in the supplied text.

## Reviewer
- **Overall assessment** The manuscript presents an interesting and potentially significant observation that MeCP2, a protein of high clinical relevance, possesses intrinsic cell-penetrating properties mediated by its disordered regions. The work combines computational prediction, live-cell imaging, and biochemical assays to support the claim. However, several technical and interpretational issues, particularly regarding quantification of uptake, specificity of the M3 motif, and functional relevance of HDAC3 recruitment, require clarification before the central claims can be considered fully established.
- **Who would be interested in the results, and why** Researchers in the fields of protein transduction, intrinsically disordered proteins, drug delivery, and Rett syndrome therapeutics would find these results of interest. The identification of a natural supercharged protein with cell-penetrating ability has implications for understanding MeCP2 biology and for designing protein-based therapies.
- **Major strengths** The study addresses a relatively underexplored aspect of MeCP2 biology, namely its disordered regions and their potential functional roles. The use of live-cell imaging to avoid fixation artifacts is appropriate. The combination of in silico prediction with experimental validation provides a reasonable approach to identify candidate transduction sequences. The inclusion of both e1 and e2 isoforms strengthens the generalizability of the findings.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5.
- **Assessment against Nature-style criteria**  
  - **Originality** Moderate. The concept of supercharged proteins is established, and the application to MeCP2 is novel but builds on prior work showing MeCP2 transduction. The identification of a specific TAT-like sequence is a useful contribution.  
  - **Scientific importance** Moderate to high. If fully validated, the findings could inform Rett syndrome therapy and broaden understanding of IDP functions. However, the clinical relevance is speculative at this stage.  
  - **Interdisciplinary readership** Moderate. The topic bridges cell biology, biophysics, and therapeutic development, but the technical depth may limit appeal to a broad audience.  
  - **Technical soundness** Adequate but with notable gaps in quantification and controls, as detailed in the concerns.  
  - **Readability for nonspecialists** The manuscript is generally well-written and accessible, though some methodological details could be clarified for a broader audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising, but the evidence as presented does not fully establish the claims of supercharged behavior, M3 necessity, and functional recruitment.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Quantification and controls  
- **Claim pointer** The authors claim that MeCP2 transduces across cell membranes and localizes to heterochromatic foci, with uptake levels "a third lower" than TAT-fused MeCP2.  
- **Evidence pointer** Figures 2, 3, and 4; location not provided for quantitative data.  
- **Concern** The quantification of uptake relies on imaging flow cytometry and ImageXpress Pico data, but the manuscript does not provide detailed gating strategies, fluorescence intensity thresholds, or raw data distributions. The statement that MG uptake is "a third lower" than TMG is presented without statistical analysis or error estimates.  
- **Why it matters** Without robust quantification, the comparative efficiency claim between MG and TMG is not substantiated, and the reader cannot assess the reliability of the uptake measurements.  
- **Resolution test** Provide representative histograms or scatter plots of fluorescence intensity, define gating criteria, and report mean ± SD/SEM with appropriate statistical tests for at least three independent experiments.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Specificity of M3 motif  
- **Claim pointer** The authors state that the M3 sequence is "necessary" for MeCP2 transduction, based on the lack of uptake of MΔM3G.  
- **Evidence pointer** Figure 5; location not provided.  
- **Concern** The conclusion that M3 is necessary relies on a single deletion mutant. It is unclear whether the deletion disrupts the overall protein conformation or stability, which could indirectly affect uptake. No data on protein folding, aggregation state, or expression levels of the mutant are shown.  
- **Why it matters** A deletion could have pleiotropic effects beyond removing the putative transduction sequence, undermining the specificity of the claim.  
- **Resolution test** Include biophysical characterization of MΔM3G (e.g., circular dichroism, size-exclusion chromatography) and demonstrate that the mutant retains overall structural integrity. Additionally, test a scrambled or point-mutated M3 sequence to confirm sequence-specificity.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Endosomal pathway evidence  
- **Claim pointer** The authors conclude that MeCP2 uptake involves macropinocytosis based on inhibition with amiloride and enhancement with endosome-disrupting agents.  
- **Evidence pointer** Figure 4; location not provided.  
- **Concern** The use of amiloride and indomethacin as pathway-specific inhibitors is not fully justified. Amiloride can have off-target effects, and the concentrations used are not reported. The enhancement by chloroquine and sucrose is interpreted as endosomal escape, but alternative explanations, such as increased membrane fluidity or altered protein stability, are not discussed.  
- **Why it matters** The mechanistic claim about macropinocytosis and endosomal escape is central to the proposed uptake model. Weak evidence here weakens the overall mechanistic narrative.  
- **Resolution test** Include dose-response experiments for inhibitors, validate with additional macropinocytosis markers (e.g., dextran co-uptake), and perform knockdown or genetic ablation of key macropinocytosis regulators to confirm pathway involvement.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Functional relevance of HDAC3 recruitment  
- **Claim pointer** The authors state that transduced MeCP2 interacts with HDAC3, implying functional activity.  
- **Evidence pointer** Figure 6; location not provided.  
- **Concern** The co-immunoprecipitation experiment shows an interaction, but the functional consequence of this interaction is not demonstrated. The authors do not assess whether HDAC3 recruitment leads to transcriptional repression or chromatin remodeling.  
- **Why it matters** The claim of functional relevance is overstated without a downstream functional readout.  
- **Resolution test** Perform a transcriptional reporter assay or measure histone acetylation levels at known MeCP2 target genes following transduction.

- **Concern ID** R1-M5  
- **Severity** Major  
- **Blocking** No  
- **Axis** Supercharged protein classification  
- **Claim pointer** The authors classify MeCP2 as a "naturally supercharged protein" based on charge and CMW calculations.  
- **Evidence pointer** Discussion; location not provided.  
- **Concern** The classification relies on theoretical calculations of net charge and CMW, but the manuscript does not provide a systematic comparison to a panel of known supercharged proteins or non-supercharged controls. The threshold for "supercharged" is not clearly defined.  
- **Why it matters** The title and framing of the manuscript depend on this classification. Without a rigorous comparative analysis, the claim is not fully supported.  
- **Resolution test** Provide a comparative analysis of MeCP2's charge properties against a set of established supercharged proteins and typical globular proteins, using consistent computational methods.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity of methods  
- **Affected element** Materials and Methods, live-cell imaging  
- **Evidence pointer** Materials and Methods; location not provided.  
- **Issue** The concentration of heparin used for washing and the duration of washing steps are not specified, which could affect reproducibility.  
- **Required correction** Specify the concentration and incubation time for heparin washes.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Statistical reporting  
- **Affected element** Figures 3 and 4  
- **Evidence pointer** Figure legends; location not provided.  
- **Issue** The figure legends do not report the number of independent experiments or the statistical test used for comparisons.  
- **Required correction** Add n numbers and statistical details to all figure legends.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Interpretation of e1 isoform data  
- **Affected element** Results, e1 isoform uptake  
- **Evidence pointer** Figure S1; location not provided.  
- **Issue** The authors note comparable uptake for e1 and e2 isoforms but do not discuss potential differences in the polyalanine tract's effect on transduction.  
- **Required correction** Briefly discuss whether the polyalanine tract could influence uptake or if the comparable levels are expected.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Literature context  
- **Affected element** Introduction and Discussion  
- **Evidence pointer** Introduction; location not provided.  
- **Issue** The discussion of supercharged proteins could be strengthened by citing more recent reviews or studies on natural supercharged proteins to contextualize the findings.  
- **Required correction** Add relevant citations to recent literature on natural supercharged proteins and their mechanisms.

- **Concern ID** R1-m5  
- **Severity** Minor  
- **Axis** Figure quality  
- **Affected element** Figure 1  
- **Evidence pointer** Figure 1; location not provided.  
- **Issue** The schematic in Figure 1a is not described in sufficient detail in the legend, making it difficult to interpret the domain boundaries and the location of the M3 motif.  
- **Required correction** Expand the Figure 1 legend to clearly describe all elements, including domain boundaries, M3 location, and construct designs.

## Risk / unsupported claims
- The claim that MeCP2 is a "naturally supercharged protein" is not fully supported by comparative analysis against established supercharged proteins.
- The assertion that the M3 sequence is "necessary" for transduction is based on a single deletion mutant without structural characterization.
- The mechanistic conclusion of macropinocytosis involvement relies on inhibitor studies without sufficient validation of specificity.
- The functional relevance of HDAC3 recruitment is implied but not demonstrated through downstream functional assays.
- The quantitative comparison of MG versus TMG uptake ("a third lower") is not supported by reported statistical analysis or raw data.