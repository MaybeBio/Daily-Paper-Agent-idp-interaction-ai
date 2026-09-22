## Review setup
- **Input scope** Full manuscript text (abstract, introduction, experimental methods, results and discussion, conclusions) as provided by the user. No figures, tables, or supplementary material were included in the supplied text.
- **Assessment boundary** The review is limited to the scientific content, methodology, and claims as presented in the supplied text. The absence of figures, tables, and supplementary data limits the ability to fully evaluate the experimental results and their interpretation.
- **Shared manuscript claim summary** The authors present a proof-of-concept study for analyte-responsive polymers (ARPs) by demonstrating that binding of the SH3 domain to a peptide-elastin-like polymer (ELP) fusion alters the polymer's phase transition temperature (Tt) and self-assembly behavior. The study combines isothermal titration calorimetry (ITC), circular dichroism (CD), dynamic light scattering (DLS), and UV-vis turbidimetry to characterize the biophysical effects of ligand binding. The observed shift in Tt is attributed to specific SH3-peptide interactions, supported by a control experiment with a binding-deficient SH3 mutant and a non-binding ELP control. The results are compared with predictions from a published computational model.
- **Visible evidence base** The provided text includes descriptions of experimental methods and qualitative summaries of results. Specific numerical data (e.g., Kd values, ΔCp values, Tt values) are mentioned in the text but are not presented in a structured format (e.g., tables or figures) within the supplied material. The text references figures (Figure 1, 2, 3, 4, 5, 6) and tables (Table 1, 2) that were not provided.
- **Missing materials affecting confidence** The absence of all figures, tables, and supplementary material (including Tables S1–S5 and Figures S1–S6) significantly limits the ability to verify the quantitative claims, assess the quality of the data, and evaluate the statistical significance of the reported effects. The full experimental details for the computational predictions are also not fully described in the provided text.

