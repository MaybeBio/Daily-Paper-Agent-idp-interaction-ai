## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results and discussion, conclusions, supplementary information notice)
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by the presented evidence
- **Shared manuscript claim summary** The authors use coarse-grained simulations to show that the kinetic competition between condensate maturation (strengthening of inter-protein interactions) and droplet coalescence determines the shape of aged protein condensates, with fast maturation relative to coalescence producing aspherical solid-like droplets. Atomistic simulations of NUP-98 peptides suggest that beta-sheet formation strengthens interactions by nearly an order of magnitude, supporting the coarse-grained model assumptions.
- **Visible evidence base** Figures 1-4 (described in text), supplementary figures S1-S9 (referenced), simulation methodology descriptions in main text and supplementary sections
- **Missing materials affecting confidence** Supplementary Information content not provided; figure data values not available; simulation parameter tables not visible; detailed methods for coarse-grained model not accessible

## Reviewer
- **Overall assessment** This manuscript presents a computational study addressing an important question in the biology of biomolecular condensates: how the kinetic interplay between condensate maturation and coalescence determines the shape of aged condensates. The authors develop a tailored coarse-grained model that captures the transition from weak to strong inter-protein interactions, and they complement this with atomistic simulations of NUP-98 peptides. The central claim, that the relative timescales of maturation versus coalescence dictate whether condensates become spherical or aspherical, is plausible and potentially interesting. However, the manuscript has several significant weaknesses. The coarse-grained model is highly simplified, and the connection between the model parameters and real protein systems is not well established. The atomistic simulations, while supporting the idea that beta-sheet formation strengthens interactions, do not directly validate the coarse-grained model's assumptions. The quantitative claims about timescales are presented without sufficient error analysis or convergence assessment. The manuscript would benefit from a more careful treatment of the limitations of the model and a clearer articulation of what is robust versus what is model-dependent.

- **Who would be interested in the results, and why** Researchers studying the physical chemistry of biomolecular condensates, particularly those interested in condensate maturation, ageing, and the liquid-to-solid transition. The work may also be of interest to computational biophysicists developing coarse-grained models for phase-separating systems, and to cell biologists studying the pathological implications of condensate ageing in neurodegenerative diseases. The specific finding that the timing of strong interaction emergence relative to coalescence determines condensate shape could inform experimental studies of condensate morphology.

- **Major strengths**
  1. The manuscript addresses a timely and important question about the mechanisms underlying condensate ageing and shape changes.
  2. The combination of coarse-grained and atomistic simulations is a reasonable multi-scale approach.
  3. The central concept, that kinetic competition between maturation and coalescence determines condensate shape, is clearly articulated and mechanistically plausible.
  4. The authors test several variations of their model (different sequence patterning, different interaction potentials) and show qualitative consistency, which strengthens the robustness of their conclusions.
  5. The writing is generally clear and the figures appear to support the described results.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "the fast accumulation of strongly binding proteins during the nucleation and growth stages of condensate formation results in aspherical solid-like condensates" and that this is a general mechanism for condensate shape determination.
