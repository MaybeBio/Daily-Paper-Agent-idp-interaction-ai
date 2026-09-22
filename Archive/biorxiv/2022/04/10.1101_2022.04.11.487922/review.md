## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, supplementary methods)
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and internal consistency of the presented evidence
- **Shared manuscript claim summary** The intrinsically disordered RelA TAD enhances DNA binding affinity of the p50/RelA heterodimer, particularly for non-specific DNA sequences, thereby reducing overall binding specificity and promoting higher-order complex formation on tandem κB site DNA.
- **Visible evidence base** SAXS, HDX-MS, EMSA, fluorescence anisotropy, computational modeling (AWSEM, BilboMD, FOXS)
- **Missing materials affecting confidence** Raw SAXS curves and fits, HDX-MS uptake plots, full EMSA gel images, fluorescence anisotropy raw data and fit residuals, statistical analysis details, replicate numbers for all quantitative assays, supplementary figures referenced but not provided (Fig. S1, S2)

## Reviewer
- **Overall assessment** The manuscript addresses an important and timely question regarding the functional role of intrinsically disordered TADs in modulating DNA binding by transcription factors. The authors present a biophysical characterization of the full-length p50/RelA heterodimer and provide evidence that the RelA TAD enhances DNA binding affinity, particularly for non-specific sequences. The finding that the TAD reduces binding specificity is novel and potentially significant for understanding NFκB target selection in vivo. However, the manuscript has several technical weaknesses that need to be addressed. The quantitative affinity measurements rely on a single method (fluorescence anisotropy) with limited validation, the EMSA-based stoichiometry conclusions are semi-quantitative, and the mechanistic interpretation of how the TAD exerts its effect is not directly tested. The claim that the TAD promotes binding to non-consensus DNA in a way that explains in vivo observations is plausible but not fully established from the presented data.

- **Who would be interested in the results, and why** Researchers studying transcription factor DNA binding specificity, intrinsically disordered proteins, NFκB signaling, and gene regulation. The results challenge the traditional modular view of transcription factor domains and suggest that disordered regions can modulate DNA binding properties. This is relevant to the broader community interested in how transcription factors achieve specificity in vivo despite the presence of vast amounts of non-specific DNA.

