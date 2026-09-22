## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods summary, funding, data availability)
- **Assessment boundary** Scientific claims, methodology, evidence consistency, and interpretation as presented in the provided text. No external literature or unpublished data were consulted.
- **Shared manuscript claim summary** The authors use coarse-grained molecular dynamics simulations of a four-component model (AMPA receptor/TARP, NMDA receptor/GluN2Bc, PSD-95, CaMKII) to show that CaMKII activation induces multiphase separation into AMPA-containing and NMDA-containing phases, that the phase arrangement is reversed between 3D solution and 2D membrane-bound systems, and that this reversal arises from a shift in balance between non-specific excluded volume interactions (dominant in 3D) and specific multivalent interactions (dominant in 2D).
- **Visible evidence base** Results sections describing simulation outcomes, figures referenced (Figures 1-6, several supplements), methods summary, and data availability statement. No actual figures, tables, or supplementary files were provided for inspection.
- **Missing materials affecting confidence** All figures, figure supplements, videos, appendices, and the detailed methods section are referenced but not included. Quantitative data (e.g., density profiles, cluster size distributions, valency measurements) are described qualitatively only. The Zenodo repository is cited but was not accessed.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and interesting question: how membrane geometry alters the balance of interaction types in multiphase biomolecular condensates, using the postsynaptic density as a model. The central claim, that CaMKII's high valency and large volume produce opposite phase arrangements in 3D versus 2D, is mechanistically plausible and potentially significant. However, the provided text is insufficient to fully evaluate the technical soundness of the simulations, the robustness of the results, or the strength of the evidence for the proposed mechanism. The qualitative descriptions of simulation outcomes, without access to the figures or quantitative analysis, limit the ability to verify the claims. The manuscript would benefit from clearer presentation of quantitative metrics and a more direct test of the proposed mechanism.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, membrane-associated signaling complexes, and synaptic biology. The work is relevant to those interested in how dimensionality and geometry influence condensate organization, and to computational biologists developing coarse-grained models of cellular processes. The proposed general principle, that reduced dimensionality shifts the balance from non-specific to specific interactions, could have broad implications for understanding membrane-associated condensates beyond the PSD.
- **Major strengths**
  - The question is well-motivated and addresses a specific, puzzling experimental observation (reversed multiphase morphology between solution and membrane).
  - The model system is biologically relevant and the four-component representation captures key features of the PSD.
  - The proposed mechanism, competition between valency-driven specific interactions and volume-driven non-specific interactions modulated by geometry, is conceptually clear and testable.
  - The use of a mesoscale model with calibrated interaction parameters based on experimental data is appropriate for the timescales and length scales of interest.
  - The authors attempt to connect their findings to broader principles of condensate organization in different cellular environments.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that the simulations "reproduce the core-shell structure in 3D in vitro solution" and "obtain a reversed morphology on the membrane," and that this reversal is "primarily driven by CaMKII's high valency and large volume."
