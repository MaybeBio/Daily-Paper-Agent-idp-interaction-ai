## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results and discussion, conclusions, and materials and methods
- **Assessment boundary** Technical and scientific evaluation of the claims presented in the manuscript, based solely on the provided text
- **Shared manuscript claim summary** The authors report a double-shell protein engineering strategy (apoferritin inner shell, KIX cargo, MBP outer shell) that enables cryo-EM structure determination of the 11 kDa KIX domain at 2.6 Å resolution, and use this system to characterize a computationally designed peptide inhibitor of the KIX-pKID interaction relevant to acute myeloid leukemia
- **Visible evidence base** Abstract, full text narrative, methods descriptions, references to supplementary figures and tables (Figures S1-S7, Tables S1-S3)
- **Missing materials affecting confidence** Supplementary figures and tables referenced but not provided; no structural coordinates or validation metrics beyond those mentioned in text; no raw cryo-EM data or processing details beyond summary statistics; no peptide synthesis or characterization data; no full simulation parameters or trajectory analyses

## Reviewer
- **Overall assessment** The manuscript presents a technically ambitious approach to a genuine problem in structural biology: determining high-resolution structures of small, flexible proteins by cryo-EM. The double-shell design is creative and the 2.6 Å resolution achieved for the KIX domain is notable. However, several claims require closer scrutiny. The resolution of the peptide inhibitor density at ~4.5 Å is marginal for the structural conclusions drawn. The functional data are limited to in vitro binding assays, and the therapeutic relevance to AML is asserted rather than demonstrated. The computational peptide design pipeline is described but the rationale for specific sequence choices is not fully transparent. The manuscript would benefit from clearer presentation of validation statistics and a more cautious interpretation of the peptide binding mode.
- **Who would be interested in the results, and why** Structural biologists working on small protein targets and cryo-EM methodology development would find the double-shell approach of interest. Researchers in protein-protein interaction inhibitor design, particularly those targeting transcriptional coactivator complexes, would value the peptide design strategy. The broader drug discovery community interested in structure-based approaches for challenging targets may also find the work relevant.
- **Major strengths** The double-shell engineering concept is elegant and addresses a real limitation in cryo-EM. The integration of cryo-EM, protein engineering, molecular dynamics simulation, and biochemical validation represents a comprehensive approach. The achievement of 2.6 Å resolution for an 11 kDa protein is technically impressive. The demonstration that the KIX domain retains its native fold within the engineered scaffold provides confidence in the system's utility.
- **Major Concerns** 
  - R1-M1: The peptide density at ~4.5 Å is insufficient to support the claimed helix-helix interaction mode. At this resolution, secondary structure elements may be discernible but side chain interactions cannot be reliably assigned. The authors state "we can only resolve its density at ~4.5 Å" which is honest, but then proceed to draw specific conclusions about the binding mode that require higher resolution.
  - R1-M2: The functional significance of the peptide inhibitors is not established. The IC50 values reported (50-311 μM) are weak for a therapeutic lead. The authors claim these are "initial candidates" but the path from these values to therapeutic development is not articulated. No cellular or in vivo data are presented to support the AML relevance.
  - R1-M3: The computational peptide design methodology is described at a level that prevents reproduction or critical evaluation. The text states simulations were used to "identify minimal segments" and "propose sequence variations" but the specific criteria for hotspot identification, the scoring functions used, and the selection rationale for the 10 peptides are not provided.
  - R1-M4: The claim that this system "can be applied to drug discovery for all these related diseases" (referring to p53, FOXO3a, BRCA1, HIV Tat interactions) is an overstatement. The manuscript demonstrates feasibility for one target with one peptide; generalization to other targets requires additional validation.
