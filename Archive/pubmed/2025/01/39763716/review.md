## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion) as provided
- **Assessment boundary** Scientific content, technical soundness, and logical coherence of the claims as presented in the supplied text
- **Shared manuscript claim summary** The manuscript proposes that the ultrastructure of a biomolecular condensate formed by the bacterial protein PopZ, specifically its hierarchical assembly into filaments, determines its material properties and cellular function. The authors integrate cryo-electron tomography, biochemistry, single-molecule FRET, and simulations to show that a C-terminal helical domain drives filamentation and condensation, while an intrinsically disordered region inhibits these processes. They further propose a phase-dependent conformational switch where H1-IDR interactions in the dilute phase suppress interfilament contacts and client binding, but condensation relieves this inhibition, exposing client-binding sites.
- **Visible evidence base** Results sections describing cryo-ET of WT and mutant condensates, mass photometry of oligomeric states, FRAP experiments on condensate diffusivity, smFRET on conformational states, and computational modeling with AlphaFold and coarse-grained simulations. Figures referenced include Fig. 1A–C, Fig. 2A–E, Fig. 3A–F, Fig. 4A–F, Fig. 5A–C, Fig. 6A–C, and supplementary figures S1–S7, tables S1–S3.
- **Missing materials affecting confidence** Figure panels and actual data values are not provided in the text. Statistical details, exact sample sizes, and quantitative fitting parameters for FRAP and smFRET are referenced but not shown. Methods section is not included in the supplied material. Supplementary videos and detailed simulation parameters are not available.

## Reviewer
- **Overall assessment** This manuscript addresses a fundamental question in the field of biomolecular condensates: how molecular-level features determine condensate ultrastructure and emergent material properties. The authors present a compelling multiscale study of PopZ, combining structural, biophysical, and computational approaches. The central claim that filamentous ultrastructure dictates material properties and function is well-motivated and supported by a coherent set of experiments. However, several technical concerns regarding the interpretation of FRAP data, the specificity of the smFRET conformational assignment, and the generalizability of the model require clarification. The manuscript is well-written and will be of interest to a broad audience in cell biology and biophysics, but the case for a direct causal link between ultrastructure and function would be strengthened by addressing the concerns below.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, and intracellular organization will find this work highly relevant. The study provides a detailed structural framework for how a condensate's internal architecture can be linked to its physical properties and biological output. The findings on PopZ, a well-studied bacterial polar organizing protein, will also appeal to microbiologists interested in cell polarity and asymmetric cell division. The methodological integration of cryo-ET, single-molecule FRET, and simulations offers a template for similar studies in other systems.

