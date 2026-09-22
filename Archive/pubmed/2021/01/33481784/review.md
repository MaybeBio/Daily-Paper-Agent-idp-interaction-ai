## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific and technical soundness of the software and its validation, as presented in the provided manuscript
- **Shared manuscript claim summary** The authors present DEER-PREdict, an open-source Python software for predicting DEER distance distributions and PRE rates from conformational ensembles using a rotamer library approach. They demonstrate its performance on three protein systems and report computational efficiency and accuracy.
- **Visible evidence base** Abstract, Introduction, Design and implementation, Results (three case studies), Conclusion, Availability section. Figures referenced but not provided. Supporting information referenced but not provided.
- **Missing materials affecting confidence** Figures 1-4, S1-S6 Figs, S1 Text, code repository contents, test data, and detailed benchmark comparisons are not available in the supplied material. This limits full verification of quantitative claims.

## Reviewer
- **Overall assessment** The manuscript describes a useful and timely software tool that addresses a real need in the structural biology community, namely the efficient prediction of spin-labeling EPR and NMR observables from conformational ensembles. The implementation appears technically sound, building on established rotamer library methodology. However, the validation presented is limited in scope and depth, and several quantitative claims cannot be fully assessed from the provided material. The manuscript would benefit from more rigorous benchmarking against existing tools and a clearer demonstration of the software's advantages.

- **Who would be interested in the results, and why** Researchers in structural biology, biophysics, and computational chemistry who use EPR (DEER/PELDOR) or NMR (PRE) spectroscopy to study intrinsically disordered proteins, multi-domain proteins, or conformational ensembles. The software's ability to handle large ensembles from MD simulations efficiently makes it relevant to those integrating experimental data with molecular dynamics. The open-source nature and Python API also appeal to method developers and bioinformaticians.

- **Major strengths** 
  1. Addresses a clear methodological gap: efficient calculation of DEER and PRE observables from large conformational ensembles, which is increasingly needed in the field.
  2. Builds on established rotamer library approach, providing continuity with prior work while extending it to ensemble calculations.
  3. Open-source, well-documented, and available through multiple channels (GitHub, PyPI, Zenodo), promoting reproducibility and community use.
  4. Demonstrates application to three experimentally characterized systems, providing some validation of the approach.
  5. The software's design allows integration with reweighting schemes, which is a valuable feature for integrative modeling.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation completeness
