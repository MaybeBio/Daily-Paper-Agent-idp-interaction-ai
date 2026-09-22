## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusions, methods summary) without supplementary information or figures beyond in-text descriptions
- **Assessment boundary** Scientific claims, methodological soundness, evidence quality, and alignment with stated conclusions based solely on the provided manuscript text
- **Shared manuscript claim summary** The authors present a computational pipeline using coarse-grained molecular dynamics simulations to screen small peptides that can decelerate the ageing of biomolecular condensates driven by cross-β-sheet formation. They report that peptides with a specific balance of aromatic and charged residues can slow ageing by over an order of magnitude in TDP-43 and FUS low-complexity domain condensates, via a mechanism involving condensate density reduction and selective interactions with aggregation-prone regions.
- **Visible evidence base** Main text figures 1–4 as described in the manuscript, simulation data from CALVADOS2 coarse-grained model, ageing kinetics fits, contact frequency maps, phase diagram calculations, statistical tests (Mann-Whitney U)
- **Missing materials affecting confidence** Supplementary Information (Sections SI–SIX, SVII, SVIII), all figure images, simulation parameter details, force field validation data, PMF calculation details, full Methods section, reporting summary

## Reviewer
- **Overall assessment** This manuscript presents a computationally driven study with a clear practical aim: identifying peptide sequences that can slow condensate ageing. The work is timely and addresses a problem of significant biomedical relevance. The authors combine equilibrium and non-equilibrium simulations with a residue-resolution model to screen peptide candidates and propose a mechanistic explanation for their effectiveness. The central claim, that peptides with balanced aromatic and charged content can decelerate ageing by over an order of magnitude, is potentially important. However, the evidence as presented in the main text is largely simulation-based with limited experimental validation, and several key methodological details are relegated to the Supplementary Information, which was not available for assessment. The mechanistic interpretation, while plausible, rests on correlative observations (density reduction, contact frequency changes) rather than direct causal demonstration. The statistical treatment appears appropriate but the number of independent simulations per condition is not stated in the main text. Overall, the study is well conceived and the results are likely to be of interest to the condensate community, but the strength of the conclusions cannot be fully evaluated without the supplementary material and additional validation.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, and ageing/aggregation phenomena in neurodegeneration would find this work directly relevant. The computational screening approach could be of interest to those developing therapeutic strategies targeting condensate maturation. The mechanistic insights into how peptide charge and aromatic content modulate condensate properties may inform future experimental designs. The work also speaks to the broader community interested in sequence-encoded determinants of condensate material properties.

- **Major strengths**
  1. The study addresses a clinically relevant problem (condensate ageing in neurodegeneration) with a practical computational screening strategy.
  2. The use of a residue-resolution model allows systematic exploration of sequence space that would be impractical experimentally.
  3. The authors consider both equilibrium (phase diagram) and non-equilibrium (ageing kinetics) properties, providing a more complete picture than many similar studies.
  4. The inclusion of two different protein systems (FUS and TDP-43) strengthens the generality of the conclusions.
  5. The mechanistic analysis using contact frequency maps provides molecular-level insight into how peptides interact with aggregation-prone regions.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that the identified peptides "substantially decelerate ageing over an order of magnitude" and that this is achieved through a specific mechanism involving condensate density reduction and selective interactions with LARKS regions.
