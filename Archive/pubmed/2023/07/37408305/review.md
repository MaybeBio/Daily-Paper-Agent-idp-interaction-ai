## Review setup
- **Input scope** Full manuscript text (abstract, significance, introduction, methods, results, discussion, conclusion) without figures or supplementary material
- **Assessment boundary** Scientific claims, methodological soundness, and internal consistency based solely on the provided text; figures and supplementary data referenced but not directly examined
- **Shared manuscript claim summary** The authors use residue-resolution coarse-grained simulations (Mpiri model) with direct-coexistence molecular dynamics and genetic algorithms to show that the difference in aromatic and arginine content between two proteins determines multiphasic versus monophasic condensation in protein-RNA mixtures, and that this principle can be used to design condensates with RNA partitioned to a specific phase.
- **Visible evidence base** Text descriptions of simulation results, fitness functions, density profiles, interaction energy analyses, and design principles; references to Figures 1–4 and Figures S1–S8
- **Missing materials affecting confidence** All figures, supplementary figures, simulation parameter tables, and the Figshare data repository contents; without these, quantitative claims about density profiles, energy differences, and sequence evolution cannot be independently verified

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question: what molecular features drive multiphasic organization in protein-RNA condensates. The combination of direct-coexistence simulations with genetic algorithm evolution is creative and well suited to the problem. The central claim, that the difference in aromatic and arginine content between two proteins controls multiphasicity, is plausible and consistent with existing experimental literature. However, the evidence as presented in the text alone is insufficient to fully evaluate the robustness of this claim. Several key results are described qualitatively without quantitative support, and the genetic algorithm methodology raises questions about convergence, reproducibility, and the interpretation of evolved sequences. The design demonstration in Figure 4d is intriguing but appears to rely on hand-picked sequences rather than systematic optimization, which weakens the generality of the proposed design rules. Overall, the work is potentially valuable but requires additional quantitative detail and methodological clarification before the central claims can be considered established.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, particularly those interested in multiphasic architectures, protein-RNA interactions, and the molecular grammar of phase separation. The work is also relevant to the growing community using computational models to predict and design condensate properties, and to experimentalists seeking design rules for synthetic condensates with controlled internal organization. The emphasis on arginine versus lysine differences and aromatic content connects directly to ongoing debates about sticker-residue identities in phase-separating systems.

