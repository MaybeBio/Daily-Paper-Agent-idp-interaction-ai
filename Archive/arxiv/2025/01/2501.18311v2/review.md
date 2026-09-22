## Review setup
- **Input scope** Full manuscript text (review article)
- **Assessment boundary** Scientific content, theoretical framework, comprehensiveness, and clarity of the review; no assessment of typesetting or final journal formatting
- **Shared manuscript claim summary** This review synthesizes theoretical and simulation studies on how membrane proteins sense and generate membrane curvature, covering isotropic proteins, anisotropic (e.g., BAR-domain) proteins, intrinsically disordered protein domains, and nanoparticle adhesion, with emphasis on equilibrium mean-field theories and relevant simulation results.
- **Visible evidence base** Full text of the manuscript, including equations, figure captions, and references; no figures or supplementary materials were provided
- **Missing materials affecting confidence** Figures and their data (Figs. 1–14) were not available for inspection; supplementary information, if any, was not provided; full reference list with complete citations was not available for verification

## Reviewer
- **Overall assessment** This is a well-structured and technically competent review of theoretical approaches to membrane curvature sensing and generation by proteins. The author, a recognized contributor to this field, provides a coherent framework that unifies isotropic and anisotropic protein models, discusses the role of IDP domains, and connects theory to simulation and experiment. The review is timely and will be useful to researchers in biophysics, cell biology, and soft matter. However, the review is largely a synthesis of the author's own body of work, which raises questions about balance and coverage of alternative viewpoints. The absence of figures in the provided material limits full evaluation of pedagogical clarity. The manuscript is suitable for publication in a specialist journal like Soft Matter, but its scope and depth are not aligned with the broad interdisciplinary impact expected of a Nature-level review.

- **Who would be interested in the results, and why** Researchers in membrane biophysics, computational biology, and soft matter physics will find this review valuable as a consolidated reference on mean-field theories of protein-membrane interactions. Cell biologists studying endocytosis, vesicle trafficking, and organelle morphology may also benefit from the conceptual frameworks presented. The review provides a useful entry point for graduate students and postdocs entering the field, as it systematically organizes theoretical models and connects them to experimental observables such as curvature-sensing ratios and tethered vesicle measurements.

