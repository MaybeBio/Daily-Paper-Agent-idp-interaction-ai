## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as stated in the abstract; no methods, figures, or supplementary data were provided for evaluation
- **Shared manuscript claim summary** The authors present a machine learning framework that inverts physics-based models to design intrinsically disordered proteins (IDPs) at proteome scale. They claim the framework enables (1) programmable sensing and response to biophysical cues, including threshold detection, bandpass filtering, and Boolean logic; (2) engineering of multicomponent IDP mixtures with tailored condensate properties, including layering, phase number, compositional specificity, and RNA-dependent remodeling; and (3) selective partitioning or depletion of designed IDPs in living cell condensates.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary materials were supplied
- **Missing materials affecting confidence** Full manuscript, methods description, model architecture and training details, validation datasets, experimental protocols, quantitative results, statistical analyses, and all figures and tables

## Reviewer
- **Overall assessment** The abstract describes an ambitious and potentially impactful framework for IDP design. The conceptual advance of inverting physics-based models via machine learning is timely and aligns with current trends in biomolecular design. However, the abstract provides no quantitative evidence, no methodological detail, and no validation metrics. The claims are broad and sweeping, and the current evidence base is insufficient to assess technical soundness or reproducibility. The work may be of high interest if the full manuscript substantiates the claims, but from the supplied material alone, the case is not established.
- **Who would be interested in the results, and why** Researchers in protein design, biomolecular condensates, synthetic biology, and biophysics would be interested. The framework addresses a known gap in IDP design, where sequence-to-ensemble relationships are poorly captured by traditional structure-based design. The demonstrated capabilities in logic operations and condensate engineering could appeal to those building synthetic cellular systems or studying phase separation.
- **Major strengths** The conceptual framing is clear and compelling. The idea of inverting physics-based models for design is a logical and potentially powerful extension of existing predictive tools. The breadth of claimed capabilities, from single-chain ensemble properties to multicomponent collective behaviors and live-cell validation, suggests a comprehensive framework. The abstract is well written and accessible to a broad audience.
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
  - Originality: The approach of inverting physics-based models via machine learning for IDP design appears conceptually novel, though prior work on sequence design for phase-separating proteins exists. The specific combination of capabilities claimed is distinctive.
  - Scientific importance: If substantiated, the framework could significantly advance IDP design and enable new synthetic biology applications. The potential to program logic operations and condensate properties is of broad interest.
  - Interdisciplinary readership: The topic bridges protein biophysics, machine learning, and cell biology, which would appeal to a wide readership. The abstract is written in an accessible style.
  - Technical soundness: Cannot be assessed from the abstract alone. No methodological details, validation metrics, or statistical analyses are provided.
  - Readability for nonspecialists: The abstract is clear and avoids excessive jargon, making it accessible to a broad scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The claims are plausible and potentially significant, but the abstract alone does not provide sufficient information to evaluate technical soundness or reproducibility. A full review of the manuscript would be required to determine whether the case is made.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The framework enables proteome-scale de novo IDP design by rationally inverting physics-based models.
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract claims proteome-scale design capability but provides no information on the scale of validation, the number of designed sequences tested, or the success rate. No quantitative metrics are given for design accuracy, ensemble property matching, or functional performance.
- **Why it matters** Proteome-scale design implies broad applicability and high throughput. Without quantitative evidence of success rates, scalability, and generalizability across sequence space, the claim cannot be evaluated. The absence of any numerical data makes it impossible to assess whether the framework performs better than existing methods or achieves practical utility.
- **Resolution test** Provide quantitative results including number of designed sequences, validation success rates, comparison to baseline methods, and metrics for ensemble property matching across diverse IDP families.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** IDP ensembles can directly encode complex signal processing, including threshold detection, bandpass filtering, and Boolean-type multi-input logic.
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract states that IDP ensembles can encode logic operations but provides no description of how these operations are implemented, measured, or validated. No information is given on the input-output relationships, the dynamic range, the response times, or the robustness of these operations.
- **Why it matters** Signal processing and logic operations are quantitative concepts that require precise characterization. Without details on the experimental or computational assays used to demonstrate these functions, the claims are unverifiable. The biological relevance and practical utility of such operations in IDPs depend on their quantitative performance characteristics.
- **Resolution test** Provide detailed descriptions of the assays, representative input-output curves, quantitative thresholds, and statistical analyses demonstrating reliable logic operations across multiple designed sequences.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** Multicomponent IDP mixtures can be engineered with tailored emergent condensate properties, including layering, number of phases, compositional specificity, and RNA-dependent remodeling.
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract claims control over complex multicomponent phase behavior but provides no experimental data, no description of the system components, and no characterization of the phase diagrams. The terms "layering" and "number of phases" imply specific phase behavior that requires detailed experimental validation.
- **Why it matters** Multicomponent condensate behavior is notoriously difficult to predict and control. Claims of tailored properties require demonstration of precise control over phase boundaries, component partitioning, and dynamic responses. Without quantitative phase diagrams and compositional analyses, the claims are not supported.
- **Resolution test** Provide experimental phase diagrams, fluorescence microscopy or other imaging data showing distinct phases and layering, quantitative compositional analyses, and evidence of RNA-dependent changes with appropriate controls.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** Designed IDPs selectively partition into or deplete from biological condensates in living cells.
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract claims live-cell validation but provides no details on the cell types, the condensate systems studied, the imaging or quantification methods, or the statistical significance of the observed partitioning behavior. No information is given on how selectivity was measured or controlled.
- **Why it matters** Live-cell behavior is subject to many confounding factors, including expression levels, protein stability, and off-target interactions. Claims of selective partitioning require rigorous controls and quantitative single-cell analyses. Without these, the biological relevance of the design framework cannot be established.
- **Resolution test** Provide detailed live-cell imaging data, quantification of partitioning coefficients, appropriate controls (e.g., scrambled sequences, localization markers), and statistical analyses demonstrating selective behavior across multiple cell lines or condensate types.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "rationally inverting physics-based models" is used without explanation of what inversion means in this context. It is unclear whether the machine learning framework learns the inverse mapping directly or iteratively optimizes sequences against forward models.
- **Required correction** Clarify the relationship between the machine learning framework and the physics-based models, including whether the models are used as differentiable surrogates, as training data generators, or as evaluation functions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Benchmarking
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract does not mention any comparison to existing IDP design methods or random sequence controls. Without benchmarking, it is unclear whether the framework offers advantages over simpler approaches.
- **Required correction** Include a statement in the abstract or manuscript about comparison to baseline methods, random sequence libraries, or existing design tools.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scope
- **Affected element** Generalizability
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract claims proteome-scale design but does not discuss the diversity of IDP sequences or functions covered. It is unclear whether the framework applies to all IDP families or only to specific sequence classes.
- **Required correction** Specify the sequence space covered, including any limitations on sequence length, composition, or post-translational modifications, and discuss generalizability across IDP families.

## Risk / unsupported claims
- The claim of "proteome-scale" design is unsupported without quantitative scale and success rate data.
- The claim that IDP ensembles "directly encode" complex signal processing is unsupported without mechanistic or quantitative evidence.
- The claim of tailored multicomponent condensate properties is unsupported without phase diagram data.
- The claim of selective partitioning in living cells is unsupported without imaging and quantification details.
- The overall framework's performance relative to existing methods is unassessable from the abstract.
- All quantitative aspects of the work, including accuracy, reproducibility, and statistical significance, are unassessable from the supplied material.