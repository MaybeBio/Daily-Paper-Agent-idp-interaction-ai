## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors report the use of HDAC1/2 pull-downs, crosslinking mass spectrometry (XL-MS), and Integrative Modeling Platform (IMP) to generate structural models of NuRD, SIN3A, and CoREST complexes. They further describe an AlphaFold-enabled, XL-MS-constrained modeling approach to investigate HDAC1 assembly, report that the HDAC1 C-terminal intrinsically disordered region (IDR) folds into alpha helices within these complexes, and present a complete integrative structural model of a NuRD subcomplex containing HDAC1, MBD3, MTA1, GATAD2B, and RBBP4, including six IDRs.
- **Visible evidence base** Abstract text only; no experimental details, model validation metrics, crosslink data, or structural coordinates provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, supplementary data, model quality statistics, crosslink tables, validation procedures, and experimental replicates

## Reviewer
- **Overall assessment** The abstract presents a technically ambitious and potentially valuable application of integrative structural biology to a biologically important family of chromatin remodeling complexes. The combination of XL-MS with AlphaFold-enabled modeling to address the conformation of the HDAC1 CTD IDR is timely and of interest to the structural biology and chromatin fields. However, the abstract alone provides insufficient evidence to evaluate the validity of the central claims, particularly the alpha-helical folding of the HDAC1 IDR and the completeness of the NuRD subcomplex model. The claim that the IDR "folds into alpha helices" is a strong structural statement that requires direct experimental validation and model quality assessment, neither of which is visible in the abstract. The overall case is plausible but not established from the supplied material.
- **Who would be interested in the results, and why** Structural biologists studying protein complexes and intrinsically disordered regions; chromatin researchers investigating HDAC-containing complexes such as NuRD, SIN3, and CoREST; method developers in integrative modeling and crosslinking mass spectrometry. The reported approach may also interest researchers studying other large multi-subunit complexes where IDRs play functional roles.
- **Major strengths** The study addresses a biologically important and technically challenging problem, namely the structure and assembly of HDAC1/2-containing complexes with a focus on a large IDR. The combination of XL-MS with integrative modeling and AlphaFold is a modern and appropriate methodological strategy. The reported construction of a complete NuRD subcomplex model including six IDRs represents a substantial technical achievement if validated. The approaches are stated to be broadly applicable, which increases potential impact.
- **Major Concerns** 
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** "We show that the CTD IDR of HDAC1 folds into alpha helices in these complexes."
  - **Evidence pointer** Abstract only; location not provided
  - **Concern** The abstract asserts a specific secondary structure outcome for the HDAC1 CTD IDR within three different complexes. No experimental evidence, such as circular dichroism, NMR, or cryo-EM density, is described. It is unclear whether the alpha-helical conformation is directly observed or inferred from the integrative models. The confidence in this claim cannot be assessed without model validation metrics, crosslink satisfaction statistics, or independent structural validation.
  - **Why it matters** The folding of a large IDR into alpha helices upon complex assembly is a central and novel claim of the study. If this claim is based solely on model inference without experimental corroboration, it may overstate the certainty of the finding. The structural biology community requires clear distinction between experimentally observed features and model-predicted features.
  - **Resolution test** Provide direct experimental evidence for alpha-helical content in the HDAC1 CTD within the complexes, or clearly state the modeling-based nature of the prediction with appropriate uncertainty estimates and validation metrics such as crosslink satisfaction rates, model precision, and convergence criteria.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** "We built a complete integrative structural model of a NuRD subcomplex including the abundant HDAC1:MBD3:MTA1:GATAD2B:RBBP4 subunits, which included 6 IDRs."
  - **Evidence pointer** Abstract only; location not provided
  - **Concern** The term "complete" is a strong qualifier for a structural model that includes six IDRs. The abstract does not describe how completeness is defined, what resolution or precision the model achieves, how the IDRs are represented, or how the model was validated. Without these details, the claim of completeness cannot be evaluated.
  - **Why it matters** Integrative models of complexes containing multiple IDRs are inherently challenging to validate. The claim of completeness may be interpreted as implying atomic-level accuracy, which is unlikely for IDR-containing regions. Overstatement of model completeness could mislead readers about the reliability of the structure.
  - **Resolution test** Define the criteria for completeness, report model precision and accuracy metrics, describe the representation of IDRs, and provide validation against independent data such as crosslinks not used in modeling or known biochemical constraints.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Methodological transparency
  - **Claim pointer** "We used HDAC1/2 to isolate their protein interaction networks from cells and used crosslinking mass spectrometry (XL-MS) coupled with the Integrative Modeling Platform to build structural models of the NuRD, SIN3A, and CoREST complexes."
  - **Evidence pointer** Abstract only; location not provided
  - **Concern** The abstract does not specify the cell type, the affinity purification strategy, the number of biological replicates, the crosslinking chemistry, or the depth of mass spectrometry analysis. The quality and completeness of the interaction networks and the crosslink datasets are not described.
  - **Why it matters** The reliability of the resulting structural models depends critically on the quality and coverage of the experimental data. Without information on replicate numbers, crosslink filtering criteria, and false discovery rates, the robustness of the input data cannot be assessed.
  - **Resolution test** Provide details on cell lines, purification methods, replicate counts, crosslinker used, mass spectrometry parameters, and data filtering criteria in the full manuscript.
