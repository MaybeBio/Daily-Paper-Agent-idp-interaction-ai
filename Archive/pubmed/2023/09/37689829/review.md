## Review setup
- **Input scope** Full manuscript text including abstract, main text, methods, and figure captions. Supplementary information referenced but not provided.
- **Assessment boundary** Assessment is limited to the content presented in the supplied manuscript text. Claims are evaluated on the basis of internal consistency, methodological soundness, and alignment with the presented evidence. No external literature verification was performed beyond what is cited in the manuscript.
- **Shared manuscript claim summary** The authors use coarse-grained dual-basin structure-based simulations of the GA/GB protein fold switch to show that macromolecular crowding shifts the population balance toward the GB fold, and that this effect is dominated by the intrinsically disordered terminal regions present only in the GA fold. They further show that the unfolded state changes character across the switch and that single-fold models do not capture the crowding response of the fold switcher.
- **Visible evidence base** Main text figures 1-5, methods section, and equations 1-5. Supplementary figures S1-S4 are referenced but not available for review.
- **Missing materials affecting confidence** Supplementary Information (including model details, Supplementary Figs. S1-S4), simulation parameter files, force field details, and convergence tests. The Peer Review File is also not available.

## Reviewer

- **Overall assessment** This manuscript presents a computational study of crowding effects on a protein fold switch using a coarse-grained dual-basin model. The work addresses a timely and interesting question, and the finding that disordered terminal regions dominate the crowding response is potentially significant. However, the study relies entirely on a highly simplified coarse-grained model, and the manuscript does not provide sufficient evidence to establish that the observed effects are robust to model choices or that they would persist in more realistic representations. The central claim that disordered regions drive the crowding-induced population shift is supported by the simulation data presented, but the generality of this conclusion is not established. The manuscript is clearly written and the methodology is described in adequate detail, though key validation steps are missing.

- **Who would be interested in the results, and why** Researchers studying protein folding, fold switching, metamorphic proteins, and macromolecular crowding effects on protein stability and function. The work may also be of interest to computational biophysicists developing coarse-grained models for crowded environments, and to experimentalists studying fold-switching proteins in cellular contexts who are seeking mechanistic hypotheses for how crowding might modulate conformational equilibria.

- **Major strengths**
  1. The study addresses a relatively unexplored question: how crowding affects proteins that switch between distinct folds, rather than the more commonly studied single-fold proteins.
  2. The dual-basin structure-based model is a reasonable and established approach for studying fold switching, and the tuning of contact strengths to mimic mutational pathways is a clever strategy.
  3. The computational experiment of turning off crowder interactions with the terminal regions is a clean and informative test of the mechanistic hypothesis.
  4. The comparison with scaled particle theory and generalized fundamental measure theory provides a useful theoretical framework for interpreting the simulation results.
  5. The manuscript is generally well written and the figures are clear.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the dual-basin model "permits us to mimic the progression of mutations along a pathway from one fold to the other by tuning the relative interaction strengths of residue-residue contacts in the GA and GB folds."
