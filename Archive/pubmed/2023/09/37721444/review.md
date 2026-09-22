## Review setup
- **Input scope** Full manuscript text including abstract, main text, and figure references, but excluding actual figures and supplementary material.
- **Assessment boundary** Scientific content, methodology, claims, and internal consistency of the provided text. No assessment of figures, tables, or supplementary data that were not supplied.
- **Shared manuscript claim summary** The authors use coarse-grained molecular dynamics simulations to quantify the contribution of cation−π interactions to the stability of biomolecular condensates formed by liquid–liquid phase separation. They report that cation−π interactions provide up to 80% stabilization, that this stabilization increases with salt concentration and aromatic residue content, and that it trades off against electrostatic interactions. They also present a bioinformatic analysis of IDR sequences suggesting conservation of positively charged residues in phase-separating proteins.
- **Visible evidence base** Main text descriptions of simulation models, phase diagrams, energetic analyses, diffusivity measurements, and a bioinformatic analysis of IDR sequences from LLPSDB and human genome databases.
- **Missing materials affecting confidence** All figures, supplementary figures (S1–S4, S7, S10), simulation parameter tables, force field details, error bars, statistical analyses, and the full bioinformatic dataset. The manuscript text references these materials but they were not provided for review.

## Reviewer
- **Overall assessment** The manuscript addresses an important and timely question regarding the interplay between cation−π, electrostatic, and aromatic interactions in biomolecular condensates. The central claim, that cation−π interactions can compensate for loss of electrostatic interactions at high salt concentrations, is mechanistically plausible and potentially significant. However, the evidence as presented in the text alone is insufficient to fully evaluate the robustness of the conclusions. The simulation model relies on several assumptions that are stated but not justified in detail, and the quantitative claims (e.g., 80% stabilization) cannot be verified without access to the figures and error analysis. The bioinformatic analysis is intriguing but its interpretation requires more careful consideration of confounding factors. The work is likely of interest to the condensate and IDP communities, but the current evidence base does not fully establish the case.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, liquid–liquid phase separation, intrinsically disordered proteins, and the molecular grammar of protein–protein interactions. The work is also relevant to those interested in the design of synthetic condensates and in understanding how salt concentration modulates condensate stability. The trade-off concept between interaction types has broad implications for understanding sequence-encoded phase behavior.
- **Major strengths** The study addresses a specific and under-quantified interaction type (cation−π) in the context of condensate formation. The systematic variation of sequence parameters (aromatic content, charge clustering) and salt concentration is a sensible approach. The use of a coarse-grained model that has been previously calibrated against experimental Rg values provides some grounding. The bioinformatic analysis adds a biological dimension that strengthens the relevance of the findings. The concept of a trade-off between interaction types is clearly articulated and potentially useful for the field.
- **Major Concerns** The following concerns are identified.
- **Minor Comments** The following comments are identified.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4.
- **Assessment against Nature-style criteria** Originality: The study offers a focused quantification of cation−π interactions in condensates, which is a relatively underexplored area compared to charge–charge or π–π interactions. The trade-off concept is not entirely new but is applied here in a systematic manner. Scientific importance: Understanding how different interaction types compensate for each other is important for predicting condensate behavior and for design purposes. The salt-dependent trade-off has practical implications. Interdisciplinary readership: The work bridges biophysics, computational chemistry, and cell biology, and should appeal to a broad readership interested in phase separation. Technical soundness: The simulation methodology is reasonable but several assumptions require further justification. The lack of error analysis and statistical details in the provided text weakens the technical assessment. Readability for nonspecialists: The text is generally clear but assumes familiarity with coarse-grained simulation approaches and phase separation concepts. The abstract is accessible, but the main text would benefit from more explicit definitions of key parameters (e.g., κ, ϕ) for a broader audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the conclusions are plausible, but the current evidence base, as presented in the text alone, does not fully establish the quantitative claims. Access to figures, error analysis, and additional methodological details is required for a definitive assessment.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that cation−π interactions provide up to 80% stabilization of condensates, with specific values for ΔTC at different salt concentrations and sequence compositions.
- **Evidence pointer** Figure 2, Figure 3, and associated text. Location not provided for specific data points.
- **Concern** The quantitative claims regarding the magnitude of stabilization (e.g., 80%, 50%, 15–60%) are presented in the text but cannot be verified without the actual figures and the underlying numerical data. No error bars, standard deviations, or statistical significance tests are reported in the text. The ΔTC values appear to be derived from phase diagrams, but the method for determining TC and its uncertainty is not described.
- **Why it matters** The central conclusion of the paper rests on these quantitative comparisons. Without error analysis, it is impossible to determine whether the observed differences in ΔTC between conditions are statistically meaningful or within the noise of the simulation method.
- **Resolution test** Provide the numerical data for all ΔTC values, including error estimates and the number of independent simulations. Describe the method for determining TC and its uncertainty. Show that the reported differences are statistically significant.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that the cation−π interaction strength is independent of salt concentration and that the same strength reproduces experimental Rg values at 20 and 40 mM salt.
- **Evidence pointer** Main text, simulation model section. Location not provided.
- **Concern** The assumption that cation−π interaction strength is salt-independent is critical to the interpretation of the salt-dependent trade-off. However, the text provides no justification for this assumption. Cation−π interactions are known to be modulated by the local electrostatic environment, which changes with ionic strength. The calibration against Rg at only two salt concentrations (20 and 40 mM) is a limited test, and the manuscript does not report the quality of the fit or the sensitivity of the results to this assumption.
- **Why it matters** If cation−π strength actually varies with salt concentration, the observed trade-off could be an artifact of the model rather than a real physical effect. The conclusion that cation−π interactions compensate for lost electrostatics depends on this assumption being valid.
- **Resolution test** Provide a sensitivity analysis showing how the results change if cation−π strength is allowed to vary with salt concentration. Justify the salt-independence assumption with additional calibration data or physical arguments.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The authors claim that the bioinformatic analysis of IDR sequences shows conservation of positively charged residues with increasing aromatic content in LLPS-prone proteins, suggesting a role for cation−π interactions.
- **Evidence pointer** Figure 5 and associated text. Location not provided.
- **Concern** The bioinformatic analysis is presented as supporting evidence for the biological relevance of cation−π interactions. However, the text does not describe the statistical methods used, the control for confounding factors (e.g., overall amino acid composition, sequence length, or evolutionary conservation), or the significance of the observed trends. The comparison between LLPS-prone IDRs and human IDRs may be confounded by differences in dataset composition or annotation.
- **Why it matters** The bioinformatic analysis is used to generalize the simulation findings to real biological sequences. If the analysis is not statistically robust, the claim that cation−π interactions are conserved in LLPS-prone proteins is not supported.
- **Resolution test** Provide details of the statistical tests used, including effect sizes and p-values. Show that the observed trends are not explained by confounding variables. Consider additional controls, such as comparing to shuffled sequences or to IDRs with similar amino acid composition.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that the coarse-grained model includes cation−π interactions modeled with a Lennard-Jones potential and that the strength was calibrated to reproduce experimental Rg values.
- **Evidence pointer** Main text, simulation model section. Location not provided.
- **Concern** The text does not provide sufficient detail on the force field parameters, the functional form of the cation−π interaction, or the calibration procedure. It is unclear how the cation−π interaction is distinguished from generic aromatic interactions, and whether the model allows for orientation dependence, which is known to be important for cation−π interactions. The transferability of the calibrated parameters to different sequences and conditions is not discussed.
- **Why it matters** The conclusions depend on the accuracy of the interaction model. If the cation−π interaction is not represented with sufficient fidelity, the quantitative results may not be reliable. The lack of detail prevents other researchers from reproducing the simulations.
- **Resolution test** Provide a complete description of the force field, including all parameters and the functional form of the cation−π interaction. Describe the calibration procedure in detail, including the data used and the quality of the fit. Discuss the limitations of the model and the potential impact on the conclusions.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Main text, simulation model section
- **Evidence pointer** Location not provided
- **Issue** The definitions of key parameters such as ϕ (aromatic content), FCR (fraction of charged residues), and κ (charge clustering coefficient) are introduced in the text but not defined explicitly in a single location. A reader unfamiliar with the prior work (reference 44) may struggle to follow the analysis.
- **Required correction** Provide explicit definitions of ϕ, FCR, and κ in the main text or in a table, with a brief explanation of how they are calculated.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Main text, simulation model section
- **Evidence pointer** Location not provided
- **Issue** The text states that the model assumes complete flexibility without dihedral angle constraints. This is a significant simplification for IDPs, which can have local backbone preferences. The potential impact of this assumption on the results is not discussed.
- **Required correction** Add a brief discussion of the limitations of the fully flexible model and justify this choice in the context of the studied sequences.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Main text, discussion of trade-offs
- **Evidence pointer** Location not provided
- **Issue** The concept of a trade-off between cation−π and electrostatic interactions is presented as a general principle, but the simulations are limited to a small set of designed sequences. The generality of the finding is not tested across a broader sequence space.
- **Required correction** Acknowledge the limited sequence space and suggest future work to test the generality of the trade-off across a wider range of sequences and conditions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract
- **Evidence pointer** Location not provided
- **Issue** The abstract states that cation−π interactions provide "greater stabilization of up to 80%" but does not specify the reference point for this percentage. It is unclear whether this is relative to the case without cation−π interactions or to some other baseline.
- **Required correction** Clarify the reference point for the 80% stabilization in the abstract.

## Risk / unsupported claims
- The quantitative claim of up to 80% stabilization via cation−π interactions is not verifiable from the provided text alone, as the figures and numerical data are missing.
- The claim that cation−π interaction strength is independent of salt concentration is stated without sufficient justification or sensitivity analysis.
- The bioinformatic claim of conservation of positively charged residues in LLPS-prone IDRs is not supported by statistical details or control analyses in the provided text.
- The generalizability of the trade-off mechanism beyond the five designed sequences is not established.
- The assumption that the coarse-grained model accurately represents cation−π interactions is not fully validated, as the calibration details are incomplete.