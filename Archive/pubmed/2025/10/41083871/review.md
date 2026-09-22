## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) as provided.
- **Assessment boundary** Scientific content, methodological validity, and support for claims based solely on the provided text. No external data, figures, or supplementary materials were available for direct inspection.
- **Shared manuscript claim summary** The authors propose a polymer physics-based model (FH-RPA) that predicts the partitioning of intrinsically disordered regions (IDRs) into condensates formed by the MED1 IDR. They claim the model, based solely on electrostatic interactions, largely explains previously published experimental data on selective partitioning, and that new predictions were experimentally validated. They further claim this demonstrates that specificity of condensate composition can emerge from multivalent interactions among disordered regions without requiring ordered structure.
- **Visible evidence base** Text descriptions of Figures 1-4, tables S1-S2, and supplementary notes. Statistical methods and results are described in text. No raw data, full figure panels, or supplementary files were available.
- **Missing materials affecting confidence** All figures, tables, and supplementary materials. Detailed model derivations in Supplementary Methods. Full experimental protocols and raw imaging data. Code repository contents.

## Reviewer
- **Overall assessment** This manuscript presents a potentially valuable theoretical framework for predicting IDR partitioning into condensates. The core idea, that a relatively simple electrostatic model can capture much of the specificity of client partitioning into MED1 condensates, is interesting and timely. The combination of theory with experimental validation is a strength. However, the manuscript as presented has significant gaps in methodological detail, statistical rigor, and clarity of model assumptions that prevent full evaluation. The central claim that specificity "can emerge" from multivalent interactions is supported, but the quantitative strength of the claim ("largely explain") is not fully established from the provided evidence. The work is likely of interest to the condensate and IDP communities, but requires substantial revision to meet the standards of a high-impact journal.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, particularly those focused on the molecular mechanisms of condensate composition and specificity. The IDP community, especially those working on sequence-function relationships in disordered regions, will find the model and its predictive power relevant. The work also speaks to the broader question of how specificity can arise without ordered structures, which is of interest to structural biologists and biophysicists. The computational efficiency of the method may appeal to those interested in proteome-wide screening approaches.

- **Major strengths**
    1. The manuscript addresses a significant and unresolved question: whether condensate specificity can be explained by statistical multivalent interactions rather than ordered structure.
    2. The FH-RPA model is computationally efficient, allowing for high-throughput screening, which is a practical advantage over more expensive simulation methods.
    3. The combination of retrospective validation on published data and prospective prediction with experimental testing is a strong study design.
    4. The identification of aromatic residues as a source of discrepancy between model and experiment is a useful insight that points toward model improvement.
    5. The writing is generally clear and the logical flow from rationale to model to validation to prediction is easy to follow.

- **Major Concerns**

    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The claim that the FH-RPA model "largely explain[s] published data on selective partitioning" is based on correlation coefficients (r ≈ 0.67 for RPA vs r ≈ 0.35 for MFT) between predicted and experimental partition coefficients.
    - **Evidence pointer** Results section "FH-RPA model rationalizes effects of charge scrambling and other sequence charge pattern variations on IDR PCs", Figures 2B, 2C, and text describing Figure S4.
    - **Concern** The improvement in correlation from 0.35 to 0.67 is presented as strong support, but the manuscript does not report confidence intervals, p-values for the difference, or any measure of predictive error (e.g., root mean square error). A correlation of 0.67, while better than 0.35, still leaves substantial unexplained variance. The claim of "largely explain" is too strong for this level of correlation. The authors should provide a more nuanced interpretation, report error metrics, and discuss what fraction of variance remains unexplained. Additionally, the model is fit to the data (parameters c1, c2, lB, κ, a are optimized), so the reported correlation is an in-sample fit, not a predictive validation. The out-of-sample predictive power is only tested on the new predictions (Figure 4), but the success rate there is 4/4 for high-PC and 4/7 for low-PC, which is mixed.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The model is described as accounting for "multivalent interactions among polymers in a statistical manner" and the Methods state that "we consider only electrostatic contributions" to the Flory-Huggins parameter.
    - **Evidence pointer** Methods section "A general screened electrostatic potential and the FH-RPA formulation", Equations 1-9.
    - **Concern** The model as described in the main text appears to consider only electrostatic interactions. However, the authors later invoke aromatic residues and cation-π interactions to explain discrepancies. This is a conceptual inconsistency. If the model is purely electrostatic, then the claim that it "largely explains" specificity is undermined by the need to invoke non-electrostatic effects for 3 of 7 low-PC predictions. The authors should clarify whether the model is intended to be purely electrostatic or if it implicitly captures other interactions. If purely electrostatic, the limitations should be stated more prominently. If not, the model description needs to be revised to include all interaction terms.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The sliding-sequence analysis is proposed as an approximation to full configurational sampling, with the claim that it "covers multiple scenarios of inter-chain interactions among sequentially local residues."
    - **Evidence pointer** Results section "Rationale", Figure 1A, 1B.
    - **Concern** The validity of the sliding-sequence approximation is not rigorously tested. The manuscript does not compare the sliding-sequence results to full configurational sampling (e.g., molecular dynamics or Monte Carlo) for any test case. The choice of inter-chain distance (2-3b) is described as "to some extent arbitrary" and "tentative." This is a significant weakness. The authors should validate the approximation against a more rigorous method for at least a few cases, or provide a theoretical justification for why the sliding-sequence approach captures the essential physics. Without this, the quantitative predictions of the model are on shaky ground.

    - **Concern ID** R1-M4
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific importance
    - **Claim pointer** The authors claim the model can be used to "scan libraries of protein sequences" and identify regions with high or low partitioning.
    - **Evidence pointer** Results section "FH-RPA model successfully predicts low-PC and high-PC IDR windows", Figure 4A.
    - **Concern** The proteome scan is limited to a small set of 11 selected regions (4 high, 7 low) from a filtered set of 865 IDRs. The selection criteria for these 11 regions are not described. How were they chosen from the 865? This is a potential source of selection bias. The authors should describe the selection process transparently. Additionally, the scan is limited to transcription-related proteins; the generalizability to other functional classes is untested.

    - **Concern ID** R1-M5
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical soundness
    - **Claim pointer** The experimental validation of new predictions relies on a cell-based assay measuring fluorescence partitioning into MED1 condensates.
    - **Evidence pointer** Methods sections "Cell culture", "Processing coverslips of co-transfected cells", "Microscopy", "Microscopy analysis", Figures 3I, 3J, 3L, 3M, 4E, 4F, 4H, 4I, 4K, 4L.
    - **Concern** The experimental method is described briefly and references prior work. The manuscript does not report the variability of the measurements (e.g., standard deviations, number of cells, number of independent experiments) in the main text. The statistical tests are mentioned but the results are not fully reported. For example, for Figure 4F, the text states "significant enrichment" but does not provide the test statistic or effect size. The authors should provide a more complete description of the experimental methods and results to allow assessment of robustness.