- **Major strengths** The study addresses a relatively underexplored question (multiphasicity in protein-RNA systems) with a well-chosen computational approach. The use of genetic algorithms to evolve sequences toward or away from multiphasicity is a powerful and creative strategy that goes beyond simple correlation analysis. The authors connect their findings to existing experimental observations (e.g., poly-arginine/poly-lysine/poly-U systems) and provide a clear, testable design principle. The writing is generally clear and the logical flow from simple model systems to design principles is easy to follow.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "The total aromatic and arginine content of the two proteins must be appreciably different for distinct phases to form, and we show that this difference increases as the system is driven toward greater multiphasicity."
- **Evidence pointer** Figures 2, 3, 4; text in sections "Multiphasicity can be fine-tuned by a genetic algorithm" and "Arginine and aromatic content controls multiphasic behavior"
- **Concern** The central quantitative claim is presented without numerical data in the text. The authors state that multiphasicity increases with the difference in aromatic and arginine content, but no quantitative measure of multiphasicity is defined or reported. The fitness functions in Eqs. 5 and 6 are density-based, but the relationship between these fitness values and the physical degree of multiphasicity is not established. Without a clear metric and associated values, the reader cannot assess the strength or significance of the reported trends.
- **Why it matters** The claim that aromatic and arginine content "drives" multiphasicity is the central message of the paper. If the supporting quantitative evidence is not clearly presented, the claim cannot be evaluated or reproduced by others.
- **Resolution test** Provide a defined multiphasicity metric (e.g., interfacial width, composition difference between phases, or similar), report its values for the systems in Figures 2–4, and show that the trend holds across multiple independent simulation runs with error estimates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological robustness
- **Claim pointer** "Using the trends observed in the different interaction energies of this system, we demonstrate that we can also construct multilayered condensates with RNA preferentially concentrated in one phase."
- **Evidence pointer** Figure 4d; text in section "Composition of coexisting phases can be designed"
- **Concern** The design demonstration in Figure 4d appears to involve hand-picked sequences (e.g., (NNNGG)10, (FFFGG)10) rather than sequences generated by the genetic algorithm or a systematic design procedure. The text states that the authors "use the lessons learnt" to design systems by hand, but the criteria for choosing these specific sequences are not fully specified. It is unclear whether these are isolated examples or representative of a general design capability.
- **Why it matters** The claim that the identified rules "can enable the design of synthetic multiphasic condensates" is a key translational outcome. If the demonstration relies on bespoke examples without a systematic procedure, the generality of the design rules is not established.
- **Resolution test** Either (a) use the genetic algorithm with a fitness function that rewards RNA partitioning to generate the designed sequences, or (b) provide a systematic screen over sequence space showing that the design principle holds for a range of sequences, not just a few hand-picked examples.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation and causality
- **Claim pointer** "Aromatic residues and arginine forming the key stabilizing interactions" and "the difference in composition of aromatics and arginine between the two proteins should be small" for monophasic condensates.
- **Evidence pointer** Figures 2, 3; text in sections "Arginine and aromatic content controls multiphasic behavior" and "Composition of coexisting phases can be designed"
- **Concern** The manuscript emphasizes arginine and aromatic content, but the genetic algorithm evolves full sequences, and many other properties (charge distribution, hydrophobicity, patterning) change simultaneously. The attribution of multiphasicity specifically to aromatic and arginine content is inferred from composition analysis, but the text does not demonstrate that these residues are causally responsible rather than correlated with other sequence features. The authors acknowledge patterning effects (Figure 3 shows scatter for the same composition), but the causal role of specific residues is not isolated.
- **Why it matters** The design rules proposed depend on identifying the key molecular determinants. If the causal residues are misidentified, the design rules may fail when applied to new sequences.
- **Resolution test** Perform controlled mutations that swap arginine to lysine or aromatic to non-aromatic residues while keeping other properties fixed, and show that multiphasicity changes accordingly. Alternatively, use a sequence-design approach that systematically varies aromatic and arginine content while controlling for other features.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** "The 'rules' identified can thus enable the design of synthetic multiphasic condensates"
- **Evidence pointer** Conclusion section; Figure 4d
- **Concern** All simulations use poly-U RNA and homopolypeptide or simple repeat proteins. The authors do not test whether the identified rules hold for more complex sequences, different RNA sequences, or different solution conditions. The claim of general design rules is therefore extrapolated beyond the tested parameter space.
- **Why it matters** The stated goal of enabling design of synthetic condensates implies broader applicability than the narrow set of systems tested. Without evidence of generalizability, the rules may be specific to the model systems studied.
- **Resolution test** Test at least one additional RNA sequence (e.g., mixed bases) and one set of more complex protein sequences to show that the aromatic/arginine difference rule holds beyond the specific systems studied.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods description
- **Evidence pointer** Section "Simulation setup"
- **Issue** The text states that simulations are run at 250 K, which is far below physiological temperature and also below the freezing point of water. The choice of temperature is not justified in the text.
- **Required correction** Provide a brief justification for the simulation temperature, or acknowledge that the coarse-grained model's energy scale is not directly mapped to physical temperature.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Genetic algorithm details
- **Evidence pointer** Section "Genetic algorithm"
- **Issue** The genetic algorithm parameters (mutation rate, crossover probability, population size, number of generations, convergence criteria) are not fully specified in the text. The authors state they "largely follow" a previous procedure, but the specific parameters used here are not given.
- **Required correction** Provide the full set of genetic algorithm parameters used, or explicitly state that they are identical to the referenced work and list any deviations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion of lysine versus arginine
- **Evidence pointer** Section "Arginine and aromatic content controls multiphasic behavior"
- **Issue** The text notes that arginine and lysine both carry positive charge but behave differently, yet the mechanistic explanation for this difference is brief. The authors mention cation-π and π-π interactions but do not elaborate on why arginine's guanidinium group is uniquely suited for these interactions.
- **Required correction** Expand the discussion of the molecular basis for the arginine-lysine difference, or refer the reader to specific prior work that provides this analysis.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure references
- **Evidence pointer** Throughout Results and Discussion
- **Issue** The text frequently refers to figures and supplementary figures, but the figures themselves are not available in the provided material. Some figure descriptions are detailed, but others are terse (e.g., "Fig. S2" is mentioned without description).
- **Required correction** Ensure that all figure references are accompanied by sufficient description in the text that the key result can be understood without viewing the figure.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Scope
- **Affected element** Conclusion
- **Evidence pointer** Conclusion section
- **Issue** The conclusion discusses limitations of the coarse-grained model and the gap between simulations and cellular behavior, which is appropriate. However, the transition from "rules identified in simulations" to "implications for cellular condensates" is somewhat abrupt and could benefit from a more explicit statement of what would need to be tested experimentally.
- **Required correction** Add a brief paragraph outlining specific experimental predictions that arise from the simulation results, which would facilitate testing of the proposed rules.

## Risk / unsupported claims
- The claim that "the total aromatic and arginine content of the two proteins must be appreciably different for distinct phases to form" is presented as a general rule but is only demonstrated for a narrow set of model sequences; the word "must" implies necessity that is not established.
- The statement that the identified rules "can enable the design of synthetic multiphasic condensates" is an extrapolation from a small number of hand-designed examples; the generality of the design capability is not demonstrated.
- The claim that "protein-RNA interactions dominate" in multiphasic condensates is stated without quantitative comparison to protein-protein or RNA-RNA interaction contributions across the full range of systems studied.
- The assertion that the Mpiri model "can predict the critical solution temperature of protein solutions in good agreement with experiment" is referenced to prior work but not demonstrated for the specific systems studied here.
- The statement that "the difference in composition of aromatics and arginine between the two proteins should be small" for monophasic condensates is presented as a design rule but is only supported by a limited number of genetic algorithm runs.