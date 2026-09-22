## Review setup

- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and supplementary information (SI) appendix.
- **Assessment boundary** Scientific validity, technical soundness, and clarity of the presented theoretical and experimental work. The review is based solely on the provided manuscript content.
- **Shared manuscript claim summary** The authors use a combination of analytical theory (rG-RPA), field-theoretic simulations (FTS), and coarse-grained molecular dynamics (MD) to rationalize experimental observations of salt- and ATP-dependent liquid-liquid phase separation (LLPS) of the Caprin1 IDR and its phosphorylated variant pY-Caprin1. They propose that electrostatic interactions, particularly ion bridging and the high valency of ATP-Mg, are key drivers of reentrant phase behavior and ATP colocalization in condensates.
- **Visible evidence base** The manuscript provides experimental phase diagrams (Fig. 1c,d), turbidity data (Fig. 3a), ion concentration measurements (Tables 1, 2), and theoretical predictions from rG-RPA (Figs. 1, 2), MD (Figs. 4-7), and FTS (Figs. 8, 9). The SI contains additional methodological details and supporting figures.
- **Missing materials affecting confidence** The manuscript does not provide full experimental details for all phase diagram points, particularly for the ATP-Mg experiments. The specific parameters for the FTS and MD simulations (e.g., force field parameters, system sizes, equilibration times) are only partially described in the main text and SI. The exact fitting procedure for the rG-RPA+FH model to experimental data is not fully detailed.

## Reviewer

- **Overall assessment** This manuscript presents a comprehensive and multi-faceted theoretical and computational study of the electrostatic determinants of LLPS in a biologically relevant IDR system. The combination of analytical theory, field-theoretic simulations, and coarse-grained MD is a significant strength, providing a robust and cross-validated framework. The work successfully rationalizes a wide range of experimental observations, including the contrasting salt-dependent behaviors of Caprin1 and pY-Caprin1, and offers a compelling electrostatic explanation for ATP's role in condensate formation and ion partitioning. The study is technically sound and the conclusions are generally well-supported by the presented evidence. However, the manuscript would benefit from a more detailed discussion of the limitations of the coarse-grained models and a clearer presentation of the quantitative agreement between theory and experiment.
- **Who would be interested in the results, and why** This work will be of high interest to researchers in the fields of biophysics, physical chemistry, and cell biology, specifically those studying biomolecular condensates, intrinsically disordered proteins, and phase separation. The findings are relevant for understanding the physical principles governing membraneless organelle formation and the diverse roles of metabolites like ATP. The methodological framework presented (combining rG-RPA, FTS, and MD) will be a valuable resource for the community.
- **Major strengths**
    1.  The use of three complementary theoretical approaches (rG-RPA, FTS, MD) to cross-validate findings is a major strength, providing a high degree of confidence in the robustness of the conclusions.
    2.  The study successfully connects theoretical predictions to a broad range of experimental data, including phase diagrams, turbidity measurements, and direct ion concentration measurements, demonstrating the practical utility of the models.
    3.  The work provides a clear and physically intuitive explanation for the reentrant phase behavior of polyelectrolytes, highlighting the role of ion bridging and counterion valency, which is a significant conceptual advance.
    4.  The study offers a nuanced perspective on ATP's role, showing that its electrostatic effects (as a high-valency ion) can complement previously identified π-related and hydrotropic functions, thereby unifying different mechanistic views.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical Soundness
    - **Claim pointer** The authors claim that their theoretical models "consistently predict salt-dependent reentrant phase behaviors for Caprin1" and that the "high valency of ATP-magnesium is a significant factor for its colocalization with the condensed phases."
    - **Evidence pointer** Figures 2, 4, 8, 9; Tables 1, 2
    - **Concern** While the qualitative agreement between theory and experiment is compelling, the manuscript lacks a quantitative comparison. For example, the rG-RPA+FH model is fitted to experimental data, but the quality of the fit and the resulting parameter values are not discussed in detail. Similarly, the MD and FTS results are presented in terms of trends, but the degree to which they quantitatively reproduce experimental phase boundaries or ion partition coefficients is not assessed. A more rigorous quantitative comparison would significantly strengthen the claims.
    - **Why it matters** Without a quantitative assessment, it is difficult to judge the predictive power of the models and to distinguish between different physical mechanisms that might produce similar qualitative trends. This is crucial for establishing the models as reliable tools for future predictions.
    - **Resolution test** The authors should provide a quantitative comparison between theoretical predictions and experimental data, such as a plot of predicted vs. experimental critical salt concentrations or a table of fitted model parameters with uncertainties. They should also discuss the quantitative accuracy of the MD and FTS predictions for ion partitioning.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific Importance
    - **Claim pointer** The authors state that their findings "support a significant—albeit not exclusive—role of electrostatics in these biophysical phenomena" and that the approach "should be of general utility."
    - **Evidence pointer** Discussion section
    - **Concern** The manuscript focuses heavily on the electrostatic effects of ATP, but the authors acknowledge that other interactions (π-related, hydrophobic) are also important. The discussion of how these different interaction types combine and compete to determine the overall phase behavior is somewhat limited. A more integrated discussion of the interplay between electrostatics and other forces would provide a more complete picture and increase the impact of the work.
    - **Why it matters** The biological function of condensates is likely determined by the complex interplay of multiple interaction types. A deeper understanding of this interplay is essential for predicting how mutations or changes in cellular conditions might affect condensate properties.
    - **Resolution test** The authors should expand the discussion to more explicitly address the relative contributions of electrostatic versus non-electrostatic interactions. They could, for example, discuss how their electrostatic model might be extended to incorporate π-related interactions or how the relative importance of these forces might vary across different IDR sequences.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical Soundness
    - **Claim pointer** The authors use a 6-bead model for ATP-Mg in FTS and a single-bead model in rG-RPA, and claim that the "high valency of ATP-magnesium is a significant factor for its colocalization."
    - **Evidence pointer** Figure 8a, Materials and Methods
    - **Concern** The modeling of ATP-Mg as a simple charged polymer or a single bead is a significant simplification. The real ATP-Mg complex has a specific charge distribution and geometry that may influence its interactions with the IDR. The manuscript does not discuss the potential limitations of these simplified models or how the results might change with a more detailed representation of ATP-Mg.
    - **Why it matters** The conclusions about the mechanism of ATP colocalization are directly dependent on the accuracy of the ATP-Mg model. If the model is too simplistic, the predicted mechanism may not be representative of the real system.
    - **Resolution test** The authors should acknowledge the limitations of their ATP-Mg model and discuss how the results might be affected by a more detailed representation. They could also perform a sensitivity analysis by varying the charge distribution or size of the ATP-Mg model to see if the qualitative conclusions hold.

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability for Nonspecialists
    - **Affected element** Introduction and Discussion
    - **Evidence pointer** Introduction, Discussion
    - **Issue** The manuscript is dense and uses specialized terminology (e.g., "rG-RPA", "FTS", "polyampholyte") that may be challenging for readers outside the immediate field of polymer physics.
    - **Required correction** The authors should consider adding a brief, plain-language summary of the key concepts and methods at the beginning of the Introduction or in a dedicated "Significance" statement. This would make the work more accessible to a broader audience.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Materials and Methods
    - **Evidence pointer** Materials and Methods, SI Appendix
    - **Issue** The description of the FTS and MD simulation parameters is somewhat fragmented, with some details in the main text and others in the SI. This makes it difficult to fully reproduce the simulations.
    - **Required correction** The authors should consolidate all simulation parameters (e.g., system size, number of chains, ion concentrations, interaction strengths, simulation length) into a single, comprehensive table or section in the SI.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Scientific Importance
    - **Affected element** Discussion
    - **Evidence pointer** Discussion
    - **Issue** The discussion of the potential biological implications of the findings is relatively brief. The authors mention the regulation of ion concentrations but do not elaborate on the potential functional consequences of this regulation.
    - **Required correction** The authors should expand the discussion of the biological relevance of their findings, perhaps by speculating on how the electrostatic control of ion concentrations within condensates might affect enzymatic activity or signaling processes.