- **Minor Comments**

    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability for nonspecialists
    - **Affected element** Introduction and Results section "Rationale"
    - **Evidence pointer** Text describing Figure 1.
    - **Issue** The description of the sliding-sequence analysis and the FH-RPA model is dense and may be difficult for a non-specialist to follow. The physical intuition behind the model could be explained more clearly.
    - **Required correction** Consider adding a more accessible explanation of the model, perhaps with a simple analogy or a step-by-step description of the logic.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Results section "FH-RPA model can be improved by including non-electrostatic effects"
    - **Evidence pointer** Figure 4M.
    - **Issue** The comparison of electrostatic-only vs. electrostatic + non-electrostatic (Mpipi) energies is qualitative. The figure shows shifts in energy, but the magnitude of the shift and its relationship to the experimental partition coefficients is not quantified.
    - **Required correction** Provide a quantitative comparison, such as a correlation between the corrected energies and the experimental partition coefficients.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Scientific importance
    - **Affected element** Discussion
    - **Evidence pointer** Discussion section.
    - **Issue** The discussion of the evolutionary conservation of PC profiles is interesting but brief. The authors could expand on the implications of this finding for the evolution of condensate function.
    - **Required correction** Consider adding a paragraph discussing the potential evolutionary implications of conserved PC profiles in more detail.

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Methods section "Calculating PC profiles"
    - **Evidence pointer** Equation 10.
    - **Issue** The definition of the PC profile similarity score is given, but the properties of this score are not discussed. For example, how does it behave for random sequences? What is the range of values?
    - **Required correction** Provide a brief discussion of the properties and limitations of the similarity score.

- **Technical failings that need to be addressed before the case is established**
    - R1-M1: Lack of error metrics and out-of-sample validation for the correlation between predicted and experimental partition coefficients.
    - R1-M2: Inconsistency between the stated scope of the model (electrostatic only) and the need to invoke non-electrostatic effects to explain discrepancies.
    - R1-M3: Lack of validation of the sliding-sequence approximation against more rigorous methods.

- **Assessment against Nature-style criteria**
    - **Originality** The work is original in its specific combination of Flory-Huggins theory with RPA for predicting client partitioning into a specific condensate. The idea that statistical multivalent interactions can provide specificity is not entirely new, but the specific model and its application to MED1 condensates is a novel contribution.
    - **Scientific importance** The question of how condensate composition is determined is of high importance to the field. A predictive, computationally efficient model would be a valuable tool. However, the importance is somewhat tempered by the model's limitations (electrostatic focus, need for empirical fitting) and the mixed predictive success.
    - **Interdisciplinary readership** The work bridges polymer physics, molecular biology, and cell biology. It should be of interest to researchers in all three areas. The writing is accessible, though the model details are complex.
    - **Technical soundness** The technical soundness is currently not fully established. The main issues are the lack of validation of the key approximation (sliding-sequence), the in-sample nature of the correlation, and the incomplete reporting of experimental variability.
    - **Readability for nonspecialists** The abstract and introduction are clear. The results and methods sections are dense but generally readable. The main concepts are explained, though the model details require effort to follow.

- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the combination of theory and experiment is appropriate. However, the manuscript in its current form does not fully establish the quantitative claims. The authors must address the validation of the sliding-sequence approximation, provide more rigorous statistical analysis of the model's predictive power, and clarify the role of non-electrostatic interactions. If these issues are resolved, the work could be a valuable contribution.

## Risk / unsupported claims
- The claim that the model "largely explain[s]" published data is not fully supported given the moderate correlation (r ≈ 0.67) and the lack of error metrics.
- The claim that the sliding-sequence analysis is a valid approximation is not supported by any direct comparison to more rigorous methods.
- The claim that the model can be used for high-throughput screening is supported by the computational efficiency, but the practical utility is not demonstrated beyond the small set of 11 tested regions.
- The generalizability of the model to condensates with scaffolds other than MED1 is explicitly not addressed and is stated as a limitation.
- The role of aromatic residues and cation-π interactions is inferred from sequence composition and a single model (Mpipi), but not directly tested experimentally (e.g., by mutating aromatic residues in the context of the model's predictions, which was done, but the model's predictions for these mutants are not shown to be improved by the Mpipi correction in a quantitative way).