## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Conceptual framework, methodological claims, and reported results as described in the abstract
- **Shared manuscript claim summary** The authors propose "binding paths" as a conceptual and computational framework to describe small-molecule interactions with disordered proteins, formalized via a Markov state model (MSM), and demonstrate it on two systems (10074-G5 with Abeta42, fasudil with alpha-synuclein), reporting that the MSM enables dynamic mapping of transient binding sites and dissociation constants consistent with experiments.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary material provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, methodological details of the MSM construction, simulation or experimental protocols, quantitative results, and validation data

## Reviewer
- **Overall assessment** The abstract presents an interesting and potentially valuable conceptual advance for a difficult problem in drug discovery. The idea of replacing static binding pockets with dynamic "binding paths" for disordered proteins is timely and could have broad appeal. However, the abstract alone provides insufficient detail to assess the technical soundness of the MSM approach, the quality of the validation, or the robustness of the claimed consistency with experimental measurements. The core claims are plausible but not verifiable from the supplied material.
- **Who would be interested in the results, and why** Researchers in computational drug discovery, biophysics of intrinsically disordered proteins, and molecular simulation method development would be interested. The framework could also appeal to experimentalists studying ligand binding to disordered targets, as it offers a quantitative language for transient interactions that are otherwise difficult to characterize.
- **Major strengths** The conceptual framing is clear and addresses a genuine gap in the field. The choice of two biologically relevant systems (Alzheimer's and Parkinson's disease associated proteins) adds translational relevance. The claim of consistency with experimental dissociation constants, if substantiated, would be a strong validation point.
- **Major Concerns** The abstract does not provide enough information to evaluate the MSM construction, the definition of states, the timescale assumptions, or the statistical quality of the transition probability estimates. The claim of consistency with experimental measurements is stated without quantitative detail or error analysis. The generalizability of the approach beyond the two test cases is asserted but not supported.
- **Minor Comments** The abstract would benefit from a brief statement of how the binding paths differ from existing approaches such as docking onto ensembles or coarse-grained models. The phrase "time scales comparable to the overall residence time" is vague and should be quantified. The term "druggable regions" is used without a clear operational definition in this context.
- **Technical failings that need to be addressed before the case is established** R1-M1 (MSM construction and validation), R1-M2 (experimental consistency claim), R1-M3 (generalizability claim)
- **Assessment against Nature-style criteria** Originality: high, the concept of binding paths appears novel. Scientific importance: potentially high, as it addresses a recognized challenge. Interdisciplinary readership: moderate to high, bridging simulation, biophysics, and medicinal chemistry. Technical soundness: not assessable from the abstract alone. Readability for nonspecialists: good, the abstract is clearly written and accessible.
- **Recommendation posture** Supportive if technical concerns are resolved; currently not established from the provided evidence.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "We formalize this approach using a Markov state model (MSM), in which each state corresponds to a set of residues simultaneously contacting the ligand and the transition probabilities capture how the ligand moves between these sets."
- **Evidence pointer** Methods section not provided
- **Concern** The abstract does not describe how the MSM states are defined, how the transition probabilities are estimated, what simulation or experimental data feed the model, or how the Markov assumption is validated. Without this information, the reliability of the model cannot be assessed.
- **Why it matters** The entire framework rests on the validity of the MSM. If the state definition is arbitrary or the transition probabilities are poorly sampled, the resulting binding paths and derived quantities would be unreliable.
- **Resolution test** Provide details on state definition, data source, estimation procedure, and validation of Markovianity, including error bars or convergence tests.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** "The MSM enables both a dynamic mapping of transient binding sites and a calculation of dissociation constants consistent with experimental measurements."
- **Evidence pointer** Results section not provided
- **Concern** The abstract states consistency with experimental dissociation constants but provides no numbers, no comparison method, and no uncertainty quantification. It is unclear how many experimental values were compared, how close the agreement was, and whether the agreement is statistically meaningful.
- **Why it matters** This is the primary quantitative validation of the framework. Without explicit comparison data, the claim of consistency is unverifiable and could be coincidental or cherry-picked.
- **Resolution test** Report computed and experimental dissociation constants for both systems, with uncertainties, and describe the statistical test or metric used to establish consistency.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** "By generalizing the concept of static binding pockets to dynamic binding paths, this approach provides a quantitative framework for characterizing small-molecule binding by disordered proteins and for identifying druggable regions on these challenging targets."
- **Evidence pointer** Discussion section not provided
- **Concern** The abstract implies broad applicability of the framework, but only two systems are mentioned. It is unclear whether the approach would work for disordered proteins with different sequence properties, ligand sizes, or interaction timescales.
- **Why it matters** The stated significance of the work depends on its generalizability. If the framework only works for the two test cases, its impact is limited.
- **Resolution test** Discuss the range of applicability, potential limitations, and ideally show at least one additional test case with different characteristics.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Definition of binding path
- **Evidence pointer** Abstract, first paragraph
- **Issue** The phrase "time scales comparable to the overall residence time" is vague and could be interpreted in multiple ways.
- **Required correction** Specify the quantitative relationship between cluster lifetime and residence time, or provide a range of values observed in the simulations.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Context
- **Affected element** Positioning relative to existing methods
- **Evidence pointer** Abstract, overall
- **Issue** The abstract does not explain how binding paths differ from or improve upon existing approaches such as ensemble docking or Markov models of conformational states.
- **Required correction** Add one or two sentences contrasting the proposed framework with prior methods.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Druggable regions"
- **Evidence pointer** Abstract, last sentence
- **Issue** The term "druggable regions" is used without a clear operational definition in the context of dynamic binding paths.
- **Required correction** Define what constitutes a druggable region in this framework, e.g., residues that are frequently engaged across multiple binding paths.

## Risk / unsupported claims
- The claim of consistency with experimental dissociation constants is unsupported without quantitative data.
- The claim of generalizability to "disordered proteins" broadly is unsupported by the two test cases alone.
- The assertion that binding paths provide a "quantitative framework for identifying druggable regions" is not substantiated without a definition and validation of the identification procedure.
- The Markovian assumption and the timescale separation between cluster dynamics and residence time are not verifiable from the abstract.