- **Claim pointer** The manuscript claims that DEER-PREdict provides accurate predictions of DEER and PRE observables, demonstrated through three case studies.
- **Evidence pointer** Results section, Figures 2-4 (not provided)
- **Concern** The validation is limited to three protein systems, all of which are folded proteins. The abstract and introduction emphasize the importance of the tool for intrinsically disordered and multi-domain proteins, yet no validation is presented for such systems. This is a significant gap, as the behavior of rotamer libraries and the accuracy of predictions may differ substantially for disordered proteins where the local environment and dynamics are different.
- **Why it matters** The stated motivation for the software is to facilitate studies of intrinsically disordered and multi-domain proteins. Without validation on such systems, the central claim of the tool's utility for the target audience is not established.
- **Resolution test** Provide additional validation on at least one intrinsically disordered protein or a multi-domain protein with known conformational heterogeneity, comparing predictions to experimental DEER/PRE data.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Benchmarking and comparative performance
- **Claim pointer** The manuscript implies that DEER-PREdict is efficient and suitable for large ensembles, but no quantitative comparison with existing tools (e.g., MMM, RotamerConvolveMD) is provided.
- **Evidence pointer** Design and implementation, Results section
- **Concern** The authors mention that MMM operates on single structures and that wrapper scripts were previously needed, but they do not provide a direct performance comparison (e.g., runtime, memory usage, accuracy) between DEER-PREdict and existing tools such as MMM or RotamerConvolveMD. The claim of "efficient calculation" is not substantiated with quantitative benchmarks.
- **Why it matters** For a software tool, demonstrating clear advantages over existing alternatives is crucial for adoption. Without benchmarks, users cannot assess whether switching to DEER-PREdict is worthwhile.
- **Resolution test** Include a benchmark section comparing runtime and accuracy of DEER-PREdict against MMM and RotamerConvolveMD on the same test systems and ensembles.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Sensitivity to parameters and assumptions
- **Claim pointer** The manuscript states that results are "virtually insensitive" to the Z cutoff between 0.05 and 0.5, but this is only shown in a supplementary figure.
- **Evidence pointer** Design and implementation, S1 Fig (not provided)
- **Concern** The sensitivity analysis is limited to the Z cutoff parameter. Other parameters, such as the rotamer library choice (175 K vs 298 K), the sigma_scaling parameter, and the low-pass filter standard deviation, are not systematically explored. The choice of rotamer library could significantly affect predictions, especially for different protein environments.
- **Why it matters** Users need to understand the robustness of the software to parameter choices to use it confidently. Limited sensitivity analysis may lead to inappropriate parameter selection in practice.
- **Resolution test** Provide a more comprehensive sensitivity analysis covering key parameters (rotamer library, sigma_scaling, filter_stdev) across the test systems, and discuss the implications for users.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility and accessibility of validation data
- **Claim pointer** The manuscript states that a Jupyter notebook to reproduce results is available in the GitHub repository.
- **Evidence pointer** Results section, Availability section
- **Concern** While the availability of a notebook is commendable, the manuscript does not provide details on the exact input structures, simulation parameters, or experimental data used for validation. Without this information, independent reproduction of the results is difficult.
- **Why it matters** Reproducibility is a core requirement for scientific software. The lack of detailed input specifications undermines the ability of others to verify the claims.
- **Resolution test** Provide a detailed description of all input files, simulation parameters, and experimental datasets used in the case studies, either in the manuscript or as supplementary material.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Equation 4
- **Evidence pointer** Design and implementation, Eq 4
- **Issue** The DEER kernel expression in Eq 4 appears to have a typographical issue. The term "cos(ω)FrC(6ωtπ)" is unclear. It should likely be "cos(ωt)FrC(6ωt/π)" or similar. The current form is dimensionally inconsistent.
- **Required correction** Verify and correct the mathematical expression in Eq 4. Ensure all variables are properly defined and the equation is dimensionally consistent.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of documentation
- **Affected element** Parameter definitions
- **Evidence pointer** Design and implementation, Eq 8-11
- **Issue** The parameters τs, τi, and S are introduced but not fully defined in the main text. The relationship between these parameters and the rotamer library approach could be clarified.
- **Required correction** Provide explicit definitions of all parameters in Eqs 8-11 and explain how they relate to the rotamer library and the physical model.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Language and style
- **Affected element** Results section, Case study 2
- **Evidence pointer** Results section, Case study 2
- **Issue** The phrase "the discrepancy between predicted and calculated P(r)'s" is confusing. It should be "predicted and experimental" or "calculated and experimental".
- **Required correction** Correct the wording to clearly distinguish between predicted/calculated and experimental data.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Case study 1
- **Evidence pointer** Results section, Case study 1
- **Issue** The manuscript states that the analysis of a 500-ns trajectory with 1,000 frames takes 13 seconds, but does not specify the hardware beyond "1.7 GHz processor". This is insufficient for meaningful performance assessment.
- **Required correction** Provide more detailed hardware specifications (e.g., CPU model, number of cores, RAM) and clarify whether the timing is for a single core or parallel execution.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Scope of application
- **Affected element** Conclusion
- **Evidence pointer** Conclusion
- **Issue** The conclusion mentions future extension to FRET data, but this is not discussed in the main text. A brief mention in the introduction or design section would provide better context.
- **Required correction** Add a brief statement in the introduction or design section about the planned or potential extension to FRET predictions.

## Risk / unsupported claims
- The claim that DEER-PREdict is suitable for intrinsically disordered and multi-domain proteins is not supported by validation data, as all test cases are folded proteins.
- The claim of "efficient calculation" is not quantitatively benchmarked against existing tools.
- The statement that results are "virtually insensitive" to the Z cutoff is only supported by a supplementary figure not provided in the supplied material.
- The accuracy of PRE predictions is demonstrated on a single protein (ACBP), which is insufficient to establish general reliability.
- The manuscript mentions that the software has been "previously used" for calculations in other studies, but no specific citations or details are provided in the supplied text.
- The claim that the software can be "readily extended" to non-protein biomolecules and additional rotamer libraries is plausible but not demonstrated.