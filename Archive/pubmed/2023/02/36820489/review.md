## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, methods, results, discussion, and conclusion. No supplementary material was provided.
- **Assessment boundary** The scientific claims, methodological validity, and internal consistency of the presented work, as described in the manuscript. No external data or replication was performed.
- **Shared manuscript claim summary** The authors present a computational method to estimate solvation free energy from water density maps of the first hydration shell, derived from all-atom MD simulations. They apply it to two intrinsically disordered ligands binding to the nSH3 domain of CrkII, finding that the viral ligand PRMNS1 incurs a lower desolvation penalty than PRMcAbl, consistent with its higher affinity. They further report a nonlocal, allosteric effect where distal "entropy hotspot" residues contribute to the desolvation penalty, and that this effect disappears when protein motion is suppressed.
- **Visible evidence base** Main text figures (Figures 1-10), Tables 1-2, and referenced supplementary tables (S1-S5) that are not provided. Methods section describes simulation parameters and analysis procedures.
- **Missing materials affecting confidence** Supplementary tables (S1-S5) referenced in the text are not available. These contain residue-level data and additional numerical results that are central to several claims, particularly the residue-level analysis and the comparison between restrained and unrestrained simulations. Without these, the quantitative support for several conclusions cannot be fully verified.

## Reviewer
- **Overall assessment** The manuscript presents a novel and potentially valuable approach to estimating solvation free energy from water density maps, with a focus on capturing the dynamic nature of protein surfaces. The application to a well-characterized SH3-ligand system is appropriate, and the finding of a nonlocal, allosteric contribution to desolvation is interesting. However, the manuscript has several technical and presentational issues that need to be addressed. The method's validation is incomplete, the comparison with GIST is not fully rigorous, and the central claim of an allosteric effect relies on a single control simulation with a strong restraint that may not be representative of typical GIST usage. The writing is generally clear but some sections are dense and could be improved for a broader audience. The work is original and of potential interest to the biophysics and computational chemistry communities, but the case is not fully established from the provided evidence.
- **Who would be interested in the results, and why** Computational biophysicists and chemists studying protein-ligand interactions, solvation thermodynamics, and the role of water in molecular recognition. Researchers developing or using solvation free energy methods (e.g., GIST, 3D-RISM) would be interested in the methodological comparison and the proposed density-based approach. The findings on allosteric hydration effects may also be of interest to those studying allostery and protein dynamics, as well as drug designers seeking to understand desolvation penalties in binding.
- **Major strengths** The manuscript addresses a challenging and important problem, namely the role of dynamic surface hydration in ligand binding. The proposed method is conceptually simple and computationally efficient, and it explicitly accounts for protein conformational motion, which is a limitation of many existing approaches. The use of a well-characterized experimental system with known binding affinities provides a relevant test case. The finding that distal residues contribute to the desolvation penalty is novel and could have implications for understanding allostery. The comparison with GIST, while not perfect, is a useful addition.
- **Major Concerns** The following concerns are detailed below.
- **Minor Comments** The following comments are detailed below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (method validation), R1-M2 (allosteric claim support), R1-M3 (GIST comparison rigor), R1-M4 (missing supplementary data).
- **Assessment against Nature-style criteria** **Originality**: High. The density-based approach to solvation free energy, particularly its application to capture nonlocal effects, appears novel. **Scientific importance**: Moderate to high. The work addresses a fundamental aspect of molecular recognition and could influence future method development and drug design. **Interdisciplinary readership**: Moderate. The topic is of interest to biophysicists, computational chemists, and structural biologists, but the technical nature may limit broader appeal. **Technical soundness**: The core idea is sound, but the validation is incomplete and the comparison with GIST is not fully rigorous, as detailed in the concerns. **Readability for nonspecialists**: The abstract and introduction are accessible, but the methods and results sections are dense and may be challenging for readers without a strong background in MD simulations and solvation thermodynamics. The manuscript would benefit from clearer explanations of the method's assumptions and limitations.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a promising approach and interesting findings, but the current evidence does not fully establish the case, particularly regarding the allosteric claim and the method's general validity.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The method's validity is asserted through comparison with experimental binding affinities and MM/GBSA, but no direct validation against established solvation free energy calculations (e.g., FEP/TI) or experimental solvation data is provided.
- **Evidence pointer** Methods section "Density-Based Solvation Free Energy Calculation"; Results section "Contribution of Surface Hydration to the Binding Free Energy"; Table 1.
- **Concern** The manuscript claims that the density-based solvation free energy (ΔGsolv∞) is a meaningful measure of desolvation penalty, but the validation is indirect. The comparison with MM/GBSA shows a difference in ΔGbind′ that is consistent with experimental affinities, but this is a composite quantity that includes other terms. The method's absolute accuracy is not established. The authors should validate their approach against a more rigorous method, such as free energy perturbation (FEP) or thermodynamic integration (TI), for at least one of the systems, or against experimental solvation free energies of model compounds. Without such validation, it is unclear whether the reported ΔGsolv∞ values are quantitatively reliable or merely qualitatively indicative.
- **Why it matters** The central claim of the paper, that the method can quantify desolvation penalties and reveal nonlocal effects, depends on the accuracy of the calculated free energies. If the method is not validated, the quantitative conclusions, including the 6.9 kcal/mol difference between the two ligands, are not trustworthy.
- **Resolution test** Provide a comparison of ΔGsolv∞ with FEP/TI calculations for the binding of PRMcAbl and PRMNS1 to nSH3, or with experimental solvation free energies for relevant model compounds. Show that the method reproduces known results within a reasonable error margin.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Support for central claim
- **Claim pointer** The claim that "ligand binding alters hydration on remote sites" and that "entropy hotspot" residues contribute significantly to the desolvation penalty is based on residue-level analysis, but the evidence is not fully presented.
- **Evidence pointer** Results section "Allosteric Role of the Side-Chain Motion for Desolvation Energy"; Figure 7; Tables S2 and S3 (not provided).
- **Concern** The allosteric effect is a key finding, but the supporting data are in supplementary tables that are not provided. The text describes residue-level contributions, but without the actual numbers, it is impossible to assess the magnitude and significance of the effect. Furthermore, the identification of "entropy hotspots" relies on previous work (reference 77), but the connection between increased side-chain entropy and increased desolvation penalty is not mechanistically explained in sufficient detail. The authors state that "their greater side-chain mobility leads to disruption of the surrounding hydration shell," but this is a hypothesis that is not directly tested. The control simulation with restrained protein atoms shows a loss of the allosteric effect, but this is a single, extreme condition (50 kcal/mol·Å² restraint) that may not be representative of the range of protein dynamics.
- **Why it matters** The nonlocal, allosteric role of hydration is the most novel and significant claim of the paper. If this claim is not robustly supported, the paper's impact is substantially reduced.
- **Resolution test** Provide the residue-level data (Tables S2 and S3) in the main text or as a clearly accessible supplement. Show a quantitative analysis of the correlation between side-chain entropy changes and desolvation penalty changes. Discuss the mechanism in more detail, and ideally test the effect with a range of restraint strengths to show that the effect is gradual and not an artifact of a single, strong restraint.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The comparison with GIST is used to argue that the density-based method is superior, but the comparison is not fully rigorous.
- **Evidence pointer** Results section "Comparison with Grid Inhomogeneous Solvation Theory"; Figure 10.
- **Concern** The comparison with GIST is based on a single simulation with restrained protein atoms. The authors argue that GIST overestimates the range of solvation free energies because it does not account for protein motion. However, GIST is typically used with restrained or fixed proteins, and the comparison should be made under conditions that are appropriate for each method. The authors also note that GIST calculates interaction energies and entropies directly, while their method is density-based. The positive correlation in Figure 10b is encouraging, but the large difference in the range of values (40 vs 2.5 kcal/mol) is not fully explained. The authors suggest that GIST values are "less realistic," but this is an assertion that is not backed by a quantitative benchmark.
- **Why it matters** The claim that the method is advantageous over GIST is a key part of the paper's contribution. If the comparison is not fair or the interpretation is not justified, the claim is weakened.
- **Resolution test** Perform a more systematic comparison with GIST, using the same simulation trajectories and appropriate parameters for each method. Discuss the differences in the free energy components (energy vs entropy) and provide a benchmark against experimental or FEP/TI data to support the claim that the density-based method is more accurate.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The manuscript relies heavily on supplementary tables (S1-S5) for quantitative support, but these are not provided.
- **Evidence pointer** Results section; Tables S1-S5 referenced in text.
- **Concern** The manuscript is not self-contained. Key numerical results, including residue-level desolvation penalties, entropy changes, and the comparison between restrained and unrestrained simulations, are only in the supplementary material. Without these, the reader cannot verify the claims or reproduce the analysis. This is a significant issue for a methods paper.
- **Why it matters** Reproducibility is a core principle of scientific publishing. The authors must make the data available to support their claims.
- **Resolution test** Provide the supplementary tables as part of the manuscript submission. Ensure that all data referenced in the text are available to the reader.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section "Density-Based Solvation Free Energy Calculation"
- **Evidence pointer** Equation 1 and surrounding text.
- **Issue** The derivation of Equation 1 is not fully explained. The relationship between the water density and the free energy is stated but not derived. The assumption that the free energy is proportional to the logarithm of the density is not justified.
- **Required correction** Provide a brief derivation or a reference to a previous work where this relationship is established. Clarify the assumptions and limitations of this approximation.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure 2
- **Evidence pointer** Figure 2 and related text.
- **Issue** The figure shows density peaks for the first and second hydration shells, but the choice of the 4.5 Å cutoff is not clearly justified. The text states that this is "slightly larger than the distance where the water density falls below the bulk value," but the figure is not annotated to show this.
- **Required correction** Add a vertical line or annotation to Figure 2 to indicate the chosen cutoff and the bulk density value. This will help the reader understand the selection criteria.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Methods section "Simulation Systems"
- **Evidence pointer** Description of restrained simulations.
- **Issue** The restraint strength of 50 kcal/(mol·Å²) is described as "strong," but no justification is given for this specific value. It is not clear whether this is a standard choice or if a range of values was tested.
- **Required correction** Provide a rationale for the choice of restraint strength, or state that a single value was used for simplicity. If a range was tested, report the results.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Results section "Changes in Surface Hydration upon Ligand Binding"
- **Evidence pointer** Figure 6 and related text.
- **Issue** The description of the cell counting and the interpretation of the differences between the two ligands is somewhat dense. The connection between the number of cells and the physical picture of hydration is not immediately clear.
- **Required correction** Simplify the explanation and consider adding a schematic or a more intuitive description of what the cell counts represent in terms of hydration structure.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Conclusion
- **Evidence pointer** Final paragraph.
- **Issue** The conclusion states that the method is "broadly applicable," but the limitations of the approach are not discussed. For example, the method relies on the choice of a density cutoff and a distance cutoff, and it is not clear how sensitive the results are to these choices.
- **Required correction** Add a paragraph discussing the limitations of the method, including the sensitivity to the chosen cutoffs and the assumptions underlying the density-based free energy calculation.

## Risk / unsupported claims
- The claim that the method is "the first approach to account for the dynamic interplay between protein motion and surface hydration in ligand binding" is not supported by a comprehensive literature review. While the approach may be novel, the authors should temper this claim or provide a more thorough comparison with existing methods.
- The claim that GIST solvation energies are "less realistic" is not supported by quantitative evidence. This is an assertion that requires benchmarking against experimental or high-level computational data.
- The quantitative values for residue-level desolvation penalties and entropy changes (Tables S2-S5) are not verifiable from the provided material. These are central to the allosteric claim and must be made available.
- The statement that the "nonlocal effect disappears when the conformational motion of the protein is suppressed" is based on a single simulation with a strong restraint. This is a limited test and the claim should be qualified accordingly.