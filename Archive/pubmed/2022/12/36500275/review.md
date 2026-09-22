## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Computational methodology, structural analysis, docking and molecular dynamics results, and conclusions as presented
- **Shared manuscript claim summary** The authors investigate the binding of the pentapeptide LPRDA to S. aureus Sortase A using docking and molecular dynamics. They report that LPRDA binds in a "reverse" orientation relative to the canonical LPxTG sorting sequence, that the SrtA binding site loops exhibit enhanced conformational sampling when complexed with LPRDA, and that no single dominant binding mode can be identified due to the shallow energy landscape and intrinsic disorder of the loops.
- **Visible evidence base** Abstract, Introduction, Results (Sections 2.1–2.4), Discussion, Conclusions, Materials and Methods (Section 4), Figures 1–10, Tables 1–2, Supplementary Tables S1–S4 referenced
- **Missing materials affecting confidence** Supplementary figures (Figure S1) and tables (Tables S1–S4) are referenced but not provided; no experimental validation data; no convergence metrics for MD simulations; no error estimates for docking energies; no force field validation details; no explicit treatment of Ca2+ in simulations

## Reviewer
- **Overall assessment** This manuscript presents a systematic computational investigation of LPRDA binding to SrtA, with a critical evaluation of existing PDB structures and a detailed docking/MD protocol. The work is technically competent in its execution, and the observation that LPRDA may bind in a reverse orientation relative to LPxTG is potentially interesting. However, the central claims are largely negative or cautionary in nature, and the manuscript does not establish a definitive binding mode or provide a validated predictive protocol. The enhanced conformational sampling claim, while plausible, is based on short simulations without rigorous statistical analysis. The manuscript reads more as a methodological feasibility study than a definitive characterization of the LPRDA–SrtA interaction. The writing is generally clear but somewhat verbose, and the lack of quantitative convergence analysis weakens several key conclusions.

- **Who would be interested in the results, and why** Researchers working on Sortase A inhibitors, particularly those interested in peptide-based antivirulence strategies against S. aureus, would find this work relevant. Computational chemists and structural biologists studying intrinsically disordered regions in drug targets may also be interested in the methodological observations regarding loop plasticity. However, the audience is relatively narrow, and the lack of experimental validation limits broader appeal to medicinal chemists seeking actionable leads.

- **Major strengths**
  1. Critical and thoughtful evaluation of existing SrtA crystal/NMR structures, with explicit criteria for assessing ligand–protein complex quality.
  2. Systematic comparison of two docking programs (AutoDock and AutoDock Vina) with increased search exhaustiveness, acknowledging the limitations of each.
  3. Use of multiple independent MD replicas to assess reproducibility of binding modes, which is a good practice for flexible targets.
  4. Honest reporting of the inability to identify a single dominant binding mode, rather than overinterpreting ambiguous results.
  5. Clear articulation of the challenges posed by the intrinsically disordered β6/β7 loop for structure-based drug design.