- **Major strengths** The study uses a full-length transcription factor construct, which is rare and valuable. The combination of multiple biophysical techniques (SAXS, HDX-MS, EMSA, fluorescence anisotropy) provides complementary views of the system. The finding that the TAD enhances non-specific DNA binding is counterintuitive and interesting, given that the p53 TAD has the opposite effect. The authors connect their in vitro observations to in vivo chromatin immunoprecipitation data, providing a potential physiological context for their findings.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of quantitative binding measurements
- **Claim pointer** The manuscript claims specific Kd values for p50/RelA FL and p50/RelA RHD binding to various DNA sequences, including a 10-fold enhancement of non-specific DNA binding by the TAD.
- **Evidence pointer** Figure 6, fluorescence anisotropy methods section
- **Concern** The fluorescence anisotropy binding assays are described but the raw data, fit quality, and validation of the assay are not shown. The Kd values are reported with errors, but the number of replicates, the consistency between replicates, and the goodness of fit are not presented. The assay uses fluorescein-labeled DNA at 5 nM, which is near or above the reported Kd values for specific binding (1-6 nM), potentially compromising the accuracy of these measurements. For the non-specific DNA binding (Kd of 130 nM for FL and 1500 nM for RHD), the dynamic range of the assay and the maximum protein concentrations used are not stated, making it difficult to assess whether the binding curves reached saturation.
- **Why it matters** The central quantitative claim of the manuscript, that the TAD enhances non-specific DNA binding by 10-fold, rests entirely on these measurements. If the assay is not properly validated or the fits are poor, the conclusion is not supported.
- **Resolution test** Provide raw anisotropy data, fit curves with residuals, replicate information, and demonstrate that the assay can accurately measure Kd values in the reported range. Show that binding curves reach saturation and that the protein concentrations used are sufficient.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of EMSA stoichiometry data
- **Claim pointer** The manuscript claims that the presence of the TAD increases the stoichiometry of NFκB-DNA complexes by promoting binding of NFκB dimers in excess of the number of κB sites.
- **Evidence pointer** Figures 3 and 4, EMSA methods
- **Concern** The EMSA experiments show bands attributed to complexes with one, two, or three NFκB dimers bound to DNA, but the assignment of these bands to specific stoichiometries is not validated. No supershift experiments with antibodies against NFκB, no protein-DNA crosslinking, and no independent method (e.g., mass photometry, analytical ultracentrifugation) are used to confirm the number of NFκB dimers in each complex. The smearing observed at high protein concentrations could also be due to non-specific aggregation or binding to the gel matrix. The conclusion that higher-order complexes involve binding to non-consensus DNA is inferred from the DNA sequence and the observation that more complexes form with longer non-specific stretches, but this is not directly demonstrated.
- **Why it matters** The claim that the TAD promotes binding in excess of the number of κB sites is a key novel finding. If the band assignments are incorrect, the conclusion is invalid.
- **Resolution test** Validate the stoichiometry of the observed complexes using an independent method. Perform competition experiments with unlabeled specific and non-specific DNA to demonstrate that the higher-order complexes are specific to NFκB binding. Show that the smeared bands are not due to protein aggregation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic basis for TAD effect
- **Claim pointer** The manuscript implies that the TAD enhances DNA binding affinity through a mechanism that does not involve stable contacts with the RHD, based on HDX-MS data showing no significant differences in deuterium uptake in the RHD with or without the TAD.
- **Evidence pointer** Figure 2, HDX-MS methods
- **Concern** The HDX-MS data are used to argue that the TAD does not form long-lived contacts with the RHD. However, the HDX-MS experiments were only performed in the absence and presence of DNA, and the comparison between p50/RelA FL and p50/RelA RHD is presented as showing no differences. The sensitivity of the HDX-MS experiment to detect transient or weak interactions is not discussed. The manuscript does not provide an alternative mechanistic explanation for how the TAD enhances DNA binding. The authors suggest the TAD may interact with the DNA backbone or promote a conformational change, but these hypotheses are not tested.
- **Why it matters** Understanding the mechanism is important for the broader significance of the finding. Without a mechanistic explanation, the observation remains descriptive.
- **Resolution test** Perform additional experiments to test the mechanism, such as mutagenesis of the TAD, DNA binding assays with the TAD in trans, or NMR studies to detect TAD-DNA interactions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability and comparison to previous work
- **Claim pointer** The manuscript states that the RelA TAD has the opposite effect of the p53 TAD, which decreases non-specific DNA binding, and suggests that modulation of DNA binding by disordered domains may be a general phenomenon.
- **Evidence pointer** Discussion section
- **Concern** The comparison to p53 is based on a single study and the authors do not discuss other transcription factors with TADs that have been characterized. The claim that this may be a general phenomenon is speculative and not supported by the data presented. The authors do not discuss how their findings relate to the in vivo observations of NFκB binding to non-consensus sites, beyond a brief mention in the discussion.
- **Why it matters** The broader significance of the work depends on whether the observed effect is specific to RelA or generalizable. Overstating the generality weakens the manuscript.
- **Resolution test** Moderate the claims of generality and provide a more nuanced discussion of the p53 comparison, acknowledging the limited number of systems studied.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of construct nomenclature
- **Affected element** Results section, Figure 1
- **Evidence pointer** Figure 1A
- **Issue** The manuscript uses p50/RelA FL and p50/RelA RHD but the domain boundaries are only shown in Figure 1A. The text should clearly state the residue numbers for each construct in the results section for clarity.
- **Required correction** Add residue numbers for each construct when first mentioned in the results.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** All quantitative assays
- **Evidence pointer** Figures 6 and 7
- **Issue** The number of replicates for the fluorescence anisotropy experiments is not stated. The errors are reported but it is unclear if they represent standard deviations or standard errors.
- **Required correction** State the number of independent replicates and the type of error bars used in all figure legends.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Supplementary figure referencing
- **Affected element** Results section, competition experiments
- **Evidence pointer** Figure 5, Figure S1
- **Issue** The manuscript references Figure S1 for the competition experiment with the longer non-specific DNA, but this figure is not provided in the submitted manuscript.
- **Required correction** Ensure all supplementary figures are included in the submission.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of in vivo relevance
- **Affected element** Discussion section
- **Evidence pointer** Discussion, paragraph 3
- **Issue** The discussion of the in vivo relevance of the findings is brief and does not fully address how the enhanced non-specific binding might contribute to the observed "global chromatin priming" or the binding to non-consensus sites in ChIP-Seq experiments.
- **Required correction** Expand the discussion to more thoroughly connect the in vitro findings to the in vivo observations, including a more detailed consideration of the concentrations and conditions in the nucleus.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Methodological detail for HDX-MS
- **Affected element** HDX-MS methods
- **Evidence pointer** Methods section, HDX-MS
- **Issue** The HDX-MS methods do not state the peptide coverage or the number of peptides identified. This information is important for assessing the confidence in the deuterium uptake measurements.
- **Required correction** Add peptide coverage information and the number of peptides analyzed.

## Risk / unsupported claims
- The claim that the TAD promotes binding to non-consensus DNA in a way that explains in vivo observations of NFκB binding to non-consensus sites is not directly supported by the data, as no in vivo experiments are presented.
- The claim that the TAD does not form long-lived contacts with the RHD is based on HDX-MS data that are not shown in sufficient detail to assess sensitivity.
- The statement that the effect of the TAD on DNA binding is "novel" is not fully contextualized, as the authors do not discuss all previous studies of TAD effects on DNA binding.
- The estimated nuclear concentration of p50/RelA (3-4 µM) is presented in the discussion without a clear derivation or citation, making it difficult to evaluate.