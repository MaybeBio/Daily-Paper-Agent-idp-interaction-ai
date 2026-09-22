## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and extended data descriptions
- **Assessment boundary** Scientific content, technical soundness, and claims as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors investigate molecular interactions driving phase separation of FUS SYGQ LC and RGG domains, and co-partitioning with RNA polymerase II CTD, using NMR spectroscopy and molecular simulations. They report that diverse residue types and interaction modes (not solely arginine-tyrosine pairs) contribute to condensed-phase contacts, and that lysines in RNA polymerase II CTD play a role in co-partitioning.
- **Visible evidence base** NMR spectroscopy data (chemical shift perturbations, NOE experiments, relaxation measurements), turbidity assays, fluorescence partitioning assays, microscopy, and all-atom molecular dynamics simulations
- **Missing materials affecting confidence** Raw NMR spectra, simulation trajectories, extended data figures (referenced but not fully visible), supplementary notes, and detailed analysis scripts were not available for full verification

## Reviewer
- **Overall assessment** This manuscript presents a systematic investigation of molecular interactions in FUS phase-separated condensates, extending prior work on single-component systems to multi-component systems including RNA polymerase II CTD. The combination of NMR and simulation approaches is appropriate and the conclusions are largely supported by the presented evidence. The work addresses an important question in the field of biomolecular condensates, though some claims regarding interaction mode quantification would benefit from additional validation. The manuscript is well-written and accessible to a broad structural biology audience.

- **Who would be interested in the results, and why** Researchers studying phase separation and biomolecular condensates, particularly those focused on FUS and FET family proteins, RNA polymerase II transcription machinery, and the molecular mechanisms underlying condensate formation. The findings on diverse interaction modes and the role of lysines in CTD co-partitioning will also interest those working on drug development for FET-associated cancers and neurodegenerative diseases involving FUS.

