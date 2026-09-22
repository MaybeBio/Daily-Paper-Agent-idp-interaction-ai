## Review setup

- **Input scope** Full manuscript text, including abstract, main text, figures (referenced), and supporting information description.
- **Assessment boundary** Scientific content, methodological soundness, validity of conclusions, and clarity of presentation as presented in the provided text. The review is based solely on the supplied material.
- **Shared manuscript claim summary** The manuscript argues that small-angle X-ray scattering (SAXS) molecular form factors (MFFs) cannot uniquely distinguish between homogeneous (homopolymer-like) and heterogeneous conformational ensembles of disordered proteins. Using coarse-grained simulations and a perturbative analytical theory, the authors demonstrate that certain heterogeneous ensembles can produce MFFs nearly identical to those of homopolymers, despite having significantly different conformational properties (e.g., R_EE distributions, asphericity). They conclude that SAXS data alone are insufficient to infer ensemble homogeneity and advocate for the use of complementary techniques.
- **Visible evidence base** The manuscript provides simulation results (coarse-grained C-alpha model) and analytical theory (perturbative expansion) for homopolymers and heteropolymers. Key evidence includes comparisons of MFFs, Kratky plots, pair distance distribution functions, and distributions of R_g and R_EE for various ensembles. Figures referenced include Figures 1-21 and Supporting Figures S1-S6.
- **Missing materials affecting confidence** The manuscript text was provided without the actual figures and figure captions. The review's assessment of the visual data (e.g., the degree of similarity between MFFs in Figures 7, 9, 10, 13) is therefore limited. The specific parameters for the simulations (e.g., chain length, number of samples, specific values of epsilon_p) are described but the quantitative details of the fitting procedures and error analysis are not fully detailed in the provided text. The Supporting Information is described but not provided.

## Reviewer

- **Overall assessment** This is a well-written and conceptually important paper that addresses a fundamental question in the biophysics of disordered proteins: the information content of SAXS data. The authors systematically demonstrate, using both simulation and theory, that the mapping from conformational ensemble to SAXS MFF is many-to-one. The construction of heterogeneous ensembles with MFFs nearly identical to homopolymers is a powerful and convincing result. The paper is likely to be of significant interest to the community and will stimulate further discussion on the interpretation of SAXS data. The main limitations are the lack of experimental validation and the reliance on a simplified coarse-grained model, which the authors acknowledge. The theoretical development, while a useful step, is limited to the perturbative regime.

- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins (IDPs), protein folding, and biophysical methods development would be the primary audience. The results are directly relevant to anyone using SAXS to characterize disordered states, as they challenge the common assumption that a homopolymer-like MFF implies a homogeneous ensemble. The paper will also be of interest to theorists and computational biophysicists working on polymer models and ensemble generation. The discussion on the interpretation of SAXS versus FRET data is particularly relevant.

- **Major strengths**
    1.  The central question is important and clearly articulated.
    2.  The methodology is rigorous, combining explicit-chain simulations with an analytical perturbative theory.
    3.  The demonstration of many-to-one mapping is compelling and well-illustrated with multiple examples (e.g., Figures 7, 9, 10, 13).
    4.  The paper provides a clear and balanced discussion of the implications for experimental data interpretation, including the limitations of using ν as a proxy for R_g.
    5.  The historical context and conceptual framing (e.g., the "near-Levinthal" scenario) are insightful and add value.

- **Major Concerns**

    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical Soundness
    - **Claim pointer** The manuscript claims that the analytical perturbative theory is a valid tool for exploring sequence-dependent MFFs and predicting R_g-R_EE decoupling in heteropolymers.
    - **Evidence pointer** Section "Approximate analytical theory for sequence-dependent MFFs of disordered heteropolymers", Equations 7-20, Figures 15-20.
    - **Concern** The perturbative theory is developed for short-range, contact-like interactions. The authors note that "subtle effects of polypeptide interactions cannot be addressed." However, the theory is then used to make predictions about sequence-dependent behavior and to guide the design of explicit-chain simulations. The validation of the theory is primarily against the same coarse-grained model it is meant to describe, and the comparison in Figure 15 shows a systematic offset for some quantities. The paper would be strengthened by a more explicit statement of the limitations of the theory, particularly regarding its applicability to real proteins where interactions are not purely contact-like and where solvent effects are significant. The claim that the theory provides a "glimpse of how various properties... might be encoded" is appropriately modest, but the potential for over-interpretation by readers is a concern.
    - **Why it matters** The analytical theory is a key novel contribution. If its limitations are not clearly defined, it could be misapplied by others to systems where it is not valid, leading to incorrect conclusions.
    - **Resolution test** The authors should add a more detailed discussion of the assumptions and limitations of the perturbative theory, perhaps including a quantitative estimate of its range of validity (e.g., in terms of the strength of the interaction parameter v). A direct comparison of the theory's predictions for a specific sequence with results from a more detailed, atomistic simulation of a real IDP would significantly strengthen the case for its utility.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific Importance
    - **Claim pointer** The manuscript concludes that "having a homopolymer-like MFF is insufficient to guarantee an underlying homogeneous conformational distribution" and that SAXS data alone cannot reliably distinguish between homogeneous and heterogeneous ensembles.
    - **Evidence pointer** Sections "MFFs of heteropolymeric and homopolymeric SAWs..." and "MFFs of select heterogeneous ensembles...", Figures 7, 9, 10, 13.
    - **Concern** The demonstration of many-to-one mapping is convincing for the specific, mathematically constructed ensembles used. However, the paper does not address the question of whether such heterogeneous ensembles are physically realizable by real amino acid sequences. The authors acknowledge this ("it suffices to define these ensembles mathematically, as long as the ensembles are in principle physically realizable"), but the "in principle" is a significant caveat. The paper would be more impactful if it could provide at least one example of a real IDP sequence that is predicted (or shown by simulation) to populate such a heterogeneous ensemble with a homopolymer-like MFF.
    - **Why it matters** The central conclusion of the paper is that SAXS data are insufficient. This conclusion is most powerful if it can be shown to apply to real, biologically relevant systems, not just to theoretical constructs.
    - **Resolution test** The authors could use their analytical theory or simulations to screen a library of real IDP sequences for those predicted to exhibit significant R_g-R_EE decoupling. Even a single example of a real sequence with a predicted homopolymer-like MFF but heterogeneous underlying ensemble would greatly strengthen the practical implications of the work.

