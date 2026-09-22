## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, acknowledgements) as provided on bioRxiv.
- **Assessment boundary** Scientific content, methodological soundness, validity of conclusions, and clarity of presentation. No assessment of formatting, grammar, or editorial style beyond readability for a general scientific audience.
- **Shared manuscript claim summary** The authors claim that the intrinsically disordered region (IDR) of transcription factor HOXA11, specifically a five-residue motif FDQFF, interacts promiscuously with two distinct sites (MLL and cMyb) on the KIX domain of CBP. This claim is supported by computational docking (RosettaDock) guided by experimental NMR constraints, with benchmarked controls using MLL and cMyb peptides.
- **Visible evidence base** Abstract, Introduction, Results (including docking of MLL/cMyb controls, eKBD at MLL site, eKBD at cMyb site), Discussion, Methods (structure preparation, rigid body docking protocol). Figures are referenced but not provided in the supplied text.
- **Missing materials affecting confidence** Figures (Figures 1-4) are referenced but not included. Experimental NMR data (chemical shift perturbations, Kd values) are cited from prior work [9] but not shown. No raw docking scores, RMSD distributions, or statistical analyses are provided. No details on the de novo folding of HOXA11 N-terminus beyond reference to prior work.

## Reviewer
- **Overall assessment** The manuscript presents a focused computational study aimed at characterizing the binding interface between the HOXA11 IDR and the KIX domain of CBP. The use of experimentally guided docking is appropriate and the benchmarking against known MLL and cMyb complexes is a strength. However, the central claim of promiscuous binding is supported by limited evidence, and several methodological details and validations are missing. The study is potentially of interest to researchers studying transcription factor IDRs and coactivator interactions, but the current evidence does not fully establish the conclusions.
- **Who would be interested in the results, and why** Researchers studying transcription factor regulation, intrinsically disordered proteins, protein-protein interactions, and the molecular basis of transcriptional coactivator recruitment. The study is also relevant to those interested in computational docking methods applied to IDRs and to the HOX family of transcription factors.
- **Major strengths** 1. The study addresses a biologically important question regarding how IDRs mediate specific yet promiscuous interactions with coactivators. 2. The use of experimental NMR constraints to guide docking is a sensible approach to reduce the conformational search space. 3. Benchmarking the docking protocol against known MLL and cMyb complexes provides a validation step that increases confidence in the methodology. 4. The identification of a specific five-residue motif (FDQFF) and its role in binding is a clear and testable hypothesis.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The authors claim that FDQFF interacts promiscuously with both MLL and cMyb sites of KIX, and that this interaction is biologically relevant.
  - **Evidence pointer** Results sections "Docking of eKBD to the MLL site" and "Docking of eKBD at cMyb site"; Discussion.
  - **Concern** The claim of promiscuous binding is based solely on docking simulations. While the authors reference prior NMR data [9] showing chemical shift perturbations, the current manuscript does not provide direct experimental evidence (e.g., binding affinity measurements, mutagenesis validation) that FDQFF binds to both sites with measurable affinity. The docking results show two conformations at the cMyb site and one at the MLL site, but the significance of these findings is unclear without experimental validation.
  - **Why it matters** Promiscuous binding is a strong claim that has implications for the mechanism of HOXA11-mediated transcription. If the binding is not experimentally validated, the conclusion remains speculative and could mislead subsequent studies.
  - **Resolution test** Provide experimental binding data (e.g., ITC, NMR titration with Kd values) for FDQFF binding to both MLL and cMyb sites, and/or mutagenesis of FDQFF residues showing loss of binding at both sites.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Methodological rigor
  - **Claim pointer** The authors claim that the docking protocol is validated by benchmarking against MLL and cMyb peptides.
  - **Evidence pointer** Results section "Docking of MLL and cMyb peptide to KIX"; Methods section "Rigid Body Docking".
  - **Concern** The benchmarking results are described qualitatively (e.g., "good agreement", "near-perfect alignment") but no quantitative metrics are provided. The RMSD values are mentioned (e.g., <0.4 Å for MLL, <1.0 Å for cMyb) but the number of models, the distribution of scores, and the criteria for selecting the "lowest energy" models are not fully described. Additionally, the use of a single NMR structure (2AGH) as the starting point for KIX may not capture conformational variability.
  - **Why it matters** Without rigorous quantitative benchmarking, it is difficult to assess whether the docking protocol is reliable for the subsequent eKBD docking. The conclusions depend on the accuracy of the docking, so methodological transparency is essential.
  - **Resolution test** Provide a detailed description of the scoring function, the selection criteria for the top models, and a statistical comparison of docked vs. experimental structures (e.g., RMSD distributions, Z-scores). Include a figure showing the docked models superimposed on the experimental structures.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Biological relevance
  - **Claim pointer** The authors suggest that the promiscuous binding of FDQFF to KIX is functionally relevant for HOXA11-mediated transcription.
  - **Evidence pointer** Discussion.
  - **Concern** The manuscript does not discuss the physiological context of the HOXA11-KIX interaction. The authors mention endometrial development but do not provide any cellular or in vivo data linking the FDQFF-KIX interaction to transcriptional outcomes. The relevance of the weak binding (Kd in the hundreds of micromolar range) is discussed but not experimentally supported.
  - **Why it matters** The study aims to provide mechanistic insight into transcription regulation. Without functional validation, the biological significance of the proposed interaction remains unclear.
  - **Resolution test** Perform cellular assays (e.g., reporter gene assays with HOXA11 mutants) to demonstrate that FDQFF is required for KIX-dependent transcriptional activation.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Methods section "Three Dimensional Structures of eKBD, KIX, MLL and cMyb"
  - **Evidence pointer** Methods.
  - **Issue** The description of how the eKBD structure was obtained is brief. The authors state that the lowest energy folded structure was identified as residues 82-152, but it is unclear how this region was selected and whether the eKBD structure is representative of the IDR in solution.
  - **Required correction** Provide more details on the de novo folding protocol, including the number of models generated, the energy distribution, and the criteria for selecting the lowest energy structure.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Results section "Docking of eKBD to the MLL site"
  - **Evidence pointer** Results.
  - **Issue** The authors mention electrostatic interactions between eKBD and KIX (e.g., Q140-K656, E147-K667) but do not discuss their potential significance or whether they are conserved across species.
  - **Required correction** Add a brief discussion of the electrostatic interactions and their potential role in binding specificity.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods section "Rigid Body Docking"
  - **Evidence pointer** Methods.
  - **Issue** The docking protocol is described but the exact parameters (e.g., number of Monte Carlo steps, temperature, scoring function weights) are not provided. This limits reproducibility.
  - **Required correction** Provide a detailed protocol or reference to a previous publication where the parameters are fully described.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Interpretation
  - **Affected element** Discussion.
  - **Evidence pointer** Discussion.
  - **Issue** The authors discuss the "fly casting model" but do not explain how their results support or contradict this model. The connection is vague.
  - **Required correction** Clarify how the observed promiscuous binding and weak affinity relate to the fly casting model, or remove the reference if it is not directly relevant.

