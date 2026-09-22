## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) without figures, tables, or supplementary material
- **Assessment boundary** Scientific claims, methodological soundness, and evidence consistency based solely on the provided text; figures and supplementary data referenced but not directly assessable
- **Shared manuscript claim summary** The authors claim that protein backbone 15N spin relaxation times correlate with backbone rigidity in short disordered linkers, demonstrated by combining NMR experiments with MD simulations via a tailored QEBSS framework, and that proline content increases rigidity while ion binding has minimal effects.
- **Visible evidence base** Text descriptions of NMR relaxation measurements (T1, T2, hetNOE), MD simulation protocols, QEBSS selection criteria, and qualitative references to figures (Figs. 1–3, S1–S49) and tables (Table 1, S1)
- **Missing materials affecting confidence** All figures, tables, supplementary data, and simulation trajectory files; no quantitative data values, error magnitudes, or statistical analyses are provided in the text

## Reviewer

- **Overall assessment** The manuscript addresses a relevant and timely question in the biophysics of disordered proteins, namely the quantitative characterization of backbone rigidity in short linkers. The combination of NMR spin relaxation with MD simulations through the QEBSS framework is a sensible and potentially valuable approach. However, the provided text alone does not contain sufficient quantitative evidence to fully evaluate the central claims. The correlation between spin relaxation times and backbone rigidity is asserted rather than demonstrated with explicit numerical data, and the manual selection of simulations raises concerns about objectivity and reproducibility. The ion-binding results are presented as preliminary, which is appropriate, but the claim that electrostatics do not dominate linker stiffness requires stronger support. The manuscript is clearly written and the methodological logic is sound, but the evidence base as presented is incomplete for a definitive assessment.

- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, protein biophysics, and computational chemistry would find these results relevant. The work provides a framework for combining NMR and MD data to extract backbone rigidity parameters, which is of direct interest to those studying disordered linkers in multidomain proteins. Additionally, the force field evaluation component is relevant to the molecular simulation community, and the potential applications in protein engineering and machine learning model development broaden the appeal to biotechnology and computational biology audiences.

- **Major Strengths**
  - The study addresses a genuine gap in the field, as quantitative experimental methods for characterizing disordered linker rigidity are indeed limited.
  - The combination of NMR spin relaxation with MD simulations via QEBSS is a thoughtful and potentially powerful approach that leverages complementary information.
  - The inclusion of multiple model peptides representing different sequence classes (glycine-rich, proline-containing, charged) is a good design choice.
  - The authors acknowledge limitations, such as the nonexponential decay of orientational correlation functions and the preliminary nature of ion-binding results.
  - The work has clear practical implications for protein engineering and force field development.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The central claim that "protein backbone 15N spin relaxation times correlate with backbone rigidities in short, disordered linkers" is the foundation of the paper.
