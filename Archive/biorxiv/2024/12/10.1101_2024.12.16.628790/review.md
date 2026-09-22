## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods summary) from bioRxiv preprint
- **Assessment boundary** Scientific content, technical soundness, and claims as presented in the provided text; no assessment of supplementary figures or data beyond what is described
- **Shared manuscript claim summary** The authors present an integrative approach combining segmental isotopic labeling, MAS NMR spectroscopy, molecular dynamics simulations, and other biophysical methods to characterize the conformational heterogeneity of wild-type HSPB1 chaperone oligomers. They claim that the N-terminal domain is rigid but conformationally heterogeneous, the α-crystallin domain forms dimers with multiple local environments, the C-terminal domain is dynamic, and that HSPB1 oligomers disassemble into smaller species in the presence of client proteins, with the NTD being essential for partitioning into condensates.
- **Visible evidence base** Main text figures 1-6 as described, supplementary figures S1-S23 as referenced, methods summary in supporting information
- **Missing materials affecting confidence** Full methods details, actual spectra and data points, cryoEM micrographs and processing statistics, mass photometry histograms, AUC traces, simulation parameters and convergence criteria, NMR assignment tables, and all supplementary figures

## Reviewer

- **Overall assessment** This manuscript addresses a significant and technically challenging problem: characterizing the structural and dynamic properties of wild-type HSPB1 oligomers, which have remained elusive due to their polydispersity and heterogeneity. The authors employ a sophisticated combination of segmental isotopic labeling via split-intein chemistry, fast MAS NMR, and computational modeling. The approach is innovative and the results, if fully supported by the data, would represent a substantial advance in understanding sHSP biology. However, the manuscript as presented has several critical gaps in evidence that prevent full evaluation of the central claims. The NMR data interpretation, particularly regarding the assignment of specific conformational states, requires more rigorous support. The computational results, while suggestive, need clearer validation against experimental data. The claim regarding oligomer disassembly in the presence of client proteins is based primarily on mass photometry and requires additional orthogonal validation. Overall, the work is promising and potentially important, but the current evidence base is insufficient to fully establish the major conclusions.

- **Who would be interested in the results, and why** Structural biologists studying molecular chaperones, particularly small heat shock proteins, would find this work directly relevant. Researchers investigating protein phase separation and biological condensates would be interested in the HSPB1-FUS LC interactions described. Methodologists developing MAS NMR approaches for heterogeneous protein assemblies would value the segmental labeling strategy. The broader protein folding and proteostasis community would be interested in the mechanistic insights into how sHSPs engage clients. The work has potential translational relevance for understanding neurodegenerative diseases where sHSP function is implicated.