- **Minor Comments**
  - R1-m1: The abstract states "2.6 Å resolution" but the text reports 2.57 Å for MKF and 2.3 Å for MKF-peptide-7. The discrepancy should be clarified.
  - R1-m2: The statement "The theoretical atomic resolution limit of 38 kDa for single-particle cryo-EM analysis (SPA) was proposed in 1995" is presented without citation and may be misleading. The resolution limits for cryo-EM have been revised substantially since 1995.
  - R1-m3: The methods state "No unexpected or unusually high safety hazards were encountered" which is unusual in a methods section and could be removed.
  - R1-m4: The authors note that the KIX domain moves outward by 7.3 Å upon peptide binding. This is an interesting observation but the functional significance is not discussed.
  - R1-m5: The manuscript would benefit from a more detailed comparison of the double-shell approach with existing strategies for small protein cryo-EM, such as antibody fragment binding or fusion to larger scaffolds.
- **Technical failings that need to be addressed before the case is established** R1-M1 (peptide density interpretation), R1-M3 (computational design transparency), R1-M4 (overgeneralization of applicability)
- **Assessment against Nature-style criteria** 
  - Originality: The double-shell concept is novel and represents a creative solution to a recognized problem. The specific application to KIX and peptide inhibitor design adds value.
  - Scientific importance: The work addresses a methodological gap in cryo-EM and a biological target of therapeutic interest. However, the demonstrated impact is limited to one system with modest binding affinities.
  - Interdisciplinary readership: The work spans structural biology, protein engineering, computational chemistry, and cancer biology, which could attract broad interest if the claims are well supported.
  - Technical soundness: The cryo-EM methodology appears sound for the scaffold structure, but the peptide complex interpretation exceeds the resolution. The simulation methodology lacks sufficient detail for evaluation.
  - Readability for nonspecialists: The manuscript is generally well written and accessible, though some sections (particularly the computational design) assume specialist knowledge.
