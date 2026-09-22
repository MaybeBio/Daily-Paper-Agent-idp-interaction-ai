## Review setup

- **Input scope** Full manuscript text, including main text, equations, and Appendix A. Figures are referenced but not provided.
- **Assessment boundary** Scientific content, theoretical framework, experimental design as described, and internal consistency of the claims with the presented evidence. No assessment of figures or supplementary materials, as these were not supplied.
- **Shared manuscript claim summary** The authors propose that client recruitment and post-translational modification (phosphorylation) of scaffolds in multicomponent biomolecular condensates act as distinct but convergent regulatory mechanisms that control condensate composition and phase behavior. Using a reconstituted focal adhesion system (FAK, Cas, PXN), they report that both FAK phosphorylation and PXN recruitment enrich FAK and deplete Cas in the condensed phase. They develop Flory–Huggins mean-field theories to interpret these observations, showing that client recruitment renormalizes effective scaffold interactions and lowers the critical interaction strength required for phase separation. Experimental validation is claimed for the prediction that PXN lowers the critical point of condensation.
- **Visible evidence base** Experimental descriptions in Section II.1 and II.6 (fluorescence imaging, intensity quantification, protein purification, phosphorylation state control). Theoretical derivations in Sections II.2–II.5 and Appendix A. No figures, numerical data, or quantitative results are provided in the supplied text.
- **Missing materials affecting confidence** All figures (Fig. 1–6), numerical values for measured intensities, statistical analyses, experimental replicates, and detailed methods. The absence of quantitative data prevents independent verification of the reported compositional changes and the claimed agreement between theory and experiment.

## Reviewer

