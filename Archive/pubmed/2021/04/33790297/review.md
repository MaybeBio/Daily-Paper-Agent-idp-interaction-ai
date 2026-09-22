## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and figure legends.
- **Assessment boundary** Scientific validity, technical soundness, and support of claims based solely on the provided manuscript content. No external literature or unpublished data were consulted.
- **Shared manuscript claim summary** The authors present a rationally designed artificial FG-Nup, NupX, which reconstitutes the selective transport barrier of the nuclear pore complex. They claim that NupX brushes selectively bind the transport receptor Kap95 over inert proteins like BSA, that NupX-lined solid-state nanopores allow Kap95 transport while blocking BSA, and that coarse-grained molecular dynamics simulations support these findings. They conclude that simple design rules, without specific spacer sequences or spatial segregation of FG-motif types, are sufficient to create selective NPC-like barriers.
- **Visible evidence base** Experimental data from quartz crystal microbalance with dissipation monitoring (QCM-D), surface plasmon resonance (SPR), solid-state nanopore ionic current measurements, and coarse-grained molecular dynamics simulations. Figures 1–5 and supplementary figures/tables are referenced.
- **Missing materials affecting confidence** Raw data files, detailed statistical analyses, full uncropped gel images (if any), and complete simulation parameter files are not provided. The manuscript does not include a detailed error analysis for the nanopore translocation rates or a direct comparison of NupX behavior to native FG-Nups under identical experimental conditions.

