## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and figure/table captions. Supplementary information referenced but not provided.
- **Assessment boundary** Scientific soundness, methodological rigor, validity of thermodynamic decomposition, clarity of claims, and alignment with stated conclusions. No assessment of editorial fit or scope policy.
- **Shared manuscript claim summary** The authors use atomistic molecular dynamics simulations of the FUS-LCD domain to decompose the free energy change of condensate formation into protein and water contributions. They report that solvation entropy and protein interaction enthalpy are the dominant favorable terms, that released water molecules gain entropy while retained water molecules lose entropy, and that the net solvation free energy is favorable. They conclude that protein and water contributions are comparable in magnitude.
- **Visible evidence base** Main text figures 1–8, tables 1–2, equations 1–21, methods section, and references to supplementary tables and figures. Supplementary material not provided.
- **Missing materials affecting confidence** Supplementary Tables 1–10, Supplementary Figures 1–5, simulation parameter files, force field validation details, convergence analyses, and the full PDB2ENTROPY output. These are referenced for key quantitative results and robustness checks.

## Reviewer
- **Overall assessment** This manuscript presents a technically ambitious decomposition of thermodynamic driving forces for FUS-LCD condensate formation using atomistic MD simulations. The central idea, that water release and retention constitute a tug-of-war with measurable thermodynamic consequences, is conceptually appealing and timely. The authors correctly identify that both protein and water terms matter, and they provide a plausible decomposition framework. However, the manuscript currently does not fully establish the quantitative reliability of its central claims. The entropy calculations rely on methods with known sensitivity to force field, sampling, and system size, and the validation presented is insufficient to rule out large systematic errors. The neglect of interface energy and the treatment of the dilute phase as pure water are simplifications that need more careful justification. The claim that the two dominant terms are comparable in magnitude is interesting but rests on error bars that may be underestimated. The paper is well written and the figures are clear, but the gap between the strength of the conclusions and the robustness of the underlying calculations needs to be addressed.

- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation, biomolecular condensates, intrinsically disordered proteins, and solvation thermodynamics. The methodological approach, decomposing free energy into protein and water contributions, will be of interest to computational biophysicists working on IDPs and phase separation. Experimental groups studying FUS and related proteins may find the molecular-level picture useful for interpreting their own data. The work also speaks to the broader question of water's role in biomolecular association, which is relevant to the protein folding and aggregation communities.

- **Major Strengths**
  - The study addresses a genuinely important and unresolved question: what are the molecular thermodynamic drivers of condensate formation?
  - The decomposition into protein and water contributions is conceptually clear and provides a useful framework for future work.
  - The use of atomistic simulations with explicit solvent is appropriate and represents a step beyond coarse-grained approaches.
  - The authors are careful to distinguish between canceling and noncanceling terms, which is a subtle and important point.
  - The manuscript is clearly written and the figures effectively communicate the main results.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the total solvation free energy change is favorable and that solvation entropy is a major driving force for condensate formation.
