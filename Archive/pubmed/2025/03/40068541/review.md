## Review setup
- **Input scope** Full manuscript text (abstract, introduction, and all sections)
- **Assessment boundary** Scientific content, technical soundness, and claims as presented in the provided text
- **Shared manuscript claim summary** The authors review recent advances in atomistic molecular dynamics simulations of intrinsically disordered proteins, arguing that IDP-tested force fields and GPU acceleration have enabled accurate simulations that now explain sequence-dependent dynamics, binding mechanisms, drug action modes, and phase separation, with AI/ML methods further expanding capabilities.
- **Visible evidence base** Abstract, introduction, and six substantive sections covering force field development, dynamics, binding, drug action, phase separation, and AI/ML applications
- **Missing materials affecting confidence** Figures referenced (Figures 1a-c, 2a-c, 3a-d) are not provided; no methods section; no force field parameter tables; no simulation protocol details; no error analysis or convergence criteria; no comparison statistics

## Reviewer
- **Overall assessment** This is a well-written, informative review that synthesizes recent progress in atomistic MD simulations of IDPs. The authors are clearly expert in the field, and the selection of topics is timely and relevant. The review successfully conveys the message that atomistic simulations have matured to a point where they can provide physical insights complementary to experiments. However, the manuscript has several structural and evidentiary weaknesses. The lack of figures in the provided material makes it impossible to assess the quality of the illustrative examples. More importantly, the review makes several strong claims about the state of the field without providing quantitative benchmarks or critical comparisons between force fields. The section on AI/ML is notably thin and does not critically evaluate the limitations of these methods. The review would benefit from a more balanced treatment of unresolved challenges, particularly regarding force field accuracy for specific IDP properties and the reproducibility of simulation results across laboratories.

- **Who would be interested in the results, and why** Computational biophysicists and molecular simulators will find this review useful as a summary of recent methodological advances and applications. Experimentalists studying IDPs by NMR, SAXS, or FRET may also benefit from understanding what simulation methods are now capable of and how they can complement experimental data. Researchers entering the IDP simulation field will find the force field guidance and examples of successful applications valuable. The review is also relevant to those interested in drug discovery targeting IDPs and in understanding phase separation phenomena.

