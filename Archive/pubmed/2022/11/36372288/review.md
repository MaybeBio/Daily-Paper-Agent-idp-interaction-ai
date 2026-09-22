## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors use molecular dynamics simulations to assess how acetylation and phosphorylation of Tau protein alter its conformation, electrostatics, and binding to microtubules, concluding that these post-translational modifications generally impair microtubule association and may inform Alzheimer's disease therapeutics.
- **Visible evidence base** Abstract text only; no methodological details, simulation parameters, quantitative results, or statistical analyses provided
- **Missing materials affecting confidence** Full methods, simulation trajectories, force field parameters, system setup, validation metrics, quantitative binding free energies, conformational analyses, and any comparison with experimental data

## Reviewer
- **Overall assessment** The abstract presents a plausible computational study addressing a relevant question in Tau biology, namely how acetylation and phosphorylation modulate microtubule binding. The design of multiple Tau variants and the use of molecular dynamics are appropriate in principle. However, the abstract lacks quantitative results, methodological transparency, and validation against experimental observations. The central claims are stated qualitatively and cannot be rigorously evaluated from the supplied material. The potential therapeutic relevance is asserted without supporting evidence.
- **Who would be interested in the results, and why** Researchers in neurodegenerative disease biology, particularly those studying Tau post-translational modifications and microtubule dynamics. Computational biophysicists interested in protein modification effects on binding. Drug discovery groups targeting Tau aggregation or microtubule stabilization in Alzheimer's disease may find the mechanistic insights useful, provided the findings are validated experimentally.
- **Major strengths** The study addresses a biologically important question with clear clinical relevance. The systematic design of eight acetylated and multiple phosphorylated Tau variants is a reasonable approach to explore modification effects. The focus on both electrostatic changes and conformational impacts on the microtubule-binding region is mechanistically sensible.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that electrostatic changes due to acetylation or phosphorylation "hamper the association to the MT tubulins in most cases."
  - **Evidence pointer** Abstract; location not provided
  - **Concern** The abstract provides no quantitative data, such as binding free energies, contact frequencies, or residence times, to support the claim that binding is hampered. The phrase "in most cases" implies variability across variants, but no specific outcomes are reported.
  - **Why it matters** Without quantitative metrics, the reader cannot assess the magnitude of the effect, the statistical significance, or whether the observed differences are biologically meaningful. The claim is currently an assertion rather than a demonstrated result.
  - **Resolution test** Provide binding free energy values or interaction energy distributions for each variant compared to native Tau, with error estimates and statistical testing.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors state that post-translational modifications "pose very distinct conformations to the ones described for native Tau, which hinders the microtubule-binding region (MTBR)."
  - **Evidence pointer** Abstract; location not provided
  - **Concern** No conformational metrics are reported, such as root-mean-square deviation, radius of gyration, secondary structure content, or solvent-accessible surface area of the MTBR. The claim that the MTBR is "hindered" is vague and unsupported.
  - **Why it matters** Conformational changes are central to the proposed mechanism. Without quantitative descriptors, the reader cannot determine whether the observed changes are significant, transient, or an artifact of simulation length or force field choice.
  - **Resolution test** Report conformational ensembles for each variant, including MTBR accessibility metrics and comparison to native Tau, with appropriate sampling statistics.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Reproducibility
  - **Claim pointer** The study uses "molecular modelling techniques" and evaluates variants "in intracellular fluid and near a microtubule (MT) model."
  - **Evidence pointer** Abstract; location not provided
  - **Concern** No methodological details are given, including force field, water model, ion concentration, simulation time, number of replicas, system size, or how the MT model was constructed. The term "intracellular fluid" is not defined in terms of ionic composition.
  - **Why it matters** Molecular dynamics results are highly sensitive to these parameters. Without this information, the study cannot be reproduced or critically evaluated, and the reliability of the conclusions is unknown.
  - **Resolution test** Provide a complete methods section with all simulation parameters, system construction details, and validation of the MT model.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The authors state that the study "can inspire novel therapeutics to address Alzheimer's disease."
  - **Evidence pointer** Abstract; location not provided
  - **Concern** The therapeutic relevance is asserted without any link to druggable targets, existing experimental data, or a proposed intervention strategy. The abstract does not explain how these computational findings translate to therapeutic development.
  - **Why it matters** Overstating translational relevance without evidence weakens the scientific impact and may mislead readers about the study's applicability.
  - **Resolution test** Either remove the therapeutic claim or provide a specific, evidence-based connection to experimental or clinical observations.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Abstract wording
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The phrase "Reported harmful Lys sites" is ambiguous. It is unclear whether "harmful" refers to disease-associated acetylation sites or sites known to impair function experimentally.
  - **Required correction** Specify the source or criterion for selecting these Lys sites, such as "previously identified in disease-associated Tau aggregates."
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Variant description
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The abstract mentions "phosphorylation sites found in normal brains and in Alzheimer's lesioned brains" but does not state how many pTau analogues were designed or which sites were included.
  - **Required correction** List the number of pTau variants and the specific phosphorylation sites modeled.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interpretation
  - **Affected element** Statement on binding impairment
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The claim that modifications "hamper the association" is presented as a general finding, but the phrase "in most cases" suggests exceptions. The abstract does not discuss which variants retained binding or why.
  - **Required correction** Briefly describe the range of outcomes across variants and any patterns that explain differential effects.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3. The absence of quantitative binding data, conformational metrics, and methodological details prevents verification of the central claims. R1-M4 is a secondary issue related to overinterpretation.
- **Assessment against Nature-style criteria**  
  Originality: Moderate. The application of molecular dynamics to Tau acetylation and phosphorylation is not entirely novel, but the systematic comparison of multiple modification types in a single framework has some originality.  
  Scientific importance: Potentially high if the findings are robust and validated, given the relevance to Alzheimer's disease. However, the current abstract does not establish this importance with evidence.  
  Interdisciplinary readership: The topic bridges computational biophysics and neurobiology, which could attract a broad audience. The abstract is written accessibly but lacks technical depth.  
  Technical soundness: Not assessable from the abstract. Critical parameters and quantitative results are missing.  
  Readability for nonspecialists: The abstract is generally clear, but terms like "MTBR" and "MT tubulins" are used without definition, which may hinder nonspecialist comprehension.
- **Recommendation posture** Currently not established from the provided evidence. The study addresses a relevant question, but the abstract alone does not provide sufficient quantitative or methodological support for the central claims. A revised manuscript with full methods, quantitative results, and validation would be needed to assess whether the case is convincing.

## Risk / unsupported claims
- The claim that electrostatic changes "hamper the association to the MT tubulins in most cases" is unsupported without quantitative binding data.
- The claim that post-translational modifications "hinder the microtubule-binding region" is unsupported without conformational metrics.
- The statement that the study "can inspire novel therapeutics" is an unsupported extrapolation from computational findings.
- The generalizability of the findings to physiological conditions is not assessable given the lack of methodological detail and experimental validation.