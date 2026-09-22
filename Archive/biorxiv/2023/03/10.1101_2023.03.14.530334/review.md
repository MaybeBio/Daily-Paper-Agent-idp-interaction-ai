## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, figure legends as embedded in text)
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and internal consistency based solely on the provided manuscript text. No external data, figures, or supplementary materials were available for direct inspection.
- **Shared manuscript claim summary** The authors report that FapC and FapA from *Pseudomonas* are intrinsically disordered proteins (IDPs) in their soluble monomeric state. Using solution NMR spectroscopy, they identify residue-specific chemical shift perturbations (CSPs) upon FapA binding to FapC, with ~18% of FapC resonances and ~90% of FapA resonances affected. They report that FapA decelerates FapC fibrillation in a temperature-dependent manner without altering fibril morphology, and propose an interaction interface at the R1/L2 and L2/R3 transition regions and the C-terminus of FapC.
- **Visible evidence base** Text descriptions of NMR experiments (2D ¹H-¹⁵N HSQC), CSP analyses, intensity decay measurements, ThT assays at 310 K and 277 K, TEM imaging, and in silico predictions (TANGO, WALTZ, AGGRESCAN, FELLS, AlphaFold). Figures referenced but not directly viewable.
- **Missing materials affecting confidence** Actual figures and figure supplements, raw NMR spectra, quantitative CSP values per residue, statistical details of ThT replicates, TEM micrographs, AlphaFold model coordinates, and any supplementary data files. Without these, quantitative claims cannot be independently verified.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question in the field of functional bacterial amyloids: how a disordered chaperone (FapA) modulates the fibrillation of a major biofilm-forming amyloid protein (FapC). The use of solution NMR to probe the interaction at residue-level resolution is a strength, and the observation that FapA is an IDP that interacts with FapC is potentially significant. However, the manuscript as presented has several critical gaps. The quantitative basis for the central claims is not fully transparent from the text alone, the temperature-dependent discrepancy between NMR and ThT results is not mechanistically resolved, and the proposed interaction interface is inferred from CSP data without validation by mutagenesis or other orthogonal approaches. The claim that this is the first reported instance of an IDP acting as a chaperone for a functional amyloid is strong and requires more careful contextualization against existing literature. Overall, the work is promising but the case is not fully established from the provided evidence.
- **Who would be interested in the results, and why** Researchers studying functional bacterial amyloids, biofilm formation, antimicrobial resistance mechanisms, protein chaperones, intrinsically disordered proteins, and amyloid fibrillation mechanisms. The work may also interest those developing therapeutic strategies targeting biofilms, as understanding the molecular basis of chaperone-mediated amyloid control could inform anti-biofilm approaches.
- **Major strengths**  
  1. The study employs high-resolution solution NMR, a powerful technique for studying IDPs, to investigate both sides of the FapC-FapA interaction.  
  2. The observation that FapA is an IDP and interacts with monomeric FapC is novel and potentially important for understanding chaperone function in amyloid systems.  
  3. The combination of NMR, ThT assays, and TEM provides complementary views of the fibrillation process.  
  4. The temperature-dependent analysis is a thoughtful addition that may explain discrepancies with prior work.  
  5. The authors are transparent about the limitations of their speculative interpretation of differential intensity patterns at later time points.
