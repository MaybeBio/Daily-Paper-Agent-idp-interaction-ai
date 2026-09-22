## Review setup
- **Input scope** Full manuscript text (main text, methods, and references) as provided.
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by the presented evidence. No line numbers were provided; all pointers refer to section or figure names.
- **Shared manuscript claim summary** The authors introduce a minimal coarse-grained "ABC" model to study how sequence complexity (quantified by word entropy H3) and monomer bending rigidity (ϵb) control the morphology and aging dynamics of protein aggregates. They report that flexible, low-complexity sequences form ergodic liquid-like droplets; increasing rigidity drives a sharp transition to ordered, fibril-like structures; high-complexity sequences form amorphous, glassy aggregates that exhibit aging; and aging dynamics follow stretched exponential relaxation with relaxation times that grow with waiting time.
- **Visible evidence base** Main text figures (Figs. 1–8) are referenced; Methods section describes the model, simulation parameters, and analysis procedures. Specific numerical data, simulation trajectories, and supplementary figures are referenced but not provided in the submitted material.
- **Missing materials affecting confidence** Supplementary Information (SI) sections I–III are referenced but not included. Raw simulation data, convergence checks, finite-size analyses, and quantitative error bars for key observables (e.g., nematic order parameter, relaxation times) are not provided. Details of the sequence shuffling algorithm and the exact definition of the word entropy calculation are incomplete.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question: how sequence complexity and monomer rigidity jointly determine the morphology and aging dynamics of protein aggregates. The minimal ABC model is elegant and the qualitative findings—particularly the rigidity-driven disorder-to-order transition and the contrast between ergodic and aging dynamics—are potentially of broad interest. However, the current evidence base is insufficient to fully establish the central claims. Key quantitative results (e.g., aging exponents, relaxation times, order parameters) are presented without error bars or convergence analysis, and the connection to experimental systems (e.g., FUS condensates, RNA repeats) is largely qualitative. The manuscript would benefit from additional validation of the model's robustness and a more quantitative comparison with experimental observables.
- **Who would be interested in the results, and why** Researchers in the fields of protein aggregation, phase separation, biophysics of intrinsically disordered proteins, and soft condensed matter physics. The work provides a conceptual framework linking sequence features to aggregate morphology and dynamics, which could inform experimental studies of condensate aging and fibril formation. The minimal model approach may also appeal to theorists interested in coarse-grained models of biological self-assembly.
- **Major strengths** 1. The minimal ABC model is conceptually clear and captures a wide range of behaviors (liquid, fibril, glass) with a small parameter set. 2. The distinction between ergodic and aging dynamics via the pMSD and overlap function is a valuable methodological contribution. 3. The predicted rigidity-driven transition from liquid to ordered fibrils for low-complexity sequences is a striking and testable result. 4. The discussion connecting the findings to IDPs and RNA repeats provides useful context and potential experimental relevance.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative robustness), R1-M2 (model validation), R1-M3 (experimental connection), R1-M4 (methodological transparency).
- **Assessment against Nature-style criteria**  
  - *Originality*: High. The combination of sequence complexity and rigidity as control parameters for aggregate morphology and aging is a novel angle.  
  - *Scientific importance*: Moderate to high. The findings could have implications for understanding protein condensate aging and fibril formation, but the current evidence is largely from a simplified model.  
  - *Interdisciplinary readership*: Moderate. The topic bridges biophysics, polymer physics, and soft matter, but the presentation may be too specialized for a general audience.  
  - *Technical soundness*: Currently insufficient. Key claims lack quantitative validation and error analysis.  
  - *Readability for nonspecialists*: The main text is generally clear, but some technical details (e.g., pMSD, overlap function) may be challenging for readers outside the field.  
- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual framework is promising, but the current evidence does not fully establish the quantitative claims.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Quantitative robustness  
- **Claim pointer** The manuscript claims specific values for the stretched exponential exponent β (e.g., β = 0.20 for ϵb = 0) and the aging exponent μ (e.g., μ ≈ 0.24 for H3 = 4.75 at ϵb = 0, and μ = 1.14 for H3 = 1.58 at ϵb = 4).  
- **Evidence pointer** Figures 3–6; location not provided  
- **Concern** The reported exponents are presented without error bars, confidence intervals, or details on the fitting procedure. It is unclear how many independent simulations were performed, how the fits were weighted, and whether the exponents are stable across different system sizes or initial conditions. The claim that μ = 1.14 exceeds unity is particularly striking and would require strong statistical support.  
- **Why it matters** The central distinction between ergodic and aging behavior, and the claim that rigidity can produce aging exponents greater than unity, rest on these quantitative values. Without error analysis, the reader cannot assess whether the differences between conditions are significant.  
- **Resolution test** Provide error bars or confidence intervals for all reported exponents, describe the fitting procedure in detail, and show that the results are robust to changes in system size, simulation length, and initial conditions.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Model validation  
- **Claim pointer** The manuscript states that "flexible monomers with low sequence complexity form liquid-like droplets that exhibit ergodic behavior" and that increasing rigidity leads to "an abrupt transition to more ordered structures, reminiscent of amyloid fibrils."  
- **Evidence pointer** Figures 1–2; location not provided  
- **Concern** The model uses a highly simplified interaction scheme (identical attractive interactions between like beads, repulsive between unlike). It is not demonstrated that the observed behaviors are robust to reasonable variations in the interaction parameters (e.g., the strength of attraction ϵ, the range of the potential, or the specific form of the angle potential). The claim of an "abrupt" transition is based on a limited set of ϵb values (0, 2, 4); a finer scan would be needed to establish whether the transition is truly discontinuous.  
- **Why it matters** The model's predictive value depends on its robustness to parameter choices. If the qualitative behaviors (liquid, fibril, glass) are only observed for a narrow parameter range, the general conclusions about sequence complexity and rigidity would be weakened.  
- **Resolution test** Perform a systematic parameter scan (e.g., varying ϵ, the interaction range, and the angle potential form) and show that the qualitative phase behavior is preserved. For the claimed abrupt transition, provide a finer scan of ϵb and quantify the sharpness of the change in order parameter.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Experimental connection  
- **Claim pointer** The manuscript states that "our findings underscore the influence of the monomer characteristics in shaping the morphology and dynamics of protein aggregates" and draws connections to FUS condensates and RNA repeats.  
- **Evidence pointer** Discussion section; location not provided  
- **Concern** The connection to experimental systems is qualitative. For example, the claim that FUS_LC has a "sufficiently high" H3 value to predict liquid-like behavior followed by aging is not quantified. The model's parameters (e.g., ϵb, ϵ) are not mapped to physical properties of real proteins or RNA. The comparison with experimental aging exponents (e.g., from Jawerth et al.) is not quantitative.  
- **Why it matters** The broader significance of the work depends on its relevance to experimental observations. Without a clear mapping between model parameters and experimental conditions, the predictions are difficult to test.  
- **Resolution test** Provide a quantitative comparison with at least one experimental system (e.g., estimate H3 for a set of IDPs and compare predicted vs. observed behavior). Discuss how ϵb could be related to measurable quantities such as persistence length or secondary structure propensity.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Methodological transparency  
- **Claim pointer** The manuscript describes the sequence generation procedure as "shuffling the sequence, accepting mutations that increase the H3 value" until H3 = 4.75.  
- **Evidence pointer** Methods section, "Sequence generation"; location not provided  
- **Concern** The details of the shuffling algorithm are incomplete. It is unclear how many shuffling steps were performed, whether the procedure was repeated to generate multiple independent high-complexity sequences, and whether the resulting sequences have any unintended biases (e.g., in monomer composition or local sequence patterns).  
- **Why it matters** The reproducibility of the results depends on a complete description of the sequence generation. If the high-complexity sequences are not representative of the ensemble of sequences with H3 = 4.75, the conclusions may be sequence-specific.  
- **Resolution test** Provide a complete description of the shuffling algorithm, including the number of independent sequences generated, the acceptance criteria, and a check for unintended biases (e.g., comparing results across multiple independent high-complexity sequences).

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Definition of word entropy  
- **Evidence pointer** Section "Word Complexity"; location not provided  
- **Issue** The definition of H3 is given in words, but the exact formula (Eq. 1) is not displayed in the provided text. The reader is left to infer the precise definition.  
- **Required correction** Display Eq. 1 explicitly and define all symbols (e.g., p_i^(n), the base of the logarithm).

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Terminology  
- **Affected element** Use of "aging"  
- **Evidence pointer** Throughout; location not provided  
- **Issue** The term "aging" is used to describe both the increase in relaxation time with waiting time and the general evolution of the aggregate structure. This dual usage could be confusing.  
- **Required correction** Clarify the distinction between "physical aging" (time-dependent material properties) and "structural evolution" (changes in morphology over time).

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Presentation  
- **Affected element** Figure captions  
- **Evidence pointer** Figures 1–8; location not provided  
- **Issue** The figure captions are not provided in the submitted text. It is difficult to fully interpret the figures without captions.  
- **Required correction** Ensure that all figure captions are included and provide sufficient detail to interpret the data.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Consistency  
- **Affected element** Terminology for "monomer rigidity"  
- **Evidence pointer** Throughout; location not provided  
- **Issue** The manuscript uses "monomer rigidity" and "bending rigidity" interchangeably. It would be clearer to use a single term consistently.  
- **Required correction** Choose one term (e.g., "bending rigidity") and use it consistently throughout.

- **Concern ID** R1-m5  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** SI references  
- **Evidence pointer** Sections I–III of SI; location not provided  
- **Issue** The manuscript references SI sections for additional data (e.g., pMSD for non-zero ϵb, trap model connection), but the SI is not provided. This limits the reader's ability to verify the claims.  
- **Required correction** Ensure that the SI is available to reviewers and readers, or summarize the key SI results in the main text.

## Risk / unsupported claims
- The claim that "flexible monomers with low sequence complexity form liquid-like droplets that exhibit ergodic behavior" is supported by the presented data but lacks quantitative error analysis.
- The claim of an "abrupt transition" from disorder to order as ϵb increases for low-complexity sequences is not fully supported, as only three ϵb values are shown.
- The claim that "the aging dynamics in both the low and high complexity sequences are qualitatively similar" is based on stretched exponential fits but lacks statistical comparison.
- The prediction that FUS_LC has a "sufficiently high" H3 to form liquid-like droplets that subsequently age is not quantitatively supported.
- The connection between the model's aging exponents and experimental observations (e.g., Jawerth et al.) is qualitative and not rigorously established.
- The statement that "the pMSD exhibits scalies as τ^κ" (likely a typo for "scales") is unclear and should be corrected.