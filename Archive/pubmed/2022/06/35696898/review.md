## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, and figure legends
- **Assessment boundary** Scientific content, methodological soundness, and interpretation of results as presented in the manuscript
- **Shared manuscript claim summary** The authors combine coarse-grained molecular simulations with SAXS data using the EROS method to characterize the conformational ensemble of the full-length SARS-CoV-2 nucleocapsid (N) protein dimer. They report large conformational fluctuations (Rg 4-8 nm), absence of direct NTD-CTD contacts, frequent nonspecific contacts between a hydrophobic α-helix in IDR2 and both RNA-binding domains, and IDR conformations that are locally compact but more extended than Gaussian chains.
- **Visible evidence base** Figures 1-5, Table 1, Supplementary Figures S1-S2 (mentioned in text), SAXS data from Zeng et al. (2020) as referenced
- **Missing materials affecting confidence** Raw SAXS data not provided; simulation trajectory details not provided; force field parameters not fully specified; convergence criteria for REMC simulations not described; error estimates for ensemble refinement not provided; Supplementary Figures S1-S2 not accessible in the provided material

## Reviewer
- **Overall assessment** This manuscript presents a useful application of established coarse-grained simulation methodology combined with SAXS-based ensemble refinement to characterize the conformational landscape of the SARS-CoV-2 N protein dimer. The work addresses a relevant gap in understanding the structural behavior of this important viral protein, which contains large intrinsically disordered regions that resist traditional structural characterization. The combination of computational and experimental approaches is appropriate, and the results provide a plausible picture of the N protein dimer's conformational ensemble. However, several technical aspects require clarification and additional validation before the conclusions can be fully established. The manuscript would benefit from more detailed methodological descriptions, particularly regarding simulation convergence, ensemble refinement parameters, and validation of the coarse-grained model's applicability to this system.

- **Who would be interested in the results, and why** Researchers studying SARS-CoV-2 biology, particularly those interested in nucleocapsid protein structure and function, viral assembly mechanisms, and the role of the N protein in RNA packaging. Additionally, the methodological community working on intrinsically disordered proteins and those developing or applying coarse-grained simulation approaches combined with SAXS data would find this work relevant. The results may also be of interest to structural biologists studying multi-domain proteins with large disordered regions, as the approach demonstrates a viable strategy for characterizing such systems.

