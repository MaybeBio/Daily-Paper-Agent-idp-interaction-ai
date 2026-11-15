## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors propose a mechanistic framework for predicting biomolecule partitioning in aqueous two-phase systems (ATPS) based on quantifiable protein biophysical properties, using SARS-CoV-2 spike protein variants as a model. They combine evaporating sessile droplet LLPS, tie-line-resolved phase diagrams, microfluidic picoliter-droplet assays, and polymer-engineered ATPS with PEG-PPG-PEG triblock copolymer. AlphaFold3 structural analysis, Kyte-Doolittle hydrophobicity, and isoelectric point calculations are integrated with multivariate linear regression. A Collander-type inter-system correlation is established. All variants partition preferentially into the dextran-rich phase, with enrichment amplified by longer tie-lines and the more hydrophobic polymer system. The Omicron variant shows the weakest enrichment. Partition coefficients correlate with hydrophobicity and isoelectric point, and obey a Collander-type relationship. An optimized ATPS pre-concentration module enhances an ELONA assay sensitivity by 11.7-fold.
- **Visible evidence base** Abstract text only; no numerical data, figures, tables, or methodological details provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, experimental protocols, statistical analyses, AlphaFold3 confidence metrics, regression model diagnostics, ELONA assay details, and validation datasets

## Reviewer
- **Overall assessment** The abstract presents a conceptually appealing and potentially generalizable framework for ATPS design, with a strong translational component demonstrated through assay sensitivity enhancement. However, the evidence base available for review is limited to the abstract, which precludes verification of the mechanistic claims, statistical robustness, and generalizability. The central claim that partitioning can be predicted mechanistically from biophysical properties is plausible but not fully established from the supplied material. The work is likely to interest researchers in bioseparations, bioprocess engineering, and molecular biophysics, and the integration of computational structural prediction with experimental phase behavior is timely. Nevertheless, several technical details and validations are absent, and the strength of the conclusions cannot be assessed without the full data.
- **Who would be interested in the results, and why** Researchers in bioseparations and downstream processing, particularly those working on ATPS for protein purification, would find the property-driven design framework directly applicable. The SARS-CoV-2 spike protein context and the ELONA integration will appeal to the diagnostic and virology communities. Computational biophysicists interested in linking sequence-derived properties to phase behavior may also find the approach valuable. The Collander-type correlation offers a practical tool for formulation transfer, which is of interest to process engineers seeking to reduce empirical screening.
- **Major strengths** The hypothesis is clearly articulated and mechanistically motivated. The use of multiple complementary experimental techniques, including microfluidic assays and tie-line-resolved phase diagrams, suggests methodological rigor. The integration of AlphaFold3-based structural analysis with classical hydrophobicity and isoelectric point calculations is innovative. The demonstration of an 11.7-fold sensitivity enhancement in a functional assay provides a tangible application. The Collander-type correlation is a pragmatic approach to test transferability across formulations.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4  
  - R1-M5
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3  
  - R1-m4
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5
- **Assessment against Nature-style criteria**  
  Originality: The concept of linking protein biophysical properties to ATPS partitioning via a mechanistic model is not entirely new, but the specific combination of AlphaFold3 structural prediction, tie-line-resolved analysis, and Collander-type transferability testing offers a fresh angle. The application to SARS-CoV-2 variants and the ELONA integration add novelty.  
  Scientific importance: If fully validated, the framework could reduce empirical screening in ATPS design, which is a significant practical advance. The generalizability claim, however, is not yet supported by the abstract alone.  
  Interdisciplinary readership: The work bridges biophysics, colloid science, and diagnostic assay development, which could attract a broad readership. The abstract is written in a way that is accessible to nonspecialists, though some terms such as "Collander-type" and "tie-line-resolved" may require context.  
  Technical soundness: The abstract suggests a well-designed experimental matrix, but the absence of statistical details, model validation metrics, and control experiments prevents an assessment of technical soundness.  
  Readability for nonspecialists: The abstract is concise and logically structured, but the density of techniques and variables may challenge readers outside the immediate field.  
  Overall, the work has potential for a high-impact venue, but the current evidence base is insufficient to confirm that it meets Nature-level standards of generalizability and mechanistic proof.
