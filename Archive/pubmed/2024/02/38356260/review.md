## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract, as supplied
- **Shared manuscript claim summary** The authors propose that coiled-coil (CC) domains, through their physical features alone, are sufficient to drive liquid-liquid phase separation (LLPS) in protein models. Using a coarse-grained simulation framework, they report that proteins with as few as two CC domains can phase separate, that increasing CC number up to four modestly enhances LLPS propensity, and that trimer- and tetramer-forming CC domains show dramatically higher LLPS propensity than dimer-forming coils. They conclude that multimerization state has a greater effect on LLPS than the number of CC domains per protein, supporting the hypothesis that CC domains act as drivers of protein LLPS.
- **Visible evidence base** Abstract text only. No figures, tables, methods details, simulation parameters, or quantitative results are provided.
- **Missing materials affecting confidence** Full manuscript, simulation methodology, force field parameters, system size and concentration ranges, phase diagram definitions, order parameters for LLPS identification, statistical error analysis, comparison to experimental data, and any validation of the coarse-grained model against known CC protein behavior.

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting computational hypothesis with a clear conceptual framework. However, the evidence base is limited to qualitative statements without quantitative support. The central claim that CC domains are sufficient to drive LLPS is plausible but not established from the supplied material. The distinction between the effect of CC number and multimerization state is a useful design, but the abstract does not provide sufficient detail to assess the robustness of this conclusion. The work may appeal to a specialized biophysics audience, but its broader significance for understanding membraneless organelle formation remains speculative at this stage.
- **Who would be interested in the results, and why** Researchers studying phase separation in biology, particularly those focused on centrosome and spindle assembly, computational biophysicists developing coarse-grained models of protein interactions, and experimentalists seeking to identify LLPS-driving regions in CC-containing proteins. The results could inform hypotheses about which protein features to target in mutagenesis or localization studies.
- **Major strengths** The study addresses a timely question about the role of CC domains in LLPS, which is underexplored relative to intrinsically disordered regions. The simulation framework is designed to isolate CC-driven interactions, which is a clean conceptual approach. The comparison between CC number and multimerization state provides a clear and testable prediction.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract lacks any quantitative metrics for LLPS propensity, such as critical concentrations, binodal curves, or free energy estimates. Without these, the claims of "sufficiency" and "dramatically higher" propensity cannot be evaluated. The absence of model validation against experimental CC protein behavior is a significant gap. The abstract does not specify how LLPS is defined in the simulations, which is essential for interpreting the results.
- **Assessment against Nature-style criteria** 
  - Originality: Moderate. The idea that CC domains can drive LLPS is not entirely new, but the systematic comparison of CC number versus multimerization state is a fresh angle.
  - Scientific importance: Moderate. If confirmed, the results would extend the known drivers of LLPS beyond disordered regions, but the abstract does not demonstrate a broad biological impact.
  - Interdisciplinary readership: Limited. The abstract is written for a biophysics or computational biology audience and does not frame the findings for cell biologists or biochemists.
  - Technical soundness: Not assessable from the abstract. The simulation framework is described only in general terms, and no validation or error analysis is presented.
  - Readability for nonspecialists: Acceptable but not strong. The abstract uses standard terms but does not explain why CC domains might be expected to drive LLPS, which would help a broader audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a plausible hypothesis and a promising framework, but the lack of quantitative results and methodological detail prevents a supportive recommendation. A revised manuscript with full data and validation could change this posture.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "the physical features of CC domains are sufficient to drive LLPS of proteins"
