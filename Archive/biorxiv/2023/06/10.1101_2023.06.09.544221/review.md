## Review setup
- **Input scope** Full manuscript text (Abstract, Introduction, Results, Discussion, Methods, Data/Code availability, Author contributions, Competing interests, Acknowledgements, Bibliography)
- **Assessment boundary** Scientific and technical assessment of the manuscript as provided, without access to figures, supplementary materials, or source data
- **Shared manuscript claim summary** The authors present a comprehensive framework combining fluorescence lifetime imaging and fluctuation spectroscopy using a single-photon array detector, and apply it to study stress granule formation in living cells, reporting changes in molecular mobility, confinement, interactions, and fluorescence lifetime of G3BP1 and FUS proteins.
- **Visible evidence base** Abstract, Introduction, Results (three subsections), Discussion, Methods, Data/Code availability statements
- **Missing materials affecting confidence** All figures and figure legends, all supplementary materials (including Supplementary Information 1 referenced in Methods), source data, analysis code, and experimental raw data

## Reviewer
- **Overall assessment** The manuscript presents a technically ambitious and potentially valuable integration of fluorescence lifetime and fluctuation spectroscopy methods on a single-photon array detector platform. The conceptual framework is sound and the application to stress granule formation is biologically relevant. However, the provided text alone does not contain sufficient quantitative evidence to fully evaluate the technical claims or the biological conclusions. The Results section is descriptive and lacks the quantitative detail necessary to assess the robustness of the reported effects. The manuscript would benefit from clearer presentation of statistical analyses, control experiments, and the specific numerical outcomes that support the central claims.
- **Who would be interested in the results, and why** Researchers in quantitative fluorescence microscopy, biophysics of phase separation, and cell biology of stress granules would find this work of interest. The methodological integration addresses a genuine need for multi-parameter measurements of biomolecular dynamics in living cells. The application to FUS mutations linked to ALS also has relevance for the neurodegeneration community.
- **Major strengths** The conceptual integration of fluorescence lifetime and fluctuation spectroscopy in a single platform is novel and well motivated. The use of a SPAD array detector with time-tagging capabilities is technically sophisticated and represents a genuine advance in instrumentation. The application to a biologically important problem, stress granule formation in the context of ALS-linked mutations, gives the work clear significance beyond methodology alone. The authors also demonstrate attention to open-source hardware and software dissemination, which is commendable.
- **Major Concerns** The Results section is largely qualitative and descriptive. Key quantitative outcomes, such as the actual diffusion coefficient values, confinement strength distributions, and statistical comparisons between conditions, are not presented in sufficient detail in the text. The validation of the FLFS approach on test samples is described but the specific results are not shown. The biological conclusions, particularly regarding FUS-G3BP1 interactions, rely on correlation amplitudes that are mentioned but not quantitatively documented. The manuscript also lacks explicit discussion of potential artifacts or alternative interpretations of the fluorescence lifetime changes.
- **Minor Comments** The abstract is dense and could be more accessible to a broad readership. The Introduction provides good context but could be more concise. The Discussion is somewhat speculative in places, particularly regarding future applications. The Methods section is detailed but the referencing to supplementary information for fitting functions is not self-contained.
- **Technical failings that need to be addressed before the case is established** The absence of quantitative results in the text, the lack of statistical details, and the unavailability of figures and supplementary data in the provided material prevent full verification of the technical and biological claims.
- **Assessment against Nature-style criteria** Originality: The integration of FLFS with SPAD array detectors and its application to condensate biology is original and goes beyond incremental methodological development. Scientific importance: The work addresses a real need for multi-parameter, multi-scale measurements of biomolecular dynamics in living cells, and the application to stress granules and ALS-linked mutations gives it broad relevance. Interdisciplinary readership: The work bridges microscopy, biophysics, and cell biology, and should appeal to researchers across these fields. Technical soundness: The instrumentation and conceptual approach are sound, but the provided text does not contain enough quantitative evidence to fully assess the robustness of the results. Readability for nonspecialists: The abstract and introduction are reasonably accessible, but the Results section assumes significant familiarity with the methods and would benefit from clearer explanation of the key concepts and findings.
- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual framework and instrumentation are promising, and the biological application is relevant, but the current evidence base is insufficient to fully establish the claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors claim that the proposed approach reveals the mutual dynamics of different RNA-binding proteins involved in stress granule formation, inaccessible to imaging alone.
- **Evidence pointer** Results section, subsection "Dual-color FCCS reveals proteins interaction"; location not provided
- **Concern** The claim that the approach reveals mutual dynamics of RNA-binding proteins is supported only by a qualitative description of cross-correlation amplitudes. The actual cross-correlation curves, their fitted parameters, and the statistical significance of the differences between conditions are not presented in the text.
- **Why it matters** The central biological conclusion of the manuscript, that FUS and G3BP1 interact within stress granules, depends on the quantitative demonstration of increased cross-correlation amplitude. Without these data, the claim is not verifiable.
- **Resolution test** Provide the cross-correlation curves, fitted amplitudes with uncertainties, and statistical comparisons between pre-stress, stress, and recovery conditions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors claim that fluorescence lifetime decreases in correlation with the diffusion coefficient for G3BP1, indicating a rearrangement of dye molecules during stress granule formation.
- **Evidence pointer** Results section, subsection "Fluorescence lifetime reveals protein confinement"; location not provided
- **Concern** The correlation between fluorescence lifetime and diffusion coefficient is stated but not quantitatively demonstrated. No correlation coefficients, scatter plots, or statistical tests are provided in the text.
- **Why it matters** The claim of a link between nanoscale environment (lifetime) and mesoscale dynamics (diffusion) is a key novel contribution. Without quantitative evidence, the relationship remains suggestive rather than established.
- **Resolution test** Provide a scatter plot or correlation analysis of lifetime versus diffusion coefficient with appropriate statistical measures.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The authors state that the k-mean clustering algorithm classifies data points into two groups corresponding to pre-stress and post-stress conditions.
- **Evidence pointer** Results section, subsection "Spot-variation FCS reveals protein condensation in living cells"; location not provided
- **Concern** The clustering analysis is described but the actual clustering results, including the number of data points, cluster centroids, and the confidence ellipses shown in the figures, are not presented in the text. The choice of k and the robustness of the clustering are not discussed.
- **Why it matters** The clustering analysis is used to support the distinction between pre-stress and post-stress conditions. Without the underlying data and analysis details, the validity of this distinction cannot be assessed.
- **Resolution test** Provide the clustering results, including the data points, cluster assignments, and the method for determining the number of clusters.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical validation
- **Claim pointer** The authors claim that the FLFS approach is validated on test samples, including fluorescent beads and in-vitro alpha-synuclein phase separation.
- **Evidence pointer** Results section, subsection "Validation of Fluorescence Lifetime Fluctuation Spectroscopy"; location not provided
- **Concern** The validation experiments are described but the results are not presented in the text. The diffusion coefficient for beads is stated, but the comparison to expected values and the uncertainty are not given. The alpha-synuclein results are described only qualitatively.
- **Why it matters** The validation of the method on well-characterized systems is essential to establish its reliability before application to cellular systems. Without quantitative validation data, the credibility of the cellular results is undermined.
- **Resolution test** Provide the validation data, including fitted parameters, uncertainties, and comparisons to literature values.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors report significant differences in diffusion coefficients and confinement strengths between conditions (e.g., pre-stress vs. stress, WT vs. mutant).
- **Evidence pointer** Results section, subsections "Spot-variation FCS reveals protein condensation in living cells" and "Fluorescence lifetime reveals protein confinement"; location not provided
- **Concern** The text reports mean values with standard deviations but does not provide the number of biological replicates, the number of measurements per condition, or the statistical tests used to establish significance. The p-value for the lifetime comparison is given but the test and sample size are not specified.
- **Why it matters** The biological conclusions depend on the statistical robustness of the reported differences. Without proper statistical reporting, the significance of the findings cannot be evaluated.
- **Resolution test** Provide sample sizes, statistical tests, and effect sizes for all reported comparisons.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract is dense and uses technical jargon without sufficient context for a general scientific audience.
- **Required correction** Simplify the abstract and define key terms such as "content-enriched" and "fluorescence lifetime fluctuation spectroscopy" more clearly.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods, fluorescence correlation calculation
- **Evidence pointer** Methods section, "Fluorescence correlation calculation and analysis"; location not provided
- **Issue** The Methods section refers to "Supplementary Information 1" for the theoretical fitting functions, but this material is not provided in the manuscript text.
- **Required correction** Include the fitting functions in the main text or ensure the supplementary information is accessible to reviewers.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion; location not provided
- **Issue** The Discussion speculates about future applications without clearly distinguishing between what has been demonstrated and what is speculative.
- **Required correction** Clearly separate demonstrated results from potential future directions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Data availability
- **Evidence pointer** Data availability statement; location not provided
- **Issue** The data availability statement indicates that not all data are currently available and some must be requested from the corresponding author.
- **Required correction** Provide a clear timeline for when all data will be made publicly available, or deposit all data in a public repository.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Methods, image reconstruction
- **Evidence pointer** Methods section, "Image reconstruction and analysis"; location not provided
- **Issue** The description of the phasor analysis and the segmentation based on phasor plots is brief and lacks details on the specific implementation.
- **Required correction** Provide more detail on the phasor analysis implementation and the segmentation algorithm.

## Risk / unsupported claims
- The claim that the approach reveals mutual dynamics of different RNA-binding proteins is not quantitatively supported in the provided text.
- The claim of a correlation between fluorescence lifetime and diffusion coefficient is stated but not demonstrated with data.
- The claim that the clustering analysis distinguishes pre-stress and post-stress conditions is not supported by presented data.
- The validation of the FLFS approach on test samples is described but not quantitatively documented.
- The statistical significance of reported differences between conditions is not established with proper statistical reporting.
- The biological interpretation of fluorescence lifetime changes as indicating "rearrangement of dye molecules" is speculative without additional control experiments.