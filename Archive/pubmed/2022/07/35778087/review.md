## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, and conclusions as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors present dynamical simulations of icosahedral protein shell assembly around a bicomponent fluid cargo, motivated by bacterial microcompartments. They claim that relative cargo–cargo interaction strengths determine encapsulated amount, composition, and spatial organization, while shell–shell and shell–cargo affinities modulate these outcomes through coupled thermodynamic and kinetic effects. They further suggest implications for natural microcompartment function, synthetic biology, and the role of self-assembly coupled to liquid–liquid phase separation in cellular organization.
- **Visible evidence base** Full manuscript text including abstract, introduction, results, discussion, methods, and figure captions (figures themselves not visible)
- **Missing materials affecting confidence** Figures and tables referenced in the text (Figs. 1–8, Table I) are not provided; simulation trajectory data and analysis code are not available for independent verification; appendices A and B are referenced but not included in the provided text

## Reviewer

- **Overall assessment** This manuscript presents a systematic computational study of a minimal model for microcompartment assembly around a two-component cargo. The work extends prior single-species models to a multicomponent system, which is a relevant and timely step given the biological importance of multicomponent encapsulation in bacterial microcompartments and the growing interest in synthetic nanoreactors. The authors identify parameter regimes where shell assembly couples to cargo compositional fluctuations, leading to purified encapsulation, and they distinguish equilibrium from kinetic effects using a permeable-shell comparison. The conclusions are generally well supported by the described simulation protocols and analyses, though the absence of the actual figures limits full verification. The manuscript is clearly written and should interest researchers in biophysics, soft matter, and synthetic biology. However, several technical aspects require clarification or additional analysis before the case is fully established.

- **Who would be interested in the results, and why** Researchers studying bacterial microcompartments, virus assembly, and protein-shell self-assembly will find the results directly relevant. The work also speaks to the broader community interested in liquid–liquid phase separation in biological systems, particularly the coupling between phase separation and self-assembly. Synthetic biologists designing nanoreactors or encapsulation systems for multienzyme cascades will value the predictions about how interaction parameters control cargo loading and composition. The methodological approach, using a minimal coarse-grained model with systematic parameter sweeps, will appeal to computational biophysicists.

- **Major strengths** 
  1. The study addresses a biologically and technologically important question: how multicomponent cargoes are encapsulated by self-assembling protein shells, which has not been systematically explored in prior computational work.
  2. The model is carefully designed to isolate key interaction parameters, and the authors make reasonable choices to keep the parameter space tractable.
  3. The comparison between dynamical assembly simulations and permeable-shell equilibrium simulations is a clever and effective way to disentangle thermodynamic from kinetic effects.
  4. The identification of distinct assembly pathways (one-step vs. two-step) and their consequences for cargo purification is a valuable conceptual contribution.
  5. The manuscript is well organized and clearly written, with a logical progression from bulk phase behavior to assembly dynamics to mechanistic interpretation.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "the relative cargo–cargo affinities are the most important factor in determining the amount and composition of packaged cargo" and that shell–shell and shell–cargo affinities provide "an alternative means to sensitively control the packaged cargo" within certain parameter ranges.
