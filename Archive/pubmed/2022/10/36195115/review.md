## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific claims, methodology, and conclusions as presented in the manuscript
- **Shared manuscript claim summary** The authors model proteins with globular and intrinsically disordered regions as "tadpoles" (colloid-polymer grafts) in hard-sphere Monte Carlo simulations. They report that these tadpoles exhibit surfactant-like behavior, including interfacial adsorption, micelle formation, and reduction of interfacial tension, and that entropic effects alone are insufficient to drive liquid-liquid phase separation at biologically relevant concentrations.
- **Visible evidence base** Abstract, Introduction, Methods, Results (Qualitative phase behaviour, Phase diagrams, Differences when Ntail = 15, Interfacial tensions), Conclusion, Data accessibility, Authors' contributions, Conflict of interest, Funding, Acknowledgements. Figures 1-6 and Tables 1-2 are referenced but not directly visible.
- **Missing materials affecting confidence** Figures and tables are not provided in the submitted text. This limits verification of quantitative results, phase diagram interpretations, and simulation snapshots. Appendix A (equilibration criterion) and Appendix B (SAFT formalism) are referenced but not included.

## Reviewer
- **Overall assessment** This manuscript presents a minimal, purely entropic model of proteins with intrinsically disordered regions, exploring whether depletion forces alone can drive liquid-liquid phase separation and surfactant-like behavior. The work is conceptually interesting and addresses a gap in both biological LLPS and grafted nanoparticle literature. The methodology is appropriate for the question posed, and the conclusion that entropy alone is insufficient at biological concentrations is a useful negative result. However, the manuscript has several technical and presentational issues that need attention, particularly around the interpretation of surfactant behavior, the treatment of finite-size effects, and the clarity of the phase diagram analysis. The work is likely of interest to researchers in biophysics and soft matter, but the current evidence base is insufficient to fully assess the strength of the claims.

- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation in biology, particularly those interested in the role of intrinsically disordered regions; soft matter physicists working on depletion interactions and colloid-polymer mixtures; and scientists interested in the physical principles underlying membraneless organelle formation. The tadpole model provides a minimal framework that could inform future experimental and theoretical work on IDR-containing proteins.

