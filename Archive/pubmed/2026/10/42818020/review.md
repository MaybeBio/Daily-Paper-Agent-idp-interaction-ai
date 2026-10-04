## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no full text, figures, tables, or supplementary materials were provided for evaluation
- **Shared manuscript claim summary** The authors present a unified, physics-based intermediate-resolution framework integrating the HyRes protein and iConNA nucleic acid models to simulate biomolecular phase separation at near-cellular complexity. The framework reportedly predicts saturation concentrations of over 60 disordered proteins within tenfold accuracy, phase diagrams of homotypic RNA and heterotypic protein-nucleic acid condensates, and introduces iConMetabolome, a machine learning-enabled metabolite library capturing metabolite-driven phase separation and experimental partitioning trends.
- **Visible evidence base** Abstract text only; no quantitative data, methodological details, validation statistics, or comparisons to experimental benchmarks are visible
- **Missing materials affecting confidence** Full text, all figures and tables, supplementary information, model parameterization details, training and validation datasets for iConMetabolome, benchmark definitions, and software availability statements

## Reviewer
- **Overall assessment** The abstract describes an ambitious and potentially valuable computational framework for biomolecular condensate simulation. The scope of the claimed capabilities is broad, spanning protein, nucleic acid, and metabolite-driven phase separation. However, the abstract alone provides insufficient detail to assess the technical soundness of the approach, the rigor of the validation, or the reliability of the reported accuracies. The central claims, particularly the tenfold accuracy across 60 proteins and the performance of the machine learning-enabled metabolite library, cannot be evaluated from the supplied material. The work is likely of interest to the computational biophysics and phase separation communities, but the evidence base is currently too limited to establish the case.
- **Who would be interested in the results, and why** Computational biophysicists and physical chemists studying phase separation and condensate formation would be the primary audience. Researchers developing coarse-grained and intermediate-resolution molecular models would also find the integration of protein and nucleic acid models relevant. Additionally, cell biologists investigating condensate regulation by metabolites and those studying disease-associated mutations affecting phase behavior may find the framework useful if the validation holds. The potential to simulate near-cellular complexity is attractive to groups seeking to bridge molecular simulations with cellular-scale phenomena.
- **Major strengths** The framework addresses a recognized gap in the field by unifying protein and nucleic acid models within a single intermediate-resolution platform. The explicit inclusion of multiple interaction types, including hydrogen bonding, electrostatics, cation-π, hydrophobic forces, and nucleic acid-specific terms, suggests a physically grounded approach. The introduction of a machine learning-enabled metabolite library is a novel extension that could broaden the applicability of condensate simulations. The reported scale of validation, over 60 disordered proteins, indicates substantial benchmarking effort if the claims are accurate.
- **Major Concerns**  
  - **Concern ID** R1-M1  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Technical soundness  
    **Claim pointer** The framework accurately predicts saturation concentrations of over 60 disordered proteins within tenfold  
    **Evidence pointer** Abstract, location not provided  
    **Concern** The abstract claims tenfold accuracy for saturation concentrations across over 60 disordered proteins, but no details are provided on the benchmark dataset, the definition of saturation concentration, the error metric used, or the comparison against experimental measurements. Tenfold accuracy is a broad range that may mask significant systematic errors. Without knowing which proteins were tested, how the experimental values were obtained, and whether the predictions are unbiased or tuned, this claim cannot be assessed.  
    **Why it matters** Saturation concentration is a central quantitative observable in phase separation studies. If the tenfold accuracy claim is not rigorously established, the framework's predictive utility for quantitative biology is questionable. Overly broad error bars can obscure poor performance on specific protein classes or interaction regimes.  
    **Resolution test** Provide a table listing all 60 proteins, their experimental and predicted saturation concentrations, the source of experimental data, and the error distribution. Show whether the tenfold accuracy holds across different protein classes, sequence lengths, and charge distributions. Report the correlation coefficient and mean absolute error, not just a fold-range.  
  - **Concern ID** R1-M2  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Technical soundness  
    **Claim pointer** The framework accurately predicts phase diagrams of homotypic RNA and heterotypic protein-nucleic acid condensates  
    **Evidence pointer** Abstract, location not provided  
    **Concern** The abstract states accurate prediction of phase diagrams for RNA and protein-nucleic acid systems, but no specifics are given on which systems were tested, how phase boundaries were computed, or how they compare to experimental phase diagrams. Phase diagram prediction is sensitive to force field balance and finite-size effects in simulations. The claim of accuracy is unsupported without quantitative comparison to experimental binodals or critical concentrations.  
    **Why it matters** Phase diagrams are the defining thermodynamic characterization of condensate-forming systems. If the framework cannot reproduce experimental phase boundaries reliably, its utility for predicting new systems or interpreting mutations is limited. The balance between protein and nucleic acid interaction terms is particularly challenging and requires careful validation.  
    **Resolution test** Show computed and experimental phase diagrams for at least several RNA and protein-nucleic acid systems. Report the deviation in binodal positions, critical concentrations, and coexistence region widths. Describe how finite-size effects and system size were handled in the simulations.  
  - **Concern ID** R1-M3  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Technical soundness  
    **Claim pointer** iConMetabolome, a machine learning-enabled library of cellular metabolites, captures metabolite-driven phase separation and reproduces experimental partitioning trends across condensates  
    **Evidence pointer** Abstract, location not provided  
    **Concern** The machine learning-enabled metabolite library is a significant new component, but the abstract provides no information on the training data, the metabolite feature representation, the machine learning architecture, or the validation against experimental partitioning measurements. The claim that partitioning trends are reproduced is vague without specifying which condensates, which metabolites, and what quantitative agreement was achieved.  
    **Why it matters** Metabolite-driven phase separation is an emerging area, and a predictive library would be valuable. However, machine learning models can easily overfit or generalize poorly if training data are limited or biased. Without details on the training set composition and validation strategy, the reliability of iConMetabolome for novel metabolites is unknown.  
    **Resolution test** Describe the training dataset, including the number and types of metabolites, the source of experimental partitioning data, and the cross-validation scheme. Report quantitative metrics for partitioning prediction accuracy across different condensate types. Show whether the model generalizes to metabolites not included in training.  
  - **Concern ID** R1-M4  
    **Severity** Major  
    **Blocking** No  
    **Axis** Reproducibility  
    **Claim pointer** The framework integrates the HyRes protein and iConNA nucleic acid models  
    **Evidence pointer** Abstract, location not provided  
    **Concern** The abstract does not state whether the framework, including the iConMetabolome library, is publicly available, open source, or documented with sufficient detail for reproduction. No software availability statement is visible.  
    **Why it matters** Reproducibility is a core expectation for computational frameworks. Without access to the code, parameters, and training data, other groups cannot apply the method or verify the claims. This limits the scientific impact and the ability of the community to build on the work.  
    **Resolution test** Provide a clear software availability statement, including a repository link, versioning, and documentation. Make the iConMetabolome library and training data accessible.  
