## Review setup

- **Input scope** Full manuscript text (abstract, methods summary, results, discussion, conclusions) as provided in the submission
- **Assessment boundary** Scientific content, methodological soundness, interpretation of results, and internal consistency of the claims as presented in the supplied text. No external validation of data or code was performed.
- **Shared manuscript claim summary** The authors report that the dimerization domain (DD) of the SARS-CoV-2 Nucleocapsid (N) protein is partially disordered and conformationally dynamic in its monomeric form, and that upon dimerization it forms a high-affinity (K_D ~ 6-12 nM) complex that retains significant conformational flexibility. They further propose that this flexibility is functionally relevant for RNA capture and phase separation behavior.
- **Visible evidence base** Single-molecule FRET measurements (transfer efficiency histograms, lifetime analysis, stoichiometry controls), denaturant titrations, temperature-dependent measurements, Van't Hoff analysis, all-atom Monte Carlo simulations, and comparison with published structures and prior work.
- **Missing materials affecting confidence** Full methods details (referred to Supplementary Information), raw FRET histograms and fitting parameters, simulation force field and validation details, exact labeling positions and dye attachment chemistry, complete temperature titration data, and the full set of supplementary figures and tables referenced in the text.

## Reviewer

- **Overall assessment** This manuscript addresses an important and timely question regarding the conformational behavior of the SARS-CoV-2 Nucleocapsid protein dimerization domain. The combination of single-molecule FRET and all-atom simulations is well suited to the problem, and the authors present a coherent narrative supported by multiple complementary approaches. The finding that the monomeric DD is partially disordered and that the dimer retains conformational flexibility is novel and potentially significant for understanding N protein function. However, several technical aspects require clarification and additional analysis before the central claims can be considered fully established. In particular, the quantitative interpretation of FRET data, the treatment of dye-linker dynamics, the modeling of the dimerization equilibrium, and the extrapolation of thermodynamic parameters warrant closer scrutiny.

- **Who would be interested in the results, and why** Structural biologists and biophysicists studying intrinsically disordered proteins and coupled folding-binding mechanisms; virologists interested in SARS-CoV-2 replication and nucleocapsid assembly; researchers working on phase separation and biomolecular condensates; and those developing therapeutic strategies targeting N protein oligomerization.

- **Major strengths**  
  1. The use of single-molecule FRET at picomolar concentrations to access the monomeric state is methodologically appropriate and technically demanding.  
  2. The combination of experimental measurements with all-atom simulations provides complementary perspectives on the conformational ensemble.  
  3. The study addresses a gap in understanding: the conformational state of the DD prior to dimerization.  
  4. The temperature-dependent measurements and Van't Hoff analysis provide thermodynamic insight beyond simple affinity measurements.  
  5. The authors are appropriately cautious in several interpretations, acknowledging limitations of their models and simulations.

