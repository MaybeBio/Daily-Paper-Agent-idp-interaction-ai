## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and figure legends.
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by presented evidence. Editorial or stylistic issues are noted only where they affect comprehension.
- **Shared manuscript claim summary** The authors combine coarse-grained lattice simulations and in vitro experiments to show that 1:1 mixtures of the prion-like low-complexity domains (PLCDs) of hnRNPA1 (A1-LCD) and FUS (FUS-LCD) phase separate more readily than either protein alone, due to complementary electrostatic interactions. Tie-line analysis of two-component phase diagrams is used to infer the relative contributions of homotypic versus heterotypic interactions. Simulations further reveal rules for how interaction strengths and chain lengths govern internal organization and interfacial properties of multicomponent condensates.
- **Visible evidence base** Main text figures 1–9, supplementary figures 1–6, supplementary tables 1–2, methods section, and in vitro phase separation assays with HPLC quantification and fluorescence microscopy.
- **Missing materials affecting confidence** Supplementary figures and tables are referenced but not provided in the submitted text. Raw simulation trajectories, force field parameter files, and full HPLC calibration data are not available. The exact simulation temperature-to-experimental temperature conversion is stated to be avoided, limiting quantitative comparison between simulations and experiments.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question: how mixtures of PLCDs, which co-exist in physiological condensates, collectively drive phase separation. The combination of lattice simulations and in vitro experiments is appropriate and the tie-line framework is a useful conceptual advance. The finding that heterotypic electrostatic interactions enhance co-phase separation of A1-LCD and FUS-LCD is plausible and supported by the presented data. However, several technical concerns limit the strength of the conclusions. The simulation model's treatment of electrostatics is acknowledged to be mean-field and does not capture charge patterning, which is a significant simplification given the claim that complementary electrostatics drive the effect. The quantitative agreement between simulation and experiment is not rigorously established, as the authors explicitly avoid converting simulation temperatures to experimental temperatures. The general rules for interfacial organization are derived from simplified homopolymer models, and their transferability to real PLCD sequences is asserted rather than demonstrated. The Li-j parameter is introduced but its statistical properties and sensitivity to simulation parameters are not fully characterized. Overall, the work is a valuable contribution, but the case for the general rules would be strengthened by additional validation.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, and intrinsically disordered proteins. The tie-line analysis framework will be of interest to experimentalists seeking to interpret multicomponent phase diagrams. The simulation predictions for interfacial organization and chain expansion may guide future experimental studies on condensate surface properties and multiphase architecture. The work also speaks to the broader question of how sequence-encoded interactions determine condensate composition and internal structure.

- **Major strengths**
  1. The combination of simulations and experiments to study mixtures of PLCDs is a strength, as most prior work has focused on single-component systems.
  2. The tie-line analysis provides a clear and interpretable framework for quantifying the relative contributions of homotypic versus heterotypic interactions.
  3. The study addresses a biologically relevant problem, as physiological condensates contain many different PLCDs.
  4. The use of a transferable coarse-grained model, previously parameterized on single-chain data, is a reasonable approach for generating testable predictions.
  5. The in vitro experiments using HPLC to measure two-component phase diagrams are technically rigorous and provide quantitative data.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of simulation model
