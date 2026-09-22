## Review setup
- **Input scope** Full manuscript text (abstract, introduction, models, results, discussion, code availability, acknowledgments)
- **Assessment boundary** Scientific content, methodological soundness, claims versus evidence, and presentation quality. Not assessed: code functionality, reproducibility of GitHub repository, editorial fit.
- **Shared manuscript claim summary** The authors present a computational rheometry framework for modeling viscoelastic networks, comparing edge-based Jeffreys networks with node-based Stokes-Maxwell networks. They apply this framework to random graphs, structured graphs, and networks extracted from coarse-grained simulations of biomolecular condensates formed by the prion-like low complexity domain of hnRNP-A1. They report that network topology, connectivity, and hydrodynamic coupling influence dynamic moduli and creep responses, and propose that a combination of rheometric tests is necessary to distinguish microstructural models.
- **Visible evidence base** Main text figures referenced: Figs. 2a–f, 3a–f, 4a–i, 5a–f, 6a–d, 7a–c, 8a–d, 9a–f, 10a–f, 11a–f. Appendices A–J referenced but not provided in the submitted material.
- **Missing materials affecting confidence** Appendices A–J (derivations, numerical methods, simulation details, parameter conversion protocols) are referenced but not included. Figure panels are described but not visible. Simulation code is not yet available at the stated GitHub repository. Experimental data from prior publications (e.g., refs. 41, 51) are cited but not reproduced.

## Reviewer
- **Overall assessment** This manuscript presents a systematic computational framework for bridging molecular-scale network structure to mesoscale viscoelastic responses in biomolecular condensates. The conceptual advance is meaningful: the authors demonstrate that different network models (Jeffreys vs. Stokes-Maxwell) yield qualitatively different predictions, and that no single rheometric test is sufficient to uniquely identify microstructural parameters. The workflow from coarse-grained simulations to graph extraction to rheological prediction is timely and potentially useful to the condensate community. However, the manuscript as submitted has several technical gaps that prevent full evaluation. The appendices containing essential derivations and numerical details are not provided, making it impossible to verify the correctness of the implementation. The comparison between models is largely qualitative, with limited quantitative metrics for model discrimination. The connection to experimental observables, while discussed, is not demonstrated with actual experimental data. The claims regarding the universality of certain scaling behaviors (e.g., G′∝ω1/2, G′′∝ω2/3) rest on limited parameter exploration. The manuscript would benefit from clearer articulation of the novelty relative to the prior work of Wróbel et al. and from a more explicit statement of the limitations of the linear viscoelastic assumption in the context of condensate mechanics.
- **Who would be interested in the results, and why** Researchers studying the mechanical properties of biomolecular condensates, particularly those using optical tweezers, microrheology, or DLS-based rheology. Computational biophysicists developing coarse-grained models of phase-separating systems. Soft matter physicists interested in viscoelastic network theory. Experimentalists seeking a framework to interpret rheological measurements in terms of microstructural parameters. The work is also relevant to those studying intracellular phase behavior and mechanosensing.
- **Major strengths** 1. The conceptual framing of condensates as viscoelastic networks with explicit hydrodynamic coupling is well motivated and timely. 2. The systematic comparison of Jeffreys and Stokes-Maxwell models across multiple network topologies is thorough and informative. 3. The workflow from simulation to graph to rheology is clearly articulated and potentially transformative for the field. 4. The emphasis on the insufficiency of single rheometric tests is an important practical message. 5. The discussion of boundary condition effects on rheometric outcomes is valuable and often overlooked. 6. The writing is generally clear and accessible to a broad audience.
- **Major Concerns** 
  - **R1-M1** (Blocking: Yes)
  - **R1-M2** (Blocking: Yes)
  - **R1-M3** (Blocking: No)
  - **R1-M4** (Blocking: No)
  - **R1-M5** (Blocking: No)
- **Minor Comments** 
  - **R1-m1** (Severity: Minor)
  - **R1-m2** (Severity: Minor)
  - **R1-m3** (Severity: Minor)
  - **R1-m4** (Severity: Minor)
  - **R1-m5** (Severity: Minor)
