## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions, supplementary material list)
- **Assessment boundary** Scientific content, methodological soundness, claims versus evidence, and presentation quality as presented in the provided text
- **Shared manuscript claim summary** The authors use isotope-labeled and unlabeled FTIR spectra to reweight simulated ensembles of the intrinsically disordered elastin-like peptide GVGVPGVG, demonstrating that ensemble weights are underdetermined by ensemble-averaged data, identifying informative labels and frequency regions, and concluding that the peptide is predominantly extended with CHARMM36m providing more accurate sampling than CHARMM27.
- **Visible evidence base** Abstract, full introduction, full methods, full results and discussion, full conclusions, supplementary material list, acknowledgments
- **Missing materials affecting confidence** Figures 1–10 and all supplementary figures/tables referenced but not provided; experimental spectra details beyond reference to ref. 57; specific numerical values for populations, error metrics, and hyperparameter selections; full details of the Bayesian refinement implementation

## Reviewer

- **Overall assessment** This manuscript addresses an important problem in IDP structural biology: how to use isotope-labeled IR spectroscopy to constrain conformational ensembles. The authors present a systematic analysis of label informativeness, demonstrate underdetermination of ensemble weights, and propose a practical framework for experiment design. The work is timely and relevant, but the core conclusions rest heavily on figures and quantitative details not available in the provided text. The claim that the extended state dominates and that CHARMM36m is more accurate is plausible but cannot be fully evaluated without the numerical results. The methodological contributions, particularly the identification of informative regions and the caution regarding multi-label coupling errors, are valuable. However, the manuscript would benefit from clearer articulation of the uncertainty in the refined populations and a more direct comparison with alternative approaches.

- **Who would be interested in the results, and why** Researchers in biophysical chemistry, computational biophysics, and structural biology of IDPs. Specifically, those developing or using spectroscopic methods (IR, 2D IR) for disordered proteins, those working on ensemble refinement methods integrating experiment and simulation, and those studying elastin-like peptides or similar IDP model systems. The practical guidance on isotope label selection will interest experimentalists planning such studies.

- **Major Strengths**
  1. The manuscript addresses a significant and underappreciated problem: the underdetermination of ensemble weights from ensemble-averaged spectroscopic data.
  2. The systematic analysis of which labels and frequency regions are most informative, and the demonstration that multi-label coupling errors can bias results, is a practical and important contribution.
  3. The integration of MD simulation, spectral mapping, and Bayesian refinement is methodologically sound and well described.
  4. The authors are appropriately cautious about the limitations of their approach and acknowledge the influence of prior distributions.
  5. The proposed framework for planning isotope-labeling experiments is practical and likely to be adopted by the community.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "the extended state is the dominant conformer, with its population increasing from the MD prior in both cases" and that "CHARMM36m likely provides a closer estimate to the true populations."