- **Evidence pointer** Figures 4–7, Section II D
- **Concern** The manuscript text describes results from parameter sweeps over cargo–cargo, shell–cargo, and shell–shell affinities, but the actual figures are not provided. Without seeing the data, it is impossible to assess whether the claimed trends are robust, whether the observed effects are statistically significant, or whether the interpretation of the results is justified. For example, the claim that one-step vs. two-step pathways lead to different cargo compositions is central to the paper, but the supporting evidence (Figs. 3–5) cannot be evaluated.
- **Why it matters** The core conclusions of the paper rest on the quantitative and qualitative patterns shown in the figures. If the figures do not clearly support the claims, or if the statistical variability across trials is large, the conclusions may be overstated. The distinction between equilibrium and kinetic effects, and the claim that shell closure "locks" cargo composition out of equilibrium, requires careful examination of the simulation data.
- **Resolution test** Provide the figures and, if possible, the underlying data for key parameter sets. The authors should show representative trajectories, quantitative measures of cargo composition and mixing with error bars, and a clear comparison between dynamical and equilibrium simulations. The statistical significance of differences between parameter regimes should be explicitly stated.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the cargo can spatially reorganize inside of the shell even after its completion" and that shell closure prevents cargo exchange with the bulk, leading to out-of-equilibrium compositions.
- **Evidence pointer** Section II C, Section II D, Figures 3–5
- **Concern** The manuscript does not provide sufficient detail on how the authors determine that cargo exchange with the bulk is negligible after shell closure. The timescales of the simulations are described (2 × 10^6 to 2 × 10^7 timesteps), but it is not clear whether the authors have verified that cargo particles cannot escape from a closed shell on these timescales. The claim that the cargo composition is "locked" is central to the kinetic interpretation, but the evidence for this is not presented in the text.
- **Why it matters** If cargo can exchange with the bulk on simulation timescales, then the observed compositions may reflect equilibrium partitioning rather than kinetic trapping. The distinction between equilibrium and kinetic control is a key message of the paper, and it must be rigorously established.
- **Resolution test** The authors should provide quantitative evidence that cargo particles do not escape from closed shells over the simulation timescales, e.g., by tracking the number of cargo particles inside shells as a function of time after closure, or by performing test simulations with longer timescales. They should also discuss the permeability of the shell to cargo in the model and how this relates to real microcompartments.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors suggest that their results "have implications for efforts in synthetic biology to colocalize alternative sets of molecules within microcompartments to accelerate specific reactions" and that "coupling between self-assembly and multicomponent liquid–liquid phase separation may play a role in the organization of the cellular cytoplasm."
- **Evidence pointer** Abstract, Introduction, Section II D, Outlook
- **Concern** The broader implications are stated but not developed. The connection to synthetic biology is plausible but vague: the authors do not specify which design principles or parameter regimes would be most useful for engineering applications, nor do they discuss how their findings might translate to experimental systems where interactions are less tunable. Similarly, the claim about cellular organization is speculative and not grounded in specific biological examples beyond the carboxysome motivation.
- **Why it matters** For a general-interest journal, the broader significance of the work needs to be articulated more concretely. If the implications are only generic, the impact of the paper is diminished. The authors should either provide more specific predictions or clearly frame these statements as speculative outlook.
- **Resolution test** The authors should expand the discussion of implications, perhaps by identifying specific experimental systems where their predictions could be tested, or by providing more concrete design rules for synthetic microcompartments. They should also clarify which of their findings are robust and general versus specific to their model parameters.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors map their simulation parameters to biological microcompartments, estimating that the cargo diameter corresponds to r* ≈ 13 nm for carboxysomes and that model subunits are about three times larger than carboxysome hexamers.
- **Evidence pointer** Section IV B, Table I
- **Concern** The mapping to biological systems is presented briefly, and the justification for the chosen parameter ranges is not fully detailed. The authors state that they estimate relevant ranges based on experimental observations, but the reasoning is not transparent. For example, the claim that empty carboxysome shells are not observed in cells is used to justify focusing on shell–shell affinities below the empty-shell assembly threshold, but the relationship between this observation and the specific values chosen is not explained.
- **Why it matters** The biological relevance of the model depends on the parameter mapping. If the mapping is not well justified, readers may question whether the predicted behaviors are relevant to real microcompartments. The authors should provide a more detailed and transparent justification for their parameter choices.
- **Resolution test** Expand the discussion in Section IV B to explain the reasoning behind each parameter range, including the relationship between experimental observations and the chosen values. If possible, provide a sensitivity analysis showing how the results depend on the mapping assumptions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction, Section II A
- **Evidence pointer** Section II A, Figure 1
- **Issue** The model description in Section II A is concise but assumes familiarity with coarse-grained simulation approaches. Terms like "pseudoatoms," "Attractors," and "Excluders" are introduced without a clear intuitive explanation of their physical meaning.
- **Required correction** Briefly explain the physical interpretation of each model component in plain language, perhaps with a schematic figure or a short paragraph describing the design rationale.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, Section IV C
- **Evidence pointer** Section IV C
- **Issue** The simulation protocol is described, but the choice of simulation length is not justified. The authors state that most simulations were run for 2 × 10^6 timesteps and longer for two-step assembly, but it is not clear how they determined that these timescales are sufficient for convergence.
- **Required correction** Provide evidence that the simulation timescales are sufficient, e.g., by showing that key observables have converged or by discussing the relevant relaxation timescales in the system.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section II D 2, Figure 8
- **Evidence pointer** Section II D 2, Figure 8
- **Issue** The comparison between dynamical and equilibrium simulations is described, but the details of the equilibrium simulations are not fully specified. It is not clear how the permeable shell is implemented and whether this implementation could introduce artifacts.
- **Required correction** Provide more detail on the equilibrium simulation setup, including how permeability is achieved and how the results might depend on this choice.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interdisciplinary readership
- **Affected element** Abstract, Introduction
- **Evidence pointer** Abstract, Introduction
- **Issue** The abstract and introduction are written primarily for a biophysics audience. The broader significance for cell biology or synthetic biology is mentioned but not explained in accessible terms.
- **Required correction** Add a sentence or two in the introduction that explains, for a general scientific audience, why understanding microcompartment assembly matters and how the findings could be relevant beyond the specific model system.

