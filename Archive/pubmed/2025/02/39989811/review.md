## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, materials and methods, results, discussion, and conclusions. Figures and tables are referenced but not provided in the supplied material.
- **Assessment boundary** The assessment is limited to the scientific content and internal consistency of the provided text. Experimental data, figures, and supplementary materials are not available for direct verification.
- **Shared manuscript claim summary** The authors report the detection of a partially folded, dimeric intermediate that accumulates during the urea-induced unfolding of the N-terminal domain of TDP-43, prior to the major unfolding transition. This intermediate is characterized by distinct intrinsic fluorescence, far-UV CD, SYPRO Orange binding, and hydrogen-deuterium exchange properties, and is not observed during thermal unfolding.
- **Visible evidence base** Text descriptions of results from stopped-flow fluorescence, equilibrium fluorescence, far-UV CD, SYPRO Orange fluorescence, HDX-MS, and DLS experiments. Statistical values (mean ± SEM, p values) are reported in the text. Figures 1-10 and Tables S1 are cited but not visible.
- **Missing materials affecting confidence** All figures, tables, and supplementary information are absent. Raw kinetic traces, spectra, statistical details, and experimental replicates cannot be independently assessed. The previous study (ref 35) providing data for 4.5-7.0 M urea is not available for comparison.

## Reviewer
- **Overall assessment** The manuscript presents a systematic and multi-probe experimental investigation of the unfolding pathway of TDP-43 NTD, providing evidence for a transient, partially folded dimeric intermediate that forms rapidly before the major unfolding barrier. The combination of kinetic and equilibrium approaches, along with multiple orthogonal probes, strengthens the central claim. However, the absence of the actual figures and tables limits the ability to fully evaluate the quality and robustness of the data. The interpretation of the chevron plot curvature and the assignment of the intermediate as dimeric rely on indirect evidence that would benefit from additional direct validation. The work is of interest to the protein folding and neurodegeneration communities, though the novelty relative to prior computational predictions and the general significance for TDP-43 pathology require careful framing.
- **Who would be interested in the results, and why** Researchers studying protein folding and misfolding mechanisms, particularly those focused on partially folded states and their role in aggregation. The TDP-43 field, including those investigating ALS, FTLD-TDP, and LATE-NC, will find the structural plasticity of the NTD relevant to understanding pathological self-assembly. The methodological approach, combining multiple spectroscopic probes with kinetic analysis, may also interest biophysicists developing tools for detecting transient unfolding intermediates.
- **Major strengths** The use of multiple orthogonal biophysical techniques (intrinsic fluorescence, far-UV CD, SYPRO Orange, HDX-MS, DLS) to cross-validate the existence of the intermediate is a clear strength. The observation of the intermediate at both high and moderate urea concentrations, and at a protein concentration below the dimer KD, addresses concerns about concentration-dependent artifacts. The comparison with thermal unfolding provides a useful control, demonstrating that the intermediate is specific to chemical denaturation. The connection to prior MD simulations and the broader context of TDP-43 structural plasticity is well articulated.
- **Major Concerns** The absence of figures and tables prevents verification of data quality, fitting procedures, and statistical robustness. The interpretation of the chevron plot curvature as evidence for an intermediate is plausible but not definitive, as curvature can also arise from transition state movement. The claim that the intermediate is dimeric is based on DLS measurements that show a constant DH, but the resolution of DLS may not be sufficient to distinguish a compact dimer from an expanded monomer. The HDX-MS data are presented qualitatively, and the degree of protection is not quantified. The physiological relevance of the intermediate, particularly at the low protein concentrations used, is not fully established.
- **Minor Comments** The manuscript would benefit from a more detailed description of the fitting procedures and error analysis. The use of the term "native-like" to describe the intermediate's HDX pattern is somewhat ambiguous, as the intermediate clearly differs from the native state in other probes. The discussion of the potential functional and pathological roles of the intermediate is speculative and could be more tightly linked to the experimental findings. The statement that the intermediate forms "within 500 ns as detected by MD simulations" is not directly supported by the experimental data presented here and should be clearly distinguished from the experimental timescale.
- **Technical failings that need to be addressed before the case is established** The lack of visible figures and tables is a major limitation. The chevron plot analysis requires a more rigorous statistical comparison between linear and polynomial fits. The DLS data should be complemented with a more direct method, such as size-exclusion chromatography coupled to multi-angle light scattering, to confirm the dimeric nature of the intermediate. The HDX-MS data should be quantified to support the claim of native-like protection.
- **Assessment against Nature-style criteria**  
  - Originality: The detection of a kinetic unfolding intermediate for TDP-43 NTD is a novel experimental observation, though it aligns with prior computational predictions. The finding is not entirely unprecedented in the protein folding literature, but its application to TDP-43 is new.  
  - Scientific importance: The work contributes to understanding the conformational landscape of TDP-43 NTD, which is relevant to its function and pathology. However, the direct link to disease mechanisms remains speculative.  
  - Interdisciplinary readership: The topic bridges biophysics, structural biology, and neurodegeneration, and would appeal to a broad audience.  
  - Technical soundness: The multi-probe approach is sound in principle, but the lack of visible data and the indirect nature of some conclusions (e.g., dimeric state) temper confidence.  
  - Readability for nonspecialists: The manuscript is generally well written and accessible, though some sections assume familiarity with protein folding terminology.
