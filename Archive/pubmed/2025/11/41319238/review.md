## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) without figures, tables, or supplementary material
- **Assessment boundary** Scientific validity, methodological soundness, and claims as presented in the provided text; no assessment of figures, tables, or supplementary data that were not supplied
- **Shared manuscript claim summary** The authors present MnM-W-MMGBSA, a modified MM-GBSA protocol that combines conformational sampling of individual protein partners via a "Mix-and-Match" (MnM) approach with inclusion of 30 interfacial water molecules, and report improved correlation with experimental binding free energies across 20 protein-protein interaction systems (r² from 0.47 to 0.70 with MnM sampling, up to 0.86 with water inclusion, and 0.89 after excluding an outlier)
- **Visible evidence base** Text descriptions of methods and results; correlation coefficients and specific values mentioned in text; references to figures and tables that were not provided
- **Missing materials affecting confidence** All figures, tables, and supplementary material; detailed numerical data for individual systems; computational details such as force field parameters, simulation lengths, and convergence criteria beyond what is stated; the duplicate run data; the per-residue decomposition results

## Reviewer

- **Overall assessment** The manuscript addresses a relevant problem in computational biophysics, namely improving MM-GBSA predictions for protein-protein interactions by addressing conformational sampling and interfacial water effects. The core idea of combining ensemble-based sampling of unbound partners with explicit water retention is physically motivated and potentially useful. However, the evidence as presented in the text is insufficient to fully evaluate the claims. Key quantitative results are described but not shown in the provided material, and several methodological details are ambiguous. The reported improvements in correlation are substantial and would be of interest if robustly demonstrated, but the current text alone does not allow verification of the statistical significance, the consistency across systems, or the generalizability of the approach.

- **Who would be interested in the results, and why** Computational biophysicists and medicinal chemists working on protein-protein interaction inhibitors, particularly those using end-point free energy methods for ranking peptide-based drug candidates. The methodological advance of incorporating explicit waters into MM-GBSA workflows and the automated pipeline for GROMACS-to-Amber conversion would be of practical interest to practitioners. The finding that excessive conformational sampling can be detrimental is conceptually important for the community.

