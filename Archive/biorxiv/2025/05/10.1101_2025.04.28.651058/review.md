## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, acknowledgements) as provided by the author. Figures, tables, and supplementary materials referenced but not included.
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by the described evidence. No assessment of formatting, grammar, or journal fit beyond Nature-style criteria.
- **Shared manuscript claim summary** The authors use all-atom explicit-solvent MD simulations to characterize the conformational ensemble and interdomain interaction network of full-length FUS in dilute and condensed phases. They report force-field-dependent chain dimensions, show that folded domain stability modulates global conformation, and identify a conserved electrostatic interaction network in the condensate that correlates with dilute-phase contacts.
- **Visible evidence base** Methods section (simulation protocols, force fields, analysis tools), Results section (quantitative values for Rg, Rh, RMSD, contact patterns), Discussion section (interpretations and mechanistic claims). Figures and tables are referenced but not provided.
- **Missing materials affecting confidence** All figures (Fig. 1-6), supplementary figures (SI Fig. 1-6), and supplementary tables (SI Table 1-2) are absent. Simulation trajectory lengths, convergence metrics, and error bars for reported quantities are not fully specified. The restraint potential equation in Methods is incomplete.

## Reviewer

- **Overall assessment** This manuscript addresses a significant and timely question: how folded domain stability and interdomain interactions collectively govern the conformational ensemble and phase separation of full-length FUS. The use of all-atom simulations with two force fields, systematic comparison to experimental data, and extension to a microsecond-scale condensate simulation represents a substantial computational effort. The central finding that folded domain stability modulates global chain dimensions, while IDR interactions dominate the contact network, is plausible and potentially important. However, the absence of all figures and supplementary materials severely limits the ability to verify the quantitative claims. Several methodological details, including the incomplete restraint potential equation and unclear convergence criteria, need clarification. The claim of a "strong linear correlation" between force-field contact profiles and the extension of dilute-phase principles to condensate behavior require the missing figures for proper evaluation. The manuscript is technically ambitious but the evidence base as provided is insufficient for full assessment.

- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation of FUS and related FET family proteins, computational biophysicists developing and benchmarking force fields for multidomain proteins with IDRs, and experimentalists investigating FUS aggregation in ALS/FTD who seek molecular-level mechanistic hypotheses. The methodological comparison of force fields and the demonstration that folded domain stability affects global conformation will interest the molecular simulation community. The identification of FR π-π interactions and the correlation between dilute and condensed phase contacts may inform future experimental designs.

- **Major strengths**
  1. The study addresses a genuine gap: atomistic characterization of full-length FUS, which is experimentally challenging due to low solubility.
  2. Systematic comparison of two modern force fields with explicit attention to folded domain stability is a rigorous approach.
  3. The extension from single-chain to condensate simulations within a single study provides a coherent multiscale picture.
  4. The identification of specific residue types (arginine, tyrosine, glutamine, serine, glycine) and interaction types (including FR π-π) offers testable hypotheses.
  5. The authors acknowledge limitations of current force fields and propose future directions, showing scientific balance.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The manuscript reports quantitative values for Rg (2.6 ± 0.1 nm for ff03ws; 5.0 ± 0.9 nm for ff99SBws-STQ) and Rh (3.44 ± 0.12 nm and 4.96 ± 0.46 nm) and states these are shown in Fig. 2A, B.