- **Technical failings that need to be addressed before the case is established** R1-M1 and R1-M2 are blocking. The central claims about the role of cargo–cargo affinities and the kinetic trapping of cargo composition cannot be fully evaluated without the figures and without explicit evidence that cargo exchange is negligible after shell closure. R1-M3 and R1-M4 are non-blocking but should be addressed to strengthen the paper.

- **Assessment against Nature-style criteria** 
  - **Originality**: The work extends prior single-species models to a two-component cargo, which is a meaningful advance. The identification of pathway-dependent compositional control is a novel contribution. However, the model is a relatively straightforward extension of existing frameworks, and the conceptual insights, while useful, are not entirely unexpected given the known behavior of multicomponent phase separation.
  - **Scientific importance**: The question of how multicomponent cargoes are encapsulated is important for understanding bacterial microcompartments and for synthetic biology. The findings provide specific predictions that could guide experimental work. However, the model is minimal, and the direct relevance to real systems remains to be established.
  - **Interdisciplinary readership**: The topic bridges biophysics, cell biology, and synthetic biology, and the manuscript is written in a way that should be accessible to researchers in these fields. However, the broader implications are not developed enough to capture the attention of a wide interdisciplinary audience.
  - **Technical soundness**: The simulation methodology is appropriate, and the comparison between dynamical and equilibrium simulations is a strength. However, the lack of figures and the insufficient detail on key technical points (e.g., cargo exchange after shell closure) prevent full assessment.
  - **Readability for nonspecialists**: The manuscript is clearly written, but some model details and the significance of the findings could be explained more accessibly for readers outside the immediate field.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses a relevant and timely question, and the approach is sound in principle. However, the blocking concerns regarding the evidence for the central claims must be resolved before the case is established. The authors should provide the figures and additional analysis to support their conclusions, and they should strengthen the discussion of broader implications.

## Risk / unsupported claims
- The claim that "the relative cargo–cargo affinities are the most important factor in determining the amount and composition of packaged cargo" is not fully supported without the figures showing the parameter sweeps.
- The claim that shell closure "locks" the cargo composition out of equilibrium is not supported by direct evidence presented in the text.
- The claim that "coupling between self-assembly and multicomponent liquid–liquid phase separation may play a role in the organization of the cellular cytoplasm" is speculative and not grounded in specific biological examples.
- The mapping of simulation parameters to biological microcompartments (r* ≈ 13 nm, subunit size ratio) is presented without sufficient justification.
- The statistical significance of differences between parameter regimes is not explicitly stated in the text.