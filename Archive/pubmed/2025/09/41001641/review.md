## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, conclusions, and methods
- **Assessment boundary** Scientific content, methodological rigor, evidence quality, and internal consistency of the presented claims
- **Shared manuscript claim summary** The authors report that full-length 2N4R Tau undergoes salt-dependent reentrant liquid-liquid phase separation (LLPS), and that single-molecule FRET and coarse-grained molecular dynamics simulations reveal a conformational transition from compact to extended states during LLPS under both low-salt (electrostatic-driven) and high-salt (hydrophobic-driven) conditions. They further propose that intramolecular interactions stabilizing compact monomer conformations are converted into intermolecular interactions that drive phase separation.
- **Visible evidence base** Phase Scan microfluidics data (Figure A), coarse-grained MD simulations (Figures B, C), smFRET histograms (Figure B), contact maps (Figure), Rg analyses (Figure), supplementary figures S1-S6, Table S1
- **Missing materials affecting confidence** Individual smFRET histograms for all four Tau variants across all conditions are not fully shown; raw FRET efficiency distributions and fitting parameters are only summarized in Table S1; representative fluorescence microscopy images of droplets are not shown in the main text; no quantitative comparison between experimental and simulated Rg values is provided; the FH-DH theory fitting parameters are not fully described

## Reviewer

### Overall assessment
This manuscript addresses an important and timely question in the field of biomolecular condensates: how the conformational properties of an intrinsically disordered protein relate to its phase separation behavior. The combination of single-molecule FRET and coarse-grained simulations is well suited to this question, and the observation that Tau transitions from compact to extended conformations during LLPS under both electrostatic- and hydrophobic-dominated conditions is potentially significant. However, several technical concerns regarding the interpretation of smFRET data in condensed phases, the coarse-grained model calibration at high salt, and the quantitative link between intramolecular and intermolecular interactions need to be addressed before the central claims can be considered fully established.

### Who would be interested in the results, and why
Researchers studying liquid-liquid phase separation of intrinsically disordered proteins, biophysicists interested in conformational dynamics of IDPs, and investigators working on Tau biology and neurodegeneration would find these results relevant. The work provides a direct experimental observation of conformational changes during LLPS and proposes a generalizable mechanism linking monomer compaction to phase separation propensity, which could inform future studies on other IDPs and on the design of interventions targeting aberrant phase transitions.