- **Evidence pointer** Fig. 2A, B; location not provided in text
- **Concern** All figures are referenced but not included in the provided material. Without the actual distributions, error bars, and statistical comparisons, the quantitative claims cannot be verified. The reported uncertainties are presented as ± values but the source of these uncertainties (block averaging, multiple trajectories, bootstrap) is not stated. The claim that ff03ws underestimates Rh by ~7% relative to the experimental value of 3.67 ± 0.35 nm depends on the precision of both the simulation and experimental values, which cannot be assessed.
- **Why it matters** The central quantitative claims of the paper, including force-field comparisons and agreement with experiment, rest entirely on these figures. Without them, the reader cannot evaluate whether the differences between force fields are statistically meaningful or whether the agreement with experiment is genuine.
- **Resolution test** Provide all figures with clear axis labels, error bars or shaded regions indicating uncertainty, and statistical significance tests where comparisons are made. State explicitly how uncertainties were computed.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological completeness
- **Claim pointer** The Methods section describes a flat-bottom restraint potential for the RRM domain with the equation "where k = 20 kcal/nm², r1 = 0.27 nm, r2 = 0.3 nm, and r3 = 0.35 nm" but the functional form is not given.
- **Evidence pointer** Methods, "All-atom MD simulations"; location not provided
- **Concern** The restraint potential equation is incomplete. The text states "The potential function is:" followed by parameter values, but the actual equation is missing. This is a critical methodological detail because the restraint scheme directly influences the reported RRM stability and the resulting conformational ensemble. Without the functional form, the work cannot be reproduced.
- **Why it matters** Reproducibility is a core requirement for computational studies. The restraint scheme is not a minor detail; it is central to the claim that stabilizing the RRM domain alters the global conformation. An incomplete equation prevents other researchers from implementing the same protocol.
- **Resolution test** Provide the complete functional form of the restraint potential, including how the flat-bottom region is defined and how forces are computed at the boundaries.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The authors state "a strong linear correlation emerged between the pairwise summations of contacts for both force fields when structural restraints are applied to stabilize folded domains" and reference Fig. 5 and SI Fig. 5.
- **Evidence pointer** Fig. 5, SI Fig. 5; location not provided
- **Concern** The correlation coefficient is not reported in the text. The claim of "strong linear correlation" is qualitative and cannot be evaluated without the figure or a numerical value. Moreover, the interpretation of this correlation as evidence that "contact-prone residue pairs are similar" between force fields requires knowing whether the correlation is driven by a few dominant contacts or is uniform across the contact map.
- **Why it matters** This correlation is used to support the argument that the two force fields converge when folded domains are stabilized, which is a key step in justifying the choice of ff99SBws-STQ-ZBM for the condensate simulation. Without a quantitative measure, the strength of this convergence claim is unclear.
- **Resolution test** Report the Pearson or Spearman correlation coefficient with confidence intervals, and show the scatter plot with a fitted line in the figure.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretive caution
- **Claim pointer** The authors state "the condensate environment did not significantly destabilize these structured regions" based on RMSD analysis of RRM and ZnF domains in the condensate simulation.
- **Evidence pointer** SI Fig. 6B; location not provided
- **Concern** The condensate simulation is described as a single trajectory of 2.5 microseconds with 25 chains. The claim that folded domains remain stable is based on this single trajectory. Sampling limitations are well documented for condensate simulations, and 2.5 microseconds may not be sufficient to observe rare unfolding events or slow conformational rearrangements. The authors do not discuss whether the observed stability is converged or whether longer timescales could reveal different behavior.
- **Why it matters** The stability of folded domains within condensates is a central mechanistic claim with implications for understanding FUS aggregation. Overinterpreting a single trajectory could lead to incorrect conclusions about the role of folded domains in phase separation and disease.
- **Resolution test** Discuss sampling limitations explicitly, report per-chain RMSD distributions rather than averages, and consider additional replicates or enhanced sampling methods to support the stability claim.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Comparison validity
- **Claim pointer** The authors compare their simulated Rg and Rh values to experimental data from DLS (Sukhanova et al., Rh = 3.67 ± 0.35 nm at 200 mM NaCl) and SAXS (Yoshizawa et al., Rg = 4.87 nm for MBP-tagged FUS at 0.5 M NaCl).
- **Evidence pointer** Results, "Conformational Ensembles of FL FUS Monomer"; location not provided
- **Concern** The experimental comparisons involve different solution conditions (salt concentration, presence of MBP tag) and different techniques (DLS measures hydrodynamic radius, SAXS measures radius of gyration). The authors acknowledge the MBP tag in the Yoshizawa study but do not discuss how the tag might affect the measured Rg. The Sukhanova study used 200 mM NaCl while simulations used 150 mM, and the authors earlier note that high salt concentrations (1 M KCl) affect the ensemble. The sensitivity of FUS conformation to salt concentration means these comparisons may not be apples-to-apples.
- **Why it matters** The claim that ff99SBws-STQ-ZBM provides a "reasonable estimate of chain dimensions with respect to experiment" is a key validation step. If the experimental comparisons are confounded by different conditions, the validation is weakened.
- **Resolution test** Discuss the potential impact of salt concentration differences and the MBP tag on the comparison. Consider additional experimental references at matched conditions, or explicitly state the limitations of the comparison.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods, "All-atom MD simulations"
- **Evidence pointer** Methods; location not provided
- **Issue** The text states "All systems were simulated in explicit solvent, modeled using the Amber ff03ws or ff99SBws-STQ force fields and the TIP4P/2005 water model, 50–52,66 with improved NaCl parameters." The reference numbering appears inconsistent with the earlier citation of the same force fields.
- **Required correction** Verify all citation numbers are correct and consistent throughout the manuscript.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods, "MD trajectory analysis"
- **Evidence pointer** Methods; location not provided
- **Issue** The text states "The gmx polystat command was used to compute the radius of gyration (Rg) and end-to-end distance (Dee)" but does not specify which GROMACS version was used for analysis, while production simulations used Amber 22 or OpenMM 8.1.1.
- **Required correction** Specify the GROMACS version used for trajectory analysis.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results, "Conformational Ensembles of FL FUS Monomer"
- **Evidence pointer** Results; location not provided
- **Issue** The reported Rg and Rh values are given as mean ± standard deviation, but the number of independent samples (trajectories, chains) used to compute these statistics is not stated.
- **Required correction** Report the number of independent trajectories and the method used to estimate statistical uncertainties.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Results, "FL FUS condensate simulation"
- **Evidence pointer** Results; location not provided
- **Issue** The term "universal residue participation" is used to describe the finding that all residue types contribute to condensate contacts. This is an overstatement; the data likely show that all residue types participate to some degree, not that participation is universal in a quantitative sense.
- **Required correction** Rephrase to "all residue types contribute to the contact network" or similar.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interpretive clarity
- **Affected element** Discussion
- **Evidence pointer** Discussion; location not provided
- **Issue** The statement "folded domains primarily function as passive structural scaffolds rather than active participants" is presented as a conclusion, but the data show that folded domains do participate in some contacts, just to a lesser extent than IDRs. The word "passive" may be too strong.
- **Required correction** Qualify the statement to reflect the quantitative degree of participation rather than a binary passive/active distinction.

