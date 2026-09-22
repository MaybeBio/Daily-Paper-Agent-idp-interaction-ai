## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no figures, methods, or supplementary data were provided for evaluation
- **Shared manuscript claim summary** The authors propose that ZAKα acts as a sensor of mRNA stasis at the ribosomal exit channel. They report that ZAKα dynamically monitors the mRNA exit channel of elongating ribosomes through direct interactions with RACK1, RPS27, and 18S rRNA helix-26. Four mRNA-binding peptides in ZAKα span the path of ribosome-exiting mRNA. Progressive elongation threads ZAKα off the ribosome, while mRNA stasis stabilizes the interaction and enables kinase activation. Prolonged binding to slow-elongating, stalled, and collided ribosomes sequesters the inhibitory SAM domain on RACK1, allowing ZAKα dimerization, activation loop trans-autophosphorylation, and RSR activation. The authors conclude that compromised ribosome processivity is a common ribotoxic stress signal and that ZAKα is a ribosome collision-agnostic sensor.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary materials were supplied
- **Missing materials affecting confidence** Full manuscript, all figures and tables, experimental methods, statistical analyses, and any supplementary data. The absence of these materials prevents independent verification of the structural predictions, CLIP data, biochemical interaction assays, and functional experiments referenced in the abstract.

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting and potentially significant model for how ZAKα senses translational stress. The proposed mechanism, involving direct ribosome binding and mRNA stasis detection, is novel and would be of broad interest to the ribotoxic stress and translation fields. However, the abstract alone provides insufficient evidence to evaluate the technical soundness of the claims. The key conclusions rest on a combination of computational prediction and experimental data that cannot be assessed without the full manuscript. The claim that ZAKα is a "ribosome collision-agnostic sensor" is particularly provocative and would require careful experimental discrimination between stasis and collision scenarios.
- **Who would be interested in the results, and why** Researchers studying the ribotoxic stress response, MAP kinase signaling, translational control, and ribosome quality control. The work also has potential relevance for understanding inflammatory diseases and cancer, where RSR and ZAKα have been implicated. The proposed mechanism of direct ribosome sensing by a kinase would interest structural biologists and cell biologists studying protein-RNA and protein-ribosome interactions.
- **Major strengths** The proposed mechanism is conceptually novel and provides a plausible molecular explanation for how ZAKα distinguishes normal translation from pathological stasis. The combination of Alphafold3 prediction with CLIP and biochemical validation suggests a multi-pronged approach. The model elegantly links mRNA stasis to kinase activation through a defined sequence of molecular events, which is mechanistically satisfying and generates testable predictions.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
  - R1-M4
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide sufficient methodological detail to assess the rigor of the CLIP experiments, the validation of Alphafold3 predictions, the specificity of the proposed interactions, or the functional assays used to demonstrate kinase activation. Without these details, the core claims cannot be evaluated.
- **Assessment against Nature-style criteria** Originality is high, as the proposed mechanism is distinct from existing models of ribotoxic stress sensing. Scientific importance is potentially high, given the broad relevance of RSR to human disease. Interdisciplinary readership is plausible, spanning cell biology, structural biology, and signal transduction. Technical soundness cannot be assessed from the abstract alone. Readability for nonspecialists is adequate, though the abstract assumes familiarity with ribosome structure and MAP kinase signaling.
- **Recommendation posture** Currently not established from the provided evidence. The conceptual framework is compelling, but the abstract alone does not permit evaluation of the experimental support. A full review would be required to determine whether the technical concerns can be resolved.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that ZAKα dynamically monitors the mRNA exit channel of elongating ribosomes through direct interactions with RACK1, RPS27, and 18S rRNA helix-26.
- **Evidence pointer** Abstract text; location not provided
- **Concern** The abstract states that Alphafold3 prediction and CLIP were used to uncover these interactions, but no details are provided regarding the CLIP methodology, the validation of the Alphafold3 predictions, or the specificity controls for the proposed RNA and protein interactions. It is unclear whether the CLIP data demonstrate direct binding or indirect association, and whether the proposed contacts with 18S rRNA helix-26 were independently verified.
- **Why it matters** The central claim of the paper rests on the specificity and directness of these interactions. If the CLIP data do not distinguish direct from indirect binding, or if the Alphafold3 predictions were not experimentally validated, the proposed mechanism would lack a solid foundation.
- **Resolution test** Provide CLIP data with appropriate controls, including input and IgG controls, and demonstrate that the interactions are direct through recombinant protein binding assays or crosslinking experiments. Validate Alphafold3 predictions with mutagenesis or structural data.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that four mRNA-binding peptides in ZAKα span across the path of ribosome-exiting mRNA, and that progressive elongation threads ZAKα off the ribosome while mRNA stasis stabilizes the interaction.
- **Evidence pointer** Abstract text; location not provided
- **Concern** The abstract does not describe how the four mRNA-binding peptides were identified, whether they were functionally validated, or how the threading and stabilization dynamics were experimentally measured. The distinction between elongation-dependent release and stasis-dependent stabilization is central to the model, but no experimental approach is described.
- **Why it matters** The proposed dynamic behavior of ZAKα on the ribosome is the core of the sensing mechanism. Without experimental evidence for the differential behavior under elongating versus stalling conditions, the model remains speculative.
- **Resolution test** Provide mutagenesis data for the four peptides showing loss of ribosome binding or sensing function. Include single-molecule or biochemical assays demonstrating differential binding under elongating versus stalled conditions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that prolonged binding of ZAKα to slow-elongating, stalled, and collided ribosomes sequesters the inhibitory SAM domain on RACK1, allowing for ZAKα dimerization, activation loop trans-autophosphorylation, and RSR activation.
- **Evidence pointer** Abstract text; location not provided
- **Concern** The abstract does not describe how SAM domain sequestration was demonstrated, how dimerization was detected, or how trans-autophosphorylation was measured. The causal sequence from ribosome binding to kinase activation is asserted but not supported by described experiments.
- **Why it matters** The link between ribosome stasis sensing and kinase activation is the functional output of the proposed mechanism. Without evidence for each step in the activation cascade, the model is incomplete.
- **Resolution test** Provide biochemical or structural data showing SAM domain displacement, dimerization assays (e.g., crosslinking or FRET), and phosphorylation assays with appropriate controls.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The authors propose that compromised ribosome processivity constitutes a common ribotoxic stress signal and that ZAKα is a ribosome collision-agnostic sensor.
- **Evidence pointer** Abstract text; location not provided
- **Concern** The claim that ZAKα is collision-agnostic is a strong conclusion that requires discrimination between stasis and collision scenarios. The abstract does not describe experiments that would distinguish these conditions, such as using ribosome mutants that stall without colliding or inducing collisions without stasis.
- **Why it matters** If ZAKα responds to both stasis and collisions, the proposed mechanism would unify disparate observations in the field. However, if the claim is not experimentally supported, it overstates the findings.
- **Resolution test** Provide experiments that separate stasis from collision, such as using drugs or mutations that induce one without the other, and show ZAKα activation in both cases.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract terminology
- **Evidence pointer** Abstract text; location not provided
- **Issue** The term "mRNA stasis" is used without a precise definition. It is unclear whether this refers to a complete halt, a slowdown, or a specific conformational state of the ribosome.
- **Required correction** Define "mRNA stasis" operationally in the abstract or refer to a defined experimental condition.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Abstract claims
- **Evidence pointer** Abstract text; location not provided
- **Issue** The abstract mentions "transient ZAKα dimerization" but does not specify the timescale or the conditions under which this transience was observed.
- **Required correction** Provide quantitative information on dimerization dynamics or refer to the relevant figure.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract structure
- **Evidence pointer** Abstract text; location not provided
- **Issue** The abstract moves rapidly from structural prediction to functional outcomes without a clear logical flow for nonspecialist readers.
- **Required correction** Consider restructuring the abstract to briefly introduce the RSR context, then the proposed mechanism, and finally the functional implications.

## Risk / unsupported claims
- The claim that ZAKα directly interacts with 18S rRNA helix-26 is unsupported without structural or crosslinking data.
- The claim that mRNA stasis stabilizes ZAKα binding while elongation threads it off is unsupported without kinetic or single-molecule data.
- The claim that SAM domain sequestration on RACK1 is the mechanism of kinase activation is unsupported without direct biochemical evidence.
- The claim that ZAKα is a "ribosome collision-agnostic sensor" is unsupported without experiments distinguishing stasis from collision.
- The overall model of ZAKα as a sensor of compromised ribosome processivity is plausible but not established from the abstract alone.