- **Minor Comments** 
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Abstract wording
  - **Evidence pointer** Abstract, first sentence
  - **Issue** The phrase "key enzymatic components in multiple large chromatin remodeling complexes" is somewhat imprecise, as HDAC1/2 are catalytic subunits but the complexes themselves are often referred to as chromatin-modifying or remodeling complexes. Clarification of the distinction between enzymatic activity and complex function would improve precision.
  - **Required correction** Rephrase to specify that HDAC1/2 are catalytic subunits within chromatin-modifying complexes, or clarify the intended meaning of "remodeling."
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** Abstract, description of modeling approach
  - **Evidence pointer** Abstract, "AlphaFold-enabled XL-MS constrained modeling approach"
  - **Issue** The term "AlphaFold-enabled" is not defined. It is unclear whether AlphaFold predictions were used as input restraints, as a scoring function, or for initial model generation. The relationship between AlphaFold and the XL-MS constraints is ambiguous.
  - **Required correction** Define the specific role of AlphaFold in the modeling pipeline, for example whether it provided subunit structures, inter-subunit orientations, or conformational sampling.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Generalizability claim
  - **Affected element** Abstract, final sentence
  - **Evidence pointer** Abstract, "The approaches used herein are broadly applicable"
  - **Issue** The claim of broad applicability is plausible but not substantiated in the abstract. No discussion of potential limitations or required adaptations for other systems is provided.
  - **Required correction** Briefly note the conditions under which the approach is applicable, or temper the claim to reflect the specific context of this study.

## Risk / unsupported claims
- The claim that the HDAC1 CTD IDR "folds into alpha helices" is unsupported in the abstract, as no direct experimental evidence or model validation metrics are provided.
- The claim of a "complete" NuRD subcomplex model is not assessable without defined completeness criteria and model quality statistics.
- The general applicability of the approach is stated without supporting evidence or discussion of limitations.
- The quality and coverage of the XL-MS datasets and interaction networks cannot be evaluated from the abstract.
- The specific role of AlphaFold in the modeling pipeline is not described, making the methodological novelty difficult to assess.

## Assessment against Nature-style criteria
- **Originality** The combination of XL-MS with AlphaFold-enabled integrative modeling to address IDR conformation within large chromatin complexes is a novel and potentially original contribution. However, the abstract does not clearly distinguish what is new relative to prior integrative modeling studies of these complexes.
- **Scientific importance** The HDAC1/2-containing complexes are central to gene regulation, and understanding their assembly and the role of the CTD IDR is of significant biological importance. If the structural claims are validated, the work would be of high importance.
- **Interdisciplinary readership** The work bridges structural biology, proteomics, and chromatin biology, and would appeal to readers across these disciplines. The methodological aspects may also interest computational biologists.
- **Technical soundness** Not assessable from the abstract. The absence of validation metrics, data quality descriptions, and methodological details prevents evaluation of technical rigor.
- **Readability for nonspecialists** The abstract is generally readable but uses specialized terminology without sufficient context. Terms such as "Integrative Modeling Platform" and "AlphaFold-enabled XL-MS constrained modeling" would benefit from brief explanation for a broader audience.

## Recommendation posture
Currently not established from the provided evidence. The study addresses an important problem with a promising methodological approach, and the authors should be encouraged to resubmit a version in which the structural claims are supported by explicit validation data and the modeling pipeline is described with sufficient transparency. The recommendation is supportive in principle, conditional on the authors providing the missing evidence in the full manuscript.