- **Major strengths**
  1. The review provides a clear and logical organization, progressing from membrane elasticity fundamentals to isotropic proteins, IDP domains, anisotropic proteins, and finally to curvature generation and nanoparticle adhesion.
  2. The theoretical framework is presented with appropriate mathematical rigor, including key equations for bending energy, protein density distributions, and force-balance relations.
  3. The connection between theory, simulation, and experiment is well articulated, particularly in the discussion of tethered vesicle experiments and the estimation of protein bending parameters.
  4. The review identifies important open questions and practical recommendations, such as the need for comparisons between cylindrical and spherical geometries to extract Gaussian curvature effects.
  5. The discussion of IDP domains and their role in modulating membrane properties is timely and adds a modern perspective.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** No
  - **Axis** Balance and comprehensiveness
  - **Claim pointer** The review claims to describe "the recent theoretical development in membrane remodeling performed by membrane proteins" and covers mean-field theories and simulation results.
  - **Evidence pointer** Sections I–V; reference list
  - **Concern** The review draws very heavily on the author's own publications (Noguchi 2014, 2015, 2016a, 2016b, 2019a, 2019b, 2021a, 2021b, 2022a, 2022b, 2023, 2025a, 2025b, and others). While this ensures technical depth, it risks presenting a one-sided view of the field. Alternative theoretical approaches, such as elastic models by other groups (e.g., Kozlov, Baumgart, or Bassereau collaborations), are mentioned but not critically compared or evaluated in depth.
  - **Why it matters** A review should provide a balanced assessment of the field to be a reliable reference. Over-reliance on a single research program may limit the review's utility and credibility for readers seeking a comprehensive understanding of competing or complementary frameworks.
  - **Resolution test** The author should expand the discussion of alternative theoretical models and explicitly compare predictions, assumptions, and limitations across different approaches. A table summarizing key models and their predictions would be helpful.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Experimental validation and quantitative comparison
  - **Claim pointer** The review states that tethered vesicle experiments can be used to estimate protein bending properties and that the theory "well reproduces the simulation results for crescent protein rods on a membrane tube."
  - **Evidence pointer** Section III.4; Fig. 6 (not available); Fig. 7
  - **Concern** While the review discusses the estimation of protein bending parameters from tethered vesicle experiments, the quantitative agreement between theory and experiment is not systematically presented. For example, the fitted values of κ_p and C_p for I-BAR domains are given, but the uncertainty, robustness, and model-dependence of these estimates are not discussed. The review would benefit from a critical assessment of how well the mean-field models actually predict experimental data across different protein types and conditions.
  - **Why it matters** The practical utility of the theoretical framework depends on its ability to make quantitative predictions that can be tested experimentally. Without a critical evaluation of the agreement between theory and experiment, readers cannot judge the reliability of the proposed models.
  - **Resolution test** Add a dedicated subsection or table comparing theoretical predictions with experimental measurements for multiple proteins, including error estimates and discussion of model limitations.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Coverage of non-equilibrium and dynamic phenomena
  - **Claim pointer** The review states it "focuses on the theoretical studies of protein behaviors with emphasis on thermal equilibrium and relaxation to the equilibrium" and explicitly excludes non-equilibrium dynamics.
  - **Evidence pointer** Section I
  - **Concern** The exclusion of non-equilibrium dynamics is acknowledged, but the review does not provide a forward-looking discussion of how non-equilibrium effects (e.g., active processes, ATP-driven remodeling, protein aggregation kinetics) might alter the equilibrium predictions presented. Given that many cellular processes involving membrane remodeling are inherently non-equilibrium, a brief outlook on this frontier would strengthen the review's relevance.
  - **Why it matters** Readers interested in cellular contexts may find the equilibrium-only focus limiting. A short discussion of open challenges in non-equilibrium membrane remodeling would make the review more forward-looking and useful.
  - **Resolution test** Add a paragraph in the Summary and Outlook section discussing the potential impact of non-equilibrium effects and identifying key open questions for future research.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity and accessibility
  - **Affected element** Section II, Eq. (1)
  - **Evidence pointer** Section II
  - **Issue** The Canham–Helfrich energy is introduced with minimal physical motivation. Readers unfamiliar with membrane elasticity may struggle to understand the physical meaning of the spontaneous curvature and the Gaussian curvature term.
  - **Required correction** Add a brief physical explanation of each term in the bending energy, possibly with a simple schematic or intuitive description of the meanings of mean and Gaussian curvature.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility and parameter definitions
  - **Affected element** Section III.3, Eqs. (25)–(28)
  - **Evidence pointer** Section III.3
  - **Issue** The parameters in the free energy expression for anisotropic proteins (e.g., the excluded volume interaction parameters) are not all explicitly defined in the text. Some are only described in the context of the equations.
  - **Required correction** Provide a table or list defining all symbols and parameters used in the key equations, including their physical meaning and typical values where available.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Figure accessibility
  - **Affected element** Figures 1–14
  - **Evidence pointer** Figure captions (not available in the provided material)
  - **Issue** The figure captions were not provided in the manuscript text, making it impossible to assess whether the figures are well-designed and informative.
  - **Required correction** Ensure that all figures are self-contained with detailed captions that explain the key findings and how they relate to the theoretical models discussed.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Terminology consistency
  - **Affected element** Section III.1 and Section IV.1
  - **Evidence pointer** Sections III.1, IV.1
  - **Issue** The terms "sensing curvature" and "generation curvature" are introduced, but the distinction between them could be made clearer, especially for readers new to the field.
  - **Required correction** Add a brief definition or schematic explaining the difference between curvature sensing and curvature generation, and how they relate to the free energy landscape.

- **Technical failings that need to be addressed before the case is established** None identified from the supplied material. The theoretical derivations appear internally consistent, and the equations are presented with appropriate context. However, the absence of figures and full reference details limits a complete technical assessment.

## Risk / unsupported claims
- The claim that "the theory well reproduces the simulation results for crescent protein rods on a membrane tube" (Section III.3) cannot be fully verified without access to the referenced figures and simulation data.
- The statement that "the same type of protein rods exhibit a membrane-mediated attractive interaction when aligned side-by-side" (Section IV.2) is presented as established but relies on simulation results not shown in the provided material.
- The quantitative estimates of protein bending properties (e.g., κ_p = 82 k_B T for I-BAR domains) are presented without discussion of uncertainty or model dependence, which could be misinterpreted as more definitive than warranted.
- The review's claim to cover "recent theoretical development" is somewhat undermined by the heavy reliance on the author's own work, potentially omitting significant contributions from other groups.