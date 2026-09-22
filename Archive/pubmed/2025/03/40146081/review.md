## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusions) as provided
- **Assessment boundary** Scientific content, methodological soundness, and support of claims based solely on the supplied text; no external verification of data or methods beyond what is described
- **Shared manuscript claim summary** The authors report an integrative study of wild-type HSPB1 chaperone oligomers using MAS NMR spectroscopy (including fast 1H-based methods), split-intein segmental labeling, cryoEM, mass photometry, AUC, and MD simulations. They claim that the N-terminal domain is rigid and conformationally heterogeneous, the α-crystallin domain forms dimers with multiple local environments, the C-terminal domain is dynamic, and that client protein FUS LC induces oligomer disassembly and that the NTD is essential for partitioning into condensates.
- **Visible evidence base** Abstract, full Introduction, full Results sections (including figure references), full Discussion, full Conclusions, Acknowledgments
- **Missing materials affecting confidence** Figures and supplementary figures referenced but not provided; Materials and Methods section not provided; experimental details for NMR, mass photometry, AUC, cryoEM, and simulations not available; sequence numbering and construct details not fully verifiable

## Reviewer
- **Overall assessment** This manuscript presents a technically ambitious and largely well-integrated study of a challenging biological system. The combination of segmental isotopic labeling with fast MAS NMR and MD simulations is appropriate and potentially powerful. However, the evidence as presented in the text alone is insufficient to fully evaluate several central claims, particularly regarding the atomic-resolution description of conformational heterogeneity, the interpretation of NMR spectra without assigned resonances, and the quantitative basis for oligomer disassembly in the presence of client. The manuscript would benefit from clearer presentation of experimental validation and from tempering of some conclusions that currently outpace the visible evidence.
- **Who would be interested in the results, and why** Researchers in the fields of molecular chaperones, protein homeostasis, biomolecular NMR methodology, and phase separation biology. The methodological advances in segmental labeling for MAS NMR of heterogeneous oligomers will interest NMR spectroscopists. The proposed model of HSPB1 oligomer architecture and client-induced remodeling will interest the chaperone and stress biology communities.
- **Major strengths** The use of split-intein segmental labeling to isolate domain-specific NMR signals in a heterogeneous oligomer is a significant technical achievement. The integration of multiple biophysical methods (mass photometry, AUC, cryoEM, NMR, MD) is commendable. The study addresses a long-standing gap in understanding wild-type HSPB1 oligomer structure and dynamics. The discussion of NTD sequestration and its functional implications is thoughtful and well contextualized.
- **Major Concerns** See detailed items below.
- **Who would be interested in the results, and why** See above.
- **Assessment against Nature-style criteria** See detailed section below.
- **Recommendation posture** Supportive if technical concerns are resolved.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that the N-terminal domain of HSPB1 is rigid and adopts an ensemble of heterogeneous conformations in the oligomer context, based on CP-based NMR signals from a segmentally labeled NTD sample.
- **Evidence pointer** Results section "Segmental Labeling Facilitates Unambiguous Characterization of HSPB1 Domains"; Figures 2c, 2d; Supplementary Figures S7, S8
- **Concern** The claim of NTD rigidity and conformational heterogeneity rests on the interpretation of 13C–13C CP spectra with broad line shapes. However, the text does not provide quantitative line width analysis, relaxation measurements, or comparison to a properly disordered control. The statement that chemical shifts are "consistent with random coil" based on comparison to BMD database distributions is qualitative and does not establish the degree of heterogeneity or distinguish between static disorder and dynamic averaging on multiple timescales. The minor α-helical component is identified but not quantified or assigned to specific residues.
- **Why it matters** The central novelty of the paper is the atomic-resolution description of HSPB1 oligomer domains. Without quantitative NMR analysis, the claim of "atomic resolution" is not supported, and the distinction between rigid heterogeneity and other dynamic regimes is not established.
- **Resolution test** Provide quantitative line width analysis, 13C T1ρ or other relaxation data for the NTD signals, and a more rigorous comparison of chemical shifts to random coil libraries including error estimates. If possible, assign at least a subset of resolved NTD resonances to specific residues to support the heterogeneity claim.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that the ACD exists in multiple distinct local environments within the oligomer, based on the fast MAS 1H–15N spectrum showing resolved peaks and a crowded center.
- **Evidence pointer** Results section "Fast 1H-Based MAS NMR Spectroscopy Captures Heterogeneous Environments in the ACD"; Figure 3a; Supplementary Figures S11, S12
- **Concern** The interpretation of the 1H–15N spectrum relies on comparison to solution NMR assignments from three different constructs (monomer, dimer, NTD-dimer). The text states that "we cannot exclude the presence of monomeric-like environments" for some residues, which undermines the specificity of the conclusion. The number of distinct environments is not determined, and the assignment of specific peaks to occupied versus empty groove states is not demonstrated. The statement that S155 and S156 "do not have easily identifiable matches" is presented without explanation of what this means for the interpretation.
- **Why it matters** The claim of multiple ACD environments is a key result that supports the heterogeneity model. Without clear assignment or at least a systematic analysis of peak counts and chemical shift distributions, the conclusion remains speculative.
- **Resolution test** Provide a more detailed analysis of the 1H–15N spectrum, including peak counting, chemical shift comparison to the three solution constructs with quantitative criteria for "match," and a discussion of why S155/S156 are not observed. If possible, perform 2D or 3D experiments to resolve the crowded center and assign at least diagnostic residues.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that HSPB1 higher order oligomers disassemble into smaller oligomeric species in the presence of FUS LC, based on mass photometry experiments.
- **Evidence pointer** Results section "HSPB1 Oligomer Size Decreases in the Presence of a Client Protein"; Figure 5a; Supplementary Figure S19
- **Concern** The mass photometry data are described qualitatively. The text states that a peak "initially centered around 85 kDa increased in intensity and moved to a higher molecular weight distribution centered around 160 kDa" and that the "high molecular weight oligomeric peak (centered around 440 kDa) decreased." However, no quantitative analysis is provided, such as peak fitting, mass distributions, or statistical comparison across conditions. The interpretation that the 160 kDa peak "could contain a mixture" of species is acknowledged but not resolved. The claim of disassembly is inferred from peak intensity changes but alternative explanations (e.g., differential binding, changes in refractive index) are not excluded.
- **Why it matters** The client-induced remodeling of HSPB1 oligomers is a major functional claim of the paper. Without quantitative mass photometry analysis, the conclusion is not robustly supported.
- **Resolution test** Provide quantitative analysis of mass photometry data, including fitted mass distributions, peak assignments, and statistical comparison across FUS LC concentrations. Discuss and exclude alternative interpretations, such as changes in protein shape or refractive index affecting mass measurements.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the NTD is essential for HSPB1 partitioning into FUS LC condensates, based on coarse-grained simulations of HSPB1 constructs with and without the NTD.
- **Evidence pointer** Results section "NTD is Essential for HSPB1 Dimer Partitioning into FUS LC Condensates"; Figure 6c; Supplementary Figure S23
- **Concern** The coarse-grained simulations use the HPS-Urry model, but the text does not provide sufficient detail on the parametrization of HSPB1 constructs, the validation of the model for this system, or the statistical sampling of the simulations. The conclusion that NTD removal reduces partitioning is based on a comparison of dilute phase concentrations, but the magnitude of the effect and the error bars are not reported in the text. The relationship between the simulation results and the experimental NMR relaxation data (Figure S22) is not quantitatively connected.
- **Why it matters** The claim that the NTD is essential for condensate partitioning is a key functional conclusion. Without robust simulation analysis and connection to experiment, the claim is not fully supported.
- **Resolution test** Provide details on simulation parameters, convergence, and error analysis. Quantitatively compare simulation predictions with experimental partitioning data. Discuss limitations of the coarse-grained model for capturing specific NTD-client interactions.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The authors state that "we could not obtain sequential residue assignments at this time" for the fast MAS NMR spectra of the ACD.
- **Evidence pointer** Results section "Fast 1H-Based MAS NMR Spectroscopy Captures Heterogeneous Environments in the ACD"
- **Concern** The lack of sequential assignments limits the interpretability of the NMR data. The authors rely on comparison to solution NMR assignments from different constructs, which is reasonable but not definitive. The absence of assignments means that the "atomic resolution" claim in the title is not fully met for the oligomer state.
- **Why it matters** The title and abstract promise atomic-resolution characterization. Without assignments, the resolution achieved is at the level of residue-type and secondary structure propensity, not atomic detail.
- **Resolution test** Either obtain assignments through additional experiments (e.g., 3D correlation experiments on labeled samples) or temper the language in the title and abstract to reflect the achieved resolution.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "at atomic resolution" in the title and abstract is not fully supported by the data presented, given the lack of sequential assignments and the qualitative nature of some NMR analyses.
- **Required correction** Consider revising to "at residue-level resolution" or "with domain-specific resolution" to accurately reflect the achieved detail.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section "HSPB1 Forms Cage-like Polydisperse Oligomers with Heterogeneous Architectures"
- **Evidence pointer** Figure 1c; Supplementary Figure S3
- **Issue** The cryoEM data are mentioned but not described in detail. The text states that 2D classes appear cage-like but that secondary structure could not be resolved. No information is provided on the number of particles, resolution, or classification.
- **Required correction** Provide a brief description of cryoEM data quality, including particle counts and any resolution estimates, or clearly state that these are preliminary observations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section "HSPB1 Oligomer Size Decreases in the Presence of a Client Protein"
- **Evidence pointer** Figure 5a
- **Issue** The mass photometry data are described in terms of peak centers and intensity changes, but the figure is not provided. The text would benefit from a clearer description of the experimental conditions, including protein concentrations and buffer conditions.
- **Required correction** Add a brief description of experimental conditions for mass photometry and clarify the concentration range over which the observed changes occur.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion section, paragraph on NTD sequestration
- **Evidence pointer** Discussion, fourth paragraph
- **Issue** The proposal that HSPB1 oligomers may function as NTD "storage" units is speculative and not directly tested in this study.
- **Required correction** Clearly label this as a hypothesis and suggest future experiments that could test it.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods (not provided)
- **Evidence pointer** Not applicable
- **Issue** The manuscript text references a Materials and Methods section that was not provided. Key experimental details, such as NMR acquisition parameters, simulation protocols, and sample preparation, are not available for evaluation.
- **Required correction** Ensure that the full Materials and Methods section is available for review, as it is essential for assessing reproducibility.

## Risk / unsupported claims
- The claim of "atomic resolution" in the title and abstract is not fully supported by the evidence presented, given the lack of sequential NMR assignments and the qualitative nature of some analyses.
- The claim that the NTD is rigid and heterogeneous is based on qualitative spectral interpretation without quantitative line width or relaxation analysis.
- The claim of multiple ACD environments is inferred from comparison to solution NMR constructs without definitive assignment.
- The claim of client-induced oligomer disassembly is based on qualitative mass photometry observations without quantitative analysis.
- The conclusion that the NTD is essential for condensate partitioning relies on coarse-grained simulations whose parameters and validation are not fully described.
- The functional model proposing NTD "storage" units is speculative and not directly tested.