- **Minor Comments**  
  - **Concern ID** R1-m1  
    **Severity** Minor  
    **Axis** Clarity  
    **Affected element** Abstract wording  
    **Evidence pointer** Abstract, location not provided  
    **Issue** The phrase "near-cellular complexity" is not defined. It is unclear what level of system size, molecular count, or compositional diversity is meant by this term.  
    **Required correction** Define "near-cellular complexity" with specific system sizes, molecular numbers, or a comparison to typical cellular condensate dimensions.  
  - **Concern ID** R1-m2  
    **Severity** Minor  
    **Axis** Completeness  
    **Affected element** Abstract scope  
    **Evidence pointer** Abstract, location not provided  
    **Issue** The abstract mentions "over 60 disordered proteins" but does not specify whether these are all from the same family, whether they include both drivers and clients, or whether any were used in training or parameterization of the model.  
    **Required correction** Clarify the selection criteria for the 60 proteins and confirm that the test set was not used in model parameterization.  
  - **Concern ID** R1-m3  
    **Severity** Minor  
    **Axis** Technical detail  
    **Affected element** Force field balance  
    **Evidence pointer** Abstract, location not provided  
    **Issue** The abstract lists hydrogen bonding, electrostatics, cation-π, hydrophobic interactions, base stacking, base pairing, and ion-mediated effects as balanced, but no information is given on how this balance was achieved or validated.  
    **Required correction** Briefly describe the parameterization strategy or refer to prior work where the balance was established.  
  - **Concern ID** R1-m4  
    **Severity** Minor  
    **Axis** Scope  
    **Affected element** Disease relevance  
    **Evidence pointer** Abstract, location not provided  
    **Issue** The abstract states the framework enables dissection of mechanisms in biology and disease, but no disease-related application or example is provided.  
    **Required correction** Either add a specific disease-related example or temper the claim to reflect the framework's potential rather than demonstrated utility.  

## Risk / unsupported claims
- The claim of accurate prediction of saturation concentrations within tenfold for over 60 disordered proteins is unsupported from the abstract alone; no benchmark data or error metrics are visible.
- The claim of accurate phase diagram prediction for RNA and protein-nucleic acid condensates is unsupported; no systems or quantitative comparisons are provided.
- The claim that iConMetabolome reproduces experimental partitioning trends is unsupported; no training data, validation metrics, or specific examples are given.
- The claim of capturing "near-cellular complexity" is not defined and cannot be evaluated.
- The overall assertion of a "unified" framework implies seamless integration of components, but the abstract does not demonstrate that the integrated model performs as well as each component individually or that the integration does not introduce artifacts.