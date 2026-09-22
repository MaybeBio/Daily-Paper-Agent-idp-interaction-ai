## Review setup
- **Input scope** Full manuscript text (main text, methods, results, discussion, conclusions) without figures, tables, or supplementary materials.
- **Assessment boundary** Scientific content, technical soundness, clarity, and support for claims based solely on the provided text. No assessment of figures, tables, or supplementary data beyond what is described in the text.
- **Shared manuscript claim summary** The authors present an analytical formulation and field-theoretic simulation (FTS) framework for sequence-specific liquid-liquid phase separation (LLPS) of proteinlike heteropolymers, extending prior random phase approximation (RPA) and FTS approaches for long-range electrostatic interactions to include short-range, hydrophobic-like interactions. The theory uses eigenvalue decomposition of pairwise residue-residue contact energy matrices to define nonelectric charges, incorporates these into a statistical field theory, and applies both a mean-field approximation (yielding an effective Flory χ parameter) and full FTS to predict LLPS behavior. The approach is tested on Ddx4 IDR variants and model hydrophobic-polar sequences, with validation against coarse-grained explicit-chain molecular dynamics simulations.
- **Visible evidence base** Main text only. No figures, tables, or supplementary materials were provided. Equations are referenced but not fully displayed in the provided text.
- **Missing materials affecting confidence** Figures 1–13, all tables, supplementary materials, and full equation derivations are not available. This significantly limits the ability to verify quantitative claims, assess the accuracy of approximations, and evaluate the comparison between theory and simulation.