- **Recommendation posture** Supportive if technical concerns are resolved. The framework is promising and the application is compelling, but the abstract-level evidence does not yet establish the mechanistic and predictive claims. Full data and validation are required before the case is convincing.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** "Partition coefficients correlated strongly with hydrophobicity and isoelectric point"  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The abstract reports strong correlations but provides no correlation coefficients, p-values, sample sizes, or model fit statistics. It is unclear how many variants were used (four spike variants are mentioned, but the Omicron receptor-binding domain is a subdomain, not a full variant) and whether the regression was performed on individual data points or averaged values.  
- **Why it matters** A claim of strong correlation with only four data points is statistically fragile. Without measures of uncertainty and model diagnostics, the predictive power of the framework cannot be evaluated.  
- **Resolution test** Provide correlation coefficients, confidence intervals, p-values, and the number of independent measurements. Show residual plots and cross-validation results to demonstrate that the model generalizes beyond the training set.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Mechanistic attribution  
- **Claim pointer** "confirming hydrophobic interactions as the dominant partitioning mechanism"  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The abstract attributes the dominant mechanism to hydrophobic interactions based on enhanced partitioning in the more hydrophobic PEG-PPG-PEG system. However, changing polymer chemistry alters multiple system properties simultaneously, including viscosity, excluded volume, and hydrogen bonding capacity. The claim of dominance is not supported without systematic variation of hydrophobicity while holding other factors constant.  
- **Why it matters** The mechanistic claim is central to the framework's generalizability. If other factors contribute significantly, the predictive model based on hydrophobicity and isoelectric point may fail for other biomolecules.  
- **Resolution test** Include experiments with a series of polymers of graded hydrophobicity, or use additives to modulate hydrophobic interactions independently. Show that partitioning changes monotonically with a quantitative hydrophobicity parameter and that other system properties are controlled or accounted for.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Generalizability  
- **Claim pointer** "This work establishes a generalizable, property-driven framework for the rational design of ATPS bioseparations and rapid adaptation to emerging pathogens"  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The framework is tested on a single protein family (SARS-CoV-2 spike variants) in a limited set of ATPS formulations. The abstract does not report validation on unrelated proteins or alternative phase-forming polymers. The claim of generalizability is therefore not supported by the visible evidence.  
- **Why it matters** The stated significance of the work rests on its applicability beyond the tested system. Without demonstration on diverse biomolecules, the framework may be overfitted to spike protein properties.  
- **Resolution test** Apply the framework to at least two unrelated proteins or protein families with distinct biophysical properties, and show that the predictive correlations hold. Report the range of hydrophobicity and isoelectric point values over which the model is valid.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Quantitative model validation  
- **Claim pointer** "A Collander-type inter-system correlation was established to test transferability across ATPS formulations"  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The Collander-type correlation is mentioned but no quantitative results are given. It is unclear whether the correlation is statistically significant, how many formulations were compared, and whether the correlation holds across the full range of partition coefficients or only a subset.  
- **Why it matters** The transferability claim is a key practical advantage. Without quantitative evidence, readers cannot assess whether a single reference measurement is sufficient for prediction in a new formulation.  
- **Resolution test** Provide the Collander plot with fitted slope, intercept, R-squared, and confidence intervals. State the number of formulations and the range of partition coefficients tested. Show that prediction error from a single reference measurement is acceptable for practical purposes.

- **Concern ID** R1-M5  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Reproducibility and methodology detail  
- **Claim pointer** "process-intensified LLPS in an evaporating sessile droplets" and "microfluidic picoliter-droplet partitioning assays"  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The abstract describes novel experimental techniques but provides no details on reproducibility, such as droplet size distributions, evaporation rates, measurement precision, or the number of replicates. The microfluidic assay is mentioned without information on throughput, error, or comparison to bulk measurements.  
- **Why it matters** The reliability of partition coefficient measurements underpins all subsequent correlations and predictions. If the assays have high variability or systematic biases, the model outputs will be unreliable.  
- **Resolution test** Include a methods section with detailed protocols, calibration procedures, and replicate statistics. Show that partition coefficients measured by the microfluidic assay agree with bulk measurements within acceptable error.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Terminology  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The term "process-intensified LLPS" is not standard and is not defined in the abstract.  
- **Required correction** Define the term or replace it with a more conventional description, such as "evaporation-driven concentration of the ATPS in sessile droplets."

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Variant description  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The abstract lists "wild type, Beta, Omicron, and the Omicron receptor-binding domain" as variants, but the Omicron RBD is a subdomain, not a full spike variant. This inconsistency may confuse readers.  
- **Required correction** Clarify whether the RBD is a standalone construct or a domain within the full spike, and describe its relationship to the other variants.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Quantitative reporting  
- **Affected element** Sensitivity enhancement  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The 11.7-fold sensitivity enhancement is reported without context, such as the baseline detection limit, the concentration factor achieved, or the assay's dynamic range.  
- **Required correction** Provide the detection limit before and after the ATPS pre-concentration step, and state the concentration factor and the assay's linear range.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Computational methods  
- **Evidence pointer** Abstract, location not provided  
- **Issue** AlphaFold3-based structural analysis is mentioned, but no details are given on the specific structures used, confidence scores, or how structural features were translated into quantitative descriptors.  
- **Required correction** Specify the AlphaFold3 model versions, the pLDDT scores for the regions used, and the exact structural descriptors (e.g., surface hydrophobicity patches) that entered the regression.

## Risk / unsupported claims
- The claim that hydrophobic interactions are the dominant partitioning mechanism is unsupported without controlled variation of system properties.
- The claim of generalizability to other biomolecules and pathogens is unsupported, as only SARS-CoV-2 spike variants were tested.
- The predictive power of the regression model is unverifiable without correlation coefficients, sample sizes, and validation statistics.
- The Collander-type correlation is mentioned but not quantitatively demonstrated.
- The 11.7-fold sensitivity enhancement is reported without baseline or methodological context.
- The reliability of the microfluidic and evaporating droplet assays cannot be assessed without replicate data and comparison to standard methods.