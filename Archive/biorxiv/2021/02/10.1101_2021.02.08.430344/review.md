## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) as provided
- **Assessment boundary** Scientific content, methodological soundness, interpretation of results, and alignment with stated claims. No assessment of editorial fit or journal policy.
- **Shared manuscript claim summary** The authors report a biophysical characterization of SARS-CoV-2 N-protein self-association and its co-assembly with nucleic acids of varying length. They propose that short oligonucleotides bind to the N-protein dimer in a length-dependent manner, that longer oligonucleotides promote higher-order oligomerization and liquid-liquid phase separation, and that these processes involve structural transitions from disordered to more ordered states.
- **Visible evidence base** Sedimentation velocity analytical ultracentrifugation (SV-AUC), dynamic light scattering (DLS), isothermal titration calorimetry (ITC), circular dichroism (CD), differential scanning calorimetry (DSC), differential scanning fluorometry (DSF), and light microscopy. Figures 1-7 and supplementary figures S1-S7 are referenced.
- **Missing materials affecting confidence** Raw data files, detailed fitting parameters for global modeling, complete ITC thermograms, full DSC thermograms, microscopy images beyond representative frames, and statistical details for replicate measurements are not provided. The manuscript is a preprint and has not undergone peer review.

## Reviewer
- **Overall assessment** This manuscript presents a systematic and technically rigorous biophysical study of SARS-CoV-2 N-protein interactions with nucleic acids. The combination of multiple orthogonal techniques is commendable and the data largely support the major claims. However, several concerns regarding quantitative rigor, interpretation of complex mixture data, and generalizability to physiological conditions need to be addressed. The work is of interest to the virology and biophysics communities, but the current evidence base does not fully establish all mechanistic conclusions.
- **Who would be interested in the results, and why** Researchers studying SARS-CoV-2 biology, particularly those focused on nucleocapsid protein function, viral assembly, and ribonucleoprotein complex formation. Also relevant to the broader field of liquid-liquid phase separation in biology, and to biophysicists interested in multi-valent protein-nucleic acid interactions.
- **Major strengths** 1) Use of multiple orthogonal biophysical techniques to characterize the same system. 2) Systematic variation of nucleic acid length to dissect length-dependent binding modes. 3) Quantitative global fitting of SV-AUC and ITC data. 4) Clear demonstration of the absence of LLPS for N-protein alone under the conditions tested. 5) The observation of length-dependent transitions from simple binding to higher-order assembly is conceptually important.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative rigor of binding parameters), R1-M2 (interpretation of complex SV-AUC boundaries), R1-M3 (generality of conclusions to physiological conditions), R1-M4 (structural interpretation of CD data).
- **Assessment against Nature-style criteria** Originality: The work is original in its systematic biophysical dissection of N-protein/NA co-assembly, though it builds on prior studies of N-protein LLPS. Scientific importance: Moderate to high, given the central role of N-protein in SARS-CoV-2 biology and the current pandemic context. Interdisciplinary readership: The work bridges virology, biophysics, and phase separation biology, and would appeal to a broad readership. Technical soundness: Generally high, with appropriate use of multiple techniques, but with some quantitative concerns as detailed below. Readability for nonspecialists: The manuscript is well-written and accessible, with clear figures and logical flow, though some sections assume familiarity with biophysical methods.
- **Recommendation posture** Supportive if technical concerns are resolved. The core observations are likely correct, but the quantitative claims and mechanistic interpretations require strengthening.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative rigor
- **Claim pointer** The authors report a microscopic dissociation constant of 0.6 μM for T6 binding to the N-protein dimer, with a 95% CI of 0.1-0.7 μM, derived from global fitting of SV-AUC and ITC data.
- **Evidence pointer** Results section, Figure 3A-B
- **Concern** The reported KD value and its confidence interval are based on a global fit of two different techniques. However, the manuscript does not provide details on the fitting model, the number of parameters, the treatment of potential systematic errors, or the criteria for assessing goodness-of-fit. The wide confidence interval (0.1-0.7 μM) suggests limited precision. Additionally, the ITC data are described but not shown in full, and the SV-AUC titration series at 0.5 μM N-protein in the presence of P20 yielded a different model with negative cooperativity, which is not reconciled with the main analysis.
- **Why it matters** The quantitative binding parameters are central to the claim of length-dependent binding modes and are used to support the mechanistic model. Without transparent and robust fitting procedures, the reliability of these parameters is uncertain.
- **Resolution test** Provide full details of the global fitting model, including equations, parameter constraints, and error analysis. Show complete ITC thermograms and fit residuals. Reconcile the discrepancy between the two models (non-cooperative vs. negatively cooperative) or justify the choice of one over the other.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of complex mixtures
- **Claim pointer** The authors interpret the broadened SV-AUC boundaries and high s-values in T10 and T20 mixtures as evidence for rapidly exchanging higher-order oligomers, including tetramers and hexamers.
- **Evidence pointer** Results section, Figure 2D-E
- **Concern** The interpretation of reaction boundaries in SV-AUC is notoriously difficult, especially for systems with multiple interacting species. The authors invoke rapid exchange to explain the broadened boundaries, but do not provide a quantitative analysis, such as simulation of expected boundary shapes for candidate models. The claim of tetramers and hexamers is based on s-value estimates, but the relationship between s-value and oligomeric state depends on assumptions about shape and hydration that are not fully justified.
- **Why it matters** The identification of specific oligomeric states is a key claim of the paper. If the interpretation of the SV-AUC data is incorrect, the proposed assembly pathway would be unsupported.
- **Resolution test** Perform quantitative simulations of SV-AUC boundaries for candidate oligomerization models and compare to experimental data. Alternatively, use an independent technique such as sedimentation equilibrium AUC or mass photometry to directly determine the molar masses of the complexes.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The authors state that their findings reveal "architectural and energetic aspects of the initial steps of RNP assembly" and discuss implications for viral assembly.
- **Evidence pointer** Discussion section
- **Concern** All experiments were performed with short synthetic oligonucleotides (up to 20 nucleotides) in low-salt buffer at pH 7.4. The viral genome is a single-stranded RNA of approximately 30,000 nucleotides, and the intracellular environment contains high concentrations of proteins, nucleic acids, and other macromolecules. The extent to which the observed behavior with short oligonucleotides in dilute solution reflects the in vivo assembly process is unclear.
- **Why it matters** The broader significance of the work depends on its relevance to actual viral assembly. If the conditions used are too far from physiological, the conclusions may not generalize.
- **Resolution test** Discuss the limitations of the model system more explicitly. If possible, include experiments with longer RNA fragments or under more physiologically relevant conditions (e.g., higher salt, presence of crowding agents) to test the robustness of the findings.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Structural interpretation
- **Claim pointer** The authors interpret the reduced negative ellipticity at 200 nm in CD spectra upon NA binding as evidence for "reduction of disorder" and "gain of structure" in the N-protein.
- **Evidence pointer** Results section, Figure 3C and Figure 7
- **Concern** CD spectroscopy reports on the average secondary structure content of the entire protein, including both folded domains and intrinsically disordered regions. The interpretation of changes at 200 nm as a reduction in disorder is plausible but not unique; changes in the folded domains could also contribute. The authors do not provide a quantitative deconvolution of the CD spectra or correlate the CD changes with the binding stoichiometry.
- **Why it matters** The claim of a structural transition from disordered to ordered states is a central part of the proposed mechanism. If the CD data are over-interpreted, the mechanistic model would be weakened.
- **Resolution test** Perform quantitative CD deconvolution using available algorithms (e.g., BeStSel, which is already used) and report the estimated secondary structure fractions. Correlate the CD changes with the binding isotherm to establish a direct link between binding and structural change.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1B
- **Evidence pointer** Results section, Figure 1B
- **Issue** The raw sedimentation boundaries shown in Figure 1B are not annotated with the concentration or the specific experimental conditions. It is unclear whether this is a representative trace at a single concentration or an overlay of multiple concentrations.
- **Required correction** Add a figure legend that clearly states the concentration, buffer conditions, and whether the data are representative or averaged.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section, protein purification
- **Evidence pointer** Methods section
- **Issue** The protein was purchased from a commercial source (EXONBIO). While the authors verified purity and mass, the batch-to-batch variability of commercial preparations is a potential concern for reproducibility.
- **Required correction** Provide the lot number or state that multiple batches were tested and found to be consistent.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 5
- **Evidence pointer** Results section, Figure 5
- **Issue** The DLS data in Figure 5A-B show size distributions, but the intensity-weighted nature of DLS can bias the apparent size toward larger particles. The authors mention this in the text but do not provide number-weighted or volume-weighted distributions for comparison.
- **Required correction** Show number-weighted or volume-weighted size distributions in the supplementary material to support the interpretation.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The discussion of the relationship between the observed in vitro behavior and in vivo RNP assembly is somewhat speculative. The authors mention potential roles of phosphorylation and M-protein interactions but do not integrate these into a coherent model.
- **Required correction** Expand the discussion to provide a more explicit model of how the observed co-assembly behavior might relate to RNP formation in the infected cell, and acknowledge alternative possibilities.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Throughout
- **Evidence pointer** Various figures
- **Issue** The number of replicates for each experiment is not consistently reported. For example, the ITC experiments are described as single titrations, and the CD temperature scans appear to be single runs.
- **Required correction** Clearly state the number of independent replicates for each experiment and report the variability (e.g., standard deviation or standard error) where appropriate.

## Risk / unsupported claims
- The claim that T10 promotes tetramer and higher-order oligomer formation is based on indirect s-value estimates and is not quantitatively supported.
- The claim of a structural transition from disordered to ordered states upon NA binding is based on qualitative CD interpretation and is not quantitatively deconvoluted.
- The extrapolation of findings with short oligonucleotides in dilute solution to the in vivo process of RNP assembly is not directly supported by the data.
- The reported KD values for T6 binding are based on a global fit with limited transparency and may not be robust.
- The claim that LLPS is "supported by structural transitions" is speculative, as the authors acknowledge that direct proof of altered conformation in the dense phase is lacking.