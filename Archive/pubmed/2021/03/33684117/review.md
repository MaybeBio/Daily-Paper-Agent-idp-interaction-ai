## Review setup
- **Input scope** Full manuscript text (Abstract, Introduction, Materials and methods, Results, Discussion, Supporting Information references)
- **Assessment boundary** Scientific claims, methodological soundness, and internal consistency of the reported simulation study; no assessment of experimental validation or biological verification beyond what is presented
- **Shared manuscript claim summary** The authors use coarse-grained molecular dynamics simulations of three Swc5 IDR segments in a slab geometry to show that LLPS occurs at low temperatures, depends on sequence length and charge pattern, and that chain conformations can be classified into three forms (packed, dispersed, fully-spread) that are distinguishable on phase diagrams.
- **Visible evidence base** Main text figures (Fig 1–7), Supporting Information figures S1–S14, and tables referenced in text; no raw simulation trajectories or analysis scripts provided
- **Missing materials affecting confidence** Simulation parameter files, force field details, convergence criteria, error bars on phase boundaries, and full statistical analysis of the reported quantities are not provided; the Supporting Information is referenced but not fully included in the supplied material

## Reviewer
- **Overall assessment** The manuscript addresses a relevant question in the LLPS field, namely how sequence length and charge patterning affect phase separation of IDR ensembles. The slab simulation approach is appropriate and the observation of three conformational forms is potentially interesting. However, the current evidence base is insufficient to fully support several key claims, particularly regarding the thermodynamic interpretation of the phase diagram, the role of electrostatics, and the generality of the proposed "trinity" classification. The manuscript would benefit from additional quantitative analysis, clearer methodological details, and a more cautious framing of the conclusions.
- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation of intrinsically disordered proteins, computational biophysicists interested in coarse-grained models of IDPs, and experimentalists investigating chromatin remodeling complexes involving Swc5 or similar chaperones. The work may also be of interest to those developing sequence-based predictors of phase behavior.
- **Major strengths** The study uses a well-established slab geometry to probe LLPS, which is computationally efficient and allows direct observation of phase coexistence. The systematic variation of sequence length and charge pattern across three Swc5 segments is a reasonable design. The identification of three distinct conformational forms (packed, dispersed, fully-spread) is a useful conceptual framework that may aid interpretation of IDP ensemble behavior.
- **Major Concerns** 
  - R1-M1: The claim that LLPS "can be observed at low temperatures even without charge interactions" is not sufficiently supported by quantitative evidence. The threshold for LLPS detection (PH − PL > 0.07) appears arbitrary and is not justified. The authors do not provide error bars or statistical significance tests for the phase boundaries.
  - R1-M2: The interpretation of the effect of electrostatics on Tcr is based on comparisons across sequences with different lengths, charge numbers, and SCD values, making it difficult to isolate the role of charge patterning. The claim that SCD values can explain the observed trends is not rigorously tested.
  - R1-M3: The proposed "three forms" classification (packed, dispersed, fully-spread) is based on qualitative inspection of D and σ distributions. The authors do not provide a quantitative criterion for distinguishing these forms, nor do they demonstrate that the classification is robust across simulation conditions.
  - R1-M4: The relationship between the simulated temperature scale (in reduced units) and experimental temperatures is not established. The authors state that "the simulation temperature cannot be transformed to the real temperature directly," which limits the biological relevance of the findings.
- **Minor Comments** 
  - R1-m1: The manuscript would benefit from a more detailed description of the coarse-grained model, including the exact form of the bonded and non-bonded potentials, and the justification for the chosen parameters.
  - R1-m2: The authors should clarify how the "head-end distance" is defined for each chain and whether this metric is appropriate for capturing conformational changes in IDPs.
  - R1-m3: The statement that "the strange behavior observed for the swc ensemble is different from that of the free IDPs" is intriguing but not fully explained. A more detailed discussion of the physical origin of this behavior would strengthen the manuscript.
  - R1-m4: The authors should consider providing a comparison with experimental data on Swc5 or related IDPs to contextualize the simulation results.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** 
  - Originality: Moderate. The application of slab simulations to Swc5 IDRs is new, but the general approach and findings are consistent with prior work on IDP phase separation.
  - Scientific importance: Moderate. The study addresses a relevant question but does not provide a major conceptual advance beyond existing literature.
  - Interdisciplinary readership: Limited. The manuscript is primarily of interest to computational biophysicists and LLPS researchers; the biological implications for Swc5 function are speculative.
  - Technical soundness: Weak. Several methodological details are missing, and the quantitative support for key claims is insufficient.
  - Readability for nonspecialists: Acceptable. The manuscript is generally clear, but the reduced units and simulation details may be challenging for non-experts.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript has potential but requires substantial revisions to address the technical and quantitative concerns before the claims can be considered supported.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "LLPS can be observed at low temperatures even without charge interactions and disappear at high temperatures."
