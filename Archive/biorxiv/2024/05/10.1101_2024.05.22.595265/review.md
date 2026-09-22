## Review setup
- **Input scope** Full manuscript text (abstract, introduction, experimental procedures, results, discussion, data availability, and supplementary figure references)
- **Assessment boundary** Scientific content, technical soundness, and claims as presented in the provided manuscript text. No external data or unpublished materials were consulted.
- **Shared manuscript claim summary** The authors report the first complete backbone NMR assignment of the N-myc transactivation domain (TAD, residues 1–137), characterize its structural propensities and dynamics across multiple timescales, identify a previously uncharacterized Aurora-A binding site within the TAD, and characterize sequential phosphorylation by ERK1 and GSK3, including formation of a complex with Fbxw7–Skp1 upon double phosphorylation.
- **Visible evidence base** NMR chemical shift assignments (BMRB entries 52047, 52066, 52067), secondary chemical shift analysis, TALOS-N predictions, relaxation measurements (R1, R2, heteronuclear NOE), CD spectroscopy on synthetic peptides, NMR titration data for Aurora-A binding, in-NMR kinase assays, and analytical size-exclusion chromatography.
- **Missing materials affecting confidence** Supplementary figures and tables (Fig. S1–S8, Table S1) are referenced but not provided. Raw NMR spectra, relaxation data fits, titration curves, and SEC chromatograms are not shown in the provided text. Experimental details for some NMR experiments (e.g., pulse sequences, acquisition parameters) are not fully described.

