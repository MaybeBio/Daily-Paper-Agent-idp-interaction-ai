## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the supplied abstract
- **Shared manuscript claim summary** The authors present metapredict V3, an updated disorder prediction tool, claiming state-of-the-art accuracy, proteome-scale throughput in seconds, and broad usability via multiple distribution channels. They further claim to have applied this tool to predict disorder across over 20,000 proteomes to evaluate disorder prevalence across kingdoms of life.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary materials provided
- **Missing materials affecting confidence** Full manuscript, methods description, benchmark datasets, validation results, comparison with existing predictors, proteome dataset details, and any statistical analyses

## Reviewer
- **Overall assessment** The abstract presents a potentially valuable tool for the intrinsically disordered protein research community, addressing a real need for accurate and high-throughput disorder prediction at evolutionary scale. However, the supplied material is insufficient to evaluate the technical validity of the claims. No quantitative accuracy metrics, benchmark comparisons, or methodological details are provided. The proteome-scale analysis is mentioned but not substantiated with any results or validation. The case for state-of-the-art accuracy and the biological findings from the 20,000 proteome analysis cannot be assessed from the abstract alone.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins and regions, particularly those working on comparative genomics, evolutionary biology, and proteome-scale analyses. The tool's claimed usability features would also interest bioinformaticians and computational biologists seeking accessible prediction tools. The proteome-wide disorder prevalence data would be relevant to anyone studying the functional and evolutionary significance of disorder across the Tree of Life.
- **Major strengths** The tool addresses a clearly identified gap in the field, namely the trade-off between accuracy and throughput for evolutionary-scale analyses. The emphasis on usability through multiple distribution channels is commendable and likely to increase adoption. The application to over 20,000 proteomes represents an ambitious and potentially impactful contribution.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: The concept of an updated predictor with evolutionary-scale application is incremental rather than conceptually novel, though the scale of application may be novel. Scientific importance: Potentially high if the accuracy and throughput claims hold, and if the proteome-scale results reveal new biological insights. Interdisciplinary readership: The tool and findings would interest structural biologists, evolutionary biologists, and bioinformaticians. Technical soundness: Cannot be evaluated from the abstract; no methodological or validation details are provided. Readability for nonspecialists: The abstract is clear and accessible, though technical terms are used without definition.
- **Recommendation posture** Currently not established from the provided evidence. The abstract alone does not provide sufficient information to assess the validity of the accuracy, throughput, or biological findings claims. A full manuscript with methods, benchmarks, and results would be required for a substantive evaluation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Metapredict V3 enables proteome-scale prediction with state-of-the-art accuracy in seconds"
- **Evidence pointer** Abstract, location not provided
- **Concern** The claim of state-of-the-art accuracy is presented without any quantitative metrics, benchmark datasets, or comparison to existing disorder prediction methods. No details are given on how accuracy was measured, which datasets were used, or which predictors were compared.
- **Why it matters** State-of-the-art accuracy is a central claim that distinguishes this tool from existing alternatives. Without supporting evidence, readers cannot verify whether the tool actually improves upon current methods, which is essential for establishing its value to the community.
- **Resolution test** Provide benchmark results on standard disorder prediction datasets, including metrics such as AUC, Matthews correlation coefficient, or per-residue accuracy, with explicit comparison to at least several existing predictors. Specify the training and test datasets and any cross-validation procedures.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility and methodology
- **Claim pointer** "we developed metapredict V3, an updated version of our disorder predictor"
- **Evidence pointer** Abstract, location not provided
- **Concern** No methodological details are provided about the architecture, training data, feature representation, or changes from previous versions of metapredict. The abstract does not describe how the model was built, what data it was trained on, or how it differs from metapredict V2.
- **Why it matters** For a computational tool, methodological transparency is essential for reproducibility and for users to understand the tool's limitations and appropriate use cases. Without this information, the tool cannot be independently evaluated or trusted for downstream applications.
- **Resolution test** Provide a detailed methods section describing the model architecture, training data, feature engineering, hyperparameter selection, and validation strategy. Clearly state the differences from previous metapredict versions and justify design choices.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence for biological findings
- **Claim pointer** "we leverage the accuracy and throughput of metapredict V3 to predict disorder for over 20,000 proteomes to evaluate the prevalence of disorder across the kingdoms of life"
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract states that disorder was predicted for over 20,000 proteomes but provides no results, trends, or biological conclusions from this analysis. No information is given about which proteomes were included, how they were selected, or what the analysis revealed about disorder prevalence across kingdoms.
- **Why it matters** The proteome-scale analysis is presented as a major outcome of the work, but without any results, the biological significance cannot be assessed. The claim of evaluating disorder prevalence across kingdoms of life requires presentation of the actual findings to be meaningful.
- **Resolution test** Present the results of the proteome-scale analysis, including the number and taxonomic distribution of proteomes analyzed, summary statistics of disorder prevalence by kingdom, and any notable patterns or comparisons with previous studies.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and completeness
- **Affected element** Tool distribution description
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract lists four distribution channels (web server, Python package, command-line interface, Google Colab notebook) but does not provide URLs, package names, or installation information.
- **Required correction** Provide specific access information, such as a website URL, package repository, or DOI for the software, to enable readers to actually use the tool.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "state-of-the-art accuracy"
- **Evidence pointer** Abstract, location not provided
- **Issue** The term "state-of-the-art" is used without qualification. It is unclear whether this refers to accuracy on specific benchmarks, speed, or a combination of factors.
- **Required correction** Define what is meant by state-of-the-art in this context and provide the specific benchmarks or criteria used to establish this claim.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scope of claims
- **Affected element** "evolutionary-scale disorder prediction"
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract claims evolutionary-scale prediction capability but does not define what constitutes evolutionary scale or how the tool's performance at this scale was validated.
- **Required correction** Clarify the definition of evolutionary scale in this context and describe any validation performed to demonstrate reliable performance at this scale.

## Risk / unsupported claims
- State-of-the-art accuracy claim is unsupported by any quantitative evidence in the supplied material.
- Proteome-scale prediction in seconds is stated without runtime benchmarks or hardware specifications.
- The biological findings from the 20,000 proteome analysis are entirely unsubstantiated as no results are presented.
- The claim of usability across multiple platforms is plausible but cannot be verified without access information or user documentation.
- The improvement over previous metapredict versions is asserted but not documented.