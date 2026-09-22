## Review setup

- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors report use of a peptide-matrix based proteomic screen (PRISMA) coupled to quantitative mass spectrometry to map interaction interfaces on the ARID1A protein at high sequence resolution. They claim the assay recapitulates known BAF subunit and YAP1 interactions, identifies SIN3A as a binding partner, and nominates TOX4, CDK2, and CCNA2 as novel interactors. They further report that mutation of a CDK2 phosphorylation site in ARID1A alters expression of microtubule-related genes and impairs cell proliferation, and they argue the method captures weak or low-abundance interactions missed by conventional affinity purification.
- **Visible evidence base** Abstract text only. No experimental details, quantitative data, statistical analyses, or methodological controls are visible.
- **Missing materials affecting confidence** Full manuscript, all figures and tables, supplementary datasets, detailed PRISMA methodology, mass spectrometry parameters, validation experiments, and statistical reporting. None of the claims can be independently assessed from the supplied material.

## Reviewer

- **Overall assessment** The abstract presents a potentially valuable technical advance and a set of biologically interesting candidate interactions for ARID1A, a cancer-relevant chromatin regulator. The central premise, that peptide-array based screening can map interaction interfaces at residue-level resolution and capture low-affinity interactions, is plausible and of interest to the chromatin and proteomics communities. However, the abstract alone provides no quantitative evidence, no controls, no validation of the novel interactors, and no demonstration that the reported functional effects are causally linked to the identified phosphorylation site. The case is currently not established from the provided evidence.
- **Who would be interested in the results, and why** Chromatin biologists studying SWI/SNF complex assembly and function; cancer researchers focused on ARID1A mutations and their oncogenic mechanisms; proteomics method developers interested in interaction screening technologies; and cell cycle researchers given the proposed CDK2 link. The resource value of a high-resolution ARID1A interaction map would appeal broadly to these groups.
- **Major strengths** The technical concept is innovative and addresses a genuine gap, since ARID1A interactions are numerous but poorly mapped at the interface level. The use of an orthogonal screening approach to complement affinity purification is methodologically sensible. The inclusion of a functional readout, namely the CDK2 phosphorylation site mutation, adds a mechanistic dimension beyond a purely descriptive interaction list. The claim that the method detects low-abundance or weak interactions is potentially significant if substantiated.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The abstract states that PRISMA identifies TOX4, CDK2, and CCNA2 as novel interactors and that mutation of a CDK2 phosphorylation site in ARID1A leads to altered gene expression and proliferation defects.
  - **Evidence pointer** Abstract only; location not provided
  - **Concern** No quantitative data, validation experiments, or statistical measures are presented for any of the claimed novel interactions. It is unclear whether these candidates were confirmed by orthogonal methods such as co-immunoprecipitation, whether the interactions are direct, and whether the CDK2 site mutation effects are specific or off-target. The causal link between the phosphorylation site and the observed phenotypes is asserted but not demonstrated.
  - **Why it matters** Novel interactor claims and functional assignments are the core scientific contributions. Without validation and appropriate controls, these claims cannot be distinguished from false positives inherent to high-throughput peptide screens, and the functional conclusion may be premature.
  - **Resolution test** Provide orthogonal validation of each novel interactor, demonstrate specificity of the CDK2 site mutation through rescue experiments or phospho-mimetic mutants, and include appropriate statistical comparisons for the gene expression and proliferation data.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Methodological rigor
  - **Claim pointer** The abstract claims that PRISMA recapitulates known BAF subunit binding and detects the YAP1 PPXY motif interaction, and that the method uncovers weak or low-abundance interactions not detectable by traditional affinity purification.
  - **Evidence pointer** Abstract only; location not provided
  - **Concern** No details are given on the peptide library design, coverage of the ARID1A sequence, peptide concentrations, mass spectrometry thresholds, false discovery rates, or how the authors distinguished specific from non-specific binding. The comparative claim against affinity purification is not supported by any direct experimental comparison in the abstract.
  - **Why it matters** The utility of the method and the validity of the interaction map depend entirely on the quality and controls of the screen. Without these details, the reader cannot assess whether the reported interactions are biologically meaningful or artifacts of the peptide array format.
  - **Resolution test** Describe the peptide library design and coverage, report false discovery rates and replicate concordance, and include a direct comparison of PRISMA results with affinity purification data for the same baits.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Functional relevance
  - **Claim pointer** The abstract states that mutation of a cell cycle-dependent CDK2 phosphorylation site in ARID1A leads to altered gene expression of microtubule factors and defects in cell proliferation.
  - **Evidence pointer** Abstract only; location not provided
  - **Concern** The abstract does not specify which ARID1A residue was mutated, how the mutation affects CDK2 phosphorylation, or whether the observed transcriptional and proliferation changes are a direct consequence of losing this phosphorylation event. The connection to microtubule factors is intriguing but unexplained mechanistically.
  - **Why it matters** The functional claim is the most biologically significant part of the study. If the link between CDK2 phosphorylation and the phenotypes is not rigorously established, the mechanistic narrative collapses.
  - **Resolution test** Identify the specific residue, show that the mutation abrogates phosphorylation in cells, and demonstrate that the phenotypes are rescued by a phospho-mimetic mutant or by restoring phosphorylation.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Abstract wording
  - **Evidence pointer** Abstract, Summary section
  - **Issue** The abstract states that ARID1A has roles in DNA damage response, replication, splicing, translation, and cell plasticity, but these are not connected to the findings. This breadth is distracting and may overstate the scope of the study.
  - **Required correction** Focus the introductory context on the aspects directly relevant to the reported interactions and functional data.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** Use of the term "novel"
  - **Evidence pointer** Abstract, Summary section
  - **Issue** The term "novel" is used for TOX4, CDK2, and CCNA2, but it is unclear whether these have been reported elsewhere in other contexts or for other proteins. The claim of novelty should be qualified.
  - **Required Correction** Clarify that these are novel for ARID1A specifically, and cite any prior evidence of these interactions in other systems.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Resource availability
  - **Evidence pointer** Abstract only; location not provided
  - **Issue** The abstract describes the work as providing a "useful resource" but does not state whether the peptide array data, raw mass spectrometry files, or analysis scripts will be deposited in a public repository.
  - **Required Correction** State data availability for the interaction map and raw proteomics data.
