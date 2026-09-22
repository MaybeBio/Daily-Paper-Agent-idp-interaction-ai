## Review setup
- **Input scope** Full manuscript text including main text, appendices, and references.
- **Assessment boundary** The scientific claims, methodology, and conclusions presented in the manuscript. The review is based solely on the provided text.
- **Shared manuscript claim summary** The authors propose an effective theory for predicting interactions between heteropolymers, specifically intrinsically disordered protein regions (IDRs). They use molecular dynamics (MD) simulations to fit a dimer-pair approximation for the virial coefficient, which improves upon a simple monomer-pair approximation. This theory is used to predict demixing and hypermixing in multi-component IDR systems, and they identify a low-dimensional space of interactions that constrains the maximum number of demixing components.
- **Visible evidence base** The manuscript includes descriptions of MD simulations (HPS-Tesei, HPS-Dignon, Mpipi models), comparisons of predicted vs. simulated Boyle and critical temperatures, analysis of sequence features (charge, aromatic content, SCD), and multi-component demixing simulations. Figures and tables are referenced but not provided in the text.
- **Missing materials affecting confidence** The actual figures, tables, and supplementary materials are not provided. This includes the data for the 200+ sequences, the specific simulation results, and the code. The review cannot independently verify the quantitative results or the statistical significance of the correlations.