- **Technical failings that need to be addressed before the case is established**
    - The lack of a detailed quantitative comparison between theory and experiment (R1-M1) is the most significant technical failing. The authors should provide a more rigorous assessment of the predictive power of their models.
    - The potential limitations of the simplified ATP-Mg model (R1-M3) should be explicitly addressed to ensure the robustness of the conclusions.

- **Assessment against Nature-style criteria**
    - **Originality:** The work is original in its comprehensive combination of three theoretical approaches to address a specific and important problem. The focus on the electrostatic role of ATP as a high-valency ion provides a new perspective.
    - **Scientific importance:** The findings are important for the field of biomolecular condensates, providing a physical framework for understanding the diverse roles of ATP and the effects of salt on phase behavior. The work has the potential to influence future experimental and theoretical studies.
    - **Interdisciplinary readership:** The topic is of interest to researchers in biophysics, physical chemistry, cell biology, and biochemistry. The manuscript is written in a way that is largely accessible to these groups, though some parts may be challenging for non-specialists.
    - **Technical soundness:** The theoretical and computational methods are state-of-the-art and appear to be applied correctly. The main weakness is the lack of a detailed quantitative comparison with experiments, which is needed to fully validate the models.
    - **Readability for nonspecialists:** The manuscript is well-written but dense. A brief summary of key concepts would improve accessibility for a broader audience.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a valuable and comprehensive theoretical framework that successfully rationalizes a wide range of experimental data. The main concerns regarding quantitative validation and model limitations should be addressed to fully establish the case.