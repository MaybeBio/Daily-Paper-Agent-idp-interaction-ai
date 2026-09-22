## Review setup
- **Input scope** Full manuscript text (main text, methods, and references to supplementary material)
- **Assessment boundary** Scientific claims, methodology, and interpretation as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors use coarse-grained (CG) simulations to study the fuzzy complex formed between the intrinsically disordered proteins (IDPs) ProTα and H1. They generate charge-swapped and charge-shuffled variants and report that affinity is modulated by both enthalpy and entropy, with configurational entropy stabilizing complex formation and counterion release providing a large additional entropic contribution. They propose an enthalpy–entropy reinforcement mechanism for high-affinity fuzzy complexes.
- **Visible evidence base** Main text figures (Figs. 1–5), Table 1, and references to SI Appendix figures and methods
- **Missing materials affecting confidence** The SI Appendix is not provided; simulation parameters, force field details, and convergence analyses are only partially described; experimental validation data are not included; the counterion entropy estimate is presented as a crude calculation without full derivation

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question in the biophysics of intrinsically disordered proteins: what thermodynamic forces govern the high-affinity binding of oppositely charged IDPs in fuzzy complexes. The authors present a systematic computational study using a CG model, with a well-designed set of sequence variants that separate the effects of net charge and charge patterning. The central claim, that configurational entropy can stabilize fuzzy complex formation and that enthalpy–entropy reinforcement (rather than compensation) operates in these systems, is interesting and potentially significant. However, the strength of the conclusions depends heavily on the accuracy of the CG model and on the entropy calculations, and several aspects of the methodology and analysis are not fully transparent from the provided material. The counterion entropy estimate is particularly concerning, as it is presented as a dominant contribution but is derived from a crude approximation. The manuscript is clearly written and will appeal to a broad readership in protein biophysics and computational biology, but the evidence as presented does not fully establish the mechanistic claims.

- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, protein–protein interactions, and the thermodynamics of biomolecular association will find this work relevant. The study also speaks to the growing community interested in the design of synthetic IDP-based materials and condensates, as it provides sequence-level rules for tuning binding affinity. The methodological approach, combining CG simulations with entropy decomposition, will be of interest to computational biophysicists.