## Reviewer
- **Overall assessment** This manuscript presents a well-motivated and carefully designed study addressing a relevant question in the field of stimuli-responsive biomaterials. The authors combine a range of biophysical techniques to characterize the effect of ligand binding on the phase behavior of an ELP fusion, and the inclusion of appropriate controls (a non-binding ELP and a binding-deficient SH3 mutant) strengthens the central claim. The work is likely to be of interest to researchers in biosensing, protein engineering, and biomaterials. However, the current manuscript has several technical and presentational issues that need to be addressed. The most significant concerns relate to the interpretation of the ITC data, the quantitative analysis of the DLS and UV-vis data, and the clarity of the computational predictions. The manuscript would be substantially strengthened by a more detailed presentation of the data and a more critical discussion of the limitations of the model system.
- **Who would be interested in the results, and why** Researchers working on the design of stimuli-responsive polymers and hydrogels, particularly those using ELPs or similar intrinsically disordered protein-based materials. The work is also relevant to the biosensor community, as it provides a proof-of-concept for a label-free detection strategy based on phase transitions. Additionally, the study contributes to the fundamental understanding of how ligand binding can modulate the phase behavior of intrinsically disordered proteins, which is of interest to the broader biophysics and cell biology communities.
- **Major strengths**
    1.  The study addresses a significant and timely problem: the rational design of analyte-responsive polymers for biosensing.
    2.  The experimental design is logical and includes appropriate controls (K-sEL, SH3W58A) to support the specificity of the observed effects.
    3.  The combination of multiple biophysical techniques (ITC, CD, DLS, UV-vis) provides a multi-faceted view of the system.
    4.  The comparison of experimental results with a published computational model is a valuable aspect of the work.
    5.  The manuscript is generally well-written and the logic is easy to follow.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Data interpretation and support for claims
    - **Claim pointer** The authors claim that the increased apparent affinity of SH3 for Scp(12)-sEL compared to the free peptide is due to avidity effects and that a fraction of the ELP may be in a coacervate phase during the ITC experiment.
    - **Evidence pointer** Results and Discussion, ITC section; Table 1 (not provided)
    - **Concern** The interpretation of the ITC data is speculative and not fully supported by the presented evidence. The lower n value and higher apparent affinity could be due to several factors, including protein aggregation, non-specific binding, or errors in active concentration determination. The authors mention ruling out truncation by mass spectrometry, but this does not exclude other causes. The hypothesis of coacervate formation during the ITC experiment is plausible but is not directly tested or supported by any data presented in the text. The ITC data itself (the isotherms, the fits, the residuals) is not shown, making it impossible to assess the quality of the fits and the reliability of the derived thermodynamic parameters.
    - **Why it matters** The interpretation of the ITC data is central to the authors' understanding of the binding mechanism in the context of the ELP fusion. If the interpretation is incorrect, the conclusions about the coupling between binding and phase behavior may be flawed. The lack of primary ITC data prevents the reader from evaluating the validity of the reported Kd and ΔH values.
    - **Resolution test** The authors should provide the raw ITC isotherms and fit results for all conditions. They should also perform and present control experiments to directly test the hypothesis of coacervate formation during the ITC experiment (e.g., ITC at concentrations below and above the Tt of the ELP, or DLS measurements under ITC conditions). A more rigorous discussion of alternative explanations for the low n value is required.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Quantitative data presentation and analysis
    - **Claim pointer** The authors report specific Tt values and ΔTt values (e.g., +4 °C, +8 °C, +16 °C) derived from DLS and UV-vis measurements.
    - **Evidence pointer** Results and Discussion, DLS and UV-vis sections; Figures 4, 5, 6 (not provided); Table S5 (not provided)
    - **Concern** The quantitative analysis of the DLS and UV-vis data is not described in sufficient detail. The method for determining Tt from the DLS data (e.g., the size threshold, the fitting procedure) is not clearly defined. The UV-vis data is presented as turbidity at 400 nm, but the exact definition of Tt from these curves is not given. The reported ΔTt values are presented without any measure of uncertainty or statistical analysis. The text mentions that "Tt values are a practical but simplified metric," but the criteria for this metric are not defined.
    - **Why it matters** The central claim of the paper is that ligand binding shifts the Tt of the ELP. Without a clear and rigorous definition of how Tt is determined and without any error analysis, the reader cannot assess the significance or robustness of the reported shifts. This is a critical issue for the validity of the main conclusion.
    - **Resolution test** The authors should provide a detailed description of the data analysis procedure for both DLS and UV-vis, including the exact criteria for determining Tt. They should present the data with appropriate error bars and perform statistical tests to demonstrate that the observed ΔTt values are significant. The raw data (e.g., DLS size vs. temperature plots, UV-vis turbidity vs. temperature curves) should be shown in the figures.
    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Computational model validation
    - **Claim pointer** The authors state that their experimental results are "consistent with predictions from a published model for ELP fusions" and that the similarities are "encouraging."
    - **Evidence pointer** Results and Discussion, Computational section; Figure 6 (not provided); Table 2 (not provided)
    - **Concern** The comparison between the experimental ΔTt and the computationally predicted ΔTt is not presented quantitatively. The text states that the model predicted a ΔTt of -20 °C for Scp(12)-sEL compared to K-sEL, while the experiment gave -10 °C, and that the model predicted +7.23 °C for binding, while the experiment gave +4 °C. While the authors note the model over-predicts by a factor of two, the significance of this discrepancy is not discussed. The model was developed for a different ELP backbone, and the authors acknowledge this, but the implications of this difference for the validity of the comparison are not explored. The details of the computational predictions (e.g., the structures, the SIC values) are not provided in the text.
    - **Why it matters** The comparison with the computational model is a key part of the paper's claim that the observed effects are predictable. A superficial comparison that does not address the quantitative discrepancies or the limitations of the model weakens this claim.
    - **Resolution test** The authors should provide a more detailed quantitative comparison, including a table of predicted and experimental ΔTt values for all constructs. They should discuss the potential reasons for the observed discrepancies (e.g., the different ELP backbones, the effect of the fusion context on the peptide structure). The computational methods should be described in enough detail to be reproducible.
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity and completeness of methods
    - **Affected element** ITC methods
    - **Evidence pointer** Materials and Methods, Isothermal Titration Calorimetry
    - **Issue** The ITC methods section does not specify the buffer conditions used for the titrations. The buffer composition can significantly affect binding thermodynamics, especially for systems involving hydrophobic interactions and potential coacervation.
    - **Required correction** Please specify the exact buffer composition (including salt concentration and pH) used for all ITC experiments.
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Clarity of data presentation
    - **Affected element** CD data analysis
    - **Evidence pointer** Results and Discussion, CD section; Figure 3 (not provided)
    - **Issue** The CD data is described qualitatively. The authors mention "increased ellipticity at 198 nm" and "reduced temperature sensitivity," but no quantitative analysis (e.g., molar ellipticity values, deconvolution results) is presented.
    - **Required correction** Please provide quantitative CD data, such as mean residue ellipticity values at key wavelengths, and consider performing a more detailed analysis of the secondary structure content if possible.
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Reproducibility of computational methods
    - **Affected element** Computational methods
    - **Evidence pointer** Materials and Methods, Computational section
    - **Issue** The description of the computational methods is brief. The specific version of Rosetta and the scoring function used are not mentioned. The method for generating the point mutations and the energy minimization protocol are described, but the parameters are not fully specified.
    - **Required correction** Please provide more details on the computational methods, including software versions, scoring functions, and any relevant parameters, to ensure the work is reproducible.
    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Interpretation of results
    - **Affected element** Discussion of CD results
    - **Evidence pointer** Results and Discussion, CD section
    - **Issue** The authors interpret the CD changes as indicating "increased order" upon SH3 binding. This is a reasonable interpretation, but it is not the only possibility. Changes in the CD spectrum could also arise from changes in the local environment of the peptide or from scattering artifacts.
    - **Required correction** Please discuss alternative interpretations of the CD data and consider whether the observed changes are consistent with the proposed mechanism.