## Reviewer
- **Overall assessment** This manuscript presents a theoretically ambitious and potentially valuable extension of field-theoretic methods to include short-range interactions in models of biomolecular LLPS. The conceptual framework, combining eigenvalue decomposition of interaction matrices with RPA and FTS, is novel and could provide a computationally efficient complement to explicit-chain simulations. However, the current submission has several significant issues that must be addressed before the case is fully established. The absence of figures and tables makes it impossible to verify the quantitative results and the claimed agreement with simulations. The presentation is dense and at times unclear, particularly in the methods section, and the authors do not adequately address the limitations of their approach, especially the restriction to Yukawa potentials and the treatment of excluded volume. The validation against experiments is indirect and relies on comparisons with other simulation studies. Overall, the work is promising but requires substantial revision and additional analysis to meet the standards of a rigorous theoretical contribution.
- **Who would be interested in the results, and why** Researchers in the fields of biophysics, polymer physics, and computational biology, particularly those studying biomolecular condensates, LLPS, and intrinsically disordered proteins. The work offers a new theoretical tool that could be used to screen sequence variants for LLPS propensity and to understand the physical principles governing sequence-encoded phase behavior. The methodological developments may also interest theorists working on field-theoretic descriptions of polymers and soft matter.
- **Major strengths** The conceptual advance of incorporating short-range interactions into a field-theoretic framework for LLPS is significant and timely. The use of eigenvalue decomposition to systematically reduce the complexity of interaction matrices is elegant and computationally appealing. The authors demonstrate the flexibility of their approach by applying it to multiple interaction schemes and sequence types. The comparison with explicit-chain MD simulations, even if only described qualitatively in the text, is an important step for validation.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that their FTS approach "provides full sequence dependence for both short- and long-range interactions" and that the mean-field approximation is "useful as a computationally efficient tool" for studying IDP LLPS.
  - **Evidence pointer** Methods section, FTS subsection; Results section, analytical and FTS applications.
  - **Concern** The manuscript does not provide sufficient detail on the numerical implementation of the FTS, including the choice of simulation parameters, convergence criteria, and error estimates. The authors mention using a semi-implicit integration scheme but do not discuss the stability or accuracy of the method for the systems studied. Furthermore, the claim of "full sequence dependence" is not adequately demonstrated, as the FTS results are only shown for three short model sequences and the Ddx4 variants are only treated with the mean-field approximation. The text does not provide quantitative evidence, such as convergence tests or comparison of FTS results with known exact limits, to support the reliability of the method.
  - **Why it matters** Without a clear demonstration of the numerical robustness and accuracy of the FTS, the central methodological claim of the paper is not fully supported. Readers cannot assess whether the observed sequence-dependent effects are genuine physical predictions or artifacts of the numerical scheme.
  - **Resolution test** The authors should provide a detailed description of the numerical implementation, including convergence tests with respect to grid size, time step, and simulation length. They should also present a validation of the FTS against a known analytical result or a benchmark problem, and ideally show FTS results for the Ddx4 variants to directly support the claim of full sequence dependence.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors state that the mean-field approximation leads to an effective Flory χ parameter that "accounts for the contact-interaction effects of amino acid composition" and that this approach is validated by comparison with explicit-chain MD simulations.
  - **Evidence pointer** Results section, analytical results for Ddx4 variants; Figures 6, 7, 11, 12 (not available).
  - **Concern** The comparison between the mean-field/RPA theory and explicit-chain MD is only described qualitatively in the text. The authors state that results are "largely consistent" but do not provide quantitative measures of agreement, such as differences in critical temperatures or coexistence curves. Moreover, the mean-field treatment of short-range interactions via a single χ parameter may be a significant oversimplification, as it neglects sequence-specific correlations that could be important for LLPS. The authors do not discuss the limitations of this approximation or provide criteria for when it is expected to be valid.
  - **Why it matters** The validity of the mean-field approximation is central to the claim that the theory is a useful screening tool. Without a quantitative assessment of its accuracy, the practical utility of the approach is unclear.
  - **Resolution test** The authors should provide a quantitative comparison between the mean-field/RPA predictions and the explicit-chain MD results, including numerical values for critical temperatures, coexistence densities, and a discussion of discrepancies. They should also discuss the expected range of validity of the mean-field approximation and, if possible, compare it with more accurate treatments for at least one test case.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The authors state that their theory "provides a computationally efficient approach for exploring sequence-dependent LLPS" and that it can be used to "screen large numbers of sequence variants."
  - **Evidence pointer** Conclusions section.
  - **Concern** While the computational efficiency of the mean-field approach is plausible, the manuscript does not provide any benchmarking data on computational cost or a demonstration of the method's scalability to larger systems or sequence libraries. The FTS approach, as described, appears to be computationally intensive and may not be practical for high-throughput screening. The authors do not discuss the computational complexity of their algorithms or compare them with existing methods.
  - **Why it matters** The claimed practical advantage of the method is a key selling point. Without evidence of its efficiency, the impact of the work is diminished.
  - **Resolution test** The authors should provide a benchmark of computational cost for the mean-field and FTS methods, including scaling with system size and sequence length. They should also discuss the potential for optimization and compare the efficiency with existing approaches, such as explicit-chain simulations or other analytical theories.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** The authors restrict their FTS to Yukawa potentials for short-range interactions, stating that this is a "first step" and that other forms should be explored in the future.
  - **Evidence pointer** Methods section, FTS subsection; Conclusions.
  - **Concern** The restriction to Yukawa potentials is a significant limitation, as real hydrophobic and π-related interactions are not well-represented by a single Yukawa form. The authors do not discuss how their results might depend on this choice or whether the qualitative conclusions are robust to changes in the potential form. The comparison with explicit-chain MD, which uses different potential forms (Lennard-Jones, Wang-Frenkel), is therefore not a direct test of the FTS approach.
  - **Why it matters** The generality of the proposed framework is questionable if it is only applicable to a narrow class of potentials. The authors need to justify the use of Yukawa potentials and discuss the implications for the applicability of their method.
  - **Resolution test** The authors should discuss the physical rationale for choosing Yukawa potentials and, ideally, perform a sensitivity analysis by testing at least one alternative potential form. They should also clarify whether the framework can be extended to other potentials and what modifications would be required.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability
  - **Affected element** Introduction and Methods
  - **Evidence pointer** Introduction, Models and Methods.
  - **Issue** The manuscript is dense and assumes a high level of familiarity with field-theoretic methods. The introduction could better motivate the need for the new approach by more clearly contrasting it with existing methods and highlighting the specific limitations being addressed.
  - **Required correction** Add a brief, accessible summary of the key innovations and a roadmap of the paper at the end of the introduction. Consider adding a short appendix or glossary for non-specialist readers.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Methods, Statistical Field Theory
  - **Evidence pointer** Equations (5)–(20).
  - **Issue** The derivation of the statistical field theory is presented in a highly condensed form. Several steps are not fully explained, and the notation is sometimes ambiguous (e.g., the use of \( \breve{\phi} \) for smeared fields is introduced but not consistently used).
  - **Required correction** Expand the derivation to include intermediate steps and clarify the notation. Define all symbols clearly at first use.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Results, Ddx4 analysis
  - **Evidence pointer** Section on analytical results for Ddx4 variants.
  - **Issue** The authors discuss the rank ordering of LLPS propensities for different Ddx4 variants but do not provide a clear explanation for why the ordering differs between interaction schemes. The discussion of the underlying physical mechanisms is brief.
  - **Required correction** Expand the discussion to provide a more detailed physical interpretation of the results, including the role of specific residue interactions and how they differ across schemes.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Results, FTS for LS sequences
  - **Evidence pointer** Section on FTS for LS sequences.
  - **Issue** The authors state that the FTS results are consistent with explicit-chain MD but do not provide a detailed comparison of the internal structure of the condensates, which is a key prediction of the FTS.
  - **Required correction** Provide a more detailed comparison of the condensate structure, such as radial density profiles or cluster size distributions, to strengthen the validation.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Conclusions
  - **Evidence pointer** Conclusions section.
  - **Issue** The conclusions are somewhat general and do not clearly summarize the specific new insights gained from the applications of the theory.
  - **Required correction** Summarize the key findings from the Ddx4 and LS sequence applications and state the main limitations and future directions more concretely.