- **Major strengths** The study addresses a fundamental and under-explored question: how do disordered proteins achieve high-affinity binding without stable folded interfaces? The design of charge-swapped and charge-shuffled variants is elegant and allows a clean separation of net charge and patterning effects. The comparison with ordered protein complexes (barnase–barstar, DNase2–Im2) provides a useful benchmark. The finding that configurational entropy can be favorable for IDP complex formation, and that this is modulated by sequence, is novel and potentially important. The manuscript is generally well written and the figures appear informative.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the CG model accurately reproduces experimental dissociation constants for the H1–ProTα complex and for the ordered complexes, and that the simulated KD values are "consistent with the experimental KD values, even at several salt concentrations."
- **Evidence pointer** Fig. 1C and associated text
- **Concern** The validation of the CG model against experimental KD values is central to the credibility of all subsequent thermodynamic analyses. However, the description of the model and the fitting procedure is incomplete. It is not clear whether the model parameters (e.g., Lennard-Jones contact strengths, electrostatic treatment) were adjusted to reproduce the experimental KD values, which would compromise the predictive power of the model. The manuscript states that "the experimental value of the salt-dependent KD of H1–ProTα is in very good agreement with that simulated by our model," but the level of agreement across the full salt range is not quantified. Furthermore, the KD values for the ordered complexes are reported at specific salt concentrations, and it is unclear whether the model was benchmarked at those conditions or extrapolated.
- **Why it matters** If the model was tuned to match experimental binding affinities, then the subsequent decomposition into enthalpy and entropy contributions may be biased, and the claim of a general mechanism for fuzzy complex stabilization would be weakened. The reader cannot assess the robustness of the model without a clear statement of parameterization and validation procedures.
- **Resolution test** Provide a detailed description of the model parameterization, including whether any parameters were fitted to experimental binding data. Show a quantitative comparison between simulated and experimental KD values across the full range of salt concentrations studied, including error estimates. If parameters were fitted, demonstrate that the enthalpy–entropy decomposition is robust to reasonable variations in those parameters.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "the entropy from counterion release varies significantly between the variants, and it mostly depends on the net charge and less on κ" and that the total counterion entropy TΔSCI is "between 40 and 80 kcal/mol," indicating that "counterions may have a significant effect and that, overall, entropy may govern the stability of the fuzzy complex."
- **Evidence pointer** Results and Discussion, section "Biophysical Driving Forces for the Formation of the Fuzzy Complex: Enthalpy versus Entropy"
- **Concern** The counterion entropy is estimated using a crude analytical formula, with the assumption that all counterions are released upon complexation. This is a strong assumption that is not justified. The degree of counterion condensation α is measured from simulations with explicit counterions, but the details of those simulations (e.g., how counterions were modeled, whether they were present in the binding simulations) are not provided. The formula itself is presented without derivation, and the range of 40–80 kcal/mol is large. Given that this contribution is claimed to potentially dominate the thermodynamics, the lack of rigor in this estimate is a serious concern.
- **Why it matters** The central conclusion that entropy may govern the stability of fuzzy complexes rests in part on this counterion entropy estimate. If the estimate is unreliable, the conclusion is not supported. The authors themselves acknowledge the estimate is crude, but they still use it to argue for a dominant entropic role.
- **Resolution test** Provide a more rigorous treatment of counterion entropy, either through explicit simulation of counterion distributions in bound and unbound states, or through a well-justified analytical model. Justify the assumption of complete counterion release. Provide error bars on the counterion entropy estimate and discuss how the conclusions would change if the estimate were reduced.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that "enthalpy–entropy reinforcement" is observed for the fuzzy complex, and that this is distinct from the more commonly observed enthalpy–entropy compensation.
- **Evidence pointer** Fig. 3A and associated text
- **Concern** The observation of a linear correlation between ΔE and −TΔSCon (Fig. 3A) is interpreted as evidence for enthalpy–entropy reinforcement. However, the correlation is based on a limited number of data points (52 complexes, but with only five net-charge variants and a small number of patterning variants per net charge). The statistical significance of the correlation is not reported. Moreover, the interpretation of a positive correlation between ΔE and −TΔSCon as "reinforcement" is not standard; typically, reinforcement would imply that both terms favor binding (i.e., ΔE < 0 and −TΔS < 0), which is indeed the case here, but the correlation across variants may simply reflect the dominant effect of net charge on both quantities. The authors do not provide a mechanistic explanation for why reinforcement should occur, beyond stating that it originates from the unbound state.
- **Why it matters** The claim of enthalpy–entropy reinforcement is a key conceptual contribution of the paper. If the correlation is not robust or the interpretation is not well supported, the novelty of the work is diminished.
- **Resolution test** Report the correlation coefficient and its statistical significance. Provide a more detailed mechanistic explanation for the reinforcement, perhaps by decomposing the entropy change into contributions from different degrees of freedom. Discuss whether the correlation holds when net charge is held constant and only κ is varied.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "the fuzzy complex H1–ProTα spans an almost 20-nm distance between the COMs of the two proteins," and that this long-range attraction is due to electrostatic interactions.
- **Evidence pointer** Fig. 1B and associated text
- **Concern** The PMF profiles show a very long-range attraction for the H1–ProTα complex, extending to 20 nm. This is unusual and may be an artifact of the CG model or of the simulation protocol. The manuscript does not discuss whether such long-range attraction is physically realistic, given that Debye screening at 200 mM salt would be expected to reduce electrostatic interactions to a few nanometers. The authors do not address the possibility that the long-range attraction is due to finite-size effects or to the absence of proper screening in the model.
- **Why it matters** If the long-range attraction is an artifact, then the PMF profiles and the derived KD values may be incorrect, and the comparison with ordered complexes may be misleading.
- **Resolution test** Provide a discussion of the expected range of electrostatic interactions at the simulated salt concentrations. Show that the PMF profiles converge with respect to system size and simulation time. If possible, compare with a model that includes explicit screening or a more accurate treatment of electrostatics.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction and Significance statement
- **Evidence pointer** Significance section
- **Issue** The Significance statement is somewhat technical and does not fully explain to a general reader why the question of how disordered proteins achieve high-affinity binding is important. The term "fuzzy complex" is used without a clear definition.
- **Required correction** Briefly define "fuzzy complex" and explain in one or two sentences why understanding the thermodynamics of such complexes is relevant to biology or medicine.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, "Studied Systems"
- **Evidence pointer** Table 1 and associated text
- **Issue** The description of how the charge-swapped and charge-shuffled variants were generated is incomplete. It is not clear how the κ values were calculated or how the sequences were designed to achieve the desired κ values while maintaining the same net charge.
- **Required correction** Provide a more detailed description of the sequence design procedure, including the algorithm used to generate variants with specified κ values.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, "Model"
- **Evidence pointer** Equation for potential energy
- **Issue** The potential energy function includes a Lennard-Jones term for "native/interface" contacts and a repulsive term for "non-contacts." It is not clear how the native contacts were defined for the disordered H1–ProTα system, given that there is no folded structure. The manuscript states that for H1–ProTα, the short-range interaction was applied only to the folded domain of histone, but the details of how this was implemented are not provided.
- **Required correction** Clarify how native contacts were defined for the disordered system and how the folded domain of histone was identified in the CG model.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, "Steered MD, umbrella sampling, and conformational entropy"
- **Evidence pointer** Text describing umbrella sampling
- **Issue** The manuscript states that 200 umbrella windows were used for H1–ProTα and 370 for the ordered complexes, but it does not specify the spacing between windows or the total simulation time per window. The convergence of the PMF is mentioned as being confirmed in the SI, but the criteria for convergence are not stated.
- **Required correction** Provide details on the umbrella sampling setup, including window spacing, simulation time per window, and the convergence criteria used.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interdisciplinary readership
- **Affected element** Discussion of counterion condensation
- **Evidence pointer** Section "Biophysical Driving Forces for the Formation of the Fuzzy Complex: Enthalpy versus Entropy"
- **Issue** The concept of counterion condensation and its relation to polyelectrolyte theory is introduced without sufficient background for readers who are not experts in polymer physics.
- **Required correction** Provide a brief explanation of counterion condensation and why it is relevant to the thermodynamics of charged IDP complexes.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Fig. 2C and associated text
- **Evidence pointer** Fig. 2C
- **Issue** The claim that "modifying κ changes KD by about 10 orders of magnitude" is based on a visual inspection of the figure, but the range of KD values for a given net charge and different κ values is not quantified. The figure appears to show a wide spread, but the exact values are not reported.
- **Required correction** Report the range of KD values for each net charge variant and the corresponding κ values in a table or in the text.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Conclusions
- **Evidence pointer** Conclusions section
- **Issue** The final sentence of the Conclusions states that "these features of the charged residues may serve to determine not only binding affinity, but also specificity." This claim is not directly supported by the data presented, as the study does not measure specificity.
- **Required correction** Soften this claim or provide a brief explanation of how the observed thermodynamic trends might relate to specificity, based on existing literature.

## Risk / unsupported claims
- The claim that counterion entropy dominates the thermodynamics of the fuzzy complex is based on a crude estimate and is not fully supported by the presented evidence.
- The claim that the CG model accurately reproduces experimental KD values is not fully verifiable without a detailed description of the parameterization procedure.
- The claim that enthalpy–entropy reinforcement is a general mechanism for fuzzy complex stabilization is based on a limited set of sequence variants and may not be generalizable.
- The long-range attraction observed in the PMF profiles (extending to 20 nm) is not physically justified and may be an artifact of the model.
- The claim that the results have implications for specificity is speculative and not directly tested.