- **Evidence pointer** Figure 7, Equations 12–14, Methods section "Entropy of water"
- **Concern** The 2PT method is used to compute water entropy, but the manuscript does not provide sufficient validation that this method is accurate for highly confined water in dense protein environments. The 2PT method was parameterized and validated primarily for bulk liquids. Its accuracy for water in strongly heterogeneous and confined environments, such as the interior of a protein condensate at 350 mg/mL, is not established. The authors validate against FEP only for bulk water, which does not test the method in the regime where it matters most. The crossover in entropy versus concentration at ~150 mg/mL is presented as a finding, but it could be an artifact of the 2PT decomposition rather than a physical feature.
- **Why it matters** The central quantitative claim of the paper, that solvation entropy favors condensate formation, depends entirely on the accuracy of the 2PT entropy estimates. If the method systematically overestimates or underestimates entropy in confined environments, the sign or magnitude of the driving force could change. The current validation is insufficient to rule this out.
- **Resolution test** Provide validation of 2PT against a more rigorous method (e.g., thermodynamic integration or free energy perturbation) for water in at least one confined environment representative of the condensate interior. Alternatively, show that the qualitative conclusions are robust to the choice of entropy calculation method.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the protein conformational entropy change upon condensate formation is small and does not affect the sign of the total free energy change.
- **Evidence pointer** Figure 8, Methods section "Protein conformational entropy", Supplementary Figure 2
- **Concern** The protein conformational entropy is estimated using the PDB2ENTROPY nearest-neighbor method, which the authors themselves describe as a rough estimate. The method is based on torsion angle distributions and is known to be sensitive to the choice of reference state, the definition of torsion angles, and the quality of sampling. The manuscript states that changing -TΔS_P by an order of magnitude does not change the sign of the total free energy, which is a useful robustness check, but the magnitude of the error in the entropy estimate is not quantified. The claim that the conformational entropy change is small is therefore not well supported.
- **Why it matters** The total free energy is the sum of several terms, and if the protein conformational entropy term is underestimated, the relative importance of the solvation and interaction energy terms could be misrepresented. The conclusion that protein and water contributions are comparable in magnitude depends on the accuracy of this term.
- **Resolution test** Provide a more rigorous estimate of the conformational entropy change, or at minimum a quantitative error bound. This could be done using a different method (e.g., quasi-harmonic analysis, or a different reference state) and showing that the conclusions are unchanged.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the free energy change calculated from separate simulations of homogeneous solutions at different concentrations captures the thermodynamics of condensate formation.
- **Evidence pointer** Introduction, Figure 2, Equations 2–3
- **Concern** The approach relies on the assumption that the free energy of the condensate can be computed from a homogeneous simulation at the condensate concentration, and that the dilute phase can be approximated as pure water. This neglects the free energy cost of creating an interface between the two phases. The authors estimate this cost to be small, but the estimate is based on a range of surface tensions that spans two orders of magnitude, and the calculation is not shown. Furthermore, the use of a single homogeneous box at 350 mg/mL to represent the condensate ignores any spatial heterogeneity or finite-size effects that may be present in a real condensate.
- **Why it matters** If the interface energy is not negligible, or if the homogeneous box is not representative of the condensate, the calculated free energy change could be systematically biased. The comparison to experimental phase behavior is qualitative, so this bias would not be detected.
- **Resolution test** Provide the interface energy calculation in detail, or perform a simulation with an explicit interface between condensate and dilute phases to directly measure the interfacial contribution. Alternatively, show that the results are converged with respect to system size.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that the results provide "detailed molecular insights on the intricate thermodynamic interplay between protein- and solvation-related forces underlying the formation of biomolecular condensates."
- **Evidence pointer** Abstract, Discussion
- **Concern** The study is performed on a single protein domain (FUS-LCD) at a single temperature and salt concentration. The authors do not test whether the conclusions generalize to other IDPs or to different solution conditions. The claim of general insight is therefore broader than the evidence supports. The authors do acknowledge this limitation in the discussion, but the abstract and introduction frame the results in more general terms.
- **Why it matters** The phase separation field is characterized by diverse sequence compositions and solution conditions. A claim of general insight requires at least some demonstration of transferability, or a clear statement of the conditions under which the conclusions are expected to hold.
- **Resolution test** Add a brief discussion of the expected dependence on sequence composition and solution conditions, or perform additional simulations with a second IDP or at a different salt concentration to test robustness.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1
- **Evidence pointer** Figure 1 caption
- **Issue** The schematic in Figure 1 is helpful but the distinction between "released" and "retained" water is not defined precisely. The caption mentions the tug-of-war but does not explain how these populations are identified in the simulations.
- **Required correction** Add a sentence to the caption or main text defining the operational criteria for released versus retained water.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, simulation setup
- **Evidence pointer** Table 2
- **Issue** The number of ions listed in Table 2 appears inconsistent with the stated salt concentration of 150 mM. For example, the 25 mg/mL system has 163 Na+ and 90 Cl- ions, which does not correspond to 150 mM NaCl plus charge neutralization. The discrepancy is not explained.
- **Required correction** Clarify the ion counting procedure and ensure the table is consistent with the stated salt concentration.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Equation 14
- **Evidence pointer** Equation 14 and surrounding text
- **Issue** The derivation of Equation 14 is not fully explained. The text states that the water-water term cancels, but the logic is compressed and may be difficult for readers to follow.
- **Required correction** Expand the derivation or add a supplementary note explaining why the water-water term cancels and how Equation 14 follows from Equations 8–13.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 8
- **Evidence pointer** Figure 8 caption
- **Issue** The figure shows the total free energy change as a function of concentration, but the individual contributions are not labeled in the figure itself. The caption lists them but the reader must refer back and forth.
- **Required correction** Add labels directly to the curves in the figure or use a legend.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, protein conformational entropy
- **Evidence pointer** Methods section "Protein conformational entropy"
- **Issue** The description of the PDB2ENTROPY calculation is brief. The specific parameters used (e.g., the cutoff distance, the definition of torsion angles, the treatment of side chains) are not fully specified.
- **Required correction** Provide the full parameter set used for the PDB2ENTROPY calculation, either in the main text or in the supplementary information.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion of dilute phase
- **Evidence pointer** Results section "Thermodynamic signatures"
- **Issue** The dilute phase is treated as pure water, but the authors note that the experimental dilute phase has a protein concentration of ~1 mg/mL. The justification for this approximation is not fully developed.
- **Required correction** Add a brief justification for why the dilute phase can be approximated as pure water, or discuss the potential error introduced by this approximation.

## Risk / unsupported claims
- The claim that solvation entropy is a major driving force for condensate formation is not fully supported because the 2PT method is not validated for confined water environments.
- The claim that protein conformational entropy change is small is not quantitatively supported, as the method used is acknowledged to be approximate and no error bounds are provided.
- The claim that the free energy decomposition captures the thermodynamics of condensate formation neglects interface energy, and the estimate of this contribution is not shown in detail.
- The claim of general insight into biomolecular condensate formation is broader than the evidence from a single protein domain at a single condition.
- The quantitative values of the entropy and energy contributions (Supplementary Tables 1–10) cannot be assessed because the supplementary material was not provided.