## Reviewer
- **Overall assessment** This manuscript presents a valuable and potentially impactful framework for predicting heteropolymer interactions from sequence. The core idea of using a dimer-pair approximation for the virial coefficient, fitted to MD simulations, is a significant step beyond simple composition-based models. The demonstration that this approach can predict demixing and hypermixing in multi-component systems is compelling. However, the manuscript's current form has several weaknesses. The presentation is dense and sometimes unclear, particularly in the methods and results sections. The lack of access to the figures and data makes it difficult to fully assess the strength of the claims. The theoretical justification for the dimer-pair approximation, while intuitive, needs to be more rigorously presented. The generalizability of the findings, especially the constraint on the number of demixing components, needs a more thorough discussion.
- **Who would be interested in the results, and why** Researchers in the fields of biophysics, computational biology, and protein chemistry, specifically those studying phase separation, intrinsically disordered proteins, and the design of synthetic biomolecular condensates. The work provides a practical tool for predicting whether protein sequences will mix or demix, which is crucial for understanding cellular organization and for engineering condensates with specific properties.
- **Major strengths**
    1.  The manuscript addresses a critical and timely problem: predicting the interaction rules that govern the formation and coexistence of multiple biomolecular condensates.
    2.  The proposed dimer-pair approximation is a novel and practical approach that captures sequence-dependent effects beyond simple composition, showing a clear improvement over the monomer-pair approximation.
    3.  The theory is validated against extensive MD simulations across multiple coarse-grained models, demonstrating its robustness.
    4.  The work provides a clear, actionable framework (with code) for predicting demixing and hypermixing, which is of high practical value for the community.
    5.  The geometric interpretation of the interaction space and the resulting constraint on the number of demixing components is a deep and thought-provoking insight.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical Soundness
    - **Claim pointer** The claim that the dimer-pair approximation, with a single fitted parameter α, can quantitatively predict the Boyle temperature and critical temperature for a wide range of IDR sequences.
    - **Evidence pointer** Section II.2, Figures 1(d-f), 2, Appendix D.
    - **Concern** The manuscript states that the dimer-pair approximation with α=0.75 provides a "quantitative agreement" with simulations. However, the evidence for this is not fully presented in the text. The correlation coefficients are high, but the mean squared error (MSE) or mean squared relative error (MSRE) is only mentioned for the fit of α. The text also notes that the approximation fails for sequences with long charge blocks. The manuscript needs to provide a more detailed error analysis, including the distribution of errors, to support the claim of quantitative agreement. The single fitted parameter α is a major simplification, and its universality across different models and conditions needs to be more strongly justified.
    - **Why it matters** The central claim of the paper is that this theory can be used for quantitative prediction. If the error is not well-characterized, the practical utility of the method is unclear. The failure for charge-blocky sequences is a significant limitation that needs to be quantified and discussed.
    - **Resolution test** Provide a detailed error analysis, such as a histogram of the errors in predicted T_B and T_c for all sequences. Show the error as a function of sequence features (e.g., SCD, charge fraction). Discuss the limitations of the single-parameter fit and under what conditions it is expected to break down.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific Importance
    - **Claim pointer** The claim that the number of sequences that can demix with each other is strongly constrained, with a maximum of six, based on the low-dimensional nature of the interaction space.
    - **Evidence pointer** Section III.5, Figure 8.
    - **Concern** The geometric argument leading to the maximum number of demixing components is elegant but relies on several assumptions. The most critical is the threshold value for the effective interaction parameter (χ~_min) required for demixing. The manuscript uses a specific value to generate Figure 8(e), but it is unclear how sensitive the maximum number (M=6) is to this choice. The argument also assumes that the hypermixing dimensions must be exactly equal across all sequences, which is a very strong constraint.
    - **Why it matters** This is a major conceptual finding of the paper. If the maximum number is highly sensitive to the chosen threshold or the assumptions, the conclusion may be an artifact of the specific model parameters rather than a general principle.
    - **Resolution test** Perform a sensitivity analysis on the maximum number of demixing components as a function of the threshold χ~_min. Discuss the validity of the assumption that hypermixing dimensions must be exactly equal. Consider a more general geometric argument that allows for some tolerance in the hypermixing dimensions.
    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Readability for Nonspecialists
    - **Claim pointer** The overall presentation of the theory and methods.
    - **Evidence pointer** Sections II, III, Appendices A, B, H.
    - **Concern** The manuscript is written in a very dense and technical style. The derivation of the dimer-pair approximation and the geometric arguments in Section III.5 are difficult to follow. The connection between the theoretical constructs (e.g., the virial coefficient matrix, the demixing space) and the physical intuition is not always clear. The appendices contain crucial details but are also presented in a highly mathematical way.
    - **Why it matters** The work is of interest to a broad community, including experimentalists who may not be familiar with the intricacies of polymer theory. A clearer presentation would significantly increase the impact and accessibility of the work.
    - **Resolution test** Rewrite the theory sections to provide more physical intuition. Use simpler language and more illustrative examples. Move some of the detailed derivations to the appendices and provide a high-level summary of the key steps in the main text.
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Section II.1, Figure 1(b)
    - **Evidence pointer** "In Fig. 1 (b), we show how T_B changes with sorting (red dots) or shuffling (yellow dots)"
    - **Issue** The text mentions "over 50 different IDR sequences" for the initial observation, but the figure is not available. It is unclear if the effect of sorting/shuffling is shown for all sequences or just a few examples.
    - **Required correction** Clarify the number of sequences used in Figure 1(b) and describe the sorting/shuffling procedure more explicitly.
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Section II.3, Figure 3
    - **Evidence pointer** "we selected l as l=3l_b by fitting so that the error between T_c and T_c^RDP is approximately minimized"
    - **Issue** The parameter l is a fitting parameter. The manuscript shows that the optimal l/l_b varies between models (3.0, 3.2, 3.6). It is not clear if this parameter has a physical interpretation or if it is purely empirical.
    - **Required correction** Discuss the physical meaning of the fitted parameter l. Is it related to the interaction range or the polymer structure? A brief discussion would strengthen the theoretical framework.
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Reproducibility
    - **Affected element** Appendix G.1
    - **Evidence pointer** "We conducted a binary search scheme at 10 K resolution between 0 K and 630 K to run the simulations at appropriate temperatures."
    - **Issue** The binary search scheme for finding T_c is described, but the criteria for determining whether a simulation is phase-separated or not is not fully detailed. The condition in equation (42) is empirical.
    - **Required correction** Provide more details on the criteria used to judge phase separation in the simulations, such as the density difference threshold or the method for identifying clusters.
    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Section III.4, Figure 7
    - **Evidence pointer** "In Fig. 7 (g), we plot P_n, calculated by..."
    - **Issue** The definition of P_n is clear, but the interpretation of the heatmap is not discussed in detail. It would be helpful to explain what a high P_n for a particular eigenvector means in terms of the physical mechanism of demixing.
    - **Required correction** Add a sentence or two interpreting the results in Figure 7(g) and how they support the proposed rules of demixing and hypermixing.

## Risk / unsupported claims
- The claim of "quantitative agreement" between the theory and simulations is not fully supported by the data presented in the text, as the error analysis is incomplete.
- The claim that the maximum number of demixing components is six is based on a specific threshold and assumptions that are not fully tested for robustness.
- The generalizability of the findings to other coarse-grained models or to experimental systems is not demonstrated, only speculated upon in the discussion.
- The claim that the dimer-pair approximation is "novel" is not fully contextualized against other possible approaches, such as machine-learning potentials or more detailed analytical theories.