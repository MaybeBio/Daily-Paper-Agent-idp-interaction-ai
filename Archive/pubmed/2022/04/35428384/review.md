## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Theoretical framework and methodology for FRET-lines in single-molecule FRET experiments; no experimental data collection is presented
- **Shared manuscript claim summary** The authors present a general theoretical framework for analyzing conformational dynamics in single-molecule FRET experiments using two-dimensional histograms of FRET efficiency (E) and donor fluorescence lifetime (τD). They introduce "FRET-lines" as parametric reference curves that relate these observables for static and dynamic molecular systems, including treatment of flexible dye linkers and polymer models for disordered proteins. A moment-based representation is proposed to simplify graphical analysis of complex kinetic networks.
- **Visible evidence base** Full manuscript text including abstract, introduction, theory sections, conceptual derivations, practical applications, and conclusions; equations (1)-(70); figures referenced but not provided; supplementary material referenced but not provided
- **Missing materials affecting confidence** Figures 1-15 not provided; supplementary material (Notes 1-6) not provided; companion paper (Paper II) not provided; software repository and graphical user interface referenced but not evaluated

## Reviewer
- **Overall assessment** This manuscript presents a comprehensive theoretical framework for interpreting two-dimensional FRET efficiency versus donor lifetime histograms in single-molecule FRET experiments. The work addresses a genuine need in the field: the detection and visualization of fast conformational dynamics that are often missed by intensity-based analyses alone. The mathematical derivations appear internally consistent, and the moment-based representation offers a potentially useful simplification for graphical analysis. However, the manuscript is largely a synthesis and formalization of previously published concepts (e.g., Kalinin et al., Gopich and Szabo), and the novelty claim is not clearly articulated. The practical utility of the framework is demonstrated only through re-analysis of previously published data, which limits the strength of the validation. The manuscript is well-organized and generally readable, though the density of notation and derivations may challenge non-specialist readers.

- **Who would be interested in the results, and why** Researchers in single-molecule biophysics, particularly those using smFRET to study conformational dynamics of proteins and nucleic acids. The framework is directly relevant to practitioners analyzing multiparameter fluorescence detection data, especially those studying intrinsically disordered proteins, folding/unfolding transitions, and multi-state kinetic networks. The software tools provided could make the methods accessible to a broader community. The moment-based representation may also interest method developers in fluorescence spectroscopy.