- **Evidence pointer** Fig. 1b, 1c, 1e; location not provided for quantitative values
- **Concern** The text asserts a correlation between spin relaxation times and backbone rigidity but does not provide any quantitative measure of this correlation. No correlation coefficients, statistical significance values, or quantitative comparisons between experimental and simulated values are given in the text. The qualitative statement that trends "follow the same order" is insufficient to establish a robust correlation, especially given the small number of labeled residues per peptide.
- **Why it matters** The central claim of the paper rests on this correlation. Without quantitative evidence, the reader cannot assess the strength or reliability of the relationship, and the claim remains an assertion rather than a demonstrated finding.
- **Resolution test** Provide explicit correlation coefficients or statistical tests between experimental spin relaxation times and simulated backbone rigidity parameters across all residues and peptides. Alternatively, provide quantitative comparisons showing that differences between peptides in spin relaxation times are mirrored by corresponding differences in rigidity parameters with associated uncertainties.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological objectivity
- **Claim pointer** The manual selection of simulations "that are in best overall agreement with experimental spin relaxation rates" is described for each peptide.
- **Evidence pointer** Section "Ranking of simulations and selection of best ensembles"; location not provided
- **Concern** The selection of simulations is described as manual, with criteria that are not fully specified. The text states that simulations were selected "mainly due to their best performance" for certain parameters, but the decision process is not transparent. This introduces potential confirmation bias, as the selection is made with knowledge of the experimental results.
- **Why it matters** The QEBSS framework is presented as a method for objective ensemble selection, but manual selection undermines this objectivity. If the selection criteria are not clearly defined and reproducible, the resulting ensembles and derived conclusions cannot be independently verified.
- **Resolution test** Define explicit, quantitative selection criteria that could be applied algorithmically. Ideally, implement an automated selection procedure and demonstrate that it reproduces the manually selected ensembles. At minimum, provide a clear decision tree or scoring function that justifies each selection.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Claim support
- **Claim pointer** The claim that "sodium and calcium binding to charged peptides minimally affected rigidity, indicating electrostatics don't dominate linker stiffness" is presented as a key finding.
- **Evidence pointer** Fig. 3b, 3c, 3d; location not provided
- **Concern** The text reports that ion-induced changes in spin relaxation times are "neither systematic nor substantial" and that the force fields predicting stronger calcium binding "slightly overestimate" the experimental differences. However, the authors also note that the changes are "not fully systematic" and call for "more systematic experimental data." This suggests the evidence is not yet conclusive, yet the claim is stated fairly strongly.
- **Why it matters** The conclusion about electrostatics is relevant to understanding the physical determinants of linker rigidity. If the evidence is preliminary, the claim should be tempered accordingly, as it may mislead readers into overinterpreting the role of electrostatics.
- **Resolution test** Either strengthen the evidence by providing more systematic data across multiple ion concentrations with clear statistical analysis, or soften the claim to reflect the preliminary nature of the findings. The claim should be directly supported by the data presented.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretive validity
- **Claim pointer** The authors state that "backbone rigidity approximated by lp values" is derived from fitting the orientational correlation function to an exponential, while acknowledging the function "does not follow clear exponential behavior."
- **Evidence pointer** Section "Molecular dynamics simulations reveal a correlation between backbone rigidity and spin relaxation times"; Fig. 1e; location not provided
- **Concern** The use of persistence length as a rigidity measure is problematic when the correlation function is nonexponential. The authors acknowledge this but still present lp values as quantitative measures. The text does not explain how the fit is performed, what range of s is used, or how reliable the resulting lp values are given the poor fit.
- **Why it matters** Persistence length is a standard and interpretable measure of polymer rigidity, but its validity depends on the exponential decay assumption. If the correlation functions deviate significantly from exponential behavior, the derived lp values may be misleading or not directly comparable across peptides.
- **Resolution test** Provide a more detailed analysis of the fitting procedure, including the range of s used, goodness-of-fit metrics, and a discussion of how the nonexponential behavior affects the interpretation of lp. Consider alternative rigidity measures that do not rely on the exponential assumption.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Peak assignment for (GGS)3
- **Evidence pointer** Section "Peak assignment"; location not provided
- **Issue** The text states that glycines 4,5 and 7,8 were assigned to peaks "in very close vicinity" and that the final assignment was selected "to provide optimal agreement with spin relaxation times from MD simulations." This is circular reasoning, as the assignment is chosen to match the simulations that are then evaluated against the experiments.
- **Required correction** Clarify whether the assignment was made independently of the simulation results, or acknowledge that the assignment choice could bias the subsequent comparison. If possible, provide evidence that alternative assignments do not affect the conclusions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Force field ranking
- **Evidence pointer** Section "Force field evaluation reveals varying performance across peptide sequences"; Fig. 2; location not provided
- **Concern** The text states that AMBER99SB-DISP is the best performing force field for (GGS)3 and (GPS)3, but the ranking is described as "less straightforward" for other peptides. The basis for the ranking is not fully explained, and the text does not provide quantitative metrics for the comparison.
- **Required correction** Provide a clear description of the ranking criteria, including which spin relaxation parameters were weighted most heavily and how the ranking was determined. Consider presenting a summary table of ranking scores.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Simulation selection
- **Evidence pointer** Section "Ranking of simulations and selection of best ensembles"; location not provided
- **Issue** The text mentions that four points with largest RMSD values were excluded to mitigate outlier effects, but the rationale for excluding exactly four points is not explained.
- **Required correction** Justify the choice of excluding four points, or state that this is an arbitrary choice. Consider performing a sensitivity analysis to show that the conclusions are robust to the number of excluded points.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Comparison with literature
- **Evidence pointer** Section "Molecular dynamics simulations reveal a correlation between backbone rigidity and spin relaxation times"; location not provided
- **Issue** The text states that the range of persistence lengths (0.4–2.7 nm) spans previously reported values (0.3–2.6 nm), but it does not discuss whether the differences between peptides are meaningful given the uncertainties in the measurements.
- **Required correction** Provide uncertainty estimates for the lp values and discuss whether the differences between peptides are statistically significant.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Lack of quantitative correlation metrics between spin relaxation times and rigidity parameters
  - R1-M2: Manual simulation selection without transparent, reproducible criteria
  - R1-M4: Use of persistence length despite acknowledged nonexponential correlation functions, without adequate justification or alternative measures