- **Evidence pointer** Results and Discussion, Figures 4, 6, 9, 10; location not provided for specific numerical values
- **Concern** The central quantitative conclusions regarding the refined populations and the comparison between force fields are presented without numerical values in the text. The figures are referenced but not available for review. Without specific population estimates, confidence intervals, or error bars, the strength of the claim that the extended state dominates cannot be assessed. Furthermore, the statement that CHARMM36m "likely provides a closer estimate" appears to be based on qualitative reasoning about systematic errors rather than a quantitative comparison metric.
- **Why it matters** The primary scientific conclusion of the paper is the experimentally informed population estimate. If the numerical support is weak or the uncertainty is large, the conclusion may not be robust. The comparison between force fields is also a key claim that requires quantitative justification.
- **Resolution test** Provide numerical population estimates with uncertainties for both force fields and all refinement schemes. Include a quantitative metric for comparing force field accuracy, such as the effective sample size, posterior predictive checks, or a direct comparison of refined populations to independent experimental observables.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency
- **Claim pointer** The authors state that "we identify which labels and frequency regions maximize structural information while minimizing sensitivity to simulation error" and use a thresholding procedure with an information function D(ω).
- **Evidence pointer** Methods, Bayesian refinement section; Results and Discussion, Analysis of state spectra section; Figures 8, S15
- **Concern** The information function D(ω) and the thresholding procedure are described, but the rationale for the specific threshold values (D > 0.0015, σ = 0.0005) is deferred to supplementary material. The sensitivity of the results to these choices is not discussed in the main text. Since the selection of informative regions is a central methodological contribution, the robustness of the conclusions to these parameters must be established.
- **Why it matters** If the results are highly sensitive to the arbitrary choice of thresholds, the framework's practical utility is diminished. Readers need to understand how to choose these parameters for their own systems.
- **Resolution test** Provide a sensitivity analysis in the main text or clearly state the range of thresholds over which the conclusions are unchanged. Justify the specific values chosen with reference to the physical properties of the spectra.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Claim overreach
- **Claim pointer** The authors conclude that "the refined populations more closely resemble the CHARMM36m prior populations, which favor more extended conformers. This validates the improvements made to the parametrization of the CHARMM36m force field."
- **Evidence pointer** Conclusions; Results and Discussion, Ensemble refinement results
- **Concern** The term "validates" is too strong. The results are consistent with CHARMM36m being more accurate, but validation would require independent experimental confirmation or a more rigorous statistical comparison. The authors themselves note that the prior distribution significantly affects the results, so the agreement with CHARMM36m could reflect the prior's influence rather than the force field's accuracy.
- **Why it matters** Overstating the conclusion could mislead readers into thinking the force field question is settled, when in fact the evidence is indirect.
- **Resolution test** Soften the language to "consistent with" or "supports" rather than "validates." Alternatively, provide additional evidence, such as a comparison to an independent experimental observable not used in the refinement.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Comparison with prior work
- **Claim pointer** The authors compare their findings to Selig et al. who "reported that the shorter ELP VPGVG primarily adopts a turned (rather than extended) structure."
- **Evidence pointer** Results and Discussion, Ensemble refinement results
- **Concern** The comparison with Selig et al. is brief and dismissive, noting that "direct comparison is not possible since their experiments were performed at a different temperature, protonation, and solvent conditions." If direct comparison is not possible, the relevance of the comparison is unclear. Either provide a more detailed discussion of how the different conditions might explain the discrepancy, or remove the comparison.
- **Why it matters** The comparison is potentially important for contextualizing the results, but as presented it raises questions without providing answers.
- **Resolution test** Expand the discussion to explain how the different experimental conditions might affect the turn population, or remove the comparison if it cannot be meaningfully interpreted.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods, FTIR Spectra section
- **Evidence pointer** "All labels were 13C18O except for G3 in the triply labeled peptide, which was 13CO to distinguish it spectrally from the other labels in that construct."
- **Issue** The rationale for using 13CO for G3 in the triple label is stated, but the spectral consequences are not explained. How does the smaller redshift of 13CO (41 cm−1) versus 13C18O (60 cm−1) affect the analysis?
- **Required correction** Briefly explain the spectral separation achieved by this choice and whether it introduces any complications in the analysis.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Results and Discussion, Dimensionality reduction section
- **Evidence pointer** "Using a 5 μs trajectory with CHARMM36m featurized by interatomic distances of amide C atoms at least two residues apart, we found that two implied time scales were well-separated from others (Figure S3)."
- **Issue** The 5 μs trajectory is mentioned here, but the Methods section describes 500 ns simulations. The relationship between these two simulations is unclear.
- **Required correction** Clarify whether the 5 μs trajectory is a separate, longer simulation used only for state identification, and explain why it was not used for the spectral analysis.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, Bayesian refinement section
- **Evidence pointer** "We note that the definition of θ is different than that of Feng et al."
- **Issue** The difference in the definition of θ is noted but not explained. This is important for readers familiar with the Feng et al. method.
- **Required correction** Briefly state how the definition differs and why the change was made.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results and Discussion, Analysis of state spectra section
- **Evidence pointer** "While G1 was synthesized on the N terminus to probe the dynamics, isotope labeling redshifted it into the congested main band, rendering it ineffective."
- **Issue** This is an important practical lesson, but it is presented only in the conclusions. It would be more useful to see this discussed in the results where the G1 data are first presented.
- **Required correction** Consider moving or repeating this observation in the results section where the G1 label is discussed.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Conclusions
- **Evidence pointer** "the spectral information remains fundamentally congested; the isotope-labeled peaks span a window of 40–50 cm−1 with homogeneous linewidths of 10–15 cm−1 which only shift a few wavenumbers with conformational variation."
- **Issue** This is a key limitation, but the numbers are presented without context. How do these values compare to the shifts expected from the conformational changes of interest?
- **Required correction** Provide context for these numbers, such as the typical frequency shift expected for the turn formation or bend formation.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Quantitative population estimates with uncertainties must be provided in the text or clearly accessible in the figures.
  - R1-M2: Sensitivity analysis for the thresholding parameters must be presented.
  - R1-M3: The claim of "validation" of CHARMM36m must be softened or supported with additional evidence.
  - The relationship between the 5 μs trajectory used for state identification and the 500 ns trajectories used for spectral analysis must be clarified.

- **Assessment against Nature-style criteria**
  - **Originality**: The work is original in its systematic analysis of label informativeness for IDP ensemble refinement. While the general approach of combining MD with spectroscopic data is established, the specific focus on label selection and the demonstration of underdetermination is novel.
  - **Scientific importance**: The problem addressed is important for the IDP community. The finding that ensemble weights are underdetermined by ensemble-averaged data has implications beyond IR spectroscopy. The practical guidance for experiment design is valuable.
  - **Interdisciplinary readership**: The work bridges physical chemistry, biophysics, and computational methods. It will appeal to a specialized but significant audience. The broader IDP community will find the conclusions relevant, though the technical detail may limit accessibility.
  - **Technical soundness**: The methods are appropriate and well described, but the lack of numerical results in the text prevents full assessment. The sensitivity of the conclusions to key parameters is not established in the main text.
  - **Readability for nonspecialists**: The manuscript is clearly written and the logic is easy to follow. However, the heavy reliance on figures and the lack of quantitative summaries in the text make it difficult for nonspecialists to assess the strength of the conclusions. The abstract is accessible, but the results section requires significant background knowledge.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important problem and presents a useful framework, but the central quantitative claims must be substantiated with numerical results and sensitivity analyses. The methodological contributions are sound and likely to be influential, but the current presentation does not allow full evaluation of the conclusions.