- **Recommendation posture** Supportive if technical concerns are resolved. The core methodological advance is valuable, but the peptide binding mode interpretation, computational design transparency, and scope of claims require revision before the case is fully established.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of structural interpretation
- **Claim pointer** The authors claim a specific helix-helix interaction between peptide 7 and a single KIX helix (α3), with a 30.9° offset compared to the pKID binding mode
- **Evidence pointer** Results and Discussion section, Figure 3c-d, Figure S4d, Figure S5
- **Concern** The peptide density is reported at ~4.5 Å resolution. At this resolution, while secondary structure elements may be visible, the assignment of a specific helix-helix interaction mode and the measurement of a 30.9° angle between helices requires atomic-level detail that is not available. The authors acknowledge the limited resolution but proceed to draw conclusions that exceed what the data can support. The claim of a "unique binding mode" is particularly strong given the resolution limitations.
- **Why it matters** The structural interpretation of the peptide binding mode is a central claim of the manuscript and the basis for the proposed therapeutic strategy. If the binding mode is incorrectly assigned, the design principles for next-generation inhibitors would be flawed. The distinction between a genuine alternative binding mode and an artifact of limited resolution is critical.
- **Resolution test** Provide validation of the peptide density at higher resolution, or temper the claims to reflect the resolution limits. Show clear density for side chains at the interaction interface. Alternatively, provide independent validation of the binding mode through mutagenesis or other biochemical approaches.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Functional validation and therapeutic relevance
- **Claim pointer** The authors state the peptides "can be used as initial candidates of KIX-pKID inhibitors for further improvements" and imply therapeutic relevance to AML
- **Evidence pointer** Results and Discussion section, Figure 3b, Figure S6, Table S3
- **Concern** The reported IC50 values (50-311 μM) are weak for therapeutic leads. The manuscript does not provide cellular assays, selectivity data, or any demonstration of functional inhibition in a disease-relevant context. The connection to AML is based on the known role of the KIX-pKID interaction in this disease, but no AML-specific experiments are presented. The claim of therapeutic relevance is therefore not supported by the data.
- **Why it matters** The title and framing of the manuscript emphasize therapeutic development against AML. Without functional validation beyond in vitro binding, the therapeutic claims are premature. This affects the significance of the work and its potential impact on the field.
- **Resolution test** Provide cellular assays demonstrating inhibition of CREB-mediated transcription or AML cell proliferation. Alternatively, reframe the claims to focus on the methodological advance and the identification of initial binding scaffolds, without asserting therapeutic relevance.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility and transparency of computational methods
- **Claim pointer** The authors state they used molecular dynamics simulations to design 10 peptides, identifying "minimal segments" and "sequence variations" to explore hotspots
- **Evidence pointer** Materials and Methods section, Computational Design of Therapeutic Peptides
- **Concern** The computational design methodology is described at a level that prevents reproduction. The text mentions simulations of 1 μs length and analysis of RMSF, but does not specify: the force field parameters beyond CHARMM36m, the simulation temperature and pressure coupling schemes, the criteria for defining "hotspots," the scoring function used to rank peptide candidates, or the rationale for the specific sequence variations tested. The selection of peptide 7 as the best candidate is not justified with quantitative metrics.
- **Why it matters** The computational design is a key component of the manuscript's contribution. Without sufficient methodological detail, the work cannot be reproduced or independently evaluated. This undermines confidence in the design strategy and the validity of the resulting peptides.
- **Resolution test** Provide complete simulation parameters, the criteria for hotspot identification, the scoring metrics used to rank peptides, and a comparison of predicted versus experimentally observed binding affinities for all 10 peptides.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scope of claims
- **Claim pointer** The authors state the double-shell system "can be applied to drug discovery for all these related diseases" and suggest applications in vaccine development
- **Evidence pointer** Conclusions section
- **Concern** The manuscript demonstrates the double-shell approach for one protein (KIX) with one peptide. The generalization to other targets (p53, FOXO3a, BRCA1, HIV Tat) and to vaccine development is speculative. Each new target would require optimization of the scaffold, disulfide bond placement, and expression conditions. The claim of universal applicability is not supported by the data.
- **Why it matters** Overstated claims can mislead readers and overstate the maturity of the technology. The manuscript's value lies in the demonstrated proof-of-concept, not in unvalidated generalizations.
- **Resolution test** Either provide additional examples of the double-shell system applied to other targets, or temper the claims to reflect the demonstrated scope.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Internal consistency
- **Affected element** Abstract and Results
- **Evidence pointer** Abstract, Results and Discussion section
- **Issue** The abstract states 2.6 Å resolution while the text reports 2.57 Å for MKF and 2.3 Å for MKF-peptide-7. This discrepancy may confuse readers.
- **Required correction** Use consistent resolution values throughout the manuscript.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Citation accuracy
- **Affected element** Introduction
- **Evidence pointer** Introduction section
- **Issue** The statement about a "theoretical atomic resolution limit of 38 kDa" proposed in 1995 lacks a citation and may be outdated given advances in cryo-EM technology.
- **Required correction** Provide the appropriate citation and contextualize the statement with more recent developments.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Materials and Methods
- **Evidence pointer** Materials and Methods section
- **Issue** The sentence "No unexpected or unusually high safety hazards were encountered" is unconventional in a methods section and adds no scientific value.
- **Required correction** Remove this sentence or integrate it into a standard safety statement if required by the journal.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results and Discussion
- **Evidence pointer** Results and Discussion section, Figure 3e
- **Issue** The observation that the KIX domain moves outward by 7.3 Å upon peptide binding is reported without discussion of its potential functional significance or whether this movement is an artifact of the scaffold.
- **Required correction** Add a brief discussion of the possible implications of this movement or acknowledge it as a scaffold-related observation.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Context
- **Affected element** Introduction
- **Evidence pointer** Introduction section
- **Issue** The manuscript does not compare the double-shell approach with other strategies for small protein cryo-EM, such as antibody fragment binding, nanodiscs, or fusion to larger scaffolds.
- **Required correction** Add a brief comparison with existing approaches to contextualize the novelty and advantages of the double-shell system.

## Risk / unsupported claims
- The claim of a "unique binding mode" for peptide 7 based on ~4.5 Å resolution density is not supported by the data
- The assertion that the double-shell system "can be applied to drug discovery for all these related diseases" is speculative and not demonstrated
- The suggestion that the system "may also play a role in vaccine development" is not supported by any experimental evidence
- The therapeutic relevance to AML is asserted based on the known biological role of the KIX-pKID interaction, but no AML-specific functional data are presented
- The computational peptide design methodology is described at a level that prevents evaluation of the design rationale or reproduction of the results