- **Major Concerns**

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency for interaction interface  
- **Claim pointer** The authors claim that CSPs identify a specific interaction interface at the R1/L2 and L2/R3 transition areas and the C-terminus of FapC, and that these sites may represent hotspots of fibrillation inhibition.  
- **Evidence pointer** Results section "FapC and FapA interaction interface by solution NMR CSPs"; Figures 1F, 2A, 2D  
- **Concern** The identification of an interaction interface is based solely on CSP data from a single NMR titration condition (1:4 ratio). No concentration-dependent titration series, no saturation analysis, no dissociation constant estimation, and no mutagenesis or cross-linking validation are presented. CSPs in IDPs can arise from non-specific, transient, or electrostatic interactions that do not represent a defined interface. The claim of a "specific interaction site" is therefore not sufficiently supported.  
- **Why it matters** The central mechanistic claim of the paper is that FapA binds to specific regions of FapC to decelerate fibrillation. Without orthogonal validation or quantitative binding analysis, the proposed interface remains speculative and the mechanistic model is not established.  
- **Resolution test** Provide a full titration series (e.g., 1:0.5 to 1:8) with fitted binding curves and estimated Kd values for representative residues. Validate the proposed interface by site-directed mutagenesis of the identified residues (e.g., A82, N201, C237, C240, A241, G245) and show loss or alteration of CSPs and fibrillation deceleration. Alternatively, use paramagnetic relaxation enhancement (PRE) or cross-linking mass spectrometry to confirm spatial proximity.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Internal consistency of temperature-dependent data  
- **Claim pointer** The authors state that FapA decelerates FapC fibrillation in a temperature-dependent manner, with the effect observed at 274 K and 277 K but largely abolished at 310 K in NMR experiments, while ThT data at 310 K still show reduced endpoint fluorescence.  
- **Evidence pointer** Results section "FapA strongly decelerates FapC fibrillation" and "FapA–FapC interaction and chaperone effect is temperature dependent"; Figures 4 and 5  
- **Concern** The text reports that at 310 K, NMR signal decay curves for FapC and FapC:FapA become similar, suggesting loss of chaperone effect, yet ThT assays at 310 K show FapA reducing endpoint fluorescence. These two observations are not reconciled. The authors note the techniques monitor different species, but no mechanistic explanation is offered for why the chaperone effect would be temperature-sensitive in one assay but not the other. This inconsistency undermines the robustness of the central claim.  
- **Why it matters** The temperature dependence is presented as a key finding that may explain discrepancies with prior work. If the effect is not reproducible across orthogonal assays at the same temperature, the conclusion that FapA is a bona fide chaperone for FapC is weakened.  
- **Resolution test** Perform parallel NMR and ThT experiments at identical temperatures (e.g., 290 K, 300 K, 310 K) with matched sample preparation and time points. Quantify the fraction of monomer remaining by NMR and the ThT endpoint values, and provide a quantitative comparison. If discrepancies persist, provide a mechanistic explanation (e.g., differential sensitivity to oligomeric species, off-pathway aggregates) supported by additional data such as size-exclusion chromatography or analytical ultracentrifugation.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** No  
- **Axis** Novelty and contextualization  
- **Claim pointer** The authors state that "fully IDP protein acting as a chaperone and having significant effect on the prefibrillar monomeric species has not been reported previously in the literature for other systems."  
- **Evidence pointer** Introduction and Discussion sections  
- **Concern** This is a strong novelty claim. The authors cite prior work on CsgC and CsgE, which are not fully disordered, but do not systematically review whether other IDP chaperones or IDP-mediated amyloid modulation has been reported for other systems (e.g., in the context of yeast prions, mammalian amyloid proteins, or other bacterial amyloids). The claim as stated may be overreaching.  
- **Why it matters** If the novelty claim is inaccurate, the significance of the work is diminished. Conversely, if it is accurate, it needs to be supported by a more thorough literature review to convince the reader.  
- **Resolution test** Expand the introduction and discussion to include a systematic comparison with other known IDP chaperones or IDP-mediated amyloid modulators. If none exist, state this explicitly with a comprehensive citation search. If any exist, revise the claim accordingly.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Quantitative rigor of NMR intensity analysis  
- **Claim pointer** The authors report that over 25 days, the 1D NMR signal for pure FapC and FapC:FapA samples is reduced by ~69% and 34%, respectively, and that relative intensity ratios increase from ~0.9 at day 1 to ~1.8 at day 25.  
- **Evidence pointer** Results section "FapA strongly decelerates FapC fibrillation"; Figure 4D, 4E, 5C, 5D  
- **Concern** The text does not report the number of replicates, error bars, or statistical significance for these intensity measurements. The claim of a ~2-fold difference at later time points is based on a single representative experiment as described. Without replicate measurements and error analysis, the quantitative conclusion is not robust.  
- **Why it matters** The magnitude of the chaperone effect is a central quantitative claim. If the variability between experiments is high, the reported 2-fold difference may not be significant.  
- **Resolution test** Provide at least three independent replicates of the time-course NMR experiments with mean ± SD or SEM plotted. Perform appropriate statistical tests (e.g., two-way ANOVA with time and condition as factors) and report p-values. If replicates are not feasible, state this limitation explicitly and temper the quantitative claims.

