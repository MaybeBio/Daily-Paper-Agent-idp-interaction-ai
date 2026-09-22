## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, methods, results, discussion, conclusions, and data availability statements.
- **Assessment boundary** Scientific content, methodological soundness, validity of claims relative to presented evidence, and clarity of presentation. No assessment of editorial fit or scope policy.
- **Shared manuscript claim summary** The authors introduce a graph-based local entropy metric (Shannon entropy over protein subgraph configurations) to quantify residue-level conformational disorder. They apply it to molecular dynamics simulations of gp53 (gpW) and α-synuclein, claim it acts as a local order parameter for unfolding, correlates with NMR chemical shifts, distinguishes folded/unfolded/disordered states, and detects mutation-induced perturbations relevant to aggregation.
- **Visible evidence base** Main text figures (Fig. 1–5), supplementary figure references (Fig. S1–S16), supplementary tables (Tables S1–S2), methods descriptions, and data availability links.
- **Missing materials affecting confidence** Supplementary Information content (figures and tables) was not provided in full; only referenced. Simulation trajectory details, force field parameters, and convergence criteria for the MD simulations are not fully described in the visible text. The Zenodo code repositories are referenced but not inspected.

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting and potentially useful metric for quantifying local conformational disorder in proteins. The application to gpW and α-synuclein is sensible, and the comparison with NMR-derived descriptors is a valuable step. However, several technical aspects require clarification and additional validation before the central claims can be considered fully established. In particular, the dependence of the results on the graph construction parameters (cutoff R, graph distance D), the statistical robustness of the entropy estimates, and the interpretation of the comparison with chemical shifts need more rigorous treatment.
- **Who would be interested in the results, and why** Researchers in protein biophysics, computational chemistry, and structural biology, particularly those studying protein folding, intrinsically disordered proteins, and the effects of mutations on conformational ensembles. The metric could also interest method developers working on graph-based representations of biomolecular structure and dynamics.
- **Major strengths** The concept of a graph-derived local entropy is novel and provides a different perspective from existing order parameters. The application to both a folded protein (gpW) and an intrinsically disordered protein (α-synuclein) demonstrates the potential generality of the approach. The comparison with experimental NMR data, even if qualitative, is a strength. The analysis of mutation effects in α-synuclein is timely and relevant.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (parameter sensitivity), R1-M2 (statistical robustness), R1-M3 (chemical shift comparison), R1-M4 (mutation analysis interpretation).
- **Assessment against Nature-style criteria** **Originality** The graph-based local entropy metric is a novel contribution. While graph representations of proteins are established, using the entropy of subgraph configurations as a residue-specific order parameter appears to be new. **Scientific importance** The metric could provide a useful tool for analyzing conformational ensembles, but its broad utility and advantage over existing methods (e.g., RMSF, S2, packing entropy) are not yet convincingly demonstrated. The findings on α-synuclein mutations are potentially important but require stronger validation. **Interdisciplinary readership** The work is primarily of interest to the biophysics and computational chemistry community. The conceptual framework is accessible, but the technical details may limit broader readership. **Technical soundness** The core idea is sound, but several technical aspects (parameter dependence, statistical convergence, comparison methodology) need strengthening. **Readability for nonspecialists** The manuscript is generally well-written and the main concepts are explained clearly. However, the methods section could benefit from more explicit definitions and justifications for the non-specialist.
- **Recommendation posture** Supportive if technical concerns are resolved. The central concept is promising, but the current evidence base is insufficient to fully support the strong claims made regarding the metric's utility as a general order parameter and its ability to capture biologically relevant mutation effects.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the local entropy metric provides a robust measure of structural disorder, with results presented for R = 8 Å and D = 1, 2. The authors state that "similar conclusions hold for other values of R" (referring to Fig. S1).
- **Evidence pointer** Methods section, Fig. 1, Fig. S1
- **Concern** The sensitivity of the local entropy values and the resulting conclusions to the graph construction parameters (cutoff distance R and graph distance D) is not systematically demonstrated. The claim that "similar conclusions hold" is supported only by a single supplementary figure for α-synuclein. A thorough parameter sweep (e.g., R from 6 to 10 Å in 0.5 Å increments, and possibly D = 3) should be presented for both gpW and α-synuclein, showing that the qualitative features (e.g., the transition near Tm, the classification of residues into categories, the mutation-induced changes) are robust. Without this, it is unclear whether the observed behavior is an artifact of a specific parameter choice.
- **Why it matters** The metric's utility depends on its robustness to reasonable variations in its defining parameters. If the results are highly sensitive to R or D, the metric's predictive and descriptive power is severely limited.
- **Resolution test** Provide a systematic analysis of S as a function of R (e.g., 6, 7, 8, 9, 10 Å) and D (1, 2, 3) for both proteins. Show that the key conclusions (e.g., the sharp transition in average S for gpW, the relative disorder of NAC vs. C-terminal regions in α-synuclein, the sign and location of mutation-induced changes) are qualitatively unchanged across this parameter range.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript states that local entropy is computed from 100,000 randomly selected snapshots and that this "provides sufficient statistical accuracy."
- **Evidence pointer** Methods section, Fig. S2
- **Concern** The statistical convergence of the entropy estimate is not rigorously demonstrated. The Shannon entropy of a discrete distribution with a large number of possible states (subgraphs) can be systematically underestimated if the sample size is insufficient. The authors reference Fig. S2, but the content of this figure is not visible in the provided material. A proper convergence analysis should be shown, e.g., a plot of S as a function of the number of snapshots used, demonstrating that the value has plateaued for all residues, particularly those with high entropy. Furthermore, the uncertainty in S (e.g., via bootstrapping) should be reported, at least for representative residues.
- **Why it matters** If the entropy estimates are not converged, the quantitative values and the differences between residues, temperatures, and mutants could be unreliable, undermining the central claims.
- **Resolution test** Provide a convergence plot (e.g., S vs. number of snapshots) for a set of representative residues (e.g., high, medium, and low entropy) at a few key temperatures for both proteins. Show that the entropy values are stable (within a small tolerance, e.g., 0.1) when the number of snapshots is increased from, say, 10,000 to 100,000. Report bootstrap confidence intervals for the entropy values shown in the main figures.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance / Technical soundness
- **Claim pointer** The manuscript claims a "remarkable similarity between ΔS(T) and Δδ(T) at D = 1" and that this confirms the interpretation of local entropy as an order parameter for unfolding.
- **Evidence pointer** Fig. 2, Fig. S10, Fig. S11
- **Concern** The comparison between the simulated local entropy and the experimental chemical shift data is purely qualitative and visual. The manuscript states that "a link between local entropy and chemical shifts is expected" but does not provide a quantitative measure of the agreement. The claim of "remarkable similarity" is subjective. A quantitative correlation analysis (e.g., Pearson or Spearman correlation between ΔS(T) and Δδ(T) for each residue, or a global measure of similarity) should be performed. Furthermore, the manuscript notes exceptions (K21 and D29) but does not discuss why these residues deviate, which is important for understanding the limits of the metric.
- **Why it matters** The claim that the metric correlates with experimental observables is a key part of its validation. A qualitative visual comparison is insufficient to establish this correlation, especially when there are known exceptions.
- **Resolution test** Perform a quantitative correlation analysis between ΔS(T) and Δδ(T) across all residues and temperatures. Report correlation coefficients and p-values. Discuss the outliers (e.g., K21, D29) and provide a plausible explanation for their behavior based on the structural or dynamic properties of these residues.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that Parkinson's-disease mutations in α-synuclein "locally reduce entropy while also perturbing distant regions including P1, P2 and NAC segments implicated in fibril formations."
- **Evidence pointer** Fig. 5, Fig. S1
- **Concern** The analysis of mutation effects is presented as a key result, but the statistical significance of the observed differences in S between wild-type and mutants is not assessed. The manuscript reports changes in the number of subgraphs for specific residues (e.g., P30, E46, E110), but it is unclear if these changes are significant given the uncertainty in the entropy estimates (see R1-M2). Furthermore, the link between the observed changes in local entropy and the experimentally known effects of these mutations on aggregation kinetics is speculative. The manuscript states that these changes "are expected to influence" dimerization, but no direct evidence is provided.
- **Why it matters** The claim that the metric can capture biologically relevant effects of disease-associated mutations is a significant one. Without statistical validation and a more direct link to aggregation behavior, this claim remains speculative.
- **Resolution test** Provide error bars or confidence intervals for the entropy values in Fig. 5. Perform a statistical test (e.g., a permutation test or a t-test) to assess whether the differences between wild-type and each mutant are significant. Discuss the limitations of the approach in predicting aggregation kinetics, and avoid overstating the biological implications.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section, Definition of local entropy
- **Evidence pointer** Methods section
- **Issue** The definition of the protein subgraph (sPG) and the graph distance D could be clearer. The text states that for D = 1, the sPG comprises immediate neighbors and all edges connecting them. It is not explicitly stated whether the central node is included in the sPG, and how the "edges connecting them" are defined (e.g., are edges between any two nodes in the sPG included, or only those involving the central node?).
- **Required correction** Provide a more formal and unambiguous definition of the sPG construction, possibly with a small schematic figure. Clarify whether the central node is included and how edges are selected.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section, Conformational ensembles
- **Evidence pointer** Methods section
- **Issue** The details of the MD simulations are only briefly described. The text refers to "previous all-atom MD simulations" and "coarse-grained MD simulations" but does not provide sufficient information on the force field, simulation length, temperature coupling, or system setup. This makes it difficult to reproduce the results.
- **Required correction** Provide a more detailed description of the simulation protocols, or clearly cite the original papers where the simulations are described. Include information on the number of independent simulations, if any, and how equilibration was handled.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Fig. 2
- **Evidence pointer** Fig. 2
- **Issue** The comparison between ΔS(T) and Δδ(T) in Fig. 2 is difficult to follow because the panels are not directly aligned. The reader has to visually compare panels (b), (c), (d), and (e) across different rows.
- **Required correction** Consider reorganizing the figure so that the ΔS(T) and Δδ(T) curves for the same residue are shown in the same panel or in directly adjacent panels with a shared x-axis. This would make the comparison much clearer.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion of packing entropy
- **Evidence pointer** Fig. 2d, Fig. S4, Fig. S13
- **Issue** The discussion of packing entropy (SP) is somewhat disconnected from the main narrative. The manuscript introduces it as a comparison, but the relationship between SP and the new local entropy metric could be explained more clearly. The text states that they "do not probe the same microstates," but a more explicit comparison of what each metric measures and when one might be preferred over the other would be helpful.
- **Required correction** Add a short paragraph explicitly contrasting the two metrics, their physical interpretations, and their respective strengths and limitations.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Data availability
- **Evidence pointer** Data availability section
- **Issue** The data availability statement provides links to code repositories and input data, which is good. However, it is not clear if the MD trajectories themselves are available, or only the input files. For full reproducibility, the trajectories (or at least the processed subgraph counts) should be made available.
- **Required correction** Clarify the availability of the MD trajectories. If they are too large to share, state this explicitly and provide the processed data (e.g., the list of subgraphs for each residue at each temperature) that is sufficient to reproduce the entropy calculations.

## Risk / unsupported claims
- The claim that the local entropy metric is a "generalizable framework for quantifying disorder" with "broad potential applications beyond protein science" is speculative and not supported by the data presented.
- The claim that the "apparent unfolding transition depends on the spatial scale used to describe amino-acid environments" is interesting but is not explored in sufficient depth to be fully supported.
- The statement that the local entropy of gpW at Tm "closely resembles" that of α-synuclein at 310 K is based on a visual comparison and is not quantified.
- The biological interpretation of the mutation-induced entropy changes in α-synuclein, particularly the link to aggregation kinetics, is speculative and requires further validation.
- The assertion that the local entropy "correlates well with experimental Cα chemical shifts" is based on a qualitative comparison and is not supported by a statistical analysis.