- **Major strengths** The review is clearly organized around key application areas where atomistic simulations have made recent contributions. The emphasis on the need for IDP-tested force fields is well justified and practically useful. The authors provide concrete examples of how simulations have explained experimental observations, such as the sequence-dependent dynamics of ChiZ and the binding mechanisms of α-MoRE. The discussion of drug action modes on IDPs is nuanced and goes beyond simple lock-and-key models. The connection between R2 values and LLPS propensity is an interesting and potentially insightful observation.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The review claims that "recent IDP simulations have shown that some force fields can reproduce both conformational and dynamic properties of IDPs" and that specific force field combinations are recommended.
  - **Evidence pointer** Section "IDP simulations require IDP-tested force fields"; location not provided
  - **Concern** The review presents force field comparisons and recommendations without providing quantitative data. For example, the claim that Amber14SB/TIP4P-D was "the best" in matching experimental data for ChiZ is stated without reporting the actual deviations from experiment or the statistical significance of differences between force fields. Similarly, the comparison between Amber99SB-disp and Amber19SB/TIP4P-D for α-synuclein is mentioned as being "on par" without quantitative support.
  - **Why it matters** For a review whose central message is that force field choice matters critically for IDP simulations, the lack of quantitative benchmarks undermines the practical guidance offered. Readers cannot assess the magnitude of differences between force fields or determine which force field might be appropriate for their specific system of interest.
  - **Resolution test** Provide a table or figure summarizing quantitative comparisons (e.g., RMSD from experimental chemical shifts, radius of gyration deviations, R2 agreement metrics) for the force fields discussed, with appropriate error estimates.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Completeness
  - **Claim pointer** The review claims that "All-atom simulations have been an equal partner to NMR and other experimental techniques" and that the field has seen "remarkable gains in accuracy."
  - **Evidence pointer** Introduction; location not provided
  - **Concern** The review does not critically discuss the limitations and failure cases of current atomistic simulations of IDPs. There is no mention of force field artifacts, sampling limitations, system size effects, or the challenges of validating simulations against ensemble-averaged experimental observables. The tone is uniformly positive, which may give readers an overly optimistic view of the current state of the field.
  - **Why it matters** A balanced review should acknowledge where simulations still struggle. For example, the timescales accessible to atomistic simulations remain limited, and the accuracy of force fields for specific sequence contexts (e.g., proline-rich regions, glycine-rich linkers) is not uniformly established. Without this critical perspective, readers may overinterpret simulation results.
  - **Resolution test** Add a section or paragraph discussing known limitations, including specific examples where simulations have failed to reproduce experimental data or where different force fields give conflicting results.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Depth of treatment
  - **Claim pointer** The review claims that "AI and ML are further expanding the reach of atomistic MD simulations" and describes several methods.
  - **Evidence pointer** Section "AI and ML expand the reach of all-atom simulations"; location not provided
  - **Concern** The AI/ML section is superficial. It describes several methods (autoencoders, variational autoencoders, diffusion models, VAMPNet) but does not critically evaluate their accuracy, limitations, or generalizability. For example, the claim that generative autoencoders "rapidly produced conformations of IDPs, which mimicked those sampled from the rest of the simulations" is presented without any quantitative comparison of the generated ensembles to the reference simulations. The IDPFold method is described as being trained on a mix of experimental structures and simulation data, but the accuracy of its predictions for unseen IDPs is not discussed.
  - **Why it matters** AI/ML methods for IDP conformational sampling are rapidly developing but also have significant caveats, including the risk of generating physically unrealistic conformations and the dependence on training data quality. A review that mentions these methods without critical assessment may mislead readers about their readiness for routine use.
  - **Resolution test** Provide a more detailed evaluation of each AI/ML method, including quantitative benchmarks (e.g., ensemble similarity metrics, physical validity checks) and a discussion of current limitations and outstanding challenges.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Reproducibility
  - **Claim pointer** The review describes specific simulation studies and their findings, including simulation lengths, system compositions, and enhanced sampling methods.
  - **Evidence pointer** Throughout; location not provided
  - **Concern** The review does not provide sufficient methodological detail for readers to reproduce or evaluate the described simulations. For example, the simulations of ChiZ, α-synuclein, Aβ42, and the phase-separated systems are described without specifying simulation lengths, number of replicas, thermostat settings, or convergence criteria. The description of the "adaptive bandit method" and "parallel cascade selection MD" lacks the algorithmic detail needed to understand their implementation.
  - **Why it matters** Reproducibility is a core value in computational science. Without adequate methodological detail, readers cannot assess the reliability of the reported results or build upon them. This is particularly important for a review that aims to guide practitioners.
  - **Resolution test** Add a table summarizing key simulation parameters for each described study (system, force field, water model, simulation length, ensemble, enhanced sampling method, software) and provide references to original publications for full methodological details.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Abstract
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The abstract states that "All-atom MD simulations are now explaining the sequence-dependent dynamics of IDPs" but does not mention the limitations of these explanations or the systems for which this has been demonstrated.
  - **Required correction** Consider adding a qualifying phrase such as "for a growing number of IDPs" or "in specific cases" to avoid overgeneralization.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** Section "IDP simulations require IDP-tested force fields"
  - **Evidence pointer** Section "IDP simulations require IDP-tested force fields"; location not provided
  - **Issue** The term "legacy force fields" is used pejoratively without a clear definition. It is unclear whether this refers to force fields developed before a certain date, force fields not tested on IDPs, or force fields with known deficiencies for IDPs.
  - **Required correction** Define the term explicitly, for example, "force fields parameterized primarily against folded protein data and not validated on IDPs."

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Section "All-atom simulations of phase-separated systems enable direct comparison with experimental measurements"
  - **Evidence pointer** Section "All-atom simulations of phase-separated systems enable direct comparison with experimental measurements"; location not provided
  - **Issue** The discussion of phase-separated systems focuses on two examples (tetrapeptides and prothymosin-α/H1.0) but does not mention other important systems studied by atomistic simulations, such as FUS, TDP-43, or elastin-like polypeptides.
  - **Required correction** Consider adding a brief discussion of other systems or explicitly state that the selected examples are illustrative rather than comprehensive.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Readability
  - **Affected element** Section "All-atom simulations reveal different modes of drug action on IDPs"
  - **Evidence pointer** Section "All-atom simulations reveal different modes of drug action on IDPs"; location not provided
  - **Issue** The section jumps between different drug-IDP systems without a clear organizing framework. The distinction between "physical blocking" and "conformational shift" modes of action could be made more explicit.
  - **Required correction** Consider reorganizing the section around the proposed modes of action, with each mode illustrated by one or two examples.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Referencing
  - **Affected element** Section "All-atom simulations provide explanations for the sequence dependence of IDP dynamics"
  - **Evidence pointer** Section "All-atom simulations provide explanations for the sequence dependence of IDP dynamics"; location not provided
  - **Issue** The SeqDYN method is described with a URL but no citation to a peer-reviewed publication. If the method has been published, a citation should be provided.
  - **Required correction** Add the appropriate citation for SeqDYN or clarify that it is an unpublished tool.

