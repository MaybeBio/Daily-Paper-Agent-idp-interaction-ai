## Review setup
- **Input scope** Full manuscript text (main text, figure legends referenced, methods summary, data availability)
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and internal consistency based solely on the provided manuscript text. No supplementary figures, tables, or datasets were available for direct inspection.
- **Shared manuscript claim summary** The authors report that ALS/WDM mutations in the TIA-1 prion-like domain (PLD) alter its self-assembly properties. They propose a five-amino acid model linking local backbone dynamics (measured by NMR relaxation) to amino acid physicochemical properties, and use MD simulations and cryo-EM crystal structures of a PLD segment to argue that P362L promotes β-sheet interactions and A381T induces highly condensed, amyloid-like assemblies, while E384K suppresses droplet formation.
- **Visible evidence base** Main text figures (Fig. 1A–E, 2A–E, 3A–E, 4A–I, 5A–J), SI references (Figs. S1–S13, Scheme S1, Dataset S1, Table S1), PDB depositions (7VI4, 7VI5), BMRB depositions (51102, 51103), Zenodo diffraction data.
- **Missing materials affecting confidence** All supplementary figures, tables, datasets, and detailed methods. Specifically, SI Appendix Figs. S1–S13, Scheme S1, Dataset S1, Table S1, and the full Materials and Methods were not provided. This limits verification of experimental details, statistical analyses, and the robustness of the five-amino acid model fitting.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question: how disease-associated mutations in the prion-like domain of TIA-1 alter its phase separation and aggregation behavior. The combination of biophysical assays, NMR relaxation analysis, MD simulations, and cryo-EM crystallography is ambitious and potentially impactful. However, the central quantitative model (five-amino acid model) is presented with limited validation, and the link between the crystal structures and the pathogenic mechanism remains partly speculative. The claim that E384K suppresses droplet formation contradicts a prior report, and the authors' explanation is underdeveloped. The evidence base is promising but incomplete as presented.
- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation, stress granules, RNA-binding proteins, and neurodegenerative disease mechanisms. The proposed five-amino acid model and the structural analysis of disease mutants will be of interest to those working on prion-like domains and the molecular determinants of condensate material properties.
- **Major strengths** 1) The study combines multiple orthogonal techniques (biochemistry, NMR, MD, cryo-EM crystallography) to address a complex problem. 2) The five-amino acid model is a novel conceptual framework that attempts to quantify sticker/spacer properties from sequence. 3) The cryo-EM crystal structures of WT and A381T peptides provide direct structural evidence for a mutation-induced change in assembly mode. 4) The authors are transparent about discrepancies with prior work (Mackenzie et al.) and attempt to reconcile them.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness / Statistical validation
  - **Claim pointer** The five-amino acid model reproduces experimental NMR relaxation rates with correlation coefficients of 0.78, 0.83, and 0.81 for R1, R2, and hNOE, respectively.
  - **Evidence pointer** Fig. 3C–D, SI Appendix Scheme S1 and Dataset S1 (not provided)
  - **Concern** The model fitting procedure is described only briefly. It is unclear how many free parameters were optimized, whether the model was validated on independent data, and how sensitive the correlation coefficients are to the choice of fitting algorithm or initial conditions. The risk of overfitting is substantial given the small number of amino acid types (20) and the large number of potential parameter combinations.
  - **Why it matters** The five-amino acid model is a central conceptual contribution. If the fit is not robust or is overfitted, the quantitative claims about sticker/spacer properties are not reliable.
  - **Resolution test** Provide a detailed description of the optimization procedure, including the number of parameters, convergence criteria, and cross-validation (e.g., leave-one-out or bootstrap). Show that the model performs significantly better than null models (e.g., random assignment of ILD values) and that the correlation coefficients are stable across different fitting runs.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency / Interpretive validity
  - **Claim pointer** The A381T mutation promotes highly condensed assemblies with few hydrated surfaces, resembling steric zippers in amyloid fibrils, and this underlies its pathogenicity.
  - **Evidence pointer** Fig. 5A–J, SI Appendix Table S1 (not provided)
  - **Concern** The crystal structures are of a 10-residue peptide (G377–Q386), not the full PLD or full-length protein. The relevance of this short segment to the behavior of the full-length protein in cells is not directly demonstrated. The claim that the A381T structure represents a "pathogenic" state is inferred from the packing density and solvation content, but no functional data (e.g., cellular toxicity, fibril formation kinetics) are presented to support this link.
  - **Why it matters** The structural data are the strongest evidence for a mutation-induced change in assembly mode. If the relevance of the peptide crystal to the full-length protein is not established, the pathogenic mechanism remains speculative.
  - **Resolution test** Show that the A381T mutation increases amyloid fibril formation or aggregation propensity in the full-length protein or in cells. Alternatively, demonstrate that the peptide crystal structure is consistent with the structure of fibrils formed by the full-length protein (e.g., by cryo-EM or solid-state NMR).
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Interpretive validity / Literature consistency
  - **Claim pointer** E384K suppresses droplet formation, contrary to the report by Mackenzie et al. that all three mutations promote droplet formation.
  - **Evidence pointer** Fig. 1D–E, SI Appendix Fig. S5 (not provided)
  - **Concern** The authors report a direct contradiction with a prior publication but do not provide a detailed explanation for the discrepancy. Possible reasons (e.g., differences in protein construct, buffer conditions, or measurement methods) are not systematically explored.
  - **Why it matters** The field needs to understand whether the discrepancy is due to technical differences or a genuine biological effect. Without this, the claim that E384K is functionally distinct from P362L and A381T is not fully supported.
  - **Resolution test** Perform head-to-head comparisons of WT, P362L, A381T, and E384K under identical conditions using multiple assays (e.g., turbidity, microscopy, FRAP). Discuss potential sources of discrepancy with Mackenzie et al. and, if possible, test them directly.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity / Reproducibility
  - **Affected element** Methods description
  - **Evidence pointer** Materials and Methods, "Data Analysis with Five-Amino Acid Model"
  - **Issue** The description of the model fitting is too brief. It is not clear how the ILD values were initialized, what constraints were applied, or how the "best" model was selected among different window sizes.
  - **Required correction** Expand the Methods section to include a step-by-step description of the fitting procedure, including initialization, optimization algorithm, constraints, and model selection criteria.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Interpretive validity
  - **Affected element** Discussion of E384K
  - **Evidence pointer** Discussion section
  - **Issue** The authors state that E384K "attenuates the sticky properties" but do not provide a mechanistic explanation for how a charge-changing mutation (E to K) reduces stickiness.
  - **Required correction** Add a brief discussion of the potential electrostatic effects of the E384K mutation on local interactions and how this might reduce protein-protein interactions.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** MD simulations
  - **Evidence pointer** Fig. 4A–I, SI Appendix Figs. S10–S12 (not provided)
  - **Issue** The MD simulations were performed on truncated peptides, and the force field and simulation length are not stated in the main text.
  - **Required correction** Specify the force field, water model, simulation time, and number of replicates in the Methods or SI. Justify the choice of truncated peptides.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Readability
  - **Affected element** Fig. 5I–J
  - **Evidence pointer** Fig. 5I–J
  - **Issue** The correlation between droplet ratio and hydrophobicity of the substituted residue is stated, but the hydrophobicity scale used is not defined.
  - **Required correction** Specify the hydrophobicity scale (e.g., Kyte-Doolittle, Eisenberg) and provide the numerical values used in the correlation analysis.

