## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, appendix, footnotes) as provided.
- **Assessment boundary** Scientific content, technical soundness, internal consistency, and support of claims by the evidence presented in the provided text. No external data, figures, or supplementary materials were available for inspection beyond what is described in the text.
- **Shared manuscript claim summary** The authors propose that the architecture of biomolecular condensates formed by the intrinsically disordered N-terminal fragment of yeast Lge1 (Lge1 1-80) can be described across scales by a fractal model whose two key parameters are the interaction valency and the compactness (volume fraction) of individual protein molecules. They combine atomistic molecular dynamics simulations of single- and multi-chain systems with an analytical fractal formalism and in vitro experiments to support this claim.
- **Visible evidence base** Text descriptions of: solubility diagrams and circularity measurements (Figure 1B-D, S1B-D); FRAP recovery dynamics (Figure 1E, S2); pairwise interaction free energy calculations (Figure S1E); single- and multi-chain MD simulations (Figures 2-4, S3, S4); fractal model derivations (Appendix, Figure 5); FracVAL reconstructions (Figure 6). No actual data values, error bars, or statistical outputs are visible in the provided text.
- **Missing materials affecting confidence** All figures, tables, source data files, and supplementary information are referenced but not provided. This includes the technical summary table, source data for Figure 4C, and all numerical values underlying the reported results. Without these, quantitative verification of the central claims is not possible.

## Reviewer
- **Overall assessment** This manuscript presents an ambitious and potentially valuable attempt to connect atomistic simulations of a condensate-forming IDP to mesoscale condensate architecture through a fractal scaling model. The conceptual framework, linking valency and compactness to fractal dimension, is interesting and could be of broad interest to the condensate field. However, the manuscript as presented has significant issues that prevent full evaluation. The central quantitative claims cannot be verified from the text alone, as all numerical data are in inaccessible figures and tables. The logical connection between the MD-derived parameters and the fractal model, while plausible, is not rigorously established. The experimental component is largely descriptive and the link between the FRAP data and the model parameters is speculative. The writing is dense and at times unclear, particularly in the results section where key definitions and statistical tests are missing. The manuscript would benefit from a major revision that makes the evidence base transparent and the arguments more rigorous.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, particularly those interested in the physical chemistry of phase separation, IDP behavior, and multiscale modeling. The fractal framework could be of interest to theorists and simulators working on condensate structure. Experimentalists studying condensate material properties might also find the framework useful for interpreting their data. The work could also appeal to the broader soft matter and colloid science community, given the explicit connection to colloid fractal aggregation.
- **Major strengths**
  - The conceptual idea of using fractal scaling to bridge atomistic and mesoscale descriptions of condensates is novel and potentially impactful.
  - The combination of multiple techniques (MD, analytical theory, in vitro experiments) is ambitious and, in principle, powerful.
  - The explicit connection to colloid physics provides a useful theoretical context.
  - The study addresses an important open question: how do molecular-level interactions determine mesoscale condensate architecture?
- **Major Concerns**
  - **R1-M1** (Blocking): The central quantitative claims are not verifiable from the provided text. All numerical results, including the key parameters φ and n, the fractal dimensions, the Rg values, the diffusion coefficients, and the statistical significance tests, are only described qualitatively and reside in figures, tables, and source data files that were not provided. Without these data, the core argument cannot be assessed.
  - **R1-M2** (Blocking): The logical connection between the MD simulations and the fractal model is not rigorously established. The model assumes constant valency and volume fraction at each iteration, but the MD simulations show dynamic, heterogeneous interactions. The manuscript does not explain how the average values from MD relate to the iterative aggregation process in the model, nor does it address whether the model's assumptions are valid for the simulated system.
  - **R1-M3** (Blocking): The experimental data are presented in a way that does not allow for a critical assessment of the claims. The solubility diagrams, FRAP data, and circularity measurements are described only in words. No quantitative values, error bars, or statistical analyses are provided in the text. The claim that the FRAP data are "consistent with" the model is not supported by any quantitative comparison.
  - **R1-M4** (Major): The manuscript lacks a clear statement of the model's assumptions and limitations. For example, the model assumes spherical clusters, but the reconstructed structures (Figure 6) appear to be highly irregular. The model also assumes that the fractal dimension is constant across scales, but this is not tested. The authors should discuss the range of validity of their model.
  - **R1-M5** (Major): The writing is often unclear and imprecise. For example, the term "dynamic interaction mode" is used without a clear definition. The description of the "symmetry breaking" between intra- and intermolecular interactions is confusing. The methods section is too brief to allow for replication of the simulations or the analysis.
