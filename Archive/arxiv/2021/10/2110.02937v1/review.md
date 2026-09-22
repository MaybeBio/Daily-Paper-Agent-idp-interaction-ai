## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, methods, results, discussion, and conclusions. Figure legends and figures themselves were not provided.
- **Assessment boundary** This review assesses the scientific claims, theoretical framework, experimental methodology, and interpretation of results as presented in the provided text. The assessment is limited to the content of the manuscript and does not include verification of data not shown or figures not provided.
- **Shared manuscript claim summary** The authors develop a mean-field Flory-Huggins-type theory for liquid-liquid phase separation (LLPS) of two species that form a stoichiometric complex. They apply this theory to the SynGAP/PSD-95 system, a model for postsynaptic densities. The central claim is that the experimentally observed phase behavior, specifically the tie-line pattern, is inconsistent with a model where LLPS is driven solely by interactions among stoichiometric 3:2 SynGAP/PSD-95 complexes. Instead, the authors propose that auxiliary, non-stoichiometric interactions (including SynGAP-SynGAP, PSD-95-PSD-95, and additional SynGAP-PSD-95 interactions) are required to explain the experimental data.
- **Visible evidence base** The evidence base consists of: (1) a theoretical mean-field model with derived free energy expressions and phase equilibrium conditions; (2) experimental sedimentation-based phase separation assays to construct a phase diagram; (3) confocal fluorescence microscopy to quantify PSD-95 concentration in the condensed phase; and (4) a comparison of theoretical predictions with experimental data, primarily through qualitative assessment of tie-line patterns.
- **Missing materials affecting confidence** The following materials were not provided and would be necessary for a complete assessment: all figures (including the phase diagrams in Figs. 2, 3, 4, and 5), detailed experimental protocols for protein purification and sedimentation assays beyond brief descriptions, raw data for the phase diagram and concentration measurements, and any statistical analysis of the experimental data. The absence of figures significantly limits the ability to independently evaluate the visual claims regarding tie-line patterns and phase boundaries.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question in the field of biomolecular condensates: whether interactions that drive LLPS are identical to those that stabilize stoichiometric complexes in dilute solution. The authors develop a tractable mean-field theory that couples complex formation to phase separation and derive a clear, testable prediction: a characteristic L-shaped phase boundary with converging tie-lines. The experimental data, however, show diverging tie-lines, which the authors interpret as evidence for auxiliary interactions. The theoretical framework is a valuable contribution, and the experimental approach is logical. However, the manuscript has several significant weaknesses. The comparison between theory and experiment is largely qualitative, relying on visual inspection of tie-line patterns rather than a rigorous quantitative fit. The experimental uncertainties, particularly in the dilute phase concentrations, are acknowledged but not fully addressed. The theoretical model, while useful, makes several simplifying assumptions (e.g., equal lattice site volumes for all species, isotropic interactions) that may limit its quantitative accuracy. The claim that auxiliary interactions are "not yet documented" is a strong statement that requires more careful justification. Overall, the core idea is interesting and the work has potential, but the current presentation does not fully establish the central claim with the rigor expected for a high-impact journal.
- **Who would be interested in the results, and why** Researchers in the fields of biophysics, cell biology, and neuroscience, particularly those studying phase separation, membraneless organelles, and synaptic biology. The theoretical framework for coupling stoichiometric binding to LLPS will be of interest to theorists and experimentalists working on other multi-component condensate systems. The specific application to SynGAP/PSD-95 provides insights into the molecular mechanisms of postsynaptic density assembly, which is relevant to understanding synaptic function and neurological disease.
- **Major strengths**
    1. The manuscript addresses a fundamental and under-explored question: the relationship between dilute-solution binding stoichiometry and condensed-phase interaction networks.
    2. The development of a mean-field theory that explicitly couples a binding equilibrium to LLPS is a novel and valuable theoretical contribution. The model is simple enough to be tractable but captures the essential physics of the problem.
    3. The combination of theory with experimental measurements on a biologically relevant system (SynGAP/PSD-95) strengthens the impact of the work.
    4. The authors are transparent about the limitations of their experimental data and the simplifying assumptions of their model.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of the theory-experiment comparison
