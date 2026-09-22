## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors present Ensemblify, an open-source Python package for generating and analyzing conformational ensembles of intrinsically disordered proteins and regions (IDPs/IDRs). The tool uses a Monte Carlo algorithm with neighbor-aware dihedral angle sampling from fragment libraries, optionally incorporates AlphaFold confidence metrics as restraints in PyRosetta, supports multi-domain and multi-chain proteins, and offers validation against experimental data via Bayesian/Maximum Entropy reweighting. Testing across ten proteins with benchmarking is claimed to demonstrate accuracy, flexibility, and recovery of experimental features.
- **Visible evidence base** Abstract text only; no methodological details, benchmark results, figures, or data are available for inspection
- **Missing materials affecting confidence** Full manuscript, all figures and tables, benchmark protocols, dataset descriptions, statistical analyses, and code documentation; without these, quantitative claims cannot be verified

## Reviewer
- **Overall assessment** The abstract describes a potentially useful software tool addressing a real need in the IDP community. The feature set is sensible and the open-source distribution model is commendable. However, the abstract makes several strong performance claims that cannot be evaluated without the underlying data and methods. The scientific case for novelty and demonstrated utility is currently not established from the provided material.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins and regions, particularly those needing accessible tools for ensemble generation and analysis. Structural biologists and computational biophysicists interested in integrative modeling with SAXS or other experimental restraints would also find the tool relevant. The Python API and CLI design may appeal to bioinformaticians seeking scriptable workflows.
- **Major strengths** The tool addresses a clear accessibility gap in IDP ensemble modeling. The combination of Monte Carlo sampling, optional AlphaFold-derived restraints, multi-domain support, and experimental validation via reweighting is a coherent and practical feature set. The open-source availability with documentation and tutorials is a significant strength for community adoption.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1 (benchmark evidence not visible), R1-M2 (AlphaFold integration claim not substantiated), R1-M3 (comparison to existing tools not specified)
- **Assessment against Nature-style criteria** Originality: the specific combination of features may be novel, but this cannot be confirmed without a comparison to existing tools. Scientific importance: the problem is relevant, but the significance of the contribution depends on demonstrated performance gains or unique capabilities. Interdisciplinary readership: the tool is likely to appeal to structural biologists and computational chemists, but the abstract does not clearly articulate broader impact. Technical soundness: the methods are described at a high level only; no evidence is visible to assess correctness or robustness. Readability for nonspecialists: the abstract is generally clear, though some terms (e.g., "neighbor-aware sampling", "Bayesian/Maximum Entropy reweighting") assume domain familiarity.
- **Recommendation posture** Currently not established from the provided evidence. The abstract describes a plausible tool, but the core performance claims require full manuscript review. I would be supportive if the technical concerns are resolved with adequate evidence.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "Testing across ten structurally diverse proteins coupled with state-of-the-art benchmarking demonstrated Ensemblify's accuracy, flexibility, and ability to recover experimentally observed structural features."
- **Evidence pointer** Location not provided
- **Concern** The abstract claims that testing across ten proteins demonstrated accuracy, flexibility, and recovery of experimental features, but no quantitative results, benchmark details, or comparison metrics are presented. The phrase "state-of-the-art benchmarking" is vague and does not specify which tools or datasets were used for comparison.
- **Why it matters** The central value proposition of the tool rests on its demonstrated performance. Without visible benchmark data, the reader cannot assess whether the tool is accurate, competitive, or fit for purpose. This is the core evidence needed to establish the scientific case.
- **Resolution test** Provide benchmark results in the full manuscript, including quantitative metrics (e.g., radius of gyration, ensemble agreement with experimental data), comparison against at least one established method, and details of the ten test proteins and the benchmarking protocol.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim substantiation
- **Claim pointer** "Optionally, it can incorporate information from AlphaFold's confidence metrics as flexible energy restraints in PyRosetta to guide sampling." and "Incorporating AlphaFold confidence metrics shows potential to improve the ensemble-data agreement."
- **Evidence pointer** Location not provided
- **Concern** The abstract states that AlphaFold confidence metrics can be used as restraints and that this "shows potential" to improve agreement with experimental data. However, no results are shown to support this claim. The word "potential" is appropriately cautious, but the claim is still unsubstantiated without any comparative analysis.
- **Why it matters** The AlphaFold integration is a distinctive feature that may differentiate Ensemblify from other tools. If this feature does not provide measurable benefit, its inclusion is not justified. Conversely, if it does improve performance, this should be demonstrated explicitly.
- **Resolution test** Provide a comparison of ensemble quality with and without AlphaFold-derived restraints for at least one test case, with quantitative metrics of experimental agreement.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Contextual positioning
- **Claim pointer** "Existing computational approaches for modeling these ensembles are often computationally expensive, inflexible, or inaccessible to non-experts."
- **Evidence pointer** Location not provided
- **Concern** The abstract critiques existing approaches but does not name any specific tools or methods. Without a clear comparison to the current state of the art, the reader cannot evaluate whether Ensemblify addresses a genuine gap or duplicates existing functionality.
- **Why it matters** The novelty and utility of the tool depend on its position relative to existing software. A vague critique without named comparators weakens the case for the tool's necessity and distinctiveness.
- **Resolution test** In the full manuscript, explicitly compare Ensemblify to at least two existing tools (e.g., EOM, Flexible-Meccano, or others) in terms of features, usability, and performance, with quantitative benchmarks where possible.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** "neighbor-aware sampling of dihedral angles"
- **Evidence pointer** Location not provided
- **Issue** The term "neighbor-aware" is not defined in the abstract. It is unclear whether this refers to sequence-neighbor effects, spatial neighbors, or something else.
- **Required correction** Provide a brief definition or clarification of "neighbor-aware" in the abstract or full text.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** "curated or user-defined fragment libraries"
- **Evidence pointer** Location not provided
- **Issue** The abstract does not specify the source or composition of the curated fragment libraries, nor how users can define their own. This affects reproducibility and ease of adoption.
- **Required correction** In the full text, describe the fragment library source, format, and the process for user-defined libraries.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scope clarity
- **Affected element** "multi-domain and multi-chain proteins"
- **Evidence pointer** Location not provided
- **Issue** The abstract claims support for multi-domain and multi-chain proteins but does not specify any limitations, such as maximum size or complexity, or how inter-chain interactions are handled.
- **Required correction** In the full text, state any known limitations and describe the treatment of inter-chain interactions in the sampling algorithm.

## Risk / unsupported claims
- The claim that Ensemblify demonstrated "accuracy, flexibility, and ability to recover experimentally observed structural features" across ten proteins is unsupported in the abstract, as no data are presented.
- The claim that AlphaFold confidence metrics "show potential to improve the ensemble-data agreement" is unsupported, as no comparative results are shown.
- The general critique of existing approaches as "computationally expensive, inflexible, or inaccessible" is unsubstantiated without named comparators or specific evidence.
- The claim that Ensemblify is "user-friendly" is subjective and not supported by usability studies or user feedback in the abstract.
- The statement that the tool "supports multi-domain and multi-chain proteins" is plausible but not demonstrated with examples or performance data in the abstract.