- **Technical failings that need to be addressed before the case is established** R1-M1 and R1-M2 are blocking. The novel interactor claims and the functional link to CDK2 phosphorylation require validation and quantitative support. The methodological details of the PRISMA screen must be provided to assess data quality. Without these, the central conclusions are unsupported.
- **Assessment against Nature-style criteria**  
  *Originality*: The approach is conceptually original in applying peptide-array based interaction screening to a large intrinsically disordered protein like ARID1A, and the potential to map interfaces at residue resolution is a meaningful advance. However, the abstract does not demonstrate that this originality translates into new biological insight beyond a list of candidates.  
  *Scientific importance*: ARID1A is a major cancer gene and a core component of a key chromatin regulator, so new interaction data and a regulatory mechanism would be of high importance. The CDK2 link is potentially significant but is not yet established.  
  *Interdisciplinary readership*: The work would appeal to chromatin biology, proteomics, and cancer research communities. The technical aspects may interest method developers. The abstract is written in a way that is broadly accessible.  
  *Technical soundness*: Cannot be assessed from the abstract. The absence of any quantitative data, controls, or methodological detail precludes evaluation.  
  *Readability for nonspecialists*: The abstract is clearly written and the logic is easy to follow, though some terms such as PRISMA and cBAF are used without full explanation. The functional claims are stated too strongly relative to the evidence shown.
- **Recommendation posture** Currently not established from the provided evidence. The study has clear potential and the technical concept is attractive, but the abstract alone does not provide sufficient support for the novel interactor claims or the functional mechanism. A supportive stance would require the full manuscript to address the blocking concerns on validation, controls, and methodological transparency.

## Risk / unsupported claims

- The identification of TOX4, CDK2, and CCNA2 as novel ARID1A interactors is unsupported without validation data.
- The claim that mutation of a CDK2 phosphorylation site causes altered gene expression and proliferation defects is unsupported without identification of the residue, evidence of phosphorylation loss, and causal demonstration.
- The claim that PRISMA detects interactions not detectable by traditional affinity purification is unsupported without a direct comparative experiment.
- The assertion that the PRISMA assay recapitulates known BAF subunit binding and YAP1 interaction is plausible but not verifiable from the abstract.
- The general statement that ARID1A has roles in DNA damage response, replication, splicing, translation, and cell plasticity is presented as context but is not tied to the findings and is not assessed here.