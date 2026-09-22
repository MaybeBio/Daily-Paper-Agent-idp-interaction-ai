## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific soundness, methodological rigor, validity of claims relative to presented evidence, and alignment with Nature-style criteria
- **Shared manuscript claim summary** The authors present a hybrid approach combining NMR chemical shift data (CSP, TALOS, sparse NOEs) with MELD molecular dynamics simulations to determine structures of protein–peptide complexes involving disorder-to-order transitions. They demonstrate the method on BRD3-ET and BRD4-ET complexes with various peptide partners, including blind predictions, and compare performance against AlphaFold. They also estimate relative binding affinities via competitive binding simulations.
- **Visible evidence base** Abstract, full introduction, methods (NMR, ITC, MELD, AlphaFold), results (blind studies, known complexes, competitive binding), discussion, conclusions, figure captions referenced in text, supplementary figure/table references
- **Missing materials affecting confidence** Actual figures and supplementary tables (S1–S10) not provided; numerical data for IRMSD, fnat, ILRMSD values only partially reported in text; detailed MELD convergence metrics not shown; AlphaFold confidence scores (pLDDT, PAE) not presented; raw NMR spectra and assignment completeness not assessable

## Reviewer
- **Overall assessment** This manuscript addresses a significant and timely problem in structural biology: predicting structures of protein–peptide complexes where the peptide folds upon binding. The hybrid MELD + NMR approach is conceptually sound and the blind study design is commendable. The results demonstrate that sparse NMR data can guide simulations to accurate bound-state conformations for moderately tight binders, and that additional peptide chemical shift data extend applicability to weaker complexes. However, several technical concerns regarding the generalizability of the method, the quantitative interpretation of funneling plots, the accuracy of relative binding affinity estimates, and the comparison with AlphaFold require clarification. The manuscript is well-written and will interest a broad readership, but the case for broad applicability is not fully established from the provided evidence.

- **Who would be interested in the results, and why** Structural biologists studying protein–peptide interactions, computational chemists developing integrative modeling approaches, NMR spectroscopists interested in sparse-data structure determination, and researchers in drug discovery targeting protein–peptide interfaces. The work is also relevant to the growing community applying machine learning methods (e.g., AlphaFold) to complex prediction, as it provides a complementary physics-based approach with uncertainty quantification.

- **Major strengths**
  1. The blind study design is rigorous and addresses a real need for unbiased assessment of structure prediction methods.
  2. The incremental information content across three data tiers (CSP, CSP + TALOS, CSP + TALOS + NOE) provides a clear demonstration of how data quantity affects prediction accuracy.
  3. The use of funneling plots to assess prediction confidence is a valuable contribution, as it offers a practical diagnostic for when a prediction can be trusted.
  4. The competitive binding simulations provide a physically grounded approach to estimating relative affinities, which is rarely attempted in docking studies.
  5. The comparison with AlphaFold is balanced and highlights complementary strengths of both methods.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the MELD + NMR approach "successfully modeled bound-state conformations and binding poses" for the blind study complexes, with IRMSD values of 2.28 Å and 1.97 Å for TP and NSD3, respectively.
