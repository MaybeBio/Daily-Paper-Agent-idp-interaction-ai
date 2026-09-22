## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv, 2024)
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the provided manuscript text. No external data or unpublished materials were consulted.
- **Shared manuscript claim summary** The authors report that C-terminal phosphomimetic substitutions (Ser-to-Asp at S403, S404, S409, S410) in the TDP-43 low complexity domain (LCD) alter the salt dependence of liquid-liquid phase separation (LLPS) from a monotonic to a biphasic response. Using turbidity, fluorescence microscopy, and coarse-grained simulations, they propose that this biphasic behavior arises from a mechanism in which long-range attractive electrostatic interactions, created by the phosphomimetic substitutions, modulate short-range hydrophobic interactions that remain the primary drivers of LLPS.
- **Visible evidence base** Main text figures (Figs. 1-7), supplementary figures (Figs. S1-S3), supplementary table (Table S1), and methods sections (experimental and computational).
- **Missing materials affecting confidence** No raw data files, simulation trajectories, or analysis scripts were provided. The manuscript does not include a figure legend for Figure 1A, and the specific protein concentrations used in turbidity and microscopy experiments are not fully detailed in the text. The exact sequence of the LCD construct (residues 266-414) and the thrombin cleavage site are described, but the final cleaved product's exact boundaries are not explicitly stated.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question: how disease-associated C-terminal phosphorylation of TDP-43 affects its phase separation behavior. The combination of experimental assays and coarse-grained simulations is a strength, and the observation of a biphasic salt dependence for phosphomimetic variants is novel and potentially significant. However, the mechanistic interpretation relies heavily on simulation data, and the experimental validation of the proposed electrostatic modulation mechanism is indirect. The manuscript would be strengthened by additional experimental evidence, such as direct measurement of intermolecular interactions or mutagenesis to disrupt the proposed electrostatic contacts. The claim that the simulations "recapitulate" the experimental data is somewhat overstated given the tuning of the hydrophobic well depth with salt concentration. Overall, the work is of interest to the phase separation and neurodegeneration communities, but the central mechanistic claim requires further support.
- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation, particularly of RNA-binding proteins and low complexity domains. The work is also relevant to the TDP-43 proteinopathy field, as it provides a potential physicochemical link between a disease-associated post-translational modification and altered condensate behavior. The methodological approach (coarse-grained simulations with salt-dependent hydrophobicity) may be of interest to computational biophysicists.
- **Major strengths**
  1. The study addresses a clinically relevant question (effect of pathological phosphorylation on TDP-43 LLPS) that has been largely unexplored experimentally.
  2. The combination of experimental (turbidity, microscopy) and computational (coarse-grained simulations) approaches provides complementary perspectives.
  3. The observation of a biphasic salt dependence for phosphomimetic variants is a clear and novel finding that challenges the simple view that phosphorylation simply suppresses LLPS.
  4. The simulation framework is based on established methods and the authors test for finite size effects.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Mechanistic interpretation
  - **Claim pointer** The central claim that the biphasic salt dependence of phosphomimetic TDP-43 LCD LLPS is due to long-range attractive electrostatic interactions modulating short-range hydrophobic interactions.
  - **Evidence pointer** Figures 3-6, Discussion
  - **Concern** The proposed mechanism is inferred primarily from coarse-grained simulations. The experimental data (turbidity, microscopy) only show the macroscopic phase behavior. The simulations suggest that attractive electrostatic forces are present in the phosphomimetic variants at low salt, but this is not directly validated experimentally. The claim that these electrostatic forces "bring protein monomers together" and thereby promote hydrophobic interactions is a plausible hypothesis, but the evidence presented is correlative. The authors do not provide experimental data that directly tests this mechanism, such as mutations that would specifically disrupt the proposed N-terminal/C-terminal electrostatic attraction without affecting other properties.
  - **Why it matters** The manuscript's main contribution is the proposed mechanism. If the mechanism is not well-supported, the significance of the work is substantially diminished. The distinction between "electrostatic forces drive LLPS" and "electrostatic forces modulate hydrophobic-driven LLPS" is subtle but important, and the current evidence may not be sufficient to definitively distinguish between these and other possibilities.
  - **Resolution test** Provide experimental evidence that directly tests the role of the proposed electrostatic interactions. For example, mutate the N-terminal charged residues to neutralize the "positive pole" and test if the biphasic salt dependence is abolished. Alternatively, use a technique such as small-angle X-ray scattering or NMR to probe intermolecular contacts in the condensates and correlate them with the salt dependence.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Simulation validity
  - **Claim pointer** The claim that the coarse-grained simulations "recapitulate" the experimental phase diagrams (Results, Figure 2C).
  - **Evidence pointer** Figure 2C, Figure S1, Computational Methods
  - **Concern** The simulation model includes an explicit salt-dependent scaling of the hydrophobic well depth (ε), which is tuned to match the experimental phase diagrams at 0 and 1250 mM NaCl. This introduces a parameter that is not derived from first principles and is adjusted to fit the data. The statement that the model "recapitulates" the experimental results is therefore somewhat circular, as the model is calibrated to those results. The authors acknowledge this in the methods, but the strength of the validation is weakened. The comparison between simulated and experimental phase diagrams appears to be qualitative, and a more quantitative comparison (e.g., of csat values) would be more convincing.
  - **Why it matters** The simulation model is the primary tool used to dissect the mechanism. If the model is not independently validated, the mechanistic conclusions drawn from it are less reliable. The salt-dependent ε is a significant assumption that could influence the results.
  - **Resolution test** Provide a more rigorous validation of the simulation model. For example, test the model's predictions against experimental data at intermediate salt concentrations that were not used for calibration. Alternatively, use a model where the salt dependence arises naturally from the electrostatic interactions (e.g., via the Debye screening length) without an ad hoc adjustment of the hydrophobic interaction strength.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Experimental characterization
  - **Claim pointer** The claim that the phosphomimetic variants form liquid droplets, and the comparison of droplet properties (e.g., size) between variants (Figure 1).
  - **Evidence pointer** Figure 1, Methods (Turbidity, Fluorescence Microscopy)
  - **Concern** The manuscript reports that 4-PM TDP-43 LCD forms "much smaller" droplets than the other proteins, but this observation is not quantified or analyzed in detail. The turbidity data show differences in the extent of phase separation, but the relationship between turbidity and droplet size is not straightforward. The microscopy images are mentioned but not shown in the provided text. A more detailed characterization of the condensates (e.g., size distribution, morphology, viscosity, or FRAP to assess dynamics) would strengthen the claim that these are liquid-like and would provide a more complete picture of how the phosphomimetic substitutions alter condensate properties.
  - **Why it matters** The manuscript focuses on the mechanism of LLPS, but the physical properties of the condensates are also relevant to their potential function and pathology. The observation of smaller droplets for 4-PM could be an important finding, but it is not explored.
  - **Resolution test** Provide quantitative analysis of droplet size and morphology from microscopy images. Perform additional characterization, such as FRAP or rheology, to confirm liquid-like behavior and assess differences between variants.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Figure 1A
  - **Evidence pointer** Figure 1A
  - **Issue** The text refers to Figure 1A, which presumably shows a schematic of the constructs, but no figure legend is provided in the manuscript text.
  - **Required correction** Provide a figure legend for Figure 1A, or describe the schematic in the text.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods (Turbidity, Microscopy)
  - **Evidence pointer** Methods
  - **Issue** The exact protein concentrations used in the turbidity and microscopy experiments are not explicitly stated in the text. The csat values are mentioned, but the range of concentrations tested is not clear.
  - **Required correction** Specify the protein concentration ranges used in the experiments.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interpretation
  - **Affected element** Discussion
  - **Evidence pointer** Discussion
  - **Issue** The authors state that the difference in csat between WT and phosphomimetic variants at 150 mM NaCl is "modest" (within a 4 μM range). This is an important point, as it suggests that at physiological ionic strength, the phosphomimetic substitutions have a relatively small effect on phase separation propensity. This could be highlighted more prominently, as it has implications for the relevance of the findings to disease.
  - **Required correction** Consider discussing the physiological relevance of the modest differences at 150 mM NaCl more explicitly.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Discussion
  - **Evidence pointer** Discussion
  - **Issue** The authors mention that authentic phosphorylation may impart a larger negative charge than a phosphomimetic substitution, but they do not discuss the potential limitations of the phosphomimetic approach in more detail. For example, phosphomimetics do not fully recapitulate the effects of phosphorylation on protein structure and interactions.
  - **Required correction** Add a brief discussion of the limitations of the phosphomimetic approach.
