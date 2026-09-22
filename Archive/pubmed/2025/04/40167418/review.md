## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results and discussion, conclusion, methods, and supplementary figure references
- **Assessment boundary** Scientific validity of the computational findings, methodological soundness, interpretation of results, and alignment with stated conclusions
- **Shared manuscript claim summary** The authors use all-atom discrete molecular dynamics simulations to show that Aβ42, particularly in fibrillar form, can bind the amyloidogenic core region (ACR) of TDP-43, induce unfolding of its helical structure, and promote formation of parallel in-register intermolecular β-sheets between ACR monomers, thereby potentially catalyzing pathogenic TDP-43 aggregation in Alzheimer's disease.
- **Visible evidence base** Results and Discussion sections with figures referenced (Figures 1–7, Figures S1–S7), Methods section describing simulation protocols and analysis criteria
- **Missing materials affecting confidence** Actual figure images, supplementary figures, simulation trajectory data, force field parameter files, and analysis scripts were not provided. Only the manuscript text was available for review.

## Reviewer
- **Overall assessment** This manuscript presents a computational investigation of cross-interactions between Aβ42 and the amyloidogenic core region of TDP-43, a topic of growing relevance given the clinical association between TDP-43 co-pathology and more severe Alzheimer's disease. The study is well-motivated and addresses a genuine gap in understanding the molecular basis of TDP-43 pathology in AD. The use of DMD simulations with substantial sampling (over 600 μs total) is appropriate for studying intrinsically disordered proteins and early aggregation events. The key finding, that fibrillar Aβ42 can template structural transformation of the TDP-43 ACR and promote β-sheet-rich dimer formation, is potentially significant. However, several technical concerns regarding simulation methodology, analysis choices, and interpretation of results need to be addressed before the conclusions can be considered fully established. The manuscript would benefit from additional validation of the simulation findings and more careful discussion of limitations.

- **Who would be interested in the results, and why** Researchers studying TDP-43 proteinopathies, including ALS and FTLD, would find these results relevant to understanding aggregation mechanisms. The Alzheimer's disease research community, particularly those investigating co-pathologies and their contribution to clinical heterogeneity, would be interested in the proposed cross-seeding mechanism. Computational biophysicists working on protein aggregation and intrinsically disordered proteins would also find the methodological approach and findings of interest. The potential clinical implications for AD patients with TDP-43 co-pathology make this relevant to translational researchers as well.

- **Major strengths** 
  1. The study addresses a clinically important and understudied question: how Aβ and TDP-43 interact at the molecular level in the context of AD co-pathology.
  2. The use of DMD simulations with extensive sampling across multiple systems and 48 independent trajectories per system provides reasonable statistical power for the observed phenomena.
  3. The comparison across multiple systems (homodimer, heterodimer, homotrimer, heterotrimers, fibril seed systems) allows for systematic assessment of concentration and stoichiometry effects.
  4. The identification of a specific mechanism (backbone hydrogen bonding with the fibril elongation surface) provides a concrete molecular hypothesis for cross-seeding.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of simulation methodology
