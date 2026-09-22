## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary information references.
- **Assessment boundary** Scientific validity, methodological rigor, interpretation of results, and alignment with claims made in the abstract and discussion.
- **Shared manuscript claim summary** The authors present a coarse-grained molecular dynamics simulation study of adenylate kinase (AdK) under molecular crowding, proposing a mechanism of crowding-induced allosteric regulation of enzymatic catalysis. They claim that crowding can either enhance or suppress enzymatic activity depending on the enzyme's intrinsic conformational propensity and the rate-limiting step of the catalytic cycle.
- **Visible evidence base** Simulation results presented in Figures 1-7, supplementary figures S1-S5, and supplementary table S1. Methodological details in the Methods section.
- **Missing materials affecting confidence** Supplementary information referenced but not fully provided in the submitted material. Experimental validation data not included. Details of model parameterization for variants not fully described.

## Reviewer
- **Overall assessment** This manuscript presents a computational study using a residue-resolved coarse-grained model to investigate the effects of molecular crowding on the enzymatic cycle of adenylate kinase. The work addresses an important and timely question in biophysics, given the growing recognition of the role of cellular crowding in enzyme function. The authors develop a framework that explicitly couples conformational dynamics, ligand binding, and chemical conversion under crowding conditions. The central finding, that crowding can either enhance or suppress activity depending on the rate-limiting step, is conceptually interesting and potentially significant. However, several technical concerns regarding model validation, parameterization, and interpretation of results need to be addressed before the conclusions can be fully supported.

- **Who would be interested in the results, and why** Researchers in biophysics, enzymology, and cellular biochemistry would find this work relevant. Those studying enzyme kinetics in cellular contexts, protein conformational dynamics, and the physical chemistry of crowded environments would be particularly interested. The computational framework may also be of interest to those developing multiscale simulation approaches for enzyme catalysis.