## Reviewer
- **Overall assessment** This manuscript presents a valuable resource in the form of the first complete backbone assignment of the N-myc TAD, along with biophysical characterization of its dynamics and interactions. The work is technically sound in its core NMR methodology and the assignment strategy using truncated constructs is sensible. The identification of a potential new Aurora-A interaction region within MBII is interesting but requires stronger validation. The phosphorylation studies are well designed and the Fbxw7–Skp1 binding data are convincing. However, several claims regarding the extent of the Aurora-A interaction surface and the functional significance of the observed dynamics are not fully supported by the evidence presented. The manuscript would benefit from additional quantitative analysis and clearer presentation of key data.
- **Who would be interested in the results, and why** Researchers studying MYC family transcription factors, intrinsically disordered proteins, and their roles in cancer biology. The NMR assignment will be a useful resource for structural biologists and biochemists investigating N-myc interactions and post-translational modifications. The findings on Aurora-A binding and phosphodegron regulation are relevant to those studying targeted therapies for MYC-driven cancers.
- **Major strengths** The first complete backbone assignment of the N-myc TAD is a significant technical achievement and a valuable community resource. The truncation-based assignment strategy is well conceived and executed. The combination of multiple biophysical techniques (NMR, CD, SEC) provides complementary evidence. The phosphorylation studies are carefully performed and the demonstration of Fbxw7–Skp1 binding to doubly phosphorylated N-myc TAD is a clear and important result.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (Aurora-A interaction surface claim), R1-M2 (dynamics interpretation), R1-M3 (CD quantification).
- **Assessment against Nature-style criteria** Originality: The work is original in providing the first complete N-myc TAD assignment and identifying a potential new Aurora-A interaction site. Scientific importance: The N-myc TAD is a key oncogenic driver, and understanding its structure, dynamics, and interactions has broad relevance. However, the functional implications of the findings are not fully explored. Interdisciplinary readership: The work will appeal to structural biologists, biochemists, and cancer researchers, but the presentation is somewhat specialized. Technical soundness: The NMR methodology is generally sound, but some claims require additional quantitative support. Readability for nonspecialists: The manuscript is clearly written but assumes familiarity with NMR techniques and MYC biology.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the extent of the Aurora-A interaction surface and the interpretation of dynamics data.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** "Solution studies on the interaction between N-myc and Aurora-A revealed a previously uncharacterised binding site" and "The last region, which aligns with MBII has not been previously characterised, and so the data indicate that the N-myc–Aurora-A interface is more extensive than previously thought."
- **Evidence pointer** Results section, "In vitro phosphorylation of N-myc TAD" subsection; Figure 6 (referenced but not provided)
- **Concern** The claim of a new Aurora-A binding site within MBII is based on NMR titration data showing intensity losses and CSPs in the MBII region. However, the manuscript does not provide quantitative binding data (e.g., dissociation constants), a clear demonstration of specificity (e.g., competition with a known binder or mutagenesis), or direct evidence of a stable complex. The intensity losses could also result from non-specific effects, aggregation, or indirect conformational changes. The authors state that "the initial peak overlap and poor quality of the N-myc–Aurora-A complex spectrum prevented a more thorough analysis" for the full-length TAD, which weakens the confidence in the interpretation of the truncation data.
- **Why it matters** The identification of a new interaction site is a central claim of the manuscript. If the MBII region is indeed a bona fide Aurora-A binding site, this has implications for understanding N-myc regulation and for drug development. However, without quantitative binding data or mutagenesis validation, the claim remains speculative and could mislead the field.
- **Resolution test** Provide quantitative binding data (e.g., ITC, MST, or NMR-derived Kd) for the interaction between Aurora-A and the MBII region, using either the full-length TAD or a peptide spanning this region. Alternatively, perform mutagenesis of key residues in the MBII region and demonstrate loss of binding. Show that the observed intensity losses and CSPs are specific to the MBII region and not due to non-specific effects.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation
- **Claim pointer** "These regions also have more restricted ps–ns motions than the rest of the TAD, and, along with another known interaction site (myc box I), have comparatively high transverse (R2) 15N relaxation rates, indicative of slower timescale dynamics and/or chemical exchange."
- **Evidence pointer** Results section, "Backbone assignment of N-myc TAD" and "N-myc TAD structure and dynamics" subsections; Figure 4 (referenced but not provided)
- **Concern** The interpretation of elevated R2 values as evidence of "slower timescale dynamics and/or chemical exchange" is plausible but not rigorously established. The manuscript does not report reduced spectral density analysis, relaxation dispersion experiments (e.g., CPMG or R1ρ), or model-free analysis to distinguish between conformational exchange and other contributions to R2. The claim that these regions have "more restricted ps–ns motions" is based on heteronuclear NOE data, but the differences may be within experimental uncertainty. The authors also do not discuss potential contributions from chemical exchange with the solvent or from oligomerization.
- **Why it matters** The dynamics data are used to support the idea that the TAD has differential propensities for structure and interaction. If the interpretation is incorrect, the conclusions about the functional significance of these regions are weakened. A more rigorous analysis would strengthen the manuscript.
- **Resolution test** Perform relaxation dispersion experiments (e.g., 15N CPMG or R1ρ) on the regions with elevated R2 to determine if chemical exchange is present. Alternatively, perform a model-free analysis of the relaxation data to extract order parameters and internal correlation times. Report uncertainties in the relaxation rates and NOE values.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical rigor
- **Claim pointer** "An estimate of helical content using the MRE222 value shows MBII+ to be 20% helical—which is significant helical content for a short peptide—whereas MBI and AIH might be ∼10% helical."
- **Evidence pointer** Results section, "N-myc peptides for regions of interest" subsection; Figure 5 (referenced but not provided)
- **Concern** The helical content estimates are based on a single wavelength (MRE222) and a simple empirical formula. This approach is known to be approximate and can be influenced by aromatic side chains, aggregation, and other factors. The authors do not report the concentration of the peptides, the path length, or the number of replicates. The statement that MBI and AIH "might be ∼10% helical" is vague and not supported by a quantitative analysis. The comparison between peptides is also complicated by differences in sequence length and composition.
- **Why it matters** The CD data are used to support the claim that the MBII+ region has intrinsic helical propensity, which is a key finding. If the helical content estimates are inaccurate, the conclusion is weakened. A more rigorous analysis would provide confidence in the result.
- **Resolution test** Provide full CD spectra (190–260 nm) for all peptides, with error bars from replicate measurements. Use a more robust method for estimating helical content (e.g., SELCON3, CDSSTR, or BeStSel). Report the peptide concentrations and path length. Consider performing concentration-dependent measurements to rule out aggregation.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, "These regions also have more restricted ps–ns motions than the rest of the TAD, and, along with another known interaction site (myc box I), have comparatively high transverse (R2) 15N relaxation rates, indicative of slower timescale dynamics and/or chemical exchange."
- **Issue** The abstract is dense and uses specialized terminology (e.g., "ps–ns motions", "transverse (R2) 15N relaxation rates") without defining these terms for a general reader. The phrase "differential propensities for structure and interaction, either internal or with binding partners" is vague.
- **Required correction** Briefly define key NMR terms and clarify the significance of the findings for a broader audience. For example, state that "regions with restricted motion and higher relaxation rates may represent sites of transient structure or interaction."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Experimental procedures
- **Evidence pointer** Experimental procedures, "NMR spectroscopy" subsection (not fully detailed in provided text)
- **Issue** The NMR experimental details are incomplete. The manuscript does not specify the NMR spectrometer frequencies for all experiments, the temperature calibration, the pulse sequences used, or the processing parameters. The relaxation experiments are described but the specific pulse sequences and analysis methods are not given.
- **Required correction** Provide a complete description of the NMR experiments, including spectrometer frequencies, pulse sequences, acquisition parameters, and data processing details. This is essential for reproducibility.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion, "Multi-site interaction with Aurora-A perturbs the N-myc TAD" subsection
- **Issue** The discussion of the AlphaFold2 predictions is somewhat speculative. The authors state that "AlphaFold2 is able to identify conditional folding, particularly of helices, in IDRs" but do not provide a rigorous comparison of the predicted and experimental data. The significance of the "ERA" insertion in N-myc MBII+ is mentioned but not explored.
- **Required correction** Provide a more detailed comparison of the AlphaFold2 predictions with the experimental data. Discuss the limitations of AlphaFold2 for disordered regions and avoid over-interpreting the predictions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figures
- **Evidence pointer** Figures 1–8 (referenced but not provided)
- **Issue** The figures are not provided in the manuscript text, making it difficult to assess the quality of the data presentation. The figure legends are not included.
- **Required correction** Ensure that all figures are clearly labeled, with informative legends that describe the experimental conditions and the data shown. Consider including representative spectra and titration curves.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Results and Discussion
- **Evidence pointer** Results, "In vitro phosphorylation of N-myc TAD" subsection; Discussion, "Two-site, specific phosphorylation of N-myc MBI" subsection
- **Issue** The manuscript states that "the action of GSK3 appears to be specific to Thr58" but also notes that "a low level of phosphorylation is consistent with overexpressed GSK3 being able to phosphorylate Thr58 in vivo, when a S62A mutation is present." This is somewhat contradictory and could be clarified.
- **Required correction** Clarify the specificity of GSK3 for Thr58 and discuss the implications of the S62A mutation data more clearly.

## Risk / unsupported claims
- The claim of a "previously uncharacterised binding site" for Aurora-A within MBII is not fully supported by quantitative binding data or mutagenesis.
- The interpretation of elevated R2 values as evidence of chemical exchange is not rigorously established without relaxation dispersion experiments.
- The helical content estimates from CD spectroscopy are approximate and not supported by full spectral analysis.
- The statement that "these regions also have more restricted ps–ns motions than the rest of the TAD" is based on qualitative comparisons and lacks statistical analysis.
- The functional significance of the observed dynamics and structural propensities is speculative and not directly tested.