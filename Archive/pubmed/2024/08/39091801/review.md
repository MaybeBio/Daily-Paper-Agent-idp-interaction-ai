## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv 2024.08.02, DOI 10.1101/2024.07.17.604679)
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the provided manuscript text. Supplementary materials referenced but not fully provided.
- **Shared manuscript claim summary** The authors propose that transient non-local intramolecular interactions between regions distant in the sequence of the intrinsically disordered measles virus NTAIL domain dominate its conformational dynamics. They use PET experiments, coarse-grained and all-atom simulations, and coevolutionary analysis to identify specific interactions that stabilize distinct conformational states, which they argue regulate the conformational preferences of the MoRE and may modulate binding to the phosphoprotein X domain (PXD), with implications for polymerase recruitment and viral transcription/replication.
- **Visible evidence base** Main text figures (Figs. 1–6), tables (Tables S1–S7 referenced), methods sections, and abstract. Supplementary figures and tables are referenced but not fully visible in the provided material.
- **Missing materials affecting confidence** Full supplementary information (detailed methods, additional figures S1–S28, tables S1–S7), raw PET data, simulation parameter files, and coevolutionary analysis details. These are essential for fully evaluating methodology and reproducibility.

## Reviewer

- **Overall assessment** This manuscript presents an integrated experimental and computational study of the dynamics of the intrinsically disordered NTAIL domain of measles virus nucleoprotein. The work addresses an important and timely question in IDP biology: how non-local interactions within disordered regions can shape conformational ensembles and potentially regulate function. The combination of PET experiments with coarse-grained and all-atom simulations is a strength, and the identification of specific conformational states stabilized by distinct interaction networks is a notable contribution. However, several technical concerns and interpretive gaps need to be addressed before the central claims are fully established. The link between the observed intramolecular interactions and functional regulation of PXD binding remains largely speculative, and the quantitative agreement between simulations and experiments, while encouraging, is based on limited sampling and a small number of variants. The manuscript would benefit from a more critical discussion of the limitations of the approaches and a clearer articulation of the evidence supporting the proposed regulatory mechanisms.

- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, viral molecular biology (particularly paramyxoviruses), biophysics of protein dynamics, and computational chemistry. The work is relevant to those studying how IDP conformational dynamics are encoded by sequence and how they influence molecular recognition. The methodological integration of PET, CG, and all-atom simulations will be of interest to biophysicists developing and applying such approaches to IDPs.

- **Major strengths**
  1. The study addresses a significant and under-explored question: the role of non-local interactions in IDP dynamics and function, specifically for a biologically important viral protein.
  2. The combination of multiple complementary techniques (PET experiments, CG simulations, all-atom simulations, coevolutionary analysis) is a powerful approach to tackle the problem.
  3. The careful validation of force fields against multiple experimental observables (SAXS, CD, NMR) is commendable and strengthens confidence in the simulation results.
  4. The identification of four distinct conformational states with specific interaction patterns provides a concrete and testable model for NTAIL dynamics.
  5. The proposal of specific mechanisms (direct competition and indirect allosteric regulation) linking intramolecular interactions to PXD binding is thought-provoking and generates testable hypotheses.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / Data interpretation