- **Overall assessment** The manuscript addresses a timely and important question in the field of biomolecular condensates: how client molecules feed back on scaffold interactions to control condensate composition. The conceptual framework, distinguishing phosphorylation-driven and client-driven modulation of scaffold interactions, is potentially valuable. However, the current version of the manuscript is severely limited by the absence of quantitative experimental data and figures. The theoretical sections are presented in a highly condensed form, with key equations and derivations either missing or only partially shown. The experimental claims, which are central to the paper's impact, cannot be evaluated without the actual data. The manuscript in its present form does not establish the case for the proposed principles.
- **Who would be interested in the results, and why** Researchers studying phase separation and biomolecular condensates, particularly those interested in multicomponent systems, client-scaffold interactions, and the role of post-translational modifications. The theoretical framework for renormalizing scaffold interactions in the presence of clients could be of interest to the biophysics and soft matter communities. The focal adhesion system is a relevant model for cell signaling and adhesion biology.
- **Major strengths** The question addressed is of high importance. The combination of a relevant biological system with a theoretical framework is appropriate. The idea that client recruitment renormalizes scaffold interactions and shifts critical points is conceptually interesting and potentially generalizable. The distinction between phosphorylation effects (via heterotypic interactions and entropy) and client effects (via renormalization of effective interactions) is a useful conceptual contribution.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental evidence
- **Claim pointer** "FAK phosphorylation increases FAK intensity and decreases Cas intensity inside condensates. Similarly, adding paxillin increases FAK intensity and decreases Cas intensity inside condensates."
- **Evidence pointer** Section II.1, Figure 2 (not provided)
- **Concern** The central experimental claim of the paper, that phosphorylation and PXN recruitment produce a common compositional response, is presented without any quantitative data. No numerical values for fluorescence intensities, no error bars, no statistical tests, and no replicate numbers are given. The figures that would support these claims are not provided. Without these data, the experimental foundation of the manuscript cannot be assessed.
- **Why it matters** The entire theoretical framework is built to explain these experimental observations. If the experimental observations are not robustly established, the theoretical interpretation loses its anchor. The claim of a "common compositional response" is a key finding that requires rigorous quantitative support.
- **Resolution test** Provide the actual fluorescence intensity measurements, including mean values, standard deviations or standard errors, number of independent experiments, and statistical significance tests for the comparisons between conditions (e.g., phosphorylated vs. dephosphorylated FAK, with vs. without PXN). The figures must be included.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Theoretical derivation
- **Claim pointer** "we develop a minimal three-component Flory–Huggins theory without an explicit solvent and map it onto an effective two-component description, demonstrating that client recruitment renormalizes homotypic and heterotypic scaffold interactions."
- **Evidence pointer** Section II.3, Equations (2) and (3) (partially shown)
- **Concern** The three-component Flory–Huggins theory is introduced but the key equations are not fully presented. Equation (2) is referenced but not shown in the supplied text. The mapping to an effective two-component description is stated but the derivation is not provided. The renormalized interaction parameters ξ₁, ξ₂, and ξ₃ are defined but the steps leading to their interpretation as effective interactions are not shown. The analytical results for critical points in Section II.5 are stated without derivation.
- **Why it matters** The theoretical framework is a major component of the paper's contribution. Without the full derivation, the reader cannot verify the correctness of the results or understand the assumptions and limitations of the model. The claim of a "minimal" theory requires that the model and its reduction be transparent.
- **Resolution test** Provide the complete free energy expression for the three-component system, the full derivation of the effective two-component mapping, and the step-by-step derivation of the critical point conditions and solutions. All equations must be numbered and referenced.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Theory-experiment comparison
- **Claim pointer** "In Sec. II.6, we show results from reconstituted experiments which confirm our theory that PXN decrease the critical point of condensation."
- **Evidence pointer** Section II.6, Figure 6 (not provided)
- **Concern** The experimental test of the theoretical prediction regarding the critical point is described only qualitatively. The authors state that adding PXN at 1 µM to a 500 nM system "was sufficient to promote robust condensate formation," but no quantitative measure of the critical point shift is provided. The connection between this single observation and the theoretical prediction of a lowered critical interaction strength is not quantitatively established.
- **Why it matters** The claim that experiments "confirm" the theory is a strong statement. A single binary observation (condensates form vs. do not form) is insufficient to confirm a quantitative prediction about critical points. The theory predicts specific shifts in critical interaction parameters, which should be testable through systematic concentration series.
- **Resolution test** Provide a systematic experimental characterization of the phase boundary as a function of PXN concentration, with quantitative measurements of condensate formation (e.g., turbidity, microscopy-based counting, or fluorescence partitioning). Compare the measured critical concentrations or interaction strengths with the theoretical predictions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Model assumptions
- **Claim pointer** "we model FAK, Cas, and PXN as sticker–spacer polymers" and "we consider a solvent-free formulation in which incompressibility is enforced explicitly among the three components."
- **Evidence pointer** Sections II.2 and II.3
- **Concern** The choice of model parameters is not justified. The authors state that χ₁₂ > χ₁₁ is chosen to "favor associative phase separation," but no rationale is given for the specific values used in the calculations. The solvent-free assumption is a significant simplification that may not be valid for the experimental system, where buffer conditions and molecular crowding could be important. The relationship between the model parameters and the actual molecular interactions in the FAK-Cas-PXN system is not discussed.
- **Why it matters** The predictive power of the theory depends on the appropriateness of the model assumptions. If the parameter choices are arbitrary or the solvent-free assumption is unjustified, the quantitative predictions may not be reliable. The authors should clarify the regime of validity of their model.
- **Resolution test** Justify the parameter choices based on experimental measurements or literature values. Discuss the limitations of the solvent-free assumption and its potential impact on the predictions. If possible, compare the model predictions with alternative formulations that include explicit solvent.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** "our results reveal distinct yet convergent physical routes by which post-translational modification and client recruitment control scaffold composition in multicomponent condensates."
- **Evidence pointer** Sections II.2–II.5, Conclusion
- **Concern** The claim of generalizability is not supported by the evidence presented. The study is limited to a single model system (FAK-Cas-PXN) with specific interaction properties. The theoretical framework is mean-field and equilibrium, which may not capture the complexity of cellular condensates. The authors do not discuss how their findings would apply to systems with different stoichiometries, interaction valencies, or numbers of components.
- **Why it matters** The title and abstract suggest broad principles, but the evidence is from one system. Without a discussion of the conditions under which the proposed mechanisms would hold, the claim of general principles is premature.
- **Resolution test** Discuss the conditions under which the proposed mechanisms would apply. Consider whether the renormalization approach would hold for systems with different interaction topologies or component numbers. If possible, test the predictions in a second model system or through simulations with different parameter regimes.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section II.1
- **Evidence pointer** "We've previously shown that both Cas and FAK can independently drive phase separation"
- **Issue** The use of "We've" is informal and inconsistent with the style of a scientific manuscript.
- **Required correction** Change to "We have previously shown" or "It has been previously shown."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Section II.2
- **Evidence pointer** "Phosphorylation is thought to enhance heterotypic scaffold–scaffold interactions."
- **Issue** The phrase "is thought to" is vague. It is unclear whether this is the authors' hypothesis, a previously published finding, or a general assumption in the field.
- **Required correction** Clarify the basis for this statement, either by citing specific literature or by stating it as the authors' assumption.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section II.5
- **Evidence pointer** "Solving Eqs. (3a)–(3d) yields closed-form expressions for the critical compositions..."
- **Issue** The closed-form expressions are not shown in the supplied text. The reader is told they exist but cannot see them.
- **Required correction** Provide the explicit expressions for φ₁ᶜ, φ₂ᶜ, ξ₁ᶜ, and ξ₂ᶜ.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Experimental detail
- **Affected element** Section II.6
- **Evidence pointer** "We combined GFP-pFAK, phosphorylated Cas, Nck, and NWASP at 500 nM concentration"
- **Issue** The concentration of each component is not specified. It is unclear whether all components are at 500 nM or if this is the total concentration.
- **Required correction** Specify the concentration of each individual component.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Referencing
- **Affected element** Throughout
- **Evidence pointer** Various citations
- **Issue** The reference list is not provided. Several citations are mentioned in the text (e.g., Harmon et al. 2017; Li et al. 2012) but the full references are absent.
- **Required correction** Include a complete reference list.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Notation
- **Affected element** Section II.2
- **Evidence pointer** "Equation (1) gives the Flory–Huggins free energy density..."
- **Issue** Equation (1) is not shown in the supplied text. The reader cannot verify the form of the free energy.
- **Required correction** Provide the full equation.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Section II.5
- **Evidence pointer** "For comparison, we also compute the critical heterotypic scaffold–scaffold interaction for the corresponding binary (two-scaffold) incompressible Flory–Huggins model with solvent; the result is given in Eq. (A.6) (Appendix A)."
- **Issue** The text says "with solvent" but the Appendix A title says "in absence of any explicit solvent." This is contradictory.
- **Required correction** Clarify whether the binary model includes solvent or not, and ensure consistency between the main text and Appendix A.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Language
- **Affected element** Section II.1
- **Evidence pointer** "For simplicity, we will refer to these multicomponent Cas-Nck-N-WASP mixtures as Cas."
- **Issue** This simplification may cause confusion, as "Cas" is also used for the individual protein. Consider using a different notation for the mixture.
- **Required correction** Use a distinct label for the Cas-Nck-N-WASP mixture, such as "Cas complex" or "Cas/Nck/N-WASP."

## Risk / unsupported claims

- The claim that "FAK phosphorylation increases FAK intensity and decreases Cas intensity inside condensates" is unsupported without the actual data and figures.
- The claim that "adding paxillin increases FAK intensity and decreases Cas intensity inside condensates" is unsupported without the actual data and figures.
- The claim that "client recruitment alone tunes proximity to criticality and reshapes condensate composition" is not quantitatively supported by the experimental evidence presented.
- The claim that "experiments confirm our theory that PXN decrease the critical point of condensation" is not supported by the qualitative description provided.
- The claim that the theoretical framework "reveals distinct yet convergent physical routes" is not fully supported, as the theoretical derivations are incomplete and the connection to experimental observations is not quantitatively established.
- The generalizability of the findings to other multicomponent condensate systems is asserted but not demonstrated or discussed in sufficient depth.