- **Evidence pointer** Results sections "Multiphasic structures of PSD are induced by CaMKII activation," "Specific and non-specific interactions in 3D/2D systems," Figures 2-4
- **Concern** The central claims of the paper rest on visual inspection of simulation snapshots and qualitative descriptions of density distributions. No quantitative metrics are provided in the text to support the assignment of "core-shell," "Janus," or "reversed" morphologies. The reader cannot assess the statistical significance of the observed differences, the degree of variability between simulation repeats, or the robustness of the morphology assignments. Without quantitative measures (e.g., radial distribution functions, order parameters, cluster size distributions with error bars), the claims of reproduction and reversal are not fully supported by the evidence presented.
- **Why it matters** The paper's main conclusions depend on the reliability and reproducibility of the observed phase morphologies. If the morphology assignments are subjective or the differences are within statistical noise, the central claims would be weakened. Quantitative validation is essential for a computational study making mechanistic claims.
- **Resolution test** Provide quantitative metrics for phase morphology (e.g., density profiles along the radial direction, contact probabilities, cluster size distributions) with error bars across independent simulation repeats. Show that the assigned morphologies are statistically distinct between conditions and robust to simulation length and system size.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic support
- **Claim pointer** The manuscript claims that "the layered structures of receptors and CaMKIIs reduce the excluded volume effects of CaMKII on receptors, making the multivalent interaction dominant" in the 2D system.
- **Evidence pointer** Results section "Roles of CaMKII in 3D/2D systems," Figure 3
- **Concern** The proposed mechanism, that layering reduces excluded volume effects, is presented as a hypothesis but the evidence for it is indirect. The authors show that non-specific contacts are reduced in 2D and that effective valency is higher, but they do not directly demonstrate that the layering itself is the cause of this reduction. The perturbation experiments (reducing CaMKII volume in 3D, reducing valency in 2D) are informative, but the text does not provide a quantitative analysis of how these perturbations affect the balance of interaction energies or the resulting morphologies. The causal link between layering, reduced excluded volume, and the observed reversal is asserted rather than demonstrated.
- **Why it matters** The paper proposes a specific physical mechanism. If the mechanism is not directly supported, the explanatory power of the study is diminished. A more direct test, such as computing the contribution of excluded volume interactions to the free energy of different phase arrangements, would strengthen the claim.
- **Resolution test** Perform a free energy decomposition or a systematic analysis of interaction energies in the 3D and 2D systems. Show quantitatively that the excluded volume contribution to the free energy is reduced in the 2D layered arrangement, and that this reduction is necessary for the observed morphology.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Model validation
- **Claim pointer** The manuscript states that "we built a mesoscale model based on available experimental data" and that the model reproduces experimental observations.
- **Evidence pointer** Results section "Mesoscale model for multivalent protein LLPS," Methods summary
- **Concern** The validation of the model is described only briefly. The text mentions that the dissociation constants between specific pairs were calibrated from experiments, but it is not clear how the non-specific interaction parameters were determined, how sensitive the results are to these parameters, or whether the model was validated against any quantitative experimental data beyond the qualitative phase behavior. The statement that the model reproduces experimental observations is not backed by a systematic comparison.
- **Why it matters** The reliability of the conclusions depends on the fidelity of the model. If the non-specific interaction parameters are not well-constrained, the predicted balance between specific and non-specific interactions could be an artifact of the parameter choice. A sensitivity analysis would help establish the robustness of the findings.
- **Resolution test** Provide a sensitivity analysis of the key parameters (e.g., non-specific interaction strength, CaMKII size, valency) and show that the qualitative conclusions are robust to reasonable variations. Compare simulation results to quantitative experimental data where available (e.g., cluster sizes, densities).

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The manuscript claims that "membrane-associated condensates and condensates in nuclei may have evolved differential interaction features under distinct pressures resulting from their differences in dimensionality."
- **Evidence pointer** Discussion section
- **Concern** This is a broad generalization based on a single model system. While the authors discuss the difference in interaction types between membrane-associated and nuclear condensates, they do not provide evidence that this difference is a result of evolutionary pressure or that it is a general phenomenon. The claim goes beyond the scope of the simulations presented.
- **Why it matters** Overgeneralization can mislead readers into thinking the findings are more universal than they are. The authors should either temper this claim or provide additional evidence or discussion of other systems that support it.
- **Resolution test** Soften the claim to a speculation or hypothesis, or provide a more thorough discussion of other membrane-associated and nuclear condensate systems that support the proposed general principle.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract and Results
- **Evidence pointer** Abstract, Results section "Multiphasic structures of PSD are induced by CaMKII activation"
- **Issue** The term "reversed morphology" is used without a clear definition. The reader must infer what "reversed" means in the context of the core-shell structure.
- **Required correction** Define "reversed" explicitly, e.g., "in the 3D system, the AMPA-containing phase forms the core and the NMDA-containing phase forms the shell, whereas in the 2D system, the NMDA-containing phase is located closer to the membrane center and the AMPA-containing phase is at the periphery."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Methods summary
- **Issue** The methods summary is too brief to allow reproduction of the simulations. Key details, such as the exact form of the non-specific interaction potential, the parameter values used, and the simulation protocol, are deferred to an appendix that was not provided.
- **Required correction** Provide a more detailed methods description in the main text or ensure the appendix is accessible and contains all necessary parameters and protocols.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Results section "Reduction of CaMKII valency can invert multiphasic structure in 2D system"
- **Evidence pointer** Figure 5
- **Issue** The text describes the results of reducing CaMKII valency but does not provide a clear quantitative measure of the "inversion" or how it was determined.
- **Required correction** Provide a quantitative metric (e.g., the fraction of NMDA receptors located within a certain distance of the cluster center) to support the claim of inversion.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion of the limitations mentions that "parameter calibration contains some uncertainty" but does not discuss how this uncertainty might affect the specific conclusions about the balance of interactions.
- **Required correction** Add a brief discussion of how parameter uncertainty could impact the predicted balance between specific and non-specific interactions and the resulting morphology.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Lack of quantitative metrics for phase morphology and statistical analysis.
  - R1-M2: Indirect evidence for the proposed mechanism; no direct demonstration of the causal role of layering in reducing excluded volume effects.
  - R1-M3: Insufficient model validation and sensitivity analysis.

- **Assessment against Nature-style criteria**
  - **Originality** The work addresses a novel question about how membrane geometry alters the balance of interaction types in multiphase condensates. The specific application to the PSD and the proposed mechanism are original. However, the general concept of competition between specific and non-specific interactions is not new.
  - **Scientific importance** The findings could be important for understanding the organization of membrane-associated condensates and for reconciling differences between in vitro and in vivo observations. The proposed general principle, if validated, could have broad implications.
  - **Interdisciplinary readership** The topic is of interest to biophysicists, cell biologists, and neuroscientists. The conceptual framework is accessible, but the technical details of the simulations may limit readability for non-specialists.
  - **Technical soundness** The technical soundness cannot be fully assessed from the provided text. The methods are described only briefly, and the key results are presented qualitatively. The lack of quantitative analysis and sensitivity testing is a significant concern.
  - **Readability for nonspecialists** The manuscript is generally well-written and the conceptual argument is clear. However, the results section relies heavily on qualitative descriptions of simulations, which may be difficult for non-specialists to follow without the figures. The discussion of the mechanism is accessible.

- **Recommendation posture** Supportive if technical concerns are resolved. The central question is interesting and the proposed mechanism is plausible. However, the current evidence, as presented in the text, is insufficient to fully establish the claims. The authors must provide quantitative support for the phase morphology assignments, a more direct test of the proposed mechanism, and a sensitivity analysis of the model parameters. If these concerns are addressed, the manuscript could make a valuable contribution.

## Risk / unsupported claims
- The claim that the simulations "reproduce" experimental observations is not fully supported without a quantitative comparison to experimental data.
- The claim that "the layered structures of receptors and CaMKIIs reduce the excluded volume effects" is a hypothesis that is not directly demonstrated.
- The claim that "membrane-associated condensates and condensates in nuclei may have evolved differential interaction features" is a speculation that goes beyond the presented evidence.
- The claim that reducing CaMKII volume in 3D or valency in 2D "inverts" the morphology is not supported by quantitative metrics in the text.
- The statement that the model is "based on available experimental data" is not fully verifiable without details on the calibration of non-specific interaction parameters.