- **Technical failings that need to be addressed before the case is established** The primary technical failing is the absence of quantitative benchmarks for force field comparisons and simulation accuracy claims. The review would be substantially strengthened by including a summary table of quantitative metrics (e.g., chemical shift deviations, Rg comparisons, R2 agreement) for the force fields and systems discussed. Additionally, the lack of figures in the provided material prevents assessment of the illustrative examples; if figures are included in the published version, they should be carefully designed to convey quantitative information rather than just representative snapshots.

## Assessment against Nature-style criteria
- **Originality** The review does not present new research findings but synthesizes recent literature. Its originality lies in the specific selection and framing of topics, particularly the emphasis on drug action modes and the connection between R2 and LLPS propensity. However, several other recent reviews cover similar ground, and the present manuscript does not offer a distinctly novel perspective.
- **Scientific importance** The topic is of high importance given the growing recognition of IDPs in biology and disease. The review addresses questions that are central to the field, such as force field accuracy and the ability of simulations to explain experimental observations. The practical guidance on force field selection is valuable.
- **Interdisciplinary readership** The review is primarily written for a computational biophysics audience. Experimentalists may find some sections accessible, but the level of technical detail in the force field discussion and the lack of a glossary for simulation-specific terms may limit broader readership. The drug action and phase separation sections have broader appeal.
- **Technical soundness** The technical content appears sound based on the described results, but the lack of quantitative data and methodological detail prevents full assessment. The force field recommendations are consistent with the current literature, but the review does not provide the critical comparison needed to establish confidence in these recommendations.
- **Readability for nonspecialists** The writing is generally clear and well-organized, but assumes familiarity with MD simulation concepts and terminology. Terms such as "PFold," "reaction coordinate," and "spin-labeling" are used without definition. The abstract is accessible, but the body of the review would benefit from brief explanations of key technical concepts.

## Risk / unsupported claims
- The claim that "some force fields can reproduce both conformational and dynamic properties of IDPs" is presented without quantitative evidence in the provided text.
- The statement that Amber14SB/TIP4P-D was "the best" among five force fields for ChiZ is unsupported without reporting the comparison metrics.
- The claim that the q parameter from SeqDYN "captures the propensity of an amino acid to form intramolecular interactions" and correlates with LLPS threshold concentration is presented without showing the correlation data.
- The description of drug-induced conformational shifts as a general mode of action for IDPs is based on limited examples and may not be generalizable.
- The AI/ML section makes claims about the capabilities of generative models and VAMPNet without providing quantitative benchmarks or discussing failure modes.
- The statement that "all-atom simulations have been an equal partner to NMR and other experimental techniques" is an overstatement that is not supported by the evidence presented in the review.