- **Technical failings that need to be addressed before the case is established**
    - R1-M1: The interpretation of ITC data is not sufficiently supported, and the primary data is not shown.
    - R1-M2: The method for determining Tt from DLS and UV-vis data is not defined, and no error analysis is provided.
- **Assessment against Nature-style criteria**
    - **Originality** The concept of using ligand-induced shifts in the phase transition of ELPs for biosensing is not entirely new, but the systematic biophysical characterization of a model system with appropriate controls is a valuable contribution. The study is not highly original but is a solid and useful piece of work.
    - **Scientific importance** The work addresses a key challenge in the field of stimuli-responsive materials: achieving specific and predictable responses to molecular analytes. The findings have implications for the design of biosensors and adaptive materials. The importance is moderate, as the system is a proof-of-concept and not a fully functional device.
    - **Interdisciplinary readership** The topic is inherently interdisciplinary, spanning protein engineering, polymer science, biophysics, and biosensing. The manuscript is written in a way that should be accessible to researchers in these fields, although some prior knowledge of ELPs and biophysical techniques is assumed.
    - **Technical soundness** The experimental design is generally sound, with appropriate controls. However, the lack of detailed quantitative data and analysis, particularly for the ITC and Tt measurements, is a significant weakness. The computational predictions are not presented in a way that allows for a rigorous comparison with the experimental results.
    - **Readability for nonspecialists** The manuscript is clearly written and the logic is easy to follow. The abstract and introduction provide a good overview. However, the results and discussion sections are dense and may be challenging for readers without a strong background in biophysical chemistry.
- **Recommendation posture** Supportive if technical concerns are resolved. The central claim is plausible and the experimental approach is sound, but the current presentation of the data does not fully support the conclusions. The authors need to provide a more rigorous and quantitative analysis of their results, particularly for the ITC and Tt measurements, and a more critical discussion of the limitations of their model system and the computational comparison.

## Risk / unsupported claims
- The claim that the increased apparent affinity of SH3 for Scp(12)-sEL is due to avidity effects is a hypothesis that is not directly tested.
- The claim that the reversal of the ΔH vs. T trend at 32 °C is due to endothermic loss of hydrophobic hydration associated with ELP coacervation is speculative and not supported by direct evidence.
- The claim that the CD changes indicate "increased order" upon SH3 binding is an interpretation that is not fully justified.
- The quantitative values of Kd, ΔH, ΔCp, and Tt are mentioned in the text but cannot be verified without the figures and tables.
- The comparison with the computational model is presented qualitatively and the significance of the discrepancies is not discussed.