- **Evidence pointer** Results section, Figure 3; location not provided for exact IRMSD values
- **Concern** The reported IRMSD values are computed against the final NMR-derived structures, which themselves are ensemble representations. It is unclear whether the comparison is against the medoid structure, the full ensemble, or a specific conformer. Additionally, the IRMSD values are only reported for the best-performing data tier; the range of IRMSD values across independent simulations or across the top five clusters is not provided. Without this information, it is difficult to assess the robustness and reproducibility of the predictions.
- **Why it matters** The central claim of the paper is that the method reliably predicts bound-state conformations. If the reported accuracy is only achieved in a subset of simulations or depends on favorable initial conditions, the generalizability of the method is questionable. The lack of uncertainty quantification undermines the practical utility of the approach.
- **Resolution test** Provide IRMSD distributions across all independent simulations and for the top five clusters for each data tier. Report the fraction of simulations that converge to within 3 Å of the reference structure. If possible, compare against the full NMR ensemble rather than a single representative structure.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the hybrid MELD + NMR approach required additional peptide ligand chemical shift data for weaker (Kd ~250 μM) peptide binding partners," implying that the method's applicability depends on binding affinity.
- **Evidence pointer** Abstract, Results section, Figure 3
- **Concern** The relationship between binding affinity and the amount of data required is not systematically explored. Only two blind complexes are presented (TP and NSD3), and the claim that weaker binders require more data is based on a single comparison. It is unclear whether this trend holds across a broader range of affinities and peptide sequences. Additionally, the JMJD6 complex (Kd ~160 μM) was not successfully modeled even with the highest data tier, which contradicts the proposed trend.
- **Why it matters** The manuscript positions the method as broadly applicable to protein–peptide complexes, but the evidence base is too narrow to support this claim. If the method fails for certain weak binders regardless of data quantity, the practical scope needs to be more clearly defined.
- **Resolution test** Apply the method to a larger panel of peptide–protein complexes spanning a wider range of binding affinities (e.g., 10 nM to 1 mM) and systematically vary the data tier. Report success rates as a function of affinity and data content. Discuss why JMJD6 fails despite having a similar affinity to NSD3.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that "MELD can directly estimate relative binding affinities" and report a ΔΔGTP/NSD3 of −2.45 ± 0.20 kcal/mol from competitive binding simulations.
- **Evidence pointer** Results section, Figure 5, Competitive Binding Simulations subsection
- **Concern** The reported ΔΔG differs from the experimental value (−5.5 ± 1 kcal/mol) by approximately 3 kcal/mol. While the authors acknowledge this discrepancy, they attribute it to "high experimental and computational uncertainties." However, the uncertainty in the computational estimate (±0.20 kcal/mol) is reported as very small, which is inconsistent with the large deviation from experiment. This suggests either a systematic error in the method or an underestimation of the statistical uncertainty.
- **Why it matters** The ability to estimate relative binding affinities is a key differentiator of the MELD approach compared to AlphaFold. If the accuracy is only qualitative, the claim that MELD "can directly estimate" affinities is overstated. The discrepancy also raises questions about the reliability of the funneling analysis for identifying the correct bound state.
- **Resolution test** Perform a more thorough error analysis, including bootstrapping or multiple independent simulations, to obtain a realistic uncertainty estimate. Test the method on additional pairs of peptides with known affinity differences to establish the range of applicability. Discuss potential sources of systematic error (e.g., force field inaccuracies, implicit solvent model).

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "AlphaFold also successfully predicts the structures of some of these peptide–protein complexes" and that "AlphaFold can provide qualitative peptide rankings."
- **Evidence pointer** Results section, AlphaFold Predictions subsection, Figure S3
- **Concern** The AlphaFold comparison is presented without quantitative metrics. It is unclear how "successful" predictions are defined (e.g., IRMSD threshold) and how the rankings are derived. The authors note that AlphaFold predicts an additional alpha helix in the NSD3 tail that is unstructured in the NMR structure, but the implications of this discrepancy for the overall complex prediction are not discussed. The comparison would be strengthened by a systematic evaluation using the same metrics as for MELD.
- **Why it matters** The manuscript positions AlphaFold as a complementary tool, but the evidence for this claim is anecdotal. A rigorous comparison is needed to support the recommendation that AlphaFold can be used for initial screening.
- **Resolution test** Provide IRMSD, fnat, and ILRMSD values for all AlphaFold predictions, using the same reference structures as for MELD. Report the ranking accuracy for the competitive binding scenario. Discuss the significance of the extra helix prediction for the NSD3 complex.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction, first paragraph
- **Evidence pointer** Introduction, paragraph 1
- **Issue** The introduction assumes familiarity with terms such as "extraterminal domain," "bromo and extraterminal domain proteins," and "folding-upon-binding" without sufficient context for a general reader.
- **Required correction** Provide a brief explanation of the biological relevance of BET proteins and the ET domain, and define "folding-upon-binding" in plain language.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, MELD Simulations
- **Evidence pointer** Methods, MELD Simulations subsection
- **Issue** The description of the MELD simulation parameters is incomplete. The force field combination (ff14SB side chains, ff99SB backbone) is unusual and may affect the results. The rationale for this choice is not provided.
- **Required correction** Justify the force field choice or cite prior work validating this combination. Provide details on the number of independent simulations, convergence criteria, and how the funneling plots were generated.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion, paragraph on funneling plots
- **Evidence pointer** Discussion, paragraph 3
- **Issue** The claim that funneling plots "provide an assessment of the reliability of any particular docking study" is based on a limited number of examples. The threshold for "highly funneled" is not defined quantitatively.
- **Required correction** Define a quantitative metric for funneling (e.g., population of the top cluster, ratio of bound to unbound states) and demonstrate its predictive power across a larger set of test cases.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Results, Blind Studies subsection
- **Evidence pointer** Results, Blind Studies subsection, Figure 3
- **Issue** The description of the "flipped" orientations of TP and NSD3 peptides is difficult to follow without a clear visual representation. The figure is referenced but not shown in the provided text.
- **Required correction** Add a schematic or textual description that clearly explains the difference in binding orientation between the two peptides.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, ITC Measurements
- **Evidence pointer** Methods, Isothermal Titration Calorimetry subsection
- **Issue** The ITC measurements were performed at 10 °C for NSD3 due to aggregation at 25 °C, but the NMR structures were determined at a different temperature. The potential impact of temperature differences on the comparison between predicted and experimental structures is not discussed.
- **Required correction** Discuss whether temperature differences could affect the binding mode or affinity and whether this could explain any discrepancies between predictions and experiments.

## Risk / unsupported claims
- The claim that the method is broadly applicable to protein–peptide complexes involving disorder-to-order transitions is not fully supported, as only two blind complexes and four additional complexes were tested, with mixed success.
- The claim that "MELD can directly estimate relative binding affinities" is overstated given the 3 kcal/mol discrepancy with experiment for the one test case presented.
- The assertion that funneling plots reliably indicate prediction accuracy is based on a small number of examples and lacks a quantitative definition.
- The comparison with AlphaFold is qualitative and lacks systematic metrics, making it difficult to evaluate the claim that AlphaFold provides complementary information.
- The statement that "the approach outlined here is limited to cases where extensive backbone resonance assignments can be obtained" is a significant caveat that is not prominently featured in the abstract or conclusions.