### Major strengths
1. The combination of experimental (smFRET) and computational (coarse-grained MD) approaches provides complementary perspectives on the conformational changes during LLPS.
2. The use of Phase Scan microfluidics enables systematic mapping of the salt-dependent phase diagram, revealing reentrant behavior.
3. The study addresses a fundamental question about the relationship between single-chain conformations and phase behavior, which has been largely unexplored experimentally.
4. The observation that conformational expansion occurs regardless of the driving force (electrostatic vs hydrophobic) suggests a potentially general principle.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors claim that smFRET reveals "a noticeable shift toward lower FRET efficiencies in the distribution of all variants" upon LLPS induction, indicating increased interdomain distances.
- **Evidence pointer** Figure B, Table S1
- **Concern** The smFRET measurements in the LLPS state are performed in the presence of 15% PEG and 10 μM unlabeled Tau as a dopant. The authors state that this suppresses intermolecular FRET, but the effectiveness of this approach in condensed phases is not demonstrated. In a dense droplet environment, the local concentration of labeled Tau within the condensate could be substantially higher than the bulk concentration, potentially leading to residual intermolecular FRET even with a 100-fold excess of unlabeled protein. Additionally, the presence of PEG itself can alter protein conformations through excluded volume effects, confounding the comparison between "native" and "LLPS" states.
- **Why it matters** The central claim of the paper, that Tau transitions to extended conformations during LLPS, depends critically on the interpretation of these smFRET measurements. If intermolecular FRET contributes to the observed shifts, the conclusion would be compromised.
- **Resolution test** The authors should provide control experiments demonstrating that the FRET efficiency distributions are independent of labeled protein concentration within the condensate, or use alternative approaches such as fluorescence correlation spectroscopy to verify that the observed shifts reflect intramolecular distance changes. Additionally, measurements in the presence of PEG but below the saturation concentration (non-LLPS conditions) would help disentangle crowding effects from LLPS-specific effects.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the coarse-grained MD simulations with a modified HPS force field (λH = 1.1) reproduce the reentrant LLPS behavior of Tau at high salt concentrations, corresponding to approximately 3 M NaCl.
- **Evidence pointer** Methods section "Coarse-Grained Model and Salt-Dependent Force Field", Figure C
- **Concern** The modification of the HPS force field involves increasing hydrophobic interactions by 10-30% based on all-atom umbrella sampling simulations of specific amino acid pairs. However, the manuscript does not provide sufficient details on how these modifications were derived, which amino acid pairs were sampled, and whether the scaling factor of 1.1 (corresponding to a 10% increase) is appropriate for Tau. The authors state that "even a modest increase of 4% in hydrophobic attraction was adequate to induce reentrant LLPS" but do not show this data. Furthermore, the mapping between λH = 1.1 and an effective salt concentration of ~3 M is based on indirect reasoning that is not fully explained.
- **Why it matters** The simulation results at high salt are used to support the claim that hydrophobic interactions drive LLPS in this regime and that Tau adopts compact conformations in the monomeric state. If the force field modifications are not well justified, the mechanistic conclusions drawn from these simulations are uncertain.
- **Resolution test** The authors should provide a more detailed description of the force field modification procedure, including the specific amino acid pairs sampled, the range of salt concentrations explored, and the sensitivity of the results to the choice of λH. Ideally, they should show that the modified force field reproduces experimental observables beyond the phase diagram, such as single-molecule FRET efficiencies or Rg values.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Evidence quality
- **Claim pointer** The authors claim that "intramolecular interactions responsible for stabilizing the compact conformations of monomeric Tau correlate with the intermolecular interactions driving the LLPS of Tau."
- **Evidence pointer** Figure, Figure S4
- **Concern** The correlation between intramolecular and intermolecular interaction patterns is inferred from comparing contact maps of monomer simulations and LLPS simulations. However, the manuscript does not provide a quantitative measure of this correlation. The statement that "the interchain contact numbers between these oppositely charged residues are much higher than intrachain contact numbers in LLPS simulation" is qualitative. Moreover, the claim that intramolecular interactions are "converted" into intermolecular interactions during LLPS is a mechanistic interpretation that is not directly tested.
- **Why it matters** This is presented as a key mechanistic insight of the paper. Without quantitative analysis, the strength of the correlation and the validity of the conversion mechanism remain unclear.
- **Resolution test** The authors should compute a quantitative correlation coefficient between intramolecular contact maps in the monomer state and intermolecular contact maps in the LLPS state. They could also test the conversion hypothesis by analyzing whether the specific residue pairs that form intramolecular contacts in the monomer are the same pairs that form intermolecular contacts in the condensate.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the smFRET histograms for the native state were fitted to a double Gaussian function to obtain the peak position" and that "the histograms for the LLPS state were fitted to a Gaussian function plus a γ function."
- **Evidence pointer** Methods section "Single-Molecule FRET Experiments and Data Analysis", Table S1
- **Concern** The fitting procedures are described but the rationale for choosing these specific functional forms is not provided. For the native state, a double Gaussian implies two distinct conformational populations, but the physical basis for this is not discussed. For the LLPS state, the use of a γ function to describe the "zero peak" is mentioned but the parameters and their interpretation are not given. The number of molecules analyzed, the selection criteria for bursts, and the uncertainty in the fitted peak positions are not reported.
- **Why it matters** The quantitative FRET efficiency values and their shifts are central to the paper's conclusions. Without proper reporting of the fitting procedures and uncertainties, the reliability of these values cannot be assessed.
- **Resolution test** The authors should provide representative fits for each condition, report the number of molecules and bursts analyzed, and provide confidence intervals for the fitted peak positions. They should also justify the choice of fitting functions based on the expected conformational distributions.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure B
- **Evidence pointer** Figure B
- **Issue** The figure panels are not clearly labeled in the text. The authors refer to "Figure B" for both the Phase Scan data and the smFRET histograms, which is confusing. The figure numbering appears to be inconsistent throughout the manuscript.
- **Required correction** The authors should ensure that all figures are properly numbered and referenced consistently throughout the text.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods section
- **Evidence pointer** Methods section "Protein Expression and Purification"
- **Issue** The methods state that the Tau gene was "generously provided by Prof. Jianzhi Wang and Rong Liu" and that the four dual-Cys variants were "constructed previously." No details are given on how the cysteine mutations were introduced or verified.
- **Required correction** The authors should provide details on the mutagenesis procedure and verification of the constructs, or cite the original publication where these variants were first described.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The discussion states that "conformational expansion is likely a ubiquitous characteristic of IDPs in their phase-separated state." This generalization is based on a limited number of examples and may be overstated given the diversity of IDP systems.
- **Required correction** The authors should temper this claim or provide a more comprehensive review of the literature to support the generalization.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical completeness
- **Affected element** Methods section "Coarse-Grained Langevin Dynamics Simulations"
- **Evidence pointer** Methods section
- **Issue** The simulation protocol describes a temperature annealing procedure from 150 K to 310 K, but the rationale for this specific protocol and the equilibration time at each temperature are not specified.
- **Required correction** The authors should provide more details on the simulation protocol, including equilibration times, the number of independent simulations, and the criteria used to determine that equilibrium was reached.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that Tau "undergoes conformational transitions from compact to extended states during LLPS, irrespective of diverse driving forces." This is a strong claim that is not fully supported by the data presented, particularly given the concerns about smFRET interpretation in condensed phases.
- **Required correction** The authors should consider softening this claim in the abstract or providing stronger evidence to support it.

## Risk / unsupported claims
1. The claim that smFRET directly observes conformational transitions during LLPS is not fully supported due to potential intermolecular FRET contributions in condensed phases and the confounding effects of PEG-induced crowding.
2. The quantitative correspondence between the modified HPS force field (λH = 1.1) and experimental high-salt conditions (~3 M NaCl) is not adequately justified.
3. The claim that intramolecular interactions are "converted" into intermolecular interactions during LLPS is a mechanistic interpretation that is not directly tested.
4. The generalization that conformational expansion is "ubiquitous" among IDPs in phase-separated states is not supported by the data presented in this study alone.
5. The statement that "the simulation results are in good agreement with the smFRET data" is not quantitatively demonstrated, as no direct comparison of FRET efficiencies and simulated distances is provided.