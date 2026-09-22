## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Technical soundness, methodological validity, and claims as presented in the provided manuscript
- **Shared manuscript claim summary** The authors present the Analytical Flory Random Coil (AFRC), a sequence-based analytical polymer model for unfolded and disordered proteins, parameterized from all-atom ideal-chain simulations. The AFRC requires only amino acid sequence as input and provides distributions of end-to-end distance, radius of gyration, inter-residue distances, and contact frequencies. The authors validate the model against numerical simulations and compare it with existing polymer models, all-atom simulations, and a curated set of SAXS-derived radii of gyration.
- **Visible evidence base** Main text, figures referenced (Fig. 1-9), supplementary figure references (Fig. S1-S6), supplementary table reference (Table S1)
- **Missing materials affecting confidence** Supplementary figures and tables are referenced but not provided; specific numerical values for model parameters, fitting procedures, and statistical analyses are not fully detailed; the curated SAXS dataset (145 entries) is not provided as a table or list

## Reviewer

- **Overall assessment** The manuscript presents a conceptually useful and practically accessible reference model for unfolded and disordered proteins. The methodological approach is sound in principle, and the validation against numerical simulations is convincing. However, the manuscript's impact is limited by the absence of key supplementary materials, incomplete reporting of model parameters and fitting procedures, and a somewhat overstated claim regarding the model's utility as a "reference state" given the demonstrated variability in experimental comparisons. The work is likely to be of interest to the biophysics and disordered protein communities, but the current evidence base is insufficient to fully establish all claims.

- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins and unfolded states, particularly those using small-angle X-ray scattering, single-molecule Förster resonance energy transfer, or all-atom simulations. The AFRC provides a simple, sequence-based null model that could be widely adopted for normalizing experimental or simulation data. The Google Colab implementation lowers the barrier for non-specialists. The work may also interest polymer physicists applying scaling theories to biological heteropolymers.

- **Major strengths** 
  1. The AFRC is genuinely simple to use, requiring only sequence input, which addresses a practical need in the field.
  2. The validation against numerical simulations is thorough, with high correlation coefficients and low RMSE values reported.
  3. The comparison with existing polymer models is fair and appropriately framed, emphasizing compatibility rather than superiority.
  4. The application to SAXS data, despite limitations, demonstrates a clear use case and provides a useful benchmark for the community.
  5. The software implementation and Colab notebook are commendable for accessibility and reproducibility.

- **Major Concerns**

  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that the AFRC "faithfully reproduces homo- and hetero-polymeric dimensions for polypeptides under the FRC assumptions" based on comparisons with numerical simulations.
  - **Evidence pointer** Methods section, Fig. 3, Fig. S3, Fig. S4
  - **Concern** The validation against numerical simulations is presented as strong evidence for the AFRC's accuracy. However, the manuscript does not provide sufficient detail on the fitting procedure for the prefactor A0 and the normalization factor X0. Specifically, it is unclear whether these parameters were fit to the same simulation data used for validation, which would constitute circular reasoning. The authors state that A0 was "parameterized by fitting internal scaling profiles" and X0 was "fit numerically-generated P(Rg) distributions," but the exact fitting methodology, including the number of data points, the range of chain lengths, and the error metrics used for fitting, is not reported. Without this information, the reported correlation coefficients and RMSE values cannot be independently assessed.
  - **Why it matters** If the model parameters are fit to the same data used for validation, the reported agreement is expected and does not demonstrate predictive power. The claim of "faithful reproduction" requires validation on independent data or a clear description of the fitting-validation split.
  - **Resolution test** Provide a detailed description of the fitting procedure, including the training and test set separation, or validate the AFRC on an independent set of sequences not used in parameterization.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors state that "the AFRC offers an analytic approach for calculating sequence-specific ensemble properties for unfolded homopolymers" and later generalize to heteropolymers.
  - **Evidence pointer** Methods section, Fig. 3, Supplementary Table 1
  - **Concern** The generalization from homopolymers to heteropolymers is based on the assumption that the prefactor for a heteropolymer is a weighted average of homopolymer prefactors. While this is a reasonable assumption for ideal chains, the manuscript does not provide a theoretical justification or empirical test of this assumption beyond the comparison shown in Fig. 3. The authors report an average RMSE of 0.5 Å across 320 sequences, but the range of sequence compositions tested is not described. It is unclear whether the model performs equally well for sequences with extreme compositions (e.g., highly charged, highly hydrophobic, or proline-rich) or only for the "average" sequences tested.
  - **Why it matters** If the weighted-average assumption fails for certain sequence classes, the AFRC would not be a universally applicable reference model, limiting its utility. The claim of general applicability requires demonstration across a diverse sequence space.
  - **Resolution test** Provide a detailed description of the 320 test sequences, including their composition ranges, and show that the AFRC performs well across the full range, or identify limitations for specific sequence classes.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The authors suggest that the AFRC provides "a convenient, analytical approach to obtain a well-defined reference state for comparing and contrasting simulations and experiments of unfolded and disordered proteins."
  - **Evidence pointer** Fig. 8, Discussion
  - **Concern** The comparison with SAXS-derived radii of gyration shows a correlation coefficient of 0.91 and an RMSE of 6.4 Å, but the authors also note that the majority of experimental values are above the AFRC prediction, with some exceeding the denatured-state model. This suggests that the AFRC systematically underestimates dimensions for many proteins. The authors acknowledge this and propose an empirical upper bound of 1.45 times the AFRC value, but this post-hoc adjustment undermines the claim that the AFRC is a useful reference state. If the model requires empirical scaling factors to match experimental data, its utility as a "parameter-free" reference is questionable.
  - **Why it matters** The central value proposition of the AFRC is its simplicity and lack of user-defined parameters. If users must apply empirical corrections to compare with experimental data, the model's advantage over existing approaches is diminished.
  - **Resolution test** Provide a more detailed analysis of the discrepancies between AFRC predictions and experimental data, including a discussion of whether the systematic offset reflects a fundamental limitation of the ideal-chain assumption or specific experimental conditions.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** The authors state that "the AFRC behaves as a truly ideal chain" and that "end-effects that emerge finite-chain effects are not experienced in terms of end effects."
  - **Evidence pointer** Fig. 1E, Fig. S2
  - **Concern** The claim that the FRC simulations are free of end-effects is based on a comparison of internal scaling profiles. However, the manuscript does not provide a quantitative analysis of how end-effects are assessed or what threshold was used to determine their absence. For short chains (e.g., 10 residues), end-effects are expected to be significant, and the manuscript does not address whether the AFRC remains accurate for very short peptides.
  - **Why it matters** If the AFRC is intended for use across a wide range of chain lengths, including short peptides, the absence of end-effects must be demonstrated quantitatively. Otherwise, users may apply the model outside its valid range.
  - **Resolution test** Provide a quantitative analysis of end-effects as a function of chain length, including a minimum chain length for which the AFRC is valid.

