## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, materials and methods, results, discussion, conclusions, and supplementary material references.
- **Assessment boundary** Evaluation is limited to the scientific content, methodology, and claims presented in the provided manuscript. No external data, experimental validation, or peer-reviewed literature beyond what is cited within the text was independently verified.
- **Shared manuscript claim summary** The authors propose that GSK3β-driven phosphorylation of ABLIM1, particularly at sites within intrinsically disordered regions, alters the conformational ensemble of ABLIM1, thereby modulating its interaction with titin's Z1Z2 segment and influencing length-dependent activation in cardiac muscle. This is supported by multiscale computational modeling, including atomistic and coarse-grained molecular dynamics simulations, and a state-based contraction model.
- **Visible evidence base** Computational predictions from molecular dynamics simulations (atomistic and coarse-grained), sequence analyses (ELM, BLAST), docking studies (ClusPro), binding free energy calculations (MMGBSA), and simulations using the MATMyoSim contraction model. Reference is made to experimental data from a prior study (Stachowski-Doll et al., 2022) for phosphorylation sites and functional outcomes.
- **Missing materials affecting confidence** No experimental validation of the predicted conformational changes or binding interactions is provided. The manuscript relies heavily on simulations and inferences from prior work. Details on the convergence of simulations, force field validation for phosphoserine parameters, and the statistical significance of observed differences in conformational ensembles are not fully described. The direct link between ABLIM1 phosphorylation, titin binding, and LDA remains inferential.

## Reviewer
- **Overall assessment** This is a computationally intensive study that addresses a significant and timely question in cardiac muscle biology: how phosphorylation of intrinsically disordered regions in a myofilament protein (ABLIM1) might regulate its interactions and contribute to length-dependent activation. The use of multiscale modeling is appropriate and the authors are to be commended for tackling a challenging system. However, the manuscript currently presents a series of computational predictions without direct experimental validation. The central claims, while plausible, are not definitively established from the evidence provided. The link between the simulated conformational changes and the physiological outcome (LDA) is made through a simplified contraction model with several assumptions. The study is more hypothesis-generating than hypothesis-testing in its current form. The strengths lie in the detailed computational approach and the integration of multiple modeling scales. The major weaknesses are the lack of experimental corroboration, the potential overinterpretation of simulation results, and the indirect nature of the evidence connecting molecular events to whole-cell physiology.
- **Who would be interested in the results, and why** Researchers in cardiac muscle physiology, particularly those studying sarcomeric proteins, length-dependent activation, and the Frank-Starling mechanism. Also, computational biophysicists interested in multiscale modeling of protein dynamics, intrinsically disordered proteins, and the effects of post-translational modifications on protein conformation and interactions. The findings could be relevant to those studying heart failure mechanisms, as altered phosphorylation is implicated in disease.
- **Major strengths**
    1.  The study addresses a complex and important biological question using a sophisticated multiscale computational approach, combining atomistic and coarse-grained simulations.
    2.  The authors are transparent about the limitations of their models and the assumptions made, particularly regarding the use of phosphomimetics and the simplified contraction model.
    3.  The integration of sequence analysis, structural modeling, and physiological simulation provides a comprehensive, if speculative, framework for understanding ABLIM1's role.
    4.  The work generates specific, testable hypotheses about the molecular mechanisms underlying phosphorylation-dependent regulation of ABLIM1 and its impact on LDA.
- **Major Concerns**
    - **R1-M1**
        - **Severity** Major
        - **Blocking** Yes
        - **Axis** Evidence strength and validation
        - **Claim pointer** The manuscript claims that phosphorylation of ABLIM1 at specific sites (e.g., S216, S450, S452) alters its conformational ensemble, which in turn modulates its interaction with titin and affects length-dependent activation.
        - **Evidence pointer** Results sections on "ABLIM1 intrinsic disorder affords diverse conformations of the 4 LIM domain construct" and "Effects of phosphorylation of S216 on the binding of ABLIM1 to Z1Z2"; Discussion section "Main highlights".
        - **Concern** The central claims are based entirely on computational predictions. There is no experimental data presented to validate that (a) the predicted conformational changes occur in the actual protein, (b) the predicted binding interface with titin is correct, or (c) the changes in binding affinity are physiologically relevant. The study relies on a single prior experimental paper (Stachowski-Doll et al., 2022) for the functional context, but does not directly test the proposed mechanism.
        - **Why it matters** Without experimental validation, the conclusions remain speculative. The computational models, while sophisticated, are based on force fields and sampling methods that have inherent limitations. The predicted effects could be artifacts of the simulation parameters or the chosen starting structures. The claim that this mechanism "provides a mechanism" for LDA is a significant overreach without direct experimental support.
        - **Resolution test** The authors should either provide experimental data (e.g., mutagenesis, binding assays, phosphorylation assays) to support their key predictions, or significantly temper their conclusions, framing the work as a set of testable hypotheses rather than an established mechanism.
    - **R1-M2**
        - **Severity** Major
        - **Blocking** No
        - **Axis** Model fidelity and parameterization
        - **Claim pointer** The manuscript uses phosphomimetic mutations (S-to-D) to model phosphorylation and claims these are reliable surrogates, stating "these results support the use of phosphomimetics as surrogates for constitutively phosphorylated proteins."
        - **Evidence pointer** Materials and methods section "Atomistic molecular dynamics simulations"; Results section "ABLIM1 phosphorylation impacts its IDR conformation ensemble".
        - **Concern** While the authors provide some validation that phosphomimetics have a "similar impact" to actual phosphorylation in their simulations, this is a critical assumption. The chemical nature of a phosphoserine (with a -2 charge and specific hydrogen bonding capabilities) is significantly different from an aspartate (-1 charge). The validation is also based on the same computational models, which may not capture the full range of phosphorylation effects.
        - **Why it matters** If the phosphomimetic is not an accurate representation of phosphorylation, then all subsequent conclusions about the effects of phosphorylation on conformation and binding are potentially invalid. This is a foundational assumption of the study.
        - **Resolution test** The authors should provide a more rigorous validation of the phosphomimetic approach, perhaps by comparing the structural ensembles of phosphomimetic and explicitly phosphorylated variants in more detail, or by referencing experimental studies that have validated this approach for similar systems.
    - **R1-M3**
        - **Severity** Major
        - **Blocking** No
        - **Axis** Link between molecular simulation and physiological outcome
        - **Claim pointer** The manuscript claims that the reduced ability of phosphorylated ABLIM1 to bind titin, as predicted by simulations, provides a mechanism for the diminished length-dependent activation observed in GSK3β knockout models.
        - **Evidence pointer** Results section "Length-dependent activation"; Discussion section "Length-dependent activation".
        - **Concern** The connection between the simulated molecular events and the whole-cell physiological readout (LDA) is made through a highly simplified contraction model (MATMyoSim). The parameters for this model are adjusted to "match the experimental trends" from a different study, but the link between the specific molecular interaction (ABLIM1-titin) and the model parameters (e.g., passive stiffness, myosin recruitment) is not rigorously established. The model is used to demonstrate plausibility, not to prove causality.
        - **Why it matters** The physiological relevance of the molecular findings is a key part of the paper's significance. If the link to LDA is only weakly supported, the broader impact of the work is diminished. The model could be consistent with many other mechanisms.
        - **Resolution test** The authors should more clearly articulate and justify the assumptions in the contraction model that link ABLIM1-titin binding to passive stiffness and myosin recruitment. They should also discuss alternative interpretations of the experimental data that are consistent with their model.
