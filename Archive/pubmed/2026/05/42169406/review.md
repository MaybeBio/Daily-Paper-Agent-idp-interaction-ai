## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no full text, figures, or supplementary materials provided
- **Shared manuscript claim summary** The authors assert that the net charge of fluorescent proteins (FPs) modulates condensation of the FUS low-complexity domain (LCD) in vivo, based on fluorescence imaging and molecular dynamics simulations in Escherichia coli, and recommend careful FP selection for accurate and reproducible condensation studies.
- **Visible evidence base** Abstract text only; no experimental details, quantitative data, or simulation parameters
- **Missing materials affecting confidence** Full manuscript, methods, figures, tables, simulation protocols, statistical analyses, and any control experiments

## Reviewer
- **Overall assessment** The abstract presents a plausible and potentially important hypothesis that FP charge can perturb protein condensation, using FUS LCD as a model. However, the evidence base is limited to a summary with no quantitative results, controls, or methodological detail. The core claim is biologically reasonable but not established from the supplied material. The recommendation to consider FP charge is sensible, but the abstract does not provide sufficient support to assess technical rigor or generalizability.
- **Who would be interested in the results, and why** Researchers in cell biology, biophysics, and molecular imaging who use fluorescent protein tags to study phase separation or other biomolecular condensates. The work could inform experimental design choices, particularly for studies where electrostatic interactions are critical. It may also interest developers of fluorescent protein variants with tailored charge properties.
- **Major strengths** The hypothesis addresses a widely overlooked variable in a popular experimental approach. The use of a physiologically relevant model system (FUS LCD) and a range of FP net charges is a logical design. The combination of in vivo imaging and molecular dynamics simulation is a potentially powerful approach to link observations to molecular mechanisms.
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
  - Originality: Moderate. The idea that FP charge affects condensation is not entirely novel, as electrostatic effects on phase separation are known, but applying this specifically to FP tags in vivo is a useful contribution.  
  - Scientific importance: Potentially high for the imaging and phase separation communities, but the abstract does not demonstrate broad impact beyond a cautionary note.  
  - Interdisciplinary readership: Relevant to biophysics, cell biology, and chemical biology, but the abstract lacks detail to engage nonspecialists.  
  - Technical soundness: Not assessable from the abstract; no data, controls, or methods are provided.  
  - Readability for nonspecialists: The abstract is clear and accessible, but technical terms (e.g., LCD, net charge) are not fully explained.
- **Recommendation posture** Currently not established from the provided evidence. Supportive if technical concerns are resolved with full data and rigorous analysis.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The abstract claims that "fluorescence imaging and molecular dynamics simulation revealed distinct condensation patterns that correlated with FP charge."  
- **Evidence pointer** Abstract, location not provided  
- **Concern** No quantitative data, representative images, or simulation results are presented. The correlation between FP charge and condensation patterns is stated but not substantiated with metrics such as condensate size, number, or density, nor with statistical significance.  
- **Why it matters** Without quantitative evidence, the core claim of a charge-dependent effect cannot be evaluated. Correlation alone does not establish causation, and alternative explanations (e.g., FP expression levels, folding stability, or interactions beyond charge) are not addressed.  
- **Resolution test** Provide quantitative data from imaging (e.g., condensate counts, size distributions) and simulation (e.g., free energy profiles, contact maps) with statistical analysis, and demonstrate that the effect scales with FP net charge in a controlled manner.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Experimental controls  
- **Claim pointer** The abstract implies that FP charge, rather than other FP properties, is the primary modulator of FUS LCD condensation.  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The abstract does not mention control experiments to isolate charge effects from other FP characteristics, such as hydrophobicity, size, or specific surface residues. It is unclear whether FPs with similar charge but different structures were compared, or whether charge-neutralized mutants were used.  
- **Why it matters** Without appropriate controls, the observed condensation differences could be attributed to factors other than net charge, undermining the central conclusion and the practical recommendation.  
- **Resolution test** Include experiments with FP variants matched for size and structure but differing only in net charge, or use charge-altering mutations to confirm that condensation changes are charge-specific.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Methodological detail  
- **Claim pointer** The abstract states that FPs with "a wide range of net charges at physiological pH" were used and that simulations were performed, but no specifics are given.  
- **Evidence pointer** Abstract, location not provided  
- **Concern** The abstract lacks details on which FPs were used, their net charge values, the simulation force field, system setup, and timescales. Without this information, the reproducibility and technical validity of the methods cannot be assessed.  
- **Why it matters** Reproducibility is a core requirement for scientific claims. The absence of methodological detail prevents readers from evaluating the robustness of the findings or replicating the experiments.  
- **Resolution test** Provide a full methods section with FP identities, charge calculations, simulation parameters, and validation of the simulation against experimental observations.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Abstract wording  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The phrase "small charged biomolecules are a main driver in protein condensation" is overly broad and could be misinterpreted as a universal rule, whereas the role of charge varies by system.  
- **Required correction** Qualify the statement to specify that electrostatic interactions are one of several drivers, and cite relevant examples or conditions.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Generalizability  
- **Affected element** Recommendation  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The recommendation to select FPs based on electrostatic properties is made for "accuracy and reproducibility," but the abstract does not discuss whether the findings extend beyond FUS LCD to other condensation-prone proteins.  
- **Required correction** Acknowledge the model-specific nature of the study and suggest that the principle be tested in additional systems before broad application.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Terminology  
- **Affected element** Use of "in vivo"  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The term "in vivo" is used for expression in Escherichia coli, which is a prokaryotic system. This is technically correct but may be confusing to readers who associate "in vivo" with eukaryotic organisms.  
- **Required correction** Clarify the context, e.g., "in bacterial cells" or "in a cellular context," to avoid ambiguity.

## Risk / unsupported claims
- The claim that FP net charge "can affect protein condensation" is unsupported by quantitative evidence in the abstract.
- The assertion that "distinct condensation patterns correlated with FP charge" is not verifiable without data.
- The recommendation for FP selection based on electrostatic properties is reasonable but not empirically validated in the abstract.
- Any mechanistic interpretation from molecular dynamics simulations is unassessable without simulation details.