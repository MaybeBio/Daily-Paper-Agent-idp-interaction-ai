## Review setup
- **Input scope** Full manuscript text (main text, methods, results, discussion) without supplementary figures/tables
- **Assessment boundary** Scientific claims, methodological soundness, and evolutionary inference as presented in the main text
- **Shared manuscript claim summary** The authors propose that phosphorylation sites in the FUS prion-like domain (PLD) have evolved specifically near amyloid-prone regions to act as "checkpoints" against aberrant liquid-to-solid transitions, while preserving the ability of the protein to undergo liquid-liquid phase separation. They support this with coarse-grained simulations of FUS and FUS PLD variants, all-atom simulations of amyloid core peptides, and comparative evolutionary analyses of 85 mammalian FUS sequences against neutrally evolved controls.
- **Visible evidence base** Main text figures (Figs. 1-7), methods descriptions, and references to SI Appendix (Tables S1-S4, Figs. S1-S15)
- **Missing materials affecting confidence** SI Appendix contents (figures, tables, and detailed methods) are referenced but not provided; specific simulation parameters, force field details, and statistical test outputs are not fully described in the main text

## Reviewer

### Overall assessment
This manuscript addresses an important and timely question: how do cells exploit aggregation-prone sequences for functional phase separation while avoiding pathological solidification? The authors combine multiscale simulations with comparative genomics to argue that phosphorylation sites have been evolutionarily positioned near amyloid-prone regions in FUS as a protective mechanism. The central hypothesis is compelling and the combination of approaches is ambitious. However, the manuscript has several significant issues that need to be addressed. The coarse-grained model's ability to capture the specific effects of phosphorylation on beta-sheet propensity is questionable, the evolutionary analysis relies on a single null model with limited controls, and the causal link between the simulation results and the evolutionary inference is not fully established. The claim that phosphorylation sites are "evolutionary checkpoints" requires stronger evidence that the observed positioning is the result of positive selection specifically for this function, rather than a byproduct of other constraints.

### Who would be interested in the results, and why
This work will be of interest to researchers studying biomolecular condensates, phase separation, and the role of post-translational modifications in regulating protein aggregation. The evolutionary analysis connecting phosphorylation site positioning to amyloid-prone regions will also appeal to those interested in the molecular evolution of intrinsically disordered proteins. The methodological framework combining coarse-grained and all-atom simulations with evolutionary simulations could serve as a template for similar studies in other systems.

### Major strengths
1. The central hypothesis is novel and biologically important, addressing a fundamental question about how cells balance the beneficial and deleterious aspects of protein self-assembly.
2. The combination of multiple computational approaches (coarse-grained simulations, all-atom simulations, evolutionary simulations) provides a multifaceted view of the problem.
3. The systematic variation of phosphorylation patterns (not just fractions) is a thoughtful approach that goes beyond simple charge-based arguments.
4. The evolutionary analysis across 85 mammalian species adds a valuable comparative dimension.

### Major Concerns

**Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of coarse-grained model for phosphorylation effects
- **Claim pointer** The authors claim that "introduction of negatively charged residues at phosphosite locations results in fewer amyloid-prone contacts and thereby lower beta-sheet propensity" based on coarse-grained simulations where phosphorylation is modeled by S/T to E substitution.
- **Evidence pointer** Methods section "Coarse-Grained Flexible Polymer Model for FUS"; Results section "Phosphorylation Reduces the Likelihood of PLD-PLD Contacts"
- **Concern** The coarse-grained model uses glutamic acid substitution to mimic phosphorylation. While this is a common approximation, the authors do not adequately discuss its limitations. Phosphorylation introduces a bulky, doubly negatively charged phosphate group that can have steric and electrostatic effects beyond a single negative charge. The model's ability to capture the specific local effects on beta-sheet propensity is particularly questionable, as the coarse-grained force field is not parameterized for secondary structure prediction. The authors acknowledge this limitation for the coarse-grained model but then use the same S/T to E substitution in the all-atom simulations, where the approximation is also problematic. The phosphate group's hydrogen bonding capacity and its ability to interact with backbone amides are not captured by a glutamate side chain.
- **Why it matters** The central mechanistic claim of the paper rests on the ability of the simulations to accurately capture how phosphorylation near amyloid-prone regions disrupts beta-sheet formation. If the S/T to E approximation is not adequate, the conclusions about the mechanism may be incorrect.
- **Resolution test** The authors should either (a) perform additional all-atom simulations with explicit phosphoserine residues for at least a subset of the peptides to validate the S/T to E approximation, or (b) provide a detailed discussion of why the approximation is adequate for the specific questions addressed, with supporting evidence from the literature.

**Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evolutionary inference and null model adequacy
- **Claim pointer** The authors claim that "evolution overcomes this challenge by placing phosphosites specifically close to amyloid-prone stretches" and that this represents positive selection.
- **Evidence pointer** Results section "Simulation of Neutrally Evolved Sequences"; Figure 7
- **Concern** The evolutionary analysis compares observed FUS sequences to neutrally evolved sequences generated with a specific codon model. However, the null model may not adequately capture the complex selective pressures acting on FUS beyond those related to phosphorylation. FUS is involved in multiple cellular processes (DNA damage response, transcription regulation, RNA metabolism), and its sequence is likely constrained by many factors. The finding that phosphosites are closer to amyloid-prone regions than expected under neutrality could reflect selection for other functions, or could be an artifact of the specific evolutionary model used. The authors do not test alternative null models (e.g., models with different codon usage, different dN/dS ratios, or models that account for the overall amino acid composition of the PLD). Additionally, the comparison to control proteins (LAF-1, RYBP, securin, osteopontin) is limited; these proteins may have different evolutionary histories and constraints that make them inappropriate controls.
- **Why it matters** The evolutionary claim is a central pillar of the paper's thesis. If the null model is inadequate or the controls are inappropriate, the conclusion that phosphorylation sites have been specifically selected for their proximity to amyloid-prone regions is not supported.
- **Resolution test** The authors should (a) perform sensitivity analyses with alternative null models, (b) include additional control proteins that are phase-separating and aggregation-prone but do not show liquid-to-solid transitions, and (c) test whether the observed pattern could arise from selection on other features (e.g., overall charge, hydrophobicity) rather than specifically on phosphorylation site positioning.

**Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Causal link between simulations and evolutionary inference
- **Claim pointer** The authors state that "phosphorylation sites are evolutionary checkpoints against liquid-solid transition in protein condensates" and that the simulation results support this conclusion.
- **Evidence pointer** Results sections "Phosphorylation Maintains Liquid-Like Intracluster Environment" and "Phosphorylation Pattern, and Not Just Net Charge of the PLD, Influences Intracluster Dynamics"; Discussion
- **Concern** The manuscript presents simulation results showing that phosphorylation can modulate intracluster dynamics and reduce beta-sheet propensity, and separately presents evolutionary analyses showing that phosphosites are near amyloid-prone regions. However, the causal link between these two sets of findings is not directly tested. The authors do not demonstrate that the specific phosphorylation patterns observed in mammalian FUS sequences are more effective at preventing liquid-to-solid transitions than alternative patterns that might have evolved. The evolutionary analysis shows correlation, but the simulations do not directly test whether the observed patterns are optimal or even particularly effective compared to other possible arrangements.
- **Why it matters** The paper's title and central claim imply a causal relationship: evolution has placed phosphosites near amyloid-prone regions because this prevents liquid-to-solid transitions. Without directly testing this causal link, the claim remains correlative.
- **Resolution test** The authors should simulate or analyze the specific phosphorylation patterns found in mammalian FUS sequences and compare their effectiveness at preventing solidification to (a) random phosphorylation patterns with the same fraction, and (b) alternative "designed" patterns. This would directly test whether the observed evolutionary patterns are particularly effective at the proposed function.

**Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of findings beyond FUS
- **Claim pointer** The authors suggest that their findings represent a general principle: "Phosphorylation sites are evolutionary checkpoints against liquid-solid transition in protein condensates."
- **Evidence pointer** Title; Discussion section
- **Concern** The analysis is performed exclusively on FUS. While FUS is an important model system, the claim of a general principle requires evidence from multiple proteins. The authors do not test whether the observed relationship between phosphosite positioning and amyloid-prone regions holds in other phase-separating proteins with PLDs (e.g., TDP-43, hnRNPA1, TAF15). The evolutionary analysis is also limited to FUS orthologs.
- **Why it matters** The title and framing of the paper suggest a general principle, but the evidence is limited to a single protein. Overgeneralization from one case study could mislead the field.
- **Resolution test** The authors should either (a) extend their analysis to at least 2-3 additional PLD-containing proteins, or (b) temper their claims to be specific to FUS and clearly state that the generalizability remains to be tested.

### Minor Comments

**Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Simulation details
- **Evidence pointer** Methods section "Coarse-Grained Simulations"
- **Issue** The manuscript states that simulations were performed with 50 chains in a cubic box but does not specify the box size, salt concentration, or the specific parameters used for the Langevin dynamics (e.g., friction coefficient, integration scheme). The damping time is stated as 3,000 fs in one sentence and 3,500 fs in the next, which appears to be a typo.
- **Required correction** Clarify the box size and simulation conditions, and correct the apparent typo in the damping time.

**Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 7 statistical tests
- **Evidence pointer** Results section "Evolution Selects Phosphosites in the Vicinity of FUS Amyloidogenic Regions"
- **Issue** The manuscript reports P-values for the Wilcoxon rank-sum tests but does not report effect sizes or confidence intervals. For the comparison between human FUS and neutrally evolved sequences (P = 0.0056), it would be helpful to know the magnitude of the difference in distances.
- **Required correction** Report effect sizes or median differences with confidence intervals for the key comparisons.

**Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of diffusion coefficients
- **Affected element** Figure 2C
- **Evidence pointer** Results section "Phosphorylation Maintains Liquid-Like Intracluster Environment"
- **Issue** The authors report a fourfold variation in diffusion coefficients with phosphorylation fraction and state that higher diffusion coefficients indicate "more liquid-like behavior." However, the relationship between single-molecule diffusion within a condensate and macroscopic material properties (viscosity, elasticity) is not straightforward. The authors should be more cautious in equating faster diffusion with liquid-like behavior.
- **Required correction** Add a caveat about the interpretation of diffusion coefficients as proxies for material properties, or provide additional analysis linking diffusion to rheological properties.

**Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness of evolutionary analysis
- **Affected element** Figure 7 and related text
- **Evidence pointer** Results section "Evolution Selects Phosphosites in the Vicinity of FUS Amyloidogenic Regions"
- **Issue** The analysis of 85 mammalian FUS sequences is described, but the authors do not provide information about the phylogenetic distribution of these species, the sequence alignment methods used, or how the "potential phosphosites" were identified in non-human sequences (since experimental phosphorylation data may not be available for all species).
- **Required correction** Provide details on the species included, alignment methods, and criteria for identifying potential phosphosites in the SI.

**Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of alternative mechanisms
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The authors focus exclusively on phosphorylation as the mechanism preventing liquid-to-solid transitions. Other post-translational modifications (e.g., arginine methylation, lysine acetylation) and sequence features (e.g., glycine content, aromatic residue patterning) are known to modulate phase behavior and aggregation propensity in FUS. The discussion would benefit from acknowledging these alternative mechanisms and explaining why phosphorylation is uniquely suited as an "evolutionary checkpoint."
- **Required correction** Add a brief discussion of alternative mechanisms and justify the focus on phosphorylation.

### Technical failings that need to be addressed before the case is established
1. The S/T to E approximation for phosphorylation needs validation or more careful justification (R1-M1).
2. The evolutionary null model needs sensitivity analysis and additional controls (R1-M2).
3. The causal link between observed phosphorylation patterns and their effectiveness at preventing solidification needs direct testing (R1-M3).

### Assessment against Nature-style criteria
**Originality:** The hypothesis that phosphorylation sites have evolved specifically as checkpoints against liquid-to-solid transitions is novel and thought-provoking. While the general idea that PTMs regulate phase separation is established, the specific evolutionary framing is original.

**Scientific importance:** If substantiated, this work would provide a general principle for understanding how cells balance the beneficial and deleterious aspects of protein self-assembly. The findings could have implications for understanding disease-associated mutations in FUS and other PLD-containing proteins.

**Interdisciplinary readership:** The work bridges biophysics, molecular evolution, and cell biology, and would appeal to readers across these disciplines. The conceptual framework is accessible, though the technical details of the simulations may be challenging for non-specialists.

**Technical soundness:** The simulation approaches are state-of-the-art, but the key approximation (S/T to E for phosphorylation) and the evolutionary null model require more careful validation. The statistical analyses are appropriate but could be more thorough.

**Readability for nonspecialists:** The manuscript is generally well-written and the main concepts are explained clearly. However, the results section is dense and would benefit from more explicit connections between the different lines of evidence. The figures are informative but some (particularly Fig. 4) are complex and would benefit from clearer labeling.

### Recommendation posture
Supportive if technical concerns are resolved. The central hypothesis is compelling and the multi-scale approach is appropriate, but the current evidence does not fully establish the claim that phosphorylation sites are "evolutionary checkpoints." The authors need to (1) validate or better justify the S/T to E approximation, (2) strengthen the evolutionary analysis with additional controls and sensitivity tests, and (3) directly test whether the observed phosphorylation patterns are particularly effective at preventing liquid-to-solid transitions. With these revisions, the manuscript could make a significant contribution to the field.

## Risk / unsupported claims
1. The claim that phosphorylation sites are "evolutionary checkpoints" implies a specific selective mechanism that is not directly tested; the evidence supports correlation but not causation.
2. The claim that the effect of phosphorylation is "highly local" is based on correlation analyses in Fig. 4, but the causal relationship between local phosphorylation and reduced amyloid contacts is not directly demonstrated.
3. The statement that "evolution overcomes this challenge by placing phosphosites specifically close to amyloid-prone stretches" is presented as a definitive conclusion, but the analysis cannot rule out alternative explanations (e.g., neutral processes, selection for other functions).
4. The generalizability of the findings beyond FUS is claimed in the title but not tested.
5. The relationship between diffusion coefficients in simulations and macroscopic material properties of condensates is asserted but not rigorously established.