- **Concern ID** R1-M5  
- **Severity** Major  
- **Blocking** No  
- **Axis** Interpretation of CSP direction and magnitude  
- **Claim pointer** The authors state that ~90% of FapA NMR signals exhibit substantial CSPs upon titration with FapC, and that the largest CSPs in FapC are at residues A82, N201, C237, C240, A241, and G245.  
- **Evidence pointer** Results section "FapC and FapA interaction interface by solution NMR CSPs"; Figures 1G, 3A, 3B  
- **Concern** The text does not specify the magnitude of CSPs in ppm for the key residues, nor the direction of chemical shift changes. For IDPs, CSPs can be influenced by changes in local electrostatic environment, pH, or ionic strength, not necessarily by direct binding. The claim that these residues form a "specific interaction site" requires a more detailed analysis, including mapping onto the AlphaFold model with clear spatial clustering and comparison to random coil chemical shift distributions.  
- **Why it matters** The identification of specific residues is a key result. Without quantitative CSP values and a clear threshold for significance, the reader cannot assess whether the reported residues are truly outliers or within the normal distribution of CSPs for a weakly interacting system.  
- **Resolution test** Provide a table of CSP values for all assigned residues with the mean and standard deviation clearly marked. Highlight the residues exceeding the 2*SD threshold. Show the spatial distribution of these residues on the AlphaFold model with a clear color scale. If possible, compare CSP patterns with a control protein or a mutant FapC to confirm specificity.

- **Minor Comments**

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity of figure references  
- **Affected element** Results section  
- **Evidence pointer** Figures 1, 2, 3, 4, 5, 6  
- **Issue** The text frequently refers to figures and figure supplements without describing the specific panels or data shown. For example, "see Figure 1A,E" and "Figure 1 – figure supplement 1" are mentioned without explaining what the reader should observe.  
- **Required correction** Add explicit descriptions of each figure panel in the text or figure legends, including what data are shown and what conclusion should be drawn from each panel.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Terminology consistency  
- **Affected element** Abstract and Results  
- **Evidence pointer** Abstract, Results section "FapC and FapA interaction interface by solution NMR CSPs"  
- **Issue** The abstract states "~18% of the resonances show FapA induced chemical shift perturbations (CPSs)" but the correct abbreviation is "CSPs" (chemical shift perturbations). The typo "CPSs" appears in the abstract.  
- **Required correction** Correct the abbreviation to "CSPs" throughout the manuscript.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Methodological detail  
- **Affected element** Materials and Methods, NMR Spectroscopy  
- **Evidence pointer** Materials and Methods section  
- **Issue** The NMR interaction experiments are described for FapC-FapA at 1:4 ratio, but the buffer conditions, salt concentration, and reducing agents are not specified for the interaction samples. The FapA-FapC interaction assay buffer is also not described.  
- **Required correction** Provide full buffer composition for all NMR samples, including pH, salt, and any additives. Specify whether DTT was present in the FapC-FapA interaction samples, as this may affect disulfide bond formation in cysteine-containing residues.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Statistical reporting  
- **Affected element** Thrombin cleavage and protein purity  
- **Evidence pointer** Materials and Methods, Recombinant protein production  
- **Issue** The text states that thrombin cleavage was performed overnight, but no information is given on the efficiency of cleavage or the final purity of FapA after cleavage and purification.  
- **Required correction** Include a statement on the purity of FapA after thrombin cleavage and any additional purification steps, with a representative SDS-PAGE gel if available.

- **Concern ID** R1-m5  
- **Severity** Minor  
- **Axis** Interpretation of temperature-dependent NMR data  
- **Affected element** Results section "FapA–FapC interaction and chaperone effect is temperature dependent"  
- **Evidence pointer** Figure 5C, 5D  
- **Issue** The text states that at 310 K, the NMR signal decay curves for FapC and FapC:FapA become similar, but it is not clear whether this is due to loss of interaction, increased exchange broadening, or faster fibrillation of FapC alone at higher temperature.  
- **Required correction** Provide a brief discussion of possible reasons for the loss of chaperone effect at 310 K, including whether the FapC-FapA interaction itself is weakened at higher temperature or whether the fibrillation kinetics of FapC alone are too fast to observe a difference.

## Risk / unsupported claims
- The claim that CSPs identify a "specific interaction site" at the R1/L2 and L2/R3 transition areas and the C-terminus of FapC is unsupported without titration data, mutagenesis validation, or an independent structural method.
- The claim that this is the first reported instance of a fully IDP chaperone affecting prefibrillar monomeric species is not adequately supported by a comprehensive literature review.
- The quantitative claim of a ~2-fold increase in soluble monomer retention in the presence of FapA is not supported by replicate data or statistical analysis.
- The statement that "~90% of FapA NMR signals exhibit substantial CSPs" is not supported by a clear quantitative threshold or a table of CSP values.
- The temperature-dependent discrepancy between NMR and ThT results is described but not mechanistically resolved, leaving the interpretation open.
- The claim that FapA does not alter fibril morphology is based on TEM images that are not shown in the provided text and cannot be assessed.
- The use of AlphaFold models to map CSPs is presented without discussion of the limitations of such models for IDPs, which may not adopt a single stable conformation.