- **Major Concerns**

  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that "the previously reported partially chaotic movement of the β6/β7 and β7/β8 loops of SrtA is exaggerated when SrtA is complexed with LPRDA" and that LPRDA acts as a "plasticizer" for these loops.
  - **Evidence pointer** Section 2.4, Figures 4–7, Tables S1–S4
  - **Concern** The claim of enhanced conformational sampling in the LPRDA-bound state relative to the apo state is based on visual inspection of aligned structures after 10 ns MD runs. No quantitative metrics (e.g., RMSD distributions, principal component analysis, free energy landscapes, or statistical tests comparing apo vs. holo fluctuations) are provided. The comparison with the apo form is made from only three 10 ns replicas, which is insufficient to establish statistically significant differences in conformational sampling, especially for intrinsically disordered regions. The "plasticizer" hypothesis is speculative and not supported by any free energy calculations or enhanced sampling methods.
  - **Why it matters** This is a central claim of the manuscript and is presented as a novel finding. Without quantitative evidence, the claim is not established and could mislead subsequent studies that rely on this observation.
  - **Resolution test** Provide quantitative measures of conformational sampling (e.g., RMSF values with error bars, dihedral angle distributions, or clustering analysis) for both apo and holo states, with statistical significance testing. Alternatively, perform longer simulations or enhanced sampling (e.g., replica exchange) to demonstrate that the enhanced sampling is not a short-time artifact.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors state that "the docking experiments—using both AutoDock and AutoDock Vina—consistently predicted that the most favorable binding modes of LPRDA are in the 'reverse direction' sequence orientation relative to the established order of the sorting sequence LPxTG."
  - **Evidence pointer** Section 2.2, Figures 1–3, Table 2
  - **Concern** The docking results show a range of binding energies across modes (e.g., −6.6 to −7.3 kcal/mol for AutoDock Vina), and the authors acknowledge that "the entire range of 15 complex geometries found by docking is close to the value of −6.9 kcal/mol reported by Wang." The energetic differences between "direct" and "reverse" orientation modes are not quantified, and no statistical analysis (e.g., energy distributions, Boltzmann weighting) is provided to support the claim that reverse modes are "most favorable." The selection of which modes to classify as "direct" vs "reverse" appears to be based on visual inspection, which is subjective.
  - **Why it matters** The reverse orientation claim is a key finding that differentiates this work from the original Wang et al. study. If the energetic preference is not statistically significant, the claim is overstated and could mislead subsequent drug design efforts.
  - **Resolution test** Provide a quantitative comparison of docking scores (with standard deviations) for direct vs reverse orientation modes, and perform a statistical test (e.g., Mann-Whitney U test) to determine if the difference is significant. Alternatively, use a more rigorous scoring function or consensus scoring to validate the ranking.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The authors state that "the main goal of the work was to establish the protocol to robustly model LPRDA (and its subsequent analogs) interaction with SrtA" and that "the useful insights about the nature of the interactions in a hypothetical LPRDA–SrtA complex were obtained."
  - **Evidence pointer** Sections 3 and 5
  - **Concern** The manuscript does not deliver a validated protocol. The authors themselves conclude that "the simple assumption that LPRDA binds similarly to the sorting sequence LPxTG is unlikely" and that "the search for a single 'correct' LPRDA–SrtA complex geometry seems to be an ill-defined problem when using fast and approximate means of modeling." This is a negative result that, while honest, does not provide a practical protocol for future drug design. The suggested use of "more elaborate modeling approaches" is vague and not tested.
  - **Why it matters** The stated goal is to establish a protocol for subsequent rational drug development. Without a validated protocol or clear recommendations for which approach to use, the practical utility of this work is limited.
  - **Resolution test** Provide a concrete, tested protocol with clear decision points (e.g., which docking program, which scoring function, how to select MD starting points, how to analyze results) and demonstrate its applicability on a test set of known SrtA inhibitors.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that "the PDB:1T2W structure... was chosen for the subsequent modeling" based on their analysis of available structures, and that this choice is justified because it provides "a more open binding site."
  - **Evidence pointer** Section 2.1, Table 1, Figure 9
  - **Concern** The choice of PDB:1T2W over other structures is based on qualitative visual inspection and the argument that it is "more open." However, the authors also note that PDB:1T2W is a C184A mutant, which may affect the binding site properties. The potential impact of this mutation on the docking and MD results is not discussed in detail. Additionally, the authors do not test whether their conclusions are robust to the choice of starting structure.
  - **Why it matters** The choice of starting structure is a critical decision in structure-based drug design. If the results are highly dependent on this choice, the conclusions may not be generalizable.
  - **Resolution test** Perform docking and MD simulations starting from multiple SrtA structures (e.g., PDB:2KID, PDB:1IJA) and compare the resulting binding modes and energies. If the conclusions are consistent across structures, the choice is justified; if not, the limitations should be acknowledged.