## Risk / unsupported claims
- The claim that the five-amino acid model "quantifies" sticker and spacer properties is not fully supported without validation of the model's predictive power on independent sequences or mutants.
- The claim that A381T induces "highly condensed pathogenic structures" is inferred from peptide crystal packing and is not directly demonstrated in the context of full-length TIA-1 or in cellular models.
- The claim that E384K suppresses droplet formation is presented as a definitive finding, but the discrepancy with prior work is not resolved.
- The relevance of the MD simulation results to the full-length protein is not established, as only short peptides were simulated.
- The statement that "the WT sequence has no self-assembling properties that lead to irreversible amyloid fibrils" is an overinterpretation based on a single peptide crystal structure.

## Assessment against Nature-style criteria
- **Originality** High. The five-amino acid model is a novel framework, and the cryo-EM crystal structures of disease-mutant peptides are a unique contribution.
- **Scientific importance** High. Understanding how disease mutations alter phase separation and aggregation in TIA-1 has broad implications for ALS/FTD and related disorders.
- **Interdisciplinary readership** Moderate to high. The work bridges biophysics, structural biology, and neurobiology, and will appeal to researchers in multiple fields.
- **Technical soundness** Moderate. The experimental design is generally sound, but the central quantitative model lacks rigorous validation, and the link between peptide structures and full-length protein behavior is not fully established.
- **Readability for nonspecialists** Moderate. The manuscript is clearly written, but the technical details of NMR relaxation analysis and the five-amino acid model may be challenging for readers outside the biophysics community.

## Recommendation posture
Supportive if technical concerns are resolved. The manuscript presents a potentially important advance, but the central quantitative model and the structural claims require additional validation and clarification. The authors should address the concerns regarding model overfitting, the relevance of peptide structures to full-length protein behavior, and the discrepancy with prior work on E384K.