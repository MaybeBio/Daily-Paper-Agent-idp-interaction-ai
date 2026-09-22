## Review setup
- **Input scope** Full manuscript text (title, abstract, introduction, methods, results, discussion, acknowledgments) as provided by the user. No supplementary files, figures, tables, or raw data were included.
- **Assessment boundary** The review is limited to the scientific content, methodology, and claims presented in the provided text. No external literature verification or data reanalysis was performed.
- **Shared manuscript claim summary** The authors report the crystal structure of the ParESO-CopASO toxin-antitoxin complex from Shewanella oneidensis, showing an open V-shaped heterotetramer. They propose that ParESO binding induces folding of the intrinsically disordered C-terminal domain of CopASO, that ParESO acts as a de-repressor of TA operon transcription at a 1:1 toxin:antitoxin ratio, and that His91 in ParESO is essential for toxicity.
- **Visible evidence base** Text descriptions of crystallographic data collection and refinement statistics (Table 1 referenced but not shown), gel filtration chromatography results (Figure 1b referenced), ITC binding data (Figure 4 referenced), cell toxicity assays (Figures 2c, 3e, S3 referenced), and structural comparisons (Figures 1, 2, 3, S1, S2 referenced).
- **Missing materials affecting confidence** All figures, tables, supplementary materials, and raw data are absent. Refinement statistics, ITC thermograms, gel filtration chromatograms, Western blot data, and structural coordinates are not available for independent assessment.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant question in the field of toxin-antitoxin systems, specifically the molecular basis of neutralization and transcriptional autoregulation in the ParESO-CopASO pair. The structural determination of the complex is a valuable contribution, and the identification of key residues through mutagenesis is informative. However, the evidence presented in the text alone is insufficient to fully support several central claims, particularly regarding the de-repressor mechanism and the conformational changes inferred from ITC data. The moderate resolution of the crystal structure (3.80 Å) and the lack of direct binding assays between ParESO and DNA or between the complex and DNA at varying ratios limit the strength of the conclusions. The manuscript is technically sound in its experimental design but requires additional data and clearer presentation to establish the proposed regulatory model.
- **Who would be interested in the results, and why** Researchers studying bacterial toxin-antitoxin systems, particularly type II TA modules, will find the structural and functional characterization of ParESO-CopASO of interest. The work also has relevance for those investigating prophage maintenance and bacterial stress responses. The identification of specific residues involved in toxicity and neutralization may inform future studies on TA system engineering or antimicrobial development.
- **Major strengths** The study provides the first structural characterization of the ParESO-CopASO complex, revealing a novel open V-shaped architecture. The combination of structural, biophysical, and cellular assays is appropriate for addressing the research questions. The identification of His91 as a critical residue for toxicity is a clear and testable finding. The discussion of conditional cooperativity in the context of this system is thoughtful and places the work in a broader framework.
- **Major Concerns** The following concerns are identified.
- **Minor Comments** The following comments are identified.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4.
- **Assessment against Nature-style criteria** Originality: The structural determination of a new TA complex is original, though the overall architecture is not unprecedented. Scientific importance: The work contributes to understanding TA system regulation, but the mechanistic claims require stronger evidence. Interdisciplinary readership: The topic is of interest to microbiologists and structural biologists, but the broader impact is limited. Technical soundness: The experimental approaches are appropriate, but the resolution and missing controls weaken the conclusions. Readability for nonspecialists: The manuscript is generally clear, but some sections assume familiarity with TA system nomenclature and structural biology terminology.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the de-repressor mechanism and the interpretation of ITC data.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors claim that ParESO acts as a de-repressor of TA operon transcription at a 1:1 toxin:antitoxin ratio, based on ITC data showing reduced DNA-binding affinity of the complex compared to CopA alone.
- **Evidence pointer** Section 3.6, Figure 4
- **Concern** The ITC experiments were performed with a single ratio of toxin to antitoxin (1:1, as inferred from the complex structure). The claim that ParESO acts as a de-repressor is based on the observation that the complex has lower DNA-binding affinity than CopA alone. However, no experiments were performed at other toxin:antitoxin ratios, which would be necessary to establish a de-repressor role. In many type II TA systems, the toxin can act as a co-repressor at low ratios and a de-repressor at high ratios. The authors acknowledge this limitation in the Discussion but still present the de-repressor conclusion as a key finding.
- **Why it matters** The proposed regulatory mechanism is central to the manuscript's conclusions. Without data at multiple ratios, the claim that ParESO functions as a de-repressor is not fully supported. The interpretation of the ITC data is also complicated by the fact that the complex is a heterotetramer, and the stoichiometry of DNA binding is not clearly established.
- **Resolution test** The authors should perform ITC or electrophoretic mobility shift assays with varying toxin:antitoxin ratios (e.g., 0.5:1, 1:1, 2:1) to demonstrate the effect of ParESO on CopA DNA binding. Alternatively, they should temper the claim and present the data as preliminary evidence consistent with a de-repressor role.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The crystal structure of the ParESO-CopASO complex was determined at 3.80 Å resolution with R/Rfree of 0.29/0.30, and the authors state that the electron density, especially for the C-terminus of CopASO, could be well traced.
- **Evidence pointer** Section 3.1, Table 1
- **Concern** The resolution of 3.80 Å is relatively low for a detailed structural analysis, particularly for making claims about specific side-chain interactions and conformational changes. The Rfree value of 0.30 is high, which may indicate overfitting or poor model quality. The authors do not provide details on the quality of the electron density maps, the number of restraints, or the validation metrics beyond the R-factors. The claim that the C-terminus of CopASO is "well traced" is difficult to assess without seeing the maps.
- **Why it matters** The structural model is the foundation for the proposed mechanism of neutralization. If the model is not reliable, the conclusions about specific interactions (e.g., salt bridges, hydrophobic contacts) and the induced-fit conformational change are weakened.
- **Resolution test** The authors should provide a more detailed validation of the structure, including electron density maps for key regions, Ramachandran statistics, and a discussion of the limitations of the resolution. If possible, higher-resolution data should be collected or the claims should be moderated to reflect the uncertainty.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors state that ParESO binding induces the intrinsically disordered C-terminal domain of CopASO to fold into a partially ordered conformation, based on the crystal structure.
- **Evidence pointer** Section 3.2, Figures 1c, S1
- **Concern** The claim of induced folding is based solely on the crystal structure of the complex. No structural or biophysical data on the free CopASO C-terminal domain are presented to demonstrate that it is disordered in solution. The authors reference a previous NMR study (reference 20) that indicated the C-terminal domain is intrinsically disordered, but this is not directly shown in the current work. The comparison between the free and bound states is therefore indirect.
- **Why it matters** The induced-fit mechanism is a key aspect of the proposed model for neutralization. Without direct evidence of the conformational change, the claim is speculative.
- **Resolution test** The authors should provide experimental evidence, such as circular dichroism, NMR, or small-angle X-ray scattering, showing that the C-terminal domain of CopA is disordered in solution and becomes more ordered upon ParESO binding. Alternatively, they should clearly state that this is a hypothesis based on the structure.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors conclude that His91 in ParESO is essential for toxicity based on cell toxicity assays with alanine mutants.
- **Evidence pointer** Section 3.5, Figures 2c, S3
- **Concern** The cell toxicity assays are described only briefly. The authors state that H91A showed a significantly higher growth rate, but no quantitative data are provided. It is unclear whether the expression levels of the mutant proteins were comparable to the wild-type, as Western blot analysis is mentioned in the methods but the results are not shown. Without confirming equal protein expression, the observed loss of toxicity could be due to reduced protein stability or expression rather than a specific functional role of His91.
- **Why it matters** The identification of His91 as a key residue is a central finding. If the effect is due to protein instability, the conclusion would be incorrect.
- **Resolution test** The authors should show the Western blot data confirming equal expression of wild-type and mutant proteins. They should also provide quantitative growth curves or statistical analysis to support the claim of reduced toxicity.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract states that ParESO acts as a "de-repressor" but does not provide the context of the toxin:antitoxin ratio. This could be misleading to readers.
- **Required correction** Clarify in the abstract that the de-repressor role is proposed based on the 1:1 complex structure and ITC data, and that further studies are needed.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, Section 2.4
- **Evidence pointer** Section 2.4, location not provided
- **Issue** The ITC experimental details are incomplete. The buffer composition, temperature, and the concentration of DNA and protein are not specified. The fitting model is mentioned as "one-site" but no details on the fitting parameters or errors are given.
- **Required correction** Provide full experimental conditions for the ITC experiments, including buffer, temperature, concentrations, and the number of replicates.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, Section 3.4
- **Evidence pointer** Section 3.4, location not provided
- **Issue** The description of the hydrophobic contacts and salt bridges is detailed but difficult to follow without the figures. The authors should consider a summary table of key interactions.
- **Required correction** Add a table summarizing the key intermolecular interactions (hydrogen bonds, salt bridges, hydrophobic contacts) with residue numbers and distances.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion
- **Evidence pointer** Section 4, location not provided
- **Issue** The discussion of conditional cooperativity is brief and does not fully explore alternative models or the implications of the findings for other TA systems.
- **Required correction** Expand the discussion to consider alternative regulatory mechanisms and the broader implications for type II TA system function.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Language
- **Affected element** Throughout
- **Evidence pointer** Throughout, location not provided
- **Issue** There are minor grammatical errors and awkward phrasings (e.g., "the to the above 25 bp DNA fragment" in Section 3.6).
- **Required correction** The manuscript should be carefully proofread for language and grammar.

## Risk / unsupported claims
- The claim that ParESO acts as a de-repressor at a 1:1 toxin:antitoxin ratio is not fully supported by the data, as only a single ratio was tested.
- The claim that ParESO binding induces folding of the CopASO C-terminal domain is based on indirect evidence and requires direct biophysical confirmation.
- The identification of His91 as essential for toxicity is not fully supported without confirmation of equal protein expression levels.
- The structural model at 3.80 Å resolution may not be of sufficient quality to support detailed mechanistic claims about specific interactions.
- The functional significance of the open V-shaped structure for prophage maintenance is speculative and not directly tested.