- **Major Strengths**
  - The problem addressed is significant and timely, given the growing interest in PPI-targeting therapeutics
  - The methodological combination of ensemble sampling and explicit water inclusion is physically motivated and addresses known limitations of standard MM-GBSA
  - The use of a diverse benchmark set of 20 PPI systems with varying sizes and affinities is commendable
  - The practical contribution of an automated workflow overcoming gmx_MMPBSA limitations is valuable
  - The observation that excessive sampling can be detrimental is a non-obvious and potentially important insight

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that MnM-W-MMGBSA improves correlation with experimental binding affinities from 47% to 70% with MnM sampling alone, and up to 89% when interfacial water molecules are included
- **Evidence pointer** Results and Discussion sections; specific figures and tables referenced but not provided (Figure 3, Figure 4, Figure S3, Figure S9, Tables S2-S4)
- **Concern** The central quantitative claims of the paper are presented as correlation coefficients in the text, but the actual data plots, per-system values, and statistical analyses are not visible in the provided material. Without seeing the correlation plots, the distribution of errors across the 20 systems, and the confidence intervals for the reported r² values, it is impossible to assess whether the improvements are robust or driven by a few outliers. The text mentions one outlier (3SGB) whose exclusion improves correlation to 0.89, but the sensitivity of the results to other potential outliers is not discussed.
- **Why it matters** The entire premise of the paper rests on the demonstrated improvement in correlation. If the reported r² values are not accompanied by proper statistical evaluation, the reader cannot determine whether the improvement is significant or an artifact of the specific benchmark set.
- **Resolution test** Provide the actual correlation plots with per-system data points, report confidence intervals or p-values for the correlation coefficients, and show the sensitivity of results to individual systems.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological clarity
- **Claim pointer** The MnM method generates starting structures by integrating "the most representative conformers from molecular dynamics-derived ensembles of each unbound partner in explicit solvent using population-weighted clustering"
- **Evidence pointer** Methods section, subsection "Generating Representative Structures for Mix-and-Match (MnM) and Subsequent MD Simulations"
- **Concern** The description of the MnM procedure is insufficiently detailed. It is unclear how the "most representative conformers" are selected, how the population-weighted clustering is performed, how many conformers are combined, how the two chains are aligned and assembled into a complex, and how clashes are resolved. The choice of clustering cutoff (0.1 nm Cα RMSD) is stated, but the rationale and sensitivity to this parameter are not discussed. Additionally, the text states that MnM-Scheme-1 uses the first 12 ns of the unbound simulations while MnM-Scheme-2 uses the last 20 ns, but the reasoning for these specific time windows is not explained.
- **Why it matters** The MnM approach is the key innovation of the paper. Without a reproducible description of the method, other researchers cannot implement or validate it. The poor performance of MnM-Scheme-2 is attributed to "excessive conformational sampling," but this interpretation depends on the specific details of how the ensembles were generated and selected.
- **Resolution test** Provide a step-by-step algorithmic description of the MnM procedure, including the number of conformers selected, the alignment and assembly protocol, and the criteria for choosing the time windows. Include a sensitivity analysis of the clustering parameters.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation rigor
- **Claim pointer** The protocol is claimed to be "robust, computationally efficient, and applicable to a broad range of PPIs"
- **Evidence pointer** Results and Discussion sections; Conclusions
- **Concern** The validation is based on a single benchmark set of 20 PPI systems, and the text does not describe any cross-validation, train/test splits, or comparison against alternative methods beyond standard MM-GBSA. The claim of broad applicability is not supported by systematic variation of system properties such as interface size, flexibility, or the presence of intrinsically disordered regions. The text mentions one application to the AF9-BCOR complex with intrinsically disordered regions, but this appears to be from a previous study and is not described in detail here. The reproducibility assessment is limited to a single duplicate run, which is insufficient to establish robustness.
- **Why it matters** For a method to be adopted by the community, it must be shown to work consistently across diverse systems and to be robust to stochastic variations in MD simulations. The current evidence is too limited to support the broad claims made.
- **Resolution test** Provide additional validation on independent benchmark sets, report the variability of results across multiple independent runs, and discuss the range of system properties for which the method is expected to work.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Comparison with alternatives
- **Claim pointer** The manuscript implies that MnM-W-MMGBSA is superior to standard MM-GBSA and addresses limitations of existing approaches
- **Evidence pointer** Introduction; Results and Discussion
- **Concern** The comparison is made only against standard MM-GBSA starting from crystal structures. No comparison is made against other enhanced sampling approaches, such as replica exchange MD, metadynamics, or other end-point methods like MMPBSA with different solvation models. The text mentions that NME and REMD are too expensive, but no quantitative comparison of computational cost is provided. The relationship to the work of Contini and Maffucci, which is cited as the inspiration for the water inclusion strategy, is described but not critically compared.
- **Why it matters** To establish the value of the proposed method, it is necessary to demonstrate its advantages over existing alternatives, both in terms of accuracy and computational cost. Without such comparisons, the incremental contribution of the method is unclear.
- **Resolution test** Include benchmark comparisons against at least one alternative enhanced sampling or water-inclusive method, and report computational costs for all methods.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of writing
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that correlation improves "from 47% to 70% with MnM sampling alone for standard MM-GBSA, and up to 89% when interfacial water molecules are included." The phrasing "for standard MM-GBSA" is ambiguous, as it could be read as the improvement being for standard MM-GBSA rather than for the modified protocol.
- **Required correction** Rephrase to clarify that the 47% is the baseline for standard MM-GBSA from crystal structures, and the 70% and 89% are for the MnM-based approaches.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Methods, MM-GBSA calculations
- **Evidence pointer** Methods section, subsection "Performing MM-GBSA Calculations"
- **Issue** The text states that 100 evenly spaced frames were extracted for MM-GBSA calculations, but it is not clear whether these frames are from a single trajectory or from multiple independent runs. The choice of 100 frames and the spacing criteria are not justified.
- **Required correction** Specify the number of independent simulations, the total simulation time, and the rationale for the frame selection.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results and Discussion
- **Evidence pointer** Results and Discussion, sections on correlation improvements
- **Issue** The text reports r² values but does not report the corresponding p-values, confidence intervals, or the number of degrees of freedom. For a benchmark of 20 systems, the statistical significance of the difference between r² = 0.47 and r² = 0.70 should be assessed.
- **Required correction** Report p-values or confidence intervals for the correlation coefficients and for the differences between methods.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** Title; Abstract; Introduction
- **Issue** The term "relative binding free energies" is used, but the manuscript appears to compare computed binding free energies against experimental values, which is more accurately described as "absolute binding free energy prediction" or "binding affinity prediction." The distinction between relative and absolute predictions should be clarified.
- **Required correction** Clarify whether the method predicts relative or absolute binding free energies, and adjust terminology accordingly.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness of reporting
- **Affected element** Methods, Structure Preparation
- **Evidence pointer** Methods, subsection "Structure Preparation"
- **Issue** The text states that missing residues were predicted with AlphaFold for three PDB IDs, but it does not specify the version of AlphaFold, the confidence of the predictions, or how the predicted structures were validated.
- **Required correction** Provide details on the AlphaFold version, prediction confidence scores, and any validation performed.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: The central quantitative claims cannot be verified from the provided text alone; the actual data must be shown and statistically analyzed
  - R1-M2: The MnM procedure is not described in sufficient detail to be reproducible
  - R1-M3: The validation is too limited to support the broad claims of robustness and applicability

- **Assessment against Nature-style criteria**
  - **Originality** The combination of ensemble-based conformational sampling with explicit water inclusion in MM-GBSA is a novel methodological contribution, though it builds on prior work by Contini and Maffucci. The specific MnM approach appears to be original.
  - **Scientific importance** The problem of accurate binding free energy prediction for PPIs is of high importance in drug discovery. If the method is robustly validated, it could have practical impact. However, the importance is somewhat limited by the incremental nature of the improvement over existing MM-GBSA approaches.
  - **Interdisciplinary readership** The work is primarily of interest to computational chemists and biophysicists. The potential application to drug discovery may attract medicinal chemists, but the technical nature of the manuscript limits its broader appeal.
  - **Technical soundness** The methodological approach is physically reasonable, but the technical soundness cannot be fully assessed from the provided text due to missing details and data. The lack of statistical rigor in reporting correlation improvements is a concern.
  - **Readability for nonspecialists** The manuscript is written in a technical style that assumes familiarity with MD simulations and MM-GBSA. The abstract is accessible, but the methods and results sections would be challenging for nonspecialists.

- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the reported improvements are potentially significant, but the current evidence is insufficient to establish the case. The authors must provide the actual data, statistical analysis, and sufficient methodological detail for the claims to be evaluated. If these concerns are addressed, the manuscript could make a valuable contribution to the field.