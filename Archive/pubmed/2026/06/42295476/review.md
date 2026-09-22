## Review setup

- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no access to methods, figures, tables, or supplementary material
- **Shared manuscript claim summary** The authors use computational modeling to predict the structure and disordered regions of the TYLCV C2 protein, generate domain deletion and point mutants, and assess subcellular localization and HR-like responses in *Nicotiana benthamiana*. They conclude that the zinc finger domain is important for structural integrity and biological activity, the NLS is important for nuclear localization, and that there is potential interplay between ordered domains and predicted IDRs.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or statistical details provided
- **Missing materials affecting confidence** Full methods, all experimental data (microscopy images, DAB staining results, MD simulation trajectories), statistical analyses, construct validation data, and any negative controls

## Reviewer

- **Overall assessment** The abstract presents a plausible and potentially interesting integration of computational prediction with experimental validation for a viral protein of functional significance. However, the evidence base available for review is limited to the abstract, which precludes verification of the central claims. The conclusions regarding the zinc finger's role in structural integrity and the NLS's role in localization are reasonable but not fully established from the abstract alone. The study would benefit from clearer presentation of quantitative data and explicit statistical support.
- **Who would be interested in the results, and why** Plant virologists studying geminivirus-host interactions, researchers interested in intrinsically disordered proteins in viral pathogenesis, and computational biologists working on structure-function prediction of small viral proteins. The work may also appeal to those studying plant innate immunity and HR-like responses.
- **Major strengths** The study addresses a relevant gap in understanding the structural basis of C2 multifunctionality. The combination of computational prediction with experimental mutagenesis and in planta assays is a sensible approach. The use of multiple complementary methods (structure prediction, disorder prediction, MD simulations, confocal microscopy, HR assays) strengthens the potential impact.
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
  - Originality: Moderate. The application of IDR prediction to a geminiviral C2 protein is somewhat novel, but the general concept of viral proteins using disordered regions for multifunctionality is established.
  - Scientific importance: Moderate. The findings could inform understanding of geminivirus pathogenesis, but the significance is not clearly demonstrated from the abstract.
  - Interdisciplinary readership: Limited. The work bridges virology and computational biology, but the appeal beyond these fields is unclear.
  - Technical soundness: Not assessable from the abstract. Key experimental details and statistical analyses are absent.
  - Readability for nonspecialists: The abstract is generally clear, though some terms (e.g., COP9 signalosome, TGS/PTGS) may require background knowledge.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising, but the current evidence base is insufficient to fully establish the claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "Wild-type C2 localized predominantly to the nucleus and was associated with HR-like responses. In contrast, deletion of the NLS, Zinc finger, or activation domain, or cysteine mutations in the zinc finger were associated with loss of detectable HR-like responses."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract states that HR-like responses were "associated with" wild-type C2 and "loss of detectable" responses in mutants, but no quantitative data, representative images, or statistical comparisons are provided. The terms "associated with" and "detectable" are vague and do not establish the strength or reproducibility of the observed phenotypes.
- **Why it matters** The central conclusion that the zinc finger and NLS are functionally important relies on these phenotypic differences. Without quantitative or statistical support, the claim that these domains are required for HR-like responses is not established.
- **Resolution test** Provide quantitative measurements of HR incidence or severity (e.g., percentage of infiltrated areas showing HR, electrolyte leakage assays) with appropriate statistical tests comparing wild-type and each mutant. Include representative images with scale bars and clear descriptions of scoring criteria.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical validation
- **Claim pointer** "Molecular dynamics simulations further showed that deletion of the zinc finger destabilized the protein, whereas removal of the NLS or activation domain produced more compact conformations."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The MD simulation results are presented as definitive findings, but no details are given on simulation parameters, force fields, simulation length, convergence criteria, or how "destabilization" and "compactness" were quantified. Without these details, the reliability of the simulations cannot be assessed.
- **Why it matters** The claim that the zinc finger is important for structural integrity is a key conclusion. If the MD simulations are not robustly performed or analyzed, this conclusion is unsupported.
- **Resolution test** Provide full MD methods including software, force field, water model, simulation time, temperature/pressure coupling, and analysis metrics (e.g., RMSD, RMSF, radius of gyration). Show convergence plots and replicate simulations to demonstrate reproducibility.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Construct validation
- **Claim pointer** "domain deletion mutants (del NLS, del ZnFn, del AD) and zinc finger point mutants (C37A, C39A) were generated and transiently expressed in Nicotiana benthamiana as CFP fusion proteins."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract does not state whether the mutant proteins were expressed at comparable levels to wild-type C2. If expression levels differed, the observed loss of HR-like responses could be due to reduced protein accumulation rather than loss of function.
- **Why it matters** Differential expression is a common confound in mutagenesis studies. Without confirming equivalent expression, the functional conclusions are not reliable.
- **Resolution test** Include Western blot or fluorescence intensity quantification showing comparable expression levels of all constructs. If expression levels differ, perform normalization or use a complementation assay to confirm functional specificity.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Subcellular localization claim
- **Evidence pointer** Abstract only; location not provided
- **Issue** The abstract states that wild-type C2 "localized predominantly to the nucleus" but does not specify the proportion of cells showing nuclear localization or whether any cytoplasmic or nucleolar localization was observed.
- **Required correction** Provide quantitative localization data (e.g., percentage of cells with nuclear vs. cytoplasmic fluorescence) and describe any additional localization patterns observed.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "HR-like response"
- **Evidence pointer** Abstract only; location not provided
- **Issue** The term "HR-like" is used without definition. It is unclear whether this refers to a hypersensitive response phenotype that is visually similar to HR but not confirmed to be HR, or whether it is a distinct response.
- **Required correction** Define "HR-like" explicitly in the methods or results, and clarify the criteria used to distinguish it from a canonical HR.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Disorder prediction validation
- **Evidence pointer** Abstract only; location not provided
- **Issue** The abstract mentions predicted IDRs between residues 40-120 but does not state whether these predictions were experimentally validated (e.g., by limited proteolysis or NMR).
- **Required correction** State whether experimental validation of IDRs was performed, or explicitly note that the IDR predictions are computational only.

## Risk / unsupported claims

- The claim that the zinc finger domain is "important for structural integrity" is not supported by the abstract alone, as no structural data on the mutants are presented.
- The claim that "removal of the NLS or activation domain produced more compact conformations" is not verifiable without MD simulation details.
- The functional significance of the predicted IDRs (residues 40-120) is asserted but not experimentally tested, making this claim speculative.
- The statement that C2 "orchestrates trans-activation of viral promoters" and "subverts host immunity" is presented as background and is not directly tested in this study; it should be clearly framed as prior knowledge.
- The overall conclusion of "potential interplay between ordered domains and predicted intrinsically disordered regions" is a hypothesis, not a demonstrated finding, based on the abstract.