## Review setup
- **Input scope** Full manuscript text (main text, significance statement, methods summary) without figures, tables, or supplementary appendix content
- **Assessment boundary** Scientific claims, methodological soundness, and interpretive validity as presented in the provided text; figure and SI content referenced but not directly assessable
- **Shared manuscript claim summary** The authors report TR-FRET measurements using TCSPC to resolve the position and dynamics of the disordered C-terminal tail of human cardiac troponin T (C-cTnT) in reconstituted thin filaments under three biochemical states (blocked, closed, open), combined with constrained molecular dynamics simulations to identify intermolecular interactions. They report that two cardiomyopathic mutations, D270N (DCM) and K273E (HCM), differentially alter C-cTnT position and flexibility, and propose a flycasting mechanism whereby C-cTnT regulates the energy barrier for tropomyosin movement.
- **Visible evidence base** Main text descriptions of TR-FRET distances and FWHM values, MD simulation interaction frequencies, DSC thermal stability measurements, myosin activity assays; references to SI figures and tables for numerical data
- **Missing materials affecting confidence** All figures, SI tables with numerical values, SI figures referenced throughout, detailed methods in SI, MD simulation parameters, and statistical analysis details are not provided in the supplied material

## Reviewer
- **Overall assessment** The manuscript addresses a genuinely important and technically challenging problem: the structural and dynamic characterization of a disordered region of cardiac troponin T that is a hotspot for disease-causing mutations. The combination of time-resolved FRET with constrained MD simulations is a reasonable and potentially powerful approach. However, the provided text alone does not permit full evaluation of the central claims. Key numerical data, statistical comparisons, and methodological details are relegated to the SI, which was not supplied. Several interpretive leaps, particularly regarding the flycasting mechanism and the energetic implications for tropomyosin movement, are presented as conclusions without direct energetic measurements. The differential effects of the two mutations are described but the mechanistic explanation remains somewhat speculative. The manuscript is likely to be of interest to the cardiac muscle biophysics and structural biology communities, but the strength of the conclusions cannot be fully assessed from the supplied material.

- **Who would be interested in the results, and why** Cardiac muscle biophysicists and structural biologists studying thin filament regulation would be the primary audience. Investigators studying hypertrophic and dilated cardiomyopathy mechanisms, particularly those focused on troponin mutations, would also find the results relevant. The methodological approach combining TR-FRET with MD simulations for disordered protein regions may interest a broader biophysics audience. Clinically oriented researchers studying genotype-phenotype relationships in cardiomyopathies may find the differential effects of D270N and K273E informative.

