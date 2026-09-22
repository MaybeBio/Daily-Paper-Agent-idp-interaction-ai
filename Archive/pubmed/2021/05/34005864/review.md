## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as stated in the provided abstract; no full text, figures, tables, or supplementary materials were supplied
- **Shared manuscript claim summary** The authors report that polyampholyte field theory and explicit-chain molecular dynamics models of two IDP species undergoing sequence-specific phase separation consistently show that substantial polymer excluded volume and significant charge-pattern mismatch act in concert, but not in isolation, to demix the two species upon condensation. They further propose that this energetic-geometric interplay underlies a stochastic, "fuzzy" molecular recognition mechanism that may facilitate subcompartmentalization of membraneless organelles.
- **Visible evidence base** Abstract text only; no methodological details, quantitative results, figures, or statistical analyses are available
- **Missing materials affecting confidence** Full manuscript, model parameters, simulation protocols, field theory derivations, convergence criteria, error estimates, comparison with experimental data, and any supporting figures or tables

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting finding regarding the cooperative role of excluded volume and charge-pattern mismatch in driving demixing of two IDP species during phase separation. The claim of consistency between two distinct theoretical approaches is encouraging. However, the abstract provides insufficient detail to evaluate the robustness of the models, the parameter ranges explored, or the biological relevance of the proposed mechanism. The central claim that the two factors act "in concert, but not in isolation" is stated without quantitative support, and the extrapolation to organelle subcompartmentalization remains speculative. The work may be of interest to the biophysics and IDP communities, but the evidence base available here is too limited to establish the case.
- **Who would be interested in the results, and why** Researchers in biophysics, computational chemistry, and cell biology studying phase separation of intrinsically disordered proteins, particularly those interested in mechanisms of membraneless organelle organization and sequence-encoded determinants of condensate multiphase behavior. The proposed interplay between excluded volume and charge-pattern mismatch could inform future experimental designs and coarse-grained modeling efforts.
- **Major strengths** The use of two complementary theoretical approaches (field theory and explicit-chain simulations) to cross-validate findings is a methodological strength. The focus on a specific mechanistic hypothesis, namely the cooperative action of two physical factors, provides a clear and testable framework. The connection to organelle subcompartmentalization gives the work broader biological relevance.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative support for the central claim), R1-M2 (parameter space and robustness), R1-M3 (biological relevance and experimental grounding)
- **Assessment against Nature-style criteria**  
  - Originality: The idea that excluded volume and charge-pattern mismatch cooperate to drive demixing is not entirely novel, as both factors have been studied separately in IDP phase separation, but the specific combination and the claim of non-additivity may offer a fresh perspective.  
  - Scientific importance: If substantiated, the finding could advance understanding of multiphase condensate organization, which is a topic of growing interest. However, the abstract does not demonstrate broad implications beyond the specific model systems.  
  - Interdisciplinary readership: The topic bridges polymer physics, computational biology, and cell biology, which could attract a diverse audience, but the abstract is written in a specialized manner that may limit accessibility.  
  - Technical soundness: Cannot be assessed from the abstract alone. The consistency between two methods is promising but unverifiable without details on model construction, parameter choices, and error analysis.  
  - Readability for nonspecialists: The abstract is concise but uses jargon ("polyampholyte field theory," "charge-pattern mismatch," "excluded-volume interaction") without sufficient context for a general scientific audience. The phrase "stochastic, 'fuzzy' molecular recognition" is evocative but undefined.
