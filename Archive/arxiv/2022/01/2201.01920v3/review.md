## Review setup
- **Input scope** Full manuscript text (book chapter, Methods in Molecular Biology format)
- **Assessment boundary** Scientific content, methodological clarity, reproducibility of described numerical techniques, and alignment with stated aims as a practical guide
- **Shared manuscript claim summary** The chapter provides a practical guide to numerical techniques for applying analytical theories (Flory-Huggins, RPA, rG-RPA) and field-theoretic simulation (FTS) to sequence-dependent liquid-liquid phase separation (LLPS) of intrinsically disordered proteins (IDPs), with a brief outline of coarse-grained molecular dynamics (CG-MD) methods. It includes software links, step-by-step protocols, and example calculations.
- **Visible evidence base** Full text including abstract, introduction, sections 2–5, equations, figure captions, and references. No figures or supplementary materials were provided for direct inspection.

## Reviewer
- **Overall assessment** This is a well-structured methods chapter that fills a genuine niche: translating analytical polymer theory into actionable numerical workflows for the LLPS community. The authors are clearly expert, and the chapter benefits from their direct involvement in developing the theories and code described. The writing is generally clear, and the practical guides (e.g., pseudocode, Jupyter notebook instructions) are a strong feature. However, the chapter's utility as a "practical guide" is partially undermined by insufficient detail on numerical implementation (e.g., convergence criteria, parameter sensitivity, error handling) and by a lack of validation metrics for the example calculations. The FTS section is the strongest, while the CG-MD section is too brief to be actionable. The chapter would be improved by adding troubleshooting guidance, benchmark comparisons, and clearer statements of limitations.

- **Who would be interested in the results, and why** Researchers entering the field of biomolecular condensates who wish to apply analytical or field-theoretic methods without deriving them from scratch. This includes computational biophysicists, physical chemists, and experimentalists seeking theoretical context for sequence-dependent phase behavior. The chapter is also useful for established theorists who want a consolidated reference to the authors' software and methods. The practical guides and code links make it particularly attractive to graduate students and postdocs.

- **Major strengths**
  1. The chapter addresses a real gap: most reviews cover theory or simulation, but few provide hands-on numerical recipes. The authors' direct involvement in the methods ensures accuracy.
  2. The step-by-step pseudocode for spinodal and binodal construction (Section 2) is clear and transferable to other free energy functions.
  3. The FTS section (Section 3) is technically detailed, with explicit equations, discretization choices, and parameter values (e.g., M=32, Δx=ā=b/√6), making it reproducible.
  4. The inclusion of software links (GitHub) and a Jupyter notebook guide is exemplary for a methods chapter.
  5. The chapter honestly notes limitations of RPA (e.g., overestimation of phase separation propensity) and contextualizes FTS as a more accurate alternative.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The chapter claims to be a "practical guide" with "step-by-step practical guides" (Section 1.6) and provides pseudocode and software links, but the numerical implementation details are insufficient for a reader to reproduce the results without significant trial and error.
