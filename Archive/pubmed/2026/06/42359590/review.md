## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no figures, methods, or supporting data were provided for evaluation
- **Shared manuscript claim summary** The authors report Gaussian accelerated molecular dynamics (GaMD) simulations of the P1LEA-22 model peptide in TFE-water and glycerol-water mixtures at 20%, 40%, 60%, and 80% cosolvent concentrations. They claim that TFE induces a compact helix-turn-helix motif at 80% concentration through hydrophobic shielding and enhanced intrahelical electrostatic interactions, whereas glycerol promotes compaction via steric restriction and competitive solvation, yielding heterogeneous ensembles with beta-sheet-like conformations and centrally localized helices. The authors conclude that the two cosolvents modulate the peptide energy landscape through distinct mechanisms despite both mimicking dehydration.
- **Visible evidence base** Abstract text only; no simulation parameters, convergence metrics, force field details, ensemble analyses, or structural figures were provided
- **Missing materials affecting confidence** Full manuscript, simulation methodology, force field and water model specifications, GaMD parameters, convergence and sampling validation, conformational ensemble analyses, free energy calculations, comparison with experimental data, and all figures and tables

## Reviewer
- **Overall assessment** The abstract presents a plausible and potentially interesting computational study of how two cosolvents differentially shape the conformational ensemble of a group-3 LEA model peptide. The central claim that solvent identity, not merely water activity, determines the structural response is conceptually valuable. However, the abstract alone provides insufficient evidence to evaluate the technical soundness of the simulations or the robustness of the reported conformational differences. The mechanistic interpretations, particularly the role of fluorine-mediated hydrophobic shielding and the distinction between TFE and glycerol effects, require substantial supporting data that are not visible in the supplied material.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, desiccation tolerance mechanisms, and the molecular basis of cosolvent effects on protein conformation. The work may also interest computational biophysicists developing and applying enhanced sampling methods to IDP systems, as well as investigators working on LEA proteins in plant stress biology and on the general problem of how solvent composition modulates IDP ensembles.
- **Major strengths** The study addresses a biologically relevant question about how LEA proteins respond to dehydration-mimicking environments. The comparative design using two cosolvents with distinct physicochemical properties is conceptually sound. The use of GaMD is appropriate for sampling conformational ensembles of IDPs. The claim that solvent identity matters beyond simple water activity is an important and testable hypothesis.
- **Major Concerns** The abstract reports specific structural outcomes without providing any quantitative measures of ensemble properties, convergence, or statistical confidence. The mechanistic claims about TFE fluorine atoms and glycerol excluded volume effects are presented as established findings but no evidence is visible. The absence of any comparison with experimental data or with control simulations in pure water weakens the interpretability of the reported cosolvent effects.
- **Minor Comments** The abstract would benefit from reporting quantitative ensemble descriptors such as radius of gyration, secondary structure populations, or free energy differences. The phrase "centrally localized helices" is vague and requires definition. The relationship between the simulated cosolvent concentrations and physiologically relevant dehydration conditions is not stated.
- **Technical failings that need to be addressed before the case is established** None can be definitively identified from the abstract alone, but the absence of any methodological detail prevents verification of sampling adequacy, force field suitability, or simulation convergence. The core claims are therefore not assessable from the supplied material.
- **Assessment against Nature-style criteria** Originality: the comparative cosolvent approach is moderately original, though cosolvent effects on IDPs have been studied extensively. Scientific importance: potentially relevant to desiccation biology and IDP biophysics, but the significance level cannot be judged from the abstract. Interdisciplinary readership: the topic bridges biophysics, physical chemistry, and plant biology, which is favorable. Technical soundness: not assessable from the abstract; no methodological details or validation are provided. Readability for nonspecialists: the abstract is clearly written and accessible, though some terms such as "helix-turn-helix motif" and "excluded volume" assume basic biophysical literacy.
- **Recommendation posture** Currently not established from the provided evidence. The conceptual framework is promising, but the abstract does not provide sufficient information to evaluate whether the simulation results are technically reliable or whether the mechanistic interpretations are supported. A full manuscript with detailed methods, convergence analyses, and quantitative ensemble comparisons would be required to assess the claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that GaMD simulations at four cosolvent concentrations provide an atomistic description of how solvent composition reshapes peptide folding.
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract provides no information about simulation length, number of replicas, force field parameters, water model, temperature and pressure coupling, or GaMD acceleration parameters. Without these details, it is impossible to assess whether the simulations were sufficiently converged or whether the sampling adequately captured the conformational ensemble of an intrinsically disordered peptide.
- **Why it matters** IDPs are notoriously difficult to sample adequately, and conformational ensembles derived from under-converged simulations can be misleading. The central claims about TFE-induced helix stabilization and glycerol-induced compaction depend entirely on the quality and extent of conformational sampling.
- **Resolution test** The full manuscript must report simulation protocols, convergence metrics such as block averaging or autocorrelation analyses, and comparison of ensemble properties across independent trajectories or replicas.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors claim that at 80% TFE, the peptide stabilizes a compact helix-turn-helix motif through enhanced intrahelical electrostatic interactions driven by hydrophobic shielding from TFE fluorine atoms.
- **Evidence pointer** Abstract; location not provided
- **Concern** The mechanistic attribution to fluorine-mediated hydrophobic shielding and enhanced intrahelical electrostatics is presented as a definitive conclusion, but no quantitative data such as contact maps, electrostatic energy decompositions, or solvent-shell analyses are provided. The abstract does not report how these interactions were identified or quantified.
- **Why it matters** The proposed mechanism is the central novel insight of the study. If the mechanism is not rigorously supported by interaction energy analyses and structural statistics, the claim is speculative rather than evidence-based.
- **Resolution test** The manuscript must include quantitative analyses of intrahelical contacts, electrostatic interaction energies, solvent accessible surface areas, and radial distribution functions around fluorine atoms, with appropriate statistical comparisons across concentrations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors claim that glycerol promotes compaction through steric restriction and competitive solvation, leading to beta-sheet-like conformations and centrally localized helices.
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract reports the presence of beta-sheet-like conformations and centrally localized helices in glycerol but provides no quantitative secondary structure populations, no definition of "centrally localized," and no comparison of ensemble heterogeneity metrics between the two cosolvent conditions.
- **Why it matters** The distinction between TFE and glycerol effects is the core comparative claim of the study. Without quantitative ensemble descriptors, the reader cannot evaluate whether the reported differences are statistically meaningful or merely anecdotal observations from individual trajectories.
- **Resolution test** The manuscript must report secondary structure populations with error estimates, ensemble heterogeneity measures such as conformational entropy or cluster analysis, and a clear operational definition of helix localization within the peptide sequence.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that both TFE-water and glycerol-water mixtures mimic distinct dehydration environments relevant to LEA protein function.
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract does not justify why these specific cosolvent concentrations (20%, 40%, 60%, 80%) correspond to physiologically relevant dehydration conditions. No connection is made between the simulated solvent conditions and the actual water activity or osmotic stress experienced by LEA proteins during desiccation.
- **Why it matters** The biological relevance of the study depends on the assumption that the chosen cosolvent systems meaningfully mimic dehydration. If this mapping is not established, the implications for LEA protein function are speculative.
- **Resolution test** The manuscript must provide a rationale for the chosen cosolvent concentrations, ideally with reference to water activity values, osmotic pressure calculations, or prior experimental studies linking these conditions to dehydration stress.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract text
- **Evidence pointer** Abstract; location not provided
- **Issue** The phrase "centrally localized helices" is ambiguous and could refer to helices positioned in the middle of the peptide sequence, helices located in the central region of the conformational ensemble, or helices that are centrally positioned within a compact structure.
- **Required correction** Define the term operationally, for example by specifying the residue range or the structural criterion used to classify helix localization.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Abstract text
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract does not report any quantitative ensemble descriptors such as radius of gyration, end-to-end distance, or secondary structure propensities. The qualitative language ("compact," "heterogeneous," "stabilizes") cannot be evaluated without numerical values.
- **Required correction** Include representative quantitative values for key ensemble properties in the abstract, or state that such values are reported in the main text.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Context
- **Affected element** Abstract text
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract does not mention whether the simulations were validated against any experimental data, such as circular dichroism or NMR measurements, which would strengthen confidence in the computational predictions.
- **Required correction** State explicitly whether experimental validation was performed, or acknowledge the absence of such validation as a limitation.

## Risk / unsupported claims
- The claim that TFE stabilizes a compact helix-turn-helix motif at 80% concentration through fluorine-mediated hydrophobic shielding and enhanced intrahelical electrostatics is unsupported by the abstract alone; no interaction energy or structural evidence is visible.
- The claim that glycerol drives compaction via steric restriction and competitive solvation is presented without quantitative support.
- The claim that the two cosolvents modulate the energy landscape through distinct mechanisms is a reasonable hypothesis but is not established from the provided evidence.
- The biological relevance of the chosen cosolvent concentrations to dehydration conditions is not assessable from the abstract.
- The overall conclusion that the findings provide molecular-level insight into LEA protein adaptation under water-deprived conditions is not supported by the visible evidence, as no connection to functional or experimental data is made.