## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions)
- **Assessment boundary** Scientific claims, methodological soundness, and evidence quality as presented in the provided text. No supplementary materials, figures, or raw data were available for inspection beyond what is described in the text.
- **Shared manuscript claim summary** The authors use all-atom molecular dynamics simulations (with and without metadynamics) to show that salt concentration modulates the conformational ensembles of disordered HP1a hinge sequences, and that low-salt conditions promote "fuzzy dimer" formation through mechanisms involving mobile ion release, enhanced local secondary structure, and increased side-chain solvent exposure. They propose this as a molecular-level explanation for experimentally observed salt-driven phase separation of HP1a.
- **Visible evidence base** Text descriptions of simulation protocols, collective variable choices, convergence assessments, and qualitative results referencing Figures 2–6. No actual figures, numerical data, or trajectory statistics are provided in the supplied material.
- **Missing materials affecting confidence** All figures and their underlying data; simulation input files and parameters; convergence metrics in quantitative form; free energy profiles with error estimates; sequence details of the hinge region construct; force field validation details; comparison with experimental data beyond qualitative statements.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question, namely the molecular mechanisms by which ionic conditions drive phase separation of the disordered hinge region of HP1a. The authors employ a reasonable computational strategy combining standard MD and metadynamics, and their qualitative conclusions are plausible and consistent with broader literature on electrostatic-driven condensation of disordered proteins. However, the evidence as presented is almost entirely qualitative, with no quantitative data, error analysis, or direct comparison to experimental observables. The central claims regarding "fuzzy dimer" stabilization and the mechanistic role of ion release are not rigorously established from the supplied material. The manuscript would benefit substantially from quantitative presentation of key results and a clearer articulation of how simulation observables connect to experimental phase separation behavior.
- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation of disordered proteins, particularly those focused on heterochromatin biology and HP1 proteins. The work may also interest computational biophysicists developing and applying enhanced sampling methods to disordered protein systems. The proposed mechanism of salt-dependent fuzzy dimer stabilization could inform experimental design for mutagenesis or ionic-condition perturbation studies.
- **Major strengths** The manuscript tackles a biologically important and mechanistically unresolved question. The computational approach is appropriate in principle, combining standard MD with metadynamics to explore dimerization free energy surfaces. The authors correctly identify the hinge region as a key determinant of HP1a condensation behavior. The qualitative findings, such as enhanced inter-chain contacts and secondary structure at low salt, are consistent with expectations from polyelectrolyte theory and prior studies of disordered protein condensation.
- **Major Concerns** 
  - R1-M1: The central claim that low-salt conditions favor fuzzy dimer formation is supported only by qualitative descriptions of free energy profiles and contact analyses. No quantitative free energy differences, error bars, or statistical significance tests are provided.
  - R1-M2: The manuscript states that "mobile ion release" accompanies dimerization, but no quantitative ion counting or spatial ion distribution analysis is presented. The claim is therefore not directly evidenced.
  - R1-M3: The choice of radius of gyration as the sole collective variable for metadynamics is questionable for capturing dimerization/unbinding events, as Rg may not distinguish well between bound and unbound states for a two-chain system. The authors note that only Rg "was found to capture binding/unbinding events," but no justification or comparison with other CVs is given.
  - R1-M4: The relationship between simulated dimerization behavior and experimentally observed phase separation is asserted but not quantitatively connected. No attempt is made to estimate phase boundaries, critical salt concentrations, or compare with experimental titration data.
  - R1-M5: The force field (AMBER99SB-ILDN) and water model (SPC/E) are stated, but no validation against experimental data for this specific sequence or related disordered proteins is provided. Given known force field sensitivity for disordered proteins, this is a notable gap.
- **Minor Comments** 
  - R1-m1: The manuscript uses "law salt" in two places (Sections 3.2 and Figure 5C), which appears to be a typo for "low salt."
  - R1-m2: The abstract states "in the agreement with condensation trends seen in experiments," which is grammatically awkward and should be revised.
  - R1-m3: The description of the hinge region construct (residue range, sequence) is not provided. This is essential for reproducibility.
  - R1-m4: The convergence assessment is described qualitatively ("splitting the trajectory into 60, 80, and 100 percent chunks") without reporting the actual results of these checks.
  - R1-m5: The manuscript would benefit from a schematic figure or table summarizing the simulation systems, salt conditions, and run lengths.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** 
  - Originality: Moderate. The application of enhanced sampling to HP1a hinge dimerization is novel, but the general concept of salt-driven condensation of disordered proteins is well established.
  - Scientific importance: High. Understanding HP1a phase separation mechanisms has implications for chromatin biology and gene regulation.
  - Interdisciplinary readership: Moderate. The topic bridges biophysics and cell biology, but the presentation is heavily computational and may not be accessible to experimental biologists without additional context.
  - Technical soundness: Weak as presented. The qualitative nature of the evidence and lack of quantitative analysis undermine confidence in the conclusions.
  - Readability for nonspecialists: Adequate but could be improved. The introduction and conclusions are clear, but the results section assumes familiarity with simulation techniques and polymer physics concepts.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript addresses an important question and the approach is reasonable, but the evidence as presented is insufficient to support the central claims. Substantial revision with quantitative analysis and clearer connection to experimental observables would be required before the case is made.

