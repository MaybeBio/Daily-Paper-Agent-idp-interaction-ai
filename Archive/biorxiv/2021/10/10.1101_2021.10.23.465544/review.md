## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, conclusion, and supporting information list
- **Assessment boundary** Scientific validity of claims, methodological soundness, internal consistency between experimental and simulation data, and alignment with stated conclusions
- **Shared manuscript claim summary** The authors propose that conformational flexibility in the β-tongue and N-terminus motifs of Cytolysin A is essential for its pore-forming lytic activity, and that mutations reducing this flexibility compromise membrane disruption and pore formation
- **Visible evidence base** Experimental hemolysis and vesicle leakage assays for four point mutants; all-atom MD simulations of monomer thermal unfolding at 310, 350, and 400 K; membrane-inserted trimer arc simulations at 310 K; structural analyses including RMSD, RMSF, secondary structure changes, tilt angles, and cholesterol occupancy
- **Missing materials affecting confidence** Full methods details for experimental assays are abbreviated; no raw data or statistical analysis details for experimental replicates; no convergence analysis for MD simulations; no free energy calculations; no direct experimental validation of proposed intermediate states; no quantification of binding affinity beyond a single endpoint measurement

## Reviewer
- **Overall assessment** This manuscript presents a combined experimental and computational study addressing a significant question in pore-forming toxin biology. The central hypothesis that conformational flexibility in key membrane-interacting motifs is critical for ClyA lytic activity is plausible and potentially important. However, the evidence provided does not fully establish the causal link claimed. The experimental data show correlations between mutations and reduced activity, and the simulations show reduced flexibility in mutants, but the direct mechanistic connection between these observations remains inferential. The study would benefit from additional experimental validation of the proposed disordered intermediate state and more rigorous quantitative analysis of the simulation data.
- **Who would be interested in the results, and why** Researchers studying pore-forming toxins, membrane protein conformational dynamics, protein folding and disorder-to-order transitions, and those interested in the biophysical basis of membrane disruption. The proposed link between intrinsic disorder and membrane-mediated conformational transitions could also interest the broader protein folding and design community.
- **Major strengths** The combination of experimental activity assays with extensive all-atom MD simulations provides complementary perspectives. The choice of mutations targets residues with clear structural roles. The thermal unfolding approach at elevated temperatures is a reasonable strategy to enhance conformational sampling. The analysis of multiple structural metrics (RMSD, RMSF, secondary structure, tilt angles, cholesterol occupancy) is thorough. The discussion connecting findings to intrinsically disordered protein behavior is thought-provoking.
- **Major Concerns** The causal relationship between reduced flexibility and loss of activity is not directly demonstrated. The experimental assays measure endpoint activity, not the specific step affected by each mutation. The simulations are performed at elevated temperatures that may not reflect physiological conditions. The trimer arc simulations use a different force field than the monomer simulations, potentially complicating comparisons. No experimental validation of the proposed disordered intermediate is provided. The relationship between the observed structural changes and the actual pore formation pathway is speculative.
- **Minor Comments** Several statements in the abstract and discussion overstate the strength of the conclusions relative to the evidence. The manuscript would benefit from clearer presentation of experimental replicates and statistical significance. Some figure references are not fully described in the text.
- **Technical failings that need to be addressed before the case is established** The lack of quantitative comparison between experimental activity levels and simulation-derived flexibility metrics; the absence of convergence assessment for the MD simulations; the use of different force fields for monomer versus trimer simulations without justification; the lack of direct experimental evidence for the proposed disordered intermediate state
- **Assessment against Nature-style criteria** Originality: The concept of linking conformational flexibility to pore-forming activity is not entirely new, but the specific focus on the β-tongue and N-terminus as key determinants, and the connection to IDP-like behavior, offers a fresh perspective. Scientific importance: Understanding the molecular basis of ClyA pore formation has implications for bacterial pathogenesis and for the general principles of membrane protein conformational transitions. The potential broader relevance to PFP biology is significant. Interdisciplinary readership: The work bridges microbiology, biophysics, and computational biology, and could appeal to readers across these fields. Technical soundness: The experimental assays are standard, but the quantitative analysis is limited. The simulations are extensive but lack convergence analysis and use inconsistent force fields. The connection between simulation observables and functional outcomes is not rigorously established. Readability for nonspecialists: The manuscript is generally well-written and accessible, though some simulation details may be challenging for experimental readers. The abstract and summary effectively communicate the main findings.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal inference
- **Claim pointer** The manuscript claims that "conformational flexibility is indispensable for the outward movement of the β-tongue and the tendency to induce disorder in the β-tongue is an important step in the transition to the membrane mediated helix-turn-helix motif integral to ClyA pore formation."
- **Evidence pointer** Results sections "Point mutations in β-tongue hairpin and N-terminus helix curtail ClyA activity" and "Monomer in silico thermal unfolding reveals β-tongue flexibility"; Figures 1E, 1F, 2C, 2D
- **Concern** The central claim of a causal relationship between reduced conformational flexibility and loss of lytic activity is supported only by correlative evidence. The experimental assays show that Y178F has greatly reduced activity and the simulations show reduced flexibility in this mutant, but no direct experimental manipulation of flexibility is performed to demonstrate causality. Alternative explanations for the loss of activity, such as altered membrane binding affinity, changes in oligomerization kinetics, or disruption of specific protein-lipid interactions, are not excluded. The simulations at 400 K are far from physiological conditions, and it is unclear whether the observed flexibility differences persist at relevant temperatures.
- **Why it matters** The manuscript's primary conclusion rests on this causal link. Without direct evidence that flexibility per se, rather than other properties altered by the mutations, is responsible for the activity differences, the central thesis is not established.
- **Resolution test** Provide experimental evidence that restoring flexibility to the mutants (e.g., through second-site suppressor mutations or chemical rescue) restores activity, or demonstrate that the flexibility differences observed in simulations directly correlate quantitatively with activity across a broader panel of mutants. Alternatively, perform simulations at physiological temperature to show the flexibility differences are maintained.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological consistency
- **Claim pointer** The manuscript compares monomer simulations (CHARMM36 force field) with trimer arc simulations (AMBER99SB and SLIPIDS force fields) and draws conclusions about the relative stability and behavior of mutants across these systems.
- **Evidence pointer** Methods section "Simulation details"; Results sections "Monomer in silico thermal unfolding reveals β-tongue flexibility" and "Membrane inserted ClyA mutants are compromised structurally, with defects in membrane insertion and cholesterol interaction"
- **Concern** The use of different force fields for the monomer and trimer simulations introduces a potential confound. Differences in behavior between the two systems could arise from force field differences rather than from the physical differences between monomeric and membrane-inserted states. The manuscript does not justify this choice or discuss its potential impact on the conclusions.
- **Why it matters** The manuscript draws conclusions about the relationship between monomer flexibility and trimer stability. If the force field differences systematically bias one system toward more or less flexibility, the comparison could be misleading.
- **Resolution test** Repeat key trimer simulations with the CHARMM36 force field used for monomers, or provide evidence that the force field choice does not significantly affect the conclusions (e.g., by comparing a subset of systems with both force fields).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative rigor
- **Claim pointer** The manuscript states that "this decreased loss of conformational flexibility correlates positively with the reduced lytic and leakage activity observed in experiments."
- **Evidence pointer** Results sections "Point mutations in β-tongue hairpin and N-terminus helix curtail ClyA activity" and "Monomer in silico thermal unfolding reveals β-tongue flexibility"; Figures 1E, 1F, 2C, 2D
- **Concern** The claimed correlation between flexibility and activity is not quantified. No statistical measure of correlation is provided, and the number of mutants (four plus wild type) is small. The relationship appears qualitative rather than quantitative, and it is unclear whether the correlation would hold with additional mutants or replicates.
- **Why it matters** A quantitative correlation would strengthen the claim that flexibility is a key determinant of activity. Without it, the relationship remains suggestive.
- **Resolution test** Provide a quantitative correlation analysis (e.g., Spearman or Pearson correlation) between a flexibility metric (e.g., RMSF in the β-tongue region) and an activity metric (e.g., t1/2 or leakage rate) across all variants, with appropriate statistical testing.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Experimental validation
- **Claim pointer** The manuscript proposes that "the tendency to disorder in the β-tongue is an important step in the transition to the membrane mediated helix-turn-helix motif" and draws parallels to intrinsically disordered proteins.
- **Evidence pointer** Discussion section; Figure 4
- **Concern** The proposed disordered intermediate state is inferred solely from simulation data at elevated temperature. No experimental evidence for such an intermediate is provided. The connection to IDP behavior is speculative and not supported by direct experimental observation of disorder in the ClyA system.
- **Why it matters** The proposed mechanism, if correct, would be a significant contribution. However, without experimental validation, it remains a hypothesis rather than an established finding.
- **Resolution test** Provide experimental evidence for a disordered or partially unfolded intermediate, for example through hydrogen-deuterium exchange, limited proteolysis, or single-molecule FRET experiments under conditions relevant to membrane binding.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first paragraph
- **Issue** The phrase "conformational flexbility" contains a typographical error.
- **Required correction** Correct to "conformational flexibility".

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Experimental methods and results
- **Evidence pointer** Results section "Point mutations in β-tongue hairpin and N-terminus helix curtail ClyA activity"; Figure 1E, 1F
- **Issue** The experimental data are presented without error bars or statistical significance testing. It is unclear how many independent replicates were performed and whether the observed differences between mutants are statistically significant.
- **Required correction** Provide the number of replicates, error bars, and appropriate statistical tests for the hemolysis and leakage assays.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** Multiple locations
- **Issue** The term "promoter" appears in the Results section where "protoner" or "protomer" is intended.
- **Required correction** Correct the typographical error.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods section
- **Evidence pointer** Methods section "Experimental methods"
- **Issue** The experimental methods are described very briefly. Details on protein expression, purification, and quality control are not provided.
- **Required correction** Provide sufficient experimental details to allow replication, or reference previously published protocols.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results section "Membrane inserted ClyA mutants are compromised structurally, with defects in membrane insertion and cholesterol interaction"
- **Evidence pointer** Figure 6
- **Issue** The increased cholesterol occupancy in the β-tongue pockets of Y178F is interpreted as potentially contributing to reduced activity, but the mechanistic link is not fully explained. It is unclear whether this increased occupancy is a cause or consequence of the mutant's reduced ability to undergo conformational changes.
- **Required correction** Clarify the proposed mechanism by which increased cholesterol occupancy would impair pore formation, and discuss alternative interpretations.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Generalizability
- **Affected element** Discussion
- **Evidence pointer** Discussion section, final paragraph
- **Issue** The claim that "inherent disorder could be a more general phenomenon invoked across a wide range of PFTs" is speculative and not supported by data from other PFT systems.
- **Required correction** Soften the claim or provide supporting evidence from other PFTs.

## Risk / unsupported claims
- The claim that conformational flexibility is "indispensable" for pore formation is not fully supported, as no experiment directly manipulates flexibility without affecting other properties.
- The proposed disordered intermediate state is not experimentally validated.
- The correlation between flexibility and activity is not quantitatively established.
- The generalization to other pore-forming toxins is speculative.
- The functional significance of increased cholesterol occupancy in Y178F is not mechanistically established.
- The use of different force fields for monomer and trimer simulations without justification or cross-validation weakens the comparability of results across systems.