- **Technical failings that need to be addressed before the case is established** R1-M1 (numerical implementation and validation of FTS), R1-M2 (quantitative comparison with MD), R1-M4 (justification of Yukawa potential restriction). These are the primary technical issues that prevent the manuscript from being fully convincing.

- **Assessment against Nature-style criteria** 
  - **Originality** The work is original in its extension of field-theoretic methods to include short-range interactions in a sequence-dependent manner. The eigenvalue decomposition approach is a creative solution to a challenging problem.
  - **Scientific importance** The topic is of high importance given the widespread interest in biomolecular condensates and the need for predictive theoretical tools. The potential for efficient sequence screening is significant.
  - **Interdisciplinary readership** The work will appeal to biophysicists, polymer physicists, and computational biologists. However, the presentation is likely too technical for a broader biological audience.
  - **Technical soundness** The theoretical framework is sound in principle, but the lack of numerical details and quantitative validation prevents a full assessment. The restriction to Yukawa potentials is a concern.
  - **Readability for nonspecialists** The manuscript is not accessible to nonspecialists. The introduction and methods are dense and assume significant prior knowledge.

- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the work has the potential to be a valuable contribution. However, the manuscript in its current form does not fully establish the validity and utility of the proposed methods. The authors must address the major concerns, particularly the numerical implementation and validation, before the case is made.

## Risk / unsupported claims
- The claim that FTS provides "full sequence dependence" is not supported by the evidence presented, as FTS is only applied to short model sequences and not to the Ddx4 variants.
- The claim that the mean-field/RPA approach is "computationally efficient" is plausible but not quantified.
- The claim that the theory can be used to "screen large numbers of sequence variants" is speculative and not demonstrated.
- The qualitative statement that FTS and MD results are "consistent" is not supported by quantitative data.
- The assertion that the eigenvalue decomposition is "reasonably accurate" for the interaction schemes considered is based on figures that are not available for review.