- **Major strengths** The manuscript addresses a complex and poorly understood problem with a computationally tractable approach. The explicit modeling of the full catalytic cycle, rather than isolated steps, is a notable strength. The systematic exploration of conformational propensity as a key variable is well conceived. The authors are appropriately cautious in acknowledging limitations of their minimal crowding model.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that the model reproduces experimentally measured closed-state population (Pclosed = 0.3) and that variants with different Pclosed values represent meaningful perturbations of enzyme conformational propensity.
- **Evidence pointer** Methods section, "Dynamic energy landscape model of enzyme catalysis"; Figure 5B; Supplementary Table S1
- **Concern** The calibration of ΔV parameters to match Pclosed = 0.3 for the wild-type is described, but the procedure for generating variants with different Pclosed values is not fully detailed. Specifically, how are the ΔV values chosen for variants with Pclosed = 0.003, 0.01, 0.05, etc.? Is there a systematic relationship between ΔV and Pclosed? Without this information, it is difficult to assess whether the variants represent physically realistic perturbations or arbitrary model adjustments. Additionally, the relationship between Pclosed in the apo state and the actual catalytic competence of the enzyme-substrate complex is not established. The authors should clarify how Pclosed in the apo state relates to the population of the closed state when substrates are bound.
- **Why it matters** The central conclusion of the paper, that crowding effects depend on the rate-limiting step and conformational propensity, rests on the validity of these variant models. If the variants are not physically meaningful, the conclusions may be artifacts of the model construction rather than general principles.
- **Resolution test** Provide a detailed description of how ΔV values are systematically varied to produce the range of Pclosed values used. Show that the relationship between ΔV and Pclosed is monotonic and physically reasonable. Ideally, validate the variant approach by comparing to known AdK mutants with altered conformational equilibria.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that the model captures the rate-limiting step correctly, particularly the assertion that product release is rate-limiting for wild-type AdK at moderate and high substrate concentrations.
- **Evidence pointer** Results section, "Effect of molecular crowding on the individual steps in the enzymatic cycle"; Figure 6
- **Concern** The model uses experimentally determined forward and reverse catalytic rates (kf and kr) for the chemical step, but the conformational dynamics are simulated with a coarse-grained model. The timescale mapping is based on matching apo-state conformational transition rates to experimental data. However, the authors do not demonstrate that the relative timescales of conformational transitions, ligand binding, and chemical conversion are correctly captured. If the conformational dynamics are too fast or too slow relative to the chemical step, the identified rate-limiting steps could be incorrect. The authors should provide evidence that the model reproduces known kinetic features of AdK, such as the overall turnover rate in dilute solution, and that the rate-limiting step assignment is robust.
- **Why it matters** The interpretation of crowding effects on activity depends critically on which step is rate-limiting. If the model misidentifies the rate-limiting step, the conclusions about crowding enhancement or suppression would be incorrect.
- **Resolution test** Compare model predictions for turnover rates and rate-limiting steps in dilute solution to experimental data for wild-type AdK. Perform sensitivity analysis on the relative timescales of conformational dynamics and chemical conversion to show that conclusions are robust to reasonable variations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The claim that the results provide a general framework for understanding diverse experimental observations of crowding effects on enzyme catalysis.
- **Evidence pointer** Discussion section; Abstract
- **Concern** The study uses a single enzyme (AdK) with a minimal crowding model (hard-sphere repulsion). The authors acknowledge this limitation but still make broad claims about explaining the diversity of experimental observations. The model does not account for soft interactions, crowder heterogeneity, or specific chemical effects that are known to be important in experimental systems. The claim that the framework can explain diverse observations is not directly supported by the data presented, as no direct comparison to specific experimental systems is made.
- **Why it matters** The significance of the work depends on its ability to provide insight into real biological systems. Without demonstrating relevance to specific experimental observations, the broader implications remain speculative.
- **Resolution test** Discuss specific experimental systems where the predicted effects could be tested. If possible, perform simulations with parameters relevant to a specific experimental system and compare predictions to measured activities.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The claim that soft crowding with attractive interactions can enhance activity for closed-biased variants beyond dilute-solution levels.
- **Evidence pointer** Results section, "Impact of crowder size and soft crowder interactions on enzyme dynamics"; Supplementary Figures S3, S4
- **Concern** The results for soft crowding are presented in supplementary figures only, with limited description in the main text. The mechanism by which attractive interactions enhance activity for closed-biased variants is not explained. The authors state that attraction "compensates the entropic effect" but do not provide a mechanistic explanation. Additionally, the range of attraction strengths tested and the physical relevance of these values to real cellular conditions are not discussed.
- **Why it matters** The soft crowding results add complexity to the story but are not well integrated into the main conclusions. Without a clear mechanistic explanation, these results are difficult to interpret and may distract from the main message.
- **Resolution test** Provide a mechanistic explanation for the observed effects of soft crowding. Discuss the physical relevance of the attraction strengths used. Consider whether these results should be more prominently featured or appropriately de-emphasized.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraphs 1-2
- **Issue** The introduction provides a good overview of crowding effects but could be more accessible to readers unfamiliar with the field. Some terms, such as "volume exclusion" and "conformational selection," are used without brief definitions.
- **Required correction** Add brief explanations of key concepts for nonspecialist readers.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, "Modeling the molecular crowding environment"
- **Evidence pointer** Methods section, equation 7
- **Issue** The choice of crowder radius (8 Å) is justified, but the relationship between this radius and the protein size is not discussed. The ratio of crowder to protein size is known to affect the nature of crowding effects.
- **Required correction** Add a brief discussion of how the crowder size relative to the protein might affect the results and whether the conclusions are expected to hold for larger crowders.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, "Effect of molecular crowding on enzyme activity of wild type AdK"
- **Evidence pointer** Figure 2
- **Issue** The error bars in Figure 2 are described as determined using bootstrapping, but the number of bootstrap samples and the method of resampling are not specified.
- **Required correction** Provide details of the bootstrap procedure in the Methods section.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Discussion
- **Evidence pointer** Discussion, paragraph 2
- **Issue** The discussion of soft crowding effects is brief and could benefit from a clearer summary of the key findings and their implications.
- **Required correction** Expand the discussion of soft crowding results to provide a clearer take-home message.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, "Dynamic energy landscape model of enzyme catalysis"
- **Evidence pointer** Methods section, equation 5
- **Issue** The functional form of f(S) is given, but the values of S0 and σS are not provided in the main text. These are presumably in the supplementary materials, but should be stated for completeness.
- **Required correction** Provide the values of S0 and σS in the main text or explicitly reference the supplementary table where they are given.

- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3

- **Assessment against Nature-style criteria** 
  - Originality: The work presents a novel computational framework for studying full enzymatic cycles under crowding, which is a methodological advance. The concept of crowding effects depending on rate-limiting steps is not entirely new but is applied here in a systematic way.
  - Scientific importance: The question of how crowding affects enzyme function is of broad importance in cellular biochemistry. The potential to explain diverse experimental observations is significant, though not fully realized in this manuscript.
  - Interdisciplinary readership: The topic bridges biophysics, enzymology, and cell biology, and should appeal to a broad readership. The writing is generally accessible, though some sections may be challenging for nonspecialists.
  - Technical soundness: The model is based on established coarse-grained approaches, but several technical aspects require clarification and validation, as detailed in the major concerns.
  - Readability for nonspecialists: The manuscript is generally well-written, but the introduction and discussion could be improved to make the concepts more accessible to a broader audience.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important problem and presents a potentially valuable computational framework. However, the major concerns regarding model validation and interpretation must be addressed before the conclusions can be fully supported.

## Risk / unsupported claims
- The claim that the framework can explain the diversity of experimental observations of crowding effects is not directly supported by comparisons to specific experimental systems.
- The claim that soft crowding can enhance activity beyond dilute-solution levels for closed-biased variants is based on limited analysis and lacks mechanistic explanation.
- The assertion that the model correctly identifies rate-limiting steps is not validated against experimental kinetic data beyond the apo-state conformational transition rates.
- The relationship between Pclosed in the apo state and catalytic competence in the substrate-bound state is not established.