- **Technical failings that need to be addressed before the case is established**
  1. Incomplete restraint potential equation in Methods (R1-M2).
  2. All figures and supplementary materials absent from the provided manuscript, preventing verification of quantitative claims (R1-M1).
  3. No convergence analysis or sampling assessment for the condensate simulation beyond a single trajectory.
  4. Statistical treatment of reported uncertainties not described.
  5. Experimental comparisons involve mismatched conditions (salt concentration, tags) without adequate discussion.

- **Assessment against Nature-style criteria**
  - **Originality** The work is original in its scope: atomistic simulation of full-length FUS in both dilute and condensed phases with systematic force-field comparison. The finding that folded domain stability modulates global conformation while IDRs dominate contacts extends prior work on isolated domains or truncated constructs. However, the conceptual framework (IDR-driven phase separation, correlation between single-chain and condensed-phase contacts) builds on established principles from prior studies by the same group and others.
  - **Scientific importance** The results are potentially important for understanding FUS phase separation and aggregation in ALS/FTD. The mechanistic distinction between folded domain stability and IDR interactions could inform therapeutic strategies. However, the importance is tempered by the reliance on a single condensate simulation and the acknowledged force-field limitations.
  - **Interdisciplinary readership** The topic bridges biophysics, computational chemistry, and neurobiology. The findings on force-field performance and folded domain stability will interest simulators; the interaction network analysis may interest experimentalists studying FUS. The clinical relevance to ALS/FTD broadens the potential audience. However, the technical density of the methods may limit accessibility to non-specialists.
  - **Technical soundness** The simulation protocols are largely standard and follow established practices from the group's prior work. The force-field comparison is appropriate. However, the incomplete restraint equation, unclear convergence criteria, and single-trajectory condensate simulation are technical weaknesses. The use of two force fields and comparison to experimental data is a strength.
  - **Readability for nonspecialists** The manuscript is clearly written but assumes familiarity with MD simulation terminology and phase separation concepts. The abstract is accessible. The Results section is organized logically. The Discussion effectively contextualizes findings. Some terms (e.g., "sp²/π plane angle-distance distribution") may be opaque to non-specialists.

- **Recommendation posture** Supportive if technical concerns are resolved. The core scientific question is significant, the approach is appropriate, and the findings are potentially valuable. However, the manuscript cannot be fully evaluated without the missing figures and supplementary materials. The incomplete Methods equation must be corrected. The single-trajectory condensate simulation and the experimental comparisons under mismatched conditions require more careful discussion of limitations. If these issues are addressed, the manuscript could make a solid contribution to the field.

## Risk / unsupported claims
- The claim of "strong linear correlation" between force-field contact profiles (R1-M3) is unsupported without the correlation coefficient or figure.
- The claim that "the condensate environment did not significantly destabilize these structured regions" is based on a single trajectory and may not be generalizable.
- The statement that "FR π-π interactions" were "previously hypothesized but unverified" and are now "confirmed" is stronger than the evidence supports; the analysis identifies such interactions in simulation, but experimental confirmation is lacking.
- The assertion that the modified force field (ff99SBws-STQ-ZBM) is "the most suitable model for describing FL FUS behavior" is based on comparison to limited experimental data under different conditions.
- The claim that "single-chain simulations recapitulate condensate interaction profiles" is presented as a general principle but is based on one protein system and one condensate simulation.
- The statement that folded domains "primarily function as passive structural scaffolds" is an interpretation that goes beyond the direct evidence of contact frequencies.