- **Assessment against Nature-style criteria**
  - **Originality** The approach of combining NMR spin relaxation with MD simulations via QEBSS to characterize linker rigidity is not entirely novel, as the QEBSS framework has been previously published. However, its application to short disordered linkers and the systematic comparison of force fields for this specific purpose has some originality. The finding that electrostatics minimally affect rigidity is potentially interesting but not fully established.
  - **Scientific importance** The work addresses a relevant problem in disordered protein biophysics and has potential implications for protein engineering. However, the importance is moderate, as the findings are largely confirmatory of known trends (proline rigidifies linkers) and the methodological advance is incremental.
  - **Interdisciplinary readership** The work is likely to appeal primarily to biophysicists and computational chemists specializing in disordered proteins. The broader interdisciplinary appeal is limited, as the methods and findings are quite specialized.
  - **Technical soundness** The methodological framework is sound in principle, but the manual selection of simulations and the lack of quantitative evidence for the central correlation claim are significant weaknesses. The technical execution cannot be fully assessed without the figures and supplementary data.
  - **Readability for nonspecialists** The manuscript is clearly written and the logic is easy to follow. However, the heavy reliance on specialized terminology (e.g., spin relaxation, persistence length, QEBSS) without sufficient background may limit accessibility for nonspecialists. The abstract and significance statement are reasonably accessible.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses a relevant question with a sensible approach, but the central claim of a correlation between spin relaxation times and backbone rigidity requires quantitative support. The manual simulation selection must be made more objective and reproducible. The ion-binding conclusions should be tempered or strengthened with additional data. If these issues are addressed, the work could make a useful contribution to the field.

## Risk / unsupported claims
- The claim that "protein backbone 15N spin relaxation times correlate with backbone rigidities" is not quantitatively supported in the provided text; no correlation coefficients or statistical tests are given.
- The claim that "electrostatics don't dominate linker stiffness" is based on preliminary data that the authors themselves acknowledge are not fully systematic.
- The statement that the QEBSS-selected ensembles "reproduce the experimentally observed spin relaxation time differences between sequences" is asserted but not demonstrated with numerical comparisons.
- The claim that the approach "provides quantitative persistence lengths describing the backbone rigidity" is weakened by the acknowledged nonexponential behavior of the correlation functions, which undermines the validity of the persistence length as a quantitative measure.
- The force field ranking for peptides other than (GGS)3 is described as "less straightforward," yet the text still draws conclusions about force field performance that are not fully supported.