### Major Concern 1
- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** "We show that the mobile ion release, enhancement of local transient secondary structural elements, and side-chain exposure to solvent are robust trends that accompany fuzzy dimer formation" and "low salt conditions... favor fuzzy dimer formation"
- **Evidence pointer** Section 3.2, Figures 4–6 (described in text, not visible)
- **Concern** The central claim that low-salt conditions favor fuzzy dimer formation is supported only by qualitative descriptions. No free energy differences (e.g., ΔG values), contact number distributions with error bars, or statistical tests are reported. The phrase "robust trends" is not backed by quantitative evidence.
- **Why it matters** Without quantitative data, the reader cannot assess the magnitude or significance of the reported effects. The claim of salt-dependent dimerization preference is the core finding of the manuscript and must be rigorously supported.
- **Resolution test** Provide numerical values for free energy minima (with uncertainties) at each salt condition, quantitative contact number distributions with statistical comparisons, and ideally a direct measure of dimerization propensity (e.g., binding free energy or dimer fraction).

### Major Concern 2
- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** "The radial distribution function between sodium and side-chain groups reveals the markedly different pattern of ionic release and conditions for high and low salt monomeric and dimeric units"
- **Evidence pointer** Section 3.2, Figure 6A (described in text, not visible)
- **Concern** The claim of "mobile ion release" accompanying dimerization is not directly evidenced. No ion counts, spatial ion density maps, or quantitative comparison of ion distributions between monomeric and dimeric states are provided. The radial distribution function is mentioned but not shown or quantified.
- **Why it matters** Ion release is proposed as a key mechanistic driver of dimerization. Without direct evidence, this mechanism remains speculative.
- **Resolution test** Provide quantitative analysis of ion distributions (e.g., number of bound ions per chain in monomer vs. dimer states) with statistical uncertainties, and show the radial distribution functions with clear interpretation.

### Major Concern 3
- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological soundness
- **Claim pointer** "From the evaluation of all collective variables, only Rg was found to capture binding/unbinding events by leading to a robust convergence."
- **Evidence pointer** Section 2 (Methods)
- **Concern** The choice of Rg as the sole collective variable for metadynamics is not adequately justified. For a two-chain system, Rg may not reliably distinguish between bound and unbound states, especially if the chains are extended. The authors do not report tests of other CVs or explain why they failed.
- **Why it matters** If the CV does not adequately describe the relevant slow degrees of freedom, the computed free energy profile may be inaccurate or misleading, undermining the central thermodynamic claims.
- **Resolution test** Provide a comparison of free energy profiles obtained with different CVs (or a clear demonstration that Rg captures the binding/unbinding transition, e.g., by showing representative conformations at different Rg values). Alternatively, use a more physically motivated CV such as inter-chain center-of-mass distance or number of inter-chain contacts.

### Major Concern 4
- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** External validity
- **Claim pointer** "in the agreement with condensation trends seen in experiments"
- **Evidence pointer** Abstract, Section 4 (Conclusions)
- **Concern** The connection between simulated dimerization behavior and experimentally observed phase separation is asserted but not quantitatively established. No experimental data are cited or compared directly. The authors do not estimate phase boundaries, critical salt concentrations, or other experimentally testable predictions.
- **Why it matters** The manuscript's significance rests on its ability to explain experimental observations. Without a direct and quantitative link, the relevance of the simulation findings to the biological phenomenon remains unclear.
- **Resolution test** Compare simulation-derived quantities (e.g., dimerization free energy as a function of salt) with experimental phase separation data (e.g., saturation concentrations or critical salt concentrations). Alternatively, make explicit, testable predictions that could be verified experimentally.

### Minor Comment 1
- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Text
- **Evidence pointer** Section 3.2, Figure 5C
- **Issue** "law salt" appears twice, which is clearly a typo for "low salt."
- **Required correction** Replace "law salt" with "low salt" in both instances.

### Minor Comment 2
- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Language
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The phrase "in the agreement with condensation trends seen in experiments" is grammatically incorrect and awkward.
- **Required correction** Revise to "in agreement with experimentally observed condensation trends" or similar.

### Minor Comment 3
- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Section 2
- **Issue** The exact sequence of the hinge region construct is not provided. This is essential for reproducibility and for readers to assess the biological relevance of the simulations.
- **Required correction** Provide the full sequence of the simulated hinge region, including residue numbering relative to the full HP1a protein.

### Minor Comment 4
- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Evidence quality
- **Affected element** Methods
- **Evidence pointer** Section 2
- **Issue** The convergence assessment is described only qualitatively. The authors state that trajectories were split into 60, 80, and 100 percent chunks, but no results of this analysis are reported.
- **Required correction** Report the actual convergence metrics (e.g., block-averaged Rg values, contact map overlap) to demonstrate that the simulations are adequately converged.

### Minor Comment 5
- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability
- **Affected element** Results
- **Evidence pointer** Section 3
- **Issue** The manuscript would benefit from a summary table or schematic figure listing the simulation systems, salt concentrations, simulation lengths, and whether standard MD or metadynamics was used.
- **Required correction** Add a table or figure summarizing the simulation setup to improve clarity and reproducibility.

## Risk / unsupported claims
- The claim that "mobile ion release" drives dimerization is not directly evidenced by quantitative ion analysis.
- The claim that low-salt conditions favor fuzzy dimer formation is not supported by quantitative free energy or statistical data.
- The assertion that simulation results agree with experimental condensation trends is not backed by direct comparison with experimental data.
- The claim that "enhancement of local transient secondary structural elements" accompanies dimerization is based on qualitative descriptions without quantitative secondary structure propensity values.
- The statement that "the changes in solvent-accessible surface and contact patterns are quite dramatic" is not supported by numerical values or statistical comparisons.
- The relevance of the simulated dimerization behavior to full-length HP1a phase separation is asserted but not demonstrated, as the simulations only cover the isolated hinge region.