- **Recommendation posture** Supportive if technical concerns are resolved. The central claim is plausible and well motivated, but the absence of figures and tables, and the need for additional validation of the dimeric intermediate, prevent full endorsement at this stage.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The authors claim detection of an unfolding intermediate based on multiple spectroscopic probes, but the actual data (figures, tables) are not provided in the supplied material.
- **Evidence pointer** Figures 1-10, Tables S1, location not provided
- **Concern** The manuscript relies entirely on experimental data presented in figures and tables that are not included in the supplied text. Without access to the raw kinetic traces, spectra, and statistical analyses, it is impossible to assess the quality of the data, the appropriateness of the fitting procedures, or the robustness of the reported differences between states.
- **Why it matters** The central claim of the manuscript, the existence of a transient unfolding intermediate, depends on the interpretation of these data. If the data are noisy, poorly fitted, or the differences are within experimental error, the conclusion would be weakened.
- **Resolution test** Provide the figures and tables, along with detailed legends, for inspection. Include representative raw traces and the results of statistical comparisons between fits.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of chevron plot
- **Claim pointer** The authors state that the curvature in the unfolding arm of the chevron plot is indicative of an intermediate, but this interpretation is not unique.
- **Evidence pointer** Section 3.7, Figure 7, location not provided
- **Concern** The downward curvature in the chevron plot is interpreted as evidence for a populated intermediate. However, such curvature can also arise from a Hammond effect, where the transition state moves along the reaction coordinate with denaturant concentration, or from the presence of multiple transition states. The authors do not provide a quantitative analysis to distinguish these possibilities.
- **Why it matters** The chevron plot is a key piece of evidence for the existence of the intermediate. If the curvature is due to other effects, the claim of an intermediate is weakened.
- **Resolution test** Perform a global fit of the chevron plot to a three-state model and compare it statistically to a two-state model with a curved unfolding arm. Report the confidence intervals for the fitted parameters.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Oligomeric state assignment
- **Claim pointer** The authors conclude that the unfolding intermediate is a partially folded dimer based on DLS measurements showing a constant DH.
- **Evidence pointer** Section 3.8, Figure 9, location not provided
- **Concern** The DLS data show that the DH remains approximately constant during unfolding, but this does not unambiguously establish that the intermediate is dimeric. An expanded monomer could have a similar DH to a compact dimer. The authors do not provide a calibration or a direct measurement of the molecular weight of the intermediate.
- **Why it matters** The claim that the intermediate is dimeric is a central finding, with implications for the mechanism of TDP-43 self-assembly. If the intermediate is actually monomeric, the interpretation changes.
- **Resolution test** Use size-exclusion chromatography coupled to multi-angle light scattering (SEC-MALS) or analytical ultracentrifugation to directly determine the molecular weight of the intermediate under the same conditions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Quantification of HDX-MS
- **Claim pointer** The authors state that the HDX-MS results show a native-like protection pattern for the intermediate, but the data are presented only qualitatively.
- **Evidence pointer** Section 3.6, Figure 6, location not provided
- **Concern** The HDX-MS data are described as showing a degree of protection similar to the native state, but no quantitative values (e.g., deuterium uptake levels, protection factors) are provided. Without quantification, it is difficult to assess the extent of structural similarity between the intermediate and the native state.
- **Why it matters** The claim that the intermediate retains native-like secondary structure is based on this qualitative assessment. Quantification would strengthen the conclusion and allow comparison with other states.
- **Resolution test** Provide deuterium uptake curves or protection factors for the intermediate, native, and unfolded states, with appropriate error bars.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** Discussion, Section 4.2
- **Evidence pointer** location not provided
- **Issue** The term "native-like" is used to describe the intermediate's HDX pattern, but the intermediate clearly differs from the native state in fluorescence, CD, and SYPRO Orange binding. This terminology could be misleading.
- **Required correction** Clarify what is meant by "native-like" in the context of HDX, and explicitly state the differences from the native state observed with other probes.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Methods, Section 2.2-2.8
- **Evidence pointer** location not provided
- **Issue** The manuscript reports mean ± SEM values but does not specify the number of replicates (n) for each experiment in the text.
- **Required correction** Include the number of independent replicates for each experiment in the figure legends or methods section.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Contextualization of MD simulations
- **Affected element** Discussion, Section 4.1
- **Evidence pointer** location not provided
- **Issue** The authors reference MD simulations showing intermediate formation within 500 ns, but this timescale is not directly comparable to the experimental timescale of milliseconds. The connection could be clarified.
- **Required correction** Explicitly state that the MD simulations were performed at high temperatures and that the experimental observation is on a different timescale, to avoid confusion.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Speculative claims
- **Affected element** Discussion, Section 4.5
- **Evidence pointer** location not provided
- **Issue** The discussion of the potential role of the intermediate in TDP-43 function and pathology is speculative and not directly supported by the experimental data.
- **Required correction** Soften the language and clearly distinguish between experimental findings and hypotheses.

## Risk / unsupported claims
- The claim that the intermediate forms within 500 ns is based on MD simulations, not experimental data, and should be clearly labeled as such.
- The claim that the intermediate is a partially folded dimer is inferred from DLS data, which may not have sufficient resolution to distinguish it from an expanded monomer.
- The physiological relevance of the intermediate, particularly at low protein concentrations, is not experimentally established.
- The absence of figures and tables makes it impossible to verify the quality and robustness of the reported data.