- **Major strengths** The combination of segmental isotopic labeling with fast MAS NMR is a technically sophisticated and appropriate approach to address a challenging biological question. The use of multiple orthogonal methods (NMR, mass photometry, AUC, EM, MD simulations) provides complementary perspectives. The focus on wild-type HSPB1, rather than stabilized mutants, addresses a critical gap in the literature. The computational modeling, including both all-atom and coarse-grained simulations, adds mechanistic insight. The work addresses a fundamental question about how sHSPs function in both oligomeric and condensate contexts.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of NMR interpretation
- **Claim pointer** The authors claim that the NTD is rigid and adopts an ensemble of heterogeneous conformations, and that the ACD experiences multiple distinct local environments, based on MAS NMR spectra of segmentally labeled samples.
- **Evidence pointer** Figures 2c-e, 3a, and related text in Results sections "Segmental labeling facilitates unambiguous characterization of HSPB1 domains" and "Fast 1H-based MAS NMR spectroscopy captures heterogeneous environments in the ACD"
- **Concern** The interpretation of the NMR spectra relies heavily on chemical shift comparisons with solution-state assignments and BMRB database distributions, but the authors state that sequential resonance assignments were not obtained. Without assignments, the identification of specific amino acid types and secondary structure elements is speculative. The claim of "multiple distinct local environments" in the ACD is based on peak patterns that could also arise from other sources of line broadening or sample heterogeneity. The comparison with solution NMR assignments from mutant or truncated constructs may not be valid for the wild-type oligomeric state.
- **Why it matters** The central structural claims of the paper depend on correct interpretation of the NMR data. If the spectral interpretation is incorrect or overinterpreted, the conclusions about NTD conformation and ACD heterogeneity would be undermined. The lack of assignments prevents verification of the specific interactions and conformations claimed.
- **Resolution test** Provide sequential resonance assignments or at minimum site-specific labeling to confirm the identity of the observed correlations. Show that the observed peak patterns are reproducible across multiple preparations. Demonstrate that the line broadening is due to conformational heterogeneity rather than other factors such as paramagnetic relaxation or sample degradation. Provide quantitative analysis of peak positions and widths compared to the solution-state references.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Support for oligomer disassembly claim
- **Claim pointer** The authors claim that HSPB1 oligomers disassemble into smaller oligomeric species in the presence of FUS LC, based on mass photometry data showing a decrease in high molecular weight peak intensity and an increase in lower molecular weight species.
- **Evidence pointer** Figure 5a, text in Results section "HSPB1 oligomer size decreases in the presence of a client protein"
- **Concern** The mass photometry data interpretation is complicated by the fact that FUS LC itself forms oligomers in the absence of HSPB1, as noted by the authors. The overlapping molecular weight ranges of FUS LC oligomers, HSPB1 oligomers, and potential complexes make it difficult to unambiguously assign the observed changes to HSPB1 disassembly. The authors acknowledge that the lower molecular weight peak "could contain a mixture" of species, which undermines the strength of the conclusion. No control experiments are described to distinguish between these possibilities.
- **Why it matters** The claim that HSPB1 oligomers disassemble in the presence of clients is a key mechanistic finding with implications for understanding sHSP function. If this claim is not robustly supported, the proposed model of client engagement is weakened.
- **Resolution test** Perform mass photometry with fluorescently labeled HSPB1 to track the oligomeric state specifically. Use size exclusion chromatography coupled with multi-angle light scattering to independently verify oligomer size distributions. Conduct cross-linking experiments to capture the oligomeric state in the presence and absence of FUS LC. Provide quantitative analysis of the mass photometry distributions with appropriate controls for FUS LC alone at matched concentrations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Validation of computational models
- **Claim pointer** The authors claim that MD simulations reveal NTD-NTD and NTD-ACD interactions that mediate oligomer assembly, and that the NTD is sequestered within the oligomer interior.
- **Evidence pointer** Figure 4, text in Results section "The NTD interacts with the ACD grooves and mediates HSPB1 oligomerization"
- **Concern** The computational models are based on AlphaFold2 predictions, which have known limitations for predicting the structure of partially disordered proteins like HSPB1. The authors acknowledge low confidence scores for the NTD, yet use these predictions as the basis for detailed interaction analysis. The MD simulations are described as microsecond-scale, but no convergence analysis or validation against experimental data is presented. The claim that the NTD is sequestered in the oligomer interior is not directly tested experimentally.
- **Why it matters** The proposed structural model of the oligomer, including the role of the NTD in mediating assembly, depends critically on the accuracy of the computational predictions. If the models are not well-validated, the mechanistic conclusions are speculative.
- **Resolution test** Validate the computational models against the experimental NMR data, for example by comparing predicted chemical shifts or contacts with observed spectra. Perform additional simulations with different starting conditions to test convergence. Use experimental approaches such as hydrogen-deuterium exchange or cross-linking mass spectrometry to test the predicted NTD sequestration and interaction interfaces.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the approach and conclusions
- **Claim pointer** The authors claim that their approach is applicable to other complex biological systems and that their findings reveal general principles of sHSP function in condensates.
- **Concern** The study focuses on a single sHSP (HSPB1) and a single client (FUS LC). The authors do not test whether their findings extend to other sHSPs or clients. The claim that the NTD is essential for partitioning into condensates is based on a single construct (HSPB1-ΔNTD) and a single client system. The generality of the proposed mechanism is therefore not established.
- **Why it matters** The broader significance of the work depends on whether the findings are generalizable. If the observed behaviors are specific to HSPB1 or FUS LC, the impact is more limited.
- **Resolution test** Test the partitioning behavior of other sHSPs or HSPB1 variants with different clients. Examine whether the NTD requirement for partitioning is conserved across different client proteins. Compare the oligomeric behavior of HSPB1 with other sHSPs under similar conditions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, Introduction
- **Issue** The abstract and introduction are dense and use specialized terminology without sufficient context for a general scientific audience. The significance of the segmental labeling approach and the specific advantages of fast MAS NMR over conventional methods could be explained more clearly.
- **Required correction** Provide brief explanations of key techniques and their advantages in the introduction. Consider adding a schematic figure showing the domain architecture and labeling strategy.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Quantitative rigor
- **Affected element** Mass photometry analysis
- **Evidence pointer** Figure 5a
- **Issue** The mass photometry data are described qualitatively (peaks "increased," "decreased," "shifted") without quantitative analysis. No error bars, replicate numbers, or statistical tests are mentioned.
- **Required correction** Provide quantitative analysis of the mass photometry distributions including mean molecular weights, peak widths, and statistical comparison between conditions. Include information on the number of replicates and variability.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** NMR experiments
- **Evidence pointer** Materials and Methods summary
- **Issue** The methods section is a summary that refers to a supplementary file. Key experimental parameters for the NMR experiments (e.g., magnetic field strengths, MAS frequencies, temperatures, pulse sequences, acquisition times) are not provided in the main text.
- **Required correction** Include key NMR experimental parameters in the main text or ensure the supplementary file is accessible and complete.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation of relaxation data
- **Affected element** T1ρ relaxation measurements
- **Evidence pointer** Figure S22, Results section "The NTD is essential for HSPB1 dimer partitioning into FUS LC condensates"
- **Issue** The T1ρ relaxation data are described as showing decreased values in the presence of FUS LC, interpreted as changes in dynamics. However, T1ρ relaxation can be affected by multiple factors including chemical exchange, dipolar coupling, and sample heterogeneity. The interpretation of decreased T1ρ as indicating specific dynamic changes is not fully justified.
- **Required correction** Provide additional analysis or discussion of the factors contributing to T1ρ relaxation changes. Consider complementary relaxation measurements or dynamic studies to support the interpretation.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 1
- **Evidence pointer** Figure 1c
- **Issue** The cryoEM 2D classes are described as cage-like, but the figure is not shown in the provided text. The quality and resolution of these classes cannot be assessed.
- **Required correction** Ensure the figure clearly shows the 2D classes with scale bars and sufficient resolution to support the cage-like interpretation.