- **Minor Comments**

    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability for Nonspecialists
    - **Affected element** Introduction and Discussion
    - **Evidence pointer** Sections "INTRODUCTION" and "DISCUSSION"
    - **Issue** The paper is dense and assumes a high level of familiarity with polymer physics concepts (e.g., perturbative expansions, Kratky plots, scaling exponents). The introduction could be more accessible to a broader biophysics audience.
    - **Required correction** Consider adding a brief, non-technical summary of the key concepts (e.g., what a Kratky plot is and why it is used) in the introduction or in a text box. The discussion of the "near-Levinthal" scenario is interesting but could be more clearly connected to the main findings of the paper.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Methods and Results
    - **Evidence pointer** Section "MODELS AND METHODS", Figures 2, 3.
    - **Issue** The manuscript states that the coarse-grained model is based on previous work but does not provide a full description of the model parameters (e.g., the exact form of the bond-angle potential, the range of the non-bonded interactions). The description of the simulation methodology is brief.
    - **Required correction** Provide more detail on the simulation parameters and the equilibration/sampling protocol to ensure reproducibility. This is particularly important for a methods-focused paper.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Scientific Importance
    - **Affected element** Discussion
    - **Evidence pointer** Section "Composite ensembles and experimental uncertainties", Figure 21.
    - **Issue** The example of a composite ensemble (mixture of two homogeneous ensembles) is interesting, but the discussion of its practical relevance is brief. The authors mention that such a situation could arise from a mixture of folded and unfolded states, but this is a well-known scenario.
    - **Required correction** The discussion could be expanded to consider other, less obvious, sources of composite ensembles, such as the presence of multiple distinct conformational states within the unfolded state itself, which is a more current and nuanced topic in the IDP field.

- **Technical failings that need to be addressed before the case is established**
    - The lack of a clear demonstration that the constructed heterogeneous ensembles are physically realizable by real amino acid sequences. The paper's central claim is about the interpretation of experimental data, and this would be significantly strengthened by a concrete example.
    - The validation of the analytical theory is limited to the coarse-grained model. A more direct test against a more detailed model or experimental data would be needed to establish its predictive power for real systems.

- **Assessment against Nature-style criteria**
    - **Originality:** High. The paper addresses a fundamental question about the information content of a widely used experimental technique and provides a novel theoretical framework for understanding it.
    - **Scientific importance:** High. The findings have direct implications for how SAXS data on IDPs are interpreted, a topic of intense current interest. The demonstration of many-to-one mapping is a significant conceptual advance.
    - **Interdisciplinary readership:** Moderate. The paper is primarily of interest to biophysicists, physical chemists, and computational biologists. The concepts are accessible to these groups, but the level of technical detail may limit its appeal to a broader biological audience.
    - **Technical soundness:** Good. The simulation and theoretical methods are appropriate for the questions asked. The main weakness is the lack of a direct test of the theory's predictive power for real protein sequences.
    - **Readability for nonspecialists:** Fair. The paper is well-written but is technically demanding. The key concepts and conclusions are clearly stated, but a non-specialist would need to invest significant effort to fully appreciate the details.

- **Recommendation posture** Supportive if technical concerns are resolved. The core message of the paper is important and the evidence is compelling. However, the impact would be significantly enhanced by addressing the concern about the physical realizability of the constructed ensembles and by providing a more robust validation of the analytical theory. The paper is a strong candidate for publication in a high-impact journal, but these points should be addressed in a revision.