- **Minor Comments**

  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Introduction
  - **Evidence pointer** Introduction, first paragraph
  - **Issue** The introduction assumes familiarity with polymer physics terminology (e.g., "scaling laws," "theta solvent," "Flory exponent") without defining these terms for a broader readership. Given the stated goal of making the model accessible to non-specialists, a brief explanation of these concepts would improve readability.
  - **Required correction** Add a short paragraph defining key polymer physics terms and their relevance to protein biophysics.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Methods, equation numbering
  - **Evidence pointer** Methods section, equations 1-8
  - **Issue** Equation 8 is used twice with different meanings. In the context of equations 5-7, equation 8 defines the relationship between x and r. Later, in the section on heteropolymer generalization, equation 8 is referenced again but appears to refer to a different relationship. This is confusing.
  - **Required correction** Renumber equations sequentially and ensure each equation is referenced uniquely.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Scientific importance
  - **Affected element** Discussion, comparison with SAXS data
  - **Evidence pointer** Fig. 8, Discussion
  - **Issue** The authors note that the AFRC outperforms several established coarse-grained models in correlating with experimental Rg values, but they do not provide a direct comparison or cite the specific models. This claim is difficult to evaluate without additional context.
  - **Required correction** Provide a direct comparison with at least one or two established models, including the relevant references and correlation coefficients.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Methods, Monte Carlo simulation description
  - **Evidence pointer** Methods section, "Implementation of a numerical model"
  - **Issue** The description of the Monte Carlo approach is brief and assumes familiarity with the CAMPARI software and the ABSINTH-OPLS forcefield. A brief description of these tools and why they were chosen would help readers who are not simulation specialists.
  - **Required correction** Add a sentence or two describing CAMPARI and ABSINTH-OPLS and their relevance to the study.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Methods, hydrodynamic radius calculation
  - **Evidence pointer** Methods section, "Constructing an analytical description"
  - **Issue** The manuscript mentions that the AFRC can calculate the hydrodynamic radius using either the Kirkwood-Riseman equation or an empirical relationship, but the details of these calculations are not provided. It is unclear which approach is implemented in the software and how the two compare.
  - **Required correction** Provide details on the hydrodynamic radius calculation, including the specific equations used and any validation against simulation or experimental data.

- **Technical failings that need to be addressed before the case is established**
  1. R1-M1: Lack of detail on fitting-validation split for model parameters.
  2. R1-M2: Insufficient description of the sequence space used for heteropolymer validation.
  3. R1-M4: No quantitative assessment of end-effects as a function of chain length.

- **Assessment against Nature-style criteria**
  - **Originality** The AFRC is not conceptually novel, as it builds on established polymer physics and existing ideal-chain models. However, the specific parameterization from all-atom simulations and the user-friendly implementation provide a practical contribution. The originality is moderate.
  - **Scientific importance** The model addresses a real need for a simple, sequence-based reference state in the disordered protein field. The demonstrated correlation with experimental SAXS data, despite limitations, suggests broad applicability. The importance is moderate to high.
  - **Interdisciplinary readership** The work bridges polymer physics, biophysics, and computational biology. The Colab notebook and Python package make it accessible to a wide audience. The interdisciplinary appeal is moderate.
  - **Technical soundness** The core methodology is sound, but the lack of detail on fitting procedures and validation limits the current evidence base. The technical soundness is moderate, with specific concerns that need addressing.
  - **Readability for nonspecialists** The manuscript is generally well-written but assumes familiarity with polymer physics and simulation methods. The readability for nonspecialists is moderate, with room for improvement.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a useful and practical tool, but the current evidence base is insufficient to fully establish the model's validity and general applicability. Addressing the major concerns, particularly the fitting-validation details and the sequence space coverage, would significantly strengthen the case.