- **Evidence pointer** Results section "Mimicking the mutational pathway between the GA and GB folds", Figure 1c-f
- **Concern** The mapping between the contact strength parameter κB and actual mutations is not validated. The authors state that the sharp transition around κB ≈ κ* is "reminiscent of experiments" but do not provide any quantitative comparison to experimental data on GA/GB variants. It is unclear whether the range of κB values explored corresponds to realistic mutational effects, and whether the specific value κB = 0.92 has any physical correspondence to actual sequences. Without such validation, the interpretation of κB as a mutational coordinate remains speculative.
- **Why it matters** The central premise of the study is that the model at κB = κ* represents a sequence at the GA/GB border. If this mapping is not established, the relevance of the crowding results to real fold-switching proteins is unclear.
- **Resolution test** The authors should provide a quantitative comparison of their model predictions to experimental data on GA/GB variants, for example by showing that the model reproduces known stability differences or mutational effects. Alternatively, they should clearly state the limitations of the κB mapping and temper their claims accordingly.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the effect of steric repulsions between crowders and protein is to favor GB over GA" and that this is due to the intrinsically disordered terminal regions in GA.
- **Evidence pointer** Results section "Macromolecular crowding effects on the GA/GB fold switch", Figures 2b, 3a
- **Concern** The simulation model uses a single bead per amino acid with a fixed bead radius. The intrinsically disordered regions in GA are modeled with the same bead size and interaction parameters as ordered regions. It is not clear whether the observed effect is a genuine property of disordered regions or an artifact of the coarse-grained representation. Specifically, the excluded volume of a disordered region in a coarse-grained model may be overestimated because the model cannot capture the conformational heterogeneity of real disordered regions. The authors do not discuss this limitation or test its impact.
- **Why it matters** The central mechanistic claim of the paper is that disordered regions drive the crowding response. If this is an artifact of the model resolution, the conclusion would not hold in more realistic representations.
- **Resolution test** The authors should test the sensitivity of their results to the bead size and to the treatment of disordered regions, for example by using different bead radii for disordered residues or by comparing with a model that includes explicit backbone atoms. Alternatively, they should discuss this limitation explicitly and temper their claims.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the generally good agreement obtained for GFMT indicates, in particular, that accounting for fluctuations in chain size, which are absent in SPT, is necessary to describe the observed ϕc-dependence of ΔFswitch."
- **Evidence pointer** Results section "Macromolecular crowding effects on the GA/GB fold switch", Figure 2c
- **Concern** The GFMT calculations are performed on only 200 conformations per fold, and the error bars shown in Figure 2c represent standard deviations over this set. It is not clear whether 200 conformations are sufficient to converge the GFMT estimates, particularly for the unfolded state which is highly heterogeneous. Additionally, the GFMT results are compared to simulation data at only a limited number of ϕc values, and the agreement is described qualitatively as "generally good" without a quantitative measure of fit quality.
- **Why it matters** The claim that GFMT captures the crowding effect better than SPT is a key part of the theoretical analysis. If the GFMT estimates are not converged, this conclusion is not reliable.
- **Resolution test** The authors should perform a convergence test for the GFMT calculations, showing that the results are stable with respect to the number of conformations used. They should also provide a quantitative measure of the agreement between GFMT and simulation data.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors state that "crowding effects, if indeed providing an overall stabilization, might therefore alleviate the partial loss of stability suffered by bridge sequences in evolutionary fold-switch transitions."
- **Evidence pointer** Discussion section
- **Concern** This statement is speculative and goes beyond the simulation results. The simulations show crowding stabilizes the GB fold relative to GA in the model system, but the connection to evolutionary fold-switch transitions is not developed or supported by any data. The authors do not discuss how the magnitude of the crowding effect compares to the stability losses observed in real bridge sequences, nor do they consider other factors that might be relevant in an evolutionary context.
- **Why it matters** This claim is presented as a potential implication of the work, but without further analysis it remains an unsupported speculation that could be misleading to readers.
- **Resolution test** The authors should either remove this speculation or provide a more careful discussion that acknowledges the limitations of extrapolating from their model to evolutionary processes.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The abstract states "Macromolecular crowding effects on globular proteins, which usually adopt a single stable fold, have been widely studied. However, little is known about crowding effects on fold-switching proteins." This framing is somewhat misleading, as there is a growing body of work on crowding effects on intrinsically disordered proteins and on proteins with multiple conformations.
- **Required correction** The authors should soften this claim or provide a more nuanced framing that acknowledges existing work on crowding effects on conformational equilibria.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, simulation details
- **Evidence pointer** Methods section "Simulation and analysis details"
- **Issue** The manuscript states that "5-10 independent runs of (4-5) x 10^9 time steps each were carried out" but does not report the total simulation time in physical units or the number of independent samples used for the error estimates. This makes it difficult to assess the statistical quality of the results.
- **Required correction** The authors should report the total simulation time in physical units and provide more detail on how the statistical uncertainties were estimated.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 2c
- **Evidence pointer** Figure 2c caption
- **Issue** The caption states that "Green rhombuses are average ΔFswitch values calculated using GFMT (Eq. (5)) for a representative set of GA and GB conformations taken from simulations, and error bars indicate standard deviations over this set." It is not clear what "representative" means in this context or how the conformations were selected.
- **Required correction** The authors should clarify how the conformations were selected for the GFMT calculations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Discussion section
- **Evidence pointer** Discussion, first paragraph
- **Issue** The discussion of the unfolded state is somewhat brief and could be expanded to better connect the findings to the broader literature on unfolded states and crowding.
- **Required correction** The authors should consider expanding this section to provide more context and interpretation.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, excluded volume crowders
- **Evidence pointer** Methods section "Excluded volume crowders"
- **Issue** The crowder size (Rc = 12.5 Å) is relatively small compared to typical crowding agents used in experiments (e.g., Ficoll, PEG, BSA). The authors do not discuss how the choice of crowder size affects the results or whether the conclusions would hold for larger crowders.
- **Required correction** The authors should discuss the choice of crowder size and its potential impact on the generality of their conclusions.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Introduction
- **Evidence pointer** Introduction, first paragraph
- **Issue** The introduction cites references 1-4 for fold switching but does not provide a clear definition of what constitutes a fold switch, which may be confusing for readers unfamiliar with the field.
- **Required correction** The authors should provide a brief definition or description of fold switching early in the introduction.

## Risk / unsupported claims
- The claim that the model "mimics the progression of mutations along a pathway" is not quantitatively validated against experimental data.
- The claim that disordered terminal regions are the dominant factor in the crowding response is based on a coarse-grained model and may not hold at higher resolution.
- The speculation that crowding might alleviate stability losses in evolutionary fold-switch transitions is not supported by direct evidence.
- The claim that GFMT provides a better description than SPT is based on a qualitative comparison with limited data.
- The generality of the findings beyond the specific GA/GB system is not established.
- The relevance of the model's crowder size to physiological crowding conditions is not discussed.