- **Major strengths**
  1. Direct experimental probing of condensed-phase interactions using advanced NMR methodology, which is technically challenging and provides unique insights
  2. Integration of experimental and computational approaches to provide complementary perspectives
  3. Systematic investigation of multi-component systems, moving beyond simplified single-component studies
  4. Clear demonstration that interactions are distributed across many residue types, challenging oversimplified models focused solely on arginine-tyrosine pairs
  5. Identification of lysine residues in RNA polymerase II CTD as important for co-partitioning, providing new mechanistic insight

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "many residue types, not solely arginine-tyrosine pairs, form condensed-phase contacts via several interaction modes including but not only sp2/π and cation-π interactions" based on NOE experiments and simulations.
- **Evidence pointer** Results section "Contacts between many residue types contribute to FUS LLPS", Figures 3 and 4
- **Concern** The quantification of interaction modes from simulations (Figure 4) relies on geometric criteria for defining hydrogen bonds, sp2/π, and cation-π interactions. The authors acknowledge that these definitions "may require additional refinement based on input from quantum calculations," yet the relative proportions of interaction modes are presented as quantitative findings. The manuscript would benefit from a more explicit statement of the limitations of these geometric criteria and how sensitive the conclusions are to the specific cutoffs chosen. Additionally, the NOE experiments provide qualitative evidence for contacts but cannot directly quantify interaction modes, creating a gap between the experimental observations and the mode-specific conclusions drawn from simulations.
- **Why it matters** The central claim of the paper is that diverse interaction modes contribute to phase separation. If the simulation-based classification of interaction modes is not robust, this claim is weakened. The field needs reliable methods to distinguish between different interaction types to guide therapeutic development.
- **Resolution test** Provide a sensitivity analysis showing how the relative proportions of interaction modes change with different geometric cutoffs for defining hydrogen bonds, sp2/π, and cation-π interactions. Alternatively, validate the simulation predictions with additional experimental approaches that can distinguish interaction modes, such as specific isotope labeling strategies or mutagenesis targeting predicted contact residues.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the observation of NOEs between all major residue types within the SYGQ LC and RGG3 strongly suggest the interactions are distributed across many residue types within the condensed phase."
- **Evidence pointer** Results section "Contacts between many residue types contribute to FUS LLPS", Figure 3
- **Concern** The NOE experiments are performed on condensed phases that are likely highly concentrated and viscous. Under such conditions, spin diffusion can be a significant concern even with short mixing times. While the authors address this with control experiments at shorter mixing times and ROE experiments, the quantitative interpretation of NOE intensities as reflecting contact frequencies remains challenging. The statement that "signal intensities may not quantitatively report on the strength or frequency of contacts due to the differential relaxation properties of various positions" is appropriate, but the qualitative conclusion that interactions are "distributed" could be strengthened by a more systematic analysis of how relaxation properties differ across residue types and how this might bias the observed NOE patterns.
- **Why it matters** The conclusion that interactions are broadly distributed across residue types is a key finding that challenges the field's focus on specific residue pairs. If this conclusion is biased by differential relaxation effects, it could mislead future studies.
- **Resolution test** Provide a more detailed analysis of relaxation properties across different residue types in the condensed phase and demonstrate that the observed NOE patterns are not simply reflecting differences in mobility. Alternatively, use selective labeling strategies to isolate specific residue pairs and confirm the distributed interaction pattern.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors conclude that "hydrogen bond interactions may be more important for LLPS, in general, than currently appreciated in the literature" based on simulation analysis of interaction modes.
- **Evidence pointer** Results section "FUS contacts with the C-terminal tail of RNA polymerase II", Figure 7
- **Concern** This is a broad claim that extends beyond the specific systems studied. The simulations are limited to short fragments (44 residues) of FUS and RNA polymerase II CTD, and the conclusions about hydrogen bonding being generally important for LLPS may not be generalizable to other systems. The authors do acknowledge limitations of their simulation approach, but the claim in the discussion is stated with more confidence than the evidence supports.
- **Why it matters** Overgeneralization from specific systems to general principles can mislead the field. The importance of hydrogen bonding versus other interaction types likely varies across different protein systems.
- **Resolution test** Soften the claim to be specific to the systems studied, or provide additional evidence from other protein systems that hydrogen bonding is generally important for LLPS. Alternatively, clearly state the limitations of extrapolating from the studied fragments to LLPS in general.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the addition of 5 μM ΔSYGQ LC to 50 μM SYGQ LC resulted in increased turbidity due to LLPS" and use this to conclude that "interactions between the SYGQ LC and domains within the ΔSYGQ LC make significant contributions to LLPS of full-length FUS."
- **Evidence pointer** Results section "RGG domains contribute to FUS LLPS", Figure 1C
- **Concern** Turbidity is a non-specific measure that can reflect aggregation, not just liquid-liquid phase separation. The authors do not provide microscopy or other evidence to confirm that the turbidity observed in the mixing experiments corresponds to liquid droplets rather than amorphous aggregates. This is particularly important because the ΔSYGQ LC construct contains folded domains (RRM and zinc finger) that could promote aggregation through non-specific interactions.
- **Why it matters** The conclusion that RGG domains contribute to LLPS specifically, rather than just promoting aggregation, is important for understanding the mechanism. If the observed turbidity reflects aggregation, the conclusions about LLPS would need to be revised.
- **Resolution test** Provide microscopy images (DIC or fluorescence) of the mixed samples to confirm the presence of liquid droplets. Alternatively, use a more specific assay for liquid-liquid phase separation, such as FRAP or rheology measurements.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The abstract states that FUS "mediates phase separation in biomolecular condensates and functions in transcription by clustering with RNA polymerase II." The causal relationship between phase separation and transcription is stated more definitively than the evidence supports.
- **Required correction** Rephrase to indicate that FUS phase separation and transcription function are associated, without implying a direct causal link.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, NMR sample preparation
- **Evidence pointer** Methods section "NMR Sample Preparation and NMR Spectroscopy"
- **Issue** The methods state that condensed phase samples contained 0.4 M residual urea from the storage buffer. Urea is a chaotrope that could affect protein interactions and phase behavior. The potential effects of this residual urea on the measured interactions are not discussed.
- **Required correction** Add a discussion of the potential effects of residual urea on the measurements, or provide control experiments demonstrating that the observed interactions are not significantly affected by urea.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, Figure 3
- **Evidence pointer** Results section "Contacts between many residue types contribute to FUS LLPS"
- **Issue** The description of NOE data in Figure 3 is somewhat dense and difficult to follow. The distinction between intra- and intermolecular NOEs could be clarified.
- **Required correction** Provide a clearer explanation of how intra- and intermolecular NOEs are distinguished in the experimental setup, and consider simplifying the figure presentation.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, Simulation details
- **Evidence pointer** Methods section "Simulation Details and analysis"
- **Issue** The simulation methods state that 16 temperature replicas from 300 K to 500 K were used. The highest temperature of 500 K is quite high for studying protein interactions and may lead to unrealistic conformations that could bias the interaction mode analysis.
- **Required correction** Discuss the potential effects of high-temperature replicas on the results, or provide evidence that the results are not sensitive to the temperature range used.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion
- **Evidence pointer** Discussion, paragraph 3
- **Issue** The discussion of the limitations of the simulation approach is somewhat buried in the text. Given the importance of the simulation results to the main conclusions, this discussion should be more prominent.
- **Required correction** Move the limitations of the simulation approach to a more prominent position in the discussion, or add a dedicated limitations paragraph.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, Figure 7
- **Evidence pointer** Results section "FUS contacts with the C-terminal tail of RNA polymerase II", Figure 7B
- **Issue** The fluorescence partitioning assay uses a single concentration of labeled RNA polymerase II CTD (1 μM). The partitioning behavior could be concentration-dependent, and a single concentration may not capture the full picture.
- **Required correction** Consider performing the partitioning assay at multiple concentrations of labeled RNA polymerase II CTD to assess concentration dependence.

## Risk / unsupported claims
- The claim that "hydrogen bond interactions may be more important for LLPS, in general, than currently appreciated" is not fully supported by the data, which are limited to specific FUS fragments and RNA polymerase II CTD.
- The conclusion that RGG domains contribute to LLPS specifically (rather than aggregation) is based on turbidity measurements that do not distinguish between liquid-liquid phase separation and other forms of aggregation.
- The quantitative proportions of interaction modes (hydrogen bonding, sp2/π, cation-π) derived from simulations should be treated with caution given the acknowledged limitations of the geometric criteria used.
- The statement that "the interactions are distributed across many residue types" is supported by NOE data, but the possibility of differential relaxation effects biasing the observed patterns is not fully addressed.
- The potential effects of residual urea (0.4 M) in NMR samples on the measured interactions are not discussed.