- **Evidence point** Figures 3a–d, 4a–f; Section II C
- **Concern** The central quantitative claim of "over an order of magnitude" deceleration is presented without clear reporting of the statistical significance, effect sizes, or confidence intervals in the main text. The box plots in Figures 3b and 3d show distributions, but the number of independent simulations, the variability between replicates, and the specific p-values from the Mann-Whitney U tests are not reported in the main text. Furthermore, the mechanistic claim that density reduction is the causal driver of decelerated ageing is inferred from correlation (density changes and contact frequency changes co-occur with slower ageing) rather than demonstrated through perturbation experiments or causal analysis.
- **Why it matters** Without clear statistical reporting and causal evidence, the reader cannot assess whether the observed deceleration is robust and whether the proposed mechanism is correct. The "order of magnitude" claim is the headline result and must be rigorously supported.
- **Resolution test** Report the number of independent simulations, effect sizes with confidence intervals, and exact p-values for all comparisons. Provide additional simulations where density is held constant (e.g., via osmotic pressure coupling) or where peptide-protein interactions are disrupted to test whether the proposed mechanism is causal.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Model validation
- **Claim pointer** The manuscript states that the CALVADOS2 model "accurately predicts the conformational properties and propensities to undergo LLPS for diverse sequences and solution conditions" and that it "provides fair predictions for condensate material properties."
- **Evidence point** Introduction, Section II A; references 78, 90, 103
- **Concern** The ageing simulation algorithm, which converts disordered LARKS into cross-β-sheet structures based on PMF calculations, is central to the study's conclusions. However, the validation of this algorithm is not presented in the main text, and the PMF calculations are from previous work (references 96, 99). The manuscript does not demonstrate that the ageing kinetics predicted by this model quantitatively match experimental observations for the pure protein systems, nor does it show that the model correctly captures the effect of peptide addition. Without such validation, the predicted deceleration factors may be artifacts of the model rather than real physical effects.
- **Why it matters** The entire study rests on the predictive power of the simulation model. If the ageing algorithm has not been validated against experimental data, the quantitative claims (e.g., order of magnitude deceleration) cannot be trusted.
- **Resolution test** Provide validation of the ageing algorithm against experimental ageing kinetics for FUS and TDP-43 condensates, or at minimum against experimental data for related systems. If such validation is not possible, temper the quantitative claims and present the results as qualitative predictions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Experimental validation
- **Claim pointer** The manuscript proposes that the identified peptides could serve as "regulators of pathological liquid-to-solid transitions" and suggests therapeutic relevance.
- **Evidence point** Conclusions section
- **Concern** The study is entirely computational. While the authors acknowledge this, the translational implications suggested in the conclusions (e.g., "guiding future therapeutic designs") require at least some experimental validation of the key predictions. For example, testing one or two of the most effective peptide sequences in vitro with purified FUS or TDP-43 LCDs would substantially strengthen the claims. Without any experimental confirmation, the practical relevance of the findings remains speculative.
- **Why it matters** Computational predictions in the condensate field have often not translated to experimental systems due to unmodeled complexities (e.g., post-translational modifications, chaperones, cellular context). The therapeutic implications are premature without experimental support.
- **Resolution test** Include at least one experimental validation experiment (e.g., turbidity assays, FRAP, or electron microscopy) demonstrating that a top-performing peptide indeed slows condensate hardening in vitro.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The manuscript states that the findings "provide a promising proof-of-concept for further investigation of potential sequences as modulators of condensate ageing" and implies that the design principles are general.
- **Evidence point** Conclusions section
- **Concern** The study is limited to two protein systems (FUS and TDP-43) and a relatively small set of peptide sequences (15 for FUS, fewer for TDP-43). The authors do not test whether the design principles (aromatic content, charge balance) generalize to other condensate-forming proteins with different sequence features, such as those with prion-like domains, RGG repeats, or different net charges. The claim of generalizability is therefore not supported by the data presented.
- **Why it matters** If the design principles are not general, the practical utility of the screening approach is limited. The condensate field is diverse, and a strategy that works for FUS and TDP-43 may not work for other systems.
- **Resolution test** Test the most promising peptide designs on at least one additional condensate-forming protein system with distinct sequence features, or clearly limit the claims to the systems studied.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1d description
- **Evidence point** Section II A, Figure 1d
- **Issue** The description of the ageing kinetics fits in Figure 1d states that "dashed lines represent fits to the data according to a secondary nucleation dominated mechanism" but does not explain what the fit parameters are or how the quality of the fits was assessed.
- **Required correction** Provide the fit parameters (e.g., rate constants, lag times) and goodness-of-fit metrics (e.g., R², AIC) either in the main text or in the figure caption.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Simulation details
- **Evidence point** Methods section
- **Concern** The Methods section states that "full methodological details can be found in the Supplementary Material," but the main text does not provide key simulation parameters such as system size, simulation length, number of replicates, temperature coupling scheme, or equilibration protocol.
- **Required correction** Include at least the essential simulation parameters in the main text Methods section, or provide a summary table of key parameters.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion of peptide charge effects
- **Evidence point** Section II B, Figure 2b
- **Concern** The manuscript discusses the role of peptide charge in modulating condensate stability but does not clearly separate the effects of charge density, charge sign, and charge distribution along the peptide sequence. The comparison between peptides with different charge patterns is not systematically analyzed.
- **Required correction** Clarify whether the observed effects are primarily due to net charge, charge density, or charge patterning, and discuss any confounding factors.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction and Discussion
- **Evidence point** Introduction, Section II D
- **Concern** The manuscript cites relevant literature on condensate ageing and peptide modulators, but the discussion of alternative mechanisms (e.g., molecular chaperones, post-translational modifications, RNA-mediated effects) is limited. The authors could better position their findings within the broader context of condensate regulation strategies.
- **Required correction** Add a brief discussion of how the proposed peptide-based approach compares to other strategies for modulating condensate ageing, such as small molecule inhibitors, chaperone overexpression, or RNA-based approaches.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Mann-Whitney U tests
- **Evidence point** Section II C, Section SVIII
- **Concern** The manuscript mentions Mann-Whitney U tests but does not report the test statistics, p-values, or the number of samples in the main text. The reader cannot assess the robustness of the statistical claims.
- **Required correction** Report the test statistics and p-values for all comparisons in the main text or in a supplementary table referenced in the main text.

## Risk / unsupported claims
1. The claim that peptides "decelerate ageing over an order of magnitude" is not fully supported by the statistical reporting visible in the main text (effect sizes, confidence intervals, and exact p-values are not provided).
2. The mechanistic claim that density reduction is the causal driver of decelerated ageing is inferred from correlation and is not directly tested.
3. The generalizability of the design principles to other condensate-forming proteins is asserted but not demonstrated.
4. The therapeutic relevance suggested in the conclusions is speculative without experimental validation.
5. The validation of the ageing simulation algorithm against experimental data is not presented in the main text and cannot be assessed from the provided material.
6. The claim that the CALVADOS2 model "accurately predicts" condensate properties is based on prior work and is not re-validated in this study for the specific systems and conditions used.