## Technical failings that need to be addressed before the case is established
- R1-M1: Lack of experimental validation for promiscuous binding.
- R1-M2: Insufficient quantitative benchmarking of the docking protocol.
- R1-M3: No functional data linking the proposed interaction to biological outcomes.

## Risk / unsupported claims
- The claim that FDQFF binds promiscuously to both MLL and cMyb sites is unsupported by direct experimental evidence in this manuscript.
- The claim that the docking models are accurate representations of the HOXA11-KIX interaction is not fully supported due to limited benchmarking details.
- The biological relevance of the interaction is speculative and not experimentally demonstrated.
- The statement that "the docking results correlate well with experimental findings" is not substantiated with quantitative data.

## Assessment against Nature-style criteria
- **Originality** Moderate. The study applies existing docking methods to a new system (HOXA11-KIX) and identifies a specific motif, but the approach is not novel.
- **Scientific importance** Moderate. The findings could be relevant to understanding IDR-mediated interactions, but the lack of experimental validation limits the impact.
- **Interdisciplinary readership** Limited. The study is primarily of interest to computational biologists and biochemists studying protein interactions.
- **Technical soundness** Weak. The docking protocol is not fully described or validated, and the conclusions rely heavily on computational predictions without experimental support.
- **Readability for nonspecialists** Acceptable. The manuscript is generally clear, but the methods section assumes familiarity with docking terminology.

## Recommendation posture
Currently not established from the provided evidence. The study has potential, but the central claim of promiscuous binding requires experimental validation, and the docking methodology needs more rigorous benchmarking and transparency. The manuscript would be suitable for a specialized journal after major revisions, but it does not meet the standards for a high-impact general journal.