- **Evidence pointer** Section 2.1 (pseudocode for critical point), Section 3.4 (FTS parameter choices), Section 3.6 (practical guide)
- **Concern** The pseudocode for finding the critical point (Section 2.1) is too high-level. It does not specify: (i) the initial guess strategy for the root-finding, (ii) the tolerance for convergence, (iii) how to handle multiple roots or non-convergence, or (iv) how the minimization of u(rho) is performed (e.g., which algorithm, bounds). Similarly, the FTS section states parameter values but does not discuss how these were chosen or how sensitive the results are to them. For example, the choice of Δt=0.01 for CL integration is stated without justification; a reader using a different system might not know if this is stable. The chapter would be far more useful if it included: (a) a table of recommended parameter ranges, (b) convergence diagnostics (e.g., how to check CL equilibration), and (c) common failure modes and troubleshooting tips.
- **Why it matters** A methods chapter's primary value is reproducibility. Without these details, readers may abandon the methods after encountering numerical difficulties, defeating the chapter's purpose. The authors' expertise makes them uniquely positioned to provide this guidance, and its absence is a missed opportunity.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Validation
- **Claim pointer** The chapter presents example calculations (Figures 5–8) but does not provide quantitative validation of the numerical results against known benchmarks or experimental data.
- **Evidence pointer** Section 3.4 (Figure 5), Section 3.5 (Figures 6–7), Section 3.7 (Figure 8)
- **Concern** The figures show phase diagrams and correlation functions, but there is no discussion of: (i) how the numerical results compare to exact solutions (where available), (ii) the statistical error bars on the FTS results (only standard deviations are mentioned for correlation functions), or (iii) how the choice of lattice size M, box size, or number of CL steps affects the results. For a methods chapter, a convergence study (e.g., phase boundary vs. M or Δt) would be invaluable. Additionally, the comparison between FTS and RPA in Figures 6–7 is qualitative; a quantitative metric (e.g., percent difference in critical temperature) would help readers understand the magnitude of RPA's overestimation.
- **Why it matters** Without validation, readers cannot assess the accuracy of the methods or trust the example results. This is particularly important for FTS, where the sign problem and discretization errors can be subtle. A brief convergence analysis would substantially increase confidence in the methods.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scope and balance
- **Claim pointer** The chapter's title and introduction promise coverage of "analytical theories" and "field-theoretic simulation," with CG-MD "briefly outlined." However, the CG-MD section (Section 4) is so brief that it is not actionable, and the chapter does not clearly state what a reader should use when.
- **Evidence pointer** Section 4 (entire), Section 1.5
- **Concern** Section 4 covers the "slab" protocol in about two pages, with no equations for the CG model (e.g., the functional form of non-bonded interactions is not given, only references). The practical guide (Section 4.4) is a list of steps without specific parameter values (e.g., number of chains, box dimensions, temperature range, Lennard-Jones parameters). A reader cannot implement this method from the chapter alone. Either expand this section to match the detail of the FTS section, or explicitly state that it is a summary and direct readers to the original papers for full details. Additionally, the chapter lacks a comparative discussion of when to use RPA vs. FTS vs. CG-MD, which would be a valuable decision tree for newcomers.
- **Why it matters** The chapter's stated aim is to be a practical guide. An outline that is too brief to use is of limited value. The imbalance between sections may mislead readers into thinking CG-MD is less important or less mature than it is.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.1, Equation 5
- **Evidence pointer** "location not provided" (equation numbering in text)
- **Issue** The text states that det H = 0 defines the spinodal boundary, but the distinction between the spinodal and binodal for multi-component systems is not fully explained. A reader unfamiliar with the field might confuse the two.
- **Required correction** Add a brief paragraph clarifying the physical meaning of spinodal vs. binodal and why both are needed for a complete phase diagram.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section 3.6.1
- **Evidence pointer** "location not provided"
- **Issue** The guide for RPA code says "users may modify parameters in the main function" but does not list which parameters are most important or how they map to physical quantities (e.g., chain length N, charge sequence, excluded volume v).
- **Required correction** Add a table mapping code variables to physical parameters, with recommended ranges and units.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 3.7
- **Evidence pointer** "location not provided"
- **Issue** The correlation function definition in Equation 42 is given without a physical interpretation. The text jumps from definition to results.
- **Required correction** Add one or two sentences explaining what G_p,q(r) measures physically (e.g., "G_p,q(r) quantifies the likelihood of finding species q at distance r from species p, relative to the bulk density product").

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section 4.2
- **Evidence pointer** "location not provided"
- **Issue** The description of the "slab" protocol is dense and assumes familiarity with CG-MD conventions. Terms like "Langevin dynamics" and "NPT" are used without definition.
- **Required correction** Add a brief glossary or introductory paragraph for non-specialist readers, or add inline definitions.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Accuracy
- **Affected element** Section 1.2
- **Evidence pointer** "location not provided"
- **Issue** The text states that RPA "tends to predict higher LLPS propensities" than CG-MD, but does not quantify this or discuss exceptions. This is a strong claim that deserves more nuance.
- **Required correction** Add a sentence noting that the magnitude of overestimation depends on chain length, charge density, and salt concentration, with a reference to a systematic comparison.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1 (reproducibility of numerical methods) is the most critical. Without parameter guidance and troubleshooting, the chapter's core promise is not fully met.
  - R1-M2 (validation) is also important; a convergence study would strengthen confidence in the methods.
  - R1-M3 (CG-MD section too brief) is a scope issue that should be resolved by either expansion or explicit deferral.

- **Assessment against Nature-style criteria**
  - **Originality**: Moderate. The chapter does not present new science but consolidates existing methods into a practical guide. Its originality lies in the pedagogical structure and the explicit link between theory and code, which is uncommon in this field.
  - **Scientific importance**: High for the target audience. The methods described are widely used, and a reliable guide to their numerical implementation is valuable. The chapter also highlights important caveats (e.g., RPA overestimation, sensitivity to excluded volume) that are often underappreciated.
  - **Interdisciplinary readership**: The chapter is primarily aimed at biophysicists and physical chemists. It assumes familiarity with polymer theory and statistical mechanics, which limits its accessibility to a broader biological audience. The practical guides help, but the mathematical density is a barrier.
  - **Technical soundness**: The theory is sound, and the authors are authoritative. However, the lack of validation and convergence analysis (R1-M2) is a technical weakness. The numerical details are not fully specified (R1-M1), which is a reproducibility concern.
  - **Readability for nonspecialists**: The chapter is clearly written for specialists. The introduction is accessible, but Sections 2–4 require significant background. The practical guides are a positive feature but assume comfort with Python and command-line tools.

- **Recommendation posture** Supportive if technical concerns are resolved. The chapter is a valuable contribution that meets a real need. The major concerns (R1-M1, R1-M2) are addressable with additional content, and the minor comments are straightforward to implement. I recommend acceptance after revision, with the expectation that the authors add: (i) parameter tables and troubleshooting guidance, (ii) a convergence or validation study, and (iii) either expansion or explicit deferral of the CG-MD section.

## Risk / unsupported claims
- The claim that RPA "tends to predict higher LLPS propensities" than CG-MD (Section 1.2) is stated without quantitative support or caveats. This is a generalization that may not hold across all parameter regimes.
- The statement that FTS is "capable of accounting for concentration fluctuations in their entirety" (Section 1.3) is technically correct only within the limitations of the model Hamiltonian and discretization; the chapter later acknowledges this, but the initial claim is too strong.
- The chapter implies that the provided software is ready for "one button" use (e.g., "one button for all" scripts), but the need for parameter tuning (acknowledged in Section 2.4) suggests that significant user expertise is still required. This could mislead novice users.
- The CG-MD section (Section 4) is presented as a "brief outline," but the chapter does not clearly state that the described protocol is not a substitute for reading the original papers. A reader might attempt to implement the method from the chapter alone and fail due to missing details.