- **Major Concerns**

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness of FRET interpretation  
- **Claim pointer** The authors claim that the monomeric DD is "partially disordered" and described as a "molten globule" based on FRET-derived distances and simulations.  
- **Evidence pointer** Results section "The Dimerization Domain is partially disordered in the monomer form"; Figures 2, 3, S1, S2  
- **Concern** The interpretation of the FRET data relies heavily on the assumption that the interdye distance distribution is well described by a Gaussian chain or SAW-ν model. However, the authors do not provide sufficient detail on how the photon statistics, dye photophysics, and linker dynamics were modeled. The mean transfer efficiency of 0.567 ± 0.005 for the monomer is interpreted as an expanded ensemble, but without a rigorous analysis of the full transfer efficiency distribution (e.g., using photon distribution analysis or maximum likelihood methods), it is difficult to exclude the presence of multiple discrete conformations or a broad but structured distribution. The comparison between experimental distances and simulation-derived distances is qualitative, and the discrepancy (5.7 nm vs 4.4 nm) is attributed to multiple factors without a quantitative decomposition of these contributions.  
- **Why it matters** The central claim of partial disorder in the monomer depends on accurate distance determination and distribution analysis. If the FRET analysis is biased by unaccounted dye dynamics or incorrect model assumptions, the conclusion of "molten globule" behavior may be overstated or mischaracterized.  
- **Resolution test** Provide a detailed description of the FRET data analysis, including the model used to convert transfer efficiencies to distances, treatment of dye linker dynamics (e.g., using FRET-restrained positioning or molecular dynamics of dye linkers), and a rigorous statistical comparison of alternative models (e.g., two-state vs continuous distribution). Show that the conclusions are robust to these modeling choices.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Quantitative rigor of dimerization affinity determination  
- **Claim pointer** The authors report a dissociation constant K_D,L/U of 6 ± 2 nM from a global fit of SVD amplitude curves to a binding model.  
- **Evidence pointer** Results section "Dimer formation induces folding of the DD domain"; Figure 3B, 3D; Supplementary Information  
- **Concern** The determination of K_D relies on a global fit of SVD amplitude curves, but the details of the binding model are not fully described in the main text. The model must account for labeled-labeled, labeled-unlabeled, and unlabeled-unlabeled dimers, each potentially with different affinities. The authors report K_D,L/U = 6 ± 2 nM and K_D,U/U = 11 ± 3 nM, but it is unclear how these values are constrained by the data, given that the labeled species is at 100 pM and the unlabeled species is titrated to micromolar concentrations. The sensitivity of the fit to the assumed model and the error propagation from the SVD decomposition are not discussed. Additionally, the authors note a discrepancy between the K_D determined from the titration (6 nM) and the value of ~12 nM mentioned in the abstract, which is not reconciled in the text.  
- **Why it matters** The affinity of dimerization is a key quantitative output of the study and is used to support the claim of a "high affinity" complex. If the binding model is underconstrained or the error estimates are not robust, the reported K_D values may not be reliable.  
- **Resolution test** Provide a complete description of the binding model, including all equations and assumptions. Show the full SVD analysis, including the magnitude of singular values and the fraction of variance explained. Perform a sensitivity analysis to demonstrate that the fitted K_D values are robust to model variations and to the choice of which singular vectors are included in the fit. Reconcile the discrepancy between the abstract value of ~12 nM and the reported 6 ± 2 nM.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** No  
- **Axis** Interpretation of temperature-dependent data and Van't Hoff analysis  
- **Claim pointer** The authors report a linear Van't Hoff relationship between 37 °C and 47 °C, yielding ΔH = -99 ± 6 kcal/mol and ΔS = 0.29 ± 0.02 kcal/mol K, and note deviations from linearity at lower temperatures attributed to heat capacity effects.  
- **Evidence pointer** Results section "Temperature effect on dimer stability"; Figure 5E; Supplementary Figure 4 and Table 5  
- **Concern** The Van't Hoff analysis is performed over a narrow temperature range (37-47 °C), and the authors acknowledge deviations from linearity when including lower temperatures. The reported ΔH and ΔS values are extremely large in magnitude, which is unusual for a protein-protein interaction and may indicate that the two-state assumption is not valid, or that the conformational changes within the dimer (which the authors themselves document) contribute significantly to the temperature dependence. The heat capacity fit is mentioned but the parameters are only reported in the Supplementary Information, which is not available for review. The authors also note a discrepancy between extrapolated and experimentally determined fractions at lower temperatures, which they attribute to conformational effects, but this is not quantitatively addressed.  
- **Why it matters** The thermodynamic characterization is presented as a significant result, but the interpretation of the Van't Hoff analysis may be compromised by the narrow temperature range, the presence of conformational heterogeneity, and the lack of a rigorous treatment of heat capacity effects. The large enthalpy and entropy values, if taken at face value, have implications for the mechanism of binding that are not discussed.  
- **Resolution test** Provide the full temperature-dependent dataset and the complete heat capacity analysis. Discuss whether the two-state assumption is valid given the documented conformational heterogeneity. Consider whether a more complex model (e.g., including a conformational pre-equilibrium) is needed to describe the data. Provide error estimates that account for the limited temperature range.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Generalizability of simulation results  
- **Claim pointer** The authors use all-atom simulations to support their experimental findings and to provide "atomistic details" of the monomeric and dimeric ensembles.  
- **Evidence pointer** Methods section "All-atom simulations"; Results sections "The Dimerization Domain is partially disordered in the monomer form" and "Conformational ensemble of the dimerization domain and C-terminal IDR"; Figures 3, S6  
- **Concern** The simulation methodology is described only briefly. For the monomer, the authors used a hybrid approach where a "partially folded region" was held fixed while the remainder was sampled. This is a significant constraint that may bias the resulting ensemble. For the dimer, the simulations start from the crystal structure and only sample the C-terminal IDR, with the DD held in place. This means the simulations cannot address the key question of whether the dimer interface itself is dynamic or whether the observed flexibility arises from the terminal regions. The force field, simulation length, and convergence criteria are not stated.  
- **Why it matters** The simulations are used to corroborate the experimental findings and to provide mechanistic insight. If the simulations are not converged or are biased by the constraints imposed, the conclusions drawn from them may not be reliable.  
- **Resolution test** Provide full details of the simulation protocol, including force field, water model, simulation length, and convergence analysis. Justify the constraints applied and discuss how they might affect the conclusions. If possible, perform additional simulations without these constraints to test the robustness of the results.

