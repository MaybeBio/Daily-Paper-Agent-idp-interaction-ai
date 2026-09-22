## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, data interpretation, and conclusions as presented in the provided manuscript
- **Shared manuscript claim summary** The authors report that D-enantiomeric NLS peptides derived from NUPR1, NUPR1L, and PADI4 bind to human importin α3 (Impα3) and its IBB-truncated form (∆Impα3) with affinities similar to their L-enantiomer counterparts, at the same binding site, and that chirality does not affect the disordered nature of the peptides or the binding outcome.
- **Visible evidence base** Abstract, Introduction, Results (Sections 2.1–2.3), Discussion, Conclusions, Materials and Methods (Sections 4.1–4.8), Figures 1–6, Tables 1–4, Supplementary Tables S1–S4
- **Missing materials affecting confidence** Raw NMR spectra, full ITC thermograms for all peptides, BLI sensorgram fits, docking pose ensembles with statistical validation, error analysis for all reported Kd values, and explicit statistical treatment of replicate measurements

## Reviewer
- **Overall assessment** The manuscript addresses an interesting and potentially important question: whether the nuclear import machinery tolerates D-enantiomeric NLS peptides. The authors combine multiple biophysical techniques and molecular docking to support their claim. However, the evidence presented has significant gaps. The fluorescence titrations did not yield reliable Kd values for most peptides, ITC only worked for one peptide, and the BLI-derived Kd values are described as "apparent" without clear validation of the two-state model assumption. The docking simulations, while suggestive, lack rigorous statistical validation. The central claim of "tolerance to chirality" rests heavily on comparisons with previously published L-enantiomer data, but the direct quantitative comparison is incomplete. The conclusion that chirality is not important for binding is plausible but not fully established from the data as presented.

- **Who would be interested in the results, and why** Researchers in nuclear transport, peptide-based drug design, and the growing field of mirror-image biology would find these results relevant. The potential use of D-peptides as stable, non-immunogenic inhibitors of nuclear import has therapeutic implications for cancer and viral infections. The broader question of chirality tolerance in protein–peptide interactions is of interest to the structural biology and biophysics communities.