- **Minor Comments**
  - **R1-m1**: The abstract is overly long and contains too much detail. It should be streamlined to focus on the main findings.
  - **R1-m2**: The introduction is too long and could be more focused. The connection to colloid physics is made late in the introduction and could be introduced earlier.
  - **R1-m3**: The use of "Lge1 1-80" is inconsistent; sometimes it is written as "Lge1 1-80" and sometimes as "Lge 1-80". Please be consistent.
  - **R1-m4**: The figure legends are not provided, making it impossible to understand what is being shown in the figures.
  - **R1-m5**: The discussion of the FRAP data is speculative. The authors should be more careful in attributing the observed recovery dynamics to specific molecular mechanisms.
  - **R1-m6**: The appendix is difficult to follow. The derivation of the fractal model should be presented more clearly, with all steps explicitly shown.
  - **R1-m7**: The authors should provide a clear definition of "valency" and "compactness" as used in the model, and explain how they are calculated from the MD simulations.
  - **R1-m8**: The manuscript would benefit from a schematic figure that summarizes the overall workflow and the relationship between the different components (MD, model, experiments).
- **Technical failings that need to be addressed before the case is established**
  - R1-M1, R1-M2, R1-M3 (as detailed above). The case is not established from the provided evidence.
- **Assessment against Nature-style criteria**
  - **Originality**: The fractal scaling approach to condensate architecture is a novel contribution. The idea of linking valency and compactness to fractal dimension is not present in the existing literature to my knowledge. This is a strength.
  - **Scientific importance**: The question of how molecular interactions determine mesoscale condensate structure is of high importance to the condensate field. If the framework is validated, it could provide a new way to think about condensate organization. However, the current evidence is insufficient to establish this importance.
  - **Interdisciplinary readership**: The work has the potential to appeal to a broad readership, including biophysicists, cell biologists, and soft matter physicists. The connection to colloid science is a plus. However, the dense writing and lack of clear explanations may limit accessibility.
  - **Technical soundness**: The technical soundness cannot be fully assessed due to the lack of data. The MD simulation methodology appears standard, but the analysis is not described in sufficient detail. The fractal model derivation is plausible but not fully rigorous. The experimental methods are standard but the data are not presented.
  - **Readability for nonspecialists**: The manuscript is not easily readable for nonspecialists. The introduction is dense, the results are described in a way that assumes significant prior knowledge, and the methods are too brief. A significant revision is needed to improve clarity.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript has a potentially interesting core idea, but the lack of accessible data and the unclear logical connections between the different components prevent a positive recommendation. A major revision that addresses the blocking concerns is required before the case can be made.

## Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence availability and verifiability
- **Claim pointer** The manuscript claims that MD simulations yield specific values for valency (approximately 4 for WT) and compactness (φ), and that these values, when used in the fractal model, predict the observed condensate architecture and fractal dimensions.
- **Evidence pointer** Figures 2D, 4A, 4B, 5B, 5C, 6, S3, S4, S5, S6; Technical summary table; Source Data 4C. All are referenced but not provided.
- **Concern** The entire quantitative basis of the paper is hidden in figures and tables that are not available for review. The reader cannot verify the reported values of valency, compactness, fractal dimension, Rg, diffusion coefficients, or any statistical significance. The claim that the model predictions "agree" with simulations and experiments cannot be checked. This is a fundamental issue that prevents any meaningful evaluation of the scientific claims.
- **Why it matters** A scientific paper must present its evidence in a form that allows the reader to assess the validity of the claims. Without the underlying data, the claims are unverifiable assertions. This is particularly critical here, as the entire argument rests on a quantitative comparison between simulations, theory, and experiments.
- **Resolution test** The authors must provide all numerical data, including the values of φ and n for all systems, the fractal dimensions, the Rg distributions, the diffusion coefficients, and the statistical tests, either in the main text, in accessible tables, or in a clearly described and accessible supplementary data file. The figures must be accompanied by complete legends that explain what is shown and how the data were analyzed.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Logical rigor and model validity
- **Claim pointer** The manuscript claims that the fractal model, using MD-derived values of valency and compactness, can describe condensate architecture across scales, and that the fractal dimension is a function of these two parameters.
- **Evidence pointer** Results section "Describing condensate architecture via a fractal scaling model"; Appendix; Figure 5.
- **Concern** The connection between the MD simulations and the fractal model is not rigorously established. The model assumes a specific iterative aggregation process with constant valency and volume fraction. However, the MD simulations show that interactions are dynamic and heterogeneous, with different regions of the protein engaging in different types of contacts. The manuscript does not explain how the average valency and compactness from the MD simulations map onto the model's parameters, nor does it justify the assumption of constant values at each iteration. The model also assumes spherical clusters, which is inconsistent with the irregular structures shown in Figure 6. The derivation of the model in the Appendix is not fully clear, and the relationship between the model's parameters and the fractal dimension is not derived in a transparent way.
- **Why it matters** The central claim of the paper is that the fractal model provides a valid description of condensate architecture. If the connection between the simulations and the model is not rigorous, the claim is not supported. The model's assumptions must be explicitly stated and justified, and the limits of its validity must be discussed.
- **Resolution test** The authors must provide a clear and detailed derivation of the fractal model, including all assumptions. They must explain how the MD-derived values of φ and n are used in the model, and why the model's assumptions are valid for the simulated system. They should also discuss the limitations of the model, including the assumption of spherical clusters and constant parameters.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental data support
- **Claim pointer** The manuscript claims that the fractal dimensions of WT, R>K, and Y>A condensates, as derived from the model, agree with their in vitro morphologies, and that the FRAP data are consistent with the model's predictions.
- **Evidence pointer** Results section "Lge1 1-80 LLPS critically depends on tyrosine residues"; Figures 1B-E, S1B-D, S2; Discussion.
- **Concern** The experimental data are presented in a purely descriptive manner. No quantitative values are given for the solubility diagrams, the circularity measurements, or the FRAP recovery times. The claim that the model's predictions "agree" with the experimental observations is not supported by any quantitative comparison. For example, the statement that the WT condensate has a fractal dimension of 2.42 and is "experimentally found to undergo robust phase separation" is not a quantitative validation. The FRAP data are interpreted in a speculative manner, with the authors attributing the recovery dynamics to specific molecular mechanisms without providing evidence for these attributions.
- **Why it matters** The experimental data are a key part of the paper's evidence base. Without quantitative data and statistical analysis, the claims of agreement between theory and experiment are not substantiated. The interpretation of the FRAP data is particularly problematic, as it is not clear how the recovery dynamics relate to the model's parameters.
- **Resolution test** The authors must provide quantitative data for all experimental measurements, including the solubility boundaries, the circularity values, and the FRAP recovery times, with appropriate error bars and statistical tests. They must also provide a more rigorous and quantitative comparison between the model's predictions and the experimental observations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Model assumptions and limitations
- **Claim pointer** The manuscript claims that the fractal model provides a general framework for describing condensate architecture across scales.
- **Evidence pointer** Discussion; Figure 5; Figure 6.
- **Concern** The manuscript does not adequately discuss the assumptions and limitations of the fractal model. For example, the model assumes that the fractal dimension is constant across scales, but this is not tested. The model also assumes that the condensate is a homogeneous fractal, but the reconstructed structures show significant heterogeneity and voids. The authors should discuss the range of validity of their model and the conditions under which it might break down.
- **Why it matters** A model that is presented as a general framework must be accompanied by a clear statement of its limitations. Without this, the reader cannot assess the applicability of the model to other systems.
- **Resolution test** The authors should add a section to the Discussion that explicitly addresses the assumptions and limitations of the model, including the range of scales over which it is valid, the effect of polydispersity, and the role of specific interactions.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Clarity and precision of writing
- **Claim pointer** The manuscript claims to provide a "multiscale description" and a "general, experimentally testable framework".
- **Evidence pointer** Throughout the manuscript, particularly in the Results and Discussion sections.
- **Concern** The writing is often unclear and imprecise. Terms such as "dynamic interaction mode" and "symmetry breaking" are used without clear definitions. The description of the relationship between the MD simulations, the fractal model, and the experiments is difficult to follow. The methods section is too brief to allow for replication. The manuscript would benefit from a thorough revision to improve clarity and precision.
- **Why it matters** A paper that is difficult to read is less likely to have an impact. The lack of clarity also makes it difficult to assess the validity of the claims.
- **Resolution test** The authors should revise the manuscript to improve clarity. They should define all technical terms, provide a clear and logical flow of arguments, and expand the methods section to allow for replication.

## Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract is overly long and contains too much detail, making it difficult to identify the main findings.
- **Required correction** The abstract should be streamlined to focus on the key question, the main result, and the significance of the work.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Introduction
- **Evidence pointer** Introduction
- **Issue** The introduction is too long and covers too much background material. The connection to colloid physics is made late and could be introduced earlier to provide a clearer framework.
- **Required correction** The introduction should be shortened and focused. The colloid physics connection should be introduced earlier to set the stage for the model.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Nomenclature
- **Evidence pointer** Throughout the text
- **Issue** The protein fragment is referred to as both "Lge1 1-80" and "Lge 1-80" in different places.
- **Required correction** Use a consistent nomenclature throughout the manuscript.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figures
- **Evidence pointer** All figures
- **Issue** Figure legends are not provided, making it impossible to understand what is being shown.
- **Required correction** Provide complete and detailed figure legends for all figures.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion of FRAP data
- **Evidence pointer** Results section "Lge1 1-80 LLCP critically depends on tyrosine residues"; Figure 1E, S2
- **Issue** The interpretation of the FRAP data is speculative. The authors attribute the recovery dynamics to specific molecular mechanisms without providing evidence for these attributions.
- **Required correction** The authors should be more cautious in their interpretation of the FRAP data and should discuss alternative explanations.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Appendix
- **Evidence pointer** Appendix
- **Issue** The derivation of the fractal model in the Appendix is difficult to follow. The steps are not clearly explained.
- **Required correction** The derivation should be rewritten to be more transparent, with all steps explicitly shown and explained.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods
- **Evidence pointer** Methods section
- **Issue** The methods section is too brief and does not provide sufficient detail for replication.
- **Required correction** The methods section should be expanded to include all necessary details of the simulations, the analysis, and the experiments.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Overall manuscript
- **Evidence pointer** Throughout
- **Issue** The manuscript would benefit from a schematic figure that summarizes the overall workflow and the relationship between the different components (MD, model, experiments).
- **Required correction** Add a schematic figure to help the reader understand the overall approach.

## Risk / unsupported claims
- The claim that the fractal model provides a "general, experimentally testable framework" is not supported by the evidence presented, as the model is only tested on a single system (Lge1 1-80).
- The claim that the FRAP data are "consistent with" the model is unsupported, as no quantitative comparison is provided.
- The claim that the MD simulations reproduce the "key determinants" of condensate formation is not fully supported, as the simulations are limited to a single concentration and timescale.
- The claim that the fractal dimension is a function of valency and compactness is not rigorously derived or tested.
- The claim that the model can describe condensate architecture "across scales" is not fully supported, as the model is only tested at the nanometer and micrometer scales, and the connection between these scales is not rigorously established.