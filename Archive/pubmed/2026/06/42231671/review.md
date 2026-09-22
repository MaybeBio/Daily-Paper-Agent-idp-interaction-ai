## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as stated in the abstract, without access to full-text methods, figures, or supporting data
- **Shared manuscript claim summary** The authors report a phase-transformable DNA framework that converts tetrahedral DNA nanostructures into condensates in situ, with condensation order governed by binding valency. They claim distinct intracellular fates for condensates of different valency, with high-order condensates avoiding endolysosomal trapping and low-order condensates localizing to lysosomes. They further claim that spatially controlled DNA condensates can act as artificial membraneless organelles, enabling targeted membrane protein degradation and prolonged cytosolic retention of therapeutic payloads.
- **Visible evidence base** Abstract text only. No figures, tables, methods, or supplementary information were provided.
- **Missing materials affecting confidence** Full methods, simulation details, experimental protocols, characterization data, statistical analyses, control experiments, and all figures and tables. The absence of these materials precludes verification of the central claims.

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting approach to engineering DNA-based condensates with valency-controlled intracellular behavior. The idea of using phase-transformable DNA frameworks to achieve subcellular sorting is novel and potentially impactful for synthetic biology and therapeutic delivery. However, the abstract alone provides insufficient evidence to assess the validity of the claims. Key mechanistic details, quantitative data, and experimental controls are not visible. The claim of distinct intracellular fates and the functional outcomes (membrane protein degradation, prolonged cytosolic residence) require substantial experimental support that is not available in the supplied material.
- **Who would be interested in the results, and why** Researchers in synthetic biology, DNA nanotechnology, and intracellular phase separation would find this work relevant. Those working on artificial organelles, drug delivery systems, and programmable biomolecular condensates would also be interested, as the approach offers a potential strategy for controlling condensate localization and function in living cells.
- **Major strengths** The conceptual advance of using valency-controlled phase transformation to direct subcellular sorting is elegant and potentially generalizable. The combination of coarse-grained simulations with experimental validation suggests a mechanistic approach. The demonstrated applications, including targeted protein degradation and payload retention, indicate practical relevance beyond fundamental phase separation biology.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria**  
  Originality: The concept of phase-transformable DNA frameworks with valency-controlled subcellular sorting appears original, though the abstract does not fully contextualize prior work on DNA condensates or synthetic MLOs.  
  Scientific importance: If substantiated, the findings could advance the design of programmable condensates for intracellular applications, which is a growing and important area.  
  Interdisciplinary readership: The topic bridges DNA nanotechnology, cell biology, and therapeutic delivery, which could attract broad interest.  
  Technical soundness: Cannot be assessed from the abstract alone. The claims require rigorous experimental and computational validation that is not visible.  
  Readability for nonspecialists: The abstract is reasonably clear but uses specialized terminology that may limit accessibility for a general scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents promising ideas, but the absence of supporting data and methods prevents any assessment of validity. A full manuscript with complete evidence would be required to evaluate the claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "the condensation order is governed by binding valencies of transformed building blocks" and that this is demonstrated with coarse-grained simulations and experiments.
- **Evidence pointer** Abstract only. No simulation or experimental data provided.
- **Concern** The abstract states that coarse-grained simulations and experiments demonstrate valency-controlled condensation order, but no quantitative results, model parameters, or experimental conditions are provided. It is unclear how valency was varied, how condensation order was measured, or whether the simulations and experiments are consistent with each other.
- **Why it matters** This is the foundational mechanistic claim of the work. Without visible evidence, the reader cannot assess whether the proposed design principle is valid or whether alternative explanations are possible.
- **Resolution test** Provide simulation snapshots or order parameters, experimental characterization of condensate formation (e.g., microscopy, turbidity, or fluorescence), and a clear definition of condensation order with statistical comparisons across valency conditions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim "distinct intracellular fates of synDNA condensates, with high-order condensates escaping the endolysosomal pathway and low-order condensates trapped in the lysosome."
- **Evidence pointer** Abstract only. No imaging or trafficking data provided.
- **Concern** The claim of differential intracellular trafficking is striking and central to the paper. However, no data are shown to support the distinction between high-order and low-order condensates in terms of endolysosomal escape or lysosomal trapping. It is unclear how these fates were quantified, what cell types were used, and whether the observations are reproducible across biological replicates.
- **Why it matters** This claim underpins the functional significance of valency control. If the trafficking distinction is not robustly demonstrated, the proposed design principle loses its practical relevance.
- **Resolution test** Provide representative fluorescence microscopy images, colocalization analyses with endolysosomal markers, time-course data, and quantitative statistics comparing the intracellular distribution of high-order versus low-order condensates.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that spatially controlled DNA condensates "facilitate the targeted degradation of membrane proteins and prolong the cytosolic residence of the therapeutic payloads."
- **Evidence pointer** Abstract only. No functional assay data provided.
- **Concern** The functional outcomes are significant and would require robust assays, including demonstration of targeted protein degradation (e.g., western blot or degradation assays) and evidence of prolonged cytosolic residence (e.g., pharmacokinetic or fluorescence tracking). None of this is visible in the abstract.
- **Why it matters** These claims suggest translational potential. Without evidence, the reader cannot determine whether the observed effects are specific, significant, or due to the condensate design rather than nonspecific effects.
- **Resolution test** Provide degradation assay data with appropriate controls, quantification of cytosolic retention over time, and statistical analysis comparing condensate-treated versus control conditions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility and rigor
- **Claim pointer** The abstract implies a generalizable design principle for "constructing programmable DNA condensates in cellulo."
- **Evidence pointer** Abstract only. No demonstration of generality or robustness.
- **Concern** The abstract does not indicate how many different DNA framework designs were tested, whether the observed behavior is consistent across multiple constructs, or whether the results are reproducible across experimental replicates. The generality of the design principle is asserted but not evidenced.
- **Why it matters** A design principle should be validated across multiple examples to be considered generalizable. Without this, the claim may be overreaching.
- **Resolution test** Provide data from multiple DNA framework variants with different valencies, show reproducibility across independent experiments, and discuss any limitations or exceptions to the proposed principle.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract, first sentence
- **Issue** The term "phase-transforming DNA framework" is introduced without definition or context. It is unclear what distinguishes this from other DNA nanostructure-based condensate systems.
- **Required correction** Define the term explicitly and clarify the novelty relative to existing DNA condensate approaches.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Experimental context
- **Evidence pointer** Abstract, methods reference
- **Issue** The abstract mentions "coarse-grained simulations and experiments" but does not specify the cell types, experimental conditions, or the nature of the therapeutic payloads used.
- **Required correction** Include brief details on cell models and payload types, or indicate that these are described in the full manuscript.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Mechanistic explanation
- **Evidence pointer** Abstract, claim of "valency-controlled subcellular sorting"
- **Issue** The abstract does not explain the mechanism by which valency controls subcellular sorting. It is unclear whether the effect is due to condensate size, stability, surface properties, or interactions with cellular machinery.
- **Required correction** Provide a brief mechanistic hypothesis or refer to specific data in the full manuscript that addresses the underlying mechanism.

## Risk / unsupported claims
- The claim that condensation order is governed by binding valency is unsupported without simulation and experimental data.
- The claim of distinct intracellular fates (endolysosomal escape versus lysosomal trapping) is unsupported without imaging and trafficking data.
- The claim of targeted membrane protein degradation and prolonged cytosolic residence is unsupported without functional assay data.
- The claim of a generalizable design principle is unsupported without evidence of validation across multiple constructs and replicates.
- The overall feasibility and robustness of the approach cannot be assessed from the abstract alone.