- **Recommendation posture** Currently not established from the provided evidence. The abstract suggests a plausible and interesting mechanism, but the lack of quantitative detail and the speculative biological extrapolation prevent a supportive recommendation. A full manuscript with rigorous model validation and parameter sensitivity analysis would be required to assess the claims properly.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Quantitative support for central claim  
- **Claim pointer** The abstract states that "a substantial polymer excluded volume and a significant mismatch of the IDP sequence charge patterns can act in concert, but not in isolation, to demix the two IDP species upon condensation."  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The central claim of cooperative action is presented as a qualitative statement without any numerical results, phase diagrams, or quantitative measures of demixing (e.g., transfer free energies, coexistence compositions, or order parameters). No thresholds for "substantial" excluded volume or "significant" charge-pattern mismatch are given.  
- **Why it matters** The claim that the two factors act "in concert, but not in isolation" is the core finding. Without quantitative evidence, the reader cannot judge the magnitude of the effect, the parameter ranges over which it holds, or whether the effect is robust or marginal.  
- **Resolution test** Provide quantitative data, such as phase diagrams or demixing order parameters, as a function of excluded volume strength and charge-pattern mismatch, demonstrating that neither factor alone produces demixing while their combination does, with clear statistical significance and error estimates.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Parameter space and model robustness  
- **Claim pointer** The abstract claims that "polyampholyte field theory and explicit-chain molecular dynamics models ... indicate consistently" the cooperative demixing effect.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The abstract does not specify the sequence space explored, the range of charge-pattern mismatches tested, the excluded volume parameters used, or the system sizes and simulation lengths. It is unclear whether the consistency between the two methods holds across a broad parameter space or only in a narrow regime.  
- **Why it matters** For a computational study, the generalizability of the findings depends critically on the explored parameter space. If the effect appears only under specific conditions, the biological relevance and the claim of a general mechanism are weakened.  
- **Resolution test** Describe the parameter ranges, sequence libraries, and simulation protocols in the full manuscript. Show that the cooperative effect is robust across multiple sequence pairs and parameter values, and discuss any regimes where the effect breaks down.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** No  
- **Axis** Biological relevance and experimental grounding  
- **Claim pointer** The abstract states that the finding "may facilitate subcompartmentalization of membraneless organelles" and invokes a "stochastic, 'fuzzy' molecular recognition mechanism."  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The connection to organelle subcompartmentalization is speculative. No experimental data, known IDP sequences from organelles, or in vivo or in vitro observations are referenced to support the claim that the modeled mechanism operates in biological systems. The term "fuzzy molecular recognition" is not defined or linked to established concepts.  
- **Why it matters** The broader significance of the work depends on its relevance to biological phase separation. Without experimental context or validation, the claim remains a theoretical extrapolation that may not hold in real cellular environments where other factors (e.g., post-translational modifications, RNA, ATP) are present.  
- **Resolution test** In the full manuscript, discuss how the model parameters map to known IDP sequences and cellular conditions. If possible, compare predictions with existing experimental data on multiphase condensates or propose specific, testable experimental predictions.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity of terminology  
- **Affected element** "stochastic, 'fuzzy' molecular recognition mechanism"  
- **Evidence pointer** Abstract only; location not provided  
- **Issue** The phrase is evocative but undefined. It is unclear what "fuzzy" means in this context and how it relates to established concepts of fuzzy complexes or molecular recognition.  
- **Required correction** Define the term explicitly in the abstract or introduction, and connect it to prior literature on fuzzy interactions or disordered protein recognition.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Readability for nonspecialists  
- **Affected element** Abstract language  
- **Evidence pointer** Abstract only; location not provided  
- **Issue** Terms such as "polyampholyte field theory," "charge-pattern mismatch," and "excluded-volume interaction" are used without brief definitions, which may limit accessibility to readers outside the immediate field.  
- **Required correction** Add brief explanatory phrases in the abstract, such as "charge-pattern mismatch (the difference in the linear arrangement of charged residues)" or "excluded-volume interaction (the steric repulsion between polymer chains)," to improve accessibility.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Quantitative thresholds  
- **Affected element** "substantial" and "significant"  
- **Evidence pointer** Abstract only; location not provided  
- **Issue** The adjectives "substantial" and "significant" are used without quantitative definitions, making the claim difficult to interpret or reproduce.  
- **Required correction** Provide specific values or ranges in the abstract or full text, such as excluded volume strengths (e.g., B2 values) and charge-pattern mismatch metrics (e.g., sequence charge decoration parameters), to define these terms operationally.

## Risk / unsupported claims
- The claim that excluded volume and charge-pattern mismatch act "in concert, but not in isolation" is unsupported by quantitative evidence in the abstract.
- The claim of consistency between field theory and molecular dynamics models is unverifiable without methodological details.
- The extrapolation to organelle subcompartmentalization is speculative and not supported by experimental data or references.
- The term "stochastic, 'fuzzy' molecular recognition mechanism" is introduced without definition or linkage to established concepts.