- **Minor Comments**

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity and consistency  
- **Affected element** Abstract and Results  
- **Evidence pointer** Abstract; Results section "Dimer formation induces folding of the DD domain"  
- **Issue** The abstract states a dissociation constant of ~12 nM, while the Results section reports K_D,L/U = 6 ± 2 nM and K_D,U/U = 11 ± 3 nM. The relationship between these values is not explained.  
- **Required correction** Clarify which K_D value is being reported in the abstract and how it relates to the values determined in the titration experiments.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Technical detail  
- **Affected element** Methods  
- **Evidence pointer** Methods section "Single-molecule FRET"  
- **Issue** The methods state that cysteine residues were introduced at positions 245 and 363, but the rationale for these specific positions and the validation that labeling does not perturb the protein structure or function is not provided.  
- **Required correction** Provide a brief justification for the labeling positions and include any control experiments demonstrating that the labeled protein behaves similarly to the unlabeled protein.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Interpretation  
- **Affected element** Discussion  
- **Evidence pointer** Discussion section, paragraph on phase separation  
- **Issue** The authors speculate that the flexibility of the dimer may favor RNA capture and that the temperature dependence of dimerization may explain phase separation behavior. These are interesting hypotheses, but they are not directly tested in this work.  
- **Required correction** Clearly distinguish between conclusions supported by the data and speculative hypotheses. Consider softening the language or explicitly stating that these are untested proposals.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Presentation  
- **Affected element** Figures  
- **Evidence pointer** Figures 3, 4, 5, S1-S6  
- **Issue** The figure captions are not provided in the submitted text, making it difficult to fully interpret the figures referenced in the Results.  
- **Required correction** Ensure that all figures have complete and self-contained captions that describe the data shown, the experimental conditions, and the statistical analysis.

- **Concern ID** R1-m5  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Methods and Data Availability  
- **Evidence pointer** Methods section; no data availability statement provided  
- **Issue** The manuscript does not include a data availability statement. The simulation data and analysis scripts are mentioned as being available on GitHub, but the raw FRET data are not mentioned.  
- **Required correction** Add a data availability statement that specifies where all raw data, analysis scripts, and simulation trajectories can be accessed.

## Risk / unsupported claims

1. The claim that the monomeric DD is "partially disordered" and described as a "molten globule" is supported by FRET and simulation data, but the quantitative interpretation depends on modeling assumptions that are not fully described or validated in the provided text.
2. The claim that the dimer retains "significant conformational flexibility" is based on FRET measurements in the presence of denaturant and on simulations where the DD is held fixed. The extent to which this flexibility reflects the native state versus partial denaturation is not fully established.
3. The speculation that the retained flexibility of the dimer favors RNA capture and that the temperature dependence of dimerization explains phase separation behavior is not directly tested and should be considered a hypothesis rather than a supported conclusion.
4. The reported thermodynamic parameters (ΔH = -99 ± 6 kcal/mol, ΔS = 0.29 ± 0.02 kcal/mol K) are derived from a narrow temperature range and may not be robust; the heat capacity analysis is not fully presented in the available text.
5. The claim that the results are "likely applicable to a series of analogous dimerization domains in other coronaviruses" is based on sequence and structural similarity but is not tested experimentally or computationally in this work.