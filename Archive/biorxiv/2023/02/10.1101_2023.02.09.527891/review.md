## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the provided abstract text
- **Shared manuscript claim summary** The authors benchmark nine molecular dynamics force fields for all-atom simulations of the FUS protein and its RNA-bound domains, using Anton 2 supercomputer simulations and dynamic light scattering data, and propose an optimal force field combination based on a common four-point water model, with a validated NAMD implementation for broader accessibility.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary materials provided
- **Missing materials affecting confidence** Full manuscript, simulation protocols, force field parameter details, experimental DLS methodology, statistical analyses, validation data for NAMD implementation, and all figures and tables

## Reviewer
- **Overall assessment** The abstract presents a timely and potentially valuable benchmarking study addressing a critical gap in simulating biological condensates with all-atom methods. The scope is ambitious, covering nine force fields, multiple simulation lengths, and both protein and RNA systems. However, the abstract alone provides insufficient detail to evaluate the rigor of the benchmarking methodology, the statistical significance of the findings, or the validity of the proposed force field combination. The claim that a common four-point water model provides optimal performance is intriguing but requires substantial supporting evidence not visible here. The NAMD implementation component adds practical value but its validation is not described in sufficient detail.
- **Who would be interested in the results, and why** Computational biophysicists and molecular dynamics method developers would be primary audiences, as the work directly addresses force field selection for disordered proteins and condensates. Experimental researchers studying phase separation, particularly those investigating FUS and related proteins in neurodegeneration, would benefit from guidance on simulation reliability. The NAMD implementation could interest a broader community of simulation practitioners seeking accessible tools for large condensate systems.
- **Major strengths** The study addresses a well-recognized gap in the field, namely the lack of validated force fields for systems combining disordered and structured regions. The use of Anton 2 for extended microsecond-scale simulations is appropriate for the questions posed. The benchmarking against experimental DLS data provides an external reference point. The inclusion of RNA-protein interactions extends the relevance beyond protein-only systems. The NAMD implementation addresses practical accessibility concerns.
- **Major Concerns** The abstract does not specify which nine force fields were tested, preventing assessment of whether the selection is comprehensive or biased. The criteria for identifying force fields producing conformations "within the experimental range" are not defined, leaving ambiguity about the stringency of this benchmark. The claim that a common four-point water model is optimal is presented without quantitative comparisons or statistical support. The stability assessment of RNA-FUS complexes is described only qualitatively. The NAMD validation is mentioned but not substantiated with performance metrics or accuracy comparisons.
- **Minor Comments** The abstract would benefit from stating the specific force field names and versions tested. The relationship between simulation timescale and convergence of conformational properties is not addressed. The choice of DLS as the sole experimental benchmark for radius of gyration warrants justification, as other methods may provide complementary or more direct measurements. The abstract does not mention how force field performance was ranked or whether any force fields were clearly inadequate.
- **Technical failings that need to be addressed before the case is established** The central claim regarding the optimal force field combination cannot be evaluated from the abstract alone. The absence of quantitative data, statistical analysis, and methodological details means the case is not currently established from the provided evidence.
- **Assessment against Nature-style criteria** Originality: The benchmarking approach is not entirely novel, but the specific focus on condensate-relevant systems and the combination of protein and RNA force fields adds a distinctive angle. Scientific importance: High, given the growing interest in condensate simulations and the practical need for validated force fields. Interdisciplinary readership: The work bridges computational chemistry, biophysics, and cell biology, though the abstract may be too technical for nonspecialists without additional context. Technical soundness: Cannot be assessed from the abstract; the lack of methodological detail precludes evaluation. Readability for nonspecialists: The abstract is reasonably clear but assumes familiarity with force field concepts and simulation terminology.

## Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "a combination of protein and RNA force fields sharing a common four-point water model provides an optimal description of proteins containing both disordered and structured regions and RNA-protein interactions."
- **Evidence pointer** Abstract text; location not provided
- **Concern** The abstract provides no quantitative data, comparative metrics, or statistical analyses to support the claim that the identified force field combination is "optimal." The basis for this conclusion, including how performance was ranked across the nine force fields and what thresholds defined "optimal," is entirely absent.
- **Why it matters** This is the central conclusion of the study. Without transparent criteria and supporting data, the claim cannot be independently verified or reproduced, undermining the scientific value of the benchmarking effort.
- **Resolution test** The full manuscript must present quantitative comparisons across all force fields, including error metrics relative to experimental data, statistical significance tests, and a clear definition of the optimization criteria.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency
- **Claim pointer** The authors state they "benchmarked the efficacy of nine presently available molecular force fields" and used "results of dynamic light scattering as a benchmark for the FUS radius of gyration."
- **Evidence pointer** Abstract text; location not provided
- **Concern** The abstract does not identify the nine force fields, the simulation conditions, the system preparation protocols, or the DLS experimental details. Without this information, the reader cannot assess whether the force field selection is representative, whether the simulations were conducted under comparable conditions, or whether the experimental benchmark is appropriate and reliable.
- **Why it matters** Benchmarking studies derive their value from methodological rigor and reproducibility. The absence of these details prevents evaluation of potential biases, such as force field parameter tuning or inconsistent simulation setups, and limits the utility of the findings for other researchers.
- **Resolution test** The full manuscript must list all force fields with versions, provide complete simulation protocols, and describe DLS experimental conditions, including sample preparation, temperature, and analysis methods.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation completeness
- **Claim pointer** The authors state "we describe and validate implementation of the best performing force fields in a publicly available molecular dynamics program NAMD."
- **Evidence pointer** Abstract text; location not provided
- **Concern** The abstract mentions validation of the NAMD implementation but provides no details on what was validated, how accuracy was assessed, or whether the implementation reproduces Anton 2 results. The claim of accessibility is meaningful only if the implementation is demonstrably equivalent in accuracy and performance.
- **Why it matters** The NAMD implementation is presented as a key deliverable for the broader community. If the validation is incomplete or the implementation introduces artifacts, the practical value of the study is significantly diminished.
- **Resolution test** The full manuscript must include validation data comparing NAMD simulations against Anton 2 results for the same systems, including structural and dynamic properties, and report computational performance metrics.

## Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Force field selection
- **Evidence pointer** Abstract text; location not provided
- **Issue** The abstract does not specify which nine force fields were tested, making it difficult to contextualize the findings within the existing literature.
- **Required correction** List the force field names and versions in the abstract or clearly reference a table in the full manuscript.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Experimental benchmark justification
- **Affected element** DLS benchmark
- **Evidence pointer** Abstract text; location not provided
- **Issue** The choice of DLS as the sole experimental benchmark for radius of gyration is not justified, and the abstract does not mention whether other experimental methods were considered.
- **Required correction** Provide a brief rationale for using DLS and acknowledge any limitations or complementary methods in the full manuscript.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology precision
- **Affected element** "Optimal" claim
- **Evidence pointer** Abstract text; location not provided
- **Issue** The term "optimal" is used without defining the performance metric or the acceptable tolerance relative to experimental data.
- **Required correction** Define the criteria for "optimal" performance, such as a specific error threshold or ranking method, in the abstract or methods.

## Risk / unsupported claims
- The claim that a combination of force fields sharing a common four-point water model is "optimal" is unsupported by the abstract evidence.
- The claim that the NAMD implementation is "validated" is unsubstantiated without validation details.
- The claim that certain force fields produced conformations "within the experimental range" is ambiguous without defined criteria.
- The claim that force field choice affects RNA-FUS complex stability is not supported by quantitative data in the abstract.
- The generalizability of the findings to other condensate-forming proteins is asserted but not demonstrated.