- **Evidence pointer** Abstract, location not provided
- **Concern** The claim of sufficiency is made without any quantitative evidence. The abstract does not report phase boundaries, critical concentrations, or any measure of LLPS propensity that would allow a reader to assess whether the observed behavior is robust or marginal. The term "sufficient" implies a strong and reproducible effect, but no data are shown to support this.
- **Why it matters** Sufficiency is a strong claim that requires demonstration that the effect is not dependent on specific simulation conditions, such as protein concentration, salt concentration, or system size. Without quantitative results, the claim cannot be distinguished from a weak or transient clustering artifact.
- **Resolution test** Provide phase diagrams or critical concentration values for the model proteins, with error bars, and show that LLPS occurs over a range of conditions. Demonstrate that the observed phase separation is stable and not a finite-size effect.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Model validation
- **Claim pointer** "We developed a coarse-grained simulation framework for investigating the LLPS propensity of CC proteins"
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract does not describe how the coarse-grained model represents CC domains, what interaction potentials are used, or how the model is parameterized. There is no mention of validation against known CC protein behavior or experimental data on CC-driven LLPS. Without this, it is unclear whether the model captures the essential physics of CC interactions or whether the results are an artifact of the chosen parameters.
- **Why it matters** Coarse-grained models can produce phase separation for many reasons, including overly attractive potentials or unrealistic multimerization constraints. If the model is not validated, the conclusions may not transfer to real CC proteins, undermining the biological relevance of the study.
- **Resolution test** Describe the model in detail, including interaction potentials and parameterization. Validate the model by reproducing known behavior of CC proteins, such as oligomerization states or binding affinities, and compare simulation predictions to experimental observations of CC-driven LLPS if available.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative comparison
- **Claim pointer** "trimer-forming and tetramer-forming CC domains have a dramatically higher LLPS propensity than dimer-forming coils, which shows that multimerization state has a greater effect on LLPS than the number of CC domains per protein"
- **Evidence pointer** Abstract, location not provided
- **Concern** The comparison between multimerization state and CC number is presented as a definitive conclusion, but no quantitative data are provided. The abstract does not state the magnitude of the differences, the range of CC numbers tested beyond two to four, or how the comparison was normalized. The claim that multimerization state has a "greater effect" requires a direct quantitative comparison, which is absent.
- **Why it matters** This is the central mechanistic conclusion of the study. If the comparison is not rigorous, the conclusion may be overstated or based on a narrow parameter range. A reader cannot judge whether the effect of multimerization is truly dominant or whether it is specific to the tested conditions.
- **Resolution test** Report quantitative measures of LLPS propensity for each CC number and multimerization state, with statistical significance. Show that the effect of multimerization state is larger than the effect of CC number across a range of conditions, and discuss any exceptions.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract, first sentence
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract states that LLPS is "thought to be a main driving force" in membraneless organelle formation, but this is presented without nuance. The field recognizes multiple mechanisms, and the role of LLPS is debated for some organelles.
- **Required correction** Soften the claim to reflect that LLPS is one proposed mechanism, or provide a brief context for why CC proteins are relevant to this debate.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "multimerization state"
- **Evidence pointer** Abstract, location not provided
- **Issue** The term "multimerization state" is used without definition. It is unclear whether this refers to the oligomeric state of individual CC domains or the higher-order assembly of multiple CC domains within a protein.
- **Required correction** Define the term explicitly, for example, as the number of helices in a CC bundle, and clarify how this is represented in the model.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scope
- **Affected element** Implications statement
- **Evidence pointer** Abstract, last sentence
- **Issue** The abstract claims implications for "identifying the LLPS-driving regions of centrosomal and central spindle proteins," but no specific predictions or examples are given. This statement is too vague to be actionable.
- **Required correction** Provide a specific example of how the framework could be applied, or state a testable prediction that follows from the results.

## Risk / unsupported claims
- The claim that CC domains are "sufficient" to drive LLPS is unsupported without quantitative phase behavior data.
- The claim that multimerization state has a "greater effect" than CC number is unsupported without a direct quantitative comparison.
- The claim that the framework can inform identification of LLPS-driving regions in centrosomal and spindle proteins is speculative and not supported by the abstract.
- The general relevance of the findings to real CC proteins is not assessable without model validation.