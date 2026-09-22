## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and supplementary figure references.
- **Assessment boundary** Scientific content, methodology, data interpretation, and internal consistency of the reported findings. No assessment of formatting or editorial style beyond readability for a general scientific audience.
- **Shared manuscript claim summary** The authors report that α-synuclein (αSyn) aggregation and liquid-liquid phase separation (LLPS) exhibit distinct salt dependencies under crowded conditions. Aggregation shows a non-monotonic salt dependence, attributed to intramolecular N-terminal domain (NTD) and C-terminal tail (CTT) interactions modulated by electrostatic screening and salting-out effects. LLPS shows a monotonic salt dependence, attributed to overall intermolecular interactions. The authors also report time-dependent interconversion between fibrillar aggregates and droplets, with droplets capable of dissolving pre-formed fibrils after prolonged incubation.
- **Visible evidence base** Main text figures 1–6 (referenced), supplementary figures S1–S17 (referenced), methods section describing protein preparation, aggregation kinetics, droplet formation, SAXS, ESI-TOF LC-MS, and coarse-grained simulations.
- **Missing materials affecting confidence** Raw data files, full supplementary figures and legends, simulation parameter files, and statistical analysis details are not provided. Exact sample sizes for some experiments and details of image analysis are not fully described.

## Reviewer
- **Overall assessment** This manuscript presents a systematic and potentially important investigation of the distinct salt dependencies of αSyn aggregation and LLPS. The combination of experiments and coarse-grained simulations is commendable and provides a plausible molecular explanation for the observed divergence. The finding that fibrillar structures can dissolve into droplets over long timescales is intriguing and challenges common assumptions. However, several technical concerns, particularly regarding the interpretation of ThT fluorescence at high salt, the long-term stability of the observed states, and the direct comparability of simulation and experimental conditions, need to be addressed before the central claims are fully established.
- **Who would be interested in the results, and why** Researchers in the fields of protein aggregation, phase separation, neurodegeneration (particularly Parkinson's disease), and biophysics of intrinsically disordered proteins. The work provides a nuanced view of the relationship between LLPS and aggregation, which is a topic of broad and current interest. The methodological approach combining high-throughput screening with simulations will also be of interest to the biophysics community.
- **Major strengths**
    1.  Systematic experimental screening across a wide parameter space (protein, salt, crowding, pH) using a robotic dispenser, providing a comprehensive dataset.
    2.  Clear demonstration of a qualitative difference in salt dependence between aggregation and LLPS, which is a significant conceptual advance over previous studies that often assumed correlated behavior.
    3.  The use of coarse-grained simulations to provide a mechanistic explanation for the experimental observations, linking single-chain properties to macroscopic assembly behavior.
    4.  The long-term observation of fibril-to-droplet conversion is a striking and novel finding that challenges the conventional view of fibril stability.
- **Major Concerns**

    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness / Data interpretation
    - **Claim pointer** The claim that aggregation is inhibited at high salt concentrations (above 250 mM) under crowded conditions, based on ThT fluorescence and free monomer concentration.
    - **Evidence pointer** Figure 1E, 1H, Figure S3, Results section "Regulation of αSyn aggregation by intramolecular electrostatic interactions between NTD and CTT"
    - **Concern** The interpretation of the non-monotonic salt dependence of aggregation relies heavily on ThT fluorescence intensity. It is well-established that ThT fluorescence can be affected by ionic strength and the specific morphology of amyloid fibrils. The authors mention verifying the trend with free monomer concentration (Fig. S3), but the details of this measurement are not provided. It is crucial to demonstrate that the decrease in ThT signal at high salt is not due to altered ThT binding affinity or quantum yield, but genuinely reflects a lower amount of aggregated protein. Furthermore, the claim that the "salting-out effect" drives the collapse of the chain at high salt and thus reduces aggregation seems counterintuitive, as salting-out typically promotes intermolecular aggregation. The authors need to clarify this point and provide more direct evidence for the amount of aggregated protein (e.g., via sedimentation assays or SDS-resistant aggregates) across the salt range.
    - **Why it matters** The central mechanistic claim of the paper, that aggregation is governed by intramolecular NTD-CTT interactions, hinges on the accurate measurement of aggregation extent. If the ThT signal is not a faithful reporter across the entire salt range, the proposed mechanism is weakened.
    - **Resolution test** Provide quantitative data on the amount of aggregated protein (e.g., pelletable material, monomer depletion) as a function of salt concentration. Include control experiments showing ThT fluorescence is not directly modulated by salt concentration in the presence of a fixed amount of pre-formed fibrils.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness / Data interpretation
    - **Claim pointer** The claim that fibrillar structures observed at 29 days convert into droplets after 120 days, and that this represents a thermodynamically driven transition to a more stable state.
    - **Evidence pointer** Figure 4, Results section "Dissolution of αSyn aggregates into droplets"
    - **Concern** The observation of fibril-to-droplet conversion is remarkable, but the evidence presented is primarily based on optical microscopy images. The authors need to provide higher-resolution characterization to confirm that the "fibrillar-like structures" are indeed amyloid fibrils and that they are truly dissolving, rather than being obscured or displaced by the growing droplets. The mass spectrometry data (Fig. S16) confirms the protein is intact, but does not address the structural state. The claim that the droplet state is "more stable" is a strong thermodynamic statement that requires more rigorous evidence, such as measuring the solubility of the fibrillar and droplet states, or demonstrating that the process is reversible.
    - **Why it matters** This is a headline finding of the paper. If the structural identity of the initial aggregates and the final droplets is not rigorously established, the conclusion that droplets can dissolve fibrils is not supported.
    - **Resolution test** Perform electron microscopy or high-resolution fluorescence microscopy on samples at intermediate time points to visualize the structural transition. Use a conformation-specific antibody (e.g., targeting amyloid structure) to confirm the nature of the initial aggregates. Measure the critical concentration of the droplet phase and compare it to the solubility of the fibrillar state to support the thermodynamic argument.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical soundness / Methodology
    - **Claim pointer** The claim that the coarse-grained simulations accurately capture the experimental conditions, particularly the effect of PEG400 and the salt-dependent behavior.
    - **Evidence pointer** Methods section "Molecular dynamics simulations", Figures 1K-M, 2B-D, 3C-D
    - **Concern** The simulations model PEG400 implicitly by increasing the interaction strength (ε) between amino acids. While this is a common approach, the quantitative mapping between the simulated ε values and the experimental PEG concentrations is not clearly established. The authors state that ε=0.15 and 0.17 kcal/mol correspond to 20% and 25% PEG400, respectively, but the basis for this assignment is not provided. Furthermore, the simulations are performed at a single protein concentration, while the experiments span a range. The comparison between simulated single-chain properties (Rg) and experimental LLPS behavior is indirect and relies on polymer theory assumptions that may not hold for a protein with specific intra- and intermolecular interaction patterns.
    - **Why it matters** The simulations are used to provide a molecular-level explanation for the experimental observations. If the simulation conditions are not accurately mapped to the experiments, the mechanistic conclusions drawn from them are less convincing.
    - **Resolution test** Provide a more detailed justification for the mapping between ε and PEG concentration, perhaps by comparing simulated Rg values to experimental SAXS data at different PEG concentrations. Perform simulations at multiple protein concentrations to test the robustness of the predicted phase behavior.

- **Minor Comments**

    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity / Reproducibility
    - **Affected element** Methods section "Measurement of droplet formation"
    - **Evidence pointer** Methods section
    - **Issue** The method for assessing droplet formation and fibril length using the Rock Imager and Fiji is described briefly. The criteria for identifying droplets versus amorphous aggregates or fibrils are not defined.
    - **Required correction** Provide a more detailed description of the image analysis protocol, including any thresholding or particle identification algorithms used. Define the morphological criteria used to distinguish droplets, fibrils, and precipitates.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Data presentation
    - **Affected element** Figure 5
    - **Evidence pointer** Figure 5
    - **Issue** The correlation between fibril size and kinetics is described qualitatively. The data in Figure 5C appears to show a relationship, but a statistical analysis is not presented.
    - **Required correction** Perform a statistical analysis (e.g., correlation coefficient) to support the claim of a distinct correlation between fibril size and kinetics.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Methods section "Measurement of aggregation kinetics"
    - **Evidence pointer** Methods section
    - **Issue** The aggregation kinetics were performed at 37°C under shaking, while the LLPS experiments were performed at 20°C under quiescent conditions. This difference in temperature and agitation could affect the relative rates and outcomes of aggregation and phase separation.
    - **Required correction** Acknowledge this limitation in the discussion and justify why the comparison between the two processes remains valid despite the different experimental conditions.

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Discussion
    - **Evidence pointer** Discussion section
    - **Issue** The discussion of the energy landscape (Figure 6C) is somewhat speculative. While it is a useful framework, the specific free energy surfaces are not directly measured.
    - **Required correction** Clearly distinguish between the proposed energy landscape model and the directly measured experimental data.

## Risk / unsupported claims
- The claim that the droplet state is thermodynamically more stable than the fibrillar state at low salt concentrations is not directly supported by the data presented. The observation of fibril-to-droplet conversion is suggestive, but thermodynamic stability requires more rigorous measurement.
- The claim that the "salting-out effect" on intramolecular interactions is the primary cause of the non-monotonic aggregation behavior is a plausible hypothesis but is not directly tested experimentally. The simulations support this, but the mapping between simulation and experiment is not fully validated.
- The statement that the droplet state is capable of "dissolving the aggregates through a variety of heterotypic interactions" is speculative. The specific interactions involved are not identified.
- The claim that the observed behavior is unique to αSyn and not general to other IDPs is not tested and is therefore an overstatement. The authors correctly note this is a "distinctive" feature but do not provide comparative data.