## Review setup
- **Input scope** Full manuscript text (preprint, arXiv:2507.22860v1)
- **Assessment boundary** Scientific content, theoretical framework, internal consistency, and claims as presented in the provided text. No supplementary information, figures, or experimental datasets were available for inspection.
- **Shared manuscript claim summary** The authors propose a universal phase diagram that predicts the minimal interfacial free energy topology of two phase-separating solutes within a finite mesoscale droplet, as a function of interfacial tension ratios and relative volume fractions. They compare their predictions qualitatively with several experimental systems (chromatin oligomers, polyK/polyR condensates, polymer mixtures) and discuss kinetic and polydispersity effects that may explain deviations from equilibrium predictions.
- **Visible evidence base** Main text only, including model description, results narrative, discussion, and references. Figures are referenced but not provided. No equations are fully displayed in the text provided (some are indicated but not rendered). No quantitative comparisons with experimental data are shown.
- **Missing materials affecting confidence** Supplementary information (SI) containing all algebraic and geometric derivations, the full phase diagram figures, and quantitative comparisons with experimental data. The absence of these materials prevents verification of the central claims.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and interesting problem: predicting the equilibrium topology of two-phase domains inside finite droplets, with potential relevance to biomolecular condensates and polymer systems. The conceptual framework, based on interfacial energy minimization and Young's law, is sound and the idea of a universal phase diagram is appealing. However, the present text does not provide sufficient quantitative evidence to establish the claims. The key derivations are relegated to the SI, the figures are not shown, and the comparison with experiments is qualitative and lacks error analysis or parameter estimation. The manuscript is likely to be of interest to the soft matter and biophysics communities, but in its current form the central claims are not fully supported by the visible evidence.
- **Who would be interested in the results, and why** Researchers in soft matter physics, biophysics, and physical chemistry studying phase separation in multicomponent systems, particularly those interested in biomolecular condensates, coacervates, and polymer blends. The universal phase diagram could serve as a useful reference for interpreting experimental observations of droplet internal structure. Experimentalists working on chromatin organization, RNA-protein condensates, or synthetic polymer mixtures would find the framework relevant for rationalizing observed topologies and for designing experiments to extract interfacial tension ratios.
- **Major strengths** 1) The problem is well-motivated and timely, with clear relevance to recent experimental observations of complex droplet topologies. 2) The theoretical approach, based on interfacial energy minimization and Young's law, is physically transparent and accessible. 3) The idea of a universal phase diagram, parameterized by tension ratios and volume fractions, is elegant and potentially powerful. 4) The discussion of kinetic limitations, polydispersity, and multiple observed topologies shows awareness of the gap between equilibrium theory and experimental reality.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** The central quantitative claims (the phase diagram, the transition lines, the comparison with experiments) are not verifiable from the provided text. The derivations are in the SI, the figures are not shown, and the experimental comparison is qualitative. Without these, the case for a "universal" phase diagram is not established.
- **Assessment against Nature-style criteria** **Originality:** The concept of a universal phase diagram for droplet topologies based on tension ratios is a useful synthesis, but the underlying physics (interfacial energy minimization, Young's law) is well-established. The originality lies in the systematic enumeration of topologies and the presentation as a universal diagram. This is a moderate advance rather than a conceptual breakthrough. **Scientific importance:** The problem is relevant to a growing community studying biomolecular condensates and multiphase droplets. A reliable predictive framework would be valuable. However, the importance is contingent on the framework being quantitatively validated, which is not demonstrated here. **Interdisciplinary readership:** The topic bridges soft matter physics, biophysics, and polymer science. The writing is generally accessible, but the lack of quantitative results and figures limits its immediate utility to a broad audience. **Technical soundness:** The theoretical framework is plausible, but the lack of visible derivations and quantitative comparisons prevents a full assessment. The qualitative comparison with experiments is suggestive but not conclusive. **Readability for nonspecialists:** The text is clearly written and the physical reasoning is explained well. However, the absence of figures and the reliance on the SI for key results make it difficult for a nonspecialist to follow the central argument.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript has potential, but the central claims require the SI and figures to be assessed. A revised version with the full derivations, the phase diagram figures, and a quantitative comparison with at least one experimental system would be needed to support the claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims to predict the minimal interfacial free energy topology of two phase-separating solutes within a droplet as a function of tension ratios and volume fractions, and to present this as a universal phase diagram.
- **Evidence pointer** Model section, Results section, Figure 2 (not provided), SI (not provided)
- **Concern** The central quantitative result, the universal phase diagram, is not visible in the provided text. The figure is referenced but not shown, and the derivations of the interfacial energy expressions and the transition lines are relegated to the SI. Without these, the reader cannot verify the correctness of the calculations or the validity of the phase diagram. The text mentions "we have calculated the interfacial energies" and "we show that this results in a universal phase diagram," but no equations or numerical results are presented in the main text.
- **Why it matters** The universal phase diagram is the core claim of the manuscript. If the derivations or the diagram are incorrect, the entire framework collapses. The reader needs to see the derivations and the figure to assess the validity of the claim.
- **Resolution test** Provide the full derivations in the main text or a clearly accessible SI, and include the phase diagram figure with clear axis labels, legend, and a description of the parameter space covered. The derivations should be complete and reproducible.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that the predicted topologies can be compared with several experimental systems to estimate the ranges of interfacial tensions.
- **Evidence pointer** Discussion section, references to experimental papers (Brennan et al., 2025; Fisher and Elbaum-Garfinkle, 2020; Yanagisawa et al., 2014; Watanabe et al., 2022)
- **Concern** The comparison with experiments is entirely qualitative. The text states that observed topologies "can be compared" and that the phase diagram "considerably limits" the possible tension ratios, but no quantitative comparison is shown. No estimates of interfacial tension ratios are derived from experimental data, no error bars are provided, and no specific experimental images are analyzed. The reader cannot assess whether the theory actually matches the experiments or whether the agreement is coincidental.
- **Why it matters** The claim that the theory can be used to extract interfacial tension ratios from experiments is a key selling point. Without a quantitative demonstration, this claim is unsupported. The reader needs to see a concrete example where the theory is applied to experimental data and the resulting tension ratios are compared with independent measurements or expectations.
- **Resolution test** Include a quantitative comparison with at least one experimental system. Show how the observed topology and contact angle are used to constrain the tension ratios, and compare the resulting values with any available independent estimates. Provide error analysis and discuss the sensitivity of the results to measurement uncertainties.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the transition between lens and crescent topologies is derived analytically and depends on volume fractions and tension ratios.
- **Evidence pointer** Results section, equation (not rendered in the provided text), SI (not provided)
- **Concern** The analytical expression for the lens-crescent transition is mentioned but not shown. The text states "we show that the locus in the tension 'phase diagram' of the lens to crescent transition is given by a curve" but the equation is not displayed. The reader cannot verify the derivation or the functional form of the transition line.
- **Why it matters** The lens-crescent transition is a key feature of the phase diagram and is stated to depend on volume fractions. Without the explicit expression, the reader cannot assess the validity of this claim or reproduce the result.
- **Resolution test** Display the full analytical expression for the lens-crescent transition line in the main text, including the definitions of all variables and the derivation steps. Provide a numerical example to illustrate the behavior.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the topologies considered (lens, crescent, partially engulfed, cap, lens plus cap, crescent plus cap) exhaust all possible topologies formed by the intersection of two or three spheres.
- **Evidence pointer** Model section, Figure 1 (not provided), SI (not provided)
- **Concern** The claim of exhaustiveness is not demonstrated. The text states that the topologies "comprise the full set of topologies allowed in the intersection of two circles (in 2d) or two spheres (in 3d)" but no proof or systematic enumeration is provided. It is unclear whether other topologies, such as multiple droplets or more complex intersections, are possible and have been excluded.
- **Why it matters** If the set of topologies is incomplete, the phase diagram may miss relevant regions of parameter space, and the predictions would be incomplete. The reader needs to be convinced that the enumeration is exhaustive.
- **Resolution test** Provide a systematic enumeration of all possible topologies for two intersecting spheres (or circles) and three intersecting spheres, with a clear argument for why no other topologies are possible. Include this in the main text or the SI.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction, Model section
- **Evidence pointer** location not provided
- **Issue** The text uses the terms "effective" and "renormalized" to describe the solutes and interactions, but the definitions are somewhat vague. The reader is told that the additional component is "subsumed" into the effective interactions, but the precise meaning of this renormalization is not fully explained.
- **Required correction** Provide a more explicit definition of what is meant by "effective" solutes and "renormalized" interactions, perhaps with a brief example or a more formal statement of the approximation.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Model section
- **Evidence pointer** location not provided
- **Issue** The text states that "the rate of drop coarsening is given by the derivative dR(t)/dt ~ 1/R(t)^2" and that "larger drops coarsening significantly more slowly." This is a minor point, but the statement is slightly imprecise: the coarsening rate decreases as R increases, but the statement "larger drops coarsening significantly more slowly" is a bit vague.
- **Required correction** Clarify the statement, for example by stating that the coarsening rate decreases as the inverse square of the droplet radius, so that larger droplets grow much more slowly than smaller ones.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Discussion section
- **Evidence pointer** location not provided
- **Issue** The discussion of kinetic limitations and multiple topologies is interesting but somewhat speculative. The text mentions "strong interactions among the solutes may lead to such kinetic barriers" and "collisions of large droplets may occur, which can lead to additional kinetic barriers," but no specific mechanisms or estimates are provided.
- **Required correction** Consider adding a brief discussion of specific kinetic mechanisms that could be relevant, or at least a more explicit statement of the assumptions underlying these speculations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results section
- **Evidence pointer** location not provided
- **Issue** The text states that the phase diagram is "universal" and "only depends on the tension ratios and relative volume fractions." However, the universality is not demonstrated beyond the specific model considered. It is unclear whether the phase diagram would change if, for example, the bulk free energy had a different functional form.
- **Required correction** Clarify the sense in which the phase diagram is universal. If it is universal within the class of models considered, state this explicitly. If it is expected to be universal more broadly, provide a justification.

## Risk / unsupported claims
- The claim of a "universal phase diagram" is not supported by the visible evidence, as the diagram itself is not shown and the derivations are in the SI.
- The claim that the predicted topologies can be compared with experiments to estimate interfacial tension ranges is not demonstrated quantitatively.
- The claim that the topologies considered are exhaustive is not proven.
- The analytical expression for the lens-crescent transition is mentioned but not shown.
- The comparison with experimental systems is qualitative and lacks error analysis or parameter estimation.
- The role of the additional component in "renormalizing" the interactions is described but not formalized.