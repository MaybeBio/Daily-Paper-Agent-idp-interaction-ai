## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no methods, figures, or supplementary materials were provided for evaluation
- **Shared manuscript claim summary** The authors use a coarse-grained polymer model (LASSI) to study how the spatial arrangement of LLPS-promoting and solubilizing RNA elements along the SARS-CoV-2 genome influences nucleocapsid (N-protein) mediated genome packaging, compaction, and cyclization. They report that the native 5ʹ/3ʹ enrichment of LLPS-promoting elements is optimal for cyclization, clustered binding sites enhance compaction, and distributed binding sites favor single-genome packaging. They argue this argues against the necessity of a singular packaging signal and suggest generalizability to other viruses and cellular organelles.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or numerical results were supplied
- **Missing materials affecting confidence** Full manuscript, methods description, model parameters, simulation details, validation against experimental data, and all quantitative results

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting hypothesis about how spatial patterning of RNA elements could influence viral genome packaging through LLPS. The modeling approach is potentially valuable, and the connection to SARS-CoV-2 is timely. However, the abstract alone provides insufficient detail to evaluate the technical soundness of the model, the robustness of the conclusions, or the strength of the evidence supporting the central claims. The claims are plausible but currently not established from the provided material.
- **Who would be interested in the results, and why** Virologists studying RNA virus genome packaging and assembly, biophysicists interested in phase separation and polymer models of nucleic acid condensation, and researchers working on SARS-CoV-2 biology. The proposed generalizability to other viruses and paraspeckles could also interest cell biologists studying ribonucleoprotein granules.
- **Major strengths** The question is well framed and addresses a fundamental challenge in virology. The use of a coarse-grained polymer model to explore spatial patterning is a creative approach that could generate testable predictions. The authors explicitly connect their findings to the native genome organization of SARS-CoV-2, which grounds the modeling in a real biological system. The suggestion that multiple distributed signals can substitute for a single packaging signal is an interesting conceptual contribution.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide any quantitative results, model validation, or methodological detail. Without these, the central claims cannot be assessed for technical soundness. Specifically, the relationship between model predictions and experimental observations is not demonstrated, and the generalizability claim is unsupported.
- **Assessment against Nature-style criteria** 
  - Originality: The idea of applying LLPS-based polymer modeling to viral genome packaging is not entirely new, but the specific focus on spatial patterning of opposing RNA elements is a fresh angle. The claim that distributed signals may obviate the need for a singular packaging signal is potentially original.
  - Scientific importance: If validated, the findings could influence how researchers think about viral genome packaging and could inform experimental design. The relevance to SARS-CoV-2 adds urgency.
  - Interdisciplinary readership: The topic bridges virology, biophysics, and polymer physics, which could attract a broad audience. However, the abstract assumes familiarity with LLPS and polymer modeling concepts that may limit accessibility.
  - Technical soundness: Cannot be evaluated from the abstract alone. No methods, parameters, or validation are provided.
  - Readability for nonspecialists: The abstract is reasonably clear but uses jargon (e.g., LASSI, LLPS-promoting features) without sufficient explanation for a general scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents an interesting hypothesis, but the lack of methodological detail and quantitative results prevents assessment of whether the claims are supported. A full manuscript with methods, validation, and results would be required to evaluate the case.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the native spatial patterning of LLPS-promoting elements at the 5ʹ and 3ʹ ends is optimal for genome cyclization, that clustered binding sites enhance compaction, and that distributed binding sites favor single-genome packaging.
- **Evidence pointer** Abstract only; no figures, tables, or methods provided
- **Concern** The abstract reports qualitative outcomes from a computational model but provides no quantitative data, simulation parameters, or statistical measures. There is no indication of how the model was parameterized, how many simulations were run, what controls were used, or how the results were scored. Without this information, the reliability of the reported optimality and efficiency claims cannot be assessed.
- **Why it matters** The central conclusions depend entirely on the model's behavior. If the model is not properly validated or if the parameter space is not adequately explored, the conclusions could be artifacts of the chosen parameters rather than robust biological insights.
- **Resolution test** Provide a detailed methods section describing the LASSI model, parameter choices, simulation protocols, and analysis criteria. Include quantitative results with error bars or confidence intervals, and demonstrate that the conclusions are robust to parameter variation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors state that their results "argue against necessity" of a singular packaging signal and suggest the model should be generalizable to multiple viruses and cellular organelles like paraspeckles.
- **Evidence pointer** Abstract only; no experimental validation or comparative analysis provided
- **Concern** The claim that a singular packaging signal is not necessary is a strong negative claim that would require demonstrating that the model's distributed-signal mechanism can achieve packaging efficiency comparable to or better than known packaging signal mechanisms. No experimental data or comparison with existing packaging models is provided. The generalizability claim is speculative and not supported by any evidence in the abstract.
- **Why it matters** These claims extend beyond the immediate model results and have implications for how the field views viral packaging mechanisms. Overreaching claims without supporting evidence could mislead readers and undermine the credibility of the work.
- **Resolution test** Provide experimental validation or at least a detailed comparison with existing packaging models. For the generalizability claim, include a discussion of how the model parameters map to other systems and what predictions could be tested experimentally.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The authors use the LASSI coarse-grained polymer model to study LLPS of N-protein with RNA sequences.
- **Evidence pointer** Abstract only; no model description or code availability statement
- **Concern** The abstract does not describe the LASSI model, its assumptions, or its limitations. There is no mention of code availability, input parameters, or how the RNA sequences were represented. This makes it impossible for another researcher to reproduce the simulations or assess whether the model is appropriate for the biological question.
- **Why it matters** Reproducibility is a core requirement for computational studies. Without model details and code access, the work cannot be independently verified, and the conclusions cannot be built upon by other groups.
- **Resolution test** Include a full model description in the methods, provide access to the code and input files, and state the version of LASSI used. Ideally, provide a reproducibility package or link to a repository.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract, first paragraph
- **Issue** The term "LLPS-promoting features" is used without definition. It is unclear whether these are sequence motifs, structural elements, or physicochemical properties.
- **Required correction** Define what constitutes an LLPS-promoting feature in the context of this model, and clarify how these features were identified or assigned in the RNA sequence.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Readability
- **Affected element** Background context
- **Evidence pointer** Abstract, first paragraph
- **Issue** The abstract references "our previous study" without providing sufficient context for readers unfamiliar with that work. The connection between the previous findings and the current model is not fully explained.
- **Required correction** Briefly summarize the key findings of the previous study that motivate the current work, or provide a citation that readers can consult.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scope
- **Affected element** Generalizability claim
- **Evidence pointer** Abstract, final sentence
- **Issue** The claim that the model "should be generalizable to multiple viruses as well as cellular organelles" is presented without any discussion of the assumptions that would need to hold for this generalization to be valid.
- **Required correction** Add a sentence acknowledging the conditions under which the model would apply to other systems, or temper the claim to reflect its speculative nature.

## Risk / unsupported claims
- The claim that the native spatial patterning is optimal for genome cyclization is unsupported because no quantitative comparison with alternative arrangements is provided in the abstract.
- The claim that distributed binding sites favor single-genome packaging is unsupported without quantitative efficiency measures.
- The claim that the results argue against the necessity of a singular packaging signal is unsupported without experimental validation or comparison with known packaging signal mechanisms.
- The generalizability claim to other viruses and paraspeckles is speculative and not supported by any evidence in the abstract.
- The overall model predictions are not validated against any experimental data, making the biological relevance of the findings unassessable from the provided material.