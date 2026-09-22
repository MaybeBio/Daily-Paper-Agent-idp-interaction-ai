## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results and discussion, conclusion) as provided by the user. No supplementary information, figures, or tables were included in the submission.
- **Assessment boundary** The review is limited to the scientific content, methodology, and claims as presented in the provided text. No external validation of the simulation methods, force fields, or comparison with experimental data beyond what is cited in the text was performed.
- **Shared manuscript claim summary** The authors use multiscale simulations (atomistic MD and coarse-grained models) to argue that the abundance and, critically, the location of aromatic-rich low-complexity aromatic-rich kinked segments (LARKS) within protein sequences dictate the rate of condensate ageing, the formation of percolating inter-molecular β-sheet networks, and the resulting viscoelastic properties. They further propose that relocating the LARKS-containing domain in FUS, combined with RNA binding, can suppress ageing.
- **Visible evidence base** The evidence base consists of: (i) all-atom umbrella sampling PMF calculations for a TDP-43 LARKS peptide, (ii) coarse-grained simulations of model low-complexity domain peptides with a dynamic algorithm for β-sheet transitions, (iii) coarse-grained simulations of full-length FUS and its variants, (iv) analysis of shear stress relaxation moduli, and (v) a percolation network analysis. All quantitative results are described in the text but the actual figures, tables, and simulation details are in the Supporting Information, which was not provided.
- **Missing materials affecting confidence** The Supporting Information, all figures, and all tables were not provided. This includes the simulation parameters, the full description of the dynamic algorithm, the force field parameters, the sequences of the model peptides, the details of the PMF calculations, and the data for the phase diagrams and viscosity calculations. The absence of these materials significantly limits the ability to fully assess the technical soundness and reproducibility of the work.

## Reviewer
- **Overall assessment** This manuscript presents a compelling and timely computational study addressing a key question in the biology of biomolecular condensates: how the sequence features of prion-like domains, specifically the location and number of LARKS, control the transition from liquid-like to solid-like states. The central finding, that LARKS at the termini promote faster network percolation and higher viscosity than centrally located LARKS, is conceptually novel and provides a testable hypothesis for experimentalists. The multiscale approach, bridging atomistic PMF calculations with coarse-grained simulations, is appropriate and powerful. However, the manuscript as presented is incomplete. The core evidence, including all figures, simulation details, and validation, resides in the Supporting Information, which was not available for review. Consequently, the technical soundness of the model, the robustness of the key claims, and the quantitative accuracy of the results cannot be fully verified. The claims are plausible and well-argued, but the current submission does not provide sufficient evidence to establish them definitively.
- **Who would be interested in the results, and why** This work will be of high interest to researchers in the fields of phase separation, intrinsically disordered proteins, neurodegeneration, and biomolecular condensates. Specifically, (i) computational biophysicists studying the molecular determinants of condensate material properties, (ii) experimental biologists investigating the role of FUS, TDP-43, and hnRNPA1 in ALS/FTD, and (iii) synthetic biologists interested in designing proteins with tunable phase behavior. The proposed design principle, that LARKS location can be used to control ageing, offers a potential roadmap for engineering condensates with desired viscoelastic properties.
- **Major strengths**
    1.  The central hypothesis is novel and significant, moving beyond simple sequence composition to highlight the importance of sequence architecture (LARKS position) in dictating the kinetics of condensate maturation.
    2.  The multiscale methodology is sophisticated, connecting atomistic-level binding free energies to mesoscale material properties, which is a powerful and increasingly necessary approach in this field.
    3.  The work provides a clear, mechanistic explanation for the observed differences in ageing behavior, linking microscopic network percolation to macroscopic viscosity.
    4.  The study offers a potential therapeutic or engineering strategy, namely sequence reordering, to mitigate pathological ageing, which is a valuable and actionable outcome.