- **Claim pointer** The claim that "transient interactions between two disordered regions distant in sequence... dominate NTAIL dynamics" is central to the paper.
- **Evidence pointer** Figure 1D, Figure 2, Figure 3, Figure 4
- **Concern** The central claim that non-local interactions "dominate" NTAIL dynamics is not fully supported by the data presented. The PET experiments show deviations from homopolymer scaling, but these are modest for most variants. The all-atom simulations identify four conformational states, but these states collectively represent only ~48% of the ensemble, meaning that a majority of conformations do not fall into these discrete states. The claim of "domination" requires a more quantitative demonstration that these interactions are the primary determinant of the observed dynamics, rather than one contributing factor among many (e.g., local secondary structure propensities, chain connectivity).
- **Why it matters** The title and abstract make a strong claim about the dominance of non-local interactions. If this is overstated, it misrepresents the significance of the findings and could mislead the field. A more nuanced interpretation would strengthen the paper.
- **Resolution test** The authors should provide a quantitative measure of the contribution of non-local interactions to the overall dynamics, e.g., by comparing the dynamics of variants where these interactions are disrupted (via mutation) to the wild-type, or by decomposing the free energy landscape to show the relative stability of states stabilized by non-local vs. local interactions. Alternatively, they could soften the claim to "significant" or "important" rather than "dominate."

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / Simulation-experiment agreement
- **Claim pointer** The claim that all-atom simulations "reproduce" the experimentally observed dynamic heterogeneity (Section "Disordered NTAIL is characterized by a conformational ensemble with distinct states").
- **Evidence pointer** Figure 2D, Figure 3, Supporting Figures S21–S22
- **Concern** The agreement between simulated and experimental relaxation times is presented as validation, but the uncertainties are large. The simulated τCW for C3W2 is 5.3 ± 3.3 μs, which overlaps with the experimental value of 7.6 μs, but the uncertainty is more than 60% of the mean. For C4W2, the simulated value is 2.0 ± 0.5 μs vs. experimental 2.3 μs, which is better, but this is only two data points. The claim that the simulations "accurately describe" the dynamics is not convincingly established with such large uncertainties and a small number of comparisons. Furthermore, the free energy landscape is computed from combined trajectories of both variants, which may obscure variant-specific differences.
- **Why it matters** The reliability of the structural interpretation (the four states and their interactions) depends critically on the accuracy of the simulations. If the simulations are not quantitatively reliable, the specific interactions identified may be artifacts of the force field or sampling limitations.
- **Resolution test** The authors should provide a more rigorous statistical comparison between simulated and experimental observables, including confidence intervals and a discussion of the expected precision given the sampling. They should also consider simulating additional variants to increase the number of comparisons. If the uncertainties cannot be reduced, the claims should be tempered accordingly.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance / Functional relevance
- **Claim pointer** The claim that the identified non-local interactions "regulate the conformational preferences of both the MoRE and the entire NTAIL domain" and the proposed mechanisms for regulating PXD binding.
- **Evidence pointer** Figure 6, Discussion section
- **Concern** The functional relevance of the identified interactions is largely speculative. The coevolutionary analysis provides correlative evidence, but the specific interactions identified in simulations (e.g., salt bridges between regions B and E) are not directly tested experimentally. The proposed mechanisms (direct competition and indirect allosteric regulation) are plausible but are not supported by direct experimental evidence, such as mutagenesis studies that disrupt the predicted interactions and measure effects on PXD binding. The discussion of the functional role in viral replication is even more speculative, extrapolating from in vitro and simulation data to complex viral processes.
- **Why it matters** The paper's significance is substantially enhanced if the identified interactions have functional consequences. Without experimental validation, the functional claims remain hypotheses, and the impact of the work is diminished.
- **Resolution test** The authors should either (a) perform mutagenesis experiments to disrupt the predicted key interactions and measure the effects on PXD binding affinity and kinetics, or (b) clearly frame these as hypotheses and discuss how they could be tested. The Discussion should be revised to distinguish between established findings and speculative proposals.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness / Methodology
- **Claim pointer** The use of PET experiments to measure contact formation times and the interpretation of these times in terms of conformational dynamics.
- **Evidence pointer** Methods section "Photo-induced electron transfer (PET) experiments", Figure 1D
- **Concern** The PET method relies on the assumption that the measured relaxation time is directly related to the contact formation time between W and C. This assumption requires that the quenching process is diffusion-limited and that the intrinsic electron transfer rate is fast compared to the contact formation rate. The authors state they assumed reaction-limited kinetics for the CG analysis, which is inconsistent with the diffusion-limited assumption. This inconsistency needs to be clarified. Additionally, the effect of the mutations (Y to W, S to C) on the local conformational preferences and dynamics is not discussed. These mutations could alter the very interactions the authors aim to probe.
- **Why it matters** If the PET measurements are not correctly interpreted, the experimental basis for the observed dynamic heterogeneity is compromised. The mutations could introduce artifacts that are misinterpreted as intrinsic properties of the wild-type protein.
- **Resolution test** The authors should clarify the kinetic regime of the PET quenching and justify the use of reaction-limited vs. diffusion-limited models. They should also discuss the potential perturbations introduced by the mutations and, ideally, validate that the mutations do not significantly alter the conformational ensemble (e.g., by comparing CD or NMR spectra of the variants to the wild-type).

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity / Reproducibility
- **Affected element** Methods section "Coarse-grained molecular dynamics"
- **Evidence pointer** Methods section, Supporting Methods S5
- **Issue** The description of the modified HPS model is brief. The specific modifications to the original HPS model, the parameterization of the angle and dihedral terms, and the fitting procedure to reproduce the experimental radius of gyration are not described in sufficient detail in the main text.
- **Required correction** Provide a more detailed description of the model modifications and parameterization in the main text or refer more explicitly to the Supporting Information. Ensure that all parameters are available for reproducibility.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity / Data presentation
- **Affected element** Figure 1D
- **Evidence pointer** Figure 1D
- **Issue** The figure shows experimental data and model predictions, but the error bars on the experimental data are not defined in the caption. It is unclear whether they represent standard deviations, standard errors, or confidence intervals.
- **Required correction** Define the error bars in the figure caption and state the number of independent measurements.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation / Literature context
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The discussion of the functional implications for viral replication is interesting but would benefit from a more explicit connection to the existing literature on paramyxovirus replication and the role of NTAIL in this process. Some statements are made without direct citations.
- **Required correction** Add appropriate citations to support the statements about the role of NTAIL in viral replication and the importance of PXD binding kinetics.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity / Terminology
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, Introduction
- **Issue** The term "non-local interactions" is used throughout, but its definition is not explicitly stated. It is implied to mean interactions between residues far apart in sequence, but this should be stated explicitly for clarity, especially for readers not familiar with the IDP field.
- **Required correction** Define "non-local interactions" explicitly at first use.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness / Statistical analysis
- **Affected element** Coevolutionary analysis section
- **Evidence pointer** Section "Functional relevance of non-local interactions is supported by coevolutionary analysis", Figure S28
- **Issue** The coevolutionary analysis is presented as supporting evidence, but the statistical significance of the identified coevolving pairs is not discussed. It is unclear how the significance threshold was set and whether the highlighted pairs are significantly above background.
- **Required correction** Provide details on the statistical significance of the coevolutionary signals and how the threshold for "high scores" was determined.

## Risk / unsupported claims
- The claim that non-local interactions "dominate" NTAIL dynamics is not quantitatively supported and may be overstated.
- The proposed mechanisms for regulating PXD binding (direct competition and indirect allosteric regulation) are speculative and not directly tested experimentally.
- The functional relevance of the identified interactions for viral replication is highly speculative and extrapolated from in vitro and simulation data.
- The quantitative agreement between simulations and experiments is based on limited data with large uncertainties, making the claim of accurate reproduction of dynamics not fully established.
- The assumption that PET measurements directly report on contact formation times without significant perturbation from the introduced mutations is not validated.
- The coevolutionary analysis is presented as corroborating evidence, but the statistical significance of the identified pairs is not established in the provided text.