- **Major strengths** The study addresses a region of troponin T that has remained structurally unresolved despite advances in cryo-EM, and the authors employ a technically sophisticated approach (TCSPC-based TR-FRET) that provides higher resolution than prior steady-state FRET studies. The use of fully human proteins in reconstituted thin filaments is a notable improvement over mixed-species systems. The integration of experimental distance constraints with atomistic MD simulations is a sensible strategy for disordered systems. The comparison of two clinically distinct mutations (DCM vs HCM) within the same structural region provides a useful framework for understanding how different perturbations produce different disease phenotypes.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "WT C-cTnT undergoes a disordered to ordered transition as the thin filament transitions from the blocked to the open state, near the IT arm (cTnT-274C), while the terminal tail (cTnT-283C) stays disordered and flexible regardless of biochemical state."
- **Evidence pointer** Results section "Structure and Dynamics of WT C-cTnT in Relation to cTnC"; Fig. 1; SI Appendix Tables S1 and S2
- **Concern** The central claim of a state-dependent disorder-to-order transition rests on FWHM comparisons across three biochemical conditions. The text reports that myosin binding decreased FWHM at cTnT-274C to both cTnC lobes (15.4 ± 2.2 Å and 8.3 ± 1.9 Å), but the statistical significance of these changes relative to the calcium-free and calcium-only conditions is not stated in the text. The numerical values for the other conditions are only in SI tables that were not provided. Without explicit statistical comparisons (p-values, confidence intervals, or effect sizes) for all pairwise condition comparisons, the claim of a discrete transition cannot be evaluated. Additionally, the text states "calcium has minimal effects on C-cTnT structure and flexibility" but then reports a 5.7 Å decrease in distance to the C-lobe upon calcium binding; the authors should clarify why a change of this magnitude is considered minimal.
- **Why it matters** The disorder-to-order transition is a central conceptual finding of the paper and underpins the proposed flycasting mechanism. If the FWHM changes are not statistically robust, or if the interpretation of "minimal" calcium effects is not justified, the mechanistic narrative loses its foundation.
- **Resolution test** Provide explicit statistical comparisons (with p-values or confidence intervals) for all pairwise comparisons of distances and FWHM across the three biochemical states for both reporter positions. State the threshold for significance and how multiple comparisons were handled. Justify the characterization of calcium effects as "minimal" with reference to the magnitude of change relative to measurement uncertainty and biological relevance.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological validation
- **Claim pointer** The authors state: "After integration of the FRET distances, average structures from three, 10 ns production runs of the C-cTnT for the blocked, closed, and open states were obtained" and use these to identify intermolecular interactions.
- **Evidence pointer** Results section "Atomic Resolution of WT C-cTnT"; Methods section "Molecular Dynamics"; SI Appendix Figs. S14–S16
- **Concern** The MD simulation protocol is described only briefly. Three 10 ns production runs are short for a disordered region, and the text does not describe how the FRET distance restraints were applied (e.g., flat-bottom potentials, harmonic restraints, force constants), how convergence was assessed, or whether the three runs sampled the same or different conformational ensembles. The text also does not state how the "average structure" was computed from the production ensembles or whether this average is physically meaningful for a disordered region. The interaction frequencies reported (e.g., "present for ≥10% of the trajectory") depend entirely on the simulation quality and restraint scheme, which cannot be evaluated from the supplied text.
- **Why it matters** The intermolecular interaction maps are used to explain the differential effects of the two mutations and to support the proposed mechanism. If the simulations are not converged, if the restraint scheme biases the results, or if the averaging procedure obscures meaningful conformational heterogeneity, the interaction frequencies and the conclusions drawn from them are unreliable.
- **Resolution test** Provide a detailed description of the restraint scheme, force constants, equilibration protocol, and convergence criteria. Show that the three production runs sample similar distributions (e.g., RMSD convergence plots, replica overlap metrics). Justify the choice of 10 ns per run for a disordered region and demonstrate that the interaction frequencies are stable over the simulation time. Describe how the average structure was computed and whether alternative averaging schemes (e.g., clustering) give consistent results.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretive validity
- **Claim pointer** The authors propose "a flycasting mechanism, like that of the C-terminal tail of cTnI, is occurring in this region of cTnT" and that C-cTnT "regulates the energy barrier required to shift tropomyosin from the blocked to closed to open states."
- **Evidence pointer** Discussion section; Results section "Effects of cTnT Mutations on Thin Filament Thermodynamics"
- **Concern** The flycasting mechanism is presented as a hypothesis but is not directly tested. The DSC experiments measure thermal stability of the troponin-tropomyosin complex, which is an indirect proxy for the energy barrier of tropomyosin movement. The text reports that D270N and K273E both reduce thermal stability in the absence of calcium, but the connection between reduced thermal stability and a lowered energy barrier for tropomyosin displacement is not established. The authors acknowledge they "did not directly measure this" but the Discussion section presents the mechanism with considerable confidence. The leap from local structural changes to altered whole-filament energetics to disease mechanism requires either direct energetic measurements or a more carefully qualified interpretation.
- **Why it matters** The proposed mechanism is the primary conceptual contribution of the paper. If the connection between the observed structural changes and the proposed functional consequences is not rigorously established, the significance of the findings is substantially diminished.
- **Resolution test** Either provide direct measurements or calculations of the energy barrier for tropomyosin movement (e.g., metadynamics simulations, as the authors note they are planning) or substantially temper the mechanistic claims in the Discussion. Clarify what specific predictions the flycasting mechanism makes that could be tested in future experiments, and distinguish between what the current data directly show versus what they suggest.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Control and validation
- **Claim pointer** The authors state: "We found no differences in myosin activity when cysteine-substituted proteins were bound with our FRET probes, suggesting the presence of bound probes do not contribute to the changes seen in our FRET data."
- **Evidence pointer** Results section; SI Appendix Fig. S2
- **Concern** The myosin activity assay is used to validate that the FRET probes do not perturb function, but the text does not report the actual activity values for the labeled versus unlabeled proteins, the statistical power of the comparison, or whether the assay would be sensitive enough to detect functionally relevant perturbations. The assay was performed "in the absence of calcium" for the mutation studies, but the FRET experiments were conducted under three conditions; validation of probe effects under only one condition may not be sufficient. Additionally, the text does not state whether the activity assay was performed with the same protein preparations used in the FRET experiments.
- **Why it matters** The interpretation of the FRET data depends on the assumption that the probes do not alter the structure or dynamics being measured. If the validation is underpowered or incomplete, the FRET measurements could reflect probe-induced artifacts rather than native behavior.
- **Resolution test** Report the actual activity values for labeled and unlabeled proteins with appropriate statistics. State the minimum effect size the assay could detect given the sample size and variability. If feasible, validate probe effects under all three biochemical conditions used in the FRET experiments.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and precision
- **Affected element** Results section "Structure and Dynamics of WT C-cTnT in Relation to cTnC"
- **Evidence pointer** Fig. 1; SI Appendix Tables S1 and S2
- **Issue** The text states "calcium has minimal effects on C-cTnT structure and flexibility" but then reports a 5.7 Å decrease in distance between cTnT-274C and the C-lobe of cTnC upon calcium binding. The term "minimal" is not defined quantitatively, and a change of nearly 6 Å may be structurally significant.
- **Required correction** Define what constitutes a "minimal" effect in the context of the measurement precision and the magnitude of changes observed with myosin binding. Alternatively, rephrase to describe the specific changes observed without the qualitative label.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of reporting
- **Affected element** Results section "Structural and Dynamic Effects of DCM-Associated cTnT-D270N"
- **Evidence pointer** Fig. 2; SI Appendix Table S1
- **Issue** The text reports that D270N "moved cTnT-274C (12.3 Å) and 283C (14.2 Å) closer to the C-lobe of cTnC" in the absence of calcium, but does not report the corresponding changes in FWHM for these conditions in the main text. The FWHM changes are described qualitatively ("decreased the FWHM near the IT arm") but the numerical values are only in the SI.
- **Required correction** Include the key FWHM values and their statistical comparisons in the main text or a main-text table, as these are central to the claim of altered flexibility.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Consistency of interpretation
- **Affected element** Discussion section
- **Evidence pointer** Location not provided
- **Issue** The Discussion states that D270N "does not alter C-cTnT structure or stability in a manner in which myosin activity is affected" based on the activity assay, but earlier the authors report that D270N does alter structure and flexibility in the FRET experiments. The distinction between structural changes that do and do not affect function is not clearly articulated.
- **Required correction** Clarify the relationship between the observed structural changes and the lack of functional effect in the activity assay. Discuss what magnitude or type of structural change would be expected to produce a functional effect.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Methodological transparency
- **Affected element** Methods section "Molecular Dynamics"
- **Evidence pointer** Location not provided
- **Issue** The methods state simulations were performed "as previously described" with a citation, but the key parameters relevant to this study (restraint scheme, force constants, equilibration time, temperature/pressure coupling) are not summarized.
- **Required correction** Provide a brief summary of the key simulation parameters in the main text or ensure the SI methods section contains all necessary details for reproduction.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion section
- **Evidence pointer** Location not provided
- **Issue** The comparison with the prior study by Zhu et al. is useful, but the discussion of how the present findings extend or contradict other structural models of thin filament regulation is limited. The authors mention cryo-EM structures but do not discuss how their dynamic findings relate to the static cryo-EM models in detail.
- **Required correction** Expand the discussion of how the present findings relate to existing cryo-EM structures of the thin filament, particularly regarding the position of the C-terminal region of cTnT in those structures.

## Risk / unsupported claims
- The claim that C-cTnT "regulates the energy barrier required to shift tropomyosin from the blocked to closed to open states" is presented as a conclusion but is not directly measured; the DSC data provide indirect support at best
- The claim that D270N "never reaches the expected activated position when myosin is bound" is based on comparison to WT in the same condition, but the "expected activated position" is not independently defined
- The statement that the flycasting mechanism is "like that of the C-terminal tail of cTnI" is an analogy that is not tested or quantitatively compared
- The claim that "increased interactions with cTnC" explain the reduced FWHM for K273E in the absence of calcium is based on MD interaction frequencies that cannot be validated from the supplied text
- The assertion that the activity assay results for K273E "could result in increased myosin attachment and thus increased activity or possibly increase the probability of myosin transitioning" presents two alternative mechanisms without discriminating between them
- The statement that the findings "may, in fact, provide new targets for clinical intervention" is speculative and not supported by any therapeutic evidence or rationale presented in the text