- **Major Concerns**

    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical Soundness
    - **Claim pointer** The authors claim that the coarse-grained model is parameterized based on atomistic PMF simulations and that the dynamic algorithm recapitulates the non-equilibrium process of condensate ageing.
    - **Evidence pointer** Figure 1a, 1b, and "Supporting Information"
    - **Concern** The entire coarse-grained model and the dynamic ageing algorithm are the foundation of this study. The parameterization details, the specific implementation of the Wang-Frenkel potential, the criteria for triggering a β-sheet transition, and the validation of the model against known experimental or theoretical results are all relegated to the Supporting Information. Without this information, it is impossible to assess whether the model is physically sound, whether the parameters are reasonable, or whether the results are an artifact of the model's construction rather than a reflection of the underlying physics.
    - **Why it matters** The conclusions of the paper rest entirely on the predictive power of this bespoke coarse-grained model. If the model is not rigorously parameterized and validated, the central claims about LARKS location and abundance dictating viscoelastic properties are unsubstantiated. The reader cannot distinguish between a robust physical finding and a model-specific outcome.
    - **Resolution test** The authors must provide the full details of the model in the main text or a comprehensive Supporting Information document. This should include, at minimum, the functional form of all interaction potentials, a table of all parameters, a step-by-step description of the dynamic algorithm, and a validation section showing that the model can reproduce known phase behavior or material properties of a benchmark system.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical Soundness
    - **Claim pointer** The authors claim that proteins with two or more LARKS form percolated β-sheet networks and become kinetically arrested (gel-like), while proteins with a single LARKS do not.
    - **Evidence pointer** Figure 2d, 2f, and "Supporting Information"
    - **Concern** The evidence for this central claim is presented in Figure 2d and 2f, which are not available in the provided text. The claim is based on the analysis of the shear stress relaxation modulus and a percolation network analysis. The text states that for 2- and 3-LARKS proteins, the modulus does not decay, but the actual data, the criteria for determining a "plateau," and the statistical significance of the difference between 1-LARKS and multi-LARKS systems are not shown. The percolation analysis is also not described in detail.
    - **Why it matters** The distinction between a highly viscous liquid and a gel is a critical qualitative difference. The authors' conclusion that multi-LARKS proteins form gels is a strong statement that requires robust quantitative evidence. Without seeing the raw data and the analysis methodology, it is impossible to verify this key finding.
    - **Resolution test** The authors must present the data for the shear stress relaxation modulus for all systems, clearly showing the difference in behavior between 1-LARKS and multi-LARKS systems. The percolation analysis must be described in detail, including the definition of a "percolating network" and the method for determining it.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific Importance
    - **Claim pointer** The authors claim that the reordering of the FUS LCD to the center of the protein, combined with RNA, can suppress ageing and maintain liquid-like behavior.
    - **Evidence pointer** Figure 3, 4, and 5
    - **Concern** While this is a fascinating and potentially important result, the claim is based on a single, specific reordering of the FUS sequence. The authors do not explore whether this is a general principle or a specific property of the FUS sequence. The text mentions that the reordered variant is not found in nature, which raises the question of its physiological relevance. The mechanism of RNA suppression is also inferred from binding probabilities, but the direct evidence for the proposed "RNA-blocking mechanism" is not presented in the text.
    - **Why it matters** The paper's broader significance hinges on whether the design principle (LARKS location) can be generalized. If it only works for this specific FUS construct, its impact is diminished. The claim about RNA suppressing ageing is a major one, and the proposed mechanism needs to be more directly supported.
    - **Resolution test** The authors should either (a) test the generality of their design principle by simulating other proteins or a library of sequences with different LARKS positions, or (b) temper their claims about the general applicability of the approach. The mechanism of RNA suppression should be supported by more direct analysis, such as radial distribution functions or contact maps showing the physical occlusion of LARKS by RNA.

    - **Concern ID** R1-M4
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical Soundness
    - **Claim pointer** The authors claim that the atomistic PMF simulations provide quantitative binding free energies for LARKS-LARKS interactions, which are then used to parameterize the coarse-grained model.
    - **Evidence pointer** Figure 1a, 1b
    - **Concern** The text states that the binding energy is "almost 7 times larger" for β-sheet structures and that the values are "consistent with" previous calculations. However, the actual PMF curves are not shown, and the methodology for extracting a single binding energy value from a PMF profile is not described. The potential overestimation of the binding energy due to positional restraints is mentioned but not quantified.
    - **Why it matters** The quantitative accuracy of the atomistic calculations is the basis for the coarse-grained model's energy scale. If the PMF calculations are not robust or the analysis is flawed, the entire coarse-grained model is built on a weak foundation.
    - **Resolution test** The authors must show the PMF curves and describe the methodology for calculating the binding free energy. They should also provide a more detailed discussion of the limitations of their approach, including the effect of restraints and the finite size of the simulation system.

- **Minor Comments**

    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability for Nonspecialists
    - **Affected element** Introduction and Results
    - **Evidence pointer** "location not provided"
    - **Issue** The manuscript uses specialized terminology (e.g., "percolating inter-molecular network," "kinetically trapped," "cation-π interactions") without always providing a brief, accessible explanation. The distinction between a "highly viscous liquid" and a "gel" is a key concept but is not clearly defined for a general reader.
    - **Required correction** Add a brief, plain-language explanation of key concepts, such as "percolation" and "gel," when they are first introduced. For example, explain that a percolating network is a connected structure that spans the entire system, and that a gel is a solid-like state where this network prevents flow.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Results and Discussion, Section 2.4
    - **Evidence pointer** "location not provided"
    - **Issue** The text states that the coarse-grained model "overestimates the kinetics of protein diffusion" but does not provide a quantitative estimate of this overestimation or discuss its potential impact on the absolute values of the calculated viscosities.
    - **Required correction** Provide a quantitative estimate of the diffusion overestimation and a brief discussion of how this affects the interpretation of the viscosity values. For example, state that while the absolute values may be off by a factor of X, the relative differences between the systems are expected to be robust.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Scientific Importance
    - **Affected element** Conclusion
    - **Evidence pointer** "location not provided"
    - **Issue** The conclusion is somewhat brief and does not fully discuss the broader implications of the work for understanding disease mechanisms or for the design of therapeutic interventions. The potential limitations of the computational approach are also not discussed in the conclusion.
    - **Required correction** Expand the conclusion to include a more detailed discussion of the implications of the findings, the limitations of the study, and the most promising avenues for future research, both computational and experimental.

## Risk / unsupported claims
- The claim that the coarse-grained model accurately captures the non-equilibrium ageing process is unverifiable without the full model details and validation data.
- The claim that proteins with two or more LARKS form percolated networks and become kinetically arrested is not supported by the visible evidence, as the relevant figures are missing.
- The claim that RNA can suppress ageing in the reordered FUS variant is based on a single simulation setup and the proposed mechanism is inferred, not directly demonstrated.
- The quantitative values for binding free energies, kinetic constants, and viscosities are presented in the text but cannot be verified without the corresponding figures and tables.
- The generalizability of the design principle (LARKS location) beyond the specific sequences tested is not established.