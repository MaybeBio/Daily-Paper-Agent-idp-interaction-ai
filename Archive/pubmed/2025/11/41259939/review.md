## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, conclusion, data availability, acknowledgements)
- **Assessment boundary** Scientific and technical evaluation of the methodology, data analysis, and claims as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors present a CW-EPR-based methodology to study protein-lipid interactions using spin-labelled Tau protein and lipid vesicles. They claim that spectral decomposition into free and bound components allows quantification of the bound protein fraction, determination of apparent binding affinities through titration, and estimation of binding constants from minimal data points (one to three measurements). The methodology is applied to Tau interacting with POPS and POPS/POPC membranes.
- **Visible evidence base** Figures 1-5 (referenced but not provided), Tables 1-4 (referenced but not provided), equations 1-9, methods descriptions, results narrative
- **Missing materials affecting confidence** Figures 1-5 and Tables 1-4 are referenced but not included in the provided material. Experimental replicates, raw spectra, fitting residuals, and statistical details are not available. The data availability statement indicates data will be made available on request, but no data are provided for verification.

## Reviewer
- **Overall assessment** The manuscript presents a potentially useful methodological framework for quantifying protein-lipid interactions using CW-EPR. The concept of leveraging the quantitative nature of EPR to obtain absolute bound protein concentrations and thereby reduce the number of measurements needed for affinity estimation is interesting and could be of value to the biophysics community. However, the provided material does not include the key figures and tables that would allow verification of the central claims. The error propagation analysis is a strength, but the practical demonstration of the minimal-data approach relies on data not visible in the supplied text. The manuscript would benefit from clearer justification of model selection and a more thorough discussion of the limitations of the approach, particularly regarding the assumption that the two-component decomposition is valid across all conditions tested.
- **Who would be interested in the results, and why** Researchers studying protein-membrane interactions, particularly those working with intrinsically disordered proteins such as Tau. The methodology could also interest biophysicists who use EPR spectroscopy and those seeking quantitative binding measurements in membrane systems where traditional methods (ITC, SPR) are challenging due to membrane heterogeneity. The minimal-data approach may appeal to researchers who need rapid affinity estimates under multiple conditions.
- **Major strengths** The manuscript addresses a real need for quantitative methods to study protein-lipid interactions. The use of EPR to obtain absolute concentrations of bound protein is a genuine advantage over relative methods. The error propagation analysis provides practical guidance for experimental design. The application to two membrane compositions demonstrates the potential utility of the approach. The writing is generally clear and the logical flow from spectral decomposition to binding models to minimal-data strategy is coherent.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** The absence of the actual spectral data, fits, and binding curves in the provided material means the central claims cannot be independently assessed. The validation of the two-component decomposition and the accuracy of the minimal-data approach require the figures and tables.
- **Assessment against Nature-style criteria** Originality: The approach of using EPR for absolute quantification of bound protein in protein-lipid systems is not entirely new, but the systematic framework for minimal-data affinity estimation has elements of novelty. Scientific importance: The work addresses a methodological gap, but the significance is moderate rather than transformative. Interdisciplinary readership: The manuscript is primarily of interest to biophysicists and EPR specialists; the broader cell biology community may find limited direct relevance. Technical soundness: The theoretical framework appears sound, but verification is impossible without the figures and tables. Readability for nonspecialists: The manuscript is reasonably accessible, though some familiarity with EPR spectroscopy is assumed.
- **Recommendation posture** Supportive if technical concerns are resolved and the missing data are provided for verification.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence availability
- **Claim pointer** The manuscript claims that "all spectra can be accurately modeled using this two-component approach" and that the extracted bound fraction θ yields reliable binding parameters.
- **Evidence pointer** Figures 1-5, Tables 1-4; location not provided
- **Concern** The central evidence for the methodology, including the spectral lineshapes, the two-component fits, the binding curves, and the comparison of minimal-data versus full-data results, is contained in figures and tables that are not included in the provided material. Without these, the accuracy of the spectral decomposition, the quality of the fits, and the validity of the binding parameters cannot be assessed.
- **Why it matters** The entire case for the methodology rests on the demonstration that the two-component decomposition is accurate and that the extracted binding parameters are reliable. If the fits are poor or the decomposition is ambiguous, the conclusions would not be supported.
- **Resolution test** Provide the figures and tables, including representative spectra with fits and residuals, the full binding curves with model fits, and the comparison of parameters obtained from full versus minimal data.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Model validation
- **Claim pointer** The authors state that "the data are best described by the non-stoichiometric quadratic model or Hill model" and that the Hill model "provides the most reliable description of the Tau-lipid interaction."
- **Evidence pointer** Figure 4, Table 2; location not provided
- **Concern** The selection of the best-fitting model is stated but the criteria for model comparison are not described. It is unclear whether the models were compared using statistical measures such as AIC, BIC, or F-tests, or whether the choice was based on visual inspection. The reported high variance (almost 100%) for the non-stoichiometric model raises questions about the reliability of this model, yet it is still considered acceptable.
- **Why it matters** The choice of model directly affects the interpretation of the binding parameters. If the model selection is not rigorous, the reported affinities and stoichiometries may not be meaningful.
- **Resolution test** Describe the model comparison criteria and provide statistical measures supporting the choice of the Hill model over the alternatives. Report confidence intervals for all fitted parameters.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Minimal-data validation
- **Claim pointer** The authors claim that "a single measurement provides the absolute concentration of free and bound protein" and that "a single EPR measurement can be used to estimate an apparent binding constant."
- **Evidence pointer** Section "Application physiological conditions", Table 4; location not provided
- **Concern** The validation of the minimal-data approach is presented in Table 4, which is not provided. The comparison between K50 obtained from three points (0.65 ± 0.04 mM) and from the full dataset (0.64 ± 0.04 mM) is stated to be "identical within error," but the uncertainty calculation for the single-point method is not described in detail. The authors note that nH is less robustly estimated from minimal data, which is acknowledged, but the practical implications of this limitation are not fully discussed.
- **Why it matters** The minimal-data approach is a key selling point of the manuscript. If the validation is not clearly demonstrated with the actual data, the practical utility of the method is not established.
- **Resolution test** Provide Table 4 and a detailed description of how uncertainties are propagated for the single-point and three-point estimates. Discuss the conditions under which the minimal-data approach would fail.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Assumption validity
- **Claim pointer** The authors assume that the two spectral components correspond to "free" and "bound" Tau and that the bound component reflects a direct interaction between the spin label and the lipid membrane.
- **Evidence pointer** Section "CW-EPR spectra of tau in presence of lipids can be decomposed into two components"; location not provided
- **Concern** The assignment of the slow-motion component to a bound state is plausible but not rigorously established. It is possible that the spectral change could arise from other effects, such as changes in local viscosity, aggregation of Tau, or non-specific interactions. The authors do not provide control experiments (e.g., with a non-binding protein or with neutral lipids) to rule out these alternatives.
- **Why it matters** If the slow component does not exclusively represent bound Tau, the quantification of bound protein would be incorrect, and all derived binding parameters would be compromised.
- **Resolution test** Provide control experiments demonstrating that the spectral change is specific to the Tau-lipid interaction. Discuss and rule out alternative explanations for the observed lineshape change.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section, spin labeling
- **Evidence pointer** Section "Spin labeling of Tau"; location not provided
- **Issue** The labeling efficiency is reported as 60%, but the method used to determine this value is not described. It is also unclear whether the 60% efficiency was consistent across preparations and whether the presence of unlabeled Tau affects the spectral decomposition.
- **Required correction** Describe how labeling efficiency was determined and discuss the potential impact of unlabeled protein on the analysis.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section, liposome preparation
- **Evidence pointer** Section "Liposome formulation into multilamellar vesicles (MLVs)"; location not provided
- **Issue** The method for preparing MLVs is described briefly. It is not stated whether the vesicle size distribution was characterized, which could affect the reproducibility of the binding measurements.
- **Required correction** Provide details on vesicle characterization (e.g., dynamic light scattering) or state that size was not measured and discuss the potential implications.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results section, binding parameters
- **Evidence pointer** Table 2; location not provided
- **Issue** The uncertainties on the fitted parameters are reported as percentages, but the number of independent experiments and the statistical treatment are not described. It is unclear whether the uncertainties represent standard deviations, standard errors, or confidence intervals.
- **Required correction** Specify the number of replicates and the statistical methods used to derive the reported uncertainties.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Generalizability
- **Affected element** Conclusion
- **Evidence pointer** Conclusion section; location not provided
- **Issue** The authors state that the methodology "is expected to be applicable to other proteins," but this claim is not supported by any data or discussion of the conditions under which the approach would work. The requirement that the bound state must produce a distinct EPR lineshape is acknowledged, but the range of systems for which this holds is not discussed.
- **Required correction** Add a brief discussion of the generalizability of the approach and the conditions required for its application.

## Risk / unsupported claims
- The claim that "a single EPR measurement can be used to estimate an apparent binding constant" is not fully supported by the provided material, as the validation data (Table 4) are not visible.
- The claim that the Hill model "provides the most reliable description" of the Tau-lipid interaction is not supported by a described model comparison procedure.
- The claim that the methodology is "expected to be applicable to other proteins" is speculative and not supported by data.
- The assertion that the two-component decomposition provides "absolute concentrations of bound and free protein" relies on the assumption that the spectral components are correctly assigned, which is not rigorously established.
- The statement that "a single measurement provides the absolute concentration of free and bound protein" is presented as a general capability, but the accuracy of this claim depends on the validity of the decomposition and the calibration of the spin label concentration, which are not fully described.