## Review setup
- **Input scope** Full manuscript text including abstract, methods, results, discussion, and conclusion
- **Assessment boundary** Scientific content, methodological rigor, and interpretation of results as presented in the manuscript
- **Shared manuscript claim summary** The authors use atomistic molecular dynamics simulations to investigate the coupled binding and folding mechanisms of two SPIN homolog N-terminal domains (NTDs) with myeloperoxidase (MPO). They report that SPIN-aureus NTD follows a cooperative binding and folding mechanism, while SPIN-delphini NTD follows a conformational selection-like mechanism, and that these differences correlate with residual structural propensities in the unbound state.
- **Visible evidence base** Simulation results presented in Figures 1-5 and Supplementary Figures S1-S4, with kinetic analyses and free energy surfaces derived from high-temperature (450 K) and room temperature (300 K) simulations
- **Missing materials affecting confidence** Supplementary Tables S1-S3 referenced but not provided; specific simulation trajectory data and force field validation details not fully described; experimental validation data not included

## Reviewer
- **Overall assessment** The manuscript presents an interesting computational study addressing a biologically relevant question about the coupled binding and folding mechanisms of disordered protein regions. The authors identify a potentially important mechanistic difference between two SPIN homologs that could explain their differential inhibitory activities. However, the study relies entirely on high-temperature simulations to infer mechanisms, and the extrapolation to physiological conditions requires more careful justification. The connection between simulated mechanisms and experimentally observed functional differences remains speculative without direct experimental validation or more rigorous sampling analysis.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins and their coupled binding and folding mechanisms, computational biophysicists interested in protein-protein interactions, and microbiologists studying host-pathogen interactions and bacterial immune evasion strategies would find this work relevant. The study provides a comparative analysis of two homologous systems that could inform broader understanding of how sequence variations modulate binding mechanisms.
- **Major strengths** The study addresses a timely and important question about IDP binding mechanisms using a comparative approach with two closely related homologs. The use of atomistic simulations with a modern force field (CHARMM36m) optimized for both folded and disordered proteins is appropriate. The authors provide a clear conceptual framework distinguishing cooperative, induced folding, and conformational selection mechanisms, and their analysis of free energy surfaces and kinetic data is methodical. The observation that β-hairpin forming IDPs may follow different mechanisms than helix-forming IDPs is a potentially valuable contribution.
- **Major Concerns** The reliance on high-temperature (450 K) simulations to infer binding mechanisms is a significant concern, as elevated temperatures can alter free energy landscapes and transition pathways. The authors acknowledge this limitation but do not provide sufficient validation that the observed mechanisms are representative of physiological conditions. The study lacks experimental validation or comparison with experimental kinetic data. The relationship between simulated mechanisms and the experimentally measured IC50 values is inferred but not directly demonstrated. The sampling in the room temperature simulations of free NTDs appears limited (20 replicas × 50 ns), which may be insufficient to characterize conformational ensembles of disordered proteins.
- **Minor Comments** The manuscript contains some typographical errors and inconsistent terminology. The authors use "SPIN" and "SPN" interchangeably in places. The description of the double exponential fitting procedure could be more detailed. The criteria for selecting trajectory segments for contact map calculations could be more clearly justified. The authors should clarify whether the restrained MPO segments could influence the observed unbinding pathways.
- **Technical failings that need to be addressed before the case is established** The lack of convergence analysis for the high-temperature simulations is a critical issue. The authors do not demonstrate that the observed differences between the two systems are statistically robust rather than arising from limited sampling. The absence of error bars or uncertainty estimates on the reported kinetic parameters and free energy surfaces weakens the quantitative claims. The authors should provide replica-to-replica variability analysis and assess whether the observed mechanistic differences are consistent across independent simulations.
- **Assessment against Nature-style criteria** Originality: The study addresses a relatively unexplored area of IDP binding mechanisms for β-hairpin forming regions, which provides some novelty. However, the conceptual framework of coupled binding and folding mechanisms is well established. Scientific importance: The potential link between binding mechanisms and differential inhibitory activities of SPIN homologs is interesting but the direct relevance to therapeutic development is overstated. Interdisciplinary readership: The work bridges computational biophysics and microbiology, which could attract readers from both fields, though the technical nature may limit broader appeal. Technical soundness: The simulation methodology is generally appropriate, but the lack of rigorous convergence analysis and validation of high-temperature extrapolation weakens the technical foundation. Readability for nonspecialists: The manuscript is reasonably well-written but assumes familiarity with IDP concepts and simulation techniques, which may limit accessibility.

## Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that high-temperature (450 K) simulations reveal the coupled binding and folding mechanisms of SPIN NTDs, and that these mechanisms differ between SPIN-aureus (cooperative) and SPIN-delphini (conformational selection-like).
- **Evidence pointer** Results section, Figures 3 and 4, Supplementary Figures S2 and S3
- **Concern** The use of 450 K simulations to infer binding mechanisms at physiological temperature is not adequately justified. Elevated temperatures can alter the relative populations of conformational states, change the heights of free energy barriers, and potentially activate non-physiological pathways. The authors acknowledge this limitation in the conclusion but do not provide any validation that the observed mechanisms are representative of lower temperature behavior. No temperature-dependent analysis or comparison with lower temperature simulations is provided.
- **Why it matters** The central claims of the paper regarding mechanistic differences between the two SPIN homologs depend entirely on the assumption that high-temperature simulations faithfully reproduce the physiologically relevant binding mechanisms. If this assumption is not validated, the conclusions may not be applicable to the actual biological system.
- **Resolution test** The authors should provide evidence that the observed mechanisms are robust to temperature, such as by performing simulations at additional temperatures (e.g., 400 K and 425 K) and demonstrating consistent mechanistic behavior, or by using enhanced sampling methods that allow simulations at physiological temperature.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that SPIN-aureus NTD follows a cooperative binding and folding mechanism, while SPIN-delphini NTD follows a conformational selection-like mechanism, based on analysis of unbinding and unfolding kinetics and free energy surfaces.
- **Evidence pointer** Results section, Figures 3 and 4, kinetic fitting analyses
- **Concern** The manuscript does not provide sufficient evidence that the observed mechanistic differences are statistically robust. The kinetic parameters (τ1 and τ2) are reported without error estimates or replica-to-replica variability. The free energy surfaces are derived from selected trajectory segments, and the criteria for segment selection may introduce bias. The authors do not demonstrate that the observed differences between the two systems exceed the expected statistical uncertainty from the limited number of simulations.
- **Why it matters** The central conclusion of the paper is that the two SPIN homologs follow different binding mechanisms. If this difference is not statistically robust, the conclusions are not supported by the data.
- **Resolution test** The authors should provide uncertainty estimates for all reported kinetic parameters, show replica-to-replica variability, and perform statistical tests to demonstrate that the observed mechanistic differences are significant. They should also assess the sensitivity of their conclusions to the trajectory segment selection criteria.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that the observed mechanistic differences between SPIN-aureus and SPIN-delphini NTDs "may help explain why the inhibition strength is not well correlated with binding affinity for different SPIN homologs."
- **Evidence pointer** Abstract, Introduction, Results, Conclusion
- **Concern** The connection between the simulated binding mechanisms and the experimentally observed functional differences (IC50 values) is speculative. The authors do not provide a quantitative or even semi-quantitative framework linking the simulated mechanistic differences to the experimentally measured inhibition strengths. The statement that the mechanisms "may help explain" the lack of correlation is not supported by direct evidence.
- **Why it matters** The potential to explain the experimentally observed lack of correlation between binding affinity and inhibition strength is a key motivation for the study. Without a more direct link between the simulated mechanisms and functional outcomes, the biological significance of the findings remains unclear.
- **Resolution test** The authors should either provide a more quantitative framework connecting the simulated mechanisms to inhibition strengths, or temper their claims about the functional implications of their findings.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that room temperature simulations of unbound SPIN NTDs reveal that "SPIN-delphini NTD has a much higher propensity to adopt pre-folded hairpin-like conformations" compared to SPIN-aureus NTD.
- **Evidence pointer** Results section, Figure 5
- **Concern** The room temperature simulations of free NTDs are limited to 20 replicas of 50 ns each. For intrinsically disordered proteins, this sampling may be insufficient to obtain converged conformational ensembles, particularly for assessing the population of specific secondary structure elements. The authors do not provide convergence analysis or comparison with experimental data on the unbound state conformations.
- **Why it matters** The claim about differential residual structure in the unbound state is important for supporting the conformational selection-like mechanism for SPIN-delphini. If the sampling is insufficient, the observed differences may not be reliable.
- **Resolution test** The authors should provide convergence analysis for the room temperature simulations, such as block averaging or comparison of independent halves of the trajectories. They should also consider longer simulations or enhanced sampling methods to ensure the conformational ensembles are adequately sampled.

## Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Throughout manuscript
- **Issue** The authors use "SPIN" and "SPN" interchangeably in several places, which could cause confusion.
- **Required correction** Standardize the abbreviation to "SPIN" throughout the manuscript.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Methods section, Analysis subsection
- **Issue** The description of the double exponential fitting procedure is brief and lacks details on the fitting algorithm, initial guesses, and goodness-of-fit assessment.
- **Required correction** Provide more details on the fitting procedure, including the functional form, fitting algorithm, and how the quality of fit was evaluated.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure presentation
- **Evidence pointer** Figures 3 and 4
- **Issue** The free energy surfaces in Figures 3B and 4B would benefit from clearer labeling of the axes and contour levels, and the representative structures in Figure 3C are not clearly described in the figure legend.
- **Required correction** Improve figure legends to clearly describe all panels, including the meaning of contour levels and the structural representations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Supplementary material
- **Evidence pointer** Supplementary Tables S1-S3
- **Issue** The supplementary tables are referenced but not provided in the manuscript text, making it impossible to assess the contact definitions and trajectory segment selections.
- **Required correction** Ensure all supplementary materials are accessible and clearly described in the main text.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Results section, subsection on SPIN-delphini
- **Issue** The authors state that SPIN-delphini NTD "fits the active site of MPO tighter than SPIN-aureus NTD" based on the observation that fewer replicas showed full dissociation. This interpretation may be confounded by the high temperature conditions and the limited sampling.
- **Required correction** Soften this claim or provide additional evidence supporting the interpretation of tighter binding.

## Risk / unsupported claims
- The claim that the observed high-temperature simulation mechanisms are representative of physiological temperature behavior is not supported by direct evidence.
- The claim that the mechanistic differences "may help explain why the inhibition strength is not well correlated with binding affinity" is speculative and not directly supported by the data.
- The claim that SPIN-delphini NTD "fits the active site of MPO tighter" than SPIN-aureus NTD is not directly supported by the simulation data.
- The assertion that the findings "can help us develop new strategies towards treating Staphylococcal infections" is overstated given the purely computational nature of the study and the lack of direct therapeutic implications.
- The statement that "none of these models is capable of describing both folded and disordered protein states" regarding coarse-grained models is too absolute and not fully justified.