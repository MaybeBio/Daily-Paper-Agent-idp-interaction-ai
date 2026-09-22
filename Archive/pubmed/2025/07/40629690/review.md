## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no methods, figures, tables, or supplementary material were available for evaluation
- **Shared manuscript claim summary** The authors present a top-down, data-driven coarse-grained model compatible with the CALVADOS framework to simulate the effects of serine and threonine phosphorylation on the global conformational properties of intrinsically disordered proteins. The model is parameterized using experimental data on phosphorylation-induced changes in global dimensions. Comparisons with baseline models and simulations using phosphomimetics (aspartate and glutamate) indicate that the effect of phosphorylation on global dimensions is primarily driven by the added negative charge. The authors propose the model is suitable for proteome-scale studies and for investigating phosphorylation effects on phase separation.
- **Visible evidence base** Abstract text only; no quantitative results, parameterization details, validation metrics, or methodological descriptions are provided
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, parameterization data, simulation protocols, validation datasets, and any comparison statistics

## Reviewer
- **Overall assessment** The abstract describes a potentially useful extension of the CALVADOS coarse-grained framework to include phosphorylated serine and threonine residues. The scientific premise is sound and the application domain is relevant. However, the abstract alone provides insufficient detail to evaluate the technical rigor of the parameterization, the quality of the experimental data used, the robustness of the conclusions, or the claimed generalizability. The central claim that charge is the dominant driver of phosphorylation effects on dimensions is plausible but not substantiated from the supplied material.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, post-translational modifications, and biomolecular phase separation would be interested. The model could be of practical value to computational biologists seeking efficient tools for proteome-scale simulations of phosphorylation effects. Experimentalists studying phosphorylation-dependent conformational changes might also find the model useful for generating testable hypotheses.
- **Major strengths** The work addresses an important and under-modeled aspect of disordered protein simulation. The choice to build on the established CALVADOS framework is sensible and likely to facilitate adoption. The explicit comparison with phosphomimetics is a valuable design element that could clarify the biophysical basis of phosphorylation effects. The stated ambition toward proteome-scale and phase-separation applications indicates broad potential impact.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide any quantitative evidence that the model reproduces experimental data beyond a general statement of parameterization. No error metrics, validation statistics, or comparison benchmarks are reported. The claim that charge is the dominant driver is presented without supporting data. The compatibility with CALVADOS is asserted but not demonstrated. The suitability for proteome-scale and phase-separation studies is speculative without evidence of computational efficiency or transferability.
- **Assessment against Nature-style criteria**  
  - Originality: The approach is incremental, extending an existing model to a new modification type. The conceptual framing is not novel, though the specific parameterization may be.  
  - Scientific importance: The topic is important, and a reliable model would be valuable. However, the abstract does not demonstrate that the model achieves the required accuracy or breadth.  
  - Interdisciplinary readership: The work sits at the interface of computational biophysics, biochemistry, and cell biology. The abstract is written in a way that is broadly accessible, but the lack of quantitative detail limits its appeal to specialists.  
  - Technical soundness: Cannot be assessed from the abstract. The parameterization strategy is described only in general terms.  
  - Readability for nonspecialists: The abstract is clear and well-structured, with minimal jargon. The main concepts are explained adequately for a general scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract describes a plausible and potentially useful model, but the absence of quantitative results and methodological detail prevents any assessment of whether the claims are supported. A full manuscript with detailed methods, validation, and comparison data would be required to evaluate the work properly.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The model is parameterized using experimental data on the effects of phosphorylation on global dimensions.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The abstract states that the model was parameterized using experimental data but provides no information on the nature, quantity, quality, or diversity of these data. It is unclear how many proteins were used, what experimental techniques were employed, how the data were processed, and whether the dataset is sufficiently representative of the sequence space of disordered proteins.  
- **Why it matters** The reliability of a data-driven model depends entirely on the quality and coverage of the training data. Without this information, the parameterization cannot be evaluated, and the model's generalizability is uncertain.  
- **Resolution test** The full manuscript must describe the experimental dataset in detail, including the number of proteins, the range of sequence properties, the experimental methods used to measure dimensions, and the uncertainty in the measurements. The authors should also report the fitting procedure and any cross-validation or holdout testing.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** By comparing with baseline models and simulations using the phosphomimetics aspartate and glutamate, we show that the effect of phosphorylation on the global dimensions of disordered proteins is mostly driven by the additional charge.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The central conclusion that charge is the dominant driver is stated without any quantitative support. No values for radii of gyration, scaling exponents, or other conformational metrics are reported. The comparison with phosphomimetics is mentioned but no results are shown. It is also unclear whether the comparison accounts for differences in side-chain size, hydrogen bonding, or other non-electrostatic effects that distinguish phosphate from carboxylate groups.  
- **Why it matters** This is the main scientific claim of the work. If the evidence is not presented clearly, the conclusion cannot be verified or reproduced. The distinction between charge effects and other physicochemical effects is critical for the model's interpretation and for its use in understanding phosphorylation biology.  
- **Resolution test** The manuscript must present quantitative comparisons of simulated dimensions for phosphorylated, unphosphorylated, and phosphomimetic variants across multiple proteins. Statistical measures of agreement with experimental data should be reported. The authors should also discuss or test whether the phosphomimetic comparison fully isolates the charge contribution.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Generalizability and scope  
- **Claim pointer** We envisage that our model can be applied to study the effects of phosphorylation of disordered proteins at the proteome scale as well as to study the important roles of protein phosphorylation on phase separation.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The abstract claims applicability to proteome-scale studies and phase separation without providing any evidence of computational efficiency, transferability to diverse sequence contexts, or validation in phase-separation systems. These are substantial extensions that require dedicated testing.  
- **Why it matters** These claims go beyond the stated scope of the model development and could mislead potential users if the model is not actually suitable for these applications. Overstating applicability without evidence undermines confidence in the work.  
- **Resolution test** The manuscript should either provide preliminary demonstrations of proteome-scale feasibility (e.g., computational cost estimates or benchmarks) and phase-separation applications, or temper these claims to clearly indicate them as future directions rather than established capabilities.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity and completeness  
- **Affected element** Model description  
- **Evidence pointer** Abstract only; location not provided  
- **Issue** The abstract does not specify which residues are parameterized beyond serine and threonine, nor does it state whether tyrosine phosphorylation is excluded.  
- **Required correction** Clarify the scope of the model with respect to phosphorylatable residues and state any limitations.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Parameterization details  
- **Evidence pointer** Abstract only; location not provided  
- **Issue** No information is given on the functional form of the added parameters, the fitting algorithm, or the treatment of the phosphate group in the coarse-grained representation.  
- **Required correction** The methods section should provide a complete description of the model parameters, their functional forms, and the fitting procedure to ensure reproducibility.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Presentation  
- **Affected element** Comparison with existing models  
- **Evidence pointer** Abstract only; location not provided  
- **Issue** The abstract does not mention how the new model compares with existing approaches for simulating phosphorylated disordered proteins, if any exist.  
- **Required correction** A brief statement in the introduction or discussion situating the model relative to prior work would help readers assess its novelty and utility.

## Risk / unsupported claims
- The claim that the effect of phosphorylation on global dimensions is mostly driven by additional charge is unsupported in the abstract, as no quantitative results are presented.
- The claim that the model is suitable for proteome-scale studies is unsupported, as no evidence of computational efficiency or scalability is provided.
- The claim that the model can be applied to study phase separation is unsupported, as no validation in phase-separation systems is described.
- The general accuracy of the model in reproducing experimental data is unverifiable from the abstract alone.