- **Evidence pointer** Figure 1B, Figure 3, Results section "Strengthening of inter-protein interactions can cause condensate maturation and thermal hysteresis"
- **Concern** The coarse-grained model uses a highly simplified representation of proteins as beads with only two interaction types (weak and strong). The transition from weak to strong interactions is implemented in a way that is not clearly described in the main text. The authors do not provide sufficient details about how the "maturation" process is modeled, what determines the timescale of this transition, and how this relates to real protein systems. The claim that this model captures the essential physics of condensate ageing requires more justification. Specifically, the model assumes that strong interactions emerge uniformly and irreversibly, but in reality, the formation of beta-sheets and other ordered structures is likely to be more complex, involving nucleation barriers and cooperative effects. The authors should provide a more detailed description of the model and justify why this simplified representation is adequate for capturing the phenomena of interest.
- **Why it matters** The central conclusion of the manuscript rests on the behavior of this coarse-grained model. If the model is not adequately justified or if its parameters are not connected to physical reality, the conclusions may not be generalizable to real protein condensates.
- **Resolution test** The authors should provide a more detailed description of the coarse-grained model, including the exact form of the interaction potentials, the dynamics of the weak-to-strong transition, and the mapping of model parameters to physical units. They should also discuss the limitations of the model and how their conclusions might depend on the specific choices made.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "formation of inter-peptide beta-sheets increases the strength of the interactions consistently with the loss of liquid-like condensate properties we observe at the coarse-grained level."
- **Evidence pointer** Figure 4, Results section "Comparing the strength of inter-protein interactions among disordered versus ordered peptides"
- **Concern** The atomistic simulations measure the binding strength between NUP-98 peptides in two states: fully disordered and constrained in a beta-sheet conformation. The authors find a roughly ten-fold difference in interaction strength. However, this comparison is not directly relevant to the coarse-grained model, which simulates the dynamics of condensate formation and maturation. The atomistic simulations are static equilibrium measurements and do not capture the kinetic process of beta-sheet formation or its effect on condensate dynamics. Furthermore, the authors constrain the peptides to the beta-sheet conformation, which may overestimate the interaction strength compared to a more realistic scenario where the peptides are partially ordered or fluctuating. The connection between these atomistic results and the coarse-grained model predictions is not clearly established.
- **Why it matters** The atomistic simulations are presented as supporting evidence for the coarse-grained model, but the link between the two is tenuous. If the atomistic results do not directly validate the model, the overall argument is weakened.
- **Resolution test** The authors should clarify how the atomistic simulation results relate to the coarse-grained model. They could perform simulations where the peptides are allowed to transition between disordered and ordered states, or they could use the atomistic results to parameterize the coarse-grained model more directly. At minimum, they should discuss the limitations of comparing static equilibrium measurements with dynamic simulations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The authors claim that their work "aids in elucidating fundamental molecular, kinetic, and thermodynamic mechanisms linking the rate of change in protein interaction strength to condensate shape and maturation during ageing."
- **Evidence pointer** Abstract, Conclusions
- **Concern** While the manuscript demonstrates that in their model, the relative timescales of maturation and coalescence determine condensate shape, the broader significance of this finding is not fully developed. The authors do not discuss how their results relate to specific experimental observations of condensate ageing, nor do they make quantitative predictions that could be tested experimentally. The model is so simplified that it is unclear whether the predicted behavior would be observed in real systems. The manuscript would be strengthened by a more explicit discussion of the experimental implications and testable predictions.
- **Why it matters** For a computational study to be impactful, it should either provide new mechanistic insights or make predictions that can guide experimental work. Currently, the manuscript does neither to a sufficient degree.
- **Resolution test** The authors should add a discussion section that explicitly connects their findings to experimental observations of condensate ageing, such as changes in viscosity, FRAP recovery, or morphology over time. They should also make specific, testable predictions about the conditions under which aspherical condensates would form.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "the observed behaviour of the diffusion coefficient signals a significant and continuous decay in the protein mobility, consistent with progressive condensate maturation."
- **Evidence pointer** Figure 1B, Results section "Strengthening of inter-protein interactions can cause condensate maturation and thermal hysteresis"
- **Concern** The authors measure the diffusion coefficient as a function of time and observe a decay for strong interaction strengths. However, it is not clear how the diffusion coefficient is calculated, what the statistical uncertainty is, and whether the observed decay is significant given the simulation length. The authors mention that they use "sufficiently large windows of time" but do not provide details on how these windows are chosen or how convergence is assessed. The lack of error bars or statistical analysis makes it difficult to evaluate the robustness of the reported results.
- **Why it matters** The claim of progressive maturation is based on the observed decay in diffusion coefficient. If this decay is not statistically significant or is an artifact of the simulation protocol, the conclusion would be weakened.
- **Resolution test** The authors should provide error bars or confidence intervals for the diffusion coefficient measurements, describe how convergence is assessed, and discuss the statistical significance of the observed decay.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction
- **Evidence pointer** Introduction, first paragraph
- **Issue** The introduction is dense and assumes significant background knowledge about condensates and phase separation. Terms like "LLPS," "FRAP," and "multivalent" are used without definition, which may limit accessibility for readers outside the immediate field.
- **Required correction** Consider adding brief definitions or explanations of key terms for nonspecialist readers.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods description
- **Evidence pointer** Results section "Strengthening of inter-protein interactions can cause condensate maturation and thermal hysteresis"
- **Issue** The description of the coarse-grained model is incomplete. The authors mention "section SIA of the Supplementary Information" but do not provide sufficient detail in the main text to understand the model without accessing the SI. Key parameters such as the number of simulations, simulation length, and system size are not stated in the main text.
- **Required correction** Provide a brief summary of the model and simulation parameters in the main text, with full details in the SI.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion of limitations
- **Evidence pointer** Conclusions
- **Issue** The manuscript does not adequately discuss the limitations of the coarse-grained model. For example, the model does not account for the sequence-specific effects that are known to be important in condensate formation, and the implicit solvent treatment may affect the dynamics.
- **Required correction** Add a paragraph discussing the limitations of the model and how they might affect the conclusions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Figure 3
- **Evidence pointer** Figure 3, Results section "Kinetic interplay between droplet maturation and coalescence"
- **Issue** The "border" curve in Figure 3 is described as being "derived from the intersection between the time-evolution diffusion coefficients and the kinetic threshold." However, the methodology for constructing this curve is not described in sufficient detail. It is unclear how the border is calculated and what its physical meaning is.
- **Required correction** Provide a more detailed description of how the border curve is constructed and what it represents.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Results section "Comparing the strength of inter-protein interactions among disordered versus ordered peptides"
- **Evidence pointer** Figure 4, Results section
- **Issue** The description of the atomistic simulations is brief and assumes familiarity with umbrella sampling and PMF calculations. The choice of the NUP-98 peptide system and the specific simulation conditions are not fully justified.
- **Required correction** Provide more context for the atomistic simulations, including why NUP-98 was chosen and what the limitations of the PMF calculations are.

## Risk / unsupported claims
- The claim that the coarse-grained model captures the essential physics of condensate ageing is not fully supported, as the model is highly simplified and the connection to real protein systems is not established.
- The claim that the atomistic simulations validate the coarse-grained model is not supported, as the two approaches measure different quantities and the relationship between them is not clearly articulated.
- The quantitative timescales reported (e.g., diffusion coefficients, coalescence times) are presented without error analysis or convergence assessment, making it difficult to evaluate their reliability.
- The claim that the observed behavior is "consistent with" experimental observations of condensate ageing is not supported by direct comparison with experimental data.
- The generalizability of the findings to real protein condensates, which have sequence-specific interactions and complex environments, is not established.