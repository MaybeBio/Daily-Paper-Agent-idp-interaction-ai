## Review setup
- **Input scope** Full manuscript text (main text, methods, significance statement) without supplementary information, figures, or tables
- **Assessment boundary** Evaluation of the methodological approach, claims, and conclusions based solely on the provided main text; supplementary figures/tables referenced but not available for inspection
- **Shared manuscript claim summary** The authors construct Markov state models (MSMs) of the folding-upon-binding pathways of the intrinsically disordered measles virus NTAIL protein to the X domain (XD) of the measles virus phosphoprotein, using a 200-μs explicit solvent MD simulation. They compare a traditional tICA-based hidden Markov state model (HMSM) with a deep learning-based MSM (VAMPnet with physical constraints) using a multi-input neural network architecture. The deep MSM resolves additional structurally and kinetically distinct states, including two encounter complexes and an off-pathway kinetic trap, and the authors conclude that folding-upon-binding proceeds via an induced-fit mechanism with multiple intermediates rather than conformational selection.
- **Visible evidence base** Main text only; references to SI Appendix figures (S1–S22), tables (S1, S2), and equations (S8) are made but the actual content is not provided
- **Missing materials affecting confidence** All supplementary information (figures, tables, methods details, transition matrices, error estimates, chemical shift predictions), the MD trajectory itself, and the code repository contents; figure panels referenced in the main text (Figs. 1–6) are not visible

## Reviewer

- **Overall assessment** The manuscript presents a technically sophisticated application of deep learning-based Markov state modeling to a biologically important problem: the folding-upon-binding mechanism of an intrinsically disordered protein. The methodological innovation, a multi-input neural network architecture combining convolutional and fully connected layers to process heterogeneous feature types, is well motivated and clearly described. The central claim, that the deep MSM resolves states not captured by a traditional tICA-based HMSM and that the resulting kinetic model supports an induced-fit mechanism with multiple intermediates, is plausible but cannot be fully verified from the provided main text alone. The absence of the supplementary material, which contains the quantitative validation (CK test, implied timescales, transition matrices, error estimates), substantially limits the ability to assess the robustness of the model and the statistical significance of the reported differences between states. The writing is clear and accessible, and the discussion appropriately contextualizes the findings within existing experimental and computational literature. However, several claims regarding the biological interpretation, particularly the dismissal of conformational selection, rest on transition probabilities that are reported with statistical uncertainties in the SI but not fully interpreted in the main text. The manuscript is likely to be of interest to the biophysics and computational chemistry communities, and the methodological framework may have broader applicability, but the strength of the conclusions depends critically on the quality of the validation presented in the SI.

- **Who would be interested in the results, and why** Computational biophysicists and chemists studying protein folding, intrinsically disordered proteins, and molecular dynamics simulation analysis would be the primary audience. Researchers developing or applying Markov state models and deep learning methods for biomolecular simulations would find the methodological advances relevant. Experimental biophysicists studying IDP binding mechanisms, particularly those using NMR, stopped-flow kinetics, or mutagenesis, would be interested in the atomistic mechanistic insights and the predicted chemical shifts that could guide future experiments. The work may also appeal to a broader readership interested in the induced-fit versus conformational selection debate in molecular recognition.

- **Major strengths**
  1. The methodological innovation of a multi-input neural network architecture that processes different feature types (contact maps, helical order parameters, secondary structure assignments) with appropriate layer types is well conceived and clearly described.
  2. The comparison between a traditional linear dimensionality reduction approach (tICA) and a deep learning approach on the same dataset provides a direct demonstration of the enhanced resolution offered by the latter.
  3. The biological question is significant, and the study leverages a long, unbiased MD simulation that contains multiple binding and unbinding events, providing a rich dataset for kinetic analysis.
  4. The interpretation of the results in the context of the induced-fit versus conformational selection debate is thoughtful and nuanced, acknowledging the complexity of the mechanism rather than forcing a simple dichotomy.
  5. The discussion of potential experimental validation through NMR chemical shift predictions and augmented Markov state models is forward-looking and practically useful.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / validation