- **Technical failings that need to be addressed before the case is established** R1-M1 (missing appendices), R1-M2 (lack of quantitative model discrimination metrics), R1-M3 (limited parameter exploration for scaling claims)
- **Assessment against Nature-style criteria** 
  - **Originality** Moderate. The computational rheometry framework itself is adapted from Wróbel et al., and the application to condensate networks is novel. However, the conceptual insight that different network models predict different rheology is not entirely new to soft matter physics. The originality lies in the specific application and the systematic comparison.
  - **Scientific importance** High for the condensate field. The ability to connect molecular-scale interactions to mesoscale mechanical responses is a major open problem. This framework provides a concrete path forward. The importance is somewhat limited by the lack of direct experimental validation.
  - **Interdisciplinary readership** Moderate. The work bridges computational biophysics, soft matter physics, and cell biology. However, the technical nature of the rheological modeling may limit accessibility to cell biologists. The authors make an effort to explain concepts, but the manuscript assumes familiarity with viscoelasticity theory.
  - **Technical soundness** Cannot be fully assessed. The core derivations and numerical methods are in the missing appendices. The results presented are plausible and internally consistent, but verification is impossible without the appendices. The comparison between models is qualitative, and the parameter space explored appears limited.
  - **Readability for nonspecialists** Good. The manuscript is well-written with clear figures (as described). The authors provide intuitive explanations of the models and their differences. The abstract and introduction are accessible. The results section is more technical but remains understandable.
- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual framework is valuable and the workflow is potentially transformative. However, the missing appendices and lack of quantitative model discrimination metrics prevent full endorsement. The authors should provide the appendices, add quantitative metrics for model comparison, and ideally include a demonstration on experimental data or a clear statement of how such a comparison would be performed.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims to present a complete computational rheometry framework with derivations and numerical methods detailed in Appendices A–J.
- **Evidence pointer** Appendices A–J (referenced throughout the main text, not provided in the submitted material)
- **Concern** The appendices containing the essential derivations (two-fluid model, hydrodynamic screening length, regularized Stokeslet method, numerical implementation details, parameter conversion protocols, simulation details for LaSSI, Mpipi-Recharged, and CALVADOS) are not included in the submitted material. Without these, the technical correctness of the framework cannot be evaluated. The main text refers to equations and methods that are not visible.
- **Why it matters** The core contribution of this work is a computational framework. If the derivations or numerical implementations contain errors, all subsequent results are compromised. The scientific community cannot assess or build upon this work without the full methodological details.
- **Resolution test** Provide the complete appendices. The derivations should be checked for mathematical consistency. The numerical methods should be described with sufficient detail for independent reproduction. The parameter conversion protocols should be clearly specified.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that "No single test provides definitive assessments of the material properties and microstructures" and that a range of tests is essential for distinguishing different network types.
- **Evidence pointer** Figs. 2–6, 8–11 (described in text, not visible)
- **Concern** The claim that multiple rheometric tests are needed to distinguish models is central to the paper's message. However, the evidence presented appears to be qualitative. The manuscript describes differences in dynamic moduli and creep responses between models, but does not provide quantitative metrics for model discrimination (e.g., statistical measures of fit quality, sensitivity analyses, or explicit criteria for when two models are distinguishable given experimental noise). Without such metrics, the claim that "no single test is sufficient" is not rigorously established.
- **Why it matters** The practical value of this framework depends on its ability to guide experimental design. If the authors cannot specify how many measurements, at what frequencies, and with what precision are needed to distinguish models, the framework's utility is limited. The claim of insufficiency of single tests is strong and requires quantitative support.
- **Resolution test** Add quantitative model discrimination analyses. For example, compute the minimum number of measurements or the required precision to distinguish Jeffreys from Stokes-Maxwell networks at a given confidence level. Provide sensitivity analyses showing how parameter uncertainties propagate to predicted rheological responses. If possible, demonstrate the framework on a synthetic dataset with known ground truth.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the Stokes-Maxwell model exhibits G′∝ω1/2 and G′′∝ω2/3 scaling in intermediate frequency regimes, and that this behavior was observed in DLS experiments by Fisher and Obermeyer.
- **Evidence pointer** Fig. 11b, 11e (described in text, not visible)
- **Concern** The scaling exponents (1/2 and 2/3) are presented as characteristic signatures of the Stokes-Maxwell model. However, the parameter exploration appears limited. The manuscript describes results for specific values of E and η, but does not demonstrate that these scaling exponents are robust across a wide range of parameters. It is unclear whether these exponents are universal to the model or specific to the chosen parameter values. Additionally, the comparison to the Fisher and Obermeyer data is qualitative; no quantitative fit or statistical comparison is shown.
- **Why it matters** If the scaling exponents are not robust, they cannot serve as reliable signatures for identifying Stokes-Maxwell behavior in experimental data. The claim of agreement with experimental observations is a key selling point of the framework and requires quantitative support.
- **Resolution test** Perform a systematic parameter sweep (e.g., varying E and η over several orders of magnitude) and show that the scaling exponents are stable. Provide a quantitative comparison to the Fisher and Obermeyer data, including best-fit parameters and goodness-of-fit metrics. If the exponents vary with parameters, characterize the conditions under which they emerge.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that networks extracted from three different coarse-grained simulation models (LaSSI, Mpipi-Recharged, CALVADOS) yield consistent network characteristics and rheological responses.
- **Evidence pointer** Figs. 7–8 (described in text, not visible)
- **Concern** The comparison of three simulation models is a strength, but the manuscript does not provide quantitative metrics for the consistency of network characteristics (e.g., degree distributions, clustering coefficients, path lengths) across models. The claim of consistency is based on visual inspection of figures that are not visible. It is unclear whether the differences between models are within statistical uncertainty or represent systematic biases.
- **Why it matters** The robustness of the framework across different simulation models is important for its general applicability. If different models yield significantly different network structures, the choice of simulation model becomes a critical parameter that must be justified.
- **Resolution test** Provide quantitative comparisons of network statistics across the three models, including means, standard deviations, and statistical tests for differences. Show that the rheological predictions are robust to the choice of simulation model, or characterize the conditions under which they diverge.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that the framework can bridge molecular-scale interactions to mesoscale viscoelastic responses, and that this is relevant for understanding condensate mechanics.
- **Evidence pointer** Figs. 10–11 (described in text, not visible)
- **Concern** The temperature-dependent studies (Fig. 10) and parameter sweeps (Fig. 11) are performed on networks extracted from LaSSI simulations. The manuscript does not discuss how the choice of E and η values relates to actual molecular parameters (e.g., sticker energies, chain stiffness, solvent quality). Without a mapping from molecular parameters to E and η, the framework's predictive power for specific condensate systems is limited.
- **Why it matters** The ultimate goal is to predict condensate rheology from molecular sequence and interactions. If the connection between molecular parameters and the phenomenological E and η is not established, the framework remains a descriptive tool rather than a predictive one.
- **Resolution test** Discuss how E and η could be estimated from molecular simulations or experiments. Provide a concrete example of how the framework would be applied to a specific condensate system, including the steps to obtain E and η from molecular parameters.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Introduction, paragraph 1
- **Evidence pointer** Location not provided
- **Issue** The introduction lists many experimental techniques for probing condensate rheology but does not clearly state which techniques are most compatible with the proposed computational framework.
- **Required correction** Add a sentence or two explicitly connecting the listed experimental techniques to the computational framework, indicating which techniques produce data that can be directly compared to model predictions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section "Edge-based Jeffreys networks"
- **Evidence pointer** Location not provided
- **Issue** The constitutive relation in Eq. 2 is presented without derivation or physical motivation. The relationship between the Jeffreys element parameters and molecular-scale properties is not discussed.
- **Required correction** Provide a brief physical interpretation of the Jeffreys element parameters and their expected ranges for condensate systems. This would help readers connect the model to physical intuition.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section "Random graphs in a spherical domain"
- **Evidence pointer** Location not provided
- **Issue** The choice of spherical domain and the specific values of R and rc are not justified. The sensitivity of results to these choices is not discussed.
- **Required correction** Add a brief justification for the domain geometry and cutoff distances. Discuss how the results might change for different domain shapes or boundary conditions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion, paragraph 2
- **Evidence pointer** Location not provided
- **Issue** The discussion of the connection to Oldroyd-B-type constitutive equations is brief and does not specify how the network parameters map to continuum model parameters.
- **Required correction** Expand this discussion to provide a more explicit mapping between network parameters and continuum constitutive parameters, or state clearly that such a mapping is not yet established.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract
- **Evidence pointer** Location not provided
- **Issue** The abstract is dense and uses technical terms (e.g., "computational rheometry", "Stokes-Maxwell") without defining them. This may limit accessibility to readers outside the immediate field.
- **Required correction** Briefly define or contextualize key technical terms in the abstract to improve accessibility for a broader audience.

## Risk / unsupported claims
- The claim that "No single test provides definitive assessments of the material properties and microstructures" is not quantitatively supported (R1-M2).
- The claim of agreement with DLS experiments by Fisher and Obermeyer is qualitative and lacks statistical rigor (R1-M3).
- The claim of consistency across three simulation models is not quantitatively demonstrated (R1-M4).
- The claim that the framework can bridge molecular-scale interactions to mesoscale responses is not fully supported without a mapping from molecular parameters to E and η (R1-M5).
- The technical correctness of the framework cannot be assessed without the missing appendices (R1-M1).
- The claim that condensates lie between the strongly screened and strong coupling limits (based on estimates of 0.1<ℋ<2) is presented without showing the underlying calculations or sensitivity to assumptions.