## Reviewer
- **Overall assessment** This manuscript presents a compelling and innovative bottom-up approach to studying nuclear pore complex selectivity. The design of a minimal artificial FG-Nup that recapitulates key selective properties is a significant conceptual advance. The combination of experimental and computational methods is strong, and the results largely support the main conclusions. However, several technical concerns, particularly regarding the quantitative interpretation of QCM-D data, the robustness of the nanopore selectivity measurements, and the directness of the simulation evidence, need to be addressed to fully establish the case.
- **Who would be interested in the results, and why** Researchers in nucleocytoplasmic transport, biophysics of intrinsically disordered proteins, synthetic biology, and nanobiotechnology. The work provides a simplified model system to test theories of NPC selectivity, offers a platform for designing artificial selective barriers, and demonstrates the power of rational design in recreating complex biological functions.
- **Major strengths**
  1. The rational design of a minimal artificial FG-Nup is a novel and elegant approach to dissect the essential features of NPC selectivity.
  2. The combination of QCM-D, SPR, nanopore electrophysiology, and coarse-grained simulations provides a multi-faceted view of the system.
  3. The clear demonstration that a simple, uniformly spaced FG-repeat design can achieve selectivity challenges existing models and simplifies the conceptual framework.
  4. The work has broad implications for understanding IDP function and for engineering biomimetic transport systems.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The claim that QCM-D measurements show selective binding of Kap95 to NupX brushes over BSA.
  - **Evidence pointer** Figure 2a, d, g; Methods section "QCM-D sample preparation and data acquisition"
  - **Concern** The QCM-D frequency shifts are interpreted as direct measures of bound mass, but the dissipation data (Figure 2a–c) indicate significant viscoelastic effects. The Sauerbrey equation, which assumes a rigid, thin film, is not valid for soft, hydrated protein layers. The authors acknowledge this limitation but do not provide an alternative analysis (e.g., using the Voigt model) to extract accurate mass and thickness values. Without this, the quantitative comparison of Kap95 binding to NupX versus Nsp1, and the lack of BSA binding, is not rigorously established.
  - **Why it matters** The central claim of selective binding rests on the QCM-D data. If the frequency shifts are not accurately converted to mass, the conclusion that Kap95 binds specifically to NupX brushes could be an artifact of viscoelastic changes rather than true mass uptake.
  - **Resolution test** The authors should re-analyze the QCM-D data using a viscoelastic model (e.g., Voigt) to obtain corrected mass uptake values. They should also provide a direct comparison of the dissipation-to-frequency ratio for Kap95 and BSA binding to demonstrate that the observed signals are due to mass loading and not just changes in layer softness.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The claim that NupX-lined nanopores selectively allow Kap95 transport while blocking BSA.
  - **Evidence pointer** Figure 3c–g; Methods section "Preparation of NupX-coated nanopores and current data acquisition"
  - **Concern** The nanopore experiments show a dramatic reduction in BSA event rate after NupX coating, but the number of BSA events in the coated pore is very low (N=28 in Figure 3f). The statistical significance of this difference is not rigorously assessed. Furthermore, the event detection algorithm and the criteria for distinguishing true translocation events from noise are not described in sufficient detail. The possibility that BSA molecules are transiently trapped in the NupX mesh and released back to the cis side (rather than fully translocating) is not discussed, which could lead to an underestimation of BSA permeation.
  - **Why it matters** The selectivity of the nanopore is the key functional demonstration of the paper. If the low BSA event rate is due to technical artifacts or incomplete analysis, the conclusion that NupX forms a selective barrier is weakened.
  - **Resolution test** The authors should provide a detailed description of the event detection algorithm and perform a statistical analysis (e.g., t-test or Mann-Whitney U test) comparing event rates across multiple pores. They should also analyze the current blockade amplitudes and dwell times for BSA in the coated pore to determine if these events represent true translocations or failed attempts.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** The claim that coarse-grained MD simulations demonstrate the formation of a selective meshwork with densities comparable to native NPCs.
  - **Evidence pointer** Figures 2h–i, 4b–h, 5; Methods section "Coarse-grained model for unfolded proteins"
  - **Concern** The coarse-grained model uses a simplified representation of amino acids and interactions. The parameters for hydrophobic interactions and electrostatics are derived from previous work, but their applicability to the NupX sequence is not fully validated. The simulation of Kap95 as a rigid particle with ten hydrophobic binding sites is a significant simplification that may not capture the true flexibility and surface properties of the protein. The PMF calculations for nanopore transport (Figure 5e) are based on a density-conductivity relationship that is not directly derived from the simulations, introducing an additional layer of approximation.
  - **Why it matters** The simulations are used to provide a mechanistic explanation for the experimental observations. If the model is not accurately representing the physical system, the proposed mechanism of selectivity (e.g., the role of FG-repeat density and distribution) may be incorrect.
  - **Resolution test** The authors should validate the coarse-grained model by comparing simulated properties (e.g., radius of gyration, end-to-end distance) of NupX to experimental measurements (e.g., SAXS, FRET) if available. They should also test the sensitivity of the PMF results to the choice of interaction parameters and the Kap95 model.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Figure 1h
  - **Evidence pointer** Figure 1h
  - **Issue** The distribution of Stokes radii for NupX and 25 design variations is shown, but the statistical significance of the difference between NupX and the variations is not stated.
  - **Required correction** Add a statistical test (e.g., ANOVA) to compare the mean Stokes radii and report the p-value.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods section "QCM-D sample preparation and data acquisition"
  - **Evidence pointer** Methods section
  - **Issue** The manuscript states that "data processing and plotting were performed using a custom-written Matlab script" but does not provide the script or a detailed description of the data processing steps.
  - **Required correction** Provide the custom script as supplementary material or describe the data processing steps in sufficient detail to be reproducible.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Discussion section
  - **Evidence pointer** Discussion section
  - **Issue** The discussion mentions that "no specific spacer sequence nor a spatial segregation of different FG-motif types are needed to create selective NPCs," but does not discuss potential limitations of this conclusion, such as the possibility that other NPC components or post-translational modifications are required for full functionality in vivo.
  - **Required correction** Add a sentence acknowledging that the simplified in vitro system may not capture all aspects of native NPC function and that future work should test the design in more complex environments.

## Risk / unsupported claims
- The claim that NupX "faithfully mimics the selective behaviour of the NPC" is not fully supported, as the experiments only demonstrate selectivity for Kap95 over BSA in a simplified system, not the full range of transport properties of the native NPC.
- The claim that "no specific spacer sequence nor a spatial segregation of different FG-motif types are needed" is supported by the NupX design, but the manuscript does not directly compare NupX to a variant with a specific spacer sequence or spatial segregation, so the claim is inferred rather than directly tested.
- The quantitative values of grafting density and brush height derived from SPR and QCM-D are model-dependent and should be treated with caution.
- The simulation results for nanopore conductance rely on a density-conductivity relationship that is not experimentally validated for NupX, making the quantitative predictions uncertain.