## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion) as provided
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims based solely on the supplied text
- **Shared manuscript claim summary** The authors propose that statistical physics-derived sequence metrics (SCDM, SHDM, SHDdz) and dynamic profiles (DFI) can functionally classify two families of intrinsically disordered proteins (NCBD and CID), and that these metrics can quantitatively model binding affinities between the two IDP families
- **Visible evidence base** Text descriptions of methods and results, references to figures (Figures 1, 3, 4, 5, 6, 7, 8, 9), tables (Tables S1, S2), and supplementary figures (Figures S1-S16) as cited in text
- **Missing materials affecting confidence** Actual figures, tables, and supplementary information are not provided; numerical values for correlations, statistical significance, and quantitative results are not visible; simulation details are only referenced

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting extension of statistical physics-based sequence metrics to the functional classification of IDPs and their complexation. The integration of multiple complementary approaches (charge-based, hydropathy-based, dynamics-based) is a strength. However, the provided text alone does not allow verification of the central quantitative claims. Key figures and numerical results are referenced but not visible, and several methodological details are described only at a high level. The claim that binding affinities can be "quantitatively recapitulated" requires scrutiny of the actual correlation values, which are not provided in the visible text. The manuscript would benefit from clearer articulation of what is novel relative to prior work by the same group, and from a more critical discussion of the limitations of the composite-chain approximation for binding free energy.

- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, protein biophysics, computational biology, and sequence-function relationships. The work is also relevant to those interested in statistical mechanics approaches to polymer theory and their application to biological macromolecules. The potential to classify IDPs and predict binding affinities from sequence alone would be of broad interest to the protein science community.

- **Major strengths**
  1. The conceptual framework is well-motivated: applying statistical physics-derived sequence metrics to IDP classification addresses a genuine challenge in the field.
  2. The study uses a well-characterized model system (NCBD-CID) with both extant and ancestral sequences, providing a rigorous test bed.
  3. The integration of multiple complementary metrics (charge, hydropathy, dynamics) is thoughtful and acknowledges the multifunctionality of IDPs.
  4. The theoretical formalism that allows extraction of interaction matrices from simulations is an elegant feature.
  5. The authors are appropriately cautious in some interpretations, acknowledging when classifications diverge and when experimental validation is lacking.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "We find that multiple physics-based sequence metrics quantitatively recapitulate the binding affinities between CID and NCBD variants"