- **Major strengths** The study addresses a novel and timely question with potential therapeutic relevance. The combination of multiple orthogonal techniques (NMR, fluorescence, ITC, BLI, docking) is commendable. The authors are transparent about the limitations of each technique. The comparison with previously published L-enantiomer data provides context. The manuscript is generally well-written and accessible.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that D-NLS peptides bind to Impα3 and ∆Impα3 with affinities similar to their L-enantiomer counterparts.
- **Evidence pointer** Tables 2 and 3, Section 2.2
- **Concern** The central quantitative claim relies on BLI-derived apparent Kd values for most peptides, but ITC only yielded binding isotherms for D-NLS-NUPR1L. Fluorescence titrations did not produce reliable Kd values for most peptides. The BLI Kd values are described as "apparent" and depend on a two-state model assumption that is not validated. For D-NLS-NUPR1, no Kd could be determined at all. The comparison with L-enantiomer affinities is therefore incomplete and based on different techniques for different peptides.
- **Why it matters** The core conclusion that chirality does not affect binding affinity cannot be rigorously established if the affinity values for the D-peptides are not reliably measured across the full set of peptides. The claim of "similar affinities" requires a consistent and validated quantitative basis.
- **Resolution test** Provide reliable Kd values for all D-NLS peptides using at least one technique with appropriate error analysis. Validate the two-state model for BLI fitting. Directly compare D- and L-enantiomer affinities using the same technique under identical conditions for all peptides.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that docking simulations show D-NLS peptides target the major NLS binding site of ∆Impα3.
- **Evidence pointer** Section 2.3, Figure 6, Table 4
- **Concern** The docking results are presented as evidence for binding location, but no statistical validation is provided. There is no clustering analysis, no comparison with known L-NLS binding modes, no RMSD-based pose selection criteria, and no discussion of docking score reliability. The binding energies in Table 4 are reported without error estimates. The use of a truncated peptide for D-NLS-PADI in simulations (Q502–Q523) versus the full-length peptide used in experiments (K499–K526) introduces a potential inconsistency.
- **Why it matters** Docking predictions are only meaningful with proper validation. Without statistical rigor, the claim that D-peptides bind at the same site as L-peptides is not convincingly supported. The discrepancy between simulated and experimental peptide lengths could affect the relevance of the docking results.
- **Resolution test** Provide docking validation including pose clustering, comparison with experimental binding data, error estimates for binding energies, and justification for using a truncated peptide in simulations. Ideally, support docking with mutagenesis or competition experiments.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation
- **Claim pointer** The authors suggest that the lack of chirality discrimination is due to the intrinsic disorder of the NLS peptides and the flexibility of Impα3.
- **Evidence pointer** Section 3 (Discussion)
- **Concern** The mechanistic interpretation is speculative. While the authors cite a previous study on c-Myc NLS chirality tolerance, the current data do not directly test the proposed mechanism. The connection between peptide disorder, receptor flexibility, and chirality tolerance is not experimentally addressed. The authors acknowledge the potential bias from Impα3 flexibility but do not provide evidence to support this explanation.
- **Why it matters** The proposed mechanism is a key part of the discussion and frames the broader significance. Without direct evidence, the interpretation remains speculative and could be misleading for future studies.
- **Resolution test** Provide experimental or computational evidence directly testing the role of disorder and flexibility in chirality tolerance, such as binding studies with more rigid NLS peptides or mutations that reduce Impα3 flexibility.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The authors report that D-NLS peptides are monomeric and disordered in solution based on NMR data.
- **Evidence pointer** Section 2.1, Figure 1, Tables S1–S4
- **Concern** The NMR characterization is presented briefly. The diffusion coefficients are reported, but the hydrodynamic radius calculations and comparison with theoretical values for random-coil peptides are not shown in detail. The 2D NMR assignments are mentioned but not fully presented. The statement that "no medium- or long-range NOEs were detected" is based on partial assignments for some peptides.
- **Why it matters** The disordered nature of the peptides is a key premise for the interpretation. Incomplete NMR characterization weakens this foundational claim.
- **Resolution test** Provide complete NMR assignment tables, show the DOSY decay curves and fitting, and present the hydrodynamic radius calculations with error estimates. Clearly state the fraction of residues assigned for each peptide.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.2, fluorescence titrations
- **Evidence pointer** Figure 3, Figure S1
- **Issue** The fluorescence titration results are described as showing "a decrease in fluorescence intensity" but no quantitative analysis is provided. The statement that Kd values could not be determined is vague.
- **Required correction** Provide representative titration curves with error bars, state the concentration range explored, and explain why Kd could not be determined (e.g., binding too weak, aggregation, or signal too small).

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2.2, ITC experiments
- **Evidence pointer** Figure 4, Figure S2
- **Issue** ITC data are only shown for D-NLS-NUPR1L. For the other peptides, the authors state that no binding isotherm was obtained, but the raw data are not shown.
- **Required correction** Show representative ITC traces for all peptides, including those that did not yield isotherms, to demonstrate that the experiments were performed and the negative results are reliable.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Section 2.2, BLI experiments
- **Evidence pointer** Figure 5, Figure S3, Tables 2 and 3
- **Issue** The BLI-derived Kd values are called "apparent" but the basis for this qualifier is not explained. The relationship between BLI Kd values and ITC Kd values for D-NLS-NUPR1L is not discussed.
- **Required correction** Clarify why the Kd values are "apparent" and discuss any discrepancies between techniques for the one peptide where both were measured.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Section 4.8, Molecular docking
- **Evidence pointer** Section 4.8
- **Concern** The docking methodology is described briefly. The choice of AutoDock Vina parameters, the preparation of the receptor structure, and the handling of peptide flexibility are not fully detailed.
- **Required correction** Provide more detail on receptor preparation, grid box definition, peptide conformational sampling, and the number of docking runs performed.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Language
- **Affected element** Abstract, last sentence
- **Evidence pointer** Abstract
- **Issue** The final sentence of the abstract is awkwardly phrased and could be misinterpreted.
- **Required correction** Rephrase for clarity, e.g., "the primary structure of the NLS binding hot spot on importin is well defined, yet the stereochemical nature of the NLS does not determine binding."

- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative affinity comparison incomplete), R1-M2 (docking validation lacking), R1-M3 (mechanistic interpretation speculative), R1-M4 (NMR characterization incomplete)

- **Assessment against Nature-style criteria** 
  - Originality: The question of chirality tolerance in NLS recognition is novel and has not been systematically addressed for importin α3. The study is original in its specific focus.
  - Scientific importance: The findings could have implications for understanding the evolutionary constraints on nuclear transport and for designing D-peptide-based therapeutics. However, the importance is moderate, as the study is limited to in vitro and in silico observations without cellular or in vivo validation.
  - Interdisciplinary readership: The topic bridges structural biology, biophysics, and drug design, which could attract readers from multiple fields. However, the technical nature of the manuscript may limit broader appeal.
  - Technical soundness: The multi-technique approach is appropriate, but the incomplete quantitative data and lack of docking validation are significant weaknesses.
  - Readability for nonspecialists: The manuscript is generally well-written, but the Results section assumes familiarity with biophysical techniques. The abstract is accessible, though the final sentence needs clarification.

- **Recommendation posture** Supportive if technical concerns are resolved. The core question is interesting and the multi-technique approach is appropriate, but the quantitative evidence for the central claim is incomplete. The authors must provide reliable affinity measurements for all peptides, validate the docking results, and either provide direct evidence for the proposed mechanism or temper the interpretation.

## Risk / unsupported claims
- The claim that D-NLS peptides bind with "similar affinities" to L-NLS peptides is not fully supported because reliable Kd values were not obtained for most D-NLS peptides by any technique.
- The claim that D-NLS peptides target the major NLS binding site is based on docking without statistical validation and is therefore not firmly established.
- The mechanistic interpretation that disorder and flexibility explain chirality tolerance is speculative and not directly tested.
- The statement that "the stereoisomeric nature is not important in defining the binding" is too broad given the incomplete quantitative data.
- The comparison with L-enantiomer data relies on previously published results from different experimental conditions and techniques, which limits the validity of the direct comparison.