- **Minor Comments**

  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods section
  - **Evidence pointer** Section 4.1.1
  - **Issue** The authors state that "Wang et al. claim that the PDB:1T2P structure was used for modeling in their work, however a closer examination reveals that PDB:1T2W was actually used." This is a strong claim that could be perceived as accusatory. The evidence for this claim is based on visual comparison of figures, which is subjective.
  - **Required correction** Soften the language and provide more objective evidence (e.g., structural alignment metrics) to support the claim. Alternatively, present this as a discrepancy that the authors noted, without implying error on the part of Wang et al.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Figure 3
  - **Evidence pointer** Section 2.4.1, Figure 3
  - **Issue** The ligand efficiency (LE) values are presented in Figure 3, but the calculation method is not described in the text. It is unclear whether LE is calculated using the docking score or the MD-derived binding free energy.
  - **Required correction** Add a brief description of how LE is calculated and which energy value is used.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Supplementary materials
  - **Evidence pointer** Section 2.4, Tables S1–S4, Figure S1
  - **Issue** The manuscript references supplementary tables and figures that are not provided in the submitted material. This makes it impossible to fully evaluate the results.
  - **Required correction** Ensure all supplementary materials are included in the submission.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** MD simulation protocol
  - **Evidence pointer** Section 4.2.1
  - **Issue** The authors use MMFF94 charges for the ligand instead of the more common AM1-BCC charges, citing artifacts in the latter. However, the choice of MMFF94 charges is not standard for GAFF and may affect the accuracy of the simulations. No validation of this choice is provided.
  - **Required correction** Provide a brief justification for the use of MMFF94 charges and, if possible, compare results with AM1-BCC charges for a subset of simulations.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Readability
  - **Affected element** Section 2.1.2
  - **Evidence pointer** Section 2.1.2, "Other Complexes"
  - **Issue** The discussion of the remaining PDB structures is brief and somewhat dismissive. The authors state that the relevance of these structures "is questionable" without providing detailed reasoning for each structure.
  - **Required correction** Expand the discussion to provide a more balanced evaluation of each structure, or clearly state the criteria used to exclude them.

- **Technical failings that need to be addressed before the case is established**
  1. Lack of quantitative analysis for the enhanced conformational sampling claim (R1-M1).
  2. Insufficient statistical analysis of docking energy differences between direct and reverse orientations (R1-M2).
  3. No validation of the MD protocol (e.g., convergence checks, force field sensitivity analysis).
  4. No discussion of the potential impact of the C184A mutation in PDB:1T2W on the results.
  5. Missing supplementary materials that are referenced in the text.

- **Assessment against Nature-style criteria**
  - **Originality** Moderate. The application of docking and MD to a specific peptide–SrtA system is not novel in itself. The observation of reverse orientation binding and the "plasticizer" hypothesis are somewhat original, but they are not rigorously established.
  - **Scientific importance** Limited. The manuscript primarily reports negative or cautionary results, which are useful for the SrtA community but do not represent a major advance. The lack of experimental validation limits the significance of the findings.
  - **Interdisciplinary readership** Narrow. The work is primarily of interest to computational chemists and SrtA researchers. The findings are unlikely to attract a broad interdisciplinary audience.
  - **Technical soundness** Adequate but with significant gaps. The docking and MD protocols are reasonable, but the lack of quantitative analysis and validation weakens the conclusions.
  - **Readability for nonspecialists** Acceptable. The manuscript is generally well-written, but the heavy reliance on structural details and computational jargon may be challenging for nonspecialists. The abstract is clear, but the results section is dense.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript presents a thorough computational study with some interesting observations, but the central claims are not quantitatively supported, and the lack of experimental validation limits the impact. The authors should address the major concerns, particularly the quantitative analysis of conformational sampling and docking energy differences, before the case for reverse orientation binding and the "plasticizer" effect can be considered established.

## Risk / unsupported claims
- The claim that LPRDA acts as a "plasticizer" for the β6/β7 and β7/β8 loops is unsupported by quantitative evidence and is speculative.
- The claim that the "reverse direction" binding mode is preferred is not statistically validated.
- The assertion that PDB:1T2W was the structure used by Wang et al. is based on subjective visual comparison and is not definitively established.
- The statement that "the modeling procedure described by Wang et al. could not be reproduced" is not fully supported, as the authors did not attempt to replicate the exact protocol used by Wang et al.
- The conclusion that "the free energy surface of LPRDA–SrtA binding is a shallow valley with numerous minima" is inferred from short MD simulations without free energy calculations and is therefore not established.