- **Minor Comments**
    - **R1-m1**
        - **Severity** Minor
        - **Axis** Clarity and presentation
        - **Affected element** Abstract and Introduction
        - **Evidence pointer** Abstract; Introduction section.
        - **Issue** The abstract and introduction could be more accessible to a general scientific audience. The term "intrinsically disordered regions" and the specific protein names are used without a brief explanation of their significance for non-specialists.
        - **Required correction** Provide a brief, clear explanation of what intrinsically disordered regions are and why their regulation is important in the context of muscle contraction.
    - **R1-m2**
        - **Severity** Minor
        - **Axis** Statistical rigor
        - **Affected element** Results sections on simulation data
        - **Evidence pointer** Figures 6, 8, 9; Results sections on "LIM domain multimers are impacted by phosphorylation" and "ABLIM1 phosphorylation impacts its IDR conformation ensemble".
        - **Issue** The manuscript reports differences in properties like Rg and end-to-end distance between WT and phosphomimetic variants, but it is unclear if these differences are statistically significant. Error bars are mentioned but the statistical tests used are not described.
        - **Required correction** Clearly state the statistical methods used to compare distributions (e.g., t-test, Mann-Whitney U test) and report p-values or confidence intervals for the key comparisons.
    - **R1-m3**
        - **Severity** Minor
        - **Axis** Completeness of methods
        - **Affected element** Materials and methods section "Martini CG MD simulations"
        - **Evidence pointer** Materials and methods section "Martini CG MD simulations".
        - **Issue** The description of the coarse-grained simulation setup is brief. Details on the elastic network applied to the folded domains, the specific parameters for the phosphoserine beads, and the equilibration protocol are not fully provided.
        - **Required correction** Provide more detail on the CG model construction, including the elastic network parameters, the mapping of phosphoserine to CG beads, and the simulation length and number of replicates.
    - **R1-m4**
        - **Severity** Minor
        - **Axis** Interpretation of docking results
        - **Affected element** Results section "Effects of phosphorylation of S216 on the binding of ABLIM1 to Z1Z2"
        - **Evidence pointer** Results section "Effects of phosphorylation of S216 on the binding of ABLIM1 to Z1Z2"; Figure 10.
        - **Issue** The docking results are used to suggest that phosphorylation does not affect binding via the interface, but the authors note that the binding poses are speculative. The MMGBSA calculations show favorable binding energies for all poses, but the significance of the differences between poses is not discussed.
        - **Required correction** Clarify the limitations of the rigid-body docking approach and discuss the variability in the predicted binding energies. The conclusion that phosphorylation does not affect the binding interface should be presented with appropriate caution.
- **Technical failings that need to be addressed before the case is established**
    - Lack of experimental validation for the central claims (R1-M1).
    - Insufficient validation of the phosphomimetic approach as a faithful representation of phosphorylation (R1-M2).
    - The link between molecular simulations and the physiological LDA model is not rigorously established (R1-M3).
    - Statistical analysis of simulation data is incomplete (R1-m2).
    - Methods for CG simulations are not fully detailed (R1-m3).

## Risk / unsupported claims
- The claim that phosphorylation of ABLIM1 at S216, S450, and S452 directly modulates its interaction with titin and thereby affects LDA is not supported by direct experimental evidence. It is a plausible hypothesis based on computational modeling.
- The claim that the predicted conformational changes in ABLIM1's IDRs are the primary mechanism for its functional regulation is not directly tested.
- The assertion that the contraction model simulations "validate" the hypothesis is an overstatement; they demonstrate consistency with a simplified model, not validation.
- The potential role of other phosphorylation sites or other post-translational modifications in regulating ABLIM1 function is not explored.
- The physiological relevance of the predicted binding affinities and conformational changes in the context of the crowded sarcomere environment is not assessed.