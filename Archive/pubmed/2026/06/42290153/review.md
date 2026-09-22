## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, conclusions, and supplementary figure references
- **Assessment boundary** Scientific content, methodological rigor, validity of claims relative to presented evidence, and clarity of presentation
- **Shared manuscript claim summary** The authors use well-tempered bias exchange metadynamics simulations to characterize the conformational ensembles of human and rat islet amyloid polypeptides in pure water and in the presence of glucose, glycerol, and sorbitol at 125, 250, and 500 mM. They report osmolyte- and concentration-dependent changes in secondary structure propensity, particularly reduced α-helical content in the amyloidogenic core of hIAPP, and interpret their results as evidence for a strong osmophobic effect with minimal direct protein-osmolyte interactions.
- **Visible evidence base** Main text figures 1-13, tables 1-7, supplementary figures S1 and S2 (referenced but not provided)
- **Missing materials affecting confidence** Supplementary figures S1 and S2 (convergence plots) were not provided; simulation trajectory data and input files are not available for independent verification; experimental validation data are absent

## Reviewer

- **Overall assessment** This manuscript presents a systematic computational investigation of how three stabilizing osmolytes modulate the conformational landscapes of hIAPP and rIAPP. The study addresses a relevant question in the context of type 2 diabetes and protein aggregation. The methodological approach using WT-BEMD is appropriate for exploring conformational ensembles of intrinsically disordered proteins. However, several concerns limit the strength of the conclusions. The reported changes in secondary structure are described as subtle, and the biological significance of these changes for aggregation propensity remains speculative. The claim of a strong osmophobic effect is supported by the lack of direct interactions, but the connection between the observed conformational changes and the proposed reduction in aggregation is not directly tested. The manuscript would benefit from clearer presentation of quantitative results and a more critical discussion of limitations.

- **Who would be interested in the results, and why** Researchers studying islet amyloid polypeptide aggregation, the molecular mechanisms of osmolytes on intrinsically disordered proteins, and computational approaches to protein conformational dynamics. The findings may also be of interest to those investigating therapeutic strategies for type 2 diabetes that target hIAPP aggregation, as well as computational chemists and biophysicists working on osmolyte-protein interactions.

