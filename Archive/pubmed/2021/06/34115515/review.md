## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors argue that SAXS-derived molecular form factors (MFFs) cannot uniquely distinguish homogeneous from heterogeneous conformational ensembles of disordered proteins. They support this via chain-model simulations and an analytical perturbation theory for flexible heteropolymers, showing that some heterogeneous ensembles with distinct end-to-end distance and radius of gyration properties can produce nearly identical MFFs to homogeneous ensembles.
- **Visible evidence base** Abstract text only; no numerical data, simulation details, or figures provided
- **Missing materials affecting confidence** Full manuscript, simulation methodology, parameter definitions, MFF calculation details, perturbation theory derivation, and all figures/tables

## Reviewer
- **Overall assessment** The abstract presents a conceptually important challenge to the assumption that SAXS data can uniquely constrain disordered protein ensembles. The claim of many-to-one mapping between ensembles and MFFs is potentially significant for the field. However, the abstract alone provides insufficient detail to evaluate the rigor of the simulations, the generality of the conclusions, or the validity of the perturbation theory. The work appears technically sophisticated but the evidence base visible here is too limited to establish the case.
- **Who would be interested in the results, and why** Researchers in intrinsically disordered proteins, biophysical chemistry, and computational polymer physics would be interested. The findings bear on how SAXS data are interpreted for disordered systems, which is central to structural biology of IDPs and to understanding folding-unfolding energetics. The methodological aspects, particularly the perturbation theory, may appeal to theorists working on heteropolymer statistics.
- **Major strengths** The abstract addresses a timely and debated question in the field. The approach is explicitly general, not restricted to specific interaction schemes, which strengthens the claim of broad applicability. The finding that MFFs can be practically identical for ensembles with drastically different asphericity and end-to-end distance is striking and, if robust, would be an important cautionary result.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide quantitative measures of MFF differences, simulation ensemble sizes, or error estimates. The perturbation theory is mentioned but not described in any testable form. Without these, the claim of "practically identical" MFFs cannot be assessed.
- **Assessment against Nature-style criteria** Originality is high, as the many-to-one mapping claim challenges a common interpretive framework. Scientific importance is potentially high for IDP research, but the abstract does not demonstrate the breadth of impact. Interdisciplinary readership is plausible, but the abstract is written for specialists and may not be accessible to nonspecialists. Technical soundness cannot be evaluated from the abstract alone. Readability for nonspecialists is limited by undefined terms such as MFF, asphericity, and perturbation theory.
- **Recommendation posture** Currently not established from the provided evidence. The abstract suggests a potentially important result, but the visible material is insufficient to support the core claims. A full manuscript with detailed methods and quantitative results would be required for a supportive posture.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "some heterogeneous ensembles with asphericity and R(EE) drastically different from those of homogeneous ensembles can nonetheless exhibit practically identical MFFs."
- **Evidence pointer** Abstract text, location not provided
- **Concern** The abstract provides no quantitative definition of "practically identical" MFFs. No numerical thresholds, error bars, or statistical tests are described. The claim rests entirely on simulation results that are not visible in the abstract.
- **Why it matters** Without a clear metric for what constitutes "practically identical," the central claim is unfalsifiable from the provided material. The significance of the finding depends on whether the MFF differences are within experimental noise or are truly negligible.
- **Resolution test** Provide in the full manuscript a quantitative comparison of MFFs, including root-mean-square deviations, maximum differences, and comparison to typical SAXS experimental uncertainties. State the criterion used to declare two MFFs "practically identical."

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the ensemble to MFF mapping is practically many-to-one and likely nonsmooth."
- **Evidence pointer** Abstract text, location not provided
- **Concern** The claim of many-to-one mapping is presented as a general conclusion, but the abstract does not describe the range of ensembles tested, the parameter space explored, or the method for generating heterogeneous ensembles. The generality of the claim cannot be assessed.
- **Why it matters** If the many-to-one mapping is only demonstrated for a narrow set of cases, the conclusion may not hold broadly. The claim has direct implications for how SAXS data are interpreted, so overgeneralization would be misleading.
- **Resolution test** Describe the full parameter space of ensembles tested, including sequence compositions, interaction schemes, and chain lengths. Show that the many-to-one behavior persists across a wide and representative range of conditions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors mention "an analytical perturbation theory developed here for flexible heteropolymers" to showcase heteropolymeric variations of the R(EE)-R(g) relationship.
- **Evidence pointer** Abstract text, location not provided
- **Concern** The perturbation theory is mentioned but not described. No equations, assumptions, or validation are provided. It is impossible to evaluate whether the theory is correct, novel, or applicable to the systems discussed.
- **Why it matters** The perturbation theory is presented as a supporting element of the paper. If it is flawed or not general, the conclusions about heteropolymeric effects would be weakened.
- **Resolution test** Provide the full derivation in the manuscript, state the assumptions and limits of validity, and validate the theory against simulation results or known exact results for simple cases.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Abstract text
- **Evidence pointer** Abstract, location not provided
- **Issue** Terms such as "molecular form factors," "asphericity," and "perturbation theory" are used without definition. A reader outside the immediate field may struggle to follow the argument.
- **Required correction** Define these terms briefly in the abstract or provide a more accessible framing of the key concepts.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity of claims
- **Affected element** Abstract text
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "likely nonsmooth" is vague. It is unclear what mathematical property is being asserted about the mapping.
- **Required correction** Specify what "nonsmooth" means in this context, for example, whether small changes in ensemble properties can lead to large changes in MFFs, or whether the mapping is discontinuous in some defined sense.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of reporting
- **Affected element** Abstract text
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract does not state the range of chain lengths or sequence compositions studied. This limits the reader's ability to gauge the scope of the simulations.
- **Required correction** Include representative chain lengths and sequence types in the abstract or indicate that full details are in the manuscript.

## Risk / unsupported claims
- The claim that MFFs do not afford unique characterizations of conformational ensembles is unsupported from the abstract alone, as no quantitative evidence is visible.
- The claim that the ensemble to MFF mapping is "practically many-to-one and likely nonsmooth" is unsupported without a description of the tested ensemble space.
- The perturbation theory is mentioned but entirely unevaluable from the provided material.
- The statement that "differences can be rather small" for certain heterogeneous ensembles is vague and not quantified.