## Risk / unsupported claims

1. The claim that the NTD is rigid in the oligomer context is based on the absence of INEPT signals in the NTD-labeled sample. This is an indirect measurement and could also be explained by intermediate timescale dynamics or relaxation properties that make signals undetectable. The claim requires additional support.

2. The claim of "multiple distinct local environments" in the ACD is based on peak patterns in 2D spectra without sequential assignments. This interpretation is not fully supported.

3. The claim that HSPB1 oligomers disassemble into smaller species in the presence of FUS LC is based on mass photometry data that cannot unambiguously distinguish between HSPB1 disassembly and FUS LC oligomerization effects.

4. The claim that the NTD is sequestered within the oligomer interior is based on computational predictions that have not been experimentally validated.

5. The claim that the approach is applicable to other complex biological systems is not tested and is therefore speculative.

6. The functional significance of the observed conformational heterogeneity for chaperone activity is not directly demonstrated.

7. The relationship between the in vitro observations and the behavior of HSPB1 in cellular contexts is not established.

8. The claim that NTD phosphorylation controls the transition from higher-order assemblies to smaller oligomers is based on literature citations rather than direct experimental evidence in this study.

9. The statement that the CTD acts as a solubility tag is supported by literature but not directly tested in this work.

10. The claim that the NTD is essential for HSPB1 partitioning into condensates is based on a single deletion construct and requires validation with additional mutants or approaches.