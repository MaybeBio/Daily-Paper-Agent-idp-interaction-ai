## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion) as provided by the user.
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims based solely on the supplied text. No external literature or unpublished data are considered.
- **Shared manuscript claim summary** The authors use MARTINI v3.0 coarse-grained molecular dynamics simulations to study the interaction between poly-glutamate (E30) and poly-lysine (K30) coacervates and lipid bilayers of varying anionic lipid (POPG) content. They report that stable coacervate-bilayer wetting requires >20% anionic lipids, that wetting induces negative membrane curvature and local lipid demixing, that polyelectrolyte-polyelectrolyte contacts decrease while polyelectrolyte-lipid and polyelectrolyte-ion contacts increase upon wetting, and that coacervate formation precedes bilayer wetting in kinetic simulations.
- **Visible evidence base** Main text figures referenced (Fig. 1–8), equations (1)–(6), and references to ESI figures and tables (Fig. S1–S4, Table S1–S3). No actual figure data, numerical values, or ESI content are provided in the supplied material.
- **Missing materials affecting confidence** Actual figure data, numerical values, simulation trajectories, ESI content, and detailed parameter tables are not available. The manuscript text alone does not allow quantitative verification of the reported trends or magnitudes.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and biologically relevant question: how complex coacervates interact with and remodel lipid membranes. The authors employ a well-established coarse-grained model (MARTINI v3.0) and present a systematic exploration of lipid composition effects. The qualitative findings, such as the threshold for wetting, negative curvature generation, and lipid demixing, are plausible and consistent with existing theoretical frameworks. However, the manuscript as provided has several significant limitations. The evidence base is incomplete, with no quantitative data shown in the text, and several claims are made without sufficient support. The kinetic interpretation is based on limited simulation setups, and the generalizability to more complex IDP systems is asserted rather than demonstrated. The work is potentially valuable but requires substantial revision and additional analysis to fully establish its conclusions.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, membrane biophysics, and computational biophysics would find this study relevant. The work provides a molecular-level view of coacervate-membrane interactions, which is of interest to those studying phase separation at membranes, membrane remodeling mechanisms, and the design of synthetic polyelectrolyte systems for biomedical applications. The use of MARTINI v3.0 for this system also appeals to the coarse-grained simulation community.
- **Major strengths** The study addresses a gap in the literature by systematically examining coacervate-membrane interactions with a molecular model. The choice of a well-characterized polyelectrolyte pair (E30/K30) and a range of lipid compositions is logical. The authors connect their observations to existing theoretical models, which strengthens the interpretation. The kinetic simulations add a dynamic perspective that is often missing in such studies.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (lack of quantitative evidence), R1-M2 (kinetic interpretation), R1-M3 (generalizability), R1-M4 (force-field validation).
- **Assessment against Nature-style criteria**  
  - **Originality** Moderate. The specific system (E30/K30 coacervates on lipid bilayers) has not been studied before, and the finding of counterion-driven wetting is a novel contribution. However, the general phenomena of curvature generation and lipid demixing by adsorbed polymers are well established.  
  - **Scientific importance** Moderate to high. Understanding coacervate-membrane interactions is relevant to cellular signaling and membrane remodeling, but the model system is simplified and the direct biological implications are not fully explored.  
  - **Interdisciplinary readership** Moderate. The topic bridges biophysics, soft matter, and cell biology, but the technical nature of the simulations may limit broader appeal.  
  - **Technical soundness** The simulation methodology is appropriate, but the lack of quantitative data and limited validation reduce confidence. The comparison to theory is qualitative and does not fully establish the mechanisms.  
  - **Readability for nonspecialists** The manuscript is generally well-written but assumes familiarity with coarse-grained simulations and phase separation concepts. Some sections, such as the theory comparison, may be challenging for a general audience.  
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising, but the current evidence base is insufficient to fully support the claims. Additional quantitative data, more robust kinetic analysis, and a clearer discussion of limitations are required.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The manuscript claims that "more than 20% anionic lipids are required for the coacervate to form stable contact with the bilayer" and that "the magnitude of negative curvature, extent of lipid demixing, and asphericity of the coacervate increase with the concentration of anionic lipids."  
- **Evidence pointer** Results section, Fig. 1–4; location not provided for specific data points.  
- **Concern** The text describes trends and qualitative observations but does not provide any numerical values, error bars, or statistical analyses. For example, the claim of a threshold at 20% POPG is based on a visual inspection of Fig. 1, but no quantitative criterion for "stable contact" is defined. Similarly, the increase in curvature and demixing is described qualitatively without reporting the actual values or uncertainties. This makes it impossible to assess the robustness of the findings.  
- **Why it matters** The central conclusions of the paper rest on these quantitative trends. Without numerical data, the claims are not verifiable and the scientific case is not established.  
- **Resolution test** Provide quantitative values for contact numbers, curvature, demixing parameters, and asphericity for all systems, including standard deviations or confidence intervals. Define a clear threshold criterion for wetting and show that the trend is statistically significant.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Interpretation of kinetics  
- **Claim pointer** The manuscript claims that "coacervate formation precedes bilayer wetting" based on kinetic simulations.  
- **Evidence pointer** Results section, Fig. 6 and 7; location not provided for specific time points.  
- **Concern** The kinetic simulations are described as starting from randomly distributed polyelectrolytes, but the number of independent simulations, the reproducibility of the observed sequence of events, and the criteria for defining "coacervate formation" and "wetting" are not specified. The claim that coacervate formation precedes wetting is based on a limited number of trajectories, and it is unclear whether this is a general result or specific to the chosen conditions.  
- **Why it matters** The temporal ordering of events is a key mechanistic claim. If not robustly supported, the interpretation of the wetting process could be incorrect.  
- **Resolution test** Report the number of independent simulations, show representative time courses for multiple replicates, and define quantitative criteria for coacervate formation and wetting. Demonstrate that the ordering is consistent across replicates and conditions.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** No  
- **Axis** Generalizability  
- **Claim pointer** The manuscript concludes that "the present study demonstrates that poly-glutamate and poly-lysine coacervate possesses a remarkable ability to remodel anionic lipid membranes" and suggests relevance to "synthetic IDPs in biology and medicine."  
- **Evidence pointer** Concluding remarks; location not provided.  
- **Concern** The study uses a single coacervate system (E30/K30) and simple lipid bilayers. The claim of generalizability to more complex IDPs and biological membranes is not supported by the data. The authors acknowledge this in the conclusion but still frame the findings as broadly relevant.  
- **Why it matters** Overgeneralization could mislead readers about the applicability of the results to real biological systems.  
- **Resolution test** Either temper the claims to be specific to the model system or provide additional simulations with different polyelectrolyte sequences or more complex lipid compositions to demonstrate broader relevance.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Force-field validation  
- **Claim pointer** The manuscript states that "the parameters are kept the same as those in Marrink et al., who could reproduce the ion concentration dependence of coacervation for poly-E/poly-K mixtures using the same parameters."  
- **Evidence pointer** System and simulation details; location not provided.  
- **Concern** The authors rely on a previous study for force-field validation but do not provide any additional validation for the membrane-coacervate interaction. The MARTINI v3.0 model is known to have limitations in capturing certain electrostatic and entropic effects, which the authors acknowledge in the energetics section. However, the impact of these limitations on the specific findings is not discussed.  
- **Why it matters** If the force-field does not accurately capture the relevant interactions, the conclusions could be artifacts of the model.  
- **Resolution test** Provide a more detailed discussion of the limitations of MARTINI v3.0 for this system, and if possible, include comparisons with atomistic simulations or experimental data to validate the key findings.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity of methods  
- **Affected element** Simulation details  
- **Evidence pointer** System and simulation details; location not provided.  
- **Issue** The description of the simulation setup is incomplete. The number of polyelectrolyte chains, the exact composition of the systems, the number of replicates, and the total simulation times are not clearly stated.  
- **Required correction** Provide a table summarizing all simulated systems, including composition, number of replicates, and simulation lengths.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Presentation of results  
- **Affected element** Figures  
- **Evidence pointer** Results section, Fig. 1–8; location not provided.  
- **Issue** The figures are referenced but not described in sufficient detail in the text. For example, the definition of "contact" and the exact method for calculating curvature are not fully explained.  
- **Required correction** Add a detailed description of the analysis methods and define all quantities shown in the figures.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Theoretical comparison  
- **Affected element** Discussion of theory  
- **Evidence pointer** Results section, Curvature generation; location not provided.  
- **Issue** The comparison to the Kim and Sung model is qualitative. The authors state that the observed curvature is in the range predicted by the theory but do not provide a quantitative comparison.  
- **Required correction** Provide a quantitative comparison between the simulated curvature values and the theoretical predictions, including the parameters used in the model.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Language and clarity  
- **Affected element** Abstract and conclusion  
- **Evidence pointer** Abstract and Concluding remarks; location not provided.  
- **Issue** The abstract and conclusion use phrases such as "remarkable ability" and "lays the groundwork" that are somewhat promotional. The scientific claims should be stated more neutrally.  
- **Required correction** Revise the language to be more measured and focused on the specific findings.

## Risk / unsupported claims
- The claim that "more than 20% anionic lipids are required for stable contact" is not quantitatively supported.
- The claim that "coacervate formation precedes bilayer wetting" is based on limited kinetic simulations and is not robustly established.
- The claim that "counterions play a major role in driving the bilayer wetting" is inferred from interaction energy analysis but not directly tested.
- The claim that the observed curvature is "in the range relevant to many realistic membrane remodeling processes" is speculative and not supported by direct comparison to biological systems.
- The generalizability of the findings to more complex IDPs and membranes is asserted but not demonstrated.