- **Major strengths**
  - The study addresses a relevant and under-explored question regarding the molecular mechanisms of osmolytes on intrinsically disordered proteins
  - The use of WT-BEMD is appropriate for enhanced sampling of IDP conformational ensembles
  - The comparison between amyloidogenic hIAPP and non-amyloidogenic rIAPP provides a useful framework
  - Multiple complementary analyses (secondary chemical shifts, DSSP, SASA, H-bonding, RDFs) provide a comprehensive characterization
  - The inclusion of three different osmolytes at multiple concentrations allows for comparative assessment

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors claim that the addition of osmolytes resulted in "subtle changes in secondary structure propensity and content" and that for hIAPP there was "a general reduction in the likelihood of α-helical conformations, particularly in the amyloidogenic core, suggesting a molecular mechanism for reduced aggregation in the presence of osmolytes."
- **Evidence pointer** Results sections on secondary Cα chemical shifts and DSSP; Figures 3-6; Tables 2-7
- **Concern** The reported changes in secondary structure are described as subtle, yet the authors use these changes to propose a molecular mechanism for reduced aggregation. The magnitude of the reported changes is not quantified in a way that allows the reader to assess their significance. For example, the DSSP data in Tables 2-7 report percentage point changes, but no statistical uncertainties or effect sizes are provided. The claim that reduced α-helical propensity in the amyloidogenic core suggests reduced aggregation is speculative, as the relationship between monomeric α-helical content and aggregation propensity is not established. The authors themselves note that the amyloidogenic core is not part of the cross-β structure in fibrils, which complicates the interpretation.
- **Why it matters** The central conclusion of the manuscript rests on the interpretation that osmolyte-induced conformational changes in the monomer are relevant to aggregation. Without quantitative assessment of the magnitude of these changes and a clear mechanistic link to aggregation, the significance of the findings remains unclear.
- **Resolution test** Provide quantitative measures of the changes in secondary structure content with associated uncertainties. Discuss the relationship between monomeric conformational preferences and aggregation propensity more critically, or provide additional analysis linking the observed changes to known aggregation-relevant conformations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological validation
- **Claim pointer** The authors state that "convergence of the free energy calculations was assessed using the METAGUI 3.0 plugin in VMD, by comparing free energy surfaces at 20 ps intervals" and that simulations were extended by 300 ns beyond convergence.
- **Evidence pointer** Methods section; Figures S1 and S2 (not provided)
- **Concern** The convergence assessment is described only briefly, and the supplementary convergence plots were not available for review. The statement that free energy surfaces were compared at 20 ps intervals is unclear, as this would represent an extremely short time interval for assessing convergence. It is not clear how the convergence time point was determined, how many replicas were used per system, or what the total simulation lengths were. Without this information, the reliability of the free energy surfaces and the derived observables cannot be properly evaluated.
- **Why it matters** The validity of all reported results depends on adequate sampling and convergence of the WT-BEMD simulations. Insufficient sampling of IDP conformational space is a common pitfall that can lead to misleading conclusions.
- **Resolution test** Provide a detailed description of the convergence assessment methodology, including the criteria used to determine convergence, the total simulation time per replica, and the number of replicas per system. Make the convergence plots available for review.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretive overreach
- **Claim pointer** The authors conclude that "the potential osmolyte-mediated reduction in aggregation-prone conformations in IDPs such as hIAPP may disrupt early aggregation and offer a potential strategy to mitigate hIAPP cytotoxicity."
- **Evidence pointer** Discussion and Conclusions sections
- **Concern** The study only examines monomeric hIAPP and rIAPP. The connection between monomeric conformational ensembles and aggregation propensity is indirect. The authors acknowledge this limitation in the final paragraph of the discussion, but the abstract and conclusions present the aggregation-related implications more strongly than the evidence supports. The claim that reduced α-helical propensity would lead to reduced aggregation is not directly tested and is in tension with some literature suggesting that α-helical intermediates can be on-pathway to amyloid formation.
- **Why it matters** Overstating the implications of the findings could mislead readers about the therapeutic potential of these osmolytes and the mechanistic understanding provided by this study.
- **Resolution test** Soften the language in the abstract and conclusions regarding aggregation implications, or provide additional analysis or discussion that more carefully considers alternative interpretations of the relationship between monomer conformation and aggregation.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The authors state that "Data (simulation trajectories and input files) will be made available upon request."
- **Evidence pointer** Data Availability Statement
- **Concern** The data availability statement is vague. For a computational study, it is standard practice to provide at least the input files, parameter files, and analysis scripts in a public repository to ensure reproducibility. "Available upon request" is insufficient for a modern computational publication, particularly given the complexity of WT-BEMD simulations.
- **Why it matters** Reproducibility is a core requirement for computational studies. Without access to the input files and analysis scripts, other researchers cannot verify or build upon these results.
- **Resolution test** Deposit input files, topology/parameter files, and analysis scripts in a public repository (e.g., Zenodo, Figshare) and provide a DOI or accession number.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section, force field description
- **Evidence pointer** Methods section, "Initial Structures and Simulation Setup"
- **Issue** The authors state that the Amber99SB*-ILDNP force field was used but do not specify the version of the force field parameters or provide a citation for the specific implementation. Additionally, the use of TIP4PD water model is mentioned but the rationale for this choice over other water models is not provided.
- **Required correction** Add appropriate citations for the force field and water model, and briefly justify the choice of TIP4PD for IDP simulations.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Results section, DSSP analysis
- **Evidence pointer** Tables 2-7
- **Issue** The tables report changes in secondary structure content as percentage points, but the text does not consistently reference specific values from the tables. This makes it difficult for the reader to follow the narrative and verify the claims.
- **Required correction** Reference specific values from the tables in the text when describing the changes in secondary structure content.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods section, H-bonding analysis
- **Evidence pointer** Methods section, "Structural and Interaction Analysis"
- **Issue** The criteria for defining a hydrogen bond (distance and angle cutoffs) are not specified. The authors mention an angle cutoff of 37 degrees and a distance cutoff of 0.35 nm, but the donor-acceptor definition and whether the angle is the H-D-A angle or D-H-A angle is not fully clarified.
- **Required correction** Provide a complete description of the hydrogen bond definition, including the specific atoms involved and the exact geometric criteria.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section, RDF analysis
- **Evidence pointer** Figures 11-12
- **Issue** The description of the RDF analysis in the text is brief, and it is not entirely clear which atoms were selected for the calculation of the hydrophobic RDFs. The authors mention "non-polar C atoms" but do not specify whether all carbon atoms in hydrophobic side chains were included or only specific ones.
- **Required correction** Clarify the atom selection criteria for the RDF calculations and describe how the coordination number was computed.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that "the addition of osmolytes resulted in subtle changes in secondary structure propensity and content" but does not provide any quantitative information. Given that the changes are described as subtle, it would be helpful to include a representative quantitative result in the abstract.
- **Required correction** Consider including a specific quantitative finding in the abstract to strengthen the impact of the work.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion compares the simulation results with experimental studies on osmolyte effects on IDP aggregation, but does not discuss potential limitations of comparing simulation results at the monomer level with experimental aggregation assays that involve multiple peptides and longer timescales.
- **Required correction** Add a brief discussion of the limitations of comparing monomer-level simulation results with experimental aggregation data.

## Risk / unsupported claims
- The claim that reduced α-helical propensity in the amyloidogenic core of hIAPP "suggest[s] a molecular mechanism for reduced aggregation" is not directly supported by the data, as the study does not measure aggregation.
- The statement that the observed effects "may disrupt early aggregation and offer a potential strategy to mitigate hIAPP cytotoxicity" is speculative and goes beyond the evidence presented.
- The claim of "a strong osmophobic effect" is supported by the lack of direct protein-osmolyte interactions, but the manuscript does not provide a quantitative measure of osmophobic exclusion (e.g., transfer free energies or preferential binding coefficients).
- The assertion that "changes in secondary structure propensity and content in monomers upon the addition of osmolytes are likely to impact their self-aggregation" is presented as a reasonable inference but is not tested.
- The convergence of the WT-BEMD simulations cannot be fully assessed from the provided materials, as the supplementary convergence plots were not available.