- **Major strengths** The study addresses a biologically relevant and technically challenging problem, namely the structural characterization of a large multi-domain protein with extensive intrinsically disordered regions. The combination of coarse-grained simulations with experimental SAXS data through the EROS method is a sound and appropriate approach. The authors provide a clear domain architecture description and use experimentally determined structures for the folded domains. The comparison between monomeric and dimeric forms provides a useful validation of the dimeric state. The analysis of contact maps and IDR conformational properties offers detailed insights into the protein's behavior.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the refined ensemble is "very close to the original ensemble" and achieves "perfect agreement" with SAXS data (χ² = 1)
- **Evidence pointer** Materials and methods, Ensemble refinement of SAXS section; Figure 2C; Figure S1
- **Concern** The selection of the θ parameter in the EROS method is described as choosing "a point in the elbow region" of the L-shaped curve, but the specific criterion for this selection is not provided. The claim of "perfect agreement" with χ² = 1 requires more context, as χ² values near 1 typically indicate that the model fits within experimental noise, but the statistical significance of the improvement from χ² = 1.9 to χ² = 1 is not discussed. Additionally, the uncertainty in the refined ensemble weights and how this propagates to the reported structural properties (Rg distributions, contact frequencies) is not addressed.
- **Why it matters** The central conclusion of the manuscript depends on the reliability of the ensemble refinement. Without a clear description of the θ selection criterion and uncertainty quantification, readers cannot assess whether the refined ensemble is uniquely determined or whether the reported structural features are robust to the refinement parameters.
- **Resolution test** Provide the specific criterion for θ selection, report the χ² values across a range of θ values, and include an analysis of how the refined ensemble properties (Rg distribution, contact maps) vary with θ. Additionally, provide bootstrap or jackknife estimates of uncertainties in the refined weights and derived quantities.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "extensive replica exchange Monte Carlo simulations" were performed and that the resulting ensemble of 20,000 conformations was used for analysis
- **Evidence pointer** Materials and methods, Coarse-grained simulations section; Results section
- **Concern** The manuscript does not provide information on simulation convergence. For REMC simulations, it is essential to demonstrate that replica exchange rates are adequate, that the simulations have reached equilibrium, and that the sampled ensemble is representative. The number of MC cycles (1.1 × 10⁸) is stated, but no convergence metrics are provided. Additionally, the coarse-grained model parameters and their transferability to this specific protein system are not discussed in sufficient detail.
- **Why it matters** Without demonstrated convergence, the reported conformational ensemble and derived properties (Rg distributions, contact maps, IDR end-to-end distances) may not be representative of the true equilibrium ensemble. This would undermine all subsequent analysis and conclusions.
- **Resolution test** Provide replica exchange acceptance rates, show convergence of ensemble-averaged properties (e.g., Rg, radius of gyration) as a function of simulation time, and demonstrate that the results are robust to initial conditions. Include a discussion of the coarse-grained model's validation for multi-domain IDPs and its known limitations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors suggest that "the NTD and CTD do not directly cooperate in RNA binding" based on the absence of direct NTD-CTD contacts in the conformational ensemble
- **Evidence pointer** Results, contact maps section; Figure 4; Discussion section
- **Concern** The absence of direct contacts in the simulated ensemble does not necessarily imply that NTD and CTD cannot cooperate in RNA binding. RNA binding could induce conformational changes that bring the domains into proximity, or cooperation could occur through indirect mechanisms (e.g., both domains binding to the same RNA molecule without direct protein-protein contact). The authors acknowledge that conformations could be modified by RNA binding, but this caveat appears only in the discussion and the claim in the results section is stated too strongly.
- **Why it matters** The functional implications of the structural findings are an important aspect of the manuscript's significance. Overstating the conclusion about NTD-CTD cooperation could mislead readers about the functional relevance of the observed conformational ensemble.
- **Resolution test** Soften the claim in the results section to reflect that the absence of direct contacts is observed in the RNA-free state, and expand the discussion of how RNA binding might alter the conformational ensemble and inter-domain interactions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors report that "each of the three IDRs exhibits a root-mean-square end-to-end distance larger than the Gaussian chains of the corresponding length" and conclude that the IDRs are "more extended than Gaussian chains"
- **Evidence pointer** Results, IDR end-to-end distances section; Table 1; Figure 5
- **Concern** The comparison to Gaussian chains assumes a specific bond length (0.38 nm) and a freely-jointed chain model. However, real polypeptide chains have excluded volume effects, steric constraints, and sequence-specific interactions that can lead to deviations from ideal chain behavior. The choice of Gaussian chain as a reference is reasonable but should be justified, and the interpretation of the ratio (1.83-2.17) as indicating "more extended" conformations should be discussed in the context of other reference models (e.g., self-avoiding walk chains, worm-like chains).
- **Why it matters** The conclusion about IDR conformational properties is a key finding of the manuscript. If the reference model is inappropriate or the comparison is not properly contextualized, the interpretation could be misleading.
- **Resolution test** Provide additional analysis comparing the observed end-to-end distances to multiple reference models, and discuss the physical interpretation of the observed ratios in terms of chain stiffness, excluded volume, and intramolecular interactions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction, first paragraph
- **Evidence pointer** Introduction, paragraph 1
- **Issue** The introduction provides a good overview of the challenges in studying IDPs, but the transition from general IDP challenges to the specific case of the SARS-CoV-2 N protein could be smoother. The relevance of studying the N protein conformational ensemble for understanding viral assembly could be stated more explicitly.
- **Required correction** Add one or two sentences explicitly connecting the N protein's conformational properties to its role in viral assembly and why understanding the conformational ensemble is important for this process.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Materials and methods, Coarse-grained simulations section
- **Evidence pointer** Materials and methods, Coarse-grained simulations section
- **Issue** The description of the coarse-grained model is brief and refers to the original publication by Kim and Hummer. While this is acceptable, a brief summary of the key features of the model (e.g., how many beads per residue, what types of interactions are included) would help readers who are not familiar with the specific model.
- **Required correction** Add a brief summary of the coarse-grained model's key features, including the representation of amino acids, the types of interactions included, and any specific parameters relevant to this system.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Results, SAXS analysis section
- **Evidence pointer** Results, SAXS analysis section; Figure 2
- **Issue** The description of the SAXS analysis and the EROS refinement is technically accurate but may be difficult to follow for readers not familiar with ensemble refinement methods. The concept of "minimally modifying statistical weights" could be explained more intuitively.
- **Required correction** Add a brief intuitive explanation of the EROS approach, perhaps with a simple analogy or a more explicit description of what "minimally modifying weights" means in practice.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, contact maps section
- **Evidence pointer** Results, contact maps section; Figure 4
- **Concern** The contact map analysis uses a distance criterion of 1.5 × σ_ij, but the choice of this threshold is not justified. Different thresholds could lead to different conclusions about contact frequencies.
- **Required correction** Provide a brief justification for the chosen distance threshold, or show that the conclusions are robust to reasonable variations in the threshold.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The discussion of the biological implications is relatively brief. The authors mention the importance for understanding nucleocapsid assembly but do not elaborate on how their findings might inform future studies or potential therapeutic strategies.
- **Required correction** Expand the discussion of biological implications, including how the conformational ensemble might relate to N protein function in viral replication and assembly, and what questions remain to be addressed.

## Risk / unsupported claims
- The claim that the NTD and CTD "do not directly cooperate in RNA binding" is not fully supported, as the simulations were performed in the absence of RNA and RNA binding could induce conformational changes.
- The statement that the refined ensemble is "very close to the original ensemble" is not quantitatively supported, as the degree of similarity is not defined or measured.
- The conclusion that IDRs are "more extended than Gaussian chains" is based on a single reference model and may not be robust to different reference choices.
- The claim that the structure shown in Figure 2E "cannot be stable in solution" is speculative, as stability cannot be assessed from a single snapshot.
- The assertion that "the N protein has never been reported to be in the monomeric form" is a strong claim that would require a comprehensive literature search to verify.
- The biological significance of the observed conformational ensemble for nucleocapsid assembly is discussed qualitatively but not quantitatively supported by the data presented.