- **Major strengths** The study is notable for its comprehensive integration of multiple techniques across length scales, from atomic-level modeling to cellular-scale imaging. The identification of a specific helical domain driving filamentation and condensation, with the IDR acting as an inhibitor, provides a clear mechanistic model. The phase-dependent conformational switch, where H1-IDR interactions are relieved upon condensation, is an elegant and novel concept. The in vivo validation using filament-deficient mutants strengthens the biological relevance of the findings.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of FRAP interpretation
- **Claim pointer** The authors claim that filamentation increases the viscosity of PopZ condensates, based on FRAP experiments showing reduced recovery in WT compared to ΔL6 condensates.
- **Evidence pointer** Fig. 3E, Table S3
- **Concern** The FRAP data are used to infer differences in viscosity between WT and ΔL6 condensates. However, FRAP recovery is influenced by multiple factors, including binding kinetics, immobile fractions, and the size of the bleached region relative to the condensate. The authors report a mobile fraction of 40% and a half-time of ~27 min for mixed condensates, and 90% and 10 min for ΔL6-only condensates. The interpretation that this reflects a change in viscosity assumes that the diffusivity of the labeled PopZ is purely governed by the material properties of the condensate. If the labeled PopZ is incorporated into filaments, its mobility may be restricted by its incorporation into the filament network rather than by the bulk viscosity. The authors should clarify whether the FRAP recovery reflects the diffusion of free PopZ molecules or the dynamics of filament turnover. Without a direct measurement of viscosity (e.g., rheology or microrheology), the claim that filamentation increases viscosity is not fully supported.
- **Why it matters** The central thesis of the manuscript is that ultrastructure determines material properties. If the FRAP data are misinterpreted, the link between filamentation and viscosity is weakened, which would undermine the broader claim that ultrastructure dictates function.
- **Resolution test** The authors should provide additional evidence that the FRAP recovery is diffusion-limited rather than reaction-limited. This could be achieved by varying the bleach spot size and showing that the recovery time scales with the square of the bleach radius, or by performing fluorescence correlation spectroscopy to directly measure diffusion coefficients. Alternatively, they could use a passive microrheology approach to measure the viscoelastic properties of the condensates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Specificity of smFRET conformational assignment
- **Claim pointer** The authors claim that in the dilute phase, H1 interacts with the OD, and that condensation relieves this interaction, exposing client-binding sites.
- **Evidence pointer** Fig. 4A–E, Fig. S7
- **Concern** The smFRET experiments show a population at low EFRET (~0.1) and an intermediate EFRET state (~0.5), which the authors assign to extended and compacted conformations, respectively. The assignment of the intermediate state to an H1-OD interaction is based on the observation that adding unlabeled ΔH1-PopZ increases the compacted population. However, the FRET efficiency depends on the distance between the two labeled cysteines, and the intermediate EFRET could also arise from other conformations, such as partial folding of the IDR or interactions between the IDR and the OD that do not involve H1. The authors should provide more direct evidence for the H1-OD interaction, such as cross-linking mass spectrometry or NMR, to confirm the structural basis of the compacted state. Additionally, the claim that condensation relieves this interaction is based on a single experiment in the condensed phase, and the interpretation relies on the assumption that the FRET signal in the condensed phase is not affected by the high local concentration of PopZ.
- **Why it matters** The phase-dependent conformational switch is a key novel finding of the manuscript. If the assignment of the compacted state to H1-OD interactions is incorrect, the proposed mechanism for client binding regulation would be invalid.
- **Resolution test** The authors should perform additional experiments to validate the H1-OD interaction, such as mutating specific residues in H1 and the OD and testing the effect on the FRET signal. They could also use a two-color labeling scheme to directly measure the distance between H1 and the OD. For the condensed phase, they could use a combination of FRET and fluorescence lifetime imaging to account for the effects of high local concentration.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the model
- **Claim pointer** The authors propose that the ultrastructure of PopZ condensates, specifically filamentation, is a general determinant of condensate material properties and function.
- **Evidence pointer** Discussion section, "Filaments in other condensate systems"
- **Concern** The manuscript discusses other filamentous condensates, such as p62 and SPOP/DAXX, but the proposed model is based on a single protein system. The authors suggest that filamentation increases viscosity and surface tension, but this may not be a universal property of filamentous condensates. For example, the mechanical properties of a filament network depend on the stiffness, length, and cross-linking density of the filaments, which can vary widely between systems. The authors should be more cautious in generalizing their findings and should explicitly state the conditions under which their model is expected to apply.
- **Why it matters** The broader significance of the work depends on its relevance to other condensate systems. If the model is too specific to PopZ, the impact on the field would be limited.
- **Resolution test** The authors should either provide a more nuanced discussion of the conditions under which filamentation is expected to affect material properties, or they should present preliminary data from another filamentous condensate system to support the generality of their model.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure presentation
- **Affected element** Fig. 1A
- **Evidence pointer** Fig. 1A
- **Issue** The cryo-ET images in Fig. 1A are described as showing filaments, but the resolution and contrast of the images are not discussed. It is unclear whether the filaments are clearly visible in the tomographic slices or whether they require segmentation to be discerned.
- **Required correction** The authors should provide a scale bar and a zoomed-in view of a representative filament to help the reader visualize the ultrastructure. They should also state the resolution of the tomograms.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Fig. 3E–F, Table S3
- **Evidence pointer** Fig. 3E–F, Table S3
- **Issue** The FRAP data are presented as mobile fractions and half-times, but the number of replicates and the error bars are not described in the text. It is unclear whether the differences between WT and ΔL6 are statistically significant.
- **Required correction** The authors should report the number of independent experiments and the standard error or confidence intervals for the FRAP parameters. They should also state the statistical test used to compare the conditions.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of simulation description
- **Affected element** Methods, "Coarse-grained molecular dynamics simulations"
- **Evidence pointer** Methods section (not provided in full)
- **Issue** The description of the coarse-grained simulations is brief. The authors state that they used the OpenABC implementation of the HPS model with the Urry hydrophobicity scale, but they do not provide details on the simulation length, temperature, or the number of replicates. The validation of the simulations against experimental data is also not described in detail.
- **Required correction** The authors should provide a more detailed description of the simulation parameters and the validation procedure in the Methods section.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation of in vivo data
- **Affected element** Fig. 5A–C
- **Evidence pointer** Fig. 5A–C
- **Issue** The in vivo experiments show that expression of ΔL6-PopZ is toxic and impairs ParB anchoring. The authors interpret this as evidence that filamentation is crucial for function. However, the toxicity could also be due to the overexpression of a mutant protein that forms non-specific aggregates, rather than a specific loss of filamentation. The authors should discuss this alternative interpretation.
- **Required correction** The authors should include a discussion of the potential off-target effects of ΔL6-PopZ expression and provide evidence that the observed toxicity is specifically due to the loss of filamentation.

- **Technical failings that need to be addressed before the case is established** R1-M1 and R1-M2 are blocking concerns. The FRAP interpretation and the smFRET conformational assignment are central to the manuscript's claims. Without addressing these, the case for a direct link between ultrastructure and function is not fully established.

- **Assessment against Nature-style criteria** 
  - **Originality** The study is original in its comprehensive integration of techniques to link ultrastructure to condensate function. The concept of a phase-dependent conformational switch is novel.
  - **Scientific importance** The work addresses a fundamental question in the field and has the potential to influence how researchers think about condensate architecture and function. The findings are likely to be of broad interest.
  - **Interdisciplinary readership** The study will appeal to researchers in cell biology, biophysics, and structural biology. The use of multiple techniques makes it accessible to a wide audience.
  - **Technical soundness** The technical quality is generally high, but the concerns regarding FRAP and smFRET interpretation need to be resolved. The computational modeling is well-integrated but requires more detail.
  - **Readability for nonspecialists** The manuscript is well-written and the concepts are explained clearly. The figures are likely to be helpful, but the text could benefit from a brief summary of the key findings at the end of the introduction.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a compelling and novel model, but the blocking concerns regarding the interpretation of FRAP and smFRET data must be addressed before the case is fully established.

## Risk / unsupported claims
- The claim that filamentation increases viscosity is not fully supported by the FRAP data, as the recovery may be influenced by binding kinetics or filament turnover.
- The assignment of the intermediate smFRET state to an H1-OD interaction is not directly validated.
- The generalizability of the model to other filamentous condensates is speculative and not supported by data from other systems.
- The in vivo toxicity of ΔL6-PopZ is interpreted as a specific effect of loss of filamentation, but alternative explanations are not ruled out.