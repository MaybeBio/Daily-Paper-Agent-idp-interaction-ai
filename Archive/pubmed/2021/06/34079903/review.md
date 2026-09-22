## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results and discussion, and future outlook sections. No supplementary information, figures, or tables were provided.
- **Assessment boundary** Evaluation is limited to the claims and evidence presented in the supplied text. Claims referencing figures, tables, or supplementary information are assessed as "not verifiable" where the referenced materials are absent.
- **Shared manuscript claim summary** The authors propose that heterogeneous charged complexes formed by two oppositely charged random copolymers can segregate a range of organic molecules from water. They report experimental dye removal efficiencies and use coarse-grained simulations to explain the role of nanoscale charge and hydrophobicity heterogeneity in this process.
- **Visible evidence base** Text descriptions of polymer synthesis and characterization, dye filtration experiments, and two coarse-grained simulation models. References to Figure 1, Figure 2, Figure 3, Figure 4, Figure 5, Table 1, and Supplementary Information (Figures S2–S4, Table S4) are made but the actual data are not available for inspection.
- **Missing materials affecting confidence** All figures, tables, and supplementary information. Experimental protocols for dye quantification, PFOA analysis, and filtration procedures are only partially described. Simulation parameters, force field details, and analysis methods are not fully specified.

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting approach to water remediation using random copolymer complexes, with a plausible mechanistic hypothesis supported by preliminary experimental and simulation data. However, the absence of all primary data (figures, tables, SI) prevents a rigorous evaluation of the central claims. The experimental section lacks quantitative details on reproducibility, controls, and error analysis. The simulation section, while thoughtfully designed, is not fully described in terms of model validation and parameter choices. The work has potential but is not yet established from the provided evidence.
- **Who would be interested in the results, and why** Researchers in polymer science, water treatment and environmental remediation, and soft matter physics would find this work relevant. The demonstration of a simple, scalable method for removing organic contaminants, including PFOA, could appeal to applied scientists and engineers. The mechanistic insights into charge heterogeneity in polyelectrolyte complexes may interest theorists and simulators in the biomimetic materials community.
- **Major strengths** The hypothesis is clearly stated and builds logically on prior work. The combination of experiments and simulations is appropriate for the research question. The choice of model dyes with different charge and hydrophobicity characteristics is thoughtful. The potential practical relevance, particularly for PFOA removal, is significant. The discussion of non-stoichiometric charge ratios and charge heterogeneity is intellectually engaging.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The manuscript claims that the polyelectrolyte complexes are capable of absorbing small cationic, anionic, and hydrophobic organic molecules, with quantitative removal efficiencies reported for crystal violet (>99.5%), phenolphthalein (>98%), methyl orange (65 ± 5%), and PFOA (63.0 ± 0.5% for single filtration, 89.0 ± 0.5% after three filtrations).
  - **Evidence pointer** Figure 2(a), location not provided
  - **Concern** The quantitative removal efficiencies are central to the manuscript's main claim, but the actual data in Figure 2(a) are not available for review. The text does not describe the calibration curve details, the number of replicates, the standard deviation calculation, or the detection limits for the UV–vis measurements. For PFOA, the LC–MS method is mentioned but no details on sample preparation, internal standards, or quantification limits are given.
  - **Why it matters** Without access to the primary data and experimental details, it is impossible to assess the reliability and statistical significance of the reported removal efficiencies. The claim that crystal violet removal is "quantitative" reaching "the detection limit of the instrument" requires supporting data to confirm this is not an artifact of the measurement method.
  - **Resolution test** Provide Figure 2(a) with error bars, the number of independent replicates, calibration curve parameters, and detection limits. For PFOA, provide full LC–MS method details including recovery rates and matrix effects.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The manuscript states that the anionic copolymer forms micelles with hydrophobic cores, and that these structures persist within the polyelectrolyte complexes, providing binding sites for organic molecules.
  - **Evidence pointer** Figure 2(b–d), Figure S2, location not provided
  - **Concern** The solvatochromic shift evidence for crystal violet is described in the text, but the actual spectra are not shown. The claim that the shift is "retained" in the complex (Figure 2c) is critical for the mechanism, but the data are not available. The simulation results supporting micelle formation are referenced to Figure S2, which is not provided. The text does not specify how the micelle size, aggregation number, or core dimensions were determined from the simulations.
  - **Why it matters** The proposed mechanism relies on the existence of hydrophobic domains within the complexes. If the experimental evidence for these domains is weak or the simulation model is not validated, the mechanistic explanation is undermined.
  - **Resolution test** Provide the UV–vis spectra showing the solvatochromic shifts, with appropriate controls. Provide the simulation data in Figure S2 with a description of how micelles were identified and characterized. Include a validation of the coarse-grained model against experimental data where possible.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Reproducibility
  - **Claim pointer** The manuscript describes a titration procedure to determine the amounts of copolymer solutions used, with macroscopic flocculation occurring at a specific volume of cationic polymer added, corresponding to a positive-to-negative charge ratio of 2.9–3.3:1.
  - **Evidence pointer** Results and Discussion, "Polyelectrolyte Complex Formation and Dye Filtration", location not provided
  - **Concern** The titration procedure is described in words but no data are shown. The charge ratio is stated as 2.9–3.3:1, but the calculation method is not explained. The text mentions that the amount of cationic polymer needed changes for phenolphthalein (240 μL vs 220 μL) due to "a slight salt concentration of about 1 mM NaCl," but this is speculative and not supported by data. The reproducibility of the flocculation point across different batches of polymers is not addressed.
  - **Why it matters** The charge ratio is a key parameter for understanding the complex formation and its heterogeneity. If the titration is not reproducible or the charge ratio calculation is not transparent, the experimental foundation is weakened.
  - **Resolution test** Provide a titration curve showing the flocculation point, the method for calculating charge ratios from polymer compositions, and data on batch-to-batch variability. Address the salt concentration effect with controlled experiments.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scope of claim
  - **Claim pointer** The manuscript claims that the method can segregate "a wide range of organic molecules" and that the heterogeneity of the complex is important for this generality.
  - **Evidence pointer** Figure 5(a), location not provided
  - **Concern** The experimental data cover only four molecules (three dyes and PFOA). The simulation study uses seven dye variants, but these are not experimentally tested. The claim of generality is therefore based on a limited set of examples. The text acknowledges that methyl orange removal is lower (65%), which suggests the method is not universally effective. The simulation results in Figure 5(a) are not available for review.
  - **Why it matters** The title and abstract imply a broad capability, but the evidence supports a more modest claim. Overstating the generality could mislead potential users of the method.
  - **Resolution test** Either expand the experimental set to include more diverse organic molecules, or temper the claim to reflect the demonstrated scope. Provide Figure 5(a) to support the simulation-based generality argument.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Experimental procedure
  - **Evidence pointer** Results and Discussion, "Polyelectrolyte Complex Formation and Dye Filtration", location not provided
  - **Issue** The text states that 300 μL of anionic copolymer and 220 μL of cationic copolymer are mixed in 10 mL of distilled water, but the final concentrations of the polymers in the mixture are not given. The concentration of the dye solutions and the amount of dye added are also not specified.
  - **Required correction** Provide the final polymer concentrations, dye concentrations, and the mass or moles of dye used in each experiment.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical detail
  - **Affected element** Polymer characterization
  - **Evidence pointer** Table 1, location not provided
  - **Issue** The text mentions that aqueous size exclusion chromatography was used to determine apparent molecular weights, but the eluent, column type, and calibration standards are not described. The low dispersity of 1.1 for the anionic polymer is attributed to aggregation, but this is not directly demonstrated.
  - **Required correction** Provide the SEC conditions and a discussion of how aggregation was inferred. Consider including a control experiment or dynamic light scattering data to support the aggregation claim.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Simulation detail
  - **Affected element** Coarse-grained models
  - **Evidence pointer** Results and Discussion, "Simulations of Polymers and Dyes", location not provided
  - **Issue** The text mentions two models (MARTINI and a more coarse implicit solvent model) but does not provide the simulation box size, the number of polymers, the equilibration time, or the production run length. The mapping of the chemical structures to coarse-grained beads is not described.
  - **Required correction** Provide full simulation parameters in the Methods or SI, including system size, simulation time, and the mapping scheme for the polymers and dyes.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Interpretation
  - **Affected element** Simulation results
  - **Evidence pointer** Figure 3, location not provided
  - **Issue** The text describes a percolation analysis but does not define the percolation threshold or how it was determined. The statement that a charge ratio near 3 was "required" for percolation is not quantified.
  - **Required correction** Define the percolation criterion and provide the percolation probability as a function of charge ratio with error estimates.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** PFOA experiments
  - **Evidence pointer** Results and Discussion, "Polyelectrolyte Complex Formation and Dye Filtration", location not provided
  - **Issue** The PFOA removal efficiency is reported, but the initial PFOA concentration, the water matrix (e.g., deionized vs. tap water), and the pH are not stated. The potential for PFOA to bind to the filtration membrane is not discussed.
  - **Required correction** Provide the experimental conditions for PFOA removal and include appropriate controls to rule out non-specific binding.
  - **Concern ID** R1-m6
  - **Severity** Minor
  - **Axis** Language
  - **Affected element** Introduction
  - **Evidence pointer** Introduction, "In contast, solid polyelectrolyte complexes..."
  - **Issue** Typographical error: "contast" should be "contrast."
  - **Required correction** Correct the typo.

