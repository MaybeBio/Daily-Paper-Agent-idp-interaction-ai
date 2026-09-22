## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract
- **Shared manuscript claim summary** The authors propose that biophysical features from molecular dynamics simulations of intrinsically disordered regions can improve interpretation and prediction of missense variant pathogenicity, particularly for long IDRs, and that pathogenic variants in long versus short IDRs exhibit distinct biophysical signatures.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary materials provided
- **Missing materials affecting confidence** Full manuscript, methods description, simulation parameters, validation datasets, performance metrics, statistical analyses, and all figures and tables

## Reviewer
- **Overall assessment** The abstract presents a potentially valuable direction for interpreting variant effects in IDRs, where conservation-based predictors are known to underperform. The central hypothesis, that MD-derived biophysical features can complement conservation signals, is scientifically plausible and of interest to the variant interpretation community. However, the abstract alone provides insufficient detail to evaluate the rigor of the computational pipeline, the validity of the biophysical feature extraction, the statistical robustness of the reported differences between long and short IDRs, or the actual predictive performance of MDmis relative to existing methods. The claims as stated are not fully assessable from the supplied material.
- **Who would be interested in the results, and why** Researchers in clinical genomics, variant effect prediction, and computational biophysics would be interested. The work addresses a recognized gap in pathogenicity prediction for IDRs, which constitute a large fraction of the proteome and are enriched in disease-associated variants. The potential to link molecular simulation to clinical interpretation could appeal to both method developers and clinicians seeking mechanistic insight beyond conservation scores.
- **Major strengths** The problem is well motivated and addresses a genuine limitation of current variant effect predictors. The use of MD simulations to extract biophysical features for IDR variants is conceptually novel and could provide mechanistic interpretability that conservation-based methods lack. The distinction between long and short IDRs is a thoughtful stratification that may reveal biologically meaningful heterogeneity.
- **Major Concerns**  
  - **Concern ID** R1-M1  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Technical soundness  
    **Claim pointer** The abstract claims that MDmis achieves strong predictive accuracy of pathogenicity for variants in long IDRs when combined with conservation information.  
    **Evidence pointer** Abstract only; no performance metrics, benchmark datasets, or comparison baselines provided  
    **Concern** The abstract reports predictive accuracy without any quantitative details. No area under the receiver operating characteristic curve, precision recall values, or comparison to existing predictors such as PrimateAI or AlphaMissense are given. Without these, the claim of strong accuracy cannot be evaluated.  
    **Why it matters** Predictive performance is the central quantitative claim of the method. If the performance is not benchmarked against established tools on standard variant effect datasets, the utility of MDmis remains unsubstantiated.  
    **Resolution test** Provide performance metrics on a well defined validation set, with comparisons to at least two existing predictors, including confidence intervals and statistical significance tests.  
  - **Concern ID** R1-M2  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Technical soundness  
    **Claim pointer** The abstract states that pathogenic variants in long IDRs manifest with transient order and depleted solvent access compared to those in short IDRs.  
    **Evidence pointer** Abstract only; no simulation details or feature definitions provided  
    **Concern** The biophysical features transient order and depleted solvent access are not defined. It is unclear how these are computed from MD trajectories, what order parameters are used, and how solvent access is quantified. Without definitions and validation of these features, the reported difference between long and short IDRs cannot be assessed.  
    **Why it matters** These features are the mechanistic basis for the entire approach. If they are not rigorously defined and shown to be reproducible, the biological interpretation is unsupported.  
    **Resolution test** Define each feature precisely, describe the MD simulation protocol, and show that the features are stable across simulation replicates and consistent with known IDR properties.  
  - **Concern ID** R1-M3  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Statistical rigor  
    **Claim pointer** The abstract claims stronger evidence for pathogenic effects in long IDRs compared to short IDRs based on MD simulations of single missense variants.  
    **Evidence pointer** Abstract only; no statistical tests or effect sizes reported  
    **Concern** No statistical framework is described. It is unclear how many variants were simulated, how significance was assessed, and whether multiple testing corrections were applied. The claim of stronger evidence may be driven by sample size or selection bias.  
    **Why it matters** The distinction between long and short IDRs is a key finding. Without proper statistical support, this could be a spurious stratification artifact.  
    **Resolution test** Report variant counts, effect sizes, confidence intervals, and statistical tests with multiple testing correction for the long versus short IDR comparison.  
  - **Concern ID** R1-M4  
    **Severity** Major  
    **Blocking** No  
    **Axis** Reproducibility  
    **Claim pointer** The method MDmis uses biophysical features extracted from MD simulations to predict pathogenicity.  
    **Evidence pointer** Abstract only; no method description or code availability stated  
    **Concern** The abstract does not describe the machine learning model, feature selection procedure, training data, or how conservation information is integrated. No mention of code or data availability is made.  
    **Why it matters** Reproducibility is essential for a computational method. Without a clear description of the model architecture and training pipeline, other groups cannot apply or validate the method.  
    **Resolution test** Provide a detailed methods section, release code and simulation data, and specify the model training and evaluation protocol.
- **Minor Comments**  
  - **Concern ID** R1-m1  
    **Severity** Minor  
    **Axis** Clarity  
    **Affected element** Definition of long and short IDRs  
    **Evidence pointer** Abstract only  
    **Issue** The threshold distinguishing long from short IDRs is not stated.  
    **Required correction** Specify the length cutoff and justify it biologically or empirically.  
  - **Concern ID** R1-m2  
    **Severity** Minor  
    **Axis** Completeness  
    **Affected element** Variant dataset description  
    **Evidence pointer** Abstract only  
    **Issue** The source and composition of the variant dataset used for training and evaluation are not described.  
    **Required correction** State the origin of the variants, the number of pathogenic and benign variants, and whether the dataset is balanced.  
  - **Concern ID** R1-m3  
    **Severity** Minor  
    **Axis** Interpretability  
    **Affected element** Claim of functional interpretation  
    **Evidence pointer** Abstract only  
    **Issue** The abstract claims biophysical interpretation but does not explain how the MD features map to biological mechanisms.  
    **Required correction** Provide a conceptual framework linking each feature to a biophysical property relevant to IDR function or dysfunction.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3. The absence of quantitative performance data, undefined biophysical features, and lack of statistical rigor prevent the central claims from being verified.
- **Assessment against Nature-style criteria**  
  Originality: The idea of using MD simulations for variant interpretation in IDRs is novel and not widely explored. Scientific importance: The problem is significant given the prevalence of IDRs in disease. Interdisciplinary readership: The work bridges biophysics and clinical genomics, which could attract a broad audience. Technical soundness: Not assessable from the abstract; the lack of methodological detail and quantitative results is a major limitation. Readability for nonspecialists: The abstract is accessible but uses terms such as transient order without definition, which may confuse readers outside the simulation field.
- **Recommendation posture** Currently not established from the provided evidence. The conceptual direction is promising, but the abstract does not provide sufficient technical or statistical support for the claims. A full manuscript with detailed methods, benchmarks, and statistical analyses would be required to assess whether the case can be made.

## Risk / unsupported claims
- The claim of strong predictive accuracy for MDmis is unsupported without performance metrics or comparisons.
- The claim that pathogenic variants in long IDRs show transient order and depleted solvent access is unsupported without feature definitions and statistical evidence.
- The claim of stronger evidence for pathogenic effects in long IDRs is unsupported without effect sizes and significance tests.
- The general statement that MD simulations can help understand drivers of predictive performance is not substantiated by any presented analysis.