- **Claim pointer** The authors claim that the experimentally observed tie-line pattern is inconsistent with the stoichiometric complex-driven LLPS model and consistent with models including auxiliary interactions.
- **Evidence pointer** Results and Discussion section, Figures 2c, 4a, and 5c-e (figures not provided)
- **Concern** The comparison between the theoretical predictions and experimental data is made qualitatively, based on the visual pattern of tie-lines. The authors do not perform a quantitative statistical test to determine whether the experimental tie-line slopes are significantly different from those predicted by the stoichiometric model. The experimental data points show significant scatter, and the theoretical phase boundaries are not overlaid on the experimental data in a way that allows for a rigorous comparison. The claim that the model in Fig. 5e "captures slightly better" the experimental trend than Fig. 5d is subjective and not supported by any quantitative metric.
- **Why it matters** The central conclusion of the paper rests on the distinction between the predicted and observed tie-line patterns. Without a quantitative comparison, it is not possible to assess the strength of the evidence for auxiliary interactions. The reader cannot determine if the discrepancy between theory and experiment is statistically significant or within the range of experimental uncertainty.
- **Resolution test** The authors should perform a quantitative comparison. This could involve: (1) fitting the theoretical models to the experimental data and comparing goodness-of-fit using an appropriate statistical test (e.g., AIC, BIC); (2) calculating the predicted tie-line slopes for the stoichiometric model under a range of parameter values and comparing them to the experimentally measured slopes with error bars; or (3) performing a bootstrap analysis to determine the confidence intervals on the experimental tie-line slopes and checking if the theoretical predictions fall within these intervals.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of the experimental methodology
- **Claim pointer** The authors use a sedimentation-based assay to construct the phase diagram and a confocal fluorescence method to measure condensed-phase PSD-95 concentrations.
- **Evidence pointer** Models, Materials, and Methods section, Figures 3a-e (figures not provided)
- **Concern** The description of the experimental methods is insufficient to fully evaluate the reliability of the data. For the sedimentation assay, the criterion for "phase separation" is defined as the pellet fraction being higher than that of individual proteins alone, but the quantitative threshold is not clear. For the confocal measurements, the authors acknowledge that small droplets are smaller than the optical section thickness, leading to inaccurate concentration measurements, but they do not provide a quantitative estimate of this error or a method to correct for it. The number of replicates for each condition is not stated, and no error bars are shown on the phase diagram or the concentration measurements.
- **Why it matters** The experimental data are the foundation for the central claim of the paper. If the methods are not robust or the uncertainties are not properly characterized, the conclusions drawn from the data are not reliable. The lack of error bars and replicate information makes it impossible to assess the precision and reproducibility of the measurements.
- **Resolution test** The authors should provide a more detailed description of the experimental methods, including: (1) the exact threshold used to define phase separation in the sedimentation assay; (2) the number of independent replicates for each condition; (3) a quantitative analysis of the error in confocal concentration measurements, particularly for small droplets, possibly by comparing measurements from droplets of different sizes; and (4) error bars on all data points in the phase diagram and concentration measurements.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Originality and significance of the theoretical framework
- **Claim pointer** The authors state that their model is a "mean-field LLPS theory of two stoichiometrically constrained solute species" and that it provides a "tractable model" for assessing the role of stoichiometric complexes in LLPS.
- **Evidence pointer** Models, Materials, and Methods section, Equations 1-11
- **Concern** While the model is a useful contribution, its novelty and generality are not fully established. The model makes several strong simplifying assumptions: (1) all species (A, B, and solvent) occupy equal lattice site volumes; (2) the complex A_xB_y is treated as a single entity occupying x+y sites, which may not be physically realistic for large protein complexes; (3) all inter-complex interactions are treated with a single mean-field parameter χ, ignoring the potential for specific, orientation-dependent interactions. The authors do not discuss how these assumptions might affect the generality of their conclusions.
- **Why it matters** The value of a theoretical model lies in its ability to provide insights that are not obvious from intuition and to make predictions that can be tested. If the model is too simplistic, its predictions may be artifacts of the assumptions rather than general features of the system. The authors should discuss the limitations of their model and how its predictions might change if these assumptions were relaxed.
- **Resolution test** The authors should add a discussion section addressing the limitations of their model. They could also perform a sensitivity analysis by varying the model parameters (e.g., the relative sizes of A and B, the number of interaction sites) to see how robust the predicted phase diagram and tie-line patterns are to these changes.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Readability and clarity for a general audience
- **Claim pointer** The manuscript is written for a specialized audience of biophysicists and biochemists.
- **Evidence pointer** Entire manuscript
- **Concern** The manuscript is dense and uses a significant amount of specialized jargon without sufficient explanation for a non-specialist. For example, the concepts of "tie-lines," "Flory-Huggins theory," and "mean-field" are used extensively but are not defined for readers who may not be experts in polymer physics. The significance of the findings for understanding postsynaptic density function could be explained more clearly for a broader neuroscience audience.
- **Why it matters** The work has the potential to be of interest to a wide range of scientists, including neuroscientists and cell biologists. If the manuscript is not accessible to these readers, its impact will be limited. A clear and accessible presentation is essential for a high-impact journal.
- **Resolution test** The authors should revise the manuscript to make it more accessible. This could include: (1) adding a brief introduction to key concepts such as LLPS, tie-lines, and Flory-Huggins theory; (2) providing a more intuitive explanation of the theoretical model and its predictions; and (3) expanding the discussion of the biological implications of the findings for synaptic function.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of writing
- **Affected element** Introduction, Postsynaptic densities section
- **Evidence pointer** "Each PSD is a disc-shaped membraneless protein-rich compartment, an assembly made up of nucleic acids and thousands of different types of proteins Zhu et al. 2016 ; Kaizuka and Takumi 2018 ."
- **Issue** The sentence is grammatically awkward and could be rephrased for clarity.
- **Required correction** Rephrase to something like: "Each PSD is a disc-shaped, membraneless, protein-rich compartment composed of nucleic acids and thousands of different types of proteins."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Consistency of terminology
- **Affected element** Throughout the manuscript
- **Evidence pointer** The terms "auxiliary interactions" and "auxilliary interactions" are both used.
- **Issue** The spelling of "auxiliary" is inconsistent.
- **Required correction** Use the correct spelling "auxiliary" consistently throughout the manuscript.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity of figure references
- **Affected element** Results and Discussion section
- **Evidence pointer** "The predicted phase behaviors are compared with experiments." and "An example of the binary phase diagrams predicted by this model is provided in Fig. 5c."
- **Issue** The text refers to figures, but the figures are not provided in the manuscript text. It is difficult to follow the argument without seeing the figures.
- **Required correction** Ensure that all figures are included and properly referenced in the text. Consider adding more detailed figure legends that explain the key features of the data.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Models, Materials, and Methods section
- **Evidence pointer** "The phase diagram was constructed from the sedimentation-based phase separation assay."
- **Issue** The method for constructing the phase diagram from the sedimentation data is not described in detail. It is unclear how the phase boundary was determined from the discrete data points.
- **Required correction** Provide a more detailed description of how the phase diagram was constructed, including the criteria for determining the phase boundary.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Conclusions section
- **Evidence pointer** "It appears that such LLPS-driving auxilliary interactions are readily available for certain folded proteins, as in the cases of lysozyme and crystallin Cinar et al. 2019 ."
- **Issue** The comparison to lysozyme and crystallin is brief and not fully developed. It would be helpful to discuss the similarities and differences between these systems and the SynGAP/PSD-95 system.
- **Required correction** Expand the discussion of the comparison to other systems to provide more context for the findings.

## Risk / unsupported claims
- The claim that "weaker interactions or higher-order complexes beyond the 3:2 stoichiometry, but not yet documented, are involved in the formation of SynGAP/PSD-95 condensates" is a strong inference from the qualitative comparison of tie-line patterns. It is not directly supported by any experimental evidence identifying such interactions. This claim is plausible but not definitively established by the data presented.
- The statement that the model in Fig. 5e "captures slightly better the tie-line trend in Fig. 4a than the model in Fig. 5d" is subjective and not supported by any quantitative measure of fit.
- The claim that the "combined theoretical-experimental analysis indicates" the presence of auxiliary interactions is based on a single experimental system and a highly simplified theoretical model. The generality of this conclusion is not established.