- **Claim pointer** The authors claim that complementary electrostatic interactions between A1-LCD and FUS-LCD enhance phase separation of the mixture, and that this is captured by their simulation model.
- **Evidence pointer** Results section "Heterotyhpic interactions enhance the driving forces for phase separation of mixtures of A1-LCD and FUS-LCD", Figures 2d, 2e, 3c, 3d; Methods section "Monte Carlo simulations"
- **Concern** The simulation model treats electrostatics via a mean-field approach based on net charge per residue (NCPR), as stated in the Results and Methods. This approach cannot capture charge patterning, which is known to be critical for the phase behavior of PLCDs. The claim that complementary electrostatics drive the enhanced phase separation is therefore not directly tested by the simulations; the model may be capturing a generic effect of opposite net charges rather than a sequence-specific electrostatic complementarity. The authors acknowledge this limitation, but it undermines the mechanistic claim. Furthermore, the model was parameterized on single-chain data and may not accurately capture the balance of homotypic versus heterotypic interactions in mixtures.
- **Why it matters** The central mechanistic conclusion of the paper rests on the role of electrostatic interactions. If the model cannot faithfully represent these interactions, the conclusion is not established. The distinction between net-charge effects and sequence-specific charge patterning is important for understanding how PLCD mixtures behave in cells.
- **Resolution test** The authors should either (a) perform simulations with a model that explicitly includes charge-charge interactions with positional information, or (b) temper the mechanistic claim and present the electrostatic complementarity as a hypothesis consistent with, but not directly proven by, the simulations. Alternatively, they could design a variant of A1-LCD with the same NCPR but scrambled charge positions and show that the enhanced phase separation is lost, both in simulations and experiments.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative agreement between simulations and experiments
- **Claim pointer** The authors state that "Results from in vitro measurements are in accord with computational predictions" and use this agreement to support their conclusions.
- **Evidence pointer** Results section "Results from in vitro measurements are in accord with computational predictions", Figures 3b–3f, 5d–5f
- **Concern** The authors explicitly state that they avoid converting simulation temperatures to experimental temperatures because the conversion was not calibrated for mixtures. This means the comparison between simulations and experiments is only qualitative (e.g., concave vs. convex shape of the binodal). While qualitative agreement is encouraging, it does not provide a quantitative test of the model. The shapes of binodals can be influenced by many factors, and without a quantitative comparison, the claim of accord is weak. The differences in the extent of concavity between simulations and experiments are noted but not explained.
- **Why it matters** A central pillar of the paper is the synergy between simulations and experiments. If the agreement is only qualitative, the predictive power of the simulation model for mixtures is not established. This limits the confidence in the general rules derived from simulations.
- **Resolution test** The authors should calibrate the simulation temperature scale for the mixtures, perhaps by matching the experimental csat values for the pure components at multiple temperatures and then testing whether the mixture binodals are quantitatively predicted. If this is not feasible, the claims should be moderated to reflect the qualitative nature of the agreement.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generality of derived rules
- **Claim pointer** The authors claim to uncover "general rules for how interaction strengths and sequence lengths modulate conformational preferences of molecules at interfaces of condensates formed by mixtures of proteins."
- **Evidence pointer** Results section "Rules for internal and interfacial organization in mixtures that form co-localized condensates", Figures 8, 9
- **Concern** The general rules are derived from simulations of simplified homopolymers with uniform interaction strengths. Real PLCDs have sequence-specific patterns of stickers and spacers, and the interaction strengths are not uniform. The transferability of these rules to real protein sequences is asserted but not demonstrated. The authors do not test whether the rules hold for the specific sequences of A1-LCD and FUS-LCD beyond the single mixture studied.
- **Why it matters** The stated goal of the paper is to understand mixtures of real PLCDs. If the rules are only valid for idealized homopolymers, their relevance to biological systems is unclear.
- **Resolution test** The authors should test the rules on a set of diverse PLCD sequences with varying lengths and interaction strengths, perhaps by simulating a small library of sequences and checking whether the predicted interfacial behaviors are observed. Alternatively, they could map the homopolymer results back to the specific sequences of A1-LCD and FUS-LCD and show that the predictions hold.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical characterization of Li-j
- **Claim pointer** The Li-j parameter is used to quantify the relative likelihood of interactions between species i and j, and values greater or less than 1 are interpreted as non-random mixing.
- **Evidence pointer** Methods section "Crosslinking analysis", Figures 7c, 8
- **Concern** The Li-j parameter is defined and computed, but its statistical properties are not characterized. No error bars or confidence intervals are provided for Li-j values in the figures. It is unclear whether the deviations from 1 are statistically significant, particularly at higher temperatures where the two-phase region narrows. The sensitivity of Li-j to simulation length, system size, and the definition of a "contact" is not discussed.
- **Why it matters** The interpretation of internal organization relies on Li-j values being meaningfully different from 1. Without statistical characterization, the reader cannot assess the robustness of the conclusions.
- **Resolution test** The authors should provide error bars or confidence intervals for Li-j, perhaps from bootstrapping or multiple independent simulations. They should also discuss the sensitivity of Li-j to the contact definition and simulation parameters.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure presentation
- **Affected element** Figure 2b
- **Evidence pointer** Figure 2b
- **Issue** The binodals for different mixture ratios are plotted in the same panel, but the legend only indicates the percentage of FUS-LCD. It is difficult to distinguish the curves for intermediate ratios.
- **Required correction** Consider using different line styles or colors that are more easily distinguishable, or plot the binodals in separate panels.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Methods section "Monte Carlo simulations"
- **Evidence pointer** Methods section "Monte Carlo simulations"
- **Issue** The methods state that the model is the same as that described by Farag et al., but the key parameters for the mixture simulations (e.g., how cross-species interaction strengths are assigned) are not fully specified. The reader is referred to prior work, which may not be convenient.
- **Required correction** Provide a brief summary of the model parameters, especially the rules for combining interaction strengths for heterotypic pairs, so that the simulations are reproducible without consulting the prior publication.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of salt dependence
- **Affected element** Results section "Results from in vitro measurements are in accord with computational predictions", Figure 3f
- **Evidence pointer** Figure 3f
- **Issue** The salt dependence of the mixture binodal is shown, but the interpretation is brief. The authors state that increasing salt weakens both homotypic and heterotypic electrostatic interactions, but the net effect on the binodal shape is not discussed in detail.
- **Required correction** Expand the discussion of the salt dependence to clarify how the data support the proposed mechanism of complementary electrostatics.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** Throughout
- **Issue** The term "co-phase separation" is used, but not explicitly defined. It is clear from context, but a brief definition would help readers unfamiliar with the term.
- **Required correction** Define "co-phase separation" at first use.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Consistency of simulation and experimental conditions
- **Affected element** Results sections, Figures 2 and 3
- **Evidence pointer** Figures 2 and 3
- **Issue** The simulation and experimental conditions are not identical (e.g., temperature, salt concentration, protein concentration ranges). The authors note this, but a more explicit statement of the differences and their potential impact on the comparison would be helpful.
- **Required correction** Add a sentence in the Results or Discussion explicitly listing the differences in conditions and why the qualitative comparison is still valid.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Accessibility of supplementary material
- **Affected element** Supplementary figures and tables
- **Evidence pointer** Supplementary figures 1–6, tables 1–2
- **Issue** The supplementary material is referenced but not provided in the submitted text. This makes it difficult to fully evaluate the methods and results.
- **Required correction** Ensure the supplementary material is available to reviewers, or provide key supplementary data in the main text.

## Risk / unsupported claims
- The claim that complementary electrostatic interactions are the primary driver of enhanced phase separation in 1:1 mixtures is not fully supported, as the simulation model uses a mean-field treatment of electrostatics that cannot capture charge patterning. The experimental data are consistent with this hypothesis, but alternative explanations (e.g., differences in solvation, aromatic interactions) are not ruled out.
- The claim that the derived rules for interfacial organization are "general" is not supported, as they are based on simplified homopolymer models and tested on only one real PLCD pair.
- The quantitative agreement between simulations and experiments is not established, as the authors avoid converting simulation temperatures to experimental temperatures. The comparison is qualitative only.
- The statistical significance of the Li-j values is not assessed, so the claim of non-random internal organization is not rigorously supported.
- The statement that "the spatial organization of PLCDs within condensates is governed by relative strengths of homotypic versus heterotypic interactions" is a reasonable interpretation of the simulations, but it is not directly tested experimentally.