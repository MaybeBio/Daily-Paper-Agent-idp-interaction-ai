## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors use the residue-resolution coarse-grained model Mpipi to simulate 140 prion-like domain (PLD) mutants from six proteins, identify scaling laws relating the number and type of amino acid mutations to changes in critical solution temperature, and propose these scaling laws as predictive tools for PLD condensate stability.
- **Visible evidence base** Abstract text only; no quantitative results, simulation details, or statistical analyses are available
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, simulation parameters, validation data, and any statistical or error analysis

## Reviewer
- **Overall assessment** The abstract presents a potentially valuable quantitative framework for predicting how amino acid mutations alter PLD phase behavior. The claim of scaling laws spanning multiple PLD families is intriguing and could have broad utility. However, the abstract alone provides insufficient evidence to evaluate the robustness, generality, or predictive accuracy of the proposed scaling laws. Key details on simulation methodology, error quantification, and validation against experimental data are absent. The central claim that these scaling laws are predictive across the entire tested family is not substantiated from the supplied material.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, and prion-like domains would find these results relevant. The work also speaks to the broader community interested in sequence-to-behavior relationships in intrinsically disordered proteins and in computational tools for predicting mutation effects on protein phase behavior. Those developing or using coarse-grained models for biomolecular systems would also be interested.
- **Major strengths** The study addresses a timely and important problem, namely predicting how mutations affect PLD-driven phase separation. The use of a residue-resolution model across multiple protein families is a sensible approach. The concept of scaling laws linking mutation number and type to critical temperature changes is elegant and potentially generalizable.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria**  
  Originality: The scaling law concept is novel in this context, though the abstract does not clarify how it differs from prior empirical rules for mutation effects on phase separation.  
  Scientific importance: If validated, the work could provide a practical predictive tool, which is of high importance to the condensate field.  
  Interdisciplinary readership: The topic bridges biophysics, computational biology, and cell biology, and the abstract is written accessibly enough for nonspecialists.  
  Technical soundness: Cannot be assessed from the abstract alone; no methodological detail or error analysis is provided.  
  Readability for nonspecialists: The abstract is clear and concise, with technical terms defined implicitly through context.
- **Recommendation posture** Currently not established from the provided evidence. The abstract is promising, but the core claims require full manuscript evaluation. I would be supportive if the technical concerns are resolved in the full paper.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The abstract claims that simulations reveal scaling laws that quantify the range of change in critical solution temperature as a function of the number and type of amino acid mutations, and that these rules extend across the entire family tested.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The abstract provides no quantitative data, no definition of the scaling laws, no measure of fit quality, and no statistical confidence intervals. Without these, the existence and generality of the scaling laws cannot be evaluated.  
- **Why it matters** The central contribution of the work is the scaling law claim. If the scaling laws are not robustly demonstrated with error bars and goodness-of-fit metrics, the predictive utility claimed in the abstract is unsupported.  
- **Resolution test** Provide the functional form of the scaling laws, the coefficient of determination or equivalent fit statistics, and confidence intervals for the scaling exponents across the six proteins.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Validation  
- **Claim pointer** The abstract implies that the scaling laws are consistent with physicochemical properties of mutations and can be used as predictive tools.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** No comparison to experimental data or to independent computational predictions is presented. The claim of predictive utility requires external validation, not just internal consistency within the simulation set.  
- **Why it matters** A scaling law fitted to simulation data may be an artifact of the model. Without validation against experimental phase behavior or orthogonal methods, the claim that these rules predict real PLD condensate stability is premature.  
- **Resolution test** Include a validation section comparing predicted critical temperature changes to experimental measurements for at least a subset of mutants, or to predictions from an independent model.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Methodological transparency  
- **Claim pointer** The abstract states that the Mpipi model is accurate at residue resolution and is used to quantify mutation effects.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** No information is given on simulation length, number of replicas, equilibration criteria, finite-size effects, or how critical temperatures were extracted from simulations. The accuracy of Mpipi for this specific application is asserted but not demonstrated.  
- **Why it matters** The reliability of the scaling laws depends entirely on the accuracy and convergence of the underlying simulations. Without methodological detail, the reader cannot assess whether the reported trends are physically meaningful or simulation artifacts.  
- **Resolution test** Provide a methods section with full simulation parameters, convergence checks, and a benchmark of Mpipi predictions against experimental critical temperatures for wild-type PLDs.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Definition of "range of change"  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The phrase "range of change in the critical solution temperature" is ambiguous. It is unclear whether this refers to the absolute shift, the spread across mutants, or a normalized quantity.  
- **Required correction** Define this quantity explicitly, for example as the difference between mutant and wild-type critical temperature, and specify units.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Mutant selection criteria  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The abstract states that 140 mutants from six proteins were studied but does not explain how these mutants were chosen. If the selection is biased toward certain mutation types, the scaling laws may not be general.  
- **Required correction** State the criteria for mutant selection, including whether they are disease-associated, random, or systematic substitutions.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Generalizability  
- **Affected element** Claim of extension across the entire family  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The abstract claims the scaling laws extend across the entire family tested, but only six proteins are included. This is a small sample for a claim of family-wide generality.  
- **Required correction** Acknowledge the limited number of families and discuss how the scaling laws might be tested on additional PLD-containing proteins.

## Risk / unsupported claims
- The existence of scaling laws relating mutation number and type to critical temperature changes is unsupported without quantitative data.
- The claim that these scaling laws are consistent with physicochemical properties of mutations is unsupported without a defined physicochemical framework.
- The claim that scaling laws can be used as predictive tools is unsupported without external validation.
- The accuracy of the Mpipi model for this application is asserted but not demonstrated.
- The generality of the scaling laws across the entire tested family is not assessable from the abstract alone.