- **Evidence pointer** Figure 8, Figure 9, Section 3.5
- **Concern** The central quantitative claim of the paper, that physics-based metrics can quantitatively model binding affinities, is presented without any visible numerical results. The text states that PC3 of the joint SHDM and SHDdz matrices "correlates reasonably well" and that the free energy model "correlates well" with measured Kd values, but no correlation coefficients, p-values, or effect sizes are provided in the visible text. The reader cannot assess the strength of these correlations or compare them across methods.
- **Why it matters** The quantitative claim is the primary novel contribution of the work. Without visible statistics, the claim is unverifiable from the provided material. The word "quantitatively" implies a specific numerical relationship that must be demonstrated.
- **Resolution test** Provide the actual correlation coefficients (e.g., Pearson r, Spearman rho), p-values, confidence intervals, and sample sizes for all reported correlations. Show the scatter plots with regression lines and clearly identify any outliers. State explicitly what "reasonably well" and "well" mean in numerical terms.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological validation
- **Claim pointer** "SHDM yields maps of nonelectrostatic interactions" and "we extracted SHDM from the ensemble average distances between residues from all-atom molecular dynamics (MD) simulations"
- **Evidence pointer** Section 2.2, Equation 3, Section 2.3
- **Concern** The extraction of SHDM from MD simulations via inversion of Equation 3 is a critical methodological step, but the text does not describe how this inversion is performed, what the numerical stability of the inversion is, how sensitive the results are to simulation length or force field, or how the extracted SHDM values were validated. The convergence criteria are referenced only to supplementary figures. Without this information, the reliability of the SHDM-based classifications cannot be assessed.
- **Why it matters** If the SHDM extraction is numerically unstable or sensitive to simulation details, the resulting classifications and correlations with binding data could be artifacts. The method must be shown to be robust.
- **Resolution test** Describe the inversion procedure in detail, including any regularization or constraints used. Show that the extracted SHDM values are converged with respect to simulation length (e.g., by splitting trajectories and comparing). Validate the extracted SHDM against known interaction propensities or against SHDM computed from independent simulations with different force fields.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Conceptual validity
- **Claim pointer** "We assume that the free energy of complexation can be approximated by the free energy of a composite IDP created by covalently linking the two sequences"
- **Evidence pointer** Section 2.6, Figure 9
- **Concern** The approximation that binding free energy can be modeled as the free energy of a covalently linked composite chain is a strong assumption. The authors acknowledge two limitations (alternate binding modes and neglect of counterion release), but there are additional concerns. A covalently linked chain has different conformational entropy than two separate chains, and the linker itself (even a 10-alanine linker) may introduce artifacts. The text does not discuss how the choice of the lowest free energy among four linkage configurations is justified, nor whether this choice introduces selection bias.
- **Why it matters** If the composite-chain model is not a valid approximation, the correlation with Kd values could be coincidental or driven by the model's artifacts rather than by the physics of binding. The model's predictive value for new sequences would be questionable.
- **Resolution test** Validate the composite-chain model against a more rigorous approach (e.g., explicit two-chain simulations or a thermodynamic cycle) for at least a subset of pairs. Show that the model's predictions are robust to the choice of linkage configuration and linker length. Discuss the entropic penalty of covalent linkage and how it is accounted for.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretive clarity
- **Claim pointer** "Different classification schemes may capture distinct features encoded in the sequence that are responsible for specific sets of functions, thereby yielding different groupings"
- **Evidence pointer** Section 3.4, Figure 7
- **Concern** The authors interpret disagreements between classification schemes as evidence of multifunctionality. While this is a plausible interpretation, an alternative explanation is that some methods are simply less accurate or capture noise. The text does not provide a principled way to distinguish between these possibilities, nor does it offer a framework for deciding which classification is "correct" for a given functional question.
- **Why it matters** The paper's conclusion that different metrics capture different functional features is a strong interpretive claim. Without a way to validate which classification is functionally relevant, the claim remains speculative.
- **Resolution test** Propose a specific, testable prediction that would distinguish between the "multifunctionality" and "method inaccuracy" interpretations. For example, design a mutagenesis experiment where the two interpretations predict different functional outcomes. Alternatively, use a dataset with known functional annotations to benchmark which classification scheme best predicts function.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Equation 1
- **Evidence pointer** Section 2.1
- **Issue** The definition of SCDM in Equation 1 is dense and the summation indices are not fully explained in the text. The physical meaning of each term could be clarified.
- **Required correction** Add a brief explanation of each summation term in Equation 1, and clarify the physical interpretation of the SCDM matrix elements.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** MD simulation parameters
- **Evidence pointer** Section 2.2, Section 2.4
- **Issue** The text states that "all-atom explicit solvent simulation" was used and references supplementary sections, but key parameters (force field, water model, salt concentration, temperature, simulation length) are not stated in the main text.
- **Required correction** Include the essential simulation parameters in the main text or ensure they are prominently stated in the supplementary information.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** PCA-based clustering
- **Evidence pointer** Section 2.5, Section 3.1
- **Issue** The text does not describe how the number of principal components was chosen, how many components were retained, or how the clustering was performed (e.g., which distance metric and linkage method were used for the dendrograms).
- **Required correction** Provide details on the PCA procedure, including the number of components retained, the variance explained, and the clustering algorithm used.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion of outliers
- **Evidence pointer** Section 3.5, Figure 9
- **Issue** The text mentions "two notable outliers with high Kd" but does not discuss what these outliers are, why they deviate, or what this deviation implies for the model.
- **Required correction** Identify the outlier pairs and provide a brief discussion of possible reasons for their deviation from the model.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "marginal IDP"
- **Evidence pointer** Introduction
- **Issue** The term "marginal IDP" is used but not defined. It is unclear whether this is a standard term or a new concept introduced by the authors.
- **Required correction** Define "marginal IDP" upon first use, or use a more standard term such as "partially structured IDP."

## Risk / unsupported claims
- The claim that physics-based metrics "quantitatively recapitulate" binding affinities is unsupported in the visible text because no numerical correlation statistics are provided.
- The claim that SHDM-based classification is "consistent with the binding affinity data" for NCBD sequences is not verifiable without the actual dendrograms and binding data being visible.
- The claim that DFI "provides broad agreement with other physics-based classification tools" is based on visual comparison of dendrograms that are not visible in the provided text.
- The statement that the free energy model "correlates well" with Kd values is unverifiable without the actual correlation coefficient and the scatter plot.
- The claim that the classification of CID into two groups "is consistent with several observations" including binding affinities and evolutionary timeline is partially supported by text description but cannot be fully assessed without the figures.
- The assertion that "different classification schemes may capture distinct features... responsible for specific sets of functions" is presented as a conclusion but is speculative without functional validation experiments.
- The statement that "adding linkers does not significantly change the correlation" is unverifiable without the actual comparison data.
- The claim that the approach "provides a generalizable strategy for classifying IDPs and predicting complexation behavior" is an extrapolation from a single model system and requires demonstration on additional IDP families.