## Technical failings that need to be addressed before the case is established
- R1-M1: Quantitative removal efficiencies are not verifiable without Figure 2(a) and detailed methods.
- R1-M2: Mechanistic claims about hydrophobic domains and micelle formation are not verifiable without spectral and simulation data.
- R1-M3: The titration procedure and charge ratio calculation are not reproducible from the text alone.

## Risk / unsupported claims
- The claim that the method can segregate "a wide range of organic molecules" is not supported by the limited experimental set (four molecules).
- The claim that charge heterogeneity is the key factor enabling generality is inferred from simulations but not directly tested experimentally.
- The statement that the anionic copolymer forms micelles in solution is not directly evidenced in the text; it is inferred from simulation and indirect SEC data.
- The claim that the complexes are "robust to mechanical perturbation" is based on qualitative observation and lacks quantitative measurement.
- The potential for practical application in "industrial water remediation" is speculative and not demonstrated at scale.

## Assessment against Nature-style criteria
- **Originality** The concept of using random copolymer complexes for organic molecule segregation is a creative extension of prior work on enzyme complexes and biomimetic membraneless organelles. The idea is not entirely novel, as polyelectrolyte complexes are well studied, but the specific application and the emphasis on heterogeneity as a design principle offer a fresh perspective.
- **Scientific importance** The potential to remove PFOA and other contaminants from water is of high societal and environmental importance. If the method proves robust and scalable, it could have significant practical impact. However, the current evidence is preliminary and does not yet demonstrate a major advance over existing water treatment technologies.
- **Interdisciplinary readership** The work bridges polymer chemistry, soft matter physics, and environmental engineering. It could appeal to readers in these fields, but the presentation is somewhat specialized and may not be immediately accessible to a broad interdisciplinary audience without additional context on polyelectrolyte complexes and water treatment challenges.
- **Technical soundness** The experimental and simulation approaches are appropriate in principle, but the lack of primary data and methodological details prevents a full assessment. The simulation models are not validated against experimental results, and the experimental section lacks error analysis and controls. The technical soundness cannot be confirmed from the provided material.
- **Readability for nonspecialists** The manuscript is generally well written and logically structured. However, the introduction assumes familiarity with polyelectrolyte complexes and membraneless organelles. The results section includes technical details that may be challenging for nonspecialists. A brief explanation of key concepts, such as charge heterogeneity and percolation, would improve accessibility.

## Recommendation posture
Currently not established from the provided evidence. The manuscript presents a promising concept with a plausible mechanism, but the absence of primary data and methodological details prevents a rigorous evaluation. The authors should provide all figures, tables, and supplementary information, along with expanded experimental and simulation methods, before the claims can be assessed. If the data support the reported efficiencies and the simulations are validated, the work could be of interest to the readership. However, at this stage, the case is not made.