- **Technical failings that need to be addressed before the case is established**
  - R1-M1: The mechanistic claim requires direct experimental testing.
  - R1-M2: The simulation model's validation is weakened by the salt-dependent tuning of the hydrophobic well depth.
- **Assessment against Nature-style criteria**
  - **Originality** The finding of a biphasic salt dependence for phosphomimetic TDP-43 LCD is novel. The proposed mechanism (electrostatic modulation of hydrophobic interactions) is a reasonable hypothesis that has not been previously proposed for this system. However, the concept of competing electrostatic and hydrophobic interactions in phase separation is not entirely new.
  - **Scientific importance** The work addresses a clinically relevant question and provides a potential physicochemical basis for understanding how a disease-associated modification alters TDP-43 phase behavior. The findings could have implications for understanding the role of phosphorylation in TDP-43 pathology. However, the physiological relevance is tempered by the modest effects observed at 150 mM NaCl.
  - **Interdisciplinary readership** The work will appeal to researchers in biophysics, cell biology, and neurodegeneration. The combination of experimental and computational approaches broadens its appeal.
  - **Technical soundness** The experimental methods are standard and appear sound. The simulation methods are based on established approaches, but the validation is a concern (R1-M2). The force analysis is a useful tool, but its interpretation is limited by the model's assumptions.
  - **Readability for nonspecialists** The manuscript is generally well-written and accessible. The concepts of phase separation and phosphomimetics are explained adequately. The results section is clear, but the discussion of the simulation details may be challenging for some readers.
- **Recommendation posture** Supportive if technical concerns are resolved. The core observation is interesting and potentially important, but the central mechanistic claim is not fully established from the provided evidence. The authors should provide additional experimental support for the proposed mechanism and address the concerns regarding the simulation model's validation.

## Risk / unsupported claims
- The claim that the biphasic salt dependence is due to "long-range attractive electrostatic interactions" modulating hydrophobic interactions is not directly supported by experimental data and relies on simulation inferences.
- The claim that the simulations "recapitulate" the experimental phase diagrams is weakened by the calibration of the hydrophobic well depth to the experimental data.
- The statement that 4-PM TDP-43 LCD forms "much smaller" droplets is not quantified or supported by shown data.
- The extrapolation of findings from the phosphomimetic model to authentic phosphorylation is speculative, as the authors acknowledge, but the potential differences are not discussed in detail.