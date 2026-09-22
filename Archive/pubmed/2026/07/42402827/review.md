## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no methods, figures, tables, or supplementary material were available for evaluation
- **Shared manuscript claim summary** The authors used molecular dynamics simulations and bioinformatic analysis to show that the LXCXE motif of the SV40 Large T antigen binds pRb with low intrinsic affinity, that flanking residues enhance binding asymmetrically, that full-length protein binds more strongly than peptide fragments, that N-terminal flanking residues drive initial recognition via an alpha-helical conformation while C-terminal residues engage later, and that an ordered-motif-disordered-architecture is conserved across polyomavirus Large T antigens as a general strategy for pRb targeting.
- **Visible evidence base** Abstract text only; no structural models, simulation parameters, convergence metrics, energetic data, or bioinformatic alignments were provided
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, simulation details (force field, sampling time, replica setup), energetic analysis (MM-PBSA/GBSA or similar), bioinformatic alignment details, and statistical analyses

## Reviewer
- **Overall assessment** The abstract presents a plausible and potentially interesting mechanistic model for LXCXE-mediated pRb recognition by SV40 Large T antigen, with a claim of evolutionary conservation across polyomaviruses. However, the evidence base provided is insufficient to evaluate the technical soundness of the simulations, the robustness of the energetic comparisons, or the statistical support for the proposed two-stage binding mechanism. The conservation claim is particularly difficult to assess without alignment details or sequence analysis methodology. The work addresses a question of moderate interest to the biophysics and virology communities, but the current abstract alone does not establish the case.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins and their role in protein-protein interactions, computational biophysicists interested in molecular recognition mechanisms, and virologists studying how viral oncoproteins inactivate tumor suppressors. The proposed ordered-disordered architecture as a conserved strategy for pRb targeting could be of interest to those working on polyomavirus biology and therapeutic targeting of LXCXE-mediated interactions.
- **Major strengths** The abstract clearly articulates a mechanistic hypothesis with a defined temporal ordering of binding events. The claim of evolutionary conservation adds a broader significance beyond a single protein system. The work connects local structural propensity, intrinsic disorder, and sequence context, which is a timely and relevant framework in the field.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: the concept of an ordered motif embedded in a disordered region driving sequential binding is not entirely new, but the specific application to LTSV40 and the conservation claim add some novelty. Scientific importance: moderate; the work addresses a specific viral-host interaction that is well studied, and the mechanistic insight, if validated, would be useful but not transformative. Interdisciplinary readership: the abstract is written in a way that is accessible to biophysicists and biochemists, but the significance for a broader readership is not clearly articulated. Technical soundness: cannot be assessed from the abstract alone; no simulation details, convergence criteria, or error estimates are provided. Readability for nonspecialists: the abstract is clear and well structured, though terms such as "ordered-motif-disordered architecture" would benefit from a brief definition.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the isolated LXCXE motif has low affinity for pRb, that flanking residues enhance binding asymmetrically, and that the full-length protein binds more strongly than peptide fragments.
- **Evidence pointer** Abstract only; no energetic data, binding free energy calculations, or experimental validation are provided
- **Concern** The abstract reports relative binding affinities among different constructs without presenting any quantitative energetic data, error estimates, or statistical significance. It is unclear whether these comparisons are based on end-point free energy methods, enhanced sampling, or other approaches, and whether the differences are robust to simulation length and force field choice.
- **Why it matters** The central claim of the paper rests on the relative binding strengths of different LTSV40 constructs. Without quantitative data and uncertainty quantification, the reader cannot judge whether the reported ordering is meaningful or an artifact of the computational protocol.
- **Resolution test** Provide binding free energy values with standard errors for each construct, specify the method used, and demonstrate convergence of the estimates. If possible, include experimental binding data for at least one comparison to validate the computational trend.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that residues N-terminal to the LXCXE motif drive initial recognition by adopting an alpha-helical conformation, while C-terminal residues engage at later stages.
- **Evidence pointer** Abstract only; no time-resolved data, contact maps, or conformational analysis are provided
- **Concern** The proposed two-stage binding mechanism implies a temporal ordering of events. The abstract does not describe how this ordering was determined from the simulations, what observables were used to define "initial" versus "later" stages, or whether multiple independent simulations support the same sequence of events.
- **Why it matters** A sequential binding mechanism is a strong mechanistic claim that requires direct evidence of time-dependent behavior, not just static structural analysis. Without such evidence, the claim is speculative.
- **Resolution test** Show time-dependent contact formation or binding pathway analysis from multiple independent simulations, with clear definitions of the stages and statistical support for the ordering.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Support for evolutionary claim
- **Claim pointer** The authors claim that the ordered-motif-disordered architecture is conserved across polyomavirus Large T antigens, suggesting a general strategy for efficient pRb targeting.
- **Evidence pointer** Abstract only; no alignment data, sequence analysis methods, or conservation metrics are provided
- **Concern** The conservation claim is presented as a general strategy, but no details are given about the number of sequences analyzed, the alignment method, the definition of "conserved" in this context, or whether the structural prediction was validated for other family members.
- **Why it matters** This claim extends the significance of the work beyond the single system studied. If not rigorously supported, it overstates the generality of the findings.
- **Resolution test** Provide the sequence alignment, the conservation score for the ordered-disordered architecture, and demonstrate that the predicted structural feature is present in multiple diverse polyomavirus Large T antigens.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract, first paragraph
- **Issue** The term "ordered-motif-disordered architecture" is introduced without definition. It is unclear whether this refers to a structural feature, a sequence feature, or a dynamic property.
- **Required correction** Define the term explicitly when first used, and clarify whether it is a computational prediction or an experimentally observed property.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Model description
- **Evidence pointer** Abstract, second sentence
- **Issue** The abstract states that "computational models of pRb bound to different LTSV40 constructs" were generated, but does not specify how many constructs were studied, what their sequences were, or how the models were built.
- **Required correction** Briefly list the constructs studied and the modeling approach used, or refer to a methods section where these details are provided.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Mechanistic claim
- **Evidence pointer** Abstract, fourth sentence
- **Issue** The claim that N-terminal residues "drive initial recognition" could be interpreted as a kinetic statement, but the abstract does not clarify whether this is based on free energy barriers, contact formation rates, or another metric.
- **Required correction** Specify the observable used to define "initial recognition" and clarify whether the claim is kinetic or thermodynamic in nature.

## Risk / unsupported claims
- The relative binding affinities of the isolated LXCXE motif, flanking residue constructs, and full-length protein are reported without quantitative data or error estimates.
- The two-stage binding mechanism with N-terminal residues driving initial recognition and C-terminal residues engaging later is not supported by any time-resolved evidence in the abstract.
- The conservation of the ordered-motif-disordered architecture across polyomavirus Large T antigens is stated without any bioinformatic details or supporting data.
- The claim that the full-length protein binds more strongly than peptide fragments is presented as a general result, but no comparison to experimental data is provided.