- **Major strengths**
  1. Comprehensive and rigorous mathematical treatment of FRET-lines, unifying previously scattered concepts into a single framework.
  2. The moment-based representation provides a genuinely useful simplification for graphical analysis of complex kinetic networks.
  3. Treatment of flexible dye linkers and polymer models extends the framework to realistic experimental conditions.
  4. Clear practical guidance for applying the framework, including software availability.
  5. Well-structured presentation that builds logically from basic concepts to complex scenarios.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Originality
  - **Claim pointer** The manuscript claims to present "a general framework for analyzing dynamics that relates average fluorescence lifetimes and intensities in two-dimensional burst frequency histograms" and to provide "a rigorous framework for their calculation."
  - **Evidence pointer** Introduction, Section III (Concepts), Section IV (Practical Aspects)
  - **Concern** The novelty of the framework is not clearly established relative to prior work. The authors acknowledge that dynamic FRET-lines were "first introduced by Kalinin et al." and that "Gopich and Szabo later described analogous relations." The current manuscript appears to be a formalization and extension of these concepts, but the specific new contributions are not explicitly delineated. The treatment of flexible linkers and polymer models builds on prior work by the same group (e.g., Ref. 39, 76). Without a clear statement of what is genuinely new, the contribution may be viewed as incremental rather than transformative.
  - **Why it matters** For a methods paper, establishing novelty is essential. If the framework is primarily a synthesis of existing concepts, the contribution may be better framed as a review or tutorial rather than a new theoretical development. The journal's standards require clear articulation of what is new and why it matters.
  - **Resolution test** The authors should provide an explicit statement in the Introduction or Discussion identifying: (i) which elements of the framework are new, (ii) which are extensions of prior work, and (iii) which are pedagogical consolidations. This would allow readers to assess the incremental contribution.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The manuscript claims that "FRET-lines serve as reference curves for a graphical interpretation of experimental data to (i) identify conformational states, (ii) resolve their dynamic connectivity, (iii) compare different kinetic models, and (iv) infer polymer properties of unfolded or intrinsically disordered proteins."
  - **Evidence pointer** Abstract, Section III, Section IV
  - **Concern** The validation of the framework relies entirely on re-analysis of previously published data (Syntaxin-1, T4 lysozyme, p27). While this demonstrates applicability, it does not provide independent validation of the framework's predictions. The manuscript would be strengthened by including simulations that systematically test the accuracy and limitations of the FRET-line approach under controlled conditions. Additionally, the treatment of shot noise and its effect on the moment-based representation is mentioned but not quantitatively characterized.
  - **Why it matters** A theoretical framework must be validated to establish its reliability. Re-analysis of existing data can show consistency but cannot demonstrate that the framework correctly identifies dynamics that were not already known. Systematic simulations would provide stronger evidence for the framework's validity and help define its limitations.
  - **Resolution test** Include simulation studies that generate synthetic smFRET data with known kinetic parameters and test whether the FRET-line analysis correctly recovers those parameters. Quantify the accuracy of the moment-based representation as a function of photon count, number of states, and rate constants.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Readability for nonspecialists
  - **Claim pointer** The manuscript claims to provide "a simple graphical analysis of complex kinetic networks" and that the moment representation "enables a graphical analysis of complex kinetic networks, which can be performed 'by hand' without having to apply complex equations."
  - **Evidence pointer** Section III (Concepts), Section IV (Practical Aspects), Conclusions
  - **Concern** While the moment representation is indeed simpler than the full E-τD treatment, the manuscript does not provide a clear step-by-step protocol for how a practitioner would actually use the framework. The figures (not provided) presumably illustrate the concepts, but the text alone does not give sufficient guidance for implementation. The relationship between the moment representation and the physical parameters of interest (e.g., rate constants, populations) is not made explicit.
  - **Why it matters** The stated goal is to facilitate analysis by practitioners. If the framework is not presented in an accessible, actionable format, its adoption will be limited. The "by hand" claim is particularly strong and needs to be substantiated with a clear protocol.
  - **Resolution test** Add a dedicated section or boxed protocol that walks through the steps of applying FRET-line analysis to a typical dataset, including how to construct the moment representation, how to identify static versus dynamic populations, and how to extract kinetic information.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Section II (Theory), equations (1)-(5)
  - **Evidence pointer** Section II
  - **Issue** The derivation of the relationship between FRET efficiency and donor lifetime assumes a single donor-acceptor distance. The extension to distributions of distances is introduced later, but the transition is not clearly marked.
  - **Required correction** Add a sentence at the end of Section II noting that the equations apply to a fixed distance and that distributions will be treated in Section IV.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Section III (Concepts), subsection on multi-state systems
  - **Evidence pointer** Section III (Multi-state systems)
  - **Issue** The treatment of multi-state systems is brief and does not address how the number of states is determined from the data. The manuscript mentions that multi-state systems are described by an area rather than a line, but does not discuss how to identify the boundaries of this area or how to determine the number of states.
  - **Required correction** Add a discussion of model selection, including how to determine the number of states and how to assess the goodness of fit.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Section IV (Practical Aspects), subsection on experimental data
  - **Evidence pointer** Section IV (Application of FRET-lines to experimental data)
  - **Issue** The re-analysis of published data is described qualitatively. The specific parameters used (e.g., Förster radius, linker widths, correction factors) are not provided in the text.
  - **Required correction** Provide a table summarizing the parameters used for each example, or reference the original publications where these parameters are given.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Notation
  - **Affected element** Section III (Concepts), moment representation
  - **Evidence pointer** Section III (Alternative representation of dynamic lines)
  - **Issue** The notation for the moment representation (Γ) is introduced but not consistently used throughout the manuscript. In some places, the text refers to "moment difference" and in others to "Γ" without clear definition.
  - **Required correction** Define Γ once and use it consistently, or use descriptive terms throughout.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Section IV (Practical Aspects), subsection on dye-linker dynamics
  - **Evidence pointer** Section IV (Dye-linker dynamics)
  - **Issue** The treatment of dye-linker dynamics assumes that the linker dynamics are fast compared to the observation time. The manuscript does not discuss the case where linker dynamics are slow, which would require a different treatment.
  - **Required correction** Add a brief discussion of the limitations of the fast-linker assumption and how to identify cases where it may not hold.

## Risk / unsupported claims
- The claim that FRET-lines can "resolve their dynamic connectivity" (Abstract) is not fully supported by the presented theory, which provides reference curves but does not demonstrate a method for uniquely determining connectivity from experimental data.
- The claim that the moment representation enables analysis "by hand" is not substantiated with a concrete protocol.
- The statement that "no decrease of the dynamic shift is observed at increasing timescales of the dynamics" (Section III) is presented without quantitative support or reference to simulations.
- The assertion that "the choice of the distance distribution model function has only a minor effect on the shape of the static FRET-lines" (Section IV) is based on a single comparison (Gaussian vs. χ-distribution) and may not generalize to other models.
- The practical utility of the framework for distinguishing between different kinetic models is claimed but not demonstrated with examples where competing models are compared.
- The treatment of shot noise in the moment representation is mentioned but not quantitatively characterized; the claim that the moment representation is robust to shot noise is not supported.