## Review setup
- **Input scope** Full manuscript text (abstract, main text, discussion, acknowledgments) as provided; no figures, tables, extended data, supplementary materials, or methods section were included in the supplied material.
- **Assessment boundary** Scientific claims, experimental design as described, interpretation of results, and alignment with stated conclusions. No assessment of data quality, statistical validity, or reproducibility is possible beyond what is described in the text.
- **Shared manuscript claim summary** The authors claim that single-fluorogen imaging, combining super-resolution localization microscopy and single-molecule tracking, reveals that biomolecular condensates are internally hydrophobic, spatially inhomogeneous at the nanoscale, and contain slow-moving nanoscale hubs coexisting with fast-moving molecules. They further claim that fluorogen orientation measurements at condensate interfaces reveal distinct interfacial features, and that these observations provide a structural and dynamical basis for condensate viscoelasticity.
- **Visible evidence base** Text descriptions of results, references to figures (Fig. 2, 3, 4, 5, 6), extended data figures, supplementary movies, and simulations. No actual data, images, or quantitative values are provided in the supplied material.
- **Missing materials affecting confidence** All figures, extended data, supplementary materials, methods section, and quantitative data (e.g., exact values for excess variance, burst durations, speeds, and statistical tests) are absent. The simulations referenced (LaSSI) are described but not presented. Without these, the strength of the evidence cannot be independently verified.

## Reviewer
- **Overall assessment** The manuscript presents an innovative application of single-fluorogen imaging to probe the internal and interfacial properties of biomolecular condensates. The conceptual framework, linking fluorogen photophysics to condensate microenvironment and molecular organization, is compelling and timely. However, the provided text alone is insufficient to evaluate the robustness of the claims. The absence of methods, quantitative data, and figures prevents verification of the central conclusions. The manuscript would benefit from clearer articulation of how the fluorogen signals map onto specific molecular features, and from explicit acknowledgment of the interpretive leap from fluorogen behavior to protein network structure.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, biophysics of intrinsically disordered proteins, and single-molecule imaging. The work bridges experimental single-molecule techniques with computational predictions, making it relevant to both experimentalists and theorists studying the material properties of condensates and their role in cellular organization.
- **Major strengths** The use of multiple fluorogens with distinct environmental sensitivities is a creative and powerful approach. The combination of super-resolution localization and single-molecule tracking within the same system provides complementary information. The connection to simulations (LaSSI) and the proposal that nanoscale hubs correspond to physically crosslinked sticker networks is a testable and mechanistically grounded hypothesis. The extension to interfacial orientation measurements using SMOLM is novel and adds a new dimension to condensate characterization.
- **Major Concerns** The central claims rest on the interpretation of fluorogen blinking and mobility as direct readouts of protein network structure. This interpretation requires validation that is not fully described in the text. The quantitative basis for distinguishing "hubs" from random density fluctuations is mentioned but not detailed. The relationship between fluorogen burst duration and the physical properties of the local environment is asserted but not mechanistically explained. The claim that the findings provide a "structural and dynamical basis for viscoelasticity" is a significant extrapolation that is not directly supported by the data described.
- **Minor Comments** The manuscript would benefit from a more explicit statement of the limitations of fluorogen-based reporting. The discussion of the relationship between nanoscale inhomogeneities and macroscopic viscoelasticity is speculative and could be more carefully framed. The use of terms such as "hubs" and "sponge-like" is evocative but would benefit from operational definitions.
- **Technical failings that need to be addressed before the case is established** The absence of the methods section and quantitative data is a critical gap. The manuscript cannot be assessed for technical soundness without these. The statistical treatment of the excess variance and clustering coefficients is not described. The control experiments needed to rule out artifacts from fluorogen photophysics or dye-induced perturbations are not mentioned.
- **Assessment against Nature-style criteria**  
  - Originality: High. The application of single-fluorogen imaging to map nanoscale inhomogeneities and interfacial features of condensates is novel and extends beyond prior work.  
  - Scientific importance: High. The findings address a central question in the condensate field regarding the internal organization and material properties of these structures.  
  - Interdisciplinary readership: Moderate to high. The work will appeal to biophysicists, cell biologists, and soft matter physicists, but the technical detail may limit accessibility to a broader audience.  
  - Technical soundness: Not assessable from the provided material. The lack of methods and data prevents evaluation.  
  - Readability for nonspecialists: The text is generally clear but relies on specialized terminology and concepts that may be challenging for readers outside the field. A more accessible introduction to fluorogen photophysics and condensate physics would improve readability.
- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual framework and experimental approach are promising, but the current submission does not provide sufficient evidence to establish the central claims. A revised version with full methods, quantitative data, and explicit validation of the fluorogen-to-structure interpretation would be needed.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The manuscript claims that "the internal environments of condensates are more hydrophobic than coexisting dilute phases" and that "molecules within condensates are organized in a spatially inhomogeneous manner."  
- **Evidence pointer** Abstract; main text sections "Single-molecule imaging shows that spatial inhomogeneities extend down to the nanoscale" and "Single-molecule tracking shows slow moving nanoscale hubs that coexist with fast moving molecules."  
- **Concern** The claims of hydrophobicity and spatial inhomogeneity are based on fluorogen blinking and mobility patterns, but the text does not provide quantitative data or a detailed description of how these patterns are converted into measures of hydrophobicity or inhomogeneity. The excess variance metric is mentioned, but the threshold for significance and the statistical framework are not described.  
- **Why it matters** Without quantitative evidence and a clear analytical pipeline, the reader cannot assess whether the observed fluorogen behavior genuinely reflects the properties of the condensate or is an artifact of the imaging method.  
- **Resolution test** Provide the methods section, including the calculation of excess variance, the definition of clustering coefficients, and the statistical tests used. Include representative data with error bars and a demonstration that the observed inhomogeneities are not present in control samples or in simulations of homogeneous distributions.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Interpretive validity  
- **Claim pointer** The manuscript claims that "nanoscale hubs uncovered using NR and NB are direct readouts of networked Aro-LCD molecules formed via reversible, intermolecular physical crosslinks among aromatic stickers."  
- **Evidence pointer** Main text section "Single-molecule tracking shows slow moving nanoscale hubs that coexist with fast moving molecules" and "Valence of aromatic residues impacts nanoscale dynamics of PLCDs within condensates."  
- **Concern** The link between fluorogen behavior and the molecular structure of the condensate is inferred from simulations, but the text does not provide a direct experimental validation of this link. The simulations are referenced but not described in sufficient detail to evaluate their relevance. The possibility that fluorogen dynamics are influenced by factors other than protein crosslinking, such as dye aggregation or photophysical effects, is not addressed.  
- **Why it matters** The central mechanistic conclusion of the paper depends on this interpretation. If the fluorogen signal is not a faithful reporter of protein network structure, the conclusions about viscoelasticity and molecular organization are unsupported.  
- **Resolution test** Include control experiments with fluorogens that do not bind to aromatic residues, or with condensates formed by proteins lacking aromatic stickers. Provide a more detailed description of the simulations and how they are used to interpret the experimental data.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** No  
- **Axis** Generalizability  
- **Claim pointer** The manuscript claims that "the picture that emerges from single fluorogen imaging may be summarized as follows: The interiors of condensates are more hydrophobic than the coexisting dilute phases" and that this is a general feature of condensates.  
- **Evidence pointer** Discussion section.  
- **Concern** The experiments are performed on a limited set of condensates (Aro-LCD variants and DDX4), and the text does not discuss whether the findings extend to other types of condensates, such as those formed by RNA or by different classes of proteins. The claim of generality is therefore not supported by the data presented.  
- **Why it matters** The manuscript positions the findings as broadly applicable to biomolecular condensates, but the evidence base is narrow. Overgeneralization could mislead readers about the universality of the observed phenomena.  
- **Resolution test** Either limit the claims to the specific systems studied or include additional experiments on a wider range of condensate types.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Quantitative rigor  
- **Claim pointer** The manuscript claims that "Aro+ exhibits the highest δ value, with a mean of 61°, while Aro− and WT have similar mean values of δ, which are 57° and 56°, respectively."  
- **Evidence pointer** Main text section "Single-molecule orientation localization microscopy reveals distinct features of interfaces."  
- **Concern** The differences in δ values between conditions are small (4-5 degrees), and the text does not report the variability or statistical significance of these differences. Without this information, it is unclear whether the observed differences are meaningful.  
- **Why it matters** The claim that Aro+ has a distinct interfacial orientation preference is a key result, but the small effect size and lack of statistical reporting undermine confidence in this conclusion.  
- **Resolution test** Report the number of measurements, the standard deviation or confidence intervals, and the results of appropriate statistical tests for the δ values.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Terminology  
- **Evidence pointer** Main text, "hubs" and "sponge-like"  
- **Issue** The terms "hubs" and "sponge-like" are used to describe the observed structures, but they are not formally defined.  
- **Required correction** Provide operational definitions of these terms, ideally with reference to the quantitative metrics used to identify them.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Discussion of limitations  
- **Evidence pointer** Discussion section  
- **Issue** The manuscript does not discuss potential artifacts or limitations of the fluorogen approach, such as dye-induced perturbations of the condensate or the influence of dye concentration on the measurements.  
- **Required correction** Add a paragraph acknowledging these limitations and describing any controls performed to address them.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Accessibility  
- **Affected element** Introduction to fluorogen photophysics  
- **Evidence pointer** Abstract and first results section  
- **Issue** The mechanism by which fluorogens are turned on in hydrophobic environments is not explained for readers unfamiliar with this class of dyes.  
- **Required correction** Add a brief explanation of the solvatochromic effect and how it is exploited in this study.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Simulation details  
- **Evidence pointer** Main text sections referencing LaSSI simulations  
- **Issue** The simulations are referenced but not described in sufficient detail for a reader to understand how they were performed or how they relate to the experimental conditions.  
- **Required correction** Provide a summary of the simulation parameters and a description of how the simulation results are compared to the experimental data.

## Risk / unsupported claims
- The claim that "the internal environments of condensates are more hydrophobic than coexisting dilute phases" is not supported by quantitative data in the provided text.
- The claim that "nanoscale hubs" correspond to "clusters of proteins that define distinctive local environments" is an interpretation that is not directly validated.
- The claim that the findings provide a "structural and dynamical basis for the viscoelasticity of condensates" is a significant extrapolation that is not directly supported by the data described.
- The claim that "dynamical inhomogeneities within condensates are likely to be the signatures of spatial inhomogeneities that result from phase separation coupled to percolation" is speculative and not directly tested.
- The generalizability of the findings to condensates beyond the specific systems studied is not established.