- **Major strengths** The manuscript addresses a timely and important question with a minimal, physically transparent model. The systematic approach to mapping phase diagrams and the explicit comparison with biological concentration ranges is commendable. The identification of surfactant-like behavior in a purely entropic system is a novel contribution. The authors are appropriately cautious in their conclusions regarding biological relevance.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that tadpoles "support phase separation via depletion flocculation" and exhibit "surfactant behaviours, including being found preferentially at interfaces and forming micelles in single phase solution."
- **Evidence pointer** Section 4.1 (Qualitative phase behaviour), Figures 3-5 (not visible)
- **Concern** The evidence for surfactant behavior is presented qualitatively through simulation snapshots. The claim that tadpoles are "found preferentially at interfaces" requires quantitative verification, such as density profiles or free energy calculations. Similarly, the identification of "micelles" in Figure 5 is based on visual inspection of snapshots; no structural order parameters or cluster size distributions are provided to support this assignment. Without quantitative measures, the surfactant interpretation remains speculative.
- **Why it matters** The central claim of the paper rests on the surfactant-like behavior of tadpoles. If this is not rigorously established, the novelty and significance of the work are substantially weakened.
- **Resolution test** Provide quantitative measures of interfacial adsorption (e.g., excess surface concentration as a function of bulk concentration), cluster size distributions for micelle identification, and possibly free energy profiles for a single tadpole at the interface.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "adding tadpoles decreases the overlap with the shaded volume" (i.e., the biologically relevant concentration range) and conclude that entropy is insufficient to drive biological phase separation.
- **Evidence pointer** Section 4.2 (Phase diagrams), Figure 6 (not visible)
- **Concern** The phase diagram construction relies on identifying binodals from tie lines in finite-size simulation boxes. The manuscript does not discuss finite-size effects, which can significantly shift binodal locations, particularly for systems with long-ranged depletion interactions. Additionally, the mapping of biological concentrations to model parameters via the SAFT formalism (Appendix B) is not described in sufficient detail to assess its validity. The conclusion that entropy is insufficient depends critically on this mapping.
- **Why it matters** The main biological conclusion of the paper hinges on the accuracy of the phase diagram and the concentration mapping. If finite-size effects or the SAFT mapping introduce systematic errors, the conclusion could be reversed.
- **Resolution test** Perform finite-size scaling analysis for at least one series of simulations to demonstrate that binodal locations are converged. Provide a more detailed description of the SAFT mapping, including its assumptions and limitations, and ideally validate it against an independent method.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that "to our knowledge purely repulsive models of proteins with both IDRs and globular regions have not yet been studied."
- **Evidence pointer** Introduction, Section 1
- **Concern** The literature review is relatively brief. While the claim may be accurate, the authors do not thoroughly discuss related work on entropic effects in IDR-containing proteins or on grafted nanoparticles with single polymer chains. A more comprehensive review would strengthen the novelty claim and better position the work within existing literature.
- **Why it matters** The significance of the contribution depends on its novelty relative to prior work. A more thorough literature review would help establish this.
- **Resolution test** Expand the introduction to include a more systematic discussion of related theoretical and simulation work on entropic effects in protein phase separation and on single-chain grafted nanoparticles.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors report interfacial tensions in Table 2 and claim they "overlap with" experimental values from Jawerth et al.
- **Evidence pointer** Section 4.4 (Interfacial tensions), Table 2 (not visible)
- **Concern** The conversion from simulation units to SI units involves assumptions about temperature and interface width (δ = 36.3 nm) that are not fully justified. The comparison with experimental values is presented as a single number without discussion of the uncertainty in the conversion or the differences between the model system and the experimental system (e.g., the experimental system likely involves attractive interactions). The agreement may be fortuitous.
- **Why it matters** The comparison with experiment is used to validate the model, but if the conversion is not robust, the validation is weak.
- **Resolution test** Provide a sensitivity analysis of the unit conversion, and discuss the limitations of comparing a purely repulsive model with experimental systems that include attractive interactions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction, Section 1
- **Evidence pointer** Location not provided
- **Issue** The introduction assumes familiarity with polymer physics concepts (e.g., depletion flocculation, radius of gyration) without defining them for a broader readership.
- **Required correction** Add brief definitions or intuitive explanations of key concepts such as depletion flocculation and the colloid-polymer ratio q.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, Section 2
- **Evidence pointer** Location not provided
- **Issue** The equilibration criterion is described only in Appendix A, which is not included in the submitted text. This makes it difficult to assess the reliability of the simulations.
- **Required correction** Include a brief description of the equilibration criterion in the main text or ensure the appendix is available to reviewers.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section 4.3 (Differences when Ntail = 15)
- **Evidence pointer** Location not provided
- **Issue** The discussion of the Ntail = 15 case is brief and does not provide a quantitative comparison with the Ntail = 30 case beyond the phase diagram. The claim that "tail length can be used to tune a macromolecule's preference for the separating phases" would benefit from a more detailed analysis.
- **Required correction** Provide quantitative measures of phase preference (e.g., partition coefficients) for both tail lengths.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interdisciplinary readership
- **Affected element** Conclusion, Section 5
- **Evidence pointer** Location not provided
- **Issue** The conclusion mentions "membraneless organelles" and their potential structure, but does not connect the findings to specific biological questions or experimental predictions.
- **Required correction** Add a paragraph discussing specific, testable predictions of the model for experimental systems.

## Risk / unsupported claims
- The claim that tadpoles act as surfactants is not quantitatively supported by the visible evidence (no density profiles, cluster analysis, or free energy calculations).
- The conclusion that entropy is insufficient to drive biological phase separation depends on the SAFT mapping (Appendix B), which is not described in sufficient detail to assess.
- The comparison of simulated interfacial tensions with experimental values involves assumptions in unit conversion that are not fully justified.
- The novelty claim ("purely repulsive models... have not yet been studied") is not fully supported by the literature review provided.
- The biological relevance of the model is asserted but not deeply explored; the connection to specific experimental systems is speculative.