## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, conclusions, and figure references
- **Assessment boundary** Scientific validity of claims based on the provided manuscript text; no external data or supplementary materials were available for verification
- **Shared manuscript claim summary** The authors propose a planar BC3/C3N/BC3 heterostructure that can stretch and confine intrinsically disordered proteins (Aβ1–42, polyQ42, α-Syn61–95) via stronger adsorption to the C3N stripe, reducing conformational fluctuations for potential single-molecule protein analysis
- **Visible evidence base** Molecular dynamics simulation trajectories, contact number analysis, interaction energy calculations, water density maps, and end-to-end distance distributions as described in the text and referenced figures
- **Missing materials affecting confidence** Supplementary figures (S1–S5) referenced but not provided; simulation parameter details beyond those stated; force field validation data; convergence criteria for the 400 ns trajectories; raw trajectory data or error bars for quantitative claims

## Reviewer
- **Overall assessment** The manuscript presents a computationally driven hypothesis for a novel 2D heterostructure application in protein manipulation. The core idea is interesting and potentially useful for the single-molecule sensing community. However, the evidence provided is largely qualitative, with limited quantitative analysis of simulation convergence, statistical robustness, or comparison to alternative designs. The mechanistic claims are plausible but not fully established from the presented data.
- **Who would be interested in the results, and why** Researchers in single-molecule biophysics, nanopore and nanochannel sensing, 2D materials for biomedical applications, and computational studies of protein-surface interactions would find this relevant. The proposed soft confinement concept could inspire experimental designs for protein stretching prior to sequencing.
- **Major strengths** The heterostructure design is conceptually novel and leverages the distinct adsorption properties of BC3 and C3N. The use of multiple IDP types strengthens the generality of the observed behavior. The inclusion of water structure analysis adds a useful mechanistic layer. The discussion of practical implications for sequencing and clogging mitigation is thoughtful.
- **Major Concerns** The quantitative support for the central claims is thin. The manuscript relies heavily on visual inspection of trajectories and single representative simulations. The claim of reduced conformational fluctuations is based on distribution widths, but no statistical measures such as standard deviations or confidence intervals are provided. The interaction energy scan is performed on a rigidly moved conformation, which may not reflect the dynamic adaptation of the peptide. The effect of C3N stripe width is explored only through energy scans, not dynamic simulations, limiting the strength of the recommendation for 1.2 nm width. The role of water clusters in confinement is inferred from density maps but not directly tested, for example by comparing simulations with and without explicit water structuring.
- **Minor Comments** The abstract states "three types of IDPs" but the main text focuses heavily on Aβ, with polyQ and α-Syn given less detailed treatment. The method section mentions pre-equilibration on BC3 before constructing the heterostructure, but the potential bias this introduces is not discussed. The claim that BC3 and C3N have higher biocompatibility than graphene is cited but not elaborated. The conclusion mentions pressure-driven delivery to a nanochannel, which is speculative and not supported by simulation.
- **Technical failings that need to be addressed before the case is established** Lack of replicate simulations and error analysis for key quantitative claims; absence of convergence assessment for the 400 ns trajectories; no validation that the frozen heterostructure approximation does not affect the results; the rigid scan for energy profiles may miss conformational rearrangements that could alter the potential landscape.
- **Assessment against Nature-style criteria** Originality is moderate to high, as the specific heterostructure application is new, though the general concept of adsorption-based confinement is known. Scientific importance is moderate, as the work is purely computational and lacks experimental validation, limiting immediate impact. Interdisciplinary readership is plausible, but the manuscript is written primarily for a computational biophysics audience. Technical soundness is adequate for a simulation study, but the lack of statistical rigor weakens the conclusions. Readability for nonspecialists is acceptable, though some jargon and methodological details could be clarified.
- **Recommendation posture** Supportive if technical concerns are resolved, specifically the addition of replicate simulations, statistical measures, and dynamic tests of the width and water effects.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical robustness
- **Claim pointer** "The conformational fluctuations of IDPs are substantially reduced after being stretched" and "the fluctuations of L/N are reduced after the peptides are stretched"
- **Evidence pointer** Figure 2D, Figure 3, Figures S1 and S2 (not provided)
- **Concern** The claim of reduced conformational fluctuations is based on the width of L/N distributions, but no quantitative measures such as standard deviation, variance, or statistical tests are reported. It is unclear whether the observed narrowing is significant given the small number of trajectories and the high flexibility of IDPs.
- **Why it matters** The central practical benefit of the proposed device is noise reduction for single-molecule sensing. Without statistical evidence, the claim that fluctuations are "substantially reduced" is not established.
- **Resolution test** Provide at least three independent replicate simulations per condition, report mean and standard deviation of L/N distributions, and perform a statistical test (e.g., ANOVA or t-test) comparing the widths across environments.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic evidence
- **Claim pointer** "The protein molecules interact more strongly with the C3N stripe than the BC3 one, which leads to their capture, elongation, and confinement"
- **Evidence pointer** Figure 4A–C, Figures S3 and S4 (not provided)
- **Concern** The interaction energy scan in Figure 4C is performed by rigidly moving a stretched conformation of Aβ from C3N to BC3. This approach ignores conformational adaptation of the peptide, which could significantly alter the energy landscape. The contact number analysis in Figure 4A is averaged over time but no error bars or trajectory-to-trajectory variability is shown.
- **Why it matters** The mechanism of preferential adsorption to C3N is the foundation of the entire design. If the energy difference is an artifact of the rigid scan, the proposed mechanism may not hold in dynamic conditions.
- **Resolution test** Perform free energy calculations (e.g., umbrella sampling or metadynamics) that allow the peptide to adapt during the transfer from C3N to BC3, and compare the resulting potential of mean force with the rigid scan results.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Parameter sensitivity
- **Claim pointer** "the C3N layer width of 1.2 nm is recommended for efficient protein stretching"
- **Evidence pointer** Figure S5 (not provided)
- **Concern** The recommendation for 1.2 nm width is based solely on static energy scans of the potential well depth and width. No dynamic simulations are performed at different stripe widths to test whether the predicted optimal width actually leads to faster or more stable stretching. The inflection point at 1.2 nm is presented without error analysis or justification for why this specific width is optimal.
- **Why it matters** The practical utility of the design depends on the robustness of the width recommendation. If the optimal width is sensitive to simulation conditions or peptide type, the design may not be generally applicable.
- **Resolution test** Run dynamic simulations of Aβ stretching on heterostructures with stripe widths of 0.6, 1.2, and 1.8 nm, and compare the time to reach a stretched state and the stability of the stretched conformation.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Role of water
- **Claim pointer** "These interfacial water molecules might further strengthen the restriction on the linear conformation of IDPs"
- **Evidence pointer** Figure 5A–E
- **Concern** The claim that water clusters on BC3 act as steric hindrances is speculative. The water density maps show periodic clusters, but no direct evidence links these clusters to reduced peptide mobility on BC3. The authors do not test this hypothesis, for example by comparing simulations with modified water models or by analyzing the correlation between water cluster positions and peptide contact points.
- **Why it matters** The water-mediated mechanism is presented as an additional factor in confinement. If it is incorrect, the overall understanding of the system is incomplete, and the design principles may be misattributed.
- **Resolution test** Perform simulations where the partial charges on BC3 are set to zero (removing the water clustering effect) and compare the peptide dynamics and confinement efficiency with the original system.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, Section 1
- **Issue** The abstract states "three types of IDPs" but the main text focuses heavily on Aβ, with polyQ and α-Syn given less detailed treatment. The introduction could better clarify why these specific IDPs were chosen and whether they represent distinct classes of IDPs.
- **Required correction** Specify in the abstract or introduction the rationale for selecting these three IDPs and note any differences in their behavior that are relevant to the conclusions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological transparency
- **Affected element** Section 2
- **Evidence pointer** Section 2, paragraph on simulation setup
- **Issue** The method states that the heterostructure atoms are frozen, but the potential impact of this constraint on the results is not discussed. Freezing the surface may affect the adsorption dynamics and the water structure near the surface.
- **Required correction** Add a sentence discussing the rationale for freezing the heterostructure and any known limitations of this approximation in similar studies.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Quantitative reporting
- **Affected element** Section 3, Figure 2D
- **Evidence pointer** Figure 2D description
- **Issue** The L/N values are reported as increasing from ~1.0 Å to 2.2–2.3 Å, but no error bars or standard deviations are shown. It is unclear how much variability exists across trajectories or time points.
- **Required correction** Include error bars or confidence intervals in Figure 2D and report the number of independent simulations used for the average.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Speculation
- **Affected element** Section 4
- **Evidence pointer** Section 4, final paragraph
- **Issue** The conclusion mentions pressure-driven delivery of stretched proteins to a nanochannel as a potential application. This is speculative and not supported by any simulation or experimental data in the manuscript.
- **Required correction** Either remove this speculation or clearly label it as a future direction that requires further investigation.

## Risk / unsupported claims
- The claim that the heterostructure can be coupled with nanopore or nanochannel sensing to ease clogging is speculative and not tested in this work.
- The statement that BC3 and C3N have higher biocompatibility than graphene is cited but not elaborated or supported by data in this manuscript.
- The recommendation for a 1.2 nm C3N stripe width is based on static energy scans only and is not validated by dynamic simulations at different widths.
- The role of interfacial water clusters in enhancing confinement is inferred from density maps but not directly tested.
- The claim of "substantially reduced" conformational fluctuations lacks statistical support due to the absence of replicate simulations and error analysis.