- **Claim pointer** The authors claim that DMD simulations with the Medusa force field and implicit solvent can accurately capture the structural dynamics and interactions between Aβ42 and the TDP-43 ACR.
- **Evidence pointer** Methods section, "Discrete Molecular Dynamics Simulations" and "Molecular Systems"
- **Concern** The manuscript does not provide sufficient validation of the simulation methodology for the specific systems studied. While DMD with the Medusa force field has been used previously for amyloid studies, the authors do not demonstrate that this approach reproduces known experimental observations for either TDP-43 ACR or Aβ42. No comparison with experimental data (e.g., secondary structure propensities from NMR, binding affinities, or aggregation kinetics) is provided. Additionally, the use of implicit solvent with the Lazaridis-Karplus EEF1 model may not accurately capture hydrophobic effects that are critical for amyloid aggregation. The authors also hold the fibril seed atoms static, which prevents any conformational reorganization of the fibril that might occur upon binding.
- **Why it matters** Without validation that the simulation methodology reproduces known biophysical properties of these systems, the quantitative and even qualitative conclusions about structural transformations and binding preferences may be artifacts of the force field or solvent model. The static fibril approximation is particularly concerning because it may bias the system toward the observed binding modes.
- **Resolution test** The authors should provide validation of their simulation approach against experimental data for TDP-43 ACR and Aβ42, such as secondary structure propensities, binding affinities, or known aggregation behavior. They should also either justify the static fibril approximation with test simulations allowing fibril flexibility, or acknowledge this as a significant limitation and discuss how it might affect the conclusions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of results and strength of conclusions
- **Claim pointer** The authors conclude that "Aβ42, especially in its fibrillar form, may catalyze the pathogenic structural transformation within the TDP-43 ACR that initiates its aberrant aggregation" and that this provides "important theoretical insights into TDP-43 pathology in AD."
- **Evidence pointer** Abstract, Results and Discussion sections, particularly "The TDP-43 ACR interacted strongly with an Aβ42 fibril seed" and "Parallel, in-register β-sheet formation occurred between TDP-43 ACR monomers contacting the elongation surface of an Aβ42 fibril seed"
- **Concern** The simulations show that ACR monomers can form β-sheet-rich structures when interacting with the Aβ42 fibril seed, but the manuscript does not establish that this represents a pathogenic transformation relevant to disease. The ACR is a 50-residue fragment, not the full-length TDP-43 protein, and the simulations do not demonstrate that the observed β-sheet formation leads to aggregation-competent species or amyloid fibril formation. The leap from "β-sheet formation in a fragment" to "pathogenic structural transformation that initiates aberrant aggregation" is not fully supported. Furthermore, the physiological relevance of the concentrations and stoichiometries used is not discussed.
- **Why it matters** The central claim of the paper is that Aβ42 can catalyze pathogenic TDP-43 aggregation. If the observed β-sheet formation in the ACR fragment does not translate to full-length TDP-43 aggregation, or if the simulation conditions are not physiologically relevant, the clinical implications drawn by the authors would be overstated.
- **Resolution test** The authors should either (a) provide additional simulations or discussion connecting the ACR fragment behavior to full-length TDP-43, (b) temper their conclusions to more clearly state that these are preliminary computational findings requiring experimental validation, or (c) provide experimental evidence (even from literature) supporting the relevance of ACR fragment studies to full-length TDP-43 aggregation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness of analysis methods
- **Claim pointer** The authors use 2D PMF analysis to characterize the energy landscapes of the systems studied, and use contact maps to identify interaction patterns.
- **Evidence pointer** Methods section, "Computational Analysis"; Results and Discussion sections referencing Figures 1–7
- **Concern** The manuscript states that PMF analysis was performed using "simulation time periods corresponding to a plateau in the averaged time evolution graphs" but does not provide these equilibration plots or specify the exact time windows used for each system. This makes it difficult to assess whether the systems were properly equilibrated and whether the PMF calculations are reliable. Additionally, the choice of reaction coordinates for the 2D PMFs (e.g., number of contacts vs. helix fraction) may not capture the most relevant collective variables for the structural transitions described.
- **Why it matters** PMF calculations are only meaningful if the underlying sampling is converged and the chosen reaction coordinates adequately describe the relevant free energy landscape. Without this information, the quantitative features of the PMFs (e.g., relative depths of basins) cannot be properly evaluated.
- **Resolution test** The authors should provide the equilibration plots, specify the exact time windows used for analysis, and justify their choice of reaction coordinates. They should also provide an assessment of sampling convergence (e.g., block averaging or multiple independent runs showing consistent results).

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Completeness of the investigation
- **Claim pointer** The authors state that "interaction with the Aβ42 fibril seed catalyzed the formation of a parallel, in-register intermolecular β-sheet between two ACR monomers" and that this represents a nucleation event for TDP-43 aggregation.
- **Evidence pointer** Results and Discussion, "Parallel, in-register β-sheet formation occurred between TDP-43 ACR monomers contacting the elongation surface of an Aβ42 fibril seed"
- **Concern** The manuscript reports that in simulations with two ACR monomers and the Aβ42 fibril seed, β-sheet formation between ACR monomers was observed. However, the frequency of this event across the 48 trajectories is not reported. If this is a rare event, the conclusion that the fibril seed "catalyzes" ACR dimerization would be weakened. Additionally, the simulations are only 1500 ns, which is short compared to the timescales of protein aggregation. The authors do not discuss whether longer simulations or enhanced sampling methods would be needed to more definitively establish the nucleation mechanism.
- **Why it matters** The claim of catalysis of ACR dimerization is central to the paper's conclusions. If the observed event is rare or not statistically robust, the strength of the claim is not justified.
- **Resolution test** The authors should report the frequency of β-sheet formation between ACR monomers across trajectories, provide statistical analysis of this event, and discuss whether the simulation timescale is sufficient to draw conclusions about nucleation.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and completeness of methods
- **Affected element** Methods section, "Molecular Systems"
- **Evidence pointer** Methods section, "Molecular Systems"
- **Issue** The manuscript states that "the amino acid sequences of the TDP-43 ACR, corresponding to residues 311–360 of wild-type TDP-43, and Aβ42 are shown in Figure S7" but does not describe how the initial structures were prepared (e.g., any energy minimization, solvation, or equilibration steps before the production runs).
- **Required correction** Provide a description of the system preparation protocol, including any minimization or equilibration steps, and specify the temperature coupling scheme and integration time step used.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Interpretation of results
- **Affected element** Results and Discussion, "Aβ42 monomers interacted with both surfaces of a TDP-43 fibril seed"
- **Evidence pointer** Results and Discussion, "Aβ42 monomers interacted with both surfaces of a TDP-43 fibril seed"
- **Issue** The authors state that "the high intrinsic amyloidogenicity of Aβ42 may preclude a significant seeding effect by TDP-43 fibrils" but this conclusion is based on simulations of Aβ42 monomers interacting with a TDP-43 fibril seed. The authors do not compare this to a control simulation of Aβ42 alone to establish the baseline aggregation propensity.
- **Required correction** Either provide control simulation data for Aβ42 alone or temper the conclusion to acknowledge that the comparison is not directly tested in this study.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation and accessibility
- **Affected element** Throughout the manuscript
- **Evidence pointer** Results and Discussion sections
- **Issue** The manuscript uses many abbreviations and technical terms (e.g., ACR, DMD, PMF, LARKS) without always defining them at first use in the main text. Some figure references are made without describing what the reader should observe in the figure.
- **Required correction** Define all abbreviations at first use, and add brief descriptions of what each figure shows when referenced in the text.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Conclusion section
- **Evidence pointer** Conclusion section
- **Issue** The authors acknowledge that "our simulation results may have been sensitive to initial conditions" but do not discuss other important limitations, such as the use of a fragment rather than full-length TDP-43, the implicit solvent model, the static fibril approximation, and the lack of experimental validation.
- **Required correction** Add a limitations paragraph to the Conclusion or Discussion that addresses these points and suggests future experimental and computational work to address them.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section
- **Evidence pointer** Methods section, "Discrete Molecular Dynamics Simulations"
- **Issue** The manuscript states that "the DMD simulation engine is available at http://www.moleculesinaction.com/" but does not provide version information, specific force field parameters, or input files needed to reproduce the simulations.
- **Required correction** Provide version information for the DMD software, specify the exact force field parameters used, and consider making input files and analysis scripts available as supplementary material or through a repository.

## Risk / unsupported claims
- The claim that Aβ42 fibrils "catalyze" pathogenic TDP-43 aggregation is not fully supported, as the simulations only show β-sheet formation in a 50-residue fragment, not full-length TDP-43 aggregation.
- The statement that "our theoretical study reveals novel insights regarding the cross-interaction between Aβ and TDP-43, providing a potential molecular explanation for the development of TDP-43 pathology in AD" overreaches, as no experimental validation is provided and the physiological relevance of the simulation conditions is not established.
- The claim that "interaction with the Aβ42 fibril seed catalyzed the formation of a parallel, in-register intermolecular β-sheet between two ACR monomers" is not quantitatively supported, as the frequency of this event across trajectories is not reported.
- The assertion that "the high intrinsic amyloidogenicity of Aβ42 may preclude a significant seeding effect by TDP-43 fibrils" is not directly tested, as no control simulation of Aβ42 alone is presented.
- The generalizability claim that "our results may be generalizable to other fibril structures" is speculative and not tested in this study.