- **Evidence pointer** Results section, Fig 2; threshold definition in Materials and methods
- **Concern** The detection of LLPS relies on a threshold of PH − PL > 0.07, which is not justified. The authors do not provide error estimates or statistical tests to confirm that the observed differences are significant. Additionally, the choice of 30 windows along the z-axis may affect the sensitivity of the detection.
- **Why it matters** The phase diagram is central to the manuscript's conclusions. Without robust criteria for LLPS detection, the reported Tcr values and the claimed temperature dependence are not reliable.
- **Resolution test** Provide a sensitivity analysis of the LLPS detection threshold, include error bars or confidence intervals for PH − PL, and demonstrate that the phase boundaries are robust to the choice of window size and simulation length.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretive validity
- **Claim pointer** "The results suggest that the electrostatic interactions on the LLPS behaviors can change significantly with the ratios and distributions of the charged residues, especially the sequence charge decoration (SCD) values."
- **Evidence pointer** Results section, Fig 2 and Fig 4; Discussion section
- **Concern** The comparison across Swc5 segments involves simultaneous changes in sequence length, total charge, and charge distribution. The authors attribute observed differences to SCD values, but this attribution is not supported by a controlled analysis. The claim that SCD is the key determinant is therefore speculative.
- **Why it matters** The manuscript aims to identify sequence features that govern LLPS. If the effect of SCD is not isolated from other variables, the conclusions may be misleading.
- **Resolution test** Perform simulations with sequences that vary SCD while keeping length and total charge fixed, or use a statistical approach (e.g., regression) to disentangle the contributions of different sequence features.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Conceptual robustness
- **Claim pointer** "Three different forms of swc chains can be distinguished on the phase diagrams of D and σ values: packed form (P), dispersed form (D), and fully-spread form (F)."
- **Evidence pointer** Results section, Fig 6 and Fig 7
- **Concern** The classification into three forms is based on visual inspection of D and σ distributions. No quantitative clustering or statistical criterion is provided to define the boundaries between forms. It is unclear whether these forms are truly distinct or represent a continuum.
- **Why it matters** The "trinity" classification is a key conceptual contribution of the manuscript. If the forms are not well-defined, the framework may not be useful for interpreting IDP ensemble behavior.
- **Resolution test** Apply a formal clustering algorithm (e.g., Gaussian mixture models) to the D and σ data, and report the separation between clusters and the robustness of the classification across simulation conditions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Relevance and generalizability
- **Claim pointer** "The trends of simulated Tcr values can reveal the probability of LLPS behaviors."
- **Evidence pointer** Materials and methods section; Discussion section
- **Concern** The simulation temperature is in reduced units and cannot be mapped to experimental temperatures. This limits the ability to compare the simulated phase behavior with experimental observations or to make quantitative predictions about biological conditions.
- **Why it matters** The biological relevance of the findings depends on the ability to relate simulation conditions to physiological environments. Without a mapping, the implications for Swc5 function remain speculative.
- **Resolution test** Discuss potential approaches for mapping reduced units to physical temperatures, or provide qualitative arguments for how the trends might translate to experimental conditions.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Materials and methods section
- **Issue** The coarse-grained model parameters are not fully described. The authors mention calibration of ε and σ but do not provide the final values or the calibration procedure.
- **Required correction** Provide a table of all model parameters, including the functional form of the potentials, and describe the calibration process in detail.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results
- **Evidence pointer** Results section, Fig 5
- **Issue** The definition of "head-end distance" is not explicitly stated. It is unclear whether this refers to the end-to-end distance of the full chain or a specific subset of residues.
- **Required correction** Define the head-end distance clearly in the Methods section and specify which residues are used for the calculation.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretive clarity
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The statement that "the strange behavior observed for the swc ensemble is different from that of the free IDPs" is not fully explained. The authors should elaborate on the physical mechanism underlying this difference.
- **Required correction** Expand the discussion to provide a mechanistic explanation for the observed conformational behavior, possibly with reference to inter-chain interactions or excluded volume effects.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Contextualization
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The manuscript does not compare the simulated phase behavior with experimental data on Swc5 or related IDPs. Such a comparison would strengthen the biological relevance of the findings.
- **Required correction** Add a paragraph discussing how the simulation results relate to experimental observations of Swc5 or other IDP systems, even if only qualitatively.

## Risk / unsupported claims
- The claim that LLPS occurs "even without charge interactions" is supported only by the PH − PL metric, which lacks statistical validation.
- The attribution of differences in Tcr to SCD values is not supported by a controlled comparison.
- The "three forms" classification is not quantitatively defined and may not be robust.
- The relationship between reduced simulation temperatures and physical temperatures is not established, limiting the biological interpretation.
- The statement that "the trends of simulated Tcr values can reveal the probability of LLPS behaviors" is vague and not operationalized.