- **Claim pointer** The deep MSM resolves two structurally and kinetically distinct encounter complex states and an off-pathway kinetic trap, and the transition probabilities among states support an induced-fit mechanism.
- **Evidence pointer** Figures 4 and 5; SI Appendix Figs. S12–S19, S17, S18; location not provided for specific values
- **Concern** The central claims of the paper depend on the quantitative validation of the deep MSM, including the Chapman–Kolmogorov test, implied timescales, transition matrix uncertainties, and the statistical significance of differences in transition probabilities between states. None of this validation material is visible in the provided main text. The CK test is mentioned as shown in SI Appendix Fig. S12, but the results are not summarized or interpreted in the main text. Without evidence that the model is well-validated and that the reported differences between states (e.g., transition probabilities from states 6 and 7 to native-like states) are statistically significant beyond the quoted error bars, the mechanistic conclusions cannot be considered established.
- **Why it matters** The entire mechanistic interpretation, including the dismissal of conformational selection, rests on the reliability of the kinetic model. If the model is not adequately validated or if the differences in transition probabilities are within statistical noise, the conclusions would be substantially weakened. The main text reports some values with uncertainties (e.g., "0.1 ± 0.01%") but does not provide a clear statistical framework for comparing these values across states.
- **Resolution test** Provide a summary of the CK test results and implied timescales in the main text, including whether the model satisfies the Markov property at the chosen lag time. Present a clear statistical comparison of transition probabilities between key states (e.g., states 6 and 7 to states 1 and 2) with appropriate uncertainty estimates, and state explicitly whether the differences are significant. If the SI contains this information, the main text should reference it more explicitly and summarize the key findings.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility / methodological completeness
- **Claim pointer** The multi-input neural network architecture with convolutional layers for contact maps and fully connected layers for vector features was optimized by iteratively maximizing the VAMP-2 score, and the final architecture is described in SI Appendix Fig. S10.
- **Evidence pointer** Methods section; SI Appendix Fig. S10; location not provided
- **Concern** The description of the neural network architecture in the main text is high-level, and the specific details (number of layers, layer sizes, activation functions, regularization, training procedure, hyperparameter search ranges) are relegated to the SI. While this is common practice, the main text does not provide sufficient information for a reader to understand the key architectural choices or to assess potential overfitting or training instability. The claim that the architecture was determined by "iteratively optimizing the VAMP-2 score" is vague without details on the search procedure and the sensitivity of the results to architectural choices.
- **Why it matters** Reproducibility is a core requirement for computational studies. The methodological novelty of this work lies in the specific neural network architecture, and readers need sufficient detail to understand and potentially replicate the approach. The lack of detail in the main text makes it difficult to assess whether the reported improvements over tICA are robust to architectural variations or specific to the chosen hyperparameters.
- **Resolution test** Provide a more detailed summary of the architecture in the main text (e.g., number of layers and units per layer, activation functions, regularization methods) and describe the hyperparameter optimization procedure, including the range of values explored and the criterion for selecting the final model. If the SI contains this information, the main text should summarize the key choices and their rationale.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Biological interpretation / claim support
- **Claim pointer** The authors conclude that folding-upon-binding pathways proceed through an induced-fit mechanism with multiple and alternative intermediates and are not consistent with a conformational selection mechanism.
- **Evidence pointer** Discussion section; Figures 4 and 5; SI Appendix Fig. S17
- **Concern** The conclusion that the mechanism is induced-fit rather than conformational selection is based on the observation that the more helical encounter complex (state 7) does not transition more readily to the more helical native-like states (states 1 and 2) than the less helical encounter complex (state 6). However, the main text reports that transition probabilities from state 7 to states 1 and 2 are actually lower than from state 6 to states 1 and 2, which is interpreted as evidence against conformational selection. This interpretation assumes that the helical content of the encounter complex should be predictive of the pathway taken, but the authors themselves note that helical content formed early frequently breaks and refolds. The distinction between induced-fit and conformational selection may be overly simplistic for a system with this degree of conformational heterogeneity, and the authors' own data suggest a more complex picture than either classical mechanism.
- **Why it matters** The biological conclusion is a major selling point of the paper. If the interpretation is not fully supported by the data, or if the induced-fit versus conformational selection framework is not the most appropriate lens through which to view the results, the significance of the work is diminished. The authors acknowledge this complexity in the discussion but do not fully resolve the tension between their conclusion and their own observations.
- **Resolution test** Clarify the criteria by which the data distinguish induced-fit from conformational selection, and discuss whether the observed mechanism might be better described as a hybrid or more complex process. If the distinction is primarily semantic, state this explicitly. Alternatively, provide additional quantitative evidence (e.g., flux analysis along specific reaction coordinates) that more directly supports the induced-fit interpretation.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity / terminology
- **Affected element** Use of "fuzzy" complex terminology
- **Evidence pointer** Significance statement; Discussion
- **Issue** The term "fuzzy" complex is used without definition or citation. While this term is established in the IDP literature, readers unfamiliar with it may be confused.
- **Required correction** Define the term "fuzzy complex" on first use and provide a citation to the relevant literature.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness / reporting
- **Affected element** Simulation temperature rationale
- **Evidence pointer** Molecular Dynamics Simulation section
- **Issue** The simulation was performed at 400 K, which is above physiological temperature. The authors state this was chosen to enable efficient sampling but do not discuss the potential impact of elevated temperature on the observed mechanisms or the generalizability of the conclusions to physiological conditions.
- **Required correction** Add a brief discussion of the potential effects of the elevated simulation temperature on the observed folding-upon-binding pathways and the extent to which the conclusions are expected to hold at lower temperatures.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity / interpretation
- **Affected element** State numbering and comparison between HMSM and deep MSM
- **Evidence pointer** Results section; Figures 1 and 4
- **Issue** The relationship between the seven HMSM states and the twelve deep MSM states is described in the text, but the correspondence is not always clear. For example, deep MSM states 1-4 are said to resemble HMSM states 1-4, and deep MSM state 8 resembles HMSM state 6, but the fate of HMSM state 7 and the relationship of deep MSM states 9-12 to the HMSM states is less clearly articulated.
- **Required correction** Provide a clearer mapping between the HMSM and deep MSM states, possibly in a table or schematic, to help the reader understand the relationship between the two models.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness / reporting
- **Affected element** Code and data availability
- **Evidence pointer** Data, Materials, and Software Availability section
- **Issue** The code is available on GitHub, but the MD trajectory is only available by request from D.E. Shaw Research. This is understandable given the proprietary nature of the simulation, but it limits the ability of other researchers to fully reproduce the analysis.
- **Required correction** Acknowledge this limitation explicitly and consider whether any processed data (e.g., feature matrices, state assignments) could be made publicly available to facilitate independent analysis.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity / presentation
- **Affected element** Figure references
- **Evidence pointer** Results section
- **Issue** The main text references figures (Figs. 1–6) that are not visible in the provided material. While this is expected for a manuscript submission, the text should be self-contained enough for a reader to understand the key findings without seeing the figures.
- **Required correction** Ensure that all quantitative claims are stated explicitly in the text and that the figures serve as supporting illustrations rather than the primary source of information.

## Risk / unsupported claims
- The claim that the deep MSM resolves two structurally and kinetically distinct encounter complexes and an off-pathway kinetic trap cannot be fully assessed without the SI figures and tables that contain the quantitative validation and state characterization.
- The conclusion that the mechanism is induced-fit rather than conformational selection is based on transition probability comparisons that are reported with uncertainties in the SI but not fully statistically analyzed in the main text.
- The claim that the multi-input neural network architecture provides a "generalizable approach" for IDP simulation data is speculative and not directly demonstrated beyond the single system studied.
- The predicted NMR chemical shifts for each deep MSM state (SI Appendix Fig. S22) are mentioned as a potential tool for experimental validation, but the actual predictions and their implications are not discussed in the main text.
- The statement that the deep MSM "effectively fine grains" the heterogeneous encounter complex into three distinct states is based on the model's state assignments, but the physical significance of these sub-states is inferred from structural properties and not directly validated against experimental data.